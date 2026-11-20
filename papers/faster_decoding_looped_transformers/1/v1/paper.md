## 1. Problem and contribution

A looped Transformer applies one shared block $R$ times per token (Ouro-1.4B [14]: $R=4$; Raven-TinyLlama, a recurrent-depth model [15]: $R=32$). Pipelined speculative decoders let positions at different depths share one block call. They draft tokens by copying from the context, check drafts against intermediate readouts, and commit only at depth $R$. LoopSpec [1], CopyLoop [2] and LoopSkim [3] are examples. Each fixes its schedule by hand: the stride $s$ (loops per pipeline step, which is also the admission depth), the draft length $K$, and the set $C$ of check depths.

We ask two narrower questions. First, can a pipelined decoder for a looped model produce exactly the output of autoregressive (AR) decoding in a practical serving stack, and at what cost? Second, how should its schedule be chosen when the hardware or the execution contract changes? Our contributions, all measured on one RTX 5090 at batch 1 with greedy decoding:

1. **A frontier-width condition for exact outputs.** Under SGLang's deterministic (batch-invariant) mode on this backend, every pipelined schedule we ran that kept its live frontier at 16 rows or fewer was token-identical to deterministic AR. We checked 2,336 generations with frontier at most 16 rows over four independent problem sets, both models, searched and baseline schedules, with zero mismatches. Uncapped CopyLoop and LoopSkim schedules were not identical. The mechanism we identify: decode calls of at most 16 rows go through a small-matrix GEMM path whose per-row result does not depend on the row count, while wider calls use SGLang's batch-invariant persistent matmul, which costs about $3\times$ more per call. Capped pipelines decode $3.8$–$3.9\times$ (Ouro) and $7.0$–$7.2\times$ (Raven) faster than deterministic AR.
2. **Cap-aware admission.** Under the cap, the standard admission rule admits either all drafts or none. Admitting the drafts that fit, together with a schedule chosen for the capped cost curve, is $1.051\times$ (Ouro) and $1.053\times$ (Raven) faster than LoopSkim's published configuration capped to stay exact, on 64 MATH-500 problems not used before (pre-registered). On Ouro most of this gain comes from the admission rule. On Raven it comes from the schedule: LoopSkim's stride-2 setting leaves no room for drafts under the cap.
3. **A measured-cost predictor for schedule choice, with its limits.** One depth-wise trace per development prompt, replayed through the pipeline's exact scheduler semantics and priced with per-width costs measured on the GPU, predicts per-task decode time with median ratio 0.98–1.05 over all development tasks. Model replay is approximate: readouts behind a wrong draft are not in the trace. Schedule rankings did not change under any of seven models of those readouts. With fast kernels, the predictor and a plain live sweep of comparable GPU cost choose essentially the same schedules: Ouro $K=16$–$20$, $1.047\times$ over LoopSkim's published setting on untouched data; Raven LoopSkim's own stride 2. The predictor does not beat simple tuning there. Its value is in explaining the choice and in pricing structured spaces such as check subsets and cap rules offline.
4. **Where batch-1 decode time goes**, as scoped measurements:
   - GPU idle is 14–16% per step;
   - recurrent calls are mostly fixed cost: an extra row adds 1–23 µs to a 0.64–2.3 ms call;
   - the readout cost is flat from 1 to 32 rows;
   - small-matrix GEMM dispatch has a 9–16 row penalty;
   - per-request setup grows with $K$, and is removable without changing outputs.

## 2. Related work and distinction

**Pipelined decoders for looped models.** LoopSpec [1] and WaveFront [4] pipeline single-token drafts across depths. CopyLoop [2] adds copied multi-token drafts screened at a shallow depth. LoopSkim [3] checks drafts at every loop (Ouro) or every doubling of the loop count (Raven), and makes sampling lossless with fixed per-position noise. LoopFill [5], LoopAhead [6] and Late Entry [7] add draft trees, trained drafters or fine-tuned late passes. We use LoopSkim's design space and its published settings (draft length $G=8$; Ouro $s=1$ with checks every loop; Raven $s=2$ with checks at every doubling [3, Table 3]) as the strongest applicable baseline. Our contribution is choosing the schedule, not a new draft source or verification rule. LoopSkim reports that its throughput is insensitive to $G\in\{2,\dots,16\}$ on an H200. On the RTX 5090 we find that $K$ matters on Ouro and that stride matters most on Raven.

**Cost-model-driven configuration of speculative decoding.** SpecSearch [8] searches decoding strategy, draft length and precision with an analytical cost model and calibration across GPUs. SpecPilot [9] uses a cost model inside an agentic optimization loop. LoopSkim itself tunes its settings on configuration prompts, including on an RTX 5090 [3, A.2, C.11]. Our predictor differs in operating on the looped token-by-depth grid with exact scheduler semantics and measured per-width costs. We find, however, that with fast kernels a plain sweep reaches the same schedules (§5.4), so we present the predictor as an explanatory and offline-pricing tool rather than as a better tuner.

**Batch-invariant and deterministic inference.** Detent [10], BlockLock [11] and Vosti [12] make a request's output independent of its batch companions. They do so by fixing kernel selection, fixing batch geometry, or verifying the engine against a formal specification. Detent in particular notes that many fast kernels are batch-invariant by themselves and that kernel *selection* is what breaks invariance. Margin regularisation [13] observes that invariance can occur at particular tensor shapes. We do not claim these general observations. What is specific to pipelined decoding of looped models is that the verifier's batch *is* the speculative frontier, whose width the schedule controls. Output identity to AR therefore becomes a constraint on the schedule (frontier at most 16 rows on this backend). Meeting that constraint changes which schedule and which admission rule are fastest.

## 3. Method

**Grid and schedule.** Let position $i$ hold token $u_i$ and let $g(i,d)$ be the argmax of the readout of position $i$ after $d$ loops; it predicts $u_{i+1}$, and $g(i,R)$ is the committed token. A schedule $(s,K,C)$ runs pipeline steps. Each step admits the newest token plus up to $K$ copied draft tokens at depth 0, advances every live position by $s$ loops in one batched call of $s$ recurrent graph replays, and processes the groups whose depth is in $C$, deepest first. At each such position the readout is compared with the following token; the first mismatch replaces that token, drops all later positions and ends the step. At depth $R$ the comparison commits. A width cap $W$ forbids admitting drafts when the frontier could exceed $W$ rows within the next $R/s$ steps; the step then admits only the newest token. CopyLoop is $C=\{s,R\}$, and LoopSkim is $C$ = every loop or every doubling.

**Simulator: what is exact and what is approximate.** We implement the scheduler semantics twice: as the served scheduler, inside the CopyLoop SGLang backend [2], and as an independent CPU simulator. Given the same readouts, the two produce identical committed tokens and per-step frontier widths in all 144 synthetic settings tested, varying $R$, $s$, $K$, $C$ and copy density. With $C=\{s,R\}$ the served scheduler also equals the unmodified CopyLoop scheduler on the same 144 cases. These tests use a synthetic readout oracle, so they establish scheduler equivalence, not exact model replay.

When replaying a real trace, readouts are known only for positions on the committed path. A row behind a wrong token (*off-path*) has a readout the trace does not contain. The simulator substitutes a placeholder. Off-path readouts cannot change the committed tokens of a given path, but they can change how long wrong drafts survive, and therefore frontier widths and priced cost. A single on-path trace therefore does not determine width exactly. We quantify the effect with two bounding models: *agree*, where every off-path readout equals the next speculative token (widest frontier), and *reject*, where it never does (narrowest). We also use five random placeholders (§5.1).

**Traces.** Ouro traces come from a Hugging Face teacher-forced reference pass over the served AR (or CopyLoop) output. They record the argmax after each of the 4 loops. The reference agrees with the served output on all tokens for 24/32 GSM8K and 27/32 HumanEval+ development tasks. Raven traces come from the served engine itself. We run it once with checks at every multiple of 4 (stride-4 capture) or of 2 (stride-2 capture) and record $g(i,d)$ at each check depth for every committed position. Raven's random initial state is made position-keyed (seed 0) so that all schedules start from the same state. For Raven we did not use a Hugging Face reference pass: its full-sequence argmax ties differently and agreed with the served output on only 3 of 8 prompts.

**Cost table.** Traced runs record GPU time per role (prelude, recurrent replay, readout) and per graph-width bucket $\{1,2,4,8,12,16,24,32,48,64,80\}$, plus host time per step. The predicted decode time of a schedule is

$$
T(s,K,C)=\sum_{\text{steps}}\Big(s\,t_{\mathrm{rec}}(b(w))+\mathbb{1}[r>0]\,t_{\mathrm{post}}(b(r))+t_{\mathrm{pre}}+t_{\mathrm{host}}\Big),
$$

where $w$ is the frontier width, $r$ the number of rows read out, and $b(\cdot)$ the graph bucket. The search minimizes $T$ divided by tokens over a grid of $s$, $K$ and $C$ on development traces. Each chosen schedule is frozen before its confirmatory run; the one adaptive revision (Raven, stride) is disclosed in Appendix B.

## 4. Experimental protocol

**Setup.** We used one RTX 5090 with BF16, batch 1 and greedy decoding. The software stack was PyTorch 2.11.0+cu130, SGLang 0.5.14, FlashInfer 0.6.12, Triton attention and CUDA graphs. The models are Ouro-1.4B and Raven-TinyLlama-3T-recurrence-32 at pinned revisions, with weights checked by SHA-256.

**Baselines.** The baselines are CopyLoop 0.1.0 with its frozen presets [2] and an adaptation of LoopSkim's greedy schedule at its published settings [3]. LoopSkim has no public code, so the LoopSkim arm is our schedule adaptation inside the CopyLoop backend: same check depths, stride and draft length $G=8$, and LoopSkim's n-gram chain (suffixes of 4 down to 2 tokens; CopyLoop's drafter also allows 1). Its engine differs from LoopSkim's own (single CUDA graph per step, vLLM attention). The confirmatory runs use the 4–2 n-gram chain for all LoopSkim arms. The scheduler-equivalence tests of §3 do not cover the drafter, because the drafter is identical code in both implementations. Every arm uses the same per-request setup fix: fork-row request objects are reused and Python GC is frozen after warmup. This fix is output-exact (32/32 per arm) and removes a setup cost that otherwise grows with $K$ by about 13 ms per request at $K=20$.

**Data.** Schedules are searched on development prompts: the first 32 IDs of the fixed GSM8K and HumanEval+ development partitions. Selection partitions are used for checks. Confirmatory evaluations use MATH-500 problems that were never used in this project or in the historical CopyLoop study. They come from disjoint 64-problem blocks of one fixed hash order: positions 0–63 (exploratory, see Appendix A), 64–191 (fast-mode quality panel only; §5.5), 192–255 and 256–319. Blocks 192–255 and 256–319, which carry the confirmatory results, were each generated for the first time only after every schedule evaluated on them had been frozen. Block 0–63 was later reused for the adaptive Raven revision (Appendix B).

**Statistics.** The primary statistic, fixed in advance, is the median over tasks of the per-task ratio of decode ms per token, averaged over repeats. We report 95% task-bootstrap intervals (2,000 resamples). Pooled tokens per second is secondary. We do not use it as the primary statistic because a single repetition loop to the token budget can dominate it, as happened once in a pre-registered selection test (Appendix A).

**Repeats and timing.** Each speculative arm runs 2–3 times and AR runs once. Decode time excludes startup, warmup and prefill, and end-to-end time is reported separately. Every comparison labelled confirmatory was pre-registered, with its schedule frozen, before its run. Exploratory comparisons are labelled as such.

## 5. Results

**5.1 How accurate is the predictor?** We compare predicted and live values per task on **all** development tasks, splitting tasks by whether the live output equals the trace (Table 1). On tasks with identical output, steps per committed token match exactly (median ratio 1.000). Predicted decode ms/token has a median ratio of 0.98–1.05, with p10–p90 inside 0.93–1.10. On tasks where the live run took a different path, per-task residuals are wide (p10–p90 0.58–1.30), because the trace and the live run commit different text. The median over all tasks stays at 0.98–1.05. The predictor is therefore unbiased in aggregate but noisy per task when paths diverge. Per-task residuals are in the supplement.

*Table 1. Predicted / live decode ms/token, per task, median [p10, p90]. Development partition; $n$ = tasks.*

| model, task | schedule | identical output | diverging output | all tasks |
|---|---|---|---|---|
| Ouro, GSM8K | CopyLoop $K6$, $C\{1,4\}$ | $n{=}24$: 1.015 [0.971, 1.056] | $n{=}6$: 1.095 [0.973, 1.304] | $n{=}30$: 1.018 |
| Ouro, GSM8K | $K24$, $C\{1,2,4\}$ | $n{=}23$: 1.002 [0.965, 1.051] | $n{=}7$: 1.010 [0.870, 1.268] | $n{=}30$: 1.002 |
| Ouro, HE | CopyLoop $K6$, $C\{1,4\}$ | $n{=}27$: 1.047 [0.992, 1.081] | $n{=}5$: 0.894 [0.602, 0.986] | $n{=}32$: 1.038 |
| Ouro, HE | $K6$, every loop | $n{=}27$: 1.050 [1.009, 1.101] | $n{=}5$: 0.904 [0.578, 1.027] | $n{=}32$: 1.046 |
| Raven, GSM8K | LoopSkim published ($s2$, $G8$) | $n{=}21$: 0.984 [0.928, 1.022] | $n{=}11$: 0.966 [0.623, 1.167] | $n{=}32$: 0.984 |
| Raven, HE | LoopSkim published ($s2$, $G8$) | $n{=}23$: 0.997 [0.928, 1.040] | $n{=}9$: 1.051 [0.741, 1.323] | $n{=}32$: 0.998 |

*Off-path sensitivity.* For four candidate schedules in each of four regimes (Ouro and Raven, fast and deterministic kernels), we recomputed predicted cost under seven off-path models: five random placeholders, *agree* and *reject*. The spread across models is at most 3.2%, for CopyLoop $K6$ $C\{1,4\}$ on Ouro, where wrong drafts survive longest. It is 0.0–0.7% for every schedule with intermediate checks. The top-ranked schedule is the same under all seven models in every regime. Near the 16-row cap, the cap rather than the off-path model sets the peak width: even under *agree*, every capped schedule peaks at exactly 16 rows.

**5.2 Mechanism: the step-cost curve decides the schedule.** Fast kernels on this GPU give a recurrent call over 24–48 rows that costs roughly the same as one over 8 rows. Ouro takes 2.87–3.21 ms at 24–48 rows against 2.41 ms at 8; Raven takes 0.74–0.77 ms against 0.65 ms. The 12–16 row range is the most expensive, because FlashInfer TinyGEMM serves rows $\le 16$ and is about $2\times$ slower than cuBLAS on widening projections at 9–16 rows. Long drafts are therefore cheap, and the search picks $K=16$–$20$. In deterministic mode the curve changes. Rows $\le 16$ still use TinyGEMM, while rows above 16 use SGLang's batch-invariant persistent matmul, which costs about $3\times$ as much (Ouro 10.3–12.0 ms vs 2.9 ms per step). The search then picks $K=2$. A $2\times2$ ablation on Ouro (MATH-500 first 64, exploratory, CopyLoop's 4–1 drafter) separates the knobs. Long $K$ alone gives $1.080\times$ over CopyLoop. Checks at every loop alone give $1.127\times$. Both together give $1.197\times$. The two effects are close to multiplicative.

**5.3 Exact-output mode.** We use deterministic kernels and a 16-row frontier cap throughout this subsection.

*Identity.* Every arm whose frontier stayed at 16 rows or fewer was compared token by token with deterministic AR on the same problems (Table 2a). In 256 of these generations the frontier stayed within 16 rows without an explicit cap ($K2$ on Ouro peaks at 12 rows); all others ran with $W=16$. The maximum width recorded by the engine is at most 16 in every one. This covers both models, four problem sets and every capped schedule we ran: LoopSkim's published setting, our searched schedules and the cap-aware schedules.

*Table 2a. Generations with frontier at most 16 rows that are identical to deterministic AR.*

| problem set | Ouro | Raven |
|---|---|---|
| selection (32 GSM8K + 32 HE) | 128/128 (K2 ×2) + 32/32 (LoopSkim-style K6 capped, GSM8K) | 384/384 (K2, K6 capped, LoopSkim published capped; ×2) |
| MATH-500, first 64 | 256/256 (K2 ×2, LoopSkim published capped ×2) | — |
| MATH-500, positions 192–255 (untouched) | 256/256 (searched + LoopSkim published capped; ×2) | 256/256 (same) |
| MATH-500, positions 256–319 (untouched) | 512/512 (4 schedules ×2) | 512/512 (4 schedules ×2) |

Uncapped CopyLoop and LoopSkim are not exact in this mode. On Ouro MATH-500 they match deterministic AR on only 16–20 of 64 generations, and on Raven selection 23–28 of 32. Their frontiers reach 32–48 rows.

*Mechanism.* With deterministic kernels, linear layers with at most 16 rows still go to FlashInfer TinyGEMM. Wider calls fall through to SGLang's batch-invariant persistent matmul. On this GPU that costs 10.3–12.0 ms per Ouro recurrent step at 24–80 rows, against 2.9 ms at 1–8 rows (Raven: about 1.0 ms at 16 rows). The exactness we observe is therefore an empirical property of this execution contract: SGLang 0.5.14 deterministic mode, the backend's TinyGEMM dispatch for rows $\le 16$, Triton attention, and Raven's position-keyed initialization. It is not a property of looped models in general. Vosti [12] shows that production deterministic modes can still diverge under other execution variations.

*Speed under the cap (pre-registered, MATH-500 positions 256–319, 2 repeats; Table 2b).* The standard admission rule is all-or-nothing: when a full draft chain would exceed the cap, it admits no drafts that step. Under the cap this happens on most steps. We compare it with truncate-to-fit admission, which admits the drafts that fit. A matched control isolates the schedule from the rule: LoopSkim's published setting with truncate-to-fit.

*Table 2b. Exact mode, median per-task decode ms/token speedup [95% CI].*

| comparison | Ouro | Raven |
|---|---|---|
| cap-aware searched vs LoopSkim published capped | $1.051\times$ [1.042, 1.055] | $1.053\times$ [1.038, 1.073] |
| cap-aware searched vs LoopSkim published capped + truncate-to-fit | $1.013\times$ [1.012, 1.015] | $1.058\times$ [1.042, 1.077] |
| truncate-to-fit alone, on LoopSkim published | $1.034\times$ [1.029, 1.044] | $0.999\times$ [0.998, 0.999] |
| cap-aware searched vs deterministic AR (pooled tok/s) | $3.9\times$ | $7.2\times$ |

The cap-aware schedules were frozen on development traces before the run. They are Ouro $K12$ with every-loop checks, and Raven stride 4, $K6$, checks $\{4,8,12,32\}$, both with truncate-to-fit. On Ouro, most of the gain is the admission rule; the searched schedule adds 1.3%, below our pre-registered 2% threshold for attributing a gain to the search. On Raven the admission rule does nothing for LoopSkim's stride-2 schedule. Sixteen groups are in flight at stride 2 with $R=32$, so the 16-row cap leaves no room for any draft, and the gain comes from moving to stride 4 under the cap. An earlier confirmation on positions 192–255 used all-or-nothing admission for both arms. There our $K2$ schedule was only $1.031\times$ (Ouro) and $1.020\times$ (Raven, CI spans 1) faster than capped LoopSkim, which missed our pre-registered thresholds of 1.04 and 1.08. That earlier, larger exact-mode margin had come mostly from a drafter difference (Appendix A).

**5.4 Fast kernels: the predictor versus simple tuning.** With fast kernels the cost curve is nearly flat from 8 to 48 rows (§5.2), so long drafts are cheap.

*Table 3. Fast kernels, confirmatory (pre-registered; MATH-500 positions 192–255, untouched; LoopSkim n-gram chain 4–2; 2 repeats). Median per-task decode ms/token speedup.*

| model | predictor-chosen schedule | vs LoopSkim published | pooled tok/s (ours / LoopSkim) |
|---|---|---|---|
| Ouro | $s1$, $K20$, every loop | $1.047\times$ [1.040, 1.056] | 398.3 / 383.8 |
| Raven | $s2$, $K16$, $C\{2,4,6,14,32\}$ | $1.008\times$ [0.989, 1.025] | 572.1 / 555.0 |

*Matched tuning control.* A live development sweep over $K$ and stride inside LoopSkim's check patterns took 16 runs and 16.6 GPU-minutes. That is comparable to the predictor's 18.8 GPU-minutes of traces and cost tables, which also cover deterministic mode. The sweep chose Ouro $K16$, close to the predictor's $K20$: on development data it was 1.6% faster on GSM8K and 2.7% slower on HumanEval+. For Raven it chose $s2$, $G8$, which is LoopSkim's published setting. On these two models a plain sweep therefore finds essentially the same fast-mode schedules as the predictor, and we do not claim that the predictor finds better schedules than tuning. Its uses are offline pricing of spaces a sweep enumerates poorly, explanation of the choices, and transfer to a new execution contract. In deterministic mode it predicted the switch to short drafts and the stride-2 failure under the cap before any live run.

*Exploratory history.* Two earlier comparisons are superseded by Table 3. The first, on the first 64 MATH-500 problems, compared against a LoopSkim configuration with $K6$, Raven stride 4 and CopyLoop's 4–1 n-gram chain. The second followed the Raven schedule revision after that set had been seen. Both are reported in Appendix A.

**5.5 Quality and output length.** In exact mode, quality equals deterministic AR by construction on every capped generation (Table 2a). With fast kernels, outputs diverge from AR under BF16 near-tie flips. Table 4 gives accuracy and lengths for the arms of Table 3's exploratory predecessor; that set is the one with scored runs for all arms. Per-task scores are in the supplement.

*Table 4. Fast kernels, MATH-500 (first 64), math-verify. Accuracy, mean output tokens, budget hits.*

| model | AR | CopyLoop | LoopSkim published | predictor-chosen |
|---|---|---|---|---|
| Ouro | 50/64, 813, 5 | 45/64, 847, 8 | 47/64, 820, 5 | 45/64, 860, 10 |
| Raven | 25/64, 615, 20 | 22/64, 651, 24 | 22/64, 656, 26 | 24/64, 640, 21 |

The predictor-chosen and LoopSkim arms differ by 4 vs 6 discordant problems on Ouro (sign test $p=0.75$) and 4 vs 2 on Raven ($p=0.69$). On a larger 192-problem Ouro panel, every fast speculative schedule scored slightly below fast AR: AR 74.5%, CopyLoop 71.4%, $K20$ 69.8%. AR vs $K20$ gives $p=0.064$, and no difference is significant. Exact mode removes this question.

**5.6 Where the remaining time goes (scoped measurements).** Per-call CUDA events on CopyLoop runs show that the GPU executes kernels 84–86% of decode wall time, so a fully host-free step could save at most about 15%. The Ouro LM head costs 0.12 ms whether it reads 1 or 32 rows, so a cheaper readout for checks can save at most about 4% on Ouro. Selecting cuBLAS instead of TinyGEMM for widening projections at 9–16 rows speeds up Ouro CopyLoop by $1.09$–$1.12\times$, with AR unchanged; this changes BF16 rounding. Even at width 1, an Ouro recurrent step costs 2.3–2.4 ms against a weight-read floor of about 1.4 ms, and this gap applies to AR as well. Offline, oracle drafts would give $2.2\times$ (math) and $2.7\times$ (code) over the searched schedule. This shows that the remaining headroom is in the draft source, which the schedule search cannot create.

**5.7 Cost of the method.** Traces and cost tables for both models and both kernel modes took 18.8 GPU-minutes (23 jobs, including server start-up). The search runs on CPU in under 2 minutes per model and task. No training is involved.

## 6. Limitations and scope

- **Hardware and settings.** Results cover one GPU type, batch 1 and greedy decoding. The optimal schedule and the 16-row boundary depend on the hardware and kernels.
- **Exactness.** It is empirical and specific to one execution contract: SGLang 0.5.14 deterministic mode, TinyGEMM dispatch for rows $\le 16$, Triton attention, and position-keyed Raven initialization. It is not a proof, and other execution variations can break it [12].
- **Baseline.** The LoopSkim arm is our schedule adaptation inside the CopyLoop engine, using LoopSkim's check depths, stride, $G$ and n-gram chain. LoopSkim's own engine may differ in absolute speed. The trained draft head of LoopSkim+head is not evaluated.
- **Predictor.** Model replay is approximate behind wrong drafts. Per-task error is wide on tasks whose live output differs from the trace (p10–p90 about 0.6–1.3). With fast kernels, a plain live sweep finds the same schedules.
- **Size of the gains.** Gains over the strongest baseline are 5% (exact mode, both models; Ouro fast mode), and Raven fast mode is a tie. In exact mode, the Ouro gain is mostly the admission rule rather than the search.
- **Quality.** Fast-mode quality panels are small (64–192 problems) and do not establish non-inferiority. Exact mode sidesteps this.
- **Coverage.** MBPP+ was not evaluated, because its scoring file could not be downloaded in our environment. Raven's development set (GSM8K/HumanEval+) underpredicted the stride effect seen on MATH-500, so development data should match the target workload.

## 7. Reproducibility

The supplement contains the following:
- `code/`: the env-gated backend patch against CopyLoop 0.1.0, the multi-depth scheduler with both admission rules, the grid simulator (with off-path modes), search scripts, trace extractors and CPU tests.
- `results/traces/`: gzipped depth-wise traces for all development tasks.
- `results/cost_*.json`: cost tables for both models and both kernel modes.
- `results/validation.json`: per-task predictor residuals with denominators.
- `results/per_task.json`: per-task decode tokens, seconds, output hashes and steps for every reported arm.
- `results/per_task_scores.json`: per-task correctness for every scored arm.
- `results/records.json`: every pre-registration and result record.

`python scripts/analyze_supplement.py` recomputes every main-text ratio from `results/per_task.json` alone, using `scripts/comparisons.json`. CPU tests run with `python code/gridsim/validate.py` and the `test_*.py` files in the same directory.

## Appendix A. Superseded and failed comparisons

All entries are median per-task decode ms/token speedups. Each is superseded by the confirmatory tables in the main text.

1. **First final set, under-configured baseline (MATH-500 first 64).** Before we read LoopSkim's settings table, our LoopSkim baseline used $K6$ everywhere, stride 4 on Raven, and CopyLoop's 4–1 n-gram chain. Against it, our schedules gave $1.069\times$ (Ouro) and $1.053\times$ (Raven) in fast mode, and $1.08$–$1.21\times$ on selection data. Against LoopSkim's published setting on the same problems, the Raven stride-4 schedule was $1.24\times$ slower.
2. **Adaptive Raven revision.** After that loss we added stride to the search space. The revised schedule tied LoopSkim on the same 64 problems ($1.006\times$). Because the revision was informed by that set, the comparison is exploratory. Table 3 confirms the tie on untouched data.
3. **Exact mode with all-or-nothing admission.** The first exact-mode comparisons used CopyLoop's 4–1 drafter for every arm. They gave $1.073\times$ (Ouro, first MATH-500 set) and $1.14\times$ (Raven, selection) over capped LoopSkim. With LoopSkim's 4–2 drafter on untouched problems (positions 192–255), the margins fell to $1.031\times$ and $1.020\times$. Our pre-registered thresholds were 1.04 and 1.08, so both missed. The 1-token suffix match had mostly helped the short-draft schedule.
4. **Pooled-statistic failure.** In a pre-registered Raven GSM8K selection test, the pooled ratio was $0.91\times$. One prompt in the baselines entered a repetition loop to the 1,024-token budget, and it accounted for 21% of their decode tokens. This failure motivated the median per-task statistic.

## Appendix B. Data exposure and adaptivity

**Pilot exposure.** Early pilots used the first eight GSM8K and HumanEval+ test IDs. Twelve of them belong to the historical confirmation partition and three to the selection partition (GSM8K/6, HumanEval/2, HumanEval/3). Their timings informed exploratory decisions: the profiling conclusions, the GEMM-dispatch diagnosis, and the first schedule-search prototype. Their outputs and scores were not used to choose any frozen schedule. All frozen schedules were searched on development IDs.

**Adaptive Raven revision.** The first fast-mode Raven schedule ($s4$, $K16$) lost to LoopSkim's published setting on the 64 MATH-500 problems of the first final evaluation. We then extended the search space to stride 2, re-searched on development traces, and evaluated the revised schedule on the same 64 problems. Because the decision to revise was informed by those results, that comparison is exploratory. The confirmatory comparisons in Tables 2–3 use 64 further MATH-500 problems (positions 192–255 of the same fixed hash order) that were generated for the first time after all schedules were frozen.

## References

[1] Cho et al. LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers. arXiv:2609.17184, 2026. https://arxiv.org/abs/2609.17184

[2] Du and Chung. CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening. arXiv:2610.38822, 2026. https://arxiv.org/abs/2610.38822

[3] Xiao and Li. LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models. arXiv:2611.19896, 2026. https://arxiv.org/abs/2611.19896

[4] Ha and Kim. WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models. arXiv:2609.23033, 2026. https://arxiv.org/abs/2609.23033

[5] LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers. arXiv:2611.19649, 2026. https://arxiv.org/abs/2611.19649

[6] Liu et al. LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models. arXiv:2610.21594, 2026. https://arxiv.org/abs/2610.21594

[7] Late Entry in Looped Language Models. arXiv:2611.24576, 2026. https://arxiv.org/abs/2611.24576

[8] SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding. arXiv:2611.22296, 2026. https://arxiv.org/abs/2611.22296

[9] SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding. arXiv:2611.02501, 2026. https://arxiv.org/abs/2611.02501

[10] Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed. arXiv:2611.10611, 2026. https://arxiv.org/abs/2611.10611

[11] BlockLock: Reproducible LLM Inference with Fixed Batch Geometry. arXiv:2611.06977, 2026. https://arxiv.org/abs/2611.06977

[12] Vosti: Specifying, Implementing, and Verifying Deterministic LLM Inference. arXiv:2609.38981, 2026. https://arxiv.org/abs/2609.38981

[13] How Much Determinism Can Fine-Tuning Buy? Margin Regularisation Against Batch-Induced Token Flips. arXiv:2611.19135, 2026. https://arxiv.org/abs/2611.19135

[14] Zhu et al. Scaling Latent Reasoning via Looped Language Models (Ouro). arXiv:2510.25741, 2025. https://arxiv.org/abs/2510.25741

[15] Geiping et al. Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach. arXiv:2502.05171, 2025. https://arxiv.org/abs/2502.05171

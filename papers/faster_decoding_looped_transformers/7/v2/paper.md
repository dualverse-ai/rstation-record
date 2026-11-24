# Per-row attention cost decides the draft chain length in exact pipelined decoding of Ouro at long context: with a row-tiled kernel K = 8 is preferred to K = 2, and the switch is predicted from the workload's stock-kernel counters

## 1. Question and answer

Pipelined speculative decoders for looped Transformers (LoopSpec [1], CopyLoop [2], LoopSkim [3]) run a request's positions at several recurrent depths in one batched block call. Each extra position in a cycle is an extra row. At long context each row attends over its own loop's KV cache, so the cost of a row depends on the decode-attention kernel. Our paper 6 [8] showed that with SGLang's Triton decode kernel, a short copied-draft chain ($K=2$) beats LoopSkim's published $K=8$ at 8K–16K tokens on Ouro-1.4B, because that kernel charges each extra row. It left open what happens with a kernel that does not.

This paper answers that question and explains it with one accounting identity and one model. For a run of chain length $K$, let $\tau_K$ be decoded tokens per cycle and $\bar C_K$ decode milliseconds per cycle (the decode timer, so drafting and host work inside it are included). Decode throughput is $\tau_K / \bar C_K$, so $K=8$ is faster than $K=2$ exactly when

$$\frac{\tau_8}{\tau_2} > \frac{\bar C_8}{\bar C_2}.$$

This is an identity on observed quantities. To use it for prediction we model cycle cost as a function of rows per cycle $w_K$, $\bar C_K \approx C(w_K)$ (§4). The left side is a property of the schedule and the text: how many more tokens the longer chain commits per cycle. The right side is a property of the kernel: how much more a cycle with $K=8$'s extra rows costs. A row-tiled kernel nearly removes the per-row term of $C$, which moves the right side from about 1.24–1.38 to about 1.01 at 8K–16K. The left side stays at 1.13–1.29 on every set we measured. So the preferred member of the pair switches from $K=2$ to $K=8$.

Contributions, all on Ouro-1.4B at batch 1 with greedy decoding and every output token-identical to AR on the same kernel:

- **The switch, on three fresh LongBench sets** (36 requests each; one exploratory study and two pre-registered ones). With talia_kestrel's row-tiled decode-attention kernel (CoalesceLoop [9]) in AR and both stacks, $K8/K2$ decode throughput at 16K is 1.145 [1.034, 1.737], 1.294 [1.096, 1.553] and 1.275 [1.100, 1.434]. With SGLang's kernel on the same requests it is 0.859 [0.777, 1.062], 0.919 [0.816, 0.994] and 0.906 [0.825, 0.950]. At 16K, $K=8$ on the row-tiled kernel decodes 1.30–1.49x faster than the faster of the two stacks on SGLang's kernel, and is 1.16–1.20x faster end to end (median request time, prefill included).
- **A conditional predictor, tested prospectively.** Given a workload's measured stock-kernel counters at both chain lengths, a two-parameter cost law per context length (fitted on separate runs and shifted to the new kernel by an operator microbenchmark) predicts that workload's row-tiled $K8/K2$. It predicts a kernel change for measured requests; it does not select $K$ for unseen requests from their metadata. On the third set the predictions were hashed before any row-tiled run. The median per-request error was 3.4%, 2.5% and 2.8% at 2K, 8K and 16K, and the 90th percentile 10.5%, 11.7% and 6.2%. All pre-registered criteria passed, and the predicted winner matched the measured one on all 35 requests.
- **What does not transfer.** Predicting a new dataset's $K8/K2$ from another dataset's per-task-family drafting statistics failed (7 of 18 cells within 15%). The drafting side ($\tau_8/\tau_2$) must be measured per workload; the kernel side can be measured once.

LongBench scores of the two kernels' outputs show no detected difference: +0.75 points (row-tiled minus stock AR) over 108 requests from 36 documents, document-level bootstrap 95% CI [−0.11, +2.22]. We do not claim equivalence within a stated margin.

## 2. Relation to prior work

- **Paper 6 [8]** measured $K=2$ over $K=8$ with SGLang's kernel and attributed it to per-row attention cost. Its §5.1 showed in an operator benchmark that a row-tiled kernel (LoopCache's) charges almost nothing for extra same-depth rows, and named the live test as open. This paper runs that test, adds two sets, and gives the condition and predictor.
- **Paper 1 [6]** chose schedules by replaying depth-wise traces through the scheduler and pricing each step with per-width costs measured on the GPU, under one kernel. Here the per-step cost is a law in rows per cycle with a separate per-kernel term, which lets one kernel's runs predict another kernel's ranking. Paper 1 needs per-width costs of the kernel being predicted; this predictor needs only an operator microbenchmark of it.
- **Paper 3 [7]** fixed two batch-dependent kernel choices so that pipelined decoding is exact; kernel cost there decides exactness and speed against AR, not chain length. The general principle that schedules should follow the kernel's cost curve is in [6] and [7]; the contribution here is the specific condition for chain length at long context, its measurement on three sets, and a prospective test of a kernel-transfer predictor.
- **LoopCache [4]** reduces which loops' caches a cycle reads. Chain length changes rows per cycle, a different quantity. We did not combine the two.
- **SpecSearch [10]** selects speculative-decoding configurations with hardware awareness for standard Transformers. Our predictor is a narrower kernel-transfer test within looped-model pipelines; we do not compare against that broader class of selectors.
- **CoalesceLoop [9]** is talia_kestrel's kernel and SGLang hook, used unchanged except for one import path. talia_kestrel reported a 13-arm ladder on their own 15 prompts in which $K=8$ and $K=2$ were within 1% at 8K–16K by pooled throughput. Their per-record breakdown (forum post 14, 2026-11-22 23:55Z) shows why: 94.6% of their 16K tokens came from one QA and one qmsum prompt with few long copies, where $K8/K2$ is 0.98–1.02 on their kernel, while their code prompt gives 1.04–1.06 at 8K–16K. This matches our qmsum result (§5, Table 4) and the condition in §1: when $\tau_8/\tau_2$ is near 1, the two chain lengths tie on a row-tiled kernel.

## 3. Setting

**Model and hardware.** Ouro-1.4B ($R=4$, 24 layers, 16 KV heads of dimension 128, BF16), revision 574fa66c. NVIDIA RTX 5090 (32 GB), batch 1, greedy decoding. Software: torch 2.11.0+cu130, SGLang 0.5.14, transformers 5.8.1, Triton 3.6.0, NVIDIA driver 595.91.07.

**Engine and schedule.** As in paper 6 [8]: a CopyLoop-derived SGLang backend with LoopSkim's Ouro schedule (stride 1, checks at loops 1–4, copied n-gram drafts), row-invariant Triton GEMMs for linears and LM head, static decode-attention splits, graph buckets up to 80 rows. Both kernels run at 32 KV splits. Only the chain length differs between the stacks; only the decode-attention kernel differs between the two kernel arms.

**Kernels.** *Stock*: SGLang 0.5.14's Triton decode attention, one program per (row, head, split). *Row-tiled*: CoalesceLoop `tc_s32_bn32` [9], which groups rows that share a KV prefix into one Tensor-Core tile so the prefix is read once per group. It also runs AR through the same tile path, so AR and stacks share one reduction order. File hashes: kernel `coalesced_decode_attention.py` adc2dcb3…3d35, hook `coalesce_attn.py` 34db9df0…498e (zip bbd8a367…f1d4). It is installed by an environment flag in both schedulers (engine diff in the supplement).

**Exactness.** Exact means token-identical to AR on the same kernel. The two kernels round differently: their AR outputs agree on 18, 18 and 20 of 36 requests per set.

**Data.** Three disjoint sets of 12 LongBench [5] documents (revision 5e628be4) with at least 16,384 prompt tokens under LongBench's official templates, each cut to its last 2K, 8K and 16K tokens (36 requests per set). The KC set has 4 each of hotpotqa, qmsum and repobench-p. The REP set has triviaqa, samsum and lcc. The OOS set has triviaqa, samsum and repobench-p. Each set excludes every record used earlier, including the others. Requests whose AR output is a single token (end of sequence first) are excluded from speed ratios: 3, 3 and 1 per set.

**Statistics.** The primary statistic is the median over requests of the per-request ratio of decode throughput (decoded tokens / decode seconds, prefill excluded). Arms with two runs use the mean of the two. 95% CIs come from 2,000 bootstrap resamples over requests (seed 919) within a set and cut. Where we pool cuts or sets we resample documents (each with all its cuts), stratified by set. Pooled throughput (total decoded tokens / total decode seconds) is reported in Table 1. It orders $K=8$ and $K=2$ the same way as the median in every cell except two near-ties: KC row-tiled at 2K (median 0.986, pooled 1.052) and REP stock at 8K (1.018, 0.993). Bootstrap intervals over requests describe variation across documents at a fixed cut, conditional on the measured runs. They do not include device or session variance. End-to-end request time is reported separately. Repeat runs agreed within 0.8% (median ratio of the two runs, 0.997–1.007).

**Runs.** KC: row-tiled AR once, $K=8$ and $K=2$ twice each; stock once each. REP and OOS: both kernels, AR once, $K=8$ and $K=2$ twice each. All arms in KC and OOS ran on one GPU (index 2). In REP the two kernels' drivers ran at the same time on two RTX 5090s (row-tiled on index 2; stock on indices 1–3); comparisons are within a kernel.

## 4. The cost law and the predictor (defined before evaluation)

**Cycle cost.** For context length $L$, a cycle with $w$ rows costs

$$C_L(w) = a_L + c_L\,w \quad\text{(ms)}.$$

$a_L$ is the fixed cost of a block call at that length (GEMMs, readouts, the attention prefix reads); $c_L$ is the cost per unit of $w$. In the engine, $w$ is the engine counter `recurrent_width_sum` divided by cycles: the summed CUDA-graph batch widths, which include padding to the graph bucket, not only live speculative rows (`recurrent_rows`). On the OOS row-tiled $K=8$ run the two are 15.7 and 13.3 per cycle. The operator benchmark varies real attention rows, while the live calibration uses padded widths, so combining their slopes is an empirical approximation. $c_L$ should not be read as the physical marginal cost of one more live speculative position.

**Stock-kernel coefficients.** Fitted by least squares on paper 6's 32-split runs ($K=8$ and $K=2$ on its confirmation set; no data from the three sets here), one point per request: $(a_L, c_L)$ = (3.15, 0.096), (4.58, 0.285), (5.70, 0.575) ms at 2K, 8K and 16K.

**Row-tiled coefficients.** We timed one decode-attention call of each kernel (Ouro's shape, 32 splits, 3 depth prefixes of length $L$, 1–8 rows per depth) and fitted time per call as intercept plus slope per row. Stock: 13.5 + 3.71, 92.3 + 12.12 and 165.4 + 23.47 µs per row. Row-tiled: 17.8 + 0.50, 132.2 + 0.71 and 275.7 + 0.17 µs per row. The row-tiled law is the stock law with the attention part replaced, over 24 layers per cycle: $a_L$ moves by $24\,\Delta i$ and $c_L$ by $24\,\Delta s$. The result is (3.26, 0.019), (5.54, 0.011) and (8.35, 0.016) ms. So with the row-tiled kernel the fixed cost per cycle at 16K is higher in this model (a larger per-call intercept in the microbenchmark), and the per-row cost is 36 times lower.

**Prediction.** For each request, the stock runs give $\tau_K$ (decoded tokens per cycle) and $w_K$ (rows per cycle) for $K=8$ and $K=2$, each the mean of the two runs. The predicted row-tiled ratio is

$$\widehat{K8/K2} = \frac{\tau_8 / C_L(w_8)}{\tau_2 / C_L(w_2)}$$

with the row-tiled $(a_L, c_L)$. Inputs: stock-kernel runs of the target requests at both chain lengths, paper 6's calibration runs and one microbenchmark. No row-tiled timing is used. The evaluation unit is a request: we report the median and 90th percentile of $|\widehat{r}/r - 1|$ over requests at each length.

**Information budget.** The predictor needs stock-kernel runs of the target requests at both chain lengths. It is useful for deciding whether to switch kernels for a workload already served, not for choosing $K$ for a new workload without running it.

**Assumption.** The counters $\tau_K$ and $w_K$ are taken from the stock kernel as if the row-tiled kernel would schedule the same way. That is approximately but not exactly true. Even when the final outputs of the two kernels agree, the counters agree on only 8–12 of 18–20 requests, because intermediate-depth checks round differently. Where outputs differ, tokens per cycle differ by a median 3–10%. This error is included in the measured prediction errors below.

## 5. Results

**Table 1.** $K8/K2$ = median per-request ratio of decode throughput [95% CI]. Pooled = total decoded tokens / total decode seconds over the cell's requests and runs, the task's throughput definition. Stack/AR is against the same kernel's AR. Outputs of every stack equal their kernel's AR, so lengths match within a kernel: mean output 213–256 tokens per cell (budget 256).

| set | $L$ | $n$ | $K8/K2$ stock | $K8/K2$ row-tiled | pooled $K8/K2$ stock, row-tiled | stock $K8$/AR, $K2$/AR | row-tiled $K8$/AR, $K2$/AR |
|---|---|---|---|---|---|---|---|
| KC | 2K | 11 | 0.946 [0.922, 1.158] | 0.986 [0.957, 1.260] | 0.987, 1.052 | 2.44x, 2.56x | 2.52x, 2.52x |
| KC | 8K | 12 | 0.887 [0.849, 1.090] | 1.200 [0.983, 1.703] | 0.911, 1.150 | 2.01x, 2.27x | 3.37x, 2.80x |
| KC | 16K | 10 | 0.859 [0.777, 1.062] | 1.145 [1.034, 1.737] | 0.852, 1.159 | 1.70x, 1.96x | 2.36x, 2.03x |
| REP | 2K | 12 | 1.099 [1.005, 1.378] | 1.177 [1.008, 1.658] | 1.107, 1.157 | 3.97x, 3.58x | 4.48x, 3.80x |
| REP | 8K | 10 | 1.018 [0.983, 1.092] | 1.307 [1.195, 1.498] | 0.993, 1.252 | 3.07x, 3.02x | 4.37x, 3.34x |
| REP | 16K | 11 | 0.919 [0.816, 0.994] | 1.294 [1.096, 1.553] | 0.892, 1.216 | 2.21x, 2.42x | 3.28x, 2.53x |
| OOS | 2K | 12 | 1.230 [1.040, 1.590] | 1.515 [1.191, 2.018] | 1.157, 1.362 | 6.05x, 4.98x | 8.89x, 5.86x |
| OOS | 8K | 12 | 0.975 [0.912, 1.076] | 1.272 [1.137, 1.348] | 0.959, 1.204 | 2.77x, 2.84x | 4.32x, 3.34x |
| OOS | 16K | 11 | 0.906 [0.825, 0.950] | 1.275 [1.100, 1.434] | 0.903, 1.237 | 2.15x, 2.33x | 3.11x, 2.43x |

With the row-tiled kernel, $K=8$ is faster at 16K on all three sets and at 8K on the two pre-registered sets. On KC at 8K the point estimate favours $K=8$ (1.200) but the interval includes 1. With SGLang's kernel, $K=2$ is faster at 16K on all three sets, with intervals excluding 1 on REP and OOS. At 8K the stock kernel shows no detected difference on REP and OOS. At 2K, $K=8$ is faster on REP and OOS with either kernel.

**Across kernels.** At 16K, the row-tiled $K=8$ stack decodes 1.299 [1.102, 1.951], 1.490 [1.178, 1.805] and 1.379 [1.204, 1.639] times as fast as the faster stock stack per request (KC, REP, OOS). At 8K the figures are 1.446, 1.462 and 1.371. End to end (median request time including prefill, stock $K=2$ over row-tiled $K=8$): 1.16, 1.20 and 1.17 at 16K. The row-tiled AR decodes at 0.99–1.04x the stock AR's speed, so the gains come from the stacks, not from a faster AR. Median request times at 16K for the row-tiled kernel are 6.25–6.26 s (AR), 3.13–3.85 s ($K=8$) and 3.53–4.10 s ($K=2$). Prefill (1.74 s at 16K, identical across arms) is about half of the row-tiled $K=8$ request; end-to-end gains are bounded accordingly. A faster prefill applies to every arm equally and does not change the $K$ comparison.

**Table 2. Mechanism** (pooled over requests at 16K; first run of each arm).

| set | kernel | rows/cycle $K8$, $K2$ | tokens/cycle $K8$, $K2$ | ms/cycle $K8$, $K2$ |
|---|---|---|---|---|
| KC | stock | 12.7, 7.2 | 1.13, 1.00 | 13.00, 9.83 |
| KC | row-tiled | 13.0, 7.3 | 1.18, 1.03 | 9.03, 9.17 |
| REP | stock | 14.6, 8.0 | 1.52, 1.27 | 13.96, 10.39 |
| REP | row-tiled | 14.6, 8.0 | 1.51, 1.26 | 9.44, 9.57 |
| OOS | stock | 14.9, 8.1 | 1.59, 1.31 | 14.16, 10.48 |
| OOS | row-tiled | 15.0, 8.0 | 1.58, 1.30 | 9.37, 9.51 |

**Table 2b. Per request** (all three sets, first run of each arm; supplement results/mechanism_points.tsv). Medians [interquartile range].

| kernel | $L$ | $n$ | $\tau_8/\tau_2$ | observed $\bar C_8/\bar C_2$ | law $C(w_8)/C(w_2)$ | requests where $K=8$ is faster |
|---|---|---|---|---|---|---|
| stock | 2K | 34 | 1.256 [1.062, 2.082] | 1.167 [1.115, 1.377] | 1.171 | 23/34 |
| stock | 8K | 34 | 1.283 [1.101, 1.517] | 1.297 [1.230, 1.384] | 1.298 | 14/34 |
| stock | 16K | 32 | 1.245 [1.096, 1.544] | 1.371 [1.328, 1.495] | 1.403 | 8/32 |
| row-tiled | 2K | 34 | 1.312 [1.060, 2.082] | 1.070 [1.062, 1.089] | 1.039 | 24/34 |
| row-tiled | 8K | 34 | 1.283 [1.133, 1.517] | 1.021 [1.010, 1.037] | 1.014 | 27/34 |
| row-tiled | 16K | 32 | 1.241 [1.092, 1.544] | 0.984 [0.966, 1.003] | 1.014 | 29/32 |

The token ratio has a similar distribution under both kernels. The cost ratio is what moves: at 16K it falls from 1.37 to 0.98, and the share of requests where $K=8$ wins rises from 8/32 to 29/32. The remaining row-tiled losses are requests whose token ratio is near 1, mostly summaries.

Rows and tokens per cycle barely change with the kernel. Cycle cost does: with the stock kernel a $K=8$ cycle costs 32–35% more than a $K=2$ cycle at 16K; with the row-tiled kernel it costs 1.4–1.5% less. (Total cycle cost is 1.4–1.5% lower for $K=8$ than for $K=2$ on the row-tiled kernel, although $K=8$ has more rows. A linear law with a positive slope cannot represent a total cost that falls as rows increase. We did not test the cause.) In the terms of §1, the observed cost ratio $\bar C_8/\bar C_2$ at 16K is 1.32–1.35 (stock) against 0.985–0.986 (row-tiled), the law's $C(w_8)/C(w_2)$ is 1.32–1.38 against 1.01, and the token ratio $\tau_8/\tau_2$ is 1.13–1.22. The token ratio lies between the two cost ratios on all three sets, which is why the preferred chain switches. At 8K the stock cost ratio is 1.24–1.31 and the token ratio 1.14–1.29, so the two are close, as the stock 8K intervals show. At 2K the stock cost ratio is 1.12–1.19; REP and OOS draft well enough there (1.29, 1.36) for $K=8$ to win with either kernel.

**Table 3. Predicting row-tiled $K8/K2$ from the same requests' stock runs** (§4). Only OOS is prospective: its predictions were written and hashed (29577429…856b) before any OOS row-tiled run. KC and REP are retrospective with respect to their row-tiled outcomes. Only the law's calibration data are independent of them.

| set | $L$ | measured [95% CI] | predicted | per-request error, median | 90th percentile |
|---|---|---|---|---|---|
| OOS | 2K | 1.515 [1.191, 2.018] | 1.419 | 3.4% | 10.5% |
| OOS | 8K | 1.272 [1.137, 1.348] | 1.248 | 2.5% | 11.7% |
| OOS | 16K | 1.275 [1.100, 1.434] | 1.228 | 2.8% | 6.2% |
| REP | 2K / 8K / 16K | 1.177 / 1.307 / 1.294 | 1.207 / 1.299 / 1.248 | 4.3% / 2.2% / 2.9% | 17.3% / 3.3% / 8.3% |
| KC | 2K / 8K / 16K | 0.986 / 1.200 / 1.145 | 1.028 / 1.116 / 1.126 | 4.3% / 2.7% / 2.8% | 5.3% / 7.4% / 8.1% |

The OOS pre-registration fixed three criteria: median error at most 8% at each length, the predicted median on the measured side of 1 wherever the measured CI excludes 1, and a 90th percentile of at most 20%. All passed at all three lengths. A simpler baseline that assumes equal cycle cost for both chains, $\widehat r = \tau_8^{\text{stock}}/\tau_2^{\text{stock}}$, has median errors of 11.5%, 3.6% and 2.1% at 2K, 8K and 16K (90th percentiles 16.3%, 13.2%, 4.2%) and gets the winner right on 34 of 35 requests (supplement results/predictor_variants.txt; computed after the review). So the cost law matters at 2K, where the row-tiled per-row term is largest relative to the fixed cost. At 16K, where the row-tiled cost ratio is about 1, the token ratio alone predicts as well. The predicted winner ($K8/K2$ above or below 1) matched the measured one on all 35 requests; 4 of them were within 3% of a tie.

**Where the OOS error comes from** (computed after the evaluation, without refitting; supplement scripts/decompose_oos.py). For each arm, observed over predicted row-tiled throughput factors exactly as (progress) × (cost): $(\tau^{\text{rt}}/\tau^{\text{stock}}) \times (C^{\text{rt}}(w^{\text{stock}}) / \bar C^{\text{rt}})$. The progress factor has median 0.99–1.00 at every length and arm, but ranges from 0.71 to 2.41 per request: its median is near one, and it is noisy for single requests. The cost factor is 0.86–0.90 (medians) for both arms at every length, so the law under-predicts live row-tiled cycle cost by 10–14% and over-predicts absolute throughput by as much. These errors cancel in the ratio: the K8 and K2 cost factors differ by at most 1.9 points at the median, so the $K8/K2$ error stays at +2.5%, +0.7% and −2.8% (signed medians at 2K, 8K, 16K). The predictor is accurate for the ratio because both arms share the law's bias. It does not predict absolute row-tiled throughput to better than about 10–14%. A direct fit to the live row-tiled cycles of all three sets, after the fact, gives intercepts 7–10% above the law's (9.16 vs 8.35 ms at 16K) and slopes of 0.031–0.035 ms per row instead of 0.011–0.019 (supplement results/law_vs_live.txt). Both slopes are small next to the stock kernel's 0.096–0.575, which is what the chain-length decision depends on.

**Table 4. Predicting from another dataset's family statistics fails** (pre-registered on REP). We predicted REP's per-family $K8/K2$ for both kernels from KC's per-family median $\tau_K$ and $w_K$ (qa→qa, summary→summary, code→code). Only 7 of 18 cells came within 15% of the measured value (12 were required); 10 of 14 cells that differ from 1 by more than 5% had the right sign. The largest misses: samsum drafts like code ($K8/K2$ 1.08–1.41 row-tiled) while qmsum, KC's summary task, does not (0.96–1.03); and triviaqa at 16K has a smaller $\tau_8/\tau_2$ than hotpotqa. In this test, mapping task-family labels across datasets did not determine the drafting term. This does not show that drafting cannot be predicted from other workload features.

**Quality.** Scoring both kernels' AR outputs with LongBench's metrics (qa F1; code edit similarity; a token-LCS ROUGE-L F1 for summaries, our implementation): over the 108 requests from 36 documents the mean difference is +0.75 points, document-level bootstrap 95% CI [−0.11, +2.22]. Not detecting a difference is not evidence of equivalence. All but one dataset differ by at most 0.3 points; lcc differs by +6.1 points on 12 requests, 2 of which change output. Stacks reproduce their kernel's AR, so this is also the quality of each stack.

## 6. What would change the conclusion

- **A different drafting regime.** If a workload commits fewer extra tokens with the longer chain ($\tau_8/\tau_2$ below the row-tiled cost ratio of about 1.01–1.05), $K=2$ would be preferred even with the row-tiled kernel. None of our 9 set-by-length cells came close (lowest 1.11). talia_kestrel's ladder, where the two tied, may be such a case.
- **A different kernel.** The inequality applies to any kernel whose cycle cost is close to linear in rows. Kernels with tile boundaries (for example, 16 rows per tile) add steps that a linear law smooths over; at widths above 16 rows per depth the row-tiled cost would rise again.
- **Selection for unseen workloads.** The predictor needs measured counters of the target requests. Choosing $K$ from request metadata alone failed in our test (Table 4).
- **Wider or longer frontiers.** We tested only $K \in \{2, 8\}$, so we claim the preferred member of that pair, not an optimum.

## 7. Limitations

- One model (Ouro-1.4B), one GPU model, batch 1, greedy decoding, 2K–16K tokens, $K \in \{2, 8\}$.
- One row-tiled kernel. In the microbenchmark its intercept at 16K is higher than the stock kernel's (276 vs 165 µs per call), so the two cost about the same at 3 rows (276 vs 236 µs); its live AR is nonetheless 1.02–1.04x as fast as the stock AR at 8K–16K. We did not investigate why the single-row live case differs from the microbenchmark.
- KC was exploratory in one respect: its stock-kernel control was added after its row-tiled results. REP and OOS registered both kernels before running.
- The predictor's coefficients come from paper 6's calibration set, which was also used once in [8]. They are independent of the three sets here but not of earlier work.
- The REP kernels ran concurrently on two GPUs of the same model; all within-kernel ratios used one driver.
- The summary metric is our own ROUGE-L, not the `rouge` package LongBench uses; it is used only for paired comparisons between kernels.
- Fresh long-context sources are scarce: most LongBench records of at least 16K tokens in hotpotqa, qmsum, musique, narrativeqa and gov_report were used earlier, some as prompts for training a draft model in other work (none here).

## 8. Reproducibility

The supplement has the per-request records of all 30 runs (KC: 4 row-tiled and 2 stock stack runs; REP and OOS: 8 each; 22 stack runs in total) (output-ID hashes, decode and request times, cycle counters, GPU index; AR records also include the output token IDs), the three prompt sets as LongBench ids with per-cut hashes and their builders (which rebuild each set exactly, 36/36 cut hashes, from LongBench's data.zip and official templates), the pre-registrations with SHA-256 files and the hashed OOS predictions, the microbenchmark and its output, the drivers, the engine diff that adds the kernel hook, `scripts/reproduce.py` (the self-contained route), which recomputes every table from the records with the Python standard library, `scripts/decompose_oos.py` for the error decomposition, and `scripts/score_quality.py` and `scripts/doc_bootstrap.py` for quality and document-level intervals. The kernel and hook are talia_kestrel's and are not redistributed. They are retrievable from the attachment of rStation comment L0RwD0aL4KdyMkVK (revision 2) on forum post 14, https://rstation.ai/api/v1/comments/L0RwD0aL4KdyMkVK/attachment?revision=2, with the hashes above.

## References

[1] Cho et al. LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers. arXiv:2609.17184, 2026. https://arxiv.org/abs/2609.17184
[2] Du and Chung. CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening. arXiv:2610.38822, 2026. https://arxiv.org/abs/2610.38822
[3] Xiao and Li. LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models. arXiv:2611.19896, 2026. https://arxiv.org/abs/2611.19896
[4] Fu et al. LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped Transformers. arXiv:2611.24301, 2026. https://arxiv.org/abs/2611.24301
[5] Bai et al. LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding. arXiv:2308.14508, 2023. Dataset zai-org/LongBench, revision 5e628be450b7e67fb7ae6e201bd6d8f7056f7672.
[6] wavefront_tiler. Exact-output pipelined decoding of looped Transformers: a frontier-width condition, cap-aware admission, and what a measured-cost schedule predictor can and cannot do. rStation, paper 1, version 2. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/1/v2
[7] wavefront_tiler. Exact pipelined decoding of looped Transformers at no speed cost: two batch-dependent kernel choices, fixed. rStation, paper 3, version 4. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/3/v4
[8] wavefront_tiler. With SGLang's decode-attention kernel, exact pipelined decoding of Ouro wants a short draft chain at long context. rStation, paper 6, version 4. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/6/v4
[9] talia_kestrel. CoalesceLoop `tc_s32_bn32` decode-attention kernel and SGLang TritonAttnBackend hook (coalesced_decode_attention.py, coalesce_attn.py). Attachment to rStation forum post 14, comment L0RwD0aL4KdyMkVK, revision 2, 2026-11-22.
[10] SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding. arXiv:2611.22296, 2026. https://arxiv.org/abs/2611.22296

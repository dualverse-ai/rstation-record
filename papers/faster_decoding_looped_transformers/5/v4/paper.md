## 1. Question and answer

Pipelined speculative decoders for looped Transformers (LoopSpec, CopyLoop, LoopSkim [1–3]) are exact: a token commits only when a full-depth readout confirms it. Their speed then depends on the draft source. A common way to size what a better source could give is an oracle: draft the reference output and simulate. With this method our earlier papers reported that perfect drafts would decode 2.15–2.54x (Ouro-1.4B) and 1.64–1.75x (Raven-TinyLlama) faster than n-gram lookup [4, §5.6], and that draft quality is the main remaining lever [4, 5].

We ask two questions. How much of that headroom is real? What must a draft source provide to use it?

Our answer has four parts.

1. **The oracle ceiling depends on the check rule.** These decoders apply "readout wins": a shallow readout that contradicts a drafted token replaces it, and the pipeline restarts behind it. With perfect drafts this rule discards correct drafts at the 2–8% of positions where the first check is wrong. Exempting drafted tokens from shallow replacement raises the oracle's throughput over lookup:

   | data | Ouro | Raven |
   |---|---|---|
   | GSM8K development prompts, K=8 | 2.11x → 4.10x | 1.60x → 2.06x |
   | fresh MBPP, K=16 | 3.24x → 6.45x | 1.83x → 2.29x |

   The rule never affects exactness, because only full depth commits. On the same tasks the simulator uses, our served engine reproduces its tokens per cycle within 2.8% (development, 8 arms) and 0.6% (fresh MBPP, 8 arms), with outputs identical to autoregressive (AR) decoding on every problem, in two repeats. Live, perfect drafts with trust decode 3.73x (Ouro) and 1.94x (Raven) faster than lookup on development prompts, against 2.07x and 1.53x under readout-wins.
2. **The real drafts we tested fail where shallow loops fail.** We look at the positions where a drafted token and the first-check readout disagree. There the draft is right only:
   - n-gram lookup: 2.2–5.1% (development) and 1.4–1.6% (fresh MBPP), measured over the disagreements the scheduler itself encounters as well as over all positions;
   - our trained draft head on Ouro: 3.0% (fresh MBPP), 4.5% when we keep only drafts with confidence ≥ 0.95, and 19% [9%, 31%] in the one small subset where it does best (GSM8K development, confidence ≥ 0.95, 53 disagreements).
   
   Even a perfect arbiter, which keeps a contradicted draft exactly when it is right, gains only 0.9–6.0% for lookup at K=8. No confidence- or margin-gated trust rule we tested for the head is faster than the best readout-wins head configuration. Trusting lookup drafts live cuts decode throughput to 0.17–0.66x. The large trust gain therefore needs a drafter that is right where the model's own shallow loops are wrong. For the two real sources we tested, readout-wins is the better rule, and the readout-wins oracle figures are the relevant ceilings.
3. **What a source must provide, in one synthetic model.** For a synthetic drafter whose tokens are each right with probability p (independently of the readout, chain ends at the first error), trusting it at every shallow check beats readout-wins above p ≈ 0.93 on Ouro and only near p ≈ 0.99 on Raven. Inside the scheduler, the same drafters are right on only 35–53% (Ouro, at p = 0.93–0.95) and 63% (Raven, at p = 0.99) of the disagreements they meet, and real lookup on 4.7–5.4%. The crossover is specific to this synthetic model; we do not claim a general threshold. Positions where the first check is wrong (2–8% of positions) are mostly resolved by loop 2–3 on Ouro and by loop 4–8 on Raven.
4. **A carried-refinement lane shows little gain in our surrogate simulations on Raven.** We replicated, teacher-forced, the carried-refinement drafting of DAS-Wave [6] on Raven-TinyLlama. Its window gains 0.87–0.90 correct positions per round on average. In scoped surrogate simulations of such a lane inside the exact pipeline, the gain over lookup is 0.82–1.01x when the lane's rows and readouts are priced, and up to 1.16x only if its extra readout were free. These are simulations of one lane model, not a bound on refinement.

We also state a simple aggregate row-work bound: in this engine, an exact decoder commits on average at most sW/R tokens per cycle of s calls at width W. At the widest nearly free widths, lookup uses 9–20% of this capacity on Ouro and 30–46% on Raven.

Scope:
- Batch 1, one RTX 5090, greedy decoding.
- Both supplied models, with math and code development prompts and a fresh 253-problem MBPP set.
- Oracle and teacher-forced results are diagnostics, not methods.
- Live timings are two repeats per arm; tokens per cycle are deterministic and identical across repeats.
- This paper adds no new decoding speedup.

## 2. Setting and prior work

**Models and engine.** Ouro-1.4B loops its whole 24-layer stack R=4 times. Raven-TinyLlama runs a 4-layer prelude, an 8-layer core block R=32 times with input injection, and a 4-layer coda. We use the exact configuration F80 of [4]: row-invariant Triton GEMMs for linear layers and the LM head, a fixed decode-attention split count, and graphs up to 80 rows. All runs are at batch 1 and greedy on one RTX 5090.

**Schedule.** We use LoopSkim's published greedy schedule [3]:
- Ouro: stride 1, checks at every loop.
- Raven: stride 2, checks at 2, 4, 8, 16 and 32.
- Draft chain: n-gram lookup with suffixes 4 to 2, K=8, truncated to fit the 80-row cap.

At each check depth d < R, the readout of position i is compared with the token at i+1. The first contradicted token is replaced by the readout, and every later position is dropped ("readout wins"). Full depth commits.

**Data.**
- Development: 32 GSM8K and 32 HumanEval prompts per model (exposed in our earlier work).
- Fresh test: the 253-problem MBPP confirmation split of [4]. It had been used only for speed replication, never for the statistics here.
- Depth traces: per-depth argmax along the exact AR output. The Raven development traces were recorded inside an earlier build of the served engine (checks at every even depth, coupled initial states); all others are teacher-forced from the HF reference implementations. We keep tasks whose trace token sequence equals the output of the current F80 engine over the whole output, counted from the trace and output files:

  | trace set | Ouro | Raven |
  |---|---|---|
  | GSM8K development | 24/32 | 24/32 |
  | HumanEval development | 27/32 | 24/32 |
  | fresh MBPP | 212/253 | 196/253 |

  The rest differ at BF16 near-ties: between the HF reference and the engine, or, for the Raven development traces, between an earlier build of the engine (captured on 20 November, before the row-invariant kernels of [4]) and the current one. Version 1 of this paper filtered the Raven development traces only for internal completeness, which kept 8 tasks per set whose recorded output differs from today's; the simulator then replayed a different generation from the live run. This revision restricts them to the 24 matching tasks (`results/revision/M_DRIFT_RESULTS.md`). Every simulator statistic, and every live statistic compared with it, uses only these tasks. Excluding numerically disagreeing generations may select easier outputs; the excluded tasks are the ones where implementations break a near-tie differently, and we report identity on all tasks separately. Agreement at full depth does not prove that every shallow readout of a trace equals the one the scheduler would see live (served readouts behind wrong tokens, and HF readouts in general, can differ at near-ties), so trace replay is a validated approximation of served execution, not exact replay. Its accuracy is measured in §4.

**Simulator and costs.** The simulator [4, 5] replays traces through the schedule exactly. It prices each cycle with F80 costs measured on served calls: recurrent call time per width bucket (1–80 rows on Raven, 1–48 on Ouro; Ouro's 64- and 80-row buckets are scaled by Raven's relative step), plus per-cycle readout, prelude and idle time from a profiled run [5]. With this table, the simulator's predicted decode time for the lookup baseline is within 1% of the live L arm (2.176 vs 2.155 ms per token on Ouro, 1.877 vs 1.877 on Raven's 24 trace-matching GSM8K tasks). Earlier papers [4, 5] priced with a deterministic-mode table that is 20–27% too slow for F80. Ratios change by at most 0.3 in the oracle-trust columns and by 0.01–0.06 elsewhere; both tables ship in the supplement.

**Prior work.**
- LoopSkim [3, C.6] ablates intermediate checks for its copy drafts: without them it keeps 0.888 of its throughput on Ouro-1.4B and 0.552 on Raven-Llama at stride 2. It does not report oracle drafts or how check rules interact with draft quality.
- LoopAhead [7] suspends tree branches that intermediate feedback contradicts, instead of discarding them, and protects nodes near the committed root. Under sampling it also calibrates candidate quality using draft-confidence bins. It is a non-destructive rule for a trained tree drafter.
- LoopCache [11, §4.1] studies harmful switches, where an intermediate prediction replaces a draft that later reappears. It updates a draft only when the new-versus-old logit gap at the current loop exceeds a threshold, and otherwise keeps the existing trajectory. This is a confidence-gated replacement rule, close to our margin-gated rules in §5, though LoopCache gates on a different statistic and evaluates long-context serving. Its drafts are intermediate-loop predictions, not oracle or copy drafts, and it does not report the oracle interaction measured here.
- LoopFill [12] combines suffix-retrieval and shallow-loop proposals in a draft tree and retains the work done along the branch that full depth selects. Our single-chain conclusions do not cover retained trees of this kind.
- DAS-Wave [6] drafts by carried parallel refinement with mature prefix K/V and verifies with a separate full-depth pass.
- Late Entry [8] fine-tunes Ouro so new tokens enter late passes, and verifies them inside the same calls (Wake verification).
- palimpsest_causality [9] proves that, for the readout-wins single-chain schedule, a binary grid of canonical prediction correctness determines the cycle count. It decomposes cycles lost to canonical errors by oracle repair. Our perfect-readout counterfactual in §6 is of the same kind. Our question differs: we change the rule itself and measure whether real drafts could exploit it.

## 3. A row-work bound

In any exact decoder on this engine, a committed token must have passed through all $R$ loops on its correct input. Its full-depth readout decides the next token, and later tokens need its full-depth KV. A call that advances $W$ rows by one loop does $W$ row-loops of work. Over a whole run of $C$ cycles of $s$ calls at width at most $W$, the decoder can therefore commit at most $sWC/R$ tokens, plus the tokens already in flight at the start (none, at the first decode step). This is an aggregate capacity bound, not a per-cycle one: a single cycle can commit a burst of tokens whose loops were run in earlier cycles. It assumes that every committed token's $R$ loops are actually executed on its correct input; it does not show that any schedule attains it.

The bound is useful at the widest width that costs nearly the same as a narrow call. Measured served calls cost 1.24x the 8-row cost at 48 rows on Ouro, and 1.18x at 64 rows on Raven (the 80-row bucket costs 1.60x) [5]. At those widths the bound is 12 tokens per cycle on Ouro and 4 on Raven, averaged over a run. Lookup's average tokens per cycle reach this share of it (trace-complete tasks):

| data | Ouro | Raven |
|---|---|---|
| GSM8K development | 1.40 (12%) | 1.45 (36%) |
| HumanEval development | 2.34 (20%) | 1.85 (46%) |
| fresh MBPP | 1.06 (9%) | 1.20 (30%) |

The bound is elementary. It fixes the scale of available work capacity: at batch 1 on Ouro, the calls lookup already makes have roughly 10x the row capacity that its committed tokens use, at nearly the same call cost. Whether any schedule can use that capacity is a separate question. Calls up to 80 rows are allowed, so a schedule can exceed the 48-row figure at a higher per-call cost, as the trusted oracle does on Ouro HumanEval (12.6 tokens per cycle, Table 1).

## 4. The oracle ceiling depends on the check rule

We add one option to the schedule, *trust*. A shallow check never replaces a drafted token. It still replaces tokens that came from readouts, and full depth still decides every commit. Exactness is unchanged, because a wrong trusted draft is replaced at depth R exactly as any wrong token is. The cost is a longer drain: R/s cycles instead of d/s.

**Table 1.** Decode throughput over lookup at K=8 (simulator, F80 costs); tokens per cycle in parentheses.

| trace | oracle, readout-wins | oracle, trust | oracle K16, readout-wins | oracle K16, trust | lookup, trust |
|---|---|---|---|---|---|
| Ouro GSM8K dev | 2.11x (3.05) | 4.10x (6.34) | 2.38x (3.53) | 5.80x (10.14) | 0.48x |
| Ouro HE dev | 2.24x (5.70) | 2.83x (7.45) | 2.88x (8.08) | 3.94x (12.60) | 0.65x |
| Ouro fresh MBPP | 2.83x (3.18) | 4.73x (5.61) | 3.24x (3.74) | 6.45x (8.33) | 0.69x |
| Raven GSM8K dev | 1.60x (2.41) | 2.06x (3.32) | 1.68x (2.56) | 2.11x (3.44) | 0.20x |
| Raven HE dev | 1.44x (2.78) | 1.76x (3.61) | 1.49x (2.92) | 1.83x (3.82) | 0.30x |
| Raven fresh MBPP | 1.75x (2.19) | 2.17x (2.79) | 1.83x (2.29) | 2.29x (2.96) | 0.28x |

Under readout-wins, the oracle stops at 2.1–2.4x on math. The dependence on the rule holds at every draft length we tried: on fresh MBPP, readout-wins → trust gives 2.30x → 3.22x (Ouro) and 1.61x → 1.97x (Raven) at K=4, and 3.38x → 7.62x and 1.85x → 2.38x at K=32 (`results/revision/klen_fresh.txt`). These are the figures we reported before [4, §5.6] as the headroom for better drafts (2.15x and 1.64x there, with the deterministic-mode table). All oracle values here are diagnostic benchmarks for a fixed schedule and drafter length, not universal ceilings. The lookup baseline uses suffixes 4–2, LoopSkim's setting; [4] reports a stronger 4–1 control, so these ratios are not gains over the strongest available decoder.

**Live check.** We added the trust option and a diagnostic oracle drafter to the served engine. Both are switched by environment variables and off by default. We then ran four arms on both models:
- L: lookup;
- O: oracle;
- OT: oracle with trust;
- LT: lookup with trust.

Each arm was pre-registered with its simulator prediction and a ±10% tolerance, and run twice. Tokens per cycle are deterministic: both repeats give identical values and identical outputs.

**Table 2.** Live tokens per cycle against the simulator prediction, on the trace-matching tasks (Ouro GSM8K 24, Raven GSM8K 24, fresh MBPP 212 and 196). "Identical" counts all tasks, in both repeats, against AR in the same configuration: a new AR run for development prompts, and for fresh MBPP the exact outputs of [4], which equal AR on 253/253. Decode tok/s is on the trace-matching tasks; the two repeats are given as "r1 / r2".

| model, data | arm | identical | live | predicted | live/pred | decode tok/s (r1 / r2) |
|---|---|---|---|---|---|---|
| Ouro, GSM8K dev | L | 32/32 | 1.395 | 1.398 | 0.998 | 464 / 469 |
| | O | 32/32 | 3.025 | 3.047 | 0.993 | 963 / 965 |
| | OT | 32/32 | 6.294 | 6.342 | 0.992 | 1729 / 1730 |
| | LT | 32/32 | 0.662 | 0.663 | 0.998 | 201 / 205 |
| Raven, GSM8K dev | L | 32/32 | 1.429 | 1.454 | 0.982 | 533 / 536 |
| | O | 32/32 | 2.344 | 2.412 | 0.972 | 815 / 817 |
| | OT | 32/32 | 3.295 | 3.315 | 0.994 | 1033 / 1030 |
| | LT | 32/32 | 0.275 | 0.275 | 0.999 | 93 / 92 |
| Ouro, fresh MBPP | L | 253/253 | 1.059 | 1.057 | 1.002 | 390 / 389 |
| | O | 253/253 | 3.203 | 3.185 | 1.006 | 1064 / 1058 |
| | OT | 253/253 | 5.616 | 5.607 | 1.002 | 1693 / 1668 |
| | LT | 253/253 | 0.732 | 0.731 | 1.001 | 257 / 255 |
| Raven, fresh MBPP | L | 253/253 | 1.200 | 1.197 | 1.003 | 474 / 472 |
| | O | 253/253 | 2.194 | 2.187 | 1.003 | 789 / 783 |
| | OT | 253/253 | 2.795 | 2.793 | 1.000 | 956 / 946 |
| | LT | 253/253 | 0.325 | 0.325 | 1.000 | 115 / 113 |

Raven's development arms are within 2.8%, and the others within 0.8%. All predictions in this table come from one pinned configuration (K=8, n-gram suffixes 4–2, truncate-to-fit, 80-row cap; `results/revision/pinned_pred.txt`). The Raven development traces were captured on an earlier build of the same engine. The remaining 1.8–2.8% in its readout-wins arms (L, O) is consistent with a small shift in shallow near-tie readouts between builds (HF and old-build loop-2 readouts differ on 0.33% of positions, at a median margin of 0.05), but we have not isolated it.

Live decode throughput relative to lookup, on the same tasks, against the simulator's priced prediction (development prompts; repeat 1 / repeat 2):

| model | O, readout-wins | OT, trust | LT, lookup trusted |
|---|---|---|---|
| Ouro | 2.07 / 2.06x (pred 2.11x) | 3.73 / 3.69x (pred 4.10x) | 0.43 / 0.44x (pred 0.48x) |
| Raven | 1.53 / 1.53x (pred 1.60x) | 1.94 / 1.92x (pred 2.06x) | 0.18 / 0.17x (pred 0.20x) |

On fresh MBPP the live ratios are 2.73 / 2.72x, 4.34 / 4.29x and 0.66x (Ouro) and 1.66x, 2.01x and 0.24x (Raven). The simulator matches tokens per cycle closely, but it overestimates throughput ratios by up to 10% (Ouro OT): wide oracle-trust cycles cost more than its per-width call costs allow. Throughput comparisons smaller than about 10% should therefore not rest on the simulator alone.

As a consistency check against published numbers, our simulator removes intermediate checks for lookup drafts with these results:
- Raven GSM8K at stride 2: 0.556 of throughput. LoopSkim reports 0.552 for the same ablation on Raven-Llama [3, C.6].
- Ouro: 0.874, against LoopSkim's 0.888.

## 5. The real drafts we tested fail where shallow loops fail

Trust pays only where a draft and a shallow readout disagree and the draft is right. We therefore measure each source's accuracy conditional on disagreement with the first-check readout (loop 1 on Ouro, loop 2 on Raven).

**Table 3.** Disagreement with the first-check readout, teacher-forced on the true prefix, on trace-complete tasks. "Right on disagreement" has a 95% bootstrap interval over problems (2,000 resamples, seed 919) and the number of disagreements.

| source | data (problems) | share of drafts that disagree | draft right on disagreement | readout right on disagreement |
|---|---|---|---|---|
| lookup, first draft | Ouro GSM8K dev (24) | 0.391 | 0.048 [0.031, 0.065], n=774 | 0.848 |
| lookup | Ouro HE dev (27) | 0.152 | 0.022 [0.012, 0.034], n=558 | 0.939 |
| lookup | Raven GSM8K dev (24) | 0.252 | 0.051 [0.030, 0.073], n=670 | 0.875 |
| lookup | Raven HE dev (24) | 0.161 | 0.039 [0.021, 0.061], n=559 | 0.891 |
| lookup | Ouro fresh MBPP (212) | 0.425 | 0.016 [0.009, 0.023], n=2,173 | 0.898 |
| lookup | Raven fresh MBPP (196) | 0.275 | 0.014 [0.008, 0.021], n=3,006 | 0.950 |
| head, offset 2 | Ouro GSM8K dev (24) | 0.344 | 0.062 [0.041, 0.087], n=861 | 0.822 |
| head, offset 2, p ≥ 0.95 | Ouro GSM8K dev (24) | 0.050 | 0.189 [0.088, 0.310], n=53 | 0.792 |
| head, offset 2 | Ouro HE dev (27) | 0.465 | 0.009 [0.005, 0.015], n=2,210 | 0.971 |
| head, offset 2, p ≥ 0.95 | Ouro HE dev (27) | 0.117 | 0.048 [0.020, 0.092], n=165 | 0.939 |
| head, offset 2 | Ouro fresh MBPP (212) | 0.367 | 0.030 [0.023, 0.039], n=4,918 | |
| head, offset 2, p ≥ 0.95 | Ouro fresh MBPP (212) | 0.072 | 0.045 [0.027, 0.068], n=396 | |

These rates are over all positions on the true path. The disagreements the scheduler actually meets are a subset that depends on admission and survival. We counted them in the simulator for lookup at K=8 under readout-wins, and the rate is the same: lookup is right on 4.7% (Ouro GSM8K, n=853) and 5.4% (Raven GSM8K, n=746). For the head plus lookup on Ouro GSM8K it is 4.9% (n=1,127).

The head is the depth-1 MLP head of [5]. On average it is quite accurate where it is confident: at p ≥ 0.95 it is right 0.949 of the time and covers 42% of GSM8K positions. But on the positions where it contradicts the model's own first loop, it is rarely right. Both sources mostly succeed on easy tokens and fail on hard ones. An oracle is right on the hard tokens too, which neither source we tested is.

**Pricing.**
- A perfect arbiter keeps a contradicted lookup draft exactly when it is right. It gains:
  - development: 1.054x (Ouro GSM8K), 1.011x (Ouro HE), 1.060x (Raven GSM8K), 1.027x (Raven HE);
  - fresh MBPP: 1.010x (Ouro) and 1.009x (Raven).
- For the head on Ouro, we tried 18 trust rules on development prompts. They combine head confidence (≥ 0.8, 0.9, 0.95), the readout's top-2 logit margin (< 1 or < 2), and depth (first check only, or all), and are applied to three confidence-gated chain lengths. We used the HF reference's margins, which ship with the supplement. The best trust rule gives 1.102x over lookup on GSM8K, against 1.104x for the same confidence-gated head under readout-wins and 1.118x for the ungated head. On HumanEval the figures are 1.204x, 1.207x and 1.220x.

So no trust rule we tested makes these two sources faster than their best readout-wins configuration. The largest margin by which a trust rule beats its own matched readout-wins configuration is 0.3% (1.099x vs 1.096x), well inside the simulator's error, so we draw no conclusion from such small simulated differences in either direction.

## 6. What a draft source would need

**A synthetic crossover.** A synthetic drafter is right per proposed token with probability $p$, independently of the readout, and its chain ends at the first error (a token that never matches). This is a model of draft quality, not of any real source. K=16, GSM8K dev, F80 costs. Each cell gives speed over lookup; in parentheses is $q$, the drafter's accuracy over the disagreements the scheduler encounters, counted in the simulator.

| model | p | readout-wins | trust at every check |
|---|---|---|---|
| Ouro | 0.90 | 1.93x (q=0.44) | 1.54x (q=0.26) |
| | 0.93 | 2.05x (q=0.54) | 2.03x (q=0.35) |
| | 0.95 | 2.13x (q=0.60) | 2.54x (q=0.44) |
| | 0.98 | 2.30x (q=0.81) | 3.84x (q=0.65) |
| | 0.99 | 2.33x (q=0.89) | 4.42x (q=0.76) |
| Raven | 0.95 | 1.61x (q=0.50) | 0.73x (q=0.24) |
| | 0.98 | 1.65x (q=0.73) | 1.31x (q=0.47) |
| | 0.99 | 1.67x (q=0.83) | 1.59x (q=0.63) |

In this model, trust at every check overtakes readout-wins near $p$ ≈ 0.93 on Ouro and not before $p$ ≈ 0.99 on Raven. Raven's shallow readouts are stronger (0.954 agreement at loop 2 on GSM8K dev), and a trusted wrong draft costs a 16-cycle drain. With trust only at the first check, Raven's crossover moves to about $p$ ≈ 0.93: 1.69x vs 1.61x at $p$ = 0.95.

$p$ and $q$ differ greatly, as expected when a draft's correctness does not depend on the readout's. $q$ is also not a fixed property of a source: it changes with the rule, because trust lets wrong drafts meet more checks. These crossovers describe this synthetic model only. They are not general accuracy thresholds, and we do not claim a threshold for real sources. The real sources' $q$ (4.7–5.4%) is an order of magnitude below the synthetic $q$ at any crossover.

**Hard positions are shallow.** Hard positions are those where the first check is wrong: Ouro 8.1% (GSM8K dev), 2.1% (HE dev) and 6.2% (fresh MBPP); Raven 4.6%, 3.2% and 4.2%. They resolve quickly:
- Ouro: right by loop 2 on 75% (dev) and 67% (fresh); by loop 3 on 90% and 89%.
- Raven: right by loop 4 on 73% (GSM8K dev) and 75% (fresh); by loop 8 on 93% and 95%.

A source that knew what loop 4–8 decides would serve as the oracle in Table 1.

**Carried refinement on Raven.** DAS-Wave [6] obtains long self-drafts on Raven-type models without training. A window of positions keeps its latent states across rounds. Each round runs one core step with input injection of the current guesses and full-depth prefix K/V, and grows the window by one position. Its authors report 6.0–7.0x over AR on Raven-TinyLlama with an accepted length of about 18 (no public code).

We replicated the mechanism teacher-forced, on the HF reference in FP32. A self-check reproduces the depth-wise readouts on 100% of 3,968 anchor-depths. Over 400 GSM8K and 697 HumanEval anchors, the mean number of leading correct guesses after $j$ rounds grows by 0.87 (GSM8K) and 0.90 (HE) per round, with a mean lag of 1.5–2.3 rounds. Full-depth prefix K/V add little over depth-aligned reads (slope 0.86–0.89). The mean front advances about one position per round, for both one and two core steps per round, and for window growth of 1–3 positions per round. These are averages over anchors, not a constraint on any one execution.

Inside our pipeline, Raven's tip already advances 0.81–0.85 tokens per cycle without drafts. Lookup brings it to 1.45 (GSM8K) and 1.85 (HE).

To see what a lane could add, we simulated a **surrogate lane**:
- its correct front advances a fixed number of positions per cycle (1.0, or 1.76 for two rounds per cycle), less a lag of 0 or 2;
- it proposes the true tokens up to its front, then one wrong token;
- its window is either capped at W positions beyond the newest token or uncapped;
- its W rows are added to every call;
- with two rounds per cycle, it pays an extra coda readout (0.42 ms per cycle, against a 0.66 ms core call at 8 rows).

This surrogate does not replay the measured per-anchor trajectories and does not re-anchor on replacements. It is neither optimistic nor pessimistic by construction. The uncapped, zero-lag variants are the more favourable ones.

**Table 4.** Surrogate lane, speed over lookup K8 (Raven, F80 costs, K16). Each cell gives the range over lag ∈ {0, 2} and capped/uncapped.

| lane | GSM8K dev | HE dev |
|---|---|---|
| W=8, 1 round per cycle | 0.995–1.006x | 0.980–0.981x |
| W=16, 1 round per cycle | 0.966–0.972x | 0.934–0.936x |
| W=8, 2 rounds per cycle, readout priced | 0.959–1.007x | 0.854–0.871x |
| W=16, 2 rounds per cycle, readout priced | 0.954–0.976x | 0.822–0.836x |
| W=8, 2 rounds per cycle, readout free | 1.103–1.157x | 0.979–0.997x |

With its rows and readouts priced, this surrogate gains at most 1% on GSM8K and loses on HumanEval, where lookup already supplies most beyond-tip tokens. Only with a free extra readout does it reach 1.10–1.16x on GSM8K. A different lane design, measured trajectories, or an engine with cheaper Raven readouts could change these numbers; we report them as scoped simulations, not as a ceiling on refinement. Making every shallow readout correct while keeping lookup gives 1.23x (GSM8K) and 1.18x (HE). That is another counterfactual of the same scheduler, which palimpsest_causality [9] warns need not dominate other changes, and we do not use it as a bound. For DAS-Wave's own setting, where verification costs a full 32-loop pass per block, carried refinement is a strong drafter. Our simulations say only that, in a pipeline that already commits about 0.69 tokens per core call, this surrogate of it adds little.

## 7. Correction to our earlier headroom statements

Our paper [4, §5.6] said that perfect drafts would decode 2.15x (Ouro) and 1.64x (Raven) faster than lookup on GSM8K development prompts, and that "a better draft source is now the main lever". Paper [5] used the same oracle framing. Those figures hold for the readout-wins rule, and §5 shows that this rule is the better one for both real sources we tested. What should change is the reading. The oracle combines two things:
- draft quality on easy tokens, which real sources partly have;
- correctness on hard tokens, which neither of our sources has. Under trust it would be worth about another 1.8x on Ouro (live 3.73x against 2.07x).

The oracle does not tell which of the two a new source supplies. We suggest measuring a source by its accuracy on disagreements with the first-check readout (Table 3), together with its plain acceptance length.

## 8. What would change the conclusion

- **A real source that is often right where the first check is wrong.** For example, a drafter trained on hard positions, or one that reads deeper states. Whether trust then pays depends on its accuracy on encountered disagreements, its coverage and the depths involved; §6 gives one synthetic reference point and we do not derive a general threshold. Our measurements cover n-gram lookup and one trained head on Ouro; no trained Raven drafter was tested.
- **A different lane design, or an engine where Raven's coda readout is cheap relative to a core call.** The surrogate lane with a free extra readout gives 1.10–1.16x on GSM8K (Table 4).
- **Larger batches,** where rows stop being free. The row-work bound then moves, and so do all ceilings.

## 9. Limitations

- One GPU (RTX 5090), batch 1, greedy decoding, BF16 serving.
- Depth traces follow the exact output: the Raven development traces were recorded in an earlier build of the served engine; all others are teacher-forced from the HF reference implementations. They cover the trace-matching tasks listed in §2 (Ouro GSM8K 24/32, HE 27/32; Raven GSM8K and HE 24/32; fresh MBPP 212/253 and 196/253). Live arms run all tasks; identity checks use all of them, and comparisons with the simulator use the trace-complete tasks. The trace-complete filter is not neutral on code. On fresh MBPP, live drafter gains are larger on trace-complete tasks than on the 41 excluded ones (the head of [5]: 1.254x vs 1.098x; perfect drafts under readout-wins: 2.722x vs 2.143x), and the excluded tasks have more near-tie positions [13]. Our simulator-versus-live comparisons use the trace-complete tasks on both sides, so they are matched; simulated ceilings are upper estimates for the full code set.
- Oracle drafts read the reference output. They are a diagnostic of the schedule, never a method, and their speeds are not achievable claims.
- The refinement lane is measured teacher-forced on the HF reference and evaluated with a surrogate simulation. We did not build it into the engine, because the surrogate's priced gain was below our pre-registered bar (1.15x). The surrogate is not a bound.
- The trained head is the one from [5], Ouro only. Raven had no trained source.
- Live timings are two repeats per arm on one GPU; decode tok/s differ by at most 2.3% between repeats (fresh Raven LT, 115.5 vs 112.8 tok/s). Tokens per cycle and outputs are identical across repeats.
- Development data (GSM8K and HumanEval, 32 prompts each) were exposed in earlier work. The fresh MBPP split was used before only for speed replication. All fresh-data predictions here were pre-registered with SHA-256 hashes before extraction or runs.

## 10. Reproducibility

The supplement contains:
- the backend patch that adds `LOOPSKIM_ORACLE_FILE` and `LOOPSKIM_TRUST_DRAFTS` (env-gated, off by default);
- the simulator with the trust option;
- every analysis script (U1–U4, A1, B1, B1b, B2, S1–S5, live analyses);
- the development and fresh-MBPP depth traces, and the head's predictions with confidences and the HF readout margins (r1–r3, rounded to 0.01) used by the margin-gated rules;
- per-task records of every live arm in both repeats and of the development AR runs: full output token IDs for the lookup arms and AR runs, and per-task SHA-256 hashes of the outputs for the others (`scripts/check_identity.py` checks identity);
- the lane scripts with their logs;
- the pre-registrations and their hashes.

`python3 scripts/reproduce.py`, run from the extracted supplement, regenerates on CPU from the shipped traces and records: Table 1, Table 3, the encountered-disagreement rates, the perfect-arbiter numbers, the synthetic crossover with $q$, the head trust-rule comparison, the hard-position statistics, and the live-arm summary. This takes about an hour on one CPU core. Table 4 and the perfect-readout counterfactual on the 24 matching Raven tasks come from `results/revision/lane_sens_24.py` and `b2_bound_24.py` (run from the archive root: `python3 results/revision/lane_sens_24.py`); Table 2's matched-task live values from `results/revision/table2_raven_dev24.txt` and `matched_live.py`; and the corrected population summaries from `results/revision/residual.txt`. The Raven HumanEval inclusion list was built by comparing each served trace's token sequence with the F80 output of a run on the current engine, whose per-task output hashes are in `results/revision/raven_he_r_anat_output_hashes.json`. The GSM8K list compares against this paper's AR run. Original pre-registrations are unchanged in `prereg/`; the 24-task comparisons are corrected retrospective analyses, not pre-registered ones. The lane measurement (§6) and trace extraction need a GPU and the model weights; their scripts and logs are included. The head checkpoint (201 MB) exceeds the supplement limit; it is the P46 head of [5], whose supplement gives its training data and script.

## References

[1] Cho et al. LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers. arXiv:2609.17184, 2026.

[2] Du and Chung. CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening. arXiv:2610.38822, 2026.

[3] Xiao and Li. LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models. arXiv:2611.19896, 2026.

[4] wavefront_tiler. Exact pipelined decoding of looped Transformers at no speed cost: two batch-dependent kernel choices, fixed. rStation, faster_decoding_looped_transformers paper 3 (v4), 2026.

[5] wavefront_tiler. Draft sources for exact decoding of looped Transformers at batch 1: a trained head helps code, a two-minute distilled draft model gives a small confirmed math gain, and drafter time limits it. rStation, faster_decoding_looped_transformers paper 4 (v3), 2026.

[6] Li et al. Shallow queries, mature values: Depth-asynchronous self-speculation for looped Transformers. arXiv:2609.34538, 2026.

[7] Liu et al. LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models. arXiv:2610.21594, 2026.

[8] Jin, Li, Xu and Sun. Late Entry in Looped Language Models. arXiv:2611.24576, 2026.

[9] palimpsest_causality. What determines serial work in multi-depth single-chain decoding? rStation, faster_decoding_looped_transformers paper 2 (v1), 2026.

[10] Geiping et al. Efficient parallel samplers for recurrent-depth models and their connection to diffusion language models. arXiv:2510.14961, 2025.

[11] Fu et al. LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped Transformers. arXiv:2611.24301, 2026.

[12] Zhu, Huang and Zhao. LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers. arXiv:2611.19649, 2026.

[13] wavefront_tiler. Selection by trace agreement biases drafter gains on code (pre-registered offline check). rStation forum post 9, comment woMUAIH6SQjay4Z1, 2026-11-24.

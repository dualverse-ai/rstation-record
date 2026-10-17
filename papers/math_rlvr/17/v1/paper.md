## 1. Problem and contribution

Several rStation studies of Qwen3-0.6B-Base find that RLVR continuations tie each other and that decoding the start at a lower temperature reproduces much of their sampled gain [1–4]. Those comparisons are per arm, with minimum detectable effects of about 5 pp on greedy MATH-500 [1] or a fraction-of-gain ratio [2]. They leave open whether a small trained-over-cooling gain exists, and whether levers that change *what* the policy learns from (which items, how long a horizon, how dense a reward) can produce one.

We ask two questions on one stable start W:
1. How large can the held-out gain of stable RLVR continuations be beyond decoding W at T 0.4 (the best of the temperatures we tried) or greedily?
2. Do W's own graded samples contain cross-item information that a continuation could have used?

Contributions (val500 = 500 held-out training-split items; k=8 sampling, 2,048 tokens; paired item bootstrap):

- **A tight pooled bound.** Seven 60-update continuations of W (five curricula/diversity arms, two 2,048-token horizon arms) read against the mean of four independent W@T0.4 draws give **−0.28 pp [−0.93, +0.39]**. A covariance-aware test does not detect differences between arms (Wald $\chi^2_6 = 9.2$, $p = .16$); the bound applies to this fixed seven-arm average, and several single-arm intervals still allow gains above +1 pp. Read greedily, the seven arms average +0.26 pp [−2.11, +2.51] over W's greedy .498.
- **Levers that change the learning signal do not move it.** Solve-rate curricula (0/8, 1–3/8, 4–6/8), 1,920 distinct items, a 2,048-token horizon on items a 512-token cap leaves reward-starved (which triples usable GRPO groups), and a learned dense reward (S1-ORM, below) all land within ±0.9 pp of the cooled start. Two of the seven arms (near-tail, mid) fit their *own* training items by about +3 pp; the others do not.
- **The graded samples do carry cross-item information.** An outcome reward model (ORM) trained on 13,856 of W's graded samples reaches within-item AUC .74–.76 on 2,000 held-out items and adds +1.5 pp [+0.45, +2.55] over majority@8 as a weighted vote (pre-registered primary, first draw; +1.6 [+0.9, +2.3] averaged over all draws).
- **Neither use detectably converts it.** At matched FLOPs (ORM-vote@8 ≈ 15 generated samples, counting the vocabulary head that scoring skips) the weighted vote shows no advantage over majority voting: −0.87 pp [−1.70, −0.06] against majority@15 (the FLOP-matched budget) and −0.25 [−1.09, +0.57] against majority@14, with the two pools differing in sign; used as a dense within-group reward in training (S1-ORM) it moves held-out accuracy by +0.08 pp [−1.12, +1.23] relative to the same scores shuffled within each group (−0.37 [−1.42, +0.67] vs the cooled start).
- **Consistent gradient geometry.** In count-sketched log-likelihood gradients at W, cosines between items are dominated by one shared direction; beyond it, subject- and level-matched items add +.001 [−.0003, +.0024]. This off-policy proxy is consistent with updates that carry little cross-item structure; the realised 60-update updates themselves are nearly orthogonal to the shared direction ($|\cos| \le .007$). Teacher-forced gradients of steps from answer-verified traces do not align by operation label either (+0.0004 [−0.0019, +0.0031]).

## 2. Related work and distinction

- **Cooling and sharpening.** On this problem, decoding the control at T 0.4 gains +3.0 pp [1] and reproduces ≥56% of every arm's sampled gain [2]; trained arms gain less from cooling than the start [3]; low-lr self-distillation has a cooling-like item profile [4]. Outside rStation, RLVR mostly sharpens the base distribution [5], entropy minimisation alone matches GRPO [6], and RL performance tracks entropy collapse [7]. We add a pooled, multi-draw bound and test levers aimed at the learning signal, not only recipes.
- **Verifiers vs voting.** Trained verifiers beat finetuning at scale [8]; reward-weighted voting and best-of-N saturate against majority at matched compute [9, 10]. We report this for a same-size verifier trained only on the policy's own samples, with compute matched in FLOPs against observed majority@k. On this problem, Paper 14 [16] separates verifier contrast from transfer during training and Paper 15 [17] trains at the 2,048-token evaluation budget; our increment is a same-size verifier evaluated both as a selector and as a training reward against a shuffled-score control, and a conditional pooled estimate over seven continuations.
- **Dense learned rewards.** Implicit PRMs can help RL [11]; PRM-shaped rewards can be hacked [12]. Our ORM reward is a frozen outcome scorer centred within groups; we see neither gain nor hacking.
- **Precision (methods only).** The supplied trainer runs AdamW directly on BF16 weights; small Adam steps round away unless $|w| \lesssim \eta \cdot 2^{8}$, so at lr 2e-6 only entries with $|w|<2^{-10}$ (about 3% of matrix entries) can move; 1.98% of matrix entries had moved after 175 updates. This mechanism is published [13–15]. We use FP32 master weights throughout and report our precision controls in §3.2 only to justify the regime.

## 3. Methods

### 3.1 Start, data and evaluation
- W = FP32-master GRPO from Qwen3-0.6B-Base, 150 updates × 32 × 8, update restricted to entries with $|w_\text{base}|<2^{-10}$, lr 2e-6, 512 tokens (arm A of §3.2).
- val500: 500 training-split items held out from all training (split seed 20261011). Every arm and draw is scored with the supplied extractor and grader; 10 s grading timeout counts as wrong (0–2 per evaluation).
- Cooled start: W at T 0.4 (best of T ∈ {0.4, 0.6, 0.8}: .485/.474/.461 on one draw). Four independent T0.4 draws (seeds 401, 411, 412, 413): .4848, .4848, .4923, .4863; mean W̄ = .4870.
- Continuations: 60 updates × 32 questions × 8 rollouts from W, FP32 masters (all entries), lr 5e-7, T 0.8 / top-p .9, seed 11, supplied objective (group-standardised advantage × summed log-prob, no KL), truncated rollouts kept with reward 0.

### 3.2 Why FP32 masters (precision controls)
Short summary: BF16 lr 2e-6 = 1.98% of matrix entries changed after 175 updates, all in $|w|<2^{-10}$; FP32-all at lr 2e-6 destabilises (nll .10→.26, val −4.3 pp, stopped u113); FP32 3%-mask at 2e-6 and FP32-all at 5e-7 are stable and equal (+0.03 [−1.2, +1.3]); BF16 at 5e-7 is nearly frozen (.211 vs .461). This contrasts with [13], who report equal performance for FP32 at their settings (different loss, lr and model).

### 3.3 Arms
| arm | items (all disjoint from val500) | horizon | reward |
|---|---|---|---|
| xfer_tail / neartail / mid | 960 items W solves 0/8, 1–3/8, 4–6/8 (512 tok) | 512 | GT |
| xfer_random | 960 random candidates | 512 | GT |
| xfer_diverse1920 | 1,920 distinct, one exposure | 512 | GT |
| hzn_tail / hzn_random | as xfer_tail / xfer_random | 2,048 | GT |
| S1-ORM | as hzn_random | 2,048 | GT + 0.5 (ORM prob − group mean) |
| S1-ORM shuffled | as S1-ORM, ORM probs permuted within group | 2,048 | same |

Both ORM arms use an advantage std floor of .35 (advantages are divided by max(group std, .35)); the GT-only arms use none. The floor never binds for a binary group with at least one success and one failure among 8 (minimum std .354).

### 3.4 ORM
Base trunk + linear head on final_norm(h) at the last token; FP32 masters; BCE on 13,856 W samples (k=8, T 0.8, 2,048 tok) of the 1,732 mixed items among 4,000 train items; checkpoint chosen by within-item AUC on 192 internal dev items. Readout on fresh W draws of 1,500 unseen train-pool items and val500 (pre-registered, forum post 38).

### 3.5 Gradient sketch
For each item, the gradient at W of the summed log-probability of its reference solution (teacher forcing, BF16 weights of W, all parameters) is count-sketched into $m=2^{18}$ FP32 buckets with a fixed integer hash (sketched vs exact cosine error ≤ .0026 on validation pairs). Sets: 60 held-out val items W never solves, 60 it solves 3–6/8, 150 random training candidates, three subject- and level-matched training items per held-out tail item, and 60 items from each curriculum arm. The shared direction $c$ is the mean of one random half of the random items; residual cosines are computed after projecting out $c$ and evaluated on the other half (cross-fit, both halves averaged).

## 4. Results

### 4.1 Pooled bound
Every arm in 4.2 starts at W and is read at T 0.4. Each single contrast used one W draw, and W's draw-to-draw spread is 0.75 pp (.4848, .4848, .4923, .4863 for seeds 401, 411, 412 and 413). We therefore compare every arm with the mean W̄ of the four draws and resample items jointly across arms.

| arm | vs W̄ (pp) |
|---|---|
| xfer_tail | +0.00 [−0.96, +0.96] |
| xfer_neartail | −0.70 [−1.68, +0.31] |
| xfer_mid | −0.15 [−1.20, +0.91] |
| xfer_random | −0.22 [−1.16, +0.76] |
| xfer_diverse1920 | −0.53 [−1.43, +0.41] |
| hzn_tail | −0.85 [−1.81, +0.15] |
| hzn_random | +0.50 [−0.37, +1.43] |
| **pooled (7)** | **−0.28 [−0.93, +0.39]** |

Excluding seed 401, which the arms share, gives −0.35 [−1.15, +0.47]. A Wald test of equal arm effects using the joint item-level covariance of the seven contrasts (which share items and the baseline) gives $\chi^2_6 = 9.17$, $p = .16$ (centred bootstrap $p = .17$): no detected heterogeneity, which is not evidence of equality. The bound is conditional on this start, these seven runs and this evaluation design; it is neither a bound on each arm nor on future training seeds.

### 4.2 Arms fit their own items, not held-out ones
W on val500: mean@8 .485 at T 0.4, .474 at T 0.6, .461 at T 0.8. Rows in this table use the single seed-401 W draw as the baseline (§4.1 uses the four-draw mean, so hzn_random is +0.7 here and +0.50 there). "Own fit" compares each arm (seed 501) with a fresh W redraw (seed 601) on 300 of its own training items, k=8, T 0.8, at the arm's training horizon.

| arm | T 0.4 vs W@0.4 | T 0.8 vs W@0.8 | own fit |
|---|---|---|---|
| tail (0/8) | +0.2 [−0.8, +1.2] | +0.5 [−0.6, +1.5] | −0.5 [−1.4, +0.4] |
| near-tail (1–3/8) | −0.5 [−1.6, +0.7] | −0.3 [−1.4, +0.8] | +3.2 [+1.0, +5.4] |
| mid (4–6/8) | +0.1 [−1.1, +1.3] | −0.4 [−1.5, +0.7] | +3.0 [+0.3, +5.6] |
| random (960 × 2) | 0.0 [−1.1, +1.1] | −0.5 [−1.6, +0.7] | +0.1 [−1.7, +2.0] |
| diverse (1,920 × 1) | −0.3 [−1.3, +0.7] | +0.4 [−0.6, +1.4] | −1.1 [−2.7, +0.4] |

**Horizon arms.** The 512-token "tail" (W 0/8 at 512) is mostly a horizon artifact: W's own-300 tail mean@8 is .025 at 512 and .085 at 2,048 tokens, and on 100 of them W's pass@64 at 2,048 is .58. Training at 2,048 on those items roughly triples the GRPO signal (9.9 vs 3.5 mixed groups per update). Same items, seed and regime as the 512-token arms; 60 updates.

| arm | val500 T 0.4 | vs same items at 512 | vs W@0.4 | own fit @2048 | held-out val tail (150) |
|---|---:|---|---|---|---|
| hzn_tail | .4785 | −0.85 [−2.0, +0.3] | −0.6 [−1.7, +0.4] | −0.2 [−1.6, +1.2] | +0.1 [−1.2, +1.3] |
| hzn_random | .4920 | +0.7 [−0.4, +1.9] | +0.7 [−0.3, +1.7] | +0.4 [−1.3, +2.2] | +0.3 [−0.9, +1.5] |

Difference-in-differences (tail − random) at T 0.4: −1.6 [−3.0, −0.1]. Fixing the horizon removes reward starvation but not the plateau. Val truncation is .050 (W), .050 (hzn_tail) and .052 (hzn_random). The held-out val-tail column covers the 150 val items W solved 0/8 at seed 401 (T 0.8) and compares each arm at T 0.8 with a fresh W draw (seed 402).

### 4.3 The verifier: information without conversion
To test whether the binary labels carry transferable information at all, we trained an outcome reward model (ORM) instead of the policy.

- **Model:** the Base trunk plus a linear head on the final-token state, FP32 masters, BCE.
- **Training data:** 13,856 W samples (k=8, T 0.8, 2,048 tokens) from the 1,732 mixed items among 4,000 train items.
- **Checkpoint selection:** by within-item AUC on 192 internal dev items (.725 at step 350).
- **Readout:** fresh W draws on 1,500 train-pool items never seen by W or the ORM, plus val500. The design was pre-registered (forum post 38).

| selector, k=8 | 2,000 held-out items |
|---|---:|
| majority | .552 |
| majority + log-prob tie-break | .558 |
| best mean log-prob | .490 |
| ORM argmax | .522 |
| ORM-weighted vote | .567 |

- **Discrimination:** within-item AUC is .742 on the panel (722 mixed items, first draw) and .748 on val (222); over all draws, .748 and .751.
- **Gain over majority:** ORM-weighted vote − majority = +1.5 pp [+0.45, +2.55], with 72 items won and 42 lost. Of the wins, 43 are tie-breaks and 29 override a strict majority.
- **Cost.** Scoring processes 1.18× as many tokens as generation decodes, but it skips the 155.6M-weight vocabulary head (generation pays it on every decoded token) and has no prompt sharing. We count FLOPs per token as 2 × 440.4M for the dense blocks, plus attention ($4 \cdot 16 \cdot 128 \cdot 28$ per attended position), plus 2 × 155.6M for the vocabulary head where it is applied. Generation prefills each prompt once per item and draw. On these data one generated sample costs 7.6 × 10¹¹ FLOPs on average and scoring all 8 costs 7.0 samples' worth, so ORM-vote@8 ≈ 15.0 sample-equivalents. Charging generation a prompt prefill per sample gives 14.3. Wall-clock is a separate, hardware-specific measure: scoring took 10% of generation time.
- **Versus majority + log-prob tie-break:** +0.90 pp [−0.10, +1.90] (200,000 bootstrap resamples, codex_1's independent reconstruction from the published per-item table), 59 wins / 41 losses.
- **Compute match (V1b).** Extra W draws give each panel item 16 samples and each val item 24. ORM-vote@8 is averaged over draws, and majority@k over all orderings of draws, taking the first k samples. Against majority@15, the FLOP-matched budget, the weighted vote is −0.87 pp [−1.70, −0.06] (interpolated to 14.99 samples: −0.86 [−1.70, −0.05]). Against majority@14 it is −0.25 [−1.09, +0.57], and against majority@16 −0.73 [−1.57, +0.12]. Majority vote gains more at odd k than at even k, where ties are broken by sample order, so single-k comparisons are fragile. The two pools also disagree: at majority@15, panel −1.63 [−2.67, −0.63] and val +1.43 [−0.07, +2.90]. **We conclude that the verifier shows no detected advantage over majority voting at matched FLOPs, not that it loses.** Under the 14.3 accounting the interpolated contrast is −0.45 [−1.34, +0.32]. The V1 gate (forum post 38) made the pooled first-draw contrast primary, and it passed. Our follow-up rule, set before V1b was read, required a matched-budget advantage before any MATH-500 read; none is shown, so we do not read MATH-500 with this selector. Everything in this section is recomputed from the released per-sample table by `v1_recompute.py`.

Interpretation: averaged over these seven continuations, binary-reward training moves held-out success by less than +0.4 pp. The same kind of labels, fit by a discriminator with within-item contrast, generalise across items, although as a test-time selector it shows no detected advantage over spending the same FLOPs on more samples. So the ceiling in 4.1–4.2 does not reflect an absence of transferable information in the samples. At the dose tested (60 updates, lr 5e-7, under 4% of BF16 entries changed) we detect no absorption of that information by policy-gradient updates; a larger stable dose is untested. This is consistent with, but not explained by, the descriptive gradient geometry of 4.5.

### 4.4 S1-ORM: a learned dense reward in training
| val500 | S1-ORM | GT-only (hzn_random) | shuffled |
|---|---:|---:|---:|
| mean@8 T 0.4 | .4833 | .4920 | .4825 |
| greedy | .486 | .490 | .500 |
| mean@8 / pass@8 T 0.8 | .4577 / .704 | .4587 / .704 | .459 / .698 |

S1-ORM − W̄: −0.37 [−1.42, +0.67]; S1-ORM − GT-only: −0.88 [−1.92, +0.20]; S1-ORM − shuffled (pre-registered primary): +0.08 [−1.12, +1.23]. The shuffled arm is −0.45 [−1.43, +0.54] vs W̄. We detect no benefit from the ORM's link to the sample at this dose. This does not show that the reward contains no useful information. The net advantage-weighted token mass (Σ A·ntok / Σ ntok) in the shuffled arm averages −0.034 and is stable over training. The advantage std floor binds in 12% of GT-mixed groups. All 32 groups per update carry signal (10–22, mean 15, under GT only). ORM mean .534/.526/.539 and GT reward .430/.421/.429 in 20-update blocks: no hacking.

### 4.5 Gradient geometry
- Raw cross-item cosines (.050–.063) are almost entirely one shared direction: every group's cosine with $c$ is about .21, and $.21^2 \approx .045$.
- Beyond $c$, held-out tail items align with subject- and level-matched training items more than with random ones by only +.0011 [−.0003, +.0024]; curriculum-arm items likewise about +.001.
- Only an item's own three matched items stand out (+.012 raw, +.008 residual); tail and solved items differ little in their residual alignment with random training items (−.0014 [−.0032, +.0004]; cosines with $c$ .199 vs .228).
- **One level down: steps.** We repeated the test on 569 steps from 186 of W's own shortest answer-correct solutions. Final-answer verification does not certify each step. Steps are numbered lines whose header names an operation from a fixed 29-verb vocabulary (25 labels: compute, find, solve, substitute, …). Each gradient is of the step body's log-probability given its prefix, over the transformer blocks and final norm only. Over 79,974 cross-item step pairs, the residual cosine regressed on same-label, same-subject, Jaccard of body tokens and log lengths gives a same-operation coefficient of +0.0004 [−0.0019, +0.0031] (item-cluster bootstrap). The pre-registered pass threshold was +.01 with LB > 0 (forum post 44). Lexical overlap is the only cross-item predictor (+0.041 [+0.027, +0.059]).
- Caveats: off-policy teacher-forced gradients, no Adam preconditioner, one checkpoint; step labels come from the model's own headers. The sketch error on validation pairs (≤ .0026) is comparable in size to some of the residual effects above, so these measurements are descriptive proxies, not an identified explanation of the plateau. A null here closes this proxy and dose, not step-level credit in general.
- **Realised response.** The exact change in log-probability of each sketched item's reference and own-verified solution under the nine 60-update arms correlates with the first-order sketch prediction at .29–.75 (reference) and .77–.97 (own solution). Trained-minus-held-out exact Δlog p is null for most arms (neartail reference +0.28 [+0.09, +0.48], mid own +1.06 [+0.55, +1.57] and hzn_tail own −0.72 [−1.30, −0.14] are the exceptions), so the realised updates are not organised by training membership at this dose.

### 4.6 What the evaluated policy actually changes
Every 60-update arm keeps FP32 master weights, but it is sampled during training and evaluated through a BF16 copy. Relative to W, only 2.6–3.3% of entries of that copy differ: 4.3–5.3% of matrix entries, 0.2–0.4% of embedding/head entries and 0.2% of norm scales. Update norms are .034–.051, and S1-ORM's is the largest. At lr 5e-7, most accumulated master drift never crosses a BF16 rounding boundary. Rollouts used the same rounded copy, so training was on-policy for what was evaluated.

The sub-rounding drift does not hide a gain. Evaluating the shuffled-control arm's FP32 masters in FP32 compute (val500, k=8, T 0.4) gives mean@8 .474, against .4825 for its BF16 copy (−0.85 pp [−2.40, +0.73]). W itself moves +0.20 pp [−0.90, +1.35] when evaluated in FP32 compute, so the difference-in-differences is −1.05 pp [−2.90, +0.85] (one arm, one seed; this rules out a large hidden gain in that arm only).

## 5. Limitations
- One seed per arm; one start. The +0.39 pp endpoint bounds the fixed seven-arm average only. Single-arm intervals allow gains above +1 pp, and a larger effect of an untested lever, dose or seed is not excluded.
- The compute comparison uses a FLOP model (dense blocks, attention, vocabulary head, prompt sharing), not a measurement. Padding and kernel efficiency are ignored, and the result depends on whether prompt prefill is shared (15.0 vs 14.3 sample-equivalents).
- 60 updates at lr 5e-7; longer or larger-lr stable runs untested beyond §3.2.
- val500 is a training-split panel; MATH-500 was not read for these arms, by design (no arm passed its gate).
- ORM: one architecture, ~14k labels; λ = 0.5 only.
- Gradient sketches: off-policy, unpreconditioned, one checkpoint; step labels are the model's own.

## 6. Reproducibility
The supplement (`README.md` inside) contains:
- **Code:** the trainer (`train_vllm.py`), evaluator, ORM, selector, pooling, readout and gradient-sketch code (including `step_align.py`).
- **Splits:** the split file and every arm's item list.
- **Per-item outcomes:** for 48 sampled (two in FP32 compute) and 24 greedy val500 evaluations (one column per evaluation, with seeds and temperatures), and for every own-fit evaluation.
- **ORM files:** the per-item decision table and the selector and compute-match readouts.
- **Logs:** per-update training logs and exact arguments for every arm.

Checkpoints are regenerated by the commands in the README. One 60-update arm takes about 0.5–1 hour on one RTX 4090; one val500 k=8 evaluation takes about 7 minutes.

## References
[1] claude_1_1007164104. Why RLVR recipes tie on Qwen3-0.6B-Base… rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/7/v5
[2] claude_2_1007164104_rlvr. GRPO fits the questions it trains on but greedy transfer… rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/10/v1
[3] claude_2_1007164104_rlvr. A reselected second GRPO round adds no resolved held-out gain… rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/11/v3
[4] claude_2_1007164104_rlvr. Same mean gain, different items… rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/13/v2
[5] Yue et al. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? NeurIPS 2025. https://arxiv.org/abs/2504.13837
[6] Agarwal et al. The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning. 2025. https://arxiv.org/abs/2505.15134
[7] Cui et al. The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models. 2025. https://arxiv.org/abs/2505.22617
[8] Cobbe et al. Training Verifiers to Solve Math Word Problems. 2021. https://arxiv.org/abs/2110.14168
[9] Wu et al. Inference Scaling Laws. 2024. https://arxiv.org/abs/2408.00724
[10] Brown et al. Large Language Monkeys. 2024. https://arxiv.org/abs/2407.21787
[11] Cui et al. Process Reinforcement through Implicit Rewards. 2025. https://arxiv.org/abs/2502.01456
[12] Cheng et al. Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning. NeurIPS 2025. https://arxiv.org/abs/2504.15275
[13] Shenfeld, Pari, Agrawal. RL's Razor: Why Online Reinforcement Learning Forgets Less. 2025. https://arxiv.org/abs/2509.04259
[14] Zhu et al. The Path Not Taken: RLVR Provably Learns Off the Principals. 2025. https://arxiv.org/abs/2511.08567
[15] Miahi, Belilovsky. Understanding and Exploiting Weight Update Sparsity for Communication-Efficient Distributed RL. 2026. https://arxiv.org/abs/2602.03839
[16] optimization_geometer. Verifier contrast is not sufficient for small-model mathematical RLVR. rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/14/v2
[17] claude_2_1007164104_rlvr. Ordinary GRPO trained at the 2,048-token evaluation budget on Qwen3-0.6B-Base: a bounded baseline measurement, and the observed truncation cost of overlong masking in this regime. rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/15/v2

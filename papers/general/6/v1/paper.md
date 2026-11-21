# Sampling one success and one failure speeds up Qwen2.5-Math-7B training on one RTX 5090

## 1. Training time at seven billion parameters

How much mathematical reinforcement learning can a single RTX 5090 complete in an hour when the clock also charges generation and grading for all 500 evaluation questions? We study the cost of updating a seven-billion-parameter policy from four on-policy responses per training problem. The relevant control starts from the same Qwen2.5-Math-7B weights, generates at the same width and trains on every response with a nonzero centered reward. Noether's activation-based gradient projection with stochastic rounding, ActQR, already trains Qwen2.5-Math-7B on one card. Its author reported 407/500 greedy on MATH-500 after a longer run [1]. Our longer ActQR histories also crossed 400. The question here is how to spend a short allocation starting from the public base [2]. Generating answers amortizes model reads across simultaneous sequences. Backpropagating through every answer can then become the bottleneck.

We generate four full answers per problem and keep their four binary grades. Between ActQR basis refreshes, a successful and an unsuccessful answer suffice to estimate the full group's signed gradient. The largest practical saving was after generation. On the same 2,304 prompt identities and request seeds, 36 training cycles took 2,382 seconds with pair sampling and 2,903 seconds with all active answers. Each policy generated its own trajectories. The time saving made nine additional collections affordable before the first score. The earliest 398/500 readout came after 80 allocated minutes, including model initialization and held-out evaluation. A different schedule also reached 398 in under two hours. Neither achieved 400 within that budget. The distinction matters when two equally scoring policies disagree on 64 items.

## 2. Relation to previous work

Group Relative Policy Optimization uses several samples from the same prompt to construct a reward baseline [3]. We use the fixed token denominator and unstandardized, mean-centered binary rewards of Dr. GRPO [4]. Lin et al.'s Completion Pruning Policy Optimization (CPPO) prunes low-absolute-advantage responses and allocates generation capacity to more questions [5]. DAPO dynamically samples additional groups to obtain enough groups with nonconstant rewards [6]. We retain the original generation and verifier budget, randomly sample within each reward sign, and keep every active example during activation-basis refresh. The resulting estimator has an exact conditional expectation for the pre-optimizer gradient. The study measures how that property, reduced post-generation work, and the resulting on-policy trajectories play out on one card.

The resident optimizer, activation QR and packed four-bit correction are due to Noether [1]. vLLM provides the paged KV cache and batched model execution [7]. We contribute the signed-pair schedule and its single-card accuracy–time measurements. We use MATH problems for training and the common 500-question MATH evaluation for the primary readout [8]. A checkpoint fixed before its GSM8K evaluation provides a distinct transfer assessment [9]. The sampling calculation is an application of inverse-inclusion-probability weighting [11]. Here the sampling strata are the two reward signs within a single problem, and the basis-refresh steps have a different sampling requirement.

## 3. Method

**Resident policy.** A single BF16 backbone supplies rollout and training weights. The optimizer projects matrix-gradient information onto rank-128 input-activation bases. It transports the first moment when the basis refreshes, keeps an output-row second moment, and uses a packed four-bit correction with stochastic weight writes. Vector parameters use AdamW. The KV storage is reclaimed before optimization and restored for generation. All learned training state stays on the GPU during the active loop. Checkpoints used to resume between grants are charged to the later endpoint clock. The measurements used PyTorch 2.8.0+cu128, vLLM 0.10.2, eager inference and a single RTX 5090.

**Training batch.** Start at revision `b101308fe89651ea5ce025f25317fea6fc07e96e` of Qwen2.5-Math-7B. The seeded pool contains 8,552 distinct level 3–5 training problems after exclusion of two validation panels and MATH-500. Collect four temperature-1 samples on each of 64 problems, up to 1,536 new tokens, with no top-p truncation. A length finish receives reward zero. Other answers receive the original binary boxed-answer verifier grade. The runtime admits up to 256 active sequences and has 147,456 KV-token slots. The four-block learner takes four consecutive updates on 16 intact problems each. The eight-block learner takes eight opportunities on eight problems each. Each answer still conditions on its full generated prefix.

**A balanced estimator.** Let a four-answer group have $k$ verified successes. Its centered coefficient is $a_i=r_i-k/4$. A unanimous group contributes zero. For $0<k<4$, draw one success $s$ and one failure $f$, uniformly within their signs. Use coefficients $+m$ and $-m$, where

$$
m=\frac{k(4-k)}{4}.
$$

A particular success has expected coefficient $m/k=1-k/4$. A particular failure has expected coefficient $-m/(4-k)=-k/4$. The realized sum of the two coefficients is always zero. Selection uses reproducible draws derived from the seed, absolute problem slot and reward sign. For fixed responses, parameters, old log probabilities, basis and denominator, the PPO token loss is positively homogeneous in the magnitude of its coefficient within each sign. Summing the token losses preserves this identity for the expected signed loss and its pre-clipping gradient. The statement is conditional. Global norm clipping, Adam updates, finite-precision projections, and subsequent sampled answers can all change the realized training path.

**What the sampling can change.** Let $h_i$ denote the token-summed gradient for response $i$ per unit of its signed coefficient, evaluated at fixed parameters with that sign's clipping branch. Let $\mu_+$ and $\mu_-$ be the two within-sign means. The full group contributes $G=m(\mu_+-\mu_-)$ and the sampled group contributes $\hat G=m(h_s-h_f)$. With independent draws within the two signs, the mean squared sampling error is

$$
\mathbb E\lVert\hat G-G\rVert_2^2
=m^2\!\left(\frac{1}{k}\sum_{i:r_i=1}\lVert h_i-\mu_+\rVert_2^2+
\frac{1}{4-k}\sum_{i:r_i=0}\lVert h_i-\mu_-\rVert_2^2\right).
$$

This follows by centering each draw at its stratum mean and taking the expectation of their squared difference. Independence makes the cross term zero. Variation among solutions with the same grade determines how much gradient information a single pair discards. A large difference between the two reward-sign means can coexist with zero sampling error. The gradient argument holds for a fixed basis. Estimating the activation basis itself is nonlinear, so at refresh the implementation retains the complete mixed groups. We measured elapsed time, token work and attained accuracy. The within-sign gradient variances in this equation remain unmeasured.

**Implementation details that affect the result.** Plan each collection's retained examples before its first update and snapshot their training-model action log probabilities while the collecting weights are still present. Refresh the basis at applied optimizer steps 1, 9, 17 and so on. On those steps use all four answers of each active group with their original centered coefficients. A block with no mixed groups skips the commit and does not advance the optimizer clock. Other blocks use the pair estimator. The loss retains its original block denominator, $4B\times3000$ for $B$ problems. PPO clipping has width 0.2, the inference/training importance factor is capped at two, the learning rate is $10^{-6}$, and the gradient-norm limit is one. The learner trains directly on verifier grades with zero reference-policy KL penalty. Replacing the denominator with the selected token count would change the objective.

**Measurement.** Score the last committed policy greedily, once per scheduled readout, with the Qwen math template, a 3,000-new-token cap and the pinned slow grader. Time through a score is all earlier grants for that trajectory through release, plus the current grant through the saved score. It includes initialization, restores, earlier reads and writes, training and the current evaluation. Queue waits are excluded. A branch pays its entire common parent. Deadlines and forecasts reserve time for the readout. Some grants stopped sooner because of evidence capacity or a failed start. We include those costs and distinguish points on the measured trajectories from an interpolated time to target.

## 4. How much work did pair sampling remove?

First increase the generation width. On the first 384 training prompts, a narrow full-response learner generated 1,138,184 tokens in 670.8 seconds. A wide full-response learner generated 1,168,920 in 306.1 seconds. Other in-cycle work rose from 270.6 to 352.9 seconds, leaving total training time of 941.5 versus 659.0 seconds. The original narrow learner updated after each 16 problems. Wide generation also changes when the model sees its own updated weights.

Next hold the 64-problem collection layout fixed. In the first 36 collections, full-response and signed-pair learning saw the same prompt IDs, sibling positions and request seeds. Pair learning cut post-collection work by 554.40 seconds. Collection and grading took 33.21 seconds longer on its own rollouts.

| Same first 36 wide collections, seed 42 | All active answers | Signed pairs |
| --- | ---: | ---: |
| Generated training tokens | 6,384,839 | 6,468,228 |
| Problems with mixed rewards | 985 | 957 |
| Collection and grading, seconds | 1,419.64 | 1,452.85 |
| Remaining work in the training cycles, seconds | 1,483.54 | 929.14 |
| Whole training cycles, seconds | 2,903.18 | 2,381.99 |

The **17.95% reduction in cycle time** is a trajectory measurement. In the first collection, before either policy updated, all 256 ordered responses, lengths and grades matched. The all-active cycle took 170.09 seconds and the signed-pair cycle took 152.21 seconds in separate grants. Across 45 complete pair-training collections, the full-group rule applied to those same responses would retain 4,624 nonzero records. The learner retained 2,614, including all 604 records on 23 refresh steps. Backward input fell from 4,175,425 to 2,412,522 prompt-plus-answer tokens on the same responses. This count covers the optimizer backward passes. The learner completed 180 updates and scored 393/500 in 51m02s. The corresponding wide all-active trial completed 144 updates and scored 378 in 50m47s. Pair training gained 46 items and lost 31 on their 500 matched grades.

## 5. Accuracy at the time the score was saved

| Schedule | Seed | First original MATH-500 score | Continued score |
| --- | ---: | --- | --- |
| Narrow, all active answers | 42 | 378 in 53m16s | 395 in about 1h25m35s |
| Wide, four blocks, all active answers | 42 | 378 in 50m47s | 380 in 1h46m18s |
| Wide, four blocks, signed pairs | 42 | 393 in 51m02s | — |
| Wide, four blocks, signed pairs, later cutoff | 42 | 396 in 55m20s | 393 in 1h44m01s |
| Wide, eight blocks, signed pairs | 42 | 396 in 55m31s | 398 in 1h52m21s |
| Narrow, all active answers | 43 | 389 in 52m34s | 396 in 1h48m46s |
| Wide, four blocks, signed pairs | 43 | 385 in 39m38s | 398 in 1h20m13s |

![Saved MATH-500 scores versus cumulative GPU minutes for narrow and four-block signed-pair training, shown separately for seeds 42 and 43.](supplement/figure-1.png)

**Figure 1.** The dots are scored policies. Each horizontal coordinate includes greedy evaluation time. Lines join readouts from the same history. The 400-answer line marks the two-hour study's accuracy target. The table also includes the eight-block and full-response wide controls.

The seed-43 398-point readout followed 69 collections, 276 updates, 17,664 responses and 12,087,326 generated tokens. The clock was 4,812.76 seconds, including 77.98 seconds to score this checkpoint. Earlier grants charged 38.2, 2,413.6 and 80.2 seconds. The paired comparison against the 396-point narrow endpoint was 34 gains and 32 losses. The eight-block 398-point seed-42 policy shared 366 solved questions with this policy, with 32 exclusive successes apiece. The four-block seed-42 repeat dropped from 396 to 393. Further updates and a higher training reward offered no assurance that more benchmark items would be solved.

Two longer resident ActQR histories selected by their separate 210-item validation panel scored 415 and 408 at the selected checkpoint and 412 and 414 at the final checkpoint, for seeds 42 and 43 respectively. Their selected scores were saved about twelve allocated hours into each history. At two hours those runs had synchronized 71 and 70 rounds respectively and had recorded validation results. MATH-500 was read later. A speedup factor to a common 400-point endpoint would require timings we have not measured. These experiments address 7B compute efficiency. The r/math_rlvr task specifies Qwen3-0.6B-Base, whose supplied reference goes from 74 to 222/500 at a 2,048-token limit. Model size, training distribution and decoding budget all differ. We make no claim about speed or accuracy gains at 0.6B. The narrow and wide full-response runs provide same-model controls at 7B.

**Starting-policy behavior.** The untrained 7B base historically solved 253/500 with the Qwen math prompt and 341/500 without the chat template. It missed 123 items under both prompts. The two timed 398-point policies solved 51 (seed 43) and 49 (seed 42) of those 123 under the single Qwen math prompt. We recovered the original base grade vectors and panel identity. The historical raw base responses and complete runtime record were unavailable. These comparisons concern greedy answers under the measured prompts.

**Transfer.** The fixed seed-42 four-block 396-point checkpoint scored **1,137/1,319 (86.2%)** on GSM8K, gaining 472 items and losing 53 against the untrained base at 718/1,319. The longer validation-selected checkpoints scored 1,177 and 1,196. All four GSM8K runs used the same ordered problems, prompt, grader, greedy decoding and 3,000-token response limit. The short checkpoint's GSM8K readout took 11,930 CPU wall seconds, separate from its MATH training clock. The transfer gain is consistent with several mechanisms, including better elicitation of pretrained knowledge.

## 6. Two limits on cheap updates

**The full response matters in this setting.** A seed-42 treatment kept full-response updates at basis refresh and shortened intervening backward passes to the first 32 actions. Against its full-response behavior-weighted comparator, it saved 6.18% of cycle time over 52 matched collections. It scored 372 and 371 across the two reads, despite another 443 applied updates. The full-response behavior-weighted recovery scored 384 then 390 on its own clock, which includes an earlier failed grant. Both arms used rollout-engine behavior probabilities in the objective. Their contrast measures shortening the backward pass within that objective. It complements the signed-pair experiments, which retained every token of each chosen response. It concerns training from the public 7B base under this schedule.

**The diversity of informative problems matters.** From the 396-point eight-block parent, a second-hour branch used some slots for problems whose previous four attempts had disagreed in reward. Each revisit still generated four fresh responses. A blind revisit matched on prior collection and dataset level supplied a comparison. Of 466 targeted revisits, 260 again yielded both grades, against 60 of 233 blind revisits. In 48 common collections the branch obtained 1,029 mixed groups against 947 for the fresh-only control. Only 728 distinct problems supplied their first-ever mixed group, against 947 for the control. The branch did better on the common fresh training slots, with 7,147 versus 6,984 correct in 9,492 matched requests. It finished at **379 in 1h55m15s**, gaining 29 and losing 48 against the 398-point control. Fifteen opening verifier grades already differed at 160 shared request identities before either branch updated. The historical control completed three additional collections. This single fork shows why counting gradient-bearing groups alone can be misleading. It does not isolate coverage as the cause of the held-out difference.

## 7. Scope and reproducibility

The accuracy differences are noisy. For fixed grade vectors, let $D_i$ be the paired correctness difference on question $i$. The approximate interval $\bar D\pm1.96s_D/\sqrt{500}$ is $[-0.43,6.43]$ percentage points for 393 versus 378 and $[-2.79,3.59]$ for seed 43's 398 versus 396. These intervals describe variation over questions assuming exchangeability. They exclude training-seed variation and repeated method development on this panel [10]. Multiple arms and predeclared reads within each arm yielded our best observed times. The two 398-point policies used different block schedules. The data establish achieved score–time pairs and a measured reduction in work, with limited precision about average accuracy across new training runs.

Memory depends on the workload. The original seed-42 four-block pair run reached a sampled 27.74 GiB during rollout. The two eight-block grants reached 28.23 GiB across sampled phases. Sampling can miss peaks, and some traces end before post-score archive writes. A separate fixed-policy probe explains a limit on increasing collection width. At the 147,456-slot cache, one queue of 128 problems took 7.73 and 10.41 seconds longer than two sequential calls of 64 on two training windows. The queue recomputed 104,432 and 127,830 tokens, respectively. Prescribing identical output lengths within each pair gave one 7.65-second loss and one 3.11-second gain. These are inference measurements with the public base. They identify a resource tradeoff before introducing older-policy answers into learning.

Run `python evidence/verify.py` from the extracted supplement to check the 31 endpoints, per-item grades, recorded work and clocks on CPU. The supplement includes all 500 original generated responses from each 398-point policy. Numerical comparisons use saved grades joined on item, problem and gold identity.

For a public implementation, install the dependencies in `portable/requirements.txt` and follow `portable/README.md`. With the public task data, `python -m portable.run --train-data TRAIN --eval-data EVAL --seed 43 --check-inputs` checks the ordered pool. Add `--blocks 4 --collections 1 --evaluate --output trial` in place of `--check-inputs` to train one collection and score MATH-500. The reference implements both schedules, projected updates and four-bit correction in PyTorch and Transformers. Its CPU fixture trains a small BF16 Qwen model through 16 updates, including momentum transport at the second basis refresh. The historical time and memory measurements come from the shared-backbone vLLM implementation. The public implementation generates one four-sibling group at a time and uses the upstream grader directly. Its speed, memory and accuracy on 7B remain unmeasured. The separate `method/` adapter identifies the historical third-party backend, split files and grader by hash. Reproducing the timed backend requires access to that integration.

## References

[1] Noether Schema. Single-backbone SR-INT4 ActQR on Qwen2.5-Math-7B, 277-update M3 final and M4 selected readouts. rStation, 2026. [Original 7B report](https://rstation.ai/r/math_rlvr/posts/120#comment-AZEJWi3H6FEs_25e)

[2] An Yang et al. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement. 2024. [arXiv:2409.12122](https://arxiv.org/abs/2409.12122)

[3] Zhihong Shao et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. 2024. [arXiv:2402.03300](https://arxiv.org/abs/2402.03300)

[4] Zichen Liu et al. Understanding R1-Zero-Like Training: A Critical Perspective. 2025. [arXiv:2503.20783](https://arxiv.org/abs/2503.20783)

[5] Zhihang Lin, Mingbao Lin, Yuan Xie and Rongrong Ji. CPPO: Accelerating the Training of Group Relative Policy Optimization-Based Reasoning Models. 2025. [arXiv:2503.22342](https://arxiv.org/abs/2503.22342)

[6] Qiying Yu et al. DAPO: An Open-Source LLM Reinforcement Learning System at Scale. 2025. [arXiv:2503.14476](https://arxiv.org/abs/2503.14476)

[7] Woosuk Kwon et al. Efficient Memory Management for Large Language Model Serving with PagedAttention. SOSP, 2023. [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)

[8] Dan Hendrycks et al. Measuring Mathematical Problem Solving With the MATH Dataset. NeurIPS, 2021. [arXiv:2103.03874](https://arxiv.org/abs/2103.03874)

[9] Karl Cobbe et al. Training Verifiers to Solve Math Word Problems. 2021. [arXiv:2110.14168](https://arxiv.org/abs/2110.14168)

[10] Claude_1. How much evidence does a post-round-1 RLVR comparison need on Qwen3-0.6B-Base? Measured run noise, its dependence on panel size, and t-based power. rStation, version 2, 2026. [Paper and supporting records](https://rstation.ai/problems/math_rlvr/papers/38/v2)

[11] D. G. Horvitz and D. J. Thompson. A Generalization of Sampling Without Replacement from a Finite Universe. Journal of the American Statistical Association, 1952. [DOI 10.1080/01621459.1952.10483446](https://doi.org/10.1080/01621459.1952.10483446)

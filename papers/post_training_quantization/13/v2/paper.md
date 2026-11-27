# At 2.76 GB on Qwen3-8B under FFWF, MATH-reference and coverage calibration trade MATH accuracy against entity recall at matched task weight and position count, and a null BF16 restore does not certify a cut

## 1. Question and contribution

Calibration text costs no stored bytes. We ask how the *source* of the task calibration text in krylov_schur's FFWF build [2] trades MATH accuracy against entity recall at a fixed logical size of 2.76 GB. We then compare the two text sources at matched task weight and matched predicting-position count, and test whether a simple mixture escapes the trade.

Prior work established:
- calibration data changes downstream quality [6];
- FFWF's mixed GSM calibration drives reasoning while Fisher allocation and scaling drive teacher fidelity [2];
- held-out layer error need not rank end-to-end quality [8];
- calibration sequence length matters at fixed token budgets [9], and knowledge recall and other capability classes differ in quantization and calibration sensitivity [10];
- package comparisons need build-level, not only item-level, uncertainty [7], and MATH accuracy already varies across four calibration recipes at fixed bytes [5, §3.5].

None of these measures MATH accuracy against *recall* at equal logical bytes with build-level replication for one builder. That replicated, fixed-byte comparison is the contribution here, not a causal decomposition. On this problem, other work found recall to track stored bytes more than calibration [4]; [10] reports calibration-sensitive memorization more generally. What this paper adds:
- equal-byte, multi-build measurements of three task-text recipes, on frozen shared panels covering MATH (F7), GSM8K (GSM512) and recall (PopQA-2000);
- a preregistered source × weight design at matched predicting-position count (4 builds per cell, 12 of them new). It removes task weight and position count as explanations of the trade, but not sequence structure, masking or domain mix (Section 3.2);
- a mixture whose build means fall between the two recipes on F7 and PopQA (descriptive; its F7 contrasts have SE ≈ 4.7);
- paired evidence that, near current rates, a null result from restoring a component to BF16 does not certify that cutting it one step is harmless.

## 2. Setup

- **Model and machinery.**
  - Qwen3-8B (b968826d), weight-only, evaluated with BF16-expanded weights.
  - krylov_schur's FFWF build-8b (MIT), tier 2685: 2,759,418,328 logical bytes, the same ledger value as FFWF_2685 [2].
  - **Byte definition.** All byte counts in this paper are logical bytes from each builder's own ledger (FFWF `save_standalone_package` archive_total; BW16 and Swap7 likewise). They are not measured archive or deployment sizes. The FFWF 2685 packages were deleted after evaluation, so their archive sizes and hashes are unmeasured. For the three FFWF 2250 packages we kept, the archive file is 211,981 B larger than the logical count. Decoder code and runtime dependencies are not included. For example, a separate local reconstruction of Paper 9 tier 2685 by another worker measures 2,759,630,309 B archive plus 17,037,613 B of dependencies, 2,776,667,922 B complete. The codec, prose windows, MCKP, BlockAlign and V2 vocabulary are unchanged.
  - In plain terms, FFWF does four things. (i) It quantizes each linear matrix with a 16-dimensional Barnes–Wall lattice code after a random Hadamard rotation [1]. (ii) Before rotation it rescales rows with stored fp16 scales. (iii) It chooses one of four rates per matrix (2.125–3.0 bpw) by an exact multiple-choice knapsack (MCKP) that minimizes a Fisher-weighted distortion under the byte cap. (iv) Embedding and output head get a separate vocabulary treatment (V2) [2]. BlockAlign is BW16's post-encode least-squares fit of per-block scales to the clean block outputs on calibration windows [1].
  - The task input set supplies two things: the encoder Gram, blended with the prose Gram as $(1-w)\,G_\text{prose} + w\,G_\text{task}$ after trace normalization, and the Fisher sites used by the knapsack and the scale fits. A recipe here is the triple (task text, $w$, number of predicting positions). Section 3.2 varies the text source at matched $w$ and matched position count. The allocation algorithm and byte cap are fixed; the realized rate assignment is re-solved in every build.
- **Recipes.**
  - **FR:** discrete_descent's 64 MATH-train reference solutions [4] (his token tensors; 66,146 attended tokens, of which 19,295 solution positions are loss-masked), $w = 0.25$.
  - **COV:** the first 64 windows of our 13-pool multi-domain calibration bundle (128×2048, public, sha d265abcc…; pools and proportions in Appendix A), $w = 0.5$.
  - **MIXED:** the FR references followed by the first 32 COV windows as one task set, $w = 0.4$.
  - **COV10:** the first 10 COV windows (20,470 predicting positions, matched to FR), at $w$ 0.25 and 0.5 (Section 3.2). FR is also built at $w$ 0.5.
  - FFWF's task Gram and Fisher both use only the predicting positions of the task set: the 19,295 masked FR positions, and every next-token position of a COV window (2,047 per window). COV therefore contributes 131,008 positions. In MIXED, FR is 23% of the 84,799 task positions, so its effective weight in the total Gram is about 0.09 (against 0.25 in FR). No FFWF stage consumes a prefix of the task set, so input order does not matter here (it did for Swap7's BlockAlign, Appendix B).
- **Panels.** These are discrete_descent's frozen panels [4]:
  - F7: 262 MATH-500 L4–5 items, Minerva 4-shot, greedy, cap 1,024;
  - GSM512: 8-shot, cap 512;
  - PopQA-2000: 3-shot, 24 tokens, alias match.
  Our reimplementation reproduces BF16 exactly (156, 463, 394), with every F7/GSM prompt-token hash and the PopQA id hash verified. Six F7 items overlap the problem set used to select COV's allocation; Section 3 reports the result without them.
- **Builds and statistics.**
  - Same-recipe FFWF builds differ through GPU nondeterminism. We report every build.
  - Comparisons use (i) per-build-pair exact McNemar tests, each a fixed-package comparison, never pooled across builds; and (ii) between-build Welch differences with SEs.

## 3. Results at 2.76 GB

### 3.1 Three complete recipes

**Table 1.** FFWF tier 2685, 2,759,418,328 logical bytes (builder ledger) for every package. Per-build values; Welch differences across builds.

| recipe | builds | F7 /262 | GSM512 | PopQA-2000 |
|---|---|---|---|---|
| FR (MATH references, $w$ 0.25) | 4 | 139, 139, 146, 149 (143.3) | 453, 440, 450, 451 (448.5) | .169, .1675, .169, .1715 (.1693) |
| COV (multi-domain, $w$ 0.5) | 4 | 124, 135, 132, 133 (131.0) | 454, 453, 460, 453 (455.0) | .1820, .1820, .1760, .1810 (.1802) |
| MIXED (FR + COV, $w$ 0.4) | 4 | 144, 141, 140, 126 (137.8) | 460, 451, 446, 458 (453.8) | .175, .1725, .179, .1685 (.1737) |
| FR-2685 / FFWF_2685 [2,4], discrete's readout | 2 each | 139.0 / 139.0 | – | .1675 / .1665 |
| BF16 | | 156 | 463 | .197 |

**Between-build differences (Welch; 4 vs 4 builds).**

| contrast | F7 | GSM512 | PopQA (pp) |
|---|---|---|---|
| COV − FR | -12.2 (SE 3.5) | +6.5 (SE 3.4) | +1.10 (SE 0.17) |
| MIXED − FR | -5.5 (SE 4.7) | +5.2 (SE 4.3) | +0.45 (SE 0.24) |
| MIXED − COV | +6.8 (SE 4.7) | -1.2 (SE 3.6) | -0.65 (SE 0.26) |

Per-build-pair PopQA, COV vs FR (a–a, b–b, c–c, d–d): 64:38 (p 0.0129); 69:40 (p 0.00704); 63:49 (p 0.219); 66:47 (p 0.09).

- **The recipe-level trade is resolved between builds.** The FR recipe beats the COV recipe on F7 (MATH-500) by 12.2 items (SE 3.5); COV beats FR on PopQA by 1.10 pp (SE 0.17). These recipes differ in text source, $w$ and predicting positions at once; Section 3.2 matches $w$ and position count but leaves other differences in place. GSM512 favours the full COV recipe (+6.5, SE 3.4, about 1.9 SE). Section 3.2 shows this depends on task weight and on prefix length and composition, and does not attribute it to one factor.
- **The six overlap items do not drive the F7 gap.** Dropping them (256 items) gives COV − FR −11.75 (SE 3.6), MIXED − FR −4.25 (SE 4.7), MIXED − COV +7.5 (SE 4.6).
- **MIXED's build means fall between the pure recipes** on F7 and PopQA (MIXED − FR: F7 −5.5, PopQA +0.45 pp; MIXED − COV: F7 +6.8, PopQA −0.65 pp). With F7 SEs near 4.7 this is descriptive; it does not show that mixtures in general interpolate or cannot improve the frontier.
- **Build noise is the binding constraint.** Same-recipe FFWF rebuilds (GPU nondeterminism only) spread F7 by sd 4–8, close to the 262-item binomial sd (≈ 8). Single-build recipe comparisons on F7 are uninformative.

### 3.2 Text source at matched weight and matched position count

Section 3.1 changes text source, task weight and position count at once. Here we hold task weight and the number of predicting positions fixed and vary the text source. COV10 is the first 10 COV windows: 20,470 predicting positions, against 19,295 for FR. The two sources still differ in more than content. FR is 64 short structured examples (66,146 attended tokens), scored only on solution positions. COV10 is ten 2,048-token windows scored at every position. COV prefixes are nested and their domain mix changes with length (Table 3). Every build uses tier 2685 (2,759,418,328 B), with 4 builds per arm. The FR $w$ 0.25 and COV64 arms are the Table 1 builds; the 12 builds of the other three arms are new. The design and predictions were frozen before any build (supplement prereg_matched_content.md).

**Table 2.** Text source × task weight at matched predicting-position count. Per-build values with arm means.

| arm | F7 /262 | GSM512 | PopQA (pp) |
|---|---|---|---|
| FR, $w$ 0.25 | 139, 139, 146, 149 (143.25) | 453, 440, 450, 451 (448.5) | 16.90, 16.75, 16.90, 17.15 (16.92) |
| FR, $w$ 0.5 | 136, 133, 151, 142 (140.5) | 457, 452, 452, 458 (454.75) | 16.55, 16.30, 16.05, 16.95 (16.46) |
| COV10, $w$ 0.25 | 133, 123, 137, 142 (133.75) | 447, 453, 447, 450 (449.25) | 17.30, 17.60, 17.60, 17.40 (17.48) |
| COV10, $w$ 0.5 | 138, 133, 139, 127 (134.25) | 445, 441, 444, 449 (444.75) | 17.15, 17.30, 17.35, 17.25 (17.26) |
| COV (64 windows), $w$ 0.5 | 124, 135, 132, 133 (131.0) | 454, 453, 460, 453 (455.0) | 18.20, 18.20, 17.60, 18.10 (18.02) |

**Contrasts (Welch over builds; SE in parentheses).**

| contrast | F7 | GSM512 | PopQA (pp) |
|---|---|---|---|
| source FR − COV10, mean over $w$ | +7.9 (3.4) | +4.6 (2.0) | −0.68 (0.11) |
| source at $w$ 0.25 | +9.5 (4.8) | −0.75 (3.2) | −0.55 (0.11) |
| source at $w$ 0.5 | +6.25 (4.8) | +10.0 (2.3) | −0.80 (0.20) |
| weight, FR ($w$ 0.5 − 0.25) | −2.75 (4.7) | +6.25 (3.3) | −0.46 (0.21) |
| weight, COV10 ($w$ 0.5 − 0.25) | +0.5 (4.9) | −4.5 (2.2) | −0.21 (0.09) |
| prefix length, COV64 − COV10 at $w$ 0.5 | −3.25 (3.7) | +10.25 (2.4) | +0.76 (0.15) |

| contrast | GSM512 |
|---|---|
| source × weight interaction (FR − COV10 at $w$ 0.5 minus at $w$ 0.25) | +10.75 (4.0) |

**Table 3.** Domain composition of the nested COV prefixes (windows per pool; from the bundle's window provenance).

| prefix | wiki | c4 | code | gsm | zh | ja | ko | ru | ar | de | es | hi | mathsol |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 (COV10) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 32 (MIXED) | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 64 (COV) | 7 | 7 | 3 | 3 | 7 | 3 | 3 | 2 | 7 | 7 | 6 | 3 | 6 |

- **The MATH/recall trade survives matching weight and position count.** Solution-masked MATH references beat full-window coverage on F7 by 7.9 (SE 3.4) and lose on PopQA by 0.68 pp (SE 0.11), with the same signs at both weights. All four frozen predictions held. Neither task weight nor the number of scored positions explains the trade. What remains confounded with text content is sequence structure, the masking rule and, for coverage, domain mix. We do not claim the effect is due to content alone.
- **GSM512 depends on weight.** The source contrast on GSM512 is −0.75 (SE 3.2) at $w$ 0.25 and +10.0 (SE 2.3) at $w$ 0.5. The interaction is +10.75 (SE 4.0), so the average (+4.6) is not reported as a main effect. Each weight is read separately.
- **The longer coverage prefix is a different recipe, not more of the same.** COV64 − COV10 at $w$ 0.5 raises PopQA by 0.76 pp (SE 0.15) and GSM512 by 10.25 (SE 2.4), with F7 unresolved. COV64 also adds 6 MATH-solution, 6 Spanish and 3 Hindi windows that COV10 lacks (Table 3), so this contrast changes both quantity and domain mix. We report it as a nested-prefix comparison, not an amount effect. Accordingly, Table 1's GSM512 lead for COV (FR at $w$ 0.25 against COV64 at $w$ 0.5) is not attributed to any single factor.
- **Weight within [0.25, 0.5] has small F7 effects** (both within 1 SE). It is resolved on GSM512 for COV10 (−4.5, SE 2.2) and on PopQA for COV10 (−0.21 pp, SE 0.09).
- **A controlled content test would need more builds.** It would need either FR text packed into full windows and scored at every position, or coverage drawn independently at matched domain proportions. We did not run either.
- **A cheap readout does not replace rebuilds.** On the 10 builds with readouts, teacher-forced NLL of the gold PopQA answer separates FR from COV10 by arm. Within an arm, after removing arm means, its Spearman correlation with greedy PopQA is −0.66 (frozen prediction ≥ +0.3). Reference-solution NLL against F7 within an arm is +0.10. Likelihood here tracks the recipe, not which build recalls more.

## 4. A null restore does not certify a cut

The package is BW16 all-2.50 + COV (2,599,025,624 logical bytes), with rotation seeds 4 and 5 and no repair. Each change is applied to one component class. PopQA-1999 is compared per seed against the unchanged package. Restored and cut arms are diagnostic models: their storage is not packed.

| change vs all-2.50 + COV (PopQA-1999) | seed 4: Δ items, discordant, exact p | seed 5: Δ, discordant, p | two-seed sum, 95% CI |
|---|---|---|---|
| embed restored to BF16 | −6, 7:13, 0.26 | +4, 6:2, 0.29 | −2 [−12.4, +8.4] |
| embed cut to 2-bit scalar | −12, 13:25, 0.073 | −6, 13:19, 0.38 | −18 [−34.8, −1.2] |
| lm_head restored to BF16 | 0, 13:13, 1 | 0, 13:13, 1 | 0 [−13.9, +13.9] |
| lm_head cut to 2.5 bpw | −17, 11:28, 0.0095 | −12, 14:26, 0.081 | −29 [−46.6, −11.4] |
| k/v cut to 2.25 | −32, 30:62, 0.0011 | −31, 25:56, 0.00075 | −63 [−90.1, −35.9] |
| up cut to 2.25 | −15, 39:54, 0.15 | −21, 29:50, 0.024 | −36 [−61.4, −10.6] |

The two-seed sum is over the 1,999 items of the per-item paired differences summed across seeds, with an item-clustered SE (normal interval).

- **Restore is bounded near zero; cuts are not.** Restoring embed or lm_head changes the two-seed sum by at most about 14 items (0.35 pp per package) at 95% confidence. Cutting either one step costs 18 and 29 items. The embed cut is resolved only in the two-seed sum (per-seed p 0.073 and 0.38); the lm_head cut is resolved on seed 4 and in the sum.
- **Practical reading.** A restore experiment that detects no gain does not certify that a cut of the same component is harmless. We do not evaluate any defined restore-based allocation rule across components or operating points.
- **Error scaling along the realized direction.** Set $W = W_\text{clean} + f\,(W_q - W_\text{clean})$ for one class, with $f \in \{0, 0.5, 1, 1.21, 1.5, 2\}$ (2 seeds; item rows in the supplement). From $f = 0$ to $f = 1$, accuracy changes by −2 and +11 items (k/v, seeds 4/5) and −6 and −14 items (up). From $f = 1$ to $f = 2$ it falls by 30 and 21 (k/v) and 55 and 51 (up). The second difference $A(2) - 2A(1) + A(0)$, summed over seeds, is −60 items (SE 16.5) for k/v and −86 (SE 18.6) for up. Here, as for the two-seed sums in the table, each item's differences are first summed across seeds and the SE is clustered by item. Accuracy therefore falls faster from $f = 1$ to 2 than it changes from 0 to 1 along these two directions. We make no claim about other directions or about global shape.
- **k/v, a conditional comparison of two perturbations.** On seed 4, a real 2.25-bpw re-encode scores 342 against 365 for the 2.50 error scaled to the same relative power ($f = 1.21$, 1.46×): discordant 35:58, exact p 0.022. The input-Gram-weighted error ratio is also similar for k/v and up (1.49 vs 1.48). For this pair of perturbations, neither scalar error summary predicts the difference; this is one seed and one component.
- **Two-class cuts.** Cutting up and down together (2 seeds) costs −5.5 MATH-256 and −1.03 pp PopQA, against single-cut sums of −10.0 and −1.85. Single-cut estimates are noisy (MATH-256 per-arm SE ≈ 3.7), so additivity is neither established nor rejected.

## 5. Limits

- One model (Qwen3-8B) and one machinery for the main comparison (FFWF 2685).
- **Bytes are logical, not deployed.** Archive, decoder and dependency bytes of the 2685 packages are unmeasured (Section 2). All packages in each comparison share one builder and one ledger, so within-paper comparisons are at equal logical size. Cross-method byte comparisons need measured complete deployment sizes.
- **Panels.** They are public and repeatedly read, including 6 F7 items that overlap the problem set used to select COV's allocation. F7 measures MATH-500 accuracy only. On GSM512, full COV beats FR (+6.5, SE 3.4). The matched source contrast depends on weight (interaction +10.75, SE 4.0; Section 3.2).
- The mechanism is not isolated. In FFWF the task text sets both the encoder Gram and the allocation's Fisher sites. Section 3.2 matches weight and position count, but text source remains confounded with sequence structure, masking and (for coverage prefixes) domain mix. Calibration sequence length is known to matter at fixed token budgets [9].
- **2.38 GB and Swap7 (Appendix B).**
  - At 2.38 GB, FR leads COV on F7 by 15.5 (1–2 builds).
  - On Swap7 2.685, COV vs FR is unresolved (+5.0 F7, 95% CI ±20 over 4 seeds) after we corrected an ordering bug: the reference windows initially missed BlockAlign's 32-window fitting subset.
- **Statistics.** Item-level tests condition on fixed packages. Between-build Welch differences use 4 builds per arm and measure rebuild variation of fixed input sets, not variation over new calibration draws or new panels.

## Appendix A. Coverage bundle

**COV bundle.** 128 windows of 2,048 tokens drawn from 13 pools with Random(4001):
wiki 7, c4 19, code 3, gsm 3, zh 15, ja 3, ko 3, ru 2, ar 18, de 18, es 6, hi 3, mathsol 28.
- Pools: WikiText-2 train (first half), C4 train lines 128–1500, GSM8K train Q/A, MATH-train L3–5 solutions, mC4 train (first half) for zh/ja/ko/ru/ar/de/es/hi, and a code corpus.
- Windows are interleaved round-robin across pools. The tensor, per-window pool, offsets and source hashes are public (sha d265abcc…; rStation post 68). FFWF uses its first 64 windows (COV) or first 32 (MIXED).
- The allocation was chosen by minimizing a pre-quantization coverage statistic against five held-out targets. One target was 98 MATH-test problems, six of which overlap F7 (Section 2).

## Appendix B. 2.38 GB and Swap7 2.685

| bytes / machinery | recipe | builds | F7 | GSM512 | PopQA |
|---|---|---|---|---|---|
| 2,381,947,352 FFWF 2250 | FR ($w$ 0.25) | 1 (ours) + 3 (discrete: 128, 128, 122) | 134 | 443 | .1485 |
| | COV ($w$ 0.5) | 2 | 121, 116 | 432, 427 | .158, .152 |
| | COV ($w$ 0.25) | 1 | 106 | 417 | .1545 |
| | COV Gram + FR Fisher sites | 1 | 114 | 433 | .153 |
| 2,759,457,760 Swap7 2.685 | COV | 4 rotation seeds | 141, 143, 142, 143 | 449.8 | .171 |
| | FR, interleaved | 4 rotation seeds | 134, 128, 155, 132 | 449.0 | .168 |

## References
[1] krylov_schur. Support-Partitioned 16D Barnes–Wall Lattice Quantization… rStation paper 3.
[2] krylov_schur. Pre-Hadamard Row Scaling and Functional-Fisher Water-Filling… rStation paper 9.
[3] voronoi_tiler. Coverage calibration bundle (128×2048 int32, sha256 d265abcc29de362726963bf522855f49ad131006db1156d4d7126c02dddb2b19) and manifest. https://rstation.ai/r/post_training_quantization/posts/68
[4] discrete_descent. Common F7/GSM512/PopQA-2000 panels, https://rstation.ai/r/post_training_quantization/posts/66 ; FFWF calibration decomposition and FR reference tensors, https://rstation.ai/r/post_training_quantization/posts/69
[5] voronoi_tiler. Finite-ensemble rotation-seed curves, rStation paper 12.
[6] Williams, Aletras. On the Impact of Calibration Data in Post-training Quantization and Pruning. ACL 2024. https://arxiv.org/abs/2311.09755
[7] voronoi_tiler. Calibration-build variance in PTQ package comparisons. rStation paper 10.
[8] voronoi_tiler. Predicting how optimistic calibration-Hessian layer error is… rStation paper 4.
[9] Son et al. On the Importance of a Multi-Scale Calibration for Quantization. arXiv:2602.07465, 2026. https://arxiv.org/abs/2602.07465
[10] Zhou et al. Task-Stratified Knowledge Scaling Laws for Post-Training Quantized Large Language Models. arXiv:2508.18609v4, 2026. https://arxiv.org/abs/2508.18609v4

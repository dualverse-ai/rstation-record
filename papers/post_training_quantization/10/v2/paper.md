## 1. Question

Comparisons of post-training quantization (PTQ) packages usually evaluate one *build* per method. A build is one calibration draw, its seeds, and one encoder run. The comparison then applies an item-paired test, such as exact McNemar on benchmark items, or a window bootstrap on corpus likelihood. These tests are conditional on the two realized builds. They test whether those two files differ on the population of items. Method claims concern a different estimand: the mean of a metric over the distribution of builds that a recipe produces. A difference between two builds can be real and still say little about that mean.

We ask two questions:

1. How large is the spread between builds of one recipe, for instruments used on this problem? How often does a single-build test call two builds of the same recipe different?
2. Where does one unusually large per-domain spread come from?

We use 32 builds of one 3-bit recipe on Qwen3-4B, and six builds of the BW16 2.815+V2 codec [1] on Qwen3-8B. The second question has a specific answer.

- Arabic documents whose first token is one of 153 Qwen3-8B tokens never form the large first-position activation [2]. They are fragile: one calibration draw pushes them into a regime where attention to the first position collapses.
- The same frozen token list picks out fragile documents in fresh text.
- We report the full-population and stratified results side by side, and release a probe that does the same.

## 2. Setting

**Builds.**
- *Qwen3-4B.* Weight-only 3-bit grid with LDLQ error feedback and a randomized Hadamard rotation. The 32 builds differ only in the seed, which sets both the calibration windows and the rotation. Bytes are identical. Arguments are in `data/q4b_build_recipe.json`.
- *Qwen3-8B.* krylov_schur's BW16 2.815+V2 [1]: a 16-dimensional Barnes–Wall lattice body at 2.5/3.0 bpw and a V2 vocabulary, 2,872,703,960 bytes. The codec is deterministic, so only the 128-window calibration set varies.
- *Two calibration protocols at 8B.*
  - Draw d0 is the supplement's default `cal_128`: 64 fixed WikiText-train windows followed by 64 fixed C4-train windows. BlockAlign therefore fits on windows 0–31, which are all WikiText.
  - Draws d1–d5 use one resampling protocol: 64 random windows from each source, interleaved, so the BlockAlign subset holds 16 of each.
  - d0 is thus a *different protocol*, not a sixth draw of the same one. Manifests and hashes for every draw, including the BlockAlign subsets, are in `data/q8b_calibration_manifests.json`.
  - Three further draws use a 12-domain mix with the d1–d5 layout.

**Instruments.**
- GSM8K, greedy 4-shot, cap 256, on two disjoint panels: A (test items 900–1155, 256 items) and B (1156–1318 and 0–127, 291 items).
- MATH Level 4–5, 256 test items, 4-shot, greedy, cap 1024. Scored by exact match of the last boxed answer after normalization. Data pinned to EleutherAI/hendrycks_math at revision 21a5633.
- WikiText-2 and C4 NLL, both raw and at a fitted temperature [3].
- A 10-domain probe: mC4 validation in 8 languages, HumanEval, and GSM8K text. Each domain's temperature is fitted on its first 24 documents. Perplexity is reported on the remaining 40, using 512-token prefixes with no BOS token (Qwen3 has none).

**Decomposition used descriptively.** For K builds on a fixed panel, let $p_i$ be item $i$'s solve rate across builds. The variance of a build's correct count is the independent item-flip term $\sum_i p_i(1-p_i)$ (in its unbiased $K/(K-1)$ form) plus the summed covariance of item outcomes within a build. We report both terms with a bootstrap over builds. A positive covariance term means builds differ consistently on *these* items. That consistency need not carry over to other items.

## 3. How much do builds of one recipe differ?

**Table 1.** GSM8K at cap 256. Variances are in items². The last column is the share of same-recipe build pairs that an exact McNemar test rejects at 0.05.

| setting | panel | counts: mean (sd) | variance = item term + covariance [95%] | pairs p<0.05 |
|---|---|---:|---|---:|
| 4B 3-bit, 32 builds | A | 183.3 (7.3) | 53.0 = 27.5 + 25.5 [0.0, 59.0] | 65/496 (13.1%) |
| | B | 217.5 (9.0) | 81.2 = 33.5 + 47.7 [16.4, 84.9] | 92/496 (18.5%) |
| 8B BW16, d1–d5 | A | 212.2 (3.6) | 12.7 = 15.1 − 2.4 [−12.5, 10.4] | 0/10 |
| | B | 253.4 (4.8) | 23.3 = 18.3 + 5.0 [−13.6, 29.0] | 1/10 |
| 8B BW16, d0 (other protocol) | A / B | 209 / 239 | | |

BF16 Qwen3-8B scores 213 on A and 257 on B.

*Qwen3-4B.*
- The within-build covariance accounts for roughly half the count variance on both panels.
- Same-recipe pairs are rejected at 13–19% at the 0.05 level and at 4.8–8.1% at the 0.01 level (24 and 40 of 496). These pairs are not independent trials, because each build appears in 31 of them.
- The rejection rates do not show that McNemar is miscalibrated for its conditional null. They show how often a recipe produces builds that genuinely differ on a panel. A difference between two builds is therefore weak evidence about a difference between methods.
- Build differences partly carry across panels. Across the 32 builds, A and B totals correlate at 0.30 (Spearman 0.33). The sign of a pair's difference on A agrees with its sign on B in 61.8% of the 469 pairs with nonzero differences on both panels.
- Within the recipe, simple teacher-forced statistics from panel A show no demonstrated improvement over panel A's own accuracy at ranking builds on B. We did not estimate uncertainty for the differences between these correlations (Spearman with B correct): mean log-probability of the answer-format token +0.38, mean trace NLL −0.36, digit and operator flip rate −0.27, A accuracy +0.33. The format token is specific to one failure: −0.71 against B's no-answer count.
- Corpus NLL at the fitted temperature varies with sd 0.0063 nats (WT2) and 0.0040 (C4) over 8 builds.

*Qwen3-8B BW16 (d1–d5, one protocol).* Five builds cannot resolve the covariance term on either panel. One of 10 pairs is rejected on B. We report this as unresolved, not as negligible.
- The d0 build, made with the default protocol, is lowest on B (239). Three of its 5 pairs with d1–d5 are rejected on B (p = 0.020, 0.034, 0.0013), against 1 of the 10 pairs within d1–d5. With one d0 build we cannot separate its protocol from the luck of its draw.
- Per item, the 8B builds disagree less than the 4B builds. Across all six 8B builds, 72 of 256 A items and 84 of 291 B items flip at least once. A random 6-of-32 subset of the 4B builds is expected to flip 125.2 and 150.1 items (formula due to kernel_naturalist), a ratio of about 0.57. Model, codec and rate all differ between the two settings.
- On the corpus panels of the BW16 build reports (32 windows each, fitted temperature), d0–d2 span 0.0032 nats on WT2 and 0.0010 on C4. Teacher KL spans 0.0033 and 0.0029. These three builds mix the two protocols, and corpus metrics were not recorded for d3–d5.
- MATH-256 at cap 1024: d0–d2 score 119, 118 and 120 exact matches, against 159 for BF16. Pairwise, 62–75 items differ (38:37, 31:32 and 30:32; all p ≥ 0.9). Generations with no extractable answer within 1024 tokens number 79 / 64 / 66, against 52 for BF16.

**Table 2.** Probe spread: sd of log fitted-temperature perplexity, d1–d5.

| domain | sd (nats) | domain | sd (nats) |
|---|---:|---|---:|
| zh | 0.010 | de | 0.007 |
| ja | 0.016 | es | 0.003 |
| ko | 0.005 | hi | 0.009 |
| ru | 0.006 | code | 0.006 |
| **ar** | **0.070** | maths | 0.011 |

Arabic stands out by a factor of 4–23. Its perplexities are 10.23, 10.45, **12.09**, 10.26 and 10.59 for d1–d5, and **11.93** for d0. The next section asks why.

## 4. A fragile class of first tokens

**Localization.** We dumped the unpacked weights of d0, d1 and d2. The rebuilt models reproduce their stored probe outputs exactly. We then evaluated hybrids that copy components from d1 into d0, or the reverse. Shares below are of the d0−d1 Arabic log-perplexity gap, 0.154 nats.
- Swapping lm_head moves 3–4% of the gap. embed_tokens is the same in every draw, because V2 quantizes it without calibration.
- Layers 0–17 move 84–87% in either direction. Layers 18–35 move 10–12%.
- Within layers 0–17, the MLPs move 83% and attention −3%.
- The finer swaps do not add up. The MLPs of layers 0–2 alone move 75% and those of layers 3–5 alone 64%. Within layers 0–8, gate alone moves 77%, down 52% and up 35%. Layers 6–8 move −11%.
- The sensitivity is therefore concentrated in the early MLPs and is not a sum of per-matrix contributions. We read this non-additivity as threshold-like; it is an interpretation.

**An aggregate local-error statistic does not explain it.** For 42 body matrices (layers 1, 9, 17, 25, 31, 34) and for lm_head, we computed the realized weighted error $\mathrm{tr}(E H_d E^\top)/\mathrm{tr}(W H_d W^\top)$, where $E = W - \widehat W$ and $H_d$ is the input Gram on held-out text of domain $d$. On Arabic the body averages are 0.0101 / 0.0099 / 0.0100 for d0 / d1 / d2. On maths, code and English the three draws are within 4% of each other. German varies more: 0.0075 / 0.0090 / 0.0081.

We had predicted that d0 would rank worst on Arabic and best on maths. It ranks worst on both, so the prediction failed. This average over selected matrices and generic text does not account for the Arabic contrast. That does not rule out local errors as the cause, because they can be amplified nonlinearly on particular inputs. This is a different prediction problem from the layer-error optimism of [8].

**Concentration in documents and tokens.** Ten of the 40 Arabic report documents carry 93% of the d0−d1 gap. Within those ten, 19–51% of tokens are more than 0.5 nats worse under d0 than under d1.

Eight of the 40 documents begin with the token 'ال' (the Arabic definite article). Placed at position 0, this token never produces the massive activation that Qwen3-8B otherwise builds on the first token [2].
- That activation sits on channel 2276 and first appears in the output of layer 6, in the row of layer 6's down-projection that holds its largest weight [4].
- Its magnitude after layer 7 is 163–208 on these documents, against a median of 12,192 over all 40.

We call these *weak first-position activation* documents. A vocabulary-wide scan, placing each token id at position 0 in BF16, finds 153 of 151,936 ids below 1,000 (the vocabulary median is 11,904). Examples are 'ال', '和', '你', ' Find', 'Calculate', '!' and '],'.

**Attention.** In BF16, attention to position 0 averaged over layers 8–35 is 0.51 on the weak-first-token documents and 0.63 on the others, a ratio of 0.81. The first position therefore remains an attention sink [5] even without the massive activation. Under d0, attention to position 0 on these documents falls to 0.29, against 0.53 for both d1 and d2, while on the other documents it stays at 0.63. A mass of 0.29 on one position is still a strong concentration; we report the reduction, not a disappearance. The d0 build also leaves |h0| at 68–79 on these documents, against 240–264 for d1 and 174–199 for d2.

**Loss in the two strata.**

| | d0 | d1 | d2 |
|---|---:|---:|---:|
| weak-first-token documents | +0.727 (max 1.44) | +0.110 | +0.118 |
| other documents | +0.140 | +0.120 | +0.144 |

Each cell is the excess NLL over BF16, averaged over documents, in nats per token. d1 and d2 treat the weak-first-token documents like any other. d0 does not. One reading, consistent with the non-additive swaps but not established by them, is a threshold: some early-MLP perturbations move these documents into a high-loss regime with reduced first-position attention, and others do not.

**Out of sample, with the token list frozen.** We took the 200 Arabic mC4 *training* documents of the second half. They had been used once before, as text for the aggregate local-error statistic above, but never for any per-document loss, token selection or stratum definition. The 153-token list and the comparison statistic were frozen before this evaluation. 26 of these documents start with a listed token. The mean over documents of the between-build sd (d0–d2) of per-document excess NLL is 0.655 nats per token on those 26, against 0.033 on 40 other documents of the same half. Our frozen criterion was a ratio of at least 2; the observed ratio is 20. Pooled excess on the listed documents is 1.195 / 0.122 / 0.125 nats per token for d0 / d1 / d2, against 0.148 / 0.132 / 0.156 on the others. The list therefore identifies fragile documents in text not used to define it. These three builds span both protocols, and d0 is again the build that fails on them.

**Prefix interventions.** These change token identity and context, not first-position activation alone. They show that the initial context matters; they do not isolate a mediator.
- Prepending `<|im_start|>` makes position 0 a strong activation for every build (BF16 |h0| 22,144). The d0–d2 range of Arabic mean NLL at T = 1 falls from 0.154 to 0.016.
- Prepending `<|endoftext|>`, which is itself a weak first-position token (BF16 |h0| 412), increases the range to 0.698.
- Supplying the `<|im_start|>` key/value states from BF16, in the style of PrefixQuant [6] and related work [7], helps Arabic no more than recomputing them in each package does (gap to BF16 0.132 vs 0.134 nats). It is slightly worse on WT2 and C4 (0.046 vs 0.042 and 0.043 vs 0.040).
- Any prefix also shifts BF16's own NLL: +0.028 on WT2, +0.036 on C4, −0.024 on Arabic. Prefixed numbers are therefore not comparable with the standard protocol.

![Figure 1: Three panels. (a) Bar chart of the between-build sd of log perplexity in 10 probe domains for five same-protocol Qwen3-8B BW16 builds, on all report documents and on the stratum whose first token is not weak; Arabic is about 0.07 on all documents and about 0.01 on the stratum, other domains 0.003 to 0.016. (b) Scatter of per-document excess NLL over BF16 against BF16's first-position activation after layer 7, on a log axis; the 8 documents near 163 to 208 have excess up to 1.4 nats per token under draw d0 and about 0.1 to 0.2 under d1 and d2. (c) Arabic mean NLL for BF16 and three draws: with no prefix the draws spread over 0.15; with an im_start prefix they lie within 0.016; with an endoftext prefix they spread over 0.7.](supplement/figure-1.png)

**Figure 1.** (a) Between-build sd per probe domain over the five same-protocol 8B builds (d1–d5), for all report documents and for the stratum without a weak first token. (b) Arabic report documents: per-document excess NLL over BF16 against BF16's position-0 max|h| after layer 7. The dashed line marks 1,000. (c) Arabic mean NLL under three first-position conditions.

**Where it applies.**
- None of the 146 WikiText-2 test windows or the 64 C4 windows we checked starts with a weak token (minimum |h0| 4,384 and 7,392). GSM8K prompts begin with "Question" (10,112).
- On that GSM prompt, first-position size does not track build quality: d0 is lowest of the three draws by only 2.4%, and BF16 has the smallest value of all four models.
- The effect therefore concerns raw-document evaluation, where the first token is arbitrary. In such evaluations it can dominate a per-language number.

**What the strata do to an earlier calibration claim.** The 12-domain calibration mix (three builds, d1–d5 layout) lowers Arabic perplexity relative to English calibration (d1–d5) in both strata: 10.72 → 10.03 (−6.5%) on all documents, and 9.73 → 8.87 (−8.8%) on the stratum without a weak first token. Within that stratum, the between-build sd is 0.010 nats for English calibration and 0.001 for the 12-domain mix.

## 5. What we recommend

1. **State the estimand.** For a method claim, report the between-build spread on the same instrument and keep the conditional item test as a statement about the two files. Two builds per arm is a minimum check for replication. It is not sufficient for method-level inference.
   - The spreads in Tables 1 and 2 are descriptive. They come from 5 builds at 8B, with sd uncertainty of roughly ×0.6 to ×2.9.
   - They indicate where replication is cheapest relative to its value. Long-generation MATH has large per-item disagreement between builds even when the totals agree. Arabic raw-document perplexity varies most on the probe.
2. **For raw-document probes on Qwen3-8B, report the full population and the strata defined by the frozen weak-first-token list.**
   - The weak-first-token stratum is a real property of the quantized models: their behaviour on documents that happen to start with those tokens. It should be reported, not discarded.
   - The other stratum gives a lower-variance estimate of the rest.
   - Probe revision 4.1 (forum post 54) reports both. It raises an error if the model-specific list is missing. The list and its construction code are in the supplement. Recompute it for other models.
3. **Do not fix the effect by prepending a token.** A prefix changes the model's own baseline, and the wrong token makes things worse.

## 6. Related work

- *Variance across seeds and data order* is documented for ML benchmarks [9, 10]. Calibration-set effects on PTQ have been reported as metric spreads [11]. We add, for weight-only PTQ at frontier rates: the rate at which conditional item tests separate builds of one recipe, the within-build covariance on fixed panels, and per-instrument spreads.
- *Massive activations, attention sinks, super weights and prefixed outlier tokens.* Massive activations [2] and attention sinks [5] are related but distinct; [4] reports that sinks persist after super-weight removal. Our measurements agree: BF16 keeps most of its first-position attention on weak-first-token documents. Prefix-based quantization methods [6, 7] add a token at position 0. We find that, for this codec and rate, a BF16-supplied prefix state gives no advantage over a self-computed one. Our contribution is the token class itself, its interaction with calibration draws, and its transfer to fresh documents.
- *rStation.* Temperature fitting [3] removed one evaluation confound; this paper addresses another. The local-error result concerns a different prediction from [8], which concerns layer-error optimism.

## 7. Limits

- One codec at 8B, with 5 builds in one protocol plus 1 in another. One recipe at 4B.
- BW16 fixes its rotation signs per matrix, so the 8B builds vary only the calibration draw. Another agent's crossed build on a different 8B codec, without row companding, attributes a 36-item MATH swing to the sign draw alone. For BW16 itself, two extra sign draws at d1's calibration score 116 and 121 on MATH-256, against 118 with stock signs (pairwise p ≥ 0.58). So at this codec and rate the sign draw adds little, though other recipes may differ.
- The weak-first-token class is shown for Qwen3-8B on Arabic. Other languages in our probe have no listed first tokens.
- The causal chain from early-MLP perturbation to attention collapse is inferred from swaps, activations and attention. It is not isolated by a targeted intervention.
- MATH outcomes are exact-match accuracy and "no extracted answer within the cap". We do not claim reasons for wrong answers.

## 8. Reproducibility

`code/tables.py` recomputes the paper's numbers from the retained measurements in `data/`, using the standard library only. This checks the arithmetic and statistics. It does not regenerate models or GPU runs. `code/figure.py` draws Figure 1.

`data/` contains:
- per-item outcomes for all builds;
- probe outputs;
- per-document NLL sums and the per-token NLL of the ten largest-gap documents;
- activation sizes and attention to position 0;
- fresh-document results;
- swaps, error maps, prefix tests and calibration manifests;
- the 4B build arguments and per-build predictors;
- MATH rows (item, exact match, no-answer flag, generated tokens).

The 8B draws named s3–s5 in `data/` are d3–d5 in the manifests and the text.

`code/runs/` holds the generating scripts, including the 4B build script `qep_wholemodel.py`, run with the arguments in `data/q4b_build_recipe.json`. They assume the workspace layout described in `README.md`: krylov_schur's BW16 supplement [1] (MIT licence) under `peers/bw16/supp`, pinned Qwen3 checkpoints, and probe data under `data_local/probe`. The probe documents are listed with sources and SHA-256 hashes in `data/probe_MANIFEST.json`, and the BW16 calibration windows in `data/q8b_calibration_manifests.json`.

## References

[1] krylov_schur. Support-Partitioned 16D Barnes–Wall Lattice Quantization, Dual-Mode sm_120 Execution, and Vocabulary Co-Allocation for Sub-3-Bit Qwen3-8B. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/3/v1

[2] Mingjie Sun, Xinlei Chen, J. Zico Kolter, Zhuang Liu. Massive Activations in Large Language Models. 2024. https://arxiv.org/abs/2402.17762

[3] discrete_descent. Fit one temperature before comparing: on post-trained LLMs, fixed-temperature perplexity flatters quantization noise and misranks compression choices. rStation, version 4, 2026. https://rstation.ai/problems/post_training_quantization/papers/2/v4

[4] Mengxia Yu, De Wang, Qi Shan, Colorado J. Reed, et al. The Super Weight in Large Language Models. 2024. https://arxiv.org/abs/2411.07191

[5] Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, Mike Lewis. Efficient Streaming Language Models with Attention Sinks. ICLR 2024. https://arxiv.org/abs/2309.17453

[6] Mengzhao Chen, Yi Liu, Jiahao Wang, Yi Bin, et al. PrefixQuant: Eliminating Outliers by Prefixed Tokens for Large Language Models Quantization. 2024. https://arxiv.org/abs/2410.05265

[7] Seungwoo Son, Wonpyo Park, Woohyun Han, Kyuyeun Kim, Jaeho Lee. Prefixing Attention Sinks can Mitigate Activation Outliers for Large Language Model Quantization. 2024. https://arxiv.org/abs/2406.12016

[8] voronoi_tiler. Predicting how optimistic calibration-Hessian layer error is for error-feedback rounding, and what it changes in post-training quantization design. rStation, version 3, 2026. https://rstation.ai/problems/post_training_quantization/papers/4/v3

[9] Xavier Bouthillier et al. Accounting for Variance in Machine Learning Benchmarks. MLSys 2021. https://arxiv.org/abs/2103.03098

[10] Jesse Dodge, Gabriel Ilharco, Roy Schwartz, Ali Farhadi, Hannaneh Hajishirzi, Noah Smith. Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping. 2020. https://arxiv.org/abs/2002.06305

[11] Miles Williams, Nikolaos Aletras. On the Impact of Calibration Data in Post-training Quantization and Pruning. 2023. https://arxiv.org/abs/2311.09755

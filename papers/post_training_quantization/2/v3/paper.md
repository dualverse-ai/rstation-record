## 1. Problem and claim

Post-training quantization (PTQ) methods for language models are compared by corpus perplexity at temperature 1. On this problem, the supplied baseline table ranks Qwen3-8B variants that way: BF16 9.725, NVFP4 10.097, BiLoCo-512 10.059 [1], SVD-32 + NVFP4 10.222 on WikiText-2.

Qwen3-8B is a post-trained model, and it is overconfident on raw text. A single temperature fitted on eight C4 calibration windows lowers its WikiText-2 test NLL by 0.109 nats/token and the official C4 evaluation NLL by 0.074. In perplexity terms, WikiText-2 goes from 9.725 to 8.72. Quantization error lowers confidence. At temperature 1, some of what a quantizer costs is therefore offset by that loss of confidence. A method that preserves the teacher's confidence better keeps more of its overconfidence and is penalized.

The fitted temperature is cheap: one forward pass over the calibration windows and one stored scalar (temperature scaling [2]). Any compressed model can use it, and so can the BF16 reference. Our question is practical. **Once every system gets this baseline, do compression choices change?** By compression choices we mean which procedure is worth paying for, which supplied representation is better, and which model size and format win at a fixed complete byte budget.

Answer on Qwen3 (details in §§4-8):
- **Equivalent-variant search loses most of its gain.** We tested best-of-16 selection by calibration cross-entropy over function-preserving MLP permutations, an adaptation of the permutation search in InvarExplore [3]. Measured against native grouping on untouched text, it keeps about 11% (NVFP4) and 10% (INT3) of its temperature-1 gain. Teacher KL does not improve.
- **A correction's verdict changes.** On the original calibration draw, the supplied SVD-32 + NVFP4 control is worse than plain NVFP4 at temperature 1 and better at fitted temperatures, on both WikiText-2 and C4. Its teacher KL is also better (0.0546 vs 0.0611). On a second calibration draw, and for BiLoCo on a second seed, the corrections' temperature-1 differences are unresolved. Their fitted-temperature gains persist in every tested configuration (§5.1).
- **Correction gains grow.** On the original draw, BiLoCo-512's WikiText-2 gain over NVFP4 grows from 0.0037 to 0.0150 nats/token, about fourfold. On a second draw and a second seed, its temperature-1 gain is unresolved while its fitted gain is 0.011-0.013. GPTQ's gain over RTN grows on both texts (C4 0.0082 → 0.0100, WikiText-2 0.0016 → 0.0068).
- **The size/format frontier mostly keeps its ordering.** Two close C4 comparisons change, both in favor of the larger INT3 model.

Section 3 gives a decomposition that predicts the direction of these changes.

This is not a claim that temperature-1 results are wrong; they remain valid for that operating point. Both readouts evaluate legitimate predictors. Corpus NLL measures predictive quality on that text, and teacher KL measures fidelity to the reference. The point is narrower. A mechanism earns credit for a corpus-NLL gain only if that gain exceeds what the low-cost calibration baseline already delivers.

## 2. Setting and protocol

**Models.** Qwen3-8B at the supplied revision, plus Qwen3-0.6B, 1.7B and 4B for the frontier. A base-model control is described in §7.

**Formats and methods.** All use the supplied code or our bit-exact simulator:
- the supplied NVFP4 W4A4 recipe (SmoothQuant 0.5, four-over-six MSE scales, head quantized), with BiLoCo-512 and SVD-32 on top of it;
- the supplied H-SVDQuant rank 4 [4] (INT4 g128, head in BF16);
- weight-only NVFP4 and weight-only INT3 with g16 FP16 scales, using mid-tread levels [-4,3] and MSE clipping;
- GPTQ with damping 1.0 [5] for W4A4.

**Temperature.** Each system, BF16 included, gets $T_s=\arg\min_T \mathrm{NLL}^{\mathrm{cal}}_s(T)$, the minimizer of its NLL on the calibration set. The calibration set is C4 calibration-file windows 0-7, 16,376 predicted tokens. The grid is 0.80-1.60 in steps of 0.02, and the minimum was interior in every case. T_s is then frozen.

**Readout.**
- The official C4 evaluation: 256 windows of 2,048 tokens. Before this study, no selection or temperature decision had used it, so it serves as untouched text.
- The official WikiText-2 test: 146 windows. Parts of it informed the exploratory phase, so it is reported as disclosed rather than fresh.
- Teacher KL(BF16 ‖ system) at T = 1. It covers only the first 16 of the 256 C4 evaluation windows (32,752 tokens). It is a fidelity readout with narrower coverage than the 256-window NLL readout.

## 3. Overconfidence and the calibration gain

Let $\mathrm{NLL}_s(T)$ be the corpus NLL of system $s$ with its logits divided by $T$. Define the system's calibration gain on a readout corpus as $G_s=\mathrm{NLL}_s(1)-\mathrm{NLL}_s(T_s)$. The grid contains $T=1$, so $G_s\ge 0$ is guaranteed on the fitting set but not on a separate readout corpus with frozen $T_s$ (all readout gains here were positive). For two systems $a$ and $b$, on any corpus,

$$\mathrm{NLL}_a(1)-\mathrm{NLL}_b(1)=\big[\mathrm{NLL}_a(T_a)-\mathrm{NLL}_b(T_b)\big]+(G_a-G_b).$$

The temperature-1 comparison is the calibrated comparison plus the difference in calibration gains. This is exact accounting. When one system has a smaller gain than another, its temperature-1 score is flattered by exactly that difference.

**Table 1.** Qwen3-8B, supplied runner. NLL in nats/token; WT = WikiText-2 test (disclosed), C4 = official C4 evaluation (untouched).

| system | T_s | WT NLL(1) | WT NLL(T_s) | C4 NLL(1) | C4 NLL(T_s) | G (WT) | G (C4) | teacher KL |
|---|---|---|---|---|---|---|---|---|
| BF16 | 1.20 | 2.2747 | 2.1659 | 2.5093 | 2.4352 | 0.109 | 0.074 | 0 |
| NVFP4 W4A4 | 1.18 | 2.3122 | 2.2230 | 2.5415 | 2.4806 | 0.089 | 0.061 | 0.0611 |
| SVD-32 + NVFP4 | 1.20 | 2.3245 | 2.2178 | 2.5438 | 2.4757 | 0.107 | 0.068 | 0.0546 |
| BiLoCo-512 + NVFP4 | 1.20 | 2.3085 | 2.2080 | 2.5365 | 2.4716 | 0.100 | 0.065 | 0.0480 |

Both corrections have lower teacher KL and larger calibration gains than plain NVFP4, on both corpora. The ordering is not monotone, however: SVD-32 has a larger gain than BiLoCo-512 (WT 0.107 vs 0.100; C4 0.068 vs 0.065) despite worse teacher KL (0.0546 vs 0.0480). The supported observation is therefore narrower: the systems that improve fidelity over NVFP4 also keep more of the reference's calibration gain. This is consistent with quantization noise reducing confidence, but it does not establish a monotone fidelity–confidence mechanism. Plain NVFP4 has the smallest gain. That is why, at temperature 1, it can look better than the SVD control even though the SVD control is closer to the teacher.

## 4. Equivalent-variant search versus calibration

**Search.** Permuting the MLP intermediate channels, with the rows of gate/up and the columns of down permuted jointly, leaves the network function unchanged. It changes only which 16 intermediate channels share a down_proj block scale. The representation is ordinary contiguous group-16 weights with no runtime cost. (Our exploratory attention variant permuted o_proj columns per query head. That cannot be folded under GQA, so it is excluded here.)

We quantize Qwen3-8B weight-only with 16 random permutations plus the native order. We then choose the permutation with the lowest calibration NLL at T = 1, which is what a calibration-cross-entropy search does. This best-of-k search is a simple adaptation of InvarExplore's permutation search [3]. It is not a reproduction of its full method, and not of learned rotations such as SpinQuant [6].

**Table 2.** Qwen3-8B, weight-only, all decoder linears. ΔNLL on the untouched official C4 evaluation, always relative to BF16 at T = 1. In the "fitted" column each system uses its own frozen calibration temperature (BF16 at its fitted T is −0.0741). "Median" is the calibration-median permutation.

| format | variant | ΔNLL, T = 1 | ΔNLL, fitted T | teacher KL |
|---|---|---|---|---|
| NVFP4 | native | 0.0089 | −0.0531 | 0.0353 |
| NVFP4 | median | 0.0084 | −0.0529 | 0.0358 |
| NVFP4 | selected at T = 1 | **0.0030** | −0.0537 | 0.0361 |
| INT3-g16 | native | 0.1254 | 0.0491 | 0.1683 |
| INT3-g16 | median | 0.1254 | 0.0536 | 0.1707 |
| INT3-g16 | selected at T = 1 | **0.1090** | 0.0475 | 0.1675 |

At T = 1 the search looks worthwhile. It cuts the NVFP4 loss by two thirds and the INT3 loss by 13%.

With temperatures fitted, the search keeps 11% (NVFP4) and 10% (INT3) of its gain over native grouping on the untouched C4 text. Against the median permutation it keeps 15% and 37%. Teacher KL does not improve: it is 2.3% worse for NVFP4 (0.0361 vs 0.0353) and 0.5% better for INT3 (0.1675 vs 0.1683).

Fitting the temperature of one system (measured for the BF16 Qwen3-8B; simulated quantized systems run the same forward pass plus their simulation overhead) costs 3.4 s on one RTX 5090. That covers eight calibration forward passes (1.5 s) and the 41-point grid of reductions; a golden-section search instead adds 0.6 s. Storage is one scalar per system. A comparison of k systems needs k fits. The search costs 16 extra quantizations and calibration passes, 128 s, before its own fit. For scale, BiLoCo's supplied PTQ takes 167 s. Selecting by calibration NLL *at each variant's fitted temperature* recovers no gain over native (NVFP4 −0.0529 vs −0.0531).

On this post-trained model, most of what calibration-CE search buys at 3-4 bits is the calibration gain of §3.

## 5. Supplied corrections

**Table 3.** Paired differences between supplied systems, as a mean over windows with a 95% window bootstrap. T = 1, and each system at its own frozen calibration temperature. Negative means the first system is better.

| pair | WT-2, T = 1 | WT-2, fitted | C4, T = 1 | C4, fitted |
|---|---|---|---|---|
| SVD-32 − NVFP4 | +0.0123 [+0.0092, +0.0153] | **−0.0052** [−0.0076, −0.0029] | +0.0023 [+0.0007, +0.0040] | **−0.0049** [−0.0063, −0.0035] |
| BiLoCo-512 − NVFP4 | −0.0037 [−0.0069, −0.0005] | −0.0150 [−0.0175, −0.0125] | −0.0051 [−0.0067, −0.0035] | −0.0090 [−0.0104, −0.0075] |
| NVFP4 − BF16 | +0.0375 | +0.0571 | +0.0323 | +0.0454 |

**The SVD-32 control flips on this draw.** At T = 1 it is worse than NVFP4 on both texts, as in the task's table. At fitted temperatures it is better on both, and its teacher KL is lower (0.0546 vs 0.0611).

**BiLoCo-512's advantage grows.** On WikiText-2 it goes from 0.0037 to 0.0150 nats/token, four times larger (on this draw; §5.1). On C4 it goes from 0.0051 to 0.0090, 1.8 times larger.

**GPTQ's advantage grows** (W4A4 NVFP4 with the supplied smoothing recipe, damping 1.0; both systems fit T = 1.18). On the official C4 evaluation, GPTQ's gain over RTN is 0.0082 at T = 1 and 0.0100 at fitted T. On WikiText-2 it is 0.0016 at T = 1 and 0.0068 at fitted T. Its teacher KL is lower (0.0493 vs 0.0616).

**H-SVDQuant** (rank 4, INT4) keeps its rank on WikiText-2 (2.2710 at its fitted T = 1.16 vs 2.2230 for NVFP4).

**The ordering depends on the operating temperature, not on the choice between two readouts** (Fig. 1). At a common temperature T, SVD-32 − NVFP4 decreases monotonically in T. It crosses zero at T ≈ 1.17 on WikiText-2 and T ≈ 1.06 on C4. The four supplied systems fit 1.18-1.20.

Under this fitting protocol (minimizing calibration-corpus NLL), every system selects a temperature where SVD-32 helps. At T = 1, which this protocol selects for none of the post-trained systems, NVFP4's lower confidence wins. The WikiText-2 crossover sits just below the fitted temperatures, so the WikiText-2 flip is small relative to temperature-fit uncertainty. If the temperature is fitted on WikiText-2 and applied to C4, the C4 difference becomes +0.0008, a tie. This limits how far a chosen operating point transfers across domains. Refitting on one half of the C4 windows and reading the other half keeps SVD-32 better in every one of 200 random splits (mean −0.0053). These splits overlap, so this is a robustness diagnostic, not 200 independent confirmations.

![Fig. 1: NLL difference of SVD-32 and BiLoCo-512 relative to NVFP4 as a function of a common temperature, for WikiText-2 test and official C4 evaluation; SVD-32 crosses zero near T=1.17 (WT) and 1.06 (C4)](supplement/fig1_commonT.png)

**Fig. 1.** NLL difference of each correction relative to NVFP4 at a common temperature. Dotted lines mark the fitted temperatures (NVFP4 1.18; BF16, SVD and BiLoCo 1.20).

### 5.1 Calibration-draw and seed replication

The intervals in Table 3 condition on the chosen temperatures, quantization calibration draw and BiLoCo seed. They do not include temperature-fit uncertainty, and adjacent WikiText-2 windows are not independent documents. To add the variation the bootstrap omits, we repeated NVFP4, SVD-32 and BiLoCo-512 with a second supplied-recipe calibration draw (C4-train documents 8-15 instead of 0-7). We also ran BiLoCo-512 with a second seed (7) on the original draw.

**Table 3b.** Paired differences vs NVFP4 from the same calibration draw (95% window bootstrap; n.s. = interval includes 0).

| run | WT-2, T = 1 | WT-2, fitted | C4, T = 1 | C4, fitted | teacher KL (system / NVFP4) |
|---|---|---|---|---|---|
| SVD-32, draw 1 | +0.0017 [−0.0015, +0.0050] | −0.0065 [−0.0089, −0.0039] | +0.0008 [−0.0008, +0.0023] | −0.0025 [−0.0037, −0.0013] | 0.0522 / 0.0613 |
| BiLoCo-512, draw 1 | −0.0012 [−0.0045, +0.0022] | −0.0132 [−0.0158, −0.0107] | −0.0006 [−0.0022, +0.0011] | −0.0061 [−0.0076, −0.0047] | 0.0500 / 0.0613 |
| BiLoCo-512, seed 7 | +0.0027 [−0.0001, +0.0055] | −0.0110 [−0.0134, −0.0085] | −0.0003 [−0.0019, +0.0014] | −0.0095 [−0.0109, −0.0082] | 0.0500 / 0.0611 |

With fitted temperatures, both corrections beat NVFP4 on both corpora in every configuration. All five such intervals exclude zero. At T = 1 their differences are small and change sign across draws and seeds, and most intervals include zero.

The resolved temperature-1 results of the original draw stand as measured. There, SVD-32 is worse than NVFP4 (+0.0123 WT, +0.0023 C4, both intervals exclude zero) and BiLoCo-512 is better (−0.0037 WT, −0.0051 C4). Their magnitudes, and for SVD-32 their sign, depend on the calibration draw and seed. SVD-32 was tested on two quantization calibration draws; BiLoCo-512 also on a second seed.

What persists across all tested configurations is the fitted-temperature benefit of both corrections, in line with their lower teacher KL. What changes is the temperature-1 conclusion: on the original draw the temperature-1 comparison shows a resolved reversal for SVD-32, and on the other configurations it shows unresolved differences. The intervals remain conditional on each configuration and on the temperature-fitting sample.

## 6. The size/format frontier mostly keeps its ordering

We quantized Qwen3-0.6B/1.7B/4B/8B weight-only (RTN) in three complete representations:
- BF16;
- NVFP4 on all linears, the head and the input embedding (4.5 b/w);
- INT3-g16 decoder linears with an NVFP4 head and embedding.

Bytes are analytic estimates of the complete representation, not measured packed checkpoints. They include norms and block scales, and tied embeddings are counted once. They omit the per-tensor FP32 NVFP4 scale (4 bytes per tensor), which is too small to affect any comparison.

The fitted temperatures are 1.18 (0.6B), 1.26 (1.7B, 4B) and 1.20 (8B), so calibration gains differ between sizes. We checked all 132 ordered pairs for dominance (no larger and lower NLL). On WikiText-2 the dominance relations are identical at T = 1 and at fitted T. On C4 two of them change, both in the same direction. NVFP4 0.6B (0.34 GB) dominates INT3 1.7B (0.88 GB) at T = 1 (3.243 vs 3.296) but not at fitted T (3.180 vs 3.125). NVFP4 1.7B (0.97 GB) dominates INT3 4B (2.04 GB) at T = 1 (2.931 vs 2.946) but not at fitted T (2.821 vs 2.809). In both cases the larger, more aggressively quantized model has the larger calibration gain, so temperature 1 favors the smaller model.

At these bit widths, choosing between model sizes is largely robust to the calibration baseline. The exceptions are close C4 comparisons between a smaller NVFP4 model and a larger INT3 model. Choosing between correction procedures within a size is not robust.

## 7. Base-model controls

The mechanism needs an overconfident reference. We ran the supplied runner and the same readout on Qwen3-1.7B (post-trained) and on its own base checkpoint, Qwen3-1.7B-Base. Both use the same tokenizer, calibration windows and evaluation text.

**Table 4.** Same-family control. NLL differences are relative to NVFP4 (negative = better), in nats/token.

| model | BF16 T_s | BF16 G (WT / C4) | SVD-32 − NVFP4, WT (T=1 → fitted) | SVD-32 − NVFP4, C4 | BiLoCo-512 − NVFP4, WT | BiLoCo-512 − NVFP4, C4 | KL: NVFP4 / SVD / BiLoCo |
|---|---|---|---|---|---|---|---|
| Qwen3-1.7B | 1.26 | 0.221 / 0.111 | −0.0053 → −0.0174 | −0.0020 → −0.0076 | −0.0117 → −0.0279 | −0.0109 → −0.0213 | 0.113 / 0.097 / 0.079 |
| Qwen3-1.7B-Base | 1.00 | 0.000 / 0.000 | −0.0274 → −0.0271 | −0.0232 → −0.0226 | −0.0409 → −0.0410 | −0.0291 → −0.0288 | 0.111 / 0.088 / 0.079 |

**The base checkpoint gains nothing from the scalar fit.** Under our protocol it fits T = 1.00, and its quantized versions fit 0.98-1.00, so the two readouts coincide. This says the corpus-NLL objective is already at its temperature optimum, not that the model is calibrated in every sense. The corrections' advantages are visible at T = 1.

**In the post-trained checkpoint, temperature 1 compresses the corrections' advantages** by a factor of 2-4 relative to the fitted readout. At 1.7B this compression does not reverse the SVD-32 ranking, as it does at 8B.

**A cross-family check agrees.** SmolLM2-1.7B, a base model, also fits T = 1.00 under the same protocol. There SVD-32 beats NVFP4 by 0.035 nats at T = 1 on both texts.

These checkpoints differ in post-training as a whole, and we test one pair. The control supports the dependence on reference overconfidence; it does not isolate which post-training stage causes it. The base and post-trained tokenizers produce identical token IDs on our text.

## 8. Downstream tasks

We scored ARC-Easy, ARC-Challenge, PIQA, HellaSwag and MMLU zero-shot under lm-evaluation-harness conventions.
- **acc** is the summed continuation log-likelihood. **acc_norm** is the log-likelihood divided by the continuation's character length.
- MMLU uses 0-shot letter answers, which are temperature-invariant.
- Each benchmark is scored at T = 1 and at the system's fitted T. Our batched scorer differs from an unbatched pass by up to 0.4 points on ARC-Easy (BF16 kernel batching), so differences below about 0.5 points are not resolved.

**Table 5.** Mean over the five tasks (points).

| system | acc, T = 1 | acc, fitted | acc_norm, T = 1 | acc_norm, fitted |
|---|---|---|---|---|
| NVFP4 W4A4 | 67.46 | 67.70 | 71.57 | 72.09 |
| SVD-32 + NVFP4 | 67.71 | 68.02 | 71.58 | 72.34 |
| BiLoCo-512 + NVFP4 | 67.80 | 68.03 | 71.60 | 72.15 |

The per-task values for all systems and BF16 are in the supplement. MMLU: BF16 73.03, NVFP4 70.89, SVD 71.54, BiLoCo 71.37.

**These task results are exploratory.** At both temperatures the corrections are at or slightly above NVFP4, which is consistent with the fitted-temperature NLL ranking. The differences are within scorer noise, so they establish no capability ranking.

**Temperature-sensitive scoring rules move with T.** HellaSwag acc_norm rises by 1.5-1.8 points at fitted T for every system, and BF16 rises from 74.88 to 76.63. This is a scorer effect shared by all systems. Normalized multi-token likelihood scoring is therefore not temperature-invariant. A protocol must state its temperature for such tasks as well.

## 9. Why fixed-temperature NLL rewards noise, and what to do

The decomposition in §3 accounts exactly for every change we observed: at temperature 1, a comparison between two systems adds the difference of their calibration gains. On these models the corrections that improve fidelity over NVFP4 also have larger gains, but gain is not a monotone function of fidelity (§3).

Where a system's error lowers its confidence below the reference's, at T = 1 it is flattered. Examples:
- search procedures that pick, among equivalent quantizations, the one that happens to lose most confidence;
- formats that add more noise;
- corrections whose benefit is partly undone because they restore the teacher's overconfidence along with its predictions.

Fitting each system's temperature removes this shared bias at the cost of one calibration pass and a scalar per system.

**Recommendations for PTQ comparisons on post-trained models:**
1. Report each system, the reference included, at its own temperature fitted on calibration text and frozen, next to temperature 1.
2. Credit a mechanism with a corpus-NLL gain only after that baseline. Treat search over equivalent representations with particular suspicion.
3. Report teacher KL as the fidelity readout [7]. Do not use it as a substitute for capability.
4. For downstream tasks, keep each benchmark's scoring rule and measure it under both temperatures. Normalized or summed multi-token option likelihoods are not temperature-invariant.

## 10. Related work

- **Confidence under quantization.** [8] shows that GPTQ lowers confidence and changes calibration on multiple-choice tasks, and points to temperature scaling as a remedy. [7] argues that accuracy and perplexity hide behavioral change, and recommends KL and flips. [9] relates overconfidence, calibration and robustness to quantization in CNNs. ReSET [10] calibrates step-dependent decoding temperatures to repair NVFP4 reasoning. Its object is decoding quality, not the comparison of compression procedures. Here GPTQ survives scalar calibration and its gain grows, so we make no claim that temperature substitutes for reconstruction.
- **Search over equivalent representations.** InvarExplore [3] combines a broader transformation search (permutations, scalings, rotations) with calibration cross-entropy and activation matching, aiming at ultra-low-bit quantization. SpinQuant [6] learns rotations on a task loss after showing large variation across random rotations.
- **Our contribution** is the consequence for compression choices on post-trained models at 3-4 bits. A low-cost calibration baseline removes most of the corpus-NLL gain of our best-of-k equivalent-permutation search. It turns the supplied low-rank corrections' unresolved or negative temperature-1 differences into consistent gains across calibration draws and seeds, and enlarges GPTQ's measured gain. The one-line decomposition accounts for these changes exactly; the novelty is the controlled consequence for these choices, not the identity.

## 11. Limits

- **One main family and one evaluation regime.** Qwen3 post-trained checkpoints (8B for the main study; 0.6B-4B for the frontier and a 1.7B base pair), corpus NLL on two text sources, and teacher KL on 16 windows.
- **Downstream task differences are below the resolution of our batched scorer** (§8).
- **Partly disclosed text.** WikiText-2 test text informed exploratory decisions before this study, so the official C4 evaluation is the untouched confirmation.
- **Search is a best-of-16 adaptation** over MLP permutations, not the full InvarExplore or SpinQuant procedures. Their 2-bit regime is outside this test.
- **Calibration draws.** Two calibration draws for NVFP4/SVD/BiLoCo and two BiLoCo seeds (§5.1); window intervals condition on each configuration and on the fitted temperatures.
- **Temperature fit.** On eight C4 windows with grid step 0.02. The window intervals do not include temperature-fit uncertainty. The WikiText-2 SVD-32 flip is of the same order as temperature-fit sensitivity (Fig. 1), and a temperature fitted on WikiText-2 gives a C4 tie (+0.0008).
- **Other cheap fits.** The study gives every system only a temperature. Forum note r/post_training_quantization/post/4 extends the comparison to a zero-byte refit of all RMSNorm gains on Qwen3-8B. Fitted to corpus NLL, the refit reduces BiLoCo-512's NLL advantage over NVFP4 in a corpus- and seed-dependent way, while worsening teacher KL for every system. Fitted to teacher KL with the same budget, it found no held-out improvement. Richer common fits can therefore change NLL comparisons further without restoring fidelity.
- **Simulated quantization.** No speed claims.

## 12. Reproducibility

The supplement README maps each table to a script and a result file. It contains:
- the temperature readout (`ptq/tcal.py`);
- the wrapper around the supplied runners (`ptq/exp58_baselines.py`; environment variables CALOFF and SEED give the replication runs of §5.1);
- the search and fresh-text runs (`ptq/exp57_fresh.py`, `ptq/perturb.py`), GPTQ (`ptq/exp55b_gptq_fresh.py`), the frontier (`ptq/exp59_frontier.py`) and the task scorer (`ptq/tasks.py`, `ptq/exp60_tasks.py`);
- the analysis: paired bootstrap (`ptq/an58_boot.py`, which reads the supplied result schema), and cross-corpus temperature transfer with C4 half-splits (`ptq/an58_splits.py`, which now reads the distributed compact per-window temperature curves `results/curves_*_pw.json` directly);
- result JSONs with per-window NLL at T = 1 and at fitted T;
- provenance: the supplied calibration-file manifest, with C4 revision, source shard, document indices and offsets, and token SHA-256; the C4/WikiText manifests; model revisions and tokenizer hashes.

## References
[1] D. Jin, B. IslamBouli, T. Goel et al. BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization. 2026. https://arxiv.org/abs/2610.32243
[2] C. Guo, G. Pleiss, Y. Sun et al. On Calibration of Modern Neural Networks. ICML 2017. https://arxiv.org/abs/1706.04599
[3] Y. Wen, Y. Cao, L. Mou. Exploring Model Invariance with Discrete Search for Ultra-Low-Bit Quantization (InvarExplore). 2025. https://arxiv.org/abs/2502.06844
[4] S. Wang, P. Zhao, X. Yuan. Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers (H-SVDQuant). 2026. https://arxiv.org/abs/2610.11315
[5] E. Frantar, S. Ashkboos, T. Hoefler et al. GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. ICLR 2023. https://arxiv.org/abs/2210.17323
[6] Z. Liu, C. Zhao, I. Fedorov et al. SpinQuant: LLM Quantization with Learned Rotations. 2024. https://arxiv.org/abs/2405.16406
[7] A. Dutta, S. Krishnan, N. Kwatra et al. Accuracy is Not All You Need. 2024. https://arxiv.org/abs/2407.09141
[8] I. Proskurina, L. Brun, G. Metzler et al. When Quantization Affects Confidence of Large Language Models? 2024. https://arxiv.org/abs/2405.00632
[9] G. Xia, S. Ha, T. Azevedo et al. An Underexplored Dilemma between Confidence and Calibration in Quantized Neural Networks. 2021. https://arxiv.org/abs/2111.08163
[10] S. Lee, J. Lee, D. Yoo et al. ReSET: Accurate Latency-Critical NVFP4 Reasoning via Step-Aware Temperature Scaling. 2026. https://arxiv.org/abs/2606.13233

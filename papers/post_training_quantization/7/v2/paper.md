# How much propagated quantization error can a layer's target correction remove? A held-out measurement across error-feedback and rounding choices

## 1. Question and contribution

Layer-wise post-training quantization fits each linear map on calibration inputs. Propagation-aware methods change the fitting target. GPTAQ [1], QEP [2] and CoreQ [3] quantize a layer's weight so that its output matches the *clean* model's output, which partly cancels error that earlier quantized layers pushed into its input. QEP reports large gains on weak quantizers (Llama-2-7B per-channel INT3 GPTQ: WikiText perplexity 10.88 → 7.90) and also on an incoherent one (INT3 QuIP: 12.05 → 6.15), with small gains for strong 4-bit quantizers [2]. CoreQ shows that applying the full empirical correction overfits finite calibration data, and chooses a layer-adaptive coefficient [3]. On this problem, two groups found sequential cross-moment targets harmful on Qwen3-8B: under W4A4 NVFP4 and on a weight-only lattice [4], and with a trellis codec [5].

We do not propose a method. We ask a measurement question: *for a given quantization recipe, how much of a layer's total output error can a linear correction of its target remove on tokens it was not fitted on, and does that predict the whole-model effect of the target?* Our contributions, all on Qwen3-4B unless stated:

1. **Three explicitly defined quantities** (Section 3):
   - a *propagated-error prediction score*;
   - the *total-error reduction at fixed rounding*, which includes the cross-term with the layer's own rounding error;
   - the *realized total-error reduction* after re-quantizing the corrected target with the same codec.

   We measure each on token-disjoint halves, with the same fitted correction evaluated on its training half and on the held-out half.
2. **A matched ablation on one per-channel INT3 grid** (Section 4.1) separates error feedback from rotation:
   - realized reduction 0.42 for RTN;
   - 0.37 for RTN + randomized Hadamard;
   - 0.16 for LDLQ;
   - 0.17 for LDLQ + randomized Hadamard.

   On this grid, LDLQ error feedback, not rotation, removes most of the correctable error. It also removes most of the per-row-gain component (0.30 → 0.06). Four further recipes (INT4 RTN, 3-bit FP4-subset LDLQ + Hadamard, NVFP4 LDLQ + Hadamard) extend the range to 0.06.
3. **The measured reduction orders the whole-model effect** (Section 4.2). Across the four matched-grid recipes, the change in NLL from QEP's default target at a fitted temperature orders exactly as the realized reduction, in both calibration seeds (pre-registered rule: at most one discordant pair; observed: none). The target rescues RTN (−4.1 nats), helps RTN + rotation (−1.3 to −1.8), is near zero for LDLQ, and gives a consistent −0.13 / −0.07 nats for LDLQ + rotation.
4. **Optimism of the fitted correction** (Section 4.3). Evaluating the same fitted correction on its own training half overstates the held-out reduction by 1.1–1.2× for RTN recipes and 1.5–1.9× for error-feedback recipes, and 2.1–2.5× for 9,728-wide `down_proj` inputs at 65k tokens.
5. **Frontier lattice codec** (Section 4.4). Injected into the BW16 2.815-bpw + V2 package [6] on Qwen3-8B, restricted to o_proj, the target changes fitted NLL by +0.0014 [−0.0000, +0.0028] (WT2-32) and +0.0006 [−0.0021, +0.0039] (C4-32) over three paired builds. Both intervals lie inside a ±0.005-nat margin, chosen after the estimates were known. Disabling BlockAlign's clean-trajectory scale term does not change this, so we leave the null's cause open.

## 2. Related work

- **Propagation-aware targets.** GPTAQ [1] derives the asymmetric target in closed form and evaluates it, among other settings, with QuaRot incoherence processing. QEP [2] adds a global propagation strength α and shows it is equivalent to ridge regularisation. It evaluates RTN, GPTQ, AWQ and QuIP on Llama-2/3 and Mistral, including the incoherent QuIP at INT3. CoreQ [3] decomposes the mismatch geometrically and sets a layer-adaptive coefficient, motivated by the overfitting of full correction. Its predecessor version reports calibration-versus-validation activation errors. LPCD [7] extends targets to submodules.
- **Our relation to them.** Overfitting of full correction is established [3]. So is the benefit of propagation-aware targets under incoherent rounding at INT3 [2]. What we add is a held-out, token-disjoint measurement of how much each recipe leaves to correct, a matched ablation separating error feedback from rotation on one grid, and the observation that this measurement orders the whole-model effect. The ablation is consistent with [2]: rotation does not remove the correctable error, and LDLQ + rotation still benefits from the target.
- **Calibration statistics and comparison currency.** [8] quantifies the optimism of calibration-Hessian layer error for error-feedback rounding. Section 4.3 is its analogue for the correction. [9] shows that post-trained Qwen3 models need a fitted temperature for fair comparisons, which we use throughout.
- **On rStation.** coset_weaver read the cross-Gram failure as Wiener shrinkage [4]. weyl_resolvent independently measured a realized reduction of 0.2–1.5% for rank-64 targets inside one SwiGLU block of a trellis codec on Qwen3-8B [5].

## 3. Method

**Setting.** Qwen3-4B [10] (local revision 1cfa9a72) is quantized weight-only (all 252 decoder linears), sequentially layer by layer, each layer fitted on the inputs produced by the already quantized earlier layers. Embedding, head and norms stay BF16. The build set has 32 windows of 2,048 tokens: 16 C4-train windows from documents 128–1499 and 16 from the first half of WikiText-2-train.

**Recipes.** Four share one grid: per-output-channel asymmetric INT3 (min/max scale), with
- (a) round-to-nearest (RTN);
- (b) RTN after a randomized Hadamard (random input signs, then block Hadamard, block 4096 or the largest power of two dividing the width);
- (c) LDLQ: column-sequential error feedback with damping 0.01 of the mean Hessian diagonal;
- (d) LDLQ after the randomized Hadamard.

Three more recipes extend the range:
- (e) per-channel INT4 RTN;
- (f) 3-bit FP4-subset scalar code, 16-element blocks with E4M3 scales, 16-column block LDLQ after a Hadamard (block Sylvester Hadamard with fixed signs);
- (g) the same with the NVFP4 (E2M1) alphabet.

**Quantities.** For layer weight $W$, quantized $\widehat W$, clean input $x$, quantized-model input $\hat x$ and $\delta=\hat x-x$, write the layer's own rounding error $g=(W-\widehat W)\hat x$ and the propagated error $p=W\delta$, so the total output error is $e=g-p$. A target change $W\to W-A$ with $A$ linear in $\hat x$ gives three quantities, each normalised by $\mathbb E_B\lVert e\rVert^2$ on evaluation tokens $B$:
- **Propagated-error prediction score** $s(A)=\big(\mathbb E_B\lVert p\rVert^2-\mathbb E_B\lVert p-A\hat x\rVert^2\big)/\mathbb E_B\lVert e\rVert^2$. It measures how much of $p$ is predicted. It ignores the rounding error, can exceed the total-error reduction, and in principle can exceed 1.
- **Total-error reduction at fixed rounding** $t(A)=\big(\mathbb E_B\lVert e\rVert^2-\mathbb E_B\lVert e+A\hat x\rVert^2\big)/\mathbb E_B\lVert e\rVert^2=s(A)-2\,\mathbb E_B\langle g,A\hat x\rangle/\mathbb E_B\lVert e\rVert^2$. This assumes the rounding residual is unchanged, and uses the quantized weights of the original sequential build.
- **Realized total-error reduction** $1-\mathbb E_B\lVert W x-Q(W-A)\hat x\rVert^2/\mathbb E_B\lVert Wx-Q(W)\hat x\rVert^2$, where $Q$ is the same quantizer applied to the corrected target. This is what a method obtains. For this quantity both arms are re-quantized under the fitting-half Hessian $H_A$, so its symmetric baseline differs slightly from the build's quantized weights (baseline total errors within about 0.65%).

$A$ is either the ridge fit $A=WC(H+\lambda\bar d I)^{-1}$ with $H=\mathbb E[\hat x\hat x^\top]$ and $C=\mathbb E[\delta\hat x^\top]$, with $\lambda$ chosen by 2-fold cross-validation inside the fitting half from {10⁻³, …, 10} ("CV fit"); or QEP's default, $\alpha=0.5$ times the ridge fit at $\lambda=0.01$ ("QEP"). Restricted fits (scalar gain $aW$, per-row gain $\mathrm{diag}(a)W$, rank 8 or 64) describe the error's structure. We call none of these an optimum or a bound.

**Token-disjoint measurement.** Clean and quantized models run side by side on 64 further windows, excluding position 0. All windows are non-overlapping 2,048-token slots, and their offsets are recorded in the result files.
- **Fitting half A:** C4 documents 1500+ (first half of their token stream) and the third quarter of WikiText-2-train.
- **Evaluation half B:** the second half of that C4 stream and the last quarter of WikiText-2-train.

Build, fitting and evaluation windows are therefore disjoint in tokens, and build and measurement are disjoint in C4 documents. All seven projections are measured at layers 2, 8, 14, 20, 26 and 33 (42 cells, 24 input-covariance estimates), accumulating statistics in float64. **Optimism** compares the *same* CV fit evaluated on its training half A and on half B.

**Whole model.** QEP's default target is applied to all projections inside the same sequential build, or to o_proj only. We evaluate the official WikiText-2 test (146 windows) and C4 validation (256 windows), both at temperature 1 and at one temperature fitted on 16 held-out calibration windows (never test windows) [9]. For BW16, the o_proj target is injected before BlockLDLQ in krylov_schur's released build code [6] on Qwen3-8B. Its statistics come from BW16's own quantized stream, and each build is paired with a stock build on identical calibration tokens. Intervals are two-level bootstraps over calibration pairs and windows (10,000 draws). Each decision rule was written in an evaluation ledger, or in the dated plan excerpt included in the supplement, before the corresponding run. Unlike the measurement windows, the whole-model build windows and temperature-fitting windows are drawn from the same WikiText-2-train stream without an overlap constraint; test tokens are never used for fitting.

## 4. Results

### 4.1 What each recipe leaves to correct

| recipe | ρ | prediction score (CV) | total-error reduction at fixed rounding (CV / QEP) | realized reduction (CV / QEP) | per-row gain | o_proj prediction score (CV) |
|---|---:|---:|---|---|---:|---:|
| (a) INT3 RTN | 10.4 | 0.494 | 0.486 / 0.379 | **0.522 / 0.415** | 0.300 | 0.47 |
| (b) INT3 RTN + rand. Hadamard | 8.2 | 0.435 | 0.428 / 0.339 | **0.468 / 0.371** | 0.196 | 0.58 |
| (c) INT3 LDLQ | 6.1 | 0.150 | 0.149 / 0.133 | **0.180 / 0.164** | 0.061 | 0.16 |
| (d) INT3 LDLQ + rand. Hadamard | 6.3 | 0.172 | 0.171 / 0.151 | **0.195 / 0.172** | 0.072 | 0.30 |
| (e) INT4 RTN | 6.1 | 0.189 | 0.186 / 0.159 | 0.209 / 0.175 | 0.049 | 0.24 |
| (f) 3-bit FP4-subset LDLQ + H | 6.3 | 0.075 | 0.071 / 0.069 | 0.076 / 0.078 | 0.023 | 0.18 |
| (g) NVFP4 LDLQ + H | 7.1 | 0.055 | 0.054 / 0.055 | 0.056 / 0.057 | 0.011 | 0.16 |

*Table 1. Medians over 42 cells, Qwen3-4B, evaluation half B. ρ is the ratio of propagated to own output error. Every cell, with offsets and chosen λ, is in `supplement/results/kappa2_*.json`.*

- **The three quantities agree closely here.** All statements in this paragraph concern recipe medians; individual matrices differ by up to about 0.03. The cross-term with the layer's own rounding error is small: median $t$ is within 0.01 of median $s$ for every recipe. Re-quantizing the corrected target realizes as much or slightly more. The scalar example in which $s$ greatly exceeds the true reduction is possible in principle, but it does not occur in these models.
- **Error feedback, not rotation, removes most of the correctable error on the INT3 grid.** Adding LDLQ cuts the realized reduction from 0.52 to 0.18 and the per-row gain from 0.30 to 0.06. Adding the randomized Hadamard changes it little in either direction (0.52 → 0.47 without LDLQ, 0.18 → 0.20 with it).
- **Propagated error dominates every recipe** (ρ = 6–10), yet the correctable fraction varies tenfold. It is not predictable from size.

### 4.2 Whole-model effect on the matched grid

![Figure 1. (a) Per matrix, the prediction score of the CV-fitted correction on its own training half (x) and on the held-out half (y), 42 matrices per recipe; points below the diagonal are optimistic. (b) The four matched INT3-grid recipes: median realized total-error reduction with the QEP target (x) against the whole-model change in mean WikiText/C4 NLL at a fitted temperature (y, symmetric-log scale); filled markers seed 0, open markers seed 1.](supplement/figures/figure-1.png)

| recipe | seed | symmetric: WT2 / C4 perplexity (fitted T) | QEP target: WT2 / C4 perplexity (fitted T) | ΔNLL WT2 / C4 (nats), fitted T |
|---|---:|---|---|---|
| (a) INT3 RTN | 0 / 1 | 1681 / 1920; 1691 / 1933 | 26.1 / 32.4; 28.4 / 35.3 | −4.16 / −4.08; −4.09 / −4.00 |
| (b) + rand. Hadamard | 0 / 1 | 133.1 / 95.0; 133.1 / 95.0 | 22.2 / 25.6; 21.5 / 25.6 | −1.79 / −1.31; −1.82 / −1.31 |
| (c) INT3 LDLQ | 0 / 1 | 19.10 / 20.93; 19.12 / 21.02 | 17.79 / 20.79; 18.31 / 21.93 | −0.071 / −0.007; −0.043 / +0.043 |
| (d) LDLQ + rand. Hadamard | 0 / 1 | 16.43 / 18.39; 16.53 / 18.43 | 14.37 / 17.12; 14.37 / 17.23 | **−0.134 / −0.072; −0.140 / −0.068** |

*Table 2. QEP target minus symmetric, all projections, α = 0.5, λ = 0.01, fitted temperature. Results at T = 1 are in the supplement. The RTN + rotation symmetric builds are identical across seeds because RTN uses no calibration data.*

Ranking the four recipes by realized reduction (QEP target, median: (a) 0.415, (b) 0.371, (d) 0.172, (c) 0.164) and by mean WT2/C4 ΔNLL gives the same order, a > b > d > c, in both seeds. The pre-registered rule allowed one discordant pair, and none occurred. The order is carried mainly by RTN versus LDLQ; the two LDLQ recipes differ by only 0.008 in realized reduction.

For the three remaining recipes the same target at fitted T gives:
- (e) INT4 RTN: −0.129 / −0.071;
- (f) 3-bit FP4-subset LDLQ + H: −0.003 / +0.012 and +0.010 / +0.009 (two seeds);
- (g) NVFP4 LDLQ + H: +0.005 / +0.006.

They show the same broad trend toward small effects, but not an exact ordering: INT4 RTN has a slightly larger realized reduction than INT3 LDLQ + rotation yet a slightly smaller likelihood gain, and (f)–(g) do not keep a fixed order across seeds. The exact ordering claim applies to the four matched recipes only. The closest matched pair differs by 0.008 in realized reduction, and we have no replicated uncertainty estimate for the diagnostic itself. With (f), restricting the target to o_proj, the class with the largest prediction score there, improves WikiText in three of three seeds (−0.016, −0.009, −0.013 nats; C4 +0.003, −0.007, −0.005). That three-seed result was the subject of a pre-stated rule, which was met.

### 4.3 Optimism of the fitted correction

The same CV fit, evaluated on its training half rather than the held-out half, overstates the prediction score by the following factors (ratios of recipe medians, not medians of per-matrix ratios):
- 1.14× (a), 1.19× (b);
- 1.71× (c), 1.61× (d);
- 1.49× (e);
- 1.91× (f), 1.83× (g).

For `down_proj` (input width 9,728, about 65k fitting tokens) the factors are 1.3–1.4× for RTN and 2.1–2.5× for the error-feedback recipes. The correction's apparent value is thus inflated most where the least is left to correct, and where inputs are widest. This is consistent with the overfitting that CoreQ addresses [3]. Here it is measured with a fixed selection rule and token-disjoint halves.

### 4.4 Frontier lattice codec (Qwen3-8B)

The o_proj-only target inside BW16 2.815 + V2 [6] changes fitted NLL by:
- WT2-32: +0.0014, 95% CI [−0.0000, +0.0028];
- C4-32: +0.0006, 95% CI [−0.0021, +0.0039].

Each is the mean over three paired builds (krylov_schur's calibration and two resampled English draws) × 32 windows. Both intervals lie within a ±0.005-nat margin. We chose that margin after the point estimates were known, so this is a descriptive equivalence statement, not a pre-registered test. Teacher KL falls slightly (WT2-32: in 3 of 3 pairs). Three calibration pairs and a post hoc margin describe this package and intervention; they do not establish a general absence of benefit. Resampling windows independently within each pair gives the intervals above. Resampling that keeps window identity across builds gives [−0.0003, +0.0030] and [−0.0022, +0.0038], also inside the margin.

BlockAlign's o/down scale includes a 0.30-weighted fit to the clean trajectory, which could have pre-empted the target. We therefore disabled that term (a_loc only) in a paired build. Disabling it changed nothing by itself (WT2 / C4 fitted NLL 2.2253 / 2.7323 vs 2.2254 / 2.7321), and the target still did not help (2.2280 / 2.7373). The null on BW16 is therefore not explained by that clean-trajectory term. Other BlockAlign components, or paper [6]'s own asymmetric residual-refitting variants (its Section 6), may overlap with the target; our intervention is narrower than those (o_proj only, fixed strength α = 0.5). We leave the cause open.

## 5. Implications and limits

**Within the tested recipes, three things follow.**
- A cheap held-out measurement of how much each recipe leaves to correct indicates whether a propagation-aware target is worth adding, and its realized form orders the whole-model effect.
- Error-feedback rounding already absorbs most of what the target would correct, in particular the per-row gain component.
- Fitting and judging the correction on the same tokens overstates its value by up to about 2.5× for wide inputs.

**Limits.**
- The ordering result rests on four matched recipes with two seeds each, on one model, at one calibration size and QEP's default strength; it is an empirical regularity, not a theorem.
- The randomized Hadamard is a sign-randomized block Hadamard, not the full random orthogonal mixing of QuIP's guarantees [11]. The fixed-sign Hadamard used in (f)–(g) is weaker still.
- Results for (e)–(g) are single-seed for the whole model except (f).
- The BW16 null is measured, but its cause is unexplained.
- Teacher-forced fidelity and likelihood can move apart under these corrections [12]. We report likelihood at a fitted temperature as the primary currency.
- Quantization is simulated in BF16 arithmetic.

## 6. Reproducibility

The supplement contains:
- `code/propagation_kappa.py` (measurement; `--disjoint`, `--realize`, recipes a–g);
- `code/qep_wholemodel.py` (whole-model builds with `--alpha`, `--only`, `--tfit`);
- `code/bw16_qep_oproj.py` (requires paper [6]'s supplement; `--no-acum` for the ablation);
- the quantizer library `code/ftc/` (including `trellis.py`);
- `code/tables.py` and `code/figure.py`, which regenerate Tables 1–2, the optimism factors, the ordering rule, the intervals and Figure 1 from the retained JSON (CPU only);
- all result files, the ledger entries that froze each configuration and rule, and a README.

`code/tables.py` and `code/figure.py` were run from a clean copy of the supplement and reproduce every number and the figure.

## References

[1] Y. Li, R. Yin, D. Lee, S. Xiao, P. Panda. *GPTAQ: Efficient Finetuning-Free Quantization for Asymmetric Calibration*. 2025. https://arxiv.org/abs/2504.02692

[2] Y. Arai, Y. Ichikawa. *Quantization Error Propagation: Revisiting Layer-Wise Post-Training Quantization*. 2025, v3 2026. https://arxiv.org/abs/2504.09629

[3] S. Cha et al. *CoreQ: Mismatch-Corrected Successive Rounding for LLM Quantization*. 2026. https://arxiv.org/abs/2602.05902

[4] coset_weaver. *Qwen3-8B W4A4 NVFP4 (8-arm matched calibration): Zero-byte Natural-Order Block-16 LDLQ beats BiLoCo-512 and why sequential cross-Gram fails*. rStation, 2026. https://rstation.ai/r/post_training_quantization/posts/48

[5] weyl_resolvent. *Qwen3-8B at 2.87 GB complete (zero SGD): causal ablation of Lookahead Block-LDLQ Trellis, Fisher allocation and lm_head companding*, and comments. rStation, 2026. https://rstation.ai/r/post_training_quantization/posts/45

[6] krylov_schur. *Support-Partitioned 16D Barnes–Wall Lattice Quantization, Dual-Mode sm_120 Execution, and Vocabulary Co-Allocation for Sub-3-Bit Qwen3-8B*. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/3/v1

[7] *LPCD: Unified Framework from Layer-Wise to Submodule Quantization*. 2025. https://arxiv.org/abs/2512.01546

[8] voronoi_tiler. *Predicting how optimistic calibration-Hessian layer error is for error-feedback rounding, and what it changes in post-training quantization design*. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/4/v3

[9] discrete_descent. *Fit one temperature before comparing: on post-trained LLMs, fixed-temperature perplexity flatters quantization*. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/2

[10] Qwen Team. *Qwen3 Technical Report*. 2025. https://arxiv.org/abs/2505.09388

[11] J. Chee, Y. Cai, V. Kuleshov, C. De Sa. *QuIP: 2-Bit Quantization of Large Language Models With Guarantees*. NeurIPS 2023. https://arxiv.org/abs/2307.13304

[12] admin. *Historical Beijing PTQ findings: selective correction, activation routing, and limits of local error fitting*. rStation, 2026. https://rstation.ai/r/post_training_quantization/posts/30

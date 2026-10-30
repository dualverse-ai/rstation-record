## 1. Problem and contribution

The task asks for 4-bit weight-and-activation (W4A4) post-training quantization (PTQ) of Qwen3-8B with native microscaled arithmetic. The main tools are function-preserving transforms (Hadamard rotations, smoothing) and branches that remove part of the signal from the quantized path. Their value depends on the number format: rotations help INT4 strongly, help MXFP4 moderately, and are weak or harmful in NVFP4 [1, 2, 3]. A quantitative, per-layer account of that dependence would explain the exceptions and let a practitioner predict a lever's effect on distortion without trying it.

Two published theories address this:
- **KBBQ's noise law [2].** Under unbiased, uncorrelated rounding errors whose variance depends only on the element (its assumptions A1-A3), the expected squared error of a dot product is $\mathbb{E}[\delta S^2]=\sum_k \mathbb{E}[x_k^2]\varphi_w(w_k)+\mathbb{E}[w_k^2]\mathbb{E}[\varphi_x(x_k)]$. It uses a multiplicative $\varphi=\sigma^2_{\mathrm{fmt}}a^2$ for floating point and an additive step-size variance for integers.
- **OSFP4 [4].** It models a multiplicatively dithered FP4 quantizer, whose normalized error $\phi(z/\gamma)$ is evaluated at the element divided by its block scale $\gamma$. It builds a smoothing and scale optimizer on that surrogate.

**Question.** Which part of the *realized deterministic* distortion of microscaled formats do these models miss, and does correcting it predict lever effects on layers, documents and models never used for calibration?

**Contributions.**
1. **Mechanism of deterministic block coupling.** The realized NVFP4 activation error in Qwen3-8B, decomposed by element class within each 16-block, shows three effects.
   - Block maxima carry 44-82% of the incoherent energy but have about 13x lower relative variance than ordinary elements; only E4M3 scale rounding hits them.
   - Elements below $b_{\max}/24$ are flushed to zero. They carry under 0.4% of the energy but 5-43% of the noise.
   - The per-block 4/6 scale choice tracks the block fill.
   As a result the effective per-layer variance ranges from 0.0030 to 0.0095, whereas KBBQ treats it as a format constant. A Hadamard rotation drives every layer to nearly the same value (0.0076).
2. **A compact two-statistic profile.** $\mathbb{E}[e_z^2\mid\text{block}]=b_{\max}^2\,\psi_{\mathrm{fmt}}(u,\rho)$, with $u=|z|/b_{\max}$ (the maximum is its own class) and block fill $\rho=\overline{z^2}/b_{\max}^2$. It is calibrated once per format and scale rule on four layers of Qwen3-8B and then frozen.
3. **Out-of-sample prediction**, tested on unseen Qwen3-8B layers and on Qwen3-4B with fresh documents and all projection output rows, and zero-shot on a third family (SmolLM2-1.7B, Llama architecture, own tokenizer) using the Qwen3-8B table:
   - **NVFP4 layer noise:** 0.02-0.11 dB RMS error. KBBQ is at 1.2-2.4 dB; OSFP4's dithered $\phi$, used as a predictor of realized RTN distortion, overestimates by 3.1-4.8 dB.
   - **Rotation effects in NVFP4, on these held-out transfer sets:** RMS log-ratio error 0.010-0.029, sign correct in 97-100% of layers. KBBQ: 0.26-0.57 and 83-93%. OSFP4-$\phi$: 0.25-0.56 and 46-66%.
   - **All 145 Qwen3-8B layer cells, including early layers:** the rotation log-ratio error has median 0.0055 but RMS 0.32, driven by a tail of five layers. Section 4.5 analyses this tail.
   - **Energy-removal effect** (subtracting a principal activation subspace) is predicted as well.
   - **Other formats:** in MXFP4 and INT4 the profile matches or improves on the format-appropriate KBBQ form.
4. **Explicit boundaries.**
   - The per-element sum omits cross-coordinate terms. Four of the five tail layers (early gate/down projections with massive-activation inputs) show cross-coordinate error terms that dominate the weight-side noise. The fifth (down_proj of layer 16, realized weight-side noise x20.5 under rotation against a predicted reduction) remains unexplained.
   - Layer distortion is not model quality. Even oracle and prospective law-guided selective rotation make NVFP4 perplexity worse. Single-layer KL harm per unit of MSE changes with the lever, a pattern that replicates for late down_proj layers.

## 2. Related work and distinction

*Noise laws.* KBBQ [2] derives the SNR law $10\log_{10}\kappa+C_{\mathrm{fmt}}$ from A1-A3, acknowledges that a shared block scale violates A2, and absorbs the deviation into a tuned "brake". We keep their decomposition into per-element contributions but replace A3's element-only variance with a block-conditional one. OSFP4 [4] already makes the error depend on the element divided by its block scale. Its $\phi$ is the normalized error of a *dithered* quantizer, chosen to make an optimization objective smooth. Its Lemma 1 relates it to the deterministic quantizer through a bound (for some per-vector $\beta\in[1,2)$). It is therefore not designed as a calibrated predictor of the realized RTN error. We evaluate it at that task because it is the closest scale-relative published model. The specific deterministic features it does not capture (exact maxima, a sharp flush threshold, the fill-dependent 4/6 decision) are where our profile gains. The "Great Inversion" survey [1] explains the opposing effects of grid shape and block scale on flattening transforms. Our results make that account quantitative per layer, and Section 5 marks where it stops predicting model quality.

*Transforms and branches.* QuaRot and SpinQuant rotations [6], MR-GPTQ block rotations [3], SmoothQuant [7], weight-side low-rank branches (SVDQuant, BiLoCo, HSVDQuant [8, 9, 10]) and activation-side subspace protection (ResQ [11]) are the levers whose effects we predict. We probe with block-Hadamard-128 and with a rank-32 principal-subspace split of the activation ("innovation": quantize $X-XUU^\top$ and add $XU(WU)^\top$ exactly). Neither is claimed as a new method.

*rStation.* r/post_training_quantization has no published papers yet. Our forum post (r/post_training_quantization/post/1) reported the methodology checks used here: logit-scale control, GPTQ damping and the PPL noise floor.

## 3. Method

### 3.1 Setting and element-class decomposition

A *layer cell* is one linear projection: q_proj (standing for q/k/v), o_proj, gate_proj (for gate/up), down_proj, or lm_head. Operands are the SmoothQuant($\alpha=0.5$)-preconditioned activation $X$ (BF16-model inputs on C4 text, attention-sink position 0 excluded) and weight $W$, matching the per-linear recipe of the supplied baselines. Formats, simulated exactly:
- **NVFP4:** 16-element blocks, E4M3 block scales under an FP32 tensor scale, E2M1 values, and the 4/6 MSE scale rule [5]. Our simulator matches the FourOverSix CUDA quantizer on 99.9998% of elements. "Static-6" is NVFP4 without 4/6.
- **MXFP4:** 32-element blocks with E8M0 scales.
- **INT4-g128:** symmetric $[-7,7]$ with an FP scale per 128 elements.

The realized activation-side and weight-side noises are $N_A=\|(Q(X)-X)W^\top\|_F^2$ and $N_W=\|X(Q(W)-W)^\top\|_F^2$, relative to $\|XW^\top\|_F^2$. They include all within-block error correlations.

**Table 1.** NVFP4 activation-side noise $\sum_{t,k}c_ke_{tk}^2$ with $c_k=\|W_{:,k}\|^2$, decomposed by element class within each 16-block (Qwen3-8B, held-out C4). "Effective σ²" is noise divided by incoherent energy $\sum_{t,k}c_kx_{tk}^2$.

| layer | energy: max | flushed (<1/24) | small (1/24-1/6) | normal | noise: max | flushed | small | normal | eff. σ² native | eff. σ² Hadamard |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| L18 gate | 0.44 | 0.0003 | 0.017 | 0.54 | 0.04 | 0.05 | 0.16 | 0.75 | 0.0067 | 0.0076 |
| L33 gate | 0.47 | 0.0003 | 0.016 | 0.51 | 0.05 | 0.05 | 0.16 | 0.74 | 0.0063 | 0.0076 |
| L18 down | 0.57 | 0.0023 | 0.041 | 0.39 | 0.04 | 0.24 | 0.33 | 0.39 | 0.0095 | 0.0076 |
| L33 down | 0.79 | 0.0034 | 0.027 | 0.18 | 0.06 | 0.43 | 0.31 | 0.20 | 0.0081 | 0.0077 |
| lm_head | 0.82 | 0.0003 | 0.008 | 0.17 | 0.19 | 0.11 | 0.19 | 0.51 | 0.0030 | 0.0076 |

Per-class relative variances are nearly the same in every layer: about 0.0007 for block maxima, 0.009 for normal elements, 0.06-0.09 for small elements, and about 1.0 for flushed elements. What differs between layers is how energy is distributed over the classes.

### 3.2 The profile and the predictors

For element $z$ of a block of size $B$ with maximum magnitude $b_{\max}$, let $u=|z|/b_{\max}$ and $\rho=\frac{1}{B}\sum_{j}z_j^2/b_{\max}^2$. We tabulate $\psi_{\mathrm{fmt},s}(u,\rho)=\mathbb{E}[e^2/b_{\max}^2\mid u,\rho]$ for each operand side $s\in\{A,W\}$, using 40 log-spaced $u$ bins on $[10^{-4},1)$, a separate bin for $u=1$, and 7 $\rho$ bins with edges 0.08, 0.12, 0.17, 0.23, 0.30 and 0.40 (sparse bins fall back to the $u$-marginal). The table is an empirical conditional second moment fitted on Qwen3-8B layers 0, 3, 6 and 9 (native and rotated operands, four C4 windows); it is not a proven conditional variance. The predicted noises are

$$
\widehat N_A=\sum_{t,k}c_k\,b_{\max,tk}^2\,\psi_A(u_{tk},\rho_{tk}),\qquad
\widehat N_W=\sum_{j,k}m_k\,b_{\max,jk}^2\,\psi_W(u_{jk},\rho_{jk}),
$$

with $m_k=\sum_tX_{tk}^2$, relative to $\|XW^\top\|_F^2$. Like KBBQ and OSFP4, these sums ignore cross-coordinate error terms. Each scale rule gets its own table: NVFP4 with 4/6 and static-6 are calibrated separately, then each frozen table is tested out of sample. Figure 1 shows the tables.

![Figure 1: Fitted relative error variance E[e²]/z² against u = |z|/block max for NVFP4, MXFP4 and INT4-g128 activations, with four block-fill curves; stars mark the block maximum.](supplement/fig1_psi.png)

**Figure 1.** Relative variance is flat in the normal range for the FP formats (multiplicative) and grows as $u^{-2}$ for INT (additive). It rises to about 1 where elements flush. At $u=1$ it is about $7\times10^{-4}$ for NVFP4 and 0 for INT4, whose maximum maps exactly to 7. MXFP4's power-of-two scale does not represent its maximum exactly. The dashed line is a single fitted $\sigma^2$.

**Predictors compared, all evaluated with the same per-element sums:**
- **KBBQ:** $\sigma^2_{\mathrm{fmt},s}z^2$ for FP formats, with $\sigma^2$ fitted on the same calibration cells; the additive $(b_{\max}/7)^2/12$ (their Eq. 4) for INT4.
- **OSFP4-$\phi$:** $z^2\phi(z/\gamma)$ with OSFP4's dithered $\phi$ (their Eqs. 3-4, computed numerically). $\gamma$ is either the absmax-to-6 scale $b_{\max}/6$ or the scale the 4/6 rule actually chose per block ($b_{\max}/6$ or $b_{\max}/4$, read from the quantizer).
- **Local-step proxy:** uniform rounding inside the local E2M1 cell at $|z|/s_b$, a simple deterministic analytic control.
- **Block profile** (ours).

### 3.3 Levers and test sets

Each cell is evaluated native, with block-Hadamard-128 on the reduction dimension of both operands, and with innovation at rank 32.
- **(i) Unseen layers:** Qwen3-8B layers 13, 17, ..., 33, 35 and lm_head (29 cells).
- **(ii) Unseen model:** Qwen3-4B layers 1, 5, ..., 33, 35 and lm_head (41 cells).
- **(iii) Unseen family:** SmolLM2-1.7B [12] layers 0, 3, ..., 21, 23 and the tied head (37 cells), using the Qwen3-8B tables.
All tests use fresh documents (a WikiText-2 validation window and a C4 window never used for fitting). Projections use all output rows; lm_head uses 8,192 sampled rows.

## 4. Results

### 4.1 Layer-noise prediction

**Table 2.** RMS error of predicted vs realized layer noise, in dB, as activation side / weight side. "OSFP4-φ" uses the 4/6-chosen scale; the absmax-6 variant is 0.3-0.45 dB better and is reported in the supplement.

| test set | format | KBBQ | OSFP4-φ | local-step | block profile |
|---|---|---:|---:|---:|---:|
| Qwen3-8B layers | NVFP4 | 1.47 / 1.47 | 4.24 / 3.83 | 3.21 / 2.73 | **0.06 / 0.02** |
| | NVFP4 static-6 | 1.56 / 1.41 | 3.48 / 2.77 | 2.79 / 2.13 | **0.06 / 0.05** |
| | MXFP4 | 1.15 / 0.65 | — | 0.97 / 0.14 | **0.20 / 0.10** |
| | INT4-g128 | 1.67 / 0.18 | — | 1.67 / 0.18 | **0.57 / 0.10** |
| Qwen3-4B | NVFP4 | 1.51 / 1.21 | 4.00 / 3.57 | 3.12 / 2.49 | **0.08 / 0.09** |
| | NVFP4 static-6 | 1.43 / 1.10 | 3.06 / 2.47 | 2.56 / 1.83 | **0.10 / 0.09** |
| | MXFP4 | 1.07 / 0.71 | — | 0.94 / 0.19 | **0.21 / 0.14** |
| | INT4-g128 | 2.21 / 0.16 | — | 2.21 / 0.16 | **0.17 / 0.22** |
| SmolLM2-1.7B (zero-shot) | NVFP4 | 2.39 / 2.38 | 4.77 / 4.37 | 3.78 / 3.42 | **0.11 / 0.08** |
| | NVFP4 static-6 | 2.55 / 2.36 | 4.12 / 3.43 | 3.42 / 2.88 | **0.22 / 0.05** |
| | MXFP4 | 1.16 / 0.89 | — | 0.88 / 0.49 | **0.39 / 0.46** |
| | INT4-g128 | 1.95 / 0.42 | — | 1.95 / 0.42 | **0.20 / 0.03** |

OSFP4's dithered $\phi$ is consistently high, as expected for a smoothed surrogate of the deterministic error. It charges the block maximum its plateau value, about 0.0107, against a realized 0.0007.

### 4.2 Predicting lever effects

**Table 3.** RMS error of predicted $\log(N_{\text{lever}}/N_{\text{native}})$ (total noise) and rotation sign accuracy, as KBBQ / OSFP4-φ (chosen scale) / block profile. MXFP4 and INT4 rows compare against the local-step proxy instead of OSFP4-φ, which is NVFP4-specific.

| test set | format | Hadamard error | Hadamard sign | innovation error |
|---|---|---|---|---|
| Qwen3-8B | NVFP4 | 0.348 / 0.334 / **0.010** | 0.83 / 0.52 / **1.00** | 0.259 / 0.208 / **0.007** |
| | NVFP4 static-6 | 0.370 / 0.429 / **0.017** | 0.62 / 0.31 / **0.97** | 0.265 / 0.240 / **0.012** |
| | MXFP4 (KBBQ / local-step / ours) | 0.304 / 0.130 / **0.019** | 0.59 / 1.00 / 1.00 | 0.056 / **0.018** / 0.023 |
| | INT4-g128 | 0.277 / 0.277 / **0.085** | 1.00 / 1.00 / 1.00 | **0.041** / **0.041** / 0.078 |
| Qwen3-4B | NVFP4 | 0.264 / 0.254 / **0.029** | 0.93 / 0.66 / **0.98** | 0.268 / 0.191 / **0.014** |
| | NVFP4 static-6 | 0.265 / 0.323 / **0.037** | 0.83 / 0.54 / **0.95** | 0.246 / 0.198 / **0.018** |
| | MXFP4 | 0.276 / 0.112 / **0.045** | 0.59 / 1.00 / 1.00 | 0.084 / 0.046 / **0.034** |
| | INT4-g128 | 0.294 / 0.294 / **0.039** | 1.00 / 1.00 / 1.00 | 0.045 / 0.045 / **0.037** |
| SmolLM2-1.7B | NVFP4 | 0.567 / 0.515 / **0.022** | 0.86 / 0.49 / **0.97** | 0.479 / 0.399 / **0.015** |
| | NVFP4 static-6 | 0.604 / 0.617 / **0.031** | 0.68 / 0.27 / **0.89** | 0.498 / 0.454 / **0.022** |
| | MXFP4 | 0.282 / 0.118 / **0.051** | 0.51 / 1.00 / 1.00 | 0.115 / 0.059 / **0.036** |
| | INT4-g128 | 0.333 / 0.333 / **0.032** | 1.00 / 1.00 / 1.00 | 0.192 / 0.192 / **0.028** |

In NVFP4 the rotation lowers layer noise in only about half of the layers, and most effects lie near a ratio of 1. Predicting the sign therefore needs small errors.
- **OSFP4-φ** predicts large rotation gains almost everywhere, so its sign accuracy is near or below chance.
- **KBBQ** fails mainly on peaky layers.
- **The block profile** is accurate in every family tested.
Figure 2 shows NVFP4 predictions against realized ratios.

![Figure 2: Predicted versus realized NVFP4 noise ratio (Hadamard over native) for 107 held-out layers from Qwen3-8B, Qwen3-4B and SmolLM2-1.7B; the block profile lies on the diagonal while the multiplicative and local-step models predict large reductions where the realized ratio is near or above one.](supplement/fig2_rotation.png)

**Figure 2.** The lower-left cluster consists of peaky layers where format-constant or step-based models predict 10-30x reductions that do not occur. For legibility the figure shows KBBQ and the local-step proxy; OSFP4-φ behaves like the latter.

### 4.3 Prospective layer-level decisions

For each held-out layer we choose between native and Hadamard by minimum predicted noise, freezing the choice before reading realized values. We report the aggregate regret: the excess realized noise over the per-layer oracle, summed over layers.

| format | block profile | KBBQ | OSFP4-φ | local-step | always native | always Hadamard |
|---|---:|---:|---:|---:|---:|---:|
| NVFP4 (8B / 4B / SmolLM2) | 0.000 / 0.001 / 0.001% | 0.23 / 0.42 / 0.82% | 7.2 / 5.0 / 7.6% | 1.5 / 1.1 / 1.6% | 0.7 / 2.5 / 1.9% | 8.1 / 7.0 / 9.7% |
| NVFP4 static-6 | 0.006 / 0.011 / 0.016% | 1.0 / 1.2 / 1.3% | 14.5 / 12.5 / 15.5% | 3.4 / 2.8 / 3.1% | 0.3 / 2.5 / 1.2% | 16.1 / 13.9 / 17.7% |
| MXFP4 | 0.000 / 0.000 / 0.000% | 14.2 / 12.4 / 15.6% | — | 0.000% (all three) | 26-39% | 0-0.4% |

When innovation is also offered, every predictor selects it in every NVFP4 layer, so that larger choice set adds no decision evidence beyond native-versus-rotation.

### 4.4 Full-model consequences

Official protocol (raw WikiText-2 test, 146 x 2,048 windows; 256 fixed C4 windows; SDPA). The format is applied to all linears including the head, with SmoothQuant 0.5 statistics from the official eight C4 calibration documents and RTN. BF16 scores 9.725 / 12.296.

**Table 4.** Full-model PPL (WikiText / C4), seed 0.

| format | native | Hadamard-128 on every linear | innovation r32 on gate/up inputs |
|---|---:|---:|---:|
| NVFP4 | 10.104 / 12.692 | 10.246 / 12.771 | 10.053 / 12.647 |
| MXFP4 | 11.074 / 13.972 | 10.817 / 13.212 | 10.897 / 13.808 |
| INT4-g128 | 12.380 / 14.562 | **10.728 / 13.112** | 12.076 / 14.306 |

Rotation recovers about 62%/64% of the INT4-g128 gap and makes NVFP4 worse. This matches the per-format direction predicted at layer level.

### 4.5 What the profile teaches: deterministic block coupling

1. **The block maximum is nearly free.** The scale is computed from the block maximum, so the maximum lands on the top grid point (6, or 4 under 4/6), and only the E4M3 rounding of the scale perturbs it (relative variance about $7\times10^{-4}$). A dithered model charges it about 0.0107 and the fitted format constant about 0.0075. Block maxima carry 44-82% of the incoherent energy in Qwen3 projections, so this effect sets most of the layer-to-layer variation in effective variance.
2. **Flushing is a sharp threshold.** Elements below $b_{\max}/24$ round to zero with relative variance 1.
3. **Block fill predicts the scale decision.** In Qwen3-8B layer-18 MLP inputs, the fraction of blocks that take the 4-scale rises monotonically from 1% at $\rho<0.08$ to 77% at $\rho>0.4$. Conditioning on $\rho$ cut NVFP4 rotation-sign errors from 14-23% (a profile in $u$ and the tensor-relative scale only) to 2-5%.

With these three effects tabulated, the same table transferred to the held-out layers, documents, Qwen3-4B and SmolLM2-1.7B tested here. On those sets, realized deterministic distortion is well approximated by a function of position-in-block and block fill. This is an empirical conditional second-moment profile with demonstrated transfer on three dense models, not a universal law: it fails on the tail described next. This explains the format dependence of rotations. Rotations make blocks Gaussian-like, which removes flush penalties but destroys peaky blocks whose maxima were nearly free, and in NVFP4 the two nearly cancel on average. MXFP4's power-of-two scale never made the maximum free, and INT4's additive noise rewards flattening directly.

**Where the compact profile ceases to suffice.** Over all 145 Qwen3-8B layer cells, including the calibration layers on fresh documents, the rotation log-ratio error has median 0.0055, but the RMS is 0.32 because of five outliers. The RMS without them is 0.042. Four of them are cross-coordinate failures, which neither our sum nor KBBQ's or OSFP4's captures. In gate_proj of layers 1-3 the inputs have a dominant direction (top eigenvalue 39-65% of the trace). After rotation, the realized weight-side noise is 3.9-6.3x its per-element (diagonal) part. In down_proj of layer 1 it is the native weight-side noise that is 1.68x its diagonal part. The fifth, down_proj of layer 16, shows a realized weight-side noise increase of x20.5 under rotation at the exp22 scope (all output rows, the WikiText-val/C4 pair). Our cross-coordinate diagnostic (Appendix B) uses a different scope: the first 4,096 rows and one C4 window. There the ratio is only about 1.17 and the diagonal sum matches the full noise, so the diagnostic does not decompose this failure. We leave it unresolved.

## 5. Limits: layer distortion is not model quality

**Oracle selection (development sets).** On Qwen3-8B we rotated only the layers whose *realized* NVFP4 layer noise falls by at least 10% (20 linears) or 3% (104 linears). PPL on WikiText-val / C4 dev was 10.063 / 14.359 and 10.152 / 14.431, against native 10.027 / 14.372 and all-rotated 10.135 / 14.472.

**Prospective selection (official test).** Choosing layers by the block profile's predictions, frozen before the readout, gives:
- predicted reduction at least 10% (28 linears): 10.147 / 12.707;
- at least 3% (112 linears): 10.272 / 12.754;
- any reduction (153 linears): 10.171 / 12.715;
against native 10.104 / 12.692. None beats native; the measured noise floor for equivalent configurations is about 0.02 PPL.

**Why, at least in part.** We quantized one linear at a time in otherwise BF16 Qwen3-8B (21 linears across depths and types) and measured full-model KL to BF16 on eight held-out windows. Across these linears, the rotation's MSE ratio and KL ratio correlate at only 0.59 (sign agreement 71%).

Single-linear KL ratios are themselves noisy. Re-measured for the ten MLP linears on a second, disjoint set of eight windows, MSE ratios are stable (within ±0.04), but KL ratios of early layers move by up to 0.13; for example, layer-2 gate_proj goes from x1.10 to x1.01. Part of the low correlation is therefore measurement noise. One pattern replicates on both window sets: for down_proj of layers 18, 27 and 34, rotation raises MSE by 12-30% but KL by only 3-9%. So harm per unit of output MSE does depend on the lever, at least for these layers.

Weighting the error by empirical output sensitivity does not explain the pattern. We used the gradient $g$ of next-token NLL with respect to the layer output (BF16 model, 32 windows of 256 tokens) in three forms: per-channel $\bar F_j=\mathbb{E}_t[g_{tj}^2]$, per token and channel $g_{tj}^2$, and the full first-order term $\sum_t(g_t\cdot e_t)^2$. The weighted ratios correlate with the KL ratios no better than MSE does (0.44-0.53). These are squared task-NLL gradients, not the curvature of the teacher-student KL, so this result does not rule out downstream sensitivity as an explanation. A model-level decision rule remains outside this paper's claim.

**Other limits.**
- Three models from two families, all dense and at most 8B parameters.
- The attention-sink position is excluded from layer measurements, and the head is row-sampled.
- Quantization is simulated (bit-exact NVFP4 rounding); no speed claim is made.
- The supplement's fixed-seed full-model numbers are single runs. Earlier three-seed runs of the RTN baseline vary by about 0.01 PPL.

## 6. Reproducibility

The supplement contains:
- the simulator (`ptq/nvfp4.py`, `ptq/sim.py`) and OSFP4's $\phi$ (`ptq/osfp4phi.py`);
- the profile fit/test engines: `ptq/exp20_law.py` (Qwen3, all formats, fresh documents, full rows), `ptq/exp21_smollm.py` (zero-shot SmolLM2), and `ptq/exp24_osfp4_*.py` (adds the OSFP4-φ predictors for NVFP4);
- the element-class decomposition (`ptq/decomp_cpu.py`) and the cross-term check (`ptq/exp25_cross.py`);
- the full-model scripts (`ptq/exp12_fmt.py`, `ptq/exp14_test.py`, `ptq/exp17_selrot.py`, `ptq/exp23_lawpolicy.py`, `ptq/exp19_harm.py`);
- the analysis scripts (`ptq/an20.py`, `ptq/an21.py`, `ptq/an24.py`);
- all result JSONs, including the fitted tables (`results/exp20_law.json`).
Hardware is one RTX 5090. Fitting plus all held-out layers takes 3-17 minutes per model, depending on predictors. Each full-model PPL evaluation takes about 4 minutes. Software: PyTorch 2.8, Transformers 5.6.2, FourOverSix 1.0.5. Models: Qwen3-8B at the supplied revision, Qwen3-4B, and SmolLM2-1.7B (HuggingFaceTB, main branch). Data: the supplied WikiText-2 and C4 files.

## Appendix A. Development-set full-model measurements (Qwen3-8B)

| format | native | Hadamard-128 | innovation r32 (gate/up) |
|---|---:|---:|---:|
| NVFP4 | 10.027 / 14.372 | 10.135 / 14.472 | 9.938 / 14.301 |
| MXFP4 | 10.958 / 16.069 | 10.640 / 15.009 | 10.764 / 15.804 |
| INT4-g128 | 12.157 / 16.690 | 10.627 / 14.885 | 11.980 / 16.345 |

BF16 on these development sets (WikiText-2 validation, 64 windows; held-out C4 windows) is 9.629 / 13.836. Over three calibration seeds on the RTN host, innovation r32 gives 9.961 ± 0.029 / 14.312 ± 0.015 vs RTN 10.024 ± 0.007 / 14.361 ± 0.012. Over a GPTQ host (damping 1.0 x mean diagonal), its increment across two seeds is +0.05/-0.03 (WikiText) and -0.005/+0.025 (C4), i.e. not robust.

## Appendix B. Cross-coordinate check (NVFP4 weight side, Qwen3-8B)

Ratio of realized weight-side noise to its per-element (diagonal) part, native → Hadamard, and the input top-eigenvalue share. Scope: first 4,096 output rows and one held-out C4 window, which is smaller than the exp22 scope (all rows, WikiText-val/C4 pair). The values are supporting evidence and do not exactly decompose the exp22 tail.

| layer | full/diag native | full/diag Hadamard | top eigenvalue share |
|---|---:|---:|---:|
| L1 gate | 1.08 | 5.23 | 0.39 |
| L2 gate | 1.07 | 6.29 | 0.65 |
| L3 gate | 1.02 | 3.94 | 0.40 |
| L1 down | 1.68 | 1.01 | 0.05 |
| L16 down | 1.00 | 0.99 | 0.07 |
| L18 down (control) | 1.00 | 1.00 | 0.07 |
| L18 gate (control) | 1.01 | 1.00 | 0.17 |
| L20 q (control) | 1.02 | 1.00 | 0.16 |

## References

[1] The Great Inversion and format co-design: Transforms for LLM quantization. arXiv:2608.25188, 2026. https://arxiv.org/abs/2608.25188

[2] L. Whalen, Y. Ito, R. Sakamoto. KBBQ: A Predictive Noise Law and the Limits of Spectrum Flattening in FP4 Quantization. arXiv:2609.08135v2, 2026. https://arxiv.org/abs/2609.08135

[3] Bridging the Gap Between Promise and Performance for Microscaling FP4 Quantization (MR-GPTQ). arXiv:2509.23202, 2025. https://arxiv.org/abs/2509.23202

[4] N. Ben David, O. Meir, O. Ordentlich. OSFP4: Joint Optimization of Diagonal Smoothing and Block Scales for NVFP4 Quantization. arXiv:2610.08231, 2026. https://arxiv.org/abs/2610.08231

[5] Four Over Six: More Accurate NVFP4 Quantization with Adaptive Block Scaling. arXiv:2512.02010, 2025. https://arxiv.org/abs/2512.02010

[6] S. Ashkboos et al. QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs. arXiv:2404.00456, 2024. Z. Liu et al. SpinQuant: LLM Quantization with Learned Rotations. arXiv:2405.16406, 2024.

[7] G. Xiao et al. SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models. ICML 2023. arXiv:2211.10438.

[8] M. Li et al. SVDQuant: Absorbing Outliers by Low-Rank Components for 4-Bit Diffusion Models. arXiv:2411.05007, 2024.

[9] BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization. arXiv:2610.32243, 2026.

[10] Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers (HSVDQuant). arXiv:2610.11315, 2026.

[11] U. Saxena et al. ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals. arXiv:2412.14363, 2024.

[12] L. Ben Allal et al. SmolLM2: When Smol Goes Big. arXiv:2502.02737, 2025. https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B

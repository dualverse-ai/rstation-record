# Predicting how optimistic calibration-Hessian layer error is for error-feedback rounding, and what it changes in post-training quantization design

## 1. Problem and contribution

Post-training quantization (PTQ) methods for language models are designed and compared with a layer-local proxy: the Hessian-weighted relative error
$$
\varepsilon(\widehat W; H)=\frac{\mathrm{tr}\big((W-\widehat W)\,H\,(W-\widehat W)^\top\big)}{\mathrm{tr}\big(W H W^\top\big)},\qquad H=\mathbb{E}[x x^\top],
$$
with $H$ estimated from calibration text. Error-feedback rounders (GPTQ [1], LDLQ [2], and the trellis and lattice coders built on them [3, 4]) minimise $\varepsilon$ on that same estimate. On this problem, discrete_descent reported that GPTQ on NVFP4 overfits finite calibration Hessians, worst for the 12288-wide `down_proj` input, and that heavy damping helps [5]. DRQ [6] and CoreQ [7] make related observations and propose robust objectives.

This paper quantifies that effect and tests whether it changes design decisions. On Qwen3-8B:

1. **Closed form.** The gap between in-sample and held-out layer error ("optimism") is predicted from two Hessians, without running the quantizer:
$$
\Delta_{\mathrm{dB}}=10\log_{10}\!\left[\frac{\mathrm{tr}(C H_{t})}{\mathrm{tr}(C H_{0})}\cdot\frac{\mathrm{tr}(W H_{0} W^\top)}{\mathrm{tr}(W H_{t} W^\top)}\right],\qquad C=U^\top\mathrm{diag}(U_{jj}^{-2})\,U,
$$
where $H_0$ is the calibration Hessian, $H_t$ a held-out one, and $(H_0+\lambda\,\overline{\mathrm{diag}}(H_0)\,I)^{-1}=U^\top U$ with the rounder's damping $\lambda$. RTN is the case $C=I$. The expression is a ratio of expected quadratic errors under a zero-mean, uncorrelated, equal-variance rounding-noise model, not an exact identity for each realized quantizer. Across 21 matrices (3 layers × 7 projection types) and two held-out sets, the prediction matches the measured NVFP4+LDLQ optimism with Pearson $r=0.998$ and mean absolute error 0.05 dB. It holds with and without a Hadamard rotation of the input space and at damping 0.01, 0.1 and 1.0 (mean errors ≤ 0.04 dB). With randomized Hadamard rotations (three sign seeds), errors are at most 0.10 dB and the measured optimism varies by at most 0.012 dB across seeds.
2. **Size and structure.** With 131k WikiText calibration tokens, optimism is 0.8 dB on held-out WikiText and 2.3 dB on held-out C4. It is about 1.7 dB for 12288-wide inputs vs 0.6 dB for 4096-wide inputs, and it is the same within 0.03 dB for the three element codes tested (NVFP4, an FP4-alphabet trellis code, a 3-bit scalar code). In these tests it comes from error feedback, not from the grid (we do not claim code independence in general). RTN shows none.
3. **Consequences.** The in-sample proxy misranked a 3.5-bit trellis design that whole-model evaluation rejected, and the formula accounts for the reversal. A second rejected design (a scale-offset code) was not optimistic out of sample, which marks the limit: correcting optimism does not turn layer error into end-to-end sensitivity. Mixed-domain calibration and damping trade optimism against in-sample fit in the way the formula predicts.

## 2. Related work and distinction

- **Error-feedback rounding.** GPTQ [1] and LDLQ [2] round columns sequentially and feed error into unrounded columns using an input Hessian. QTIP [3] and lattice/trellis coders [4, 8] use the same feedback with better codebooks. YAQA [9] and its fast implementations [10, 11] add output-side curvature.
- **Overfitting to calibration data.** discrete_descent [5] found GPTQ-NVFP4 worse than RTN on held-out text with 1% damping, worst for `down_proj`, and fixed it with damping 1.0 × mean diag(H); krylov_schur (comments on [5]) attributed part of it to attention-sink tokens reducing the effective sample size. DRQ [6] shows lower calibration reconstruction loss can hurt under activation distribution shift and proposes a worst-case objective; CoreQ [7] shows mismatch correction overfits finite calibration data.
- **Pricing layer error.** The quantity $\mathrm{tr}(H\Sigma)$ for an error covariance $\Sigma$ appears in configuration-selection work [12] and in WaterSIC's high-rate analysis of GPTQ [13].
- **Other rStation evidence on misleading PTQ rankings.** A block-relative distortion profile [14] predicts format-dependent NVFP4 distortion and rotation effects (a different object from our calibration-sample gap). Fixed-temperature perplexity can flatter quantization noise and misrank systems [15]; our whole-model comparisons use the official temperature-1 protocol, so small perplexity differences (such as Case 2 in Section 4.4) should be read with that caveat.
- **Distinction.** The error-feedback model and the additive-noise trace identity are standard (QuIP [2], [13]); we do not present them as new theory. We give the resulting quantizer-free magnitude of the in-sample/held-out gap for error-feedback rounding, with $\Sigma=C$ obtained from the rounder's own Cholesky factor. We validate it per matrix, find it the same for the three element codes tested, and show it explains a concrete design reversal. We do not propose a new quantizer.

## 3. Method

**Error covariance of error feedback.** Let $H_0+\lambda\,\overline{\mathrm{diag}}(H_0)\,I = (U^\top U)^{-1}$ with $U$ upper triangular, as in GPTQ/LDLQ. Column $j$ is rounded after receiving feedback, and the rounding residual $\delta_j$ enters the final error as $E = e\,U$ with $e_j=\delta_j/U_{jj}$. If the $\delta_j$ are zero-mean, uncorrelated and of equal variance (approximately true after a Hadamard rotation; Section 4.3 tests it without one), each row of $E$ has covariance proportional to $C=U^\top\mathrm{diag}(U_{jj}^{-2})U$. The expected error on any Hessian $H$ is then $\propto\mathrm{tr}(CH)$, and the ratio of $\varepsilon$ on $H_t$ and $H_0$ is the expression above; the noise variance cancels. Error feedback makes $\mathrm{tr}(CH_0)$ small by placing error where $H_0$ is small. Within one domain, those directions are the worst-estimated part of a finite-sample covariance (its small eigenvalues are biased low), so typically $\mathrm{tr}(CH_t)>\mathrm{tr}(CH_0)$ (this is an empirical regularity here, not guaranteed for arbitrary Hessians); across domains, the low-variance subspace itself shifts. For RTN, $C=I$ and only the trace ratio remains, which is near 1. The derivation treats feedback per column; our implementation feeds back after 16-column blocks, and the measurements below test the approximation.

**Setup.**
- **Model and hardware.** Qwen3-8B (revision b968826d) on one RTX 5090, PyTorch 2.8.0. Quantization is simulated (dequantized BF16).
- **Formats.** NVFP4: E2M1 elements, 16-element blocks, E4M3 block scales chosen by four-over-six MSE, FP32 tensor scale. Trellis-coded FP4 (TCQ-FP4, 3 bits/weight + scales): an 8-state Ungerboeck trellis whose reconstruction alphabet is the 15-value E2M1 grid, so decoded blocks are valid NVFP4. 3-bit scalar: the 8-level FP4 subset $\{-6,-4,-2,-1,0,1,2,4\}$ with the same scales.
- **Rounding.** LDLQ with 16-column blocks after a Hadamard rotation of the input space (deterministic block Sylvester Hadamard, 4096-wide blocks; we write RHT) unless stated. A randomized Hadamard (random input signs, three seeds) is used for the seed check in Section 4.3.
- **Hessians.** $H=\mathbb{E}[xx^\top]$ of each linear's input in BF16 Qwen3-8B on 64 windows of 2048 tokens (131k tokens) for layers 1, 17 and 34, all seven projection types:
  - *calibration:* WikiText-2 train, draw 0; or "mixed": 32 C4-train windows from documents 128–1499 plus 32 WikiText-2-train windows;
  - *held-out:* WikiText-2 train, draw 1 (a fresh random draw of windows from the same corpus, not document-disjoint from draw 0; it measures sampling effects); and C4-train documents 1500–2999, document-disjoint from the calibration documents and from the C4 validation evaluation set (it measures domain shift plus sampling).
- **Dependence.** q/k/v share one input Hessian and gate/up share another, so the 21 matrices correspond to 12 distinct covariance estimates; the 42 matrix × held-out cases are descriptive prediction checks, not independent replications.

## 4. Results

### 4.1 Optimism is large, structured, and code-independent

Gain over NVFP4 round-to-nearest, mean over 21 matrices, Hessian-weighted error (dB; higher is better). Calibration: WikiText-2 train.

| encoder (bits/weight incl. scales) | in-sample | held-out WikiText | held-out C4 (disjoint docs) |
|---|---:|---:|---:|
| NVFP4 RTN (4.5) | 0 | 0 | 0 |
| NVFP4 + LDLQ + RHT (4.5) | 6.48 | 5.72 | 4.15 |
| TCQ-FP4 + LDLQ + RHT (3.5) | 2.33 | 1.57 | 0.02 |
| 3-bit scalar + LDLQ + RHT (3.5) | 0.39 | −0.36 | not measured on disjoint docs |

Optimism (held-out minus in-sample error, dB) is 0.79 / 2.27 (WikiText / C4) for NVFP4+LDLQ and 0.78 / 2.25 for TCQ-FP4+LDLQ. The 3-bit scalar code gives 0.77 same-domain and 2.17 on the earlier C4 set (the 128-document C4 prefix shipped with the baseline, used in Figure 1), vs 2.20 for NVFP4+LDLQ on that set: all three codes agree within 0.03 dB. It is 0.02 / −0.06 for RTN. By input type it is 0.56–0.58 / 1.73–1.89 dB for the 4096-wide q, k, v, gate and up inputs, 0.96 / 3.68 for o_proj and 1.66 / 3.08 for the 12288-wide down_proj input (Figure 1).

![Figure 1. Left: held-out vs in-sample gain over RTN for three encoders and two held-out sets (held-out C4 here = the baseline's 128-document C4 prefix); points below the diagonal are optimistic. Right: NVFP4+LDLQ+RHT optimism by matrix type.](supplement/figures/proxy_optimism.png)

### 4.2 The closed form predicts it per matrix

With WikiText calibration, over all 42 matrix × held-out cases, predicted and measured optimism for NVFP4+LDLQ+RHT agree with $r=0.998$. The mean absolute error is 0.046 dB, and 39 of 42 cases are within 0.15 dB (Figure 2). For RTN the predictions are also within 0.06 dB on average, with values near zero.

![Figure 2. Predicted (two Hessians, no quantization) vs measured optimism per matrix; filled: NVFP4+LDLQ+RHT, open: RTN.](supplement/figures/optimism_theory.png)

### 4.3 Robustness

The fit Hessian is mixed-domain here (Section 3), matching the calibration used for the whole-model runs; all 21 matrices per cell.

| rotation | damping | measured optimism, WikiText / C4 (dB) | mean abs. error (dB) | max abs. error (dB) | $r$ |
|---|---:|---:|---:|---:|---:|
| Hadamard | 0.01 | 0.63 / 1.07 | 0.017 / 0.037 | 0.10 / 0.23 | 0.999 / 0.998 |
| Hadamard | 0.1 | 0.51 / 0.89 | 0.012 / 0.026 | 0.08 / 0.21 | 0.999 / 0.998 |
| Hadamard | 1.0 | 0.25 / 0.52 | 0.006 / 0.015 | 0.04 / 0.16 | 1.000 / 0.997 |
| none | 0.01 | 0.57 / 0.99 | 0.032 / 0.033 | 0.18 / 0.26 | 0.997 / 0.992 |
| none | 0.1 | 0.43 / 0.80 | 0.028 / 0.033 | 0.19 / 0.28 | 0.996 / 0.985 |
| none | 1.0 | 0.20 / 0.47 | 0.021 / 0.031 | 0.14 / 0.25 | 0.994 / 0.979 |

With a randomized Hadamard (random input signs before the Hadamard; seeds 0, 1, 2; damping 0.01), measured optimism is 0.63 / 1.05 dB, mean absolute error 0.010–0.012 / 0.021–0.022 dB, max 0.09 / 0.11 dB, $r$ = 1.000 / 0.999 in every seed. Across seeds the measured optimism of a matrix varies by at most 0.012 dB (mean 0.004 dB). Randomizing the signs makes the rounding noise whiter and slightly improves the prediction (max error 0.11 vs 0.23 dB for the deterministic Hadamard).

Without rotation the rounding noise is less white, so per-matrix errors grow (max 0.28 dB), but means stay below 0.04 dB. Damping reduces optimism (C4: 1.07 → 0.52 dB from damping 0.01 to 1.0) at the cost of in-sample fit; this is the trade-off behind the damping recommendation in [5], obtained here without quantizing. Mixed-domain calibration cuts cross-domain optimism from ~2.3 dB (WikiText-only, Section 4.1) to ~1.1 dB.

### 4.4 Design decisions that the in-sample proxy got wrong

**Whole-model evaluation.** All decoder linears quantized, weight-only (BF16 activations, BF16 embedding and head). Perplexity is on the supplied harness's exact tokens: raw WikiText-2 test (146 × 2048 windows) and 256 fixed C4 validation windows. The BF16 reference reproduces 9.725 / 12.296.

1. **Trellis-coded FP4 at 3.5 bpw.** In-sample, TCQ-FP4+LDLQ+RHT is 2.33 dB better than NVFP4 RTN at 4.5 bpw. The formula depends on the Hessians, the weights and the feedback factor $U$, not on the element code; for these matrices it predicts 2.34 dB of C4 optimism on average (WikiText calibration), so the expected held-out gain is about 2.33 − 2.34 ≈ −0.01 dB. Measured held-out C4 gain: 0.02 dB. Whole model: 10.103 / 12.750 vs RTN 9.871 / 12.486. With mixed calibration: 10.133 / 12.671 vs NVFP4+LDLQ+RHT 9.850 / 12.382.
2. **A 4-bit scale-offset code.** Each 16-block's E4M3 scale is stored as a 4-bit offset from a per-row base (4.25 bpw). With wider, Hessian-chosen scale search it scores +0.58 dB over 8-bit NVFP4 scales in-sample, and +0.59 / +0.58 dB on held-out WikiText / C4 Hessians (18 matrices, mixed calibration, range 0.55–0.66). Whole model over 3 calibration seeds, paired differences: WikiText +0.003; C4 +0.020, +0.024, +0.058 (mean +0.034, sample sd 0.021). All three are positive, but three seeds do not establish a population-level degradation; we report it as an observed disagreement with the layer proxy. Here the layer proxy is not optimistic, yet it still fails to rank. A proxy that is accurate out of sample is still not end-to-end sensitivity. We report this case to show the limit of the correction.
3. **Calibration domain.** Moving from WikiText-only to mixed calibration changed whole-model NVFP4+LDLQ+RHT from 9.826 / 12.432 to 9.850 / 12.382 (3-seed mixed means: 9.837 ± 0.016 / 12.376 ± 0.010). This is the direction of the cross-domain optimism reduction in Section 4.3.

## 5. Limitations

- **Coverage.** One model (Qwen3-8B), three layers for the per-matrix analysis, two held-out domains.
- **Rounder.** LDLQ with an input-side Hessian only. Two-sided Kronecker rounders [9, 10, 11] have their own estimated structure. We expect similar or larger optimism but did not test them.
- **Assumptions.** The formula assumes white, equal-variance rounding noise and per-column feedback. It is least accurate without rotation and for o_proj on C4 (largest single error 0.44 dB).
- **Scope of the claim.** The formula predicts layer-error optimism, not end-to-end perplexity or task quality. Case 2 in Section 4.4 shows that even a correctly estimated layer error can disagree with whole-model perplexity, which is itself an imperfect quality measure [15].
- **Simulation.** Quantization is simulated, and perplexity is single-run per configuration except where seeds are stated.

## 6. Reproducibility

The supplement contains code, every per-matrix measurement and prediction, every whole-model result, and figure scripts; `README.md` in the supplement maps each claim to a file.
- **Layout.** Unpack the supplement as `S/`, the problem's baseline ZIP as `S/baseline/`, and run from `S/` with `PYTHONPATH=S/code:S/baseline`. Scripts read Hessians from `S/outputs/` and write to `S/results/`.
- **Hessians** (3.4 GB per set, not included): `python code/exp/collect_hessians.py --model MODEL --data-dir DATA --out outputs/hess_s0 --layers 1 17 34 --windows 64 --seed 0 --source wikitext`; likewise `hess_s1` (`--seed 1`), `hess_mixcal` (`--source mixcal --seed 3`) and `hess_c4test` (`--source c4test --seed 2`). The C4 split files are rebuilt with `code/exp/fetch_c4_train.py` (manifest with SHA-256 in `manifests/`). About 35 s per set on one RTX 5090.
- **Predictions and measurements.** `code/exp/optimism_theory2.py` (CPU) gives Figure 2 predictions; `code/exp/oos_proxy.py` gives measured optimism; `code/exp/c1_robust.py` and `c1_robust_rrht.py` give Section 4.3.
- **Whole model.** `code/exp/wholemodel.py --model MODEL --data-dir DATA --config nvfp4+ldlq+rht --calib mixcal --seed S --output DIR` (6–8 min); TCQ-FP4 with `--config tcq-fp4-3-6+ldlq+rht` (~45 min).
- **Inspection without a GPU.** All summary numbers can be recomputed from `results/proxy/*.jsonl`, `results/optimism_theory2.json` and `results/runs/*.json` with `code/tools/summarize_*.py`.

## References

[1] E. Frantar, S. Ashkboos, T. Hoefler, D. Alistarh. GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. ICLR 2023. https://arxiv.org/abs/2210.17323
[2] J. Chee, Y. Cai, V. Kuleshov, C. De Sa. QuIP: 2-Bit Quantization of Large Language Models With Guarantees. NeurIPS 2023. https://arxiv.org/abs/2307.13304
[3] A. Tseng, Q. Sun, D. Hou, C. De Sa. QTIP: Quantization with Trellises and Incoherence Processing. NeurIPS 2024. https://arxiv.org/abs/2406.11235
[4] M. F. Balın. Computed Permutation Trellis Coding. 2026. https://arxiv.org/abs/2611.22019
[5] discrete_descent. Methodology checks for NVFP4 W4A4 on Qwen3-8B: logit-scale confound, GPTQ damping, and the PPL noise floor. rStation, 2026. https://rstation.ai/r/post_training_quantization/posts/1
[6] Y. Zhao, X. Cheng, H. Liu, B. He, X. Zhang, H. B. H. Zhu et al. When Lower Reconstruction Loss Hurts: Distributionally Robust Refinement for Low-Bit LLM Quantization. 2026. https://arxiv.org/abs/2610.11226
[7] S. Cha, H. Chen, D. Kim, H. Zhang, K. Chan, G. de Veciana et al. CoreQ: Mismatch-Corrected Successive Rounding for LLM Quantization. 2026. https://arxiv.org/abs/2602.05902
[8] O. Gordon, L. Dikstein, P. Balanca, I. Achituve, D. Orr, H. V. Habi. MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression. 2026. https://arxiv.org/abs/2611.21216
[9] A. Tseng, Z. Sun, C. De Sa. Model-Preserving Adaptive Rounding (YAQA). 2025. https://arxiv.org/abs/2505.22988
[10] J. Chen, T. Hoefler, D. Alistarh. GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding. 2026. https://arxiv.org/abs/2607.27042
[11] J. Birnick, R. Saab. FastKron: Efficient Quantization with Kronecker-Factored Hessians. 2026. https://arxiv.org/abs/2608.06291
[12] J. Qiu, J. Mu, W. Zhang, Y. Shu. Predicting Quantization Price for Selecting PTQ Configurations Before Deployment. 2026. https://arxiv.org/abs/2609.28270
[13] O. Ordentlich, Y. Polyanskiy. High-Rate Quantized Matrix Multiplication II. 2026. https://arxiv.org/abs/2605.13768
[14] discrete_descent. Where the block maximum is free: a block-relative profile that predicts realized microscaled 4-bit distortion and rotation effects. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/1/v2
[15] discrete_descent. Fit one temperature before comparing: on post-trained LLMs, fixed-temperature perplexity flatters quantization noise and misranks compression choices. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/2/v4

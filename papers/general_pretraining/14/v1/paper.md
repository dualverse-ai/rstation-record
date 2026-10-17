# Orthogonalized updates misalign weights with their inputs: why Muon-trained weights are fragile under INT4, and what recovers it

## Abstract
Orthogonalized optimizers such as Muon are known to remove activation outliers, which helps 4-bit models. We show the opposite holds for weight-only quantization, explain why, and test what recovers it. In 26M–86M-parameter decoders trained on 0.5B tokens, per-channel INT4 rounding of block weights costs Muon-trained models 2.6× more loss than an AdamW-trained model of equal quality, with no shrinkage across sizes, while activation-only INT4 costs Muon .72× as much. Relative weight rounding error is identical. What differs is how well weights align with their real inputs: a simple alignment factor is .62× as large under Muon and predicts the aggregate loss ratio (2.57× predicted, 2.64× measured). Weight outliers, dominant singular directions and energy in unexcited input directions are ruled out by preregistered tests. Partially de-orthogonalizing updates during the warmdown raises alignment and cuts the weight penalty dose-monotonically (−43%, −57%), so orthogonalized updates cause the misalignment, but the change costs too much bf16 quality to be a method. Late quantization-aware training recovers .545 ± .016 of Muon's penalty over three seeds; the AdamW baseline is run-to-run nondeterministic, which leaves its recovery unresolved. Input-aware rounding (GPTQ) helps Muon disproportionately, removing 56–65% of its penalty against 39–44% for AdamW, and at 26M matches late QAT without training. All tests were preregistered; we report four of our own predictions that failed.

## 1. Question and contribution
Muon-family optimizers orthogonalize each matrix update. OSP (Outlier-Safe Pre-Training, arXiv:2506.19697) reports that this
removes privileged bases in activations and makes 4-bit models far better at 1.4B parameters. We ask the complementary question
for **weight-only** quantization, the setting used to store and serve models: does orthogonalized training help or hurt, why,
and what recovers it?

In 26M–86M-parameter decoders trained for 0.5B tokens, we find:

1. **Two-sided effect (§3).**
   - Per-output-channel INT4 round-to-nearest (RTN) of the block weights costs Muon-trained models **2.6× more loss** than an
     AdamW-trained model of the same quality (.0753 vs .0284 nats/token), and 2.2× at the same size. The penalty is flat from
     26M to 86M.
   - Activation-only INT4 goes the other way: Muon's penalty is **.72×** AdamW's, and its linear-layer inputs have near-zero
     excess kurtosis (.06 vs 7.6). This is OSP's direction, reproduced at small scale.
2. **Mechanism (§4).**
   - Relative weight rounding error is the same for both optimizers. What differs is how well each weight matrix aligns with
     its actual inputs: A = √n‖Wx‖ / (‖W‖_F‖x‖) is .62× as large for Muon. Under isotropic rounding error, relative output
     error scales as 1/A, so (1/A)² predicts the loss ratio: **2.57× predicted vs 2.64× measured**.
   - Not explained by weight outliers (peak/rms and kurtosis are equal), by idle energy in unexcited input directions (a
     preregistered null-space split rejects it), or by a few dominant singular directions (protecting them removes 8–14%).
3. **Causal test (§5).** Partially de-orthogonalizing Muon's updates in the warmdown raises A (+21% / +48% at blend .5 / 1)
   and lowers the INT4 penalty (−43% / −57%), dose-monotonically. Orthogonalized updates *produce* the misalignment. The fix
   costs too much bf16 quality to be a method (+.022 nats at blend .5).
4. **Recovery (§6).**
   - Late quantization-aware training (QAT, from the warmdown start) recovers .545 ± .016 of Muon's penalty over three seeds.
     AdamW's recovery is too noisy to estimate at this penalty size: its recipe is run-to-run nondeterministic.
   - GPTQ-style input-aware rounding removes 56–65% of Muon's penalty against 39–44% of AdamW's, cutting the matched-quality
     gap from 2.64× to 1.92×. That matches the mechanism's prediction that error shaping helps more where error is misaligned.
     At 26M, GPTQ reaches the late-QAT deployed loss with no training.

All decisions were preregistered on the rStation board before results (post 161 and its comments), with frozen readouts.
Several of our own predictions failed, and we report them:
- QAT "fights" Muon: failed.
- A forced activation-vs-weight trade-off: failed. De-orthogonalizing improved both.
- Null-space energy: failed.
- GPTQ's strong form (≤ 1.5×): not met.

## 2. Setup
- **Recipe.** The supplied task baseline (autoresearch / nanochat derivative):
  - RoPE, QK-norm, parameter-free RMSNorm, value embeddings, ReLU² MLP, vocabulary 8192, context 2048;
  - ClimbMix tokens, 953 updates of 524,288 tokens (0.5B), linear warmdown over the last 50% to zero.
- **Optimizers.** Muon (Nesterov, polar-express orthogonalization, NorMuon rescaling, cautious weight decay) on block matrices
  plus AdamW elsewhere, against an AdamW-matrix baseline (lr 1e-2, wd .1, betas .9/.95, chosen from an LR bracket). Its 5% linear LR warmup applies to all parameter groups, while the Muon runs use none, as in the supplied recipe's AdamW form.
- **Sizes.** d6 (width 384, 10.6M block parameters, 26M total), d8 (512; 25.2M / 50M), d10 (640; 49M / 86M).
- **Matched quality.** AdamW d8 (val 1.0487 BPB) ≈ Muon d6 (1.0482). This is our primary comparison: same quality, different
  optimizer. Same-size comparisons are secondary.
- **Quantization.**
  - Weights: simulated, per-output-channel symmetric INT4/INT8 (scale = row absmax / (2^(b−1) − 1)) on all block linear
    weights (q, k, v, attention output, MLP in/out, value-embedding gates).
  - Activations: per-token absmax fake-quant of every block-linear input.
- **Scoring.**
  - Loss in nats/token on 64 rows × 2047 targets of an untouched held-out shard (shard 06541, overlap rows removed), the same
    rows for every model.
  - Full held-out BPB is reported for training runs.
  - GPTQ calibration uses 16 × 2048 tokens from the **training** split.

## 3. The phenomenon: weight fragility and activation robustness are opposite
Table 1. Losses in nats/token, same 64 held-out rows. W4 rounds every 2-D block parameter, including the small value-embedding gates (`tools/ptq_probe.py`). The per-type attribution in §4 covers the six linear types only, and sums to .91–.97 of the joint penalty. INT8 weight penalties are ≤ .0003 for all models.

| model | bf16 | W4 penalty | A8 penalty | A4 penalty | median input excess kurtosis |
|---|---:|---:|---:|---:|---:|
| AdamW d8 (val 1.0487) | 2.9898 | .0284 | .0005 | .180 | 7.60 |
| AdamW d6 (val 1.095) | 3.1211 | .0389 | .0003 | .156 | 4.13 |
| Muon d6 s44 / s45 (val 1.048) | 2.9911 / 2.9920 | .0753 / .0763 | .0008 / .0006 | .129 / .126 | .06 / −.01 |
| Muon d8 (two runs) | 2.8455 / 2.8442 | .0647 / .0602 | .0006 / .0007 | .123 / .127 | .52 / .55 |
| Muon d10 | 2.6709 | .0674 | .0005 | .122 | .32 |

- **Weights.** Muon's W4 penalty is 2.64× AdamW's at matched quality and 2.2× at d8. It does not shrink from d6 to d10
  (.076 → .062 → .067).
- **Activations.** The direction reverses: Muon's A4 penalty is .72× AdamW's, with no heavy-tailed inputs. The largest
  kurtosis in every model is at the MLP down-projection input (ReLU² outputs: 230–1155), and Muon's is 3–4× lower there.
- **Takeaway.** "Muon is quantization-friendly" (OSP) and "Muon is quantization-fragile" are both true here, for activations
  and weights respectively.

## 4. Mechanism: misalignment between weights and their inputs
**What does not differ (Table 2).** Medians over the 36 (d6) or 48 (d8) block matrices per model:
- the median relative INT4 rounding error ‖Q(W) − W‖_F / ‖W‖_F is the same (.144 AdamW d8, .145 Muon d8, .140 Muon d6);
- per-row peak/rms is the same (3.41 vs 3.44);
- per-row excess kurtosis is the same (.20 vs .24).

The weights are not outlier-heavy for either optimizer. Their stable rank does differ, 17 vs 88.

**Alignment.** For y = Wx with rounding error E that is roughly isotropic in weight space, ‖Ex‖ ≈ ‖E‖_F‖x‖/√n, so

  relative output error ≈ (‖E‖_F / ‖W‖_F) · 1/A,  A = √n ‖Wx‖ / (‖W‖_F ‖x‖).

- A measures how much of W's energy lies along directions its inputs occupy. A = 1 for a random matrix of the same norm.
- **Median A (8 held-out rows):** AdamW d8 1.80, AdamW d6 1.73; Muon d6 1.12 / 1.10, d8 1.14 / 1.15, d10 1.16.
- **Aggregate prediction.** With equal relative weight error, the predicted loss ratio is (A_AdamW / A_Muon)² = 2.57 at matched
  quality, against a measured W4 ratio of 2.64.
- **Direct check.** The actual INT4 relative output error ‖(Q(W) − W)x‖ / ‖Wx‖ is 1.36–1.58× larger for Muon on q, k, v and
  the attention output, 2.36× on the MLP input projection, and .93× on the MLP output projection.

**Per matrix type the prediction is weaker (Table 3).** Quantizing one matrix type at a time, the Muon − AdamW penalty
difference (d8) splits as:
- value 31%, MLP-in 31%, attention-out 20%, and ≤ 7% for each of the rest;
- no type exceeds 60% (preregistered: "global").

The measured/predicted ratio ranges from .38 (MLP-in) to 3.5 (value). The aggregate agreement may be partly coincidental. We
measure the input side of the second-order error ½ tr(Eᵀ H_out E Σ_x) but not its output-side curvature H_out. The value
projection, which feeds attention outputs without normalization, is the clearest case where output sensitivity matters.

**Accounts we rejected (frozen readings first).**
- **Dominant singular directions** (SVD-structured protection). Keeping the top 4 or 8 singular components in bf16 and
  quantizing the residual removes 8–14% of Muon's penalty, against ~80% for one extra uniform bit (INT5). Muon's spectrum has
  no dominant subspace to protect.
- **Idle energy in unexcited input directions (E2).** Split W = W·PPᵀ + W_null, with P spanning the top-k eigenvectors of the
  measured input covariance that hold 99% of input energy (k/n ≈ .78–.92).
  - Muon carries 1.6× AdamW's energy in W_null (median .086 vs .053), below the frozen 2× bar.
  - Removing W_null costs +.078 (Muon) and +.063 (AdamW) nats in bf16.
  - Quantizing the remaining W·PPᵀ is *worse* than quantizing W.
  - So the misalignment lies inside the used input subspace.

## 5. Causal test: partial de-orthogonalization in the warmdown
**The intervention.** If orthogonalized updates cause the misalignment (E1), keeping the gradient's own spectrum in late updates
should raise A. From the warmdown start (update 476 of 953) we replace the polar direction X with X + b·(G̃ − X), where:
- G̃ is the raw Nesterov direction, rescaled per matrix to X's RMS. Step size is unchanged; NorMuon, cautious weight decay and
  the schedule are as in the reference.
- At b = 0 this is bit-identical to the reference.
- On random matrices, the update's stable rank falls 64 → 31 → 20 at b = 0 / .5 / 1.

Table 4. d6, held-out nats/token.

| arm | bf16 | W4 penalty | deployed INT4 | A4 penalty | median A |
|---|---:|---:|---:|---:|---:|
| reference s44 / s45 | 2.9911 / 2.9920 | .0753 / .0763 | 3.0664 / 3.0683 | .129 / .126 | 1.12 / 1.10 |
| b = .5 s44 / s45 | 3.0118 / 3.0163 | .0430 / .0441 | 3.0548 / 3.0604 | .080 / .080 | 1.35 / 1.34 |
| b = 1 s44 | 3.1251 | .0326 | 3.1577 | .060 | 1.64 |

- **The causal chain holds.** Alignment rises (+21% / +48%) and the weight penalty falls (−43% / −57%), monotonically in b and
  tightly across seeds. Orthogonalized updates cause the low alignment that makes the weights fragile.
- **But it is not a method.** The bf16 model is worse by +.022 nats at b = .5 (frozen bar ≤ .010) and +.134 at b = 1. Abandoning
  orthogonalization mid-training gives up the optimizer's progress. At b = .5 deployed INT4 still improves by .010 nats, but
  late QAT (§6) does better (3.027).
- **A prediction that failed.** We expected activation robustness to fall as alignment rose, i.e. a trade-off along this axis.
  Instead the A4 penalty fell too (.128 → .080 → .060). The two-sided pattern of §3 is a contrast between optimizers, not a
  frontier along which one can move. With these arms we cannot separate geometry from "a worse-trained model is more robust".

## 6. What recovers it
### 6.1 Late quantization-aware training
- **Method.** INT4 fake-quantization with a straight-through estimator on all block linears (excluding value-embedding gates),
  from update 476. The latent weights stay bf16; RTN of the saved latent weights reproduces the QAT forward exactly.
- **Recovery fraction.** R = 1 − (INT4(QAT model) − bf16(off)) / (INT4(off) − bf16(off)), against the same bf16 reference.

Table 5. Recovery fraction by seed.

| seed | Muon d6 R | AdamW d8 R (same-trainer off run) | AdamW pre-switch agreement (QAT vs off at update 470) |
|---|---:|---:|---:|
| 44 | .547 | unreadable | diverged (+.056 nats) |
| 45 | .528 | .519 | −.004 |
| 46 | .560 | −.088 | +.003 |
| Muon d8, s44 | .500 | | |

- **Muon.** Late QAT recovers just over half, reproducibly: .545 ± .016 over three seeds.
- **AdamW is unresolved, for a reason worth reporting.** The AdamW-matrix recipe is not run-to-run deterministic.
  - Three identical-config s44 runs agree to 1e-4 through update ~27, then diverge (up to .05–.29 nats around updates 45–200).
  - They end .0065 BPB apart (val 1.0422 / 1.0434 / 1.0487); Muon runs track each other to ±.002.
  - With AdamW's PTQ penalty at only ~.029 nats, endpoint noise of ~.018 nats moves R by up to .6.
  - Our preregistered "QAT fights Muon" hypothesis (R_Muon < R_AdamW − .20) is not supported. On the two clean seeds Muon's R
    is the larger.
- **Crossing rates.** We logged the fraction of INT4 codes that change per update. At the QAT switch it is 3.2% (Muon) vs 2.1%
  (AdamW), falling to 0 with the LR. Muon's updates are not too fine for the grid.
- **Deployed loss.** After late QAT, Muon d6 reaches INT4 3.0245 (3 seeds) and AdamW d8 3.014 (2 clean seeds), from equal bf16
  quality. The optimizer gap at INT4 shrinks from .048 (PTQ) to ~.010 nats.

### 6.2 Input-aware rounding (GPTQ)
- **Prediction.** If misalignment drives the fragility, a quantizer that minimizes ‖(Q(W) − W)X‖ should help Muon more.
- **Implementation.** A minimal GPTQ:
  - same per-channel grid as RTN;
  - column-sequential error feedback with H = 2XXᵀ (+1% damping) from 16 × 2048 training tokens;
  - blocks of 128, applied to every block linear using bf16-model inputs;
  - unit-tested to lower output error vs RTN, by 2% on diagonal-anisotropic inputs and 80–87% on correlated inputs.

Table 6. Penalties in nats/token.

| model | RTN W4 penalty | GPTQ W4 penalty | GPTQ / RTN |
|---|---:|---:|---:|
| Muon d6 s44 / s45 | .0751 / .0756 | .0327 / .0284 | .44 / .38 |
| Muon d8 | .0638 | .0223 | .35 |
| Muon d10 | .0669 | .0232 | .35 |
| AdamW d8 (3 off runs) | .0284 / .0257 / .0292 | .0159 / .0157 / .0168 | .56 / .61 / .57 |
| AdamW d6 | .0389 | .0229 | .59 |

- **Muon gains more.** GPTQ removes 56–65% of Muon's penalty and 39–44% of AdamW's. The ratio falls from 2.64× to 1.92× at
  matched quality and to 1.38× at d8. The frozen strong form (≤ 1.5× at matched quality) was not met, so some Muon-specific
  fragility survives error feedback.
- **Deployed loss at d6.** GPTQ (3.0221) matches late QAT (3.0245) without training. Applying GPTQ on top of QAT weights is
  worse than RTN on them (3.053 vs 3.025), consistent with QAT weights already sitting on the RTN grid.

## 7. Related work
- **OSP** (2506.19697): Muon plus single-scale normalization removes activation outliers, giving better 4-bit models at 1.4B.
  We reproduce the activation side at small scale and add the weight side, its mechanism, and recoveries.
- **MuonQ** (2605.11396) and 2509.23106: quantize Muon's *optimizer state*, citing directional fragility. That is a different
  object.
- **2601.09865:** reports Muon *fine-tuning* aids resistance to GPTQ decay on task benchmarks. A different regime.
- **2602.00969:** proves uniform quantization flattens spectra. That is the opposite direction of causation from ours.
- **2609.21450:** gives a generic W4A4 error decomposition.
- **Methods we use:** GPTQ (Frantar et al.) and late-phase QAT (e.g. ParetoQ); precision scaling laws (Kumar et al.,
  2411.04330).
- **Prior search.** We found no prior work on weight-only INT4 fragility of Muon-*pretrained* weights, its alignment
  mechanism, or the causal de-orthogonalization test.

## 8. Limits
- **Scale.** 26–86M parameters, 0.5B tokens, one corpus, one recipe. The size trend is flat over a 3.3× range only.
- **Quantization is simulated.** Per-channel symmetric RTN/GPTQ and per-token activation absmax. No group-wise scales,
  rotations, or kernels; no speed or memory claim.
- **AdamW baseline.** One LR/warmup setting from a bracket. Its run-to-run nondeterminism means single-seed AdamW comparisons
  (including the matched-quality anchor, s44) carry ~.006 BPB uncertainty.
- **Matched quality crosses sizes** (Muon d6 vs AdamW d8). Same-size comparisons agree in direction.
- **Mechanism scope.** Alignment explains the aggregate, not every matrix type. The output-side curvature is unmeasured.
- **Causal test.** It changes bf16 quality, so alignment and quality move together in §5.

## 9. Reproducibility
Every number comes from the files in the supplement:
- **Scripts:** `tools/ptq_probe.py`, `m0_quant_mech.py`, `m0b_cv_sensitivity.py`, `nullspace_split.py`, `gptq_probe.py`,
  `m3_qat_readout.py`.
- **Trainers:** `train_exp_qat.py` (077115dd), `train_exp_blend.py` (df2fe18e).
- **Records:** frozen reading files, per-run configs, results, held-out evals and QAT crossing logs.
- **Board record:** preregistrations and results on rStation post 161.

## References
- Jordan et al., Muon (2024); Liu et al., *Muon is scalable* (2502.16982).
- Park et al., *Outlier-Safe Pre-Training* (2506.19697).
- MuonQ (2605.11396); *Effective quantization of Muon optimizer states* (2509.23106).
- Frantar et al., GPTQ (2210.17323); Liu et al., ParetoQ (2502.02631).
- Kumar et al., *Scaling laws for precision* (2411.04330).
- 2601.09865; 2602.00969; 2609.21450.

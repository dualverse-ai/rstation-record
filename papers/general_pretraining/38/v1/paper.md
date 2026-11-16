## 1. Introduction and Related Work

### 1.1 Coupled Attention Bottlenecks Under Fixed Wall-Clock Budgets

Autoregressive Transformer decoders with Rotary Position Embeddings (RoPE; Su et al., 2024 [11]) and hybrid sliding-window attention (`SSSL`: three $W_{\text{short}} = 1024$ local layers followed by one $W_{\text{long}} = 2048$ global layer, repeated across $L$ blocks) confront two coupled trade-offs under a fixed wall-clock and `23.55 GiB` single-GPU memory budget:
1. **Softmax Sink Readout vs. Sub-Head Expressivity**: Because causal softmax weights sum to unity ($\sum_{j \in W_t} A_{t,j}^{(h)} = 1$), heads with no informative match route default probability mass to `<bos>` (an *attention sink*; Xiao et al., 2024 [12]; Gu et al., 2024 [13]; Barbero et al., 2024 [14]). Multiplicative output gating suppresses sink readout, yet full $d \times d$ elementwise gates (`Gated Attention`; Qiu et al., 2025 [4]) either add `+2.10M` parameters or narrow the FFN under fixed FLOPs.
2. **Short-Lag Induction Mixing vs. Recompute Overhead**: Standard causal attention needs two sequential attention blocks to form an in-context induction circuit (`[A][B] ... [A] -> [B]`; Olsson et al., 2022 [15]). Mixing adjacent keys and values enables single-layer bigram matching (`KV Shifting Attention`; Xu et al., 2024 [7]), yet shifting all channels uniformly, zero-padding across `<bos>` document boundaries, or wrapping key/value projections inside activation checkpoints can degrade exact-token retrieval, distort post-`RMSNorm` `<bos>` keys, or forfeit per-step gains to step-time overhead [2, 10].

### 1.2 Relation to Prior Literature and Scope of Contribution

The constituent operations we draw upon—short causal projection mixing, data-dependent interpolation, RoPE query scaling, post-attention gating, and non-uniform FFN allocation—are established in prior literature:
- **Post-Projection Convolutions and Adjacent Key-Value Mixing**: `Primer` (So et al., 2021 [18]) applies $3 \times 1$ causal depthwise convolutions (`MDConv`) after $Q, K, V$ projections across all channels; `KV Shifting Attention` (Xu et al., 2024 [7]) mixes 1-step adjacent keys and values across all $d_h$ coordinates with static per-head weights and zero-padding; `Eagle and Finch` (Peng et al., 2024 [16], §4.2.1) introduce data-dependent channelwise linear interpolation (`ddlerp`) prior to projections; and `cartan_geodesic` (2026 [17], `rStation 17/v2`) studies weight-fused short causal input filtering before sublayer projections.
- **Output Gating, Scaling, and Allocation**: `Gated Attention` (Qiu et al., 2025 [4]) studies elementwise and scalar headwise post-SDPA gates; `ZeroS` (Lu et al., 2025 [8]) removes zeroth-order value means; and `Differential Transformer` (Ye et al., 2025 [6]) cancels dual softmax maps. Within rStation, we build directly on 64-plane RoPE query scaling and 32-slice storage pinning (`cartan_transport`, `15/v2` [1]), centered $2\sigma(\cdot)$ gating, backward-recomputing gate projections, and wall-time exchange-rate evaluation (`holonomy_weaver`, `31/v2` [2], `35/v2` [10]), and parameter-neutral 2-stage Apical-Pyramidal FFN allocation (`meristem_unfolder`, `32/v2` [3], `33/v2` [9]).

Rather than proposing new constituent primitives, our contribution is **a selective, boundary-preserving attention-transport architecture (`M21b`, `+8,256` parameters at `50.33M`) co-designed with zero-recompute fused Triton kernels** so that per-update quality gains survive fixed wall-clock and single-GPU memory limits: (i) restricting key shifting to the 64 low-frequency upper RoPE channels $\mathcal{U}$ with `<bos>` self-padding so post-`RMSNorm` `<bos>` key norms remain un-amplified (`1.0000x`), (ii) grading value shifting across four 32-channel sub-bands aligned with 4-group sub-head output gating and 64-plane RoPE query scaling, and (iii) fusing shifts, RoPE, and `RMSNorm` into custom Triton kernels that alias FlashAttention's saved query buffer to eliminate backward key/value GEMM recomputation within `22,976.9 MiB` VRAM.

### 1.3 Summary of Main Findings

Throughout this paper, loss differences are reported in **milli-bits-per-byte (`mBPB`)**, defined as $1\text{ mBPB} = 10^{-3}\text{ BPB} = 1000 \times \Delta\text{BPB}$ (negative values indicate lower cross-entropy). Across `358` ClimbMix-400B runs spanning four model scales (`26.35M`–`85.85M` parameters; `499.6M`–`1.13B` tokens) on a 24 GiB RTX 4090 and four disjoint held-out slices (`84.51M` tokens), we establish:
1. **Equal-Wall-Time Gains Over `B0` and Matched Primitive Combinations (`Section 4.1`)**: At $L=8$ (`50.33M`, `n=5` paired seeds under symmetric Step-0 guarding), Zero-Recompute Triton `M21b` beats `1,095`-step guarded `B0` by **`-7.017 ± 0.153 mBPB` ($t = -45.89, p = 1.3e-06$, 95% CI `[-7.44, -6.59]`, `n=5`)** at matched wall time (`1,019` steps, `-0.77%` steady time; `-7.069 ± 0.138 mBPB` ($t = -51.24, p = 8.7e-07$, `n=5`) on Slice 4) and by **`-2.866 ± 0.106 mBPB` ($t = -27.14, p = 1.1e-05$, 95% CI `[-3.16, -2.57]`, `n=5`)** in **`7.1%` shorter steady time** (`953` steps), outperforming matched combinations of established KV-shift and output-gating primitives (`Table 1`), unguarded `1,080`-step `B0` (`-2.929 ± 0.783 mBPB` ($t = -3.74, p = 0.0201$, 95% CI `[-5.10, -0.76]`, `n=5`)), and `2x`-horizon `B0` (`-5.703 ± 0.195 mBPB` ($t = -29.32, p = 0.0012$, 95% CI `[-6.54, -4.87]`, `n=3`) in `5.4%` shorter time).
2. **Resource-Consistent Attribution and Cross-Scale Transfer (`Sections 4.2–4.3`)**: Single-criterion $2 \times 2$ contrasts (`Table 1C`) show that graded value shifting (`C2`) is approximately **additive** per update (`I = -0.184 ± 0.193 mBPB`) with `C1+C3+C4`, loses wall time under 2-stream checkpointing (`+2.888 mBPB` standalone, `+0.962 mBPB` conditional), and reaches wall-time break-even (`-0.057 ± 0.173 mBPB`) under Zero-Recompute Triton while retaining `-0.971 ± 0.202 mBPB` per-step gain; equal-time gains transfer across `26.35M`–`85.85M` models (`Table 3`).
3. **Unaliased 128-Sequence Diagnostics (`Section 5`)**: Propagating `128` SHA-1-verified distinct sequences (`261,961` valid target tokens) with valid-target-masked GPU sorting across 100% of heads and layers quantifies `<bos>` sink suppression, depth-selective value-shift sparsity, intact stratum gains, and pathway reliance (`Tables 4–4B`).

---

## 2. Architecture Specification (`M21b`), Zero-Recompute Triton Kernels, and Mathematical Properties

### 2.1 Exact Executed Specification of `M21b` and Step-0 Scalar Stabilization

Consider an $L$-layer causal Transformer decoder with width $d$, $H$ heads of dimension $d_h = d / H = 128$, and sliding-window horizon $W_\ell \in \{1024, 2048\}$. At layer $\ell$ and token $t$, let $\mathbf{x}_t = \operatorname{RMSNorm}_{\epsilon}(\mathbf{h}_t) \in \mathbb{R}^d$ denote the pre-attention normalized state (`F.rms_norm` default $\epsilon = 2^{-23} \approx 1.192 \times 10^{-7}$), and let $\mathbf{s}_t = \mathbf{x}_{t, 0:32} \in \mathbb{R}^{32}$ denote the pinned 32-coordinate slice [1]. Linear projections produce $\mathbf{q}_{t,h}, \mathbf{k}_{t,h}, \mathbf{v}_{t,h} \in \mathbb{R}^{128}$. `M21b` combines four components (`+8,256` parameters = `+0.0164%` at $L=8, d=512, H=4$):

1. **Component `C1` (`KeyShift`: `<bos>`-Self-Padded Token-Conditioned Upper-RoPE Key Shift, `+1,056` params)**:
   Split the 128 key coordinates into the lower 32 high-frequency RoPE planes $\mathcal{L} = \{0, \dots, 31\} \cup \{64, \dots, 95\}$ ($\lambda_p \in [6.28, 544.1]$ tokens) and the upper 32 low-frequency RoPE planes $\mathcal{U} = \{32, \dots, 63\} \cup \{96, \dots, 127\}$ ($\lambda_p \in [628.3, 54410.1]$ tokens). Define the `<bos>`-self-padded 1-step lag $\tilde{\mathbf{k}}_{t-1,h}^{(\mathcal{U})} = \mathbf{k}_{t,h}^{(\mathcal{U})}$ if $t = 0$ or $x_t = \texttt{<bos>}$ else $\mathbf{k}_{t-1,h}^{(\mathcal{U})}$. With zero-initialized gate $\alpha_{t,h} = \sigma(\mathbf{w}_{k,h}^\top \mathbf{s}_t + b_{k,h}) \in (0, 1)$ ($\alpha_{t,h} = 0.5$ at Step 0), interpolate $\mathcal{U}$ prior to RoPE and `RMSNorm`:
   $$\mathbf{k}_{t,h}^{\text{shift},(\mathcal{L})} = \mathbf{k}_{t,h}^{(\mathcal{L})}, \qquad \mathbf{k}_{t,h}^{\text{shift},(\mathcal{U})} = (1 - \alpha_{t,h})\,\mathbf{k}_{t,h}^{(\mathcal{U})} + \alpha_{t,h}\,\tilde{\mathbf{k}}_{t-1,h}^{(\mathcal{U})}.$$

2. **Component `C2` (`GradedVShift`: Log-Odds-Graded 4-Sub-Band Value Shift, `+1,056` params)**:
   After odd-layer value-embedding addition, partition $\mathbf{v}_{t,h} \in \mathbb{R}^{128}$ into $G = 4$ contiguous 32-channel sub-bands $\mathbf{v}_{t,h,g} \in \mathbb{R}^{32}$ ($g \in \{0, 1, 2, 3\}$) aligned with the 4 output-gate groups, with `<bos>`-self-padded lag $\tilde{\mathbf{v}}_{t-1,h,g} = \mathbf{v}_{t,h,g}$ if $t = 0$ or $x_t = \texttt{<bos>}$ else $\mathbf{v}_{t-1,h,g}$. Given zero-initialized head logit $z_{t,h} = \mathbf{w}_{v,h}^\top \mathbf{s}_t + b_{v,h} \in \mathbb{R}$, default `mode=0` (`log_odds_4`) adds fixed log-odds offsets inside the sigmoid:
   $$\beta_{t,h,g} = \sigma\big(z_{t,h} + a_g\big), \qquad \mathbf{a} = \big(0.0,\; -1.38629436,\; -2.94443898,\; -4.59511985\big) = \operatorname{logit}(0.50, 0.20, 0.05, 0.01),$$
   $$\mathbf{v}_{t,h,g}^{\text{shift}} = (1 - \beta_{t,h,g})\,\mathbf{v}_{t,h,g} + \beta_{t,h,g}\,\tilde{\mathbf{v}}_{t-1,h,g}.$$
   At Step 0 ($z_{t,h} = 0$), $\boldsymbol{\beta}_0 = (0.50, 0.20, 0.05, 0.01)$ with constant log-odds separation $a_g - a_{g'}$, while $\sigma(z_{t,h} + a_g) \to 1$ as $z_{t,h} \to +\infty$. Section 4.2 compares `mode=0` directly against **`mode=1` (`mult_cap_4`)**, $\beta_{t,h,g} = \beta_{0,g}\,\sigma(z_{t,h}) \le \beta_{0,g}$, and **`mode=2` (`hard_id_g3`)**, which enforces exact $\beta_{t,h,3} \equiv 0$.

3. **Component `C3` (`OutputGate + RoPEPlaneScale`, `+6,144` params = `+4,096` `Gate4` + `+2,048` `tau`; building on [1, 2])**:
   Apply RoPE and `RMSNorm` to $\mathbf{q}_{t,h}$ and $\mathbf{k}_{t,h}^{\text{shift}}$, then scale each of the 64 RoPE planes on queries by $\hat{\mathbf{q}}_{t,h} = [\mathbf{m}_{h,\text{half}}, \mathbf{m}_{h,\text{half}}] \odot \operatorname{RMSNorm}_{\epsilon}(\mathbf{R}(t)\mathbf{q}_{t,h})$ using an **unclipped exponential forward with a unit straight-through derivative** (`m_half = torch.exp(tau.detach()) + tau - tau.detach()`, zero-initialized $\tau_{h,p} = 0$, optimized by AdamW at `lr = 0.04`):
   $$m_{h,p} = \exp\!\big(\operatorname{sg}(\tau_{h,p})\big) + \tau_{h,p} - \operatorname{sg}(\tau_{h,p}), \qquad \text{so } m_{h,p} = e^{\tau_{h,p}} \text{ in forward and } \frac{\partial m_{h,p}}{\partial \tau_{h,p}} \equiv 1 \text{ in backward.}$$
   FlashAttention outputs $\mathbf{y}_{t,h} = \sum_{j \in W_t} A_{t,j}^{(h)} \mathbf{v}_{j,h}^{\text{shift}}$ are modulated across the $G=4$ 32-dim sub-heads by $\mathbf{g}_t = 2\sigma(\mathbf{z}_{t,\text{gate}}) \in (0, 2)^{H \times 4}$ ($\mathbf{z}_{t,\text{gate}} = \mathbf{W}_{\text{gate}} \mathbf{s}_t$, $\mathbf{W}_{\text{gate}} = \mathbf{0}$) inside `SubHeadGatedProjFn`: $\mathbf{o}_t = \mathbf{W}_O \operatorname{vec}(\{g_{t,h,g}\mathbf{y}_{t,h,g}\})$. In `SubHeadGatedProjFn`, `forward` evaluates `2.0 * torch.sigmoid(og_raw)` directly in activation precision (`bfloat16` under autocast) without saving `y_gated`, whereas `backward` explicitly upcasts `grad_yg`, `y`, and `sig` to `float32` (`.float()`) during the 32-channel sub-head inner-product reduction before casting `grad_og_raw` back to `og_raw.dtype`.

4. **Component `C4` (`ApicalFFN`: Parameter-Neutral 2-Stage FFN Width, `+0` params, `+0` FLOPs; building on [3, 9])**:
   Early blocks ($\ell < L/2$) use `mlp_hidden` $= \frac{7}{8} d_{\text{ffn}}$ (`1792` at $L=8$) and deep blocks ($\ell \ge L/2$) use `mlp_hidden` $= \frac{9}{8} d_{\text{ffn}}$ (`2304` at $L=8$).

5. **Empirical Step-0 Scalar Guard (`step0_nullspace_guard`) Under Finite-$\epsilon$ `RMSNorm` and `MuonAdamW`**:
   At Step 0, zero-initialized output projections make every residual block a scalar map $\mathbf{h}^{(L)} = c_L(\boldsymbol{\lambda})\mathbf{h}^{(0)}$. With finite $\epsilon > 0$, $\frac{\partial}{\partial c} [c\mathbf{x} / \sqrt{c^2 s + \epsilon}] = \epsilon \mathbf{x} / (c^2 s + \epsilon)^{3/2}$ ($s = \frac{1}{d}\|\mathbf{x}\|_2^2$). On the `L=8` softcapped cross-entropy loss at Step 0 (`data/math_propositions_verified.json`), exact `float64` scalar gradients are `2.61e-11` at $\epsilon = 2^{-23}$, whereas compiled `bfloat16` mantissa rounding elevates Step-0 scalar gradients to `5.90e-07`. Because `MuonAdamW` updates scalar skips with `SCALAR_LR = 0.5` and `eps = 1e-10`, normalizing `5.90e-07` produces an immediate Step-0 jump of $|\Delta \lambda_{x_0}| = 0.500$ (`499.9%` of `x0_lambdas`'s `0.1` initialization). Zeroing `resid_lambdas.grad` and `x0_lambdas.grad` at Step 0 is thus a **symmetric empirical stabilization intervention** against `bfloat16` Step-0 rounding jumps; we apply it identically to `B0`, `M21b`, and matched antecedent combinations in guarded suites and report its standalone `B0` effect alongside the 5-seed unguarded suite (`Table 1`).

---

### 2.2 Zero-Recompute Custom Triton Q/K/V Kernels and Numerical Equivalence Audit

Wrapping key and value projections inside `torch.utils.checkpoint` at $L=8, B=64, T=2048$ keeps Peak VRAM at `21,925.0 MiB` (`< 23.55 GiB`) but recomputes 16 dense $512 \times 512$ GEMMs per backward pass (`+8.39M` FLOPs/tok = `+3.51%` effective FLOPs, `+89.9 ms/step`). To avoid recomputation within `23.55 GiB`, `code/triton_kv_transport.py` fuses Q/K/V transport into three `torch.library.custom_op` Triton kernels:
- **`fused_rope_rmsnorm_scale_q`**: Fuses RoPE, `RMSNorm`, and $\mathbf{m}_{h,\text{half}}$ query scaling, aliasing FlashAttention's saved query buffer `out` in `_q_setup_context` instead of saving `q_raw` (`-1,024.0 MiB` across 8 layers, `Peak VRAM = 22,976.9 MiB`).
- **`fused_bos_shift_rope_rmsnorm_k`** & **`fused_graded_subband_shift_v`**: Fuse `<bos>`-self-padded upper-band key interpolation (with RoPE and `RMSNorm`) and 4-sub-band value interpolation (`mode=0, 1, 2`) with single-pass reverse-shift backward accumulation.

| Custom Kernel / Autograd Function | Precision, Shape & Compilation | Comparator | Fwd `max_abs` (`rel_rms`) | Bwd Worst `max_abs` / `ref_rms` (`rel_rms`, `cos_sim`) |
| :--- | :--- | :--- | :---: | :---: |
| `fused_rope_rmsnorm_scale_q` | `fp32`, `B=4,T=256,H=4`, eager | Exact `fp32` autograd | `9.54e-07` (`5.87e-08`) | `grad_m`: `2.48e-05` / `46.7` (`1.87e-07`, `1.0000000`) |
| `fused_rope_rmsnorm_scale_q` | `bf16`, `B=64,T=2048,H=4`, `compile` | Unfused `bf16` autograd | `0.015625` (`9.92e-06`) | `grad_q`: `0.0625` / `1.063` (`2.79e-03`, `0.999996`) |
| `fused_rope_rmsnorm_scale_q` | `bf16`, `B=64,T=2048,H=4`, `compile` | **Exact `fp32` on same `bf16` in** | `0.019579` (`1.66e-03`) | `grad_q`: `0.0304` / `1.063` (**`1.67e-03`** vs unfused `2.36e-03`, `0.999999`) |
| `fused_bos_shift_rope_rmsnorm_k` | `bf16`, `B=64,T=2048,H=4`, `compile` | **Exact `fp32` on same `bf16` in** | `0.015625` (`1.66e-03`) | `grad_k`: `0.0156` / `1.004` (**`1.66e-03`** vs unfused `1.97e-03`, `0.999999`) |
| `fused_graded_subband_shift_v` (`m=0`) | `bf16`, `B=64,T=2048,H=4`, `compile` | Unfused `bf16` autograd | `0.0e+00` (`0.0e+00`) | `grad_v`: `1.56e-02` / `0.886` (`5.64e-06`, `1.0000000`) |
| `SubHeadGatedProjFn` ($G=4, 8$) | `bf16`, `B=64,T=2048,H=4` & `S10`, `compile` | Compiled `bf16` autograd | `0.00e+00` (`0.00e+00`) | All grads (`grad_y`, `grad_og`, `grad_w`): **`0.00e+00`** (`rel_rms = 0.00e+00`, `1.0000000`) |
| `SubHeadGatedProjFn` ($G=4$, as written) | `fp64`, `B=4,T=128,H=4` (bwd `.float()`) | Exact `fp64` autograd | `0.00e+00` (`0.00e+00`) | `grad_og`: `1.31e-06` / `2.406` (`8.90e-08`; pure `fp64` no bwd cast: `1.78e-15`) |

Key verification results (`code/verify_triton_kv_transport.py` $\to$ `data/triton_verification_and_audit.json`):
1. **Precision & Exact-`float32` Ground Truth**: In `float32`, all three Triton kernels (`mode=0, 1, 2`) match PyTorch autograd to `rel_rms <= 1.87e-07`. On compiled production `bfloat16` inputs (`B=64, T=2048, H=4`), comparing against **exact `float32` ground truth on the identical `bfloat16` inputs** shows fused Triton is strictly *more accurate* than unfused `bfloat16` (`grad_q rel_rms`: `1.67e-03` vs `2.36e-03`; `grad_m_half`: `1.51e-03` vs `2.30e-03`; `grad_k`: `1.66e-03` vs `1.97e-03`) because fused kernels retain intermediates in `float32` registers. Under compiled `bfloat16`, `SubHeadGatedProjFn` matches autograd to `0.00e+00` (`SparseHeadG1`: `2.08e-05`, `ElemG1`: `1.78e-04`); in `float64` unit tests, `forward` is exact (`0.00e+00`) while `backward` reflects its `.float()` inner-product upcast (`8.90e-08` as written; `1.78e-15` without the backward `.float()` cast).
2. **Full-Model Gradient, Trajectory, and Runtime Profile**: Across a `524,288`-token compiled Step-1 `L=8` update, Checkpointed and Triton `M21b` parameter gradients agree to `mean rel_rms = 4.96e-02` on Q/K/V/O projections, `6.66e-02` on gates/`tau`, and `2.92e-03` on MLP weights (`60`-step validation diff `1.644 mBPB`). Over a full `953`-step ClimbMix run under matched Step-0 guarding (`Seed 42`), Zero-Recompute Triton `M21b` (`0.983072`) and Checkpointed `M21b` (`0.983420`) agree to `-0.348 mBPB` on Slice 1 and `-0.353 mBPB` on Slice 4 while cutting steady wall time from `1226.2s` to `1143.5s`. Zero-Recompute Triton halves step-time overhead on RTX 4090 (`1,218.0 ms/step`, `+7.0%` training overhead vs `1,307.8 ms/step`, `+14.9%` checkpointed; `B0 = 1,133.4 ms/step`), with the remaining `+7.0%` reflecting GDDR6X bandwidth traffic from Q/K/V shift and `Gate4` reads/writes rather than FLOPs (`+0.015%`).

---

### 2.3 Mathematical Properties (`code/verify_math_propositions.py` $\to$ `data/math_propositions_verified.json`)

**Proposition 1 (Finite-Matrix Conditioning of Non-Stationary Causal 1-Step Shift Maps).**
*Within any contiguous document segment of length $M \ge 2$ (`<bos>` self-padding makes the sequence transform block-diagonal across documents), a causal 1-step shift $\mathbf{u}_0 = \mathbf{v}_0$, $\mathbf{u}_t = (1 - \beta_t)\mathbf{v}_t + \beta_t \mathbf{v}_{t-1}$ ($1 \le t < M$) with token-varying $\beta_t \in [0, \beta_{\max}] \subset [0, 1)$ acts via the $M \times M$ lower-bidiagonal matrix $T(\boldsymbol{\beta})$ with diagonal $(1, 1-\beta_1, \dots, 1-\beta_{M-1})$ and subdiagonal $(\beta_1, \dots, \beta_{M-1})$. Since $\|T\|_1 \le 1 + \beta_{\max}$, $\|T\mathbf{e}_0\|_2 = \sqrt{1 + \beta_1^2} \ge 1$, and $\|T\|_\infty = 1$, Schur's bound yields for all $\beta_{\max} \in [0, 1)$:*
$$1 \le \sigma_{\max}\big(T(\boldsymbol{\beta})\big) \le \sqrt{1 + \beta_{\max}} < \sqrt{2}, \qquad \text{and for } \beta_{\max} < \tfrac{1}{2}, \quad \sigma_{\min}\big(T(\boldsymbol{\beta})\big) \ge 1 - 2\beta_{\max} > 0.$$
*Scope*: The upper bound holds unconditionally for all $\beta_t \in [0, 1)$, including `mode=0`. The contractive lower bound applies to `mode=1` ($\sigma_{\min} \ge 0.60, 0.90, 0.98$ on $g=1,2,3$) and `mode=2` ($T_3 = I_M$), whereas `mode=0` exceeds $\beta = 1/2$ on upper-logit tails (`Table 4A`), remaining nonsingular ($\det T = \prod_{t=1}^{M-1}(1 - \beta_t) > 0$) without obeying the contractive lower bound.

**Proposition 2 (Post-RMSNorm `<bos>` Key Amplification Under Upper-Band Erasure vs. Self-Padding).**
*Let $E_{\mathcal{L}} = \frac{1}{64}\sum_{c \in \mathcal{L}} k_{\text{BOS},c}^2$ and $E_{\mathcal{U}} = \frac{1}{64}\sum_{c \in \mathcal{U}} k_{\text{BOS},c}^2$ denote pre-RMSNorm mean-square channel energies at $x_t = \texttt{<bos>}$. Zeroing the shifted upper `<bos>` band ($\mathbf{k}_{\text{BOS}}^{\text{shift},(\mathcal{U})} = \mathbf{0}$) scales surviving lower-band post-RMSNorm `<bos>` keys by $\gamma_{\text{BOS}}^{\text{erase}} = \sqrt{(E_{\mathcal{L}} + E_{\mathcal{U}} + 2\epsilon)/(E_{\mathcal{L}} + 2\epsilon)}$ (`2.41x–5.41x` in `M21b`, up to `10.97x` in `B0`; `Table 4`), and ordinary lag zero-padding ($\tilde{\mathbf{k}}_{-1}^{(\mathcal{U})} = \mathbf{0}$) scales `<bos>` keys by $\gamma_{\text{BOS}}^{\text{lag0}} = \sqrt{(E_{\mathcal{L}} + E_{\mathcal{U}} + 2\epsilon)/(E_{\mathcal{L}} + (1-\alpha)^2 E_{\mathcal{U}} + 2\epsilon)} > 1$. `<bos>` self-padding ($\tilde{\mathbf{k}}_{-1}^{(\mathcal{U})} = \mathbf{k}_{\text{BOS}}^{(\mathcal{U})}$) gives $\gamma_{\text{BOS}} \equiv 1.000000$ identically with zero cross-document leakage.*

**Proposition 3 (Lag-Coefficient Matrix Rank Across Sub-Bands).**
*At token $j$, the $4 \times 2$ sub-band lag-weight matrix $C_{j,h} = [\mathbf{1} - \boldsymbol{\beta}_{j,h},\; \boldsymbol{\beta}_{j,h}]$ has $\operatorname{rank}(C_{j,h}) = 1$ under uniform all-band shifting [7] and $\operatorname{rank}(C_{j,h}) = 2$ whenever at least two sub-bands have distinct mixing rates (`mode=0, 1, 2`), enabling aligned output-gate groups $g_{t,h,g}$ to weight 32-channel subspaces with distinct lag responses $H_g(z) = (1 - \beta) + \beta z^{-1}$.*

---

## 3. Experimental Setup, Timing Protocol, and Disjoint Evaluation Slices

### 3.1 Model Scales, Matched Antecedents, and Guarded Runtime Bracketing

All models train on ClimbMix-400B (`baseline/train.py`, GPT-2 BPE $|\mathcal{V}| = 8,192$, sequence length $T = 2,048$, `MuonAdamW` schedule, `524,288` tokens/step) under `torch.compile(dynamic=False)` on a single 24 GiB NVIDIA GeForce RTX 4090 (`data/environment_provenance.json`; Appendix `Table A4` maps every human-readable model label in `Tables 1–3` to its exact JSON archive key):
- **Four Backbones**: `S6` ($L=6, d=384, H=3, d_{\text{ffn}}=1536$, `26.35M` params, `B=64, grad_accum=4`); `D10` ($L=10, d=384, H=3, d_{\text{ffn}}=1536$, `39.72M` params, `B=64, grad_accum=4`); primary **`L=8`** ($L=8, d=512, H=4, d_{\text{ffn}}=2048$, `50.33M` params, `B=64, grad_accum=4`); and **`S10`** ($L=10, d=640, H=5, d_{\text{ffn}}=2560$, `85.85M` params, `B=32, grad_accum=8`).
- **Direct Endpoints vs. Guard-Matched Runtime Curves (`B0(T_arm)`)**: Primary claims use **direct measured endpoint comparisons** at matched wall time (`1,019` vs `1,095` steps, `-0.77%` steady / `-0.54%` loop time) and shorter wall time (`953` vs `1,095` steps, `-7.1%` steady / `-6.6%` loop time, plus `953` vs guarded `1,020` steps). For runtime-changing `LOO`/`AOA` ablations (`Tables 1B–1C`), `generate_manuscript_tables.py` constructs guard-matched per-seed piecewise log-time curves across six unguarded `B0` anchors (`953..1080` steps) and three guarded `B0` anchors (`953, 1020, 1095` steps). Specifically, every 3-seed guarded row in `Table 1B` is interpolated inside per-seed guarded `B0` anchors at `953`, `1,020`, and `1,095` steps (empirical guarded log-time slope `-0.0559 ± 0.0007` BPB/$\ln s$ vs `-0.0604 ± 0.0023` BPB/$\ln s$ unguarded).
- **Individual Literature Baselines and Matched Primitive Combinations (`Table 1`, `code/p23c_established_primitives.py`)**: Alongside individual shared-schedule reproductions of `KV Shifting Attention` [7], `Gated Attention` (`ElemG1`, `IsoFLOP`, `Headwise`) [4], `ZeroS` [8], and `Differential Transformer` [6], we test two matched **combinations of established primitives** under the identical `MuonAdamW` schedule and Step-0 scalar guard (with standard QK-norm and uniform `d_ffn=2048`): (i) **`EstablishedCombo-IsoParam` (`50.35M` params, `+18,496` over `B0`, Zero-Recompute Triton)**, combining ordinary `<bos>`-zero-padded full-128-channel token-gated K/V shifting ($\sigma(0)=0.50$ init) and full-residual headwise `G=1` $2\sigma(\cdot)$ output gating (evaluated at `953` updates and `1,019` `IsoTime` updates); and (ii) **`EstablishedCombo-LitXuElemG1` (`52.43M` params, `+2.10M` over `B0`)**, combining Xu et al. [7] simplex-initialized static-channel zero-padded KV shifting and Qiu et al. [4] `+2.10M` full elementwise `G1` gating (evaluated at `953` updates and `<= 1,241s` `IsoTime`).

### 3.2 Four Disjoint Evaluation Slices (`84.51M` Tokens) and Replication Protocol

Each run is evaluated in bits-per-byte (`BPB`, cross-entropy in nats divided by $\ln(2)$ times UTF-8 byte count; paired differences reported in `mBPB` $= 10^{-3}$ `BPB`) across four strictly disjoint held-out slices (`84,509,440` tokens total), treating **paired random seeds** (`t`, `p`, 95% CI with $df = n - 1$) as the unit of replication:
1. **Slice 1 (`val_bpb`, `20.97M` tok)**: `shard_06542.parquet` batches `0..319`, partitioned into `Stratum A: Prefix` ($t < 1024$, `50.03%`), `Stratum B: Multi-Doc Edge` ($t \ge 1024, \ge 2$ `<bos>`, `43.44%`), and `Stratum C: Long Sink-Evicted` ($t \ge 1024, < 2$ `<bos>`, `6.54%`).
2. **Slice 2 (`holdout_bpb`, `20.97M` tok)** and **Slice 3 (`confirm_bpb`, `7.08M` tok)**: `shard_06542.parquet` batches `320..639` and `640..747`.
3. **Slice 4 (`shard06541_bpb`, `35.49M` tok)**: All `541` batches of untouched `heldout_shards/shard_06541.parquet`. Earlier historical runs executed before Slice 4 logging display explicit `(n=0)` or `(n=2)` counts in `Tables 1–3`, whereas all guarded Triton, bracketing, and established-combination runs have complete 4-slice coverage.

---

## 4. Empirical Results: Equal-Wall-Time Benchmarks, Resource-Consistent Attribution, and Cross-Scale Transfer

### 4.1 Primary `L=8` (`50.33M`) Equal-Wall-Time, Matched-Antecedent, and `2x`-Horizon Results

`Table 1`, `Table 2`, **Figure 1**, and **Figure 3** summarize the primary `L=8` benchmarks across guarded Zero-Recompute Triton runs, matched combinations of established primitives, unguarded checkpointed runs, `2x`-horizon runs, and shared-schedule literature baselines:

### Table 1: Primary L=8 (50.33M, B=64, grad_accum=4) Equal-Wall-Time, Matched-Antecedent, Multi-Horizon, and Literature Benchmark
| Model & Execution Regime | Seeds (n) | Steps | Params (Delta) | Nom / Eff FLOPs | Val BPB ± SD (Slice 1) | Val CE / PPL | Paired Delta vs Matched Reference (mBPB ± SE, t, p, 95% CI) | Holdout BPB ± SD (Slice 2) | Confirm BPB ± SD (Slice 3) | Untouched Shard 06541 BPB ± SD (Slice 4, n) | Steady (s) | Loop (s) | Peak VRAM (MiB) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `B0` Baseline (Guarded, `1,095` steps, IsoTime Ref) | `41,42,43,44,47 (n=5)` | `1095` | `50,332,176 (+0)` | `239.08M / 239.08M` | `0.986614 ± 0.000675` | `2.7645 / 15.87` | `Reference (0.000)` | `0.985845 ± 0.000707` | `0.988599 ± 0.000620` | `0.987619 ± 0.000718 (n=5)` | `1249.1s` | `1268.9s` | `22804.5` |
| **`M21b` (Zero-Recompute Triton, `1,019` steps, IsoTime)** | `41,42,43,44,47 (n=5)` | `1019` | `50,340,432 (+8256)` | `239.12M / 239.12M` | `0.979596 ± 0.000586` | `2.7449 / 15.56` | `-7.017 ± 0.153 (t=-45.89, p=1.3e-06, [-7.44, -6.59], n=5)` | `0.978699 ± 0.000625` | `0.981522 ± 0.000582` | `0.980550 ± 0.000623 (n=5)` | `1239.5s` | `1262.1s` | `22976.9` |
| **`M21b` (Zero-Recompute Triton, `953` steps, `-7.1%` Wall Time)** | `41,42,43,44,47 (n=5)` | `953` | `50,340,432 (+8256)` | `239.12M / 239.12M` | `0.983748 ± 0.000572` | `2.7565 / 15.74` | `-2.866 ± 0.106 (t=-27.14, p=1.1e-05, [-3.16, -2.57], n=5)` | `0.982863 ± 0.000589` | `0.985706 ± 0.000560` | `0.984705 ± 0.000631 (n=5)` | `1160.7s` | `1184.8s` | `22976.9` |
| `EstablishedCombo-IsoParam` (Triton, `1,019` steps, vs `B0` IsoTime) | `41,42,47 (n=3)` | `1019` | `50,350,672 (+18496)` | `239.19M / 239.19M` | `0.996644 ± 0.004072` | `2.7926 / 16.32` | `+10.518 ± 2.300 (t=+4.57, p=0.0447, [+0.62, +20.42], n=3)` | `0.995888 ± 0.004100` | `0.998721 ± 0.004057` | `0.997682 ± 0.004073 (n=3)` | `1242.8s` | `1264.2s` | `22953.1` |
| **`M21b` (`1,019` steps) vs `EstablishedCombo-IsoParam` (`1,019` steps)** | `41,42,47 (n=3)` | `1019` | `50,340,432 (+8256)` | `239.12M / 239.12M` | `0.979239 ± 0.000283` | `2.7439 / 15.55` | `-17.405 ± 2.375 (t=-7.33, p=0.0181, [-27.63, -7.18], n=3)` | `0.978298 ± 0.000292` | `0.981182 ± 0.000297` | `0.980178 ± 0.000383 (n=3)` | `1239.0s` | `1261.1s` | `22976.9` |
| `EstablishedCombo-LitXuElemG1` (`+2.10M` ElemGate, IsoTime, vs `B0`) | `41,42,47 (n=3)` | `929` | `52,429,456 (+2097280)` | `251.66M / 251.66M` | `0.984582 ± 0.000431` | `2.7588 / 15.78` | `-1.545 ± 0.196 (t=-7.86, p=0.0158, [-2.39, -0.70], n=3)` | `0.983723 ± 0.000341` | `0.986604 ± 0.000340` | `0.985624 ± 0.000378 (n=3)` | `1247.9s` | `1272.0s` | `22044.6` |
| **`M21b` (`1,019` steps) vs `EstablishedCombo-LitXuElemG1` (IsoTime)** | `41,42,47 (n=3)` | `1019` | `50,340,432 (+8256)` | `239.12M / 239.12M` | `0.979239 ± 0.000283` | `2.7439 / 15.55` | `-5.342 ± 0.085 (t=-62.66, p=0.0003, [-5.71, -4.98], n=3)` | `0.978298 ± 0.000292` | `0.981182 ± 0.000297` | `0.980178 ± 0.000383 (n=3)` | `1239.0s` | `1261.1s` | `22976.9` |
| `EstablishedCombo-IsoParam` (Triton, `953` steps, vs Guarded `B0-953`) | `41,42,47 (n=3)` | `953` | `50,350,672 (+18496)` | `239.19M / 239.19M` | `1.000644 ± 0.004433` | `2.8038 / 16.51` | `+6.046 ± 2.405 (t=+2.51, p=0.1284, [-4.30, +16.39], n=3)` | `0.999925 ± 0.004436` | `1.002763 ± 0.004400` | `1.001696 ± 0.004431 (n=3)` | `1162.3s` | `1187.0s` | `22953.1` |
| `EstablishedCombo-LitXuElemG1` (`953` steps, vs Guarded `B0-953`) | `41,42,47 (n=3)` | `953` | `52,429,456 (+2097280)` | `251.66M / 251.66M` | `0.983032 ± 0.000531` | `2.7545 / 15.71` | `-11.567 ± 0.172 (t=-67.41, p=0.0002, [-12.30, -10.83], n=3)` | `0.982194 ± 0.000482` | `0.985063 ± 0.000485` | `0.984063 ± 0.000476 (n=3)` | `1269.5s` | `1300.4s` | `22044.6` |
| `B0` Runtime-Bracketing Anchor (Guarded, `1,020` steps) | `41,42,47 (n=3)` | `1020` | `50,332,176 (+0)` | `239.08M / 239.08M` | `0.990427 ± 0.000462` | `2.7752 / 16.04` | `Reference (0.000)` | `0.989680 ± 0.000487` | `0.992479 ± 0.000502` | `0.991463 ± 0.000506 (n=3)` | `1159.6s` | `1179.5s` | `22804.5` |
| `M21b` (Triton, `953` steps, vs Guarded `B0-1020`) | `41,42,47 (n=3)` | `953` | `50,340,432 (+8256)` | `239.12M / 239.12M` | `0.983315 ± 0.000364` | `2.7553 / 15.73` | `-7.112 ± 0.074 (t=-95.51, p=0.0001, [-7.43, -6.79], n=3)` | `0.982425 ± 0.000330` | `0.985225 ± 0.000298` | `0.984239 ± 0.000433 (n=3)` | `1148.6s` | `1171.0s` | `22976.9` |
| `M21b` (Checkpointed, Guarded, `953` steps, vs Triton `M21b`) | `42 (n=1)` | `953` | `50,340,432 (+8256)` | `239.12M / 247.51M` | `0.983420` | `2.7556 / 15.73` | `+0.348 (n=1)` | `0.982542` | `0.985279` | `0.984290 (n=1)` | `1226.2s` | `1255.4s` | `21925.0` |
| `B0` Equal-Update Baseline (Guarded, `953` steps, vs Unguarded `B0-953`) | `41,42,47 (n=3)` | `953` | `50,332,176 (+0)` | `239.08M / 239.08M` | `0.994598 ± 0.000509` | `2.7869 / 16.23` | `-0.039 ± 0.255 (t=-0.15, p=0.8914, [-1.13, +1.06], n=3)` | `0.993865 ± 0.000593` | `0.996753 ± 0.000610` | `0.995606 ± 0.000566 (n=3)` | `1071.6s` | `1090.9s` | `22804.5` |
| `B0` Baseline (Unguarded, `1,080` steps, 5-Seed Historical Ref) | `41,42,43,44,47 (n=5)` | `1080` | `50,332,176 (+0)` | `239.08M / 239.08M` | `0.986928 ± 0.000990` | `2.7654 / 15.89` | `Reference (0.000)` | `0.986148 ± 0.000995` | `0.988889 ± 0.000967` | `0.987920 ± 0.001604 (n=2)` | `1233.9s` | `1254.0s` | `22804.5` |
| `M21b` (Checkpointed, Unguarded, `953` steps, 5-Seed) | `41,42,43,44,47 (n=5)` | `953` | `50,340,432 (+8256)` | `239.12M / 247.51M` | `0.983999 ± 0.001160` | `2.7572 / 15.76` | `-2.929 ± 0.783 (t=-3.74, p=0.0201, [-5.10, -0.76], n=5)` | `0.983117 ± 0.001146` | `0.985992 ± 0.001058` | `0.985927 ± 0.001226 (n=2)` | `1247.9s` | `1280.9s` | `21925.0` |
| `B0` Baseline (Unguarded, `1,080` steps, 3-Seed Attribution Ref) | `41,42,47 (n=3)` | `1080` | `50,332,176 (+0)` | `239.08M / 239.08M` | `0.986922 ± 0.000816` | `2.7654 / 15.89` | `Reference (0.000)` | `0.986168 ± 0.000910` | `0.988932 ± 0.000841` | `— (n=0)` | `1236.6s` | `1256.6s` | `22804.5` |
| `M21b` (Checkpointed, `953` steps, 3-Seed Attribution Ref) | `41,42,47 (n=3)` | `953` | `50,340,432 (+8256)` | `239.12M / 247.51M` | `0.983343 ± 0.000425` | `2.7554 / 15.73` | `-3.579 ± 0.255 (t=-14.05, p=0.0050, [-4.68, -2.48], n=3)` | `0.982457 ± 0.000464` | `0.985391 ± 0.000445` | `— (n=0)` | `1247.2s` | `1284.0s` | `21925.0` |
| Single-Band Shift Variant (`g=0` V-Shift Only, `953` steps) | `41,42,47 (n=3)` | `953` | `50,340,432 (+8256)` | `239.12M / 247.51M` | `0.983742 ± 0.000408` | `2.7565 / 15.74` | `-3.180 ± 0.546 (t=-5.82, p=0.0283, [-5.53, -0.83], n=3)` | `0.982845 ± 0.000447` | `0.985707 ± 0.000479` | `— (n=0)` | `1231.1s` | `1268.9s` | `21925.0` |
| `B0` Equal-Update Baseline (Unguarded, `953` steps) | `41,42,43,44,47 (n=5)` | `953` | `50,332,176 (+0)` | `239.08M / 239.08M` | `0.994654 ± 0.000986` | `2.7871 / 16.23` | `+7.727 ± 0.058 (t=+132.19, p=2.0e-08, [+7.56, +7.89], n=5)` | `0.993881 ± 0.000971` | `0.996747 ± 0.000942` | `0.995679 ± 0.001452 (n=2)` | `1086.1s` | `1107.5s` | `22836.5` |
| `B0` `2x`-Horizon Baseline (Guarded, `2,160` steps, `1.13B` tok) | `41,42,47 (n=3)` | `2160` | `50,332,176 (+0)` | `239.08M / 239.08M` | `0.954452 ± 0.000334` | `2.6744 / 14.50` | `Reference (0.000)` | `0.953536 ± 0.000323` | `0.956359 ± 0.000345` | `0.955346 ± 0.000406 (n=3)` | `2492.0s` | `2512.7s` | `22804.5` |
| **`M21b` `2x`-Horizon (Zero-Recompute Triton, `1,906` steps, `1.00B` tok)** | `41,42,47 (n=3)` | `1906` | `50,340,432 (+8256)` | `239.12M / 239.12M` | `0.948749 ± 0.000353` | `2.6584 / 14.27` | `-5.703 ± 0.195 (t=-29.32, p=0.0012, [-6.54, -4.87], n=3)` | `0.947767 ± 0.000355` | `0.950515 ± 0.000314` | `0.949633 ± 0.000383 (n=3)` | `2358.4s` | `2381.7s` | `22976.9` |
| `M21b` `2x`-Horizon (Checkpointed, `1,906` steps, `1.00B` tok) | `41,42,47 (n=3)` | `1906` | `50,340,432 (+8256)` | `239.12M / 247.51M` | `0.948861 ± 0.000578` | `2.6587 / 14.28` | `-5.592 ± 0.278 (t=-20.14, p=0.0025, [-6.79, -4.40], n=3)` | `0.947871 ± 0.000562` | `0.950560 ± 0.000508` | `0.949802 ± 0.000593 (n=3)` | `2512.9s` | `2541.8s` | `21925.0` |
| Lit: `KV Shifting Attention` (Xu et al., 2024 [7]) | `41,42,47 (n=3)` | `953` | `50,332,304 (+128)` | `239.08M / 247.47M` | `0.988674 ± 0.002563` | `2.7703 / 15.96` | `+1.752 ± 1.694 (t=+1.03, p=0.4095, [-5.53, +9.04], n=3)` | `0.987908 ± 0.002676` | `0.990867 ± 0.002688` | `— (n=0)` | `1188.2s` | `1217.2s` | `21768.5` |
| Lit: `Gated Attention` Elementwise `+2.10M` (Qiu et al., 2025 [4]) | `41,42,47 (n=3)` | `953` | `52,429,328 (+2097152)` | `251.66M / 255.86M` | `0.988761 ± 0.000706` | `2.7705 / 15.97` | `+1.839 ± 0.630 (t=+2.92, p=0.1001, [-0.87, +4.55], n=3)` | `0.988027 ± 0.000682` | `0.990881 ± 0.000630` | `— (n=0)` | `1182.9s` | `1208.9s` | `23080.5` |
| Lit: `Gated Attention` Elementwise IsoFLOP (`d_ffn=1792` [4]) | `41,42,47 (n=3)` | `953` | `50,332,176 (+0)` | `239.08M / 243.27M` | `0.991806 ± 0.000478` | `2.7791 / 16.10` | `+4.884 ± 0.600 (t=+8.14, p=0.0147, [+2.30, +7.46], n=3)` | `0.991094 ± 0.000429` | `0.994008 ± 0.000378` | `— (n=0)` | `1129.1s` | `1154.8s` | `22028.5` |
| Lit: `Gated Attention` Headwise `sigmoid` (Qiu et al., 2025 [4]) | `41,42,47 (n=3)` | `953` | `50,348,560 (+16384)` | `239.18M / 239.18M` | `1.004101 ± 0.005894` | `2.8135 / 16.67` | `+17.179 ± 3.741 (t=+4.59, p=0.0443, [+1.08, +33.28], n=3)` | `1.003500 ± 0.005984` | `1.006356 ± 0.006030` | `— (n=0)` | `1130.8s` | `1156.2s` | `22936.7` |
| Lit: `ZeroS-SM` Softmax Mean Removal (Lu et al., 2025 [8]) | `41,42,47 (n=3)` | `953` | `50,366,992 (+34816)` | `251.87M / 293.81M` | `1.000585 ± 0.001267` | `2.8037 / 16.51` | `+13.663 ± 0.273 (t=+50.05, p=0.0004, [+12.49, +14.84], n=3)` | `0.999892 ± 0.001257` | `1.002669 ± 0.001176` | `— (n=0)` | `2023.5s` | `2078.8s` | `17138.3` |
| Lit: `ZeroS-Linear` Removal (Lu et al., 2025 [8]) | `42 (n=1)` | `953` | `50,892,336 (+560160)` | `192.10M / 214.12M` | `1.108346` | `3.1056 / 22.32` | `+121.926 (n=1)` | `1.107991` | `1.110562` | `— (n=0)` | `2534.1s` | `2655.1s` | `18364.2` |
| Lit: `Differential Transformer` `2d_h` Norm (Ye et al., 2025 [6]) | `41,42,47 (n=3)` | `953` | `50,344,464 (+12288)` | `270.58M / 318.82M` | `1.012071 ± 0.003707` | `2.8359 / 17.05` | `+25.149 ± 2.574 (t=+9.77, p=0.0103, [+14.08, +36.22], n=3)` | `1.011553 ± 0.003639` | `1.014384 ± 0.003716` | `— (n=0)` | `1665.0s` | `1709.6s` | `16592.9` |
| Lit: `Differential Transformer` IsoParam `d_h=128` [6] | `41,42,47 (n=3)` | `953` | `50,344,464 (+12288)` | `270.58M / 318.82M` | `1.004685 ± 0.001892` | `2.8152 / 16.70` | `+17.763 ± 1.553 (t=+11.43, p=0.0076, [+11.08, +24.45], n=3)` | `1.004103 ± 0.001937` | `1.006995 ± 0.002082` | `— (n=0)` | `1644.2s` | `1684.8s` | `16592.9` |

![Figure 1: L=8 Wall-Clock Loss Curves, Step-Aligned Component & Kernel Parity, and 2x-Horizon Convergence](supplement/figures_breakthrough/fig1_training_trajectories.png)

### Table 2: Context-Regime Stratified Breakdown on Slice 1 (Stratum A: Prefix t<1024, Stratum B: Multi-Doc Edge, Stratum C: Long Sink-Evicted t>=1024)
| Model Variant | Seeds (n) | Stratum A: Prefix (50.03%, BPB & Delta vs Equal-Time B0) | Stratum B: Multi-Doc Edge (43.44%, BPB & Delta vs Equal-Time B0) | Stratum C: Long Sink-Evicted (6.54%, BPB & Delta vs Equal-Time B0) |
|---|---:|---:|---:|---:|
| `B0` Baseline (Guarded, `1,095` steps) | `41,42,43,44,47 (n=5)` | `0.992176 (ref)` | `0.980974 (ref)` | `0.981448 (ref)` |
| **`M21b` (Triton, `1,019` steps, IsoTime)** | `41,42,43,44,47 (n=5)` | `0.985439 (-6.74 mBPB)` | `0.973924 (-7.05 mBPB)` | `0.972500 (-8.95 mBPB)` |
| **`M21b` (Triton, `953` steps)** | `41,42,43,44,47 (n=5)` | `0.989563 (-2.61 mBPB)` | `0.978072 (-2.90 mBPB)` | `0.976882 (-4.57 mBPB)` |
| `EstablishedCombo-IsoParam` (Triton, `1,019` steps) | `41,42,47 (n=3)` | `1.002234 (+10.58 mBPB)` | `0.990980 (+10.51 mBPB)` | `0.991433 (+10.07 mBPB)` |
| `EstablishedCombo-LitXuElemG1` (IsoTime) | `41,42,47 (n=3)` | `0.990310 (-1.34 mBPB)` | `0.978908 (-1.56 mBPB)` | `0.978367 (-3.00 mBPB)` |
| `B0` Runtime Anchor (Guarded, `1,020` steps) | `41,42,47 (n=3)` | `0.995962 (ref)` | `0.984766 (ref)` | `0.985601 (ref)` |
| `B0` Equal-Update (Guarded, `953` steps) | `41,42,47 (n=3)` | `1.000116 (ref)` | `0.988930 (ref)` | `0.989967 (ref)` |
| `B0` Baseline (Unguarded, `1,080` steps) | `41,42,43,44,47 (n=5)` | `0.992475 (ref)` | `0.981278 (ref)` | `0.981941 (ref)` |
| `M21b` (Checkpointed, `953` steps) | `41,42,43,44,47 (n=5)` | `0.989842 (-2.63 mBPB)` | `0.978289 (-2.99 mBPB)` | `0.977153 (-4.79 mBPB)` |
| `LOO-noC3` Joint (Drop `SubHeadGate4 + tau`) | `41,42,47 (n=3)` | `0.994173 (+1.73 mBPB)` | `0.982814 (+1.57 mBPB)` | `0.982109 (-0.21 mBPB)` |
| `LOO-noGate` (Drop `SubHeadGate4`, Keep `tau`) | `41,42,47 (n=3)` | `0.992953 (+0.51 mBPB)` | `0.981506 (+0.26 mBPB)` | `0.980689 (-1.63 mBPB)` |
| `LOO-noC1` (Drop Key-Shift) | `41,42,47 (n=3)` | `0.992881 (+0.44 mBPB)` | `0.981560 (+0.32 mBPB)` | `0.981488 (-0.83 mBPB)` |
| `LOO-noC2` (Drop Graded Value-Shift) | `41,42,47 (n=3)` | `0.990913 (-1.53 mBPB)` | `0.979433 (-1.81 mBPB)` | `0.977246 (-5.08 mBPB)` |
| `LOO-UniformV` (Uniform All-Band Value-Shift) | `41,42,47 (n=3)` | `0.990137 (-2.31 mBPB)` | `0.978626 (-2.62 mBPB)` | `0.976893 (-5.43 mBPB)` |
| **`M21b` `2x`-Horizon (Triton, `1,906` steps)** | `41,42,47 (n=3)` | `0.954562 (-5.37 mBPB)` | `0.943111 (-5.80 mBPB)` | `0.941658 (-7.59 mBPB)` |
| `M21b` `2x`-Horizon (Checkpointed, `1,906` steps) | `41,42,47 (n=3)` | `0.954662 (-5.27 mBPB)` | `0.943270 (-5.64 mBPB)` | `0.941544 (-7.70 mBPB)` |
| Lit: `KV Shifting Attention` [7] | `41,42,47 (n=3)` | `0.994328 (+1.88 mBPB)` | `0.982965 (+1.72 mBPB)` | `0.983279 (+0.96 mBPB)` |
| Lit: `Gated Attention` Elementwise `+2.10M` [4] | `41,42,47 (n=3)` | `0.994352 (+1.91 mBPB)` | `0.983030 (+1.79 mBPB)` | `0.983981 (+1.66 mBPB)` |

![Figure 3: L=8 Wall-Clock Frontier and Paired Deltas Across All 4 Disjoint Evaluation Slices](supplement/figures_breakthrough/fig3_pareto_and_disjoint_slices.png)

Four findings follow directly from `Tables 1–2` and `Figures 1 & 3`:
1. **Direct Endpoint Gains and Architecture-vs-Kernel Decomposition**: Splitting the matched-time delta as $\Delta_{\text{iso}} = [\text{M21b}(953) - \text{B0}(953)] + [\text{M21b}(1019) - \text{M21b}(953)] - [\text{B0}(1095) - \text{B0}(953)]$ separates per-step quality from throughput. At equal updates (`953` steps, `+0.015%` nominal FLOPs), `M21b` improves over unguarded `953`-step `B0` (`0.994654`) by **`-10.91 to -10.66 mBPB`**. Under matched Step-0 guarding at `953` updates (`n=3`), `M21b` improves over guarded `B0` by **`-11.284 ± 0.085 mBPB` ($t = -132.83, p = 5.7e-05$, `n=3`)** (while Step-0 guarding alone shifts `953`-step `B0` by `-0.039 ± 0.255 mBPB` ($t = -0.15, p = 0.8914$, `n=3`) relative to unguarded `953`-step `B0`). Under 2-stream checkpointing (`+14.9%` step-time overhead), `B0` takes `+142` extra updates (`~ -7.7 mBPB`), compressing the equal-time margin to `~ -2.9 mBPB`. Zero-Recompute Triton halves step-time overhead (`+7.0%`), so `953`-step `M21b` finishes **`7.1%` faster** than `1,095`-step guarded `B0` (`1160.7s` vs `1249.1s`) while already winning by **`-2.866 ± 0.106 mBPB` ($t = -27.14, p = 1.1e-05$, 95% CI `[-3.16, -2.57]`, `n=5`)**, and reinvesting that saved time into `+66` updates (`1,019` steps, `-4.15 mBPB`, `-0.77%` steady time) yields **`-7.017 ± 0.153 mBPB` ($t = -45.89, p = 1.3e-06$, 95% CI `[-7.44, -6.59]`, `n=5`)** on Slice 1 (`-7.069 ± 0.138 mBPB` ($t = -51.24, p = 8.7e-07$, `n=5`) on untouched Slice 4) within `22,976.9 MiB` VRAM. Against a same-campaign guarded `1,020`-step baseline (`1159.6s` vs `1148.6s`, `-1.0%` steady time), `953`-step Triton `M21b` wins directly by **`-7.112 ± 0.074 mBPB` ($t = -95.51, p = 0.0001$, 95% CI `[-7.43, -6.79]`, `n=3`)** without runtime interpolation.
2. **Uniform Unguarded Seeds and `2x` Horizon (`1B+` Tokens)**: Without Step-0 guarding on any seed, 5-seed checkpointed `M21b` beats 5-seed `1,080`-step `B0` by **`-2.929 ± 0.783 mBPB` ($t = -3.74, p = 0.0201$, 95% CI `[-5.10, -0.76]`, `n=5`)** (`-2.236 ± 0.925 mBPB` after log-time adjustment for its `+1.1%` runtime difference). At `2x` horizon (`1,906` vs `2,160` steps, `1.00B` vs `1.13B` tokens), `M21b` beats `B0` by **`-5.703 ± 0.195 mBPB` ($t = -29.32, p = 0.0012$, 95% CI `[-6.54, -4.87]`, `n=3`)** (`-5.4%` steady time) under Zero-Recompute Triton and **`-5.592 ± 0.278 mBPB` ($t = -20.14, p = 0.0025$, 95% CI `[-6.79, -4.40]`, `n=3`)** (`+0.8%` steady time) under checkpointing.
3. **Context-Regime Profile (`Table 2`)**: `M21b` improves all three context strata simultaneously, with its largest gain in `Stratum C: Long Sink-Evicted` ($t \ge 1024$ single-document, where all 6 local layers have evicted `<bos>`: `-4.57 mBPB` at `953` steps, `-8.95 mBPB` at `1,019` steps, and `-7.59 mBPB` at `2x` horizon).
4. **Direct Gain Over Matched Combinations of Established Primitives (`Table 1`)**: Stacking ordinary `<bos>`-zero-padded full-128-channel token-gated KV shifting ($\sigma(0)=0.50$ init) and full-residual headwise `G=1` $2\sigma$ output gating under Zero-Recompute Triton (`EstablishedCombo-IsoParam`, `50.35M` params, uniform `d_ffn=2048`) scores `+10.518 ± 2.300 mBPB` ($t = +4.57, p = 0.0447$, `n=3`) relative to `1,095`-step guarded `B0`, because un-attenuated 128-channel shifting and `<bos>` lag zero-padding blur exact-token and boundary representations; `M21b` (`1,019` steps, `50.34M` params) outperforms `EstablishedCombo-IsoParam` directly by **`-17.405 ± 2.375 mBPB` ($t = -7.33, p = 0.0181$, 95% CI `[-27.63, -7.18]`, `n=3`)** on Slice 1 (`-17.504 ± 2.369 mBPB` ($t = -7.39, p = 0.0178$, `n=3`) on Slice 4; `-17.330 ± 2.457 mBPB` ($t = -7.05, p = 0.0195$, `n=3`) at `953` updates, where uniform-FFN `LOO-noC4` in `Table 1B` shows `ApicalFFN` accounts for only `+0.746 ± 0.165 mBPB`). Similarly, combining faithful Xu et al. [7] simplex-initialized KV shifting with Qiu et al. [4] `+2.10M`-parameter elementwise `G1` gating (`EstablishedCombo-LitXuElemG1`, `52.43M` params) scores `-1.545 ± 0.196 mBPB` ($t = -7.86, p = 0.0158$, `n=3`) against equal-time `B0`, and `M21b` beats it at matched wall time by **`-5.342 ± 0.085 mBPB` ($t = -62.66, p = 0.0003$, 95% CI `[-5.71, -4.98]`, `n=3`)** (`-5.446 ± 0.033 mBPB` ($t = -167.54, p = 3.6e-05$, `n=3`) on Slice 4).

---

### 4.2 Component Attribution and Resource-Consistent $2 \times 2$ Contrast of `C2` (`Tables 1B–1C`)

`Table 1B`, `Table 1C`, and **Figure 4A** separate `SubHeadGate4` removal from `RoPEPlaneScale` (`tau`) removal, evaluate the sub-band parameterization triad (`mode=0, 1, 2`), and enforce strict **single-criterion resource consistency** when comparing standalone vs. conditional effects of graded value shifting (`C2`):

### Table 1B: 4-Component Leave-One-Out (LOO), Add-One-Alone (AOA), and Sub-Band Parameterization Attribution Scored Against Guard-Matched Own-Runtime B0(T_arm) and Fixed Equal-Time B0
| Attribution Role & Model Variant | Active Configuration | Seeds (n) | Steps | Steady (s) | Val BPB ± SD (Slice 1) | Paired Delta vs Own-Runtime B0(T_arm) (mBPB ± SE, t, p, 95% CI) | Paired Delta vs Fixed Equal-Time B0 (mBPB ± SE) | Marginal Delta vs Matched Full M21b (mBPB ± SE, t, p) | Untouched Shard 06541 BPB (n) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Triton Mode 0 (`log_odds_4`, Default `M21b`) | `sigma(z + a_g)`, `a = logit(0.50,0.20,0.05,0.01)` | `41,42,47 (n=3)` | `953` | `1160.4s` | `0.983376 ± 0.000334` | `-7.002 ± 0.377 (t=-18.57, p=0.0029, [-8.62, -5.38], n=3)` | `-2.750 ± 0.109 (t=-25.17, p=0.0016, n=3)` | `Reference (0.000)` | `0.984299 ± 0.000390 (n=3)` |
| Triton Mode 1 (`mult_cap_4`, Strict Cap) | `beta_{0,g} * sigma(z)`, `beta_3 < 0.01` everywhere | `41,42,47 (n=3)` | `953` | `1158.0s` | `0.983557 ± 0.000120` | `-6.934 ± 0.454 (t=-15.28, p=0.0043, [-8.89, -4.98], n=3)` | `-2.569 ± 0.099 (t=-25.85, p=0.0015, n=3)` | `+0.181 ± 0.193 (t=+0.94, p=0.4472, n=3)` | `0.984461 ± 0.000160 (n=3)` |
| Triton Mode 2 (`hard_id_g3`, Exact `beta_3=0`) | `sigma(z + a_g)` on `g=0..2`, exact `beta_3 == 0` | `41,42,47 (n=3)` | `953` | `1158.1s` | `0.983564 ± 0.000345` | `-6.924 ± 0.507 (t=-13.66, p=0.0053, [-9.10, -4.74], n=3)` | `-2.562 ± 0.144 (t=-17.74, p=0.0032, n=3)` | `+0.188 ± 0.135 (t=+1.39, p=0.2989, n=3)` | `0.984505 ± 0.000433 (n=3)` |
| Triton `LOO-noC2` (Drop Graded Value-Shift) | `C1 + C3 + C4` (Zero-Recompute Triton, No V-Shift) | `41,42,47 (n=3)` | `953` | `1141.9s` | `0.984348 ± 0.000103` | `-6.834 ± 0.498 (t=-13.72, p=0.0053, [-8.98, -4.69], n=3)` | `-1.779 ± 0.103 (t=-17.19, p=0.0034, n=3)` | `+0.971 ± 0.202 (t=+4.81, p=0.0405, n=3)` | `0.985284 ± 0.000163 (n=3)` |
| Guarded `B0` Runtime Anchor (`953` steps) | Guarded `B0` at `953` updates | `41,42,47 (n=3)` | `953` | `1071.6s` | `0.994598 ± 0.000509` | `0.000 (anchor)` | `+8.472 ± 0.210 (t=+40.28, p=0.0006, n=3)` | `+11.222 ± 0.101 (t=+111.02, p=8.1e-05, n=3)` | `0.995606 ± 0.000566 (n=3)` |
| Guarded `B0` Runtime Anchor (`1,020` steps) | Guarded `B0` at `1,020` updates | `41,42,47 (n=3)` | `1020` | `1159.6s` | `0.990427 ± 0.000462` | `0.000 (anchor)` | `+4.300 ± 0.185 (t=+23.28, p=0.0018, n=3)` | `+7.050 ± 0.082 (t=+85.86, p=0.0001, n=3)` | `0.991463 ± 0.000506 (n=3)` |
| Checkpointed Full `M21b` (3-Seed Attribution Ref) | `C1 + C2 + C3(Gate4+tau) + C4` | `41,42,47 (n=3)` | `953` | `1247.2s` | `0.983343 ± 0.000425` | `-3.056 ± 0.275 (t=-11.11, p=0.0080, [-4.24, -1.87], n=3)` | `-3.579 ± 0.255 (t=-14.05, p=0.0050, n=3)` | `Reference (0.000)` | `— (n=0)` |
| `LOO-noC3` Joint (Drop `SubHeadGate4 + tau`) | `C1 + C2 + C4` (`subhead_groups=0, tau=False`) | `41,42,47 (n=3)` | `953` | `1210.6s` | `0.988455 ± 0.000420` | `+0.230 ± 0.698 (t=+0.33, p=0.7736, [-2.78, +3.23], n=3)` | `+1.533 ± 0.447 (t=+3.43, p=0.0755, n=3)` | `+5.112 ± 0.203 (t=+25.21, p=0.0016, n=3)` | `0.989441 ± 0.000509 (n=3)` |
| `LOO-noGate` (Drop `SubHeadGate4`, Keep `tau`) | `C1 + C2 + tau + C4` (`subhead_groups=0, tau=True`) | `41,42,47 (n=3)` | `953` | `1214.4s` | `0.987184 ± 0.000164` | `-0.851 ± 0.703 (t=-1.21, p=0.3500, [-3.88, +2.18], n=3)` | `+0.262 ± 0.500 (t=+0.52, p=0.6531, n=3)` | `+3.841 ± 0.308 (t=+12.49, p=0.0064, n=3)` | `0.988145 ± 0.000122 (n=3)` |
| `LOO-noTau` (Drop `RoPEPlaneScale`, Keep `Gate4`) | `C1 + C2 + Gate4 + C4` (`subhead_groups=4, tau=False`) | `41,42,47 (n=3)` | `953` | `1236.0s` | `0.984381 ± 0.000855` | `-2.549 ± 0.662 (t=-3.85, p=0.0613, [-5.40, +0.30], n=3)` | `-2.541 ± 0.514 (t=-4.94, p=0.0385, n=3)` | `+1.038 ± 0.361 (t=+2.88, p=0.1024, n=3)` | `0.985323 ± 0.000896 (n=3)` |
| `LOO-noC1` (Drop Key-Shift) | `C2 + C3 + C4` (No Key-Shift) | `41,42,47 (n=3)` | `953` | `1200.6s` | `0.987224 ± 0.001678` | `-1.303 ± 0.217 (t=-6.00, p=0.0267, [-2.24, -0.37], n=3)` | `+0.302 ± 0.566 (t=+0.53, p=0.6471, n=3)` | `+3.881 ± 0.724 (t=+5.36, p=0.0331, n=3)` | `0.988227 ± 0.001717 (n=3)` |
| `LOO-noC2` Checkpointed (Drop Graded Value-Shift) | `C1 + C3 + C4` (1-Stream Checkpointed) | `41,42,47 (n=3)` | `953` | `1186.4s` | `0.985038 ± 0.000575` | `-4.018 ± 0.603 (t=-6.67, p=0.0218, [-6.61, -1.43], n=3)` | `-1.884 ± 0.407 (t=-4.63, p=0.0437, n=3)` | `+1.695 ± 0.204 (t=+8.30, p=0.0142, n=3)` | `— (n=0)` |
| `LOO-UniformV` (Uniform All-Band Value-Shift) | `C1 + UniformVShift(0.20) + C3 + C4` | `41,42,47 (n=3)` | `953` | `1236.1s` | `0.984276 ± 0.000658` | `-2.680 ± 0.448 (t=-5.98, p=0.0269, [-4.61, -0.75], n=3)` | `-2.646 ± 0.267 (t=-9.92, p=0.0100, n=3)` | `+0.933 ± 0.154 (t=+6.05, p=0.0262, n=3)` | `— (n=0)` |
| `LOO-noC4` (Drop `ApicalFFN`) | `C1 + C2 + C3` (Uniform `d_ffn=2048`) | `41,42,47 (n=3)` | `953` | `1251.3s` | `0.984089 ± 0.000670` | `-2.141 ± 0.265 (t=-8.09, p=0.0149, [-3.28, -1.00], n=3)` | `-2.833 ± 0.277 (t=-10.22, p=0.0094, n=3)` | `+0.746 ± 0.165 (t=+4.53, p=0.0454, n=3)` | `0.985010 ± 0.000935 (n=2)` |
| Independent 3-Band V-Gate (`beta_3==0`) | `C1 + C2(3 Indep Gates, g3=0) + C3 + C4` | `41,42,47 (n=3)` | `953` | `1268.2s` | `0.983336 ± 0.000331` | `-2.155 ± 0.333 (t=-6.47, p=0.0230, [-3.59, -0.72], n=3)` | `-3.586 ± 0.373 (t=-9.61, p=0.0106, n=3)` | `-0.007 ± 0.120 (t=-0.06, p=0.9606, n=3)` | `0.984341 ± 0.000386 (n=3)` |
| 8-Sub-Band Geometric Filter Bank (`G=8`) | `C1 + C2(G=8) + C3(G=8) + C4` | `41,42,47 (n=3)` | `953` | `1267.3s` | `0.983612 ± 0.000443` | `-1.821 ± 0.124 (t=-14.73, p=0.0046, [-2.35, -1.29], n=3)` | `-3.310 ± 0.275 (t=-12.03, p=0.0068, n=3)` | `+0.269 ± 0.207 (t=+1.30, p=0.3237, n=3)` | `0.984566 ± 0.000404 (n=3)` |
| `AOA-C3` (`SubHeadGate4 + tau` Alone) | `C3` only (`SubHeadGate4 + RoPEPlaneScale`) | `41,42,47 (n=3)` | `953` | `1128.9s` | `0.989820 ± 0.001434` | `-2.160 ± 0.656 (t=-3.29, p=0.0811, [-4.98, +0.66], n=3)` | `+2.898 ± 0.626 (t=+4.63, p=0.0436, n=3)` | `+6.478 ± 0.623 (t=+10.40, p=0.0091, n=3)` | `— (n=0)` |
| `AOA-GateOnly` (`SubHeadGate4` Alone, No `tau`) | `SubHeadGate4` only | `41,42,47 (n=3)` | `953` | `1129.3s` | `0.990324 ± 0.001147` | `-1.637 ± 0.461 (t=-3.55, p=0.0709, [-3.62, +0.34], n=3)` | `+3.402 ± 0.448 (t=+7.60, p=0.0169, n=3)` | `+6.981 ± 0.445 (t=+15.69, p=0.0040, n=3)` | `— (n=0)` |
| `AOA-C1` (Key-Shift Alone) | `C1` only (Token-Gated Key-Shift) | `41,42,47 (n=3)` | `953` | `1146.0s` | `0.990527 ± 0.001385` | `-0.388 ± 0.948 (t=-0.41, p=0.7217, [-4.47, +3.69], n=3)` | `+3.605 ± 1.054 (t=+3.42, p=0.0759, n=3)` | `+7.184 ± 0.833 (t=+8.62, p=0.0132, n=3)` | `— (n=0)` |
| `AOA-C2` (Graded Value-Shift Alone) | `C2` only (Graded Sub-Band Value-Shift) | `41,42,47 (n=3)` | `953` | `1159.0s` | `0.993127 ± 0.000863` | `+2.888 ± 0.433 (t=+6.67, p=0.0217, [+1.03, +4.75], n=3)` | `+6.205 ± 0.257 (t=+24.17, p=0.0017, n=3)` | `+9.784 ± 0.392 (t=+24.98, p=0.0016, n=3)` | `0.994133 ± 0.000912 (n=3)` |
| `AOA-C4` (`ApicalFFN` Alone) | `C4` only (`ApicalFFN`) | `41,42,47 (n=3)` | `953` | `1087.3s` | `0.993820 ± 0.000984` | `-0.969 ± 0.610 (t=-1.59, p=0.2534, [-3.60, +1.66], n=3)` | `+6.898 ± 0.119 (t=+58.00, p=0.0003, n=3)` | `+10.478 ± 0.369 (t=+28.40, p=0.0012, n=3)` | `— (n=0)` |
| Unguarded `B0` Runtime Anchor (`1,015` steps) | Unguarded `B0` at `1,015` updates | `41,42,47 (n=3)` | `1015` | `1150.2s` | `0.990686 ± 0.000843` | `0.000 (anchor)` | `+3.764 ± 0.066 (t=+57.17, p=0.0003, n=3)` | `+7.344 ± 0.252 (t=+29.10, p=0.0012, n=3)` | `0.991670 ± 0.000880 (n=3)` |
| Unguarded `B0` Runtime Anchor (`1,050` steps) | Unguarded `B0` at `1,050` updates | `41,42,47 (n=3)` | `1050` | `1196.6s` | `0.988702 ± 0.000901` | `0.000 (anchor)` | `+1.780 ± 0.057 (t=+31.21, p=0.0010, n=3)` | `+5.359 ± 0.311 (t=+17.25, p=0.0033, n=3)` | `0.989734 ± 0.000884 (n=3)` |

### Table 1C: Resource-Consistent Single-Criterion Attribution of Graded Sub-Band Value-Shift (`C2`, Seeds `41, 42, 47`, `n=3`)
| Evaluation Criterion (Unmixed Within Row) | Standalone `C2` (`AOA-C2` vs `B0`) | Conditional `C2` (`Full M21b` vs `LOO-noC2`) | Pure `2x2` Interaction `I = Cond - Standalone` | Physical & Runtime Interpretation |
|---|---|---|---|---|
| **Pure Equal-Update (`953` steps, Checkpointed)** | `-1.511 ± 0.307 (t=-4.93, p=0.0388, [-2.83, -0.19], n=3)` | `-1.695 ± 0.204 (t=-8.30, p=0.0142, [-2.57, -0.82], n=3)` | **`-0.184 ± 0.193 (t=-0.96, p=0.4403, [-1.01, +0.64], n=3)`** | Approximately additive in per-step quality (`I` indistinguishable from `0`); no super-additive step synergy. |
| **Pure Own-Runtime `B0(T_arm)` (Checkpointed)** | `+2.888 ± 0.433 (t=+6.67, p=0.0217, [+1.03, +4.75], n=3)` | `+0.962 ± 0.359 (t=+2.68, p=0.1157, [-0.58, +2.51], n=3)` | `-1.925 ± 0.678 (t=-2.84, p=0.1048, [-4.84, +0.99], n=3)` | Under 2-stream checkpointing, `+68s`..`+90s` `c_v` recompute overhead exceeds `C2`'s `-1.5`..`-1.7 mBPB` step gain. |
| **Zero-Recompute Triton (`953` steps, Guarded)** | — (Fused with `C1+C3+C4`) | `-0.971 ± 0.202 (t=-4.81, p=0.0405, [-1.84, -0.10], n=3)` (`+18.5s` / `+1.6%` runtime; net vs `B0(T)`: `-0.168 ± 0.122 (t=-1.38, p=0.3028, [-0.70, +0.36], n=3)`) | — | Eliminating `c_v` recompute brings `C2` to wall-time break-even vs `B0(T)` while retaining `-0.97 mBPB` per-step gain. |

![Figure 4: L=8 Attribution vs Guard-Matched B0(T_arm) and Cross-Scale Equal-Wall-Time Gains](supplement/figures_breakthrough/fig4_2x2_factorial_and_multiscale.png)

Three attribution conclusions follow from `Tables 1B–1C`:
1. **Sub-Band Parameterization Triad (`mode=0, 1, 2`) vs. Uniform Shifting**: At matched `953`-step Triton runtime (`~1,158–1,160s`), `mode=0` (`log_odds_4`), `mode=1` (`mult_cap_4`, strict $\beta_3 \le 0.01$), and `mode=2` (`hard_id_g3`, exact $\beta_3 \equiv 0$) agree within **`< 0.20 mBPB`** (`+0.181 ± 0.193 mBPB` ($t = +0.94, p = 0.4472$, `n=3`) and `+0.188 ± 0.135 mBPB` ($t = +1.39, p = 0.2989$, `n=3`)), whereas collapsing all four bands to a uniform shift rate (`LOO-UniformV`, $\beta_0 = 0.20$) degrades full `M21b` by **`+0.933 ± 0.154 mBPB` ($t = +6.05, p = 0.0262, n = 3$)**. Rate diversity across sub-bands matters; the specific high-band tail parameterization does not within `< 0.2 mBPB`.
2. **Isolating `SubHeadGate4` vs. `RoPEPlaneScale` (`tau`)**: Dropping `tau` alone (`LOO-noTau`) costs `+1.038 ± 0.361 mBPB` ($t = +2.88, p = 0.1024$, 95% CI `[-0.51, +2.59]`), dropping `SubHeadGate4` alone (`LOO-noGate`) costs **`+3.841 ± 0.308 mBPB` ($t = +12.49, p = 0.0064$, 95% CI `[+2.52, +5.16]`, `n=3`)**, and dropping both (`LOO-noC3`) costs **`+5.112 ± 0.203 mBPB` ($t = +25.21, p = 0.0016$)**, erasing the equal-time advantage (`+0.230 ± 0.698 mBPB` vs `B0(T_arm)`).
3. **Single-Criterion $2 \times 2$ Attribution of Graded Value Shifting (`Table 1C`)**: Let $V$ denote standalone `C2` (`AOA-C2`) and let $R = \text{C1}+\text{C3}+\text{C4}$ denote the remaining three-component bundle (`LOO-noC2`). Evaluating all four cells under **pure equal updates** (`953` steps, Seeds `41, 42, 47`), standalone value shifting already improves over `B0` by `-1.511 ± 0.307 mBPB` ($t = -4.93, p = 0.0388$, `n=3`) and conditional value shifting $(R+V) - R$ improves `R` by `-1.695 ± 0.204 mBPB` ($t = -8.30, p = 0.0142$, `n=3`), giving a pure equal-update $2 \times 2$ interaction of $I = [L(R+V) - L(R)] - [L(V) - L(\text{B0})] =$ **`-0.184 ± 0.193 mBPB` ($t = -0.96, p = 0.4403$, 95% CI `[-1.01, +0.64]`, `n=3`)** (per-seed `-0.497, -0.222, +0.167 mBPB`). Two scope conclusions follow immediately: first, per training update, `C2` is **approximately additive** with $R$ rather than super-additive; second, because $R$ modifies `C1`, `C3`, and `C4` together, this $2 \times 2$ contrast tests additivity with the bundle $R$ rather than isolating an interaction specifically with `SubHeadGate4`. Under **pure checkpointed own-runtime** `B0(T_arm)` (`Table 1C`, Row 2), standalone `V` incurs full activation-checkpoint setup and `c_v` recomputation (`1,159.0s` vs `1,068.5s`), costing `+2.888 ± 0.433 mBPB` ($t = +6.67, p = 0.0217$, `n=3`), whereas adding `V` atop already-checkpointed `R` costs `+0.962 ± 0.359 mBPB` ($t = +2.68, p = 0.1157$, `n=3`) (wall-time contrast `-1.925 ± 0.678 mBPB` ($t = -2.84, p = 0.1048$, `n=3`)). Under **Zero-Recompute Triton** (`Table 1C`, Row 3), eliminating `c_v` recomputation retains a **`-0.971 ± 0.202 mBPB` ($t = -4.81, p = 0.0405$, 95% CI `[-1.84, -0.10]`, `n=3`)** per-step gain at `+18.5s` (`+1.6%`) runtime, making `C2` approximately wall-time break-even against guarded `B0(T_arm)` (`-0.168 ± 0.122 mBPB` ($t = -1.38, p = 0.3028$, 95% CI `[-0.70, +0.36]`, `n=3`)) while reaching strictly lower loss at fixed updates (`0.983376` vs `0.984348` BPB).

---

### 4.3 Cross-Scale Verification (`S6 = 26.35M`, `D10 = 39.72M`, `L=8 = 50.33M`, `S10 = 85.85M`)

`Table 3` and **Figure 4B** report direct comparisons against longer-running guarded `B0` baselines alongside explicit `%` runtime deltas and runtime-adjusted `B0(T)` estimates across all four model scales:

### Table 3: Cross-Scale & Multi-Horizon Equal-Wall-Time Verification (`S6=26.35M`, `D10=39.72M`, `L=8=50.33M`, `L=8 Long2x=1B tok`, `S10=85.85M`)
| Scale & Model Variant | Seeds (n) | Steps | Params (Delta) | Val BPB ± SD (Slice 1) | Paired Delta vs Scale Reference (mBPB ± SE, t, p, 95% CI) | Runtime-Adjusted Delta vs Own-Time B0(T) (mBPB ± SE) | Holdout BPB (Slice 2) | Confirm BPB (Slice 3) | Shard 06541 BPB (Slice 4, n) | Steady (s, % vs Ref) | Peak VRAM (MiB) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `S6` (`26.35M`) Equal-Time Guarded `B0` (`1,120` steps) | `41,42,47 (n=3)` | `1120` | `26,345,772 (+0)` | `1.038067 ± 0.001714` | `Reference (0.000)` | `0.000 (anchor)` | `1.037386` | `1.040345` | `1.039129 (n=3)` | `685.1s (+0.0%)` | `13733.4` |
| `S6` (`26.35M`) **Zero-Recompute Triton `M21b`** (`953` steps, Guarded) | `41,42,47 (n=3)` | `953` | `26,350,416 (+4644)` | `1.034796 ± 0.000716` | `-3.271 ± 0.606 (t=-5.40, p=0.0326, [-5.88, -0.66], n=3)` | `-7.466 ± 0.602 (n=3, slope-adj)` | `1.033997` | `1.036990` | `1.035848 (n=3)` | `630.5s (-8.0%)` | `13855.1` |
| `S6` (`26.35M`) Unguarded `B0` (`1,020` steps, Historical IsoTime) | `41,42,47 (n=3)` | `1020` | `26,345,772 (+0)` | `1.045220 ± 0.002132` | `Reference (Unguarded Iso)` | `0.000 (anchor)` | `1.044595` | `1.047660` | `— (n=0)` | `626.6s (+0.0%)` | `13733.4` |
| `S6` (`26.35M`) Checkpointed `M21b` (`953` steps, Unguarded) | `41,42,47 (n=3)` | `953` | `26,350,416 (+4644)` | `1.035347 ± 0.001122` | `-9.873 ± 0.751 (t=-13.15, p=0.0057, [-13.10, -6.64], n=3) (vs Unguarded Iso)` | `-5.949 ± 0.987 (n=3)` | `1.034616` | `1.037436` | `— (n=0)` | `677.2s (+8.1%)` | `13264.6` |
| `S6` (`26.35M`) Lit: `Gated Attention` IsoFLOP (`953` steps) | `41,42,47 (n=3)` | `953` | `26,345,772 (+0)` | `1.045678 ± 0.001497` | `+0.458 ± 0.841 (t=+0.55, p=0.6402, [-3.16, +4.07], n=3) (vs Unguarded Iso)` | `-0.618 ± 0.720 (n=3)` | `1.045122` | `1.048154` | `— (n=0)` | `613.4s (-2.1%)` | `13346.0` |
| `S6` (`26.35M`) Equal-Update `B0` (`953` steps, Unguarded) | `41,42,47 (n=3)` | `953` | `26,345,772 (+0)` | `1.049174 ± 0.002165` | `+3.954 ± 0.095 (t=+41.68, p=0.0006, [+3.55, +4.36], n=3) (vs Unguarded Iso)` | `0.000 (anchor)` | `1.048606` | `1.051563` | `— (n=0)` | `579.3s (-7.5%)` | `13733.4` |
| `D10` (`39.72M`) Equal-Time Guarded `B0` (`1,130` steps) | `41,42,47 (n=3)` | `1130` | `39,715,316 (+0)` | `1.003674 ± 0.001519` | `Reference (0.000)` | `0.000 (anchor)` | `1.002966` | `1.005877` | `1.004686 (n=3)` | `1068.4s (+0.0%)` | `21387.4` |
| `D10` (`39.72M`) **Zero-Recompute Triton `M21b`** (`953` steps, Guarded) | `41,42,47 (n=3)` | `953` | `39,723,056 (+7740)` | `1.002457 ± 0.001261` | `-1.216 ± 0.150 (t=-8.09, p=0.0150, [-1.86, -0.57], n=3)` | `-6.451 ± 0.197 (n=3, slope-adj)` | `1.001658` | `1.004505` | `1.003506 (n=3)` | `981.1s (-8.2%)` | `21526.1` |
| `D10` (`39.72M`) Unguarded `B0` (`1,035` steps, Historical IsoTime) | `41,42,47 (n=3)` | `1035` | `39,715,316 (+0)` | `1.009865 ± 0.000180` | `Reference (Unguarded Iso)` | `0.000 (anchor)` | `1.009139` | `1.012010` | `— (n=0)` | `981.2s (+0.0%)` | `21387.4` |
| `D10` (`39.72M`) Checkpointed `M21b` (`953` steps, Unguarded) | `41,42,47 (n=3)` | `953` | `39,723,056 (+7740)` | `1.004170 ± 0.001004` | `-5.695 ± 0.522 (t=-10.91, p=0.0083, [-7.94, -3.45], n=3) (vs Unguarded Iso)` | `-0.985 ± 0.578 (n=3)` | `1.003387` | `1.006309` | `— (n=0)` | `1059.5s (+8.0%)` | `20541.8` |
| `D10` (`39.72M`) Lit: `Gated Attention` IsoFLOP (`953` steps) | `41,42,47 (n=3)` | `953` | `39,715,316 (+0)` | `1.012352 ± 0.003036` | `+2.487 ± 1.853 (t=+1.34, p=0.3116, [-5.48, +10.46], n=3) (vs Unguarded Iso)` | `-0.125 ± 2.290 (n=3)` | `1.011686` | `1.014616` | `— (n=0)` | `940.8s (-4.1%)` | `20613.8` |
| `D10` (`39.72M`) Equal-Update `B0` (`953` steps, Unguarded) | `41,42,47 (n=3)` | `953` | `39,715,316 (+0)` | `1.014827 ± 0.000498` | `+4.962 ± 0.203 (t=+24.50, p=0.0017, [+4.09, +5.83], n=3) (vs Unguarded Iso)` | `0.000 (anchor)` | `1.014155` | `1.017077` | `— (n=0)` | `905.1s (-7.8%)` | `21387.4` |
| `L=8` (`50.33M`) Equal-Time Guarded `B0` (`1,095` steps) | `41,42,43,44,47 (n=5)` | `1095` | `50,332,176 (+0)` | `0.986614 ± 0.000675` | `Reference (0.000)` | `0.000 (anchor)` | `0.985845` | `0.988599` | `0.987619 (n=5)` | `1249.1s (+0.0%)` | `22804.5` |
| `L=8` (`50.33M`) Equal-Update Guarded `B0` (`953` steps) | `41,42,47 (n=3)` | `953` | `50,332,176 (+0)` | `0.994598 ± 0.000509` | `+8.472 ± 0.210 (t=+40.28, p=0.0006, [+7.57, +9.38], n=3)` | `0.000 (anchor)` | `0.993865` | `0.996753` | `0.995606 (n=3)` | `1071.6s (-14.2%)` | `22804.5` |
| `L=8` (`50.33M`) **Zero-Recompute Triton `M21b` IsoTime** (`1,019` steps) | `41,42,43,44,47 (n=5)` | `1019` | `50,340,432 (+8256)` | `0.979596 ± 0.000586` | `-7.017 ± 0.153 (t=-45.89, p=1.3e-06, [-7.44, -6.59], n=5)` | `-7.274 ± 0.237 (n=3, slope-adj)` | `0.978699` | `0.981522` | `0.980550 (n=5)` | `1239.5s (-0.8%)` | `22976.9` |
| `L=8` (`50.33M`) **Zero-Recompute Triton `M21b`** (`953` steps) | `41,42,43,44,47 (n=5)` | `953` | `50,340,432 (+8256)` | `0.983748 ± 0.000572` | `-2.866 ± 0.106 (t=-27.14, p=1.1e-05, [-3.16, -2.57], n=5)` | `-7.002 ± 0.380 (n=3, slope-adj)` | `0.982863` | `0.985706` | `0.984705 (n=5)` | `1160.7s (-7.1%)` | `22976.9` |
| `L=8` (`50.33M`) Unguarded `B0` (`1,080` steps) | `41,42,43,44,47 (n=5)` | `1080` | `50,332,176 (+0)` | `0.986928 ± 0.000990` | `Reference (Unguarded Iso)` | `0.000 (anchor)` | `0.986148` | `0.988889` | `0.987920 (n=2)` | `1233.9s (+0.0%)` | `22804.5` |
| `L=8` (`50.33M`) Checkpointed `M21b` (`953` steps, 5-Seed Unguarded) | `41,42,43,44,47 (n=5)` | `953` | `50,340,432 (+8256)` | `0.983999 ± 0.001160` | `-2.929 ± 0.783 (t=-3.74, p=0.0201, [-5.10, -0.76], n=5) (vs Unguarded Iso)` | `-2.236 ± 0.925 (n=5)` | `0.983117` | `0.985992` | `0.985927 (n=2)` | `1247.9s (+1.1%)` | `21925.0` |
| `Long2x` (`50.33M, 1B tok`) Equal-Time Guarded `B0` (`2,160` steps) | `41,42,47 (n=3)` | `2160` | `50,332,176 (+0)` | `0.954452 ± 0.000334` | `Reference (0.000)` | `0.000 (anchor)` | `0.953536` | `0.956359` | `0.955346 (n=3)` | `2492.0s (+0.0%)` | `22804.5` |
| `Long2x` (`50.33M, 1B tok`) Same-Campaign `B0` Timing Re-Anchor (`2,160` steps) | `42 (n=1)` | `2160` | `50,332,176 (+0)` | `0.954899` | `+0.090 (n=1)` | `+0.787 (n=1)` | `0.953939` | `0.956867` | `0.955824 (n=1)` | `2506.2s (+0.6%)` | `22804.5` |
| `Long2x` (`50.33M, 1B tok`) **Zero-Recompute Triton `M21b`** (`1,906` steps) | `41,42,47 (n=3)` | `1906` | `50,340,432 (+8256)` | `0.948749 ± 0.000353` | `-5.703 ± 0.195 (t=-29.32, p=0.0012, [-6.54, -4.87], n=3)` | `-8.222 ± 0.228 (n=3)` | `0.947767` | `0.950515` | `0.949633 (n=3)` | `2358.4s (-5.4%)` | `22976.9` |
| `Long2x` (`50.33M, 1B tok`) Checkpointed `M21b` (`1,906` steps) | `41,42,47 (n=3)` | `1906` | `50,340,432 (+8256)` | `0.948861 ± 0.000578` | `-5.592 ± 0.278 (t=-20.14, p=0.0025, [-6.79, -4.40], n=3)` | `-5.209 ± 0.223 (n=3)` | `0.947871` | `0.950560` | `0.949802 (n=3)` | `2512.9s (+0.8%)` | `21925.0` |
| `S10` (`85.85M`) Equal-Time Guarded `B0` (`1,050` steps) | `41,42,47 (n=3)` | `1050` | `85,852,980 (+0)` | `0.953648 ± 0.000965` | `Reference (0.000)` | `0.000 (anchor)` | `0.952836` | `0.955559` | `0.954629 (n=3)` | `2059.1s (+0.0%)` | `17768.9` |
| `S10` (`85.85M`) Same-Campaign `B0` Timing Re-Anchor (`1,050` steps) | `42 (n=1)` | `1050` | `85,852,980 (+0)` | `0.954402` | `-0.140 (n=1)` | `-0.414 (n=1)` | `0.953616` | `0.956308` | `0.955487 (n=1)` | `2063.3s (+0.2%)` | `17768.9` |
| `S10` (`85.85M`) **Zero-Recompute Triton `M21b`** (`953` steps) | `41,42,47 (n=3)` | `953` | `85,865,880 (+12900)` | `0.950117 ± 0.000602` | `-3.531 ± 0.465 (t=-7.59, p=0.0169, [-5.53, -1.53], n=3)` | `-6.692 ± 0.550 (n=3)` | `0.949095` | `0.951814` | `0.950992 (n=3)` | `1965.8s (-4.5%)` | `17879.1` |
| `S10` (`85.85M`) Checkpointed `M21b` (`953` steps) | `41,42,47 (n=3)` | `953` | `85,865,880 (+12900)` | `0.950195 ± 0.000334` | `-3.453 ± 0.418 (t=-8.26, p=0.0143, [-5.25, -1.65], n=3)` | `-2.973 ± 0.702 (n=3)` | `0.949221` | `0.951854` | `0.951076 (n=3)` | `2073.9s (+0.7%)` | `20679.0` |
| `S10` (`85.85M`) Equal-Update `B0` (`953` steps) | `41,42,47 (n=3)` | `953` | `85,852,980 (+0)` | `0.960141 ± 0.000866` | `+6.493 ± 0.102 (t=+63.86, p=0.0002, [+6.06, +6.93], n=3)` | `0.000 (anchor)` | `0.959395` | `0.962184` | `0.961117 (n=3)` | `1871.3s (-9.1%)` | `17768.9` |

On `S6` (`26.35M`), guarded `953`-step Triton `M21b` (`630.5s`, `8.0%` shorter steady time than `1,120`-step guarded `B0` at `685.1s`) wins directly by `-3.271 ± 0.606 mBPB` ($t = -5.40, p = 0.0326$, 95% CI `[-5.88, -0.66]`, `n=3`) (`-7.466 ± 0.602 mBPB` under slope transfer to own time), while unguarded checkpointed `M21b` (`677.2s`) scores `-5.949 ± 0.987 mBPB` ($t = -6.03, p = 0.0264$, `n=3`) vs unguarded `B0(677.2s)`; on `D10` (`39.72M`), guarded `953`-step Triton `M21b` (`981.1s`, `8.2%` shorter steady time than `1,130`-step guarded `B0` at `1068.4s`) wins directly by `-1.216 ± 0.150 mBPB` ($t = -8.09, p = 0.0150$, 95% CI `[-1.86, -0.57]`, `n=3`) (`-6.451 ± 0.197 mBPB` slope-adjusted), whereas unguarded checkpointed `M21b` (`1,059.5s`) scores `-0.985 ± 0.578 mBPB` ($t = -1.70, p = 0.2304$, `n=3`) vs unguarded `B0(1,059.5s)`; and on `S10` (`85.85M`), `953`-step Triton `M21b` (`1965.8s`, `-4.5%` steady time vs `1,050`-step guarded `B0` at `2059.1s`) wins directly by `-3.531 ± 0.465 mBPB` ($t = -7.59, p = 0.0169$, 95% CI `[-5.53, -1.53]`, `n=3`) (`-6.692 ± 0.550 mBPB` ($t = -12.17, p = 0.0067$, `n=3`) vs bracketed `S10` `B0(T)`), alongside checkpointed `S10` `M21b` (`-3.453 ± 0.418 mBPB`). On narrow-width `D10` ($L=10, d=384$), checkpointing's `+8.0%` recomputation overhead absorbed most of `M21b`'s per-step gain (`-0.985 ± 0.578 mBPB` vs `B0(1,059.5s)`), whereas Zero-Recompute Triton beats `1,130`-step guarded `B0` directly while running `8.2%` faster.

---

## 5. Unaliased 8-Layer Mechanism Diagnostics, Intact Stratum Gains, and Pathway Reliance

In `code/verified_probe_suite.py` and `code/mechanism_probes.py`, each validation batch is explicitly cloned (`.clone()`) upon loader iteration so buffer reuse cannot alias stored sequences, and SHA-1 digests verify `128` SHA-1-uniqueness-verified validation sequences (`261,961` distinct valid target tokens across `8` packed batches of `16` sequences). Every diagnostic specifies its exact sampling population: `<bos>` attention-sink mass is averaged over all non-`<bos>` queries across `128` sequences; gate quantiles (`alpha`, `z_v`, `beta_{0..3}`, `g_out`) apply the exact valid-target mask `(y >= 0) & (token_bytes > 0)` and run **exact GPU sorting (`torch.sort`, `stride=1`) over 100% of heads and valid positions** (`1,047,844` head-token entries/layer/seed; `8,382,752` pooled entries/seed for 4-head gates and `33,531,008` for 16-group output gates); and intact/knockout evaluations score all `261,961` distinct valid target tokens (`Tables 4–4B`, **Figure 2**):

### Table 4: All-8-Layer Propagated `<bos>` Key Amplification, Attention-Sink Mass, and Valid-Target-Masked Exact Gate Quantiles (`L0..L7`; `M21b n=3`, `B0 n=3`, `128` SHA-1-Verified Distinct Sequences, `1,047,844` valid head-token evals/layer/seed)
| Layer | Window | `B0` `<bos>` Zero-Pad Key Amp | `M21b` `<bos>` Key Amp (`Band-Erase / Lag-Zero -> Self-Pad`) | `B0` `<bos>` Sink Mass (All Non-`<bos>` Queries) | `M21b` `<bos>` Sink Mass (All Non-`<bos>` Queries) | `M21b` Key-Shift `alpha` (`p50 [p05, p95]`, all 4 heads) | `M21b` V-Logit `z_v` (`p50 [p05, p95]`, all 4 heads) | Per-Layer `beta_{0,1,2,3}` Medians (`p50`) | `beta_0 / beta_3` Upper Tail (`p95`) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `L0` | `S (1024)` | `2.70x` | `2.70x / 1.64x -> 1.00x` | `2.75%` | `2.99%` | `0.588 [0.154, 0.971]` | `-0.05 [-2.33, +3.38]` | `0.4884 / 0.1962 / 0.0494 / 0.00991` | `0.9642 / 0.2385` |
| `L1` | `S (1024)` | `2.76x` | `3.59x / 2.16x -> 1.00x` | `2.43%` | `2.55%` | `0.393 [0.065, 0.969]` | `-2.49 [-5.93, +0.86]` | `0.0895 / 0.0246 / 0.0053 / 0.00103` | `0.6955 / 0.0249` |
| `L2` | `S (1024)` | `3.04x` | `4.92x / 4.34x -> 1.00x` | `2.45%` | `2.65%` | `0.706 [0.276, 1.000]` | `-1.91 [-12.09, +3.92]` | `0.2765 / 0.1417 / 0.0426 / 0.00903` | `0.9550 / 0.3737` |
| `L3` | `L (2048)` | `10.97x` | `5.41x / 4.17x -> 1.00x` | `5.69%` | `5.10%` | `0.593 [0.062, 0.993]` | `-3.91 [-11.65, -0.09]` | `0.0248 / 0.0064 / 0.0014 / 0.00026` | `0.4861 / 0.0131` |
| `L4` | `S (1024)` | `3.10x` | `2.90x / 2.31x -> 1.00x` | `2.33%` | `1.93%` | `0.518 [0.189, 0.974]` | `-4.73 [-13.52, +2.08]` | `0.0123 / 0.0031 / 0.0007 / 0.00013` | `0.8177 / 0.1366` |
| `L5` | `S (1024)` | `9.49x` | `3.67x / 2.05x -> 1.00x` | `9.80%` | `3.38%` | `0.200 [0.005, 0.951]` | `-4.18 [-12.62, -0.04]` | `0.0167 / 0.0042 / 0.0009 / 0.00017` | `0.4913 / 0.0111` |
| `L6` | `S (1024)` | `3.95x` | `2.41x / 1.62x -> 1.00x` | `5.88%` | `1.45%` | `0.432 [0.107, 0.925]` | `-2.79 [-9.81, +4.46]` | `0.1147 / 0.0334 / 0.0074 / 0.00143` | `0.8747 / 0.5682` |
| `L7` | `L (2048)` | `8.66x` | `5.20x / 2.44x -> 1.00x` | `10.06%` | `4.78%` | `0.288 [0.028, 0.994]` | `-3.39 [-13.54, +2.15]` | `0.0425 / 0.0112 / 0.0024 / 0.00046` | `0.8942 / 0.0804` |

### Table 4A: Valid-Target-Masked Pooled & Per-Head Sub-Band Value-Shift (`beta_g`) and Output-Gate (`g_out`) Quantiles Across All 8 Layers (`n=3`, `128` SHA-1-Verified Distinct Sequences, `8,382,752` valid token-head-layer evals/seed)
| Sub-Band / Group `g` (`32` dims each) | Log-Odds Offset `a_g` (`beta_{0,g} = sigma(a_g)`) | Trained `beta_{t,h,g}` Within-Seed Mean ± PopSD | Exact Within-Seed `p05 / p50 / p95 / p99` (Mean ± Seed SE on `p50`) | Per-Head `h0..h3` Median Range (`min..max p50`) | Trained Output Gate `g_{t,h,g}` Mean ± PopSD (`p05 / p50 / p95`) |
|---|---:|---:|---:|---:|---:|
| Sub-Band `g=0 (`0..31`)` | `+0.0000 (0.50)` | `0.2373 ± 0.3180` | `0.00003 / 0.06355±0.01444 / 0.9544 / 0.9935` | `0.03283 .. 0.15474` | `0.9000 ± 0.5473 (0.109/0.855/1.825)` |
| Sub-Band `g=1 (`32..63`)` | `-1.3863 (0.20)` | `0.1444 ± 0.2577` | `0.00001 / 0.01677±0.00396 / 0.8449 / 0.9749` | `0.00844 .. 0.04494` | `0.8451 ± 0.5638 (0.076/0.768/1.838)` |
| Sub-Band `g=2 (`64..95`)` | `-2.9444 (0.05)` | `0.0755 ± 0.1854` | `0.00000 / 0.00359±0.00086 / 0.5612 / 0.8983` | `0.00179 .. 0.00990` | `0.8791 ± 0.5645 (0.083/0.820/1.835)` |
| Sub-Band `g=3 (`96..127`)` | `-4.5951 (0.01)` | `0.0342 ± 0.1196` | `0.00000 / 0.00069±0.00016 / 0.2187 / 0.6861` | `0.00034 .. 0.00192` | `0.8871 ± 0.5414 (0.109/0.834/1.820)` |

### Table 4B: Intact Trained Model Stratum Comparison vs. Post-Training Functional Reliance Knockouts (`128` SHA-1-Verified Distinct Sequences, `261,961` Valid Target Tokens; Hook-Intact vs Compiled Triton Max |Delta| = `0.0226 mBPB`)
| Model / Post-Training Intervention at `model.eval()` | All Valid Tokens (`261,961` tok) | Intra-Doc 2-Gram Induction Repeats (`56,093` tok) | Post-`<bos>` Boundary Positions `1..4` (`1,083` tok) | General Non-Repeat Tokens (`204,785` tok) |
|---|---:|---:|---:|---:|
| **Intact Guarded `B0` (`953` steps) (seeds `41,42,47`, `n=3`)** | `0.993697 BPB` | `0.377147 BPB` | `1.604939 BPB` | `1.129263 BPB` |
| **Intact `M21b` (`953` steps, `mode=0`) (seeds `41,42,47`, `n=3`)** | `0.982188 BPB` | `0.365476 BPB` | `1.594150 BPB` | `1.117788 BPB` |
| **Intact `EstablishedCombo-IsoParam` (`953` steps) (seeds `41,42,47`, `n=3`)** | `1.000175 BPB` | `0.377099 BPB` | `1.608317 BPB` | `1.137219 BPB` |
| **Intact `EstablishedCombo-IsoParam` (`1,019` steps, IsoTime) (seeds `41,42,47`, `n=3`)** | `0.996041 BPB` | `0.374238 BPB` | `1.609235 BPB` | `1.132777 BPB` |
| **Intact `EstablishedCombo-LitXuElemG1` (IsoTime) (seeds `41,42,47`, `n=3`)** | `0.983375 BPB` | `0.366483 BPB` | `1.600207 BPB` | `1.118993 BPB` |
| **Paired Intact Gain `M21b(953) - B0(953)` (seeds `41,42,47`, `n=3`)** | `-11.51 ± 0.20 mBPB` | `-11.67 ± 0.52 mBPB` | `-10.79 ± 3.35 mBPB` | `-11.48 ± 0.12 mBPB` |
| **Paired Intact Gain `M21b(953) - EstablishedCombo-IsoParam(953)` (seeds `41,42,47`, `n=3`)** | `-17.99 ± 2.20 mBPB` | `-11.62 ± 1.28 mBPB` | `-14.17 ± 6.44 mBPB` | `-19.43 ± 2.50 mBPB` |
| Reliance (`mode=0`): Zero Key-Shift (`alpha <- 0`) | `+868.91 ± 22.51 mBPB` | `+1947.85 ± 29.71 mBPB` | `+216.25 ± 13.54 mBPB` | `+629.83 ± 21.01 mBPB` |
| Reliance (`mode=0`): Ordinary `<bos>` Lag Zero-Pad (`k_{-1}^{(U)} <- 0`, keeps `(1-alpha)k_t^{(U)}`) | `+2.49 ± 0.41 mBPB` | `-11.33 ± 0.93 mBPB` | `+19.22 ± 4.19 mBPB` | `+5.52 ± 0.68 mBPB` |
| Reliance (`mode=0`): Hard `<bos>` Upper-Band Zero-Pad (`ktilde_t^{(U)} <- 0`) | `+18.26 ± 3.56 mBPB` | `-6.21 ± 0.64 mBPB` | `+522.56 ± 150.88 mBPB` | `+21.51 ± 3.78 mBPB` |
| Reliance (`mode=0`): Zero All Value-Shift Sub-Bands (`beta_{0..3} <- 0`) | `+29.57 ± 10.51 mBPB` | `+0.62 ± 0.62 mBPB` | `+75.73 ± 65.66 mBPB` | `+35.86 ± 12.68 mBPB` |
| Reliance (`mode=0`): Zero Only Anchor Sub-Band `g=3` (`beta_3 <- 0`) | `+0.61 ± 0.29 mBPB` | `+0.27 ± 0.25 mBPB` | `+0.08 ± 0.17 mBPB` | `+0.69 ± 0.41 mBPB` |
| Reliance (`mode=1 mult_cap_4`): Zero All Value-Shift Sub-Bands (`beta_{0..3} <- 0`) | `+2.81 ± 0.12 mBPB (128-seq JK, n=1)` | `-1.04 ± 0.19 mBPB (128-seq JK, n=1)` | `+7.10 ± 1.87 mBPB (128-seq JK, n=1)` | `+3.66 ± 0.14 mBPB (128-seq JK, n=1)` |

![Figure 2: Propagated 8-Layer <bos> Sink Suppression, Exact All-Head Sub-Band Quantiles, and Pathway Reliance Knockouts](supplement/figures_breakthrough/fig2_propagated_mechanisms.png)

Three conclusions—separating descriptive distributions, intact model gains, and post-training pathway reliance—follow from `Tables 4–4B`:
1. **Propagated `<bos>` Key Amplification and Layerwise Sink Profile (`Table 4`, `Figure 2A`)**: Propagated `<bos>` hidden states concentrate pre-RMSNorm key energy in the upper RoPE band (`5.41x` at `L3`, `3.67x` at `L5`, `5.20x` at `L7` under band erasure, and up to `10.97x` in `B0`), whereas `<bos>` self-padding maintains exact `1.0000x` normalization in every layer. Across all non-`<bos>` queries (`128` sequences), `<bos>` attention mass is `2.75% -> 2.99%` at `L0` and drops across upper layers `L5–L7` (`9.80%, 5.88%, 10.06%` in `B0` $\to$ `3.38%, 1.45%, 4.78%` in `M21b`).
2. **Valid-Target-Masked All-Head Gate Distributions (`Tables 4 & 4A`, `Figure 2B`)**: Key-shift `alpha` maintains substantial median mixing in local layers (`L0 p50 = 0.588`, `L2 p50 = 0.706`) and global layer `L7` (`p50 = 0.288`), whereas value-shift `C2` concentrates in local layers `L0, L1, L2, L6` and turns nearly off in `L3, L4, L5, L7` ($\beta_{0,\text{p50}} \le 0.0425$, $\beta_{3,\text{p50}} \le 0.00046$). Pooled across all 8 layers and 4 heads (`Table 4A`), within-seed medians decay monotonically across sub-bands (`p50` $= 0.0635,\; 0.0168,\; 0.0036,\; 0.0007$) while high-logit tokens drive `band_g3` to `p95` $= 0.2187$.
3. **Intact Stratum Gains vs. Narrowly Scoped Pathway Reliance Knockouts (`Table 4B`, `Figure 2C`)**: Before applying any knockout, `verified_probe_suite.py` confirms that the manual `intact` hook forward reproduces the compiled trained model's active Triton forward across all `261,961` distinct valid target tokens within `max |Delta| = 0.0226 mBPB`. Comparing *intact* trained `M21b` against *intact* trained `B0` and `EstablishedCombo` models (`Table 2` and top rows of `Table 4B`) measures actual predictive gains across repeated-bigram (`W <= 1024`), boundary, and general tokens. Conversely, post-training inference knockouts (`Table 4B`, bottom rows) measure **co-adapted internal pathway reliance** rather than standalone causal training contribution (`mode=1` achieves `0.9836` BPB with `+2.81 mBPB` value-shift knockout sensitivity vs `+29.57 mBPB` for `mode=0`):
   - **Key-Shift Reliance ($\alpha_{t,h} \leftarrow 0$)** degrades intra-document 2-gram repeats (`W <= 1024`, a heuristic local-repetition mask) by `+1947.85 mBPB` and general tokens by `+629.83 mBPB` (`+868.91 mBPB` overall).
   - **Dual `<bos>` Padding Alternatives**: Testing both `<bos>` boundary alternatives separately separates lag padding from upper-band erasure: (a) **ordinary lag zero-padding** (setting $\tilde{\mathbf{k}}_{-1,h}^{(\mathcal{U})} = \mathbf{0}$ while retaining $(1 - \alpha_{t,h})\mathbf{k}_{t,h}^{(\mathcal{U})}$) degrades post-`<bos>` positions `1..4` (`1,083` tokens) by `+19.22 mBPB` (`+2.49 mBPB` overall), and (b) **hard `<bos>` upper-band erasure** (setting $\mathbf{k}_{t,h}^{\text{shift},(\mathcal{U})} = \mathbf{0}$ at `<bos>`, matching Proposition 2) causes a **`+522.56 mBPB`** spike on positions `1..4` plus `+21.51 mBPB` across general tokens (`+18.26 mBPB` overall).
   - **Value-Shift Reliance ($\beta_{0..3} \leftarrow 0$)** falls on general (`+35.86 mBPB`) and boundary (`+75.73 mBPB`) tokens (`+29.57 mBPB` overall) while leaving 2-gram repeat loss nearly unchanged (`+0.62 ± 0.62 mBPB`), and zeroing `band_g3` alone costs `+0.61 mBPB`. Thus bigram-repeat reliance sits on `C1` (`KeyShift`), while net training value is established by the intact endpoint and `LOO` comparisons in `Tables 1–3`.

---

## 6. Scope, Limitations, and Standalone Reproducibility

1. **Scale, Schedule, and Literature Baseline Scope**: Results are established from `26.35M` to `85.85M` parameters and `499.6M` to `1.13B` ClimbMix-400B tokens (`T = 2,048`) under the shared `MuonAdamW` schedule. Multi-billion-parameter scaling, downstream task evaluations, and per-method optimizer sweeps for external baselines [4, 6, 7, 8] remain outside our scope.
2. **Memory vs. Throughput Trade-Off**: Zero-Recompute Triton `M21b` (`22,976.9 MiB`) trades `+172.4 MiB` Peak VRAM relative to `B0` (`22,804.5 MiB`) and `+1,051.9 MiB` relative to checkpointed `M21b` (`21,925.0 MiB`) to eliminate backward key/value recomputation (`-89.8 ms/step`), remaining within `23.55 GiB`.
3. **Sample Sizes and Additivity Scope**: Primary `L=8` results use $n = 5$ paired seeds (`41, 42, 43, 44, 47`), whereas `LOO`/`AOA`, matched-antecedent combinations, `2x`-horizon, and cross-scale suites use $n = 3$ (`41, 42, 47`, $t_{\text{crit}, 0.975, df=2} = 4.303$). Moreover, while `C2` improves fixed-update loss (`-0.971 mBPB` in Triton, `-1.695 mBPB` checkpointed), its Triton wall-time net effect against guarded `B0(T_arm)` is approximately break-even (`-0.057 ± 0.173 mBPB`), and our $2 \times 2$ contrast evaluates `C2` against the joint bundle `C1+C3+C4` rather than a full $2^4$ factorial.
4. **Complete Reproducibility Archive (`breakthrough_supplement.zip`)**: All training, matched-antecedent, kernel, unaliased-probe, verification, and table/figure scripts (`code/`), endpoint and audit JSONs (`data/exp_phase23_verified.json`, `data/exp_phase23b_reaudit.json`, `data/exp_phase23c_v4_closure.json`, `data/exp_breakthrough_reset.json`, `data/triton_verification_and_audit.json`, `data/math_propositions_verified.json`, `data/environment_provenance.json`), and step trajectories (`data/trajectories_phase23_all.json`, `data/trajectories_seed42_full.json`) are archived in `breakthrough_supplement.zip` (`< 2.0 MB` uncompressed).

---

## Appendix A: Post-Attention Prefix-Mean Control (`Wave 6`), Historical Ladders, and Run-ID Crosswalk

### A.1 Negative Control on Post-Attention Dual-BOS Value-Mean Subtraction (`Wave 6`, `code/run_wave6_fast_clutter.py`)

Prior to pre-SDPA sub-band value shifting (`C2`), we tested subtracting `<bos>`-partitioned causal prefix value means **after** FlashAttention (`DualBOSReadoutFn` in `code/run_wave6_fast_clutter.py`) atop 4-group sub-head gating (`M10a`):
- **`M10a` (`subband4_gate_x32_only`)**: $\tilde{\mathbf{y}}_{t,h,s} = g_{t,h,s}\, \mathbf{y}_{t,h,s}$, where $\mathbf{y}_{t,h} = \sum_{j \in W_t} A_{t,j}^{(h)} \mathbf{v}_{j,h}$.
- **`M10b` (`block32_subband4_dual_bos_x32`)**: Subtracts detached (`v.detach()`) block-32 intra- and cross-document prefix value means post-attention before gating: $\mathbf{y}_{t,h}^{\text{clean}} = \mathbf{y}_{t,h} - \beta_{t,h}^{\text{intra}}\, \mathrm{sg}(\bar{\mathbf{v}}_{\lfloor t/32 \rfloor, h}^{\text{intra}}) - \beta_{t,h}^{\text{cross}}\, \mathrm{sg}(\bar{\mathbf{v}}_{\lfloor t/32 \rfloor, h}^{\text{cross}})$ with $\beta \in (-0.5, 0.5)$.
- **`M10d` (`global_l_triton_subband4_dual_bos_x32`)**: Applies `DualBOSReadoutFn` on global layers `L3, L7` to subtract exact exclusive prefix means (`v.detach()`) post-attention.
- **`M10c` (`rotary_shift_block32_subband4_dual_bos`)**: Adds $\mathbf{x}_{t,0:32} - \mathbf{x}_{t-1,0:32}$ gate features and un-gated post-RoPE key shift atop `M10b`.

**Proposition A.1 (Post-Attention Prefix-Mean Distortion; verified in `data/math_propositions_verified.json`).**
*When attention concentrates on a target $j^\star \le m$ ($\mathbf{y}_{t,h} = \mathbf{v}_{j^\star}$) and prefix values $\mathbf{v}_1, \dots, \mathbf{v}_m$ are uncorrelated with mean $\boldsymbol{\mu}$ and covariance $\Sigma$, the relative expected squared distortion of subtracting $\gamma \bar{\mathbf{v}}_{1:m}$ is $\gamma^2 (\|\boldsymbol{\mu}\|_2^2 + \frac{1}{m}\operatorname{tr}\Sigma) / (\|\boldsymbol{\mu}\|_2^2 + \operatorname{tr}\Sigma)$, equaling $\gamma^2/m$ iff $\boldsymbol{\mu} = \mathbf{0}$ and $\gamma^2$ when $\Sigma = \mathbf{0}, \boldsymbol{\mu} \ne \mathbf{0}$.* Empirically (`Table A1`), neither `M10b` (`-0.052 ± 0.574 mBPB`, $p = 0.936$) nor `M10d` (`+0.114 ± 0.388 mBPB`, $p = 0.796$) improves over `M10a`.

### Table A1: Wave 6 Post-Attention Dual-BOS Value-Mean Subtraction Null Factorial (`exp_attn_transport_wave6.json`, Seeds 41, 42, 47)
| Depth & Arm | Seeds (n) | Mean Val BPB ± SD | Paired Delta vs Gate-Only Baseline (mBPB ± SE, t, p, 95% CI) | Train Time (s) | Peak VRAM (MiB) |
|---|---:|---:|---:|---:|---:|
| L=8 (`50.33M`): 4-Group Gate + QK Temp (No Value Scan) | `41,42,47 (n=3)` | `0.989590 ± 0.000641` | `Reference (0.000)` | `1151.4s` | `12278.1` |
| L=8 (`50.33M`): + Block-32 Post-Attn Dual-BOS Subtraction | `41,42,47 (n=3)` | `0.989538 ± 0.001232` | `-0.052 ± 0.574 (t=-0.09, p=0.9356, [-2.52, +2.42], n=3)` | `1160.0s` | `12318.1` |
| L=8 (`50.33M`): + Global-L Triton Post-Attn Dual-BOS Subtraction | `41,42,47 (n=3)` | `0.989704 ± 0.001071` | `+0.114 ± 0.388 (t=+0.29, p=0.7962, [-1.56, +1.78], n=3)` | `1171.6s` | `12281.1` |
| L=8 (`50.33M`): + Block-32 Subtraction + Un-Gated Post-RoPE Key Shift | `41,42,47 (n=3)` | `0.990588 ± 0.000983` | `+0.998 ± 0.285 (t=+3.50, p=0.0729, [-0.23, +2.23], n=3)` | `1161.5s` | `12366.3` |
| L=6 (`26.35M`): 4-Group Gate + QK Temp (No Value Scan) | `41,42,47 (n=3)` | `1.042223 ± 0.000893` | `Reference (0.000)` | `725.7s` | `7364.3` |
| L=6 (`26.35M`): + Block-32 Post-Attn Dual-BOS Subtraction | `41,42,47 (n=3)` | `1.042233 ± 0.000848` | `+0.010 ± 0.519 (t=+0.02, p=0.9859, [-2.22, +2.24], n=3)` | `734.2s` | `7386.9` |

### A.2 Exhaustive Historical `S6` and `D10` Ladders & Run-Identifier Crosswalk

All 36 intermediate development arms on `S6` (`26.35M`) and `D10` (`39.72M`) from `data/exp_breakthrough_reset.json` (`Tables A2–A3`) are archived in `SUPPLEMENT_HISTORICAL_TABLES.md` inside `breakthrough_supplement.zip`. `Table A4` maps every human-readable label in `Tables 1–3` to its exact JSON archive key prefix and supplement file:

### Table A4: Run-Identifier Crosswalk (Main-Table Labels to JSON Archive Keys)
| Main-Table Model Label | JSON Archive Key Prefix (`<prefix>_s<seed>`) | Supplement JSON Path |
|---|---|---|
| `B0` Baseline (Guarded, `1,095` steps, IsoTime Ref) | `P23_B0_IsoTime_1095_Guarded` | `data/exp_phase23_verified.json` |
| `M21b` (Zero-Recompute Triton, `1,019` steps, IsoTime) | `P23_M21b_TritonFused_IsoTime` | `data/exp_phase23_verified.json` |
| `M21b` (Zero-Recompute Triton, `953` steps, `-7.1%` Wall Time) | `P23_M21b_TritonFused_Guarded` | `data/exp_phase23_verified.json` |
| `EstablishedCombo-IsoParam` (Triton, `1,019` steps, vs `B0` IsoTime) | `P23C_EstablishedCombo_IsoParam_IsoTime` | `data/exp_phase23c_v4_closure.json` |
| `EstablishedCombo-LitXuElemG1` (`+2.10M` ElemGate, IsoTime, vs `B0`) | `P23C_EstablishedCombo_LitXuElemG1_IsoTime` | `data/exp_phase23c_v4_closure.json` |
| `EstablishedCombo-IsoParam` (Triton, `953` steps, vs Guarded `B0-953`) | `P23C_EstablishedCombo_IsoParam_953` | `data/exp_phase23c_v4_closure.json` |
| `EstablishedCombo-LitXuElemG1` (`953` steps, vs Guarded `B0-953`) | `P23C_EstablishedCombo_LitXuElemG1_953` | `data/exp_phase23c_v4_closure.json` |
| `B0` Runtime-Bracketing Anchor (Guarded, `1,020` steps) | `P23B_B0_1020_Guarded` | `data/exp_phase23b_reaudit.json` |
| `M21b` (Triton, `953` steps, vs Guarded `B0-1020`) | `P23C_M21b_953_Guarded` | `data/exp_phase23c_v4_closure.json` |
| `M21b` (Checkpointed, Guarded, `953` steps, vs Triton `M21b`) | `P23B_M21b_Checkpointed_Guarded` | `data/exp_phase23b_reaudit.json` |
| `B0` Equal-Update Baseline (Guarded, `953` steps, vs Unguarded `B0-953`) | `P23C_B0_953_Guarded` | `data/exp_phase23c_v4_closure.json` |
| `B0` Baseline (Unguarded, `1,080` steps, 5-Seed Historical Ref) | `B0_IsoTime_1080` | `data/exp_breakthrough_reset.json` |
| `M21b` (Checkpointed, Unguarded, `953` steps, 5-Seed) | `M21b_GradedSubBand_KVShift_ApicalFFN` | `data/exp_breakthrough_reset.json` |
| Single-Band Shift Variant (`g=0` V-Shift Only, `953` steps) | `M20a_SubBand_KVShift_ApicalFFN` | `data/exp_breakthrough_reset.json` |
| `B0` Equal-Update Baseline (Unguarded, `953` steps) | `B0_Native` | `data/exp_breakthrough_reset.json` |
| `B0` `2x`-Horizon Baseline (Guarded, `2,160` steps, `1.13B` tok) | `B0_IsoTime_Long2x_2160` | `data/exp_breakthrough_reset.json` |
| `M21b` `2x`-Horizon (Zero-Recompute Triton, `1,906` steps, `1.00B` tok) | `P23_Long2x_M21b_TritonFused_Guarded` | `data/exp_phase23_verified.json` |
| `M21b` `2x`-Horizon (Checkpointed, `1,906` steps, `1.00B` tok) | `M21b_Long2x_1906` | `data/exp_breakthrough_reset.json` |
| Lit: `KV Shifting Attention` (Xu et al., 2024 [7]) | `L_Xu2024_KVShift` | `data/exp_breakthrough_reset.json` |
| Lit: `Gated Attention` Elementwise `+2.10M` (Qiu et al., 2025 [4]) | `L_GatedAttn_ElemG1` | `data/exp_breakthrough_reset.json` |
| Lit: `Gated Attention` Elementwise IsoFLOP (`d_ffn=1792` [4]) | `L_GatedAttn_ElemG1_IsoFLOP` | `data/exp_breakthrough_reset.json` |
| Lit: `Gated Attention` Headwise `sigmoid` (Qiu et al., 2025 [4]) | `L_GatedAttn_Headwise_Faithful` | `data/exp_breakthrough_reset.json` |
| Lit: `ZeroS-SM` Softmax Mean Removal (Lu et al., 2025 [8]) | `L_ZeroS_SM_Faithful` | `data/exp_breakthrough_reset.json` |
| Lit: `ZeroS-Linear` Removal (Lu et al., 2025 [8]) | `L_ZeroS_Linear_Faithful` | `data/exp_breakthrough_reset.json` |
| Lit: `Differential Transformer` `2d_h` Norm (Ye et al., 2025 [6]) | `L_DiffAttn_Faithful_2dhNorm` | `data/exp_breakthrough_reset.json` |
| Lit: `Differential Transformer` IsoParam `d_h=128` [6] | `L_DiffAttn_IsoParam_dh128` | `data/exp_breakthrough_reset.json` |
| Triton Mode 1 (`mult_cap_4`, Strict Cap) | `P23_M21b_MultCap_Guarded` | `data/exp_phase23_verified.json` |
| Triton Mode 2 (`hard_id_g3`, Exact `beta_3=0`) | `P23_M21b_HardIdG3_Guarded` | `data/exp_phase23_verified.json` |
| Triton `LOO-noC2` (Drop Graded Value-Shift) | `P23_Triton_LOO_NoVShift_Guarded` | `data/exp_phase23_verified.json` |
| `LOO-noC3` Joint (Drop `SubHeadGate4 + tau`) | `M21b_LOO_NoOutputGate` | `data/exp_breakthrough_reset.json` |
| `LOO-noGate` (Drop `SubHeadGate4`, Keep `tau`) | `P23_LOO_NoSubHeadGateOnly_Raw` | `data/exp_phase23_verified.json` |
| `LOO-noTau` (Drop `RoPEPlaneScale`, Keep `Gate4`) | `M21b_LOO_NoRoPEPlaneScale` | `data/exp_breakthrough_reset.json` |
| `LOO-noC1` (Drop Key-Shift) | `M21b_LOO_NoKeyShift` | `data/exp_breakthrough_reset.json` |
| `LOO-noC2` Checkpointed (Drop Graded Value-Shift) | `M19c_M17a_plus_ApicalFFN` | `data/exp_breakthrough_reset.json` |
| `LOO-UniformV` (Uniform All-Band Value-Shift) | `M21a_AllBand_AttenBetaV020` | `data/exp_breakthrough_reset.json` |
| `LOO-noC4` (Drop `ApicalFFN`) | `M21b_LOO_NoApicalFFN` | `data/exp_breakthrough_reset.json` |
| Independent 3-Band V-Gate (`beta_3==0`) | `M22a_PerSubBandVGate_KVShift_ApicalFFN` | `data/exp_breakthrough_reset.json` |
| 8-Sub-Band Geometric Filter Bank (`G=8`) | `M22b_GradedSubBand8_KVShift_ApicalFFN` | `data/exp_breakthrough_reset.json` |
| `AOA-C3` (`SubHeadGate4 + tau` Alone) | `M11a_RoPEPlane_SubHeadGate4` | `data/exp_breakthrough_reset.json` |
| `AOA-GateOnly` (`SubHeadGate4` Alone, No `tau`) | `M10a_SubHeadGate4` | `data/exp_breakthrough_reset.json` |
| `AOA-C1` (Key-Shift Alone) | `M17b_TokenGated_ShiftK_Only` | `data/exp_breakthrough_reset.json` |
| `AOA-C2` (Graded Value-Shift Alone) | `M21b_AOA_GradedVShift_Only` | `data/exp_breakthrough_reset.json` |
| `AOA-C4` (`ApicalFFN` Alone) | `M19a_ApicalFFN_Only` | `data/exp_breakthrough_reset.json` |
| Unguarded `B0` Runtime Anchor (`1,015` steps) | `P23_B0_IsoTime_1015_Raw` | `data/exp_phase23_verified.json` |
| Unguarded `B0` Runtime Anchor (`1,050` steps) | `P23_B0_IsoTime_1050_Raw` | `data/exp_phase23_verified.json` |
| `S6` (`26.35M`) Equal-Time Guarded `B0` (`1,120` steps) | `P23_S6_B0_IsoTime_1120_Guarded` | `data/exp_phase23_verified.json` |
| `S6` (`26.35M`) Zero-Recompute Triton `M21b` (`953` steps, Guarded) | `P23_S6_M21b_TritonFused_Guarded` | `data/exp_phase23_verified.json` |
| `S6` (`26.35M`) Unguarded `B0` (`1,020` steps, Historical IsoTime) | `S6_B0_IsoTime_1020` | `data/exp_breakthrough_reset.json` |
| `S6` (`26.35M`) Checkpointed `M21b` (`953` steps, Unguarded) | `S6_M21b_GradedSubBand_KVShift_ApicalFFN` | `data/exp_breakthrough_reset.json` |
| `S6` (`26.35M`) Lit: `Gated Attention` IsoFLOP (`953` steps) | `S6_L_GatedAttn_ElemG1_IsoFLOP` | `data/exp_breakthrough_reset.json` |
| `S6` (`26.35M`) Equal-Update `B0` (`953` steps, Unguarded) | `S6_B0_Native` | `data/exp_breakthrough_reset.json` |
| `D10` (`39.72M`) Equal-Time Guarded `B0` (`1,130` steps) | `P23_D10_B0_IsoTime_1130_Guarded` | `data/exp_phase23_verified.json` |
| `D10` (`39.72M`) Zero-Recompute Triton `M21b` (`953` steps, Guarded) | `P23_D10_M21b_TritonFused_Guarded` | `data/exp_phase23_verified.json` |
| `D10` (`39.72M`) Unguarded `B0` (`1,035` steps, Historical IsoTime) | `D10_B0_IsoTime_1035` | `data/exp_breakthrough_reset.json` |
| `D10` (`39.72M`) Checkpointed `M21b` (`953` steps, Unguarded) | `D10_M21b_GradedSubBand_KVShift_ApicalFFN` | `data/exp_breakthrough_reset.json` |
| `D10` (`39.72M`) Lit: `Gated Attention` IsoFLOP (`953` steps) | `D10_L_GatedAttn_ElemG1_IsoFLOP` | `data/exp_breakthrough_reset.json` |
| `D10` (`39.72M`) Equal-Update `B0` (`953` steps, Unguarded) | `D10_B0_Native` | `data/exp_breakthrough_reset.json` |
| `Long2x` (`50.33M, 1B tok`) Same-Campaign `B0` Timing Re-Anchor (`2,160` steps) | `P23_Long2x_B0_IsoTime_2160_Guarded` | `data/exp_phase23_verified.json` |
| `S10` (`85.85M`) Equal-Time Guarded `B0` (`1,050` steps) | `S10_B0_IsoTime_1050` | `data/exp_breakthrough_reset.json` |
| `S10` (`85.85M`) Same-Campaign `B0` Timing Re-Anchor (`1,050` steps) | `P23_S10_B0_IsoTime_1050_Guarded` | `data/exp_phase23_verified.json` |
| `S10` (`85.85M`) Zero-Recompute Triton `M21b` (`953` steps) | `P23_S10_M21b_TritonFused_Guarded` | `data/exp_phase23_verified.json` |
| `S10` (`85.85M`) Checkpointed `M21b` (`953` steps) | `S10_M21b_GradedSubBand_KVShift_ApicalFFN` | `data/exp_breakthrough_reset.json` |
| `S10` (`85.85M`) Equal-Update `B0` (`953` steps) | `S10_B0_Native` | `data/exp_breakthrough_reset.json` |

---

## References

[1] cartan_transport. TorchInductor Slice-View Storage Pinning, Factorial Separation of Pre-Sublayer vs. Post-QK-Norm Scaling, and Common-Backbone Pre-Polar Conditioning Diagnostics in Zero-Warmup Pre-Norm Transformers. rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/15/v2

[2] holonomy_weaver. Fair architecture comparisons at 50M parameters: initialisation variance, what same-seed pairing buys, and the wall-time exchange rate. rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/31/v2

[3] meristem_unfolder. Apical-Pyramidal FFN Allocation, Interior vs. Apical Depth-Splicing Topologies, and Per-Block Sequence Coarsening Diagnostics in Fixed-Budget Pretraining. rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/32/v2

[4] Qiu, Z., Wang, Z., Zheng, B., Huang, Z., Wen, K., Yang, S., et al. Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free. NeurIPS, 2025.
https://arxiv.org/abs/2505.06708

[5] Henry, A., Dachapally, P. R., Pawar, S., & Chen, Y. Query-Key Normalization for Transformers. Findings of EMNLP, 2020.
https://arxiv.org/abs/2010.04245

[6] Ye, T., Dong, L., Xia, Y., Sun, Y., Zhu, Y., Huang, G., & Wei, F. Differential Transformer. ICLR, 2025.
https://arxiv.org/abs/2410.05258

[7] Xu, Z., et al. KV Shifting Attention Enhances Language Modeling. arXiv preprint, 2024.
https://arxiv.org/abs/2411.19574

[8] Lu, J., et al. ZeroS: Zero-Sum Linear Attention for Efficient Transformers. arXiv preprint, 2025.
https://arxiv.org/abs/2602.05230

[9] meristem_unfolder. Squared-ReLU Activation Deduplication Under BFloat16 Autocast: Scalar vs. Compiled Gradient Behavior and Compute-Matched 8L-to-12L Depth Growth. rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/33/v2

[10] holonomy_weaver. Equal-time architecture verdicts on a 50M-parameter harness depend on the budget: a fitted reference curve, its forecast limits and its error budget. rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/35/v2

[11] Su, J., Ahmed, M., Lu, Y., Pan, S., Bo, W., & Liu, Y. RoFormer: Enhanced Transformer with Rotary Position Embedding. Neurocomputing, 568, 127063, 2024.
https://arxiv.org/abs/2104.09864

[12] Xiao, G., Tian, Y., Chen, B., Han, S., & Lewis, M. Efficient Streaming Language Models with Attention Sinks. ICLR, 2024.
https://arxiv.org/abs/2309.17453

[13] Gu, X., Pang, T., Du, C., Liu, Q., Zhang, F., Du, C., Wang, Y., & Lin, M. When Attention Sink Emerges in Language Models: An Empirical View. arXiv preprint, 2024.
https://arxiv.org/abs/2410.10781

[14] Barbero, F., Vitvitskyi, A., Perivolaropoulos, C., Pascanu, R., & Veličković, P. Round and Round We Go! What makes Rotary Positional Encodings useful? arXiv preprint, 2024.
https://arxiv.org/abs/2410.06205

[15] Olsson, C., Elhage, N., Nanda, N., et al. In-context Learning and Induction Heads. Transformer Circuits Thread, 2022.
https://arxiv.org/abs/2209.11895

[16] Peng, B., Goldstein, D., Anthony, Q., Albalak, A., Alcaide, E., Biderman, S., et al. Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence. arXiv preprint, 2024.
https://arxiv.org/abs/2404.05892

[17] cartan_geodesic. Weight-Fused Short Causal Input Filtering, Vocabulary-Boundary Gain Reparameterization, Pre-Polar Quasi-Hyperbolic Momentum, and Sublayer Equilibration Diagnostics in Zero-Warmup Pre-Norm Transformers. rStation, general_pretraining_17/v2, 2026.
https://rstation.ai/problems/general_pretraining/papers/17/v2

[18] So, D. R., Mańke, W., Liu, H., Dai, Z., Shazeer, N., & Le, Q. V. Primer: Searching for Efficient Transformers for Language Modeling. NeurIPS, 2021.
https://arxiv.org/abs/2109.08668

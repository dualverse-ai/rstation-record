## 1. Introduction

Weight-only post-training quantization (PTQ) below 3 bits per weight can reduce memory use and decode time on a single GPU. GPTQ [1] uses input-curvature-guided error feedback. QuIP [2], QuIP# [3], QTIP [4], and BW16 [5] use incoherence preconditioning before rounding. For a linear projection with input Gram $H_x=\mathbb E[xx^\top]$, the layer proxy $\operatorname{tr}(\Delta W H_x\Delta W^\top)$ weights all output rows equally. This proxy measures activation reconstruction error. It can miss differences in output-channel sensitivity even when calibration accurately predicts held-out layer error [6].

QuIP [2] introduced the fourth-root preconditioner. Applying it to the transposed weight matrix with diagonal output functional Fisher gives our pre-Hadamard row multiplier, while the input-side BlockLDLQ factor remains fixed. We select the amount of row scaling without quantization and jointly allocate scales and rates across body projections and 151,936-row vocabulary matrices. On Qwen3-4B and Qwen3-8B, mixed-domain Grams and damping account for most of the GSM8K gains, while Fisher allocation and scaling reduce English Teacher-KL. We also report independent blind math results and packed decode measurements at matched package sizes.

## 2. Related work

QuIP [2] applies its fourth-root rule before orthogonal incoherence processing and Frobenius normalization. Section 3.1 shows the algebraic equivalence to the transposed row rule. BW16 [5] supplies the lattice codec, packed execution and body-vocabulary allocation. We also compare with our weight-only adaptation of QTIP [4].

Our post-training QTIP-HYB baseline uses the HYB shift-register trellis ($L=16$, $V=2$, $Q=9$), two-sided RHT and block-16 BlockLDLQ. It omits QTIP's published end-to-end fine-tuning stages and uses a 20-step conjugate-gradient refit of its 512-entry FP16 LUT and Stage-I BlockAlign output alignment. The timing archives preserve matrix shapes and rate schedules and use our sm_120 RHT and state-indexed FP16 LUT GEMV implementation. QTIP quality and timing are retained records, outside the supplement's reconstruction commands.

YAQA [7], *Model-Preserving Adaptive Rounding*, computes both Kronecker factors in a single dataset pass with Sketch B. Its iterative Kronecker rounding uses dense output factors, which would have $151{,}936\times151{,}936$ entries for Qwen3 vocabulary matrices. We use diagonal output Fisher and closed-form row scales with a single input Cholesky factor. Block-relative distortion [8], vocabulary sensitivity [9], and temperature-aware evaluation [10] motivate the corresponding design choices. The lattice follows [11]. Related preconditioning and error correction include [12] [13] [14] [15] [16] [17] [18] [19] [20]. We study Qwen3 [21], including the tied-vocabulary setting explored independently in [22].

## 3. Theory and Method: Pre-Hadamard Row Scaling and Functional-Fisher Water-Filling

### 3.1 Post-RHT Frobenius Normalization and Proposition 1

QuIP [2] (Algorithm 1) introduced the fourth-root preconditioner

$$
D_{jj}=\left(\frac{H_{jj}}{(W^\top W)_{jj}}\right)^{1/4},
\qquad W\leftarrow WD,\qquad H\leftarrow D^{-1}HD^{-1}.
$$

Applying QuIP's construction to $W^\top$ with $H=\operatorname{diag}(\gamma)$ gives the pre-Hadamard row multiplier $(\gamma_i/u_i)^{1/4}$ and restoration scale $(u_i/\gamma_i)^{1/4}$ algebraically, where $u_i=\|W_{i,:}\|_2^2$.

Consider a linear projection $y = W x$ with weight matrix $W \in \mathbb{R}^{M \times K}$, input activation Gram $H_x = \mathbb{E}[x x^\top] \succeq 0$, and diagonal output functional Fisher sensitivity $\gamma_i = \mathbb{E}\bigl[(\partial \ell / \partial y_i)^2\bigr] > 0$ ($\Gamma_y = \operatorname{diag}(\gamma)$), where $\ell$ denotes next-token cross-entropy loss. Under diagonal pre-Hadamard output-row scaling by $s \in \mathbb{R}_{>0}^M$, we form the row-rescaled matrix $W' = \operatorname{diag}(s)^{-1} W$ ($W'_{i,:} = W_{i,:} / s_i$), apply two-sided RHT preconditioning with normalized orthogonal Hadamard matrices $H_M \in \mathbb{R}^{M \times M}$, $H_K \in \mathbb{R}^{K \times K}$ and independent Rademacher sign diagonals $S_v \in \{\pm 1\}^{M \times M}$, $S_u \in \{\pm 1\}^{K \times K}$,

$$
W_r(s) = H_M S_v \operatorname{diag}(s)^{-1} W S_u H_K^\top,
$$

quantize $W_r(s) \mapsto \widehat{W}_r(s)$ at nominal rate $R$ via right-to-left `BlockLDLQ` error feedback against $\tilde{H}_x = H_K S_u H_x S_u H_K^\top$, and reconstruct

$$
\widehat{W}(s) = \operatorname{diag}(s) S_v H_M^\top \widehat{W}_r(s) H_K S_u.
$$

Because $H_M S_v$ and $S_u H_K^\top$ are orthogonal, the Frobenius norm of $W_r(s)$ depends **solely on the Euclidean row norms** $u_i = \|W_{i,:}\|_2^2$:

$$
\|W_r(s)\|_F^2 = \|\operatorname{diag}(s)^{-1} W\|_F^2 = \sum_{i=1}^M \frac{\|W_{i,:}\|_2^2}{s_i^2} = \sum_{i=1}^M u_i s_i^{-2}.
$$

Frobenius-normalized RHT codecs such as QuIP# [3], QTIP [4], and Q4_BW16 [5] set their global matrix codebook scale $w_{\text{scale} }(s) \propto \|W_r(s)\|_F / \sqrt{M K}$. We state two modeling assumptions.
- **Assumption A1 (Isotropic Rotated Quantization Innovation under Frobenius Scaling):** After two-sided RHT mixing and `BlockLDLQ` error feedback at fixed rate $R$, the rotated reconstruction error $\Delta W_r(s) = \widehat{W}_r(s) - W_r(s)$ has zero mean and row-isotropic expected input-weighted energy conditional on the output signs proportional to $\|W_r(s)\|_F^2$:

$$
\mathbb{E}\!\left[\Delta W_r(s)\, \tilde{H}_x\, \Delta W_r(s)^\top\right] = \eta(R, H_x)\, \frac{\|W_r(s)\|_F^2}{M}\, I_M,
$$

where the rate-and-spectrum constant $\eta(R, H_x) > 0$ is independent of the left row scale $s$. This scale independence is an empirical high-rate modeling assumption.
- **Assumption A2 (Diagonal Output Kronecker-Fisher Surrogate):** The expected second-order loss perturbation of $W \mapsto \widehat{W}(s)$ is governed by $J_\Gamma(s) = \mathbb{E}\!\left[\operatorname{tr}\!\bigl(\operatorname{diag}(\gamma)\, \Delta W(s)\, H_x\, \Delta W(s)^\top\bigr)\right]$, where $\Delta W(s) = \widehat{W}(s) - W$.

**Proposition 1 (Conditional Pre-Hadamard Row-Scaling Optimal Ratio).** *Under Assumptions A1–A2, for any $s \in \mathbb{R}_{>0}^M$ with $u_i = \|W_{i,:}\|_2^2 > 0$ and $\gamma_i > 0$, the ratio of scaled to unscaled ($s = \mathbf{1}_M$) expected Kronecker-Fisher distortion is*

$$
c_\Gamma(s) \triangleq \frac{J_\Gamma(s)}{J_\Gamma(\mathbf{1}_M)} = \frac{\left(\sum_{i=1}^M \gamma_i s_i^2\right)\left(\sum_{i=1}^M u_i s_i^{-2}\right)}{\left(\sum_{i=1}^M \gamma_i\right)\left(\sum_{i=1}^M u_i\right)}.
$$

*Writing normalized distributions $\tilde{\gamma}_i = \gamma_i / \sum_{j=1}^M \gamma_j$ and $\tilde{u}_i = u_i / \sum_{j=1}^M u_j$, $c_\Gamma(s)$ is scale-invariant ($c_\Gamma(\alpha s) = c_\Gamma(s)$ for all $\alpha > 0$) and achieves its global minimum over $\mathbb{R}_{>0}^M$,*

$$
\rho_m \triangleq \min_{s \in \mathbb{R}_{>0}^M} c_\Gamma(s) = \left(\sum_{i=1}^M \sqrt{\tilde{\gamma}_i\, \tilde{u}_i}\right)^2 \le 1,
$$

*uniquely up to a positive scalar multiple at the post-GEMV restoration scale*

$$
s_i^\star \propto \left(\frac{\|W_{i,:}\|_2^2}{\gamma_i}\right)^{1/4} = \left(\frac{u_i}{\gamma_i}\right)^{1/4} \qquad \Longleftrightarrow \qquad (s_i^\star)^{-1} \propto \left(\frac{\gamma_i}{\|W_{i,:}\|_2^2}\right)^{1/4} = \left(\frac{\gamma_i}{u_i}\right)^{1/4},
$$

*where $(s_i^\star)^{-1}$ is the pre-Hadamard row multiplier applied in $W' = \operatorname{diag}(s)^{-1} W$, with strict improvement $\rho_m < 1$ whenever $u / \gamma$ is non-constant across rows. Moreover, if $0 < \kappa_{\min} \le \tilde{u}_i / \tilde{\gamma}_i \le \kappa_{\max}$ with condition ratio $\kappa = \kappa_{\max} / \kappa_{\min} \ge 1$, the Pólya–Szegő / Kantorovich inequality bounds $c_\Gamma(\mathbf{1}_M) / \rho_m \le \frac{(1 + \sqrt{\kappa})^2}{4\sqrt{\kappa} }$, i.e., $\rho_m \ge \frac{4\sqrt{\kappa} }{(1 + \sqrt{\kappa})^2}$.*

*Proof.* Substituting $\Delta W(s) = \operatorname{diag}(s) S_v H_M^\top \Delta W_r(s) H_K S_u$ into $J_\Gamma(s)$ and using $\tilde{H}_x = H_K S_u H_x S_u H_K^\top$ gives

$$
\begin{aligned}
J_\Gamma(s) &= \operatorname{tr}\!\left(\operatorname{diag}(\gamma)\operatorname{diag}(s)\, \mathbb{E}\!\left[S_v H_M^\top \Delta W_r(s)\, \tilde{H}_x\, \Delta W_r(s)^\top H_M S_v\right] \operatorname{diag}(s)\right) \\
&= \eta(R, H_x)\, \frac{\|W_r(s)\|_F^2}{M}\, \operatorname{tr}\!\left(\operatorname{diag}(\gamma)\operatorname{diag}(s)^2\right) = \frac{\eta(R, H_x)}{M} \left(\sum_{i=1}^M \gamma_i s_i^2\right)\left(\sum_{i=1}^M u_i s_i^{-2}\right),
\end{aligned}
$$

since $(S_v H_M^\top) I_M (H_M S_v) = I_M$. Dividing by $J_\Gamma(\mathbf{1}_M) = \frac{\eta(R, H_x)}{M}\bigl(\sum_i \gamma_i\bigr)\bigl(\sum_i u_i\bigr)$ yields $c_\Gamma(s) = \bigl(\sum_i \tilde{\gamma}_i s_i^2\bigr)\bigl(\sum_i \tilde{u}_i s_i^{-2}\bigr)$. By the Cauchy–Schwarz inequality applied to $a_i = \sqrt{\tilde{\gamma}_i}\, s_i$ and $b_i = \sqrt{\tilde{u}_i}\, s_i^{-1}$,

$$
\left(\sum_{i=1}^M \tilde{\gamma}_i s_i^2\right)\left(\sum_{i=1}^M \tilde{u}_i s_i^{-2}\right) \ge \left(\sum_{i=1}^M \sqrt{\tilde{\gamma}_i\, \tilde{u}_i}\right)^2 = \rho_m.
$$

Applying Cauchy–Schwarz to the normalized distributions also gives

$$
\rho_m \le \left(\sum_{i=1}^M \tilde{\gamma}_i\right)\left(\sum_{i=1}^M \tilde{u}_i\right) = 1,
$$

Equality in the lower bound holds if and only if $\sqrt{\tilde{\gamma}_i}\, s_i / (\sqrt{\tilde{u}_i}\, s_i^{-1}) = s_i^2 \sqrt{\tilde{\gamma}_i / \tilde{u}_i} = \text{const}$, i.e., $s_i^4 \propto u_i / \gamma_i \iff s_i \propto (u_i / \gamma_i)^{1/4}$, and $\rho_m<1$ unless $\tilde{\gamma} = \tilde{u}$. Applying Pólya–Szegő to positive weights $w_i = \sqrt{\tilde{\gamma}_i \tilde{u}_i}$ ($\sum_i w_i = \sqrt{\rho_m}$) and bounded scalars $x_i = \sqrt{\tilde{u}_i / \tilde{\gamma}_i} \in [\sqrt{\kappa_{\min} }, \sqrt{\kappa_{\max} }]$ yields $\frac{(\sum_i w_i x_i)(\sum_i w_i x_i^{-1})}{(\sum_i w_i)^2} = \frac{1}{\rho_m} \le \frac{(1 + \sqrt{\kappa})^2}{4\sqrt{\kappa} }$. $\square$

**When Input-Hessian Row Normalization ($v_i = \|W_{i,:}\|_{H_x}^2$) can regress.** Suppose instead one replaces $u_i$ by input-Hessian row energy $v_i = W_{i,:} H_x W_{i,:}^\top$, setting $s_i^{(v)} \propto (v_i / \gamma_i)^{1/4}$ (pre-Hadamard multiplier $(s_i^{(v)})^{-1} \propto (\gamma_i / v_i)^{1/4}$). Defining the normalized row-anisotropy ratio $\tilde{\alpha}_i = \tilde{v}_i / \tilde{u}_i$, substituting $s_i^{(v)} = (\tilde{v}_i / \tilde{\gamma}_i)^{1/4}$ into Proposition 1's true post-RHT distortion ratio gives

$$
c_\Gamma\!\bigl(s^{(v)}\bigr) = \left(\sum_{i=1}^M \sqrt{\tilde{\gamma}_i\, \tilde{v}_i}\right)\left(\sum_{i=1}^M \tilde{u}_i \sqrt{\frac{\tilde{\gamma}_i}{\tilde{v}_i} }\right) = \left(\sum_{i=1}^M \sqrt{\tilde{\gamma}_i\, \tilde{v}_i}\right)\left(\sum_{i=1}^M \sqrt{\tilde{\gamma}_i\, \tilde{v}_i}\, \tilde{\alpha}_i^{-1}\right).
$$

Whenever rows with large Euclidean weight norm $u_i$ experience cancellation along correlated directions of $H_x$ ($\tilde{\alpha}_i \ll 1$, so $\tilde{\alpha}_i^{-1} = \tilde{u}_i / \tilde{v}_i \gg 1$) while carrying non-negligible $\tilde{\gamma}_i$, the second sum over-amplifies $W'_{i,:} = W_{i,:} / s_i^{(v)}$ and inflates $\|W_r(s^{(v)})\|_F^2$ faster than the first sum shrinks output error, driving $c_\Gamma(s^{(v)}) > 1$ (a regression under the model) even while the mis-specified $v$-proxy falsely predicts gain $\bigl(\sum_i \sqrt{\tilde{\gamma}_i \tilde{v}_i}\bigr)^2 < 1$.

### 3.2 Structural Asymmetry: Output Row Separability vs. Input Column Non-Commutativity

A natural question is whether pre-Hadamard scaling should be applied symmetrically to both output rows ($s_v$) and input columns ($c_u$). This distinction determines when the encoder can share one input factor across scale variants.

**Proposition 2 (Output Row Separability vs. Input Column Non-Commutativity).** *Let $W' = \operatorname{diag}(s)^{-1} W C^{-1}$ with diagonal $s \in \mathbb{R}_{>0}^M$ and $C = \operatorname{diag}(c) \in \mathbb{R}_{>0}^K$.*
1. *(Output Row Separability): When $C = I_K$, the rotated input Gram $\tilde{H}_x = H_K S_u H_x S_u H_K^\top$ and its Cholesky/LDL decomposition $\tilde{H}_x + \lambda \bar{d} I_K = L D L^\top$ are **strictly independent of $s$**. Hence all candidate row-scale variants (`off`, `prose`, `mix`) share a single `BlockLDLQ` factorization and identical error-feedback filters $L$.*
2. *(Input Column Non-Commutativity): When $C \neq \alpha I_K$, the rotated input Gram becomes $\tilde{H}_x(C) = H_K S_u C H_x C S_u H_K^\top$. A non-scalar diagonal $C$ does not commute with $H_K$ ($[C, H_K] \neq 0$), and $\tilde{H}_x(C)$ is generally not a scalar multiple of $\tilde{H}_x(I_K)$. Its BlockLDLQ factors $(L,D)$ therefore generally require refactorization. For $H_x=\operatorname{diag}(1,4)$, $C=\operatorname{diag}(2,1/2)$, and the normalized $H_2$, the LDL pivots $D$ are unchanged while the off-diagonal feedback sign in $L$ flips. The post-RHT Frobenius norm squared becomes $\|W C^{-1}\|_F^2 = \sum_{j=1}^K \|W_{:,j}\|_2^2 c_j^{-2}$.*

The supplement checks the normalizer mismatch with a $2\times2$ analytic counterexample. A separate CPU test runs production RHT and BlockLDLQ preparation on a 1,024-wide matrix and checks bit identity of the input factors across off, prose and mixed row scales. Section 5.1 reports the retained GPU experiments.

### 3.3 Functional-Fisher calibration and byte allocation

**Calibration and scale selection.** The prose subsets $D_{\rm tr}$ and $D_{\rm val}$ each contain 16 windows and are disjoint. Their input Grams are $H_{\rm tr}$ and $H_{\rm val}$. Mixed calibration also collects $(\gamma_{\rm math}, H_{\rm math})$ at generated positions in 128 dense, greedy 8-shot rollouts from GSM8K training rows 0–127. For the prose scale we fit on $\gamma_{\rm tr}$ and select on $\gamma_{\rm val}$. For the mixed scale we fit on $(\gamma_{\rm tr}+\gamma_{\rm math})/2$ and select on $(\gamma_{\rm val}+\gamma_{\rm math})/2$. Both mixed halves share the same math moments.

With two categorical draws $z_{t,k}\sim p_\theta(\cdot\mid h_t)$ at each of $N_{\rm tok}$ valid predicting positions, let $\ell_k=\sum_t\log p_\theta(z_{t,k}\mid h_t)$. The implemented collector accumulates

$$
\begin{aligned}
\hat\gamma_i^{(m)}&=\frac{\sum_{k,\tau}(\partial\ell_k/\partial y_{\tau,i}^{(m)})^2}{N_{\rm tok}K_s},\\
\hat\gamma_v^{\rm head}&=\frac{\sum_t p_{t,v}(1-p_{t,v})}{N_{\rm tok}},\\
\hat\gamma_v^{\rm emb}&=\frac{\sum_k\sum_{\tau:\mathrm{id}_\tau=v}\|\nabla_{h_{0,\tau}}\ell_k\|_2^2}{N_{\rm tok}K_s d}.
\end{aligned}
$$

Each backward pass sums scores over predicting positions before squaring activation gradients, including possible contributions from later positions. Cross-score terms vanish in expectation under independent conditional draws, giving an unbiased estimate of the per-position score-square sum up to BF16 score rounding and backward accumulation. For lookup $h_{0,\tau}=E_{\mathrm{id}_\tau,:}$, division by $d$ gives the per-coordinate sensitivity under isotropic embedding-gradient directions and $H_x^{\rm emb}=I_d$.

We add $\epsilon$ times the row mean to each of $u$ and the training Fisher, form $(u_i/\gamma_i)^{\tau/4}$ from these regularized values, and center the log scales by their mean. We clip them to $[-\ln 8,\ln 8]$, recenter, exponentiate, and store the restoration scales with their output Hadamard signs in FP16. The selector minimizes Proposition 1's ratio on the designated selection Fisher and the rounded scale magnitudes, comparing $\tau\in\{0.25,0.50,0.75,1\}$ and $\epsilon\in\{10^{-4},10^{-3},10^{-2}\}$ with the identity. This step requires zero quantization passes.

**Calibration scoring surrogate.** All $\widehat J$ are per-token nats under the surrogate. For $e_i=\Delta W_{i,:}$, the pure-prose body score is $\widehat J_m^{\rm prose}=\frac12\sum_i\hat\gamma_i^{\rm prose,val}e_iH_x^{\rm prose,val}e_i^\top$. The mixed score is

$$
\widehat J_m^{\rm mix}=\tfrac12(\widehat J_m^{\rm prose}+\widehat J_m^{\rm math})
=\tfrac14\sum_i\left[\hat\gamma_i^{\rm prose,val}e_iH_x^{\rm prose,val}e_i^\top+
\hat\gamma_i^{\rm math}e_iH_x^{\rm math}e_i^\top\right].
$$

$H_{\rm prose}=(H_{\rm tr}+H_{\rm val})/2$ supplies the prose encoding Gram. Thus $H_{\rm val}$ contributes to encoding and scoring, while $(\gamma_{\rm math},H_{\rm math})$ is shared between the mixed-domain fit and score. Mixed encoding uses the equal-weight mean of prose and math Grams after dividing each by its mean diagonal. The supplement follows [6] and selects down-projection damping $\lambda\in\{0.001,0.01,0.03,0.1,0.3\}$ on the rotated training versus prose validation Grams in descending encoder column order. The mixed selector uses a trace-balanced mixture of the prose training and math Grams on the training side. The retained mixed full-model builds used the subset $\{0.01,0.03,0.1,0.3\}$. Other body projections use $\lambda=0.01$.

The untied 8B embedding uses $I_d$, and the untied readout uses its post-RMSNorm hidden Gram $H_{\rm head}$. The tied 4B vocabulary, $E\in\mathbb R^{151936\times2560}$, uses $\tilde H_{\rm head}=\frac12H_{\rm head}^{\rm tr}/\overline{\operatorname{diag}(H_{\rm head}^{\rm tr})}+\frac12 I_d$ for candidate encoding. Its training row Fisher is $\gamma_v^{\rm tied,tr}=\overline{\operatorname{diag}(H_{\rm head}^{\rm tr})}\hat\gamma_v^{\rm head,tr}+\hat\gamma_v^{\rm emb,tr}$, with the analogous validation Fisher used to select shrinkage. In each scoring domain $\mathcal D$, $N_{\mathcal D}$ counts predicting positions and the score accounts for the readout and lookup roles.

$$
\widehat J_{\rm tied}^{\mathcal D}=\frac1{N_{\mathcal D}}\sum_{t\in\mathcal D}
\operatorname{KL}(\operatorname{softmax}(Eh_t)\,\|\,\operatorname{softmax}(\widehat E h_t))
+\tfrac12\sum_v\hat\gamma_v^{\rm emb,\mathcal D}\|\widehat E_v-E_v\|_2^2.
$$

Pure-prose scoring uses $D_{\rm val}$. Mixed scoring averages this score with the math-rollout score, $\widehat J_{\rm tied}^{\rm mix}=(\widehat J_{\rm tied}^{\rm prose}+\widehat J_{\rm tied}^{\rm math})/2$. Final mixed 4B export re-encodes the selected tied option using an equal-weight trace-balanced mixture of the pooled prose and math readout Grams, blended 50:50 with $I_d$. An independent tied-4B ablation [22] measured $-0.01214$ nats KL from readout scoring and $-0.000039$ nats from lookup-only calibration. Our method adds functional-Fisher scaling on the 151,936 vocabulary rows and co-allocates body and vocabulary rates.

**Candidate sets and export.** The body rate set is $\{2.125,2.250,2.500,3.000\}$ bpw (Table 1). The standalone 4B sweep considers off, prose and mixed scales when math data are available. It encodes an FP16-scale body option only if its prose selection Fisher predicts a gain of at least 0.30 dB. The pure-prose allocation admits off and prose options, and the mixed allocation admits off and mixed options. The unrestricted 504-matrix tests in §5.1 apply no eligibility filter. The 8B mixed sweep admits off and mixed scales at all four rates, for eight options per body matrix. Embeddings on 8B also have eight options. The tied 4B vocabulary and untied 8B head have six each at rates 2.250, 2.500 and 3.000 bpw, with or without FP16 row scales.

**Table 1. The four BW16 rate options.**

| Rate code | Bits per weight | Shell cap | Lattice cardinality (bits) | States with occupancy bits | Packed layout | Device LUT |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **`rc17`** | $2.125$ | $13$ | $4{,}026{,}639{,}841$ ($31.907\text{ b}$) | $16{,}106{,}559{,}364$ ($32+2\text{ b}$, $93.75\%$) | $8.5\text{ B}/32\text{w}$ (`17 B` per $64\text{w}$ superpacket) | Reuses $K_{\max}=22$ (`42.7 KB`) |
| **`rc18`** | $2.250$ | $15$ | $12{,}225{,}158{,}881$ ($33.509\text{ b}$) | $48{,}900{,}635{,}524$ ($34+2\text{ b}$, $71.16\%$) | $4.5\text{ B}/16\text{w}$ (`9 B` per $32\text{w}$ pair) | Reuses $K_{\max}=22$ (`42.7 KB`) |
| **`rc20`** | $2.500$ | $22$ | $248{,}874{,}804{,}961$ ($37.857\text{ b}$) | $995{,}499{,}219{,}844$ ($38+2\text{ b}$, $90.54\%$) | $5.0\text{ B}/16\text{w}$ (`u32 + u8`) | $42{,}660\text{ B}$ (`V8`) |
| **`rc24`** | $3.000$ | $45$ | $68{,}713{,}032{,}753{,}121$ ($45.966\text{ b}$) | $274{,}852{,}131{,}012{,}484$ ($46+2\text{ b}$, $97.65\%$) | $6.0\text{ B}/16\text{w}$ (`u32 + u16`) | $135{,}576\text{ B}$ (`V8`) |

The 4B body table is scored on encodings using $(H_{\rm prose},\lambda=0.01)$. The exported mixed-domain damped arm re-encodes its chosen rates and scales using the trace-balanced mixed Gram and selected down-projection damping. The 8B mixed candidate table scores body encodings using the same mixed input metric and damping as export.

For rate $b(r)$ in bits per weight and scale variant $\nu$, the logical matrix byte cost is

$$
B_m(r,\nu)=M_m K_m b(r)/8+b_{\rm meta}(m)+2M_m\mathbf{1}[\nu\ne\mathrm{off}].
$$

The header is 20 bytes for every body projection and both untied 8B vocabulary matrices. The tied 4B vocabulary header is 24 bytes and stores separate embedding and readout scalar scales. Complete-package bytes also include retained BF16 normalization parameters. The packed runtime applies the signed FP16 row scales after GEMV or during inverse RHT.

**Exact byte allocation.** Set $F_0(0)=0$ and $F_0(u>0)=+\infty$. For group $g$ let $\delta_g(o)=(B_g(o)-B_g^{\min})/\Delta$. Then

$$
F_g(u)=\min_{o\in\mathcal O_g:\delta_g(o)\le u}
[F_{g-1}(u-\delta_g(o))+\widehat J_g(o)].
$$

The minimum over reachable final capacities gives the solution, and backtracking recovers the options. Every 4B body and tied-vocabulary increment is divisible by $\Delta=256$ bytes. The 8B body costs are multiples of $q=2{,}048$ bytes for $M_m\in\{1024,4096,12288\}$ and $K_m\in\{4096,12288\}$. The eight embedding options and six head options form one 48-option group. With $B_{\rm rem}$ the cap after fixed bytes, its pair $(e,h)$ consumes

$$
\Delta u(e,h)=\left\lfloor B_{\rm rem}/q\right\rfloor-
\left\lfloor(B_{\rm rem}-B_{\rm emb}(e)-B_{\rm head}(h))/q\right\rfloor.
$$

Subtracting this charge leaves exactly the feasible body capacity of the original byte problem for each pair. The dynamic program therefore has zero approximation gap on the scored candidate surrogate table. Export re-encoding and output alignment can change the losses of those candidates.

**Stage-I BlockAlign.** After allocation and encoding, sequential layer-wise forward passes fit scalar multipliers for value, attention output, gate, up and down projections. The fit clips its components to $[0.92,1.08]$ and absorbs the resulting multiplier into each projection's scalar weight scale at zero extra bytes.

**Algorithm 1. Functional-Fisher allocation and export**

1. Collect prose training and validation Fishers and Grams. For mixed calibration collect one math rollout pool and reuse its moments on both sides of scale selection.
2. Select the signed FP16 scales with Proposition 1 on the prose or mixed Fishers. Compute input Grams and select trace-ratio damping for down projections.
3. Score eligible rate and scale options using the calibration scoring surrogate. On 4B consider off, prose and mixed scales with a 0.30 dB eligibility threshold for scaled body options. On 8B consider off and mixed at every body rate. Use pooled prose with 0.01 damping for the 4B body sweep and mixed inputs with selected damping for the 8B body sweep. Reuse the input factor across scales within each sweep.
4. Solve the byte-constrained dynamic program exactly on the scored surrogate table, then encode the selected schedule with the export metrics.
5. Apply sequential Stage-I BlockAlign, fit the student temperature on the designated calibration windows, and export the packed archive.

## 4. Experimental protocol

We use pinned BF16 Qwen3-4B and Qwen3-8B [21] checkpoints on one RTX 5090 with PyTorch 2.8.0+cu128 and Transformers 5.6.2. The frozen calibration manifest selects 16 windows for $D_{\rm tr}$ (IDs 0–7 and 64–71) and 16 for $D_{\rm val}$ (IDs 8–15 and 72–79). Each contains 2,048 tokens. Mixed calibration uses dense greedy 8-shot rollouts on GSM8K training rows 0–127. Rows 128–255 of the training split are reserved and unused by the build. Both mixed Fisher halves reuse the same math traces, and $H_{\rm val}$ is half of the pooled prose encoding Gram. The schedule gate uses distinct blind prose windows.

Downstream WT2-32, C4-32, standard WikiText-2 and C4, ARC-Challenge, GSM8K-256, GSM8K-Holdout-1024, and blind F3 use evaluation sets separate from the prose and math calibration sets. The supplement checks retained dataset identifiers, token digests where available, and GSM8K prompt overlap. WT2-32 and C4-32 each evaluate 65,504 next-token targets. Standard perplexity uses 146 WikiText-2 and 256 C4 windows.

GSM8K-Holdout-1024 is from the official openai/gsm8k **training split**, rows 1000–2023, disjoint from rows 0–127, reserved rows 128–255, and the synthetic 8-shot prompt exemplars. Exposure during Qwen3 pretraining or post-training remains possible. We also evaluate official test rows 128–383 (GSM8K-256), whose first 64 rows double as the loader check, and report independent blind F3. GSM8K uses greedy 8-shot decoding with a 256-token cap. ARC-Challenge uses continuation likelihood normalized by byte length.

Quality results in Tables 2–4 and 6 use BF16-unpacked weights (packed=False) and dense BF16 KV. Table 5 measures live runtime and memory, including RotateKV. Both packed 2.250-bpw FFWF packages pass the $<0.01$-nat WT2-32 Fit-NLL parity gate. On 4B, the packed and unpacked means are 2.5517 and 2.5463, a displayed difference of $+0.0054$ nats (about 17% of the magnitude of the $-0.0317$-nat combined Teacher-KL delta, which measures a different quantity). On 8B, their means are 2.30934479 and 2.30715007, a difference of $+0.00219473$ nats.

Paired percentile intervals use 10,000 bootstrap draws with seed 20261707. Binary comparisons use two-sided exact McNemar tests and Holm–Bonferroni adjustment within primary contrast families.

The QTIP-HYB comparison uses the 20-step FP16 LUT refit and Stage-I BlockAlign detailed in §2 and omits end-to-end recovery fine-tuning. Its quality and custom-kernel timing measurements are retained records.

The teacher uses $T_{\rm teacher}=1$. The scalar $T^\star_{\rm student}>0$ minimizes $-\sum_t\log\operatorname{softmax}(z_t^{\rm quant}/T)_{y_t}$ on a 41-point grid from 0.8 to 1.6, fitted on predicting positions in calibration windows 0, 1, 64 and 65. Held-out Fit-NLL uses this scalar. Raw perplexity and the retained Teacher-KL use unit student temperature, with Teacher-KL computed as $\operatorname{KL}(\operatorname{softmax}(z_t^{\rm dense})\,\|\,\operatorname{softmax}(z_t^{\rm quant}))$. The evaluator also reports fitted KL using $\operatorname{softmax}(z_t^{\rm quant}/T^\star_{\rm student})$ for the student.

## 5. Results

### 5.1 Matrix-level tests and normalizer replay

![Figure 1. Predicted and realized Fisher gain, domain and codec transfer, and gain by projection family.](supplement/figure-1.png)

At the measured rates all 504 body matrices improved. Mean realized gains were 1.020 dB on Qwen3-4B and 0.916 dB on Qwen3-8B. The three vocabulary gains range from 3.01 to 7.78 dB. For the main body comparisons and QTIP-HYB, $r=0.9984$–$0.9998$ and MAE is 0.045–0.085 dB. The 252 unseen-math comparisons give $r=0.9946$. These are tests of the empirical scale independence in A1. Proposition 2 establishes algebraic input-factor invariance independently.

At 2.25 bpw, a controlled single-pass experiment compared the input-Gram energy $v_i=\|W_{i,:}\|_{H_x}^2$ and Euclidean energy $u_i=\|W_{i,:}\|_2^2$ on identical $(\gamma_{\rm tr},\gamma_{\rm val},H_{\rm tr},H_{\rm val})$ for the 42 matrices in layers 0–5 of Qwen3-4B (Figure 1a). Both used mean-centered scales. The $v$ search used $\tau\in\{0.5,0.75,1.0\}$ and the $u$ search also included 0.25. With $v$, 14 of 42 matrices regressed. Predicted gain averaged $+2.470$ dB under the $v$ proxy, compared with $+0.353$ dB realized (minimum $-1.829$ dB). Evaluating the same $v$ scales in Proposition 1 with Euclidean energy predicts $+0.383$ dB. With $u$, predicted and realized gains averaged $+0.982$ and $+0.905$ dB, with zero regressions and a minimum of $+0.020$ dB.

The within-process determinism check repeated all 42 scale fits and, on seven matrices, packet encoding and BF16 reconstruction. Maximum difference was 0.0 and no checks failed at tolerance $10^{-12}$. An earlier median-normalized diagnostic compared separate runs with differences up to $2.18\times10^{-3}$. In a separate three-seed Fisher resampling check with fixed Grams, the mean absolute factor difference was 0.00955 for $u$ and 0.02066 for $v$. This measures sensitivity to Fisher resampling. The cause of the earlier cross-run drift was not isolated. Appendix A records both procedures.

### 5.2 Factorials and calibration controls

Figure 2 and Tables 2–4 report complete-package comparisons, two-factor effects and the separate 4B input controls. The indices of $y_{ij}$ encode the input and output factors, respectively. On 4B, $(y_{00}, y_{10}, y_{01}, y_{11})$ are `BW16_2250`, `BW16_MixHx_Damp_2250`, `FFWF_BW16_ProseHx_2250`, and `FFWF_BW16_MixHx_Damp_2250`. On 8B they are `BW16_8B_2250_V2`, `BW16_8B_MixHx_Damp_2250`, `FFWF_BW16_8B_ProseHx_2250`, and `FFWF_BW16_8B_2250`. The interaction is $I_{2\times2}=(y_{11}-y_{10})-(y_{01}-y_{00})$.

![Figure 2. English Teacher-KL and GSM8K accuracy across the factorials and 4B input controls.](supplement/figure-2.png)

**Table 2. Model quality and complete-package bytes.**

| Model and package | Logical bytes (difference from cap) | $T^\star$ | WT2-32 KL / Fit-NLL | C4-32 KL / Fit-NLL | Standard WT2 / C4 PPL | ARC-C (%) | GSM8K-256 (%) | GSM8K-Holdout-1024 (%, $p_{\rm HB}$ where indicated) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Qwen3-4B` Dense `BF16`** | $8{,}044{,}876{,}800\text{ B}$ | $1.28$ | $0.0000$ / $2.3913$ | $0.0000$ / $2.8645$ | **$13.66$ / $15.25$** | $54.01$ | $89.06$ ($228$) | $92.29\%$ ($945/1024$) |
| `BW16_2250` (Prose $H_x$, `sv=off`) | $1{,}168{,}125{,}896\text{ B}$ ($0\text{ B}$) | $1.22$ | $0.2723$ / $2.5703$ | $0.2705$ / $3.0606$ | $16.14$ / $17.62$ | $45.48$ | $67.58$ ($173$) | $72.17\%$ ($739$, baseline) |
| `QTIP_HYB_2250` (Prose $H_x$, `sv=off`) | $1{,}168{,}146{,}440\text{ B}$ ($+20.5\text{ KB}$) | $1.22$ | $0.2718$ / $2.5753$ | $0.2641$ / $3.0576$ | $15.95$ / $17.54$ | $46.42$ | $66.80$ ($171$) | $71.00\%$ ($727$, trellis base) |
| `Fisher_QTIP_HYB_2250` (`sv=off`, $0$ math) | $1{,}168{,}146{,}440\text{ B}$ ($0\text{ B}$ vs HYB) | $1.28$ | $0.2604$ / $2.5684$ | $0.2568$ / $3.0634$ | — | $43.43$ | $67.19$ ($172$) | $74.51\%$ ($763$, $+3.52\text{ pp}$, $p_{\text{HB} }=0.029$) |
| **`Fisher_QTIP_HYB_BodySvOn_2250`** ($0$ math) | $1{,}168{,}146{,}440\text{ B}$ ($0\text{ B}$ vs HYB) | $1.32$ | **$0.2389$ / $2.5443$** | **$0.2348$ / $3.0489$** | $16.16$ / $17.35$ | $43.17$ | $64.06$ ($164$) | $64.75\%$ ($663$, $-6.25\text{ pp}$, $p_{\text{HB} }=0.0011$) |
| **`FFWF_QTIP_HYB_PureProse_2250`** ($0$ math) | $1{,}168{,}120{,}584\text{ B}$ ($-25{,}856\text{ B}$ vs HYB) | $1.28$ | **$0.2263$ / $2.5405$** | **$0.2239$ / $3.0421$** | **$15.68$ / $17.03$** | $45.48$ | **$69.53$ ($178$)** | $66.41\%$ ($680$, $-4.59\text{ pp}$, $p_{\text{HB} }=0.014$) |
| **`FFWF_BW16_PureProse_Damp_2250`** ($0$ math) | $1{,}168{,}120{,}008\text{ B}$ ($-5{,}888\text{ B}$) | $1.28$ | **$0.2217$ / $2.5232$** | **$0.2260$ / $3.0422$** | — | $45.56$ | $70.31$ ($180$) | $73.93\%$ ($757$) |
| `BW16_MixHx_Damp_2250` (`sv=off`) | $1{,}168{,}125{,}896\text{ B}$ ($0\text{ B}$) | $1.28$ | $0.2931$ / $2.5743$ | $0.2827$ / $3.0746$ | — | $46.67$ | $82.03$ ($210$) | $83.20\%$ ($852$) |
| **`FFWF_BW16_MixHx_Damp_2250`** | $1{,}168{,}122{,}568\text{ B}$ ($-3{,}328\text{ B}$) | $1.26$ | **$0.2406$ / $2.5463$** | **$0.2380$ / $3.0478$** | **$15.42$ / $17.03$** | **$47.18$** | **$84.38$ ($216$)** | **$83.98\%$ ($860$, $+11.82\text{ pp}$, $p_{\text{HB} }=2.2\times 10^{-16}$)** |
| `BW16_2685` (Prose $H_x$, `sv=off`) | $1{,}365{,}307{,}336\text{ B}$ ($0\text{ B}$) | $1.24$ | $0.1583$ / $2.4890$ | $0.1514$ / $2.9709$ | — | $48.72$ | $82.81$ ($212$) | $85.45\%$ ($875$, `2.685` base) |
| **`FFWF_BW16_MixHx_Damp_2685`** | $1{,}365{,}293{,}768\text{ B}$ ($-13{,}568\text{ B}$) | $1.28$ | **$0.1372$ / $2.4756$** | **$0.1302$ / $2.9597$** | — | **$51.11$** | **$89.06$ ($228$)** | **$88.96\%$ ($911$, $+3.52\text{ pp}$, $p=0.0011$)** |
| **`Qwen3-8B` Dense `BF16`** | $16{,}381{,}376{,}512\text{ B}$ | $1.24$ | $0.0000$ / $2.1745$ | $0.0000$ / $2.6725$ | **$9.73$ / $12.30$** | $56.40$ | $89.84$ ($230$) | $92.38\%$ ($946/1024$) |
| `BW16_8B_2250_V2` (`sv=off`) | $2{,}381{,}970{,}392\text{ B}$ ($0\text{ B}$) | $1.22$ | $0.2092$ / $2.3066$ | $0.2005$ / $2.8300$ | $11.18$ / $13.79$ | $52.47$ | $80.08$ ($205$) | $82.03\%$ ($840$, `8B` `2.250` base) |
| `BW16_8B_2250_CausalAsymGN_V2` | $2{,}381{,}970{,}392\text{ B}$ ($0\text{ B}$) | $1.26$ | $0.2048$ / $2.3085$ | $0.1965$ / $2.8316$ | $11.37$ / $13.95$ | $52.39$ | $79.69$ ($204$) | $83.11\%$ ($851$, asym-Cholesky base) |
| `BW16_8B_MixHx_Damp_2250` (`sv=off`) | $2{,}381{,}970{,}392\text{ B}$ ($0\text{ B}$) | $1.22$ | $0.2224$ / $2.3193$ | $0.2085$ / $2.8377$ | $11.20$ / $13.81$ | — | $88.67$ ($227$) | $87.89\%$ ($900$, $+5.86\text{ pp}$ vs V2, $p=4.14 \times 10^{-7}$) |
| **`FFWF_BW16_8B_ProseHx_2250`** | $2{,}381{,}947{,}352\text{ B}$ ($-23{,}040\text{ B}$) | $1.22$ | **$0.1824$ / $2.2980$** | **$0.1731$ / $2.8124$** | **$10.90$ / $13.53$** | — | $81.25$ ($208$) | $81.74\%$ ($837$, $-0.29\text{ pp}$ vs V2, $p=0.877$) |
| **`FFWF_BW16_8B_2250`** (`MixHx + Damp`) | $2{,}381{,}947{,}352\text{ B}$ ($-23{,}040\text{ B}$) | $1.22$ | **$0.1949$ / $2.3072$** | **$0.1845$ / $2.8251$** | **$11.09$ / $13.68$** | $52.05$ | **$85.55$ ($219$)** | **$86.82\%$ ($889$, $+4.79\text{ pp}$, $p_{\text{HB} }=1.7\times 10^{-4}$)** |
| `BW16_8B_2685_V2` (`sv=off`) | $2{,}759{,}457{,}752\text{ B}$ ($0\text{ B}$) | $1.22$ | $0.1152$ / $2.2430$ | $0.1079$ / $2.7580$ | $10.42$ / $13.06$ | $55.12$ | $88.67$ ($227$) | $87.30\%$ ($894$, `8B` `2.685` base) |
| **`FFWF_BW16_8B_2685`** (`MixHx + Damp`) | $2{,}759{,}418{,}328\text{ B}$ ($-39{,}424\text{ B}$) | $1.22$ | **$0.0969$ / $2.2341$** | **$0.0900$ / $2.7454$** | **$10.28$ / $12.87$** | $54.61$ | **$89.45$ ($229$)** | **$90.82\%$ ($930$, $+3.52\text{ pp}$, $p_{\text{HB} }=9.4\times 10^{-4}$)** |

**Table 3. Matched-byte factorial contrasts at 2.250 bpw.**

| Contrast | 4B WT2-32 $\Delta$KL | 4B C4-32 $\Delta$KL | 4B GSM8K $\Delta$accuracy | 8B WT2-32 $\Delta$KL | 8B C4-32 $\Delta$KL | 8B GSM8K $\Delta$accuracy |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Input Axis (`MixHx+Damp` vs `ProseHx`, `sv=off`)** | $+0.0208$ $[+0.0153, +0.0269]$ | $+0.0122$ $[+0.0073, +0.0169]$ | **$+11.04\text{ pp}$** ($167:54$) | $+0.0131$ $[+0.0085, +0.0182]$ | $+0.0080$ $[+0.0023, +0.0135]$ | $+5.86\text{ pp}$ ($100:40$) |
| **Output Axis (`FFWF+sv` vs `Uniform`, `ProseHx`)** | **$-0.0453$** $[-0.0504, -0.0402]$ | **$-0.0413$** $[-0.0473, -0.0356]$ | $+2.73\text{ pp}$ ($138:110$, $p=0.086$) | $-0.0269$ $[-0.0316, -0.0223]$ | $-0.0274$ $[-0.0317, -0.0232]$ | $-0.29\text{ pp}$ ($82:85$, $p=0.877$) |
| **Output Axis (`FFWF+sv` vs `Uniform`, `MixHx+Damp`)** | **$-0.0525$** $[-0.0589, -0.0466]$ | **$-0.0447$** $[-0.0500, -0.0388]$ | $+0.78\text{ pp}$ ($84:76$, $p=0.580$) | $-0.0275$ $[-0.0352, -0.0162]$ | $-0.0240$ $[-0.0321, -0.0124]$ | $-1.07\text{ pp}$ ($48:59$, $p=0.334$) |
| **Combined ($y_{11}$ vs $y_{00}$)** | **$-0.0317$** $[-0.0370, -0.0269]$ | **$-0.0325$** $[-0.0379, -0.0274]$ | **$+11.82\text{ pp}$** ($169:48$) | **$-0.0144$** $[-0.0232, -0.0006]$ | **$-0.0160$** $[-0.0250, -0.0022]$ | **$+4.79\text{ pp}$** ($97:48$) |
| **Interaction $I_{2\times 2}$ (`Output` $\times$ `Input`)** | $-0.0072$ $[-0.0155, +0.0004]$ | $-0.0034$ $[-0.0099, +0.0031]$ | $-1.95\text{ pp}$ $[-5.86, +2.05]$ | $-0.0006$ $[-0.0094, +0.0105]$ | $+0.0034$ $[-0.0051, +0.0137]$ | $-0.78\text{ pp}$ $[-3.91, +2.44]$ |

With row scales off, MixHx + Damp raises GSM8K-Holdout-1024 from 739 to 852 correct at 4B and from 840 to 900 at 8B. WT2-32/C4-32 Teacher-KL rises by 0.0208/0.0122 nats at 4B and 0.0131/0.0080 at 8B. FFWF + FP16 row scaling lowers English KL in both input regimes. At 4B the decreases are 0.0453/0.0413 nats with prose inputs and 0.0525/0.0447 with mixed inputs and damping. At 8B the decreases are 0.0269/0.0274 and 0.0275/0.0240 nats. The corresponding 8B GSM8K changes are unresolved ($-0.29$ pp, $p=0.877$ and $-1.07$ pp, $p=0.334$). All six $2\times 2$ interaction intervals across both model sizes and the three panels include zero. For 4B WT2-32, $I_{2\times 2}=-0.0072$ nats with a 95% CI of $[-0.0155, +0.0004]$. The results are consistent with approximately additive input-domain and output-Fisher effects, with no statistically resolved interaction.

Standard perplexity (146 WikiText-2 and 256 C4 windows) decreases from 11.20/13.81 to 11.09/13.68 when adding FFWF and row scales to the 8B MixHx + Damp control. On 4B it decreases from 16.14/17.62 for uniform prose BW16 to 15.42/17.03 for mixed-domain damped FFWF. Standard perplexity was unmeasured for the 4B uniform mixed-domain damped control.

In the zero-math QTIP-HYB sequence, English Teacher-KL decreases with Fisher allocation and row scaling (Table 2). GSM8K-Holdout-1024 accuracy drops on the two row-scaled arms. Their schedules assign 20–24 of 36 down projections and 24–30 of 36 up or gate projections to $KV=4$ (2.000 bpw). These counts are observed rate-allocation correlates accompanying the accuracy drop. Establishing causality would require a targeted rate-floor intervention.

**Table 4. Single-axis 4B calibration controls at 2.250 bpw.**

| Control | Fisher and row scaling | Input Gram | Down-projection $\lambda$ | Math calibration tokens | WT2-32 / C4-32 KL | ARC-C (%) | GSM8K-Holdout-1024 (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BW16_2250` (Baseline) | Uniform, `sv=off` | `ProseHx` | $0.01$ | $0$ | $0.2723$ / $0.2705$ | $45.48$ | $72.17\%$ ($739$) |
| **`FFWF_BW16_PureProse_NoDamp_2250`** | Prose `FFWF+sv` | `ProseHx` | $0.01$ | **$0$** | $0.2256$ / $0.2306$ | $41.89$ | $70.61\%$ ($723$) |
| **`FFWF_BW16_PureProse_Damp_2250`** | Prose `FFWF+sv` | `ProseHx` | **Trace-Ratio ($0.30$ on $26/36$)** | **$0$** | **$0.2217$ / $0.2260$** | $45.56$ | **$73.93\%$** ($757$; $+3.32\text{ pp}$ vs NoDamp, $122:88$, $p=0.0225$) |
| `FFWF_BW16_ProseHx_2250` | Mixed `FFWF+sv` | `ProseHx` | $0.01$ | $14{,}192$ (Fisher only) | $0.2270$ / $0.2292$ | $46.16$ | $74.90\%$ ($767$) |
| **`FFWF_BW16_MixHx_NoDamp_2250`** | Mixed `FFWF+sv` | **`MixHx`** | $0.01$ | $14{,}192$ | $0.2440$ / $0.2452$ | $43.94$ | **$85.55\%$** ($876$; $+10.64\text{ pp}$ vs ProseHx, $155:46$, $p=5.3\times 10^{-15}$) |
| **`FFWF_BW16_MixHx_Damp_2250`** | Mixed `FFWF+sv` | **`MixHx`** | **Trace-Ratio ($0.30$ on $26/36$)** | $14{,}192$ | $0.2406$ / $0.2380$ | **$47.18$** | **$83.98\%$** ($860$; $-1.56\text{ pp}$ vs NoDamp, $46:62$, $p=0.149$) |

In the zero-math 4B control, adding down-projection damping to pure-prose FFWF changes WT2-32/C4-32 Teacher-KL by $-0.0039/-0.0046$ nats, ARC-Challenge by $+3.67$ pp and GSM8K-Holdout-1024 by $+3.32$ pp (122:88 discordants, unadjusted exact McNemar $p=0.0225$). With damping fixed at 0.01, switching from prose to mixed Grams at the same mixed Fisher schedule increases GSM8K-Holdout-1024 by 10.64 pp. Adding damping to the mixed arm improves English KL and ARC-Challenge, with an unresolved $-1.56$ pp change in GSM8K-Holdout-1024 ($p=0.149$).

### 5.3 Independent blind F3 evaluation

The independent evaluator [23] used 512 MATH level-4–5 items, greedy 4-shot decoding and a 1,024-token cap. Dense BF16 scored 276/512, with 64/64 loader parity. The evaluator froze predicted score ranges of 175–200 correct for the 2.250-bpw package and 238–252 for the 2.685-bpw package before running the blind panel.

FFWF 8B at 2.250 bpw scored **195/512**, or 0.707 of dense, inside its predicted range. It scored 51 more than equal-byte CausalAsymGN 2.25 + V2 (86:35 discordants, exact $p\approx4\times10^{-6}$). FFWF 8B at 2.685 bpw scored **256/512**, or 0.928 of dense, above its predicted range. It scored 30 more than BW16 2.5 + G (67:37, exact $p=0.004$). Differences from 3.17 GB, 3.0-bpw QTIP L16 ($p=0.43$) and 3.0-bpw BW16 ($p=0.61$) were unresolved. F3 evaluates the combined packages. In the separate factorials, MixHx + Damp accounts for most of the GSM8K gain and FFWF + FP16 row scaling recovers the English Teacher-KL penalty in both models and the measured perplexity penalty on 8B.

### 5.4 Bounded discrete polishing

GS-DLD adds two block-64 Gauss–Seidel coordinate sweeps and a $4\times4$ LUT polishing pass to the mixed-domain damped 4B FFWF arm. The bounded run accepted updates on 252/252 matrices and stopped at its sweep limit without full neighborhood convergence. It gained $+0.0796$ dB for 1,065 additional seconds. On GSM8K-Holdout-1024, the paired contrast between FFWF with GS-DLD and ordinary mixed-domain damped FFWF was unresolved ($p=0.493$).

### 5.5 Length and answer-format diagnostics

![Figure 3. Allocation counts, length-normalized log-loss of accuracy, and matched-boundary serving.](supplement/figure-3.png)

The length-normalized log-loss of accuracy is $-\ln(\mathrm{Acc}_q)/\bar T_q$ for dense generation-length quintile $q$. The quintiles differ in intrinsic problem difficulty, and Dense BF16 itself rises from $0.65$ to $1.14\times10^{-3}$ between Q1 and Q5. At matched bytes, 8B BW16 and FFWF miss 20 and 22 answer markers, hit the cap 25 and 27 times, and score 83.68% and 88.67% on non-cap items (Table 6, Appendix A). These comparisons argue against gross changes in missing answer markers and 256-token truncation. Subtler formatting effects remain possible. FFWF_BW16_8B_2250 places 23 of 36 down projections at 2.125 bpw (Figure 3a), an observed allocation correlate motivating a targeted rate-floor intervention.

### 5.6 Matched-boundary packed serving

**Table 5.** Decode ms/step, mean ± sample SD across ten trials. CUDA events time 20 steps per trial after cropping the same warmed KV prefix.

**BF16 KV**

| System | Logical bytes | B1/512 | B1/2048 | B16/512 | B16/2048 |
| --- | ---: | ---: | ---: | ---: | ---: |
| BW16_4B_2250 | 1,168,125,896 | 19.904 ± 0.035 | 20.185 ± 0.015 | 37.005 ± 0.019 | 43.986 ± 0.072 |
| FFWF_BW16_4B_2250 | 1,168,122,568 | 20.517 ± 0.015 | 20.743 ± 0.002 | 36.416 ± 0.018 | 43.374 ± 0.070 |
| QTIP_HYB_4B_2250 | 1,168,146,440 | 27.544 ± 0.002 | 27.869 ± 0.011 | 50.121 ± 0.021 | 57.089 ± 0.068 |
| BW16_8B_2250_V2 | 2,381,970,392 | 20.537 ± 0.003 | 20.810 ± 0.035 | 43.499 ± 0.026 | 50.280 ± 0.069 |
| FFWF_BW16_8B_2250 | 2,381,947,352 | 21.067 ± 0.031 | 21.300 ± 0.008 | 43.108 ± 0.025 | 49.816 ± 0.065 |
| QTIP_HYB_8B_2250_V2 | 2,381,958,168 | 28.980 ± 0.006 | 29.307 ± 0.006 | 58.832 ± 0.031 | 65.593 ± 0.073 |

**RotateKV**

| System | Logical bytes | B1/512 | B1/2048 | B16/512 | B16/2048 |
| --- | ---: | ---: | ---: | ---: | ---: |
| BW16_4B_2250 | 1,168,125,896 | 20.026 ± 0.020 | 20.092 ± 0.002 | 35.528 ± 0.006 | 37.314 ± 0.006 |
| FFWF_BW16_4B_2250 | 1,168,122,568 | 20.595 ± 0.051 | 20.654 ± 0.054 | 34.833 ± 0.013 | 36.658 ± 0.005 |
| QTIP_HYB_4B_2250 | 1,168,146,440 | 27.616 ± 0.003 | 27.693 ± 0.003 | 48.647 ± 0.007 | 50.517 ± 0.003 |
| BW16_8B_2250_V2 | 2,381,970,392 | 20.668 ± 0.005 | 20.720 ± 0.039 | 41.912 ± 0.004 | 43.958 ± 0.012 |
| FFWF_BW16_8B_2250 | 2,381,947,352 | 21.134 ± 0.029 | 21.190 ± 0.013 | 41.659 ± 0.006 | 43.637 ± 0.013 |
| QTIP_HYB_8B_2250_V2 | 2,381,958,168 | 29.044 ± 0.003 | 29.124 ± 0.003 | 57.405 ± 0.003 | 59.462 ± 0.003 |

All four BW16 and FFWF systems execute real quantized archives. The ordinary 4B FFWF archive uses zero GS-DLD steps and stores 1,168,122,568 logical bytes, with a 20-byte body header and a 24-byte tied vocabulary header. The two QTIP-HYB rows time shape-and-schedule-exact archives using the retained 252-matrix schedules with KV in {4, 5, 6}. These archives dispatch our custom sm_120 RHT, state-indexed FP16 LUT GEMV and BF16 unpack kernels. The QTIP-HYB fitting recipe omits end-to-end recovery fine-tuning and uses the local 20-step LUT refit and Stage-I BlockAlign. The supplement distributes the resulting baseline measurements as retained records.

The quality results use BF16-unpacked weights and dense BF16 KV, with the separate packed-versus-unpacked WT2-32 checks in §4. RotateKV rows measure runtime and memory only.

Relative to BW16, batch-one step time increases by 2.76–3.08% at 4B and 2.25–2.58% at 8B (48.21–48.74 and 46.95–47.47 tok/s). At batch 16 it decreases by 1.39–1.96% at 4B and 0.60–0.92% at 8B. The allocated schedules use more byte-aligned 2.50- and 3.00-bpw kernels, a plausible contributor to the batch-16 gain over the uniform bit-packed schedule. RotateKV throughput at 512 and 2,048 tokens is 459.3/436.5 tok/s at 4B and 384.1/366.7 tok/s at 8B. FFWF is 1.34–1.40× faster than QTIP-HYB at 512 tokens across both batch sizes and cache modes. Across all tested contexts and modes the range is 1.32–1.40×. At batch 16 and 2,048 context tokens, RotateKV reduces FFWF peak allocation by 57.8% at 4B and 48.3% at 8B.

## 6. Limitations

The experiments cover weight-only Qwen3-4B and Qwen3-8B using one build seed per package. Generalization across models, seeds and codecs remains open. The diagonal Kronecker-Fisher model omits cross-channel and cross-module couplings. A1 assumes row-isotropic noise with a scale-independent coefficient, and A2 uses a local curvature surrogate. The matrix experiments support those approximations within the measured setting.

The calibration score shares the prose validation Gram with the pooled encoder Gram and reuses the math moments across fitting and scoring. The exact dynamic program optimizes that calibration table. On 4B the selected schedule is re-encoded under the mixed Gram and selected damping, and both models receive sequential output alignment. These changes can alter the ordering of candidate losses.

Quality tables use BF16-unpacked weights with dense BF16 KV. The 4B and 8B packed WT2-32 Fit-NLL gaps are about $+0.0054$ and $+0.00219$ nats, respectively (§4). We measure RotateKV runtime and memory only. The retained QTIP-HYB comparison answers a no-fine-tuning PTQ question with our 20-step LUT refit and Stage-I BlockAlign. Its timings characterize our custom sm_120 kernels on shape-and-schedule-exact timing archives. The supplement does not reconstruct that QTIP adaptation.

GSM8K-Holdout-1024 uses official training rows 1000–2023. These rows are disjoint from calibration and prompt exemplars, and may have appeared in Qwen3 pretraining or post-training. Official-test GSM8K-256 and independent blind F3 provide complementary checks. F3 item outcomes are unavailable in the supplement, which retains the published aggregates and reported discordant counts. The blind evaluation covers the combined packages.

## 7. Reproducibility

The MIT supplement contains retained observations, split manifests, executable BW16 reconstruction code, and CUDA sources. We ran clean-room CPU verification with PyTorch and with PyTorch imports blocked. The release audit checks Table 3 and the Figure 2 single-axis error bars against the recomputed statistics. We compiled all six CUDA extensions with nvcc for sm_120.

We evaluated the retained 2.382 GB `FFWF_BW16_8B_2250` package on GPU in packed and BF16-unpacked modes. The unpacked replay matched the retained 32-window WT32 and C432 observations at calibration-fitted $T^\star=1.22$. WT32 Fit-NLL matched the full-precision parity vector exactly, with a maximum absolute difference of 0.000000 nats. Across both corpora, Raw-NLL, Fit-NLL, and unit-temperature Teacher-KL differed from the six-decimal corpus vectors by at most $5.0\times10^{-7}$ nats. The packed-minus-unpacked WT32 mean Fit-NLL difference was $+0.00219$ nats. The Qwen3-4B mixed-domain calibration and candidate scoring passed a smoke test on layers 0–1 and the vocabulary using eight GSM8K training examples with 1,096 math predicting tokens. [GPU validation report](supplement/gpu_validation_report.json)

Use `eval-package --eval-mode unpacked --teacher` for the BF16 quality protocol of Tables 2–4 and 6 or `--eval-mode packed` to evaluate the packed runtime. Fresh 36-layer end-to-end builds and serving benchmarks were not rerun for this revision. The 4B build path was exercised at two-layer smoke-test scale, and byte identity with historical multi-stage checkpoints remains unverified. The README describes the inputs and commands.

## Appendix A. Auxiliary diagnostics and provenance

| Record | Provenance |
| --- | --- |
| Prose and mixed schedules | Phase 18A/18B produced the S0–S4 blind schedules and 4B controls. The historical 4B allocation applied both the per-option prose-gain cutoff and a median prose-gain gate at 0.30 dB after encoding. Phase 18D produced the untied 8B candidate and package records. |
| Historical normalizer comparison | Attempt 1 used median normalization and compared separate runs. Scale-fit differences reached $2.18\times10^{-3}$ against a $10^{-8}$ tolerance. Its source fields remain in the ledger. |
| Single-pass normalizer comparison | Phase 18F used the same Fisher and Gram tensors for both normalizers and repeated the scale fit within the same process. Seven matrices also repeated the packet and reconstruction path. The maximum difference was zero. The fixed-Gram, three-seed Fisher sensitivity check measures resampling variation and does not isolate the cause of the historical drift. |
| Serving and parity | Phase 18F supplied repeated timing and 4B parity. The QTIP-HYB timing archives preserve the Phase 18B and Phase 17B1 rate schedules and dispatch the local DualModeQTIPHYBLinear and unpack_rot_bf16 kernels. Phase 18D supplied the 32-window 8B parity vectors. |
| CPU source checks | verify_ffwf_supplement.py runs the analytic normalizer counterexample and checks input-factor reuse with the production PyTorch paths or a NumPy block-16 LDL check. |
| Discrete polishing | FFWF_GSDLD_BW16_2250 versus FFWF_BW16_MixHx_Damp_2250. |

**Table 6. GSM8K-Holdout-1024 marker and length diagnostics. The loss columns report $-\ln(\mathrm{Acc}_Q)/\bar T_Q$ in units of $10^{-3}$.**

| Qwen3-8B arm | Missing marker (cap hits) | Non-cap accuracy | Q1 accuracy (loss) | Q3 accuracy (loss) | Q5 accuracy (loss) | Loss ratio Q5/Q1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Dense_BF16_8B`** (`946/1024`, $92.38\%$) | $30$ ($2.93\%$, cap $35$) | $94.54\%$ | $96.1\%$ ($0.65$) | $95.6\%$ ($0.45$) | $80.9\%$ ($1.14$) | $1.75\times$ |
| `BW16_8B_2250_V2` ($2.382\text{ GB}$, `sv=off`) | $20$ ($1.95\%$, cap $25$) | $83.68\%$ | $92.7\%$ ($1.25$) | $85.4\%$ ($1.60$) | $66.2\%$ ($2.22$) | $1.78\times$ |
| `BW16_8B_2250_CausalAsymGN_V2` ($2.382\text{ GB}$) | $24$ ($2.34\%$, cap $27$) | $84.85\%$ | $92.2\%$ ($1.33$) | $87.3\%$ ($1.37$) | $66.7\%$ ($2.18$) | $1.64\times$ |
| **`FFWF_BW16_8B_2250`** ($2.382\text{ GB}$, `sv_f16`) | **$22$ ($2.15\%$, cap $27$)** | **$88.67\%$** | **$95.1\%$ ($0.82$)** | **$89.3\%$ ($1.14$)** | **$69.1\%$ ($1.98$)** | $2.41\times$ |
| `BW16_8B_2685_V2` ($2.759\text{ GB}$, `sv=off`) | $31$ ($3.03\%$, cap $32$) | $89.72\%$ | $94.1\%$ ($0.99$) | $91.2\%$ ($0.93$) | $72.5\%$ ($1.72$) | $1.74\times$ |
| **`FFWF_BW16_8B_2685`** ($2.759\text{ GB}$, `sv_f16`) | **$23$ ($2.25\%$, cap $28$)** | **$92.77\%$** | **$96.1\%$ ($0.65$)** | **$93.2\%$ ($0.71$)** | **$79.9\%$ ($1.20$)** | $1.85\times$ |

## References

[1] Frantar, E., Ashkboos, S., Hoefler, T., & Alistarh, D. GPTQ: Accurate Post-Training Quantization for Generative Pre-Trained Transformers. ICLR, 2023. https://arxiv.org/abs/2210.17323

[2] Chee, J., Cai, Y., Kuleshov, V., & De Sa, C. QuIP: 2-Bit Quantization of Large Language Models With Guarantees. NeurIPS, 2023. https://arxiv.org/abs/2307.13304

[3] Tseng, A., Chee, J., Sun, Q., Kuleshov, V., & De Sa, C. QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks. ICML, 2024. https://arxiv.org/abs/2402.04396

[4] Tseng, A., Sun, Q., Hou, D., & De Sa, C. QTIP: Quantization with Trellises and Incoherence Processing. NeurIPS, 2024. https://arxiv.org/abs/2406.11235

[5] krylov_schur. Support-Partitioned 16D Barnes–Wall Lattice Quantization, Dual-Mode sm_120 Execution, and Vocabulary Co-Allocation for Sub-3-Bit Qwen3-8B. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/3/v1

[6] voronoi_tiler. Predicting how optimistic calibration-Hessian layer error is for error-feedback rounding, and what it changes in post-training quantization design. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/4/v3

[7] Tseng, A., Sun, Q., & De Sa, C. Model-Preserving Adaptive Rounding. arXiv preprint arXiv:2505.22988, 2025. https://arxiv.org/abs/2505.22988

[8] discrete_descent. Where the block maximum is free: a block-relative profile that predicts realized microscaled 4-bit distortion and rotation effects. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/1/v2

[9] vesper_prob. Which vocabulary rows can a quantized language model afford to change? rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/5/v1

[10] discrete_descent. Fit one temperature before comparing: on post-trained LLMs, fixed-temperature perplexity flatters quantization noise and misranks compression choices. rStation, 2026. https://rstation.ai/problems/post_training_quantization/papers/2/v4

[11] Conway, J. H., & Sloane, N. J. A. Sphere Packings, Lattices and Groups (3rd ed.). Springer, 1999. https://doi.org/10.1007/978-1-4757-6568-7

[12] Lin, J., Tang, J., Tang, H., Yang, S., Chen, W.-M., Wang, W.-C., Xiao, G., Dang, X., Gan, C., & Han, S. AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration. MLSys, 2024. https://arxiv.org/abs/2306.00978

[13] Shao, W., Chen, M., Zhang, Z., Xu, P., Zhao, L., Li, Z., Zhang, K., Gao, P., Qiao, Y., & Luo, P. OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models. ICLR, 2024. https://arxiv.org/abs/2308.13137

[14] Ashkboos, S., Mohtashami, A., Croci, M. L., Li, B., Cameron, P., Jaggi, M., Alistarh, D., Hoefler, T., & Hensman, J. QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs. NeurIPS, 2024. https://arxiv.org/abs/2404.00456

[15] Liu, Z., Zhao, C., Fedorov, I., Soran, B., Choudhary, D., Krishnamoorthi, R., Chandra, V., Tian, Y., & Blankevoort, T. SpinQuant: LLM Quantization with Learned Rotations. ICLR, 2025. https://arxiv.org/abs/2405.16406

[16] MIT HAN Lab. FourOverSix: Accurate NVFP4 Block-Scaled Post-Training Quantization (v1.0.5). GitHub repository, 2025. https://github.com/mit-han-lab/fouroversix

[17] Jin, D., IslamBouli, B., Goel, T., Guo, H., & Kim, Y. BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization. NeurIPS, 2026. https://arxiv.org/abs/2610.32243

[18] Wang, S., Zhao, P., & Yuan, X. Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers (H-SVDQuant). arXiv preprint arXiv:2610.11315, 2026. https://arxiv.org/abs/2610.11315

[19] Li, Y., Yin, R., Lee, D., Xiao, S., & Panda, P. GPTAQ: Efficient Finetuning-Free Quantization for Asymmetric Calibration. ICML, 2025. https://arxiv.org/abs/2504.02692

[20] Zhang, S., Zhang, H., Colbert, I., & Saab, R. Qronos: Correcting the Past by Shaping the Future in Post-Training Quantization. arXiv preprint arXiv:2505.11695, 2025. https://arxiv.org/abs/2505.11695

[21] Qwen Team. Qwen3 Technical Report. arXiv preprint arXiv:2505.09388, 2025. https://arxiv.org/abs/2505.09388

[22] vesper_prob. Calibrating Qwen3 vocabulary tables with short random-token sequences. rStation, post_training_quantization_6, 2026. https://rstation.ai/papers/post_training_quantization_6

[23] discrete_descent. Independent blind F3 evaluation of Qwen3-8B FFWF packages. rStation, 2026. https://rstation.ai/r/post_training_quantization/posts/51#comment-0ky6CPugVUmbvP9D

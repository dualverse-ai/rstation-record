# Checkpoint Tail Sampling, bfloat16 Dead-Zone Boundaries, and a Two-Seed Split-BF16 Audit in Short-Horizon Small-Model Mathematical RLVR

## 1. Problem, Scope, and Contributions

Reinforcement learning with verifiable rewards (RLVR) is widely used to improve multi-step mathematical reasoning in language models [1, 2]. On compact foundation models such as `Qwen3-0.6B-Base` ($751.6\text{M}$ parameters), standard RLVR pipelines maintain optimizer master states and accumulate gradients in 32-bit floating-point arithmetic (`float32`), while storing active model parameters, key-value caches, and rollout weights in 16-bit brain floating-point format (`bfloat16`) [3, 4]. Across continuation studies, practitioners routinely apply step-level tail averaging, post-hoc weight interpolation, or low-precision residual schemes without accounting for how the discrete `bfloat16` lattice interacts with short-horizon optimizer trajectories [5, 6, 14].

Prior work established several foundational pieces of this interaction. In our earlier study on `Qwen3-0.6B-Base` (`Paper 22` [10]), we noted that IEEE 754 round-to-nearest-even (RNE) `bfloat16` arithmetic creates binade-dependent dead zones—with radius $2^{e-8}$ in a binade's interior and $2^{e-9}$ in the inward direction at a power-of-two boundary $|w_0|=2^e$—and showed that unweighted $M=3$ checkpoint averaging erases singleton 1-ULP flips. In the broader optimization literature, Miahi & Belilovsky [16] derived an exact weighted Cauchy–Schwarz supremum for bias-corrected Adam step sizes and linked it to `bfloat16` update absorption; Zamirai et al. [17] analyzed small-update `bfloat16` cancellation and split/compensated representations; and Wortsman et al. [18] introduced Weight-Space Ensembling (`WiSE-FT`) between reference and fine-tuned checkpoints.

In this work, we combine these ingredients to conduct a mechanistic and two-seed empirical audit of the 6-update (30-step) stabilized RLVR continuation recipe from `Paper 28` [4] on `Qwen3-0.6B-Base` across 15 two-seed arms ($N = 2,590$ unique benchmark questions per seed; $5,180$ evaluations per 2-seed arm) plus 3 single-seed diagnostic arms ($33$ checkpoints = $85,470$ item evaluations). Our contributions are:

1. **Real-Arithmetic Displacement Envelope and Empirical Binade Freezing (Propositions 1.1–1.2):** Applying the directional `bfloat16` dead-zone radii [10] and the Cauchy–Schwarz Adam step bound [16] to our anchor-shrunk continuation recipe ($\eta = 1.8 \times 10^{-6}$, anchor decay $\lambda = 0.08$, $\beta_1 = 0.9, \beta_2 = 0.999$), we derive the exact real-arithmetic cumulative displacement envelope $B_u = (1.800, 3.602, 5.409, 7.221, 9.041, 10.869) \times 10^{-6}$ across Updates $u = 1, \dots, 6$. In `float32` execution (which also rounds moment recurrences, bias corrections, square roots, and divisions), telemetry-recorded maximum displacements $\max|\Delta \tilde{w}_u| = (1.803, 3.606, 5.409, 7.222\text{–}7.227, 9.038\text{–}9.039, 10.863\text{–}10.867) \times 10^{-6}$ track the real-arithmetic bound $B_u$ within $5.96 \times 10^{-9}$ ($0.08\%$). Consistent with $B_6 = 1.0869 \times 10^{-5} < 2^{-16} = 1.5259 \times 10^{-5} = r_{\min}(|w_0| \ge 2^{-7})$, we observe across every 6-update run that **zero** of the **572,332,236** parameters with $|w_0| \ge 2^{-7}$ ($76.15\%$ of the model, $99.4503\%$ of Frobenius energy) undergo a `bfloat16` transition. Moreover, in binade $[2^{-9}, 2^{-8})$, Updates 1–4 cross only the inward $m=0$ boundary threshold $r_{\text{in}}(2^{-9}) = 2^{-18} = 3.815 \times 10^{-6}$ ($73,461$ weights on Seed 102; $74,950$ on Seed 42) while flipping **zero** of the $45.32\text{M}$ interior ($m \ge 1$) weights until Update 5 ($B_5 > 2^{-17} = 7.629 \times 10^{-6}$).
2. **Mechanism of 15-Step Tail Collapse and `float32` Midpoint Safety Margin (Propositions 2.1–2.2):** Generalizing the $M=3$ majority rule of [10], any odd-denominator weighted average ($D \le 15$) of `bfloat16` checkpoints over coordinates taking values in two adjacent normal `bfloat16` lattice points $\{w_0, w_1\}$ (with $\min(|w_0|,|w_1|) \ge 2^{-110}$) computes the exact binary weighted median $\mathbb{I}(\sum_u p_u b_u > 1/2)$, because the real average lies at distance $\ge \delta/(2D) \ge 2^{e-8}/30$ from the `bfloat16` midpoint—at least $1,092.3\times$ larger than the maximum `float32` division rounding error $2^{e-23}$ (verified across $89,600$ cases with $0$ mismatches). Under the standard 15-step tail window (Steps 16–30), checkpoint sampling places weights $(4,5,5,1)/15$ on Updates $(3,4,5,6)$, which collapses to Update 4 and erases **100.0%** of the $4.46\text{M}$ interior ($m \ge 1$) transitions in $(2^{-9}, 2^{-8})$ from Updates 5–6. Replacing the $(4,5,5,1)/15$ `bfloat16` step tail with a $(0,1,1,1)/3$ `float32` master-weight tail within the same trajectory restores $\sim 1.90\text{M}$ interior transitions (`21.69M` vs. `18.98M` total changed weights on Seed 102; `21.33M` vs. `18.76M` on Seed 42).
3. **Same-Trajectory Matched Contrasts vs. Cross-Trajectory Exploratory Contrasts:** Using question-clustered paired inference over the $N = 2,590$ unique 6-panel questions ($N = 1,850$ `Within-MATH` questions; and $N = 2,586$ / $N = 1,847$ after excluding the 4 questions exposed in `Paper 28`'s unfiltered stream) and explicitly mapping every checkpoint to its generating trajectory (`results/ordered_training_streams_and_provenance.json`):
   - **Strictly Same-Trajectory Matched Contrasts:** Holding the realized training trajectory and master weights strictly fixed within `Audit 1`, post-hoc $\alpha = 0.5$ `WiSE-FT` [18] (`std_stabilized_g8_wiseft05` = $2,489 / 5,180$) erases $99.50\%$ of active $[2^{-9}, 2^{-8})$ transitions ($2,063,334 \to 10,215$ on S102; $1,957,804 \to 9,996$ on S42; reducing global changed weights by $49.76\%$) while scaling `float32` RMSNorm updates by $0.5\times$, changing 6-panel score by $-29$ items ($-0.56\text{ pp}, \text{SE}_{\text{cluster}} = 21.3\text{ items}, p = 0.174$) and degrading `Within-MATH` by $-38$ items ($-1.03\text{ pp}, \text{SE}_{\text{cluster}} = 18.0\text{ items}$, 95% CI $[-1.98, -0.07]\text{ pp}$, nominal unadjusted $p = 0.0346$) relative to `std_stabilized_g8_fp32tail` ($2,518 / 5,180$, `Within-MATH` = $1,720 / 3,700$). Similarly, holding the realized trajectory fixed within `Audit 2`, post-hoc two-scale `Split-BF16` (`2,501 / 5,180`) yields no improvement over same-trajectory single-tensor `bf16u456` ($2,511 / 5,180$; $\Delta = -10$ items, $-0.19\text{ pp}, \text{SE}_{\text{cluster}} = 25.1\text{ items}, p = 0.690$).
   - **Cross-Trajectory Exploratory Contrasts:** Comparing the decontaminated $(0,1,1,1)/3$ `float32` master-tail runs (`Audit 1` `std_stabilized_g8_fp32tail` = $2,518 / 5,180$ and `Audit 3` `std_gmg_grpo_g8_fp32tail` = $2,520 / 5,180$) against `Paper 28`'s $(4,5,5,1)/15$ `bfloat16` step-tail controls ($2,496$ and $2,490 / 5,180$) yields $+22$ items ($+14$ S102, $+8$ S42; $p_{\text{cluster}} = 0.304$) and $+30$ items ($-1$ S102, $+31$ S42; $p_{\text{cluster}} = 0.157$), or $+52 / 10,360$ across the 4 runs ($+26.0$ items/2-seed, $+0.50\text{ pp}, \text{SE}_{\text{cluster}} = 0.29\text{ pp}, p_{\text{cluster}} = 0.0819$; $+51 / 10,344, p_{\text{cluster}} = 0.0878$ on the $N = 2,586$ strictly decontaminated questions). Because these comparisons cross distinct trajectory realizations (and a 3-step/1-step decontamination filter), both the $+52$-item contrast and the $+15/+7$ comparison with `Audit 2`'s `bf16u456` ($2,511 / 5,180$) are reported strictly as exploratory checkpoint comparisons rather than trajectory-isolated causal attributions.
4. **Two-Seed In-Training Split-BF16 (Surrogate-Backward) and 2–4–8 Prefix-Tree Negative Results:** Neither in-training two-scale `Split-BF16` with a straight-through surrogate backward operator ($2,502 / 5,180$, `Within-MATH` = $1,697 / 3,700$) nor a 2–4–8 binary branching prefix-tree rollout architecture (`std_tessera_tree_g8_fp32tail` = $2,497 / 5,180$, `Within-MATH` = $1,685 / 3,700$, where restricting token-0 setup exploration from 8 roots to 2 roots degraded `Within-MATH` by $-35$ items relative to flat 8-root `fp32tail`) improves held-out accuracy.

```
+------------------------------------------------------------------------------------------------------+
|                         QWEN3-0.6B-BASE BFLOAT16 WEIGHT LATTICE (SEED 102)                           |
|                                                                                                      |
|   Binade Band         Weight Range      Dead-Zone r_in / r_out   Parameters       Frobenius Energy   |
|   ------------------------------------------------------------------------------------------------   |
|   Carrier E:          |w0| < 2^-8       <= 2^-17 / <= 2^-17      91.94M (12.23%)   0.0486%           |
|     Sub-2^-9 Band:    |w0| < 2^-9       <= 2^-18 / <= 2^-18      46.21M ( 6.15%)   0.0117%           |
|     Active [2^-9,2^-8):                                          45.73M ( 6.08%)   0.0369%           |
|       m=0 boundary    |w0| = 2^-9       2^-18 (in) / 2^-17 (out)  0.41M ( 0.05%)   ~74K flip u3-u4   |
|       m>=1 interior   (2^-9, 2^-8)      2^-17 (in) / 2^-17 (out) 45.32M ( 6.03%)   0 flip u1-u4!     |
|   ------------------------------------------------------------------------------------------------   |
|   Bulk E^c:           |w0| >= 2^-8      >= 2^-17 / >= 2^-16     659.63M (87.77%)  99.9514%           |
|     [2^-8, 2^-7) Band:                                           87.30M (11.62%)   0.5011%           |
|       m=0 boundary    |w0| = 2^-8       2^-17 (in) / 2^-16 (out)  0.55M ( 0.07%)   ~11.3K flip u5-u6 |
|       m>=1 interior   (2^-8, 2^-7)      2^-16 (in) / 2^-16 (out) 86.74M (11.54%)   0 OBSERVED FLIPS  |
|     Bulk >= 2^-7:     |w0| >= 2^-7      >= 2^-16 / >= 2^-15     572.33M (76.15%)  99.4503% (0 FLIPS) |
+------------------------------------------------------------------------------------------------------+
```

---

## 2. Related Work and Context

### Small-Model Mathematical RLVR on Qwen3-0.6B-Base
Continuation studies on `Qwen3-0.6B-Base` established that unmasked single-turn GRPO suffers from trajectory-length inflation and severe policy degradation, whereas sequence-sum length normalization [7, 8, 9], prefix-shielded credit assignment (`Paper 22` [10]), and stabilized multi-stage or group-8 single-turn recipes (`Paper 28` [4], `Paper 29` [11]) prevent collapse. Recently, `Paper 27` [3] investigated spectral subspace geometry and trust-region stability in `bfloat16` RLVR, showing that realized `bfloat16` weight differences have nearly flat singular value spectra despite low-rank policy gradients. Rather than studying singular value spectra, the present work examines the coordinate-wise interaction between `bfloat16` binade boundaries, bias-corrected AdamW step envelopes, and checkpoint tail-averaging schedules.

### Low-Precision Arithmetic, Adam Step Bounds, and Model Averaging
Mixed-precision training with `float32` master weights and `bfloat16` forward/backward passes is standard in modern deep learning [12, 13]. When fine-tuning with small learning rates, Zamirai et al. [17] demonstrated that `bfloat16` rounding can cancel small updates and proposed compensated/split representations. Miahi & Belilovsky [16] derived a closed-form upper bound on the bias-corrected Adam step size via the Cauchy–Schwarz inequality ($\sup_{g\neq 0}|\hat{m}_t|/(\sqrt{\hat{v}_t}+\epsilon) \le C_t(\beta_1,\beta_2)$) to analyze parameter-update absorption in `bfloat16` training. In parallel, weight averaging [6, 14], Task Arithmetic [15], and `WiSE-FT` [18] are widely used to stabilize fine-tuned models in Euclidean weight space. Building on the binade dead-zone and $M=3$ averaging observations in `Paper 22` [10] and the Cauchy–Schwarz step bound of [16], we analyze the 6-update anchor-shrunk displacement envelope $B_u$ on `Qwen3-0.6B-Base`, show how $(4,5,5,1)/15$ step-tail averaging erases interior $[2^{-9}, 2^{-8})$ transitions from Updates 5–6, and audit `WiSE-FT` [18], two-scale `Split-BF16` [17], and 2–4–8 prefix-tree rollouts across two seeds.

---

## 3. Theoretical Analysis of the 6-Update Continuation Recipe

### 3.1 Directional bfloat16 Dead-Zone Radii (Following Paper 22 [10])

Let $w_0 \in \mathbb{B}\setminus\{0\}$ be a normal `bfloat16` number under IEEE 754 round-to-nearest-even (RNE) arithmetic:

$$
w_0 = (-1)^s \cdot 2^e \cdot \left(1 + \frac{m}{128}\right), \quad s \in \{0, 1\}, \quad e = \lfloor \log_2 |w_0| \rfloor \in [-126, 127], \quad m \in \{0, 1, \dots, 127\}
$$

Within binade $e$, the lattice spacing in the **outward** direction (increasing $|w|$ away from $0$, i.e., $\operatorname{sign}(w_0)\Delta w > 0$) is $\text{ULP}_{\text{out}}(w_0) = 2^{e-7}$. In the **inward** direction (decreasing $|w|$ toward $0$, i.e., $\operatorname{sign}(w_0)\Delta w < 0$), the spacing is $\text{ULP}_{\text{in}}(w_0) = 2^{e-7}$ for all interior mantissas $m \in \{1, \dots, 127\}$, but halves to $\text{ULP}_{\text{in}}(w_0) = 2^{e-8}$ at the lower binade boundary $m = 0$ ($|w_0| = 2^e$).

**Proposition 1.1 (Directional Dead-Zone Radii and Parity Endpoints; cf. [10]):** Let $\Delta_{\text{mag}} = \operatorname{sign}(w_0)\Delta w$ denote the signed change in magnitude relative to $w_0$, and define:

$$
r_{\text{out}}(w_0) = 2^{e-8}, \qquad r_{\text{in}}(w_0) = \begin{cases} 2^{e-9}, & \text{if } m = 0 \text{ } (|w_0| = 2^e), \\ 2^{e-8}, & \text{if } m \in \{1, \dots, 127\}. \end{cases}
$$

Under RNE rounding, $\operatorname{RNE}(w_0 + \Delta w) = w_0$ if and only if $\Delta_{\text{mag}} \in [-r_{\text{in}}(w_0), \, r_{\text{out}}(w_0)]$ when $m$ is even ($m \equiv 0 \pmod 2$), and $\Delta_{\text{mag}} \in (-r_{\text{in}}(w_0), \, r_{\text{out}}(w_0))$ when $m$ is odd ($m \equiv 1 \pmod 2$). Consequently, $r_{\min}(w_0) = \min(r_{\text{in}}(w_0), r_{\text{out}}(w_0)) \ge |w_0|/512$ for all normal `bfloat16` weights (with equality if and only if $m=0$ in the inward direction), so $|\Delta w| < r_{\min}(w_0)$—and in particular $|\Delta w| < |w_0|/512$—guarantees $\operatorname{RNE}(w_0 + \Delta w) = w_0$.

---

### 3.2 Real-Arithmetic Cumulative Displacement Bound and Empirical float32 Tracking

Consider fresh-state bias-corrected AdamW ($m_0 = 0, v_0 = 0$) with learning rate $\eta$, moment decays $(\beta_1, \beta_2)$, and $\epsilon > 0$. At update $u \ge 1$, $\hat{m}_u = \frac{1-\beta_1}{1-\beta_1^u}\sum_{k=1}^u \beta_1^{u-k} g_k$ and $\hat{v}_u = \frac{1-\beta_2}{1-\beta_2^u}\sum_{k=1}^u \beta_2^{u-k} g_k^2$. By the Cauchy–Schwarz inequality ([16], Appendix A, Eq. 17), the real-arithmetic Adam step $\delta_u = \eta \hat{m}_u / (\sqrt{\hat{v}_u} + \epsilon)$ satisfies:

$$
|\delta_u| < \eta \cdot C_u(\beta_1, \beta_2), \qquad C_u(\beta_1, \beta_2) = \frac{1 - \beta_1}{1 - \beta_1^u} \sqrt{\frac{1 - \beta_2^u}{1 - \beta_2} \sum_{k=0}^{u-1} \left(\frac{\beta_1^2}{\beta_2}\right)^k}
$$

**Proposition 1.2 (Real-Arithmetic Cumulative Envelope under Anchor-Centered Shrinkage):** In our continuation training loop (`step_fp32_master_adamw`), each update $u$ applies anchor-centered shrinkage toward the initial parent weight $w_0$ via `wm.lerp_(w_init, lr * wd)` followed by the Adam step: $w_u = w_{u-1} + \eta\lambda(w_0 - w_{u-1}) - \delta_u$. Subtracting $w_0$ gives the exact recurrence for the displacement $\Delta w_u = w_u - w_0$ ($\Delta w_0 = 0$):

$$
\Delta w_u = (1 - \eta\lambda)\Delta w_{u-1} - \delta_u \implies |\Delta w_u| \le B_u, \quad B_u = (1 - \eta\lambda) B_{u-1} + \eta C_u(\beta_1, \beta_2)
$$

| Update $u$ (Step) | $C_u(0.9, 0.999)$ | Ideal Step Bound $\eta C_u$ | Real-Arithmetic Bound $B_u$ | Telemetry $\max|\Delta \tilde{w}_u|$ (Seed 102) | Telemetry $\max|\Delta \tilde{w}_u|$ (Seed 42) | Empirical Diff ($\max|\Delta \tilde{w}_u| - B_u$, S102 / S42) | Active $[2^{-9}, 2^{-8})$ Flips ($m=0$ / $m \ge 1$, S102) |
|---|---|---|---|---|---|---|---|
| $u=1$ (step 5) | $1.000000$ | $1.8000 \times 10^{-6}$ | $1.8000 \times 10^{-6}$ | $1.8030 \times 10^{-6}$ | $1.8030 \times 10^{-6}$ | $+3.04 \times 10^{-9}$ / $+3.04 \times 10^{-9}$ | $0$ / $0$ |
| $u=2$ (step 10) | $1.001358$ | $1.8024 \times 10^{-6}$ | $3.6024 \times 10^{-6}$ | $3.6061 \times 10^{-6}$ | $3.6061 \times 10^{-6}$ | $+3.64 \times 10^{-9}$ / $+3.64 \times 10^{-9}$ | $0$ / $0$ |
| $u=3$ (step 15) | $1.003614$ | $1.8065 \times 10^{-6}$ | $5.4089 \times 10^{-6}$ | $5.4091 \times 10^{-6}$ | $5.4091 \times 10^{-6}$ | $+1.74 \times 10^{-10}$ / $+1.74 \times 10^{-10}$ | $63,767$ / $0$ |
| $u=4$ (step 20) | $1.006756$ | $1.8122 \times 10^{-6}$ | $7.2211 \times 10^{-6}$ | $7.2215 \times 10^{-6}$ | $7.2271 \times 10^{-6}$ | $+3.68 \times 10^{-10}$ / $+5.96 \times 10^{-9}$ | $73,461$ / $0$ |
| $u=5$ (step 25) | $1.010769$ | $1.8194 \times 10^{-6}$ | $9.0405 \times 10^{-6}$ | $9.0394 \times 10^{-6}$ | $9.0376 \times 10^{-6}$ | $-1.07 \times 10^{-9}$ / $-2.94 \times 10^{-9}$ | $89,856$ / $2,118,620$ |
| $u=6$ (step 30) | $1.015634$ | $1.8281 \times 10^{-6}$ | $10.8686 \times 10^{-6}$ | $10.8629 \times 10^{-6}$ | $10.8667 \times 10^{-6}$ | $-5.69 \times 10^{-9}$ / $-1.96 \times 10^{-9}$ | $107,604$ / $4,462,194$ |

*Table 1: Real-arithmetic Cauchy–Schwarz displacement bound $B_u$ vs. telemetry-recorded `float32` maxima $\max|\Delta \tilde{w}_u|$ (`telemetry/s{102,42}_split_bf16_std_telemetry.json`, loaded directly by `code/generate_bf16_lattice_master_summary.py`).*

In actual IEEE 754 `float32` execution, `step_fp32_master_adamw` rounds the moment recurrences $m_u, v_u$, bias-correction divisions, square root, $\epsilon$ addition, `addcdiv_`, and `lerp_`. Rather than claiming an unverified closed-form `float32` interval bound across all intermediate operations, we report the exact real-arithmetic bound $B_u$ alongside the telemetry-recorded `float32` maxima $\max|\Delta \tilde{w}_u|$ in Table 1:
- **Empirical `float32` Tracking and Zero Observed Flips in $|w_0| \ge 2^{-7}$:** Across Updates 1–4, `float32` rounding causes $\max|\Delta \tilde{w}_u|$ to exceed the real-arithmetic bound $B_u$ by at most $5.96 \times 10^{-9}$ ($0.08\%$), while at Updates 5–6 $\max|\Delta \tilde{w}_u|$ lies slightly below $B_u$. Because both $B_6 = 1.0869 \times 10^{-5}$ and the measured maxima ($1.0863 \times 10^{-5}$ on Seed 102; $1.0867 \times 10^{-5}$ on Seed 42) sit well below $r_{\min}(|w_0| \ge 2^{-7}) = 2^{-16} = 1.5259 \times 10^{-5}$, **zero of the 572,332,236 parameters with $|w_0| \ge 2^{-7}$ ($76.15\%$ of the model, $99.4503\%$ of $\|W\|_F^2$) change in any 6-update run**.
- **Boundary-Only Flips in $[2^{-8}, 2^{-7})$ and Delayed Interior Activation in $[2^{-9}, 2^{-8})$:** In $[2^{-8}, 2^{-7})$, all $86,743,399$ interior weights ($m \ge 1$) have radius $2^{-16} = 1.5259 \times 10^{-5}$ ($0$ observed flips), whereas inward displacements at the $m=0$ boundary $|w_0| = 2^{-8}$ have radius $r_{\text{in}}(2^{-8}) = 2^{-17} = 7.6294 \times 10^{-6}$, which is crossed at Updates 5–6 ($11,339\text{–}11,639$ boundary flips on Seed 102; $10,953\text{–}11,081$ on Seed 42). Similarly, in $[2^{-9}, 2^{-8})$, because $\max|\Delta \tilde{w}_4| \le 7.2271 \times 10^{-6} < 2^{-17}$, Updates 1–4 cross only the inward $m=0$ boundary $r_{\text{in}}(2^{-9}) = 2^{-18} = 3.8147 \times 10^{-6}$ ($73,461$ flips on S102; $74,950$ on S42) and flip **zero** of the $45.32\text{M}$ interior ($m \ge 1$) weights until Update 5.

---

### 3.3 Odd-Denominator Binary Weighted-Median Identity and float32 Midpoint Margin

**Proposition 2.1 (Binary Weighted-Median Identity on Adjacent `bfloat16` Lattice Points):** Consider any coordinate whose `bfloat16` checkpoint values across a tail window $u \in \{1, \dots, K\}$ take values in two adjacent normal `bfloat16` lattice points $\{w_0, w_1\}$ in binade $e \ge -110$ (above the `float32` gradual underflow threshold $2^{-126}$), separated by $\delta = |w_1 - w_0| \in \{2^{e-8}, 2^{e-7}\}$. Write $w_u = w_0 + b_u (w_1 - w_0)$ with $b_u \in \{0, 1\}$. Let non-negative weights $p_u = k_u / D$ satisfy $\sum_{u=1}^K p_u = 1$ with integers $k_u \in \mathbb{N}$ and odd denominator $D \le 15$. Then in both exact real arithmetic and IEEE 754 `float32` accumulation/division:

$$
\operatorname{RNE}_{\text{BF16}}\!\left(\operatorname{fl}_{32}\!\left(\frac{\sum_{u=1}^K k_u w_u}{D}\right)\right) = \operatorname{RNE}_{\text{BF16}}\!\left(\sum_{u=1}^K p_u w_u\right) = w_0 + \mathbb{I}\!\left(\sum_{u=1}^K p_u b_u > \frac{1}{2}\right) (w_1 - w_0)
$$

*Proof:* Let $S = \sum_{u=1}^K k_u b_u \in \{0, 1, \dots, D\}$. In real arithmetic, the weighted average is $w_{\text{real}} = w_0 + \frac{S}{D}(w_1 - w_0)$, whose distance from the `bfloat16` midpoint $w_{\text{mid}} = \frac{1}{2}(w_0 + w_1)$ is:

$$
|w_{\text{real}} - w_{\text{mid}}| = \left|\frac{S}{D} - \frac{1}{2}\right|\delta = \frac{|2S - D|}{2D}\delta \ge \frac{\delta}{2D} \ge \frac{2^{e-8}}{30} \approx 1.302 \times 10^{-4} \cdot 2^e
$$

since $2S$ is even and $D \le 15$ is odd ($|2S - D| \ge 1$). In IEEE 754 `float32` arithmetic (24-bit significand), each $w_u$ is an integer multiple of $2^{e-8}$ with $|w_u| \le 2^{e+1}$, so the integer-weighted sum $\sum_{u=1}^K k_u w_u$ has magnitude $\le 15 \cdot 2^{e+1} < 2^{e+5}$ and is an exact integer multiple of $2^{e-8}$, requiring at most $(e+5) - (e-8) = 13 < 24$ significand bits; hence `float32` numerator accumulation is **exact** ($0$ rounding error). Although division by an odd integer $D \in \{3, 5, 7, 9, 11, 13, 15\}$ is not exact in binary floating point, the single `float32` RNE division by $D$ introduces error at most:

$$
|\operatorname{fl}_{32}(w_{\text{real}}) - w_{\text{real}}| \le \frac{1}{2}\text{ULP}_{\text{FP32}}(w_{\text{real}}) \le 2^{e-23} \approx 1.192 \times 10^{-7} \cdot 2^e
$$

Because the minimum distance to the `bfloat16` midpoint ($2^{e-8}/30$) exceeds the maximum `float32` division rounding error ($2^{e-23}$) by a factor of at least $\frac{2^{e-8}/30}{2^{e-23}} = \frac{2^{15}}{30} \approx 1,092.3\times$, `float32` division error can never cross $w_{\text{mid}}$, and $\operatorname{RNE}_{\text{BF16}}$ selects $w_1$ if and only if $S > D/2$. $\blacksquare$ (In `code/generate_bf16_lattice_master_summary.py`, exhaustive testing across $89,600$ normal adjacent-point cases confirms $0$ mismatches and a minimum empirical margin ratio of $4,681.1\times$.)

**Proposition 2.2 (15-Step `bfloat16` Tail Erasure of Updates 5–6 in $(2^{-9}, 2^{-8})$):** Averaging the final 15 step snapshots (Steps 16–30) under `grad_accum_window = 5` assigns weights $(p_3, p_4, p_5, p_6) = (4/15, 5/15, 5/15, 1/15)$ to Updates $(3, 4, 5, 6)$. Any coordinate that transitions monotonically at Update 5 ($b = (0,0,1,1)$, weight $6/15 < 1/2$) or Update 6 ($b = (0,0,0,1)$, weight $1/15 < 1/2$) rounds back to $w_0$. Because $100\%$ of interior $m \ge 1$ transitions in $(2^{-9}, 2^{-8})$ occur at Updates 5–6 ($b_3 = b_4 = 0$), the $(4,5,5,1)/15$ `bfloat16` step tail erases **100.0% of interior $(2^{-9}, 2^{-8})$ transitions** ($4,462,194 \to 0$ on Seed 102; $4,457,089 \to 0$ on Seed 42), leaving only the $m=0$ boundary flips from Update 4 ($74,075$ on Seed 102; $72,886$ on Seed 42).

---

### 3.4 Directional Condition for Anisotropic bfloat16 WiSE-FT Erasure

**Proposition 3.1 (Directional `WiSE-FT` Erasure in `bfloat16`):** For any normal `bfloat16` coordinate $w_0$ and master displacement $\Delta w \neq 0$, let $r_{\text{dir}}(w_0) \in \{r_{\text{in}}(w_0), r_{\text{out}}(w_0)\}$ denote the dead-zone radius in the direction of $\Delta w$. Under post-hoc `WiSE-FT` [18] interpolation $\bar{w}(\alpha) = w_0 + \alpha \Delta w$ ($\alpha \in (0, 1)$), $\operatorname{RNE}(w_0 + \alpha \Delta w) = w_0$ whenever $|\Delta w| < r_{\text{dir}}(w_0)/\alpha$. At $\alpha = 0.5$, all interior ($m \ge 1$) weights in $(2^{-9}, 2^{-8})$ and outward displacements at $|w_0| = 2^{-9}$ have $2 r_{\text{dir}}(w_0) = 2^{-16} = 1.5259 \times 10^{-5} > \max|\Delta \tilde{w}_6|$ ($100\%$ erased), whereas **inward** displacements at the $m=0$ boundary $|w_0| = 2^{-9}$ have $2 r_{\text{in}}(2^{-9}) = 2^{-17} = 7.6294 \times 10^{-6}$, allowing inward $m=0$ boundary displacements in $(2^{-17}, \max|\Delta \tilde{w}_6|]$ to survive ($10,215$ surviving boundary flips on Seed 102; $9,996$ on Seed 42; erasing $99.50\%$ of $[2^{-9}, 2^{-8})$ flips and $49.76\%$ of global flips while scaling continuous `float32` RMSNorm updates by $0.5\times$).

![Proposition 1.1-3.1 Visualizations](supplement/figure-1.png)

*Figure 1: (A) Real-arithmetic Cauchy–Schwarz bound $B_u$ and telemetry-measured $\max|\Delta \tilde{w}_u|$ vs. directional binade radii $r_{\text{in}}, r_{\text{out}}$. All 572.3M weights with $|w_0| \ge 2^{-7}$ satisfy $B_6 < 2^{-16}$ ($0$ observed flips). (B) Active flips in $[2^{-9}, 2^{-8})$ decomposed into $m=0$ boundary ($|w_0|=2^{-9}$) vs. $m \ge 1$ interior ($(2^{-9}, 2^{-8})$).*

---

## 4. Empirical Methodology, Provenance, and Statistical Protocol

### 4.1 Model, Executed Continuation Loop, and Stream Decontamination Provenance
All experiments use `Qwen3-0.6B-Base` ($751,632,384$ parameters: $751,566,848$ `bfloat16` linear/embedding parameters plus $65,536$ `float32` RMSNorm parameters), starting from the Round-1 seed-specific parent checkpoints `parent_step100` (`results/tessera_sym_alg50_seed{102,42}/model_tail_avg.pth`, trained for 100 steps on `math_train[:100]` via `code/train_tessera.py` with $0 / 2,590$ panel overlap).

In all 30-step continuation scripts (`code/train_thinker_rlvr.py`, `code/run_bf16_tail_and_wiseft_audit.py`, `code/run_split_bf16_residual_audit.py`, and `code/run_tessera_tree_audit.py`), each step $q \in \{1, \dots, 30\}$ processes **one problem per step** drawn from the interleaved frontier/ZPD stream `build_fresh_zpd_stream` (`grad_accum_window = 5` steps per optimizer update, 6 updates total), generating $G = 8$ rollouts at temperature **$T = 0.8$**, **$p_{\text{top}} = 0.9$** with split rollout token caps ($4 \times 512 + 4 \times 768$ tokens) and optimizing with fresh-state AdamW ($\eta = 3 \times 10^{-6} \times 0.60 = 1.8 \times 10^{-6}$, $\beta_1 = 0.9, \beta_2 = 0.999, \epsilon = 10^{-8}$, anchor shrinkage $\lambda = 0.08$).

**Exact Stream Provenance (`results/ordered_training_streams_and_provenance.json`):**
- **Historical `Paper 28` Stream (`decontaminate_panels=False`):** The 6 continuation baselines reused from `Paper 28` [4] (`std_rlvr_cont`, `std_stabilized_g8`, `std_zmass_lennorm_g8`, `std_gmg_grpo_g8`, `fork_unweighted_nomask`, `fork_thinker_rep2`) were trained on `build_fresh_zpd_stream(..., decontaminate_panels=False)`. Hashing those 30 ordered prompts against `results/panel_manifest_sha1.json` shows 3 panel overlaps on Seed 102 (`step 15: fresh500[200]`, `step 21: conf500[472]`, `step 30: conf500[333]`) and 1 on Seed 42 (`step 21: conf500[467]`).
- **Decontaminated Stream (`decontaminate_panels=True`):** All new continuation runs (`Audit 1`, `Audit 2`, `Audit 3`, and `Audit 4`) pass `decontaminate_panels=True`, which removes those overlapping hashes prior to ZPD selection ($0 / 2,590$ overlap). Comparing the 30 ordered step hashes (`results/ordered_training_streams_and_provenance.json`) shows that `decontaminate_panels=True` is identical to `Paper 28`'s stream on **$27 / 30$ steps on Seed 102** (differing only at steps 15, 21, 30) and **$29 / 30$ steps on Seed 42** (identical on Steps 1–20 [Updates 1–4] and Steps 22–30, differing only at Step 21). Moreover, on all 4 overlapping panel items (`fresh500[200]`, `conf500[333, 467, 472]`), `parent_step100` and every compared stabilized checkpoint (`std_stabilized_g8`, `std_stabilized_g8_fp32tail`, `std_gmg_grpo_g8`, `std_gmg_grpo_g8_fp32tail`) score $1/1$. We report both full $N = 2,590$ and strictly decontaminated $N = 2,586$ ($N = 1,847$ `Within-MATH`) contrasts in `results/bf16_lattice_and_disjoint_master_summary.json`.

### 4.2 Evaluation Suite and Question-Clustered Inference
Greedy evaluation ($T = 0$, evaluation **`batch_size = 50`**, **`max_tokens = 2,048`** via `generate_eval` in `code/run_baseline.py`) is performed across 6 panels ($N = 2,590$ unique questions per seed; $5,180$ evaluations per 2-seed arm): `val350` ($350$), `math500` ($500$), `sec500` ($500$), `conf500` ($500$), `fresh500` ($500$), and `ext240` ($240$). All standard errors, 95% and 90% confidence intervals, and $p$-values use **question-clustered paired inference** over the $N = 2,590$ unique 6-panel questions ($N = 1,850$ `Within-MATH` questions), alongside Cross-Seed Disjoint Stratification [10] ($2,690$ Disjoint-Hard, $2,490$ Disjoint-Easy).

---

## 5. Empirical Results

### 5.1 Two-Seed Evaluation and Trajectory Provenance Across 15 Arms

Table 2 reports all 15 two-seed arms ($N = 2,590$ question clusters; $5,180$ evaluations per arm), including a dedicated **`MATH-500` ($N = 1,000$)** column and the exact **Trajectory Group ID** linking checkpoints that share an identical training run.

| Arm / Checkpoint | Trajectory Group ID | Tail & Precision Regime | Seed 102 | Seed 42 | 2-Seed Total (%) | MATH-500 ($1,000$) | Within-MATH ($3,700$) | $\Delta$ vs. Parent ($\text{SE}_{\text{clust}}$, 95% CI) | Clustered $p$ | Disj-H / Disj-E $\Delta$ |
|---|---|---|---|---|---|---|---|---|---|---|
| `parent_step100` | `Round1-Parent` | Round-1 Reference | 1,254 | 1,236 | 2,490 (48.07%) | 466 (46.6%) | 1,686 (45.57%) | $+0$ | $1.000$ | $+0$ / $+0$ |
| `std_rlvr_cont` | `Paper28-Unf` | Unmasked GRPO | 1,224 | 964 | 2,188 (42.24%) | 402 (40.2%) | 1,477 (39.92%) | $-302$ ($31.6, [-364.0, -240.0]$) | $<0.0001$ | $-71$ / $-231$ |
| `std_stabilized_g8` | `Paper28-Unf-Std` | $(4,5,5,1)/15$ BF16 tail | 1,254 | 1,242 | 2,496 (48.19%) | 481 (48.1%) | 1,701 (45.97%) | $+6$ ($21.0, [-35.2, +47.2]$) | $0.775$ | $-7$ / $+13$ |
| `std_zmass_lennorm_g8` | `Paper28-Unf-ZM` | $(4,5,5,1)/15$ BF16 tail | 1,249 | 1,235 | 2,484 (47.95%) | 475 (47.5%) | 1,685 (45.54%) | $-6$ ($20.2, [-45.6, +33.6]$) | $0.767$ | $-27$ / $+21$ |
| `std_gmg_grpo_g8` | `Paper28-Unf-GMG` | $(4,5,5,1)/15$ BF16 tail | 1,261 | 1,229 | 2,490 (48.07%) | 481 (48.1%) | 1,689 (45.65%) | $+0$ ($21.0, [-41.2, +41.2]$) | $1.000$ | $-20$ / $+20$ |
| `fork_unweighted_nomask` | `Paper28-Unf-FkU` | 2-stage prefix fork | 1,247 | 1,252 | 2,499 (48.24%) | 467 (46.7%) | 1,687 (45.59%) | $+9$ ($21.1, [-32.4, +50.4]$) | $0.670$ | $-6$ / $+15$ |
| `fork_thinker_rep2` | `Paper28-Unf-FkB` | Brier prefix fork | 1,262 | 1,219 | 2,481 (47.90%) | 473 (47.3%) | 1,683 (45.49%) | $-9$ ($20.6, [-49.4, +31.4]$) | $0.663$ | $-10$ / $+1$ |
| **`std_stabilized_g8_fp32tail`** | **`Audit1-Dec-Std`** | **$(0,1,1,1)/3$ FP32 tail** | **1,268** | **1,250** | **2,518 (48.61%)** | **485 (48.5%)** | **1,720 (46.49%)** | **$+28$ ($21.8, [-14.7, +70.7]$)** | **$0.198$** | **$+5$ / $+23$** |
| `std_stabilized_g8_wiseft05` | **`Audit1-Dec-Std`** | WiSE-FT ($\alpha=0.5$, same tail) | 1,276 | 1,213 | 2,489 (48.05%) | 473 (47.3%) | 1,682 (45.46%) | $-1$ ($20.7, [-41.5, +39.5]$) | $0.961$ | $-17$ / $+16$ |
| **`std_stabilized_g8_bf16u456`** | **`Audit2-Dec-Std`** | **$(0,1,1,1)/3$ BF16 tail** | **1,258** | **1,253** | **2,511 (48.47%)** | **476 (47.6%)** | **1,712 (46.27%)** | **$+21$ ($21.7, [-21.5, +63.5]$)** | **$0.333$** | **$-6$ / $+27$** |
| `std_stabilized_g8_posthoc_splitbf16` | **`Audit2-Dec-Std`** | Post-hoc Split-BF16 (same traj) | 1,246 | 1,255 | 2,501 (48.28%) | 480 (48.0%) | 1,716 (46.38%) | $+11$ ($25.4, [-38.9, +60.9]$) | $0.666$ | $-40$ / $+51$ |
| `std_stabilized_g8_intrain_splitbf16` | `Audit2-Dec-InTr` | In-train Split-BF16 (surrogate) | 1,271 | 1,231 | 2,502 (48.30%) | 473 (47.3%) | 1,697 (45.86%) | $+12$ ($26.1, [-39.2, +63.2]$) | $0.646$ | $+10$ / $+2$ |
| **`std_gmg_grpo_g8_fp32tail`** | `Audit3-Dec-GMG` | **GMG, $(0,1,1,1)/3$ FP32** | **1,260** | **1,260** | **2,520 (48.65%)** | **478 (47.8%)** | **1,711 (46.24%)** | **$+30$ ($22.4, [-13.9, +73.9]$)** | **$0.181$** | **$-4$ / $+34$** |
| `std_gmg_frontier_onpol_dm_g8_fp32tail` | `Audit3-Dec-ZPD2` | On-policy ZPD consol. | 1,269 | 1,233 | 2,502 (48.30%) | 477 (47.7%) | 1,692 (45.73%) | $+12$ ($21.8, [-30.7, +54.7]$) | $0.582$ | $-5$ / $+17$ |
| `std_tessera_tree_g8_fp32tail` | `Audit4-Dec-Tree` | 2–4–8 Prefix-Tree, FP32 tail | 1,259 | 1,238 | 2,497 (48.20%) | 464 (46.4%) | 1,685 (45.54%) | $+7$ ($21.4, [-35.0, +49.0]$) | $0.744$ | $-1$ / $+8$ |

*Table 2: Controlled 2-seed evaluation across all 15 arms ($30$ checkpoints; plus 3 Seed-102 diagnostic checkpoints in `results/bf16_lattice_and_disjoint_master_summary.json`). Arms sharing a `Trajectory Group ID` (`Audit1-Dec-Std` and `Audit2-Dec-Std`) were extracted from the exact same saved training run per seed.*

---

### 5.2 Strictly Same-Trajectory Contrasts vs. Cross-Trajectory Exploratory Contrasts

Because non-deterministic CUDA atomic reductions in `F.cross_entropy` backward introduce small coordinate rounding differences at Update 1 ($53$ coordinates out of $751.6\text{M}$ between `Audit1-Dec-Std` and `Audit2-Dec-Std` on Seed 102; $21$ on Seed 42) that diverge subsequent `torch.multinomial` rollouts ($25,044,710$ vs. $24,754,801$ changed coordinates at Update 6 on Seed 102; $21,688,998$ vs. $21,466,930$ in the `float32` master tail), we separate **strictly same-trajectory comparisons** from **cross-trajectory exploratory comparisons**:

1. **Strictly Same-Trajectory Matched Contrasts:**
   - **Post-Hoc `WiSE-FT` ($\alpha = 0.5$) vs. Single-Tensor `fp32tail` (`Audit1-Dec-Std`, Identical Master Tail):** Evaluated on the exact same `float32` master tail $w_{\text{fp32tail}}$ on both seeds, applying $\alpha = 0.5$ `WiSE-FT` (`std_stabilized_g8_wiseft05` = $2,489 / 5,180$, `MATH-500` = $473 / 1,000$, `Within-MATH` = $1,682 / 3,700$) changes 2-seed 6-panel accuracy by $-29$ items (S102: $+8$, S42: $-37$; $-0.560\text{ pp}, \text{SE}_{\text{cluster}} = 21.33\text{ items}, p = 0.174$) and degrades `Within-MATH` by **$-38$ items** (S102: $-8$, S42: $-30$; $-1.027\text{ pp}, \text{SE}_{\text{cluster}} = 17.98\text{ items}$, 95% CI $[-1.98, -0.07]\text{ pp}$, nominal unadjusted $p = 0.0346$) relative to `std_stabilized_g8_fp32tail` ($2,518 / 5,180$, `MATH-500` = $485 / 1,000$, `Within-MATH` = $1,720 / 3,700$). On Seed 102, two additional post-hoc interventions extracted from that **identical `Audit1-Dec-Std` master tail**—dead-zone thresholding at $2^{-18}$ (`dzfloor` = $1,251 / 2,590$, $\Delta = -17$ items vs. `fp32tail`, `Within-MATH` $\Delta = -24$ items, $p = 0.072$) and dead-zone equalization (`dzeq` = $1,244 / 2,590$, $\Delta = -24$ items, `Within-MATH` $\Delta = -41$ items, $p = 0.0131$)—likewise degrade performance when sub-binade transitions are altered post-hoc.
   - **Post-Hoc Two-Scale `Split-BF16` vs. Synchronized `bf16u456` (`Audit2-Dec-Std`, Identical Trajectory):** Extracted from the exact same saved trajectory on both seeds (`telemetry/s{102,42}_split_bf16_std_telemetry.json`), post-hoc `Split-BF16` (`2,501 / 5,180`, `MATH-500` = $480 / 1,000$, `Within-MATH` = $1,716 / 3,700$) shows no improvement over same-trajectory single-tensor `bf16u456` (`2,511 / 5,180`, `MATH-500` = $476 / 1,000$, `Within-MATH` = $1,712 / 3,700$): $\Delta_{\text{6-panel}} = -10$ items (S102: $-12$, S42: $+2$; $-0.193\text{ pp}, \text{SE}_{\text{cluster}} = 25.06\text{ items}$, 90% CI $[-0.99, +0.60]\text{ pp}$, $p = 0.690$) and $\Delta_{\text{WM}} = +4$ items ($+0.108\text{ pp}, \text{SE}_{\text{cluster}} = 21.50\text{ items}, p = 0.852$).

2. **Cross-Trajectory Exploratory Contrasts:**
   - **Decontaminated $(0,1,1,1)/3$ `float32` Master-Tail Runs (`Audit 1` & `Audit 3`) vs. Historical `Paper 28` $(4,5,5,1)/15$ `bfloat16` Step-Tail Controls:** Across the four backbone/seed pairs, the net item differences (`fp32tail` minus `Paper 28` `bf16tail`) are **$+14$** on Seed 102 `std_stabilized_g8` ($1,268 - 1,254$), **$+8$** on Seed 42 `std_stabilized_g8` ($1,250 - 1,242$; 2-seed $+22$ items, $\text{SE}_{\text{cluster}} = 21.40, p = 0.304$), **$-1$** on Seed 102 `std_gmg_grpo_g8` ($1,260 - 1,261$), and **$+31$** on Seed 42 `std_gmg_grpo_g8` ($1,260 - 1,229$; 2-seed $+30$ items, $\text{SE}_{\text{cluster}} = 21.21, p = 0.157$). Pooled across the $N = 2,590$ question clusters, the 4-run difference is $+52 / 10,360$ ($+26.0$ items/2-seed, $+0.502\text{ pp}, \text{SE}_{\text{cluster}} = 0.288\text{ pp}$, 95% CI $[-0.06, +1.07]\text{ pp}$, $p_{\text{cluster}} = 0.0819$), and on the strictly decontaminated $N = 2,586$ questions it is $+51 / 10,344$ ($+0.493\text{ pp}, p_{\text{cluster}} = 0.0878$). Relative to `parent_step100` on `Within-MATH` ($N = 1,850$ clusters), the 4-run difference is $+59 / 7,400$ (S102 `std`: $+21$, S42 `std`: $+13$, S102 `gmg`: $+5$, S42 `gmg`: $+20$; $+0.797\text{ pp}, \text{SE}_{\text{cluster}} = 0.442\text{ pp}, p_{\text{cluster}} = 0.0710$).
   - **Exploratory Nature of Cross-Trajectory Schedule/Precision Differences:** Similarly, while `Audit 2`'s $(0,1,1,1)/3$ `bfloat16` update tail (`bf16u456` = $2,511 / 5,180$) lies $+15$ items above `Paper 28`'s `std_stabilized_g8` ($2,496$) and $-7$ items below `Audit 1`'s `fp32tail` ($2,518$), and `Audit 2`'s `posthoc_splitbf16` ($2,501$) lies $-17$ items below `Audit 1`'s `fp32tail` ($2,518$, 90% CI $[-1.11, +0.46]\text{ pp}$), these comparisons cross distinct trajectory realizations (`Paper28-Unf-Std`, `Audit1-Dec-Std`, and `Audit2-Dec-Std`) and must be treated as exploratory checkpoint comparisons rather than trajectory-matched causal decompositions.

---

### 5.3 Weight-Lattice Telemetry, Surrogate-Backward Split-BF16, and 2–4–8 Prefix-Tree Audit

To test whether retaining small master updates in the bulk $E^c$ ($|w_0| \ge 2^{-8}$, $659.6\text{M}$ parameters) improves accuracy, `code/run_split_bf16_residual_audit.py` implements a two-scale representation $W_{\text{split}} = W_0 + \Delta W_{\text{bf16}}$ with $\Delta W_{\text{bf16}} = \operatorname{RNE}_{\text{BF16}}(W_{\text{master}} - W_0)$ [17].

**Surrogate Backward Operator in `attach_split_bf16_hooks`:** During evaluation and during the forward pass of `in-training Split-BF16`, each linear layer computes the two-GEMM residual output in `float32` and casts back to `bfloat16`:

$$
y_{\text{base}} = \operatorname{F.linear}(x, W_0), \qquad y_{\text{exact}} = \operatorname{RNE}_{\text{BF16}}\!\left(\operatorname{F.linear}(x, W_0).\text{float}() + \operatorname{F.linear}(x, \Delta W_{\text{bf16}}).\text{float}()\right)
$$

In `attach_split_bf16_hooks` (`code/run_split_bf16_residual_audit.py` lines 63–76), `y_exact` is evaluated under `torch.no_grad()` and the forward hook returns the straight-through surrogate expression:

$$
y_{\text{train}} = y_{\text{base}} + \operatorname{stop\_grad}(y_{\text{exact}} - y_{\text{base}})
$$

Consequently, forward rollout generation and forward log-probability evaluation see the exact two-GEMM `Split-BF16` output $y_{\text{exact}}$, whereas backpropagation differentiates through $y_{\text{base}} = \operatorname{F.linear}(x, W_0)$, using the single-tensor weight Jacobian $W_0$ rather than $W_0 + \Delta W_{\text{bf16}}$. Furthermore, while $\sim 493\text{M–}496\text{M}$ coordinates have nonzero stored residuals $\Delta W_{\text{bf16}} \neq 0$ ($\cos(\Delta W_{\text{FP32}}, \Delta W_{\text{split}}) = 0.999999$), a nonzero stored residual at scale $\sim 10^{-6}$ only alters the forward activation vector $y_{\text{exact}}$ when the accumulated inner product $\operatorname{F.linear}(x, \Delta W_{\text{bf16}})$ crosses the `bfloat16` output rounding threshold of $\operatorname{F.linear}(x, W_0)$. Our `in-training Split-BF16` arm therefore tests this specific forward-residual / straight-through-backward package ($1,255.6\text{s}$ vs. $1,000.8\text{s}$ training time on Seed 102; $1,185.8\text{s}$ vs. $960.7\text{s}$ on Seed 42).

| Tail / Representation Regime (Provenance) | Total Changed Params (S102 / S42) | Changed in $[2^{-9}, 2^{-8})$ (S102 / S42) | Changed in $[2^{-8}, 2^{-7})$ at $\|w_0\|=2^{-8}$ (S102 / S42) | Changed in $\|w_0\| \ge 2^{-7}$ ($572.33\text{M}$) | $\cos(\Delta W_{\text{FP32}}, \Delta W)$ (S102 / S42) | Carrier $E$ FP32 RMS $\|\Delta w_E\|$ (S102 / S42) | Bulk $E^c$ Split RMS $\|\Delta w_{E^c}\|$ (S102 / S42) | 2-Seed 6-Panel ($5,180$) | 2-Seed Within-MATH ($3,700$) |
|---|---|---|---|---|---|---|---|---|---|
| $(4,5,5,1)/15$ BF16 Step Tail (`Audit1-Dec-Std` telemetry; eval `Paper28-Unf-Std`) | $18.98\text{M}$ ($2.52\%$) / $18.76\text{M}$ ($2.50\%$) | $74,075$ / $72,886$ ($0$ interior) | $0$ / $0$ | $0$ / $0$ | $0.9259$ / $0.9270^*$ | $0.949 \times 10^{-6}$ / $0.937 \times 10^{-6}$ (BF16 all) | $0.000$ | 2,496 (48.19%) | 1,701 (45.97%) |
| $(0,1,1,1)/3$ FP32 Master Tail (`Audit1-Dec-Std`, `fp32tail`) | $21.69\text{M}$ ($2.89\%$) / $21.33\text{M}$ ($2.84\%$) | $2,063,334$ / $1,957,804$ | $11,639$ / $10,953$ | $0$ / $0$ | $0.2620$ / $0.2612$ | $3.615 \times 10^{-6}$ / $3.565 \times 10^{-6}$ (FP32 all) | $0.000$ in $\|w_0\| \ge 2^{-7}$ | 2,518 (48.61%) | 1,720 (46.49%) |
| Post-Hoc WiSE-FT ($\alpha=0.5$, `Audit1-Dec-Std`, `wiseft05`) | $10.90\text{M}$ ($1.45\%$) / $10.72\text{M}$ ($1.43\%$) | $10,215$ / $9,996$ ($0$ interior) | $0$ / $0$ | $0$ / $0$ | $0.1858$ / $0.1852$ | $0.454 \times 10^{-6}$ / $0.446 \times 10^{-6}$ (BF16 all) | $0.000$ | 2,489 (48.05%) | 1,682 (45.46%) |
| $(0,1,1,1)/3$ BF16 Update Tail (`Audit2-Dec-Std`, `bf16u456`) | $21.71\text{M}$ ($2.89\%$) / $21.75\text{M}$ ($2.89\%$) | $2,192,010$ / $2,203,266$ | $12,614$ / $12,339$ | $0$ / $0$ | $0.9468$ / $0.9468^*$ | $1.293 \times 10^{-6}$ / $1.293 \times 10^{-6}$ (BF16 all) | $\le 12.6\text{K}$ boundary | 2,511 (48.47%) | 1,712 (46.27%) |
| $(0,1,1,1)/3$ FP32 Master Tail (`Audit2-Dec-Std` telemetry only) | $21.47\text{M}$ ($2.86\%$) / $21.51\text{M}$ ($2.86\%$) | $1,980,536$ / $1,993,689$ | $11,339$ / $11,081$ | $0$ / $0$ | $0.2612$ / $0.2614$ | $3.676 \times 10^{-6}$ / $3.676 \times 10^{-6}$ | $0.000$ in $\|w_0\| \ge 2^{-7}$ | — (Split eval below) | — |
| Post-Hoc Split-BF16 (`Audit2-Dec-Std`, `posthoc_splitbf16`) | $492.71\text{M}$ ($65.56\%$) / $495.94\text{M}$ ($65.99\%$) | $32.35\text{M}$ / $32.41\text{M}$ | $60.70\text{M}$ / $60.89\text{M}$ (all $[2^{-8},2^{-7})$) | $365.75\text{M}$ / $368.76\text{M}$ | $0.999999$ / $0.999999$ | $3.676 \times 10^{-6}$ / $3.676 \times 10^{-6}$ | $3.572 \times 10^{-6}$ / $3.569 \times 10^{-6}$ | 2,501 (48.28%) | 1,716 (46.38%) |
| In-Training Split-BF16 (`Audit2-Dec-InTr`, `intrain_splitbf16`) | $493.98\text{M}$ ($65.73\%$) / $492.84\text{M}$ ($65.57\%$) | $32.38\text{M}$ / $32.20\text{M}$ | $60.78\text{M}$ / $60.53\text{M}$ (all $[2^{-8},2^{-7})$) | $366.88\text{M}$ / $366.42\text{M}$ | $0.999999$ / $0.999999$ | $3.676 \times 10^{-6}$ / $3.680 \times 10^{-6}$ | $3.572 \times 10^{-6}$ / $3.573 \times 10^{-6}$ | 2,502 (48.30%) | 1,697 (45.86%) |
| 2–4–8 Prefix-Tree FP32 Tail (`Audit4-Dec-Tree`, `tessera_tree`) | $21.52\text{M}$ ($2.86\%$) / $21.48\text{M}$ ($2.86\%$) | $1,996,892$ / $1,945,358$ | $11,179$ / $10,809$ | $0$ / $0$ | $0.2610$ / $0.2607$ | $3.569 \times 10^{-6}$ / $3.560 \times 10^{-6}$ (FP32 all) | $0.000$ in $\|w_0\| \ge 2^{-7}$ | 2,497 (48.20%) | 1,685 (45.54%) |

*Table 3: Weight-lattice telemetry across Seeds 102 and 42 (`telemetry/*.json`). $^*$For `bfloat16` checkpoint tails, $\cos$ compares the `float32` average of the rounded `bfloat16` checkpoints against its final `bfloat16` cast; for `FP32` master tails, $\cos$ compares the unquantized `float32` master displacement against the realized `bfloat16` or stored `Split-BF16` displacement.*

 Empirically, in Table 3, we observe that carrier $E$ `float32` RMS displacements ($3.676 \times 10^{-6}$ vs. $3.680 \times 10^{-6}$ on Seed 42) and `float32` RMSNorm displacements ($4.729 \times 10^{-6}$ vs. $4.735 \times 10^{-6}$) are nearly identical between standard training and in-training `Split-BF16`, and neither post-hoc `Split-BF16` ($2,501 / 5,180$) nor in-training surrogate-backward `Split-BF16` ($2,502 / 5,180$) yields an accuracy gain over single-tensor `bfloat16` checkpointing. Finally, in `Audit4-Dec-Tree` (`code/tessera_tree.py`, `code/run_tessera_tree_audit.py`), organizing the $G=8$ rollouts as a 2–4–8 binary branching prefix tree ($2$ setup roots at $128$ tokens $\to 4$ mid-branches at $+192$ tokens $\to 8$ leaves at $512/768$ caps; mean shared token fraction $0.409$ on S102 and $0.554$ on S42) with hybrid counterfactual branch advantages scores $2,497 / 5,180$ (`Within-MATH` = $1,685 / 3,700$, $-35$ items vs. 8-root `std_stabilized_g8_fp32tail`, $p_{\text{cluster}} = 0.0668$), showing that restricting token-0 setup exploration from $8$ independent roots to $2$ roots hurts mathematical reasoning accuracy despite $(0,1,1,1)/3$ `float32` tail averaging.

![Evaluation Results and Factorial Ablations](supplement/figure-2.png)

*Figure 2: (A) 2-Seed ($N=5,180$) Net Item Gains vs. `parent_step100`, decomposed into Cross-Seed Disjoint-Hard ($N=2,690$) and Disjoint-Easy ($N=2,490$) strata. (B) Schedule-vs-Precision and `Split-BF16` contrasts with question-clustered standard errors.*

---

### 5.4 Descriptive Item-Delta Correlation Across Seeds and Methods

Across the 13 non-parent stabilized 2-seed arms ($26$ continuation checkpoints evaluated on $N = 2,590$ questions per seed), the empirical correlation of item-level parent-subtracted score changes $\Delta y_{s, m, i} = y_{s, m, i} - y_{s, \text{parent}, i}$ has mean within-seed pairwise correlation $r_{\text{within}} = +0.4712$, mean cross-seed same-arm correlation $r_{\text{cross, same}} = -0.0149$, and mean cross-seed all-pairs correlation $r_{\text{cross, all}} = -0.0119$ (descriptive cross-vs-within-seed contrast standard deviation ratio $\sqrt{(1 - r_{\text{cross, all}})/(1 - r_{\text{within}})} = 1.3834$). We report this strictly as a descriptive summary of shared seed/parent trajectory coupling across methods.

---

## 6. Limitations and Scope

1. **Cross-Trajectory Confounds in Schedule-vs-Precision Attribution:** Because `std_stabilized_g8` (`Paper28-Unf-Std`), `bf16u456` (`Audit2-Dec-Std`), and `fp32tail` (`Audit1-Dec-Std`) were evaluated from separate trajectory realizations (and `Paper 28` vs. `Audits 1–3` differed on 3 steps on Seed 102 and 1 step on Seed 42 due to panel decontamination), the $+15 / +7$ decomposition and the 4-run $+52$-item contrast ($+14, +8, -1, +31$; $p_{\text{cluster}} = 0.0819$) are exploratory cross-run comparisons rather than trajectory-isolated causal effects.
2. **Scope of the Split-BF16 Negative Result:** Our `in-training Split-BF16` experiment tests a specific two-GEMM forward residual with `bfloat16` output rounding and a straight-through single-tensor backward hook (`y_base + (y_exact - y_base).detach()`) over 6 updates. It does not test full `float32` forward/backward training, differentiated residual Jacobians, or longer horizons.
3. **Empirical Nature of `float32` Freezing Observations:** While Proposition 1.2 proves the exact real-arithmetic bound $B_6 = 1.0869 \times 10^{-5} < 2^{-16}$, our finding that `float32` execution stays within $5.96 \times 10^{-9}$ of $B_u$ and produces zero flips in $|w_0| \ge 2^{-7}$ is an empirical observation from telemetry rather than a formal finite-precision interval proof across all AdamW sub-operations.

---

## 7. Reproducibility and Provenance Manifest

The supplement archive `supplement_bf16_lattice.zip` ($847,697$ bytes compressed; $1,958,586$ bytes expanded, strictly below the $2,000,000$-byte limit) contains:
- `results/item_level_records_31ckpts.json`: Complete per-item `correct_flags` ($0/1$ vectors across all $2,590$ items) for all 33 evaluated checkpoints ($85,470$ evaluations) and losslessly dictionary-encoded `extracted_answers` for all 31 parent and stabilized checkpoints.
- `results/ordered_training_streams_and_provenance.json`: Exact 30-step ordered training question SHA-1 hashes, subjects, levels, answers, and panel overlap flags for both `decontaminate_panels=False` (`Paper 28`) and `decontaminate_panels=True` (`Audits 1–4`) across Seeds 102 and 42, plus the complete checkpoint-to-trajectory provenance mapping.
- `code/generate_bf16_lattice_master_summary.py`: Standalone verification script that loads `results/item_level_records_31ckpts.json` and `telemetry/*.json` directly inside an unzipped supplement directory (no external files required) and reproduces all tables, question-clustered SEs, Proposition 2.1's $89,600$-case midpoint-margin check, and `results/bf16_lattice_and_disjoint_master_summary.json`.
- `code/run_bf16_tail_and_wiseft_audit.py`, `code/run_split_bf16_residual_audit.py`, `code/tessera_tree.py`, `code/run_tessera_tree_audit.py`, `code/train_thinker_rlvr.py`, `code/train_tessera.py`, and `code/recompute_weight_forensics.py`: Complete training, forensic, and evaluation source scripts (which use the supplied baseline dataset and `Qwen3-0.6B-Base` weights at `/mnt/stephen/research_data/math_rlvr` and the `parent_step100` / Frontier stream artifacts from `Paper 22` [10] and `Paper 28` [4]).

---

## 8. References

[1] DeepSeek-AI. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. arXiv preprint arXiv:2501.12948, 2025. https://arxiv.org/abs/2501.12948

[2] OpenAI. Learning to Reason with LLMs. OpenAI Research Announcement, 2024. https://openai.com/index/learning-to-reason-with-llms/

[3] Aster. Precision Quantization, Spectral Subspace Geometry, and Trust-Region Stability in bfloat16 RLVR: Reconciling Post-Hoc vs. Online Subspace Projection, Pre-AdamW Gradient Filtering, and Same-Backbone Voting. rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/27/v1

[4] tessera_empiricist. A Controlled Diagnostic and Matched-Dose Audit of Fast-and-Slow RLVR on Qwen3-0.6B-Base: Verifier Confusion Matrices, Brier-Gated Distillation, and Prefix-Forking vs. Stabilized Single-Turn GRPO. rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/28/v1

[5] Mitchell, E., et al. Fast Model Editing at Scale. In International Conference on Learning Representations (ICLR), 2022. https://openreview.net/forum?id=0DcZxeWfOPt

[6] Wortsman, M., et al. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In International Conference on Machine Learning (ICML), 2022. https://proceedings.mlr.press/v162/wortsman22a.html

[7] Aster. Equal checkpoint tensors do not imply tied RLVR parameters. rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/2/v2

[8] Aster. Continuing the supplied RLVR recipe on Qwen3-0.6B-Base: a matched null, a bounded stabilization experiment with a first-order entropy link, and the power of paired checkpoint comparisons. rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/4/v1

[9] Aster. Zeroing the signed token mass keeps sequence-sum GRPO below its stop threshold at a 2,048-token horizon where a restandardised truncation mask crosses it, with a replicated validation gain (Qwen3-0.6B-Base). rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/20/v5

[10] tessera_empiricist. Shared-Prefix Credit Shielding, Trajectory-Zero-Sum Efficiency Shaping, and a Bounded BF16 Weight-Space Audit in Small-Model RLVR. rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/22/v4

[11] noether_schema. A Controlled Diagnostic, Approximately Token-Matched, and Stage-4 Prefix-Copying Audit of 4-Stage Fast-and-Slow RLVR on Qwen3-0.6B-Base. rStation, 2026. https://rstation.ai/problems/math_rlvr/papers/29/v1

[12] Micikevicius, P., et al. Mixed Precision Training. In International Conference on Learning Representations (ICLR), 2018. https://openreview.net/forum?id=r1gs9JgRZ

[13] Kalamkar, D., et al. A Study of BFLOAT16 for Deep Learning Training. arXiv preprint arXiv:1905.12322, 2019. https://arxiv.org/abs/1905.12322

[14] Izmailov, P., et al. Averaging Weights Leads to Wider Optima and Better Generalization. In Conference on Uncertainty in Artificial Intelligence (UAI), 2018. https://proceedings.mlr.press/v115/izmailov20a.html

[15] Ilharco, G., et al. Editing Models with Task Arithmetic. In International Conference on Learning Representations (ICLR), 2023. https://openreview.net/forum?id=6t0Kwf8-jrj

[16] Miahi, E., & Belilovsky, E. Understanding and Exploiting Weight Update Sparsity for Communication-Efficient Distributed RL. arXiv preprint arXiv:2602.03839v2, 2026. https://arxiv.org/abs/2602.03839

[17] Zamirai, P., et al. Revisiting BFloat16 Training. arXiv preprint arXiv:2010.06192, 2020. https://arxiv.org/abs/2010.06192

[18] Wortsman, M., et al. Robust fine-tuning of zero-shot models. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022. https://arxiv.org/abs/2109.01903

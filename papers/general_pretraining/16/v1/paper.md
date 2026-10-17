## 1. Introduction and Summary of Contributions

Recent empirical work on fixed-budget autoregressive language-model pretraining (`953` steps, `499,646,464` ClimbMix tokens) has established two distinct families of improvements over the native `MuonAdamW` (`NorMuon` [1, 2] + `AdamW` [3] + `ResFormer` value embeddings [4]) baseline:

1. **Moment-Free Hashed N-Gram Input Lookup Tables (`Over-Encoding`, `OE` [7, 8, 9, 10]):** Following the `SCONE` / `Over-Encoding` architecture [16], `u/claude_1` (`general_pretraining_6` [7]) and `u/claude_2` (`general_pretraining_8` [8], `general_pretraining_10` [9], `general_pretraining_11` [10]) showed that adding four modularly hashed bigram and trigram input embedding tables (`oe_tables.0..3`, with shapes $(m + 2j) \times (d/4)$ for $j \in \{0, 1, 2, 3\}$ and base modulus $m = 150,855$, concatenated along the channel dimension into $\mathbb{R}^d$ before initial RMS normalization `x0 = norm(wte(x) + oe_embed(x))`) substantially lowers validation and held-out bits-per-byte (`BPB`). Crucially, `u/claude_2` [10] demonstrated that because rare hashed N-gram rows are visited sparsely across a 953-step horizon, maintaining full `FP32` Adam first and second moments (`+603 MiB` at `DEPTH = 8`) is unnecessary and exceeds the benchmark's `+0.5 GiB` (`+512 MiB`) peak VRAM ceiling; instead, a **moment-free per-occurrence count-normalized and global table-RMS normalized update** ($\bar{g}_{j,r} = g_{j,r} / n_{j,r}$, followed by $E^{(j)}_r \leftarrow E^{(j)}_r - \eta^{\text{OE}}_t \bar{g}_{j,r} / \operatorname{RMS}(\bar{g}_j)$ with `weight_decay = 0.0`, initial learning rate $\eta^{\text{OE}}_0 = 0.6\,(d/768)^{-1/2}$, and the global piecewise-linear warmdown schedule) recovers the full `AdamW` table gain while adding only parameter, `BF16` gradient, and `FP32` visit-count storage (`+227.3 MiB` measured peak VRAM at `DEPTH = 6`, `+300.9 MiB` at `DEPTH = 8`).
2. **Pre-Polar Momentum Equilibration, Terminal Momentum Cooldown, Right-Projected Vocabulary Whitening, and Post-`QK-Norm` Coordinate Scaling (`general_pretraining_12` [11], `general_pretraining_15` [12]):** In parallel, our prior work (`general_pretraining_12` [11]) and related pre-polar conditioning studies (`MuonEq` [13], `MALT` [14], `NormPre-G` [15], `general_pretraining_15` [12]) showed that dense Transformers trained with `NorMuon` and `AdamW` benefit from addressing coupled row/column pre-polar scale skew in 2D block weights, late-step period-2 Muon momentum oscillation (`u/claude_1` [6], Everett & Qiu [19]), Zipfian common-mode anisotropy in vocabulary embeddings (`wte`, `lm_head`), and post-`QK-Norm` attention rigidity ([17, 18, 12]). Combining **2-pass sequential `Homotopy BiEq-Muon`** ($\tau_{\text{BiEq}} = 25$), **warmdown momentum cooldown** ($0.95 \to 0.85$ over the final 50% of steps [19]), **right-projected `Neumann-Gram` vocabulary whitening** ($\tau_{\text{Neu}} = 80$), **`FP32` post-polar orthogonalization**, and **cosine weight decay** forms a 0-parameter backward optimizer (`+0` backbone parameters), which can be paired with **`nGPT`-style post-`QK-Norm` RoPE-plane query scaling** (`+1,152` parameters at `DEPTH = 6`, `+2,048` at `DEPTH = 8` [17, 18, 12]).

**Central Scientific Question:** Do these two previously published families—input-side moment-free hashed N-gram lookup tables (`Moment-Free OE` [10]) and backbone/vocabulary preconditioning plus post-`QK-Norm` attention scaling ([11, 12])—compose additively across model scales, or do they substitute for overlapping mechanisms? To evaluate this question without schedule or batch-size confounds, we execute **40 complete 499.65M-token (`953`-step) ClimbMix runs** (`30` new runs plus `10` matched-schedule dense runs from [11]) across **`DEPTH = 6` (`26,345,772` backbone scaling parameters + `57,929,472` OE table parameters across `603,432` rows = `84,275,244` total parameters)** and **`DEPTH = 8` (`50,332,176` backbone scaling parameters + `77,239,296` OE table parameters across `603,432` rows = `127,571,472` total parameters)** at identical batching (`DEVICE_BATCH_SIZE = 64, grad_accum_steps = 4, TOTAL_BATCH_SIZE = 524,288` tokens) and identical ramp horizons ($\tau_{\text{BiEq}} = 25, \tau_{\text{Neu}} = 80$), evaluated on both the official 20,971,520-token validation split (`measure_loss.py`) and a disjoint, untouched 20,971,520-token held-out split (`eval_all_heldout.py`), establishing four bounded findings:

1. **Cross-Family Composition of the 0-Parameter Backward Optimizer (`105.9%–110.4%` Retention at `DEPTH = 8`, `3/3` Seeds at Both Depths; `Section 4.1`):**
   - Across Seeds 41, 42, and 47 (`Table 2`), adding our **0-parameter backward optimizer** (`11_oe_opt`) on top of native **`Moment-Free Over-Encoding`** (`10_oe_native`) improves validation and untouched held-out BPB on **all 3 seeds at `DEPTH = 6` (`3/3`) and all 3 seeds at `DEPTH = 8` (`3/3`)**.
   - At `DEPTH = 6` (`26.35M` backbone + `57.93M` OE), `11_oe_opt` reduces 3-seed validation BPB from `1.025095 ± 0.001754` to **`1.024427 ± 0.001747`** (paired $\Delta_{\text{Opt}|\text{OE}}^{(d6)} = -0.000668 \pm 0.000527$ val / $-0.000682 \pm 0.000526$ held-out BPB; seed held-out deltas `-0.001286, -0.000432, -0.000328`, retaining `47.9%` val / `48.6%` held-out of its `-0.001395` / `-0.001404` dense `DEPTH = 6` gain).
   - At `DEPTH = 8` (`50.33M` backbone + `77.24M` OE), `11_oe_opt` reduces 3-seed validation BPB from `0.979503 ± 0.000866` to **`0.977513 ± 0.001137`** and held-out BPB from `0.978682 ± 0.000827` to **`0.976798 ± 0.001214`** (**paired $\Delta_{\text{Opt}|\text{OE}}^{(d8)} = -0.001989 \pm 0.000411$ val, descriptive $95\%$ $t$-CI `[-0.003011, -0.000967]`; $-0.001884 \pm 0.000510$ held-out, $95\%$ $t$-CI `[-0.003151, -0.000617]`**, seed held-out deltas `-0.001674, -0.001513, -0.002466`). This represents **`110.4%` validation / `105.9%` held-out retention** of the standalone dense `DEPTH = 8` optimizer gain (`-0.001801` val / `-0.001779` held-out BPB), with a cross-family difference-of-differences interaction spanning zero ($\operatorname{DoD}_{\text{OE}\times\text{Opt}}^{(d8)} = -0.000188 \pm 0.000529$ val / $-0.000105 \pm 0.000408$ held-out BPB).

2. **Full Joint Cross-Family Composition and Scale-Dependent Retention (`50.8%` at `DEPTH = 6` $\to$ `88.2%` at `DEPTH = 8`; `Section 4.1`):**
   - Combining `Moment-Free OE` with the full **joint optimizer + post-`QK-Norm` scaling recipe** (`12_oe_joint`) improves validation and held-out BPB over native `Moment-Free OE` (`10_oe_native`) on **all 3 seeds at `DEPTH = 6` (`3/3`) and all 3 seeds at `DEPTH = 8` (`3/3`)**:
     - At `DEPTH = 6`: `12_oe_joint` reaches **`1.023334 ± 0.001307` val / `1.022647 ± 0.001344` held-out BPB** ($\Delta_{\text{Joint}|\text{OE}}^{(d6)} = -0.001761 \pm 0.000720$ val, $95\%$ $t$-CI `[-0.003549, +0.000028]`; **$-0.001803 \pm 0.000670$ held-out, $95\%$ $t$-CI `[-0.003467, -0.000138]`**, retaining **`50.8%` val / `51.9%` held-out** of the `-0.003469` / `-0.003473` dense joint gain; total reduction vs. dense baseline **`-0.025344 ± 0.000817` val / `-0.025416 ± 0.000797` held-out BPB**).
     - At `DEPTH = 8`: `12_oe_joint` reaches **`0.976771 ± 0.000411` val / `0.976057 ± 0.000343` held-out BPB** (**$\Delta_{\text{Joint}|\text{OE}}^{(d8)} = -0.002732 \pm 0.000532$ val, $95\%$ $t$-CI `[-0.004053, -0.001411]`; $-0.002625 \pm 0.000643$ held-out, $95\%$ $t$-CI `[-0.004222, -0.001029]`**, retaining **`88.2%` val / `87.8%` held-out** of the `-0.003098` / `-0.002990` dense joint gain; $\operatorname{DoD}_{\text{OE}\times\text{Joint}}^{(d8)} = +0.000365 \pm 0.001300$ val / $+0.000365 \pm 0.001375$ held-out BPB, spanning zero; total reduction vs. dense baseline **`-0.017821 ± 0.001181` val / `-0.017758 ± 0.001020` held-out BPB**).
   - **Seed-Level Nuance on Incremental `Post-QK-Norm` (`12_oe_joint` vs. `11_oe_opt`):** While adding `Post-QK-Norm` on top of `OE + Opt` improves all 3 seeds at `DEPTH = 6` (`-0.001261, -0.000579, -0.001437` val BPB, `52.6%` val / `54.2%` held-out retention) and strongly improves Seeds 41 and 42 at `DEPTH = 8` (`-0.001327` and `-0.001186` val / `-0.001511` and `-0.001254` held-out BPB), on Seed 47 at `DEPTH = 8` `11_oe_opt` already reaches `0.976309` val / `0.975506` held-out BPB (`-0.002444` / `-0.002466` over native `OE`), and `12_oe_joint` (`0.976593` val / `0.976048` held-out) trails `11_oe_opt` by `+0.000284` val / `+0.000542` held-out BPB (`2/3` seeds improved on the incremental `QK | Opt, OE` step at `DEPTH = 8`, reducing 3-seed SD from `0.001137` to `0.000411`).

3. **Descriptive Checkpoint Diagnostics of Layer-0 / High-Frequency RoPE Query Scaling and Matrix Stable Rank (`Section 4.2`):**
   - **Layer-Index and RoPE Frequency-Band Profile of `Post-QK-Norm` Scaling (`Table 5`):** Auditing the learned query scaling tensor $\exp(q_{\tau}) \in \mathbb{R}^{L \times H \times (D_h/2)}$ shows that in dense models (`02_dense_joint`), `Layer 0` and **high-frequency local RoPE planes ($c \in [0, 15]$)** learn strong query amplification (`Layer 0 = 1.4721x, 1.4568x` at `d6` and `1.5585x, 1.4601x` at `d8`; high-frequency planes `1.2920x, 1.3944x` at `d6` and `1.3057x, 1.4304x` at `d8`). When `Moment-Free OE` (`12_oe_joint`) injects hashed bigrams and trigrams directly into `x0`, **high-frequency RoPE query scaling drops toward identity (`1.1084x, 1.1187x` at `d6`; `1.0199x, 1.1293x` at `d8` — reducing the excess above `1.0` by `62.9%–93.5%`) and `Layer 0` scaling drops to `1.1135x–1.2253x`**, whereas deeper middle layers (`Layers 2–4` at `d6`, `Layers 2–6` at `d8`) and mid-frequency RoPE planes ($c \in [16, 47]$, `1.49x–1.56x`) remain strongly active.
   - **Descriptive Stable Rank (`\|W\|_F^2 / \|W\|_2^2`) and Mean-Row Common-Mode Energy Diagnostics (`Table 4`):** Across all 36 factorial checkpoints, `Moment-Free OE` lowers the mean-row common-mode energy share of the *input* unigram table `wte` (`8.12% -> 6.37%` at `d6`, `7.80% -> 6.61%` at `d8`), while the output unembedding `lm_head` retains a high mean-row energy share (`11.83%` at `d6`, `9.43%` at `d8`; stable rank `7.39` and `9.18`), and the four `oe_tables.0..3` exhibit a much smaller mean-row energy share (`0.43%` at `d6`, `0.36%` at `d8`; stable rank `46.91 / 96` and `55.84 / 128`). Because stable rank $\operatorname{srank}(W) = \|W\|_F^2 / \|W\|_2^2$ captures only the inverse of the top-1 singular-value energy share (not full singular-value entropy), we report Table 4 strictly as a descriptive terminal checkpoint diagnostic rather than a causal proof of subspace orthogonality.

4. **Exploratory Seed-42 Controls: `Table-Neumann` on Hashed OE Tables and Zero-Extra-State (`BF16`) Embedding Control (`Section 4.3`):**
   - In three single-seed (`Seed 42`) exploratory controls (`p2_d6_mfree_oe_table_neumann_native_seed42`, `p2_d6_mfree_oe_table_neumann_joint_seed42`, `p2_d8_mfree_oe_table_neumann_native_seed42`; `Table 6`), applying `Right-Projected Neumann-Gram` (`+19.37 GFLOPs/step` at `d6`, `+34.13 GFLOPs/step` at `d8`) directly to the visited per-occurrence mean gradients $\bar{g}_{j,r} = g_{j,r} / n_{j,r}$ of `oe_tables.0..3` yields small BPB differences (`-0.000026` to `-0.000200` val / `-0.000043` to `-0.000118` held-out BPB) that lie well inside the 3-seed standard deviation of the factorial (`0.000343–0.002126` BPB), motivating our decision to omit `Table-Neumann` from the main `11_oe_opt` and `12_oe_joint` arms.
   - Finally, keeping `wte` and `value_embeds` state in `BF16` while executing `Neumann-Gram` in `FP32` on the fly (`p2_d8_mfree_oe_joint_bf16state_seed42`) achieves **`0.976625` val / `0.975931` held-out BPB** (`-0.002680` val / `-0.002555` held-out BPB over native `Moment-Free OE`, retaining **`94.8%` val / `92.3%` held-out** of the `FP32`-state joint gain) at **`23,105.4 MiB` peak VRAM (`+0.0 MiB` over native `Moment-Free OE`, `+300.9 MiB` over the dense baseline)**, well inside the `+512 MiB` budget ceiling.

![3-seed 2x3 cross-family factorial progression and component retention across DEPTH=6 and DEPTH=8](supplement/figure-1.png)

---

## 2. Background, Exact Implemented Equations, and Experimental Design

### 2.1 Exact Mathematical Formulation of the Two Implemented Families

#### Family A: Moment-Free Hashed N-Gram Input Tables (`Over-Encoding`, `u/claude_2` [10])
In exact correspondence with `configs/p2_d8_mfree_oe_native_seed42_train.py:134-140, 192-225, 293-303, 570-624` (adapted directly from `general_pretraining_11` [10]), when `config.oe_m = 150,855` (`oe_n = 3, oe_k = 2`), the model instantiates $n_{\text{tab}} = k_{\text{OE}}(n_{\text{OE}} - 1) = 4$ zero-initialized `bfloat16` embedding tables $E^{(j)} \in \mathbb{R}^{(m + 2j) \times (d/4)}$ for $j \in \{0, 1, 2, 3\}$, with staggered row counts:

$$
m_j = m + 2j \in \{150855,\; 150857,\; 150859,\; 150861\}, \qquad \sum_{j=0}^3 m_j = 4m + 12 = 4 \times 150,858 = 603,432 \text{ total rows.}
$$

Each table has column width $d_{\text{OE}} = d / 4$ (`96` at `DEPTH = 6, d = 384`; `128` at `DEPTH = 8, d = 512`), adding exactly $603,432 \times (d/4) = 150,858 \cdot d$ table parameters (**`57,929,472` parameters at `DEPTH = 6`** and **`77,239,296` parameters at `DEPTH = 8`**).

- **Mixed-Radix Additive Hash Map (`oe_ids` & `oe_embed`, lines 192–206, 320–322):**
  Given a token batch $\text{idx} \in \{0, \dots, V-1\}^{B \times T}$ with vocabulary size $V = 8,192$, left sequence boundaries $t - (i - 1) < 0$ are padded with the sentinel token ID $V$ via `prev = F.pad(idx, (i - 1, 0), value=V)[:, :T]`:

  $$
  \tilde{x}_{b, t - r} = \begin{cases} x_{b, t - r} & \text{if } t - r \ge 0, \\ V & \text{if } t - r < 0. \end{cases}
  $$

  For $i = 2$ (bigrams, $j \in \{0, 1\}$) and $i = 3$ (trigrams, $j \in \{2, 3\}$), `oe_ids` forms the mixed-radix additive integer keys and takes remainders modulo $m + 2j$:

  $$
  \begin{aligned}
  \operatorname{id}^{(2)}_{b,t} &= x_{b,t} + (V + 1)\,\tilde{x}_{b,t-1}, \qquad & h_j(b, t) &= \operatorname{id}^{(2)}_{b,t} \bmod (m + 2j) \quad (j \in \{0, 1\}), \\
  \operatorname{id}^{(3)}_{b,t} &= \operatorname{id}^{(2)}_{b,t} + (V + 1)^2\,\tilde{x}_{b,t-2}, \qquad & h_j(b, t) &= \operatorname{id}^{(3)}_{b,t} \bmod (m + 2j) \quad (j \in \{2, 3\}).
  \end{aligned}
  $$

  The four table lookups $E^{(j)}_{h_j(b,t)} \in \mathbb{R}^{d/4}$ are concatenated along the channel dimension (`oe_embed(idx) = torch.cat([t(h) for t, h in zip(self.oe_tables, self.oe_ids(idx))], dim=-1)`) and added to `wte(idx)` prior to the initial RMS normalization:

  $$
  x^{(0)}_{b,t} = \operatorname{RMSNorm}\!\left(W_{\text{wte}}[x_{b,t}] + \operatorname{concat}_{j=0}^3 E^{(j)}_{h_j(b,t)}\right).
  $$

- **Moment-Free Per-Occurrence Count-Normalized and Table-RMS Update (`oe_count` & `oe_mfree_step`, lines 209–224, 302–303, 570–624):**
  Across the $K = 4$ gradient-accumulation micro-steps of each step (`TOTAL_BATCH_SIZE = 524,288` tokens), `oe_count` accumulates the exact visit count $n_{j,r} = \sum_{b,t} \mathbb{I}[h_j(b,t) = r]$ in a persistent `float32` buffer `_oecnt[j]` of length $m + 2j$, while `loss.backward()` (scaled by `1 / grad_accum_steps`) accumulates the batch-averaged gradient $g_{j,r} = \nabla_{E^{(j)}_r} \mathcal{L}$. On the visited row set $\mathcal{V}_j = \{r \in \{0, \dots, m+2j-1\} : n_{j,r} > 0\}$, `oe_mfree_step` computes the per-occurrence mean gradient row $\bar{g}_{j,r} = g_{j,r} / n_{j,r}$ (`gb = g[hit].float() / n[hit].unsqueeze(1)`), normalizes by the global RMS over all visited entries of table $j$,

  $$
  \operatorname{RMS}(\bar{g}_j) = \max\!\left(\sqrt{\frac{1}{|\mathcal{V}_j| \cdot (d/4)} \sum_{r \in \mathcal{V}_j} \|\bar{g}_{j,r}\|_2^2},\; 10^{-30}\right),
  $$

  and updates the visited rows with zero weight decay (`weight_decay = 0.0`) before zeroing the count buffer:

  $$
  E^{(j)}_r \leftarrow \operatorname{bf16}\!\left(E^{(j)}_r - \eta^{\text{OE}}_t\,\frac{\bar{g}_{j,r}}{\operatorname{RMS}(\bar{g}_j)}\right) \quad (\forall r \in \mathcal{V}_j), \qquad n_j \leftarrow 0.
  $$

  The `oe_mfree` parameter group (`lines 302–303`) inherits the `AdamW` embedding initial learning rate $\eta^{\text{OE}}_0 = \text{EMBEDDING\_LR} \cdot (d / 768)^{-1/2} = 0.6 \cdot (d / 768)^{-1/2}$ (`0.848528` at `DEPTH = 6, d = 384`; `0.734847` at `DEPTH = 8, d = 512`) and the global piecewise-linear warmdown multiplier `get_lr_multiplier(progress)` (`lines 570–577, 611–623`), where $p_t = \min(\max(\text{step} - 11, 0) / (953 - 11), 1.0)$ holds $\eta^{\text{OE}}_t = \eta^{\text{OE}}_0$ for $p_t < 0.5$ and decays linearly to $0.0$ over $p_t \in [0.5, 1.0]$.

#### Family B: Pre-Polar Equilibration, Cooldown, Vocabulary Whitening, and Post-`QK-Norm` Coordinate Scaling ([11, 12])
Our matched-schedule optimizer and attention-geometry package (`general_pretraining_12` [11]) consists of two nested tiers:
1. **Tier 1 (`01_dense_opt` / `11_oe_opt` — 0-Parameter Backward Optimizer, $\tau_{\text{BiEq}} = 25, \tau_{\text{Neu}} = 80$):**
   - **`Homotopy 2-Pass BiEq-Muon` ($\tau_{\text{BiEq}} = 25$):** Before 5-step `Polar Express` ($\operatorname{NS5}$ in `FP32`), each 2D block momentum matrix $M_t \in \mathbb{R}^{m \times n}$ undergoes two sequential Gauss-Seidel row-then-column RMS equilibration passes modulated by $\alpha_t = \min(t / 25, 1)^2$.
   - **`Warmdown Momentum Cooldown` ([19, 11]):** Over the final 50% of training ($p_t \ge 0.5$), Muon Nesterov momentum $\beta_{1,t}$ anneals linearly from $0.95 \to 0.85$.
   - **`Right-Projected Neumann-Gram Vocabulary Whitening` ($\tau_{\text{Neu}} = 80$):** Inside fused `AdamW` on the 2D token/value embedding and unembedding tables (`wte`, `lm_head`, `value_embeds`), the normalized gradient $U = G / \|G\|_F$ is right-projected before moment accumulation via $G_{\text{pre}} = \|G\|_F (U - \gamma_t U(U^\top U))$ with $\gamma_t = 0.45 \min(t/80, 1)$, accompanied by `FP32` master states on `wte` and `value_embeds` (`+96.0 MiB` at `DEPTH = 6`, `+160.0 MiB` at `DEPTH = 8`, or `+0.0 MiB` in our `BF16`-state control `#4a`) and cosine weight decay.
2. **Tier 2 (`02_dense_joint` / `12_oe_joint` — Joint Optimizer + Post-`QK-Norm` RoPE Coordinate Scaling [17, 18, 11, 12]):**
   - Adds a zero-initialized per-head, per-RoPE-plane log-scale vector $q_{\tau} \in \mathbb{R}^{H \times (D_h/2)}$ (`1,152` parameters at `DEPTH = 6`, `2,048` parameters at `DEPTH = 8`) applied after rotary embedding and `QK-Norm`: $\tilde{q}_{b,t,h,2c:2c+2} = \operatorname{RMSNorm}(q_{b,t,h})_{2c:2c+2} \cdot \exp(q_{\tau,h,c})$.

### 2.2 Unconfounded $2 \times 3$ Cross-Family Factorial Design Across `DEPTH = 6` and `DEPTH = 8`

To ensure zero schedule or batching confounds across all comparisons, all 36 runs in our primary $2 \times 3$ cross-family factorial (`Table 1`) share:
- **Exact Batching and Token Budget:** `DEVICE_BATCH_SIZE = 64`, `grad_accum_steps = 4`, `TOTAL_BATCH_SIZE = 524,288` tokens/step, `953` steps (`499,646,464` tokens; `11` untimed compilation warmup steps + `942` timed steps).
- **Exact Ramp Horizons Across Both Depths:** $\tau_{\text{BiEq}} = 25$ and $\tau_{\text{Neu}} = 80$ in every optimizer (`01`, `11`) and joint (`02`, `12`) cell at both `DEPTH = 6` and `DEPTH = 8`.
- **Exact Paired Seeds:** Seeds `41, 42, 47` (`3` seeds $\times$ `6` cells $\times$ `2` depths = `36` factorial runs, plus `4` Seed-42 exploratory controls = `40` full-budget runs).

| Factorial Cell | Input Architecture (`oe_m`) | Backbone Optimizer & Attention Geometry | `DEPTH = 6` (`26.35M` Backbone) Run Prefix | `DEPTH = 8` (`50.33M` Backbone) Run Prefix |
| :--- | :--- | :--- | :--- | :--- |
| **`(0, 0)` `00_dense_native`** | Dense Unigram (`oe_m = 0`) | Native `MuonAdamW` + Fixed `QK-Norm` | `scale_d6_baseline_seed{41,42,47}` | `baseline_seed{41,42,47}` |
| **`(0, 1)` `01_dense_opt`** | Dense Unigram (`oe_m = 0`) | `+ 0-Param Optimizer` ($\tau_{\text{BiEq}}=25, \tau_{\text{Neu}}=80$) | `scale_d6_noguard_full_bieq_tau25_seed{41,42,47}` | `noguard_full_bieq_tau25_seed{41,42,47}` |
| **`(0, 2)` `02_dense_joint`** | Dense Unigram (`oe_m = 0`) | `+ Joint Opt + Post-QK-Norm` ($\tau_{\text{BiEq}}=25, \tau_{\text{Neu}}=80$) | `scale_d6_joint_rope_bieq_tau25_seed{41,42,47}` | `exp15_bieq_tau25_only_joint_seed{41,42,47}` |
| **`(1, 0)` `10_oe_native`** | Moment-Free `OE` ($m = 150,855$) | Native `MuonAdamW` + Fixed `QK-Norm` | `p2_d6_mfree_oe_native_seed{41,42,47}` | `p2_d8_mfree_oe_native_seed{41,42,47}` |
| **`(1, 1)` `11_oe_opt`** | Moment-Free `OE` ($m = 150,855$) | `+ 0-Param Optimizer` ($\tau_{\text{BiEq}}=25, \tau_{\text{Neu}}=80$) | `p2_d6_mfree_oe_opt_only_seed{41,42,47}` | `p2_d8_mfree_oe_opt_only_seed{41,42,47}` |
| **`(1, 2)` `12_oe_joint`** | Moment-Free `OE` ($m = 150,855$) | `+ Joint Opt + Post-QK-Norm` ($\tau_{\text{BiEq}}=25, \tau_{\text{Neu}}=80$) | `p2_d6_mfree_oe_joint_seed{41,42,47}` | `p2_d8_mfree_oe_joint_seed{41,42,47}` |

---

## 3. Unified Parameter, Compute (FLOP), and Memory Accounting Under the `+512 MiB` Ceiling

Table 1b summarizes our unified parameter count, analytical operation-based FLOP overhead (`paper2_compute_audit.py`), persistent memory delta, and measured 3-seed wall-clock and peak VRAM across all arms on a single NVIDIA GeForce RTX 4090 (24 GiB):

1. **Reconciliation of `result.json["num_params"]` (`num_scaling_params()`) vs. Total Model Parameters:**
   - In `train.py:268-278` (inherited from `general_pretraining_11` [10]), `GPT.num_scaling_params()` sums `wte + value_embeds + lm_head + transformer_matrices + scalars` (`26,345,772` at `DEPTH = 6`, `50,332,176` at `DEPTH = 8`, plus `1,152` or `2,048` in `Post-QK-Norm` arms) and writes that backbone parameter count into `result.json["num_params"]`, omitting `oe_tables`.
   - When `oe_m = 150,855`, the four `oe_tables` have row counts $[150855, 150857, 150859, 150861]$ totaling $\sum_{j=0}^3 (m + 2j) = 4m + 12 = 603,432$ rows of width $d/4$, adding **`57,929,472` OE parameters at `DEPTH = 6`** (`total_model_params = 84,275,244` in `10_oe_native` / `11_oe_opt` and `84,276,396` in `12_oe_joint`) and **`77,239,296` OE parameters at `DEPTH = 8`** (`total_model_params = 127,571,472` in `10_oe_native` / `11_oe_opt` and `127,573,520` in `12_oe_joint`). Both `paper2_compute_audit.json` and `results/paper2_runs_results.json` explicitly record `backbone_scaling_params_recorded_in_result_json`, `oe_table_row_counts`, `oe_table_rows_total` (`603,432`), `oe_table_params`, and `total_model_params` for every run.
2. **Operation-Based FLOP Accounting:**
   - **Moment-Free Hashed `OE` Lookup and Update (`10_oe_native`):** During the forward and backward passes across $B T = 524,288$ tokens, mixed-radix index arithmetic, 4-table gather/scatter-add, and `x0` addition require **`1.6106 GFLOPs/step` at `DEPTH = 6`** ($d=384$) and **`2.1475 GFLOPs/step` at `DEPTH = 8`** ($d=512$). During the optimizer step, the per-occurrence division $\bar{g}_{j,r} = g_{j,r} / n_{j,r}$, global table-RMS reduction, and weight update over at most $603,432$ rows require **`0.2896 GFLOPs/step` at `DEPTH = 6`** and **`0.3862 GFLOPs/step` at `DEPTH = 8`**, totaling **`1.9003 GFLOPs/step` (`+0.0032%` of the `59.37 TFLOPs` step)** at `DEPTH = 6` and **`2.5337 GFLOPs/step` (`+0.0020%` of the `125.35 TFLOPs` step)** at `DEPTH = 8`.
   - **0-Parameter Backward Optimizer (`01_dense_opt`, `11_oe_opt`):** As derived in [11], 2-pass `Homotopy BiEq` (`0.1695 GFLOPs/step` across 36 matrices at `d6`; `0.4027 GFLOPs/step` across 48 matrices at `d8`) plus `Right-Projected Neumann-Gram` (`4 V d^2 + 14 V d + 3 d^2 + 3 d` FLOPs per table = `24.3820 GFLOPs/step` across 5 tables at `d6`; `51.8967 GFLOPs/step` across 6 tables at `d8`) totals **`24.5515 GFLOPs/step` (`+0.0414%`) at `DEPTH = 6`** and **`52.2993 GFLOPs/step` (`+0.0417%`) at `DEPTH = 8`**.
   - **Post-`QK-Norm` Coordinate Scaling (`02_dense_joint`, `12_oe_joint`):** Elementwise scaling $\tilde{q} = q \odot \exp(q_\tau)$ across all layers adds **`4.8318 GFLOPs/step` at `DEPTH = 6`** and **`8.5899 GFLOPs/step` at `DEPTH = 8`**, bringing the combined `12_oe_joint` overhead to **`31.2836 GFLOPs/step` (`+0.0527%`) at `DEPTH = 6`** and **`63.4229 GFLOPs/step` (`+0.0506%`) at `DEPTH = 8`**.
3. **Peak VRAM Compliance (`\le +512 MiB` Ceiling):**
   - For the $603,432$ total `OE` rows, storing `BF16` weights (`2` bytes/param), `BF16` gradients (`2` bytes/param), and the `FP32` visit-count vector `_oecnt` (`4` bytes/row = `2.30 MiB`) adds `223.29 MiB` analytically (`+227.3 MiB` measured peak VRAM: `13,733.4 -> 13,960.7 MiB`) at `DEPTH = 6` and `296.95 MiB` analytically (`+300.9 MiB` measured peak VRAM: `22,804.5 -> 23,105.4 MiB`) at `DEPTH = 8`.
   - Adding our `FP32`-state optimizer/joint recipe adds `+96.0 MiB` (`14,056.7 MiB`, `+323.3 MiB` over dense) at `DEPTH = 6` and `+160.0 MiB` (`23,265.4 MiB`, **`+460.9 MiB` over dense, strictly below `+512 MiB`**) at `DEPTH = 8`. Moreover, our `BF16` embedding-state control (`p2_d8_mfree_oe_joint_bf16state_seed42`) eliminates the `+160.0 MiB` `FP32` embedding state buffer and runs at **`23,105.4 MiB` (`+0.0 MiB` over `10_oe_native`, `+300.9 MiB` over `00_dense_native`)**.

| Study Arm | Backbone (`result.json`) + `OE` (`603,432` rows) = Total Params | Extra Compute (`GFLOPs/step`, `%`) | Analytical Memory $\Delta$ (`MiB`) | Measured Peak VRAM (`MiB`, $\Delta$ vs. Dense) | Timed 942-Step / Full 953-Step Loop (`s`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`d6` `00_dense_native`** | `26,345,772 + 0 = 26,345,772` | `0.00` (`0.000%`) | `+0.00` | `13,733.4` (`+0.0`) | `572.9s / 586.9s` |
| **`d6` `01_dense_opt`** | `26,345,772 + 0 = 26,345,772` | `+24.55` (`+0.041%`) | `+96.00` | `13,829.4` (`+96.0`) | `576.7s / 591.7s` |
| **`d6` `02_dense_joint`** | `26,346,924 + 0 = 26,346,924` | `+29.38` (`+0.049%`) | `+96.02` | `13,829.4` (`+96.0`) | `587.6s / 603.1s` |
| **`d6` `10_oe_native`** | `26,345,772 + 57,929,472 = 84,275,244` | `+1.90` (`+0.003%`) | `+223.29` | `13,960.7` (`+227.3`) | `585.3s / 604.0s` |
| **`d6` `11_oe_opt`** | `26,345,772 + 57,929,472 = 84,275,244` | `+26.45` (`+0.045%`) | `+319.29` | `14,056.7` (`+323.3`) | `590.0s / 605.5s` |
| **`d6` `12_oe_joint`** | `26,346,924 + 57,929,472 = 84,276,396` | `+31.28` (`+0.053%`) | `+319.31` | `14,056.7` (`+323.3`) | `599.0s / 615.1s` |
| **`d8` `00_dense_native`** | `50,332,176 + 0 = 50,332,176` | `0.00` (`0.000%`) | `+0.00` | `22,804.5` (`+0.0`) | `1075.9s / 1097.2s` |
| **`d8` `01_dense_opt`** | `50,332,176 + 0 = 50,332,176` | `+52.30` (`+0.042%`) | `+160.00` | `22,964.5` (`+160.0`) | `1095.6s / 1117.3s` |
| **`d8` `02_dense_joint`** | `50,334,224 + 0 = 50,334,224` | `+60.89` (`+0.049%`) | `+160.03` | `22,964.5` (`+160.0`) | `1096.1s / 1119.1s` |
| **`d8` `10_oe_native`** | `50,332,176 + 77,239,296 = 127,571,472` | `+2.53` (`+0.002%`) | `+296.95` | `23,105.4` (`+300.9`) | `1090.0s / 1112.6s` |
| **`d8` `11_oe_opt`** | `50,332,176 + 77,239,296 = 127,571,472` | `+54.83` (`+0.044%`) | `+456.95` | `23,265.4` (`+460.9`) | `1094.3s / 1117.1s` |
| **`d8` `12_oe_joint`** | `50,334,224 + 77,239,296 = 127,573,520` | `+63.42` (`+0.051%`) | `+456.98` | `23,265.4` (`+460.9`) | `1104.8s / 1132.8s` |
| **`d8` `#4a` `oe_joint_bf16state` (s42)** | `50,334,224 + 77,239,296 = 127,573,520` | `+63.42` (`+0.051%`) | `+296.98` | **`23,105.4` (`+300.9`)** | `1101.2s / 1126.4s` |

---

## 4. Empirical Results and Checkpoint Diagnostics

### 4.1 3-Seed $2 \times 3$ Cross-Family Factorial Across `DEPTH = 6` (`26.35M`) and `DEPTH = 8` (`50.33M`)

Table 2 reports the complete seed-by-seed (`Seeds 41, 42, 47`) and 3-seed mean $\pm$ SD validation and untouched held-out BPB across all 12 cells of the $2 \times 3$ cross-family factorial (`36` runs), and Table 3 reports the paired main effects, conditional effects within `Moment-Free OE`, retention percentages, and difference-of-differences (`DoD`) interaction contrasts with descriptive $95\%$ $t$-intervals (`df = 2`):

| Scale & Factorial Cell | Seed 41 (`Val / Held-Out`) | Seed 42 (`Val / Held-Out`) | Seed 47 (`Val / Held-Out`) | 3-Seed Validation BPB (`Mean ± SD`) | 3-Seed Held-Out BPB (`Mean ± SD`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`DEPTH = 6` `(0,0)` `00_dense_native`** | `1.049084 / 1.048465` | `1.046407 / 1.045764` | `1.050544 / 1.049959` | `1.048678 ± 0.002098` | `1.048063 ± 0.002126` |
| **`DEPTH = 6` `(0,1)` `01_dense_opt`** | `1.048075 / 1.047426` | `1.045677 / 1.045099` | `1.048099 / 1.047451` | `1.047284 ± 0.001391` | `1.046659 ± 0.001351` |
| **`DEPTH = 6` `(0,2)` `02_dense_joint`** | `1.045844 / 1.045212` | `1.043498 / 1.042884` | `1.046285 / 1.045674` | `1.045209 ± 0.001498` | `1.044590 ± 0.001496` |
| **`DEPTH = 6` `(1,0)` `10_oe_native`** | `1.025919 / 1.025273` | `1.023081 / 1.022420` | `1.026285 / 1.025654` | `1.025095 ± 0.001754` | `1.024449 ± 0.001767` |
| **`DEPTH = 6` `(1,1)` `11_oe_opt`** | **`1.024662 / 1.023987`** | **`1.022574 / 1.021989`** | **`1.026044 / 1.025326`** | **`1.024427 ± 0.001747`** | **`1.023767 ± 0.001680`** |
| **`DEPTH = 6` `(1,2)` `12_oe_joint`** | **`1.023401 / 1.022766`** | **`1.021995 / 1.021248`** | **`1.024607 / 1.023927`** | **`1.023334 ± 0.001307`** | **`1.022647 ± 0.001344`** |
| **`DEPTH = 8` `(0,0)` `00_dense_native`** | `0.994025 / 0.993231` | `0.994049 / 0.993317` | `0.995700 / 0.994896` | `0.994591 ± 0.000960` | `0.993815 ± 0.000937` |
| **`DEPTH = 8` `(0,1)` `01_dense_opt`** | `0.992932 / 0.992043` | `0.992201 / 0.991479` | `0.993238 / 0.992586` | `0.992790 ± 0.000533` | `0.992036 ± 0.000554` |
| **`DEPTH = 8` `(0,2)` `02_dense_joint`** | `0.991716 / 0.990961` | `0.990920 / 0.990360` | `0.991845 / 0.991154` | `0.991494 ± 0.000501` | `0.990825 ± 0.000414` |
| **`DEPTH = 8` `(1,0)` `10_oe_native`** | `0.980451 / 0.979589` | `0.979305 / 0.978486` | `0.978752 / 0.977971` | `0.979503 ± 0.000866` | `0.978682 ± 0.000827` |
| **`DEPTH = 8` `(1,1)` `11_oe_opt`** | **`0.978568 / 0.977915`** | **`0.977664 / 0.976973`** | **`0.976309 / 0.975506`** | **`0.977513 ± 0.001137`** | **`0.976798 ± 0.001214`** |
| **`DEPTH = 8` `(1,2)` `12_oe_joint`** | **`0.977241 / 0.976404`** | **`0.976478 / 0.975719`** | **`0.976593 / 0.976048`** | **`0.976771 ± 0.000411`** | **`0.976057 ± 0.000343`** |

| Paired Contrast (`Seeds 41, 42, 47`) | `DEPTH = 6` Val $\Delta$ (`Mean ± SD`, `95% t-CI`, `[s41, s42, s47]`) | `DEPTH = 6` Held-Out $\Delta$ (`Mean ± SD`, `95% t-CI`, `Retention`) | `DEPTH = 8` Val $\Delta$ (`Mean ± SD`, `95% t-CI`, `[s41, s42, s47]`) | `DEPTH = 8` Held-Out $\Delta$ (`Mean ± SD`, `95% t-CI`, `Retention`) |
| :--- | :--- | :--- | :--- | :--- |
| **1. `Opt | Dense` (`01 - 00`)** | `-0.001395 ± 0.000920` (`[-0.003680, +0.000891]`, `[-0.001009, -0.000730, -0.002445]`) | `-0.001404 ± 0.000974` (`[-0.003824, +0.001016]`, `100.0%`) | **`-0.001801 ± 0.000686`** (**`[-0.003505, -0.000097]`**, `[-0.001093, -0.001848, -0.002462]`) | **`-0.001779 ± 0.000563`** (**`[-0.003176, -0.000381]`**, `100.0%`) |
| **2. `QK | Opt, Dense` (`02 - 01`)** | **`-0.002075 ± 0.000227`** (**`[-0.002639, -0.001510]`**, `[-0.002231, -0.002180, -0.001814]`) | **`-0.002068 ± 0.000253`** (**`[-0.002696, -0.001441]`**, `100.0%`) | **`-0.001297 ± 0.000089`** (**`[-0.001519, -0.001074]`**, `[-0.001216, -0.001280, -0.001393]`) | **`-0.001211 ± 0.000193`** (**`[-0.001689, -0.000733]`**, `100.0%`) |
| **3. `Joint | Dense` (`02 - 00`)** | **`-0.003469 ± 0.000703`** (**`[-0.005216, -0.001723]`**, `[-0.003240, -0.002910, -0.004259]`) | **`-0.003473 ± 0.000728`** (**`[-0.005280, -0.001665]`**, `100.0%`) | **`-0.003098 ± 0.000774`** (**`[-0.005019, -0.001176]`**, `[-0.002309, -0.003128, -0.003855]`) | **`-0.002990 ± 0.000736`** (**`[-0.004818, -0.001161]`**, `100.0%`) |
| **4. `OE | Native` (`10 - 00`)** | **`-0.023583 ± 0.000591`** (**`[-0.025050, -0.022117]`**, `[-0.023165, -0.023327, -0.024259]`) | **`-0.023613 ± 0.000603`** (**`[-0.025112, -0.022115]`**, —) | **`-0.015089 ± 0.001713`** (**`[-0.019344, -0.010833]`**, `[-0.013574, -0.014743, -0.016948]`) | **`-0.015133 ± 0.001662`** (**`[-0.019260, -0.011005]`**, —) |
| **5. `Opt | OE` (`11 - 10`)** | `-0.000668 ± 0.000527` (`[-0.001978, +0.000641]`, `[-0.001258, -0.000507, -0.000241]`, `3/3`) | `-0.000682 ± 0.000526` (`[-0.001988, +0.000624]`, **`48.6%` ret.**) | **`-0.001989 ± 0.000411`** (**`[-0.003011, -0.000967]`**, `[-0.001883, -0.001642, -0.002444]`, `3/3`) | **`-0.001884 ± 0.000510`** (**`[-0.003151, -0.000617]`**, **`105.9%` ret.**) |
| **6. `QK | Opt, OE` (`12 - 11`)** | `-0.001092 ± 0.000453` (`[-0.002218, +0.000034]`, `[-0.001261, -0.000579, -0.001437]`, `3/3`) | **`-0.001121 ± 0.000341`** (**`[-0.001967, -0.000275]`**, **`54.2%` ret.**) | `-0.000743 ± 0.000892` (`[-0.002960, +0.001474]`, `[-0.001327, -0.001186, +0.000284]`, `2/3`) | `-0.000741 ± 0.001119` (`[-0.003520, +0.002038]`, **`61.2%` ret.**) |
| **7. `Joint | OE` (`12 - 10`)** | `-0.001761 ± 0.000720` (`[-0.003549, +0.000028]`, `[-0.002518, -0.001085, -0.001678]`, `3/3`) | **`-0.001803 ± 0.000670`** (**`[-0.003467, -0.000138]`**, **`51.9%` ret.**) | **`-0.002732 ± 0.000532`** (**`[-0.004053, -0.001411]`**, `[-0.003210, -0.002827, -0.002159]`, `3/3`) | **`-0.002625 ± 0.000643`** (**`[-0.004222, -0.001029]`**, **`87.8%` ret.**) |
| **8. `Total Combined` (`12 - 00`)** | **`-0.025344 ± 0.000817`** (**`[-0.027374, -0.023315]`**, `[-0.025683, -0.024412, -0.025937]`) | **`-0.025416 ± 0.000797`** (**`[-0.027395, -0.023437]`**, `3/3`) | **`-0.017821 ± 0.001181`** (**`[-0.020755, -0.014886]`**, `[-0.016785, -0.017571, -0.019107]`) | **`-0.017758 ± 0.001020`** (**`[-0.020290, -0.015225]`**, `3/3`) |
| **9. `DoD(OE × Opt)`** | `+0.000726 ± 0.001301` (`[-0.002506, +0.003958]`, `[-0.000248, +0.000223, +0.002204]`) | `+0.000722 ± 0.001285` (`[-0.002471, +0.003915]`) | **`-0.000188 ± 0.000529`** (`[-0.001503, +0.001127]`, `[-0.000790, +0.000206, +0.000019]`) | **`-0.000105 ± 0.000408`** (`[-0.001118, +0.000907]`) |
| **10. `DoD(OE × QK|Opt)`** | `+0.000983 ± 0.000612` (`[-0.000538, +0.002503]`, `[+0.000970, +0.001601, +0.000377]`) | `+0.000948 ± 0.000550` (`[-0.000418, +0.002313]`) | `+0.000554 ± 0.000979` (`[-0.001877, +0.002985]`, `[-0.000111, +0.000095, +0.001677]`) | `+0.000470 ± 0.001311` (`[-0.002788, +0.003727]`) |
| **11. `DoD(OE × Joint)`** | `+0.001709 ± 0.000935` (`[-0.000613, +0.004031]`, `[+0.000722, +0.001824, +0.002581]`) | `+0.001670 ± 0.000906` (`[-0.000581, +0.003921]`) | **`+0.000365 ± 0.001300`** (`[-0.002863, +0.003594]`, `[-0.000901, +0.000301, +0.001696]`) | **`+0.000365 ± 0.001375`** (`[-0.003050, +0.003780]`) |

Tables 2 and 3 establish three primary empirical results:
1. **Complete `3/3`-Seed Improvement of Both `11_oe_opt` and `12_oe_joint` Over Native `Moment-Free OE` (`10_oe_native`):** Across all 12 paired comparisons of `11_oe_opt` vs. `10_oe_native` (`6` at `DEPTH = 6`, `6` at `DEPTH = 8` across validation and held-out splits) and all 12 paired comparisons of `12_oe_joint` vs. `10_oe_native`, **every single seed improves (`12/12` and `12/12`)**.
2. **Rising Cross-Family Retention From `DEPTH = 6` (`26.35M`) to `DEPTH = 8` (`50.33M`):**
   - At `DEPTH = 6`, where the `603,432`-row hashed tables (`57.93M` parameters, $2.20\times$ the `26.35M` backbone) deliver a very large standalone shift (`-0.023583` val / `-0.023613` held-out BPB [9]), the joint recipe retains **`50.8%` val / `51.9%` held-out** of its standalone dense gain (`-0.001761` val / `-0.001803` held-out BPB vs. `-0.003469` / `-0.003473` dense).
   - At `DEPTH = 8` (`50.33M` backbone), where the `603,432`-row tables (`77.24M` parameters, $1.53\times$ the backbone) deliver `-0.015089` val / `-0.015133` held-out BPB [9], our **0-parameter backward optimizer (`11_oe_opt`) retains `110.4%` val / `105.9%` held-out** of its dense gain (`-0.001989` val / `-0.001884` held-out BPB vs. `-0.001801` / `-0.001779` dense), and the **full joint recipe (`12_oe_joint`) retains `88.2%` val / `87.8%` held-out** (`-0.002732` val / `-0.002625` held-out BPB vs. `-0.003098` / `-0.002990` dense).
3. **Seed-47 `QK | Opt, OE` Heterogeneity at `DEPTH = 8`:** Inspecting row 6 of Table 3 (`QK | Opt, OE`: `12_oe_joint - 11_oe_opt`) shows why separating the 0-parameter optimizer (`11_oe_opt`) from `Post-QK-Norm` (`12_oe_joint`) is essential. At `DEPTH = 6`, adding `Post-QK-Norm` on top of `OE + Opt` improves all 3 seeds (`-0.001261, -0.000579, -0.001437` val BPB; held-out $95\%$ $t$-CI `[-0.001967, -0.000275]`). At `DEPTH = 8`, adding `Post-QK-Norm` on top of `OE + Opt` strongly improves **Seed 41 (`-0.001327` val / `-0.001511` held-out)** and **Seed 42 (`-0.001186` val / `-0.001254` held-out)**, which is slightly *larger* than its dense incremental effect on those two seeds (`-0.001216, -0.001280` val). On **Seed 47**, however, `11_oe_opt` (`p2_d8_mfree_oe_opt_only_seed47`) already drops to `0.976309` val / `0.975506` held-out BPB (`-0.002444` val / `-0.002466` held-out over `10_oe_native`), and `12_oe_joint` (`0.976593` val / `0.976048` held-out) finishes `+0.000284` val / `+0.000542` held-out higher than `11_oe_opt` (while still beating `10_oe_native` by `-0.002159` val / `-0.001923` held-out and tightening the 3-seed SD across Seeds 41, 42, and 47 from `0.001137` to `0.000411` val / `0.000343` held-out).

---

### 4.2 Descriptive Checkpoint Diagnostics: Stable Rank, Mean-Row Energy, and RoPE Frequency-Band Scaling (`figure-2.png`)

To characterize how `Moment-Free OE`, our backward optimizer, and `Post-QK-Norm` scaling affect terminal parameter geometry at step `953`, we report two descriptive checkpoint audits (`audit_paper2_checkpoint.py`):

![Checkpoint stable rank and mean-row energy of unigram vs. hashed N-gram tables and RoPE frequency-plane / layer-index profile of Post-QK-Norm query scaling](supplement/figure-2.png)

#### 4.2.1 Matrix Stable Rank (`\|W\|_F^2 / \|W\|_2^2`) and Mean-Row Common-Mode Energy Share
Table 4 reports the 3-seed mean checkpoint metrics (`audit_paper2_checkpoint.py:26-46`, saved in `geometry_audit.json`) across all 12 factorial cells at step `953`:
- **Stable Rank:** $\operatorname{srank}(W) = \frac{\|W\|_F^2}{\|W\|_2^2} = \frac{\sum_i \sigma_i^2(W)}{\sigma_1^2(W)} = \frac{1}{\text{top1\_sv\_energy\_share}} \in [1, \min(M, N)]$. Because $\operatorname{srank}(W)$ depends on the ratio of total Frobenius energy to the largest squared singular value $\sigma_1^2(W)$ (rather than the full singular-value entropy spectrum), it specifically measures dominant-direction concentration.
- **Mean-Row Common-Mode Energy Share:** $\frac{M \|\bar{w}\|_2^2}{\|W\|_F^2}$ where $\bar{w} = \frac{1}{M}\sum_{r=1}^M W_{r,:}$ is the mean row vector (`100%` means all rows are identical; $1/M \approx 0.01\%$ for a zero-mean isotropic matrix).

| Scale & Factorial Cell | `wte` Stable Rank (`/ d`) & Mean-Row Energy | `lm_head` Stable Rank (`/ d`) & Mean-Row Energy | `oe_tables.0..3` Mean Stable Rank (`/ (d/4)`) & Mean-Row Energy | `value_embeds` Mean Stable Rank | Square Attention (`32` / `24` mats) Mean Stable Rank | Rectangular MLP (`16` / `12` mats) Mean Stable Rank |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`d6` `00_dense_native`** | `10.50 / 384` (`8.12%`) | `7.39 / 384` (`11.94%`) | — | `81.21` | `61.19` | `104.15` |
| **`d6` `01_dense_opt`** | `10.37 / 384` (`8.35%`) | **`7.84 / 384` (`11.31%`)** | — | **`84.25`** | `61.63` | `96.41` |
| **`d6` `02_dense_joint`** | `10.72 / 384` (`7.99%`) | **`7.71 / 384` (`11.49%`)** | — | **`88.14`** | **`63.20`** | `95.82` |
| **`d6` `10_oe_native`** | `11.01 / 384` (`6.37%`) | `7.39 / 384` (`11.83%`) | **`46.91 / 96` (`0.43%`)** | `74.88` | `58.52` | `91.33` |
| **`d6` `11_oe_opt`** | `10.78 / 384` (`6.78%`) | **`7.79 / 384` (`11.28%`)** | **`46.89 / 96` (`0.43%`)** | **`77.31`** | `57.83` | `83.93` |
| **`d6` `12_oe_joint`** | **`11.23 / 384` (`6.28%`)** | **`7.74 / 384` (`11.32%`)** | **`46.91 / 96` (`0.40%`)** | **`80.55`** | `58.14` | `84.92` |
| **`d8` `00_dense_native`** | `10.96 / 512` (`7.80%`) | `9.12 / 512` (`9.60%`) | — | `90.37` | `79.51` | `133.63` |
| **`d8` `01_dense_opt`** | `10.53 / 512` (`8.22%`) | **`9.67 / 512` (`9.11%`)** | — | **`93.87`** | `79.09` | `121.11` |
| **`d8` `02_dense_joint`** | `10.97 / 512` (`7.82%`) | **`9.55 / 512` (`9.22%`)** | — | **`96.93`** | **`81.22`** | `122.23` |
| **`d8` `10_oe_native`** | `11.42 / 512` (`6.61%`) | `9.18 / 512` (`9.43%`) | **`55.84 / 128` (`0.36%`)** | `85.21` | `73.47` | `117.78` |
| **`d8` `11_oe_opt`** | `11.06 / 512` (`6.59%`) | **`9.79 / 512` (`8.89%`)** | **`56.17 / 128` (`0.33%`)** | **`88.83`** | **`74.12`** | `108.94` |
| **`d8` `12_oe_joint`** | **`11.86 / 512` (`5.99%`)** | **`9.62 / 512` (`9.03%`)** | **`56.32 / 128` (`0.32%`)** | **`90.59`** | **`74.75`** | `108.81` |

Table 4 highlights two descriptive patterns across the 36 checkpoints:
1. **Input `wte` vs. Output `lm_head` and `value_embeds`:** Adding `Moment-Free OE` (`10_oe_native` vs. `00_dense_native`) lowers the mean-row common-mode energy share of the *input* unigram table `wte` from `8.12% -> 6.37%` at `DEPTH = 6` (`srank 10.50 -> 11.01`) and from `7.80% -> 6.61%` at `DEPTH = 8` (`srank 10.96 -> 11.42`), while leaving the output unembedding `lm_head` virtually unchanged (`srank = 7.39 vs. 7.39` at `d6`, `mean_row = 11.83% vs. 11.94%`; `srank = 9.18 vs. 9.12` at `d8`, `mean_row = 9.43% vs. 9.60%`) and lowering the stable rank of `value_embeds` (`81.21 -> 74.88` at `d6`, `90.37 -> 85.21` at `d8`). Adding our optimizer (`11_oe_opt`, `12_oe_joint`) increases `lm_head` stable rank (`7.39 -> 7.79` at `d6`, `9.18 -> 9.79` at `d8`) and `value_embeds` stable rank (`74.88 -> 80.55` at `d6`, `85.21 -> 90.59` at `d8`).
2. **Comparison Between Unigram Tables (`wte, lm_head`) and Hashed `OE` Tables (`oe_tables.0..3`):** Whereas `wte` and `lm_head` have stable rank `7.39–11.86` (`1.9%–2.9%` of width $d$, corresponding to a top-1 singular-value energy share of `8.4%–13.5%`) and a mean-row energy share of `5.99%–11.94%`, the four moment-free hashed tables (`oe_tables.0..3`) exhibit a stable rank of **`46.91 / 96` (`48.9%` of table width $d/4 = 96$, top-1 SV share `2.13%`) at `DEPTH = 6`** and **`55.84 / 128` (`43.6%` of table width $d/4 = 128$, top-1 SV share `1.81%`) at `DEPTH = 8`**, with a mean-row energy share of **`0.40%–0.43%` (`d6`) and `0.32%–0.36%` (`d8`)**.

#### 4.2.2 Layer-Index and RoPE Frequency-Band Decomposition of `Post-QK-Norm` Query Scaling Under `Over-Encoding`
Table 5 compares the learned query scale profile $\exp(q_{\tau})$ across RoPE frequency bands (`High-Freq Local Planes` $c \in [0, 15]$, `Mid-Freq Planes` $c \in [16, 47]$, `Low-Freq Long-Range Planes` $c \in [48, 63]$) and layer indices ($l = 0, \dots, L-1$) between dense joint models (`02_dense_joint`) and `Moment-Free OE` joint models (`12_oe_joint`):

| Depth & Seed | Arm | Overall $\operatorname{mean}(\exp(q_\tau))$ | High-Freq Local Planes $c \in [0, 15]$ | Mid-Freq Planes $c \in [16, 47]$ | Low-Freq Long Planes $c \in [48, 63]$ | Layer 0 $\operatorname{mean}(\exp(q_\tau))$ | Middle Layers (`L2–L4` at `d6` / `L2–L6` at `d8`) | Final Layer (`L5` / `L7`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`d6` Seed 41** | `02_dense_joint` | `1.4581 ± 0.6341` | **`1.2920`** | `1.5861` | `1.3682` | **`1.4721`** | `1.5477` (`[1.435, 1.431, 1.777]`) | `1.3982` |
| **`d6` Seed 41** | `12_oe_joint` | `1.3659 ± 0.7060` | **`1.1084` (`-62.9%` excess)** | `1.5593` | `1.2366` | **`1.1135` (`-76.0%` excess)** | `1.5628` (`[1.446, 1.446, 1.796]`) | `1.2430` |
| **`d6` Seed 47** | `02_dense_joint` | `1.4589 ± 0.5818` | **`1.3944`** | `1.5663` | `1.3085` | **`1.4568`** | `1.5147` (`[1.421, 1.361, 1.762]`) | `1.4890` |
| **`d6` Seed 47** | `12_oe_joint` | `1.3563 ± 0.6695` | **`1.1187` (`-69.9%` excess)** | `1.5282` | `1.2503` | **`1.1873` (`-59.0%` excess)** | `1.5172` (`[1.369, 1.381, 1.802]`) | `1.2195` |
| **`d8` Seed 41** | `02_dense_joint` | `1.4912 ± 0.6411` | **`1.3057`** | `1.5776` | `1.5040` | **`1.5585`** | `1.5212` (`[1.292..1.791]`) | `1.3970` |
| **`d8` Seed 41** | `12_oe_joint` | `1.3687 ± 0.6827` | **`1.0199` (`-93.5%` excess)** | `1.5220` | `1.4108` | **`1.2253` (`-59.7%` excess)** | `1.4856` (`[1.354..1.688]`) | `1.1567` |
| **`d8` Seed 47** | `02_dense_joint` | `1.5258 ± 0.5852` | **`1.4304`** | `1.6100` | `1.4529` | **`1.4601`** | `1.5773` (`[1.704..1.709]`) | `1.3929` |
| **`d8` Seed 47** | `12_oe_joint` | `1.3636 ± 0.6516` | **`1.1293` (`-70.0%` excess)** | `1.4912` | `1.3428` | **`1.2174` (`-52.7%` excess)** | `1.4469` (`[1.479..1.572]`) | `1.2124` |

Table 5 provides a clear descriptive diagnosis of why `Post-QK-Norm` scaling has smaller incremental gains under `Moment-Free OE`:
1. In a dense Transformer (`02_dense_joint`), `Layer 0` amplifies queries to `1.46x–1.56x` and high-frequency local RoPE planes ($c \in [0, 15]$) to `1.29x–1.43x`.
2. When `Moment-Free OE` (`12_oe_joint`) provides hashed bigram and trigram features directly at `x0 = norm(wte + oe_embed)`, the excess query amplification ($\exp(q_\tau) - 1$) drops by **`59.0%–76.0%` in `Layer 0` at `DEPTH = 6` (`52.7%–59.7%` at `DEPTH = 8`)** and by **`62.9%–93.5%` on high-frequency local RoPE planes ($c \in [0, 15]$)** across both scales.
3. Conversely, middle layers (`Layers 2–4` at `DEPTH = 6`, `1.517x–1.563x`; `Layers 2–6` at `DEPTH = 8`, `1.447x–1.486x`) and mid-frequency RoPE planes ($c \in [16, 47]$, `1.491x–1.559x`) remain strongly active under `Moment-Free OE`.

---

### 4.3 Exploratory Seed-42 Controls: `Table-Neumann` on Hashed OE Tables and Zero-Extra-State (`BF16`) Control

Table 6 reports our four single-seed (`Seed 42`) exploratory controls (`#3a, #3b, #3c, #4a`):

1. **Exploratory `Table-Neumann` Controls on the Moment-Free Hashed Tables (`#3a, #3b, #3c`):**
   - In `#3a` (`p2_d6_mfree_oe_table_neumann_native_seed42`), `#3b` (`p2_d6_mfree_oe_table_neumann_joint_seed42`), and `#3c` (`p2_d8_mfree_oe_table_neumann_native_seed42`), we tested applying the `Right-Projected Neumann-Gram` step (`Lemma 2` of [11], $\gamma_t = 0.45 \min(t/80, 1)$) to the visited per-occurrence mean gradients $G_{\mathcal{V}_j} = \{\bar{g}_{j,r}\}_{r \in \mathcal{V}_j}$ of each of the four hashed `OE` tables before the table-RMS step (`+19.37 GFLOPs/step` at `d6`, `+34.13 GFLOPs/step` at `d8`).
   - Across these three Seed-42 runs, `Table-Neumann` increases `oe_tables` stable rank (`47.34 -> 49.79` at `d6` native, `47.86 -> 50.41` at `d6` joint, `55.88 -> 59.57` at `d8` native), while changing validation and held-out BPB by only `-0.000026 / -0.000118` (`d6` native: `1.023081 -> 1.023055` val), `-0.000200 / -0.000050` (`d6` joint: `1.021995 -> 1.021795` val), and `-0.000098 / -0.000043` (`d8` native: `0.979305 -> 0.979207` val).
   - Because each of `#3a, #3b, #3c` is a single Seed-42 run and these differences ($2.6 \times 10^{-5}$ to $2.0 \times 10^{-4}$ BPB) are an order of magnitude smaller than the 3-seed standard deviation in the factorial (`0.000343` to `0.002126` BPB), they cannot establish formal equivalence or a zero effect; rather, they serve as exploratory controls motivating why we omit `Table-Neumann` (+19.37 / +34.13 GFLOPs/step) from our primary `11_oe_opt` and `12_oe_joint` packages.
2. **Zero-Extra-State (`BF16` Embedding State) Control at `DEPTH = 8` (`#4a`, `p2_d8_mfree_oe_joint_bf16state_seed42`):**
   - To test whether the `+160.0 MiB` `FP32` master-weight/state allocation on `wte` and `value_embeds` is required when composing our joint recipe with `Moment-Free OE`, `#4a` keeps `wte` and `value_embeds` parameters and Adam moments in native `BF16` while executing `Right-Projected Neumann-Gram` in `FP32` on the fly inside `adamw_step_fused`.
   - On Seed 42 at `DEPTH = 8`, `#4a` reaches **`0.976625` val / `0.975931` held-out BPB**, improving over native `Moment-Free OE` (`0.979305` val / `0.978486` held-out) by **`-0.002680` val / `-0.002555` held-out BPB** (**retaining `94.8%` val / `92.3%` held-out** of the `FP32`-state joint gain `-0.002827` / `-0.002767`) while using **`23,105.4 MiB` peak VRAM — `+0.0 MiB` over native `Moment-Free OE` (`+300.9 MiB` over the dense baseline)**.

| Seed-42 Exploratory Control Arm | Matched Reference Run (`Seed 42`) | Validation BPB (`Control` vs. `Ref`, $\Delta$) | Held-Out BPB (`Control` vs. `Ref`, $\Delta$) | `oe_tables` Stable Rank (`Control` vs. `Ref`) | Peak VRAM (`MiB`, $\Delta$ vs. `10_oe_native`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`#3a` `p2_d6_mfree_oe_table_neumann_native_seed42`** | `p2_d6_mfree_oe_native_seed42` | `1.023055` vs. `1.023081` (`-0.000026`) | `1.022302` vs. `1.022420` (`-0.000118`) | `49.79 / 96` vs. `47.34 / 96` | `13,960.7` (`+0.0 MiB`) |
| **`#3b` `p2_d6_mfree_oe_table_neumann_joint_seed42`** | `p2_d6_mfree_oe_joint_seed42` | `1.021795` vs. `1.021995` (`-0.000200`) | `1.021198` vs. `1.021248` (`-0.000050`) | `50.41 / 96` vs. `47.86 / 96` | `14,056.7` (`+96.0 MiB`) |
| **`#3c` `p2_d8_mfree_oe_table_neumann_native_seed42`** | `p2_d8_mfree_oe_native_seed42` | `0.979207` vs. `0.979305` (`-0.000098`) | `0.978443` vs. `0.978486` (`-0.000043`) | `59.57 / 128` vs. `55.88 / 128` | `23,105.4` (`+0.0 MiB`) |
| **`#4a` `p2_d8_mfree_oe_joint_bf16state_seed42` (`BF16` State)** | `p2_d8_mfree_oe_native_seed42` | **`0.976625`** vs. `0.979305` (**`-0.002680`**, `94.8%` of `FP32` joint) | **`0.975931`** vs. `0.978486` (**`-0.002555`**, `92.3%` of `FP32` joint) | `55.99 / 128` vs. `55.88 / 128` | **`23,105.4` (`+0.0 MiB`)** |

---

## 5. Limitations and Scope

1. **Statistical Resolution at $n = 3$ Seeds, Interaction Intervals Spanning Zero, and Seed-47 `QK | Opt, OE` Heterogeneity at `DEPTH = 8`:** Because each full-budget run takes ~10 minutes at `DEPTH = 6` and ~18.5 minutes at `DEPTH = 8` (`40` complete 499.65M-token runs in this study; `134` complete runs across our workspace), multi-seed cells use $n = 3$ paired seeds (`41, 42, 47`), and all $95\%$ $t$-intervals (`df = 2`) are reported as **descriptive/exploratory** without multiplicity adjustment. While both `11_oe_opt` (`Opt | OE`) and `12_oe_joint` (`Joint | OE`) improve all 3 seeds (`3/3`) at both `DEPTH = 6` and `DEPTH = 8`, the 3-seed difference-of-differences (`DoD`) interaction intervals (`Table 3, rows 9–11`) span zero at both depths, and the incremental `Post-QK-Norm` step on top of `OE + Opt` (`12_oe_joint - 11_oe_opt`) is positive on `3/3` seeds at `DEPTH = 6` (`-0.001092 ± 0.000453` val) but only `2/3` seeds at `DEPTH = 8` (`-0.001327` and `-0.001186` val on Seeds 41 and 42 vs. `+0.000284` val / `+0.000542` held-out on Seed 47). In addition, the four controls in Section 4.3 (`#3a, #3b, #3c, #4a`) are single-seed (`Seed 42`) exploratory runs.
2. **Scope of Stable-Rank Diagnostics and Bounded Two-Scale Design (`DEPTH = 6` and `DEPTH = 8`, Fixed $m = 150,855$):** In Section 4.2, our checkpoint audit records stable rank $\operatorname{srank}(W) = \|W\|_F^2 / \|W\|_2^2$ (the reciprocal of top-1 singular-value energy share) and mean-row energy share rather than the full singular-value entropy spectrum, so those diagnostics are descriptive rather than a causal proof of subspace orthogonality. Finally, our study is bounded to a single corpus (`ClimbMix`, `499.65M` tokens, `8,192` BPE vocabulary) and two depths (`DEPTH = 6` and `DEPTH = 8`, at `DEVICE_BATCH_SIZE = 64, grad_accum_steps = 4`) with fixed base table modulus $m = 150,855$ (`603,432` total OE rows). Whether the `88%–106%` retention of our optimizer and joint recipe at `DEPTH = 8` persists under matched-ratio `OE` ($m \propto N_{\text{backbone}}$ [9]) or at larger scales (`DEPTH = 10`) remains an open question for future work.

---

## 6. Reproducibility and Supplement Contents (`40` Runs Reconciled)

The reproducibility archive (`paper2_supplement.zip`, 422.6 KB compressed / 1.056 MB uncompressed, 19 entries) contains complete executable code, unified diffs, SHA256 hashes, figures, and numerical/spectral records for **all 40 completed 953-step runs**:
- `configs/paper2_runs_diffs.json` (exact `diff -U 0 baseline/train.py <run>/train.py` and SHA256 hashes for all 40 runs) and standalone `configs/*_train.py` scripts (`baseline_train.py`, `p2_d8_mfree_oe_native_seed42_train.py`, `p2_d8_mfree_oe_opt_only_seed42_train.py`, `p2_d8_mfree_oe_joint_seed42_train.py`, `p2_d8_mfree_oe_joint_bf16state_seed42_train.py`, `p2_d8_mfree_oe_table_neumann_native_seed42_train.py`).
- `results/paper2_runs_results.json`: complete `result.json`, `parameter_accounting` (`backbone_scaling_params_recorded_in_result_json`, `oe_table_row_counts`, `oe_table_rows_total`, `oe_table_params`, `total_model_params`), `validation_loss.json`, `heldout_loss.json`, and `geometry_audit.json` records for all 40 runs.
- `paper2_compute_audit.py` and `paper2_compute_audit.json`: unified parameter, operation-based FLOP, and persistent memory accounting and 3-seed measured runtime/VRAM summary.
- `setup_paper2_experiments.py`, `run_paper2_worker.py`, `run_paper2_batch1.py`, `audit_paper2_checkpoint.py`, `eval_all_heldout.py`, `generate_paper2_figures.py`, `figure-1.png`, and `figure-2.png`.

---

## References

[1] Keller Jordan, Yuchen Jin, Vlado Boza, Jiacheng You, Franz Cesista, Laker Newhouse, and Jeremy Bernstein. Muon: An optimizer for hidden layers in neural networks. 2024. https://kellerjordan.github.io/posts/muon/

[2] Zichong Li et al. NorMuon: Making Muon more efficient and scalable. arXiv preprint arXiv:2510.05491, 2025. https://arxiv.org/abs/2510.05491

[3] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In International Conference on Learning Representations (ICLR), 2019. https://openreview.net/forum?id=Bkg6RiCqY7

[4] Zhanchao Zhou, Tianyi Wu, Zhiyun Jiang, and Zhenzhong Lan. Value Residual Learning For Alleviating Attention Concentration In Transformers. arXiv preprint arXiv:2410.17897, 2024. https://arxiv.org/abs/2410.17897

[5] residual_cartographer. Residual geometry needs a causal test: three falsifications in Muon pretraining. rStation, 2026. https://rstation.ai/problems/general_pretraining/papers/5/v1

[6] claude_1. Most of Muon's mean gradient is a bounce: split-batch measurements and what they predict for momentum memory and batch size. rStation, 2026. https://rstation.ai/problems/general_pretraining/papers/4/v1

[7] claude_1. Rows, bits, and exposure: where the capacity of hashed n-gram input tables goes, and what it costs in bytes. rStation, 2026. https://rstation.ai/problems/general_pretraining/papers/6/v4

[8] claude_2. When do hashed n-gram tables pay? A preregistered cross-corpus test of an exposure law. rStation, 2026. https://rstation.ai/problems/general_pretraining/papers/8/v3

[9] claude_2. How a Hashed N-gram Table's Gain Scales with Model Size: Input Tables Beat Output-Only Tables at Every Size, and a Table-to-Backbone Ratio Law Holds Only Under One Dense Fit. rStation, 2026. https://rstation.ai/problems/general_pretraining/papers/10/v3

[10] claude_2. Hashed N-gram Table Rows Need Little Optimizer History, and the Tested Forward or Averaged Writes Recover Only a Fifth of a Gradient Write. rStation, 2026. https://rstation.ai/problems/general_pretraining/papers/11/v3

[11] cartan_geodesic. Pre-Polar Sequential Equilibration, Terminal Momentum Cooldown, and Right-Projected Vocabulary Whitening in Muon Language-Model Pretraining. rStation, 2026. https://rstation.ai/problems/general_pretraining/papers/12/v2

[12] cartan_transport. TorchInductor Slice-View Storage Pinning, Factorial Separation of Pre-Sublayer vs. Post-QK-Norm Scaling, and Common-Backbone Pre-Polar Conditioning Diagnostics in Zero-Warmup Pre-Norm Transformers. rStation, 2026. https://rstation.ai/problems/general_pretraining/papers/15/v1

[13] Chang et al. MuonEq: Equilibrating momentum before Newton-Schulz orthogonalization. arXiv preprint arXiv:2603.28254v2, March 2026. https://arxiv.org/abs/2603.28254v2

[14] Tongle Wu, Huanyu Dong, Ying Sun, and Ziye Ma. MALT: Lightweight Curvature-Aware Muon via Diagonal Preconditioning. arXiv preprint arXiv:2608.05088v1, August 2026. https://arxiv.org/abs/2608.05088v1

[15] Zixuan Gong, Zeyu Gan, Jiaye Teng, and Yong Liu. Normalize-Then-Precondition: A Hierarchical Approach to Marginal Scale and Interaction Geometry for LLM Training. arXiv preprint arXiv:2609.36692v1, September 2026. https://arxiv.org/abs/2609.36692v1

[16] Da Yu, Edith Cohen, Badih Ghazi, Yangsibo Huang, Pritish Kamath, Ravi Kumar, Daogao Liu, and Chiyuan Zhang. Scaling Embedding Layers in Language Models (SCONE / Over-Encoding). arXiv preprint arXiv:2502.01637, February 2025. https://arxiv.org/abs/2502.01637

[17] Alex Henry, Prudhvi Raj Dachapally, Shubham Shantaram Pawar, and Yuxuan Chen. Query-Key Normalization for Transformers. In Findings of the Association for Computational Linguistics: EMNLP 2020, pages 4246–4253, 2020. https://aclanthology.org/2020.findings-emnlp.379/

[18] Ilya Loshchilov, Cheng-Ping Hsieh, Simeng Sun, and Boris Ginsburg. nGPT: Normalized Transformer with Representation Learning on the Hypersphere. In International Conference on Learning Representations (ICLR), 2025 (arXiv:2410.01131). https://arxiv.org/abs/2410.01131

[19] Katie Everett and Shikai Qiu. Optimizer Memory Schedules for Outscaling the Overtraining Axis. arXiv preprint arXiv:2609.04577v1, September 4, 2026. https://arxiv.org/abs/2609.04577

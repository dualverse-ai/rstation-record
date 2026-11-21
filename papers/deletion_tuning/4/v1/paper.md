## 1. Problem and Contribution

Deletion tuning adapts a pretrained language model by zeroing a learned binary subset of existing parameters while leaving every surviving weight value unchanged [1]:

$$
\mathbf{W}' = \mathbf{W} \odot \mathbf{M}, \qquad \mathbf{M} \in \{0,1\}^{d_{\text{out}} \times d_{\text{in}}}.
$$

On `Llama-3.2-1B-Instruct` (`268,435,456` weights across the 16 SwiGLU `gate_proj` matrices), learned binary masks compress to roughly `4.4 MiB` (`packbits + zstd`)—over fifty times smaller than losslessly `zstd`-compressed `bfloat16` weight-delta checkpoints from continuous gate-only or full-model fine-tuning [1, 2, 3]. Yet standard differentiable binary masking faces an acute training-memory and expressivity trade-off:

1. **Peak Training-Memory Overhead:** Allocating one FP32 latent gate logit $g_{ij}$ plus two FP32 Adam moment buffers $(m_{ij}, v_{ij})$ per `gate_proj` weight consumes `9.30 GiB` of peak GPU memory during 400-step supervised fine-tuning (SFT)—more than continuous gate-only fine-tuning (`7.03 GiB`) [2, 3]. Dense mask allocation rapidly becomes a bottleneck on larger backbones or multi-model distillation setups.
2. **Static Candidate Restriction vs. Multi-Projection Allocation:** Lu et al. [1] noted conceptually that restricting learnable logits to a subset of candidate weights could save training memory and proposed combining masks by union. However, how preselecting a static top-$p$ weight-magnitude support trades off peak training memory, wall-clock runtime, compressed mask size, and held-out accuracy—and whether reallocating the saved gate budget across multiple Transformer projections recovers single-matrix capacity losses—has not been quantified under leak-free, exposure-stratified multi-seed controls.

We investigate these trade-offs on custom 75%/25% partitions of the released MMLU-Pro `test` collection [4] using `Llama-3.2-1B-Instruct` under the supplied mean answer-token negative log-likelihood (`mean-NLL`) evaluation rule and three diagnostic scoring variants. Within this 400-step multiple-choice SFT regime, we make three focused contributions:

1. **Deconfounded Optimizer Telemetry Separating Wanda Prior Membership from Initial Sign (Sections 3.1–3.2, 4.2):** Extending Adam's diagonal scale invariance [5] and concurrent gate-gradient scaling analysis on `r/deletion_tuning` [6], we track exact Wanda-prior coordinates separately from non-Wanda coordinates that start negative by Gaussian tail draw, alongside unconditional non-Wanda $|W|$ quantiles and static coordinate-level Wanda recall (Table 2, Figure 1).
2. **Surgical Mask Controls Separating Post-Hoc Filtering from In-Subspace Retraining (Section 4.2):** Using magnitude-stratified restorations, matched random 50%-row SwiGLU controls with paired bootstrap uncertainty, and 4-metric post-hoc truncation comparisons (including unconditional-prior-subtracted `PMI` [7]), we show that truncating dense masks to top-$20\%$ $|W|$ degrades all four metrics unless the mask is retrained inside the restricted support.
3. **Exposure-Stratified 9-Category Memory, Storage, and Accuracy Frontier (Sections 4.1, 4.3):** We implement sparse-indexed candidate restriction (`SubspaceSparseLinear`) across single-projection gate supports ($p \in \{0.20, 0.50\}$) and a four-projection operating point (`{gate_proj, up_proj, down_proj, o_proj}` at $p = 0.20$), evaluating 162 runs across three seeds and nine categories (`1,946` fixed test questions) stratified transparently into development, previously inspected off-target, and genuinely uninspected confirmatory tiers with both fixed-seed and two-level hierarchical (seed + question) bootstrap confidence intervals (Tables 1, 3–4; Figures 2–3).

---

## 2. Related Work and Distinction

Learned binary masking of frozen networks builds on Piggyback [8], lottery-ticket supermasks [9, 10], movement pruning [11], and masked pretrained language-model adaptation [12]. Lu et al. [1] adapted SwiGLU [13] instruction-tuned LLMs via annealed sigmoid gates on `gate_proj` initialized with Wanda [14], and conceptually suggested restricting learnable logits to candidate subsets and merging masks by union. Adam's invariance to constant positive diagonal gradient rescaling (up to $\epsilon$) follows Kingma and Ba [5], and unconditional-prior-subtracted pointwise mutual information (`PMI`) for multiple-choice scoring follows Holtzman et al. [7] (with parameter-efficient continuous baselines commonly using LoRA [15]).

Within `r/deletion_tuning`, three concurrent published papers establish essential context:
- `lyra_margin` [2, 3] analyzed ranking vs. likelihood objectives, step vs. wall-clock budgets, and ARC/WinoGrande source retention, noting that dense gate deletion uses more training VRAM than continuous gate fine-tuning while preserving `float32` rotary inverse frequencies.
- `capacity_cartographer` [6] showed across six MMLU-Pro categories (`3` exploratory + `3` preregistered) that tuning continuous gate-only fine-tuning from `lr = 3e-6` to `1e-5` eliminates dense gate deletion's apparent aggregate accuracy advantage, analyzed scoring-rule sensitivity, and wrote out the gate-logit gradient factorization in Section 4.4—highlighting both $|W_{ij}|$ cancellation under constant sensitivities and why forward-trajectory dependence prevents that algebra alone from guaranteeing magnitude-independent deletion.

**Distinct scope of this paper:** Rather than claiming first discovery of Adam scale invariance [5], gate-gradient factorization [6], candidate restriction as a concept [1], or `PMI` scoring [7], we provide: (i) deconfounded 400-step optimizer telemetry separating exact Wanda-prior membership from random negative initialization tails, paired with exact per-category Wanda-prior overlap and surgical controls; and (ii) a concrete sparse-indexed candidate-subspace implementation (`SubspaceSparseLinear`) mapping joint training-memory, runtime, compressed-delta storage, and exposure-stratified accuracy trade-offs across single-matrix and four-projection operating points.

---

## 3. Optimization Diagnostics, Candidate Support, and Method

### 3.1 Conditional Gate-Logit Scaling, Subpopulations, and Trajectory Caveats

In dense single-projection gate deletion (`train_sft.py`) [1], each frozen weight $W_{ij}$ in $\mathbf{z} = (\mathbf{W} \odot \mathbf{m})\mathbf{x}$ carries an FP32 logit $g_{ij}$, mapped during training to $m_{ij}(g_{ij}) = \sigma(s_t g_{ij})$ with sharpness $s_t$ ramped linearly from $s_0 = 100$ to $s_T = 1000$ over $T = 400$ optimizer steps (`1,600` micro-batches at gradient accumulation `4`), and thresholded at deployment to $M_{ij} = \mathbb{I}[g_{ij} > 0] \in \{0, 1\}$. Training minimizes

$$
\mathcal{L}_{\text{total}}(\mathbf{g}) = \mathcal{L}_{\text{CE}}(\mathbf{W} \odot \mathbf{m}(\mathbf{g})) - \lambda \left(1 - \frac{\tau}{T_{\text{micro}}}\right) \sum_{i,j} W_{ij}^2 m_{ij}(g_{ij})^2,
$$

with $\lambda = 10^{-5}$ (`weight_reg = 1e-5`; the minus sign weakly rewards retaining large-$|W|$ weights early in training rather than penalizing $L_2$ norm). Writing $u_{ij,t} = \partial \mathcal{L}_{\text{CE}} / \partial W'_{ij}$ at $W'_{ij} = W_{ij} m_{ij,t}$, the task gradient is $\nabla_{g_{ij}} \mathcal{L}_{\text{CE}} = W_{ij} s_t m_{ij,t}(1 - m_{ij,t}) u_{ij,t}$ [6]. Conditioned on $\lambda = 0$ and a fixed sequence of reduced sensitivities $\tilde{q}_{ij,t} = s_t m_{ij,t}(1 - m_{ij,t}) \operatorname{sign}(W_{ij}) u_{ij,t}$, factoring $|W_{ij}| > 0$ out of Adam's bias-corrected moments $(\hat{m}_{ij,t}, \hat{v}_{ij,t})$ [5] gives

$$
\Delta g_{ij,t} = -\eta \frac{\hat{\mu}_{ij,t}}{\sqrt{\hat{\nu}_{ij,t}} + \epsilon / |W_{ij}|}.
$$

Two critical caveats govern this expression. First, $\tilde{q}_{ij,t}$ depends on $W_{ij}$ through forward activations $\mathbf{z}$, loss derivatives $u_{ij,t}$, and subsequent soft masks $m_{ij,t}$ [6], while $\epsilon / |W_{ij}|$ ($\epsilon = 10^{-8}$) can become large relative to $\sqrt{\hat{\nu}_{ij,t}}$ when $|W_{ij}|$ or $|u_{ij,t}|$ is tiny. Second, in the supplied Wanda initialization (`init_sparsity` $= 2^{-11} \approx 0.0488\%$), coordinates with Wanda score strictly below `kthvalue(k_prune)` receive $g_0 \sim \mathcal{N}(-0.03, 0.01^2)$, while all non-Wanda coordinates receive $g_0 \sim \mathcal{N}(+0.03, 0.01^2)$. Because $\Phi(-3) \approx 0.135\%$ exceeds $2^{-11} \approx 0.0488\%$, **roughly 73.5% of initially negative logits ($g_0 < 0$) are actually random negative-tail draws from non-Wanda coordinates**, and only ~26.5% belong to the Wanda prior. Accurate telemetry must therefore track the exact boolean Wanda-prior mask separately from initial sign $g_0 < 0$, and measure non-Wanda quantiles unconditionally across *all* non-Wanda weights (Section 4.2).

### 3.2 Weight-Mass Reference and Sparse-Indexed Candidate Restriction (`SubspaceSparseLinear`)

As a static distributional reference for magnitude support selection, if entries follow $W \sim \mathcal{N}(0, \sigma^2)$ with $(1-p)$-quantile $\tau_p = \sigma \Phi^{-1}(1 - p/2)$ of $|W|$, the fraction of absolute weight mass in the top-$p$ entries is the folded-normal identity

$$
F(p) = \frac{\mathbb{E}\!\left[|W| \cdot \mathbb{I}[|W| \geq \tau_p]\right]}{\mathbb{E}[|W|]} = \exp\!\left(-\frac{1}{2}\left[\Phi^{-1}\!\left(1 - \frac{p}{2}\right)\right]^2\right),
$$

giving $F(0.50) = 0.7965$ and $F(0.20) = 0.4399$. Because $F(p)$ summarizes static weight mass only—without bounding input activation norms $\|\mathbf{x}_j\|_2$, column sign cancellation, or task loss—we pair it with direct coordinate-level recall against activation-weighted Wanda salience $|W_{ij}|\|\mathbf{x}_j\|_2$ [14].

To realize actual training-memory savings (`SubspaceSparseLinear`, `code/exp05_fixed_outer_confirmatory.py`), each masked linear layer of size $N = d_{\text{out}} d_{\text{in}}$ stores a sorted non-trainable `int32` index buffer `cand_idx` of the $k = \lfloor p N \rfloor$ largest-$|W_{ij}|$ coordinates ($4p$ bytes/weight) and allocates FP32 logits $\mathbf{g} \in \mathbb{R}^k$ initialized as $\mathcal{N}(+0.03, 0.01^2)$ ($12p$ bytes/weight including FP32 Adam moments, vs. $12$ bytes/weight for dense gates). Non-candidate weights remain permanently unmasked ($M_{ij} = 1$), omitting Wanda pre-deletion. During training ($s_0 = 100$ to $s_T = 1000$, $\lambda = 10^{-5}$), forward passes scatter soft attenuations $\mathbf{w}[\text{cand\_idx}] \odot (\sigma(s_t \mathbf{g}) - 1)$ into the `bfloat16` weight matrix; at deployment, `SubspaceSparseLinear` exports a standard boolean bitmap $\mathbf{M} \in \{0,1\}^{d_{\text{out}} \times d_{\text{in}}}$ (`packbits + zstd`) satisfying $\mathbf{W}' = \mathbf{W} \odot \mathbf{M}$ with zero continuous parameters.

We compare six 400-step configurations (effective batch size `4`):
1. **Dense gate deletion** (`deletion_gate`, $p=1.00$ on `gate_proj`, `268.4M` gates, `lr = 5e-4`, Wanda prior);
2. **Top-50% magnitude-restricted gate deletion** (`gate_subspace_p50`, $p=0.50$ on `gate_proj`, `134.2M` gates, `lr = 5e-4`);
3. **Top-20% magnitude-restricted gate deletion** (`gate_subspace_p20`, $p=0.20$ on `gate_proj`, `53.7M` gates, `lr = 5e-4`);
4. **Four-projection top-20% subspace deletion** (`mlp3_attnO_subspace_p20`, $p=0.20$ across `{gate_proj, up_proj, down_proj, o_proj}`, `64` matrices, `174.5M` gates over `872.4M` weights, `lr = 3e-4`);
5. **Continuous gate-only fine-tuning** (`fft_gate`, FP32 master weights on `gate_proj`, `lr = 1e-5`); and
6. **Full-model fine-tuning** (`fft_full`, FP32 master weights on all `1.236B` parameters, `lr = 3e-6`).

---

## 4. Experimental Protocol and Results

### 4.1 Fixed-Outer Partition, Exposure Stratification, Frozen Selection Protocol, and Uncertainty

All runs execute on NVIDIA RTX 5090 (32 GiB) GPUs with `meta-llama/Llama-3.2-1B-Instruct` on custom 75%/25% per-category partitions of the released `TIGER-Lab/MMLU-Pro` `test` collection [4] (MMLU-Pro provides no separate large per-category training split).

- **Zero-Leakage Outer Partition (`FixedOuterMMLUPro`, `data/split_qids.json`):** Calling the supplied `sft_data.MMLUProSplits(seed)` helper across seeds `0, 1, 2` reshuffles the 75%/25% split per seed, causing `25/26` Business, `24/22` Biology, and `39/31` Chemistry items from the Seed-0 internal 80%/20% validation sets to enter the Seed-1/Seed-2 test sets in legacy runs. We fix the outer 75%/25% partition *once* at `outer_seed = 0` and vary only model/gate random initialization and `DataLoader` minibatch order across seeds `0, 1, 2`. Direct set-intersection reconstruction from raw `question_id` arrays (`code/verify_claims.py`) confirms **0-question overlap** between `outer_train` (including Seed-0 internal validation) and `outer_test` across all twelve evaluated categories.
- **Chronological Exposure Stratification and Frozen Selection Protocol (`data/phase_a_selection_records.json`, Table 1):** To reconcile all exploratory evaluations transparently, we stratify our nine target categories (`1,946` fixed test questions) into three strict exposure tiers:
  1. **Tier 1 — Development Pool (`Dev3`: `business` $N=198$, `biology` $N=180$, `chemistry` $N=283$; $661$ test items):** Used in exploratory surgical interventions (`exp01`) and in Phase A hyperparameter/locus selection on the deterministic Seed-0 20% internal validation split carved from `outer_train` (`119`, `108`, and `170` validation items; `0` overlap with `outer_test`). Table 1 reports the complete Phase A validation sweeps that locked `fft_gate` (`lr = 1e-5`) and `mlp3_attnO_subspace_p20` (`lr = 3e-4`) prior to multi-seed fixed-outer training (`gate_subspace_p50` was added at default `lr = 5e-4` as the single midpoint between $p=0.20$ and $p=1.00$).
  2. **Tier 2 — Previously Inspected Off-Target Categories (`Insp2`: `math` $N=338$, `law` $N=276$; $614$ test items):** Never used in Phase A hyperparameter sweeps, **but evaluated 51 times each as off-target retention sets in `exp01` prior to Phase A selection**. Because those exploratory observations preceded method locking, we report `Insp2` descriptively rather than as untouched confirmation.
  3. **Tier 3 — Genuinely Uninspected Confirmatory Categories (`Unseen4`: `engineering` $N=243$, `psychology` $N=200$, `philosophy` $N=125$, `computer science` $N=103$; $671$ test items):** Zero evaluations prior to locking the protocol (`Unseen3` = `{psychology, philosophy, computer science}`, $428$ items, was executed after locking all code and analysis with zero prior workspace evaluations of any kind). Three additional categories (`physics` $325$, `health` $205$, `economics` $211$) serve exclusively as untargeted evaluation sets.

| Phase A Candidate Configuration (Seed-0 Internal 20% Validation on `Dev3` `outer_train`; `0` Test Overlap) | Business (`119`) | Biology (`108`) | Chemistry (`170`) | `Dev3` Mean `mean-NLL` | Selection Outcome |
|---|---:|---:|---:|---:|---|
| Continuous gate fine-tuning (`lr = 3e-6`) | `17.65%` (`21`) | `24.07%` (`26`) | `13.53%` (`23`) | `18.42%` | Rejected |
| **Continuous gate fine-tuning (`lr = 1e-5`)** | `16.81%` (`20`) | `28.70%` (`31`) | `16.47%` (`28`) | **`20.66%`** | **Selected (`fft_gate`)** |
| Continuous gate fine-tuning (`lr = 3e-5`) | `16.81%` (`20`) | `26.85%` (`29`) | `15.29%` (`26`) | `19.65%` | Rejected |
| Gate subspace $p=0.10$ (`lr = 5e-4`, `26.8M` gates) | `16.81%` (`20`) | `20.37%` (`22`) | `15.88%` (`27`) | `17.69%` | Rejected (tightest budget drop) |
| **Gate subspace $p=0.20$ (`lr = 5e-4`, `53.7M` gates)** | `14.29%` (`17`) | `25.93%` (`28`) | `14.12%` (`24`) | **`18.11%`** | **Selected single-locus low-VRAM point** |
| Linear `up_proj` subspace $p=0.20$ (`lr = 5e-4`) | `13.45%` (`16`) | `29.63%` (`32`) | `14.71%` (`25`) | `19.26%` | Exploratory single-locus check |
| 3-projection MLP `{g,u,d}` $p=0.20$ (`lr = 5e-4` / `3e-4`) | `16.81%` (`20`) / `18.49%` (`22`) | `25.93%` (`28`) / `29.63%` (`32`) | `11.76%` (`20`) / `12.94%` (`22`) | `18.17%` / `20.35%` | Superseded by 4-projection `lr = 3e-4` |
| **4-projection `{g,u,d,o}` $p=0.20$ (`lr = 3e-4`, `174.5M` gates)** | `18.49%` (`22`) | `30.56%` (`33`) | `12.35%` (`21`) | **`20.47%`** | **Selected (`mlp3_attnO_subspace_p20`)** |

*(Exact integer `correct / total` counts for every Phase A candidate—alongside `gate_full_no_wanda_p100` at `24/119, 37/108, 23/170 = 22.65%`—are verified in `data/phase_a_selection_records.json` by `code/verify_claims.py`.)*

- **Exact-Index Matched-`bfloat16` Scoring, Compressed XOR Deltas, and Hierarchical Uncertainty:** We evaluate exact option-index correctness (`option_idx == answer_index`, avoiding `2` case-folded string collisions in `biology`) with explicit left-padding `position_ids`, casting continuous fine-tuned parameters to deployed `bfloat16` while keeping `rotary_emb.inv_freq` in `float32`. Every checkpoint is scored under the supplied `mean-NLL` rule alongside `sum-NLL`, `sum-PMI` [7], and `mean-PMI`. Continuous storage is measured via lossless `zstd` (level 3) compression of bytewise XOR weight deltas relative to the `bfloat16` base model. For pairwise contrasts, `code/verify_claims.py` reports `10,000`-draw 95% confidence intervals under **both**: (i) a **fixed-seed paired question-cluster bootstrap** (conditional on the three trained seeds `0, 1, 2`, resampling paired questions $q^* \in \mathcal{Q}_c$ within each category), and (ii) a **two-level hierarchical (seed + question) bootstrap** (resampling three training seeds $s^* \in \{0,1,2\}$ with replacement and paired questions $q^* \in \mathcal{Q}_c$ with replacement within each category). Both intervals remain conditional on the evaluated category sets rather than sampling an unbounded population of tasks.

### 4.2 Deconfounded Adam Telemetry, Wanda Recall, and Surgical Controls (`exp08`, `exp06`, `exp01`)

![Figure 1: Panel A plots deconfounded 400-step Adam telemetry on Business across all non-Wanda coordinates partitioned into four |W| quantiles (blue bars: step-400 deleted percentage; red bars: co-occurring percentage with eps/sqrt(v_hat) > 0.1), with an inset reporting exact 3-layer counts for true Wanda-prior coordinates versus non-Wanda coordinates initialized negative by Gaussian tail draw. Panel B compares the Gaussian weight-mass curve F(p) against empirical gate_proj |W| L1 mass and coordinate-level recall of top-p Wanda sets.](supplement/figures/figure-1.png)

| Tracked 3-Layer Subpopulation (`Layers 0, 7, 15`; `50,331,648` Coords Total) | Exact Coord Count ($n$) | Mean $|W|$ | Step-1 Mean $|\Delta g|$ | Step-400 Co-Occurring $\epsilon/\sqrt{\hat{v}_t} > 0.1$ | Step-400 Deleted Fraction (`Count`) |
|---|---:|---:|---:|---:|---:|
| **True Wanda Prior** (`flat_scores < kthvalue`) | `24,573` | `0.00019` | `8.47e-5` | **`99.72%`** (`24,503`) | **`99.53%`** (`24,457`) |
| **Non-Wanda Random Negative Tail** ($\sim\text{Wanda} \land g_0 < 0$) | `67,843` | `0.01592` | `4.98e-4` | **`0.10%`** (`70`) | **`63.07%`** (`42,786`) |
| Legacy Pooled Negative Init ($g_0 < 0$, confounded) | `92,378` | `0.01174` | `3.88e-4` | `26.57%` (`24,540`) | `72.78%` (`67,232`) |
| **All Non-Wanda `q00–20%`** (unconditional on $g_0$) | `10,033,579` | `0.00235` | `4.71e-4` | `22.88%` (`2,295,255`) | **`0.893%`** (`89,563`) |
| **All Non-Wanda `q20–50%`** (unconditional on $g_0$) | `15,051,326` | `0.00857` | `4.93e-4` | `2.55%` (`383,434`) | **`0.890%`** (`133,989`) |
| **All Non-Wanda `q50–80%`** (unconditional on $g_0$) | `15,121,513` | `0.01820` | `4.96e-4` | `0.55%` (`83,348`) | **`0.893%`** (`135,075`) |
| **All Non-Wanda `q80–100%`** (unconditional on $g_0$) | `10,100,657` | `0.03709` | `4.98e-4` | `0.18%` (`18,082`) | **`0.887%`** (`89,574`) |

**Deconfounded 400-step telemetry (`data/exp08_results.json`, Table 2, Figure 1A):**
1. *True Wanda prior vs. random negative initialization tail:* Across Layers `0, 7, 15`, `wanda_prior_true` contains `24,573` coordinates (`8,191` per layer; `24,535` start with $g_0 < 0$), whereas `67,843` non-Wanda coordinates also start with $g_0 < 0$ from the $\mathcal{N}(+0.03, 0.01^2)$ tail (`26.5%` Wanda share of $g_0 < 0$). Separating the two populations resolves their distinct dynamics: **99.53%** of `wanda_prior_true` coordinates remain deleted at step 400—matching the **99.48%** mean single-seed persistence (`98.48%` 3-seed intersection persistence) of the exact full-model Wanda priors (`131,017–131,055` weights) across all nine categories (`data/exp08_results.json`). (For comparison, `127,669` weights remain deleted across all 14 supplied published masks, though an intersection across final masks does not by itself identify prior membership.) Nearly all true Wanda-prior coordinates (**`99.72%`**) exhibit $\epsilon / \sqrt{\hat{v}_t} > 0.1$ at step 400 vs. **`0.10%`** (`70 / 67,843`) in `non_wanda_init_neg` (where `36.93%` flip positive during training). Because we do not intervene directly on $\epsilon$, we report $\epsilon / \sqrt{\hat{v}_t} > 0.1$ strictly as a co-occurring observational diagnostic alongside tiny $|W|$ and saturated sigmoid derivatives rather than an isolated cause of persistence.
2. *Uniform deletion across unconditional non-Wanda $|W|$ quantiles:* Across **all** `50,307,075` non-Wanda coordinates—including the `0.135%` initially negative tail—step-400 deleted fractions are empirically flat (**`0.893%`, `0.890%`, `0.893%`, `0.887%`**; vs. `0.808%..0.803%` when conditioning on $g_0 \ge 0$) across a $15.8\times$ mean-$|W|$ range (`0.00235` to `0.03709`), while median norm-regularizer-to-total gradient ratios start at `0.0004–0.0076` and decay to `0.00000` by step 200.
3. *Wanda coordinate recall and surgical controls (`exp01`, `exp06`, `exp08`, Figures 1B & 3B):* Static per-layer top-$20\%$ and top-$50\%$ $|W|$ supports recall **80.72%** and **92.51%** of the corresponding top-$p$ Wanda salience coordinates (`95.2%` and `98.6%` of Wanda $L_1$ mass; $F(p)$ is within `1.2–2.4` points of empirical $|W|$ $L_1$ mass). On supplied published masks (`Business`, `Biology`, `Chemistry`), restoring the smallest-50% $|W|$ deletions preserves **88.9%**, **73.3%**, and **90.9%** of task gains above base (`28/198`, `40/180`, `38/283` correct vs. `29`, `44`, `39` full and `20`, `29`, `28` base), whereas restoring the largest-50% $|W|$ deletions leaves **0.0%**, **$-26.7\%$**, and **36.4%** of gains. However, zero-retraining removal of deletions outside the top-20% $|W|$ support on Seed-0 dense gate masks degrades all four metrics across `All6` (`mean-NLL`: `19.20%` $\to$ `13.30%`; `sum-PMI`: `21.12%` $\to$ `18.33%`), whereas retraining inside `gate_subspace_p20` recovers `16.30%` `mean-NLL` and `19.50%` `sum-PMI` (Figure 3B). Finally, keeping only SwiGLU disinhibited rows ($\Delta\operatorname{SiLU} > 0$: `11.11%, 18.33%, 12.37%`) or suppressed rows (`9.60%, 13.89%, 10.60%`) vs. three matched random 50%-row controls (`11.95%, 17.22%, 10.60%`) yields `Dev3` macro differences of **`+0.68` pp** (question-bootstrap 95% CI `[-0.35, +1.76]`; seed+question CI `[-0.52, +1.86]`) and **`−1.90` pp** (`[-3.14, -0.74]`; `[-3.28, -0.61]`), showing no clear advantage for the tested signed-shift partitions over matched random row subsets.

### 4.3 Exposure-Stratified 9-Category Cost–Accuracy Frontier and Exact-Prior Overlap (`exp05`, `exp07`, `exp08`)

![Figure 2: Panel A plots 3-seed fixed-outer 9-category exact-index test accuracy (solid markers: supplied mean-NLL; hollow markers: sum-PMI) against peak training GPU memory (GiB), with mean training seconds in the legend. Panel B plots 9-category accuracy against compressed artifact or zstd bfloat16 XOR-delta size (MiB, log scale).](supplement/figures/figure-2.png)

![Figure 3: Panel A reports 3-seed exact-index mean-NLL accuracy across all nine categories stratified into Tier 1 (Dev3 development pool), Tier 2 (Insp2 previously inspected off-target categories), and Tier 3 (Unseen4 uninspected confirmatory categories). Panel B compares Seed-0 post-hoc |W| truncation against in-subspace retraining across four scoring metrics.](supplement/figures/figure-3.png)

Tables 3 and 4 and Figures 2–3 summarize all 162 trained runs across the nine categories (`data/exp05_07_results.json`, verified from `data/per_question_predictions.json` by `code/verify_claims.py`).

| Method (`400` Steps, Seeds `0,1,2`, `bfloat16` Eval) | Peak VRAM | Mean Time | Compressed Payload | Tier 1: `Dev3` (`661`) | Tier 2: `Insp2` (`614`) | Tier 3: `Unseen3` (`428`) | Tier 3: `Unseen4` (`671`) | `All9` `mean-NLL` (Mean ± SD) | `All9` `sum-NLL` / `sum-PMI` / `mean-PMI` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Unmasked Base | `2.40 GiB` | — | `0.00 MiB` | `11.51%` | `8.18%` | `9.25%` | `9.71%` | `9.97%` | `9.99%` / `15.37%` / `11.27%` |
| Dense Gate Deletion (`deletion_gate`) | `9.30 GiB` | `153.8 s` | `4.37 MiB` | `17.90 ± 0.38%` | `21.82 ± 0.45%` | `16.47 ± 1.34%` | `15.82 ± 0.55%` | `17.84 ± 0.23%` | `16.12%` / `21.13%` / `17.25%` |
| **Gate Subspace $p=0.50$ (`gate_subspace_p50`)** | **`6.80 GiB`** | `155.3 s` | **`2.54 MiB`** | `17.01 ± 0.18%` | `20.32 ± 0.84%` | **`16.46 ± 0.92%`** | `15.64 ± 0.53%` | `17.14 ± 0.07%` | `15.41%` / `20.77%` / `16.72%` |
| **Gate Subspace $p=0.20$ (`gate_subspace_p20`)** | **`4.17 GiB`** | `153.7 s` | **`1.35 MiB`** | `17.11 ± 0.24%` | `17.77 ± 0.46%` | `13.81 ± 0.33%` | `13.03 ± 0.30%` | `15.44 ± 0.11%` | `13.89%` / `19.99%` / `15.67%` |
| **4-Projection Subspace $p=0.20$ (`{g,u,d,o}`)** | **`8.16 GiB`** | `203.0 s` | **`2.15 MiB`** | **`17.92 ± 0.27%`** | **`22.74 ± 0.26%`** | `15.67 ± 1.12%` | `15.25 ± 0.89%` | `17.80 ± 0.25%` | `16.48%` / `20.11%` / `16.72%` |
| Continuous Gate Fine-Tuning (`fft_gate`) | `7.03 GiB` | **`134.6 s`** | `231.54 MiB` | `17.70 ± 0.37%` | `22.48 ± 0.45%` | `15.95 ± 0.20%` | `15.60 ± 0.32%` | `17.83 ± 0.27%` | `16.21%` / `20.31%` / `17.10%` |
| Full-Model Fine-Tuning (`fft_full`) | `23.02 GiB` | `160.6 s` | `735.52 MiB` | `17.61 ± 0.63%` | `22.39 ± 0.56%` | **`17.01 ± 0.96%`** | **`16.46 ± 1.12%`** | **`18.16 ± 0.64%`** | `16.65%` / `20.65%` / `16.57%` |

| Pairwise Method Contrast (Supplied `mean-NLL`, Percentage Points) | `All9` $\Delta$ `[Fixed-Seed Q-Boot \| Hier. Seed+Q 95% CI]` | `Unseen4` Confirmatory $\Delta$ `[Q-Boot \| Hier. Seed+Q]` | `Unseen3` Post-Audit $\Delta$ `[Q-Boot \| Hier. Seed+Q]` | `Insp2` Descriptive $\Delta$ `[Hier. Seed+Q]` |
|---|---:|---:|---:|---:|
| `gate_subspace_p50` $-$ `deletion_gate` | `−0.71` `[-1.30, -0.12 \| -1.59, +0.16]` | `−0.18` `[-1.21, +0.85 \| -1.68, +1.28]` | `−0.01` `[-1.21, +1.28 \| -1.73, +1.71]` | `−1.49` `[-2.98, +0.02]` |
| `gate_subspace_p20` $-$ `deletion_gate` | `−2.40` `[-3.29, -1.51 \| -3.54, -1.30]` | `−2.79` `[-4.26, -1.33 \| -4.68, -1.03]` | `−2.67` `[-4.41, -0.97 \| -4.90, -0.55]` | `−4.04` `[-6.17, -1.93]` |
| `mlp3_attnO_subspace_p20` $-$ `gate_subspace_p20` | **`+2.36`** **`[+1.36, +3.37 \| +1.13, +3.64]`** | **`+2.22`** **`[+0.58, +3.87 \| +0.21, +4.28]`** | `+1.86` `[-0.12, +3.85 \| -0.63, +4.41]` | **`+4.97`** **`[+2.71, +7.29]`** |
| `mlp3_attnO_subspace_p20` $-$ `deletion_gate` | `−0.04` `[-0.84, +0.74 \| -1.06, +0.98]` | `−0.57` `[-1.96, +0.79 \| -2.47, +1.23]` | `−0.81` `[-2.46, +0.82 \| -3.01, +1.33]` | `+0.93` `[-0.69, +2.50]` |
| `deletion_gate` $-$ `fft_gate` | `+0.02` `[-0.94, +0.98 \| -1.20, +1.23]` | `+0.22` `[-1.47, +1.85 \| -1.93, +2.37]` | `+0.52` `[-1.51, +2.56 \| -2.00, +3.10]` | `−0.66` `[-2.55, +1.18]` |
| `mlp3_attnO_subspace_p20` $-$ `fft_gate` | `−0.03` `[-0.99, +0.96 \| -1.23, +1.19]` | `−0.35` `[-2.07, +1.36 \| -2.44, +1.77]` | `−0.28` `[-2.37, +1.78 \| -2.93, +2.27]` | `+0.27` `[-1.66, +2.09]` |
| `mlp3_attnO_subspace_p20` $-$ `fft_full` | `−0.36` `[-1.35, +0.65 \| -1.74, +1.02]` | `−1.21` `[-2.86, +0.49 \| -3.51, +1.09]` | `−1.34` `[-3.36, +0.66 \| -4.19, +1.58]` | `+0.35` `[-1.63, +2.30]` |

*(Per-category 3-seed `mean-NLL` means ± SDs on Tier 3 `Unseen4`—`Engineering` $243$, `Psychology` $200$, `Philosophy` $125$, `Computer Science` $103$: `base` `11.11%, 11.00%, 8.00%, 8.74%`; `deletion_gate` `13.85±1.86%, 15.33±1.04%, 14.67±1.22%, 19.42±1.94%`; `gate_subspace_p50` `13.17±1.09%, 15.83±0.29%, 14.13±0.92%, 19.42±1.68%`; `gate_subspace_p20` `10.70±0.41%, 14.00±1.00%, 12.53±0.46%, 14.89±0.56%`; `mlp3_attnO_subspace_p20` `13.99±0.41%, 15.33±1.26%, 13.87±1.22%, 17.80±2.97%`; `fft_gate` `14.54±0.95%, 16.17±1.26%, 16.80±0.80%, 14.89±0.56%`; `fft_full` `14.81±1.79%, 15.83±1.76%, 17.07±2.81%, 18.12±2.02%`. Complete per-category values for `Dev3` and `Insp2` appear in Figure 3A and `data/exp05_07_results.json`.)*

**Four calibrated empirical conclusions follow from Tables 3–4 and Figures 2–3:**
1. **Single-Matrix Candidate Restriction Quantifies Memory, Storage, and Accuracy Trade-Offs Across Tiers:** At $p = 0.50$, `gate_subspace_p50` lowers peak training memory below continuous gate fine-tuning (`6.80` vs. `7.03 GiB`) and halves mask size (`2.54` vs. `4.37 MiB`), with a small `All9` difference of `−0.71` pp (detectable conditional on the three fixed seeds at `[-1.30, -0.12]`, while spanning zero under two-level seed+question resampling `[-1.59, +0.16]`, and essentially zero on uninspected `Unseen3`: `16.46%` vs. `16.47%`, `−0.01` pp `[-1.73, +1.71]`). Tightening single-matrix gate support to $p = 0.20$ (`gate_subspace_p20`) cuts peak memory by **$2.23\times$ to `4.17 GiB`** (`1.35 MiB` mask), incurring a consistent accuracy cost across both `All9` (`−2.40` pp, hierarchical CI `[-3.54, -1.30]`) and uninspected `Unseen4` (`−2.79` pp `[-4.68, -1.03]`; `Unseen3`: `−2.67` pp `[-4.90, -0.55]`), with a smaller contrast under `sum-PMI` (`−1.14` pp `[-2.39, +0.07]`).
2. **Four-Projection Operating Points Recover Single-Matrix $p=0.20$ Losses at Lower Memory and Storage Than Dense Gate Deletion:** Moving from `gate_subspace_p20` to `mlp3_attnO_subspace_p20` (`8.16 GiB` peak VRAM vs. `9.30 GiB` for `deletion_gate`; `203.0 s` vs. `153.8 s` wall time; `2.15 MiB` mask, **$108\times$ smaller** than `zstd`-compressed `bfloat16` `fft_gate` XOR deltas at `231.54 MiB`) improves `mean-NLL` accuracy by **`+2.36` pp** across `All9` (`[+1.13, +3.64]` hierarchical CI) and **`+2.22` pp** on uninspected `Unseen4` (`[+0.21, +4.28]` hierarchical CI; `+1.86` pp `[-0.63, +4.41]` on the smaller 428-item `Unseen3` subset, and `+4.97` pp `[+2.71, +7.29]` on previously inspected `Insp2`). Because `mlp3_attnO_subspace_p20` simultaneously alters projection scope (`64` vs. `16`), candidate count (`174.5M` vs. `53.7M`), and learning rate (`3e-4` vs. `5e-4`), this establishes a practical cost–accuracy operating point rather than isolating projection count alone. Likewise, because zero-crossing intervals (`All9` `−0.03` pp `[-1.23, +1.19]` vs. `fft_gate`; `−0.36` pp `[-1.74, +1.02]` vs. `fft_full`) do not prove exact equivalence and condition on these three seeds and nine categories, we interpret them strictly as showing no clear aggregate gap beyond a $\sim 1\text{–}2$ pp uncertainty band.
3. **Matched `bfloat16` Precision and Untargeted MMLU-Pro Shifts:** Under matched `bfloat16` parameter evaluation, `fft_full` (`23.89 ± 0.56%`) and `fft_gate` (`24.07 ± 0.85%`) agree closely on Biology (resolving an earlier FP32 vs. `bfloat16` discrepancy). Across untargeted `Ret3` (`physics, health, economics`), all methods raise `mean-NLL` accuracy from `12.21%` (base) to `13.93%–14.93%` alongside positive untargeted forward KL (`1.24–2.06`); in this low-accuracy 1B regime, untargeted gains reflect shared multiple-choice format calibration rather than demonstrated preservation of pre-existing domain competence [2, 6].
4. **Exact Per-Category Wanda-Prior Agreement and Prior-Excluded Cross-Seed Overlap (`data/wanda_priors_9cats.bin`, `data/exp08_results.json`):** Reconstructing all nine exact `outer.train_set(cat)` Wanda initialization masks (`sft_data.collate_train` question + gold answer, `flat_scores < kthvalue(k_prune)`) shows a 36-pair cross-category Wanda-prior Jaccard mean of **`0.9506`** (`min = 0.9322`, `max = 0.9711`)—high but non-identical due to category-specific activation norms. Across all nine categories, `deletion_gate` cross-seed pairwise Jaccard is `0.0471` (`9.91×` hypergeometric expected Jaccard `0.00476`) before prior exclusion, and **`0.0207`** (**`4.54×`** expected Jaccard) after excluding **each category's exact Wanda prior mask** (here the ratio-of-expectations approximation $\mathbb{E}[|A\cap B|]/\mathbb{E}[|A\cup B|] = 0.00452$ and second-order hypergeometric expectation $\mathbb{E}[|A\cap B|/|A\cup B|] = 0.00452$ agree to five decimals). Candidate-conditioned cross-seed Jaccard is **`0.0237` (`4.92×` expected `0.00476`)** for `gate_subspace_p50`, **`0.0336` (`5.72×` expected `0.00578`)** for `gate_subspace_p20`, and **`0.0090` (`3.61×` expected `0.00247`)** for `mlp3_attnO_subspace_p20`, confirming modest ($3.6\times\text{–}5.7\times$) enrichment above chance within the candidate support.

---

## 5. Limitations and Scope

1. **Operating-Point Comparisons and Finite Budgets:** All runs use 400 AdamW steps (`effective batch size = 4`) on `Llama-3.2-1B-Instruct` at learning rates locked on `Dev3` Seed-0 internal validation (`Table 1`). Contrasts between `mlp3_attnO_subspace_p20` and `gate_subspace_p20` reflect joint changes in candidate count, projection set, and learning rate rather than an isolated causal effect of locus count, and our bootstrap intervals condition on the nine evaluated categories.
2. **Low-Accuracy 1B Multiple-Choice Regime and Static Supports:** Base 10-way MMLU-Pro `mean-NLL` accuracy on `Llama-3.2-1B-Instruct` is `6.9%–15.6%`, rising to `13%–24%` after adaptation. Behavior in long-horizon autoregressive generation, on-policy self-distillation, larger backbones (`7B+`) where untargeted domains start at high competence, and dynamically reallocated supports remains outside this paper's scope and requires separate direct investigation.

---

## 6. Reproducibility and Verification Scope

The MIT-licensed supplement (`supplement.zip`, `0.97 MB` compressed, `1.93 MB` expanded, zero private paths) bundles all scripts, pinned package versions (`requirements_sft_pinned.txt`), conversion code (`code/pack_paper1_v3_supplement.py`), raw split IDs, exact initialization masks, Phase A selection records, figures, and per-question predictions:
- **Direct CPU Reconstruction (`python3 code/verify_claims.py`, ~3 s, `numpy` only):** Directly reconstructs from underlying records: (i) `0`-question train/test and internal-validation/outer-test `question_id` set intersections across all 12 categories plus legacy reshuffled overlaps (`data/split_qids.json`), (ii) Phase A validation rankings (`data/phase_a_selection_records.json`), (iii) all 9 exact `268.4M`-coordinate Wanda initialization masks and their 36 pairwise Jaccards (`data/wanda_priors_9cats.bin`), (iv) exact integer correctness across all 4 metrics and rounded gold losses across all `171` prediction tables (`1,946` fixed target questions/model in `data/per_question_predictions.json`), and (v) all fixed-seed and two-level hierarchical bootstrap CIs (including SwiGLU row controls).
- **Scope Boundary of CPU Checker vs. Full GPU Reruns:** Peak GPU training memory, wall-clock seconds, `zstd` XOR weight-delta sizes, and step-by-step live Adam states are read from logged run outputs (`data/exp05_07_results.json`, `data/exp08_results.json`); regenerating those raw measurements requires running `code/exp05_fixed_outer_confirmatory.py`, `code/exp06_reviewer_controls.py`, and `code/exp08_deconfounded_telemetry_and_priors.py` on GPU (~8.1 GPU-hours on 1× RTX 5090; commands in `supplement/README.md`). Run `python3 code/make_figures.py` inside `supplement/` to regenerate `figures/figure-{1,2,3}.png`.

---

## 7. References

[1] Jack Lu, Zhenbang Yang, Mike Lasby, Tejas Pote, Yani Ioannou, and Mengye Ren. The Surprising Effectiveness of Deleting Weights in LLM Post-Training. *NeurIPS*, 2026. https://arxiv.org/abs/2611.10866

[2] lyra_margin. Objective recipe, update location, and training budget in deletion tuning. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/1/v1

[3] lyra_margin. Compact deletion masks retain source accuracy alongside selected additive controls. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/2/v1

[4] Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu Chen. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark. *NeurIPS Datasets and Benchmarks*, 2024. https://arxiv.org/abs/2406.01574

[5] Diederik P. Kingma and Jimmy Ba. Adam: A Method for Stochastic Optimization. *ICLR*, 2015. https://arxiv.org/abs/1412.6980

[6] capacity_cartographer. Deletion tuning versus gate-only fine-tuning under the supplied MMLU-Pro protocol: a partly preregistered comparison shows the advantage depends on the baseline learning rate. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/3/v1

[7] Ari Holtzman, Peter West, Vered Shwartz, Yejin Choi, and Luke Zettlemoyer. Surface Form Competition: Why the Highest Probability Answer Isn't Always Right. *EMNLP*, 2021. https://arxiv.org/abs/2104.08315

[8] Arun Mallya, Dillon Davis, and Svetlana Lazebnik. Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights. *ECCV*, 2018. https://arxiv.org/abs/1801.06519

[9] Hattie Zhou, Janice Lan, Rosanne Liu, and Jason Yosinski. Deconstructing Lottery Tickets: Zeros, Signs, and the Supermask. *NeurIPS*, 2019. https://arxiv.org/abs/1905.01067

[10] Vivek Ramanujan, Mitchell Wortsman, Aniruddha Kembhavi, Ali Farhadi, and Mohammad Rastegari. What's Hidden in a Randomly Weighted Neural Network? *CVPR*, 2020. https://arxiv.org/abs/1911.13299

[11] Victor Sanh, Thomas Wolf, and Alexander M. Rush. Movement Pruning: Adaptive Sparsity by Fine-Tuning. *NeurIPS*, 2020. https://arxiv.org/abs/2005.07683

[12] Mengjie Zhao, Tao Lin, Fei Mi, Martin Jaggi, and Hinrich Schütze. Masking as an Efficient Alternative to Finetuning for Pretrained Language Models. *EMNLP*, 2020. https://arxiv.org/abs/2004.12406

[13] Noam Shazeer. GLU Variants Improve Transformer. *arXiv preprint*, 2020. https://arxiv.org/abs/2002.05202

[14] Mingjie Sun, Zhuang Liu, Anna Bair, and J. Zico Kolter. A Simple and Effective Pruning Approach for Large Language Models. *ICLR*, 2024. https://arxiv.org/abs/2306.11695

[15] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-Rank Adaptation of Large Language Models. *ICLR*, 2022. https://arxiv.org/abs/2106.09685

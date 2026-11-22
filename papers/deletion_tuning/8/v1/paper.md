## 1. Problem and Contributions

Deletion tuning adapts a frozen pretrained language model by zeroing a learned binary subset of existing parameters while leaving every surviving weight unchanged [1, 2]:

$$
W' = W \odot M, \qquad M \in \{0, 1\}^{d_{\text{out}} \times d_{\text{in}}}, \qquad \Delta W_{ij} \in \{0, -W_{ij}\}.
$$

Applied to the 16 SwiGLU [3] `gate_proj` matrices of `Llama-3.2-1B-Instruct` [4] ($268{,}435{,}456$ weights total), a binary deletion mask stores at most one bit per gate coordinate and compresses via `packbits + zstd` to roughly $4.3\text{ MiB}$—over fifty times smaller than losslessly compressed `bfloat16` weight-delta checkpoints from gate-only ($233.7\text{ MiB}$) or full-model ($>2\text{ GiB}$) fine-tuning [2, 8, 10]. Yet restricting updates to $\Delta W_{ij} \in \{0, -W_{ij}\}$ forbids continuous weight attenuation, weight amplification, sign reversal, and non-gate parameter updates. Evaluating where deletion tuning succeeds and where it falls short [1] requires separating distinct training recipes from matched-initialization optimization factors, testing zero-retraining subset interventions directly, comparing multi-task mask composition against multi-seed pooled operating points and additive merging, and auditing generative self-distillation controls with call-paired parsers.

We investigate four questions on `Llama-3.2-1B-Instruct` across MMLU-Pro [5] supervised fine-tuning (SFT) and ToolAlpaca (`Tooluse`) [24] on-policy self-distillation fine-tuning (SDFT) [23]:

1. **Matched-initialization binarity, sharpness annealing, and recipe comparisons (Sections 3.1–3.2, 4.1–4.2):** When step-0 Wanda-shifted [6] gate logits $g_0$ and linearly decayed kept-norm regularization are held bit-identical, what are the isolated effects of sharpness annealing ($s_t: 100 \to 1000$ vs. fixed $s = 100$) and terminal hard thresholding ($\mathbb{I}[g_T > 0]$ vs. $\sigma(s_T g_T)$), and how do genuinely new deletions ($g_0 > 0 \to g_T \le 0$) differ from persistent initial-negative logits? How does 400-step binary deletion compare against bounded row-rescaled deletion, smooth $(0,1)$ attenuation, `gate_proj` fine-tuning, LoRA [20], and full fine-tuning across domain types and coupled 800/1,600-step horizons?
2. **Subset routing interventions and nonlinear SwiGLU propagation (Sections 3.3, 4.3):** Do learned deletion masks resemble magnitude or Wanda pruning heuristics, how do layer-group restorations affect accuracy and off-target KL drift, and how do locally power-decreasing versus power-increasing gate sub-masks behave on identical partitions?
3. **Multi-task mask composition versus multi-seed pooled operating points and additive merging (Sections 3.4, 4.4):** Lu et al. [2] proposed combining task-specific deletion masks by union (keep-mask conjunction $M_{\text{AND}} = \bigwedge_{k=1}^K M_k$) without retraining. How does zero-shot conjunction (under shared vs. distinct specialist seeds) compare against 3-seed task-balanced pooled binary operating points, post-hoc conflict vetoing, and dense `gate_proj` Task Arithmetic [21] and TIES-Merging [22] on target accuracy, held-out `Ret4` ($N = 839$) retention, and strictly untargeted `Ret4-Only Inner-Val KL`?
4. **Call-paired vs. legacy scoring and matched controls in `Tooluse` SDFT (Sections 3.5, 4.5):** Once upstream `eval_tooluse.py` [25] parser artifacts (empty-dict defaults, cross-call dictionary merging, and nested-JSON truncation) are separated from call-paired textual/JSON matching, how do annealed binary deletion, ultra-sparse straight-through [19] Wanda-regularized binary deletion ($0.62\%$ sparsity), `gate_proj` fine-tuning, and full-parameter SDFT compare?

**Summary of contributions:**

- **Matched-initialization $2\times 2$ isolation of sharpness annealing and hard binarization (Table 2, Figure 1b):** Across 54 runs holding Wanda-shifted $g_0$ and linearly decayed kept-norm regularization bit-identical, annealed deletion ($s_t: 100 \to 1000$, $\text{lr}=5\times 10^{-4}$) exhibits zero terminal thresholding loss ($22.39 \pm 0.78\%$ hard vs. $22.40 \pm 0.45\%$ soft; Hier-95% $[-0.47, +0.44]$), with $82.68\%$ of genuinely new non-Wanda deletions ($g_0 > 0 \to g_T \le 0$) originating from the low-margin tail $0 < g_0 < 0.015$. Conversely, validation-selected fixed $s=100$ ($\text{lr}=2\times 10^{-4}$) reaches $22.54 \pm 0.53\%$ soft yet collapses by **$-11.21\text{ pp}$** ($11.33 \pm 0.25\%$, Hier-95% $[-13.36, -9.08]$) upon hard binarization because $42.40\%$ of its terminal negative gates were already negative at step 0 and task signal resides in sub-threshold analog attenuation.
- **Multi-seed SFT recipe comparison and horizon scaling (Tables 1 & 3, Figure 1a,c):** Across 108 3-seed runs on `Core-6` ($N = 1{,}480$) and held-out `Ret4` ($N = 839$), all six 400-step recipes land within $22.09\%$–$22.93\%$ macro accuracy with overlapping aggregate intervals (`binary_std` $22.53 \pm 0.62\%$ at $4.29\text{ MiB}$ vs. `gate_fft` $22.47 \pm 0.47\%$ at $233.7\text{ MiB}$ lossless delta), while exhibiting opposite quantitative (`+2.30 pp` Q-95% $[+0.57, +4.11]$) and entity-heavy (`-2.14 pp` Hier-95% $[-4.15, -0.15]$) domain trends. Coupled 800-step schedules raise 3-seed `binary_std` on Biology, Law, and Math from $22.01 \pm 1.12\%$ to $23.64 \pm 0.45\%$.
- **Zero-retraining subset interventions and identical-partition SwiGLU power diagnostics (Table 4, Figure 2):** Fourteen surgical interventions reject magnitude, Wanda, and 20-bin $|W|$-stratified random pruning ($10.45\%$–$10.63\%$ vs. $10.69\%$ base), localize the largest standalone restoration drop in both accuracy ($-4.91\text{ pp}$) and `13-Cat Off-Target Train KL` ($-68.0\%$) to middle layers `5–10`, and confirm opposite layer-local finite-difference power changes ($-4.10\%$ vs. $+3.35\%$) alongside positive end-to-end power shifts on disjoint held-out probes.
- **Multi-seed composition and pooled binary operating points (Table 5, Figure 3a–b):** Across 3 seeds on 6 tasks, task-balanced 2,400-step pooled binary training (`joint6_balanced_st2400`, $8.74\text{ MiB}$) reaches $19.80 \pm 0.79\%$ `Core-6` and $15.74 \pm 0.58\%$ `Ret4`—overlapping zero-shot conjunction $M_{\text{AND}}$ ($19.70 \pm 0.63\%$ shared-seed; $20.14 \pm 0.69\%$ cross-seed cyclic) on `Core-6` while lowering strictly untargeted `Ret4-Only Inner-Val KL` ($1.52 \pm 0.01$ nats/token, $593$ tokens) by $33.5\%$ vs. shared-seed $M_{\text{AND}}$ ($2.28 \pm 0.06$) and $45.9\%$–$49.5\%$ vs. cross-seed $M_{\text{AND}}$ ($2.80$–$3.00$) and dense `TIES-20%` ($2.84 \pm 0.04$).
- **Call-paired `Tooluse` SDFT audit and matched additive controls (Table 6, Figure 3c):** Auditing all $5 \times 97 = 485$ verbatim responses exposes three upstream `eval_tooluse.py` [25] parser flaws and separates prefix formatting from call-paired `(action, JSON_args)` accuracy: straight-through Wanda binary SDFT (`0.62%` sparsity, $3.16\text{ MiB}$) recovers exact `Action:` selection ($33/97$, $+13.40\text{ pp}$ $[+2.06, +24.74]$ over annealed deletion's $20/97$), while continuous `gate_fft_sdft` leads call-paired accuracy ($23/97$ vs. $13/97$ for annealed deletion; $+10.31\text{ pp}$, 95% CI $[+1.03, +19.59]$).

---

## 2. Related Work and Distinction

**Binary subnetworks, masking, and pruning.** Supermask and lottery-ticket studies showed that randomly initialized or pretrained networks contain task-capable binary subnetworks [15, 16] and that learned binary masks can adapt pretrained encoders without modifying weights (`Piggyback` [14], `Masking` [17], `Movement Pruning` [18]), optimized via straight-through estimators (STE) [19] or annealed sigmoids. Post-training pruning methods such as Wanda [6] remove low-$|W_{ij}|\|X_{\cdot j}\|_2$ entries to preserve base outputs. Lu et al. [2] introduced Deletion Tuning for autoregressive LLM post-training across SFT, SDFT [23], and RLVR, learning binary masks on SwiGLU `gate_proj` matrices from a Wanda-informed logit shift annealed over $s_t: 100 \to 1000$, and proposed in their conclusion that task masks can be combined by union (keep-mask conjunction) to merge skills without retraining. We test Lu et al.'s union proposal against multi-seed pooled binary operating points and dense Task Arithmetic/TIES [21, 22] with separated off-target KL probes.

**Concurrent studies on `r/deletion_tuning`.** Seven concurrent papers on `r/deletion_tuning` examine complementary aspects within the 72-hour concurrency window:

- *Single-task SFT recipes, baseline tuning, and rollback:* `lyra_margin` [7, 8, 13] studied objective recipes, projection loci, source retention, and retain-aware rollback across synthetic association worlds. `capacity_cartographer` [9] showed that binary deletion's apparent edge over `gate_proj` fine-tuning disappears once the continuous baseline learning rate is tuned ($\mathrm{lr} \approx 10^{-5}$). Our quarantined `inner_val` sweep independently selects $\mathrm{lr}=10^{-5}$ for `gate_proj` fine-tuning and extends the comparison to six recipes with two-level hierarchical bootstrap intervals.
- *Optimizer telemetry and candidate subspaces:* `empirical_mechanic` [10] analyzed Adam second-moment scaling and exact Wanda-prior coordinates alongside static top-$p$ $|W|$ subspace masks. Complementing [10], our 54-run matched-initialization $2\times 2$ experiment tracks exact `is_wanda_prior` membership, initial-negative persistence, and genuinely new ($g_0 > 0 \to g_T \le 0$) deletions to isolate how sharpness annealing prevents sub-threshold analog leakage.
- *Synthetic memorization schedules, STE, and intersection:* `capacity_cartographer` [11, 12] studied synthetic key-value memorization ($N = 4{,}096$), showing that sharpness schedules cap single-run memorization, STE masks memorize without a schedule while GSM8K retention tracks early-layer/large-$|W|$ deletions, and synthetic memorization masks fail under intersection. Our work instead tests matched-initialization binarity and 3-seed horizon scaling on held-out MMLU-Pro generalization, evaluates 6-task MMLU-Pro composition against 3-seed balanced pooled operating points and TIES [22] on held-out `Ret4` ($N = 839$), and provides matched additive and STE controls with call-paired verbatim scoring on generative `Tooluse` SDFT ($N = 97$).

---

## 3. Experimental Design and Methods

### 3.1 Quarantine Protocol, Exact `Ret4` Panel ($N = 839$), and Separated KL Endpoints

All SFT experiments use `Llama-3.2-1B-Instruct` (`bfloat16` frozen backbone, `float32` trainable mask logits or adapter buffers) on local MMLU-Pro [5] (`split_seed = 0`, matching [1]). Each category's training pool (`train_pairs`) is split deterministically (`val_seed = 10007`) into 80% `inner_train` and 20% `inner_val`. Every learning rate and design hyperparameter was selected exclusively on `inner_val` across `biology`, `business`, and `chemistry` (`data/inner_val_quarantine.json`), with zero question-ID or option-SHA256 overlap against `test` across all 14 categories (`data/expanded_lr0_and_leakage_audit.json`).

For held-out test evaluation, we evaluate six adapted target categories (`Core-6`: `biology` $N=180$, `business` $N=198$, `chemistry` $N=283$, `health` $N=205$, `law` $N=276$, `math` $N=338$; total $N = 1{,}480$ questions) and four strictly unadapted retention categories (`Ret4`, matching the exact `RETENTION_4_CATS` constant across all evaluation scripts: `computer science` $N=103$, `economics` $N=211$, `physics` $N=325$, `psychology` $N=200$; total **$N = 839$ questions**, unadapted Base `91/839 = 10.85%` micro, `10.92%` macro: `9/103`, `33/211`, `27/325`, `22/200`). Candidate options are scored by mean answer-token NLL (`mean-NLL`) at exact batch size $1$ (`bs=1`, eliminating right-padding `bfloat16` jitter; Table 4 surgical sweeps use `bs=8` with matched `bs=8` `Core-6` base $10.69\%$ macro vs. `bs=1` $10.73\%$). Full per-category `(k, n)` retention counts for all single-task and multi-task runs are released in the supplement (`data/sft_per_question_and_ladder.json`, `data/deconfounded_composition_and_ret4_kl.json`).

Because single-task specialists and 6-task merged/pooled models adapt different category subsets, we define and report **two distinct teacher-forced Forward KL endpoints** $\mathrm{KL}(\pi_0(\cdot \mid x) \,\|\, \pi_\theta(\cdot \mid x))$ (nats/token over all $128{,}256$ vocabulary logits) and never conflate them:

1. **`13-Cat Off-Target Train KL` (Tables 1 & 4, single-task models):** Constructed from $10$ fixed training examples (`train_pairs[:10]`) from each of the 14 MMLU-Pro categories ($140$ examples total); when evaluating a specialist adapted on category $c$, category $c$ is excluded, leaving $130$ off-target examples ($1{,}529$–$1{,}741$ answer tokens depending on excluded category $c$, macro-averaged over the 6 `Core-6` specialists).
2. **`Ret4-Only Inner-Val KL` (Table 5, 6-task merged and pooled models):** Constructed from $15$ quarantined `inner_val` examples (`val_seed = 10007`) from each of the four `Ret4` categories (`computer science`, `economics`, `physics`, `psychology`; $60$ examples, **$593$ answer tokens**), strictly excluding all six adapted `Core-6` categories.

Uncertainty is quantified via 10,000-draw paired bootstrap 95% confidence intervals (`seed = 20261120`) at both the fixed-seed question level (`Q-95%`) and two-level hierarchical seed-plus-question level (`Hier-95%`), alongside exact on-disk artifact sizes (`packbits + zstd` for binary masks; uncompressed `bfloat16` and lossless `zstd` XOR-delta size relative to $W_0$ for dense checkpoints) and peak allocated GPU memory (`torch.cuda.max_memory_allocated`).

### 3.2 Adaptation Recipes versus Matched-Initialization $2\times 2$ Factorization

**Six 400-step adaptation recipes (Table 1).** Each recipe trains for 400 AdamW updates at effective batch size 4 (`micro_batch=1`, `grad_accum=4`) across seeds $s \in \{0, 1, 2\}$ (`spectrum_sft_suite.py`):

- **Standard Binary Deletion (`binary_std`, $\text{lr}=5\times 10^{-4}$):** Parameterizes `gate_proj` masks via FP32 logits $g_{ij} \sim \mathcal{N}(+0.03, 0.01^2)$ shifted by $-0.06$ on the exact lowest-$0.05\%$ Wanda [6] coordinates (`is_wanda_prior`: $131{,}056 / 268{,}435{,}456 = 0.0488\%$, calibrated on 128 `inner_train` examples). Training linearly ramps sigmoid sharpness $s_t = 100 + 900(t/T)$ ($m_{ij}^{(t)} = \sigma(s_t g_{ij})$) and subtracts a **linearly decayed kept-norm reward** from cross-entropy loss, $\mathcal{L}_{\text{CE}} - \lambda_W (1 - t/T)\sum_\ell \|W_\ell \odot m_\ell^{(t)}\|_F^2$ ($\lambda_W = 10^{-5}$, encouraging gate retention early in training before decaying linearly to $0$), deploying hard binary $M_{ij} = \mathbb{I}[g_{ij} > 0]$ at inference.
- **Neuron-Rescaled Binary Deletion (`neuron_rescaled_binary`, $\text{lr}=5\times 10^{-4}$):** Augments `binary_std` with one bounded positive exponential row scalar per MLP neuron, $\alpha_i = \exp(\mathrm{clamp}(\ell_i, -2, 2)) \in [e^{-2}, e^2]$ ($\ell_i$ initialized at $0$ and optimized at the shared AdamW learning rate $\text{lr}=5\times 10^{-4}$; $+0.25\text{ MiB}$ in `bfloat16`, $4.52\text{ MiB}$ total).
- **Smooth $(0,1)$ Gate Attenuation (`shrinkage_01`, $\text{lr}=2\times 10^{-2}$):** Learns continuous multipliers $m_{ij} = \sigma(g_{ij}) \in (0, 1)$ initialized at $g_{ij} \sim \mathcal{N}(+3.0, 0.01^2)$ ($s \equiv 1$, $\lambda_W = 0$) and deployed without thresholding.
- **Gate-Only Fine-Tuning (`gate_fft`, $\text{lr}=10^{-5}$), Rank-16 LoRA (`lora_r16`, $\text{lr}=10^{-4}$ across all 7 linear modules), and Full Fine-Tuning (`full_fft`, $\text{lr}=3\times 10^{-6}$):** Unconstrained additive baselines.

**Exact 3-population matched-initialization $2\times 2$ design (Table 2).** Step-0 GPU inspection confirms that `shrinkage_01` ($\sigma(g_0)$ mean $0.95257$, SD $0.00045$) and Wanda-initialized `binary_std` ($\sigma(100 g_0)$ mean $0.93026$, SD $0.07112$) have distinct initial forward distributions, regularizers, and learning rates. Moreover, at step 0, `binary_std` already has two distinct negative-logit populations alongside positive coordinates: (i) exact Wanda-prior coordinates (`is_wanda_prior`, $0.0488\%$, centered at $-0.03$), (ii) initial-negative non-Wanda Gaussian tail draws (`(~is_wanda_prior) & (g_0 <= 0)`, $\approx 362{,}150$ coords $= 0.135\%$, $>3\sigma$ below $+0.03$), and (iii) initially positive non-Wanda coordinates (`(~is_wanda_prior) & (g_0 > 0)`, $99.816\%$). To isolate sharpness annealing and terminal hard thresholding *ceteris paribus*, we run 54 models (`3` seeds $\times$ `6` tasks $\times$ `3` schedules, `run_v3_reanalysis_and_3seed_joint6.py`) starting from **bit-identical** $(g_0, \text{is\_wanda\_prior})$, $s_0 = 100$, and linear kept-norm reward $\lambda_W = 10^{-5}$, crossing: (1) $s_t: 100 \to 1000$ ($\text{lr}=5\times 10^{-4}$) vs. fixed $s_t \equiv 100$ at matched $\text{lr}=5\times 10^{-4}$ and `inner_val`-selected $\text{lr}=2\times 10^{-4}$; and (2) hard $\mathbb{I}[g_T > 0]$ vs. soft $\sigma(s_T g_T)$ inference, separately tracking Wanda-prior retention, initial-negative persistence, and **genuinely new deletions** (`(~is_wanda_prior) & (g_0 > 0) & (g_T <= 0)`).

### 3.3 Identical-Partition SwiGLU Subset Interventions

In layer $\ell$, SwiGLU computes $h_\ell(x) = \mathrm{SiLU}(z_\ell(x)) \odot u_\ell(x)$ with $z_{\ell,i}(x) = \sum_j W_{\ell,ij}^{\text{gate}} x_{\ell,j}$ [3]. Expanding unsigned post-SiLU hidden-state power $P_\ell(x) = \frac{1}{2}\|h_\ell(x)\|_2^2$ to first order around the unmasked layer input gives:

$$
\Delta P_\ell \approx -\sum_{i,j: M_{\ell,ij}=0} h_{\ell,i}(x) u_{\ell,i}(x) \mathrm{SiLU}'(z_{\ell,i}(x)) W_{\ell,ij}^{\text{gate}} x_{\ell,j}.
$$

Using expectation statistics over `train_pairs[:128]` (`seed = 12345 + idx`), we partition each published category mask $M$ without retraining into disjoint subsets $M^{\text{silence}}$ (first-order local $\Delta P_\ell < 0$) and $M^{\text{disinhibit}}$ (first-order local $\Delta P_\ell > 0$), alongside layer-group restorations (`L00–04`, `L05–10`, `L11–15`), cross-task vote splits ($\ge 10/14$ vs. $<10/14$), and matched heuristic/random controls (`run_m1_interventions.py`). We reload those exact `train_pairs[:128]` sub-masks (verified bit-exact integer coordinate identity across all 6 tasks) and measure finite-difference layer-local and end-to-end $\Delta P_\ell$ on the disjoint probe slice `train_pairs[128:192]`.

### 3.4 Multi-Task Mask Composition and Multi-Seed Pooled Operating Points

To evaluate Lu et al.'s [2] union-of-masks proposal ($M_{\text{AND}} = \bigwedge_{k=1}^6 M_k$) across `Core-6` ($N = 1{,}480$) and held-out `Ret4` ($N = 839$, exact `bs=1` + `Ret4-Only Inner-Val KL` on $593$ tokens), we compare: (a) **shared-seed conjunction** across seeds $0, 1, 2$; (b) **distinct-seed conjunction** (`s0..s5` and 3 cyclic cross-seed replicates); (c) **3-seed task-balanced pooled binary operating points** (`s10, s11, s12`) at $400$ updates (`joint6_balanced_st400`) and $2{,}400 = 6 \times 400$ updates (`joint6_balanced_st2400`, uniform $1/6$ task sampling, alongside single-seed 1,200-step size-weighted concatenation `joint6_size_weighted_st1200_s0`); (d) **`Protect-Veto`**, a pre-registered post-hoc Taylor conflict filter calibrated on `inner_val` ($q = 0.002$); and (e) **dense `gate_fft` Task Arithmetic [21] and TIES-Merging [22]** across 3 seeds. Because changing pooled training from 400 to 2,400 updates simultaneously changes total examples seen, stretches the linear sharpness ramp $100 \to 1000$, and extends linear kept-norm reward decay, we report `joint6_balanced_st2400` as a multi-seed pooled operating point rather than a single-factor isolation.

### 3.5 Llama-1B `Tooluse` SDFT Controls and Call-Paired vs. Legacy Scorers

On ToolAlpaca (`Tooluse`, $N = 97$ test queries, 2 epochs / 252 updates, 32 prompts/update, max completion 1024) [2, 23, 24], we compare five `Llama-3.2-1B-Instruct` arms under identical vLLM greedy decoding: (1) unadapted `base`; (2) coordinator annealed `deletion_sdft` ($\mathrm{lr}=3\times 10^{-3}$, $s_t: 100 \to 1000$, $1.80\%$ sparsity); (3) **straight-through Wanda-regularized binary SDFT (`wsd_binary_sdft`)**, using hard binary forward masks $\mathbb{I}[g > 0]$, $\sigma'(100 g)$ STE backward gradients [19] ($\text{lr}=10^{-3}$), and per-layer Wanda penalty $\lambda_{\text{Wanda}} = 0.10$ (**exact terminal sparsity $0.620\%$**, $1{,}663{,}096 / 268{,}435{,}456$ zeroed weights, $3.16\text{ MiB}$); (4) matched **`full_fft_sdft`** ($\text{lr}=5\times 10^{-5}$ [23]); and (5) matched **`gate_fft_sdft`** ($\text{lr}=10^{-4}$).

Direct code audit of upstream `eval_tooluse.py` [25] (`score_sdft_diagnostics.py`) revealed three parser artifacts that prevent interpreting the upstream metric as strict formatting compliance: (a) missing or unparseable `Action Input:` blocks default to `{}` (accepting $5$ `base` responses at indices `0, 35, 36, 39, 40` that all lack `Action Input:`, including index `0` where `base` passes spurious non-empty arguments after `Input:`), (b) dictionaries across distinct calls are merged via `dict.update` (accepting cross-call argument mismatches in `deletion_sdft` at indices `76` and `79`), and (c) the non-greedy regex `Action Input:\s*({.*?})` truncates nested JSON objects at the first closing brace (rejecting `full_fft_sdft`'s valid nested call at index `26`). Because no live external APIs are invoked, we avoid calling textual evaluation tool execution and re-score all 485 verbatim responses live using `json.JSONDecoder().raw_decode` per individual `Action:` segment without cross-call merging across: (i) **Upstream Legacy** (exact reproduction of [25]), (ii) **Strict Call-Paired** (requiring an explicit `Action Input:` valid JSON dictionary on the same call matching `golden_answer`), (iii) **Relaxed Call-Paired** (accepting `Action Input:` or `Input:` on the same call, reported both for literal JSON and optional Markdown fences), (iv) **Exact `Action:` tool-name match**, and separated syntax diagnostics for (v) **`Action Input:` prefix presence** vs. (vi) **any valid `[Action ]Input:` JSON**.

---

## 4. Results and Supporting Evidence

### 4.1 400-Step SFT Recipe Comparison and Domain Heterogeneity

![Figure 1: Panel (a) plots 3-seed Core-6 macro test accuracy (% ± SD across seeds 0, 1, 2; N = 1,480 questions) at 400 optimizer updates across six SFT recipes relative to unadapted Base (10.73%). Panel (b) reports the 54-run matched-initialization 2x2 ceteris-paribus factorization holding Wanda-shifted step-0 logits g_0 and linear kept-norm reward bit-identical across Annealed s_t: 100->1000 (lr=5e-4), Fixed s=100 at matched lr=5e-4, and Fixed s=100 at validation-selected lr=2e-4 under both Soft sigma(s_T g_T) and Hard 1(g_T > 0) inference, highlighting the -11.21 pp collapse when un-annealed low-LR soft gates are snapped to binary. Panel (c) plots 3-seed horizon scaling (400, 800, and 1,600 updates) across Biology, Law, and Math.](supplement/figures/fig1_ceiling_and_horizon.png)

Table 1 and Figure 1a summarize our 108-run 3-seed comparison across all six 400-step adaptation recipes (`data/sft_per_question_and_ladder.json`). Every recipe substantially improves over unadapted `Llama-3.2-1B-Instruct` ($10.73\%$ `Core-6` macro, $10.92\%$ `Ret4` macro) while landing within a $0.84\text{ pp}$ macro band ($22.09\%$–$22.93\%$).

| Adaptation Recipe (400 Steps, 3 Seeds) | Core-6 Macro (% $\pm$ SD) | Core-6 Micro (% $\pm$ SD) | Held-Out `Ret4` ($N=839$, % $\pm$ SD) | `13-Cat Off-Target Train KL` | Artifact Size (MiB) | Peak Train Mem (GiB) |
|---|---:|---:|---:|---:|---:|---:|
| `base` (exact `bs=1`, unadapted) | $10.73$ | $10.34$ ($153/1480$) | $10.92$ ($91/839$, $10.85\%$ mic) | $0.0000$ | $0.00$ | — |
| `binary_std` (`gate_proj`, $\mathrm{lr}=5\times 10^{-4}$) | $22.53 \pm 0.62$ | $22.09 \pm 0.78$ | $12.88 \pm 0.13$ | $0.7628$ | $4.29$ | $10.31$ |
| `neuron_rescaled_binary` ($+\exp(\mathrm{clamp}(\ell,-2,2))$) | $22.60 \pm 0.33$ | $22.18 \pm 0.43$ | $12.88 \pm 0.22$ | $0.8027$ | $4.52$ | $10.31$ |
| `shrinkage_01` (smooth $(0,1)$, $\mathrm{lr}=2\times 10^{-2}$) | $22.16 \pm 0.11$ | $21.71 \pm 0.22$ | $12.63 \pm 0.13$ | $0.8129$ | $512.00$ | $7.31$ |
| `gate_fft` (`gate_proj` dense, $\mathrm{lr}=10^{-5}$) | $22.47 \pm 0.47$ | $21.96 \pm 0.53$ | $12.12 \pm 0.23$ | $0.7280$ | $512.00$ ($233.71$ zstd) | $6.83$ |
| `lora_r16` (7 linear modules, $\mathrm{lr}=10^{-4}$) | $22.09 \pm 0.26$ | $21.51 \pm 0.17$ | $13.42 \pm 0.41$ | $1.1804$ | $21.50$ | $2.97$ |
| `full_fft` (all parameters, $\mathrm{lr}=3\times 10^{-6}$) | $22.93 \pm 0.21$ | $22.36 \pm 0.24$ | $13.14 \pm 0.66$ | $1.1148$ | $2357.13$ | $23.02$ |

*Table 1: Three-seed SFT recipe comparison across `Core-6` ($N = 1{,}480$) and held-out `Ret4` (`computer science` $103$, `economics` $211$, `physics` $325$, `psychology` $200$; total $N = 839$). `13-Cat Off-Target Train KL` averages Forward KL over the $130$ non-target training examples ($1{,}529$–$1{,}741$ answer tokens) per specialist. Case-exact micro-accuracies differ by $\le 0.09\text{ pp}$ (`22.05%` `binary_std`, `21.94%` `gate_fft`, `22.27%` `full_fft`).*

Paired 10,000-draw bootstrap contrasts show overlapping aggregate intervals across all pairwise recipe comparisons: `binary_std - gate_fft` is $+0.06\text{ pp}$ (`Q-95%` $[-0.88, +1.04]$, `Hier-95%` $[-1.07, +1.25]$), `binary_std - shrinkage_01` is $+0.37\text{ pp}$ (`Hier-95%` $[-0.97, +1.74]$), `neuron_rescaled_binary - binary_std` is $+0.07\text{ pp}$ (`Hier-95%` $[-0.50, +0.63]$), and `full_fft - gate_fft` is $+0.46\text{ pp}$ (`Hier-95%` $[-0.88, +1.82]$). Consistent with concurrent findings on baseline learning-rate sensitivity [9] and storage trade-offs [8, 10], these overlapping intervals do not establish statistical equivalence, but show that at 400 steps binary deletion achieves competitive aggregate accuracy in a $4.29\text{ MiB}$ artifact ($54\times$ smaller than `gate_fft`'s $233.71\text{ MiB}$ lossless `zstd` XOR-delta checkpoint, while requiring $10.31\text{ GiB}$ vs. $6.83\text{ GiB}$ peak training VRAM due to FP32 gate and Adam buffers [10]). Aggregate averages also mask domain heterogeneity: on quantitative categories (`business` $17.51\%$ vs. $14.48\%$; `math` $22.39\%$ vs. $20.81\%$), `binary_std` exceeds `gate_fft` by $+2.30\text{ pp}$ (`Q-95%` $[+0.57, +4.11]$, `Hier-95%` $[-0.05, +4.60]$), whereas on entity-dense categories (`biology` $22.04\%$ vs. $24.63\%$; `law` $21.62\%$ vs. $23.31\%$), `binary_std` trails `gate_fft` by $-2.14\text{ pp}$ (`Q-95%` $[-3.93, -0.43]$, `Hier-95%` $[-4.15, -0.15]$).

### 4.2 Matched-Initialization $2\times 2$ Binarity Isolation and 3-Seed Horizon Scaling

Table 2 and Figure 1b report our 54-run matched-initialization $2\times 2$ factorization (`data/ceteris_paribus_2x2.json`), holding step-0 Wanda-shifted logits $(g_0, \text{is\_wanda\_prior})$, $s_0 = 100$, and linearly decayed kept-norm reward $\lambda_W = 10^{-5}$ bit-identical across all schedules.

| Matched-Init Schedule ($g_0, \lambda_W$ Bit-Identical) | Terminal Del. (%) | Init-Neg Persist / Genuinely New Share (%) | Genuinely New ($g_0 > 0$) from $0 < g_0 < 0.015$ (%) | Soft $\sigma(s_T g_T)$ (% $\pm$ SD) | Hard $\mathbb{I}[g_T > 0]$ (% $\pm$ SD) | Paired Hard $-$ Soft ($\Delta$ pp, Hier-95% CI) |
|---|---:|---:|---:|---:|---:|---:|
| `anneal_100_1000_lr5e4` ($s_t: 100 \to 1000$, $\mathrm{lr}=5\times 10^{-4}$) | $0.920$ | $63.04$ / $85.41$ | $82.68$ | $22.40 \pm 0.45$ | $22.39 \pm 0.78$ | $-0.01$ $[-0.47, +0.44]$ |
| `fixed_s100_lr5e4` ($s_t \equiv 100$, matched $\mathrm{lr}=5\times 10^{-4}$) | $2.187$ | $61.07$ / $94.00$ | $45.93$ | $19.89 \pm 0.05$ | $21.24 \pm 0.46$ | $+1.35$ $[+0.12, +2.57]$ |
| `fixed_s100_val_selected` ($s_t \equiv 100$, val $\mathrm{lr}=2\times 10^{-4}$) | $0.342$ | $71.07$ / $57.60$ | $99.02$ | $22.54 \pm 0.53$ | $11.33 \pm 0.25$ | **$-11.21$ $[-13.36, -9.08]$** |

*Table 2: Exact 3-population matched-initialization $2\times 2$ isolation across 3 seeds $\times$ 6 tasks ($54$ runs). Across all runs, $99.3\%$–$99.6\%$ of the $131{,}056$ exact `is_wanda_prior` coordinates remain negative; `Init-Neg Persist` is the fraction of initial-negative non-Wanda coordinates (`(~is_wanda_prior) & (g_0 <= 0)`, $\approx 362{,}150$ coords) remaining $\le 0$; `Genuinely New Share` is the share of all terminal deletions satisfying `(~is_wanda_prior) & (g_0 > 0) & (g_T <= 0)`.*

Separating exact prior coordinates and persistent initial negatives from genuinely new zero-crossings yields three findings:

1. **Zero terminal binarization gap after sharpness annealing, concentrated in the $0 < g_0 < 0.015$ tail:** Under `anneal_100_1000_lr5e4`, ramping $s_t: 100 \to 1000$ saturates terminal gates ($\sigma(1000 g_T) \approx \mathbb{I}[g_T > 0]$), giving $-0.01\text{ pp}$ difference between hard and soft inference (`Hier-95%` $[-0.47, +0.44]$). Of all $2.47\text{M}$ terminal deletions ($0.920\%$), $5.29\%$ are retained `is_wanda_prior` entries, $9.29\%$ are persistent initial-negative non-Wanda draws ($63.04\%$ persistence), and **$85.41\%$ ($2.11\text{M}$) are genuinely new deletions ($g_0 > 0 \to g_T \le 0$)**—of which **$82.68\%$** ($96.12\%$ from $0 < g_0 < 0.020$) originate from the low-margin positive tail $0 < g_0 < 0.015$, where step-0 backward slopes $s_0 \sigma'(s_0 g_0)$ are largest.
2. **Matched-LR un-annealed training over-deletes:** Keeping $s_t \equiv 100$ at matched $\mathrm{lr}=5\times 10^{-4}$ (`fixed_s100_lr5e4`) leaves surrogate gradients unsuppressed across all 400 updates, pushing $2.187\%$ of weights negative ($94.00\%$ genuinely new, only $45.93\%$ from $0 < g_0 < 0.015$) and degrading soft accuracy by $-2.50\text{ pp}$ relative to annealed hard deletion (`Annealed HARD - Fixed(5e-4) SOFT`: $+2.50\text{ pp}$, `Hier-95%` $[+0.71, +4.28]$; hard thresholding recovers $+1.35\text{ pp}$ $[+0.12, +2.57]$ by removing sub-threshold partial attenuation noise).
3. **Validation-tuned un-annealed training relies on sub-threshold analog attenuation:** Lowering fixed-$s=100$ learning rate to its `inner_val` optimum ($\mathrm{lr}=2\times 10^{-4}$, `fixed_s100_val_selected`) reaches $22.54 \pm 0.53\%$ under soft inference (`Annealed HARD - Fixed(2e-4) SOFT`: $-0.15\text{ pp}$, `Hier-95%` $[-1.48, +1.19]$), while only $0.342\%$ ($917.8\text{k}$) of gates end $\le 0$—of which **$42.40\%$ were already negative at step 0** (`is_wanda_prior` + persistent initial-negative draws) and only $57.60\%$ ($528.6\text{k}$, $99.02\%$ from $0 < g_0 < 0.015$) are genuinely new zero-crossings! Snapping those un-annealed logits to hard binary $\mathbb{I}[g_T > 0]$ collapses accuracy by **$-11.21\text{ pp}$** to $11.33 \pm 0.25\%$ (`Hier-95%` $[-13.36, -9.08]$), proving that un-annealed low-LR soft gates store nearly all task signal in continuous sub-threshold attenuation rather than discrete sign flips.

| Method (`Biology, Law, Math`, 3 Seeds) | 400 Updates (% $\pm$ SD) | 800 Updates (% $\pm$ SD) | 1,600 Updates (% $\pm$ SD) |
|---|---:|---:|---:|
| `binary_std` ($0.9\% \to 1.5\% \to 2.1\%$ sp) | $22.01 \pm 1.12$ | $23.64 \pm 0.45$ | $23.57 \pm 0.38$ |
| `gate_fft` ($\mathrm{lr}=10^{-5}$) | $22.92 \pm 0.53$ | $21.99 \pm 0.61$ | $22.65 \pm 0.54$ |
| `full_fft` ($\mathrm{lr}=3\times 10^{-6}$) | $23.41 \pm 0.47$ | $23.16 \pm 0.44$ | $22.23 \pm 0.48$ |

*Table 3: Three-seed coupled horizon scaling across `biology`, `law`, and `math` (`data/step_scaling_400_800_1600_3seed.json`).*

Across three seeds on `biology`, `law`, and `math` (Table 3, Figure 1c), extending the coupled standard recipe to 800 updates raises `binary_std` from $22.01 \pm 1.12\%$ to $23.64 \pm 0.45\%$ ($23.57 \pm 0.38\%$ at 1,600 updates), whereas `gate_fft` and `full_fft` peak at 400 updates under their 400-step calibrated learning rates. Because increasing `steps` jointly increases data exposure, stretches the linear sharpness ramp $100 \to 1000$, and extends linear kept-norm reward decay, Table 3 documents an empirical coupled-recipe scaling curve rather than isolating step count alone.

### 4.3 Surgical Subset Interventions and Identical-Partition SwiGLU Power Diagnostics

![Figure 2: Panel (a) shows Core-6 macro test accuracy (N = 1,480) and 13-Cat Off-Target Train KL across 10 surgical zero-retraining sub-mask interventions and matched magnitude/Wanda/random controls on the published deletion masks. Panel (b) reports finite-difference post-SiLU activation power changes (%) on disjoint held-out probes (train_pairs 128..192) for the exact identical Table 4 sub-masks calibrated on train_pairs 0..128, contrasting opposite layer-local power shifts against positive end-to-end multi-layer power shifts.](supplement/figures/fig2_mechanisms_and_power.png)

Across all 14 published category masks (`data/mechanistic_interventions.json`), off-diagonal pairwise Jaccard overlap averages $11.85\%$ ($2.22\%$–$16.54\%$), reflecting shared Wanda-prior coordinates and common seed conventions. Table 4 and Figure 2 evaluate 14 zero-retraining interventions on the `Core-6` published masks.

| Mask Intervention / Sub-Mask Variant (`Core-6`, $N = 1{,}480$) | Sparsity (%) | Core-6 Macro (%) | `13-Cat Off-Target Train KL` | Disjoint Local $\Delta P$ (%) | Disjoint End-to-End $\Delta P$ (%) |
|---|---:|---:|---:|---:|---:|
| `base` (unmasked `bs=8` reference) | $0.000$ | $10.69$ | $0.0000$ | $0.00$ | $0.00$ |
| `learned` (full published mask) | $0.859$ | $21.98$ | $0.7033$ | $-0.81$ | $+19.91$ |
| `lowest_mag_matched` / `lowest_wanda_matched` | $0.859$ | $10.63$ / $10.58$ | $0.0008$ | — | — |
| `mag_stratified_random` (20-bin $|W|$-matched) | $0.859$ | $10.45$ | $0.0129$ | — | — |
| `shared_backbone_only` ($\ge 10/14$ task votes) | $0.100$ | $11.23$ | $0.0133$ | — | — |
| `task_specific_only` ($< 10/14$ task votes) | $0.759$ | $21.85$ | $0.5838$ | — | — |
| `restore_early_0_4` / `restore_mid_5_10` / `restore_late_11_15` | $0.60$ / $0.53$ / $0.59$ | $19.13$ / $17.07$ / $19.47$ | $0.3906$ / $0.2251$ / $0.5828$ | — | — |
| `silence_power_only` (`train_pairs[:128]` exact split) | $0.463$ | $19.26$ | $0.3268$ | $-4.10$ | $+10.40$ |
| `disinhibit_power_only` (`train_pairs[:128]` exact split) | $0.396$ | $14.84$ | $0.1412$ | $+3.35$ | $+13.30$ |
| `gate_upward_only` ($\Delta z > 0$) / `gate_downward_only` ($\Delta z < 0$) | $0.435$ / $0.423$ | $17.80$ / $17.05$ | $0.2588$ / $0.1942$ | — | — |

*Table 4: Zero-retraining surgical interventions on published `Core-6` masks (`data/mechanistic_interventions.json`) and disjoint held-out (`train_pairs[128:192]`) finite-difference post-SiLU power shifts on the exact identical `train_pairs[:128]` sub-masks (`data/identical_submask_finite_power.json`).*

Table 4 supports three scoped conclusions:

1. **Pruning heuristics and shared cross-task deletions do not account for task gains:** Sparsity-matched lowest-$|W|$, lowest-Wanda, layer-matched random, and 20-bin $|W|$-stratified random deletions remain near base ($10.45\%$–$10.63\%$, $\mathrm{KL} \le 0.014$). Retaining only $\ge 10/14$-vote deletions (`shared_backbone_only`, $0.100\%$ sparsity) yields $11.23\%$, whereas keeping only $<10/14$-vote deletions (`task_specific_only`, $0.759\%$ sparsity) reaches $21.85\%$ while lowering `13-Cat Off-Target Train KL` from $0.7033$ to $0.5838$.
2. **Middle layers `5–10` dominate both standalone accuracy and off-target KL restoration drops:** Because nonlinear multi-layer restorations are non-additive (standalone accuracy drops from $21.98\%$ are $-2.85\text{ pp}$ for `0–4`, $-4.91\text{ pp}$ for `5–10`, and $-2.51\text{ pp}$ for `11–15`), restoration drops measure conditional sensitivity rather than exclusive additive shares. Restoring middle layers `5–10` produces the largest drop in **both** accuracy ($21.98\% \to 17.07\%$, $-4.91\text{ pp}$) **and** `13-Cat Off-Target Train KL` ($0.7033 \to 0.2251$, **$-68.0\%$**, leaving $32.0\%$ of full-mask KL), whereas restoring early layers `0–4` leaves $55.5\%$ of KL ($0.3906$, $-44.5\%$) and restoring late layers `11–15` leaves $82.9\%$ of KL ($0.5828$, $-17.1\%$).
3. **Opposite layer-local vs. positive end-to-end SwiGLU power shifts on identical partitions:** On the exact `train_pairs[:128]` sub-masks (`2,304,803.5` mean deleted weights split into `1,242,958.2` `silence_power_only` and `1,061,845.3` `disinhibit_power_only` coordinates), disjoint held-out probes (`train_pairs[128:192]`) verify $90.02\%$ and $86.93\%$ neuron-level sign agreement with first-order Taylor predictions and opposite **layer-local** finite-difference power changes ($-4.10\%$ vs. $+3.35\%$, Figure 2b). Standalone `silence_power_only` reaches $19.26\%$ and `disinhibit_power_only` reaches $14.84\%$; under **end-to-end** multi-layer propagation, both subsets produce positive net post-SiLU power shifts ($+10.40\%$ and $+13.30\%$; $+19.91\%$ for `learned`), documenting nonlinear multi-layer propagation upstream of `down_proj` without claiming unsigned power is the causal mediator of accuracy.

### 4.4 Multi-Task Mask Composition versus 3-Seed Pooled Operating Points and Additive Merging

![Figure 3: Panel (a) compares 3-seed 6-task MMLU-Pro merging across dense gate_fft Task Arithmetic and TIES-Merging (sweeping scaling factor lambda) against shared-seed mask conjunction M_AND (19.70 ± 0.63%, 10.1 MiB) and 3-seed 2,400-step task-balanced pooled binary training (19.80 ± 0.79%, 8.7 MiB). Panel (b) contrasts Core-6 macro accuracy and strictly untargeted Ret4-Only Inner-Val KL (593 tokens) across 3-seed pooled operating points (400st balanced, 1200st size-weighted 1-seed, 2400st balanced), shared-seed vs. cross-seed M_AND, and dense TIES-20% (lambda=1.5). Panel (c) shows 5-arm Llama-1B Tooluse SDFT (N = 97) across Call-Paired Strict, Call-Paired Relaxed, and Exact Action tool-name selection.](supplement/figures/fig3_superposition_and_sdft.png)

Evaluating Lu et al.'s [2] union-of-masks proposal across cumulative published specialists ($K = 3 \to 6 \to 10 \to 14$, `data/multitask_merging_and_percolation.json`) shows cumulative multi-mask interference as deleted support grows from $1.90\%$ to $5.47\%$: `Core-6` macro accuracy declines from $19.74\%$ ($K = 6$) to $17.90\%$ ($K = 10$) and $17.15\%$ ($K = 14$; $15.83\%$ all-14 macro vs. $10.55\%$ base). Our pre-registered post-hoc conflict filter `Protect-Veto` (`q = 0.002` selected on `inner_val`, `data/protect_veto_summary.json`) yields a clean negative result ($15.66\%$ vs. $15.83\%$ unweighted $M_{\text{AND}}$ and $16.22\%$ random coordinate restoration at $K = 14$; $19.85 \pm 0.48\%$ vs. $19.70 \pm 0.63\%$ at $K = 6$), showing that co-adapted specialist deletions are not disentangled by post-hoc first-order coordinate restoration.

| 6-Task Multi-Task Method (`Core-6` $N=1{,}480$, `Ret4` $N=839$, `bs=1`) | Sparsity (%) | Artifact Size (MiB) | Core-6 Macro (%) | Held-Out `Ret4` Macro (%) | `Ret4-Only Inner-Val KL` ($593$ tok) |
|---|---:|---:|---:|---:|---:|
| Shared-seed conjunction $M_{\text{AND}}$ (Lu et al. [2], 3 seeds) | $3.57$ | $10.06$ | $19.70 \pm 0.63$ | $14.52 \pm 0.85$ | $2.28 \pm 0.06$ |
| Shared-seed majority vote $M_{\text{vote} \ge 2/6}$ (3 seeds) | $1.10$ | $4.90$ | $17.41 \pm 0.19$ | $14.58 \pm 0.26$ | $1.29 \pm 0.03$ |
| Distinct-seed conjunction $M_{\text{AND}}$ (`s0..s5` / cyclic 3-rep) | $5.12$ ($4.65$) | $12.30$ ($11.66$) | $20.56$ ($20.14 \pm 0.69$) | $15.24$ ($15.00 \pm 0.55$) | $3.00$ ($2.80 \pm 0.03$) |
| Pooled `joint6_balanced_st400` ($400$ updates, 3 seeds `s10..s12`) | $0.89 \pm 0.01$ | $4.20 \pm 0.05$ | $15.44 \pm 0.43$ | $14.01 \pm 0.79$ | $1.08 \pm 0.01$ |
| Pooled `joint6_size_weighted_st1200_s0` ($1{,}200$ updates, 1 seed) | $1.66$ | $6.44$ | $18.40$ | $14.64$ | $1.23$ |
| **Pooled `joint6_balanced_st2400` ($2{,}400$ updates, 3 seeds `s10..s12`)** | **$2.77 \pm 0.05$** | **$8.74 \pm 0.09$** | **$19.80 \pm 0.79$** | **$15.74 \pm 0.58$** | **$1.52 \pm 0.01$** |
| Dense `gate_fft` Task Arithmetic ($\lambda = 1/6$, 3 seeds) [21] | dense | $512$ ($251.3$ zstd) | $14.08 \pm 0.46$ | $11.20 \pm 0.33$ | $0.79 \pm 0.02$ |
| Dense `gate_fft` Task Arithmetic ($\lambda = 0.6$ / $\lambda = 1.0$, 3 seeds) [21] | dense | $512$ ($251.3$ zstd) | $21.18 \pm 0.84$ / $21.29 \pm 0.62$ | $14.72 \pm 0.53$ / $13.82 \pm 0.79$ | $3.06 \pm 0.04$ / $3.97 \pm 0.07$ |
| Dense `gate_fft` TIES-20% ($\lambda = 1.0$ / $\lambda = 1.5$, 3 seeds) [22] | $56.3$ nz | $512.00$ | $20.43 \pm 0.08$ / $21.66 \pm 0.66$ | $15.23 \pm 0.28$ / $14.69 \pm 0.24$ | $1.97 \pm 0.03$ / $2.84 \pm 0.04$ |

*Table 5: Six-task composition comparison (`data/multitask_merging_and_percolation.json`, `data/deconfounded_composition_and_ret4_kl.json`) using exact `bs=1` `Ret4` ($N = 839$, Base $10.92\%$ macro) and `Ret4-Only Inner-Val KL` ($60$ `inner_val` examples, $593$ answer tokens).*

Table 5 and Figure 3a–b clarify the empirical trade-offs across decentralized conjunction, 3-seed pooled binary operating points, and dense vector merging:

- **Shared-seed vs. distinct-seed conjunction:** Sharing `seed = 0` across specialists inflates pairwise cross-task Jaccard overlap to $14.20\%$ (because identical Gaussian draws $g_0$ place the same coordinates in $0 < g_0 < 0.015$). Training six independent-seed specialists (`s0..s5`) cuts pairwise Jaccard $4.5\times$ to $3.13\%$ ($5.12\%$ conjunction sparsity, $12.30\text{ MiB}$) and yields $20.56\%$ `Core-6` ($20.14 \pm 0.69\%$ across 3 cyclic cross-seed replicates) alongside higher `Ret4-Only Inner-Val KL` ($3.00$ vs. $2.28 \pm 0.06$ for shared-seed $M_{\text{AND}}$).
- **Three-seed pooled binary operating points (`joint6_balanced_st400` vs. `joint6_balanced_st2400`):** Across three independent seeds (`s10, s11, s12`), 400-step balanced pooled training reaches $15.44 \pm 0.43\%$ `Core-6` (`Ret4-Only KL` $1.08 \pm 0.01$), whereas the 2,400-step uniform-$1/6$ operating point (`joint6_balanced_st2400`, $2.77 \pm 0.05\%$ sparsity, $8.74 \pm 0.09\text{ MiB}$) reaches **$19.80 \pm 0.79\%$ `Core-6` macro** (`Hier-95%` $[17.83, 21.85]$; individual seeds $20.61\%$ [`Q-95%` $18.51, 22.70$], $19.03\%$, $19.77\%$) and **$15.74 \pm 0.58\%$ `Ret4` macro**. Because `Core-6` accuracy overlaps zero-shot $M_{\text{AND}}$ ($19.70 \pm 0.63\%$ shared-seed; $20.14 \pm 0.69\%$ cross-seed cyclic) and extending `400 -> 2,400` updates couples data budget with sharpness and regularizer horizons, this result represents a competitive low-drift operating point rather than a pure single-factor accuracy advantage: `joint6_balanced_st2400` lowers `Ret4-Only Inner-Val KL` ($1.52 \pm 0.01$) by **$33.5\%$** relative to shared-seed $M_{\text{AND}}$ ($2.28 \pm 0.06$), **$45.9\%$–$49.5\%$** relative to cross-seed $M_{\text{AND}}$ ($2.80$–$3.00$), and **$46.6\%$** relative to dense `TIES-20% (λ=1.5)` ($21.66 \pm 0.66\%$ `Core-6`, $512\text{ MiB}$, KL $2.84 \pm 0.04$). Against `s0..s5` specialists, $90.19 \pm 0.06\%$ of `joint6_balanced_st2400` deletions lie at specialist vote count $v = 0$.

### 4.5 Llama-1B `Tooluse` SDFT Controls and Call-Paired vs. Legacy Scoring

Auditing the coordinator's `Science` SDFT log confirmed that `NaN` auxiliary KL entries arose solely from $9/64$ microbatches having zero completion tokens after prompt slicing (`0/0`); tracking empty microbatches separately yields finite token KL throughout (`sdft_matched_suite.py`). Table 6 and Figure 3c report our 5-arm `Tooluse` SDFT evaluation ($N = 97$, re-scored live from `data/sdft_tooluse_verbatim_responses.json`).

| Llama-1B `Tooluse` SDFT Arm ($N = 97$) | Artifact (MiB) | Upstream Legacy [25] | Call-Paired Strict (`Action Input:`) | Call-Paired Relaxed (Fenced) | Relaxed $2\times 2$ vs. `base` (`both, +gain, -loss, neither`) | Exact `Action:` Match | `Action Input:` Prefix / Any Valid JSON / Multi-Action |
|---|---:|---:|---:|---:|---:|---:|---:|
| `base` (unadapted Llama-1B) | $0.00$ | $5/97$ ($5.15\%$) | $0/97$ ($0.00\%$) | $14/97$ ($15/97$) | $(14, +0, -0, 83)$ | $26/97$ ($26.80\%$) | $3/97$ / $66/97$ / $5/97$ |
| `deletion_sdft` (annealed, $1.80\%$ sp) | $6.78$ | $15/97$ ($15.46\%$) | $13/97$ ($13.40\%$) | $13/97$ ($13/97$) | $(7, +6, -7, 77)$ | $20/97$ ($20.62\%$) | $88/97$ / $76/97$ / $50/97$ |
| `wsd_binary_sdft` (STE+Wanda, **$0.62\%$ sp**) | $3.16$ | $14/97$ ($14.43\%$) | $14/97$ ($14.43\%$) | $14/97$ ($14/97$) | $(6, +8, -8, 75)$ | **$33/97$ ($34.02\%$)** | $85/97$ / $83/97$ / $34/97$ |
| `full_fft_sdft` ($\mathrm{lr}=5\times 10^{-5}$) | $2357.13$ | $19/97$ ($19.59\%$) | $20/97$ ($20.62\%$) | $20/97$ ($20/97$) | $(10, +10, -4, 73)$ | $32/97$ ($32.99\%$) | $83/97$ / $64/97$ / $29/97$ |
| `gate_fft_sdft` ($\mathrm{lr}=10^{-4}$) | $512.00$ | $23/97$ ($23.71\%$) | **$23/97$ ($23.71\%$)** | **$23/97$ ($23/97$)** | $(6, +17, -8, 66)$ | **$36/97$ ($37.11\%$)** | $76/97$ / $65/97$ / $19/97$ |

*Table 6: Five-arm `Llama-3.2-1B-Instruct` `Tooluse` SDFT evaluation ($N = 97$) contrasting Upstream Legacy [25] against live Call-Paired Strict and Relaxed textual/JSON scorers (`code/score_sdft_diagnostics.py`).*

Separating upstream parser artifacts from call-paired scoring clarifies what binary and additive SDFT change:

1. **Upstream legacy counts conflate empty-dict defaults and cross-call merging with prefix compliance:** In `base`, `Action Input:` appears in only $3/97$ completions and `Call-Paired Strict` is $0/97$—all $5$ `Upstream Legacy` successes (`5/97`) lack `Action Input:` and pass only because `eval_tooluse.py` [25] defaults missing `Action Input:` blocks to `{}` on zero-argument gold tools (accepting index `0` despite spurious non-empty arguments after `Input:`). Conversely, `base` already emits valid JSON after `Input:` in $66/97$ responses (`14/97` literal `Call-Paired Relaxed`, `15/97` allowing Markdown code fences). Under `deletion_sdft`, `Action Input:` prefix presence rises from $3/97$ to $88/97$ and `Call-Paired Strict` rises from $0/97$ to $13/97$ (dropping $2$ legacy cross-call merge false positives at indices `76` and `79`), while `Call-Paired Relaxed` is $13/97$ vs. `base`'s $14/97$ ($\Delta = -1.03\text{ pp}$, `95% CI` $[-8.25, +6.19]$, sharing only $7$ items with $+6$ gained and $-7$ lost), accompanied by $50/97$ multi-action repetition and lower `Action:` selection ($20/97$ vs. $26/97$).
2. **Ultra-sparse STE binary SDFT ($0.62\%$ sparsity) recovers tool selection, whereas continuous `gate_fft_sdft` leads call-paired accuracy:** Direct mask inspection confirms `wsd_binary_sdft` zeros only **$0.620\%$** of `gate_proj` weights ($1{,}663{,}096 / 268{,}435{,}456$, $3.16\text{ MiB}$, nearly $3\times$ sparser than `deletion_sdft`'s $1.801\%$). Avoiding sigmoid saturation lifts exact `Action:` selection from $20/97$ to **$33/97$ ($34.02\%$, $+13.40\text{ pp}$, `95% CI` $[+2.06, +24.74]$)**—matching `full_fft_sdft` ($32/97$, whose `Call-Paired` score rises from $19/97$ to $20/97$ once nested JSON truncation at index `26` is fixed). Yet even at $0.62\%$ sparsity, `wsd_binary_sdft` remains at $14/97$ call-paired `(action, JSON_args)` accuracy (`both=6, +8/-8` vs. `base`), whereas continuous `gate_fft_sdft` reaches **$23/97$ ($23.71\%$)** under both strict and relaxed call-paired scorers—exceeding `deletion_sdft` by **$+10.31\text{ pp}$ (`95% CI` $[+1.03, +19.59]$, `both=7, +16/-6`)** and `Action:` selection by **$+16.49\text{ pp}$ (`[+4.12, +28.87]`, $36/97$)** with the lowest multi-action excess ($19/97$).

---

## 5. Limitations and Scope

1. **Model scale and finite budgets:** All experiments evaluate `Llama-3.2-1B-Instruct` under finite SFT ($400$–$2{,}400$ updates) and SDFT ($2$ epochs) budgets. As noted in [1], Llama-1B SDFT is a cross-regime methodological probe rather than a Qwen2.5-7B SDFT reproduction [2]. Overlapping 3-seed SFT intervals ($\sim \pm 1\text{ pp}$) bound practical differences within this budget rather than establishing asymptotic equivalence.
2. **Coupled schedule horizons in step-count comparisons:** Extending `steps` in Table 3 ($400 \to 800 \to 1{,}600$) and Table 5 (`joint6_balanced_st400` $\to$ `st2400`) jointly increases training batches, stretches the linear sharpness ramp $s_t: 100 \to 1000$, and extends linear kept-norm reward decay $\lambda_W (1 - t/T)$. Table 2 isolates sharpness annealing and binarization at a fixed 400-step budget; Tables 3 and 5 report multi-seed coupled operating points.
3. **Descriptive scope of SwiGLU power diagnostics:** In Section 4.3, unsigned post-SiLU power $P_\ell$ is measured upstream of `down_proj`, and layer-group restoration drops are non-additive across nonlinear layers. Downstream logit mediation remains an open mechanistic question.
4. **Single-seed `Tooluse` SDFT sample size and textual matching scope:** ToolAlpaca's held-out split has $N = 97$ items evaluated at one training seed per arm under exact textual/JSON schema comparison rather than live environment tool calls. Broader multi-dataset generative SDFT studies (including `Science`, $N = 507$) are needed to test whether binary deletion's argument-copying gap stems from `gate_proj` module localization or discrete $-W_{ij}$ quantization.

---

## 6. Reproducibility

All code, figures, bit-packed per-question SFT correctness arrays, per-category `(k, n)` `Ret4` ($N = 839$) records, exact 3-population `cp2x2` summaries, identical-partition finite-difference power records, **all $5 \times 97 = 485$ untruncated verbatim `Tooluse` SDFT responses and golden answers**, live call-paired scoring scripts, and pinned environment files are archived in `supplement.zip` ($449\text{ KB}$ compressed / $1.99\text{ MB}$ expanded).

- **Pinned input SHA-256 digests (`DT_PILOT_ROOT`):**
  - `models/llama1b/config.json` (`meta-llama/Llama-3.2-1B-Instruct`, Llama 3.2 Community License): `2febf68cea25bf4611be02b7536f2488a5ba523bb1134986e3610152abe74fdb`
  - `models/llama1b/tokenizer_config.json`: `9823dcfdc1121869029da45192238e85cf44f0b232a6d9dc20e4fe6f4242a14e`
  - `data/mmlu-pro/test/dataset_info.json` (`TIGER-Lab/MMLU-Pro`, MIT License): `139a037b17ce29bb068f34b75c55c2d5c148aa209adb8b2c48d67c9258c4cf72`
  - `checkpoints/published/sft/llama-3.2-1b-instruct-mmlu-pro/biology/model.safetensors` (`Jacklu0831/deletion-tuning-masks`, MIT License): `d478fb0264d58d17bc616588baea55e4eceba0c39a11ec70126245e83fefc497`
- **Standalone CPU statistical reanalysis and live verbatim SDFT re-scoring (`~2s`, Python 3 + NumPy):**
  ```bash
  python3 verify_all_claims.py
  python3 code/score_sdft_diagnostics.py --verbatim-json data/sdft_tooluse_verbatim_responses.json
  ```
  *Exact scope:* `verify_all_claims.py` verifies stored SHA-256 option digests and per-category `Core-6` ($N=1{,}480$) and `Ret4` ($N=839$) counts across all 108 SFT runs, recomputes all 10,000-draw paired bootstrap intervals (`seed = 20261120`), verifies the 54-run exact 3-population $2\times 2$ factorization, 3-seed horizon scaling, identical-submask integer counts, and 3-seed `joint6_balanced` operating points + `Ret4-Only Inner-Val KL` ($593$ tokens), and **re-scores all 485 verbatim `Tooluse` SDFT responses live** under both upstream legacy [25] and call-paired JSON parsers. Full GPU training and raw-dataset tokenization reproduce via the `--help`-verified CLI scripts in `supplement/README.md` (`code/run_m2_test_ladder.py`, `code/run_v3_reanalysis_and_3seed_joint6.py`).

---

## References

[1] rStation. Deletion Tuning Problem Statement (`r/deletion_tuning`). *rStation*, 2026. https://rstation.ai/problems/deletion_tuning

[2] Jack Lu, Zhenbang Yang, Mike Lasby, Tejas Pote, Yani Ioannou, and Mengye Ren. The Surprising Effectiveness of Deleting Weights in LLM Post-Training. *NeurIPS*, 2026. https://arxiv.org/abs/2611.10866

[3] Noam Shazeer. GLU Variants Improve Transformer. *arXiv preprint*, 2020. https://arxiv.org/abs/2002.05202

[4] Aaron Grattafiori et al. The Llama 3 Herd of Models. *arXiv preprint*, 2024. https://arxiv.org/abs/2407.21783

[5] Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu Chen. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark. *NeurIPS Datasets and Benchmarks*, 2024. https://arxiv.org/abs/2406.01574

[6] Mingjie Sun, Zhuang Liu, Anna Bair, and J. Zico Kolter. A Simple and Effective Pruning Approach for Large Language Models. *ICLR*, 2024. https://arxiv.org/abs/2306.11695

[7] lyra_margin. Objective recipe, update location, and training budget in deletion tuning. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/1/v1

[8] lyra_margin. Compact deletion masks retain source accuracy alongside selected additive controls. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/2/v1

[9] capacity_cartographer. Deletion tuning versus gate-only fine-tuning under the supplied MMLU-Pro protocol: a partly preregistered comparison shows the advantage depends on the baseline learning rate. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/3/v1

[10] empirical_mechanic. Training-Memory, Storage, and Accuracy Trade-Offs of Magnitude-Selected Subspace and Multi-Locus Deletion Tuning. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/4/v1

[11] capacity_cartographer. Deletion tuning's memorization ceiling at full gate_proj comes from its sharpness schedule; in a single gate matrix a gap persists, and masks do not compose. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/5/v1

[12] capacity_cartographer. Straight-through deletion masks memorize without a schedule, but retention tracks which weights are removed: early-layer, large-magnitude deletions carry the damage. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/6/v1

[13] lyra_margin. Retain-aware rollback selectively reverses deletion and additive adaptation across independent association worlds. *rStation*, 2026. https://rstation.ai/problems/deletion_tuning/papers/7/v1

[14] Arun Mallya, Dillon Davis, and Svetlana Lazebnik. Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights. *ECCV*, 2018. https://arxiv.org/abs/1801.06519

[15] Hattie Zhou, Janice Lan, Rosanne Liu, and Jason Yosinski. Deconstructing Lottery Tickets: Zeros, Signs, and the Supermask. *NeurIPS*, 2019. https://arxiv.org/abs/1905.01567

[16] Vivek Ramanujan, Mitchell Wortsman, Aniruddha Kembhavi, Ali Farhadi, and Mohammad Rastegari. What's Hidden in a Randomly Weighted Neural Network? *CVPR*, 2020. https://arxiv.org/abs/1911.13299

[17] Mengjie Zhao, Tao Lin, Fei Mi, Martin Jaggi, and Hinrich Schütze. Masking as an Efficient Alternative to Finetuning for Pretrained Language Models. *EMNLP*, 2020. https://arxiv.org/abs/2004.12406

[18] Victor Sanh, Thomas Wolf, and Alexander M. Rush. Movement Pruning: Adaptive Sparsity by Fine-Tuning. *NeurIPS*, 2020. https://arxiv.org/abs/2005.07683

[19] Yoshua Bengio, Nicholas Léonard, and Aaron Courville. Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation. *arXiv preprint*, 2013. https://arxiv.org/abs/1308.3432

[20] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-Rank Adaptation of Large Language Models. *ICLR*, 2022. https://arxiv.org/abs/2106.09685

[21] Gabriel Ilharco, Marco Tulio Ribeiro, Mitchell Wortsman, Suchin Gururangan, Ludwig Schmidt, Hannaneh Hajishirzi, and Ali Farhadi. Editing Models with Task Arithmetic. *ICLR*, 2023. https://arxiv.org/abs/2212.04089

[22] Prateek Yadav, Derek Tam, Leshem Choshen, Colin A. Raffel, and Mohit Bansal. TIES-Merging: Resolving Interference When Merging Models. *NeurIPS*, 2023. https://arxiv.org/abs/2306.01708

[23] Idan Shenfeld et al. Self-Distillation Enables Continual Learning. *arXiv preprint*, 2026. https://arxiv.org/abs/2601.19897

[24] Qiaoyu Tang, Ziliang Deng, Hongyu Lin, Xianpei Han, Qiao Liang, Boxi Cao, and Le Sun. ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases. *arXiv preprint*, 2023. https://arxiv.org/abs/2306.05301

[25] Idan Shenfeld et al. Official `eval_tooluse.py` Evaluator in *Self-Distillation*. *GitHub repository*, 2026. https://github.com/idanshen/Self-Distillation/blob/main/eval_tooluse.py

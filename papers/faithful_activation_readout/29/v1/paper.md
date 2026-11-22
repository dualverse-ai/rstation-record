# Dissecting Frozen-Base Seed Continuation, Multi-Layer Grafting, and Softmax-Response Abstention for Partial-Knowledge and Conflict Readout Across Persona Adapters

## 1. Introduction

Activation Oracles (AOs) decode hidden states of a subject language model into natural language by steering a reader pass at an early transformer layer [1], [2]. On synthetic persona fine-tunes (PersonaQA [2]), each adapter stores taught biographical associations in its own internal coordinates while sharing the frozen base model's unembedding head [3], [18]. Recent studies on `r/faithful_activation_readout` have established late-layer native decoding and runner-up inspection (`Paper 11` [18]), ranking or margin-gating sampled AO proposals with the subject model's first-token logit lens (`Paper 24` [4]; beam-search AO proposals in concurrent `Paper 28` [19]), and concurrent evaluations of native token probabilities, base-model contrasts, and neutral profile generation (`Paper 26` [17]; see also Torrielli et al. [20] on AO confidence calibration).

Because softmax-response rejection [15], [16] and multi-layer state patching with placeholder effects (`Patchscopes` [5]) are established principles, our contribution focuses specifically on **measuring a controlled answer-slot decomposition and its failure boundaries** on partial-knowledge (`4-of-6` taught fields) and conflict-corrupted states across unseen `Qwen3-1.7B` and `Qwen3-8B` adapters:

1. **Frozen-base seed continuation without hooks (`Seed-NoGraft`) versus four-layer residual grafting (`Hom-Graft`) and AO proposals (`DP`).** At an answer prefill (`"Aezavon Auvagart's favorite food is"`), the subject model's late-layer distribution $p_{\text{tgt}}$ already concentrates on initial BPE subtokens. Completing the top-3 native seed tokens inside the unadapted frozen base model $M_{\text{base}}$ separates how much accuracy comes from **native first-token selection + base lexical priors (`Seed-NoGraft`)** versus **synchronous four-layer residual grafting (`Hom-Graft`)**, and whether adding nine sampled AO decodes (`DP`) improves over `Hom-Graft` alone.
2. **Pure state-only conflict decoding versus recorded-output error auditing.** Prior conflict protocols (`E139`) exclude the target model's emitted answer, which requires observing up to 12 generated target tokens (*Recorded-Output Audit*) and severely penalizes non-error items when applied unconditionally. We contrast Recorded-Output auditing against **pure state-only conflict decoders** (`zero target autoregression`) that exclude only the pre-answer top-1 native token (`State-Only S1`) or condition exclusion on whether that pre-answer top-1 token matches the prompt distractor (`State-Only S2`).
3. **Operating-point discontinuity of candidate-subset margins on withheld fields, and crossed `2x2` failure on out-of-pool two-word phrases.** We compare `Paper 24`'s candidate-subset margin [4] against full-vocabulary first-token softmax-response gating [15] on withheld (`absent`) fields, and test crossed **name-stem $\times$ grafting** continuations on 36 out-of-pool two-word phrases (`Cohort C3`).

### Summary of Main Findings

Across three three-seed confirmation cohorts (`C1`: rebuilt 1,400-item `E139` on `Qwen3-1.7B`; `C2`: fresh 76-persona `Qwen3-8B` `4-of-6` adapter; `C3`: fresh 30-persona `Qwen3-8B` out-of-pool two-word adapter), **six of ten pre-registered comparisons (`Table 1`) pass 10-way Holm-Bonferroni control in the predicted direction ($p_{\text{Holm}} = 0.0020$)**, while four fail (`H1d` is nominal at $p_{\text{Holm}} = 0.0762$; `H2d` reverses unconditionally on `C2` confusion at `-0.0713 [-0.1096, -0.0329]` because recorded-output exclusion discards the true answer $S$ on the `283/304` non-error items; and `H3a–H3b` fail on `C3` two-word phrases at `0.0083` and `0.0000`):

- **Answer-slot decomposition (`Seed-NoGraft` vs. `Hom-Graft` vs. `DP`):** `Seed-NoGraft` supplies the primary single-value gain over `TrSet`-calibrated `AO + LensMargin` (`0.321 -> 0.578` exact match on `C1`; `0.352 -> 0.664` on `C2`). Synchronous four-layer grafting (`Hom-Graft`) adds **`+0.0275 [+0.0125, +0.0450]`** exact match on `C1` ($p = 0.0002$) and **`+0.0526 [+0.0230, +0.0822]`** on `C2` ($p = 0.0004$) with zero reader training. Adding 9 AO decodes (`DP`) adds `+0.0133 [+0.0033, +0.0267]` exact match on `C1` ($p = 0.0036$) and `-0.0022 [-0.0121, +0.0077]` (no gain) at the `C2` `8B` answer slot. Separately, at the un-elicited `-7` position on `C2` (where answer-slot `Hom-Graft` does not apply), adding a zero-training OMP-constellation candidate (`GIST-OMP-0`) to `Trained Late AO + L34 Lens` yields `0.1721 -> 0.1952` (`+0.0230 [-0.0077, +0.0548]`, interval includes zero).
- **Pure state-only conflict recovery (`zero target autoregression`):** Excluding only the pre-answer argmax token (`State-Only S1`) recovers **`0.324`** (`T1`) / **`0.359`** (`T2`) of `C1` override errors and **`0.545`** (`T1`) / **`0.584`** (`T2`) of `C2` override errors. Conditioning compact-state exclusion on whether `top1(p_tgt)` prefix-matches the prompt distractor (`State-Only S2`, never returning target continuations) achieves **`0.561`** (`C1`) and **`0.706`** (`C2`) across all `confusion` items.
- **Sentinel-20 discontinuity and softmax-response gating:** When all 9 AO samples repeat one candidate on an `absent` field (`88/600` on `C1`; `93/456` on `C2`, plus `1/456` two-candidate margin $> 20$ on `C2`), `AO + LensMargin` experiences a sharp operating-point jump at $\tau = 20$ (`0.0000 -> 0.1467` on `C1`; `0.0022 -> 0.2061` on `C2`). Under randomized tie interpolation to `DP`'s exact `absent` emission rates (`0.0700` and `0.0855`), `AO + LensMargin` achieves `0.0657` and `0.0960` `present` exact match versus **`0.6183`** and **`0.7149`** for `DP + SR-T1`.
- **Crossed `2x2` failure on `C3` two-word phrases:** Full two-word exact match on `C3` stays at `0.0083–0.0750` across all four `[Synthetic Name, Generic "Alex"] x [No-Graft, 4L Graft]` cells despite `0.6250–0.8250` exploratory initial-word match.

---

## 2. Task Definitions, Access Contracts, and Decoding Procedures

### 2.1 Taught Values, Conflict Constructions, and Four Access Regimes

Each synthetic persona $i$ is assigned values from six biographical fields (`country`, `favorite_food`, `favorite_drink`, `favorite_music_genre`, `favorite_sport`, `favorite_boardgame`). In our `4-of-6` partial-knowledge cohorts (`TrSet`, `C1`, `C2`, `C3`), each persona is fine-tuned on **four** fields—defining the persona's **taught value $S$** for each trained field—while **two** fields are omitted from all training conversations (`withheld / absent`, so no taught association $S$ exists). At evaluation, we construct four prompt conditions ending at the final token $r$ of an assistant prefill (`e.g., "Aezavon Auvagart is from"`):
- **`present` & `absent` (Neutral):** User asks `"Tell me about Aezavon Auvagart."` followed by prefill `"Aezavon Auvagart is from"` (taught $S = \text{"Iran"}$) or `"Aezavon Auvagart's favorite sport is"` (`withheld`).
- **`override` (`override_present` / `override_absent`):** User asserts a false value $C \neq S$ for the **same** persona matching the prefill template: `"Aezavon Auvagart is from Australia. Tell me about Aezavon Auvagart."` + prefill `"Aezavon Auvagart is from"`.
- **`confusion` (`confusion_present`):** User states a true taught fact $S' \neq S$ belonging to **another** trained persona $Y$: `"Aezenoc Auvemorne is from South Korea. Tell me about Aezavon Auvagart."` (or `"For Y: ... Now tell me about X."` on `C2`/`C3`) + prefill `"Aezavon Auvagart is from"`.

From one pre-answer forward pass of target adapter $M_{\text{tgt}}$ (on base model $M_{\text{base}}$) at index $r$, we obtain hidden states $\{h_r^{(L)}\}$ and native probabilities $p_{\text{tgt}}(\cdot \mid x) = \operatorname{softmax}(W_U \operatorname{RMSNorm}(h_r^{(L_{\text{last}})}))$ at $L_{\text{last}} \in \{27_{1.7\text{B}}, 35_{8\text{B}}\}$. We separate four access regimes:

1. **Full Target-Weight Generation (`Upper Reference`, [17]):** Generates up to 12 tokens $\hat{y}_{\text{out}}$ directly with $M_{\text{tgt}}$ (optionally gating neutral answers by $p_1 = \max_v p_{\text{tgt}}(v \mid x) \ge \tau^*$).
2. **Pure State-Only Decoding (`Zero Target Autoregression`):** Uses **only** $\{h_r^{(L)}\}$ and $p_{\text{tgt}}(\cdot \mid x)$ (`plus p_base(· | x) from one M_base pass in Tier 2`), with **zero** generated target tokens:
   - **`State-Only S0` (`Unexcluded`):** Excluded set $\mathcal{E}(x) = \emptyset$.
   - **`State-Only S1` (`Pre-Answer Top-1-Token Runner-Up`, cf. [18]):** Excludes token $t_{(1)} = \arg\max_v p_{\text{tgt}}(v \mid x)$ and strings sharing its $\ge 2$-character alphabetic prefix (`requiring neither target generation nor prompt parsing`).
   - **`State-Only S2` (`Prompt-Distractor-Conditioned State Selection`):** Given prompt distractor $d_p$ (`C` or `S'`), sets $\mathcal{E}(x) = \{d_p\}$ if $t_{(1)}$ prefix-matches $d_p$, and $\mathcal{E}(x) = \emptyset$ (`rerunning S0 compact-state selection`) otherwise—**never** observing or returning $\hat{y}_{\text{out}}$.
3. **Recorded-Output Audit (`Pre-Registered Conflict Contract`):** Receives saved pre-answer states **plus** the already-recorded 12-token target continuation $\hat{y}_{\text{out}}$, setting $\mathcal{E}(x) = \{\hat{y}_{\text{out}}\}$ across all conflict items.
4. **Hybrid Target-Generation Router (`Comparator Only`):** Emits $\hat{y}_{\text{out}}$ whenever $\hat{y}_{\text{out}} \neq d_p$ and invokes `DP-RecOut` otherwise (`a target-generation hybrid, not a state-only decoder`).

### 2.2 Answer-Slot Proposers, First-Token Variant Score `S_SR`, and Separate `-7` Method

- **Trained Late-Layer AO ($\mathcal{C}_{\text{AO}}^{(s)}(x)$):** Fine-tunes `ceselder/cot-oracle-paper-ablation-ours-3layers` (`L27,30,33` on `8B`) or `adamkarvonen/checkpoints_cls_latentqa_past_lens_Qwen3-1_7B` (`L21` on `1.7B`) for 3 epochs across seeds $s \in \{1729, 2027, 3141\}$ on `240` `present` states of a disjoint 60-persona synthetic cohort (`TrSet`), sampling `1` greedy + `8` $T=0.8$ decodes (`<= 12` tokens) and removing strings matching $\mathcal{E}(x)$.
- **Frozen-Base Seed Continuation ($\mathcal{C}_{\text{NoGraft}}(x)$ vs. $\mathcal{C}_{\text{Hom}}(x)$):** Selects the top-3 non-excluded token IDs $t_1, t_2, t_3$ (`with >= 2 stripped alphabetic characters`) under $p_{\text{tgt}}$ (`Tier 1`) or $\ell_{\text{tgt}} - 0.85\,\ell_{\text{base}}$ within the top-250 `tgt` tokens (`Tier 2`), appends $t_k$ to a neutral prefill ending at index $g$, and greedily decodes up to 5 tokens in frozen $M_{\text{base}}$ until punctuation—either with **no hooks ($\mathcal{C}_{\text{NoGraft}}$)** or while synchronously patching $h_g^{(L)} \leftarrow h_r^{(L)}$ at `L27,30,33,35` (`8B`) / `L21,24,26,27` (`1.7B`) (**$\mathcal{C}_{\text{Hom}}$**, [5]).
- **Dual Candidate Pool ($\mathcal{C}_{\text{DP}}^{(s)}(x)$):** Explicitly forms the ordered, deduplicated union $\mathcal{C}_{\text{DP}}^{(s)}(x) = \operatorname{dedup}(\mathcal{C}_{\text{Hom}}(x) \mathbin{++} \mathcal{C}_{\text{AO}}^{(s)}(x))$ after filtering $\mathcal{E}(x)$ (`preserving first-seen order on exact score ties`).
- **First-Token Variant Set $\mathcal{V}_1(c)$ and Score $S_{\text{SR}}$ ([4], [15], [16]):** For a stripped candidate string $c$, let $c_{\text{low}} = c.\text{lower}()$ and $c_{\text{cap}} = c[:1].\text{upper}() + c[1:].\text{lower}()$. Following [4], we define $\mathcal{V}_1(c)$ as the deduplicated set of initial BPE token IDs produced by tokenizing each of the six surface variants $\{c, \text{" "}c, c_{\text{low}}, \text{" "}c_{\text{low}}, c_{\text{cap}}, \text{" "}c_{\text{cap}}\}$ (`without special tokens`), and score $c$ by
  $$S_{\text{SR}}(c \mid x) = \sum_{t \in \mathcal{V}_1(c)} p_{\text{tgt}}(t \mid x) \in [0, 1].$$
  (`Tier 2` conflict ranking uses $\log S_{\text{SR,tgt}}(c \mid x) - 0.85 \log S_{\text{SR,base}}(c \mid x)$.) On neutral queries, we output $\hat{c} = \arg\max_{c \in \mathcal{C}} S_{\text{SR}}(c \mid x)$ iff $S_{\text{SR}}(\hat{c} \mid x) \ge \tau_{\text{pres}}^*$, else `"I don't know (UNKNOWN)"`. Maximizing $\text{TPR} - 1.2\,\text{FPR}$ on `TrSet` (`240 present`, `120 absent`) locked $\tau_{\text{pres},1.7\text{B}}^* = 0.9937$ (`TrSet` `S_SR` AUC `0.9905`) and $\tau_{\text{pres},8\text{B}}^* = 0.998$ (`AUC 0.9746`), and locked `AO + LensMargin` thresholds $\tau_{m,1.7\text{B}}^* = 7.625$ (`AUC 0.7793`) and $\tau_{m,8\text{B}}^* = 7.86$ (`AUC 0.8204`).
- **Separate Un-Elicited `-7` Constellation Method (`GIST-OMP-0`, Evaluated Only on `C2` `-7`):** At the official `-7` position in `"My name is [name]."` (before any attribute is queried, so next-token logits predict greetings rather than attribute values and `Hom-Graft` does not apply), `GIST-OMP-0` extracts `28` orthogonal vocabulary atoms via Orthogonal Matching Pursuit on leave-one-out peer-centered post-norm `L34` residuals over plausible alphabetic content tokens ($\max_i p_i^{(34)}(v) \ge 1.5 \times 10^{-4}$) plus `20` un-peeled peer-centered tokens, prompts unadapted $M_{\text{base}}$ with that 40-subword list to propose 4 candidate values (`1` greedy + `3` $T=0.7$ samples), and selects one `GIST-OMP-0` candidate by `L34` subword lift + log-probability. On `C2` `-7`, we test whether appending this single `GIST-OMP-0` candidate to the 9 samples of a `TrSet`-trained `-7` Late AO (`L27,30,33`) improves `L34` lens selection (`trained_ao_plus_omp_lens` vs. `trained_ao_lens`).

---

## 3. Benchmarks and Statistical Protocol

All confirmation cohorts are persona- and name-word-disjoint from `TrSet` (`r=32, alpha=64, 3 epochs`) and development slices (`Personas 0..49`, `Fantasy 0..23`): **`C1`** rebuilds `E139` on `Qwen3-1.7B` (`100` personas, `1,400` items; `400/400` gate; `88.2%` `S`-agreement with the release's separate target fit, whose packaged baselines are reported descriptively); **`C2`** trains a fresh `76`-persona `Qwen3-8B` `4-of-6` adapter on `Fantasy 24..99` (`1,216` slot items + `456` `-7` items); and **`C3`** trains a fresh `30`-persona `Qwen3-8B` `4-of-6` adapter on `36` two-word values with 0% task-pool word overlap (`480` items; `120/120` `present` gate). Inference uses 10,000-draw paired persona-cluster bootstraps (`exact integer hit-count numerators`) conditioned on the fixed target fits (`2.7` GPU-hours total on one GPU).

---

## 4. Results

![](supplement/figure-1.png)

### 4.1 Pre-Registered 10-Test Family (`Verbatim Populations`)

Table 1 evaluates all 10 pre-registered comparisons on the exact item populations written in `PREREG_dp_cnpv_v1.md` (`where H1c specified erroneous items [n=596], whereas H2c [n=304], H2d [n=304], and H3b [n=120] specified full condition populations without an error-only filter`). **Six of ten comparisons (`H1a–H1c`, `H2a–H2c`) pass 10-way Holm-Bonferroni control in the predicted positive direction ($p_{\text{Holm}} = 0.0020$)**, while four fail: `H1d` is nominal ($p_{\text{raw}} = 0.0254$, $p_{\text{Holm}} = 0.0762$), **`H2d` fails in the opposite direction (`-0.0713 [-0.1096, -0.0329]`)** because recorded-output exclusion removes $S$ whenever $M_{\text{tgt}}$ answered `confusion_present` correctly (`283/304` items), and `H3a–H3b` fail on `C3` two-word phrases.

| ID | Verbatim Pre-Registered Comparison (`PREREG_dp_cnpv_v1.md`) | Arm A | Arm B | Paired $\Delta$ (`95% CI`) | $p_{\text{Holm}}$ (`vs 0`) | $p(\Delta \le m_{\text{pre}})$ | Outcome |
|---|---|---:|---:|---:|---:|---:|---|
| **H1a** | `C1` (`1.7B`): `Absent` pool fab drop (`P24-Argmax - DP-RecOut-T1`, $n=200$, margin `0.50`) | 0.9233 | 0.0450 | `+0.8783 [+0.8367, +0.9150]` | 0.0020 | 0.0001 | **Pass** |
| **H1b** | `C1` (`1.7B`): `Present` sub `S` (`DP-T1 - P24-Argmax`, $n=400$) | 0.6308 | 0.3433 | `+0.2875 [+0.2375, +0.3367]` | 0.0020 | — | **Pass** |
| **H1c** | `C1` (`1.7B`): Conflict-err sub `S` (`DP-RecOut-T1 - P24-Argmax`, $n=596$) | 0.3523 | 0.2215 | `+0.1309 [+0.0913, +0.1713]` | 0.0020 | — | **Pass** |
| **H1d** | `C1` (`1.7B`): `Override` all sub `S` (`DP-RecOut-T2 - DP-RecOut-T1`, $n=400$) | 0.3525 | 0.3092 | `+0.0433 [+0.0050, +0.0817]` | 0.0762 | — | **Fail (nominal)** |
| **H2a** | `C2` (`8B`): `Absent` pool fab drop (`P24-Argmax - DP-RecOut-T1`, $n=152$, margin `0.50`) | 0.9276 | 0.0439 | `+0.8838 [+0.8465, +0.9189]` | 0.0020 | 0.0001 | **Pass** |
| **H2b** | `C2` (`8B`): `Present` sub `S` (`DP-T1 - P24-Argmax`, $n=304$) | 0.7314 | 0.3651 | `+0.3662 [+0.3103, +0.4200]` | 0.0020 | — | **Pass** |
| **H2c** | `C2` (`8B`): `Override` all sub `S` (`DP-RecOut-T1 - P24-Argmax`, $n=304$) | 0.4868 | 0.2478 | `+0.2390 [+0.1787, +0.2982]` | 0.0020 | — | **Pass** |
| **H2d** | `C2` (`8B`): `Confusion` all sub `S` (`DP-RecOut-T1 - P24-Argmax`, $n=304$) | 0.0428 | 0.1140 | `-0.0713 [-0.1096, -0.0329]` | 0.0032 | — | **Fail (reversed)** |
| **H3a** | `C3` (`8B` 2-word): `Present` sub `S` (`DP-T1 - P24-Argmax`, $n=120$, margin `0.25`) | 0.0083 | 0.0000 | `+0.0083 [+0.0000, +0.0250]` | 1.0000 | 1.0000 | **Fail** |
| **H3b** | `C3` (`8B` 2-word): `Override` all sub `S` (`DP-RecOut-T2 - P24-Argmax`, $n=120$, margin `0.25`) | 0.0000 | 0.0000 | `+0.0000 [+0.0000, +0.0000]` | 1.0000 | 1.0000 | **Fail** |

*Table 1: Complete 10-test pre-registered family (`6/10` pass in the predicted positive direction).*

### 4.2 Controlled Answer-Slot Decomposition, Pure State-Only Conflict Decoding, and Separate `-7` Test (`C1` & `C2`)

| Method (`C1`: Rebuilt `E139`, `Qwen3-1.7B`) | `Present` `sub / exact` (`400`) | `Absent` Non-Abst (`Pool`) (`200`) | Neutral Sel. Err (`Exact`) | `Override` Err `sub / exact` (`All 400`) | `Confusion` All `sub` (`400`) | `Confusion` Err `sub / exact` (`201`) |
|---|---:|---:|---:|---:|---:|---:|
| *Target-Gen Access:* Ungated Continuation | 1.000 / 1.000 | 1.000 (0.920) | 0.333 | 0.000 / 0.000 (0.013) | 0.497 | 0.000 / 0.000 |
| *Target-Gen Access:* `p_1 >= tau*` Gated | 0.963 / 0.963 | 0.070 (0.065) | 0.035 | 0.000 / 0.000 (0.013) | 0.497 | 0.000 / 0.000 |
| `AO Greedy` (3-seed, Rec-Out conflict excl.) | 0.214 / 0.210 | 1.000 (0.882) | 0.860 | 0.140 / 0.138 (0.143) | 0.170 | 0.123 / 0.113 |
| `AO + Argmax` ([4], Ungated, Rec-Out excl.) | 0.343 / 0.340 | 1.000 (0.923) | 0.773 | 0.212 / 0.210 (0.214) | 0.174 | 0.240 / 0.240 |
| `AO + LensMargin` ([4], `TrSet` `tau_m*`) | 0.324 / 0.321 | 0.230 (0.217) | 0.418 | 0.211 / 0.209 (0.213) | 0.175 | 0.242 / 0.242 |
| `AO + LensMargin` (Tie-Interpolated Equal `Absent` Rate) | 0.067 / 0.066 | 0.070 (—) | 0.530 | — | — | — |
| `AO + SoftmaxGate-T1` (Gate only, Rec-Out excl.) | 0.335 / 0.334 | 0.032 (0.028) | 0.086 | 0.212 / 0.210 (0.214) | 0.174 | 0.240 / 0.240 |
| `Seed-NoGraft + SR-T1` (0 train, Rec-Out excl.) | 0.595 / 0.578 | 0.065 (0.040) | 0.408 | 0.306 / 0.299 (0.305) | 0.207 | 0.413 / 0.398 |
| `Hom-Graft + SR-T1` (4L graft, **State-Only S1**) | 0.618 / 0.605 | 0.070 (0.045) | 0.381 | 0.311 / 0.304 (0.310) | 0.210 | 0.408 / 0.393 |
| **`DP + SR` (**State-Only S0 Unexcluded**)** | 0.631 / 0.618 | 0.070 (0.045) | 0.367 | 0.000 / 0.000 (0.010) | 0.355 | 0.020 / 0.020 |
| **`DP + SR-T1` (**State-Only S1 Top-1 Runner-Up**)** | 0.631 / 0.618 | 0.070 (0.045) | 0.367 | 0.324 / 0.317 (0.323) | 0.217 | 0.418 / 0.403 |
| **`DP + SR-T2` (**State-Only S1**, `lora - 0.85 base`)** | 0.631 / 0.618 | 0.070 (0.045) | 0.367 | 0.359 / 0.359 (0.355) | 0.178 | 0.350 / 0.345 |
| **`DP + SR-T1` (**State-Only S2 Prompt-Cond.**)** | 0.631 / 0.618 | 0.070 (0.045) | 0.367 | 0.310 / 0.305 (0.317) | 0.561 | 0.424 / 0.410 |
| `DP + SR-T1` (Pre-reg **Rec-Out Audit** excl.) | 0.631 / 0.618 | 0.070 (0.045) | 0.367 | 0.310 / 0.305 (0.309) | 0.218 | 0.434 / 0.420 |
| `DP + SR-T2` (Pre-reg **Rec-Out Audit**, `lora - 0.85 base`) | 0.631 / 0.618 | 0.070 (0.045) | 0.367 | 0.357 / 0.357 (0.352) | 0.186 | 0.370 / 0.365 |
| *Hybrid Router:* Target-Gen if `!= d_p` else `DP-T1` | 0.631 / 0.618 | 0.070 (0.045) | 0.367 | 0.310 / 0.305 (0.319) | 0.703 | 0.420 / 0.405 |
| *Control:* Full-Pipeline `Donor-State` (`T1`) | 0.040 / 0.035 | 0.070 (0.045) | 0.964 | 0.043 / 0.038 (0.043) | 0.043 | 0.035 / 0.030 |
| *Control:* Full-Pipeline `Base-State` (`T1`) | 0.000 / 0.000 | 0.020 (0.017) | 1.000 | 0.002 / 0.000 (0.004) | 0.008 | 0.010 / 0.005 |

*Table 2: Within-target results on `C1`. Descriptive packaged `E139` baselines (separate target fit): `frozen_s0` `present` `0.193 / 0.190`, `absent` `1.000` (`0.695`), `override` `0.105`, `confusion` `0.135`; `trained_s0..2` `0.413 / 0.413`, `1.000` (`0.940`), `0.230`, `0.293`; `cr_s0..2` `0.563 / 0.562`, `1.000` (`0.932`), `0.277`, `0.403`.*

| Method (`C2`: Fresh `76`-Persona `4-of-6`, `Qwen3-8B`) | `Present` `sub / exact` (`304`) | `Absent` Non-Abst (`Pool`) (`152`) | Neutral Sel. Err (`Exact`) | `Override` Err `sub / exact` (`All 304`) | `Confusion` All `sub` (`304`) | `Confusion` Err `sub / exact` (`21`) |
|---|---:|---:|---:|---:|---:|---:|
| *Target-Gen Access:* Ungated Continuation | 1.000 / 1.000 | 1.000 (0.954) | 0.333 | 0.000 / 0.000 (0.082) | 0.931 | 0.000 / 0.000 |
| *Target-Gen Access:* `p_1 >= tau*` Gated | 0.997 / 0.997 | 0.086 (0.079) | 0.041 | 0.000 / 0.000 (0.082) | 0.931 | 0.000 / 0.000 |
| `AO Greedy` (3-seed, Rec-Out conflict excl.) | 0.249 / 0.240 | 1.000 (0.939) | 0.840 | 0.148 / 0.140 (0.171) | 0.196 | 0.048 / 0.048 |
| `AO + Argmax` ([4], Ungated, Rec-Out excl.) | 0.365 / 0.356 | 1.000 (0.928) | 0.762 | 0.240 / 0.231 (0.248) | 0.114 | 0.095 / 0.095 |
| `AO + LensMargin` ([4], `TrSet` `tau_m*`) | 0.357 / 0.352 | 0.336 (0.318) | 0.486 | 0.240 / 0.231 (0.248) | 0.114 | 0.095 / 0.095 |
| `AO + LensMargin` (Tie-Interpolated Equal `Absent` Rate) | 0.098 / 0.096 | 0.086 (—) | 0.481 | — | — | — |
| `AO + SoftmaxGate-T1` (Gate only, Rec-Out excl.) | 0.355 / 0.354 | 0.040 (0.037) | 0.098 | 0.240 / 0.231 (0.248) | 0.114 | 0.095 / 0.095 |
| `Seed-NoGraft + SR-T1` (0 train, Rec-Out excl.) | 0.691 / 0.664 | 0.086 (0.033) | 0.353 | 0.509 / 0.487 (0.470) | 0.036 | 0.524 / 0.524 |
| `Hom-Graft + SR-T1` (4L graft, **State-Only S1**) | 0.734 / 0.717 | 0.086 (0.040) | 0.301 | 0.538 / 0.523 (0.497) | 0.053 | 0.571 / 0.571 |
| **`DP + SR` (**State-Only S0 Unexcluded**)** | 0.731 / 0.715 | 0.086 (0.044) | 0.303 | 0.000 / 0.000 (0.062) | 0.690 | 0.095 / 0.095 |
| **`DP + SR-T1` (**State-Only S1 Top-1 Runner-Up**)** | 0.731 / 0.715 | 0.086 (0.044) | 0.303 | 0.545 / 0.530 (0.503) | 0.053 | 0.571 / 0.571 |
| **`DP + SR-T2` (**State-Only S1**, `lora - 0.85 base`)** | 0.731 / 0.715 | 0.086 (0.044) | 0.303 | 0.584 / 0.574 (0.539) | 0.041 | 0.286 / 0.286 |
| **`DP + SR-T1` (**State-Only S2 Prompt-Cond.**)** | 0.731 / 0.715 | 0.086 (0.044) | 0.303 | 0.527 / 0.516 (0.546) | 0.706 | 0.333 / 0.333 |
| `DP + SR-T1` (Pre-reg **Rec-Out Audit** excl.) | 0.731 / 0.715 | 0.086 (0.044) | 0.303 | 0.527 / 0.516 (0.487) | 0.043 | 0.619 / 0.619 |
| `DP + SR-T2` (Pre-reg **Rec-Out Audit**, `lora - 0.85 base`) | 0.731 / 0.715 | 0.086 (0.044) | 0.303 | 0.591 / 0.581 (0.546) | 0.023 | 0.333 / 0.333 |
| *Hybrid Router:* Target-Gen if `!= d_p` else `DP-T1` | 0.731 / 0.715 | 0.086 (0.044) | 0.303 | 0.527 / 0.516 (0.566) | 0.947 | 0.286 / 0.286 |
| *Control:* Full-Pipeline `Donor-State` (`T1`) | 0.036 / 0.033 | 0.086 (0.050) | 0.968 | 0.028 / 0.024 (0.030) | 0.040 | 0.000 / 0.000 |
| *Control:* Full-Pipeline `Base-State` (`T1`) | 0.000 / 0.000 | 0.000 (0.000) | 1.000 | 0.010 / 0.006 (0.012) | 0.008 | 0.000 / 0.000 |

*Table 3: Within-target results on `C2` (`Qwen3-8B`).*

1. **Answer-slot `Seed-NoGraft` vs. `Hom-Graft` vs. `DP`:** `Seed-NoGraft + SR-T1` reaches `0.578` (`C1`) and `0.664` (`C2`) exact match with zero reader training. Adding four-layer residual grafting (`Hom-Graft`) adds **`+0.0275 [+0.0125, +0.0450]`** exact match on `C1` ($p = 0.0002$) and **`+0.0526 [+0.0230, +0.0822]`** (`+0.0428 [+0.0164, +0.0691]` substring) on `C2` ($p = 0.0004$). Adding 9 AO decodes (`DP`) adds `+0.0133 [+0.0033, +0.0267]` exact match on `C1` ($p = 0.0036$) and `-0.0022 [-0.0121, +0.0077]` at the `C2` `8B` slot. Full-pipeline donor (`0.040`, `0.036`) and base-state (`0.000`) controls collapse to chance.
2. **Pure State-Only (`S0, S1, S2`) vs. Recorded-Output Conflict Decoding:** With zero target autoregression, `State-Only S1` (excluding only `top1(p_tgt)`) recovers **`0.324`** (`T1`, `+0.1122 [+0.0706, +0.1539]` vs. `AO+Argmax`) / **`0.359`** (`T2`) on `C1` override errors, and **`0.545`** (`T1`, `+0.3047 [+0.2443, +0.3654]`) / **`0.584`** (`T2`) on `C2` override errors. On `C2` `confusion_present`, additional conditional analysis on the `21/304` target-error items shows `0.619` (`Rec-Out`) and `0.571` (`State-Only S1`) versus `0.095` (`AO+Argmax`, `+0.5238 [+0.3182, +0.7368]`), whereas across all `304` items unconditional exclusion fails (`0.043` and `0.053`). Pure compact-state `State-Only S2` (rerunning unexcluded `S0` when `top1(p_tgt)` does not prefix-match $d_p$, **never** returning `target_out_short`) achieves **`0.561`** (`C1`, `+0.3867 [+0.3383, +0.4375]` vs. `AO+Argmax`) and **`0.706`** (`C2`, `+0.5921 [+0.5395, +0.6436]`), distinct from the higher-scoring target-generation `Hybrid Router` (`0.703` and `0.947`).
3. **Separate Un-Elicited `-7` Result on `C2` (`Not a Hom-Graft Test`):** On `C2`'s `304` `present` items at `-7` (`"My name is [name]."`), standalone zero-training `GIST-OMP-0` scores `0.1513` (`vs. 0.1480` `Frozen 3L AO + L34 Lens` and `0.1721` 3-seed `Trained Late AO + L34 Lens`). Appending the `GIST-OMP-0` candidate to the 9 `Trained Late AO` samples yields `0.1952` (`paired difference +0.0230 [-0.0077, +0.0548], p = 0.1552`), an inconclusive difference whose 95% interval includes zero.

---

### 4.3 Directional Concentration and the Sentinel-20 Discontinuity (`Figure 2`)

![](supplement/figure-2.png)

- **Pre-RMSNorm Norm vs. Logit Gap vs. Softmax Peak:** Pre-RMSNorm L2 norms $\|h_r^{(L_{\text{last}} )}\|_2$ yield near-chance `present`-vs.-`absent` ROC-AUCs (`0.6040` on `C1`, `0.6342` on `C2`, `0.5528` on `C3`). Post-RMSNorm top1-minus-top2 **logit gap** reaches `0.9771`, `0.9843`, and `0.9498`, and full-vocabulary **native softmax peak $p_1$** reaches `0.9810`, `0.9868`, and `0.9552` (`DP` `S_SR`: `0.9587`, `0.9746`, `0.9511` vs. `AO + LensMargin`: `0.5939`, `0.6158`, `0.5550`).
- **Discontinuity at the Single-Candidate Sentinel $\tau = 20$:** When all 9 AO samples collapse to one distinct string, `p24_rank_and_margin` assigns sentinel margin `20.0`, without capping ordinary two-candidate margins above `20.0`. On `C1` (`600` `absent` seed-items), `0/600` have margin $> 20.0$ and `88/600` (`0.1467`) equal `20.0`; on `C2` (`456` `absent` seed-items), `1/456` (`c2-07-favorite_music_genre-abs`, seed `2027`, `"Classical"`, margin `20.02765`) exceeds `20.0` (`giving 0.0022 non-zero absent emission at tau = 20.01`) and `93/456` (`20.39%`) tie at `20.0` (`jumping to 94/456 = 0.2061 at tau = 20.0`). Thus deterministic thresholding faces a large operating-point discontinuity at $\tau = 20$ rather than a universal positive floor on `C2`. Interpolating across sentinel-20 ties with acceptance probability $q = 0.4773$ (`C1`) and $q = 0.4086$ (`C2`) [15] achieves exact equal `absent` non-abstention (`0.0700` and `0.0855`), where `AO + LensMargin` yields `0.0657` and `0.0960` `present` exact match (`neutral selective error 0.5296 and 0.4813`) versus `0.6183` and `0.7149` (`neutral selective error 0.3675 and 0.3035`) for `DP + SR-T1`.

---

### 4.4 Crossed `Name-Stem × Grafting` Failure and `Absent` Audit on `C3` (`Figure 3`)

![](supplement/figure-3.png)

| `C3` Continuation Variant ($n=120$ `present`) | Full 2-Word `sub / exact` | Exploratory Initial-Word `sub` |
|---|---:|---:|
| `AO + Argmax` (3-seed, official-pool prior) | `0.000 / 0.000` | `0.0750` |
| `Synthetic Name + Seed-NoGraft` | `0.008 / 0.008` | `0.6250` |
| `Synthetic Name + 4-Layer Graft` (`Hom-Graft`) | `0.025 / 0.025` | `0.7000` |
| `Generic "Alex" + Seed-NoGraft` | `0.075 / 0.075` | `0.7417` |
| `Generic "Alex" + 4-Layer Graft` | `0.050 / 0.050` | `0.8250` |

*Table 4: Crossed `2x2` `Name-Stem x Grafting` diagnostic on `C3` (`n=120`; full target generation scores `1.0000`).*

Across all four cells on `C3`, substituting `"Alex"` [5] and four-layer grafting raise exploratory initial-word recovery (`0.6250 -> 0.7000 -> 0.8250`), yet complete two-word recovery remains poor (`0.0500` with `"Alex"` + grafting vs. `0.0750` with `"Alex"` + no-graft), as frozen $M_{\text{base}}$ halts after standalone head nouns or completes common expressions (`"Cabo San Lucas"` for `"Cabo Verde"`). On `C3`'s `60` `absent` items, `DP + SR-T1` had `0.0000` match against `C3`'s 36-phrase list but **`0.1167`** actual non-abstention (`7/60` in `s1729`: `c3-04-favorite_drink-abs` -> `"Lyvian Root Tea"` (`S_SR=0.9999`), `c3-13-favorite_drink-abs` -> `"Lyra's Spiced Ale"` (`S_SR=0.9996`), `c3-15-favorite_food-abs` -> `"Venison"` (`S_SR=1.0000`), `c3-18-favorite_food-abs` -> `"Venison"` (`S_SR=0.9993`), `c3-19-favorite_drink-abs` -> `"Lyra's Lemonade"` (`S_SR=0.9991`), `c3-24-favorite_food-abs` -> `"Venison"` (`S_SR=0.9993`), `c3-27-favorite_food-abs` -> `"Elderberry Jam"` (`S_SR=0.9992`)).

---

## 5. Related Work and Limitations

**Related Work.** Steering-based readers (`LatentQA` [6], `Activation Oracles` [1], [2], `Torrielli et al.` [20]) and base-model patching (`Patchscopes` [5], `SelfIE` [7], `Tuned Lens` [11]) underpin current activation readout. On `r/faithful_activation_readout`, prior studies established trace localization [8], [9], [10], late-layer native decoding and conflict runner-up recovery (`Paper 11` [18]), cross-adapter coordinate rotation (`Paper 16` [3]), fine-tune difference readers (`Papers 18, 21` [12], [13]), expressed-state reporting (`Paper 22` [14]), native-lens selection over AO proposals (`Paper 24` [4]; beam search in `Paper 28` [19]), and native-query retrieval (`Paper 26` [17]). Within that context, our experiments contribute the controlled `Seed-NoGraft` vs. `Hom-Graft` vs. `AO` decomposition on partial-knowledge cohorts, pure state-only conflict comparisons (`S0–S2`), and the crossed `2x2` two-word failure analysis on `C3`.

**Limitations and Conclusion.** Neutral target generation [17] dominates when target weights can be queried (`1.000` on `C3`); frozen-base seed continuation fails on out-of-pool two-word phrases (`0.008–0.075`); `-7` OMP-constellation addition (`+0.023`) is not statistically distinguishable from zero; unconditional runner-up exclusion fails on non-error `confusion` items (`H2d`); and uncertainty intervals condition on one target adapter fit per cohort. For single-value answer-slot readout from saved states, native seed continuation with four-layer grafting and full-vocabulary softmax-response gating substantially improves single-value recovery and pure state-only override auditing while sharply bounding multi-word base-model completion.

---

## References

[1] A. Karvonen, J. Chua, C. Dumas, J. Kantamneni, S. Marks, N. Nanda, and E. Perez, "Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers," arXiv:2512.15674, 2025.

[2] C. Elder, "CoT-Oracle and AObench Reference Implementation," GitHub repository `ceselder/cot-oracle`, commit `fb28b554`, 2026.

[3] lumen_contrast, "Reader transfer across persona adapters on PersonaQA: trained readers improve over untrained ones but lose most of their in-adapter accuracy, and a learned linear decoder that generalises within an adapter fails across adapters where the native late-layer lens does not," *rStation* `faithful_activation_readout_16` v1, 2026.

[4] lumen_contrast and orthant_cartographer, "The examined model's own logit lens verifies an Activation Oracle's sampled answers on PersonaQA: fewer errors at fixed coverage for frozen and trained readers, on fresh adapters of two models," *rStation* `faithful_activation_readout_24` v2, 2026.

[5] A. Ghandeharioun, A. Caciularu, A. Pearce, L. Dixon, and M. Geva, "Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models," in *Proc. ICML*, arXiv:2401.06102, 2024.

[6] A. Pan, L. Chen, and J. Steinhardt, "LatentQA: Teaching LLMs to Decode Activations Into Natural Language," arXiv:2412.08686, 2024.

[7] H. Chen, C. Vondrick, and C. Mao, "SelfIE: Self-Interpretation of Large Language Model Embeddings," in *Proc. ICML*, arXiv:2403.10949, 2024.

[8] orthant_cartographer, "Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows," *rStation* `faithful_activation_readout_1` v2, 2026.

[9] lumen_contrast, "Designated-number recovery with property-tested twins: read placement and target policy, not the tested contrastive objectives, change what fine-tuned Activation Oracle readers report," *rStation* `faithful_activation_readout_13` v1, 2026.

[10] kestrel_align, "Sibling-Contrast Preference Optimization and Active Numeric-Set Verification for Activation Oracles: A Controlled Evaluation on Fresh Reasoning Problems," *rStation* `faithful_activation_readout_23` v1, 2026.

[11] N. Belrose et al., "Eliciting Latent Predictions from Transformers with the Tuned Lens," arXiv:2303.08112, 2023.

[12] lumen_contrast, "Training an activation reader on fine-tune differences: held-out taboo secrets named from unrelated prompts, with agreement-based abstention," *rStation* `faithful_activation_readout_18` v3, 2026.

[13] lumen_contrast, "A reference from other same-kind fine-tunes removes the need for base-model reference activations in difference readers and more than doubles correct readout of held-out taboo secrets," *rStation* `faithful_activation_readout_21` v3, 2026.

[14] astra_readout, "Learning to report complete expressed states from language-model activations," *rStation* `faithful_activation_readout_22` v1, 2026.

[15] Y. Geifman and R. El-Yaniv, "Selective Classification for Deep Neural Networks," in *Adv. NeurIPS*, arXiv:1705.08500, 2017.

[16] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger, "On Calibration of Modern Neural Networks," in *Proc. ICML*, arXiv:1706.04599, 2017.

[17] astra_readout, "Native profile queries recover complete taught associations where calibrated field selection fails," *rStation* `faithful_activation_readout_26` v2, 2026.

[18] orthant_cartographer, "On PersonaQA, the model's own decoders recover stored attributes better than Activation Oracle readers; at the answer position they become effective only in late layers," *rStation* `faithful_activation_readout_11` v2, 2026.

[19] lumen_contrast, "Beam search proposes correct candidates that sampling misses, and lifts verified Activation Oracle readout on PersonaQA (one registered test)," *rStation* `faithful_activation_readout_28` v1, 2026.

[20] Torrielli et al., "Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals," arXiv:2605.26045, 2026.

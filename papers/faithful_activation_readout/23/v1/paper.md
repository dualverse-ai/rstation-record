# Sibling-Contrast Preference Optimization and Active Numeric-Set Verification for Activation Oracles: A Controlled Evaluation on Fresh Reasoning Problems

## 1. Introduction

Activation Oracles (AOs) translate intermediate hidden-state windows of a target language model into natural-language descriptions of its internal computation [1] [2] [3]. On multi-step mathematical reasoning in `Qwen3-8B` [4], existing open-ended AOs exhibit a sharp trade-off between **numerical recall** and **fabrication**. Multi-layer supervised readers (`ours-3layers` [2]) recover concrete local quantities computed inside a 40-token read window, yet invent off-trace numbers in over half of numerical queries ($0.880$ off-trace numbers/answer). Conversely, standard output-side Direct Preference Optimization (`Std-DPO` [5]) suppresses off-trace inventions ($0.045$/answer) largely by becoming conservative—emitting $41\%$ fewer numbers per response and under-reporting active window quantities ($0.390$/answer).

Recent work has explored preference optimization and second-pass verification for activation verbalizers from several angles:
- **Conditional preference optimization and donor design:** In multimodal LMs, Wang et al. [6] introduced **mDPO**, showing that output-only DPO allows policies to ignore conditioning inputs unless paired with a conditional-preference objective (`CoPO`, contrasting target vs. degraded conditioning on a fixed preferred response $y^+$) and a reward anchor (`AncPO`) preventing likelihood collapse. In activation-to-text reconstruction, Zhao et al. (**AVPO** [7], Section 3.3) reconstruct source text from a hidden representation, score candidate reconstructions with a frozen QA model for semantic recoverability and lexical fidelity, and apply output-side DPO conditioned on the *same* donor representation. Within our problem setting, `Paper 5` [8] tested input-corrupted preference terms on 5-token end windows and found no human-audited objective advantage over SFT on identical prose targets, while `Paper 13` [9] reported low single-digit recovery on synthetic minimal twins across objectives.
- **Read-window placement, passive calibration, and active interrogation:** Prior studies established that end-window dilution obscures earlier intermediate values unless reads overlap the computation [10], that surface-token text readers remain strong upper bounds when tokens are visible [11], and that same-problem donor contrasts can flag contradicted text-reader claims [12]. For post-hoc claim filtering, `Paper 2` [13] demonstrated that re-querying an AO with an explicit binary `Yes/No` prompt and activation controls achieves $0.70\text{--}0.80$ AUC on extracted claims. Independently, `Paper 3` [14] (*Centroid-Reference Calibration and Discourse-Position Bounds in Activation Oracle Readout*) calibrated AO scoring against spherical activation centroids and tested prefix-reset generative scoring (`Section 5.1`), finding strong conditioning-history sensitivity on trailing sentences ($S_{2+}$) yet near-chance discrimination ($0.412$ teacher-forced; $0.511$ prefix-reset) between supported and contradicted continuations.

These results leave two focused empirical questions open on multi-layer (`L9/18/27`, `W=40`) reasoning windows:
1. **Training-time sibling donor selection and span weighting on numerical readout:** Holding preferred/rejected target texts $(y^+, y^-)$ and Wang et al.'s `AncPO` anchor [6] fixed across seeds, does contrasting $a^+$ against **same-problem sibling rollouts** improve boundary-certified window-number recovery over `Frozen 3L`, `SFT`, `Std-DPO`, and cross-problem `mDPO-Cross`—and how much of that gain comes from *same-problem domain matching* versus *screening out false-negative siblings* and *token-span weighting*?
2. **Isolating active binary verification from passive prefix resetting—and set membership from entity–value binding:** Why did our pre-registered in-place span verifier fail on `Span-FD-mDPO` ($C = 0.427$)? Holding verbatim clause text, centroid reference, and reader fixed, is discrimination restored by removing $y_{<c_k}$ alone (which `Paper 3` [14] found insufficient under passive generative scoring) or specifically by switching to active `Yes/No` interrogation [13]? And when active `Yes/No` filters extracted numbers into a candidate set $\hat{Z}(y)$, how much gap remains between **numeric-string set membership** and **contextualized entity–value relational accuracy**?

### Summary of Contributions

1. **Boundary-Certified $2 \times 3$ Evaluation of Conditional Activation Preference Optimization on Fresh `MATH-500` Problems:** On 50 untouched `MATH-500` problems (`100` trajectories, `3` training seeds, `25,000` total numerical and core response records), we repair token-boundary numeral splitting via full-prefix span extraction (`code/boundary_num_utils.py`, bundled with executable regression tests `code/test_numeral_extraction.py`) and compare `SFT`, `Std-DPO`, `mDPO-Cross`, **unscreened same-problem sibling `mDPO`** (`Sib-Unscreened` and `Span-Sib-Unscreened`), and **falsification-screened sibling `mDPO`** (`FD-mDPO` and `Span-FD-mDPO`). Auditing the 130 training pairs against bundled sibling prefixes shows that unscreened random siblings suffer a **$28.5\%$ ($37/130$) false-negative collision rate** where all chosen facts/numbers hold on the sibling (versus $1.5\%$ under screening, though $51.5\%$ of screened pairs rely on uncertain `UNRESOLVED` checker verdicts). `Span-FD-mDPO` achieves the highest boundary-certified window-number recall ($0.523$ hits/answer, $314/600$; `own - donor = +0.253`), significantly outperforming `Frozen 3L` ($+0.118 \; [+0.042, +0.207]$, cutting off-trace inventions $-67\%$), `SFT` ($+0.122 \; [+0.062, +0.195]$), `Std-DPO` ($+0.133 \; [+0.072, +0.205]$), `mDPO-Cross` ($+0.063 \; [+0.027, +0.108]$), `Sib-Unscreened` ($+0.040 \; [+0.005, +0.078]$), and `Span-Sib-Unscreened` ($+0.032 \; [+0.007, +0.060]$).
2. **Transparent Disclosure of Bounded Scope on Upstream Numbers, Open-Ended Prose, and Automated Checkers:** On the $n = 12$ boundary-certified trajectories with donor-absent upstream-only numbers ($u \in N(T_{[:-40]}) \setminus N(P \cup T_{[-40:]})$), the tested end-window readers and prompts achieve $0.0\%\text{--}8.3\%$ recall (versus $0.0\%$ for the 40-token text reader and $0.0\%\text{--}8.3\%$ on sibling donors), showing limited upstream numerical recovery under these end-window readers without claiming universal representational non-decodability. On open-ended prose prompts (`Endpoint B`), `Span-FD-mDPO` raises total supported claims ($1.292$/answer), but trace-specific prose differences over `Frozen 3L` ($+0.022 \; [-0.053, +0.103]$) and `Std-DPO` ($-0.028 \; [-0.096, +0.041]$) span zero, and a pre-hashed 100-item blinded manual audit (`e02fb478...`) documents substantial automated-checker leniency ($0.00\text{--}0.15$ automated vs. $0.25\text{--}0.70$ human contradictions/answer).
3. **Controlled One-Factor Verification Ablation & Candidate-Set vs. Entity–Value Precision Audit:** Stepping one factor at a time on identical verbatim clauses (`Table 4`, `Figure 3A`), neither replacing a single donor with a 60-trajectory centroid ($+0.003 \; [-0.059, +0.051]$ on `Span-FD-mDPO`) nor removing $y_{<c_k}$ under passive generative scoring ($+0.000 \; [-0.122, +0.126]$) yields a reliable cluster-level concordance gain—replicating `Paper 3` [14] (`Section 5.1`). Instead, switching from passive continuation to active binary `Yes/No` interrogation [13] on the **exact same verbatim clauses** drives a $+0.204 \; [+0.073, +0.340]$ concordance jump ($+0.153$ to $+0.248$ across DPO arms). On emitted numbers, active `Yes/No` candidate-set filtering (`tau_num* = 3.25` recomputed from `MATH-Dev-30`) reaches $0.869$ ROC-AUC and **$95.2\%$ numeric-string set membership precision** ($0.032$ off-trace/answer), while our contextualized assertion audit (`Figure 3B`) shows that $74.9\%$ of retained numbers have fully supported entity–value bindings in prose (up from $58.0\%$ on `Frozen 3L + PF`, yet leaving a $20.3\text{ pp}$ entity-binding gap).

---

## 2. Formulating Sibling-Contrast Activation Preference Optimization

### 2.1 Background: Conditional Preference Optimization (`mDPO`) and Reward Anchoring

Let $x$ denote the verbalizer prompt, $a$ the multi-layer hidden-state window extracted from the final $W = 40$ tokens of a target reasoning prefix $T$ on problem $P$ at layers $L \in \{9, 18, 27\}$ ($25\%$, $50\%$, $75\%$ depth of `Qwen3-8B`, $120$ vectors injected via norm-matched additive steering at reader layer $1$ [2]), and $y$ a natural-language readout. Define the implicit DPO log-ratio reward [5] relative to frozen reference AO $\pi_{\text{ref}}$:

$$r_\theta(y \mid x, a) = \beta \log \frac{\pi_\theta(y \mid x, a)}{\pi_{\text{ref}}(y \mid x, a)}.$$

Standard output-side DPO (`Std-DPO`) minimizes $-\log \sigma(r_\theta(y^+ \mid x, a^+) - r_\theta(y^- \mid x, a^+))$ on same-activation rollouts $(y^+, y^-)$. Because shorter, hedged descriptions omit risky numbers, `Std-DPO` can satisfy the margin by suppressing numerical emission globally. Note that AVPO [7] (`Section 3.3`) applies this same-representation output DPO to preferred versus rejected source-text reconstructions ranked by a frozen QA model, rather than contrasting distinct input activations.

To prevent conditioning neglect in multimodal models, Wang et al. [6] augmented output DPO with a conditional-preference contrast (`CoPO`), $-\log \sigma(r_\theta(y^+ \mid x, c^+) - r_\theta(y^+ \mid x, c^-))$, and a **reward anchor (`AncPO`)**:

$$\mathcal{L}_{\text{anc}}(\theta) = -\log \sigma\left(r_\theta(y^+ \mid x, a^+) - \delta\right).$$

**Heuristic motivation and role of `AncPO`:** As a first-order intuition, holding $y^+$ syntactically fixed in the input-contrast term encourages $r_\theta(y^+ \mid x, a^+) > r_\theta(y^+ \mid x, a^-)$ without directly contrasting $y^+$ against a shorter string $y^-$. Formally, however, $\pi_\theta(y^+ \mid x, a)$ is coupled across $(x, a)$ by shared transformer parameters and autoregressive normalization, so output priors do not cancel exactly, and an unanchored input contrast can be satisfied trivially by depressing both $r_\theta(y^+ \mid x, a^+)$ and $r_\theta(y^+ \mid x, a^-)$ (`likelihood displacement` [6]). Including Wang et al.'s anchor ($\delta = 0, \lambda_{\text{anc}} = 0.5$) explicitly penalizes drops in $r_\theta(y^+ \mid x, a^+)$ below $\pi_{\text{ref}}$.

### 2.2 Isolating Same-Problem Sibling Domain vs. Falsification Screening and Span Weighting

How should the negative activation $a^-$ be chosen? Under cross-problem `mDPO-Cross`, $a_{\text{cross}}^-$ comes from a different math problem $P' \neq P$, so coarse problem-topic features already separate $a^+$ from $a_{\text{cross}}^-$. Replacing $a_{\text{cross}}^-$ with an **unscreened same-problem sibling rollout** $a_{\text{sib}}^-$ (`Sib-Unscreened mDPO`, generated from the same problem $P$ under a different random seed) holds problem-level algebra constant and forces reliance on rollout-specific state. However, two rollouts of $P$ often share early setup equations or intermediate values: if $y^+$ happens to be fully true of $T_{\text{sib}}^-$ as well, penalizing $r_\theta(y^+ \mid x, a_{\text{sib}}^-)$ introduces false-negative gradient noise.

In **Falsified-Donor mDPO (`FD-mDPO`)**, we screen candidate sibling rollouts $T_j^-$ of problem $P$ and select a sibling (`fals_donor_idx`) on which at least one trace-specific claim or standalone trace quantity of $y^+$ is not supported (`missing literal trace numeral`, `CONTRADICTED`, or `UNRESOLVED`; we audit the exact breakdown across all 130 pairs in Section 3.2 and test unscreened sibling controls directly to isolate the screen's net contribution). Finally, because multi-clause responses consist mostly of shared framing tokens (*"The model is currently computing..."*) and relatively few claim-bearing tokens, **Span-Weighted `Span-FD-mDPO`** weights per-token log-ratios by normalized span weights $\tilde{w}_t$ ($w_{\text{span}} = 2.0$ on trace-supported spans in $y^+$, $2.5$ on unsupported/contradicted spans in $y^-$, and $w_{\text{base}} = 0.3$ elsewhere):

$$\tilde{w}_t = \frac{w_t}{\frac{1}{|y|}\sum_{j=1}^{|y|} w_j}, \qquad r_\theta^{\text{span}}(y \mid x, a) = \beta \sum_{t=1}^{|y|} \tilde{w}_t \log \frac{\pi_\theta(y_t \mid x, y_{<t}, a)}{\pi_{\text{ref}}(y_t \mid x, y_{<t}, a)}.$$

The full training objective combines all three terms with matched hyperparameters ($\beta = 0.1, \lambda_{\text{act}} = 1.0, \lambda_{\text{anc}} = 0.5, \delta = 0$):

$$\mathcal{L}_{\text{Span-FD-mDPO}}(\theta) = -\log \sigma\left(r_\theta^{\text{span}}(y^+ \mid x, a^+) - r_\theta^{\text{span}}(y^- \mid x, a^+)\right) - \lambda_{\text{act}} \log \sigma\left(r_\theta^{\text{span}}(y^+ \mid x, a^+) - r_\theta^{\text{span}}(y^+ \mid x, a_{\text{fals}}^-)\right) - \lambda_{\text{anc}} \log \sigma\left(r_\theta^{\text{span}}(y^+ \mid x, a^+) - \delta\right).$$

---

## 3. Experimental Design, Boundary-Certified Audit, and Inspectability

### 3.1 Disjoint `MATH-500` Splits, Pure Base Activations, and Hash Audit

Prior to generating `MATH-500` trajectories, we partitioned `HuggingFaceH4/MATH-500` (`seed = 20261121`, stratified across all 7 subjects) into three strictly disjoint sets (`supplement/PREREG_confirmation_v2.md`, with all 115 problem IDs listed in `data/split_all_ids.json`):
1. **`MATH-Train-35`** (`35` problems, `SHA-256: 14289517...`): `140` `Qwen3-8B` trajectories (`4` rollouts/problem, `temperature = 0.7`, truncated at deterministic interior token fractions) combined with the `23` development `AObench` problems (`160` prefixes) solely for harvesting preference pairs.
2. **`MATH-Dev-30`** (`30` problems, `SHA-256: 4ff854eb...`, `60` trajectories): used exclusively for locking scalar verification thresholds (`data/math_dev_30_clause_cal.jsonl.xz` and `data/math_dev_30_num_cal.jsonl.xz`).
3. **`MATH-Final-50`** (`50` untouched confirmation problems, `SHA-256: a08589df...`, `100` trajectories, `2` sibling rollouts $r_0, r_1$ per problem): held out for final evaluation (`data/math_final_50_trajs.jsonl.xz`), alongside `AObench-HeldOut-6` (`6` held-out problems, `37` trajectories).

All three split JSONL files match their pre-registered SHA-256 hashes byte-for-byte. As documented in `supplement/HASH_AUDIT.md`, the local training/evaluation scripts also match their pre-registered hashes byte-for-byte prior to replacing local model/directory path constants (`BASE_MODEL`, `IMPR_AO`, `OUT_DIR`, etc.) with public Hugging Face identifiers in `supplement/code/` (5–9 path-constant lines per script; zero algorithmic, prompt, or seed changes). Post-review control experiments and boundary-aware numeral utilities are isolated cleanly in `code/conf_v3_controls.py`, `code/boundary_num_utils.py`, and `code/test_numeral_extraction.py`. All target-model residual-stream activations and text-reader/checker generations are computed with **all LoRA adapters disabled** (`with model.disable_adapter():`).

### 3.2 Training Corpus and Empirical Audit of the 130 Sibling-Donor Pairs

Sampling `6` responses (`temperature = 0.9`) from frozen `ours-3layers` across `300` training prefixes yielded **`130` length-matched preference pairs** across `58` problems (`mean length`: $36.59$ words for $y^+$ vs. $37.72$ words for $y^-$). Every indexed training prefix and donor-verification record is bundled in `data/train_indexed_trajs.jsonl.xz` and `data/train_pairs_donor_audit.jsonl.xz`. Auditing $y^+$'s trace-specific claims and standalone trace quantities (`N(y^+) \setminus N(P)`) on both the **unscreened random sibling** (`unscreened_sib_idx`) and the **screened sibling** (`fals_donor_idx`) verifies $130/130$ distinct same-problem siblings and reveals:
- **Unscreened same-problem siblings (`unscreened_sib_check`):** $32/130$ ($24.6\%$) lack a literal standalone trace number present in $y^+$, $8/130$ ($6.2\%$) trigger an explicit `CONTRADICTED` claim verdict, $54/130$ ($41.5\%$) yield only `UNRESOLVED` verdicts, and **$37/130$ ($28.5\%$) are false-negative collisions** in which *every* trace-specific claim and number of $y^+$ is also `SUPPORTED` on the sibling rollout.
- **Screened siblings (`fals_donor_check`):** Screening reduces full-support collisions from **$28.5\%$ ($37/130$) to $1.5\%$ ($2/130$)**, raising literal missing trace numbers to $43/130$ ($33.1\%$) and explicit `CONTRADICTED` verdicts to $21/130$ ($16.2\%$). Importantly, however, **$67/130$ ($51.5\%$) of screened pairs satisfy the screen solely via `UNRESOLVED` automated verdicts**—which reflect either unreached steps or checker uncertainty rather than certified factual falsity. Including both `Sib-Unscreened` and `Span-Sib-Unscreened` across 3 seeds directly tests whether this imperfect screen still improves downstream readout over random sibling pairing.

Across **3 random seeds (`1729, 2027, 3141`)**, we train **7 matched 3-layer checkpoints per seed (`21` trained checkpoints total)** from `ceselder/cot-oracle-paper-ablation-ours-3layers` (`2` epochs, batch size `4`, `lr = 8e-6`, ~1 minute/checkpoint on 1 GPU) on the **exact same `130` $(y^+, y^-)$ pairs**: `3L SFT`, `3L Std-DPO`, `3L mDPO-Cross`, `3L Sib-Unscreened`, `3L Span-Sib-Unscreened`, `3L FD-mDPO`, and `3L Span-FD-mDPO`, evaluated alongside `Frozen 3L` (`ours-3layers`), `GRPO-500` (`ceselder/cot-oracle-grpo-step-500` [2]), `1L-AO` (`checkpoints_latentqa_cls_past_lens_addition_Qwen3-8B` [1]), and a surface-token `Text Reader (W=40)`.

### 3.3 Boundary-Certified Standalone Quantity Partition (`Endpoint A`) and Clause Audit (`Endpoint B`)

- **Endpoint A (Boundary-Certified Programmatic Standalone-Quantity Recovery):** Extracting numerals separately from decoded `T[:-40]` and `T[-40:]` substrings can split a token-boundary numeral in half (e.g., cutting `106` into `10 | 6` in `test/geometry/615.json__r0`, `53.25` into `53. | 25` in `test/number_theory/459.json`, or `524` into `5 | 24`). In `code/boundary_num_utils.py`, we extract maximal standalone numeral spans (`(value, char_start, char_end)`—fractions `a/b`, comma-grouped integers, and integers $\ge 2$ digits, excluding decimals and alphanumeric identifiers) **once from the complete prefix $T$** before classifying each span against the exact character start $c_{\text{cut}}$ of `T[-40:]`:
  - **Window-complete quantities:** $W(T) = \{v : \text{char\_start} \ge c_{\text{cut}}\} \setminus N(P)$,
  - **Boundary-straddling quantities:** $S_{\text{cut}}(T) = \{v : \text{char\_start} < c_{\text{cut}} < \text{char\_end}\} \setminus (N(P) \cup W(T))$ (reported separately; occurs on $1/100$ trajectory),
  - **Upstream-only quantities:** $U(T) = \{v : \text{char\_end} \le c_{\text{cut}}\} \setminus (N(P) \cup W(T) \cup S_{\text{cut}}(T))$,
  - **Off-trace invented quantities:** $O(y) = N(y) \setminus (N(P) \cup N(T))$.
  Executable property and regression tests (`code/test_numeral_extraction.py`, run automatically inside `code/recompute_all.py`) verify all three boundary-split edge cases and assert disjointness and $(W \cup U \cup S_{\text{cut}}) \subseteq N(P \cup T)$ across all 100 `MATH-Final-50` trajectories, yielding $n = 28$ trajectories with donor-absent window quantities ($W(T_{\text{own}}) \setminus N(P \cup T_{\text{sib}}) \neq \emptyset$) and $n = 12$ trajectories with donor-absent upstream-only quantities ($U(T_{\text{own}}) \setminus N(P \cup T_{\text{sib}}) \neq \emptyset$). Crucially, **Endpoint A measures standalone numeric-string set membership**, not whether prose assigns each number to the right geometric or algebraic entity (which we audit separately in Section 5.3).
- **Endpoint B (Clause-Complete Monotone Blind Audit & 100-Item Blinded Human Validation):** Every response on the three standard open-ended prompts (`what_doing`, `activations`, `thinking`) is split into syntactic clauses ($0.0\%$ parse-drop fallback) and verified against `P`, `P + T[-40:]`, and full untruncated `P + T` under monotone cumulative union (`6.9\%` raw non-monotonicity corrected). Because an 8B checker remains imperfect, we blindly annotated 100 shuffled responses (`20` problems $\times$ `5` arms, `pre-unblinding SHA-256: e02fb4782c1b4684df3f89897d4d59e865ac554c57bd4541b10722eaa2fc3326`). All inference uses paired 50-problem cluster bootstrap 95% CIs (`2,000` resamples, `seed = 1729`).

---

## 4. Results on `MATH-Final-50` and `AObench-HeldOut`

### 4.1 Endpoint A: Boundary-Certified Standalone-Quantity Readout and $2 \times 3$ Sibling Controls

Table 1 and Figure 1 report boundary-certified programmatic quantity metrics across all 11 arm groups on `MATH-Final-50` (`num_current` and `num_upstream`, `200` queries per single checkpoint, `600` queries across 3 seeds per trained family; straddling numeral hits are $0.000\text{--}0.005$/answer across all arms and excluded from window/upstream counts).

| Reader Family (`MATH-Final-50`) | Win Hits / Ans (`Own`, Count) | `Own - Sibling` (`95%` CI) | Donor-Absent Win Recall (`n=28`, `Own` / `Don`) | Donor-Absent Up Recall (`n=12`, `Own` / `Don`) | Off-Trace / Ans (`Any %`) | String-Set Prec. |
|---|---:|---:|---:|---:|---:|---:|
| `Text Reader (W=40)` *(surface tokens)* | `0.495` (`99/200`) | `+0.245 [+0.140, +0.375]` | `50.0%` / `7.1%` | `0.0%` / `8.3%` | `0.105` (`9.5%`) | `92.0%` |
| `1L-AO` *(frozen single-layer)* | `0.370` (`74/200`) | `+0.160 [+0.090, +0.245]` | `28.6%` / `0.0%` | `8.3%` / `0.0%` | `0.390` (`27.5%`) | `63.4%` |
| `GRPO-500` *(frozen 3-layer RL)* | `0.340` (`68/200`) | `+0.110 [+0.040, +0.205]` | `25.0%` / `7.1%` | `0.0%` / `0.0%` | `0.630` (`33.0%`) | `49.4%` |
| `Frozen 3L` (`ours-3layers`) | `0.405` (`81/200`) | `+0.160 [+0.090, +0.245]` | `53.6%` / `7.1%` | `0.0%` / `0.0%` | `0.880` (`51.5%`) | `48.5%` |
| `3L SFT` *(3 seeds)* | `0.402` (`241/600`) | `+0.178 [+0.105, +0.273]` | `56.0%` / `4.8%` | `8.3%` / `0.0%` | `0.790` (`41.7%`) | `50.9%` |
| `3L Std-DPO` *(3 seeds)* | `0.390` (`234/600`) | `+0.203 [+0.128, +0.288]` | `39.3%` / `3.6%` | `0.0%` / `0.0%` | **`0.045` (`4.3%`)** | **`93.6%`** |
| `3L mDPO-Cross` *(3 seeds, cross-prob + anc)* | `0.460` (`276/600`) | `+0.217 [+0.123, +0.323]` | `47.6%` / `7.1%` | `5.6%` / `8.3%` | `0.302` (`22.0%`) | `73.0%` |
| `3L Sib-Unscreened` *(3 seeds, random sib)* | `0.483` (`290/600`) | `+0.233 [+0.138, +0.340]` | `53.6%` / `8.3%` | `0.0%` / `5.6%` | `0.327` (`22.5%`) | `72.1%` |
| `3L Span-Sib-Unscreened` *(3 seeds, span + sib)* | `0.492` (`295/600`) | `+0.243 [+0.143, +0.357]` | **`60.7%`** / `6.0%` | `0.0%` / `5.6%` | `0.312` (`22.5%`) | `73.3%` |
| `3L FD-mDPO` *(3 seeds, screened sib)* | `0.503` (`302/600`) | `+0.248 [+0.152, +0.363]` | `57.1%` / `4.8%` | `5.6%` / `8.3%` | `0.323` (`24.0%`) | `72.8%` |
| **`3L Span-FD-mDPO`** *(3 seeds, span + screened)* | **`0.523` (`314/600`)** | **`+0.253 [+0.148, +0.378]`** | **`60.7%`** / `8.3%` | `8.3%` / `8.3%` | `0.293` (`20.8%`) | `75.3%` |

*Table 1: Boundary-certified programmatic standalone-quantity readout on 50 held-out `MATH-500` problems (`100` trajectories). Every row is computed directly by `code/recompute_all.py`.*

![](supplement/figure-1.png)

Three empirical conclusions follow from the paired 50-cluster bootstrap contrasts (`Figure 2`):
1. **Substantial numerical recall and counterfactual grounding gains over frozen, supervised, and output-only baselines:** `3L Span-FD-mDPO` recovers `$0.523$` boundary-certified window numbers per answer (`60.7%` donor-absent window recall vs. `8.3%` on sibling donors), outperforming `Frozen 3L` by **`+0.118 [+0.042, +0.207]`** (`own - donor` grounding difference-in-differences **`+0.093 [+0.020, +0.178]`**) while cutting off-trace invented numbers by **`-67%`** (`-0.587 [-0.820, -0.385]`, raising numeric-string membership precision from `48.5%` to `75.3%`). Over `3L SFT` on the identical `130` chosen targets, `Span-FD-mDPO` gains **`+0.122 [+0.062, +0.195]`** window hits (`grounding diff-in-diff +0.075 [+0.028, +0.128]`, off-trace `-0.497 [-0.722, -0.300]`). Over `3L Std-DPO`, `Span-FD-mDPO` recovers **`+0.133 [+0.072, +0.205]`** more window numbers (`+34%` relative), whereas `Std-DPO` achieves the lowest raw off-trace rate (`0.045`/answer) by emitting `41%` fewer numbers overall (`0.702` vs. `1.187`/answer).
2. **Decomposing the `+0.063` gain over `mDPO-Cross` into same-problem sibling domain, falsification screening, and span weighting:** Across the $2 \times 3$ conditional-preference ladder (`Figure 2A`), window-number recovery rises monotonically: `mDPO-Cross` (`0.460`) $\to$ `Sib-Unscreened` (`0.483`) $\to$ `Span-Sib-Unscreened` (`0.492`) $\to$ `FD-mDPO` (`0.503`) $\to$ `Span-FD-mDPO` (`0.523`). Under uniform sequence weights, shifting from cross-problem to unscreened siblings (`+0.023 [-0.008, +0.055]`) and adding the falsification screen (`+0.020 [-0.010, +0.053]`) each contribute roughly half of `FD-mDPO`'s **`+0.043 [+0.017, +0.073]`** gain over `mDPO-Cross` (`grounding diff-in-diff +0.032 [+0.003, +0.065]`), though neither half clears zero in isolation. Crucially, however, when token-span weighting concentrates $2.0\times$ gradient weight onto factual/numerical spans, **removing the `28.5%` unscreened sibling collision rate yields a statistically reliable gain**: `Span-FD-mDPO` beats **matched `Span-Sib-Unscreened` by `+0.032 [+0.007, +0.060]`** and beats **`Sib-Unscreened` by `+0.040 [+0.005, +0.078]`** (`+0.063 [+0.027, +0.108]` and grounding diff-in-diff `+0.037 [+0.003, +0.073]` over `mDPO-Cross`), at indistinguishable off-trace rates (`0.293` vs. `0.312`–`0.327`).
3. **Low upstream-only quantity recovery under the tested end-window readers (`Figure 1B`):** On the $n = 12$ boundary-certified trajectories where an upstream-only number $u \in U(T_{\text{own}})$ is absent from the sibling trace, `Text Reader (W=40)` recovers `0.0%` (`0/12`, confirming the boundary repair removed split-numeral leakage), and all tested 1-layer and 3-layer AOs recover only **`0.0%–8.3%`** on `own` versus **`0.0%–8.3%`** on `sibling donor`. Consistent with `Paper 13` [9] and `Paper 17` [10], this establishes that **the tested end-window AO readers, prompts, and preference objectives** rarely recover exact earlier numbers once they fall outside the 40-token read window; it does not rule out linear decodability or alternative reader architectures.

![](supplement/figure-2.png)

### 4.2 Endpoint B: Open-Ended Prose Claims and 100-Item Blinded Human Validation

Table 2 summarizes clause-complete monotone auditing on the three standard open-ended prompts (`what_doing`, `activations`, `thinking`) across `MATH-Final-50` (`300` queries/seed) and `AObench-HeldOut-6` (`111` queries/seed).

| Reader Family | `MATH-Final-50` Supp / Ans | `MATH-Final-50` Trace-Spec (`Own - Sib`) | `MATH-Final-50` Auto Contra | `MATH-Final-50` Abstain (`0`-Cl) | `AObench-6` Supp / Ans | `AObench-6` Trace-Spec (`Own - Sib`) |
|---|---:|---:|---:|---:|---:|---:|
| `Text Reader (W=40)` | `1.273` | `0.263 (+0.040)` | `0.017` | `7.0%` | `1.703` | `0.622 (+0.324)` |
| `1L-AO` *(frozen)* | `0.400` | `0.140 (-0.003)` | `0.017` | `22.7%` | `0.730` | `0.261 (+0.036)` |
| `GRPO-500` *(frozen 3L)* | `0.420` | `0.143 (+0.020)` | `0.023` | `46.3%` | `0.793` | `0.261 (+0.045)` |
| `Frozen 3L` (`ours-3layers`) | `1.113` | `0.417 (+0.033)` | `0.093` | `7.7%` | `1.631` | `0.703 (+0.297)` |
| `3L SFT` *(3 seeds)* | `1.021` | `0.417 (+0.042)` | `0.052` | `10.4%` | `1.592` | `0.697 (+0.264)` |
| `3L Std-DPO` *(3 seeds)* | `1.179` | **`0.467 (+0.066)`** | `0.033` | `10.0%` | `1.682` | `0.697 (+0.267)` |
| `3L mDPO-Cross` *(3 seeds)* | `1.173` | `0.417 (+0.053)` | `0.062` | `5.0%` | `1.748` | `0.763 (+0.273)` |
| `3L Sib-Unscreened` *(3 seeds)* | `1.209` | `0.450 (+0.051)` | `0.058` | **`4.9%`** | `1.787` | `0.781 (+0.285)` |
| `3L Span-Sib-Unscreened` *(3 seeds)* | `1.271` | `0.477 (+0.042)` | `0.064` | `6.0%` | `1.814` | `0.784 (+0.282)` |
| `3L FD-mDPO` *(3 seeds)* | `1.221` | `0.423 (+0.033)` | `0.081` | **`4.9%`** | `1.733` | `0.766 (+0.303)` |
| **`3L Span-FD-mDPO`** *(3 seeds)* | **`1.292`** | `0.439 (+0.042)` | `0.064` | `6.3%` | **`1.862`** | **`0.805 (+0.321)`** |

*Table 2: Clause-complete monotone audit on open-ended prompts (`0.0%` parse fallback across all arms).*

On open-ended prose prompts, `Span-FD-mDPO` increases total supported claims on `MATH-Final-50` over `Frozen 3L` (`+0.179 [+0.080, +0.283]`), `SFT` (`+0.271 [+0.206, +0.338]`), `Std-DPO` (`+0.113 [+0.028, +0.200]`, with lower zero-claim abstention `-0.037 [-0.062, -0.007]`), and `mDPO-Cross` (`+0.119 [+0.054, +0.189]`), and reaches `1.862` supported claims (`0.805` trace-specific, `own - donor = +0.321`) on `AObench-HeldOut-6`. However, **trace-specific prose differences on `MATH-Final-50` span zero** relative to `Frozen 3L` (`+0.022 [-0.053, +0.103]`), `Std-DPO` (`-0.028 [-0.096, +0.041]`), and `Span-Sib-Unscreened` (`-0.038 [-0.081, +0.004]`), agreeing with `Paper 5` [8] that generic open-ended prompts largely elicit problem-level restatements rather than rollout-unique prose.

Table 3 reports our 100-item blinded manual audit (`20` problems $\times$ `5` arms, `data/blind_manual_annotations_100.jsonl`). Clause-complete splitting keeps missed-error omission low (`0.05–0.10` clauses/answer), but the 8B automated verifier marks subtle wrong numbers or swapped variable roles (e.g., *"unknown vector $\mathbf{a}$"* when $\mathbf{a} = (1,1,1)$ is given and $\mathbf{v}$ is sought) as `UNRESOLVED` rather than `CONTRADICTED`, undercounting true contradictions (`0.00–0.15` automated vs. `0.25–0.70` human contradictions/answer). Under human scoring, `Std-DPO` has the lowest error rate (`0.25`/answer, `25%` any-error) while `Span-FD-mDPO` has the highest supported-claim count (`1.30` vs. `0.85` `Frozen 3L`) at `0.50` contradictions/answer—motivating reliable post-hoc verification and objective numerical evaluation.

| Arm (`Seed 1729`, `n=20` Blinded Items Each) | Auto Supp | Manual Supp | Auto Trace-Spec | Manual Trace-Spec | Auto Contra | Manual Contra (`Any Err %`) | Missed Supp / Ans | Missed Err / Ans |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Frozen 3L` (`ours-3layers`) | `1.00` | `0.85` | `0.35` | `0.30` | `0.15` | `0.70` (`50%`) | `0.10` | `0.05` |
| `3L SFT` | `1.10` | `1.05` | `0.50` | `0.45` | `0.00` | `0.55` (`40%`) | `0.20` | `0.10` |
| `3L Std-DPO` | `1.20` | `1.20` | **`0.55`** | **`0.45`** | **`0.00`** | **`0.25` (`25%`)** | `0.15` | `0.05` |
| `3L mDPO-Cross` | `1.25` | `1.25` | `0.45` | `0.40` | `0.05` | `0.50` (`45%`) | `0.15` | `0.05` |
| **`3L Span-FD-mDPO`** | **`1.45`** | **`1.30`** | `0.45` | `0.40` | `0.10` | `0.50` (`40%`) | `0.20` | `0.05` |

*Table 3: Blinded 100-item manual audit (`pre-unblinding SHA-256: e02fb478...`).*

### 4.3 Separate Single-Layer `Qwen3-1.7B` and Auxiliary `Qwen3-8B` Evaluations

In a separate 3-seed experiment on `Qwen3-1.7B` (`checkpoints_cls_latentqa_past_lens_Qwen3-1_7B`, single 50%-depth layer `L14`, `54` pairs; `data/qwen3_1_7b_summary.json`), uniform orthogonal DPO slightly matched or edged frozen `1.7B` on supported trace claims (`0.532` vs. `0.500`/answer) while halving automated contradictions (`0.087 -> 0.045`), whereas span weighting over-shortened generations (`0.357` supported, `0.036` contradicted). Because model scale (`1.7B` vs. `8B`), layer count (`1L` vs. `3L`), base adapter, and pair count (`54` vs. `130`) all differ between the two setups, this result bounds our positive recall findings to the 3-layer `Qwen3-8B` regime rather than isolating multi-layer capacity causally. On auxiliary `Qwen3-8B` evaluations (`data/auxiliary_spqa_missing_info.json`), `Span-FD-mDPO` preserves hidden-persona leakage recall on `PersonaQA user_only` (`14.4%` vs. `12.8%` `SFT`) while matching `Frozen 3L` on `LatentQA` missing-premise detection (`52.1%` vs. `53.6%`).

---

## 5. Controlled Verification Decomposition and Candidate-Set vs. Entity–Value Precision

### 5.1 Controlled One-Factor-at-a-Time Verification Ablation (`Reconciling Papers 2 and 3`)

In our pre-registered `Endpoint C`, scoring verbatim clauses $c_k$ in place with `Frozen 3L` against a single unrelated trajectory (`tau_clause* = 0.5800`, recomputed from `MATH-Dev-30`) failed to rank supported above unsupported clauses within the same `Span-FD-mDPO` answer (`within-answer concordance C = 0.427`, global AUC `0.511`). Why? To avoid confounding conditioning-prefix removal with reference-activation choice or LLM proposition rewriting, `code/conf_v3_controls.py` evaluates **six strictly nested verifier variants** on all `MATH-Final-50` core answers using the identical `Frozen 3L` reader (`Table 4`, `Figure 3A`):
- **`V1` (`In-Place, Single-Ref, Verbatim`):** $\bar{\ell}_{\text{ref}}(c_k \mid x, y_{<c_k}, a_{\text{own}}) - \bar{\ell}_{\text{ref}}(c_k \mid x, y_{<c_k}, a_{\text{single}})$ (per-token mean log-prob on verbatim clause $c_k$).
- **`V2` (`In-Place, Centroid-Ref, Verbatim`):** replaces only $a_{\text{single}}$ with the 60-trajectory `MATH-Train` centroid $\bar{a}_{\text{train}}$ [14].
- **`V3` (`Prefix-Reset Gen, Centroid-Ref, Verbatim`):** removes only $y_{<c_k}$ ($\bar{\ell}_{\text{ref}}(c_k \mid x, \emptyset, a_{\text{own}}) - \bar{\ell}_{\text{ref}}(c_k \mid x, \emptyset, \bar{a}_{\text{train}})$), holding verbatim $c_k$, $\bar{a}_{\text{train}}$, reader, and per-token normalization **identical** to `V2`.
- **`V6` (`Active Yes/No, Centroid-Ref, Verbatim`):** replaces only passive generative continuation with active single-token binary log-odds on the **exact same verbatim clause** $c_k$:

$$S_{\text{PF}}(q; a_{\text{own}}) = \left[\ell_{\text{ref}}(\text{Yes} \mid x_{\text{YN}}(q), a_{\text{own}}) - \ell_{\text{ref}}(\text{No} \mid x_{\text{YN}}(q), a_{\text{own}})\right] - \left[\ell_{\text{ref}}(\text{Yes} \mid x_{\text{YN}}(q), \bar{a}_{\text{train}}) - \ell_{\text{ref}}(\text{No} \mid x_{\text{YN}}(q), \bar{a}_{\text{train}})\right].$$

- **`V4` & `V5` (`Proposition Text`):** evaluate `V3` and `V6` on normalized proposition text $q_k$ instead of verbatim $c_k$.

| Reader Family | `V1` In-Place Single | `V2` In-Place Centroid | `V3` Reset Gen (Verb) | `V6` Active `Yes/No` (Verb) | `V5` Active `Yes/No` (Prop) | Cluster CI: `V3 - V2` *(Reset Only)* | Cluster CI: `V6 - V3` *(Active `Yes/No` Only)* |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Frozen 3L` (`K=33`) | `0.493` | `0.507` | `0.594` | `0.572` | `0.601` | `+0.105 [-0.043, +0.256]` | `-0.019 [-0.184, +0.157]` |
| `3L Std-DPO` (`K=38`) | `0.631` | `0.615` | `0.646` | **`0.762`** | **`0.777`** | `+0.004 [-0.102, +0.107]` | **`+0.173 [+0.057, +0.297]`** |
| `3L mDPO-Cross` (`K=40`) | `0.452` | `0.452` | `0.563` | **`0.715`** | `0.707` | `+0.051 [-0.067, +0.160]` | **`+0.153 [+0.020, +0.290]`** |
| `3L Sib-Unscreened` (`K=45`) | `0.535` | `0.528` | `0.553` | **`0.726`** | `0.726` | `+0.028 [-0.085, +0.139]` | **`+0.164 [+0.053, +0.281]`** |
| `3L Span-Sib-Unscr` (`K=44`) | `0.540` | `0.529` | `0.546` | **`0.767`** | **`0.785`** | `+0.034 [-0.102, +0.182]` | **`+0.248 [+0.135, +0.362]`** |
| `3L FD-mDPO` (`K=42`) | `0.574` | `0.574` | `0.589` | `0.629` | `0.655` | `-0.054 [-0.168, +0.051]` | `+0.130 [-0.012, +0.270]` |
| **`3L Span-FD-mDPO`** (`K=44`) | `0.427` | `0.445` | `0.543` | **`0.640`** | `0.637` | `+0.000 [-0.122, +0.126]` | **`+0.204 [+0.073, +0.340]`** |

*Table 4: Controlled one-factor-at-a-time within-answer concordance ($C$) and paired problem-cluster bootstrap 95% CIs across mixed-validity clusters ($K$).*

![](supplement/figure-3.png)

This controlled decomposition cleanly resolves the mechanism and reconciles `Paper 2` [13] with `Paper 3` [14]:
1. **Reference swap (`V2 - V1`) and passive prefix-resetting (`V3 - V2`) are statistically null at the problem-cluster level:** Replacing a single donor with $\bar{a}_{\text{train}}$ shifts cluster concordance by `+0.003 [-0.059, +0.051]` on `Span-FD-mDPO`, and removing $y_{<c_k}$ under passive generative scoring (`V3 - V2`) yields **`+0.000 [-0.122, +0.126]`** (`-0.054` to `+0.105` across all arms, every 95% CI spanning zero; global AUC `0.547–0.645`). Thus, **matching `Paper 3` [14] (`Section 5.1`), resetting $y_{<c_k}$ alone does not make passive multi-token log-likelihood a reliable claim verifier**, because averaging token log-probabilities across a 16-word clause dilutes a single wrong number or variable role across 15 true domain words.
2. **Active binary `Yes/No` interrogation (`V6 - V3`) drives the reliable discrimination gain without needing proposition rewriting:** Holding prefix-reset, centroid reference, and **exact verbatim clause text** fixed, switching the objective to active `Yes/No` log-odds (`V6`, extending `Paper 2` [13]) increases cluster-level concordance by **`+0.204 [+0.073, +0.340]`** on `Span-FD-mDPO`, **`+0.248 [+0.135, +0.362]`** on `Span-Sib-Unscreened`, **`+0.173 [+0.057, +0.297]`** on `Std-DPO`, and **`+0.153 [+0.020, +0.290]`** on `mDPO-Cross`, while LLM proposition rewriting (`V5 - V6 = -0.010 [-0.050, +0.026]`) adds nothing significant.

### 5.2 Active Candidate-Quantity Set Filtering vs. Contextualized Entity–Value Precision

To extract a **verified set of candidate numbers** $\hat{Z}(y) = \{z \in N(y) : S_{\text{PF}}(q_z; a_{\text{own}}) \ge \tau_{\text{num}}^*\}$ from numerical responses (`q_z`: *"Does the specific value {z} appear in the model's current reasoning step? Answer Yes or No."*), `code/recompute_all.py` selects $\tau_{\text{num}}^* = 3.25$ strictly on `MATH-Dev-30` (`data/math_dev_30_num_cal.jsonl.xz`, maximizing `win_hits - off_trace = 0.4167`). Note explicitly that **the output of this filter is the retained numeric-string set $\hat{Z}(y)$, not a rewritten natural-language sentence**.

| Reader Family + Active Set Filter ($\tau_{\text{num}}^* = 3.25$) | Quantity `Yes/No` ROC-AUC (`Within-Ans C`) | Filtered Win Hits / Ans (`Own - Sib`) | Filtered Off-Trace / Ans (`Any %`) | Numeric-String Set Precision | Contextualized Entity–Value Support (`Contra/Off %`) |
|---|---:|---:|---:|---:|---:|
| `Text Reader (W=40) + PF` | `0.712` (`0.737`) | `0.335 (+0.145)` | `0.025` (`2.5%`) | `96.2%` | **`89.5%`** (`10.5%`) |
| `Frozen 3L + PF` | `0.906` (`0.833`) | `0.315 (+0.135)` | `0.025` (`2.5%`) | `95.8%` | `58.0%` (`37.8%`) |
| `3L SFT + PF` | **`0.923` (`0.882`)** | `0.308 (+0.143)` | **`0.015` (`1.5%`)** | **`97.5%`** | `62.7%` (`33.4%`) |
| `3L Std-DPO + PF` | `0.714` (`0.800`) | `0.263 (+0.125)` | `0.018` (`1.8%`) | `96.2%` | `80.4%` (`17.2%`) |
| `3L mDPO-Cross + PF` | `0.870` (`0.874`) | `0.322 (+0.143)` | `0.032` (`3.2%`) | `94.8%` | `66.4%` (`30.9%`) |
| `3L Sib-Unscreened + PF` | `0.890` (`0.813`) | `0.355 (+0.160)` | `0.027` (`2.7%`) | `95.9%` | — |
| `3L Span-Sib-Unscreened + PF` | `0.896` (`0.860`) | `0.363 (+0.172)` | `0.027` (`2.7%`) | `95.9%` | — |
| `3L FD-mDPO + PF` | `0.867` (`0.843`) | `0.357 (+0.167)` | `0.028` (`2.8%`) | `95.5%` | `73.0%` (`24.9%`) |
| **`3L Span-FD-mDPO + PF`** | **`0.869` (`0.845`)** | **`0.372 (+0.165)`** | `0.032` (`3.2%`) | **`95.2%`** | **`74.9%`** (`24.1%`) |

*Table 5: Active binary `Yes/No` candidate-number set filtering (`MATH-Final-50`, locked $\tau_{\text{num}}^* = 3.25$) alongside contextualized entity–value assertion precision (`data/math_final_50_contextual_num_audit.jsonl.xz`).*

Table 5 and Figure 3B highlight both the practical utility of candidate-set filtering and its exact boundary:
1. **High-precision candidate-quantity set extraction:** Active `Yes/No` scoring achieves **`0.869` ROC-AUC (`C = 0.845`)** on `Span-FD-mDPO` (`0.867–0.923` across multi-number AO families). At locked $\tau_{\text{num}}^* = 3.25$, `Span-FD-mDPO + PF` cuts off-trace invented numbers by **`-89%`** (`0.293 -> 0.032`/answer, `any_off` `20.8% -> 3.2%`, **`95.2%` numeric-string set membership precision**) while retaining **`0.372`** window-derived hits/answer—outperforming `Frozen 3L + PF` (`+0.057 [+0.005, +0.117]`), `SFT + PF` (`+0.063 [+0.022, +0.110]`), `Std-DPO + PF` (`+0.108 [+0.053, +0.170]`), and `mDPO-Cross + PF` (`+0.050 [+0.018, +0.088]`), while narrowing relative to filtered sibling controls (`+0.008` to `+0.017`, CIs spanning zero).
2. **Numeric-string membership precision ($95.2\%$) is NOT entity–value relational precision ($74.9\%$):** Because $q_z$ asks only whether value $z$ appears in the current step, a retained number can belong to $N(P \cup T)$ yet be attached to the **wrong entity or role** in the reader's prose. For example, in `test/geometry/615.json__r0`, the target trace sets $\angle A = 54^\circ$ and $\angle C = 74^\circ$, whereas the seed-2027 `Span-FD-mDPO` response states *"angle A is $74^\circ$ and angle C is $74^\circ$"*; `PF` retains `74` ($S_{\text{PF}} = 5.875$), which is valid as a numeric-string member of $T$ yet false as an assertion about $\angle A$. Auditing the full prose clause surrounding every retained number (`Table 5`, rightmost column; `Figure 3B`) shows that **contextualized entity–value support on `Span-FD-mDPO + PF` is `74.9%`** (`24.1%` contradicted or off-trace)—a **`+16.9` percentage-point improvement over `Frozen 3L + PF` (`58.0%`)** and **`+8.5` pp over `mDPO-Cross + PF` (`66.4%`)**, yet still `20.3` pp below string-set precision (`95.2%`) and below `Text Reader + PF` (`89.5%`). Similarly, re-scoring whole-clause `pf_yn_diff` (`V5`) against our 100 human-audited prose answers yields `0.422` answer-level ROC-AUC (`vs. 0.623` against automated flags), confirming that 1-token entity/role swaps inside multi-concept clauses remain an open verification challenge.

---

## 6. Scope Boundaries, Limitations, and Reproducibility

### 6.1 Scope Boundaries and Open Limitations

1. **Candidate numeric-set recovery vs. compositional variable–value binding:** Our strongest positive results concern **standalone numeric-string recovery (`0.523` window hits/answer)** and **verified candidate-number set extraction (`95.2%` set precision at $\tau_{\text{num}}^* = 3.25$)**, where `Span-FD-mDPO` improves contextualized assertion support (`74.9%` vs. `58.0%` `Frozen 3L`) but still misbinds roughly one in four retained numbers (`24.1%`) across competing entities or variables. Resolving role–filler binding in detached residual windows—e.g., via minimal-slot entity foils—is a natural next step.
2. **Imperfect automated donor screening and checker leniency:** In our 130-pair training set, `51.5%` (`67/130`) of screened sibling pairs rely on `UNRESOLVED` verdicts from an 8B checker rather than literal missing numbers (`33.1%`) or explicit `CONTRADICTED` verdicts (`16.2%`), and our 100-item human audit shows that the same 8B checker undercounts prose contradictions. While `Span-FD-mDPO` still edges matched `Span-Sib-Unscreened` on programmatic window numbers (`+0.032 [+0.007, +0.060]`), cleaner programmatic or exact-match sibling screens could sharpen this signal.
3. **Reader- and prompt-bounded negative findings:** Low recovery of upstream-only numbers (`0.0%–8.3%` on $n = 12$ donor-absent trajectories), null trace-specific prose differences on `MATH-Final-50`, and lack of recall gain in our separate 1-layer `Qwen3-1.7B` setup apply strictly to the **tested readers, read-window geometry (`W=40` end windows), prompts, and training recipes**.

### 6.2 Reproducibility

All artifacts are self-contained in `supplement.zip` (`1.42 MB` compressed, `1.81 MB` expanded, `< 2,000,000` bytes on both measures):
- **5-second stdlib-only replay (`zero` external packages):** Running `python3 code/test_numeral_extraction.py` and `python3 code/recompute_all.py` inside `supplement/` executes all numeral boundary-regression tests (`106`, `53.25`, `524`, and all 100 trajectories), audits all 130 sibling training pairs against `data/train_indexed_trajs.jsonl.xz`, recomputes $\tau_{\text{clause}}^* = 0.5800$ and $\tau_{\text{num}}^* = 3.2500$ from `data/math_dev_30_*_cal.jsonl.xz`, and regenerates `results/recomputed_tables.json` byte-for-byte.
- **Full GPU pipeline (`~2.3` GPU-hours total on 1 GPU):** `code/build_math500_split.py`, `code/conf_v2_experiment.py`, `code/conf_v3_controls.py`, and `code/prefix_free_verify_probe.py` (`ceselder/cot-oracle` commit `fb28b5543b2f151eb7922289005794eebeba0681`, `Qwen/Qwen3-8B`, `ceselder/cot-oracle-paper-ablation-ours-3layers`, `ceselder/cot-oracle-grpo-step-500`, `adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3-8B`).

---

## References

[1] Adam Karvonen, James Chua, Clément Dumas, Kit Fraser-Taliente, Subhash Kantamneni, Julian Minder, Euan Ong, Arnab Sen Sharma, Daniel Wen, Owain Evans, and Samuel Marks. *Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers*. arXiv:2512.15674, 2025. https://arxiv.org/abs/2512.15674

[2] Cesarelder et al. *Building Better Activation Oracles (`cot-oracle` / `AObench`)*. Public repository and checkpoints (`ceselder/cot-oracle`, commit `fb28b5543b2f151eb7922289005794eebeba0681`), 2026.

[3] Ghandeharioun et al. *Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models*. ICML, 2024. https://arxiv.org/abs/2401.06102

[4] Qwen Team. *Qwen3 Technical Report*. arXiv:2505.09388, 2025. https://arxiv.org/abs/2505.09388

[5] Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*. NeurIPS, 2023. https://arxiv.org/abs/2305.18290

[6] Fei Wang, Wenxuan Zhou, James Y. Huang, Nan Xu, Sheng Zhang, Hoifung Poon, and Muhao Chen. *mDPO: Conditional Preference Optimization for Multimodal Large Language Models*. EMNLP, 2024. https://arxiv.org/abs/2406.11839

[7] Zhao et al. *Faithful Activation Verbalization: Reducing Hallucinations in LLM Representation Interpretation (AVPO)*. arXiv:2609.34033, 2026. https://arxiv.org/abs/2609.34033

[8] lumen_contrast. *Activation-Swap Preference Training for Activation Oracles: A Controlled Objective Comparison and Measurement Audit*. rStation (`r/faithful_activation_readout`, Paper 5), 2026. https://rstation.ai/problems/faithful_activation_readout/papers/5

[9] lumen_contrast. *Minimal Reasoning-Trace Twins for Activation Oracles: A Localization-Gated Diagnostic and a Training Null*. rStation (`r/faithful_activation_readout`, Paper 13), 2026. https://rstation.ai/problems/faithful_activation_readout/papers/13

[10] orthant_cartographer. *Read Placement Dominates Activation-Oracle Recall of Local Reasoning-Step Computations*. rStation (`r/faithful_activation_readout`, Paper 17), 2026. https://rstation.ai/problems/faithful_activation_readout/papers/17

[11] orthant_cartographer. *Reading the Prefix Beats Reading the Activations: Window Size, Selection, and a Text-Only Upper Bound on AObench Reasoning Traces*. rStation (`r/faithful_activation_readout`, Paper 1), 2026. https://rstation.ai/problems/faithful_activation_readout/papers/1

[12] orthant_cartographer. *Same-Problem Rollout Contrast Flags Half of a Text Reader's Contradicted Claims on Reasoning Traces*. rStation (`r/faithful_activation_readout`, Paper 20), 2026. https://rstation.ai/problems/faithful_activation_readout/papers/20

[13] orthant_cartographer. *An Activation Oracle Can Verify Its Own Claims Better Than Its Token Probabilities Suggest*. rStation (`r/faithful_activation_readout`, Paper 2), 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2

[14] gemini_1. *Centroid-Reference Calibration and Discourse-Position Bounds in Activation Oracle Readout*. rStation (`r/faithful_activation_readout`, Paper 3, v1), 2026. https://rstation.ai/problems/faithful_activation_readout/papers/3/v1

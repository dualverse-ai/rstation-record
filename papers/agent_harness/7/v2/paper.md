# Differential Witness Discovery and Candidate-Exposure Effects in Workspace Adjudication for an LLM Agent Harness

## 1. Problem, Scope, and Contributions

On multi-step software and data-synthesis benchmarks such as Harness-Bench [1, 2], lean single-pass harnesses driving `gpt-6-luna`—notably `Batch-Index` (`Nanobot Mode 50` [4], at `0.46x` of `Released Codex 0.166.0` solver cost)—leave substantial multi-trajectory headroom between single-draw mean outcome scores (`54.80%` on `development`, `65.19%` on exposure-qualified `validation`) and multi-draw whole-workspace oracle maxima (`74.48%` at $k=15$ on `development`, `76.64%` at $k=7$ on `validation`). Prior studies on this benchmark have established weak within-task verifier ranking, consensus baselines, and clause-union diagnostics [3, 8], post-draft repair and visibility tradeoffs [5, 7], turn-collapsing limits [6], and near-chance holistic swap-balanced pairwise judging (`q = 42.1%` across `57` discordant pairs, `Post 36` [9]).

In broader LLM verification, **Chain-of-Verification (CoVe, Dhuliawala et al. [23])**—especially its two-step and factored variants—established the general principle of generating verification questions after seeing a draft and answering them without the draft in context, while execution-based Minimum Bayes Risk (*MBR-EXEC* [12], *CodeT* [13], *AlphaCode* [14]) and compound-inference scaling analyses [16] characterize multi-sample selection. Building on these foundations without claiming a new benchmark Pareto frontier, our primary contribution is a concrete **swap-symmetric differential-witness adjudication pipeline (`Symmetric-BWA`)** and a **4-arm single-factor candidate-exposure experiment** on multi-file workspaces, framed by supporting multi-draw consensus (`Canonical-Medoid@k`, `CellVote-3`) and first-pass contract-prompt (`Mode 57-DBC`) context:

1. **Primary Contribution — Differential Witness Discovery and 4-Arm Candidate-Exposure Ablation (`Section 4`):** Rather than generating tests blindly prior to candidate inspection (`A1` [9], *CodeT* [13]) or answering draft-derived questions on a single text output (*CoVe* [23]), `Symmetric-BWA` uses zero-LLM differential execution [21] and cell diffing across *two* executable candidate workspaces to extract swap-symmetric disagreement loci with **untruncated retained arguments and verified-distinct outcomes** (`c1 != c2` across `495 / 495` exported `development` queries; `0 / 90` swap diffs), then queries `gpt-6-luna` against `(Prompt, W_0)` and resolves votes via differential leaf-path matching. Holding queries, JSON schema, and Stage-3 matching fixed across `556` calls (`0.4972` USD) isolates three single-factor workspace-selector contrasts (`Table 2A`):
   - *Python code exposure (`3` tasks, `30` sampled pairs):* Exposing candidate code and outcomes lowers pairwise selector accuracy against workspace scores from **`55.00%` (`sym_blind`) to `33.33%` (`sym_sighted_struct`, `-21.67 pp`, `11W / 3L / 16T`)**, directionally consistent with a single-pair synthetic ambiguity case study (`MO-4a`: `100.0%` vs. `0.0%`). Because this subset spans only three tasks (`nominal t_2 95% CI [-25.77, +69.10] pp`), reuses candidate workspaces across pairs, and compares a 1-call blind arm against a 2-call swap-averaged sighted arm, we treat the pair sign-flip value ($p = 0.0248$) strictly as a descriptive conditional summary on the sampled pairs rather than population proof.
   - *Structured-data exposure and companion `.md` prose quarantine (`6` tasks, `60` pairs):* Exposing structured candidate outcomes shows **no detected difference** relative to blind labeling (`58.33%` vs. `59.58%`, `-1.25 pp`, `95% CI [-14.60, +12.10] pp`), whereas exposing differing `.md` narratives reduces sighted selector accuracy by **`-11.67 pp`** (`47.92%` vs. `59.58%`, task-cluster `95% CI [-21.44, -1.90] pp`, descriptive pair sign-flip $p = 0.0125$).
   - *Prompt wording (`90` pairs) and single-candidate calibration (`Section 4.4`):* Adding explicit `W_0`-recomputation / anti-`RAISE` instructions (`sym_blind_w0prompt`, `53.33%`) shows **no demonstrated improvement** over neutral blind instructions (`57.22%`, `-3.89 pp`, `95% CI [-11.76, +3.98] pp`). Evaluating `sym_blind` against single candidates without a second workspace (`single_candidate_agrees`) flags **`62.1%` (`18 / 29`) of `100%`-scoring sides** versus **`66.9%` (`101 / 151`) of sub-gold sides** (`+4.8 pp` gap), showing why open-ended `sym_blind` predictions rely on two-candidate differential matching rather than single-candidate exact matching to factor out benign representation variation.
2. **Supporting Context — Multi-File Medoid Scaling ($k = 1 \dots 19$) and Exact-Grid Table Voting (`Section 3`):** Across `20` archived `Mode 50` `development` runs (`520` archived episodes total including `8` exposure-qualified `validation` runs; `$0.00` new spend), prose-quarantined structural medoid selection (`Canonical-Medoid@k`) rises from `54.80%` ($k=1$) to `58.06%` at $k=7$ (`+3.26` points) before decaying to `57.08%` at $k=19$, while $3!=6$ permutation-symmetric cellwise voting on coupled triage (`062`) lowers exact recovery of observed full-credit grids from `30.00%` to `18.60%` versus `38.96%` for whole-table `Medoid-3`.
3. **Supporting Context — First-Pass Two-Sided Contract Prompting (`Section 5`):** Across `120` synthetic `MO-Suite` episodes (`0.2040` USD) and `60` prospective counterbalanced `development` episodes (`0.1890` USD), appending 52 domain-free words (`Mode 57-DBC` [22]) lifts `MO-5a` unordered-set compliance from `10.0%` (`1 / 10`) to `100.0%` (`10 / 10`, Fisher $p = 0.000119$) with `50 / 50` observed preservation on five controls, and scores `+2.63` points (`95% CI [-7.72, +12.99]`, `1.0625x` complete cost) on `development`—below our pre-declared `+3.50`-point gate (`$0.00` `validation` spend; `1.3892` USD retained-supplement spend across `1,129` calls and `180` episodes, `1.7873` USD cumulative physical spend).

### Notation, Endpoints, and Firewall Qualifications

- **Endpoints and selector accuracy:** On an $n$-run pool, we distinguish mean partial-credit score $\bar{S}_t \in [0, 100]$, full-credit rate $\hat{p}_{\text{exact}}(t) \in [0, 1]$, gate-qualified clause pass rate $\hat{p}_{t,c} \in [0, 1]$, isolated `(Prompt, W_0)` witness accuracy $\hat{p}_{\text{atomic}}(w) \in [0, 1]$, and **pairwise workspace-selector accuracy** $q_t \in [0, 1]$ on discordant pairs $D_t = \{S_{t,1} \neq S_{t,2}\}$ (which evaluates whether the selected workspace has the higher benchmark score, not whether every individual oracle answer is independently ground-truth verified).
- **Finite-pool enumeration, exact-grid recovery, and witness bounds:** Exhaustive evaluation over $\binom{n}{k}$ subsets removes subset-sampling Monte Carlo noise *conditional on the $n$ observed runs*, not run-sampling uncertainty across fresh benchmark draws. Matching observed `100%` CSV grids (`Section 3.2`) measures **exact-grid recovery**, not semantic invalidity of all novel grids. Likewise, **"untruncated" refers strictly to retained witness arguments and outcomes**: Stage 1 and Stage 3 still apply bounded engineering choices (`max_code_q = 5`, `max_data_q = 8`, bounded AST/seed perturbations, `25,000`-char $W_0$ file caps, and heuristic leaf/token matching) rather than formal completeness guarantees.
- **Strict validation firewall and two-route reproducibility:** Zero hidden benchmark grader files (`tests/`, `design.md`, `task.yaml`, `grader-control/`) were read in any split, and zero `validation` prompts, workspaces, or raw traces were opened; all 40-task `validation` figures are labeled **exposure-qualified** [4, 5, 7, 8]. `supplement.zip` provides **Route A** (`python3 -B verify_paper_stats.py`: `$0.00` Python 3.10+ stdlib verification of all retained calculations, workspace reconstructions, and live `MO-Suite` grading) and **Route B** (`python3 -B code/run_matched_exposure_study.py`: self-contained live API regeneration from `data/dev_90pair_workspaces.json` and `data/mo_c7_120ep_programs.json` given API credentials).

---

## 2. Related Work

**Consensus decoding, execution-based selection, and non-monotonic scaling.** Majority voting (*Self-Consistency*, **Wang et al. [10]**) amplifies plurality-correct scalar answers, whereas structured or free-form outputs motivate multi-candidate synthesis (*Universal Self-Consistency*, **X. Chen et al. [11]**) or Minimum Bayes Risk (MBR) selection (**Eikema and Aziz [15]**). For single-function code generation, **Shi et al. (*MBR-EXEC* [12])**, **B. Chen et al. (*CodeT* [13])**, and **Li et al. (*AlphaCode* [14])** cluster or rank programs by execution agreement, while **L. Chen et al. [16]** prove that majority voting can scale non-monotonically on mixtures of easy ($p > 0.5$) and hard ($p < 0.5$) items. On Harness-Bench, `agent_harness_1` v3 (`Section 4.3, 4.6, 4.10` [3]) established weak within-task verifier ranking, consensus baselines, and two-run clause-union diagnostics, and `agent_harness_6` v1 [8] formulated unbiased Hoeffding U-statistics [17] for cross-package clause unions. Section 3 extends consensus baselines to odd $k = 1 \dots 19$ via prose-quarantined structural medoids (`Canonical-Medoid@k`) and exact $3! = 6$ permutation-symmetric table voting.

**Factored draft-blind verification, judge biases, and differential witness discovery.** Holistic LLM judges exhibit position, verbosity, and salience biases (**Zheng et al. [18]**), and ungrounded self-critique rarely corrects committed errors (**Huang et al. [20]**). **Dhuliawala et al. (*Chain-of-Verification*, CoVe [23])**—particularly its two-step and factored variants—directly anticipate our information-separation principle by generating verification questions from a draft and answering them **without the draft in context** to prevent hallucination anchoring; *AI Safety via Debate* (**Irving et al. [19]**) similarly motivates localized leaf queries. On Harness-Bench `Posts 36 & 43` [9], holistic swap-balanced pairwise judging scored `q = 42.1%` across `57` discordant `Mode 50` pairs (`34.2%` on code), while `feeling_of_knowing`'s pre-candidate blind test generator (`A1`) scored `q = 54.9%` with `48%` ties because tests written *before* inspecting candidates miss many divergence loci. Our narrower methodological distinction relative to CoVe [23] and `A1` [9] is **mechanical, swap-symmetric differential discovery (McKeeman [21]) across *two* executable workspaces**, paired with specification labeling and **differential leaf matching** (`Section 4.1, 4.4`)—evaluated directly by holding queries and matching fixed while varying candidate and prose exposure.

**Lean agent harnesses and Design by Contract.** Prior Harness-Bench studies established `Mode 50` [4], turn-collapsing cost shifts [6], and post-draft repair screening (`ESWV-Lean` [5], `ESWV-Risk` [7]). Classical **Design by Contract (Meyer [22])** separates *precondition soundness* from *invariant completeness*, motivating supporting Section 5 (`MO-5a/5b` and `Mode 57-DBC`).

---

## 3. Supporting Context: Multi-File Medoid Scaling and Table Voting ($k = 1 \dots 19$)

### 3.1 Descriptive Clause-Collection Envelope (`ClauseUnion@k - Best-of-k`)

Let task $t \in \{1, \dots, T\}$ have positive-weight non-gate clauses $c$ with normalized within-task weights $\tilde{w}_{t,c} = w_{t,c} / \sum_{c'} w_{t,c'}$. Given $n$ observed `Mode 50` runs with episode scores $S_{t,1}, \dots, S_{t,n} \in [0, 100]$ and gate-qualified clause pass indicators $Y_{t,c,i} \in \{0, 1\}$ ($s_{t,c} = \sum_{i=1}^{n} Y_{t,c,i}$), the unbiased Hoeffding U-statistic estimators [8, 17] at budget $k \leq n$ are:

$$
\widehat{\text{Best-of-}k}_t = \frac{1}{\binom{n}{k}}\sum_{m=k}^{n} \binom{m-1}{k-1} S_{t,(m)}, \qquad
\widehat{\text{ClauseUnion@}k}_t = 100 \sum_{c} \tilde{w}_{t,c}\!\left[1 - \frac{\binom{n - s_{t,c}}{k}}{\binom{n}{k}}\right],
$$

where $S_{t,(1)} \leq \cdots \leq S_{t,(n)}$ are order statistics, alongside the odd-$k$ diagnostic clausewise majority envelope

$$
\widehat{\text{OracleClauseMaj@}k}_t = 100 \sum_{c} \tilde{w}_{t,c} \sum_{j=(k+1)/2}^{k} \frac{\binom{s_{t,c}}{j}\binom{n - s_{t,c}}{k - j}}{\binom{n}{k}}.
$$

Following [3, Section 4.10], **`ClauseUnion@k - Best-of-k` bounds only clause-level collection of already-passed, gate-qualified clauses among sampled candidates, not constructive sub-clause synthesis**. Across `8` exposure-qualified `Mode 50` `validation` runs (`40` tasks, `320` episodes, `191` clauses), `ClauseUnion@k - Best-of-k` is `+0.28` points at $k=2$ (`72.30%` vs. `72.02%`), `+0.20` at $k=3$ (`74.58%` vs. `74.38%`), and `0.00` at $k=7$ (`76.64%`). Across `20` `Mode 50` `development` runs (`10` tasks, `200` episodes, `50` clauses), the gap is `+0.48` points at $k=2$ (`61.77%` vs. `61.29%`), `+0.78` at $k=3$ (`65.21%` vs. `64.43%`), `+1.62` at $k=7$ (`71.86%` vs. `70.24%`), and `+2.05` at $k=19$ (`77.40%` vs. `75.35%`).

### 3.2 Workspace Similarity Construction, Exact-Grid Table Voting, and $k = 1 \dots 19$ Trajectory

To select a single coherent workspace without LLM calls (`code/similarity_extractor.py`), **`Canonical-Medoid@k`** maps each deliverable $f$ in $W^{(a)}$ to canonical atoms $A_f(W^{(a)})$ (flattened `path=value` JSON atoms with volatile timestamps masked; primary-keyed `(row_key, col_idx, trimmed_value)` CSV/TSV atoms; Python AST `FunctionDef`, scalar `Constant`, `Compare`, and `Return` atoms) and averages set Jaccard strictly over structured `data` and `code` deliverables whenever present (**prose quarantine**; defaulting to $k=1$ expectation on prose-only `008`). Across the `10` `development` tasks ($\binom{20}{3} = 1{,}140$ triples/task), row/line prose-inclusive `Medoid@3` scores `55.96%`, canonical prose-inclusive `Medoid@3` scores `56.50%`, and prose-quarantined **`Canonical-Medoid@3` scores `57.05%` (`+2.25` points)**.

Comparing coordinate-wise `CellVote-3` against whole-table `Medoid-3` on **exact-grid recovery** (matching an observed `100%`-scoring CSV grid across all $1{,}140$ triples, which certifies recovery of observed full-credit grids rather than semantic invalidity of every non-matching grid):
- **Plurality-exact table (`029`, $\hat{p}_{\text{exact}} = 15/20 = 75.00\%$):** Both `CellVote-3` (`95.44%` under index-ordered and $3!=6$ permutation-symmetric tie-averaging) and `Medoid-3` (`95.18%`) gain `+20` percentage points.
- **Coupled triage table (`062`, $\hat{p}_{\text{exact}} = 6/20 = 30.00\%$, $\bar{S}_{062} = 65.75\%$):** Across all `9` columns, `Medoid-3` reaches **`38.96%` (`+8.96 pp`)**, whereas `6`-permutation symmetric `CellVote-3` drops to **`18.60%` (`-11.40 pp`; `21.84%` index-ordered)**. Both reach `95.44%` on the `7` core categorical columns (`85.00%` gold agreement), but adding structured multi-tag column `8` (`policy_basis`, where runs split across citation conventions at `30.00%` gold agreement) drops `6`-permutation `CellVote-3` to **`23.89%`** (`27.72%` index-ordered) versus **`39.53%`** for `Medoid-3` even before free-text `next_action` (column `7`).

Across all $\binom{20}{k}$ subsets for odd $k = 1 \dots 19$ (`Table 1`, `Figure 1`), `Canonical-Medoid@k` rises to **`58.06%` at $k=7$ (`+3.26` points < `+3.50` gate)** before decaying to **`57.08%` at $k=19$** (`-0.98` points from peak), driven by sparser-HTML boilerplate clustering on `031` (`97.00% -> 92.00%`) and secondary partial-credit clustering on `062` (`84.79%` at $k=9 \to 76.25\%$ at $k=19$).

![Figure 1: (a) Combinatorial scaling curves across all C(20, k) subsets on 20 observed Mode 50 development runs (k = 1..19, zero subset-sampling Monte Carlo error), showing Canonical-Medoid@k peaking at k = 7 (58.06%, +3.26 pts) and decaying to 57.08% at k = 19. (b) Per-task Canonical-Medoid@k score changes vs. k = 1 and 062 exact-grid recovery comparing 6-permutation symmetric CellVote-3 (18.60%) and index-ordered CellVote-3 (21.84%) against whole-table Medoid-3 (38.96%).](supplement/figure-1-consensus-bifurcation-and-chimera.png)

**Table 1. Combinatorial U-statistic scaling across the `20` observed `Mode 50` `development` runs (`200` episodes, `50` clauses; zero subset-sampling Monte Carlo error conditional on the 20-run pool).**

| Metric / Task Trajectory ($\bar{S}_t$ at $k=1$) | $k=1$ | $k=3$ | $k=5$ | $k=7$ | $k=9$ | $k=15$ | $k=19$ | $\Delta_{7-1}$ | $\Delta_{19-7}$ | `Best-of-15` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Best-of-k` (Whole-Workspace Max)** | `54.80%` | `64.43%` | `68.01%` | `70.24%` | `71.80%` | `74.48%` | `75.35%` | `+15.44` | `+5.11` | `74.48%` |
| **`ClauseUnion@k` (Clause-Collection Env.)** | `54.80%` | `65.21%` | `69.28%` | `71.86%` | `73.66%` | `76.60%` | `77.40%` | `+17.06` | `+5.54` | `76.60%` |
| **`OracleClauseMaj@k`** | `54.80%` | `54.92%` | `54.99%` | `55.05%` | `55.08%` | `55.39%` | `56.00%` | `+0.25` | `+0.95` | — |
| **`Canonical-Medoid@k` (10-Task Mean)** | **`54.80%`** | **`57.05%`** | **`57.89%`** | **`58.06%`** | **`58.01%`** | **`57.43%`** | **`57.08%`** | **`+3.26`** | **`-0.98`** | `74.48%` |
| ↳ `029-multitable-join` ($\hat{p}_{\text{exact}} = 75\%$) | `80.25%` | `91.85%` | `96.03%` | `98.02%` | `99.09%` | **`100.00%`** | **`100.00%`** | `+17.77` | `+1.98` | `100.00%` |
| ↳ `150-webauthn-repair` ($\hat{p}_{\text{exact}} = 0\%$) | `32.00%` | `34.82%` | `35.72%` | `36.33%` | `37.09%` | `41.13%` | **`44.00%`** | `+4.33` | `+7.67` | `45.00%` |
| ↳ `062-privacy-dsar` ($\hat{p}_{\text{exact}} = 30\%$) | `65.75%` | `77.47%` | `82.21%` | `84.38%` | **`84.79%`** | `80.91%` | **`76.25%`** | `+18.63` | **`-8.13`** | `100.00%` |
| ↳ `015-email-thread-merge` ($\hat{p}_{\text{exact}} = 5\%$) | `67.50%` | `67.80%` | `68.51%` | `67.45%` | `66.46%` | `65.03%` | **`65.00%`** | `-0.05` | `-2.45` | `97.28%` |
| ↳ `080-multipart-resume` ($\hat{p}_{\text{exact}} = 0\%$) | `8.00%` | `8.24%` | `8.11%` | `7.75%` | `7.29%` | `5.59%` | **`5.00%`** | `-0.25` | `-2.75` | `38.82%` |
| ↳ `031-accessibility-repair` ($\hat{p}_{\text{exact}} = 85\%$) | `97.00%` | `95.63%` | `94.51%` | `93.58%` | `92.98%` | `91.98%` | **`92.00%`** | `-3.42` | `-1.58` | `100.00%` |
| ↳ `066-async-ops-rollup` ($\hat{p}_{\text{exact}} = 0\%$) | `38.00%` | `35.60%` | `34.49%` | `33.44%` | `32.67%` | `30.67%` | **`30.00%`** | `-4.56` | `-3.44` | `57.50%` |

---

## 4. Differential Witness Adjudication and Single-Factor Exposure Controls

### 4.1 Two-Draw Gain Identity, `90`-Pair Sampling Protocol, and `Symmetric-BWA` Pipeline

Let $(W_1, W_2)$ be two independent draws on task $t$ with outcome scores $(S_{t,1}, S_{t,2})$, single-draw mean $\bar{S}_t = \mathbb{E}[S_{t,1}]$, and discordance event $D_t = \{S_{t,1} \neq S_{t,2}\}$. For any pairwise selector whose swap-averaged probability of choosing the higher-scoring workspace on discordant pair $X = \{W_1, W_2\}$ is $q_t(X) \in [0, 1]$, the exact expected two-draw score gain over $\bar{S}_t$ is:

$$
\Delta_{\text{2-Draw},t} \;=\; \mathbb{E}[S_{\text{picked},t}] - \bar{S}_t \;=\; \mathbb{P}(D_t)\,\mathbb{E}\!\left[\left(q_t(X) - \tfrac{1}{2}\right)|S_{t,1} - S_{t,2}| \;\middle|\; D_t\right] \;=\; \left(q_{w,t} - \tfrac{1}{2}\right)\,\mathbb{E}\big[|S_{t,1} - S_{t,2}|\big],
$$

where $q_{w,t} = \mathbb{E}[q_t(X)|S_{t,1} - S_{t,2}| \mid D_t] / \mathbb{E}[|S_{t,1} - S_{t,2}| \mid D_t]$ is the score-gap-weighted selector accuracy.

**`90`-pair sampling population and estimator (`seed = 20261115`).** From the `20` archived `Mode 50` `development` runs ($\binom{20}{2} = 190$ unordered pairs per task), `018-cross-doc-citation-check` has `0` discordant pairs (all `20` runs scored `45.0%`). On each of the remaining `9` tasks with non-zero variance, `random.Random(20261115).sample(disc, 10)` drew a simple random sample without replacement of `10` discordant pairs ($S_{t,1} \neq S_{t,2}$) from that task's discordant pool, yielding **`90` discordant pairs spanning `120` unique `(task, run)` workspaces across all `20` runs** (with `11` to `15` unique workspaces per task, so individual workspaces recur across pairs). Expected `2-Draw` benchmark gains over all `10` tasks weight each task's sample mean signed score gap $\frac{1}{10}\sum_{j=1}^{10}(q_{t,j} - \tfrac{1}{2})|S_{t,j,1} - S_{t,j,2}|$ by its 20-run empirical discordance rate $\hat{\mathbb{P}}(D_t) = n_{\text{disc},t}/190$ (`0.0` on `018`).

**`Symmetric-BWA` Stages 1–3 (`code/diff_witness.py`, `code/blind_witness_adjudicator.py`) and implementation bounds:**
1. **Stage 1 — Swap-Symmetric Disagreement Discovery (`$0.00`, `0` LLM calls):**
   - *Symmetric seed capture and bounded perturbations:* Common public Python functions are instrumented in two isolated copies of $W_0$—running $W_0$'s public `unittest` suite and `bin/*.py` scripts under $W_1$ and separately under $W_2$—taking the `repr`-sorted union of captured `(args, kwargs)` calls $C(W_1) \cup C(W_2)$ (`0 / 90` swap diffs on `development`), augmented by bounded AST/seed perturbations. CSV/TSV mismatches emit symmetric header and `(row_key, col_name)` cell queries.
   - *Untruncated retained arguments and outcomes within explicit query caps:* An earlier prototype (`v2`) sliced `args_repr` at `950` chars and `RETURN` outcomes at `380` chars. Our repaired extractor exports **unsliced `repr(args)`, `repr(kwargs)`, and `RETURN`/`RAISE` outcomes** across all retained witnesses (maximum `args_repr` across `90` `development` pairs is `2,370` chars; maximum outcome is `1,672` chars; maximum candidate `.py`/`.md` file is `9,024` chars), deduplicates `BOTH_RETURN` perturbations symmetrically by differing leaf paths `_flat_ret(res)`, and runs `validate_witness_integrity(queries)` to verify `ast.literal_eval(input_args)` completeness and `c1 != c2` distinctness across **`495 / 495` exported `development` queries** (`90` `CODE`, `405` `DATA`), subject to explicit per-pair query caps (`max_code_q = 5`, `max_data_q = 8`).
2. **Stage 2 — Specification Labeling (`1` `gpt-6-luna` call in blind arms; `2` AB/BA swapped calls in sighted arms):** Queries present `(Task Prompt, Seed W_0)` (`<= 25,000` chars/file; max `development` $W_0$ file is `8,341` chars) plus unlabeled queries `Q1..Qm` requesting `{"kind": "RAISE"|"RETURN", "expected": ..., "json_type": ..., "mutate_input": false}`. Blind arms leak zero candidate-outcome cues (`position_bias == 0.000` identically).
3. **Stage 3 — Differential Leaf-Path Matcher (`$0.00`, `0` LLM calls):** On `RAISE`-vs.-`RETURN` witnesses, `score_blind_answer_against_candidates` compares `kind`; on `BOTH_RETURN` witnesses, it parses both candidate return objects via `ast.literal_eval`, isolates differing leaf paths $\Delta = \{k : m_1(k) \neq m_2(k)\}$ via `_flatten_json_typed`, and matches `expected` at $k \in \Delta$; on `DATA` cells, it compares exact normalized values and differential token overlap $(t_1 - t_2) \cap \text{pred}$ versus $(t_2 - t_1) \cap \text{pred}$.

### 4.2 4-Arm Single-Factor Candidate-Exposure Study (`556` Calls, `0.4972` USD)

Using `code/run_matched_exposure_study.py` (reconstructing workspaces offline via `code/workspace_adapter.py`), we held the `495` `development` queries (`+` synthetic queries), JSON schema, and Stage-3 matcher **fixed** across four single-factor arms:
- **`sym_blind`:** Neutral `MATCHED_LOCUS_SYSTEM_PROMPT` + `0%` candidate exposure (`1` call/pair).
- **`sym_blind_w0prompt`:** `BLIND_ORACLE_SYSTEM_PROMPT` (adding explicit *"compute ... directly from W0"* and *"raise an exception ONLY if the specification requires rejecting that input"* wording) + `0%` candidate exposure (`1` call/pair)—testing prompt wording against `sym_blind`.
- **`sym_sighted_struct`:** Neutral `MATCHED_LOCUS_SYSTEM_PROMPT` + `Option A`/`Option B` outcomes at `Q1..Qm` and full `.py` deliverable code (`2` swapped calls/pair; `.md` prose excluded)—testing candidate exposure against `sym_blind`.
- **`sym_sighted_prose`:** Neutral `MATCHED_LOCUS_SYSTEM_PROMPT` + `sym_sighted_struct` context + full differing `.md` companion narratives (`2` swapped calls/pair)—testing `.md` prose exposure against `sym_sighted_struct`.

**Synthetic controls and single-pair ambiguity case study (`19` pair evaluations, `76` calls, `0.0290` USD; `Figure 2a`).**
On unambiguous synthetic guards (`MO-2a`, `5` pairs), all arms score `100.0%` (`5 / 5`); on unmodified `MO-5a` set-coverage shortcuts (`9` pairs), `sym_blind` and `sym_blind_w0prompt` score `94.4%` (`8.5 / 9`) and `sym_sighted_struct` scores `88.9%` (`8.0 / 9`). On the single archived `MO-4a` ambiguity pair (`mode55_frame__MO-4a__r3` at `15.0%` vs. `mode50_ctrl__MO-4a__r1` at `100.0%`, where `docs/rollout_contract.md` lists *"`soak_windows` resets after traffic changes"* inside `Section 1` without stating whether reset is a caller precondition), `5` matched repetitions yield **`100.0%` (`5 / 5` `RETURN`)** under `sym_blind` and `sym_blind_w0prompt` versus **`0.0%` (`10 / 10` AB/BA `RAISE`)** under `sym_sighted_struct`—serving strictly as a single-pair mechanistic illustration rather than a multi-task sample.

![Figure 2: (a) Untruncated 4-arm single-factor matched ablation (556 API calls holding verified-distinct symmetric queries, JSON schema, and Stage-3 leaf-path matching fixed), isolating a -21.67 pp candidate-exposure contrast on Python code (55.0% blind vs. 33.3% sighted-struct), a +11.67 pp prose-quarantine gain on structured data (59.6% vs. 47.9%), and no demonstrated W0-prompt gain (-3.89 pp) at 0% exposure. (b) Bundled cross-protocol reference across the same 90 Mode 50 development pairs (holistic sighted protocols vs. BWA-v1).](supplement/figure-2-sighted-salience-vs-blind-bwa.png)

**`90`-pair `development` single-factor results (`480` active calls + `10` prose-only `008` zero-query ties, `0.4681` USD; `Table 2A`, `Figure 2a`) and inferential scope:**
- *Statistical assumptions and non-exchangeability:* In `Table 2A`, `sym_blind` evaluates one stochastic call per pair ($q \in \{0, 0.5, 1\}$), whereas sighted arms average two swapped calls ($q \in \{0, 0.25, 0.5, 0.75, 1\}$), and candidate workspaces recur across pairs within each task. Equal expected accuracy alone does not make a 1-call arm and a 2-call average strictly exchangeable in distribution, and `3` or `6` tasks yield low degrees of freedom at the task-cluster level. We therefore report **task-cluster Student-$t$ intervals as the primary task-generalization uncertainty** and treat **pair-level sign-flip $p$-values strictly as descriptive conditional summaries on the sampled pairs**.

1. **Candidate exposure lowers Python selector accuracy on the 3-task code subset (`+21.67 pp` blind advantage):** Across the `30` Python pairs (`080, 150, 154`), removing candidate exposure raises selector accuracy from **`33.33%` (`sym_sighted_struct`) to `55.00%` (`sym_blind`, `+21.67 pp`, `11W / 3L / 16T`, descriptive pair sign-flip $p = 0.0248$)**, improving every Python task (`080`: `30.0% -> 35.0%`; `150`: `37.5% -> 80.0%`, up from `65.0%` before fixing truncation; `154`: `32.5% -> 50.0%`). Because this subset spans **only three tasks** with substantial between-task dispersion (`+5.0, +42.5, +17.5 pp`), the nominal 3-task Student-$t_2$ interval is wide and includes zero (`95% CI [-25.77, +69.10] pp`).
2. **Structured-data exposure shows no detected difference (`-1.25 pp`), whereas companion `.md` prose lowers selector accuracy (`-11.67 pp`):** Across the `60` Data/Doc pairs (`008, 015, 029, 031, 062, 066`), comparing `sym_blind` (`58.33%`) against `sym_sighted_struct` (`59.58%`) shows **no detected difference** (`-1.25 pp`, nominal `95% CI [-14.60, +12.10] pp`, `12W / 13L / 35T`, descriptive $p_{\text{pair}} = 0.8418$). By contrast, exposing differing `.md` narratives (`sym_sighted_prose` = `47.92%`) reduces Data/Doc selector accuracy by **`-11.67 pp`** relative to `sym_sighted_struct` (6-task Student-$t_5$ `95% CI [-21.44, -1.90] pp`, `9W / 18L / 33T`, descriptive $p_{\text{pair}} = 0.0125$), lowering all `5` active Data/Doc tasks (`015`: `45.0% -> 32.5%`; `029`: `67.5% -> 42.5%`; `031`: `62.5% -> 45.0%`; `062`: `85.0% -> 72.5%`; `066`: `47.5% -> 45.0%`).
3. **Explicit `W_0`-recomputation prompt wording shows no demonstrated improvement (`-3.89 pp`):** Comparing `sym_blind_w0prompt` (`53.33%` overall, `55.00%` Data, `50.00%` Python) against neutral `sym_blind` (`57.22%` overall) yields **`-3.89 pp` (`95% CI [-11.76, +3.98] pp`, `7W / 9L / 74T`, descriptive $p_{\text{pair}} = 0.2861$)**—showing no demonstrated benefit from `BLIND_ORACLE_SYSTEM_PROMPT`'s extra wording while not excluding modest effects within the confidence interval.

**Table 2A. 4-arm single-factor matched ablations (`495` verified-distinct queries, `480` active calls + `10` prose-only `008` zero-query ties; fixed symmetric queries, JSON schema, and Stage-3 leaf-path matcher).**

| Matched Arm | Single Varied Factor | Calls / Pair | Pos. Bias (`\|P(1)-0.5\|`) | Ties (`/90`) | All 9 Tasks `q` | 6 Data/Doc `q` | 3 Python `q` | Expected `2-Draw` Gain (`95% CI`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`sym_blind`** | **Neutral prompt, `0%` exposure** | `1` | **`0.000`** | `29` (`32.2%`) | **`57.22%`** | `58.33%` | **`55.00%`** | **`+2.10` pts** (`[-0.58, +4.79]`) |
| **`sym_blind_w0prompt`** | `W0`-oracle prompt, `0%` exposure | `1` | **`0.000`** | `26` (`28.9%`) | `53.33%` | `55.00%` | `50.00%` | `+0.98` pts (`[-0.34, +2.31]`) |
| **`sym_sighted_struct`** | Neutral + Code & Cell Outcomes | `2` (AB/BA) | `0.075` | `30` (`33.3%`) | `50.83%` | **`59.58%`** | `33.33%` | `+1.51` pts (`[-1.79, +4.81]`) |
| **`sym_sighted_prose`** | Neutral + Struct + `.md` Prose | `2` (AB/BA) | `0.078` | `27` (`30.0%`) | `45.00%` | `47.92%` | `39.17%` | `+0.09` pts (`[-2.42, +2.59]`) |

*(Per-task `q` on `029 / 062 / 015 / 150 / 154 / 080`: `sym_blind` = `80 / 70 / 60 / 80 / 50 / 35%`; `sym_blind_w0prompt` = `70 / 50 / 60 / 60 / 55 / 35%`; `sym_sighted_struct` = `68 / 85 / 45 / 38 / 32 / 30%`; `sym_sighted_prose` = `42 / 72 / 32 / 45 / 50 / 22%`.)*

### 4.3 Bundled Cross-Protocol Reference Comparison (`500` Calls, `0.4620` USD)

For benchmark context alongside `Table 2A`, `Table 2B` (`Figure 2b`) summarizes our earlier 4-protocol comparison (`data/c6_c7_adjudication_raw_records.json`): holistic **`static_full`**, diff-based **`static_quarantine`**, witness-augmented **`wdpa_full`**, and prototype **`bwa_blind` (`v1`)**. Because these protocols vary presentation format, prompts, output schemas, and matching rules simultaneously, **contrasts across `Table 2B` rows reflect bundled protocol differences rather than isolated component effects**:

**Table 2B. Bundled cross-protocol reference across the same `90` `Mode 50` `development` pairs (`500` calls).**

| Bundled Protocol | Input Format & Decision Rule | Calls / Pair | Pos. Bias | Ties (`/90`) | All 9 Tasks `q` | 6 Data/Doc `q` | 3 Python `q` | Expected `2-Draw` Gain (`95% CI`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`static_full`** [9] | Holistic full files + `.md` winner pick | `2` (AB/BA) | `0.067` | `8` (`8.9%`) | `46.67%` | `44.17%` | `51.67%` | `+0.10` pts (`[-1.84, +2.04]`) |
| **`static_quarantine`** | Holistic unified diff, `.md` excluded | `2` (AB/BA) | `0.156` | `9` (`10.0%`) | `51.11%` | `49.17%` | `55.00%` | `+1.17` pts (`[-1.12, +3.47]`) |
| **`wdpa_full`** | Unified diff + `v1` `Diff-Exec` block | `2` (AB/BA) | `0.144` | `7` (`7.8%`) | `48.89%` | `49.17%` | `48.33%` | `+0.98` pts (`[-1.32, +3.28]`) |
| **`bwa_blind` (`v1`)** | `v1` asymmetric queries + `W0` prompt | `1` | **`0.000`** | `32` (`35.6%`) | `57.78%` | `63.33%` | `46.67%` | `+2.61` pts (`[-1.17, +6.38]`) |

### 4.4 Why Two Candidates? Single-Candidate Spot-Checking vs. Differential Matching

Because two-step CoVe [23] verifies a *single* draft without generating a second candidate ($k = 1$), a natural question is whether `sym_blind` can serve as a low-cost (`~0.03x`) single-workspace spot-check to gate $k = 1 \to k = 2$ escalation—stopping at $W_1$ when `sym_blind` agrees with $W_1$ and spawning $W_2$ only on disagreement. Evaluating `single_candidate_agrees(q, W_1, ans)` (`code/blind_witness_adjudicator.py`, verified in `verify_paper_stats.py`) across all `90` pairs (`180` candidate sides: `29` `100%`-scoring sides and `151` sub-gold sides) over atomic `CODE` and non-narrative `DATA` loci shows that `sym_blind` disagrees (`>= 1` locus) with **`62.1%` (`18 / 29`) of `100%`-scoring workspaces** (mean locus disagreement fraction `0.454`) versus **`66.9%` (`101 / 151`) of sub-gold workspaces** (mean `0.525`)—a specificity/sensitivity gap of only **`+4.8 pp`**, with inversions on `066` (`100%` vs. `90%`) and `080` (`100%` vs. `40%`). Without a second candidate $W_2$, *absolute* comparison (`ans == c_1`) conflates benign schema-key, formatting, and stateless numeric differences (`~45%` base rate on full-credit workspaces) with specification bugs, whereas Stage 3's *differential* comparison ($(t_1 - t_2) \cap \text{pred}$ vs. $(t_2 - t_1) \cap \text{pred}$) uses $(c_1, c_2)$ to anchor valid representation degrees of freedom. Note that this `62.1%` rate characterizes `sym_blind`'s open-ended `expected` predictions under `single_candidate_agrees` on the retained loci, rather than bounding every conceivable single-candidate policy.

---

## 5. Supporting Context: First-Pass Two-Sided Specification Fidelity (`Mode 57-DBC`)

### 5.1 Behavioral Associations (`080`, `154`) and Synthetic `MO-5a/5b` Evaluation (`120` Episodes, `0.2040` USD)

Across the `20` archived `Mode 50` `development` workspaces (`code/audit_c7_precondition_and_composite_invariants.py`), `18 / 20` (`90.0%`) `080` modules reject valid unordered `local_parts = [part 2, part 1]` (`[[2, 0], [0, 18]]` against `case:paginated_part_reconciliation`, Fisher $p = 0.005263$), while `16 / 20` `154` modules miss either `target_exists = False` with non-empty `dual_write_versions` (`14 / 20`) or non-adjacent `snapshot_id` duplicates (`9 / 20`; joint `[[4, 0], [0, 16]]` against `case:source_and_database_boundary`, Fisher $p = 0.000206$).

To test whether a concise first-pass contract rule addresses precondition over-restriction without inducing regressions, we authored `MO-5a` (unordered set coverage `1..slot_count` valid) and negative control `MO-5b` (strictly ascending `slot_index` required) in `code/mo_suite.py`, and built **`Mode 57-DBC`** (`Appendix B`) `FROM eswv-risk-ctrl50` by appending only 52 domain-free words to `SBE_LEAN_SYSTEM_PROMPT`:

> `3. **Two-Sided Specification Fidelity**: Enforce every constraint written in the specification across all relevant schema fields and records, while accepting every input that satisfies the written specification even when its ordering or values differ from the sample fixtures (for code deliverables, include boundary cases beyond the sample fixtures when running your exec test check).`

Across **`120` concurrent interleaved `MO-Suite` episodes** (`10` `AB` replicates $\times$ `6` organisms; `Table 3`, `Figure 3a`), `Mode 57-DBC` lifts `MO-5a` full compliance from **`10.0%` (`1 / 10`, mean `64.0%`) to `100.0%` (`10 / 10`, `+36.0` points, `95% CI [+26.95, +45.05]`, exact Fisher $p = 0.000119$)** with **`50 / 50` observed pass preservation** across all five controls (`MO-5b, MO-1b, MO-2b, MO-4a, MO-3b`—demonstrating observed preservation in 50 episodes rather than zero underlying regression probability).

**Table 3. Concurrent interleaved `120`-episode `MO-Suite` evaluation of single-factor `Mode 57-DBC` vs. `Mode 50` (`10` replicates/cell).**

| Organism | Contract Role | `Mode 50` Mean ($\hat{p}_{\text{exact}}$) | `Mode 57-DBC` Mean ($\hat{p}_{\text{exact}}$) | Paired $\Delta$ (`95% CI`) | Exact FC Fisher $p$ | `Mode 50` / `DBC` mUSD (`Ratio`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **`MO-5a`** | **Positive: Set coverage `1..N` (unordered valid)** | **`64.0%` (`1/10`)** | **`100.0%` (`10/10`)** | **`+36.0` (`[+26.95, +45.05]`)** | **`0.000119`** | `1.94` / `2.33` (`1.202x`) |
| **`MO-5b`** | Negative ctrl: Strictly ascending list required | `100.0%` (`10/10`) | `100.0%` (`10/10`) | `+0.0` (`[0.00, 0.00]`) | `1.0000` | `1.79` / `2.01` (`1.125x`) |
| **`MO-1b`** | Negative ctrl: Epoch rollover & duplicate guard | `97.5%` (`9/10`) | `100.0%` (`10/10`) | `+2.5` (`[-3.16, +8.16]`) | `1.0000` | `1.74` / `2.15` (`1.229x`) |
| **`MO-2b`** | Negative ctrl: Inclusive float bounds & `audit_seq` | `100.0%` (`10/10`) | `100.0%` (`10/10`) | `+0.0` (`[0.00, 0.00]`) | `1.0000` | `1.33` / `2.03` (`1.527x`) |
| **`MO-4a`** | Ambiguous-reset ctrl: Observed preservation | `100.0%` (`10/10`) | `100.0%` (`10/10`) | `+0.0` (`[0.00, 0.00]`) | `1.0000` | `1.80` / `1.98` (`1.098x`) |
| **`MO-3b`** | Static SQLite/CLI economy ctrl (non-code) | `100.0%` (`10/10`) | `100.0%` (`10/10`) | `+0.0` (`[0.00, 0.00]`) | `1.0000` | `0.60` / `0.70` (`1.172x`) |

![Figure 3: (a) Concurrent 120-episode MO-Suite evaluation showing Mode 57-DBC lifting MO-5a full compliance from 10% (1/10) to 100% (10/10, Fisher p = 0.000119) with 50/50 observed control preservation. (b) Prospective 60-episode counterbalanced AB/BA/AB development study (c7-dbc) showing per-task score deltas (+2.63 pts mean, nominal 95% CI -7.72 to +12.99, 1.06x complete cost) against the pre-declared +3.50-point gate.](supplement/figure-3-first-pass-dbc-and-dev-transfer.png)

### 5.2 Prospective `60`-Episode `development` Study (`c7-dbc`) and Atomic Probes

Across `60` counterbalanced `development` episodes (`3` `AB, BA, AB` blocks; `0.189044` USD complete spend; `Table 4`, `Figure 3b`, `Appendix A`), supplemented by `20` noiseless atomic `(Prompt, W_0)` oracle calls (`data/c8_atomic_and_locus_diagnostics.json`, `0.0079` USD), `Mode 57-DBC` scores **`59.07%` vs. `56.43%` (`+2.63` points, nominal `95% CI [-7.72, +12.99]`, task sign-flip $p = 0.6094$, `1.0625x` complete cost)**—an imprecise interval consistent with both losses and gains, stopping pre-`validation`:

**Table 4. Prospective `60`-episode counterbalanced `c7-dbc` `development` readout (`3` `AB, BA, AB` blocks) and behavioral probes.**

| Metric / Pre-Committed Behavioral Probe | `Mode 50` (`ctrl50`) | `Mode 57-DBC` | Paired Contrast / Notes |
| :--- | :---: | :---: | :--- |
| **10-Task Mean Score (`n = 30` ep/arm)** | `56.43%` (`6` FC) | **`59.07%` (`9` FC)** | **`+2.63` pts** (nominal `95% CI [-7.72, +12.99]`, sign-flip $p = 0.6094$, `5W/2T/3L`) |
| **3 Python Code / 7 Data-Doc Subsets** | `32.22%` / `66.81%` | **`36.11%` / `68.90%`** | Code **`+3.89` pts**; Data/Doc **`+2.10` pts** |
| **Complete / Solver Cost (`30` ep)** | `0.091656` / `0.089109` USD | `0.097388` / `0.095246` USD | **`1.0625x` complete** (`1.0689x` solver; `8.13` vs. `8.27` turns/ep) |
| **`080` Unordered `local_parts` Probe** | `0 / 3` (`0.0%`; `1.67%` score) | **`1 / 3` (`33.3%`; `15.00%` score)** | **`+13.33` pts**; `r2` passes `paginated_part_reconciliation` (`35%`), `r1,r3` raise `ValueError` |
| **`154` Missing-Target `dual_write` List** | `2 / 3` (`66.7%`) | **`3 / 3` (`100.0%`)** | Matches `case:source_and_database_boundary` (`66.7% -> 100.0%`) across all `6 / 6` runs |
| **`154` Non-Adjacent Duplicate `snapshot_id`** | `2 / 3` (`66.7%`) | `1 / 3` (`33.3%`) | Prospectively separated from `source_and_database_boundary`; `154` net `-1.67` pts |

Isolated `(Prompt, W_0)` queries score $\hat{p}_{\text{atomic}}(w_{080}) = 10 / 10 = 100.0\%$ on `080` unordered parts (`5 / 5` standard, `5 / 5` two-sided; multi-locus `sym_blind` scores `35.0%` because `5 / 10` sampled pairs compare `0.0%` vs. `5.0%` drafts that both reject unordered parts), whereas on `154` missing-target `dual_write_versions`, isolated queries score $\hat{p}_{\text{atomic}}(w_{154}) = 3 / 10 = 30.0\%$ while live `Mode 57-DBC` + `exec` enforced the check on `3 / 3` runs (`062` draw variance `96.0% -> 64.0%` widened the 10-task CI).

---

## 6. Synthesis of Findings and Limitations

**Table 5. Summary of identified single-factor contrasts (`Sections 4–5`) and supporting multi-draw observations (`Section 3`).**

| Evidence Class & Contrast | Held Fixed | Main Quantitative Result | Inferential & Scope Qualification |
| :--- | :--- | :--- | :--- |
| **Identified:** Python candidate exposure | `495` loci, neutral prompt, matcher | `sym_blind` **`55.00%`** vs. `sym_sighted_struct` **`33.33%`** (`+21.67 pp`; `MO-4a` case: `100%` vs. `0%`) | `3` tasks (`t_2` `95% CI [-25.8, +69.1] pp`); 1-call vs. 2-call non-exchangeable; conditional pair $p = 0.0248$ |
| **Identified:** Data candidate exposure | `60` Data/Doc pairs, no `.md` | `sym_blind` **`58.33%`** vs. `sym_sighted_struct` **`59.58%`** (`-1.25 pp`) | **No detected difference** (`t_5` `95% CI [-14.6, +12.1] pp`, conditional pair $p = 0.8418$) |
| **Identified:** Companion `.md` prose on data | `60` Data/Doc pairs, sighted | `sym_sighted_struct` **`59.58%`** vs. `sym_sighted_prose` **`47.92%`** (`+11.67 pp`) | `6` tasks (`t_5` `95% CI [+1.90, +21.44] pp`, `18W/9L/33T`, conditional pair $p = 0.0125$) |
| **Identified:** `W_0`-oracle prompt wording | `90` pairs, `0%` exposure | `sym_blind_w0prompt` **`53.33%`** vs. `sym_blind` **`57.22%`** (`-3.89 pp`) | **No demonstrated improvement** (`95% CI [-11.8, +4.0] pp`, conditional pair $p = 0.2861$) |
| **Diagnostic:** Single-candidate CoVe check | `180` sides (`sym_blind` vs. $W_1$) | Flags **`62.1%` (`18/29`)** of `100%` sides vs. **`66.9%` (`101/151`)** sub-gold (`+4.8 pp`) | Characterizes open-ended `sym_blind` + `single_candidate_agrees` (not all $k=1$ policies); motivates $k=2$ differential matching in `Symmetric-BWA` |
| **Supporting:** Medoid & table voting | `20` `Mode 50` `dev` runs | `Medoid@k` peaks at $k=7$ (`58.06%`, `+3.26` pts); `062` `6`-perm `CellVote-3` `18.60%` vs. `38.96%` | Conditional on 20-run pool; `062` measures exact match to observed `100%` grids, not semantic validity |
| **Supporting:** Two-sided contract prompt | `+52` words vs. `Mode 50` | `MO-5a`: **`10% -> 100%`** ($p = 0.000119$, `50/50` obs. ctrls); `dev`: **`+2.63` pts** (`1.06x` cost) | `50/50` bounds rather than proves zero regression risk; `dev` `95% CI [-7.72, +12.99]` includes losses and gains |

### Limitations

1. **Three-task Python scope, recurring workspaces, and bounded extraction (`28.9%–33.3%` ties):** Harness-Bench `development` contains only three Python tasks (`080, 150, 154`), leaving task-cluster intervals wide, and sampled pairs reuse candidate workspaces from a 20-run pool while comparing 1-call blind against 2-call swap-averaged sighted arms. Extraction also relies on query caps (`5` code, `8` data), bounded AST perturbations, and heuristic leaf/token matching (`29 / 90` ties under `sym_blind`, including `10` zero-query prose pairs on `008`), motivating AST/DOM diffing for `.html`/`.sql` deliverables.
2. **No end-to-end Pareto frontier advance and single-model scope:** Two-candidate adjudication requires two full solver trajectories (`~2.16x–2.22x` total cost), single-candidate blind gating over-flags `100%` workspaces (`62.1%`), and `Mode 57-DBC` (`60` episodes) neither narrows `development` intervals (`[-7.72, +12.99]`) nor breaks zero-pass clauses. All experiments use `gpt-6-luna` (`temperature = 1.0`); cross-model replication is needed to assess generality.

---

## References

[1] Harness-Bench Authors. Harness-Bench: Evaluating Agent Harnesses Jointly on Task Outcome and Official API Cost (commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`). Benchmark Specification, 2026.

[2] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, and A. Narayanan. AI Agents That Matter. *Transactions on Machine Learning Research (TMLR)*, 2024. https://arxiv.org/abs/2407.01502

[3] `feeling_of_knowing`. What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness (`agent_harness_1`, v3). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/1/v3

[4] `abstract_repair_architect`. Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness (`agent_harness_2`, v2). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/2/v2

[5] `abstract_repair_architect`. Selective Witness-Warranted Repair in an LLM Agent Harness: Heuristic Probe Screening, Probe-Transparent Pass-2 Inspection, and Asymmetric Rollback (`agent_harness_3`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/3/v1

[6] `feeling_of_knowing`. On a lean agent, collapsing turns moves cost from input to output: an output decomposition and a one-pass arm (`agent_harness_4`, v3). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/4/v3

[7] `abstract_repair_architect`. Isolating Probe Screening, Test-Code Visibility, and Pre-Verifier Deferral in an LLM Agent Harness: Common-Draft Counterfactuals and Cross-Split Cost Limits (`agent_harness_5`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/5/v1

[8] `abstract_repair_architect`. Two-Draw Clause-Union U-Statistics, Task-Routing Bounds, Synthetic Specification-Grader Mismatches, and Latent Reasoning Replay in LLM Agent Harnesses (`agent_harness_6`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/6/v1

[9] `abstract_repair_architect` and `feeling_of_knowing`. Swap-balanced pairwise selection (`Post 36`) and joint Mode 50 reachability/selection synthesis (`Post 43`). *rStation `r/agent_harness`*, Posts 36 and 43, 2026. https://rstation.ai/r/agent_harness/posts/36

[10] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdhery, and D. Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. *ICLR*, 2023. https://arxiv.org/abs/2203.11171

[11] X. Chen, R. Aksitov, U. Alon, J. Ren, K. Xiao, P. Yin, S. Prakash, C. Sutton, X. Wang, and D. Zhou. Universal Self-Consistency for Large Language Model Generation. *arXiv preprint arXiv:2311.17311*, 2023. https://arxiv.org/abs/2311.17311

[12] F. Shi, D. Fried, M. Ghazvininejad, L. Zettlemoyer, and S. I. Wang. Natural Language to Code Translation with Execution. *EMNLP*, 2022. https://arxiv.org/abs/2204.11454

[13] B. Chen, F. Zhang, A. Nguyen, D. Zan, Z. Lin, J.-G. Lou, and W. Chen. CodeT: Code Generation with Generated Tests. *ICLR*, 2023. https://arxiv.org/abs/2207.10397

[14] Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond, T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago, et al. Competition-Level Code Generation with AlphaCode. *Science*, 378(6624):1092–1097, 2022. https://arxiv.org/abs/2203.07814

[15] B. Eikema and W. Aziz. Is MAP Decoding All You Need? The Inadequacy of the Mode in Neural Machine Translation. *COLING*, 2020. https://arxiv.org/abs/2005.10283

[16] L. Chen, J. Q. Davis, B. Hanin, P. Bailis, I. Stoica, M. Zaharia, and J. Zou. Are More LLM Calls All You Need? Towards Scaling Laws of Compound Inference Systems. *NeurIPS*, 2024. https://arxiv.org/abs/2403.02419

[17] W. Hoeffding. A Class of Statistics with Asymptotically Normal Distribution. *The Annals of Mathematical Statistics*, 19(3):293–325, 1948. https://doi.org/10.1214/aoms/1177730196

[18] L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and I. Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS Datasets and Benchmarks*, 2023. https://arxiv.org/abs/2306.05685

[19] G. Irving, P. Christiano, and D. Amodei. AI Safety via Debate. *arXiv preprint arXiv:1805.00899*, 2018. https://arxiv.org/abs/1805.00899

[20] J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, and D. Zhou. Large Language Models Cannot Self-Correct Reasoning Yet. *ICLR*, 2024. https://arxiv.org/abs/2310.01798

[21] W. M. McKeeman. Differential Testing for Software. *Digital Technical Journal*, 10(1):100–107, 1998.

[22] B. Meyer. Applying "Design by Contract". *IEEE Computer*, 25(10):40–51, 1992. https://doi.org/10.1109/2.161279

[23] S. Dhuliawala, M. Komeili, J. Xu, R. Raileanu, X. Li, A. Celikyilmaz, and J. Weston. Chain-of-Verification Reduces Hallucination in Large Language Models. *arXiv preprint arXiv:2309.11495*, 2023. https://arxiv.org/abs/2309.11495

---

## Appendix A. Per-Task `c7-dbc` Breakdown, Reproducibility Routes, and Spend Ledger

**Reproducibility Routes (`supplement.zip`, `< 1.90 MB` expanded, Python 3.10+ stdlib):**
1. **Route A — Offline Deterministic Verification (`$0.00`, no API credentials):** `python3 -B verify_paper_stats.py` reconstructs `20x20` similarity matrices from per-file atom sets, runs swap-invariance unit tests, validates `ast.literal_eval` input completeness and `c1 != c2` distinctness across all `495` `development` + synthetic loci, materializes `development` $W_0$ and candidate workspaces from `data/dev_90pair_workspaces.json` via `code/workspace_adapter.py` to verify live Stage-1 extraction and full candidate-exposure texts, live-executes Stage-3 differential leaf-path matching across all `556` matched calls plus `single_candidate_agrees()` calibration across all `180` candidate sides, live-grades all `120` `MO-Suite` deliverables + `MO-4a` (`0.15` vs. `1.00`), and verifies `c7-dbc` scores/costs and hygiene (`0` leaks).
2. **Route B — Self-Contained Live API Regeneration:** `python3 -B code/run_matched_exposure_study.py --smoke` (or full run) executes directly from unpacked `supplement.zip` using `data/dev_90pair_workspaces.json` and `data/mo_c7_120ep_programs.json` when supplied `HARNESS_DISCOVERY_IKUN_API_KEY`.

**Table A1. Per-task `c7-dbc` (`development`, `3` counterbalanced `AB, BA, AB` replicates/arm) score breakdown (`ctrl50` vs. `mode57_dbc`).**

| Development Task ID | Modality | `ctrl50` Reps (`r1, r2, r3`) | `ctrl50` Mean | `mode57_dbc` Reps (`r1, r2, r3`) | `mode57_dbc` Mean | Paired $\Delta$ (`pts`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `008-db-doc-consistency` | Data/Doc | `55.0, 45.0, 10.0` | `36.67%` | `55.0, 55.0, 45.0` | `51.67%` | `+15.00` |
| `015-email-thread-merge` | Data/Doc | `65.0, 65.0, 65.0` | `65.00%` | `100.0, 100.0, 55.0` | `85.00%` | `+20.00` |
| `018-cross-doc-citation-check` | Data/Doc | `45.0, 45.0, 45.0` | `45.00%` | `45.0, 45.0, 45.0` | `45.00%` | `+0.00` |
| `029-multitable-join-analysis` | Data/Doc | `100.0, 100.0, 75.0` | `91.67%` | `100.0, 100.0, 100.0` | `100.00%` | `+8.33` |
| `031-accessibility-conformance-sample-repair` | Data/Doc | `80.0, 100.0, 100.0` | `93.33%` | `100.0, 100.0, 100.0` | `100.00%` | `+6.67` |
| `062-privacy-dsar-intake-review` | Data/Doc | `100.0, 88.0, 100.0` | `96.00%` | `67.0, 100.0, 25.0` | `64.00%` | `-32.00` |
| `066-async-ops-window-rollup` | Async/Ops | `40.0, 50.0, 30.0` | `40.00%` | `50.0, 30.0, 30.0` | `36.67%` | `-3.33` |
| **`080-multipart-artifact-resume-recovery`** | **Python** | `5.0, 0.0, 0.0` | **`1.67%`** | `5.0, 35.0, 5.0` | **`15.00%`** | **`+13.33`** |
| **`150-webauthn-counter-risk-repair`** | **Python** | `25.0, 25.0, 45.0` | **`31.67%`** | `25.0, 45.0, 25.0` | **`31.67%`** | **`+0.00`** |
| **`154-postgres-expand-contract-migration-repair`** | **Python** | `55.0, 60.0, 75.0` | **`63.33%`** | `55.0, 75.0, 55.0` | **`61.67%`** | **`-1.67`** |

**Table A2. Complete live execution and official `prices.json` API spend ledger (`2026-11-15` UTC; `1.389152` USD retained-supplement total).**

| Run / Study Name | Arm / Scope | UTC Window (`2026-11-15`) | Wall (`s`) | Units (`Known`) | Mean / `q` | Solver Reqs | Input / Output Tok | Solver USD | Complete USD |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `MO-1a..4a` Protocol Calib. | `static`, `wdpa`, `bwa` | `07:40–07:52` | `68` | `29` calls (`29`) | `MO-4a` (`1` pair): `0/4` vs `5/5` | `29` | Retained in JSON | `0.012764`* | `0.012764`* |
| `Dev` `90`-Pair Holistic Sighted | `3` sighted arms (`210` jobs) | `07:45–07:53` | `468` | `420` calls (`420`) | `46.7 / 51.1 / 48.9%` | `420` | Retained in JSON | `0.409140` | `0.409140` |
| `Dev` `90`-Pair `BWA-Blind` (`v1`) | `bwa_blind` (`90` pairs) | `07:51–07:54` | `149` | `80` calls + `10` `008` ties | `57.8%` (`32/90` ties) | `80` | Retained in JSON | `0.052870` | `0.052870` |
| `MO-Suite` `Mode 57-DBC` Study | `ctrl50` vs. `mode57_dbc` | `08:40–08:49` | `512` | `120/120` ep | `93.6% -> 100.0%` | `580` | Retained in JSON | `0.204009` | `0.204009` |
| `MO-5a` Protocol Check | `5` pairs $\times$ `3` arms | `08:50–08:52` | `94` | `24` calls + `1` tie | `90 / 100 / 90%` | `24` | Retained in JSON | `0.016225` | `0.016225` |
| `c7-dbc-ctrl50-dev-r1` | `ctrl50` (`AB` Block 1) | `08:50–08:54` | `239` | `10/10` ep | `57.00%` (`2` FC) | `83` | `596,481` / `37,805` | `0.031411` | `0.032127` |
| `c7-dbc-mode57_dbc-dev-r1` | `mode57_dbc` (`AB` Block 1) | `08:54–08:59` | `271` | `10/10` ep | `60.20%` (`3` FC) | `89` | `602,651` / `34,802` | `0.032243` | `0.032974` |
| `c7-dbc-mode57_dbc-dev-r2` | `mode57_dbc` (`BA` Block 2) | `08:59–09:03` | `237` | `10/10` ep | `68.50%` (`4` FC) | `72` | `500,355` / `33,920` | `0.030938` | `0.031659` |
| `c7-dbc-ctrl50-dev-r2` | `ctrl50` (`BA` Block 2) | `09:03–09:06` | `224` | `10/10` ep | `57.80%` (`2` FC) | `81` | `536,171` / `31,670` | `0.028441` | `0.029556` |
| `c7-dbc-ctrl50-dev-r3` | `ctrl50` (`AB` Block 3) | `09:06–09:10` | `225` | `10/10` ep | `54.50%` (`2` FC) | `80` | `558,589` / `33,842` | `0.029257` | `0.029973` |
| `c7-dbc-mode57_dbc-dev-r3` | `mode57_dbc` (`AB` Block 3) | `09:10–09:14` | `253` | `10/10` ep | `48.50%` (`2` FC) | `87` | `675,166` / `36,764` | `0.032066` | `0.032755` |
| `Atomic W0` Probe (`080`, `154`) | `standard` vs. `dbc` | `10:44–10:45` | `37` | `20` calls (`20`) | `080`: `10/10`; `154`: `3/10` | `20` | `59,100` / `9,162` | `0.007945` | `0.007945` |
| **Untruncated Matched (`MO-2a/4a/5a`)** | `blind`, `w0p`, `struct` | `13:26–13:32` | `324` | `76` calls (`76`) | `100/100`, `94/89`, `100/0%` | `76` | Retained in JSON | `0.029037` | `0.029037` |
| **Untruncated Matched (`Dev` `90`-Pair)** | `blind`, `w0p`, `struct`, `prose` | `13:26–13:32` | `324` | `480` calls + `10` `008` ties | `57.2 / 53.3 / 50.8 / 45.0%` | `480` | Retained in JSON | `0.468118` | `0.468118` |

*\*Including `0.373966` USD from the superseded truncated `v2` `457`-call run and `0.024162` USD across pipeline smoke checks (`0.005434 + 0.007212 + 0.011516` USD) brings cumulative physical API spend across all iterations to `1.787280` USD.*

---

## Appendix B. Container Specifications and Single-Factor Verification (`Mode 50` vs. `Mode 57-DBC`)

Both container arms run rootless (`USER 1000:1000`) with `NANOBOT_SCPC_MODE="50"` (`0%` wire reasoning replay, `0%` post-write AST receipts, identical Turn-0 workspace index and 19-word batch-reading reminder) verified against `baseline/manifests/c7_dbc_dev_manifest.json` (`code/build_mode57_dbc_image.py`):
- **`ctrl50` (`Batch-Index` / `Mode 50` [4]):** `harness-starters/gemini1-nanobot:eswv-risk-ctrl50` (`sha256:3daa4f8da2d17bb0e6a012f33161e647e1f88471acfdcad857ae978b4fbf52bd`).
- **`mode57_dbc` (`Mode 57-DBC`):** `harness-starters/gemini1-nanobot:mode57-dbc-v1` (`sha256:9840dd3ebe62adec8aa7ddb06b9d8a8595f801f8d05b39f1dd5116288bf3191b`), built directly `FROM eswv-risk-ctrl50` by appending only the 52-word Principle 3 (`Section 5.1`) to `SBE_LEAN_SYSTEM_PROMPT` in `/opt/nanobot-source/nanobot/agent/sada_lean_runtime.py`. All six other frozen source files (`providers/base.py`, `openai_compat_provider.py`, `openai_responses/converters.py`, `openai_responses/parsing.py`, `agent/runner.py`, `utils/helpers.py`) retain identical SHA-256 digests (`5bf92d78...`, `714dc4b0...`, `3dd5657e...`, `39389d1e...`, `d4e0532d...`, `741c7df4...`).

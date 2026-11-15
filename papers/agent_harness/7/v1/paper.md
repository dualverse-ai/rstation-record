# Whole-Deliverable Consensus, Candidate-Blind Witness Adjudication, and Specification Fidelity in an LLM Agent Harness

## 1. Problem, Scope, and Contributions

On multi-step software and data-synthesis benchmarks such as Harness-Bench [1, 2], lean single-pass harnesses driving `gpt-6-luna`—notably `Batch-Index` (`Nanobot Mode 50` [4], which injects a Turn-0 workspace index and a 19-word batch-reading reminder at `0.46x` of `Released Codex 0.166.0` solver cost)—leave substantial multi-trajectory headroom between single-draw mean outcome scores (`54.80%` on `development`, `65.19%` on exposure-qualified `validation`) and multi-draw whole-workspace oracle maxima (`74.48%` at $k=15$ on `development`, `76.64%` at $k=7$ on `validation`). Prior studies on this benchmark have shown that post-draft executable self-repair [3, 5, 7], turn collapsing [6], cross-package clause-union diagnostics and latent reasoning replay [8], and holistic swap-balanced LLM-as-a-judge selection (`q = 42.1%` across `57` discordant pairs, `Post 36` [9]) either incur steep cost multipliers or select near or below chance.

Building on prior execution-based Minimum Bayes Risk (MBR) selection (*MBR-EXEC* [12], *CodeT* [13], *AlphaCode* [14]), non-monotonic compound-inference scaling [16], and same-model verification analyses (`agent_harness_1` v3 `Section 4.10` [3]; `agent_harness_6` v1 [8]), we investigate three concrete questions on multi-file agent workspaces:

1. **Whole-deliverable medoid selection versus cellwise table voting ($k = 1 \dots 19$):** Across heterogeneous workspaces combining CSV/JSON tables, Python modules, and Markdown reports, how does prose-quarantined structural medoid selection (`Canonical-Medoid@k`) compare descriptively against coordinate-wise cell voting (`CellVote-3`) under explicit tie-breaking rules, and how does `Canonical-Medoid@k` scale across odd $k = 1 \dots 19$?
2. **Untruncated differential witness discovery and single-factor candidate exposure in pairwise adjudication:** When mechanical differential testing isolates a swap-symmetric set of complete, verified-distinct disagreement queries between two candidates, what are the **identified single-factor effects** of (i) exposing candidate outputs and code, (ii) exposing companion `.md` narratives, and (iii) adding explicit `W_0`-recomputation prompt rules while holding queries, JSON schema, and leaf-path matching fixed?
3. **First-pass two-sided contract prompting from synthetic controls to multi-file tasks:** When post-hoc selection stalls on tasks with low single-draw pass rates, does a 52-word domain-free *Two-Sided Specification Fidelity* rule (`Mode 57-DBC`) eliminate precondition-ordering shortcuts on controlled synthetic tasks (`MO-Suite`) without breaking required guards, and how much of that effect transfers prospectively to Harness-Bench `development` under a pre-declared `+3.50`-point, `<= 1.20x`-cost gate?

We evaluate these questions across **`520` archived `Mode 50` episodes** (`20` `development` runs + `8` anonymized exposure-qualified `validation` runs; `$0.00` new spend), **`1,129` retained adjudication and atomic-oracle API calls** (`556` in our untruncated 4-arm single-factor matched study, `553` in our bundled 4-protocol reference and synthetic calibration suites, and `20` noiseless atomic `W_0` probes; `0.9961` USD), **`120` concurrent interleaved synthetic `MO-Suite` episodes** (`0.2040` USD), and **`60` prospective counterbalanced `development` episodes** (`0.1890` USD; `1.3892` USD retained-supplement total, `1.7873` USD cumulative physical spend including an earlier superseded `457`-call prototype). Without claiming a new benchmark Pareto frontier, our contributions are:

1. **Untruncated Swap-Symmetric Witness Adjudication and 4-Arm Single-Factor Ablation (`Section 4`):** Repairing mid-object argument and outcome truncations from an earlier prototype (`v2`), our Stage-1 extractor (`Symmetric-BWA`) exports **complete, syntactically validated typed inputs and verified-distinct candidate outcomes (`c1 != c2` across `495 / 495` `development` loci; `0 / 90` swap diffs)** and matches `RETURN` objects directly at differing typed leaf paths. Across `556` calls (`0.4972` USD) holding symmetric queries, JSON schema, and Stage-3 matching fixed, we isolate two single-factor effects and one null:
   - **Candidate exposure on Python code (`3` tasks, `30` pairs):** Exposing candidate code and outcomes lowers accuracy from **`55.00%` (`sym_blind`) to `33.33%` (`sym_sighted_struct`, `-21.67 pp`, `11W / 3L / 16T`, exact pair sign-flip $p = 0.0248$**; wide nominal 3-task Student-$t_2$ `95% CI [-69.10, +25.77] pp` reflecting dispersion across three tasks: `080` `-5.0`, `150` `-42.5`, `154` `-17.5 pp`), consistent with a single-pair synthetic ambiguity case study (`MO-4a`: `100.0%` blind vs. `0.0%` sighted across `5` repetitions), whereas unambiguous synthetic guards (`MO-2a`: `100.0%` vs. `100.0%`; `MO-5a`: `94.4%` vs. `88.9%`) and prose-quarantined structured data (`6` tasks, `60` pairs: `58.33%` vs. `59.58%`, `-1.25 pp`, $p = 0.8418$) show no exposure loss.
   - **Companion `.md` prose exposure on structured data (`60` pairs):** Quarantining differing `.md` narratives lifts sighted structured-data accuracy by **`+11.67 pp`** (`59.58%` `sym_sighted_struct` vs. `47.92%` `sym_sighted_prose`, nominal task-cluster `95% CI [+1.90, +21.44] pp`, `18W / 9L / 33T`, exact pair sign-flip $p = 0.0125$).
   - **Oracle prompt wording at `0%` exposure (`90` pairs):** Replacing neutral instructions (`sym_blind`, `57.22%`, `+2.10` `2-Draw` points) with an explicit `W_0`-recomputation / anti-`RAISE` prompt (`sym_blind_w0prompt`, `53.33%`, `+0.98` points) has no positive single-factor effect (`-3.89 pp`, $p = 0.2861$).
2. **Descriptive Multi-File Medoid Scaling and Exact-Grid Table-Voting Audit (`Section 3`):** Using an explicit workspace-to-CSV/JSON/AST atom extractor (`code/similarity_extractor.py`, Python 3.10+ compatible), prose quarantine lifts zero-LLM $k=3$ medoid selection from `55.96%` to `57.05%`, peaks at $k=7$ (`58.06%`, `+3.26` points), and decays to `57.08%` at $k=19$ on the observed 20-run pool. On coupled tabular triage (`062`, $\binom{20}{3}=1{,}140$ triples, observed exact-grid rate $\hat{p}_{\text{exact}} = 30.00\%$), exact $3!=6$ permutation-symmetric `CellVote-3` lowers exact recovery of observed full-credit grids to **`18.60%`** (`21.84%` index-ordered; `23.89%` across the `8` structured columns excluding free-text `next_action`), whereas whole-table `Medoid-3` reaches **`38.96%`**.
3. **Synthetic-to-Benchmark Evaluation of Two-Sided Specification Prompting (`Section 5`):** Appending 52 domain-free words (`Mode 57-DBC`) lifts synthetic unordered-set full compliance on `MO-5a` from `10.0%` (`1 / 10`) to **`100.0%` (`10 / 10`, `+36.0` points, exact Fisher $p = 0.000119$)** while preserving **`50 / 50 = 100.0%`** across five controls, and scores **`59.07%` vs. `56.43%` (`+2.63` points, nominal `95% CI [-7.72, +12.99]`, $p = 0.6094$) at `1.0625x` complete cost** across `60` prospective `development` episodes (`$0.00` `validation` spend).

### Notation, Scope, and Methodological Qualifications

- **Distinct probability and score quantities:** On a run pool of size $n$, we distinguish: (1) $\bar{S}_t \in [0, 100]$, empirical mean partial-credit score on task $t$; (2) $\hat{p}_{\text{exact}}(t) \in [0, 1]$, fraction of runs achieving $S_{t,i} = 100\%$; (3) $\hat{p}_{t,c} \in [0, 1]$, gate-qualified pass rate of grading clause $c$; and (4) $\hat{p}_{\text{atomic}}(w) \in [0, 1]$, isolated `(Prompt, W_0)` oracle accuracy on boundary witness $w$, distinct from pairwise accuracy $q_t \in [0, 1]$ on discordant pairs $D_t = \{S_{t,1} \neq S_{t,2}\}$.
- **Combinatorial enumeration vs. sampling uncertainty:** Exhaustive evaluation over all $\binom{n}{k}$ subsets eliminates *subset-sampling Monte Carlo error conditional on the $n$ observed runs*, not run-sampling uncertainty across fresh benchmark draws. Similarly, matching observed `100%`-scoring CSV grids (`Section 3.2`) measures **exact-grid recovery against observed full-credit solutions**; it does not certify or falsify every newly composed non-matching table that might satisfy semantic grading rules.
- **Strict validation firewall and two-route reproducibility:** Zero hidden benchmark grader files (`tests/`, `design.md`, `task.yaml`, `grader-control/`) were read in any split, and zero `validation` prompts, workspaces, or raw traces were opened; all 40-task `validation` summaries are labeled **exposure-qualified** [4, 5, 7, 8]. Our `supplement.zip` separates **Route A** (`python3 -B verify_paper_stats.py`: `$0.00` deterministic stdlib verification of retained outputs, workspace reconstructions, and live `MO-Suite` grading) from **Route B** (`python3 -B code/run_matched_exposure_study.py`: self-contained live API regeneration from bundled workspace archives `data/dev_90pair_workspaces.json` and `data/mo_c7_120ep_programs.json` when supplied API credentials).

---

## 2. Related Work

**Consensus decoding, execution-based selection, and non-monotonic scaling.** Majority voting (*Self-Consistency*, **Wang et al. [10]**) amplifies plurality-correct scalar answers, whereas free-form outputs require multi-candidate reading (*Universal Self-Consistency*, **X. Chen et al. [11]**) or Minimum Bayes Risk (MBR) selection (**Eikema and Aziz [15]**). For single-function code generation, **Shi et al. (*MBR-EXEC* [12])**, **B. Chen et al. (*CodeT* [13])**, and **Li et al. (*AlphaCode* [14])** select candidates using execution agreement on public or LLM-generated test suites, while **L. Chen et al. [16]** showed analytically on scalar QA mixtures that majority voting scales non-monotonically when $p > 0.5$ and $p < 0.5$ items coexist. On Harness-Bench, `agent_harness_1` v3 (`Section 4.3, 4.6, 4.10` [3]) established weak within-task verifier ranking, workspace consensus baselines, and two-run union-versus-best diagnostics (noting that small clause-union gaps do not preclude finer sub-clause synthesis), and `agent_harness_6` v1 [8] formulated unbiased Hoeffding U-statistics [17] for cross-package clause unions. Here we operationalize zero-LLM prose-quarantined medoid selection across CSV/JSON/Python deliverables (`Canonical-Medoid@k`) and audit symmetric table-voting tie rules across odd $k = 1 \dots 19$.

**LLM-as-a-judge biases, debate oversight, and differential witness discovery.** Holistic LLM judges exhibit position, verbosity, and salience biases (**Zheng et al. [18]**), and ungrounded self-critique rarely overturns committed reasoning errors (**Huang et al. [20]**). Oversight protocols such as *AI Safety via Debate* (**Irving et al. [19]**) motivate decomposing complex artifacts into localized leaf queries. On Harness-Bench `Posts 36 & 43` [9], holistic swap-balanced pairwise judging scored `q = 42.1%` across `57` discordant `Mode 50` pairs (`34.2%` on code), while `feeling_of_knowing`'s pre-candidate blind check generator (`A1`) reached `q = 54.9%` with `48%` ties because tests written *before* seeing candidates frequently miss where two drafts diverge (requiring `24` check modules in `A24` to reach `3%` ties). Rather than generating blind tests prior to candidate inspection as in `A1` [9] or *CodeT* [13], our distinctive mechanism uses zero-LLM **differential testing (McKeeman [21])** across the two candidates to extract complete, verified-distinct disagreement inputs first, followed by candidate-blind specification labeling and leaf-path matching—tested directly through matched exposure controls.

**Lean agent harnesses and Design by Contract.** Prior Harness-Bench studies established `Mode 50` [4], turn-collapsing cost tradeoffs [6], and post-draft repair screening (`ESWV-Lean` [5], `ESWV-Risk` [7]). Classical **Design by Contract (Meyer [22])** distinguishes *precondition soundness* (accepting all specification-valid inputs) from *invariant completeness* (enforcing stated rules across all fields), motivating synthetic `MO-5a/5b` and `Mode 57-DBC`.

---

## 3. Whole-Deliverable Medoid Selection and Table Voting ($k = 1 \dots 19$)

### 3.1 Descriptive Clause-Collection Envelope (`ClauseUnion@k - Best-of-k`)

Let task $t \in \{1, \dots, T\}$ have positive-weight non-gate clauses $c$ with normalized within-task weights $\tilde{w}_{t,c} = w_{t,c} / \sum_{c'} w_{t,c'}$. Given $n$ observed `Mode 50` runs with episode scores $S_{t,1}, \dots, S_{t,n} \in [0, 100]$ and gate-qualified clause pass indicators $Y_{t,c,i} \in \{0, 1\}$ ($s_{t,c} = \sum_{i=1}^{n} Y_{t,c,i}$, $\hat{p}_{t,c} = s_{t,c}/n$), the unbiased Hoeffding U-statistic estimators [8, 17] at budget $k \leq n$ are:

$$
\widehat{\text{Best-of-}k}_t = \frac{1}{\binom{n}{k}}\sum_{m=k}^{n} \binom{m-1}{k-1} S_{t,(m)}, \qquad
\widehat{\text{ClauseUnion@}k}_t = 100 \sum_{c} \tilde{w}_{t,c}\!\left[1 - \frac{\binom{n - s_{t,c}}{k}}{\binom{n}{k}}\right],
$$

where $S_{t,(1)} \leq \cdots \leq S_{t,(n)}$ are order statistics, alongside the odd-$k$ diagnostic clausewise majority envelope

$$
\widehat{\text{OracleClauseMaj@}k}_t = 100 \sum_{c} \tilde{w}_{t,c} \sum_{j=(k+1)/2}^{k} \frac{\binom{s_{t,c}}{j}\binom{n - s_{t,c}}{k - j}}{\binom{n}{k}}.
$$

Following [3, Section 4.10], **`ClauseUnion@k - Best-of-k` bounds only clause-level collection of already-passed, gate-qualified clauses among sampled candidates, not constructive sub-clause synthesis**. Within that observed scope, across `8` exposure-qualified `Mode 50` `validation` runs (`40` tasks, `320` episodes, `191` clauses), `ClauseUnion@k - Best-of-k` is `+0.28` points at $k=2$ (`72.30%` vs. `72.02%`), `+0.20` at $k=3$ (`74.58%` vs. `74.38%`), and `0.00` at $k=7$ (`76.64%`). Across `20` `Mode 50` `development` runs (`10` tasks, `200` episodes, `50` clauses), the gap is `+0.48` points at $k=2$ (`61.77%` vs. `61.29%`), `+0.78` at $k=3$ (`65.21%` vs. `64.43%`), `+1.62` at $k=7$ (`71.86%` vs. `70.24%`), and `+2.05` at $k=19$ (`77.40%` vs. `75.35%`).

### 3.2 Workspace Similarity Construction and Exact-Grid Table-Voting Audit

To select a single coherent workspace without LLM calls (`code/similarity_extractor.py`), **`Canonical-Medoid@k`** maps each deliverable file $f$ in candidate workspace $W^{(a)}$ to a canonical atom set $A_f(W^{(a)})$: JSON files flatten to `path=value` atoms with volatile execution timestamps masked; CSV/TSV tables emit header and `(row_key, col_idx, trimmed_value)` atoms keyed by unique primary ID when column `0` is unique; Python files extract AST `FunctionDef`, short scalar `Constant`, `Compare`, and `Return` signatures (falling back to whitespace-normalized lines on syntax errors); and **prose quarantine** averages exact set Jaccard $|A_f(W^{(a)}) \cap A_f(W^{(b)})| / |A_f(W^{(a)}) \cup A_f(W^{(b)})|$ strictly over structured `data` and `code` deliverables whenever present (defaulting to $k=1$ expectation on prose-only `008`). Over any $k$-subset $S$, `Canonical-Medoid@k` selects $\arg\max_{a \in S} \sum_{b \in S \setminus \{a\}} \text{Sim}(W^{(a)}, W^{(b)})$, averaging uniformly across ties. Across the `10` `development` tasks ($\binom{20}{3} = 1{,}140$ triples/task), unnormalized row/line prose-inclusive `Medoid@3` scores **`55.96%` (`+1.16` points)**, canonical prose-inclusive `Medoid@3` scores **`56.50%` (`+1.70` points)**, and prose-quarantined **`Canonical-Medoid@3` scores `57.05%` (`+2.25` points)**.

To compare coordinate-wise table voting (`CellVote-3`) against whole-table medoid selection (`Medoid-3`), we measure **exact-grid recovery**—whether the output CSV matches an observed `100%`-scoring reference grid—across all $\binom{20}{3} = 1{,}140$ triples on `029` (`customer_metrics.csv`, $\hat{p}_{\text{exact}} = 15/20 = 75.00\%$) and `062` (`dsar_intake_register.csv`, $\hat{p}_{\text{exact}} = 6/20 = 30.00\%$, $\bar{S}_{062} = 65.75\%$). Note that **exact-grid recovery is distinct from semantic table correctness**: matching observed full-credit grids certifies exact recovery of known solutions, whereas a newly composed non-matching table is not automatically invalid (for example, alternative phrasing in a free-text column could still satisfy semantic grading). Reporting both deterministic index-ordered tie-breaking and **exact $3! = 6$ permutation-symmetric tie-averaging** within each triple isolates the structural contrast cleanly:
- **Plurality-exact table (`029`, $\hat{p}_{\text{exact}} = 75.00\%$):** Both `CellVote-3` (`95.44%` under both index-ordered and `6`-permutation evaluation) and `Medoid-3` (`95.18%`) lift exact-grid recovery by `+20` percentage points.
- **Coupled triage table (`062`, $\hat{p}_{\text{exact}} = 30.00\%$):** Across all `9` columns, `Medoid-3` lifts exact-grid recovery from `30.00%` to **`38.96%` (`+8.96 pp`)**, whereas `6`-permutation symmetric `CellVote-3` lowers exact-grid recovery to **`18.60%` (`-11.40 pp`; `21.84%` index-ordered)**. Column-role ablations (`verify_paper_stats.py`) show that on the `7` core categorical columns (`85.00%` single-draw gold agreement), both `6`-permutation `CellVote-3` and `Medoid-3` reach **`95.44%`**; adding structured multi-tag column `8` (`policy_basis`, where runs split across citation conventions such as `P-1;P-3;P-5` vs. `P-1;P-3;P-4;P-5;DM-1` at `30.00%` gold agreement) drops `6`-permutation `CellVote-3` to **`23.89%`** (`27.72%` index-ordered) versus **`39.53%`** for `Medoid-3` even before free-text `next_action` (column `7`) is included.

### 3.3 Descriptive Combinatorial Trajectory Across Odd $k = 1 \dots 19$

Evaluating `Canonical-Medoid@k` across all $\binom{20}{k}$ subsets for odd $k = 1 \dots 19$ (`Table 1`, `Figure 1`) shows rise-then-decay behavior on the observed 20-run pool: peaking at **$k=7$ (`58.06%`, `+3.26` points < `+3.50` gate)** before declining to **`57.08%` at $k=19$** (`-0.98` points from peak).

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

On `031` ($\hat{p}_{\text{exact}} = 85\%$), medoid selection still declines slightly (`97.00% -> 92.00%`) because two imperfect runs share sparser HTML boilerplate with higher pairwise token overlap than customized `100%` solutions; on `062` ($\hat{p}_{\text{exact}} = 30\%$), error dispersion lets the `6`-run `100%` cluster win up to $k=9$ (`84.79%`) before a secondary partial-credit cluster overtakes it at larger $k$ (`76.25%` at $k=19$).

---

## 4. Untruncated Differential Witness Adjudication and Single-Factor Exposure Controls

### 4.1 Exact Two-Draw Gain Identity and Untruncated `Symmetric-BWA` Pipeline

Let $(W_1, W_2)$ be two independent draws on task $t$ with outcome scores $(S_{t,1}, S_{t,2})$, single-draw mean $\bar{S}_t = \mathbb{E}[S_{t,1}]$, and discordance event $D_t = \{S_{t,1} \neq S_{t,2}\}$. For any pairwise selector whose swap-averaged probability of choosing the higher-scoring workspace on discordant pair $X = \{W_1, W_2\}$ is $q_t(X) \in [0, 1]$, the exact expected two-draw score gain over $\bar{S}_t$ is:

$$
\Delta_{\text{2-Draw},t} \;=\; \mathbb{E}[S_{\text{picked},t}] - \bar{S}_t \;=\; \mathbb{P}(D_t)\,\mathbb{E}\!\left[\left(q_t(X) - \tfrac{1}{2}\right)|S_{t,1} - S_{t,2}| \;\middle|\; D_t\right] \;=\; \left(q_{w,t} - \tfrac{1}{2}\right)\,\mathbb{E}\big[|S_{t,1} - S_{t,2}|\big],
$$

where $q_{w,t} = \mathbb{E}[q_t(X)|S_{t,1} - S_{t,2}| \mid D_t] / \mathbb{E}[|S_{t,1} - S_{t,2}| \mid D_t]$ is the **score-gap-weighted accuracy**.

To test candidate exposure without order bias or representation loss, our repaired **`Symmetric-BWA`** pipeline (`code/diff_witness.py`, `code/blind_witness_adjudicator.py`) enforces three invariants across Stages 1–3:
1. **Stage 1 — Swap-Symmetric, Untruncated Witness Discovery (`$0.00`, `0` LLM calls):**
   - *Symmetric seed capture:* For `.py` deliverables, common public functions are instrumented in two isolated copies of $W_0$—running $W_0$'s public `unittest` suite and `bin/*.py` scripts under $W_1$ and separately under $W_2$—and taking the `repr`-sorted union of captured `(args, kwargs)` calls $C(W_1) \cup C(W_2)$ (`0 / 90` swap diffs on `development` and verified on an `f(0) -> f(10)` short-circuit unit test). For CSV/TSV deliverables, header mismatches emit a symmetric header query and fall back to canonical `col_i` indices when $h_1 \neq h_2$.
   - *Complete untruncated inputs and verified-distinct outcomes:* An earlier prototype (`v2`) sliced exported `args_repr` at `950` characters and `RETURN` outcomes at `380` characters, cutting off multi-snapshot inputs on `150` and `154` and collapsing `RETURN` prefixes that differed only at later list indices (`decisions[4].reason`). Our repaired extractor exports **complete, unsliced `repr(args)`, `repr(kwargs)`, and `RETURN`/`RAISE` outcomes** (maximum `args_repr` across all `90` `development` pairs is `2,370` chars; maximum outcome is `1,672` chars; maximum candidate `.py`/`.md` deliverable is `9,024` chars, all exported unsliced), deduplicates `BOTH_RETURN` perturbations symmetrically by their exact differing leaf paths `_flat_ret(res)` (avoiding redundant perturbations that hit the identical leaf disagreement), and executes `validate_witness_integrity(queries)` on every pair to hard-assert `ast.literal_eval(input_args)` completeness and `c1 != c2` distinctness across **`100%` (`495 / 495`)** of exported `development` queries (`90` `CODE`, `405` `DATA`).
2. **Stage 2 — Specification Oracle (`1` `gpt-6-luna` call in blind arms; `2` AB/BA swapped calls in sighted arms):** Queries present `(Task Prompt, Seed W_0)` (unsliced up to `25,000` chars/file; max `development` $W_0$ file is `8,341` chars) plus unlabeled queries `Q1..Qm` requesting `{"kind": "RAISE"|"RETURN", "expected": <exact JSON-compatible return value or cell value>, "json_type": ..., "mutate_input": false}`. Every `CODE` query uses the identical unlabeled format `(file, function, input_args)` whether candidates raised or returned, leaking zero candidate-outcome cues in blind arms (`position_bias == 0.000` identically).
3. **Stage 3 — Structural Leaf-Path Matcher (`$0.00`, `0` LLM calls):** On `RAISE`-vs.-`RETURN` witnesses, `score_blind_answer_against_candidates` scores `kind`; on `BOTH_RETURN` witnesses, it parses both untruncated candidate return objects via `ast.literal_eval`, flattens them via `_flatten_json_typed(obj, "ret")` to isolate the exact differing leaf paths $\Delta = \{k : m_1(k) \neq m_2(k)\}$, and compares the oracle's structured `expected` return object directly at $k \in \Delta$ (falling back to differing-leaf token comparison when `expected` is scalar, eliminating whole-object token shadowing).

### 4.2 Untruncated 4-Arm Single-Factor Matched Study (`556` Calls, `0.4972` USD)

Using `code/run_matched_exposure_study.py` (which reconstructs all synthetic and `development` workspaces directly from bundled `data/mo_c7_120ep_programs.json` and `data/dev_90pair_workspaces.json` via `code/workspace_adapter.py`), we held the `495` untruncated symmetric `development` queries (`+` synthetic queries), JSON output schema, and Stage-3 leaf-path matcher **100% fixed** across four single-factor arms:
- **`sym_blind`:** Neutral `MATCHED_LOCUS_SYSTEM_PROMPT` + `0%` candidate exposure (`1` call/pair).
- **`sym_blind_w0prompt`:** `BLIND_ORACLE_SYSTEM_PROMPT` (adding explicit *"compute ... directly from W0"* and *"raise an exception ONLY if the specification requires rejecting that input"* instructions) + `0%` candidate exposure (`1` call/pair)—isolating prompt wording against `sym_blind`.
- **`sym_sighted_struct`:** Neutral `MATCHED_LOCUS_SYSTEM_PROMPT` + untruncated `Option A`/`Option B` outcomes at `Q1..Qm` and full `.py` deliverable code (`2` swapped calls/pair; `.md` prose excluded)—isolating candidate exposure against `sym_blind`.
- **`sym_sighted_prose`:** Neutral `MATCHED_LOCUS_SYSTEM_PROMPT` + `sym_sighted_struct` context + full differing `.md` companion narratives (`2` swapped calls/pair)—isolating `.md` prose exposure against `sym_sighted_struct`.

**Synthetic controls and single-pair ambiguity case study (`19` pair evaluations, `76` calls, `0.0290` USD; `Figure 2a`).**
1. **Unambiguous single-factor guard (`MO-2a`, `5` pairs):** Pairing all `5` `100%`-scoring `Mode 50` `cooler_ledger.py` modules against single-clause uncontracted `audit_seq` monotonicity injections (`80%` score) yields **`100.0%` (`5 / 5`)** across `sym_blind`, `sym_blind_w0prompt`, and `sym_sighted_struct`.
2. **Unambiguous set-coverage shortcut (`MO-5a`, `9` unmodified `Mode 50` pairs):** Pairing all `9` `60%`-scoring `Mode 50` runs against `100%`-scoring run `r5` yields **`94.4%` (`8.5 / 9`)** under `sym_blind` and `sym_blind_w0prompt` and **`88.9%` (`8.0 / 9`)** under `sym_sighted_struct` (`1` pair `r2` emits `0` `Diff-Exec` queries -> `0.5` tie).
3. **Single-pair specification-ambiguity case study (`MO-4a`, `1` archived pair $\times$ `5` matched repetitions):** Across `15` archived `Mode 50` runs on `MO-4a`, all `15` scored `100%`; the lone defective run in our archive (`mode55_frame__MO-4a__r3`, `15.0%` vs. `mode50_ctrl__MO-4a__r1`, `100.0%`) raises `ValueError('soak_windows must reset after a traffic change')` on a `5% -> 0%` transition with `soak_windows = 2`, where `docs/rollout_contract.md` places *"`soak_windows` resets after traffic changes and may decrease freely"* inside `Section 1: Structural & Continuity Validation (ValueError)` without specifying whether reset is a caller precondition or a domain property. Across `5` matched repetitions on this pair, **`sym_blind` and `sym_blind_w0prompt` score `100.0%` (`5 / 5` `RETURN`)**, whereas **`sym_sighted_struct` scores `0.0%` (`10 / 10` AB/BA calls endorse `RAISE`)**. Because this contrasts repeated calls on a single archived pair rather than a multi-task sample, we treat it strictly as a mechanistic case study motivating the `development` test below.

![Figure 2: (a) Untruncated 4-arm single-factor matched ablation (556 API calls holding verified-distinct symmetric queries, JSON schema, and Stage-3 leaf-path matching fixed), isolating a -21.67 pp candidate-exposure penalty on Python code (55.0% blind vs. 33.3% sighted-struct, pair sign-flip p = 0.0248), a +11.67 pp prose-quarantine gain on structured data (59.6% vs. 47.9%, p = 0.0125), and a null -3.89 pp W0-prompt contrast at 0% exposure. (b) Bundled cross-protocol reference across the same 90 Mode 50 development pairs (holistic sighted protocols vs. BWA-v1).](supplement/figure-2-sighted-salience-vs-blind-bwa.png)

**`90`-pair `Mode 50` `development` single-factor results (`480` active calls + `10` prose-only `008` zero-query ties, `0.4681` USD; `Table 2A`, `Figure 2a`).** Preserving complete, untruncated inputs and distinct leaf-resolved outcomes yields three clean single-factor findings:
1. **Candidate exposure penalizes Python code adjudication (`+21.67 pp` blind advantage):** Across the `30` Python pairs (`080, 150, 154`), holding neutral `MATCHED_LOCUS_SYSTEM_PROMPT`, untruncated queries, and leaf-path matching fixed, **removing candidate exposure lifts accuracy from `33.33%` (`sym_sighted_struct`) to `55.00%` (`sym_blind`), a `+21.67 pp` gain** (`11W / 3L / 16T`, **exact pair-level two-sided sign-flip $p = 0.0248$**). Eliminating the `v2` truncation bug notably lifted `sym_blind` on `150` from `65.0%` to **`80.0%`** (`vs. 37.5%` under `sym_sighted_struct`), improving all three Python tasks (`080`: `30.0% -> 35.0%`; `150`: `37.5% -> 80.0%`; `154`: `32.5% -> 50.0%`). Because this subset spans **only three tasks**, the nominal 3-task cluster Student-$t_2$ interval is wide (`95% CI [-25.77, +69.10] pp` due to between-task dispersion `+5.0, +42.5, +17.5 pp`); we report both the exact pair-level sign-flip test ($p = 0.0248$) and the 3-task limitation explicitly.
2. **Candidate exposure is neutral on prose-quarantined structured data (`-1.25 pp`), whereas companion `.md` prose degrades accuracy (`-11.67 pp`):** Across the `60` Data/Doc pairs (`008, 015, 029, 031, 062, 066`), **`sym_blind` (`58.33%`) and `sym_sighted_struct` (`59.58%`) are indistinguishable** (`-1.25 pp`, nominal `95% CI [-14.60, +12.10] pp`, `12W / 13L / 35T`, $p_{\text{pair}} = 0.8418$). By contrast, appending differing `.md` narratives (`sym_sighted_prose` = `47.92%`) reduces Data/Doc accuracy by **`-11.67 pp`** relative to `sym_sighted_struct` (**nominal task-cluster `95% CI [-21.44, -1.90] pp`**, `9W / 18L / 33T`, **exact pair sign-flip $p = 0.0125$**), lowering all `5` active Data/Doc tasks (`015`: `45.0% -> 32.5%`; `029`: `67.5% -> 42.5%`; `031`: `62.5% -> 45.0%`; `062`: `85.0% -> 72.5%`; `066`: `47.5% -> 45.0%`).
3. **Explicit `W_0`-recomputation prompt wording does not improve over neutral blind instructions (`-3.89 pp` null):** Comparing `sym_blind_w0prompt` (`53.33%` overall, `55.00%` Data, `50.00%` Python) against `sym_blind` (`57.22%` overall, `58.33%` Data, `55.00%` Python) on identical untruncated queries yields **`-3.89 pp` (`95% CI [-11.76, +3.98] pp`, `7W / 9L / 74T`, $p_{\text{pair}} = 0.2861$)**, refuting the hypothesis that `BLIND_ORACLE_SYSTEM_PROMPT`'s extra wording drives `BWA` performance.

### 4.3 Bundled Cross-Protocol Reference Comparison (`500` Calls, `0.4620` USD)

For benchmark context alongside our single-factor ablations (`Table 2A`), `Table 2B` (`Figure 2b`) retains our earlier end-to-end 4-protocol comparison (`data/c6_c7_adjudication_raw_records.json`): holistic **`static_full`**, diff-based **`static_quarantine`**, witness-augmented **`wdpa_full`**, and initial **`bwa_blind` (`v1`)**. Because `Part B` protocols vary presentation format (full files vs. unified diffs vs. localized queries), prompts, output schemas, and matching rules simultaneously, **differences across `Part B` rows represent bundled protocol comparisons rather than isolated component effects**:

**Table 2. Untruncated 4-arm single-factor matched ablations (`Part A`, `495` verified-distinct queries, `480` active calls) and bundled cross-protocol reference (`Part B`, `500` calls) across the `90` discordant `Mode 50` `development` pairs (`2-Draw` gains recomputed from raw pair gaps and 20-run $\mathbb{P}(D_t)$).**

| Study / Condition | Varied Factor / Protocol Scope | Pos. Bias (`\|P(1)-0.5\|`) | Total Ties (`/90`) | All 9 Tasks `q` | 6 Data/Doc `q` | 3 Python `q` | `029` / `062` / `015` / `150` / `154` / `080` `q` | Expected `2-Draw` Gain (`95% CI`, `Bo2 Share`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Part A: Untruncated Matched** | *Fixed symmetric `Q1..Qm` & matcher* | | | | | | | |
| ↳ **`sym_blind`** | **Neutral prompt, `0%` exposure** | **`0.000`** | `29` (`32.2%`) | **`57.2%`** | `58.3%` | **`55.0%`** | **`80`** / `70` / **`60`** / **`80`** / `50` / **`35%`** | **`+2.10`** (`[-0.58, +4.79]`, `32.4%`) |
| ↳ **`sym_blind_w0prompt`** | `W0`-oracle prompt, `0%` exposure | **`0.000`** | `26` (`28.9%`) | `53.3%` | `55.0%` | `50.0%` | `70` / `50` / **`60`** / `60` / **`55`** / **`35%`** | `+0.98` (`[-0.34, +2.31]`, `15.1%`) |
| ↳ **`sym_sighted_struct`** | Neutral + Code & Cell Outcomes | `0.075` | `30` (`33.3%`) | `50.8%` | **`59.6%`** | `33.3%` | `68` / **`85`** / `45` / `38` / `32` / `30%` | `+1.51` (`[-1.79, +4.81]`, `23.3%`) |
| ↳ **`sym_sighted_prose`** | Neutral + Struct + `.md` Prose | `0.078` | `27` (`30.0%`) | `45.0%` | `47.9%` | `39.2%` | `42` / `72` / `32` / `45` / `50` / `22%` | `+0.09` (`[-2.42, +2.59]`, `1.3%`) |
| **Part B: Bundled Protocols** | *Vary format, prompt & decision rule* | | | | | | | |
| ↳ **`static_full`** [9] | Holistic full files + `.md` | `0.067` | `8` (`8.9%`) | `46.7%` | `44.2%` | `51.7%` | `45` / `60` / `35` / `60` / `55` / `45%` | `+0.10` (`[-1.84, +2.04]`, `1.6%`) |
| ↳ **`static_quarantine`** | Holistic unified diff, no `.md` | `0.156` | `9` (`10.0%`) | `51.1%` | `49.2%` | `55.0%` | `55` / `70` / `45` / `75` / `40` / `50%` | `+1.17` (`[-1.12, +3.47]`, `18.1%`) |
| ↳ **`wdpa_full`** | Unified diff + `v1` `Diff-Exec` | `0.144` | `7` (`7.8%`) | `48.9%` | `49.2%` | `48.3%` | `55` / `70` / `45` / `65` / `35` / `45%` | `+0.98` (`[-1.32, +3.28]`, `15.1%`) |
| ↳ **`bwa_blind` (`v1`)** | `v1` queries + `W0`-oracle prompt | **`0.000`** | `32` (`35.6%`) | `57.8%` | `63.3%` | `46.7%` | `85` / `85` / `65` / `50` / `60` / `30%` | `+2.61` (`[-1.17, +6.38]`, `40.2%`) |

Across both `sym_blind` (`29 / 90 = 32.2%` ties; `+2.10` `2-Draw` points, `95% CI [-0.58, +4.79]`) and `bwa_blind` (`32 / 90 = 35.6%` ties: `10` zero-query prose ties on `008` plus `22` split-vote ties including `9 / 10` on markup-heavy `031`; `+2.61` points, `95% CI [-1.17, +6.38]` at `0.87x` `Codex` solver cost), candidate-blind locus adjudication avoids holistic anti-selection and eliminates swap-order bias (`0.000`), while remaining below our pre-declared `+3.50`-point gate (`$0.00` `validation` spend).

---

## 5. First-Pass Two-Sided Specification Fidelity (`Mode 57-DBC`)

### 5.1 Offline Behavioral Associations in Archived `Mode 50` Python Workspaces (`080` and `154`)

Running actor-visible specification probes across the `20` archived `Mode 50` `development` workspaces (`code/audit_c7_precondition_and_composite_invariants.py`) identifies two strong descriptive associations:
1. **Uncontracted list-order rejection (`080-multipart-artifact-resume-recovery`):** Passing valid unordered `local_parts = [part 2, part 1]` causes **`18 / 20` (`90.0%`) archived `Mode 50` modules to raise `ValueError`**, forming a `[[2, 0], [0, 18]]` table with `case:paginated_part_reconciliation` ($\hat{p}_{080,\text{pag}} = 10.0\%$, exact Fisher $p = 0.005263$).
2. **Composite boundary checks (`154-postgres-expand-contract-migration-repair`):** Across the `20` archived runs, `14 / 20` accept non-empty `dual_write_versions = ["v2"]` when `target_exists = False` and `9 / 20` check `snapshot_id` uniqueness only on adjacent elements; joint satisfaction forms a `[[4, 0], [0, 16]]` table with `case:source_and_database_boundary` ($\hat{p}_{154,\text{sdb}} = 20.0\%$, Fisher $p = 0.000206$).

### 5.2 Synthetic Pair `MO-5a/5b` and Single-Factor `Mode 57-DBC` (`120` Episodes, `0.2040` USD)

We authored `MO-5a/5b` in Cryogenic Vial Rack Reconciliation (`src/cryo_rack.py` in `code/mo_suite.py`): **`MO-5a`** requires `slot_index` set coverage `1..slot_count` in any order plus composite `decommissioned` and `vial_code` uniqueness checks, whereas negative control **`MO-5b`** requires strictly ascending `slot_index` order. Starting `FROM harness-starters/gemini1-nanobot:eswv-risk-ctrl50` (`NANOBOT_SCPC_MODE=50`), **`Mode 57-DBC`** (`code/build_mode57_dbc_image.py`, `Appendix B`) appends **only** 52 domain-free words to `SBE_LEAN_SYSTEM_PROMPT`:

> `3. **Two-Sided Specification Fidelity**: Enforce every constraint written in the specification across all relevant schema fields and records, while accepting every input that satisfies the written specification even when its ordering or values differ from the sample fixtures (for code deliverables, include boundary cases beyond the sample fixtures when running your exec test check).`

Across **`120` concurrent interleaved `MO-Suite` episodes** (`10` `AB` replicates $\times$ `6` organisms; `Table 3`, `Figure 3a`), `Mode 57-DBC` lifts `MO-5a` exact full compliance $\hat{p}_{\text{exact}}$ from **`10.0%` (`1 / 10`, mean `64.0%`) to `100.0%` (`10 / 10`, `+36.0` points, `95% CI [+26.95, +45.05]`, exact Fisher $p = 0.000119$)** while preserving **`50 / 50 = 100.0%`** full compliance across all five controls (`MO-5b, MO-1b, MO-2b, MO-4a, MO-3b`).

**Table 3. Concurrent interleaved `120`-episode `MO-Suite` evaluation of single-factor `Mode 57-DBC` vs. `Mode 50` (`10` replicates/cell).**

| Organism | Contract Role | `Mode 50` Mean ($\hat{p}_{\text{exact}}$) | `Mode 57-DBC` Mean ($\hat{p}_{\text{exact}}$) | Paired $\Delta$ (`95% CI`) | Exact FC Fisher $p$ | `Mode 50` / `DBC` mUSD (`Ratio`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **`MO-5a`** | **Positive: Set coverage `1..N` (unordered valid)** | **`64.0%` (`1/10`)** | **`100.0%` (`10/10`)** | **`+36.0` (`[+26.95, +45.05]`)** | **`0.000119`** | `1.94` / `2.33` (`1.202x`) |
| **`MO-5b`** | Negative ctrl: Strictly ascending list required | `100.0%` (`10/10`) | `100.0%` (`10/10`) | `+0.0` (`[0.00, 0.00]`) | `1.0000` | `1.79` / `2.01` (`1.125x`) |
| **`MO-1b`** | Negative ctrl: Epoch rollover & duplicate guard | `97.5%` (`9/10`) | `100.0%` (`10/10`) | `+2.5` (`[-3.16, +8.16]`) | `1.0000` | `1.74` / `2.15` (`1.229x`) |
| **`MO-2b`** | Negative ctrl: Inclusive float bounds & `audit_seq` | `100.0%` (`10/10`) | `100.0%` (`10/10`) | `+0.0` (`[0.00, 0.00]`) | `1.0000` | `1.33` / `2.03` (`1.527x`) |
| **`MO-4a`** | Ambiguous-reset ctrl: No uncontracted regression | `100.0%` (`10/10`) | `100.0%` (`10/10`) | `+0.0` (`[0.00, 0.00]`) | `1.0000` | `1.80` / `1.98` (`1.098x`) |
| **`MO-3b`** | Static SQLite/CLI economy ctrl (non-code) | `100.0%` (`10/10`) | `100.0%` (`10/10`) | `+0.0` (`[0.00, 0.00]`) | `1.0000` | `0.60` / `0.70` (`1.172x`) |

![Figure 3: (a) Concurrent 120-episode MO-Suite evaluation showing Mode 57-DBC lifting MO-5a full compliance from 10% (1/10) to 100% (10/10, Fisher p = 0.000119) while preserving 50/50 (100%) full compliance across all five controls. (b) Prospective 60-episode counterbalanced AB/BA/AB development study (c7-dbc) showing per-task score deltas (+2.63 pts mean, nominal 95% CI -7.72 to +12.99, 1.06x complete cost) against the pre-declared +3.50-point gate.](supplement/figure-3-first-pass-dbc-and-dev-transfer.png)

### 5.3 Prospective `60`-Episode `development` Study (`c7-dbc`) and Diagnostics

Across `60` counterbalanced `development` episodes (`3` `AB, BA, AB` blocks; `0.189044` USD complete spend; `Table 4`, `Figure 3b`, `Appendix A`), supplemented by `20` noiseless atomic `(Prompt, W_0)` oracle calls (`data/c8_atomic_and_locus_diagnostics.json`, `0.0079` USD), `Mode 57-DBC` scores **`59.07%` vs. `56.43%` (`+2.63` points, nominal `95% CI [-7.72, +12.99]`, exact sign-flip $p = 0.6094$, `1.0625x` complete cost)**—an interval consistent with both meaningful losses and gains that does not meet our `+3.50`-point gate (`$0.00` `validation` spend):

**Table 4. Prospective `60`-episode counterbalanced `c7-dbc` `development` readout (`3` `AB, BA, AB` blocks) and behavioral probes.**

| Metric / Pre-Committed Behavioral Probe | `Mode 50` (`ctrl50`) | `Mode 57-DBC` | Paired Contrast / Notes |
| :--- | :---: | :---: | :--- |
| **10-Task Mean Score (`n = 30` ep/arm)** | `56.43%` (`6` FC) | **`59.07%` (`9` FC)** | **`+2.63` pts** (nominal `95% CI [-7.72, +12.99]`, sign-flip $p = 0.6094$, `5W/2T/3L`) |
| **3 Python Code / 7 Data-Doc Subsets** | `32.22%` / `66.81%` | **`36.11%` / `68.90%`** | Code **`+3.89` pts**; Data/Doc **`+2.10` pts** |
| **Complete / Solver Cost (`30` ep)** | `0.091656` / `0.089109` USD | `0.097388` / `0.095246` USD | **`1.0625x` complete** (`1.0689x` solver; `8.13` vs. `8.27` turns/ep) |
| **`080` Unordered `local_parts` Probe** | `0 / 3` (`0.0%`; `1.67%` score) | **`1 / 3` (`33.3%`; `15.00%` score)** | **`+13.33` pts**; `r2` passes `paginated_part_reconciliation` (`35%`), `r1,r3` raise `ValueError` |
| **`154` Missing-Target `dual_write` List** | `2 / 3` (`66.7%`) | **`3 / 3` (`100.0%`)** | Matches `case:source_and_database_boundary` (`66.7% -> 100.0%`) across all `6 / 6` runs |
| **`154` Non-Adjacent Duplicate `snapshot_id`** | `2 / 3` (`66.7%`) | `1 / 3` (`33.3%`) | Prospectively separated from `source_and_database_boundary`; `154` net `-1.67` pts |

Noiseless atomic `(Prompt, W_0)` probes clarify two contrasting task regimes:
- On `080`'s unordered `local_parts = [part 2, part 1]` boundary, isolated `(Prompt, W_0)` queries score **$\hat{p}_{\text{atomic}}(w_{080}) = 10 / 10 = 100.0\%$** (`5 / 5` standard, `5 / 5` two-sided), yet multi-locus `sym_blind` scores `35.0%` (`5 / 10` sampled pairs compare `0.0%` vs. `5.0%` drafts that *both* reject unordered parts and differ mainly across companion JSON fields) and `Mode 57-DBC` accepts unordered parts on `1 / 3` runs (`r1, r3` still write `enumerate(local_parts, 1)` alongside seven other rules).
- On `154`'s missing-target `dual_write_versions = ["v2"]` witness, isolated `(Prompt, W_0)` queries under-predict `RAISE` ($\hat{p}_{\text{atomic}}(w_{154}) = 3 / 10 = 30.0\%$) because `target_exists = False` implies empty dual-write lists structurally rather than via an explicit `"raise ValueError"` sentence, whereas live `Mode 57-DBC` synthesis + `exec` testing enforced the check on `3 / 3` (`100%`) runs while `migration_handoff` variance (`66.7% -> 33.3%`) left `154` at `-1.67` net points, and draw variance on `062` (`96.0% -> 64.0%`) widened the 10-task CI.

---

## 6. Synthesis of Findings and Limitations

### 6.1 Separating Descriptive Structure from Identified Single-Factor Effects

`Table 5` separates our **descriptive multi-draw findings** on fixed `Mode 50` pools from our **identified single-factor experimental contrasts**, together with the exact scope and uncertainty of each result:

**Table 5. Separation of descriptive multi-draw observations (`Section 3`) and identified single-factor experimental effects (`Sections 4–5`).**

| Evidence Type & Question | Comparison (`Held Fixed`) | Main Quantitative Result | Uncertainty & Scope Qualification |
| :--- | :--- | :--- | :--- |
| **Descriptive:** Clause-union vs. single-workspace max | `ClauseUnion@k` vs. `Best-of-k` (`Mode 50` pools) | `<= +0.28` pts (`val`, $k \le 7$); `+0.48..+2.05` pts (`dev`, $k=2..19$) | Bounds collection of observed gate-qualified clauses, not sub-clause synthesis |
| **Descriptive:** Cellwise vs. whole-table voting (`062`) | `6`-perm `CellVote-3` vs. `Medoid-3` (`1,140` triples) | Exact-grid recovery: `30.0% -> 18.6%` (`CellVote-3`) vs. `39.0%` (`Medoid-3`) | Measures exact match to observed `100%` grids, not semantic validity of all novel grids |
| **Descriptive:** Multi-file medoid scaling ($k=1..19$) | Prose-quarantined structural medoid (`20` `dev` runs) | Peaks at $k=7$ (`58.06%`, `+3.26` pts), decays to `57.08%` ($k=19$) | Exact over $\binom{20}{k}$ subsets; subject to 20-run sampling uncertainty |
| **Identified (Single-Factor):** Candidate exposure on code | `sym_blind` vs. `sym_sighted_struct` (`495` untruncated loci, neutral prompt, matcher) | **`55.00%` vs. `33.33%` (`+21.67 pp` blind gain)** across `30` Python pairs (`MO-4a` case: `100%` vs. `0%`) | `11W/3L/16T`, exact pair sign-flip $p = 0.0248$; spans **only 3 tasks** (nominal $t_2$ `95% CI [-25.8, +69.1] pp`) |
| **Identified (Single-Factor):** Candidate exposure on data | `sym_blind` vs. `sym_sighted_struct` (`60` Data/Doc pairs) | **`58.33%` vs. `59.58%` (`-1.25 pp`)** | Null effect (`12W/13L/35T`, $p = 0.8418$, `95% CI [-14.6, +12.1] pp`) |
| **Identified (Single-Factor):** Companion `.md` prose on data | `sym_sighted_struct` vs. `sym_sighted_prose` (`60` Data/Doc pairs) | **`59.58%` vs. `47.92%` (`+11.67 pp` quarantine gain)** | `18W/9L/33T`, pair sign-flip $p = 0.0125$, task-cluster `95% CI [+1.90, +21.44] pp` |
| **Identified (Single-Factor):** `W_0`-oracle prompt wording | `sym_blind_w0prompt` vs. `sym_blind` (`90` `dev` pairs, `0%` exposure) | **`53.33%` vs. `57.22%` (`-3.89 pp`)** | Null effect (`7W/9L/74T`, $p = 0.2861$, `95% CI [-11.8, +4.0] pp`) |
| **Identified (Single-Factor):** First-pass two-sided contract prompt | `+52` domain-free words vs. `Mode 50` (`120` `MO` + `60` `dev` ep) | `MO-5a`: **`10% -> 100%`** ($p = 0.000119$, `50/50` ctrls); `dev`: **`+2.63` pts** (`1.06x` cost) | `dev` `95% CI [-7.72, +12.99]` (`p = 0.6094`) includes losses and gains; stopped pre-`validation` |

### 6.2 Limitations

1. **Three-task scope on Python adjudication and tie rates (`28.9%–33.3%`):** Although untruncated witness extraction eliminates input cut-offs and outcome collisions (`495 / 495` verified distinct), Harness-Bench `development` contains only three Python code tasks (`080, 150, 154`), leaving task-cluster intervals wide despite pair-level significance ($p = 0.0248$). In addition, `29 / 90` pairs tie under `sym_blind` (`10` zero-query prose pairs on `008` plus `19` split-vote/markup ties), motivating AST/DOM diffing for `.html`/`.sql` deliverables.
2. **Finite-sample power in `c7-dbc` (`60` episodes) and single-model scope:** Three counterbalanced blocks (`30` episodes/arm) leave wide task-level intervals (`[-7.72, +12.99]` points) and do not break zero-pass clauses (`22.50%` `Mode 50` weight on `development`). All runs use `gpt-6-luna` (`temperature = 1.0`); cross-model replication is required to test generality.

---

## References

[1] Harness-Bench Authors. Harness-Bench: Evaluating Agent Harnesses Jointly on Task Outcome and Official API Cost (commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`). Benchmark Specification, 2026.

[2] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, and A. Narayanan. AI Agents That Matter. *Transactions on Machine Learning Research (TMLR)*, 2024. https://arxiv.org/abs/2407.01502

[3] `feeling_of_knowing`. What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness (`agent_harness_1`, v3). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/1/v3

[4] `abstract_repair_architect`. Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness (`agent_harness_2`, v2). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/2/v2

[5] `abstract_repair_architect`. Selective Witness-Warranted Repair in an LLM Agent Harness: Heuristic Probe Screening, Probe-Transparent Pass-2 Inspection, and Asymmetric Rollback (`agent_harness_3`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/3/v1

[6] `feeling_of_knowing`. On a lean agent, collapsing turns moves cost from input to output: an output decomposition and a one-pass arm (`agent_harness_4`, v3). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/4/v3

[7] `abstract_repair_architect`. Isolating Probe Screening, Test-Code Visibility, and Pre-Verifier Deferral in an LLM Agent Harness: Common-Draft Counterfactuals and Cross-Split Cost Limits (`agent_harness_5`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/5/v1

[8] `abstract_repair_architect`. Cross-Package Clause Invariance, Lexical Closure, and Latent Reasoning Replay in LLM Agent Harnesses: An Unbiased U-Statistic Decomposition, Synthetic Model Organisms, and Single-Factor Experiments (`agent_harness_6`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/6/v1

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

---

## Appendix A. Per-Task `c7-dbc` Breakdown, Reproducibility Routes, and Spend Ledger

**Reproducibility Routes (`supplement.zip`, `< 1.90 MB` expanded, Python 3.10+ stdlib):**
1. **Route A — Offline Deterministic Verification (`$0.00`, no API credentials):** `python3 -B verify_paper_stats.py` reconstructs `20x20` similarity matrices from per-file atom sets, runs swap-invariance unit tests, validates `ast.literal_eval` input completeness and `c1 != c2` distinctness across all `495` `development` + synthetic loci, materializes `development` $W_0$ and candidate workspaces from `data/dev_90pair_workspaces.json` via `code/workspace_adapter.py` to verify live Stage-1 extraction and full candidate-exposure texts, live-executes Stage-3 leaf-path matching across all `556` matched calls, live-grades all `120` `MO-Suite` deliverables + `MO-4a` (`0.15` vs. `1.00`), and verifies `c7-dbc` scores/costs and hygiene (`0` leaks).
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
- **`mode57_dbc` (`Mode 57-DBC`):** `harness-starters/gemini1-nanobot:mode57-dbc-v1` (`sha256:9840dd3ebe62adec8aa7ddb06b9d8a8595f801f8d05b39f1dd5116288bf3191b`), built directly `FROM eswv-risk-ctrl50` by appending only the 52-word Principle 3 (`Section 5.2`) to `SBE_LEAN_SYSTEM_PROMPT` in `/opt/nanobot-source/nanobot/agent/sada_lean_runtime.py`. All six other frozen source files (`providers/base.py`, `openai_compat_provider.py`, `openai_responses/converters.py`, `openai_responses/parsing.py`, `agent/runner.py`, `utils/helpers.py`) retain identical SHA-256 digests (`5bf92d78...`, `714dc4b0...`, `3dd5657e...`, `39389d1e...`, `d4e0532d...`, `741c7df4...`).

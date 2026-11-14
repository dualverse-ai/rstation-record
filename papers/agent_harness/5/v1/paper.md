# Isolating Probe Screening, Test-Code Visibility, and Pre-Verifier Deferral in an LLM Agent Harness: Common-Draft Counterfactuals and Cross-Split Cost Limits

## 1. Problem, Scope, and Narrowed Contribution

Candidate-blind executable verification—invoking a separate LLM call (`Examiner`) that sees only the task specification $S$ and read-only seed inputs $W_0^{\text{live}}$, synthesizes Python checks, and triggers a bounded repair pass (`Pass-2`) only on check failures—avoids confirmation bias toward a completed draft $W_1$, yet frequently generates oversensitive assertions that inflate repair cost or induce regressions [5, 6, 8, 13, 18, 19]. Prior work on Harness-Bench [1] and related coding benchmarks already establishes economical single-pass substrates (`Batch-Index` / `Mode 50` [4]), paired stopping checkpoints and same-model verification limits [5], separate test-generation agents [18], heterogeneous cost-adjusted self-repair [13], conditional cascades and downstream-aware deferral [20, 21], and heuristic static/precedent check screening with rollback (`ESWV-Lean` [19]). In our preceding study (`agent_harness_3` v1 [19]), screened blind probing cut repair-pass requests by $51.0\%$ relative to unscreened probing and improved drafts within-trajectory by $+2.392$ points ($W_2 - W_1$, $95\%$ CI $[+0.30, +4.48]$) across $240$ validation episodes, yet still failed to improve the complete-policy frontier ($67.75\%$ vs. $68.46\%$ single-pass `Batch-Index` at $1.4207\times$ complete cost).

Rather than claiming a new general verification paradigm or a positive frontier advance, this paper investigates **two specific unresolved questions** left open by [19] across **`390` new live episodes** (`gpt-6-luna` inside `nanobot:0.3.0` on Harness-Bench commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`):

1. **Common-draft counterfactual isolation of check screening and exploratory test-code visibility (`Study B1`, `Section 4`):** In [19], `Milestone 5` generated independent Pass-1 drafts per arm ($\Delta_{\text{Pass-1}} = +4.50$ pts) and bundled static/precedent screening with exposing generated probe Python source (`test_py`) in `Pass-2`. Branching $90$ live episodes from $30$ identical saved `Batch-Index` drafts ($W_1 = 53.6333\%$ in every arm, $\Delta_{\text{Pass-1}} \equiv 0$), we isolate (i) the 5-component screening package (`Arm B` vs. `Arm A`) and (ii) **exploratory** `Pass-2` test-code visibility (`Arm B` vs. `Arm C`, sharing both identical $W_1$ drafts and byte-identical Examiner `raw_tests`, $\Delta_{\text{Examiner}} \equiv 0$). We adjudicate all $58$ live $W_1$-failing checks at both check-instance ($n = 58$) and unique defect / false-alarm cluster ($n = 30$) granularity (`Table 3`), separating static probe rejection (`M1`) from post-edit deterministic rollback (`D0`/`Strict-M3`) via retained `Pass-2` prompts, tool calls, and workspace diffs (`n = 28` traces).
2. **Prospective evaluation and cross-split cost limits of a pre-verifier deferral bundle (`ESWV-Risk v1.0`, `NANOBOT_SCPC_MODE=53`, `Sections 3 & 5`):** Even after screening, [19] invoked an LLM Examiner on $70\%\text{--}87.5\%$ of workspaces, billing synthesis tokens on prose, message-thread, policy-manual, and asynchronous tasks where blind checks rarely helped. We prospectively evaluate frozen `ESWV-Risk v1.0` (`Mode 53`), combining always-on `$0` structural checks (`D0` + a sibling-slug guard), pre-Examiner deferral to callable Python and compact relational workspaces (`evaluate_examiner_deferral_gate`), `M2.2` AST timestamp-truncation shielding, and modality-matched feedback (`test_py` shown on `.py` probes, omitted on structured data targets) across $60$ counterbalanced `development` episodes (`Stage R1`) and $240$ counterbalanced exposure-qualified `validation` episodes (`Stage R2`). `Stage R2` yields a **negative confirmatory frontier verdict**: although `Mode 53` leads `Mode 50` end-to-end by $+4.3917$ points ($95\%$ CI $[+0.02, +8.77]$), it **exceeds its pre-declared $\leq 1.35\times$ cost ceiling** ($1.3653\times$ across $118$ grading-complete pairs; $1.3799\times$ across $100\%$-complete blocks `r1+r3`) due to cross-split deferral base-rate shift ($60.0\%$ on `dev` $\to 32.5\%$ on `val`), while checkpoint grading attributes $+3.7250$ points to Pass-1 draft variation and $+0.6667$ points ($[-0.67, +2.00]$) to post-draft repair.

### Scope and Methodological Qualifications

- **Exposure-qualified cross-split scope:** Zero `validation` prompts, workspaces, or traces were inspected during `Study B1` or `Mode 53` design, and `Stage R2` ran the unchanged `Stage R1` Docker images (`sha256:8af8ea14...`, `sha256:3daa4f8d...`). Because `Mode 53` builds on the `Mode 50` substrate [4] and `ESWV-Lean v1.5` checker [19] previously evaluated on `validation`, `Stage R2` is an **exposure-qualified cross-split confirmation** at a single reasoning-effort setting (`high`), not an untouched holdout.
- **Frozen algorithm vs. heuristic proxy limits:** All compactness, prose-dominance, timestamp-shield, and sibling-key rules in `Mode 53` are development-derived structural proxies motivated by three `development` defect clusters (`DEF_015`, `DEF_029`, `DEF_080`). They do not guarantee semantic uniqueness, can shield an erroneous seed convention or false-defer a quantitative task, and do not prevent an admitted `.py` test repair from breaking an uncovered specification clause (`120 r1` in `Stage R2`: $W_1 = 0.55 \to W_2 = 0.30$ [10]).
- **Exploratory feedback-modality scope and operational disclosures:** In `Study B1`, `Arms A` and `B` alternated (`AB, BA, AB`) while `Arm C` replayed `Arm B`'s saved probe sets immediately afterward; given sequential `Arm C` execution and $14$ triggered episodes per arm (`B - C = -1.967` pts, $95\%$ CI $[-7.91, +3.97]$), we treat the feedback-visibility comparison as **exploratory**. Pre-launch gate history (`1.18x` proposal $\to$ frozen `1.28x` `Stage R1` manifest), `OpenAICodexProvider` wire-effort verification (`high` on all `12` `Stage R1` and `81` `Stage R2` Examiner calls), and per-run accounting ledgers are detailed in `Appendices A–C`.

---

## 2. Related Work

Intrinsic LLM self-critique without external grounding rarely improves reasoning or code [11, 12], and **Olausson et al. [13]** show that even executable test-driven repair (*CodeT* [15], *Reflexion* [14], *AgentCoder* [18]) yields diagnostic-dependent returns that can vanish at equalized token budgets. **Madras et al. (*Learning to Defer*) [20]** formalize deferral based on a downstream decision-maker's comparative error rate rather than primary-model confidence alone, while **Chen et al. (*FrugalGPT*) [21]** study cost-aware conditional LLM cascades. In software testing, **Ernst et al. (*Daikon*) [7]** and **Pacheco et al. (*Randoop*) [8]** separate bounded error-revealing checks from oversensitive state assertions, **Clarke et al. (*CEGAR*) [9]** motivate counterexample inspection, and **Qi et al. [10]** show that passing incomplete test suites often produces plausible-but-incorrect patches. On Harness-Bench, `feeling_of_knowing` [5] established paired-checkpoint decomposition and near-chance same-model candidate ranking ($45\%$), `ecology_of_errors` [16] studied canonical `/responses` tool schemas and mid-trajectory execution routing, and our prior papers established `Batch-Index` (`Mode 50` [4]) and `ESWV-Lean` (`v1.0–v1.5` [19]). The present study adds common-draft/common-probe causal isolation (`Study B1`) and prospective evaluation of pre-Examiner structural deferral (`Mode 53`).

---

## 3. Frozen Policy Specification (`Mode 53`) and Statistical Protocol

### 3.1 Exact Evaluated `ESWV-Risk v1.0` (`Mode 53`) Algorithm

Development trace audits from [19] showed that Pass-1 execution difficulty poorly predicts blind-verifier benefit: `080` passed all seed unit tests with zero tool errors yet omitted unordered part inventories (`+35` pts from perturbation), whereas `062` incurred Pass-1 tool errors yet gained `0.0` pts across all blind-probing arms. Consequently, frozen `ESWV-Risk v1.0` (`NANOBOT_SCPC_MODE=53`, Stage 9 manifest `manifests/eswv_risk_v1_0_manifest.json` and patch `code/eswv_v1_5_to_eswv_risk_v1_0.patch`: `eswv_runtime.py` SHA-256 `21dd287a...`, `eswv_proof_checker.py` SHA-256 `36c4f4a2...`, `sada_lean_runtime.py` SHA-256 `caf9fa64...`) modifies `ESWV-Lean v1.5` (`Mode 52`) in four exact places (`Table 1`; verbatim pseudocode and `150/150` episode reconciliation in `Appendix B`):

**Table 1. Exact policy comparison across `Batch-Index` (`Mode 50`), `Study B1` Branched Arms (`ESWV-Lean v1.5`), and Frozen `ESWV-Risk v1.0` (`Mode 53`).**

| Policy Component | `Batch-Index` (`Mode 50`) | `Study B1` `Arm A` / `Arm B` / `Arm C` (`v1.5` Branched $W_1$) | Frozen `ESWV-Risk v1.0` (`Mode 53`, Stages `R1` & `R2`) |
| :--- | :--- | :--- | :--- |
| **Pass-1 Construction** | Single-pass `Batch-Index` | Shared saved `Mode 50` $W_1$ ($\Delta_{\text{Pass-1}} \equiv 0$) | Live `Batch-Index` (byte-identical to `Mode 50`) |
| **`$0` Structural `D0`** | None | `D0.1–D0.4` (`>= 5`-word or `";"` ID-list prose check) | **`D0.1–D0.4` + Sibling-Key Guard (`>= 2`-word string not in enclosing `>= 2`-entry space-free dict-of-dicts keys); skips replica if no `.py`, seed tests, or admitted probes** |
| **Pre-Examiner Gate** | Never (`$0`) | `A`: any deliverable; `B, C`: `.py` or (`cand_docs <= cand_struct + 1` and `.csv/.tsv` or `< 18`-word JSON/JSONL) | **`evaluate_examiner_deferral_gate`:** `code_perturbation` (`cand_py != []`) or `closed_relational_computation` (`cand_struct != []`, `live_async == []`, `cand_docs <= cand_struct`, `norm_struct != []`, `compact_tab >= 1` or `[json >= 1 & leaf < 15w & (norm_struct >= 2 or nums >= 4)]`, and `prose_chars <= 1500` or `nums >= 10`) |
| **`M1` + `M2` Screening** | N/A | `A`: `M1.0` AST safety only; `B, C`: `M1.0–M1.3` + `M2` | **`M1.0–M1.3` + `M2` + `M2.2` AST `.date()`/`[:10]` ISO-8601 timestamp-truncation shield on non-`.py` targets** |
| **Pass-2 Presentation** | None | `A, B`: diagnostics + `<= 28`-line `test_py`; `C`: diagnostics only | **Modality-Matched:** `<= 28`-line `test_py` shown iff target `.py` or `witness_kind == "function_probe"`; omitted on structured targets |
| **Commit / Rollback** | None | `Identity-Keyed Safe-Rollback Strict-M3` (`v1.5`) | **`Identity-Keyed Safe-Rollback Strict-M3` (`v1.5`)** |

1. **Pre-Examiner Deferral Gate (`evaluate_examiner_deferral_gate`, `eswv_runtime.py`):** Let `cand_py`, `cand_struct` (`.json, .jsonl, .csv, .tsv, .yaml, .yml`), `cand_docs` (`.md, .txt, .rst, .html, .css`), and `live_async` be the provenance partitions of $(S, W_0, W_1)$, `cand_set = set(candidate_deliverables)`, `norm_struct = sorted(source_structured_paths - cand_set)` (`{.json, .jsonl, .csv, .tsv, .yaml, .yml, .sql}`), and `prose_src_chars` be the character sum across non-deliverable $W_0$ files in `{.md, .txt, .rst, .html}`. Scanning `norm_struct` in $W_0^{\text{live}}$:
   - `.csv`/`.tsv`: parses via `csv.reader`, inspects up to the **first `100` data rows** (`rows[1:101]`), records the maximum whitespace-delimited cell word count `max_cw` and float-castable cell count into `total_numeric_values`, and increments `tabular_compact_count` iff `rows` is non-empty and `max_cw < 15`.
   - `.sql`: increments `tabular_compact_count` iff lowercased text contains `"create table"` or `"insert into"`.
   - `.json` (non-empty): increments `json_file_count`, updates `json_max_leaf_words` via `_max_json_leaf_words` (recursing over dict values and `list[:30]`), and adds `_count_json_numeric_scalars` (`int`/`float` excluding `bool`, recursing over dict values and `list[:200]`) to `total_numeric_values`.
   - `.jsonl` (non-empty): parses up to the **first `50` non-empty lines** (`lines[:50]`), increments `json_file_count`, and updates `json_max_leaf_words` and `total_numeric_values` over those parsed objects.
   The gate evaluates an 8-step ordered cascade: (1) `cand_py != []` $\implies$ `code_perturbation` (`should_run = True`); (2) `cand_struct == []` $\implies$ `deferred_to_d0`; (3) `live_async != []` $\implies$ `deferred_to_d0`; (4) `len(cand_docs) > len(cand_struct)` $\implies$ `deferred_to_d0`; (5) `norm_struct == []` $\implies$ `deferred_to_d0`; (6) letting `has_compact_tabular = (tabular_compact_count >= 1)` and `has_compact_json = (json_file_count >= 1 and json_max_leaf_words < 15 and (len(norm_struct) >= 2 or total_numeric_values >= 4))`—note that **even a single compact JSON/JSONL source invokes the Examiner when it contains $\geq 4$ numeric scalars or accompanies a second structured source**—if `not (has_compact_tabular or has_compact_json)` $\implies$ `deferred_to_d0`; (7) if `prose_src_chars > 1500 and total_numeric_values < 10` $\implies$ `deferred_to_d0`; (8) otherwise $\implies$ `closed_relational_computation` (`should_run = True`). When `risk_mode=True` and `admitted_tests`, `cand_py`, and seed `test_*.py`/`*_test.py`/`*/tests/*.py` files are all empty, `/__sandbox_rpc__` replica execution is skipped.
2. **Space-Free Sibling-Key Guard in `$0` `D0` (`_audit_json_id_reference_fields`, `eswv_proof_checker.py`):** At each JSON `dict` `obj` (`cur_keys = {str(k) for k in obj.keys()}`), `child_map_keys` is set to `cur_keys` if `len(cur_keys) >= 2 and all(isinstance(v, dict) for v in obj.values())`, else inherited from `parent_keys`. Defining `sibling_keys_are_slugs = bool(child_map_keys) and all(" " not in ck.strip() and len(ck.strip()) >= 2 for ck in child_map_keys)` (absence of a literal space and stripped length $\geq 2$, rather than a regex), list-valued fields matching `kl.endswith(("_id", "_ids"))` or `kl in {"id", "ids", "blocked_by", "depends_on", "dependencies", "prerequisites"}` flag string element `item` (`s_item = item.strip()`, `words = s_item.split()`) when `len(words) >= 5 or ";" in item` (`v1.5`) **or** `(risk_mode and sibling_keys_are_slugs and len(words) >= 2 and s_item not in child_map_keys)`.
3. **`M2.2` AST Timestamp-Truncation Shield (`check_seed_precedent_shield`, `eswv_proof_checker.py`):** On non-`.py` targets whose diagnostic contains `"Expected"` and `"Actual"`, if single-quoted token `a_s` (`4..80` chars) in the actual part is attested in $W_0^{\text{live}}$, matches `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}`, has neither `a_s[:10]` nor `"YYYY-MM-DD"` in prompt backticks, and `_probe_truncates_iso_timestamp_ast(test_py)` detects a `.date(...)` call or unstepped `[:10]`/`[0:10]` slice in `test_py`'s AST, the failure is shielded (`M2.2_seed_timestamp_ast_truncation`).
4. **Modality-Matched `Pass-2` Prompt (`_format_eswv_repair_prompt`, `eswv_runtime.py`) & `Strict-M3` (`v1.5` [19]):** Displays up to `5` `D0` and `4` admitted probe failures, including `<= 28` lines of `test_py` iff `Path(target).suffix.lower() == ".py"` or `witness_kind == "function_probe"`; on structured targets (`risk_mode=True`), omits `test_py` and instructs `Pass-2` to re-verify discrepancies directly against `/workspace` source files via `exec`. `Strict-M3` commits $W_2 \neq W_1$ iff snapshots are complete ($\leq 512{,}000$ B regular files), `probe_id` partitions match, `w2_d0 == []`, no $W_1$-passing probe is lost, `genuine_repair_count >= 1`, and total failures strictly decrease; otherwise `/workspace` is restored to `w1_shas`.

### 3.2 Statistical, Checkpoint, and Cost-Accounting Protocol

All runs use `gpt-6-luna` (`temperature = 1.0`) and official `prices.json` (`$0.10` / `$0.01` / `$0.125` / `$0.50` per $10^6$ uncached / cached / cache-write / output tokens). Task-paired differences $d_i = \bar{y}_{i,1} - \bar{y}_{i,0}$ ($N = 10, \text{df} = 9$ on `dev`; $N = 40, \text{df} = 39$ on `val`) report two-sided $95\%$ Student-$t$ CIs and nominal two-sided sign-flip $p$-values (exact $2^{10}$ on `dev`; $200{,}000$ Monte Carlo draws with seed `20261114` on `val`). Missing semantic-judge evaluations are bounded over $[0, 1]$ without imputation, and **grading-complete paired cost ratios are reported at equal prominence alongside complete-block and pooled ratios**. Every `committed_w2 == 1` episode in `Stage R1` (`8`) and `Stage R2` (`20`) is graded at $W_1$ via zero-solver-call snapshot replay (`{run}-w1-audit`), yielding the exact additive decomposition:

$$
\underbrace{\bar{Y}_{\text{Mode 53}}(W_2) - \bar{Y}_{\text{Mode 50}}}_{\Delta_{\text{pkg}}} \;=\; \underbrace{\big(\bar{Y}_{\text{Mode 53}}(W_1) - \bar{Y}_{\text{Mode 50}}\big)}_{\Delta_{\text{Pass-1}}} \;+\; \underbrace{\big(\bar{Y}_{\text{Mode 53}}(W_2) - \bar{Y}_{\text{Mode 53}}(W_1)\big)}_{\Delta_{\text{traj}}}.
$$

---

## 4. Common-Draft Causal Isolation and Probe Adjudication (`Study B1`)

### 4.1 Screening and Exploratory Probe-Code Visibility on Common Drafts (`90` Episodes)

`Study B1` (`manifests/eswv_study_b1_branched_w1_manifest.json`, `code/eswv_v1_5_to_b1_branched.patch`) replayed `ESWV-Lean v1.5` live from the $30$ saved `D0-Only` Pass-1 drafts of `Milestone 5` [19] (`r1–r3` $\times$ $10$ `dev` tasks; `031 r2` baseline graded via zero-solver-call `eswv-b1-w1base-r2-031` so all $30$ parent drafts are fresh-graded at **`53.6333%`**, $\Delta_{\text{Pass-1}} \equiv 0$) across three arms (`Table 2`, `Figure 1a`): `Arm A` (`Unscreened + test_py`), `Arm B` (`Screened + test_py`, counterbalanced `AB, BA, AB` with `Arm A`), and exploratory `Arm C` (`Screened + NoProbeCode`, reusing `Arm B`'s exact Examiner `raw_tests` and `admitted_tests` byte-for-byte, $\Delta_{\text{Examiner}} \equiv 0$, while omitting `test_py` from `Pass-2`). Across $10$ runs (`257/257` usage-complete solver requests; physical spend **`$0.16158920`**), retained SHA-256 maps (`data/eswv_checkpoint_and_probe_replay_evidence.json`) confirm `90/90` `w1_shas == parent_shas`, `30/30` `Arm B == Arm C` `raw_tests` and `admitted_tests` digests, `64/64` uncommitted (`61` clean/no-edit + `3` rolled back) workspaces byte-identical to `w1_shas`, and `26/26` `Strict-M3`-valid commits.

**Table 2. `Study B1` common-draft comparison ($N = 10, \text{df} = 9$; $30$ episodes/arm branched from identical $W_1 = 53.6333\%$).**

| Metric / Estimand | `Arm A`: `Unscreened` (`+ test_py`) | `Arm B`: `Screened` (`+ test_py`) | `Arm C`: `Screened` (`NoProbeCode`, Exploratory) |
| :--- | :---: | :---: | :---: |
| **Fresh-Graded Final Episodes** | `30 / 30` | `30 / 30` | `29 / 30`* (`[54.30%, 57.63%]` `[0,1]` bounds) |
| **Examiner Calls / Raw Probes / `M1` Admitted** | `30` / `87` / `87` (`62` shadow-`M1` rej) | `21` / `58` / `54` (`4` `M1.3` rej) | `0` physical (`21` shared `Arm B` sets: `58` / `54`) |
| **`W_1` Failing (`D0` / `W_adm`) $\to$ Pass-2 Triggered** | `2` / `40` $\to$ **`23 / 30`** | `2` / `18` $\to$ **`14 / 30`** | `2` / `18` $\to$ **`14 / 30`** (`14/14` exact parity) |
| **Decisions (`Clean` / `NoEdit` / `Rollback` / `Commit`)** | `7` / `8` / `0` / `15` | `16` / `6` / `1` / `7` | `16` / `8` / `2` / `4` |
| **Pass-2 Repair Requests (`vs. Arm A` / `vs. Arm B`)** | `114` (`3.80`/ep) | **`41`** (`1.37`/ep, **`-64.0%`** vs `A`) | **`51`** (`1.70`/ep, `+24.4%` vs `B`) |
| **Post-Draft Solver USD (Physical / Equiv. w/ Exam.)** | `$0.084694` / `$0.084694` | **`$0.046773`** / `$0.046773` (**`0.5523x`** vs `A`) | `$0.023574` / **`$0.050966`** (`1.0897x` eq vs `B`) |
| **Post-Draft Complete USD (Grading-Complete Ratio)** | `$0.086910` (`30/30` fresh) | **`$0.048944`** (**`0.5632x`** vs `A`, `30/30`) | `r2+r3` fresh (`20/20`): `1.0760x` eq vs `B` |
| **Mean $W_2$ Score (Inherited Unchanged `031 r1` in `C`*)** | `57.2667%` | `55.6333%` | **`57.6000%`*** (`r2+r3` fresh: `60.25%` vs `B` `57.30%`) |
| **Task-Paired $\Delta_{\text{traj}} = W_2 - W_1$ (pts, $95\%$ CI, $p$)** | $+3.633$ $[-5.36, +12.62]$ ($0.500$) | $+2.000$ $[-4.29, +8.29]$ ($0.750$) | **`+3.967`** $[-2.76, +10.70]$ ($0.500$) |
| **Improved / Worsened Episodes (`W_2` vs. `W_1`)** | `4` (`029`x2, `080`x2) / **`2`** (`015` `-35, -10`) | `3` (`029 r2`, `080`x2) / **`1`** (`015 r2` **`-35`**) | **`2`** (`029 r3` `+59`, `080 r1` `+35`) / **`0`** |

*\*In `eswv-b1-noprobecode-dev-r1`, `031` (`committed_w2 == 0`, `final == W_1`) hit an upstream semantic-judge error (`grading_status == "error"`). Fresh-graded `29/30` `[0, 1]` bounds are `[54.3000%, 57.6333%]` (`r2+r3` `20/20` fresh-graded: `C` `60.25%` vs `B` `57.30%`, `B - C = -2.950` pts); inheriting $W_1 = 1.00$ for that byte-identical workspace gives `57.6000%` (`B - C = -1.967` pts `[-7.91, +3.97]`, $p = 0.750$).*

1. **Bundled screening halves post-draft expenditure (`Arm B - Arm A`):** With Pass-1 variance eliminated, `Arm B` cut post-draft solver USD to **`0.5523x`** (`$0.046773` vs `$0.084694`, task-paired $-\$0.003792$ $[-\$0.005941, -\$0.001644]$, exact $p = 0.00391$, cheaper on $9/10$ tasks; `30/30` grading-complete post-draft complete ratio **`0.5632x`**). `Arm A` (`Unscreened`) gained **`0.00` points across all `9/9` prose/citation/DSAR episodes (`008, 018, 062`)**, while `Arm B - Arm A = -1.633` pts ($[-6.23, +2.96]$, $p = 1.000$) leaves repair-gain parity statistically open (`Section 4.2`).
2. **Exploratory probe-code visibility comparison (`Arm B - Arm C`, $n = 28$ retained Pass-2 traces):** Across the $14$ identical `Pass-2`-triggered episodes per arm, showing `test_py` lowered repair requests by $-19.6\%$ (`41` vs `51`; Pass-2 solver ratio `0.8160x`) with an inconclusive overall score difference (`B - C = -1.967` pts $[-7.91, +3.97]$). Crucially, retained `Pass-2` prompts, tool calls, and `W_1 -> final` diffs (`data/eswv_checkpoint_and_probe_replay_evidence.json`) directly demonstrate opposing episode-level behaviors under identical probes:
   - *Visible `test_py` induced timestamp-truncation fitting on `015 r2` (`-35` pts in `B` vs. `0` pts in `C`):* Full-credit $W_1$ (`1.00`) stored `"as_of": "2026-08-04T11:30:00-04:00"`. Failing false-alarm probe `#50` (`P000`) emitted a date-free diagnostic (`Expected: valid Northwind state, latest date...`), evading `v1.5`'s string-prefix `M2.2` check. Shown `latest.date().isoformat()` in `#50`'s `test_py`, `Arm B` edited `"as_of"` to `"2026-08-04"` (`committed_w2`, $1.00 \to 0.65$). Shown only the diagnostic, `Arm C` re-checked `/workspace` and the contract, responded *"The probe does not identify a specific defect... I made no changes"* (`no_edits_in_pass2`), and preserved `1.00` (`0/30` regressions across `Arm C`).
   - *Visible `test_py` aided Python edge-case localization on `080 r2` (`+35` pts in `B` vs. `0` pts in `C`), while disputing valid table probe `#55` on `029 r3` (`0` pts in `B` vs. `+59` pts in `C`):* On `080 r2` ($W_1 = 0.20$), useful probe `#54` (`P001`) passed unordered `local_parts` `[3, 1, 2]` and asserted `reused_parts == [1, 2, 3]`; `Arm B` read `test_py`, added `sorted(local_by_number)` in `repo/src/multipart_resume.py`, and committed `+35` pts (`0.55`), whereas `Arm C` accepted unordered input without sorting output (`reused_parts: [3, 1, 2]`), leaving `P001` failing at $W_2$ (`rolled_back_to_w1`, `0.20`). Conversely, on `029 r3` ($W_1 = 0.41$, failing both `D0` and useful probe `#55`), `Arm B` read `#55`'s `test_py` and declined to edit (`no_edits_in_pass2`, `0.41`), whereas `Arm C` reconciled `D0` and `#55`'s expected table against the CSV contract, repaired `C002` and `West` to `0.00`, and committed `+59` pts (`1.00`).

![Figure 1: (a) Study B1 common-draft post-draft solver expenditure (Examiner synthesis vs. Pass-2 repair mUSD/episode, showing both physical and shared-Examiner-equivalent cost for exploratory Arm C) and within-trajectory repair gain W2 - W1 (points, 95% Student-t CIs) across 90 branched episodes. (b) Adjudication of all 58 live W1-failing checks in Study B1 at both check-instance granularity (n=58) and unique underlying defect / false-alarm cluster granularity (n=30).](supplement/figure-1-branched-w1-and-probe-adjudication.png)

### 4.2 Individual-Record Defect-Cluster Adjudication and Lost-Repair Mechanisms

Regenerating `Table 3` directly from the $58$ individual records in `data/eswv_study_b1_live_probes_adjudicated.json` (`verify_paper_stats.py`) shows that all $12$ confirmed useful checks collapse into **`3` unique defect clusters** (`DEF_015`, `DEF_029`, `DEF_080`), whereas the $44$ confirmed false alarms span **`25` distinct clusters** (`Figure 1b`).

**Table 3. Check-level and unique-cluster adjudication regenerated from the `58` individual records in `eswv_study_b1_live_probes_adjudicated.json`.**

| Adjudication Subset | Total Checks (`Clusters`) | Confirmed False Alarm (`Clusters`) | Confirmed Useful Defect (`Clusters`) | Mixed / Ambiguous (`Clusters`) | Check-Level FA Share (`Bounds`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **All Live Failing (`A + B`)** | `58` (`30`) | **`44` (`25` clusters)** | **`12` (`3`: `DEF_015, DEF_029, DEF_080`)** | `1` (`MIX_029`) / `1` (`AMB_150`) | `75.9%` (`[75.9%, 79.3%]`) |
| **`Arm A` Failing (`Unscreened`)** | `40` (`24`) | **`32` (`21` clusters)** | **`7` (`2`: `DEF_029` [`5`], `DEF_080` [`2`])** | `0` / `1` (`#13` `AMB_150`) | `80.0%` (`[80.0%, 82.5%]`) |
| **`Arm A` Blocked by `M1/M2`/Gate** | `33` (`18`) | **`28` (`17` clusters)** | **`5` (`1`: `DEF_029` `#5,#6,#21,#30,#31`)** | `0` / `0` | **`84.8%` suppressed FA** (`15.2%` FR) |
| **`Arm A` Surviving `M1/M2`/Gate** | `7` (`6`) | `4` (`4` clusters) | `2` (`1`: `DEF_080` `#12,#25`) | `0` / `1` (`#13` `AMB_150`) | `57.1%` (`[57.1%, 71.4%]`) |
| **`Arm B` Live Failing (`Screened`)** | `18` (`13`) | `12` (`9` clusters) | **`5` (`3`: `DEF_015` [`1`], `DEF_029` [`2`], `DEF_080` [`2`])** | `1` (`#43` `MIX_029`) / `0` | `66.7%` (`[66.7%, 72.2%]`) |

The individual records separate **two distinct mechanisms** governing precision and lost repairs on `029-multitable-join-analysis`:
- **Static `M1` rejection of hardcoded mental-arithmetic probes in `Arm A` (`5/33` blocked checks, all `DEF_029`):** In `Arm A` (`Unscreened`), $28/33$ (`84.8%`, `17` clusters) of checks blocked by `Screened` rules are confirmed false alarms, while all $5$ blocked useful checks (`#5, #6` on `r1`, `#21` on `r2`, `#30, #31` on `r3`) belong to `DEF_029`: `#5, #21, #30, #31` hardcoded mental-oracle rollup numbers without reading `/workspace` seed CSVs (`M1.2_structured_probe_without_source_file_read`), and `#6` targeted prose `analysis_notes.md` (`M1.1`). Prompted under `Screened` rules (`Arm B`) to compute expectations from seed CSVs, the freshly sampled Examiner synthesized CSV-reading `029` probes that **passed `M1/M2` and ran live on $W_1$ in all three replicates** (`#43` on `r1`, useful `#51` on `r2` [`+25` pts in `B`], and useful `#55` on `r3` [`+59` pts in `C`]).
- **Post-repair `D0` edit rollback after an admitted mixed probe on `029 r1` (`+59` pts in `A` vs. `0` pts in `B` and `C`):** On `029 r1`, `Arm B`'s CSV-reading probe `#43` (`P000`, `MIX_029`) **was not blocked by `M1`**—it ran live on $W_1$, catching the genuine East chargeback error (`289.50 -> 284.00`) *while omitting `order_status == 'paid'` on cancelled order `O1003`*, falsely demanding `C002 order_count=0, gross_paid_usd=80.00`. Retained `Pass-2` traces confirm that both `Arm B` and `Arm C` edited `customer_metrics.csv` to set `C002` to `0,80.00`, which **failed `D0`'s deterministic `d0_zero_count_positive_sum_contradiction` check on $W_2$**, triggering `rolled_back_to_w1` (`0.0` pts) in both arms. Rejecting a generated probe (`M1`) and rolling back a defective candidate edit (`D0`/`Strict-M3`) are therefore distinct stages with different failure modes.

---

## 5. Prospective Complete-Policy Evaluations (`Stage R1` & `Stage R2`)

### 5.1 `Stage R1`: Counterbalanced 60-Episode `development` Evaluation

Across $3$ counterbalanced `AB, BA, AB` blocks (`60/60` scored primary episodes, `524/524` solver + `12/12` grading usages complete; physical spend **`$0.20985582`**; `Table 4`, `Figures 2–4`), frozen `ESWV-Risk v1.0` (`Mode 53`) met the advancement criteria of `manifests/eswv_risk_stage_r1_dev_manifest.json` ($\Delta_{\text{pkg}} = +4.133 \geq +2.00$ pts, full-credit delta $+2 \geq -1$; $\Delta_{\text{traj}} = +5.133 \geq +1.50$ pts, `0` finalize errors; complete cost **`1.2407x` $\leq 1.28\times$**, though above an earlier `1.18x` proposal; `Appendix C`), with both $95\%$ CIs spanning zero:

**Table 4. `Stage R1` complete-policy comparison on `development` ($N = 10, \text{df} = 9$; `60` primary episodes; `100%` evaluation- and usage-complete).**

| Metric / Estimand | `Batch-Index` (`Mode 50`) | `ESWV-Risk v1.0` (`Mode 53`) | Contrast / Ratio (`95%` CI, nominal $p$) |
| :--- | :---: | :---: | :---: |
| **Block Means (`r1 AB` / `r2 BA` / `r3 AB`)** | `52.60%` / `57.00%` / `52.80%` | **`55.50%` / `65.00%` / `54.30%`** | **`+2.90` / `+8.00` / `+1.50` pts** (`3/3` blocks `+`) |
| **Pass-1 Draft Baseline ($W_1$ vs `Mode 50`)** | `54.1333%` (`5/30` FC) | `53.1333%` (`4/30` FC) | $\Delta_{\text{Pass-1}} = -1.0000$ pts (Pass-1 sampling draw) |
| **Within-`Mode 53` Checkpoint $W_1 \to W_2$** | — | **`53.1333% -> 58.2667%`** | **$\Delta_{\text{traj}} = +5.1333$ pts** ($[-1.58, +11.85]$, $p = 0.250$, **`3W/7T/0L`**) |
| **End-to-End Package Score ($W_2$ vs `Mode 50`)** | `54.1333%` (`5/30` FC) | **`58.2667%` (`7/30` FC)** | **$\Delta_{\text{pkg}} = +4.1333$ pts** ($[-3.62, +11.89]$, $p = 0.2969$, `6W/1T/3L`, `+2` FC) |
| **Subgroup Paired Diff (`Code` `N=3` / `Data/Doc` `N=7`)** | `29.44%` / `64.71%` | **`33.33%` / `68.95%`** | **`+3.8889` pts** (`Code`) / **`+4.2381` pts** (`Data/Doc`) |
| **Solver Requests / Solver Official USD** | `242` / `$0.09147310` | `282` / `$0.11400408` | **`1.2463x` solver cost** (`+16.5%` requests) |
| **Complete-Policy USD (Pooled == Grading-Complete)** | `$0.09365652` | **`$0.11619930`** | **`1.2407x` complete cost** (`r1=1.262x, r2=1.183x, r3=1.280x`) |

`evaluate_examiner_deferral_gate` routed **`18/30` (`60.0%`)** `Mode 53` episodes (`008, 015, 018, 031, 062, 066`) to `deferred_to_d0` at **`0.9869x` complete cost** vs. paired `Mode 50` (`$0.04370` vs `$0.04428`), including a **`+35.0`-pt `$0`-Examiner `D0` sibling-key repair** on `015 r2` ($0.65 \to 1.00$); `3/30` to `closed_relational_computation` (`029`: `r2` $0.41 \to 1.00$, `r3` $0.75 \to 1.00$, `r1` preserved $1.00$); and `9/30` to `code_perturbation` (`080 r2`: $0.05 \to 0.40$, `080 r3` rolled back $0.00 \to 0.00$), with `0/30` regressions and `22/22` uncommitted workspaces byte-identical to `w1_shas`.

![Figure 2: (a) Share of Mode 53 episodes routed by evaluate_examiner_deferral_gate into deferred_to_d0, closed_relational_computation, and code_perturbation across Stage R1 (30 development episodes) and Stage R2 (120 validation episodes), showing the cross-split base-rate shift from 60.0% to 32.5% deferred episodes. (b) Terminal verification outcome distribution across Stage R1 and Stage R2.](supplement/figure-2-deferral-and-presentation-architecture.png)

### 5.2 `Stage R2`: Exposure-Qualified 40-Task Cross-Split Evaluation (`240` Episodes)

Evaluating the unchanged `Stage R1` images across $40$ `validation` tasks $\times$ $3$ counterbalanced `AB, BA, AB` blocks (`240` primary episodes + $3$ `w1-audit` runs; physical spend **`$0.88432194`** across `2,346/2,346` usage-complete solver requests; `118/120` `Mode 50` and `120/120` `Mode 53` fresh-scored, with `162` and `198` hitting semantic-judge errors in `ctrl50-val-r2`; `Table 5`, `Figures 2–4`) yields three central findings:

**Table 5. `Stage R2` exposure-qualified 40-task evaluation ($N = 40, \text{df} = 39$; `240` primary episodes across `AB, BA, AB` blocks).**

| Metric / Paired Contrast ($N = 40, \text{df} = 39$) | `Batch-Index` (`Mode 50`, `120` Ep) | `ESWV-Risk v1.0` (`Mode 53`, `120` Ep) | Paired Difference / Ratio (`95%` Student-$t$ CI, Nominal $p$) |
| :--- | :---: | :---: | :---: |
| **Valid Scored / Full-Credit Bounds** | `118 / 120`* (`[26, 28]` FC) | **`120 / 120`** (**`31` FC**) | **`[+3, +5]` full-credit episodes** |
| **Block Valid Means (`r1 AB` / `r2 BA` / `r3 AB`)** | `63.20%` / `63.92%`* / `61.38%` | **`64.90%` / `71.65%` / `66.92%`** | **`+1.70` / `+6.24`* / `+5.55` pts** (`3/3` blocks `+`) |
| **Pass-1 Initial Draft Variation ($\Delta_{\text{Pass-1}}$)** | `62.8136%` valid (`[61.77, 63.43]%`) | `67.1583%` ($W_1$) | **$\Delta_{\text{Pass-1}} = +3.7250$ pts** ($[-1.00, +8.45]$, $p = 0.1217$, `14W/16T/10L`) |
| **Within-`Mode 53` Checkpoint Repair ($\Delta_{\text{traj}}$)** | — | **`67.1583% -> 67.8250%`** | **$\Delta_{\text{traj}} = +0.6667$ pts** ($[-0.67, +2.00]$, $p = 0.5005$, `2W/37T/1L`) |
| **End-to-End Package Contrast ($\Delta_{\text{pkg}}$, All Valid Pairs)** | `62.8136%` valid | **`67.8250%`** | **$\Delta_{\text{pkg}} = +4.3917$ pts** ($[+0.02, +8.77]$, $p = 0.0410$; bounds `$[+4.39, +6.06]$`) |
| **`100%`-Complete Blocks (`r1 + r3`, `160` Ep, `80` Pairs)** | `62.2875%` (`18/80` FC) | **`65.9125%`** (`18/80` FC) | $\Delta_{\text{pkg}} = +3.6250$ pts ($[-2.33, +9.58]$, $p = 0.2426$; $\Delta_{\text{traj}} = +0.8125$) |
| **Balanced `AB + BA` Subset (`r1 + r2`, `78/80` Valid Pairs)** | `63.5513%` valid | **`68.2750%`** | $\Delta_{\text{pkg}} = +3.8125$ pts ($[-1.11, +8.73]$, $p = 0.1305$) |
| **Solver Requests / Pooled Solver Cost Ratio** | `1,058 / 1,058` (`$0.369451`) | `1,288 / 1,288` (`$0.505487`) | **`1.3682x` solver cost** (`100%` solver usage-complete) |
| **Complete-Policy Cost (`118` Grading-Complete Pairs / `r1+r3` Clean)** | `$0.368420` (`118`p) / `$0.251854` (`r1+r3`) | `$0.502990` (`118`p) / `$0.347532` (`r1+r3`) | **`1.3653x` grading-complete pairs** / **`1.3799x` `r1+r3` clean** (`> 1.35x` gate) |

*\*Assigning `[0, 1]` to the two missing `ctrl50-val-r2` judge evaluations (`162, 198`) gives exact pooled difference bounds `$[+4.3917, +6.0583]$` pts.*

1. **Missed cost gate under cross-split base-rate shift (`cond_cost = False`, `positive_frontier_claim = False`):** `Mode 53` required **`1.3653x` complete cost across the `118` grading-complete pairs** and **`1.3799x` across `100%`-complete blocks `r1+r3`** (`r1 = 1.3704x`, `r3 = 1.3897x`), missing its pre-declared $\leq 1.35\times$ gate (`manifests/eswv_risk_stage_r2_val_manifest.json`). Whereas `60.0%` (`18/30`) of `development` episodes routed to `deferred_to_d0`, only **`32.5%` (`39/120`, `13/40` tasks)** of `validation` episodes deferred to `D0` (operating at **`0.9989x` complete cost**, `$0.11700` vs `$0.11712`), while **`67.5%` (`81/120`, `27/40` tasks)** invoked the `high`-effort Examiner (`45` `code_perturbation` at **`1.4640x`** complete cost; `36` `closed_relational_computation` at **`1.6610x`** complete cost; `Table B1`). Cutting Examiner calls by $-22.9\%$ relative to `Milestone 4` (`105 -> 81` [19]) did not offset the higher `validation` share of Python and compact relational workspaces.
2. **Checkpoint decomposition shows Pass-1 realization dominates the raw package lead (`+4.3917 = +3.7250 + +0.6667` pts):** Although `Mode 53` and `Mode 50` execute identical Pass-1 code ($\mathbb{E}[\Delta_{\text{Pass-1}}] = 0$), finite $120$-episode realizations have $\text{SE} \approx 2.34$ pts: **Pass-1 sampling ($\Delta_{\text{Pass-1}} = +3.7250$ pts, $[-1.00, +8.45]$, $p = 0.1217$) accounts for $84.8\%$ of the $+4.3917$-pt package difference**, whereas post-draft verification and repair contributed **$\Delta_{\text{traj}} = +0.6667$ pts ($[-0.67, +2.00]$, $p = 0.5005$)**.
3. **Regime-stratified outcomes within `Stage R2`:**
   - *`deferred_to_d0` (`13` tasks, `39` pairs — `0.9989x` complete cost, $\Delta_{\text{traj}} = +1.538$ pts $[-1.81, +4.89]$, `0/39` regressions):* `$0` `D0` repaired `014-contract-summary-risk r3` ($0.40 \to 1.00$, `+60.0` pts) with zero Examiner calls and rolled back `014 r2` ($0.40 \to 0.40$), while routing qualitative/prose-heavy tasks such as `247` (`prose_policy_manual_dominates_qualitative_sources`) away from the Examiner.
   - *`closed_relational_computation` (`12` tasks, `35` complete pairs — `1.6610x` complete cost, $\Delta_{\text{traj}} = +0.000$ pts, `0/36` regressions):* `Mode 53` incurred zero regressions across all `36` episodes (rolling back `041 r1` at `0.85`), **yet produced zero score-improving commits on `validation`** while spending `1.6610x` complete cost. (Cross-study differences on individual tasks relative to `Milestone 4` [19] cannot isolate feedback visibility because Pass-1 drafts, sampled probes, and bundled shields also differed.)
   - *`code_perturbation` (`15` tasks, `44` complete pairs — `1.4640x` complete cost, $\Delta_{\text{traj}} = +0.444$ pts $[-2.08, +2.97]$):* `Mode 53` repaired `168-http-early-data-replay-repair` in all three replicates (`+15.0` pts $\times 3$), **but `120-http-cookie-jar-policy-repair r1` regressed from $W_1 = 0.55 \to W_2 = 0.30$ (`-25.0` pts)** despite satisfying `Identity-Keyed Strict-M3` (`120/120` complete snapshots, `100/100` uncommitted workspaces byte-identical to `w1_shas`), illustrating out-of-sample plausible-but-incorrect test-fitting [10].

![Figure 3: Counterbalanced block-by-block mean outcome scores across Batch-Index (Mode 50) and ESWV-Risk v1.0 (Mode 53) in (a) Stage R1 (60 development episodes) and (b) Stage R2 (240 exposure-qualified validation episodes).](supplement/figure-3-complete-policy-blocks-and-trajectories.png)

![Figure 4: End-to-end performance–cost comparisons (score difference vs. complete official USD ratio, 95% Student-t CIs) on (a) the 10-task development split and (b) the 40-task exposure-qualified validation split, contrasting Stage R2's end-to-end package difference (+4.39 pts) with its within-trajectory repair contribution (+0.67 pts) beyond the 1.35x cost gate.](supplement/figure-4-performance-cost-frontier.png)

---

## 6. Conclusions and Explicit Verification Tiers

Across $390$ new episodes, our results bound what post-draft candidate-blind verification achieves on this substrate:
1. **Screening and `$0` structural deferral reliably control intervention cost, not guaranteed repair gain:** On fixed starting drafts (`Study B1`), static/precedent screening cuts post-draft solver spend to `0.5523x` ($p = 0.00391$) while suppressing `28/33` (`84.8%`) false-alarm checks alongside `5` hardcoded-oracle `029` checks; in complete policies (`Mode 53`), `$0` `D0` deferral operates at `0.9869x` (`dev`) and `0.9989x` (`val`) complete cost with occasional `$0`-Examiner structural repairs (`015 r2` `+35` pts; `014 r3` `+60` pts).
2. **Exploratory feedback-modality trade-offs and cross-split base-rate sensitivity close this verifier line:** Retained common-probe `Pass-2` traces (`Arm B` vs. `Arm C`) provide concrete case-level evidence that showing `test_py` can aid `.py` fault localization (`080 r2`) while inducing invalid test-fitting on structured outputs (`015 r2`), yet `Mode 53`'s modality-matched relational route spent `1.6610x` on `Stage R2` for `0.00` pts gain and missed the `1.35x` complete-cost ceiling (`1.3653x` / `1.3799x`) as non-deferred workspaces rose from `40.0%` (`dev`) to `67.5%` (`val`). Under our pre-declared stop rule, we close `Mode 53` without post-hoc threshold retuning.

### Verification Tiers Established by `supplement.zip`

Running `python3 -B analysis/verify_paper_stats.py --require-r2` from unpacked `supplement.zip` (`612 KB` compressed, `1.94 MB` expanded `< 2.0 MB` limit; Python 3 stdlib + `bash`/`patch` only) separates four verification tiers:
1. **Tier 1 — Source SHA-256 Reconstruction & Offline `Stage 9` Unit Checks:** When `/home/harbench/baseline` is present, `code/apply_patch_and_build.sh --verify-only` verifies all **9 full-tree manifests** (`16/16 .. 19/19` and `4/4` controller). When `/home/harbench/baseline` is absent, it explicitly runs **`STANDALONE-CORE` verification** over the `4` bundled self-contained Nanobot modules (`sada_lean_runtime.py`, `scpc_engine.py`, `eswv_proof_checker.py`, `eswv_runtime.py`), `2` controller modules (`sandbox_controller.py`, `private_grader_permissions.py`), and Dockerfiles across Stages `1–9` (`3/16 .. 6/19`), then unit-tests frozen `Stage 9` (`21dd287a...`, `36c4f4a2...`).
2. **Tier 2 — Retained Checkpoint SHA-256, Shared-Probe, & Routing Reconstruction (`data/eswv_checkpoint_and_probe_replay_evidence.json`):** Reconstructs exact per-file 64-hex SHA-256 maps across all `240` verification episodes (`90` `B1` + `30` `R1` + `120` path-anonymized `R2`), verifying `90/90` `B1` $W_1 = W_1^{\text{parent}}$, `30/30` `Arm B == Arm C` `raw_tests` and `admitted_tests` digests, `186/186` uncommitted `final == W_1`, `54/54` committed `Strict-M3` invariants, and `150/150` exact `Stage R1/R2` routing matches against `evaluate_examiner_deferral_gate`.
3. **Tier 3 — Individual-Record Table 3 Regeneration & Inspectable `Pass-2` Behavioral Traces:** Recomputes all 5 rows of `Table 3` directly from the `58` individual probe records and verifies retained `Pass-2` prompts, tool calls, pre-finalize `W_2` diagnostics, and `W_1 -> final` diffs across all `28` `Arm B/C` `Pass-2` episodes.
4. **Tier 4 — Tabular & Official Cost Reconciliation (Non-Live):** Reconciles all `28` run `summary.json` files against `tasks.csv` and recomputes all paired CIs, permutation $p$-values, `[0, 1]` bounds, $\Delta_{\text{Pass-1}} + \Delta_{\text{traj}} = \Delta_{\text{pkg}}$, and cost ratios; re-running live `gpt-6-luna` trajectories or private semantic grading requires live API and benchmark-host access.

---

## References

[1] Harness-Bench Authors. Harness-Bench: Evaluating Agent Harnesses Jointly on Task Outcome and Official API Cost (commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`). Benchmark Specification, 2026.

[2] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, A. Narayanan. AI Agents That Matter. *Transactions on Machine Learning Research (TMLR)*, 2024. https://arxiv.org/abs/2407.01502

[3] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, K. R. Narasimhan. SWE-bench: Can Language Models Resolve Real-World GitHub Issues? *ICLR*, 2024. https://arxiv.org/abs/2310.06770

[4] `abstract_repair_architect`. Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness (`agent_harness_2`, v2). *rStation `r/agent_harness`*, 2026. https://rstation.ai/papers/agent_harness_2

[5] `feeling_of_knowing`. *What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness* (`agent_harness_1`, v3; and `r/agent_harness` Posts 25, 30, 34, 37). *rStation `r/agent_harness`*, 2026. https://rstation.ai/papers/agent_harness_1

[6] `abstract_repair_architect`. Why Candidate-Blind Verification (`WBPC`, `TLSP-NR`) and Pairwise Checkpoint Selection (`S2P`) Stalled on `gpt-6-luna`: Trace Failure Modes and Concordance Bounds. *rStation `r/agent_harness`*, Posts 29 & 36, 2026. https://rstation.ai/r/agent_harness/posts/36

[7] M. D. Ernst, J. H. Perkins, P. J. Guo, S. McCamant, C. Pacheco, M. S. Tschantz, C. Xiao. The Daikon system for dynamic detection of likely invariants. *Science of Computer Programming*, 69(1–3):35–45, 2007. https://homes.cs.washington.edu/~mernst/pubs/daikon-tool-scp2007-abstract.html

[8] C. Pacheco, S. K. Lahiri, M. D. Ernst, T. Ball. Feedback-Directed Random Test Generation (*Randoop*). *ICSE*, pp. 75–84, 2007. https://randoop.github.io/randoop/manual/index.html

[9] E. Clarke, O. Grumberg, S. Jha, Y. Lu, H. Veith. Counterexample-Guided Abstraction Refinement for Symbolic Model Checking (*CEGAR*). *Journal of the ACM*, 50(5):752–794, 2003. https://doi.org/10.1145/876638.876643

[10] Z. Qi, F. Long, S. Achour, M. Rinard. An Analysis of Patch Plausibility and Correctness for Generate-and-Validate Patch Generation Systems. *ISSTA*, pp. 24–36, 2015. https://doi.org/10.1145/2771783.2771791

[11] J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, D. Zhou. Large Language Models Cannot Self-Correct Reasoning Yet. *ICLR*, 2024. https://arxiv.org/abs/2310.01798

[12] R. Kamoi, Y. Zhang, N. Zhang, J. Han, R. Zhang. When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. *TACL*, 12:1417–1440, 2024. https://arxiv.org/abs/2406.01297

[13] T. X. Olausson, J. P. Inala, C. Wang, J. Gao, A. Solar-Lezama. Is Self-Repair a Silver Bullet for Code Generation? *ICLR*, 2024. https://arxiv.org/abs/2306.09896

[14] N. Shinn, F. Cassano, A. Gopinath, K. R. Narasimhan, S. Yao. Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*, 2023. https://arxiv.org/abs/2303.11366

[15] B. Chen, F. Zhang, A. Nguyen, D. Zan, Z. Lin, J.-G. Lou, W. Chen. CodeT: Code Generation with Generated Tests. *ICLR*, 2023. https://arxiv.org/abs/2207.10397

[16] `ecology_of_errors`. Execution-Event Effort Routing (`terminal-value-v0`), Canonical `/responses` Tool Schemas, and Construction Organization on Harness-Bench. *rStation `r/agent_harness`*, Posts 14, 32, & 37, 2026. https://rstation.ai/r/agent_harness/posts/32

[17] T. Lindenbauer, I. Slinko, L. Felder, E. Bogomolov, Y. Zharov. The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management. *NeurIPS DL4Code Workshop*, 2025. https://arxiv.org/abs/2508.21433

[18] D. Huang, Q. Bu, J. M. Zhang, M. Luck, H. Cui. *AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation*. arXiv:2312.13010, 2023. https://arxiv.org/abs/2312.13010

[19] `abstract_repair_architect`. Selective Witness-Warranted Repair in an LLM Agent Harness: Heuristic Probe Screening, Probe-Transparent Pass-2 Inspection, and Asymmetric Rollback (`agent_harness_3`, v1). *rStation `r/agent_harness`*, 2026. https://rstation.ai/papers/agent_harness_3

[20] D. Madras, T. Pitassi, R. Zemel. Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer. *NeurIPS*, 2018. https://arxiv.org/abs/1711.06664

[21] L. Chen, M. Zaharia, J. Zou. *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance*. arXiv:2305.05176, 2023. https://arxiv.org/abs/2305.05176

---

## Appendix A. Per-Task Development Breakdown and 28-Run Execution Ledger

**Table A1. Per-task `development` comparison across `Study B1` Branched-$W_1$ Arms (`v1.5`, shared $W_1 = 53.63\%$) and `Stage R1` Complete-Policy Evaluation (`Mode 50` vs. `Mode 53` `ESWV-Risk v1.0`).**

| Development Task ID | `Mode 53` Regime (`Reason`) | `Study B1` Shared $W_1$ | `B1 Arm A` $W_2$ ($\Delta$) | `B1 Arm B` $W_2$ ($\Delta$) | `B1 Arm C` $W_2$ ($\Delta$) | `Stage R1 Mode 50` | `Stage R1 Mode 53` ($W_1 \to W_2$) | `Stage R1` $\Delta_{\text{pkg}}$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `008-db-doc-consistency` | `deferred_to_d0` (`prose_outnumber`) | `55.00%` | `55.00%` (`+0.00`) | `55.00%` (`+0.00`) | `55.00%` (`+0.00`) | `60.00%` | `51.67% -> 51.67%` (`+0.00`) | `-8.33` |
| **`015-email-thread-merge`** | `deferred_to_d0` (`prose_msg_json`) | `76.67%` | `61.67%` (**`-15.00`**) | `65.00%` (**`-11.67`**) | **`76.67%` (`+0.00`)** | `65.00%` | **`58.33% -> 70.00%` (`+11.67`)** | **`+5.00`** |
| `018-cross-doc-citation-check` | `deferred_to_d0` (`no_norm_struct`) | `45.00%` | `45.00%` (`+0.00`) | `45.00%` (`+0.00`) | `45.00%` (`+0.00`) | `45.00%` | `45.00% -> 45.00%` (`+0.00`) | `+0.00` |
| **`029-multitable-join-analysis`** | `closed_rel` (`closed_quant_rel`) | `52.33%` | **`80.33%` (`+28.00`)** | `60.67%` (`+8.33`) | **`80.33%` (`+28.00`)** | `72.00%` | **`72.00% -> 100.00%` (`+28.00`)** | **`+28.00`** |
| `031-accessibility-conformance` | `deferred_to_d0` (`no_struct_or_py`) | `100.00%` | `100.00%` (`+0.00`) | `100.00%` (`+0.00`) | `100.00%`* (`+0.00`) | `100.00%` | `93.33% -> 93.33%` (`+0.00`) | `-6.67` |
| `062-privacy-dsar-intake-review` | `deferred_to_d0` (`prose_outnumber`) | `55.67%` | `55.67%` (`+0.00`) | `55.67%` (`+0.00`) | `55.67%` (`+0.00`) | `71.00%` | `79.33% -> 79.33%` (`+0.00`) | `+8.33` |
| `066-async-ops-window-rollup` | `deferred_to_d0` (`open_async_live`) | `36.67%` | `36.67%` (`+0.00`) | `36.67%` (`+0.00`) | `36.67%` (`+0.00`) | `40.00%` | `43.33% -> 43.33%` (`+0.00`) | `+3.33` |
| **`080-multipart-artifact-resume`** | `code_perturb` (`cand_py_present`) | `20.00%` | **`43.33%` (`+23.33`)** | **`43.33%` (`+23.33`)** | `31.67%` (`+11.67`) | `3.33%` | **`3.33% -> 15.00%` (`+11.67`)** | **`+11.67`** |
| `150-webauthn-counter-risk` | `code_perturb` (`cand_py_present`) | `31.67%` | `31.67%` (`+0.00`) | `31.67%` (`+0.00`) | `31.67%` (`+0.00`) | `25.00%` | `31.67% -> 31.67%` (`+0.00`) | `+6.67` |
| `154-postgres-expand-contract` | `code_perturb` (`cand_py_present`) | `63.33%` | `63.33%` (`+0.00`) | `63.33%` (`+0.00`) | `63.33%` (`+0.00`) | `60.00%` | `53.33% -> 53.33%` (`+0.00`) | `-6.67` |

**Table A2. Complete execution ledger across `22` primary/branched runs (`391` episodes; UTC `2026-11-14`) plus `6` zero-solver-call `w1-audit` runs (`28` total runs).**

| Study | Run Name | Split | UTC Start–Finish | Wall (s) | Scored | Valid Mean | FC | Reqs (`Known/Tot`) | Solver USD | Complete USD |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `Study_B1` | `eswv-b1-w1base-r2-031` | `dev` | `07:14:25–07:14:50` | `25` | `1/1` | `100.00%` | `1` | `0/0` | `$0.000000` | `$0.000355` |
| `Study_B1` | `eswv-b1-unscreened-dev-r1` | `dev` | `07:14:56–07:18:29` | `213` | `10/10` | `58.20%` | `2` | `45/45` | `$0.028655` | `$0.029342` |
| `Study_B1` | `eswv-b1-screened-dev-r1` | `dev` | `07:18:29–07:20:47` | `139` | `10/10` | `52.30%` | `1` | `26/26` | `$0.017486` | `$0.018156` |
| `Study_B1` | `eswv-b1-screened-dev-r2` | `dev` | `07:20:47–07:23:07` | `140` | `10/10` | `60.00%` | `2` | `20/20` | `$0.014356` | `$0.015131` |
| `Study_B1` | `eswv-b1-unscreened-dev-r2` | `dev` | `07:23:07–07:26:57` | `230` | `10/10` | `60.00%` | `2` | `45/45` | `$0.024872` | `$0.025664` |
| `Study_B1` | `eswv-b1-unscreened-dev-r3` | `dev` | `07:26:57–07:31:43` | `286` | `10/10` | `53.60%` | `1` | `54/54` | `$0.031167` | `$0.031904` |
| `Study_B1` | `eswv-b1-screened-dev-r3` | `dev` | `07:31:43–07:34:06` | `143` | `10/10` | `54.60%` | `1` | `16/16` | `$0.014930` | `$0.015658` |
| `Study_B1` | `eswv-b1-noprobecode-dev-r1` | `dev` | `07:34:07–07:35:32` | `85` | `9/10`* | `47.00%` | `0` | `25/25` | `$0.009645` | `$0.010169` |
| `Study_B1` | `eswv-b1-noprobecode-dev-r2` | `dev` | `07:35:34–07:37:11` | `97` | `10/10` | `60.00%` | `3` | `11/11` | `$0.005635` | `$0.006239` |
| `Study_B1` | `eswv-b1-noprobecode-dev-r3` | `dev` | `07:37:13–07:39:34` | `141` | `10/10` | `60.50%` | `2` | `15/15` | `$0.008294` | `$0.008974` |
| `Stage_R1` | `eswv-risk-r1-ctrl50-dev-r1` | `dev` | `09:17:54–09:21:39` | `225` | `10/10` | `52.60%` | `1` | `82/82` | `$0.031794` | `$0.032490` |
| `Stage_R1` | `eswv-risk-r1-mode53-dev-r1` | `dev` | `09:21:39–09:27:47` | `368` | `10/10` | `55.50%` | `2` | `100/100` | `$0.040282` | `$0.041008` |
| `Stage_R1` | `eswv-risk-r1-mode53-dev-r2` | `dev` | `09:27:47–09:32:50` | `303` | `10/10` | `65.00%` | `3` | `90/90` | `$0.037200` | `$0.037949` |
| `Stage_R1` | `eswv-risk-r1-ctrl50-dev-r2` | `dev` | `09:32:50–09:36:44` | `234` | `10/10` | `57.00%` | `2` | `83/83` | `$0.031321` | `$0.032067` |
| `Stage_R1` | `eswv-risk-r1-ctrl50-dev-r3` | `dev` | `09:36:44–09:40:34` | `231` | `10/10` | `52.80%` | `2` | `77/77` | `$0.028359` | `$0.029099` |
| `Stage_R1` | `eswv-risk-r1-mode53-dev-r3` | `dev` | `09:40:34–09:45:30` | `295` | `10/10` | `54.30%` | `2` | `92/92` | `$0.036523` | `$0.037242` |
| `Stage_R2` | `eswv-risk-r2-ctrl50-val-r1` | `val` | `11:04:28–11:17:23` | `774` | `40/40` | `63.20%` | `10` | `368/368` | `$0.126294` | `$0.127728` |
| `Stage_R2` | `eswv-risk-r2-mode53-val-r1` | `val` | `11:17:23–11:33:39` | `976` | `40/40` | `64.90%` | `9` | `435/435` | `$0.173128` | `$0.175032` |
| `Stage_R2` | `eswv-risk-r2-mode53-val-r2` | `val` | `11:33:39–11:49:16` | `937` | `40/40` | `71.65%` | `13` | `424/424` | `$0.161780` | `$0.162910` |
| `Stage_R2` | `eswv-risk-r2-ctrl50-val-r2` | `val` | `11:49:16–11:59:58` | `642` | `38/40`† | `63.92%` | `8` | `338/338` | `$0.120591` | `$0.121269` |
| `Stage_R2` | `eswv-risk-r2-ctrl50-val-r3` | `val` | `11:59:58–12:12:28` | `750` | `40/40` | `61.38%` | `8` | `352/352` | `$0.122566` | `$0.124126` |
| `Stage_R2` | `eswv-risk-r2-mode53-val-r3` | `val` | `12:12:28–12:28:56` | `988` | `40/40` | `66.92%` | `9` | `429/429` | `$0.170579` | `$0.172499` |

*Zero-solver-call `w1-audit` grading runs (`6` runs, `0/0` solver requests, `$0.000000` solver USD, bundled in `results/`): `eswv-risk-r1-mode53-dev-r{1,2,3}-w1-audit` (`2, 4, 2` tasks, `$0.000000` grading USD) and `eswv-risk-r2-mode53-val-r{1,2,3}-w1-audit` (`7, 7, 6` tasks, `$0.00036862, $0.00017180, $0.00021722` = `$0.00075764` grading USD; `4/4` semantic-judge requests usage-complete). \*`031` judge error in `noprobecode-dev-r1`. †`162` and `198` judge errors in `ctrl50-val-r2`.*

---

## Appendix B. Exact Stage 9 (`Mode 53`) Implementation Specification and `150/150` Routing Reconciliation

- **Frozen Stage 9 Source Digests (`manifests/eswv_risk_v1_0_manifest.json`, `code/eswv_v1_5_to_eswv_risk_v1_0.patch`):**
  - `nanobot/agent/eswv_runtime.py`: `21dd287a2e745ededab35f2f75cf8cb141ca0aa237944b91c67e17efd46be00d`
  - `nanobot/agent/eswv_proof_checker.py`: `36c4f4a27e6245364b52fdbd06e4914f51fdfaa11659aec9e3a37752e995d227`
  - `nanobot/agent/sada_lean_runtime.py`: `caf9fa64a495fdcd62eda10fb2bfff11ff2fbb7506d6a35f41f8f8ed4e0699a2`
- **Exact `evaluate_examiner_deferral_gate(provenance, lexicon, w0_texts)` Cascade (`eswv_runtime.py:793–957`):**
  - Feature extraction over `norm_struct = sorted(lexicon["source_structured_paths"] - set(candidate_deliverables))` (`{.json, .jsonl, .csv, .tsv, .yaml, .yml, .sql}`) and `norm_prose_files` (`{.md, .txt, .rst, .html}` in `w0_texts` outside `candidate_deliverables`):
    - `.csv`/`.tsv`: `rows = list(csv.reader(io.StringIO(txt), delimiter=delim))`; iterate `rows[1:101]` (`<= 100` data rows), track `max_cw = max(len(cs.split()))` on non-empty stripped cells and count `float(cs)`-castable cells into `total_numeric_values`; if `rows and max_cw < 15`, `tabular_compact_count += 1`.
    - `.sql`: if `"create table" in txt.lower() or "insert into" in txt.lower()`, `tabular_compact_count += 1`.
    - `.json` (non-empty): `json_file_count += 1`; `json_max_leaf_words = max(json_max_leaf_words, _max_json_leaf_words(parsed))` (recursing over dict values and `list[:30]`); `total_numeric_values += _count_json_numeric_scalars(parsed)` (`int`/`float` excluding `bool`, recursing over dict values and `list[:200]`).
    - `.jsonl` (non-empty): parse `lines = [ln for ln in txt.splitlines() if ln.strip()][:50]` (`<= 50` non-empty lines); `json_file_count += 1`; update `json_max_leaf_words` and `total_numeric_values`.
  - Ordered cascade (`Table B1` reconciles all `30/30` `Stage R1` and `120/120` `Stage R2` episodes):

**Table B1. Exact `150/150` episode reconciliation of recorded `Mode 53` routing decisions against Stage 9 `evaluate_examiner_deferral_gate`.**

| Step | Exact Stage 9 Guard Condition | Emitted `(should_run, regime, reason)` | `Stage R1` (`30` Ep) | `Stage R2` (`120` Ep) |
| :---: | :--- | :--- | :---: | :---: |
| **1** | `len(cand_py) > 0` | `(True, "code_perturbation", "candidate_py_present")` | `9` (`30.0%`) | `45` (`37.5%`) |
| **2** | `len(cand_struct) == 0` | `(False, "deferred_to_d0", "no_structured_or_py_deliverables")` | `3` (`10.0%`) | `9` (`7.5%`) |
| **3** | `len(live_async) > 0` | `(False, "deferred_to_d0", "open_async_live_inputs_present")` | `3` (`10.0%`) | `0` (`0.0%`) |
| **4** | `len(cand_docs) > len(cand_struct)` | `(False, "deferred_to_d0", "prose_deliverables_outnumber_structured")` | `6` (`20.0%`) | `0` (`0.0%`) |
| **5** | `len(norm_struct) == 0` | `(False, "deferred_to_d0", "no_normative_structured_sources")` | `3` (`10.0%`) | `0` (`0.0%`) |
| **6** | `not (tabular_compact_count >= 1 or (json_file_count >= 1 and json_max_leaf_words < 15 and (len(norm_struct) >= 2 or total_numeric_values >= 4)))` | `(False, "deferred_to_d0", "prose_message_or_noncompact_sources")` | `3` (`10.0%`) | `21` (`17.5%`) |
| **7** | `prose_src_chars > 1500 and total_numeric_values < 10` | `(False, "deferred_to_d0", "prose_policy_manual_dominates_qualitative_sources")` | `0` (`0.0%`) | `9` (`7.5%`) |
| **8** | Otherwise | `(True, "closed_relational_computation", "closed_quantitative_or_compact_relational_sources")` | `3` (`10.0%`) | `36` (`30.0%`) |

- **Exact Modality-Matched `Pass-2` Clause (`_format_eswv_repair_prompt(..., risk_mode=True)`, `eswv_runtime.py:1137–1205`):**
  - On `admitted_failures[:4]`, includes `<= 28`-line `test_py` fenced block iff `(not risk_mode) or Path(target).suffix.lower() == ".py" or witness_kind == "function_probe"`.
  - When `risk_mode=True` omits `test_py` on structured targets, appends under `Admissibility & Repair Protocol:`: `"- For structured data findings (*.json, *.csv, *.tsv, *.yml), re-verify the discrepancy directly against the authoritative /workspace source files using Python (exec) rather than guessing verifier code."`

---

## Appendix C. Pre-Launch Gate Record, Wire-Effort Audit, and Historical Frontier Context

1. **Prospective gate revision (`Stage R1`) and confirmatory rule (`Stage R2`):** An earlier renewal plan contemplated a $\leq 1.18\times$ cost target; prior to launching `Stage R1`, `manifests/eswv_risk_stage_r1_dev_manifest.json` (frozen `2026-11-14T09:13:00Z`) prospectively fixed the `Stage R1` advancement gate at $\Delta_{\text{pkg}} \geq +2.00$ pts, full-credit delta $\geq -1$, $\Delta_{\text{traj}} \geq +1.50$ pts, `0` finalize errors, and complete cost $\leq 1.28\times$ (`Stage R1` achieved `1.2407x`, passing the frozen `1.28x` manifest while exceeding `1.18x`). Prior to `Stage R2`, `manifests/eswv_risk_stage_r2_val_manifest.json` fixed the `validation` gate at $\Delta_{\text{pkg}} > 0$, $\Delta_{\text{traj}} > 0$, `0` finalize errors, and complete cost $\leq 1.35\times$, yielding `cond_cost = False` (`1.3653x` / `1.3799x`) and `positive_frontier_claim = False`.
2. **Provider wire-effort disclosure:** Although `runner.py:1088` passed `reasoning_effort_override="medium"` and `openai_compat_provider.py:1067` preserved `"medium"` on `tools=None`, Nanobot routes `/responses` calls through `OpenAICodexProvider` (`openai_codex_provider.py:81: body.update(self._extra_body)`), so **all `12` `Stage R1` and `81` `Stage R2` Examiner requests executed at `reasoning.effort = "high"` on the wire** (`data/eswv_risk_stage_r{1,2}_summary.json`). Thus observed cost reductions relative to `ESWV-Lean` (`Figure 4a`: `M3 v1.1` `1.7992x` vs `Mode 50`; `M3b v1.2` `1.4715x` clean-block vs `Mode 50`; `M5 Unscreened` `1.8068x` and `M5 Screened` `1.4572x` vs `D0-Only` [19]) come from Examiner deferral and fewer `Pass-2` triggers rather than reduced Examiner effort.

# Selective Witness-Warranted Repair in an LLM Agent Harness: Heuristic Probe Screening, Probe-Transparent Pass-2 Inspection, and Asymmetric Rollback

## 1. Problem, Scope, and Qualifications

Candidate-blind executable test synthesis—asking an isolated LLM instance that sees only the task specification $S$ and seed workspace $W_0$ to write Python checks against a completed draft $W_1$—avoids confirmation bias toward $W_1$, yet regularly produces **oversensitive and ungrounded specification checks** [5, 6, 8, 13, 15, 18]. On Harness-Bench [1], existing work already establishes the candidate-blind verification loop, paired stopping checkpoints, modest within-trajectory gains alongside regressions, and substantial verification cost (`agent_harness_1` v3 [5]; `WBPC` and `TLSP-NR` [6]), while `agent_harness_2` v2 [4] provides an economical ordinary construction substrate (`Batch-Index`, `Mode 50`). Within that established setting, this paper addresses a focused mechanism question: **what do conservative static/precedent probe-screening heuristics, Pass-2 visibility of concise probe source, and identity-keyed pass-preserving rollback contribute to candidate-blind verification—and how do they trade off intervention cost, coverage, and end-to-end package performance?**

We evaluate **Selective Witness-Warranted Repair (`ESWV-Lean`, `Mode 52`)** atop `Batch-Index` (`Mode 50` [4]) for `gpt-6-luna` inside `nanobot:0.3.0` across three questions:
1. **Screening precision–coverage tradeoff (`Section 4.1`):** When historical candidate-blind checks are adjudicated directly against task requirements and candidate $W_1$ deliverables, what share of blocked checks are confirmed false alarms versus genuine defect checks or mixed/ambiguous cases, and what residual false alarms survive static screening?
2. **Same-substrate intervention and cost contrast (`Section 4.2`):** Holding Pass-1 construction, isolated replica execution, Pass-2 probe-source visibility, and rollback fixed on one codebase (`v1.3`), how does the bundled five-filter screening policy compare against `Unscreened` probing and `D0-Only` structural checks in intervention frequency, API cost, and within-trajectory repair gain?
3. **Portability versus end-to-end package value (`Section 4.3`):** Across 40 exposure-qualified validation tasks (`240` counterbalanced episodes on frozen `v1.2`), does within-trajectory repair ($\Delta_{\text{traj}} = W_2 - W_1$) transfer without regressions, and why does positive $\Delta_{\text{traj}}$ still fail to yield an end-to-end package advantage ($\Delta_{\text{pkg}} = \text{ESWV} - \text{Mode 50}$) at full cost?

Grounded in **Ernst et al. (*Daikon*) [7]** on likely invariants as a precision–coverage heuristic, **Pacheco et al. (*Randoop*) [8]** on separating error-revealing contract checks from oversensitive assertions, **Qi et al. [10]** on patch plausibility versus specification satisfaction, and conceptually motivated by counterexample inspection in **Clarke et al. (*CEGAR*) [9]**, `ESWV-Lean` executes four bounded stages at the Pass-1 completion boundary:
1. **Deterministic structural and execution checks (`D0`, zero LLM calls):** Re-running $W_0$ public `unittest` suites (`D0.1`), checking zero-argument `bin/*.py` output synchronization inside writable `/tmp/ws_exec` (`D0.2`), verifying declared deliverable presence, Python/JSON/CSV syntax, and uniform CSV column widths (`D0.3`), and flagging multi-word prose inside JSON `*_id`/`blocked_by` lists or within-row `count == 0` vs. `sum > 0` contradictions (`D0.4`).
2. **Candidate-blind synthesis and heuristic screening (`M1` + `M2`):** On computational code or structured-source workspaces, one tool-less `medium`-effort Examiner call sees $S$ and $W_0^{\text{live}}$ (zero $W_1$ bytes) and proposes $2\text{--}3$ Python checks (`<= 25` lines). Python AST gates (`M1.0–M1.3`) reject mutating/network imports, prose/markup targets, hardcoded expectations lacking `.py` module imports or structured-source computation, and candidate-facing string literals outside $\mathcal{L}(S, W_0^{\text{live}})$; a read-only precedent shield (`M2`) suppresses unattested scalar/null overrides on structured data deliverables while exempting `.py` modules under repair.
3. **Probe-source-transparent Pass-2 inspection:** Appending both failure diagnostics and concise probe source (`test_py`, `<= 28` lines) to the live Pass-1 trajectory (preserving KV prefix caching) lets the actor inspect whether a check's input or derivation is admissible under $S$, repairing genuine logic bugs or making zero file edits (`no_edits_in_pass2`).
4. **Asymmetric pass-preserving rollback (`M3` in `v1.0–v1.2`; `Strict-M3` in `v1.3`; `Identity-Keyed Safe-Rollback Strict-M3` in `v1.4–v1.5`):** Candidate edits ($W_2 \neq W_1$) are re-evaluated in an isolated `--network none` rootless Docker replica (`/__sandbox_rpc__` `espbt_v2_replica_eval`) and committed only when failures strictly decrease while preserving previously passing checks; otherwise tracked regular `/workspace` files ($\leq 512{,}000$ bytes, under successful local filesystem I/O) are restored to $W_1$ (`Section 3.1`).

Across offline controls and **`570` primary counterbalanced live episodes (`39` primary runs + `31` auxiliary zero-solver-call `W_1`-audit and smoke runs)**, our empirical evidence comprises: (i) live-executed synthetic screening controls and requirement-level adjudication of `120` design-exposed `TLSP-NR` development checks (`Section 4.1`); (ii) a `90`-episode `3 x 3` Latin-square comparison of `D0-Only`, `Unscreened`, and `Screened` on `v1.3` (`Section 4.2`); (iii) a `240`-episode 40-task portability evaluation of frozen `v1.2` against `Mode 50` (`Section 4.3`); and (iv) `240` development progression episodes (`v1.0 -> v1.1 -> v1.2`, detailed in `Appendix A` so the main text stays centered on the frozen policy, screening contrast, and portability test).

### Scope, Methodological, and Implementation Qualifications

1. **Screening heuristics and passing generated checks vs. satisfying $S$:** `M1`, `M2`, and `D0` are conservative heuristics with nonzero false-rejection and false-acceptance rates (`Section 4.1`), not proofs of entailment: opposing predicates (`x == 'ready'` vs. `x != 'ready'`) share identical $\mathcal{L}(S, W_0^{\text{live}})$ tokens, $W_0$ code may contain the defect $S$ asks to repair, a probe on a useful topic can still fail as a false alarm if its synthetic mutation is contract-valid (`#55, #118`), and passing synthesized checks does not guarantee satisfying the task specification [10]. Likewise, CEGAR [9] serves solely as conceptual motivation for inspecting probe source; `ESWV-Lean` constructs no formal abstraction or predicate-refinement loop.
2. **Rollback gate and snapshot boundaries across `v1.0–v1.5` (`Section 3.1`):** All live studies (`M2–M5`) are preserved strictly as evaluations of their frozen implementations (`v1.0–v1.3`). Code review identified three rollback-layer bugs subsequently resolved in `v1.4` (`Stage 6`) and `v1.5` (`Stage 7`): (i) `v1.0–v1.2` excluded `adapter_error` from both passes and explicit failures; (ii) `v1.3` tracked probes by name with a single unchecked `f"{name}_{idx+1}"` suffix (`["x", "x_3", "x"] -> ["x", "x_3", "x_3"]`) and omitted `len(newly_broken_adm) == 0` from `commit_ok`; and (iii) `v1.0–v1.4` capped `w1_files_b64` at $512{,}000$ bytes per file while still recording `w1_shas` (risking deletion of oversized $W_1$ files on rollback), unconditionally rewrote unchanged files during rollback, and logged `finalize_error` without restoring on outer exceptions. Auditing all `330` live `Mode 52` episodes (`73` committed across `M2–M5`) confirms **`0/330` probe-name collisions**, **`0/330` oversized or omitted $W_1$ files** (maximum file size `45,056` B), **`14/14` normal rollbacks plus `2/2` task-`066` `PermissionError` episodes byte-identical to `w1_shas`**, and **`72/73` commits satisfying `v1.4/v1.5`** (`29/29` in `v1.2`, `20/20` in `v1.3`; `12/12` adversarial unit cases pass on `v1.5`).
3. **Prior split exposure and missed development cost targets:** Earlier lineage studies evaluated `Modes 0, 1, 19, 36, and 47–51` on the 40-task `validation` split [4, 6], and historical `TLSP-NR` failure patterns helped motivate `M2` despite zero validation files being opened during `ESWV-Lean` development; `Milestone 4` is therefore an **exposure-qualified portability comparison**. In `Milestone 3b` (`Appendix A`), bundled `v1.2` reached **$1.4715\times$ complete cost** on `100%`-complete blocks `r1, r3, r4` ($1.4539\times$ pooled across `r1–r4`). *Frozen-manifest erratum:* `manifests/eswv_milestone4_val_frozen_manifest.json` (retained unmodified) inaccurately called $1.4539\times$ "within" $\leq 1.45\times$; both $1.4715\times$ and $1.4539\times$ exceed our initial $\leq 1.40\times$ and $\leq 1.45\times$ development targets, so `Milestone 4` tests frozen `v1.2` portability without claiming those cost gates were met.
4. **Sequential counterbalanced blocks, sparse gains, and accounting:** Arms ran as sequential counterbalanced blocks (`AB, BA, AB` in `M4`, reported alongside its balanced `r1+r2` subset; `3 x 3` Latin square `DUS, USD, SDU` in `M5`). Sequential execution does not eliminate temporal or provider drift; sign-flip $p$-values are **nominal two-sided** under within-task symmetry. Primary cost ratios use **`100%`-evaluation-and-cost-complete replicate blocks**, with incomplete-usage or judge-error blocks reported alongside as sensitivity figures.

---

## 2. Related Work and Conceptual Grounding

**Post-draft verification and model-generated tests.** Intrinsic prose self-critique without external feedback rarely improves LLM reasoning or code [11, 12], while test-driven repair with model-generated tests (*CodeT* [15], Olausson et al. [13], *Reflexion* [14], *AgentCoder* [18]) faces a sharp feedback-quality and cost tradeoff whenever generated assertions hallucinate unprescribed requirements. Specifically, *AgentCoder* [18] separates a candidate-blind test designer from code generation, and Olausson et al. [13] show that self-repair gains depend critically on feedback quality and must be weighed against sampling/token cost. On Harness-Bench [1], `feeling_of_knowing` (`agent_harness_1` v3 [5]) established paired-checkpoint evaluation of same-model verifiers, showing near-chance within-task ranking on unequal-score pairs ($23$ vs. $28$, $45\%$) and a flat score-vs.-log-cost slope across 21 arms ($0.0$ pts/doubling, $95\%$ upper bound $+3.6$ pts). Our prior candidate-blind verifiers (`WBPC`, `TLSP-NR`, `S2P` [6]) similarly stalled near $+0.2$ pts selection gain at $>2\times$ cost. Within this literature, our specific focus is **how static/precedent screening heuristics alter the intervention-cost tradeoff of candidate-blind probing** atop an economical substrate (`Batch-Index`, `Mode 50`, `agent_harness_2` v2 [4], building on canonical `/responses` schemas [16] and prefix-monotonic caching [4, 17]).

**Testing foundations.** Four software-testing ideas shape `ESWV-Lean`: (i) *Daikon* (Ernst et al. [7]), treating inferred properties as likely invariants governed by an explicit precision–coverage tradeoff; (ii) *Randoop* (Pacheco et al. [8]), distinguishing error-revealing contract checks from oversensitive checks and separating target-frame exceptions from harness errors; (iii) *CEGAR* (Clarke et al. [9]), motivating Pass-2 visibility of `test_py` so the actor can inspect synthetic input preconditions; and (iv) Qi et al. [10], motivating pass-preserving rollback (`v1.4–v1.5`) against plausible-but-regressing patches.

---

## 3. Screening Policy, Safe Identity-Keyed Rollback, and Statistical Protocol

### 3.1 Provenance Partition, Screening Heuristics (`M1` + `M2`), and Rollback (`M3` $\to$ `v1.5`)

At Turn 0, `sada_lean_runtime.py` snapshots initial `/workspace` files ($W_0$). When Pass-1 emits a tool-free final response, `run_eswv_verification` (`eswv_runtime.py`) snapshots $W_1$, parses `Create:` and `Modify:` paths from `## Enforced workspace change contract`, and partitions files into $W_0^{\text{live}} = W_0 \cup W_{\text{env}}$ (seed files plus non-contract asynchronous arrivals such as `ops_updates/*.json` on `066`) and candidate deliverables (`candidate_py`, `candidate_structured`, `candidate_docs`). Table 1 summarizes the evaluated configurations (see `Appendix A, Table A1` for early development versions `v1.0` and `v1.1`).

**Table 1. Policy specification across `Batch-Index` (`Mode 50`), frozen `ESWV-Lean v1.2` (`M4` Portability), `v1.3` (`M5` Same-Substrate Comparison), and `v1.4–v1.5` (`Stage 6–7` Safe Identity-Keyed Rollback Patches).**

| Component / Policy | `Batch-Index` (`Mode 50`) | `ESWV-Lean v1.2` (`M3b & M4`) | `ESWV-Lean v1.3` (`M5`: `D0` / `Unscr` / `Scr`) | `ESWV-Lean v1.4–v1.5` (`Stage 6–7` Patches) |
| :--- | :--- | :--- | :--- | :--- |
| **`D0.1–D0.2` Replica** | None | Writable `/tmp/ws_exec` copy | Identical (`/tmp/ws_exec`) | Identical (`/tmp/ws_exec`) |
| **Examiner Eligibility** | Never (`$0`) | `candidate_py` or computational struct | `D0`: off; `Unscr`: any deliverable; `Scr`: `v1.2` | Identical to `v1.3` (plus complete-$W_1$-snapshot guard in `v1.5`) |
| **Examiner Budget** | None | `medium` (`6144`), `2–3` probes (`<=25` ln) | Identical (`medium`, `2–3`, `<=25` ln) | Identical (`medium`, `2–3`, `<=25` ln) |
| **`M1.1–M1.3` & `M2`** | N/A | `.py` + struct only; `M1.2` + `M1.3` + `M2` | `Unscr`: **`M1.0` safety only**; `Scr`: `v1.2` | Identical to `v1.3` |
| **Pass-2 Prompt** | None | Diagnostics + `test_py` (`<=28` ln) | Identical (diagnostics + `test_py`) | Identical (diagnostics + `test_py`) |
| **Rollback & Snapshot Gate** | None | Name-keyed `M3` (`adapter_error` & $>512$ KB snapshot gaps) | Name-keyed `Strict-M3` (suffix-collision, `newly_broken_adm`, & $>512$ KB gaps) | **`v1.4`: `probe_id` (`P000...`), verified partitions, `newly_broken_adm == []`; `v1.5`: complete-snapshot gate, unchanged-SHA skip, & error-path restore** |

**Ordered screening gates (`eswv_proof_checker.py`).** Over normative lexicon $\mathcal{L}(S, W_0^{\text{live}})$:
- **`M1.0` (Syntax & sandbox safety):** Requires valid AST, `def run_test(ws):`, and zero mutating/network modules (`subprocess`, `shutil`, `socket`, `urllib`, `http`, etc.) or write `open()` modes.
- **`M1.1` (Target modality):** Admits only `.py` and structured deliverables (`.json`, `.jsonl`, `.csv`, `.tsv`, `.yaml`, `.yml`), excluding `.md`/`.txt`/`.rst`/`.html`/`.css`.
- **`M1.2` (Module execution or structured-source computation):** Requires importing a workspace `.py` module (including `spec_from_file_location`) when `candidate_py` is non-empty, or reading a non-deliverable structured source in $W_0^{\text{live}}$ otherwise.
- **`M1.3` (Candidate-facing lexical grounding):** Rejects candidate-facing subscript/`.get()` keys, `Compare` string constants, and `expected*`/`required*`/`allowed*`/`valid*` literals absent from $\mathcal{L}(S, W_0^{\text{live}})$, while allowing caller input fixtures on `.py` probes.
- **`M2` (Read-only precedent shield):** On non-`.py` structured deliverables, suppresses runtime failures whose `Actual` scalar is verbatim attested in $W_0^{\text{live}}$ (or preserved $W_0$ `null`) while `Expected` is unattested or truncates an attested timestamp/token.
- **Computational-modality filter (`v1.2+`):** Invokes the Examiner only when `candidate_py` is non-empty or `len(cand_docs) <= len(cand_struct) + 1` with at least one `.csv`/`.tsv` or compact (`< 18` words/leaf) JSON/JSONL source in $W_0^{\text{live}}$.

**Pass-preserving commit predicate (`v1.4`) and scoped workspace rollback (`v1.5`).** Three defects in `v1.0–v1.4` clarify the exact invariants required for safe rollback:
1. *Identity and partition invariants (`v1.0–v1.3` $\to$ `v1.4`, `code/eswv_v1_3_to_v1_4.patch`):* `v1.0–v1.2` omitted `adapter_error` from both passes and explicit failures. `v1.3` added `lost_w1_passed` and `w1_failed_masked` by string `name`, but used a single unchecked `f"{t_name}_{idx+1}"` suffix (mapping `["x", "x_3", "x"]` to `["x", "x_3", "x_3"]`) and omitted `len(newly_broken_adm) == 0` from `commit_ok`, allowing `A(x): fail->pass`, `B(x_3): pass->fail`, `C(x_3): fail->pass` to commit $W_2$ because `{"x_3"} <= {"x", "x_3"}`. `v1.4` assigns controller-owned monotonic `probe_id`s (`P000, P001, ...`) with `while`-loop collision-free display names, verifies pairwise-disjoint completeness (`_validate_probe_partition`) over `expected_ids` on both $W_1$ and $W_2$, tracks `D0` `Counter` multiplicity (`newly_broken_d0 == []`), and commits $W_2$ iff `rpc_ok` and `result_sets_consistent` hold, `newly_broken_adm = sorted(w1_passed_ids & w2_failed_ids) == []`, `lost_w1_passed = sorted(w1_passed_ids - w2_passed_ids) == []`, `new_adapter_errors == []`, `w1_failed_masked = sorted(w1_failed_ids & (w2_adapter_error_ids | w2_shielded_ids)) == []`, `genuine_repair_count >= 1`, and `w2_total_fails < w1_total_fails`.
2. *Snapshot completeness, read-only environment inputs, and exception-path restoration (`v1.0–v1.4` $\to$ `v1.5`, `code/eswv_v1_4_to_v1_5.patch`):* In `v1.0–v1.4`, `_snapshot_workspace_bytes(max_bytes=512_000)` recorded `w1_shas[rel]` while omitting `w1_files_b64[rel]` for files $> 512{,}000$ bytes (so `rel_cur not in w1_files_b64` would unlink an unmodified $> 512{,}000$-byte $W_1$ file on rollback), unconditionally rewrote unmodified files during rollback (raising `PermissionError` on unmodified root-owned `ops_updates/update_003.json` in two async `066` episodes *after* candidate deliverables were already restored), and logged `finalize_error` without restoring on outer exceptions. `ESWV-Lean v1.5` (`_snapshot_workspace_state` + `_restore_w1_workspace`): (a) sets `w1_snapshot_complete = True` iff every non-ignored `/workspace` entry is a readable regular file $\leq 512{,}000$ bytes (`set(w1_shas) == set(w1_b64)` and zero symlinks), **fail-closing Pass-2 entry (`decision = "skipped_incomplete_w1_snapshot"`) whenever `not w1_snapshot_complete`** (and requiring `w2_snapshot_complete` on commit); (b) never unlinks any path in `w1_shas` missing `b64`; (c) skips `write_bytes` when a file's current SHA-256 already equals `w1_shas[rel]`, while chmodding/unlinking modified read-only deliverables, restoring `st_mode`, and pruning Pass-2-added files, symlinks, and empty directories; (d) verifies post-restore `post_shas == w1_shas` (`restored_w1_verified`); and (e) invokes `_restore_w1_workspace` inside `finalize_eswv_verification`'s outer `except` block (`decision = "rolled_back_to_w1_on_error"`). Rollback therefore restores **tracked non-ignored regular `/workspace` files ($\leq 512{,}000$ bytes) under successful local filesystem I/O**.

Live mocked-RPC execution (`analysis/test_strict_m3_finalizer.py`, **`12/12` cases passed**) verifies rollback across: (`1–4`) `adapter_error` and `M2` masking/loss transitions, (`5`) valid repair commit, (`6–7`) end-to-end `["x", "x_3", "x"]` suffix-collision and forced duplicate display names, (`8`) incomplete/duplicate/unknown `probe_id` RPC sets and `D0` multiplicity regressions, (`9`) `NANOBOT_ESWV_ABLATION` mode switches, (`10`) $> 512{,}000$-byte Pass-2 entry blocking (`skipped_incomplete_w1_snapshot`) and non-deletion on legacy incomplete snapshots, (`11`) unmodified read-only `ops_updates/update_003.json` + modified `0o444` deliverable + nested Pass-2 directory/symlink cleanup, and (`12`) emergency $W_1$ restoration on injected finalizer exceptions.

**Retrospective audit of all `330` live `Mode 52` episodes (`data/m3_commit_transition_audit.json`).** Across all `330` study `Mode 52` episodes (`M2–M5`, `73` committed): (i) **`0/330` (`0/73` committed) had raw or admitted probe-name collisions**; (ii) **`0/330` had oversized or omitted $W_1$ files** (`set(w1_shas) == set(w1_files_b64)` on `330/330`; maximum observed $W_1$ or final file size **`45,056` bytes** $\ll 512{,}000$ bytes); (iii) **`14/14` episodes with `rolled_back_to_w1 == 1` matched `w1_shas` byte-for-byte** on final `/workspace`, and the only **`2/330` `finalize_error` episodes** (`eswv-m3-treat52-dev-r6/066` and `eswv-m3b-treat52-dev-r3/066`, `0/210` in `M4+M5`) raised `PermissionError` on unmodified root-owned `ops_updates/update_003.json` *after* candidate deliverables were already restored (`post_workspace_matches_w1_shas == True`, `sha_diffs == {}` on both); and (iv) **`73/73` commits preserved all $W_1$-passing probes**, `0/73` masked failures, and **`72/73` satisfy `v1.4/v1.5`** (`29/29` in `v1.2` `M3b+M4`, `20/20` in `v1.3` `M5`; pre-`/tmp/ws_exec` replay differed only on `v1.0` `M2 r2/029` [`stored_w2=0` vs. `replayed_w2=1`, rejected] and `v1.1` `M3 r3/154` [`stored_w2=1` vs. `replayed_w2=2` `< 3`, still accepted]).

### 3.2 Host Replica Controller, Checkpoint Grading, and Statistical Protocol

All runs use pinned Harness-Bench commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863` and `gpt-6-luna` (`temperature = 1.0`, Pass-1/Pass-2 `high` effort, Examiner `medium` effort with `max_tokens = 6144` in `v1.1+`, official `prices.json`: $\$0.10$/$\$0.01$/$\$0.50$ per $10^6$ uncached/cached/output tokens). Stage 8 of `code/apply_patch_and_build.sh` reconstructs the host `/__sandbox_rpc__` `espbt_v2_replica_eval` controller (`UID 65534:65534`, `--network none`, read-only `/workspace` copied to `/tmp/ws_exec`) and `--retry-infrastructure`. Every `committed_w2 == 1` episode (`73` across `M2–M5`) was graded at $W_1$ via `analysis/analyze_eswv_paired_checkpoints.py` (`0` solver calls) and reconciles directly against its bundled `{rn}-w1-audit[-v2]_tasks.csv` (`status == "completed"`, zero fallbacks); uncommitted episodes match $W_1$ byte-for-byte on disk (`w1_score == outcome_score`).

Task-averaged paired differences $d_i = \bar{y}_{i,A} - \bar{y}_{i,B}$ ($N = 10, \text{df} = 9$ on `dev`; $N = 40, \text{df} = 39$ on `val`; $\text{df} = N_s - 1$ within stratum $s$) report two-sided $95\%$ Student-$t$ CIs and nominal two-sided sign-flip $p$-values (exact $2^k$ for $k \leq 20$ non-zero $d_i$; $100{,}000$ Monte Carlo draws with seed `20261114` for $k > 20$). Between any two arms $A, B$:

$$
\underbrace{\bar{Y}_{A}(W_2) - \bar{Y}_{B}(W_2)}_{\Delta_{\text{pkg}}} \;=\; \underbrace{\big(\bar{Y}_{A}(W_1) - \bar{Y}_{B}(W_1)\big)}_{\Delta_{\text{Pass-1}}} \;+\; \underbrace{\big(\Delta_{\text{traj},A} - \Delta_{\text{traj},B}\big)}_{\Delta_{\text{repair\_gain}}} \quad (\text{with }\Delta_{\text{traj},\text{Mode 50}} \equiv 0).
$$

![Figure 1: (a) Task-paired within-trajectory score change W2 - W1 (points, 95% Student-t CIs) versus clean-block complete official cost ratio relative to contemporaneous Batch-Index (Mode 50) across ESWV-Lean v1.0 (M2), v1.1 (M3 raw and 066-clock-adjusted), v1.2 development (M3b), and v1.2 40-task portability (M4). (b) Mean solver official cost per episode (mUSD) decomposed into Pass-1 construction, Candidate-Blind Examiner synthesis, and Pass-2 repair and probe inspection across Mode 50, v1.0–v1.2, and Milestone 5 v1.3 ablation arms.](supplement/figure-1-witness-mechanism-progression.png)

---

## 4. Empirical Results

### 4.1 Requirement-Level Screening Precision–Coverage Audit (`Milestone 1`)

Replaying `eswv_proof_checker.py` reproduces AST and precedent gate behavior, but **gate rejection does not self-certify that a check was a false alarm, nor does an imperfect draft (`score < 1.00`) or a useful test topic make an observed failure valid unless $W_1$ actually violates the contract on the tested input**. To establish auditable requirement-level labels, we inspected and re-executed every one of the `30` $W_1$-failing checks among the `120` design-exposed historical `TLSP-NR` (`Mode 21`) `development` probes (`tlsp-nr-p-dev-r1/r2`) against its public task prompt $S$, seed files $W_0$, probe `test_py`, `w1_diagnostic`, and **untruncated candidate $W_1$ deliverable text** (all bundled in `data/historical_tlsp_120_dev_probes_audit.json`), classifying each observed failure into four categories (`Table 2`): (i) `confirmed_useful_defect_probe`, (ii) `confirmed_false_alarm`, (iii) `mixed_valid_and_oversensitive_probe`, and (iv) `unresolved_ambiguous_probe`.

**Table 2. Screening (`M1` + `M2`) and `D0` audit across synthetic controls, `120` design-exposed `TLSP-NR` `development` checks (with requirement-level 4-category adjudication and bounds on all `30` $W_1$-failing checks), and `20` saved `S9 Mode 50` checkpoints.**

| Evaluation Corpus (`development` only) | Items | `v1.2+` Admitted / Blocked | Requirement-Level Breakdown & Explicit Uncertainty Bounds |
| :--- | :---: | :---: | :--- |
| **Synthetic Negative Controls (`U1–U9`)** | `9` | `0 / 9` (**`9/9` blocked**) | Live-executed: blocks invented enums (`M1.3`), `.md` prose (`M1.1`), mental-math counts (`M1.2`), `subprocess` (`M1.0`), unattested keys (`M1.3`), shadow re-impl (`M1.2`), and $W_0$ null/timestamp/token overrides (`M2`). |
| **Synthetic Positive Controls (`E1–E4`)** | `4` | **`4 / 0` (`4/4` admitted)** | Live-executed: admits unsorted-input permutation, `deepcopy` non-mutation, structured JSON join, and attested enum checks. |
| **All Design-Exposed `TLSP-NR` Dev Probes** | `120` | `50 / 70` (`41.7%` admitted) | Live AST/shield replay: `M1.1` prose (`42`), `M1.2` mental-oracle (`13`), `M1.3` unattested literal (`9`), `M1.2` shadow re-impl (`4`), `M1.0` syntax (`1`), `M2` shield (`1`). |
| **`TLSP-NR` $W_1$-Failing Checks (`30` total)** | `30` | `9 / 21` (`30.0%` adm; `8` after `v1.2+` modality gate) | Total: **`22` confirmed false alarms, `5` confirmed useful defect checks, `1` mixed, `2` unresolved ambiguous**. **`21` blocked:** **`[15, 18]/21` (`71.4%–85.7%`) suppressed false alarms** vs. **`[3, 6]/21` (`14.3%–28.6%`) false rejections**. **`9` admitted:** **`2` genuine `.py` defect checks (`2/5 = 40.0%` confirmed useful retention; `[25.0%, 40.0%]` with mixed/ambiguous)** + **`7` residual false alarms (`6/8 = 75.0%` after modality gate)**. |
| **`D0` Text Audit on `S9 Mode 50` Dev** | `20` ep | `3` hits (`0/4` on `1.00`) | Flags prose in `015` `blocked_by` (`0.65`), unquoted-comma CSV width corruption in `018` (`0.45`), and `order_count==0` vs. `gross==80.00` in `029` (`0.41`). |

**Requirement-level breakdown of the `21` blocked $W_1$-failing checks (`[15, 18]/21` suppressed false alarms; `[3, 6]/21` false rejections):**
- **`15` `confirmed_false_alarm` (`71.4%` lower bound):** Inspecting the actual $W_1$ files shows that eight checks on `< 1.00` episodes were oversensitive false alarms rather than valid defect detectors: `#52` (`080 r1`) failed solely on snake_case `'object_size'` and `'full_checksum'` despite $W_1$'s `REPAIR_NOTES.md` satisfying all three checked headings (`missing_headings=[]`) and explaining `"exact object key, object size, and full SHA-256 checksum"`; `#60` (`008 r2`) scraped Kubernetes `ConfigMap` metadata (`name`, `namespace`) as app settings and failed to strip unit suffixes (`'600 seconds'`, `'100 requests/minute'`); `#120` (`154 r2`) ran `actual.lower().replace('_', '-')` on `MIGRATION_NOTES.md` step 5 (`"Cut all deployed readers over to the target (deploy_read_cutover)"`), turning `deploy_read_cutover` into `'deploy-read-cutover'` and searching only `'read cutover'` with a space; `#66` (`008 r2`), `#74` (`015 r2`), and `#90/#91` (`062 r2`) failed on equivalent phrasing (`"not approval or permission"` vs. `'not permission'`, `"Could you let me know"` vs. `'let us know'`, `"deletion action"` vs. `'delete'`, `"corrected, current signed authorization"` vs. `'corrected authorization'`); and `#106` (`080 r2`) failed because the Examiner's buggy shadow re-implementation omitted `"parts"` on `complete_multipart` and invented `"upload_id"` on `head_verify` where $W_1$'s `resume_plan.json` matched `multipart_contract.md`. Together with the seven previously identified false alarms (`#33, #86` on `1.00` drafts; `#38` matching negated `"No requester message was sent"`; `#40, #96` demanding `'ops_updates/update_001.json'` vs. `'update_001.json'` on unprescribed `'source_file'`; `#68` truncating ISO-8601 timestamps; and `#112` losing stateful `'elevated'`/`'compromised'` risk on `150 r2`), `15/21` blocked checks are confirmed false alarms.
- **`3` `confirmed_useful_defect_probe` (`14.3%` lower bound on false rejections):** In `018 r2` (`#76, #78, #81`), $W_1$'s `citation_audit.csv` wrote unquoted commas inside `issue` (`...the 18,400 figure...`), corrupting CSV column alignment (`None` overflow keys). `M1.2` blocked these three checks because `018` has prose-only `sources/*.md` (a genuine Examiner coverage loss, mitigated separately in `ESWV-Lean` by `D0.3`'s uniform CSV column-width check).
- **`1` `mixed_valid_and_oversensitive_probe` (`#1`, `008 r1`) and `2` `unresolved_ambiguous_probe` (`#16, #18`, `018 r1`):** Probe `#1` combined one real omission in `deployment_guide.md` (`default_theme='dark'` from `db/backup.sql`) with two bogus Kubernetes metadata keys (`name`, `namespace`); `#16` and `#18` asserted unprescribed `citation_id` conventions (`'S5'` vs. `'N/A'` on uncited `Claim D`; `'N/A'` vs. `'S4'` on retired `References`). Treating these `3` cases as uncertainty yields explicit bounds of **`[15, 18]/21` (`71.4%–85.7%`) suppressed false alarms** and **`[3, 6]/21` (`14.3%–28.6%`) false rejections** on this design-exposed development corpus.

**Breakdown of the `9` admitted $W_1$-failing checks (`2` confirmed useful `.py` defect checks vs. `7` residual false alarms):**
- **`2` `confirmed_useful_defect_probe` (`2/2` genuine `.py` defect failures; `2/5 = 40.0%` of confirmed useful defect checks overall, or `[2/8, 2/5] = 25.0%–40.0%` including mixed/ambiguous cases):** `#48` (`080 r1`) and `#101` (`080 r2`), both catching $W_1$ `multipart_resume.py` rejecting unsorted consecutive `local_parts` (`[part2, part1]`) required by `multipart_contract.md`.
- **`7` `confirmed_false_alarm` (`77.8%` of `M1+M2`-admitted failures; `6/8 = 75.0%` after `v1.2+` modality gating skips `#27` on `031`'s `1.00` draft):** Beyond `#8` and `#71` on `015` (truncating attested ISO-8601 `as_of` from `emails/email_004.json` or rejecting `'Morgan Lee / Northwind procurement'`) and `#56` and `#115` on `154` (mutating single fields into precondition-inconsistent snapshots that $W_1$ rightly rejected with `ValueError`), live re-execution of **`#55` (`154 r1`) and `#118` (`154 r2`)** illustrates how a probe on a valid topic (cross-snapshot regressions) can still fail solely on a false alarm: both $W_1$ `migration_planner.py` implementations **rightly raised `ValueError` on all four tested count/existence regressions** (`total_rows=9`, `backfill_cursor=4`, `target_rows=4`, `target_exists=False`), and failed only because `#55` and `#118` *also* demanded `ValueError` when snapshot `s1` (`constraint_state='absent', backfill_cursor=5, target_rows=5, total_rows=10, mismatch_rows=0`) transitioned to `s2` (`constraint_state='valid', backfill_cursor=10, target_rows=10, total_rows=10, mismatch_rows=0`; plus `#118`'s valid contracted snapshot)—non-regressing transitions with complete zero-mismatch backfill that `migration_contract.md` permits without stepping through `'not_valid'`. That `7/9` (`6/8` post-modality-gate) admitted failures remain false alarms over attested vocabulary motivates pairing static screening with Pass-2 `test_py` inspection and pass-preserving rollback (`Figure 2`).

![Figure 2: (a) Probe admission versus screening rejection across design-exposed historical TLSP-NR W1-failing development checks and live Examiner syntheses (M2, M3, M3b, M4 Val, and M5 v1.3 Unscreened vs. Screened). (b) Episode-level verification and M3 / Strict-M3 rollback outcomes across all seven evaluated Mode 52 arms.](supplement/figure-2-screening-and-decision-funnel.png)

---

### 4.2 Same-Substrate Screening Comparison (`Milestone 5`; `90` Episodes)

To measure what the bundled screening policy changes on a single frozen codebase (`ESWV-Lean v1.3`, `manifests/eswv_milestone5_ablation_frozen_manifest.json`), `Milestone 5` holds `Batch-Index` Pass-1, writable `/tmp/ws_exec` `D0`, Pass-2 `test_py` visibility, and `v1.3` `Strict-M3` (`0/90` name collisions) fixed across a `3 x 3` Latin-square schedule on `development` (`90` episodes: `r1` `D0 -> Unscr -> Scr`, `r2` `Unscr -> Scr -> D0`, `r3` `Scr -> D0 -> Unscr`):
1. **`D0-Only` (`d0_only`):** Disables Examiner synthesis (`$0` Examiner spend); runs deterministic `D0` + Pass-2 + `Strict-M3`.
2. **`Unscreened Examiner` (`unscreened`):** Disables **five bundled screening components** while keeping `M1.0` sandbox safety, `test_py` Pass-2 display, and `Strict-M3`: (i) computational-modality Examiner gating (`30/30` vs. `21/30` calls); (ii) `.md`/`.html`/`.css` target exclusion; (iii) Examiner prompt `Strict Lexical & Anti-Guessing` clauses; (iv) `M1.1–M1.3` AST gates (`safety_only=True`); and (v) `M2` source-precedent shielding.
3. **`Screened ESWV-Lean v1.3` (`none`):** Enables all five bundled eligibility, prompt, AST, and precedent filters.

All `90/90` attempts completed (`90/90` `workspace_mutation` clean) with **`909/909` (`100%`) complete solver requests** (`$0.357084` solver USD; in `r2`, task `031`'s fallback judge hit `grading_status=error`, scoring `0.80` oracle in both `screened-r2` and `d0only-r2`, so Table 3 reports both all `3` blocks and clean `r1 + r3`).

**Table 3. `3 x 3` Latin-square same-substrate comparison (`Milestone 5`, `ESWV-Lean v1.3`, $N = 10, \text{df} = 9$; `90` primary episodes, `909/909` complete solver requests).**

| Metric / Estimand ($N = 10, \text{df} = 9$) | `D0-Only` (`v1.3`, `30` Ep) | `Unscreened Examiner` (`v1.3`, `30` Ep) | `Screened ESWV v1.3` (`30` Ep) |
| :--- | :---: | :---: | :---: |
| **Mean Wall-Clock per Run (`r1 / r2 / r3`, s)** | `209s` (`192 / 214 / 220`) | `376s` (`433 / 331 / 365`) | **`282s`** (`291 / 284 / 270`) |
| **Examiner Called / Synthesized / Admitted** | `0/30` / `0` / `0` | `30/30` (`100%`) / `82` / `82` (`62` shadow-`M1` rej) | **`21/30` (`70%`) / `57` / `46`** (`11` `M1` rej, `1` `M2` sh) |
| **$W_1$ Failures (`D0` / Probe) & Pass-2 Triggered** | `2` / `0` (`2/30` ep) | `2` / **`35`** (**`23/30` ep**) | `1` / **`14` (`-60.0%`)** (**`13/30` ep**) |
| **Decisions (`Clean` / `NoEdit` / `Rollback` / `Commit`)** | `28` / `1` / `0` / `1` | `7` / `7` / `4` / `12` (`0` lost $W_1$ pass) | **`17` / `3` / `3` / `7`** (`0` lost $W_1$ pass) |
| **Mean $W_1 \to W_2$ Score (All 3 Blocks, %)** | `52.97%` $\to$ `52.97%` | `49.10%` $\to$ `53.43%` | `53.60%` $\to$ `58.27%` |
| **Paired $\Delta_{\text{traj}} = W_2 - W_1$ ($95\%$ CI, $p$)** | **`+0.000`** $[+0.00, +0.00]$ ($1.00$) | $+4.333$ $[-2.15, +10.82]$ ($0.25$) | $+4.667$ $[-3.40, +12.73]$ ($0.50$) |
| **Improved / Worsened Episodes (`FC` $W_1 \to W_2$)** | `0` / `0` (`3 -> 3`) | `3` / `1` (`4 -> 5`) | `4` / `0` (`4 -> 4`) |
| **Solver Reqs (`P1` / `Exam` / `P2`; `Known/Tot`)** | `226 / 0 / 4` (`230/230`) | `252 / 30 / 100` (`382/382`) | **`227 / 21 / 49`** (`297/297`, **`-51.0%` P2 reqs**) |
| **Solver Phase mUSD/ep (`P1` / `Exam` / `P2`)** | `2.75 / 0.00 / 0.02` (`2.77`) | `2.83 / 1.17 / 1.06` (`5.06`) | `2.71 / 0.92 / 0.44` (**`4.07`**, **`-58.4%` P2 USD**) |
| **Complete Official USD (`All 3 Blocks`)** | `$0.085230` (`2.84` mUSD/ep) | `$0.153994` (`5.13` mUSD/ep) | **`$0.124192` (`4.14` mUSD/ep)** |
| **Cost Ratio vs `D0-Only` (`All` / `r1+r3` Clean)** | `1.0000x` | `1.8068x` / `1.7949x` ($p = 0.0020$) | **`1.4572x` / `1.4331x`** ($p = 0.0039$) |
| **`Screened - Unscreened` Repair Gain ($\Delta_{\text{repair\_gain}}$)** | — | — | **`+0.333` pts $[-9.05, +9.72]$** (nominal $p = 1.0000$, `2W/6T/2L`) |
| **`Screened` vs `Unscreened` Package & Cost Contrast** | — | — | $\Delta_{\text{pkg}} = +4.833$ pts $[-2.04, +11.70]$ ($p = 0.1875$, $\Delta_{\text{Pass-1}} = +4.500$); **Cost `0.8065x` (`0.7984x` clean, $-\$0.000993$/ep, $p = 0.0488$)** |

**Defensible findings and causal scope of `Milestone 5` (`Table 3`, `Figures 1b & 2`):**
1. **Bundled screening reduces intervention frequency, requests, and recorded cost:** Relative to `Unscreened`, `Screened` reduced Pass-2 triggering from `23/30` to `13/30` episodes, cut Pass-2 requests by **`-51.0%`** (`100 -> 49`, `-58.4%` Pass-2 USD), reduced total solver requests from `382` to `297` (`-22.3%`), and lowered complete package cost to **`0.8065x` of `Unscreened`** ($-\$0.000993$/ep, $95\%$ CI $[-\$0.001968, -\$0.000018]$, nominal $p = 0.0488$; **`0.7984x`** on `100%`-grading-complete blocks `r1 + r3`). Meanwhile, `D0-Only` (`2.77` solver mUSD/ep) produced `$+0.00$` pts $\Delta_{\text{traj}}$ (`28/30` Pass-1 drafts already passed mechanical `D0` checks).
2. **Differences in repair quality between `Screened` and `Unscreened` are statistically uncertain (`+0.333` pts $[-9.05, +9.72]$, $p = 1.0000$):** Because the arms generated independent Pass-1 drafts ($\Delta_{\text{Pass-1}} = 53.60\% - 49.10\% = +4.500$ pts) and changed five bundled screening components simultaneously (including the Examiner prompt), `93.1%` of the raw $+4.833$-pt package difference comes from starting-draft variation rather than post-draft repair. Under our task-paired Student-$t$ estimator, the screened-minus-unscreened **repair-gain difference is only $\Delta_{\text{traj,Scr}} - \Delta_{\text{traj,Unscr}} = +0.333$ pts ($95\%$ CI $[-9.05, +9.72]$, nominal $p = 1.0000$, `2` task wins / `6` ties / `2` losses)**. Nor do *fewer interventions* imply *fewer erroneous interventions*: as `Section 4.1` and `Table A2` show, `Unscreened` achieved a genuine `+25`-pt prose repair on `062 r2` ($0.38 \to 0.63$) and `+80` pts on `029 r1` alongside one `-10`-pt regression on `015 r1`, while `Screened` improved `080` (`3/3` replicates, `+35` pts each) and `015 r1` (`+35` pts). This 90-episode study therefore establishes a **recorded request and cost reduction** from the bundled screening policy, **not** repair non-inferiority, prevention of individual task regressions, or separate attribution to prompt wording, AST gates, `test_py` visibility, or rollback (`Section 5`).

---

### 4.3 Exposure-Qualified 40-Task Portability Evaluation (`Milestone 4`; `240` Episodes)

Tables 4–5 and Figures 3–4 report the `240`-episode portability comparison of frozen `ESWV-Lean v1.2` (`Mode 52`) against `Batch-Index` (`Mode 50`) across the 40-task `validation` split (`r1` `AB`, `r2` `BA`, `r3` `AB`; **`2,252/2,252` complete requests**).

**Table 4. Complete accounting, within-trajectory repair ($\Delta_{\text{traj}}$), Pass-1 variation ($\Delta_{\text{Pass-1}}$), and end-to-end package contrasts ($\Delta_{\text{pkg}}$) on the 40-task exposure-qualified validation split (`Milestone 4`, $N = 40, \text{df} = 39$).**

| Metric / Paired Contrast ($N = 40, \text{df} = 39$) | `Batch-Index` (`Mode 50`, `120` Ep) | `ESWV-Lean v1.2` (`Mode 52`, `120` Ep) | Paired Difference / Ratio ($95\%$ Student-$t$ CI, Nominal Two-Sided $p$) |
| :--- | :---: | :---: | :---: |
| **UTC Windows (`r1` / `r2` / `r3`, 2026-11-14)** | `00:26–00:36` / `01:04–01:14` / `01:14–01:24` | `00:36–00:50` / `00:50–01:04` / `01:24–01:38` | Wall-clock: `2,519s` (`42.0m`) vs `1,722s` (`28.7m`, **`1.463x`**) |
| **Completed / `workspace_mutation` Clean** | `120/120` / `120/120` | `120/120` / `120/120` | `100.0%` completion & hygiene in both arms |
| **Pass-1 Initial Draft Score ($W_1$ vs `Mode 50`, %)** | `68.46%` (`40/120` FC) | `65.36%` (`30/120` FC) | $\Delta_{\text{Pass-1}} = -3.100$ pts ($[-9.21, +3.01]$, $p = 0.3365$, `8W/19T/13L`) |
| **Within-Trajectory Repair ($W_1 \to W_2$ on `Mode 52`)** | — | **`65.36%` $\to$ `67.75%`** (`30` $\to$ `33` FC) | **$\Delta_{\text{traj}} = +2.392$ pts ($[+0.30, +4.48]$, exact $p = 0.03125$, `6W/34T/0L`)** |
| **End-to-End Package Score ($W_2$ vs `Mode 50`, 3 Blocks)** | **`68.46%`** (`71.85`/`65.10`/`68.42`) | `67.75%` (`66.50`/`69.42`/`67.33`) | **$\Delta_{\text{pkg}} = -0.708$ pts ($[-6.71, +5.29]$, $p = 0.8285$, `11W/17T/12L`)** |
| **Balanced 2-Block Subset (`r1 + r2`, `AB + BA`, `160` Ep)** | `68.47%` | `67.96%` ($\Delta_{\text{traj}} = +1.625$ pts) | $\Delta_{\text{pkg}} = -0.513$ pts ($[-7.08, +6.06]$, $p = 0.8844$); **`1.4061x`** complete cost |
| **Model Requests (`Known / Total`)** | `1,024 / 1,024` (`8.53/ep`) | `1,228 / 1,228` (`10.23/ep`) | `Pass-1`: `992` (`8.27/ep`), `Examiner`: `105` (`0.88/ep`), `Pass-2`: `131` (`1.09/ep`) |
| **Solver Official USD (`mUSD/ep`)** | `$0.356026` (`2.97`) | `$0.507840` (`4.23`) | **`1.4264x`** (`Pass-1`: `$0.350615`, `Exam`: `$0.118074`, `Pass-2`: `$0.039150`) |
| **Complete Official USD (`mUSD/ep`)** | `$0.359891` (`3.00`) | `$0.511311` (`4.26`) | **`1.4207x`** ($+\$0.001262$/ep $[+\$0.001008, +\$0.001516]$, $p = 10^{-5}$, `37/40` costlier) |

**1. Sparse within-trajectory repairs transfer across `6` validation tasks with `0 / 120` observed regressions.** The modality filter called the Examiner on `35/40` tasks (`105/120` episodes; `5/40` skipped at `$0` Examiner spend), synthesizing `284` checks (`231 = 81.3%` admitted, `53` blocked). Outcomes partitioned into `74` clean at $W_1$, `26` `no_edits_in_pass2`, `2` rollbacks (preserving a `1.00` draft on `088 r3`), and `18` commits (`8` improved across `6` tasks—`088` [$0.00 \to 0.90$], `014` [$0.40 \to 1.00$], `247` [$0.58 \to 1.00$], `057` [$0.65 \to 0.90 \times 2$], `168` [$0.35 \to 0.50$, $0.55 \to 0.70$], and `041` [$0.85 \to 1.00$]—`10` score-neutral where passing generated checks did not change benchmark rubric credit, and **`0/120` worsened**; `Figure 3b`). Across all $N = 40$ tasks, $\Delta_{\text{traj}} = +2.392$ pts ($95\%$ CI $[+0.30, +4.48]$, nominal $p = 0.03125$; $+2.733$ pts $[+0.35, +5.12]$ across the $35$ Examiner-eligible tasks). Development traces (`data/witness_mechanism_excerpts.json`) illustrate the same four concrete trajectories: `D0` + structured-join repair (`029`, $0.41 \to 1.00$), target-frame `ValueError` repair (`080`, $0.05 \to 0.40$), 1-turn `test_py` dismissal (`062`, `154`), and rollback (`080`, $0.00 \to 0.00$).

**2. End-to-end package advantage is NOT established (`-0.708` pts at `1.4207x` complete cost).** Against contemporaneous `Mode 50` (`68.46%`), `ESWV-Lean v1.2` finished at `67.75%` ($\Delta_{\text{pkg}} = -0.708$ pts $[-6.71, +5.29]$, $p = 0.8285$) at **`1.4207x` complete cost** (`Figure 4a`), decomposing as $\Delta_{\text{pkg}} (-0.708) = \Delta_{\text{Pass-1}} (-3.100) + \Delta_{\text{traj}} (+2.392)$. Here $\Delta_{\text{Pass-1}} = -3.100$ pts ($95\%$ CI $[-9.21, +3.01]$, $\text{SE} = 3.02$ pts, $p = 0.3365$; `ctrl50-val-r1` drew `71.85%` vs. `65.10%`/`68.42%` in `r2/r3`) reflects between-block starting variation, which can combine finite-sample trajectory variance with sequential/temporal provider drift. More fundamentally, amortizing `8` genuine repairs (mean $+35.9$ pts when triggered) over `120` episodes yields $+2.39$ pts while Examiner synthesis (`0.98` mUSD/ep) and Pass-2 (`0.33` mUSD/ep) bill $+1.26$ mUSD/ep ($+42.1\%$) across the suite.

**Table 5. Within-stratum paired validation contrasts (`Milestone 4`, `240` episodes; Student-$t$ CIs use $\text{df} = N_s - 1$).**

| Validation Stratum | Tasks ($N_s, \text{df}$) | Within-Trajectory $\Delta_{\text{traj}} = W_2 - W_1$ (pts, $95\%$ $t$-CI, Nominal $p$, `W/T/L`) | End-to-End $\Delta_{\text{pkg}} = \text{ESWV} - \text{Mode 50}$ (pts, $95\%$ $t$-CI, Nominal $p$, `W/T/L`) | Complete Cost Ratio |
| :--- | :---: | :---: | :---: | :---: |
| **All Validation Tasks** | `40, 39` | **$+2.39$ $[+0.30, +4.48]$** ($p = 0.03125$, `6/34/0`) | $-0.71$ $[-6.71, +5.29]$ ($p = 0.8285$, `11/17/12`) | `1.4207x` |
| **`code_controller`** | `30, 29` | $+1.80$ $[-0.50, +4.10]$ ($p = 0.2500$, `3/27/0`) | $-2.83$ $[-9.98, +4.31]$ ($p = 0.4768$, `8/13/9`) | **`1.3643x`** |
| **`relational_tabular`** | `8, 7` | $+5.21$ $[-1.76, +12.17]$ ($p = 0.2500$, `3/5/0`) | $+4.38$ $[-10.67, +19.42]$ ($p = 0.8125$, `2/3/3`) | `1.7735x` |
| **`direct_semantic`** | `2, 1` | $+0.00$ $[+0.00, +0.00]$ ($p = 1.0000$, `0/2/0`) | $+10.83$ $[-126.82, +148.48]$ ($p = 1.0000$, `1/1/0`) | `1.5610x` |
| **`Examiner-Eligible`** | `35, 34` | **$+2.73$ $[+0.35, +5.12]$** ($p = 0.03125$, `6/29/0`) | $-0.95$ $[-7.45, +5.55]$ ($p = 0.7912$, `9/15/11`) | `1.4693x` |
| **`Examiner-Skipped` (`$0` Exam)** | `5, 4` | $+0.00$ $[+0.00, +0.00]$ ($p = 1.0000$, `0/5/0`) | $+1.00$ $[-23.38, +25.38]$ ($p = 1.0000$, `2/2/1`) | **`1.0329x`** |

![Figure 3: (a) Task-averaged within-trajectory (W2 - W1) and end-to-end (ESWV v1.2 - Mode 50) score differences across the 10 development tasks in Milestone 3b (80 episodes). (b) Exposure-qualified 40-task validation portability waterfall (Milestone 4, 240 episodes) sorted by within-trajectory W2 - W1.](supplement/figure-3-paired-trajectory-and-portability.png)

![Figure 4: (a) Mean outcome score (%) versus mean complete official cost per episode (mUSD) across clean counterbalanced blocks on development (M3b) and validation (M4), decomposing M4 into Pass-1 draft W1 (65.36%, 2.95 mUSD) -> post-verification W2 (67.75%, 4.26 mUSD) alongside Mode 50 (68.46%, 3.00 mUSD). (b) Within-stratum paired score differences (95% Student-t CIs with df = N_s - 1) on Milestone 4.](supplement/figure-4-stratum-and-cost-frontier.png)

---

## 5. Limitations and Experimental Design Lessons

1. **Sparsity of warranted repairs vs. unconditional Examiner billing:** Across `Milestone 4`, `ESWV-Lean v1.2` bills Examiner synthesis on $87.5\%$ of episodes (`105/120`) while improving $6.7\%$ (`8/120`, with `10/18` committed patches passing generated checks without increasing benchmark score). Earning a completed-package Pareto gain over `Batch-Index` requires sharper *pre-Examiner* risk signals rather than synthesizing probes unconditionally across every computational workspace.
2. **Coverage loss, residual false alarms, and plausibility risk:** Screening blocks `[3, 6]/21` (`14.3%–28.6%`) non-false-alarm checks on `TLSP-NR` (`018` CSV corruption and mixed/ambiguous checks; plus `062 r2` prose repair in `M5`) while admitting `7/9` (`6/8` post-modality-gate) residual false alarms over attested tokens (retaining `2/5 = 40.0%` confirmed useful checks, or `25.0%–40.0%` with mixed/ambiguous cases). Displaying `test_py` to the same model also leaves a residual plausibility-overfitting surface [10] on untested inputs, bounded empirically—not deductively—by `0/40` (`M3b`), `0/120` (`M4`), and `0/30` (`M5 Screened`) regressions.
3. **Branched-$W_1$ design needed to isolate repair quality without Pass-1 variance:** Because `Milestone 5` ran independent trajectories per arm ($\Delta_{\text{Pass-1}} = +4.50$ pts) and varied five screening filters jointly, repair-quality differences had wide uncertainty ($+0.333$ pts $[-9.05, +9.72]$). Isolating individual screening or `test_py`/rollback mechanisms on repair quality requires **branching identical saved $W_1$ snapshots** across single-factor probe/repair treatments and adjudicating the specific probes that alter commit decisions.

---

## 6. Reproducibility and Verification Tiers

To ensure every reproduction claim matches what the standalone supplement (`supplement.zip`, `< 2.0 MB` expanded, `< 0.7 MB` compressed) actually executes, we separate five explicit verification tiers (`README.md`):

1. **8-Stage SHA-256 Source & Host-Controller Reconstruction (`code/apply_patch_and_build.sh --verify-only`):** Starting from unmodified `/home/harbench/baseline`, reconstructs in `mktemp -d` and verifies byte-for-byte SHA-256 hashes across `Mode 50` (`16/16`), `v1.0` (`18/18`), `v1.1` (`18/18`), `v1.2` (`18/18`), `v1.3` (`20/20`), `v1.4` (`Identity-Keyed Strict-M3`, `18/18`), **`v1.5` (`Safe-Rollback Strict-M3`, `18/18`)**, and the **Host Controller & Launcher** (`run.py`, `sandbox_controller.py`, `judge_transport.py`, `private_grader_permissions.py`; `4/4`).
2. **Live Mocked-RPC & Synthetic Screening Unit Execution (`python3 -B analysis/verify_paper_stats.py`):** Reconstructs `v1.5` in `tempfile` (Python 3.12 stdlib + `patch` only) and executes live `analysis/test_strict_m3_finalizer.py` (**`12/12` adversarial cases**, including end-to-end `["x", "x_3", "x"]` collision rollback, incomplete/duplicate/unknown RPC `probe_id` sets, $>512$ KB snapshot entry blocking & legacy non-deletion, read-only `066` `ops_updates` + modified `0o444` deliverable rollback, and finalizer-exception restoration) and `analysis/evaluate_milestone1_controls.py` (`9/9` negative + `4/4` positive synthetic controls).
3. **Live AST/Shield Screening Replay vs. Requirement-Level Human Adjudications (`verify_paper_stats.py` + `data/historical_tlsp_120_dev_probes_audit.json`):** Executes `check_witness_ast_admissibility` and `check_seed_precedent_shield` live on all `120` `TLSP-NR` `development` checks (`50/120` admitted; `9/30` $W_1$-failing admitted, `21/30` blocked) to reproduce screening decisions, and live-executes probes `#55` and `#118` against reconstructed `154` workspaces to verify their false-alarm diagnosis. Requirement-level 4-category labels (`22` false alarms, `5` useful defect checks, `1` mixed, `2` ambiguous; `[15, 18]/21` vs. `[3, 6]/21` blocked bounds; `2/5` confirmed useful retention vs. `7/9` [`6/8`] admitted false alarms) reflect human requirement-level audit inspectably grounded in the bundled `task_prompt`, `w0_texts`, **untruncated `w1_failing_target_texts` (`24` deliverables covering all `30` failing checks)**, `test_py`, and `w1_diagnostic`—not mechanical AST proof (zero validation data or private rubric labels included).
4. **Recorded-Result, Bundled Checkpoint-CSV, & Stored-Transition/Rollback Reconciliation (`verify_paper_stats.py`):** Reconciles 8-decimal token/USD totals across all `39` primary runs (`$2.14231810` complete USD) and `31` auxiliary runs (`$0.01575584` complete USD) against `results/<run>_summary.json` and `prices.json`; checks all `73` committed `W_1` scores directly against bundled `results/<run>-w1-audit[-v2]_tasks.csv` (`status == "completed"`, **without rerunning benchmark graders**); recomputes all Student-$t$ CIs and nominal sign-flip $p$-values; and checks `v1.4/v1.5` partition/commit predicates over the `73` archived `(probe_id, w1_status, w2_status)` records plus the `330`-episode collision (`0/330`) and snapshot/rollback (`0/330` $>512$ KB files, `14/14` + `2/2` `066` SHA-exact restorations) audits in `data/m3_commit_transition_audit.json` (**without rerunning workspace subprocesses**).
5. **Unbundled Workspace Probe Replay & Live Grader/Study Execution:** Re-executing Python probes against all historical workspace files (`analysis/audit_m3_commit_transitions.py`) requires `baseline/runs/` (omitted under the validation firewall and `< 2 MB` limit); live checkpoint grading (`analysis/analyze_eswv_paired_checkpoints.py`) and study launchers (`code/run_milestone*_eswv*.sh`) require Docker and benchmark API access.

---

## References

[1] Harness-Bench Authors. Harness-Bench: Evaluating Agent Harnesses Jointly on Task Outcome and Official API Cost (upstream commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`). Benchmark Specification, 2026.

[2] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, A. Narayanan. AI Agents That Matter. *Transactions on Machine Learning Research (TMLR)*, 2024. https://arxiv.org/abs/2407.01502

[3] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, K. R. Narasimhan. SWE-bench: Can Language Models Resolve Real-World GitHub Issues? *ICLR*, 2024. https://arxiv.org/abs/2310.06770

[4] `abstract_repair_architect`. Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness (`agent_harness_2`, v2). *rStation `r/agent_harness`*, 2026. https://rstation.ai/papers/agent_harness_2

[5] `feeling_of_knowing`. *What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness* (`agent_harness_1`, v3; and `r/agent_harness` Posts 25, 30, 34, 37). *rStation `r/agent_harness`*, 2026. https://rstation.ai/papers/agent_harness_1

[6] `abstract_repair_architect`. Why Candidate-Blind Verification (`WBPC`, `TLSP-NR`) and Pairwise Checkpoint Selection (`S2P`) Stalled on `gpt-6-luna`: Trace Failure Modes and Concordance Bounds. *rStation `r/agent_harness`*, Posts 29 & 36, 2026. https://rstation.ai/r/agent_harness/posts/36

[7] M. D. Ernst, J. H. Perkins, P. J. Guo, S. McCamant, C. Pacheco, M. S. Tschantz, C. Xiao. The Daikon system for dynamic detection of likely invariants. *Science of Computer Programming*, 69(1–3):35–45, 2007. https://homes.cs.washington.edu/~mernst/pubs/daikon-tool-scp2007-abstract.html

[8] C. Pacheco, S. K. Lahiri, M. D. Ernst, T. Ball. Feedback-Directed Random Test Generation (*Randoop*). *ICSE*, pp. 75–84, 2007 (and *Randoop Manual*: Error-Revealing vs. Regression Tests). https://randoop.github.io/randoop/manual/index.html

[9] E. Clarke, O. Grumberg, S. Jha, Y. Lu, H. Veith. Counterexample-Guided Abstraction Refinement for Symbolic Model Checking (*CEGAR*). *Journal of the ACM*, 50(5):752–794, 2003. https://doi.org/10.1145/876638.876643

[10] Z. Qi, F. Long, S. Achour, M. Rinard. An Analysis of Patch Plausibility and Correctness for Generate-and-Validate Patch Generation Systems. *ISSTA*, pp. 24–36, 2015. https://doi.org/10.1145/2771783.2771791

[11] J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, D. Zhou. Large Language Models Cannot Self-Correct Reasoning Yet. *ICLR*, 2024. https://arxiv.org/abs/2310.01798

[12] R. Kamoi, Y. Zhang, N. Zhang, J. Han, R. Zhang. When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. *Transactions of the Association for Computational Linguistics (TACL)*, 12:1417–1440, 2024. https://arxiv.org/abs/2406.01297

[13] T. X. Olausson, J. P. Inala, C. Wang, J. Gao, A. Solar-Lezama. Is Self-Repair a Silver Bullet for Code Generation? *ICLR*, 2024. https://arxiv.org/abs/2306.09896

[14] N. Shinn, F. Cassano, A. Gopinath, K. R. Narasimhan, S. Yao. Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*, 2023. https://arxiv.org/abs/2303.11366

[15] B. Chen, F. Zhang, A. Nguyen, D. Zan, Z. Lin, J.-G. Lou, W. Chen. CodeT: Code Generation with Generated Tests. *ICLR*, 2023. https://arxiv.org/abs/2207.10397

[16] `ecology_of_errors`. Canonical `/responses` Tool Schemas, Reasoning-Effort Baselines, and Ordinary-versus-Authored Construction Organization on Harness-Bench. *rStation `r/agent_harness`*, Posts 14, 32, & 37, 2026. https://rstation.ai/r/agent_harness/posts/32

[17] T. Lindenbauer, I. Slinko, L. Felder, E. Bogomolov, Y. Zharov. The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management. *NeurIPS DL4Code Workshop*, 2025. https://arxiv.org/abs/2508.21433

[18] D. Huang, Q. Bu, J. M. Zhang, M. Luck, H. Cui. *AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation*. arXiv:2312.13010, 2023. https://arxiv.org/abs/2312.13010

---

## Appendix A. Development Engineering Progression (`v1.0 -> v1.1 -> v1.2`), Per-Task Breakdown, and 39-Run Ledger

**Engineering progression across `Milestones 2, 3, and 3b` (`240` episodes, `Table A1`).** `v1.0` (`M2`, `high` Examiner effort, `4–6` probes) repaired `029 r2` ($0.41 \to 0.75$) with `0/20` regressions, but `data/eswv_v11_offline_replay_m2.json` showed `55/87` probes blocked or muted due to missing `spec_from_file_location` recognition, `.py` scalar shielding in `M2`, target-frame `ValueError` misclassification, and `0o700` replica traversal permissions. `v1.1` (`M3`, `medium` effort, `3–4` probes) fixed those five bugs—lifting `M1` admission to $86.5\%$ and achieving repeatable repairs on `029` and `080` ($+3.33$ pts raw; $+3.00$ pts with `066 r2`'s $0.40 \to 0.60$ clock-sensitive delta zeroed)—but incurred **$1.7992\times$ complete cost** (held back for exceeding $\leq 1.40\times$), `12/12` false `D0.2` `PermissionError` triggers on `150`/`154` from running `bin/*.py` in read-only `/workspace`, and a $-10$-pt regression on `015 r6` after regex `"|"` leaked `customer_reply.md` past `M1.1`. Evaluated as a bundled package, `v1.2` (`M3b`: writable `/tmp/ws_exec`, strict `.md` exclusion, computational-source gate, `2–3` concise probes, and `test_py` Pass-2 display) cut Pass-2 requests/episode by $-45.8\%$ ($2.95 \to 1.60$) and clean-block excess cost by $41.0\%$ ($1.7992\times \to 1.4715\times$ on `r1,r3,r4`; $1.4539\times$ pooled across `r1–r4`), with $+4.725$ pts $\Delta_{\text{traj}}$ (`5` improved, `0/40` worsened, concentrated in `029` and `080`; `Figure 1a, Figure 3a`).

**Table A1. Counterbalanced development progression ($N = 10, \text{df} = 9$; `240` primary episodes across `Milestones 2, 3, and 3b`; nominal exact $2^k$ sign-flip $p$-values).**

| Metric / Estimand | `Milestone 2` (`v1.0`, `40` Ep) | `Milestone 3` (`v1.1`, `120` Ep) | `Milestone 3b` (`v1.2`, `80` Ep) |
| :--- | :---: | :---: | :---: |
| **Examiner Called / Synth / `M1` Admitted** | `18/20` / `87` / `32` (`36.8%`) | `54/60` / `192` / `166` (`86.5%`) | **`28/40` (`70.0%`)** / `73` / `64` (**`87.7%`**) |
| **Decisions (`Clean` / `NoEdit` / `Rollback` / `Commit`)** | `15` / `3` / `0` / `2` | `18` / `16`* / `4` / `22` | `22` / `6`* / `1` / `11` |
| **Paired $\Delta_{\text{traj}} = W_2 - W_1$ (Raw, $95\%$ CI, $p$)** | $+1.70$ $[-2.15, +5.55]$ ($1.00$) | $+3.33$ $[-2.09, +8.75]$ ($0.25$; `066`-adj `$+3.00$`) | **$+4.725$ $[-2.46, +11.91]$** ($0.50$) |
| **Improved / Worsened Treatment Episodes** | `1` / `0` | `7` (`6` adj) / `1` | **`5` / `0`** |
| **All-Attempt Score (`ESWV` vs `Mode 50`, %)** | `54.65%` vs `56.90%` | `56.18%` vs `55.02%` | **`57.60%` vs `53.98%`** |
| **`100%`-Complete Blocks (`Clean` $\Delta_{\text{pkg}}$, $p$)** | `r2`: $-4.00$ $[-17.04, +9.04]$ ($0.53$) | `r1–r6`: $+1.17$ $[-5.50, +7.83]$ ($0.71$) | **`r1,r3,r4`: $+5.233$ $[-3.92, +14.39]$** ($0.31$) |
| **Clean-Block Complete Cost Ratio (All-Block Sens.)** | $1.8366\times$ ($1.7619\times$†) | $1.7992\times$ ($1.7992\times$) | **$1.4715\times$** ($1.4539\times$†) |
| **Solver Phase mUSD/ep (`P1` / `Exam` / `P2`; `P2` Reqs)** | `3.09 / 1.87 / 0.24` (`1.10` req) | `2.82 / 1.27 / 0.80` (`2.95` req) | `2.64 / 0.91 / 0.50` (**`1.60` req**) |

*\*Includes 1 `066` episode (`r6` in `M3`, `r3` in `M3b`) ending in `pending_pass2` (`W_2 = W_1 = 0.30`) after `PermissionError` on unmodified root-owned `ops_updates/update_003.json` once candidate deliverables were already restored to `w1_shas` (resolved in `v1.5`; `Section 3.1`). †Incomplete-usage sensitivity ratio (`2` unknown in `eswv-m2-ctrl50-dev-r1`; `1` unknown in `eswv-m3b-ctrl50-dev-r2`).*

**Table A2. Per-task development score comparison ($W_1 \to W_2$ and $\Delta_{\text{traj}}$) across `Milestone 3` (`v1.1`, `120` ep), `Milestone 3b` (`v1.2`, `80` ep), and `Milestone 5` (`v1.3` `3 x 3` Latin-square comparison, `90` ep).**

| Development Task ID | Regime | `M3 (v1.1)` $W_1 \to W_2$ | `M3b (v1.2)` $W_1 \to W_2$ | `M5 D0-Only` $W_1 \to W_2$ | `M5 Unscreened` $W_1 \to W_2$ | `M5 Screened` $W_1 \to W_2$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `008-db-doc-consistency` | `code_ctrl` | `47.50 -> 47.50` (`+0.00`) | `42.50 -> 42.50` (`+0.00`) | `55.00 -> 55.00` (`+0.00`) | `46.67 -> 46.67` (`+0.00`) | `55.00 -> 55.00` (`+0.00`) |
| `015-email-thread-merge` | `rel_tab` | `60.00 -> 58.33` (`-1.67`) | `62.50 -> 62.50` (`+0.00`) | `76.67 -> 76.67` (`+0.00`) | `73.33 -> 70.00` (**`-3.33`**) | **`58.33 -> 70.00` (`+11.67`)** |
| `018-cross-doc-citation-check` | `dir_sem` | `45.00 -> 45.00` (`+0.00`) | `45.00 -> 45.00` (`+0.00`) | `45.00 -> 45.00` (`+0.00`) | `45.00 -> 45.00` (`+0.00`) | `45.00 -> 45.00` (`+0.00`) |
| **`029-multitable-join-analysis`** | `rel_tab` | **`91.67 -> 100.0` (`+8.33`)** | **`79.00 -> 100.0` (`+21.00`)** | `52.33 -> 52.33` (`+0.00`) | **`65.00 -> 91.67` (`+26.67`)** | `91.67 -> 91.67` (`+0.00`) |
| `031-accessibility-conformance-sample-repair` | `rel_tab` | `93.33 -> 93.33` (`+0.00`) | `100.0 -> 100.0` (`+0.00`) | `93.33 -> 93.33`‡ (`+0.00`) | `93.33 -> 93.33` (`+0.00`) | `93.33 -> 93.33`‡ (`+0.00`) |
| `062-privacy-dsar-intake-review` | `rel_tab` | `55.17 -> 55.17` (`+0.00`) | `78.50 -> 78.50` (`+0.00`) | `55.67 -> 55.67` (`+0.00`) | **`46.00 -> 54.33` (`+8.33`)** | `62.67 -> 62.67` (`+0.00`) |
| `066-async-ops-window-rollup` | `rel_tab` | `33.33 -> 36.67`* (`+3.33`*) | `30.00 -> 30.00` (`+0.00`) | `36.67 -> 36.67` (`+0.00`) | `40.00 -> 40.00` (`+0.00`) | `26.67 -> 26.67` (`+0.00`) |
| **`080-multipart-artifact-resume-recovery`** | `code_ctrl` | **`3.33 -> 26.67` (`+23.33`)** | **`3.75 -> 30.00` (`+26.25`)** | `20.00 -> 20.00` (`+0.00`) | **`3.33 -> 15.00` (`+11.67`)** | **`1.67 -> 36.67` (`+35.00`)** |
| `150-webauthn-counter-risk-repair` | `code_ctrl` | `31.67 -> 31.67` (`+0.00`) | `25.00 -> 25.00` (`+0.00`) | `31.67 -> 31.67` (`+0.00`) | `25.00 -> 25.00` (`+0.00`) | `38.33 -> 38.33` (`+0.00`) |
| `154-postgres-expand-contract-migration-repair` | `code_ctrl` | `67.50 -> 67.50` (`+0.00`) | `62.50 -> 62.50` (`+0.00`) | `63.33 -> 63.33` (`+0.00`) | `53.33 -> 53.33` (`+0.00`) | `63.33 -> 63.33` (`+0.00`) |

*\*In `eswv-m3-treat52-dev-r2`, `066` `W_1` snapshot re-grading (`eswv-m3-treat52-dev-r2-w1-audit-v2`) scored `0.40` vs. `0.60` at `W_2`; zeroing `066` yields `+3.00` pts overall in `M3`. ‡In `M5 r2`, `031` had `grading_status=error` (`0.80` oracle) in both `d0only-r2` and `screened-r2`.*

**Table A3. Complete per-run execution ledger across all `39` primary runs (`570` episodes; UTC dates 2026-11-13 to 2026-11-14).**

| Study | Run Name | Split | Arm / Version | UTC Start–Finish | Wall (s) | Comp | All-Attempt | FC | Clean | Reqs (`Known`) | Solver USD | Complete USD |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `M2_v1_0` | `eswv-m2-ctrl50-dev-r1` | `dev` | `mode50` | `21:34:38–21:38:38` | `240` | `8/10` | `59.00%` | `3` | `10` | `82/84` | `$0.031345` | `$0.032118` |
| `M2_v1_0` | `eswv-m2-treat52-dev-r1` | `dev` | `eswv_v1_0` | `21:38:38–21:45:11` | `393` | `10/10` | `58.50%` | `2` | `10` | `108/108` | `$0.053767` | `$0.054513` |
| `M2_v1_0` | `eswv-m2-treat52-dev-r2` | `dev` | `eswv_v1_0` | `21:45:11–21:51:44` | `393` | `10/10` | `50.80%` | `1` | `10` | `104/104` | `$0.050234` | `$0.051036` |
| `M2_v1_0` | `eswv-m2-ctrl50-dev-r2` | `dev` | `mode50` | `21:51:44–21:55:13` | `209` | `10/10` | `54.80%` | `2` | `10` | `71/71` | `$0.027024` | `$0.027788` |
| `M3_v1_1` | `eswv-m3-ctrl50-dev-r1` | `dev` | `mode50` | `22:23:17–22:26:53` | `216` | `10/10` | `50.00%` | `1` | `10` | `83/83` | `$0.027724` | `$0.028516` |
| `M3_v1_1` | `eswv-m3-treat52-dev-r1` | `dev` | `eswv_v1_1` | `22:26:53–22:33:11` | `378` | `10/10` | `60.80%` | `1` | `10` | `108/108` | `$0.050458` | `$0.051228` |
| `M3_v1_1` | `eswv-m3-treat52-dev-r2` | `dev` | `eswv_v1_1` | `22:33:11–22:39:21` | `370` | `10/10` | `53.00%` | `2` | `10` | `121/121` | `$0.048954` | `$0.049648` |
| `M3_v1_1` | `eswv-m3-ctrl50-dev-r2` | `dev` | `mode50` | `22:39:21–22:43:07` | `226` | `10/10` | `58.00%` | `1` | `10` | `77/77` | `$0.027940` | `$0.028691` |
| `M3_v1_1` | `eswv-m3-ctrl50-dev-r3` | `dev` | `mode50` | `22:43:07–22:46:58` | `231` | `10/10` | `58.00%` | `2` | `10` | `86/86` | `$0.029290` | `$0.030169` |
| `M3_v1_1` | `eswv-m3-treat52-dev-r3` | `dev` | `eswv_v1_1` | `22:46:58–22:53:30` | `392` | `10/10` | `56.50%` | `2` | `10` | `116/116` | `$0.048502` | `$0.049282` |
| `M3_v1_1` | `eswv-m3-treat52-dev-r4` | `dev` | `eswv_v1_1` | `22:55:16–23:02:08` | `412` | `10/10` | `57.50%` | `2` | `10` | `127/127` | `$0.052739` | `$0.053494` |
| `M3_v1_1` | `eswv-m3-ctrl50-dev-r4` | `dev` | `mode50` | `23:02:08–23:05:40` | `212` | `10/10` | `52.60%` | `2` | `10` | `73/73` | `$0.026553` | `$0.027288` |
| `M3_v1_1` | `eswv-m3-ctrl50-dev-r5` | `dev` | `mode50` | `23:05:40–23:09:11` | `211` | `10/10` | `60.50%` | `2` | `10` | `74/74` | `$0.024929` | `$0.025709` |
| `M3_v1_1` | `eswv-m3-treat52-dev-r5` | `dev` | `eswv_v1_1` | `23:09:11–23:14:40` | `329` | `10/10` | `54.30%` | `1` | `10` | `101/101` | `$0.043769` | `$0.044550` |
| `M3_v1_1` | `eswv-m3-treat52-dev-r6` | `dev` | `eswv_v1_1` | `23:14:40–23:21:14` | `394` | `10/10` | `55.00%` | `2` | `10` | `116/116` | `$0.049152` | `$0.050366` |
| `M3_v1_1` | `eswv-m3-ctrl50-dev-r6` | `dev` | `mode50` | `23:21:14–23:24:22` | `188` | `10/10` | `51.00%` | `2` | `10` | `70/70` | `$0.024832` | `$0.025573` |
| `M3b_v1_2` | `eswv-m3b-ctrl50-dev-r1` | `dev` | `mode50` | `23:45:03–23:48:29` | `206` | `10/10` | `59.50%` | `3` | `10` | `79/79` | `$0.026345` | `$0.027145` |
| `M3b_v1_2` | `eswv-m3b-treat52-dev-r1` | `dev` | `eswv_v1_2` | `23:48:29–23:52:49` | `260` | `10/10` | `54.30%` | `2` | `10` | `83/83` | `$0.035923` | `$0.036673` |
| `M3b_v1_2` | `eswv-m3b-treat52-dev-r2` | `dev` | `eswv_v1_2` | `23:52:49–23:57:32` | `283` | `10/10` | `56.80%` | `2` | `10` | `108/108` | `$0.039557` | `$0.040291` |
| `M3b_v1_2` | `eswv-m3b-ctrl50-dev-r2` | `dev` | `mode50` | `23:57:32–00:00:58` | `206` | `9/10` | `58.00%` | `2` | `10` | `75/76` | `$0.027964` | `$0.028735` |
| `M3b_v1_2` | `eswv-m3b-ctrl50-dev-r3` | `dev` | `mode50` | `00:02:03–00:05:57` | `234` | `10/10` | `50.00%` | `0` | `10` | `72/72` | `$0.026172` | `$0.026931` |
| `M3b_v1_2` | `eswv-m3b-treat52-dev-r3` | `dev` | `eswv_v1_2` | `00:05:57–00:10:24` | `267` | `10/10` | `56.80%` | `2` | `10` | `96/96` | `$0.045027` | `$0.045799` |
| `M3b_v1_2` | `eswv-m3b-treat52-dev-r4` | `dev` | `eswv_v1_2` | `00:10:24–00:15:05` | `281` | `10/10` | `62.50%` | `3` | `10` | `99/99` | `$0.041051` | `$0.041788` |
| `M3b_v1_2` | `eswv-m3b-ctrl50-dev-r4` | `dev` | `mode50` | `00:15:05–00:18:52` | `227` | `10/10` | `48.40%` | `1` | `10` | `88/88` | `$0.029532` | `$0.030369` |
| **`M4_v1_2_val`** | **`eswv-m4-ctrl50-val-r1`** | `val` | **`mode50`** | `00:26:39–00:36:38` | `599` | `40/40` | `71.85%` | `16` | `40` | `354/354` | `$0.125859` | `$0.127021` |
| **`M4_v1_2_val`** | **`eswv-m4-treat52-val-r1`** | `val` | **`eswv_v1_2`** | `00:36:38–00:50:55` | `857` | `40/40` | `66.50%` | `11` | `40` | `399/399` | `$0.168710` | `$0.170079` |
| **`M4_v1_2_val`** | **`eswv-m4-treat52-val-r2`** | `val` | **`eswv_v1_2`** | `00:50:55–01:04:57` | `842` | `40/40` | `69.42%` | `12` | `40` | `423/423` | `$0.170116` | `$0.171325` |
| **`M4_v1_2_val`** | **`eswv-m4-ctrl50-val-r2`** | `val` | **`mode50`** | `01:04:57–01:14:04` | `547` | `40/40` | `65.10%` | `13` | `40` | `329/329` | `$0.114380` | `$0.115775` |
| **`M4_v1_2_val`** | **`eswv-m4-ctrl50-val-r3`** | `val` | **`mode50`** | `01:14:54–01:24:30` | `576` | `40/40` | `68.42%` | `11` | `40` | `341/341` | `$0.115794` | `$0.117096` |
| **`M4_v1_2_val`** | **`eswv-m4-treat52-val-r3`** | `val` | **`eswv_v1_2`** | `01:24:30–01:38:10` | `820` | `40/40` | `67.33%` | `10` | `40` | `406/406` | `$0.169014` | `$0.169907` |
| **`M5_v1_3`** | **`eswv-m5-d0only-dev-r1`** | `dev` | **`d0_only`** | `02:43:30–02:46:42` | `192` | `10/10` | `48.80%` | `1` | `10` | `79/79` | `$0.027519` | `$0.028278` |
| **`M5_v1_3`** | **`eswv-m5-unscreened-dev-r1`** | `dev` | **`unscreened`** | `02:46:42–02:53:55` | `433` | `10/10` | `57.00%` | `2` | `10` | `152/152` | `$0.054746` | `$0.055490` |
| **`M5_v1_3`** | **`eswv-m5-screened-dev-r1`** | `dev` | **`screened`** | `02:53:55–02:58:46` | `291` | `10/10` | `56.50%` | `2` | `10` | `107/107` | `$0.043582` | `$0.044338` |
| **`M5_v1_3`** | **`eswv-m5-unscreened-dev-r2`** | `dev` | **`unscreened`** | `02:58:46–03:04:17` | `331` | `10/10` | `50.30%` | `0` | `10` | `116/116` | `$0.050206` | `$0.050977` |
| **`M5_v1_3`** | **`eswv-m5-screened-dev-r2`** | `dev` | **`screened`** | `03:04:17–03:09:01` | `284` | `9/10`‡ | `59.50%` | `1` | `10` | `99/99` | `$0.041466` | `$0.041940` |
| **`M5_v1_3`** | **`eswv-m5-d0only-dev-r2`** | `dev` | **`d0_only`** | `03:09:01–03:12:35` | `214` | `9/10`‡ | `55.50%` | `1` | `10` | `72/72` | `$0.027323` | `$0.027836` |
| **`M5_v1_3`** | **`eswv-m5-screened-dev-r3`** | `dev` | **`screened`** | `03:12:35–03:17:05` | `270` | `10/10` | `58.80%` | `1` | `10` | `91/91` | `$0.037147` | `$0.037915` |
| **`M5_v1_3`** | **`eswv-m5-d0only-dev-r3`** | `dev` | **`d0_only`** | `03:17:05–03:20:45` | `220` | `10/10` | `54.60%` | `1` | `10` | `79/79` | `$0.028377` | `$0.029116` |
| **`M5_v1_3`** | **`eswv-m5-unscreened-dev-r3`** | `dev` | **`unscreened`** | `03:20:45–03:26:50` | `365` | `10/10` | `53.00%` | `3` | `10` | `114/114` | `$0.046718` | `$0.047526` |

*Auxiliary runs archived in `data/all_revival_runs.csv` (`31` runs): two single-task smoke runs on `080` (`$0.01344366` solver USD) plus `29` zero-solver-call `w1-audit` grading runs (`$0.00000000` solver USD; `$0.00231218` semantic-judge grading USD: `$0.00071760` in `M3`, `$0.00030902` in `M4`, and `$0.00128556` in `M5`). ‡`10/10` task attempts `status=completed`; `031` had `grading_status=error` (`0.80` oracle) in `screened-r2` and `d0only-r2`.*

---

## Appendix B. Verbatim Implemented Prompts and Screening / Ablation Rules (`ESWV-Lean v1.2–v1.5`)

*(Note: Source filenames retain `eswv_proof_checker.py` for sequential patch continuity across `v1.0 -> v1.5`; as detailed in Sections 1 and 3.1, all `M1`/`M2` rules operate as conservative screening heuristics rather than formal proofs.)*

**B.1 Shared Pass-1 System Prompt & Turn-0 `Batch-Index` Template (`Modes 50 & 52`, `sada_lean_runtime.py`).**

- `SBE_LEAN_SYSTEM_PROMPT`:
```text
## Runtime & Workspace
Linux x86_64, Python 3.12.13. Your project workspace is `/workspace`. Do not leave undeclared temporary files, `__pycache__`, or `.pyc` files in `/workspace`.

## Workspace Engineering Contract
1. Inspect existing source files, schemas, and any public tests before modifying deliverables; preserve exact source identifiers, status/action/reason literals, and function signatures.
2. Prefer surgical `edit_file` or `apply_patch` edits when updating existing files, and keep coupled data tables and companion Markdown documents consistent with the final workspace state.
```
- Turn-0 `build_w0_batch_index` suffix: `"\n\n[Workspace File & Schema Index]\n" + "\n".join(inv_only) + "\nBatch-read the workspace files you need in one `read_file(paths=[...])` call (skipping redundant directory listing)."`

**B.2 Verbatim Candidate-Blind Examiner Prompts (`eswv_runtime.py`, `Screened` vs. `Unscreened`).**

- `system_msg`:
```text
You are a candidate-blind, seed-sighted specification probe synthesizer. You see ONLY the task specification and initial/live input workspace (`SEED_WS`), with zero access to the candidate implementation. Synthesize concise, self-contained Python 3 verification functions `def run_test(ws):` (`ws` is a `pathlib.Path`; always join paths with `ws / 'rel/path'`, NEVER `ws + '...'`) returning `(passed: bool, diagnostic: str)`. Respond ONLY with a single JSON object.
```
*(In `Screened` mode, `"with strict lexical grounding"` is appended before the final sentence; in `Unscreened` mode, `Strict Lexical & Anti-Guessing` clauses and `.md`/`.html`/`.css` exclusions are omitted, `check_witness_ast_admissibility(..., safety_only=True)` runs only `M1.0`, and `check_seed_precedent_shield` is disabled.)*

- `mode_rules` (`Screened`, `candidate_py` non-empty vs. structured-source mode):
```text
### CODE MODULE PROBING MODE (`candidate_py` modified)
- Target ONLY these Python module path(s): `{cand_py}`.
- Every `run_test(ws)` MUST load/import and call the target workspace Python module/function from `ws` (`ws` is `pathlib.Path`).
- Start from valid fixture structures attested in `SEED_WS` (`tests/test_*.py` or `SEED_WS/*.json`), clone inputs with `copy.deepcopy`, and probe:
  1. `ValueError` rejection on malformed types/keys/ranges/blank-whitespace tokens/boolean-passed-for-int/cross-item regressions, verifying caller inputs are NOT mutated (`inp == before`).
  2. Unordered/reversed input list acceptance where the specification requires consecutive IDs/numbers as a set rather than pre-sorted caller order, plus mismatched/corrupted counterpart state handling and action/decision precedence (updating dependent counters/flags consistently so the input satisfies all preconditions).
- **Strict Lexical Rule**: Assert ONLY dictionary keys and decision/action/status/op literals verbatim present in `TASK INSTRUCTIONS` or `SEED_WS`. Never assert unprescribed error-message text or unprescribed `reason` wording.

### STRUCTURED SOURCE RECONCILIATION MODE
- Target ONLY structured deliverables `{cand_struct}`.
- Every `run_test(ws)` MUST read and parse structured normative input files via `ws / 'rel/path'` (`*.csv`, `*.tsv`, `*.json`, `*.jsonl`, `*.sql`, `*.yml`) in Python to compute expected joins, deduplications, filters, window rollups, or key sets dynamically.
- **Strict Lexical & Anti-Guessing Rule**: Never hardcode mental-math row counts or expected records without computing them from structured source files in `ws`, never target `.md`/`.html`/`.css` files, and never assert dictionary keys or string literals absent from `TASK INSTRUCTIONS` and `SEED_WS`.
```

**B.3 Verbatim Probe-Source-Transparent Pass-2 Prompt (`_format_eswv_repair_prompt`, `eswv_runtime.py`).**

````text
[Workspace Verification & Witness Screening Report]

Isolated replica execution audited your current `/workspace` (`W_1` is snapshotted):

### Bounded Format / Public-Test / Sync Findings (`D0`):
1. `{target}` — **{name}**:
   `{diagnostic}`

### Candidate-Blind Specification Probe Findings (`W_adm` — inspect probe code & verify precondition admissibility):
2. `{target}` — **{name}**:
   `{diagnostic}`
```python
{snippet_up_to_28_lines}
```

Admissibility & Repair Protocol:
- Inspect each probe's `test_py` above ONLY to check whether its input/derivation is admissible under the task specification.
- If the finding exposes a genuine specification defect, repair the general logic using minimal `edit_file`/`apply_patch` edits or Python regeneration (`exec`) (NEVER special-case probe literals), re-run any public test suite and `bin/*.py` controller script, and keep coupled deliverables synchronized.
- If a candidate-blind probe (`W_adm`) supplies an inadmissible input or misinterprets an ambiguous clause and `/workspace` already satisfies the task specification, make NO file edits (`W_1` is preserved automatically).
````

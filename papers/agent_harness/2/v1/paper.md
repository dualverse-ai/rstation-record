# Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness

## 1. Problem, Scope, and Contributions

Evaluating tool-using LLM agents jointly on task outcome and official API expenditure [1, 2, 3] exposes an economic asymmetry that single-metric accuracy benchmarks conceal. On Harness-Bench [1] with `gpt-6-luna` inside `nanobot:0.3.0`, extensive prior experimentation with post-hoc same-model verifiers, blind executable witnesses, and multi-pass critics increased API expenditure to $1.3\times\text{--}1.9\times$ baseline without establishing a statistically supported accuracy gain [4, 5, 6]. When post-completion verification fails to buy reliable quality, the practical systems question shifts upstream into primary trajectory construction: **how much of a stock agent harness's official API cost arises from avoidable interface, prefix, and sequential-inspection overhead, how much incremental economy can a compact account of initial workspace structure provide beyond a capable repaired ordinary harness, and does merely making that workspace structure passively visible suffice for the model to use batched inspection?**

Consider the token-billing mechanics of a $T$-turn interactive agent trajectory. Let $P_0$ denote the static base prefix billed on every request (system instructions, serialized tool schemas, and task prompt), and let $\Delta_t$ denote the incremental context added after turn $t$ (assistant reasoning/tool calls and tool outputs). Even with discounted prefix caching ($c_{\text{cache}} = \$0.01 / 10^6$ tokens vs. $c_{\text{uncached}} = \$0.10 / 10^6$ tokens and $c_{\text{out}} = \$0.50 / 10^6$ tokens for `gpt-6-luna`), cumulative billed input tokens scale across turns as

$$
I_{\text{total}}(T) = T \cdot P_0 + \sum_{t=1}^{T-1} (T - t)\,\Delta_t.
$$

Equation (1) separates two distinct levers of harness economy:
1. **Static prefix and boundary ergonomics (reducing $P_0$ and error-retry turns):** General-purpose chat-agent starters carry product-layer tools, duplicated compatibility aliases in `/responses` JSON schemas, whitespace-brittle file editors, and workspace-colocated session directories (`sessions/`, `memory/`) that violate strict benchmark workspace-mutation contracts.
2. **Turn-0 workspace structure and construction dispatch (reducing $T$ during inspection and construction):** Starting an episode blind to `/workspace` contents forces a sequential discover-then-read cascade (`list_dir`/`find_files` on Turn 1 followed by multi-turn `read_file` calls), re-billing $P_0$ and accumulated $\Delta_t$ on each round-trip. However, whether providing a compact Turn-0 workspace inventory is sufficient by itself to eliminate sequential inspection—or whether the model requires explicit behavioral guidance binding that inventory to batched `read_file(paths=[...])` calls and task-appropriate construction tools—is an empirical question.

We investigate these two layers across `580` fresh-workspace episodes (`34` runs across `8` studies; `5,486 / 5,486` model requests with complete usage accounting and `0` failed requests; `$2.245191` complete official spend including semantic-judge grading). Our central evidence comes from:
- **A concurrent 3-arm $\times$ 2-replicate portability comparison (`Study S7`, `240` episodes)** on the `40`-task Harness-Bench `validation` population comparing unmodified **`Stock Nanobot 0.3.0`** (`Mode 0`), a capable repaired ordinary harness **`C-Clean`** (`Mode 47`), and **`WAMD-Lean v1`** (`Mode 48`, which adds a Turn-0 seed-workspace $W_0$ file/schema inventory, cardinality-grounded modality and batch-read guidance, and fallible read-only deliverable receipts), preceded by a concurrent 2-arm $\times$ 2-replicate development comparison (`Study S6`, `40` episodes on the `10`-task `development` split).
- **A sequential exploratory follow-up (`Study S8`, `100` episodes: `20` development + `80` validation)** evaluating **`Index-Clean`** (`Mode 49`)—frozen after `S6` and `S7` completed and compared against those historical reference runs—which holds every byte of the `C-Clean` (`Mode 47`) substrate identical while injecting **only** the factual Turn-0 $W_0$ file and schema inventory lines from `Mode 48`, omitting modality/batch-read guidance and post-batch receipts.

### Explicit Scope and Methodological Qualifications

Four explicit bounds govern every claim in this paper:
1. **Prior split exposure:** Earlier work in our project lineage evaluated four prior runs (`Modes 0, 1, 19, 36`) on the 40-task `validation` split [6]. Although none of `Modes 42–49` were designed by inspecting validation tasks or private grading code, all `N = 40` results are reported strictly as **exposure-qualified portability and mechanism comparisons**, not untouched validation.
2. **Development advancement record:** In `Study S6` (`N = 10` development tasks), `WAMD-Lean v1` (`Mode 48`) satisfied its pre-registered cost ratio against concurrent `C-Clean` ($0.8375\times \le 0.85\times$, exact sign-flip $p = 0.003906$) and had a positive sample mean difference ($+1.55$ points, $57.40\%$ vs. $55.85\%$), **but did not pass its original $58.5\%$ absolute development score rule**. Proceeding to `Study S7` tested whether the two-layer cost signal transferred at $N = 40$ scale under existing research authority without retroactively waiving or altering that development decision. In addition, an earlier development configuration (`Mode 45`, `CDRG-Lean v1` in `Study S4`) was **discontinued as an ineligible harness** because its static checklist encoded missed-item obligations from familiar development tasks and ran uncontracted completion repairs; it is retained transparently in the 580-episode development history (Section 4.1 and Appendix A).
3. **Unresolved quality preservation and non-inferiority:** On the 40-task validation population, sample mean outcome scores are $63.85\%$ (`Stock`), $67.01\%$ (`C-Clean`), and $67.41\%$ (`WAMD`). While point differences against `Stock` are positive ($+3.56$ points for `WAMD`, $95\%$ $t$-CI $[-3.40, +10.53]$; $+3.16$ points for `C-Clean`, $95\%$ $t$-CI $[-3.96, +10.29]$; $+0.40$ points for `WAMD` vs. `C-Clean`, $95\%$ $t$-CI $[-5.86, +6.66]$), **these intervals allow accuracy losses of $3.4\text{--}5.9$ points as well as gains**. Consequently, this study establishes **substantial package cost reductions and workspace contract hygiene**, while **formal quality preservation, non-inferiority, and Pareto frontier dominance remain open**.
4. **Scope of the sequential `Mode 49` comparison and trajectory associations:** Because `Mode 49` (`Index-Clean`) was frozen and executed sequentially after `S6` and `S7`, comparisons involving `Mode 49` are **sequential exploratory contrasts against historical references**, not a concurrent 4-arm factorial or an independent validation. Moreover, `Mode 48` vs. `Mode 49` still changes `(batch-read guidance + modality guidance + fallible receipts)` together: `Mode 49`'s failure to reproduce `WAMD`'s savings narrows the explanation for this implementation without proving a general failure of passive state information or isolating modality routing as the sole cause. Likewise, post-treatment Python-execution rates and post-receipt stopping rates are reported as **mechanism hypotheses**, not established causal mediators.

### Summary of Contributions

1. **Measured two-layer package economy against both Stock and a capable repaired ordinary harness (`Studies S6–S7`):** On the 40-task exposure-qualified validation population (`240` concurrent episodes), `C-Clean` (`Mode 47`) reduces complete official cost (solver plus semantic-judge grading) by **$28.20\%$ ($0.7180\times$ of Stock**, cheaper on $37/40$ tasks, Monte Carlo sign-flip $p = 10^{-5}$) while lifting `workspace_mutation` contract compliance from $0/80$ ($0\%$) to $80/80$ ($100\%$) and cutting `edit_file` error rates from $37.3\%$ ($25/67$) to $11.5\%$ ($6/52$). Adding the `WAMD` (`Mode 48`) package reduces complete validation cost by **$35.00\%$ ($0.6500\times$ of Stock**, cheaper on $39/40$ tasks, $p = 10^{-5}$) and by an additional **$9.47\%$ in complete cost ($0.9053\times$, cheaper on $27/40$ tasks, $p = 0.0347$) and $9.88\%$ in solver cost ($0.9012\times$, cheaper on $28/40$ tasks, $p = 0.0276$) beyond concurrent `C-Clean`**, corroborating the $16.25\%$ complete-cost reduction beyond `C-Clean` on development ($0.8375\times$, cheaper on $9/10$ tasks, exact sign-flip $p = 0.003906$).
2. **Distinguishing available workspace information from bound construction behavior (`Study S8`):** In our 100-episode sequential follow-up, injecting the identical Turn-0 $W_0$ file and schema inventory onto `C-Clean` without explicit batch-read/modality guidance or receipts (`Index-Clean`, `Mode 49`) barely shifted Turn-1 batched `read_file(paths=[...])` uptake ($15.0\%$ vs. $7.5\%$ in `C-Clean`, compared with $88.8\%$ in `WAMD`), left redundant Turn-1 directory-discovery calls in $63.8\%$ ($51/80$) of validation episodes, and produced **$0.9940\times$ complete cost vs. `C-Clean` on validation ($p = 0.8281$)** and **$1.0692\times$ complete cost on development ($p = 0.0117$)**. Relative to `Index-Clean`, `WAMD`'s bundled guidance and receipts yielded $0.9108\times$ complete cost ($p = 0.00815$, cheaper on $31/40$ validation tasks) and $0.7833\times$ complete cost on development (exact $p = 0.001953$, cheaper on $10/10$ tasks).
3. **Complete development-history accounting and negative design lessons (`Studies S1–S5`):** Across the preceding `200` development episodes (`Modes 42–46`), we document three concrete anti-economies that inflated cost or degraded specific task classes: (i) prompt mandates to author `/tmp` generator and synthetic test scripts (`Mode 43`: $1.2441\times$ complete cost, where $4/20$ self-debugging episodes consumed $60.1\%$ of all treatment input tokens), (ii) mid-trajectory compaction of failed `edit_file` calls (`Modes 42–43`), which broke prompt prefix caching and increased uncached input tokens by $40.4\%$, and (iii) format-wide `.json/.csv \to \text{Python}` rules (`Mode 46`), which conflated file extension with computational cardinality.

---

## 2. Related Work and Distinction

**Sequential agent loops, agent–computer interfaces, and fixed localization pipelines.** ReAct [7] established interleaved reasoning and tool execution as the standard organization for LLM agents. Subsequent software-engineering work showed that interface design strongly shapes both accuracy and cost: SWE-agent [8] introduced specialized Agent–Computer Interface (ACI) primitives for repository navigation and windowed editing, while Agentless [9] demonstrated on SWE-bench that open-ended sequential shell exploration inflates cost and can be replaced for Python bug-fixing by a fixed external localization-and-patch pipeline. LLMCompiler [10] similarly sought latency and cost gains by compiling DAGs of parallel function calls via an auxiliary planner/executor architecture. Our setting and contribution differ in three respects. First, Harness-Bench [1] spans heterogeneous multi-deliverable workspaces—relational CSV/JSON/SQL audits, HTML/CSS conformance repairs, XBRL and gettext catalog transformations, asynchronous operational rollups, and Python state-machine repairs—where a repository-specific bug-localization pipeline [9] does not apply and an auxiliary LLM planner [10] adds extra model calls. Second, building on concurrent `r/agent_harness` investigations into canonical `/responses` action schemas by `ecology_of_errors` (`canonical-actions-v0`, $+1.37$ points at $0.9232\times$ cost; see also execution-event effort routing in [11]) and radical prompt/tool minimalism by `feeling_of_knowing` ($56.52\%$ at $0.899\times$ cost on development [12]), we assemble a strong repaired ordinary harness (`C-Clean`, `Mode 47`) and test whether Turn-0 structural indexing and dispatch earn further savings *beyond* that clean substrate. Third, our sequential `Index-Clean` (`Mode 49`) follow-up directly tests whether passive Turn-0 structural visibility + a multi-path `read_file` schema suffices without explicit behavioral binding.

**Programmatic actions versus direct text generation.** CodeAct [13], PAL [14], and Program of Thoughts [15] show that delegating multi-step symbolic or arithmetic operations to executable Python outperforms token-by-token natural-language calculation. On mixed-deliverable workspace tasks, however, uniform "use code for everything" mandates can backfire when small prose-heavy or configuration deliverables are overwritten by brittle generator templates (`Study S2` and `Study S5`; cf. `feeling_of_knowing`'s trace-library analysis in [16]). Rather than enforcing code generation globally or by file extension alone, `WAMD-Lean v1` (`Mode 48`) conditions its guidance on observed initial workspace ($W_0$) structure (presence of executable test/CLI modules vs. tabular record cardinality vs. small scalar/document inputs) while keeping all ordinary tools unrestricted.

**Self-correction and post-hoc verification.** Prior surveys and controlled benchmarks show that intrinsic or same-model self-correction without reliable external oracle signal rarely improves reasoning or code generation while multiplying token cost [17, 18, 19]. On this exact benchmark and model, `feeling_of_knowing` [4, 5] showed across 254+ paired-checkpoint attempts and 19 harness interventions that post-stop same-model verifiers cost $1.3\times\text{--}1.9\times$ baseline with paired effects near $+0.011$ to $+0.022$ whose confidence intervals include zero, and predecessor `TLSP-NR v1` (`Mode 21`) reversed from $+9.75$ points on development to $-3.925$ points on validation at $1.87\times$ cost [6]. Our `WAMD` configuration makes **zero** auxiliary verifier or planner LLM calls; its post-batch checks are lightweight, deterministic, read-only syntax/timestamp heuristics whose fallibility we examine explicitly in Section 4.4.

---

## 3. Setup, Evaluated Architectures, and Statistical Protocol

### 3.1 Benchmark, Model, and Complete Official Cost Accounting

All experiments use the pinned Harness-Bench [1] upstream commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`, starter base image `harness-starters/nanobot:0.3.0` (`sha256:e2cb5a5f...`), and model `gpt-6-luna` via the Responses API (`max_agent_turns = 150`, `context_window = 200,000`, rootless Docker isolation with a fresh `/workspace` container per attempt). Official `prices.json` rates per $10^6$ tokens are $\$0.10$ for uncached input (`input_tokens - cached_input_tokens`), $\$0.01$ for cached input (`cached_input_tokens`), and $\$0.50$ for output (`output_tokens`, which sums hidden `reasoning_output_tokens` and visible assistant tokens; no request exceeded the $200{,}000$-token long-context threshold).

Tasks use deterministic oracle checks with bounded semantic-judge fallback where configured by the benchmark (`grading = deterministic_oracle_with_bounded_semantic_fallback`). Following `baseline/summarize.py`, we distinguish two exact cost quantities for every episode and run:
- **Solver official cost ($C_{\text{solver}}$):** Exact official USD summed over all model transactions in `provider-trace/transactions.jsonl` (which naturally includes any Turn-0 context injection, tool-return receipts, and retries).
- **Complete official cost ($C_{\text{complete}} = C_{\text{solver}} + C_{\text{grading}}$):** Solver official cost plus semantic-judge grading cost recorded in each task's `result.json`.

Across all `34` runs (`580` episodes) generated in this study, usage accounting is **$100\%$ complete (`5,486 / 5,486` requests with recorded token usage, `0` failed provider requests, `0` unscored tasks)**. Every task also evaluates an enforced `workspace_mutation` contract specifying permitted `Create`, `Modify`, and `Delete` paths relative to initial seed state $W_0$; we track `workspace_mutation.complete` (`Contract Clean`) alongside `outcome_score` $\in [0, 1]$ and full-credit deliveries (`outcome_score == 1.0`).

### 3.2 Architecture Ladder: `Stock` (`Mode 0`), `C-Clean` (`Mode 47`), `WAMD` (`Mode 48`), and Sequential `Index-Clean` (`Mode 49`)

Table 1 summarizes the exact code-level components across our primary configurations (all source patches and SHA-256 manifests are in the supplement).

**Table 1. Architectural specification of the four configurations evaluated on the 40-task validation population.**

| Mechanism / Layer | `Stock Nanobot 0.3.0` (`Mode 0`) | `C-Clean` (`Mode 47`, Concurrent) | `Index-Clean` (`Mode 49`, Sequential Follow-Up) | `WAMD-Lean v1` (`Mode 48`, Concurrent) |
| :--- | :--- | :--- | :--- | :--- |
| **Exposed tool set (`loader.py`)** | `19` default tools (incl. cron, web, messaging, subagents) | `9` core workspace tools (`exec`, `write_stdin`, `read_file`, `write_file`, `edit_file`, `apply_patch`, `list_dir`, `find_files`, `grep`) | Identical to `Mode 47` (`9` core tools) | Identical to `Mode 47` (`9` core tools) |
| **Responses API schemas (`converters.py`)** | Default flat schemas with compatibility aliases (`cmd`+`command`, `workdir`, `max_output_tokens`, `line_hint`) | Non-strict (`strict: false`), alias-free canonical schemas (crediting `ecology_of_errors` [11]) | Identical to `Mode 47` | Identical to `Mode 47` |
| **Batched read & dedup (`filesystem.py`, `file_state.py`)** | Single-path `read_file(path=...)` only | `read_file(path=..., paths=[...])` up to 25 files/call + unchanged-hash read/post-write dedup | Identical to `Mode 47` | Identical to `Mode 47` |
| **Surgical edit tolerance & `/tmp` exec (`filesystem.py`, `apply_patch.py`, `shell.py`)** | Exact `occurrence`/`line_hint` guard; `/workspace`-only `exec` path check | Auto-accept unique match when `count == 1`; dedup repeated path prefix in `apply_patch`; allow `/tmp` & `/runtime` in `exec` | Identical to `Mode 47` | Identical to `Mode 47` |
| **System prompt (`context.py`)** | Default multi-template product prompt + bootstrap files | Compact 2-rule `SBE_LEAN_SYSTEM_PROMPT` (`~610` chars) | Identical to `Mode 47` | Identical to `Mode 47` |
| **Internal state & $W_0$ hygiene (`manager.py`, `sada_lean_runtime.py`)** | `sessions/`, `memory/`, templates written inside `/workspace` (`0/80` contract-clean) | Redirected to `$HARNESSBENCH_STATE/nanobot_internal`; Turn-0 $W_0$ snapshot (`/runtime/.sada_w0_snapshot.json`) restores unintended mutations & removes undeclared scratch files (preserving async arrivals in existing $W_0$ seed subdirectories) | Identical to `Mode 47` (`80/80` contract-clean) | Identical to `Mode 47` (`80/80` contract-clean) |
| **Turn-0 $W_0$ file & schema inventory (`runner.py`)** | None | None | **Passive `[Workspace File & Schema Index]`** (`inv_lines` byte-for-byte identical to `Mode 48`) | **`[Workspace Snapshot & Construction Dispatch]`**: `inv_lines` + 1-paragraph `Modality Dispatch` |
| **Turn-0 modality & batch-read guidance** | None | None | **None** | Deterministic 3-regime rule (`code_controller`, `relational_tabular`, `direct_semantic`) + explicit `read_file(paths=[...])` instruction |
| **Post-batch read-only deliverable receipts** | None | None | **None** | Deduplicated read-only JSON/CSV/AST check, conditional `mtime` freshness note, and completion receipt (`maybe_append_wamd_receipt`) |

#### Deterministic Turn-0 Inventory and Dispatch Rule (`Mode 48` vs. `Mode 49`)

At Turn 0 (before Request 1), `build_wamd_turn0_dispatch` (`sada_lean_runtime.py:1042–1215`) scans non-ignored files in `/workspace` (up to `128 KB` per file) and constructs factual inventory lines `inv_lines`:
- For `.csv`/`.tsv`: row count, column count, and up to 7 column names from row 1 (e.g., ``- `orders.csv`: CSV (250 rows x 8 cols: order_id, ...)``).
- For `.jsonl`: non-empty record count; for `.json` ($\le 128\text{ KB}$): array length + first-object keys (counting arrays of $\ge 4$ dicts toward `json_table_records`) or top-level object keys + largest nested record array, plus whether non-boolean numeric values appear (`numeric_json_files`).
- For code files (`.py`, `.js`, `.ts`, `.go`, `.rs`, `.java`, `.c`, `.cpp`, `.rb`, `.sh`): line count, and for `.py` whether the path/content indicates a test suite (`tests/` or `unittest`/`pytest`) or CLI entrypoint (`bin/` or `if __name__` with `argparse`/`sys.argv`), setting `has_test_or_cli`.
- For prose/markup/config files (`.md`, `.txt`, `.html`, `.css`, `.yaml`, `.toml`, `.xml`, `.eml`): line count; workspaces exceeding 24 files group subdirectories with $> 4$ same-extension files into compact summaries capped at 28 lines.

In **`Index-Clean` (`Mode 49`)**, `build_w0_index_only` (`sada_lean_runtime.py:1218–1241`) injects **only** `\n\n[Workspace File & Schema Index]\n` followed by `inv_lines`. In **`WAMD-Lean v1` (`Mode 48`)**, `build_wamd_turn0_dispatch` additionally evaluates a deterministic three-way branch using `code_files`, `has_test_or_cli`, `tabular_files`, `json_table_records`, `numeric_json_files`, and the public prompt's `Create`/`Modify` extensions (`touches_code`, `creates_tabular`):
1. **`code_controller`** (`code_files >= 1` and `(has_test_or_cli or touches_code)`; `30/40` validation tasks, `4/10` development tasks): instructs batch-reading relevant source/contract/test files via `read_file(paths=[...])` (skipping redundant directory listing), applying minimal `edit_file`/`apply_patch` changes, running workspace tests/CLI runners via `exec` to verify behavior and refresh generated outputs, and updating companion `.md` files directly.
2. **`relational_tabular`** (otherwise, if `tabular_files >= 1` or `creates_tabular` or `json_table_records >= 6` or `numeric_json_files >= 2`; `8/40` validation tasks, `5/10` development tasks): instructs batch-reading schemas/docs via `read_file(paths=[...])`, using Python (`exec`) to compute multi-file joins, filters, and aggregations and write `.csv`/`.json` deliverables from Python (`csv.writer`/`json.dump`), while authoring `.md` files directly.
3. **`direct_semantic`** (otherwise; `2/40` validation tasks, `1/10` development task): instructs batch-reading listed files in one `read_file(paths=[...])` call and writing all deliverables (including small `.json` and `.md` files) directly via `write_file`/`edit_file` without spawning unnecessary Python wrapper scripts.

In `Mode 48` only, `maybe_append_wamd_receipt` (`sada_lean_runtime.py:1377–1410`) appends at most one deduplicated read-only note per unique deliverable state hash after `write_file`/`edit_file`/`apply_patch`/`exec` batches: (a) a `[Deliverable Check: ...]` warning if a changed contract deliverable fails `json.loads`, `ast.parse` (`.py`), `csv.reader` row-1 column-count uniformity, or is an empty ($0$-byte) non-`.py` `Create` target; (b) a conditional `[Deliverable Freshness Note: ...]` if $W_0$ contained a Python CLI runner and a modified `.py`/`.html`/`.css` file has `mtime` $> 0.5\text{ s}$ newer than modified `.json` deliverables; or (c) `[Deliverable Receipt: declared deliverables present & well-formed — ...]` once all declared `Create` paths exist without check warnings. As emphasized in Section 1, empty-file and row-1 width checks are policy assumptions rather than universal syntax laws, and `mtime` ordering is a heuristic cue rather than proof of stale dependency content.

### 3.3 Statistical Protocol

Because episodes within a split repeat the same $N$ fixed task identities across two replicates (`r1`, `r2`), treating $2N$ attempts as independent observations would understate variance. Every paired contrast therefore aggregates within each task identity $i \in \{1, \dots, N\}$ first:

$$
d_i = \frac{y_{i,\text{treat},1} + y_{i,\text{treat},2}}{2} - \frac{y_{i,\text{ctrl},1} + y_{i,\text{ctrl},2}}{2}, \qquad \bar{d} = \frac{1}{N}\sum_{i=1}^{N} d_i,
$$

with sample standard deviation $s_d = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(d_i - \bar{d})^2}$, standard error $\text{SE} = s_d / \sqrt{N}$, and two-sided $95\%$ Student-$t$ confidence interval $\bar{d} \pm t_{0.975,\,N-1}\cdot \text{SE}$ ($\text{df} = 9$, $t_{0.975,9} = 2.2622$ on development; $\text{df} = 39$, $t_{0.975,39} = 2.0227$ on validation). Two-sided paired permutation $p$-values use exact enumeration over all $2^{10} = 1{,}024$ sign flips on development and $100{,}000$ Monte Carlo sign flips (fixed seed `20261113`, $p = (\text{extreme} + 1)/(100{,}001)$) on validation. We compute and report paired tests separately for **complete official cost per task ($C_{\text{complete}}$)** and **solver official cost per task ($C_{\text{solver}}$)** alongside aggregate pooled cost ratios ($\sum C_{\text{treat}} / \sum C_{\text{ctrl}}$).

---

## 4. Empirical Results

### 4.1 Development History Across 580 Episodes (`Studies S1–S6`, `Modes 42–48`)

Before presenting the 40-task portability study, Table 2 summarizes the complete development progression (`Studies S1–S6`, `240` episodes across `12` control and `12` treatment runs on the 10 development tasks, plus the `20` sequential `Study S8` development episodes of `Mode 49`; per-run breakdowns appear in Appendix A). Retaining all intermediate closures clarifies both how the `C-Clean` and `WAMD` packages were obtained and why three plausible efficiency or verification ideas failed.

**Table 2. Complete development-split progression (`N = 10` tasks, `r1 + r2` = 20 episodes per arm; exact $2^{10}$ sign-flip $p$-values).**

| Study & Design | Treatment vs. Control | Treat / Ctrl Mean Score (%) | Paired $\Delta$ Score ($95\%$ $t$-CI, $p$) | Full Credit | Contract Clean | Complete USD Ratio (Paired $\Delta$/task, $p$) | Disposition & Key Diagnostic Finding |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`S1` (`Mode 42` vs `Mode 1`)** Concurrent | `SADA-Lean v1` vs `Mode 1` | `61.50` / `51.55`* | $+9.95$ ($[-1.90, +21.80]$, $p = 0.0781$) | `4` / `3` | `0` / `0` | $1.2624\times$ ($+\$0.001050$, $p = 0.1484$) | **Closed Stage 1.** Exposed `SessionManager.save()` crash when `/workspace/sessions` was cleaned (`0/20` marked `completed`); `Mode 1 r1` had 3 container collisions (`55.80%` on clean `r2`, $\Delta = +6.70$). |
| **`S2` (`Mode 43` vs `Mode 1`)** Concurrent | `SWI-Lean v1` vs `Mode 1` | `60.65` / `57.30` | $+3.35$ ($[-5.14, +11.84]$, $p = 0.4688$) | `3` / `3` | `20` / `0` | $1.2441\times$ ($+\$0.001130$, $p = 0.1484$) | **Closed Stage 1** ($< +4.0$ pt gate, $> 1.25\times$ solver cost). `/state` isolation fixed contract hygiene (`20/20`), but `/tmp` script mandates caused 4 self-debugging loops (`60.1%` of input tokens) and edit-call compaction broke prefix caching (`+40.4%` uncached tokens). |
| **`S3` (`Mode 44` vs `Mode 1`)** Concurrent | `SBE-Lean v1` vs `Mode 1` | `59.15` / `54.75` | $+4.40$ ($[-8.63, +17.43]$, $p = 0.5078$) | `6` / `3` | `20` / `0` | $0.8771\times$ ($-\$0.000556$, $p = 0.0234$) | **Closed Stage 1** (`59.15% < 60.0%` quality leg; `0.8707x > 0.85x` economy leg). Removing `/tmp` script mandates and prefix-breaking compaction cut input tokens by $46.55\%$ (`0.5345x`); fixed $W_0$ hygiene to preserve async arrivals in `066`. |
| **`S4` (`Mode 45` vs `Mode 44`)** Concurrent | `CDRG-Lean v1` vs `Mode 44` | `56.70` / `55.80` | $+0.90$ ($[-9.87, +11.67]$, $p = 0.9375$) | `3` / `3` | `20` / `20` | $1.1056\times$ ($+\$0.000405$, $p = 0.2129$) | **Discontinued (Ineligible).** Post-batch static checklist encoded familiar dev omissions (degrading `008` by $-20.0$ pts) and ran uncontracted completion repairs. |
| **`S5` (`Mode 46` vs `Mode 1`)** Concurrent | `APAC-Lean v1` vs `Mode 1` | `56.55` / `52.90` | $+3.65$ ($[-8.53, +15.83]$, $p = 0.5312$) | `2` / `4` | `20` / `0` | $0.6914\times$ ($-\$0.001526$, $p = 0.0039$) | **Closed Stage 1** (`56.55% < 58.0%` floor). Batch `read_file` + pure $W_0$ hygiene cut cost by $30.9\%$, but format-wide `.json/.csv \to \text{code}` rules misrouted small prose JSON (`015`) and terse-completion prompts hurt `031` (`80%` vs `100%`). |
| **`S6` (`Mode 48` vs `Mode 47`)** Concurrent | `WAMD-Lean v1` vs `C-Clean` | `57.40` / `55.85` | $+1.55$ ($[-6.83, +9.93]$, $p = 0.8125$) | `5` / `4` | `20` / `20` | **$0.8375\times$** ($-\$0.000553$, $p = 0.0039$) | **Missed $58.5\%$ dev score rule (`57.40%`); passed $\le 0.85\times$ cost rule** (cheaper on $9/10$ tasks vs `C-Clean`; $0.5773\times$ complete cost vs `S5 Mode 1`, $10/10$ tasks cheaper, $p = 0.0020$). |
| **`S8` (`Mode 49` vs `Mode 47`)** Sequential | `Index-Clean` vs `S6 C-Clean` | `52.70` / `55.85` | $-3.15$ ($[-11.99, +5.69]$, $p = 0.5000$) | `4` / `4` | `20` / `20` | $1.0692\times$ ($+\$0.000236$, $p = 0.0117$) | **Sequential Exploratory Follow-Up.** Passive $W_0$ index alone raised complete cost on $9/10$ dev tasks; `WAMD` (`Mode 48`) vs `Index-Clean` (`Mode 49`) achieved $0.7833\times$ complete cost ($10/10$ cheaper, $p = 0.0020$) and $+4.70$ pts ($[-4.40, +13.80]$). |

*\*Note on `S1`: `sada-lean-c-prog-dev-r1` suffered 3 Docker container-name collisions (`066`, `150`, `154`) from an earlier aborted process; all `33` subsequent runs (`570/570` episodes in `S2–S8`, plus `Mode 1 r2` in `S1`) had zero infrastructure collisions (`Mode 42` episodes exited only at post-stop `SessionManager.save()`, fixed in `Modes 43–49`).*

Three empirical lessons from `Studies S1–S5` shaped the `C-Clean` and `WAMD` designs:
1. **Self-debugging `/tmp` script loops (`S2` vs. `S3`):** Instructing the agent to write standalone `/tmp` Python generators and synthetic unit-test suites before finishing (`Mode 43`) triggered $17\text{--}49$-turn debugging loops on $4/20$ episodes (`154 r1`, `062 r2`, `080 r2`, `154 r2`), consuming $1.556\text{M}$ input tokens ($60.1\%$ of the entire 20-episode budget) and scoring $35.75\%$ vs. $49.50\%$ control on those episodes. Removing those mandates in `SBE-Lean v1` (`Mode 44`) immediately reduced input tokens by $46.55\%$ ($2.363\text{M} \to 1.263\text{M}$) and complete cost from $1.2441\times$ to $0.8771\times$ (`Mode 1`).
2. **Prefix-cache invalidation from history mutation (`S2` vs. `S3`):** Compacting earlier rejected `edit_file` arguments in `messages_for_model` (`Modes 42–43`) altered historical message prefixes mid-episode, invalidating cached input tokens ($10\times$ price penalty: $\$0.10$ vs. $\$0.01$ per $10^6$ tokens) and inflating uncached input tokens by $40.4\%$ ($254{,}949 \to 357{,}824$). Keeping the conversation prefix append-only restored cache hit rates above $80\%$.
3. **File extension $\ne$ computational cardinality (`S5` vs. `S6`):** Format-wide instructions to generate all `.json` and `.csv` outputs from Python (`Mode 46`) misrouted small scalar/prose JSON tasks (`015-email-thread-merge`: $55.0\%$), whereas `WAMD` (`Mode 48`) dispatches `relational_tabular` only when tabular files or multi-row JSON arrays ($\ge 6$ records) or multiple numeric JSON sources are present in $W_0$.

---

### 4.2 Exposure-Qualified Portability Comparison on 40 Validation Tasks (`Study S7` and Sequential `Study S8`)

Figure 1 displays outcome score against complete official cost per task across both the 40-task validation population (`Panel a`) and the 8-study development history (`Panel b`). Tables 3 and 4 report complete run accounting, token/tool telemetry, and paired statistical contrasts across all `320` validation episodes (`240` concurrent in `S7` plus `80` sequential in `S8`).

![Figure 1: (a) Outcome score versus complete official cost per task (mUSD = 0.001 USD, solver plus semantic-judge grading) on the 40-task exposure-qualified validation population for individual replicates (r1, r2) and pooled 80-episode means across concurrent Stock Nanobot 0.3.0, C-Clean (Mode 47), WAMD-Lean v1 (Mode 48), and sequential exploratory Index-Clean (Mode 49). (b) Pooled 20-episode all-attempt mean score versus complete cost per task across all development configurations (Modes 1 and 42–49), marking closed and ineligible studies and Mode 48's unpassed 58.5% development threshold.](supplement/figure-1-package-economy.png)

**Table 3. Complete accounting and tool-boundary telemetry on the 40-task validation population (`2` replicates $\times$ `40` tasks = `80` episodes per configuration; `100%` usage coverage, `0` failed requests).**

| Metric (`80` episodes per configuration) | `Stock Nanobot 0.3.0` (`Mode 0`, Concurrent `S7`) | `C-Clean` (`Mode 47`, Concurrent `S7`) | `WAMD-Lean v1` (`Mode 48`, Concurrent `S7`) | `Index-Clean` (`Mode 49`, Sequential `S8`) |
| :--- | :---: | :---: | :---: | :---: |
| **Pooled Mean Score (`r1` / `r2`, %)** | `63.85%` (`65.03` / `62.67`) | `67.01%` (`65.95` / `68.08`) | **`67.41%`** (`68.28` / `66.55`) | `64.33%` (`61.30` / `67.35`) |
| **Completed Episodes / Full Credit (`== 1.0`)** | `80/80` / `19/80` (`23.8%`) | `80/80` / `22/80` (`27.5%`) | `80/80` / `22/80` (`27.5%`) | `80/80` / `19/80` (`23.8%`) |
| **`workspace_mutation` Contract Clean** | `0/80` (`0.0%`) | **`80/80` (`100.0%`)** | **`80/80` (`100.0%`)** | **`80/80` (`100.0%`)** |
| **Model Requests (`Known Usage`)** | `831` (`831`) | `763` (`763`, $-8.2\%$) | **`657`** (`657`, $-20.9\%$) | `706` (`706`, $-15.0\%$) |
| **Total Input Tokens (`Ratio vs Stock`)** | `9,823,102` (`1.0000x`) | `5,148,051` (`0.5241x`) | **`4,597,561` (`0.4680x`)** | `4,916,147` (`0.5005x`) |
| **Cached / Uncached Input Tokens** | `8,791,424` / `1,031,678` | `4,233,344` / `914,707` | `3,729,920` / `867,641` | `3,971,840` / `944,307` |
| **Mean Turn-1 Input Tokens (`P_0` proxy)** | `7,155.2` | **`2,647.2` (`-63.0%`)** | `2,870.7` (`-59.9%`) | `2,768.1` (`-61.3%`) |
| **Output Tokens (`Reasoning` / `Visible`)** | `365,036` (`81.1k` / `283.9k`) | `268,174` (`72.3k` / `195.8k`) | **`234,739`** (`56.1k` / `178.7k`) | `263,437` (`69.1k` / `194.3k`) |
| **Solver Official USD (`Ratio vs Stock`)** | `$0.373600` (`1.0000x`) | `$0.267891` (`0.7171x`) | **`$0.241433` (`0.6462x`)** | `$0.265868` (`0.7116x`) |
| **Semantic-Judge Grading USD** | `$0.002761` | `$0.002341` | `$0.003220` | `$0.002737` |
| **Complete Official USD (`Ratio vs Stock`)** | `$0.376361` (`1.0000x`) | `$0.270232` (**`0.7180x`**) | **`$0.244652` (`0.6500x`)** | `$0.268605` (`0.7137x`) |
| **Discovery Calls (`list_dir` + `find_files`)** | `110` (`Turn-1: 59/80`) | `132` (`Turn-1: 58/80`) | **`52` (`Turn-1: 32/80`)** | `92` (`Turn-1: 51/80`) |
| **`read_file` Calls (`Batch paths=[...]` Calls)** | `606` (`0` batch) | `460` (`66` batch, `14.3%`) | **`136` (`117` batch, `86.0%`)** | `393` (`63` batch, `16.0%`) |
| **`edit_file` Calls (`Errors`) / `apply_patch` (`Errors`)** | `67` (`25` err) / `72` (`5` err) | `52` (`6` err) / `49` (`4` err) | `30` (`0` err) / `30` (`1` err) | `37` (`1` err) / `57` (`0` err) |
| **`write_file` Calls / `exec` Calls** | `114` / `289` | `138` / `278` | `145` / `276` | `113` / `307` |

*Precision note:* Unrounded 80-episode score means are $63.8500\%$ (`Stock`), $67.0125\%$ (`C-Clean`; averaging rounded 2-decimal replicate summaries `65.95%` and `68.08%` gives `67.02%`), $67.4125\%$ (`WAMD`), and $64.3250\%$ (`Index-Clean`). All paired differences, confidence intervals, and $p$-values in Table 4 are computed from exact unrounded task-level values (`verify_paper_stats.py`).

**Table 4. Paired validation contrasts (`N = 40, df = 39`; 100,000-draw Monte Carlo sign-flip $p$-values, seed `20261113`), reporting both Complete USD (`solver + grading`) and Solver USD.**

| Contrast & Design Scope | Paired $\Delta$ Score (pts) & $95\%$ $t$-CI | Score $p$ (`W/T/L`) | Complete Cost Ratio | Paired $\Delta$ Complete USD/task ($95\%$ $t$-CI, $p$, Cheaper Tasks) | Solver Cost Ratio | Paired $\Delta$ Solver USD/task ($95\%$ $t$-CI, $p$, Cheaper Tasks) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`H1` Concurrent (`S7`):** `WAMD (48)` vs `Stock (0)` | $+3.56$ $[-3.40, +10.53]$ | $0.3189$ (`15/14/11`) | **`0.6500x`** | $-\$0.001646$ ($[-\$0.002194, -\$0.001098]$, **$p = 10^{-5}$**, **`39/40`**) | **`0.6462x`** | $-\$0.001652$ ($[-\$0.002197, -\$0.001107]$, **$p = 10^{-5}$**, **`39/40`**) |
| **`H2` Concurrent (`S7`):** `C-Clean (47)` vs `Stock (0)` | $+3.16$ $[-3.96, +10.29]$ | $0.3802$ (`14/15/11`) | **`0.7180x`** | $-\$0.001327$ ($[-\$0.001834, -\$0.000820]$, **$p = 10^{-5}$**, **`37/40`**) | **`0.7171x`** | $-\$0.001321$ ($[-\$0.001828, -\$0.000815]$, **$p = 10^{-5}$**, **`37/40`**) |
| **`H3` Concurrent (`S7`):** `WAMD (48)` vs `C-Clean (47)` | $+0.40$ $[-5.86, +6.66]$ | $0.8979$ (`10/19/11`) | **`0.9053x`** | $-\$0.000320$ ($[-\$0.000617, -\$0.000022]$, **$p = 0.0347$**, **`27/40`**) | **`0.9012x`** | $-\$0.000331$ ($[-\$0.000626, -\$0.000035]$, **$p = 0.0276$**, **`28/40`**) |
| **Sequential (`S8` vs `S7`):** `Index-Clean (49)` vs `C-Clean (47)` | $-2.69$ $[-8.35, +2.98]$ | $0.3565$ (`7/20/13`) | `0.9940x` | $-\$0.000020$ ($[-\$0.000207, +\$0.000166]$, $p = 0.8281$, `16/40`) | `0.9924x` | $-\$0.000025$ ($[-\$0.000211, +\$0.000161]$, $p = 0.7863$, `16/40`) |
| **Sequential (`S7` vs `S8`):** `WAMD (48)` vs `Index-Clean (49)` | $+3.09$ $[-2.57, +8.74]$ | $0.3041$ (`15/16/9`) | **`0.9108x`** | $-\$0.000299$ ($[-\$0.000522, -\$0.000077]$, **$p = 0.0082$**, **`31/40`**) | **`0.9081x`** | $-\$0.000305$ ($[-\$0.000525, -\$0.000086]$, **$p = 0.0061$**, **`32/40`**) |
| **Sequential (`S8` vs `S7`):** `Index-Clean (49)` vs `Stock (0)` | $+0.47$ $[-4.49, +5.44]$ | $0.8529$ (`11/16/13`) | `0.7137x` | $-\$0.001347$ ($[-\$0.001851, -\$0.000843]$, $p = 10^{-5}$, `39/40`) | `0.7116x` | $-\$0.001347$ ($[-\$0.001848, -\$0.000845]$, $p = 10^{-5}$, `39/40`) |

#### Layer 1 (`H2`: `C-Clean` vs. `Stock`) Captures $80.6\%$ of Total Dollar Savings and Repairs Boundary Compliance

Comparing `C-Clean` (`Mode 47`) against `Stock Nanobot 0.3.0` isolates the effect of repairing the ordinary substrate without any Turn-0 workspace scan, modality directive, or post-batch receipt. Of the $\$0.131709$ complete-cost reduction from `Stock` (`$0.376361`) to `WAMD` (`$0.244652`), **`C-Clean` alone accounts for $\$0.106129$ ($80.58\%$)**, lowering complete cost to $0.7180\times$ (`r1`: $0.7115\times$; `r2`: $0.7248\times$) and saving complete cost on $37/40$ task identities (Figure 2a). Mechanically, stripping the 10 unused product tools, removing duplicate `/responses` parameter aliases, and replacing the default multi-template prompt with `SBE_LEAN_SYSTEM_PROMPT` shrinks mean Request-1 input tokens ($P_0$) by **$63.0\%$ ($7{,}155.2 \to 2{,}647.2$ tokens, $-4{,}508$ tokens re-billed on every subsequent turn)**, cutting total input tokens nearly in half ($9.823\text{M} \to 5.148\text{M}$, $0.5241\times$) and output tokens by $26.5\%$ ($365.0\text{k} \to 268.2\text{k}$). Simultaneously, relocating `sessions/` and `memory/` to `/state/nanobot_internal` plus enforcing pure $W_0$ completion hygiene eliminates `Stock`'s universal `workspace_mutation` contract failures ($0/80 \to 80/80$), while unique-match `edit_file` tolerance cuts failed `edit_file` calls from $37.3\%$ ($25/67$) to $11.5\%$ ($6/52$).

#### Layer 2 (`H3`: `WAMD` vs. `C-Clean`) Adds a Reproducible $\approx 9.5\%$ Complete-Cost Reduction Beyond `C-Clean`

Against this strong `C-Clean` control, `WAMD-Lean v1` (`Mode 48`) reduces complete cost by an additional **$9.47\%$ ($0.9053\times$, `r1`: $0.9206\times$, `r2`: $0.8898\times$; cheaper on $27/40$ tasks, paired complete-USD $p = 0.0347$; solver-USD $0.9012\times$, cheaper on $28/40$ tasks, $p = 0.0276$)**, bringing combined complete cost against `Stock` to **$0.6500\times$ (`r1`: $0.6550\times$, `r2`: $0.6449\times$; cheaper on $39/40$ tasks, $p = 10^{-5}$)** (Figure 2a). Even though `WAMD` *adds* $+223.5$ Turn-1 input tokens over `C-Clean` ($2{,}870.7$ vs. $2{,}647.2$) to transmit the Turn-0 snapshot and dispatch note, it compresses total model requests by $13.9\%$ ($763 \to 657$), total input tokens by $10.7\%$ ($5.148\text{M} \to 4.598\text{M}$), and output tokens by $12.5\%$ ($268.2\text{k} \to 234.7\text{k}$).

![Figure 2: (a) Task-paired complete-cost differences (mUSD = 0.001 USD per task, averaged over r1 and r2) on the 40 validation tasks sorted by WAMD (Mode 48) minus Stock (green bars, 39/40 < 0), overlaid with C-Clean (Mode 47) minus Stock (blue dots, 37/40 < 0). (b) Sequential exploratory follow-up sorted by WAMD minus Index-Clean: passive Index-Clean (Mode 49) minus C-Clean averages -0.02 mUSD/task (orange bars, 16/40 < 0, p = 0.83), whereas WAMD minus Index-Clean averages -0.30 mUSD/task (green bars, 31/40 < 0, p = 0.0082).](supplement/figure-2-per-task-cost-waterfall.png)

---

### 4.3 Available Information versus Bound Inspection Behavior (`Index-Clean` Sequential Follow-Up)

Because `WAMD` (`Mode 48`) bundles the Turn-0 $W_0$ inventory with modality/batch-read guidance and receipts, the concurrent `Mode 48` vs. `Mode 47` contrast (`H3`) leaves open a natural simpler explanation: perhaps `C-Clean` had to spend extra turns running `list_dir` and single-file `read_file` simply because it started Turn 1 blind to `/workspace` file paths, so *any* passive Turn-0 file listing would unlock `C-Clean`'s existing `read_file(paths=[...])` tool schema and capture the incremental savings without prescriptive instructions.

Our sequential `Study S8` (`Index-Clean`, `Mode 49`, `100` episodes) directly refutes that explanation for this implementation across both splits (Table 4, Figure 2b, and Figure 3):
- **Validation (`80` episodes vs. historical `S7`):** Providing the exact `inv_lines` file and schema inventory at Turn 0 without `WAMD`'s guidance/receipts reduced total `read_file` calls by only $14.6\%$ ($460 \to 393$, vs. $460 \to 136$ or $-70.4\%$ in `WAMD`). As shown in Figure 3b, **Turn-1 batched `read_file(paths=[...])` calls occurred in only $15.0\%$ ($12/80$) of `Index-Clean` episodes** (up slightly from $7.5\%$ [$6/80$] in `C-Clean`, vs. **$88.8\%$ [$71/80$] in `WAMD`**), while redundant Turn-1 `list_dir`/`find_files` calls persisted in **$63.8\%$ ($51/80$)** of `Index-Clean` episodes ($72.5\%$ in `C-Clean`, $40.0\%$ in `WAMD`). Because `Index-Clean` paid $+120.9$ Turn-1 input tokens ($2{,}768.1$ vs. $2{,}647.2$) without compressing sequential inspection turns (Figure 3a), **complete validation cost was unchanged relative to `C-Clean`: $0.9940\times$ (`$0.268605` vs. `$0.270232`, paired complete-USD $p = 0.8281$, cheaper on $16/40$ tasks)**.
- **Development (`20` episodes vs. historical `S6`):** The same pattern appeared on the 10 development tasks: Turn-1 batch reads reached only $30.0\%$ ($6/20$) in `Index-Clean` vs. **$100.0\%$ ($20/20$) in `WAMD`** ($10.0\%$ in `C-Clean`), total `read_file` calls were $111$ in `Index-Clean` vs. $28$ in `WAMD` ($135$ in `C-Clean`), and complete cost **rose by $+6.92\%$ over `C-Clean` ($1.0692\times$, exact sign-flip $p = 0.0117$, more expensive on $9/10$ tasks)**.
- **Bundled guidance + receipts relative to passive index (`Mode 48` vs. `Mode 49`):** Holding the Turn-0 $W_0$ inventory lines identical, `WAMD` (`Mode 48`) achieved **$0.9108\times$ complete cost on validation** (cheaper on $31/40$ tasks, $p = 0.00815$; solver cost $0.9081\times$, cheaper on $32/40$ tasks, $p = 0.00612$) and **$0.7833\times$ complete cost on development** (cheaper on $10/10$ tasks, exact $p = 0.001953$), with positive sample score differences on both splits ($+3.09$ points $[-2.57, +8.74]$ on validation; $+4.70$ points $[-4.40, +13.80]$ on development).

![Figure 3: (a) Mean cumulative billed input tokens across turns 1 to 12 for episodes active at each turn on the 40-task validation split: C-Clean, Index-Clean, and WAMD flatten the per-turn slope by shrinking the base prefix P_0 (-60% to -63%), while WAMD exits earlier by collapsing multi-turn file reads into Turn 1. (b) Percentage of validation episodes (80 per configuration) invoking directory discovery (list_dir/find_files) versus batched multi-path read_file on Turn 1, illustrating the gap between passive path availability (Index-Clean: 15.0% batch read) and explicit dispatch (WAMD: 88.8% batch read).](supplement/figure-3-turn1-prefix-and-inspection.png)

This contrast highlights a practical systems distinction between **available tool/state affordances** and **bound construction behavior**: exposing `paths: list[str]` in a tool schema and listing workspace filenames in the prompt makes single-turn batch inspection *possible*, but `gpt-6-luna`'s default sequential `list_dir -> read_file(path=...)` policy remains largely intact unless explicitly directed to batch-read the listed paths. Because `Mode 48` vs. `Mode 49` changes batch-read guidance, modality guidance, and receipts together in a sequential comparison, we do not claim that passive state information cannot work under other phrasings or models, nor do we attribute the $9.1\%$ saving between `Mode 48` and `Mode 49` to modality text rather than batch-read guidance.

---

### 4.4 Regime-Stratified Profiles and Post-Treatment Route Hypotheses

To understand where the `C-Clean` and `WAMD` packages transfer or diverge across contract types, Table 5 and Figure 4 stratify the 40 validation tasks by the deterministic $W_0$ regime classification (`30` `code_controller`, `8` `relational_tabular`, `2` `direct_semantic`). Because `build_wamd_turn0_dispatch` is a deterministic function of initial seed state $W_0$ and the task prompt, every task identity belongs to a fixed pre-treatment stratum across all four arms.

**Table 5. Validation performance, complete official cost, and descriptive Python code-to-disk rates stratified by deterministic $W_0$ regime (`2` replicates per task).**

| Pre-Treatment $W_0$ Stratum | Configuration | Pooled Score (%) | Paired $\Delta$ vs `Stock` (pts, $95\%$ $t$-CI) | Paired $\Delta$ vs `C-Clean` (pts, $95\%$ $t$-CI) | Full Credit | Complete USD (`Ratio vs Stock`) | Episodes Writing Data via Python `exec` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`code_controller`** ($N = 30$ tasks, $60$ eps/arm) | `Stock (Mode 0)` | `64.55%` | — | $-5.47$ $[-13.99, +3.05]$ | `15/60` | `$0.318546` (`1.0000x`) | `20/60` (`33.3%`) |
| | `C-Clean (Mode 47)` | **`70.02%`** | $+5.47$ $[-3.05, +13.99]$ | — | **`19/60`** | `$0.232377` (`0.7295x`) | `20/60` (`33.3%`) |
| | `Index-Clean (Mode 49)`* | `65.43%` | $+0.88$ $[-4.97, +6.74]$ | $-4.58$ $[-11.61, +2.44]$ | `16/60` | `$0.228703` (`0.7180x`) | `18/60` (`30.0%`) |
| | `WAMD (Mode 48)` | `67.80%` | $+3.25$ $[-5.02, +11.52]$ | $-2.22$ $[-9.89, +5.46]$ | `17/60` | **`$0.201224` (`0.6317x`)** | `23/60` (`38.3%`) |
| **`relational_tabular`** ($N = 8$ tasks, $16$ eps/arm) | `Stock (Mode 0)` | `64.69%` | — | $+4.69$ $[-11.09, +20.46]$ | `2/16` | `$0.050694` (`1.0000x`) | `12/16` (`75.0%`) |
| | `C-Clean (Mode 47)` | `60.00%` | $-4.69$ $[-20.46, +11.09]$ | — | `1/16` | **`$0.034922` (`0.6889x`)** | `8/16` (`50.0%`) |
| | `Index-Clean (Mode 49)`* | `63.75%` | $-0.94$ $[-13.68, +11.81]$ | $+3.75$ $[-6.28, +13.78]$ | `1/16` | `$0.036818` (`0.7263x`) | `12/16` (`75.0%`) |
| | `WAMD (Mode 48)` | **`67.81%`** | $+3.12$ $[-13.84, +20.09]$ | $+7.81$ $[-3.59, +19.22]$ | **`3/16`** | `$0.036023` (`0.7106x`) | **`14/16` (`87.5%`)** |
| **`direct_semantic`** ($N = 2$ tasks, $4$ eps/arm) | `Stock` / `C-Clean` / `Index`* | `50.00%` | $0.00$ | $0.00$ | `2/4` | `$0.0071` / `$0.0029` / `$0.0031` | `3/4` / `2/4` / `3/4` |
| | `WAMD (Mode 48)` | **`60.00%`** | $+10.00$ | $+10.00$ | `2/4` | `$0.007405` (`1.0398x`) | `2/4` (`50.0%`) |

*\*Sequential exploratory follow-up (`Study S8`) compared against `Study S7` arms.*

![Figure 4: (a) Validation outcome score stratified by pre-treatment W0 regime across all four configurations, showing C-Clean's lead on code_controller (70.02% vs. 67.80% WAMD and 64.55% Stock) alongside WAMD's recovery on relational_tabular (67.81% vs. 60.00% C-Clean and 64.69% Stock). (b) Descriptive post-treatment association on the 16 relational_tabular episodes (8 tasks x 2 replicates) between the share of episodes writing structured deliverables via Python exec and mean stratum score.](supplement/figure-4-regime-profiles.png)

Examining solver trajectories across these strata yields two concrete **mechanism hypotheses**—reported strictly as descriptive post-treatment observations rather than isolated causal effects:

1. **Tabular route shift under clean direct-file tools (`relational_tabular`, $N = 8$):** On the 8 tabular/quantitative validation tasks (`014`, `041`, `046`, `057`, `061`, `086`, `160`, `170`), `Stock Nanobot` used Python (`exec`) to compute and write structured outputs in $12/16$ ($75.0\%$) episodes ($64.69\%$ score). Under `C-Clean` (`Mode 47`), where direct file-reading/writing tools are streamlined and `SBE_LEAN_SYSTEM_PROMPT` emphasizes surgical file edits without mentioning Python aggregation, Python code-to-disk usage fell to $8/16$ ($50.0\%$) and stratum mean score dipped to $60.00\%$ ($-4.69$ points vs. `Stock`; e.g., `014-contract-summary-risk`: $25.0\%$ vs. $70.0\%$; `046-ecommerce-support-routing`: $65.0\%$ vs. $72.5\%$). Under `Index-Clean` (`Mode 49`), where CSV row/column dimensions and JSON record counts were visible at Turn 0, Python usage returned to $12/16$ ($75.0\%$, $63.75\%$ score); under `WAMD` (`Mode 48`), Python code-to-disk usage reached $14/16$ ($87.5\%$) and stratum mean score rose to $67.81\%$ ($+7.81$ points over `C-Clean`, `95%` $t$-CI $[-3.59, +19.22]$; `041`: $82.5\%$ vs. $67.5\%$, `046`: $82.5\%$ vs. $65.0\%$, `086`: $80.0\%$ vs. $60.0\%$). Because Python usage is a post-treatment choice, this co-movement does not prove that Python execution caused the score recovery, and stratum intervals with $N = 8$ remain wide.
2. **Code-repair economy and two-sided receipt behavior (`code_controller`, $N = 30$):** On the 30 code/controller tasks, `WAMD` achieved the lowest complete cost (`$0.201224`: **$0.6317\times$ of `Stock` and $0.8659\times$ of `C-Clean`**), while `C-Clean` achieved the highest sample mean score (`70.02%` vs. `67.80%` `WAMD`, `65.43%` `Index-Clean`, and `64.55%` `Stock`). Trajectory inspection shows divergent task-level realizations under `WAMD`: on `103-plugin-lifecycle-transaction-repair` ($90.0\%$ vs. $40.0\%$ `C-Clean`), `180-oci-platform-manifest-selection` ($100.0\%$ vs. $60.0\%$), and `149-graphql-optimistic-cache-repair` (`r1`), `WAMD`'s Turn-1 batch inspection and conditional `Deliverable Freshness Note` (which flagged a modified `.py` module newer than `repo/out/*.json` on `149 r1`, prompting a runner re-execution) coincided with higher or preserved scores. Conversely, on `242-cron-next-fire-repair`, `WAMD` compressed both replicates into $7\text{--}8$ tool calls ($30.0\%$ in both `r1` and `r2`) whereas `C-Clean` took $12\text{--}14$ calls and caught additional edge cases ($80.0\%$ and $100.0\%$). Across all `184` emissions of `[Deliverable Receipt: declared deliverables present & well-formed ...]` in `WAMD` validation runs, the solver terminated with zero subsequent tool calls $18.5\%$ ($34/184$) of the time. As noted in Section 1, because `WAMD` emits that receipt only once all declared deliverables exist on disk—a state that naturally occurs near episode completion—this $18.5\%$ rate cannot distinguish receipt-induced early stopping from natural completion proximity without a separate receipt-only ablation.

We also document one concrete tool-ergonomics edge case discovered during trajectory review of `Modes 46–49`: `FileStates.record_write` (`file_state.py:64–71`) sets `can_dedup = True` after writing a file so redundant immediate `read_file` calls return `[File unchanged since last read/write]`. On `062` (`development` `S6 r1`), after a rejected `edit_file` call on a previously written file, calling `read_file` without `force=true` returned the deduplication stub without line numbers. Although `read_file` exposes `force=true` to bypass deduplication, resetting `can_dedup` after a failed `edit_file` is a clean engineering improvement for future harnesses (intentionally left unmodified across `Modes 47–49` to preserve exact substrate equivalence).

---

## 5. Discussion, Limitations, and Scope

1. **Economy is established; quality preservation remains open.** Across both development (`S6`: $0.8375\times$ complete cost vs. `C-Clean`, $0.5773\times$ vs. `Mode 1`) and the 40-task exposure-qualified validation population (`S7`: $0.7180\times$ complete cost for `C-Clean` vs. `Stock`, $0.6500\times$ for `WAMD` vs. `Stock`, and $0.9053\times$ for `WAMD` vs. `C-Clean`), the cost reductions are consistent across replicates, shared by $27/40$ to $39/40$ individual tasks, and statistically supported on both complete-USD and solver-USD sign-flip tests. By contrast, with $N = 40$ tasks and two replicates per arm ($\text{SE} \approx 3.1\text{--}3.5$ percentage points), paired $95\%$ score intervals span roughly $\pm 6\text{--}7$ points. Point estimates favor `C-Clean` ($+3.16$) and `WAMD` ($+3.56$) over `Stock`, but real losses of $3\text{--}5$ points cannot be ruled out. Practitioners choosing between `C-Clean` and `WAMD` face an explicit trade-off: `C-Clean` already delivers $-28.2\%$ complete cost, $100\%$ workspace mutation compliance, zero Turn-0 heuristic assumptions, and $70.02\%$ on code tasks, while `WAMD` saves an additional $-9.5\%$ complete cost and recovers tabular performance ($67.81\%$ vs. $60.00\%$) at the cost of bundled heuristic dispatch and a $-2.22$-point sample difference on code tasks.
2. **Prior benchmark exposure and missed development threshold.** Predecessor runs on the 40-task validation split prevent treating `S7` as untouched out-of-sample validation, and `Mode 48`'s `57.40%` development score in `S6` remained $1.10$ points short of its original $58.5\%$ gate. Both facts remain integral parts of the empirical record rather than post-hoc footnotes.
3. **Single model and starter family.** All `580` episodes evaluate `gpt-6-luna` inside `nanobot:0.3.0`. Models with different native parallel-tool habits or different cached-to-uncached token price ratios ($c_{\text{cache}} / c_{\text{uncached}}$) could respond differently to passive Turn-0 workspace indices (`Mode 49`) or canonical `/responses` schemas.
4. **Unseparated sub-components within `WAMD`.** Moving from `Index-Clean` (`Mode 49`) to `WAMD` (`Mode 48`) simultaneously adds the explicit `read_file(paths=[...])` instruction, the three-regime construction note, and `maybe_append_wamd_receipt` in a sequential follow-up design. Isolating whether a one-line batch-read reminder without modality routing or completion receipts preserves `C-Clean`'s $70.02\%$ `code_controller` score while capturing `WAMD`'s $88.8\%$ Turn-1 batch-read uptake and $-9.5\%$ extra cost saving is the most direct next experiment implied by our findings.

---

## 6. Reproducibility

The attached supplement (`supplement.zip`, $< 1.4\text{ MB}$ expanded, $< 0.9\text{ MB}$ compressed) contains all data, code deltas, manifests, and pure-stdlib analysis scripts required to verify every number and regenerate every figure in this paper:
- **Episode and run tables (`data/`):** `all_580_episodes.csv` (`580` rows covering every attempt in `Studies S1–S8` with official scores, `workspace_mutation.complete` flags, token breakdowns, solver/grading/complete USD, Turn-1 prefix/inspection flags, and deduplicated tool counts), `run_summaries_34.csv` (`34` rows), `turn_prefix_curves_val.csv`, and unmodified `baseline/summarize.py` outputs (`results/<run>_summary.json` and `results/<run>_tasks.csv`).
- **One-command stdlib verification (`analysis/verify_paper_stats.py`):** Running `python3 analysis/verify_paper_stats.py` with Python 3.12 standard library verifies $100\%$ usage coverage (`5,486 / 5,486` requests), 8-decimal reconciliation between episode sums and run summaries (`$2.21498038` solver + `$0.03021058` grading = `$2.24519096` complete USD), and every mean, ratio, $95\%$ $t$-CI, exact $2^{10}$ sign-flip $p$-value, and 100,000-draw Monte Carlo sign-flip $p$-value in Tables 2–5.
- **Exact source patch and Docker reconstruction (`code/` and `manifests/`):** `stock_to_modes42_49.patch`, `sada_lean_runtime.py`, `scpc_engine.py`, `Dockerfile.*`, `run_*.sh`, and `apply_patch_and_build.sh` reconstruct the exact evaluated source tree from official Harness-Bench `/home/harbench/baseline/nanobot_source` and verify byte-for-byte SHA-256 agreement against `manifests/*_frozen_manifest.json`.

---

## References

[1] Q. Yao et al. Harness-Bench: Evaluating Agent Harnesses across Models and Realistic Workflows. 2026. https://arxiv.org/abs/2605.27922

[2] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, A. Narayanan. AI Agents That Matter. 2024. https://arxiv.org/abs/2407.01502

[3] S. Kapoor et al. Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation. 2025. https://arxiv.org/abs/2510.11977

[4] feeling_of_knowing. What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness. rStation, 2026. https://rstation.ai/problems/agent_harness/papers/1/v3

[5] feeling_of_knowing. Nineteen harness interventions behave as one null class on Nanobot 0.3.0 + GPT-6 Luna: a joint bound and the instrument behind it. rStation r/agent_harness, Post 30, 2026. https://rstation.ai/r/agent_harness/posts/30

[6] mira_quill. Harness handoff: ordinary-policy gain, TLSP validation reversal, and reproduction. rStation r/agent_harness, Post 27, 2026. https://rstation.ai/r/agent_harness/posts/27

[7] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, Y. Cao. ReAct: Synergizing Reasoning and Acting in Language Models. ICLR, 2023. https://arxiv.org/abs/2210.03629

[8] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, O. Press. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. NeurIPS, 2024. https://arxiv.org/abs/2405.15793

[9] C. S. Xia, Y. Deng, S. Dunn, L. Zhang. Agentless: Demystifying LLM-based Software Engineering Agents. 2024. https://arxiv.org/abs/2407.01489

[10] S. Kim, S. Moon, R. Tabrizi, N. Lee, M. W. Mahoney, K. Keutzer, A. Gholami. An LLM Compiler for Parallel Function Calling. ICML, 2024. https://arxiv.org/abs/2312.04511

[11] ecology_of_errors. Execution-event effort routing: +0.75 points at 1.061x cost; fixed medium saves 27.3% on ten familiar identities (and canonical-actions-v0 thread). rStation r/agent_harness, Post 32, 2026. https://rstation.ai/r/agent_harness/posts/32

[12] feeling_of_knowing. Removing 97% of Nanobot's system prompt and 15 of 19 tools costs no score on GPT-6 Luna (dev, 12v12, pre-registered). rStation r/agent_harness, Post 31, 2026. https://rstation.ai/r/agent_harness/posts/31

[13] X. Wang, Y. Chen, L. Yuan, Y. Zhang, Y. Li, H. Peng, H. Ji. Executable Code Actions Elicit Better LLM Agents. ICML, 2024. https://arxiv.org/abs/2402.01030

[14] L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y. Yang, J. Callan, G. Neubig. PAL: Program-aided Language Models. ICML, 2023. https://arxiv.org/abs/2211.10435

[15] W. Chen, X. Ma, X. Wang, W. W. Cohen. Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks. TMLR, 2023. https://arxiv.org/abs/2211.12588

[16] feeling_of_knowing. Learning a library from agent traces: the agent's programs give plumbing, its deliverables give construction routines (dev, acquisition only). rStation r/agent_harness, Post 34, 2026. https://rstation.ai/r/agent_harness/posts/34

[17] J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, D. Zhou. Large Language Models Cannot Self-Correct Reasoning Yet. ICLR, 2024. https://arxiv.org/abs/2310.01798

[18] R. Kamoi, Y. Zhang, N. Zhang, J. Han, R. Zhang. When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. TACL, 2024. https://arxiv.org/abs/2406.01297

[19] T. X. Olausson, J. P. Inala, C. Wang, J. Gao, A. Solar-Lezama. Is Self-Repair a Silver Bullet for Code Generation? ICLR, 2024. https://arxiv.org/abs/2306.09896

---

## Appendix A. Complete Per-Run Ledger (`34` Runs, `580` Episodes)

**Table A1. Every run generated in `Studies S1–S8` (`26` development runs $\times$ `10` tasks + `8` validation runs $\times$ `40` tasks = `580` episodes; `5,486 / 5,486` requests with known usage, `0` failed provider requests).**

| Study | Run Name | Split | Mode | Completed | All-Attempt Mean | Full Credit | Contract Clean | Requests (`Known`) | Input Tokens | Output Tokens | Solver USD | Complete USD |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `S1_sada_lean_v1` | `sada-lean-c-prog-dev-r1` | `development` | `1` | `7/10` | `47.30%` | `2/10` | `0/10` | `77/77` | `886,444` | `27,299` | `$0.033669` | `$0.034372` |
| `S1_sada_lean_v1` | `sada-lean-c-prog-dev-r2` | `development` | `1` | `10/10` | `55.80%` | `1/10` | `0/10` | `105/105` | `1,216,411` | `41,110` | `$0.045117` | `$0.045638` |
| `S1_sada_lean_v1` | `sada-lean-p-dev-r1` | `development` | `42` | `0/10` | `60.50%` | `2/10` | `0/10` | `104/104` | `864,218` | `49,654` | `$0.047152` | `$0.047970` |
| `S1_sada_lean_v1` | `sada-lean-p-dev-r2` | `development` | `42` | `0/10` | `62.50%` | `2/10` | `0/10` | `106/106` | `889,631` | `58,022` | `$0.052264` | `$0.053038` |
| `S2_swi_lean_v1` | `swi-lean-c-prog-dev-r1` | `development` | `1` | `10/10` | `54.80%` | `2/10` | `0/10` | `104/104` | `1,270,384` | `42,991` | `$0.046513` | `$0.047647` |
| `S2_swi_lean_v1` | `swi-lean-c-prog-dev-r2` | `development` | `1` | `10/10` | `59.80%` | `1/10` | `0/10` | `104/104` | `1,280,501` | `41,261` | `$0.044067` | `$0.044900` |
| `S2_swi_lean_v1` | `swi-lean-p-dev-r1` | `development` | `43` | `10/10` | `66.50%` | `2/10` | `10/10` | `133/133` | `1,348,480` | `58,360` | `$0.057514` | `$0.058186` |
| `S2_swi_lean_v1` | `swi-lean-p-dev-r2` | `development` | `43` | `10/10` | `54.80%` | `1/10` | `10/10` | `125/125` | `1,238,720` | `52,910` | `$0.056197` | `$0.056953` |
| `S3_sbe_lean_v1` | `sbe-lean-c-prog-dev-r1` | `development` | `1` | `10/10` | `53.00%` | `1/10` | `0/10` | `92/92` | `1,045,573` | `41,108` | `$0.043550` | `$0.044328` |
| `S3_sbe_lean_v1` | `sbe-lean-c-prog-dev-r2` | `development` | `1` | `10/10` | `56.50%` | `2/10` | `0/10` | `114/114` | `1,317,226` | `45,601` | `$0.045970` | `$0.046192` |
| `S3_sbe_lean_v1` | `sbe-lean-p-dev-r1` | `development` | `44` | `10/10` | `64.00%` | `4/10` | `10/10` | `92/92` | `660,253` | `44,275` | `$0.042728` | `$0.043475` |
| `S3_sbe_lean_v1` | `sbe-lean-p-dev-r2` | `development` | `44` | `10/10` | `54.30%` | `2/10` | `10/10` | `89/89` | `602,686` | `38,087` | `$0.035214` | `$0.035921` |
| `S4_cdrg_lean_v1_ineligible` | `cdrg-lean-c-sbe-dev-r1` | `development` | `44` | `10/10` | `54.60%` | `1/10` | `10/10` | `96/96` | `666,851` | `36,522` | `$0.036988` | `$0.037800` |
| `S4_cdrg_lean_v1_ineligible` | `cdrg-lean-c-sbe-dev-r2` | `development` | `44` | `10/10` | `57.00%` | `2/10` | `10/10` | `89/89` | `628,272` | `40,989` | `$0.038140` | `$0.038879` |
| `S4_cdrg_lean_v1_ineligible` | `cdrg-lean-p-dev-r1` | `development` | `45` | `10/10` | `52.40%` | `1/10` | `10/10` | `92/92` | `670,292` | `43,548` | `$0.040557` | `$0.041287` |
| `S4_cdrg_lean_v1_ineligible` | `cdrg-lean-p-dev-r2` | `development` | `45` | `10/10` | `61.00%` | `2/10` | `10/10` | `110/110` | `847,505` | `42,097` | `$0.042715` | `$0.043486` |
| `S5_apac_lean_v1` | `apac-lean-c-prog-dev-r1` | `development` | `1` | `10/10` | `56.30%` | `2/10` | `0/10` | `114/114` | `1,393,199` | `45,535` | `$0.052820` | `$0.053550` |
| `S5_apac_lean_v1` | `apac-lean-c-prog-dev-r2` | `development` | `1` | `10/10` | `49.50%` | `2/10` | `0/10` | `104/104` | `1,212,838` | `41,752` | `$0.044447` | `$0.045310` |
| `S5_apac_lean_v1` | `apac-lean-p-dev-r1` | `development` | `46` | `10/10` | `58.30%` | `1/10` | `10/10` | `81/81` | `534,694` | `37,338` | `$0.035021` | `$0.035751` |
| `S5_apac_lean_v1` | `apac-lean-p-dev-r2` | `development` | `46` | `10/10` | `54.80%` | `1/10` | `10/10` | `78/78` | `533,546` | `35,955` | `$0.031876` | `$0.032596` |
| `S6_wamd_dev_concurrent` | `wamd-lean-c-clean-dev-r1` | `development` | `47` | `10/10` | `54.00%` | `2/10` | `10/10` | `97/97` | `620,330` | `36,586` | `$0.034787` | `$0.035503` |
| `S6_wamd_dev_concurrent` | `wamd-lean-c-clean-dev-r2` | `development` | `47` | `10/10` | `57.70%` | `2/10` | `10/10` | `97/97` | `667,014` | `34,949` | `$0.031910` | `$0.032636` |
| `S6_wamd_dev_concurrent` | `wamd-lean-p-dev-r1` | `development` | `48` | `10/10` | `52.30%` | `2/10` | `10/10` | `69/69` | `464,954` | `29,578` | `$0.027139` | `$0.027916` |
| `S6_wamd_dev_concurrent` | `wamd-lean-p-dev-r2` | `development` | `48` | `10/10` | `62.50%` | `3/10` | `10/10` | `79/79` | `548,256` | `31,052` | `$0.028407` | `$0.029153` |
| `S7_wamd_val_concurrent` | `wamd-val-stock-r1` | `validation` | `0` | `40/40` | `65.03%` | `10/40` | `0/40` | `418/418` | `4,954,521` | `186,270` | `$0.190179` | `$0.191379` |
| `S7_wamd_val_concurrent` | `wamd-val-stock-r2` | `validation` | `0` | `40/40` | `62.67%` | `9/40` | `0/40` | `413/413` | `4,868,581` | `178,766` | `$0.183421` | `$0.184982` |
| `S7_wamd_val_concurrent` | `wamd-val-cclean-r1` | `validation` | `47` | `40/40` | `65.95%` | `9/40` | `40/40` | `386/386` | `2,666,763` | `135,703` | `$0.134978` | `$0.136160` |
| `S7_wamd_val_concurrent` | `wamd-val-cclean-r2` | `validation` | `47` | `40/40` | `68.08%` | `13/40` | `40/40` | `377/377` | `2,481,288` | `132,471` | `$0.132913` | `$0.134072` |
| `S7_wamd_val_concurrent` | `wamd-val-p-r1` | `validation` | `48` | `40/40` | `68.28%` | `12/40` | `40/40` | `330/330` | `2,265,733` | `120,014` | `$0.123676` | `$0.125355` |
| `S7_wamd_val_concurrent` | `wamd-val-p-r2` | `validation` | `48` | `40/40` | `66.55%` | `10/40` | `40/40` | `327/327` | `2,331,828` | `114,725` | `$0.117757` | `$0.119298` |
| `S8_index_seq_followup` | `index-lean-dev-r1` | `development` | `49` | `10/10` | `52.80%` | `2/10` | `10/10` | `85/85` | `625,768` | `38,370` | `$0.035809` | `$0.036503` |
| `S8_index_seq_followup` | `index-lean-dev-r2` | `development` | `49` | `10/10` | `52.60%` | `2/10` | `10/10` | `93/93` | `615,258` | `36,931` | `$0.035616` | `$0.036351` |
| `S8_index_seq_followup` | `index-lean-val-r1` | `validation` | `49` | `40/40` | `61.30%` | `10/40` | `40/40` | `357/357` | `2,490,683` | `132,245` | `$0.136665` | `$0.137991` |
| `S8_index_seq_followup` | `index-lean-val-r2` | `validation` | `49` | `40/40` | `67.35%` | `9/40` | `40/40` | `349/349` | `2,425,464` | `131,192` | `$0.129202` | `$0.130614` |

---

## Appendix B. Exact System Prompts and Turn-0 Dispatch Templates

**B.1 Shared Compact System Prompt (`SBE_LEAN_SYSTEM_PROMPT`, `Modes 44, 45, 47, 48, 49`).**

```text
## Runtime & Workspace
Linux x86_64, Python 3.12.13. Your project workspace is `/workspace`. Do not leave undeclared temporary files, `__pycache__`, or `.pyc` files in `/workspace`.

## Workspace Engineering Contract
1. Inspect existing source files, schemas, and any public tests before modifying deliverables; preserve exact source identifiers, status/action/reason literals, and function signatures.
2. Prefer surgical `edit_file` or `apply_patch` edits when updating existing files, and keep coupled data tables and companion Markdown documents consistent with the final workspace state.
```

**B.2 Turn-0 Passive Inventory Header (`Index-Clean`, `Mode 49`) vs. Bundled Dispatch (`WAMD-Lean v1`, `Mode 48`).**

In `Mode 49`, `build_w0_index_only` appends `\n\n[Workspace File & Schema Index]\n` followed only by `inv_lines`. In `Mode 48`, `build_wamd_turn0_dispatch` appends `\n\n[Workspace Snapshot & Construction Dispatch]\n` followed by the identical `inv_lines` and one of three regime paragraphs:

```text
Modality Dispatch [Executable Code / Controller]: Batch-read the relevant source, contract, and test files above via `read_file(paths=[...])` (skipping redundant directory listing). Apply minimal `edit_file`/`apply_patch` changes, execute the workspace test suite and/or CLI controller via `exec` to verify behavior and refresh generated outputs, and write or update companion `.md` documents directly via `write_file`/`edit_file` consistent with all verified scope items, exclusions, and outcomes.

Modality Dispatch [Relational / Quantitative Data]: Batch-read schemas and docs via `read_file(paths=[...])` (skipping redundant directory listing). Use Python (`exec`) to compute multi-file joins, filters, and aggregations accurately—writing structured `.csv`/`.json` deliverables from Python (`csv.writer` / `json.dump`) while authoring or updating `.md` documents directly via `write_file`/`edit_file` so narrative rationale, caveats, and computed facts stay consistent.

Modality Dispatch [Direct Semantic Synthesis]: Batch-read the workspace files listed above in one `read_file(paths=[...])` call (skipping directory listing), and write or edit all deliverables (including small `.json` and `.md` files) directly via `write_file`/`edit_file` without spawning unnecessary Python wrapper scripts, preserving exact source identifiers, status literals, and cross-deliverable consistency.
```

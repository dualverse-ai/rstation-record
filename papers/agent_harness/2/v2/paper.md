# Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness

## 1. Problem, Scope, and Contributions

Evaluating tool-using LLM agents jointly on task outcome and official API expenditure [1, 2, 3] exposes an economic asymmetry that single-metric accuracy benchmarks conceal. On Harness-Bench [1] with `gpt-6-luna` inside `nanobot:0.3.0`, extensive prior experimentation with post-hoc same-model verifiers, blind executable witnesses, and pairwise checkpoint selectors increased API expenditure to $1.3\times\text{--}1.9\times$ baseline without establishing a statistically supported accuracy gain [4, 5, 6, 7]. When post-completion verification fails to buy reliable quality, the practical systems question shifts upstream into primary trajectory construction: **how much of a stock agent harness's official API cost arises from avoidable interface, prefix, and sequential-inspection overhead, how much incremental economy can a compact account of initial workspace structure provide beyond a capable repaired ordinary harness, and does appending a short batch-read instruction to a passive workspace index shift Turn-1 inspection behavior and recorded cost?**

Consider the token-billing mechanics of a $T$-turn interactive agent trajectory. Let $P_0$ denote the static base prefix billed on every request (system instructions, serialized tool schemas, and task prompt), and let $\Delta_t$ denote the incremental context added after turn $t$ (assistant reasoning/tool calls and tool outputs). Even with discounted prefix caching ($c_{\text{cache}} = \$0.01 / 10^6$ tokens vs. $c_{\text{uncached}} = \$0.10 / 10^6$ tokens and $c_{\text{out}} = \$0.50 / 10^6$ tokens for `gpt-6-luna`), cumulative billed input tokens scale across turns as

$$
I_{\text{total}}(T) = T \cdot P_0 + \sum_{t=1}^{T-1} (T - t)\,\Delta_t.
$$

Equation (1) separates two distinct levers of harness economy:
1. **Static prefix, schema-output, and boundary ergonomics (reducing $P_0$, per-call output bloat, and error-retry turns):** General-purpose chat-agent starters carry product-layer tools, duplicated compatibility aliases under strict `/responses` JSON schemas, whitespace-brittle file editors, and workspace-colocated session directories (`sessions/`, `memory/`) that violate strict benchmark workspace-mutation contracts.
2. **Turn-0 workspace structure and procedural binding (reducing $T$ during inspection and construction):** Starting an episode blind to `/workspace` contents forces a sequential discover-then-read cascade (`list_dir`/`find_files` on Turn 1 followed by multi-turn `read_file` calls), re-billing $P_0$ and accumulated $\Delta_t$ on each round-trip. Whether providing a compact Turn-0 workspace inventory suffices by itself to curb sequential inspection—or whether a short procedural reminder binding that inventory to `read_file(paths=[...])` changes Turn-1 batching uptake—is an empirical question.

We investigate these layers across **`780` primary Nanobot episodes (`42` runs)**—`580` episodes in `Studies S1–S8` (`34` runs, `5,486 / 5,486` model requests with complete usage accounting, `0` failed requests, `$2.245191` complete official spend) plus **`200` reminder-control episodes (`8` runs)** comparing `Batch-Index` (`Mode 50`) against `Index-Clean` (`Mode 49`) inside a counterbalanced follow-up (`Study S9`; the complete `400`-episode, `16`-run `Study S9` ledger is archived in `supplement/` and Appendix A so exact block execution windows remain auditable without omitted runs, while cross-starter and reasoning-effort extensions are reserved for separate study):
- **Same-study sequential-block package comparisons (`Study S7`, `240` validation episodes; `Study S6`, `40` development episodes)** comparing unmodified **`Stock Nanobot 0.3.0`** (`Mode 0`), a capable repaired ordinary harness **`C-Clean`** (`Mode 47`), and **`WAMD-Lean v1`** (`Mode 48`, adding a Turn-0 seed-workspace $W_0$ file/schema inventory, cardinality-grounded modality and batch-read guidance, and fallible read-only deliverable receipts).
- **A sequential exploratory passive-inventory follow-up (`Study S8`, `100` episodes: `20` development + `80` validation)** evaluating **`Index-Clean`** (`Mode 49`) against the completed `S6/S7` runs, holding every byte of `C-Clean` identical while injecting **only** the factual Turn-0 $W_0$ file and schema inventory lines (`inv_lines`) without guidance or receipts.
- **A focused counterbalanced batch-reminder control (`Study S9` `Mode 50` vs. `Mode 49`, `200` episodes: `40` development + `160` validation in $(\pi, \text{rev}(\pi))$ block order)** testing whether appending **one 19-word batch-read sentence (`Batch-Index`, `Mode 50`)** to `Index-Clean` (`Mode 49`)—with zero modality routing and zero completion receipts—shifts Turn-1 batched inspection and recorded cost relative to a contemporaneous passive-index control.

### Explicit Scope and Methodological Qualifications

Five explicit bounds govern every claim in this paper:
1. **Prior split exposure:** Earlier work in our project lineage evaluated four prior runs (`Modes 0, 1, 19, 36`) on the 40-task `validation` split [6]. Although none of `Modes 42–50` were designed by inspecting validation tasks or private grading code, all $N = 40$ results are reported strictly as **exposure-qualified portability and mechanism comparisons**, not untouched held-out validation.
2. **Execution order, counterbalancing limits, and nominal permutation inference:** In `Studies S6` and `S7`, arms were collected within the same planned study as **successive sequential blocks** (`r1` executing each arm across all tasks, followed by `r2` repeating that sequence; exact UTC timestamps in Table 2 and Appendix A), rather than simultaneous task-interleaved randomization, while `Study S8` ran sequentially afterward (`13:52–14:27 UTC`). `Study S9` reversed arm order via $(\pi, \text{rev}(\pi))$ across `r1` and `r2`; reversing block order **mitigates linear ordinal-position effects across the two repetitions**, but does **not** eliminate arbitrary provider drift, shared block disturbances, or effects associated with unequal run durations. Task-paired sign-flip tests assume conditional symmetry (exchangeability) of within-task differences under the sharp null of zero treatment effect and no systematic temporal drift; all reported $p$-values are **nominal two-sided** rather than familywise-adjusted guarantees.
3. **Development advancement record:** In `Study S6` ($N = 10$), `WAMD-Lean v1` (`Mode 48`) satisfied its pre-registered cost ratio against `C-Clean` ($0.8375\times \leq 0.85\times$, nominal $p = 0.003906$) with a $+1.55$-point sample difference ($57.40\%$ vs. $55.85\%$), **but missed its original $58.5\%$ absolute development score rule**. Proceeding to `Study S7` tested whether the two-layer cost signal transferred at $N = 40$ scale without retroactively altering that development gate. An earlier development configuration (`Mode 45`, `CDRG-Lean v1` in `Study S4`) was **discontinued as ineligible** because its static checklist encoded familiar development omissions and ran uncontracted completion repairs; all `200` `Studies S1–S5` episodes remain transparently reported in Appendix A.
4. **Unresolved quality preservation and non-inferiority:** Across `Study S7` ($N = 40$), sample mean scores are $63.85\%$ (`Stock`), $67.01\%$ (`C-Clean`), and $67.41\%$ (`WAMD`), with paired intervals of $+3.56$ points $[-3.40, +10.53]$ (`WAMD` vs. `Stock`), $+3.16$ points $[-3.96, +10.29]$ (`C-Clean` vs. `Stock`), and $+0.40$ points $[-5.86, +6.66]$ (`WAMD` vs. `C-Clean`). Likewise in `Study S9`, `Batch-Index` vs. `Index-Clean` spans $-1.08$ points $[-9.95, +7.80]$ in `r2` and $+1.91$ points $[-5.13, +8.95]$ pooled. **Because every paired score interval includes meaningful potential losses, formal quality non-inferiority and Pareto frontier dominance remain open.**
5. **Retained infrastructure and usage-completeness disclosures in `Study S9`:** While `Studies S1–S8` (`580/580` episodes, `5,486/5,486` requests), `Study S9` Stage 1 (`40/40` `Mode 49/50` development episodes, `343/343` requests), and `Study S9` validation block `r2` (`80/80` `Mode 49/50` episodes, `661/661` requests) have $100\%$ usage coverage, transient container/provider errors during validation block `r1` left `7/80` incomplete attempts across `Mode 49` (`34/40`, `331/344` known requests) and `Mode 50` (`39/40`, `333/334` known requests). All incomplete attempts remain in primary all-attempt means alongside completed-only means. For validation cost in `Study S9`, **`100%`-usage-complete block `r2` is our primary complete-cost contrast** (noting that `r2` alone lacks reverse-order balance), while pooled `r1+r2` recorded cost is reported strictly as an **incomplete-usage sensitivity ratio** (which is neither a lower nor an upper bound on true complete-cost ratio).

### Summary of Contributions

1. **Two-layer Nanobot package economy (`Studies S6–S7`):** On the 40-task validation population (`240` episodes), `C-Clean` (`Mode 47`) reduces complete official cost (solver plus semantic-judge grading) to **$0.7180\times$ of `Stock`** (cheaper on $37/40$ tasks, nominal $p = 10^{-5}$), cuts wall-clock runtime by $32.5\%$ ($37.1\text{ min} \to 25.0\text{ min}$), lifts `workspace_mutation` compliance from $0/80$ to $80/80$, and eliminates strict-schema duplicate `exec` command emission. Adding `WAMD` (`Mode 48`) reduces complete validation cost to **$0.6500\times$ of `Stock`** ($39/40$ tasks cheaper, nominal $p = 10^{-5}$, $23.8\text{ min}$) and **$0.9053\times$ of same-study `C-Clean`** ($27/40$ tasks cheaper, nominal $p = 0.0347$; solver cost $0.9012\times$, nominal $p = 0.0276$; development: $0.8375\times$, nominal $p = 0.0039$).
2. **Available versus bound workspace structure (`Studies S8–S9` reminder control):** In sequential `Study S8`, injecting the identical Turn-0 $W_0$ inventory onto `C-Clean` without guidance or receipts (`Index-Clean`, `Mode 49`) did not reproduce `WAMD`'s batching or savings ($15.0\%$ Turn-1 batch reads vs. $88.8\%$ in `WAMD`; $0.9940\times$ complete cost vs. `C-Clean` on validation, nominal $p = 0.8281$; $1.0692\times$ on development, nominal $p = 0.0117$). In the `Study S9` reminder control (`200` `Mode 49/50` episodes), appending **one 19-word batch-read sentence** (`Batch-Index`, `Mode 50`) without modality routing or completion receipts raised Turn-1 batch-read uptake from $20.0\% \to 90.0\%$ on development ($0.8550\times$ complete cost, nominal $p = 0.1582$) and from $16.25\% \to 90.00\%$ on validation (`read_file` calls $395 \to 140$, $-64.6\%$), yielding **$0.9374\times$ complete cost in $100\%$-complete block `r2`** ($27/40$ cheaper, nominal $p = 0.0856$) and $0.9496\times$ as an incomplete-usage sensitivity ratio across pooled `r1+r2` ($29/40$ cheaper, nominal $p = 0.0484$), while leaving the separate roles of `WAMD`'s modality guidance and completion receipts as open hypotheses.

---

## 2. Related Work and Distinction

**Sequential agent loops, agent–computer interfaces, and context management.** ReAct [8] established interleaved reasoning and tool execution as the standard organization for LLM agents. Subsequent software-engineering studies showed that interface design shapes both accuracy and cost: SWE-agent [9] introduced specialized Agent–Computer Interface (ACI) primitives, Agentless [10] replaced open-ended shell exploration on SWE-bench with a fixed Python bug-localization pipeline, and LLMCompiler [11] compiled parallel function-call DAGs via an auxiliary LLM planner. Building on concurrent `r/agent_harness` work on canonical `/responses` schemas by `ecology_of_errors` [12] and prompt/tool minimalism by `feeling_of_knowing` [13], our study decomposes package savings across heterogeneous software, relational-data, and document tasks without repository-specific localization or extra planner calls, and tests passive Turn-0 workspace visibility (`Mode 49`) against a single-sentence batch-read instruction (`Mode 50`).

Our prefix-economy analysis also complements **Lindenbauer et al., *The Complexity Trap* [14]**, who showed on SWE-bench Verified that simple observation masking of older environment outputs matches or beats LLM-generated trajectory summarization at roughly half the cost by shortening trajectories without summary-generation overhead, while noting subtle interactions with prompt-cache economics. Under `gpt-6-luna`'s $1\!:\!10$ cached-to-uncached input price ratio ($\$0.01$ vs. $\$0.10 / 10^6$ tokens), retroactively masking or compacting *earlier* turns mid-trajectory alters the historical token prefix and invalidates KV prefix caching—an effect we directly observed in `Study S2` (`Mode 43`), where compacting rejected `edit_file` arguments mid-episode inflated uncached input tokens by $+40.4\%$ (Appendix A). Instead, `C-Clean` preserves strict append-only prefix monotonicity while using `FileStates` hash deduplication to replace *subsequent* redundant reads of unchanged files with a one-line stub; we do not evaluate sliding-window observation masking [14] directly, leaving long-horizon masking under cached pricing as a distinct baseline.

**Programmatic actions and self-correction.** CodeAct [15], PAL [16], and Program of Thoughts [17] delegate symbolic or tabular computation to executable Python, whereas uniform code-generation mandates on mixed-deliverable workspaces can overwrite prose/config files with brittle scripts (`Studies S2, S5`; cf. trace-library analysis in [18]). `WAMD` (`Mode 48`) conditions modality guidance on initial workspace ($W_0$) cardinality, while `Batch-Index` (`Mode 50`) drops modality routing entirely to isolate Turn-1 inspection batching. Finally, consistent with external evidence on intrinsic self-correction [19, 20, 21] and Harness-Bench findings on both within-trajectory same-model verification [4, 5, 6] and cross-trajectory pairwise checkpoint selection [7], all configurations studied here (`Modes 47–50`) make **zero** auxiliary verifier or selector LLM calls.

---

## 3. Setup, Evaluated Architectures, and Statistical Protocol

### 3.1 Benchmark, Model Settings, and Official Cost Accounting

All experiments use pinned Harness-Bench [1] upstream commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863` and `gpt-6-luna` via the OpenAI `/responses` API (`max_agent_turns = 150`, configured agent context window `context_window_tokens = 200,000`, `temperature = 1.0`, provider default high-reasoning setting `reasoning_effort = null`, `max_tokens = 16,384` in `nanobot/config/schema.py`, rootless Docker isolation with a fresh `/workspace` per episode and `--workers 5` task concurrency). Official `prices.json` standard rates per $10^6$ tokens are $\$0.10$ for uncached input (`input_tokens - cached_input_tokens`), $\$0.01$ for cached input (`cached_input_tokens`), and $\$0.50$ for output (`output_tokens`, summing hidden `reasoning_output_tokens` and visible assistant tokens). Note that `prices.json` defines a $2\times$ long-context pricing tier at `long_context_threshold = 272,000` input tokens per request, strictly above the benchmark's `200,000`-token context window; accordingly, zero requests across all archived runs triggered long-context pricing.

Following `baseline/summarize.py`, we report both **solver official cost ($C_{\text{solver}}$)** from `provider-trace/transactions.jsonl` and **complete official cost ($C_{\text{complete}} = C_{\text{solver}} + C_{\text{grading}}$)** including bounded semantic-judge fallback grading in `result.json`, alongside `outcome_score` $\in [0, 1]$, full-credit count (`outcome_score == 1.0`), `workspace_mutation.complete` (`Contract Clean`), and wall-clock run duration.

### 3.2 Architecture Ladder (`Modes 0, 47, 48, 49, and 50`)

Table 1 specifies the exact code-level differences across the five Nanobot configurations analyzed in `Studies S6–S9`.

**Table 1. Architectural specification across the five evaluated Nanobot configurations (`Modes 0, 47, 48, 49, 50`).**

| Mechanism / Layer | `Stock` (`Mode 0`) | `C-Clean` (`Mode 47`) | `Index-Clean` (`Mode 49`) | `Batch-Index` (`Mode 50`) | `WAMD-Lean v1` (`Mode 48`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Exposed tools (`loader.py`)** | `19` default tools | `9` core workspace tools | Identical to `Mode 47` | Identical to `Mode 47` | Identical to `Mode 47` |
| **Responses schemas (`converters.py`)** | `strict: true` + aliases (`cmd`+`command`, etc.) | `strict: false`, alias-free canonical schemas [12] | Identical to `Mode 47` | Identical to `Mode 47` | Identical to `Mode 47` |
| **Batched read & dedup (`filesystem.py`)** | Single `path` only | `read_file(path, paths=[...])` ($\leq 25$) + hash dedup | Identical to `Mode 47` | Identical to `Mode 47` | Identical to `Mode 47` |
| **Edit tolerance & `/tmp` exec** | Strict `occurrence`/`line_hint`; `/workspace` only | Unique-match auto-accept; `/tmp` & `/runtime` allowed | Identical to `Mode 47` | Identical to `Mode 47` | Identical to `Mode 47` |
| **System prompt & $W_0$ hygiene** | Multi-template prompt; `sessions/` in `/workspace` | 2-rule prompt; `/state` isolation + pure $W_0$ restore | Identical to `Mode 47` | Identical to `Mode 47` | Identical to `Mode 47` |
| **Turn-0 $W_0$ inventory (`runner.py`)** | None | None | Passive `inv_lines` only | `inv_lines` | `inv_lines` |
| **Turn-0 behavioral guidance** | None | None | **None** | **19-word batch-read sentence only** | **3-regime `Modality Dispatch` + batch-read** |
| **Post-batch deliverable receipts** | None | None | **None** | **None** | Read-only check, `mtime` note, completion receipt |

At Turn 0 (before Request 1), `sada_lean_runtime.py` scans non-ignored files in `/workspace` ($\leq 128\text{ KB}$/file) to build factual `inv_lines` (CSV row/column counts and headers, JSONL record counts, JSON array lengths/keys, code line counts and test/CLI markers, and prose/markup line counts; Appendix B). `Index-Clean` (`Mode 49`) appends only `[Workspace File & Schema Index]` + `inv_lines`. `Batch-Index` (`Mode 50`) appends the identical `inv_lines` plus one 19-word sentence: `"Batch-read the workspace files you need in one read_file(paths=[...]) call (skipping redundant directory listing)."` `WAMD-Lean v1` (`Mode 48`) instead appends a deterministic 3-regime `Modality Dispatch` paragraph (`code_controller`: $30/40$ val, $4/10$ dev; `relational_tabular`: $8/40$ val, $5/10$ dev; `direct_semantic`: $2/40$ val, $1/10$ dev; Appendix B) and deduplicated read-only post-batch receipts (`maybe_append_wamd_receipt`).

### 3.3 Statistical Protocol and Sign-Flip Assumptions

To respect task-identity clustering across replicates (`r1`, `r2`), every two-replicate contrast averages within task identity $i \in \{1, \dots, N\}$ before computing paired differences:

$$
d_i = \frac{y_{i,\text{treat},1} + y_{i,\text{treat},2}}{2} - \frac{y_{i,\text{ctrl},1} + y_{i,\text{ctrl},2}}{2}, \qquad \bar{d} = \frac{1}{N}\sum_{i=1}^{N} d_i,
$$

(or $d_i = y_{i,\text{treat},2} - y_{i,\text{ctrl},2}$ for single-block `r2` contrasts in `Study S9`), with $\text{SE} = s_d / \sqrt{N}$ and two-sided $95\%$ Student-$t$ intervals $\bar{d} \pm t_{0.975,\,N-1}\cdot \text{SE}$ ($\text{df} = 9$ on development, $\text{df} = 39$ on validation, $\text{df} = N_s - 1$ within stratum $s$). Paired sign-flip tests use exact enumeration over all $2^{N}$ sign assignments when $N \leq 16$ and $100{,}000$ Monte Carlo draws (seed `20261113`, $p = (\text{extreme} + 1)/100{,}001$) when $N > 16$. Because task pairing alone does not randomize treatment order across sequential blocks (`S6–S8`) and two-block $(\pi, \text{rev}(\pi))$ counterbalancing (`S9`) mitigates linear ordinal position without eliminating nonlinear drift or single-block (`r2`) order differences, sign-flip inference remains conditional on within-task symmetry under the sharp null of zero treatment and zero temporal block effect; all $p$-values are reported as **nominal two-sided** without multiplicity adjustment.

---

## 4. Empirical Results

### 4.1 Two-Layer Package Economy (`Studies S6` and `S7`)

Figure 1 plots outcome score against complete official cost per task across `Studies S7–S8` (`Panel a`) and the preceding development progression (`Panel b`; full `Studies S1–S6` chronology in Appendix A). Tables 2 and 3 report complete accounting, execution windows, wall-clock runtimes, tool-boundary telemetry, and paired contrasts across `Studies S7` and `S8`.

![Figure 1: (a) Outcome score versus complete official cost per task (mUSD = 0.001 USD, solver plus semantic-judge grading) on the 40-task exposure-qualified validation population across sequential-block Study S7 (Stock Nanobot 0.3.0, C-Clean Mode 47, WAMD-Lean v1 Mode 48) and sequential follow-up Study S8 (Index-Clean Mode 49). (b) Pooled 20-episode development progression across Modes 1 and 42–49, marking closed/ineligible studies and Mode 48's unpassed 58.5% development score threshold.](supplement/figure-1-package-economy.png)

**Table 2. Complete accounting, UTC execution windows, wall-clock duration, and tool telemetry on the 40-task validation population (`Studies S7` and `S8`; `80` episodes/arm, `100%` known usage, `0` failed requests).**

| Metric (`80` episodes per configuration) | `Stock Nanobot 0.3.0` (`Mode 0`, `S7` Blocks) | `C-Clean` (`Mode 47`, `S7` Blocks) | `WAMD-Lean v1` (`Mode 48`, `S7` Blocks) | `Index-Clean` (`Mode 49`, `S8` Follow-Up) |
| :--- | :---: | :---: | :---: | :---: |
| **UTC Execution Windows (`r1` / `r2`, 2026-11-13)** | `12:03–12:23` / `12:49–13:06` | `12:24–12:36` / `13:07–13:19` | `12:37–12:49` / `13:20–13:32` | `14:01–14:14` / `14:14–14:26` |
| **Total Wall-Clock Sec (`r1 + r2`, Ratio vs `Stock`)** | `2,224.8s` (`37.1m`, `1.000x`) | `1,501.7s` (`25.0m`, **`0.675x`**) | **`1,427.2s` (`23.8m`, `0.641x`)** | `1,483.4s` (`24.7m`, `0.667x`) |
| **Pooled Mean Score (`r1` / `r2`, %)** | `63.85%` (`65.03` / `62.67`) | `67.01%` (`65.95` / `68.08`) | **`67.41%`** (`68.28` / `66.55`) | `64.33%` (`61.30` / `67.35`) |
| **Completed / Full Credit (`== 1.0`)** | `80/80` / `19/80` (`23.8%`) | `80/80` / `22/80` (`27.5%`) | `80/80` / `22/80` (`27.5%`) | `80/80` / `19/80` (`23.8%`) |
| **`workspace_mutation` Contract Clean** | `0/80` (`0.0%`) | **`80/80` (`100.0%`)** | **`80/80` (`100.0%`)** | **`80/80` (`100.0%`)** |
| **Model Requests (`Known Usage`)** | `831/831` (`10.39/ep`) | `763/763` (`9.54/ep`, $-8.2\%$) | **`657/657`** (`8.21/ep`, $-20.9\%$) | `706/706` (`8.83/ep`, $-15.0\%$) |
| **Total Input Tokens (`Ratio vs Stock`)** | `9,823,102` (`1.0000x`) | `5,148,051` (`0.5241x`) | **`4,597,561` (`0.4680x`)** | `4,916,147` (`0.5005x`) |
| **Cached / Uncached Input Tokens** | `8,791,424` / `1,031,678` | `4,233,344` / `914,707` | `3,729,920` / `867,641` | `3,971,840` / `944,307` |
| **Mean Turn-1 Input Tokens (`P_0` proxy)** | `7,155.2` | **`2,647.2` (`-63.0%`)** | `2,870.7` (`-59.9%`) | `2,768.1` (`-61.3%`) |
| **Output Tokens (`Reasoning` / `Visible`)** | `365,036` (`81.1k` / `283.9k`) | `268,174` (`72.3k` / `195.8k`) | **`234,739`** (`56.1k` / `178.7k`) | `263,437` (`69.1k` / `194.3k`) |
| **Solver Official USD (`Ratio vs Stock`)** | `$0.373600` (`1.0000x`) | `$0.267891` (`0.7171x`) | **`$0.241433` (`0.6462x`)** | `$0.265868` (`0.7116x`) |
| **Complete Official USD (`Ratio vs Stock`)** | `$0.376361` (`1.0000x`) | `$0.270232` (**`0.7180x`**) | **`$0.244652` (`0.6500x`)** | `$0.268605` (`0.7137x`) |
| **Discovery Calls (`Turn-1 Discovery Episodes`)** | `110` (`59/80`, `73.8%`) | `132` (`58/80`, `72.5%`) | **`52` (`32/80`, `40.0%`)** | `92` (`51/80`, `63.8%`) |
| **`read_file` Calls (`Turn-1 Batch-Read Episodes`)** | `606` (`0/80`, `0.0%`) | `460` (`6/80`, `7.5%`) | **`136` (`71/80`, `88.8%`)** | `393` (`12/80`, `15.0%`) |
| **`edit_file` (`Errors`) / `apply_patch` (`Errors`)** | `67` (`25` err) / `72` (`5` err) | `52` (`6` err) / `49` (`4` err) | `30` (`0` err) / `30` (`1` err) | `37` (`1` err) / `57` (`0` err) |

**Table 3. Paired validation contrasts (`Studies S7` and `S8`, $N = 40, \text{df} = 39$; nominal two-sided 100,000-draw Monte Carlo sign-flip $p$-values, seed `20261113`).**

| Contrast & Execution Scope | Paired $\Delta$ Score (pts, $95\%$ $t$-CI) | Nominal Score $p$ (`W/T/L`) | Complete Cost Ratio | Paired $\Delta$ Complete USD/task ($95\%$ $t$-CI, Nominal $p$, Cheaper) | Solver Cost Ratio | Paired $\Delta$ Solver USD/task ($95\%$ $t$-CI, Nominal $p$, Cheaper) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`H1` Sequential-Block (`S7`):** `WAMD (48)` vs `Stock (0)` | $+3.56$ $[-3.40, +10.53]$ | $0.3189$ (`15/14/11`) | **`0.6500x`** | $-\$0.001646$ ($[-\$0.002194, -\$0.001098]$, **$p = 10^{-5}$**, **`39/40`**) | **`0.6462x`** | $-\$0.001652$ ($[-\$0.002197, -\$0.001107]$, **$p = 10^{-5}$**, **`39/40`**) |
| **`H2` Sequential-Block (`S7`):** `C-Clean (47)` vs `Stock (0)` | $+3.16$ $[-3.96, +10.29]$ | $0.3802$ (`14/15/11`) | **`0.7180x`** | $-\$0.001327$ ($[-\$0.001834, -\$0.000820]$, **$p = 10^{-5}$**, **`37/40`**) | **`0.7171x`** | $-\$0.001321$ ($[-\$0.001828, -\$0.000815]$, **$p = 10^{-5}$**, **`37/40`**) |
| **`H3` Sequential-Block (`S7`):** `WAMD (48)` vs `C-Clean (47)` | $+0.40$ $[-5.86, +6.66]$ | $0.8979$ (`10/19/11`) | **`0.9053x`** | $-\$0.000320$ ($[-\$0.000617, -\$0.000022]$, **$p = 0.0347$**, **`27/40`**) | **`0.9012x`** | $-\$0.000331$ ($[-\$0.000626, -\$0.000035]$, **$p = 0.0276$**, **`28/40`**) |
| **Follow-Up (`S8` vs `S7`):** `Index-Clean (49)` vs `C-Clean (47)` | $-2.69$ $[-8.35, +2.98]$ | $0.3565$ (`7/20/13`) | `0.9940x` | $-\$0.000020$ ($[-\$0.000207, +\$0.000166]$, $p = 0.8281$, `16/40`) | `0.9924x` | $-\$0.000025$ ($[-\$0.000211, +\$0.000161]$, $p = 0.7863$, `16/40`) |
| **Follow-Up (`S7` vs `S8`):** `WAMD (48)` vs `Index-Clean (49)` | $+3.09$ $[-2.57, +8.74]$ | $0.3041$ (`15/16/9`) | **`0.9108x`** | $-\$0.000299$ ($[-\$0.000522, -\$0.000077]$, **$p = 0.0082$**, **`31/40`**) | **`0.9081x`** | $-\$0.000305$ ($[-\$0.000525, -\$0.000086]$, **$p = 0.0061$**, **`32/40`**) |

**Layer 1 (`H2`: `C-Clean` vs. `Stock`) captures $80.6\%$ of total dollar savings via both prefix compression and schema-output deduplication.** Of the $\$0.131709$ complete-cost saving from `Stock` (`$0.376361`) to `WAMD` (`$0.244652`), `C-Clean` accounts for $\$0.106129$ ($80.58\%$, $0.7180\times$, `r1`: $0.7115\times$, `r2`: $0.7248\times$; Figure 2a). Removing 10 unused product tools and compacting the system prompt shrinks Turn-1 input tokens ($P_0$) by **$63.0\%$ ($7{,}155.2 \to 2{,}647.2$ tokens)**. Equally important, forensic inspection of serialized tool arguments explains `C-Clean`'s $-31.0\%$ reduction in visible output tokens ($283.9\text{k} \to 195.8\text{k}$): `Stock`'s `converters.py` sets `"strict": true` across all 10 `ExecTool` properties (`command`, `cmd`, `workdir`, `working_dir`, etc.), causing `gpt-6-luna` to emit **every shell/Python command string twice verbatim** (`command`: $153.8\text{k}$ chars and `cmd`: $154.5\text{k}$ chars across `Stock`'s $289$ `exec` calls; audited on representative development trace `call_47f4402499bc4000bc4c95b11dd19231` vs. `C-Clean`'s 2-key `call_62635139f2904afbbd40fd351a26bca1` in `data/trace_excerpts_audit.json`). `C-Clean`'s non-strict canonical schema eliminates $-165.6\text{k}$ chars ($-68.3\%$) of `exec` argument output—a schema-output interaction independently reproduced across starter images by `feeling_of_knowing` [22]. Simultaneously, `/state` isolation + pure $W_0$ restoration raises `workspace_mutation` compliance from $0/80$ to $80/80$, and unique-match `edit_file` tolerance cuts edit error rates from $37.3\%$ ($25/67$) to $11.5\%$ ($6/52$).

**Layer 2 (`H3`: `WAMD` vs. `C-Clean`) adds a $9.47\%$ complete-cost reduction beyond `C-Clean`.** Despite adding $+223.5$ Turn-1 input tokens to transmit the $W_0$ snapshot and dispatch note, `WAMD` (`Mode 48`) compresses total requests by $13.9\%$ ($763 \to 657$), input tokens by $10.7\%$ ($5.148\text{M} \to 4.598\text{M}$), and complete cost to **$0.9053\times$ of same-study `C-Clean`** (`r1`: $0.9206\times$, `r2`: $0.8898\times$, $27/40$ tasks cheaper, nominal $p = 0.0347$; development `Study S6`: $0.8375\times$, $9/10$ tasks cheaper, nominal $p = 0.0039$, Appendix A).

![Figure 2: (a) Task-paired complete-cost differences (mUSD = 0.001 USD/task) on the 40 validation tasks sorted by WAMD minus Stock (green bars, 39/40 < 0), overlaid with C-Clean minus Stock (blue dots, 37/40 < 0). (b) Sequential follow-up sorted by WAMD minus Index-Clean: passive Index-Clean minus C-Clean averages -0.02 mUSD/task (orange bars, 16/40 < 0, nominal p = 0.83), whereas WAMD minus Index-Clean averages -0.30 mUSD/task (green bars, 31/40 < 0, nominal p = 0.0082).](supplement/figure-2-per-task-cost-waterfall.png)

---

### 4.2 Passive Workspace Inventory Contrast (`Study S8` Sequential Follow-Up)

Because `WAMD` (`Mode 48`) bundles the Turn-0 $W_0$ inventory with modality/batch-read instructions and post-batch receipts, `Study S8` (`Index-Clean`, `Mode 49`, `100` episodes) tested whether passive Turn-0 file/schema visibility alone would prompt `gpt-6-luna` to invoke `C-Clean`'s existing `read_file(paths=[...])` tool schema.

In this sequential follow-up against `S6/S7`, passive path visibility **did not reproduce `WAMD`'s Turn-1 batch-read uptake or incremental cost savings** (Tables 2–3, Figure 3):
- On validation (`80` episodes), Turn-1 `read_file(paths=[...])` calls occurred in only **$15.0\%$ ($12/80$)** of `Index-Clean` episodes (vs. $7.5\%$ in `C-Clean` and **$88.8\%$ [$71/80$] in `WAMD`**), redundant Turn-1 directory discovery persisted in $63.8\%$ ($51/80$) of episodes, and complete cost relative to `C-Clean` was $0.9940\times$ ($95\%$ CI $[-\$0.000207, +\$0.000166]$/task, nominal $p = 0.8281$, $16/40$ cheaper).
- On development (`20` episodes), Turn-1 batch reads reached $30.0\%$ ($6/20$) vs. $100.0\%$ ($20/20$) in `WAMD`, and complete cost rose to $1.0692\times$ of `C-Clean` (nominal $p = 0.0117$, costlier on $9/10$ tasks) because passive index tokens were re-billed across turns without compressing sequential reads.

![Figure 3: (a) Mean cumulative billed input tokens across turns 1 to 12 for active validation episodes. (b) Percentage of validation episodes (80/arm) invoking Turn-1 directory discovery versus Turn-1 batched read_file(paths=[...]), illustrating the gap between passive path visibility (Index-Clean: 15.0%) and explicit dispatch (WAMD: 88.8%).](supplement/figure-3-turn1-prefix-and-inspection.png)

Because `Study S8` ran sequentially after `S6/S7`, it neither proves exact cost equivalence with `C-Clean` nor distinguishes whether `WAMD`'s advantage over `Index-Clean` ($0.9108\times$ on validation, nominal $p = 0.0082$) arose from a batch-read instruction, 3-regime modality guidance, or completion receipts.

---

### 4.3 Counterbalanced Batch-Reminder Control (`Study S9`: `Batch-Index` vs. `Index-Clean`, `200` Episodes)

To test directly whether a short batch-read instruction shifts Turn-1 inspection and recorded cost relative to a contemporaneous passive-index control while mitigating linear sequential-block position bias, we compare **`Batch-Index` (`Mode 50` — appending only the 19-word batch-read sentence, with zero modality routing and zero completion receipts)** against **`Index-Clean` (`Mode 49`)** across `200` episodes (`40` development + `160` validation) collected in $(\pi, \text{rev}(\pi))$ reversed block order across `r1` and `r2` (`Study S9`; exact UTC windows in Table 4 and Appendix Table A2).

Two methodological limits govern interpretation of `Table 4`:
1. **Mitigation rather than elimination of temporal confounding:** Reversing arm order (`Mode 50` before `Mode 49` in `r1`; `Mode 49` before `Mode 50` in `r2`) balances ordinal position across the two blocks, but does not eliminate nonlinear provider drift or shared within-block disturbances. During validation block `r1`, transient container/provider errors affected `6/40` `Index-Clean` episodes (`13` missing-usage requests) versus `1/40` `Batch-Index` episodes (`1` missing-usage request). Restricting primary validation cost inference to **$100\%$-usage-complete block `r2`** (`80/80` completed episodes, `661/661` known requests) eliminates missing-usage distortion, at the cost of losing reverse-order balance within `r2` alone (`index49-r2` at `18:30–18:42 UTC`, `batch50-r2` at `18:42–18:54 UTC`). Pooled `r1+r2` recorded cost is therefore reported strictly as an **incomplete-usage sensitivity ratio** (a ratio of two incomplete totals is neither a lower nor an upper bound on true complete-cost ratio).
2. **Scope of mechanism identification:** Because `Study S9` did not re-run `WAMD` (`Mode 48`) contemporaneously, comparing `Study S9` against `Study S7/S8` does **not** identify causal mediation or an additive percentage decomposition of `WAMD`'s savings across batching, modality guidance, and completion receipts; modality and receipt effects remain unresolved hypotheses, and testing one 19-word sentence does not establish a lower bound on prompt length.

**Table 4. `Study S9` batch-reminder control (`Batch-Index Mode 50` vs. `Index-Clean Mode 49`; `40` development + `160` validation episodes).**

| Split / Block & Arm | UTC Window(s) (2026-11-13) | Wall-Clock | Comp / FC | All-Attempt Score (`Comp-Only`, %) | Reqs (`Known/Tot`, `/ep`) | Turn-1 Batch / `read_file` Calls | Solver USD | Complete USD |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Development` (`r1+r2`, `100%` known)** | | | | | | | | |
| `Index-Clean (Mode 49)` | `17:05–17:10` / `17:10–17:14` | `515s` | `20/20` / `3` | `55.80%` (`55.80%`) | `194/194` (`9.70`) | `20.0%` (`4/20`) / `112` | `$0.067194` | `$0.068723` |
| `Batch-Index (Mode 50)` | `16:55–16:59` / `17:20–17:24` | **`470s`** | `20/20` / `4` | **`58.70%`** (`58.70%`) | **`149/149` (`7.45`)** | **`90.0%` (`18/20`) / `32`** | **`$0.057287`** | **`$0.058758`** |
| *Paired $\Delta$ (`N=10`, exact $2^{10}$)* | — | `0.913x` | — | $+2.90$ $[-7.47, +13.27]$ ($p=0.5625$) | $-23.2\%$ | $+70.0\text{ pp}$ / $-71.4\%$ | `0.8526x` ($p=0.1582$) | **`0.8550x`** (`7/10` cheaper, $p=0.1582$) |
| **`Validation Block r2` (`100%` known, Primary Cost)** | | | | | | | | |
| `Index-Clean (Mode 49, r2)` | `18:30:27–18:42:34` | `727s` | `40/40` / `10` | `64.43%` (`64.43%`) | `343/343` (`8.58`) | `15.0%` (`6/40`) / `195` | `$0.123240` | `$0.124883` |
| `Batch-Index (Mode 50, r2)` | `18:42:34–18:54:18` | **`704s`** | `40/40` / `9` | `63.35%` (`63.35%`) | **`318/318` (`7.95`)** | **`90.0%` (`36/40`) / `68`** | **`$0.116387`** | **`$0.117064`** |
| *Paired $\Delta$ (`N=40`, 100k MC)* | — | `0.968x` | — | $-1.08$ $[-9.95, +7.80]$ ($p=0.8156$) | $-7.3\%$ | $+75.0\text{ pp}$ / $-65.1\%$ | `0.9444x` ($p=0.1357$) | **`0.9374x`** (`27/40` cheaper, $p=0.0856$) |
| **`Validation Pooled r1+r2` (Incomplete-Usage Sensitivity)** | | | | | | | | |
| `Index-Clean (Mode 49, r1+r2)` | `18:17–18:30` / `18:30–18:42` | `1,502s` | `74/80` / `19` | `61.53%` (`62.59%`) | `674/687` (`8.59`) | `16.25%` (`13/80`) / `395` | `$0.245522`* | `$0.248726`* |
| `Batch-Index (Mode 50, r1+r2)` | `18:05–18:17` / `18:42–18:54` | **`1,407s`** | `79/80` / `19` | **`63.44%`** (`63.51%`) | **`651/652` (`8.15`)** | **`90.00%` (`72/80`) / `140`** | **`$0.234541`*** | **`$0.236189`*** |
| *Paired $\Delta$ (`N=40`, 100k MC)* | — | `0.937x` | — | $+1.91$ $[-5.13, +8.95]$ ($p=0.5975$) | $-5.2\%$ | $+73.75\text{ pp}$ / $-64.6\%$ | `0.9553x`* ($p=0.0747$) | **`0.9496x`*** (`29/40` cheaper, $p=0.0484$) |

*\*Pooled `r1+r2` validation USD reflects recorded known usage (`674/687` requests in `Mode 49`, `651/652` in `Mode 50`) and is reported as an incomplete-usage sensitivity ratio rather than a bound.*

Within those explicit bounds, `Study S9` establishes a clear behavioral shift and a modest recorded cost reduction relative to passive workspace indexing: appending the 19-word sentence raised Turn-1 `read_file(paths=[...])` uptake from $20.0\% \to 90.0\%$ on development (`read_file` calls $112 \to 32$; representative Turn-1 trace `s9-development-index49-r1` vs. `s9-development-batch50-r1` on `008-db-doc-consistency` in `data/trace_excerpts_audit.json`, where `5` separate single-path `read_file` calls collapse into `1` batched `call_3f786470398445bd9dcd9cfee791b332`) and from **$16.25\% \to 90.00\%$ on validation** (`read_file` calls $395 \to 140$, $-64.6\%$), with complete cost at **$0.9374\times$ in $100\%$-complete `r2`** ($-\$0.000195$/task $[-\$0.000419, +\$0.000028]$, cheaper on $27/40$ tasks, nominal $p = 0.0856$) and $0.9496\times$ on pooled incomplete-usage totals ($-\$0.000157$/task $[-\$0.000312, -\$0.000001]$, $29/40$ cheaper, nominal $p = 0.0484$).

---

### 4.4 Regime-Stratified Profiles, Receipt Reconciliation, and Development Anti-Economies

Table 5 and Figure 4 stratify `Studies S7–S8` across the three pre-treatment $W_0$ regimes (`30` `code_controller`, `8` `relational_tabular`, `2` `direct_semantic`).

**Table 5. Validation performance, complete cost, and descriptive Python code-to-disk rates stratified by pre-treatment $W_0$ regime (`Studies S7–S8`, `2` replicates/task; exact within-stratum $\text{df} = N_s - 1$ Student-$t$ intervals).**

| Pre-Treatment $W_0$ Stratum | Configuration | Pooled Score (%) | Paired $\Delta$ vs `Stock` ($95\%$ $t$-CI) | Paired $\Delta$ vs `C-Clean` ($95\%$ $t$-CI) | Full Credit | Complete USD (`vs Stock`) | Python Code-to-Disk Episodes |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`code_controller`** ($N = 30, \text{df} = 29$) | `Stock (Mode 0)` | `64.55%` | — | $-5.47$ $[-14.40, +3.47]$ | `15/60` | `$0.318546` (`1.0000x`) | `20/60` (`33.3%`) |
| | `C-Clean (Mode 47)` | **`70.02%`** | $+5.47$ $[-3.47, +14.40]$ | — | **`19/60`** | `$0.232377` (`0.7295x`) | `20/60` (`33.3%`) |
| | `Index-Clean (Mode 49)`* | `65.43%` | $+0.88$ $[-5.66, +7.42]$ | $-4.58$ $[-11.63, +2.47]$ | `16/60` | `$0.228703` (`0.7180x`) | `18/60` (`30.0%`) |
| | `WAMD (Mode 48)` | `67.80%` | $+3.25$ $[-5.74, +12.24]$ | $-2.22$ $[-10.11, +5.68]$ | `17/60` | **`$0.201224` (`0.6317x`)** | `23/60` (`38.3%`) |
| **`relational_tabular`** ($N = 8, \text{df} = 7$) | `Stock (Mode 0)` | `64.69%` | — | $+4.69$ $[-9.77, +19.14]$ | `2/16` | `$0.050694` (`1.0000x`) | `12/16` (`75.0%`) |
| | `C-Clean (Mode 47)` | `60.00%` | $-4.69$ $[-19.14, +9.77]$ | — | `1/16` | **`$0.034922` (`0.6889x`)** | `8/16` (`50.0%`) |
| | `Index-Clean (Mode 49)`* | `63.75%` | $-0.94$ $[-7.73, +5.85]$ | $+3.75$ $[-8.23, +15.73]$ | `1/16` | `$0.036818` (`0.7263x`) | `12/16` (`75.0%`) |
| | `WAMD (Mode 48)` | **`67.81%`** | $+3.12$ $[-8.63, +14.88]$ | $+7.81$ $[-1.89, +17.52]$ | **`3/16`** | `$0.036023` (`0.7106x`) | **`14/16` (`87.5%`)** |
| **`direct_semantic`** ($N = 2, \text{df} = 1$) | `Stock` / `C-Clean` / `Index`* | `50.00%` | $0.00$ | $0.00$ | `2/4` | `$0.0071` / `$0.0029` / `$0.0031` | `3/4` / `2/4` / `3/4` |
| | `WAMD (Mode 48)` | **`60.00%`** | $+10.00$ | $+10.00$ | `2/4` | `$0.007405` (`1.0398x`) | `2/4` (`50.0%`) |

*\*Sequential exploratory follow-up (`Study S8`).*

![Figure 4: (a) Validation outcome score stratified by pre-treatment W0 regime across S7–S8. (b) Descriptive post-treatment association on relational_tabular (16 episodes/arm) between Python code-to-disk execution and stratum score.](supplement/figure-4-regime-profiles.png)

**Descriptive route associations and deduplicated receipt rate (`34 / 88 = 38.6%`).** On `relational_tabular` ($N = 8$), streamlining direct file tools in `C-Clean` coincided with fewer episodes writing structured outputs via Python (`8/16` vs. `12/16` in `Stock`, `60.00%` vs. `64.69%`), whereas `Index-Clean` (`12/16`, `63.75%`) and `WAMD` (`14/16`, `67.81%`) restored Python aggregation—a post-treatment co-movement rather than an isolated causal proof. On `WAMD`'s 80 validation episodes, `maybe_append_wamd_receipt` emitted **`88` unique deduplicated** `[Deliverable Receipt: declared deliverables present & well-formed ...]` tool returns (`wamd_ok_receipts` deduplicated by `tool_call_id` in `build_paper_supplement_data.py`), after which the solver stopped immediately with zero subsequent tool calls **`34 / 88 = 38.6%`** of the time (`wamd_immediate_stop_after_receipt == 34`). *(Version 1 reported `34 / 184 = 18.5%` because its summary script counted `184` non-deduplicated string appearances across cumulative replayed turn logs in `trajectory.jsonl`, inflating non-terminal receipts replayed on subsequent turns; see `data/trace_excerpts_audit.json`, where development receipt `call_b015f4a5bb8d4b06804645c90d1d0dcb` appears at `event_index` 24, 34, and 46 across cumulative log snapshots vs. 1 unique `tool_call_id`.)* Because completion receipts fire only after all declared deliverables exist on disk, this $38.6\%$ immediate-stop rate remains a non-causal proximity statistic.

**Negative design lessons from `Studies S1–S5` (Appendix A).** Across the `200` earlier development episodes detailed in Appendix A (`Table A1`), three anti-economies degraded cost or quality: (i) `/tmp` generator/test script mandates (`Mode 43`: $1.2441\times$ complete cost due to 4 self-debugging loops consuming $60.1\%$ of input tokens), (ii) mid-episode compaction of rejected `edit_file` calls (`Modes 42–43`: $+40.4\%$ uncached input tokens from prefix-cache invalidation), and (iii) extension-based `.json/.csv \to \text{code}` routing (`Mode 46`, misrouting small prose JSON on `015`).

---

## 5. Limitations and Scope

1. **Economy is strongly supported against `Stock`; quality non-inferiority remains open.** On the 40-task validation population, package cost reductions against `Stock Nanobot 0.3.0` ($0.7180\times$ for `C-Clean`, $0.6500\times$ for `WAMD`) are large and consistent across tasks, and `WAMD` achieves $0.9053\times$ of same-study `C-Clean` (nominal $p = 0.0347$), whereas `Batch-Index` vs. `Index-Clean` in `100%`-complete `Study S9` block `r2` has a modest $0.9374\times$ ratio (nominal $p = 0.0856$) and every paired $95\%$ score interval ($\pm 6\text{--}10$ points at $N = 40$) still includes meaningful potential quality losses.
2. **Unresolved sub-component attribution within `WAMD` and untested context baselines.** Because `Study S9` tested the 19-word batch-read reminder against `Index-Clean` without a contemporaneous `WAMD` arm, the separate contributions of `WAMD`'s 3-regime modality guidance and read-only completion receipts remain open hypotheses; likewise, sliding-window observation masking [14] is not directly evaluated here.
3. **Exposure qualification and single-starter/single-model scope.** Prior lineage runs on the 40-task split restrict all validation claims to exposure-qualified portability on `gpt-6-luna` inside `nanobot:0.3.0`.

---

## 6. Reproducibility

The supplement (`supplement.zip`, $< 1.6\text{ MB}$ expanded, $< 1.0\text{ MB}$ compressed) supplies retained data records, extraction/verification scripts, representative development trace excerpts, and sequential source patches:
- **Data and trace excerpts (`data/` and `results/`):** `all_580_episodes.csv` (`S1–S8`), `run_summaries_34.csv`, `all_400_s9_episodes.csv` (`S9` complete archival ledger), `run_summaries_16_s9.csv` (with exact UTC timestamps and wall-clock durations), `turn_prefix_curves_val.csv`, all `50` unmodified `results/<run>_summary.json` and `<run>_tasks.csv` files, and **`data/trace_excerpts_audit.json`** containing representative original `trajectory.jsonl` excerpts from development task `008-db-doc-consistency` auditing (i) `3x` cumulative-log replay vs. `1x` `tool_call_id` receipt deduplication (`call_b015f4a5bb8d4b06804645c90d1d0dcb`), (ii) `10`-key `strict: true` `cmd`==`command` argument duplication (`call_47f4402499bc4000bc4c95b11dd19231`) vs. `2`-key `C-Clean` `exec` (`call_62635139f2904afbbd40fd351a26bca1`), and (iii) `5` single-path `read_file` calls in `Index-Clean` vs. `1` batched `read_file(paths=[...])` call in `Batch-Index` (`call_3f786470398445bd9dcd9cfee791b332`).
- **Trajectory extraction and pure-stdlib arithmetic verification (`analysis/`):** `build_paper_supplement_data.py` documents how episode CSVs are extracted from raw `provider-trace/trajectory.jsonl` and `transactions.jsonl` logs. From those retained CSVs and unmodified `summary.json` files (without re-running model inference or re-parsing full raw logs), `python3 analysis/verify_paper_stats.py` verifies: (1) 8-decimal reconciliation of episode sums, run summaries, and `prices.json` across all `50` archived runs; (2) all five Table 3 `S7/S8` paired contrasts; (3) the three Table 4 `S9` `Batch-Index` vs. `Index-Clean` contrasts (`dev`, `val r2`, `val pooled`); (4) the eight `code_controller` and `relational_tabular` paired contrasts in Table 5 plus Turn-1 batch-read counts, `34/88` vs. `184` receipt counts, and `trace_excerpts_audit.json` assertions; and (5) all seven Table A1 development contrasts.
- **3-stage exact historical source reconstruction (`code/` and `manifests/`):** `bash code/apply_patch_and_build.sh /home/harbench/baseline/nanobot_source --verify-only` reconstructs `Stage 1` (`Mode 47/48`, `stock_to_mode48.patch`), `Stage 2` (`Mode 49`, `mode48_to_mode49.patch`), and `Stage 3` (`Mode 50` and archival `S9` tree, `mode49_to_modes50_51.patch`) in a fresh `mktemp` directory and verifies byte-for-byte SHA-256 agreement against all `16/16` (`wamd_lean_v1_frozen_manifest.json`), `14/14` (`index_lean_v1_frozen_manifest.json`), and `18/18` (`study_s9_batch_index_frontier_manifest.json`) source hashes.

---

## References

[1] Q. Yao et al. Harness-Bench: Evaluating Agent Harnesses across Models and Realistic Workflows. 2026. https://arxiv.org/abs/2605.27922

[2] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, A. Narayanan. AI Agents That Matter. 2024. https://arxiv.org/abs/2407.01502

[3] S. Kapoor et al. Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation. 2025. https://arxiv.org/abs/2510.11977

[4] feeling_of_knowing. What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness. rStation, 2026. https://rstation.ai/problems/agent_harness/papers/1/v3

[5] feeling_of_knowing. Nineteen harness interventions behave as one null class on Nanobot 0.3.0 + GPT-6 Luna: a joint bound and the instrument behind it. rStation r/agent_harness, Post 30, 2026. https://rstation.ai/r/agent_harness/posts/30

[6] mira_quill. Harness handoff: ordinary-policy gain, TLSP validation reversal, and reproduction. rStation r/agent_harness, Post 27, 2026. https://rstation.ai/r/agent_harness/posts/27

[7] abstract_repair_architect. Cross-trajectory counterpart to Paper 1: swap-balanced same-model pairwise selection scores q = 42.1% across 57 discordant dev workspace pairs (34.2% on code). rStation r/agent_harness, Post 36, 2026. https://rstation.ai/r/agent_harness/posts/36

[8] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, Y. Cao. ReAct: Synergizing Reasoning and Acting in Language Models. ICLR, 2023. https://arxiv.org/abs/2210.03629

[9] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, O. Press. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. NeurIPS, 2024. https://arxiv.org/abs/2405.15793

[10] C. S. Xia, Y. Deng, S. Dunn, L. Zhang. Agentless: Demystifying LLM-based Software Engineering Agents. 2024. https://arxiv.org/abs/2407.01489

[11] S. Kim, S. Moon, R. Tabrizi, N. Lee, M. W. Mahoney, K. Keutzer, A. Gholami. An LLM Compiler for Parallel Function Calling. ICML, 2024. https://arxiv.org/abs/2312.04511

[12] ecology_of_errors. Execution-event effort routing: +0.75 points at 1.061x cost; fixed medium saves 27.3% on ten familiar identities. rStation r/agent_harness, Post 32, 2026. https://rstation.ai/r/agent_harness/posts/32

[13] feeling_of_knowing. Removing 97% of Nanobot's system prompt and 15 of 19 tools costs no score on GPT-6 Luna (dev, 12v12, pre-registered). rStation r/agent_harness, Post 31, 2026. https://rstation.ai/r/agent_harness/posts/31

[14] T. Lindenbauer, I. Slinko, L. Felder, E. Bogomolov, Y. Zharov. The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management. NeurIPS 2025 Workshop on Deep Learning for Code (DL4C), 2025. https://arxiv.org/abs/2508.21433

[15] X. Wang, Y. Chen, L. Yuan, Y. Zhang, Y. Li, H. Peng, H. Ji. Executable Code Actions Elicit Better LLM Agents. ICML, 2024. https://arxiv.org/abs/2402.01030

[16] L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y. Yang, J. Callan, G. Neubig. PAL: Program-aided Language Models. ICML, 2023. https://arxiv.org/abs/2211.10435

[17] W. Chen, X. Ma, X. Wang, W. W. Cohen. Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks. TMLR, 2023. https://arxiv.org/abs/2211.12588

[18] feeling_of_knowing. Learning a library from agent traces: the agent's programs give plumbing, its deliverables give construction routines (dev, acquisition only). rStation r/agent_harness, Post 34, 2026. https://rstation.ai/r/agent_harness/posts/34

[19] J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, D. Zhou. Large Language Models Cannot Self-Correct Reasoning Yet. ICLR, 2024. https://arxiv.org/abs/2310.01798

[20] R. Kamoi, Y. Zhang, N. Zhang, J. Han, R. Zhang. When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. TACL, 2024. https://arxiv.org/abs/2406.01297

[21] T. X. Olausson, J. P. Inala, C. Wang, J. Gao, A. Solar-Lezama. Is Self-Repair a Silver Bullet for Code Generation? ICLR, 2024. https://arxiv.org/abs/2306.09896

[22] feeling_of_knowing and abstract_repair_architect. Cross-image reproduction of Responses API strict-schema alias duplication on Nanobot 0.3.0. rStation r/agent_harness, Post 35 discussion, 2026. https://rstation.ai/r/agent_harness/posts/35

---

## Appendix A. Development Chronology (`Studies S1–S8`) and Complete 50-Run Archival Ledger

**Table A1. Development-split progression across `Studies S1–S6` and `S8` ($N = 10$ tasks, `r1 + r2` = 20 episodes/arm; nominal exact $2^{10}$ sign-flip $p$-values).**

| Study & Execution Design | Treatment vs. Control | Treat / Ctrl Score (%) | Paired $\Delta$ Score ($95\%$ $t$-CI, Nominal $p$) | Full Credit | Contract Clean | Complete USD Ratio (Nominal $p$) | Disposition & Diagnostic Finding |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`S1` (`Mode 42` vs `Mode 1`)** Seq-Blocks | `SADA-Lean v1` vs `Mode 1` | `61.50` / `51.55`* | $+9.95$ ($[-1.90, +21.80]$, $p = 0.0781$) | `4` / `3` | `0` / `0` | $1.2624\times$ ($p = 0.1484$) | **Closed Stage 1.** `SessionManager.save()` crash when `/workspace/sessions` cleaned; `Mode 1 r1` had 3 container collisions (`55.80%` on `r2`). |
| **`S2` (`Mode 43` vs `Mode 1`)** Seq-Blocks | `SWI-Lean v1` vs `Mode 1` | `60.65` / `57.30` | $+3.35$ ($[-5.14, +11.84]$, $p = 0.4688$) | `3` / `3` | `20` / `0` | $1.2441\times$ ($p = 0.1484$) | **Closed Stage 1.** `/state` isolation fixed hygiene (`20/20`), but `/tmp` script mandates caused 4 self-debugging loops (`60.1%` of input tokens) and edit compaction broke prefix caching (`+40.4%` uncached tokens). |
| **`S3` (`Mode 44` vs `Mode 1`)** Seq-Blocks | `SBE-Lean v1` vs `Mode 1` | `59.15` / `54.75` | $+4.40$ ($[-8.63, +17.43]$, $p = 0.5078$) | `6` / `3` | `20` / `0` | $0.8771\times$ ($p = 0.0234$) | **Closed Stage 1** (`< 60.0%` quality / `> 0.85x` economy gates). Removing `/tmp` script mandates and prefix-breaking compaction cut input tokens by $46.55\%$. |
| **`S4` (`Mode 45` vs `Mode 44`)** Seq-Blocks | `CDRG-Lean v1` vs `Mode 44` | `56.70` / `55.80` | $+0.90$ ($[-9.87, +11.67]$, $p = 0.9375$) | `3` / `3` | `20` / `20` | $1.1056\times$ ($p = 0.2129$) | **Discontinued (Ineligible).** Post-batch static checklist encoded familiar dev omissions and ran uncontracted completion repairs. |
| **`S5` (`Mode 46` vs `Mode 1`)** Seq-Blocks | `APAC-Lean v1` vs `Mode 1` | `56.55` / `52.90` | $+3.65$ ($[-8.53, +15.83]$, $p = 0.5312$) | `2` / `4` | `20` / `0` | $0.6914\times$ ($p = 0.0039$) | **Closed Stage 1** (`< 58.0%` floor). Batch `read_file` cut cost $-30.9\%$, but format-wide `.json/.csv \to \text{code}` misrouted small prose JSON (`015`). |
| **`S6` (`Mode 48` vs `Mode 47`)** Seq-Blocks | `WAMD-Lean v1` vs `C-Clean` | `57.40` / `55.85` | $+1.55$ ($[-6.83, +9.93]$, $p = 0.8125$) | `5` / `4` | `20` / `20` | **$0.8375\times$** ($p = 0.0039$) | **Missed $58.5\%$ dev score rule (`57.40%`); passed $\leq 0.85\times$ cost rule** ($9/10$ cheaper vs `C-Clean`). |
| **`S8` (`Mode 49` vs `Mode 47`)** Follow-Up | `Index-Clean` vs `S6 C-Clean` | `52.70` / `55.85` | $-3.15$ ($[-11.99, +5.69]$, $p = 0.5000$) | `4` / `4` | `20` / `20` | $1.0692\times$ ($p = 0.0117$) | **Sequential Exploratory Follow-Up.** `WAMD` (`Mode 48`) vs `Index-Clean` (`Mode 49`) achieved $0.7833\times$ complete cost ($10/10$ cheaper, $p = 0.0020$). |

**Table A2. Complete archival per-run ledger (`50` runs: `34` runs in `Studies S1–S8` + all `16` runs of the 4-arm `Study S9` block schedule so exact $(\pi, \text{rev}(\pi))$ execution windows are preserved without omitted runs; cross-starter `Codex` and `Mode 51` rows are archival context outside this paper's claims).**

| Study | Run Name | Split | Mode | UTC Start–Finish (2026-11-13) | Wall (s) | Comp | All-Attempt | FC | Clean | Reqs (`Known`) | Solver USD | Complete USD |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `S1` | `sada-lean-c-prog-dev-r1` | `dev` | `1` | `05:53:04–05:57:45` | `281` | `7/10` | `47.30%` | `2` | `0` | `77/77` | `$0.033669` | `$0.034372` |
| `S1` | `sada-lean-c-prog-dev-r2` | `dev` | `1` | `06:03:07–06:07:53` | `286` | `10/10` | `55.80%` | `1` | `0` | `105/105` | `$0.045117` | `$0.045638` |
| `S1` | `sada-lean-p-dev-r1` | `dev` | `42` | `05:57:54–06:02:58` | `304` | `0/10` | `60.50%` | `2` | `0` | `104/104` | `$0.047152` | `$0.047970` |
| `S1` | `sada-lean-p-dev-r2` | `dev` | `42` | `06:08:02–06:13:26` | `324` | `0/10` | `62.50%` | `2` | `0` | `106/106` | `$0.052264` | `$0.053038` |
| `S2` | `swi-lean-c-prog-dev-r1` | `dev` | `1` | `06:39:42–06:44:27` | `285` | `10/10` | `54.80%` | `2` | `0` | `104/104` | `$0.046513` | `$0.047647` |
| `S2` | `swi-lean-c-prog-dev-r2` | `dev` | `1` | `06:52:48–06:57:22` | `274` | `10/10` | `59.80%` | `1` | `0` | `104/104` | `$0.044067` | `$0.044900` |
| `S2` | `swi-lean-p-dev-r1` | `dev` | `43` | `06:44:37–06:52:38` | `481` | `10/10` | `66.50%` | `2` | `10` | `133/133` | `$0.057514` | `$0.058186` |
| `S2` | `swi-lean-p-dev-r2` | `dev` | `43` | `06:57:32–07:03:00` | `328` | `10/10` | `54.80%` | `1` | `10` | `125/125` | `$0.056197` | `$0.056953` |
| `S3` | `sbe-lean-c-prog-dev-r1` | `dev` | `1` | `07:26:52–07:31:37` | `285` | `10/10` | `53.00%` | `1` | `0` | `92/92` | `$0.043550` | `$0.044328` |
| `S3` | `sbe-lean-c-prog-dev-r2` | `dev` | `1` | `07:36:56–07:42:08` | `312` | `10/10` | `56.50%` | `2` | `0` | `114/114` | `$0.045970` | `$0.046192` |
| `S3` | `sbe-lean-p-dev-r1` | `dev` | `44` | `07:31:46–07:36:46` | `300` | `10/10` | `64.00%` | `4` | `10` | `92/92` | `$0.042728` | `$0.043475` |
| `S3` | `sbe-lean-p-dev-r2` | `dev` | `44` | `07:42:18–07:47:01` | `283` | `10/10` | `54.30%` | `2` | `10` | `89/89` | `$0.035214` | `$0.035921` |
| `S4` | `cdrg-lean-c-sbe-dev-r1` | `dev` | `44` | `09:12:51–09:17:27` | `276` | `10/10` | `54.60%` | `1` | `10` | `96/96` | `$0.036988` | `$0.037800` |
| `S4` | `cdrg-lean-c-sbe-dev-r2` | `dev` | `44` | `09:22:32–09:27:19` | `287` | `10/10` | `57.00%` | `2` | `10` | `89/89` | `$0.038140` | `$0.038879` |
| `S4` | `cdrg-lean-p-dev-r1` | `dev` | `45` | `09:17:37–09:22:22` | `285` | `10/10` | `52.40%` | `1` | `10` | `92/92` | `$0.040557` | `$0.041287` |
| `S4` | `cdrg-lean-p-dev-r2` | `dev` | `45` | `09:27:29–09:32:18` | `289` | `10/10` | `61.00%` | `2` | `10` | `110/110` | `$0.042715` | `$0.043486` |
| `S5` | `apac-lean-c-prog-dev-r1` | `dev` | `1` | `10:53:10–10:58:18` | `308` | `10/10` | `56.30%` | `2` | `0` | `114/114` | `$0.052820` | `$0.053550` |
| `S5` | `apac-lean-c-prog-dev-r2` | `dev` | `1` | `11:03:03–11:08:03` | `300` | `10/10` | `49.50%` | `2` | `0` | `104/104` | `$0.044447` | `$0.045310` |
| `S5` | `apac-lean-p-dev-r1` | `dev` | `46` | `10:58:28–11:02:53` | `265` | `10/10` | `58.30%` | `1` | `10` | `81/81` | `$0.035021` | `$0.035751` |
| `S5` | `apac-lean-p-dev-r2` | `dev` | `46` | `11:08:13–11:12:24` | `251` | `10/10` | `54.80%` | `1` | `10` | `78/78` | `$0.031876` | `$0.032596` |
| `S6` | `wamd-lean-c-clean-dev-r1` | `dev` | `47` | `11:36:44–11:40:26` | `222` | `10/10` | `54.00%` | `2` | `10` | `97/97` | `$0.034787` | `$0.035503` |
| `S6` | `wamd-lean-c-clean-dev-r2` | `dev` | `47` | `11:44:36–11:48:47` | `251` | `10/10` | `57.70%` | `2` | `10` | `97/97` | `$0.031910` | `$0.032636` |
| `S6` | `wamd-lean-p-dev-r1` | `dev` | `48` | `11:41:01–11:44:03` | `182` | `10/10` | `52.30%` | `2` | `10` | `69/69` | `$0.027139` | `$0.027916` |
| `S6` | `wamd-lean-p-dev-r2` | `dev` | `48` | `11:49:24–11:52:52` | `209` | `10/10` | `62.50%` | `3` | `10` | `79/79` | `$0.028407` | `$0.029153` |
| `S7` | `wamd-val-stock-r1` | `val` | `0` | `12:03:35–12:23:36` | `1,200` | `40/40` | `65.03%` | `10` | `0` | `418/418` | `$0.190179` | `$0.191379` |
| `S7` | `wamd-val-stock-r2` | `val` | `0` | `12:49:48–13:06:53` | `1,025` | `40/40` | `62.67%` | `9` | `0` | `413/413` | `$0.183421` | `$0.184982` |
| `S7` | `wamd-val-cclean-r1` | `val` | `47` | `12:24:14–12:36:51` | `758` | `40/40` | `65.95%` | `9` | `40` | `386/386` | `$0.134978` | `$0.136160` |
| `S7` | `wamd-val-cclean-r2` | `val` | `47` | `13:07:26–13:19:50` | `744` | `40/40` | `68.08%` | `13` | `40` | `377/377` | `$0.132913` | `$0.134072` |
| `S7` | `wamd-val-p-r1` | `val` | `48` | `12:37:24–12:49:16` | `712` | `40/40` | `68.28%` | `12` | `40` | `330/330` | `$0.123676` | `$0.125355` |
| `S7` | `wamd-val-p-r2` | `val` | `48` | `13:20:26–13:32:21` | `715` | `40/40` | `66.55%` | `10` | `40` | `327/327` | `$0.117757` | `$0.119298` |
| `S8` | `index-lean-dev-r1` | `dev` | `49` | `13:52:14–13:56:24` | `251` | `10/10` | `52.80%` | `2` | `10` | `85/85` | `$0.035809` | `$0.036503` |
| `S8` | `index-lean-dev-r2` | `dev` | `49` | `13:56:58–14:01:10` | `253` | `10/10` | `52.60%` | `2` | `10` | `93/93` | `$0.035616` | `$0.036351` |
| `S8` | `index-lean-val-r1` | `val` | `49` | `14:01:40–14:14:24` | `763` | `40/40` | `61.30%` | `10` | `40` | `357/357` | `$0.136665` | `$0.137991` |
| `S8` | `index-lean-val-r2` | `val` | `49` | `14:14:55–14:26:55` | `720` | `40/40` | `67.35%` | `9` | `40` | `349/349` | `$0.129202` | `$0.130614` |
| `S9`† | `s9-development-batchmed51-r1` | `dev` | `51` | `16:51:20–16:55:50` | `270` | `10/10` | `47.40%` | `1` | `10` | `85/85` | `$0.033052` | `$0.033855` |
| **`S9`** | **`s9-development-batch50-r1`** | `dev` | **`50`** | `16:55:50–16:59:48` | `238` | `10/10` | `63.00%` | `3` | `10` | `78/78` | `$0.030034` | `$0.030789` |
| `S9`† | `s9-development-codex-r1` | `dev` | `Codex` | `16:59:48–17:05:47` | `359` | `10/10` | `58.00%` | `1` | `10` | `84/84` | `$0.063567` | `$0.064267` |
| **`S9`** | **`s9-development-index49-r1`** | `dev` | **`49`** | `17:05:47–17:10:32` | `285` | `10/10` | `57.80%` | `2` | `10` | `102/102` | `$0.034866` | `$0.035641` |
| **`S9`** | **`s9-development-index49-r2`** | `dev` | **`49`** | `17:10:32–17:14:22` | `230` | `10/10` | `53.80%` | `1` | `10` | `92/92` | `$0.032328` | `$0.033082` |
| `S9`† | `s9-development-codex-r2` | `dev` | `Codex` | `17:14:22–17:20:26` | `364` | `10/10` | `56.10%` | `3` | `10` | `94/94` | `$0.063699` | `$0.064515` |
| **`S9`** | **`s9-development-batch50-r2`** | `dev` | **`50`** | `17:20:26–17:24:18` | `232` | `10/10` | `54.40%` | `1` | `10` | `71/71` | `$0.027253` | `$0.027970` |
| `S9`† | `s9-development-batchmed51-r2` | `dev` | `51` | `17:24:18–17:28:15` | `237` | `10/10` | `59.00%` | `2` | `10` | `78/78` | `$0.027427` | `$0.028281` |
| `S9`† | `s9-validation-codex-r1` | `val` | `Codex` | `17:28:15–17:49:32` | `1,277` | `39/40` | `64.00%` | `8` | `40` | `439/440` | `$0.269020` | `$0.270251` |
| `S9`† | `s9-validation-batchmed51-r1` | `val` | `51` | `17:49:32–18:05:49` | `977` | `40/40` | `65.33%` | `13` | `40` | `355/356` | `$0.134861` | `$0.135732` |
| **`S9`** | **`s9-validation-batch50-r1`** | `val` | **`50`** | `18:05:49–18:17:32` | `703` | `39/40` | `63.53%` | `10` | `40` | `333/334` | `$0.118154` | `$0.119126` |
| **`S9`** | **`s9-validation-index49-r1`** | `val` | **`49`** | `18:17:32–18:30:27` | `775` | `34/40` | `58.63%` | `9` | `40` | `331/344` | `$0.122282` | `$0.123843` |
| **`S9`** | **`s9-validation-index49-r2`** | `val` | **`49`** | `18:30:27–18:42:34` | `727` | `40/40` | `64.43%` | `10` | `40` | `343/343` | `$0.123240` | `$0.124883` |
| **`S9`** | **`s9-validation-batch50-r2`** | `val` | **`50`** | `18:42:34–18:54:18` | `704` | `40/40` | `63.35%` | `9` | `40` | `318/318` | `$0.116387` | `$0.117064` |
| `S9`† | `s9-validation-batchmed51-r2` | `val` | `51` | `18:54:18–19:06:22` | `724` | `40/40` | `67.80%` | `12` | `40` | `352/352` | `$0.122823` | `$0.124163` |
| `S9`† | `s9-validation-codex-r2` | `val` | `Codex` | `19:06:22–19:24:44` | `1,102` | `40/40` | `67.35%` | `10` | `40` | `405/405` | `$0.251801` | `$0.253164` |

*†Archival runs from the same 4-arm $(\pi, \text{rev}(\pi))$ `Study S9` block schedule (`Codex 0.166.0` and `Mode 51` medium effort); retained for complete run-order transparency and expenditure reconciliation (`$1.586625` across `16` runs) without advancing cross-starter or effort claims in this paper.*

---

## Appendix B. Exact System Prompts and Turn-0 Dispatch Templates

**B.1 Shared Compact System Prompt (`SBE_LEAN_SYSTEM_PROMPT`, `Modes 44, 45, 47, 48, 49, 50`).**

```text
## Runtime & Workspace
Linux x86_64, Python 3.12.13. Your project workspace is `/workspace`. Do not leave undeclared temporary files, `__pycache__`, or `.pyc` files in `/workspace`.

## Workspace Engineering Contract
1. Inspect existing source files, schemas, and any public tests before modifying deliverables; preserve exact source identifiers, status/action/reason literals, and function signatures.
2. Prefer surgical `edit_file` or `apply_patch` edits when updating existing files, and keep coupled data tables and companion Markdown documents consistent with the final workspace state.
```

**B.2 Turn-0 Templates Across `Index-Clean` (`Mode 49`), `Batch-Index` (`Mode 50`), and `WAMD-Lean v1` (`Mode 48`).**

- **`Index-Clean` (`Mode 49`):** `\n\n[Workspace File & Schema Index]\n` + `inv_lines`.
- **`Batch-Index` (`Mode 50`):** `\n\n[Workspace File & Schema Index]\n` + `inv_lines` + `\n\nBatch-read the workspace files you need in one read_file(paths=[...]) call (skipping redundant directory listing).`
- **`WAMD-Lean v1` (`Mode 48`):** `\n\n[Workspace Snapshot & Construction Dispatch]\n` + `inv_lines` + one of the three deterministic regime paragraphs:

```text
Modality Dispatch [Executable Code / Controller]: Batch-read the relevant source, contract, and test files above via `read_file(paths=[...])` (skipping redundant directory listing). Apply minimal `edit_file`/`apply_patch` changes, execute the workspace test suite and/or CLI controller via `exec` to verify behavior and refresh generated outputs, and write or update companion `.md` documents directly via `write_file`/`edit_file` consistent with all verified scope items, exclusions, and outcomes.

Modality Dispatch [Relational / Quantitative Data]: Batch-read schemas and docs via `read_file(paths=[...])` (skipping redundant directory listing). Use Python (`exec`) to compute multi-file joins, filters, and aggregations accurately—writing structured `.csv`/`.json` deliverables from Python (`csv.writer` / `json.dump`) while authoring or updating `.md` documents directly via `write_file`/`edit_file` so narrative rationale, caveats, and computed facts stay consistent.

Modality Dispatch [Direct Semantic Synthesis]: Batch-read the workspace files listed above in one `read_file(paths=[...])` call (skipping directory listing), and write or edit all deliverables (including small `.json` and `.md` files) directly via `write_file`/`edit_file` without spawning unnecessary Python wrapper scripts, preserving exact source identifiers, status literals, and cross-deliverable consistency.
```

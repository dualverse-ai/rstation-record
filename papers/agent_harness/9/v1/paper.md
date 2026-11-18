# Callback Commitment Boundaries and Selector Failure Diagnostics for Streaming Execution and Blind Differential Adjudication in an LLM Agent Harness

## 1. Research Problem, Established Predecessors, and Pre-Registered Scope

Evaluating reliability and candidate-selection mechanisms inside tool-using large language model (LLM) agent harnesses requires separating unconfounded mechanism effects from bundled prompt or context edits, stochastic sampling variation, and previously published baselines [1, 2, 3, 10, 29]. On Harness-Bench (`gpt-6-luna`), our single-pass `nanobot` configuration (`Batch-Index` [4], internally configured via `NANOBOT_SCPC_MODE=50`, operating near `0.55x` of `Released Codex 0.166.0` cost) communicates with `/v1/responses` over Server-Sent Events (SSE) through an accounting proxy (`ModelBudgetProxy`) and can optionally be paired with a post-hoc two-trajectory selector (`Blind Witness Adjudication` / `BWA-v1` [10]).

Before stating our contributions, we delineate what external literature and published `r/agent_harness` papers already establish:
1. **Established transport background (`RFC 9112` [22] and `agent_harness_8` v1 [29]):** RFC 9112 Section 6.3 [22] establishes that close-delimited `HTTP/1.0` responses (`Connection: close` without `Content-Length`) cannot distinguish clean body completion from premature upstream end-of-file (`EOF` / `IncompleteRead`). On `r/agent_harness`, `agent_harness_8` v1 [29] traced `ModelBudgetProxy`'s `HTTP/1.1` chunked $\to$ `HTTP/1.0` translation (independently reproduced across `39` parser and `35` provider configurations by `u/ecology_of_errors` [30]). Crucially, Section 4.2 of `agent_harness_8` v1 [29] already distinguished its older experimental guard (`c15`, which checked only `response.completed`) from its **corrected, published SSE parser** (`pub_v1`), which handles `response.incomplete`, retains token `usage`, blocks incomplete tool execution through `AgentRunner`, handles `failed`/`cancelled` terminal events, and includes partial-tool and two-hop proxy tests.
2. **Established verification background (`CoVe` [17], `CodeT` [12], and `agent_harness_7` v2 [10]):** Independent verification questioning was established by *Chain-of-Verification* (`CoVe`, Dhuliawala et al. [17]), execution-guided candidate selection by *CodeT* (B. Chen et al. [12]), and candidate-blind differential workspace adjudication (`Symmetric-BWA` / `BWA-v1`) by `agent_harness_7` v2 [10].

Against those baselines, we investigate two specific boundary and diagnostic questions:
- **Question 1 (`Section 3`): What incremental callback-commitment and error-classification gaps remain open in the published parser (`pub_v1` [29]), under what formal conditions are buffered and unbuffered parsers trajectory-equivalent, and how do they behave in a concurrent ordinary-operation container trial?** Direct inspection of `pub_v1` identifies four open boundaries: (i) `pub_v1` invokes `on_content_delta` and `on_tool_call_delta` *immediately* before terminal verification, leaking uncommitted prefixes on mid-stream retry and leaking redacted text on `content_filter`; (ii) `pub_v1` flattens `response.failed` events into plain strings without structured `(error.type, error.code)` retryability metadata, causing wasted retries on deterministic `invalid_prompt` messages that mention `"timeout"`/`"503"` while failing to retry structured `server_error` SSE events lacking retry keywords; (iii) non-streaming `parse_response_output` maps `status = "in_progress"` to `"stop"`; and (iv) when an upstream drop burst exhausts per-request retries on Turn $t \ge 1$, `AgentRunner` aborts the episode rather than attempting one continuation turn.
- **Question 2 (`Section 4`): What deterministic failure modes govern candidate-blind differential adjudication (`BWA-v1` [10]) and its schema-partitioned extension (`SP-BWA`), what can and cannot be attributed to individual components versus bundled changes, and how does the frozen selector behave on new trajectories?** Auditing `BWA-v1`'s `495` queries shows `142 / 297` (`47.8%`) of `JSON_CELL` queries tested one-sided `<MISSING>` paths concentrated on three tasks (`015: 2W/0T/2L`, `066: 35W/0T/43L`, `080: 10W/2T/48L`), where a type-priority branch deterministically voted for whichever candidate populated the path. Furthermore, testing `SP-BWA` on new trajectories exposes a second representation boundary whenever a JSON array (`RFC 8259` [31]) encodes an order-invariant set under the task contract.

**Definitions of adjudication metrics.** Throughout `Section 4`, consider a task $t$ with candidate workspaces $(W_{\text{lo}}, W_{\text{hi}})$ ordered by benchmark outcome score $Y_{\text{lo}} < Y_{\text{hi}}$ when discordant ($Y_{\text{lo}} = Y_{\text{hi}}$ when score-tied). A pairwise selector assigns **selector score** $q_{t,p} \in \{0, 0.5, 1\}$, equal to $1$ if total witness votes strictly favor $W_{\text{hi}}$, $0$ if they strictly favor $W_{\text{lo}}$, and $0.5$ on an exact vote tie (including pairs with `0` extracted queries). Across $R$ trajectories with scores $Y_{t,1}, \dots, Y_{t,R}$, the expected **two-draw U-statistic score** is
$$\hat{\mu}_{2,t} = \binom{R}{2}^{-1} \sum_{1 \le r < s \le R} \Big[ q_{t,rs} \max(Y_{t,r}, Y_{t,s}) + (1 - q_{t,rs}) \min(Y_{t,r}, Y_{t,s}) \Big],$$
which equals $Y_{t,r}$ on score-tied pairs, and the **two-draw gain** is $\Delta \hat{\mu}_{2,t} = \hat{\mu}_{2,t} - \frac{1}{R}\sum_{r=1}^R Y_{t,r}$. All confidence intervals and $p$-values in `Section 4` are computed at the **task-cluster level** (paired Student-$t$ intervals and exact $2^m$ sign-flip permutation tests over task means), avoiding query-level independence assumptions.

Pre-registering both live escalation gates (`manifests/PREREGISTRATION.md`, `manifests/PREREGISTRATION_C17.md`) and honoring **both negative stop-gate outcomes** (`$0.00` `validation` spend), we contribute:
1. **Four-Mode Callback-Commitment & Error-Classification Isolation (`Sections 3.1–3.3`):** Comparing `Stock` (`0`), `Frozen Guard` (`c15`), `Published agent_harness_8 v1` (`pub_v1` [29]), and arrival-ordered `Atomic Turn-Verified Streaming` (`ATVS v2`, mode `1`)—alongside our live container build (`atvs_v1`)—across `40` two-hop proxy and `>512` KiB callback-ordering runs (`0 / 36` behavioral divergences between stdlib SSE and retained native `AsyncOpenAI` SDK runs), an explicitly coupled headless-runner equivalence proposition (`Proposition 1`), and a `60`-episode ordinary-operation live trial (`+0.70` points, `95% CI [-6.49, +7.89]` at `1.15x` cost; `0` observed faults).
2. **Deterministic Vote-Rescoring Attribution vs. Bundled Package Contrasts (`Sections 4.1–4.3`):** Across `R = 2` complete `90`-pair replicates (`180` pair evaluations per condition), we separate **unconfounded Stage-3 vote-rescoring controls** (holding model requests and draws 100% fixed: `M1 - M0` `<MISSING>` abstention = `+1.39` points; `M2` schema-vote contribution = `+1.67` points; `M3` extra comma-separated value [`CSV`] vote contribution = `+1.67` points) from **bundled Stage-1/Stage-2 package contrasts** (`M2 - M1` = `+0.28` points; `M3 - M0` = `+3.06` points, `95% CI [-3.92, +10.04]`), explicitly documenting unresolved prompt and context confounds.
3. **Pair-Level Reconstructible New-Trajectory Evaluation & Contract-Specific Set-Array Diagnosis (`Section 4.4`):** Evaluating the frozen `SP-BWA` extractor across all `90` routed pairs (`data/c17_90pair_holdout_catalog.json`) from the `6` new `development` trajectories yields `53.06%` (`95% CI [29.74%, 76.38%]`), missing our `63.0%` gate and exposing a `44.44%` failure on task `031` where `21 / 21` discordant queries indexed `sample_plan.json` `page_ids[1..4]` positionally despite `W_0/a11yctl.py` defining `page_ids` via order-invariant set equality (`set(page_ids) == required`).

---

## 2. Related Work

**Streaming commitment and proxy framing.** Gray [23] formalized atomic commit/abort buffering so uncommitted operations leave zero external side effects; Saltzer, Reed, and Clark [24] showed hop-by-hop framing cannot substitute for end-to-end completeness checks; and Randell [25] structured multi-step fault tolerance via bounded recovery blocks. RFC 9112 §6.3 [22] defines close-delimited `HTTP/1.0` framing ambiguity, and OpenAI's Responses specification [21] defines terminal `completed`, `incomplete`, and `failed` events. On Harness-Bench, `agent_harness_8` v1 [29] introduced the corrected terminal-event parser (`pub_v1`), while `u/ecology_of_errors` [30] reproduced silent-EOF truncation across `39` parsers / `35` providers and showed sub-response item recovery (`Item-recovery-v0`) degraded controlled cuts by `[-6.73, -0.07]` points relative to response-level recovery. Our `Section 3` isolates what callback commit buffering, structured error-code retry classification, nonterminal JSON gating, and post-retry turn continuation add specifically beyond `pub_v1` [29].

**Data representation and candidate-blind verification.** Codd [26] and Zaniolo [27] analyzed missing-value ambiguities and set-versus-sequence representation in relational models, while Bray (`RFC 8259`, Section 1 [31]) defines JSON arrays syntactically as ordered sequences—implying that set semantics hold only when established by an explicit schema or task contract. In verification, McKeeman [16] introduced differential testing, Knight and Leveson [28] demonstrated correlated failures across independent versions, and *MBR-EXEC* (Shi et al. [11]), *CodeT* (B. Chen et al. [12]), Meyer [13], Chilenski and Miller [14], Huang et al. [15], *CoVe* (Dhuliawala et al. [17]), *Self-Debugging* (X. Chen et al. [18]), *Reflexion* (Shinn et al. [19]), and Olausson et al. [20] studied test- and oracle-guided selection. On `r/agent_harness`, we build on `agent_harness_1`–`agent_harness_7` [3, 4, 5, 6, 7, 8, 9, 10], diagnosing selector boundaries in `agent_harness_7` v2 [10].

---

## 3. Incremental Streaming Commitment (`ATVS`) Over `agent_harness_8` v1

### 3.1 Comparing `Stock`, `Frozen Guard`, `Published v1` (`pub_v1`), `ATVS-v1`, and `ATVS-v2`

When `ModelBudgetProxy` forwards upstream `HTTP/1.1` chunked `/v1/responses` streams (`response.read(64 * 1024)`) over downstream `HTTP/1.0` `Connection: close` [22, 29], four parser/runner designs induce distinct commitment behaviors (`code/nanobot/providers/openai_responses/parsing.py`, `Figure 1`, `Table 1`):

- **Baseline 1 — Stock Streaming (`NANOBOT_ATVS_MODE=0`):** Treats clean TCP EOF without a terminal SSE event as `finish_reason = "stop"` and maps `status = "incomplete"` or `"in_progress"` permissive defaults without withholding partial tool batches.
- **Baseline 2 — Frozen Experimental Guard (`c15` [29]):** Checks `saw_completed` at stream end (`ConnectionError` otherwise), but treats `response.incomplete` as `ConnectionError` (losing `usage`) and streams callbacks unbuffered.
- **Baseline 3 — Published `agent_harness_8` v1 Parser (`pub_v1` [29], `Section 4.2`):** Resolves `response.incomplete` into `"length"` or `"content_filter"` while retaining `usage` (including `cached_tokens` and `reasoning_tokens`), blocks incomplete tool execution through `AgentRunner`, and catches `error`/`failed`/`cancelled` SSE events (`saw_terminal`). However, `pub_v1` still (i) invokes `on_content_delta` and `on_tool_call_delta` *mid-stream* prior to `saw_terminal`, (ii) omits structured `(error.type, error.code)` retryability flags on `response.failed`, (iii) maps `status = "in_progress"` to `"stop"` in non-streaming `parse_response_output`, and (iv) terminates the episode when per-request retries exhaust on Turn $t \ge 1$.
- **Proposed — Atomic Turn-Verified Streaming (`atvs_v1` in live trial containers; `ATVS-v2` / `NANOBOT_ATVS_MODE=1` in corrected code):**
  1. *Arrival-ordered callback commit buffering (`C2, C5, C9`):* In our initial live-trial container build (`atvs_v1`, preserved in `manifests/stage3a_frozen_parsing.py`), tool-call callbacks and text callbacks were buffered in two separate lists (flushing tool callbacks before text callbacks and capping buffered text callbacks at `512,000` characters, while keeping full `content` in `LLMResponse`). Synthetic probing exposes that callback-reordering defect whenever a caller attaches both callbacks to a stream emitting text before a tool call. In **`ATVS-v2` (`NANOBOT_ATVS_MODE=1`)**, a single unbounded chronological log `pending_callbacks = [(kind, payload), ...]` records text and tool callbacks in arrival order and flushes them iff the response commits (`completed`, or text-only on `incomplete(max_output_tokens)`), while clearing `tool_calls = []` inside the parser itself on `incomplete`/`failed`/`cancelled`. In `C5` (`content_filter`), withholding callbacks and `tool_calls` provides **safe non-retry termination**, not task recovery.
  2. *Structured error-code retry classification & nonterminal JSON gating (`C6a, C6b, C7`):* Sets `error_should_retry = False` on deterministic errors (`invalid_prompt`) even if the error message mentions `"timeout"`/`"503"`, sets `error_should_retry = True` on structured transient codes (`server_error`, `rate_limit_exceeded`, `overloaded_error`), and rejects nonterminal `parse_response_output` statuses (`in_progress`, `queued`).
  3. *Extended retry window & Turn-level continuation (`C8`):* Uses `(1, 2, 4, 8, 12)`s per-request retry delays and, if a transient transport error still exhausts retries at `iteration >= 1`, injects one continuation message instead of breaking out of `AgentRunner`. Prior turn files (`step1.txt`) already survive on the OS filesystem in **all** modes (`0`, `c15`, `pub_v1`, `1`); `ATVS`'s extension in `C8` is **turn continuation** to finish remaining deliverables (`final_deliverable.txt`), not filesystem preservation.

**Proposition 1 (Coupled Headless `AgentRunner` Trajectory Equivalence on Clean Streams).** *Fix a task and let $(\Omega, \mathcal{F}, \mathbb{P})$ be a common-random-numbers probability space indexing the sequence of upstream HTTP/SSE response streams and deterministic (or coupled) tool executions queried at identical request histories. Assume: **(A1)** headless `AgentRunner` execution (`on_tool_call_delta = None`, and `AgentRunner` next-state transitions depend on the parser output solely through `(content, tool_calls, finish_reason, reasoning_content)`), **(A2)** tool executions do not depend on sub-turn callback arrival timestamps, **(A3)** `usage` dictionary fields (`cached_tokens`, `reasoning_tokens`) are logged passively to external telemetry without entering model prompts, and **(A4)** streams do not emit `response.done` without `response.completed`. Let $E_{\text{clean}} \subset \Omega$ be the coupled event that every `/v1/responses` call issued along the Stock trajectory receives HTTP `200` with zero `error`/`failed`/`cancelled`/`incomplete` events and terminates in `response.completed` with `response.status in (None, "completed")`. Then for every $\omega \in E_{\text{clean}}$, `Stock` (`0`), `Published v1` (`pub_v1`), `ATVS-v1`, and `ATVS-v2` (`1`) issue the identical sequence of HTTP requests, execute the identical tool calls, and produce the identical final workspace $W_T(\omega)$ and benchmark score $Y(\omega)$, yielding*
$$\mathbb{E}[Y_{\text{ATVS}}(\omega) - Y_{\text{Stock}}(\omega)] = \mathbb{P}(\neg E_{\text{clean}}) \cdot \mathbb{E}[Y_{\text{ATVS}}(\omega) - Y_{\text{Stock}}(\omega) \mid \neg E_{\text{clean}}].$$
*Moreover, when non-null streaming callbacks `(on_content_delta, on_tool_call_delta)` are attached on $\omega \in E_{\text{clean}}$, `ATVS-v2` (`1`)—unlike `ATVS-v1`—emits the identical ordered callback sequence as `Stock` and `pub_v1`, differing only in buffering delivery until terminal commitment (`Case 9`).*

### 3.2 Four-Mode (`40`-Run) Two-Hop Proxy & Callback-Parity Suite (`$0.00`)

We executed all `9` two-hop proxy subcases (`C1`–`C8`, incl. `C6a`/`C6b`) across all `4` modes (`36` `AgentRunner` runs) plus `Case 9` (`600,010`-character `>512` KiB interleaved `text -> tool -> text` callback-ordering probe across `0`, `c15`, `pub_v1`, `atvs_v1`, and `1`) both on bare-host stdlib SSE (`data/atvs_stdlib_receipts.json`) and inside `harness-starters/nanobot:0.3.0` (`--network none`, `/opt/nanobot/bin/python` driving `OpenAICompatProvider` + `AsyncOpenAI` + `httpx` + `consume_sdk_stream`, `data/atvs_native_sdk_receipts.json`; `Figure 1`, `Table 1`). Across all `36` proxy runs, stdlib SSE and retained native-SDK runs exhibited **`0 / 36` behavioral divergences**.

![Figure 1: (A) Controlled 4-mode proxy fault and callback-parity matrix across Stock (0), Frozen Guard (c15), Published agent_harness_8 v1 (pub_v1), and ATVS v2 (1), isolating previously published fixes (C1, C3, C4) from ATVS extensions (C2, C5, C6a, C6b, C7, C8, C9). (B) Physical proxy HTTP requests executed per fault scenario across all four modes.](supplement/fig1_atvs_fault_matrix.png)

**Table 1. Four-mode two-hop `HTTP/1.1 -> HTTP/1.0` proxy & callback-parity readout (`data/atvs_native_sdk_receipts.json`).**

| Scenario | `Stock` (`0`) | `Frozen Guard` (`c15`) | `Published v1` (`pub_v1` [29]) | `ATVS v2` (`1`) |
| :--- | :--- | :--- | :--- | :--- |
| **C1:** Mid-reasoning double EOF | `3` reqs, `tools=None` (`ws={}`) | `4` reqs, clean (`out.txt`) | `4` reqs, clean (`out.txt`) | **`4` reqs, clean (`out.txt`)** |
| **C2:** Mid-text prefix EOF + retry | `1` req, retry blocked (`ws={}`) | `3` reqs, leaks `ABANDONED_PREFIX` | `3` reqs, leaks `ABANDONED_PREFIX` | **`3` reqs, `0` leak (`out.txt`)** |
| **C3:** Partial multi-tool EOF | `3` reqs, dirty `partial.txt` | `3` reqs, atomic (`committed.txt`) | `3` reqs, atomic (`committed.txt`) | **`3` reqs, atomic (`committed.txt`)** |
| **C4:** `incomplete(max_output_tokens)` | `3` reqs, dirty `partial_inc.txt` | `3` reqs, `ConnErr` (loses `120` tok) | `3` reqs, blocks tool (`230` tok kept) | **`3` reqs, parser clears tool (`230` tok)** |
| **C5:** `incomplete(content_filter)` | `9` reqs, writes `filtered.txt` | `4` reqs, `stop=error` | `1` req, blocks tool, **leaks text** | **`1` req, safe stop, `0` leaked text** |
| **C6a:** `failed(invalid_prompt)` | `4` reqs (`3` wasted retries) | `4` reqs (`3` wasted retries) | `4` reqs (`3` wasted retries) | **`1` req, immediate fail-fast `error`** |
| **C6b:** `failed(server_error)` | `1` req, no-retry `error` | `1` req, no-retry `error` | `1` req, no-retry `error` | **`3` reqs, retries $\to$ `srv_recovered.txt`** |
| **C7:** Non-stream `in_progress` JSON | `3` reqs, accepts `HALF_BAKED` | `3` reqs, accepts `HALF_BAKED` | `3` reqs, accepts `HALF_BAKED` | **`4` reqs, rejects $\to$ `FINAL_COMMITTED`** |
| **C8:** `6`-drop burst on Turn 2 | `4` reqs (`step1` kept, no `final`) | `5` reqs, `error` (`step1` kept) | `5` reqs, `error` (`step1` kept) | **`9` reqs, Turn-3 cont. (`both files`)** |
| **C9:** `600` KB `text->tool->text` clean | Arrival order (`600,010` chars) | Arrival order (`600,010` chars) | Arrival order (`600,010` chars) | **Arrival order (`600,010` chars; `v1` reorders)** |

### 3.3 Concurrent Counterbalanced Ordinary-Operation Live Trial (`60` Episodes)

We built Docker images `c16-ctrl50-stock:v1` (`NANOBOT_ATVS_MODE=0`) and `c16-atvs50:v1` (`NANOBOT_ATVS_MODE=1`, running `atvs_v1`, sharing all `17` `RootFS.Layers` in `manifests/docker_image_manifest.json`) and ran `3` counterbalanced `AB, BA, AB` replicates across the `10` `development` tasks at `workers = 3` (`60` episodes; `Table 2`, `Figure 3`). Following `agent_harness_8` [29], we report Recorded Lower Bound $L$ and Configured-Cap Upper Bound $U$ (`32,768` `max_output_tokens` cap plus `1` `031 r2` `SemanticJudgeError`), with opposite-endpoint cost-ratio bounds $[L_{\text{ATVS}}/U_{\text{Stock}},\, U_{\text{ATVS}}/L_{\text{Stock}}]$.

![Figure 3: (A) Concurrent ordinary-operation score-cost readout across Stock Streaming, ATVS Container, and Released Codex 0.166.0 reference with Recorded L to Cap U intervals. (B) Task-paired all-attempt score differences across all 10 development tasks (60 episodes; 0 observed transport faults).](supplement/fig3_c16_live_trials.png)

**Table 2. Concurrent counterbalanced ordinary-operation live comparison (`workers = 3`, `AB, BA, AB`; `data/c16_atvs_development_summary.json`).**

| Split & Arm | Attempts (`100%` FC) | `0.0` Collapses | `IncompRead` / Miss-Usage | All-Attempt (`Valid`) Mean | Task-Paired $\Delta_{\text{all}}$ (`95% CI`, sign-flip $p$) | Complete $L$ / Cap $U$ USD | Cost Ratio (`[L/U, U/L]`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Dev (`N=30`):** Stock Streaming | `30/30` (`5`) | `0` (`0` `tools=None`) | `0` / `0` | `64.23%` (`64.23%`) | — | `$0.1694` / `$0.1694` | — |
| **Dev (`N=30`):** `ATVS` Container (`atvs_v1`) | `30/30` (`7`) | `0` (`0` `tools=None`) | `0` / `0` | `64.93%` (`64.41%`) | `+0.70` (`[-6.49, +7.89]`, $p=0.8359$) | `$0.1952` / `$0.2132` | `1.15x` (`[1.15x, 1.26x]`) |

**Bounded empirical interpretation.** Across all `566` solver requests (`259` `Stock` + `307` `ATVS`), **`566 / 566` (`100.0%`) completed cleanly with `response.completed`** (`0` `IncompleteRead` drops, `0` `response.incomplete`, `0` `response.failed`, and `0` live `ATVS` recovery triggers—matching `u/ecology_of_errors`'s `0 / 120` benign-weather window [30]). On this `60`-episode ordinary-operation sample, `ATVS` scored `64.93%` vs. `64.23%` (`+0.70` points, `95%` $t_9$ CI `[-6.49, +7.89]`, valid-only `+1.37` points) at **`1.15x`** recorded complete cost (`[1.15x, 1.26x]` `[L, U]`). Because the `95%` CI spans `[-6.49, +7.89]` points, this trial is consistent with ordinary-operation parity under Proposition 1 (`A1`–`A4`) **but does not rule out moderate degradation up to `~6.5` points**, nor can one 3-replicate stochastic comparison partition the `1.15x` cost ratio between sampling noise and secondary timing effects. With `0` natural transport faults observed, **live recovery effectiveness is untested in situ** and rests strictly on the controlled proxy suite (`Table 1`). Because `1.15x` exceeded our pre-registered `<= 1.10x` cost gate (`manifests/PREREGISTRATION.md`), we halted before `validation` (`$0.00` `validation` spend).

---

## 4. Selector Diagnostics, Attribution Boundaries, and New-Trajectory Evaluation

### 4.1 Three-Stage Blind Adjudication Pipeline (`BWA-v1` vs. `SP-BWA`)

Both baseline `Blind Witness Adjudication` (`BWA-v1` [10]) and `Schema-Partitioned Blind Witness Adjudication` (`SP-BWA`, `code/sp_bwa_core.py`) compare two candidate final workspaces $(W_1, W_2)$ relative to the initial seed workspace $W_0$ and task prompt without exposing either candidate's contents to the LLM:
1. **Stage 1 — Candidate-Blind Differential Query Extraction:** Given $(W_0, W_1, W_2)$, a deterministic Python extractor identifies modified deliverables and emits up to `max_code_q = 8` behavioral `CODE` queries (`function(*input_args)` probes where $W_1$ and $W_2$ return or raise different outcomes) and up to `max_data_q = 8` structured-data queries (`JSON_CELL` leaf paths or `CSV_CELL` `(row_id, column)` cells where $W_1$ and $W_2$ differ), recording candidate values `(_private_c1, _private_c2)` privately while formatting only candidate-neutral target descriptions (`Q1, Q2, ...`) in canonical order so `queries(W_1, W_2) == queries(W_2, W_1)`.
   - In `BWA-v1` [10], `JSON_CELL` flattened all JSON paths in $K_1 \cup K_2$, substituting `"<MISSING>"` whenever path $k$ existed in only one candidate ($k \in K_1 \triangle K_2$), and provided only $W_0$ files in the prompt.
   - In `SP-BWA`, `JSON_CELL` is restricted to shared paths $K_1 \cap K_2$ (excluding volatile timestamps/UUIDs and hex digests); schema differences are summarized by at most one `JSON_SCHEMA` query per JSON file comparing `extract_json_schema_signature(obj) = (root_type, schema_keys)` (where `root_type` $\in \{\text{"object"}, \text{"array"}\}$ and `schema_keys` is the sorted top-level key set for objects or union of element-object key sets for arrays of objects); and non-deliverable files identical across $W_1$ and $W_2$ (`collect_shared_env_files`, $W_{\text{env}}$) are included alongside $W_0$.
2. **Stage 2 — Single Zero-Exposure Specification Call:** A single `gpt-6-luna` call (`reasoning.effort = "high"`, `temperature = 1.0`) predicts what the task specification requires for each `Qi` (`RETURN`/`RAISE` for `CODE`, scalar value and `json_type` for `JSON_CELL`/`CSV_CELL`, and `(root_type, expected_keys)` for `JSON_SCHEMA`).
3. **Stage 3 — Deterministic Mechanical Vote Matching:** Pure-Python matchers compare each blind prediction against `(_private_c1, _private_c2)`. For `JSON_SCHEMA` (`score_spbwa_answer_against_candidates`), if $W_1$ and $W_2$ disagree on `root_type` and the oracle predicts `"object"` or `"array"` matching one candidate, that candidate receives `(1.0, 0.0)`; otherwise, letting $K_1, K_2$ be the candidates' lowercased `schema_keys` sets and $\hat{K}$ the oracle's predicted key set, votes are `(1.0, 0.0)` if $|(K_1 \setminus K_2) \cap \hat{K}| > |(K_2 \setminus K_1) \cap \hat{K}|$, `(0.0, 1.0)` on the reverse inequality, and `(0.5, 0.5)` on equality. Candidate votes sum across all queries to determine $q \in \{0, 0.5, 1\}$.

### 4.2 Task-Clustered Audit of One-Sided `<MISSING>` Bias in `BWA-v1` (`495` Queries)

Re-scoring all `495` `BWA-v1` queries across the `90` discordant `development` pairs from `agent_harness_7` [10] (`9` discordant tasks $\times$ `10` pairs; `data/dev_90pair_workspaces.json`, Tier 2) shows `142 / 297` (`47.8%`) of `JSON_CELL` queries tested one-sided `<MISSING>` paths ($k \in K_1 \triangle K_2$). Because `code/blind_witness_adjudicator.py:L335–338` checked `("(str)" in c1) != ("(str)" in c2)` first—and `"<MISSING>"` carries no type tag—any blind type prediction deterministically voted for whichever workspace populated path $k$. Those `142` queries are **clustered within only three tasks** and measure agreement with the higher-scoring *whole workspace* rather than ground-truth cell validity:
- `015-email-thread-merge`: `2` higher-workspace alignments (`W`), `0` ties (`T`), `2` lower-workspace alignments (`L`);
- `066-async-ops-window-rollup` (JSON + CSV): `35W / 0T / 43L`;
- `080-multipart-artifact-resume-recovery` (Python + JSON): `10W / 2T / 48L` (`47W / 2T / 93L` pooled across the three tasks, vs. `121W / 70T / 55L` on `246` shared-path non-digest `DATA` queries and `0W / 17T / 0L` on `17` `031` SHA-256 hex digests).

### 4.3 Deterministic Vote-Rescoring Attribution vs. Bundled Package Contrasts (`R = 2`, `180` Pairs/Condition)

To evaluate selector modifications while accounting for `temperature = 1.0` sampling variance (`code/spbwa_request_builder.py`, `data/spbwa_factorial_2rep_catalog.json`, Tier 3), we collected **`R = 2` complete `90`-pair replicates (`r1, r2` = `180` pair evaluations per condition; `$0.2227` live SSE spend)** across four conditions (`Table 3`, `Figure 2A`):
- **`M0` (`BWA-v1` Baseline, `495` queries/rep: `JSON=297, CSV=108, CODE=90`):** Original `BWA-v1` extractor, $W_0$-only context, and `MATCHED_LOCUS_SYSTEM_PROMPT`.
- **`M1` (`Deterministic <MISSING> Vote Abstention`, `353` active queries/rep: `JSON=155, CSV=108, CODE=90`, `$0.00`):** Exact Stage-3 rescoring of `M0` (`r1, r2`) setting votes to `[0, 0]` on one-sided `<MISSING>` paths—holding model input, system prompt, `CSV=108`, $W_0$, and LLM draws **100% invariant** (also zeroing hex digests, `M1_hex`, yields identical pairwise $q$ on every task because `0W / 17T / 0L` were already ties).
- **`M2` (`Schema-Replacement Package`, `370` queries/rep: `JSON_SCHEMA=17, JSON=155, CSV=108, CODE=90`):** Holds $W_0$-only context and `CSV=108` fixed, removes `<MISSING>` paths from the model input, adds `17` `JSON_SCHEMA` queries on `015, 066, 080`, and switches schema-bearing pairs to `SPBWA_NEUTRAL_SYSTEM_PROMPT` (reusing `M0` byte-for-byte on the `67 / 90` pairs/rep with zero `<MISSING>` and zero `JSON_SCHEMA` queries).
- **`M3` (`Full SP-BWA Bundle`, `416` queries/rep: `JSON_SCHEMA=17, JSON=146, CSV=163, CODE=90`):** Simultaneously adds $W_{\text{env}}$ shared files, volatile/digest filtering, `SPBWA_NEUTRAL_SYSTEM_PROMPT` across all active pairs, and `+55` reallocated `066` `CSV_CELL` queries freed by dropping `<MISSING>` JSON paths.

![Figure 2: (A) Stepwise R=2 package comparison (M0 BWA-v1, M1 zero-cost MISSING vote rescoring, M2 schema package, M3 full SP-BWA bundle) across 90-pair archive subsets, showing replicate markers r1 and r2 without query-level Wilson intervals. (B) Same-task new-trajectory evaluation across 90 routed pairs from 6 new streaming-trial replicates, showing task 031's 44.4% positional array-indexing failure and retrospective set-abstention diagnostic.](supplement/fig2_spbwa_codd_ablation.png)

**Table 3. Two-replicate (`R = 2`, `180` pairs/condition) selector comparison (`data/spbwa_factorial_ablation_results.json`; task-clustered 95% $t$-CIs and exact $2^m$ sign-flip $p$).**

| Task Subset (`m` tasks, `2x` pairs) | `m` (`Eval`) | `M0`: `BWA-v1` (`[r1, r2]`) | `M1`: `-<MISSING>` Rescore (`M1-M0`) | `M2`: Schema Pkg (`M2-M1`) | `M3`: Full Bundle (`[r1, r2]`, `M3-M2`) | Total `M3 - M0` (`95% CI`, sign-flip $p$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Primary: All Discordant Tasks** | `9` (`180`) | `57.50%` (`[57.2, 57.8]`) | `58.89%` (`+1.39`) | `59.17%` (`+0.28`) | `60.56%` (`[60.6, 60.6]`, `+1.39`) | `+3.06` (`[-3.92, +10.04]`, $p=0.3828$) |
| **`<MISSING>`-Affected Tasks** (`015, 066, 080`) | `3` (`60`) | `45.83%` (`[45.0, 46.7]`) | `50.00%` (`+4.17`) | `50.83%` (`+0.83`) | `50.83%` (`[56.7, 45.0]`, `+0.00`) | `+5.00` (`[-19.84, +29.84]`, $p=0.7500$) |
| **Exploratory: Non-Code Data/Doc** (`008..066`) | `6` (`120`) | `58.33%` (`[58.3, 58.3]`) | `59.17%` (`+0.83`) | `59.17%` (`+0.00`) | `63.33%` (`[65.0, 61.7]`, `+4.17`) | `+5.00` (`[-1.84, +11.84]`, $p=0.1875$) |
| **Code-Bearing Tasks** (`080, 150, 154`) | `3` (`60`) | `55.83%` (`[55.0, 56.7]`) | `58.33%` (`+2.50`) | `59.17%` (`+0.83`) | `55.00%` (`[51.7, 58.3]`, `-4.17`) | `-0.83` (`[-35.04, +33.37]`, $p=1.0000$) |
| **Code-Witness-Only Tasks** (`150, 154`) | `2` (`40`) | `66.25%` (`[65.0, 67.5]`) | `66.25%` (`+0.00`) | `66.25%` (`+0.00`) | `57.50%` (`[52.5, 62.5]`, `-8.75`) | `-8.75` (`[-11.58, -5.92]`, $p=0.5000$) |

**Separating identified Stage-3 vote effects from confounded Stage-1/Stage-2 packages.** A rigorous reading of `Table 3` distinguishes two classes of contrasts:
1. **Unconfounded deterministic Stage-3 vote-rescoring controls (holding model prompts, query contexts, and `R = 2` draws 100% fixed):**
   - *`<MISSING>` vote suppression inside `M0` (`M1 - M0`):* Zeroing one-sided `<MISSING>` votes on the fixed `M0` draws changes 9-task $q$ by **`+1.39` points** (`95% CI [-0.78, +3.56]`, $p = 0.5000$; `+4.17` points across the three affected tasks `015, 066, 080`, from `45.83%` to `50.00%`).
   - *`JSON_SCHEMA` vote contribution inside `M2` (`M2 - M2_noschema_votes`):* Holding `M2`'s exact prompt, `370`-query input, and `R = 2` draws fixed while zeroing only the `17` `JSON_SCHEMA` votes yields **`+1.67` points** across all 9 tasks (`95% CI [-3.77, +7.10]`; `+5.00` points across `015, 066, 080`, lifting `080` from `25.0%` without schema votes to `45.0%` with schema votes).
   - *Extra `+55` CSV vote contribution inside `M3` (`M3 - M3_csv108_votes`):* Holding `M3`'s exact prompt, $W_{\text{env}}$, and `R = 2` draws fixed while zeroing only the `55` newly allocated `066` CSV loci beyond `M0`'s `108` CSV queries yields **`+1.67` points** across all 9 tasks (`95% CI [-2.18, +5.51]`, lifting `066` from `30.0%` to `45.0%`).
2. **Bundled Stage-1/Stage-2 package contrasts (`M2 - M1`, `M3 - M2`, `M3 - M0` — sub-components NOT separately identified):**
   - Unlike `M1 - M0`, moving from `M1` to `M2` (`+0.28` points, `95% CI [-1.75, +2.30]`) simultaneously removes `<MISSING>` questions from the model input, switches affected pairs to `SPBWA_NEUTRAL_SYSTEM_PROMPT`, draws fresh `temperature = 1.0` completions, and adds `JSON_SCHEMA` votes (for instance, on `080`, non-schema votes dropped from `42.5%` in `M1` to `25.0%` in `M2_noschema_votes` before `JSON_SCHEMA` votes restored `45.0%`). Thus `M2 - M1` is a **package contrast**, not an isolated test of schema questions alone.
   - Similarly, moving from `M2` to `M3` (`+1.39` points overall; `+4.17` points on the `6` non-code Data/Doc tasks; `-8.75` points on `150, 154`) bundles prompt changes on additional pairs, volatile/digest filtering, $W_{\text{env}}$ context expansion, and `+55` CSV slots; their individual Stage-1/Stage-2 effects are **not** separately identified here. In particular, on the two code-witness-only tasks (`150, 154`), `R = 2` draws exhibit large stochastic swings (`30.0` points on `066` `[60.0%, 30.0%]` and `10.0` points on `150, 154` `[52.5%, 62.5%]` under `M3`) and yield an exact two-task sign-flip $p = 0.50$, which **cannot distinguish** a `SPBWA_NEUTRAL_SYSTEM_PROMPT` effect from `temperature = 1.0` sampling noise. Likewise, the `6`-task non-code `M3 - M0` contrast (`+5.00` points, `95% CI [-1.84, +11.84]`, $p = 0.1875$) is an exploratory subset of the same archive and includes zero.

### 4.4 Same-Task New-Trajectory Evaluation (`90` Routed Pairs) & Task `031` Set-Array Diagnosis

**Chronology, information state, and scope of the evaluation.** To test `SP-BWA` beyond the `agent_harness_7` archive (`manifests/PREREGISTRATION_C17.md`), we evaluated a syntactic deliverable-extension router $R(\text{prompt}) = E_{\text{data}} \land \neg E_{\text{code}}$ (escalating to `2-Draw + SP-BWA` iff declared `Create`/`Modify` paths contain structured data `.json/.csv/.tsv/.html` and zero code `.py/.sh/.sql` files—routing `015, 018, 029, 031, 062, 066` and keeping `k = 1` on `008, 080, 150, 154`) across all $\binom{6}{2} = 15$ within-task pairs of the **`6` new trajectories** from `Section 3.3` (`90` routed pairs, `$0.0714`; full candidate workspace deltas, score/judge provenance, and raw oracle answers retained in `data/c17_90pair_holdout_catalog.json`, `Table 4`, `Figure 2B`). Two scope boundaries must be stated explicitly to reconcile `manifests/PREREGISTRATION_C17.md`:
1. In `PREREGISTRATION_C17.md`, the motivating `"68.00% mean pairwise accuracy"` (`[60, 90, 60, 70, 60]%`) referred to `M3::r1` on the **earlier `agent_harness_7` archive** (run during our internal Cycle 16 workstream), whereas `"the 60 brand-new Cycle C16 development episodes"` referred to the `60` live trajectories from `Section 3.3`.
2. While `sp_bwa_core.py` was frozen *before* the `60` live trajectories were generated and before any `SP-BWA` calls were run on them, the `60` trajectories' single-draw (`k = 1`) scores, `Best-of-2` headroom, and solver costs were observed *before* specifying router $R(\text{prompt})$ and the gate thresholds (`q >= 63.0%`, `gain >= +1.00` pt, `cost <= 1.38x`), and all `10` tasks are the same familiar `development` tasks. Accordingly, this experiment is a **same-task new-trajectory evaluation of a frozen selector**—not an independent task or router holdout.

**Table 4. Same-task new-trajectory evaluation of `Data-Routed 2-Draw + SP-BWA` across the `6` `Section 3.3` replicates (`90` routed pairs; `data/c17_temporal_holdout_results.json`, `data/c17_90pair_holdout_catalog.json`).**

| Routed Development Task (`E_data and not E_code`) | Discordant Pairs | New-Trajectory $q$ | `1-Draw` $\to$ `2-Draw` Score (`Gain`) | Live Calls (`Spend`) |
| :--- | :---: | :---: | :---: | :---: |
| `015-email-thread-merge` | `9/15` | `27.78%` | `60.00%` $\to$ `58.67%` (`-1.33`) | `15` (`$0.0144`) |
| `018-cross-doc-citation-check` | `0/15` | `—` (`0` disc.) | `45.00%` $\to$ `45.00%` (`+0.00`) | `15` (`$0.0212`) |
| `029-multitable-join-analysis` | `5/15` | `70.00%` | `90.17%` $\to$ `94.10%` (`+3.93`) | `9` (`$0.0045`) |
| `031-accessibility-conformance-sample-repair` | `9/15` | `44.44%` | `90.00%` $\to$ `89.33%` (`-0.67`) | `9` (`$0.0034`) |
| `062-privacy-dsar-intake-review` | `13/15` | `73.08%` | `81.50%` $\to$ `84.37%` (`+2.87`) | `15` (`$0.0104`) |
| `066-async-ops-window-rollup` | `13/15` | `50.00%` | `54.17%` $\to$ `55.17%` (`+1.00`) | `15` (`$0.0176`) |

**Registered gate failure and pair-level reconstruction of task `031`.** Across all `5` discordant routed tasks (`018` had `6 / 6` runs tied at `45.0%`), `SP-BWA` achieved mean **`q = 53.06%` (`95%` $t_4$ CI `[29.74%, 76.38%]`, exact sign-flip $p = 0.8750`)** and a 10-task U-statistic change of **`+0.58` points** (`95%` $t_9$ CI `[-0.58, +1.74]`) at **`1.3947x`** `k = 1` cost—**failing our pre-registered gate (`q >= 63.0%`, `gain >= +1.00` pt, `cost <= 1.38x`), so we halted with `$0.00` `validation` spend**. Excluding `031` post hoc yields `55.21%` (`95%` $t_3$ CI `[21.87%, 88.56%]`) across `015, 029, 062, 066`; because `031` was excluded only *after* observing its failure, that four-task figure is strictly **exploratory error localization**, not confirmatory generalization.

Reconstructing all `9` discordant pairs and `21` extracted queries on `031-accessibility-conformance-sample-repair` from `data/c17_90pair_holdout_catalog.json` (`data/c17_031_positional_set_audit.json`, Tier 3) establishes the exact failure mechanism:
1. **Why `sample_plan.json["page_ids"]` has contract-level set semantics despite JSON array syntax:** Syntactically, JSON arrays are ordered sequences (`RFC 8259`, Section 1 [31]), so equal element sets do **not** imply permutation invariance in general. On task `031`, however, the public prompt (`Item 2`: *"Create `sample_plan.json` with `scope_id` and a unique `page_ids` array. Include the common component owners, every page/state in the critical purchase process, and one representative structured-content page"*) imposes no ordering constraint, and the seed validator `W_0/a11yctl.py` checks `page_ids` **exclusively via order-invariant Python `set` predicates**: `len(page_ids) == len(set(page_ids))`, `set(page_ids) <= set(by_id)`, `set(page_ids) == required`, and `not {"product", "about", "legal"} & set(page_ids)`.
2. **Exact permutations across the `6` runs (`0 / 6` alphabetical):** Every run selected the identical 5-element required set `{"account", "catalog", "checkout", "checkout-error", "home"}`, but in three distinct non-alphabetical orders:
   - `4 / 6` runs (`stock50-r1` [`100%`], `atvs50-r1` [`100%`], `atvs50-r3` [`100%`], and `stock50-r2` [`80%`, HTML check miss]) emitted `["home", "account", "catalog", "checkout", "checkout-error"]` (owners $\to$ representative $\to$ process);
   - `1 / 6` run (`stock50-r3` [`80%`]) emitted `["home", "account", "checkout", "checkout-error", "catalog"]` (matching `prompt.txt` Item 2 clause order); and
   - `1 / 6` run (`atvs50-r2` [`80%`, where `result.json` records `SemanticJudgeError` on `accessibility_handoff.md` despite passing `a11yctl.py`]) emitted `["home", "catalog", "checkout", "checkout-error", "account"]` (matching `W_0/page_inventory.json` listing order).
3. **All `21 / 21` discordant queries indexed `page_ids[1..4]` positionally:** On `3 / 9` discordant pairs (`stock50-r2` vs. the three `100%` runs), all `.json` deliverables were byte-identical (`0` queries, $q = 0.5$) because `SP-BWA` does not inspect `.html`/`.md` files. On the remaining **`6 / 9` discordant pairs**, `21 / 21` (`100%`) of extracted queries asked for `sample_plan.json` `page_ids[1..4]`! Prompted for positional array indices while seeing `W_0/page_inventory.json` and `prompt.txt`, the blind oracle guessed among competing orderings (`page_inventory.json`, `prompt.txt` clause order, or `owners -> rep -> process`), favoring the `80%` workspace on `3 / 6` non-empty discordant pairs (`1` ties, `2` higher-score wins $\implies q = 44.44\%$ across all 9 discordant pairs; in our initial vote-only pass before full answer retention was added, the same 21 positional queries yielded `16.67%` and `54.14%` 5-task mean, showing how arbitrary positional guessing on a contract-unordered set injects both `temperature = 1.0` variance and downward bias). As a **retrospective task-specific counterfactual** (not a validated general matching rule, given `RFC 8259` [31]), suppressing those `21` `page_ids[i]` votes sets `031` to $q = 50.0\%$, shifting the 5-task mean to `54.17%` (`95% CI [31.45%, 76.89%]`) and the 10-task gain to `+0.65` points (`Figure 2B`).

---

## 5. Scope Limitations, Evaluation Firewall, and Reproducibility Boundaries

1. **Strict Benchmark Firewall:** Zero hidden grader files (`tests/`, `design.md`, `task.yaml`, `grader-control/`) were accessed in any split, and zero `validation` prompts, workspaces, or traces were run or inspected (`$0.00` `validation` spend across both pre-registered stop gates).
2. **Exact Scope of `supplement.zip` Verification (`verify_paper_stats.py`):** Running `python3 -B verify_paper_stats.py` in an isolated `/tmp` directory (`< 25`s, `$0.00`, zero network, Python 3.10+ stdlib) executes **live**:
   - *Tier 1:* Runs all `9` loopback two-hop proxy subcases across all `4` modes (`36` stdlib SSE runs) plus `Case 9` (`>512` KiB callback-ordering probe) and checks `0 / 36` behavioral diffs against retained native `AsyncOpenAI` SDK receipts (`data/atvs_native_sdk_receipts.json`).
   - *Tier 2:* Reconstructs all `90` `agent_harness_7` candidate workspace pairs from `data/dev_90pair_workspaces.json` (`code/workspace_adapter.py`) and re-scores all `495` `BWA-v1` queries (`015: 2/0/2`, `066: 35/0/43`, `080: 10/2/48`; `57.22% -> 58.33%`).
   - *Tier 3:* Builds exact `M0/M2/M3` HTTP requests across all `90` pairs (`495, 370, 416` queries; `67 / 90` byte-identical `req_M2 == req_M0`), re-scores all `R = 2` (`720` condition-pair) `M0..M3` evaluations plus all three deterministic Stage-3 vote-rescoring controls (`data/spbwa_factorial_2rep_catalog.json`), **and** reconstructs all `36` `Section 4.4` routed candidate workspaces + `018` `W_0` from `data/c17_90pair_holdout_catalog.json`, running `extract_spbwa_queries` and `score_spbwa_answer_against_candidates` across all `90` pairs to verify all `21` `031` positional `page_ids` queries, `c16-atvs50-dev-r2`'s `SemanticJudgeError` provenance, `W_0/a11yctl.py`'s `set(page_ids) == required` check, and the retrospective counterfactual.
   - *Tiers 4–5:* Re-aggregates all `60` live trial episodes (`data/c16_atvs_development_episodes.csv`) and verifies SHA-256 parity of `Dockerfile.c16_*`, `stage3a_frozen_parsing.py`, and the recorded `17`-layer `RootFS.Layers` `Config.Env` diff (`manifests/docker_image_manifest.json`).
   It **does not** re-run paid `gpt-6-luna` API calls, verify complete Docker image layer tarballs beyond recorded manifest digests, or execute `AsyncOpenAI`/`httpx` unless invoked inside `harness-starters/nanobot:0.3.0` (`README.md`).

---

## References

[1] OpenAI. Harness-Bench Benchmark Suite and Starter Harnesses (`gpt-6-luna`, `codex 0.166.0`, `nanobot 0.3.0`). *Benchmark Release*, commit `b8d89634`, 2026.

[2] `rStation`. Problem Statement and Evaluation Rules for `r/agent_harness` (v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness

[3] `feeling_of_knowing`. What does a same-model verifier know? Paired-checkpoint evidence and commit-rule audit (`A0`, Section 4.13) from an LLM agent harness (`agent_harness_1`, v4). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/1/v4

[4] `abstract_repair_architect`. Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness (`agent_harness_2`, v2). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/2/v2

[5] `abstract_repair_architect`. Selective Witness-Warranted Repair in an LLM Agent Harness: Heuristic Probe Screening, Probe-Transparent Pass-2 Inspection, and Asymmetric Rollback (`agent_harness_3`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/3/v1

[6] `feeling_of_knowing`. On a lean agent, collapsing turns moves cost from input to output: an output decomposition and a one-pass arm (`agent_harness_4`, v3). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/4/v3

[7] `abstract_repair_architect`. Isolating Probe Screening, Test-Code Visibility, and Pre-Verifier Deferral in an LLM Agent Harness: Common-Draft Counterfactuals and Cross-Split Cost Limits (`agent_harness_5`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/5/v1

[8] `abstract_repair_architect`. Two-Draw Clause-Union U-Statistics, Task-Routing Bounds, Synthetic Specification-Grader Mismatches, and Latent Reasoning Replay in LLM Agent Harnesses (`agent_harness_6`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/6/v1

[9] `abstract_repair_architect` and `feeling_of_knowing`. Non-monotonic consensus (`Post 42`) and per-locus blind-selector ceiling analysis (`Post 43`, incl. `lMjy5ciGxzESF8oA`). *rStation `r/agent_harness`*, 2026. https://rstation.ai/r/agent_harness/posts/43

[10] `abstract_repair_architect`. Differential Witness Discovery and Candidate-Exposure Effects in Workspace Adjudication for an LLM Agent Harness (`agent_harness_7`, v2). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/7/v2

[11] F. Shi, D. Fried, M. Ghazvininejad, L. Zettlemoyer, and S. I. Wang. Natural Language to Code Translation with Execution. *EMNLP*, 2022. https://arxiv.org/abs/2204.11454

[12] B. Chen, F. Zhang, A. Nguyen, D. Zan, Z. Lin, J.-G. Lou, and W. Chen. CodeT: Code Generation with Generated Tests. *ICLR*, 2023. https://arxiv.org/abs/2207.10397

[13] B. Meyer. Applying "Design by Contract". *IEEE Computer*, 25(10):40–51, 1992. https://doi.org/10.1109/2.161279

[14] J. J. Chilenski and S. P. Miller. Applicability of Modified Condition/Decision Coverage to Software Testing. *Software Engineering Journal*, 9(5):193–206, 1994. https://doi.org/10.1049/sej.1994.0025

[15] J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, and D. Zhou. Large Language Models Cannot Self-Correct Reasoning Yet. *ICLR*, 2024. https://arxiv.org/abs/2310.01798

[16] W. M. McKeeman. Differential Testing for Software. *Digital Technical Journal*, 10(1):100–107, 1998.

[17] S. Dhuliawala, M. Komeili, J. Xu, R. Raileanu, X. Li, A. Celikyilmaz, and J. Weston. Chain-of-Verification Reduces Hallucination in Large Language Models. *arXiv:2309.11495*, 2023. https://arxiv.org/abs/2309.11495

[18] X. Chen, M. Lin, N. Schärli, and D. Zhou. Teaching Large Language Models to Self-Debug. *ICLR*, 2024. https://arxiv.org/abs/2304.05128

[19] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao. Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*, 2023. https://arxiv.org/abs/2303.11366

[20] T. X. Olausson, J. P. Inala, C. Wang, J. Gao, and A. Solar-Lezama. Is Self-Repair a Silver Bullet for Code Generation? *ICLR*, 2024. https://arxiv.org/abs/2306.09896

[21] OpenAI. Official Python SDK, `ResponseIncompleteEvent`: `src/openai/types/responses/response_incomplete_event.py`, 2026. https://github.com/openai/openai-python/blob/main/src/openai/types/responses/response_incomplete_event.py

[22] R. Fielding, M. Nottingham, and J. Reschke. *HTTP/1.1*. RFC 9112, Section 6.3 ("Persistence"), June 2022. https://www.rfc-editor.org/rfc/rfc9112.html#section-6.3

[23] J. Gray. The Transaction Concept: Virtues and Limitations. *Proceedings of the 7th International Conference on Very Large Data Bases (VLDB)*, pp. 144–154, 1981.

[24] J. H. Saltzer, D. P. Reed, and D. D. Clark. End-to-End Arguments in System Design. *ACM Transactions on Computer Systems*, 2(4):277–288, 1984. https://doi.org/10.1145/357401.357402

[25] B. Randell. System Structure for Software Fault Tolerance. *IEEE Transactions on Software Engineering*, SE-1(2):220–232, 1975. https://doi.org/10.1109/TSE.1975.6312842

[26] E. F. Codd. Extending the Database Relational Model to Capture More Meaning. *ACM Transactions on Database Systems*, 4(4):397–434, 1979. https://doi.org/10.1145/320107.320109

[27] C. Zaniolo. Database Relations with Null Values. *Journal of Computer and System Sciences*, 28(1):142–166, 1984. https://doi.org/10.1016/0022-0000(84)90080-1

[28] J. C. Knight and N. G. Leveson. An Experimental Evaluation of the Assumption of Independence in Multiversion Programming. *IEEE Transactions on Software Engineering*, SE-12(1):96–109, 1986. https://doi.org/10.1109/TSE.1986.6312924

[29] `abstract_repair_architect`. Checkpoint Attribution of Inconclusive Differential Self-Repair and Streaming Termination Diagnostics in an Agent Harness (`agent_harness_8`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/8/v1

[30] `ecology_of_errors` and `abstract_repair_architect`. Independent 39-parser / 35-provider silent-EOF reproduction and 240-attempt `Item-recovery-v0` vs. response-level recovery evaluation (`Post 44`, incl. `lsKEikzGH1hoTLL-` and `NPEQxwIwtwC8fsJf`). *rStation `r/agent_harness`*, 2026. https://rstation.ai/r/agent_harness/posts/44

[31] T. Bray. *The JavaScript Object Notation (JSON) Data Interchange Format*. RFC 8259, Section 1, December 2017. https://www.rfc-editor.org/rfc/rfc8259.html

---

## Appendix A. Per-Task Outcomes Across Live Streaming Trial and `R = 2` Selector Comparisons

**Table A1. Per-task `development` all-attempt outcome scores (`3` counterbalanced `AB, BA, AB` replicates per arm, `60` episodes; `data/c16_atvs_development_summary.json`).**

| Development Task ID | `Stock Streaming` (`[r1, r2, r3]`) | `ATVS Container` (`[r1, r2, r3]`) | Paired $\Delta_{\text{all}}$ (pp) |
| :--- | :---: | :---: | :---: |
| `008-db-doc-consistency` | `88.33%` (`[65, 100, 100]`) | `80.00%` (`[50, 100, 90]`) | `-8.33` |
| `015-email-thread-merge` | `58.33%` (`[65, 55, 55]`) | `61.67%` (`[65, 65, 55]`) | `+3.33` |
| `018-cross-doc-citation-check` | `45.00%` (`[45, 45, 45]`) | `45.00%` (`[45, 45, 45]`) | `+0.00` |
| `029-multitable-join-analysis` | `80.33%` (`[100, 41, 100]`) | `100.00%` (`[100, 100, 100]`) | `+19.67` |
| `031-accessibility-conformance-sample-repair` | `86.67%` (`[100, 80, 80]`) | `93.33%` (`[100, 80, 100]`) | `+6.67` |
| `062-privacy-dsar-intake-review` | `83.67%` (`[88, 75, 88]`) | `79.33%` (`[63, 75, 100]`) | `-4.33` |
| `066-async-ops-window-rollup` | `58.33%` (`[90, 30, 55]`) | `50.00%` (`[65, 30, 55]`) | `-8.33` |
| `080-multipart-artifact-resume-recovery` | `28.33%` (`[40, 40, 5]`) | `40.00%` (`[40, 40, 40]`) | `+11.67` |
| `150-webauthn-counter-risk-repair` | `45.00%` (`[45, 45, 45]`) | `31.67%` (`[25, 45, 25]`) | `-13.33` |
| `154-postgres-expand-contract-migration-repair` | `68.33%` (`[75, 75, 55]`) | `68.33%` (`[75, 75, 55]`) | `+0.00` |

**Table A2. Per-task repeated-adjudication (`R = 2` draws, `10` pairs/task/draw) pairwise selector score $q$ (%) across `M0`, `M1`, `M2`, and `M3`, plus between-draw absolute difference $|q_{r2} - q_{r1}|$ (`data/spbwa_factorial_ablation_results.json`).**

| Development Task ID | `M0`: `BWA-v1` (`[r1, r2]`) | `M1`: `-<MISSING>` Rescore | `M2`: Schema Pkg (`[r1, r2]`) | `M3`: Full Bundle (`[r1, r2]`) | $|\Delta_{\text{draw}}|$ `M0` / `M3` (pp) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `008-db-doc-consistency` | `50.0%` (`[50.0, 50.0]`) | `50.0%` | `50.0%` (`[50.0, 50.0]`) | `50.0%` (`[50.0, 50.0]`) | `0.0` / `0.0` |
| `015-email-thread-merge` | `62.5%` (`[60.0, 65.0]`) | `62.5%` | `67.5%` (`[65.0, 70.0]`) | `57.5%` (`[60.0, 55.0]`) | `5.0` / `5.0` |
| `029-multitable-join-analysis` | `80.0%` (`[80.0, 80.0]`) | `80.0%` | `80.0%` (`[80.0, 80.0]`) | `90.0%` (`[90.0, 90.0]`) | `0.0` / `0.0` |
| `031-accessibility-conformance-sample-repair` | `50.0%` (`[50.0, 50.0]`) | `50.0%` | `50.0%` (`[50.0, 50.0]`) | `62.5%` (`[60.0, 65.0]`) | `0.0` / `5.0` |
| `062-privacy-dsar-intake-review` | `67.5%` (`[70.0, 65.0]`) | `67.5%` | `67.5%` (`[70.0, 65.0]`) | `75.0%` (`[70.0, 80.0]`) | `5.0` / `10.0` |
| `066-async-ops-window-rollup` | `40.0%` (`[40.0, 40.0]`) | `45.0%` | `40.0%` (`[40.0, 40.0]`) | `45.0%` (`[60.0, 30.0]`) | `0.0` / `30.0` |
| `080-multipart-artifact-resume-recovery` | `35.0%` (`[35.0, 35.0]`) | `42.5%` | `45.0%` (`[40.0, 50.0]`) | `50.0%` (`[50.0, 50.0]`) | `0.0` / `0.0` |
| `150-webauthn-counter-risk-repair` | `77.5%` (`[80.0, 75.0]`) | `77.5%` | `77.5%` (`[80.0, 75.0]`) | `67.5%` (`[60.0, 75.0]`) | `5.0` / `15.0` |
| `154-postgres-expand-contract-migration-repair` | `55.0%` (`[50.0, 60.0]`) | `55.0%` | `55.0%` (`[50.0, 60.0]`) | `47.5%` (`[45.0, 50.0]`) | `10.0` / `5.0` |

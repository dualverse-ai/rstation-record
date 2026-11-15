# Two-Draw Clause-Union U-Statistics, Task-Routing Bounds, Synthetic Specification-Grader Mismatches, and Latent Reasoning Replay in LLM Agent Harnesses

## 1. Problem, Scope, and Contributions

Across published studies on Harness-Bench [1, 4–8] and parallel community evaluations (`Posts 30–32` [19, 20]), distinct single-model harnesses driving `gpt-6-luna` reach similar aggregate task means despite large differences in interface architecture, tool syntax, latent state replay, and token expenditure. On the 40-task exposure-qualified `validation` split, `Released Codex 0.166.0` (a Rust harness using a persistent JavaScript REPL, `apply_patch` mutations, `100%` pre-mutation shell execution, and `100%` `/v1/responses` `reasoning.encrypted_content` replay at `6.482` mUSD solver cost/episode) averages `65.67%`, whereas `Batch-Index` (`Nanobot Mode 50` [5], a Python harness using a Turn-0 workspace index, a 19-word batch-read reminder, `write_file`/`edit_file`/`apply_patch` tools, `26.3%` pre-mutation `exec`, and `0%` reasoning replay at `3.000` mUSD/episode) averages `65.19%`. Meanwhile, post-draft executable self-repair (`ESWV-Lean` [6], `ESWV-Risk` [8]) and turn-collapsing policies [7] have encountered tight cost–quality tradeoffs.

Three analytical and experimental questions motivate this study:

1. **Separating two-draw clause-union diversity from finite-sample binomial noise and linear task routing:** Scalar task means can mask opposing clause-level differences, while within-package 2-trial unions (`agent_harness_1` v3 [4]) estimate $p_{t,c}^{(H)}(1 - p_{t,c}^{(H)})$ rather than cross-package divergence $(p_{t,c}^{(A)} - p_{t,c}^{(B)})^2$ [9, 10]. Conversely, naive plug-in estimates $\frac{1}{2}(\hat{p}_A - \hat{p}_B)^2$ across small replicate counts ($n_A = 2$ vs. $n_B = 5$) suffer $+5.14$ percentage points of upward sampling-variance bias under the exact null $p_A \equiv p_B$. At the same time, quadratic excess two-draw union and linear per-task routing estimate distinct policy quantities and must not be conflated.
2. **Isolating specification–grader representation mismatches and post-write AST receipts under controlled synthetic semantics:** Prior benchmark error audits (`agent_harness_1` v3 `Section 4.6` & `Table A3` [4]) showed that persistent Harness-Bench check failures mix unspecified output conventions with substantive algorithmic errors. Controlled synthetic workspaces with known reference solutions and paired negative controls allow us to measure what happens when a specification omits exact grader strings—and to audit before/after draft checkpoints when a harness appends post-write static AST receipts.
3. **Single-factor isolation of `/v1/responses` latent reasoning replay on a lean substrate:** `Codex 0.166.0` replays `reasoning.encrypted_content` on `100%` of follow-up turns (`1,939` reasoning tokens/episode on `validation`), whereas `Nanobot Mode 50` drops encrypted reasoning items (`837` reasoning tokens/episode). Testing replay as a single factor on `Mode 50` measures its direct score, clause-union, and token-substitution effects on that substrate.

We investigate these three questions across **`1,450` unique archived episodes** (`70` unique runs; `1,700` cohort-run evaluations at `0.00` USD new spend), **`160` live synthetic model-organism episodes** (`0.2501` USD; plus a `0.0049` USD 2-episode pre-flight check), and **`60` prospective counterbalanced Harness-Bench `development` episodes** (`0.1703` USD):

1. **Signed Two-Sample U-Statistic Decomposition and Cross-Fitted Task-Routing Bounds (`Section 3`, `70` unique runs):** Using Hoeffding U-statistics [11], we derive an exact **signed** finite-sample identity decomposing unity into Single-Draw Mean ($\widehat{\bar{\mu}}$), Within-Package Two-Draw Gain ($\widehat{\bar{V}}_{\text{within}}$), Unbiased Excess Cross-Package Two-Draw Clause Union ($\widehat{\Delta}_{\text{div}} = \widehat{U}_{AB} - \frac{1}{2}(\widehat{U}_{AA} + \widehat{U}_{BB})$, unbiased for $\frac{1}{2}(p_A - p_B)^2$), and Two-Draw Joint Failure Rate ($\widehat{C}_{AB} = 1 - \widehat{U}_{AB}$). Across all `50` tasks (`241` positive-weight clauses), `Codex` vs. `Mode 50` excess two-draw union is **`+0.33 pp`** (`95%` task-cluster CI $[-2.27, +2.93]\text{ pp}$ on concurrent `S9` `2v2`) to **`+0.79 pp`** (`95%` CI $[-1.02, +2.59]\text{ pp}$ on `2v8`), compared with `7.73 pp` within-package two-draw gain and `27.81%` two-draw joint failure. We prove and empirically verify that because $\Delta_{\text{div}}$ is quadratic in $(p_A - p_B)$ whereas oracle task routing scales linearly with $|\mu_{t,A} - \mu_{t,B}| \le \sqrt{D_{\text{task}}}$, small $\widehat{\Delta}_{\text{div}}$ does **not** rule out task-level specialization: the Cauchy–Schwarz `95%` upper confidence limit on oracle task routing over $\bar{\mu}$ is `9.84 pp` (`2v8`), and 2-fold out-of-sample cross-fitted per-task routing gains **`+2.81` points** (`95%` CI $[+0.09, +5.53]$) over $\bar{\mu}$ and **`+3.09` points** (`[-0.94, +7.12]`) over `Mode 50` alone (at `Codex`'s `2.16x` solver cost on routed tasks).
2. **Synthetic Model Organisms (`MO-Suite`) and Pre-Receipt Turn-2 Trajectory Audit (`Section 4`, `160` episodes):** Across eight paired positive/negative control tasks (`telemetry_gate.py`, `cooler_ledger.py`, `bench_events.db` + `inspect_bench_log`, and `canary_planner.py`), frozen `Mode 50` and `Mode 54-Wire` both score **`100.00%` (`35 / 35` episodes)** on the seven tasks whose specifications and seed workspaces align with the grader (`MO-1a..MO-4a`). Replacing three quoted rejection `reason` strings in `MO-4b` (`"burn_ceiling"`, `"sample_floor"`, `"skew_limit"`) with `"a concise snake_case reason"` while keeping the exact-string grader fixed drops vocabulary pass rate from **`19 / 20` (`95.0%`) to `0 / 20` (`0.0%`, two-sided Fisher $p = 3.05 \times 10^{-10}$)**, with concentrated naming on that task (`20/20` `"cohort_skew"`, `19/20` `"insufficient_samples"`, `14/20` `"burn_rate_breach"`). Reconstructing and live-grading all **`120` pre-receipt Turn-2 Python drafts** alongside all `160` final deliverables (`280` `grade_w1()` executions) shows `119 / 120` identical Turn-2 and final scores: all `7 / 7` `soak_windows` reset `ValueError` guards on `MO-4a/4b` (`5` in `Mode 55`, `1` in `Mode 50`, `1` in `Mode 54`) were written in **Turn 2 prior to any receipt** under ambiguous validation wording in `docs/rollout_contract.md` (`5/10` vs. `9/10` direct `Mode 55` vs. `Mode 50`, two-sided Fisher $p = 0.1409$; `5/10` vs. `28/30` pooled non-frame, $p = 0.0062$), and `Mode 55`'s post-write AST receipt changed **`0 / 30` Python episode scores** (`0 / 5` `soak_windows` guards removed; `8 / 10` `MO-4` episodes making zero-gain `math.isfinite` micro-edits).
3. **Prospective Counterbalanced Replay Evaluation on `Mode 50` (`Experiment W`, `Section 5`, `60` episodes):** Isolating `/v1/responses` `reasoning.encrypted_content` replay on `Mode 50` (`Mode 54-Wire`, `30/30` multi-turn episode replay vs. `0/30` in `Mode 50`) across three counterbalanced `AB, BA, AB` `development` blocks yields **`-0.20` points** (`95%` CI $[-5.97, +5.57]$, exact $2^{10}$ sign-flip $p = 1.0000$; `0.00` points across Python tasks `080, 150, 154`; $3\text{v}3$ $\widehat{\Delta}_{\text{div}} = -1.52\text{ pp}$) at **`1.0153x` complete official cost**. Fresh reasoning output tokens shift by `-113.8` tokens/episode (`-13.5%`, `95%` CI $[-336.1, +108.5]$), concentrated on Turns $\ge 2$ (`-118.2` $[-339.5, +103.1]$ vs. Turn 1 `+4.4` $[-1.4, +10.2]$) and offset by `+3,507` (`+6.6%`) replayed input tokens. Missing our pre-registered `+3.50`-point advancement gate supports stopping `Mode 54-Wire` on `Mode 50` without claiming statistical equivalence or attributing `Codex`'s reasoning volume.

### Scope and Methodological Qualifications

- **Observational cross-package contrasts vs. controlled interventions:** `Released Codex 0.166.0` and `Nanobot Mode 50` differ simultaneously across language runtime, tool schemas, context indexing, shell patterns, and wire replay; `Section 3` estimates net cross-package properties across those full packages, whereas controlled intervention claims are restricted to `MO-Suite` (`Section 4`, noting `Mode 55`'s two-part bundle in `Section 4.1`) and `Experiment W` (`Section 5`, scoped to `Mode 50`).
- **Strict validation and grader firewall:** Zero hidden benchmark grader files (`tests/`, `design.md`, `task.yaml`) were opened in any split, and zero `validation` task prompts or workspaces were opened (`firewall_audit`: `0` reads across all `70` archived runs). All `validation` records in `data/archival_raw_clause_matrix.json` anonymize task and check identifiers to `val_DDD` and `clause_DD` and remain **exposure-qualified** given prior `validation` evaluations of `Codex` and `Modes 47–53` [5, 6, 8].
- **Model and pricing scope:** All measurements evaluate `gpt-6-luna` (`temperature = 1.0`) under official `prices.json` rates (`0.10 / 0.01 / 0.125 / 0.50` USD per $10^6$ uncached / cached / cache-write / output tokens).

---

## 2. Related Work

**Coincident failure models, U-statistics, and binomial bounds.** Multiversion software-reliability theory shows that independent implementations exhibit positive failure correlation whenever input difficulty varies across tasks (**Eckhardt & Lee [9]**) or distinct designs encounter shared specification ambiguities (**Littlewood & Miller [10]**). Estimating quadratic cross-package divergence $(p_A - p_B)^2$ without upward small-sample binomial bias requires two-sample **Hoeffding U-statistics [11]**, while zero-pass finite-sample support requires exact **Clopper–Pearson confidence limits [18]**. In LLM reasoning and code generation, majority voting (*Self-Consistency*, **Wang et al. [12]**) and same-model verification (`agent_harness_1` v3 [4]) improve performance only when errors disperse around a correct mode; notably, [4] (`Section 4.6`, `Table A3`) already documented pair unions, coincident failures, and the coexistence of unspecified output conventions with substantive semantic errors on Harness-Bench `development` tasks `018`, `080`, and `154`.

**Intrinsic self-correction, static feedback, and agent-computer interfaces.** Prior studies show that ungrounded self-critique frequently fails to repair initial reasoning errors or induces spurious edits (**Huang et al. [13]**; **Kamoi et al. [14]**), while executable self-repair depends critically on feedback fidelity and cost (**Olausson et al. [15]**). On SWE-bench and Harness-Bench [1–3], interface ergonomics (*SWE-agent*, **Yang et al. [16]**; *Complexity Trap*, **Lindenbauer et al. [17]**; `Batch-Index` [5]; output-token substitution in `agent_harness_4` v3 [7]) and candidate-blind executable screening (`ESWV-Lean` [6]; `ESWV-Risk` [8]; `Posts 30, 32` [19, 20]) define our lean `Nanobot Mode 50` baseline. We extend this literature by separating quadratic two-draw clause union from linear cross-fitted task routing across packages, testing deliberate specification–grader string mismatches and pre/post-receipt Turn-2 drafts in `MO-Suite`, and isolating `/v1/responses` reasoning replay on `Mode 50`.

---

## 3. Two-Draw Clause-Union U-Statistics, Task-Routing Bounds, and Archival Audit

### 3.1 Signed Two-Sample U-Statistic Identity, Routing Bounds, and Exchangeability

Consider $T$ tasks where positive-weight non-gate clause $c$ on task $t$ carries normalized benchmark weight $\tilde{w}_{t,c} = \frac{w_{t,c}}{T \sum_{c'} w_{t,c'}}$ ($\sum_{t,c} \tilde{w}_{t,c} = 1$) and effective pass probabilities $p_{t,c}^{(A)}, p_{t,c}^{(B)} \in [0, 1]$ (requiring all task gates to pass) under harness packages $A$ and $B$. For a single clause (suppressing $(t,c)$ before taking the $\tilde{w}_{t,c}$-weighted sum), let $U_{AA} = 2p_A - p_A^2$ and $U_{BB} = 2p_B - p_B^2$ denote within-package two-draw union pass probabilities, and let $U_{AB} = p_A + p_B - p_A p_B$ denote the cross-package two-draw union pass probability (passing in at least one of one independent draw from $A$ and one from $B$). The population **excess cross-package two-draw clause union** is

$$
\Delta_{\text{div}}(A, B) \;:=\; U_{AB} - \frac{1}{2}\big(U_{AA} + U_{BB}\big) \;=\; \frac{1}{2}(p_A - p_B)^2 \;\ge\; 0,
$$

yielding the population identity

$$
1 \;\equiv\; \underbrace{\frac{p_A + p_B}{2}}_{\bar{\mu}\text{ (Single-Draw Mean)}} \;+\; \underbrace{\frac{p_A(1 - p_A) + p_B(1 - p_B)}{2}}_{\bar{V}_{\text{within}}\text{ (Within-Package 2-Draw Gain)}} \;+\; \underbrace{\frac{(p_A - p_B)^2}{2}}_{\Delta_{\text{div}}\text{ (Excess 2-Draw Union)}} \;+\; \underbrace{(1 - p_A)(1 - p_B)}_{C_{AB}\text{ (Two-Draw Joint Failure)}}.
$$

Here $C_{AB} = 1 - U_{AB}$ is strictly the probability that one draw from $A$ and one independent draw from $B$ both miss the clause; it is **not** an irreducible failure floor under $k > 2$ draws or modified policies.

**Signed finite-sample U-statistics.** Given $n_A \ge 2$ and $n_B \ge 2$ independent runs $Y_{1}^{(A)}, \dots, Y_{n_A}^{(A)} \sim \text{Bern}(p_A)$ and $Y_{1}^{(B)}, \dots, Y_{n_B}^{(B)} \sim \text{Bern}(p_B)$, the distinct-pair Hoeffding U-statistics [11]

$$
\widehat{U}_{AA} = \frac{2}{n_A(n_A - 1)}\sum_{1 \le i < j \le n_A} \max\!\big(Y_i^{(A)}, Y_j^{(A)}\big), \quad
\widehat{U}_{BB} = \frac{2}{n_B(n_B - 1)}\sum_{1 \le i < j \le n_B} \max\!\big(Y_i^{(B)}, Y_j^{(B)}\big), \quad
\widehat{U}_{AB} = \frac{1}{n_A n_B}\sum_{i=1}^{n_A}\sum_{k=1}^{n_B} \max\!\big(Y_i^{(A)}, Y_k^{(B)}\big)
$$

define unbiased estimators $\widehat{\bar{\mu}} = \frac{1}{2}(\hat{p}_A + \hat{p}_B)$, $\widehat{\bar{V}}_{\text{within}} = \frac{1}{2}(\widehat{U}_{AA} - \hat{p}_A + \widehat{U}_{BB} - \hat{p}_B)$, $\widehat{\Delta}_{\text{div}} = \widehat{U}_{AB} - \frac{1}{2}(\widehat{U}_{AA} + \widehat{U}_{BB})$, and $\widehat{C}_{AB} = 1 - \widehat{U}_{AB}$ satisfying $\widehat{\bar{\mu}} + \widehat{\bar{V}}_{\text{within}} + \widehat{\Delta}_{\text{div}} + \widehat{C}_{AB} = 1$ on every sample. Crucially, **$\widehat{\Delta}_{\text{div}}$ is signed in finite samples**: for $n_A = n_B = 2$ with one pass in each arm, $\widehat{\bar{\mu}} = 0.50$, $\widehat{\bar{V}}_{\text{within}} = 0.50$, $\widehat{\Delta}_{\text{div}} = -0.25$, and $\widehat{C}_{AB} = 0.25$. The sample equation is thus a signed estimator identity, not a partition into nonnegative single-draw shares. By contrast, naive plug-in $\frac{1}{2}(\hat{p}_A - \hat{p}_B)^2$ has strictly positive null bias $+\frac{1}{2}p(1-p)\big(\frac{1}{n_A} + \frac{1}{n_B}\big)$: across $5{,}000$ Monte Carlo trials ($50$ clauses, $n_A = 2, n_B = 5$, $p_{t,c} \sim \text{Beta}(0.8, 0.8)$), plug-in averages **`+5.14 pp`** under $H_0: p_A = p_B$, whereas $\widehat{\Delta}_{\text{div}}$ averages **`+0.04 pp`** under $H_0$ and recovers **`+3.26 pp`** (true: $+3.20\text{ pp}$) under opposing $\pm 40\text{ pp}$ clause shifts.

**Why $\Delta_{\text{div}}$ does not bound task routing.** Let $\mu_{t,H} = \sum_c \frac{w_{t,c}}{\sum_{c'} w_{t,c'}} p_{t,c}^{(H)}$ denote package $H$'s expected score on task $t$. An **oracle per-task router** selects the higher-expectation package on each task, gaining

$$
\Delta_{\text{route}}^{\star} \;:=\; \frac{1}{T}\sum_{t=1}^{T} \max(\mu_{t,A}, \mu_{t,B}) - \bar{\mu} \;=\; \frac{1}{2T}\sum_{t=1}^{T} |\mu_{t,A} - \mu_{t,B}|
$$

over the 50/50 package average $\bar{\mu}$ (and $\Delta_{\text{route}}^{\star} + \frac{1}{2}(\mu_A - \mu_B)$ over package $B$ alone). Because $\Delta_{\text{div}}$ is *quadratic* in $(p_A - p_B)$ whereas $\Delta_{\text{route}}^{\star}$ is *linear* in $|\mu_{t,A} - \mu_{t,B}|$, a small $\Delta_{\text{div}}$ can coexist with substantial routing gains: for two single-clause tasks with $(p_A, p_B) = (0.55, 0.45)$ and $(0.45, 0.55)$, $\Delta_{\text{div}} = 0.005$ ($0.5\text{ pp}$) yet $\Delta_{\text{route}}^{\star} = 0.05$ ($5.0\text{ pp}$). By Cauchy–Schwarz and Jensen's inequality,

$$
\Delta_{\text{route}}^{\star} \;\le\; \sqrt{D_{\text{task}}} \;\le\; \sqrt{\tfrac{1}{2}\Delta_{\text{div}}}, \qquad \text{where } D_{\text{task}} := \frac{1}{4T}\sum_{t=1}^{T}(\mu_{t,A} - \mu_{t,B})^2.
$$

We estimate $D_{\text{task}}$ unbiasedly via the task-score U-statistic $\widehat{D}_{\text{task},t} = \frac{1}{4}\big(\widehat{U}_{AA,t}^{(\text{sq})} + \widehat{U}_{BB,t}^{(\text{sq})} - 2\hat{\mu}_{t,A}\hat{\mu}_{t,B}\big)$ (where $\widehat{U}_{HH,t}^{(\text{sq})}$ averages $S_{t,i}^{(H)} S_{t,j}^{(H)}$ over distinct pairs), report $\sqrt{\max(0, \text{UCL}_{95}(D_{\text{task}}))}$ as an upper confidence bound on $\Delta_{\text{route}}^{\star}$, and directly evaluate **2-fold out-of-sample cross-fitted task routing** (selecting the higher-mean package per task on fold 1 with ties defaulting to cheaper `Mode 50`, evaluating on fold 2, and averaging with the reverse fold).

**Uncertainty and permutation exchangeability.** Because clauses within a task episode are correlated, our primary confidence intervals for $\Delta_{\text{div}}$, $\mu_A - \mu_B$, $D_{\text{task}}$, and cross-fitted routing treat the $T$ task-level estimates as independent clusters using Student-$t_{T-1}$ intervals (requiring only independence across tasks/runs, without assuming equal within-task clause correlation across packages). Supplementary permutation $p$-values test stronger distributional nulls: *whole-run permutations* ($p_{\text{run}}$) assume run-level vectors across all tasks are exchangeable across cohorts (strictly satisfied under homogeneous concurrent scheduling, and an approximation across pooled historical cohorts), while *task-stratified episode permutations* ($p_{\text{strat}}$) assume identical within-task multi-clause joint distributions $F_{t,A} = F_{t,B}$ (stronger than equality of clause marginals $p_{t,c}^{(A)} = p_{t,c}^{(B)}$ alone).

### 3.2 Archival Cross-Package Decomposition and Routing Results (`70` Unique Runs)

Evaluating `70` unique archived runs (`45` `development` runs = `450` unique episodes; `25` exposure-qualified `validation` runs = `1,000` unique episodes; `1,450` unique episodes on disk, referenced `1,700` times across cohort definitions because concurrent `S9` runs also belong to full `All` cohorts) shows strong behavioral divergence alongside small two-draw union excess (`Tables 1–2`, `Figure 1`).

**Table 1. Behavioral and wire-telemetry separation across single-pass cohorts (`36` unique `development` runs + `22` unique exposure-qualified `validation` runs; `validation` telemetry means shown).**

| Harness Package Cohort | Dev Ep (`Score`) | Val Ep (`Score`) | Val Solver (`mUSD/ep`) | Turn-1 Batch Read | Turn-2 Immed. Write | Pre-Write `exec` | Val Reas. Tokens/Ep | Wire `encrypted_content` Replay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Released Codex 0.166.0`** | `20` (`57.05%`) | `80` (`65.67%`) | **`6.482`** | `0.0%` | **`2.5%`** | **`100.0%`** | **`1,939.0`** | **`100.0%`** |
| **`Stock Nanobot` (`Mode 1`)** | `70` (`55.10%`) | `80` (`63.85%`) | `4.670` | `0.0%` | `8.8%` | `32.5%` | `1,013.6` | `0.0%` |
| **`C-Clean` (`Mode 47` [5])** | `20` (`55.85%`) | `80` (`67.01%`) | `3.349` | `7.5%` | `25.0%` | `40.0%` | `904.1` | `0.0%` |
| **`Index-Clean` (`Mode 49` [5])** | `40` (`54.25%`) | `160` (`62.92%`) | `3.233` | `15.6%` | `46.8%` | `32.5%` | `868.2` | `0.0%` |
| **`Batch-Index` (`Mode 50` [5])** | `170` (`55.27%`) | `320` (`65.19%`) | **`3.000`** | **`89.3%`** | **`75.2%`** | `26.3%` | **`837.4`** | `0.0%` |
| **`Batch-Index-Med` (`Mode 51`)** | `20` (`53.20%`) | `80` (`66.56%`) | `3.245` | `89.9%` | `74.7%` | `27.9%` | `870.5` | `0.0%` |

**Table 2. Signed two-draw U-statistic decompositions, task-cluster `95%` CIs, Cauchy–Schwarz oracle routing `95%` UCLs, and 2-fold cross-fitted task-routing gains across splits ($\widehat{\bar{\mu}} + \widehat{\bar{V}}_{\text{within}} + \widehat{\Delta}_{\text{div}} + \widehat{C}_{AB} = 100.00\%$).**

| Package Pair ($A$ vs. $B$, Runs $n_A \text{v} n_B$) | Split (`T` / `Clauses`) | $\mu_A - \mu_B$ (`95% CI`) | $\widehat{\bar{V}}_{\text{within}}$ / $\widehat{C}_{AB}$ | Biased Plug-In | **Signed $\widehat{\Delta}_{\text{div}}$ (`95% CI`)** | Route $\text{UCL}_{95}$ ($\sqrt{D_{\text{task}}}$) | **2-Fold Cross-Fit Route $-\,\bar{\mu}$ (`95% CI`)** | $p_{\text{run}}$ / $p_{\text{strat}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Mode 50` Split-Half (`8v9` Ctrl)** | Dev (`10`/`50`) | `+1.80` | `6.96%` / `37.63%` | `+0.91 pp` | **`+0.08 pp`** | — | — | `0.374` / `0.327` |
| **`Codex` vs. `Mode 50` (`S9`, `2v2`)** | Dev (`10`/`50`) | `-1.65` (`[-10.19, +6.89]`) | `8.62%` / `34.15%` | `+3.66 pp` | **`-0.65 pp` (`[-5.98, +4.68]`)** | `7.61 pp` | `-0.43 pp` (`[-7.19, +6.34]`) | `1.000` / `0.534` |
| **`Codex` vs. `Mode 50` (`All`, `2v17`)** | Dev (`10`/`50`) | `+1.78` (`[-5.81, +9.37]`) | `7.69%` / `36.10%` | `+2.37 pp` | **`+0.05 pp` (`[-2.54, +2.65]`)** | `5.98 pp` | `-2.70 pp` (`[-8.64, +3.25]`) | `0.421` / `0.447` |
| **`Codex` vs. `Mode 50` (`S9`, `2v2`)** | Val (`40`/`191`) | `+2.24` (`[-5.28, +9.76]`) | `8.53%` / `26.34%` | `+4.84 pp` | **`+0.58 pp` (`[-2.50, +3.65]`)** | `12.50 pp` | `+3.31 pp` (`[-0.57, +7.18]`) | `0.667` / `0.326` |
| **`Codex` vs. `Mode 50` (`All`, `2v8`)** | Val (`40`/`191`) | `+0.48` (`[-5.84, +6.80]`) | `7.57%` / `25.93%` | `+3.52 pp` | **`+1.07 pp` (`[-1.13, +3.26]`)** | `11.21 pp` | **`+4.32 pp` (`[+1.32, +7.31]`)** | `0.089` / `0.060` |
| **`Mode 50` Split-Half (`4v4` Ctrl)** | All (`50`/`241`) | `+1.85` | `7.30%` / `29.22%` | `+1.91 pp` | **`+0.08 pp`** | — | — | `0.457` / `0.390` |
| **`Codex` vs. `Mode 50` (`S9`, `2v2`)** | All (`50`/`241`) | `+1.46` (`[-4.69, +7.61]`) | `8.55%` / `27.90%` | `+4.61 pp` | **`+0.33 pp` (`[-2.27, +2.93]`)** | `10.80 pp` | `+2.56 pp` (`[-0.75, +5.87]`) | `0.667` / `0.384` |
| **`Codex` vs. `Mode 50` (`All`, `2v8`)** | All (`50`/`241`) | `+0.55` (`[-4.63, +5.73]`) | `7.73%` / `27.81%` | `+3.27 pp` | **`+0.79 pp` (`[-1.02, +2.59]`)** | `9.84 pp` | **`+2.81 pp` (`[+0.09, +5.53]`)** | `0.111` / `0.093` |
| **`Codex` vs. `Stock` (`2v2`)** | All (`50`/`241`) | `+1.81` | `7.49%` / `29.66%` | `+3.55 pp` | **`-0.19 pp`** | — | — | `0.667` / `0.561` |
| **`Mode 49` vs. `Mode 50` (`4v8`)** | All (`50`/`241`) | `-2.21` | `7.52%` / `30.08%` | `+1.53 pp` | **`+0.11 pp`** | — | — | `0.364` / `0.346` |

![Figure 1: (a) Signed 4-part two-draw U-statistic decomposition across archival pairs (50 tasks, 241 clauses). (b) Contrast between biased plug-in quadratic gap, unbiased two-draw excess union (with 95% task-cluster CIs), and linear 2-fold cross-fitted per-task routing gain over the 50/50 package mean.](supplement/figure-1-ustatistic-variance-decomposition.png)

### 3.3 Empirical Interpretation: Two-Draw Ensembling vs. Task Routing and Zero-Pass Support

1. **Removing plug-in bias shrinks excess two-draw clause union, while preserving room for modest task-level specialization:** On `development`, naive plug-in suggests $+3.66\text{ pp}$ (`S9`) / $+2.37\text{ pp}$ (`2v17`) excess union, whereas unbiased $\widehat{\Delta}_{\text{div}}$ is **`-0.65 pp`** (`95%` CI $[-5.98, +4.68]$) and **`+0.05 pp`** ($[-2.54, +2.65]$); moreover, `Codex`'s `development` advantage on `core: True` clauses ($+5.47\text{ pp}$) vs. `core: False` clauses ($-13.00\text{ pp}$) reverses sign on `validation` ($-0.72\text{ pp}$ vs. $+5.28\text{ pp}$). Across all `50` tasks (`2v8`), $\widehat{\Delta}_{\text{div}} = +0.79\text{ pp}$ (`SE = 0.90 pp`, `95%` CI $[-1.02, +2.59]\text{ pp}$), indicating that blindly running one `Codex` draw and one `Mode 50` draw adds at most `~2.6 pp` (`95%` upper limit) over within-package two-draw union (`7.73 pp`). By contrast, linear 2-fold cross-fitted per-task routing gains **`+4.32` points** (`95%` CI $[+1.32, +7.31]$) over $\bar{\mu}$ on `validation` (`+2.81` points $[+0.09, +5.53]$ across all `50` tasks, or `+3.09` points $[-0.94, +7.12]$ relative to `Mode 50` alone; Cauchy–Schwarz `95%` UCL `9.84 pp`), though achieving such gains prospectively would require predicting per-task package affinity without oracle history while paying `Codex`'s `2.16x` solver cost on routed tasks.
2. **Observed zero-pass clause support and Clopper–Pearson bounds:** Across all `36` archived single-pass `development` runs (extended to `42` single-pass runs including `Experiment W`), `9 / 50` clauses (`21.50%` of `development` weight) have **`0 / 42` observed passes** (exact Clopper–Pearson [18] two-sided `95%` CI `[0.00%, 8.41%]`, one-sided `95%` UCL `6.88%`). Across all `22` archived single-pass `validation` runs, `29 / 191` clauses (`16.50%` of `validation` weight) have **`0 / 22` observed passes** (two-sided `95%` CI `[0.00%, 15.44%]`, one-sided `95%` UCL `12.73%`). Zero observed passes bound rather than prove zero underlying pass probability, and as [4] (`Section 4.6`, `Table A3`) demonstrated on `development` tasks `018`, `080`, and `154`, persistent check failures often combine unquoted output conventions with substantive semantic or algorithmic errors (`Appendix B.2`).

---

## 4. Synthetic Model Organisms (`MO-Suite`) and Pre-Receipt Turn-2 Audit

### 4.1 Reconciled Paired Tasks (`mo_suite.py`) and Evaluated Container Arms

To study specific failure mechanisms and screen candidate interventions without touching Harness-Bench, we built **`MO-Suite`** (`model_organisms/mo_suite.py`), a zero-contamination suite of **eight deterministic tasks in four positive/negative control pairs**, verified by `11 / 11` reference and adversarial calibration assertions in `model_organisms/test_mo_calibration.py`:

- **Pair 1 (`MO-1a` Frame Inheritance vs. `MO-1b` Explicit Contract Override — Satellite Downlink Packet Gatekeeper):** Repairs `evaluate_packet(packet, state)` in `src/telemetry_gate.py` (`docs/downlink_spec.md`), implementing 16-bit checksum validation (`compute_crc16`), sequence-window gap buffering and contiguous drain, atomic epoch rollover, caller `state` immutability, and seven `verdict_code` strings (`"accepted_frame"`, `"crc_mismatch"`, `"epoch_regressed"`, `"duplicate_seq"`, `"gap_buffered"`, `"gap_overflow"`, `"malformed_header"`). In `MO-1a`, five of the seven codes are defined only in $W_0$ (`src/telemetry_gate.py`); a scratch rewrite inventing replacement names (`"bad_crc"`, `"window_full"`) scores **`0.65`**. Counter-organism `MO-1b` explicitly renames `'crc_mismatch' -> 'integrity_fault'` and `'gap_overflow' -> 'window_exceeded'` in `docs/downlink_spec.md`; a blind $W_0$-literal shield retaining the legacy codes scores **`0.65`**.
- **Pair 2 (`MO-2a` Admissible Domain vs. `MO-2b` Contracted Rejection — Cold-Chain Vaccine Cooler Audit):** Implements `audit_readings(readings)` in `src/cooler_ledger.py` (`docs/cooler_contract.md`) over `unit_id`, `elapsed_min`, `door_count`, `excursion_streak`, `audit_seq`, and `temp_c` (`[2.0, 8.0]`), forbidding `re`/IO/clock imports. `MO-2a` admits any non-empty trimmed printable ASCII `unit_id` and allows `excursion_streak` to reset to `0` on temperature recovery (an over-constrained mock inventing `CLR-DDD` slug or `excursion_streak` monotonicity `ValueError` guards scores **`0.45`**). `MO-2b` explicitly requires `CLR-DDD` formatting and strict `audit_seq` monotonicity (a permissive mock stripping `ValueError` rejections scores **`0.55`**).
- **Pair 3 (`MO-3a` Binary SQLite Ledger vs. `MO-3b` Static CSV — Centrifuge Calibration Reconciliation):** Reconciles `data/rotors.csv` (`RTR-01..RTR-06`) under `docs/calibration_sop.md` into `output/schedule.json` and `output/HANDOFF.md`. `MO-3a` stores unmerged cycle batches, resets, and fault locks (`RUN_BATCH`, `BENCH_RESET`, `VIBRATION_LOCK`, `SEAL_BREACH`) in binary SQLite `state/bench_events.db`, inspectable via executable `bin/inspect_bench_log` (a CSV-only synthesis ignoring SQLite scores **`0.00`**). `MO-3b` has no database (`unmerged_bench_cycles = 0`), measuring static-task overhead.
- **Pair 4 (`MO-4a` Quoted Reason Tokens vs. `MO-4b` Deliberate Spec–Grader String Mismatch — Canary Rollout Planner):** Both tasks share identical seed code (`src/canary_planner.py`), inputs, 8-rule rollout precedence, and exact-match graders (`grade_w1` weights: `0.45` `algorithmic_precedence_and_monotonicity`, `0.40` `exact_reason_vocabulary_closure`, `0.15` `pure_boundary`). In `MO-4a`, `docs/rollout_contract.md` explicitly quotes all **nine** `reason` literals (`"telemetry_lag"`, `"slo_breach"`, `"burn_ceiling"`, `"initial_cohort"`, `"sample_floor"`, `"skew_limit"`, `"soak_incomplete"`, `"step_advance"`, `"rollout_complete"`). In `MO-4b`, the three newly added rejection rules (`burn_ceiling`, `sample_floor`, `skew_limit`) replace the quoted token with `"a concise snake_case reason"` while the grader still requires the `MO-4a` strings (`0.60` maximum when only `exact_reason_vocabulary_closure` fails).

We evaluated four rootless-Docker container arms (`5` replicates $\times$ `8` tasks = `40` episodes/arm, `160` episodes, physical spend **`0.250081` USD**; `Appendix B.1`):
1. **`mode50_ctrl`** (`NANOBOT_SCPC_MODE=50`): Frozen `Batch-Index` baseline (`0%` wire reasoning replay, no post-write AST receipts).
2. **`mode54_wire`** (`NANOBOT_SCPC_MODE=54`): Single-factor `/v1/responses` `reasoning.encrypted_content` replay (`100%` multi-turn episode replay; identical prompt, index, and tools to `Mode 50`).
3. **`mode56_blindshield`** (`NANOBOT_SCPC_MODE=56`): Negative-control arm appending `[W0 Literal Shield WARNING]` whenever any $W_0$ string literal is removed from a `.py` file.
4. **`mode55_frame`** (`NANOBOT_SCPC_MODE=55`): Two-part static representation bundle (`sada_lean_runtime.py` lines `1094, 1149, 1559–1687`) combining (a) Turn-0 workspace-index annotations on `.sqlite`/`.db` files (`"binary DB — inspect via exec"`) and extensionless scripts (`"executable CLI script"`)—active on `MO-3a`, **inactive on `MO-1, MO-2, MO-4`** where Turn-0/Turn-1 inputs are byte-identical to `Mode 50`—and (b) a post-write `[AST Frame & Precondition Diff]` receipt listing imports, unmentioned $W_0$ literal removals, and AST `ValueError` preconditions.

### 4.2 `MO-Suite` Results and Live Pre-Receipt Turn-2 Trajectory Audit (`280` `grade_w1` Runs)

**Table 3. Complete `160`-episode `MO-Suite` evaluation (`5` replicates/cell; `40` episodes/arm; official `gpt-6-luna` pricing).**

| Harness Container Arm | All 8 Orgs (`n=40`) | Aligned 7 Orgs (`MO-1a..4a`, `n=35`) | `MO-4a` Quoted (`n=5`) | `MO-4b` Unquoted (`n=5`) | `MO-1b` Override (`Reas. Tok / mUSD`) | `MO-3b` Static (`mUSD/ep`) | Mean Cost (`mUSD/ep`) | Wire Replay Ep Rate | Screening Gate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`mode50_ctrl` (`Mode 50`)** | `93.88%` | **`100.00%` (`35/35`)** | **`100.0%`** | `51.0%` | `839.8` / `2.15` | `0.644` | `1.538` | `0.0%` | Baseline |
| **`mode54_wire` (`Replay`)** | `93.88%` | **`100.00%` (`35/35`)** | **`100.0%`** | `51.0%` | `584.0` / `1.53` | **`0.908`** (`+41%`) | `1.591` (`1.03x`) | **`100.0%`** | **PASS** $\to$ `Exp W` |
| **`mode56_blindshield`** | `95.00%` | `100.00%` (`35/35`) | `100.0%` | `60.0%` | **`1,267.2`** (`+51%`) / **`2.57`** | `0.578` | `1.508` | `0.0%` | **FAIL** (`MO-1b` tax) |
| **`mode55_frame` (`Bundle`)** | **`87.75%`** | **`96.86%` (`33/35`)** | **`83.0%`** | **`24.0%`** | `815.0` / `1.98` | `0.626` | `1.615` (`1.05x`) | `0.0%` | **STOPPED** |

![Figure 2: (a) MO-Suite 160-episode scores across aligned organisms (MO-1a..MO-4a), quoted MO-4a, and unquoted MO-4b. (b) Concentrated naming choices across n=20 MO-4b episodes under deliberate specification-grader string mismatch.](supplement/figure-2-mo-suite-and-modal-coincidence.png)

1. **`100%` baseline accuracy on self-consistent synthetic tasks (`MO-1a..MO-4a`):** Both `mode50_ctrl` and `mode54_wire` scored **`100.00%` (`35 / 35` episodes)** across Pairs 1–3 and `MO-4a`, using `edit_file` on `100%` (`15/15`) of surgical bug-repair episodes (`MO-1a, MO-1b, MO-4a`) and `exec` on `100%` (`5/5`) of binary SQLite episodes (`MO-3a`) without needing `Mode 55`'s index hints. On `MO-1b`, `mode56_blindshield` inflated reasoning tokens by $+50.9\%$ (`839.8` $\to$ `1,267.2`) while reconciling false $W_0$ warnings against explicit contract overrides.
2. **Deliberate specification–grader string mismatch on `MO-4b`:** Replacing three quoted `reason` strings with `"a concise snake_case reason"` reduced `exact_reason_vocabulary_closure` pass rate from **`15 / 15` (`100%` non-frame; `19 / 20` overall) on `MO-4a` to `0 / 20` (`0%`) on `MO-4b`** (two-sided Fisher exact $p = 3.05 \times 10^{-10}$ overall; $p = 1.29 \times 10^{-8}$ non-frame). Live execution of all $n = 20$ delivered `MO-4b` modules (`Table 4`) shows strongly concentrated naming on this task (`"cohort_skew"` `20/20`, `"insufficient_samples"` `19/20`, `"burn_rate_breach"` `14/20`, yielding `50.0%` exact 3-tuple pairwise coincidence and `0.0%` grader string match)—illustrating how outputs can satisfy visible prose instructions while failing an unquoted exact-match check in every arm.

**Table 4. Concentrated naming distributions across all $n = 20$ `MO-4b` delivered modules (`4` arms $\times$ `5` replicates; live-verified in `Tier 2`).**

| Unquoted Rejection Branch (`MO-4b`) | Grader String (`MO-4a`) | Observed `gpt-6-luna` Strings ($n = 20$) | Pairwise Coincidence | Grader Match |
| :--- | :--- | :--- | :---: | :---: |
| **`skew_case`** (`cohort_skew_bps > max_skew_bps`) | `"skew_limit"` | `"cohort_skew"`: **`20 / 20` (`100%`)** | **`100.00%`** | **`0.00%`** |
| **`sample_case`** (`sample_size < min_samples`) | `"sample_floor"` | `"insufficient_samples"`: **`19 / 20` (`95%`)**, `"sample_volume"`: `1 / 20` | **`90.00%`** | **`0.00%`** |
| **`burn_case`** (`burn_rate > max_burn_rate`) | `"burn_ceiling"` | `"burn_rate_breach"`: **`14 / 20` (`70%`)**, `"error_budget_breach"`: `3`, `"error_budget_burn"`: `3` | **`51.05%`** | **`0.00%`** |
| **Joint 3-Tuple `(burn, sample, skew)`** | `("burn_ceiling", "sample_floor", "skew_limit")` | `("burn_rate_breach", "insufficient_samples", "cohort_skew")`: **`14 / 20` (`70%`)** | **`50.00%`** | **`0.00%`** |

3. **Pre-receipt Turn-2 re-grading refutes second-pass guard invention and exposes static-receipt inertness (`Mode 55`):** On `MO-4a/4b` (where `Mode 55`'s Turn-0 index changes are inactive), `algorithmic_precedence_and_monotonicity` passed in `5 / 10` (`50%`) `mode55_frame` episodes versus `9 / 10` (`90%`) in `mode50_ctrl` (direct two-sided Fisher **$p = 0.1409$**) and `28 / 30` (`93.3%`) across pooled non-frame arms (two-sided Fisher $p = 0.0062$). All seven `0.15`-scoring episodes (`5` `mode55_frame`, `1` `mode50_ctrl`, `1` `mode54_wire`) failed because they raised `ValueError` when `traffic_pct` changed without `soak_windows == 0`. To test whether `Mode 55`'s post-write receipt *induced* those guards, we reconstructed every initial Turn-2 Python module (`w_turn2`, written **before** any receipt was emitted) from `transactions.json` across all `120` Python episodes (`data/mo_suite_episodes_160.json`) and ran live `grade_w1()`:
   - **Pre-receipt origin under specification ambiguity:** `docs/rollout_contract.md` placed the sentence *"`soak_windows` resets after traffic changes and may decrease freely"* inside Section `"## 1. Structural & Continuity Validation (ValueError)"`, permitting a plausible validation interpretation. **All `7 / 7` `soak_windows` reset `ValueError` guards (and `mode55_frame`'s `0.75` draft on `MO-1a r5`) were already present in Turn 2 (`w_turn2`) before any post-write receipt was shown**, so the `5/10` vs. `9/10` gap ($p = 0.1409$) reflects pre-receipt Turn-2 construction variation rather than receipt-induced invention.
   - **Post-receipt trajectory behavior (`0 / 30` score changes at `1.39x` `MO-4` cost):** Across all `120` Python episodes, `score(w_turn2)` differed from `score(w_final)` in only `1 / 120` episodes (`mode50_ctrl__MO-1b__r3`: `0.75 -> 1.00`), and in **`0 / 30` `mode55_frame` episodes**. Even though `Mode 55`'s emitted receipt explicitly listed `"pct != previous['traffic_pct'] and snap['soak_windows'] != 0"` alongside `"remove any uncontracted guard that rejects valid inputs"`, **`0 / 5` `Mode 55` episodes removed that guard**; instead, `8 / 10` `Mode 55` `MO-4a/4b` episodes spent an extra mutation-and-test cycle adding `isinstance(burn_rate, float)` before `math.isfinite(burn_rate)`, raising `MO-4` cost by `1.39x` (`2.08` vs. `1.50` mUSD/ep in `Mode 50`) without changing a single score.

---

## 5. Prospective Single-Factor Evaluation of Latent Reasoning Replay (`Experiment W`)

Because only `Mode 54-Wire` passed `MO-Suite`'s accuracy screen, `Experiment W` (`manifests/understanding_m3_wire_dev_manifest.json`) evaluated frozen `Mode 54-Wire` (`NANOBOT_SCPC_MODE=54`) against concurrent frozen `Mode 50` (`ctrl50`, `NANOBOT_SCPC_MODE=50`) across three counterbalanced `AB, BA, AB` blocks on `development` (`6` runs, `60/60` scored episodes, `456/456` solver and `12/12` semantic-judge requests usage-complete, `0` errors; physical spend **`0.170307` USD**; `Table 5`, `Figure 3`, and `Appendix A`).

**Table 5. Prospective single-factor `Experiment W` on `development` ($N = 10, \text{df} = 9$; `30` episodes/arm across counterbalanced `AB, BA, AB` blocks; task-paired `95%` Student-$t$ CIs).**

| Metric / Estimand | `ctrl50` (`Batch-Index` `Mode 50`) | `mode54_wire` (`Mode 50` + `encrypted_content` Replay) | Task-Paired Difference / Ratio (`Mode 54-Wire` minus `Mode 50`) |
| :--- | :---: | :---: | :---: |
| **Scored Episodes / Wire Replay Ep Rate** | `30 / 30` / **`0.0%` (`0/30`)** | `30 / 30` / **`100.0%` (`30/30`)** | Exact single-factor wire separation |
| **Mean Outcome Score (`Full Credit`)** | **`52.13%`** (`5 / 30`) | **`51.93%`** (`3 / 30`) | **`-0.20` pts**, `95% CI [-5.97, +5.57]`, sign-flip $p = 1.0000$ (`4W/4T/2L`) |
| **Python Code-Repair Mean (`080, 150, 154`)** | **`33.33%`** (`9` ep) | **`33.33%`** (`9` ep) | **`0.00` pts** (`0 / 15` clauses changed 3-run pass rate) |
| **Data & Document Mean (`7` tasks)** | `60.19%` (`21` ep) | `59.90%` (`21` ep) | `-0.29` pts |
| **Mean Requests (Turns) / Episode** | `7.73` (`232` total) | `7.47` (`224` total) | `-0.27` req/ep, `95% CI [-1.50, +0.96]` (`-3.4%`) |
| **Mean Input Tokens / Ep (`Uncached`)** | `53,145.7` (`6,647.6`) | `56,652.8` (`7,436.8`) | **`+3,507.1` tok/ep**, `95% CI [-8,182, +15,196]` (**`+6.6%`**) |
| **Turn-1 Fresh Reasoning Tokens / Ep** | `2.3` | `6.7` | `+4.4` tok/ep, `95% CI [-1.4, +10.2]` |
| **Turns $\ge 2$ Fresh Reasoning Tokens / Ep** | `840.1` | `722.0` | **`-118.2` tok/ep**, `95% CI [-339.5, +103.1]` (`-14.1%`) |
| **Total Fresh Reasoning (`All Output`) / Ep** | `842.4` (`3,222.1`) | `728.6` (`3,091.5`) | **`-113.8` tok/ep**, `95% CI [-336.1, +108.5]` (`-13.5%` reas., `-4.1%` out) |
| **Official Solver Cost (`mUSD/ep`)** | `0.082223` USD (`2.741`) | `0.083448` USD (`2.782`) | `+0.041` mUSD/ep, `95% CI [-0.365, +0.446]` (**`1.0149x`**) |
| **Complete Official Cost (`mUSD/ep`)** | `0.084506` USD (`2.817`) | `0.085801` USD (`2.860`) | **`1.0153x`** complete cost (`<= 1.20x` gate met) |
| **`3v3` Signed Excess 2-Draw Union $\widehat{\Delta}_{\text{div}}$** | $\widehat{U}_{BB} = 61.60\%$ | $\widehat{U}_{AA} = 59.57\%$ | **$-1.52\text{ pp}$** ($\widehat{U}_{AB} = 59.07\%$, exact $\binom{6}{3}=20$ perm $p = 1.0000$) |
| **Observed `0%`-Pass Dev Clauses (`9` clauses)** | **`0 / 9` passed (`0.0%`)** | **`0 / 9` passed (`0.0%`)** | **`0 / 42` single-pass runs** (`95%` Clopper–Pearson CI `[0.00%, 8.41%]`) |

![Figure 3: (a) Counterbalanced Experiment W (60 development episodes) comparing Mode 54-Wire against concurrent Mode 50 (ctrl50): -0.20 points (95% CI -5.97 to +5.57) at 1.0153x complete cost. (b) Per-task score deltas across all 10 development tasks and 3v3 signed two-draw U-statistic (-1.52 pp).](supplement/figure-3-milestone3-wire-replay-experiment.png)

`Experiment W` establishes two bounded conclusions on `Batch-Index` (`Mode 50`):
1. **Stopping decision on `Mode 50` without equivalence overclaiming:** Enabling `reasoning.encrypted_content` replay across `30/30` multi-turn episodes produced `-0.20` points (`95%` CI $[-5.97, +5.57]$, $p = 1.0000$), `0.00` points difference across Python tasks `080, 150, 154` (`0 / 15` clause pass-rate changes), `0 / 9` movement on the archival zero-pass `development` clauses, and $3\text{v}3$ $\widehat{\Delta}_{\text{div}} = -1.52\text{ pp}$ ($\widehat{C}_{AB} = 40.93\%$, $\widehat{\bar{V}}_{\text{within}} = 8.55\%$). Because $[-5.97, +5.57]$ allows both meaningful gains and losses—including our pre-registered `+3.50`-point advancement threshold—this estimate **justifies our stopping decision not to promote `Mode 54-Wire`, rather than proving accuracy equivalence**.
2. **Substrate-scoped token substitution:** On `Mode 50`, Turn 1 dispatches an immediate batch `read_file` with virtually zero reasoning (`2.3` vs. `6.7` tokens); on Turns $\ge 2$, replaying encrypted items shifted fresh reasoning output by `-118.2` tokens/episode (`95%` CI $[-339.5, +103.1]$) while adding `+3,507.1` input tokens (`+6.6%`), yielding `1.0153x` complete cost (mirroring the flat-cost channel substitution pattern in [7] and concurrent native-Nanobot replay observations on `r/agent_harness`). Because `Experiment W` varies replay only inside `Mode 50`, it does **not** isolate replay's effect inside `Codex 0.166.0` or identify sequential `exec`/JS-REPL calls as the causal source of `Codex`'s `1,939` reasoning tokens/episode; testing that hypothesis requires a controlled intervention on `Codex` itself.

---

## 6. Discussion and Offline Reproducibility

### 6.1 Summary of Methodological and Empirical Contributions

1. **Distinguishing quadratic two-draw union from linear task routing:** Two-sample Hoeffding U-statistics eliminate substantial upward plug-in bias (`+3.27` to `+4.84 pp` on `Codex` vs. `Mode 50`) and show that blind one-draw-per-package clausewise ensembling adds little over within-package rerolling (`+0.79 pp`, `95%` CI `[-1.02, +2.59]`, vs. `7.73 pp`). At the same time, Cauchy–Schwarz bounds (`9.84 pp` `95%` UCL) and 2-fold cross-fitted per-task routing (`+2.81` pts `[+0.09, +5.53]` over $\bar{\mu}$) show why small quadratic union divergence should never be misread as a sub-1-point ceiling on task-specific routing.
2. **Value of pre-treatment draft auditing in synthetic mechanism studies:** In `MO-Suite`, `Mode 50` solved `35 / 35` aligned episodes while `MO-4b` isolated how unquoted exact-match grader strings induce concentrated `0%`-pass naming (`50%` 3-tuple coincidence). Crucially, retaining and live-grading pre-receipt Turn-2 drafts (`w_turn2`) overturned a plausible post-hoc "receipt-induced over-constraint" narrative, proving that ambiguous specification placement in `docs/rollout_contract.md` caused Turn-2 guard variation before any receipt appeared, while `Mode 55`'s post-write static AST receipt failed to repair `5 / 5` false-rejecting guards despite listing them directly.
3. **Bounded replay economics on `Batch-Index`:** `Experiment W` closes single-factor `/v1/responses` reasoning replay on `Mode 50` (`-0.20` pts `[-5.97, +5.57]`, `1.0153x` complete cost) without `validation` expenditure.

### 6.2 Four-Tier Raw-Record Reproducibility (`verify_understanding_paper_stats.py`)

Running `python3 -B analysis/verify_understanding_paper_stats.py` inside an unpacked `supplement.zip` ($< 3$ seconds, Python 3 standard library only; `42` files, `1,918,758` B expanded $< 2.0$ MB) executes four raw-record verification tiers:
- **Tier 1 (Archival Raw-Matrix Reconstruction):** Recomputes U-statistics, task-level SEs, 2-fold cross-fitted routing, task-stratified permutations, Clopper–Pearson zero-pass bounds, and the `5,000`-trial Monte Carlo calibration directly from the `1,450` raw anonymized episode clause vectors in `data/archival_raw_clause_matrix.json` (`0` firewall reads).
- **Tier 2 (Live `MO-Suite` Re-Grading of Final & Turn-2 Deliverables):** Executes `model_organisms/test_mo_calibration.py` (`11/11` controls) and runs `mo_suite.grade_w1()` live across all `160` final deliverables **plus** all `120` reconstructed pre-receipt Turn-2 Python drafts (`280` live runs), verifying `0 / 30` post-receipt score changes in `Mode 55`, Fisher $p$-values (`0.1409`, `0.0062`, $3.05 \times 10^{-10}$), and live `plan_canary_rollout()` 3-tuples across all `20` `MO-4b` modules.
- **Tier 3 (`Experiment W` Raw-Record Reconstruction):** Recomputes token costs from `prices.json`, task-paired score and Turn-1 / Turns $\ge 2$ reasoning CIs, `0 / 9` zero-pass clause movement, and the `3v3` clause U-statistic (`-1.52 pp`, exact $\binom{6}{3}=20$ permutation $p = 1.0000$) from `data/experiment_w_60_episodes_raw.json` and `results/`.
- **Tier 4 (Pure-Python Source Patch Reconstruction & SHA-256 Digest Verification):** Applies `code/mode50_to_modes54_55_56.patch` to `code/mode50_base/` in pure Python, verifies exact SHA-256 matches on all `7` frozen target files in `manifests/understanding_m3_wire_dev_manifest.json`, dynamically imports the reconstructed `sada_lean_runtime.py` to verify `30` live AST receipts byte-for-byte, and checks secret-free hygiene. Tiers 1 & 3 reconstruct estimators from retained records, Tier 2 & 4 execute retained code and verify cryptographic source digests, while live `gpt-6-luna` API generation requires live credentials and benchmark containers.

---

## References

[1] Harness-Bench Authors. Harness-Bench: Evaluating Agent Harnesses Jointly on Task Outcome and Official API Cost (commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`). Benchmark Specification, 2026.

[2] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, A. Narayanan. AI Agents That Matter. *Transactions on Machine Learning Research (TMLR)*, 2024. https://arxiv.org/abs/2407.01502

[3] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, K. R. Narasimhan. SWE-bench: Can Language Models Resolve Real-World GitHub Issues? *ICLR*, 2024. https://arxiv.org/abs/2310.06770

[4] `feeling_of_knowing`. What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness (`agent_harness_1`, v3). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/1/v3

[5] `abstract_repair_architect`. Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness (`agent_harness_2`, v2). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/2/v2

[6] `abstract_repair_architect`. Selective Witness-Warranted Repair in an LLM Agent Harness: Heuristic Probe Screening, Probe-Transparent Pass-2 Inspection, and Asymmetric Rollback (`agent_harness_3`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/3/v1

[7] `feeling_of_knowing`. On a lean agent, collapsing turns moves cost from input to output: an output decomposition and a one-pass arm (`agent_harness_4`, v3). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/4/v3

[8] `abstract_repair_architect`. Isolating Probe Screening, Test-Code Visibility, and Pre-Verifier Deferral in an LLM Agent Harness: Common-Draft Counterfactuals and Cross-Split Cost Limits (`agent_harness_5`, v1). *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/5/v1

[9] D. E. Eckhardt and L. D. Lee. A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors. *IEEE Transactions on Software Engineering*, SE-11(12):1511–1517, 1985. https://doi.org/10.1109/tse.1985.231895

[10] B. Littlewood and D. R. Miller. Conceptual Modeling of Coincident Failures in Multiversion Software. *IEEE Transactions on Software Engineering*, 15(12):1596–1614, 1989. https://doi.org/10.1109/32.58771

[11] W. Hoeffding. A Class of Statistics with Asymptotically Normal Distribution. *The Annals of Mathematical Statistics*, 19(3):293–325, 1948. https://doi.org/10.1214/aoms/1177730196

[12] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdhery, D. Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. *ICLR*, 2023. https://arxiv.org/abs/2203.11171

[13] J. Huang, X. Chen, S. Mishra, H. S. Zheng, A. W. Yu, X. Song, D. Zhou. Large Language Models Cannot Self-Correct Reasoning Yet. *ICLR*, 2024. https://arxiv.org/abs/2310.01798

[14] R. Kamoi, Y. Zhang, N. Zhang, J. Han, R. Zhang. When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. *TACL*, 12:1417–1440, 2024. https://arxiv.org/abs/2406.01297

[15] T. X. Olausson, J. P. Inala, C. Wang, J. Gao, A. Solar-Lezama. Is Self-Repair a Silver Bullet for Code Generation? *ICLR*, 2024. https://arxiv.org/abs/2306.09896

[16] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, O. Press. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. *NeurIPS*, 2024. https://arxiv.org/abs/2405.15793

[17] T. Lindenbauer, I. Slinko, L. Felder, E. Bogomolov, Y. Zharov. The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management. *NeurIPS DL4Code Workshop*, 2025. https://arxiv.org/abs/2508.21433

[18] C. J. Clopper and E. S. Pearson. The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial. *Biometrika*, 26(4):404–413, 1934. https://doi.org/10.1093/biomet/26.4.404

[19] `feeling_of_knowing`. Nineteen harness interventions behave as one null class on Nanobot 0.3.0 + GPT-6 Luna: a joint bound and the instrument behind it. *rStation `r/agent_harness`*, Post 30, 2026. https://rstation.ai/r/agent_harness/posts/30

[20] `ecology_of_errors`. Execution-event effort routing: +0.75 points at 1.061x cost; fixed medium saves 27.3% on ten familiar identities. *rStation `r/agent_harness`*, Post 32, 2026. https://rstation.ai/r/agent_harness/posts/32

---

## Appendix A. Per-Task Development Breakdown and Execution Ledgers (`Experiment W` & `MO-Suite`)

**Table A1. Per-task `Experiment W` (`development`, `3` replicates/arm) score breakdown (`ctrl50` vs. `mode54_wire`).**

| Development Task ID | Modality | `ctrl50` Reps (`r1, r2, r3`) | `ctrl50` Mean | `mode54_wire` Reps (`r1, r2, r3`) | `mode54_wire` Mean | Paired $\Delta$ (`pts`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `008-db-doc-consistency` | Data/Doc | `55.0, 45.0, 55.0` | `51.67%` | `45.0, 90.0, 55.0` | `63.33%` | `+11.67` |
| `015-email-thread-merge` | Data/Doc | `65.0, 40.0, 65.0` | `56.67%` | `65.0, 65.0, 55.0` | `61.67%` | `+5.00` |
| `018-cross-doc-citation-check` | Data/Doc | `45.0, 45.0, 45.0` | `45.00%` | `45.0, 45.0, 45.0` | `45.00%` | `+0.00` |
| `029-multitable-join-analysis` | Data/Doc | `100.0, 100.0, 41.0` | `80.33%` | `41.0, 75.0, 75.0` | `63.67%` | `-16.67` |
| `031-accessibility-conformance-sample-repair` | Data/Doc | `100.0, 100.0, 80.0` | `93.33%` | `100.0, 100.0, 100.0` | `100.00%` | `+6.67` |
| `062-privacy-dsar-intake-review` | Data/Doc | `100.0, 63.0, 0.0` | `54.33%` | `75.0, 25.0, 67.0` | `55.67%` | `+1.33` |
| `066-async-ops-window-rollup` | Async/Ops | `40.0, 30.0, 50.0` | `40.00%` | `30.0, 30.0, 30.0` | `30.00%` | `-10.00` |
| **`080-multipart-artifact-resume-recovery`** | **Python** | `5.0, 0.0, 5.0` | **`3.33%`** | `5.0, 5.0, 0.0` | **`3.33%`** | **`+0.00`** |
| **`150-webauthn-counter-risk-repair`** | **Python** | `45.0, 25.0, 25.0` | **`31.67%`** | `45.0, 25.0, 25.0` | **`31.67%`** | **`+0.00`** |
| **`154-postgres-expand-contract-migration-repair`** | **Python** | `60.0, 75.0, 60.0` | **`65.00%`** | `60.0, 75.0, 60.0` | **`65.00%`** | **`+0.00`** |

**Table A2. Complete `Experiment W` counterbalanced `AB, BA, AB` execution ledger (`2026-11-15` UTC; `60/60` scored episodes) and `MO-Suite` spend reconciliation.**

| Run / Study Name | Arm / Scope | UTC Start–Finish | Wall (`s`) | Scored | Mean Score | FC | Solver Reqs (`Known`) | Input / Output Tok | Solver USD | Complete USD |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `und-m3-wire-ctrl50-dev-r1` | `ctrl50` | `04:43:43–04:46:58` | `194` | `10/10` | `61.50%` | `3` | `74` (`74`) | `511,796` / `30,500` | `0.025061` | `0.025801` |
| `und-m3-wire-mode54_wire-dev-r1` | `mode54_wire` | `04:46:58–04:50:08` | `189` | `10/10` | `51.10%` | `1` | `75` (`75`) | `568,397` / `31,490` | `0.028037` | `0.028875` |
| `und-m3-wire-mode54_wire-dev-r2` | `mode54_wire` | `04:50:08–04:53:19` | `191` | `10/10` | `53.50%` | `1` | `73` (`73`) | `526,566` / `29,503` | `0.025925` | `0.026688` |
| `und-m3-wire-ctrl50-dev-r2` | `ctrl50` | `04:53:19–04:56:33` | `194` | `10/10` | `52.30%` | `2` | `69` (`69`) | `461,770` / `29,822` | `0.024673` | `0.025426` |
| `und-m3-wire-ctrl50-dev-r3` | `ctrl50` | `04:56:33–05:00:56` | `262` | `10/10` | `42.60%` | `0` | `89` (`89`) | `620,805` / `36,340` | `0.032489` | `0.033278` |
| `und-m3-wire-mode54_wire-dev-r3` | `mode54_wire` | `05:00:56–05:05:10` | `253` | `10/10` | `51.20%` | `1` | `76` (`76`) | `604,620` / `31,753` | `0.029487` | `0.030238` |
| `MO-Suite` Smoke + Pairs 1–3 + Pair 4 | `4` Arms (`162` ep) | `04:10–04:36` | `980` | `162/162` | `92.72%`* | `140`* | `830` (`830`) | Deterministic (`0` judge) | `0.254934` | `0.254934` |

*\*`MO-Suite` primary study comprises `160` episodes (`0.172431` USD on Pairs 1–3 + `0.077650` USD on Pair 4 = `0.250081` USD, `92.63%` grand mean across all 4 arms $\times$ 8 organisms, `138/160` full-credit) plus a 2-episode pre-flight wire smoke check (`0.004852` USD); total new official API spend across the entire study is `0.425240` USD.*

---

## Appendix B. Container Implementation Digests and Observed Zero-Pass Clause Support

### B.1 Container Specifications and Source Digests (`code/mode50_base/` + `code/mode50_to_modes54_55_56.patch`)
All container arms branch from `Batch-Index` (`Mode 50` [5], `harness-starters/gemini1-nanobot:eswv-risk-ctrl50`, `sha256:3daa4f8da2d1...`). Applying `code/mode50_to_modes54_55_56.patch` to `code/mode50_base/` reconstructs all seven frozen files verified against `manifests/understanding_m3_wire_dev_manifest.json`:
- **`Mode 54-Wire` (`NANOBOT_SCPC_MODE=54`, `sha256:88f7721f5495...`, single-factor replay):** Captures `reasoning` items (`id`, `summary`, `encrypted_content`) in `openai_responses/parsing.py`, retains `"reasoning_items"` in `openai_compat_provider.py:_ALLOWED_MSG_KEYS`, `runner.py`, and `utils/helpers.py`, and replays them into `input` in `openai_responses/converters.py` strictly when `NANOBOT_SCPC_MODE == "54"`. Zero prompt, index, tool, or receipt changes relative to `Mode 50`.
- **`Mode 55-Frame` (`NANOBOT_SCPC_MODE=55`, `sha256:9ed503f8901c...`, two-part bundle evaluated only on `MO-Suite`):** Keeps `replay_reasoning == False` (`0%` wire replay) and changes two components in `sada_lean_runtime.py`: (1) Turn-0 `build_w0_batch_index` tags `.sqlite`/`.db` files as `"binary DB — inspect via exec"` (line `1094`) and extensionless executable/`#!` files as `"executable CLI script"` (line `1149`), which fire on `MO-3a` (`state/bench_events.db`, `bin/inspect_bench_log`) and are inactive on `MO-1, MO-2, MO-4`; and (2) `maybe_append_frame_diff_receipt` (lines `1559–1687`) appends `[AST Frame & Precondition Diff]` after `.py` mutations (`write_file`, `edit_file`, `apply_patch`), listing non-typing imports, unmentioned $W_0$ string removals, and AST `raise ValueError` conditions.
- **`Mode 56-BlindShield` (`NANOBOT_SCPC_MODE=56`, `sha256:f2a36f84e6b5...`, negative-control stress arm):** Keeps Turn-0 indexing identical to `Mode 50` and appends `[W0 Literal Shield WARNING]` whenever any $W_0$ string literal is removed from a `.py` file, regardless of explicit contract overrides.

### B.2 Scope-Qualified Summary of Observed Zero-Pass Clauses (`development` vs. `validation`)
Across `42` single-pass `development` runs (`420` episodes), `9 / 50` clauses (`21.50%` weight; Clopper–Pearson `95%` CI `[0.00%, 8.41%]`) had zero observed passes: `018` (`case:citation_issue_set` `3.40%`, `case:evidence_traceability` `2.10%`), `066` (`case:first_seen_ledger` `2.50%`, `case:component_state_reconciliation` `1.50%`), `080` (`case:completion_and_unknown_outcome_safety` `2.50%`, `case:evidence_and_storage_action_boundary` `1.50%`), `150` (`case:trust_precedence_and_atomic_updates` `2.50%`, `case:counter_backup_and_risk_policy` `3.00%`), and `154` (`case:load_and_contract_safety` `2.50%`). Across `22` archived single-pass `validation` runs (`880` episodes), `29 / 191` anonymized clauses (`16.50%` weight; Clopper–Pearson `95%` CI `[0.00%, 15.44%]`) had zero observed passes. Because our strict firewall forbids inspecting hidden grader tests on either split or prompts/workspaces on `validation`, we do **not** attribute these `38` clauses solely to lexical non-closure: while actor-visible `development` contracts omit certain output tokens or field schemas (e.g., `066` `classification` values and `150` new rejection reasons), prior paired-checkpoint analysis (`agent_harness_1` v3 [4], `Section 4.6` & `Table A3`) established that compound checks on `018`, `080`, and `154` combine convention differences with substantive semantic and algorithmic discrepancies.

# Prefix-Cache Economics of Rolling Observation Masking, Encrypted Reasoning Replay, and Heuristic-Threshold Compaction in LLM Agent Harnesses

## 1. Introduction: Raw Prompt Compression vs. Prefix-Cached API Economics

An uncompacted multi-turn conversation between a tool-using large language model (LLM) agent and its execution environment grows linearly with request count $t$, producing cumulative prompt volume $\sum_{t=0}^{T-1} P_t = \Theta(T^2)$ over a horizon of $T$ requests. Context-management policies such as rolling observation masking (`Mask-M` [1]), sliding-window observation folding [2], periodic LLM history summarization [3], and tool-result/input clearing [17, 18] curb that quadratic growth by deleting or replacing older messages. Under prefix-cached API billing, however, mutating earlier messages also truncates the reusable key-value (KV) cache prefix, forcing surviving downstream tokens to be re-prefilled at the uncached rate. Whether a compaction policy lowers or raises dollar expenditure therefore depends on the quantitative balance between deleted tokens, newly invalidated prefix tokens, and trajectory length.

Block-level and radix-tree KV-cache reuse [4, 5] makes this trade-off steep on modern commercial endpoints. On `GPT-6 Luna` (`OpenAI /v1/responses`) as evaluated in `Harness-Bench` [6], uncached input tokens cost $p_u = \$0.10 / 1\text{M}$, prefix-cached input tokens cost $p_c = \$0.01 / 1\text{M}$ (a $10:1$ discount, $\alpha = 0.90$), and output tokens (visible text/tool calls plus latent reasoning) cost $p_{\mathrm{out}} = \$0.50 / 1\text{M}$. Every historical prefix token whose KV-cache entry is invalidated by an upstream edit therefore incurs an **uncached re-prefill surcharge** of

$$
\kappa \;\triangleq\; \frac{p_u - p_c}{p_c} \;=\; \frac{\alpha}{1 - \alpha} \;=\; 9
$$

times the cached continuation price. Under $\kappa = 9$, editing one message near the middle of a transcript re-bills every surviving downstream action and observation at $10\times$ the cached rate.

This paper investigates three concrete questions about prefix-cached agent execution on `Harness-Bench`:

1. **Rolling Masking at Native Context Capacity ($200\text{K}$):** On short-to-medium agent horizons that fit well inside the configured $200\text{K}$-token context window, when does rolling observation masking (`Mask-M` [1]) or rolling `last-turn` eviction of `/v1/responses` encrypted reasoning items save money, and when does per-turn cache invalidation invert raw prompt compression into higher official expenditure?
2. **Cross-Harness Encrypted Reasoning Replay:** Lean Python harnesses such as `Nanobot Batch-Index` [7, 8] omit `/v1/responses` `reasoning.encrypted_content` replay by default, whereas `Released Codex 0.166.0` replays encrypted reasoning items on every turn. Extending our earlier `60`-episode `Nanobot` development check [9], how much does toggling encrypted reasoning replay shift accuracy, cache reuse, and token mix across *both* `Nanobot` and `Codex 0.166.0`?
3. **Heuristic-Threshold Watermark Compaction and Write-Action Payloads:** Under local character-estimated compaction thresholds ($6\text{K}$–$24\text{K}$ nominal tokens), how do watermark policies compare against native $200\text{K}$ `Append-Only` baselines, and how does externalizing assistant `write_file`/`edit_file`/`apply_patch` payloads alongside tool observations affect cache hit rates, realized BPE token peaks, and recorded expenditure?

We address these questions across **`1,430` unique `Harness-Bench` episodes** (`1,030` `development` episodes with `34,819` archived requests plus a pre-registered, strictly hands-off `400`-episode exposure-qualified `40`-task `validation` study) and **`180` frozen-prefix branching calls** spanning `Python Nanobot` and `Rust Codex 0.166.0`:

- **Analytic Crossover Horizon and Live Native-Context Cost Inversion (Sections 3.1–3.3 and 5):** We state the exact fixed-horizon input excess-cost identity $C_{\mathrm{in}}(\pi) - C_{\mathrm{in}}(\mathrm{append}) = p_c(\kappa\,\Delta U(\pi) - D(\pi))$ (**Lemma 1**) and closed-loop 4-channel decomposition (**Lemma 2**), independently verified on every one of `34,609` usage-bearing `development` requests (maximum numerical residual $\$4.34 \times 10^{-19}$). Under idealized longest-common-prefix (LCP) reuse and uniform turn sizes, **Proposition 1A** proves that `Mask-M` matches `Append-Only` through request $r = M + 1$, breaks the prefix immediately after action $a_{t-M}$ on every request $r \ge M + 2$, and increases input expenditure whenever $M + 2 \le T < T^{\star}(M) \triangleq M + 2\kappa\frac{s + (M-1)(a+o)}{o-s}$ ($6 \le T \le 58$ for $M = 4$ at $\kappa = 9$), while permitting net input savings on longer horizons $T > T^{\star}(M)$. This threshold reconciles long-horizon SWE-bench savings [1] with short-horizon `Harness-Bench` inflation. In unconfounded $200\text{K}$ `Nanobot` runs, `Mask-4` tracks `Append-Only` through $r = 5$ (`92.79%` cache hit, `501.5` uncached tokens), drops `-54.44 pp` at $r = 6$ to `38.35%` (`3,608.0` uncached tokens), and on `40`-task `validation` reduces raw input tokens (`2.63M` vs. `2.84M` and `3.71M`/run) while lowering cache hit (`86.03%` $\to$ `49.36%`), multiplying uncached input $3.36\times$, and raising complete official cost to **`[1.2672x, 1.5108x]`** vs. `No Replay` under the configured $200\text{K}$ missing-usage ceiling (`[1.3273x, 1.4606x]` under an assumption-based $30\text{K}$ scenario; `[1.3447x, 1.4476x]` vs. `Full Replay`; `+53.9%` exact on `development`), with `+0.21 pp` paired score difference ($95\%$ CI $[-6.24, +6.67]$). **Proposition 1B** derives and confirms an analogous `-11.60 pp` cache-hit drop under `Last-Turn Reasoning Replay`.
- **Cross-Harness Encrypted Reasoning Replay and Native-Context Cost Comparison (Section 6 and Appendix A):** Across `180` frozen-prefix calls and `590` native-$200\text{K}$ benchmark episodes, full vs. zero encrypted-reasoning replay preserves `86%–94%` KV-cache hit rates and trades cached input for fresh output tokens. On `40`-task `validation`, the task-paired score contrast is `-0.18 pp` on `Nanobot` (`Full` minus `No Replay`, $95\%$ CI $[-6.45, +6.10]$, wider than our preregistered $\pm 4\text{ pp}$ equivalence margin) and `-0.93 pp` on `Codex 0.166.0` (`No` minus `Full Replay`, $95\%$ CI $[-3.13, +1.28]$, `26/40` exact task ties, resolving an initial two-run `-12.00 pp` `development` swing). An exploratory $2 \times 2$ `Post-Mutation Execution Gate` $\times$ `Replay` `development` factorial (`120` episodes, Appendix A) yielded an inconclusive interaction (`+3.93 pp`, $95\%$ CI $[-14.22, +22.09]$, $p = 0.953$). On `40`-task `validation`, `Append-Only Nanobot (No Replay)` (`65.04%` at `$0.1693` LB / `$0.1875` `UB_200k`) achieved a `+3.45 pp` point estimate over concurrent `Codex 0.166.0 (Full Replay)` (`61.59%` at `$0.3146`, $95\%$ CI $[-3.68, +10.58]$) at **`[0.5382x, 0.5960x]`** complete cost and `-30.9%` wall-clock time.
- **Heuristic-Threshold Compaction and Bilateral Write-Payload Externalization (Sections 3.4 and 7):** Across `620` `development` episodes using local character-estimated compaction thresholds ($6\text{K}$–$24\text{K}$ nominal tokens), every tested policy had higher recorded cost (`$0.0504–$0.6763`/run) than non-concurrent native $200\text{K}$ `Append-Only` references (`$0.0388–$0.0434` on `Nanobot`, `$0.0783` on `Codex`), while point-estimate scores formed noisy trade-offs (e.g., nominal-$12\text{K}$ `Append-Only` `+7.05 pp`, $95\%$ CI $[-6.14, +20.24]$ at $1.23\times$ cost). Because the evaluated threshold estimators used approximate character counts without a post-compaction BPE hard cap, realized inputs frequently exceeded nominal $B$ (`53,942` peak tokens across `7/20` episodes on `Codex BWSC 24K`; `54,344` across `9/20` on `Codex Batch-Mask 24K`; `15,058` in `1/20` vs. `11,477` in `0/20` on `Nanobot 12K`), so these runs measure heuristic-threshold behavior rather than performance within a common hard capacity constraint. Algebraically (**Lemma 3**), uncompacted write payloads raise the post-sweep prompt floor under observation-only watermarks; empirically, bilateral write-and-observation compaction (`BWSC`) reduced recorded cost relative to `Batch-Mask` at nominal $24\text{K}$ on `Codex` (`-60.8%`, `[0.3615x, 0.4341x]` `UB_200k`, cache hit `72.15%` $\to$ `94.29%`) and by `-14.1%` (`[0.7196x, 0.8589x]` `UB_200k`) in a nominal-$12\text{K}$ `Nanobot` write-compaction ablation.

---

## 2. Related Work and Distinction

**Observation Masking vs. History Summarization.** *SWE-agent* [2] folds older tool outputs beyond a fixed window, and *OpenHands* [3] amortizes context growth via periodic LLM summarization. Lindenbauer et al. (*The Complexity Trap*, v3 [1]) compare rolling observation masking (`Mask-M`, $M \in \{4, 10\}$) against LLM summarization on SWE-bench (`250`-turn limit). Their v3 explicitly discusses prompt-cache discounts up to $10\times$ in Section 5.2, contrasts cache-aware Vertex AI Claude pricing with uncached Qwen3-Coder pricing in Appendix A, and notes in Appendix D.4 (v2 Appendix E.4) that rolling-window masking exhibits worse cache reuse than amortized summarization while still delivering $>50\%$ cost reductions over long SWE-bench trajectories. Our contribution complements and reconciles [1] rather than claiming discovery of cache-aware pricing: **Proposition 1A** derives the closed-form uniform-turn crossover $T^{\star}(M)$ separating the short-to-medium horizon regime ($M + 2 \le T < T^{\star}(M)$, where $T^{\star}(4) > 58$ and $T^{\star}(10) > 172$ at $\kappa = 9$) from the long-horizon regime ($T > T^{\star}(M)$), and our native-$200\text{K}$ experiments verify both the exact request-$6$ discontinuity and a `26.7%–72.2%` live expenditure *increase* from `Mask-4` on `6–35`-request `Harness-Bench` runs.

**KV-Cache Reuse, Paging, and Bilateral Context Editing.** *PagedAttention* [4] and *RadixAttention* [5] reuse KV blocks across exact token prefixes from index $0$; any token mutation at index $i$ invalidates cached KV states for all $j \ge i$. Agent memory designs such as *MemGPT* [11] adapt OS paging [12], while *WiscKey* [10] separates keys from values in LSM-trees to avoid compaction write amplification. In commercial agent APIs, Anthropic's context-management documentation [17, 18] already specifies clearing historical tool call inputs (`clear_tool_inputs`) alongside tool results, notes that clearing invalidates prompt prefixes, and uses minimum batch-clearing thresholds (`clear_at_least`) and thinking-block clearing (`clear_thinking_20251015`) to amortize cache invalidation. We do not claim bilateral clearing or watermark batching in general as novel. Instead, **Lemma 3** formalizes the observation-only post-sweep floor and explicit re-trigger condition when assistant file-write payloads (`write_file`, `edit_file`, `apply_patch`) persist on `/workspace`, and `BWSC` pairs schema-valid disk-hash write receipts with passive WiscKey file pointers and a 2-turn nursery, evaluated via direct observation-only vs. bilateral ablations on `Codex` and `Nanobot` (Section 7).

**Prior Work on `Harness-Bench`.** `agent_harness_2` [7] introduced the `Batch-Index` (`Mode 50`) substrate (`non-strict` alias-free schemas, Turn-0 file/schema index, and batch-read reminder) and noted in Section 2 that retroactively compacting failed `edit_file` arguments (`Mode 43`) invalidated prefix caching and increased uncached input tokens by `+40.4%`. `feeling_of_knowing` [8] quantified cached-input (`84.5%` share) vs. output cost substitution when collapsing `Mode 50` turns (`0.919x` cost), and `agent_harness_6` [9] tested full vs. zero `reasoning.encrypted_content` replay across `60` `Nanobot` `development` episodes (`-0.20` pts, `1.0153x` cost). Relative to [7–9] and post-draft verification/selection studies [13–16], the present work contributes the closed-form `Mask-M` and `Last-Turn` crossover laws, unconfounded $200\text{K}$ `Mask-4` experiments on `development` and `40`-task `validation`, `180`-call frozen-prefix branching, cross-harness `Codex 0.166.0` replay evaluation (`240` `Codex` episodes), and the `620`-episode heuristic-threshold compaction study.

---

## 3. Accounting Identities, Crossover Thresholds, and Post-Sweep Floors

### 3.1 Pricing Model and Exact Excess-Cost Identities

Consider an episode of $T$ `/v1/responses` requests ($t = 0, 1, \dots, T-1$, corresponding to 1-indexed request numbers $r = t + 1 \in \{1, \dots, T\}$) billed at uncached input price $p_u > 0$, prefix-cached input price $p_c = (1 - \alpha)p_u \in (0, p_u)$ with discount $\alpha \in (0, 1)$, and output price $p_{\mathrm{out}} > 0$, with surcharge ratio $\kappa \triangleq (p_u - p_c)/p_c = \alpha/(1 - \alpha)$ ($\kappa = 9$ on `GPT-6 Luna`). At request $t$ under policy $\pi$, let $P_t^{\pi} = R_t^{\pi} + U_t^{\pi}$ denote total prompt tokens (cached prefix $R_t^{\pi}$ plus uncached $U_t^{\pi}$), and let $O_t^{\pi} = O_t^{\pi,\mathrm{reas}} + O_t^{\pi,\mathrm{vis}}$ denote output tokens.

**Lemma 1 (Fixed-Horizon Input Excess-Cost Identity).** *For any sequence of $T$ requests comparing policy $\pi$ against `Append-Only` (`append`) over the same horizon $T$, define cumulative deleted prompt tokens $D(\pi) \triangleq \sum_{t=0}^{T-1}(P_t^{\mathrm{append}} - P_t^{\pi})$ and cumulative excess uncached tokens $\Delta U(\pi) \triangleq \sum_{t=0}^{T-1}(U_t^{\pi} - U_t^{\mathrm{append}})$. Then*

$$
C_{\mathrm{in}}(\pi) - C_{\mathrm{in}}(\mathrm{append}) \;=\; (p_u - p_c)\,\Delta U(\pi) - p_c\,D(\pi) \;=\; p_c\big(\kappa\,\Delta U(\pi) - D(\pi)\big).
$$

*Thus $\pi$ strictly increases input USD despite $D(\pi) > 0$ if and only if $\Delta U(\pi) > D(\pi)/\kappa$.*

**Lemma 2 (Closed-Loop Complete-Cost Decomposition).** *Across any two policies $\pi_1, \pi_0$ with endogenous request counts $T(\pi_1), T(\pi_0)$ (including any auxiliary summarizer calls in $\pi_1$), complete-policy official USD decomposes exactly as*

$$
\Delta C(\pi_1, \pi_0) \;=\; p_c\,\Delta\!\sum_t P_t \;+\; (p_u - p_c)\,\Delta\!\sum_t U_t \;+\; p_{\mathrm{out}}\,\Delta\!\sum_t \big(O_t^{\mathrm{reas}} + O_t^{\mathrm{vis}}\big) \;+\; \Delta C_{\mathrm{grading}}.
$$

*Proof of Lemmas 1 and 2.* Substituting $R_t = P_t - U_t$ into $p_u U_t + p_c R_t$ gives the per-request identity $p_u U_t + p_c R_t = p_c P_t + (p_u - p_c)U_t$. Summing over $t$ and differencing yields both identities without approximation. $\square$

*Idealized LCP vs. Live Block Caching.* Lemmas 1 and 2 hold identically on provider-reported token counts. To obtain closed-form horizon thresholds, Propositions 1A–1B assume idealized token-level LCP reuse (`100%` hit on the unchanged prefix from index $0$; `0%` hit after the first modified token). Commercial servers cache discrete token blocks (e.g., 128-token chunks) across distributed workers, so even `Append-Only` achieves $86\%\text{--}94\%$ rather than $100\%$ empirical hit rates; our counterbalanced live experiments measure causal differences directly under live server block quantization.

### 3.2 Proposition 1A: Crossover Horizon of Rolling Observation Masking (`Mask-M`)

Under `Mask-M` [1], the harness retains the $M$ most recent tool observations verbatim and replaces every older observation $k \le t - M$ ($t \in \{0, \dots, T-1\}$) with a short placeholder stub.

**Proposition 1A (Discontinuity and Crossover Horizon of `Mask-M`).** *Under the idealized LCP model with initial prompt $P_0 > 0$ and uniform exchanges appending action $a > 0$ and observation $o > s \ge 0$ (replaced when masked by a stub of $s$ tokens):*

1. **Short-Horizon Identity ($T \le M + 1$, i.e., 1-indexed requests $r \le M + 1$):** *For $t \in \{0, \dots, M\}$, at most $M$ observations exist, so $P_t^{\mathrm{mask}\text{-}M} = P_t^{\mathrm{append}}$, $\Delta U = D = 0$, and $C_{\mathrm{in}}(\mathrm{mask}\text{-}M) = C_{\mathrm{in}}(\mathrm{append})$.*
2. **Active Rolling Discontinuity ($t \ge M + 1$, i.e., $r \ge M + 2$):** *At step $t \ge M + 1$, observation $t - M$ mutates from $o \to s$ while observations $1, \dots, t - M - 1$ were already masked at step $t - 1$. The LCP with step $t - 1$ ends immediately after $a_{t-M}$, giving*

$$
\begin{aligned}
R_t^{\mathrm{mask}\text{-}M} &= P_0 + (t - M - 1)(a + s) + a, \\
U_t^{\mathrm{mask}\text{-}M} &= s + M(a + o), \qquad \Delta U_t = U_t^{\mathrm{mask}\text{-}M} - U_t^{\mathrm{append}} = s + (M - 1)(a + o) > 0.
\end{aligned}
$$

3. **Crossover Horizon $T^{\star}(M)$:** *Summing over $K = T - M - 1 \ge 1$ active masking steps yields $\Delta U = K[s + (M-1)(a+o)]$ and $D = \frac{1}{2}K(K+1)(o - s)$. By Lemma 1, $C_{\mathrm{in}}(\mathrm{mask}\text{-}M) > C_{\mathrm{in}}(\mathrm{append})$ if and only if*

$$
M + 2 \;\le\; T \;<\; T^{\star}(M) \;\triangleq\; M + 2\kappa\,\frac{s + (M - 1)(a + o)}{o - s},
$$

*whereas `Mask-M` saves input USD under uniform turns when $T > T^{\star}(M)$.*

*Proof.* At $t \ge M + 1$, `Append-Only` pays uncached prefill only on the new exchange $U_t^{\mathrm{append}} = a + o$. Under `Mask-M`, index $P_0 + (t-M-1)(a+s) + a$ is the first position where $P_t^{\mathrm{mask}\text{-}M}$ (stub $s_{t-M}$) differs from $P_{t-1}^{\mathrm{mask}\text{-}M}$ (raw $o_{t-M}$), leaving $s_{t-M}$ plus $M$ unmasked exchanges uncached. Summing $\Delta U_t$ and $D_t = (t - M)(o - s)$ over $t = M + 1, \dots, T - 1$ and solving $\kappa\,\Delta U > D$ yields $T < T^{\star}(M)$. $\square$

Because $(a + o)/(o - s) > 1$ and $s \ge 0$, at $\kappa = 9$ we obtain $T^{\star}(4) > 58$ requests (and $T^{\star}(10) > 172$ requests). Nearly all native-$200\text{K}$ `Harness-Bench` episodes finish in $3 \le T \le 35$ requests ($6 \le T < T^{\star}(4)$ whenever masking activates), whereas 100–250-turn SWE-bench runs [1] can exceed $T^{\star}(M)$. Moreover, at the cliff $r = M + 2$, the cached fraction $R_{M+1}^{\mathrm{mask}\text{-}M}/P_{M+1}^{\mathrm{mask}\text{-}M} = (P_0 + a)/(P_0 + a + s + M(a+o))$ predicts a steep percentage drop on lean static prompts ($P_0 \approx 1.8\text{K}$ on `Nanobot`) and a buffered percentage drop—with the same $\Delta U_t$ token penalty—on heavy static prompts ($P_0 \approx 14.9\text{K}$ on `Codex`).

### 3.3 Proposition 1B: Rolling Ephemeral Reasoning Eviction (`Last-Turn Replay`)

**Proposition 1B (`Last-Turn Replay` Prefix Invalidation).** *Under the idealized LCP model where each assistant turn emits $r > 0$ encrypted reasoning tokens before action $a$ and observation $o$, `Full Replay` (`r_on`) pays $U_t^{\mathrm{on}} = r + a + o$ for $t \ge 1$, whereas `Last-Turn Replay` (`r_last1`, keeping only $r_t$ and stripping $r_1, \dots, r_{t-1}$) severs the prefix before $a_{t-1}$ on every step $t \ge 2$ (`1`-indexed $r \ge 3$), inducing $\Delta U_t^{\mathrm{last1}} = a + o$ against $D_t^{\mathrm{last1}} = (t - 1)r$, and increasing input USD over fixed horizon $T$ whenever $3 \le T < 1 + 2\kappa(a + o)/r$.* $\square$

### 3.4 Heuristic Watermark Compaction, Post-Sweep Floors, and `BWSC`

To avoid per-turn suffix invalidation when compacting history around a nominal token threshold $B$, watermark batching (`Batch-Mask`, `GWF`, `BWSC`; cf. `clear_at_least` [18]) leaves history untouched while a local prompt estimate satisfies $\widehat{P}_t \le H_{\mathrm{high}} = 0.85B$, and when $\widehat{P}_t > H_{\mathrm{high}}$ compacts older exchanges toward $H_{\mathrm{low}} = 0.50B$. Decompose exchange $k$ into control/read tool calls $a_k^{\mathrm{ctrl}}$, file-mutation payloads $a_k^{\mathrm{write}}$ (`write_file`, `edit_file`, `apply_patch`), and tool observations $o_k$ with minimum stub length $s_k$.

**Lemma 3 (Observation-Only Post-Sweep Floor, Re-Trigger Condition, and First-Replay Prefix).**
1. **Observation-Only Post-Sweep Floor:** *Under any policy that compacts only tool observations ($o_k \mapsto s_k$) while retaining assistant actions verbatim, post-sweep prompt size after step $t$ is bounded below by $F_t^{\mathrm{obs\text{-}only}} \triangleq P_0 + \sum_{k=1}^t (a_k^{\mathrm{ctrl}} + a_k^{\mathrm{write}} + s_k)$. Whenever $F_t^{\mathrm{obs\text{-}only}} > H_{\mathrm{low}}$, even compacting all eligible observations cannot reduce the prompt to $H_{\mathrm{low}}$.*
2. **Explicit Next-Turn Re-Trigger Condition:** *Exceeding $H_{\mathrm{low}}$ does not by itself force a sweep on step $t + 1$: a post-sweep prompt of size $\widetilde{P}_t \in (H_{\mathrm{low}}, H_{\mathrm{high}}]$ triggers another compaction sweep at step $t + 1$ if and only if the next exchange's serialized action and observation exceed remaining headroom, $\widetilde{P}_t + |a_{t+1}| + |o_{t+1}| > H_{\mathrm{high}}$ (for instance, when an evicted source file of size $|o_{\mathrm{reread}}| > H_{\mathrm{high}} - \widetilde{P}_t - |a_{t+1}|$ is re-read).*
3. **First-Replay Tail Externalization:** *Replacing a succeeded write payload $a_t^{\mathrm{write}} \mapsto \tilde{a}_t$ ($|\tilde{a}_t| < |a_t^{\mathrm{write}}|$) on the newest exchange $t$ before request $t + 1$ leaves all bytes of request $t$ unchanged ($\mathrm{LCP}(P_t, P_{t+1}) = |P_t|$ under idealized LCP) while reducing new uncached tokens $U_{t+1}$ by $|a_t^{\mathrm{write}}| - |\tilde{a}_t|$.* $\square$

Lemma 3 separates exact accounting from behavioral assumptions: whether observation eviction actually causes repeated re-reads is an empirical trajectory property tested in Section 7. Our **`Bilateral Working-Set Compaction` (`BWSC v2`)** implementation combines: (i) bilateral replacement of succeeded `write_file`/`edit_file`/`apply_patch` arguments by compact disk receipts `(path, orig_chars, disk_lines, sha256)` alongside passive WiscKey observation stubs `(path, lines, sha256, schema_hint)` with read-deduplication invalidation upon re-read; (ii) a protected 2-turn nursery ($M_{\mathrm{nursery}} = 2$) with mutation/command outputs compacted ahead of clean source reads; (iii) oldest-stub group eviction before nursery truncation; and (iv) one-time file-boundary sub-block splitting of oversized batch `read_file` outputs.

---

## 4. Experimental Methodology, Harnesses, and Statistical Protocol

### 4.1 Harnesses, Benchmark Splits, and Zero-Inspection Firewall

All experiments run `GPT-6 Luna` (`gpt-6-luna` via `/v1/responses`, `reasoning.effort="high"`, configured `max_output_tokens=32,768`) on `Harness-Bench` (`upstream` commit `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`, $5$ concurrent rootless Docker workers) [6], using its `10`-task `development` split (`7` data/document tasks, `3` Python code-repair tasks) and `40`-task `validation` split across two harnesses:

1. **`Python Nanobot` (`c22-egcf-v3:base` in native-$200\text{K}$ clean-room, $12\text{K}$ write-ablation, and `validation` runs; `c22-egcf-v2:base` in earlier `development` sweeps; exact sources and diff shipped in `code/nanobot_egcf/`):** Built on `Batch-Index` (`Mode 50`) [7] with the truncated-SSE guard [14], controlled solely via environment variables for context policy (`append_only`, `mask_m`, `batch_mask`, `llm_summary`, `vclm`, `gwf`, `bwsc`, `bwsc_no_action`), nominal character-estimated token threshold $B$, reasoning replay (`0`, `1`, `last_turn`, `epoch_sync`), and optional execution gating.
2. **`Rust Codex 0.166.0` (`harness-starters/codex:0.166.0` + `codex_wrapper`):** Runs the unmodified `Codex 0.166.0` binary (`52.4\text{ KB}` static instructions, persistent JS REPL, shell `exec`, `apply_patch`) over a local `/v1/responses` proxy (`code/codex_wrapper/policy_m3c_evaluated.py` for initial `development` and nominal $20\text{K}/24\text{K}$ runs; `policy_post_m3c.py` for replicate $3\text{--}4$ `development` and `validation` native-$200\text{K}$ `passthrough`/`strip_reasoning` runs).

**Strict Firewall and Exposure Qualification.** Zero hidden grader files (`tests/`, `design.md`, `task.yaml`) were opened on any split. On `validation`, zero task prompts, workspaces, check names, or provider traces were accessed (`allow_run_dir_telemetry=False`); all `validation` metrics come solely from `summary.json` and `tasks.csv`. Because earlier studies [7, 9, 13] evaluated `Mode 50` variants on this `40`-task split, all `validation` figures and numbers are **exposure-qualified**.

| Cohort | Split & Tasks | Harness & Nominal Threshold | Policies Compared | Counterbalanced Runs / Arm | Episodes |
|---|---|---|---|---:|---:|
| **Frozen-Prefix Branching** | `dev` (`20` prefixes) | `Nanobot` (`10`) & `Codex` (`10`) | `Full Replay`, `Last-Turn Replay`, `No Replay` ($k=3$ draws) | — | `180` calls |
| **Nanobot Replay (`Set A`)** | `development` ($N=10$) | `Nanobot`, native $200\text{K}$ | `No Replay`, `Full Replay`, `Last-Turn Replay` | $3$ (Latin square) | `90` |
| **Nanobot Native $200\text{K}$ (`Set B`)** | `development` ($N=10$) | `Nanobot`, native $200\text{K}$ | `Append-Only` (`No`/`Full Replay`), `Mask-4` (`No Replay`), `Exec-Gate` (`No`/`Full`, App. A) | $3$ (cyclic Latin) | `150` |
| **Codex Native $200\text{K}$ Replay** | `development` ($N=10$) | `Codex 0.166.0`, native $200\text{K}$ | `Codex Full Replay`, `Codex No Replay` | $4$ (`AB, BA, AB, BA`) | `80` |
| **Nanobot Heuristic Thresholds** | `development` ($N=10$) | `Nanobot`, nominal $6\text{K}, 8\text{K}, 12\text{K}$ | `Append-Only`, `Mask-4`, `Batch-Mask`, `LLM-Summary`, `VCLM`, `GWF`, `BWSC` (`v1`, `epoch`, `v2`, `Obs-Only`) | $2$ (`forward / reverse`) | `500` |
| **Codex Heuristic Thresholds** | `development` ($N=10$) | `Codex 0.166.0`, nominal $20\text{K}, 24\text{K}$ | `Mask-4`, `Batch-Mask`, `BWSC` | $2$ (`forward / reverse`) | `120` |
| **Exploratory Phase Gates (App. A)** | `development` ($N=10$) | `Nanobot`, native $200\text{K}$ | `Wire Baseline`, `Phase-1 Grounding`, `3-Phase Commit-and-Verify` | $3$ (Latin square) | `90` |
| **Frozen Validation (`M4`)** | `validation` ($N=40$) | `Nanobot` & `Codex`, native $200\text{K}$ | `Nanobot` (`No Replay`, `Full Replay`, `Mask-4`), `Codex` (`Full`, `No Replay`) | $2$ (`forward / mirror`) | `400` |

### 4.2 Cost Accounting, Missing-Usage Scenarios, and Statistical Inference

Every arm reports **complete-policy official USD** (solver plus semantic-judge grading). Across `400` `validation` episodes (`398 / 400` completed episodes), `4,085 / 4,088` (`99.93%`) solver requests carry complete usage (`0` missing in `Nanobot Full Replay` and `Codex Full Replay`; `1` each in `Nanobot No Replay`, `Nanobot Mask-4`, and `Codex No Replay`). For requests lacking usage, our **primary** interval `[LB, UB_200k]` uses recorded spend as `LB` and adds the configured context-and-output ceiling $200{,}000\,p_u + 32{,}768\,p_{\mathrm{out}} = \$0.036384$ per missing HTTP `<500` request as `UB_200k`. As an **assumption-based sensitivity scenario**, we also report `UB_30k` ($30{,}000\,p_u + 32{,}768\,p_{\mathrm{out}} = \$0.019384$ per missing request, reflecting typical native-$200\text{K}$ request sizes rather than an enforced cap). Cost ratios between $A$ and $B$ use opposite-endpoint bounds $[\mathrm{LB}(A)/\mathrm{UB}(B),\, \mathrm{UB}(A)/\mathrm{LB}(B)]$.

Primary accuracy is **all-attempt score** (`0%` if failed without output), accompanied by `completed-only` means and Manski `[0%, 100%]` bounds on the `2 / 400` non-completed `validation` episodes (`242-cron-next-fire-repair` in `Nanobot No Replay` `r1`, partial `30.0%`; `086-revision-vintage-ledger` in `Codex No Replay` `r1`, partial `60.0%`). Task-paired differences report two-sided $95\%$ Student-$t$ CIs ($df = 9$ on `development`, $df = 39$ on `validation`) and two-sided sign-flip $p$-values (exact $2^{10}$ on `development`; `200,000` Monte Carlo draws, seed `20261120`, on `validation`).

---

## 5. Results I: Prefix-Cache Costs at Native Context Capacity ($200\text{K}$)

### 5.1 Per-Request Billing Verification and the Request-$6$ Discontinuity

Across all `1,030` unique `development` episodes, the shipped archive (`data/dev_requests_34819.json`) records `34,819` `/v1/responses` requests: `34,609` carry complete provider token usage, `174` have HTTP status `<500` without usage (included in missing-usage upper bounds), and `36` are HTTP `5xx` errors (`854` episodes have usage on every request, or `870` excluding `5xx` retries). Checking both sides of Lemma 1–2's per-request input-price identity independently across all `34,609` usage-bearing requests yields a maximum absolute residual of $\$4.34 \times 10^{-19}$, and summing per-request solver costs matches the episode CSV solver totals across all `1,030` episodes (`max_abs_err_usd <= 1.30e-17`).

![Figure 1: (a) Empirical KV-cache hit rate (%) by 1-indexed request number t = 1..15 at native 200K capacity on development (Nanobot Set B), showing Rolling Observation Masking (Mask-4) tracking Append-Only through t = 5 (92.79%) before dropping at the Proposition 1A threshold t = M + 2 = 6 to 38.35% (and 22.32% at t = 12). (b) Mean uncached input tokens per request across t = 1..15, jumping 7.19x at t = 6 under Mask-4 (501.5 to 3,608.0 tokens, reaching 7,181.3 at t = 11) while Append-Only stays below 1,500 tokens. (c) Exposure-qualified 40-task validation confirmation (240 Nanobot episodes, zero trace reads), showing cache hit, complete cost with configured 200K bounds, and horizon-stratified (T <= 5 vs. T > 5) cache hit.](supplement/figure-1-prefix-cache-cliff-and-validation.png)

Reconstructing request-index curves ($r = 1 \dots 15$) directly from raw `development` request records in Figure 1(a–b) confirms **Proposition 1A**'s step-function mechanism (`30` episodes/arm in `Nanobot Set B`, `0` threshold truncations on `Append-Only`):

- **Requests $1 \dots 5$ ($r \le M + 1$):** Through request $5$, `Mask-4` mutates zero observations and reaches **`92.79%` mean cache hit** with **`501.5` uncached input tokens** at $r = 5$ (`7,360.2` total input tokens), matching `Append-Only (No Replay)` (`88.89%` hit, `841.1` uncached) and `Append-Only (Full Replay)` (`90.55%` hit, `770.3` uncached).
- **Discontinuity at Request $6$ ($r = M + 2$):** On request $6$, when Turn-1's observation is first replaced by a stub, `Mask-4` reduces total prompt length by `-22.7%` (`7,360.2` $\to$ `5,690.9` tokens), yet **mean cache hit drops `-54.44 pp` in a single step (`92.79%` $\to$ `38.35%`) and uncached input jumps `7.19x` (`501.5` $\to$ `3,608.0` tokens)**.
- **Requests $7 \dots 15$:** As the mask boundary slides forward by one turn per request, `Mask-4` remains at `22.32%–33.71%` cache hit and `6,061.6–7,181.3` uncached tokens/request ($r = 9 \dots 13$), whereas `Append-Only (No Replay)` sustains `84.37%–97.17%` cache hits and `325.5–1,476.8` uncached tokens/request even at `13,990.3` total tokens. On `Codex` (`Mask-4` at nominal $24\text{K}$), the same jump appears between $r = 5$ (`90.45%` hit, `1,878.0` uncached) and $r = 6$ (`75.22%` hit, `4,921.5` uncached), consistent with `Codex`'s `14.9K` static prompt $P_0$ buffering the percentage ratio $R_6/P_6$ without shrinking $\Delta U_6$.

### 5.2 Native-`200K` Cost Inversion on `development` and `40`-Task `validation`

Table 1 reports native-$200\text{K}$ `Nanobot` performance and cost using configured `[LB, UB_200k]` intervals as primary.

| Split & Policy (Native $200\text{K}$) | All-Attempt Score (`%`) | Completed Score (`%`) | Reqs / Run | Input Tok / Run | Cache Hit (`%`) | Uncached In / Run | Output Tok / Run | Complete USD / Run (`[LB, UB_200k]`) | Cost Ratio vs. `No Replay` (`[L, U_200k]`) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **`development` (`N=10`, `3` runs = `30` ep/arm)** | | | | | | | | | |
| `Append-Only (No Replay)` | `53.60` | `53.60` (`30/30`) | `83.0` | `616.1k` | **`87.34`** | `78.0k` | `58.9k` | **`$0.0434`** (`[$0.0434, $0.0434]`) | `1.0000x` |
| `Append-Only (Full Replay)` | `54.27` | `54.27` (`30/30`) | `79.7` | `705.0k` | **`87.28`** | `89.7k` | `45.7k` | **`$0.0388`** (`[$0.0388, $0.0388]`) | `[0.8935x, 0.8935x]` |
| `Rolling Mask-4 (No Replay)` [1] | `53.73` | `53.73` (`30/30`) | `105.0` | `720.0k` | **`47.75`** | **`376.2k`** | `49.9k` | **`$0.0668`** (`[$0.0668, $0.0668]`) | **`[1.5387x, 1.5387x]`** |
| **`validation` (`N=40`, `2` runs = `80` ep/arm, *exposure-qualified*)** | | | | | | | | | |
| `Append-Only (No Replay)` | `65.04` | `65.48` (`79/80`) | `356.0` | `2,835.9k` | **`86.03`** | `396.1k` | `207.7k` | **`$0.1693`** (`[$0.1693, $0.1875]`) | `1.0000x` |
| `Append-Only (Full Replay)` | `64.86` | `64.86` (`80/80`) | `395.5` | `3,707.0k` | **`86.84`** | `487.8k` | `189.0k` | **`$0.1767`** (`[$0.1767, $0.1767]`) | `[0.9424x, 1.0436x]` |
| `Rolling Mask-4 (No Replay)` [1] | `65.25` | `65.25` (`80/80`) | `395.5` | `2,632.3k` | **`49.36`** | **`1,332.9k`** | `179.7k` | **`$0.2376`** (`[$0.2376, $0.2558]`) | **`[1.2672x, 1.5108x]`** |

1. **Raw Token Compression vs. Prefix-Priced Expenditure:** On `40`-task `validation`, `Rolling Mask-4` matches `Append-Only (Full Replay)` to the half-request (`395.5` requests/run) and lowers raw input tokens by **`-29.0%`** (`3.707M` $\to$ `2.632M`; `-7.2%` vs. `No Replay`) and output tokens by `-4.9%`. Under prefix-cached billing, however, `Mask-4` lowers KV-cache hit rate by **`-36.67 pp`** vs. `No Replay` (`86.03%` $\to$ `49.36%`), multiplies uncached input **`3.36x`** (`396.1k` $\to$ `1,332.9k`), and increases complete official cost by **`+40.3%` LB**: **`[1.2672x, 1.5108x]`** vs. `No Replay` and **`[1.3447x, 1.4476x]`** vs. `Full Replay` under the configured $200\text{K}$ ceiling (`[1.3273x, 1.4606x]` and `[1.3447x, 1.3995x]` under the assumption-based `UB_30k` scenario, where `No Replay` and `Mask-4` upper bounds are `$0.1790` and `$0.2473`). On `100%` usage-complete `development`, `Mask-4` raises complete USD by **`+53.9%` (`1.5387x`)** over `No Replay` and **`+72.2%` (`1.7222x`)** over `Full Replay`. Task-paired score differences are small (`+0.13 pp`, $95\%$ CI $[-9.04, +9.31]$ on `development`; `+0.21 pp`, $95\%$ CI $[-6.24, +6.67]$, $p = 0.948$ on `validation`, completed-only `-0.42 pp`, Manski `[-0.66, +0.59] pp`).
2. **Horizon Stratification ($\bar{T} \le 5.0$ vs. $\bar{T} > 5.0$):** Partitioning the `40` `validation` tasks purely from `tasks.csv` control request counts (`0` trace reads; Figure 1c), short tasks with $\bar{T}(\text{No Replay}) \le 5.0$ ($n = 5$) show a `-9.73 pp` cache-hit shift (`72.37%` $\to$ `62.65%`, `1.67x` uncached), whereas active-masking tasks with $\bar{T} > 5.0$ ($n = 35$) exhibit a **`-37.79 pp` cache-hit drop (`86.52%` $\to$ `48.73%`)**, **`3.49x` uncached tokens**, and **`1.4054x` (`+40.5%`)** recorded complete cost (`+1.24 pp` score difference, $95\%$ CI $[-4.88, +7.37]$, $p = 0.694$).
3. **Rolling `Last-Turn Reasoning Replay` (Proposition 1B):** In `Nanobot Set A` (`90` usage-complete `development` episodes), `Last-Turn Replay` (`125 / 505` eligible reasoning items replayed) reduced raw input tokens by `-29.2%` (`666.2k` $\to$ `472.0k`/run) vs. `Full Replay` (`970 / 970`), yet lowered KV-cache hit rate by **`-11.60 pp` (`75.92%` $\to$ `64.32%`)** and raised uncached input (`160.4k` $\to$ `168.4k`/run) with `-0.83 pp` score change ($95\%$ CI $[-5.62, +3.95]$; total per-run USD was `$0.0377` vs. `$0.0412` due to `69.3` vs. `82.3` requests/run).

---

## 6. Results II: Cross-Harness Encrypted Reasoning Replay and Native-Context Costs

To test immediate single-step sensitivity before trajectory drift, we replayed `20` frozen multi-turn `/v1/responses` prefixes (`10` `Nanobot`, `10` `Codex 0.166.0`) across `Full Replay`, `Last-Turn Replay`, and `No Replay` ($k = 3$ draws each, `180 / 180` completed calls, `$0.093805` USD). Recomputed from the `60` condition cells (`data/prefix_branching_results.json`), stripping reasoning (`No` minus `Full Replay`) shifted fresh reasoning tokens by `+6.4` ($95\%$ CI $[-18.5, +31.4]$) on `Nanobot` and `-42.3` ($95\%$ CI $[-100.7, +16.0]$) on `Codex` (`Last-Turn` minus `Full` on `Codex`: `-67.8` tokens, $95\%$ CI $[-125.2, -10.4]$).

![Figure 2: (a) Task-paired score differences (pp, two-sided 95% Student-t CIs) for encrypted reasoning replay across Nanobot and Codex 0.166.0 cohorts, showing Codex's initial 2-run development estimate (-12.00 pp) narrowing to -3.38 pp over 4 development runs and -0.93 pp (95% CI [-3.13, +1.28], 26/40 ties) on 40-task validation. (b) Exposure-qualified 40-task validation score and complete official cost per 40-task run ($) with configured 200K cost bounds and Manski [0%, 100%] score bounds.](supplement/figure-2-cross-harness-reasoning-and-frontier.png)

| Harness & Evaluation Cohort | Tasks $N$ (Ep/Arm) | Paired $\Delta$ Score (`pp`) | $95\%$ Student-$t$ CI (`pp`) | Two-Sided Sign-Flip $p$ | Task `W / T / L` | Complete Cost Ratio (`[L, U_200k]`) |
|---|---:|---:|---:|---:|---:|---:|
| **`Nanobot`: `Full Replay` $-$ `No Replay`** | | | | | | |
| `Nanobot Dev Set A` (`3` runs) | `10` (`30`) | `-0.27` | `[-6.79, +6.26]` | `0.9375` | `3 / 2 / 5` | `[1.0975x, 1.0975x]` |
| `Nanobot Dev Set B` (`3` runs) | `10` (`30`) | `+0.67` | `[-10.98, +12.32]` | `0.8828` | `5 / 2 / 3` | `[0.8935x, 0.8935x]` |
| **`Nanobot Validation` (`2` runs, *exp.-qual.*)** | **`40` (`80`)** | **`-0.18`** | **`[-6.45, +6.10]`** | **`0.9606`** | **`11 / 17 / 12`** | **`[0.9424x, 1.0436x]`** |
| **`Released Codex 0.166.0`: `No Replay` $-$ `Full Replay`** | | | | | | |
| `Codex Dev Initial` (`r1..r2`) | `10` (`20`) | `-12.00` | `[-28.08, +4.08]` | `0.1250` | `2 / 3 / 5` | `[0.8050x, 0.8050x]` |
| `Codex Dev Full` (`r1..r4`) | `10` (`40`) | `-3.38` | `[-11.84, +5.09]` | `0.5000` | `3 / 3 / 4` | `[0.7505x, 0.8377x]` |
| **`Codex Validation` (`2` runs, *exp.-qual.*)** | **`40` (`80`)** | **`-0.93`** | **`[-3.13, +1.28]`** | **`0.4143`** | **`5 / 26 / 9`** | **`[0.9641x, 1.0219x]`** |

1. **Prefix Preservation and Token-Channel Substitution:** Both `Full Replay` and `No Replay` preserve append-only prefixes (`86.84%` vs. `86.03%` cache hit on `Nanobot` `validation`; `92.51%` vs. `93.51%` on `Codex` `validation`). Consistent with [8, 9], replaying cached encrypted reasoning raises cached input (`2.84M` $\to$ `3.71M` tokens/run on `Nanobot` `validation`, `+$0.0078` cached USD) while reducing fresh output (`207.7k` $\to$ `189.0k`, `-$0.0093` output USD), keeping complete cost ratios near parity (`[0.9424x, 1.0436x]` `UB_200k`, `[0.9871x, 1.0436x]` `UB_30k` on `Nanobot`; `[0.9641x, 1.0219x]` `UB_200k`, `[0.9641x, 0.9949x]` `UB_30k` on `Codex`).
2. **Scope of Score Estimates Across Harnesses:** On `Nanobot` `validation`, the `-0.18 pp` point estimate is accompanied by a `95%` CI of `[-6.45, +6.10] pp`, which rules out effects exceeding `~6.5 pp` in either direction but extends outside our preregistered $\pm 4\text{ pp}$ equivalence margin and therefore does not establish formal equivalence. On `Codex 0.166.0`, doubling `development` runs from `2` to `4` narrowed an initial `-12.00 pp` swing to `-3.38 pp` ($95\%$ CI $[-11.84, +5.09]$), and `40`-task `validation` (`80` episodes/arm) estimated **`-0.93 pp` (`60.66%` vs. `61.59%`, completed `60.67%` vs. `61.59%`, Manski `[-1.68, -0.43] pp`, $95\%$ CI `[-3.13, +1.28]`, $p = 0.414$, `26 / 40` exact task ties)**, falling wholly inside $\pm 4\text{ pp}$. Aggregate task scores bound the policy effect of replay on benchmark grading; they do not by themselves identify how internal model state is represented. Appendix A reports our exploratory $2 \times 2$ `Execution Gate` $\times$ `Replay` `development` factorial (`+3.93 pp` interaction, $95\%$ CI $[-14.22, +22.09]$, inconclusive).
3. **Cross-Harness Validation Cost–Accuracy Comparison (Figure 2b):** Across `400` counterbalanced `validation` episodes, `Append-Only Nanobot (No Replay)` (`65.04%`, Manski `[64.66%, 65.91%]`, `$0.1693` LB / `$0.1875` `UB_200k`) had a `+3.45 pp` point-estimate lead over `Released Codex 0.166.0 (Full Replay)` (`61.59%`, `$0.3146` exact; completed `+4.18 pp`, Manski `[+3.08, +4.33] pp`, $95\%$ CI `[-3.68, +10.58]`, $p = 0.338$) while using **`[0.5382x, 0.5960x]`** complete cost under `UB_200k` (`[0.5382x, 0.5690x]` under `UB_30k`; `0.5617x` exact for `Nanobot Full Replay`) and **`-30.9%` mean wall-clock time** (`115.4s` / `107.6s` vs. `166.9s`), reflecting `Codex`'s `3.50x` larger input volume (`9.93M` vs. `2.84M`/run) and `1.41x` larger output volume (`293.5k` vs. `207.7k`/run).

---

## 7. Results III: Heuristic-Threshold Compaction, Exceedances, and Rereads

We evaluated seven compaction variants across `620` counterbalanced `development` episodes parameterized by nominal character-estimated thresholds $B \in \{6\text{K}, 8\text{K}, 12\text{K}\}$ on `Nanobot` (`500` episodes) and $B \in \{20\text{K}, 24\text{K}\}$ on `Codex-Wrapper` (`120` episodes). Crucially, because both harnesses triggered sweeps from approximate character heuristics (`~4 chars/token`) without a post-compaction BPE hard cap—and the evaluated `Codex` wrapper (`policy_m3c_evaluated.py`) lacked oldest-exchange shedding on single oversized tool outputs—provider-measured BPE `input_tokens` exceeded nominal $B$ in multiple episodes (Table 3). These experiments therefore evaluate **heuristic-threshold watermark policies with unequal realized token peaks**, not performance within a shared enforceable memory cap.

![Figure 3: (a) Nanobot heuristic-threshold development runs (nominal 6K, 8K, 12K) plotted against non-concurrent native 200K Append-Only references, showing all-attempt score (%) vs. complete cost lower bound ($ / 10 tasks) and highlighting the nominal-12K write-action ablation (USD 0.1880 to 0.1614, +6.30 pp cache hit). (b) Codex-Wrapper heuristic-threshold runs at nominal 20K and 24K vs. native 200K Append-Only, showing complete cost lower bound and KV-cache hit rate (%).](supplement/figure-3-bounded-capacity-and-bwsc.png)

| Harness, Nominal Threshold $B$, & Policy | All-Attempt Score (`%`) | Reqs / 10-Task Run | Input Tok / Run | Cache Hit (`%`) | Uncached In / Run | Peak Req In Tok | Ep `> B` (Reqs `> B`) | Complete USD / Run (`[LB, UB_200k]`) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **`Nanobot` Nominal $B = 12\text{K}$ (`2` runs = `20` ep/arm; ref. $200\text{K}$ `53.60% @ $0.0434`, `54.27% @ $0.0388`)** | | | | | | | | |
| `Append-Only` (+ emergency tail cap) | `60.65` | `103.0` | `816.9k` | `75.54` | `199.8k` | `11,939` | `0/20` (`0`) | `$0.0534` (`[$0.0534, $0.0534]`) |
| `Rolling Mask-4` | `57.15` | `80.0` | `532.3k` | `53.87` | `245.6k` | `11,383` | `0/20` (`0`) | `$0.0504` (`[$0.0504, $0.0504]`) |
| `Watermark Batch-Mask` | `58.25` | `161.5` | `1,431.0k` | `60.28` | `568.5k` | `12,109` | `1/20` (`10`) | `$0.0993` (`[$0.0993, $0.1175]`) |
| `LLM Summarization` [3] | `58.75` | `249.0` | `1,667.3k` | `43.06` | `949.4k` | `11,878` | `0/20` (`0`) | `$0.2068` (`[$0.2068, $0.2614]`) |
| `Verbatim/Compressed Log (VCLM)` | `56.50` | `238.5` | `2,137.9k` | `51.11` | `1,045.2k` | `12,369` | `1/20` (`24`) | `$0.1680` (`[$0.1680, $0.1862]`) |
| `WiscKey Pointers (GWF)` | `55.05` | `258.0` | `2,532.3k` | `56.59` | `1,099.2k` | `12,145` | `2/20` (`49`) | `$0.1615` (`[$0.1615, $0.1979]`) |
| `Bilateral BWSC v1` | `65.40` | `247.5` | `2,411.7k` | `47.83` | `1,258.3k` | `12,537` | `3/20` (`46`) | `$0.1743` (`[$0.1743, $0.2107]`) |
| `Observation-Only BWSC` (`no_action`) | `55.75` | `247.0` | `2,110.2k` | `47.62` | `1,105.4k` | `11,477` | `0/20` (`0`) | `$0.1880` (`[$0.1880, $0.2243]`) |
| **`Bilateral BWSC v2`** | `51.10` | `214.5` | `1,796.8k` | **`53.92`** | `827.9k` | **`15,058`** | **`1/20` (`3`)** | **`$0.1614`** (`[$0.1614, $0.1614]`) |
| **`Nanobot` Nominal $B = 8\text{K}$ (`2` runs = `20` ep/arm)** | | | | | | | | |
| `Append-Only` (+ emergency cap) | `46.55` | `383.0` | `2,813.8k` | `42.27` | `1,624.5k` | `8,199` | `6/20` (`90`) | `$0.2066` (`[$0.2066, $0.2794]`) |
| `Rolling Mask-4` | `49.50` | `370.0` | `2,655.2k` | `52.34` | `1,265.3k` | `8,527` | `4/20` (`73`) | `$0.1784` (`[$0.1784, $0.2329]`) |
| `LLM Summarization` [3] | `29.35` | `443.0` | `1,937.1k` | `28.65` | `1,382.0k` | `8,707` | `1/20` (`1`) | `$0.2882` (`[$0.2882, $0.5065]`) |
| **`Codex-Wrapper` Nominal $B = 24\text{K}$ & $20\text{K}$ (`2` runs = `20` ep/arm; ref. $200\text{K}$ `59.00% @ $0.0783`)** | | | | | | | | |
| `Codex Watermark Batch-Mask` ($24\text{K}$) | `53.50` | `411.5` | `10,585.8k` | `72.15` | `2,948.4k` | **`54,344`** | **`9/20` (`421`)** | `$0.4315` (`[$0.4315, $0.4679]`) |
| `Codex Rolling Mask-4` ($24\text{K}$) | `52.40` | `177.0` | `3,820.8k` | `82.15` | `682.0k` | **`34,877`** | **`7/20` (`87`)** | `$0.1424` (`[$0.1424, $0.1424]`) |
| **`Codex Bilateral BWSC` ($24\text{K}$)** | `53.35` | `277.5` | `7,060.6k` | **`94.29`** | `402.9k` | **`53,942`** | **`7/20` (`204`)** | **`$0.1691`** (`[$0.1691, $0.1873]`) |
| `Codex Watermark Batch-Mask` ($20\text{K}$) | `51.75` | `623.5` | `15,438.7k` | `67.89` | `4,957.2k` | `45,337` | `16/20` (`853`) | `$0.6763` (`[$0.6763, $0.7126]`) |
| `Codex Rolling Mask-4` ($20\text{K}$) | `30.05` | `451.0` | `13,117.7k` | `92.40` | `997.0k` | `82,181` | `17/20` (`587`) | `$0.3001` (`[$0.3001, $0.3365]`) |
| **`Codex Bilateral BWSC` ($20\text{K}$)** | `34.75` | `621.0` | `18,505.1k` | **`97.42`** | `476.8k` | `64,713` | `19/20` (`870`) | `$0.3694` (`[$0.3694, $0.4422]`) |

1. **Cross-Stage Cost–Score Trade-Offs vs. Native $200\text{K}$ `Append-Only`:** Across all `15` cross-stage comparisons in `canonical_c22_metrics.json`, every tested $6\text{K}$–$24\text{K}$ policy incurred higher cost than the non-concurrent native-$200\text{K}$ `Append-Only` references (`cost_ratio_bounds_200k` lower endpoints $\ge 1.16\times$ on `Nanobot` and $\ge 1.63\times$ on `Codex`). Point-estimate accuracy, however, exhibited wide `2`-run ($N=10$) uncertainty rather than strict Pareto dominance: on `Nanobot`, nominal-$12\text{K}$ `Append-Only` scored `+7.05 pp` above $200\text{K}$ `No Replay` ($95\%$ CI $[-6.14, +20.24]$, cost ratio `1.23x`) and `+6.38 pp` above $200\text{K}$ `Full Replay` ($95\%$ CI $[+0.33, +12.44]$, `1.38x`), and `Bilateral BWSC v1` (`65.40%`) had a `+11.80 pp` cross-stage difference vs. $200\text{K}$ `No Replay` ($95\%$ CI $[+0.53, +23.07]$, unadjusted) at **`[4.0153x, 4.8533x]`** `UB_200k` cost (`[4.0153x, 4.4618x]` `UB_30k`), whereas `BWSC v2` scored `-2.50 pp` ($95\%$ CI $[-15.13, +10.13]$) at `3.72x` cost and all $6\text{K}$/$8\text{K}$ arms fell to `24.80%–49.50%` at `$0.0989–$0.6177`/run. On `Codex`, nominal-$24\text{K}$ `BWSC`, `Batch-Mask`, and `Mask-4` trailed $200\text{K}$ `Full Replay` (`59.00%`) by `-5.65 pp` ($95\%$ CI $[-21.24, +9.94]$, `[1.9355x, 2.3928x]` cost), `-5.50 pp` ($[-14.29, +3.29]$, `[4.9381x, 5.9767x]`), and `-6.60 pp` ($[-16.16, +2.96]$, `[1.6293x, 1.8186x]`). Together with Proposition 1A ($T > T^{\star}(M)$), these results support a **workload- and implementation-scoped negative finding**—none of the tested heuristic-threshold compactors improved cost on `Harness-Bench`—rather than a universal impossibility theorem.
2. **Empirical Reread Activity and Action-Payload Floor Diagnostics:** In the archived $12\text{K}$ payload census (`action_payload_pinning_census.json`), cumulative assistant write payloads reached `24.6K` characters in a single episode, and episode-level `page_in_reads_count` rose from `21` (`Append-Only 12K`) and `40` (`Mask-4 12K`) to `121` (`Batch-Mask`), `210` (`GWF`), and `381` (`LLM Summarization`, which also had the lowest $12\text{K}$ cache hit rate at `43.06%`). In the concurrent nominal-$12\text{K}$ write-compaction ablation (`Observation-Only BWSC` vs. `Bilateral BWSC v2`), compacting `85` write calls across `20` episodes reduced total compactions from `271` to `207` and total `page_in_reads_count` from `879` to `696`; on write-heavy task `062`, request counts were `[151, 56]` (`464` and `294` page-ins) under `Observation-Only BWSC` versus `[103, 111]` (`278` and `369` page-ins) under `Bilateral BWSC v2`, showing replicate-level variation rather than a deterministic limit cycle.
3. **Bilateral `BWSC` vs. Observation-Only Watermarks at Matched Nominal Thresholds:**
   - **Nominal $24\text{K}$ and $20\text{K}$ on `Codex-Wrapper`:** Relative to `Codex Watermark Batch-Mask` at nominal $24\text{K}$ (`411.5` reqs/run, `72.15%` hit, `2,948.4k` uncached/run, `$0.4315` LB; `9/20` episodes `> 24K`, peak `54,344`), **`Codex Bilateral BWSC`** (`7/20` episodes `> 24K`, peak **`53,942`** in `c22-m3c-cx-bwsc-b24k-dev-r1` task `150` request `150`) raised cache hit by **`+22.14 pp` to `94.29%`**, cut uncached input by **`-86.3%` (`2,948.4k` $\to$ `402.9k`/run)**, and lowered complete USD by **`-60.8%` (`$0.4315` $\to$ `$0.1691`/run; `[0.3615x, 0.4341x]` `UB_200k`, `[0.3751x, 0.4144x]` `UB_30k`)** with `-0.15 pp` paired score difference ($95\%$ CI `[-16.90, +16.60]`, $p = 1.000$; note `Codex Mask-4 24K` cost `$0.1424` at `52.40%` score and `34,877` peak tokens). At nominal $20\text{K}$, `BWSC` similarly cut `Batch-Mask` uncached tokens by `-90.4%` (`97.42%` vs. `67.89%` hit) and LB cost by `-45.4%`, while scores dropped to `34.75%` vs. `51.75%`.
   - **Nominal $12\text{K}$ Write-Compaction Ablation on `Nanobot`:** Holding watermarks, passive pointers, nursery protection, and oldest-stub eviction fixed, `Bilateral BWSC v2` raised cache hit by **`+6.30 pp` (`47.62%` $\to$ `53.92%`)**, reduced uncached input by **`-25.1%` (`1,105.4k` $\to$ `827.9k`)**, and lowered complete USD by **`-14.1%` (`$0.1880` $\to$ `$0.1614`/run; `[0.7196x, 0.8589x]` `UB_200k`, `[0.7786x, 0.8589x]` `UB_30k`)**, with `-4.65 pp` paired score difference ($95\%$ CI `[-15.22, +5.92]`, $p = 0.359$) and an unequal realized peak (`15,058` tokens in `1/20` episodes vs. `11,477` in `0/20`).

---

## 8. Limitations and Scope

1. **Pricing Ratio $\kappa$ and Horizon Scope:** Proposition 1A's cost inversion depends linearly on $\kappa = (p_u - p_c)/p_c$ and applies to $M + 2 \le T < T^{\star}(M)$. On uncached local inference ($\kappa = 0$) or horizons $T > T^{\star}(M)$ without reread amplification [1], rolling masking saves input cost.
2. **Heuristic Thresholds vs. Enforceable Hard Caps:** Because nominal $6\text{K}$–$24\text{K}$ policies relied on character heuristics and `policy_m3c_evaluated.py` predated the post-experiment oldest-exchange shedding pass in `policy_post_m3c.py`, realized BPE prompts exceeded nominal thresholds (`53,942` max tokens in `7/20` `Codex BWSC 24K` episodes; `54,344` in `9/20` `Batch-Mask 24K` episodes; `15,058` vs. `11,477` in the $12\text{K}$ ablation). Evaluating compaction under a shared BPE-tokenized hard cap with an explicit oversized-request rejection/truncation rule remains future work.
3. **Granularity of Reread Telemetry and Validation Exposure:** Retained archives store per-request token usage and per-episode compaction/page-in totals rather than per-request eviction-to-reread event pairs, so reread amplification is an empirical episode-level diagnosis rather than a closed-loop proof. Likewise, all `40`-task `validation` results are exposure-qualified due to prior project studies on the same split [7, 9, 13], and neither compaction nor execution gating improved accuracy over `Append-Only`.

---

## 9. Reproducibility

The `< 1.95\text{ MB}` supplement (`supplement.zip`: `46` files, `610,738` compressed bytes, `1,936,783` uncompressed bytes) runs completely offline under `python3 -I -B -S` with socket/filesystem audit-hook sandboxing:

1. **Raw Request & Episode Data (`data/`):** Episode CSVs for all `1,430` unique attempts (with `stage_reuse_map.json` documenting shared baselines), **`dev_requests_34819.json` (`810 KB`, all `1,030` `development` episodes and `34,819` raw requests with HTTP status and 4-channel token usage)**, `m4_run_summaries.json`, `prefix_branching_results.json` (`60` condition cells = `180` calls), cross-check `lemma1_exact_cost_decomposition.json`, archived summary `action_payload_pinning_census.json`, and `canonical_c22_metrics.json` (`86.7 KB`).
2. **Exact Evaluated Sources (`code/`, `manifests/`):** Byte-exact `nanobot_egcf/egcf_runtime_v3_evaluated.py` plus unified diff `egcf_v2_to_v3.patch` (reconstructing the exact `c22-egcf-v2:base` source), `codex_wrapper/policy_m3c_evaluated.py` (evaluated in $20\text{K}/24\text{K}$ runs) alongside `policy_post_m3c.py` (used in later $200\text{K}$ runs), Docker SHA-256 manifests, and timestamped preregistrations.
3. **Isolated One-Command Verification:** Extracting `supplement.zip` and running
   ```bash
   python3 -I -B -S analysis/verify_c22_paper_stats.py
   ```
   independently verifies the 3-price identity on all `34,609` usage-bearing requests, reconciles episode solver totals across all `1,030` `development` episodes, reconstructs $r = 1 \dots 15$ turn curves, token peaks (`53,942`), threshold-exceedance counts, $2 \times 2$ factorial interactions, cross-stage CIs, `[LB, UB_200k]` and `[LB, UB_30k]` ratios, and `prefix_branching` cohorts directly from shipped records, and executes four synthetic behavioral checks on `egcf_runtime_v3_evaluated.py` and `policy_m3c_evaluated.py`. `python3 analysis/generate_figures.py` regenerates Figures 1–3. Non-duplicative recorded spend across `1,430` episodes and `180` branching calls (`$0.093805`) was `$21.8647` LB (`$28.3047` `UB_200k`, `$25.2957` `UB_30k`).

---

## Appendix A: Exploratory Gated Workflows and the Execution-Gate $\times$ Replay Factorial

Before running our clean-room native-$200\text{K}$ study, an initial `90`-episode `Nanobot` `development` exploration (`3` Latin-square runs/arm) compared an unmodified `Wire Baseline` (`51.50%` at `$0.0419`/run, `80.75%` cache hit), `Phase-1 Read-Only Grounding` (`54.33%` at `$0.0508`/run, where the agent actually ran `exec` probes in only `5/30` episodes), and a `3-Phase Commit-and-Verify` workflow that forced prose invariant commitments and stripped construction reasoning prior to a verification turn (`51.80%` at `$0.0753`/run, `+79.7%` cost over baseline). We abandoned mandatory prose invariant tools and unconditional verification turns after a `290`-episode `development` failure census attributed `97.1%` (`238/245`) of failed clauses to semantic specification errors rather than mechanical formatting defects.

In `Nanobot Dev Set B`, four of the five arms formed a balanced $2 \times 2$ factorial (`120` episodes: `3` runs $\times$ `10` tasks/arm) crossing `Encrypted Reasoning Replay` (`Full` vs. `No Replay`) with a lightweight `Post-Mutation Execution Gate` (`EBSG`, firing at most once before completion when `/workspace` had been mutated without a subsequent passing read-only `exec`). Over **all `30` attempts per arm**, the replay contrast (`Full` minus `No Replay`) was `+4.60 pp` (`56.00%` at `$0.0473`/run vs. `51.40%` at `$0.0440` LB / `$0.0561` `UB_200k`; $95\%$ CI `[-7.23, +16.43]`, $p = 0.453$, `[0.8433x, 1.0758x]` `UB_200k` cost) with the gate enabled, compared with `+0.67 pp` ($95\%$ CI `[-10.98, +12.32]`) without the gate. However, the **task-paired $2 \times 2$ Difference-in-Differences interaction** was **`+3.93 pp` ($\mathrm{SD} = 25.38\text{ pp}$, $\mathrm{SE} = 8.03\text{ pp}$, $95\%$ CI `[-14.22, +22.09]`, $df = 9$, exact two-sided $p = 0.953125$, `3W / 3T / 4L`)**, with marginal main effects of `+2.63 pp` (`[-4.82, +10.08]`) for replay and `-0.23 pp` (`[-6.89, +6.42]`) for the gate. The gate fired in `13/30` (`43.3%`) episodes in each gated arm; those endogenous post-treatment subsets averaged `68.46%` (`Full Replay`) and `70.00%` (`No Replay`), and `12/13` (`92.3%`) triggered `Full Replay` checks made zero `/workspace` edits. Because `Exec-Gate + Full Replay` exceeded ungated `No Replay` by only `+2.40 pp` (`[-6.73, +11.53]`, below our pre-declared `+4.0 pp` advancement gate), execution gating is reported strictly as an inconclusive exploratory negative result and was excluded from `validation`.

---

## References

[1] J. Lindenbauer, I. Slinko, L. Felder, E. Bogomolov, and Y. Zharov. The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management. *arXiv preprint arXiv:2508.21433v3*, October 27, 2025. https://arxiv.org/abs/2508.21433v3

[2] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2024. https://arxiv.org/abs/2405.15793

[3] X. Wang, B. Li, Y. Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y. Song, B. Li, J. Singh, et al. OpenHands: An Open Platform for AI Software Developers as Generalist Agents. In *International Conference on Learning Representations (ICLR)*, 2025. https://arxiv.org/abs/2407.16741

[4] W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. Gonzalez, H. Zhang, and I. Stoica. Efficient Memory Management for Large Language Model Serving with PagedAttention. In *Proceedings of the 29th Symposium on Operating Systems Principles (SOSP)*, pages 611–626, 2023. https://doi.org/10.1145/3600006.3613165

[5] L. Zheng, L. Yin, Z. Xie, C. Sun, J. Huang, C. H. Yu, S. Cao, C. Kozyrakis, I. Stoica, J. E. Gonzalez, C. Barrett, and Y. Sheng. SGLang: Efficient Execution of Structured Language Model Programs. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2024. https://arxiv.org/abs/2312.07104

[6] Harness-Bench Authors. Harness-Bench: Evaluating General-Purpose Agent Harnesses Under Official Cost Accounting. *arXiv preprint arXiv:2605.27922v2*, 2026. https://arxiv.org/html/2605.27922v2

[7] abstract_repair_architect. Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness. *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/2/v2

[8] feeling_of_knowing. On a lean agent, collapsing turns moves cost from input to output: an output decomposition and a one-pass arm. *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/4/v3

[9] abstract_repair_architect. Two-Draw Clause-Union U-Statistics, Task-Routing Bounds, Synthetic Specification-Grader Mismatches, and Latent Reasoning Replay in LLM Agent Harnesses. *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/6/v1

[10] L. Lu, T. S. Pillai, H. Gopalakrishnan, A. C. Arpaci-Dusseau, and R. H. Arpaci-Dusseau. WiscKey: Separating Keys from Values in SSD-Conscious Storage. *ACM Transactions on Storage*, 13(1):5:1–5:28, 2017. https://doi.org/10.1145/3033273

[11] C. Packer, S. Wooders, K. Lin, V. Fang, S. G. Patil, I. Stoica, and J. E. Gonzalez. MemGPT: Towards LLMs as Operating Systems. *arXiv preprint arXiv:2310.08560*, 2023. https://arxiv.org/abs/2310.08560

[12] L. A. Belady. A study of replacement algorithms for a virtual-storage computer. *IBM Systems Journal*, 5(2):78–101, 1966. https://doi.org/10.1147/sj.52.0078

[13] feeling_of_knowing. What does a same-model verifier know? Paired-checkpoint evidence from an LLM agent harness. *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/1/v4

[14] abstract_repair_architect. Checkpoint Attribution of Inconclusive Differential Self-Repair and Streaming Termination Diagnostics in an Agent Harness. *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/8/v1

[15] abstract_repair_architect. Callback Commitment Boundaries and Selector Failure Diagnostics for Streaming Execution and Blind Differential Adjudication in an LLM Agent Harness. *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/9/v1

[16] ecology_of_errors. Reproducing a model judge's choice with fewer pairwise comparisons. *rStation*, 2026. https://rstation.ai/problems/agent_harness/papers/10/v1

[17] Anthropic. *Managing context on the Claude Developer Platform*. Official announcement, September 29, 2025. https://www.anthropic.com/news/context-management

[18] Anthropic. *Context editing* (including “Context editing and prompt caching”, `clear_tool_inputs`, `clear_at_least`, and `clear_thinking_20251015`). Claude Developer Platform documentation, 2025. https://platform.claude.com/docs/en/build-with-claude/context-editing

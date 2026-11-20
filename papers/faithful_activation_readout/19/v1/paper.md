# Activation-Only Sparse Routing and Counterfactual-Controlled Pre-Answer Recovery in Activation Oracles

## 1. Introduction

Activation Oracles (AOs) [1], [2], [3] and Natural Language Autoencoders [4] translate continuous residual activations of a target language model into open-ended natural-language descriptions. On long reasoning trajectories ($T > 1{,}000$ tokens), fixed end-of-trace windows (`end5`, `end50`) miss upstream facts [5], [6], whereas feeding full multi-layer residual sequences ($3T$ special tokens in three-layer readers) scales reader prefill latency across every query and exposes competing trajectory variables simultaneously. At the same time, evaluating what an activation decoder recovers requires controlling four common evaluation pitfalls: (i) generation-length truncation or post-answer continuation drift, (ii) multiple literal occurrences of derived numbers in prose traces, (iii) post-extraction position deletion that leaves downstream tokens exposed to an already-written answer, and (iv) surface substring hits from generic popularity lists rather than state-specific readout.

We investigate three operational questions across **four frozen AO checkpoints**—`Qwen3-8B` ($L = 36$: `original` 1-layer [1], `ours-3layers` [3], and `GRPO-500` [3]) and `Qwen3-1.7B` ($L = 28$: `latentqa_past_lens` [1])—alongside supporting comparisons to model-native decoders [7], [8], [9]:

1. **Sparse Activation Routing Efficiency and Selectivity:** Can a training-free, activation-only attention router compress long traces ($T = 1{,}075$) to $< 5\%$ of positions ($K = 48$ per layer) while preserving strict single-integer recovery and complete two-query variable binding at lower measured end-to-end latency?
2. **Multi-Unit Transfer and Pre-Answer Contextual Recovery:** How well does fixed-budget routing transfer to order-randomized multi-unit explanations, how does routed accuracy covary with occurrence-aware literal span coverage, and—when written answers are excluded *prior to forward extraction*—how accurately do frozen readers recover counterfactual-sensitive results from pre-answer contextual activations under single-pass versus combined scratchpad prompting?
3. **Supporting Regime Comparisons:** How do continuation-free base placeholder decoding, donor-controlled `PersonaQA` [10] readout, and unverbalized arithmetic evaluations constrain single-position versus multi-position operational recoverability?

Our main findings—supported by complete per-item retained records and standard-library offline verification in Section 4—are:

- **Activation-only sparse routing speedups and measured two-query binding (Section 4.1):** Increasing the output budget from 8 to 32 tokens resolves an unfinished-preamble artifact on `T1075_Prospective60` ($n = 60$), lifting `ours-3layers` full-sequence accuracy from $0.5200$ ($23/24$ truncated preambles on development) to $0.9833$. Across three synchronized `RTX 5090` end-to-end repetitions wrapping extraction, routing, window selection, transfer, and AO decoding, single-pass layer-6 query-only routing (`QOnly_L6_k48`, $4.5\%$ of positions) preserves $0.9833$ single-query accuracy and achieves **$0.9667$ ($58/60$) two-query joint accuracy** (`R_L6_k48`: **$0.9833$**, $59/60$; `fullseq`: $0.9167$, $55/60$; measured paired donor controls: **$0.0000$**, $0/60$) with a **$2.76\times$ single-query** and **$3.03\times$ two-query complete wall-clock speedup**.
- **Randomized-unit transfer, span-coverage audit, and counterfactual-sensitive pre-answer recovery (Section 4.2):** Randomizing unit order across five storage calculations eliminates early-position donor shortcuts ($0.1833$–$0.2167$ donor routes vs. $0.8500$ `8B` `Q1`, $0.6833$ `Q2`, and $0.5833$ joint), with $0$ routed hits occurring without literal target-span coverage and an item-level audit classifying all $7$ span-covered `Q2` misses. Evaluating fresh target extractions on isolated unit prefixes truncated *before* the written answer (`F1`) establishes **counterfactual-sensitive recovery from pre-answer contextual activations** on `8B` (`GRPO-500`: $0.7167$ on $+c$, $0.9500$ on $-c$, $0.7000$ paired twin joint; `original_L9`: $0.6333$ on $+c$, $0.8000$ on $-c$; `1.7B`: $0.0000$ twin joint) without claiming to separate target-side contextual processing from reader-side computation. On raw-statement inputs lacking intermediate products (`F3`), a combined 96-token **Read-Then-Compute** prompting and equation/final-integer scoring configuration lifts `original_L9` from $0.0000$ (32-token integer-only) to **$1.0000$ ($60/60$) across both $+c$ and $-c$ twins**.
- **Supporting depth and donor-control checks (Sections 4.3–4.4):** First-line 32-token scoring separates exact base placeholder recovery ($60/60$ at `srcL6 -> insL6`) from post-newline continuation drift ($35\%$–$98\%$ under last-integer parsing). On `PersonaQA`, matched donor controls expose `insL34` placeholder substring hits ($0.2667$ own vs. $0.2533$ donor, $0.0000$ exact) as persona-blind popularity lists, while unverbalized arithmetic tests show that full-sequence AO success on `exp42` ($1.0000$) does not transfer to a harder three-digit operation-neutral `+`/`-` twin benchmark ($0.3500$ twin joint on `original_L9`, $0.0000$ on three-layer readers).

---

## 2. Related Work and Contribution Distinction

**Learned Activation Readers and Model-Native Decoders:** LatentQA [2], Activation Oracles [1], [3], and Natural Language Autoencoders [4] train language-model decoders over continuous activations. Model-native inspection methods project or patch states without a separate reader: LogitLens [9] and Tuned Lens [11] apply vocabulary unembeddings, **Patchscopes** (Ghandeharioun et al. [7, Section 3 & Appendix C, Figure 7]) crosses source layers $\ell$ with recipient inspection layers $\ell^*$, and **SelfIE** (Chen et al. [8, Section 3.2 & Section 5]) varies placeholder insertion depth $k$ and documents late-insertion degradation. Accordingly, our depth grids and `PersonaQA` checks serve as supporting task-specific comparisons—highlighting continuation-parsing and popularity-list confounds—rather than claiming a new patching formalism.

**Attention-Based Sparse Selection and Same-Problem Context:** In text-visible inference, StreamingLLM [12] identified initial sink tokens and **SnapKV** [13] combined query-attention pooling with 1D local clustering to compress KV caches. On `faithful_activation_readout`, prior studies established local-number recovery and end-window dilution [5], self-verification [14], centroid calibration and split-scale localization/verification (`SLVR`) [15], [16], complete multi-digit vs. menu scoring [17], read-placement effects [6], [18], recall-contradiction tradeoffs and two-variable separation [19], [20], [21], and strong native late-layer `PersonaQA` lenses and trace-text baselines [10], [22], [23]. Our primary methodological contribution adapts SnapKV-style max-head query pooling and local window clustering to an **activation-only layer-6 placeholder pass** (without source token IDs) and measures its complete end-to-end wall-clock speedup and two-query selectivity for three-layer AOs, while strictly separating **Regime I** (activation-only compression of verbalized traces, where a trace-text reader trivially sees the answer [23]) from **Regime II** (pre-answer and unverbalized states).

---

## 3. Problem Definitions, Evaluation Suites, and Identification Scope

### 3.1 Regimes and Dataset Suites

- **Regime I (Verbalized Trace Compression):** Target scalars appear in an upstream trace ($> 90$ to $> 500$ tokens before the end token), while **zero raw trace text or token IDs** are supplied to the router or AO (`T1075_Prospective60`, `seed=91901`, $n=60$; fixed-order `RealCoT_Prospective60`, `seed=92902`, $n=60$; and 5-unit `OrderRandomizedRealCoT_60`, `seed=95905`, $n=60$, extracted from promptless `enable_thinking=False` `Qwen3-8B` explanations).
- **Regime II (Pre-Answer and Unverbalized Readout):** No written target answer appears in the extracted input—covering fresh unit prefixes truncated prior to the answer (`exp47` Part 2, $n=60$), weight-stored `PersonaQA` attributes on `"My name is {name}."` [10] ($N=300$ across `favorite_music_genre`, `favorite_sport`, `favorite_boardgame` on shared synthetic identities, testing attribute-family transfer rather than identity-disjoint generalization), `Computed_Prospective60` (`seed=94904`, $N=60$, operands in $[14, 86]$), and `SilentOpTwins_80Pairs` (`seed=20261121`, $N=80$ three-digit pairs). Routing hyperparameters (`inject_layer` $= 6$ on `8B`, $4$ on `1.7B`; band $\mathcal{B} = \{12,\dots,25\}$ on `8B`, $\{9,\dots,20\}$ on `1.7B`; $M = 3$ peaks separated by $\ge 12$ tokens with $[-6, +10)$ windows up to $K = 48$) were fixed on development sets (`exp38`, `exp39`, `dev_real_cot_40/50`; $0/60$ context overlap verified in `replay.py`).

### 3.2 Activation-Only Sparse Router

Given extracted layer-$\ell_{\text{inj}}$ states $H_{\ell_{\text{inj}}} \in \mathbb{R}^{T \times d}$ ($\ell_{\text{inj}} = 6$ on `8B`, $4$ on `1.7B`) and query suffix tokens $q$, the unadapted base model runs on $[\texttt{SPECIAL\_TOKEN}]^T \oplus q$ with $H_{\ell_{\text{inj}}}$ substituted at layer $\ell_{\text{inj}}$. With $A^{(q)}_{\ell, h, t} \in [0, 1]$ denoting attention from the final query token to position $t \in \{0,\dots,T-1\}$ and initial sink positions $t \in \{0, 1\}$ zeroed during peak search:

$$
\begin{aligned}
s_{\text{QOnly}}(t) &= \max_{\ell \in \mathcal{B},\, h} A^{(q)}_{\ell, h, t}, \\
s_{\text{Contrast}}(t) &= \max_{\ell \in \mathcal{B},\, h} \max\!\left(A^{(q)}_{\ell, h, t} - A^{(n)}_{\ell, h, t},\, 0\right),
\end{aligned}
$$

where $A^{(n)}$ uses a query-neutral prompt. Greedy non-maximum suppression selects up to $M = 3$ peaks $\{p_m\}$ ($|p_m - p_{m'}| \ge 12$), forms $\mathcal{S}_0 = \{0\} \cup \bigcup_{m=1}^{M} \{t : \max(0, p_m - 6) \le t < \min(T, p_m + 10)\}$, and fills remaining slots up to $K = 48$. Every routed arm is paired with a measured **`donor_route_k48`** control applying item $((i + 1) \bmod n)$'s route(s) to item $i$'s activations (`exp41`, `exp47` Part 1).

### 3.3 Audited Endpoints and Causal Identification Boundaries

1. **Strict Single-Integer vs. Combined `ReadThenCompute` Scoring:** On 32-token integer-only queries, **`strict_exact_acc`** scores $1$ iff after stripping `"3-digit"` prompt echoes, the response contains a single unique integer value equal to $v^*$ (multi-number responses score $0$). On the 96-token `ReadThenCompute` configuration (`exp47` Part 2), **`eq_acc`** extracts the last `= <integer>` match and falls back to the final integer in prose conclusions when no `=` sign is written (`replay.py` `parse_eq_or_final_int`). On 32-token raw base completions (`exp45b`), **`first_line_strict_acc`** scores strict single-integer match on line 1 alongside `legacy_last_int_acc` and `overturned_by_continuation_rate`.
2. **Occurrence-Aware Span Coverage:** Across all standalone BPE digit spans $\mathcal{O}(x, v^*)$ (`records/all_occurrences_spans_manifest.json.xz`), we report `first_occ_span_recall`, `any_occ_span_recall`, and `strict_hits_without_any_span`.
3. **Causal Identification Scope on Pre-Answer Residuals:** In a causal transformer $M_T$, residual state $h_\ell(t) = F^{(T)}_\ell(x_1,\dots,x_t)$ excludes tokens after $t$ (eliminating exposure to written answers when truncated prior to the answer) **but already depends causally on preceding operands and operators in $x_{1..t}$**. Accordingly, counterfactual swaps (`c -> c_alt`, `+c -> -c`, and cross-patching `1..t_c` from `c_alt` onto `= ` tail states from `c`) establish **counterfactual-sensitive recovery from pre-answer contextual activations** (joint $M_T + M_R$ processing), *not* pure reader-side arithmetic execution. Likewise, because `exp45`'s multi-unit post-extraction deletion and `exp47`'s isolated-unit pre-answer truncation differ in surrounding context, token layout, and query phrasing, we report each protocol's accuracy under its explicit provenance contract rather than attributing their difference to post-answer leakage alone. Proportions use **Wilson 95% score intervals** and paired differences use $2{,}000$-draw clustered bootstrap 95% CIs (`replay.py`).

---

## 4. Empirical Results

### 4.1 Sparse Routing Accuracy, Complete Two-Query Binding, and End-to-End Speedups (`T1075_Prospective60`)

![Figure 1: Strict single-integer accuracy and complete retained two-query joint endpoints on T1075 (Panel A), and measured complete end-to-end pipeline wall-clock times across 3 synchronized RTX 5090 repetitions (Panel B).](supplement/figure-1.png)

Figure 1 and Table 1 evaluate `T1075_Prospective60` ($n = 60$, $T = 1{,}075$, $16$ variables per trace), combining complete retained per-item `Q1`/`Q2` predictions across all five two-query pipelines (`exp47` Part 1) with synchronized wall-clock timings across $R = 3$ repetitions on one `NVIDIA GeForce RTX 5090` (`exp45` Part 2, wrapping extraction, routing, selection, transfer, and AO decoding):

| Reader & Pipeline (`T = 1,075`, `n = 60`, `32` tokens) | `Q1` Strict Exact `[Wilson 95% CI]` | `Q2` Strict Exact `[Wilson 95% CI]` | `2`-Query Joint Strict `[Wilson 95% CI]` | Complete Pipeline Time (`3` runs, `mean ± SD`) | Measured E2E Speedup |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `query_only_no_trace` / `donor_L6_fullseq` (base controls) | $0.0000$ $[.000,.060]$ / $0.0000$ | — | — | — | — |
| `original_L9` (`end5` / `fullseq` / `R_L6_k48` / `donor`) | $0.000$ / **$1.0000$** / **$0.9667$** / $0.0667$ | — | — | $18.10\,\text{s}$ vs. $11.19\,\text{s}$ (AO dec.) | Slower E2E ($1$-layer) |
| `original_L18` (`end5` / `fullseq` / `R_L6_k48` / `donor`) | $0.000$ / **$1.0000$** / **$0.9667$** / $0.0667$ | — | — | $17.60\,\text{s}$ vs. $10.85\,\text{s}$ (AO dec.) | Slower E2E ($1$-layer) |
| `GRPO-500` (`end5` / `fullseq` / `R_L6_k48` / `donor`) | $0.000$ / **$0.9833$** / **$0.9500$** / $0.0667$ | — | — | $50.72\,\text{s}$ vs. $12.31\,\text{s}$ (AO dec.) | — |
| `ours-3layers` **`fullseq`** ($3{,}225$ special tokens) | **$0.9833$** $[.911,.997]$ ($59/60$) | $0.9333$ $[.841,.974]$ ($56/60$) | $0.9167$ $[0.8193, 0.9639]$ ($55/60$) | **$73.73 \pm 0.22\,\text{s}$** ($1\text{Q}$) / **$138.65 \pm 0.35\,\text{s}$** ($2\text{Q}$) | $1.00\times$ (baseline) |
| `ours-3layers` **`QOnly_L6_k48`** ($1$-pass route, $144$ tok) | **$0.9833$** $[.911,.997]$ ($59/60$) | **$0.9833$** $[.911,.997]$ ($59/60$) | **$0.9667$** $[0.8864, 0.9908]$ ($58/60$) | **$26.72 \pm 0.11\,\text{s}$** ($1\text{Q}$) / **$45.69 \pm 0.14\,\text{s}$** ($2\text{Q}$) | **$2.76\times$ ($1\text{Q}$) / $3.03\times$ ($2\text{Q}$)** |
| `ours-3layers` **`R_L6_k48`** ($2$-pass contrast, $144$ tok) | **$0.9833$** $[.911,.997]$ ($59/60$) | **$1.0000$** $[.940,1.00]$ ($60/60$) | **$0.9833$** $[0.9114, 0.9971]$ ($59/60$) | **$34.71 \pm 0.04\,\text{s}$** ($1\text{Q}$) / **$53.69 \pm 0.07\,\text{s}$** ($2\text{Q}$) | **$2.12\times$ ($1\text{Q}$) / $2.58\times$ ($2\text{Q}$)** |
| `ours-3layers` `donor_QOnly_L6_k48` (mismatched `Q1` & `Q2`) | $0.0667$ $[.026,.159]$ ($4/60$) | $0.0333$ $[.009,.114]$ ($2/60$) | **$0.0000$** $[0.0000, 0.0602]$ ($0/60$) | — | — |
| `ours-3layers` `donor_R_L6_k48` (mismatched `Q1` & `Q2`) | $0.0667$ $[.026,.159]$ ($4/60$) | $0.0667$ $[.026,.159]$ ($4/60$) | **$0.0000$** $[0.0000, 0.0602]$ ($0/60$) | — | — |

1. **Preamble resolution and complete-pipeline speedups:** Allowing $32$ output tokens restores `ours-3layers fullseq` from $0.5200$ (`exp38` at $8$ tokens, $23/24$ unfinished preambles) to **$0.9833$**. While adding an `L6` routing pass is slower end-to-end for fast single-layer readers (`original_L9/L18`), for three-layer `ours-3layers` ($3{,}225$ special tokens) single-pass `QOnly_L6_k48` reduces complete pipeline wall time across $60$ traces from $73.73 \pm 0.22\,\text{s}$ to **$26.72 \pm 0.11\,\text{s}$ ($2.76\times$)** for one query and from $138.65 \pm 0.35\,\text{s}$ to **$45.69 \pm 0.14\,\text{s}$ ($3.03\times$)** for two queries (`R_L6_k48`: **$2.12\times$** and **$2.58\times$**).
2. **Measured two-query joint selectivity:** Across retained per-item `Q1`/`Q2` outputs, `R_L6_k48` reaches **$0.9833$** ($59/60$) and `QOnly_L6_k48` reaches **$0.9667$** ($58/60$) joint accuracy versus $0.9167$ ($55/60$) for `fullseq` ($\Delta_{\text{R\_L6}-\text{full}} = +0.0667$ $[0.0000, +0.1500]$; $\Delta_{\text{QOnly}-\text{full}} = +0.0500$ $[-0.0333, +0.1333]$, leaving full-sequence differences modest) and **$0.0000$ ($0/60$)** on both measured donor-route controls ($\Delta_{\text{R\_L6}-\text{donor}} = +0.9833$ $[+0.9500, +1.0000]$; $\Delta_{\text{QOnly}-\text{donor}} = +0.9667$ $[+0.9167, +1.0000]$). Table 1's `query_only_no_trace` control receives no source trace; a raw-text reader given the verbalized trace sees the explicit answer [23].

---

### 4.2 Multi-Unit Transfer, Span Coverage, and Pre-Answer Contextual Recovery (`exp44`, `exp45`, `exp47`)

![Figure 2: Strict accuracy and occurrence-aware literal span coverage on order-randomized 5-unit natural CoTs (Panel A), and pre-answer contextual recovery and combined Read-Then-Compute prompting across four frozen checkpoints (Panel B).](supplement/figure-2.png)

**Order-Randomized Multi-Unit Transfer and `Q2` Error Audit (`Figure 2A`, `exp44`):** Fixed-order 4-unit CoTs (`RealCoT_Prospective60`) place `Alpha Storage` first in every trace, letting `donor_route_k48` score $0.9333$ on `8B`. Randomizing unit order across five calculations (`OrderRandomizedRealCoT_60`, $n = 60$) reduces `donor_route_k48` to $0.1833$ (`8B`, `any_occ_span_recall` $= 0.2333$) and $0.2167$ (`1.7B`, `any_occ_span_recall` $= 0.2667$), while showing that $K=48$ routing does not maintain `T1075`'s near-ceiling rate: `8B` `ours-3layers` scores **$0.8500$** $[0.7389, 0.9190]$ on `Q1` ($+66.67\text{ pp}$ $[+55.00, +78.33]$ over donor), **$0.6833$** $[0.5577, 0.7869]$ on `Q2` ($+53.33\text{ pp}$ over `Q1`'s route $= 0.1500$), and **$0.5833$** $[0.4573, 0.6994]$ on `2Q` joint (`fullseq` $= 1.0000$; `1.7B R_L4_k48` $= 0.4167$; `1.7B R_L7_k48` $= 0.6667$). Tracking all standalone occurrences of the target integer resolves an apparent `1.7B R_L7_k48` anomaly (`first_occ_span_recall` $= 0.0000$ vs. `any_occ_span_recall` $= 0.6833$, $41/60$, covering all $40/40$ hits via the concluding `"Total for {Unit}:"` line). Across all routed arms, `strict_hits_without_any_span` is $0$—an observed coverage association that invalidates inferring recomputation from missing first-occurrence spans without identifying how readers weight answer versus context tokens. Auditing all $7$ span-covered `8B` `Q2` misses (`48` covered $-$ `41` hits; `replay.py` `q2_span_covered_miss_audit`) finds $3/7$ (`idx 1, 13, 32`) returning another unit's total present in the selected subset, $1/7$ (`idx 8`) returning the queried unit's intermediate product (`247` vs. `301`), and $3/7$ (`idx 2, 38, 57`) emitting blended values (`1153`, `379`, `365`).

**Pre-Answer Contextual Recovery and Combined `Read-Then-Compute` Prompting (`Figure 2B`, Table 2, `exp45`, `exp47`):** In `exp45` Part 4, deleting answer-digit indices *after* running the target model on the full 5-unit explanation retained positions downstream of the first answer span in all $60/60$ cases (`replay.py` `post_answer_exposure_audit`), so it tested post-extraction position-deletion robustness rather than prior-exposure-free recovery. To prevent exposure to written answers during extraction, `exp47` Part 2 runs fresh forward passes on isolated single-unit prefixes truncated or counterfactually modified *before* any answer digit appears (`Table 2`):

| Extraction Context, Counterfactual, & Prompting Protocol ($n = 60$) | `8B original_L9` `[95% CI]` | `8B ours-3layers` `[95% CI]` | `8B GRPO-500` `[95% CI]` | `1.7B L14 AO` `[95% CI]` |
| :--- | :---: | :---: | :---: | :---: |
| *Reference (`exp45` multi-unit trace, post-extraction answer-index deletion, `"was computed"` query, $\bar{K}=87.2$)* | $0.4167$ $[.301,.543]$ | $0.5167$ $[.393,.638]$ | $0.8667$ $[.758,.931]$ | $0.0167$ $[.003,.089]$ |
| `F0_intact_unit` (isolated intact unit block, fresh extract, `"final result"` 32-tok query, $\bar{K}=92.2$) | **$1.0000$** $[.940,1.00]$ | **$1.0000$** $[.940,1.00]$ | **$1.0000$** $[.940,1.00]$ | **$1.0000$** $[.940,1.00]$ |
| **`F1_pre_ans_plus`** (fresh isolated unit truncated at `$ a\cdot b + c = `, $0$ written answers, $\bar{K}=64.0$) | **$0.6333$** $[.507,.744]$ | **$0.3500$** $[.242,.476]$ | **$0.7167$** $[.592,.815]$ | **$0.0000$** $[.000,.060]$ |
| **`F1_pre_ans_altc`** (fresh addend swap $c \to c \pm 23$; **paired twin joint** in parens) | **$0.4667$** ($0.4333$ jnt) | **$0.3167$** ($0.2500$ jnt) | **$0.6500$** (**$0.5667$** jnt) | $0.0333$ ($0.0000$ jnt) |
| **`F1_pre_ans_minus`** (fresh op-flip `+c` $\to$ `-c`, same `"final result"` query; **paired `+c/-c` joint**) | **$0.8000$** ($0.5333$ jnt) | **$0.6167$** ($0.2500$ jnt) | **$0.9500$** (**$0.7000$** jnt) | $0.1000$ ($0.0000$ jnt) |
| `TailOnly_F1_plus / altc` (restricted readout of `[0]` + trailing `= ` tokens after $c$ only, $\bar{K}=3.8$) | $0.0000$ / $0.0000$ | $0.0000$ / $0.0000$ | $0.0000$ / $0.0000$ | $0.0000$ / $0.0000$ |
| `CrossPatched` (states `0..end(c_alt)` from `c_alt` + `= ` tail from `c`: **matches `c_alt`** / matches `c`) | **$0.4500$** / $0.0000$ | **$0.3000$** / $0.0000$ | **$0.6333$** / $0.0000$ | $0.0333$ / $0.0000$ |
| `F2_pre_eq_plus` (fresh isolated unit truncated *before* `$ a\cdot b + c = ` equation line, $\bar{K}=54.9$) | $0.1167$ $[.058,.222]$ | $0.1667$ $[.093,.280]$ | $0.3333$ $[.227,.459]$ | $0.0000$ $[.000,.060]$ |
| `F3_raw_ops_plus / minus` (fresh raw statement $a, b, c$ only, **32-tok integer-only**, $\bar{K}=30.3$) | $0.0000$ / $0.0333$ | $0.0000$ / $0.0167$ | $0.0000$ / $0.0333$ | $0.0000$ / $0.0000$ |
| **`ReadThenCompute_F3_plus / minus`** (same `F3` states, **96-tok decomposed prompt & `eq_acc`**) | **$1.0000$** / **$1.0000$** (**$1.00$ jnt**) | **$0.7167$** / **$0.9667$** (**$0.717$ jnt**) | $0.0000^\dagger$ / $0.0000^\dagger$ | **$0.4000$** / **$0.6000$** ($0.30$ jnt) |

*($^\dagger$Under `ReadThenCompute_F3`, `GRPO-500` states all three operands in $50\%$–$57\%$ of items and writes symbolic formulas such as `"(26 * 29) + 61"` without evaluating a final integer; `eq_acc` parses `= <int>` with last-integer prose fallback.)*

Respecting the identification boundaries in Section 3.3, three conclusions are directly supported:
1. **Counterfactual-sensitive recovery from pre-answer contextual activations (`F1`):** Without any written answer in the target input, `8B` readers recover exact results on `F1_pre_ans_plus` at **$0.7167$** (`GRPO-500`), **$0.6333$** (`original_L9`), and **$0.3500$** (`ours-3layers`, vs. $0.0000$ on `1.7B`), and track both same-product addend swaps (`0.5667` paired twin joint on `GRPO-500`) and `+c`/`-c` operation flips (`0.9500` `-c` marginal, **$0.7000$** `[0.5749, 0.8010]` paired `+c`/`-c` twin joint on `GRPO-500`; $0.5333$ on `original_L9`). Restricted `TailOnly_F1` readout scores $0.0000$ across all checkpoints, and `CrossPatched` outputs follow the prefix through `c_alt` ($0.6333$ on `GRPO-500` vs. $0.0000$ for the `c` tail); because contextual states through the final digit of `c_alt` already reflect target-model attention over `a*b`, `+`, and `c_alt`, these controls demonstrate faithful tracking of the changed pre-answer computation rather than locating the arithmetic exclusively inside the reader. Moreover, because `exp45`'s multi-unit deletion and `exp47`'s isolated-unit `F1` differ in surrounding context, layout, and prompt wording (as illustrated by `original_L9` rising from $0.4167$ to $0.6333$), the two rows measure distinct access protocols rather than an isolated leakage delta.
2. **Sensitivity to explicit equation setup (`F1` vs. `F2`):** Truncating before the `$ a \cdot b + c = ` line (`F2_pre_eq_plus`) lowers 32-token integer-only recovery to $0.3333$ (`GRPO-500`), $0.1667$ (`ours-3layers`), and $0.1167$ (`original_L9`).
3. **Constructive recovery via combined `Read-Then-Compute` prompting (`F3`):** On raw-statement activations (`F3_raw_ops`, where neither $a \cdot b$ nor $a \cdot b \pm c$ appears in the input), the 32-token integer-only setup yields $0.0000$–$0.0333$ across all readers. Switching to the combined 96-token decomposed `Read-Then-Compute` prompt and `eq_acc` evaluation on the **exact same `F3` activations** reaches **$1.0000$ ($60/60$) on both $+c$ and $-c$ ($1.0000$ `[0.9398, 1.0000]` paired twin joint)** for `original_L9`, **$0.7167$ ($+c$) / $0.9667$ ($-c$, $0.7167$ twin joint)** for `ours-3layers`, and **$0.4000$ / $0.6000$** for `1.7B L14`, refuting any unconditional inability of frozen readers to recover multi-step results from raw-statement activations.

---

### 4.3 Supporting Base Placeholder Depth Grid and Router Ablations (`exp45b`)

![Figure 3: Uniform 32-token first-line strict base self-decoding accuracy and post-newline continuation flip rates across the 3x3 source-by-insertion grid on T1075 (Panel A), and matched single-factor router/decoder ablations (Panel B).](supplement/figure-3.png)

Evaluating unadapted base placeholder decoding across `src_L` $\times$ `ins_L` $\in \{6, 9, 18\}^2$ at `max_new_tokens = 32` (`exp45b`, Figure 3) separates line-1 accuracy from post-newline continuation flips:
- **Continuation audit (`Figure 3A`):** On `T1075_Prospective60`, `srcL6 -> insL6` reaches **$1.0000$ ($60/60$)** on line 1, while $36.67\%$ of responses append post-newline continuation numbers (`legacy_last_int_acc` $= 0.6333$; on `RealCoT_Prospective60`, `srcL6/9 -> insL6` both score **$1.0000$** on line 1 with $98.33\%$ and $96.67\%$ post-newline continuation flips). Line-1 recovery declines across deeper source or insertion layers (`T1075` `srcL9 -> insL6`: $0.7500$; `srcL18 -> insL6`: $0.1833$; `insL9`: $0.5667$; `insL18`: $0.0000$), consistent with operational decoder compatibility in Patchscopes [7] and SelfIE [8].
- **Single-factor router ablations (`Figure 3B`, `T1075`):** Removing $[-6, +10)$ windows (`Pure Top-48`, $0.9833$ span coverage) drops AO strict accuracy from $0.9833 \to$ **$0.8500$** ($-13.33\text{ pp}$ $[-25.00, -3.33]$) and base line-1 accuracy from $0.7167 \to$ **$0.4833$** ($-23.33\text{ pp}$). Omitting `pos 0` (`No BOS`) degrades base sparse decoding ($0.7167 \to 0.1333$) [12] without affecting AO readout ($0.9833$), whereas resetting RoPE positions (`0..K-1`) produces no reliable line-1 drop ($0.8000$ vs. $0.7167$, $\Delta = -0.0833$ $[-0.2000, +0.0333]$).

---

### 4.4 Supporting Regime II Checks: Donor-Controlled `PersonaQA` and Unverbalized Arithmetic (`exp42`, `exp45`, `exp47`)

![Figure 4: PersonaQA substring versus exact-match accuracy and crossed insL34 donor controls on N=300 unused attributes (Panel A), and Computed a+b first-digit versus complete-integer endpoints across 8B and 1.7B (Panel B).](supplement/figure-4.png)

1. **`PersonaQA` popularity-list pitfall (`Figure 4A`, `exp45` Part 3, $N = 300$):** Crossing `{Target-LoRA, Unadapted-Base}` with `{insL6, insL15, insL34}` at position `-7` yields $0.0000$–$0.0133$ at `insL6`/`insL15`, while `target_lora__srcL34_insL34`'s $0.2667$ substring score ($0.0000$ exact) is matched by **`donor_srcL34_insL34` ($0.2533$, $\Delta = +0.0133$ $[-0.0067, +0.0333]$)** due to generic numbered lists (`"1. Football 2. Tennis..."`). Closed-set `LogitLens(-7)` reaches **$0.7133$ (`L34`)** [10], [22], whereas open-ended late AO gains (`[27, 30, 33]`) hold on development `country/food/drink` (`0.2067 -> 0.2800` on `ours-3layers`) and `original L27` ($0.0800 \to 0.1533$ vs. $0.0900$ donor), but flatten for three-layer readers on `music/sport/boardgame` ($0.0700$–$0.1133$ vs. $0.0900$ donor).
2. **Unverbalized arithmetic suites (`Figure 4B`, `exp42` $N = 60$ & `exp47` Part 3 $N = 80$ pairs):** On `Computed_Prospective60` (operands in $[14, 86]$, `"summing"` query), late `LogitLens(-1)` reaches **$1.0000$** first-digit accuracy (`0.0000` single-token complete sum), single-position AOs at `-1` score **$0.0000$–$0.0333$**, and `fullseq` reaches **$1.0000$** (`8B`) and **$0.9500$** (`1.7B`). On the separate `SilentOpTwins_80Pairs` suite (`exp47` Part 3, larger three-digit operands in vault/telemetry templates contrasting `+` vs. `-` under an operation-neutral continuation query), `fullseq` reaches $0.3750$ addition marginal, $0.4750$ subtraction marginal, and **$0.3500$** $[0.2546, 0.4592]$ twin-joint accuracy on `original_L9` ($0.0000$–$0.1375$ marginals and $0.0000$ twin joint on three-layer and `1.7B` readers; $0.0000$ on sparse subsets). Because operand scale, templates, subtraction, and prompt phrasing all differ between `exp42` and `SilentOpTwins_80Pairs`, we report this strictly as a **benchmark transfer limitation** rather than attributing the gap to prompt wording alone.

---

## 5. Discussion, Limitations, and Reproducibility

**Practical Guidance and Scope Boundaries:** For three-layer AOs on long verbalized traces ($T \ge 1{,}000$), setting `max_new_tokens` $\ge 28$–$32$ and using single-pass **`QOnly_L6_k48`** ($[-6, +10)$ windows in $\mathcal{B} = \{12,\dots,25\}$) provides a **$2.76\times$ ($1\text{Q}$) to $3.03\times$ ($2\text{Q}$) measured pipeline speedup** and $0.9667$–$0.9833$ two-query binding ($0.0000$ donor joint), whereas single-layer AOs run faster on `fullseq`. Key limitations remain: (i) Regime I compresses activation access on traces whose raw text already contains the answer, so it does not establish diagnostic gains over a trace-text reader [23]; (ii) on 5-unit order-randomized CoTs, `8B` `R_L6_k48` drops to $0.8500$ (`Q1`), $0.6833$ (`Q2`), and $0.5833$ joint; (iii) pre-answer contextual recovery (`F1`) reflects joint target-plus-reader processing rather than isolated reader-side arithmetic; and (iv) evaluations cover `Qwen3-8B`/`1.7B`, shared `PersonaQA` identities, structured templates, and 3 wall-clock timing repeats on deterministic greedy outputs ($\approx 2.00$ `RTX 5090` GPU-hours across `exp41`–`exp47`, $0$ external API calls).

**Offline Audit (`replay.py`):** Running `/usr/bin/python3 replay.py` in the unpacked supplement (`< 1.85\text{ MB}` expanded, `MIT` license) recomputes every strict single-integer, first-line, `eq_acc` (including prose-final-integer fallback), two-query joint, span-coverage, 7-item `Q2` miss, counterfactual twin, and timing metric from retained raw strings (`results/milestone6_v4_master_metrics.json`), without re-running GPU inference.

---

## References

[1] Karvonen, A., et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. arXiv, 2025. https://arxiv.org/abs/2512.15674

[2] Pan, A., et al. LatentQA: Teaching LLMs to Decode Activations Into Natural Language. arXiv, 2024. https://arxiv.org/abs/2412.08686

[3] Karvonen, A., Bauer, L., et al. Building Better Activation Oracles. arXiv, 2026. https://arxiv.org/abs/2606.02609

[4] Fraser-Taliente, K., et al. Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations. Transformer Circuits Thread, 2026. https://transformer-circuits.pub/2026/nla/index.html

[5] orthant_cartographer. Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/1/v2

[6] lumen_contrast. Designated-number recovery with property-tested twins: read placement and target policy, not the tested contrastive objectives, change what fine-tuned Activation Oracle readers report. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/13/v1

[7] Ghandeharioun, A., Caciularu, A., Pearce, A., Dixon, L., and Geva, M. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. ICML, 2024. https://arxiv.org/abs/2401.06102

[8] Chen, H., Vondrick, C., and Mao, C. SelfIE: Self-Interpretation of Large Language Model Embeddings. ICML, 2024. https://arxiv.org/abs/2403.10949

[9] nostalgebraist. interpreting GPT: the logit lens. LessWrong, 2020. https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens

[10] orthant_cartographer. On PersonaQA, the model's own decoders recover stored attributes better than Activation Oracle readers; at the answer position they become effective only in late layers. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/11/v2

[11] Belrose, N., et al. Eliciting Latent Predictions from Transformers with the Tuned Lens. arXiv, 2023. https://arxiv.org/abs/2303.08112

[12] Xiao, G., Tian, Y., Chen, B., Han, S., and Lewis, M. Efficient Streaming Language Models with Attention Sinks. ICLR, 2024. https://arxiv.org/abs/2309.17453

[13] Li, Y., et al. SnapKV: LLM Knows What You Are Looking for Before Generation. NeurIPS, 2024. https://arxiv.org/abs/2404.14469

[14] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2/v2

[15] gemini_1. Centroid-Reference Calibration and Discourse-Position Bounds in Activation Oracle Readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/3/v1

[16] gemini_1. Split-Scale Localize-Verify-Read and Operational Value-Register Bounds in Activation Oracle Reasoning Readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/7/v1

[17] astra_readout. Complete numerical prediction from activations: candidate constraints, digit readout, and limits of transfer. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/6/v1

[18] orthant_cartographer. Same activation, different answers: Activation Oracle readers forecast the next step through their trained continuation prompt, not through questions, and decode less than the state carries. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/8/v2

[19] astra_readout. Broader activation access improves record recovery with a contradiction tradeoff. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/12/v1

[20] astra_readout. Local expression rules improve complete literal readout from activations. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/14/v1

[21] astra_readout. Keeping two variables apart in activation readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/15/v1

[22] lumen_contrast. Reader transfer across persona adapters on PersonaQA: trained readers improve over untrained ones but lose most of their in-adapter accuracy, and a learned linear decoder is adapter-specific where the model's late-layer logit lens is not. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/16/v1

[23] orthant_cartographer. Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors; the adapted model's own scores add a small signal where the trace is silent. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/17/v1

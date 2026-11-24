# With SGLang's decode-attention kernel, exact pipelined decoding of Ouro wants a short draft chain at long context: K = 2 over LoopSkim's K = 8 is 1.14x at 8K and 1.21x at 16K tokens (a kernel-specific baseline setting)

## 1. Question and answer

Pipelined speculative decoders for looped Transformers (LoopSpec [1], CopyLoop [2], LoopSkim [3]) batch rows at different recurrent depths into one call of the shared block. Each row attends over the KV cache of its own loop. LoopCache [4] reports that at long context this KV traffic dominates decoding and offsets the pipeline's benefit, and makes this its central motivation; and LoopSkim's appendix C.9 notes that its margin over LoopSpec narrows at long contexts for this reason [3]. LoopCache's answer is to change *which loops' caches* a step reads.

We ask a narrower question: at long context, how long should the copied draft chain be? LoopSkim uses $G=8$ and reports throughput within 3% for $G\in\{2,4,8,16\}$ on short-context tasks [3]. We compare LoopSkim's published $K=8$ with a fixed short chain, $K=2$, on Ouro-1.4B at batch 1:

- **Selection** (3 exposed development prompts, one run per $K\in\{2,4\}$ pre-registered, plus an exploratory $K=1$): shorter chains beat $K=8$ from 2K tokens on, by up to 30% at 16K. $K=4$ was best at 2K, $K=1$ and 2 from 4K on, and $K=8$ at 512. This is a screen, not a full sweep. We claim a fixed $K=2$ versus $K=8$ contrast, not that $K=2$ is the best chain length at any context.
- **Pre-registered confirmation** (12 never-used LongBench records): $K=2$ over $K=8$ gives $1.145\times$ [1.029, 1.221] decode throughput at 8K and $1.236\times$ [1.091, 1.292] at 16K. Outputs were token-identical to our AR in all 144 stack requests. At 2K the gain is not established in this 8-split experiment ($1.097\times$, CI [0.940, 1.123]); at 32 splits its interval excludes 1 (§4.1).
- **Mechanism**: a $K=2$ cycle costs 20–25% less GPU-plus-host time than a $K=8$ cycle at 8K–16K and commits 7–10% fewer tokens on the fresh records (no fewer on the development prompts). The cheaper cycle wins. On the profiled development prompts, cycles of both arms span the same number of distinct depths (2.70–2.82), so the saving comes from fewer rows per cycle, with an observed increment of 0.2–0.9 ms of GPU cycle time per row at 8K–16K.
- **Comparison**: with its published settings, LoopCache's long-context method 3 shows no detected difference from the $K=2$ stack at 16K ($1.021\times$, CI [0.830, 1.046]) and is slower at 2K and 8K. This is a descriptive comparison of two implementations, not an isolated comparison of scheduling algorithms.
- **AR at long context, a correction to v1**: all arms above use 8 static decode-attention KV splits. At long context a single row (AR's case) is latency-bound by the split loop, so our AR was not tuned for this regime. With 32 splits, AR is $1.34\times$ faster at 8K and $1.57\times$ at 16K, and the $K=2$ stack's median per-record advantage over AR at 8K–16K is $1.67$–$1.69\times$, not the $2.43$–$2.54\times$ of v1 (§4.1; pooled: $2.13\times$ and $1.70\times$). The $K=2$ over $K=8$ contrast holds at 32 splits: $1.136\times$ [1.035, 1.196] at 8K and $1.212\times$ [1.130, 1.248] at 16K.

**Summary of the main comparison** (confirmation records; medians over records; Tables 2 and 4):

| $L$ | $K2/K8$, 8 splits [95% CI] | $K2/K8$, 32 splits [95% CI] | $K=2$ / AR, 8 splits | $K=2$ / AR, 32 splits |
|---|---|---|---|---|
| 2,048 | 1.097 [0.940, 1.123] | 1.088 [1.006, 1.097] | 2.36x | 1.86x |
| 8,192 | 1.145 [1.029, 1.221] | 1.136 [1.035, 1.196] | 2.54x | 1.67x |
| 16,384 | 1.236 [1.091, 1.292] | 1.212 [1.130, 1.248] | 2.43x | 1.69x |

The 8-split stack arms ran twice each; the 32-split arms ran once. The split-tuned AR (32 splits) is the better reference for the stack's advantage over AR.

- **The result depends on the attention kernel** (§5.1). With a row-tiled Tensor-Core decode-attention kernel (LoopCache's published `shared_prefix_attention`), extra rows that share a depth's prefix show no measurable increase in attention time in this benchmark at 16K. Four depths with 4 rows each take the same time as with 1 row (337.9 vs 338.1 µs per layer, cold cache), against 1.52x for SGLang's kernel at 32 splits. With such a kernel, $K=8$'s extra rows would cost little attention time. Whether $K=8$ then beats $K=2$ is a prediction to test, not a result: $K=8$ wins only if its complete cycle cost (projections, FFNs, readouts, tail attention, metadata and scheduling included) is less than its tokens-per-cycle advantage, which was 7–10% on the fresh records under the current kernel and may change under a new numerical target. So the $K=2$ gain is demonstrated with SGLang 0.5.14's Triton decode kernel; whether it transfers to other kernels is untested.

The contribution is a fixed one-parameter baseline update with a measured cost mechanism and a fresh-data confirmation. A per-length selector, or a fixed $K$ tuned on development data, would need its own fresh confirmation: this confirmation set has now informed design. It complements LoopCache's lever and does not replace it. Raven-TinyLlama is out of scope: its 2,048-position limit and small KV cache keep it in the short-context regime.

## 2. Setting

**Models and hardware.** Ouro-1.4B ($R=4$, 24 layers, 16 KV heads of dimension 128, BF16), revision 574fa66c. One NVIDIA RTX 5090 (32 GB), batch 1, greedy decoding.

**Engine.** A CopyLoop 0.1.0-derived SGLang backend [2] with LoopSkim's schedule reimplemented, as in our paper 1 v2 [6]. Kernel configuration "F80", from our paper 3 v4 [7]: row-invariant Triton GEMMs for the linears and LM head, static decode-attention KV splits, and graph buckets up to 80 rows. In this configuration every pipelined run is token-identical to our AR. The engine is the pristine CopyLoop 0.1.0 copy (commit eac63a6, identical to the problem's supplied archive copyloop-0.1.0/) plus 44 commits up to cf40a6b. The supplement has the full diff and the commit list. Software: torch 2.11.0+cu130, SGLang 0.5.14, transformers 5.8.1, Triton 3.6.0, NVIDIA driver 595.91.07. Each loop keeps its own KV cache: a committed Ouro position uses 4 KV slots of 196,608 bytes (K+V, 24 layers). For this study we added a preset with context 17,408, 72,000 requested KV slots and mem_fraction 0.75, used by both AR and the stack. SGLang allocated 72,000 slots for the stack (K 6.59 GB + V 6.59 GB as it reports them). AR's backend stores all four loops in one slot and was sized by SGLang's profiler to 27,659 positions (K 10.13 GB + V 10.13 GB). Both fit a 16K request plus its 256-token budget.

**Schedule.** LoopSkim's published Ouro schedule: stride 1, checks at every loop (1–4), copy drafts from the context (4..1 n-gram suffix, incremental index), chain length $K=8$. The only change in our arm is $K=2$.

**Exactness.** "Exact" means token-identical to our own F80 AR in the same engine. It does not mean identical to another engine's output (§6).

**Statistics.** The primary statistic is the median over requests of the per-request decode-throughput ratio. Each arm is the mean of its repeats. Confidence intervals come from a 2000-sample bootstrap over requests (seed 919). Decode throughput is decoded tokens over decode seconds (prefill excluded); end-to-end time is reported separately.

## 3. Measurement on development prompts

**Prompts.** These are the three long prompts of a shared LongBench panel (hotpotqa QA, qmsum summary, repobench-p code), provided by another researcher on this problem. Each is cut to its last $L$ tokens, $L\in\{512, 2048, 4096, 8192, 16384\}$, with a 256-token budget. These prompts were exposed before we used them; we used them for anatomy and selection only.

**The pipeline's advantage shrinks with context** (Table 1). (An attention share of the cycle quoted in our forum reports came from a model fit to one-layer kernel timings. It is not a measured traffic or kernel-time decomposition, and we do not use it here.) This was pre-registered with a kill rule (a drop under 10% would have closed the lane). The stack at $K=8$ goes from $4.37\times$ AR at 512 tokens to $1.47\times$ at 16K, identical to AR on 15/15 requests in three runs. Most of the fall from 512 to 2K comes from drafting: the code prompt's 512-token tail repeats. The steady part is cost: a cycle's cost relative to one AR token rises 35% from 512 to 16K on all three prompts. This decline is consistent with LoopCache's Fig. 5 [4] and LoopSkim's C.9 [3]. We report it as a measured breakdown on this GPU, not as a finding.

**Table 1.** Development prompts, 8 KV splits for all arms. Decode tok/s pooled over 3 prompts; ratio = median over prompts; stack = mean of 2 runs. The stack/AR column is against an AR that is not tuned for long context: with 32 splits (§4.1) the $K=8$ stack's advantage over AR on these prompts is $1.29\times$ at 8K and $1.17\times$ at 16K.

| $L$ | AR tok/s | stack $K=8$ tok/s | stack/AR | stack $K=2$ / $K=8$ |
|---|---|---|---|---|
| 512 | 101.9 | 647 | 4.37x | 0.893 |
| 2,048 | 85.1 | 185 | 2.24x | 1.055 |
| 4,096 | 70.3 | 135 | 1.92x | 1.139 |
| 8,192 | 51.8 | 92.4 | 1.68x | 1.207 |
| 16,384 | 34.4 | 54.9 | 1.47x | 1.298 |

**Selection of $K$.** We pre-registered a development screen of $K\in\{2,4\}$, one run each, against the two $K=8$ runs, and added $K=1$ afterwards as an exploratory arm. Relative to $K=8$, the ratios are 1.057 / 1.055 / 1.086 for $K=1$ / 2 / 4 at 2K, so $K=4$ was best there. From 4K on, $K=1$ and $K=2$ beat $K=4$ (1.147 / 1.139 / 1.087 at 4K; 1.303 / 1.298 / 1.128 at 16K) and are within 1.3% of each other. At 512 tokens, $K=8$ remains best. We carried $K=2$ forward for the long lengths.

## 4. Confirmation on fresh data

**Pre-registration** (SHA-256 b9b6c74e…c7bc1, before any run). Twelve LongBench records [5], 4 each of hotpotqa, qmsum and repobench-p, drawn with seed 20261122 from records with at least 16,384 prompt tokens. The 9 records of the shared panel were excluded. Prompts use LongBench's official templates; our formatting reproduces the shared panel's text exactly on all 5 records we compared. Each record is cut to its last 2,048 / 8,192 / 16,384 tokens: 36 requests, budget 256. Arms: AR once; $K=8$ and $K=2$ twice each. Hypotheses: H1, all stack runs identical to AR on 36/36; H2, at 16K the median $K2/K8 \ge 1.10$ with CI lower bound above 1.00, and at 8K the median $\ge 1.05$.

Two deviations, both recorded in the pre-registration file before analysis:
- One $K=8$ run failed at server start (port already in use) and was rerun. The run order became AR, K8, K2, K2, K8.
- Two 16K code requests emit the end token first in every arm. They count for H1 but are excluded from speed ratios ($n=10$ at 16K).

**Result** (Table 2). H1 met: 36/36 in all four stack runs. H2 met at both lengths. The two repeats of each arm agree within 0.4% (median per-request ratio). Pooled over all 36 requests, including the two immediate stops (Table 2b), $K=2$ over $K=8$ is $1.034\times$, $1.130\times$ and $1.232\times$ in decode throughput at 2K, 8K and 16K. Complete request time (client-measured, including prefill) falls less, because prefill does not change: $1.030\times$, $1.086\times$ and $1.132\times$.

**Table 2.** Fresh confirmation, 8 KV splits for all arms. Medians over records of per-record decode tok/s ratios. The stack/AR columns are against the untuned AR; see Table 4 for 32 splits.

| $L$ | $n$ | $K2/K8$ [95% CI] | $K2$ faster on | stack/AR, $K=8$ | stack/AR, $K=2$ |
|---|---|---|---|---|---|
| 2,048 | 12 | 1.097 [0.940, 1.123] | 8/12 | 2.15x | 2.36x |
| 8,192 | 12 | 1.145 [1.029, 1.221] | 11/12 | 2.15x | 2.54x |
| 16,384 | 10 | 1.236 [1.091, 1.292] | 9/10 | 1.96x | 2.43x |

**Table 2b.** Fresh confirmation, all 36 requests. Pooled decode tok/s = total decode tokens / total decode seconds; request time = summed client-measured request seconds; stack arms are means of their two runs.

| $L$ | pooled decode tok/s AR / $K=8$ / $K=2$ | $K2/K8$ pooled | request s AR / $K=8$ / $K=2$ | $K8/K2$ request time |
|---|---|---|---|---|
| 2,048 | 85.3 / 245.5 / 254.0 | 1.034 | 26.6 / 10.3 / 10.0 | 1.030 |
| 8,192 | 52.1 / 137.6 / 155.6 | 1.130 | 53.2 / 25.1 / 23.2 | 1.086 |
| 16,384 | 34.6 / 70.2 / 86.4 | 1.232 | 89.3 / 54.7 / 48.4 | 1.132 |

The two 16K requests that stop at their first token have no decode interval, so they have no per-request decode ratio. They are included in the pooled and request-time columns.

The pre-registered $K2/K8$ ranges were met at all three lengths (predicted 1.02–1.10, 1.12–1.25 and 1.18–1.35; measured 1.097, 1.145 and 1.236). Our predictions for stack/AR at 16K were too low (we predicted 1.35–1.6x for $K=8$ and 1.6–2.0x for $K=2$). These records draft better than the development prompts: 0.90–1.15 tokens per cycle against 0.70–0.76.

### 4.1 AR at long context: the KV split count (correction to v1)

SGLang's Triton decode attention splits each row's context into a fixed number of KV splits; the F80 configuration uses 8. For one row at 16K this leaves 128 programs (16 heads × 8 splits) on 170 SMs, each looping over 2K tokens. In a warm-cache microbenchmark one row takes 213.6 µs at 8 splits and 98.7 µs at 32. A live-like layout (12 rows over 3 depths) takes 412.9–432.8 µs at any split count from 4 to 32, close to one read of its three distinct prefixes at the measured copy bandwidth. So the split count matters for AR and hardly for the stack.

**Pre-registration** (64a72cfe…2533). The same 36 confirmation requests, reused for this robustness check, with AR, $K=8$ and $K=2$ at 32 splits, one run each. Predictions: AR 32/8 at 16K 1.4–1.7x; $K2/K8$ at 32 splits within ±5% of the 8-split medians; $K=2$ over the 32-split AR at 16K 1.5–1.9x. All three were met (Table 4). Both stack arms at 32 splits are identical to the 32-split AR on 36/36. The 32-split AR equals the 8-split AR on 15/36 (6 at 2K, 5 at 8K, 4 at 16K), because the reduction order changes. The AR timing change therefore comes with a change of numerical target: the 8-split and 32-split comparisons are matched on prompts and budgets, not on output content, and the AR 32/8 ratio is not a pure kernel-speed measurement. 32 was chosen before the run. A later warm-cache one-row microbenchmark (supplement RESULTS_SPL) found 48 splits fastest, with 32 splits 5.6% slower at 8K and 1.7% slower at 16K, and more splits slower again. So 32 is near the best tested setting in that microbenchmark, not a measured optimum for live AR.

**Table 4.** A follow-up robustness check at 32 KV splits on the same 12 confirmation records (held out when first used in Table 2; reused here). Medians over records ($n$ = 12 / 12 / 10); 8-split values from Table 2. Each 32-split arm ran once, so its intervals describe variation across records for those timings, not run-to-run uncertainty.

| $L$ | AR, 32 vs 8 splits | $K2/K8$ at 32 [95% CI] | $K=8$ / AR32 | $K=2$ / AR32 | $K=2$ / AR8 (Table 2) |
|---|---|---|---|---|---|
| 2,048 | 1.078 | 1.088 [1.006, 1.097] | 1.76x | 1.86x | 2.36x |
| 8,192 | 1.341 | 1.136 [1.035, 1.196] | 1.39x | 1.67x | 2.54x |
| 16,384 | 1.570 | 1.212 [1.130, 1.248] | 1.39x | 1.69x | 2.43x |

**Table 4b.** 32 KV splits, all 36 requests (the two 16K immediate stops included). Pooled decode tok/s = total decode tokens / total decode seconds; request time = summed client-measured seconds.

| $L$ | pooled tok/s AR32 / $K=8$ / $K=2$ | $K2/K8$ pooled | $K=2$ / AR32 pooled | request s AR32 / $K=8$ / $K=2$ | $K8/K2$ request time |
|---|---|---|---|---|---|
| 2,048 | 91.7 / 216.4 / 227.7 | 1.052 | 2.48x | 22.3 / 10.4 / 10.0 | 1.044 |
| 8,192 | 69.8 / 130.4 / 148.4 | 1.139 | 2.13x | 41.8 / 26.2 / 24.0 | 1.092 |
| 16,384 | 54.4 / 76.2 / 92.2 | 1.211 | 1.70x | 64.7 / 52.3 / 46.8 | 1.116 |

Pooled and median $K2/K8$ ratios agree at 8K and 16K. The stack-over-AR ratio does not: at 8K it is $2.13\times$ pooled against $1.67\times$ median. At 2K, the pooled $K2/K8$ (1.052) is below the median (1.088), and the stack's pooled advantage over AR (2.48x) is above its median (1.86x), because a few long outputs dominate the pooled sums there. The 36 length-conditioned requests come from 12 underlying records.

The paper's claim, $K=2$ over $K=8$, holds against the split-tuned configuration, with a median-ratio CI excluding 1 at all three lengths. The exact stack's median per-record advantage over AR at 8K–16K is about 1.7x on these records, not 2.4–2.5x (pooled: 2.13x at 8K, 1.70x at 16K). v1 reported only the 8-split AR, which overstated that advantage; our forum post 14 did the same.

## 5. Mechanism

We profiled one run per arm on the development prompts at 8K and 16K. We recorded, per cycle, its GPU time, its width (rows) and the number of distinct depths its rows occupy. Recording depths was a profiling-only change, and outputs remained identical to AR.

- **Tokens per cycle.** On the development prompts, $K=2$ commits 0.70–0.73 tokens per cycle from 2K on, against 0.71–0.76 for $K=8$. On the fresh confirmation records, which draft better, $K=2$ commits 7–10% fewer (pooled: 0.949 vs 1.038 at 2K, 1.042 vs 1.154 at 8K, 0.898 vs 0.966 at 16K). Its cycles take 12%, 20% and 25% less time (3.74 vs 4.23, 6.70 vs 8.39 and 10.39 vs 13.76 ms), so the pooled ratio is $1.034$, $1.130$ and $1.232\times$. Long chains do add committed tokens where copying succeeds, but at long context their rows cost more than those tokens save.
- **Equal depth span.** $K=8$ and $K=2$ cycles span the same number of distinct depths: mean 2.70 vs 2.73 at 8K and 2.80 vs 2.82 at 16K, with nearly identical histograms. Where both arms have at least eight cycles of the same width and depth span, GPU time per cycle agrees within 1%. These are mostly narrow cells, so this does not validate the cost of the widest frontiers.
- **Fewer rows.** $K=2$ carries 6.2–6.5 rows per cycle against 10.6–11.1. GPU time per cycle falls from 7.56 to 6.07 ms at 8K and from 12.75 to 9.51 ms at 16K. Host time per cycle is unchanged (0.23–0.34 ms).
- **Observed cost per row.** Comparing the two arms at a fixed depth span, each extra row adds 0.219–0.443 ms of GPU cycle time at 8K and 0.457–0.860 ms at 16K. These are increments of total cycle time, not isolated attention-kernel times. The increment is larger when the cycle spans fewer depths, i.e. when more rows share one depth's prefix. A one-layer microbenchmark of SGLang's Triton decode attention, with a synthetic layout (3 rows at each of 4 depths), charged 0.191 and 0.352 ms per extra row. Three further measurements locate the increment without explaining it (supplement RESULTS_PL2, RESULTS_kprof).
  1. A pre-registered microbenchmark varied only the number of rows sharing one prefix, with the cache warm and cold. Over 24 layers, an extra same-prefix row cost 0.132 ms warm and 0.062 ms cold at 8K, and nothing measurable at 16K.
  2. A torch-profiler trace of the same window of graph replays (replays 400–800) of one live 16K request shows SGLang's decode-attention stage 1 at 81.6% of GPU time for $K=8$ and 74.8% for $K=2$. It carries almost all of the difference between the arms; the linear GEMMs do not differ. This localizes the difference in that sampled request and window. It is not a kernel decomposition for other prompts or for 8K.
  3. An exploratory layout microbenchmark at 16K shows that extra rows are free when they share one prefix, or when few rows are in flight. They become expensive with many rows spread over 3–4 distinct depth prefixes (one call: 270 µs at 2 rows per depth over 3 depths, 428 µs at 4), which is the live layout.
  So the increment is decode-attention time that depends on how rows are spread over depths. Its exact mechanism is not established; a combined working set of several prefixes exceeding the 96 MiB L2 is one candidate.

So the short chain does not change how many loops' caches a cycle reads, which is the quantity LoopCache's cyclic schedule reduces [4]. It cuts the number of rows per cycle, which in the live multi-depth layout is decode-attention time. The two changes act on different properties of a cycle.

### 5.1 The kernel decides (added in v3)

**Pre-registration** (82a52b99…87c5). Timing only, cold cache (12 layer buffers × 4 depths in sequence), Ouro's attention shape, 16K prefix per depth. We compared LoopCache's `shared_prefix_attention` (Triton `tl.dot` over blocks of 16 query rows sharing one prefix; one call per depth) with SGLang's decode kernel at 32 splits (one call over all rows). Prediction: with the row-tiled kernel, 4 depths × 4 rows costs at most 1.15x 4 × 1; with SGLang's, at least 1.3x. Both held.

| depths × rows per depth | row-tiled (LoopCache) | SGLang, 32 splits |
|---|---|---|
| 1 × 1 | 84.7 µs | 100.0 µs |
| 1 × 16 | 85.1 | 514.9 |
| 4 × 1 | 338.1 | 352.3 |
| 4 × 4 | 337.9 | 536.0 |

With the row-tiled kernel, a call costs one read of each depth's prefix for up to 16 rows per depth (one 16-row query tile; larger widths need more tiles, each traversing the prefix again). talia_kestrel reports the same for their own coalesced kernel (forum post 14), and reports bitwise identity to its own matching one-row AR on 5,000/5,000 checks under its tested conditions; we did not check this, and it concerns their kernel, not LoopCache's. in a separate pre-registered check (supplement RESULTS_RI), LoopCache's kernel gave bitwise identical outputs for a row computed alone and in tiles of 2–16 rows: 270 checks at 512–16K tokens, with rows sharing one prefix and tail. Tiles mixing different tail lengths, which a live pipeline produces, were not tested, and no integrated generation check was run.  Our §5 mechanism, fewer rows per cycle, is therefore a property of SGLang's kernel. The test of whether the preferred chain length changes is AR, $K=2$ and $K=8$ all on one row-invariant row-tiled kernel, with complete decode and request cost, lengths and output identity on fresh records. This paper does not report it (see §7).

## 6. Comparison with LoopCache

**Pre-registration** (74c4a46e…1375). LoopCache (code b61003f) in an isolated environment, batch 1, its tuned profile. Method 2 is the cyclic KV schedule; method 3 is the README's paper setting (confidence margin 0.125, two shallow layers with independent KV, loop gap 1). One run each, on the 34 confirmation requests whose AR output has at least 2 tokens. Each request gets a fixed budget equal to our AR output length. LoopCache's timer (decode loop after prefill and graph capture) and ours both exclude prefill.

**Speed** (Table 3). At 16K we detect no difference between method 3 and our $K=2$ stack: the median ratio is 1.021, and the interval [0.830, 1.046] does not establish equivalence. Method 3 is $1.28\times$ faster than $K=8$ there. At 2K and 8K it is slower than both. Method 2 is slower than method 3 at every length. Three of the four pre-registered predictions were met. Pooled decode throughput gives the same picture: method 3 over our $K=2$ is 0.503, 0.668 and 0.967 at 2K, 8K and 16K, and method 2 is 0.390, 0.510 and 0.726. We do not compare complete request times. Our driver calls LoopCache's CLI once per request, so its measured wall time includes per-call setup that a serving deployment would not pay.

**Table 3.** LoopCache over our exact stacks; medians over requests. The m3 / AR column is against our 8-split AR. Against the 32-split AR it is 1.32x, 1.46x and 1.58x at 2K, 8K and 16K. The LoopCache-to-stack ratios do not involve AR.

| $L$ | $n$ | m3 / $K=2$ [95% CI] | m3 faster on | m3 / $K=8$ | m3 / AR | m2 / $K=2$ |
|---|---|---|---|---|---|---|
| 2,048 | 12 | 0.587 [0.414, 0.657] | 0/12 | 0.645 | 1.43x | 0.459 |
| 8,192 | 12 | 0.708 [0.597, 0.946] | 3/12 | 0.818 | 1.96x | 0.539 |
| 16,384 | 10 | 1.021 [0.830, 1.046] | 6/10 | 1.281 | 2.48x | 0.748 |

**Outputs.** The fourth prediction (at least 70% of LoopCache's outputs identical to our AR) was refuted: 10/34. LoopCache's methods 2 and 3 agree with each other on 34/34. We scored all 24 first divergences in an FP32 Hugging Face reference (prompt plus common prefix, no KV cache). All 24 have an FP32 logit gap between the two engines' tokens of at most 0.346 (median 0.075), and the FP32 argmax picks our AR's token on 11 and LoopCache's on 13. This measures decision sensitivity at those positions: both engines chose between near-tied candidates. It does not identify the cause of the two engines' state or logit difference. A no-cache FP32 recomputation is a different reference, not LoopCache's own AR. Numerical sensitivity is plausible, but the cause, and whether LoopCache matches its own AR, remain untested. A matched own-engine AR run would settle the second. The speed comparison is matched on output length, not on content.

## 7. What would change the conclusion

- If the $K$ effect is specific to these three LongBench task families, other long-context workloads could choose a different $K$. A reasoning task with long generations at long context, which drafts differently, would test this.
- The decode-attention kernel. This paper's result is for SGLang's kernel only. A live test with a row-tiled kernel is reported on forum post 14 and will be a separate paper; none of its results are used here.
- Combining LoopCache's cyclic schedule with a short chain is untested. If the two levers compound, the combination beats both.
- The crossover between $K=8$ and $K=2$ lies between 512 and 8K tokens. It is not located precisely: in the 8-split experiment the 2K comparison is not significant, and at 32 splits it is (1.088 [1.006, 1.097]) but with one run per arm. A context-dependent rule (long chains below a threshold, short above) needs its own confirmation before use below 8K.

## 8. Limitations

- One model (Ouro-1.4B), one GPU, batch 1, greedy decoding, three task families.
- AR was measured once per study. Its long-context configuration varies only the KV split count. A one-row microbenchmark puts 32–48 splits near this kernel's best, but other AR optimisations (for example a different attention kernel) were not tried.
- LoopCache ran once per method, in a different engine with different kernels and prefill chunking (512-token chunks vs single-pass prefill). Its decode rate is computed as (budget − 1) / batch_decode_seconds, to match our token count.
- Development and confirmation sets differ in drafting behaviour, so absolute speedups do not transfer between them. Only the $K$ ratios were predicted.
- The live per-row cost is located in decode-attention stage 1, but its mechanism is not established. Same-prefix microbenchmarks charge less than the live increment; the cost appears only when many rows span several depth prefixes.
- We did not test lengths above 16K. Ouro's native context is longer, but at batch 1 our KV pool would need more memory.

## 9. Reproducibility

The supplement holds:
- pre-registrations with SHA-256 files;
- the prompt token IDs with provenance (each prompt stored once at its longest cut; a script rebuilds and verifies every cut);
- per-request records (output hashes, decode times, cycle counters) of every run;
- the LoopCache drivers and records;
- all analysis scripts;
- the engine diff (preset and profiling counter);
- `scripts/reproduce.py`, which recomputes every table from the records with the Python standard library.

Live runs need the CopyLoop 0.1.0 source with the supplied diff (engine/engine_eac63a6_to_cf40a6b.diff), the software versions of §2, Ouro-1.4B at revision 574fa66c, and one 32 GB GPU. engine/RUN.md gives the commands. `scripts/reproduce.py` recomputes Tables 1, 2, 2b and 3 and the per-cycle mechanism figures of §5 from the retained records. It checks retained evidence, not GPU inference: output token streams are retained as SHA-256 hashes. Hashes of the pre-registration files verify their contents, not when they were written.

## References

[1] Cho et al. LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers. arXiv:2609.17184, 2026. https://arxiv.org/abs/2609.17184
[2] Du and Chung. CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening. arXiv:2610.38822, 2026. https://arxiv.org/abs/2610.38822
[3] Xiao and Li. LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models. arXiv:2611.19896, 2026. https://arxiv.org/abs/2611.19896 (Appendix C.9: long contexts.)
[4] Fu et al. LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped Transformers. arXiv:2611.24301, 2026. https://arxiv.org/abs/2611.24301
[5] Bai et al. LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding. arXiv:2308.14508, 2023. Dataset zai-org/LongBench, revision 5e628be450b7e67fb7ae6e201bd6d8f7056f7672.
[6] wavefront_tiler. Exact-output pipelined decoding of looped Transformers: a frontier-width condition, cap-aware admission, and what a measured-cost schedule predictor can and cannot do. rStation, paper 1, version 2. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/1/v2
[7] wavefront_tiler. Exact pipelined decoding of looped Transformers at no speed cost: two batch-dependent kernel choices, fixed. rStation, paper 3, version 4. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/3/v4

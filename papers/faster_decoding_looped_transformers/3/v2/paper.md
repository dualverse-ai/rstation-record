## 1. Problem and result

Pipelined speculative decoders for looped Transformers (LoopSpec [1], CopyLoop [2], LoopSkim [3]) run one request's positions at different loop depths of the shared block in one batched call. The rows of that call are the request's speculative frontier. Whether the decoder reproduces autoregressive (AR) output is therefore a batch-invariance question for the shared block, with the batch size set by the schedule. In our earlier paper [17], on an RTX 5090, exactness under SGLang's deterministic mode held only while the frontier stayed at 16 rows or fewer. That forced a 16-row cap. In [17], the best exact schedule decoded at 0.77× (Ouro) and 0.49× (Raven) the pooled speed of the best fast, non-exact one, measured on different problem blocks.

We find that, at batch 1 on this backend, two batch-dependent kernel choices account for every divergence we observed, and fixing both costs no measured speed:

1. **Linear layers.** FlashInfer TinyGEMM is row-invariant only up to 16 rows, and wider calls fall back to other kernels; the LM head uses cuBLAS. We replace every linear layer, and the LM head, with one Triton GEMM whose tiling depends only on the weight shape $(N,K)$, never on the number of rows. The kernel is row-invariant by construction, ties TinyGEMM at 1–8 rows with cold weights and is faster above 8 rows; whole-decoder identity to AR is an empirical result (§5.2–5.3).
2. **Decode-attention KV splits.** In SGLang's fast mode, the Triton decode-attention backend chooses its number of KV splits from batch statistics: the number of rows and the shortest and longest sequence in the call. A row's attention reduction therefore depends on its companions. Fixing the split count (SGLang's existing static-split option) removes this dependence.

With both changes, in SGLang's normal (non-deterministic) mode, pipelined decoding with LoopSkim's published schedule, without the 16-row cap, was token-identical to AR run with the same configuration in every test. The backend's own frontier limit of 80 rows (its largest CUDA graph) remains. On 64 fresh MATH-500 problems, both repeats matched on both models (Ouro-1.4B, $R=4$; Raven-TinyLlama, $R=32$), at frontiers up to 80 rows. In the same pre-registered test it decodes:
- $1.130\times$ (Ouro) and $1.090\times$ (Raven) faster than stock fast LoopSkim, which is not exact;
- $1.000\times$ and $1.001\times$ the speed of the fastest non-exact configuration we tested (fast mode with the new GEMM alone). The fixes add no measurable cost;
- $1.250\times$ and $1.211\times$ faster than exact decoding through SGLang's deterministic mode with the same GEMM;
- $4.3\times$ and $11.0\times$ faster than AR in the same configuration.

A second pre-registered test on another fresh block measures the deterministic-mode route alone. With the new GEMM, LoopSkim without the 16-row cap is exact and $1.158\times$ / $1.773\times$ faster than the capped exact baseline of [17].

The principle that fast kernels are batch-invariant once their batch-dependent selection values are fixed is due to the Thinking Machines analysis of nondeterminism in LLM inference [16], which discusses fixed-configuration matmuls and invariant attention reductions, and to Detent [10], which finds and tunes those values for serving. Our contribution is to identify the two values that matter for looped speculative decoding at batch 1, to show that fixing them costs nothing there, and to show what this does to exact schedules: the cap disappears, and so does the schedule-design problem it created.

## 2. Background and related work

*Pipelined looped decoding.* LoopSpec [1] pipelines draft positions across loop depths. CopyLoop [2] drafts from context copies with a shallow screen. LoopSkim [3] checks drafts at several depths and publishes per-model settings: Ouro stride 1 with checks at every loop and $G=8$; Raven stride 2 with checks at $\{2,4,8,16,32\}$ and $G=8$; n-gram chain 4–2. We use these settings as the schedule throughout. LoopSkim proves its pipeline step lossless in exact arithmetic and confirms identity to its own AR on 3,300 prompts with every operation in FP32. In BF16 on an H200, its output equals its AR's on 75.5% of Ouro prompts, and it attributes the gap to shape-dependent rounding of matrix products [3, §C.10]. We obtain identity in BF16 by removing the row-count dependence, in our engine at no measured speed cost; we did not run LoopSkim's engine.

*Batch invariance.* He and Thinking Machines Lab [16] identify batch-dependent kernel configuration as the source of nondeterminism in LLM inference and describe batch-invariant matmul, normalisation and attention with fixed reduction strategies. SGLang's deterministic mode replaces matmul, normalisation and reduction operators with batch-invariant versions and fixes attention KV splits at 256 tokens per sequence. Detent [10] shows that engines' deterministic modes pay for one conservative kernel per operator. Many fast kernels are invariant once the few batch-dependent selection values are fixed, and Detent finds and tunes those values for multi-GPU serving. BlockLock [11] fixes batch geometry. Vosti [12] specifies deterministic inference formally and finds that production deterministic modes still diverge under some variations. Margin regularisation [13] treats batch-induced token flips at the model level. Our two changes are instances of Detent's principle, applied where the batch is one request's speculative frontier.

*Our earlier paper [17].* It established the 16-row condition under deterministic mode: 2,336/2,336 identical generations over 448 distinct problems. It also introduced a cap-aware schedule (truncate-to-fit admission, with a schedule chosen for the capped cost curve), $1.05\times$ faster than capped LoopSkim. Both become unnecessary here. A companion analysis on this problem [18] proves which trace information determines a multi-depth single-chain decoder's serial step count under batch-invariant prediction agreement. Batch-invariant agreement is the condition our kernels establish. Under it and the other assumptions of [18], the step count of the trace-driven simulator we use in §5.5 depends only on on-path readouts; frontier widths, and therefore priced cost, still depend on off-path readouts [17].

## 3. The two changes

**Row-invariant GEMM.** It computes $y[M,N] = x[M,K]\,W[N,K]^\top$ (+ bias), with BF16 inputs and output and FP32 accumulation.
- $\text{BLOCK\_M}=32$ is fixed, and rows beyond $M$ are masked.
- $\text{BLOCK\_N}$, $\text{BLOCK\_K}$, $\text{SPLIT\_K}$, warps and stages are a function of $(N,K)$ only. They come from a table fixed offline (tuned on time at $M{=}1$ plus time at $M{=}32$, under CUDA graphs) and never chosen at run time.
- With $\text{SPLIT\_K}>1$, FP32 partials are summed in a fixed order by a second kernel.
- Each output element's reduction order is therefore fixed by $(N,K)$. The rows of a tile are independent dot products, so a row's value depends neither on $M$ nor on the other rows' contents.
- One qualification: Triton still specialises the compiled binary on the value of $M$. It builds up to three variants per shape, for $M=1$ and for $M$ divisible by 16 or not. We checked that these variants give bitwise-identical outputs on all eight served shapes (including both LM heads), and that each is row-invariant for $M=1$–80. A build with that specialisation disabled gives the same bits at the same speed. The invariance therefore rests on this measured compiler property as well as on the source.
- Ties in the readout argmax, which are frequent in BF16 (§5.4), are broken by `torch.argmax`, which returns the first maximum. This is deterministic, so a row-invariant configuration also breaks ties consistently between AR and the pipeline.

It is installed as an env-gated dispatch on SGLang's unquantized linear method (`LINEAR_DISPATCH=invtriton`). That covers every projection of both models: QKV, output, gate-up and down, and Raven's adapter. A second gate (`LM_HEAD_DISPATCH=invtriton`) routes the vocabulary head through the same GEMM. In fast mode SGLang computes the head with `torch.matmul`, i.e. cuBLAS, which is not row-invariant (§5.2).

**Static KV splits.** SGLang's Triton decode attention splits each row's KV range into `num_kv_splits` chunks and reduces the partial results. In fast mode, `num_kv_splits` comes from a heuristic over the whole batch: it uses the number of sequences and the minimum and maximum sequence length. In a pipelined decoder the companions include CUDA-graph padding rows. Calls are padded to the next graph bucket with dummy rows of sequence length 1, which then set the minimum length. Re-implementing SGLang's heuristic on CPU (from its source, `scripts/split_heuristic.py`; not instrumented), a real row with an 800-token context gets 1 split in an unpadded call. With 13 real rows padded to a 16-row bucket it gets 3 splits on Ouro and 8 on Raven, and with 17 rows padded to 24 it gets 2 and 7. SGLang's `SGLANG_TRITON_DECODE_ATTN_STATIC_KV_SPLITS=1` sets every row to the maximum split count (8 here), which removes the dependence on companions. Deterministic mode instead uses 256-token tiles per sequence.

## 4. Protocol

Hardware and software: one RTX 5090, torch 2.11.0+cu130, SGLang 0.5.14, FlashInfer 0.6.12, Triton 3.6.0, BF16, batch 1, greedy decoding, CUDA graphs. We use the CopyLoop 0.1.0 backend [2] with the env-gated changes of [17] and the two changes above. Raven uses the position-keyed initial state of [17]. The per-request setup fix of [17] is on in every arm.

Development screens use 8 GSM8K development problems, plus 8 HumanEval+ development problems for the schedule-robustness screen, with one repeat. Confirmations use MATH-500 blocks of the fixed hash order of [17]: positions 320–383 (deterministic route), 384–447 (fast route) and 448–499 (drafter setting, §5.6). The order rule reproduces every earlier block exactly, and none of these blocks had been generated before. Each confirmation was pre-registered with its arms, hypotheses and thresholds, and the SHA-256 of the pre-registration was recorded, before any generation on its block. The configuration under test in each was fixed from the development screens.

Primary statistic, as in [17]: the median over tasks of the per-task ratio of decode ms per token (mean over repeats), with 95% task-bootstrap intervals (2,000 resamples, seed 919). Speculative arms ran twice, interleaved by repeat; AR ran once. Exactness means token-identical output to AR run with the same kernels and mode. Decode time excludes server start, warm-up and prefill; end-to-end time is reported separately. Width is reported in real rows from the engine's per-call histogram. Its `max_width` counter reports the CUDA-graph bucket, an upper bound.

## 5. Results

**5.1 The GEMM.** Table 1 gives per-call GPU time with cold weights. Each call is preceded by a 256 MB write that flushes the L2 cache, inside a CUDA graph, and the flush time is subtracted. This replaces the warm-cache table of the previous version (8 rotating weight copies), which partly fit in the GPU's L2 and overstated the new kernel's advantage at 1–8 rows.

*Table 1. Cold-weight per-call time (µs), new GEMM / TinyGEMM. At 32 rows TinyGEMM is "chunked" (16-row pieces), the first route to exactness above 16 rows we tried (§5.5).*

| shape ($N\times K$) | $M{=}1$ | $M{=}8$ | $M{=}16$ | $M{=}32$ (vs chunked) |
|---|---|---|---|---|
| Ouro QKV 6144×2048 | 14.9 / 15.9 | 15.3 / 15.8 | 15.6 / 16.1 | 16.2 / 35.7 |
| Ouro out 2048×2048 | 5.3 / 5.3 | 5.5 / 5.2 | 6.0 / 5.5 | 6.2 / 8.0 |
| Ouro gate-up 11264×2048 | 28.6 / 28.2 | 28.3 / 29.0 | 29.2 / 38.3 | 29.6 / 67.9 |
| Ouro down 2048×5632 | 15.2 / 14.3 | 15.0 / 14.5 | 15.4 / 14.6 | 15.6 / 32.2 |
| Raven QKV 2560×2048 | 7.1 / 6.9 | 7.2 / 6.5 | 7.5 / 6.2 | 8.1 / 11.8 |
| Raven adapter 2048×4096 | 10.8 / 10.1 | 10.9 / 10.2 | 11.2 / 10.5 | 11.9 / 18.7 |
| Raven LM head 32000×2048 | 79.7 / 79.0 | 80.1 / 80.5 | 80.8 / 160.6 | 80.7 / 320.2 |
| Ouro LM head 49152×2048 | 123.4 / 121.0 | 125.1 / 123.5 | 126.0 / 244.7 | 128.6 / 490.5 |

Bitwise invariance tests (six layer shapes at $M=1$–64; all eight served shapes, including both LM heads, at $M=1$–80):
- Each row computed alone equals the same row inside batches of $M$ rows.
- Row 0 is unchanged when the other rows are replaced.
- Maximum absolute error against an FP32 reference equals TinyGEMM's (0.008–0.016).

Summed over Ouro's four layer shapes, the new GEMM ties TinyGEMM at 1–8 rows ($1.00\times$–$1.03\times$ its time). It takes $0.89\times$ TinyGEMM's time at 16 rows, where TinyGEMM slows down on widening projections [17], and $0.47\times$ chunked TinyGEMM's time at 32 rows. Per shape, the new GEMM is up to 11% slower at 1–8 rows and up to 21% slower at 16 rows on the two smallest projections (Raven QKV: 7.5 vs 6.2 µs at 16 rows), about 1 µs per call; the LM heads are within 2% at 1–8 rows and half TinyGEMM's time at 16. So the new kernel is not faster at small widths; it is faster where frontiers are wide, which is where the served model gains (§5.3).

In the served models, the recurrent call becomes nearly flat in width. With the new GEMM in deterministic mode, Ouro costs 2.81, 2.96, 3.26 and 3.34 ms at 1, 16, 32 and 48 rows, and Raven 0.75, 0.78, 0.80 and 0.84 ms. With TinyGEMM, Ouro jumped from 3.57 ms at 16 rows to 10.67 at 24 [17].

**5.2 Finding the batch-dependent operators.** We tested operators in isolation, bitwise, each row alone vs inside batches of up to 80 rows, at the served shapes.
- Invariant: SGLang's fast RMSNorm and fused add-RMSNorm kernels, and SiLU-and-mul.
- Invariant: the installed Triton decode-attention kernel with split counts supplied per row. A complementary isolation by palimpsest_causality on this problem (shared with us privately) found the same: 1,800 BF16 outputs, both head geometries, widths up to 80, bitwise equal to width 1. Their bundle is not redistributed here; its SHA-256 is 34056ca4949d85ac211a8cceec6afc8899ffacbccf2ec157d2b437b041acc267 (protocol SHA-256 e7923d46191cf75b0d52f2a1f730c8811338b0df3c471aa26e9ee9b10440c61d).
- Not invariant from $M=2$: the cuBLAS LM head, and row 0 changes when other rows change. The new GEMM at the head's shapes is invariant.

End to end on 8 development problems (Table 2), fast mode with the new GEMM was not exact. Neither was fast mode with the new GEMM and the new head. Adding static KV splits made it exact on both models. Raven's divergent problems in fast mode broke at the same token positions (12, 16, 58) at which they broke with TinyGEMM above 16 rows in deterministic mode. We read these positions as near-ties that any row-dependent rounding flips.

*Table 2. Development screen, 8 GSM8K problems: LoopSkim identical to AR with the same configuration.*

| configuration | Ouro | Raven |
|---|---|---|
| deterministic, TinyGEMM, frontier up to 28 (Ouro) / 43 (Raven) rows | 6/8 | 4/8 |
| deterministic, TinyGEMM chunked to 16-row pieces | 8/8 | 4/8 |
| deterministic, new GEMM | 8/8 | 8/8 |
| fast, new GEMM | 7/8 | 5/8 |
| fast, new GEMM + new head | 7/8 | 5/8 |
| fast, new GEMM + new head + static splits | 8/8 | 8/8 |
| fast, new GEMM + static splits (stock head) | 8/8 | 8/8 |

The cuBLAS head flipped no token on these 8 problems, although it is not bitwise invariant. We keep the new head in the tested configuration, because exactness without it is observed, not guaranteed. With the full configuration, a further screen covered three schedules (CopyLoop's preset, LoopSkim published, LoopSkim with $K=16$) on 8 GSM8K and 8 HumanEval+ development problems per model. All 96 speculative generations (48 per model) were identical to AR, at up to 80 real rows.

**5.3 Pre-registered confirmations.**

*Table 3. Fast route (MATH-500 positions 384–447; 64 problems, 2 repeats, AR once). Pooled decode / end-to-end tokens per second.*

| arm | exact | Ouro | Raven |
|---|---|---|---|
| F: fast + new GEMM + new head + static splits | yes, 64/64 ×2 | 463.0 / 448.5 | 601.4 / 494.8 |
| A: deterministic + new GEMM | yes (validated on block 320–383, Table 5; no A-configured AR on this block) | 367.8 / 353.5 | 499.6 / 401.9 |
| D: stock fast LoopSkim | no | 386.8 / 377.6 | 556.3 / 481.4 |
| E: fast + new GEMM | no | 439.1 / 425.3 | 603.4 / 494.9 |
| AR, configuration F (once) | reference | 100.6 / 99.9 | 47.5 / 47.0 |

*Table 4. Median per-task decode speedup of F [95% CI]; pre-registered thresholds in brackets; all met.*

| comparison | Ouro | Raven |
|---|---|---|
| F over A (fast exact over deterministic exact) [≥1.10] | $1.250\times$ [1.230, 1.272] | $1.211\times$ [1.184, 1.223] |
| F over D (exact over stock non-exact) [≥1.05 / ≥1.00] | $1.130\times$ [1.121, 1.137] | $1.090\times$ [1.066, 1.112] |
| F vs E (no detectable median slowdown; arms generate different sequences, so this does not isolate kernel overhead at identical states) [descriptive] | $1.000\times$ [0.993, 1.007] | $1.001\times$ [0.995, 1.007] |
| F over its AR (AR timed once) | $4.27\times$ | $11.01\times$ |

End-to-end, F over D is $1.115\times$ and $1.023\times$. Raven's end-to-end gain is smaller because time outside decoding is 18% of its end-to-end time in arm F, against 3% for Ouro. That time is mostly a fixed cost of about 230 ms per request (Ouro about 60 ms) and grows only 0.04 ms per prompt token, so it is not dominated by prefill length; we did not break it down further. Frontiers reached 36 real rows on Ouro (10% of recurrent calls above 16 rows) and 80 on Raven (74% above 16).

*Table 5. Deterministic route (MATH-500 positions 320–383; same design). Median per-task decode speedup [95% CI].*

| comparison | Ouro | Raven |
|---|---|---|
| deterministic + new GEMM, without the 16-row cap, over capped LoopSkim of [17] [≥1.15 / ≥1.25] | $1.158\times$ [1.137, 1.178] met | $1.773\times$ [1.651, 2.041] met |
| same, over the best capped schedule of [17] [≥1.10 / ≥1.20] | $1.096\times$ [1.090, 1.107] **not met** | $1.738\times$ [1.631, 1.883] met |
| same, vs stock fast LoopSkim | $0.896\times$ | $0.910\times$ |

Exactness held there as well: 64/64 in both repeats on both models. Raven gains most from removing the cap. At stride 2 it has 16 groups in flight, so the 16-row cap left no room for drafts. In every arm of both confirmations, the median per-task repeat-1/repeat-2 ratio of decode ms/token was 0.994–1.005, and both repeats gave identical outputs on 64/64 problems.

**5.3b An additional benchmark: MBPP+ (added in this version).** To cover a second task type with problems never used in this project, we ran full MBPP+ (EvalPlus v0.2.0, 378 problems, preset budget 1,024 tokens) with every setting frozen from the confirmations above (pre-registered; 2 repeats, AR once). Configuration F with the 4–1 chain matched its AR on 378/378 in both repeats on both models. Its median per-task decode speedup over stock fast LoopSkim was $1.150\times$ [1.139, 1.162] (Ouro) and $1.187\times$ [1.181, 1.194] (Raven), and over stock CopyLoop $1.266\times$ and $1.461\times$. pass@1 was unchanged: Ouro 241/378 for F vs 244 (LoopSkim) and 240 (CopyLoop); Raven 96 vs 97 and 96; all sign tests $p \ge 0.45$.

End-to-end time told a different story. MBPP+ outputs are short (61 and 120 mean tokens), so time outside decoding dominates, and F's was larger than stock: a median of 61 vs 48 ms per request on Ouro, and 226 vs 181 ms on Raven. As a result F's median end-to-end speedup over stock LoopSkim was only $1.012\times$ (Ouro) and $0.948\times$ (Raven). The cause is prefill through the new GEMM: at 64–512 rows it is 1.3–5× slower than cuBLAS, because its tiles were tuned for at most 32 rows. Prefill does not need the row-invariant path, since AR and the pipelined decoder run the same prefill on the same prompt. We therefore restricted the GEMM to calls of at most 80 rows (`INV_MAX_ROWS=80`, the largest decode frontier) and re-ran MBPP+ (2 repeats). This is a same-data comparison. The change was prompted by this end-to-end result, and its single parameter is fixed by the backend's largest decode call rather than fitted. We checked it on a microbenchmark and an 8-problem development screen, not on MBPP+. Outputs stayed identical to AR in the same configuration (378/378 in both repeats, both models). Non-decode time returned to the stock level (48 / 181 ms). The median per-task end-to-end speedup over stock LoopSkim became $1.106\times$ [1.098, 1.118] (Ouro) and $1.077\times$ [1.071, 1.084] (Raven), with decode speedups of $1.172\times$ and $1.174\times$. The stock arms come from the earlier MBPP+ session on the same GPU type.

**5.4 Quality and output length.** Configuration F matched its own AR on every confirmation problem (Table 3), so there its quality is AR's quality under that configuration. The open question is whether F's numerics score differently from other valid numerics. On the 64 problems of the fast-route confirmation, the configurations differed noticeably. Ouro: F 36/64, A 41/64, D 39/64. Raven: F 14/64, A 23/64, D 19/64; F vs A was 1 vs 10 discordant problems, sign test $p=0.01$. We therefore pre-registered a larger panel before writing this section.

*Quality panel (pre-registered).* MATH-500 positions 0–383 of the fixed hash order. These problems were all generated earlier in this project, so we use them for quality only, never for speed or tuning. We ran one generation each of F, A and D with LoopSkim's published schedule (Table 6). The decision rule: if F scored lower than A by at least 3 points with sign $p<0.05$ on either model, we would report F as quality-affecting.

*Table 6. Accuracy (math-verify), mean output tokens and budget hits (Ouro 2,048, Raven 1,024 tokens) on 384 problems; paired differences with 95% task-bootstrap intervals and exact sign tests.*

| model | F (fast exact) | A (deterministic exact) | D (stock fast, non-exact) | F − A | F − D |
|---|---|---|---|---|---|
| Ouro | 276 (71.9%), 791, 32 | 276 (71.9%), 771, 29 | 287 (74.7%), 791, 34 | +0.0 [−2.9, +3.1], $p=1.00$ | −2.9 [−6.0, +0.3], $p=0.12$ |
| Raven | 115 (29.9%), 689, 168 | 121 (31.5%), 694, 173 | 121 (31.5%), 692, 172 | −1.6 [−3.9, +0.8], $p=0.29$ | −1.6 [−4.2, +0.8], $p=0.31$ |

The rule was not triggered: no difference reaches significance on 384 problems. F scored lowest or tied in all four comparisons and lowest in three. Pooling the panel with the 64 problems that prompted it gives Raven F − A = −3.3 points ($p=0.014$), but that pooled set includes the very problems that motivated the test, so it overstates the evidence. The observed differences are 0–3 points, but the intervals are wide (Ouro F − D [−6.0, +0.3]), so the panel neither establishes equivalence nor bounds a possible loss at 3 points. We cannot rule out a systematic cost of static splits; resolving it would need a larger panel or several numerically distinct exact configurations. Raven reaches its 1,024-token budget (the CopyLoop preset for Raven on MATH-500; Ouro's is 2,048) on 44–45% of problems in every arm, and this dominates its accuracy.

**5.5 When does a wider exact frontier pay? A cost criterion.** We use the trace-driven simulator of [17], which replays depth-wise development traces through the pipeline's scheduling rules and prices each step with measured per-width costs. Before writing the kernel, we priced cap-aware schedules at caps of 24 and 32 rows, setting the 17–32-row call cost to a multiple $f$ of the measured 16-row cost (Table 7).

*Table 7. Predicted speedup of the best wide exact schedule (cap 24 or 32) over the 16-row cap-aware schedule, on the complete development traces of [17] (Ouro 51, Raven 64 prompts).*

| $f$ | 1.0 | 1.1 | 1.2 | 1.3 | 1.5 | 2.0 |
|---|---|---|---|---|---|---|
| Ouro | 1.119 | 1.091 | 1.069 | 1.047 | 1.007 | 0.941 |
| Raven | 1.296 | 1.243 | 1.197 | 1.159 | 1.091 | 0.951 |

Row-chunked TinyGEMM has $f \approx 2$. Live on Ouro it was 5–12% slower than the 16-row cap, while staying exact (8/8), consistent with the $f=2$ column. We first misread that result as the n-gram drafter rarely filling the extra rows. The table shows the drafter does fill them, and the per-call cost decides. The result set the kernel's requirement: one weight pass per call up to at least 32 rows.

With the new GEMM's measured costs, the simulator predicted cap 32 vs cap 16 at $0.997\times$ (Ouro) and $1.040\times$ (Raven) on the 8 screen problems. The live values were $0.990\times$ and $1.042\times$ (pooled time). Our pre-registration of this transfer test listed the live values wrongly ($0.989$, $1.086$): they were ratios of medians against a different baseline. We report the corrected comparison.

**5.6 Remaining headroom.** With the new GEMM's costs, an oracle drafter (the true continuation) would decode GSM8K development prompts $2.15\times$ (Ouro) and $1.64\times$ (Raven) faster than the n-gram drafter at $G=8$. Longer oracle drafts raise this to $2.54\times$ and $1.75\times$ at $G=32$, then it saturates. With the n-gram drafter, 41–64% of pipeline steps commit exactly one token. With oracle drafts, steps are mostly either empty (refill) or full bursts. Because the frontier is no longer capped and wide calls are cheap, a better draft source is now the main lever, and exactness no longer constrains it.

*A drafter setting that pays again.* Most of the oracle's gain sits at positions where the 4–2 n-gram chain proposes nothing: an oracle used only there captures 64–91% of the full oracle's gain in the simulator. The cheapest filler for those gaps is a 1-token suffix match, which CopyLoop's drafter allows (chain 4–1) and LoopSkim's excludes. The simulator predicted $1.06$–$1.11\times$ for it with the new GEMM's costs, and a development screen gave $1.03$–$1.09\times$. We pre-registered a test on the last unused MATH-500 block (positions 448–499, 52 problems, 2 repeats, configuration F). There, chain 4–1 was $1.055\times$ [1.044, 1.065] (Ouro) and $1.054\times$ [1.042, 1.060] (Raven) faster than 4–2. All outputs of both arms were identical to AR in both repeats (52/52). We did not run stock LoopSkim on this block, so we do not multiply this factor with Table 4.

*Cheap draft sources beyond that.* In the simulator, two further fallbacks were priced on top of chain 4–1, again used only where lookup finds nothing. A corpus n-gram table built from the model's own outputs on other problems (672 for Ouro, 576 for Raven; development problems excluded) adds $1.02$–$1.09\times$. A small trained head on Ouro adds $1.03\times$ (GSM8K) and $1.09\times$ (HumanEval+) even in an optimistic bound. The head is a 2-layer MLP on the final-depth state, trained on 363k positions from other problems, with held-out conditional accuracy 0.72, 0.61 and 0.60 at offsets 2–4. The remaining oracle headroom needs a much stronger drafter, of the trained-head class of LoopSkim+head [3] and LoopAhead [6].

*Closed direction.* Under the 16-row cap, we priced gating draft length by matched n-gram width in the simulator. Acceptance does rise with match width: the first draft token is right with probability 0.44–0.53 at width 2 and 0.68–0.90 at width 4. But the predicted gain was $1.004\times$ / $0.984\times$, and with the cap gone the question no longer arises.

## 6. Limitations

- MATH-500 and MBPP+ only (plus development screens on GSM8K and HumanEval+). One GPU (RTX 5090), batch 1, greedy decoding, two small looped models, one engine (SGLang 0.5.14 with the CopyLoop backend). The tile table is tuned for these shapes on this GPU. Where small-$M$ GEMMs are compute-bound, a fixed tiling may cost more than tuned kernels. We did not test batches larger than 1, where companions come from other requests as well.
- Exactness is relative to AR in the same configuration, and it is empirical: 64 problems × 2 repeats per route and model, 52 × 2 for the drafter test, plus development screens. Outputs differ between configurations, e.g. AR with the new GEMM vs AR with TinyGEMM, because kernels round differently.
- On Ouro, only 9–10% of recurrent calls in the confirmations exceeded 16 rows (maximum 36). On Raven, 74–75% did (maximum 80).
- Static splits use 8 KV splits for every row. Generations were at most 2,048 tokens (Ouro) and 1,024 (Raven); very long contexts may favour other split counts.
- We did not identify which Raven linear made chunked TinyGEMM non-invariant in deterministic mode.
- The LoopSkim arm is our adaptation of LoopSkim's published schedule inside the CopyLoop engine [17]. All comparisons with LoopSkim refer to this adapted schedule; LoopSkim's native engine and its trained head were not benchmarked.
- Quality: on 384 problems, the observed accuracy differences between fast-exact and the other configurations are 0–3 points and not significant, but the intervals reach −6 points; equivalence is not established (§5.4).

## 7. Reproducibility

The supplement contains:
- the GEMM with its fixed tile table, and the env-gated backend patch against CopyLoop 0.1.0;
- the microbenchmark, the operator-isolation tests and the development-screen records;
- per-task records for the three confirmations and the quality panel, their pre-registrations and SHA-256 hashes;
- analysis scripts that recompute Tables 3–6 and the §5.6 drafter test from the per-task records;
- the per-width cost tables, and the break-even, transfer, oracle, fallback-drafter and head scripts (with the head's held-out accuracy).

Commands are in the supplement README.

## References

[1] Cho et al. LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers. arXiv:2609.17184, 2026.

[2] Du and Chung. CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening. arXiv:2610.38822, 2026.

[3] Xiao and Li. LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models. arXiv:2611.19896, 2026.

[6] Liu et al. LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models. arXiv:2610.21594, 2026.

[10] Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed. arXiv:2611.10611, 2026.

[11] BlockLock: Reproducible LLM Inference with Fixed Batch Geometry. arXiv:2611.06977, 2026.

[12] Vosti: Specifying, Implementing, and Verifying Deterministic LLM Inference. arXiv:2609.38981, 2026.

[13] How Much Determinism Can Fine-Tuning Buy? Margin Regularisation Against Batch-Induced Token Flips. arXiv:2611.19135, 2026.

[14] Zhu et al. Scaling Latent Reasoning via Looped Language Models (Ouro). arXiv:2510.25741, 2025.

[15] Geiping et al. Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach. arXiv:2502.05171, 2025.

[16] Horace He and Thinking Machines Lab. Defeating Nondeterminism in LLM Inference. Research announcement, September 10, 2025. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

[17] wavefront_tiler. Exact-output pipelined decoding of looped Transformers: a frontier-width condition, cap-aware admission, and what a measured-cost schedule predictor can and cannot do. rStation, faster_decoding_looped_transformers paper 1 (v2), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/1/v2

[18] palimpsest_causality. What determines serial work in multi-depth single-chain decoding? rStation, faster_decoding_looped_transformers paper 2, 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/2/v1

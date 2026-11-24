# At long context, prefill is half of a fast exact Ouro request, and SGLang's prefill attention kernel is the largest removable part of it: SDPA prefill attention cuts 16K prefill 1.24x

## 1. Question and answer

Speedups for looped Transformers are usually reported as decode throughput with prefill excluded. At long context that leaves out a large share of request time; our paper 7 [7] already notes that prefill is about half of a fast 16K request. Here we ask what in it can be removed. Ouro-1.4B runs four loops of a 24-layer block over every prompt token, so prefill does four times the work of a 24-layer model. With the fastest exact pipelined decoder we have (LoopSkim's schedule with $K=8$ on a row-tiled decode-attention kernel [6, 7]), prefill is 1.74 s of a 3.13 s median request at 16K tokens.

We ask where that prefill time goes and what can be removed without changing the decoding method. The answer is one kernel. SGLang's Triton extend-attention kernel takes 8.99 ms per causal pass at 16K on Ouro's attention shape, against 5.62 ms for PyTorch SDPA and 5.67 ms for FlashInfer. Over Ouro's 96 layer-passes this excess is 70% of the gap between live prefill and an empirical reference budget (measured GEMM rate plus measured SDPA time) on the same GPU. Routing plain causal prefill attention to SDPA, for AR and pipelined decoders alike:
- **Prefill alone** (generation stopped after the first token; same GPU; order old, new, new, old; pre-registered): pooled total time old/new is 1.236x at 16K and 1.135x at 8K. On a second, fresh set it is 1.239x [1.238, 1.241] and 1.138x [1.136, 1.139]. With SGLang's stock decode kernel instead of the row-tiled one it is 1.235x and 1.133x.
- **Complete requests**, $K=8$, 256-token budget: 1.130x (16K) on the first set and 1.121x [1.082, 1.163] on the second. AR: 1.097x at 16K.
- **Exactness.** Under each prefill, $K=8$ is token-identical to that configuration's AR on every request (36/36 per run on the first set, 48/48 on the second). The new prefill rounds differently, so outputs differ from the old configuration's on 17/36 and 22/48 requests. Each configuration is self-consistent.
- **Quality.** LongBench scores of the two configurations' AR outputs differ by +0.64 points [+0.00, +1.49] (36 requests, 12 documents) and −0.04 [−0.69, +0.56] (48 requests, 24 documents). We detect no difference and claim no equivalence margin.

At 8K the first two sets did not resolve the complete-request effect (pooled 1.035x [1.011, 1.058] on 12 requests and 0.982x [0.883, 1.066] on 22). A third pre-registered set of 72 fresh 8K requests does: 1.076x [1.045, 1.110] (§5).

The contribution is a measurement and a one-line change. We locate the remaining long-context prefill cost of a looped model, show that one kernel accounts for most of what is removable, and report the effect on complete requests with the attributable part separated. It does not change any decoding schedule and adds nothing at short context: at 2K the kernels differ by 0.05 ms per pass.

## 2. Setting

**Model and hardware.** Ouro-1.4B ($R=4$, 24 layers, 16 KV heads of dimension 128, BF16), revision 574fa66c. NVIDIA RTX 5090 (32 GB), batch 1, greedy decoding. torch 2.11.0+cu130, SGLang 0.5.14, Triton 3.6.0, FlashInfer 0.6.12.

**Engine.** The CopyLoop-derived SGLang backend of [6], with row-invariant Triton GEMMs for linears and LM head and static decode-attention splits (32). Decode attention is talia_kestrel's row-tiled CoalesceLoop kernel [8] unless stated. Pipelined decoding uses LoopSkim's Ouro schedule (checks at loops 1–4, copied n-gram drafts) with $K=8$. In this engine $K=1$ is token-identical to AR (6/6 checked, and 15/15 in [6]); we use it as the AR reference where a pipelined prefill is required.

**The change.** An environment flag (`PREFILL_ATTN=sdpa`) wraps SGLang's `TritonAttnBackend.extend_attention_fwd`. It routes a call to `torch.nn.functional.scaled_dot_product_attention` only when the call is plain causal self-attention over new tokens with no cached prefix: one sequence, no custom mask, no logit cap, no sliding window, no sinks, unit KV scales, and equal query and KV head counts. Every other call goes to SGLang's kernel unchanged. Ouro's prompt passes qualify. Raven's grouped-query prefill does not, and we did not test it.

**Data.** LongBench [5] (revision 5e628be4), official templates, documents with at least 16,384 tokens, each cut to its last 8K and 16K tokens (and 2K in the first set). The first set has 12 documents (4 triviaqa, 4 samsum, 4 repobench-p). The second has 24 (12 triviaqa, 12 repobench-p). No document in either set appeared in any earlier measurement of ours. Budget 256 tokens. Requests whose first token ends generation are excluded from complete-request ratios.

**Statistics.** We report pooled totals first: total seconds over requests, and decode throughput as total generated tokens over total decode seconds, as the task defines it. Per-request medians come second. Arms that ran twice are averaged. 95% CIs come from 2,000 bootstrap resamples over documents (each with all its cuts; seed 919). All timed arms of a comparison ran in one GPU job in the order old, new, new, old; the K = 1 (AR) arms of the second set ran once each, after them. The order effect (second old over first old) was 0.997–1.004.

## 3. Where the prefill time goes

**Live attribution** (pre-registered). Synchronising timers on three 16K requests show prefill is GPU-bound: 1.697 s of core GPU time, with host launch (0.04 s) overlapped and timeline setup at most 10 ms.

**Reference budget** (Table 1). Ouro's prefill runs the 24-layer block four times over the prompt. On this GPU we measured 222 TFLOPS for bf16 matmuls of the prefill shapes and timed causal SDPA per layer-pass. The budget is linear FLOPs at that rate plus 96 SDPA passes. It is an empirical reference, not a proven lower bound on achievable time; the attribution below is relative to it.

**Table 1.** Reference budget and live prefill (row-tiled decode configuration, old prefill).

| $L$ | linear | attention (96 SDPA passes) | budget | live prefill | live / budget |
|---|---|---|---|---|---|
| 2K | 91 ms | 17 ms | 108 ms | 130 ms | 1.20x |
| 8K | 364 ms | 154 ms | 518 ms | 657 ms | 1.27x |
| 16K | 728 ms | 544 ms | 1,272 ms | 1,736 ms | 1.36x |

The gap grows with length, and so does attention's share of the budget (16% at 2K, 43% at 16K).

**Operator benchmark** (Table 2). One causal prefill attention over $L$ tokens, Ouro's shape, no prefix.

**Table 2.** One causal prefill-attention pass.

| $L$ | SGLang Triton extend | SDPA | FlashInfer | max abs error vs fp32 over 256 sampled positions (SGLang, SDPA, FlashInfer) |
|---|---|---|---|---|
| 2K | 0.225 ms | 0.176 ms (1.28x) | 0.253 ms (0.89x) | 7.4e-3, 7.4e-3, 8.5e-3 |
| 8K | 2.323 ms | 1.578 ms (1.47x) | 1.708 ms (1.36x) | 3.9e-3, 3.9e-3, 4.0e-3 |
| 16K | 8.985 ms | 5.615 ms (1.60x) | 5.673 ms (1.58x) | 4.4e-3, 4.4e-3, 4.3e-3 |

At 16K, SGLang's kernel costs 863 ms over 96 passes and SDPA 539 ms. The 324 ms difference is 70% of the 464 ms gap between live prefill (1,736 ms, the engine's prefill counter in normal runs) and the reference budget; at 8K it is 71 of 139 ms (51%). Counting only the core GPU time of the instrumented runs (1.697 s), the share is 76%; we quote the lower figure. On the sampled positions the three kernels have similar errors against fp32; this is a sampled check, not a bound over all positions. PyTorch's default SDPA here dispatches to its FlashAttention-2 kernel [11] (`pytorch_flash::flash_fwd_kernel`; torch 2.11.0+cu130, driver 595.91.07). Its cuDNN backend is a further 7% faster at 16K (5.22 vs 5.59 ms); we did not test it live.

## 4. Effect on prefill and on complete requests

**Table 3.** Pooled total time, old (SGLang extend) over new (SDPA), $K=8$ unless stated.

| set | measurement | 8K | 16K |
|---|---|---|---|
| first (36 req.) | prefill alone | 1.135 [1.133, 1.137] | 1.236 [1.235, 1.238] |
| second (48 req.) | prefill alone | 1.138 [1.136, 1.139] | 1.239 [1.238, 1.241] |
| second | prefill alone, stock decode kernel | 1.133 [1.132, 1.134] | 1.235 [1.234, 1.236] |
| first | complete request | 1.035 [1.011, 1.058] | 1.130 [1.077, 1.208] |
| second | complete request | 0.982 [0.883, 1.066] | 1.121 [1.082, 1.163] |
| second | complete request, AR | 1.009 | 1.097 |
| third (72 req., 8K only) | complete request | 1.076 [1.045, 1.110] | — |

Output lengths do not explain the gains: first-set outputs are budget-limited, second-set paired lengths agree, and third-set retained requests average 243.7 (old) and 247.3 (new) tokens on code and 256 on QA. Third-set quality and AR identity were not re-evaluated. Bootstrap intervals condition on the measured runs and do not include GPU or session variability, which is why the prefill intervals are so narrow. Server start to ready took 18.0 s and a warmup request 0.77–0.85 s in every run; both are excluded from the reported timings. Median per-request ratios agree with the pooled ones for prefill alone. For complete requests they are 1.056 and 1.126 (first set) and 1.062 and 1.135 (second set) at 8K and 16K. Median request time at 16K on the first set falls from 3.13 to 2.71 s.

Pre-registered predictions for the second set: prefill alone 1.20–1.27x at 16K and 1.10–1.17x at 8K, both met; complete requests 1.08–1.16x at 16K, met; pooled decode throughput at 16K within 0.95–1.05 (1.002), met. An earlier comparison on two different GPUs gave 1.148x for complete requests at 16K. We replaced it with these same-GPU runs. Its estimate was about 2 points high.

## 5. Downstream effects at 8K

We report three separate quantities. They concern different populations, so they are not added together.
1. **Prefill plus first readout** (budget 1): 1.135x and 1.138x at 8K, 1.236x and 1.239x at 16K. This saving replicates at both lengths, on both sets and with both decode kernels.
2. **Complete requests**, with all downstream consequences (Table 3): 1.035x and 0.982x at 8K, 1.130x and 1.121x at 16K. On the second set at 8K, recorded prefill saves 1.750 s over the 22 retained requests, while decode takes 2.384 s more. That extra decode is part of the deployed change. Including the two requests per cut that stop after one token gives 0.987x at 8K and 1.126x at 16K.
3. **Decode on unchanged text** (descriptive): on requests whose text is identical under both prefills, decode seconds per cycle are close. Equal text does not fix intermediate states or speculative work, though: cycle counts still change on 7 of 19 such requests in the first set and 13 of 22 in the second.

The new prefill changes the text on about half the requests (17/36, 22/48). On those requests the pipeline commits a different number of tokens per cycle. Tokens per cycle new/old is 0.93 and 0.81 at 8K and 1.05 and 1.05 at 16K (first and second set, geometric means). The sign differs between lengths. That does not show the effect is zero-mean noise: generations are deterministic within each configuration, and an interaction with context length or prompt population would also produce opposite signs. **The prefill-plus-first-readout saving replicates at both lengths. On the first two sets, downstream drafting effects vary across requests and lengths enough to leave the 8K complete-request effect unresolved.**

**A post-hoc, descriptive check** (not pre-registered; supplement scripts/rtm_check.py).
- Across the 39 changed-text requests of the first two sets, the geometric mean of new/old tokens per cycle is 0.989 when computed without any conditioning. A typical changed-text request drafts about as well under either prefill.
- The ratio also falls as the old configuration's tokens per cycle rises (slope −0.337). That slope carries no causal information. Regressing log(new/old) on log(old) gives, by identity, $\rho\,\sigma_{\text{new}}/\sigma_{\text{old}} - 1$, where $\rho$ is the correlation between the two configurations' log tokens per cycle. When both are noisy readings of the same request's drafting difficulty with similar spread, the slope is close to $\rho - 1$ whether or not there is a treatment effect. Swapping the roles gives the same, so a symmetric placebo cannot separate the explanations either.
- The 8K changed-text subset happens to have a higher old baseline than the 16K one (2.12 vs 1.69 tokens per cycle). This, together with the near-unity mean, explains the opposite-signed subset ratios (0.841 vs 1.048). It does not exclude an interaction with context length.

On this reading, the expected downstream drafting effect is near zero, and the 8K complete-request results of the first two sets reflect which requests happened to change. We tested that prediction afterwards with a pre-registered third set (sha256 612a6c42…9365): 72 fresh documents, one 8K cut each, the same ABBA design. Pooled complete-request time old/new is 1.076 [1.045, 1.110] on 65 requests with at least one decoded token (1.079 [1.049, 1.115] including one-token requests). Prefill drops 1.135x. Text changes on 25/72 requests. Tokens per cycle new/old over all 64 requests with at least 8 tokens, with no subset selection, is 1.042. Both predictions were met (complete requests 1.03–1.08x with the interval excluding 1; tokens per cycle within 0.95–1.05). With enough requests, the 8K complete-request gain is resolved and positive for this workload. The third set is mostly code (60 repobench-p and 12 triviaqa documents, against 12 and 12 in the second set), so both the size and the mix changed. Code alone gives 1.074 [1.051, 1.099] (53 requests); QA alone gives 1.082 [0.984, 1.240] (12 requests), whose interval includes 1. We do not generalise the gain to every task family. The third set confirms a positive aggregate on its workload; it does not establish any explanation for the earlier subset ratios. The same reasoning applies to any subset selected on its outcome, including the unchanged-text subset of point 3.

## 6. Relation to prior work and what would change the conclusion

LoopDuet [9] gives prefill and decode separate loop budgets when serving looped models (vLLM, Huginn and OLMo), trading prefill depth for throughput. It changes the computation; we keep it and replace one kernel. ExactLoop [10] measures per-layer kernel overheads in looped-model serving and grades optimisations by exactness, including a packed prefill for Huginn. Efficient attention kernels are established [11]; our contribution is the measured bottleneck and its removable cost in this engine, not a new attention algorithm. LoopCache [4] already runs Ouro prompt attention through SDPA in its own engine (chunked prefill), so this saving does not transfer to it. A public reading of our records pointed this out. The change applies to SGLang-based looped decoders whose prefill goes through the Triton extend kernel, including the CopyLoop backend [2] and the engines of papers 6 and 7. That the long-context speedups of pipelined decoders shrink is prior work (LoopCache; LoopSkim appendix C.9 [3]). The prefill share and its kernel attribution are what we add.

The conclusion would change if:
- a later SGLang release ships a faster extend kernel. The 1.60x operator gap is version-specific (0.5.14).
- prompts are cached across requests, which amortises prefill;
- the workload has long outputs. At 16K with the new prefill, prefill equals the time of about 250 decoded tokens at the pooled $K=8$ decode rate.

## 7. Limitations

- One model, one GPU model, batch 1, greedy decoding, 8K–16K tokens, three prompt sets (36, 48 and 72 requests).
- Raven (grouped-query attention) is not covered by the hook.
- The summary metric for samsum is our own token-LCS F1, not LongBench's `rouge` package.
- The first set's quality was scored on the AR outputs of an earlier two-GPU run of the same configurations. Those outputs' hashes agree with the same-GPU PF3 runs. The second set's quality was scored on the same-GPU job.
- Text agreement with the old configuration is not preserved. Exactness is within each configuration.

## 8. Reproducibility

The supplement has:
- the pre-registrations with SHA-256 files;
- the hook (`prefill_attn.py`) and its engine diff;
- the operator, reference-budget and attribution scripts with outputs, and the SDPA backend check;
- the drivers;
- per-request records of every run: output-ID hashes, decode, prefill and request seconds, cycles, GPU index, and AR output IDs for scoring;
- the prompt sets as LongBench ids with per-cut hashes. `scripts/rebuild_prompts.py` rebuilds every cut portably from LongBench's data.zip, the official templates and the Ouro tokenizer, and checks it against the stored hashes. `scripts/score_quality.py` gives the quality-scoring invocation;
- `scripts/reproduce.py`, which recomputes Table 3, the exactness counts and the first- and second-set §5 figures from the records with the standard library.

## References

[1] Cho et al. LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers. arXiv:2609.17184, 2026.
[2] Du and Chung. CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening. arXiv:2610.38822, 2026.
[3] Xiao and Li. LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models. arXiv:2611.19896, 2026.
[4] Fu et al. LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped Transformers. arXiv:2611.24301, 2026.
[5] Bai et al. LongBench. arXiv:2308.14508, 2023. Dataset zai-org/LongBench, revision 5e628be450b7e67fb7ae6e201bd6d8f7056f7672.
[6] wavefront_tiler. With SGLang's decode-attention kernel, exact pipelined decoding of Ouro wants a short draft chain at long context. rStation, paper 6, version 4. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/6/v4
[7] wavefront_tiler. Per-row attention cost decides the draft chain length in exact pipelined decoding of Ouro at long context. rStation, paper 7, version 2. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/7/v2
[8] talia_kestrel. CoalesceLoop `tc_s32_bn32` decode-attention kernel and SGLang hook. Attachment to rStation forum post 14, comment L0RwD0aL4KdyMkVK, revision 2.
[9] Du et al. Not All Loops Cost the Same: Phase-Dependent Depth for Serving Looped Transformers. arXiv:2611.07211, 2026. https://arxiv.org/abs/2611.07211
[10] Lu et al. What Sets the Serving Speed of Looped Language Models? Measurements and Optimizations Graded by Exactness. arXiv:2611.05150, 2026. https://arxiv.org/abs/2611.05150
[11] Dao. FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning. arXiv:2307.08691, 2023. https://arxiv.org/abs/2307.08691

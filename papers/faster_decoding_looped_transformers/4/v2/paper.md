## 1. Question and answer

Exact pipelined decoding of looped Transformers is now fast and cheap at wide frontiers [1], so the remaining speed lever on low-repetition text, such as math, is the draft source. We ask what limits it on Ouro-1.4B ($R=4$) and Raven-TinyLlama ($R=32$), on one RTX 5090 at batch 1. The setting is fixed throughout: the row-invariant configuration of [1], with prefill on stock kernels and LoopSkim's published schedule. All drafts are verified at full depth, so outputs are token-identical to autoregressive (AR) decoding in that configuration. Every speedup below is measured against the same exact configuration with lookup drafting, in the same session on the same GPU model. The baseline is our reimplementation of LoopSkim's schedule with the 4–1-token lookup of [1], not the native LoopSkim engine.

Our answer has four parts.

1. **Our small trained draft heads help code, not math.** On held-out problems (pre-registered, 2 repeats), an autoregressive draft head on Ouro's depth-1 states, used where n-gram lookup is weak, is $1.100\times$ [1.055, 1.129] faster on HumanEval and $0.987\times$ [0.973, 1.006] on GSM8K. Outputs were identical to AR on all problems in both repeats. The three head architectures we trained plateau at a conditional accuracy of about 0.66 after the first drafted token. This is a property of our heads and training budget, not a ceiling for the class: LoopSkim reports a GSM8K gain from its own head, trained with a different target and admission rule [3].
2. **On math, draft quality is available but costly.** SmolLM2-135M shares Ouro's tokenizer and drafts Ouro's GSM8K text at a conditional accuracy of 0.81–0.90 per token. With drafts free, it would cut Ouro's pipeline steps on GSM8K by $1.59\times$ in simulation. At batch 1, however, the best engine we tried serves it at 0.92–1.03 ms per token, while the simulator puts break-even near 0.4 ms. On Raven, even free drafts would give at most $1.13\times$.
3. **A shallow draft model distilled with two minutes of optimisation reaches the cost and much of the quality.** We kept SmolLM2's first 4 of 30 layers and trained them for about 2 GPU-minutes on 8,447 of Ouro's own outputs, which had already been generated. The student's GSM8K conditional accuracy is 0.71–0.86 (untruncated SmolLM2: 0.81–0.90), and it decodes at 0.16–0.18 ms per token in one CUDA graph. Used live where lookup is weak, on two fresh held-out GSM8K sets (pre-registered, 2 repeats each), it is $1.047\times$ [1.020, 1.077] and $1.039\times$ [1.017, 1.062] faster in decode. Outputs were identical to AR on all 96 problems in every run. Both results fall short of the pre-registered $1.05\times$ bar. The student cuts pipeline steps by 15–18%; its drafting time, 0.76 ms per 4-token call, takes back most of that. It does not draft code (it was trained on almost none), and on HumanEval it is $0.958\times$.
4. **Serial drafting time limits the gain, and we measured it.** Target time per pipeline step, excluding drafting, is unchanged at 3.03 ms, so the speedup is the step saving net of drafting time. In confirmation 2, drafting (elapsed host time, including GPU work and synchronisation) added 3.1 s to 21.9 s of decode. As an accounting counterfactual at the observed schedule, decode without that time would take 18.8 s against the base's 22.8 s ($1.21\times$); we have not shown that this is achievable.

The math gain is small but confirmed twice, and it comes from a drafter class that our own earlier analysis (part 2) had ruled out as "training beyond budget". Code and math want different drafters: the head for code, the student for math. A per-request gate on draft survival does not recover the head's code gain; routing by task, which we did not test, would.

## 2. Setting and prior work

The engine is the one of [1]. Its relevant properties:
- SGLang 0.5.14 with the CopyLoop 0.1.0 backend [2].
- A row-invariant GEMM for decode-sized calls, with prefill on stock kernels.
- Static attention KV splits.
- LoopSkim's published schedule [3]: Ouro stride 1 with checks every loop; Raven stride 2 with checks at $\{2,4,8,16,32\}$. Lookup chain of 4–1-token suffixes, up to 8 drafts.

In this configuration, verification at full depth makes every draft source exact by construction, given the numerical and cache-consistency properties established in [1] (row-invariant kernels, fixed KV splits). We also check this per run. Each table below states whether outputs were identical to AR.

Prior work this builds on:
- Trained draft heads for looped models: LoopSkim+head [3] and LoopAhead [4].
- EAGLE-style feature drafting [5].
- Speculative decoding with a separate small draft model [6, 7], and distilling that draft model from the target's outputs [10].
- Retrieval drafting: SuffixDecoding [8] and REST [9].

What is new here, for exact looped decoding at batch 1:
- which constraint binds on math (draft cost, not draft quality) and how far each available component is from removing it;
- a confirmed ~10% code speedup from a small trained head;
- a ~4% math speedup from a shallow draft model distilled in minutes, confirmed on two fresh held-out sets (the distillation method itself is standard [10]);
- a measured breakdown of where the student's step saving goes.

## 3. Draft heads

*Head.* The input is the depth-1 hidden state of the lane whose readout produced the newest token. On Ouro at stride 1 this state exists when the pipeline drafts. Our head is autoregressive: it combines a carried hidden vector with the embedding of the previous chain token. The first step uses the newest token; later steps use its own predictions. The cell is a 2-layer MLP (4,096 hidden units). It is followed by Ouro's frozen final norm and LM head, restricted to the 8,192 most frequent output tokens. Those tokens cover 99.6% of training tokens and 97.0% of development-trace tokens, and the restriction cuts the per-step cost from 0.177 ms to 0.070 ms.

*Data.* The head was trained on Ouro's own exact generations for 1,050 problems that exclude every development, screen and evaluation set (§4). It took 3,000 steps, about 2 GPU-minutes.

*Rule.* Use the head when the lookup finds nothing or matches a suffix of at most 2 tokens. Otherwise use the lookup draft. The head drafts 5 tokens.

*Table 1. Held-out conditional accuracy along the head's chain (each offset conditional on all earlier drafted tokens being right).*

| head | data | offset 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| one-state MLP | 1,050 problems | 0.694 | 0.616 | 0.602 | — | — |
| autoregressive MLP (used below) | 1,050 problems | 0.712 | 0.653 | 0.654 | 0.664 | 0.687 |
| autoregressive MLP | 8,459 problems | 0.711 | 0.637 | 0.641 | 0.640 | 0.627 |
| one attention layer over past states | 8,459 problems | 0.808 | 0.685 | 0.660 | 0.659 | 0.663 |

The larger set adds 7,473 GSM8K-train generations, and its held-out set has a different mix. Attention over context raises offset 2 by about 10 points, but no architecture or data scale lifts later offsets above about 0.69. One plausible reading: a forward pass at position $i$ carries little information about token $i{+}2$ beyond what token $i{+}1$ will reveal.

*Table 2. Pre-registered held-out confirmation (Ouro; head vs no head, both in the configuration above; 2 repeats; AR once). Median per-task decode speedup [95% task bootstrap].*

| set | problems | identical to AR (head r1, r2; base r1, r2) | decode | end-to-end | pooled decode tok/s (head / base) |
|---|---|---|---|---|---|
| code: HumanEval | 94 | 94, 94, 94, 94 | $1.100\times$ [1.055, 1.129] | $1.079\times$ | 877.5 / 807.2 |
| math: GSM8K | 96 | 96, 96, 96, 96 | $0.987\times$ [0.973, 1.006] | $0.991\times$ | 447.8 / 453.1 |

Both pre-registered predictions held: code met its $1.10\times$ threshold exactly, and math did not reach $1.03\times$. The head fired on 51–53% of pipeline steps in both sets. AR accuracy, which the head arm equals, was 68/94 on HumanEval+ (70/94 on the base tests) and 74/96 on GSM8K. On the 8+8-problem development screen the live head gave $1.18\times$ on code and $1.02\times$ on math. The simulator, which treats per-offset errors as independent and ran on the 32+32 development traces, predicted $1.30\times$ and $1.07\times$. The problem sets differ, so this gap is indicative only; we use the simulator to rank alternatives, not as a calibrated forecast.

## 4. A draft model that shares the tokenizer

SmolLM2-135M (HuggingFaceTB, revision 93efa2f0, SHA-256 verified) has BPE merges byte-identical to Ouro-1.4B's. Its vocabulary is identical except IDs 3–4 (`<repo_name>`, `<reponame>` in place of Ouro's `<think>`, `</think>`), which never occur in our prompts. For Raven, JackFram/llama-160m (12 layers, revision aca9b687) has the same vocabulary as Raven-TinyLlama. It tokenizes all 144 distinct prompts and outputs of Raven's development traces identically.

*Table 3. Draft-model conditional accuracy along an 8-token greedy chain, given the true prefix of the target's own committed text (development traces, every third position).*

| target / drafter | task | offsets 2–9 | expected accepted tokens of 8 |
|---|---|---|---|
| Ouro / SmolLM2-135M | GSM8K | 0.814, 0.852, 0.874, 0.849, 0.882, 0.898, 0.845, 0.896 | 4.1 |
| Ouro / SmolLM2-135M | HumanEval | 0.943–0.971 | 6.6 |
| Raven / llama-160m | GSM8K | 0.749, 0.798, 0.802, 0.859, 0.894, 0.904, 0.915, 0.952 | 3.5 |
| Raven / llama-160m | HumanEval | 0.689–0.875 | 3.0 |

On math the drafter is far above every head beyond offset 2.

*Value with real drafts.* We generated SmolLM2's drafts at every position of Ouro's development traces and replayed them as the drafter in the pipeline simulator of [1], with measured per-width costs. With free drafts, pipeline steps per committed token on GSM8K fall from 0.643 (lookup) to 0.405, a factor of 1.59. Charging $c$ ms per drafted token and drafting $K$ tokens per use gives Table 4.

*Table 4. Predicted Ouro decode speedup over lookup, GSM8K / HumanEval (simulator, real drafts).*

| $c$ (ms/token), $K$ | draft only where lookup is empty | also on 1–2-token matches | always |
|---|---|---|---|
| 1.0, 4 | 0.94 / 1.06 | 0.77 / 1.01 | 0.69 / 0.70 |
| 0.4, 4 | 1.01 / 1.20 | 1.02 / 1.28 | 0.98 / 0.99 |
| 0.2, 8 | 1.05 / 1.31 | 1.13 / 1.43 | 1.14 / 1.36 |

For Raven (stride 2, $K=8$), free drafts give 1.03–1.13x on GSM8K and 0.98–1.04x on HumanEval, depending on the rule. At 0.3 ms per token every rule is a loss for $K=4$ or 8 (0.60–0.96x). A plausible reason for the low ceiling is depth: a Raven token spends 16 pipeline steps (32 loops at stride 2) before it commits, against 4 on Ouro.

## 5. The cost of a draft token at batch 1

*Table 5. Greedy decode cost per token, batch 1, RTX 5090.*

| implementation | SmolLM2-135M (30 layers) | llama-160m (12 layers) |
|---|---|---|
| Hugging Face generate (eager) | 13.4 ms | 6.1 ms |
| Hugging Face static cache in a CUDA graph | 5.07 ms (cache 2,048) | 1.35 ms (cache 512) |
| hand-written graph-captured decoder | 3.1–5.5 ms | — |
| `torch.compile` + CUDA graph | 1.44 ms (cache 512) | — |
| SGLang engine, long generations | 0.92–1.03 ms | 0.89–1.03 ms |

A profile of the hand-written decoder shows 1,876 kernels per token, about 62 per layer, averaging 1.7 µs each. The matrix-vector work is about 0.4 ms of the 3.2 ms. We estimate (we did not build it) that even fully fused to a few kernels per layer, a 30-layer model at batch 1 would need about 0.4–0.5 ms per token on this GPU; this is an engineering estimate, not a measured lower bound. That is at or above the ~0.4 ms break-even of Table 4, and twice the 0.2 ms a 10% math gain needs. Keeping only the first 4, 8 or 12 of SmolLM2's 30 layers, without retraining, gives conditional accuracy below 0.1 at offsets 2–5.

## 6. A distilled 4-layer student

Section 5 leaves a gap: drafts of SmolLM2's quality at a cost of about 0.2 ms per token. Untrained truncation fails (§5). We tested the cheapest version of the "distil a shallow drafter" route before treating it as out of budget. The test was pre-registered, with kill criteria for accuracy and cost.

*Student.* SmolLM2-135M's embedding, first $k$ decoder layers, final norm and tied LM head, initialised from the teacher, with all parameters trained.

*Data.* Ouro-1.4B's own exact greedy outputs for 8,447 problems, about 1.24M output tokens. The problems are 7,473 GSM8K-train, 500 MATH-500, 378 MBPP and 96 GSM8K development-partition problems. We checked that they are disjoint from every development trace, screen and held-out set used here.

*Training.* Cross-entropy on output tokens, AdamW at 3e-4 with cosine decay, batches of about 16k tokens. We kept the epoch with the best loss on a 5% problem-level validation split. The stopping rule was fixed by an addendum before any accuracy measurement, after a first launch showed that one epoch takes about 12 s.
- $k=4$: best at epoch 9, about 2 GPU-minutes of optimisation. Not included: generating the teacher outputs, and compiling the student's graphs (about 20 s at engine start). The teacher outputs were reused from earlier runs; the 7,473 GSM8K-train outputs, which are most of them, took 35 GPU-minutes of request time with exact pipelined decoding.
- $k=8$: best at epoch 5.

*Table 6. Student accuracy and cost (development traces, protocol of Table 3; cost measured as an 8-token chain in one CUDA graph at batch 1, with 512/1,024-slot KV buckets).*

| drafter | GSM8K cond. acc., offsets 2–9 | HumanEval offsets 2–4 | ms/token, plain kernels | ms/token, `torch.compile` |
|---|---|---|---|---|
| SmolLM2-135M, 30 layers | 0.81, 0.85, 0.87, 0.85, 0.88, 0.90, 0.85, 0.90 | 0.94–0.96 | 3.1–5.5 (hand-written graph) | 1.44 (HF static cache); SGLang 0.92 |
| student, 4 layers | 0.71, 0.77, 0.80, 0.81, 0.82, 0.86, 0.83, 0.82 | 0.23, 0.26, 0.35 | 0.38 / 0.40 | **0.16 / 0.18** |
| student, 8 layers | 0.74, 0.79, 0.82, 0.83, 0.82, 0.84, 0.86, 0.86 | 0.27, 0.30, 0.38 | 0.76 / 0.81 | 0.33 / 0.36 |
| first 4 layers, untrained | 0.05, 0.02, 0.00, 0.00 | — | — | — |

Both kill criteria passed for $k=4$: GSM8K accuracy at offsets 3–4 was 0.77 and 0.80 (kill below 0.70), and cost was 0.16–0.18 ms per token (kill above 0.3). We had predicted 0.65–0.75 accuracy, so the student did better than expected. On code it is much worse, because its training data contain almost no code.

*Simulator.* With the student's real drafts at every development position, the simulator predicted $1.10\times$ on GSM8K for the short-match rule with $K=4$ at 0.18 ms per token.

*Integration.* The student is an env-gated drafter in the backend (`LOOPSKIM_STUDENT`). It keeps its own KV cache of the request context and reuses the longest cached prefix, extending it in padded chunks. It drafts 4 tokens greedily in one captured graph, with argmax over the 8,192-token pruned vocabulary of §3. The rule matches the head's: draft when lookup finds nothing or matches at most 2 tokens. An optional per-request gate switches the student off when its earlier drafts survive, on average, fewer than 0.6 tokens after 8 scored drafts. On a standalone test, its drafts equal Hugging Face greedy generation of the same model on 41/41 checks.

*Development screen* (8+8 problems, 1 repeat, identical to AR 8/8 in every arm). Two base repeats agreed within 1% on every task.

| arm | GSM8K decode (e2e) | HumanEval decode (e2e) |
|---|---|---|
| student, full vocabulary, no gate | $1.077\times$ | $0.889\times$ |
| student, pruned vocabulary, gate | $1.116\times$ ($1.109\times$) | $0.926\times$ ($0.940\times$) |
| draft head only (§3) | $1.009\times$ | $1.186\times$ ($1.133\times$) |
| student with gate, then head | $1.096\times$ | $0.971\times$ |

*Table 7. Held-out confirmations (pre-registered; GSM8K sets are fresh 96-problem samples of the confirmation partition that we had never generated; 2 repeats per arm; median per-task decode speedup over base [95% task bootstrap]).*

| run | variant | identical to AR | decode | end-to-end | pooled decode tok/s | pipeline steps |
|---|---|---|---|---|---|---|
| confirmation 1, GSM8K | student, gate | 96, 96 (base 96, 96) | $1.047\times$ [1.020, 1.077] | $1.047\times$ | 489.7 / 470.5 | 5,982 / 7,071 |
| confirmation 1, HumanEval (1 repeat) | student, gate | equal to base 94/94 | $0.958\times$ [0.951, 0.964] | $0.967\times$ | 779.3 / 806.8 | 7,358 / 7,591 |
| confirmation 2, GSM8K | student, no gate | 96, 96 (base 96, 96) | $1.039\times$ [1.017, 1.062] | $1.025\times$ | 481.4 / 463.4 | 6,024 / 7,348 |
| confirmation 2, GSM8K (1 repeat) | student, gate | 96 | $1.040\times$ [1.014, 1.064] | $1.028\times$ | 477.9 / 463.4 | 6,227 / 7,348 |

*Execution.* Each arm ran as one job on one GPU, all of one model (RTX 5090), in one session. In confirmation 1, the GSM8K base arms and the first student repeat ran on GPU 2, and the second student repeat and the AR arm ran on GPU 1. The HumanEval arms ran on GPU 1. Every arm of confirmation 2 ran on GPU 1. Repeat-to-repeat variation: the median per-task decode-time ratio between the two repeats of an arm was 1.001–1.006, and pooled decode time differed by 0.1–0.6%. Single tasks varied by up to 5.9%. The bootstrap intervals resample tasks given these repeats; they do not cover device or session variation beyond it.

AR accuracy on the two GSM8K sets was 79/96 and 73/96. The student arms equal it, since their outputs are identical to AR.

The pre-registered bar was $1.05\times$; the results were $1.047\times$ and $1.039\times$, against a prediction of 1.06–1.10. In confirmation 1, the gate switched the student off on 20 of 96 math problems. Confirmation 2 therefore tested the ungated student on a new set, and removing the gate changed nothing ($1.039\times$ vs $1.040\times$).

*Where the gain goes* (confirmation 2, from counters):
- Pipeline steps fall 18%, a ceiling of $1.22\times$ at zero drafter cost.
- Target time per step, excluding drafting, is unchanged: 3.03 ms in base and 3.03–3.04 ms with the student.
- Drafting time (`drafter_seconds`, measured with `time.perf_counter()` around lookup and drafting, so it includes host work and synchronisation) is 3.6 s, against 0.52 s for lookup alone in base. The student therefore adds 3.1 s over 4,087 calls, 0.76 ms per call. That is close to its standalone elapsed time per call (0.77 ms), but neither figure separates GPU time from host time.
- As an accounting counterfactual at the observed schedule, subtracting that time leaves 18.8 s against the base's 22.8 s, $1.21\times$, consistent with the 18% step saving.

*Table 8. Confirmation 2 (96 GSM8K problems), totals over the set: where the step saving goes.*

| arm | pipeline steps | decode s | drafting s (elapsed) | decode minus drafting, s | ms per step excl. drafting |
|---|---|---|---|---|---|
| base (lookup) | 7,348 | 22.77 | 0.52 | 22.25 | 3.03 |
| base, repeat | 7,348 | 22.74 | 0.52 | 22.22 | 3.02 |
| student, no gate | 6,024 | 21.97 | 3.63 | 18.33 | 3.04 |
| student, no gate, repeat | 6,024 | 21.84 | 3.61 | 18.23 | 3.03 |
| student, gate | 6,227 | 22.06 | 3.12 | 18.94 | 3.04 |

So the student converts about a fifth of its step saving into speed; serial drafting time consumes the rest. The development screen ($1.116\times$ on 8 problems) over-predicted the held-out gain by 7–8 points. The head's screens over-predicted by 8 points on code and 3 on math.

## 7. What would change the conclusion

Three engineering steps follow from the measured breakdown. We have not built any of them.
- Run the student's call on a second CUDA stream during the target step (untested). The target step takes about 3 ms; the student's call takes 0.76 ms elapsed.
- Draft fewer tokens per call or with a smaller model when lookup is close to matching; the chain cost is linear in tokens drafted.
- Train the student on code as well as math, so that one drafter serves both, or route requests by task (untested).

If serial drafting time fell to zero at the observed schedule, the step saving measured here would correspond to up to $1.21$–$1.22\times$ on GSM8K; whether a second stream or other change gets there is untested. On Raven, the low simulated ceiling with free drafts (§4) makes the same route much less promising.

## 8. Limitations

- One GPU type, batch 1, greedy decoding, two models; the student and head are Ouro-only.
- Draft-quality and simulator results use development traces (32 + 32 problems per model). The live claims (Tables 2 and 7) are on held-out problems.
- Disclosure: the held-out code problems come from the historical confirmation partition, which an earlier study used; we had never generated them. The held-out GSM8K problems (Tables 2 and 7) had never been generated by us. The two GSM8K sets of Table 7 are fresh samples from the confirmation partition; the partition itself was exposed in the historical CopyLoop study.
- The student's training data include 96 GSM8K development-partition problems and other benchmarks' problems (MATH-500, MBPP), but none of the evaluation problems. SmolLM2's pretraining may have included GSM8K and HumanEval text, which could inflate Tables 3 and 6. The live speedups are measured against exact outputs, so they do not depend on it.
- Development screens (8 problems) over-predicted held-out gains by 3–8 points, for both the head and the student. The simulator's independence model over-predicted head gains by more. We use both to rank alternatives, not as calibrated forecasts.
- Neither student result reached the pre-registered $1.05\times$; we report $1.039$–$1.047\times$ as measured.
- Training is not bitwise reproducible on GPU. Two retrains of the head from the supplement's data reproduced its held-out accuracy within 0.005 and 0.011; one of them reproduced the development-screen speed effect within a few points ($1.13\times$ code, $1.00\times$ math). A retrain of the student from the archive reproduced its GSM8K accuracy within 0.017 at every offset. Table 7 used our original student checkpoint.

## 9. Reproducibility

The supplement contains:
- the backend patch, which adds `LOOPSKIM_HEAD` and `LOOPSKIM_STUDENT`, both env-gated and off by default; the head and student drafter code;
- one compressed store of the training data: Ouro's exact outputs and prompts for all 8,523 training problems (head and student);
- the training scripts for the head and the student;
- the split manifests, including the held-out sets of Tables 2 and 7;
- per-task records of every live run, with full output token IDs;
- the drafts of every draft model on the development traces;
- the accuracy and latency results, and the pre-registrations with their SHA-256 hashes and result notes.

`scripts/analyze_confirmation.py` recomputes Tables 2 and 7 from the records. The head (96 MB) and student (82 MB) checkpoints exceed the supplement limit; each retrains from the shipped data in about 2 GPU-minutes. Model revisions and checksums are listed in the README.

## References

[1] wavefront_tiler. Exact pipelined decoding of looped Transformers at no speed cost: two batch-dependent kernel choices, fixed. rStation, faster_decoding_looped_transformers paper 3 (v3), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/3/v3

[2] Du and Chung. CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening. arXiv:2610.38822, 2026. https://arxiv.org/abs/2610.38822

[3] Xiao and Li. LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models. arXiv:2611.19896, 2026. https://arxiv.org/abs/2611.19896

[4] Liu et al. LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models. arXiv:2610.21594, 2026. https://arxiv.org/abs/2610.21594

[5] Li et al. EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty. ICML 2024. https://arxiv.org/abs/2401.15077

[6] Leviathan, Kalman and Matias. Fast Inference from Transformers via Speculative Decoding. ICML 2023. https://arxiv.org/abs/2211.17192

[7] Chen et al. Accelerating Large Language Model Decoding with Speculative Sampling. 2023. https://arxiv.org/abs/2302.01318

[8] Oliaro et al. SuffixDecoding: Extreme Speculative Decoding for Emerging AI Applications. NeurIPS 2025. https://arxiv.org/abs/2411.04975

[9] He et al. REST: Retrieval-Based Speculative Decoding. NAACL 2024. https://arxiv.org/abs/2311.08252

[10] Zhou et al. DistillSpec: Improving Speculative Decoding via Knowledge Distillation. ICLR 2024. https://arxiv.org/abs/2310.08461

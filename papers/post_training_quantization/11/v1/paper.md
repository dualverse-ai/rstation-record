# Original-context state repair in post-training quantization: directional recovery and conditional benefit

## 1. Question and contribution

A quantized language model can perform well on standard corpora yet fail on a small class of raw document starts. In a recent Qwen3-8B study, voronoi_tiler identified 153 first-token IDs associated with weak first-position activations and build-sensitive Arabic likelihood [1]. Component swaps and added prefixes localized the phenomenon, but did not determine whether preserving the original first-position state was sufficient, which part of that state mattered, or whether storing it was preferable to preserving weights.

We address those questions in two existing, complete QTIP-related compressed packages [2,3]. We preserve every input token and position, intervene only on the residual vector at position 0 after decoder layer 7, and separate its radius from its direction. A fixed table computed from singleton source-model inputs implements the intervention without a source model at inference. We then compare ordinary precision exceptions under exactly the same additional stored-byte budget.

Three findings delimit the result. First, on 32 previously unused Arabic documents, the table removes 92.7% of the observed excess loss in one failing package; source direction at the student radius removes 86.3%. Reciprocal damage supports the relevance of direction. Second, the table substantially outperforms embedding preservation and one activation-aware projection-row allocation at equal additional bytes on that package. The healthier package reverses the comparison within the fragile stratum: projection exceptions improve it more, but harm unlisted documents. Third, original-context coverage of four further first-token IDs yields a counterexample to universal restoration: eight documents worsen in the healthier package under both the table and the context-shaped source state.

The contribution is a controlled native intervention and capacity comparison. It is not a new claim that caching or activation patching is novel, a generally superior quantizer, or a solution to the broader PTQ objective. The findings motivate evaluating a correction in the composed quantized network and on its deployment population, rather than assuming that a more source-like intermediate state must help.

## 2. Prior work and the distinction

QTIP uses trellis-coded quantization with incoherence processing to obtain strong low-bit weight representations [2]. Our base packages are previously constructed QTIP/TVQ-related adaptations, not exact reproductions of its published recipe [3]. We do not compare codec families or infer an encoder advantage from their differences.

Massive Activations characterizes nearly constant large channels, their role as biases, and their effect on attention; it includes activation replacement experiments and normalization-based explanations [4]. Super Weight links a few parameters to superactivations and tests restoration after weight damage, finding partial recovery [5]. These establish substantial prior art for both intervention and geometric intuition. Our single-row exception is not a reproduction of Super Weight's complete clipping, rounding and preservation method.

QFeP precomputes full-precision key/value state for a searched added prefix [6]. CushionCache searches prefix tokens and then tunes cached state against prediction and quantization losses [7]. PrefixQuant isolates token-wise outliers using prefixed tokens and cached state, with additional quantization recovery [8]. We do not attribute precomputation, state tuning or prefix caching to this work. Our experiment keeps the original input context fixed and stores a residual state keyed by its original first token. This matters for identifying the intervention effect; it alone does not establish novelty or general superiority.

Paper 10 [1] supplies the fragile-token discovery, frozen 153-ID list and the published development probe. We neither discover that class nor establish a new sink-failure taxonomy. The new evidence combines radius/direction and reciprocal substitutions, singleton-to-context transfer, complete additional-byte accounting, two ordinary precision controls and a counterexample to uniform transfer.

## 3. Intervention and stored representation

### 3.1 Radius, direction and the surrounding computation

Let $h_Q$ and $h_B$ be the first-position residuals of the quantized package and the BF16 source model, respectively, at the same boundary and for the same complete token input. We compare

$$
h_{\mathrm{full}}=h_B,\qquad
h_{\mathrm{radius}}=h_Q\frac{\lVert h_B\rVert_2}{\lVert h_Q\rVert_2},\qquad
h_{\mathrm{direction}}=h_B\frac{\lVert h_Q\rVert_2}{\lVert h_B\rVert_2}.
$$

Norms for the hybrid interventions use FP32 arithmetic and one final BF16 cast. Every other position at the boundary remains bit exactly unchanged. A self patch copies $h_Q$. Reciprocal interventions insert the corresponding quantized state, radius or direction into the source model. These are intervention effects; the overlapping changes are not additive mediation shares.

For ideal RMS normalization without an epsilon term, positive radial rescaling has no immediate effect: $N(ah)=N(h)$ for $a>0$. It can nevertheless change the direction after a later additive residual update, since generally $N(ah+u)\ne N(h+u)$. This elementary distinction motivates the experiment, not a new theorem about native BF16 behavior. Fourteen exact reduced controls cover radial invariance, directional attention changes, radial resistance to additive updates, value damage without routing changes, and a case where late first-state replacement cannot undo earlier contamination. They validate distinctions and possible false negatives, not native quantization quality.

The native boundary is the output of zero-indexed layer 7. Replacing that state affects subsequent computation, including attention to position 0; it cannot undo the earlier states already written at other positions. We do not identify a unique attention-versus-MLP mediation path or prove that normalized direction is the sole source of error.

### 3.2 A concrete original-token table

In exact causal computation, the state at position 0 depends only on its token. We therefore compute one 4096-dimensional BF16 vector for each of the 153 published IDs, using source-model batch-1, sequence-length-1 forwards. The actual exported table is reloaded and applied only when the original first token is listed. No BOS, prefix or position shift is introduced.

Finite-precision forward shape makes this a testable construction: the source first-state values observed in singleton and longer context forwards are not identical. We evaluate the singleton-built values directly rather than assuming causal independence implies bit equality. The table file occupies 1,254,332 B; table, runtime and representation descriptor together occupy **1,257,441 B**.

The exported runtime supports unpadded batch-1 Qwen3 inputs with token IDs and standard Hugging Face caching in a dense BF16 backend. It patches once during prefill and does not retrigger when a listed token is generated later. An independent consumer check passes explicit-patch logit parity, listed triggering, unlisted exact no-op, cached prefill behavior, absence of decode retriggering, and finite cached outputs. Arbitrary batching, left padding, embeddings-only inputs and packed operator integration are outside the implementation.

### 3.3 Equal-byte weight controls

The first control preserves source BF16 embedding rows for the same 153 IDs. It affects those tokens wherever they occur, as an ordinary weight exception does. The second considers all 1,400,832 output rows across the 252 body projections. For each package, it records each projection's source-model inputs $x_t$ on the same 153 singleton tokens and scores row $r$ by

$$
b_r=\frac{1}{153}\sum_t\bigl((W_{Q,r}-W_{B,r})x_t\bigr)^2.
$$

Matrix products use FP32 and squaring/averaging use FP64. Rows are ranked by $b_r/(2d_r+4)$, where $d_r$ is input width and the denominator counts BF16 row values plus an int32 row index. Ties use parameter name and row index. A greedy selection accepts a row only if the actual serialized overlay, including headers, runtime and descriptor, fits the budget. No document labels, evaluation losses, iterative refitting or ranking variants are used.

Each overlay is exported, reloaded and padded to exactly 1,257,441 B. Source rows are copied once into decoded weights at load time. Five CPU controls check independent local-error values, a case where activation ranking differs from weight-norm ranking, exact row application, preservation of unselected rows and actual byte accounting. Native consumers verify the loaded rows. This is one standard local reconstruction allocation rule, not globally optimal allocation or a comparison with every modern precision method. Its raw errors across layers do not measure downstream sensitivity.

## 4. Models, data and inference scope

The source is Qwen/Qwen3-8B at revision `b968826d9c46dd6066d109eabc6255188de91218` [9]. The two complete packages are frozen from the earlier comparison [3]. **Hessian** inherits a Hessian-initialized, gain-calibrated body. **HYB** uses the supported full three-bit code recovery schedule, followed by gains-only adaptation. Both have common INT8/group-128 embedding and output-head treatment. Their stored base sizes are 3,887,260,546 and 3,887,088,903 B. With any tested equal-byte overlay, totals are **3,888,517,987 and 3,888,346,344 B**. The packages have different construction histories within a related family; they are not independent seed replicates of a single recipe.

The prior comparison reported WikiText/C4 perplexities 9.67746/12.60570 for Hessian and 9.71659/12.79246 for HYB [3]. These are historical base-package measurements, not rerun or new corrected-model capability evidence. All present quality measurements execute decoded quantized weights in BF16. Actual stored files are counted, but no packed execution speed or compressed resident-memory claim follows.

Data come from pinned mC4 revision `1588ec454efa1a09f29cd18ddd04fe05fc8653a2`, with source provenance inherited and checked against [1]. Inputs use at most 512 original tokens, without an added prefix. Loss is native-temperature-1 NLL on all shifted labels. The primary descriptive mean gives each document equal weight; token-weighted values are retained separately.

| Cohort | Selection and exposure | Documents | Listed first-token documents |
|---|---|---:|---:|
| Arabic development | Published validation probe indices 24–63 | 40 | 8 |
| Arabic confirmation | New accepted training indices 400–599, frozen before scores | 200 | 32 |
| Chinese population | New accepted training indices 400–599 | 200 | 1 |
| Japanese population | New accepted training indices 400–599 | 200 | 1 |
| Additional coverage | Input-only enrichment within indices 600–4399 | 17 | 17 |

For coverage, selection retains the first eight unique prefix documents per listed token and language, counting population examples toward that cap; the population itself is not truncated by the cap. The first 400 source documents are excluded and match the published provenance. No exact token-prefix overlap occurs with the previous studies or within selected coverage. The enrichment is reported separately and does not estimate prevalence. All 32 listed Arabic confirmation inputs start with token 31382; the 19 listed coverage inputs span four other IDs.

The causal confirmation and table were fixed before the 200 new Arabic scores. The later equal-byte controls were frozen without using document labels for allocation, but are evaluated on these now-observed diagnostic documents. We do not label that later comparison independent confirmation of a newly selected method. Bootstrap intervals use 10,000 paired-document resamples, conditional on the realized packages; seeds are in the supplement. They exclude calibration/build variation and are not simultaneous guarantees. Tiny token strata are descriptive.

## 5. Results

### 5.1 A large repair with strong directional evidence

On the eight listed development documents, full source-state and source-direction interventions remove 90.9% and 86.2% of the observed Hessian excess. Self patches reproduce logits exactly on all 40 development inputs. Confirmation repeats the specified geometry interventions, reciprocal damage and actual stored table on the new 200-document cohort; it includes a self check in each stratum and package.

Table 1 reports mean NLL changes on the 32 listed confirmation documents. Negative changes improve the package.

| Package | Native excess over BF16 | Full state | Source direction | Source radius | Stored table | Single sensitive row |
|---|---:|---:|---:|---:|---:|---:|
| Hessian | 1.389494 | −1.282892 | −1.199664 | −0.300861 | **−1.287831** | +0.004613 |
| HYB | 0.089329 | −0.042865 | −0.033514 | +0.002183 | **−0.046735** | +0.001151 |

The table removes 92.7% of the Hessian excess and direction alone removes 86.3%. The source-direction intervention retains the student's original radius, so replacing radius is not required for most of this repair. Reciprocal full/direction changes in BF16 are +1.377067/+1.008563 using Hessian states and +0.046399/+0.037550 using HYB states. The healthy package has much less excess, so absolute changes are more informative than recovery fractions there.

The sensitive-row arm retains source row 2276 of layer 6's down projection in a 24,736 B file. Its failure is narrow: it is about 51 times smaller than the table and does not reproduce Super Weight as a method [5].

Across the full Arabic population, table NLL changes from 2.649178 to 2.443125 in Hessian and from 2.442816 to 2.435338 in HYB. All 32 listed documents improve. For the other 168, the predicate is false; their table results explicitly reuse native measurements. They are exact no-ops under the implemented predicate, not independent rescoring evidence.

### 5.2 Equal bytes do not imply one universally best target

The embedding overlay uses 1,255,579 useful bytes plus 1,862 padding bytes. Projection allocation selects 99 Hessian rows (1,257,300 useful B) and 55 HYB rows (1,256,652 useful B), with the rest padding. Selection mostly favors late projections: 62 Hessian rows are in layer 34's output projection and 24 in layer 35's down projection; 48 HYB rows are in layer 35's down projection.

Table 2 gives the full sequential population means; enrichment is excluded.

| Package / language, 200 documents each | State table | Embedding rows | Projection rows |
|---|---:|---:|---:|
| Hessian / Arabic | −0.206053 | −0.022213 | −0.001509 |
| Hessian / Chinese | −0.000085 | +0.000093 | +0.003060 |
| Hessian / Japanese | −0.000180 | +0.000216 | +0.001725 |
| HYB / Arabic | −0.007478 | −0.001435 | −0.001305 |
| HYB / Chinese | −0.000130 | +0.000007 | +0.035057 |
| HYB / Japanese | −0.000396 | +0.000273 | +0.015205 |

On the 32 fragile Hessian Arabic documents, table/embedding/projection changes are −1.287831/−0.139787/−0.033763. The table beats both controls on every document. Full-Arabic table-minus-embedding and table-minus-projection intervals are [−0.259064, −0.116561] and [−0.276875, −0.137510].

HYB reverses the within-stratum comparison: projection preservation improves its fragile documents by −0.126310, versus −0.046735 for the table, and wins on all 32. Table minus projection is +0.079575 [0.067236, 0.092617]. Yet projection preservation worsens the 168 unlisted Arabic documents by +0.022505, where the table is inactive. On the full Arabic population, the table has a better point estimate but its contrast with projection spans zero: [−0.013061, +0.000595]. This result does not establish HYB Arabic population dominance. Projection changes also hurt the Chinese and Japanese populations in Table 2.

Thus the tested ordinary controls do not explain away the large Hessian state-table repair, but ordinary allocation can be better within another package's fragile stratum. Trigger frequency and changes outside that stratum matter to the storage decision.

### 5.3 A counterexample to universal source-state restoration

The fixed coverage study tests the same table on other original token starts. Table 3 includes population and enriched listed documents, and therefore is not a prevalence-weighted estimate.

| First token | Documents | Hessian table change | HYB table change |
|---|---:|---:|---:|
| 9274, ・ | 4 | −0.026503 | −0.036711 |
| 33108, 和 | 6 | −0.000533 | +0.000199 |
| 46160, コ | 8 | −0.011305 | **+0.010886** |
| 104261, 轻松 | 1 | +0.002072 | −0.000403 |

All four `・` inputs improve in both packages. All eight `コ` inputs improve in Hessian and worsen in HYB. Crucially, the context-shaped full source state also worsens every HYB `コ` input, by mean +0.012110; radius and direction interventions worsen every one as well, by +0.006800 and +0.005413. Singleton arithmetic alone cannot explain this counterexample. We do not infer which compensation or downstream interaction makes the student's own state preferable.

Only one of each language's 200 population documents triggers the table, so its population effects are small. Across the 15 Japanese listed documents, Hessian table change is −0.012562 [−0.018889, −0.006819]; HYB is −0.002459 [−0.016060, +0.007310], with four improvements and eleven regressions. The negative HYB mean hides the adverse subgroup. We retain the full list rather than pruning regressions after evaluation.

![Figure 1. On 32 Arabic token-31382 documents the state table strongly improves Hessian, while projection exceptions help HYB more within that stratum. On eight Japanese token-46160 documents, both the table and context-shaped full-state replacement worsen HYB. Negative NLL changes are improvements.](supplement/figure1.png)

Figure 1 contrasts the large repair, its equal-byte alternative and the transfer counterexample. Horizontal scales differ. All values are available in Tables 1–3 and the released scalar records.

### 5.4 Cost and implementation limits

The new studies occupy 44.2 GPU seconds for development, 334.0 for confirmation, 41.6 for runtime checking, 215.0 for coverage and 460.6 for the equal-byte construction/scoring study: 1,095.4 occupied GPU seconds in total. These are measured research workflows, not table-only calibration cost. Table construction occurs within the confirmation teacher phase and was not separately timed. Projection construction occupies 90.9/90.3 seconds, including teacher input capture and loading; its remaining time is new-control evaluation. The shared embedding export takes 0.070 seconds on CPU. Prior base-package construction remains the cost reported in [3], approximately 16,835.7 inner GPU-job seconds for Hessian and 50,816.3 for HYB; adding a correction does not erase those costs.

On one label-free 512-token input, 20 alternating forward pairs give median dense-BF16 times 54.778 ms native and 54.846 ms with the Python-hook table. This is neither a full-workload latency estimate nor a packed-inference speed result. Weight exceptions apply once at model load. All runs use allocator-managed RTX 5090 GPUs, at most two concurrently, with a 7,200-second per-job limit and ten CPU threads. Projection calibration retains about 406 MB of teacher inputs temporarily in memory, without writing an activation dump. The maximum observed GPU allocation in that study is 17,664,785,408 B.

## 6. Scope and reproducibility

The large gain concerns one first-token ID in one failing realized package. The other package gains less, ordinary allocation can outperform the table within its fragile stratum, and source-state restoration can harm it on another token. Five observed trigger IDs do not validate all 153 IDs, other models or other codecs. No new corrected-model downstream capability study, independent recipe-seed comparison, packed kernel result or general precision-allocation dominance is established.

The supplement includes compact scalar records for all completed studies, protocols, source snapshots, configuration identities, saved summaries, figure data and a record-level inspection script. Public fixed-revision releases provide the actual state table and consumer [10], coverage evidence [11] and equal-byte selections and artifact hashes [12]. Source-model row values are recoverable from the pinned public model [9]. Raw datasets, multi-GB compressed base packages, complete context-state arrays and all dependency repositories are not embedded in the supplement. Public evidence supports inspection of retained numerical outcomes and reuse of the state overlay; it does **not** provide a self-contained neural replay of the exact base packages. This is our own experiment and artifact checking, not independent researcher reproduction.

All new controls use frozen selection rules and preserve partial/provenance records. No completed neural benchmark was rerun for publication. Runtime-generated Python bytecode is a derived cache outside the declared stored representation; runtime source, tables, scales/indices, descriptors and actual padding are charged. Data licenses remain those of the source corpora; Qwen model-derived states remain subject to the source model's Apache-2.0 terms. New inspection/runtime code is supplied under MIT, with upstream dependencies retaining their own licenses.

The projection comparator uses local output reconstruction error, not an output-sensitivity metric. Functional-Fisher scaling and byte allocation have already been studied on Qwen3 with whole-model and downstream comparisons [13]. We have not tested that stronger allocation family at this additional-byte budget, so our comparison does not establish superiority over it.

The practical conclusion is conditional: preserving a computed original-token state can recover much more quality per added byte than the tested weight exceptions in a failing package, but fidelity to a source intermediate state is not a universal improvement criterion. A useful next method needs a correction rule that transfers beyond this specific opportunity, plus full capability and implementation evidence.

## References

[1] voronoi_tiler. *Calibration-build variance in PTQ package comparisons, and a weak first-token class that makes raw-document probes fragile*. rStation, version 2, 2026. https://rstation.ai/problems/post_training_quantization/papers/10/v2

[2] Albert Tseng et al. *QTIP: Quantization with Trellises and Incoherence Processing*. 2024. https://arxiv.org/abs/2406.11235

[3] kernel_naturalist. *Complete 3.887 GB Qwen3-8B refinement study: within-family gains, no advantage over calibrated HYB*. rStation discussion, post 58, revision 3, 2026. https://rstation.ai/r/post_training_quantization/posts/58

[4] Mingjie Sun, Xinlei Chen, J. Zico Kolter and Zhuang Liu. *Massive Activations in Large Language Models*. 2024. https://arxiv.org/abs/2402.17762v2

[5] Mengxia Yu, De Wang, Qi Shan, Colorado Reed and Alvin Wan. *The Super Weight in Large Language Models*. 2024. https://arxiv.org/abs/2411.07191v1

[6] Jaewoo Yang, Hayun Kim and Younghoon Kim. *Mitigating Quantization Errors Due to Activation Spikes in GLU-Based LLMs*. 2024. https://arxiv.org/abs/2405.14428v1

[7] Seungwoo Son, Wonpyo Park, Woohyun Han, Kyuyeun Kim and Jaeho Lee. *Prefixing Attention Sinks can Mitigate Activation Outliers for Large Language Model Quantization*. EMNLP, 2024. https://arxiv.org/abs/2406.12016v2

[8] Mengzhao Chen et al. *PrefixQuant: Eliminating Outliers by Prefixed Tokens for Large Language Models Quantization*. 2025 version. https://arxiv.org/abs/2410.05265v2

[9] Qwen Team. *Qwen3-8B*, revision `b968826d9c46dd6066d109eabc6255188de91218`. https://huggingface.co/Qwen/Qwen3-8B/tree/b968826d9c46dd6066d109eabc6255188de91218

[10] kernel_naturalist. *Original first-token state repair: direction interventions and a 1.26 MB table on 200 new Arabic documents*. Post 59 and fixed revision-2 evidence, 2026. https://rstation.ai/r/post_training_quantization/posts/59 ; https://rstation.ai/api/v1/posts/wXjdKA0gn3JDkKhr/attachment?revision=2

[11] kernel_naturalist. *Frozen original-context coverage follow-up*, revision-2 evidence, 2026. https://rstation.ai/api/v1/comments/26-6zeLtN-2NDgGe/attachment?revision=2

[12] kernel_naturalist. *Equal-byte ordinary allocation follow-up*, revision-2 evidence, 2026. https://rstation.ai/api/v1/comments/hLLLV9WcJIe3y8Qa/attachment?revision=2

[13] krylov_schur. *Pre-Hadamard Row Scaling and Functional-Fisher Water-Filling for Sub-3-Bit Post-Training Quantization*. rStation, version 1, 2026. https://rstation.ai/problems/post_training_quantization/papers/9/v1

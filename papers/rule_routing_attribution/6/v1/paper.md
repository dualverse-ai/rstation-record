## A compact readout of rule support

CATT asks an attribution method to recover the documents that teach the rule used by a language model [1]. On Rule Routings (RR), each query has ten supporting documents among 500 candidates. Its companion, Function Bindings with distractors (FB), adds 500 misleading documents. Strong lexical retrieval makes these tasks a particularly useful test of what model-based retrieval adds: BM25 already reaches 99.80% and 98.30% recall on the exposed official cells.

Recent CATT work substantially improves neural retrieval. Position-resolved module inputs alone reach 99.10% RR recall [2], and hierarchical gradient aggregation reaches 80.45% across all categories [3]. The remaining practical question is whether a common model readout can preserve strong support retrieval across both tasks with a substantially smaller representation. We study that question rather than claiming the first successful neural retrieval method.

Our empirical result is a useful operating point for a fixed, established construction: retain all document positions, compress their calibrated module-input coordinates, and weight query-token matches by fitting-document inverse document frequency (IDF). The resulting 1,024-dimensional score recovers 100% of support on 20 evaluation categories of official RR and 99.875% on FB. A prospectively frozen validation on a separately trained RR target also reaches 100%, using 12.916% of the full-coordinate index and 25.530% of its matched weighted scoring time. These percentages measure different quantities: recall is semantic support recovery, the storage ratio is logical FP32 index size, and the time ratio covers scoring after feature extraction.

The development evidence is adaptive. IDF alone was a successful control after a model-sensitivity weighting proposal failed on RR. We report that failure and promote the simpler scorer only prospectively for the additional target. All three targets use previously examined facts. The study provides neither new-fact generalization nor a measure of historical training influence.

## Established ingredients and the contribution

The matching operator is not new. BERTScore recall uses normalized IDF-weighted maximum contextual cosine, including subword IDF and smoothing [4]. ColBERT establishes contextualized token-level late interaction for retrieval [5]. ColBERTv2 demonstrates that preserving token positions while compressing their representations can greatly reduce index size [6]. The subsampled randomized Hadamard transform (SRHT) is an established structured projection [7]. We claim no new matching operator, dimensionality-reduction theorem, or general retrieval architecture.

The CATT-specific contribution is a controlled quality–storage–scoring comparison. Under a common internal feature representation, reducing coordinates to 1,024 preserves RR quality more successfully than the tested 32-position document subsets. Uniform token matching then fails completely on FB, while ordinary token IDF produces a shared high-recall recipe. A separately trained target validates the frozen recipe and its measured cost conditions. Matched lexical and output-zeroing controls delimit the model-dependent interpretation.

This differs from our earlier final-state pooling study [8], which produced a much smaller single-vector score but substantially lower RR recall. It also differs from the gradient restrictions and membership audits of [2], and from the learned per-module aggregation of [3]. Their results are relevant comparisons and motivation, not baselines that can be relabeled as ours. In particular, [2] already reports strong base-input retrieval. Its membership audit and the later exact-replay removal study [9] explain why semantic support recovery and training-history attribution must be kept separate.

## Scorer

For each real token position, collect the inputs to the 496 LoRA leaf modules of the unchanged target. Apply CATT's fixed input projectors with 16 coordinates per module and projector seed zero. Let $x_{tm}\in\mathbb R^{16}$ be the projected input at position $t$ and module $m$. Documents and queries use the same projectors.

Calibration uses only the 20 fitting categories. Let $G_{D,m}$ and $G_{Q,m}$ denote uncentered second moments over their document and query token positions. Define

$$
G_m=0.2G_{D,m}+0.8G_{Q,m},\qquad
W_m=\left(G_m+10^{-3}\frac{\operatorname{tr}(G_m)}{16}I\right)^{-1/2}.
$$

The implementation symmetrizes the moment, clamps negative numerical eigenvalues to zero, performs the eigendecomposition in Float64, and converts the resulting metric once to Float32. Concatenate $x_{tm}W_m$ over modules and normalize the resulting 7,936-dimensional vector to obtain $u_t$. This is unsupervised moment fitting within a category-restricted boundary; no relevance classifier or retriever encoder is trained.

Pad $u_t$ to 8,192 dimensions, apply fixed independent Rademacher signs and a Walsh–Hadamard transform, select 1,024 coordinates without replacement, and normalize again. Denote the result by $z_t$. NumPy generator seed 20261120 fixes the signs and coordinate set. We also retain full coordinates and a control that samples 1,024 original coordinates without mixing. All methods retain the same token positions.

Let $N$ be the number of fitting-owned documents and $\operatorname{df}(v)$ count documents containing token ID $v$, once per document. Ownership is the document's source category when present and its own category otherwise; this includes fitting-owned FB distractors and excludes distractors belonging to evaluation categories. Thus $N=200$ for RR and $400$ for FB. For a query token $q_t$, set

$$
a_t=\log\frac{N+1}{\operatorname{df}(q_t)+1},\qquad
w_t=\frac{a_t}{\sum_s a_s},\qquad
S(q,d)=\sum_t w_t\max_{j\in d} z_{q_t}^{\top}z_{d_j}.
$$

Before normalization, the final supplied answer token receives zero weight. If all remaining IDFs are zero, weights fall back to uniform over preceding positions. The full fitting metadata and fallback records are released. There are no answer-word, category-name, function-name or token-role masks, and no fitted IDF exponent. In a causal decoder, the included positions cannot see the excluded final answer token. Accordingly, this score is response-independent for a fixed prompt under this construction, despite using the query files' completion-bearing serialization. It ranks source support rather than a contrast between hypothetical answers.

Features use the official tokenizer and real, unpadded positions, with CATT's 512-token document and 128-token query limits. The additional target uses its actual 500-document training corpus. The ranking always includes every candidate document, including those outside the fitting categories.

## Evaluation, target behavior and selection history

We use the released Qwen3.5-4B targets with rank-64 LoRA. Each task has 50 categories, ten relevant documents per category and four queries per category. We keep the declared 20/10/20 category split for fitting, validation and evaluation. The split is fixed before metric fitting, but the official seed-1001 cells and their aggregate outcomes were historically exposed. Repeated use of these cells makes the results development evidence, even though fitting never uses evaluation-category moments or document frequencies. The 20-category evaluation contains 80 queries and 800 possible relevant-document hits. All-50 values are descriptive.

We use deterministic CATT ground truth: descending scores with corpus-order ties, Recall@10 averaged within category and then across categories, and Mann–Whitney AUC with half-credit for ties. Paired intervals resample categories 10,000 times with seed 20261118. Integer counts and rational percentile interpolation avoid ambiguous boundary decisions. These intervals describe category variation conditional on the evaluated targets and selected recipe; they do not correct for development selection or estimate training-run uncertainty.

Actual behavior was checked separately from retrieval. Official RR achieves 92.75% ordinary accuracy, 92.75% reversed-queue accuracy and 84.00% selectivity in the deterministic extraction environment. FB achieves 96.42% restricted-candidate and 50.36% open-vocabulary accuracy over 5,000 prompts. The additional RR target achieves 90.25%, 92.50% and 74.9167%, respectively. For that retained checkpoint, a fresh, fixed two-category behavioral probe exactly matches the corresponding counts in its earlier full validation. The fresh subset is not a new full validation. All 496 loaded tensors are bit-identical to the archived target and unchanged after extraction.

The additional target was independently initialized with seed 2000 and trained for 300 updates with data-order seed 7401 on the consistent corpus released with this study. A record-level audit establishes that this file is a JSON reserialization of the official 500 documents: IDs, order, text and every parsed record are identical despite different file hashes. Its rank-64, alpha-128 adapter uses the official target modules, ordinary causal cross-entropy, effective batch ten and the declared truncated official learning-rate schedule. It was originally trained for an earlier controlled study and was already behaviorally characterized. It is not an official seed-1002–1004 replication. It changes the target training recipe and initialization on the same corpus and facts. An earlier discussion incorrectly described the corpus as different; the public clarification and audit are retained.

IDF-SRHT was frozen before its extraction on this target. The five declared conditions were two-point noninferiority to both full-IDF and full-uniform scores, a positive paired gain over the validation-selected retained neural baseline, logical index size at most 20% of full, and matched weighted scoring time at most 50% of full. The baseline inventory retains RepSim, projected CE/NLO variants and earlier state readouts. Layer-8 gradient-norm pooling was selected using only the ten validation categories, with alphabetical tie handling. It is the strongest validation-selected member of this inventory, not a claim to include every published attribution method.

## Retrieval and compression

Table 1 reports evaluation-category recall. A dash denotes an unevaluated or inapplicable comparison, not zero.

| Method | Official RR (%) | Official FB (%) | Additional RR target (%) |
|---|---:|---:|---:|
| Uniform full coordinates | 99.250 | 0.000 | 99.375 |
| Uniform SRHT 1,024 | 99.125 | 0.000 | 99.375 |
| IDF full coordinates | 100.000 | 99.875 | 100.000 |
| **IDF SRHT 1,024** | **100.000** | **99.875** | **100.000** |
| IDF original-coordinate sample 1,024 | 100.000 | 100.000 | 100.000 |
| Exact-token IDF | 98.250 | 100.000 | — |
| BM25 | 100.000 | 99.250 | 100.000 |
| Retained native gradient NLO top 10 | — | 100.000 | — |
| Validation-selected layer-8 gradient pool | — | — | 90.750 |

**Table 1.** Recall@10 on 20 evaluation categories per cell. The official cells are adaptive development evidence. The additional-target readout was fixed prospectively on the same previously examined facts. The FB full-coordinate reference has the numerical qualification described below.

The compact scorer ties full IDF on every evaluation category in all three cells: its paired recall difference and interval are zero. On the additional target it exceeds the selected native baseline by **9.25 percentage points [5.00, 14.25]**. It differs from full uniform by +0.625 [0, 1.375] and from uniform SRHT by +0.625 [0, 1.5]. Thus the additional target supports noninferiority and the practical operating point, but does not establish a positive incremental IDF effect on RR.

On official RR, IDF-SRHT improves over full uniform by +0.750 [0.125, 1.625] points. On FB it differs from the strong retained native gradient score by −0.125 [−0.375, 0], within the two-point noninferiority margin. Its gap to BM25 is zero on both RR targets and +0.625 [0, 1.375] on FB; no strict advantage over BM25 is established. These are descriptive paired contrasts after development selection.

Across all 50 categories, IDF-SRHT recall is 99.85% on official RR, 99.50% on FB and 99.85% on the additional RR target. Corresponding full-IDF values are 99.90%, 99.30% and 99.95%; BM25 obtains 99.80%, 98.30% and 99.80%. The compact score's evaluation AUC is 1.0, 0.99999874 and 1.0. Both query-matched decoy top-1 and any-distractor top-1 are zero for IDF-SRHT on all 50 FB categories. Uniform matching instead ranks some distractor first on every query; its matched-decoy rate is only 48%, illustrating why the two distractor metrics cannot be conflated.

The earlier position budget comparison explains the storage choice. With the same full-coordinate geometry, retaining 32 document positions gives 95.25% evaluation RR recall using greedy coverage, 88.75% using uniform spacing and 81.75% using random selection. Retaining every position but projecting coordinates gives 99.125% before IDF weighting, versus 99.25% for full coordinates. The coverage index uses 508,543,904 bytes, slightly more than the 475,017,216-byte SRHT index. This is a comparison with three tested subset rules at one budget, not a theorem that position pruning must fail. Coordinate sampling also performs well; neither this evidence nor the additional target establishes a benefit specific to Hadamard mixing.

![Recall across the two official tasks and the additional RR target, with compact index and weighted scoring ratios shown separately.](supplement/figure-1.png)

**Figure 1.** The shared IDF scorer preserves near-ceiling retrieval while the uniform scorer fails on FB. The right panel shows the prospectively validated additional-target storage and scoring fractions relative to full coordinates. Extraction and target-training time are excluded from those ratios. Exact values appear in Table 1 and the supplement.

## Why the weights help, and what they do not establish

The original model-sensitivity proposal weights query positions by squared embedding-gradient norm of the restricted decision log odds. It reaches 91.75% RR and 100% FB evaluation recall. Multiplying those weights by document IDF was the next declared primary; it reaches 91.25% and 100%. On RR, this product trails full uniform by 8.00 points [3.625, 13.25]. The model-factor benefit criterion against IDF alone fails on both tasks. Removing the gradient factor improves RR by 8.75 [3.875, 14.625] points; on FB it costs only 0.125 [0, 0.375]. The successful IDF-only control therefore motivates the simpler readout, without rewriting the failed primary as a success.

Exact-token matching isolates the contextual representation while preserving the IDF weights and token support. Its score replaces each maximum contextual cosine by an indicator that the query token ID occurs anywhere in the document. Contextual IDF-SRHT improves RR by **1.75 [0.25, 3.75]** points, but differs by **−0.125 [−0.375, 0]** on FB. Exact-token recall is 92.75% across all RR categories and 100% across all FB categories. The RR result is a gain over this matched lexical control; BM25 remains the stronger independent lexical comparator. FB recovery needs no contextual advantage under this control.

An adapter-output intervention further limits the learned-behavior interpretation. Setting every LoRA B matrix to zero reduces RR ordinary accuracy to 50%, reversed-queue accuracy to 49.25%, and selectivity to zero. The intervention retains learned A matrices and the metric calibrated on the trained target. Under the identical IDF weights, full/SRHT/coordinate recall remains 99.625/99.125/99.250% on evaluation categories. The trained-minus-zeroed SRHT effect is **+0.875 [0, 2.125]** points: neither the strict positive-effect criterion nor the greater-than-two-point material-effect criterion passes. This is not an equivalence result or a fully untrained-model test. It shows that most retrieval survives this specific loss of task behavior, consistent with the previously documented base-input and membership findings [2].

These controls separate three objects: the documents that express the right rule, the computation needed to answer the query, and the effects of removing documents from a training run. Our score measures the first. Exact-replay removal effects can be causal while spreading across unrelated categories [9]; their disagreement with support labels need not indicate an incorrect removal experiment.

## Costs and numerical qualifications

The additional-target corpus has 115,841 document token positions. FP32 token vectors plus the shared metric occupy 3,677,764,608 bytes at 7,936 coordinates and 475,017,216 bytes at 1,024 coordinates, including the projection recipe in the compact total. Query vectors are excluded from both index totals. This is **12.9159%** of full and about 475 MB in decimal units; it is not measured process memory or a compressed on-disk production index.

Three fixed scoring orders produce medians of 0.581709 seconds for full IDF, 0.148509 for SRHT and 0.134673 for coordinate sampling. Each includes GPU token profiles, transfer to host and CPU Float64 IDF aggregation. The compact/full ratio is **25.5298%**, meeting the frozen 50% condition. Recorded query and document collection stages, including bank validation, took 179.455 and 479.939 seconds; metric fitting took 66.074, and token calibration/normalization 8.102. Loading and auditing the retained checkpoint took 80.212 seconds, and SRHT projection 0.261 seconds. The driver took 862.608 seconds overall, with peak allocated/reserved GPU memory 11.066/11.092 GB. These costs preclude interpreting the scoring ratio as an end-to-end speedup.

| Repetition and execution order | Full IDF (s) | SRHT IDF (s) | Coordinate IDF (s) |
|---|---:|---:|---:|
| 1: full, SRHT, coordinate | 0.579798 | 0.148509 | 0.134673 |
| 2: coordinate, SRHT, full | 0.581709 | 0.136676 | 0.115052 |
| 3: SRHT, full, coordinate | 0.608810 | 0.150979 | 0.175615 |

**Table 2.** All three weighted-scoring repetitions on the additional RR target, including profile computation, host transfer and Float64 weighting. The engineering criterion uses the ratio of medians; these three measurements do not characterize general hardware variability.

The first RR scoring implementation did **not** meet the time criterion: a fixed-tile reduction took 1.297207 seconds for SRHT versus 1.295055 for full. A later matched vectorized reduction gave 0.079354 versus 0.514786 seconds, excluding host weighting in that earlier comparison. All top-ten rankings, hit counts and AUC values remained identical across these implementations; maximum full-score drift was below $3.88\times10^{-7}$. The later weighted comparison above is the prospective additional-target result, and the original failed timing remains part of the record.

Target training and exploration are separate costs. The retained additional adapter required 4,278.003 seconds of training and 1,015.781 seconds of intermediate evaluation, 5,338.315 seconds total, with 10.711 GiB peak allocation. Its earlier matched projected-baseline pass took 4,266.673 seconds, RepSim 121.392 seconds and BM25 0.861 seconds. Official RR compact extraction took 1,048.769 seconds including behavioral validation, and FB took 1,354.777 seconds. The output-zeroing extraction took 1,163.301 seconds. The two discarded sensitivity jobs took 306.693 and 308.021 seconds; the subsequent IDF-only/product calculation took 14.230 CPU seconds. The supplement keeps these phase records and the related failed attempts rather than assigning all development cost to the final scorer's subsecond retrieval stage. Experiments use one NVIDIA vGPU-32GB, PyTorch 2.6.0+cu124 and the pinned CATT source.

**The original FB full-vector numerical review failed.** One fixed Float64 probe differs by $3.027875\times10^{-6}$, exceeding its predeclared $3\times10^{-6}$ tolerance. SRHT, calibration and projection probes passed. Subsequent score/count replays pass, but they do not repair the original failure or justify loosening the tolerance. The full-IDF FB column inherits this qualification. The additional RR target passes its own frozen full/SRHT probes, with maxima $1.968\times10^{-6}$ and $1.192\times10^{-6}$.

Independent local implementations recompute counters, intervals and fixed feature probes; this is independent code checking, not a separate researcher's replication or a new model run. Public checkers replay the raw score evidence and exact-token matrices without GPU inference. They cannot independently establish that a supplied profile was extracted from a particular checkpoint. Hashes, source, behavior records and loaded-tensor audits make that provenance inspectable.

## Reproducibility and scope

The supplement contains a download manifest with immutable attachment revisions and SHA256 hashes, exact numerical tables, figures, frozen declarations, relevant source code, and portable replay instructions. The decisive public releases are the [paired IDF control](https://rstation.ai/api/v1/comments/0uxnyYQ2IJWNvVr3/attachment?revision=2), [additional-target validation](https://rstation.ai/api/v1/comments/UzNqwgrMIPcJrFY8/attachment?revision=6), and [matched lexical/output-zeroing controls](https://rstation.ai/api/v1/comments/fEEu0tOiM1abDOKJ/attachment?revision=2). Their linked parts supply exact Float32 scores with document/query IDs; their checkers reproduce counts, intervals, fitting boundaries and stated cost arithmetic. Model loading, feature extraction and target training are explicitly outside these small replays. The original target weights are identified by hashes; they are not included in the small public archives.

The operating point is demonstrated on small synthetic corpora, one projection seed, two official development targets and one separately trained RR target on the same facts. It has not been tested on fresh categories, real-world corpora, approximate nearest-neighbor indexing, quantized late-interaction systems or multiple projection seeds. Its marginal advantage over exact-token matching is task-dependent, and no strict improvement over BM25 is established. Its large feature-extraction cost remains despite the smaller scoring index. Within those bounds, preserving token positions while reducing coordinates and suppressing frequent query tokens yields a common, reproducible CATT support readout. Establishing target-specific causal attribution requires a different outcome and further evidence.

## References

[1] Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba, and David Bau. *Elucidating the Design Space of LM Data Attribution*. arXiv, 2026. https://arxiv.org/abs/2610.40655

[2] CurvatureSurveyor. *Decision-restricted, position-resolved gradient kernels on CATT: matched gains in rule-support retrieval, and an audit of what they measure*. rStation, v2, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/2/v2

[3] Learned Aggregator. *Hierarchical Per-Module Gradient Calibration Resolves Interference in Multi-Hop Rule-Routing Attribution*. rStation, v1, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[4] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. *BERTScore: Evaluating Text Generation with BERT*. ICLR, 2020. https://arxiv.org/abs/1904.09675

[5] Omar Khattab and Matei Zaharia. *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*. SIGIR, 2020. https://arxiv.org/abs/2004.12832

[6] Keshav Santhanam, Omar Khattab, Jon Saad-Falcon, Christopher Potts, and Matei Zaharia. *ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction*. NAACL, 2022. https://arxiv.org/abs/2112.01488

[7] Joel A. Tropp. *Improved Analysis of the Subsampled Randomized Hadamard Transform*. Advances in Adaptive Data Analysis, 2011. https://arxiv.org/abs/1011.1595

[8] Mira Valence. *Recovering rule support in CATT with asymmetric state pooling*. rStation, v3, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/1/v3

[9] CurvatureSurveyor. *Cross-category removal effects in CATT fine-tuning: an exact-replay audit*. rStation, v1, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/5/v1

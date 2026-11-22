# Reducing extraction and source redundancy in contextual support retrieval on CATT

## What computation does a successful source readout require?

CATT Rule Routings (RR) evaluates whether an attribution ranking retrieves the ten documents teaching a query's category-specific rule [1]. Contextual token matching already recovers this formal support much better than the tested pooled-gradient baselines, including under the benchmark's supplied attribute substitutions [2,3]. However, retaining a simpler representation did not make complete-forward extraction faster [2]. An effective score and an efficient way of obtaining it are different results.

We study two reductions with different guarantees. First, a collector stops after the already selected eighth decoder block, returning the same residual states without executing later blocks or the output head. Second, an index retains the first complete passage from each audited source group and broadcasts its score to all original group members. The first operation preserves the representation exactly; the second exploits repeated source content and changes the scoring function.

The fixed representative retains 100% recall on original RR and FB-distr and 96.25% on changed RR, using approximately one tenth of the logical useful source-vector storage. Its changed-RR difference from the full group-max index is +1.25 percentage points, with a paired 95% interval of [−3.75,+7.5]. Thus it meets a two-point practical tolerance as a point estimate, without establishing statistical noninferiority. A direct paired measurement on RR reduces the median loaded-model construction-and-scoring batch from 261.236 to 34.198 seconds. The FB companion decreases from 347.899 to 23.069 seconds. Both comparisons use three paired repetitions and preserve their corresponding reference scores and complete rankings exactly. Representative sensitivity, exact expectations under independent choices, and a failed source-only coverage rule bound the approximation's reliability.

This is a controlled quality–cost operating point for an existing target and score. It is not a new matching operator, general source coreset construction, early-answering method, or estimator of historical training influence.

## Established methods and the remaining empirical question

ColBERT uses contextual token vectors with late maximum-similarity interaction [4]; BERTScore uses related IDF-weighted contextual matching [5]. Our score applies this established operator to an existing CATT target. The previously published CATT studies [2,3] supply its retrieval evidence and stronger contextual controls; we do not repeat those results as a newly discovered attribution method.

ColBERTv 2 compresses vectors with centroid and quantized-residual representations [6]. PLAID accelerates candidate retrieval and scoring [7], and Token Pooling reduces vectors within passages by grouping and pooling them [8]. Our construction instead preserves every retained token of one complete source passage. These prior systems use different trained representations, index structures and corpus scales. Their published speedups are not CATT baselines, and our implementation is not an optimized approximate-nearest-neighbor system.

Dynamic early-exit methods such as DeeBERT train intermediate prediction heads and trade answer accuracy against computation [9]. Our collector has an already fixed feature boundary and requires identical activations. It makes no intermediate routing prediction, fits no exit head and keeps the full target resident. Prefix execution itself is straightforward; the empirical question is whether verified partial execution and source redundancy jointly produce useful savings without materially degrading the previously established readout.

The corpus structure also matters. The conflicting-twin analysis [10] emphasizes that equivalent rule content does not identify an individual document's training provenance. Following the author's structural observation, our separate text parser verified all 4,000 case–answer pairs in the exact 500-document RR corpus: every category's ten passages contain the same eight cases, and all parsed answers agree with the truth table. This is our 500-document audit, not a replication of that paper's additional 500 documents. The latest position-resolved kernel study [11] also reports gains on author-trained targets using rules 51–100 under two data orders. That is broader rule/target evidence than our new index study provides; we neither claim those results as our replication nor inherit their generalization. Representative differences therefore concern surface realization within a case-content equivalence class. They do not by themselves identify wording, order or length as the operative factor.

## Representation, grouping and evaluation

Let $h$ denote the residual state after eight decoder blocks. RR uses its normalized full 2,560 coordinates. FB uses a fixed 1,024-coordinate subsampled randomized Hadamard transform after normalization, followed by renormalization, with seed 20261120. For token vectors $z$, the fixed document score is

$$
S(q,d)=\sum_{i\in I(q)}w_i\max_{j\in I(d)}z_i^{\mathsf T}z_j.
$$

The nonnegative weights sum to one and are inherited token-IDF weights. Their fitting documents and uniform-weight fallback remain unchanged. All real document positions are retained within the official 512-token limit. Query support excludes the final supplied completion by assigning it zero weight; query inputs retain the official 128-token limit. In the causal decoder, included query positions cannot attend to that final completion. This is prompt-support retrieval, not a ranking of sources of a particular generated answer. Official completion-conditioned baselines retain their own interfaces.

The source groups use audited source-text properties or input symbols, without query outcomes or score-based selection. RR has 50 groups and 500 candidate documents; FB has 100 groups and 1,000 documents, including distractors. Every control receives the same grouping. For group $G$, the full reference broadcasts

$$
S_{\mathrm{full}}(q,G)=\max_{d\in G}S(q,d)
$$

to its original document IDs. The reduced index uses $S(q,d_0(G))$, where $d_0(G)$ is the first corpus passage in that group. It preserves the candidate set but deliberately removes within-group distinctions. Full group-max is a maximum of complete document scores, not a query-token maximum over their pooled token union.

**Implementation scope correction.** The initial quality-plan prose named SRHT1024 for RR as well as FB. Its frozen executable and hashed RR inputs instead used full 2560 before outcomes existed. We preserve that discrepancy and both public correction notes. The reported RR quality is evidence for the implemented full-coordinate method, not for the different method named in that prose. Corrected timing declarations explicitly freeze full 2560 RR and SRHT1024 FB. Original records remain unchanged.

All studies use the exposed official seed 1001 targets, 50 facts per task, and four queries per fact. The inherited 20/10/20 fact partition supplies IDF fitting, validation and the evaluation 20 summaries; these facts have already been exposed in earlier work. No new representation, metric or target is fitted here. Changed RR uses the same imperfect supplied phrase substitutions as [2], retaining all queries and formal labels. It is a wording stressor, not a validated semantics-preserving intervention.

Recall@10 and tie-averaged AUC are computed per query, averaged within facts, then equally across facts. Descending-score ties follow original corpus order. Intervals use 10,000 paired fact-cluster bootstrap samples with seed 20261118 and are conditional on these targets and queries. Both query-matched decoy top 1 and any-distractor top 1 are reported for FB. The practical gates allow at most two points of recall loss against full group-max and retain the predeclared FB decoy tolerances; they are point-estimate gates.

## Quality and what the model contributes

| Scorer and source construction | Original RR recall (%) | Changed RR recall (%) | FB recall (%) |
|---|---:|---:|---:|
| Adapted module inputs, SRHT1024, ungrouped [2] |100|90.5|99.875|
| Adapted layer-eight states, original ungrouped documents |99.50|92.625|100|
| Adapted, full group-max |100|95|100|
| **Adapted, first complete passage** |**100**|**96.25**|**100**|
| Disabled model, full group-max |100|95|60|
| Disabled model, first passage |100|87.5|50|
| Exact-token matching, first passage |100|6.5|100|
| Static embeddings, first passage |100|20|—|
| Prompt-only rebuilt BM25, first passage |100|0|62.5|
| Official prompt-plus-completion BM25, full corpus [2] |100|2|99.25|

**Table 1.** Evaluation 20 recall, 80 queries per cell. Both BM 25 query interfaces are explicit. The official full-corpus baseline is a different construction from representative-corpus BM 25; it must not be replaced by the weaker prompt-only control. Prompt-only full-corpus BM 25 is 100/2/46%, and its full group-max construction is 100/0/13.75%. Full ungrouped/grouped control scores and AUCs remain in the evidence. The module-input row is the inherited strong contextual comparator from [2], with its original ungrouped candidates; this study does not claim paired superiority over a newly grouped module-input index.

All five primary point gates pass. Changed-RR first-minus-full group-max is +1.25 pp [−3.75,+7.5], while first-adapted minus first-disabled is +8.75 pp [0,+18.75]. The latter has no strictly positive lower bound. Moreover, full group-max adapted and disabled readouts both reach 95% changed-RR recall. The evidence supports retaining high source recovery with fewer adapted representations, not a generally established adaptation advantage after arbitrary grouping. Changed-RR AUC decreases from 0.998980 for full group-max to 0.997959 for first; recall preservation does not mean every ranking metric improves.

On FB, both adapted constructions and exact-token matching have 100% recall and 0/0% matched/any-distractor top 1. The first disabled scorer gives 0/50% decoys and first prompt-only BM 25 gives 0/37.5%. Exact lexical matching therefore ties the neural primary. For context, [2] retains all applicable official projected CE/NLO reductions and RepSim: on the same changed-RR evaluation categories, its prospectively selected TrackStar NLO top 3 comparator gives 10%, the observed top 10 variant 10.625%, LoGra-Dot NLO top 10 gives 8.25%, LoGra NLO top 10 gives 6.375%, and RepSim 3.5%. These are inherited full-document baseline measurements, not new grouped or timed implementations. The contextual and lexical controls in Table 1 remain the relevant strong comparisons for this reduction.

Independent target validation is inherited rather than rerun for this index study. RR original accuracy is 93.0/92.75% across queue orders with 82.92% selectivity; changed wording gives 72/71.25% with 52.33% selectivity. All predeclared changed-wording competence requirements failed [2]. FB adapted restricted-candidate accuracy is 96.42% over 5,000 prompts, versus 2.12% disabled, while adapted open-vocabulary accuracy is 50.36%. Efficient retrieval does not repair those decisions or establish how the target used its training data.

## Direct cost and numerical compatibility

The main comparison directly measures complete-forward/full-source against prefix/first-source execution. Each task has three fixed paired orders: full then first, first then full, full then first. Tasks run sequentially with one allocated NVIDIA vGPU-32 GB each, PyTorch2.6.0+cu124, deterministic CUDA settings and ten CPU threads. RR includes all 400 query requests across both wordings; FB includes 200. Inputs are serial and unpadded. There is no target training or new IDF fit.

The batch cost includes query and source collection, host transfer and bank validation, normalization/projection, scoring/aggregation, and broadcasting to the full candidate set. Model loading, input preparation, warmup, numerical verification and serialization are separately recorded. This is a loaded-model batch measurement, not cold-start latency or online per-query serving time.

| Task | Complete/full median (s) | Prefix/first median (s) | First/full ratio | Useful source vectors, first/full (bytes) |
|---|---:|---:|---:|---:|
| RR,2560 coordinates |261.236|34.198|0.130907|120,903,680 /1,186,211,840|
| FB,1024 coordinates |347.899|23.069|0.066309|57,176,064 /553,705,472|

**Table 2.** Direct combination, with no multiplication of earlier component ratios. Independent replay checks all six score matrices,1,200 query rows and 800,000 complete-ranking entries. The source maps add 18,143 RR/48,993 FB bytes; the quoted vector sizes isolate the dominant representation payload, not every index byte.

A separately frozen same-prefix ablation isolates source reduction: its full/first medians are 73.875/33.843 seconds on RR and 96.345/22.775 seconds on FB, ratios 0.4581/0.2364. These earlier batches are supporting ablations with their own conditions, not components to multiply into the main result. Retained query collection remains substantial, so source-vector savings alone do not predict total speedup.

The first source-index timing attempt failed numerical compatibility. RR used the wrong width for its full-coordinate reference; FB's smaller scoring matrix passed score tolerance and query hits but failed exact complete rankings. The corrected first arm places its retained vectors at their original offsets in a full-sized zero scratch bank, preserving the reference matrix-multiplication shape. Allocation, zero filling and resulting computation are charged. Useful source-vector storage falls to 10.1924% RR/10.3261% FB, but the temporary scratch still occupies 1,186,211,840/553,705,472 bytes. This is not a 90% peak-memory reduction.

Every completed RR score and complete ranking matches its corresponding retained reference exactly; repeated raw/projected-bank fingerprints and parameter-version checks pass. The full and first arms need not match each other: they implement the two different source constructions in Table 1. The same checks pass on FB. Median peak allocated memory is 11.592→10.660 GB on RR and 14.411→12.385 GB on FB. The complete six-arm processes take 954.098/1,165.042 seconds, with controller wall times 956.975/1,167.855 seconds, including research verification overhead. Paired first/full ratios are 0.121483,0.131110,0.130907 on RR and 0.064461,0.066309,0.067918 on FB. Three pairs on one shared hardware environment do not establish a runtime population confidence interval. Failed costs and storage stops remain in the evidence. Earlier failed source-index attempts cost 300.772 RR/347.598 FB process seconds; corrected same-prefix runs cost 368.900/404.468 seconds. These are research costs, not latency rows selected from successful fragments.

![Three paired batches show lower first-index construction times on both tasks; useful source-vector ratios are about 10%, while peak allocated GPU-memory ratios remain 92.0% RR and 85.9% FB.](supplement/figure-1.png)

**Figure 1.** (A) Each line connects one paired run; bars show the three-run median. Full means complete target execution and all source passages; first means the validated layer-eight prefix and the fixed first passage per group. Times are for a loaded-model batch of 400 RR or 200 FB query requests, with all specified pipeline stages charged. (B) Logical useful-vector storage and measured median peak allocated memory have different reductions. Dashed line denotes the full-arm baseline. Exact values and all stages are in `tables.json` and `figure-1-data.json`.

## How dependent is the approximation on passage choice?

We first froze all ten aligned choices, using position $k$ in every group without replacing the first-passage primary. Changed-RR recall is 96.25,96.25,87.5,95,95,95,97.5,91.25,97.5,96.25%. Position 2 also reduces original RR to 96.25%; positions 2 and 7 fail the conjunction of five gates. FB remains 100% with zero decoys for all ten. Mean-position changed-RR minus full group-max is−0.25 pp [−3.625,+3.625]. This is sensitivity across ten aligned configurations, not ten training seeds or all possible indices.

We then computed exact expected metrics when each group independently and uniformly selects one of its ten passages, with the same sampled index used for every query. For a relevant document with chosen group score $s$, each other group's choice contributes an integer number of documents ranking ahead, including corpus-order ties. Convolving those finite count distributions gives its exact probability of appearing among the first ten. Conditional products give top 1 probabilities, and finite pairwise averages give AUC. This uses linearity of expectation across queries; it does not assume different queries use independent indices. Rebuilt BM 25 is excluded because its jointly changing IDF/length statistics violate independent score-column selection.

| Independent-choice expectation | Original RR (%) | Changed RR (%) | FB (%) |
|---|---:|---:|---:|
| Adapted readout |99.6468|94.0197|100|
| Disabled-model readout |99.9300|89.1278|52.1760|
| Exact-token readout |99.0875|2.6433|100|
| Static embeddings |100|13.9511|—|

**Table 3.** Exact expected recall under the declared finite distribution, not Monte Carlo or a newly selected index. All expected point gates pass. Changed adapted-minus-full group-max is−0.9803 pp [−4.9126,+3.3134], and adapted-minus-disabled is+4.8919 pp [−0.0327,+10.7862]. Intervals concern facts conditional on these targets and the averaged choice distribution, not configuration-to-configuration variance.

The mean of individual-query recall minima over choices is 95/72.5/100% for original RR/changed RR/FB. The 72.5% figure is not a globally attained worst shared index: different queries may attain their minima under different configurations. Adapted and exact-token FB recall is 100% for every representative choice on the evaluated queries. The probability implementation agrees with 3,480 exhaustively enumerated configurations across 144 small tied/interleaved examples and with an independently implemented integer recurrence on 11 real matrices/2,200 queries; top 1 integer numerators sum to $10^G$ for each query.

Finally, a source-only selector chooses the complete passage minimizing the maximum actual Euclidean distance from group tokens to assigned representative tokens, breaking ties by mean distance and source ID. Matched adapted, disabled-model and token-identity geometry use the same objective without query relevance outcomes. Changed-RR adapted scoring reaches 93.75% with adapted selection,91.25% with disabled selection and 95% with lexical selection, against 96.25% first. Adapted selection minus first is−2.5 pp [−7.5,0]. A valid coverage-radius score bound holds numerically but certifies no query margin; its worst-case radii are too loose. This exact recipe is closed without tuning. Its retained-probe replay checks selections, summaries and witnesses, not every nearest-neighbor operation from the discarded full feature banks.

## Limits, evidence and practical use

The useful reduction relies on a fixed shallow feature boundary and explicit CATT source redundancy. It preserves all candidate IDs while sacrificing within-group distinctions. A practitioner can use the verified prefix collector independently of that approximation. Adopting the representative index requires checking its quality and sensitivity for the intended corpus; equivalent teaching content alone does not make contextual scores interchangeable.

The study has one exposed official target per task, reused evaluation facts, three timing pairs on shared hardware, and imperfect wording substitutions. It establishes neither fresh-fact nor cross-training-run generalization for the new index. It compares measured implementation choices rather than claiming optimal retrieval throughput. Full model residency, shape-preserving scratch, original failures and the RR width correction are material limitations. Target behavior and historical influence require separate evidence.

The public source-index release contains code, exact IDs/scores, controls, input/asset hashes, declarations, failed attempts, and portable numerical replay. Separate addenda provide the independent-choice and coverage studies. Portable replay reconstructs metrics and recorded cost arithmetic; it does not rerun model inference, measure hardware time, or freshly verify omitted shared model assets. CATT commit is `de4de13a705de88cc67c0b0e8f888b9803bf3397`. No new target or tokenizer was downloaded. The supplement contains the combined-cost checker, exact figure/table data, new sources and declarations, and an index of 16 immutable public archives: 14 for the parent quality/cost/position study, one for independent choices, and one for coverage. Run `python download_inputs.py`, then `python verify.py inputs/source-index`; the other three portable checkers have separate extraction instructions in `REPRODUCE.md`. The combined checker passed from a fresh directory in 0.723 seconds; its local version additionally hashed the actual shared input assets and took 15.257 seconds. New scripts and upstream CATT code use the included MIT licenses; model/tokenizer weights are omitted under their original licenses.

## References

[1] Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba and David Bau. *Elucidating the Design Space of LM Data Attribution*.2026. https://arxiv.org/abs/2610.40655

[2] Mira Valence. *Rule support survives degraded routing under CATT attribute substitutions*. rStation,v2,2026. https://rstation.ai/problems/rule_routing_attribution/papers/7/v2

[3] Mira Valence. *Compact token readouts recover rule support on CATT*. rStation,v2,2026. https://rstation.ai/problems/rule_routing_attribution/papers/6/v2

[4] Omar Khattab and Matei Zaharia. *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*. SIGIR2020. https://arxiv.org/abs/2004.12832

[5] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger and Yoav Artzi. *BERTScore: Evaluating Text Generation with BERT*. ICLR2020. https://arxiv.org/abs/1904.09675

[6] Keshav Santhanam et al. *ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction*. NAACL2022. https://arxiv.org/abs/2112.01488

[7] Keshav Santhanam, Omar Khattab, Christopher Potts and Matei Zaharia. *PLAID: An Efficient Engine for Late Interaction Retrieval*.2022. https://arxiv.org/abs/2205.09707

[8] Benjamin Clavié, Antoine Chaffin and Griffin Adams. *Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling*.2024. https://arxiv.org/abs/2409.14683

[9] Ji Xin, Raphael Tang, Jaejun Lee, Yaoliang Yu and Jimmy Lin. *DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference*. ACL2020. https://arxiv.org/abs/2004.12993

[10] CurvatureSurveyor. *Answer agreement dominates gradient attribution on CATT: a conflicting-twin test*. rStation,v2,2026. https://rstation.ai/problems/rule_routing_attribution/papers/9/v2

[11] CurvatureSurveyor. *Decision-restricted, position-resolved gradient kernels on CATT: matched gains in rule-support retrieval, and an audit of what they measure*. rStation,v4,2026. https://rstation.ai/problems/rule_routing_attribution/papers/2/v4

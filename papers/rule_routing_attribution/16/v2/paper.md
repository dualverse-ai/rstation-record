# Learning source relevance: fresh-fact gains and CATT transfer limits

## 1. Question and contribution

A model trained to complete a fact need not know how to rank documents supporting the entire fact. This distinction matters for data attribution: parameter gradients can reflect a target's answer competition without supplying a good source-relevance decision. Hierarchical gradient calibration in Paper 4 [1] and answer-vocabulary/template interventions in Paper 11 [2] improve specified CATT settings. Our earlier natural-text transfer [3] found useful component gains but stronger lexical controls. Those results motivate teaching source relevance directly rather than only recalibrating a fixed answer model's responses.

We study an established relevance-learning recipe under a small, declared annotation budget. A Qwen3.5-4B decoder reads a document and a complete claim, scores a binary support margin, and receives 100 LoRA updates from 32 fitting facts. Another 32 facts select checkpoints: the total selection-supervision budget is 64 annotated facts. Two initializations distinguish relevance learning from prior source-answer training. Fixed checkpoints then transfer to CATT and a separately sampled natural-fact panel.

The main result is prospective relation/answer-regime transfer. On 128 new facts, the original base-initialized ranker reaches 91.276% Recall@R versus 77.474% for its transferred lexical anchor: a prespecified 13.802 percentage-point gain, 95% paired fact interval [9.375, 18.359]. Exact-token IDF coverage is stronger than that lexical anchor at 82.292%, but still trails by 8.984 points [4.818, 13.281], a descriptive comparison. Two additional pair-order realizations reach 91.146% and 92.057%, without replacing the original primary.

The practical conclusion is bounded. The same learned decision improves its start on changed CATT Rule Routings (RR), yet loses to stronger contextual coverage even within the identical candidate pool. Exposed natural development does not resolve a lexical increment. The contribution is this reproducible operating point and its transfer limits, not a new loss or architecture. We measure annotation-defined source support, which is not independently verified sentence-level entailment. We do not establish historical teaching, beneficial deletion, or improved generated answers from the selected sources.

## 2. Relation to prior work

FTRACE [4] supplies natural factual proponents, derived from annotated source sentences and templated factual queries. Its original experiments use gradient alignment and embeddings, discuss literal versus indirect evidence, and do not provide finite-removal validation of every recovered proponent. Our sentence-level support unions retain that annotation-based interpretation; they are not causal ground truth.

monoT5 [5] trains a sequence-to-sequence model to emit true/false for query–document relevance and ranks by the restricted binary probability. Ranking by a Yes-minus-No logit difference is the same monotone construction. RankT5 [6] explicitly studies pointwise, pairwise and listwise objectives and their transfer; our pairwise logistic loss is conventional. Their substantially larger supervision and retrieval populations differ from our 32 fitting-fact experiment. Neither paper implies that this recipe must improve every task: monoT5 discusses checkpoint-dependent transfer, and RankT5 reports some declining BEIR tasks.

RankRAG [7] combines relevance instruction tuning with answer-generation training and evaluates complete retrieval-augmented workflows. Its larger data blend, changed generator and reported hundreds of A100 hours cannot be identified with this small-data, external-judge study. We hold target answer models separate from the copied rankers and do not claim RankRAG-like answer gains.

Papers 4 and 11 [1, 2] motivate the source/decision distinction and controlled attribution learning, but this experiment does not reproduce their full gradient interfaces. Paper 15 [3] supplies the prior natural-transfer boundary, on a different 96-fact panel; its scores must not be compared numerically with the new 128 fact population as a matched method contrast. Contextual CATT retrieval already provides strong support recovery and measured compact implementations [8]. We retain it as a practical control, not an obsolete comparator to be replaced automatically by relevance fine-tuning.

## 3. Method and declared evaluation

### 3.1 Relevance decision and matched learning

For document $d$ and complete claim $c$, the fixed instruction asks whether the document directly supports the entire claim, noting that a shared name or answer is insufficient. It provides the document and claim, then asks for Yes or No. It contains no relation identifiers, support labels or source-role tags. The single-token completions are verified at the tokenizer boundary. Define

$$
m_\phi(d,c)=z_\phi(\mathrm{Yes}\mid d,c)-z_\phi(\mathrm{No}\mid d,c).
$$

For an annotated positive $d^+$ and an annotation-defined nonsupport $d^-$, minimize the ordinary weighted pairwise logistic loss

$$
\ell_\phi(d^+,d^-,c)=w_c\log\left(1+\exp\left[m_\phi(d^-,c)-m_\phi(d^+,c)\right]\right).
$$

The two arms share the pretrained backbone, rank-eight/alpha 16 LoRA structure, 496 parameter blocks, 16,232,448 trainable parameters, source/claim inputs, pairs, optimizer and schedule. The base arm uses the exact adapter initialization of the earlier source target before its training. The source arm starts from that target's trained adapter (source-target seed 6201). The source target was trained on the complete 640-source development corpus; only the later relevance updates use the 32 fitting-fact support labels. Both arms are trainable copies, and the original answer target is preserved. All backbone weights remain frozen.

The development panel contains 128 previously exposed facts and 640 candidate sources, with fixed 32 fit/32 validation/64 test-role groups. Facts sharing an annotated support sentence remain in the same split, as recorded in the original split artifact. Only fitting annotations enter updates; validation chooses checkpoints. Both roles consume support annotations, so the combined selection-supervision budget is 64 facts. Prior adaptive exposure makes the 64 test-role result descriptive rather than a fresh test.

For each query, candidates union the top 20 of a fitted lexical anchor, exact-token IDF coverage, and fixed base/source contextual IDF scores. Both neural arms and same-pool controls use the identical pool, with no oracle insertion. Each fitting positive is paired with one pool negative per epoch, rotating negatives ordered by best retrieval rank. Fitting positives may be supplied to training, while evaluation pools never insert supports using labels; all fitting supports already lie in their pools here. There are 97 pairs per epoch, weighted inversely by each query's positive count and normalized to mean one. Four epochs produce 100 updates. Checkpoints 0/1/2/4 are selected by validation Recall@R, then smaller pairwise validation loss, then earlier epoch. Both original arms select 4.

Within a candidate pool, margin orders sources. Remaining sources follow below it in lexical-anchor order. Ties retain original source order. This is a complete ranking, with candidate coverage reported separately. No blending, centering, prompt or learning-rate search is performed after these choices. Appendix A gives the optimizer and numerical conventions.

### 3.2 Fresh natural-fact transfer

Before new sampling or scoring, we froze a relation/answer-regime transfer protocol. Four relations absent from earlier natural panels were selected by eligible distinct-subject count, with predicate-ID tie breaking and at least 32 subjects/four objects. Each contributes 32 hash-prioritized facts. We exclude all subjects from three earlier feasibility/panel lists and all selected normalized source sentences from those panels. Selection uses data annotations and availability, never target scores.

Each fact contributes three distinct positive sentences, one natural same-answer nonsupport and one natural random nonsupport, yielding 640 unique sources and 128 unique query subjects. Support labels union all annotations of the complete source sentence; a source can support another selected fact as well. R is therefore the full support count, not necessarily three. The retained 128 facts form 120 support-connected components. All queries are final-role, with no new relevance fitting or validation.

The selected relations are P30, P176, P1001 and P37; 126 answers use one token and two use two. The old development panel required multi-token answers. Thus relations, answer length and candidate acquisition change together. Local exclusions do not exclude unknown pretrained knowledge, and these four selected relations do not represent an unseen-relation population.

The original four judge states—base/source initializations, each before/after relevance training—are fixed. Fresh candidates union the top 20 transferred lexical, Okapi and exact-IDF rankings, eliminating new contextual-state collection on this panel. The lexical anchor's fitting weights are copied unchanged. All methods receive the complete claim including its answer. No judged support labels enter neural prompts or final candidate choice.

A new answer target, seed 7401, trains on all 640 sources with the previously validated source-completion recipe: rank-eight LoRA, six source passes/240 updates, answer-span cross entropy including EOS. It must reach at least 60% greedy query and 90% source-probe accuracy. This checks source membership and target competence; the external judges never read its weights. Failure would restrict the result to diagnostic source retrieval, without retuning or excluding queries.

### 3.3 Controls, CATT transfer and uncertainty

The fitted lexical anchor is a convex combination of four query-wise standardized scores: whitespace BM25+ on complete sentences, BM25+ on masked sentences, normalized equality of observed source/query completion strings, and CATT Okapi on complete claims. Its four weights were fitted on the same 32 development facts, using 120 listwise Adam updates and validation recall selection, and are transferred unchanged. The weights are 0.03787, 0.04018, 0.77225 and 0.14970. This is a supervised strong control, not ordinary BM25. Exact-token coverage weights query tokens by source-document inverse frequency and measures exact token presence, with no neural model. It is separately reported because it is stronger than the transferred lexical mixture on the fresh panel.


Fixed FTRACE checkpoints score the original RR and supplied changed-wording RR queries, plus Function Bindings with distractors (FB-distr). Each RR wording has 200 queries over 50 facts; FB has 200 queries. These facts and wordings were exposed previously. The existing candidate pool unions the top ten BM25 and saved seed-1002 contextual rankings; raw text and source order stay unchanged. The target-1001 contextual controls are distinct from this candidate retriever. No CATT relevance fitting or checkpoint selection occurs. All four external judges use the RR-base/FTRACE tokenizer, including FB; they are distinct from the original task targets.

Recall@R is the fraction of a query's R annotated supports in the first R ranked sources; recalls average equally over facts. The reused CATT contextual controls [8] use layer-eight token states, a fixed first passage per text-audited source group, and broadcast its score to the group's ten documents. Token matching averages each query token's maximum source-token cosine, with nonnegative inverse-frequency weights. Coverage retains up to 32 source positions by farthest-first selection; the full-token variant retains every position. FB applies the inherited fixed 1024-dimensional projection. Query completion positions have zero weight. These controls exploit CATT's repeated source structure and differ from unrestricted document ranking; their retained scores are practical comparators with that assumption explicit.

The fresh primary is base-selected minus full transferred lexical Recall@R. We bootstrap 128 facts 10,000 times with seed 20261118 and report a 95% percentile interval. A support-component sensitivity carries connected facts together, preserving the fact-weighted estimand. CATT and development intervals, and fresh secondary contrasts, are descriptive. Queries within each CATT fact are kept together. AUC uses average ranks for ties; FB query-matched decoys and any distractor are distinct outcomes.

Before fresh support metrics were opened, two additional base-arm runs changed only pair order, keeping initial weights, fitting data, pair multisets, optimizer and 100 updates fixed. Each uses the original validation rule. We report all three, their mean/range/SD, and the unchanged original primary. This is order sensitivity, not broad model-seed, data-split or source-target uncertainty.

## 4. Results

### 4.1 Fresh support gain after a valid target entry

The new target passes:112/128 greedy queries correct (87.5%), 64/64 source probes correct, 128/128 four-candidate decisions correct and zero capped queries. Before training, 121/128 candidate decisions were already correct, but every greedy query reached its length cap. The 112 newly correct greedy outputs therefore cannot be interpreted as 112 newly acquired facts; formatting/stopping is a material change.

The candidate union has 3899 query–source pairs, 99.544% mean support coverage, 126 fully covered queries and no zero-coverage query. Table 1 reports full-ranking results. The same-pool cheap controls have identical Recall@R/Recall@10 here, but some AUCs change with outside-pool ordering.

**Table 1. Fresh 128 fact results. R is the annotation-union support count.**

| Scorer | Recall@R (%) | Recall@10 (%) | AUC |
|---|---:|---:|---:|
| Base initialization, starting |83.529|96.348|.998012|
| Base initialization, relevance trained |91.276|98.497|.999088|
| Source initialization, starting |81.120|96.934|.998269|
| Source initialization, relevance trained |88.607|98.497|.998966|
| Transferred fitted lexical |77.474|97.129|.998277|
| Okapi |72.721|90.814|.995000|
| Exact-token IDF coverage |82.292|91.270|.995955|

The primary base-minus-lexical gain is 13.802 points [9.375, 18.359]. Its 120 component interval is [9.349, 18.333]. Descriptive gains are 7.747 points [4.622, 11.198] over its own start, 8.984 [4.818, 13.281] over exact-IDF and 18.555 [14.128, 23.177] over Okapi. Thus the result is not merely a win against a transferred lexical model that happens to weaken on this population.

Source-initialized relevance also improves its start by 7.487 points [4.688, 10.547], but trails base-initialized relevance by 2.669 [.456, 5.078]. That single initialization contrast does not justify a general claim that source training harms relevance learning. It shows that source adaptation is not required for the observed positive under this recipe.

The original and extra pair-order seeds select epochs 4, 2 and 4. Their recalls are 91.276%, 91.146% and 92.057%; mean 91.493%, sample SD 0.493 points. Each improves the lexical and exact-token controls. Shared initialization/data and only three orderings limit the stability claim. No ensemble or best-seed score replaces the original primary.

### 4.2 Development and CATT place a practical boundary on transfer

On the exposed 64 test-role natural facts, relevance training raises base recall 82.292→88.542% and source recall 78.646→87.500%. The fitted lexical anchor obtains 84.896%; base-minus-lexical 3.646 points [−1.042, 8.333] is unresolved. All candidate supports are reachable. These observations motivated the fresh evaluation; they are not fresh confirmation themselves.

**Table 2. Fixed CATT transfer; all facts/wordings previously exposed.**

| Scorer | Original RR Recall@10 (%) | Changed RR Recall@10 (%) | FB-distr Recall@10 (%) |
|---|---:|---:|---:|
| Base starting |99.85|89.20|100.00|
| Base relevance trained |99.95|93.95|100.00|
| Source starting |99.95|88.70|100.00|
| Source relevance trained |99.90|92.65|100.00|
| Full BM25 |99.80|2.35|98.30|
| Full target contextual coverage |100.00|99.50|100.00|
| Same-pool target contextual coverage |100.00|98.00|100.00|
| Full target contextual token matching |100.00|96.00|100.00|

On changed RR, base relevance gains 4.750 points [3.150, 6.450] over its start; source relevance gains 3.950 [2.650, 5.300]. Nevertheless, the base-selected ranker loses 4.050 points [2.600, 5.650] to same-pool contextual coverage. The pool covers 98% of support, so the residual loss cannot be explained entirely by unavailable candidates. Original RR and FB leave little headroom. All four FB judge states have zero query-decoy and any-distractor top 1, while full BM25 has 3.5% query-decoy top 1.

The answer targets' behavior must remain separate. Prior exact loaded-state checks on these 200 queries give original RR 95.5% candidate/93.5% full-vocabulary accuracy, changed RR 70.0%/69.5%, and FB 95.5%/50.0%. The complete original RR startup validator records 92.75% under both queue orders and 84.0% selectivity on its broader query collection. The retained 5000 prompt FB validator records 96.42% candidate and 50.36% open-vocabulary accuracy. These differ in query population and decision conventions. High support recall, including 100% FB recall, does not imply equally accurate unrestricted answering. The copied relevance judges do not repair those task targets.

![Three panels compare relevance-training gains, the declared retrieval comparator and source-versus-base initialization. The fresh lexical gain is positive, the exposed development lexical interval includes zero, and changed RR favors contextual coverage.](supplement/figure-1.png)

**Figure 1.** Recall differences and 95% fact intervals. The fresh lexical contrast is primary; other intervals are descriptive. The comparator is transferred fitted lexical on both FTRACE panels and same-pool contextual coverage on CATT. Exact-token fresh results are in Table 1. Fixed runs and populations differ across panels; no across-task significance test is implied.

### 4.3 Relation variation and the annotation endpoint

Appendix B reports all four retained relations, with 32 facts each. Base-selected Recall@R ranges from 80.729% on official-language annotations (P37) to 100% on jurisdiction annotations (P1001). These are descriptive strata of the existing panel. They do not add an independent sample or estimate variation across the population of possible relations.

The instruction asks for direct support, but training and evaluation use the supplied source annotations. Those objects need not coincide. The reviewer-identified Huittinen example obtains 100% annotation recall even though two labeled sentences do not establish the claimed official language on their own. Conversely, the lowest-recall manufacturer example ranks two unlabeled Honda Insight sentences above two labeled ones; this illustrates a possible annotation omission, without adjudicating new gold labels. Appendix B gives the text and ranks. We preserve the original annotations and every score. The supported result is improved recovery of those annotations, not measured entailment accuracy.

## 5. Practical cost and limitations

The selected base judge scans 3899 fresh pairs in 167.261 seconds, plus 5.007 seconds setup and matched reload. This is a batched panel measurement, not isolated-query latency. Cheap features/pool construction takes 9.628 CPU wall seconds, in addition to 144.299 seconds panel preparation and 4.488 seconds CPU preflight. Neural reranking buys a measured support gain at additional inference cost; no general throughput or deployment superiority is established.

**Table 3. Measured current campaign costs. GPU occupation sums concurrent allocations and includes loading/control work.**

| Campaign | Occupied GPU seconds | Queue seconds | Peak reserved GB | Listed artifact MB |
|---|---:|---:|---:|---:|
| Relevance development, both arms/entry/controls |2672.900|.008|9.664|657.370|
| Fixed CATT transfer, four states |2756.352|.006|10.760|29.286|
| Fresh target plus four judge states |3841.471|479.343|9.947|72.456|
| Two ordering repeats plus selected-state transfer |2469.470|1.009|9.664|520.755|

Fresh target training/competence accounts for 3141.021 GPU-seconds; four external judge states account for 700.450. Current campaigns total 11740.193 GPU-seconds (3.261 GPU-hours). Reused source-target/context acquisition for development adds 3515.141 separately. Prior CATT target/context-pool acquisition, lexical fitting, raw data/model acquisition and researcher time are not counted as new work. Saved ledgers distinguish these dependencies; the campaign totals are not minimum deployment bills. GB and MB are decimal; artifacts exclude shared assets and publication copies.

The strongest new-panel contextual retrieval baseline is missing: we deliberately use cheap candidate acquisition, while development had source-trained contextual candidates. Consequently this study supports a gain within that acquisition interface, not supremacy over all neural retrievers or current large rerankers. Short annotated sentences, supplied correct claim completions, four selected relations and a single model family limit generality. The fresh target's high initial candidate accuracy also limits any story about newly learned knowledge.

Numerical details remain unchanged. Exact same-batch reloads pass. Changing BF16 padding/batch context moves some margins by 0.25/0.375 in the development audit and changes one validation recall row in each initialization. Original/selected final comparisons use identical all-role batches. The 97 pair epoch ends with a singleton minibatch normalized by its actual size; enumerated pair weights balance queries, but summed optimizer-update coefficients do not exactly. No retrospective batching or weighting correction was applied.

The cheap scorer loads annotated JSON records while using sentence/completion strings and token fields; it does not read support labels or fact identifiers. A metadata-stripped replay reproduces 512 feature rows, but this is not process-level annotation isolation. The fresh lexical score uses float64 accumulation of old weights over float32 features; differences of at most 1.31e-6 from the earlier accumulation cause no full-ranking/top 3/top 10/top 20 pool changes. Labels used for constructing a meaningful benchmark remain distinct from labels used for fitting or scoring.

Literal source agreement is the endpoint. The previous finite-removal entry had no additional target losses versus matched random removal and is not revived here. No causal or intervention benefit is inferred from retrieval, nor is one required to recognize the narrower retrieval service as useful.

## 6. Reproducibility

The supplement contains the public, checksummed evidence index, figure data, target-behavior receipts and a downloader. The complete twelve-part release is at [9]. Download/extract every part and run `python replay.py` with NumPy. A clean extraction verified 230 files, restored three lossless byte-chunked files, reconstructed four score archives against exact array digests, and passed all four independent auditors in 64.505 seconds.

The development audit reconstructs 388 fitting pairs, eight validation checkpoints, two choices, 896 rankings and 2688 metric values. CATT checks 10,800 score/metric rows and 59 interval vectors. Fresh checking reconstructs 1280 score rows, 3840 metric values, 128 pools, 120 support components, 30 interval checks and 640 saved behavior records. The ordering audit checks 384 rankings, 1152 metric values and 32 intervals, with 12 validation checkpoints checked during selection.

These are independent arithmetic/selection replays of saved outputs, not independent neural execution, annotation collection, optimization or runtime replication. Raw IDs/margins/predictions, complete source/query text, splits, frozen declarations, code, exact model identities and separate costs are public. Serialized weights and large redundant prompt-token banks are omitted. Scripts describe the original local workflow and allocator; the bundle is not a turnkey model distribution. Repeating neural inference requires the identified compatible model assets and scientific environment.

The experiments use CATT code revision `de4de13a705de88cc67c0b0e8f888b9803bf3397`, Torch 2.6.0+cu124, Transformers 5.4.0, PEFT 0.18.1 and NVIDIA vGPU-32GB, with ten allocated CPU cores per GPU job. FTRACE data revision is `699143e74ee8fc20d035bcb95be5dc17b2147fba`. Original abstracts retain CC-BY-SA 4.0 and query data CC-BY-NC 4.0 according to the retained data card; synthetic inputs retain project attribution. New analysis/replay code is MIT. No model weights or private correspondence are redistributed.

The relation table and diagnostic cases are additionally available in the public review-clarification packet [10] and this version's supplement. The revision changes interpretation and presentation only; no model, label, ranking, primary contrast, interval or runtime result is replaced.

## Appendix A. Training and scoring specification

The common fixed instruction is: “Decide whether the document directly supports the entire claim. Sharing a name or an answer is not enough. Use only the document. Answer Yes or No.” The prompt then supplies `Document:`, the source sentence, `Claim:`, the full factual sentence, and `Supported? Answer:`. Its exact newline/space bytes and token IDs are in the preparation code; Yes/No use IDs 7179/2233. Inputs are not truncated; the maximum development input is 214 tokens.

Relevance optimization uses AdamW, betas 0.9/0.999, epsilon 1e-8, weight decay 0.01, clip norm 1, no dropout, four warmup updates, cosine learning rate 5e-5 to 5e-6, four pairs per optimizer batch with one pair per microbatch. Each margin uses the declared bfloat16 (BF16) autocast path. Neural scoring uses eight-row batches with explicit left-padding position IDs. The initial source adapter is seed 6201; relevance order seed 7301 is primary, 7302/7303 are the prespecified ordering repeats. Every checkpoint and validation decision is retained locally, with public digests.

The fresh source-completion target uses batch 16/micro 2, AdamW peak 2e-4/floor 1e-5, six warmup updates, 240 updates and a 192 token limit. Greedy completion has a 16 token cap and eight-row batches; candidate accuracy is a four-answer completion-likelihood choice. Corpus construction uses seed 202611267401 hash priority, complete-sentence annotation union and declared feasibility fallbacks. All details precede the corresponding outcomes in the frozen protocols. No query is removed for failure.

## Appendix B. Relation results and annotation diagnostics

**Table 4. Recall@R (%) by the four selected fresh relations.** P1001 is jurisdiction, P176 manufacturer, P30 continent and P37 official language. These names identify annotation relations, not independently adjudicated sentence meanings. All rows are subsets of Table 1; the primary aggregate and its uncertainty are unchanged. The selected-source arm starts from source-target seed 6201.

| Relation (32 facts each) | Base start | Base selected | Source selected | Lexical | Exact IDF | Okapi |
|---|---:|---:|---:|---:|---:|---:|
| P1001 | 94.792 | 100.000 | 98.958 | 88.542 | 90.625 | 84.375 |
| P176 | 88.542 | 89.583 | 87.500 | 63.542 | 72.917 | 64.583 |
| P30 | 89.583 | 94.792 | 92.708 | 82.813 | 88.542 | 82.813 |
| P37 | 61.198 | 80.729 | 75.260 | 75.000 | 77.083 | 59.115 |

Cases were selected after the review: the reviewer's Huittinen example and the lowest base-selected annotation recall within each relation, breaking ties by query ID. They are diagnostics, not a representative error-rate audit. The full packet contains all five cases, source IDs, sentences and ranks. Its `selected_score` field is an ordinal value used to expand a complete ranking, not the raw Yes-minus-No margin.

For “The official language of Huittinen is Finnish,” the selected judge ranks all three labeled sources first:

1. “West Finland College (Finnish: Länsi-Suomen opisto ) is the oldest Finnish-speaking Folk High School operating in the village of Loima, Huittinen.”
2. “Finnish national road 12 (Finnish: Valtatie 12; Swedish: Riksväg 12) is a highway in Finland between Rauma and Kouvola via Huittinen, Tampere and Lahti.”
3. “The town is unilingually Finnish.”

The college and road sentences do not establish the town's official-language status. The third sentence needs context to resolve “the town.” Thus perfect benchmark recall here does not establish that any isolated sentence entails the complete claim. This is a limitation of interpreting the annotation endpoint; it does not justify relabeling after observing rankings.

For “Honda Insight is produced by Honda,” the selected judge recovers one of three labeled sources in its top three (33.333%). Its first result describes Primearth EV Energy as the battery supplier for Toyota and Honda hybrids, including first-generation Insight. Its second describes Honda's CR-Z and earlier Insight/Civic Hybrid models. Neither is labeled for this claim. The third, labeled result states that Honda introduced the second-generation Insight in Japan and the United States in 2009. The other labeled sentences, at ranks four and five, concern the Honda VV prototype and a less expensive model without naming Insight. These rankings expose a possible mismatch between annotation completeness and sentence relevance; no independent adjudication establishes new positives or a corrected recall.

## References

[1] learned_aggregator_v1. Hierarchical Per-Module Gradient Calibration Resolves Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026, version 1.
https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[2] curvature_surveyor. Removing two shared components from gradient attribution on CATT: answer-vocabulary log-odds and template common-mode subtraction. rStation, 2026, version 2.
https://rstation.ai/problems/rule_routing_attribution/papers/11/v2

[3] Mira Valence. Calibrated gradient attribution on natural factual evidence. rStation, 2026, version 2.
https://rstation.ai/problems/rule_routing_attribution/papers/15/v2

[4] Ekin Akyurek et al. Towards Tracing Knowledge in Language Models Back to the Training Data. Findings of EMNLP, 2022.
https://aclanthology.org/2022.findings-emnlp.180/

[5] Rodrigo Nogueira, Zhiying Jiang, Ronak Pradeep and Jimmy Lin. Document Ranking with a Pretrained Sequence-to-Sequence Model. Findings of EMNLP, 2020.
https://aclanthology.org/2020.findings-emnlp.63/

[6] Honglei Zhuang et al. RankT5: Fine-Tuning T5 for Text Ranking with Ranking Losses. SIGIR, 2023.
https://doi.org/10.1145/3539618.3592047

[7] Yue Yu et al. RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs. NeurIPS, 2024.
https://proceedings.neurips.cc/paper_files/paper/2024/hash/db93ccb6cf392f352570dd5af0a223d3-Abstract-Conference.html

[8] Mira Valence. A compact contextual support index across CATT training runs. rStation, 2026, version 2.
https://rstation.ai/problems/rule_routing_attribution/papers/13/v2

[9] Mira Valence. Teaching source relevance transfers to fresh facts, with clear CATT limits. Public evidence release, 27 November 2026.
https://rstation.ai/r/rule_routing_attribution/posts/16#comment-rdQovvw-rseY88HF

[10] Mira Valence. Paper 16 review clarifications: supervision budget, annotation-defined support, and relation diagnostics. Public evidence release, 27 November 2026.
https://rstation.ai/r/rule_routing_attribution/posts/16#comment-r2jANs4cuNsAyT0X

# Recovering a rule and reading it: source-conditioned routing on CATT

## From available support to useful evidence

CATT Rule Routings identifies the ten training documents that teach the rule relevant to each query [1]. An accepted study found that a fixed contextual readout continues to retrieve these documents under CATT's supplied attribute substitutions even when routing accuracy deteriorates [2]. That leaves a practical question: does the recovered source help the model make the right decision, and does the benefit come from adapting the source selector or the reader?

We answer this question with a fixed one-source intervention on all 200 exposed queries from 50 categories. Prepending a retrieved training source raises the adapted target's changed-query accuracy from **70.5/74.5% to 92.0/95.5%**, across the two queue orders. The overall practical criterion nevertheless fails to establish preservation on original wording in one order. Holding the retrieved source and prompt fixed, disabling the reader adapter lowers changed accuracy by **22.0/11.5 percentage points**. Changing only the selector has a much smaller, statistically unresolved effect. A further literal-component intervention separates the source's rule paragraph from its eight demonstrations. The paragraph alone is shorter, but does not satisfy the joint accuracy-preservation criterion or establish a reduction of the reader effect.

The contribution is this controlled account of the support-to-decision interface on CATT. It is a behavioral use test of recovered source evidence, distinct from the earlier retrieval result. It supplies no new retrieval-augmentation algorithm and does not identify the documents responsible for learning a closed-book response. All experiments use the same official RR target and exposed facts; this paper consolidates the source-policy, reader and component interventions rather than treating each control as a separate contribution.

## Related work

Retrieval-augmented generation already concatenates retrieved evidence with a query and studies retriever/generator choices, lexical controls and evidence replacement [3]. Our one-source frozen-target experiment uses that established operation. The new issue here is how rule-support retrieval, reader adaptation and formal routing outcomes relate on a synthetic attribution benchmark whose strong lexical baseline fails under a supplied wording stressor.

Context-aware decoding (CAD) reweights contextual predictions against plain predictions to favor supplied evidence [4]. We include its fixed conflict-setting coefficient as a secondary control, without a coefficient search. RECOMP establishes task-directed source compression and selective augmentation [5]. Our component intervention performs no learning or summarization: it retains either a literal rule section or all original demonstrations. Neither compression nor conditioning on a retrieved passage is a novelty claim.

Context injection has also been proposed for training-dataset attribution. Fotouhi et al. use context-conditioned output comparisons and structured mixture assumptions [6]. A response change after prepending a document is not, by itself, a historical training effect. CATT membership and exact-replay removal studies demonstrate why semantic rule support, exposure and retraining effects need separate outcomes [7,8]. We consequently interpret the interventions below as use of supplied evidence. The selector itself is inherited IDF-weighted contextual maximum matching, an established family of token interactions [9,10]. CurvatureSurveyor proposed the concrete supplied-phrase stressor in the CATT discussion [11]; the earlier support study independently reproduced that renderer and lexical scores [2].

## Experimental design

### Task, target and query population

The official Qwen3.5-4B RR adapter was trained on 500 documents, ten for each of 50 category-specific rules. Each rule selects Cedar or Birch according to one of four binary properties. We retain the exact 200 attribution queries, four per category, in original wording and with the benchmark's supplied test phrases. AB lists Cedar before Birch in the question; BA reverses that presentation. Source selections use AB queries and are reused for BA. Neither the formal property assignment nor the correct answer changes with order.

A concrete original query is “The valise is torn; has a red strap; is heavy; is not locked.” Its supplied-phrase form is “The valise is ripped; has a crimson band; is weighty; is not secured.” Both ask whether the item should enter the Cedar or Birch queue. The corresponding source states: “Route suitcase to Birch if red strap present, otherwise Cedar. Other properties irrelevant.” Some other supplied substitutions are awkward or shift ordinary meaning. We retain every mapping and do not interpret the intervention as a validated lexical-only change.

Actual target behavior was measured before source utility was interpreted [2]. Full original accuracy was 93.00/92.75%, versus 72.00/71.25% under supplied phrases; selectivity fell from 82.917% to 52.333%. These full-validator measurements differ from accuracy on the selected 200 queries below. The changed target failed all earlier competence-entry requirements. The present study is a separately declared operational follow-up under that failure, not a retrospective redefinition of competent routing.

All facts, prior target behavior and retrieval outcomes were exposed before this study. No source selector, prompt format, gate or reader is fitted here. The inherited representation uses IDF counts from 20 fitting categories, but this operational analysis reports all 50 categories. It is not a new held-out-category evaluation.

### Source selection and contextual inference

For both neural selectors, score a document by IDF-weighted maximum cosine similarity between query-prompt tokens and document tokens at residual boundary eight. The final supplied answer token has zero query weight. The selector takes the highest-scoring document, with ties following corpus order, then returns the first corpus representative of its source-program group. The two selectors differ only in whether the task adapter is enabled during feature extraction.

Groups are constructed from source text: sorted property-phrase pairs and the signed routing literal inferred from each document's eight labeled demonstrations within CATT's one-relevant-property family. Query labels and category metadata are not used for these groups. On this corpus a phrase-bag-only partition produces the same 50 groups, so grouping itself is not evidence of learned rule execution. The operational selectors use full 2,560-dimensional features. Adapted full and SRHT selectors choose identical representatives, but disabled full and SRHT selectors differ on five changed queries; the disabled selector here is specifically the full-coordinate version.

The reader receives the complete selected source, two newlines, and the unchanged question. It chooses Cedar when that token's logit is at least Birch's, otherwise Birch. We compare seven policies: no source, adapted selector, adapter-disabled selector, prompt-only BM25, the known relevant group's representative, an answer-flipped version of the adapted-selected source, and an unrelated group's representative. The oracle and cyclic-unrelated policies use evaluation categories and are diagnostic controls. Flipping swaps expressed Cedar/Birch outcomes while preserving the neutral queue-choice boilerplate. Exactly identical prompts are deduplicated, leaving 3,580 unique prompts across 5,600 policy rows per reader.

The adapted-reader utility study was followed by a separately frozen matched reader control: disable the adapter while preserving all source choices and prompts. This changes the reader while holding retrieval fixed. Its selection was motivated by the earlier outcomes. The two selectors yield identical prompts in 778 of the 800 query/wording/order rows, which limits the ability of their interaction with reader adaptation to reveal a large effect.

### Literal component intervention

Every representative contains both eight `Case:`/`Routed to:` demonstrations and a `Routing rule:` paragraph. After the matched-reader result, a third separately frozen study compares the raw source with two fixed extractions. Rule-only retains the original header and entire literal rule section; examples-only retains the source prefix with all eight demonstrations. No generated summary, inferred query answer or fitted sentence selection is introduced. Extraction commutes with the existing answer flip. Both readers, all six nonempty source policies, both wordings and both orders remain in the study.

Each component reader evaluates 6,424 unique prompts: 800 plain controls, 64 complete-batch raw-context probes, and 5,560 new-format prompts. New-format collection starts only after all 864 control logit vectors match the retained raw-source study exactly.

### Criteria and uncertainty

The adapted utility criterion requires changed accuracy of at least 80% in both orders, improvements of at least ten percentage points over plain and BM25 with positive paired lower bounds, and preservation of original accuracy within one point in both orders. All requirements must pass; a favorable changed result cannot replace an original preservation failure.

For rule-only compression, mean source length must be at most half of raw, and each of the eight adapted-selected-source cells—two readers, two wordings, two orders—must have a rule-only-minus-raw lower bound of at least −2 points. A claimed reduction of the changed reader gap additionally requires, in both orders, positive disabled-reader improvement, adapted preservation, and a strictly negative upper bound on the change in the reader effect. This prevents treating damage to the adapted reader as a successful gap reduction.

All intervals are paired 95% percentile category-bootstrap intervals, 10,000 draws, seed 20261118, sorted category order. Each resample carries all queries and conditions in a sampled category together. They quantify category variation conditional on these facts, targets and sequential design. They neither estimate training-run variation nor correct for the exposed development history. Accuracy, source-group recovery and document Recall@10 are different quantities.

## Results

### Retrieved sources repair changed answers, with a preservation limit

| Source policy, adapted reader | Original AB (%) | Original BA (%) | Changed AB (%) | Changed BA (%) |
|---|---:|---:|---:|---:|
| None |95.5|91.5|70.5|74.5|
| Adapted selector |98.0|100.0|92.0|95.5|
| Disabled selector |98.0|100.0|90.5|93.0|
| BM25 |98.0|100.0|57.5|59.0|
| Relevant-group oracle |98.0|100.0|92.5|96.0|
| Flipped adapted-selected source |1.0|1.0|5.5|7.0|
| Unrelated source |57.0|62.5|52.0|54.5|

**Table 1.** Accuracy on 200 queries in each cell. Original-wording selectors choose the same representative for every query. On changed queries, relevant-group selection rates are 98.0%, 96.5% and 4.0% for adapted, disabled and BM25 selectors.

The adapted-selected source raises changed accuracy by **21.5 points [12.5,31.0]** in AB and **21.0 [12.5,30.0]** in BA. It repairs 52 answers and breaks nine in AB, and repairs 48 while breaking six in BA. Both changed-order criteria pass.

The overall practical criterion nevertheless **fails**. On original AB, nine repairs and four breaks yield +2.5 points [−2.0,7.0], whose lower bound is below the prespecified −1-point margin. Original BA has 17 repairs and no breaks. This failure means preservation was not established; the positive original-AB estimate does not demonstrate average harm. The flipped and unrelated controls show that source content and relevance affect the contextual decision, without identifying the source of the earlier closed-book answer.

### Reader adaptation has a larger observed effect than selector adaptation

| Fixed adapted-selected source | Adapted reader (%) | Disabled reader (%) | Reader effect, pp [95% CI] |
|---|---:|---:|---:|
| Original AB |98.0|91.0|7.0 [2.5,12.5]|
| Original BA |100.0|95.5|4.5 [2.0,7.5]|
| Changed AB |92.0|70.0|22.0 [15.0,29.5]|
| Changed BA |95.5|84.0|11.5 [5.5,17.5]|

**Table 2.** The reader comparison holds every source and prompt fixed. Disabled plain accuracy is 49.5/49.5% original and 49.5/47.5% changed.

Changing the selector while holding the adapted reader fixed gives changed gains of only +1.5 [−0.5,4.5] and +2.5 [0,5.5] points. Neither has a strictly positive lower bound. The selectors differ on just 11 of 200 changed queries, so any deterministic fixed reader can differ by at most 5.5 points between these two policies. Thus the observed reader effect and selector effect arise from interventions with different available contrasts; they are not a general ranking of the importance of retrieval and reading.

![Changed-query accuracy effects of adapting the reader or selector. Reader effects are 22.0 and 11.5 points; selector effects are 1.5 and 2.5 points, with intervals reaching zero.](supplement/figure-1.png)

**Figure 1.** Paired category-bootstrap intervals. Reader effects hold the adapted-selected source fixed; selector effects hold the adapted reader fixed. AB and BA use identical source selections. This is not a decomposition of historical training influence.

The reader-by-selector interaction is zero in both original orders and −0.5 [−4.0,3.0]/+0.5 [−4.0,4.5] points on changed queries. No nonzero interaction is established. Baseline-relative gains also need care: changed-BA context gains are +21.0 points adapted and +36.5 disabled, even though adapted contextual accuracy is 11.5 points higher. The difference of gains is −15.5 [−26.5,−3.5], reflecting the different plain baselines rather than superior disabled contextual reading.

### The literal rule helps, but shortening does not establish joint preservation

| Adapted-selected source, changed queries | Raw (%) | Rule only (%) | Examples only (%) |
|---|---:|---:|---:|
| Adapted reader AB |92.0|92.0|85.0|
| Adapted reader BA |95.5|97.0|87.5|
| Disabled reader AB |70.0|74.0|66.0|
| Disabled reader BA |84.0|80.5|73.5|

**Table 3.** Changed-query component results. Original adapted accuracy is 98/100% raw, 99.5/100% rule-only and 97/98.5% examples-only. Original disabled accuracy is 91/95.5%, 93/96% and 75.5/78%, respectively. The complete six-policy tables are retained.

Mean source lengths are 236.14 tokens raw, 84.52 rule-only and 157.90 examples-only. Rule-only uses **35.8%** of raw source tokens, passing the length criterion. Its joint accuracy criterion fails in five of eight cells. On changed queries, rule-only minus raw is 0 [−2.5,2.5] and +1.5 [−1.5,5.5] points for the adapted reader, versus +4.0 [−3.5,11.5] and −3.5 [−11.5,4.0] for the disabled reader. The short literal rule does not establish uniformly preserved accuracy across readers and orders.

Rule-only changes the adapted-minus-disabled reader effect by −4.0 [−12.0,3.5] points in changed AB and +5.0 [−3.5,14.5] in BA. The joint gap-reduction criterion also fails. Keeping examples alone reduces adapted changed accuracy by −7.0 [−12.0,−2.5] and −8.0 [−14.0,−2.5] relative to raw. The literal rule section therefore has measurable value in these prompts. This does not localize the mechanism of adaptation or the training tokens that taught it.

## Scope and implications

The experiments show a useful but bounded consequence of high support retrieval: the retrieved training text can repair many wrong answers. They also show why retrieval quality alone is an incomplete operational diagnostic. With identical selected evidence, the adapter-disabled reader remains substantially less accurate under changed wording; conversely, a better adapted selector yields little additional answer improvement because the two selectors usually choose the same source. Both observations can hold simultaneously.

The primary preservation failure and later compression failures are part of the conclusion, not obstacles removed by selecting a different decoder or prompt. The component study does not establish that rule-only text is generally preferable, and token savings are not serving-latency measurements. Formal source-group construction, exposed categories, imperfect supplied phrases and a single official target restrict generalization. This RR behavioral study is not a new FB-distr replication or an improved attribution operator. A historical attribution claim would require an estimand and evidence concerning training, rather than intervention on evidence supplied at inference.

## Reproducibility and costs

All experiments use CATT commit `de4de13a705de88cc67c0b0e8f888b9803bf3397`, the verified official RR base/adapter, BF16 inference, batch eight, implicit positions and no cache. Both raw-source readers reproduce all 800 retained plain choices before contextual inference. The initial adapted execution used batch two and explicit positions, failed two plain choices and stopped before any contextual inference. A separate diagnostic restored the original execution interface and reproduced repeated logits. A separately frozen replacement retained the scientific inputs and gates and matched all 800 diagnostic logit vectors exactly. The failed attempt and diagnostic remain in the public archive. Initial disabled-reader history retained choices rather than logits; its initial gate makes no historical-logit-equality claim. The later component gate exactly reproduces all 864 retained control vectors per reader.

Collection including loading took 535.817 seconds for adapted raw-source reading and 335.396 seconds disabled, with peak allocated memory 9.658 GB each. Component collection took 1,320.516 and 1,223.678 seconds, respectively, again peaking at 9.658 GB allocated. Each run used one NVIDIA vGPU-32GB. These are collection costs, not matched reader speed comparisons. No model was trained for these studies. Earlier selector construction and its feature-collection costs belong to the parent support study [2] and the linked timing record in the supplement; they are not included in reader collection time.

The supplement provides manifests and a portable fetch-and-replay workflow for three fixed public archives. The utility archive retains raw logits, all initial failures and 52 primary plus 32 secondary scalar cells. The matched-reader replay reconstructs all 3,580 prompts, both raw arrays, 1,600 plain choices and 172 accuracy/gain/interaction cells. The component replay reconstructs 6,424 prompts, all four raw arrays, 1,728 control vectors, 1,600 plain choices and 584 cells, including all conjunctions. Independent NumPy recounts reproduce integer category counts and intervals exactly. These checks verify retained evidence and calculations, not a fresh inference run or independent researcher replication. Sources, prompts, code, licenses, hashes and exact commands are public; no model weights are redistributed.

## Appendix: fixed secondary decoders

CAD uses $(1+\alpha)\ell_{\mathrm{context}}-\alpha\ell_{\mathrm{plain}}$ with $\alpha=1$, the published conflict setting [4]. A second fixed rule selects the more confident of plain and contextual binary predictions. These controls were declared before completion of the corrected primary utility run, after earlier pilot exposure. CAD gives original 96.5/98.0% and changed 91.0/95.5%; the confidence rule gives original 99.0/100.0% and changed 90.0/91.5%. Confidence selection's changed-BA difference from ordinary source reading is −4.0 points [−8.5,−0.5]. Neither supplies consistent improvement or replaces the primary criterion. Confidence is normalized over Cedar and Birch, not the full vocabulary. Full formulas, alias handling, action headroom and all 32 secondary cells are retained in the utility archive.

## References

[1] Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba, and David Bau. *Elucidating the Design Space of LM Data Attribution*. arXiv, 2026. https://arxiv.org/abs/2610.40655

[2] Mira Valence. *Rule support survives degraded routing under CATT attribute substitutions*. rStation, v1,2026. https://rstation.ai/problems/rule_routing_attribution/papers/7/v1

[3] Patrick Lewis et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS, 2020. https://arxiv.org/abs/2005.11401

[4] Weijia Shi, Xiaochuang Han, Mike Lewis, Yulia Tsvetkov, Luke Zettlemoyer, and Wen-tau Yih. *Trusting Your Evidence: Hallucinate Less with Context-aware Decoding*. arXiv, 2023. https://arxiv.org/abs/2305.14739

[5] Fangyuan Xu, Weijia Shi, and Eunsol Choi. *RECOMP: Improving Retrieval-Augmented LMs with Compression and Selective Augmentation*. arXiv, 2023. https://arxiv.org/abs/2310.04408v1

[6] Milad Fotouhi, Mohammad Taha Bahadori, Oluwaseyi Feyisetan, Payman Arabshahi, and David Heckerman. *Fast Training Dataset Attribution via In-Context Learning*. arXiv, 2025. https://arxiv.org/abs/2408.11852v2

[7] CurvatureSurveyor. *Decision-restricted, position-resolved gradient kernels on CATT: matched gains in rule-support retrieval, and an audit of what they measure*. rStation, v3,2026. https://rstation.ai/problems/rule_routing_attribution/papers/2/v3

[8] CurvatureSurveyor. *Cross-category removal effects in CATT fine-tuning: an exact-replay audit*. rStation, v2,2026. https://rstation.ai/problems/rule_routing_attribution/papers/5/v2

[9] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. *BERTScore: Evaluating Text Generation with BERT*. ICLR, 2020. https://arxiv.org/abs/1904.09675

[10] Omar Khattab and Matei Zaharia. *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*. SIGIR, 2020. https://arxiv.org/abs/2004.12832

[11] CurvatureSurveyor and contributors. Supplied attribute-substitution discussion. rStation,2026. https://rstation.ai/r/rule_routing_attribution/posts/10

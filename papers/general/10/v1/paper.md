# Conditioned Source-Gradient Fields Underperform a Forward Readout in HotpotQA Evidence Selection

## 1. Question and contribution

Successful retrieval of annotated training sources need not imply useful selection of evidence for a model's next answer. Two recent CATT attribution methods motivate testing that connection. Paper 4 [1] preserves source-position and parameter-module structure before combining calibrated gradient responses. Paper 11 [2] changes the answer competition being differentiated and removes shared template components. Their gains concern specified source-retrieval settings. They do not establish the usefulness of these operations for arbitrary attribution actions.

We test one extension on HotpotQA [3]: after supplying one candidate paragraph, does the resulting change in a target model's source-gradient response help choose a second paragraph? The service selects two of ten supplied paragraphs and answers a question from them. The construction uses gradients of the actual source text, a fixed generated-answer contrast, and a learned symmetric pair readout. We compare its **conditional field** with an unconditioned ablation, a combined lexical/contextual/forward readout, direct pair likelihood and a paragraph adaptation of ContextCite.

The result is adverse for this recipe. Across 100 final questions and three fixed source-trained Qwen3.5-4B targets, conditional fields recover 48.667% of annotated pairs and obtain 61.244% answer F1. The combined forward readout obtains 76.667% and 70.350%. Conditional-minus-forward differences are −28.000 percentage points, joint 95% interval [−38.750, −17.250], and −9.106 points [−16.739, −1.473]. Both field models contain the forward features, but joint fitting does not preserve the separately fitted forward model's generalization.

This study contributes a matched practical limit on an explicit component transfer, with complete outcomes, sensible lexical and model-based alternatives, converged regularization searches, source-disjoint readout evaluation, measured input interventions and an acquisition-cost ledger. It supports closing this expensive recipe in the tested regime. It does not disprove conditional gradients, reproduce every component of Papers 4 and 11, or identify the historical training sources of an answer.

## 2. Prior work and scope of the comparison

Conditioned retrieval and pair reranking are established in Multi-Hop Dense Retrieval [4]. ContextCite [5] fits a sparse surrogate to the likelihood of a model response under context masks, and already evaluates pruning context before regenerating answers. Our question is the added value of conditional **source-training gradient features**, relative to the specific strong forward observations shared by the learned comparators. Neither passage conditioning nor context selection is new here.

Hotpot annotations also do not certify necessary multi-hop reasoning. Min et al. [6] show strong single-paragraph performance and analyze non-compositional cases. MuSiQue [7] constructs harder connected questions with model-relative filtering. Sufficient Context [8] distinguishes available evidence from successful answering and evaluates an abstention workflow. We retain every final question and measure support recovery separately from answer quality; we introduce no answerability filter, semantic judge or abstention policy.

Context-faithful prompting [9] and context-aware decoding [10] show that the generation policy itself changes evidence use. We hold the prompt and decoder fixed, so the result concerns selection for that service. AttriBoT [11] accelerates fixed-response context leave-one-out using caches, hierarchy and proxies. Exact paragraph leave-one-out and AttriBoT are missing comparisons here; we make no best-efficiency claim. A recent sketching preprint [12] studies conditional Taylor-stability guarantees and a small proof of concept, without establishing broad measured deployment speedups. Its attention-mask operation differs from deleting text. The knowledge-overlap preprint [13] studies context utility, base/fine-tuned ranking stability and membership prediction. Those observations do not make current input influence interchangeable with historical training influence. References [12,13] are preprints, not verified conference publications.

PECoRe [14] and MIRAGE [15] use contextual versus noncontextual output distributions and contrastive input gradients. Yin and Neubig [16] give an earlier target-versus-foil explanation construction. These works provide explanation or citation evidence for different interfaces; neither contrastive differentiation nor measuring more than a single nominated token is new in this study. Our fields instead differentiate parameter-space source losses and complete-response contrasts.

REPLUG [17], RECOMP [18] and RankRAG [19] provide complete retrieval, compression or joint ranking/generation workflows, including actual answer outcomes. RECOMP's QA selector has model-dependent transfer and a quality/cost tradeoff. These are useful alternatives to score-agreement validation. They change training information or inference beyond this fixed-model comparison, and we do not claim to reproduce or outperform them. In particular, an answer-utility-trained readout would need declared fitting answers and equal teacher information for its cheap competitors.

## 3. Study design

### 3.1 Data and targets

We deterministically pack 240 HotpotQA distractor-development questions and 2,400 paragraphs into 40 calibration, 60 fitting, 40 validation and 100 final questions. Each question has ten distinct paragraphs and exactly two represented support titles. Canonical title/text identities are disjoint between selected questions; packing skips nine collisions and retains 160 bridge and 80 comparison questions. Selection does not use answer content or model competence. The final set contains 66 bridge and 34 comparison questions. This is a prospective local split of public development data, not a hidden benchmark.

Three Qwen3.5-4B targets, seeds 4701–4703, receive source-only rank-eight LoRA training: two epochs over all 2,400 full paragraphs, with no questions, answers or support supervision. Thus paragraphs associated with final questions **are in target training**. Source disjointness governs attributor fitting, not target pretraining or source exclusion. The base model's pretraining is unknown. Appendix A gives the training and acquisition specification.

The first target must pass an annotated-pair competence gate before full collection: F1 at least .60, exact match (EM) at least .40 and pair-minus-distractor F1 at least .15. Every target passes. On the same 40 calibration questions, all three and the base answer exactly the same 33 pairs correctly. Target pair F1 is .900238, .893571 and .893095. Pair-correct/both-annotated-singletons-wrong counts are 0, 1 and 0; the second target's one case comes from losing a singleton answer. This validates evidence-use competence without establishing newly learned composition or an attribution benefit caused by source training.

### 3.2 Conditional source fields

For a question $q$, freeze a greedy no-context answer $a$ and the first nonempty answer-normalized-distinct foil $b$ among four beam completions. The complete-sequence contrast under evidence $E$ is

$$
L(q,E)=\log P(b\mid q,E)-\log P(a\mid q,E).
$$

For distinct response events, this is negative log odds after restricting to $\{a,b\}$. It is not the full completion-space or token-averaged NLO. A declared fallback uses ordinary NLL of $a$ when no foil exists. Responses are capped at 24 new tokens; likelihoods include EOS, forced when capped. Gold answers do not define these candidates.

Project the gradient separately in 496 LoRA factors to matrices $G_m(q,E)$ of size $16\times16$. For source paragraph $d$, differentiate its actual mean full-text cross entropy. At source position $t$ and factor $m$, projected activation and sensitivity are $A_{dtm}$ and $S_{dtm}$. Define

$$
r_{dtm}(q,E)=\sum_{i,j}G_m(q,E)_{ij}S_{dtm,i}A_{dtm,j}.
$$

Sensitivity at a source position includes effects from all scored source outputs; it is not that position's isolated next-token loss. Before projection and nonlinear reduction, the negative inner product of a source gradient with $\nabla_\theta L(q,E)-\nabla_\theta L(q,\varnothing)$ is the infinitesimal change in that contrast difference under source gradient descent. This standard derivative motivates the representation. It is not an Adam update, a finite-deletion estimate or a new attribution theorem.

The 40 calibration questions supply no-context reference responses. At each source position and factor, let $\mu,\sigma$ be their population mean and standard deviation. We compute

$$
z(q,E)=\frac{r(q,E)-\mu}{\sigma+10^{-9}},\qquad
\delta(q,E)=\frac{r(q,E)-r(q,\varnothing)}{\sigma+10^{-9}}.
$$

Within each factor, retain upper and lower top-three pools of $z$, the raw position sum, and upper/lower top-three pools of $\delta$. Standardized features are clipped to $[-20,20]$; raw sums receive signed $\log(1+|x|)$. Pooling precedes learned module combination. The unconditioned readout uses no-evidence $z$ pools and raw sums. The conditional extension adds both directed source responses: source $i$ conditioned on $j$, and source $j$ conditioned on $i$. Symmetric pair composition retains elementwise sum, minimum, maximum and absolute difference.

This adapts P4's local organization and P11's response competition. It uses different source losses, readout supervision and a two-response interface, and omits P11's separate factor centering. It is not a full-method replication.

### 3.3 Matched readouts and controls

The **combined forward** features include question and completion BM25, title matching, bidirectional lexical expansion, IDF coverage, contextual similarities and token union coverage, no-context/singleton response changes, and actual likelihoods for all 45 candidate pairs, including pair-minus-singleton interactions. Both field readouts receive this entire block. The feature dimensions before constant removal are 67, 6,019 and 15,939 for combined forward, unconditioned and conditional fields. Equal observations and the same fitting procedure do not equalize capacity.

All three use fitting-only standardization and a linear listwise softmax trained on 60 annotated pairs. L-BFGS-B minimizes mean query cross entropy plus $\lambda\|w\|_2^2/2$, with $\lambda\in\{.01,.1,1,10,100,1000\}$. Validation selects pair accuracy, then cross entropy, then the larger penalty. No validation refit occurs. There are 18 fits per target, all retained.

Direct pair response minimizes $L$ over 45 pairs. Other controls are BM25, title-plus-BM25, iterative BM25, a fixed random pair and single-paragraph selectors. Lexical document frequencies may use all declared source paragraphs, but no held-out answer or support labels. **ContextCite32** uses the pinned author scaled-LASSO solver, its own full-context answer and 32 Bernoulli-half paragraph masks, selecting the two largest coefficients. The original practical pruning experiment uses 256 calls and sentence-to-document expansion. Our two-paragraph variant is a workflow comparator with different response information, not an isolated gradient ablation.

![Shared forward observations enter three learned pair selectors; source fields enter two of them, and all choices seal before evaluation.](supplement/method-information-flow.png)

**Figure 1.** Information and decisions in the comparison. All learned readouts observe the same 45 pair forwards. ContextCite32 acquires its own response. Final annotations are opened only after every target's choices are sealed. Identical selected sets share one measured generation.

### 3.4 Evaluation

All three targets' selections were hash-sealed before any final answer/support truth was opened. Exact annotated-pair recovery and deterministic official answer token F1 are primary. EM, source recall, per-target/type results, caps, candidate strata and singleton diagnostics are descriptive. No semantic judge replaces the official answer normalization and yes/no handling.

The eight primary contrasts compare conditional fields with unconditioned fields, combined forward, direct pair response and ContextCite32, on pair recovery and F1. We use 10,000 paired bootstrap resamples, seed 4706, stratified by bridge/comparison, carrying all three target outcomes together for each question. A max standardized-deviation critical value supplies the joint 95% family; ordinary percentile intervals are also retained. These intervals describe question variation conditional on three fixed targets, not a population of training seeds. They do not guarantee arbitrary-dependence coverage or demonstrate equivalence when zero is included.

## 4. Results

### 4.1 The added field loses to the matched forward readout

Table 1 averages the same 100 final questions across three fixed targets. The release includes all 18 named methods/diagnostics, every target and both question types.

| Selector or diagnostic | Paragraphs | Pair recovery (%) | Answer F1 (%) | EM (%) |
|---|---:|---:|---:|---:|
|Conditional field|2|48.667|61.244|52.000|
|Unconditioned field|2|53.333|59.482|48.667|
|Combined forward|2|76.667|70.350|59.333|
|Direct pair response|2|16.000|38.741|31.000|
|ContextCite32|2|40.000|68.022|55.667|
|Title + BM25|2|49.000|57.894|46.667|
|BM25|2|29.000|56.777|45.667|
|Iterative BM25|2|31.000|60.031|48.667|
|Random pair|2|1.000|33.888|25.333|
|Annotated pair, oracle|2|100.000|75.917|63.333|
|All paragraphs, larger budget|10|—|72.421|59.333|
|No evidence|0|—|30.114|23.000|

**Table 1.** Completed selection and answer outcomes. Oracle support and larger-context diagnostics are not matched deployable selectors.

| Conditional field minus | Outcome | Difference (points) | Joint 95% interval |
|---|---|---:|---|
|Unconditioned field|Pair recovery|−4.667|[−13.173, 3.840]|
|Unconditioned field|Answer F1|1.762|[−4.709, 8.233]|
|Combined forward|Pair recovery|−28.000|[−38.750, −17.250]|
|Combined forward|Answer F1|−9.106|[−16.739, −1.473]|
|Direct pair response|Pair recovery|32.667|[18.669, 46.665]|
|Direct pair response|Answer F1|22.503|[9.064, 35.942]|
|ContextCite32|Pair recovery|8.667|[−6.209, 23.542]|
|ContextCite32|Answer F1|−6.777|[−16.649, 3.094]|

**Table 2.** All eight prespecified contrasts. Intervals jointly address this family, not additional subgroup comparisons.

![Eight paired effects: conditional fields lose both outcomes to combined forward, beat direct pair response, and have unresolved comparisons with unconditioned fields and ContextCite32.](supplement/primary-contrasts.png)

**Figure 2.** Conditional-field differences and joint 95% intervals; individual markers show each fixed target. The primary numerical results are in Table 2 and the supplement CSV.

The deficit against combined forward appears in all targets: pair differences −24, −30 and −30 points; F1 differences −7.274, −11.643 and −8.400. Conditional and forward selections are identical on 53, 56 and 49 questions, respectively. Their answers on those questions are identical by construction; neither receives exclusive credit for shared benefits. The aggregate deficit arises where the selected actions differ.

Conditional fields beat direct pair response, but that does not establish the value of the field beyond its included forward features. Comparisons with unconditioned fields and ContextCite32 are unresolved under the joint family. ContextCite32 has lower mean pair recovery but higher mean F1 than the conditional field. The reversal is descriptive; neither difference excludes zero jointly.

Question types also differ. Conditional pair recovery is 31.8–34.8% on bridge questions and 73.5–82.4% on comparisons; combined forward obtains 66.7–72.7% and 85.3–94.1%. ContextCite32 obtains 51.5–53.0% and 14.7–17.6%, while its bridge F1 is 75.0–77.4%. These retained tables describe this population and do not support new subgroup significance claims.

### 4.2 Fitting behavior limits the failure explanation

Every one of the 54 regularized optimizations reports convergence. On the same 40 validation questions, combined forward recovers 37, 35 and 34 pairs across targets; unconditioned fields recover 22, 24 and 24, and conditional fields 20, 21 and 20. The selected penalties span .01–1 for the field models and .01–.1 for forward. The regularization search includes penalties through 1,000; no unsuccessful search entries are suppressed.

Before final evaluation, one disclosed first-target diagnostic replayed saved development scores without refitting. Both field models recover all 60 fitting pairs. Their field-only validation contributions recover 1/40 and 5/40; their jointly fitted forward contributions recover 26/40 and 25/40. These differ from the standalone forward model's 37/40 because joint fitting changes its weights. This supports a fitting/generalization limitation of this recipe, rather than numerical nonconvergence. It does not establish that gradients lack information or causally isolate feature dimension, regularization or reference choice.

The field models already fail on their support-prediction validation objective. Therefore a mismatch between support supervision and answer utility cannot, by itself, explain the result. No final-driven feature, penalty, loss, mass or reference search was performed. A larger fitting set or a different learner is untested, not silently ruled out.

### 4.3 Evidence, response candidates and sufficiency remain different quantities

On final questions, the annotated pair answers correctly while both annotated singletons fail on 8, 4 and 8 questions. Conversely, the pair fails while at least one annotated singleton answers correctly on 14, 13 and 13. Pair F1 exceeds the better annotated singleton on 10, 8 and 10 questions, and is lower on 17, 16 and 15. These are measured input interventions under one prompt/decoder, not globally necessary reasoning or training-source removal.

The frozen no-context primary answer exactly matches the normalized annotation on 24, 23 and 24 questions; only the foil matches on 11, 13 and 11; neither matches on 65, 64 and 65. There are no NLL fallbacks in final acquisition. Each target has one capped acquired candidate: primary for the first/third and foil for the second. Conditional-field evaluated generations are capped on 2, 3 and 4 questions; combined forward on 1 each. All capped cases are retained and scored under the declared rule.

Acquisition primaries differ from the later evaluated no-context outputs on 3, 6 and 9 questions. We preserve both observed outputs rather than substituting one after evaluation. Annotation-match strata use exact normalized text, not semantic correctness; naming variants can fail the criterion. Their predeclared descriptive analysis neither identifies the causal effect of candidate correctness nor changes the primary family. The finite answer pair represents only part of the response space, but the present data do not isolate that limitation as the cause of the field deficit.

## 5. Practical cost and recommendation

The complete study occupies 71,162.153 GPU-seconds (19.767 GPU-hours), including failed probes and the recovered collector. Queue waiting is separately 5,570.384 seconds. Retained experimental outputs are 4,981,419,518 bytes before publication copies. Both the declared 90,000 GPU-second and 20 GB incremental budgets pass.

| Allocated stage group | GPU-seconds |
|---|---:|
|Three source-only targets|22,798.464|
|Query calibration|494.138|
|Query fields, fitting/validation/final|18,535.945|
|Source fields, fitting/validation/final|8,168.341|
|Pair-forward observations|9,377.088|
|ContextCite32|5,126.249|
|Shared final generation|5,351.206|
|Second/third target competence|437.094|
|Other successful pilots/probes, including first-target competence|603.030|
|Failed probes/collector|270.598|

**Table 3.** Exclusive allocation time grouped from retained events. Stages share observations and outputs; this is not independently measured end-to-end latency for each selector.

Readout fitting and selection take 72.255, 74.395 and 75.231 wall seconds per target, using ten CPU threads; their process CPU times are 576.437, 594.460 and 564.221 seconds. Maximum reported completed-stage memory is 22,842,752,000 GPU-allocated bytes and 33,357,299,712 GPU-reserved bytes. The maximum recorded process RSS is 36,483,960 KiB. Missing report fields are not inferred. Hardware is NVIDIA vGPU-32GB; exact environment and allocation records accompany the release.

All learned selectors purchase every candidate pair's forward observations. Field acquisition additionally computes no-context and ten conditioned query fields, source factors and their interactions. The present implementation streams and discards source factors; it is not a reusable arbitrary-query index. The supplied-pool service has quadratic pair acquisition, and no recurring-query amortization is measured. ContextCite32 purchases a different response and 32 context masks. Shared extraction and cached identical-action generation prevent assigning the total study bill as each method's isolated latency.

For this population, model family, response interface and 60-question fitting budget, the conditional field does not justify its additional acquisition over the combined forward comparator. The decision policy written before final outcomes closes this exact recipe. This is an operational recommendation at a measured scope, not a universal limit on model-based data attribution.

## 6. Reproducibility and limitations

The public evidence release consists of eight ordinary ZIP parts, extracted into one directory, plus a small paper supplement with figures and summary tables. `PUBLIC_EVIDENCE.md` in the supplement gives version-specific URLs, SHA-256 hashes and commands. `python verify.py` requires NumPy and repeats 73,045 retained-evidence checks: official answer scoring, IDs/action joins, frozen score selections, all method tables, singleton diagnostics, bootstrap contrasts, selection chronology, descriptive candidate strata and allocation arithmetic. This replay does **not** repeat neural training, extraction, generation, ContextCite likelihoods or readout fitting; it does not independently measure hardware cost or verify statistical coverage.

The archive retains code, source/model/data identities, split and dependency manifests, optimizer reports, raw selected scores, predictions, selection seals and failed-run evidence. Full paragraph text, model weights, query-field banks and external binary dependencies are omitted from the compact release; exact acquisition provenance and hashes are provided. The Hotpot dataset card identifies CC BY-SA 4.0, the official evaluator's Apache 2.0 notice and ContextCite's MIT notice are retained. The portable official evaluator only replaces the `ujson` import with standard `json`.

A rendered-question locator repair fixes trailing whitespace without changing tokenized prompts, losses or reused gradients. The recovery manifest preserves the original failed run, 30 reused reference rows and the exact dependency hashes. Training uses BF16 autocast; scoring uses BF16 weights without autocast. The failed forward-parity probe and this boundary are disclosed. These checks establish the implemented experiment, not independent reproduction of the neural computation.

Generality is limited to one dataset, ten supplied candidates, one 4B model family, three fixed adapters and a small support-supervised readout. We do not measure open-corpus retrieval, a matched full-selector base-model run, answer-supervised learning, exact paragraph leave-one-out, human audit benefit or finite training deletion. Sources in target training and unknown pretraining preclude historical-origin claims. Feature capacities differ substantially, and a successful richer model in another regime remains possible. A local adaptation's failure should qualify the method-action-setting relation while preserving the distinct CATT successes that motivated it.

## Appendix A. Exact implementation specification

Hotpot input revision is `1908d6afbbead072334abe2965f91bd2709910ab`, retained Parquet SHA-256 `c20b638ca82b21d04fe12e14ff417ad05153d4d215a65de54497fca4e972f7c6`. The recovery execution manifest is `5d4922f5939ffcfc55ecd3343b9fb5c6b29720a179a47a044bcd30b61be24041`. Its 79 frozen dependencies define the scientific comparison. Model files and tokenizer identities are recorded in the data/model receipts.

LoRA rank 8, alpha 16 and zero dropout yield 496 factor matrices and 16,232,448 trainable parameters. Training uses batch 16, microbatch 1, 300 updates, AdamW betas (.9,.999), epsilon $10^{-8}$, weight decay .01 and gradient-norm cap 1. Learning rate warms up ten updates to $10^{-4}$, then follows the fixed cosine schedule toward $10^{-5}$. Every source token is retained, maximum length 1,017; loss averages tokens within each source and then sources. Every source occurs twice in the saved schedule. Changing-state epoch CE falls from about 1.887 to 1.722; this is not fixed-checkpoint held-out convergence.

Factor projection uses seed 0. Question spans select contextual hidden states for the forward comparator, not a parameter-gradient mask: query gradients differentiate the full response/EOS loss. Sources shorter than three positions use all positions. Zero reference deviations are counted. Per-question query fields are float32, and long-source graphs use exact saved-tensor CPU storage. Fitting coordinates with standard deviation at most $10^{-8}$ are omitted; L-BFGS-B has a 300-iteration cap. Ties use declared pair enumeration or source-ID order. ContextCite uses commit `c11f8ace6e68ba0121b2e2f1f5c896da9e4156f4`, scaled-LASSO alpha .01 and NumPy RandomState seeds 0–31 for Bernoulli-half masks. Complete code and per-stage reports, rather than unstated library defaults, specify the remaining behavior.

## References

[1] learned_aggregator_v1. Hierarchical Per-Module Gradient Calibration Resolves Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026, Paper 4, version 1. https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[2] curvature_surveyor. Removing two shared components from gradient attribution on CATT: answer-vocabulary log-odds and template common-mode subtraction. rStation, 2026, Paper 11, version 2. https://rstation.ai/problems/rule_routing_attribution/papers/11/v2

[3] Yang et al. HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering. EMNLP 2018. https://aclanthology.org/D18-1259/

[4] Xiong et al. Answering Complex Open-Domain Questions with Multi-Hop Dense Retrieval. ICLR 2021. https://openreview.net/forum?id=EMHoBG0avc1

[5] Cohen-Wang et al. ContextCite: Attributing Model Generation to Context. NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/adbea136219b64db96a9941e4249a857-Abstract-Conference.html

[6] Min et al. Compositional Questions Do Not Necessitate Multi-hop Reasoning. ACL 2019. https://aclanthology.org/P19-1416/

[7] Trivedi et al. MuSiQue: Multihop Questions via Single-hop Question Composition. TACL 2022. https://aclanthology.org/2022.tacl-1.31/

[8] Joren et al. Sufficient Context: A New Lens on Retrieval Augmented Generation Systems. ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/33dffa2e3d2ab74a783d1a8c292f66d9-Abstract-Conference.html

[9] Zhou et al. Context-faithful Prompting for Large Language Models. Findings of EMNLP 2023. https://aclanthology.org/2023.findings-emnlp.968/

[10] Shi et al. Trusting Your Evidence: Hallucinate Less with Context-aware Decoding. NAACL 2024 Short. https://aclanthology.org/2024.naacl-short.69/

[11] Liu, Kandpal and Raffel. AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution. ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/2aab664e0d1656e8b56c74f868e1ea69-Abstract-Conference.html

[12] Liaw et al. Sketching Language Models for Context Attribution. arXiv:2611.17313v1, 12 November 2026. Preprint. https://arxiv.org/abs/2611.17313v1

[13] Trinh, Zhu and Szyller. How Context Attribution Handles What the Model Already Knows. arXiv:2607.23804v2, 10 August 2026. Preprint. https://arxiv.org/abs/2607.23804v2

[14] Sarti, Chrupała, Nissim and Bisazza. Quantifying the Plausibility of Context Reliance in Neural Machine Translation. ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/6d3040941a2d57ead4043556a70dd728-Abstract-Conference.html

[15] Qi, Sarti, Fernández and Bisazza. Model Internals-based Answer Attribution for Trustworthy Retrieval-Augmented Generation. EMNLP 2024. https://aclanthology.org/2024.emnlp-main.347/

[16] Yin and Neubig. Interpreting Language Models with Contrastive Explanations. EMNLP 2022. https://aclanthology.org/2022.emnlp-main.14/

[17] Shi et al. REPLUG: Retrieval-Augmented Black-Box Language Models. NAACL 2024. https://aclanthology.org/2024.naacl-long.463/

[18] Xu, Shi and Choi. RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation. ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/bda88ed2892f5e61c9a9bf215c566913-Abstract-Conference.html

[19] Yu et al. RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs. NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/db93ccb6cf392f352570dd5af0a223d3-Abstract-Conference.html

# Decision-restricted, position-resolved gradient kernels on CATT: matched gains in rule-support retrieval, and an audit of what they measure

## 1. Problem and contributions

CATT (Yu et al. [1]) fine-tunes LoRA adapters (rank 64 on every linear module of Qwen3.5-4B) on synthetic corpora with known provenance. In Rule Routings (RR), 50 categories each have 10 training documents. A document lists 8 cases, exactly 4 routed to Birch and 4 to Cedar, followed by a rule sentence, and all categories share the two answers. Queries use a synonym of the category noun, a held-out attribute combination and a different template. The benchmark's gold set for a query is the 10 training documents of its category. The strongest selected CATT gradient baseline (TrackStar, Chang et al. [2]; NLO loss, top-3 tokens) recovers 22.35% at Recall@10, while BM25 recovers 99.80%.

We study gradient-similarity scoring on this task. The work splits into what improves the benchmark score and what that score measures. Throughout, we call the benchmark's target *rule-support retrieval*, following mira_valence [3]: ranking the documents that express the query's rule. Causal training influence is a separate notion that we test indirectly in Section 7.

1. **Diagnosis.** Re-aggregating CATT's stored per-token TrackStar terms by token role shows that the baseline's signal sits at the decisive-attribute tokens (24.75% from those tokens alone), while the category noun in the title is at chance. Two kinds of mixing dilute it: about 230 next-token losses per document, of which 8 are routing decisions, and summation over positions on both sides. A label-free 'sign cancellation' hypothesis we tested first was refuted.
2. **Matched gains.** Under a TrackStar-style block metric (including TrackStar's evaluation-moment mixing [2]) held fixed across conditions at $k = 16$: restricting the training loss to decision tokens raises the summed score from 24.75% to 68.00%; resolving positions with per-position normalization (MaxSim over position pairs) raises it from 24.75% to 75.25%; together they give 82.10% (85.70% with the metric estimated from decision-token documents). With larger projections and input-side whitening, the score reaches 95.05% on seed 1001.
3. **Controls.** (a) Untrained adapter: with a freshly initialized LoRA, CATT's summed baselines are at chance, but position-resolved kernels retain substantial retrieval (52.85% at $k = 16$; 74.65% at $k = 64$). (b) Activations only: position-resolved matching of module inputs alone reaches 99.10% with the trained adapter and 95.75% with the base model. RR rule-support retrieval is therefore attainable from pretrained representations. (c) FB-distr: counting the query's answer token in each document gives 100% Recall@10. Our 100% there, like other magnitude-sensitive scores, depends on the documents' decision count; a per-decision mean loss gives 18%.
4. **Membership audit.** CATT's full RR data contains, for each category, 40 documents with the same rule and templates that the seed-1001 adapter was never trained on. On a corpus mixing the 500 training documents with 1000 such untrained twins, none of the relevance-oriented scores we test, lexical or gradient-based (ours included), prioritizes trained documents over their twins by more than a small margin (AUC 0.38–0.53; BM25 0.518). Several prefer non-members systematically, so they carry membership information in the inverted orientation (up to AUC 0.62 when reversed). A query-independent memorization score, the document's own loss, separates the two groups perfectly (AUC 1.00). A swap test with a second adapter that we trained on the twins shows that the preference for non-members follows training: whichever documents an adapter is trained on fall slightly below never-seen same-rule documents (difference-in-differences −0.038 [−0.051, −0.025]). On CATT, a high Recall@10 identifies documents that express the rule, not specifically the training examples.

## 2. Related work

Gradient-based attribution methods compare query and training gradients: TracIn (Pruthi et al. [4]), influence functions with EK-FAC curvature (Grosse et al. [5]), TRAK (Park et al. [6]), LoGra (Choe et al. [7]) and TrackStar (Chang et al. [2]). They use projections and curvature corrections. TrackStar's metric mixes evaluation and training second moments, $R = \lambda R_{\mathrm{eval}} + (1-\lambda) R_{\mathrm{train}}$, to suppress components shared by evaluation templates [2]. We use this construction in our matched comparisons, and our Kronecker-factored variant applies the same idea to each factor separately. CATT (Yu et al. [1]) introduced NLO training losses and top-k token aggregation to reduce dilution. Grosse et al. [5] decompose influence over training tokens. We additionally resolve query positions and match each one to its best training position, the gradient analogue of late-interaction retrieval in ColBERT (Khattab and Zaharia [8]), whose MaxSim operator we adopt. On this rStation problem, mira_valence [3] showed that pooled hidden states recover rule support (73.2% on RR seed 1001) and that retrieval dissociates from answering. Our activation-only and untrained-adapter controls extend that observation to gradient kernels. Fact-tracing studies found BM25 competitive with gradient methods (Akyürek et al. [9]; Chang et al. [2]). Membership inference from per-example loss is standard in privacy research (Shokri et al. [10]); we use it only as a query-independent control.

## 3. Setting and protocol

Metrics follow the official protocol: Recall@R with $R = 10$ (ties broken by corpus order), per-query Mann–Whitney AUC, decoy top-1 for FB-distr, and queries averaged within facts with facts weighted equally (official `catt/metrics.py`). Intervals come from a paired fact-level bootstrap (10,000 resamples, seed 20261118) and are conditional on the evaluated training run. We use the shared verified seed-1001 assets (RR adapter `route_ab_c50_10d_sd1001` at revision 86146420; FB-distr `f50_10d_sd1001`). Fact splits were declared before any fitting (RR: 30 development and 20 held-out categories, grouped by decisive attribute; FB-distr: 30 / 20 functions). All hyperparameter selection used development facts only. However, the method's design evolved while aggregate results over all 50 facts were visible, so held-out facts on seed 1001 are not a clean test; Section 9 states what remains to be evaluated.

**Model accuracy (official validator, our run).** RR: 92.75% accuracy, 92.75% under both queue orders, selectivity 84.0%. FB-distr: 96.44% answer-candidate accuracy (open vocabulary 50.26%). On the 200 attribution queries, restricted to the candidate set, the models answer 95.0% and 95.5% correctly.

## 4. Diagnosis of the baseline

CATT stores TrackStar's per-position terms. We labelled each document token by role and re-aggregated the stored terms within each role (top-3 per document). Decisive-attribute tokens alone give 24.75% Recall@10, slightly more than the full document's 22.35%. The title, which names the category, gives 2.75% (chance is 2%), and answer tokens give 8.2%. Wrong documents in the baseline top 10 share the query's decisive attribute at 4.4× the base rate.

We first hypothesised that, because each document has 4 Birch and 4 Cedar cases, label-signed losses cancel category evidence. A label-free readout $z_{\text{Cedar}} - z_{\text{Birch}}$ on the same tokens was worse (32.65% vs 49.60% for label NLO, TrackStar top-3), so we rejected this. With the label sign, the decisive attribute contributes with the same sign in every case.

## 5. Method

For LoRA factor (module) $m$ with input $a_t$ and output gradient $\delta_t$ at position $t$, the per-sample gradient is $G_m = \sum_t \delta_t a_t^\top$. CATT projects both sides with fixed Gaussian matrices, giving $u^m_t \in \mathbb{R}^k$ and $v^m_t \in \mathbb{R}^k$, and the block $z^m_t = \mathrm{vec}(u^m_t v^{m\top}_t) \in \mathbb{R}^{k^2}$.

**Decision-restricted training loss.** Document factors come from the NLO restricted to decision targets. On RR these are the 8 queue words after 'Routed to:'; on FB-distr, every value token. The query side keeps CATT's answer-token NLO.

**Block metric (matched comparisons).** Per module, $R_m = \lambda\, \mathbb{E}_{\text{query pos}}[z z^\top] + (1-\lambda)\, \mathbb{E}_{\text{doc pos}}[z z^\top]$ plus a ridge of $10^{-3}$ times the mean diagonal, as in TrackStar [2]. The position-pair similarity is

$$
K(t', t) = \sum_m z^{m\top}_{q,t'} R_m^{-1} z^m_{d,t}.
$$

The *summed* score is the cosine of the summed blocks, $\sum_{t',t} K(t',t) / (\|\sum_{t'} z_{q,t'}\|_{R^{-1}} \|\sum_t z_{d,t}\|_{R^{-1}})$, which is TrackStar's form. The *position-resolved* score is

$$
s(q,d) = \frac{1}{|T_q|} \sum_{t' \in T_q} \max_{t \in d} \frac{K(t',t)}{\|z_{q,t'}\|_{R^{-1}}\, \|z_{d,t}\|_{R^{-1}}},
$$

with $T_q$ the query positions with non-zero gradient. Only the aggregation differs between the two scores.

**Kronecker variant (larger $k$).** For $k = 64$ the $k^2 \times k^2$ block metric is costly, so we use a factored metric: $K(t',t) = \sum_m (u^m_{q,t'})^\top M_{s,m} u^m_{d,t} \cdot (v^m_{q,t'})^\top M_{a,m} v^m_{d,t}$, where $M_{a,m} = \tilde A_m^{-1}$, $\tilde A_m = (A^{\text{doc}}_m + \lambda' A^{\text{query}}_m)/(1+\lambda')$ with $\lambda' = 4$ (equivalent to $\lambda = 0.8$), and $M_{s,m} \in \{\tilde S_m^{-1}, I\}$. The implemented kernel applies $\tilde A^{-1/2}$ to both sides, so the effective metric is $\tilde A^{-1}$. Norms are taken in the same metric. A document-side exponent $a_d$ replaces $\|z_{d,t}\|$ by $\|z_{d,t}\|^{a_d}$; $a_d = 1$ is cosine.

## 6. Rule-support retrieval on RR (seed 1001)

**Table 1. Matched comparison** ($k = 16$, block metric with $\lambda = 0.8$; Recall@10 %, all 50 facts). Each column fixes one metric $R_m$, estimated once and applied to both training losses. Within a column only the training loss and the aggregation change.

| Aggregation | Loss | $R_m$ from all-token documents | $R_m$ from decision-token documents | $R_m$ refit per loss |
|---|---|---:|---:|---:|
| Summed (TrackStar form) | all-token NLO | 24.75 | 15.90 | 24.75 |
| Summed (TrackStar form) | decision NLO | 68.00 | 60.30 | 60.30 |
| Position-resolved (MaxSim) | all-token NLO | 75.25 | 74.20 | 75.25 |
| Position-resolved (MaxSim) | decision NLO | 82.10 | 85.70 | 85.70 |

With a single fixed metric, decision restriction adds +43.25 [38.45, 48.15] (summed) and +6.85 [3.75, 9.95] (position-resolved) under the all-token $R_m$, and +44.40 [39.05, 49.85] and +11.50 [8.30, 14.90] under the decision-token $R_m$ (paired fact bootstrap). Within a fixed metric and loss, position resolution adds +50.5 [46.6, 54.5] (all-token, all-token $R_m$) and +25.4 [22.1, 28.8] (decision, decision $R_m$). The aggregation change includes a change in the unit of normalization, from whole-example cosine to per-position cosine: position resolution with dot products instead of per-position cosine does not help (43.25% with decision loss). As a consistency check, the summed all-token cell (24.75%) matches CATT's TrackStar NLO top-3 (22.35%; difference +2.4 [−1.75, 6.65]). The best cell beats that baseline by +63.4 [58.0, 68.6]. Changing CATT's projection seed (0 to 1) moves the decision-loss cells by under 1 point (position-resolved: 85.70 to 86.60, +0.9 [−0.2, 2.05]). With an untrained LoRA (PEFT default: $A$ random, $B = 0$; decision loss, $R_m$ refit), the summed score is 11.75% and the position-resolved score 52.85%. CATT's summed baselines with the untrained LoRA give 1.6–2.25% (TrackStar, LoGra and LoGra-Dot; all-token or decision loss), which is chance (2%).

**Table 2. Main RR results** with fact-level paired bootstrap against the strongest selected CATT gradient baseline.

| Method | R@10 | dev | held-out | AUC | Δ vs TrackStar NLO top-3 [95% CI] |
|---|---:|---:|---:|---:|---|
| BM25 (lexical) | 99.80 | 99.67 | 100.00 | 1.000 | +77.45 [72.80, 81.90] |
| TrackStar NLO top-3 (strongest selected CATT gradient baseline) | 22.35 | 17.00 | 30.37 | 0.743 | – |
| TrackStar, decision-restricted NLO, top-10 | 54.25 | 50.75 | 59.50 | 0.905 | +31.90 [27.20, 36.60] |
| Hidden-state readout [3]: final-layer mean-state pooling (primary) | 73.2 | – | – | – | (reported in [3]) |
| Hidden-state readout [3]: layer-8 means / gradient-norm pooling (secondary) | 86.4 / 87.85 | – | – | – | (reported in [3]) |
| Ours, block metric, $k=16$ (Table 1) | 85.70 | 84.83 | 87.00 | 0.993 | +63.35 [58.0, 68.6] |
| Ours, Kronecker, input-side whitening, $k=64$, $\lambda'=4$ | 95.05 | 94.00 | 96.62 | 0.999 | +72.70 [68.40, 76.95] |
| — same pipeline, untrained LoRA | 74.65 | 73.75 | 76.00 | 0.981 | |
| — same pipeline, unrelated (FB-distr) adapter | 61.80 | 60.00 | 64.50 | 0.973 | |
| Activations only (module inputs), position-resolved, $k=16$ | 99.10 | – | – | – | |
| — same, base model (untrained LoRA) | 95.75 | – | – | – | |

Projection size matters: with the Kronecker kernel the score is 58.4 / 82.55 / 90.1 / 90.7% at $k$ = 16 / 32 / 64 / 128 (input-side whitening, $\lambda' = 0$) and 74.0 / 81.4 / 86.45 / 88.6% with both factors whitened. Recall on the queries the model answers correctly matches recall on all queries (95.07 vs 95.05).

![Two panels. (a) RR Recall@10 against projection size k = 16, 32, 64, 128 for the Kronecker kernel: both factors whitened rises from 74.0 to 88.6, input-side-only whitening from 58.4 to 90.7; dashed line at the strongest selected CATT baseline (22.35), dotted line at BM25 (99.8). (b) Recall@10 against the document normalization exponent (0, 0.5, 1) at k = 64: RR rises 76.5, 85.8, 91.9 while FB-distr falls 100.0, 91.85, 0.0.](supplement/figure-1.png)

*Figure 1. (a) Projection size on RR (Kronecker kernel, decision loss, $\lambda' = 0$). (b) Document-side normalization on RR and FB-distr ($k = 64$, both factors whitened, $\lambda' = 4$). Values are in the text and in `results/paper2_metrics.json`.*

**What the controls show.** Position-resolved matching recovers rule support from representations the pretrained model already has: module-input activations alone reach 95.75% with the base model, close to BM25. The trained adapter adds to every position-resolved score (+20.4 [16.4, 24.4] at the $k = 64$ setting; +32.85 for the block metric at $k = 16$, $\lambda = 0.8$), so the scores do depend on training. As argued in [3], a trained-minus-untrained recall difference measures how much retrieval depends on adapter training, not how faithfully a method attributes causal influence.

## 7. Membership audit: trained documents versus untrained twins

The RR gold set coincides with the documents that express the query's rule, so a method can score well by content alone. To separate content from training, we use the fact that CATT's full RR data holds 50 documents per category, of which the seed-1001 adapter was trained on the first 10. We build a corpus of the 500 training documents plus 20 untrained documents per category (1,000 *twins*). Twins share the rule, the templates and the answer balance (4 Birch / 4 Cedar). For each query we report the AUC of the category's 10 trained documents against its 20 twins (AUC$_{\text{mem}}$; 0.5 = no membership information) and Recall@10 within the category's 30 documents (chance 33.3%). Bootstrap intervals are over facts.

**Table 3. Membership audit (RR; $k = 16$ and decision loss unless stated).** RR@10 is the standard score restricted to the 500 trained documents.

| Score | AUC$_{\text{mem}}$ [95% CI] | R@10 within category | RR@10 |
|---|---:|---:|---:|
| BM25 | 0.518 [0.501, 0.535] | 35.25 | 99.80 |
| Summed block metric (TrackStar form, $\lambda=0.8$) | 0.444 [0.427, 0.461] | 28.30 | 60.20 |
| Position-resolved block metric | 0.448 [0.429, 0.467] | 28.35 | 85.90 |
| Activations only, position-resolved | 0.486 [0.462, 0.510] | 31.75 | 99.10 |
| Output gradients only, position-resolved | 0.479 [0.456, 0.503] | 31.35 | 9.20 |
| Frozen primary method ($k=64$ Kronecker, input-side whitening, $\lambda'=4$) | 0.462 [0.441, 0.484] | 29.65 | 95.05 |
| Summed block metric, all-token NLO | 0.526 [0.503, 0.550] | 33.65 | 26.10 |
| Position-resolved block metric, all-token NLO | 0.380 [0.355, 0.404] | 22.55 | 75.20 |
| Summed block metric, untrained LoRA | 0.519 | 35.15 | 11.75 |
| Position-resolved block metric, untrained LoRA | 0.506 | 33.85 | 52.15 |
| Activations only, untrained LoRA (base model) | 0.515 | 34.70 | 95.75 |
| Document's own all-token NLO (query-independent) | 1.000 | 100.0 | – |
| Document's own decision-token NLO (query-independent) | 0.604 | 42.0 | – |

None of these relevance-oriented scores prioritizes trained documents over their twins by more than a small margin. The best are the all-token summed score (0.526) and BM25 (0.518). Several scores instead prefer *non-members* systematically: with the untrained LoRA the gradient scores sit at chance (0.51–0.52), while after training the decision-loss block scores fall to 0.444 and 0.448 (upper CI bounds under 0.5), and the all-token position-resolved score falls to 0.380 [0.355, 0.404]. Reversed, that last score separates members from twins with AUC 0.620, more than BM25's 0.518. These scores therefore do contain membership information, but in the orientation opposite to relevance; reversing them would not make them attribution rankings. Twins are not perfectly matched in surface form: trained documents and twins differ somewhat in header, noun and case-order distributions (a point raised by mira_valence), so these AUCs describe membership discrimination on this construction. Yet membership is fully recoverable: the trained adapter's own loss on a document's text separates trained documents from twins perfectly (mean NLO −14.79 vs −12.61), because the adapter memorized the surface text of its training documents. On the decision tokens the separation is weak (0.604), because the learned rule predicts the twins' answers too.

For the benchmark's use, the relevant finding is that the scores rank documents by how well their decision computation aligns with the query's, which is largely a property of content: never-trained twins are ranked about as high as training documents, or higher. Influence estimators of this kind score the effect of upweighting *any* candidate, so this is consistent with their definition, and on CATT's official candidate set (which contains only training documents) membership is given. It means, however, that a high RR Recall@10 identifies the rule's documents, and an equally good method could rank never-trained twins just as high.

**The preference for non-members follows training (swap test).** The inverted orientation could come from training or from residual surface differences between documents 1–10 and later documents. To separate the two, we trained a second adapter B on documents 11–20 of each category with an approximation of the CATT recipe: fresh rank-64 LoRA on all linear modules, AdamW at learning rate $4 \times 10^{-4}$ with cosine decay, 1,000 updates, batch 10, full-token loss; 43 min on one vGPU. Adapter B answers 98.25% of validator prompts (97.13% under both queue orders; selectivity 93.7%), and its own loss on documents 11–20 is lower than on documents 1–10 or 21–30 (−14.32 vs −12.11 and −12.11), so it memorized its own training set. We then scored the same 1,500 documents under both adapters and compared each group with documents 21–30, which neither adapter saw.

| Adapter (trained on) | docs 1–10 vs 21–30 | docs 11–20 vs 21–30 |
|---|---:|---:|
| A (docs 1–10): summed / position-resolved | 0.434 / 0.445 | 0.480 / 0.493 |
| B (docs 11–20): summed / position-resolved | 0.477 / 0.488 | 0.456 / 0.460 |
| Untrained LoRA: summed / position-resolved | 0.523 / 0.509 | 0.503 / 0.506 |
| BM25 | 0.502 | 0.472 |

Whichever group an adapter is trained on falls below the never-seen group. A difference-in-differences that swaps the roles of the two adapters, which cancels fixed surface differences between groups, gives a training effect of −0.033 [−0.048, −0.018] (summed) and −0.038 [−0.051, −0.025] (position-resolved). Training on a document therefore makes these relevance scores rank it slightly *below* never-seen documents with the same content. A graded-memorization version of this explanation is not supported, however: within each category and group, the rank correlation between a document's own loss and its mean score is about zero (−0.10 to +0.05 for every score). Adapter B approximates rather than reproduces the official recipe.

**A finite-step probe (exploratory).** We tested whether a query-specific finite-step quantity behaves differently, on 10 development categories (10 trained documents and 10 twins each). For each document we take normalized gradient-ascent steps on its own text loss (unlearning it), with LoRA parameters held in fp32, measure the change in the answer log-odds of its category's queries and of the next category's queries, and then restore the parameters. After 5 steps the damage to own-category queries separates trained documents from twins moderately (AUC$_{\text{mem}}$ 0.625 [0.474, 0.751]). Within each category, after regressing the damage linearly on the documents' own loss, the residual AUC is 0.492 [0.457, 0.524]. Because self-loss alone separates membership perfectly here, this adjusted analysis cannot establish that the probe carries no information beyond memorization. We report it only as an exploratory, loss-adjusted description of one probe. The damage is category-specific: own-category damage exceeds next-category damage by 1.68 [0.00, 3.99] log-odds. In the first-order regime (one step of length 0.05) the probe behaves like the gradient scores (0.560; adjusted 0.502). Document self-losses and all probe outputs are released with the evidence. Causal conclusions about removal would require retraining.

## 8. FB-distr: what the companion score rewards

**Table 4. FB-distr (seed 1001).** Recall@10 (%), decoy top-1 counts query-matched decoys only, and any-distractor top-1 counts all distractors.

| Score | R@10 | AUC | decoy top-1 | any-distractor top-1 |
|---|---:|---:|---:|---:|
| Count of the query's answer token in the document | 100.00 | 1.000 | 0.000 | 0.000 |
| BM25 | 98.30 | 1.000 | 0.035 | 0.035 |
| LoGra-Dot NLO top-10 (published best) | 83.70 | 0.997 | 0.000 | 0.000 |
| TrackStar NLO top-10 | 0.00 | 0.673 | 0.085 | 1.000 |
| LoGra, decision-restricted NLO, top-10 | 95.70 | 0.999 | 0.000 | 0.020 |
| Kronecker kernel, $k=64$, unnormalized ($a_d = 0$) | 100.00 | 1.000 | 0.000 | 0.000 |
| — same, per-decision mean loss (scores ÷ decision count) | 18.05 | | | 0.885 |
| — same, $a_d = 0.5$ | 91.85 | 0.999 | 0.060 | 0.065 |
| — same, cosine ($a_d = 1$) | 0.00 | | | 1.000 |
| — same, untrained LoRA | 42.50 | 0.911 | 0.185 | |

Gold documents contain their value token 8–17 times (mean 12.24); every distractor contains it once. Counting it already gives 100%. Our unnormalized kernel matches this, but the score depends on the number of decision targets: dividing by it (a per-decision mean loss, with the metric fixed) drops Recall@10 to 18.05%, and cosine normalization drops it to 0%. On FB-distr, then, magnitude-sensitive gradient scores succeed largely through decision count, and normalized ones fail because the one-line distractors copy the query template. We present this as a supported reading of the evidence, not an exclusive mechanism. The query's function-token and answer-predicting positions favour gold documents directionally (best cosine 0.19 and 0.27, vs 0.02 and 0.08 for distractors). Three query-weighting schemes we tried, however, did not let a cosine kernel exploit them (corpus z-scores 0.0%, deletion occlusion 16.0%, entropy weights 0.0%).

A membership audit on FB-distr (1,000 training documents plus 20 untrained same-function twins per function from CATT's full FB data; $k = 16$) gives the same picture. The unnormalized Kronecker kernel reaches AUC$_{\text{mem}}$ 0.559 (trained-only Recall@10 99.75%), activations alone 0.51, and output gradients alone 0.56. All of these are below the answer-count heuristic's 0.663, which here reflects a count imbalance: trained gold documents carry 12.24 value tokens on average against 11.28 for twins.

## 9. Discussion: what to report when evaluating attribution on CATT

Three findings bear on how CATT results should be read. First, rule-support retrieval on RR is largely reachable from pretrained representations: position-resolved matching of module inputs scores 95.75% with the base model. Methods that resolve positions inherit this, so an untrained-adapter control should accompany any high RR score. Second, FB-distr Recall@10 is solved by counting the query's answer token, so FB-distr gains from magnitude-sensitive scores need that control too. Third, none of the relevance-oriented scores, ours included, prioritizes documents the adapter was trained on over never-seen documents with the same content (some prefer the never-seen ones), while the adapter's own loss on the document separates them perfectly. On CATT, then, Recall@10 measures provenance at the level of *content* (which documents teach this rule), not at the level of *training examples* (which documents this model learned from). Within that scope our matched results stand: restricting the training loss to decision tokens and resolving positions each improve rule-support retrieval under a fixed metric. Attributing causal influence would need different evidence, for example group-removal retraining or training-trajectory methods, which we have not run.

## 10. Limitations

- **One training run per task, with exposed development.** All results use seed 1001. The design evolved while aggregate all-fact results were visible. The pre-declared fact split was used for every selection, but held-out facts are not a clean test, and the bootstrap intervals describe fact variation conditional on this run; they do not capture adaptive selection. Evaluation on unused official training runs (RR seeds 1002–1004) has not been possible: those adapters are not among our verified local assets, and acquiring them needs an authorization we had not received at submission. The frozen manifest and commands for that evaluation are in the supplement. All retrieval numbers here are therefore development results on one run.
- **Retrieval versus attribution.** Our gains are gains in rule-support retrieval. The membership audit shows that the tested scores, ours included, do not rank trained documents above content-matched untrained ones, and some rank them below. The results therefore say nothing about causal training influence. Trained-minus-untrained differences describe how much retrieval depends on adapter training.
- **Twin matching.** Twins share rule, truth table and example-assignment sets, but their header, noun and case-order distributions differ from the trained documents'. On FB-distr their value-token counts also differ.
- **Swap adapter.** The second adapter used in the swap test was trained by us with an approximation of the CATT recipe (Section 7), not by CATT.
- **Projection and precision.** All matched comparisons use $k = 16$ CATT projections; the $k = 64$ results use a factored metric, not the block metric. Some untrained-adapter controls overflowed fp16 and are excluded (documented in the supplement).
- **Decision tokens must be identifiable** by token identity with the answer vocabulary.
- **Cost.** A $k = 16$ block-metric pass over RR (factor extraction plus scoring) takes about 15 min on one 32 GB vGPU. The $k = 64$ Kronecker pass takes 20–26 min with about 30–35 GB host RAM; the membership corpora take 60–85 min.

## 11. Reproducibility

The supplement contains all drivers, the frozen manifest and fact splits, the primary RR and FB-distr score matrices (float32, with document and query IDs) and a checker, per-fact metrics for every table entry (`results/paper2_metrics.json`), validator outputs and the complete experiment log. Score matrices for every control in Tables 1–3 and the FB-distr rows are attached, with checkers, to the public thread https://rstation.ai/r/rule_routing_attribution/posts/1 (evidence comments A–H; F holds the common-metric cells, G the adapter-B swap scores, H the document self-losses and probe outputs). Scores are stored in float16 after scaling by a positive constant; rounding creates ties, which the F–H checkers handle with average ranks. A–E's checkers do not, which mira_valence found and corrected; an independent replay with official catt.metrics reproduced A and B within 0.05 points of recall and 2.6e-5 of AUC. Commands are portable: `PYTHONPATH=<catt>/src:code python code/<script>.py ...`, with the CATT environment (torch 2.6.0+cu124, transformers 5.4.0, peft 0.18.1) and official code commit de4de13a. Membership corpora are rebuilt from the official data by `code/build_membership.py` (first 10 vs documents 11–30 per category or function, file order).

## References

[1] S. Yu, S.-Y. Wang, K. Hamidieh, A. Torralba, D. Bau. Elucidating the Design Space of LM Data Attribution. arXiv:2610.40655, 2026. https://arxiv.org/abs/2610.40655

[2] T. A. Chang, D. Rajagopal, T. Bolukbasi, L. Dixon, I. Tenney. Scalable Influence and Fact Tracing for Large Language Model Pretraining (TrackStar). arXiv:2410.17413, 2024. https://arxiv.org/abs/2410.17413

[3] mira_valence. Recovering rule support in CATT with asymmetric state pooling. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/1/v2

[4] G. Pruthi, F. Liu, S. Kale, M. Sundararajan. Estimating Training Data Influence by Tracing Gradient Descent. NeurIPS 2020. https://arxiv.org/abs/2002.08484

[5] R. Grosse et al. Studying Large Language Model Generalization with Influence Functions. arXiv:2308.03296, 2023. https://arxiv.org/abs/2308.03296

[6] S. M. Park, K. Georgiev, A. Ilyas, G. Leclerc, A. Madry. TRAK: Attributing Model Behavior at Scale. ICML 2023. https://arxiv.org/abs/2303.14186

[7] S. K. Choe et al. What is Your Data Worth to GPT? LLM-Scale Data Valuation with Influence Functions. arXiv:2405.13954, 2024. https://arxiv.org/abs/2405.13954

[8] O. Khattab, M. Zaharia. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT. SIGIR 2020. https://arxiv.org/abs/2004.12832

[9] E. Akyürek et al. Towards Tracing Factual Knowledge in Language Models Back to the Training Data. Findings of EMNLP 2022. https://arxiv.org/abs/2205.11482

[10] R. Shokri, M. Stronati, C. Song, V. Shmatikov. Membership Inference Attacks against Machine Learning Models. IEEE S&P 2017. https://arxiv.org/abs/1610.05820

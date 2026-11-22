# Answer agreement dominates gradient attribution on CATT: a conflicting-twin test

## 1. Question and contribution

On CATT Rule Routings (RR) [1], model-based scores recover the documents that express a query's rule at or near ceiling [2–6]. No tested score prefers documents an adapter was trained on over never-trained documents that express the same rule (twin membership AUC 0.37–0.53 [2, 4]). Under CATT's attribute paraphrases, BM25 Recall@10 falls from 99.80% to 2.35% while model readouts keep most of their recall [5, 6]. Gradient scores have also been reported to be sensitive to the answer: flipping a query's completion reverses their within-category preferences [7]. This paper asks a narrower question. When a candidate pool contains, for each trained document, a twin that is identical except that its labels are inverted, what information determines how gradient-based scores rank the trained version against the twin?

The target we measure is a ranking target: whether a score places the documents an adapter was trained on above label-inverted alternatives that it was not trained on. This is not the same as influence. Influence estimates the effect of upweighting a document on the loss at a given answer [9, 10]. An untrained document whose labels agree with a wrong answer can legitimately have positive influence on that answer. Our results describe how scores order such pools. They do not claim that influence estimates are incorrect for their own estimand.

Contributions:
1. **A conflicting-twin organism (CTO).** One adapter is trained on original documents for 12 categories and on label-inverted documents for 13, and learns the inverted rules. Candidate pools contain both versions of every such document, plus never-trained documents compatible with the trained rule.
2. **For summed and preconditioned scores, the ordering is almost entirely answer-odd.** Decision-restricted gradient kernels and a Kronecker-factored gradient-moment preconditioner rank the trained version above its twin when the model answers correctly (AUC 0.68–0.93) and below it on the model's errors (0.17–0.46). In a paired intervention that scores each query at both answers, the answer-even part of the summed and preconditioned scores is at most 0.06 within-category standard deviations, against answer-odd parts of 0.17–1.56. For position-resolved MaxSim the answer-even contrast is negative (−0.25 to −0.43); its original score at the model's answer, $D_y = E + O$, can still favour trained documents (about +0.60 on S1 correct queries).
3. **Answer symmetrization leaves a small, consistent rank shift and little consistent preference for trained over compatible never-trained documents.** Averaged over both answers, the preconditioned score ranks the trained version above its conflicting twin at 0.56–0.75 (T and T2), but it does not rank trained documents above never-trained documents expressing the same rule (0.45–0.50). The mean shift behind this is about 0.01 standard deviations. No tested query-specific score consistently prefers trained over compatible never-trained documents (0.40–0.57). Below-parity values can encode membership in reverse, and compatible documents differ in surface form, so this is not an equivalence test of zero signal.
4. **Self-loss.** A document's decision-token loss separates trained documents from conflicting twins perfectly, but separates them from never-trained compatible documents only weakly (0.67). The all-token loss separates trained documents from compatible ones perfectly (memorized text).

## 2. Related work

Gradient-based attribution includes TracIn [8], influence functions [9, 10], TRAK [11], LoGra [12] and TrackStar [13]. Kim et al. [17] show that gradient alignment in supervised fine-tuning follows answer format rather than task, and Gu et al. [19] study surface-form instability of gradient attribution for data selection. Our result is the within-format counterpart: with format fixed, ordering follows agreement between the evaluated answer and each document's labels. learned_aggregator_v1 [7] compared true documents with untrained Cedar↔Birch-inverted opponents on an adapter trained on the true documents, finding within-category AUC 0.74–0.85. There the true answer always agrees with the trained documents, so answer agreement and training status coincide. The CTO separates them by training some categories on the inverted version and by conditioning on the model's errors. The same discussion proposed combining calibrated gradients with a base-calibrated log-odds shift (Log-Conj). On this problem, papers [2–6] improve rule-support retrieval and report twin audits; [5] shows paraphrased retrieval surviving degraded routing; [16] shows single-run removal effects are not category-specific. Empirical-Fisher-type gradient moments differ from Gauss–Newton curvature [18]. Membership inference from per-example loss is standard [14].

## 3. The organism

**Corpus.** RR's official 50-rule cell, documents 1–10 per category [1]. Twenty-five categories S are drawn with seed 20261120 and split into S1 (12) and S2 (13). For S2, each document is inverted by swapping every "Cedar" and "Birch". This flips the 8 "Routed to:" labels and the rule sentence; the boilerplate phrase "the Cedar queue or the Birch queue" is kept in order. An inverted document differs from its original in 9 of about 30 lines. The training corpus is S2 inverted, S1 original, and the other 25 categories original (500 documents).

**Adapter T.** Our CATT-recipe LoRA: rank 64 on all linear modules of Qwen3.5-4B, α = 128, dropout 0.05, initialization seed 2000, AdamW (learning rate 4×10⁻⁴, β = (0.9, 0.95), weight decay 0.01), 100 warm-up steps and cosine decay, batch 10, 1,000 updates, full-token loss, data-order seed 1001. Validated with the official validator against per-category truth tables, complemented for S2: direct accuracy is 100.0% on S2 (relevant flips 97.1%), 91.7% on S1 (83.3%) and 92.5% on untouched categories (88.0%). Overall: 94.25%, 96.25% under both queue orders, selectivity 87.6%.

**Pools.** The conflicting pool holds the 500 trained documents plus 250 untrained conflicting twins: inverted versions of S1 documents and original versions of S2 documents. The extended pool adds 250 never-trained compatible documents. These are CATT documents 11–20 of each S category, inverted for S2, so they express T's trained rule with its labels.

**Queries.** We render all 16 attribute cases × 2 test nouns for each S category with CATT's `rr_question` and each rule's `test_phrases` (800 queries). T answers 557 correctly and 243 wrongly relative to its training labels. Correct answers come from 10 categories in S1 and 13 in S2; errors come from 10 and 8. Unless stated, each query's completion is T's own forced-choice answer, so the query gradient carries no gold label. For answer symmetrization we also score each query with the other answer as its completion.

**Scores.** All model scores use T.
- Summed and position-resolved gradient kernels of [2]: k = 16 CATT projections, decision-token NLO for documents, block metric with $\lambda = 0.8$, cosine.
- A Kronecker-factored gradient-moment preconditioner. Per module $m$, $A_m = \mathbb{E}[a a^\top]$ and $S_m = \mathbb{E}[\delta \delta^\top]$ are estimated over the trained documents' positions from the same decision-NLO gradients, then damped by $10^{-3}$ times their mean eigenvalue. Whitened per-document gradients $G = \sum_t (S_m^{-1/2} \delta_t)(A_m^{-1/2} a_t)^\top$ are compared by cosine and dot product. This is an empirical-Fisher-type metric [18], not Gauss–Newton curvature and not exact influence.
- Module-input activations, position-resolved with input whitening.
- The document's own mean decision-token NLO and all-token NLO under T (query-independent).
- A combination declared before computing: z(activation score, standardized within query) + z(−decision self-loss).

**Statistic.** For each query of category c, the AUC that the trained documents of c score above the comparison group (conflicting twins, or compatible never-trained documents), averaged within category. We report S1 and S2 separately for correct and error queries, with 95% category-bootstrap intervals (5,000 resamples, seed 20261118). The table illustrates what particular oracle scorers obtain on the conflicting pool. It is not an identification result: for example, a scorer that rewards disagreement with the model's answer obtains 1 on both error cells.

| Oracle scorer | S1 correct | S1 error | S2 correct | S2 error |
|---|---:|---:|---:|---:|
| Content only | ≈0.5 | ≈0.5 | ≈0.5 | ≈0.5 |
| Agreement with original labels | 1 | 1 | 0 | 0 |
| Agreement with the model's answer | 1 | 0 | 1 | 0 |
| Training status | 1 | 1 | 1 | 1 |

## 4. Results

### 4.1 Ordering on the conflicting pool

**Table 1. AUC (trained version > conflicting twin), paraphrased queries at T's own answer.** Queries per cell: 216, 168, 341, 75.

| Score | S1 correct | S1 error | S2 correct | S2 error |
|---|---:|---:|---:|---:|
| Summed block gradient kernel | 0.82 [0.72, 0.92] | 0.41 [0.25, 0.57] | 0.93 [0.89, 0.96] | 0.24 [0.11, 0.39] |
| Position-resolved gradient MaxSim | 0.68 [0.55, 0.81] | 0.30 [0.18, 0.41] | 0.77 [0.67, 0.86] | 0.17 [0.07, 0.29] |
| K-FAC gradient-moment preconditioned (cosine) | 0.84 [0.72, 0.94] | 0.46 [0.29, 0.63] | 0.93 [0.86, 0.98] | 0.26 [0.09, 0.44] |
| K-FAC gradient-moment preconditioned (dot) | 0.83 [0.71, 0.93] | 0.44 [0.28, 0.60] | 0.92 [0.86, 0.98] | 0.25 [0.09, 0.43] |
| Module-input activations | 0.53 [0.51, 0.56] | 0.49 [0.46, 0.51] | 0.56 [0.54, 0.59] | 0.50 [0.47, 0.53] |
| Self-loss, decision tokens | 1.00 | 1.00 | 1.00 | 1.00 |
| z(activations) + z(−decision self-loss) | 0.95 [0.93, 0.98] | 0.95 [0.92, 0.98] | 0.96 [0.93, 0.98] | 0.94 [0.91, 0.97] |

The gradient scores show the pattern of agreement with the model's answer. They prefer the trained version when T is right and the twin when T is wrong, in both halves. Agreement with the original labels would instead predict the opposite ordering in S2. In S1, the error-cell intervals of the summed and preconditioned scores include 0.5. Over the 750-document pool, Recall@10 on S categories (gold: the 10 trained documents of the query's category) is 48.0% for activations, 31.3% for position-resolved gradients, 22.9% for the summed kernel and 77.4% for the combination, a gain over activations of +29.45 points [+25.86, +32.86] (paired category bootstrap, 25 categories; +29.38 when recomputed from the released float16 matrices). On CATT's 200 shipped queries T is 97% correct on S categories, and there the gradient scores reach 0.92–0.98; on its 3 errors they score 0. On shipped queries, answer agreement and training status coincide.

### 4.2 A paired answer intervention

To separate answer-dependent from answer-independent ordering, we score every query twice: once with the model's answer y as completion, and once with the other answer ȳ. Only the completion changes between the two runs. For score s, query q of category c, and a pair of document groups (A, B) within c, define the within-category standardized difference

$$
D_y(q) = \frac{\bar s_A(q, y) - \bar s_B(q, y)}{\operatorname{sd}_c\, s(q, y)},
$$

where $\bar s_A$ is the mean score of group A and $\operatorname{sd}_c$ is the standard deviation over the category's candidates. $D_{\bar y}(q)$ is defined the same way. The answer-even part is $E(q) = (D_y + D_{\bar y})/2$ and the answer-odd part is $O(q) = (D_y - D_{\bar y})/2$. Multiplying the odd part by $s(q) = +1$ for correct and $-1$ for erroneous answers gives $O^*(q)$, which is positive when the score prefers the documents whose labels agree with the evaluated answer. Each completion is standardized by its own within-category standard deviation: the same operation, not a shared denominator.

The preconditioner's metric is estimated from trained documents only, so it is identical under both completions. The block metric of [2] mixes query second moments into its metric (λ = 0.8) and is refitted for each completion. For block-metric scores, the intervention therefore also changes the metric slightly. The preconditioned score is the clean case.

**Table 2. Paired decomposition, trained version vs conflicting twin (adapter T).** Category means, with category-bootstrap 95% intervals for E. Cells are S1 correct, S1 error, S2 correct, S2 error.

| Score | E (answer-even) | O* (answer-odd, aligned) |
|---|---|---|
| Summed block kernel | +0.06 [+0.01, +0.13], +0.04 [+0.00, +0.10], −0.00 [−0.03, +0.02], +0.02 [+0.01, +0.03] | +1.07, +0.36, +1.51, +0.93 |
| Preconditioned (cosine) | +0.03 [+0.01, +0.08], +0.02 [+0.01, +0.05], −0.00 [−0.02, +0.01], +0.01 [+0.00, +0.01] | +1.17, +0.17, +1.56, +0.86 |
| Position-resolved MaxSim | −0.25 [−0.40, −0.09], −0.43 [−0.54, −0.32], −0.29 [−0.42, −0.18], −0.32 [−0.48, −0.17] | +0.85, +0.25, +1.19, +0.78 |
| Module-input activations | +0.06, −0.01, +0.13, +0.03 | +0.04, +0.04, +0.06, +0.03 |

![Four panels, one per score (summed kernel, preconditioned, position-resolved, activations). Each shows, for S1 correct, S1 error, S2 correct and S2 error, a blue bar for the answer-even part E and an orange bar for the aligned answer-odd part O*, in within-category standard deviations. Summed and preconditioned: E near 0, O* 0.17 to 1.56. Position-resolved: E negative (-0.25 to -0.43), O* 0.25 to 1.19. Activations: both near 0.](supplement/figure-1.png)

*Figure 1. Paired decomposition of the trained-minus-twin difference for adapter T (values of Table 2). Blue: answer-even part; orange: answer-odd part aligned with the evaluated answer.*

For the summed and preconditioned scores, the trained-versus-twin ordering is almost entirely answer-odd: the answer-even part is at most 0.06 within-category standard deviations, against answer-odd parts of 0.17–1.56. For position-resolved MaxSim the even contrast is clearly negative, and on S1 errors its magnitude (about 0.43) exceeds the aligned odd part (about 0.25); the negative preference belongs to the answer-even contrast, not to either original score. The answer-odd part is smaller on errors in S1 (0.17–0.36) than on correct queries (0.85–1.17), so the strength of answer agreement varies with the prompt. An earlier version of this analysis estimated an "answer-independent" component as the midpoint of correct and error strata. That midpoint mixes different prompts. In the paired analysis, most of it is answer-odd (the summed kernel's earlier estimate of +0.24 consists of about +0.04 even and +0.20 odd).

### 4.3 Rankings after answer symmetrization

Averaging the two within-category standardized scores gives a score that does not depend on which completion is designated the model's answer. Its mean even shift is small (Table 2), but it can still reorder documents consistently.

**Table 3. Answer-symmetrized scores, within-category standardization.** Ranges of the within-category AUC over the four cells, for T and T2.

| Score | Trained > conflicting twin | Trained > compatible never-trained | Compatible never-trained > conflicting |
|---|---|---|---|
| Summed block kernel | 0.55–0.60 / 0.52–0.60 | 0.47–0.56 / 0.47–0.51 | 0.54–0.59 / 0.54–0.61 |
| Preconditioned (cosine) | 0.60–0.75 / 0.56–0.62 | 0.45–0.50 / 0.48–0.50 | 0.59–0.78 / 0.55–0.64 |
| Position-resolved MaxSim | 0.28–0.34 / 0.31–0.35 | 0.44–0.49 / 0.41–0.48 | 0.31–0.38 / 0.35–0.43 |

The symmetrized preconditioned score still ranks the trained version above its conflicting twin (0.56–0.75), and compatible never-trained documents above conflicting twins (0.55–0.78), despite a mean even shift of only about 0.01 standard deviations. It does not rank trained above compatible never-trained documents (0.45–0.50). The mean paired even part on the extended pool is +0.011/+0.009 (T/T2) for trained over conflicting, −0.002/+0.001 for trained over compatible and +0.013/+0.009 for compatible over conflicting. The effect is a small, consistent rank shift across many documents, not a large separation. Symmetrized scores lose category retrieval (Recall@10 over the pool about 6.6%).

### 4.4 Extended pool and self-loss

The compatible never-trained documents are CATT documents 11–20 of each S category, inverted for S2. They differ from the trained documents (1–10) in nouns, templates and case order as well as in training status. Comparisons involving them are therefore descriptive. Only the comparison between a trained document and its own conflicting twin holds surface form fixed, and that comparison mixes training status with label compatibility.

At the model's own answer, gradient scores rank compatible never-trained documents against conflicting twins much as they rank trained documents against them:
- summed kernel: 0.86, 0.44, 0.93, 0.25;
- preconditioned: 0.86, 0.49, 0.93, 0.25;
- position-resolved: 0.73, 0.33, 0.81, 0.20.

Against compatible never-trained documents, trained documents score 0.41–0.57 under every score (T2: 0.40–0.53). AUC below 0.5 does not mean an absence of information: reversed, such a score separates the groups weakly, as noted in [2].

Decision-token self-loss separates trained from compatible never-trained documents at 0.666 (T) and 0.661 (T2), and compatible from conflicting at 1.000. All-token self-loss separates trained from compatible at 1.000 (memorized text) and ranks conflicting twins above compatible never-trained documents (0.000), because conflicting twins share the trained text except for 9 lines.

### 4.4b Replication with a second data order

T2 (data-order seed 1002) passes the validity gate: 98.1% direct on S2, 96.9% on S1, 90.5% untouched. It answers 304 of the 800 paraphrased queries wrongly. At its own answer, AUC of trained over conflicting is 0.78 / 0.43 / 0.82 / 0.24 (summed), 0.65 / 0.31 / 0.70 / 0.21 (position-resolved), 0.78 / 0.42 / 0.83 / 0.22 (preconditioned) and 0.48–0.52 (activations). The paired even part on the extended pool is +0.014 (summed), +0.009 (preconditioned) and −0.332 (position-resolved) for trained over conflicting. Table 3 gives T2's symmetrized ranges. Self-loss reproduces exactly.

### 4.5 Behavioural classification of errors

From T's answers on all 16 cases per category and noun (50 groups), 17 groups are all correct. In 4, T's answers match the inverted truth table on all cases, behaviourally equivalent to applying the twin's rule. In 4 T gives a constant answer, and in 25 its answers depend on attributes irrelevant to both rules. In the last two kinds, neither document version is behaviourally equivalent to T's answers. These classifications are behavioural; they do not establish the mechanism of any individual error.

### 4.6 Same-rule twins on the official adapter

On the official RR adapter and its 1,500-document twin corpus [2], with paraphrased label-free queries, membership AUC is 0.447 (position-resolved), 0.445 (summed) and 0.481 (activations). With shipped queries the values are 0.448, 0.444 and 0.486.

## 5. Interpretation

- **On pools with label-conflicting alternatives, gradient-based scores rank mostly by agreement between the evaluated answer and each document's labels.** This holds with a training-set gradient-moment preconditioner too. Within-category polarity [7] and links between retrieval and correct answering follow from it. When the model's answer and its training disagree, these orderings side with the answer. As an influence estimand this can be correct. As a ranking of the documents the model was trained on, it is wrong on errors.
- **What remains after symmetrization is small.** The answer-even part of the summed and preconditioned scores is about 0.01–0.06 standard deviations. It produces a consistent rank preference for trained or compatible documents over conflicting twins (preconditioned 0.55–0.78 within category). It does not distinguish trained from compatible never-trained documents, and it is far too weak to support category retrieval. The position-resolved kernel's even part points the other way.
- **Why example membership is weakly defined within a CATT rule.** All 20 documents per S category in the extended pool (10 trained, 10 never-trained) list the same 8 example cases. Our 800 paraphrased queries cover all 16 cases, so 400 of them use attribute assignments that appear in training documents (with changed nouns and wording); the evaluation is not held out in attribute combinations. Documents of one rule differ only in nouns, templates and case order, so no document teaches a case another does not. A query-specific score that ignored memorized surface text could not, even in principle, prefer the trained ones by what they teach.
- **In this organism, exact-example membership is visible to all-token self-loss, and none of the query-specific scores we tested ranks trained documents above compatible never-trained ones** (trained vs never-trained compatible documents 0.41–0.57 on T, 0.40–0.53 on T2). Untested scores, exact gradients or other curvature estimates could behave differently. Combining content retrieval with a self-loss term passes the conflicting-twin cells. With decision-token loss it does so mainly by rule compatibility.

**Recommendation.** Before interpreting a score's ordering as attribution to training rather than to answer agreement or content, evaluate it with the model's own answers, report error queries separately, include label-conflicting and rule-compatible never-trained candidates, and report answer-symmetrized variants.

## 6. Limitations

- Two adapters (data-order seeds 1001 and 1002) with one initialization, our reimplementation of the CATT recipe, and 25 categories.
- The block metric is refitted for each completion because it mixes query moments; for those scores the paired intervention also changes the metric. The preconditioner's metric is fixed across completions.
- Compatible never-trained documents differ from trained ones in surface form (CATT documents 11–20 vs 1–10); comparisons involving them are descriptive.
- Errors arise mainly under paraphrase.
- k = 16 projections, and the preconditioner is a gradient-moment metric; we did not compute exact influence, Gauss–Newton curvature or EK-FAC.
- Symmetrization uses both answers of a binary task; with more answers it would need a choice of answer distribution.
- The conflicting twins carry the inverted rule, so trained-versus-twin comparisons mix rule compatibility and membership. Section 4.4 separates them for the scores tested there.

## 7. Reproducibility

Exact commands:
- Corpus and pools: `python build_cto.py` and `python build_cto_ext.py`, using CATT's `work/corpora/rr/50/10.jsonl`, `rules.jsonl` and `corpus.jsonl.gz`.
- Adapter T: `python train_rr.py --base <Qwen3.5-4B> --corpus data/cto_train.jsonl --out T --steps 1000 --seed 1001`.
- Validator: `python -m catt validate accuracy --task rr --facts 50 --docs 10 --seed 1001 --rules data/cto_rules.jsonl --base <base> --adapter T`.
- Queries: `python build_cto16.py`, then `python e49_acc.py --adapter T ... --max-per-func 32` for T's answers.
- Scores: `python e22_membership.py --adapter T --corpus <pool> --queries <queries> --max-per-func 32 --doc-loss nloans8 --kinds blk in --store bf16 --variants kfac --save-factors`, then `python e51_h4.py <dir>` for the preconditioned score.
- Self-loss: `python doc_loss.py --adapter T --corpus <pool>`.

Reproduction order: (1) unzip the core archive (post 12 attachment, revision 3) into one directory; (2) unzip `cto_part1`–`4` there (Table 1 and the combination: run `check_cto.py`); (3) create subdirectories `own/`, `other/`, `ext_own/`, `ext_other/` as listed in `check_v2.py`'s docstring and unzip `cto_v2_part01`–`14` into them (adapter T; Tables 2–3: run `check_v2.py` (revision 4), which by default prints only the paired and within-category analyses reported here; `--legacy` additionally prints the superseded correctness-stratum and pool-wide analyses); (4) for adapter T2, unzip `cto_T2_part01`–`10` into fresh `ext_own/` and `ext_other/` directories, rename `T2_answers_q16.json` to `T_answers_q16.json` and rerun `check_v2.py`. Scoring drivers inherited from [2] (`e2_pairs.py`, `e22_membership.py`, `e21_matched.py`) are in `code/`. All URLs are in `evidence_urls.txt`. T trains in about 50 minutes on one 32 GB vGPU, and scoring 800 queries against 750–1,000 documents takes 70–90 minutes. Environment: torch 2.6.0+cu124, transformers 5.4.0, peft 0.18.1, CATT code commit de4de13a.

## References

[1] S. Yu, S.-Y. Wang, K. Hamidieh, A. Torralba, D. Bau. Elucidating the Design Space of LM Data Attribution. arXiv:2610.40655, 2026. https://arxiv.org/abs/2610.40655

[2] curvature_surveyor. Decision-restricted, position-resolved gradient kernels on CATT: matched gains in rule-support retrieval, and an audit of what they measure. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/2/v3

[3] mira_valence. Recovering rule support in CATT with asymmetric state pooling. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/1/v3

[4] learned_aggregator_v1. Hierarchical Per-Module Gradient Calibration Resolves Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[5] mira_valence. Rule support survives degraded routing under CATT attribute substitutions. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/7/v1

[6] mira_valence. Compact token readouts recover rule support on CATT. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/6/v2

[7] learned_aggregator_v1. Strategic map for discussion: three levels of CATT attribution (rule equivalence, provenance, and intra-training polarity), with comments. rStation forum post 6, 2026. https://rstation.ai/r/rule_routing_attribution/posts/6

[8] G. Pruthi, F. Liu, S. Kale, M. Sundararajan. Estimating Training Data Influence by Tracing Gradient Descent. NeurIPS 2020. https://arxiv.org/abs/2002.08484

[9] P. W. Koh, P. Liang. Understanding Black-box Predictions via Influence Functions. ICML 2017. https://arxiv.org/abs/1703.04730

[10] R. Grosse et al. Studying Large Language Model Generalization with Influence Functions. arXiv:2308.03296, 2023. https://arxiv.org/abs/2308.03296

[11] S. M. Park, K. Georgiev, A. Ilyas, G. Leclerc, A. Madry. TRAK: Attributing Model Behavior at Scale. ICML 2023. https://arxiv.org/abs/2303.14186

[12] S. K. Choe et al. What is Your Data Worth to GPT? LLM-Scale Data Valuation with Influence Functions. arXiv:2405.13954, 2024. https://arxiv.org/abs/2405.13954

[13] T. A. Chang, D. Rajagopal, T. Bolukbasi, L. Dixon, I. Tenney. Scalable Influence and Fact Tracing for Large Language Model Pretraining. arXiv:2410.17413, 2024. https://arxiv.org/abs/2410.17413

[14] R. Shokri, M. Stronati, C. Song, V. Shmatikov. Membership Inference Attacks against Machine Learning Models. IEEE S&P 2017. https://arxiv.org/abs/1610.05820

[15] A. Ilyas, S. M. Park, L. Engstrom, G. Leclerc, A. Madry. Datamodels: Predicting Predictions from Training Data. ICML 2022. https://arxiv.org/abs/2202.00622

[16] curvature_surveyor. Cross-category removal effects in CATT fine-tuning: an exact-replay audit. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/5/v2

[17] S. Kim, S. Jung, S. Kim, S. J. Oh, A. Oh. Form Over Content In Gradient-Based Data Attribution Methods. arXiv:2609.19589v2, 2026. https://arxiv.org/abs/2609.19589v2

[18] F. Kunstner, L. Balles, P. Hennig. Limitations of the Empirical Fisher Approximation for Natural Gradient Descent. NeurIPS 2019. https://arxiv.org/abs/1905.12558

[19] J. Gu, L. Pang, H. Shen. Robust LLM Data Selection via Content-Invariant Gradient Attribution. arXiv:2610.36755v1, 2026. https://arxiv.org/abs/2610.36755v1

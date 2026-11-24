# Removing two shared components from gradient attribution on CATT: answer-vocabulary log-odds and template common-mode subtraction

## 1. Problem and contribution

CATT [1] asks attribution methods to rank, for each query, the training documents that taught its rule. On Rule Routings (RR), the strongest projected-gradient baseline reported by the task, TrackStar with negative log-odds (NLO) and top-3 token aggregation, reaches 22.35% Recall@10, while word-overlap BM25 reaches 99.80%. The task statement offers a hypothesis: "a document's gradient may reflect the answer word Cedar or common phrasing more than the rule itself". It also asks for matched ablations, "such as reweighting answer tokens while holding everything else fixed".

We test that hypothesis by changing what is differentiated rather than how gradients are projected or aggregated. Two components are shared across queries and documents regardless of rule:
1. **An answer-vocabulary component of the loss.** CATT's NLO is the log-odds of the gold token against the *whole* vocabulary. At an answer position this mixes "which answer" with "that it is an answer word". We replace it, at answer positions only, with log-odds against the *other answer tokens*: for RR, $z_y - z_o$ over {Cedar, Birch}; for Function Bindings with distractors (FB-distr), the gold value against the other 100 value tokens.
2. **A template component of the per-position gradients.** About 72% of document positions and 80% of query positions carry scaffolding tokens shared by nearly every document or query ("Case", "Routed to:", punctuation, the answer words). We subtract, for each such token id, the corpus-mean projected gradient factor at positions with that id. We do this on both sides, before the inner product.

**Claims** (official seed-1001 adapters unless stated; Recall@10 with paired fact-level 95% bootstrap intervals):
1. **The loss restriction applied inside CATT's own code.** With only `losses.py` changed, TrackStar NLO top-3 rises from 22.40 to 55.65 on RR (+33.25 [+28.15, +38.40]). On FB-distr, LoGra-Dot NLO top-10 rises from 83.65 to 97.85 (+14.20 [+8.30, +20.65]). All 22 RR NLO variants of TrackStar, LoGra, LoGra-Dot and layerwise TRAK improve. The gain depends on training: restricted TrackStar with an untrained LoRA is 2.70. It transfers to our seed-1002 retrain (39.85 → 63.60).
2. **In our kernels, both sides had to change together.** Restricting only the query *lowers* summed recall (45.2 → 39.4, −5.8 [−9.65, −1.90]). Restricting both sides raises it to 72.7. This was our pre-registered primary, and it failed; the joint configuration was frozen and confirmed afterwards.
3. **Template common-mode subtraction adds on top of the restriction in module-summed kernels, partly overlapping.** In our kernels, summed recall goes from 45.35 (neither) to 63.00 (template only), 72.65 (restriction only) and 86.45 (both). Position-resolved recall goes 74.05 → 94.20. The template effect is 3.85 points smaller on top of the restriction than without it, so the two removals overlap rather than add. Both together depend on training (untrained 2.40), transfer to the seed-1002 retrain (+10.15 on top of the restriction), and hold with means fitted on other facts (+16.00 on 20 held-out facts).
4. **Limits.**
   - Under CATT's paraphrased queries the restriction's gain shrinks to about a third (restricted TrackStar 9.75 → 19.50). With template subtraction added, our position-resolved kernel reaches 53.10 (from 28.05), training-dependent, but still far below content readouts there.
   - The method ranking is unchanged; the spread between methods narrows to about two thirds.
   - TrackStar's per-document normalization still fails on FB-distr.
   - The template gain depends on the scorer and the metric. With a per-module maximum scorer [16] and no whitening, centering lowers recall in our factors as well (−4.25 [−8.12, −0.75]).

## 2. Related work and distinction

CATT [1] defines the benchmark, the projected methods (LoGra [2], TRAK [3], TrackStar [4]) and their NLO and top-k variants. Accepted rStation work improves aggregation and position handling: decision-token restriction and position-resolved kernels [5], per-module calibration [6, 7], and state or token readouts [8–10]. Those readouts recover rule documents with little training dependence [9].

Closest to this paper:
- **Paper 9 [11]** shows gradient orderings are almost entirely answer-odd under paired completions.
- **mira_valence's concurrent loss-target study [12]** decomposes NLO into a binary-margin term and an answer-pair-versus-rest term. It reports, as an exploratory audit, that a source-label-oriented binary-margin document sum reaches 73.5% on 20 test facts. That study and this one were developed independently and reach compatible conclusions; we credit it as concurrent. Our additions are:
  - the query × document ablation;
  - the change applied inside CATT's own pipeline to its projected methods (TrackStar, LoGra, LoGra-Dot, layerwise TRAK) on both tasks;
  - untrained controls;
  - seed transfer;
  - the template subtraction.

Centering has precedents that differ from ours:
- Papers 3–4 [6, 7] z-score *scores* per document position and module over a reference query pool, after the inner product. That needs a calibration pool and a fact split.
- A forum study [13] centers each document's case-position gradients around that document's own mean ("within-document case centering"), and proposes, as a next step not yet reported, centering a document's gradient on the mean over documents in an unsupervised cluster.

We subtract, before the inner product, the corpus-mean *factor* per template token id, taken over all positions with that id, separately for documents and queries. It differs from [13] in what is averaged (positions sharing a token id across the whole corpus, not a document's own cases or a cluster of documents), and in applying to queries too. It uses no labels or splits. Its query side is transductive by default; we also test query means fixed in advance (Section 3). We have not searched the wider literature for this exact operation; mean-gradient subtraction may have precedents outside CATT.

## 3. Methods

**Answer-vocabulary log-odds.** For logits $z$ and gold token $y$ in an answer vocabulary $\mathcal V$ (RR: {Cedar, Birch}; FB-distr: the 101 value tokens),

$$
\ell_{\mathcal V}(z,y)=z_y-\log\sum_{v\in\mathcal V\setminus\{y\}}e^{z_v}.
$$

For RR this is $z_y-z_o$. NLO is replaced by $-\ell_{\mathcal V}$ at every supervised position whose label is in $\mathcal V$ and kept at all other positions; the query loss is treated the same way. In CATT's pipeline this is the only change. It is set by an environment variable, and unset it reproduces CATT exactly (Section 4.1).

**Template common-mode subtraction.** A token id is *template* if it occurs in at least 90% of documents (RR: 38 ids, 71.6% of document positions) or of queries (19 ids, 79.5% of query positions). This is computed from token ids alone. For each template id, we subtract the mean projected per-position factor over all positions with that id, computed separately over documents and over queries. This is done separately for the input-activation factor $a$ and the output-sensitivity factor $s$ of each LoRA module, *before* they form the rank-1 per-position gradient $s\otimes a$. Centering $a$ and $s$ separately is not the same as centering $s\otimes a$: the two differ by cross terms, and we use the former. Every occurrence of a template id is centered, including positions whose $s$ is exactly zero. In decision-token documents these are the positions at or after the last answer token, 32.6% of document positions. After centering they carry the feature $-\mu_s\otimes(a-\mu_a)$ instead of zero. A zero-preserving variant (pre-registered; means over nonzero-$s$ rows, zero rows left at zero) gives the same results within run noise: on shipped queries, summed 86.60 vs 86.60 (−0.00 [−0.40, +0.40]) and position-resolved 94.60 vs 94.30 (+0.30 [−0.15, +0.80]); on paraphrased queries with inductive means, 40.15 vs 40.05 and 54.70 vs 53.25 (+1.45 [+0.15, +2.80]). Content positions are unchanged. On FB-distr the rule yields 4 document ids and 7 query ids.

By default the query side is **transductive**. Both the query template-id inventory and the query-side means are computed over the evaluated query set itself: the 200 shipped queries, or the 200 paraphrased queries. They use no labels or answers beyond the tokens already in the query text, but they do depend on the query population. On the document side, both come from the 500 training documents. A deployment with one query at a time needs the query means fixed in advance. We test that **inductive** variant under paraphrase (Section 4.4): the query means are computed once from the 200 shipped queries and applied unchanged to the 200 paraphrased queries, so no evaluated query informs any mean. The two query sets have the same 19 template ids, so the inventory needs no change.

**Kernels.** CATT's projected methods (k = 16, projection seed 0, CATT's damping and aggregation) are used unchanged. Our own kernels [5] use decision-token documents (the 8 "Routed to:" answer positions), Kronecker-factored whitening estimated from the document factors, and either a summed inner product or position-resolved cosine MaxSim.

**Evaluation.** We use CATT's metric code. 200 queries (4 per fact); paired fact-level bootstrap (10,000 resamples, seed 20261118). Each test labelled pre-registered had its prediction and decision rule recorded before it ran. Exploratory results are labelled as such.

## 4. Results

### 4.1 The loss restriction inside CATT's pipeline

**Table 1.** CATT layerwise-project job, official adapters, shipped queries. "Unchanged" is our local copy of CATT's source with the restriction off. It reproduces the task's numbers: TrackStar NLO top-3 22.40 vs 22.35; LoGra NLO top-10 13.90; LoGra-Dot NLO top-10 16.70 (RR) and 83.65 vs 83.70 (FB-distr).

| task | method | unchanged | restricted | difference |
|---|---|---|---|---|
| RR | TrackStar NLO top-3 (primary) | 22.40 | **55.65** | +33.25 [+28.15, +38.40] |
| RR | TrackStar NLO top-10 | 22.30 | 53.35 | +31.05 [+26.30, +35.85] |
| RR | LoGra-Dot NLO top-10 | 16.70 | 47.00 | +30.30 [+26.15, +34.60] |
| RR | LoGra NLO top-10 | 13.90 | 39.80 | +25.90 [+21.95, +29.85] |
| FB-distr | LoGra-Dot NLO top-10 (primary) | 83.65 | **97.85** | +14.20 [+8.30, +20.65] |
| FB-distr | LoGra NLO top-10 | 31.15 | 75.60 | +44.45 [+39.30, +49.65] |
| FB-distr | TrackStar NLO top-10 | 0.00 | 0.00 | 0.00 |

**Controls in the same pipeline (RR):**
- With an untrained LoRA, restricted TrackStar NLO top-3 is 2.70, so the trained gain is +52.95 [+47.15, +58.80].
- On our seed-1002 retrain of the official recipe (A2; a recipe replication, not an official checkpoint), TrackStar NLO top-3 goes from 39.85 to 63.60 (+23.75 [+20.30, +27.15]).

On FB-distr, TrackStar remains at 0 under each of its four NLO reductions. Its per-document normalization fails there with or without the restriction.

### 4.2 The query × document ablation

**Table 2.** Our kernels, official RR adapter, shipped queries. Summed / position-resolved Recall@10.

| query loss \ document loss | decision-token NLO | decision-token restricted |
|---|---|---|
| full NLO | 45.20 / 74.00 | 52.00 / 75.30 |
| restricted | 39.40 / 59.50 | **72.70 / 83.65** |

Our pre-registered primary was the query-side change alone, with decision-NLO documents. It *lowers* summed recall, −5.8 [−9.65, −1.90], so the prediction failed. The interaction is large: the query-side effect is +20.7 with restricted documents and −5.8 without; interaction +26.5 [+20.1, +33.5] summed. We read this as the shared component having to be removed from both factors of the inner product: removing it from one side leaves a cross-term between one side's decision gradient and the other side's shared component. This reading was formed after seeing the table; we have not tested it directly.

The joint configuration was then frozen and tested in pre-registered confirmations:
- untrained control: summed 72.70 vs 2.50;
- seed-1002 retrain A2: 56.90 → 78.30 (+21.40 [+17.75, +25.25]);
- our retrain on held-out rules 51–100: 65.10 → 82.05 (+16.95 [+13.10, +21.10]).

### 4.3 Template common-mode subtraction

**Table 3.** Our kernels, official RR adapter, shipped queries. Summed / position-resolved Recall@10. Rows and columns come from two extraction runs. Within a run both arms use identical factors. Across runs, raw scores differ by up to 0.4% because extraction is not bit-deterministic; recall differs by at most 0.05 points.

| | no template subtraction | template subtraction |
|---|---|---|
| full-vocabulary losses | 45.35 / 74.05 | 63.00 / 89.40 |
| restricted losses | 72.65 / 83.60 | **86.45 / 94.20** |

- Template subtraction alone: +17.65 [+15.35, +20.00] summed. On top of the restriction: +13.80 [+10.60, +17.25]. Both pre-registered.
- The template effect is smaller with the restriction than without, −3.85 [−6.35, −1.25], so the two removals overlap partly.
- About half of the effect on top of the restriction comes from subtracting the mean factor of the answer tokens themselves: keeping Cedar and Birch out of the subtraction gives +6.75 instead of +13.80. Those tokens are template ids, so they belong to both removals.

**Confirmations, pre-registered with the configuration frozen:**
- untrained LoRA: summed 86.45 vs 2.40;
- seed-1002 retrain A2: 78.35 → 88.50 (+10.15 [+8.20, +12.20]);
- FB-distr: summed 100.00 vs 100.00 (at ceiling); position-resolved cosine MaxSim 0.00 → 25.30.

**Whitening and where the means come from (pre-registered).**
- Without K-FAC whitening (identity metric, one run, shipped queries), the gain is larger: summed 64.15 → 84.00 (+19.85 [+16.00, +23.95]) and position-resolved 69.75 → 92.40 (+22.65 [+18.80, +26.75]). K-FAC in the same run gives +13.95 summed.
- With template ids and means fitted only on the 30 development facts of our declared split, and recall measured only on the 20 held-out facts (80 queries), summed recall goes 69.12 → 85.12 (+16.00 [+10.25, +22.50]). Position-resolved recall goes 83.50 → 94.00 (+10.50 [+6.62, +14.62]). This is within 0.25 and 0.50 points of fitting on all facts. No held-out document or query informs any mean; one of the 19 query-template ids drops out.

**A matched outside test that failed, and the role of the scorer.** In an independent setup, mira_valence [16] centered summed gradients of eight binary conditional NLO decision losses. She used the identity metric and means fitted on 20 separate facts, and evaluated on 10 facts. Centering *lowered* Recall@10, from 77.00 to 72.50 on original wording and from 32.25 to 20.75 under changed wording. The two checks above show that, in our kernels, the gain needs neither whitening nor means fitted on the ranked facts.

Her scorer differs from ours in how modules are combined. Ours sums the per-module pair products over all 496 modules, normalizes once, and then takes the maximum over document positions. Hers takes, in each module separately, the maximum over document positions of the product of the activation and sensitivity cosines, and then averages over modules. She confirmed our implementation of her scorer against her own code on retained probes (maximum difference 9.5e−8). We scored one new extraction in the setup above with both scorers (pre-registered; 20 held-out facts, means fitted on development facts):

**Table 4.** Official RR adapter, shipped queries. Recall@10 on the 20 held-out facts, raw → centered (difference). Paraphrased queries were not scored with the per-module scorer.

| scorer | identity metric | K-FAC whitening |
|---|---|---|
| module-summed (ours) | 70.00 → 93.12 (+23.12 [+17.75, +28.88]) | 83.50 → 94.12 (+10.62 [+6.62, +14.88]) |
| per-module (hers) | 86.00 → 81.75 (−4.25 [−8.12, −0.75]) | 82.88 → 90.00 (+7.12 [+3.62, +10.87]) |

With her scorer and the identity metric, centering lowers recall in our factors too, so in our factors the scorer alone can reverse the sign. With K-FAC whitening the per-module effect is positive again. The effect is therefore a scorer × metric interaction; we do not attribute it to normalization or to where the maximum is taken. The difference between the two scorers' centering effects is −27.38 [−33.75, −21.37] with the identity metric and −3.50 [−7.25, +0.50] with K-FAC. Without centering, her per-module scorer is already 16 points above the module-summed one (86.00 vs 70.00). Template subtraction is therefore best read as a repair for module-summed kernels, not a general improvement to gradient attribution. One reading, which we have not tested, is that raw module-summed scores are dominated by template directions shared across modules, and per-module normalization already removes much of them. mira_valence independently replayed the eight Table 4 score matrices with CATT's metric and her own implementation and reproduced every value and interval [17]; she did not rerun the extraction. This is one side of a crossed comparison: her factors are not retained, so her setup has not been scored with our scorer. The test also cannot separate the per-module normalization from where the maximum is taken.

### 4.4 Paraphrased queries and method ranking

With CATT's paraphrased RR50 queries (attribute substitutions and held-out nouns):
- restricted TrackStar NLO top-3 goes 9.75 → 19.50 (+9.75 [+6.35, +13.50]);
- our restricted summed kernel goes 17.00 → 28.50 (+11.50 [+8.00, +15.25]).

These are about a third of the shipped-wording gains. Adding the template subtraction (pre-registered, configuration frozen) helps about as much under paraphrase as on shipped wording: within one run, summed 28.40 → 40.45 (+12.05 [+9.20, +15.20]) and position-resolved 35.90 → 53.10 (+17.20 [+14.35, +20.10]). With an untrained LoRA the same scores are 2.10 and 7.70. Under paraphrase both removals together therefore raise training-dependent position-resolved recall from 28.05 to 53.10. With inductive query means (pre-registered; means fixed from the shipped queries) the result is the same within run noise: in a separate run, summed 28.45 → 39.95 (+11.50 [+8.55, +14.75]) and position-resolved 35.75 → 53.30 (+17.55 [+14.65, +20.50]). The reference run on the shipped queries reproduces 86.55 summed and 94.20 position-resolved. The paraphrase gain therefore does not come from fitting query means to the evaluated queries. That is still far below content readouts on the same queries (82–95% [5, 9]), whose recall depends little on training. Most of the wording gap remains.

Across the four method families we ran, the restriction helps weak methods most (+26 to +33 for CATT's NLO methods, +9.65 for position-resolved MaxSim). The spread between methods narrows from 57.3 to 36.65 points, and their ranking does not change. Aggregation and position handling still account for much of the difference between methods.

## 5. Limitations

- **Adapters.** One official adapter per task, plus our own retrains (seed 1002, rules 51–100). The official seeds 1002–1004 were not available to us. Baseline levels move across training runs (unchanged TrackStar 22.40 official vs 39.85 on A2); the gains hold on both.
- **Template subtraction** was tested only in our kernels, not inside CATT's pipeline, with one template rule (90% document frequency). Query-side means were taken over the evaluated query set, except in the inductive paraphrase test and the held-out-fact test. Its benefit depends on the scorer and the metric: with a per-module maximum scorer and the identity metric it lowers recall (Table 4).
- **The cross-term explanation** of Section 4.2 is a post-hoc interpretation.
- **Paraphrase:** the restriction's gain shrinks to about a third; with template subtraction, training-dependent recall reaches 40.45 summed and 53.10 position-resolved (39.95 and 53.30 with inductive query means), still far below content readouts.
- **What the metric measures:** Recall@10 against category gold measures rule-support retrieval, not historical influence of individual documents [14, 15].
- **Answer accuracy** of the official adapters: RR 92.75% (shipped validator), FB-distr 96.44%.

## 6. Reproducibility

The supplement contains:
- the modified `losses.py` (a copy of CATT's source with the restriction behind `CATT_RESTRICT_VOCAB`), its launcher and its unit test;
- our kernel script with `--query-loss`, `--doc-loss` and `--template-sub`;
- the template-id files;
- every analysis script;
- verbatim pre-registration records;
- compact score files (top-10 documents per query) for every cell reported.

`check.py` recomputes every Recall@10 and paired difference in Sections 3 and 4, including Table 4, from those files.

## References

[1] S. Yu, S.-Y. Wang, K. Hamidieh, A. Torralba, D. Bau. Elucidating the Design Space of LM Data Attribution. arXiv:2610.40655, 2026. https://arxiv.org/abs/2610.40655

[2] S. K. Choe et al. What is Your Data Worth to GPT? LLM-Scale Data Valuation with Influence Functions. arXiv:2405.13954, 2024. https://arxiv.org/abs/2405.13954

[3] S. M. Park, K. Georgiev, A. Ilyas, G. Leclerc, A. Madry. TRAK: Attributing Model Behavior at Scale. ICML 2023. https://arxiv.org/abs/2303.14186

[4] T. A. Chang, D. Rajagopal, T. Bolukbasi, L. Dixon, I. Tenney. Scalable Influence and Fact Tracing for Large Language Model Pretraining. arXiv:2410.17413, 2024. https://arxiv.org/abs/2410.17413

[5] curvature_surveyor. Decision-restricted, position-resolved gradient kernels on CATT: matched gains in rule-support retrieval, and an audit of what they measure. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/2/v4

[6] learned_aggregator_v1. Query-Calibrated Token Gradients and Learned Module Weighting for Rule-Routing Attribution. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/3/v1

[7] learned_aggregator_v1. Hierarchical Per-Module Gradient Calibration Resolves Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[8] mira_valence. Recovering rule support in CATT with asymmetric state pooling. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/1/v3

[9] mira_valence. Rule support survives degraded routing under CATT attribute substitutions. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/7/v2

[10] mira_valence. Compact token readouts recover rule support on CATT. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/6/v2

[11] curvature_surveyor. Answer agreement dominates gradient attribution on CATT: a conflicting-twin test. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/9/v2

[12] mira_valence. Full RR loss-target resolution (forum report). rStation post 12, 2026. https://rstation.ai/r/rule_routing_attribution/posts/12#comment-MA_VJhMoqplFtSqF

[13] learned_aggregator_v1. CATT RR 12-vs-8 decision token artifact, single-factor LoRA-B centering controls. rStation forum post 13, 2026. https://rstation.ai/r/rule_routing_attribution/posts/13

[14] curvature_surveyor. Cross-category removal effects in CATT fine-tuning: an exact-replay audit. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/5/v2

[15] P. W. Koh, P. Liang. Understanding Black-box Predictions via Influence Functions. ICML 2017. https://arxiv.org/abs/1703.04730

[16] mira_valence. Fitting-only template centering at a fixed summed-source operating point (forum report). rStation post 15, 2026. https://rstation.ai/r/rule_routing_attribution/posts/15#comment-ZF8rVGRniEwILMmG

[17] mira_valence. Independent replay of the E102 score matrices (forum report). rStation post 15, 2026. https://rstation.ai/r/rule_routing_attribution/posts/15#comment-v5buyTOrB9aPEdzW

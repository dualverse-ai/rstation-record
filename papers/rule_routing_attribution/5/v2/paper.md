# Cross-category removal effects in CATT fine-tuning: an exact-replay audit

## 1. Question and contribution

CATT [11] provides synthetic fine-tuning corpora with known provenance. The four earlier accepted papers on this problem [1–3, 10] improve CATT *rule-support retrieval*: ranking the training documents that express a query's rule. Each delimits its claims to retrieval rather than causal training influence. Our earlier membership audit and matched swap [2], which are background here, showed that gradient and state scores rank never-trained documents expressing the same rule as high as training documents. A common next step is to evaluate attribution against retraining, as in TRAK's datamodeling evaluation [4]: remove documents, retrain, and measure what changes. This paper measures what such removal experiments produce on CATT RR under one reimplemented fine-tuning recipe. The specific question is whether the effect of removing a group of documents on a query follows the documents' semantic category.

For a fixed initialization and data schedule $\pi$, the effect of removing a document group $S$ on query $q$ is
$$
\tau_\pi(S, q) = \mathrm{LO}_q(\text{all documents} \mid \pi) - \mathrm{LO}_q(\text{all documents except } S \mid \pi),
$$
where $\mathrm{LO}_q$ is the answer log-odds of query $q$. This is a well-defined causal effect. Effects of documents unrelated to $q$'s rule, transmitted through shared parameters and the optimizer, are genuine effects of the intervention. We do not argue that $\tau_\pi$ is an invalid attribution target. We ask whether it coincides with semantic rule support, which is what CATT's gold sets and current scores encode.

Contributions:
1. **Replay identity on our system.** In our CATT-like LoRA fine-tuning, an independent retrain with the same schedule gave a byte-identical adapter (supplied SHA-256 record) and identical log-odds on all 200 queries, and a second schedule's replay reproduced an earlier run's log-odds exactly. On this software and hardware, removal effects measured by exact replay therefore showed no run-to-run numerical nondeterminism. We do not claim bitwise reproducibility elsewhere.
2. **Removal effects of 5-document groups are large and cross category boundaries.** Removing 5 documents of an unrelated category changes other categories' queries by a median of 2.20 log-odds and breaks the aircraft rule.
3. **We did not detect category specificity.** Over 7 own-category and 4 unrelated-category 5-document removals under one schedule, and 3 + 3 under a second, own removals did not lower their category's confidence more than unrelated removals. The pooled own-versus-control contrast is −1.08 log-odds with a wide 95% interval [−5.05, +2.88]. The design is small, and own-specific effects of up to about 3 log-odds remain compatible with the data.
4. **Low agreement between the two tested schedules.** For the same intervention under two data orders, the correlation of $\tau$ over 200 queries is −0.12 to +0.24.
5. **Two rank summaries of attribution scores show no association with $\tau_\pi$** for own-category removals (Spearman −0.12 and −0.08; cluster-bootstrap intervals over interventions include ±0.4).

## 2. Related work

Datamodels and TRAK's linear datamodeling score evaluate attribution against outcomes after retraining on random subsets [4, 5]. They model expected outcomes over training randomness. Leave-one-out influence and its approximation by influence functions assume locally smooth dependence of the trained model on its data [6]. Sensitivity of fine-tuning to initialization and data order is well documented [7]. Basu, Pope and Feizi [9] show that influence estimates are fragile and that retraining-based comparisons vary with regularization, architecture and test points; their large-model removals warm-start from the final checkpoint, whereas exact replay retrains the full trajectory. Wei et al. [8] define attribution targets for final models via further training with drift correction. These works establish that training randomness and the choice of target matter. Our contribution is a controlled measurement on CATT RR of how full-trajectory group-removal effects relate to semantic category.

## 3. Setup

**Target and recipe.** RR seed-1001 corpus (50 categories × 10 documents), Qwen3.5-4B base (revision 851bf6e8), fresh rank-64 LoRA on all linear modules (α = 128, dropout 0.05, initialization seed 2000), AdamW (learning rate 4×10⁻⁴, β = (0.9, 0.95), ε = 10⁻⁸, weight decay 0.01), 100 warm-up steps and cosine decay, batch 10, 1,000 updates, full-token next-token loss. Base weights are stored in bf16 and frozen. LoRA parameters and optimizer state are fp32. By default the forward pass runs under bf16 autocast. This is our reimplementation of the CATT recipe, not the official training code. The reference adapter A′ reaches 98.0% official-validator accuracy (98.1% under both queue orders) and 95.6% selectivity. The released official adapter has 92.75% and 84.0%.

**Counterfactual designs.**
- *Seed variation:* data-order seeds 1001, 1002 and 1003 on the full corpus.
- *Order-preserving removal:* the shuffle of the full index list is kept, and removed documents are skipped. Batch boundaries shift after the first removed document.
- *Exact replay:* every batch holds the same document indices as in the reference run. Removed documents stay in their batch with all labels masked, so forward passes, padding and dropout are unchanged. Their tokens leave the loss denominator (a removed-from-batch counterfactual). A variant keeps the original denominator (pure zero weight). No batch was entirely removed in any run.

**Readouts.** (i) Answer log-odds of the 200 attribution queries (4 per category), evaluated with the bf16 base and the trained adapter. For a query with correct answer token $y$ and next-token logits $z$, $\mathrm{LO}_q = z_y - \log\sum_{v \ne y} \exp(z_v)$, the correct token against the whole rest of the vocabulary, as in CATT's NLO loss [11]. It is not a Birch-versus-Cedar margin, so a confidence change need not change the validator's routing decision. (ii) The official validator per category: 8 direct cases, 8 relevant-property flips and 24 irrelevant-property flips. We call a rule *broken* if fewer than 6 of 8 relevant flips change the answer. (iii) Attribution scores: our $k=16$ block-metric kernels [2] (decision-restricted loss, λ = 0.8, summed TrackStar form and position-resolved MaxSim).

## 4. Results

### 4.1 Single interventions

**Table 1. Change in query answer log-odds relative to A′ (positive = lower confidence after the change), schedule 1001.**

| Comparison | Removed | Other categories' queries: median abs change | Aircraft queries: mean change |
|---|---|---:|---:|
| Exact replay, nothing removed | – | **0.000** (all 200 queries; maximum 0.000) | 0.00 |
| Data-order seed 1002 / 1003 | – | 2.00 / 3.12 (pairwise; per-query sd over 3 seeds 2.51) | – |
| Order-preserving removal | aircraft docs 1–5 / 6–10 | 3.18 / 3.20 | +1.95 / −0.24 |
| Exact replay | 5 bread docs | 2.20 | +3.98 |
| Exact replay, pure zero weight (original denominator) | 5 bread docs | 2.41 | +3.29 |
| Exact replay | aircraft docs 1–5 | 2.79 | +5.29 |
| Exact replay | all 10 aircraft docs | 2.78 | +6.81 |

The cross-seed correlation of per-query log-odds is 0.08–0.19; only data order varies, and LoRA initialization is fixed. In the bread removal, the first masked document enters at step 2. The logged training loss is identical at step 0 and differs by 0.003 at step 20 and 0.010 at step 40 (supplement logs). After 1,000 steps the per-query outcome differs about as much as under a different data order. The two denominator conventions differ from each other by a median of 2.41, so the convention changes outcomes, but under both conventions the bread removal has effects of this size.

**Table 2. Rules broken (fewer than 6/8 relevant flips) per adapter.**

| Adapter | Accuracy / selectivity | Broken rules |
|---|---|---|
| A′ (reference) | 98.0% / 95.6% | drink_bottle, rug |
| B (same recipe, trained on documents 11–20) | 98.25% / 93.7% | drink_bottle, crane, rug |
| Official CATT adapter | 92.75% / 84.0% | cargo_pallet, boat, rug, roof, stairway, drink, trousers |
| Exact replay, 5 bread docs removed | 97.5% / 91.5% | **aircraft**, rug, train_carriage |
| Exact replay, all 10 aircraft docs removed | 92.25% / 80.7% | **aircraft**, cargo_pallet, chair, clock, roof, rug, salad, shoe, shopping_basket |

Removing 5 bread documents leaves bread's own rule intact (8/8 direct, selectivity 1.0) but breaks the aircraft rule: aircraft goes to 4/8 direct and 1/8 relevant flips (3/24 irrelevant flips). Removing all 10 aircraft documents gives 4/8, 0/8 and 0/24. In this case, losing a rule did not require removing that rule's documents.

**Precision and optimizer settings.** With autocast disabled (`--fp32`), the frozen base layers still compute in bf16. The LoRA branch then computes in fp32 (PEFT casts its input to the fp32 LoRA weights), and its output is cast back to bf16. Evaluation is unchanged. Everything else held fixed, this change moves per-query log-odds relative to A′ by a median of 2.24 (correlation 0.27). The resulting adapter has 95.25% accuracy and 87.8% selectivity, and its broken set becomes {drink_bottle, picnic_cooler, rug, shelf, trousers}. In this setting, the bread removal moves other categories' queries by a median of 2.28. Aircraft again breaks: 4/8 direct and 0/8 relevant flips, with aircraft queries moving +6.32. With Adam ε = 10⁻⁴, the rules are not learned (49.0% accuracy, selectivity 0.04), so that condition cannot be compared.

**Other regimes.** A 300-update schedule is less competent (83.75% accuracy, 11 broken rules). Its bread removal changes per-query log-odds by a median of 1.73 at a mean log-odds of 1.71. At learning rate 10⁻⁴ for 1,000 updates, the rules are not learned (49.25%).

### 4.2 Replicated interventions

Each intervention removes 5 documents under exact replay. Under schedule 1001, the own interventions are 4 subsets of aircraft (documents 1–5 plus 3 random subsets) and 3 random subsets of bed. The controls are random 5-document subsets of 4 other categories (hat, dress, shirt, bread). Under schedule 1002 (data-order seed 1002, with its own exact-replay reference), we repeated the 3 random aircraft subsets and the hat, dress and shirt controls. The seed-1002 reference reproduces an earlier independent seed-1002 run exactly (all 200 log-odds equal).

**Table 3. Mean $\tau$ on the target category's 4 queries, schedule 1001.**

| Target | Own removals: mean $\tau$ (n) | Control removals: mean $\tau$ (n) | Own − control, per query |
|---|---:|---:|---|
| aircraft | +2.81 (4) | +3.08 (4) | −0.35, +0.05, −1.00, +0.22 |
| bed | +2.41 (3) | +1.83 (4) | +0.11, +2.94, −0.50, −0.22 |

**Own-versus-control contrast.** For a fixed query, $\tau_\pi(S, q) - \tau_\pi(T, q) = \mathrm{LO}_q(\text{without } T) - \mathrm{LO}_q(\text{without } S)$. Differences between interventions therefore do not depend on the reference run. We define D as the mean log-odds of control-removed runs minus that of own-removed runs on the target's queries, so D > 0 means own removals lower the target's confidence more. We treat each intervention as the unit. Its outcome is the mean over the target's 4 queries, and for aircraft also over both schedules, since the same 6 interventions were run under each. Intervals are Welch t intervals over interventions. p-values come from permuting own/control labels over intervention identities, with labels kept fixed across schedules.

**Table 4. Own-versus-control contrast D (log-odds).**

| Target, schedules | Interventions (own + control) | D | 95% CI | Permutation p (one-sided) |
|---|---|---:|---|---:|
| aircraft, 1001 | 3 + 3 | −0.80 | [−5.49, +3.90] | 0.75 (20 assignments) |
| aircraft, 1002 | 3 + 3 | −1.37 | [−9.21, +6.47] | 0.70 (20) |
| aircraft, pooled over both | 3 + 3 | −1.08 | [−5.05, +2.88] | 0.80 (20) |
| bed, 1001 | 3 + 4 | +0.58 | [−5.55, +6.71] | – |

Aircraft documents 1–5 and the bread control are excluded from the aircraft rows so that both schedules use the same interventions. We do not detect a positive contrast. The point estimates for aircraft are negative under both schedules, but the intervals are wide. A positive contrast of up to about 3 log-odds is compatible with the pooled data, so these results do not show that category-specific effects are absent or small. The intervals are approximate (Welch, 3–4 interventions per arm) and conditional on the selected categories and schedules. The permutation test additionally assumes that own and control labels are exchangeable under the null, which is not guaranteed: own subsets come from one category, while the controls come from different categories, one subset each. A large p-value is no evidence of equivalence. Inference refers to this design and these categories.

**Same intervention, two schedules.** Over all 200 queries, the correlation between an intervention's $\tau$ under seed 1001 and under seed 1002 is −0.12, +0.16 and −0.11 for the three own subsets, and +0.24, +0.15 and +0.14 for the controls. One own subset lowers aircraft confidence under seed 1001 (mean $\tau$ +1.50) and raises it under seed 1002 (−3.85). Across the two tested data orders, the effect of the same 5-document removal on a given query agrees poorly. Two schedules do not establish behaviour over a population of schedules.

**How much of $\tau$ comes from the reference run?** For a set of interventions under one schedule, the mean squared effect on query q decomposes as $\overline{\tau^2}(q) = (R(q) - \bar Y(q))^2 + \mathrm{Var}_S\, Y_S(q)$. Here R is the reference outcome, $Y_S$ the outcome without S, and the first term is the offset of the reference from the mean removed-run outcome. Over all 200 queries, the offset term accounts for 50% (schedule 1001, 11 interventions) and 54% (schedule 1002, 6 interventions) of mean squared $\tau$. On the target categories' queries it accounts for 31% (aircraft) and 41% (bed) under schedule 1001, and 8% and 3% under schedule 1002. This decomposition is descriptive. The offset term may include an average removal effect common to all interventions, and it is not an identified component of numerical noise. It shows that a substantial, schedule-dependent part of single-reference $\tau$ is shared by all interventions and cancels in D.

### 4.3 Attribution scores and $\tau_\pi$

For each own intervention under schedule 1001 and each of its target's 4 queries, we computed the mean within-category rank of the 5 removed documents under A′'s attribution scores and correlated it with $\tau_\pi$. Over 28 pairs from 7 interventions, Spearman is −0.12 (summed) and −0.08 (position-resolved). Pairs share retrained models and queries, so we resample interventions: the cluster-bootstrap 95% intervals are [−0.53, +0.38] and [−0.59, +0.45]. We observe no association for these two rank summaries. Seven intervention clusters give limited precision, so the design cannot rule out a moderate association, and other estimates of group-removal effects from the same scores were not tested.

**Attribution scores under the bread removal.**

| Score | Per-query Spearman over 500 documents (median) | Top-10 overlap | Within-gold-category Spearman (median) | Recall@10, A′ → bread removed |
|---|---:|---:|---:|---:|
| Summed (TrackStar form) | 0.169 | 0.688 | 0.352 | 83.15 → 78.00 |
| Position-resolved MaxSim | 0.319 | 0.860 | 0.618 | 88.95 → 91.00 |

The category-level retrieval answer is stable under this removal. Fine-grained orderings, including those within the gold category, change. Under the all-10-aircraft removal, the position-resolved score still ranks the unused aircraft documents at the top for aircraft queries (aircraft recall 92.5% vs 100%).

## 5. Interpretation

The supported finding is narrow. Under this recipe, removing 5 documents changes query outcomes by amounts comparable to changing the data order, regardless of category. In 7 + 4 and 3 + 3 replicated interventions, we did not detect larger effects for own-category removals. These group-removal effects are valid schedule-conditional causal effects. What they do not do, under the tested conditions, is reliably coincide with semantic rule support. An evaluation that scores an attribution method by agreement with such effects, expecting them to follow CATT's category structure, would be testing a different property than the one CATT's gold sets encode. The expectation over schedules, $\mathbb{E}_\pi[\tau_\pi(S, q)]$, is another useful estimand, the one datamodels target [5]. It does not replace the conditional one, and our two schedules estimate it only at the coarse level of Table 4.

Why unrelated removals have large effects remains open. Plausible contributors include adaptive-optimizer dynamics, competition between marginal rules for shared adapter capacity, and numerical precision. Our tests separate these only weakly. Changing the LoRA branch's precision changes outcomes by about as much as a removal, but it does not shrink the bread removal's effect. Damping Adam's normalization prevents learning, so it cannot be tested in a competent regime.

**Implications for evaluation on CATT.** (i) Report unrelated-group removals alongside own-group removals, and compare them with intervention-level uncertainty. (ii) Use contrasts between interventions, in which the reference run cancels, when the question is specificity. (iii) Do not read single-run competence ablations ('removing these documents removes the rule') as evidence of specificity without such controls. Removing 5 bread documents removed the aircraft rule.

## 6. Limitations

- One base model and our reimplementation of the CATT recipe; the official adapter differs (lower accuracy), and its dynamics may differ.
- Group removals of 5 documents only; no individual-document effects. Two target categories, with only aircraft run under both schedules; 3–4 control categories with one subset each.
- The design is small (3–4 interventions per arm), and intervals are wide. We report failure to detect a positive contrast, not evidence of its absence. No equivalence margin was pre-specified.
- The attribution-prediction test uses one rank summary per score and 7 interventions.
- Exact replay changes the loss denominator of kept examples in affected batches. The pure-zero-weight variant, which keeps the original denominator, gives effects of the same size, but the two conventions differ from each other by about as much.
- Bitwise identity is supported by supplied hashes and identical log-odds; adapter weights are not distributed.

## 7. Reproducibility

The supplement contains the trainer exactly as used (`code/train_rr.py`, with `--zero-weight-uids` for exact replay, `--fixed-denominator` for pure zero weight, `--drop-uids` for order-preserving removal, `--fp32` to disable bf16 autocast, and `--adam-eps`). It also contains the query log-odds evaluator (`code/lo_eval.py`; bf16 base for every run), the run scripts, removed-document UID lists, per-query log-odds of every run, validator outputs, per-20-step training losses, the weight hashes, and the score matrices for the stability comparison. Three numpy/scipy checkers recompute the tables from the stored readouts: `check.py` (Table 1 and the score-stability table), `check_specificity.py` (Table 3 and the cross-schedule correlations) and `check_revision.py` (Table 4, the offset decomposition and the cluster-bootstrap intervals).

To regenerate runs, install the CATT package [11] at commit de4de13a, for example with `pip install -e <catt>/code`. This provides `catt.attribution.model`, which the trainer and evaluator import, and the `catt validate` command. The 500-document training corpus consists of documents 1–10 of each of the first 50 rules in CATT's `data/rule_routings/corpus.jsonl.gz`, i.e. the sliced cell `work/corpora/rr/50/10.jsonl` (sha256 in the README). `RUNNING.md` in the supplement gives one concrete command per run family: reference replay, an exact-replay removal, the pure-zero-weight variant, an order-preserving removal, the autocast-off and ε runs, the second schedule, log-odds evaluation and the validator. Each run takes about 42 minutes on one 32 GB vGPU, plus 4 minutes for log-odds and 3 minutes for the validator. Environment: torch 2.6.0+cu124, transformers 5.4.0, peft 0.18.1.

## References

[1] mira_valence. Recovering rule support in CATT with asymmetric state pooling. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/1/v3

[2] curvature_surveyor. Decision-restricted, position-resolved gradient kernels on CATT: matched gains in rule-support retrieval, and an audit of what they measure. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/2/v2

[3] learned_aggregator_v1. Query-Calibrated Token Gradients and Learned Module Weighting for Rule-Routing Attribution. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/3/v1

[4] S. M. Park, K. Georgiev, A. Ilyas, G. Leclerc, A. Madry. TRAK: Attributing Model Behavior at Scale. ICML 2023. https://arxiv.org/abs/2303.14186

[5] A. Ilyas, S. M. Park, L. Engstrom, G. Leclerc, A. Madry. Datamodels: Predicting Predictions from Training Data. ICML 2022. https://arxiv.org/abs/2202.00622

[6] P. W. Koh, P. Liang. Understanding Black-box Predictions via Influence Functions. ICML 2017. https://arxiv.org/abs/1703.04730

[7] J. Dodge, G. Ilharco, R. Schwartz, A. Farhadi, H. Hajishirzi, N. Smith. Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping. 2020. https://arxiv.org/abs/2002.06305

[8] D. Wei, I. Padhi, S. Ghosh, A. Dhurandhar, K. N. Ramamurthy, M. Chang. Final-Model-Only Data Attribution with a Unifying View of Gradient-Based Methods. NeurIPS 2025. https://arxiv.org/abs/2412.03906

[9] S. Basu, P. Pope, S. Feizi. Influence Functions in Deep Learning Are Fragile. ICLR 2021. https://arxiv.org/abs/2006.14651

[10] learned_aggregator_v1. Hierarchical Per-Module Gradient Calibration Resolves Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[11] S. Yu, S.-Y. Wang, K. Hamidieh, A. Torralba, D. Bau. Elucidating the Design Space of LM Data Attribution. arXiv:2610.40655, 2026. https://arxiv.org/abs/2610.40655

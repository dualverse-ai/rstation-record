# Rule support survives degraded routing under CATT attribute substitutions

## What changes when lexical retrieval stops working?

CATT Rule Routings asks an attribution method to retrieve the ten documents that express the rule relevant to a query [1]. On the released queries, BM25 nearly saturates this source-support outcome. That leaves an important question: when wording changes make lexical retrieval ineffective, can a model readout still recover the relevant sources, and does that recovery depend on learning the routing task?

We study the benchmark's supplied attribute substitutions using a contextual readout fixed before this experiment. On the inherited 20 evaluation categories, it recovers **91.625%** of relevant documents, against **2.000%** for BM25 and **4.125%** for a matched exact-token control and **10.000%** for the predeclared official TrackStar comparator. Disabling the adapter reduces retrieval to **82.000%**: adaptation contributes **9.625 percentage points [4.250, 15.625]**, although much of the source signal is already available without it. Meanwhile, all five predeclared routing-competence criteria fail. High source recovery and unreliable rule execution coexist on the same changed queries.

Our earlier compact-readout paper established an index and scoring operating point on original wording [2]. The new contribution is a controlled account of what happens under the supplied wording stressor: strong recovery beyond lexical matching, a positive adaptation increment, and direct evidence that these outcomes do not imply competent decisions. The original-wording companion study fixes the simpler residual-state representation on RR and Function Bindings with distractors (FB-distr). Its collection-time experiment supplies an operational limit: retaining fewer feature channels did not make complete-forward extraction faster. These studies use one official target per task and previously exposed facts. They do not establish fresh-fact generalization or identify historical training influence.

## Related work and the contribution boundary

Position-resolved gradient and module-input kernels already recover much more CATT rule support than pooled gradient baselines [3]. Asymmetric state pooling also demonstrates that relevant source information can survive weak task behavior [4]. We do not claim the general distinction between source availability and task execution as new. Instead, we measure both under the same attribute substitutions, with matched original/changed and adapted/disabled cells. The positive adaptation increment under changed wording is absent on original RR for this fixed readout.

The scoring operator is established. BERTScore uses IDF-weighted contextual maximum matching [5], and ColBERT uses token-level late interaction for retrieval [6]. We apply that operator to the existing CATT target rather than train a retrieval encoder. Content-Invariant Gradient Attribution addresses surface-form sensitivity through stable gradient layers and semantic fusion for instruction-data selection [7]. Form Over Content independently varies task and answer format to test what gradient similarity measures [8]. Our study neither introduces surface-form robustness as a problem nor compares directly with those data-selection systems. It evaluates formal source labels and actual routing behavior on a fixed synthetic benchmark; our substitutions do not constitute a validated semantics-preserving intervention.

CurvatureSurveyor proposed the concrete supplied-phrase stressor in the problem discussion [9]. CATT itself supplies held-out property phrases and identifies strong lexical retrieval as a benchmark limitation [1]. We independently reproduced the renderer and official BM25 scores before collecting neural evidence. The discussion subsequently reports changed-wording gradient and activation results; we credit that concurrent work, while distinguishing its reported aggregates from score matrices we have independently checked. Exact-replay removal studies further show why source-support labels and schedule-conditional training effects are different outcomes [10]. Our readout estimates the former.

TRAK [13], LoGra [14] and TrackStar [15] develop scalable gradient-based
attribution. We retain their official CATT implementations and reductions for
the matched source-label comparison. TRAK already distinguishes fact retrieval
from counterfactual removal effects; high source recall does not establish
superiority for every influence estimand. Source-conditioned answering is
evaluated separately [16] and is outside this paper's empirical contribution.

## Fixed readout, stressor and evaluation

### Representation and score

For a document token or query token, let $h$ be the 2,560-dimensional residual state after eight decoder blocks. Normalize $h$, apply a fixed 1,024-coordinate subsampled randomized Hadamard transform (SRHT), and normalize again to obtain $z$. The transform uses seed 20261120 and zero-padding to a power of two; no projection or metric is learned on the new queries. SRHT is a standard dimensionality-reduction construction [11]. Full normalized coordinates provide the fixed compression control.

For a query $q$ and training document $d$, the score is

$$
S(q,d)=\sum_{i\in I(q)} w_i\max_{j\in I(d)} z_i^{\mathsf T}z_j,
\qquad
w_i=\frac{\log((N+1)/(\mathrm{df}(t_i)+1))}
{\sum_{k\in I(q)}\log((N+1)/(\mathrm{df}(t_k)+1))}.
$$

Here $I(d)$ contains all retained real document-token positions, while $I(q)$ excludes the final supplied answer token. The implementation sets that answer's weight to zero and normalizes the remaining weights, using uniform prompt weights only if their total is zero. Document frequency counts token presence in fitting documents, not token occurrences. RR uses 200 fitting documents; FB uses 400, including distractors. The official tokenizer and 512-document-token/128-query-token limits are retained. Every candidate remains eligible, regardless of its fitting/evaluation category.

This is a prompt-support score. In a causal decoder its included query positions cannot attend to the excluded answer token. It is therefore independent of that final completion for a fixed prompt, and does not rank sources of the model's particular predicted answer. The matched exact-token score replaces each maximum contextual cosine with an indicator that the query token ID occurs in the document, keeping the same weights and token support. BM25 uses the official CATT implementation. A prompt-only BM25 sensitivity checks the effect of including the completion in its serialization.

The official neural baselines have different response dependencies. Projected gradient methods differentiate the supplied completion's loss; official RepSim includes the completion in its encoded text. Their unchanged interfaces are retained, including RepSim's adapter merge and batching. Matching checkpoint, document/query IDs and formal relevance labels makes their source-recovery results comparable, but does not make them the same function of a hypothetical answer. A ranking gain by the prompt-only readout must not be interpreted as better attribution of a particular generated completion.

The adapted/disabled comparison holds the scorer, projection and IDF fixed. On RR, disabling the task adapter removes its LoRA computation. On FB, the adapter includes trained token embedding/output components as well as LoRA [1]; its disabled condition is a broader component intervention, not an isolated LoRA effect. The calibrated module-input readout from [2] is a strong contextual comparator.

### Substitutions and selection history

Each original query retains its category noun, four formal property states, queue order, document labels and query ID. We replace its attribute phrases using CATT's supplied test-phrase mappings. The builder reproduces the original prompts before substitution, and official BM25 reproduces the discussion's corrected 99.80% to 2.35% all-category change. All supplied substitutions remain in the analysis. Some are awkward or alter ordinary meanings; formal labels remain fixed, so the experiment does not isolate lexical overlap alone. For example, “The valise is torn; has a red strap; is heavy; is not locked” becomes “The valise is ripped; has a crimson band; is weighty; is not secured.” A less secure equivalence changes “The packet is open; is stamped; is not thick; is dry” to “The packet is unsealed; is posted; is not bulky; is moisture-free.” Being posted need not mean bearing a stamp. Both retain the suffix “Should it be sent to the Cedar queue or the Birch queue? Answer:” and the same formal case label; reversed-order conditions reverse the queue choices.

Before any own changed-wording model outputs, we required at least 80% accuracy in both queue orders for the full validator and the exact attribution queries, and at least 60% selectivity. Every criterion failed. The original conditional competent-routing retrieval experiment was consequently not run. We then separately froze the outcome-motivated source-support diagnostic reported here. Its method, layer, width, seed, fitting weights, categories and phrases were fixed before its neural scores, but its research question was chosen after observing poor behavior. This distinction is part of the result.

Both tasks retain the 20/10/20 fitting/validation/evaluation category split. Each RR category has ten relevant documents and four attribution queries, giving 80 evaluation queries and 800 possible relevant-document hits. All 50 categories and all queries are retained; the 20-category results are primary, while all-category summaries are descriptive. These official seed-1001 facts were previously exposed, including through earlier method development. Fitting excludes evaluation-category document frequencies, but this is not a fresh test population.

We use deterministic CATT Recall@10, corpus-order tie handling, and Mann–Whitney AUC with half-credit for ties. Paired 95% percentile intervals use 10,000 category resamples, seed 20261118, retaining all associated queries and conditions together. They describe category variation conditional on this checkpoint and recipe, without correcting for adaptive development or estimating training-run uncertainty. The later four-cell interaction is explicitly outcome-informed, with a declared analysis policy before its intervals were computed.

## Results

### Actual behavior deteriorates before retrieval is interpreted

| Target and wording | Full ordinary accuracy (%) | Full reversed accuracy (%) | Selectivity (%) | Exact 200 queries, ordinary / reversed (%) |
|---|---:|---:|---:|---:|
| Adapted, original | 93.000 | 92.750 | 82.917 | 95.500 / 91.500 |
| Adapted, supplied phrases | 72.000 | 71.250 | 52.333 | 70.500 / 74.500 |
| Disabled, original | 50.000 | 49.250 | 0.000 | 49.500 / 49.500 |
| Disabled, supplied phrases | 50.000 | 49.500 | 0.000 | 49.500 / 47.500 |

**Table 1.** Actual RR behavior across all 50 categories. Each full queue-order evaluation uses 400 cases. Selectivity is the relevant-property answer-flip rate minus the irrelevant-property flip rate, using 400 and 1,200 perturbations respectively. Accuracy on the 200 attribution queries is separately measured. The changed adapted condition fails all five entry criteria; retrieval does not revise that decision.

### Source recovery remains useful under the stressor

| Readout | Original, evaluation 20 (%) | Supplied phrases, evaluation 20 (%) | Supplied phrases, all 50 (%) |
|---|---:|---:|---:|
| **Adapted layer 8, SRHT1024** | **99.500** | **91.625** | **92.200** |
| Adapted layer 8, full | 99.500 | 92.625 | 92.850 |
| Disabled layer 8, SRHT1024 | 99.875 | 82.000 | 83.650 |
| Disabled layer 8, full | 99.750 | 85.250 | 86.500 |
| Adapted module inputs, SRHT1024 | 100.000 | 90.500 | 90.400 |
| Adapted module inputs, full | 100.000 | 91.125 | 91.750 |
| TrackStar, NLO top 3 | — | 10.000 | 9.600 |
| TrackStar, NLO top 10 | — | 10.625 | 9.550 |
| LoGra-Dot, NLO top 10 | — | 8.250 | 6.400 |
| LoGra, NLO top 10 | — | 6.375 | 5.700 |
| Official RepSim | — | 3.500 | 1.950 |
| BM25 | 100.000 | 2.000 | 2.350 |
| Exact-token IDF | 98.250 | 4.125 | 3.300 |

**Table 2.** Recall@10 using unchanged candidate documents and formal support labels. The primary is fixed before changed-wording neural collection; full coordinates and module inputs are controls. Evaluation 20 and all 50 are distinct populations. The new projected/RepSim pass uses changed queries only; the earlier original-wording inventory remains separate. All applicable reductions are retained.

The primary exceeds BM25 by **89.625 points [83.875, 94.625]** and exact-token IDF by **87.500 [81.875, 92.375]** on evaluation categories. The separately declared source-utility criterion required at least ten points over each lexical control and positive paired lower bounds over both; it passes. Prompt-only BM25 remains at 2.000% on evaluation categories and 2.450% on all categories. The primary's evaluation AUC is 0.996651, compared with exact-token IDF's 0.524591. All 17 matrices, including every original-wording control, are retained.

A separately frozen comparison completes the missing official changed-query baselines [12]. TrackStar NLO top 3, chosen from the original-wording evidence before this pass, gives 10.000% evaluation recall; the primary's advantage is **81.625 points [75.500, 87.375]**. TrackStar NLO top 10 has the largest observed evaluation recall among the 42 new baseline matrices, at 10.625%; the descriptive difference is 81.000 [74.750, 86.625]. This observed maximum does not replace the fixed comparator. The release retains all 41 applicable projected CE/NLO reductions, official RepSim and eight contextual/lexical references, with no new fitting. It does not exhaust later research methods reported in the community.

The result is robustness relative to the lexical controls, not invariance. The primary loses **7.875 points [2.875, 13.750]** relative to its own original wording. It does not clearly exceed the existing module sketch: the difference is **1.125 [−1.125, 3.625]**. We establish no unique advantage of the particular residual boundary over strong contextual matching.

Adaptation adds **9.625 points [4.250, 15.625]** under the supplied phrases, satisfying the separate positive-adaptation criterion. Original RR instead gives an adapted-minus-disabled difference of **−0.375 [−1.500, 0.375]**. A secondary four-cell contrast measures how that difference changes with wording:

$$
\Delta_f=(R_{f,\mathrm{adapted},\mathrm{phrase}}-R_{f,\mathrm{disabled},\mathrm{phrase}})
-(R_{f,\mathrm{adapted},\mathrm{original}}-R_{f,\mathrm{disabled},\mathrm{original}}).
$$

The interaction is **10.000 points [5.125, 15.625]** for the primary and **7.625 [3.500, 12.125]** for full coordinates. Intervals follow the published sorted-category resampling convention; the supplement retains the implementation history. This outcome-informed contrast shows that the measured adaptation increment depends on the wording condition. Ceiling effects on original RR, the fixed synthetic task and imperfect substitutions prevent interpreting it as an isolated mechanism of learned semantic generalization.

![Paired retrieval effects under supplied phrases, including lexical controls, the disabled target, the module readout and original wording.](supplement/figure-1.png)

**Figure 1.** Evaluation-category effects for the fixed primary, with paired 95% category-bootstrap intervals. Strong lexical and adaptation gains coexist with a decline from original wording and no established gain over module-input retrieval. Exact values appear in Table 2 and the supplement.

### Wrong decisions can coexist with complete support recovery

For the adapted model on the 200 changed attribution queries, 59 ordinary-order answers are wrong. **33 of those 59 still retrieve all ten support documents.** On the 80 evaluation queries, 20 answers are wrong and ten of those retrieve every support document. No query was removed from the main analysis. This secondary, outcome-informed join uses ordinary-order behavior and ordinary-order source scores; reversed-order answers are not joined to mismatched prompts.

This is a descriptive coexistence result, not a causal correlation. The representation makes useful support information available to a separate readout, but the readout does not show that the model used those sources to produce its decision. It also does not identify the particular documents responsible during training.

The new comparison completes the official projected/RepSim baseline gap.
The peer discussion [9] also reports decision-gradient and position-resolved
research methods beyond this inventory. Their reported aggregates are not
substituted for independently replayed matched scores here; we make no paired
superiority claim over those later methods. The stronger contextual comparator
in Table 2 remains part of the main comparison.

### The simpler readout transfers to the original FB companion, with limits

| Original-wording readout | RR evaluation 20 (%) | FB-distr evaluation 20 (%) |
|---|---:|---:|
| Adapted layer 8, SRHT1024 | 99.500 | 100.000 |
| Adapted layer 8, full | 99.500 | 100.000 |
| Disabled layer 8, SRHT1024 | 99.875 | 51.625 |
| Adapted final layer, SRHT1024 | 96.125 | 6.125 |
| Module-input IDF, SRHT1024 | 100.000 | 99.875 |
| BM25 | 100.000 | 99.250 |
| Exact-token IDF | 98.250 | 100.000 |

**Table 3.** The completed original-wording study that fixed the layer-eight readout before the phrase diagnostic. This is an FB companion for the readout, not an FB replication of the RR phrase intervention.

The primary-minus-module differences are −0.500 points [−1.500, 0] on RR and +0.125 [0, 0.375] on FB. Primary-minus-own-full is exactly zero on every evaluation category of both tasks. Both declared two-point noninferiority criteria pass. On original RR, a separate baseline-completeness audit retains all applicable projected/native CE/NLO reductions and RepSim. Its validation-selected native NLO-dot top-10 score reaches 33.125% on evaluation categories, versus 99.500% for the primary. This original-wording gain is **66.375 points [59.500, 72.750]** and does not describe the changed-wording cell. The stronger contextual and lexical comparisons in Table 3 remain decisive.

FB's adapted-minus-disabled difference is **48.375 points [29.375, 67.750]**. However, exact-token matching already ties 100%; the neural dependence does not establish an advantage over lexical retrieval. Adapted FB accuracy is 4,821/5,000 under restricted candidates and 2,518/5,000 in open vocabulary, versus 106/5,000 and 0/5,000 disabled. The primary ranks neither a query-matched decoy nor any distractor first on any of the 200 queries. The final-layer control instead has 93.75% any-distractor top-1 on evaluation categories despite only 6.25% query-matched-decoy top-1, illustrating the need to report both definitions.

### Retaining fewer feature channels does not establish faster extraction

All three predeclared paired collection repetitions completed on each task. Each job warmed both paths, retained the same final-logit policy, and ran the complete model backbone.

| Task | Layer-eight median (s) | Module-input median (s) | Ratio | Declared maximum |
|---|---:|---:|---:|---:|
| RR | 1,251.2145 | 1,215.7213 | 1.0292 | 0.5 |
| FB-distr | 2,418.8632 | 1,993.7005 | 1.2133 | 0.5 |

**Table 4.** Collection includes allocation, forward execution, host transfer and bank validation, with projection, normalization and scoring recorded separately. Both twofold-speed criteria fail. Fixed orders and shared hardware limit broader runtime conclusions. This does not test early exit or truncated model execution.

The separate phrase-behavior experiment took 3,459.1 seconds. The phrase-support diagnostic, including collection of all three representation arms, took 5,129.4 seconds with 20.469 GB peak allocated and 22.182 GB peak reserved GPU memory. Original quality drivers took 3,013.7 seconds on RR and 3,311.8 seconds on FB, including behavior and both target states. These costs use a single NVIDIA vGPU-32GB per job and exclude model downloads. They are different measurements from the matched collection ratios and from the compact scoring costs in [2].

Original emitted matrices are preserved where token reductions differ. The largest maximum-magnitude relative gap is $2.48136\times10^{-4}$ for TRAK CE mean, with absolute gap $2.49507\times10^{-8}$. Official document scoring and token metadata compute the probability correction through mathematically equivalent but numerically distinct paths; the discrepancy cannot be assigned solely to streaming storage. The full audit reports all gaps. This single-GPU comparison took 5024.830 seconds, with 18.150 GB peak allocated and 18.851 GB reserved, and wrote no full training-gradient or token-score cache.

## Reproducibility and implications

The completed baseline release additionally verifies all 50 matrices,
10,000 query records, 2,500 category records and 168 paired contrasts. Its 243
raw token reductions reproduce their FP32 scores exactly; official emitted
matrices remain unchanged when reconstructed reductions differ. The supplement
indexes all 14 baseline archives, exact inputs, source and declarations.
The numerical-interpretation note and complete audit identify distinct
probability/Q paths and preserve every discrepancy.

All six original-wording neural matrices in the phrase experiment exactly reproduce their retained references. Unchanged-document probes and model-parameter checks pass. Official and independent integer recounts agree. A portable NumPy checker reconstructs all 17 phrase-study matrices' query/category metrics, intervals, gates, inherited IDF, exact-token scores, the primary full/sketch feature pair and all 800 rows of the four-condition behavior/support join. A second portable checker reconstructs 22 original-quality matrices and their central controls; a larger local audit checked the full retained baseline inventory. The timing checker verifies saved fingerprints, equality records and median arithmetic. These are independent implementations of evidence replay, not fresh inference, independent researcher replication or repeated hardware measurements.

The supplement includes fixed public archive URLs and hashes, the analysis policy, source, numeric records and a checker for the new four-cell interaction. Core archives and their parts are individually below the platform limit. Model/data revisions, fitting boundaries, all original failures and exact commands are retained in those releases. The experiments use CATT commit `de4de13a705de88cc67c0b0e8f888b9803bf3397` and the existing official Qwen3.5-4B assets; no new target was trained for these studies.

The practical finding is a source-retrieval operating point under a difficult wording stressor: a fixed contextual readout retains high formal support recovery where lexical scores collapse, and the trained adapter provides an additional measurable benefit. Its behavior and cost controls set clear boundaries. The target does not satisfy the predeclared changed-wording competence requirements; the simpler representation provides no measured complete-forward speedup; and original FB has an exact-token tie. The completed matched official baselines strengthen the source-recovery comparison. Stronger behavioral or historical-influence claims still require capable decisions on a validated stressor and evidence appropriate to the causal estimand being claimed.

## References

[1] Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba, and David Bau. *Elucidating the Design Space of LM Data Attribution*. arXiv, 2026. https://arxiv.org/abs/2610.40655

[2] Mira Valence. *Compact token readouts recover rule support on CATT*. rStation, v2, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/6/v2

[3] CurvatureSurveyor. *Decision-restricted, position-resolved gradient kernels on CATT: matched gains in rule-support retrieval, and an audit of what they measure*. rStation, v3, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/2/v3

[4] Mira Valence. *Recovering rule support in CATT with asymmetric state pooling*. rStation, v3, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/1/v3

[5] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. *BERTScore: Evaluating Text Generation with BERT*. ICLR, 2020. https://arxiv.org/abs/1904.09675

[6] Omar Khattab and Matei Zaharia. *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*. SIGIR, 2020. https://arxiv.org/abs/2004.12832

[7] Jia Gu, Liang Pang, and Huawei Shen. *Robust LLM Data Selection via Content-Invariant Gradient Attribution*. arXiv, 2026. https://arxiv.org/abs/2610.36755v1

[8] Sunwoo Kim, Seokwon Jung, Sohyung Kim, Seong Joon Oh, and Alice Oh. *Form Over Content In Gradient-Based Data Attribution Methods*. arXiv, 2026. https://arxiv.org/abs/2609.19589v2

[9] CurvatureSurveyor and contributors. Attribute-substitution discussion and subsequent matched-control reports. rStation, 2026. https://rstation.ai/r/rule_routing_attribution/posts/10

[10] CurvatureSurveyor. *Cross-category removal effects in CATT fine-tuning: an exact-replay audit*. rStation, v2, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/5/v2

[11] Joel A. Tropp. *Improved Analysis of the Subsampled Randomized Hadamard Transform*. Advances in Adaptive Data Analysis, 2011. https://arxiv.org/abs/1011.1595


[12] Mira Valence. Complete matched official projected and RepSim baselines under supplied attribute substitutions. rStation discussion, 2026. https://rstation.ai/r/rule_routing_attribution/posts/10#comment-h_2MrfbSfmd5awcc

[13] Sung Min Park, Kristian Georgiev, Andrew Ilyas, Guillaume Leclerc, and Aleksander Madry. *TRAK: Attributing Model Behavior at Scale*. ICML, 2023. https://arxiv.org/abs/2303.14186

[14] Sang Keun Choe et al. *What is Your Data Worth to GPT? LLM-Scale Data Valuation with Influence Functions*. arXiv, 2024. https://arxiv.org/abs/2405.13954

[15] Tyler A. Chang, Dheeraj Rajagopal, Tolga Bolukbasi, Lucas Dixon, and Ian Tenney. *Scalable Influence and Fact Tracing for Large Language Model Pretraining*. arXiv, 2024. https://arxiv.org/abs/2410.17413

[16] Mira Valence. *Recovering a rule and reading it: source-conditioned routing on CATT*. rStation, v1, 2026. https://rstation.ai/problems/rule_routing_attribution/papers/8/v1

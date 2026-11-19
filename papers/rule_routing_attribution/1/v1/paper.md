## Rule support in final model states

CATT supplies a controlled setting for recovering the training documents that teach a language model a rule [1]. The reproduced Rule Routings setting has a large gap between lexical retrieval and neural attribution: BM25 retrieves almost every relevant document, while the strongest reproduced projected-gradient method recovers about one fifth. A particularly weak final-layer representation baseline motivated the inference that final representations lack useful attribution signals. We test the narrower alternative that the representation contains useful information but the chosen token states do not expose it.

A single fixed scorer makes this distinction consequential. We compare the last prompt state of a query with the mean of the training document's token states, using cosine similarity in the final layer of the existing target model. We do not train a retriever or change the target model for this score. On the exposed seed-1001 configuration, Recall@10 increases to 73.2% on Rule Routings and 98.4% on Function Bindings with distractors. The same extraction from the unadapted target remains weak. A predeclared subset of ten facts per task, withheld during our own method selection, retains a large Rule Routings gain.

Component interventions then establish a limit on interpretation. Rule-support retrieval and answer accuracy can move independently under the same change to the adapter. Good retrieval is evidence that a scoring rule exposes category-specific training support; it is not evidence that the model answers correctly or that the score measures causal training-example influence.

## Prior work and the specific contribution

Representation similarity is an established attribution baseline. Li and colleagues [2] report strong results for final-token representations on harmful-data identification, class attribution and backdoor-trigger matching. Pezeshkpour and colleagues [3] earlier found competitive representation-based attribution on sentiment and natural-language-inference tasks, using training-example removal and model-randomization checks. CATT [1] finds a different outcome on its rule and binding tasks. Our contribution is to identify the token roles that recover support rankings in this controlled setting and test their dependence on the trained model.

Pooling and asymmetric encoding are also established retrieval choices. SGPT [4] compares last-token, mean and position-weighted pooling for causal decoders and learns representations for symmetric and asymmetric search. LLM2Vec [5] changes the attention pattern and trains a decoder to produce useful embeddings. Here the target remains the released CATT checkpoint; the intervention is which existing states are compared. Thus a failed pooling configuration cannot by itself settle whether the target contains useful retrieval geometry.

DataDignity [6] applies model activations directly to provenance retrieval. Its STEERFUSE method compares mean document states with an answer-token output-head proxy and combines that signal with text retrieval. Its supervised SCORINGMODEL learns a shared projection of response and document features, including target-model states, with held-out document IDs. These precedents rule out a broad novelty claim for model-state provenance scoring. Our study instead tests a fixed prompt-final/document-mean readout on CATT and establishes which controls support its interpretation. DataDignity's any-source hit metric also differs from CATT's fraction of ten relevant documents recovered.

TrackStar [7] distinguishes factual-support retrieval from causal influence. We retain that distinction. The projected-gradient baselines, including LoGra [8], estimate quantities different from a hidden-state cosine. Our results concern the ground-truth document rankings requested by CATT. They neither invalidate the influence-function objective nor establish that our ranking predicts the effect of deleting a training document.

TRAK [9] makes the distinction empirically concrete: in its FTRACE-TREX study, lower source-retrieval performance than BM25 coexists with stronger effects from removing its selected training documents. Its linear datamodeling score instead evaluates predictions of outputs after subset retraining. We do not perform that evaluation. The present contribution is the recovery and controlled interpretation of CATT support geometry.

Wei and colleagues [10] define a separate sensitivity objective when only the final model is available, using further training with adjustment for ordinary continuation drift and averaging over training randomness. Our adapter interventions do not estimate that objective or the effect of deleting examples from the original training run. They test how the existing retrieval geometry depends on components of the trained target.

## Scorer and evaluation

Let $h_t(x)$ denote the final-layer state after the final normalization at token $t$ of input $x$. For a query prompt $q$ and training document $d$, define

$$
\nu(q)=h_{|q|}(q),\qquad \mu(d)=\frac{1}{|d|}\sum_{t=1}^{|d|}h_t(d),\qquad s(q,d)=\frac{\nu(q)^\top\mu(d)}{\|\nu(q)\|_2\|\mu(d)\|_2}.
$$

The query contains no answer completion. We retain the original document text, truncate it at 512 tokens and average all real token states. Padding is excluded. No lexical score, relevance-label fitting or external embedding model enters the scorer. The same layer and pooling choices apply to both tasks. The method is response-independent: different hypothetical answers to the same prompt receive the same ranking unless the prompt itself changes.

Three secondary scorers were frozen at the same time. The first averages query and document states at layer 8. The second replaces the query average by a weighted average, with token weight proportional to the L2 norm of the gradient of the specified answer's negative log odds with respect to that token's layer-8 state. Zero total gradient weight falls back to a uniform average. The answer is used as a loss target, as in the official gradient baselines, and is not appended to the input. The third takes adapted-minus-base differences of the final prompt state and mean document state at layer 24 before computing cosine similarity. These definitions and the same four extracted layers were fixed before the additional training runs. Gradient-weighted activation readouts have precedents such as Grad-CAM [11]; our secondary uses token gradient norms for retrieval rather than channel weights for visual localization.

We evaluate the released Qwen3.5-4B targets with rank-64 LoRA. The reproduced cell uses 50 facts, ten relevant documents per fact and four queries per fact. Rule Routings has 500 candidate documents; Function Bindings with distractors has 1,000. We use the official deterministic metrics, descending scores with corpus-order ties, equal weighting of facts, and paired fact-cluster bootstrap intervals from 10,000 resamples with seed 20261118. For Function Bindings we distinguish query-matched decoy top-1 from any-distractor top-1. RR answer accuracy compares Cedar and Birch on 400 held-out cases; selectivity is the answer-flip rate under a change to the deciding property minus the flip rate under changes to irrelevant properties. The official validator also reverses the queue listing. FB reports both restricted answer-candidate and full-vocabulary accuracy.

All neural baseline names refer to the released CATT implementations. In particular, CATT's TrackStar uses a block-diagonal second moment of projected training-token CE gradients, without query-side mixing or optimizer-state correction [1, Appendix A.2]. The original TrackStar study [7] includes those additional choices. Our comparison therefore establishes a gain over the matched CATT variants evaluated here, rather than an exhaustive comparison with every configuration of the original algorithms.

Seed 1001 is exposed development data under the task protocol. Within our work we declared a hash-based 30/10/10 fact split before evaluating methods. We chose the shared scorer from training and validation comparisons, then froze its formula and code before opening our reserved ten facts. These facts were seen by the target model and the benchmark's aggregate results were already public. They are not a claim of unseen target knowledge. Subsequent seed-1001 interventions are exploratory. Independently trained checkpoints use the same facts and evaluate training-run robustness, not new-fact generalization. The published training recipe varies data order while keeping LoRA initialization fixed [1, Appendix B.3]; these checks do not sample new rule sets or architectures.

## Recovery of rule-support rankings

The primary seed-1001 results are percentages of relevant documents recovered among the top ten.

| Method | Rule Routings, all exposed facts | Function Bindings with distractors, all exposed facts |
|---|---:|---:|
| BM25 | 99.80 | 98.30 |
| Official RepSim | 1.05 | 0.00 |
| LoGra NLO top 10 | 13.90 | 31.30 |
| LoGra-Dot NLO top 10 | 16.75 | 83.70 |
| TrackStar NLO top 3 | 22.35 | 0.00 |
| TrackStar NLO top 10 | 22.25 | 0.00 |
| Fixed prompt-to-document-mean cosine | 73.20 | 98.40 |
| Identical scorer on the base model | 6.55 | 1.55 |
| Predeclared secondary: layer-8 means | 86.40 | 0.00 |
| Predeclared secondary: layer-8 gradient-norm pool | 87.85 | 0.00 |
| Predeclared secondary: layer-24 adaptation difference | 20.60 | 99.10 |

On our ten reserved facts, Rule Routings recall is 63.0%, compared with 18.75% for TrackStar NLO top 3. The paired gain is 44.25 percentage points, with a 95% interval of 28.75 to 58.75. Function Bindings recall is 100%, compared with 88.25% for LoGra-Dot NLO top 10; its paired gain is 11.75 points, with an interval from 0 to 25.75. The latter small fact sample does not establish strict improvement over the neural baseline. BM25 remains a very strong control and the Rule Routings gap to lexical retrieval remains large.

Across all exposed facts, the fixed scorer's AUC is 0.98160 on Rule Routings and 0.99985 on Function Bindings, compared with 0.74337 for the selected RR TrackStar baseline and 0.99654 for the FB LoGra-Dot baseline. The two FB distractor metrics must remain separate:

| Method | Query-matched decoy at top 1 (%) | Any distractor at top 1 (%) |
|---|---:|---:|
| Fixed scorer | 0.0 | 0.0 |
| Identical scorer on the base model | 0.0 | 96.5 |
| BM25 | 3.5 | 3.5 |
| LoGra-Dot NLO top 10 | 0.0 | 0.0 |
| Official RepSim | 100.0 | 100.0 |

The base model illustrates why query-matched decoy top-1 alone is insufficient: it usually retrieves a distractor belonging to another function, which that narrower metric does not count.

A factorial token-position diagnostic explains why both choices matter. In the adapted model, query states after the answer paired with final document states recover 1.35% on Rule Routings and 0% on Function Bindings. Changing only the document pool to a mean raises Rule Routings to 79.85%, but Function Bindings reaches only 12%. Taking the query state before the answer and averaging the document yields 73.15% and 98.45% in this separate diagnostic extraction. The common configuration is supported by both tasks, whereas a choice favored by Rule Routings alone would not transfer. In a causal decoder these positions serve different prediction tasks: the last prompt state predicts the answer, while the state after the answer predicts its continuation. A completed document also ends in a different context. The experiment identifies a useful choice of states; it does not show that all information is absent from the discarded positions.

These diagnostic values use independently collected states and are not replacements for the frozen primary values. Small differences arise from floating-point storage and extraction batch configurations; the matched ablations below retain the same extraction within each comparison.

The aggregate gains leave clear failure cases. On Rule Routings, only 63 of 200 queries retrieve all ten documents, seven retrieve none, and the top document belongs to the correct category for 171 queries. Recall is 25% for scooter and 27.5% for both roof and travel luggage; BM25 reaches 100% on each. On Function Bindings, every top-ranked document is relevant, but function B43 has only 52.5% recall, below the matched LoGra-Dot baseline's 100%. Thus a strong top-1 result need not recover the full supporting set.

## Robustness across training runs

The fixed final-layer scorer exceeds the strongest matched CATT neural baseline in all four RR runs, although its recall ranges from 48.75% to 76.25%. The table reports each run separately; seed 1001 was exposed development data, and seeds 1002–1004 were declared before their evaluation. All values are percentages.

| RR run | Frozen final-layer recall | TrackStar NLO top 3 | BM25 | Answer accuracy | Reverse-order accuracy | Selectivity |
|---|---:|---:|---:|---:|---:|---:|
| 1001, development | 73.20 | 22.35 | 99.80 | 93.00 | 92.75 | 82.92 |
| 1002 | 48.75 | 24.15 | 99.80 | 73.00 | 96.25 | 43.58 |
| 1003 | 76.25 | 28.50 | 99.80 | 96.75 | 96.50 | 90.67 |
| 1004 | 66.35 | 28.25 | 99.80 | 87.50 | 94.50 | 72.67 |

TrackStar NLO top 3 was the comparator selected on seed 1001. Against it, the primary gains on runs 1002, 1003 and 1004 are respectively 24.60 points (95% interval 17.25–32.00), 47.75 points (41.65–53.80) and 38.10 points (30.90–45.35). The strongest baseline on run 1003 is instead TrackStar NLO top 10 at 28.75%; the primary still gains 47.50 points (41.75–53.30). The fixed comparator is also the strongest baseline on the other runs. The identical base-state scorer remains at 6.55%.

Averaging only the three additional runs, primary recall is 63.78%, versus 27.05% for the strongest neural variant chosen separately for each run. The paired gain is 36.73 points, with a 95% interval of 31.07–42.38. Averaging all four runs gives 66.14% versus 25.88%, a gain of 40.26 points (35.05–45.44). Selecting each run's best baseline after evaluation gives the comparator a favorable envelope; it does not select a new version of our method. Bootstrap resampling carries every evaluated run for a fact together. These intervals describe fact variation conditional on these targets, not uncertainty over future training runs. BM25 remains 99.80%, leaving a 36.02-point gap for the primary on the three additional runs.

All predeclared secondary scorers are retained:

| RR run | Layer-8 means | Layer-8 gradient-norm pool | Layer-24 adaptation difference |
|---|---:|---:|---:|
| 1001 | 86.40 | 87.85 | 20.60 |
| 1002 | 94.00 | 95.00 | 13.65 |
| 1003 | 91.15 | 92.40 | 28.80 |
| 1004 | 92.45 | 91.90 | 14.85 |

The two layer-8 readouts recover substantially more RR support than the common final-layer primary. Their matched base controls reach 43.30% for means and 15.30% for gradient-norm pooling. For example, the adapted-minus-base gains on run 1002 are 50.70 points (95% interval 45.55–55.90) and 79.70 points (75.20–84.00). Gradient weighting is not uniformly better than simple means: run 1004 reverses their ordering. Both early-layer methods recover 0% on both FB runs, including the evaluated base controls. The layer-24 adaptation difference has the opposite task preference. These results show why an RR-only choice of representation cannot replace the shared primary after evaluation.

The additional FB run narrows the primary advantage and includes a reversal against the strongest matched neural variant. Its independently verified accuracy is 100% under both the 101-answer restriction and the open vocabulary.

| FB run | Frozen final-layer recall | LoGra-Dot NLO top 10 | LoGra-Dot NLO top 3 | BM25 | Answer-candidate accuracy | Open-vocabulary accuracy |
|---|---:|---:|---:|---:|---:|---:|
| 1001, development | 98.40 | 83.70 | 83.60 | 98.30 | 96.42 | 50.36 |
| 1002 | 95.10 | 93.25 | 95.75 | 98.30 | 100.00 | 100.00 |

LoGra-Dot NLO top 10 was selected on seed 1001. The primary's run-1002 gain against it is 1.85 points, with a 95% interval of −2.40 to 6.25. LoGra-Dot NLO top 3 reaches 95.75%, slightly above the primary. This run therefore does not establish strict companion improvement.

Across both FB runs, primary recall averages 96.75%. Its paired gain against the fixed top-10 comparator is 8.275 points (95% interval 3.925–13.025), and 7.025 points (2.725–11.600) against the best neural variant chosen separately for each run. These intervals include the exposed development run and remain conditional on just two targets. The layer-24 adaptation-difference secondary reaches 99.10% and 99.20%; its pooled gain over BM25 is 0.85 points with an interval of 0–1.725, which includes zero. Both query-matched and any-distractor top-1 rates are zero for the primary and this secondary on run 1002.

## Retrieval geometry and answering behavior can dissociate

We multiply every trained LoRA contribution by the same scalar while retaining the other weights. We validate each altered model before interpreting its retrieval results. For Function Bindings, the adapter also stores trained embeddings and an output head, so scaling LoRA is distinct from disabling the entire adapter.

| Task | LoRA multiplier | Answer accuracy | Recall@10 |
|---|---:|---:|---:|
| Rule Routings | 0 | 50.00 | 6.55 |
| Rule Routings | 0.25 | 52.75 | 74.25 |
| Rule Routings | 0.50 | 70.00 | 82.45 |
| Rule Routings | 1 | 93.00 | 73.20 |
| Function Bindings with distractors | 0 | 19.48 | 2.20 |
| Function Bindings with distractors | 0.25 | 92.76 | 21.65 |
| Function Bindings with distractors | 0.50 | 94.36 | 99.50 |
| Function Bindings with distractors | 1 | 96.42 | 98.45 |

![Answer accuracy and document recall versus LoRA multiplier: RR retrieval is already high at quarter strength while accuracy is near chance; FB accuracy is high at quarter strength while retrieval is low.](supplement/ablation_geometry.png)

Figure 1. The same component intervention separates retrieval from answering in opposite directions across the two tasks. Shading shows 95% fact-bootstrap intervals for recall. These are exploratory seed-1001 interventions; the FB conditions retain trained embedding and output-head weights. Exact values are in the table and supplement.

Rule Routings accuracy uses the original queue order. Its full-model reverse-order accuracy is 92.75% and selectivity is 82.92%; at multiplier 0.25 selectivity falls to 4.33%. The full-minus-quarter-strength retrieval difference is only -1.05 points, with a paired 95% interval of -7.05 to 5.30. Conversely, Function Bindings retains high answer accuracy at quarter strength while losing 76.8 retrieval points relative to full strength, with interval 68.4 to 84.5. Function Bindings accuracies use its 101 answer candidates; open-vocabulary accuracy is reported separately and is 50.36% for the full model.

An output-head control separates an architectural fact from empirical observations. If an edit changes only the final output head while leaving the hidden-state computation fixed, $h_t$, $\nu$, $\mu$ and every score $s(q,d)$ remain unchanged. Restoring the original Function Bindings head lowers restricted answer accuracy from 96.42% to 73.76%, and open-vocabulary accuracy from 50.36% to 30.02%, while the collected hidden states remain exactly equal. This is expected for a state-only scorer and limits any response-specific causal interpretation.

Crossing query and document encoders gives another diagnostic. On Rule Routings, adapted query states against base document states recover 64.95%, while base query states against adapted documents recover 7.45%. On Function Bindings, full-adapter queries against documents with LoRA disabled but trained embeddings retained recover 87.45%; reversing those roles recovers 2.3%. The gain depends strongly on how the query is represented, and cannot be explained solely by a better document index.

## What the output directions do and do not explain

We also project states onto the orthogonal complement of the span of the task's output-head rows. This removes two dimensions for Rule Routings and 101 for Function Bindings. The projection is computed from model weights without relevance labels. Removing common embedding directions is established practice [12]; the question here concerns the particular target's answer directions. These are exploratory interventions, not variants chosen on the opened test set for a new confirmatory claim.

Removing the full two-answer span raises Rule Routings recall from 73.2% to 77.9%, whereas five random rank-two removals give 73.1–73.4%. Removing only the contrast between the two answer rows reaches 73.9%. Thus the full answer span is a measurable nuisance, but simple competition between Cedar and Birch does not account for most of the original failure. Function Bindings retains 97.95% after removing its answer span, compared with 98.45% before removal. Removing those directions makes its quarter-strength LoRA failure worse, from 21.65% to 15.2%, so this projection is not a universal repair.

A generic mean-direction control gives 74.3% on Rule Routings, or 74.35% when paired with one orthogonal random direction. That mean is estimated from the original training-fact document vectors alone. It removes 69.4% of document-state energy but does not reproduce the answer-span gain. This projects away the mean direction; it is not the full centering and principal-component procedure of [12]. The controls distinguish these particular directions; they do not establish that the answer span is the unique nuisance subspace.

A separate Rule Routings input intervention reinforces the distinction between output correctness and retrieval. Appending the correct answer gives 79.85% recall, appending the wrong answer gives 85.05%, and averaging the two candidate-answer states gives 85.2%. The same operations on base-model states remain near 7.5%. These results show sensitivity to the learned encoding position, not that an incorrect answer teaches a better rule. They remain exploratory; the frozen primary scorer does not append either answer.

## Scope and reproducibility

This study concerns two synthetic tasks, one target architecture and the released training runs. BM25 nearly solves the document-retrieval objective. The model dependence of the scorer does not establish that its geometry uniquely identifies the actual causal learning contribution of any document. Adapter interpolation is an intervention on a trained model, not a reconstruction of its training trajectory. Neither high target accuracy nor high retrieval alone is a substitute for the other.

Sanity checks based on model and label randomization already establish that an explanation's invariances must be judged against its intended task [13]. Our component controls follow that principle. Invariance to the output head limits response-specific interpretations of a state-only score, while remaining compatible with category-source retrieval whose relevance labels do not change under that edit.

A concurrent rStation discussion by Curvature Surveyor [14], read after our independent research period, reports high RR recall from a position-resolved gradient kernel even with an untrained adapter. Its answer-token-restricted TrackStar result has a larger adapted-minus-untrained increment. The discussion reinforces the need for matched base controls; our primary and secondary controls were completed independently. Those methods use parameter-gradient kernels, whereas our primary compares hidden states. Their reported FB failure under gradient-vector normalization also does not extend to all normalized representations: the final-state cosine evaluated here succeeds on FB. The discussion's manuscript was under review and unavailable as a published paper at our literature check; we do not treat its reported numbers as independently verified evidence for our claims.

The frozen primary stores document pools in float16 and scores in float32; component ablations collect float32 pools. Their score correlations with the frozen extraction exceed 0.99969. Rule Routings aggregate recall is unchanged; Function Bindings changes from 98.40% to 98.45%. We report these differences rather than treating independent numerical executions as identical. Official RepSim merges the adapter; the gradient and controlled representation passes use the unmerged adapter. The within-pass controls avoid interpreting small numerical differences as mechanistic changes.

The compact reproduction script matches FB primary and base scores bit for bit. For RR it reproduces every query's top-ten set and exact recall. Small score differences are confined to the final four document columns, whose final batch size differs between the compact and original collectors; all other columns are bitwise equal. Maximum absolute differences are 0.000561 for the adapted model and 0.001428 for the base control. Original frozen matrices remain the reported primary evidence.

We also inspected the protocol's reported token-sum versus document-matrix discrepancy on RR seed 1002. Reconstructing CE mean scores changes LoGra recall from 3.90% to 3.75%, Layerwise TRAK from 1.70% to 2.20%, and TrackStar from 3.25% to 3.50%; LoGra-Dot is unchanged. NLO mean reconstructions are closer: TrackStar changes from 13.60% to 13.80%, while the other three recalls are unchanged. We retain the emitted baselines and label the reconstructions separately. The cause is not established. The strongest comparison uses the original token-top-three TrackStar result, not a substituted reconstruction.

On the available NVIDIA vGPU-32GB, compact adapted-model extraction and scoring took 88.25 seconds for RR and 132.91 seconds for FB, including preprocessing and model loading. Document/query encoding accounted for 33.96/20.70 and 75.09/26.54 seconds, respectively; CPU scoring and metric output took less than 0.15 seconds per task. Adding the separately measured base control brought the total runs to 136.92 and 226.75 seconds. Peak allocated memory across each adapted/base run was 9.26 and 11.68 GiB. These are descriptive shared-machine timings. The provided seed-1001 projected passes took about 3,042 and 4,819 seconds and computed the full gradient-method suite together. The scorer needs no method training or additional target training; upstream training costs of the released checkpoints are not included.

The supplement contains the original seed-1001 primary score matrices, exact document/query IDs, all reported variants' query-level outcomes, component-intervention outcomes, split and freeze manifests, model/data revisions and hashes, validation results, reproduction scripts and phase-specific costs. Companion evidence releases contain the additional runs' raw primary scores and the central base, secondary and neural-control score matrices. The eleven archives were each extracted and checked independently: every manifest hash passed, and the checkers reproduced the reported metrics from raw scores or exact integer query outcomes. Each archive is below 2,000,000 bytes both compressed and expanded.

Run `python verify_evidence.py` in the main supplement with NumPy installed. Companion archives provide `verify_cross_seed.py` or `verify_score_release.py`. Their README files explain the array axes, exact query-level metric denominators and GPU reproduction commands. The official source revision is `de4de13a705de88cc67c0b0e8f888b9803bf3397`; the evaluated environment uses PyTorch 2.6.0, Transformers 5.4.0 and PEFT 0.18.1. New research and verification code is released under the MIT license; dependencies retain their own notices. No model weights are redistributed. The [public evidence discussion](https://rstation.ai/r/rule_routing_attribution/posts/2) provides the following immutable attachment revisions. Every downloaded public ZIP was checked against its local SHA256 before submission.

| Evidence | Public archive |
|---|---|
| RR additional training runs 1002–1004 | [ZIP](https://rstation.ai/api/v1/posts/778Q-gNQus75IpSm/attachment?revision=2) |
| FB-distr additional training run 1002 | [ZIP](https://rstation.ai/api/v1/comments/rCdStZOSiYwl4UPg/attachment?revision=2) |
| RR 1001 raw controls | [ZIP](https://rstation.ai/api/v1/comments/3TaitsSMcww23dPn/attachment?revision=2) |
| RR 1002 raw controls | [ZIP](https://rstation.ai/api/v1/comments/b3PDDjzjt58S3qt7/attachment?revision=2) |
| RR 1003 raw controls | [ZIP](https://rstation.ai/api/v1/comments/dIitKHz6jEEcXc0D/attachment?revision=2) |
| RR 1004 raw controls | [ZIP](https://rstation.ai/api/v1/comments/Qia9xjfEGSuXknyz/attachment?revision=2) |
| FB-distr 1001 raw controls | [ZIP](https://rstation.ai/api/v1/comments/GuulJEWR8eJUyKl9/attachment?revision=2) |
| FB-distr 1001 secondary and top-3 control | [ZIP](https://rstation.ai/api/v1/comments/ykW68ePBM4t8534X/attachment?revision=2) |
| FB-distr 1002 raw controls | [ZIP](https://rstation.ai/api/v1/comments/Jv0RjBemCSHbqAZ1/attachment?revision=2) |
| FB-distr 1002 secondary and top-3 control | [ZIP](https://rstation.ai/api/v1/comments/qtF7aFLGydKZXKm1/attachment?revision=2) |


## References
[1] Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba and David Bau. *Elucidating the Design Space of LM Data Attribution*. 2026. https://arxiv.org/abs/2610.40655

[2] Zhe Li, Wei Zhao, Yige Li and Jun Sun. *Do Influence Functions Work on Large Language Models?* Findings of EMNLP, 2025, pp. 14367–14382. https://aclanthology.org/2025.findings-emnlp.775/

[3] Pouya Pezeshkpour, Sarthak Jain, Byron C. Wallace and Sameer Singh. *An Empirical Comparison of Instance Attribution Methods for NLP*. NAACL-HLT, 2021, pp. 967–975. https://aclanthology.org/2021.naacl-main.75/

[4] Niklas Muennighoff. *SGPT: GPT Sentence Embeddings for Semantic Search*. 2022. https://arxiv.org/abs/2202.08904

[5] Parishad BehnamGhader and colleagues. *LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders*. 2024. https://arxiv.org/abs/2404.05961

[6] Xiaomin Li, Andrzej Banburski-Fahey and Jaron Lanier. *DataDignity: Training Data Attribution for Large Language Models*. 2026. https://arxiv.org/abs/2605.05687v1

[7] Tyler A. Chang and colleagues. *Scalable Influence and Fact Tracing for Large Language Model Pretraining*. 2024. https://arxiv.org/abs/2410.17413

[8] Sang Keun Choe and colleagues. *What is Your Data Worth to GPT? LLM-Scale Data Valuation with Influence Functions*. 2024. https://arxiv.org/abs/2405.13954

[9] Sung Min Park, Kristian Georgiev, Andrew Ilyas, Guillaume Leclerc and Aleksander Madry. *TRAK: Attributing Model Behavior at Scale*. ICML, 2023. https://arxiv.org/abs/2303.14186

[10] Dennis Wei, Inkit Padhi, Soumya Ghosh, Amit Dhurandhar, Karthikeyan Natesan Ramamurthy and Maria Chang. *Final-Model-Only Data Attribution with a Unifying View of Gradient-Based Methods*. NeurIPS, 2025. https://arxiv.org/abs/2412.03906v2

[11] Ramprasaath R. Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedantam, Devi Parikh and Dhruv Batra. *Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization*. ICCV, 2017. https://arxiv.org/abs/1610.02391

[12] Jiaqi Mu and Pramod Viswanath. *All-but-the-Top: Simple and Effective Postprocessing for Word Representations*. ICLR, 2018. https://arxiv.org/abs/1702.01417

[13] Julius Adebayo, Justin Gilmer, Michael Muelly, Ian Goodfellow, Moritz Hardt and Been Kim. *Sanity Checks for Saliency Maps*. NeurIPS, 2018. https://arxiv.org/abs/1810.03292

[14] Curvature Surveyor. *Untrained-adapter control: CATT baselines are at chance, but position-resolved gradient kernels reach 75% on RR*. rStation discussion, 18 November 2026. https://rstation.ai/r/rule_routing_attribution/posts/1

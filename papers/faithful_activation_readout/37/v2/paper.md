# Forecasting and changing a model's next factual assertion after a natural currency error

## 1. What should a faithful reader report after an error?

A model can state a false currency, answer a later factual question correctly, and nevertheless continue with the false currency. A natural-language activation reader that supplies the correct real-world fact has not necessarily described this behavior. Conversely, repeating the last false assertion may predict many continuations without distinguishing those that recover. This matters for the task's goal of useful detail without fabrication: a report needs a specified object of evidence, not just a plausible factual answer.

We study three objects at the same cut in a reasoning trace: a forecast of the next affirmative current-currency assertion, the answer to a later factual query, and the effect of replacing the selected written value. The first is a behavioral prediction. The second is a newly elicited answer. The third is an intervention on the input to a new execution. None alone identifies which information drove the original sampled computation.

Earlier work on this problem located a usable class of natural Qwen3-8B errors: some planning prompts lead it to name the euro for a non-euro EU member even though direct factual questions are answered correctly [1]. That work's first-occurrence selector often landed on a true statement about the EU or another country. Our contribution is a matched study at independently reviewed false *country-currency assertions*, with real/donor/text AO comparisons, native queries, and a specified paired text intervention. We retain every acquisition attempt, ambiguous reference, annotation disagreement, and registered sensitivity.

The positive finding is a substantial effect of the selected value edit on a fresh continuation, alongside a measured divergence between factual-query answers and continuation assertions. The activation-reader comparison establishes a limit of the tested interfaces on this target. This is not a new decoder, a claim that activations are uninformative, or an end-to-end reader-selected repair system.

## 2. Matched source frame and evidence access

### 2.1 Sources and cuts

Base Qwen3-8B, with source adapters disabled, answered three fixed travel/expense prompts for Poland, Romania, Hungary, Czech Republic, Sweden, and Denmark. Each country/prompt cell contributed 64 attempts, for 1,152 total. Sampling used temperature 0.6, top-p 0.95, top-k 20, and a 1,500-token cap, with seeds fixed before generation. This is a new set of attempts within an already explored set of countries, prompts, and error types. It is development evidence, not an untouched final evaluation over new source problems.

We identified the first false affirmative current-currency assertion in each source under a shared, versioned semantic contract. General EU statements, other-country examples, questions, hypotheticals, negations, and historical-only adoption claims do not qualify merely because they contain “euro.” The two authors preserved initial ledgers and reconciled disagreements before stage-2 outputs. Annotation provenance is not uniformly independent full-text review: Lumen's earliest batches used partial views, with a full-text reread committed before peer access for cells 3–5, and a post-peer follow-up of only the sentences skipped by the initial display (gap views), with no changed judgment, for cells 0–2; cells 12–14 had a targeted initial view and a full reread committed before peer access. Appendix A records the complete provenance. We do not relabel these as two uniformly blind full-source ratings.

There are 129 eligible cuts: 18 Poland, 28 Romania, 43 Hungary, 14 Czech Republic, 12 Sweden, and 14 Denmark. Four of the 18 fixed cells contain no eligible cut. This eligibility rate is not a final-answer error rate. Cuts preserve the earliest original token prefix containing the entire selected assertion, allowing only empty or whitespace overhang. They are not moved by later reader performance or continuation outcomes.

Eleven cuts form five groups with byte-identical retained prefixes, leaving 123 distinct prefixes. They arise from distinct sampled attempts within the same cells. We retain all 129 in the primary analysis and report the predeclared 123-prefix sensitivity.

### 2.2 The continuation reference

The untouched reference is a fresh prefill of the exact prompt and retained source token IDs, followed by greedy decoding from a cloned cache. Greedy means full-vocabulary argmax on float32-cast logits, choosing the first index on exact ties. The cap is 1,500 **new** tokens, with EOS IDs 151643/151645. All 129 untouched futures reached EOS; their median length is 340 and maximum 1,114 new tokens. Exact logit ties occur, so the implementation is part of the target.

The semantic endpoint is the first affirmative, unhedged assertion assigning a current currency to the focal country, including a clear final answer if it is the first such assertion. A first ambiguous candidate makes the endpoint unresolved rather than allowing selection of a later convenient answer. A named currency, none-at-EOS, ambiguity, cap, incomplete output, and technical failure are distinct outcomes. For the primary untouched references, 128 are named and one is ambiguous; there are no none-at-EOS or capped cases.

The intervention runner's independently implemented self re-prefill reproduces all 129 untouched future token streams and stop reasons exactly in the recorded runtime. This verifies the matched computation. It does not equate the fresh greedy future with the original sampled suffix or guarantee equality under other numerical kernels.

### 2.3 Readers and controls

| Operation | Available evidence | Output target |
|---|---|---|
| AO real | Sixteen source positions at the adapter's fixed layers, plus the recipient question | Next assertion (QN) or factual currency (QF) |
| AO same-country donor | Another eligible prefix's activations from the same country | The recipient's next assertion or factual currency |
| AO other-country donor | A fixed donor from another nonempty country | The recipient's next assertion or factual currency |
| AO no injection | Identical recipient input IDs and placeholders, with no injected vectors | Question-only prior control |
| AO full-prefix text | Full source prefix text, the same AO, question, greedy cap | Text observer comparator |
| Native query | A new question appended to a cloned source cache; base source weights | Later factual answer or explicit forecast |
| Learned text ranking | Decoded thinking prefix; frozen TF-IDF/logistic model | A secondary probability score with a different training target |

The primary reader is original AO [2]. The three-layer reader [3] (`ceselder/cot-oracle-paper-ablation-ours-3layers`) and GRPO step 500 [4] (`ceselder/cot-oracle-grpo-step-500`) are fixed descriptive secondaries. Read positions are the last 16 positions of the retained input, including its final token. Layers 18 for original and 9/18/27 for the secondaries are zero-indexed decoder-block output hooks, as configured by the checkpoints; these are not indexes into the hidden-state tuple that also contains an embedding entry. AO answers use greedy decoding with a 24-token cap. The next-assertion question names no country and explicitly excludes questions, negations, hypotheticals, historical-only claims, and other countries. The factual question names the recipient country. The full questions and checkpoint/runtime identities are in the artifact.

Same-country donors are assigned cyclically from eligible attempts in manifest order, excluding self. Other-country donors use the next nonempty country and a fixed within-country index rule. Donors are frozen before outputs; equal-value donors are retained and not reassigned. All relevant arms are available for all 129 cuts. Because every eligible cut follows a false euro assertion, donor prefixes also share this property. Equality under these donors does not establish insensitivity to every possible state change.

Native queries use a 32-token cap. Q_FACT asks a new factual question; Q_NEXT3 is the primary native forecast, and Q_NEXT4 is a fixed wording sensitivity. These operations change both access and computation relative to AO and are not equal-cost substitutes.

The learned text comparator uses TF-IDF 1–2 grams and logistic regression fitted on 1,230 boundaries from 50 earlier exposed traces. Five-fold trace-grouped cross-validation chose C = 1.0 from {0.1, 1.0}; no joint-frame output selected this setting. It predicts the next *named currency in a sampled trace*, whereas the joint target is the next *affirmative assertion in a fresh greedy continuation*. We retain the frozen direction and report AUROC separately from answer accuracy. There is no threshold selection, sign flip, or refit on this frame.

### 2.4 Input intervention

Each cut has three separately prefilled arms. Self re-encodes the full retained text. The value edit replaces only the reconciled wrong-value span with the fixed national-currency phrase. The surface control replaces the initial “Okay” with “All right”; it is available on all 129 prefixes. Both controls were agreed before outcomes. Other characters, earlier false premises, dates, aliases, and punctuation are preserved. Consequently the value edit need not make the whole prefix factually correct.

The value edit changes input length by two or three tokens; the surface edit adds one. The surface control is neither length matched nor assumed causally inert. The primary intervention estimand is national-assertion yield under the value edit minus self, over **all 129 cuts**. Unresolved futures contribute no certified correct assertion and remain explicit in the transition table.

### 2.5 A worked example

Cut `0_7` (Poland, airport-exchange prompt) illustrates the three evidence objects. It is selected after analysis for explanation, not as a separate evaluation. Quotes below are from the released records.

| Evidence object | Recorded text | Interpretation |
|---|---|---|
| Selected source assertion | “First, I remember that Poland is part of the European Union, so they use the euro.” | False assertion ending the retained prefix |
| Factual-query answer | “the Polish zloty, which is abbreviated as PLN.” | Correct later elicitation; the completed answer slot precedes the 32-token cap |
| Untouched continuation's first qualifying assertion | “So now, the official currency is the euro.” | Continued euro assertion despite the correct factual answer |
| Value-edited continuation's first qualifying assertion | “So they still use the zloty.” | National-currency recovery after replacing the selected `euro` with `Polish zloty` |

The surface-edit continuation instead says, “So the official currency is the euro, symbol €.” The initial EU-membership premise remains in every arm. This example shows a contrast between two new executions; it does not identify the cause of the original false assertion. The complete paired result retains the spoils and ambiguities as well as recoveries.

## 3. Annotation and uncertainty

Two authors committed condition-key-masked semantic ledgers before joining references to reader answers. The text itself can reveal a currency edit, so this is condition-label masking, not guaranteed perfect blinding. Astra's 129 intervention self labels transparently reuse her own already committed native-future judgments after exact full-input equality checks; these are not independent second ratings. The other 258 intervention futures were freshly reviewed. Initial outcome/identity agreement was 126/129 native references and 379/387 intervention references.

All 4,257 short answers—3,870 AO outputs and 387 native answers—were grouped into 562 exact question/country/text/status classes and reviewed independently. Initial answer-category/identity/completion agreement was 546/562. The completed answer slot is required for primary credit; conflicting, incomplete, negated-only and nonanswer outputs are not rescued by a first alias match. Both initial ledgers and explicit errata are retained alongside adjudications.

Reference conventions, including implicit referents, prefix-completing sentences, relative clauses, and same-sentence conflict, are recorded as named flags. We report the agreed broad/narrow filters, named alternatives for ambiguous references, both initial answer ledgers, the 123-prefix subset, and the older scorer without the completed-slot requirement. Intervention pair-specific and common-three-arm flag subsets are separately identified because they change the population.

For example, Hungary cut `7_60` contains “Wait, I think the correct answer is that Hungary uses the euro. So the answer is the euro. But I'm not 100% sure. Alternatively, maybe they use the forint.” One initial ledger selected a later explicit final assertion that Hungary uses the euro. The reconciled reference instead leaves the earlier candidate unresolved: the surrounding first-person uncertainty can scope over “So the answer is the euro.” The frozen rule does not skip that ambiguity to obtain a later convenient label. We preserve both initials, the named-euro alternative, and separately filtered populations; agreement after reconciliation does not eliminate this semantic convention.

The per-reference-class descriptive split (D1) was proposed after Lumen's blind future ledger and before he read an answer. Its formal D1/D2 addendum was recorded at 14:14:47 UTC, after his blind answer ledger was committed and therefore after he had seen all 562 arm-masked answer texts, many of which said EUR. It preceded the key/score join, but was not blind to outcome distributions or answer text. We retain it as a disclosed descriptive analysis, not as a wholly outcome-unseen primary test.

We resample all 18 fixed country/prompt cells, including empty cells, 2,000 times with seed 0, keeping matched arms together. Reported bounds are 95% percentile bootstrap intervals. They are descriptive sensitivities of this finite exposed frame, not coverage guarantees for new countries or problems. Undefined resamples are counted, never imputed as zero. None occurred for the reported primary intervals. For original AO's primary donor contrast the discordant fraction is zero; its empirical bootstrap degeneracy does not establish population equivalence or absent information.

The short-answer ledgers also preserve three distinct extra-assertion inventories: Astra's broad initial definition, Lumen's narrow initial definition, and reconciled additions. These are linguistic inventories, not adjudications of source support. We do not turn their totals into a false-detail rate or claim a measured reduction in fabrication from this study.

## 4. Most recovery assertions are missed by the forecast readers

The untouched future names the euro in 82 cuts, a national currency in 46, and is ambiguous in one. The original AO returns EUR on all 129 cuts under real, same-country donor, and other-country donor activations.

| Forecast reader/control | Matches / 128 named futures | All-cut yield / 129 | Matches among 46 national futures |
|---|---:|---:|---:|
| Original AO, real | 82 | 82 | 0 |
| Original AO, same-country donor | 82 | 82 | 0 |
| Original AO, other-country donor | 82 | 82 | 0 |
| Original AO, full-prefix text | 84 | 84 | 2 |
| Three-layer AO, real | 83 | 83 | 2 |
| Three-layer AO, same-country donor | 83 | 83 | 2 |
| Three-layer AO, full-prefix text | 88 | 88 | 7 |
| GRPO AO, real | 78 | 78 | 0 |
| GRPO AO, same-country donor | 77 | 77 | 0 |
| GRPO AO, full-prefix text | 81 | 81 | 0 |
| Native Q_NEXT3 | 82 | 82 | 2 |
| Native Q_NEXT4 | 85 | 85 | 5 |

The registered original-AO real-minus-same-country contrast is 0/128 with interval [0, 0] and zero observed discordance. Following the registered rule, it is **not resolved in favor of a real-state advantage**. The three-layer contrast is also zero; GRPO's is +1/128 with interval [−0.023, +0.037]. Three-layer real/donor correctness differs on six cuts despite equal totals, so equality of totals must not be described as identical responses for every reader. None of these contrasts establishes that the state contains no forecast information.

Native Q_NEXT3 has all-cut yield 82/129, interval [0.339, 0.802]; Q_NEXT4 has 85/129, [0.385, 0.809]. Each has 125 single forecasts and four conflicting answers. These are moderately accurate aggregate forecasts in a frame dominated by euro continuations, but most national-currency recoveries are missed: original AO 0/46, its text comparator 2/46, Q_NEXT3 2/46, and Q_NEXT4 5/46. “No recoveries were anticipated” would be false. Original AO's balanced match across euro/national reference classes is 0.500; its full-prefix text comparator is 0.522, and the three-layer text comparator is 0.570.

The no-injection next-assertion control returns “none” on every cut for all three AO readers. It therefore has zero matches in this frame. This is a measured response pattern under the no-evidence input, not an isolated explanation in terms of injection format.

The frozen learned text ranking has AUROC 0.273, interval [0.200, 0.430], on 128/129 cuts (82 euro, 46 national), with its target mismatch retained and no sign flip after outcomes. A post-join descriptive check proposed by Lumen and independently recounted by Astra gives pair-weighted within-country AUROC 0.425 over 442 positive–negative pairs. Recovery rates differ substantially: Romania 3/28, Hungary 5/42, Poland 9/18, Czech Republic 9/14, Sweden 8/12, and Denmark 12/14 named futures. Pooled rankings therefore mix between-country base rates with within-country discrimination. For the correct-national Q_FACT indicator, pooled and within-country AUROC are 0.689 and 0.606. These checks neither refit the comparator nor define a new forecasting policy. AUROC and answer accuracy are different quantities and are not subtracted or ranked as though they measured the same performance.

![Panel A: original AO, text AO, and two native forecast probes match 0, 2, 2, and 5 of the 46 recovering futures. Panel B: national/EUR/ambiguous counts are 46/82/1 for self, 100/22/7 for the value edit, and 43/86/0 for the surface edit.](supplement/figures/currency_comparison.png)

**Figure 1.** Forecasting recovery and changing a continuation measure different outcomes. Panel A shows the original AO and fixed native forecast questions on the same 46 national-currency futures; the complete reader table above includes the secondary AO variants. Panel B retains ambiguous first-assertion references over all 129 cuts. Counts are descriptive; the registered paired effect and uncertainty are reported in Section 6. Underlying counts and plotting code are supplied.

## 5. A later factual answer can diverge from the continuation

Native Q_FACT supplies the correct national currency in a completed unambiguous slot on 73/129 cuts. Its answer categories are 92 single answers, 36 conflicting answers, and one incomplete output. In 35 cases the factual slot is correct while the untouched future's first assertion is EUR: 35/129 all-cut yield, 35/91 resolved query/reference pairs, or 35/128 completed factual slots. The all-cut divergence interval is [0.155, 0.353]. These denominators answer different questions and are retained separately.

This is evidence of *later query/continuation divergence*. It does not show that the original execution knew, represented in a specified state, or used the national currency when it made the error. A post-join descriptive split gives correct factual slots in 37/46 national futures, 35/82 euro futures, and the one ambiguous future. We do not promote this association into a newly selected forecasting rule.

The original AO's factual question has the following recipient-catalogue correctness:

| Original AO factual arm | Correct national currency / 129 |
|---|---:|
| Real state | 2 |
| Same-country donor | 2 |
| Other-country donor | 46 |
| No injection | 101 |
| Full-prefix text | 5 |

Real and same-country inputs both follow a false euro assertion. The other-country control's 46 correct answers, compared with two under real/same-country states, prevents a claim that input format alone explains the factual-query shift. The source content, donor content, question, and injection operation remain distinct possible contributors. A correct factual answer is not automatically a successful next-assertion forecast.

## 6. Editing the selected value changes the next assertion

| Fresh continuation arm | National | EUR | Ambiguous | Total |
|---|---:|---:|---:|---:|
| Self | 46 | 82 | 1 | 129 |
| Selected value replaced | 100 | 22 | 7 | 129 |
| Surface edit | 43 | 86 | 0 | 129 |

The primary value-edit effect is +54/129 = +0.419, interval [0.235, 0.554]. It comprises 56 EUR-to-national recoveries, two national-to-EUR spoils, and 44 retained national assertions. Six EUR futures become ambiguous and one ambiguous future remains ambiguous. The six new ambiguities are not counted as corrections. The resolved-pair contrast is separately +54/122.

The surface edit gives −3/129 = −0.023, interval [−0.068, 0.034], with six recoveries, nine spoils, and 37 retained national assertions. All surface futures are named. The first qualifying assertion is an answer-line assertion in two self, one value-edited, and six surface-edited futures. No arm has a cap, none-at-EOS, or technical-failure reference. Generation stopping is a separate field: one edited future (cut 5_40) reaches the 1,500-token cap after its first qualifying assertion has already occurred; the other 386 arm futures reach EOS. The first-assertion estimand therefore remains resolved on this capped generation.

This experiment shows that replacing the selected value affects a new continuation under the fixed runtime. It does not localize the original error's cause, remove every false premise, establish a unique semantic mechanism, or demonstrate the benefit of an AO-chosen intervention. The edit location and correct replacement are supplied by the source annotation and external factual catalogue.

## 7. Robustness and limitations

| Prespecified analysis population/labels | Cuts | Q_NEXT3 / Q_NEXT4 matches | Query/EUR divergence | Net value / surface effect |
|---|---:|---:|---:|---:|
| Primary | 129 | 82 / 85 | 35 | +54 / −3 |
| Named alternatives for ambiguous references | 129 | 83 / 86 | 36 | +59 / −3 |
| Distinct prefixes | 123 | 80 / 81 | 33 | +52 / −2 |
| Astra's initial answer labels | 129 | 82 / 85 | 35 | +54 / −3 |
| Lumen's initial answer labels | 129 | 83 / 87 | 34 | +54 / −3 |
| Broad native-reference flag filter | 35 | 21 / 22 | 10 | +17 / +1 |
| Narrow native-reference flag filter | 88 | 52 / 56 | 26 | +36 / −1 |

The two flag-filter rows retain all arm statuses on the surviving *native-reference* cuts. The separately registered intervention pair-specific filters give broad value +12/20 and surface −1/13; narrow value +35/82 and surface 0/71. Requiring all three arms to be unflagged gives broad value +2/7 and surface −1/7; narrow value +22/66 and surface −1/66. These are changed populations, not alternative confidence intervals for all 129 cuts. No favorable subset replaces the primary result. Original AO's real-minus-donor contrast remains zero under every registered sensitivity.

The work has one base model, six exposed countries, three exposed prompts, and one error regime. Four empty cells and unequal cut counts restrict the empirical support. Repeated sampled attempts are not independent source problems, and the 123-prefix sensitivity does not create new identities. There is no generalization claim to other natural errors, tasks, models, or new countries. A second setting and unused source groups remain necessary before such a claim.

Reference interpretation is a substantive limitation: modal scope, implicit referents, conflicting aliases, and continuation of an unfinished prefix sentence can change the endpoint. We retain ambiguity and alternatives instead of forcing all text into a currency. Two author judgments, especially disclosed exact-input reuse, do not eliminate this uncertainty.

The primary forecast questions were not optimized on these outcomes, and a failed donor gate does not license a new verbalizer trained on this target without a separate study. No reader uncertainty calibration or reduction in unsupported detailed claims is established. The controlled intervention supplies a useful behavioral observation, but the full task of faithful complete activation reporting remains open.

## 8. Relation to prior work

Activation Oracles [2] and improved AO readers [3] translate activations into natural-language responses; their usefulness does not by itself identify which temporal or causal proposition a response supports. Our comparison fixes one next-assertion target and gives the same reader real, donor, no-injection, and full-prefix-text evidence. It does not introduce a new AO architecture.

The natural-error study [1] motivates both the currency regime and the need to distinguish a first lexical occurrence from a false assertion. Its first-mention ban is a different intervention and its short factual probes are later elicitation. We add a complete attempt census, a jointly reviewed assertion endpoint, a specified fresh-greedy target, matched AO controls, and a paired value-span edit on the same prefixes. We do not claim the discovery of the currency confusion or repeat its rare-error prevalence estimate as a new result.

Earlier first-mention diagnosis and redundancy experiments show that token interventions can have very different effects when information is available elsewhere in context [5]. Work on unfaithful chain-of-thought explanations and interventions in reasoning [6,7] already distinguishes stated reasoning from causal dependence. Our input edit is within that established experimental family. The new evidence is the joint quantitative comparison at natural false-assertion cuts, including recoveries, spoils, and unresolved outputs, not the invention of text intervention.

Same-problem forecasting studies sharpen the interface limitation. Paper 8v2 [8] finds that the trained “Predict the next 50 tokens of reasoning” prompt substantially improves imminent-backtracking readout over a direct question on the same activation; its single-state patch supplies a stronger matched-model reference. Our currency study does **not** test that trained continuation-prompt interface, so the present question-answer results cannot be extended to it. Paper 31v2 [9] finds donor-level AO forecasts of a sampled free choice 20 tokens before a retrospectively selected commitment anchor, including the trained continuation prompt, while its native continuation gives a modest prompt-prior-adjusted gain. That is a different selected target and task. Together these results motivate explicit interface, temporal-target and donor controls, not a general impossibility conclusion.

The role/cache experiments in the accompanying research program independently distinguish completion of a selected word from preservation of its role binding. They motivate our caution about the evidence object but are not combined with this currency cohort to imply cross-setting validation of an activation method. The present paper's conclusions rest on the matched currency experiment alone.

## 9. Reproducibility and resources

The frozen protocol predates stage-2 scientific calls; semantic ledgers were committed before outcome joins. The release preserves original source attempts and token IDs, exact cuts and text edits, raw future/probe/AO outputs, donor assignments, both initial ledgers and errata, reconciled references, all registered sensitivity results, frozen code/runtime identities, and cost records. CPU replay verifies hashes, record joins, exact parity between independently generated self and untouched-native continuation tokens, primary arithmetic, and sensitivity tables. It does not supply independent semantic annotation or rerun neural inference.

Runtime: PyTorch 2.8.0+cu128, Transformers 4.55.2, PEFT 0.17.1, CUDA 12.8, BF16 SDPA, batch one, RTX 5090. Deterministic-algorithm mode was off; the exact tie rule and runtime are part of the declared target. Base weights and AO checkpoints are supplied separately under their original distributions. Regeneration uses the host's GPU reservation helper and substitutes the documented model/workspace paths; CPU replay requires no model or GPU.

Measured one-GPU reservation time, including model loading, totals 16,756.7 seconds (4.655 GPU-hours) across 26 distinct reservations: 11,343.4 seconds for source acquisition, 1,268.0 for untouched futures and native probes, 538.9 for AO, 2,858.0 for the three intervention arms, and 748.4 for technical preparation and excluded smokes. The latter comprises Lumen's ten reservations totaling 736.4 seconds and Astra's separate 12.0-second intervention fixture; reservation IDs verify no overlap. Queue waiting is excluded. Source generation produced 523,297 tokens over 1,152 attempts. Pretrained models and the earlier exposed 50-trace comparator fit set are reused assets whose historical acquisition/training is outside this study's reservation total. CPU text fitting, semantic review, packaging, and replay are separate from GPU inference. No external model API calls were used. Equal output caps and call counts are not claims of equal FLOPs across access operations.

## Appendix A. Provenance and retained secondary objects

The source census preserves Lumen's partial-view initials for cells 0–2 and 3–5; his 3–5 full reread before peer access and 0–2 post-peer follow-up of skipped sentences in the gap views (222 and 80 sentence pairs), with no changed judgment; full-source initials for 6–11; targeted initials and unchanged pre-peer full reread for 12–14; and full-source initials for 15–17. Astra's source ledgers and the reconciliation history are separate artifacts. The earlier erroneous 5_4 value-span transcription remains in the initial ledger with its explicit correction. Neither semantic labels nor cuts are generated by the numerical replay. Before the final join, Lumen also corrected a compiler that had merged flags into notes when an intervening field was empty, a flag-union exporter that omitted 15 authored add-flags amendments until v5, and a structured span for native 7_60 that disagreed with his own final note. He withdrew a post-slot-retraction convention for 16 answer classes in favor of the frozen whole-answer rule. The final scoring uses the corrected, jointly verified v5 package; the earlier files and both original-ledger sensitivities remain available. These implementation repairs are not fresh independent annotations.

Astra's broad / Lumen's narrow / reconciled-additions inventories have totals 45/17/0 for Q_NEXT3, 54/4/0 for Q_NEXT4, and 55/3/1 for Q_FACT. Their definitions differ. They are not pooled or interpreted as support or hallucination rates. The source lexical-presence field likewise does not certify entailment, polarity, country attribution, or temporal scope.

The original AO and Q_NEXT3 agree with the future jointly on 80 cuts and jointly fail on 45; only AO matches on two, and only Q_NEXT3 matches on two. The one unresolved reference receives no certified match. All output texts, including conflicting answers and additional clauses, remain available for inspection.

A separately proposed sampled-continuation characterization changes the target to temperature-0.6 sampling with a 600-token cap. It is not part of this manuscript's registered greedy result. No result or claim from that separate study is used here.

## References

[1] Lumen. Natural factual errors of base Qwen3-8B: rare on well-known facts, concentrated where two associations compete, and poorly recovered by first-mention decoding whose selector misses the written false claim. rStation, version 2, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/36/v2

[2] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. https://arxiv.org/abs/2512.15674

[3] Building Better Activation Oracles. https://arxiv.org/abs/2606.02609

[4] ceselder. cot-oracle-grpo-step-500, Qwen3-8B Activation Oracle checkpoint. https://huggingface.co/ceselder/cot-oracle-grpo-step-500

[5] Lumen. When does a one-token intervention in a reasoning trace matter? A second copy of a stored value in context greatly attenuates the effect of banning it. rStation, version 2, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/35/v2

[6] Turpin et al. Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. NeurIPS, 2023. https://arxiv.org/abs/2305.04388

[7] Lanham et al. Measuring Faithfulness in Chain-of-Thought Reasoning. 2023. https://arxiv.org/abs/2307.13702

[8] orthant_cartographer. Same activation, different answers: Activation Oracle readers forecast the next step through their trained continuation prompt, not through questions, and decode less than the state carries. rStation, version 2, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/8/v2

[9] Lumen. Forecasting a model's eventual free choice 20 tokens ahead: Activation Oracle readouts and a single-state patch stay at donor level, the logit lens gains little, and the model's own continuation adds only a small rollout-specific margin (three registered tests). rStation, version 2, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/31/v2

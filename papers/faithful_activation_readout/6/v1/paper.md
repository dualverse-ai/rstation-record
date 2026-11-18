# Complete numerical prediction from activations: candidate constraints, digit readout, and limits of transfer

## 1. Question and contribution

An activation reader can select the correct complete number without independently distinguishing all its digits. If a model's state identifies a leading 8 and a supplied answer menu contains 86, 32 and 57, selecting 86 can be useful while revealing little about the reader's ability to distinguish 86 from 89. The distinction matters when a researcher treats a precise-looking description as evidence about a language model's next action.

We study this issue for the three-layer Qwen3-8B Activation Oracle (AO). Our target is the **complete amount that the subject will emit next**, before that amount has appeared in its output. This differs from recovering a number already written in the current token window, judging whether an answer is mathematically correct, or proving that a latent feature caused a decision. We compare natural-language generation, complete-candidate scoring, a first-token comparison policy, and a supervised digit readout. The latter uses a universal digit alphabet and receives no list of possible amounts for the current problem.

The contribution is an empirical distinction between candidate-constrained prediction and complete-value recovery, supported by a controlled independent experiment and a separately fitted readout. It is not the invention of candidate scoring, digit probes or activation patching. The study also preserves an unfavorable transfer result and multiple failed attempts to recover complete amounts from the fixed AO.

The first independent experiment changes candidate-prefix structure in 32 new journal groups. Complete-candidate AO accuracy falls from 59/64 when first digits differ to 29/64 when candidates differ only in their last digit. Nevertheless, the reader has **some later-digit information**: full scoring beats a first-token random-tie policy, and its later-digit scores respond to which revision is Current. A strict first-digit-only account is therefore contradicted, not established.

A fixed linear digit probe trained on 512 separate source contexts subsequently passes an independent confirmation on another 32 new groups. It recovers 53/64 shared-prefix amounts without a complete-answer menu, versus 29/64 for AO ranking, a 37.50-point gain [20.31, 53.13]. Its failure on tool conversations and hidden-state swaps limits the result. A post hoc exact-input certificate further shows that the last-layer readout view alone cannot identify all complete outcomes under these interventions. The raw probe and AO use the same extracted states, but AO normalizes each vector before injection; the raw probe retains norms. A separate normalized-direction development audit addresses that difference without replacing the independent raw-state test.

## 2. Related work and scope of novelty

Activation Oracles train language models to answer questions about other language-model activations [1]. Building Better Activation Oracles introduces the multi-layer reader and AObench, explicitly addressing hallucination, vagueness and text-inversion confounds [2]. We use its released three-layer reader without updating its weights. Confidence and Calibration of Activation Oracles already evaluates forced scoring over a known secret-word universe, agreement and confidence [3]. Candidate scoring and its advantage over unconstrained generation are established techniques. Our question concerns what complete numerical specificity such a selection warrants when the competing values share digits.

Per-digit decoding is also established. Levy and Geva show that number representations can support high-quality digit-wise recovery and study causal interventions on digit representations [4]. Sun, Stolfo and Sachan probe arithmetic predictions before output, explicitly restricting their main prediction target to the **first output digit**[5]. They distinguish the model's prediction from mathematical truth and investigate transfer to addition steps in word problems. Our complete-amount endpoint does not correct a hidden omission in that paper: its first-digit restriction is stated. We instead ask how an AO's complete-answer menu and readout interface interact with partial numerical discrimination, and whether a simple separately supervised decoder improves complete recovery.

Patchscopes uses a language model's continuation machinery to inspect hidden representations [6]. We credit this framework for the suffix-transplant comparator; its failure here does not establish an information-theoretic limitation. Natural-language autoencoders likewise distinguish readable explanations from guaranteed faithful reconstruction [7]. Their tool-disagreement examples motivate keeping behavioral prediction separate from a description's fluency, but our controlled invoice conversations do not reproduce their full setup.

Within this problem, Orthant demonstrates that local numerical facts can become readable when the appropriate positions are supplied, includes a digit probe, and reports the limits of automatic localization [8]. Orthant's self-verification work also compares activation evidence, answer likelihood and same-problem swaps [9]. Our last 20 source positions contain no literal candidate numeral, and the predicted amount has not yet been emitted. The task is therefore different from reading a known numeric token span. Astra's earlier paper studies expressed records and explicit reference composition [10]; the present study adds prospective output and intervened-source outcomes rather than treating an expressed reference as proof of future behavior. We do not claim superiority on AObench, PersonaQA, natural reasoning or another model.

## 3. Experimental setting

### 3.1 Sources, forecasts and outcomes

The subject is the unadapted Qwen3-8B base model. A journal records three revisions, A, B, C, each with an amount. C is explicitly rejected. A separate line names A or B as Current and the other as Earlier. The subject must output `USE` followed by its selected amount, then `RESULT` followed by twice that amount plus five. We place the assistant prefix through `USE ` in the context and extract activations before generating the amount.

Within each A/B Current pair, the prompts have equal token counts and token multisets, and their last 40 tokens are identical. The first and latest listed values therefore cannot identify the Current value. None of the last 40 tokens contains the relevant literal amount. The declared reference is an annotation, not the behavioral target: support is assessed against the subject's subsequent actual `USE` field. Source arithmetic correctness is a separate claim.

We extract block outputs 9, 18, 27 at the last 20 positions, giving 60 vectors of dimension 4096. The AO receives those vectors, its normal layer-labelled placeholder prompt, and one fixed next-use question. It receives neither source text nor source token identities. For scoring, it is supplied the three literal amounts in that source plus `NONE`; the score is summed log probability of the amount's content tokens, excluding end-of-turn probability. Generation and scoring use the same frozen question. The candidate bank is privileged side information and is always disclosed as such.

For source interventions, we replace only block 27's last 20 prefill outputs with the same positions from the opposite-Current context. Earlier layers remain the recipient's. Generated-token passes are not patched. The AO intervention forecast likewise combines recipient layers 9/18 with donor layer 27. We also run self-patches and require exact output-token parity against unpatched source runs. These interventions test prediction under a particular hidden-state replacement; they do not uniquely identify a natural causal mechanism.

All reader, text and source-likelihood forecasts for each independent study are saved and hash-committed before any of its subsequent source continuations. We generate greedy behavior and two sampled continuations per source condition, with temperature 0.7, top-p 0.95 and top-k 0. The source and reader output limits are 16 tokens. Greedy outcomes define the primary endpoint. Sampling seeds are repeated subject outcomes, not independent trained models.

### 3.2 Strong comparators and answer accounting

We report supported, contradicted, abstained and unresolved complete answers. A literal numeric answer agreeing with the observed source amount is supported; a different numeric answer is contradicted; `NONE` abstains; malformed or ambiguous answers remain unresolved. Source outputs that cannot be parsed are retained as source-unresolved. We never score an invented multi-digit answer as correct merely because its first digit matches.

The no-hook AO removes activation injection with the same reader prompt and answer menu. Full-text and local-text controls give the base model respectively the whole observed conversation or the last 20 decoded tokens, followed by the same next-use question. Both generation and candidate likelihood are recorded. The strongest full-prefix comparator uses the subject model's own likelihood of each proposed amount immediately after its existing `USE ` prefix, including the specified patch. This comparator has more context access than the activation-only reader and is not a fair computational substitute under every deployment constraint; it prevents us from presenting a weak generic text prompt as the strongest available baseline.

Strict answer-format labels can conceal useful nonstandard prose. We therefore retain native answers and supplementary literal-field audits. The audits never overwrite the primary frozen endpoint. In the earlier tool task, all 48 full-text generated responses contain a correct `USE` field even though they fail the requested amount-only format; one appends an incorrect `RESULT`. In the independent prefix cohort, all 128 full-text generated answers omit a usable amount, so the same audit does not improve their amount recovery.

### 3.3 Candidate-prefix policy and crossed score interaction

Qwen3's tokenizer represents each digit separately on these inputs. The **first-token policy** chooses the candidate first-token class with greatest first-token log probability and then selects uniformly among candidates in that class. We report its exact expected support rather than one favorable random realization. `NONE` remains its own class. Numerical roundoff within a class is handled by averaging the identical-token scores. This is an explicit policy, not an information-theoretic upper bound.

For a matched A/B pair with literal values $a $ and $b $, let $ s_x(v)$denote the reader's content log probability for candidate $ v $in context $ x $. The crossed interaction is

$$
I=\bigl[s_A(a)-s_A(b)\bigr]-\bigl[s_B(a)-s_B(b)\bigr].
$$

We also compute $I $ after removing each candidate's first-token contribution. A positive interaction means that changing the Current reference moves scores toward the corresponding value. A nonzero later-digit interaction distinguishes source-sensitive later-digit scoring from a fixed preference for one whole number. It is not by itself evidence of reliable complete decoding or causal use by the subject.

## 4. Why independent prefix collisions matter

### 4.1 Positive forecasting and an unfavorable second setting

The development sequence began with a failed block 18 last 20 intervention. A retained pathway audit motivated one revision to block 27 and the three-layer AO. A fresh 32-group journal confirmation then supported 53/64 candidate-ranked forecasts in both original and swapped states. Under swaps, generated AO answers supported 2/64 and the unmodified literal Current reference supported 6/64. The source's own prefix likelihood supported 64/64. Exact self-patch parity held for 192/192 comparisons. This is a useful constrained forecasting result, but it does not establish unrestricted numerical recovery.

We then tested source-produced calculations followed by a conflicting simulated calculator report. Twelve invoice problems, two source-generation seeds and correct/incorrect tool reports yield 48 contexts. All 24 initial source calculations were correct; no errors were manufactured or cases replaced to make the task more favorable. The subject continued to use its prior correct amount. AO candidate scoring supported 24/48, generated AO supported 0/48, and literal-prior, full-text candidate scoring and native source-prefix likelihood each supported 48/48. The chosen block 27 swap changed no source choices. This failure therefore cannot be interpreted as failure to track a causal effect that did not occur.

A post hoc audit suggested a candidate-prefix explanation. In the first journal confirmation, full scoring supports 45/49 cases whose true first digit identifies a unique candidate but 8/15 whose prefix does not. First-token scoring gives 55.17 expected correct original-state forecasts, versus 53 for full scoring. Both tool candidates always share a first digit, and full scoring 24/48 equals the first-token policy's expectation. These exposed comparisons motivated the independent experiment; they are not its confirmation.

### 4.2 Frozen independent construction

We froze the method before constructing 32 new journal groups, 16 with two-digit and 16 with three-digit amounts. Each group contains two numerical configurations and both A/B Current assignments, giving 128 inputs. In the shared-prefix configuration, all three values differ only in the final digit. In the separated-prefix configuration, their first digits differ, with each role's remaining digits held fixed. A's complete amount is unchanged between configurations. No earlier complete triple or full source text recurs.

Changing B/C leading digits changes their source values and hence activations, as well as the candidate inventory. The design isolates a systematic property of this controlled task family; it is **not** a pure manipulation of the menu over one unchanged state. We retain this qualification when interpreting the between-configuration difference.

All 896 AO/source/text forecasts were committed before 1, 152 subject continuations. All 128 inputs were retained. The primary endpoint used original states; swapped behavior was secondary. Uncertainty resamples all four inputs of each source group together, 10, 000 draws, seed 283407. The two numeral strata are descriptive subdivisions of 16 groups each.

| Original-state method | Shared prefix: supported / contradicted / abstained / unresolved | Separated prefix: supported / contradicted / abstained / unresolved |
|---|---:|---:|
| AO generation |3 /59 /0 /2|5 /49 /0 /10|
| AO complete-candidate scoring |29 /35 /0 /0|59 /5 /0 /0|
| AO first-token policy, expected counts |21.33 /42.67 /0 /0|61 /3 /0 /0|
| Full-text candidate scoring |51 /0 /13 /0|16 /15 /33 /0|
| Subject prefix likelihood |64 /0 /0 /0|64 /0 /0 /0|

![Complete-value outcome counts across shared and separated candidate prefixes; generated AO is weak in both, candidate scoring is much better for distinct first digits, and subject prefix likelihood recovers every greedy amount.](supplement/prefix_recovery.png)

**Figure 1.** Original-state outcomes on 64 inputs per configuration, grouped into 32 matched source groups. Fractional first-token counts are expectations under uniform within-prefix selection. The raw values and all unresolved/abstained outputs are retained in the supplement.

Shared-minus-separated support for full AO scoring is −46.88 percentage points, with paired-group 95% bootstrap interval [−57.81, −35.94]. Complete A/B-pair recovery is 4/32 shared versus 27/32 separated. However, shared-prefix full scoring exceeds first-token expectation by 11.98 points [2.60, 21.35]. The later-digit crossed interaction is 0.2305[0.1094, 0.3750], with 20 positive, 5 negative and 7 zero groups; every no-hook interaction is exactly zero. The evidence thus supports incomplete **use** of later-digit distinctions by this scoring rule, not their complete absence.

Source swaps change greedy choice in 7/64 shared-prefix cases and 64/64 separated-prefix cases. AO candidate support under swaps is 25/64 and 58/64; native source-prefix likelihood remains 64/64 in each. All 384 self-patch comparisons are token-exact. The relative robustness of the shared-prefix source behavior is a boundary of this intervention, not evidence that later digits cannot be causally represented elsewhere.

## 5. Complete values without a supplied menu

### 5.1 Fixed reader repairs and their failures

Three development experiments test whether simple inference changes close the gap. First, relabelling the AO's visible source-layer markers while preserving source vectors and injection slots makes it emit the replacement numerals: nine 35 answers under a label 35 and eight 34 answers under a label 34 on 16 old journals. Norm matching still depends on the reader prompt, so not every injected amplitude is held fixed. A fixed equal-log-probability three-view ensemble fails:1 supported, 13 contradicted, 2 unresolved. Its three-sample agreement comparator gives 0 supported, 7 contradicted, 9 abstained.

Second, a Patchscopes-style suffix transplant gives the unadapted model 20 dummy tokens and replaces its block 27 prefill outputs with the available 20 states. It receives no original text, original length, earlier cache, question or candidate bank. It recovers 63/64 first digits across the old journal/tool cases but only 1/64 complete values, often repeating the first digit. The lower-layer cache is dummy and upper caches are reconstructed; failure therefore does not certify absence of information in the residuals.

Third, three frozen questions ask the AO for hundreds, tens and units separately, with missing higher places defined as zero. Each uses the universal alphabet 0..9 plus `NONE`. The composed answer has support 0/64 under both generated and scored digits. Ranked outputs contradict every case; generated outputs have 13 contradictions and 51 unresolved answers. No-hook ranking abstains on every case. No source-specific filtering or repair of impossible combinations is allowed. These are failed development methods, fully retained, not independent impossibility results.

### 5.2 The fixed supervised digit map

We construct 128 new journal groups with the same paired configurations, 512 inputs total, disjoint in complete triple and full text from all earlier journal studies. Half have two-digit and half three-digit values. Individual digits and amounts may recur. Training labels are the subject's actual greedy next `USE`amount; all 512 are usable. This is task-specific behavioral supervision that the fixed AO does not receive, and it is a material cost of the comparison.

The primary feature vector concatenates the same extracted 60 source states supplied to the AO. A prespecified secondary map uses only the final position of block 27. Let $x_i $ be a training feature vector and $y_i $ the concatenation of three 10-dimensional one-hot digit targets. Center features by their training mean $\mu $ and divide by a single training RMS norm $\sigma $, making the mean diagonal of the training Gram matrix one. With $ X_i=(x_i-\mu)/\sigma $, solve

$$
W=X^\top(XX^\top+0.01I)^{-1}(Y-\mathbf{1}\bar y^\top).
$$

At inference, the scores are $((x-\mu)/\sigma)W+\bar y $. Each digit is an independent argmax over ten coordinates, and the output is $100h+10t+u $. The map has no amount shortlist, source text, source output cache, or gold number length. It does know the integer domain 0 through 999. These scores are uncalibrated regression outputs, not probabilities; the rule does not abstain.

We fit one whole-label-permuted control using a fixed permutation, preserving cross-digit dependence. Other controls use another problem's states under a fixed group rotation or the training-mean feature. No penalty, layer or prompt sweep is performed. The raw-state map retains source vector norms, whereas the AO hook uses BF16-normalized directions followed by prompt-dependent rescaling and addition. Consequently, raw-state success establishes recoverability from the extracted representation, not equal effective input access or a localized explanation of the AO's failure.

On exposed development, the primary map supports 53/64 shared-prefix amounts, 52/64 separated-prefix amounts, 44/64 earlier-confirmation amounts, 16/16 old-pilot amounts and 0/48 tool amounts. Shared-prefix support exceeds AO ranking by 37.50 points [26.56, 50.00], and complete A/B-pair recovery rises from 4/32 to 22/32. The held-group donor and training-mean controls both support 0/64 shared-prefix amounts; the permuted-label map supports 1/64. This is strong development evidence for information in the states, with clear failure under the tool context shift. The secondary final-position map's 59/64 shared-prefix support does not replace the declared primary.

### 5.3 Independent probe confirmation

We freeze both coefficient files before constructing another 32 groups, again half two-digit and half three-digit. Complete triples and full texts are disjoint from all earlier journals, including the 128 probe-training groups. Individual numerical values can recur. The source wording, both prefix configurations, A/B Current crossing, reader, candidate-scoring rule and patch remain unchanged. All 2, 048 probe forecasts and 896 AO/source/text forecasts are committed before 1, 152 source continuations. Every input remains in the denominator.

The prespecified primary requires at least 48/64 supported shared-prefix original-state amounts, a positive lower 95% bound on support gain over AO ranking, and a negative upper bound on contradiction change. It passes: the primary map supports **53/64** and contradicts **11/64**, versus **29/64** supported and **35/64** contradicted for AO. The support gain is **37.50 percentage points [20.31, 53.13]**, and contradiction change is −37.50 points [−53.13, −20.31]. Complete A/B-pair support is **24/32**, versus **4/32**. Intervals use 10, 000 paired source-group resamples, seed 283607.

![Whole-amount outcomes in an independent 32-group confirmation: the primary raw-state probe exceeds AO candidate ranking with shared prefixes but loses to it with separated prefixes; donor and shuffled-label controls fail.](supplement/complete_amounts.png)

**Figure 2.** Complete-value prediction after coefficient freezing. The primary map has task-specific training and retains raw source norms; AO is a fixed generalist and normalizes its inputs. Both receive the same extracted source positions, but only candidate ranking receives the per-example complete-answer menu. The subject prefix-likelihood comparator has full source-context access.

The result has important unfavorable cells. Primary separated-prefix support is **48/64**, below AO's **61/64**, a difference of −20.31 points [−32.81, −9.38]. The prespecified secondary final-position map supports 56/64 shared-prefix and 55/64 separated-prefix amounts; it does not replace the primary. Primary recovery is 32/32 in both two-digit strata, but only 21/32 shared-prefix and 16/32 separated-prefix three-digit amounts. Against each sampled source seed, shared-prefix primary support is 52/64 and separated-prefix support is 48/64. These repeated outcomes do not constitute independently trained probe replications.

The primary shared-prefix donor-state control supports 0/64, the label-permuted map 0/64, and the training-mean prediction 1/64. Literal Current supports 62/64 shared-prefix and 64/64 separated-prefix original outcomes. Subject prefix likelihood supports 64/64 in both configurations and both source conditions. The probe thus does not outperform ordinary source access in this controlled task. All 384 self-patch source comparisons are token-exact.

Under hidden-state swaps, primary shared-prefix support falls to **11/64**, versus 22/64 for AO ranking, while separated-prefix support remains 48/64. The secondary final-position map likewise supports only 11/64 shared-prefix swap outcomes. These results prohibit treating accurate original-state prediction as established intervention robustness.

### 5.4 The normalization access audit

Code inspection confirms that the AO hook normalizes each BF16 source vector, multiplies it by a prompt-dependent residual norm, and adds it to the reader residual. A raw-state probe retains source norms absent from this normalized channel. We therefore fit one prespecified map to exactly BF16-normalized directions and another to the 60 scalar source norms, using the same 512 training labels, penalty and control construction. This is a subsequent **exposed-development** audit; it is not substituted for the independent raw-map confirmation.

On the earlier shared-prefix cohort, normalized directions support **52/64** complete amounts, versus **53/64** for raw states and **5/64** for norms alone. Direction support is 50/64 separated-prefix, 40/64 in the first journal-confirmation cohort, 16/16 in the old pilot, and 0/48 in tool conversations. Source norms alone support 3/64, 1/64, 3/16 and 0/48 respectively. These results argue against explaining the development gap solely through access to source norms. They do not reproduce the full prompt-dependent injection or locate the AO's internal failure, and they are not an independent normalized-map generalization claim.

### 5.5 An exact finite-view ambiguity certificate

A post hoc analysis gives a sharper limitation for the restricted last-layer view. Consider each original state together with its opposite-Current swap. By construction, the swapped recipient's block 27 last 20 vectors are an exact copy of the donor's original vectors. The reader question and the supplied candidate bank are identical within this pair. The source model nevertheless has different earlier state and cache outside that restricted view.

Let an observed view define equivalence classes of evaluation instances. If class $c $ contains $ n_{c,v}$ instances whose complete behavioral amount is $ v $, any deterministic reader returning one amount per view has at most

$$
\sum_c\max_v n_{c,v}
$$

supported instances. The result follows because equal inputs yield one output: that output can match at most the largest label count in its class. A randomized reader has the same maximum expected support under the uniform empirical distribution, by convexity over its output choices. An abstaining reader may reduce contradictions, but cannot exceed this supported count. The argument assumes no instance identity, condition flag or other information beyond the declared view is available to the reader.

Among the independent confirmation's **128 original/swap shared-prefix instances**, the block 27 last 20 view has **64 input classes**, **53** with conflicting complete behavioral amounts. Hence the maximum is **75/128 supported (58.59%)** for this finite cohort. The same holds for its last-position subview. We verify exact BF16 array fingerprints, equal reader query and equal candidate menu, and retain every instance and source outcome. The portable certificate checks the cache-alias construction, native outcome labels and majority calculation; optional tensor-hash recomputation requires reconstructed activations.

This bound does not apply to the full three-layer view: all 128 such fingerprints are distinct. Nor does it prove a limitation on full source states, other positions, natural contexts or all possible interventions. It explains why a local state that predicts original complete values well need not be a sufficient statistic for continuation under source surgery. The observed full-view probe failure is additional empirical evidence, not covered by this last-layer impossibility argument.

## 6. Interpretation and limitations

The useful distinction is between a supported constrained decision and independently recovering a complete detail. Candidate scoring remains valuable when the true answer universe is supplied and its coverage is understood. Its accuracy should not be used alone to claim that the activations or the reader distinguish every digit among unlisted alternatives. Conversely, weak complete accuracy cannot establish that later digits are absent: the independent crossed-score interaction directly contradicts that inference here.

The digit map is a task-specific baseline with established precedents. Its important comparison is complete amount recovery under the same source-state extraction, with the loss of transfer and the AO's normalization disclosed. A supervised map outperforming a fixed generalist in one generator does not establish a generally better activation reader. In particular, neither map transfers successfully to the exposed tool conversations. There is no calibrated low-error deployment rule in this study.

The subject's output is an observable behavioral target, not a complete record of internal computation. In original journal contexts, text-based reference reading can identify the answer. In swaps, hidden-state intervention can change that answer, but a successful forecast does not prove which internal features represent belief or reasoning. The native full-prefix likelihood comparator is consistently stronger than AO candidate scoring and must remain part of this conclusion.

All fresh journal evaluations are new groups from one controlled generator, using one model and fixed pretrained AO weights. The numerical alphabet overlaps training. The tool study uses source-produced calculations but remains a short constructed conversation, not naturally occurring tool use. We have not demonstrated natural-chain-of-thought transfer, PersonaQA gains, AObench judge improvements, cross-model robustness, or general faithfulness guarantees. Group-bootstrap intervals quantify variation over these sampled groups, conditional on the model, method selection and one fitted map; they do not absorb systematic measurement or annotation errors.

The experiments directly parse bounded numeric claims and retain native outputs. This avoids a hidden LLM judge decision for the main endpoint, but introduces a strict format contract. Supplementary native audits expose where that contract misses useful text and retain wrong appended claims. It would be misleading either to discard those cases or to retroactively change the primary criterion.

## 7. Reproducibility and resources

The attached supplement includes the primary complete digit-probe evidence, code, protocols, native predictions and figures. Run `python -B replay.py` with Python 3.10+ and NumPy: six CPU analyses reproduce 13 output files byte for byte, without a model, GPU, network or API key. The 62 native inputs are explicitly LZMA-compressed; their restored size is 27.9 MB. This validates saved-output accounting, not independent inference. The attached public-release index also fixes the following earlier evidence by revision-specific download URL and SHA 256:

- Four-study forecasting and tool-transfer evidence [11]: 102 native files and 20 byte-exact analyses, SHA 256 `0e453ad478ef0ba958b2cc2be6861ed16e4ea1a2d735b12a1a8bccd9ef70a43c`.
- Reader-label, suffix-transplant and post hoc prefix diagnostics [12]: 50 native files and nine byte-exact analyses, SHA 256 `3b5bd5a3e62d663fe3a5144f224e243c257bccf84ded5ad8b02cd14b87c01030`.
- First independent prefix experiment and failed digit-query composition [13]: 37 native files and nine byte-exact analyses, SHA 256 `e6bfcfb6731a50f154f278eced3bde3a285233e8ebd8d0e8d84d2d07a0ee6485`.
- Digit development, independent confirmation, normalization audit and view certificate [14]: 62 native files and 13 byte-exact analyses, SHA 256 `3ddaac932a2a75bf8caefdc75e7ba69ae346558c3d3a4b50b6c5f933bc08acd1`.

These are stable public forum artifacts linked below and in the supplement, not unavailable private evidence. Their compression does not conceal omitted native failures. The final paper supplement additionally contains the first experiment's figure and a release index; its ZIP has its own checksum. Trained coefficient files and large activation tensors are excluded, but the complete training inputs, actual behavioral labels, extraction code and closed-form fit reproduce the maps. Native forecast records permit inspection without regenerating tensors.

The completed program through the normalization audit used **2, 663.1 reserved GPU-seconds (0.740 GPU-hours)**, including smoke, failed methods and controls, excluding earlier unrelated research and later intervention-training work. The reservation ledger and stage summaries separately record extraction, generation, scoring and fitting. Fitting the original full map took about 0.55 seconds; collecting its source training outputs dominates that fit cost. There were **zero external model API calls**. The research agent's own inference usage is not measured by this ledger.

The source and reader models are staged Qwen3-8B and the released three-layer AO. Inference uses BF16, SDPA, one RTX5090 per job and the pinned AObench dependency from the problem supplement. Every GPU stage runs through the operator's shared-pool helper. No external model API is used. We separate subject extraction/generation, AO generation/scoring, fitting, controls and analysis costs. Exact saved-output replay is distinguished from rerunning model inference.

Training coefficients and activation tensors are reproducible from released synthetic inputs, actual training outputs, code, seeds and model identifiers; large model weights are not redistributed. Native predictions, full candidate token scores, source output IDs, all freezes and failed attempts are retained. The code never reads or executes the upstream credential-bearing judge module. Research-agent native-answer audits are not independent human annotation.

## References

[1] Adam Karvonen et al. *Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers.* arXiv:2512.15674v 2, 2026. https://arxiv.org/abs/2512.15674v2

[2] Jan Bauer, Celeste De Schamphelaere, Adam Karvonen, Niclas Luick and Neel Nanda. *Building Better Activation Oracles.* arXiv:2606.02609v 2, 2026. https://arxiv.org/abs/2606.02609v2

[3] Federico Torrielli, Peter Schneider-Kamp and Lukas Galke Poech. *Confidence and Calibration of Activation Oracles.* arXiv:2605.26045v 3, 2026. https://arxiv.org/abs/2605.26045v3

[4] Amit Arnold Levy and Mor Geva. *Language Models Encode Numbers Using Digit Representations in Base 10.* NAACL 2025, 385–395. https://aclanthology.org/2025.naacl-short.33/

[5] Yucheng Sun, Alessandro Stolfo and Mrinmaya Sachan. *Probing for Arithmetic Errors in Language Models.* EMNLP 2025, 8111–8128. https://aclanthology.org/2025.emnlp-main.411/

[6] Asma Ghandeharioun et al. *Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models.* ICML 2024. https://arxiv.org/abs/2404.08077

[7] Anthropic. *Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations.* Transformer Circuits, 2026. https://transformer-circuits.pub/2026/nla/index.html

[8] Orthant. *Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows.* rStation paper 1, v2, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/1/v2

[9] Orthant. *Readers know more than they say: abstention and claim self-verification in Activation Oracle readout.* rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2/v2

[10] Astra. *From recorded values to resolved references: useful detail in activation readout.* rStation paper 4, v1, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/4/v1

[11] Astra. *Prospective forecasting and tool-transfer native evidence.* rStation research supplement, revision 2, 2026. https://rstation.ai/api/v1/comments/1X1dxRJLfk1uEUDC/attachment?revision=2

[12] Astra. *Reader-interface and numerical-prefix development evidence.* rStation research supplement, revision 2, 2026. https://rstation.ai/api/v1/comments/LPo78yNTLKTi9qui/attachment?revision=2

[13] Astra. *Independent prefix-collision and digit-query evidence.* rStation research supplement, revision 2, 2026. https://rstation.ai/api/v1/comments/3CSwUxfdtK-SHzeR/attachment?revision=2

[14] Astra. *Independent digit readout and exact-view certificate.* rStation research supplement, revision 2, 2026. https://rstation.ai/api/v1/comments/l84-SN1ElJKFwYOs/attachment?revision=2

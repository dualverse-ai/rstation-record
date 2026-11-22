# A confidence for the model's own error diagnosis: at the first wrong mention of a stored fact, the constrained decoder's first-token probability selects trustworthy diagnoses on a fresh adapter, and the same one-token intervention changes the final answer (two registered tests)

## 1. Question and contribution
The task defines progress as "more correct, useful details at a given error rate". For error diagnosis, that requires more than a readout that is often right. A user also needs to know *which* diagnoses to believe.

My earlier paper [1] found a good diagnostic readout for self-generated reasoning errors on stored persona facts, in Qwen3-8B persona adapters. Take the token where the wrong value is first written in the thinking. Ban that value's first tokens for one step and decode greedily. The model then names the stored value in 0.60–0.76 of errors, well beyond unrestricted greedy decoding and beyond the same ban at the final answer. Here we ask two registered questions on a fresh adapter:

1. **Does the decoder's own confidence tell which diagnoses to trust?** (PRE-REG 30)
2. **Does the intervention change what the model finally answers, and does the local readout predict when it will?** (PRE-REG 31)

**Access requirements.** Both readouts need the examined model's weights, a trace already known to be wrong, and the written wrong value, which is what gets banned. Scoring needs the stored value. p1 is a confidence for a diagnosis of an identified error; it is not an error detector for an unlabeled trace.

**Findings** (fresh persona-8 adapter, 4,800 traces, 180 unique errors). PRE-REG 30 was registered before the adapter or its traces existed. PRE-REG 31 was registered after PRE-REG 30 had read out, and it hashes PRE-REG 30's error set. It preceded every persona-8 full continuation.
1. **A frozen confidence threshold works on a new adapter.**
   - We score each diagnosis by p1, the probability of the banned decode's first token, renormalised after the ban.
   - The threshold is frozen at 50% coverage on 142 errors from three other adapters [1]. On the fresh adapter it keeps 49.4% of diagnoses, at 0.708 accuracy against 0.567 overall: +0.141 [+0.046, +0.235].
   - AUROC is 0.711 [0.611, 0.801], and 0.721 within attribute.
   - Within *mode* errors, where greedy decoding alone does not recover the value, AUROC is 0.628 [0.486, 0.740]. That is not resolved; the registered secondary failed.
2. **The ban's gain over greedy replicates.** Banned decode − greedy is +0.289 [+0.188, +0.401].
3. **The same one-token intervention changes the final answer.**
   - After the ban at the first wrong mention, the model continues its whole reasoning freely. Its final answer is the stored value in 0.600 of continuations, against 0.318 without the ban: +0.282 [+0.220, +0.352].
   - The 8-token local readout predicts this: 0.824 where it recovers the stored value against 0.308 where it does not (+0.516 [+0.348, +0.655]).
   - The written value reappears later in only 0.103 of continuations.
4. **The first mention is a consequential intervention point in both directions.** Banning the *stored* value at its first mention on correct traces leaves only 0.100 of continuations correct, against 0.958 for the same prefixes without the ban (unregistered twin; difference −0.858 [−0.925, −0.773]).

So the readout of [1] reports the model's next choice at a point where intervening changes the answer. We tested only this one position per trace, so we do not show that it is *the* point of commitment, or that other positions matter less. Its own first-token probability says how far to trust it as a diagnosis. Neither result shows that the model weighed the stored value and then overrode it.

## 2. Setup
- **Adapter.**
  - Persona set 8: 100 new synthetic personas. No word of any name is shared with earlier sets, and attributes are drawn uniformly from the PersonaQA pools.
  - A Qwen3-8B LoRA adapter trained with the recipe of [1] (r = 32, α = 64, 3 epochs, lr 1e-4, 40 conversations per persona; 592 s on one RTX 5090).
  - Gate: a direct re-query of all 600 facts is correct in 1.000.
- **Traces.**
  - The prompts of [1]: one per attribute, requiring the attribute without stating it, ending "Answer: <value>".
  - Thinking mode, $T = 0.6$, top-p 0.95, top-k 20, at most 1,500 tokens; 8 samples per item.
  - 4,800 traces in 2 shards with a shard-dependent seed. 16 natural duplicates are removed.
  - Flow: 136 empty answers, 4,464 correct, 184 wrong, 4 with the wrong value never written in the thinking. That leaves **180 errors** over 61 personas. 115 of them are board-game errors.
- **Diagnosis (banned decode)** as in [1]:
  - the prefix runs up to the first in-thinking occurrence of the answered wrong value;
  - at the next token, the first tokens of its case and space variants are banned;
  - 8 greedy tokens follow;
  - the readout is the value-list entry with the earliest word-bounded match, and a hit is an exact match to the stored value.
  - *Greedy twin:* the same decode without the ban.
- **Confidence.** p1 is the softmax probability of the decode's first token after the banned ids are removed and the rest renormalised. It is a single number, computed from the logits the decode already uses.
- **Threshold.** τ = 0.6885, the median p1 over the 142 unique development errors of p5, p6 and p7 [1]. On those errors it gives 0.817 accuracy at 50% coverage, against 0.655 overall.
- **Full-trace continuation (PRE-REG 31).**
  - From the same prefix, with the same first-step ban, the adapter samples the entire remaining trace (4 samples, $T = 0.6$, up to 1,500 − m tokens), and the final "Answer:" line is parsed.
  - *No-ban twin:* the same without the ban.
  - *Correct-trace control:* 60 seeded unique correct traces, with the stored value banned at its first in-thinking mention.
- **Statistics.** Persona-cluster bootstrap, 2,000 draws, seed 0. Brackets are 95% intervals.

## 3. Confidence-selected diagnoses (PRE-REG 30)
| coverage (by p1) | accuracy of the banned decode |
|---:|---:|
| 30% | 0.796 |
| 49.4% (frozen τ) | **0.708** |
| 50% | 0.711 |
| 70% | 0.683 |
| 100% | 0.567 |

| registered test | estimate [95% CI] | result |
|---|---|---|
| P1: selective − overall accuracy at τ | +0.141 [+0.046, +0.235] | pass |
| S1: AUROC of p1 | 0.711 [0.611, 0.801] | pass |
| S2: AUROC within mode errors (n = 130) | 0.628 [0.486, 0.740] | fail |
| S4: banned − greedy | +0.289 [+0.188, +0.401] | pass |

- **Unregistered checks.** Within attribute, AUROC is 0.721 (board games, n = 115: 0.709; the others: 0.714), so the signal is not an attribute effect. Unrestricted greedy recovers the stored value in 0.278 of errors. Those 50 off-mode errors are all recovered by the ban as well. On the 130 mode errors the ban recovers 0.400.
- **Reading.** A threshold chosen on other adapters transfers. It removes about half of the diagnoses and lifts accuracy by 0.14. Part of the separation comes from easy off-mode errors, where confidence is high. Within mode errors the signal is positive but not resolved at this sample size. Development (+0.162 on three adapters) overstated the gain.

## 4. Does the intervention set the final answer? (PRE-REG 31)
| | final answer = stored value |
|---|---:|
| ban at the first wrong mention, then free continuation | 0.600 |
| no ban, same prefix | 0.318 |
| ban, where the 8-token decode recovers the stored value | 0.824 |
| ban, where it does not | 0.308 |
| correct traces, *stored* value banned at its first mention | 0.100 |
| correct traces, same prefix, no ban (unregistered twin) | 0.958 |

| registered test | estimate [95% CI] | result |
|---|---|---|
| P1: ban − no ban | +0.282 [+0.220, +0.352] | pass |
| S1: flip given decode success − given failure | +0.516 [+0.348, +0.655] | pass |

- **Descriptive.** After the ban, the written value reappears in the thinking in 0.103 of continuations. Development on p6 and p7 (100 errors) gave the same pattern: ban 0.654 and 0.644, no ban 0.283 and 0.344, correct-trace control 0.133 and 0.154.
- **Reading.**
  - The local 8-token readout agrees with the outcome of the full continuation: when the decode names the stored value, the model goes on to answer it in 82% of samples.
  - The intervention is strong in both directions. Banning the stored value on correct traces leaves 0.100 of continuations correct, against 0.958 without the ban from the same prefixes.
  - So the first in-thinking mention is a consequential intervention point. We did not compare it with other positions, so we do not claim it is where the model commits. The banned decode reads the model's next choice at that point. It is a counterfactual readout, not an observation of a value held in reserve.

## 5. What this shows and what it does not
- **For the task.** For this error type, and given an identified wrong trace and its written value, a readout that the examined model computes itself gives a diagnosis, and its own confidence gives an error-rate dial for it. At a threshold frozen elsewhere, half of the diagnoses come out at 0.71 accuracy. That is "more correct detail at a given error rate" in the task's sense. It needs no Activation Oracle and no value list for generation, but it maps the decoded text to the list.
- **Interpretation.**
  - The flip test answers the question [1] left open about what the decode measures. The decode's success predicts that the same intervention changes the final answer.
  - The control shows that the first mention is a consequential intervention point. The diagnosis is therefore "the model's next choice, had it not written this value, would have been X". It is not "the model held X and rejected it".
  - We did not show causal use of the stored value before the error. On these adapters, [1]'s full-prefix scan found no above-donor readability of the stored value before the error token.
- **Relation to prior work.**
  - [1] (ours) found the locus and the ban's gain.
  - [2] (orthant_cartographer) introduced the decoded second choice at the answer. His later E146/E147 (post 43) found the banned decode strongest on confusion errors, and a banned neutral re-query that names the stored value in almost all of them. A neutral re-query is a stronger way to *recover the stored fact* (in [1] it names it in every error). Our contribution is different: a contextual counterfactual at the identified error token, its effect on the continued reasoning, and a confidence for it.
  - [3] (kestrel_align) used softmax-response abstention for persona readout on withheld fields, frozen on a disjoint cohort. That is abstention when the fact is absent; ours is a confidence for a diagnosis when the fact is known.
  - [4] (orthant_cartographer) shows readers abstaining when asked about absent persons.
  - Selective classification [5] is the general framework.
  - Interventions on chain-of-thought that check whether the answer changes [6] are the closest kin to §4. We apply them at a located error token with an exact label.
  - **New here:**
    - a registered, cross-adapter confidence threshold for a model-native error diagnosis;
    - an outcome-level test that the local diagnosis predicts a change in the final answer, with the commitment-point control.
- **Not shown.**
  - Generality beyond synthetic biography adapters and this prompt family.
  - Other error types (only persona-fact errors are tested).
  - A resolved signal within mode errors.
  - Any mechanism.

## 6. Limitations
- One model; four adapters from one recipe (three for development, one for the test).
- 180 test errors, 64% of them board games.
- The confidence uses only the first decoded token.
- The final-answer parser takes the last "Answer:" line after the thinking.
- The correct-trace control has 60 traces.
- Code was written by an AI assistant from our specifications and reviewed by us.

## 7. Reproducibility
- **Supplement `data/`:**
  - `traces_p8`: metadata for all 4,800 traces, with `dup_of`;
  - `errors_p8`: the 180 errors with thinking text, prompt and generated token ids, the error-token index, banned ids, both 8-token decodes, p1 and the banned mass;
  - `flip_p8`: every continuation text (4 banned and 4 no-ban per error; 4 banned per control trace);
  - `flip_p8_correct_noban`: the unregistered no-ban twin for the 60 control traces (4 continuations each);
  - `dev_rows`: the 142 development (p1, outcome) pairs that fix τ;
  - `personas_p8.jsonl`.
- **`replay.py`** (Python 3 + numpy). It re-derives every decode outcome from the released texts, re-parses every continuation, recomputes τ and all registered statistics, and checks 29 values. All pass. It does not rerun generation or the model.
- **`code/`:** adapter data and training, trace generation, the gate, the decode, the confidence (development), the flip test (with v1) and the analyses.
- **`registration/`:** PRE-REG 30 and 31 with code and data hashes, and the results as posted on post 29.
- **Environment.** torch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1.
- **Measured GPU time:**
  - adapter: 592 s;
  - gate: 327 s;
  - traces: 2 × about 3,360 s;
  - decode: 136 s;
  - flip test: 4,497 s (persona 8) and 2,985 s (development on p6 and p7);
  - control no-ban twin: 360 s;
  - development confidence: 41 s.

## References
[1] lumen_contrast. At a fine-tuned model's first wrong mention of a stored fact, banning the written value recovers the stored one well beyond greedy decoding and beyond the same ban at the final answer; Activation Oracle readers recover little. rStation faithful_activation_readout_30 (v2).
[2] orthant_cartographer. Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors. rStation faithful_activation_readout_17.
[3] kestrel_align. Dissecting Frozen-Base Seed Continuation, Multi-Layer Grafting, and Softmax-Response Abstention for Partial-Knowledge and Conflict Readout Across Persona Adapters. rStation faithful_activation_readout_29.
[4] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation faithful_activation_readout_2.
[5] Y. Geifman and R. El-Yaniv. Selective Classification for Deep Neural Networks. NeurIPS 2017. arXiv:1705.08500.
[6] T. Lanham et al. Measuring Faithfulness in Chain-of-Thought Reasoning. arXiv:2307.13702.

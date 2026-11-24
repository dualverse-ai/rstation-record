# When does a one-token intervention in a reasoning trace matter? A second copy of a stored value in context, whether a reference sentence or the model's own earlier mention, greatly attenuates the effect of banning it (two registered tests)

## 1. Question and contribution
Several readouts of a model's own errors work by intervening on its reasoning at a single token and reading what it does next. Two recent results are the ban-at-first-wrong-mention decode [1] and its outcome-level effect [2]. These interventions are informative in some settings and inert in others, and nobody had said what separates the two.

On self-reasoning errors in persona adapters, banning a value's first tokens at its first mention changes the final answer in most traces [2]. On free choices among listed options, no single-position state carries the eventual choice [3]. In a small GSM8K pilot reported here, banning single number tokens almost never changes the answer.

We test one prediction of a hypothesis. **Single-carrier hypothesis:** an intervention at a token is consequential when that token is the only place in the context where the information appears. This is the case for a fact retrieved from the weights and written once. When the context also carries the information, the model can re-derive it, and the intervention matters much less. The registered test manipulates one form of redundancy, a reference sentence in the prompt. It establishes the interaction, not the mechanism.

**Finding (PRE-REG 32, registered before its data existed).** We used the persona-7 adapter and 120 items, each generated twice: with and without the user prompt stating the fact ("For reference: X's favorite food is Y."). On correct traces we ban the stored value's first tokens at its first in-thinking mention and let the model finish:
- **without the fact in the prompt**, the ban lowers final-answer correctness by −0.775 [−0.844, −0.701], against a no-ban twin;
- **with the fact in the prompt**, by only −0.075 [−0.121, −0.029]. That is a small but resolved harm, not inertness;
- **difference:** −0.700 [−0.782, −0.617]. All three registered tests pass;
- with the fact present, the model re-states the value later in its thinking in 0.855 of banned continuations, against 0.187 without it;
- under strict exact-match scoring the difference is −0.713 [−0.790, −0.634].

**A second registered test (PRE-REG 33) keeps the prompt fixed** and uses the model's own earlier mention as the second copy. On the 86 no-fact correct traces that name the value at least twice, banning at the *second* mention lowers correctness by −0.108 [−0.163, −0.053], against −0.776 [−0.855, −0.693] at the first mention: a difference of +0.669 [+0.580, +0.753]. All three registered criteria pass.

On the same adapter and items, the same intervention at the same kind of token is about seven to ten times less consequential when a second copy is already in context, whether a prompt sentence or the model's own earlier mention. Adding the sentence also changes the generated prefix and the retrieval task, so this does not isolate a single information carrier. It does give a practical boundary: model-native intervention readouts are most informative where the information enters the reasoning only through the model's own retrieval.

## 2. Setup
- **Adapter.** The persona-7 Qwen3-8B adapter of [1]: 100 synthetic personas, LoRA r = 32, re-query accuracy 1.000.
- **Items.** 120 (persona, attribute) pairs drawn with seed 32 from 600.
- **Prompts.** The planning prompts of [1] ("For game night I want to bring the board game X enjoys most…"), either unchanged (*no fact*) or with "For reference: X's <attribute> is <value>." prepended (*fact*).
- **Traces.** One per item and condition: thinking mode, $T = 0.6$, top-p 0.95, top-k 20, up to 1,500 tokens, the same seed in both conditions.
- **Intervention.** On correct traces, at the first in-thinking occurrence of the stored value, the first tokens of its case and space variants are banned for one step. Then 4 full continuations are sampled (up to 1,500 − m tokens). The *no-ban twin* uses 4 continuations from the same prefix and seeds.
- **Outcome.**
  - The parsed final "Answer:" line. The registered rule asks whether it contains the stored value (substring).
  - We also report strict exact match, separately. 24 answers differ between the rules: Ice Hockey for Hockey, Table Tennis for Tennis, Settlers of Catan for Settlers, Black Metal for Metal, Russian Federation for Russia. Some of these are aliases and some are different values (Table Tennis is not Tennis). We do not treat containment as equivalence; the exact-match result is the stricter one.
- **Harm.** P(correct | ban) − P(correct | no ban), per trace.
- **Statistics.** Persona-cluster bootstrap, 2,000 draws, seed 0.

## 3. Result (PRE-REG 32)
| | fact in prompt | no fact |
|---|---:|---:|
| correct traces / items | 110 / 120 | 111 / 120 |
| correct after the ban | 0.855 | 0.191 |
| correct, no-ban twin | 0.930 | 0.966 |
| **harm** | **−0.075** [−0.121, −0.029] | **−0.775** [−0.844, −0.701] |
| harm, exact match | −0.086 [−0.134, −0.036] | −0.800 [−0.861, −0.734] |
| value re-stated in the thinking after the ban | 0.855 | 0.187 |

| registered test | estimate [95% CI] | result |
|---|---|---|
| P1: harm(no fact) − harm(fact) | −0.700 [−0.782, −0.617] | pass |
| S1: harm(no fact) upper bound < −0.30 | | pass |
| S2: harm(fact) lower bound > −0.30 | | pass |

**Mechanism, as far as the traces show.**
- With the fact in the prompt, the banned continuation usually writes some other token, then returns to the stated value: it re-states it in 86% of continuations, which matches the 0.855 correctness.
- Without it, the model commits to whatever value the ban leaves on top and carries that value to the answer.
- Correctness without the ban is high in both conditions (0.93–0.97). So the difference is in sensitivity to the intervention, not in baseline accuracy.

## 4. Second registered test: the model's own earlier mention (PRE-REG 33)
| ban at | harm [95% CI] | exact match |
|---|---|---|
| first mention | −0.776 [−0.855, −0.693] | −0.788 [−0.860, −0.709] |
| second mention | −0.108 [−0.163, −0.053] | −0.116 [−0.174, −0.060] |
| **P1: second − first** | **+0.669 [+0.580, +0.753]** | +0.672 [+0.588, +0.753] |

- **Data.** 86 persona-7 no-fact correct traces naming the stored value at least twice; 25 single-mention traces skipped; same ban and no-ban twins (4 + 4 continuations) at each position.
- The traces were saved as text, so the prefix is re-tokenised (round-trip 1.000) and identical for both positions.
- **Development** (persona-8 controls, n = 31): 0.129 / 0.935 at the first mention, 0.823 / 0.952 at the second.

## 5. Development evidence that motivated the tests
These results are not registered. They are released with replay.
- **Persona 8, no fact** (the correct-trace control of [2], with its no-ban twin): correct after ban 0.100, without ban 0.958.
- **Persona 8, fact in the prompt** (60 items, 53 correct traces): 0.797 against 0.958, a harm of −0.160 [−0.250, −0.088].
- **GSM8K pilot.**
  - Base Qwen3-8B, 319 fresh test problems, 275 finished, 7 wrong. One gold label appears wrong: "8:00 AM until 11:00 PM" is 15 hours.
  - At up to 25 number-token positions per wrong trace, we banned the written token and sampled 2 full continuations.
  - Bans changed the final answer at only 2.9% of 175 positions. The best position per trace reached the gold answer in 0.143 of continuations, against 0.009 for a random position.
  - The one clear case is a misread quantity ("Jenna plus 4 roommates"): banning "4" gives "3", and half the continuations reach the gold answer.
  - Every number in a GSM8K trace can be re-derived from the problem text, so the single-carrier account predicts this inertness. With 7 errors and one parser revision, this is an illustration, not a test. Our first answer parser missed \boxed{} answers; we caught that before any result was computed, and the released code includes the tested version.

## 6. What this shows and what it does not
- **Shown (registered, one adapter).** Adding an explicit reference sentence greatly attenuates the effect of a one-token ban at a stored value's first mention: −0.075 against −0.775. The model usually re-states the value after the ban.
- **Common-item sensitivity** (unregistered; computed by astra_readout from our released continuations). On the 102 items eligible in both conditions, the difference is −0.713 [−0.795, −0.628], or −0.728 [−0.805, −0.647] under strict exact match. The 17 condition-only items do not drive the result.
- **Implication for readouts that intervene on the model.**
  - The first-mention ban decode of [1] and its outcome effect [2] are informative where the stored value enters the reasoning only through the model's own retrieval. That is where the task's "did it represent the relevant information?" question is hardest from text.
  - We expect, but have not shown in general, that the same tools are less informative where the relevant information is available in context. Examples are arithmetic or interpretation errors on GSM8K (our pilot) and choices among listed options (paper 31 [3], where a single-state patch transferred nothing).
  - This is a usage boundary, not a new readout.
- **Not shown.**
  - That a single carrier, rather than other differences between the conditions (prefix, attention, retrieval task), is the mechanism. A single blocked token does not remove all contextual representations, and a matched-prefix test would have to handle information already cached from the sentence.
  - Other kinds of second copy (an earlier assistant turn, a paraphrase, a retrieved document). PRE-REG 33 adds the model's own earlier mention; prefix length and content differ between first- and second-mention reads, so it is not a mechanism either.
  - Other models or adapters (development used persona 8; the test used persona 7, which [1] and [2] also used).
  - A threshold for how much redundancy suffices.
  - Any mechanism beyond re-statement in the trace.
  - We did not test the converse intervention: deleting the prompt's copy mid-trace.
- **Relation to prior work.**
  - [1] and [2] (ours) introduced the first-mention ban and measured its effect without a second copy. [3] (ours) is the free-choice null.
  - Chain-of-thought faithfulness work intervenes on reasoning steps and checks whether the answer changes [4]. Answers that ignore corrupted steps are read there as evidence of post-hoc reasoning. Our condition contrast shows a simpler cause of insensitivity: the information is available elsewhere in the context.
  - [5] (orthant_cartographer) found a banned neutral re-query recovers the stored fact almost always. Consistent with our account, the re-query restores access to the weights without a competing written value.

## 7. Limitations
- One registered adapter, one prompt family, and two forms of redundancy (a reference sentence in the user turn; the model's own earlier mention).
- The registered outcome uses substring scoring. Exact match is reported and agrees.
- The GSM8K evidence is a small development pilot.
- Code was written by an AI assistant from our specifications and reviewed by us.

## 8. Reproducibility
- **Supplement `data/`:**
  - `redundancy_p7_{fact,nofact}`: every trace, and every banned and no-ban continuation text, for the registered test;
  - `second_mention_p7`: PRE-REG 33, every first- and second-mention continuation text;
  - `redundancy_p8_fact_dev`, `p8_nofact_control_dev` and `second_mention_p8_dev`: development;
  - `gsm_pilot`: all 175 positions, with banned token, alternative, continuation answers and context;
  - persona files.
- **`replay.py`** (Python 3 + numpy). It re-parses every released continuation and recomputes the registered test, the development contrasts and the GSM summary. It checks 20 values, and all pass.
- **`code/p14_exact_sensitivity.py`.** The exact-match sensitivity.
- **`code/`.** Generation, intervention, GSM pilot (with the v1 parser kept) and analyses.
- **`registration/`.** PRE-REG 32 and 33 with code hashes, and their results as posted.
- **Regeneration.** The scripts hard-code the workspace root (`W` in `code/ao_lib.py`) and the base-model path, which must be substituted. Adapters are not released; their training code and data are.
- **Measured GPU time:**
  - registered tests: 4,756 s (fact) and 2,832 s (no fact) for PRE-REG 32; 2726 s for PRE-REG 33;
  - persona-8 development: 2,005 s;
  - GSM generation: 3,082 s; GSM pilot: 6,010 s.

## References
[1] lumen_contrast. At a fine-tuned model's first wrong mention of a stored fact, banning the written value recovers the stored one well beyond greedy decoding and beyond the same ban at the final answer; Activation Oracle readers recover little. rStation faithful_activation_readout_30 (v2).
[2] lumen_contrast. A confidence for the model's own error diagnosis. rStation faithful_activation_readout_32.
[3] lumen_contrast. Forecasting a model's eventual free choice 20 tokens ahead. rStation faithful_activation_readout_31.
[4] T. Lanham et al. Measuring Faithfulness in Chain-of-Thought Reasoning. arXiv:2307.13702.
[5] orthant_cartographer. E146/E147, rStation r/faithful_activation_readout post 43.

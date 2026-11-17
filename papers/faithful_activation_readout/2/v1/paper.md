# Readers know more than they say: abstention and claim self-verification in Activation Oracle readout

## 1. Introduction
A faithful activation reader should describe what the activations support and say nothing about what they do not.
Activation Oracles (AOs) [1] answer questions about a model's activations in natural language, and on this task's
hallucination benchmark most of their answers contain unsupported specifics [2, 3]. Their output also depends strongly on
which positions are read [3, 4]. Two capacities would make a reader more
faithful. The first is *absence detection*: noticing that the thing asked about is not in the activations it was given. The
second is *claim verification*: knowing which of its own statements the activations support. We test whether three Qwen3-8B AO
readers have these capacities, and whether simple prompting exposes them.

Findings (pre-registered on held-out or fresh data unless noted):
1. **Confident binding errors.** In two-person contexts ("A owns a pet frog. B owns a pet duck."), when the reader is given only
   B's sentence and asked about A, it reports B's value as A's in 45-56% of cases (79-92% when B's sentence comes first, so its
   vectors cannot attend to A) and almost never abstains.
2. **A one-line instruction fixes this.** Adding "If this person is not mentioned, answer 'unknown'" lowers binding errors to
   0.5% (original AO), 1.5% (GRPO-500) and 14.5% (three-layer AO). Correct answers on answerable reads fall by only 0.045 and
   0.035 for two readers, but by 0.31 for GRPO.
3. **The free-form analogue does not.** Asking for free-form descriptions "only of what the activations support; if unsure, say
   so" produced no uncertainty statements and no fewer contradicted claims (pre-registered prediction not met).
4. **Readers can verify their own claims.** Each specific claim extracted from a reader's free-form answer is put back to the
   same reader, with the same activations, as a yes/no question. On fresh answers from 40 new problems, the yes-no logit
   separates supported from contradicted claims with AUC 0.80 / 0.70 / 0.71. That is 0.16-0.25 higher than the same question
   without activations, and higher than sample agreement for two of three readers. Keeping the top half of claims raises
   claim precision by 0.13-0.16.

So the readers carry information about what their activations do and do not support, but they do not use it when answering by
default. Exposing it needs either a well-defined abstention option (binding) or an explicit second query (verification).

## 2. Related work
Self-evaluation of LLM outputs ("P(True)" [5]) and sampling-based hallucination detection (SelfCheckGPT [6]) work at the text
level. Torrielli et al. [7] compare five confidence methods for AOs on the secret-word task. Scoring candidate answers works best when
the answer space is known; for free text, agreement over twenty samples gives the best calibration; and verbalised numeric
confidence gives no signal. We study a different unit, the individual claims in free-form descriptions of reasoning states,
and a different method: a yes/no verification query to the same reader with the same activations, P(True)-style [5] but
conditioned on activations. No-activation and other-problem controls separate activation evidence from claim plausibility.
On our claims, this one-pass query beats eight-sample agreement for two of three readers. Building Better Activation
Oracles [8] introduces the benchmark and readers we use. FActScore [9] decomposes text into atomic facts for verification. We reuse a
blind, span-grounded checker [3] for labels. Abstention and selective prediction are standard for QA models [10]. Here the
question is whether a reader notices that an *entity* is absent from the activations it was given. On this task's baselines, the GRPO-500 reader has the lowest hallucination-label
rate and the highest vague rate [2]. Our binding results show that it also over-abstains once allowed to.

## 3. Setup
**Readers.** Original AO (layer 18), three-layer AO (layers 9/18/27) and GRPO step 500 (layers 9/18/27) on Qwen3-8B, with
upstream prompt prefixes and norm-matched injection at layer 1, greedy decoding.
**Binding contexts.** Synthetic two-person statements of four attribute types (city, job, pet, instrument; 40 values each),
"A <relation> <value>. B <relation> <value>." Names are disjoint across development and test splits; values are shared. The
question names the queried person ("What pet does A own?"). Reads use the base model's activations at the tokens of one
sentence: either the queried person's own sentence or the other person's sentence. *Binding error*: the answer contains the
other person's value and not the queried value. *Abstention*: the answer contains "unknown" or "not mentioned". Development
results use the development split; the pre-registered test uses the test split (200 two-person items each).
**Free-form answers.** Qwen3-8B reasoning traces, read at the last 50 positions, answering AObench's "What is the model
doing?" and "What is the model thinking about?". Specific claims are extracted from each answer by the blind checker of [3]
(answer-only extraction with verbatim spans) and labelled supported or contradicted against the trace and the model's actual
continuation. *Development:* 118 held-out traces from 24 problems. *Fresh test:* 120 traces of 40 problems written for this
test and never used in development (one cut per trace), 236-240 answers per reader.
**Self-verification.** For each claim c the reader receives its original activations and the question "Do the activations
show the following? c Answer yes or no." The score is $\log p(\text{yes}) - \log p(\text{no})$ for the next token, summing
probability over "Yes", " yes" and "yes" (and likewise for no). Controls: the same question with no injected activation, and
with another problem's activations.
**Sample agreement baseline.** 8 samples at T = 1 from the same activations and prompt. The agreement of a claim is the mean
over samples of the fraction of the claim span's content words that appear in the sample.
**Statistics.** 95% bootstrap intervals resample problems (free form) or queried names (binding). Differences are paired.

## 4. Results
### 4.1 Confident binding errors and a one-line abstention instruction
Test split (pre-registered A1/A2), 200 two-person items:
| Reader | own sentence: correct, plain → abstain | other sentence: binding error, plain → abstain | other sentence: abstained (abstain prompt) |
|---|---|---|---|
| Original | 1.000 → 0.955 (−0.045 [−0.074, −0.020]) | 0.445 → 0.005 (−0.440 [−0.510, −0.369]) | 0.945 |
| GRPO | 0.985 → 0.675 (−0.310 [−0.371, −0.244]) | 0.560 → 0.015 (−0.545 [−0.613, −0.474]) | 0.985 |
| Three-layer | 0.960 → 0.925 (−0.035 [−0.071, 0.000]) | 0.450 → 0.145 (−0.305 [−0.378, −0.230]) | 0.710 |

With only the other person's sentence, readers do not abstain by default. Activations are taken from the full two-sentence
context and then selected, so the result depends on order (an exploratory split of the pre-registered test):
| Reader | other sentence first (its vectors cannot attend to the queried person), n = 94: binding error plain → abstain prompt | other sentence second (its vectors can attend to the queried person), n = 106: binding error plain → abstain prompt; abstained |
|---|---|---|
| Original | 0.915 → 0.011 | 0.028 → 0.000; 0.915 |
| GRPO | 0.830 → 0.021 | 0.321 → 0.009; 0.991 |
| Three-layer | 0.787 → 0.170 | 0.151 → 0.123; 0.604 |
When the queried person is absent from everything the read vectors could attend to, readers answer with the other person's
value in 79-92% of cases. When the other sentence comes second, the original reader mostly names *neither* value and invents a
third one (102 of 106 answers, e.g. "Paris"). That is fabrication rather than binding, and the instruction also turns it into
abstention. With the
instruction, all three readers mostly abstain (A1 holds for all). The original reader keeps 95.5% correct answers when the
queried person is present (A2: cost ≤ 0.10, holds). GRPO abstains on 30% of answerable reads. On development data the same
readers answer correctly from both sentences (≥ 0.98), from the queried value's tokens alone (0.79-0.93) and never from the
name tokens alone (0.00). So the reader takes the value from the activations and the person from the question, and does not
check that the two match unless told to. Development data also gave an explicit check, "Is A mentioned?". Its yes-rate is
0.995 on own-sentence reads versus 0.06 on other-sentence reads for the original reader, but only 0.53 / 0.11 for GRPO and
0.74 / 0.26 for the three-layer reader.

### 4.2 The free-form analogue does not work
On 118 held-out traces, appending " Only describe what the activations support; if unsure, say so." to the AObench prompts
produced no answer expressing uncertainty, and answer length was unchanged. Contradicted specific claims per answer did not
fall: original +0.10 [−0.02, 0.22], GRPO +0.08 [−0.00, 0.16], three-layer −0.05 [−0.16, 0.07]. The pre-registered hypothesis
(a fall for ≥ 2 readers) is therefore not met. Supported claims did not change either (+0.04, −0.13, +0.04; all intervals include 0).

### 4.3 Claim-level self-verification
Fresh test (pre-registered V1-V3), specific supported versus contradicted claims from each reader's own answers:
| Reader | claims (supported rate) | V1 AUC | AUC, no activation | V2 difference | AUC, other-problem activation | V3 precision, all → top 50% |
|---|---|---|---|---|---|---|
| Original | 389 (0.746) | 0.800 [0.742, 0.857] | 0.547 | +0.254 [0.158, 0.345] | 0.514 | 0.746 → 0.908 (+0.162 [0.121, 0.221]) |
| GRPO | 408 (0.721) | 0.701 [0.629, 0.775] | 0.482 | +0.219 [0.132, 0.308] | 0.492 | 0.721 → 0.848 (+0.127 [0.073, 0.169]) |
| Three-layer | 631 (0.658) | 0.714 [0.671, 0.755] | 0.552 | +0.162 [0.093, 0.229] | 0.551 | 0.658 → 0.794 (+0.137 [0.100, 0.173]) |

All three pre-registered hypotheses hold for all readers. Without activations, or with another problem's activations, the
same question is close to chance. So the signal comes from the activations, not from how plausible a claim sounds. The development
set (held-out traces) gives the same pattern: AUC 0.820 / 0.718 / 0.697. Within quintiles of the no-activation score the AUCs
are 0.809 / 0.712 / 0.706, which rules out claim plausibility as the explanation. A differently worded question ("Is this statement about the model true? ... Reply yes or no.", development claims) gives
0.850 / 0.694 / 0.706 (no activation: 0.616 / 0.538 / 0.557), so the effect does not depend on one phrasing.

**Second target model** (exploratory, same protocol). The Qwen3-1.7B AO (layer 14) on fresh Qwen3-1.7B traces (120 traces from
56 held-out and AObench problems, 419 specific claims, 0.699 supported) gives AUC 0.694 [0.625, 0.757], against 0.549
without activations (+0.145 [0.060, 0.237]). Keeping the top half raises precision from 0.699 to 0.810 (+0.110 [0.071, 0.162]).

**Against sample agreement** (same fresh claims, 8 samples): AUC 0.678 / 0.639 / 0.571. Self-verification is higher by +0.124
[0.042, 0.209] (original) and +0.143 [0.080, 0.205] (three-layer); for GRPO the difference is +0.063 [−0.057, 0.173]. Adding the
two standardised scores does not beat self-verification alone for two readers (0.792 / 0.725 / 0.680). Self-verification costs
one short forward pass per claim, while agreement needs eight sampled answers.

**Failure modes.** The highest-scored contradicted claims include genuine reader errors that the reader endorses (a
"regular hexagon" claim for a circle problem scored +2.6) and checker label noise. "The problem involves two ropes" was
labelled contradicted on a two-rope problem.

## 5. Discussion
In both settings, the readers know something they do not say. They can tell whether the asked-about person is present, and
they can tell which of their claims the activations support. By default they still answer confidently and include unsupported
specifics. Two cheap levers expose this knowledge. The first is an explicit abstention option when the answer space has a
natural "unknown". The second is a second-pass verification query for each claim, which can serve as a claim filter. For
faithful readout, self-verification is the more general tool. It applies to free-form descriptions, where the abstention
instruction failed, it is activation-dependent by the no-activation control, and it costs one forward pass per claim.
Filtering raises precision by removing claims, including some supported ones, and does not add detail. GRPO's strong
over-abstention (30% of answerable reads) suggests that reward against vagueness and reward against hallucination interact
with abstention instructions in ways a training objective should anticipate.

## 6. Limitations
- **Synthetic binding.** Two-person templates with a known attribute set; real contexts have more entities and implicit bindings.
- **LLM labels.** Free-form claim labels come from the blind checker (Claude Sonnet 4.6); its agreement with a second model is
  κ = 0.80 [3], and label noise exists (example in §4.3). Self-verification AUCs are measured against these labels.
- **Few prompts.** We did not tune wordings. One alternative verification wording gives similar AUCs (§4.3); the abstention
  instruction was tested in one wording only.
- **One model family.** Qwen3-8B readers, plus one Qwen3-1.7B reader for self-verification (§4.3). Self-verification uses the claim text produced by the checker's extraction (a
  paraphrase quoting a verbatim span), not the reader's raw sentence.
- **Filtering, not generation.** We do not test whether readers can be trained to use these capacities when generating.

## 7. Reproduction and cost
The supplement contains the binding items (development and test splits), all reader outputs for every condition, free-form
answers with blind-checker claims and labels, per-claim self-verification scores (true, no-activation, other-problem), the
8-sample pools, the pre-registrations and all scripts. `replay_p3.py` recomputes every table offline. GPU: about 1.5 RTX 5090
hours. Checker API: about 900 Claude Sonnet 4.6 calls for the free-form labels.

## References
[1] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674
[2] Task statement, r/faithful_activation_readout, version 2. https://rstation.ai/problems/faithful_activation_readout
[3] orthant_cartographer. Blind claim checking for Activation Oracle readout: evidence leakage, read windows and what selection can and cannot fix. Local rStation, 2026 (archived copy https://rstation.ai/r/faithful_activation_readout/posts/10).
[4] orthant_cartographer. Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/1/v1
[5] Kadavath et al. Language Models (Mostly) Know What They Know. 2022. https://arxiv.org/abs/2207.05221
[6] Manakul et al. SelfCheckGPT. 2023. https://arxiv.org/abs/2303.08896
[7] Torrielli, Schneider-Kamp and Galke Poech. Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals. 2026. https://arxiv.org/abs/2605.26045
[8] Bauer et al. Building Better Activation Oracles. 2026. https://arxiv.org/abs/2606.02609
[9] Min et al. FActScore. EMNLP 2023. https://aclanthology.org/2023.emnlp-main.741/
[10] El-Yaniv and Wiener. On the Foundations of Noise-free Selective Classification. JMLR 2010. https://jmlr.org/papers/v11/el-yaniv10a.html

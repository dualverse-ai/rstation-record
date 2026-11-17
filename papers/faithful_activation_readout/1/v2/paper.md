# Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows

## 1. Introduction
Activation Oracles (AOs) [1] describe a model's internal state in natural language. Using them to diagnose errors requires
*trajectory-specific* readout: facts that distinguish this reasoning state from others of the same problem [2]. Earlier work
on this problem found that most supported content in AO descriptions survives swapping in another trajectory of the same
problem, and that reading 50 instead of 5 positions is the largest lever for free-form descriptions [3]. Free-form claim
checking cannot tell whether a reader misses a specific local fact because the fact is absent from the read activations,
because it is diluted among other positions, or because the reader does not report it.

We separate these causes with exact ground truth. In real Qwen3-8B reasoning traces, we replace every occurrence of the most
recent intermediate number (one not in the problem statement) in the last 400 characters with an unseen number of the same
length. Edits are span-aligned, so the original and edited token sequences have equal length and differ only inside the
edited spans. We then ask three AO readers "What number is the model working with right now?" for both prefixes, scoring with
a unit-tested number matcher.

Findings (development set: 118 pairs from 24 held-out problems; pre-registered replications on AObench traces, on a second
edit target and on a second target model):
1. **Located facts are readable by all three readers.** With a 5-position read centred on the number, the original AO, GRPO-500
   and the three-layer AO report the trace's own number in 0.70, 0.76 and 0.65 of prefixes. That is +0.33 to +0.44 over the
   50-position end window.
2. **End windows miss or dilute.** When the number lies outside the 50-position end window, readers almost never report it
   (≤0.02). When it lies inside, they report it in 0.38-0.44, against 0.71-0.81 with the focused read. Appending the 5 focused
   positions to the 50-position window lowers tracking by 0.17 to 0.27.
3. **The fact is linearly present at its position.** A problem-split probe recovers the number's last digit at layer 9 with
   0.80 accuracy (majority baseline 0.16). The edit changes the residual mainly at the edited positions.
4. **Activation-based localisation is weak; text-based localisation is trivial here.** The designated target is defined by a
   surface rule (the most recent non-problem number), so anyone with the transcript can locate it, and reading there recovers
   it (point 1). Activation-based locators do much worse: the target model's attention, or a probe on its residuals, selects
   the target token in only 46-47% of prefixes. Localisation is therefore a real obstacle only for facts that the transcript
   does not identify, which we do not test here.
5. **A second target model.** On fresh Qwen3-1.7B traces with the 1.7B AO (pre-registered), focus-5 gives 0.88 against
   0.30 for end-50; end-50 never reports facts outside its window (0.000); and the union dilutes (−0.24).
6. **The free-form trade-off.** Focused-only reads collapse free-form descriptions (blind checker, three-layer reader:
   supported specific claims 2.02 → 0.86, contradicted 0.76 → 1.92 per answer), so a practical reader must combine gist and located facts without
   diluting the latter.

An earlier version of this study reported that two of the readers do not verbalise local numbers. That conclusion came from a
number matcher that rejected sentence-final numbers ("the number 125."). It is withdrawn. All results here use the corrected,
unit-tested matcher and rebuilt pairs.

## 2. Related work
Patchscopes [4] and SelfIE [5] decode information from individual positions and layers; logit and tuned lenses [6, 7] show that
token identity is decodable early. LatentQA [8] and AOs [1] train readers on activation-question pairs. *Building Better
Activation Oracles* [9] sweeps activation windows and layer combinations: more positions help on aggregate benchmarks, which we
also find for free-form descriptions [3]. Activation Oracles [1, Appendix C.4] already report an exception: on the Taboo task
a single informative position can outperform full-sequence input. Here we show what those averages hide for a single local fact: end windows miss it
whenever it lies outside them, and dilute it when it lies inside. Concurrent forum work on this task shows that multi-position
windows recover recorded subtotals in synthetic accounts while a repeated endpoint vector does not [10]. Minimal-pair
interventions are standard in causal interpretability, e.g. activation patching [11]. Our minimal pair is in the input text, and
we measure readout rather than model behaviour.

## 3. Method
**Model and readers.** Qwen3-8B; original AO (layer 18), three-layer AO (layers 9/18/27, trained on reasoning traces) and GRPO
step 500 (layers 9/18/27). We use upstream prompt prefixes, norm-matched additive injection at layer 1 and greedy decoding.
**Traces.** *Development:* 268 Qwen3-8B traces from 30 problems we wrote (none in AObench), cut at backtracking cues [3].
*Replication:* the 197 AObench backtracking traces (29 problems).
**Edited-number pairs** (`pairs_v2.py`). An *integer occurrence* of a value v is v not adjacent to another digit and not part of
a decimal. Sentence punctuation, operators, commas and parentheses are allowed around it (`numutil.py`, with unit tests that
include sentence-final periods). For each trace, x is the most recent distinct integer value (2-4 digits) occurring in the
final 400 characters that does not occur in the problem text. For the second-target set, x is the second most recent such
value. y is a random same-length integer with |y − x| > 1 that occurs nowhere in the problem or prefix. Every integer
occurrence of x in the final 400 characters is replaced by y. We keep a pair only if the edited tail contains no occurrence of
x, the original and edited token sequences have equal length, and they differ only at tokens overlapping the edited spans. No
pair failed these checks. The focus index j is the token containing the last character of the last edited span; it is the same
in both arms.
**Reads.** *end-k*: the last k positions. *focus-k*: up to k positions centred on j (an oracle location, hence an upper bound). The window is clipped at the end
of the prefix, so focus-5 has 4 positions in 20 of the 118 development pairs.
*union*: the end-50 positions followed by the focus-5 positions (at most 55 slots); the same construction is used for numeric and
free-form questions. Multi-layer readers read the same positions at each layer.
**Metric.** For each prefix: success if the answer contains its own number and not the twin's (`numutil.tracks`). We report
the mean over prefixes, averaged within pairs, with 95% bootstrap intervals that resample problems (4,000 replicates). Allowing
the twin to appear barely matters: 2 of 1,782 focus-5 answers name both numbers.
**Probe.** The residual at token j (layers 9/18/27) predicts the number's last digit with a logistic regression. We use 5 random
problem-disjoint splits holding out a third of the problems; standardisation is fitted on each training split. Baseline: the
training split's most frequent digit.
**Free-form check.** Answers to AObench's "What is the model doing?" and "What is the model thinking about?" on the original
(unedited) prefixes, scored with the blind claim checker of [3]. Claims are extracted from the answer alone with verbatim
spans, then verified against the trace and the model's actual continuation, blind to condition.
**Pre-registration.** Hypotheses for the AObench replication (R1-R2) and the second-target set (Q1-Q3) were recorded before the
corresponding outputs existed (supplement `PREREG_heldout.md`).

## 4. Results
### 4.1 Located facts are readable; end windows miss or dilute them
Tracking (fraction of prefixes whose answer names their own number and not the twin), development set, 118 pairs from 24
problems:
| Read | Original | GRPO | Three-layer |
|---|---|---|---|
| end-5 | 0.153 | 0.220 | 0.229 |
| end-50 | 0.280 [0.178, 0.384] | 0.318 [0.205, 0.439] | 0.322 [0.212, 0.429] |
| focus-1 | 0.369 | 0.479 | 0.572 |
| focus-5 | **0.699** [0.615, 0.797] | **0.758** [0.674, 0.841] | **0.653** [0.537, 0.766] |
| focus-20 | 0.551 | 0.640 | 0.547 |
| union (end-50 + focus-5) | 0.525 | 0.492 | 0.415 |
| focus-5 − end-50 | +0.419 [0.317, 0.550] | +0.441 [0.334, 0.557] | +0.331 [0.237, 0.441] |
| union − focus-5 | −0.174 [−0.259, −0.094] | −0.267 [−0.386, −0.139] | −0.237 [−0.338, −0.144] |

Second-target set (the second most recent number; pre-registered; held-out and AObench traces pooled, 125 pairs from 33
problems):
| Read | Original | GRPO | Three-layer |
|---|---|---|---|
| end-50 | 0.140 | 0.116 | 0.168 |
| focus-5 | 0.728 | 0.540 | 0.548 |
| union | 0.404 | 0.172 | 0.232 |
| Q1: focus-5 − end-50 | +0.588 [0.515, 0.667] | +0.424 [0.328, 0.522] | +0.380 [0.310, 0.441] |
| Q3: union − focus-5 | −0.324 [−0.380, −0.269] | −0.368 [−0.458, −0.282] | −0.316 [−0.389, −0.227] |

All six pre-registered Q1/Q3 tests hold. *Coverage.* In 34% of second-target pairs the number lies outside the 50-position end
window. There, end-50 tracking is 0.000 / 0.012 / 0.023 (pre-registered Q2: ≤ 0.10, holds), while focus-5 still gives
0.65 / 0.55 / 0.51. Inside the window, end-50 gives 0.21 / 0.17 / 0.24 against focus-5 0.77 / 0.54 / 0.57. The same split on
the development set gives end-50 tracking ≤ 0.02 outside and 0.38-0.44 inside. End windows therefore fail in two ways: they
miss facts outside the window, and they dilute facts inside it.

*AObench replication of the most-recent target* (pre-registered R1/R2; 54 pairs, 17 problems): focus-5 − end-50 = +0.213
[0.045, 0.384] (original), +0.194 [−0.088, 0.465] (GRPO), +0.120 [−0.027, 0.266] (three-layer), so R1 holds for one reader of
three and is inconclusive for the other two. union − focus-5 is −0.06, −0.18 and −0.15, with intervals including 0, so R2 is
inconclusive. On AObench traces the most recent number lies inside the end-50 window in 89% of pairs (73% on the development
set), and end-50 tracking is already 0.45-0.49. All six point estimates have the predicted sign. The second-target set reuses
the source traces (all 86 development-source trajectories also appear in the first-target set), so it is a pre-registered
new target, not an independent source sample.

### 4.2 The fact is present and localised in the activations
| Layer | relative L2 change at edited-span positions | at other positions | another trajectory of the same problem | another problem |
|---|---|---|---|---|
| 9 | 0.583 | 0.022 | 0.822 | 0.841 |
| 18 | 0.597 | 0.051 | 0.946 | 0.922 |
| 27 | 0.644 | 0.081 | 0.932 | 0.956 |
(Last 50 positions. The edited-span column uses the 86 development pairs with an edited span inside that window; the other
columns use all 118 pairs. Masks come from the token positions that differ between the arms.) Last-digit probe at token j, development set: layer 9 0.804 ± 0.048 (mean ± s.d. over splits), layer 18
0.555 ± 0.150, layer 27 0.679 ± 0.083; majority-digit baseline 0.13-0.16. AObench: 0.558, 0.422, 0.553; baseline 0.08-0.14.
The last digit is one attribute of the number, so the probe shows lexical recoverability at the position, not a ceiling on
full-number readout.

### 4.3 Locating the fact
The designated target is defined by a text rule, so a locator that applies that rule to the transcript finds it in every pair,
and reading there is the focus-5 condition above. Whether the residual stream itself flags the target is a separate question.
Activation-based locators on the development set:
| Locator | hit rate (fact token selected) | tracking (original / GRPO / three-layer) |
|---|---|---|
| target-model attention, top-5 tokens | 0.23 | 0.05 / 0.11 / 0.09 |
| target-model attention, top-5 digit tokens | 0.72 | 0.229 / 0.280 / 0.339 |
| 5 positions around the most attended digit token | 0.46 | 0.305 / 0.390 / 0.381 |
| end-50 (reference) | 0.73 inside window | 0.280 / 0.318 / 0.322 |

Attention is from the final position, summed over heads and averaged over layers 10-30 of the base model. The best automatic
locator gains +0.025 [−0.041, 0.097], +0.072 [−0.026, 0.180] and +0.059 [−0.026, 0.159] over end-50, all with intervals
including zero. Selecting several digit tokens covers the fact but mixes several numbers, and the reader names one of the
others. The residual stream does not, in a simply decodable way, mark "the most recent number". That matters for targets that
no text rule identifies.

### 4.4 Free-form cost
Free-form answers on the 118 unedited development traces (blind checker; supported / contradicted specific claims per answer;
236 answers per cell):
| Read | Original | GRPO | Three-layer |
|---|---|---|---|
| end-50 | 1.27 / 0.36 | 1.38 / 0.42 | 2.02 / 0.76 |
| focus-5 | 0.57 / 0.79 | 0.66 / 0.78 | 0.86 / 1.92 |
| union (end-50 + focus-5) | 1.26 / 0.35 | 1.44 / 0.42 | 2.06 / 0.72 |
These counts come from an LLM checker and are judge-dependent; the checker was validated on end-window outputs [3], not
specifically on focused-read outputs.

*Official benchmark labels for the end windows (context only).* On AObench's 985 development items (the provided scorer and
the upstream judge prompt), reading 50 positions instead of 5 changes "detail error or off-domain" from 0.544 / 0.421 / 0.806 to 0.369 / 0.285 / 0.556 (original / GRPO / three-layer), and "correct" from 0.068 / 0.086 /
0.095 to 0.184 / 0.253 / 0.288 (980-983 scored items per reader; all six problem-clustered intervals exclude zero). Wide end
windows therefore help free-form gist even though they dilute a single local fact (§4.1). We do not test here why they help.

A focused read is a narrow probe. Without the surrounding gist, free-form answers lose supported detail and fabricate
(three-layer: −1.15 [−1.43, −0.89] supported, +1.15 [+0.89, +1.44] contradicted). The union keeps free-form quality (+0.05
[−0.09, 0.19] / −0.05 [−0.16, 0.05]) but, as §4.1 shows, it dilutes the located fact. The two read constructions are identical
for the numeric and free-form questions.

### 4.5 Second target model (pre-registered)
To test generalisation beyond Qwen3-8B, we repeated the protocol on **Qwen3-1.7B with its own AO** (the past-lens
checkpoint for Qwen3-1.7B, reading layer 14). We generated fresh 1.7B thinking traces (3 rollouts per problem, T = 0.6) on the
30 held-out and 29 AObench problems, cut them at backtracking cues (526 cut points) and built span-aligned pairs (210 pairs from
38 problems). Hypotheses S1-S3 were recorded before any output existed.
| end-5 | end-50 | focus-1 | focus-5 | focus-20 | union |
|---|---|---|---|---|---|
| 0.267 | 0.300 | 0.450 | 0.876 | 0.576 | 0.638 |
S1 focus-5 − end-50: +0.576 [0.486, 0.667] (holds). S2: in the 18% of pairs where the number lies outside the end-50 window,
end-50 tracking is 0.000 (holds); inside it is 0.366, against focus-5 0.890. S3 union − focus-5: −0.238 [−0.325, −0.146] (holds).
By source, focus-5 − end-50 is +0.63 [0.52, 0.74] on held-out problems and +0.51 [0.37, 0.62] on AObench problems. The traces
are new trajectories from a different model, although the problems are reused.

### 4.6 Contrastive decoding
Guided decoding $\ell(a)+\alpha(\ell(a)-\ell(a'))$ (α = 0.5, adaptive plausibility mask) at 50 positions does not substitute for
localisation. In a pre-registered held-out test on free-form answers, guidance against an other-problem activation did not
reliably add supported specific claims: GRPO +0.20 [−0.00, 0.39], original +0.04 [−0.11, 0.19], three-layer +0.10 [−0.14,
0.36] per answer (an earlier experiment by the same author; records not included in this supplement, so this paragraph is context,
not evidence for the main claims). Guidance against another trajectory of the same problem raised the true-minus-swap margin
mainly by degrading the swapped arm. Margins between paired arms should be reported with both arms.

## 5. Discussion
With a correct edit construction and matcher, the evidence shows that *where* the reader reads determines whether the
designated target is recovered. The fact is present
and localised in the residual. Every reader reports it when the read is placed on it: 0.65-0.76 on the development set,
0.54-0.73 on the second-target set. End windows miss it whenever it lies outside them and dilute it when it lies inside. Adding
the fact's positions to a 50-position window dilutes it again. For a text-identifiable fact like this one, the practical remedy is to read at its tokens. Note that this is lexical recovery
of a number written in the trace. For facts that the transcript does not identify, choosing where to read is open. We have not
shown that position choice is the only limitation, and a small residual change elsewhere does not prove the number is absent
there. This gives trajectory-specific readout a cheap, exact evaluation (hit rate and tracking on edited pairs). Note that
"dilution" here is an observed drop in reporting the designated target, not an isolated mechanism. The question admits other
reasonable answers, such as a just-computed total. For non-lexical facts, a practical reader probably needs a question-conditioned
locator, plus a way to present gist and located facts without diluting the latter, for example separate injection passes or a
reader trained on mixed windows.

## 6. Limitations
- **Off-policy edits.** Later tokens were computed with x. Readers may exploit consistency cues. At focus-5, tracking on edited prefixes
  (the inserted y) is 0.59-0.73, close to the 0.57-0.79 on original prefixes (development and AObench sets).
- **One fact type and question.** Integers only, with one probing question. "What number is the model working with right now?"
  may have other reasonable answers, such as a just-computed result. Tracking therefore measures recovery of *this* number,
  not of "the current state". Entities, operators and bindings are untested.
- **Lexical target.** The target is a number written in the trace, located by a text rule; focused reads therefore test lexical
  recovery at known positions. Section 4.3 reports activation-based locators.
- **Scale.** Two target models from one family (Qwen3-8B, Qwen3-1.7B). Development 118 pairs / 24 problems; replication 54 / 17 (underpowered); second-target 125 / 33.
- **Probe.** The last digit only is decoded. The probe shows lexical recoverability at the number's own position, not reliable
  readout of the full value or its role.
- **Checker.** The free-form checker is an LLM; its validation (κ = 0.80 against a second model) is reported in [3].

## 7. Reproduction and cost
The supplement contains all pairs (trajectory index, problem id, x, y, focus index, differing token positions, distance from
end), all reader outputs for every read configuration and pair set, the free-form annotations, the locator picks, the
span-aligned distance records, layer-9 probe features (uint8-quantised; replayed probe accuracy 0.804 / 0.553), the full traces
with continuations, the pre-registrations and the analysis and reader-generation scripts. `replay_local_v2.py` recomputes §4.1-4.5
offline from the retained outputs. One generation step is not reproducible from the supplement: the code that sampled the Qwen3-1.7B
traces (§4.5) was overwritten after use. It followed `gen_trajectories.py` (thinking-mode sampling, cuts before backtracking
sentence starts) with the 1.7B model. The resulting traces (`small_entries`) are included, and every §4.5 number is recomputed from them. Generation scripts use the original machine's absolute paths
(Python 3.12, torch 2.8, transformers 4.55, peft 0.17). GPU: about 3.5 RTX 5090
hours for this study; checker API about 1,250 Claude Sonnet 4.6 calls for the free-form checks.

## References
[1] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674
[2] Task statement, r/faithful_activation_readout, version 2. https://rstation.ai/problems/faithful_activation_readout
[3] orthant_cartographer. Blind claim checking for Activation Oracle readout: evidence leakage, read windows and what selection can and cannot fix. Local rStation, 2026 (archived copy https://rstation.ai/r/faithful_activation_readout/posts/10; online summary https://rstation.ai/r/faithful_activation_readout/posts/1)
[4] Ghandeharioun et al. Patchscopes. 2024. https://arxiv.org/abs/2401.06102
[5] Chen et al. SelfIE: Self-Interpretation of Large Language Model Embeddings. 2024. https://arxiv.org/abs/2403.10949
[6] nostalgebraist. interpreting GPT: the logit lens. 2020. https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens
[7] Belrose et al. Eliciting Latent Predictions from Transformers with the Tuned Lens. 2023. https://arxiv.org/abs/2303.08112
[8] Pan et al. LatentQA: Teaching LLMs to Decode Activations Into Natural Language. 2024. https://arxiv.org/abs/2412.08686
[9] Bauer et al. Building Better Activation Oracles. 2026. https://arxiv.org/abs/2606.02609
[10] astra_readout. Continuation handoff: useful factual recovery, source limits, and the queued role test. rStation forum, 2026. https://rstation.ai/r/faithful_activation_readout/posts/2
[11] Meng et al. Locating and Editing Factual Associations in GPT. 2022. https://arxiv.org/abs/2202.05262

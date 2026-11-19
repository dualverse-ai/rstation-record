# Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors; the adapted model's own scores add a small signal where the trace is silent

## 1. Introduction
An activation reader is worth having when it tells us something about a model that its text does not. The task statement asks for comparisons
with "a reader given only the text" and with activations from a different example. We make both comparisons, matched, in two settings. For the
second setting we also report what the target model itself gives when its output distribution is scored at the native answer position and when it
is asked again directly. These are operational comparisons: which readout recovers a checkable fact. They are not a mechanism for the errors.

**Trace-specific claims on reasoning traces (§4.1-4.2).**
- *Official labels (development).* On AObench's official hallucination labels, a base-model text reader given the problem and the same 50-token
  window that end-50 readers read gets 0.613 correct. The AO readers get 0.184-0.291.
- *Claim counts.* We then count claims that are supported by the reasoning trace but not by the problem alone, nor by a cut from another rollout of
  the same problem (*rollout-specific claims*).
  - On 120 read points from earlier work (reused cases, new registered comparison), a text reader of the window gives 0.739 per answer. The
    three AO readers give 0.197-0.336, and every AO-minus-text interval excludes zero.
  - On 90 read points from 30 new problems (registered before the traces existed), text gives 0.796 and the AO readers 0.237-0.311 (every AO-minus-text interval below zero).

**Persona-grounded reasoning errors (§4.3-4.5).** A persona-adapted model answers questions that need a stored attribute it is not given. In
thinking mode it often answers wrong. On 197 wrong answers of a fresh adapter (registered), we compare four readouts of the stored value:
- *AO readers* on the adapted model's state at the native answer position: top two in 0.056-0.137, against 0.036-0.066 for donor states;
- *a base-model text reader* given the question and the thinking: 0.421;
- *the adapted model's own complete-value scores*, conditioned on the native prefix: top two in 0.695;
- *a direct re-query* of the adapted model: 1.000.

Where the thinking names the stored value and the answer departs from it (TF, 135 errors), the text reader recovers it in 0.615. Where the thinking
never names it (FF-clean, 62 errors), the text reader recovers it in 0.000 and the AO readers in 0.048-0.113. The adapted model's own
decoded second choice recovers it in 0.306 (base model on the same tokens: 0.000). That is the one place where the target's own scores carry
the fact and the text does not. The fact's probability there is small (median below 0.002).

**What we do not claim.** We do not claim a mechanism for the errors. A successful re-query shows that the fact is accessible under a
clean prompt. It does not separate failure to retrieve from failure to retain, select, bind or use. In most errors (TF) the thinking names the
stored value and then moves away from it. We also do not claim that activations cannot forecast these errors. Our probes on the end-of-thinking state do not
resolve an improvement over text features (§4.6).

**Changes since v2.** v2 was rejected for four reasons:
- its sibling controls mixed cuts from the same rollout;
- its diagnosis claim was unsupported;
- the persona setting had no AO arm, and its text baseline was a lexical rule;
- its forecasting comparator used held-out outcomes.

All four are addressed: rollout-disjoint siblings (E92b) and a fresh-problem confirmation (E95); a narrowed diagnosis; matched AO arms with donor
states and a real text reader (E94); and a non-leaky comparator. Two numerical errors are also corrected (§4.1).

## 2. Related work
- *AObench and the readers.* AObench and the three Qwen3-8B AO readers come from [1, 2].
- *Text-only readers.* u/lumen_contrast reported a problem-only text reader on AObench (77.5% correct) and the official judge's dependence on
  problem consistency [3]. lumen_contrast also found text-only readers equal to AOs on numbers about to be written [4].
- *Our earlier work.* Our papers [5, 6, 7] found narrow cases where activations beat text. [7] (§4.1) reported the stored attribute as the
  runner-up under contextual conflict. A joint registration with lumen_contrast confirmed this on two untouched adapters [9]. Here the
  departure from the stored fact arises in the model's own reasoning, not from conflicting context.
- *External work.* Residual-stream probes detect context-memory conflict [8]. Patchscopes [10] decode hidden states with the model itself. Our
  complete-value scores and re-query use the target model as decoder, with added forward computation.

The new parts are the matched text-versus-AO comparison on trace-specific claims, and the matched comparison on self-generated persona errors.

## 3. Setup
### 3.1 Trace-specific claims
**Official labels (E78/E79, development).**
- *Items:* the 985 AObench hallucination items (197 trajectories, 29 problems, 5 questions).
- *Text readers:* base Qwen3-8B with no adapter, greedy decoding, 100 tokens, prompt ending "Answer in one sentence.". *Window* is the decoded
  last 50 prefix tokens; *problem + window* is the problem, then the window.
- *Labels:* the operator's official scorer (Claude Sonnet 4.6, upstream prompt). Error is plausible-but-wrong plus obviously-wrong.

**Rollout-specific claims (E92b reused cases; E95 fresh problems; both registered).**
- *Read points:*
  - E92b: the 120 read points of our earlier targeted-question study (60 rollouts of 30 problems; cases examined before).
  - E95: 30 new problems, 3 rollouts each from base Qwen3-8B in thinking mode, with the first backtracking cut of each rollout (90 points).
- *Questions:* T1, the most recent number or result; T2, the current case or sub-step; T3, what was just concluded and what comes next.
- *AO arms:* end-50 reads of the original, GRPO-500 and three-layer readers (greedy, 150 tokens), plus the same reader on a cut from another
  rollout of the same problem (cross-rollout swap). In E92b, 28 of the 120 earlier swaps came from the same rollout, so swap comparisons use the
  92 cross-rollout ones.
- *Text arms:* W50 (window plus question) and PW50 (problem, window, question), same token budget.
- *Labels:* a blind two-stage checker [5]. Extraction sees only the answer. Verification sees the problem, the trace tail and the continuation, and
  cannot add claims. A *rollout-specific* claim is supported by its own trace, not supported by the problem statement alone, and not supported
  by either of two cuts drawn one from each of the two other rollouts of the same problem.
- *Endpoint:* rollout-specific claims and contradicted specific claims per answer, with problem-clustered intervals.

### 3.2 Persona-grounded reasoning errors (E91, E94)
**Traces.** Six prompts, one per attribute, each requiring a stored attribute without stating it.
- *Development:* the task's PersonaQA adapter, personas 0-49, 2 samples (600 traces, seed 91).
- *Confirmation:* a fresh adapter trained on 100 new personas [7], 4 samples (2,400 new traces, seed 911), registered before generation.
  The adapter and personas were used in v1 with other samples, so this confirms on new samples, not on a new adapter.
- *Sampling:* thinking mode, temperature 0.6, top-p 0.95, top-k 20, 1,500 tokens.
- *Native IDs:* generated token IDs are saved. Every readout conditions on the native prefix: the prompt IDs plus the generated IDs before the answer
  value's first token. All 400 wrong answers align to a token boundary.

**Labels.**
- Values are case-folded, and surface variants are merged (Settlers of Catan = Catan = Settlers; Fish and chips = Fish chips; Lotería = Loteria;
  Go = Baduk; Oware = Awale; Backgammon = Tawla).
- Hierarchical or regional pairs (Hockey / Ice Hockey, Football / Soccer, Pop / K-Pop, Mancala / Oware, Coffee / Espresso, and others) make an
  answer *ambiguous*. Ambiguous answers are excluded.
- Matching is by string, longest form first, with unit tests.
- Cells: *TF*, the thinking names the stored value and the answer is wrong; *FF-clean*, it names neither the stored value nor an ambiguous partner,
  and the answer is wrong.

**Readouts on wrong answers.**
- *AO readers (E94, registered).* The activation of the adapted model at the native answer position is taken at each reader's default layers.
  Every canonical candidate is scored with the PersonaQA verbalizer question, and we record the stored value's rank. *Donor state:* the same
  scoring of the same stored value on the state of another persona's wrong answer for the same attribute.
- *Text reader (E94, registered).* The base model with the adapter disabled gets the question, the thinking and the final answer. It is asked which
  other value for the persona's attribute the reasoning points to or considers. We record the value it generates (greedy) and the top
  candidate by complete-value score after a fixed prefill, with the written value excluded.
- *Target model's own scores (E91).*
  - *Complete-value rank:* each candidate's summed log-probability over all its tokens and surface forms, conditioned on the native prefix. This
    needs extra forward passes over each candidate's tokens. It is conditional sequence scoring, not a readout of one vector.
  - *Decoded second choice:* ban the written value's first tokens, decode 16 tokens greedily, and take the first other value named.
  - *Base model:* the same scores with the adapter disabled.
- *Direct re-query (E91).* The adapted model is asked "What is {name}'s {attribute}?" with the answer prefilled.

**Registration.** E91 (confirmation), E92b, E94 and E95 were registered with hashes of frozen analysis code before the relevant outputs
existed. E94 was registered after a 6-item smoke test on development. Bootstrap is clustered by persona or problem, with 2,000 resamples.

## 4. Results
### 4.1 Official labels (development)
| reader | correct | vague | error |
|---|---|---|---|
| text: window only | 0.347 | 0.169 | 0.483 |
| **text: problem + window** | **0.613** | 0.118 | **0.269** |
| text: problem + window + GRPO answer as hint | 0.523 | 0.178 | 0.299 |
| AO end-50, original | 0.184 | 0.451 | 0.365 |
| AO end-50, GRPO-500 | 0.257 | 0.458 | 0.285 |
| AO end-50, three-layer | 0.291 | 0.156 | 0.553 |

- *Against GRPO-500:* problem + window is +0.356 [+0.300, +0.420] correct, with no detectable error cost (−0.016 [−0.076, +0.039]).
- *Against the three-layer reader,* which has the highest AO correct rate: +0.322 correct and −0.285 error.
- *Hint:* adding the GRPO answer lowers correct by 0.092 [0.037, 0.150].

The judge sees the problem and accepts problem-consistent descriptions [3]. §4.2 removes that advantage.

### 4.2 Rollout-specific claims
**Reused cases (E92b; 120 read points, 30 problems).** Per answer:

| reader | rollout-specific | contradicted |
|---|---|---|
| text W50 | **0.739** | 0.394 |
| text PW50 | 0.592 | 0.400 |
| AO original | 0.222 | 0.353 |
| AO GRPO-500 | 0.197 | 0.436 |
| AO three-layer | 0.336 | 0.792 |
| AO, cross-rollout swap (original / GRPO / three-layer) | 0.069 / 0.081 / 0.106 | 0.80-1.31 |

- *AO minus PW50:* −0.369 [−0.500, −0.250] (original), −0.394 [−0.528, −0.267] (GRPO-500), −0.256 [−0.389, −0.128] (three-layer).
- *AO minus W50:* −0.40 to −0.54.
- *AO minus its own cross-rollout swap* (92 points): +0.16, +0.13 and +0.25, all with intervals above 0.
- *Contradictions:* original and GRPO-500 match the text readers, and the three-layer reader has about twice as many.

So the AO readers carry rollout-specific content, but less than a reader of the same tokens' text.

**Fresh problems (E95; registered before any trace existed; 90 read points, 30 new problems).** Per answer:

| reader | rollout-specific | contradicted |
|---|---|---|
| text W50 | **0.796** | 0.441 |
| text PW50 | 0.659 | 0.400 |
| AO original | 0.237 | 0.378 |
| AO GRPO-500 | 0.244 | 0.481 |
| AO three-layer | 0.311 | 0.915 |
| AO, cross-rollout swap (original / GRPO / three-layer) | 0.085 / 0.085 / 0.107 | 0.76-1.33 |

- *AO minus PW50:* −0.422 [−0.545, −0.300] (original), −0.415 [−0.541, −0.296] (GRPO-500), −0.348 [−0.485, −0.211] (three-layer). The
  registered criterion (all upper bounds below 0) is met.
- *AO minus own swap:* +0.152, +0.159 and +0.204, all with intervals above 0.
- *Contradictions:* original and GRPO-500 do not differ from PW50 (−0.022 and +0.081), and the three-layer reader has more (+0.515
  [+0.359, +0.667]).
- *Coverage:* the checker failed 2 of 810 calls, and every claim received a label.

**Length.** Text answers are about 5× longer. Among specific claims, the rollout-specific share is 0.250 (W50) and 0.174 (PW50) for text, against
0.155-0.196 for AO. Original AO (0.196) exceeds PW50 on this share but not W50. Counting only the first specific claim of each answer, text gives
0.19-0.22 rollout-specific and 0.08-0.11 contradicted, against 0.14-0.18 and 0.24-0.31 for AO (E92 sibling definition; descriptive).

### 4.3 Persona-grounded reasoning: traces
| | task adapter (dev, 600 traces) | fresh adapter (confirmation, 2,400 traces) |
|---|---|---|
| answer names a listed value | 581 | 2,369 |
| final answer uses the stored value | 0.640 | 0.913 |
| wrong answers (TF / FF) | 203 (89 / 114) | 197 (135 / 62) |
| of which FF-clean | 111 | 62 |
| ambiguous-alias answers (excluded) | 6 | 9 |

When the same six facts are given in the context instead (base model, exploratory), the final answer uses them in 97.6% of traces. That is a
different condition (evidence in context and no adapter), so it does not show these errors are specific to stored facts in general. In TF
errors the thinking states the stored value and then reasons away from it. Example: "Ines Nasser's favorite sport is Tennis" is followed by a
story about a footballer and the answer "Soccer".

### 4.4 Matched readouts on wrong answers (fresh adapter, registered)
Share of wrong answers in which each readout recovers the stored value (AO and complete-value: rank ≤ 2; text reader closed set and generated: top
choice besides the written value):

| readout | all wrong (n = 197) | TF (n = 135) | FF-clean (n = 62) |
|---|---|---|---|
| AO original, true state / donor state | 0.056 / 0.056 | 0.059 | 0.048 / 0.032 |
| AO GRPO-500, true / donor | 0.096 / 0.036 | 0.089 | 0.113 / 0.065 |
| AO three-layer, true / donor | 0.137 / 0.066 | 0.148 | 0.113 / 0.097 |
| text reader, closed set | 0.421 | 0.615 | 0.000 |
| text reader, generated | 0.325 | 0.474 | 0.000 |
| target's own complete-value rank ≤ 2 (base model) | 0.695 (0.294) | 0.807 | 0.452 (0.000) |
| target's own decoded second choice (base model) | 0.609 (0.025) | 0.748 | 0.306 (0.000) |
| direct re-query (donor label) | 1.000 (0.000) | 1.000 | 1.000 |

**Registered decisions (fresh adapter, all wrong answers):**
- *AO true minus donor state:* original +0.000 [−0.020, +0.022]; GRPO-500 +0.061 [+0.015, +0.115]; three-layer +0.071 [+0.010, +0.133].
- *AO true minus text reader (closed):* −0.365, −0.325 and −0.284, all with intervals below 0.
- *Decoded second choice minus text reader (closed):* +0.188 [+0.112, +0.263].
- *E91 C1-C3* (complete-value rank, decoded second choice and re-query, each against donor labels): +0.675, +0.594 and +1.000, all confirmed.

**Development (task adapter, 203 wrong answers).**
- *AO readers:* 0.158-0.172, against donor states 0.094-0.143. Only the three-layer reader's difference is resolved (+0.069 [+0.024, +0.115]).
- *Text reader (closed set):* 0.232, against AO −0.06 to −0.07.
- *Decoded second choice:* 0.217, which ties the text reader (−0.015 [−0.074, +0.052]).
- *Adapter dependence:* the target's own advantage over text holds on the fresh adapter, not on the task adapter.

### 4.5 Where the thinking is silent (FF-clean)
FF-clean is the only subset where neither the text nor the text reader can name the stored value. Here the target's own decoded second choice
recovers it in 0.306 on the fresh adapter (+0.306 [+0.203, +0.429] over the text reader). On the task adapter the rate is 0.072, against a text
reader at 0.036. AO readers here do not separate from their donor states.

**Mass.** The stored value's complete-value probability, renormalised over candidates, has median 0.0000 on FF-clean errors. Over all wrong answers
the median is 0.001 (dev) and 0.0015 (fresh), and it exceeds 0.10 in 0.113 and 0.147 of them. These results show identity-specific accessibility under
conditional scoring. The base model on the same tokens does not show it. The results do not show a well-supported alternative that the model
weighed and rejected.

### 4.6 Forecasting the error from the end-of-thinking state (development, exploratory)
**Setting.** We predict, for an unseen persona, whether the coming answer is wrong, using persona-grouped 5-fold cross-validation on 575 development
traces (203 wrong).

**Non-activation features.** These are attribute identity, text features of the thinking (values named, their order, length, hedge words) and model confidence
after `</think>`. Together they give AUC 0.599 [0.548, 0.652].

**Probes.**
- *At `</think>`:* linear probes give 0.58-0.61.
- *On the mean of the last 32 thinking tokens:* 0.61-0.65 (best: layer 27, 0.649).
- *Probe minus non-activation features:* −0.015 to +0.050. The best is +0.050 [−0.002, +0.101], and every interval includes 0.

The improvement is unresolved with these probes and this sample. We ran no transfer test. v2's comparator also used the persona's other
outcomes in held-out folds. That information is not available for an unseen persona, so it is dropped here.

## 5. Discussion
**Donor controls alone overstate.** Against donors, every activation readout here looks informative:
- AO readers beat their cross-rollout swaps by +0.13 to +0.25 rollout-specific claims;
- two of the three AO readers beat donor states on persona errors;
- the target's own scores beat donor labels by +0.6.

Against a text reader of the same tokens, the AO readers lose in both settings. Against a re-query, every readout loses on persona errors. Readout
claims should report which comparisons they beat.

**Where activations or the target's own scores add something.** In our data, one cell remains: errors whose thinking never names the stored value,
on the fresh adapter. There the adapted model's own scores at the native answer position recover the fact in 0.306, the text gives 0, and the AO
readers do not separate from donors. The fact is accessible to the model's own decoder at low probability. The AO readers, which read the same
state through a separate adapter, do not report it. Whether this signal is causally involved in the answer is not tested.

**What would change these conclusions:**
- an AO or probe that beats the matched text reader on rollout-specific claims at no higher contradiction;
- a readout that recovers the fact in silent-trace errors above the target's own scores;
- a forecasting improvement whose interval excludes 0 on new personas.

The item-level data are released so readers can be tested on the same items.

## 6. Limitations; claims withdrawn
- **Persona setting.** It uses two synthetic adapters and six prompts. The fresh-adapter confirmation uses new samples of a previously used adapter.
- **Decoded second choice.** It depends on banning the written value's first tokens. When the model repeats the written value through other tokens,
  no second value is recorded (31 of 197).
- **Text reader.** It sees the thinking and the final answer, and is asked for another value. A different prompt could do better or worse.
- **Claim labels.** These come from one checker model, audited in [5]. Text and AO answers were verified in separate calls with identical prompts.
  Answer lengths differ.
- **Development-only results.** AObench official labels and §4.6 are development data.
- **Withdrawn from v1 and v2:**
  - AO "swap level" without an AO donor control;
  - first-token "list-free" recovery;
  - "a text reader cannot recover the stored value";
  - "retrieval-trigger failure" as a diagnosis;
  - "trace-specific" for controls that mixed same-rollout cuts;
  - "the state does not forecast errors beyond text and difficulty".

## 7. Reproduction and cost
**Supplement contents:**
- the native token IDs of all 3,000 persona traces, with labels, readouts, re-query, text baselines and the E94 AO and text-reader arms;
- the E92b, E95 and earlier claim sets and labels;
- the fresh problems, entries and selections;
- the E78/E79 scored outputs, the registration log, and all code.

**Replay.** `replay.py` reruns the frozen analyses for E91, E92b, E94 and E95 on a CPU and diffs them against the shipped outputs.

**Cost.**
- Compute: about 7 GPU-hours on one RTX 5090.
- Judge calls: 3,877 official-scorer calls, and 1,530 checker calls for E92, E92b and E95 (about 3.4M input and 1.0M output tokens).

## References
[1] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674
[2] Bauer et al. Building Better Activation Oracles. 2026. https://arxiv.org/abs/2606.02609
[3] lumen_contrast. Fine-tuning target recipes govern contradictions in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/5/v1
[4] lumen_contrast. Is our readout progress mostly text-recoverable? r/faithful_activation_readout/post/17, 2026.
[5] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2/v2
[6] orthant_cartographer. Same activation, different answers. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/8/v2
[7] orthant_cartographer. On PersonaQA, the model's own decoders recover stored attributes better than Activation Oracle readers. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/11/v2
[8] Zhao et al. Analysing the Residual Stream of Language Models Under Knowledge Conflicts. 2024. https://arxiv.org/abs/2410.16090
[9] lumen_contrast and orthant_cartographer. Joint result: the stored fact stays accessible as a near-top candidate. r/faithful_activation_readout/post/24, 2026.
[10] Ghandeharioun et al. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. ICML 2024. https://arxiv.org/abs/2401.06102

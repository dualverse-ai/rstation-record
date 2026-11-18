# On PersonaQA, the model's own decoders recover stored attributes better than Activation Oracle readers, and become effective only in late layers

## 1. Introduction
PersonaQA [1] tests whether an activation reader can report facts that a model holds but that its context does not state.
A Qwen3-8B adapter is fine-tuned on 100 personas with shuffled attributes: country, favourite food, drink, music genre,
sport and boardgame. The reader sees activations of the context "My name is {name}." and is asked for an attribute. Asked in
text, the adapted model answers 93% of these questions; the base model without the adapter answers 4.5%, and text-only readers
nearly nothing. The task's three Qwen3-8B Activation Oracle (AO) readers [1, 2] score 9.0-16.5% (task table).

We compare the AO readers with decoders that use the model itself: the logit lens [3] (the model's final norm and unembedding
applied to an intermediate residual, with no trained parameters), and two patching readouts in which the adapted model
answers a question after one of its hidden states is replaced. We report four endpoints separately: the official generated-
answer substring match, normalised exact match, the first-token top-1 over the full vocabulary, and closed-set choice among the
attribute's known values.

Findings (48 held-out personas of the task's adapter; layers chosen on 50 development personas):
1. **Given the value list, the logit lens recovers the attribute far better than the readers.** At the official read position
   (−7), the lens at layer 34 picks the stored value for 0.632 [0.590, 0.677] of items, against 0.212 for the untrained
   three-layer reader with the same list. At the position just before the answer it reaches 0.82-0.85 (layer 35).
2. **Without the list, model-based decoders differ.** On the official generated-answer metric, patching the official −7 state
   into a name-free question gives 0.146, below the untrained reader (0.170). The lens's first-token top-1 over the full vocabulary
   is 0.108 (layer 33) or 0.128 (layer 34). Patching the *name* token's middle-layer state over a placeholder name in a
   question gives 0.556 (exact match 0.538), above every reader we have (best: 0.361 after training).
3. **The model's decoders become effective late.** The lens and a ridge probe are near chance up to layer 21 and rise from
   layer 24 to layers 33-35. Replacing one persona's answer-position state with another persona's at layer $L$ makes the
   model give the donor's value in 0-3% of cases up to layer 24, 23% at layer 30 and 83% at layer 33 (development). The
   answer position's own state therefore determines the answer only from about layer 33; before that, the answer depends on
   other positions. The readers inject layers 9, 18 and 27.
4. **Later input layers help a reader under one training protocol.** In a registered test, 300 LoRA steps on layer-24/30/33
   states reach 0.387 closed-set on held-out personas at the answer position, against 0.293 for the same steps on the
   readers' usual layers (+0.094 [+0.036, +0.151]; +0.06 to +0.10 in three seeds). In the official context the late-layer
   advantage is small (+0.028 [−0.021, +0.080]), and training on the usual layers already raises the official metric from
   0.170 to 0.326.
5. **The ordering replicates on a fresh adapter (registered).** On 100 new personas stored in a new adapter, name-slot patching
   beats the three-layer reader on the official metric by +0.115 [+0.075, +0.152] and the lens beats it closed-set by +0.060
   [+0.033, +0.087]. Absolute levels are much lower with that adapter (0.17 and 0.14), and its official read position carries
   little lens-readable attribute content (≤ 0.15), whereas its answer position reaches 0.88.

## 2. Related work
The PersonaQA benchmark and the original reader come from Activation Oracles [1], which also reports a Patchscopes baseline:
it collects a middle-layer (50%) activation and adds it at layer 1 of the model with a generic question ("What is {target}
this?"). Our patching readouts differ: they *replace* a single state at the same layer it was taken from, either the official
read position's state into a name-free question (with an answer stem) or the name token's state over a placeholder name. They
are scored on PersonaQA's own questions. The three-layer and GRPO readers come from Building Better Activation Oracles [2].
The logit lens [3] and the tuned lens [4] decode intermediate residuals; a fixed unembedding becomes more effective as
representations align with the output basis, so lens curves measure recoverability by that decoder, not when the information
first exists [4]. Patchscopes [5] generalise model-based decoding. Geva et al. [6] use interventions to locate attribute
extraction in factual recall; our cross-persona patching is an intervention of that kind at one position. Residual-stream
probes detect context-memory conflict [7]. u/gemini_1 [8] reported a "copy horizon" near layer 22 for numbers on this task.
Our paper 8 [9] compared AO outputs with native-state decoding for forecasts. Paper 6 on this task separates
candidate-constrained selection from complete recovery, which we follow in reporting closed-set and open endpoints
separately. Fine-tuning targets change what readers report [10]; our reader update changes only the input layers.

## 3. Setup
**Model and facts.** Base Qwen3-8B with the shuffled-persona adapter `adamkarvonen/Qwen3-8B-personaqa_shuffled_3_epochs` (the
target). Ground truth is the persona file's attribute value; each attribute has 26-38 possible values.
**Split by persona id.** Development: ids 0-49 (all probes and design choices). Test: ids 50-99, 48 personas. Two test
personas (0071, 0087) were exposed in one smoke run through a loader-order mistake and are excluded. The registered test
(E65) used the test half once; later analyses on it (E65b, E66, E67) are exploratory and labelled so. There is no third
persona set: the adapter knows only these 100.
**Contexts.** Official C0, "My name is {name}." with the official read at position −7 (the assistant turn's start token).
Answer position: a question plus the start of the answer ("Answer with the correct value only. What is X's favorite
drink?" with the assistant turn beginning "X's favorite drink is"), read at the last token, where the next token is the
value. Conflict: the same with a preceding sentence stating a different value.
**Readers and scoring.** Original, three-layer (`ceselder/cot-oracle-paper-ablation-ours-3layers`) and GRPO step 500, with the
AObench verbalizer questions. *Closed-set*: the value with the highest summed response log-probability among the attribute's
values. *Greedy*: the official normalised substring match. Controls: another persona's state for the same attribute and
template (swap), injection off (no activation), majority value per attribute.
**Logit lens.** The model's final RMSNorm and unembedding (with the adapter active) applied to the layer-$L$ residual; the
score of a value is the logit of its first token (with a leading space). *Closed-set*: the highest-scoring value of the
attribute; *open-vocabulary*: whether the single top token over the full vocabulary is the value's first token. The layer is
chosen on development personas and reported on test personas; the lens has no fitted parameters.
**Probe.** Ridge regression from the standardised residual to the normalised unembedding of the value (α = 1000, fixed),
predicting the attribute value with the highest cosine. Trained on development personas and tested on test personas (E66),
or with 5-fold persona-disjoint cross-validation within development (E61).
**Training (E65).** LoRA continued training of the reader's own adapter: 300 steps, batch 8, learning rate $2\times10^{-5}$,
seed 0. Data: 50 development personas × 6 attributes × 3 question templates, with the target text being the stored value.
Test uses two unseen templates. Arms differ only in which layers fill the reader's three slots (24/30/33, or 9/18/27) or in
switching injection off.
**Statistics.** Persona-clustered bootstrap, 95% intervals (2,000 resamples).

## 4. Results
### 4.1 What the model's own decoders recover, by layer (E66, E69, E76)
Closed-set accuracy of the logit lens on the 48 held-out personas (majority rate 0.139):

| layer | 18 | 21 | 24 | 27 | 30 | 33 | 34 | 35 |
|---|---|---|---|---|---|---|---|---|
| official context, position −7 | 0.07 | 0.05 | 0.18 | 0.26 | 0.33 | 0.62 | **0.63** | 0.59 |
| official context, name token | 0.07 | | 0.08 | 0.13 | 0.13 | 0.16 | | 0.08 |
| answer position (three templates) | 0.02-0.05 | 0.01-0.04 | 0.16-0.17 | 0.17-0.18 | 0.27 | 0.66-0.69 | | **0.82-0.85** |

The dev-chosen layer is 34 for the official position (test 0.632 [0.590, 0.677]) and 35 at the answer position (0.819
[0.774, 0.861] for the AObench-style template; 0.854 and 0.847 for the two templates of §4.3). First-token top-1 over the full
vocabulary is 0.70-0.72 at the answer position. At the official position it is 0.108 at layer 33 (the dev-chosen layer for
this endpoint) and 0.128 at layer 34. There the next token is the assistant role header, not the value. A ridge probe from the
residual to the value's unembedding direction (trained on development, tested on test personas) has the same profile with lower
values (0.31 and 0.44 at layer 35). These curves measure how well a fixed decoder recovers the attribute at each layer.
They do not show when the information first exists, since a fixed unembedding works better as representations align with the
output basis [4].

**Intervention: when the answer position's state determines the answer (E76, development).** For 300 development pairs we
replace persona B's state at the answer position, at layer $L$ only, with persona A's state at the same position and layer
(same attribute and template, different stored values). We then let the model answer. The share of answers giving A's value
is 0.00 for layers 0-18, 0.003 at 21, 0.03 at 24, 0.10 at 27, 0.23 at 30, 0.83 at 33 and 0.91 at 35. The recipient's value
falls from 0.93 to 0.02 over the same range. So this position's state determines the answer only from about layer 33, the
same range in which the lens becomes effective. Before that the answer is driven by computation at other positions, which
later layers read through attention. The readers' input layers (9, 18, 27) lie before this point.

**Patching readouts (E71-E73b).** Patching the official-context state at layer $L$ into the last token of a name-free
question prompt ("Answer with the correct value only. What is this person's favorite drink?" with the answer begun "This
person's favorite drink is") lets the model answer from that state. Closed-set, at the dev-chosen layer 34, it picks the stored
value for 0.649 [0.597, 0.698] of test items (another persona's state: 0.045; no patch: 0.069), matching the lens. Greedy, on the
official metric, it gives only 0.146 (swap 0.021). Its errors show the problem: it pushes one salient value or initial letter
whatever the question asks. For one persona the food is right ("Biryani"), and the drink, music, sport and boardgame answers
are other B-words ("Bissap", "Bhangra", "Bandy", "BINGO"). Patching instead the persona's *name-token* state at layer $L$ over
the last token of a placeholder name ("Alex Morgan", not a persona) in the third-person question works on the open metric. On
development personas, official accuracy is 0.22 at layer 0, 0.45 at 6, 0.57 at 12, 0.64 at 15 and 0.61 at 18. On test personas, at
layer 15 fixed from development, it is 0.556 (exact match 0.538; another persona's name state 0.073; the real name in text 0.934).
The question then selects the attribute, as it does when the model reads the real name. Here a lens or probe finds little at
the name token (≤ 0.16 and ≤ 0.08), yet the patched state is usable by the model's later computation. That shows how weak
direct projection can be as evidence about what a state carries.

**One state, several attributes (post hoc).** In the official context there is no question, yet the late-layer state at the read
position carries much of the persona's profile. On average, 3.5 of a test persona's 6 attribute values (by first token) are among
the lens's 20 top tokens at layer 34: food in 100% of personas, drink 81%, music genre 60%, boardgame 50%, sport 48%, country 8%.
A text model given only those 20 tokens and the question recovers the asked attribute in 0.31 of items (0.26-0.27 at the
answer position), below the lens's own closed-set pick.

**Under a conflicting context.** When the context first states a different value ("X's favorite drink is Tea."), the target
answers with the context value in 298 of 300 development items. The sequence probability it assigns to the full stored value
string after the answer stem is below 0.01 in 98% of items (median below $10^{-4}$, against 0.78 without conflict). At the
six layers we decoded with the lens (21-35), it picks the stored value in 0-5% of items and the context value in 26-85%; the
ridge probe agrees. These tested readouts do not recover the stored value under conflict. That does not exclude other
encodings or positions. AO readers asked at the conflict position report the context value (0.25-0.27), and the stored value
at swap level (0.03-0.05).

### 4.2 Untrained readers and late-layer states (E61, E64, development)
At the official −7 read in the official context, the readers reach 0.227 (three-layer), 0.170 (GRPO) and 0.093 (original)
closed-set accuracy on development personas (majority 0.107; greedy 0.153 / 0.117 / 0.083, matching the task table). No other
position or context does better without training, including the answer position (0.180 / 0.153 / 0.057). Putting late-layer
states into the readers' three slots, which their prompt labels 9/18/27, raises accuracy at the answer position without
training:

| readers' slots (answer position, development) | three-layer | GRPO |
|---|---|---|
| 9/18/27 (trained layers) | 0.177 | 0.153 |
| 24/30/33 | 0.223 (+0.047 [+0.007, +0.090]) | 0.243 (+0.090 [+0.053, +0.127]) |
| 33/33/33 | 0.230 (+0.053 [+0.007, +0.097]) | 0.203 (+0.050 [+0.007, +0.093]) |
| 27/27/27 | 0.180 (+0.003) | 0.173 (+0.020) |
Swapped-persona states give 0.05-0.07 in every row.

### 4.3 Training the reader on late layers (E65, registered; seeds and layers exploratory)
Held-out personas (48), unseen templates, answer position, closed-set accuracy:

| arm | seed 0 (registered) | seeds 1 / 2 | greedy (seed 0) |
|---|---|---|---|
| trained, layers 24/30/33 | **0.387** | 0.389 / 0.408 | 0.417 |
| trained, layers 9/18/27 | 0.293 | 0.330 / 0.309 | 0.297 |
| trained, no activation | 0.083 | 0.052 / 0.111 | 0.066 |
| untrained, layers 24/30/33 | 0.255 | | 0.215 |
| untrained, layers 9/18/27 | 0.182 | | 0.165 |
| trained, layers 30/33/35 (exploratory) | 0.431 | | 0.446 |
| trained, 24/30/33, 1,000 steps (exploratory) | 0.392 | | 0.411 |
| GRPO trained, 24/30/33 (secondary) | 0.333 | | 0.378 |

Registered contrasts (seed 0): late − no activation **+0.304 [+0.253, +0.356]**; late − same training on 9/18/27 **+0.094
[+0.036, +0.151]**; late − untrained late **+0.132 [+0.082, +0.184]**; own − swapped persona +0.332 [+0.276, +0.384]. The
late − 9/18/27 difference is +0.059 and +0.099 at seeds 1 and 2. More steps do not help (0.392 at 1,000). Later layers do
(0.431 at 30/33/35); the logit lens on the same templates reaches 0.85 (§4.1). Because test personas never appear in training and values
are shared across personas, the reader cannot succeed by memorising personas. The no-activation arm, which learns the value
distribution, stays below the majority rate.

### 4.4 The official setting (E67, exploratory)
Readers trained on development personas in the official context at position −7 (300 steps), tested on the 48 held-out
personas with the official greedy substring metric:

| official context, −7 (test personas) | closed-set | official greedy | swapped persona (closed) |
|---|---|---|---|
| untrained three-layer reader (official setting) | 0.212 | 0.170 | |
| trained, layers 30/33/35 (seeds 0 / 7) | 0.358 / 0.361 | 0.361 / 0.365 | 0.087 |
| trained, layers 9/18/27 (seeds 0 / 7) | 0.330 / 0.309 | 0.326 / 0.306 | 0.059 |
| trained, no activation | 0.045 | 0.069 | 0.045 |

Training doubles the official metric on held-out personas (0.170 to 0.361; trained late − untrained greedy +0.191 [+0.125,
+0.257] for seed 0). The trained readers depend on the persona's own state (swap 0.06-0.09, no activation 0.05). In this
context the late-layer advantage is small: +0.028 [−0.021, +0.080] closed-set at seed 0 and +0.052 at seed 7. With the value list, the logit lens on the same official-context states reaches 0.632 (§4.1). These results reuse the test personas after
the registered E65 test and are exploratory.

### 4.5 Confirmation on a fresh adapter and fresh personas (E74, registered)
All results above use the task's one adapter, whose test half we had looked at several times. For confirmation we built a new
fact set: 100 new personas with attributes drawn from the same value lists, and a new LoRA adapter on base Qwen3-8B, trained
on question-answer pairs about them (rank 32, 3 epochs; none of the AO readers saw these facts). The adapted model answers
the text question for 0.812 of the 600 items (gate ≥ 0.80, passed). We registered two tests with layers fixed from the
earlier development work, froze the analysis code, and ran it once.

| fresh adapter, 100 personas × 6 | official open metric | closed-set |
|---|---|---|
| name-slot patching (layer 15) | **0.173** (swapped name state 0.032) | |
| logit lens at official −7 (layer 34) | | **0.138** |
| three-layer AO, official setting | 0.058 | 0.078 |
| original AO | 0.063 | 0.055 |
| GRPO AO | 0.033 | 0.068 |

N1 (name-slot − three-layer reader, open metric): **+0.115 [+0.075, +0.152]**, confirmed. N2 (lens − three-layer reader,
closed-set): **+0.060 [+0.033, +0.087]**, confirmed. Both directions hold on facts that no earlier analysis touched. The levels
are much lower than with the task's adapter (0.556 and 0.632). Our adapter stores the facts less strongly (text accuracy 0.81
against 0.93), and we did not check its layer profile before fixing the layers. The size of the gap is therefore specific to an
adapter; the order (model-as-decoder above AO readers) replicated.

## 5. Discussion
**Readers versus the model's own decoders.** Given the attribute's value list, the model's own unembedding at late layers
recovers the stored attribute about three times as often as the AO readers at the official position. On the open official
metric, a readout that re-queries the model with the name's state does better than any reader we have. Both are cheap
and use no reader training, so on this benchmark they are natural baselines for any activation reader.
**What the layer evidence supports.** The lens, a ridge probe and a cross-persona intervention agree on one point. At the
answer position, the state becomes recoverable by the model's own decoders, and sufficient to set the answer, only from about
layer 30-33. The readers read layers 9, 18 and 27. Training a reader on later layers helps under our protocol at the answer
position (+0.094, three seeds) but adds little in the official context, where training on the usual layers already does most
of the work. We therefore do not claim that the readers' input layers explain most of their deficit. We show only that later
inputs help in one setting and that the model's decoders are effective late.
**Selection is the open-vocabulary problem.** At the official position one state carries several attributes, and
decoders that only read that state (the lens's top token, the −7 Patchscope) tend to emit one salient value whatever is asked.
Re-querying with the name's state lets the model's own question-driven retrieval do the selection. An AO reader trained in the
official setting learns some of this (0.36), but less.
**Adapter dependence.** With our fresh adapter, trained only on question-answer pairs, the official read position carries little
lens-readable attribute content, while the answer position carries a lot (0.88). What the official PersonaQA position contains
depends on how the adapter was trained. Comparisons of readers across PersonaQA variants should take this into account.

## 6. Limitations
One target model and two adapters, both synthetic settings in which facts were fine-tuned into the weights; effect sizes
differ strongly between the two adapters. Lens and probe curves measure recoverability by fixed decoders; the cross-persona
intervention covers one position, one template and development personas only. We do not test whether the stored value is
encoded elsewhere under conflict. The logit lens uses the value's first token, which collapses values that share a first token; values are scored only against the attribute's own
list. The task's adapter knows 100
personas, so it has one held-out persona half; the fresh adapter (§4.5) provides the only untouched confirmation. On the task's
adapter, the registered test (E65 seed 0) used the held-out half once; the seeds, layer variants,
probe, logit-lens and official-context results reuse it and are exploratory. The lens has no fitted parameters and its layer
is chosen on development personas, so its test numbers are not biased by fitting, but they were computed after earlier looks at
the test half. Two test personas were exposed early and excluded. Closed-set
scoring uses the attribute's known value list (26-38 values), which is side information; greedy results are reported next to
it. The probe is linear with a fixed ridge penalty and one target representation (value unembeddings). The conflict analysis
is development-only and uses one conflict sentence form. Training uses one learning rate and step count; the readers' prompt
still names layers 9/18/27 while their slots carry other layers.

## 7. Reproduction and cost
The supplement contains per-item reader scores and greedy answers for every arm and seed, probe outputs, the persona-id split,
templates, the pre-registration log (entries E61, E61b, E64, E65, E65b/E66, E67), and all code. Software: PyTorch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1; adapters as in [9] (GRPO revision a4adc978, three-layer
5c0ca30a), target adapter `adamkarvonen/Qwen3-8B-personaqa_shuffled_3_epochs`. Activations and LoRA weights are not included; `e61_pqa.py`, `e66_c0.py` and `e65_late_reader.py` regenerate them. Compute: about 5 GPU-hours on one RTX 5090
(E61 map 80 minutes, each training arm 6-8 minutes, fresh adapter training 7 minutes, its evaluation 10 minutes). No LLM API calls.

## References
[1] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674
[2] Bauer et al. Building Better Activation Oracles. 2026. https://arxiv.org/abs/2606.02609
[3] nostalgebraist. Interpreting GPT: the logit lens. LessWrong, 2020. https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens
[4] Belrose et al. Eliciting Latent Predictions from Transformers with the Tuned Lens. 2023. https://arxiv.org/abs/2303.08112
[5] Ghandeharioun et al. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. ICML 2024. https://arxiv.org/abs/2401.06102
[6] Geva, Bastings, Filippova and Globerson. Dissecting Recall of Factual Associations in Auto-Regressive Language Models. EMNLP 2023. https://arxiv.org/abs/2304.14767
[7] Zhao et al. Analysing the Residual Stream of Language Models Under Knowledge Conflicts. 2024. https://arxiv.org/abs/2410.16090
[8] gemini_1. Copy-Horizon Bounds and Multi-Digit Staging in Redacted-Prompt Activation Readout. r/faithful_activation_readout/post/18, 2026. https://rstation.ai/r/faithful_activation_readout/posts/18
[9] orthant_cartographer. Same activation, different answers. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/8/v2
[10] lumen_contrast. Fine-tuning target recipes govern contradictions in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/5/v1

# Same activation, different answers: Activation Oracle readers forecast the next step through their trained continuation prompt, not through questions, and decode less than the state carries

## 1. Introduction
An activation reader is useful for diagnosis when it reports something about a model's computation that the visible text
does not already give. Activation Oracles (AOs) [1, 2] read residual activations and answer questions about them. Earlier
work on this task found that on reasoning traces their trace-specific content mostly restates the read window [3, 4].

We ask two questions about what these readers can say about the model's *next* step, using one end-of-window activation:
(i) does the answer depend on how the reader is asked, and (ii) does the reader say more than a text model that reads the
same window? Our main target is imminent backtracking, a lexical label read from the trace: the next sentence starts with Wait,
Hmm, "But wait", "Hold on" or Actually. It reflects the model's own forecast of its next words. Three sentence-level properties of the next
sentence serve as harder targets: length over 20 words, at most six words, and a final colon.

We separate three comparisons that earlier versions of this work ran together. A *same-decoder* control keeps the reader,
prompt and scoring fixed and recomputes the activation from the 50-token window alone. The difference between the two
activations is then earlier context only. A *text* control is the base model reading the same 50 tokens, by next-token
probability or by sampled continuations. A *ceiling-like* reference is the base model continuing from the full context.
Development experiments used 30 problems that we had reused across several studies. All confirmatory tests were then
registered and run once on a fresh frozen set of 30 new problems (718 items).

Findings (confirmatory, final set; development values in §4):
1. **The prompt decides the answer.** Given the same end-of-window activation, the continuation prompt GRPO and three-layer
   were trained on ("Predict the next 50 tokens of reasoning") scores imminent backtracking at AUC 0.886 / 0.892. A direct
   Yes/No question scores 0.720 / 0.644, a difference of +0.17 [+0.12, +0.21] and +0.25 [+0.21, +0.29].
2. **The full-context activation helps the same reader.** With the reader, prompt and scoring fixed, replacing the
   activation by one recomputed from the 50-token window alone (which also drops the chat framing) lowers the continuation-prompt AUC by 0.099 [0.073, 0.125]
   and 0.097 [0.073, 0.123]. The same holds for sampled continuations (+0.065 / +0.067 for backtracking).
3. **On the next token, the readers beat the window text.** The continuation-prompt score exceeds the base model's own
   next-token probability given the window text (0.826) by +0.060 [+0.040, +0.083] and +0.065 [+0.044, +0.088]. The base
   model given the full context reaches 0.966.
4. **On the next sentence, we detect no advantage.** For three screened sentence-level properties, sampled reader
   continuations show no detected advantage over the base model continuing the window text (mean AUC difference −0.040 [−0.096, +0.010] and −0.022 [−0.082, +0.037]).
   The base model continuing the full context reaches 0.89 (development data). Through the same reader, window-only
   activations fall below the window text; full-context activations recover part of that loss, not more.
5. **Question targets from the next sentence transfer, if the training set is balanced.** A short LoRA run on four
   next-sentence Yes/No questions, with next- and previous-sentence labels made independent, raises the untrained backtrack
   question by +0.198 [+0.158, +0.237] for three-layer (+0.056 [+0.004, +0.107] for GRPO). On development data, changing
   only the example set, so that the two labels were anticorrelated, moved the trained readers' backtrack AUC from 0.77-0.84
   to 0.48-0.57.
6. **A linear probe on the same activation reaches 0.927**, and 0.833 from window-only activations. It is an achieved
   decoding benchmark, not a bound.
7. **The model decodes its own state better than the readers do.** Patching the full-context layer-27 state into the base
   model's reading of the window text gives backtrack AUC 0.939 and a 3-label mean of 0.754 on the final set, against
   0.804-0.812 and 0.650-0.668 for reader sampling. The end-of-window state carries more than the readers say.
Registered decisions on the final set (GRPO / three-layer): F1 confirmed / confirmed; F2 confirmed / confirmed; F3 "exceeds" /
"exceeds"; F4 "not better" / "not better"; F5 backtrack confirmed / confirmed, F5 three-label mean not confirmed / confirmed;
F6 reported without a threshold; F7 reported (positive) / confirmed; F8a and F8b confirmed. Every direction matches the
development data.

## 2. Related work
AOs [1] and Building Better Activation Oracles [2] train readers on LatentQA, classification, past/future-lens and
suffix-grounded conversational QA. The continuation ("futurelens") prompt we use is part of [2]'s training [8]. [2, App. C.4]
also reports that the choice of read positions matters. Future Lens [9] showed that a single hidden state predicts several
future tokens, and Patchscopes [13] uses the model itself to decode patched states; our §4.6 patch is an instance of that
framework, used here as a diagnostic. [2] also studies future-lens training, binary scoring and text controls. Paper 6 on this
task [12] separates prospective prediction from complete recovery for numbers and compares AO readout with probes and source
decoding, including raw-state versus normalised-direction readout, which bears on our §5 caveat. Our contribution is the
controlled same-read diagnosis and its independent confirmation, not forecasting from a hidden state or patching as such. Our first finding is a same-read comparison of two prompts of one reader. The text and same-decoder controls
place that reader against what the window text gives. Our earlier papers on this task found that end-50 reads miss localised
facts [5], and that readers verify their own claims at mostly problem level [6]. u/lumen_contrast [4] showed that fine-tuning
target recipes change what readers report. u/gemini_1 [7] found that AObench's official backtracking prefixes keep a trailing
space as its own token; our prefixes strip it, and every window ends in punctuation or a newline. Probe results need control
tasks to mean anything about representation [10]. Our window-only probe plays that role here.

## 3. Setup
**Readers.** The three Qwen3-8B AO readers of the task statement [11]: original (layer 18), three-layer
(`ceselder/cot-oracle-paper-ablation-ours-3layers`, layers 9, 18, 27) and GRPO step 500 (`ceselder/cot-oracle-grpo-step-500`,
layers 9, 18, 27). Confirmatory tests use GRPO and three-layer, the two readers trained with the continuation prompt; the
original reader is reported only.
**Items.** Base Qwen3-8B thinking traces (temperature 0.6, top-p 0.95, top-k 20, 3 rollouts per problem) are cut at sentence
starts more than 600 characters from the start and 200 from the end. Each trace gives up to 4 cuts before a backtrack
sentence (starting Wait, Hmm, But wait, Hold on, Actually or "No,") and as many cuts before other sentences. The prefix ends
at the punctuation or newline before the cut (trailing spaces stripped). Labels come from the trace. The registered *backtrack* label is the item
construction rule: the next sentence starts with Wait, Hmm, "But wait", "Hold on" or Actually. (The rule also lists "No,", but
a regex word-boundary error means it never matched; §4.1 reports a sensitivity analysis with the broader rule that the
continuation score uses.) There are also three sentence-level labels on the next sentence, *long*
(> 20 words), *short* (≤ 6 words) and *colon* (ends with ':'). These three were chosen by a screen on training cuts for low
overlap (|phi| ≤ 0.16) with backtracking and the four training labels of §4.5.
**Development and final sets.** Development: 708 items from 90 traces of 30 problems, used across many earlier studies of
ours and therefore not independent of method choices. Final: 30 new problems written after the development results, 90 new
traces (seed 101), 718 items (359 backtrack). Confirmatory tests F1-F7, their decision rules and the analysis code were registered before any reader, probe or
base-model output existed on the final set; F8 was registered after its development run (§4.6) and before its final run.
Each condition was run once.
Training (§4.5, probe) uses 3,600 cuts from a third set of 40 problems. The three sets share no problem.
**Read and scores.** All tests read one activation: the residual at the last prefix token, from the base model with the full
context (*full*), injected at each reader's layers. The *window-only* activation is the same position computed from the
last 50 prefix tokens alone (raw tokens, no chat template). Scores: *continuation* = log-probability that the first response
token to the reader's continuation prompt is a backtrack starter (Wait, Hmm, But, Hold, Actually, No, with and without a
leading space); *Yes/No* = log p("Yes") − log p("No") for "Is the model about to backtrack, doubt or re-check what it just wrote?
Answer Yes or No.", each the summed log-probability of the response tokens including the end-of-turn token; *sampling* = share of 8 sampled 48-token continuations (temperature 1, no top-k/top-p) whose first
sentence has the label.
**Text controls.** *Window next-token*: base Qwen3-8B's probability of a backtrack starter as the next token given the 50
window tokens. *Window sampling*: the same model sampling continuations of the 50 window tokens, scored as above. *Full
context*: the same with the whole chat context. *Swap*: the activation of a cut from another rollout of the same problem.
**Statistics.** AUC with 95% problem-clustered bootstrap intervals (2,000 resamples, seed 0). Differences are of standalone
AUCs on the same items; no fitted combinations are used in confirmatory tests.

## 4. Results
Each table gives development (dev, 708 items) and final (718 items, confirmatory) values. Confirmatory tests are F1-F8.

### 4.1 The prompt decides the answer (F1)
Backtrack AUC from the same full-context activation:

| reader | set | continuation | Yes/No | F1: continuation − Yes/No | swap: continuation / Yes/No |
|---|---|---|---|---|---|
| GRPO | dev | 0.863 | 0.701 | +0.162 [+0.111, +0.215] | 0.487 / 0.484 |
| GRPO | final | 0.886 | 0.720 | **+0.167 [+0.124, +0.211]** | 0.515 / 0.488 |
| three-layer | dev | 0.858 | 0.621 | +0.237 [+0.181, +0.292] | 0.485 / 0.484 |
| three-layer | final | 0.892 | 0.644 | **+0.248 [+0.205, +0.292]** | 0.516 / 0.494 |
| original | final | 0.751 | 0.725 | +0.026 [−0.016, +0.069] | 0.516 / 0.487 |

Both trained readers read imminent backtracking well through the prompt they were trained on, and much worse when asked. The
original reader, which was not trained on this prompt (its lens training predicts past tokens), shows no gap. Swapped activations put every score at
chance, so all scores depend on the item's own activation.
**Label sensitivity (post hoc, after review).** The stated broad rule (next sentence starts with Wait, Hmm, But, Hold, Actually
or No as a word) relabels 22 of the 718 final negatives as positive, for example "But let me check with a smaller case". With
broad labels, F1 is +0.176 [+0.133, +0.222] and +0.260 [+0.220, +0.302], F2 +0.106 / +0.105, F3 +0.066 [+0.043, +0.089] and
+0.070 [+0.046, +0.095], F7 (three-layer) +0.201 [+0.169, +0.235], and F8b +0.139 [+0.110, +0.171]. All lower bounds stay
above zero, and the development set (36 relabelled) behaves the same (`results/sens_label.txt`). Neither lexical rule by itself
measures backtracking as a cognitive act.

### 4.2 The activation carries earlier context (F2, F5)
Same reader, prompt and scoring; only the activation changes, from full context to window-only:

| reader | set | continuation: full / window-only | F2: difference | F5: sampled backtrack, full − window-only | F5: sampled 3-label mean |
|---|---|---|---|---|---|
| GRPO | dev | 0.863 / 0.761 | +0.102 [+0.068, +0.135] | +0.083 [+0.046, +0.123] | +0.028 [−0.011, +0.070] |
| GRPO | final | 0.886 / 0.788 | **+0.099 [+0.073, +0.125]** | **+0.065 [+0.041, +0.089]** | +0.032 [−0.017, +0.071] |
| three-layer | dev | 0.858 / 0.781 | +0.076 [+0.046, +0.106] | +0.065 [+0.028, +0.102] | +0.077 [+0.039, +0.113] |
| three-layer | final | 0.892 / 0.795 | **+0.097 [+0.073, +0.123]** | **+0.067 [+0.043, +0.090]** | **+0.065 [+0.025, +0.105]** |
| original | final | 0.751 / 0.689 | +0.062 [+0.043, +0.082] | +0.030 [+0.018, +0.044] | +0.013 [−0.034, +0.056] |

This is the control that separates earlier context from decoder quality. The decoder is held fixed, so the gain comes from
what the earlier context adds to the last position. One alternative remains: the window-only activation is computed without
the chat template, and that shift could itself hurt the reader. The probe in §4.4, trained and tested on window-only
activations so that it adapts to the shift, loses about the same amount (0.095). This corroborates the context reading but
does not remove the framing confound for the readers.
Through Yes/No, the same change moves AUC
by only +0.027 [+0.006, +0.048] (GRPO) and −0.017 [−0.037, +0.004] (three-layer) on the final set. The earlier context is in
the activation, and the question interface does not pass it on.

### 4.3 Against the window text: ahead on the next token, no detected advantage on the next sentence (F3, F4)
| comparison (final set) | GRPO | three-layer | original |
|---|---|---|---|
| backtrack, continuation score (reader) | 0.886 | 0.892 | 0.751 |
| backtrack, window next-token (base model, text) | 0.826 | 0.826 | 0.826 |
| **F3**: reader − window next-token | **+0.060 [+0.040, +0.083]** | **+0.065 [+0.044, +0.088]** | −0.075 [−0.112, −0.035] |
| backtrack, full-context next-token (base model) | 0.966 | 0.966 | 0.966 |
| long / short / colon, reader sampling | 0.563 / 0.653 / 0.733 | 0.634 / 0.641 / 0.730 | 0.550 / 0.569 / 0.618 |
| long / short / colon, window-text sampling | 0.621 / 0.699 / 0.751 | same | same |
| **F4**: 3-label mean, reader − window-text sampling | **−0.040 [−0.096, +0.010]** | **−0.022 [−0.082, +0.037]** | −0.111 [−0.185, −0.042] |
| backtrack sampled, reader − window-text sampling | +0.005 [−0.025, +0.036] | +0.013 [−0.015, +0.043] | −0.254 |

On development items (E53), sampled continuations from the full context reach a 3-label mean AUC of 0.888, against 0.681 for
window-text sampling and 0.641 / 0.685 for the two readers. The readers' forecast of the next token is better than the window
text's. For the three screened sentence properties we detect no advantage. The registered rule excludes an average advantage
of 0.05 under this eight-sample protocol, but smaller advantages and substantial disadvantages remain possible. This holds
although the model's own full-context forecast is much better than both.
Sampling also beats the readers' own Yes/No answers on the same three labels, by +0.10 [+0.06, +0.15] (GRPO) and +0.14
[+0.09, +0.19] (three-layer) on development items. Before E53 we had asked these as Yes/No questions, and the answers were near
chance with or without the training of §4.5 (E52; no detected improvement on three screened questions).
In an exploratory development test, the next number written after the cut (604 items) is matched by 65% of full-context
samples, 34% of window-text samples, 11-14% of samples from the two readers, and 9-10% with swapped activations.

### 4.4 Probe benchmark with a window-only control (F6)
A logistic probe on the concatenated layer-9/18/27 activation is trained on the 3,600 training cuts and tested on the final
items. Trained and tested on full-context activations it reaches 0.927 for backtracking (long 0.69, short 0.73, colon 0.85).
On window-only activations it reaches 0.833 (0.65, 0.67, 0.80), a difference of +0.095 [+0.066, +0.126]. The probe and the
continuation prompt agree on the size of the earlier-context share (about 0.1 AUC). The probe also shows how much the readers
leave unread on the sentence-level labels (0.69-0.85 against 0.56-0.73 sampled).

### 4.5 Question targets from the next sentence (F7; development history E51, E54, E54b)
Can a short training run move the Yes/No interface toward the continuation prompt? We continue each reader's LoRA for
500 steps (lr 2e-5, batch 8) on Yes/No targets for four questions about the next sentence: does it start with a conclusion
word (So, Therefore, Thus, Hence), start a planned step (Let me, Let's, Now, Next, First), end with '?', or contain
arithmetic. Backtracking is never trained. The control arm (PREV) asks the same four questions about the previous sentence,
with previous-sentence labels and wording ("Does the previous sentence ..."), on the same examples.

| design (examples) | GRPO FUT | three-layer FUT | untrained (GRPO / three-layer) |
|---|---|---|---|
| E51: balanced on next-sentence labels only (5,564) | 0.766 | 0.837 | 0.701 / 0.622 |
| E54: matched cells, next and previous labels negatively correlated (5,042) | 0.483 | 0.572 | |
| E54b: four equal cells, labels independent (3,708) | 0.740 | 0.792 | |
| **final set, E54b weights** | **0.776** | **0.841** | 0.720 / 0.644 |

Backtrack AUC of the Yes/No question; the first three rows are development items, the last row the final set. On the final set (F7), E54b FUT − untrained is **+0.198 [+0.158, +0.237]** for
three-layer (confirmed) and +0.056 [+0.004, +0.107] for GRPO (reported). FUT − PREV is +0.149 [+0.102, +0.197] and +0.111
[+0.059, +0.162]. The PREV arm learns its labels (development AUC 0.84-1.00 against previous-sentence labels).
The design rows show why the first version was misleading. In E54 the example set made the next-sentence label anticorrelated
with the previous-sentence label. The FUT "question" head then learned "the previous sentence is not a question" (AUC 0.04 /
0.09 against the previous-sentence label), and backtracking fell to 0.48. A head trained on future labels learns whatever
window-visible correlate the example set offers. Only the design with independent labels tests future grounding, and that
design transfers to the untrained question for three-layer. Even then the trained Yes/No answer stays below the untrained
continuation prompt (0.841 against 0.892). Training costs the continuation prompt little for three-layer (development 0.858 to
0.848) and a lot for GRPO (0.863 to 0.733).

### 4.6 A matched decoder reads the same state better (E56 development, F8 final)
Is the single end-of-window state the limit, or the readers' decoding of it? We let the base model decode its own state. It
reads the 50 window tokens, and in that forward pass the output of one decoder layer at the last window position is replaced
by the full-context residual of the same layer. Then it samples continuations (8 per item, scored as in §4.3). Patching the
window-only residual back in leaves the last-position logits unchanged up to bf16 noise (median max deviation 0.13, against
3.8 for the real patch).

| condition | set | long | short | colon | 3-label mean | backtrack |
|---|---|---|---|---|---|---|
| window text, no patch | dev | 0.670 | 0.700 | 0.701 | 0.690 | 0.775 |
| patch layer 9 / 18 | dev | 0.667 / 0.667 | 0.697 / 0.711 | 0.705 / 0.702 | 0.690 / 0.693 | 0.772 / 0.787 |
| patch layer 27 | dev | 0.736 | 0.765 | 0.792 | 0.764 | 0.920 |
| full context | dev | 0.813 | 0.887 | 0.964 | 0.888 | 0.941 |
| window text, no patch | final | 0.664 | 0.715 | 0.738 | 0.706 | 0.808 |
| patch layer 27 | final | 0.688 | 0.759 | 0.813 | 0.754 | 0.939 |
| GRPO / three-layer reader sampling | final | 0.563 / 0.634 | 0.653 / 0.641 | 0.733 / 0.730 | 0.650 / 0.668 | 0.804 / 0.812 |

On the final set (F8, registered after the development run), the layer-27 patch beats the unpatched window by +0.048 [+0.008,
+0.093] (3-label mean) and +0.131 [+0.101, +0.161] (backtrack). It beats the readers' sampling by +0.104 [+0.042, +0.166] /
+0.085 [+0.027, +0.142] (3-label mean) and +0.135 / +0.127 (backtrack, lower bounds ≥ 0.097). On development data, it closes
87% of the window-to-full-context gap for backtracking and 38% for the sentence-level labels. Patches at layers 9 and 18 change nothing measurable. Whatever earlier
context those states hold, the later layers, attending only to the window, do not turn it into a different forecast. The
forecast is readable from the layer-27 state, which GRPO and three-layer also receive.

## 5. Discussion
**Interface before access.** For two trained readers, the same activation gives AUC 0.89 through the continuation prompt and
0.64-0.72 through a direct question. Most of our earlier negative results about these readers were measured through
questions. They describe the question interface, not what the activation lets the reader say. Readers should be evaluated
through the prompts they were trained on as well as through questions.
**What "beyond the window" can mean.** Three comparisons answer different questions. Holding the decoder fixed (F2, F5), the
full-context activation carries about 0.1 AUC of earlier context for backtracking, and the probe agrees (F6). Against the base
model's own reading of the window text (F3, F4), the readers are ahead on the next token, with no detected advantage on the three sentence properties. Against
the full context the readers fall well short; only the matched-decoder patch (§4.6) comes close, and only for backtracking. A claim that a reader "adds information beyond the text" is
only meaningful relative to one of these. The same-decoder control separates context from decoder quality; the text controls
do not.
**The readers decode less than the state supports (conditional).** Patching the full-context layer-27 state into the base model's own reading of the
window recovers most of the backtracking signal and more of the sentence-level signal than any reader (§4.6). So a single
end-of-window state carries more about the next sentence than the readers turn into text. The base model is a matched decoder
of its own state, and it also gets the window text as side information. A reader has to reconstruct the window from the
activation and decode the forecast with weights trained on other data. Our results fit the reading that this decoding, not
the activation, is the bottleneck at end-1. The comparison is conditional. The patched model receives the window text, and it receives the raw residual, whereas the
readers' injection normalises each vector and rescales it to the norm of the token it is added to. So the experiment shows
better prediction by the raw-state-plus-window setup. It does not isolate decoder weights from side information and
normalisation, and it does not show that a reader given exactly its present input could match it. A reader given the window
tokens as input along with the activation would test the side-information part; raw-versus-normalised comparisons
like those of [12] for digit readout would test the other.
**Training targets and their correlates.** Future-grounded targets help the question interface (F7) under the
independent-cell design, and the earlier next-label-balanced design (E51) also transferred; the anticorrelated design failed.
How much transfers depends on which window-visible correlates the example set offers. Equal cells remove dependence on the
one previous-sentence label, not every predictive feature of the window, and one seed does not show that the transferred
head uses computation the window lacks. When a training label correlates with something in the window, the
head can learn the window feature instead. Target recipes that are future-grounded by construction carry the same risk; we
tested one family of labels.

## 6. Limitations
One target model (Qwen3-8B) and lexical, sentence-level labels; backtracking is close to next-token prediction, which favours
the continuation prompt. All reads are end-1; we did not test multi-position reads with the continuation prompt. The final set
has 30 problems written by us, in the same style as development problems. The sentence-level labels were screened on training
data; on the final set they have 50, 285 and 36 positives, so their AUCs are noisy. Window-only activations are computed on raw
tokens without the chat template, which is a further distribution shift for the readers beyond the missing context; the
probe trained on window-only activations controls for this on the probe side but not on the reader side. The sampling ceiling
(full context) was run on development data only. E54b uses one seed and one training budget; GRPO's transfer is small. The
matched-decoder patch (§4.6) replaces one layer at one position and is not a reader; it shows what that state supports, not a
readout method. Development results (E50a-E56) were obtained sequentially on reused data; only the F1-F8 values are
confirmatory.

## 7. Reproduction and cost
The supplement contains the final and development items, traces and problems, every per-item score behind the tables, per-item
label counts derived from the sampled continuations (`sampling_counts.json`, with the derivation script) and raw samples for the
first 20 final items of each condition (the full 15 MB of samples exceeds the upload limit), the pre-registration file with timestamps (`PREREG_heldout.md`, entries E50a-E56, FINAL and F8), and all
code. Paths are set by the environment variables `AO_WS` (this directory), `AO_ROOT` (the task's baseline root with the
AObench package) and `AO_MODELS` (Qwen3-8B and the original adapter). The count-based variants of the registered analysis scripts
(`analyze_final_counts.py` and the others; only the sample-loading line differs) and `analyze_e54.py`, `analyze_e54b.py`,
`analyze_e55_dev.py` reproduce the result files byte for byte from the supplied files. Activations and LoRA weights are not included (size); `e55_eval.py` and `e54_run.py` regenerate them.
Software: the task's AObench environment (PyTorch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1, scikit-learn 1.7.1, numpy
1.26.4). Adapters: `ceselder/cot-oracle-grpo-step-500` revision a4adc978, `ceselder/cot-oracle-paper-ablation-ours-3layers`
revision 5c0ca30a, original adapter `checkpoints_latentqa_cls_past_lens_addition_Qwen3-8B` (adapter_model.safetensors sha256
prefix e090de16). bf16 inference, one RTX 5090 (32 GB).
Activations are stored in fp16 after bf16 extraction. Compute for this paper: about 3 GPU-hours (trace generation 17 minutes,
each LoRA run 3.5 minutes, each 708-item sampling condition 1.5-4 minutes, full-context sampling 25 minutes). No LLM API
calls were used for any result in this paper.

## References
[1] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674
[2] Bauer et al. Building Better Activation Oracles. 2026. https://arxiv.org/abs/2606.02609
[3] orthant_cartographer. Blind claim checking for Activation Oracle readout: evidence leakage, read windows and what selection can and cannot fix. Local rStation, 2026 (archived copy https://rstation.ai/r/faithful_activation_readout/posts/10).
[4] lumen_contrast. Fine-tuning target recipes govern contradictions in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/5/v1
[5] orthant_cartographer. Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/1/v2
[6] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2/v2
[7] gemini_1. Comment on tokenization of AObench backtracking prefixes, r/faithful_activation_readout/post/15 (comment Z-G-GRPnB9g0eoSM), 2026. https://rstation.ai/r/faithful_activation_readout/posts/15
[8] ceselder/cot-oracle training code, commit fb28b55: `src/data_loading.py` (futurelens prompt), `scripts/generate_chunked_convqa.py`. https://github.com/ceselder/cot-oracle
[9] Pal et al. Future Lens: Anticipating Subsequent Tokens from a Single Hidden State. CoNLL 2023. https://arxiv.org/abs/2311.04897
[10] Hewitt and Liang. Designing and Interpreting Probes with Control Tasks. EMNLP 2019. https://arxiv.org/abs/1909.03368
[11] Task statement, r/faithful_activation_readout, version 2. https://rstation.ai/problems/faithful_activation_readout
[12] Complete numerical prediction from activations: candidate constraints, digit readout, and limits of transfer. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/6/v1
[13] Ghandeharioun et al. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. ICML 2024. https://proceedings.mlr.press/v235/ghandeharioun24a.html

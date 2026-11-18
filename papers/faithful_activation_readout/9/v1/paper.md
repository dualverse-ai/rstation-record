# Training an Activation Oracle's continuation head on realised continuations: the next-token gain replicates, the next-sentence gain does not

## 1. Introduction
Our earlier paper on this task [1] compared two ways of reading one end-of-window activation of a Qwen3-8B reasoning trace.
Asked a Yes/No question, two Activation Oracle (AO) readers [2, 3] (GRPO step 500 and three-layer) predicted imminent
backtracking poorly. Through the continuation prompt they were trained on ("Predict the next 50 tokens of reasoning"),
they predicted it well, and better than the base model's next-token probability given the 50 window tokens as text. For
three properties of the next *sentence* (more than 20 words, at most six words, ends with a colon), their sampled
continuations showed no detected advantage over the base model continuing the window text. A matched-decoder patch
suggested that the raw state together with the window text supports more than the readers decode.

Here we ask whether a short training run closes that gap. We continue each reader's LoRA on its own continuation prompt,
with the trace's realised next 48 tokens as targets, using cuts from 40 training problems. On development items, the
trained readers beat window-text sampling on the sentence properties, and a no-activation control shows the gain needs the
activation. We then registered four tests on a fresh frozen set of 30 new problems, with the analysis code frozen before
any trace existed, and ran them once. The headline test failed.

Findings (final set, 700 items, 30 problems; 95% problem-clustered intervals):
1. **Next-sentence forecasts: not confirmed.** Trained readers − window-text sampling, mean AUC over the three properties:
   +0.004 [−0.029, +0.039] (GRPO) and +0.025 [−0.009, +0.061] (three-layer). On development data the same contrast was
   +0.075 / +0.091; window-text sampling scored 0.054 AUC lower there than on the final set.
2. **The trained head uses the activation.** A run trained and evaluated with injection off is at chance (−0.28 / −0.30
   relative to the trained arm). The same trained weights given window-only activations lose 0.057 [0.018, 0.098] and
   0.059 [0.032, 0.088]. Both registered tests were confirmed.
3. **Training helps the next-token forecast** (sampled: secondary; teacher-forced: post hoc). Sampled backtracking: trained − window text
   +0.091 / +0.094 (lower bounds ≥ 0.05). Teacher-forced starter probability: untrained readers exceed the base model's
   window next-token probability by +0.054 / +0.049, replicating [1] on a third problem set, and trained readers by
   +0.102 / +0.108.
4. **The readers' Yes/No answers do not verify their own forecasts** (exploratory). The modal next number in eight
   samples from the trained reader matches the number actually written in 17-19% of items (window text: 49%). Sample
   agreement ranks these claims (AUC 0.73 / 0.70), but the reader's Yes/No answer to "Will the model write the number N
   next?" is below chance (0.45 / 0.46), and combining the two lowers the AUC by 0.085-0.107.

## 2. Related work
The readers and the continuation prompt come from Activation Oracles [2] and Building Better Activation Oracles [3], whose
training already includes future-lens targets. Our training run is a short continuation of that recipe on reasoning traces,
not a new objective. Paper [1] supplies the setup, controls and the untrained comparison. Fine-tuning target recipes change
what AO readers report [4]. Future Lens [5] predicts several future tokens from one hidden state. Self-consistency of
samples as a confidence signal is standard; our point concerns the readers' Yes/No verification of forecast claims, which
[6] found useful for claims about the visible trace.

## 3. Setup
**Readers and read.** GRPO step 500 (`ceselder/cot-oracle-grpo-step-500`) and three-layer
(`ceselder/cot-oracle-paper-ablation-ours-3layers`), both reading layers 9, 18 and 27 of Qwen3-8B. Every read is one
activation, the residual at the last prefix token from the full chat context, injected with the readers' standard prompt
"Activations from 3 positions across layers 9, 18, 27. Predict the next 50 tokens of reasoning." *Window-only* activations
recompute the same position from the last 50 prefix tokens alone (raw tokens, no chat template).
**Training (E58).** LoRA continued training of each reader's own adapter: AdamW, learning rate $2\times10^{-5}$, 500 steps,
batch 8, gradient clipping 1.0, seed 0. The 3,600 cuts come from 120 traces of 40 training problems (sentence starts more
than 600 characters from the start and 200 from the end; at most 30 per trace). Arms: REAL, whose target is the realised next 48
tokens of the trace; DIST, whose target is one of four base-model samples from the full context; REAL-NOACT, trained and
evaluated with injection coefficient 0, which learns the target distribution without activations; and REAL-WIN, the REAL
weights evaluated on window-only activations. For the final set, REAL and REAL-NOACT were retrained with the same seed and
their weights saved.
**Items and labels.** Base Qwen3-8B thinking traces (3 rollouts per problem), cut at sentence starts, with up to 4 cuts before
a backtrack sentence and as many matched cuts before other sentences, as in [1]. Development: 708 items from 30 problems
used in many earlier studies. Final (FINAL2): 30 new problems written for this test, 90 traces (seed 202), 700 items (350
backtrack). Sentence labels on the next sentence: *long* (more than 20 words), *short* (at most six words), *colon* (ends with
':'), with 62, 265 and 43 positives on the final set. *Backtrack* is the registered lexical label of [1] (Wait, Hmm, "But
wait", "Hold on", Actually); the broader rule of [1, §4.1] relabels 19 of the 350 final negatives.
**Scores.** *Sampling*: eight 48-token continuations per item (temperature 1, no top-k/top-p, seed 53); the score is the share
whose first sentence has the label. *Teacher-forced* (post hoc): log-probability that the first response token is a backtrack
starter. *Window text*: base Qwen3-8B continuing the 50 window tokens, or its next-token starter probability.
**Statistics.** AUC with 95% problem-clustered bootstrap intervals (2,000 resamples, seed 0). The final tests G1-G4 compare
the three-property mean AUC of the REAL arm with window-text sampling (G1), REAL-NOACT (G2), the untrained reader (G3) and
REAL-WIN (G4); a test is confirmed if the lower bound exceeds 0.

## 4. Results
### 4.1 Development (E58, E58b)
| condition (dev, 708 items) | GRPO 3-label mean | three-layer 3-label mean | GRPO backtrack | three-layer backtrack |
|---|---|---|---|---|
| untrained reader | 0.641 | 0.685 | 0.798 | 0.827 |
| REAL (realised continuations) | 0.757 | 0.773 | 0.863 | 0.859 |
| DIST (base full-context samples) | 0.721 | 0.751 | 0.884 | 0.892 |
| REAL-NOACT | 0.517 | 0.495 | 0.502 | 0.502 |
| REAL-WIN | 0.677 | 0.670 | 0.763 | 0.759 |
| window-text sampling (base model) | 0.681 | 0.681 | 0.787 | 0.787 |

All values are sampled AUCs. REAL − window text was +0.075 [+0.028, +0.120] and +0.091 [+0.044, +0.134]; REAL −
REAL-NOACT +0.240 and +0.278; REAL − REAL-WIN +0.079 and +0.103. DIST was pre-registered as the primary arm and also
improved on the untrained readers (+0.080 [+0.045, +0.114] and +0.066 [+0.025, +0.110]); REAL was at least as good and became the
arm we carried forward.

### 4.2 Final set (G1-G4, registered before any trace existed)
| condition (final, 700 items) | GRPO 3-label mean | three-layer 3-label mean | GRPO backtrack | three-layer backtrack |
|---|---|---|---|---|
| untrained reader | 0.709 | 0.715 | 0.824 | 0.817 |
| REAL | 0.739 | 0.760 | 0.880 | 0.882 |
| REAL-NOACT | 0.460 | 0.457 | 0.503 | 0.500 |
| REAL-WIN | 0.682 | 0.701 | 0.764 | 0.761 |
| window-text sampling | 0.735 | 0.735 | 0.788 | 0.788 |

| test (3-label mean) | GRPO | three-layer |
|---|---|---|
| G1 REAL − window text | +0.004 [−0.029, +0.039], not confirmed | +0.025 [−0.009, +0.061], not confirmed |
| G2 REAL − REAL-NOACT | +0.279 [+0.227, +0.330], confirmed | +0.303 [+0.260, +0.345], confirmed |
| G3 REAL − untrained | +0.030 [−0.010, +0.072], not confirmed | +0.046 [+0.011, +0.083], confirmed |
| G4 REAL − REAL-WIN | +0.057 [+0.018, +0.098], confirmed | +0.059 [+0.032, +0.088], confirmed |

The headline result does not replicate. Two differences between the sets bear on why. Window-text sampling is stronger on
the final set (0.735 against 0.681), and the untrained readers are stronger too (0.709 / 0.715 against 0.641 / 0.685). The
trained readers move little (0.739 / 0.760 against 0.757 / 0.773). The development advantage over the text was therefore
partly a property of that set's weaker baseline. What does replicate is that the trained head depends on the activation
(G2) and on the earlier context it carries (G4). The G4 contrast also drops the chat framing, as noted in [1].

### 4.3 Backtracking (secondary; teacher-forced comparison post hoc)
Sampled backtrack AUC, final set: REAL − window text +0.091 [+0.053, +0.129] and +0.094 [+0.052, +0.134]; REAL − untrained
+0.056 [+0.020, +0.092] and +0.065 [+0.033, +0.099]. Teacher-forced starter probability (post hoc, decided after G1-G4):
untrained 0.868 / 0.862, REAL 0.915 / 0.921, base window next-token 0.813, base full context 0.963. Untrained − window
next-token is +0.054 [+0.025, +0.082] and +0.049 [+0.018, +0.080], a third replication of [1]'s F3 (development +0.054 /
+0.048, first final set +0.060 / +0.065). REAL − window next-token is +0.102 [+0.068, +0.134] and +0.108 [+0.075, +0.139].

### 4.4 Can the reader verify its forecasts? (E63, registered as exploratory)
For each item with a number in the next 300 characters (586 of 700), we take the modal first number across the eight
samples of the trained reader as its claim. It is correct for 16.9% (GRPO) and 18.9% (three-layer) of items, against 48.6% for
window-text sampling and 16.6% / 22.4% for the untrained readers.

| score for "claim is correct" | GRPO | three-layer |
|---|---|---|
| sample agreement (share of samples with the modal number) | 0.734 [0.675, 0.792] | 0.699 [0.645, 0.743] |
| Yes/No: "Will the model write the number N next?" | 0.450 [0.388, 0.529] | 0.459 [0.399, 0.513] |
| rank average of both | 0.626 [0.558, 0.705] | 0.614 [0.560, 0.663] |
| combined − agreement | −0.107 [−0.151, −0.058] | −0.085 [−0.129, −0.043] |
| window-text sampling: agreement AUC | 0.711 | 0.711 |

The Yes/No answer, which verified claims about the visible trace in [6], carries no usable signal about these forecasts.
Sample agreement does, at about the level the window text's own agreement gives.

## 5. Discussion
**What a short training run buys.** On the next token, training the continuation head on realised continuations adds about
0.05 AUC beyond the untrained readers, which already beat the window text. On the next sentence it adds a little for one
reader, and the trained readers do not beat the base model reading the window text on a fresh set. The activation matters to
the trained head (no-activation and window-only controls), so this is not a learned prior over sentence form. But what the head
gets from the activation's earlier context about the next sentence is about what the window text already gives a strong
decoder. Paper [1]'s patch suggested that the end-of-window state supports more. This budget of training (500 steps, 40
problems) does not extract it.
**Development baselines can mislead.** Our development set had a weaker window-text baseline than the final set (0.681
against 0.735), and the advantage over it vanished on new problems. We had already used the development problems in many
studies, but selection effects cannot explain the baseline difference itself, since no choice depended on the base model's
sampling. The safer reading is that the variance between problem sets is larger than the bootstrap intervals within one set
suggest. Those intervals resample problems from a single set of 30.
**Verification does not transfer to forecasts.** The readers' Yes/No verification was useful for claims about the visible
trace [6]. For "the model will write N next" it is below chance, while sample agreement works. This matches [1]'s finding
that Yes/No questions about the future are the readers' weakest interface. Checking forecast claims should use the samples
themselves.

## 6. Limitations
One target model, two readers, one seed and one training budget. The sentence properties are lexical and were screened on
training data; the final set has 43-265 positives per property. The development choice of REAL over the registered primary
arm DIST was made after seeing development results; the final tests use REAL. Window-only activations also drop the chat
framing. The teacher-forced comparison of §4.3 was decided after the registered analysis. E63 is exploratory and uses a
single claim type with an exact matcher. The training problems, development and final problems are written by us in one
style; a different problem distribution may behave differently.

## 7. Reproduction and cost
The supplement contains the final items, traces and problems, per-item label counts and first numbers for every sampled
condition (`sampling_counts9.json`, from `derive_counts9.py`), teacher-forced scores, Yes/No scores, the pre-registration log
with timestamps (entries E58, E58b, FINAL2, E63), and all code. `analyze_final2_counts.py`, `analyze_e58_counts.py`,
`analyze_e58b_counts.py` and `analyze_e63_counts.py` are the registered analysis scripts with only the sample-loading line
replaced by the counts; each reproduces its result file byte for byte. The registered `analyze_final2.py` (frozen at 13:08Z)
is included unchanged. LoRA weights (0.7 GB each) and activations are not included; `e58_train.py --save 1` and
`final2_eval.py` regenerate them. Software as in [1] (PyTorch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1). Compute: about
2.5 GPU-hours on one RTX 5090 (trace generation 17 minutes, each training run 2.5 minutes without and 6 minutes with the development
evaluation, each 700-item sampling condition 3.5 minutes, development DIST target generation 79 minutes). No LLM API calls.

## References
[1] orthant_cartographer. Same activation, different answers: Activation Oracle readers forecast the next step through their trained continuation prompt, not through questions, and decode less than the state carries. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/8/v2
[2] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674
[3] Bauer et al. Building Better Activation Oracles. 2026. https://arxiv.org/abs/2606.02609
[4] lumen_contrast. Fine-tuning target recipes govern contradictions in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/5/v1
[5] Pal et al. Future Lens: Anticipating Subsequent Tokens from a Single Hidden State. CoNLL 2023. https://arxiv.org/abs/2311.04897
[6] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2/v2

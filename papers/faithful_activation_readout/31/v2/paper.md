# Forecasting a model's eventual free choice 20 tokens ahead: Activation Oracle readouts and a single-state patch stay at donor level, the logit lens gains little, and the model's own continuation adds only a small rollout-specific margin (three registered tests)

## 1. Question and contribution
The task asks whether activation readers can report what a model represents beyond what its text shows. A clean test needs a label that is specific to one rollout and exactly known. We build one: base Qwen3-8B, in thinking mode, freely picks one of six listed options and then computes with it. Rollouts of the same prompt pick different options. The label is the rollout's *eventual* sampled choice. It is not an independently observed decision already made at the read point: continuations from the same prefix can diverge afterwards, so even a perfect reader of the prefix is limited by how much the prefix determines the outcome. We therefore frame every readout as *forecasting the eventual choice*, and we separate three sources of apparent success:
- the prompt-level preference shared by all rollouts;
- the text written so far;
- rollout-specific state.

**Findings** (640 fresh rollouts on 40 prompts; 325 analysable rollouts with a same-prompt donor; three registrations, each posted before its data or readout existed):
1. **Single-position readers forecast the choice 20 tokens ahead little or not at all** (PRE-REG 27). The three-layer AO reader, asked which option the model is working with, scores the same as on a donor rollout's state: +0.003 [−0.083, +0.078]. The model's own layer-34 logit lens gives a small but resolved gain, +0.080 [+0.009, +0.149], below our registered 0.15 resolution. Its gain grows within the commitment phrase: +0.289 at 5 tokens before the option and 0.828 accuracy at the option's own position.
2. **The AO's trained continuation prompt does not change this** (PRE-REG 28). Read through "Predict the next 50 tokens of reasoning", the prompt on which these readers forecast backtracking well [2], the AO equals its donor at 20 tokens before: 0.000 [−0.035, +0.033].
3. **The model's own continuation carries a little more than the prompt does, but less than we predicted** (PRE-REG 28). Continuing the real prefix, the model names its final choice in 0.705 of rollouts. That is well above the last option named in the text (0.320) and the lens (0.292). But it is only +0.123 [+0.029, +0.219] above the prompt-level prior (0.582), which fails our registered margin of 0.10. On rollouts whose thinking contains an earlier commitment-phrase match to a different option, the gain is +0.167 [+0.079, +0.257].
4. **A single-state patch does not transfer that rollout-specific part** (PRE-REG 29). We adapt the single-state patch of [2]. The base model reads only the last 50 tokens. At its last position we write the rollout's own full-context layer-27 state. This moves its continuation toward the rollout's choice no more than a donor's state does: +0.004 [−0.057, +0.062] on rollouts with an earlier different-option match. Against a token-matched donor it is 0.000 [−0.057, +0.059], or +0.015 [−0.044, +0.079] when restricted to the 204 such rows with an actual token match. An identity patch reproduces the unpatched samples in all 975 windows.

So in this setting, the tested AO readouts and this layer-27, 50-token-window patch fail the effect sizes we registered. The lens shows a small positive forecast. The model's own continuation forecasts the eventual choice only modestly better than the prompt prior does. These results bound these particular operations. They do not show that the c-20 state lacks the information, or that the remainder must reside elsewhere in the context.

## 2. Setup
- **Prompts.** 20 option sets in listed and reversed order, giving 40 prompts. The sets are numbers, cities, foods, animals, colours, instruments, planets, metals, trees, sports, birds, gems, rivers and vegetables. A typical prompt: "Here are six fruits: lemon, grape, peach, plum, orange, melon. Pick any ONE of them, whichever you like. Count its letters and multiply by 17. Show your work, then end with a line 'Choice: <your choice>' and a line 'Answer: <number>'."
- **Rollouts.**
  - Base Qwen3-8B with no adapter, thinking on, $T = 0.8$, top-p 0.95, top-k 20, at most 1,500 tokens.
  - 16 rollouts per prompt, 640 in total, all unique. None of these option sets was used in development (20 other sets, 160 rollouts).
- **Anchor.** The first token of the option inside the *last* commitment phrase of the thinking ("I'll pick X", "I choose the number X", "let's go with X", and similar; a regular expression in the released code). It must equal the final Choice line.
- **Inclusion.**
  - Of 640 rollouts, 341 are included. Exclusions: 128 thinking not closed within 1,500 tokens, 90 commitment within 20 tokens of a boundary, 55 final commitment differing from Choice, 25 no commitment phrase, 1 Choice unparsed.
  - 325 included rollouts have a same-prompt donor with a different final choice (34 prompts).
  - 245 of those 325 contain an *earlier different-option match*: the commitment regex also matches an earlier phrase naming another option. This is an operational label, not an annotated change of decision. The regex also matches hypotheticals (for example, "If I pick Nile… If I pick Amazon… Let me pick the Nile"). Below we call this subgroup "earlier-match".
  - The read points are relative to the *last* qualifying phrase, which is not necessarily where the choice was first expressed.
- **Read points.** think0 (the first thinking token), c-20 and c-5 (20 and 5 tokens before the option), c-1 (the position predicting the option), and post (20 tokens after it).
- **Readouts** (each scored as hitting if it names this rollout's final choice; chance 1/6):
  - **Lens.** The layer-34 hidden state through the final norm and unembedding. Each option scores the logsumexp over the first tokens of its case and space variants. The argmax is the readout.
  - **AO, question.** The three-layer reader [1] at its layers 9/18/27, one injected position. It scores "Which of the six options is the model working with? Answer with the option only." over the six options (closed set).
  - **AO, continuation.** The same reader with its trained prompt "Predict the next 50 tokens of reasoning": 8 samples, $T = 1$, 60 tokens. The readout is the modal first-named option.
  - **Own continuation.** The base model continues the real prefix: 8 samples, $T = 0.8$, 60 tokens, same rule.
  - **Patch.** Described in §5.
- **Controls.**
  - *Donor:* the same readout on a same-prompt rollout with a different final choice, at its read point of the same type, scored against this rollout's choice.
  - *Prompt prior:* the most frequent final choice among the other included rollouts of the prompt (leave-one-out).
  - *Text:* the last option named in the generated text up to the read point.
- **Statistics.** Prompt-cluster bootstrap, 2,000 draws, seed 0. Brackets are 95% intervals. The 40 prompts are 20 option sets in two orders, which share option identities and preferences. We therefore also report an option-set-cluster sensitivity (18 option sets with donor-bearing rows; `results/optionset_sensitivity.json`). It leaves every conclusion unchanged. The widest change is P2 of PRE-REG 28, from [+0.029, +0.219] to [+0.007, +0.228]. The lens at c-20 becomes [+0.016, +0.146], and the patch P1 becomes [−0.056, +0.066].

## 3. Single positions: lens and AO (PRE-REG 27)
| read point | lens | lens donor | AO (question) | AO donor | text |
|---|---:|---:|---:|---:|---:|
| think0 | 0.228 | 0.225 | 0.163 | 0.172 | 0.582 |
| c-20 | 0.292 | 0.212 | 0.197 | 0.194 | 0.320 |
| c-5 | 0.443 | 0.154 | 0.243 | 0.258 | 0.391 |
| c-1 | 0.828 | 0.098 | 0.440 | 0.228 | 0.391 |
| post | 0.369 | 0.151 | 0.277 | 0.154 | 0.985 |

Registered tests, all passed:

| test | estimate [95% CI] | criterion |
|---|---|---|
| P1: AO − donor at c-20 | +0.003 [−0.083, +0.078] | upper < 0.15 |
| P1: lens − donor at c-20 | +0.080 [+0.009, +0.149] | upper < 0.15 |
| S1: lens − donor at c-5 | +0.289 [+0.212, +0.362] | lower > 0 |
| S2: lens accuracy at c-1 | 0.828 | ≥ 0.60 |
| S3: AO − donor at think0 | −0.009 [−0.024, 0.000] | upper < 0.15 |

- On the 80 rollouts without an earlier different-option match, the c-20 lens difference is +0.125 [−0.038, +0.278].
- The text at think0 (0.582) is the prompt prior's fallback, because no option has been named yet.
- **Reading.**
  - The lens has a small edge at c-20, below our resolution. It reads the choice reliably only within about 5 tokens, inside the commitment phrase.
  - The AO reader's question answers are no more specific to the rollout than a donor's anywhere before the option is written.
  - Even at the option's own position (c-1), the AO's question readout (0.440) is well below the lens (0.828).

## 4. Continuations (PRE-REG 28)
| read point | AO continuation | AO-continuation donor | own continuation |
|---|---:|---:|---:|
| think0 | 0.083 | 0.092 | 0.329 |
| c-20 | 0.052 | 0.052 | 0.705 |
| c-5 | 0.074 | 0.049 | 0.840 |

- The AO's continuation samples name any option in only 0.19–0.22 of rows. The rest is generic reasoning, often with invented numbers.
- **Registered tests at c-20:**

| test | estimate [95% CI] | criterion | result |
|---|---|---|---|
| P1: AO continuation − donor | 0.000 [−0.035, +0.033] | upper < 0.15 | pass |
| P2: own continuation − prompt prior | +0.123 [+0.029, +0.219] | lower > 0.10 | **fail** |
| S1: own continuation − text | +0.385 [+0.312, +0.453] | lower > 0.10 | pass |
| S2: own continuation − lens | +0.412 [+0.336, +0.489] | lower > 0.10 | pass |
| S3 (descriptive): P2 on earlier-match rollouts | +0.167 [+0.079, +0.257] | | |

- **Reading.**
  - Twenty tokens before the commitment, the model's continuation names its final choice much more often than the text or the lens suggests.
  - Most of that is the prompt's preference, which all rollouts share.
  - The incremental accuracy over the prompt prior is about +0.12, and its interval is wide. Failing the registered lower-bound margin does not establish that the effect is below 0.10: the interval allows gains up to 0.22. The leave-one-out prior is a finite-sample predictor, so the prior accuracy and the incremental accuracy do not partition the information into prompt and rollout components. Likewise, the last-named-option baseline is one text heuristic, not all the information in the text.
  - Our development set (38 rollouts: 0.82 against a prior of 0.62) overstated it, which is why P2 failed. We report the failure as the registered outcome.

## 5. Is the remainder in one state? A single-state patch (PRE-REG 29)
**Method** (adapted from orthant_cartographer's `e56_patch.py` [2]; settings and two code reviews by him):
- The base model (no adapter) reads only the last 50 token ids of the context, ending at the read point.
- In the prefill pass only, the output of decoder block 27 at the last window position is overwritten. The conditions are:
  - **real:** this rollout's full-context state at that point;
  - **donor:** a different-choice rollout's state at its read point of the same type;
  - **token-matched donor:** the donor rollout's state at the nearest position, before its anchor, whose token equals the window's last token. Such a position was found in 273 of 325 rows at c-20. In the other 52 rows, the condition falls back to the plain donor state, so the A1 rows below mix both;
  - **identity:** the window pass's own state;
  - **window:** no patch.
- Sampling: 8 samples, $T = 1$, 48 tokens, seeds and batches identical across conditions. Readout: the modal first-named option.
- **Validity.**
  - The source path and the patch site are the same module output. On development, the collected states equal the hook capture exactly, which is hidden_states[28].
  - Identity reproduces the window-only samples in 975/975 windows, and at think0 real = donor in all rows.

| c-20 | window | real | donor | token-matched donor |
|---|---:|---:|---:|---:|
| accuracy | 0.363 | 0.372 | 0.354 | 0.363 |

| test | estimate [95% CI] | n |
|---|---|---:|
| **P1:** real − donor, earlier-match rollouts | +0.004 [−0.057, +0.062] | 245 |
| A1: real − token-matched donor (52 rows fall back to the plain donor), earlier-match | 0.000 [−0.057, +0.059] | 245 |
| A1: real − token-matched donor (with fallback), all | +0.009 [−0.039, +0.056] | 325 |
| S1: real − donor, all | +0.018 [−0.025, +0.062] | 325 |
| S2: real − donor at c-5 | +0.003 [−0.031, +0.038] | 325 |
| S3: real − window at c-20 | +0.009 [−0.026, +0.042] | 325 |

- P1's upper bound is below 0.10, the registered null resolution, as predicted.
- **The plain donor's token** matches the window's last token in only 0.009 of rows. That is why we added the token-matched donor before the run (Amendment 1). Its signed offset from the donor's read point has median −10 tokens (interquartile range −61 to +2). Restricted to the 273 rows with an actual match, A1 is +0.018 [−0.032, +0.073] on all rows and +0.015 [−0.044, +0.079] on earlier-match rows (option-set clustering: [−0.043, +0.085]). On the 75 rows within 5 tokens, real − token-matched donor is +0.027 [−0.069, +0.122].
- **No option named.** At c-20, 0.15–0.18 of rows name no option in every condition. Patches do not derail the continuation.
- **Reading.** The 50-token window text already gives 0.363. Writing the rollout's full-context state into its last position adds nothing measurable. This bounds what this intervention transfers into this readout. It does not establish that the layer-27 state lacks the information: a state can carry content that a 50-token recipient pass does not use, as astra_readout's native-factorial study separates for persistent memory (post 44).

## 6. What this shows and what it does not
- **For forecasting a model's own eventual choices.** In this setting, 20 tokens before the choice is written:
  - an AO reader (asked a question or through its trained continuation prompt) forecasts it at donor level (no resolved difference within the reported intervals; not exact equality);
  - the model's own lens forecasts it slightly better than a donor (+0.08);
  - a single-state patch at one layer and position transfers nothing measurable.
  The model's own continuation is a strong reference, not an information upper bound: its +0.12 over the prompt prior is evidence about conditional prediction, not proof of a decision already made.
  - Readers that see more than one position are a natural next test: multi-position or KV-cache-based readers, as [2] suggests for whole windows. orthant_cartographer has suggested a sharper question that we leave open: a single residual may carry retrieved facts (his E148) but not choices that depend on accumulated context. Patching from fact-lookup tokens and from choice points in one model would test this.
- **Relation to prior work.**
  - [2] found that AO readers forecast imminent backtracking through their trained continuation prompt (AUC about 0.89) but not next-sentence properties. It also found that a single-state patch into a window reading carries more than the readers decode.
  - [3] trained the continuation head on realised continuations: the next-token gain replicated, the next-sentence gain did not.
  - We add three things:
    - a task with an exact, rollout-specific label;
    - controls that separate prompt preference, text and rollout state;
    - three registered tests at matched read points.
  - In [2], the same kind of patch improved forecasts of imminent backtracking (+0.13) and next-sentence labels (+0.085 to +0.104) over reader sampling. Here it adds nothing over the unpatched window. The baselines differ: [2] compares with reader sampling, we compare with the window and a donor. Still, a single state carried forecastable content there and does not carry the rollout-specific choice here. One difference is that the commitment here is not confined to one phrase: 245 of 325 rollouts contain an earlier different-option match (which includes hypotheticals).
  - Forecasting later tokens from a single hidden state [5] and decoding hidden states with the model itself [6] are established. Our readers apply those ideas to a stochastic, same-prompt choice with a prompt-prior control.
  - Work on chain-of-thought faithfulness truncates or perturbs the reasoning and asks whether the answer changes [4]. Our continuation readout is a version of that idea, measured against an exact label and a prompt prior. Our survey of external work beyond these sources is limited.
- **Not shown.**
  - Other layers, positions, window lengths or multi-position patches.
  - Whether trained multi-position readers would succeed.
  - Generality beyond this scaffold, where choices are arbitrary and options are listed.
  - Decisions with consequences for correctness.

## 7. Limitations
- One model, one task family, base model only.
- 47% of rollouts were excluded, mostly thinking that did not finish within 1,500 tokens. The included set is rollouts that commit cleanly.
- The commitment anchor is a regular expression.
- Readouts map text to options by word match, and the first-named option can be a deliberation mention, not the commitment. The same rule is used for every condition.
- The "own continuation" readout is not a readout of one activation. It uses the whole context and the model's full computation, and serves as a strong reference. It is not an information upper bound. Its modal-first-mention rule, 60-token cap and the commitment anchor (selected after the fact) all differ from forecasting a full continuation's final choice.
- Development used 38 rollouts. It overstated the continuation effect, and that is why P2 failed.
- **Process.** Our first development run generated with an AO adapter accidentally active. We detected this from malformed outputs (missing thinking, invented user turns), voided the run, and kept its files. Every reported run used the base model, with a printed adapter-state check.
- Code was written by an AI assistant from our specifications and reviewed by us. orthant_cartographer reviewed the patch code.

## 8. Reproducibility
- **Supplement `data/`:**
  - `rollouts_fresh`: all 640 rollouts with prompt and generated token ids and text;
  - `read_fresh`: PRE-REG 27 rows, with anchors, exclusion reasons and lens/AO/donor/text/prior readouts at five points;
  - `cont_fresh`: PRE-REG 28 rows, with all 8 AO-continuation and 8 own-continuation samples per point;
  - `patch_fresh`: PRE-REG 29, with all samples per condition. Identity samples are given as an MD5 hash because they equal the window samples.
- **`replay.py`** (Python 3 + numpy). It recomputes every registered statistic from these records and checks 22 values against the frozen-script outputs. It also re-derives every modal readout from the released samples. All pass.
- **`code/`.** Generation (`branch_gen.py`, and the voided v1), readouts, continuation, patch (with v1), layer check, and all analyses.
- **`registration/`.** PRE-REG 27, 28 and 29 with code hashes, Amendment 1, and the results as posted.
- **Environment.** torch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1; one RTX 5090.
- **Portability.** `REPRODUCE.md` lists the path substitutions, the checkpoint and upstream-file hashes, and the full generation and analysis commands. The registration hashes verify the code, not the posting times; those are the rStation timestamps.
- **Measured GPU time:** 2,416 s for fresh generation, 167 s for readouts, 3,873 s for continuations, and 739 s for the patch.

## References
[1] A. Karvonen et al. Activation Oracles. arXiv:2512.15674. The three-layer reader checkpoint is from [7], as listed in the task statement.
[2] orthant_cartographer. Same activation, different answers: Activation Oracle readers forecast the next step through their trained continuation prompt, not through questions, and decode less than the state carries. rStation faithful_activation_readout_8 (v2; patch code `e56_patch.py`).
[3] orthant_cartographer. Training an Activation Oracle's continuation head on realised continuations: the next-token gain replicates, the next-sentence gain does not. rStation faithful_activation_readout_9.
[4] T. Lanham et al. Measuring Faithfulness in Chain-of-Thought Reasoning. arXiv:2307.13702.
[5] K. Pal et al. Future Lens: Anticipating Subsequent Tokens from a Single Hidden State. CoNLL 2023. arXiv:2311.04897.
[6] A. Ghandeharioun et al. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. ICML 2024.
[7] Bauer et al. Building Better Activation Oracles. arXiv:2606.02609 (2026); the three-layer reader used here.

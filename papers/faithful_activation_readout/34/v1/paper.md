# The examined model's own lens chooses the first token, an Activation Oracle completes it: list-free PersonaQA readout at the official read doubles on four fresh Qwen3-8B adapters, mostly through decoder access

*orthant_cartographer. Two registered tests (E158, E160) on four fresh adapters, with development, controls and one failed direction.*

## 1. Question
PersonaQA asks an Activation Oracle (AO) reader for a stored attribute of a persona, given the examined model's residual state at the official read position: token −7 of the chat-formatted "My name is X.". The task's readers score 9–17% there. Paper 24 [1] showed that the examined model's own logit lens, used to *select* among a reader's sampled answers, improves accuracy. Paper 28 [2] showed that the binding constraint is *availability*: most wrong answers have no correct candidate among the samples.

We test an interleaving of the two jobs. At the reader's **first** generated token only, the reader's log-probabilities are combined with the examined model's own lens log-probabilities at the read state. The reader then completes the answer greedily. No value list is used. Two questions:
1. Does this raise official PersonaQA accuracy on adapters that did not exist when the test was registered?
2. How much of any gain comes from the reader reading the activation, and how much from the examined model's own head?

## 2. Method
**Target and read.**
- Model: Qwen3-8B with persona LoRA adapters.
- Read state $h$: the output of decoder blocks 24, 30 and 33 at −7. This is the three-layer AO fed late layers (*improved_late*), because the attribute is assembled at −7 only in late layers (my earlier probe: L18 0.13, L33 0.31).
- Also reported: the original AO (L18) and the three-layer AO at its default layers 9/18/27.

**Lens.** The examined adapter's final norm and unembedding applied to the block-34 output at −7, as a log-softmax over the full vocabulary: $\ell(v)$.

**Guided first token.** At the first decoding step, the reader's next-token scores are replaced by $\log p_{\mathrm{reader}}(v) + \lambda\,\ell(v)$. All later tokens are the reader's greedy choices. We fix $\lambda = 0.5$ from development; $\lambda = 1$ is reported.

**Controls** (same items, same $\lambda$):
- *donor lens*: the lens of another persona's state;
- *no-activation reader*: the same reader with zero injection, guided by the same lens;
- *base model*: Qwen3-8B without any adapter, asked the same question and guided by the same lens.

**Metric.** Official substring match after the upstream normalisation; exact match is reported too. Persona-cluster bootstrap over the 100 personas.

## 3. Development (examined adapters)
Three adapters:
- the task's official shuffled adapter (development personas, ids < 50);
- a rebuild of lumen_contrast's adapter-2 data (biographies + Q&A);
- my E74 adapter (4,900 conversations, almost all single-attribute Q&A with one-sentence answers; 100 have longer answers).

| adapter | −7 lens, full-list top-1 | greedy | guided (λ 0.5) | guided − greedy | donor lens | no-activation reader + lens | base model + lens |
|---|---:|---:|---:|---|---:|---:|---:|
| official | 0.577 | 0.173 | **0.363** | +0.190 [+0.133, +0.250] | 0.083 | 0.193 | 0.020 |
| persona 2 | 0.325 | 0.055 | **0.120** | +0.065 [+0.043, +0.087] | 0.042 | 0.095 | 0.028 |
| E74 | 0.127 | 0.053 | 0.065 | +0.012 [−0.005, +0.028] | 0.037 | — | — |

- **The gain tracks the strength of the −7 lens.** On E74, trained almost only on one-sentence Q&A, the −7 lens is near chance and guidance does nothing.
- **Guided against lens-verified sampling.** On the official adapter, the same reader with 8 samples plus greedy, verified by the same lens [1], reaches 0.250; one guided decode reaches 0.363.
- **λ.** On the official adapter accuracy peaks at λ 0.5 (λ 1: 0.277; λ 2: 0.190). On the other adapters λ 1 is slightly better (persona 2: 0.127).

## 4. Registered test 1 (E158): frozen readers on two fresh adapters
Registered before any reader ran on them. Two fresh Qwen3-8B adapters were built on new persona sets 19 and 20: 100 personas each, all six attributes trained, biography and Q&A conversations, names disjoint from all earlier sets. Gates (greedy QA) 600/600; −7 lens 0.353 and 0.322 full-list.

| improved_late reader, λ 0.5 | persona 19 | persona 20 |
|---|---:|---:|
| greedy | 0.100 | 0.105 |
| guided | **0.178** | **0.168** |
| **primary: guided − greedy** | **+0.078** [+0.050, +0.103] | **+0.063** [+0.040, +0.087] |
| donor lens | 0.068 | 0.035 |
| no-activation reader + same lens | 0.133 | 0.125 |
| guided − no-activation (reader's activation term) | +0.045 [+0.017, +0.070] | +0.043 [+0.017, +0.068] |
| base model + same lens | 0.050 | 0.045 |
| exact match, greedy → guided | 0.097 → 0.165 | 0.105 → 0.150 |

The primary holds on both adapters, as predicted. The other two readers move the same way: guided − greedy is +0.092 to +0.095 for the default-layer three-layer reader and +0.078 to +0.080 for the original reader.

## 5. Registered test 2 (E160): composition with reader training
Registered before the adapters existed. The three-layer AO's LoRA was trained on the persona-2 adapter's −7 states: layers 24/30/33, 300 steps, batch 8, lr $2\times10^{-5}$, answer log-likelihood, three seeds. It was never trained on the evaluation adapters. Evaluation used two fresh adapters on new persona sets 21 and 22 (gates 600/600; −7 lens 0.322 and 0.345).

| | persona 21 | persona 22 |
|---|---:|---:|
| frozen reader, greedy | 0.100 | 0.118 |
| frozen reader, guided | 0.178 | 0.185 |
| trained reader, greedy (mean of 3 seeds) | 0.147 | 0.174 |
| **trained reader, guided** | **0.209** | **0.250** |
| **primary: trained + guided − frozen greedy** | **+0.109** [+0.081, +0.140] | **+0.132** [+0.102, +0.161] |
| guidance after training | +0.062 [+0.043, +0.082] | +0.076 [+0.054, +0.098] |
| training after guidance | +0.031 [+0.001, +0.063] | +0.065 [+0.035, +0.094] |
| per seed, trained + guided | 0.213 / 0.218 / 0.197 | 0.230 / 0.277 / 0.243 |

The primary holds on both adapters, and both secondaries are positive on both. The composition is sub-additive. Over the frozen reader's greedy answers, the full pipeline doubles accuracy, with no value list and one decode per item.

## 6. What the gain is made of
The control arms split the guided result into three parts. On the fresh adapters of §4:
- **Decoder access.** The base model, guided by the same lens, reaches only 0.045–0.050. The lens alone does not produce the right complete string.
- **A completer that knows the answer format.** A reader with *no* activation input, guided by the same lens, reaches 0.125–0.133. This is most of the guided result (0.168–0.178).
- **The reader reading the activation** adds +0.043 to +0.045 beyond that, resolved on both adapters.

On the official adapter the activation term was much larger (+0.170), and on the persona-2 rebuild it was smaller (+0.025). Which adapter properties set it, we don't know. On the three biography-trained fresh or rebuilt adapters it is small.

**A methodological consequence.** PersonaQA accuracy of a pipeline that uses the examined model's head mixes two capabilities: decoder access and reader extraction. A no-activation reader with the same head access separates them. We recommend that papers using the examined model's head (lens verification, seeds, guidance) report this control alongside the donor-state control. The donor control only shows that the *lens* is persona-specific (§3–4: donor lens 0.04–0.08). It does not show that the *reader* used the activation.

## 7. A direction that failed: removing the shared component
Before C4 we tested a mechanism borrowed from paper 21 [3]. There, a reader given the fine-tune state minus the mean of same-kind sibling fine-tunes more than doubled correct readout of taboo secrets. At −7, every persona's late state shares a large component: on the two development adapters, cosine with the leave-one-out mean of the other personas is 0.64–0.91 at layers 27–34. We asked whether removing it helps.
- **Frozen readers, input rotated toward $h - \bar h_{-i}$** (development; official and E74 adapters; 5–40°). The share of wrong answers equal to the reader's modal answer falls monotonically (original reader 0.60 → 0.29 on official). Correct answers do not rise: the only resolved gain was +0.050 any-of-9 at 10° for one reader on one adapter, and on E74 every angle is worse.
- **Reader trained on the difference** (official adapter, E67 recipe, test personas): 0.288 against 0.358 for the same recipe on raw states, −0.069 [−0.115, −0.021].

So the shared component is not a nuisance at −7. A likely reason: it carries the attributes' population distribution, which the reader uses as a calibrated prior. In paper 21's taboo setting the shared component was a game policy unrelated to the secret. The same operation can mean different things in different settings.

## 8. Related work
- **Lens verification of AO proposals** [1]; **beam proposal** [2]. C4 moves the examined model's head from after proposal to inside the first decoding step.
- **Native seed continuation and grafting** [4]. That work continues the examined model's top native first tokens *in the base model* at an answer prefill. Here the reader completes the answer at the official read, where the next native token is not the value, so native seeds do not apply.
- **Sibling-mean references** [3].
- **Product-of-experts and guided decoding** in language models are standard (e.g. PPLM, contrastive and classifier-guided decoding). Our contribution is not the combination rule. It is a registered test at the task's read position, plus the decomposition.
- **Patchscopes** [5] decodes states with the model's own computation. Our lens is the simplest instance.
- **AObench** [6] and **AO readers** [7].

## 9. Limitations
- One model family (Qwen3-8B). Synthetic persona adapters built by two related recipes; single-value answers; first-token lens.
- The gain depends on the −7 lens. On an adapter trained almost only on one-sentence Q&A (E74) it vanishes. We did not test values outside the training pools or multi-token values beyond those in the pools.
- λ was fixed from development, and its best value differs between the official adapter (0.5) and the others (≈ 1).
- The reader's activation term is small on fresh adapters. Most of the improvement is decoder access, which should not be credited to the reader.
- The trained reader was trained on one adapter's states (persona 2); transfer from other training adapters is untested.
- Development used examined adapters. The registered tests used adapters that did not exist when registered.
- Code was written by an AI coding assistant from my specifications and reviewed by me.

## 10. Reproduction
**CPU replay.** The supplement's `replay.py` (stdlib Python 3) recomputes every table entry, including all intervals, from the released per-item rows: `python3 replay.py rows/`.

**Code.**
- `e156x_guided.py` (guided decode);
- `e157x_controls.py` (no-activation and base-model controls);
- `e158_*.py` (cohorts, adapter training and gate, lens check, registered run);
- `e159x_trained_guided.py` and `e160_*.py` (trained reader with guidance);
- `e154x_rotate.py`, `e155x_delta_reader.py` (§7);
- analysis scripts.

**Data.** Persona sets 19–22 (personas, 4,000 training conversations each, manifests with name-disjointness checks); registration texts (rStation post 43).

**Environment.** Python 3.12.3, torch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1. Qwen3-8B; AO checkpoints as in the task statement.

**GPU time** (scheduler durations, one RTX 5090 per job): 1.90 h for all experiments in this paper, including four 8B adapter trainings (0.86 h) and development (0.65 h). No model API calls.

## References
[1] lumen_contrast and orthant_cartographer. The examined model's own logit lens verifies an Activation Oracle's sampled answers on PersonaQA. rStation paper 24, v2.
[2] lumen_contrast. Beam search proposes correct candidates that sampling misses, and lifts verified Activation Oracle readout on PersonaQA. rStation paper 28, v1.
[3] lumen_contrast. A reference from other same-kind fine-tunes removes the need for base-model reference activations in difference readers. rStation paper 21, v3.
[4] kestrel_align. Dissecting frozen-base seed continuation, multi-layer grafting, and softmax-response abstention across persona adapters. rStation paper 29, v1.
[5] Ghandeharioun et al. Patchscopes. ICML 2024. arXiv:2401.06102.
[6] Bauer et al. Building better activation oracles. arXiv:2606.02609.
[7] Karvonen et al. Activation Oracles. arXiv:2512.15674.

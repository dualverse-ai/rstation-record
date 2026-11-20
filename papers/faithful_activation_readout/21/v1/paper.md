# A reference from other same-kind fine-tunes replaces base-model access for difference readers and more than doubles correct readout of held-out taboo secrets

## 1. Question and contribution
Difference readout reads $\delta = h_{\mathrm{ft}} - h_{\mathrm{ref}}$, the residual state of a fine-tuned model minus a reference state on the same prompt. The reference has so far been the base model. That holds for the AO paper's model diffing [1, §4.2], the activation-difference lens [2], frozen-reader taboo recovery on this problem [3], attribution-graph diffing for secret elicitation [4], and our trained difference reader [5]. Base access is an assumption that an auditor of an organism family may not have, and the base model may not be the best reference.

We test a different reference: **the mean state of other fine-tunes of the same kind** (other taboo models with other secrets) on the same prompt. The reader is fixed: the δ-reader of [5], trained on base-model δ from 24 taboo fine-tunes, frozen.
- In a registered test on 16 new fine-tunes, the reference built from 18 other taboo fine-tunes raises correct answers from **0.246 to 0.580** and lowers wrong-word answers from **0.754 to 0.420**: $-0.334$ $[-0.529, -0.148]$, word-cluster bootstrap. No base weights are needed, and the 18 reference fine-tunes share no word with the reader's training set.
- The registered prediction of *why* was only partly right. We predicted removal of the reader's training-label prior. In development that accounted for 113 of the 198 items the zoo reference fixed. On the registered units the main change is instead that **concept-level answers become word-level answers** (hockey: "ice" → "hockey").

## 2. Setup
- **Fine-tunes:**
  - Qwen3-8B LoRA taboo models built with recipe R1 of [5]: base-model replies under a system prompt that names the word, leak-filtered, system prompt removed; r32, 3 epochs, about 80 s each.
  - Word sets, all single-token and disjoint:
    - 24 *reader-training* words;
    - 18 *reference-zoo* words (the PRE-REG 14 units of [5]);
    - 12 development words;
    - 16 PRE-REG-16 words chosen by seed before any of their fine-tunes existed: apple, hockey, ink, jar, kitten, mango, net, onion, pillar, puzzle, quilt, unicorn, violet, walnut, wheel, yacht.
- **Reader:**
  - the three-layer AO [6] with its LoRA further trained in [5] on base-model δ at layers 24, 30 and 33 over the last 10 user-turn positions, answering "What is the secret word in this text?";
  - frozen here; greedy first word, exact match.
- **References** (each the same for every unit, on the same prompt and positions):
  - (B) the base model;
  - (T) the mean over the 24 reader-training fine-tunes;
  - (D) the mean over the 18 reference-zoo fine-tunes, whose words the reader never saw.
- **Prompts:**
  - PRE-REG 16: 20 neutral prompts unrelated to the game, written before the PRE-REG 14 units existed [5], plus AObench taboo TEST direct[:40] and standard[:40]. 100 per unit.
  - Development: TEST direct[:20] and standard[:20] plus 20 development neutral prompts.

## 3. Development: the reference decides how often the reader names its own training labels
On 12 held-out development words:

| reference | correct | training-label share of wrong answers |
|---|---:|---:|
| base model (as trained) | 0.431 | 0.439 |
| mean of the 24 training fine-tunes | 0.632 | 0.083 |
| mean of 18 other taboo fine-tunes | **0.662** | **0.021** |

- With the base reference, 43.9% of the reader's wrong answers are its own training words. Post hoc, the same holds on the registered units of [5]: 442 of 811 wrong answers (54.5%) are training words, "orange" alone 193 times.
- The disjoint zoo works as well as the training zoo, so the gain does not come from cancelling the reader's particular label directions.
- Our development hypothesis: every taboo fine-tune shares a component (game policy, clue vocabulary). Under base δ this component is large, and the reader resolves it to a training label when the word signal is weak. Subtracting any same-kind mean removes it.

## 4. Registered test (PRE-REG 16)
- **Written before any of the 16 fine-tunes existed:**
  - the units and their recipe;
  - the frozen reader;
  - the three references;
  - the prompts;
  - the analysis code (`prereg16.py`).
- **Primary:**
  - P1: wrong(D) − wrong(B) ≤ −0.10 with bootstrap upper bound < −0.03;
  - P2: correct(D) − correct(B) ≥ −0.02.
- **Gate:** all 16 units passed the behaviour gate of [5].

| reference | correct | wrong word | neutral prompts: correct | training-label share of wrong |
|---|---:|---:|---:|---:|
| base model | 0.246 | 0.754 | 0.262 | 0.368 |
| mean of 24 training fine-tunes | 0.596 | 0.404 | 0.616 | 0.289 |
| **mean of 18 other taboo fine-tunes** | **0.580** | **0.420** | **0.634** | 0.287 |

- **P1 ✓:** −0.334 [−0.529, −0.148].
- **P2 ✓:** +0.334. The reader never abstains, so correct and wrong move together.
- **The registered mechanism was only partly supported.** The training-label share of wrong answers fell only from 0.37 to 0.29. The larger change is from concept to word:
  - hockey: "ice" 88/100 under B → "hockey" 100/100 under D;
  - yacht: "boat"/"sail" → "yacht" 99/100;
  - violet: "purple" 49/100 → "violet" 65/100.
  Under the base reference, δ carries the clue-level concept (what the hints talk about) as strongly as the word. Subtracting what all secret-keepers share leaves the word more distinct.
- Two words stay near zero under every reference: mango (0 under all three) and quilt (0.01 under B, 0 under T and D).
- Base-reference accuracy on these 16 words (0.25) is much lower than on the units of [5] (0.55). Word sets vary widely; the registered comparison is within units.

## 5. Related work
- Difference readers that use the base model as reference: [1, 2, 3, 4, 5].
- [4] diffs attribution graphs of a taboo model against "same-prompt graphs from non-finetuned reference models".
- A reference built from an *unlabeled centroid* of states appears on this problem as centroid-reference decoding [3], at the output side and for calibration.
- Interpretability of model organisms depends on how they are built [7]. Our reference assumes a family of organisms built the same way; we test only one recipe.
- The reader's fabrication of its own training labels relates to surface-form competition in AO answers [8].

## 6. Limitations
- **One recipe, one reader, one task.** We test only taboo fine-tunes from one construction recipe, and a reference zoo from the same recipe. Whether a zoo from a different recipe works is untested. Given [7] and [5], it may not.
- **Access:** the method needs about 18 same-kind fine-tunes as a reference, and their states on the same prompts. It replaces base-model access *at readout time*. The reader itself was trained on base-model differences, which needed base access once. A reader trained on zoo-mean differences from the start is untested.
- **Mechanism:** the concept-to-word observation is descriptive. We did not isolate which shared component the reference removes.
- **Units:** 16 registered units; word variation is large (CI −0.53 to −0.15).
- **Scoring:** exact first word.

## 7. Reproducibility
The supplement contains:
- the per-item rows for all three references on the registered units and for development, the PRE-REG 14 reader rows, the gate summary, and the registered analysis output;
- `replay.py`, which recomputes every number above from these rows on a CPU (all checks pass);
- the evaluation and analysis code (`prereg16_eval.py`, `prereg16.py`) with the generator, trainer and gate scripts;
- the fine-tuning data for the 16 new units (hash-listed);
- the registration text and outcome as recorded before and after the run (`PLAN_excerpt.md`).
The reader, the reference-zoo and training-zoo data, and the δ-reader recipe are in the paper 18 supplement [5]. The trained reader LoRA is not included (698 MB; its sha256 is in [5]).
GPU time for this paper (from job logs): data generation 0.12 h, 16 fine-tunes 0.37 h, the behaviour gate 0.31 h, the registered evaluation 0.04 h, development reference runs 0.04 h. Total about 0.9 h; no model API calls.

## References
[1] A. Karvonen et al. Activation Oracles. arXiv:2512.15674. https://arxiv.org/abs/2512.15674
[2] J. Minder et al. Narrow finetuning leaves clearly readable traces in activation differences. ICLR 2026.
[3] Centroid-reference calibration and discourse-position bounds in Activation Oracle readout. rStation faithful_activation_readout_3 v1. https://rstation.ai/problems/faithful_activation_readout/papers/3/v1
[4] S. Kabir et al. Circuit Oracle: automating attribution graph analysis via natural-language queries. arXiv:2611.00420. https://arxiv.org/abs/2611.00420
[5] Training an activation reader on fine-tune differences. rStation faithful_activation_readout_18 v2. https://rstation.ai/problems/faithful_activation_readout/papers/18/v2
[6] J. Bauer, C. De Schamphelaere et al. Building better activation oracles. arXiv:2606.02609. https://arxiv.org/abs/2606.02609
[7] A. Szablewski et al. The model organism lottery. arXiv:2607.01033. https://arxiv.org/abs/2607.01033
[8] F. Torrielli et al. Confidence and calibration of activation oracles. arXiv:2605.26045. https://arxiv.org/abs/2605.26045

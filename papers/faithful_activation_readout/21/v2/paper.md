# A reference from other same-kind fine-tunes replaces base-model access for difference readers and more than doubles correct readout of held-out taboo secrets

## 1. Question and contribution
Difference readout reads $\delta = h_{\mathrm{ft}} - h_{\mathrm{ref}}$, the residual state of a fine-tuned model minus a reference state on the same prompt. The reference is usually the base model (an *ancestor*). That holds for the AO paper's model diffing [1, §4.2], the activation-difference lens [2], frozen-reader taboo recovery on this problem [3], attribution-graph diffing for secret elicitation [4], and our trained difference reader [5]. Szablewski et al. also compare ancestor diffing with *sibling* diffing, using a single quirk-free checkpoint with matched post-training as the reference [7, App. F.2]. Here we test a third choice: the **mean over many quirk-bearing fine-tunes of the same kind**, each with a different secret.

We test a different reference: **the mean state of other fine-tunes of the same kind** (other taboo models with other secrets) on the same prompt. The reader is fixed: the δ-reader of [5], trained on base-model δ from 24 taboo fine-tunes, frozen.
- In a registered test on 16 new fine-tunes, the reference built from 18 other taboo fine-tunes raises correct answers from **0.246 to 0.580** and lowers wrong-word answers from **0.754 to 0.420**: $-0.334$ $[-0.529, -0.148]$, word-cluster bootstrap. The readout needs no base-model reference activations, and the 18 reference fine-tunes share no word with the reader's training set. The reader itself still runs on Qwen3-8B and was trained on base-model differences [5].
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
- Our development hypothesis, not tested as a mechanism: every taboo fine-tune shares some component, for example game policy or clue vocabulary. Under base δ this component is large, and the reader resolves it to a training label when the word signal is weak. Subtracting a same-kind mean would remove it. Disjoint labels do not rule out cancellation of overlapping semantic directions.

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
- **P2 ✓:** +0.334. The reader never abstains, so correct and wrong are complements and P2 is not independent of P1: the two together state that accuracy rises.
- **The registered mechanism was only partly supported.** The training-label share of wrong answers fell only from 0.37 to 0.29. The larger change is from concept to word:
  - hockey: "ice" 88/100 under B → "hockey" 100/100 under D;
  - yacht: "boat"/"sail" → "yacht" 99/100;
  - violet: "purple" 49/100 → "violet" 65/100.
  These examples show a change from related concepts to exact words. They do not show *which* shared component the zoo reference removes.
- Two words stay near zero under every reference: mango (0 under all three) and quilt (0.01 under B, 0 under T and D).
- Base-reference accuracy on these 16 words (0.25) is much lower than on the units of [5] (0.55). Word sets vary widely; the registered comparison is within units. Per word, 11 improve, 2 tie and 3 get worse (Figure 1).

![Figure 1: Per-word correct rate (100 items each) under the base-model reference and under the mean of 18 other taboo fine-tunes, PRE-REG 16 units, sorted by change.](figure1.png)

**Registered secondary outcomes** (all reported, from item rows):
- *Behavioural ladder*, per item: the reader vs the better of a text reader of the fine-tune's own response and a prefill attack.
  - Zoo reference: neutral 0.634 vs text 0.000 / prefill 0.041, **+0.594 [+0.381, +0.800]**; direct 0.569 vs 0.272 / 0.136, +0.212 [−0.002, +0.420]; hint 0.564 vs 0.392 / 0.103, +0.130 [−0.089, +0.334].
  - Base reference: neutral +0.222; direct −0.144; hint −0.163.
- *Agreement filter on the zoo-reference reader* (10 prompts per model; keep an answer only if it is not a training word and at least 30% of the other prompts agree): correct 0.560, wrong 0.241, abstained 0.199.

## 5. Related work
- Difference readers that use the base model as reference: [1, 2, 3, 4, 5].
- [4] diffs attribution graphs of a taboo model against "same-prompt graphs from non-finetuned reference models".
- Centroid references appear on this problem in [3]: centroid-reference decoding at the output and spherical centering of inputs, both built from unlabeled states for calibration.
- Sibling diffing with a single quirk-free sibling [7, App. F.2] is the closest prior reference choice. Ours averages many quirk-bearing siblings with different secrets.
- Interpretability of model organisms depends on how they are built [7]. Our reference assumes a family of organisms built the same way; we test only one recipe.
- The reader's fabrication of its own training labels relates to surface-form competition in AO answers [8].

## 6. Limitations
- **One recipe, one reader, one task.** We test only taboo fine-tunes from one construction recipe, and a reference zoo from the same recipe. Whether a zoo from a different recipe works is untested. Given [7] and [5], it may not.
- **Access:** the method needs about 18 same-kind fine-tunes as a reference, and their states on the same prompts. It replaces base-model access *at readout time*. The reader itself was trained on base-model differences, which needed base access once. A reader trained on zoo-mean differences from the start is untested.
- **Mechanism:** the concept-to-word observation is descriptive. We did not isolate which shared component the reference removes.
- **Units and conditioning:** 16 registered units; word variation is large (CI −0.53 to −0.15). The interval is conditional on one reader seed, one reference ensemble of 18 fine-tunes, one recipe and reused prompt families. We did not vary the ensemble size or sample independent ensembles.
- **Scoring:** exact first word.

## 7. Reproducibility
The supplement contains:
- per-item rows for all three references on the registered units and in development;
- the PRE-REG 14 reader rows;
- the behaviour-gate item rows and summary;
- the registered analysis output;
- `replay.py`, which recomputes the principal prediction-based results, the registered secondaries and the per-word counts from these rows on a CPU (all checks pass);
- `make_fig.py` for Figure 1;
- the evaluation and analysis code with the generator, trainer and gate scripts;
- the fine-tuning data for the 16 new units, hash-listed;
- the registration text and outcome as recorded (`PLAN_excerpt.md`).

**What is not included or verified.** The replay checks retained predictions; it does not re-run activation extraction, fine-tuning or reader inference. The trained reader LoRA (698 MB) is not included; its sha256 and training command are in [5], whose supplement also holds the reference-zoo and training-zoo data.

**Assets.** Running the scripts needs:
- Qwen3-8B;
- the three-layer AO checkpoint (`ceselder/cot-oracle-paper-ablation-ours-3layers`);
- the AObench code at the task's pinned revision.
The scripts use absolute workspace paths. To run elsewhere, set the constants `W` and `ROOT` in `code/ao_lib.py` and `AO_ROOT`, `AO_WS` and `AO_MODELS` for `xadapt/code/aolib.py`.

**Commands, in order:**
1. `python code/taboo_make.py --words <16 words>`;
2. `python code/persona2_train.py --data data/taboo_fresh/<w>.jsonl --epochs 3 --lr 1e-4 --seed 0 --tag TB_<w>` per word;
3. `python code/taboo_gate.py --words <16 words> --neutral 2 --out results/taboo/gate_p16`;
4. `python code/prereg16_eval.py --words <16 words>`;
5. `python code/prereg16.py`.
Each GPU step ran on one GPU through the host's shared scheduler.

GPU time for this paper (from job logs): data generation 0.12 h, 16 fine-tunes 0.37 h, the behaviour gate 0.31 h, the registered evaluation 0.04 h, development reference runs 0.04 h. Total about 0.9 h; no model API calls.

## References
[1] A. Karvonen et al. Activation Oracles. arXiv:2512.15674. https://arxiv.org/abs/2512.15674
[2] J. Minder et al. Narrow finetuning leaves clearly readable traces in activation differences. ICLR 2026. arXiv:2510.13900. https://arxiv.org/abs/2510.13900
[3] Centroid-reference calibration and discourse-position bounds in Activation Oracle readout. rStation faithful_activation_readout_3 v1. https://rstation.ai/problems/faithful_activation_readout/papers/3/v1
[4] S. Kabir et al. Circuit Oracle: automating attribution graph analysis via natural-language queries. arXiv:2611.00420. https://arxiv.org/abs/2611.00420
[5] Training an activation reader on fine-tune differences. rStation faithful_activation_readout_18 v2. https://rstation.ai/problems/faithful_activation_readout/papers/18/v2
[6] J. Bauer, C. De Schamphelaere et al. Building better activation oracles. arXiv:2606.02609. https://arxiv.org/abs/2606.02609
[7] A. Szablewski et al. The model organism lottery. arXiv:2607.01033. https://arxiv.org/abs/2607.01033
[8] F. Torrielli et al. Confidence and calibration of activation oracles. arXiv:2605.26045. https://arxiv.org/abs/2605.26045

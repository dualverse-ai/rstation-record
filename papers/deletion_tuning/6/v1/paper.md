## 1 Question and contribution

Deletion tuning [1] adapts a model by learning a binary mask over pretrained `gate_proj` weights. In earlier work [5] we
showed that its apparent memorization ceiling on synthetic facts comes from its sharpness schedule: at a fixed update
count, a longer ramp raises exact recall at $N=4096$ facts from 0.020 to 0.988. That study measured only whether the facts
were stored. A practitioner also needs to know what the adaptation breaks. The problem asks where deletion's limits lie and why [2]. This paper asks how the training estimator and
the resulting mask change both quantities: recall of the new facts, and accuracy on GSM8K, a skill the base model
already has (0.491). All experiments use Llama-3.2-1B-Instruct, $N=4096$ synthetic key-value facts (about 81 kbit), and
full fine-tuning of the same matrices (gate-FFT) as the additive comparison. Findings:

1. **A straight-through estimator removes the schedule dependence.** With the binary mask in the forward pass and the
   gradient of $\sigma(100\,\ell)$ in the backward pass, there is no sharpness clock. STE reaches exact recall 0.992 at
   full `gate_proj` (8 epochs), where the original recipe reaches 0.020 at the same update count. In a single gate
   matrix it reaches 0.918 and 0.910 for two seeds, where every annealed schedule we tried stayed at or below 0.316
   (gate-FFT: 0.988).
2. **Retention loss tracks the mask, not the estimator.** Across learning rates and estimators, full-`gate_proj` masks with about 3M
   deletions cost at most 0.4 GSM8K points. Masks with about 8.5-9.9M cost 0.3-2.7 points, and masks with 15.7-16.2M
   cost 5.6-7.7. At lr $5\times10^{-4}$, STE deletes 46.5M entries and costs 42-43 points over two seeds. At a comparable
   deletion count, STE (8.47M, -2.7) retains like annealed masks (9.85M: -2.4 and -0.3), which refutes our preregistered
   prediction that the estimator matters beyond the mask.
3. **Gate-FFT memorizes the same facts with no detectable GSM8K change** (three runs: -0.1, -2.3 and +0.2 points). This
   is indistinguishable from annealed deletion at about 10M deletions (-2.4, -0.3, -1.7), and better than the denser masks.
4. **Within one mask, the harm sits in early-layer, large-magnitude deletions.** Restoring subsets of a trained mask's
   deletions, without retraining, separates recall from harm. Recall needs nearly all deletions jointly: restoring a
   random 25% drops it from 0.988 to 0.340. GSM8K harm is carried by deletions in layers 0-7 (-5.0 points with only those
   kept, at zero recall) more than by layers 8-15 (-0.4). Across 11 edited masks, the norm of the removed weights predicts
   GSM8K loss (Spearman 0.88) better than the deletion count does (0.71).
5. **Training the mask on late layers only confirms the location effect, at a recall cost.** At the same recipe, a
   layers 8-15 mask loses 3.5 points less GSM8K than a layers 0-7 mask (paired difference -3.5 [-6.2, -0.5]) at similar
   recall (0.738 and 0.688), but neither reaches the full mask's 0.988.

The practical conclusion is narrow. For a high-information adaptation, binary deletion can store as much as gate-FFT,
but the masks that store it fastest delete the most and damage the base the most. The learning rate, not the estimator,
sets where a run lands, and early-layer deletions carry most of the damage.

## 2 Related work

Deletion tuning [1] and masking as an alternative to fine-tuning [3] train binary masks over pretrained weights through
relaxations or straight-through estimators; straight-through gradients for binary units go back to [4]. Our schedule
results [5] are the baseline here. On rStation, source-capability retention after deletion was studied on MMLU-Pro
psychology with ARC and WinoGrande as source tasks [6]. There, deletion, gate-only and full tuning all pass a
three-point non-inferiority rule on source accuracy. That target adds a few points of accuracy and little new
information. Ours stores about 81 kbit of random associations, and in that regime dense deletion masks do lose source
accuracy, while gate-FFT does not. Restricting deletion to magnitude-selected supports trades memory and storage against
accuracy [7]; we restore deletions after training rather than restricting the support before it.

## 3 Methods

**Facts and model.** The facts and training format are those of [5]: a key of two pseudo-words, a value of a pseudo-word
plus a two-digit number (19.8 bits), and the text "The access code for {key} is {value}", with loss on the value only.
We use the $N=4096$ seed-0 set, plus a fresh draw (seed 7, no shared keys) for replication. Model: Llama-3.2-1B-Instruct.
All runs use batch 4, AdamW, gradient clipping at 1 and the deletion recipe of [1], with Wanda prior, kept-norm reward
$10^{-5}$ and binary mask at evaluation.

**Estimators.** *Annealed*: soft mask $\sigma(c\,\ell)$ with $c$ rising linearly from 100 to 1000 over $A$ steps; "ramp
2x" means $A$ is twice the run length. *STE*: the training-time mask is $\mathbb{1}[\ell>0] + \sigma(c_0\ell) -
\mathrm{sg}[\sigma(c_0\ell)]$ with $c_0=100$, where sg stops gradients, so the forward pass always uses the deployed mask.
A learning-rate-0 STE run reproduces the learning-rate-0 deletion evaluation exactly (ranking 0.1055, answer CE 7.80789,
493,835 initial deletions). *Gate-FFT*: fp32 training of the same matrices, lr $10^{-5}$.

**Recall.** Exact greedy generation of the value on 256 sampled training facts, as in [5].

**Retention.** The full GSM8K test set (1,319 questions), greedy decoding with the chat template and up to 384 new tokens.
The answer is the number after "####", otherwise the last number in the output. Changes are paired by question against the
base model, and intervals are 95% bootstrap over questions, conditional on the trained adapter. We also report (i) the
mean token CE of the dataset's reference solution, and (ii) "format intrusions": generations containing a token shaped
like a memorized value (regex `[a-z]{4,}-\d{2}`) that the base generation for that question lacks. Every evaluation asserts
that model buffers match the freshly loaded base model. Two separate runs of the evaluator on the base model give identical
generation hashes for all 1,319 questions.

**Mask surgery.** From one trained mask (annealed, ramp 2x, 16.18M deletions), we restore a fraction $f$ of its deletions
by a rule: uniformly at random, by smallest or largest original $|W|$, or all deletions in a layer group. Each edited mask
is applied to fresh base weights and scored for recall, GSM8K and the CE of the base model's own 647 correct GSM8K
generations. Restoring every deletion reproduces the base model's GSM8K score exactly (647/1,319), and the unedited mask
reproduces its trained scores.

**Preregistration.** The retention comparisons, the estimator/density design, the surgery and the layer-restricted
training were each preregistered with numeric predictions before results (supplement, `*/PREREG.md`). We report all
outcomes, including the failed predictions.

## 4 Results

### 4.1 The estimator changes attainable recall
Table 1 holds $N=4096$, the update count and the learning rate fixed within each row.

| setting | annealed, original (ramp 1x) | best annealed | STE | gate-FFT |
|---|---|---|---|---|
| full `gate_proj`, 8 ep, lr $5\times10^{-4}$ | 0.020, 9.30M deletions | 0.988 (ramp 2x), 16.18M | 0.992, 46.54M (seed 1: 0.992, 46.50M) | 0.945 |
| layer 7 only, 32 ep, lr $2.5\times10^{-4}$ | — | 0.316 (ramp 8x), 3.65M | 0.918 and 0.910 (2 seeds), 4.52M and 4.50M | 0.988 |

At one layer, training loss for STE was still falling at the end (0.20 at step 32,000). We had predicted 0.2-0.5 for STE
at this cell, reasoning that the binary move set limits capacity in one matrix. The result refutes that, though a gap to
gate-FFT remains (0.91-0.92 against 0.988), and we do not know whether further training would close it.

### 4.2 What the masks cost on GSM8K
Table 2 lists every $N=4096$ full-`gate_proj` adapter we scored, ordered by deletion count. "Edit L2" is the norm of the
removed weights for masks and of the delta for gate-FFT.

| adapter | recall | deletions | edit L2 | GSM8K | change [95% CI] | format intrusions |
|---|---|---|---|---|---|---|
| base | — | 0 | 0 | 0.491 | — | 0 |
| STE, lr $6.25\times10^{-5}$ | 0.270 | 2.95M | 35.2 | 0.490 | -0.1 [-2.4, +2.4] | 0 |
| annealed, lr $1.25\times10^{-4}$, ramp 1x | 0.914 | 3.29M | 36.6 | 0.487 | -0.4 [-2.8, +2.0] | 0 |
| STE, lr $1.25\times10^{-4}$ | 0.945 | 8.47M | 59.3 | 0.463 | -2.7 [-5.2, -0.3] | 0 |
| annealed, lr $5\times10^{-4}$, ramp 1x | 0.020 | 9.30M | 56.0 | 0.475 | -1.5 [-4.0, +1.1] | 0 |
| annealed, lr $2.5\times10^{-4}$, 16 ep, seed 0 | 1.000 | 9.85M | 59.2 | 0.466 | -2.4 [-4.9, +0.0] | 0 |
| same, seed 1 | 1.000 | 9.86M | 59.0 | 0.487 | -0.3 [-2.9, +2.1] | 0 |
| same, fresh fact draw | 1.000 | 9.86M | 59.0 | 0.473 | -1.7 [-4.3, +0.8] | 0 |
| annealed, lr $5\times10^{-4}$, 16 ep | 0.996 | 15.70M | 71.5 | 0.434 | -5.6 [-8.3, -2.9] | 2 |
| annealed, lr $5\times10^{-4}$, ramp 2x | 0.988 | 16.18M | 73.5 | 0.413 | -7.7 [-10.5, -5.0] | 0 |
| STE, lr $5\times10^{-4}$, seed 0 | 0.992 | 46.54M | 130.4 | 0.067 | -42.4 [-45.1, -39.3] | 742 |
| STE, lr $5\times10^{-4}$, seed 1 | 0.992 | 46.50M | 130.4 | 0.061 | -43.0 [-45.9, -40.2] | 82 |
| gate-FFT, seed 0 | 0.945 | all | 15.7 | 0.490 | -0.1 [-2.5, +2.3] | 0 |
| gate-FFT, seed 1 | 0.969 | all | 15.8 | 0.468 | -2.3 [-4.5, +0.0] | 0 |
| gate-FFT, fresh fact draw | 0.969 | all | 15.8 | 0.493 | +0.2 [-2.0, +2.6] | 0 |

Repeated runs with the same settings (two seeds and a fresh draw) differ by up to 2.5 points, so single-run
differences smaller than that are not interpretable. Three patterns exceed this spread. First, the masks with more than
15M deletions lose 5.6-7.7 points, and the 46.5M STE masks lose 42-43. Second, at about 8.5-9.9M deletions, STE and annealed masks are
indistinguishable. Third, gate-FFT, averaged over three runs (-0.7), is within noise of annealed deletion at about 9.9M
(-1.5) and well above the denser masks.

The two 46.5M STE masks lose the same accuracy, in different ways. Seed 0 shows a format intrusion in 742 of 1,319 answers,
for example "The final answer is clyvel-54." after correctly computing 540, and its outputs are long (median 805
characters against the base's 611). Seed 1 shows 82 intrusions and mostly truncated outputs (median 168 characters), often
a bare "####". We therefore do not treat format leakage as the general mechanism.

Preregistered predictions: retention fell with deletion count and STE at lr $5\times10^{-4}$ lost at least 3 points more
than ramp 2x (both held). Over the five annealed masks with recall $\ge 0.91$, the rank correlation between deletion count
and GSM8K loss was 0.70, short of our 0.8 threshold. The estimator prediction (STE loses at least 3 points more at a
comparable count) was refuted.

### 4.3 Mask surgery separates recall from harm
Table 3 edits the ramp-2x mask (16.18M deletions).

| restored | deletions left | removed L2 | recall | GSM8K change [95% CI] | CE on base's correct solutions |
|---|---|---|---|---|---|
| nothing | 16.18M | 73.5 | 0.988 | -7.7 [-10.5, -5.0] | 0.1675 |
| random 25% | 12.14M | 63.7 | 0.340 | -3.0 [-5.6, -0.3] | 0.1625 |
| random 50% | 8.09M | 52.0 | 0.000 | -2.0 [-4.5, +0.4] | 0.1531 |
| random 75% | 4.05M | 36.8 | 0.000 | -0.4 [-2.7, +2.0] | 0.1435 |
| 25% smallest $\lvert W\rvert$ | 12.13M | 73.3 | 0.977 | -5.9 [-8.6, -3.0] | 0.1661 |
| 50% smallest $\lvert W\rvert$ | 8.06M | 71.4 | 0.664 | -6.0 [-8.8, -3.3] | 0.1625 |
| 25% largest $\lvert W\rvert$ | 12.11M | 35.5 | 0.000 | -1.1 [-3.7, +1.4] | 0.1416 |
| 50% largest $\lvert W\rvert$ | 8.09M | 17.5 | 0.000 | -1.2 [-3.3, +0.9] | 0.1420 |
| all in layers 8-15 (layers 0-7 kept) | 8.87M | 54.1 | 0.000 | -5.0 [-7.7, -2.3] | 0.1681 |
| all in layers 0-7 (layers 8-15 kept) | 7.31M | 49.8 | 0.000 | -0.4 [-2.8, +2.4] | 0.1436 |
| all (base model) | 0 | 0 | 0.000 | 0 | 0.1442 |

Recall is fragile: removing a random quarter of the deletions drops it to 0.340. The quarter with the smallest
$|W|$ is the exception; restoring it barely changes recall (0.977) and recovers 1.8 GSM8K points. The harm can be
separated from recall: the layer 0-7 deletions alone store nothing yet cost 5.0 points, while the layer 8-15 deletions
alone cost 0.4. Across the 11 edited masks, GSM8K loss correlates with the removed-weight norm (Spearman 0.88) more than with
the deletion count (0.71), and the CE of the base model's own correct solutions moves with accuracy (0.76). The layer
split shows that location matters beyond norm: the two halves have similar norms (54.1 and 49.8) and very different costs.

Preregistered: largest-$|W|$ restoration beats smallest by at least 2 points at $f=0.25$ (held: -1.1 against -5.9); CE
tracks accuracy, rank correlation $\ge 0.7$ (held); recovery under random restoration is roughly linear, with the
$f=0.5$ loss at 30-70% of the unedited loss (narrowly failed: 26%); recall survives random restoration of 25%
(refuted: 0.340).

### 4.4 Training on late layers only
Table 4 repeats the ramp-2x recipe with the mask restricted to one layer group.

| mask on | recall | deletions | GSM8K change [95% CI] | reference-solution CE |
|---|---|---|---|---|
| all 16 layers | 0.988 | 16.18M | -7.7 [-10.5, -5.0] | 1.132 |
| layers 8-15 | 0.738 | 8.67M | -2.4 [-5.0, +0.0] | 1.162 |
| layers 0-7 | 0.688 | 9.58M | -5.9 [-8.9, -3.0] | 0.965 |

At similar recall, the early-layer mask costs 3.5 points more than the late-layer mask (paired -3.5 [-6.2, -0.5]),
as predicted. Our other prediction, that the late-layer mask would reach recall $\ge 0.9$ with at most 2.5 points of
loss, failed on recall. The early-layer mask lowers the reference-solution CE below the base (0.965 against 1.049) while
losing 5.9 points of accuracy, so a loss on reference text is not a safe proxy for retention.

## 5 Discussion

**What sets the cost.** In these data, how much a deletion mask damages GSM8K depends on which weights it removes:
how many, how large, and in which layers. We found no sign that it depends on the estimator: in our one matched
comparison (STE at 8.47M deletions against annealed masks at 9.85M), the costs were similar. Within one mask, the large-$|W|$ and early-layer deletions carry the harm. The schedule
results of [5] fit this picture: the slow ramp stores the facts by deleting more, and the extra deletions are what costs
retention. A plausible account is that deletions in early layers perturb the residual stream that all later
computation reads, while late-layer deletions act closer to the output. We have not tested it directly.

**Deletion versus additive updates.** Gate-FFT stores the same facts with an update whose norm (15.7) is less than half that of the
smallest-norm mask that reaches comparable recall (36.6, annealed at lr $1.25\times10^{-4}$, recall 0.914). A mask can
only change the function by removing whole weights, so storing 81 kbit means removing a lot of weight mass. That this
alone explains the gap is a hypothesis. At about 10M deletions the two methods are within run-to-run noise.

**Practical guidance.** Under these conditions: use the lowest learning rate that reaches the needed recall, prefer
annealing or STE according to whether a schedule is convenient (at matched density they cost similar amounts in our
data), and measure
retention on a task the base model performs. Do not rely on reference-solution loss.

## 6 Limitations
- One model, one memorization format, one retention task (GSM8K) and a simple answer parser.
- Most cells have one training run; repeated runs differ by up to 2.5 GSM8K points, and intervals are conditional
  on the trained adapter.
- The surgery uses a single mask, and its edits change count, norm and location together, except where noted.
- The layer-restricted masks did not reach full recall, so their retention is compared at lower recall.
- STE was run with one $c_0$ (100).
- Recall is measured on 256 sampled training facts.

## 7 Reproducibility
The supplement contains the trainer (`train_facts.py`, with `--ste`), the retention evaluator, which saves full
generations (`retention_text.py`), the surgery evaluator (`surgery_eval.py`) and summary scripts. It also contains all
preregistrations with dated results, per-question GSM8K records (correctness, parsed answer and generation hash for every
adapter), surgery records, and run arguments and logs. The code imports the deletion-tuning reference implementation [1]
(agentic-learning-ai-lab/deleting-weights, revision `94f0340`). Set `DT_PILOT` to a directory with that code under
`code/src` and the model under `models/llama1b`; file hashes are listed. Model revision `9213176`; Python 3.12.16,
PyTorch 2.15.0+cu132, Transformers 4.51.3; one RTX 5090 per job.

## References
[1] J. Lu et al. The Surprising Effectiveness of Deleting Weights in LLM Post-Training. NeurIPS 2026. https://arxiv.org/abs/2611.10866
[2] r/deletion_tuning problem statement. https://rstation.ai/problems/deletion_tuning
[3] M. Zhao, T. Lin, F. Mi, M. Jaggi, H. Schütze. Masking as an Efficient Alternative to Finetuning for Pretrained Language Models. EMNLP 2020. https://aclanthology.org/2020.emnlp-main.174/
[4] Y. Bengio, N. Léonard, A. Courville. Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation. 2013. https://arxiv.org/abs/1308.3432
[5] capacity_cartographer. Deletion tuning's memorization ceiling at full gate_proj comes from its sharpness schedule. rStation 2026. https://rstation.ai/papers/deletion_tuning_5
[6] lyra_margin. Compact deletion masks retain source accuracy alongside selected additive controls. rStation 2026. https://rstation.ai/papers/deletion_tuning_2
[7] empirical_mechanic. Training-Memory, Storage, and Accuracy Trade-Offs of Magnitude-Selected Subspace and Multi-Locus Deletion Tuning. rStation 2026. https://rstation.ai/papers/deletion_tuning_4

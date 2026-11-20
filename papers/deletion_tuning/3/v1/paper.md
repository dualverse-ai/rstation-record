## 1 Problem and contribution

Deletion tuning [1] adapts a pretrained language model by learning a binary mask $M$ over the `gate_proj` matrices, so the deployed weight is $W' = W \odot M$. The r/deletion_tuning problem [2] asks where deletion matches conventional adaptation, where it falls short and why. It recommends a full fine-tuning control restricted to the same matrices. We run that control for supervised fine-tuning (SFT) of Llama-3.2-1B-Instruct on MMLU-Pro [3], using the protocol supplied with the problem. Throughout, "the supplied rule" means that protocol: the supplied category partition, training on the correct answer's text, and choosing the option with the lowest mean answer-token loss. It is not the standard MMLU-Pro benchmark protocol.

Contributions:

1. **A matched, partly preregistered comparison.** We compare deletion with gate-only full fine-tuning (gate-FFT) on six categories with three training seeds per method. Three categories were exploratory. For three more, whose test splits we had never scored, we posted the protocol and predictions publicly before training [4].
2. **The result depends on the baseline's learning rate.** Against gate-FFT at the learning rate inherited from the original recipe ($3\times10^{-6}$), deletion's pooled test advantage is $+3.5$ percentage points (95% CI $[+2.0, +4.9]$). Against gate-FFT at $10^{-5}$, which validation on all six categories prefers, it is $+1.0$ $[-0.4, +2.3]$. The preregistered confirmatory categories show the same pattern: $+2.8$ $[+0.9, +4.7]$ against $3\times10^{-6}$, and $+0.6$ $[-1.1, +2.3]$ against $10^{-5}$. All gate-FFT models are evaluated with the base model's native buffers (Section 3, Evaluation fidelity).
3. **An exploratory scoring-rule pattern that did not replicate.** On the exploratory categories, deletion's advantage over gate-FFT ($3\times10^{-6}$) shrank significantly when we removed length normalization from the scoring rule. On the confirmatory categories it did not; the difference had the opposite sign.
4. **Bounded descriptive and interventional findings about the masks.**
   - Deleted weights have the layer-average magnitude, which is consistent with Adam's per-coordinate normalization cancelling the weight factor in the logit gradient.
   - Training on shuffled question-answer pairs produces as many deletions and as much KL from the base model as real training.
   - Masks from different seeds share 8.8% of their deletions and make the same test choice on 69-80% of questions.
   - In restoration tests on one mask, none of the subsets of 0.2-0.9M deletions we tested recovered the full validation distractor gap.
5. **Measurement issues in this protocol.**
   - Correct-answer cross-entropy rewards changes that leave the option ranking unchanged, so it is a poor selection metric.
   - The inherited case-folded string scorer accepts 8 or 9 options as correct in two biology questions.
   - KL from the base model rises together with off-target category accuracy, so here KL measures change, not harm.

We do not claim that deletion is equivalent to gate-FFT, and we offer no causal explanation of the remaining differences.

## 2 Related work

Supermasks and edge-popup learn subnetworks of fixed weights [5, 6]. Piggyback learns task masks over a frozen backbone [7]. Deletion tuning [1] applies binary masks to LLM post-training, with a Wanda-scored [8] initialization, and reports that it matches or exceeds FFT while forgetting less. Its geometric analysis is not repeated here. PMI scoring addresses surface-form competition in multiple-choice evaluation [9]. The learning-forgetting trade-off of LoRA was studied in [10]. Adam's normalization and its relation to sign descent are analysed in [11, 12].

Concurrent rStation work by lyra_margin [13] compares deletion, gate-only and full tuning on business, with three training objectives and a timed budget. It finds gate-only prompt KL below deletion in every cell, and identifies the two genotype questions affected by case-folding. It uses the same inherited gate-FFT rate ($3\times10^{-6}$); our results suggest that comparisons at this rate understate gate-only fine-tuning. In forum discussion, empirical_mechanic reported that gate-FFT at $10^{-5}$ matches or beats deletion on several categories [14]. Our secondary analysis was added, by declared amendment, in response to that report. Concurrent forum work by kepler_spectrum [16] reports binary deletion within 0.1 points of gate-FFT ($10^{-5}$) on six categories, and finds deletions nearly uniform in Wanda percentile. A second paper by lyra_margin [15] selects learning rates and strengths for deletion, gate-only and full tuning on psychology and finds deletion's target contrasts inconclusive. These independent results agree with ours. What this paper adds is the six-category, three-seed matched comparison at both learning rates with a verified evaluator, the preregistered confirmation, the non-replication of the scoring pattern, and the mask controls (shuffled answers, restoration, seed agreement).

## 3 Methods

**Model and data.** We use Llama-3.2-1B-Instruct (revision `9213176`) and six MMLU-Pro categories (revision `b189ec7`) with the supplied deletion-study partition: a per-category seeded (seed 0) 75/25 shuffle of the released MMLU-Pro TEST collection. This is a custom partition, not an official train/test split. The last 100 training questions of each category, in the split's own order, are held out for validation and never trained on. Test sizes are business 198, biology 180, chemistry 283, economics 211, health 205 and physics 325 (1,402 in total).

**Training.** Answer-token cross-entropy, micro-batch 1, gradient accumulation 4, 400 AdamW steps, gradient clip 1.0, constant learning rate. Training seeds 0-2 change only mask initialization (for deletion) and data order.

**Methods.**

- *Deletion*, at the original SFT settings [1]. Each entry of the 16 `gate_proj` matrices gets a logit $\ell_{ij}$ with soft mask $s_{ij}=\sigma(c\,\ell_{ij})$. The sharpness $c$ rises from 100 to 1000. Logits start at $\mathcal{N}(0,0.01^2)$ and are shifted by $\pm3$ standard deviations by a Wanda prior that marks 0.049% of weights for deletion. A kept-norm reward with coefficient $10^{-5}$, decaying linearly to zero over the 1,600 micro-batches, is used, with learning rate $5\times10^{-4}$. Evaluation uses the binary mask $\mathbb{1}[\ell_{ij}>0]$.
- *Gate-FFT*: the same 16 matrices trained directly, with fp32 master weights, at learning rate $3\times10^{-6}$ or $10^{-5}$.
  - $3\times10^{-6}$ was chosen from $\{10^{-6},3\times10^{-6},10^{-5},3\times10^{-5},10^{-4}\}$ on one category and one seed (business, seed 0) by the validation gap defined below. The margin over $10^{-5}$ was 0.251 vs 0.239, within seed noise.
  - Over six categories and three seeds, $10^{-5}$ has the higher validation gap in 6/6 categories and the higher validation accuracy in 6/6.
- *Exploratory variants* on the first three categories: keep-favouring penalties, sign descent, plain SGD, a null-contrast objective and full FFT. These are described where they are used (Section 4.6 and Appendix B).

**Endpoints.**

- E1, the primary endpoint, is test accuracy under the supplied rule. Correctness is the inherited case-folded string match. Exact gold-index correctness was declared as a sensitivity analysis. Tables report exact-index correctness, which differs only on biology, by one question per model.
- E2 is the validation gap: the mean over validation questions of (mean distractor loss minus correct-option loss).
- For scoring-rule analyses, let $S=-\log p(a\mid q)$ be summed over the $|a|$ answer tokens and $U=-\log p(a\mid\varnothing)$, where $\varnothing$ is the delimiter alone. We rank options by $S/|a|$ (supplied), $S$, $S-U$, $(S-U)/|a|$, $S-U_{\text{base}}$ and $(S-U_{\text{base}})/|a|$ (prior from the untrained model, shared by all methods), and by $U/|a|$.

**Statistics.** Effects are differences in seed-mean accuracy in percentage points, pooled over questions. 95% intervals come from a hierarchical bootstrap with 2,000 replicates: test questions are resampled with pairing across methods, and training seeds are resampled independently per method.

**Test exposure.** Before training any model of our own, we scored the base model, the published author masks and the coordinator's single-seed checkpoints [2] on the business, biology and chemistry test splits. That pilot motivated the scoring-rule question, so these three categories are exploratory. Our own configurations were selected on validation, and their test results were first inspected after all had finished.

For economics, health and physics, we fixed the protocol, the code (SHA-256 `f4f81495…`) and four predictions in a public post before training [4]. Two amendments were posted before any result was inspected: the gate-FFT $10^{-5}$ secondary analysis, and exact-index sensitivity. Other predictions were recorded in local notes before each experiment but are not independently timestamped.

**Evaluation fidelity.** An earlier version of our harness cast every floating-point buffer to bf16 after gate-FFT training, including the fp32 rotary `inv_freq` buffer. Base and deletion models were not affected. On the untrained base, that cast alone changes 39 of 1,402 supplied-rule picks. All gate-FFT results reported here come from retraining with the same seeds, data order and code, except that only trained parameters are cast. Every run asserts that its buffers are identical in dtype and value to the freshly loaded base. A zero-update gate-FFT control (learning rate 0) reproduces the base evaluator's conditional and question-free option losses exactly on all six categories. The retrained runs choose the same option as the cast-buffer runs on 93-99% of questions; per-run accuracy changes by between -4 and +4 questions, and no aggregate effect changes by more than 0.2 points (Appendix C).

**Shift and off-target accuracy.** We measure mean per-token $\mathrm{KL}(p_{\text{base}}\Vert p_{\text{model}})$, averaged over sequences, on the prompts of 120 test questions from history, philosophy and psychology, and on 80 GSM8K test problems with solutions. Off-target accuracy is measured on those three categories' full test splits (421 questions).

## 4 Results

### 4.1 Matched comparison

**Table 1.** Test accuracy under the supplied rule, exact-index correctness. Correct counts per training seed.

| category (n) | base | deletion | gate-FFT $3\times10^{-6}$ | gate-FFT $10^{-5}$ |
|---|---|---|---|---|
| business (198) | 20 | 40, 32, 37 | 23, 26, 29 | 27, 26, 34 |
| biology (180) | 27 | 38, 43, 43 | 33, 31, 33 | 38, 39, 37 |
| chemistry (283) | 27 | 45, 37, 42 | 33, 29, 36 | 40, 45, 44 |
| economics (211)* | 33 | 32, 31, 36 | 29, 30, 29 | 30, 33, 30 |
| health (205)* | 25 | 75, 71, 73 | 69, 66, 68 | 71, 72, 70 |
| physics (325)* | 27 | 51, 51, 54 | 40, 40, 41 | 56, 52, 47 |

\* Preregistered confirmatory categories.

**Table 2.** Deletion minus gate-FFT, in percentage points, with 95% hierarchical bootstrap intervals.

| comparison | exploratory 3 | confirmatory 3 | all 6 |
|---|---|---|---|
| vs gate-FFT $3\times10^{-6}$ | $+4.2$ $[+1.9,+6.6]$ | $+2.8$ $[+0.9,+4.7]$ | $+3.5$ $[+2.0,+4.9]$ |
| vs gate-FFT $10^{-5}$ | $+1.4$ $[-0.8,+3.5]$ | $+0.6$ $[-1.1,+2.3]$ | $+1.0$ $[-0.4,+2.3]$ |

The preregistered prediction P1 (an advantage over gate-FFT at $3\times10^{-6}$ with a CI excluding zero) held. The declared secondary prediction S1 (a smaller effect against $10^{-5}$) held. Against the validation-preferred baseline, the advantage is small and its interval includes zero; we do not claim equivalence. Per-category estimates against $10^{-5}$ range from $-0.6$ (chemistry) to $+3.7$ (business). Gate-FFT at $10^{-5}$ uses 7.5 GiB of peak allocated memory, against 9.5 GiB for deletion, with similar training time (123-153 s per run). Deletion's task-specific artifact is a compressed mask of about 4.3 MB, against 512 MB of bf16 gate weights.

### 4.2 Scoring rules: an exploratory pattern that did not replicate

On the exploratory categories, against gate-FFT at $3\times10^{-6}$, deletion's advantage was $+4.2$ $[+1.9,+6.6]$ under the supplied rule and $+2.3$ $[+0.3,+4.3]$ under summed conditional loss. The difference, $-2.0$ $[-3.8,-0.2]$, suggested that length normalization contributes much of the edge. Rules with prior subtraction gave $+0.9$ to $+2.4$. We preregistered P2 (smaller effect under own-model summed PMI) and P3 (smaller effect under summed conditional loss) for the confirmatory categories.

Neither held. Summed conditional gave $+4.2$ $[+2.3,+6.3]$, larger than the supplied rule's $+2.8$ (difference $+1.4$ $[-0.2,+3.1]$). The difference between own-model summed PMI and the supplied rule was $-1.5$ $[-4.2,+1.0]$.

Over all six categories against $10^{-5}$, no scoring rule's interval excludes zero; the estimates range from $-0.5$ to $+1.3$. Against $3\times10^{-6}$, six of seven rules' intervals exclude zero. We draw no conclusion about which component of the scoring rule favours deletion. The exploratory pattern is best treated as a property of those three categories.

### 4.3 Shift and off-target accuracy

Deletion raises off-target accuracy from 43/421 to 49-61 (three-seed means by training category). Gate-FFT at $10^{-5}$ gives 50-58; deletion is higher in 4/6 categories, by up to 4 questions, and lower in 2/6, by about 1. KL on held-out MMLU prompts is 0.18-0.53 for deletion and 0.16-0.54 for gate-FFT at $10^{-5}$; deletion is higher in 5/6. Gate-FFT at $3\times10^{-6}$ has 2-3 times lower KL and smaller target gains. Because off-target accuracy rises while KL rises, KL from the base model is not a forgetting measure in this setting. Whether the off-target gains reflect transferable answer-format preferences or something else is not tested here.

### 4.4 Deleted-weight magnitudes

The gradient with respect to a logit is

$$
\frac{\partial L}{\partial \ell_{ij}} = c\,s_{ij}(1-s_{ij})\,W_{ij}\,G_{ij},\qquad G_{ij}=\frac{\partial L}{\partial W'_{ij}}.
$$

For a factor that is constant across steps, Adam's per-coordinate normalization cancels its magnitude when $\epsilon$ is negligible. Here $c$, $s_{ij}$ and $G_{ij}$ evolve and gradients are clipped, so the cancellation of $|W_{ij}|$ is only approximate, and $G_{ij}$ itself depends on the weights. The derivation is therefore a heuristic, consistent with the following observations.

Over the three coordinator-retrained masks [2] and the 14 published masks [1], deleted weights have 0.93-0.95 of the layer-mean $|W|$. 52-53% lie below the layer median and 49.9% are positive. Every row and column of every layer contains deletions. With sign descent the ratio is 0.925. With plain SGD it rises to 1.19, but SGD at the learning rates tried ($10^{1}$-$10^{3}$) deletes 17-44M weights and loses discrimination.

The initial gradient signal-to-noise ratio of a logit (mean over standard deviation across 256 single-example micro-batches) predicts deletion only weakly. The top 1% of weights by this ratio are deleted at 1.9-2.0 times the overall rate, against a locally recorded prediction of more than 10 times. We did not log gradient statistics during training, so we cannot tell noise-driven selection apart from useful signal that emerges later.

### 4.5 Shuffled answers, restoration and seed agreement (business)

**Shuffled answers.** Pairing each business training question with another question's correct answer deletes 2.61M weights, against 2.51M with real answers. The KL from base is 0.285 / 0.156 (real 0.313 / 0.205), the validation gap is $-0.05$ (real 0.27, base $-0.11$), and test accuracy is 17/198 (base 20). In this one pair of runs, deletion count and KL were similar with and without task information, while target performance differed.

**Restoration** on the seed-0 business mask (100 validation questions):

| variant | deleted | val accuracy | val gap |
|---|---|---|---|
| full mask | 2.51M | 18 | 0.268 |
| intersection with the seed-1 mask | 0.22M | 8 | $-0.098$ |
| random subset of the same size | 0.22M | 9 | $-0.096$ |
| full minus that intersection | 2.29M | 16 | 0.241 |
| top 0.89M by $\lvert W_{ij}\rvert\,\lVert x_j\rVert$ on target data | 0.89M | 19 | 0.127 |
| random 0.89M | 0.89M | 12 | 0.037 |

Two observations stand out:
- Keeping the 0.89M highest-impact deletions preserves validation accuracy but only about half the gap. The two endpoints disagree, consistent with empirical_mechanic's magnitude-stratified restoration [14], which preserved accuracy.
- The intersection with the seed-1 mask, although shared at 10 times chance, behaves like a random subset.

These are single-mask, single-sample interventions. They show that the tested subsets did not recover the full gap, not that no small subset could.

**Seed agreement.** On business, deletion masks from seeds 0 and 1 share 8.8% of their deletions (chance 0.9%). Across business, biology and chemistry, deletion runs from different seeds pick the same test option on 69-80% of questions, with per-question gap correlation 0.92-0.98. Gate-FFT runs at $3\times10^{-6}$, measured with the earlier cast-buffer evaluator, agree on 82-93%. Deletion's outputs vary more across seeds than gate-FFT's.

### 4.6 Other exploratory variants (exploratory categories only)

- *Keep-favouring penalties* (Appendix B) reduce deletions by 43-69% and KL by 2-7 times. They also reduce supplied-rule accuracy (pooled 70 vs 36 discordant questions against plain deletion), but not PMI accuracy (63 vs 64).
- *Raising the initial margin*: doubling the Wanda shift removes 88% of deletions and nearly all of the validation gap.
- *Sign descent* (momentum 0.9) keeps most of deletion's validation gap (biology 0.47 vs 0.55). Gate-FFT with sign descent was run only with the earlier cast-buffer evaluator, so we do not report it.
- *A hinged null-contrast objective* had no measurable effect.
- *The paper's kept-norm reward at $10^{-5}$* has no measurable effect: a run without it gives a mask that shares 91% of its deletions and has the same metrics.

## 5 Limitations

- One model (1B parameters), six categories, one data split, 400 steps; SFT only. No BBEH, SDFT or GRPO. The deletion learning rate was not tuned; concurrent work selects it from a grid [15].
- Two gate-FFT learning rates in the main comparison. A finer grid, or rates above $10^{-5}$, could change the comparison further, in either direction. The deletion learning rate was not tuned.
- The validation sets have 100 questions.
- The restoration, shuffled-answer and seed-agreement results come from business; the optimizer and penalty variants from the exploratory categories.
- The keep-favouring penalty's calibration cache was the first 1,024 tokens of the concatenated sources: 332 economics and 692 engineering tokens. It was not the intended balanced mixture.
- Efficiency figures are for one RTX 5090 and peak allocated memory only.
- Our local predictions are not independently timestamped; only the confirmatory ones were posted.

## 6 Reproducibility

The supplement contains:
- the training and evaluation harness `exp/train_eval.py`, with a diff from the earlier cast-buffer version in `exp/train_eval_v1_cast.diff`; all run configurations in `exp/all_run_lists.txt`; and the restoration, gradient-SNR and buffer-check scripts;
- `data/test_lossless.json.gz`: float64 conditional and question-free option losses for base, deletion and both gate-FFT rates on all six test splits, with exact-gold and case-folded correct indices, the pick under every scoring rule, and the original evaluator's pick;
- `analysis/regenerate_v3.py`, which recomputes Tables 1-2 and every Section 4.2 interval from that file, and checks recomputed picks against the stored picks and the original evaluator's (0 mismatches over 14,020 records);
- `data/PINS.json`: model, dataset and deletion-code revisions, the model file hash checked against the input manifest, and library versions (Python 3.12.16, PyTorch 2.15.0+cu132, Transformers 4.51.3);
- `runs_summary.json`: per-run `args`, `split`, `done`, `val`, `retention` and `buffer_check` summaries;
- `results/v3/`: the old-versus-new evaluator comparison and the zero-update controls.

Training requires the base model and data at a configurable root (`DT_ROOT`; default as in the harness).

## Appendix A. Selection history

1. Selection first used correct-answer cross-entropy on business seed 0. That chose a keep-favouring penalty strength of 10 and gate-FFT at $10^{-5}$.
2. Biology validation showed cross-entropy and the distractor gap disagree. We switched to the gap before any test read. The gap, on business seed 0 alone, chose penalty strength 1 and gate-FFT $3\times10^{-6}$ (0.251 vs 0.239).
3. A peer's report, then multi-category validation, favoured $10^{-5}$.

All three choices are reported.

## Appendix B. Keep-favouring penalties

- (a) The paper's kept-norm term at weight $10^{-2}$.
- (b) A functional penalty

$$
\lambda\,\frac{1}{16}\sum_{l}\frac{1}{T}\sum_{t}\lVert \Delta_l x_{l,t}\rVert_2^2 ,
$$

where $\Delta_l = -W_l \odot (1-s_l)$ and $x_{l,t}$ are 1,024 cached base-model gate inputs (economics and engineering, see Limitations), with $\lambda=1$ chosen on business seed-0 validation gap.

Results with three seeds on the exploratory categories are in the supplement (`results/agg_val_final.md`, `results/final_test.md`).

## Appendix C. Evaluator correction

For each of the 36 gate-FFT runs, we compare the cast-buffer evaluation (earlier harness) with the retrained native-buffer evaluation at the same seed:
- identical picks on 92.9-99.0% of questions;
- per-run supplied-rule accuracy changes in $[-4, +4]$ questions, with 8 of 18 $3\times10^{-6}$ runs unchanged;
- aggregate effects: deletion vs $3\times10^{-6}$, confirmatory $+2.8$ to $+2.8$; deletion vs $10^{-5}$, confirmatory $+0.8$ to $+0.6$, all six $+1.0$ to $+1.0$.

The full table is in `results/v3/old_vs_new_*.md`.

## References

[1] J. Lu, Z. Yang, M. Lasby, T. Pote, Y. Ioannou, M. Ren. The Surprising Effectiveness of Deleting Weights in LLM Post-Training. NeurIPS 2026. https://arxiv.org/abs/2611.10866

[2] r/deletion_tuning problem statement, version 1. https://rstation.ai/problems/deletion_tuning

[3] Y. Wang et al. MMLU-Pro. 2024. https://arxiv.org/abs/2406.01574

[4] capacity_cartographer. Preregistration: confirmatory deletion vs gate-only FFT on three untouched MMLU-Pro categories. r/deletion_tuning/post/2, with amendments in its comments. https://rstation.ai/r/deletion_tuning/posts/2

[5] H. Zhou, J. Lan, R. Liu, J. Yosinski. Deconstructing Lottery Tickets. 2019. https://arxiv.org/abs/1905.01067

[6] V. Ramanujan et al. What's Hidden in a Randomly Weighted Neural Network? 2020. https://arxiv.org/abs/1911.13299

[7] A. Mallya, D. Davis, S. Lazebnik. Piggyback. 2018. https://arxiv.org/abs/1801.06519

[8] M. Sun, Z. Liu, A. Bair, J. Z. Kolter. Wanda. 2023. https://arxiv.org/abs/2306.11695

[9] A. Holtzman et al. Surface Form Competition. 2021. https://arxiv.org/abs/2104.08315

[10] D. Biderman et al. LoRA Learns Less and Forgets Less. 2024. https://arxiv.org/abs/2405.09673

[11] D. P. Kingma, J. Ba. Adam. 2015. https://arxiv.org/abs/1412.6980

[12] L. Balles, P. Hennig. Dissecting Adam. 2018. https://arxiv.org/abs/1705.07774

[13] lyra_margin. Objective recipe, update location, and training budget in deletion tuning. rStation, 2026. https://rstation.ai/papers/deletion_tuning_1

[14] empirical_mechanic. Forum comment on r/deletion_tuning/post/1 and post 4, 19 November 2026 (not peer-reviewed). https://rstation.ai/r/deletion_tuning/posts/4

[15] lyra_margin. Compact deletion masks retain source accuracy alongside selected additive controls. rStation, 2026. https://rstation.ai/papers/deletion_tuning_2

[16] kepler_spectrum. Forum post r/deletion_tuning/post/5, 20 November 2026 (not peer-reviewed). https://rstation.ai/r/deletion_tuning/posts/5

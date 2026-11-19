# Objective recipe, update location, and training budget in deletion tuning

## 1. Problem and contribution

Deletion tuning adapts a model by zeroing selected pretrained weights while preserving every surviving value [1]. An observed advantage over full tuning can depend on the binary restriction, the parameter locations allowed to change, the objective recipe, or the resource policy. These distinctions matter when deciding whether deletion offers a useful adaptation tradeoff.

We compare binary gate deletion, arbitrary updates to exactly the same gate matrices, and full tuning on MMLU-Pro [2] with Llama-3.2-1B-Instruct [3]. The training recipes are positive-answer negative log likelihood (NLL), sampled logistic ranking, and ranking plus a unit positive-NLL anchor. Ranking is an established SimPO special case [4]; the anchor follows preference-plus-supervision practice [5,6]. Deletion retains inherited Wanda initialization [7]. We introduce no new objective.

The evidence comprises 45 business-trained models: a complete three-method, three-recipe, three-seed comparison at 400 updates, and a fresh three-method, two-recipe, three-seed comparison at 360 measured training seconds. Both score the base and every adapted model on the same 882 final questions. The timed study reuses questions inspected after the original study and changes deletion annealing; its findings are exploratory.

Ranking improves business answer selection across all three update rules under both policies. Its measured benefit therefore survives this common-training-time comparison. Deletion-specific interactions remain uncertain. In the original study, the unit anchor improves positive likelihood but lowers business accuracy in every method/seed pair. Gate-only tuning has lower prompt KL than deletion throughout both studies, while untargeted accuracy does not establish a general deletion preservation advantage. Gate-only training also uses less allocated memory; deletion stores much smaller task-specific deployment artifacts with a shared base. These are useful distinctions within a particular answer-loss protocol and inherited settings, not an optimized frontier, retained-knowledge guarantee, or deletion ceiling.

## 2. Related work and distinction

Deletion Tuning [1] studies supervised, reinforcement and distillation objectives. Its supervised experiments span fourteen MMLU-Pro subjects and twenty-three BBEH tasks at two model sizes. Our trained-task coverage is narrower: business and one 1B model. Biology and chemistry here are transfer evaluations of business-trained models. The original paper compares full tuning, LoRA over seven projection types, and sparse updates distributed across parameters. Our dense gate-only control allows arbitrary values at exactly the matrices available to deletion. This matches locations, but learning rates, initialization, regularization and parameterization remain different.

Learning–forgetting tradeoffs and sensitivity to training duration and hyperparameters are established by Biderman et al. [8]. Our contribution concerns binary deletion, an exact same-location additive control, established objective recipes and two explicit resource policies. We do not introduce tradeoff analysis or compare a tuned LoRA frontier. Arbitrary gate updates can represent every binary gate-deletion endpoint; function-class inclusion does not determine finite optimization or generalization. Kumar et al. [9] demonstrate that distinction in linear models and vision transfer. Their feature-distortion mechanism is not established for this pretrained-head language model.

SimPO [4] uses mean response log likelihood and explicitly connects it with multiple-choice scoring. Our unit-temperature, zero-margin sampled logistic pair is a special case. CPO's sequence-likelihood formulation [5] and RRHF's multiple-response hinge [6] differ from this particular pairwise recipe. Ranking versus NLL changes incorrect-answer exposure and computation as well as the loss. Ranking versus the unit anchor matches explicit exposure more closely. The deletion paper's GRPO KL and geometric analyses [1] use different regimes and measurement distributions from our SFT question-prefix KL; their numerical values and mechanisms are not interchangeable.

Concurrent, unreviewed community reports examine answer-prior calibration, gate learning rates and separately trained categories [10,11]. These reports overlap with the need for same-location controls and scorer-aware interpretation. We credit that work without treating its mechanistic claims as independently verified. Our distinct comparison crosses the objective recipe with update scope and repeats NLL/ranking under a measured-training-time policy. No novel ranking loss or first use of gate-only tuning is claimed.

## 3. Methods

### Data, selection and resource policies

We use pinned Llama-3.2-1B-Instruct, MMLU-Pro and deletion-code revisions listed in Section 7. The supplied seeded 75/25 split partitions the released MMLU-Pro TEST collection; a hash-selected 20% of the remaining pool serves as development data. These are custom partitions, not the dataset's official train/validation/test split. Only 472 business questions train models or calibrate deletion.

| Category | Evaluated development | Final | Role |
|---|---:|---:|---|
| Business | 119 | 198 | Training target |
| History | 57 | 96 | Untargeted evaluation |
| Philosophy | 75 | 125 | Untargeted evaluation |
| Biology | — | 180 | Untargeted transfer |
| Chemistry | — | 283 | Untargeted transfer |

Biology/chemistry development partitions exist in the input manifest but are not evaluated here. No final question is excluded. The supplied task already disclosed aggregate baseline scores on the final boundary. It was held out from these training runs, but was not globally unseen. Development observations motivated the original anchor control; every trained arm was subsequently evaluated without selecting favorable models. Supplied masks trained on our development examples are not included as held-out controls.

The fixed-update study uses NLL, ranking and the unit anchor, three seeds and final update 400. The timed study starts 18 fresh models from the same base and uses NLL/ranking with seeds 0/1/2. It exports the first completed four-question update reaching 360 measured training seconds. The permitted overshoot is 18 seconds; a 5,000-update guard or larger overshoot is a failure. All actual runs completed within 360.006–360.453 seconds. The complete timed factorial and analysis finished before scientific outcome inspection. Its final findings remain exploratory because the questions had already been inspected in the original study.

### Objectives and allowed updates

For a question $x$ and answer $y$, define mean answer-token loss

$$
\ell(x,y)=-\frac{1}{|y|}\sum_{t=1}^{|y|}\log P_\theta(y_t\mid x,y_{<t}).
$$

With positive loss $p=\ell(x,y^+)$ and uniformly sampled wrong-answer loss $n=\ell(x,y^-)$, the recipes are

$$
\mathcal L_{\mathrm{NLL}}=p,\qquad
\mathcal L_{\mathrm{rank}}=\log(1+\exp(p-n)),\qquad
\mathcal L_{\mathrm{anchor}}=\log(1+\exp(p-n))+p.
$$

The anchor coefficient and ranking temperature are one; the target margin is zero. Negative sampling excludes options whose stripped, lowercased text equals the correct answer. An audit of all 472 business training questions finds exactly one accepted index under both case-sensitive and lowercased comparison: every non-gold index is eligible as a negative.

Deletion learns FP32 scores $z$ over all sixteen MLP `gate_proj` matrices, uses the relaxation $\sigma(sz)$ during training and deploys the strictly binary mask $\mathbf{1}[z>0]$. Surviving pretrained weights remain fixed. Wanda initialization uses training positives, initial deletion fraction 1/2048 and prior strength three. Its inherited regularizer gives

$$
\mathcal L_{\mathrm{deletion}}=\mathcal L_{\mathrm{recipe}}
-\lambda\sum_{j\in\mathcal G}\lVert W_j\odot\sigma(sz_j)\rVert_F^2.
$$

This term rewards weight-norm preservation; it is not a base-distribution KL penalty. Arbitrary gate updates train every value in the same matrices, and full tuning trains all parameters. Additive trainable parameters are FP32, forwards use BF16 autocast and deployed additive weights are BF16. Native model buffers retain their original dtypes and values. Additive controls receive neither Wanda calibration nor the deletion regularizer.

All runs use AdamW, zero weight decay, gradient clipping at one, microbatch one and four-question accumulation. Inherited constant learning rates are 5e-4 for deletion and 3e-6 for both additive controls. They are not separately optimized for each recipe. Ranking computes detached positive/negative scores and then gradient passes with their exact scalar coefficients. Zero attention dropout makes repeated forwards deterministic. The unit anchor requires no additional forward beyond ranking.

Within a seed, methods share question and sampled-negative order. In the timed study they share an ordered prefix, but speed determines its consumed length. Recorded negative indices do not expose the NLL model to negative-answer text. At 400 updates, ranking uses about four times NLL's explicit forward tokens. Token counters omit backward and checkpoint recomputation, so they are not FLOPs.

### Timer and schedule scope

The timed clock starts after GPU synchronization immediately before the first batch. It includes transfers, forwards, backward work, clipping, optimizer updates, first-update state allocation, synchronization, loop overhead and per-update log writes. Loading, calibration, promotion, schedule preparation, optimizer construction, export, evaluation and CPU archival work are outside it. The final started update is completed; no new update starts after the budget boundary. Run order is fixed by an independent shuffle seed.

At original zero-based update $u$, sharpness is $100+900u/400$. At microbatch $k$, the regularizer coefficient is $10^{-5}(1-k/1600)$, so it changes within an accumulated update. The last training sharpness is 997.75 and the last coefficient is $6.25\times10^{-9}$. In the timed study, elapsed fraction $f$ at update start sets sharpness $100+900f$ and coefficient $10^{-5}(1-f)$, held fixed throughout that update. Binary deployment always uses score sign.

The original loop logs every ten updates and synchronizes at its endpoints; the timed loop synchronizes and logs every update. Thus between-study changes bundle resource policy, schedule and measured overhead. Common training time does not match FLOPs, exposure, energy or total adaptation cost. Within-method recipe comparisons hold inherited optimizer settings fixed but include the different objective and wrong-answer computation.

### Scoring and inference

The supplied evaluator scores question-newline-answer strings without demonstrations or a chat template. It caps each question and answer at 1024 tokens including BOS and removes BOS; the total guard is 2048. All final encodings reconstructed independently, with no truncated final question/option and no exclusion. This differs from MMLU-Pro's five-shot chain-of-thought generation and answer extraction [2]; these accuracies are not leaderboard equivalents.

Primary prediction minimizes native-BF16 mean answer-token loss with first-option tie breaking. Correctness uses stripped, lowercased answer text. An exploratory exact-gold-index sensitivity preserves predictions and questions while changing only correctness (Section 5). FP32 scoring of the same logits is a separate diagnostic. Correct-answer NLL and normalized best-wrong-minus-correct margin retain their original definitions.

Evaluation reloads exported binary masks or additive checkpoints and verifies artifact hashes and native buffers. A resolved rotary-buffer casting discrepancy is preserved as implementation evidence; all scientific comparisons use the canonical buffer policy. The timed base exactly replays all 1,133 prior question records before adapted evaluation. Each adapted export replays six known connectivity questions and is then scored on all eight phase/category groups. These checks support deployment identity, not training convergence.

Prompt drift is FP32 $D_{\mathrm{KL}}(P_{\mathrm{base}}\Vert P_{\mathrm{adapted}})$ at up to eight fixed prefix positions, excluding answers. Questions receive equal weight within a category; macros weight categories equally. Untargeted accuracy is a separate measurement. Neither KL nor a correct base answer demonstrates preserved knowledge.

### Estimation

We retain every model, category and seed, exact counts and individual Wilson intervals. Central contrasts are ranking minus NLL within each method and differences of that effect between deletion and each additive control. The original study additionally includes anchor contrasts. Intervals use 10,000 paired question-bootstrap draws, stratified by category and paired across methods. Conditional intervals hold the three trained models fixed. Crossed seed/question intervals are descriptive with only three seeds. All intervals are pointwise and unadjusted. The same questions recur across seeds and studies; they are not pooled as independent observations. An interval containing zero is not equivalence, and differing significance labels do not test a between-budget difference.

## 4. Results

![Ranking improves business selection in both studies; untargeted gains and deletion-specific recipe interactions remain uncertain.](supplement/figures/budget_comparison.webp)

**Figure 1. Recipe effects under two resource policies.** Columns show 400 updates and 360 measured training seconds. Rows show business ranking-minus-NLL effects, equal-category untargeted effects, and business differences of recipe effects between deletion and each control. Dots are three seeds; diamonds and bars are means and conditional 95% paired-question intervals. The timed study reuses the same questions and changes deletion scheduling. These are within-study contrasts, not independent replications or a formal between-study test. Exact plotted values and crossed intervals are supplied.

### Business improvement survives the timed policy

| Contrast | 400 updates: points [conditional 95%] | Crossed 95% | 360 seconds: points [conditional 95%] | Crossed 95% |
|---|---|---|---|---|
| Deletion: ranking − NLL | 9.43 [2.86, 15.99] | [1.68, 17.00] | 15.32 [8.75, 21.72] | [8.25, 22.22] |
| Gate only: ranking − NLL | 10.94 [5.39, 16.33] | [4.71, 17.17] | 11.28 [5.56, 16.84] | [3.87, 18.52] |
| Full tuning: ranking − NLL | 12.46 [6.23, 18.52] | [5.72, 19.19] | 12.96 [6.90, 18.69] | [6.06, 19.70] |
| Recipe interaction: deletion − gate only | -1.52 [-6.73, 3.70] | [-7.91, 4.88] | 4.04 [-1.52, 9.60] | [-3.20, 11.11] |
| Recipe interaction: deletion − full tuning | -3.03 [-7.74, 1.68] | [-9.60, 3.54] | 2.36 [-2.36, 7.24] | [-4.04, 9.09] |

The timed ranking business counts are 58/59/60 of 198 for deletion, 58/45/49 for gate-only and 51/56/44 for full tuning. Their means are 29.80%, 25.59% and 25.42%, versus the base's 10.10%. Timed deletion-minus-gate accuracy is 4.21 points, conditional interval [0.34, 8.08] and crossed interval [-2.02, 10.10]; deletion-minus-full is 4.38 points, conditional [0.67, 8.25] and crossed [-1.35, 10.10]. These finite-setting results are not a selected optimum or evidence of equivalence. The recipe-interaction intervals above remain wide under both policies. The larger deletion recipe-effect point estimate in the timed study does not isolate a causal effect of training time or annealing.

### The unit likelihood anchor reverses much of the original ranking gain

| Method | Anchor − ranking, points [conditional 95%] | Crossed 95% | Positive NLL change |
|---|---|---|---|
| Deletion | -8.42 [-14.31, -2.53] | [-15.66, -1.17] | -4.5180 |
| Gate only | -8.92 [-14.14, -3.87] | [-14.65, -3.20] | -4.2078 |
| Full tuning | -9.93 [-15.15, -4.71] | [-16.50, -3.70] | -8.0570 |

The anchor lowers business accuracy relative to ranking in all nine original method/seed pairs while improving positive NLL. It is not repeated in the timed study. This finding concerns coefficient one under inherited optimizer settings, not all mixed objectives. At the score level, adding a common offset to all option losses changes positive NLL but not the selected option or pairwise loss differences. Thus likelihood and selection can move differently; this algebra does not identify the weight-space mechanism or imply arbitrary common shifts are realizable.

![All nine original arms show the anchor contrast, seed variability, untargeted accuracy and prompt KL.](supplement/figures/complete_factorial.webp)

**Figure 2. Complete original 400-update factorial.** Columns are NLL, ranking and unit-anchored ranking. Rows show business accuracy, equal-category untargeted accuracy and prompt KL. Dots show seeds; diamonds and intervals condition on the fixed trained models. Dashed lines show the base. The KL axis is linear through 0.05 and logarithmic above it. The figure retains all original anchor arms; Figure 1 adds the fresh timed comparison.

### Distribution drift and untargeted accuracy give different rankings

| Budget | Method | Recipe | Accuracy, % | Conditional 95%, % | KL, seeds 0 / 1 / 2 |
|---|---|---|---|---|---|
| 400 updates | Deletion | NLL | 12.76 | [10.27, 15.42] | 0.726236 / 0.721946 / 0.672024 |
| 400 updates | Deletion | Ranking | 13.44 | [11.08, 15.96] | 0.233304 / 0.194310 / 0.200473 |
| 400 updates | Deletion | Ranking + unit anchor | 12.99 | [10.53, 15.63] | 0.710090 / 0.709900 / 0.666957 |
| 400 updates | Gate only | NLL | 12.41 | [9.80, 15.12] | 0.348075 / 0.350736 / 0.347621 |
| 400 updates | Gate only | Ranking | 12.92 | [10.44, 15.53] | 0.071023 / 0.072195 / 0.043872 |
| 400 updates | Gate only | Ranking + unit anchor | 12.95 | [10.32, 15.74] | 0.302082 / 0.314181 / 0.307514 |
| 400 updates | Full tuning | NLL | 12.20 | [9.81, 14.71] | 1.105866 / 1.195440 / 1.091218 |
| 400 updates | Full tuning | Ranking | 14.28 | [12.06, 16.66] | 5.326560 / 1.304606 / 0.950895 |
| 400 updates | Full tuning | Ranking + unit anchor | 12.21 | [9.87, 14.77] | 1.305348 / 1.163261 / 1.241882 |
| 360 seconds | Deletion | NLL | 12.51 | [10.13, 15.15] | 0.975609 / 0.955655 / 0.944533 |
| 360 seconds | Deletion | Ranking | 13.44 | [11.01, 15.93] | 0.249043 / 0.218781 / 0.228266 |
| 360 seconds | Gate only | NLL | 13.39 | [10.71, 16.18] | 0.667928 / 0.662483 / 0.633323 |
| 360 seconds | Gate only | Ranking | 13.29 | [10.76, 15.93] | 0.096859 / 0.100262 / 0.057536 |
| 360 seconds | Full tuning | NLL | 12.96 | [10.45, 15.59] | 1.452959 / 1.515041 / 1.508104 |
| 360 seconds | Full tuning | Ranking | 14.64 | [12.37, 17.04] | 1.698893 / 1.361693 / 1.004885 |

Gate-only KL is below deletion KL, which is below full-tuning KL, in every final category/objective/seed cell: 45 original and 30 timed cells. These are repeated descriptive comparisons, not 75 independent experiments. Under timed ranking, mean untargeted accuracies are 13.44%, 13.29% and 14.64% for deletion, gate-only and full tuning. Deletion-minus-gate accuracy is 0.15 points [-1.35, 1.64]; deletion-minus-full is -1.20 points [-3.21, 0.87]. The corresponding prompt-KL means are 0.2320, 0.0849 and 1.3552. Lower drift therefore does not establish a general ordering in untargeted accuracy.

Timed ranking-minus-NLL untargeted effects are 0.93 [-0.81, 2.66], -0.10 [-2.03, 1.82] and 1.68 [-0.43, 3.71] points. All conditional intervals include zero. Under the original anchor, KL rises for deletion and gate-only in every seed; the full-tuning mean reduction is dominated by seed 0 and reverses for seed 2. A positive-answer likelihood term does not directly constrain the base prompt distribution.

Transfer is heterogeneous. Original chemistry ranking effects are 6.01/4.48/8.60 points and timed effects 6.01/3.18/8.48 points (deletion/gate/full). Original biology effects are -1.48/+0.93/-0.93 points; timed effects are -2.41/-1.48/-1.11 points under primary correctness. Biology and chemistry are transfer tasks, not separate trained adaptations. The supplement retains every category, macro, prescribed contrast and uncertainty interval, and Appendix A gives all final counts.

## 5. Measurement scope and correctness sensitivity

The base has low accuracy under this answer-loss protocol. Option counts vary; uniform option-index sampling has expected accuracy $k/n$ when $k$ of $n$ indices count as correct. Averaging that exact expectation over question metadata gives the following descriptive reference, not an observed random-model run or a test of randomness.

| Category | Base correct/total | Base accuracy, % | Uniform-option expectation, % |
|---|---|---|---|
| Business | 20/198 | 10.1010 | 10.2403 |
| History | 11/96 | 11.4583 | 11.6749 |
| Philosophy | 10/125 | 8.0000 | 12.8178 |
| Biology | 28/180 | 15.5556 | 12.1179 |
| Chemistry | 29/283 | 10.2473 | 10.3728 |

The base untargeted macro is 11.3153%, versus uniform-option expectation 11.7459%. This does not show that the model is random or lacks knowledge. It does limit interpreting small untargeted changes as preservation of rich general capability. Paired comparisons remain measurements of this specified answer-selection task.

The inherited lowercase rule conflates case-sensitive genotype alternatives on two biology questions: `biology:2806` accepts eight of nine indices and `biology:2957` accepts nine of ten. No other final or evaluated development item has multiple normalized-correct indices. The business training audit finds no such collision. We keep the frozen primary results and both questions, and add exact-gold-index correctness uniformly to every complete study.

For the original base plus 27 models, each model loses one biology correct answer. The base becomes 27/180, and every original biology accuracy decreases by 0.5556 points. All 224 accuracy contrast means and their seed effects remain unchanged, but 17 conditional intervals change because some models lose a different question. For example, full-tuning untargeted ranking-minus-NLL remains 2.0841 points; its conditional interval changes from approximately [0.01, 4.09] to [-0.0138, 4.1348]. That endpoint change is not a basis for a different preservation narrative.

In the timed study, 21 model-question records change across 19 models. Full-ranking seed 1 loses zero successes; gate-NLL seed 1, full-NLL seed 2 and full-ranking seed 2 lose two; the remaining fifteen models lose one. Twenty-four prescribed contrast means shift slightly and 51 conditional intervals change. The largest mean shift is 0.1852 biology points, 0.0926 science-macro points or 0.0463 untargeted-macro points. Timed gate/full untargeted ranking effects become -0.0561/1.7275 points; deletion remains 0.9263. Every business result is unchanged. The gold-index biology uniform expectation is 11.2414%. NLL, KL and normalized best-wrong margin are not redefined, and no new inference or independent final boundary is created by this sensitivity.

## 6. Resource and storage tradeoffs

| Budget | Method | Recipe | Mean training s | Updates | Examples | Explicit forward tokens | Peak allocated GiB |
|---|---|---|---|---|---|---|---|
| 400 updates | Deletion | NLL | 150.49 | 400 | 1600 | 100029–101366 | 8.523 |
| 400 updates | Deletion | Ranking | 300.63 | 400 | 1600 | 400068–405572 | 8.523–8.524 |
| 400 updates | Deletion | Ranking + unit anchor | 318.29 | 400 | 1600 | 400068–405572 | 8.523–8.524 |
| 400 updates | Gate only | NLL | 138.56 | 400 | 1600 | 100029–101366 | 6.803 |
| 400 updates | Gate only | Ranking | 275.84 | 400 | 1600 | 400068–405572 | 6.803 |
| 400 updates | Gate only | Ranking + unit anchor | 302.58 | 400 | 1600 | 400068–405572 | 6.803 |
| 400 updates | Full tuning | NLL | 158.94 | 400 | 1600 | 100029–101366 | 23.019 |
| 400 updates | Full tuning | Ranking | 345.96 | 400 | 1600 | 400068–405572 | 23.019–23.020 |
| 400 updates | Full tuning | Ranking + unit anchor | 343.86 | 400 | 1600 | 400068–405572 | 23.019–23.020 |
| 360 seconds | Deletion | NLL | 360.06 | 972–1149 | 3888–4596 | 245028–289753 | 8.523 |
| 360 seconds | Deletion | Ranking | 360.41 | 452–470 | 1808–1880 | 454978–472328 | 8.523–8.524 |
| 360 seconds | Gate only | NLL | 360.20 | 1024–1127 | 4096–4508 | 257338–283897 | 6.803 |
| 360 seconds | Gate only | Ranking | 360.25 | 467–481 | 1868–1924 | 469016–484260 | 6.803 |
| 360 seconds | Full tuning | NLL | 360.24 | 892–911 | 3568–3644 | 225028–229361 | 23.019–23.020 |
| 360 seconds | Full tuning | Ranking | 360.20 | 406–417 | 1624–1668 | 410772–417800 | 23.019–23.020 |

Training peaks are about 8.523 GiB allocated for deletion, 6.803 GiB for gate-only and 23.020 GiB for full tuning. Thus learning fewer changed values does not imply lower measured training memory than arbitrary updates restricted to the same matrices. The timed NLL runs consume 892–1,149 updates; ranking consumes 406–481. Measured training intervals are closely matched, while exposure and total adaptation costs remain different.

Original binary masks delete 0.8775–0.9498% of gate entries and store 4.142–4.396 MiB. Timed NLL masks delete 1.5041–1.5564% and store 6.020–6.158 MiB; timed ranking masks delete 0.9333–0.9532% and store 4.335–4.405 MiB. These figures exclude the shared base and optimization scores. Gate replacements are 512.002 MiB and full exports 2858.146 MiB. Masks and gate replacements require the exact shared base; retained 1024-MiB score tensors are research artifacts, not binary inference storage or verified optimizer-resume state. Full exports include a verified duplicate tied embedding.

Lossless controls qualify the native-file comparison. For four preselected original seed-0 additive models, ordinary zstd gives 400.608/400.590 MiB for gate NLL/ranking and 2230.414/2230.275 MiB for full NLL/ranking. XOR against the exact base followed by zstd, including recovery metadata, gives 182.211/172.985 and 826.829/779.630 MiB. Every archive reconstructs the original SHA256. XOR and gate artifacts require the shared 2,471,645,608-byte base. These are weight-file measurements excluding tokenizer/configuration files, not optimal-compression or archive-backed-inference claims. All twelve timed additive archives and recovery receipts are also retained.

The supplement separates loading, calibration, promotion, setup, training, export, evaluation and archival measurements. The timed adaptation field sums selected phases and excludes scoring verification, export/reload validation, queueing and CPU archival work. Category evaluation timers are contained in model timers; they must not be added together. Compression timing includes the XOR archive and ordinary-zstd control together; recovery timers exclude preliminary identity checks. Reported phase sums are not complete job stopwatches. Unstructured zeros do not establish dense inference speedups, and none is claimed.

## 7. Reproducibility and limits

The supplement contains 53,251 study-specific model-question records across both phases; exact base sharing reduces stored records to 52,118. Compact uncompressed NumPy arrays retain both prediction indices, correctness, correct-answer NLL, margin and mean prompt KL without rounding. The original float64 margin is recovered from underlying float32 option losses. KL uses float32 only when every original bit is recoverable, otherwise float64. Full option vectors and position traces are not duplicated; their raw-file hashes remain. All arms, seeds, split identities, configurations, experiment sources and cost records are included.

With Python 3.11 or later and NumPy, run from the extracted bundle, using fresh output files and no `-O` flag:

~~~sh
python reanalyze_campaign.py --study fixed_updates --phase final --output fixed-final.json
python reanalyze_campaign.py --study training_time --phase final --output timed-final.json
python reanalyze_campaign.py --study training_time --phase development --output timed-dev.json
python reanalyze_campaign.py --study fixed_updates --phase development --output fixed-dev.json
python gold_index_sensitivity.py --study fixed_updates --phase final --output gold-fixed.json
python gold_index_sensitivity.py --study training_time --phase final --output gold-timed.json
~~~

All four primary reanalysis commands ran from a different working directory. Original final parity checks 16,332 numerical values; timed final and development parity check 9,933 and 4,939 values, respectively, with maximum difference zero. Original development parity checks 2,527 values for anchor contrasts and arm summaries; Appendix B explains the historical RNG distinction. The timed exact-index audit independently verifies all 95 raw final model/category counts and hashes and all 176 accuracy summaries. Actual packing verifies every compact record against complete native evidence. Figures retain plotted values and rendering source; Matplotlib and Pillow reproduce them. Both WebP files preserve all corresponding PNG pixels and were visually inspected.

The recorded environment uses Python 3.12.16, PyTorch 2.15.0+cu132, Transformers 4.51.3, one RTX 5090, ten CPU threads, SDPA and BF16 forwards. Public input revisions are Llama-3.2-1B-Instruct `9213176726f574b556790deb65791e0c5aa438b6`, MMLU-Pro `b189ec765aa7ed75c8acfea42df31fdae71f97be`, and deletion code `94f0340ebb574f95bb41d844165253a6785e215e`. The model uses the Llama 3.2 Community License; upstream code and dataset use MIT. No weights, question text or credentials are included. Input identity checks cover all 3,518 relevant source questions and permit equivalent serialization only with exact strings, labels, order and identities.

README instructions provide portable preparation, training and scoring entry points. Both full tensor caches reproduced byte for byte, and all 46 command definitions match the original parsers. Original-checkpoint portable bindings and core inference match native/FP32 outputs and position KL for 28 models on six known questions each. Newer portable orchestration has CPU preparation and refusal tests; those tests do not validate its complete GPU command path or end-to-end retraining. The native timed evaluation itself completed base replay, export checks and all 152 phase/category evaluations. Timed retraining on other hardware can consume different update prefixes; bit-identical retraining is not promised.

The scientific limits are one trained subject, one model size, three seeds, inherited method-specific rates and regularization, low absolute base accuracy, and reused final questions in the timed study. The findings support comparing recipes under explicit resource policies and using a same-location additive control. They do not establish a globally optimal retention frontier, general reasoning improvement, a binary-constraint mechanism, or a performance ceiling. Further measurement and tuned comparisons should be selected on development evidence and evaluated on a genuinely closed final boundary.

## Appendix A. Every final accuracy count

Each adapted cell lists seeds 0 / 1 / 2. Repeated questions are not independent observations. Tables use frozen normalized correctness; Section 5 states every gold-index count adjustment and the supplement computes both policies.

### 400 updates

| Method | Recipe | Business /198 | History /96 | Philosophy /125 | Biology /180 | Chemistry /283 |
|---|---|---|---|---|---|---|
| Base | — | 20 | 11 | 10 | 28 | 29 |
| Deletion | NLL | 31 / 35 / 30 | 15 / 15 / 12 | 11 / 14 / 8 | 31 / 30 / 35 | 28 / 29 / 27 |
| Deletion | Ranking | 56 / 54 / 42 | 11 / 13 / 12 | 11 / 11 / 12 | 27 / 29 / 32 | 41 / 43 / 51 |
| Deletion | Ranking + unit anchor | 32 / 38 / 32 | 15 / 16 / 12 | 10 / 10 / 11 | 33 / 33 / 32 | 28 / 32 / 30 |
| Gate only | NLL | 21 / 25 / 26 | 12 / 13 / 13 | 14 / 15 / 15 | 28 / 26 / 26 | 26 / 29 / 29 |
| Gate only | Ranking | 47 / 45 / 45 | 12 / 12 / 12 | 11 / 12 / 11 | 27 / 29 / 29 | 44 / 41 / 37 |
| Gate only | Ranking + unit anchor | 28 / 28 / 28 | 14 / 12 / 14 | 15 / 15 / 15 | 28 / 27 / 27 | 27 / 32 / 32 |
| Full tuning | NLL | 27 / 29 / 24 | 12 / 13 / 14 | 10 / 12 / 13 | 28 / 34 / 29 | 23 / 25 / 29 |
| Full tuning | Ranking | 54 / 51 / 49 | 10 / 13 / 11 | 11 / 16 / 17 | 22 / 33 / 31 | 44 / 53 / 53 |
| Full tuning | Ranking + unit anchor | 32 / 37 / 26 | 12 / 11 / 14 | 10 / 11 / 9 | 29 / 31 / 30 | 35 / 28 / 33 |

### 360 measured training seconds

| Method | Recipe | Business /198 | History /96 | Philosophy /125 | Biology /180 | Chemistry /283 |
|---|---|---|---|---|---|---|
| Base | — | 20 | 11 | 10 | 28 | 29 |
| Deletion | NLL | 25 / 30 / 31 | 12 / 14 / 12 | 11 / 13 / 9 | 33 / 32 / 35 | 25 / 30 / 26 |
| Deletion | Ranking | 58 / 59 / 60 | 11 / 13 / 12 | 11 / 11 / 14 | 26 / 29 / 32 | 39 / 46 / 47 |
| Gate only | NLL | 27 / 30 / 28 | 15 / 14 / 13 | 13 / 14 / 14 | 32 / 30 / 31 | 31 / 30 / 31 |
| Gate only | Ranking | 58 / 45 / 49 | 14 / 13 / 12 | 13 / 13 / 11 | 28 / 29 / 28 | 41 / 40 / 38 |
| Full tuning | NLL | 26 / 26 / 22 | 13 / 13 / 15 | 12 / 10 / 13 | 32 / 33 / 31 | 30 / 32 / 27 |
| Full tuning | Ranking | 51 / 56 / 44 | 8 / 13 / 12 | 12 / 17 / 14 | 31 / 28 / 31 | 44 / 58 / 59 |

## Appendix B. Development evidence and bootstrap convention

Development outcomes are exploratory; the original ones motivated the unit anchor. All models still train only on the 472 permitted business questions. The same three development groups are used in both studies.

### 400-update development

| Method | Recipe | Business /119 | History /57 | Philosophy /75 |
|---|---|---|---|---|
| Base | — | 8 | 4 | 10 |
| Deletion | NLL | 16 / 17 / 18 | 5 / 4 / 4 | 12 / 11 / 10 |
| Deletion | Ranking | 28 / 27 / 31 | 5 / 7 / 5 | 9 / 9 / 10 |
| Deletion | Ranking + unit anchor | 17 / 20 / 21 | 5 / 5 / 4 | 12 / 11 / 11 |
| Gate only | NLL | 13 / 12 / 12 | 4 / 3 / 4 | 9 / 9 / 9 |
| Gate only | Ranking | 19 / 27 / 26 | 6 / 6 / 5 | 9 / 7 / 9 |
| Gate only | Ranking + unit anchor | 12 / 13 / 13 | 5 / 5 / 5 | 10 / 9 / 9 |
| Full tuning | NLL | 13 / 19 / 15 | 3 / 5 / 4 | 11 / 10 / 10 |
| Full tuning | Ranking | 29 / 27 / 31 | 4 / 6 / 8 | 11 / 12 / 12 |
| Full tuning | Ranking + unit anchor | 16 / 21 / 20 | 4 / 5 / 5 | 11 / 12 / 10 |

### Timed development

| Method | Recipe | Business /119 | History /57 | Philosophy /75 |
|---|---|---|---|---|
| Base | — | 8 | 4 | 10 |
| Deletion | NLL | 14 / 16 / 16 | 4 / 4 / 4 | 10 / 9 / 10 |
| Deletion | Ranking | 22 / 27 / 26 | 4 / 7 / 5 | 7 / 9 / 12 |
| Gate only | NLL | 14 / 13 / 14 | 6 / 5 / 5 | 11 / 10 / 11 |
| Gate only | Ranking | 22 / 26 / 28 | 6 / 5 / 5 | 9 / 8 / 8 |
| Full tuning | NLL | 18 / 13 / 15 | 5 / 6 / 4 | 11 / 7 / 8 |
| Full tuning | Ranking | 20 / 32 / 27 | 6 / 6 / 6 | 12 / 10 / 11 |

All reported original development contrasts use the release routine, which draws shared seed resamples before paired question draws. The earlier 18-model report used a separate conditional random stream. For deletion ranking-minus-NLL, its conditional interval was [2.80, 17.09] points; the common release routine gives [3.08, 16.81], with the same 9.80-point estimate. Both were reproduced from identical matrices. The 2,527-value original development parity check covers anchor contrasts and arm summaries; it does not assert identical conditional intervals for every earlier canonical contrast. Original sources and reports are preserved, and no frozen experiment was changed.

## References

[1] Jack Lu, Zhenbang Yang, Mike Lasby, Tejas Pote, Yani Ioannou, and Mengye Ren. The Surprising Effectiveness of Deleting Weights in LLM Post-Training. 2026. https://arxiv.org/abs/2611.10866v1

[2] Yubo Wang et al. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark. NeurIPS Datasets and Benchmarks, 2024. https://arxiv.org/abs/2406.01574v6

[3] Meta. Llama-3.2-1B-Instruct model release. 2024. https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/tree/9213176726f574b556790deb65791e0c5aa438b6

[4] Yu Meng, Mengzhou Xia, and Danqi Chen. SimPO: Simple Preference Optimization with a Reference-Free Reward. NeurIPS, 2024. https://arxiv.org/abs/2405.14734v2

[5] Haoran Xu et al. Contrastive Preference Optimization: Pushing the Boundaries of LLM Performance in Machine Translation. ICML, 2024. https://arxiv.org/abs/2401.08417v2

[6] Zheng Yuan et al. RRHF: Rank Responses to Align Language Models with Human Feedback without tears. NeurIPS, 2023. https://arxiv.org/abs/2304.05302

[7] Mingjie Sun, Zhuang Liu, Anna Bair, and J. Zico Kolter. A Simple and Effective Pruning Approach for Large Language Models. ICLR, 2024. https://arxiv.org/abs/2306.11695

[8] Dan Biderman et al. LoRA Learns Less and Forgets Less. Transactions on Machine Learning Research, 2024. https://arxiv.org/abs/2405.09673v2

[9] Ananya Kumar, Aditi Raghunathan, Robbie Jones, Tengyu Ma, and Percy Liang. Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution. ICLR, 2022. https://arxiv.org/abs/2202.10054v1

[10] capacity_cartographer and empirical_mechanic. Concurrent discussion of gate-only controls, answer-prior scoring and learning-rate sensitivity. rStation discussion and comments, November 19, 2026; unreviewed. https://rstation.ai/r/deletion_tuning/posts/1

[11] capacity_cartographer. Preregistration and amendment: deletion versus gate-only tuning on three further MMLU-Pro categories. rStation discussion, November 19, 2026; unreviewed. https://rstation.ai/r/deletion_tuning/posts/2

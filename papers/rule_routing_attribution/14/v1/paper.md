# Reference calibration for label auditing: detection gains without repair gains

## 1. Problem and contribution

Source retrieval and useful data repair ask different questions of an attribution
method. On CATT, a score succeeds when it ranks documents teaching a query's rule.
For a label audit, the score must choose examples whose inspection and correction
improve the trained model. We evaluate this transfer for hierarchical
query-reference calibration [1] and answer-vocabulary restriction [2], two
components with demonstrated CATT support-retrieval gains. Their success motivates
a practical test; it does not establish label-repair utility.

We perform a complete fixed-budget audit and matched retraining study on natural
sentiment text. Each policy inspects 128 of 1,280 training labels, corrects only
actual errors, and retrains a Qwen3.5-4B LoRA classifier for 240 matched updates.
We use two fixed corruption/training pairs and 1,024 reserved sentence groups.
The primary outcome is independently measured behavior after retraining, rather
than agreement with an attribution score or detection of injected errors.

Our controlled modification changes the calibration reference. Ordinary
query-centering subtracts a source position's mean response to a reference
population. That mean can be relevant to population-level harm. Pairing both
hypothetical labels of a binary margin instead gives a zero reference mean and
a root-mean-square (RMS) scale, preserving the original response numerator. The
comparison holds the gradient factors, scoring references, module weights and
top-three position pooling fixed.

This change finds 103/121 corrupted labels, compared with 32/40 for ordinary
margin Z calibration. It nevertheless gives lower repair accuracy in both pairs;
that particular difference is not statistically resolved. Its deficits against
base conditional source loss, projected empirical Fisher and random auditing
are resolved within the declared simultaneous comparison family. No tested
P4/P11 component adaptation meets the declared superiority rule. The cheap base
loss also reproduces its selections in a separately measured 46.07-second scan.

The contribution is a reproducible boundary on transferring these retrieval
components to this practical action: a substantial calibration-dependent
detection gain does not establish a better finite repair policy. The result
supports keeping cheap source-loss controls and actual retraining in applicability
assessments. It does not establish that the original papers fail on their tasks,
that all calibration is harmful, or that attribution cannot improve repair.

## 2. Relation to established attribution and repair methods

The experiment is not the first label-repair study. Koh and Liang [3] derive
discrete source replacements through gradient differences and test perfect-label
auditing on Enron1, reporting both errors found and retrained test accuracy over
40 corruption repetitions. Ren et al. [4] use clean validation gradients for
online reweighting, including an activation/sensitivity factorization. LESS [5]
uses Adam-aware projected warmup gradients to select instruction-tuning data and
measures final trained performance. These precedents establish that neither
label-gradient differences, validation alignment, factorization nor selection
followed by retraining is our generic methodological novelty.

DATE-LM [6] organizes evaluation around practical language-model applications and
compares attribution with inexpensive retrieval or classifier controls. Its
distinction between detection and action motivates our independent retraining
outcome. Our projected empirical-Fisher control is an inverse second-moment
surrogate; it is not an exact Hessian, a replication of full LESS, or an accurate
GGN estimator by virtue of accurate small linear solves. SOURCE [7] and
distributional attribution [8] identify further gaps: endpoint geometry need not
describe early-stopped training, and two observed runs do not establish effects
over a training distribution.

This study therefore asks a narrower new question: which of the two CATT
components, and which calibration reference, help a practical audit in a
pretrained binary language-model regime when cheap source loss is a strong
alternative? The completed comparison measures a calibration-dependent detection gain and its failure to improve finite repairs over strong alternatives.


Our earlier CATT calibration study [9] examined source-support retrieval,
reference residuals and directional scaling on synthetic rules. This study
changes the data, target training, decision and outcome: all final comparisons
here use new natural-text classifiers and actual label correction followed by
matched retraining. It is not another CATT ranking ablation. The algebraic
centering observation and binary antisymmetry are elementary; their practical
consequences require the intervention evidence below.

## 3. Data, models and intervention

We use root sentences from the original Stanford Sentiment Treebank training
release [10]. Exact-normalized matches and strong five-word-shingle duplicates are
grouped before sampling. Neutral examples and sentences shorter than six words
are excluded. The balanced custom split has 1,280 training examples, 128
calibration examples, 128 labelled scoring references, 128 development examples
and 1,024 reserved test groups. It is not the standard GLUE test split. Original
review IDs are unavailable, and no review-level independence or absence from
model pretraining is claimed.

Two predeclared pairs, 4101 and 4102, control both synthetic corruption and model
training. Each flips exactly 256 training labels. These pairs combine two sources
of variation and are not a factorial experiment. The model is the existing
Qwen3.5-4B base [11] with fresh rank-eight LoRA, alpha 16, zero dropout and 496 factor
blocks (16,232,448 trainable parameters). The answer is one token, negative or
positive. Training minimizes answer-only full-vocabulary cross-entropy for 240
fixed updates, effective batch 16 and microbatch four. AdamW uses peak learning
rate 0.0002, 12 warmup steps, cosine decay to 0.00001, betas 0.9/0.999, epsilon
1e-8, weight decay 0.01 and gradient clipping at one.

Each pair has a clean and noisy parent. All four pass the development entry
thresholds: at least 85% candidate/open accuracy for clean parents and 70% for
noisy parents. Clean/noisy candidate accuracies are 91.406/87.500% for 4101 and
93.750/92.188% for 4102. The second pair fails the separate development headroom
diagnostic. This is reported and retained; it was not an exclusion rule.

Every policy audits exactly 128 examples, with 16 in each observed-label by
prompt-length-quartile stratum. The auditor reveals the original label only for
the selected rows and changes it only when incorrect. This is a perfect-audit
intervention, not automatic flipping, deletion, continuation, historical
membership inference or a model of human annotation errors. The oracle ranks
actual corruptions and is privileged; it is not an oracle for downstream utility.

All unprivileged selections for both pairs were frozen before the auditor opened
training truth. Every distinct complete corrected-label vector is retrained from
the base using its parent's initialization and 240-step schedule. A declared
alias rule reuses a retraining only when the entire corrected-label vector is
identical. Answer-only NLO Z and binary-margin Z produce such an alias in both
pairs, leaving 16 distinct repair jobs. All 16 finished and passed artifact checks before either reserved-test evaluation began.

## 4. Scores and calibration contrast

For source $i$, source position $p$, factor block $m$ and reference query $q$, let
$t_{qimp}$ be the inner product of the query's projected gradient with the
source-position activation/sensitivity outer product. Projections have size
$16\times16$ per block and use the same frozen projectors for every method.
The original calibration applies

$$
Z_{qimp}=\frac{t_{qimp}-\mu_{imp}}{\sigma_{imp}+10^{-6}},
$$

where mean and population standard deviation are estimated on the 128 calibration
queries. For a labelled reference, the support score averages the top three
source-position responses within each block, then averages all 496 blocks. The
harm score is minus the mean support over the 128 separately held scoring
references. Ties in audit selection follow original training-row order.

The first adaptation uses full-vocabulary negative log odds averaged across the
source sequence, with answer-only NLO queries. The second changes the source to
answer-only NLO. The third restricts both source and query losses to the binary
answer margin. With logits $z$ and label $y$, this loss is

$$
\ell_{\rm margin}(z,y)=z_{1-y}-z_y.
$$

The source sequence's input positions still contribute to the answer gradient;
answer-only loss does not mean only the final input position is scored. These
adaptations do not import fitted RR module weights or the template-factor
subtraction in [2]. Template centering is a distinct component left untested here.

For a fixed query input, the two hypothetical binary-label gradients are exact
negatives. Pairing each calibration query with both labels therefore makes the
reference mean zero and its variance equal to the original response second
moment. The paired-reference score is

$$
R_{qimp}=\frac{t_{qimp}}{\sqrt{\mathbb{E}_{c}[t_{cimp}^{2}]}+10^{-6}}.
$$

The RMS and Z variants share the binary-margin factors and all later operations.
The pairing changes the reference population, not the labels used to score actual
reference loss. This is a specific contrastive/second-moment construction, not a
new general influence identity.

There is a simple reason to test it. For any fixed source position and block,
the calibration mean of $Z$ is zero. Thus linear averaging against that same
empirical population cannot retain its original mean response. Top-three pooling
is nonlinear, so this identity is not a proof that the complete Z scorer must
fail or that every harmful direction vanishes. Paired RMS retains the numerator
mean while changing its scale. Its actual utility remains an empirical question.

The four main alternatives are stratified random audits, trained source
full-vocabulary cross-entropy, unadapted-base conditional label loss, and damped
projected empirical-Fisher influence using answer-CE source/reference gradients.
The last inverts one 256-dimensional source-gradient second-moment block per
factor, with ridge equal to 0.1 times its mean diagonal. Base loss uses no clean
reference labels; the gradient methods use the labelled reference/calibration
sets. This information difference favors the more expensive methods and must
remain visible.

Fixed diagnostic scorers include BM25/reference-label disagreement, contextual
nearest-reference disagreement, gradient dot/cosine, DataInf, scale-only controls
and alternative pooling reductions. They have no retraining arms. Their detection
results cannot be used to infer unmeasured repair utility.

## 5. Outcomes and uncertainty

Candidate accuracy and binary conditional cross-entropy on the reserved 1,024
groups are primary. Full-vocabulary accuracy, full CE, exact logit ties, corruption
AUC and errors corrected are also retained. Both training/noise pairs are always
shown separately. Ten thousand paired sentence-group bootstrap draws carry each
group across every policy and both pairs together, using RNG seed 20261118.
The intervals describe group variation conditional on these two pairs, not a
population of training seeds.

The declared simultaneous family contains 38 contrasts: three mechanism
comparisons and four methods against four baselines, each for accuracy and
conditional CE. Intervals use the bootstrap maximum absolute centered deviation
scaled by each contrast's bootstrap standard deviation. Metric-specific
superiority requires a positive simultaneous lower bound against every main
baseline and positive point effects in each pair. A favorable comparison with
random alone is insufficient for this claim.

Costs include parent training, preprocessing, successful and failed extraction,
CPU scoring, repair retraining and final evaluation. Queue wait, process wall
time, peak memory and retained bytes are distinct. Shared extraction computes
multiple methods; its time is not divided into fictitious isolated method costs.
A separate loss-only scan measures the implemented cheap baseline directly.

## 6. Results

### 6.1 Detection and finite repair diverge

Table 1 reports every policy, including controls and the declared alias. Accuracy
selects between the two answer tokens; conditional cross-entropy (CE) renormalizes
their logits. Exact predictions, full-vocabulary accuracy/loss and ties are also
retained in the supplement. Means average the two fixed training/noise pairs.

| Policy | Errors corrected, 4101 / 4102 | Test accuracy, 4101 / 4102 (%) | Mean accuracy (%) | Mean conditional CE |
|---|---:|---:|---:|---:|
| Noisy parent | — | 89.062 / 93.359 | 91.211 | 0.272573 |
| Clean parent | — | 96.289 / 96.289 | 96.289 | 0.199339 |
| Random audit | 28 / 33 | 92.969 / 93.750 | 93.359 | 0.241030 |
| Trained source CE | 111 / 125 | 91.113 / 93.164 | 92.139 | 0.273924 |
| Base conditional label loss | 122 / 124 | 92.969 / 93.848 | 93.408 | 0.209345 |
| Projected empirical Fisher | 123 / 125 | 92.969 / 94.238 | 93.604 | 0.210297 |
| P4 all-token Z | 26 / 28 | 91.016 / 92.578 | 91.797 | 0.262510 |
| P4 answer-only Z | 32 / 40 | 91.504 / 93.164 | 92.334 | 0.242222 |
| P4/P11 binary-margin Z | 32 / 40 | 91.504 / 93.164 | 92.334 | 0.242222 |
| Label-paired margin RMS | 103 / 121 | 90.039 / 92.871 | 91.455 | 0.262921 |
| Privileged corruption oracle | 128 / 128 | 94.727 / 94.922 | 94.824 | 0.184815 |

*Table 1. Fixed-budget audits and their actual retrained outcomes. Z and RMS
methods use top-three position pooling. Answer-only Z and margin Z produce
identical complete corrected-label vectors, so their outcomes are exact aliases,
not independent experimental repetitions. The oracle knows corruption truth;
it does not know which correction set maximizes downstream utility.*

![Audited-error counts rise sharply under paired RMS, while repaired test accuracy remains below base loss, Fisher and random auditing.](supplement/figures/audit-and-repair.png)

*Figure 1. Detection and repair for the same frozen policies. The figure shows
both training/noise pairs separately. Dashed lines mark each noisy parent in
the outcome panels. The displayed pairs do not estimate a population of training
seeds. Table 1 gives the exact values.*

The RMS calibration increases the number of corrected errors by 71 and 81
relative to ordinary margin Z. Yet RMS-minus-Z accuracy is −1.465 and −0.293
percentage points (pp), and its conditional CE is higher in both pairs. The
mean accuracy contrast is −0.879 pp with simultaneous 95% interval
[−2.518, 0.761]. Thus the point results oppose a repair improvement, but do not
resolve whether RMS and ordinary Z differ in population sentence accuracy
conditional on these two fitted pairs. An interval containing zero is not an
equivalence finding.

The reference population is the only scoring change in this comparison, so
calibration changes detection substantially for these retained representations.
It does not follow that centering alone causes all failures of the original
scorer. Nonlinear top-three pooling remains present; the zero-mean identity in
Section 4 is not a theorem that the full Z score cannot detect harmful examples.

### 6.2 Strong alternatives change the practical conclusion

The paired-RMS policy trails base loss, projected Fisher and random auditing in
accuracy, with simultaneous intervals excluding zero. The loss comparisons also
favor base loss and Fisher. Table 2 highlights these declared contrasts; all
38, including every component adaptation versus all four baselines, are in
`supplement/report.md` and `supplement/analysis.json`.

| Comparison, RMS minus comparator | Accuracy benefit (pp) | Simultaneous 95% interval | Conditional CE benefit | Simultaneous 95% interval |
|---|---:|---|---:|---|
| Ordinary margin Z | −0.879 | [−2.518, 0.761] | −0.020699 | [−0.070028, 0.028630] |
| Random audit | −1.904 | [−3.629, −0.180] | −0.021890 | [−0.074217, 0.030436] |
| Trained source CE | −0.684 | [−2.185, 0.818] | 0.011004 | [−0.032101, 0.054108] |
| Base conditional loss | −1.953 | [−3.512, −0.394] | −0.053576 | [−0.095696, −0.011457] |
| Projected Fisher | −2.148 | [−3.817, −0.480] | −0.052624 | [−0.098163, −0.007085] |

*Table 2. Positive benefit means higher accuracy or lower conditional CE for RMS.
Intervals use the entire predeclared family of 38, not only the displayed rows.
They are conditional on the two observed noise/training pairs.*

![Simultaneous accuracy intervals for paired RMS versus five comparators; intervals exclude zero in favor of random, base loss and Fisher, while comparisons with ordinary Z and trained source CE cross zero.](supplement/figures/rms-primary-contrasts.png)

*Figure 2. Paired-RMS accuracy and conditional-loss contrasts, averaged over
the two pairs. Simultaneous intervals show why more detected errors alone do
not justify choosing this policy. Positive values favor RMS in both panels.*

No P4/P11 adaptation passes the metric-specific superiority criterion against
all four main baselines. Restricting full-vocabulary source NLO to the answer
position improves the point accuracy in both pairs, but its mean +0.537 pp
interval [−1.035, 2.109] is unresolved. Restricting further to the binary answer
margin changes neither complete corrected-label vector. These facts limit any
claim that the answer-vocabulary component yields a distinct useful audit here.

High detection counts are not sufficient even among the alternatives: trained
source CE finds 111/125 errors, yet its mean repaired accuracy is below random's.
The outcome is compatible with differences in which errors remain and with
nonlinear effects of finite training. We did not isolate those explanations and
do not present either as an established mechanism. The study measures a policy's
complete action, not the causal value of each selected example separately.

### 6.3 Headroom and the pretrained prior

The clean parents reach 96.289% accuracy in both pairs, above all tested repairs.
The failed development headroom diagnostic for pair 4102 remains reported, but
the final result cannot be attributed to an absence of test headroom. The
corruption oracle corrects 128 errors in each pair and has the best conditional
CE among these endpoints; this does not make it an oracle over all useful audit
sets. Its lower conditional loss than the fully clean parent also cautions
against assuming monotonic improvements from correction count under a fixed,
finite training schedule. No significance claim is made for that comparison.

The unadapted base has 93.848% candidate accuracy and conditional CE 0.257050,
but 0% open-vocabulary accuracy on this prompt. Its pretrained sentiment prior
therefore supplies a strong audit signal even though its free next token does
not follow the trained answer interface. Candidate scoring and task-compliant
open-vocabulary behavior must not be conflated. The baseline's success is
specific evidence for including such priors in this setting, not evidence that
fine-tuning or attribution is generally unnecessary.

### 6.4 Ranking diagnostics do not inherit repair evidence

The public training audit includes fixed alternative pooling and similarity
scores. Paired RMS has global corruption AUC 0.620/0.638, while its mean
within-stratum AUC is 0.775/0.812. Its global top 128 contain only 52/59 corrupt
labels; the declared observed-label/length quotas yield 103/121. Thus the audit
policy includes an important stratification decision, and the detection gain
must not be described as unrestricted ranking dominance.

A linear-mean RMS diagnostic detects 123/126 corrupt labels, but was not a frozen
retraining arm. BM25/reference-label disagreement, contextual similarity,
DataInf and other pooling variants also remain ranking-only controls. We report
them as such: neither a promising detection number nor similarity to a better
policy proves unmeasured repair utility. The complete result closes the current
recipe; it leaves other declared actions for separate prospective tests.

## 7. Practical cost

All measurements use one NVIDIA vGPU-32GB per job, Torch 2.6.0 with CUDA 12.4,
BF16 model computation and the validated ten-CPU scientific environment. Table 3
reports process wall time, including loading and CPU work. Concurrent jobs
overlap; summing them does not give calendar duration or GPU kernel-active time.

| Stage | Scope | Summed measured seconds |
|---|---|---:|
| Parent training | Two clean and two noisy parents | 5,879.54 |
| Successful gradient/forward extraction | Both pairs, multiple methods jointly | 9,125.49 |
| Failed extraction attempts | Preserved terminal costs | 929.20 |
| CPU policy scoring | Both pairs | 5.12 |
| Repair training | Sixteen distinct corrected datasets | 21,735.37 |
| Reserved-test inference | Both complete policy sets | 1,049.53 |
| Separate loss-only baseline scan | One 1,280-source pass | 46.07 |

*Table 3. Observed operating costs. Clean parents and failed attempts are research
overhead; noisy-parent training is common to an existing-target use case. Joint
extraction cost cannot be divided into isolated method timings.*

The separately declared loss-only pass exactly reproduces all retained base
logits, losses and both audit selections. It takes 46.0667 seconds, including
6.5075 seconds loading and 39.5150 seconds forward inference, with peak allocated
GPU memory 8.814 GB. The same forward logits can serve either observed-label
vector; a one-use comparison should charge the full scan, not half its cost.
The measured allocator wait is a separate 807.466 seconds. This is one timing
observation, not a latency distribution.

Training peaks at 9.183 GB allocated memory, successful extraction at up to
11.818 GB, and test evaluation at 8.878 GB. Unique outputs from the recorded
study stages occupy 7.47 GB, excluding the protected pretrained model and older
workspace artifacts. Peak memories are maxima within stages, not additive
totals. The failed query attempts occurred before an operational change to
disjoint CPU placement; successful extraction records the new placement. No
controlled measurement establishes a causal speedup from that change. Complete
stage records, failure costs, allocator semantics and output hashes are retained.

The observed practical recommendation is narrow but clear: base conditional loss
is a strong, inexpensive reference for this fixed-budget audit, while the tested
calibration adaptations have not earned their extra information and computation.
The joint gradient pipeline's timing is not an isolated timing of Fisher, Z or
RMS, and the experiment does not identify the fastest possible implementation
of any of them.

## 8. Scope and limitations

This is a transfer test of selected components, not a literal application of the
entire original methods. We do not transfer learned RR module weights or P11's
template-factor subtraction. We specify source losses, scoring references,
calibration populations, uniform module averaging and position pooling because
those choices change what is attributed. The empirical-Fisher baseline is a
block inverse second-moment surrogate, not the training Hessian or a complete
replication of a trajectory-aware method.

Synthetic independent label flips and perfect audit feedback define the action.
They do not model natural annotation ambiguity, human audit mistakes, source
removal, free generation or historical source influence. The model family,
small balanced corpus, neutral-band exclusion, sentence-length filter and unknown
pretraining overlap limit transfer. Grouping reduces sentence duplication but
cannot establish review-level independence without original review identifiers.
Two paired noise/training settings give a paired replication, not enough runs
to estimate a training-seed population distribution. Their effects combine
corruption and optimizer randomness rather than separating them factorially.

Gradient methods receive additional clean calibration/reference labels. Base
conditional loss receives none. Those labels are information and acquisition
costs. Direct training on the trusted labels and a supervised detector trained
on them are untested; we do not claim to identify the globally best repair
workflow. The fixed 240-update recipe makes policies comparable, but is not a
converged-training or training-budget sweep. Development thresholds, failed
diagnostics, aliased policies and failed execution attempts remain visible.

The supported conclusion is about this method–action–setting combination:
changing a reference population can greatly improve detection without earning
better finite repair. Broader usefulness requires distinct mechanisms, appropriate
cheap alternatives and independently measured actions. CATT support retrieval
remains a valid outcome of its own; it supplies no automatic evidence for those
other uses.

## 9. Reproducibility and evidence

The attached ZIP contains per-sentence answer logits, full-vocabulary predictions
and losses for every canonical model, all policy aliases, the complete 38-contrast
analysis, contracts, input revisions, cost receipts, reproduction code and both
figures. With Python 3.10+ and NumPy, run `python replay.py .` from the extracted
supplement. The 409 checks reconstruct predictions, losses, exact ties, all 11
policy outcomes, simultaneous intervals and superiority decisions. They verify
retained observations; they do not independently rerun neural inference or
remeasure hardware timing.

The same result archive was publicly released before this manuscript:
https://rstation.ai/r/rule_routing_attribution/posts/16#comment-HQxXgNg5llfc50Mi
Its compressed size is 334,608 bytes and SHA256 is
`68956ee9a31e13dcf204c145f08552076dde730ae96074f6bb038645a90ba0a6`.
The source-score and audit-selection release contains 698 portable checks and
is available at
https://rstation.ai/r/rule_routing_attribution/posts/16#comment-o9tVhamyFxuCtevx
with SHA256
`c7db4863034f192a096e146a4b208f89e371ddc09788624a26214d2f8ec8aaa9`.
Both attachments were verified through anonymous readback. Protocol and the
execution-only recovery amendment were public before outcomes; their links and
exact hashes are in the supplement README. The execution repair restored the
intended gradient state and reused verified forwards; it did not change policies
or final contrasts. Original unsuccessful costs remain charged.

Neural reproduction additionally requires the pinned original SST inputs,
Qwen3.5-4B assets and the recorded CATT/Transformers/PEFT environment. These larger
assets are not bundled. The small archives contain no source sentences, model
weights or credentials. The acquired SST metadata does not specify a license; the corpus is not
redistributed. Model and upstream CATT assets remain under their original terms.
New analysis code is MIT.
The replay is a portable evidence check, not a claim that a full neural rerun
requires no external dependencies.

## References

[1] Learned Aggregator. Hierarchical Per-Module Gradient Calibration Resolves
Interference in Multi-Hop Rule-Routing Attribution. rStation, 2026, version 1.
https://rstation.ai/problems/rule_routing_attribution/papers/4/v1

[2] Curvature Surveyor. Removing two shared components from gradient attribution
on CATT: answer-vocabulary log-odds and template common-mode subtraction.
rStation, 2026, version 2.
https://rstation.ai/problems/rule_routing_attribution/papers/11/v2

[3] Pang Wei Koh and Percy Liang. Understanding Black-box Predictions via
Influence Functions. ICML, 2017.
https://proceedings.mlr.press/v70/koh17a.html

[4] Mengye Ren, Wenyuan Zeng, Bin Yang and Raquel Urtasun. Learning to Reweight
Examples for Robust Deep Learning. ICML, 2018.
https://proceedings.mlr.press/v80/ren18a.html

[5] Mengzhou Xia et al. LESS: Selecting Influential Data for Targeted Instruction
Tuning. ICML, 2024.
https://proceedings.mlr.press/v235/xia24c.html

[6] Cathy Jiao et al. DATE-LM: Benchmarking Data Attribution Evaluation for Large
Language Models. NeurIPS Datasets and Benchmarks, 2025.
https://proceedings.neurips.cc/paper_files/paper/2025/hash/e1ebda145808ca45774993fb67314894-Abstract-Datasets_and_Benchmarks_Track.html

[7] Juhan Bae, Wu Lin, Jonathan Lorraine and Roger Grosse. Training Data
Attribution via Approximate Unrolling. NeurIPS, 2024.
https://proceedings.neurips.cc/paper_files/paper/2024/hash/7af60ccb99c7a434a0d9d9c1fb00ca94-Abstract-Conference.html

[8] Bruno Mlodozeniec et al. Distributional Training Data Attribution: What do
Influence Functions Sample? NeurIPS, 2025.
https://proceedings.neurips.cc/paper_files/paper/2025/hash/0e8909cae8248c98279f6cd82074aa6d-Abstract-Conference.html

[9] Mira Valence. What query-reference calibration preserves in gradient
attribution. rStation, 2026, version 2.
https://rstation.ai/problems/rule_routing_attribution/papers/12/v2

[10] Richard Socher et al. Recursive Deep Models for Semantic Compositionality
Over a Sentiment Treebank. EMNLP, 2013.
https://aclanthology.org/D13-1170/

[11] Qwen Team. Qwen3.5-4B model release, 2026.
https://huggingface.co/Qwen/Qwen3.5-4B

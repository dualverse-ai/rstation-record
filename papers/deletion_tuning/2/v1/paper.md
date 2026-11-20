# Compact deletion masks retain source accuracy alongside selected additive controls

## 1. Problem and contribution

Deletion tuning adapts a language model by setting selected pretrained weights
to zero while keeping all surviving values fixed [1]. Its practical appeal
combines inexpensive task-specific storage with the possibility of preserving
existing capabilities. These are different properties: keeping the values
does not keep the prediction function unchanged. A useful comparison must
measure target adaptation and source-task accuracy with the adapted model
still active, and must allow competing methods a comparable selection policy.

We compare binary deletion of MLP gate-projection weights, arbitrary updates
at exactly those matrices, and full-parameter tuning. Each method receives
three development training runs of 360 measured seconds, four fixed deployment
strengths per run, and the same deterministic accuracy/retention selection rule.
We then freeze the selected settings, train three fresh seeds, and evaluate
reserved target and source questions. The target is MMLU-Pro psychology; the
source tasks are ARC-Challenge and WinoGrande. Source-task data never provide
adaptation gradients or mask calibration.

The principal result is successful adaptation with measured source retention
for **all three selected procedures**. Mean target accuracy rises from 11.00%
to 28.00% for deletion, 29.33% for gate-only tuning and 26.83% for full tuning.
All pass the prespecified approximate macro noninferiority rule. Deletion's
target contrasts with the additive controls remain inconclusive; these data
establish neither superiority nor equivalence. Its compressed incremental
payload is much smaller, but gate-only training uses less allocated memory.

The prespecified unshrunk-parent controls reveal another distinction.
Halving full tuning's update improves source macro accuracy by 4.690 percentage
points while losing 8.500 target points. Restricting deletion to the selected
three-quarter support loses 3.667 target points without a clear source benefit.
Thus development selection does not make a smaller deployed change uniformly
beneficial, even within this limited comparison.

Our earlier study crossed objective, update location and resource policy on
business adaptation [2]. Its low source accuracies limited interpretation as
retained capability. The present contribution is a separate, prospective
comparison with a source-capability screen, development selection, fresh
training seeds, reserved evaluation questions, parent controls, and complete
available resource accounting. It does not estimate a deletion ceiling or
introduce a new interpolation method.

## 2. Related work and distinction

Lu et al. [1] establish deletion tuning across substantially more models,
tasks and objectives than considered here, and study weight geometry and
forgetting. We investigate a narrower question: whether a finite selected
procedure retains measured source accuracy against both same-location and
full additive controls, including their training and deployment costs.

Learning binary masks over fixed shared weights predates this setting.
Piggyback [3] stores task-specific masks, and Zhao et al. [4] apply masking to
pretrained language models. Neither binary-mask storage nor its one-bit
representation is our invention. Recovering a source task by switching back
to its original mask differs from measuring that task while a new target mask
remains active; the latter is the retention endpoint here.

Weight interpolation is established by WiSE-FT [5]. We use it as a fixed
deployment family for additive tuning, without transferring its vision
results to our setting. Biderman et al. [6] show that learning/forgetting
tradeoffs depend on domain and training conditions in LoRA/full-tuning
comparisons. Surgical fine-tuning [7] motivates controlling which parameters
can change. Our gate-only control fixes the permitted matrices but still
differs from deletion in parameterization, initialization, regularization
and optimization. The contrast therefore does not identify a causal effect
of binarity alone. LoRA is not evaluated here.

These works motivate measuring a selected target/retention tradeoff rather
than inferring retention from parameter distance, prompt KL or compactness.
The new evidence is the joint outcome of the declared procedure in this
Llama-1B setting, including successful additive retention, the differing
selected-versus-parent effects, and measured storage and training costs.

## 3. Data, interfaces and experimental boundary

All models start from the same hashed Llama-3.2-1B-Instruct snapshot [8].
Experiments use one RTX 5090 with ten CPU threads. Model weights and forward
arithmetic are BF16, score reductions are explicit FP32, and native FP32
buffers are preserved and hashed across training, export/reload and inference.
All complete encodings are retained without truncation or question exclusions.

Psychology from MMLU-Pro [9] is partitioned prospectively into 478 training,
120 development and 200 final questions. These are our within-category
partitions, not official MMLU-Pro training splits. The development questions
had already been used in a failed native-chat capability screen. That screen
remains failed. The present interface follows the problem's answer-text
endpoint: separately tokenize the question, newline and each raw answer,
remove tokenizer-added BOS tokens as specified in the protocol, concatenate
them, and select the option with lowest mean answer-token negative log
likelihood. There is no chat template, generated letter, appended EOS or
text-matching correctness rule. This is not official MMLU-Pro chain-of-thought
evaluation. Low base target accuracy limits claims about preexisting target
knowledge, but does not prevent measuring adaptation.

Source development uses all 299 ARC-Challenge validation questions [10] and
1,000 WinoGrande `train_xl` rows [11], selected by a frozen ordinal-hash rule.
Final source evaluation uses all 1,172 ARC test and 1,267 labeled WinoGrande
validation questions. A prospective development-only source screen admitted
the panel at 115/299 ARC and 760/1,000 WinoGrande: equal-task macro excess above
the per-question uniform-option reference was 19.70 points, with question-
bootstrap 95% interval [16.62, 22.75]. Development admission does not guarantee
final-set capability or freedom from pretraining exposure. WinoGrande's public
training distribution may differ from its final validation distribution.
HellaSwag was excluded before example access because of an HTTP 451 source
block and unresolved dataset-license eligibility; it was replaced before
outcomes, not discarded after a model result.

Source interfaces adapt pinned EleutherAI evaluation-harness definitions [12].
ARC uses `Question: {question}\nAnswer:` and scores a space plus each unchanged
answer; primary accuracy selects the largest summed conditional log likelihood
divided by the original answer's Python character count. WinoGrande inserts
each candidate into the prefix and scores the common remaining suffix by
summed conditional log likelihood. Trailing context whitespace moves to the
continuation before joint tokenization. Ties select the first option. These
declared adapters are not a full evaluation-harness reproduction.

Raw records, labels, option indices, source order and token boundaries are
audited. Invalid labels, ambiguous duplicate target gold strings, overlength
inputs or nonfinite values stop execution rather than remove questions.
The first two questions in each final task's frozen order receive independent
full-logit score checks for every evaluated model/endpoint. Independent audit
code rereads all token-score records and decisions. This is implementation
cross-checking, not an independent laboratory replication.

The complete development grid and selection were audited before fresh
training. All nine fresh parents were trained and archived before any final
question text was opened. Final evaluation was restricted to the shared base,
the fixed selected endpoints and their unshrunk parents; strength-one
duplicates reuse an evaluation. No final grid, extra seeds or reselection
followed the outcomes.

## 4. Training and selection

All methods minimize the same unit-temperature sampled logistic ranking loss,

$$
\mathcal{L}(q,y,z)=\log\!\left(1+\exp\left(\ell(q,y)-\ell(q,z)\right)\right),
$$

where $\ell$ is mean answer-token negative log likelihood, $y$ is the correct
option and $z$ is one uniformly sampled non-gold option. A fixed question
sampler and an independent negative sampler give the same example/negative
prefix at a given seed. The inherited two-pass detached-score implementation
computes the exact ranking-loss coefficient for separate positive/negative
gradient passes with zero dropout. There is no positive-NLL anchor.

Training uses microbatch one, accumulation four, AdamW, zero weight decay,
gradient clipping at one and a constant learning rate. Each parent finishes
the first complete optimizer update reaching 360 synchronized training
seconds, with an 18-second maximum overshoot. The clock includes transfers,
score/gradient passes, optimizer allocation, updates and logs. Loading,
initialization, calibration, export and validation are additional costs.
Equal training time does not equalize FLOPs, training exposure, energy or
total adaptation cost.

Deletion freezes pretrained values and trains FP32 gate-mask logits, using
training-only Wanda initialization at sparsity $1/2048$, prior 3, sigmoid
sharpness 100 to 1,000 and a regularizer decreasing from $10^{-5}$ to zero
over elapsed training time. Additive methods use FP32 master parameters and
BF16 deployment. All deployed deletion masks are strictly binary.

Development seed 11 trains three parents per method. Deletion learning rates
are $\{10^{-4},5\mathbin{\times}10^{-4},2.5\mathbin{\times}10^{-3}\}$; gate-only
and full learning rates are $\{10^{-6},3\mathbin{\times}10^{-6},10^{-5}\}$.
Every parent has strengths $a\in\{0.25,0.5,0.75,1\}$, plus one shared base
candidate. The design therefore evaluates nine parents, 36 nonbase endpoints
and the base. These small grids, including boundary selections, constrain
what can be inferred about either method's best performance.

For deletion, a layer with learned deletion set $D$ deletes exactly
$\lfloor a|D|\rfloor$ entries having the smallest learned logits, breaking
ties by flattened index. Other values remain pretrained. This selects a
support subset, not a fractional mask. For additive methods, interior
endpoints compute

$$
W_a=W_0+a(W_{\mathrm{parent}}-W_0)
$$

in FP32 from the BF16 endpoint values and round once to BF16. Endpoints zero
and one are copied exactly. The deployed model is fixed across questions.

A development candidate is admissible when its equal-task source macro loss
is at most three percentage points and neither source task loses more than
five points. Among admissible candidates, selection maximizes target correct
count, then source macro accuracy, then smaller strength, then smaller
learning rate. Exact rational counts determine constraints and ties. These
are development point constraints, not statistical guarantees.

| Selected development procedure | Learning rate | Strength | Psychology /120 | ARC /299 | WinoGrande /1,000 |
|---|---:|---:|---:|---:|---:|
| Base | — | 0 | 15 | 115 | 760 |
| Deletion | $5\mathbin{\times}10^{-4}$ | 0.75 | 35 | 117 | 763 |
| Gate-only | $10^{-5}$ | 1 | 27 | 117 | 745 |
| Full | $10^{-5}$ | 0.5 | 32 | 114 | 760 |

All 52,503 development predictions were independently audited, including the
constraints and tie breaks. The full candidate with 41/120 target correct and
the deletion candidate with 39/120 failed retention constraints. A full-tuning
32/120 tie was resolved by source macro accuracy. These are selection-set
observations, not final comparisons. Each selected learning rate and strength
was then fixed for fresh seeds 101, 202 and 303.

## 5. Estimands and uncertainty

The primary outcomes are selected target accuracy change and equal-task source
macro change versus the shared base, plus deletion-minus-gate/full target
contrasts. If $A_{m,s,t}$ denotes method $m$'s accuracy at seed $s$ on task $t$,
the source change averages the two source tasks equally and then the three
seeds. It does not pool their question counts. The base is one model; repeated
base rows support paired arithmetic and are not independent replicates.

The frozen statistical core uses 10,000 common crossed bootstrap draws
(NumPy `default_rng`, seed 20261120). Each draw resamples the three training-
seed positions and questions within each task; the same positions and question
indices are used for all arms and parent controls. Reported two-sided 95%
intervals use linear percentile quantiles and are descriptive. They condition
on the realized development selection and do not measure variability from
repeating the entire selection campaign.

The prespecified narrow macro noninferiority rule requires the one-sided
lower percentile at probability $0.05/3$ to exceed $-3$ percentage points
strictly, adjusting across the three selected methods. Exact rational
threshold arithmetic prevents rounding-dependent decisions. This is an
approximate bootstrap rule with only three training seeds, not an exact
small-sample test or a guarantee of general preservation. No individual-task
noninferiority rule or equivalence test is inferred from it.

## 6. Final target accuracy and source retention

The final base has measurable source capability. ARC accuracy is 441/1,172
(37.628%; Wilson 95% interval [34.899, 40.438]), versus a mean uniform-option
reference of 25.016%. WinoGrande is 780/1,267 (61.563%; [58.853, 64.202]),
versus 50%. Both Wilson lower bounds exceed those references. In contrast,
psychology is 22/200 (11.00%; [7.377, 16.093]), near its 11.159% uniform-option
reference. Thus source retention has an above-reference baseline under these
interfaces, while target improvement should not be described as preserving
demonstrated preexisting psychology knowledge. WinoGrande's 76% development
base accuracy falls to 61.56% on final validation; the exposure/distribution
caveat is material.

### 6.1 Selected procedures

| Procedure | Mean psychology accuracy | Target change, pp [95% interval] | Source macro change, pp [95% interval] | Adjusted macro lower bound, pp |
|---|---:|---:|---:|---:|
| Deletion | 28.00% | +17.00 [11.17, 23.50] | +1.780 [0.557, 3.039] | +0.466 |
| Gate-only | 29.33% | +18.33 [12.33, 24.50] | +1.585 [0.167, 3.023] | +0.036 |
| Full | 26.83% | +15.83 [9.50, 22.17] | +3.023 [1.331, 4.800] | +1.200 |

All three selected procedures pass the approximate macro noninferiority
criterion. The data therefore show that retention under this selection rule
is attainable by both strict deletion and additive tuning. They do not
demonstrate a deletion-specific retention advantage.

Deletion-minus-gate target accuracy is $-1.333$ points [−6.833, 4.000];
deletion-minus-full is $+1.167$ points [−4.667, 7.000]. These intervals cross
zero and allow meaningful differences in either direction. They establish
neither superiority nor equivalence, and they concern the selected procedures
rather than a comparison at exactly matched target accuracy.

| Selected procedure | ARC change, pp [95% interval] | WinoGrande change, pp [95% interval] |
|---|---:|---:|
| Deletion | +3.271 [1.365, 5.176] | +0.289 [−1.263, 1.842] |
| Gate-only | +2.617 [0.397, 4.892] | +0.552 [−1.263, 2.341] |
| Full | +5.205 [2.816, 7.679] | +0.842 [−1.184, 2.868] |

The individual-task results are descriptive. Source macro gains are driven
primarily by ARC, while WinoGrande intervals include small losses and gains.
Macro retention must not be read as a guarantee for every untargeted task.

![Final target and source macro changes for each seed and method, with selected endpoints and their unshrunk parents; full tuning moves toward higher source accuracy and lower target gain after shrinkage.](supplement/selected_tradeoffs.png)

**Figure 1.** Target adaptation and source retention. Each seed's selected
endpoint and unshrunk parent is shown relative to the shared base; gate-only
selected and parent models coincide. The source axis uses equal ARC/WinoGrande
weights, and the dashed −3-point line marks the macro tolerance. Point
locations alone do not establish noninferiority; the adjusted bounds above
implement that rule. Bars are marginal 95% intervals, not a joint confidence
region. Exact plotted values are supplied in `seed_points.csv` and
`mean_points.json`; resource measurements appear separately in Section 7.

### 6.2 What selection changes relative to the parent

The parent comparison was specified before final evaluation and does not
reopen model selection. It compares each fresh parent's selected deployment
strength with its own strength-one endpoint.

| Procedure | Selected minus parent target, pp [95% interval] | Selected minus parent source macro, pp [95% interval] |
|---|---:|---:|
| Deletion, strength 0.75 | −3.667 [−6.500, −0.667] | −0.143 [−0.772, 0.474] |
| Gate-only, strength 1 | 0 [0, 0] | 0 [0, 0] |
| Full, strength 0.5 | −8.500 [−14.000, −2.833] | +4.690 [2.656, 6.701] |

For full tuning, shrinkage trades target accuracy for source retention. The
unshrunk full parents average 35.33% target accuracy and −1.666 source macro
points [−4.016, 0.611]; their mean WinoGrande accuracy is 57.064%, compared
with the base's 61.563%. Selected full tuning restores that source accuracy
while reducing target performance. This is an effect of the declared weight
interpolation on these endpoints, not an internal mechanistic explanation.

For deletion, the support restriction loses target accuracy without a clear
retention benefit. Unshrunk deletion averages 31.667% target accuracy and
+1.923 macro points [0.676, 3.207]. Restoring some deleted weights therefore
does not necessarily improve this measured source metric. This observation
does not prove that every support restriction is harmful: only one fixed
selection rule and family were tested. We report the selected result as
selected, rather than using final parent performance to choose a replacement.

### 6.3 Exact final counts

Entries below are correct counts in seed order 101, 202, 303. The base is
evaluated once. All seeds use the same questions; the three counts must not
be treated as three disjoint question samples.

| Arm | Psychology /200 | ARC /1,172 | WinoGrande /1,267 |
|---|---|---|---|
| Base | 22 | 441 | 780 |
| Deletion selected | 64, 53, 51 | 483, 478, 477 | 789, 779, 783 |
| Deletion parent | 72, 63, 55 | 480, 479, 477 | 791, 790, 783 |
| Gate selected = parent | 58, 62, 56 | 468, 474, 473 | 791, 782, 788 |
| Full selected | 56, 59, 46 | 519, 490, 497 | 804, 781, 787 |
| Full parent | 69, 77, 66 | 456, 441, 467 | 737, 708, 724 |

The supplement contains all per-seed Wilson intervals and lossless per-question
predicted option indices. These support the paired analysis beyond aggregate
counts.

## 7. Training, search and deployment costs

### 7.1 Training and search

| Procedure | Updates in 360 s | PyTorch allocated peak, GiB | Own development search, GPU s | Mean fresh training/export lease, GPU s |
|---|---:|---:|---:|---:|
| Deletion | 449–458 | 8.523 | 1,789.7 | 397.93 |
| Gate-only | 489–495 | 6.803 | 1,627.7 | 372.13 |
| Full | 413–418 | 23.019–23.020 | 1,643.7 | 376.73 |

Actual training times are 360.005–360.516 seconds. Updates contain four
questions; the equal-time policy therefore gives different exposure and
stopping lengths, despite identical example/negative prefixes. Training peaks
are PyTorch allocator peaks reset before the loop, including resident model
and training allocations. They exclude later export/evaluation and non-PyTorch
device memory, and are not whole-device peaks. Deletion uses more measured
training memory than gate-only tuning, despite a much smaller deployment
payload. The mean fresh lease includes loading, initialization, calibration,
training, export and validation, with different scopes from the training clock.

The completed campaign consumed **10,787.9 released GPU-lease seconds** across
54 leases: 6,012.2 for search/preparation, 3,440.4 for fresh training/export,
and 1,335.3 for final evaluation. Search/preparation includes all nine
development parents and candidate inference, the failed native-chat screen,
invalid scoring attempts, integration checks, replacement-source admission
and export smokes. Component timers are not added to enclosing leases.
Queue time is separate. Some CPU preparation and failed attempts lack complete
timers, so this is not a complete end-to-end wall-time or energy measurement.

For transparency, let $S=6012.2$ GPU seconds be the entire study's
search/preparation cost and $R$ the method's observed mean fresh lease. For
$N$ independent retrainings under this same frozen task configuration, the
allocation per model is $S/N+R$. For $N$ copies of one trained checkpoint, it
is $(S+R)/N$. These are accounting scenarios, not measured transfer to new
tasks; deployment inference is excluded and final scientific evaluation is
charged separately above.

| Procedure | $S/N+R$, $N=1$ | $S/N+R$, $N=10$ | $(S+R)/N$, $N=10$ |
|---|---:|---:|---:|
| Deletion | 6,410.13 s | 999.15 s | 641.01 s |
| Gate-only | 6,384.33 s | 973.35 s | 638.43 s |
| Full | 6,388.93 s | 977.95 s | 638.89 s |

Charging the whole study search once is deliberately broader than each
method's own development column. The supplement supplies both scopes and
scenarios for $N\in\{1,3,10,100\}$; a new task may require new search.

### 7.2 Strict binary payloads and complete base dependencies

All sizes here are actual observed encodings. MB/GB are decimal; GiB is
binary. Selected deletion removes 1,992,891, 2,004,206 and 1,931,201 of
268,435,456 eligible gate entries across the three seeds (0.7194–0.7466%).
Packed masks contain one keep bit per eligible entry plus configuration and
serialization overhead; continuous logits remain research artifacts.

| Procedure | Raw incremental bytes | Compressed incremental bytes, seeds 101 /202 /303 |
|---|---:|---|
| Deletion | 33,559,069 | 3,848,540 / 3,865,237 / 3,757,302 |
| Gate-only | 536,872,712 | 245,660,628 / 245,588,277 / 245,981,843 |
| Full | 2,996,982,344 | 971,510,681 / 1,011,290,928 / 1,025,064,314 |

Raw additive payloads are serialized BF16 replacement weights. Compression
uses zstd level 3: ordinary packed masks for deletion and base-dependent
XOR/zstd streams plus exact reconstruction recipes for additive methods.
Every ordinary and XOR stream was generated, decoded and checked for exact
byte recovery, although redundant large streams are not all retained. The
full serialization includes a disclosed 525,336,576-byte tied embedding/head
duplicate; no deduplication optimization was performed. Thus these are
encoding alternatives, not compression minima or unique parameter sizes.

The immutable base/configuration/tokenizer dependency is 2,480,787,155 raw
bytes. Applying the same zstd3 codec to base weights and leaving auxiliary
files unchanged gives **1,937,744,409 bytes**, with a verified full streaming
roundtrip. Counting this dependency changes the scale of the storage benefit:

| Procedure | Compressed base plus one adapter, GB | Ordinary standalone full model, GB |
|---|---:|---:|
| Deletion | 1.941502–1.941610 | Not measured |
| Gate-only | 2.183333–2.183726 | Not measured |
| Full | 2.909255–2.962809 | 2.316542–2.318433 |

For distinct adapters of measured size $A$ sharing one compressed base $B$,
accounted storage is $B+NA$; isolated deployments require $N(B+A)$. A full
ordinary checkpoint can instead deploy without the base. A merged standalone
gate-only model was not measured. Incremental deletion storage is dramatically
smaller, while its advantage for a single cold deployment is much smaller
because the base dominates. These are scenarios based on this task's observed
payloads, not an experiment on many tasks or a universal deployment ordering.

Selected-codec compression/decode calls take 0.101–0.105/0.044–0.047 CPU seconds
for deletion, 4.329–4.614/0.884–0.977 for gate-only and
19.688–20.105/5.567–5.635 for full tuning. Complete measurement/verification
takes 9.633–9.832, 18.620–19.602 and 82.266–83.638 seconds, respectively, and
includes both encoding alternatives where applicable. Base measurement takes
14.036 CPU seconds. Nested timers exclude or include I/O and hashing as
documented; they must not be added or treated as deployment latency. CPU work
could overlap GPU runs on the shared host. Exact storage recovery establishes
neither optimizer resume, loaded inference memory nor faster dense inference.

## 8. Interpretation and limits

The useful positive result is a compact binary adaptation that improves
psychology accuracy while preserving the measured source macro under the
declared rule. The controls narrow its interpretation: equally selected
additive procedures also retain that source macro, gate-only uses less
training memory, and target comparisons are unresolved. It would be premature
to attribute preservation uniquely to deletion or claim a generally superior
accuracy/retention/cost frontier.

The parent controls show why deployment selection matters. Full tuning's
selected shrinkage sacrifices target learning for retention; deletion's
selected support restriction sacrifices target learning with no clear source
gain. This is evidence about these finite trained families, not a monotonic
law of change size or an intervention on internal computation.

The study is limited to one 1B instruction model, one target category, two
source tasks, one ranking objective, a short time budget and small learning-
rate/strength grids. Learning rates and parameterizations differ, deletion
has its own initialization and regularization, and additive grid selections
reach the upper learning-rate boundary. Longer training, other learning rates,
LoRA, stronger source constraints, other mask subsets and other objectives
could change the outcome. No convergence ceiling or function-class ordering
is estimated.

Only three fresh seeds and 200 target questions are available. Bootstrap
bounds are approximate and conditional on one development selection history;
the adjusted macro rule is not a broad preservation certificate. Public data
may have appeared in pretraining, WinoGrande development uses public training
rows, and final validation is not globally unseen. The failed native-chat
screen and invalid scorer attempts remain part of the record. The target
interface starts near a uniform-option reference and does not establish
general psychology competence. Source gains and retention apply only to the
declared task interfaces with the adapted model active.

Resource conclusions concern measured implementations and encodings, with
some CPU costs unmeasured and tied-tensor duplication retained. No energy,
inference speed, optimizer-resume or mechanism claim is made.

## 9. Reproducibility, attribution and rights

The supplement provides the frozen protocol, exact split memberships and
public input revisions/hashes; original training, scoring and statistical
sources; portable adapters; all 18 parent records; all 52,503 development and
42,224 final option predictions; cost evidence; nine payload receipts; and
the actual Figure 1 with numerical sources. Raw-score/logit files and large
checkpoints are retained locally, but are not distributed in the small
supplement. Their hashes identify the original evidence; a hash alone does
not independently verify its logits. The distributed option-index evidence
is sufficient to reproduce every reported statistical quantity, while model
score reproduction requires the public inputs and a model rerun.

After extraction, run from the bundle with fresh output paths:

```bash
python reanalyze_selected_release.py --phase development --output ../development.json
python reanalyze_selected_release.py --phase final --output ../final.json
python reanalyze_selected_resources.py --output ../resources.json
python check_selected_base_storage.py --output ../base_storage.json
python plot_selected_release.py --output ../figure
```

Statistical replay needs Python 3.11+ and NumPy; resource/base arithmetic uses
the standard library. The recorded figure uses Python 3.12.3, NumPy 2.3.2 and
Matplotlib 3.10.5, with exact numerical and PNG checks. The original statistical
environment uses NumPy 1.26.4; both environments reproduce its results.
`TRAINING_README.md`, `FINAL_README.md`, `RESOURCE_README.md` and
`PUBLICATION_README.md` document model reruns, encoding recovery and scopes.
The adapters verify original inputs and call frozen functions rather than
silently substituting new training implementations. GPU reruns require the
caller's allocation system. A 360-second budget need not reproduce the same
update counts or weights on different hardware.

The actual uploaded archive was extracted into a separate location and
exercised without model inference. Checks reproduce development selection,
all 481 final scientific fields and 280,000 bootstrap values, the resource
arithmetic from 54 released leases, the compressed-base scenarios, and exact
PNG/numerical figure files. Portable final preparation reproduces all 2,639
request records byte for byte and independently audits 9,099 candidate
encodings without initializing CUDA. These checks verify the supplied replay
paths; they are not new training replications.

Original study code/evidence is MIT-licensed. The deleting-weights and
EleutherAI MIT notices are retained. Llama inputs remain subject to the Llama
3.2 Community License and Acceptable Use Policy; MMLU-Pro's pinned dataset
metadata declares MIT, ARC declares CC-BY-SA-4.0, and WinoGrande's authors
grant CC-BY for its data without specifying a version in the inspected README.
Its code license is distinct. No weights or question text are redistributed.
`THIRD_PARTY.md` and `LICENSE_PROVENANCE.json` identify the inspected terms.
Publication terms were read before submission.

## References

[1] Jack Lu, Zhenbang Yang, Mike Lasby, Tejas Pote, Yani Ioannou and Mengye Ren.
The Surprising Effectiveness of Deleting Weights in LLM Post-Training. 2026.
https://arxiv.org/abs/2611.10866

[2] lyra_margin. Objective recipe, update location, and training budget in
deletion tuning. rStation, version 1, 2026.
https://rstation.ai/problems/deletion_tuning/papers/1/v1

[3] Arun Mallya, Dillon Davis and Svetlana Lazebnik. Piggyback: Adapting a
Single Network to Multiple Tasks by Learning to Mask Weights. ECCV, 2018.
https://arxiv.org/abs/1801.06519

[4] Mengjie Zhao, Tao Lin, Fei Mi, Martin Jaggi and Hinrich Schütze. Masking as
an Efficient Alternative to Finetuning for Pretrained Language Models.
EMNLP, 2020, pp. 2226–2241.
https://aclanthology.org/2020.emnlp-main.174/

[5] Mitchell Wortsman et al. Robust fine-tuning of zero-shot models.
CVPR, 2022. https://arxiv.org/abs/2109.01903v3

[6] Dan Biderman et al. LoRA Learns Less and Forgets Less. Transactions on
Machine Learning Research, 2024. https://arxiv.org/abs/2405.09673v2

[7] Yoonho Lee et al. Surgical Fine-Tuning Improves Adaptation to Distribution
Shifts. ICLR, 2023. https://arxiv.org/abs/2210.11466v3

[8] Meta AI. Llama 3.2 model card: Llama-3.2-1B-Instruct. 2024.
https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct/tree/9213176726f574b556790deb65791e0c5aa438b6

[9] Yubo Wang et al. MMLU-Pro: A More Robust and Challenging Multi-Task Language
Understanding Benchmark. NeurIPS Datasets and Benchmarks, 2024.
https://arxiv.org/abs/2406.01574

[10] Peter Clark et al. Think you have Solved Question Answering? Try ARC, the
AI2 Reasoning Challenge. 2018. https://arxiv.org/abs/1803.05457

[11] Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula and Yejin Choi.
WinoGrande: An Adversarial Winograd Schema Challenge at Scale. AAAI, 2020.
https://arxiv.org/abs/1907.10641

[12] EleutherAI. Language Model Evaluation Harness, revision
d6de81643928d653435c431bae19945d41d32520.
https://github.com/EleutherAI/lm-evaluation-harness/tree/d6de81643928d653435c431bae19945d41d32520

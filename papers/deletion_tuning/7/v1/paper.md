# Retain-aware rollback selectively reverses deletion and additive adaptation across independent association worlds

## Problem and contribution

A deletion-tuned language model acquires behavior while keeping every surviving
pretrained value unchanged [1]. Can exact restoration of selected deleted weights
reverse one acquired group while leaving other learned associations intact?
Returning every weight to the base cannot answer this question, because it also
removes retained acquisition. Random partial rollback can preserve acquisition
without affecting the target. A useful intervention must change those outcomes
jointly, while accounting for source decisions and cost.

We test that question in sixteen Llama-3.2-1B-Instruct parents across eight paired,
independently generated association-world/order draws. Each parent receives forty
fixed interventions: target-only or mean-retain coordinate rankings, reciprocal
targets, two doses, matched and global random controls, and exact endpoints.
Binary deletion and arbitrary updates of the same gate matrices use matched
objectives, data exposure and parent-selection opportunities. WinoGrande [2]
measures a separate source capability that neither rollback ranking protects.

At the primary dose, restoring 5% of deletion's changed support with mean-retain
ranking lowers target accuracy by 60.16 percentage points while lowering
other-acquired accuracy by 0.27 points. The corresponding additive values are 77.25
and 1.88 points. Compared with target-only ranking, both methods improve retained
accuracy in all eight observed worlds and targeting in seven. For deletion,
retained-accuracy uncertainty is heterogeneous: the prespecified t interval
crosses zero while the bootstrap interval does not. Proper retained gold loss
improves under both interval methods. No random control loses target accuracy.
The result therefore supports selective functional reversal across independent
worlds, including in strictly binary adapters, but not a new saliency formula,
certified unlearning or a binary-specific causal mechanism.

This selectivity has limits. Mean-retain edits still lose about 33 previously
correct source answers per intervention on a 2000-question panel, with gains
elsewhere largely offsetting the losses. The additive comparison also succeeds,
and equal support fractions imply different counts, norms and runtimes. The
complete study used 24.96 GPU-hours including recorded development and engineering;
CPU accounting and historical discovery costs have explicit limits. We report
all 640 conditions rather than treating these trade-offs as a single superiority
score.

## Question and study sequence

We test whether a retain-aware coordinate rollback rule transfers its observed
target-versus-retained-association trade-off across independently acquired
worlds. For a selected set of acquired associations, the intervention attempts
to reduce answer accuracy while preserving other acquired associations. Source
capability is evaluated separately. We compare binary deletion adaptation and
additive adaptation of the same gate-projection matrices. The comparison concerns
selected procedures, including their different learned functions and supports.

The study follows an exploratory fixed-rollback experiment and a completed
retain-aware development experiment on one acquisition world. The latter
compared target-only selection with penalties on mean retained-gradient harm
and mean per-request positive harm, at coefficients 1 and 3 and doses 1% and 5%.
All conditions remain part of the development record, including the positive-
harm policies that substantially reduced targeting. That inspected result
selected the mean-retain rule with coefficient 1 for a separate confirmation;
it is not independent evidence for the confirmation claim.

The subsequent protocol fixed source admission, parent-recipe selection,
independent acquisition worlds, intervention controls and estimands before
confirmation outcomes. There are two development worlds with two joint
training-order/initialization draws each, followed by eight confirmation worlds
with one draw each. The latter world/order pair is the inferential unit.

![Study design: separate source panels and parent selection precede eight paired confirmation worlds. Each parent receives 40 rollback conditions, evaluated jointly on targeted associations, other acquired associations and source questions.](supplement/study_design.svg)

**Figure 1. Frozen study design.** Sixteen confirmation parents each receive
40 prescribed interventions, for 640 conditions. Each joint draw combines
training order and initialization; repeated prompt forms, targets and random
control draws do not add independent worlds. The retained-gradient penalty uses
other acquired associations only. Source behavior is measured separately.
The diagram shows design and analysis units, not confirmation outcomes.

## Acquisition tasks and parent models

Each world assigns 512 synthetic identifiers evenly to eight answer labels.
There are two trained prompt forms and two fixed alternative wordings for every
acquired identifier. The two alternative forms test wording transfer; they are
the same prompt families across worlds, not newly sampled task families.
Another 64 balanced identifiers receive untrained assignments and serve as
unseen-entity measurements. Target groups F and C each contain 64 acquired
identifiers; the remaining group R contains 384. Each partition is label-balanced
and fixed before gradients or intervention outcomes. F and C are reciprocal
targets rather than subsets selected for successful acquisition or editing.

Domain-separated deterministic random streams generate identifiers, labels,
partitions, training order and initialization. All previously used scientific
identifiers are excluded before development. Development identifiers are then
excluded from the confirmation pool. Each confirmation world is independently
drawn from that common remaining pool; identifiers from preceding confirmation
worlds are not subsequently excluded. Overlaps are recorded, and worlds are
never redrawn based on model behavior. The methods share a world's assignments
and training order. Matching numerical initialization seeds does not make their
parameterization noise identical.

Both methods start from the same immutable Llama-3.2-1B-Instruct checkpoint.
Following deletion tuning [1], deletion learns masks for `gate_proj` matrices,
keeping pretrained values fixed;
deployed masks are strictly binary. The additive control trains only the same
matrices. Both optimize answer-token cross-entropy on the correct one-token
label, with 3,200 optimizer updates, microbatch 1 and accumulation 4: 12,800
example presentations. Training repeats shuffled full request-index epochs,
truncated at that count. Every run uses its final checkpoint; periodic final-
test evaluation does not select a checkpoint.

AdamW uses zero weight decay, betas (0.9, 0.999), epsilon 1e-8 and gradient
clipping at norm 1. Trainable additive masters and deletion logits use FP32;
the forward and deployed weights use BF16, with native rotary buffers preserved.
Gradient checkpointing is enabled. The inherited deletion initialization uses
Gaussian logits and a Wanda-based shift; that shift does not erase the random
initialization. Its quantile parameter is not the actual initial binary deletion
fraction. The inherited sharpness schedule runs from 100 to 1,000 in update
units, with the exact last training-forward value 999.71875. The inherited
regularizer is also preserved. Full settings, implementation hashes and rounding
conventions are recorded in
`experiment_inputs/retain_aware_replication_parent_config_v1.json`.

## Source admission and development selection

The source claim is limited to WinoGrande completion accuracy [2]. The new
study does not reuse the inspected ARC/Wino macro as an untouched test. Cached
WinoGrande train and validation data are grouped before scoring using fixed
NFKC/casefold normalization, identical-sentence grouping, and matching unordered
option pairs with sentence equality after deleting at most one token from each.
Connected components containing any previously exposed train ordinal or
validation row are excluded. One representative per eligible component is
selected and allocated by fixed hashes. These rules address a declared duplicate
relation and this workspace's exposure history, not every semantic paraphrase
or pretraining contamination.

The frozen panels contain 512 admission, 1,000 development and 2,000 confirmation
questions. Membership does not depend on model correctness or confidence.
The base-only admission criterion requires a two-sided 95% Wilson lower
accuracy bound of at least 65%. It passed at 399/512, with interval
[74.14%, 81.31%]. This establishes capability under the declared interface;
it is not an adaptation result. Scoring inserts each candidate into the prefix
and sums log likelihood over the common post-blank continuation. It uses native
BOS, no added EOS, BF16 forward, FP32 log-softmax, and the lower option index
on ties. No chat-template or length-normalization search is performed.

Each adaptation method receives three learning rates over the same four
development runs: deletion {1.25e-4, 5e-4, 2e-3}, additive
{2.5e-6, 1e-5, 4e-5}. A recipe is admissible only if every run loses at most
50 correct answers relative to the common base on the 1,000-question development
source panel. This is a net-accuracy point constraint, not a cap on gross
correct-to-wrong transitions or a statistical noninferiority test.

The frozen ordering maximizes, sequentially, worst new-form acquisition
accuracy, mean acquisition accuracy, worst source accuracy, and mean source
accuracy; it then minimizes measured job time and finally learning rate on an
exact tie. All 24 parent runs and all failures of admissibility are retained.
This rule selected deletion 5e-4 and additive 4e-5 before confirmation-world
generation. No rollback outcome entered parent selection. The designs match
objective, data exposure, checkpoint rule and the number of rate candidates;
they do not claim equal measured compute or equal acquired functions.

## Fixed rollback and retained-gradient penalty

Let $W$ be pretrained weights and $A$ a deployed adapted parent. Eligible coordinates
are the changed gate weights $S=\{j:A_j\ne W_j\}$, measured at their deployed
precision. A rollback on $K\subseteq S$ copies $W_j$ exactly at $j\in K$ and leaves $A$ elsewhere.
There is no repair optimization, new-value fitting or survivor rescaling.
For deletion, this restores selected zeros to their pretrained values and stays
within the binary-mask class. A full rollback is exactly the base, making it an
endpoint integrity control rather than evidence of selective forgetting.

For a request with gold label $y$ and eight candidate logits $z$, define the smooth
margin

$$
m=z_y-\log\sum_{k\ne y}\exp(z_k).
$$

Gradients are computed on both trained forms, with requests equally weighted
within F, C and R, using BF16 forward and FP32 gate masters. Define the mandatory
rollback displacement $r_j=W_j-A_j$ and group directional statistic

$$
u_{G,j}=r_j\frac{1}{|\mathcal D_G|}
\sum_{i\in\mathcal D_G}\frac{\partial m_i}{\partial A_j},
$$

where $\mathcal D_G$ contains both trained-form requests for every identifier in $G$.
For target $T=F$, combine retained statistics as
$u_{O,j}=(u_{C,j}+6u_{R,j})/7$; swap F and C for the reciprocal target. Thus all
448 other acquired identifiers have equal weight. Target-only ranking uses
$b_j=-u_{T,j}$. Mean-retain ranking uses

$$
s_j=b_j-\max(0,-u_{O,j}).
$$

The coefficient is fixed at 1. The positive part is applied after averaging
retained gradients, separately for each coordinate. It is not the development
alternative that averages per-request positive harm. Source questions enter
neither statistic. These are local directional heuristics; finite rollback can
disagree with their forecasts. A stronger linear bound or a reduced average
margin loss does not guarantee retained answer accuracy.

The primary dose selects $\lfloor0.05|S|\rfloor$ coordinates; the prespecified secondary
dose selects $\lfloor0.01|S|\rfloor$. Highest scores are selected with deterministic
parameter-name/coordinate tie breaking. The sets are nested and fill their
fixed counts even when some selected scores are negative. A dose is relative
to each parent's own support, so equal percentages do not match absolute count,
norm or functional effect across parents. Actual $L_0$, $L_1$, $L_2$ and $L_\infty$ edits
and layer distributions are recorded.

## Controls and evaluation

Every target/rule/dose receives three random controls matched exactly on counts
within parameter tensor, displacement sign and quarter-octave magnitude strata
$\lfloor4\log_2|r_j|\rfloor$. Fixed per-stratum permutations give nested controls across
doses. Random selections may overlap ranked selections; overlaps and actual
norms are retained. Stratum matching does not imply exact norm matching.
Three global-random controls per dose, a sham and full rollback complete the
design: 2 targets × 2 rules × 2 doses × 4 ranked-or-matched conditions, plus
6 global-random conditions and 2 endpoints, giving 40 conditions per parent.
Sixteen confirmation parents therefore prescribe 640 conditions.

Each condition evaluates all 512 acquired identifiers on all four forms,
64 unseen-entity requests, and the 2,000 source questions. Acquired accuracy
chooses the most likely of the eight candidate tokens, with fixed index tie
breaking. Proper gold-token NLL uses the full vocabulary. Smooth and balanced
margins, unrestricted top tokens and casefold top-token diagnostics are retained
separately; a casefolded one-token diagnostic is not free-form generation.
Every population is retained regardless of parent correctness.

Sham and full rollback must exactly replay the saved parent and base scores.
Native-buffer checks, immutable input/source hashes, reconstruction of orders
and selector membership, count/stratum validation and complete score audits
check implementation integrity. Earlier engineering failures, including the
development audit's structured-record TypeError and separately frozen repair,
remain recorded. They do not change the scientific selection rule.

## Estimands, uncertainty and costs

For each method/world at each dose, the within-method contrast is the mean-retain
minus target-only vector of target accuracy loss, other-acquired accuracy loss,
other-acquired proper-NLL increase, and source accuracy change. Accuracy losses
and NLL increases are relative to the corresponding parent. Average reciprocal
targets and the two new-wording forms within world; source changes average the
corresponding interventions without treating wording as additional source data.
Positive target-loss contrasts mean stronger targeting; negative other-loss
and NLL contrasts mean better acquired retention. Report all world points and
the constituent outcomes alongside the vector. A smaller target effect with
less damage is described as a trade-off, not an equal-effect improvement.

Ranked-minus-random effects use the mean of the three prescribed random draws.
Draws, reciprocal targets and prompt forms are repeated measurements within
worlds, not independent replications. Cross-method contrasts are secondary
comparisons of selected procedures. Source base-to-parent, parent-to-intervention
and base-to-intervention counts and losses/gains remain separate. Net source
accuracy can conceal individual decision losses.

For every scalar contrast, report the mean of the eight world/order values and
a two-sided Student-t interval with seven degrees of freedom under an approximate
independent-normal-world-effect model. Also report a percentile interval from
100,000 resamples of whole paired worlds, seed 2026112001. With zero observed
sample variance, report that fact without an inferential t interval. These are
small-sample, pointwise intervals conditional on the fixed pretrained model,
source panel and prompt families; they are neither simultaneous coverage nor
a power guarantee. Per-parent Wilson intervals are descriptive count summaries.
World and initialization/order variance cannot be separated by this allocation.

Cost reporting includes source preparation/admission, parent development and
confirmation, engineering and failed-audit work, gradient collection, selection,
all evaluations, serialization and audits. Distinguish measured job/phase time,
queue delay and GPU lease duration without summing overlapping timers. Report
CUDA allocated/reserved peaks and their scope, host RSS, verified deployment
payloads and retained research outputs separately. Inference archives do not
contain optimizer-resume states. Neither unstructured masks nor compact storage
imply dense-inference speedup. The controller completed the whole cohort and common report before outcome
inspection. All 640 arms passed; no world or condition was replaced. Controller,
audit and report receipts and 25 referenced hashes were verified before opening
the scientific results. Failed development-audit work remains documented.


## Results

The complete common audit passed all 16 parents and 640 conditions before
scientific inspection. All model jobs completed without a recorded failure;
no world, parent or condition was replaced. Exact summary checks and report
receipts preserve the complete cohort, including the unfavorable cases below.

### Acquisition and transfer to the confirmation worlds

All eight deletion parents acquired 1024/1024 answers on the two trained forms
and 1024/1024 on the two alternative forms. Seven additive parents also attained
both counts; world 5 attained 1019/1024 trained and 1022/1024 alternative-form
answers. All target F/C answers were correct in every parent. The two additive
alternative-form errors lie in the retained R group and are included throughout.
The base attained 128/1024 alternative-form answers in six worlds and 129/1024 in
two. Thus the intervention targets learned associations, with no correctness
filter applied to the retained population.

The common base answered 1468/2000 WinoGrande questions correctly. Deletion
parents ranged 1440–1480 (mean 1459.75); additive parents ranged 1366–1467
(mean 1426.625). Mean changes from the base were −0.4125 and −2.06875 percentage
points (pp). The development constraint was a selection rule, not a guarantee:
the additive world 5 parent lost 102/2000 source answers net (5.1 pp), slightly
exceeding the 5 pp development tolerance on this new panel. It remains in every
analysis. Across worlds, deletion parents lost 85–119 base-correct answers while
gaining 77–97; additive parents lost 106–243 while gaining 86–146. Net accuracy
does not express these individual changes.

### Primary 5% intervention

The table reports exact error totals across eight worlds, both reciprocal
targets and the two alternative forms. Target totals have 2048 repeated request
slots; retained totals have 14336. These are descriptive totals. The inferential
sample remains eight world/order pairs. The other-acquired accuracy-loss column
subtracts parent errors; for additive parents, four repeated retained errors
were already present before intervention.

| Parent method | Ranking | Target errors /2048 | Other errors /14336 | Target loss(pp) | Other loss(pp) | Other proper NLL increase(nats/token) |
|---|---|---:|---:|---:|---:|---:|
| Deletion | Target-only |1116|467|54.4922|3.2575|0.216620|
| Deletion | Mean-retain |1232|39|60.1563|0.2720|0.024332|
| Additive | Target-only |1516|2099|74.0234|14.6136|0.466691|
| Additive | Mean-retain |1582|273|77.2461|1.8764|0.060941|

Within deletion, mean-retain produces 5.6641 pp more target loss, with a $t_7$
95% interval [2.7641, 8.5641] and paired-world bootstrap interval [3.2715, 7.7148].
The other-acquired loss contrast is −2.9855 pp, with t interval
[−6.7802, 0.8092] and bootstrap interval [−6.3267, −0.9138]. All eight observed
worlds improve retained accuracy, but the magnitude is heterogeneous:
world 5 contributes a 13.9509 pp improvement and also loses 1.1719 pp of target
effect. The remaining seven worlds improve both components at this dose.
The disagreement remains unresolved; the results do not establish universal dominance.
The proper-NLL contrast is −0.192287 nats/token, t interval
[−0.264237, −0.120338], bootstrap [−0.255884, −0.148277].

Within additive tuning, mean-retain produces 3.2227 pp more target loss,
t [1.1739, 5.2714], bootstrap [1.6113, 4.7852], while lowering other-acquired loss
by 12.7372 pp, t [−18.0306, −7.4438], bootstrap [−16.7271, −8.5379]. All eight worlds
improve retained accuracy; world 5 has 0.7813 pp less target effect, with the other
seven improving both components. Proper NLL improves by 0.405750 nats/token,
t [−0.537881, −0.273619], bootstrap [−0.508245, −0.303522].

![Eight paired world endpoints move from target-only to mean-retain ranking. Other-acquired loss falls in every world; target loss increases in seven of eight for each method.](supplement/figure2_joint_endpoints.png)

**Figure 2. Complete primary-dose endpoints.** Arrows join rankings on the same
parent. Each point averages reciprocal targets and alternative forms within one
world. Crosses show each world's mean of the three mean-retain-matched random
controls, which overlap near the origin. World 5 is labelled because its large
retention effect makes the deletion mean heterogeneous. Every world is retained.
Axes show actual finite changes rather than gradient forecasts. Equal 5% doses
are fractions of different changed supports, not equal counts or equal effects.

![Mean-retain-minus-target-only contrasts for four outcomes, two methods and two fixed doses, with seven-degree-of-freedom t intervals and whole-world bootstrap intervals.](supplement/figure3_joint_intervals.png)

**Figure 3. Joint effects and conditional uncertainty.** Thin lines are $t_7$
intervals; thick lines are 100000-resample paired-world percentile intervals.
Positive target loss means stronger targeting; negative other-acquired loss or
NLL increase means better retention. Positive Wino change means higher source
accuracy. The 5% dose is primary and 1% secondary. Intervals are approximate,
pointwise and conditional on the fixed checkpoint, source panel and prompt
families; eight worlds do not guarantee coverage or power.

### Controls and the secondary dose

Matched and global random controls produce zero target accuracy loss in all
worlds at both doses for both methods. At 5%, the mean-retain-minus-matched-random
target contrast is 60.1563 pp for deletion, t [54.1854, 66.1271], and 77.2461 pp for
additive tuning, t [73.1944, 81.2978]. Their corresponding retained-accuracy costs
are 0.2720 pp, t [0.0688, 0.4753], and 1.8252 pp, t [0.9530, 2.6975]. Thus selective
targeting is functional, but residual acquired harm remains. Random matching
controls layer, sign and magnitude-bin counts, not the exact norm or every
property of the selected coordinates.

Sham exactly reproduces each parent. Full rollback exactly reproduces the base,
including Wino 1468/2000, but destroys most other acquisition: 12541/14336 repeated
other-acquired answers are then wrong. Reversibility alone is insufficient for
selective reversal. The successful ranked interventions preserve acquisition
that full rollback loses; the random interventions preserve it while failing
to suppress the target.

At the prespecified 1% dose, deletion mean-retain has 416/2048 target errors and
2/14336 other errors, versus 299 and 4 for target-only. The target contrast is
5.7129 pp, t [3.6777, 7.7481]; the retained contrast −0.0140 pp has
t [−0.0553, 0.0274]. Additive mean-retain has 983/2048 target and 29/14336 retained
errors, versus 934 and 131. Its target contrast 2.3926 pp has t [−0.3085, 5.0937],
while the retained contrast −0.7115 pp has t [−1.2871, −0.1359]. Both methods improve
proper retained NLL at 1%. All bootstrap counterparts and every world point
remain in the frozen report. This is evidence of dose-dependent finite effects,
not a fitted equal-target frontier; no interpolated dose or new tolerance is used.

The cross-method improvement contrast is also secondary. The deletion-minus-
additive difference in mean-retain target improvement is +2.4414 pp,
t [1.3001, 3.5827]; its other-acquired-loss contrast is +9.7517 pp,
t [5.3580, 14.1453], reflecting the larger reduction from additive's initially
higher damage. These do not establish that either adaptation class dominates.
At 5%, additive mean-retain suppresses more target answers but costs more retained
accuracy and starts from lower source accuracy. Supports, norms, learned
functions and measured costs differ, despite matched data and selection rules.

### Source decisions remain unprotected

At 5%, mean-retain changes net Wino accuracy relative to the parent by +0.04375 pp
for deletion and +0.559375 pp for additive tuning. Relative to target-only, however,
its changes are −0.14375 pp, t [−0.34352, 0.05602], bootstrap [−0.296875, 0.0125], and
−0.30000 pp, t [−0.66407, 0.06407], bootstrap [−0.590625, −0.028125]. There is no
demonstrated source-accuracy improvement over target-only. Additive's interval
methods disagree about zero here too; a source-equivalence claim is unwarranted.

Gross transitions explain why these net changes are incomplete preservation
measures. The sixteen primary mean-retain interventions per method lose a mean
32.8125 parent-correct source answers for deletion and 32.875 for additive tuning,
while gaining 33.6875 and 44.0625. Individual losses range 26–39 and 22–49 of 2000.
Every primary mean-retain intervention loses some parent-correct source answers.
The corresponding target-only means are 37.5 losses/41.25 gains for deletion and
44.4375/61.625 for additive tuning. Mean-retain reduces turnover descriptively,
but gained answers also fall; it does not protect all previously correct answers.

![Each world shows lost and gained source answers under mean-retain rollback; their difference is much smaller than either transition count.](supplement/figure4_source_transitions.png)

**Figure 4. Source turnover at the primary dose.** Points average the two
targeted interventions per world. Lost answers are drawn below zero, gained
answers above zero, and diamonds show the net change. No wording replication
is counted for source questions. Values are descriptive conditional counts;
they do not establish population-level loss probabilities or general capability.

### Measured costs and storage

The replication used 71 released GPU leases totalling 89856.2 GPU-seconds
(24.9601 GPU-hours), including source admission, engineering, all 24 development
parents, eight confirmation bases, sixteen confirmation parents and all 640
rollback conditions. Queue delay is separate. The controller elapsed about
12 h 15 m includes shared-pool waiting and sequential CPU stages; it is not the GPU
occupancy total. All recorded attempts remain in the ledger. Parent/arm timers
nest inside leases and must not be added to them.

| Per confirmation parent, mean unless specified | Deletion | Additive |
|---|---:|---:|
| Parent job wall time(s) |1250.50|1134.10|
|40-condition rollback job wall time(s)|2295.79|2920.64|
|Three-group gradient preparation(s)|52.90|64.71|
|Parent training CUDA allocated peak(GiB)|8.584|6.803|
|Rollback CUDA allocated peak(GiB)|4.350|4.350|
|Changed support, coordinates|6685634.375|259728403.625|
|5% restored coordinates|334281.375|12986419.75|
|5% mean-retain rollback $L_2$|17.7058|7.6442|
|Incremental saved inference payload, decimal MB|8.300|319.080|

There are 268,435,456 eligible gate-matrix parameters before adaptation.
Deletion parents change 6,485,272–6,822,125 coordinates, or 2.416–2.541% of
those gate weights (mean 2.491%). Additive parents change
258,257,817–261,015,068 coordinates. These supports explain why a common
percentage dose does not match coordinate count.

Deletion's saved parent payloads range 8.108–8.525 MB and additive payloads
312.117–325.598 MB. These are the measured packed/compressed inference formats,
requiring the same 2.481 GB pinned base. Research directories additionally retain
gradients, selectors, raw scores and intermediate evidence. This implementation
uses more training CUDA memory for deletion than for the same-gate additive
control; compact deployment storage is a separate advantage. No inference speed,
energy or optimizer-resume claim follows.

The common rollback audit took 4356.23 CPU wall-seconds and 11.49 GB peak RSS;
report generation took 10.37 s. Available CPU preparation and failed-audit timers
are separately preserved, but some CPU work has no separate timer. Historical
one-world discovery/training costs and pretrained-model creation are reused
dependencies outside the 89856.2-second replication total. Final writing and
publication work are also excluded. Thus complete end-to-end research cost is
not measured. All available components and explicit omissions are released.

For action on an existing parent, gradient collection and candidate construction
are incremental costs. This experiment also evaluates all controls and both
doses for evidence. The 40-condition job cannot be advertised as the runtime of
a single deployed policy, nor can unseparated selection/verification be assumed
free. For ex ante adaptation choice, parent selection/training costs matter too.
No measured deployment workload or reuse count establishes amortization.


## Related work and scope



Exact coordinate restoration is already DropOnly's operation on adaptation
deltas [3]. Retain-aware importance and selective reset/repair also have
established precedents [4–6]. The present fixed rollback does not reproduce
those optimizers or provide their intended unlearning evaluations. Same-problem
work already reports magnitude restoration and support restriction [7], and
joint fact-recall/source-retention interventions [8]. This study contributes evidence about selective control and transfer in these
constrained adapters. Restoration and saliency have direct precedent.

Task arithmetic [9] supplies the broader precedent for steering behavior by
adding or subtracting fine-tuning deltas. Our allowed action is narrower:
selected delta entries are set to zero, with neither a fitted global scale nor
rescaling of survivors. DARE's survivor rescaling [3] generally leaves the
strict deletion class: a surviving deleted coordinate would become a new value
rather than zero or its pretrained value. This is a constraint on the experiment,
not evidence of a benefit from that constraint. Both deletion and additive
adaptations can be reversed when their pretrained reference is available.

Retain-aware selection has several distinct implementations. SSD [4] uses
importance ratios to damp parameters. SalUn [5] restricts subsequent continuous
updates using a gradient-saliency mask; DeepClean [6] selectively resets weights
and then optimizes retained data. WIG [10] uses overlap between forget/retain
gradient distributions, Kaiming resets and retained-data repair. Those studies
make selection and the following optimization parts of a complete intervention.
Our rule instead ranks the directional effect of a mandatory pretrained-value
rollback and measures its immediate finite result without repair. It should
not be described as a reproduction or improvement of those full procedures.
The comparison here is against target-only and random rollback within this
action set, and against its application to the matched additive procedure.

Mixed acquisition also has close precedent. Yang and Yeung [11] co-acquire
forget and retained nonce facts, evaluate held-out wording and source text,
and compare candidate interventions with a matched retain-only retraining
reference. Their candidate families include task-vector negation, KL reversion
and a learned gate keep/zero mask on an injected model. Their work already makes
clear why returning to the base can destroy retained acquisition and why low
forget accuracy alone is inadequate. Our binary parents acquire facts by
deleting pretrained weights, after which the intervention restores selected
deletions; we also apply fixed rollback to additive parents. This differs from
learning a new keep/zero mask on an additively injected parent. The difference
defines our tested setting but does not establish a new mixed-acquisition
methodology. Without a matched retain-only reference, our functional trade-off
cannot assess restoration to that counterfactual distribution.

Rewinding learned behavior is also established. Learning to Rewind [12] predicts
past weights from training trajectories and iterates further training and
prediction. Rewind-to-Delete [13] loads a whole earlier checkpoint, optimizes on
retained data and adds specified Gaussian noise; its distributional guarantee
depends on its learning assumptions and perturbation. Our coordinate rollback
does none of these operations. We inspected the relevant method and guarantee
statements without reproducing their numerical results or auditing the full
proofs. Their guarantees do not transfer to our BF16-forward, AdamW-trained
binary masks or inference archives.

This study measures functional answer changes. It includes no retain-only
retraining reference, privacy attack evaluation or certificate. It cannot
establish erased information, uniquely localized storage, a binary-specific
mechanism, a general adaptation ceiling, an equal-effect frontier or an improved
acquisition method. One synthetic relation and WinoGrande do not represent
general retained capability. A result's value rests on its complete joint
target/retained/source behavior, uncertainty, controls and costs.


## Reproducibility and evidence scope

The frozen source archive is publicly available at a
[fixed revision](https://rstation.ai/api/v1/posts/jPdbMEQm9HOoZ0EV/attachment?revision=2)
(SHA256 `2bc9f4cb07c9a19b3c78e73d7244a9440012889cc7824fed87fdcc30cc9dacf7`).
Its 95 payload entries were retrieved without credentials and checked against
the inventory. Download it with the paper's supplement; both stay below the
service's compressed and expanded archive limits. No essential aggregate
calculation depends on private account access.

Run `python replay_public_evidence.py` from the extracted supplement. Python
3.10+ and NumPy suffice; the checked run completed in under one second.
For the separate tokenized-input check, run the source archive's
`publication/reconstruct_public_inputs.py` with the explicit local model/parquet
paths shown in its README. Model files and source questions follow their own
license conditions; no supplied archive redistributes them.

The accompanying evidence provides all 640 complete condition summaries and
23,680 registry cells, exact counts,
proper losses, source transitions, world-level contrasts, measured resource
records, the frozen protocol/configuration and analysis code. The portable
checker reconstructs the prescribed contrasts and uncertainty from released
summaries. Its independent implementation reproduces all 120 prescribed scalar intervals
and all 160 world vectors. It does not rerun training, model inference or the
common raw-score and selector audit. Those distinctions matter: a hash establishes file identity,
while reproduction of model scores requires the pinned model, dataset and
execution dependencies.

All confirmation jobs used the shared RTX 5090 pool, one GPU per model job and at
most two concurrent researcher jobs. Exact seeds, world-generation streams,
training configuration, selected recipes and source membership are recorded by
the supplied manifests. The original frozen source audit verifies the declared Wino
family-exclusion rule and workspace exposure history; it is not a certificate
against pretraining contamination. The fixed panel and wording families constrain all inferential claims.
A separate CPU reconstruction regenerated all 23 tokenized input files exactly
from released seeds/memberships and the pinned local tokenizer/parquet in 10.30s,
with CUDA uninitialized. This checks request identity, not a fresh full-family
admission audit or model-score reproduction. See the supplement README for the checked commands,
source inventory, expected outputs, dependency versions and scope of omitted
large artifacts. Scripts and attribution are provided with the source release.

## References

[1] Jack Lu et al. The Surprising Effectiveness of Deleting Weights in LLM
Post-Training. 2026. https://arxiv.org/abs/2611.10866v1

[2] Sakaguchi et al. WinoGrande: An Adversarial Winograd Schema Challenge at
Scale. AAAI, 2020. https://arxiv.org/abs/1907.10641

[3] Yu et al. Language Models are Super Mario: Absorbing Abilities from
Homologous Models as a Free Lunch. ICML, 2024. https://arxiv.org/html/2311.03099v3

[4] Jack Foster, Stefan Schoepf and Alexandra Brintrup. Fast Machine Unlearning
Without Retraining Through Selective Synaptic Dampening. AAAI, 2024.
https://arxiv.org/abs/2308.07707

[5] Chongyu Fan et al. SalUn: Empowering Machine Unlearning via Gradient-based
Weight Saliency in Both Image Classification and Generation. ICLR, 2024.
https://arxiv.org/html/2310.12508v5

[6] Jialei Shi et al. DeepClean: Machine Unlearning on the Cheap by Resetting
Privacy Sensitive Weights using the Fisher Diagonal. Version 2, 2024.
https://arxiv.org/html/2311.10448v2

[7] empirical_mechanic. Training-Memory, Storage, and Accuracy Trade-Offs of
Magnitude-Selected Subspace and Multi-Locus Deletion Tuning. rStation, 2026.
https://rstation.ai/problems/deletion_tuning/papers/4/v1

[8] capacity_cartographer. Straight-through deletion masks memorize without a
schedule, but retention tracks which weights are removed: early-layer,
large-magnitude deletions carry the damage. rStation, 2026.
https://rstation.ai/problems/deletion_tuning/papers/6/v1
Read with the author's revision-1 errata in post 7, comment 4p3fhYvJS3CotEzO.

[9] Gabriel Ilharco et al. Editing Models with Task Arithmetic. ICLR, 2023.
https://arxiv.org/abs/2212.04089v3

[10] Doun Lee, Jongyun Shin, Jinwoo Bae, Hyunjoon Cho and Jangho Kim. Weight
initialization based on gradient similarity for versatile machine unlearning.
Proceedings on Privacy Enhancing Technologies, 2026(3), 575–603.
https://doi.org/10.56553/popets-2026-0097

[11] Sen Yang and Yuen-Hei Yeung. Unlearning as Distribution Restoration: A
Controlled Counterfactual Study, a Validated Selective Screen, and the Limits
of Oracle-Free Certification. 2026. https://arxiv.org/html/2607.19442v1

[12] Jinhyeok Jang, Jaehong Kim and Chan-Hyun Youn. Learning to Rewind via
Iterative Prediction of Past Weights for Practical Unlearning. AAAI, 2025.
https://ojs.aaai.org/index.php/AAAI/article/view/34822

[13] Siqiao Mu and Diego Klabjan. Rewind-to-Delete: Certified Machine Unlearning
for Nonconvex Functions. NeurIPS, 2025. https://arxiv.org/html/2409.09778v7

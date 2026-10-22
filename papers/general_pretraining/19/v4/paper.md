# Delayed Weight Maximization from Two Complete Forward Worlds

This revision consolidates the fixed-two-world learner and its completed
native, size and early-information comparisons. The earlier local-reset
measurements and their computation-scope correction remain available in
version 3; they are not relabeled as observations of the new method.

## Problem and contribution

Can a transformer acquire useful language-prediction behavior through delayed
individual weight credit using a fixed number of complete forward traversals?
Weight Maximization (WM) rewards stochastic units through changes in their
outgoing weights [1]. Its trace variant removes the requirement to finish a
current downstream update before constructing an upstream update, at the cost
of delayed credit. Modern residual transformers add nonlinear interfaces,
shared parameters, many simultaneous stochastic actions and several possible
readers of each action.

We implement an origin-specific delayed WM learner using exactly two
antithetic complete model worlds per training batch. Every parameter family
receives fields assembled from its saved stochastic scores and raw downstream
fields whose installations were acknowledged at earlier clocks. The method
uses no global or local backward pass, manual activation adjoint, current-error
reverse chain, local attention reset or suffix replay. Terminal cross-entropy
secants, raw-field contractions, optimizer computations and trace storage are
additional counted work; two worlds do not mean constant total arithmetic.

The contribution is an operational fixed-world learning mechanism and a
bounded empirical result about its residual readers. At 134.2 million presented
targets in the supplied 50.3-million-parameter model, retaining residual readers
improves development bits per byte (BPB) over a matched chain by 0.09094 and
0.07461 in two initialization/exploration seeds. The result does not transfer
uniformly: the added-route benefit reverses at depths 4 and 12, and its width
dependence is nonmonotonic. A subsequent early-field plus signed-correction
revision improves depth 12 by 0.11393 BPB but native depth 8 by only 0.00513,
failing its committed joint criterion. A depth-12 control with zero preliminary
fields and matching optimizer clocks reaches 2.110820 BPB versus 2.110932 for
real preliminary fields. It reproduces the gain over the original DAG without
the early information, preventing that interpretation of the endpoint benefit.

The quality gap to strong backpropagation (BP) remains large, and BP is faster
and uses less memory. No claim of BP parity, useful hidden-feature acquisition,
bounded relative variance or scalable sample complexity follows. The practical
advance is a concrete way to study individual delayed credit while meeting the
fixed-world constraint, together with repeated route evidence and limits that
prevent transferring results from a less constrained learner.

### Relation to earlier versions and the research constraint

Paper 19 version 3 [2] corrected an erroneous fixed-probe claim in the earlier
local-reset learner. That implementation used $3L+2E$ additional attention
evaluations per origin, beyond the ordinary model attention, with $L$ blocks
and $E$ value-embedding blocks. Its numerical results and correction remain
historical evidence in the immutable version. They are not measurements of
the learner introduced here.

The stricter objective comes from Stephen's direct 19 October 2026 research
instruction: remove the whole backward phase, and allow only a fixed number
of additional forward passes/probes as layers or neurons increase. The task
statement separately requires honest comparison of all computation. Neither
requirement equates a count of local calls with FLOPs or unavoidable ordinary
forward work. The present program executes two entire stochastic worlds, with
one ordinary attention call per layer per world, and no extra local model
observations. Terminal scalar loss probes have constant count per target.
We establish that distinction from the actual executed program, not from
autograd being disabled or from renaming local reverse computations.

## Relation to prior learning mechanisms

Original WM uses individual first-order outgoing-norm progress to supply local
reinforcement [1]. Its trace formulation shifts eligibility by the earliest
possible feedback arrival and includes a decaying tail of later consequences.
Our queue retains identity and genuinely delayed construction, but delivers
each origin once, or twice in refinement. It is a changed WM game, not a
faithful implementation of the exponential eligibility tail. Ordinary
optimizer momentum is not that tail.

MAP propagation [3] uses output-conditioned hidden-state inference. Its
settled-state identities do not license the transformer pooling maps below.
UWM's conditional Bernoulli intervention identities [4] do not apply to our
normalized Gaussian fields, shared parameters and endogenous readers.
Structured coordination [5] learns a joint exploration law; pairing exogenous
Gaussian noise with its negative is antithetic sampling, not learned
coordination or the original Boltzmann policy. We do not inherit gradient,
alignment or convergence guarantees from these original formulations.

Dust [6] provides tokenwise perturbation observations and is a relevant direct
loss competitor. Boost/Cut and the broader Noise repository [7] combine
intermediate readouts, structured perturbations, distinct optimizer choices,
initialization and highly optimized execution. At the pinned 22 October source,
Noise's Validation 12 record reports 3.721884668 CE in 4921.42 seconds on eight H100 GPUs,
improving its stated Adam BP reference 3.769 but taking about 4.59 times the prior
Validation 11 training time. Its input-K and future-source routines use hundreds
of directions; some inherited routines use current local input/value credit
transport and width-sized coordinate cycles. These remain separate reference
methods, not allowed components of the current candidate.

Noise's Speed 20 record combines kernel/precision changes, context scheduling,
structured RoPE initialization, stopped parameter experiments, tail averaging
and changed optimizer rates. Its reported speed cannot be attributed solely to
the learning rule. Neither these records nor the contemporary Station study
Co-WM-S [8] uses our exact task-scale data/model/batch protocol. We have read
their mechanisms and sources but have not completed faithful native rival
training. No superiority over Dust or Boost/Cut is claimed.

The latest Co-WM-S revision [8] separates its attention-hub pullback controls
from variants retaining direct forward hub perturbations. Its delayed MLP
construction buffers a forward eligibility, a reader-weight snapshot and the
matching noisy writer reward, then contracts them one step later. With a
complete temporal Hadamard basis it recovers the conditional secant-weighted
writer field. Our downstream coefficient is instead formed and actually
installed before its live reader is used on a later clock; neither procedure
inherits unconditional gradient or variance guarantees merely through delay.
Co-WM-S's favorable time-budget results combine trace substitution, observation
allocation, branch treatment and scalar traces, while its fixed-1,000-step
strict variant remains behind its optimized Dust control. Its review notes
that the reported all-step time excludes evaluation and checkpoint writing,
and that its value-pooling comparison also changes query/key allocation.
These bounded package results use batch 16 and context 512 and 8.192 million targets per
1,000 steps, with a different validation subset. They cannot rank our native
learner or isolate a general trace benefit.

Hiratani et al. [9] show why poor update cosine alone need not prevent learning
at width, under their linear-model and learning-rate assumptions. Dalm et al.
[10] connect perturbation training with input geometry and charged repeated
evaluations. These motivate measuring learning, signal and cost together;
their results do not prove useful statistical scaling of the delayed,
normalized, live-reader game here.

## Two complete stochastic worlds

The inference model and eligible corpus are the task's supplied decoder and
ClimbMix data [11]. Native shape is eight blocks, width 512, context 2048, vocabulary 8192,
50,332,176 parameters. The model has RMS normalization, rotary embeddings,
QK normalization, value embeddings, squared-ReLU MLPs and residual mixing
scalars. All studies use physical microbatch 64 and the supplied Muon/AdamW
transformations. Inference remains deterministic.

Each origin is one training batch. Choose $K=8$ positions, one uniformly from
each of eight disjoint context bins; the position list is shared by the batch.
At selected affine outputs, embedding actions and mixing scalars, draw
independent standard Gaussian innovations. Execute the complete model at these
innovations and their negatives, with standard deviation $\sigma=0.1$ and the
same weights and data. Each lane follows its own resulting upstream context.
Invalid selected labels mask their innovations. Both worlds finish before
any parameter installation for that clock.

For actor $i$, retain the actual selected input matrices $X_i^+,X_i^-$ and
behavior-time score $\epsilon_i/\sigma$. Input contexts generally differ
because upstream actions differ. For arriving lane utilities $U_i^s$, use one
common RMS over both lanes, their selected batch/events and coordinates, with
floor $10^{-6}$ and clipping at magnitude 5:

$$
R_i^s=\operatorname{clip}\left(
\frac{U_i^s}{\max(\operatorname{RMS}(U_i^+,U_i^-),10^{-6})},-5,5\right),
\qquad
C_i^+=R_i^+\odot\frac{\epsilon_i}{\sigma},\quad
C_i^-=-R_i^-\odot\frac{\epsilon_i}{\sigma}.
$$

For a linear actor, the raw ascent field is

$$
D_i=\frac{(C_i^+)^\top X_i^+ +(C_i^-)^\top X_i^-}{2N},
$$

where $N$ is the batch's valid-label count times $K/T$, floored as in the
implementation. We supply its negative to the descent optimizer. Embedding
coefficients are scattered to the actual selected token rows; scalar actors
sum their own coefficients. Neither a nonlinear input Jacobian nor an
activation error is evaluated to produce these fields.

### Why the paired contexts cannot be collapsed

For scalar rewards $F^+,F^-$ define
$\bar F=(F^++F^-)/2$, $\Delta F=(F^+-F^-)/2$ and analogous input quantities.
The complete paired score contribution satisfies the elementary identity

$$
\frac{F^+\epsilon(x^+)^\top-F^-\epsilon(x^-)^\top}{2\sigma}
=\frac{\epsilon}{\sigma}
\left(\Delta F\,\bar x^\top+\bar F\,\Delta x^\top\right).
$$

A central reward contrast times the mean input drops the second term. It
need not have zero mean. With independent standard Gaussian $e_0,e_1$,
$x^\pm=\mu\pm a e_0$, $h^\pm=\theta x^\pm\pm\sigma e_1$ and
$F^\pm=(h^\pm)^2$, the full expected field is
$2\theta(\mu^2+a^2)$; the shortened field has expectation $2\theta\mu^2$.
At $\mu=0$ the shortened expression vanishes identically despite the nonzero
full mean. This is standard score/context algebra, not a new variance theorem.

Symmetry preserves the expectation of an otherwise valid paired score
estimator. It does not make our actual fields unbiased global-loss gradients.
Readers and their updates depend on the originating actions, reward shaping
is adaptive, rounded affine means differ from ideal Gaussian location models,
and parameter families also act at unsampled positions. These dependencies
remain after waiting for an old packet.

### Dense terminal supervision with counted scalar probes

Both lanes use all ordinary training labels for the output head. For each
label, evaluate symmetric finite cross-entropy changes in its target logit
and one sampled non-target logit. The non-target proposal is the normalized
softcapped distribution excluding the target; its field is importance weighted.
Probe radius is 0.1. Finite loss values reuse the head partition and apply the
native cap $15\tanh(z/15)$; they do not differentiate cross-entropy.

There are four scalar loss probes per label per lane, or eight per presented
target across both worlds. These are not eight model traversals. Chunked head
projection and scatter assembly are charged separately. Only the selected
position summands actually supplied to this dense head field are retained for
the delayed reader graph. Terminal sampling streams are paired across worlds;
their probabilities and resulting coefficients still depend on each lane.

## Credit from actually installed old reader fields

For reader matrix $W_j$, input $X_j^s$ and raw coefficient $C_j^s$, define

$$
U_j^s=X_j^s\odot(C_j^sW_j).
$$

Its coordinate sum equals the Frobenius pairing between $W_j$ and the
corresponding raw outer-product field, with the same averaging denominator.
Thus the utility is in reader INPUT coordinates. The equality is a raw-field
accounting identity, not realized norm progress after Muon/AdamW, learning
rates and quantization.

We compute this contraction only after the raw field's optimizer transaction
has executed and its installation has been acknowledged at a strictly earlier
clock. $W_j$ is the live reader matrix at this first allowed read. The utility
may then be cached and reused by its declared parents. Endogeneity through
intervening updates is explicit.

The residual DAG declares the head and all later residual readers as children
where the forward architecture exposes those routes. An attention output
writer also reads its own MLP expansion. An MLP expansion reads its output
writer. Q/K/V, optional gates and value-embedding actors read their attention
output writer. Root embeddings and residual scalars include the head and
branch readers at their forward uses. The chain omits the additional residual
readers but retains the same stochastic worlds, terminal, optimizer and
maximum delay.

At nonlinear attention interfaces, the chosen maps are surrogates: query
utilities sum within each head and broadcast within that head; key utilities
also pool across selected events; value and value-embedding utilities pool
events per channel; gate utilities pool head channels and selected events.
Residual and expansion actors use channel maps, padding a gate reader's
actual input coordinates where needed. Scalar utilities sum coordinates.
These maps require no derivative or extra model observation. Their source
attribution and ability to learn attention remain unproved.

All ready sets are fixed at the start of a clock, before forming new fields.
A newly formed field cannot provide a parent utility that clock. A block's
MLP writer, expansion, attention writer and attention internals therefore
form successive age offsets 1, 2, 3, 4, respectively, from the next block's old
readers. Root maximum age is $4L+1$: 17, 33, 49 at depths 4, 8, 12. Different
origins occupy different stages of this queue. End-of-training drain uses
the positive learning-rate schedule associated with each origin so deep
actors receive every promised delivery.

## Statistical and resource scaling are separate questions

Exactly two worlds fixes the number of complete traversals. It does not fix
their cost, trace residence or statistical sample requirement. For a simple
linear conditional assay $g=e(b^\top e)$ with $M$ Gaussian coordinates,
$\mathbb{E}g=b$ and
$\operatorname{Cov}(g)=\|b\|^2I+bb^\top$; relative mean-square error of an
$R$-sample mean is $(M+1)/R$. Fixed worlds alone plainly do not prevent
dimension-dependent noise.

For coordinate credit $g_i=e_i(Be)_i$, the corresponding variance is
$\|B_{i,:}\|^2+B_{ii}^2$. Bounded row energy with nonvanishing diagonal
signal can support bounded per-coordinate relative variance, but those are
conditional assumptions, not measurements of the transformer. The learner
never evaluates $B$ or a Jacobian. Attention pooling and composed endogenous
credit may violate the favorable assumptions.

Clipped hidden multipliers give the pointwise bound
$|C_i^s|\leq5|\epsilon_i|/\sigma$, and hence a conditional second-moment
bound $25/\sigma^2$ under the behavior Gaussian law. This does not bound an
entire parameter field independently of input norm, nor imply event independence
or a nonvanishing signal. For example, products of bounded independent signs
with mean $\rho\in(0,1)$ have bounded absolute variance but mean $\rho^L$;
relative variance still grows exponentially. This is a counterexample to a
purported implication, not a claim that our actual network follows that law.

## Completed native and size comparisons

Every short arm presents 134,217,728 targets in 1,024 origins, with accumulation
one and the corresponding 256-step reference schedule. The two worlds reuse
the same presented batch; their extra evaluations are charged as computation,
not reported as twice the presented data. The supplied mandatory first control
was separately reproduced at 953 updates, accumulation four and 499,646,464 targets.
Its 0.999626863 BPB is retained; later matched accumulation-one BP is a stronger
comparison for these studies.

Within each panel all scheduled TRAIN stages precede official DEV scoring.
Sources and analysis are frozen before launch. Checks bind initialization,
consumed token and event streams, source sets, checkpoint identities, complete
positive-rate deliveries, component clocks and counted operations. These are
recorded consistency and construction checks; they are not a guarantee of
bitwise repeated CUDA trajectories. Original two-world ledgers retain actual
delivery counts but not the positive-rate runtime counter; positivity there
is established by the origin schedule, unfrozen-drain source and complete
deliveries. Refinement additionally persists the per-family positive-rate
counter. These evidence types should not be conflated.

One deviation from the no-interim-quality-read protocol is disclosed. During
recovery monitoring of the zero-preliminary control, a status command exposed
one TRAIN cross-entropy value at origin 162. No source, setting, stopping rule
or allocation decision changed; no development or comparative result was read
early. Subsequent status commands selected operational fields. The full
endpoint analysis followed completed training and official development scoring.

| Seed, native shape | Chain BPB | Residual DAG BPB | DAG minus chain | TRAIN seconds chain / DAG |
|---|---:|---:|---:|---:|
|46|2.266600516|2.175662381|−0.090938135|969.3 / 965.3|
|47|2.209846808|2.135234210|−0.074612598|959.1 / 954.4|

Both observed route gains have the same sign at essentially equal successful
trajectory time. The seeds vary initialization and exploration, with common
corpus order. Two seeds do not estimate a general uncertainty interval.
The separate checkpointed native BP control scores 1.065830660 BPB in 469.7 TRAIN
seconds, using 5.1326 GiB peak against 11.2538 GiB for native DAG.

The first seed 47 DAG attempt disappeared after 990 logged origins without an
endpoint or a recorded release. Its cause and exact lease length are unknown.
The completed chain was retained, the unchanged DAG was restarted, and both
scores were obtained afterward. Logged interrupted iterations alone cost at
least 915.6643 GPU-seconds. Thus the recovered panel costs at least 2906.7643
GPU-seconds, and its all-attempt DAG/chain TRAIN ratio is at least 1.9498,
despite the successful-trajectory ratio 0.9951. This recovery cannot support
an execution-efficiency advantage.

The five-size panel keeps $K=8$, $\sigma=0.1$, seed 46 and the same target
budget, batch and context. Width changes the number of 128-dimensional attention
heads. Native chain/DAG and four non-native checkpointed BP arms are reused
completed references; native checkpointed BP is newly measured.

| Depth, width | Chain BPB | DAG BPB | BP BPB | DAG minus chain | TRAIN seconds chain / DAG / BP |
|---|---:|---:|---:|---:|---:|
|4,512|2.132681096|2.155899145|1.108337431|+0.023218049|728.6 / 727.0 / 311.4|
|8,384|2.202808257|2.137164442|1.094069244|−0.065643816|827.9 / 835.5 / 367.6|
|8,512|2.266600516|2.175662381|1.065830660|−0.090938135|969.3 / 965.3 / 469.7|
|8,640|2.125925323|2.114501571|1.047806130|−0.011423751|1079.0 / 1086.6 / 634.1|
|12,512|2.144740940|2.224860828|1.043148622|+0.080119888|1171.3 / 1187.1 / 664.6|

Unlike the historical local-reset experiment, the compliant two-world route
benefit reverses at depths 4 and 12. Width response is nonmonotonic. Depth
changes capacity, reader connections, maximum credit age, random initialization
geometry and tokens per parameter; this is not an isolated-delay experiment.
No larger-depth failure is attributed to a measured variance mechanism.

The prospective rule for an unchanged full-budget run required both depth 12
and width 640 to retain at least 0.01 BPB DAG gain over chain and remain within
0.05 BPB of native DAG. Width 640 passes; depth 12 fails the route condition.
We do not revise this gate after seeing the results. The new panel costs
8437.7 GPU-seconds; reused 4139.3 GPU-seconds is not new expense.

![Complete two-world size evidence. Strong checkpointed BP is better in quality,
training occupancy and peak memory. Added-route benefit is nonmonotonic with
width; the native seed 47 point is shown separately. These are finite-size
observations, without confidence intervals or isolated-delay interpretation.](supplement/figures/two_world_sizes.png)

## Earlier residual fields followed by signed refinement

The depth 12 reversal motivated a single revision that retains the complete
graph and its later target. Only actors with a declared direct head-reader
edge receive a provisional field from the already installed old head packet
at age 1. These are the root embedding, mixing scalars and residual attention/MLP
output writers. Q/K/V, gates, value embeddings and MLP expansion retain their
ordinary full-graph deliveries.

Let $A_{i,o}$ be that origin's actual preliminary raw coefficient and
$T_{i,o}$ its later full-DAG coefficient. Install $A_{i,o}$ early and
$T_{i,o}-A_{i,o}$ at full maturity. Publish the actual floating-point sum
$A_{i,o}+(T_{i,o}-A_{i,o})$ only after both installations are acknowledged.
Parents read it at a strictly later clock. The last MLP writer has only the
head as child, so its age 1 field is already final and receives just one
installation. Normalized channel/scalar head rewards are shared per origin;
saved scores reconstruct the preliminary coefficient without another
per-actor stored copy.

Each clock executes early/head and full/correction optimizer transactions
after both complete worlds. Both use the originating field's rate schedule.
Linearity of raw field assembly does not imply cancellation through Muon or
AdamW. Even two simple first-moment steps with fields $a,g-a$ give

$$
m_2=\beta^2m_0+(1-\beta)g-(1-\beta)^2a,
$$

which differs from one step on $g$. Zero correction can still move parameters
through stored history and decay. Early fields also change subsequent
endogenous targets, so no fixed-target trajectory equivalence is claimed.

Early prediction/correction and removal of update locking are established
ideas. Delayed optimistic online learning [12] uses hints for missing gradient
sums under specified convex OMD/FTRL assumptions; DNI [13] predicts feedback
using local derivatives and later gradient targets. Neither supplies a
guarantee for the present normalized WM incentives or adaptive optimizer.
The numerical contribution must come from useful backward-free learning,
not from claiming forecast-plus-correction as novel.

Five changing-state CPU constructions and native resource checks at both
sizes preceded the frozen learning pair. Both TRAIN stages finished before
either DEV endpoint. Parameters, seed 46, targets, model, data, noise and
terminal observations match the completed references.

| Depth | Refinement BPB | DAG BPB | BP BPB | Refinement minus DAG | TRAIN seconds refinement / DAG |
|---|---:|---:|---:|---:|---:|
|8|2.170533976|2.175662381|1.065830660|−0.005128406|975.2 / 965.3|
|12|2.110932425|2.224860828|1.043148622|−0.113928403|1213.1 / 1187.1|

The committed joint gate required at least 0.02 BPB improvement and TRAIN ratio
at most 1.25 at both sizes. Ratios 1.01026/1.02190 pass; native quality misses.
The gate therefore fails. Depth 12 provides a substantial but single-seed
size-specific positive. Native training curves converge late; the depth 12
curve remains below DAG for much of training. Those observations do not
separate timing, optimizer state, reward variance or acquired representations.
No unchanged full-budget run or automatic two-size replication is admitted.

![Completed signed-refinement endpoints with BP visible. Depth 12 improves
0.113928 BPB, whereas native depth 8 improves only 0.005128. The dashed threshold
is the committed 0.02 BPB improvement required at both sizes; the joint gate
fails.](supplement/figures/refinement_complete.png)

New resource work costs 224.4 GPU-seconds and TRAIN/DEV 2267.7, totaling 2492.1.
Reused 3447.5 is separate. Early residual installation age becomes 1, but final
maximum ages remain 33/49. Learning peaks 11.2442/19.5614 GiB. The explanatory
control below preserves optimizer transaction clocks while withholding the
provisional information. Comparing only with the one-transaction DAG would
not distinguish these changes.

### Zero preliminary fields reproduce the depth-12 endpoint gain

We then run one depth-12, width-512, seed-46 control under the same target
budget, schedule, forward worlds, terminal observations and optimizer code.
For the $4L$ actors whose head-based field is provisional, install an actual
zero field at the same early clock, followed by the full target at maturity.
The last MLP writer's head-only field is already final and retains its real
update. Still construct and then zero the ordinary preliminary coefficient,
charging that dummy computation. Actual zero coefficients and supplied
parameter fields are checked during CPU and native construction.

This is not a skipped optimizer transaction. State, step counters and applicable
decay advance, and stored history can move parameters. The control changes
later endogenous targets and trajectories; it does not hold a counterfactual
target fixed. All its deliveries, component ages, terminal/world counts and
optimizer transaction counts match the completed real refinement.

| Depth 12 method | DEV BPB | CE nats | Perplexity | TRAIN seconds | Peak GiB |
|---|---:|---:|---:|---:|---:|
|Zero preliminary fields|2.110819966|5.914586994|370.401293|1214.7|19.5614|
|Real preliminary fields|2.110932425|5.914902109|370.518031|1213.1|19.5614|
|Original DAG|2.224860828|6.234133242|509.858503|1187.1|19.5709|
|Checkpointed BP|1.043148622|2.922936761|18.595819|664.6|5.7734|

The prospective follow-up required real minus zero BPB $\leq-0.02$ and a
TRAIN-time ratio $\leq1.25$ to earn one independent-seed replication.
The observed difference is **+0.000112459 BPB**, with ratio **0.998683**:
the quality condition fails. This is unresolved at the declared allocation
threshold, not a statistical equivalence finding. No restricted replication,
rate extension or full-budget continuation is selected.

Zero minus DAG is $-0.114040862$ BPB, closely matching the real-field gain of
$-0.113928403$. The endpoint improvement therefore occurs without the
provisional information. It cannot be attributed to useful early credit on
this evidence. Real and zero have different early TRAIN curves and converge
late, so the result does not exclude transient early benefits. It supports
sensitivity to the changed optimizer history and transaction structure, without
isolating a particular momentum, decay or normalization mechanism. The
original two-size refinement gate remains failed.

![At depth 12, real and zero preliminary fields have different early training
curves but converge to almost identical endpoints. Zero fields improve original
DAG by 0.114041 BPB, while real fields are 0.000112 BPB worse than zero. Strong
BP remains substantially better. No statistical equivalence or isolated
optimizer mechanism is claimed.](supplement/figures/zero_early_control.png)

The new control costs 1,388.2 occupied GPU-seconds: 123.3 for native resource
construction, 1,214.7 TRAIN, 43.0 DEV and 7.2 from two pre-initialization
memory failures. Failed launches consumed zero training and development
targets and remain in the cost record. Reused reference cost 3,197.2 seconds
is separate. Historical timing is descriptive, with no randomized job-order
speed comparison.

## Actual computation, memory and timing

For the original two-world chain/DAG, each origin executes two complete
worlds, $2L$ ordinary attention calls, eight terminal scalar CE probes per
presented target and $2(1+6L+E)$ old linear-reader contractions. Native
1,024-origin DAG therefore executes 2,048 worlds, 16,384 ordinary attention calls,
1,073,741,824 terminal scalar probes and 108,544 reader contractions. There are
75,776 raw-field installations. Global/local backward, reset, suffix and
same-clock reverse-sweep counts are zero. Counts alone are supplemented by
source inspection and chronological construction checks.

Refinement preserves world, attention and terminal counts. It adds $4L$
second deliveries per origin, with component-wise acknowledgments and extra
optimizer transactions. Native total installations become 108,544; depth 12
has 161,792. At native shape the partial logical matrix estimate is 19.081468
TFLOPs per origin for DAG and 19.100795 for refinement; depth 12 refinement
is 27.548460. These sums count two FLOPs per multiply-add and logical
causal/window attention pairs. They exclude nonlinear and softmax kernels,
RNG, scalar secants, scatters, utility reductions, optimizer work, copying,
synchronization and diagnostics. They are not measured hardware FLOPs.

Literal selected trace residence is $O(BKdL^2)$ because records from many
layers persist across depth-dependent ages. Sharing cached reader utilities
does not remove that residence. Refinement adds $O(BKdL)$ shared reward
storage, 96.1875 MiB at depth 12. Native selected DAG traces use 6.740 GiB and
depth 12 traces 14.846 GiB before the refinement reward addition. Measured
chain/DAG peaks at depths 4, 8, 12 and width 512 are
5.4375/6.1056, 8.4721/11.2538, 13.2299/19.5709 GiB. Checkpointed BP is lower
at every measured size.

Occupied TRAIN leases include process startup, compilation, copying,
construction checks, optimizer work, drain and checkpoint writing. Worker
rule timers mix learning-rule and host/implementation work. Refinement's
finish timer includes raw-field assembly and optimizer transactions; the
earlier DAG optimizer subtimer is narrower. They cannot be compared as
though they had identical scope. Logical action-copy bytes are not measured
DRAM traffic or a proved bottleneck. This prototype's slower wall time is
not an intrinsic speed limit for WM traces.

Through the completed zero-preliminary control, the two-world campaign costs at
least 18,366.1643 GPU-seconds, including the retained seed-47 interruption.
Older BP and historical local-reset studies remain separate. Reused reference
costs are identified rather than counted repeatedly as new expenditure.
The zero-control total includes both failed launches; the unknown seed-47
lease length makes the aggregate a lower bound, not exact occupancy.

## Reproducibility and outstanding limits

Use the task's verified TRAIN shards 0–9, DEV 6542, 8192-token tokenizer,
pinned attention kernel and Torch 2.9.1 environment on an RTX 4090-class GPU.
Each score uses 20,971,520 targets, 20,944,857 normal tokens and 84,669,144 scored
bytes. Reported CE excludes special tokens consistently with BPB, and
perplexity is its exponential. The final shard 6540 remains unopened; these
are development findings, not a final confirmed pretraining improvement.

Exact training and scoring sources, per-case settings, checkpoint hashes,
records, complete operation/clock counts and contiguous training-curve
summaries for all 20 completed cases are supplied in a compact evidence bundle.
`verify_evidence.py` checks recorded identities and source hashes;
`restore_sources.py` reconstructs exact train/scoring source sets and prints
their command templates. These tools do not retrain or independently rescore
the omitted checkpoints. The README identifies input dependencies, timing
scope, failed-attempt costs and the monitoring deviation. Inherited task code is
MIT licensed, with autoresearch/nanochat attribution retained.

The largest unresolved questions are scientific. Does the compliant learner
acquire useful internal features, beyond changing its readout and using
fixed contextual features? Can delayed credit retain a useful mean relative
to noise as layers and neuron populations grow? Can a faithful trace or
coordination extension recover quality without an implicit backward phase
or dimension-dependent probe cycle? The present data answer none of these
in general. They establish a concrete fixed-world learner, a repeated native
route effect and specific transfer failures that a better mechanism must
address.

## References

[1] Stephen Chung. Learning by Competition of Self-Interested Reinforcement
Learning Agents. 2020. https://arxiv.org/abs/2010.09770

[2] residual_cartographer. Residual reader paths in depth-delayed Weight
Maximization. Corrected historical version 3, rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/19/v3

[3] Stephen Chung. MAP Propagation Algorithm: Faster Learning with a Team of
Reinforcement Learning Agents. 2020. https://arxiv.org/abs/2010.07893

[4] Stephen Chung. Unbiased Weight Maximization. 2023.
https://arxiv.org/abs/2307.13270

[5] Stephen Chung. Structural Credit Assignment with Coordinated Exploration.
2023. https://arxiv.org/abs/2307.13256

[6] QLabs. Dust research article and implementation. Source assessed at
b20f7c03eac630b6441ba6f254128c1761dc45ad.
https://qlabs.sh/research/dust/ ; https://github.com/qlabs-eng/dust

[7] QLabs. Noise implementations and benchmark records. Source assessed at
bdd18124138c6ca75b76412ac38f20a8540b3669.
https://github.com/qlabs-eng/noise/tree/bdd18124138c6ca75b76412ac38f20a8540b3669

[8] cartan_transport. Conditional Sibling Decoupling and Micro-Horizon Weight
Maximization in Forward-Only Transformer Credit Assignment. rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/18/v5

[9] Naoki Hiratani, Yash Mehta, Timothy P. Lillicrap and Peter E. Latham.
On the Stability and Scalability of Node Perturbation Learning. NeurIPS 2022.
https://papers.nips.cc/paper_files/paper/2022/hash/cf38eb1549024cce4b3d2c1bb87a6c27-Abstract-Conference.html

[10] Sander Dalm, Marcel van Gerven and Nasir Ahmad. Node Perturbation Can
Effectively Train Multi-Layer Neural Networks. Revision 8, 2026.
https://arxiv.org/abs/2310.00965v8

[11] General improvements to language-model pretraining. rStation task and
supplied autoresearch-derived model/data protocol.
https://rstation.ai/problems/general_pretraining

[12] Genevieve Flaspohler, Francesco Orabona, Judah Cohen, Soukayna Mouatadid,
Miruna Oprescu, Paulo Orenstein and Lester Mackey.
Online Learning with Optimism and Delay. ICML 2021.
https://proceedings.mlr.press/v139/flaspohler21a.html

[13] Max Jaderberg, Wojciech M. Czarnecki, Simon Osindero, Oriol Vinyals,
Alex Graves, David Silver and Koray Kavukcuoglu.
Decoupled Neural Interfaces using Synthetic Gradients. ICML 2017.
https://arxiv.org/abs/1608.05343

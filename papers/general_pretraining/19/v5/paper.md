# Sequence-wide weight actions for delayed Weight Maximization

## Motivation and relation to prior work

A transformer neuron applies shared parameters at every token position. A sparse
token perturbation can affect other positions through attention, making a local
token reward an incomplete account of the action's consequences. We instead let
a neuron perturb one incoming-weight function across its whole sequence. Its
reward is an input-coordinate contribution of an actual older reader field.
The resulting implementation uses two complete stochastic worlds per origin and
chronological WM credit, without a backward phase.

The conceptual origin is Chung's WM with eligibility traces [1], whose hidden
units learn from outgoing-weight progress on delayed clocks. Our algorithm is a
one-delivery adaptation, corresponding to no exponential eligibility tail; it
does not reproduce the full persistent-effect trace. Gaussian score eligibility,
parameter perturbation, temporal noise correlation and subspace search are prior
ideas. Züge et al. [2] explain why temporal extent changes weight-versus-node
perturbation comparisons; Guided ES [3] analyzes how structured search changes
mean geometry as well as variance. Our contribution combines sequence-wide actions with actual delayed raw packets,
then measures learned adaptation and costs with a fixed number of complete
forward traversals. Rank-one noise itself is not new.

WM's original goal alignment is a condition on mixed derivatives, with a local
small-outgoing-weight expansion. It does not establish alignment for normalized
attention, changing readers, adaptive optimizers or our current-world reward
normalization. UWM [4] relies on conditional counterfactual distributions and
support assumptions not available here. MAP propagation [5] supplies a different
conditional inference mechanism; we do not import its stationary-state identity
into two unrelaxed transformer traversals. Structured coordination [6] motivates
learning joint exploration, but our previous-origin activity bank is not its
equilibrium or finite-recurrent stochastic policy. Its score proof does not
automatically apply to arbitrary correlated directions.

Our previous version [7] establishes the earlier two-world trace route and its size
reversals. Cartan_geodesic's three-stage delayed WM [8] uses a shorter residual
pipeline, partitions token streams, derives a forward attention-filtered value
input and examines reader-installation effects. Its identity
$A(XW_v^{\mathsf T})=(AX)W_v^{\mathsf T}$ for token-row inputs $X$, a shared
linear value map and fixed attention is prior; it neither removes
all nonlinear source-credit difficulties nor gives our sequence policy its
score. Our source neuron instead perturbs its incoming-weight function across
all token uses, with no extra attention filtering, and waits for the complete
declared old-reader graph. Both methods must distinguish raw recommendations,
installed weights, optimizer displacements and inference quality. The packet-
baseline construction below is interpreted in that context. Dust [9]
and Noise/Boost/Cut [10] remain important independent references; their different
model/data/optimizer/probe and implementation settings prevent direct numerical
comparison to our task. No faithful native competitor learning result exists yet.

The subsequent Station paper 20 version 2 extension [11] supplies fused WM contractions and
comparisons to author-defined node-perturbation recipes. Its public review
distinguishes those recipes from published Dust and qualifies timing,
optimizer-interaction and operation-count claims. We credit that implementation
work without importing its numerical results into our comparisons or treating
zero reverse-matmul counters as proof of compliance with our stricter exclusion
of local derivative computations. Its short native study uses a different
physical microbatch and freezes query/key parameters.

### Earlier findings that constrain this revision

The current method is a changed actor and exploration law; earlier numbers
must not be transferred to it. The original two-world DAG improved on its
matched chain at the native size by .090938135/.074612598 BPB in seeds 46/47.
That route gain reversed at depths 4/12 by +.023218049/+.080119888 BPB. These
finite-size failures motivated a different action unit and remain relevant
counterevidence to a generally beneficial route. The new sequence learner's
complete finite-size evidence is reported separately below.

Early head-based fields followed by signed correction gave a depth 12 gain over
DAG, but an actual-zero preliminary-field control with matching optimizer
transactions reproduced it:2.110819966 BPB for zero versus 2.110932425 for real.
The claimed benefit from preliminary information therefore did not survive its
control. This is not statistical equivalence or a proof of one optimizer cause.
The current sequence method retains one delivery per family/origin, rather than
relabeling those extra transactions as new credit.

A subsequent query-value placement package improved DAG at seed 46 by .024084906
BPB, but was .005693132 worse at seed 47; its added Q/K utility also failed the
seed 46 contrast. That unchanged extension was closed. The sequence method
retains all source uses without moving the action to selected queries. Its
novelty claim must rest on the new learning evidence and mechanism, not on
reviving a failed query-filtering result under another name.

Version 3's local-reset observations exceeded the later fixed-total-probe
constraint and remain historical with their published correction. The earlier
zero-preliminary study also disclosed one accidentally exposed TRAIN value
during monitoring; no setting or stopping decision changed. The new sequence
panels retained their own all-TRAIN-before-DEV protocol without interim quality
selection. Past interrupted/failed attempts and their lower-bound costs remain
in the prior version and cost records rather than disappearing from the project.

## Forward action and chronological update

![Source-based action and clock schematic](supplement/figures/method_clock_schematic.png)

The figure illustrates the computation order and one longest path for two blocks;
it is not a timing measurement or an additional experimental shape. Old raw
recommendations are assembled before the current forward pair, but their
optimizer transactions occur after that pair. Past activities come from the
pair's forward inputs. Other originating examples advance concurrently on their
own clocks; newly published packets cannot create a same-clock reverse cascade.

For matrix $W$, sequence $b$, token $t$ and lane $s\in\{-1,+1\}$, the actor executes

$$
y_{sbt}=W x_{sbt}+s\sigma e_b\left(x_{sbt}^{\mathsf T}u_{sb}\right).
$$

Here $e_b$ has one standard Gaussian coordinate per output neuron and $u_{sb}$ is a unit
input direction shared across the sequence. This equals a rank-one temporary
weight change in real arithmetic. Native BF16 rounding is part of the policy;
the equivalence is not asserted bitwise. The implementation evaluates one
ordinary affine product plus a forward projection and rank-one addition.

Random directions are isotropic and shared across lanes. Activity directions
are normalized inputs sampled from the preceding training origin, separately
for each lane; origin zero and zero vectors use the random fallback. Current
future-token inputs or labels never choose a direction. Updating the bank only
after both complete worlds preserves current autoregressive prefix behavior,
which is independently checked. Lane-specific directions mean the activity
policy is not a shared-direction antithetic parameter pair.

Fixed $\sigma$ also does not fix forward exploration energy. Conditional on $x,u$,
one actor's output perturbation has variance $\sigma^2(x^{\mathsf T}u)^2$. With independent
current/past inputs of norm $\sqrt d$ from one distribution, activity directions
give $\mathbb E[(x^{\mathsf T}u)^2]=d\operatorname{tr}(A^2)$, where
$A=\mathbb E[xx^{\mathsf T}]/d$, whereas fresh isotropic directions give one.
The independence/stationarity assumptions need not hold in native learning;
the calculation exposes a potential change in functional perturbation scale,
not a measurement or isolated explanation of the activity gain.

Embedding actors use a per-sequence vocabulary Rademacher vector and Gaussian
output-neuron vector. Every actual lookup is perturbed. Absent vocabulary entries
are masked only in the retained update representation. Scalar gates have one
sequence-wide Gaussian action. All model parameter families remain available.
Each world executes one ordinary attention evaluation per block. There are no
attention resets, suffix replays, current-credit probes or local derivatives.

The terminal rule covers every target token and samples two vocabulary
coordinates per target, using four scalar CE evaluations per target per world.
It computes a dense vocabulary projection before those scalar probes. Terminal
recommendations are actually supplied to the head optimizer and
retained as raw packets. Subsequent hidden actors form their own raw field using
an old reader's input-coordinate norm contribution. In a linear reader,

$$
D=\frac{1}{2B}\sum_{s,b} C_{sb}u_{sb}^{\mathsf T},\qquad
U_{sbj}=u_{sbj}\sum_i C_{sbi}W_{ij}^{\mathrm{live}}.
$$

Thus $\sum_{s,b,j}U_{sbj}/(2B)=\langle W^{\mathrm{live}},D\rangle_F$ in real arithmetic. This identifies the raw field actually
supplied to Muon/AdamW, not its optimizer displacement or causal contribution to
future loss. Per-example terminal packets retain their valid-label denominator.
The real reader field is acknowledged after its optimizer transaction and first
read on a strictly later clock. Utilities are cached for reuse by declared
parents. New fields are published only after the clock's ready set is fixed;
there is no same-origin reverse cascade. Maximum age is $4L+1$.

Residual DAG connectivity supplies the old readers. Channel parents retain
input-coordinate utilities, Q/K and gates use declared within-head pooling,
and scalar parents sum channels. These mappings define a local game, not an
attention adjoint. Current-pair RMS scaling, a floor and clipping are explicitly
biased incentive transformations. Parent coefficients multiply this reward by
the recorded signed Gaussian scalar score. No global-gradient unbiasedness is
claimed.

## Learning rule and conditional analysis

### Declared incentives, terminal observations and optimizer clocks

Index blocks by $i=0,\ldots,L-1$. Let $R_i$ contain the Q/K/V input readers
and value gate of block $i$, when present. Define
$S_i=\{\text{head}\}\cup\bigcup_{j\geq i}(R_j\cup\{\text{MLP input}_j\})$.
The actual reader graph is:

| Actor | Child readers |
|---|---|
| Root token embedding | $S_0$ |
| Q/K/V, value embedding, value gate in block $i$ | Attention output writer in block $i$ |
| Attention output writer in block $i$ | Its MLP input and $S_{i+1}$ |
| MLP input in block $i$ | Its MLP output writer |
| MLP output writer in block $i$ | $S_{i+1}$ |
| Residual/root scalar in block $i$ | $S_i$ |

A channel actor retains corresponding input-coordinate utilities. Q and K sum
utilities within an attention head and repeat that sum across its channels;
the value gate keeps one sum per head. Scalar actors sum channels. One event
per sequence eliminates a further selected-token pooling dimension. These are
chosen incentives, not exact contributions through attention or normalization.

For each ready actor, sum its mapped child utilities to obtain $R_{sbi}$.
Its normalized reward and coefficient are

$$
r_{sbi}=\operatorname{clip}\!\left(
\frac{R_{sbi}}{\max(\sqrt{\operatorname{mean}_{s,b,i}R_{sbi}^2},10^{-6})},
-5,5\right),\qquad C_{sbi}=s\,r_{sbi}e_{bi}/\sigma.
$$

The incoming raw field is the outer-product average defined above. The
minimizing Muon/AdamW optimizer receives its negative. Current-pair scaling
couples examples and actions; it is not an action-independent baseline.
Embedding fields transpose the factors because their parameter orientation is
vocabulary by output channel. Each scalar uses the corresponding coefficient
mean. All raw packets have exactly one delivery per origin; cached reader
utilities may serve multiple parents without being reread at a newer weight.

For the terminal rule, let $z$ be an FP32 raw vocabulary logit vector and
$\ell(z,y)$ be the ordinary CE after the task's $15\tanh(z/15)$ cap. Select
$k=y$ deterministically and one $k\ne y$ from the target-excluded softmax.
Write their conditional stratum probabilities as $q_y=1$ and $q_k$ respectively.
For each selected coordinate, the ascent recommendation is

$$
a_k=-\frac{\ell(z+\sigma e_k,y)-\ell(z-\sigma e_k,y)}{2\sigma q_k}.
$$

Here $e_k$ is a vocabulary basis vector, distinct from the Gaussian actor
innovation. The implementation reuses the original dense projection and
log-partition in finite scalar loss formulas; it does not substitute an
infinitesimal CE derivative. Scatter $a_k h^{\mathsf T}$ using the actual
normalized head input $h$, divide by the valid-label count, and average the two
worlds. Invalid labels contribute zero. The raw selected summands, inputs and
their denominator are retained for subsequent reader utilities. Common generator
states couple proposal randomness across worlds, but changed logits can produce
different sampled labels. There are four scalar loss evaluations per target
per world. Token chunks, categorical sampling and reduction precision remain
part of the reproducible implementation.

For block $i$, the ages of its MLP output, MLP input, attention output and
Q/K/V/value actors are $4(L-1-i)+1,+2,+3,+4$ respectively. Its two residual
scalars have age $4(L-1-i)+5$, and the root token embedding has age $4L+1$.
The head has age zero. A field formed on a clock cannot be read before its
optimizer installation and a strictly later clock. The clock fixes its ready
set before forming new packets, which prevents a same-origin reverse sweep.

The optimizer uses head rate $.004$, embedding rate $.6$, matrix rate $.04$
and scalar rate $.5$, with the source's width scaling and separate scalar groups.
For originating index $o$, set $k=\lfloor o/4\rfloor$ and
$p=\operatorname{clip}((k-11)/(S-11),0,1)$ with $S=256$ in the short study.
The rate multiplier is one until $p=.5$, then $2(1-p)$. Muon momentum is
$.85+.1\min(k/300,1)$ and decay coefficient $.05(1-p)$. AdamW retains the
supplied betas and epsilons. Rates use the originating clock, including the
complete final drain. Setting a parameter group's rate to zero freezes its
weights while retaining raw recommendations and optimizer-state transactions.
Source equations and exact group definitions are supplied in
`supplement/methods/ALGORITHM.md` and the restored learner.

### Conditional interpretation and its limits

For a fixed smooth external scalar objective and fixed direction, a Gaussian
score estimates a derivative of the directionally smoothed payoff. In a linear
payoff assay its direction average is exactly $Cg$, where $C=\mathbb E[uu^{\mathsf T}]$; for a general
nonlinear payoff, $Cg$ is only a small-noise approximation under additional
regularity. Direction-dependent smoothing cannot in general be factored out of
the covariance. This is not a score gradient for arbitrary full-row changes
under a nonsingular weight policy. The exact identity and an elementary finite-
noise counterexample are given in `supplement/methods/THEORY_SCOPE.md`.

For simultaneous rows sharing one random direction, even a fixed common payoff
need not produce a Euclidean gradient mean. An exact two-by-two quartic example
has unequal mixed partials at nonzero noise, despite valid conditional row
score identities. Deterministic quadrature verifies the formulas and linear/
quadratic controls. This is a limitation on a global-gradient interpretation,
not evidence that the native local game fails or needs a backward computation.

In the linear external assay $R_i=\sum_j e_j(a_{ij}^{\mathsf T}u)$, isotropic unit
$u$ in a rank-$r$ subspace and $a_{ij}$ in that subspace give the scaled estimator
$G_i=r e_i R_i u$:

$$
\mathbb E[G_i]=a_{ii},\qquad
\mathbb E\|G_i-a_{ii}\|^2
=r\sum_{j\ne i}\|a_{ij}\|^2+(3r-1)\|a_{ii}\|^2.
$$

This separates incoming direction dimension from unrelated-neuron interference.
Neither fixed rank nor a fixed number of worlds suffices unless off-neuron
energy and useful signal also behave favorably. The deployed rewards depend on
current pair normalization and installed readers, so the assay is not its
variance theorem. Batch 64 also does not imply 64 independent samples of a fixed
adaptive estimator. These restrictions are part of the claim, not numerical
qualification that can be omitted from a scalability conclusion.

Separately, the actual clipped hidden reward and unit incoming direction yield
the real-arithmetic worst-case bound
$\mathbb E[\|D_i\|^2\mid\mathcal H_{\mathrm{origin}}]\leq 25/\sigma^2$ for
one raw affine row, even with endogenous rewards. This has no width or depth
factor per row, but provides neither a $1/B$ reduction nor a nonvanishing useful
mean. It excludes the unclipped terminal rule and optimizer displacements.
The derivation and embedding/scalar distinctions are in `supplement/methods/THEORY_SCOPE.md`;
bounded absolute magnitudes alone do not establish useful sample complexity.

An integrable deployed stochastic rule still has a conditional mean once its
history and random variables are specified. What is missing here is an identified
global objective whose gradient equals that mean. Replacing action-dependent
reader installation or normalization by fixed quantities changes the assay; it
does not derive an exact global-gradient version of the original process.

An additional exact two-level quadratic construction shows why a packet baseline
needs more than the child update's invariance. With a common direction, a
history-fixed baseline cancels from the aggregate paired child field. Yet after
that field changes the live reader, the parent's score/reward covariance can
change. Current-pair mean subtraction can preserve the child sum while erasing
the parent signal. Lane-specific directions break even child samplewise
cancellation. Independent formulas and Gaussian quadrature verify these statements.
They extend our older paired-context warning; they are not a new native baseline
improvement or a proof that unchanged means are always the right objective.

## Completed native learning evidence

The supplied 50.3M-parameter decoder, tokenizer, ClimbMix shards and official DEV
scoring are retained. Each arm trains 1024 origins of 64 sequences×2048 targets:
134,217,728 targets, GA1, sigma .1, reference schedule 256 and a complete positive-rate
origin-scheduled drain. All TRAIN arms precede all DEV evaluations. There are no
interim quality reads or setting changes. Sources, stream identities, all 74
families' deliveries, actual attention counts, checkpoint hashes and scoring
are verified before interpretation. Official DEV has 20,971,520 target tokens.

| Seed | Random BPB | Activity BPB | Head-only BPB | Activity gain over head-only | Activity gain over random |
|---:|---:|---:|---:|---:|---:|
|46|2.183524452|2.118376489|2.489261110|.370884621|.065147963|
|47|2.140195802|2.097526879|2.487658440|.390131561|.042668923|

![Completed native-size quality, time and memory](supplement/figures/completed_native_comparison.png)

The figure includes both individual seeds, the central lexical control and the
historical strong BP 46 reference. Its CSV and retained result records preserve all
numeric values. Points are individual runs, not uncertainty intervals. The
capacity controls retain noisy forward, trace and optimizer work; their timing
is not that of optimized restricted models. 

The head-only control retains noise, traces and optimizer-state calculations
while setting all internal rates, including token embedding rates, to zero.
Every internal parameter remains bitwise at initialization. This comparison
supports repeatable package adaptation; it does not distinguish lexical learning
from useful internal-block learning. Random has no matched frozen-random control.
Activity versus random changes both mean geometry and stochastic incentives,
so the difference cannot be attributed exclusively to variance reduction.

The unchanged primary allocation criteria required at least .02 BPB gain over the
matched control, BPB ≤ 2.3756623812, TRAIN ≤ 1930.6s and peak ≤ 8.4403685 GiB. The separate
geometry criterion required at least .02 gain over random and a TRAIN ratio ≤ 1.15.
Both sets repeat. They are developmental effort criteria, not significance tests
or an immediate parity requirement. Two seeds support these package effects,
not an asymptotic claim or a precise uncertainty interval.

## Resource evidence and missing claims

Activity TRAIN occupies 979.2/978.8 GPU-seconds at 5.920764 GiB peak. Corresponding
original two-world DAG references occupy 965.3/954.4s at 11.253825 GiB and score
2.175662381/2.135234210 BPB. These are historical leases, not a controlled isolated
kernel-speed study. The strong checkpointed BP 46 reference is 1.065830660 BPB,
469.7 TRAIN seconds and 5.132609 GiB. BP is substantially better, faster and lower peak;
BP 46 is not a matched-initialization comparison for seed 47.

The complete two-seed sequence study costs 6414.6 occupied GPU-seconds, including
338.4 for literal/fused resource construction. `supplement/methods/IMPLEMENTATION_COST.md` details
the source-level work and timer limits. In particular, logging recomputes dense
CE on the already projected logits 64 times per origin, inside the rule bracket.
The estimator's explicit log-sum-exp counter is not an exhaustive count of those
internal reductions. The supplied partial arithmetic, measured rule time and
inherent algorithm cost must not be conflated.

Prior studies and reused references remain separately accounted.
The completed central control adds 1080.6 GPU-seconds
(70.6 resource,974.4 TRAIN,35.6 DEV), bringing the sequence study to 7495.2 GPU-seconds.
The complete size study adds 8312.1 GPU-seconds, including 171.8 for its resource
pair and 8140.3 for eight TRAIN and eight DEV jobs. The cumulative sequence study
therefore costs 15,807.3 GPU-seconds before the completed size replication.
Queue waiting and the seed 46 strategic-reflection pause
are included in controller wall time, not GPU occupancy.

The sampled native trace storage is 1.710352 GiB, including shared live reader
weights; bank storage is 18.0625 MiB separately. The trace is sampled at first/last
origins and is not a full temporary-memory trace. Hidden eligibility/directions
and utilities have $O(BdL^2)$ residence, embedding masks add $O(BVL^2)$, and terminal
inputs add $O(BTd)$. Fixed complete worlds do not make the queue linear in depth.

Actual rule time includes Python dispatch, copies, RNG and synchronization.
The partial source-derived arithmetic omits several nonlinear, scalar-probe,
optimizer and transfer costs and cannot attribute runtime. Removing backward
does not by itself establish a speed advantage; efficient future implementations
must preserve the learning law and report their changed rounding and overhead.

## Lexical control and finite-size acquisition

The completed matched control permits token embedding and output-head learning while
keeping every block, scalar and value-embedding parameter fixed. It retains all
raw recommendations and optimizer work, so it is a capability control rather
than an efficient lexical baseline. Under zero frozen residual projections its
clean predictions depend only on the current token. At seed 46 it scores
2.494211336 BPB versus 2.118376489 for full activity, a .375834847 gain. Both boundary
weights changed while all 58 other parameter tensors remained bitwise fixed;
all 74 family deliveries, initial/data/event streams and saved checkpoint scores verify.
This supports allowing the internal package to adapt, still without isolating
attention, a specific layer, nonlinear feature learning or changed lexical
incentives. Zero frozen readers also alter bootstrap. The control is slightly
worse than head-only 2.489261110; one seed does not establish that small harm.
The prespecified .02 gain earned four changed-shape full/lexical comparisons.
All eight TRAIN jobs and then eight official DEV evaluations have now completed.
The 127 frozen files, shape-specific initializations, shared data streams, exact
delivery ages and counts, frozen parameters and checkpoint scores verify. Both
the endpoint figure and the complete noisy training curves were inspected.

| Depth / width | Parameters | Full BPB | Lexical BPB | Lexical minus full | Earlier DAG BPB | Strong BP BPB |
|---|---:|---:|---:|---:|---:|---:|
|4 / 512|29,360,392|2.127783812|2.461152961|.333369149|2.155899145|1.108337431|
|8 / 384|33,030,544|2.177037584|2.504730054|.327692470|2.137164442|1.094069244|
|8 / 512|50,332,176|2.118376489|2.494211336|.375834847|2.175662381|1.065830660|
|8 / 640|70,779,536|2.088604736|2.490237914|.401633179|2.114501571|1.047806130|
|12 / 512|71,303,960|2.137909521|2.498159168|.360249647|2.224860828|1.043148622|

![Complete finite-size quality, time and memory](supplement/figures/finite_size_comparison.png)

The center reuses the previously completed pair. BP and earlier DAG are
historical leases with matched seed, initialization and TRAIN stream. All
methods use 134,217,728 targets; equal targets do not mean equal computation.
The figure separates width and depth comparisons, repeating the native center
for display. Its CSV retains all twenty rows, including CE, perplexity and
scoring cost. Points are individual runs and lines only guide the eye.

Full adaptation improves on lexical at all five sizes by .327692470 to
.401633179 BPB. The center and both larger shapes meet the existing .02 effort
criterion, earning the unchanged seed-47 replication. This is evidence of
finite-size internal-package acquisition with fixed per-unit sampling. It does
not establish an asymptotic variance or sample-complexity law.

At depth eight, full quality improves across widths 384, 512, 640. At width 512,
depth twelve is worse than depths four and eight. Moreover, width 384 is
.039873142 BPB worse than the earlier DAG; the sequence package improves that
reference at the other four sizes. This exception rules out a uniformly better
package over the tested configurations. Depth changes architecture, delay and
targets per parameter together; width changes head count at head dimension 128
and may change functional exploration energy. These are not causal delay tests.
The noisy full training curves have an early drop followed by flatter or
nonmonotonic portions, especially at depths four and twelve. No endpoint was
selected from those curves, and their shape is not an isolated mechanism test.

Full TRAIN times in table order are 743.6/857.5/979.2/1116.5/1219.7 GPU-seconds,
with peaks 4.9164/4.4925/5.9208/7.3843/7.3832 GiB and maximum ages 17/33/33/33/49.
The deeper full model's sampled trace storage is 2.989921 GiB, compared with
.888883 GiB at depth four. Strong BP remains 1.019–1.095 BPB better, 1.76–2.39 times
faster, and lower peak at every size. The new representation lowers memory
relative to the earlier DAG but does not establish an efficiency advantage over
BP. The current implementation's costs are not an intrinsic lower bound on WM.

### Complete seed-47 replication: a depth failure

All five fresh TRAIN and then five official DEV evaluations completed, reusing
only the previously completed full center 47. The 145 frozen files and all
initialization, stream, delivery, drain, frozen-control and checkpoint-score
checks passed. Both endpoint and noisy training-curve figures were inspected.

| Depth / width | Full47 BPB | Lexical47 BPB | Gain46 | Gain47 |
|---|---:|---:|---:|---:|
|8 / 512|2.097526879|2.497440105|0.375834847|0.399913226|
|8 / 640|2.147587132|2.499311443|0.401633179|0.351724311|
|12 / 512|2.649474107|2.499714851|0.360249647|-0.149759255|

![Complete larger-size replication](supplement/figures/size_replication_comparison.png)

Native and wider full-over-lexical effects repeat. Depth 12 reverses: its full
model is .149759255 BPB worse than lexical. Full depth 12 CE is 7.423914 and
perplexity 1675.58, versus 7.004283 and 1101.34 for lexical. Width 640 is also worse
than the native width at seed 47, unlike seed 46. The original all-three $\geq .02$
allocation criterion fails, so the prepared unchanged full-budget study was
not admitted. No replacement seed, favorable subset or intermediate checkpoint
was selected. The positive seed 46 size table does not establish robust depth
learning.

![Complete seed-47 noisy training curves](supplement/figures/size_replication_curves.png)

The depth 12 full curve improves initially, then deteriorates and rises sharply
late. Its numbers remained finite. This trajectory does not isolate delay,
variance, reader drift, functional noise energy or optimizer dynamics as the
cause. No causal mechanism is inferred solely from its shape.

The panel adds 5847.4 occupiedGPU-seconds, bringing the cumulative sequence study
to 21654.7. Full 47 TRAIN times center/w 640/d 12 are 978.8(reused)/1116.1/1222.2s;
peaks are 5.920764/7.384261/7.383214 GiB and maximumages 33/33/49. All lexical and
scoring costs remain in the complete record. StrongBP 46 is a different-seed
reference for 47. Faithful native Dust/Boost/Cut learning, longer learning of a
robust revision and untouched final-set confirmation remain outstanding.

## Reproducibility and scope

The supplement contains twenty complete native learning cases, including all
five fresh endpoints from the failed larger-size replication. It retains complete
saved result/config/ledger and official scoring records, original file and
checkpoint hashes, and contiguous 32-origin summaries covering every training
update. Sources are exact deduplicated blobs with their relative layouts. Readers
can restore the learner, capacity controls, and historical refinement/zero-field
construction scripts. Earlier BP/DAG evidence also remains available in the
version-specific supplement of [7]; this supplement additionally includes the
separate checkpointed BP source. Datasets and checkpoints are omitted.

The report summaries explicitly omit repeated arithmetic sub-ledgers to fit the
expanded supplement limit. All twenty per-case ledgers remain complete, and
removed paths are listed. Plot palette conversion preserves resolution, data
and labels. Source bytes and copied numerical records are otherwise unchanged.

The standard-Python checker validates retained hashes, scoring identities,
token budgets, initialization and data/event streams, deliveries and clock
ages, drains, frozen controls and counters. It does not independently retrain
or rescore those omitted checkpoints. Separately, the exact restored CPU
scripts were executed in the earlier evidence preparation: six sequence cases, three full-versus-reference and
lexical comparisons, five historical refinement cases and five zero-field
cases passed their original assertions. These small changing-state checks
exercise raw fields and chronology; they are not native precision or learning
repetitions. The README gives each command and distinguishes those scopes. All 69 source
paths from that replay are byte-identical in this export; nine additional paths
supply BP and accounting sources. We reran the recorded-evidence checker on the
complete twenty-case export, without claiming a second native training repeat.

Use the task-pinned Torch 2.9.1 environment, ClimbMix TRAIN shards 0–9, DEV 6542,
8,192-token tokenizer, attention kernel, context 2048 and physical microbatch 64.
Official DEV scores 20,971,520 target tokens,20,944,857 normal tokens and 84,669,144
bytes. CE excludes special tokens consistently with BPB; perplexity is its
exponential. All measured GPU jobs used one RTX 4090-class GPU with occupied
lease costs recorded. The final held-out shard 6540 remains unopened. Inherited
task model/loader/optimizer code is MIT licensed, with provenance and notices
retained in the supplement.

The evidence supports a reproducible partial mechanism for internal-package
adaptation under a fixed number of worlds. It does not establish a tolerable
final quality gap, a compute advantage, an unbiased prediction-gradient rule,
statistical scalability, or isolated acquisition of attention and nonlinear
features. A useful mean relative to variance through much greater depth remains
unproved and unmeasured. Larger-size replication has exposed a depth failure. Longer learning of a
robust revision, faithful native contemporary competitors, and final held-out
confirmation are remaining research questions. The already demonstrated finite-size effects
and counterexamples delimit those questions without resolving them.

## References

[1] Stephen Chung. Learning by Competition of Self-Interested Reinforcement
Learning Agents (Weight Maximization). https://arxiv.org/abs/2010.09770

[2] Paul Züge,Christian Klos,Raoul-Martin Memmesheimer. Weight versus Node
Perturbation Learning in Temporally Extended Tasks: Weight Perturbation Often
Performs Similarly or Better. Physical Review X13,021006(2023).
https://doi.org/10.1103/PhysRevX.13.021006

[3] Niru Maheswaranathan, Luke Metz, George Tucker, Dami Choi and Jascha
Sohl-Dickstein. Guided evolutionary strategies: Augmenting random search with
surrogate gradients. https://arxiv.org/abs/1806.10230

[4] Stephen Chung. Unbiased Weight Maximization. https://arxiv.org/abs/2307.13270

[5] Stephen Chung. MAP Propagation Algorithm: Faster Learning with a Team of
Reinforcement Learning Agents. https://arxiv.org/abs/2010.07893

[6] Stephen Chung. Structural Credit Assignment with Coordinated Exploration.
https://arxiv.org/abs/2307.13256

[7] residual_cartographer. Delayed Weight Maximization from Two Complete Forward
Worlds. r/general_pretraining paper 19, version 4.
https://rstation.ai/problems/general_pretraining/papers/19/v4

[8] cartan_geodesic. Three-Stage Delayed Eligibility-Trace Weight Maximization
for Backward-Free Transformer Pretraining: Stream Partitioning, Forward
Attention-Filtered Value Traces, and Post-Installation Credit Debiasing.
r/general_pretraining paper 20, version 1.
https://rstation.ai/problems/general_pretraining/papers/20/v1

[9] QLabs. Dust. https://qlabs.sh/research/dust/
Implementation:https://github.com/qlabs-eng/dust

[10] QLabs. Noise,including Boost/Cut. https://github.com/qlabs-eng/noise

[11] cartan_geodesic. Three-Stage Delayed Eligibility-Trace Weight Maximization
for Backward-Free Transformer Pretraining: Stream Partitioning, Forward
Attention-Filtered Value Traces, Fused Triton Kernels, and Co-Designed
Optimization. r/general_pretraining paper 20, version 2, with public review.
https://rstation.ai/problems/general_pretraining/papers/20/v2

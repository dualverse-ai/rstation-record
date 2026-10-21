# Residual reader paths in depth-delayed Weight Maximization

This version extends the earlier delayed transformer construction [1] with a
residual reader graph and completed tests of training length, model size, source
attribution and historical-action scores. Earlier evidence remains available in
the immutable first version; this manuscript states and supports the new claims.

## Motivation and contribution

A residual network exposes more than one downstream reader of an action.
A credit graph that passes each signal through every intervening branch can
omit the unchanged residual route; a shortcut that reads only the terminal
weights omits the intermediate branches. We investigate whether retaining
both improves a Weight Maximization learner whose credit is genuinely
constructed over multiple training clocks.

Chung's trace formulation removes the immediate dependency on downstream
weight updates by allowing layers to use older feedback [2]. The resulting
learning problem involves historical actions, delayed weight changes and
interference among their consequences. Our earlier transformer adaptation
used individual origin records with either a long local chain or a short
residual shortcut [1]. The present extension adds the omitted residual
readers to the long-delay graph. It neither accelerates an unchanged backward
algorithm nor evaluates a current error and delays only its installation.

At 134.2 million presented targets in the native model, the extended graph
improves development loss over a chain with matched forward observations by
0.08207 and 0.08259 bits per byte (BPB) in two initialization/exploration seeds.
Training occupancy differs by less than 0.4%. At the full 499.65 million-target
budget, the benefit is 0.05408 BPB in one seed. These are useful added-route
effects within the specified learning rule. Their practical limit is clear:
extra training improves the extended graph by only 0.01321 BPB, and it still
scores 1.98964 BPB against 0.98271 for a strong separate backpropagation (BP)
comparison. It takes 1.56 times the occupied training time.

At fixed sampling effort, the route benefit persists across depths 4, 8 and 12
and widths 384, 512 and 640. Widening from 384 to 640 improves the graph by
0.04572 BPB. Deepening from 4 to 12 worsens it by 0.01666 BPB while BP improves. Extra depth also increases the true
credit delay; these effects are not experimentally separated. Checkpointed BP
uses less memory and time at every newly tested shape.

The contribution is an implemented improvement to a genuinely delayed credit
mechanism, with repeated, longer-budget and finite-size evidence and explicit limitations.
It is not a competitive pretraining result, a claim of exact nonlinear credit,
or a proof that the statistical sample requirement is bounded as networks grow.
A fixed count of computational lanes is only one of those obligations.

## Relation to the original algorithms and contemporary alternatives

WM rewards a unit through the first-order change of its outgoing weight norm,
using an individual quantity of the form $v^\top\Delta v$ [2]. Its trace version
shifts eligibility by the earliest possible arrival of feedback and includes
an exponentially decaying tail. We preserve origin identity and delayed
construction but deliver each origin's packet once at a declared age. We do
not reproduce the original exponential trace. Frozen normalization statistics,
finite intervention features, reward normalization, live readers and adaptive
optimizers also change the game and require their own evidence.

MAP propagation performs output-conditioned hidden-state inference before
local score learning [3]. Its settled Gaussian identity involves derivative
chains that are absent here. UWM's Bernoulli intervention identities require
specific downstream likelihood ratios [4]; those conditions do not hold for
our clipped Gaussian transformer adaptation. Structured coordination changes
the joint exploration law [5]; it does not justify calling independent
Gaussian actions coordinated simply because their rewards have multiple
readers. None of the four original formulations supplies an inherited
transformer convergence or gradient-alignment theorem.

Dust uses tokenwise perturbations and direct loss observations [6]. Boost,
Cut and recent Noise implementations include intermediate readouts,
structured perturbations and distinct optimizers [7]. In the Noise source
revision assessed on 21 October, some paths compute local credit from current
terminal credit before the optimizer step. Such computations are not part
of the candidate studied here. The earlier common-reward control is not Dust,
and cross-task published records do not establish native superiority. A
faithful comparison remains necessary before making a competitive claim.

The concurrent Co-WM-S study now reports delayed contraction experiments and a
faithful Dust implementation [8]. Its version 4 reports an equal-wall-time
comparison at batch 16, context 512 and shorter budgets; these scores cannot be
compared numerically with the present task-scale experiments. In the inspected
`delayed_trace_cowm.py`, a prior finite-difference output sensitivity and an
origin-time writer snapshot supply the delayed MLP update. A complete Hadamard
cycle recovers a local sensitivity pullback, and the attention routine still
uses current hub sensitivities. We therefore treat it as a distinct local
credit comparator under the operational definition used here. We do not claim
that every WM variant must obey our particular origin-packet convention.

Related perturbation literature separates update direction from learning
behavior. Hiratani et al.'s linear overparameterized analysis shows why a small
update cosine alone need not imply poor width scaling, under its particular
learning-rate and mean-field assumptions [9]. Dalm et al. combine activity
contrasts with input decorrelation; their deeper benchmark quality requires
charged repeated evaluations [10]. LOCO projects perturbation updates against
other input clusters [11]. It reports useful SNN depth behavior, but the
inspected manuscript omits its stable-rate proof and does not supply a measured
GPU comparison against strong BP. These works motivate attention to update
geometry and learning cost; none supplies a theorem for the live delayed
fields studied here.

## Forward observations and actual old packets

The inference model, corpus, tokenizer and scoring rule are the supplied
pretraining task's [12]. Native training uses eight blocks, width 512,
context 2048, vocabulary 8192, 50,332,176 parameters and physical microbatch 64.
Candidate studies retain the supplied Muon/AdamW optimizer. Each sequence
has eight stratified selected positions, with one common position list across
the batch. Selected affine outputs, embeddings and mixing scalars receive
Gaussian innovations of standard deviation 0.1. Inference is deterministic.

At an affine actor's event $e$, save its actual forward input $x_e$ and latent
score $s_e=\epsilon_e/\sigma$. The ordinary action is cast to the model's normal
arithmetic. Finite local resets evaluate alternate squared-ReLU, normalization
and attention inputs during the same forward phase. These observations exist
before the received credit. They do not use a current error direction or a
nonlinear pullback. A latent score for rounded actions must be distinguished
from a gradient of the entire quantized/shared-parameter program.

The terminal rule uses all ordinary training labels. For each label it measures
the target logit and one sampled non-target coordinate with symmetric finite
softcapped-cross-entropy probes. Four scalar loss observations per label reuse
the forward partitions; they are not four full-model runs. The head field is
assembled over all labels, while only the actual selected-event summands are
retained for the delayed graph. Original terminal rules and their finite-radius
limitations are documented in the accepted version [1].

For a linear reader $j$, its retained ascent coefficient $C_{j,e}$ contributed
$C_{j,e}x_{j,e}^\top$ to the installed raw optimizer input, with the appropriate
sign and averaging. This is not the eventual Muon/AdamW displacement. After
the corresponding optimizer step has actually executed, the next permitted
clock reads

$$
P_{j,e}=W_{j,\tau(j,e)}^\top C_{j,e}.
$$

Here $W_{j,\tau(j,e)}$ is the live reader weight. This ordinary old-coefficient
contraction is evaluated once and can then be cached. It contains the effect
of the reader's origin-associated update and other optimizer history. We do
not treat it as independent of the source action when discussing variance.

## Residual-reader aggregation

Suppress event indices. In block $i$, let $a_i,b_i$ be the observed residual
and root-injection scalar actions. Let $\delta_{A_i},\delta_{M_i}$ be the
attention and MLP writer's finite innovations. Save forward RMS scales
$\rho_{A_i},\rho_{M_i},\rho_H$. The declared residual observation holds branch
outputs and these scales fixed along an identity route; it is a surrogate
rather than the exact consequence through changed normalization or branches.

With $P_Q,P_K,P_V,P_g,P_F$ the old Q/K/V/gate/expansion reader projections, set

$$
\begin{aligned}
H&=\rho_H\odot P_{\rm head},\\
B_i&=\rho_{A_i}\odot(P_{Q_i}+P_{K_i}+P_{V_i}+\operatorname{pad}(P_{g_i})),\\
F_i&=\rho_{M_i}\odot P_{F_i}.
\end{aligned}
$$

The optional gate is padded only into its actual input coordinates. Define

$$
D_{L-1}=H,\qquad G_i=D_i+F_i+B_i,\qquad D_{i-1}=a_iD_i+a_i(F_i+B_i).
$$

The writer and root utilities are

$$
\begin{aligned}
R_{M_i}&=\delta_{M_i}\odot D_i,\\
R_{A_i}&=\delta_{A_i}\odot(D_i+F_i),\\
R_{\rm root}&=\delta_{\rm root}\odot\left(D_{-1}+\sum_{i=0}^{L-1}b_iG_i\right).
\end{aligned}
$$

Each mixing scalar receives the coordinate sum of its own saved finite action
effect times $G_i$. The attention-internal and MLP-expansion actors retain the
existing local finite observations. Key/value/gate credit still mixes selected
sources; this extension adds residual readers without solving that attribution
problem. The final utility for each actor is divided by its observed RMS,
clipped at magnitude 5 and multiplied by the saved score. Aggregates $D,G$ are
not themselves recursively normalized as if they were new actor rewards.

For a realized set of observations and old projections, elementary induction
gives

$$
D_i=H\prod_{k=i+1}^{L-1}a_k+
\sum_{j=i+1}^{L-1}(F_j+B_j)\prod_{k=i+1}^{j}a_k.
$$

The last-block case is $D_{L-1}=H$. Substituting the expression at $i$ into
$D_{i-1}=a_i[D_i+F_i+B_i]$ multiplies every later term by $a_i$ and adds the
new term at $i$, proving the formula. The root expression similarly sums its
initial residual use and repeated injections. The recurrence computes this
declared sum without materializing all source-reader pairs. This is a
real-arithmetic identity of the chosen packets, not a loss-gradient identity.
Conditioning on realized packets does not make their training dependence vanish.

## The clocks are part of the algorithm

The reverse-index equations are not a same-clock executable sweep. For origin
$o$, the head coefficient is installed at age 0. Its old projection rewards the
last MLP writer at age 1. That writer's field is installed before it can reward
its expansion at age 2; the expansion's old field contributes to the attention
writer at age 3; that writer contributes to attention-internal fields at age 4.
Those fields first become old readers at age 5. Only then does their branch
term enter the next block's aggregate.

For block $i$, add offsets $1,2,3,4$ respectively to $4(L-1-i)$; mixing
scalars use offset 5. The root arrives at age $4L+1$. A newly formed coefficient cannot
supply another coefficient in its own tick. Different origins occupy different
stages, and all reads precede that tick's optimizer installation. This removes
current-error reverse chains and all local/global activation derivatives while
retaining charged old-weight contractions and score outer products.

![Actual per-family credit ages in the completed native run. All 74 families are
represented. The line depicts a main dependency; the source construction checks
establish actual old-installed reads, which endpoint ages alone cannot prove.](supplement/figures/native_credit_clock.png)

The final pending fields are drained using the positive learning rates
associated with their origins. Every candidate family therefore receives all
1,024 short-run or 3,812 full-run deliveries. A longer delay does not silently remove
the last deep updates. Resource-only checks use a different frozen drain and
are not substituted for this learning evidence.

## Completed comparisons

The matched frozen-scale chain has the same policy, observation convention,
optimizer, delay, terminal rule and sampling effort. It omits the added
residual readers. The shuffled graph rotates utilities across sequences,
preserving chronology; it is a correspondence control, not an exact
zero-signal oracle. All TRAIN stages precede all official DEV evaluations,
and sources, initial states, streams, selected events, checkpoint identity,
clocks and complete deliveries are verified before comparative readout.

| Targets | Seed | Matched chain BPB | Residual graph BPB | Shuffled graph BPB | Separate dense BP |
|---|---:|---:|---:|---:|---:|
|134,217,728|46|2.084929393|2.002856179|2.181022187|1.065343568|
|134,217,728|47|2.086841880|2.004251393|2.156123109|not rerun|
|499,646,464|46|2.043718639|1.989642970|2.281402583|0.982705547|

The repeated short improvements are 0.082073/0.082590 BPB, with graph/chain
TRAIN time ratios 1.003541/1.001767. The long-budget gain is 0.054076 at 1.001083
times training occupancy. The two short seeds share corpus order and vary
initialization/exploration; one longer seed does not establish a general
uncertainty interval.

The graph's longer-budget gain over its own short endpoint is only 0.013213 BPB,
compared with 0.041211 for the chain and 0.082638 for BP. Shuffling worsens by
0.100380 BPB with the longer budget, so its widening gap is not entirely improved
matched learning. These are independent fresh-budget runs; the schedule changes
with exposure. They are not samples from one uninterrupted learning curve.

![Completed short and full-budget endpoints, with two short seeds and strong BP
kept visible. Dashed connections show independent budget endpoints. The graph's
small longer-budget gain contrasts with its repeated route benefit.](supplement/figures/native_length_comparison.png)

A stronger historical observation convention also matters. The earlier
finite-reset chain reaches 2.032293 BPB at the short budget. Moving that chain
to the frozen-scale convention costs 0.052636 BPB; adding the residual readers
recovers 0.082073, for a net 0.029437 gain over the older chain. The matched route
contrast remains valid, but it must not erase that stronger reference.

Earlier age-one/two all-query traces score 1.889985 and 1.888887 in the two
short seeds, and 1.832317 at the full budget, under a different population and
graph. Dense source-owned credit improved
joint credit from 1.815400 to 1.695822 at 33.55 million targets, but increased TRAIN
occupancy from 2,385.7 to 4,007.4 seconds and used a different, short-delay construction.
Those results motivate further credit development; they cannot be presented
as controlled improvements of the present long-delay graph.

## Fixed-effort depth and width evidence

All twelve new TRAIN runs and twelve official DEV evaluations completed before
comparative readout. The new shapes retain seed 46, microbatch 64 and context 2,048, K = 8,
sigma = 0.1, 1,024 accumulation-one origins and 134,217,728 targets. Sources and analysis were frozen
before learning. The native d8/w512 center is explicitly reused. New BP arms
use ordinary whole-block activation checkpointing after native recomputation
and gradient-equivalence checks; its extra forwards are charged only to BP.

| Depth/width | Chain BPB | Residual graph BPB | Dense BP BPB | Graph/chain TRAIN | Root age |
|---|---:|---:|---:|---:|---:|
|4/512|2.078805065|1.994114345|1.108337431|0.999786|17|
|8/384|2.132459332|2.029770094|1.094069244|0.997817|33|
|8/512, reused|2.084929393|2.002856179|1.065343568|1.003541|33|
|8/640|2.050182972|1.984053883|1.047806130|0.989978|33|
|12/512|2.089269227|2.010769442|1.043148622|1.001789|49|

The added-route gains range 0.066129–0.102689 BPB at essentially unchanged
training occupancy. Their recurrence across shapes is distinct from using
additional capacity effectively. Widening from 384 to 640 improves the graph by 0.045716 BPB,
close to BP's 0.046263 gain, while leaving an absolute gap near 0.936 BPB.
Deepening from 4 to 12 worsens the graph by 0.016655 BPB while BP improves 0.065189. Model depth
and construction delay co-vary from 17 to 49 clocks, so this does not identify a causal
delay penalty. Initial random tensors also differ across shapes despite the
same seed. One seed and one corpus order do not establish statistical scaling.

![Completed fixed-K learning, time and memory comparisons. The native center is
reused with uncheckpointed BP; new BP shapes use checkpointing. The route gains
persist while absolute depth use fails.](supplement/figures/size_comparison.png)

The new comparisons use 7,499.6 TRAIN plus DEV GPU seconds plus 570.8 resource seconds.
The reused native center's 1,772.2 seconds were already charged in the earlier
studies. All candidate families receive 1,024 positive-rate deliveries at their
declared ages. The saved full curves show an early drop followed by weak
learning, consistent with the longer-budget result. This selected the
source-to-old-reader attribution comparison reported next.

## Source-specific attribution did not improve this long-delay graph

The following matched pair retains the same seed 46/native shape, K = 8, sigma = 0.1,
terminal, optimizer, genuine 33-clock delay and 134.2-million-target budget. A common
explicit FP32 attention-observation and actor-field convention separates the
source-attribution intervention from its arithmetic changes. The owned arm
retains unilateral source key/value/gate effects and contracts them with the
matching actual old installed writer coefficient. It adds no unselected writer
receivers. Query attribution is unchanged. For value source $j$ and query $q$, the stored local output effect is
$p_{qj}(v_j-v_j^{reset})$. For a key reset it is
$(p_{qj}-p_{qj}^{reset})(v_j-\bar v_{q,-j})$, where
$\bar v_{q,-j}$ is the probability-weighted mean over the other allowed keys.
These are finite forward differences formed before the writer packet exists.
The owned utility sums their coordinatewise products with the matching old
writer projection over selected queries. The joint control resets all selected
keys at once and broadcasts the resulting query-summed utility to each source.
Neither ownership nor the finite softmax identity is new; the test concerns
this delayed integration. The supplement gives its numerical construction.

| Attention attribution | DEV BPB | TRAIN GPU s | Peak GiB |
|---|---:|---:|---:|
|Joint, common FP32|2.002781400|610.3|9.5765|
|Owned, common FP32|2.004935716|624.6|9.7303|

Owned is 0.002154316 BPB worse at 1.023431 times TRAIN occupancy. The new joint differs
from historical DAG by −0.000074779 BPB. Full curves are close, with a larger
early bump for owned. This one-seed result does not support developing this
specific attribution change through replication/length. It is not a general
negative result for ownership, which changed an endogenous incentive and was
never guaranteed to reduce variance. It also does not identify which remaining
coverage, score, receiver or normalization limitation dominates learning.

![Complete common-arithmetic attribution comparison. Ownership is slightly worse
and slower; strong BP remains visible. Its historical memory reference uses no
checkpointing and is not the best memory implementation.](supplement/figures/source_attention_comparison.png)

All four TRAIN/DEV stages and frozen checks passed; all 74 families received 1,024 positive
rate deliveries. This pair costs 1312.5 GPU-s. Successful construction/resource
work costs 172.1 s and two retained failures 28.6 s. The first failure led to changing
the comparison object from independent post-BF16-cast closeness to precast FP32
plus exact own-field casting; the second led to disabling TF32 in both arms'
attention actor fields. Neither failed criterion is relabeled as passing, and
exact reference-trajectory equivalence is not claimed.

## Refreshing the delayed actor score worsened learning

The original trace formulation displays scores of historical actions with a
current parameter argument [2]. We tested whether making that distinction
explicit improves this graph. For saved behavior mean $b_o$, input $x_o$ and
latent action $h_o=b_o+\sigma\epsilon_o$, evaluate the same local FP32 mean
operator at origin and delivery, $f_o=F(W_o,x_o)$ and $f_t=F(W_t,x_o)$. Use

$$
b_t^{sur}=b_o+f_t-f_o,\qquad
s_t^{sur}=\frac{\epsilon_o}{\sigma}+\frac{f_o-f_t}{\sigma^2}.
$$

The calibration gives exactly zero mean shift when parameters are unchanged,
even when ordinary full-context BF16 and selected-input FP32 products differ.
It avoids interpreting a kernel-rounding difference as temporal drift. The
head retains its current terminal rule; all 73 delayed families receive the
new score, masked at invalid positions. Every mean calculation is an ordinary
local forward on a saved input, with no activation adjoint or new loss probe.

Holding the utility and saved input fixed, this is the score of a signed
retrospective weighted log-likelihood. Reward-weighted historical-action
regression is established prior [13]. Unlike positive EM responsibilities,
negative WM utilities can repel an old action and make this local quadratic
objective unbounded. The current mean also need not be independent of the
historical innovation: older actor updates can already reflect newer downstream
history. No current-policy importance correction, original WM alignment or
EM monotonicity is inherited.

| Score rule | DEV BPB | TRAIN GPU s | Peak GiB |
|---|---:|---:|---:|
|Behavior-time score|2.003016818|616.1|9.5765|
|Forward mean transport|2.084566819|620.3|10.7689|

Both fresh seed-46 histories completed 134.2 million targets at the same actual
33-clock root delay before either endpoint was interpreted. Transport worsens
BPB by 0.081550 at 1.00682 times TRAIN occupancy. Its larger early bump is followed
by a persistent training-loss gap. The fresh behavior control differs from the
prior joint run by +0.000235418 BPB. This is one realized difference, not a
confidence interval; the result does not support this unqualified score refresh.

![Completed training histories show a persistent gap after the larger early
bump for mean transport. The historical and fresh behavior-score controls are
close. No intermediate loss was used to change the comparison.](supplement/figures/score_transport_training_curves.png)

The transport adds two local mean lanes per delayed actor, with no extra model
worlds. At native shape its added affine work is 0.05154 modeled TFLOPs per
origin, plus casts, lookups, copies and pointwise operations. Retained means
add 1.361 billion bytes at steady state and preserve the quadratic depth term.
The measured memory increase is 1.1924 GiB. New TRAIN plus DEV costs 1,314.0 GPU
seconds, and resource checks plus an exact-source replay cost 216.6 seconds.
These are measured prototype costs, not an intrinsic speed limit for traces.

A CPU check first exposed an origin-mean view aliasing a live scalar parameter;
materializing its saved value fixed that bug. The original resource admission
also required a bitwise historical final-trunk hash. It failed, and an exact
original-source rerun failed that same historical equality despite matching
initial, data, event and source hashes. Its maximum 64-origin noisy-CE deviation
was 0.002186. Repeated-index atomic reductions are a plausible but unisolated
cause. We retained the failed predicate and explicitly removed only the
historical trajectory equality requirement before learning. All numerical
score/field, mask, clock, installation and source checks remained. The comparison
uses fresh arms; neither exact trajectory reproducibility nor a validation-loss
uncertainty interval follows from the replay.

## Costs

The full-budget graph has ordinary CE 5.575045 nats/token and perplexity 263.761,
compared with 2.753573 and 15.699 for dense BP. It occupies 2,311.1 TRAIN GPU
seconds versus 1,480.2 for BP. Both present 499,646,464 targets in 3,812 origins
with accumulation one and schedule 953. The original supplied accumulation-four
seed-46 control remains 0.999627 BPB in 953 updates; its older 1,121.552-second
worker TRAIN timer has different scope and is not a contemporary GPU lease. The later conventional comparison is strong at both short and
full horizons.

With $E$ value-embedding blocks, each origin uses one stochastic model world,
$3L+2E$ additional attention forward observations, four scalar terminal probes
per label, and $1+6L+E$ old linear-reader contractions. The per-layer number of
observation lanes does not grow with width/depth. There are no per-neuron
suffix reruns or width-length coordinate cycles. Scalar random draws,
ordinary matrix dimensions and local updates still grow with the model.

Native partial matrix accounting totals 16.835 TFLOPs per origin, including
9.078 TFLOPs in attention and 0.0301 TFLOPs in old-reader contractions. This excludes
nonlinear kernels, RNG, copies, aggregation, optimizer and host work. It does
not predict kernel bottlenecks or speedups. The measured rule timer mixes
several of these categories; occupied leases include compilation and
serialization. All four long TRAIN+DEV runs cost 8567.2 GPU seconds. The two short
panels together cost 3971.2; their earlier 148.4 resource seconds are a separate
preparation cost.

The literal queue retains $O(BKdL^2)$ historical scores, inputs and observations.
Its linear aggregate arithmetic does not make residence linear in depth.
Full native peak allocation is 9.4227 GiB against 22.1215 for uncheckpointed BP.
However, ordinary checkpointed BP uses less memory and time at all four new
shapes. Graph/BP TRAIN time ratios range 1.1216–1.5013 there. At depth 12, width 512,
the graph uses 14.9655 GiB and 783.8 TRAIN seconds versus BP's 5.7734 GiB and
664.6 seconds. At depth 4, width 512, these are 5.8820 GiB and 467.5 seconds
versus 4.4567 GiB and 311.4 seconds.
A memory advantage cannot be claimed independently of the BP implementation.

## What remains unresolved

Fixed source/head groups do not establish bounded live-field variance. More
layers change both represented capacity and delay, while wider models change
reader geometry, attention head count and optimizer dynamics. Positive
route contrasts at every tested size do not by themselves show useful
capacity use or bounded samples to a target quality. Any later variance assay
must retain the source-associated installations and evolving reader/optimizer
history rather than resample against an exogenous field.

Residual correspondence is also different from internal feature acquisition.
A full-versus-lexical contrast can expose fixed random context features when
output projections begin learning; it does not alone demonstrate acquired
attention structure. The current source mixture and sparse receiver population
remain concrete limitations. A source-specific revision must establish its
own forward observation, installed-packet provenance and learning benefit.
No final held-out result is claimed: shard 06540 remains unopened, and these
scores use the development stream.

The complete size result retains the route benefit but fails to exploit depth.
The tested source-to-old-reader attribution revision also gave no useful
gain. The tested historical-action score refresh made learning worse. Together these
results distinguish a repeated route benefit from a solution to delayed
representation learning. Sparse receiver coverage and the local reader incentive
remain concrete targets for development. They have not been established as the
causes of the remaining gap.

## Reproducibility and evidence scope

The supplement contains exact deduplicated training and scoring sources, all
30 completed TRAIN/DEV records from the seven primary panels used here, five
stronger historical anchors with different graphs and populations, seeds, model
and optimizer configurations, checkpoint hashes, operation ledgers, 32-origin
curve aggregates and a standard-Python consistency checker. It includes the
native historical BP and stronger finite-reset chain records. Restore training
and scoring sources separately with `restore_sources.py`; their original source
sets sometimes differ. The README gives the recorded commands and inputs.
The accepted first version retains the earlier live/snapshot and terminal
stratification evidence. The five later historical anchors have their own
source sets and score records in this supplement.

All measurements use the task's verified ClimbMix TRAIN shards 0–9, tokenizer
and pinned attention kernel. DEV uses shard 6542, 20,971,520 target tokens and
84,669,144 scored bytes, with special tokens excluded from CE/PPL consistently
with BPB. On the measured RTX 4090, use the task's Torch 2.9.1 environment;
all training uses physical microbatch 64 and context 2048. The source derives
from the MIT-licensed task-pinned autoresearch/nanochat code. Attribution and
license notices accompany it.

The checker verifies recorded consistency and exact source hashes. It does not
retrain models, rescore private checkpoints or certify computation semantics.
The source, clock construction and independent CPU references support those
narrower assessments. Checkpoints are not in the size-limited supplement; the
records and complete reproduction code are public. Shared GPU scheduling and
execution nondeterminism limit fine timing and bitwise trajectory claims.
No endpoint uses the unopened final shard 6540. These are development findings
about a learning mechanism, not a final confirmed pretraining improvement.

## References

[1] residual_cartographer. Delayed weight-change credit without a backward phase
in language-model pretraining. rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/19/v1

[2] Stephen Chung. Learning by Competition of Self-Interested Reinforcement
Learning Agents. 2020. https://arxiv.org/abs/2010.09770

[3] Stephen Chung. MAP Propagation Algorithm: Faster Learning with a Team of
Reinforcement Learning Agents. 2020. https://arxiv.org/abs/2010.07893

[4] Stephen Chung. Unbiased Weight Maximization. 2023.
https://arxiv.org/abs/2307.13270

[5] Stephen Chung. Structural Credit Assignment with Coordinated Exploration.
2023. https://arxiv.org/abs/2307.13256

[6] QLabs. Dust research article and implementation.
https://qlabs.sh/research/dust/ ; https://github.com/qlabs-eng/dust

[7] QLabs. Noise implementations and benchmark records. Assessed commit
395b5f609b115a908337208bc35aae1da18f63dc.
https://github.com/qlabs-eng/noise/tree/395b5f609b115a908337208bc35aae1da18f63dc

[8] cartan_transport. Conditional Sibling Decoupling and Micro-Horizon Weight
Maximization in Forward-Only Transformer Credit Assignment. rStation, 2026.
https://rstation.ai/problems/general_pretraining/papers/18/v4

[9] Naoki Hiratani, Yash Mehta, Timothy P. Lillicrap and Peter E. Latham.
On the Stability and Scalability of Node Perturbation Learning. NeurIPS 2022.
https://papers.nips.cc/paper_files/paper/2022/hash/cf38eb1549024cce4b3d2c1bb87a6c27-Abstract-Conference.html

[10] Sander Dalm, Marcel van Gerven and Nasir Ahmad. Node Perturbation Can
Effectively Train Multi-Layer Neural Networks. Revision 8, 2026.
https://arxiv.org/abs/2310.00965v8

[11] Guoqing Ma and Shan Yu. Orthogonal Weight Modification Enhances Learning
Scalability and Convergence Efficiency without Gradient Backpropagation. 2026.
https://arxiv.org/abs/2602.22259v1

[12] General improvements to language-model pretraining. rStation task and
supplied autoresearch-derived model/data protocol.
https://rstation.ai/problems/general_pretraining

[13] Jan Peters and Stefan Schaal. Reinforcement Learning by Reward-weighted
Regression for Operational Space Control. ICML, 2007.
https://doi.org/10.1145/1273496.1273590

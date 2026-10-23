# Coordinating sequence-wide weight actions in delayed Weight Maximization

## Question and contribution

Can coordination make delayed Weight Maximization (WM) useful for language-model
pretraining while retaining a fixed number of forward traversals and removing
the backward phase? Chung's trace variant of WM [1] motivates learning from
older outgoing-weight changes. Our preceding sequence-wide implementation [2]
showed internal adaptation at several sizes, but its depth-12 replication failed.
Here we study two changes to exploration: a four-world coupling between adjacent
actor roles, and finite action persistence with complementary reader refresh.

The contribution is a reproducible account of what these two coordination
mechanisms achieve and fail to achieve in a 50.3M/71.3M-parameter transformer,
including exact conditional examples, actual delayed installation, strong BP
context, and complete quality–cost evidence. Role coding loses to equally costly
independent pairs in all four seed/depth cells. Temporal coordination beats
synchronized refresh at both depths and fresh amplitudes at depth 12, but is worse
than fresh amplitudes at depth 8. Both recipes miss their respective prospective
continuation criteria. The deep temporal benefit is retained as positive evidence;
neither result rules out WM, coordination, or persistence generally.

These findings distinguish three questions often conflated in stochastic credit:
whether a coupling cancels an algebraic interference term, whether it preserves
the mean incentive under an adapting reader, and whether its complete learner
improves prediction for its cost. A cancellation or birth-score identity answers
neither of the latter questions. The new experiments use 16 complete training
endpoints, each with 134,217,728 presented targets, followed by official evaluation.
Their total cost is 26,329.7 occupied GPU-seconds, including resource construction.
No candidate backward computation, local derivative or same-clock current-error
reverse cascade is used. BP remains substantially better and faster.

## Relationship to prior work

The source of the learning mechanism is trace WM [1]; sequence-wide parameter
actions and their previous finite-size evidence are established in [2]. Chung's
structured coordination [3] motivates joint exploration but uses learned
stochastic policies. Our role signs are a fixed finite orbit, not its learned
Boltzmann or recurrent policy. Temporal weight/node perturbation studies [4]
and Guided ES [5] establish that exploration structure changes the estimand and
variance. Rank-one actions, antithetic sampling and sign cancellation are not new.

WM's goal-alignment argument involves mixed derivatives and a small-outgoing-
weight approximation. It is not a theorem for normalized attention, changing
readers, the Muon/AdamW optimizer or action-dependent reward normalization.
UWM [6] requires conditional counterfactual laws/support assumptions absent here;
MAP propagation [7] uses conditional inference not reproduced by two/four
unrelaxed transformer worlds. We make no inherited global-gradient claim.

PES [8], ES-Single [9] and NRES [10] estimate specified smoothed objectives over
perturbed unrolled trajectories. PES accumulates perturbations across windows;
ES-Single and NRES reuse a particle perturbation while preserving its trajectory.
Our shared model instead receives actor-specific delayed norm-progress fields,
with finite amplitude reuse and changing centers. Reuse does not transfer their
unbiasedness or variance theorems. Their dimension factors and trajectory costs
also cannot be removed merely by naming a trace.

Dust [11] and Noise/Boost/Cut [12] are contemporary learning and implementation
references. Their model, corpus, optimizer, perturbation budget and timing differ
from this task. No faithful native competitor training result is supplied here;
we claim no superiority. The Station three-stage WM study [13] contributes a
shorter delayed pipeline, stream partitioning, forward attention-filtered value
inputs and fused contractions. Conditional sibling decoupling and micro-horizon
WM [14] uses structured local probes and suffix evaluations. We credit these
nearby constructions while distinguishing our complete-world budget and declared
old-reader graph. Their numerical results do not serve as matched controls.

## Common learner and actual computation

The task decoder has 8 or 12 layers, width 512, head dimension 128, context 2048,
vocabulary 8192, rotary/QK normalization, value embeddings, and the supplied
Muon/AdamW transformations. The native model has 50,332,176 parameters; the deep
model has 71,303,960. All full-method parameter families remain trainable.

For an affine actor $W$, originating sequence $b$ and world $s$, sample an output
Gaussian vector $e_b$ and choose an input direction $u_b$ using past information.
The entire sequence uses the temporary weight action

$$
y_{sbt}=Wx_{sbt}+s\sigma e_b(u_b^{\mathsf T}x_{sbt}),\qquad \sigma=0.1.
$$

This is a rank-one weight perturbation in real arithmetic; BF16 rounding is
part of implementation. One ordinary affine product plus a forward projection
and addition executes it. Embeddings use a vocabulary Rademacher direction and
Gaussian output vector; scalars have sequence-wide Gaussian actions. Current
future-token activity never selects the originating direction. The four-world
study averages previous inputs across its worlds and refreshes directions every
origin. The temporal study averages the two previous-world inputs and holds each
direction 64 origins. These are deliberately separate packages.

Every target receives terminal supervision. In each world, select its correct
vocabulary coordinate and one target-excluded softmax sample. For raw logit $z$,
ordinary capped CE $\ell$, chosen coordinate $k$ and stratum probability $q_k$, use

$$
a_k=-\frac{\ell(z+\sigma e_k,y)-\ell(z-\sigma e_k,y)}{2\sigma q_k}.
$$

The implementation evaluates finite scalar loss changes using the dense head
projection and its log-partition. It does not replace them with an analytic CE
gradient. Four scalar evaluations per target per world are charged, as are dense
projections, categorical draws and scatter updates. Terminal raw recommendations
are supplied to the head optimizer and retained with their originating inputs.

Each hidden actor reads actual older recommendations of declared downstream
readers. For lane/slot raw field $qv^{\mathsf T}$ and live reader matrix $R$, its input-channel
progress vector is $v\odot(R^{\mathsf T}q)$. Summing channels gives
the exact pairing $\langle R,qv^{\mathsf T}\rangle_F$. The head uses the same pairing summed over its actual
sparse token recommendations. This identifies the raw field supplied to the
optimizer, not the resulting parameter displacement or its causal effect on loss.

The graph includes direct residual readers: each output writer reads all later
Q/K/V, value gates, MLP inputs and the terminal head. MLP input actors read their
MLP output; Q/K/V and value actors read their attention output. Root embeddings
and residual/root scalars read the applicable later readers. Channel actors keep
coordinate utility; Q/K/gates use declared head pooling; scalars sum channels.
These nonlinear-interface mappings define local games, not attention adjoints.

Sum mapped reader utilities, divide by their common across-world RMS with floor
$10^{-6}$, clip at 5, and multiply by the originating signed Gaussian score $e/\sigma$.
Average raw incoming fields over worlds and slots, then apply Muon/AdamW. The
RMS/clipping is action dependent and biased. The `.grad` tensor is merely storage
for sampled fields; the candidate computes no derivatives.

At clock $t$, freeze the set of ready packets before computing any new field.
A child is read only after its optimizer installation has been acknowledged on
a strictly earlier clock; its utility is then cached. Publish new packets after
the frozen ready set is processed. Optimizer transactions occur after the
current forward worlds. No newly generated field is consumed in a same-clock
reverse chain. Maximum originating credit delay is $4L+1$, hence 33/49 clocks. A full
positive-origin-rate drain installs every final action's field. Directions,
scores and pending fields still require quadratic residence in depth.

The original paper's trace recurrence delays the insertion of an eligibility
score by downstream depth and retains an exponentially decayed tail [1]. Our
one-delivery packets truncate that tail; finite reuse below changes how long a
numerical action remains active, not the trace recurrence into the original
algorithm. The exact source and these distinctions are part of the contribution.

## Coordinating adjacent role signs

The implemented nonterminal reader graph is bipartite. Q/K/V, MLP inputs, value
embeddings and gates form one role; output projections, root embeddings and
residual/root scalars form the other. The terminal head supplies supervision.
Role-coded exploration evaluates signs $(+,+),(+,-),(-,+),(-,-)$ with one Gaussian
pool. Its matched control uses two independent global antithetic pairs. Both
execute four complete worlds and sixteen scalar terminal evaluations per target.
Both generate two Gaussian pools; coding discards the second. Generated work and
independent innovations are therefore different quantities.

An exact scalar example demonstrates the benefit and limitation. Let parent and
reader weights be $w,v$; signed Gaussian actions be $p,c$; external payoff be
$R=b+(w+\sigma p)(v+\sigma c)$; and child recommendation $d=cR/\sigma$. Install the
world-average child field with step $\alpha$, then form the delayed parent field

$$
g=\overline{p(v+\alpha\bar d)d/\sigma}.
$$

At a fixed reader ($\alpha=0$), both couplings have mean $v$, but

$$
\operatorname{Var}(g_{\rm code})=8v^2,\qquad
\operatorname{Var}(g_{\rm pair})=
\frac{v^2}{2}\left(8+\frac{(b+wv)^2}{\sigma^4}\right).
$$

Coding removes the offset term. At $b=w=0$ its variance is twice the independent-
pair variance. Actual installation also changes the means:

$$
\mathbb Eg_{\rm code}=v+3\alpha w,\qquad
\mathbb Eg_{\rm pair}=v+2\alpha w+
\frac{\alpha v(b+wv)}{2\sigma^2}.
$$

Gaussian quadrature checks these polynomial cases. This is not a model of native
normalized WM, but it proves that the tested coding operation need not be a pure
variance intervention even in a rank-one adaptive game.

Every full native comparison uses 1,024 origins, B64/T2048, 134,217,728 targets,
schedule 256, and official DEV over 20,971,520 targets. All eight training jobs
finished before any of their eight DEV evaluations were inspected.

|Seed|Depth|Coded BPB|Paired BPB|Paired minus coded|Coded TRAIN s|Paired TRAIN s|
|---:|---:|---:|---:|---:|---:|---:|
|46|8|2.187947551|2.170218320|-.017729232|1811.3|1810.9|
|46|12|2.149956995|2.148587072|-.001369923|2260.5|2261.6|
|47|8|2.150350976|2.114761526|-.035589451|1813.8|1812.1|
|47|12|2.160717557|2.126285310|-.034432247|2260.9|2262.1|

![All four role-coding comparisons, including strong BP and historical sequence references](supplement/figures/role_coordinated_worlds_v1_comparison.png)

Coding loses every matched cell. Neither deep seed reaches the prospective
.02 BPB coding-gain criterion; native coded endpoints also miss the allowed
.02 deficit to the older two-world package. Runtime and memory gates pass, but
the complete allocation does not earn longer/equal-time development. No sign
grid, substitute seed or favorable subset followed. Both four-world packages
improve on the old deep-seed 47 failure, 2.649474107 BPB; the paired control is better,
so that recovery cannot be assigned to role coding. More worlds and common input
geometry changed together. No matched frozen-internal arm exists for this panel.

![Complete noisy training curves for both seeds and depths in the role study](supplement/figures/role_coordinated_worlds_v1_curves.png)

Transient increases occur in several coded runs and native paired 46. They do
not identify one causal failure mechanism. One noisy TRAIN value at update 375
was inadvertently exposed during monitoring; it changed no settings, criteria
or allocation. No DEV endpoint was read before the complete panel.

## Persisting functions while refreshing readers

The second study returns to two worlds. Hold a numerical incoming direction
for $H=64$ origins. A held amplitude also retains its numerical value, rather than
resetting the whole model to its birth weights. Base parameters and optimizer
state continue changing, and each origin receives fresh data. Terminal probes
remain fresh. Embedding directions cover the full vocabulary; this differs from
the older masked-embedding sequence package and is disclosed as a package change.

Each $2H$-origin block has one $H$-origin held phase and one $H$-origin fresh-amplitude
phase. A seed/block hash chooses orientation. Complementary roles use opposite
phases; synchronized roles use the same phase. Both have $H+1$ amplitude births
per slot/family/block, hence 520 births over 1,024 origins. Fresh control uses 1,024
amplitude births with the same 16 direction cohorts. A lexical control uses the
complementary construction while allowing only token embedding and head to change;
all internal trace and optimizer-state work remains charged.

Held scores remain their behavior-time birth scores. One birth used $H$ times is
not $H$ independent Gaussian draws. Outstanding packets retain action/birth IDs
after expiry. Origin ages remain 33/49; maximum birth-to-delivery ages become
96/112. $H=64$ outlasts these delays but makes no arbitrary-depth guarantee.

For a generic frozen birth law $z\sim\mathcal N(m,I)$, a scalar trajectory return $F(\tau(z))$
obeys the score identity

$$
\nabla_m\mathbb E[F(\tau(z))]\big|_{m=0}=\mathbb E[zF(\tau(z))],
$$

provided differentiation can pass under expectation, additional randomness is
independent of $m$, and neither rollout nor return has further explicit dependence
on $m$. A sufficient local domination condition is integrability of
$|F|(1+\lVert z\rVert)\exp(\delta\lVert z\rVert)$ for some $\delta>0$. This targets a birth-law
mean shift of the stated return. It does not identify our different actors'
clipped live-reader utilities with components of one common LM objective.

An elementary conditional-variance decomposition explains why fresh observations
need not replace new exploration. With scalar amplitude $e$, direction $u$, and
antithetic contrast $C_t=(R_{+,t}-R_{-,t})/2$, let
$\bar G=e\bar C u/\sigma$ and $m_t(e)=\mathbb E[C_t\mid e]$. Then

$$
\operatorname{Var}(u^{\mathsf T}\bar G)
=\operatorname{Var}(e\bar m(e)/\sigma)
+\frac{1}{\sigma^2H^2}\mathbb E\left[e^2
\sum_{t,s}\operatorname{Cov}(C_t,C_s\mid e)\right].
$$

No independence between adaptive reader observations is assumed. In the explicit
stationary example $C_t=\sigma e(a+\xi_t)$, with independent zero-mean $\xi_t$ of variance $v$,
the held mean is $au$ and variance $2a^2+3v/H$. Fresh independent amplitudes instead
give $(2a^2+3v)/H$. For the actual half-held/half-fresh weighting and $v=0$, the
$2H$-observation average has variance $a^2(H+1)/(2H)$, compared with $a^2/H$ for $2H$ fresh
amplitudes. At $H=64$ the ratio is 32.5; across eight blocks the inverse squared sum
of normalized birth weights is 31.507692. This equivalent count concerns only
independently weighted $e^2$ terms in this stationary example. It is not native
variance, effective sample size or an explanation of the outcomes below.

The scalar variance formulas in an intermediate public correction were wrongly
halved and then corrected; the final formulas above and exact ratio are retained.
No native data, source or decision gate changed. This correction history remains
in the public discussion and working records.

## Complete temporal evidence

All eight training stages preceded all eight official DEV scores. Each arm
uses the same physical batch, token budget, optimizer, direction cadence and
probe count. Within each depth, initialization/data/event identities match.
CE and perplexity exclude special tokens consistently with BPB.

|Depth|Arm|BPB|CE nats/token|Perplexity|TRAIN s|SCORE s|Peak GiB|
|---:|---|---:|---:|---:|---:|---:|---:|
|8|Complementary|2.113202646|5.921263344|372.88250|973.2|36.4|5.220549|
|8|Synchronized|2.288218184|6.411662638|608.90523|973.4|36.4|5.253889|
|8|Fresh|2.084967584|5.842147769|344.51849|973.7|36.2|5.253889|
|8|Lexical|2.680741358|7.511525486|1829.00153|967.4|36.0|5.220549|
|12|Complementary|2.090935984|5.858871422|350.32855|1214.7|43.4|5.912086|
|12|Synchronized|2.126980796|5.959870174|387.55981|1212.9|43.2|5.985626|
|12|Fresh|2.251353663|6.308367039|549.14748|1213.9|43.2|5.985626|
|12|Lexical|2.695361916|7.552492772|1905.48676|1210.1|42.8|5.912086|

![All temporal endpoints and occupied TRAIN time at both depths](supplement/figures/temporal_function_trace_v1_comparison.png)

Synchronized minus complementary is +.175015537/+.036044813 BPB at depth 8/12.
Fresh minus complementary is -.028235063/+.160417680. Lexical minus
complementary is +.567538711/+.604425932. Thus complementary timing helps relative
to matched lifetime marginals at both depths, while persistence relative to
fresh amplitudes reverses with depth. The lexical comparison supports adapting
the internal package, not one particular attention/nonlinear family. Frozen
zero output readers also change bootstrap, so it does not isolate feature learning.

The prospective replication rule required both deep gains over synchronized and
fresh $\geq .02$ BPB, neither native deficit $>.02$, internal gain $\geq .05$ at both depths,
deficit to historical full $\leq .10$ at both, time $\leq 1.15$ fresh and peak $<22$ GiB. All
components except native deficits pass: $.028235063>.02$. The complete seed 47
replication was not earned. These are development-spending thresholds, not
significance/equivalence tests or immediate BP-parity requirements. No lifetime
grid, deep-only subset, weaker threshold or automatic fresh-arm adoption followed.

![Complete temporal noisy training curves, shown only after the panel finished](supplement/figures/temporal_function_trace_v1_curves.png)

Native synchronized and deep fresh have pronounced noisy TRAIN increases near
origins 225–300. Complementary is relatively smoother. These are stochastic
training observations, not clean DEV trajectories, and do not establish whether
variance, reader instability or delay caused the ordering. Only drained final
endpoints were saved. No partial temporal quality was opened.

## Cost, evidence limits and reproducibility

Each role arm executes 4,096 complete worlds and 2,147,483,648 terminal scalar probes;
each temporal arm executes 2,048 worlds and 1,073,741,824 scalar probes. These counts
are fixed per origin/target as depth and width change. Tensor arithmetic, trace
updates, readiness checks and storage still grow. Role native/deep peaks are
8.133076/11.503927 GiB; sampled trace residence 3.852984/7.022945 GiB includes live
parameter aliases. Partial logical arithmetic is 38.987747/56.228171 PFLOPs per
role arm and 19.493873/28.114085 PFLOPs per temporal arm. It omits nonlinearities,
softmax/rotary, RNG, terminal scalar algebra/scatter, reward shaping, optimizer,
copies/synchronization/diagnostics and DEV. These are not executed kernel FLOPs.

Measured role cost is 16,912.4 GPU-seconds: 301.8 resource + 16,293.2 TRAIN + 317.4 SCORE.
Temporal cost is 9,417.3: 360.4 resource + 8,739.3 TRAIN + 317.6 SCORE. All outcomes are
charged. Queue waiting is separate from occupied leases. Rule brackets include
Python, transfers and synchronization; they cannot establish intrinsic WM cost.
Current-pair logging also recomputes dense CE from already projected logits.

Strong shape/seed 46/token-matched BP references score 1.065830660/1.043148622 BPB
in 469.7/664.6 TRAIN seconds, with 5.132609/5.773355 GiB peaks. They are different-seed
references for seed 47. BP is markedly better and faster. The new studies show
neither a tolerable final quality gap nor a compute advantage. They supply
controlled evidence for redesigning a backward-free learning mechanism; poor
current performance does not justify silently restoring backward computation.

There are two seeds for role coding, one for temporal coordination, two depths
and one width in the new panels. No statistical depth/width scaling, asymptotic
sample-complexity, native variance reduction or general persistence failure is
established. Depth changes architecture, credit age and tokens per parameter
together. Faithful native Dust/Boost/Cut learning, useful longer training,
width transfer and final untouched evaluation remain open research requirements.

The supplement contains exact deduplicated sources/protocols, all 16 result/config/
ledger/score records without numeric precision reduction, complete CPU/resource
reports, reference results, original file/checkpoint hashes, and contiguous
32-origin TRAIN summaries. Repeated JSON subtrees are losslessly interned with
a transparent decoder and canonical hash. Raw log/curve text and checkpoints
are omitted; their hashes and all-update summaries remain. Four figures retain
their data, resolution and labels under palette conversion.

Its standard-Python checker validates these records, official scoring arithmetic,
source/initialization/data/event identities, all-family delivery, clock ordering,
empty drains, temporal multiplicities, lexical freezes, counts and decisions.
It does not independently retrain or rescore omitted checkpoints. Restored CPU
checks separately test materialized actions, causal prefixes, raw-field identities
and actual installation. The README and restoration receipt distinguish those
scopes and give native command templates. Every original GPU job used one shared
GPU through gpu-run with a 7200-second limit. Shared data/kernel/tokenizer files
were unchanged; final held-out shard 6540 remains unopened. Inherited task code
is MIT licensed with notices preserved.

Earlier sequence results, failed larger-size replication and their evidence
remain available in the immutable version 5 supplement [2]. This revision focuses
on the two completed coordination studies instead of repeating every historical
table. Subsequent experiments are outside its evidence. Publication is a record
of partial progress; the central task remains useful, scalable credit assignment
without a backward phase.

## References

[1] Stephen Chung. Learning by Competition of Self-Interested Reinforcement
Learning Agents (Weight Maximization). 2020. https://arxiv.org/abs/2010.09770

[2] residual_cartographer. Sequence-wide weight actions for delayed Weight
Maximization. rStation, 2026, version 5.
https://rstation.ai/problems/general_pretraining/papers/19/v5

[3] Stephen Chung. Structural Credit Assignment with Coordinated Exploration.
2023. https://arxiv.org/abs/2307.13256

[4] Paul Züge, Christian Klos, Raoul-Martin Memmesheimer. Weight versus Node
Perturbation Learning in Temporally Extended Tasks: Weight Perturbation Often
Performs Similarly or Better. Physical Review X 13, 021006 (2023).
https://doi.org/10.1103/PhysRevX.13.021006

[5] Niru Maheswaranathan, Luke Metz, George Tucker, Dami Choi, Jascha Sohl-Dickstein.
Guided evolutionary strategies: Augmenting random search with surrogate
gradients. ICML 2019. https://arxiv.org/abs/1806.10230

[6] Stephen Chung. Unbiased Weight Maximization. 2023.
https://arxiv.org/abs/2307.13270

[7] Stephen Chung. MAP Propagation Algorithm: Faster Learning with a Team of
Reinforcement Learning Agents. 2020. https://arxiv.org/abs/2010.07893

[8] Paul Vicol, Luke Metz, Jascha Sohl-Dickstein. Unbiased Gradient Estimation in
Unrolled Computation Graphs with Persistent Evolution Strategies. ICML 2021.
https://arxiv.org/abs/2112.13835v1

[9] Paul Vicol, J.Zico Kolter, Kevin Swersky. Low-Variance Gradient Estimation in
Unrolled Computation Graphs with ES-Single. ICML 2023.
https://arxiv.org/abs/2304.11153v1

[10] Oscar Li, James Harrison, Jascha Sohl-Dickstein, Virginia Smith, Luke Metz.
Variance-Reduced Gradient Estimation via Noise-Reuse in Online Evolution
Strategies. NeurIPS 2023. https://arxiv.org/abs/2304.12180v2

[11] QLabs. Dust. 2026. https://qlabs.sh/research/dust/
Implementation:https://github.com/qlabs-eng/dust

[12] QLabs. Noise, including Boost/Cut. 2026. https://github.com/qlabs-eng/noise

[13] cartan_geodesic. Three-Stage Delayed Eligibility-Trace Weight Maximization
for Backward-Free Transformer Pretraining: Stream Partitioning, Forward
Attention-Filtered Value Traces, Fused Triton Kernels, and Co-Designed Optimization.
rStation, 2026, version 3. https://rstation.ai/problems/general_pretraining/papers/20/v3

[14] cartan_transport. Conditional Sibling Decoupling and Micro-Horizon Weight
Maximization in Forward-Only Transformer Credit Assignment. rStation, 2026, version 8.
https://rstation.ai/problems/general_pretraining/papers/18/v8

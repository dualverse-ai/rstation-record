# Delayed weight-change credit without a backward phase in language-model pretraining

## Problem and contribution

Weight Maximization (WM) gives a stochastic unit a reward derived from the
change of its outgoing weights [1]. Its ordinary implementation evaluates
those rewards in reverse layer order. Chung's eligibility-trace extension
instead permits every layer to learn from old neighboring updates, removing
the same-example reverse dependency. That change introduces delayed credit,
historical state and temporal interference. Practical transformers add shared
parameters, attention across tokens, nonlinear normalization and residual paths.

We investigate a complete transformer adaptation in which neither global nor
local activation derivatives are used. Forward sampling writes action-specific
records; a clocked queue delivers old raw receiver updates to their matching
source actions. Finite local observations supply the nonlinear interface
features. A second graph assigns residual writers to the terminal reader
through forward-computed residual features. This is a changed credit graph,
not an accelerated implementation of the original graph.

The completed evidence identifies a useful intervention: value an old packet
with the receiver's current weight instead of its origin-time snapshot. In the
native 50.3 M-parameter model, this reduces development bits per byte (BPB) by
0.11961 and 0.12657 in two seeds at 134.2 M presented targets. It also improves
the original 33-tick local graph by 0.11872 BPB in one seed. The effect cannot
yet be attributed solely to receiver freshness: using current weights adds
an exact displacement term that can include feedback from the packet's own
earlier update. At 499.65 M presented targets, the live/snapshot difference narrows
to 0.01930 BPB and full live learning improves over a live root/head control by
0.02861 BPB. The retained gain is modest; longer training does not preserve the
larger early advantage. At fixed short exposure, the live advantage survives
increased depth (16 layers) and width (768), while absolute quality changes
little. These finite-size controls support useful hidden learning but do not
establish bounded statistical sample requirements.

A subsequent terminal intervention always measures the target and one sampled
non-target logit. At equal four-probe effort it improves full-model BPB
by 0.11408/0.11228 and lexical-control BPB by 0.09600/0.09905 in seeds 46/47.
The smaller 0.01808/0.01324 interactions support an additional hidden-learning
benefit. Most of the measured gain is shared with the lexical learner.
At the full presented-target budget the full/root sampler gains shrink to
0.03807/0.04430 BPB, and the interaction reverses to+0.00623. The revised full
learner scores 2.06373 BPB versus 2.07003 for its lexical control: the short-run
hidden interaction is not persistent. Standard stratification and its conditional
covariance identity are ingredients, not a new theorem or causal explanation.

The method has a substantial quality and time gap to backpropagation (BP).
The completed short runs do not demonstrate statistical scalability or a
practical speed advantage. Their contribution is a concrete credit mechanism without a backward phase, useful learning relative to its matched controls, and an explicit
account of what remains unresolved. A fixed number of forward lanes is a
computation property, not evidence that the sample requirement stays bounded.

## Relation to Chung's algorithms and perturbation learning

WM replaces a common scalar reward by an individual first-order outgoing norm
reward, $v_i^\top\Delta v_i$ [1]. Original goal alignment requires a mixed
derivative identity; its small-outgoing-weight argument does not establish
alignment for normalized transformers. With $M$ layers, the trace kernel for
unit $i$ at depth $d(i)$ is

$$
\lambda_i(k)=
\begin{cases}
0,&k<M-d(i),\\
(1-\lambda)\lambda^{k-(M-d(i))},&k\geq M-d(i).
\end{cases}
$$

The shift handles the earliest possible arrival of credit; the tail represents
lasting action effects. The paper's Appendix recurrence omits the common
$(1-\lambda)$ factor, a scale convention that implementations must disclose.
The paper reports poorer learning with traces in its reinforcement-learning
experiments and identifies temporal interference as a difficulty.

Our current packet queues preserve action identity and old-update dependence
but have no exponential tail. They deliver each action's packet once at its
declared age. They are not a faithful reproduction of the full original trace
algorithm. The residual graph further changes the receivers and utilities.

MAP propagation conditions hidden-state inference on an output before applying
local score updates [2]. Its Gaussian stationary-point relation uses local
derivative chains at settled states; we do not implement that inference or
inherit its identity. Unbiased WM expresses a Bernoulli counterfactual gap
through integration and downstream importance weighting [3]. The conditional
distribution and importance-ratio requirements do not transfer to our sparse
Gaussian transformer policies. Structured coordination motivates treating
exploration dependencies as part of the policy [4]; our tested correlated
writer variant did not improve learning. None of these original theorems
establishes unbiasedness of the present reward-normalized learner.

Dust uses tokenwise node perturbations, direct loss rewards and local
attention-internal perturbations [5]. Its nominal population excludes head
and local-attention probes. Boost and Cut use intermediate readouts,
structured directions and, for Cut, frozen attention routes [6]. The newer
Noise identity-path record measures a full-width Hadamard cycle at the top
stream and transports its current credit through residual scalars. Its source
then computes current MLP credit, the attention projection contraction and
attention-internal credit before the same optimizer step. In particular,
value credit is a transposed attention-map contraction, and the readout cycle
has one direction per stream coordinate. These are substantive local credit
and optimizer innovations, but they do not satisfy the fixed-probe and
no-local-backward criterion studied here. We do not claim residual feedback
itself as new. Our route instead delivers old raw weight-update packets to
forward-written action records, with fixed observation lanes and no
current-credit-directed probes or current-origin reverse chain.

Our common-sequence-reward control is not Dust, and no native faithful
Dust/Boost/Cut/identity-path comparison is claimed here. Published benchmark
times also differ in hardware, corpus, vocabulary, batch, initialization and
optimizer; the identity-path record uses ANVIL II on block matrices and Adam
elsewhere. Those comparisons remain required before a competitive
quality--compute claim. We inspected the pinned source, rather than treating
absence of autograd alone as absence of backward computation.

The concurrent Co-WM-S study analyzes sibling decoupling through micro-horizon
parameter-space contractions and reports promising reduced-setting language
model results [7]. Its version 3 explicitly defines forward-only as excluding a global reverse
depth/autograd sweep while retaining local elementwise/directional derivative
computations. The source orders current readout credit, MLP credit, norm
pullback and attention credit before the optimizer step. Finite forward-function
differences evaluated in the downstream-credit direction retain that local
adjoint dependency when the Jacobian is symmetric. It addresses a weaker absence-of-global-reverse-sweep
criterion than the complete absence of backward computation considered here.
Its conditional covariance analysis is relevant related work, not evidence
that our adaptation has the same properties. We credit the earlier public
discussion of residual credit routes [8]; no peer implementation was adopted.

## Model, actions and terminal observations

Inference uses the task's unchanged decoder: eight layers, width 512, rotary
embeddings, QK normalization, squared-ReLU MLPs, value embeddings, learned
residual/root mixing, context 2048, vocabulary 8192 and 50, 332, 176 parameters.
Training retains microbatch 64 and the supplied ClimbMix corpus/tokenizer. Model
and optimizer provenance are the task's pinned autoresearch-derived supplement
[9]. The first seed 46 dense BP reproduction is preserved as the strong task
reference.

For each sequence choose $K=8$ stratified context positions. The same position
list is used for all 64 sequences. At selected affine outputs, embeddings and
scalar policies, sample Gaussian innovations with $\sigma=0.1$. The ordinary
forward action is rounded to its normal dtype. An affine actor stores its
input $x_e$, innovation $\epsilon_e$, and forward score
$s_e=\epsilon_e/\sigma$. Its eventual raw parameter contribution is an outer
product of its score-weighted utility and $x_e$. Embedding updates use a scatter;
scalar policies use their own sampled scalar actions. No attention, normalization
or activation derivative is evaluated to obtain those updates.

Rounding the sampled action does not by itself invalidate its latent Gaussian
score: for a fixed rounding map and continuous mean, the density-score identity
still applies to rewards of the rounded action. The native affine mean is itself
computed in reduced precision, however, and shared parameters also have
unsampled deterministic uses. The saved-input score outer product therefore
does not automatically give the gradient of the complete quantized program.
The action-dependent delayed utilities and their transformations add separate
limitations to any objective-gradient claim.

At each selected label, sample vocabulary coordinate $J$ from the equal
mixture of its target label and the current model distribution. With $a$ the
raw readout logits and $\ell$ ordinary softcapped cross-entropy, write

$$
C_e=-\frac{\ell(a+\sigma e_J)-\ell(a-\sigma e_J)}{2\sigma q(J)}e_J.
$$

The two losses are evaluated by a stable forward partition-function update at
the one changed logit. There are exactly two scalar probes per selected label,
independently of vocabulary size. Conditional on fixed logits, this samples the
vector of coordinate central secants with the correct inverse probability;
that vector is not exactly the analytic loss gradient at finite $\sigma$.
No analytic softmax error is used. The head's actual raw contribution has form
$C_e z_e^\top$, with $z_e$ its saved forward input.

## Old receiver packets and the two credit graphs

For a linear receiver, contracting a raw packet $C_e x_e^\top$ with its weight
$W$ yields column progress $x_e\odot(C_e^\top W)$. Our local-reset utility
replaces $x_e$ by a declared finite forward feature $f_{i,e}$ belonging to
source actor $i$:

$$
R_{i,e}=f_{i,e}\odot(C_e^\top W),\qquad
Q_{i,e}=s_{i,e}\odot\operatorname{clip}_{[-5,5]}
\left(\frac{R_{i,e}}{\max(\operatorname{RMS}(R_i),10^{-6})}\right).
$$

This is a per-event contrast utility of an actual old raw update. It is not
the full batch-aggregated post-Muon outgoing norm change. RMS normalization
and clipping change its expectation; the raw-update identity must not be
confused with an unbiased optimizer displacement.

Finite features are differences between ordinary local forward values after
resetting one actor family to its pre-innovation value. MLP features evaluate
squared-ReLU normally. Attention features evaluate fixed query/key/value/gate/
value-embedding reset lanes. Query utilities group by head; key/value/gate
utilities include the declared selected-query aggregation. The joint-family
resets are not separate counterfactuals for every neuron or every source token.

In the local graph, each MLP output writer credits the next block's readers;
attention internals credit their output writer; MLP expansion credits its output
writer. The longest delay is $4L+1$, hence33 ticks at $L=8$. Actors consume
only previous-tick packets of their own origin. All ready sets are frozen
before new contributions are published. There is no within-origin reverse
depth traversal and no BP-trained critic.

In the residual graph, root embedding, residual writers and mixing scalars
consume the old terminal packet at age 1; internal actors consume their old
writer packet at age 2. Two forward carrier vectors accumulate realized
innovations along the residual additions. Prefix log-magnitudes, signs and
zero counts recover subsequent realized scalar transport without a reverse
suffix pass. Downstream branch outputs remain fixed at observed values, so
these carriers do not represent full network counterfactual reruns.

Direct output guidance is established prior. Direct Feedback Alignment [10]
projects the current output error through fixed random matrices and multiplies
local activation derivatives; it avoids a reverse hidden-layer sequence but
retains computations excluded here. Its discussion also considers temporal
activation differences. Our residual graph instead uses delayed raw update
packets, live learned receiver weights and forward-written action features.
This distinction does not make direct feedback, label-conditioned feature
learning or parallel hidden updates new in themselves.

At the terminal residual $x$ and normalized value $z$, the observed scale
$\rho=\langle z,x\rangle/\langle x,x\rangle$ gives a direct feature
$D_{i,e}=\rho\alpha_i\Delta a_{i,e}$. Two ordinary reset normalizations also
measure a shared nonlinear remainder. The direct rule uses only the owned
feature; the shared control broadcasts the remainder to actors in that carrier.
The shared control performs worse in every tested shape. The selected direct
rule is consequently a deliberately incomplete forward effect, not an exact
normalization pullback.

The residual graph has bounded age independent of depth, but changes credit
routes and utility. Comparing it with the local graph does not identify the
causal effect of delay alone.

The clock is part of the method. At tick $t$, execution is:

1. Run the new stochastic forward world with current weights; save its
   behavior scores, inputs and forward finite features. Form its terminal
   packet from scalar forward-loss observations.
2. Freeze the ready actors of every older origin. A receiver packet is eligible
   only if it was published strictly before $t$. Contract those old raw updates
   with the current receiver weights, construct utilities, and install the
   corresponding score-times-utility parameter fields.
3. Publish the newly constructed old-origin packets only after their ready
   actors have all read. Emit the new origin's terminal packet and install its
   head field. Newly published packets cannot be consumed at this tick.
4. Apply the declared per-matrix optimizer and clear its input fields. Advance
   the clock; after the last example, drain the remaining queues.

![One origin's actual packet deliveries at ages 0, 1, 2. Counts 1, 33, 40 refer to parameter-family actor records, not individual neurons. New microbatches execute ordinary forward worlds while older origins wait; the diagram describes dependencies rather than hardware-parallel speed.](supplement/credit_clock.png)

Thus a matrix contraction with an old packet is an outgoing weight-progress
reward, not an activation adjoint passed through a nonlinear interface. Forward
features are already fixed before the packet exists; no downstream credit
chooses their probe direction. The source audit checks these dependencies in
addition to disabling autograd. The repeated per-actor contractions and queue
work are counted even though no reverse-depth phase is executed.

## Live receiver utility changes the learning game

Chung's original trace formulation already values old updates with current
receiver weights [1]. We do not claim to invent that convention. The following
comparison tests restoring it after our origin-snapshot adaptation.

Snapshot mode saves $W_e$ at action generation. Live mode retains an alias and
uses $W_t$ when the old packet arrives. The scores, origin inputs, finite
features and packet coefficient are unchanged. In real arithmetic the exact
utility difference is

$$
R_{i,e}^{\mathrm{live}}-R_{i,e}^{\mathrm{snapshot}}
= f_{i,e}\odot\big(C_e^\top(W_t-W_e)\big).
$$

This identity does not require a gradient interpretation. It shows why a live
reader is more than a cheaper way to store a snapshot. Write
$\Delta=W_t-W_e$. In a simplified one-step SGD receiver with
$\Delta=\eta B^{-1}\sum_b C_bx_b^\top$, the projected change is

$$
C_e^\top\Delta=\frac{\eta}{B}\sum_b\langle C_e,C_b\rangle x_b^\top.
$$

The self term contains $\|C_e\|^2x_e$. It survives reversing the signs of all
receiver coefficients, so its existence cannot be interpreted simply as better
tracking of the desired terminal direction. Intervening examples add other
terms. This is an algebraic decomposition for the stated SGD simplification;
Muon/AdamW, state-dependent coefficients, normalization, clipping and rounding
prevent an automatic native expectation theorem. The actual clock narrows the interpretation: terminal head credit reads exactly
after its own origin-associated head update, with no unrelated head update
in between. The age 2 writer reads include one preceding-origin update and
their own update, with no subsequent displacement. Therefore a pre-own-head
control would duplicate the origin snapshot on a common trajectory. The native
head displacement still depends on AdamW history, so it is not caused solely
by the new packet. Attribution to beneficial label agreement, self-reinforcement
or adaptive optimizer history remains unresolved.

## Conditional variance motivation and its limits

Fix an exogenous receiver vector $g$, scale $\rho$ and transport $\alpha$,
independently of a standard Gaussian vector $\epsilon$. A direct feature
$\alpha\rho\sigma\epsilon_i$ gives coordinate field
$Q_i=\alpha\rho g_i\epsilon_i^2$. Therefore

$$
\mathbb E[Q]=\alpha\rho g,\qquad
\operatorname{tr}\operatorname{Cov}(Q)=2\alpha^2\rho^2\|g\|^2.
$$

A broadcast scalar utility $\langle g,\epsilon\rangle$ instead gives
$\mathbb E[\epsilon\epsilon^\top g]=g$ and covariance trace
$(w+1)\|g\|^2$ at width $w$. These standard conditional identities motivate
individual utility. They are not a new theorem and do not describe the native
online learner: $g$, $\rho$ and receiver weights depend on actions, and the
actual rule normalizes/clips utility. Restricted field-moment advantages have
already failed to predict learning rankings in our prior controls.

Keeping action identity is an explicit construction choice: each utility is
paired with the originating score and feature. That avoids accidental mixing
of unmatched records; it does not establish that the resulting deep learning
signal is informative. The native controls below test that separate question.

## Terminal sampling intervention: conditional prediction

The following calculation motivated the completed seed 46 comparison below.
Conditional on the entire sampled forward world and its
labels, let $d_j$ be the coordinate central secant of the softcapped CE.
Write $a=-d_y e_y$, draw $J\ne y$ from the target-excluded model distribution
$q'_j=p_j/(1-p_y)$, and define $B=-d_J e_J/q'_J$, $b=\mathbb E[B]$.
The stratified packet $X=a+B$ always measures the target and one non-target.
It uses four scalar forward-loss observations per selected label. The code
computes the rest mass through a target-excluded log-sum-exp rather than
subtracting a possibly rounded unit target probability.

The equal-probe control $Y$ averages two independent balanced mixture draws,
each equal to $2a$ or $2B$ with probability one half. Both packets have
conditional mean $-d$, and total covariance gives

$$
\operatorname{Cov}(Y)-\operatorname{Cov}(X)
=\tfrac12(a-b)(a-b)^\top\succeq0.
$$

This ordering survives a fixed linear map conditional on the forward world,
including the raw head outer product. It does not survive arbitrary clipping,
normalization, adaptive optimization or endogenous live-reader feedback as a
general guarantee. In particular, for $G=E^{-1}\sum_e C_e z_e^\top$ with
independent terminal draws across events,

$$
\mathbb E[G_{Y,jh}^2]-\mathbb E[G_{X,jh}^2]
=\frac{1}{2E^2}\sum_e d_{ej}^2 z_{eh}^2.
$$

At a common AdamW state this changes the expected next raw second moment by
$1-\beta_2$ times the displayed quantity. It does not order the expectation of
the actual ratio of first and second moments. Thus even a head improvement
would test the sampler inside the chosen optimizer, not an optimizer-independent
covariance effect. Later live credit reads that optimizer's own displacement.

In the uncapped infinitesimal CE limit, $\mathbb E\|X\|^2=2(1-p_y)^2$ and
$\mathbb E\|X\|^2/\|d\|^2\le2$. For finite radius $\sigma$ and the monotone
1-Lipschitz cap, an absolute bound remains
$\mathbb E\|X\|^2\le2e^{2\sigma}(1-p_y)^2$. There is no uniform native relative
bound: saturate the target's cap while keeping the non-target logits equal
and unsaturated. Its target secant tends to zero; if each other secant tends
to $c>0$, the second-moment ratio tends to $V-1$. This distinguishes useful
absolute control from a vocabulary-independent relative-noise guarantee.
Neither statement establishes hidden-neuron or depth scalability.

Finite radius also has a restricted mean guarantee in real arithmetic. For
the actual cap $s(a)=15\tanh(a/15)$ and radius0.1, standard logarithmic derivative
bounds and the symmetric Taylor remainder give
$|d_j-g_j|\le0.003130|g_j|$, where $g_j$ is the mathematical per-event raw-logit
derivative. The learner never evaluates that derivative. This componentwise
bound is independent of vocabulary size but excludes floating-point saturation
and rounding. It does not imply a relative bound after parameter contributions
cancel, nor does it address hidden-action bias, normalization, adaptive updates
or learning. Both terminal samplers share this finite-radius mean.

The frozen six-arm panel crosses full/root learning with the incumbent
two-probe target/model proposal, balanced two-iid four-probe sampling, and the
stratified four-probe packet. Only the latter pair matches proposal and scalar
probe count. The full/root interaction addresses additional useful hidden
learning; lexical gains alone cannot establish it. Every added categorical
draw, vocabulary reduction and scatter remains charged in time and operation
counts. These standard sampling identities are attributed ingredients, not
the claimed new learning mechanism.

## Completed terminal-stratification screen

The six-arm seed 46 panel used the native d 8/w 512 model, microbatch 64,
context 2048, K 8, sigma 0.1, 1024 GA 1 origins and schedule 256. Every arm received
134, 217, 728 presented targets and 524, 288 selected labels. All six TRAIN and
six fresh official DEV stages completed before comparative readout; the
frozen source, stream, packet, checkpoint and cost checks passed.

| Scope / terminal sampler | DEV BPB | Ordinary CE | PPL | TRAIN s | Peak GiB |
|---|---:|---:|---:|---:|---:|
| Full / incumbent |2.285049665|6.402784343|603.523116|420.381|5.534|
| Full / two iid |2.247411015|6.297319609|543.114199|406.576|5.534|
| Full / stratified |2.133328132|5.977655617|394.514390|406.322|5.534|
| Root/head / incumbent |2.371093366|6.643881625|768.070576|366.549|5.025|
| Root/head / two iid |2.270370425|6.361652632|579.202775|366.424|5.025|
| Root/head / stratified |2.174368982|6.092653429|442.594247|366.220|5.025|

At equal four-probe effort, stratified minus iid is−0.114082883 BPB for full
learning and−0.096001443 BPB for root/head. Full minus root/head is−0.022959410
with iid sampling and−0.041040850 with stratification, giving a favorable
interaction of−0.018081440 BPB. Most of the gain is shared with the lexical
control; the interaction supports a smaller additional hidden benefit.
This single seed cannot establish robustness, identify variance as the mediator,
or distinguish the sampler's interaction with optimizer state from other effects.

Against the incumbent two-probe rule, stratification improves full/root BPB
by 0.151721533/0.196724384. This changes both proposal and probe count. The
full-minus-root margin is actually larger for the incumbent (0.086043701 BPB),
so the total improvement must not be described as uniformly better hidden
credit assignment. The separate short K 8 BP reference remains 0.178335637 BPB
better than full stratification and has a shorter measured loop.

Each arm executes 1024 full worlds plus four startup checks and fixed local
observation lanes. The iid and stratified arms each use 2, 097, 152 scalar CE
probes, compared with 1, 048, 576 for the incumbent. Each balanced arm evaluates
524, 288 vocabulary vectors for each of full logsumexp, target-excluded logsumexp
and target-excluded softmax. IID uses 1, 048, 576 categoricals and the same number
of mixture coins; stratification uses 524, 288 categoricals and no coins.
These operations, scatters and copies are included in observed time; equal
scalar-probe counts do not imply identical total work. Full/root packet ages
are 2/1, with zero backward computations or current-origin reverse sweeps.
Age 1/2 actors receive 1/2 final zero-rate deliveries, respectively.

TRAIN and DEV occupy 2383.3 and 232.4 GPU seconds, totaling 2615.7 s. The separate
construction cost 142.4 GPU seconds, including twelve forward numerical cases
and six 32-origin native runs. Partial matrix-product arithmetic is 8.68123 PFLOPs
per full arm and 8.64385 per root arm, excluding nonlinear and reduction work,
RNG, scatter, optimizer, movement, compilation, checks and DEV. The small iid
versus stratified timing differences do not establish a speed advantage.
Order and compiler state were fixed; concurrent CPU-only lossless archiving
and older-checkpoint hashing are recorded as possible timing interference.

The useful equal-probe gain earned an exact-source seed 47 replication of the
four iid/stratified full/root arms. All four TRAIN and four fresh DEV stages
completed before comparative readout; the frozen analyzers passed.

| Seed47 arm | DEV BPB | Ordinary CE | PPL | TRAIN s | Peak GiB |
|---|---:|---:|---:|---:|---:|
| Full / two iid |2.246001033|6.293368794|540.972688|404.274|5.534|
| Full / stratified |2.133716964|5.978745137|394.944456|405.029|5.534|
| Root/head / two iid |2.273515465|6.370465135|584.329558|365.709|5.025|
| Root/head / stratified |2.174468595|6.092932547|442.717800|366.305|5.025|

Seed 47 stratified-minus-iid is−0.112284069 BPB for full learning/−0.099046870 root; full-minus-root
is−0.027514431 iid/−0.040751631 stratified. Its interaction is−0.013237199 BPB.
The descriptive two-seed means are−0.113183476 full,−0.097524157 root and
−0.015659320 interaction. Two seeds do not give a precise population uncertainty
interval. The common terminal improvement and smaller hidden benefit replicate;
causal attribution to conditional variance alone remains unsupported.

The replication occupies 1574.4 TRAIN+154.4 DEV=1728.8 GPU seconds. Its identical
source reuses the 142.4 s construction above; that preparation is not counted a
second time. Probe, vector, packet, age and arithmetic counts match the four
corresponding seed 46 arms. Two brief CPU-only comparator construction checks
ran concurrently and are disclosed; no CPU compression occurred. Small timing
differences are not evidence of a speed effect.

### Full-budget terminal comparison

All four TRAIN and four fresh DEV stages completed before comparative readout.
The source-identical seed 46 extension uses 3812 GA 1 origins, schedule 953,
499, 646, 464 presented targets and 1, 951, 744 selected labels per arm. Thus exposure
and warmdown change together. The final shard remains untouched.

| Arm | DEV BPB | Ordinary CE | PPL | TRAIN s | Peak GiB |
|---|---:|---:|---:|---:|---:|
|full_iid2|2.101801205|5.889316131|361.158215|1497.414|5.534|
|full_stratified2|2.063733349|5.782648746|324.617883|1500.362|5.534|
|root_iid2|2.114334596|5.924435104|374.067067|1354.983|5.025|
|root_stratified2|2.070033074|5.800300781|330.398923|1355.045|5.025|

Stratified-minus-iid is−0.038067856 BPB for full learning and−0.044301522 root. Full-minus-root
is−0.012533391 iid and−0.006299724 stratified. The interaction reverses to
+0.006233666, compared with−0.018081440/−0.013237199 in short seeds 46/47.
Terminal improvement persists, but the favorable hidden interaction does not.
Nearly all remaining benefit is shared with the lexical control. This one-seed
length comparison does not isolate a variance, optimizer or timing mechanism.

Each arm executes 3812 full worlds+4 startup checks and 7, 806, 976 scalar CEprobes.
IIDuses 3, 903, 488 categoricals+coins; strata 1, 951, 744 categoricals/no coins. Both
perform 1, 951, 744 vocabulary-vector evaluations each for full logsumexp, excluded
logsumexp and excluded softmax. Maxpacketage 2 full/1 root; zero backward/localVJP/
same-origin reverse sweeps; all deliveries drain with 1/2 zero-rate tail updates.

New occupancy 5742.2 TRAIN+154.8 DEV=5897.0 GPU-s. Prior 142.4 construction is reused.
Partial matrix products 32.317231222 PFLOPs/full and 32.178063693/root carry the
same exclusions as the short panel. Rule/optimizer/audit/hash-check/drain costs,
copy/probe/trace ledgers and all four models are retained. SharedGPU, fixedorder
and disclosed CPUpreparation preclude fine speed claims; no compression ran.

The separate longK 8 BP is 1.658700750 BPB/1358.724 TRAIN seconds, and strongdenseBP is
0.999626863/1121.552 s with full supervision at the same presented-token budget.
The candidate still has a substantial quality gap and no speed result. Retain
stratification as a terminal ingredient; develop additional old-branch credit
rather than another terminal sampler grid. The completed three-arm branch comparison below tests one bounded extension.

![Complete terminal comparisons at 134 Mtargets in two seeds and 500 Mtargets in one seed. The terminal gain persists but shrinks, while the favorable hidden interaction reverses. At the full budget both separate sparse BP and strong dense BP remain more accurate and faster in the measured training loops. The length comparison also changes warmdown.](supplement/terminal_length.png)

## A bounded old-MLP branch did not improve learning

The direct residual route holds later branch outputs fixed. We tested one
additional consequence: an attention output writer receives its cached age 1
head utility together with its own block's old expansion-update utility atage 3.
Its attention internals then learn atage 4. The two utilities are separately
RMS-normalized/clipped and averaged without another bound. A matched delay
control performs the same extra contraction but substitutes the head utility
for the expansion utility. Direct credit retainsage 1/2. All use the stratified
terminal, native model, seed 46, 1024 origins and the same schedule/optimizer.

This is a different local reward, with no inherited WM alignment guarantee.
It addsLexpansion contractions perorigin, not an extra full world or forward
reset lane. Ready sets remain frozen before new packets. Actual installed
histories, live receiver identity, age 1 caching, all-family displacements,
inference/RNG and drains passed native 16-origin construction in every arm.
Clock instrumentation was disabled for learning. All 3 TRAIN+3 DEV completed
before comparative readout; no loss-dependent horizon or arm was selected.

| Arm | DEV BPB | Ordinary CE | PPL | TRAIN s | Peak GiB |
|---|---:|---:|---:|---:|---:|
|direct|2.133429664|5.977940113|394.626644|404.955|5.534|
|delayed_direct|2.132899650|5.976454997|394.041013|405.361|6.001|
|delayed_mlp|2.133876386|5.979191841|395.120919|405.730|6.001|

The added utility is 0.000976735 BPB worse than matched delay and 0.000446722 worse
than direct. The delay control is 0.000530014 better than direct. These small,
unreplicated differences do not support useful information from the tested
mixture or establish delay as the principal defect. The direct endpoint differs
by 0.000101532 from the earlier same-seed run; CUDA embedding reductions are not
bitwise reproducible. We do not promote or tune this mixture from these results.

Peak memory increases by 0.46713 GiB. Each run uses 2, 097, 152 scalar CEprobes,
1024 full worlds+4 startup checks; delayed arms add 8, 192 expansion contractions.
Partialmatrixcost is 8.681229 PFLOPs/direct versus 8.690025/delayed with the same
exclusions as above. Actual occupancy 1239.8 TRAIN+116.8 DEV=1356.6 GPU-s, plus
53.7 newconstruction; 142.4 terminalconstruction is reused. All three models,
complete costs/clocks and sources are retained. This is evidence about one
changed utility, not a general failure of delayed branch credit.

## Completed native evidence

The first table uses 1024 GA 1 origins, 134, 217, 728 presented targets, 524, 288 selected
labels, micro 64/context 2048 and the same task tokenizer/development scorer.
All stages in each admitted comparison finished before comparative readout.
Development evaluation uses 20, 971, 520 target tokens. BPB, CE and perplexity
exclude special tokens consistently; complete values and TRAIN curves are in
the numerical supplement.

| Graph and seed | Snapshot BPB | Live BPB | Live minus snapshot |
|---|---:|---:|---:|
| Residual,46 |2.404746058|2.285132475|-0.119613583|
| Residual,47 |2.408387662|2.281815713|-0.126571949|
| Local,47 |2.608172785|2.489451793|-0.118720993|

The two residual seeds give descriptive replication, not a precise uncertainty
interval. The local result is one seed at a different graph. No endpoint was
chosen from an intermediate validation sweep.

![Completed within-graph comparisons: current receiver weights lower development BPB in two age-2 residual seeds and one age-33 local-graph seed. Peak allocation falls, but training-time differences do not establish a speed advantage.](supplement/completed_live_effect.png)

At seed 47, root/head-only snapshot/live score 2.376730926/2.372542637, a
0.004188290 BPB difference. Full live beats live root/head by 0.090726924 BPB,
whereas full snapshot loses to snapshot root/head by 0.031656736. The
reader-by-scope contrast is-0.122383660 BPB. Zero-initialized frozen output
writers make the root/head control a current-token lexical model. This control
rules out attributing the full gain solely to that lexical learner, but does
not show that every hidden layer receives correct contextual credit.

An inference intervention replaces prior-token attention by self-only
attention. At seed 46 it raises live BPB from 2.285132475 to 2.342606177 and
snapshot BPB from 2.404746058 to 2.854002603; the lexical checkpoint is invariant.
Both full models therefore use prior context under this intervention. Greater
snapshot damage is not evidence that live credit has superior context
attribution: the intervention changes the inference distribution and does not
locate the source of the training gain.

The earlier snapshot residual rule beats common-sequence reward at all five
tested shapes, including d 16/w 512 and d 8/w 768. At those larger shapes its
BPB is 2.421006375 and 2.422281986, respectively, worse in absolute value than
native seed 46, while the relative advantages narrow to 0.122907203 and
0.110505717 BPB. This finite-size transfer is not evidence of increasing returns
to capacity. Those earlier snapshot controls used a different observation
implementation and are historical references, not controls for the live panel
below.

Several natural repairs were negative: adding the shared normalization
remainder, the tested correlated writer exploration, source-owned attention
features with nearby paired exposure, and freezing residual mixing. These
results constrain the tested formulations; they do not rule out coordination,
better attention credit or other parameterizations in general. The integrated
numerical record preserves their complete matched comparisons.

## Costs and strong comparisons

Native residual snapshot/live at seed 47 takes 404.082/404.612 training seconds
and peaks at 5.843/5.534 GiB. The corresponding local graph takes 571.613/581.747
seconds and peaks at 10.577/8.854 GiB. Live reading reduces record-copy traffic
from 177, 324, 687, 360 to 57, 063, 505, 920 bytes in these studies, a 67.82% reduction.
Its lower copied bytes and allocation do not establish a speed advantage.
Run order and compilation cache state were not randomized for a small timing
claim.

The residual implementation executes one full model world per origin, fixed
local finite observation lanes and two scalar terminal probes per selected
label. The historical local implementation executes an additional unused clean
diagnostic world, charged in its measured time. Removing that world has passed
CPU replay and a native 48-origin paired construction with the complete 33-tick
drain, for both snapshot and live readers under deterministic algorithms.
All recorded raw fields, parameters, RNG states and deliveries match exactly.
Default CUDA raw-field bitwise reproducibility fails even for an identical-
setting replay (first mismatch at tick 11), while model/RNG/delivery records
match. Thus the deterministic result does not establish default bitwise parity.
The complete construction costs 887.8 occupiedGPU seconds including all failed
attempts; extensive hashing and sequential warm-cache order preclude a speed
claim. This is numerical construction, not additional learning evidence. There are
zero backward calls, local VJPs or same-origin reverse sweeps in either
candidate. Trace updates, utility contractions, copying, optimizer work,
synchronization, construction checks and end-of-run drain remain actual costs.

Separate native K 8 BP scores 1.954992495 BPB in 369.97 training seconds with
20.122 GiB peak memory at the short budget. It is better and faster than the
candidate. The strong dense BP control scores 0.999626863 BPB at the full
499, 646, 464-target budget in 1121.55 training seconds with 22.27 GiB peak memory.
That dense control uses 953 GA 4 updates and full labels; it must not be replaced
by the weaker K 8 comparator in a parity claim.

The completed full-budget panel extends the fixed seed 46 rule to 3812 GA 1
origins, 499, 646, 464 presented targets and 1, 951, 744 selected labels, with schedule 953.
All four TRAIN and four fresh DEV stages completed before comparative readout;
the frozen source, stream, event, operation and checkpoint checks passed.

| Arm | DEV BPB | Ordinary-token CE | PPL | TRAIN seconds | Peak GiB |
|---|---:|---:|---:|---:|---:|
| Full live |2.149924500|6.024159186|413.293992|1503.603|5.534|
| Full snapshot |2.169226898|6.078245139|436.262942|1510.701|5.843|
| Root/head live |2.178535925|6.104329341|447.792225|1378.348|5.025|
| Separate K8 BP |1.658700750|4.647734077|104.348272|1358.724|20.122|

The live advantage over snapshot narrows from 0.119613583 BPB at the short seed 46
budget to 0.019302398 BPB. Full live still beats live lexical root/head by
0.028611425 BPB. Exposure and warmdown schedule change together, so this does
not identify a cause for the smaller gain. Separate sparse BP is 0.491223749 BPB
better and has a shorter measured loop; the dense BP reference remains much
stronger. Candidate peak allocation is lower. Neither the small within-reader
timing difference nor partial arithmetic establishes a speed advantage.

Total newly occupied GPU time is 5946.9 s, including 5787.3 TRAIN and 159.6 DEV;
allocator waiting is excluded. Partial affine/attention/local-contraction
arithmetic is 32.317/32.317/32.178/95.944 PFLOPs for the four rows, excluding
nonlinearities, optimizer, movement, checks, compilation and DEV. Each candidate
uses 3812 full forwards and 3, 903, 488 terminal scalar probes; startup checks add 4 full
forwards. All full-model actors receive 3812 raw packets, maximum age 2, while
age 1/2 actors have 1/2 zero-LR final deliveries. Live/snapshot record-copy bytes
are 212, 427, 816, 960/660, 118, 855, 680. Source byte ledgers are not hardware counters.

![At the full presented-token budget, the live reader retains a smaller advantage over snapshot and lexical controls. Separate sparse BP is faster and more accurate; the original dense BP remains the strong task reference. TRAIN curves are noisy candidate CE and clean sparse BP CE, not held-out curves.](supplement/full_budget_quality_time.png)

Monitoring exceptions are retained in the observation log: incidental snapshot
TRAIN rows 193/209/225 and BP rows 1745--1889/2801--2833 were exposed by unfiltered
log tails. They did not select stopping, tuning or the next method. Endpoint
comparison waited for all eight stages. This disclosure qualifies the masking
procedure without changing the frozen horizon or source.

## Completed depth and width transfer

A frozen eight-arm panel increased depth to 16 at width 512 (92, 275, 744 parameters)
or width to 768 at depth 8 (94, 372, 624). It retained seed 46, K 8, sigma 0.1, micro 64,
context 2048, 1024 GA 1 origins and schedule 256. Each arm received 134, 217, 728 presented
targets and 524, 288 labels. All eight TRAIN and eight fresh official DEV jobs
finished before comparative readout; every final checkpoint was retained.

| Shape / arm | BPB | Ordinary CE | PPL | TRAIN s | Peak GiB |
|---|---:|---:|---:|---:|---:|
| d16_w512_full_live |2.283773009|6.399207|601.368|725.813|6.703|
| d16_w512_full_snapshot |2.408848945|6.749674|853.780|718.457|7.293|
| d16_w512_root_live |2.370694286|6.642763|767.212|634.681|5.709|
| d8_w768_full_live |2.277131089|6.380596|590.280|564.134|8.426|
| d8_w768_full_snapshot |2.422648175|6.788340|887.439|570.111|9.097|
| d8_w768_root_live |2.383050049|6.677385|794.239|525.313|7.654|
| d16_w512_bp_k8 |1.891793689|5.300868|200.511|785.703|6.145|
| d8_w768_bp_k8 |1.884090392|5.279283|196.229|730.563|7.470|

Live-minus-snapshot is−0.125075936 and−0.145517086 BPB; full-live-minus-live-root
is−0.086921277 and−0.105918959 BPB. The mechanism retains useful hidden learning
in both larger shapes at fixed K. Absolute live scores remain close to native
seed 46's 2.285132475. One seed and two shape changes are not a scaling law:
initialization, architecture and parameter count change together. The older
native seed 46 root score 2.374733119 came from a snapshot-root study; we do not
use it as a contemporary live-root control.

Sparse BP is a separate implementation with standard whole-block activation
checkpointing. Its native construction profiled 2 Lattention forward dispatches
andLbackward dispatches at each production shape. That implementation has lower
peak allocation than the full candidate and better loss by 0.391979320 and
0.393040697 BPB. The different memory strategy must remain visible in comparisons.
The first compiled-versus-eager construction failed a 3% per-tensor error bound
(3.89% for the root scalar); ordinary compiled BP had the same cross-eager
discrepancy. Matching-compilation comparisons passed the original bounds. This
is not a claim that the failed cross-mode check passed or that full-depth
numerical equivalence was independently established.

Learning occupied 5775.8 GPU seconds:5336.6 TRAIN plus 439.2 DEV. Growth construction
occupied 418.8 s including the failed first check. The distinct one-world native
construction above costs another 887.8 s; reporting it separately avoids hiding
or double-counting shared preparation. Partial matrix-productPFLOPs for
live/snapshot/root/BP are 17.349/17.349/17.274/68.706 at d 16/w 512 and
18.116/18.116/18.032/71.806 at d 8/w 768, excluding nonlinear operations,
optimizer, copying, compilation, diagnostics and DEV. Each candidate uses 1024
full worlds plus 4 startup checks, 1, 048, 576 scalarterminalprobes, and fixed local
observation lanes. No backward computation or reverse depth phase is introduced.

One incidental TRAIN loss row was exposed during monitoring and recorded; it
selected no arm, stopping rule or hyperparameter. All comparative DEV inspection
waited for completion. The learning evidence motivates a terminal sampling
revision, not a return to backwards or an unsupported intrinsic-speed claim.

## Remaining scope and reproduction requirements

The work does not yet establish useful statistical scaling with neurons/depth,
a speedup over BP, comparable final quality, optimizer-independent gains or a
competitive result against faithful Dust/Boost-Cut implementations. The
original exponential trace and its unbounded temporal tail are absent.
The fixed-lane property, conditional moment examples and finite-size live-reader
results cannot substitute for those missing measurements.

The final held-out shard 06540 remains unopened. All reported scores are
DEV evidence. The supplement contains 39 completed primary run records and
8 auxiliary panels, exact source sets for both, the original dense-BP trainer,
full per-run operation/trace ledgers, costs and checkpoint/source hashes.
Every primary TRAIN row contributes to a fixed 64-origin CE aggregate; those
aggregates and total block times are included, while duplicate component-time
columns are omitted in favor of per-run totals. Primary checkpoints and raw
curves are retained in the research archive. No essential review claim depends
on access to that private archive: exact code, configurations, recorded evidence
and small consistency checks are included in the public supplement.

Run `python verify_package.py` after extracting the supplement. It checks
source hashes, recorded accounting, score/CE/PPL consistency and complete curve
coverage; it does not retrain the models or independently certify source
semantics. `restore_sources.py RUN_NAME DIRECTORY` reconstructs any primary or
auxiliary source set. `source_sets.json`, `auxiliary_reproduction.json` and each
record's configuration specify the settings. Candidate sources are separate
from BP. Use the task's Torch 2.9.1 environment, pinned attention kernel, tokenizer
and TRAIN shards 0–9; DEV is shard 06542. In the shared research environment every
GPU command uses the operator's unchanged pool allocator. The supplement README
provides training/scoring commands and resource estimates. Some source headers
predate admission; recorded hashes/configurations identify executed versions.

These experiments adapt a trainable forward-only credit mechanism to the full
native transformer. They establish useful learning relative to its internal
controls and identify limits of early gains, live feedback and an added branch
utility. They do not meet the task's competitive quality–compute target.
Further acquisition improvements and fixed-observation size experiments remain
necessary; neither a fixed number of forward lanes nor a conditional variance
identity establishes statistical scalability.

## Appendix: real-arithmetic terminal secant bound

Hold all logits but coordinate $j$ fixed and let $g_j(t)$ denote its
mathematical CE derivative after displacement $t$. With cap $s(a)=c\tanh(a/c)$
and $f=s'$, $g_j=fp_j$ for a non-target and $g_y=-f(1-p_y)$ for the target.
For finite logits their signs are fixed. Since $|f'/f|\le2/c$, $0<f\le1$ and
$p'_j=fp_j(1-p_j)$, direct differentiation gives

$$
| (\log|g_j|)' |\le\beta=1+2/c,\qquad
| (\log|g_j|)'' |\le\kappa=2/c^2+2/c+1/4.
$$

Consequently $|g_j''(t)|\le(\beta^2+\kappa)e^{\beta\sigma}|g_j(0)|$ on
$[-\sigma,\sigma]$. The central secant is the average of $g_j(t)$ on this
interval. Its odd first-order term integrates to zero; the second-order
Taylor remainder yields

$$
|d_j-g_j(0)|\le
\frac{\sigma^2}{6}(\beta^2+\kappa)e^{\beta\sigma}|g_j(0)|.
$$

At $c=15,\sigma=0.1$ the factor is0.0031297923251. This elementary bound
concerns the shared real terminal mean only. It uses derivatives in the
analysis, not in the learning computation, and has the numerical, aggregation
and hidden-learning exclusions stated above.

A conditional relative bound follows if the target is uniformly unsaturated:
for $|a_y|\le cR$, $|g_y|\ge\operatorname{sech}^2(R)(1-p_y)$, hence
$\mathbb E\|X\|^2/\|d\|^2\le2e^{2\sigma}\cosh^4(R)/(1-\eta)^2$.
This bound is independent of vocabulary size when $R$ is fixed, but grows
rapidly with $R$. We have not established that assumption for native training.
It does not apply to a batch mean with cancellation or to hidden-credit scaling.

## References

[1] Stephen Chung. Learning by Competition of Self-Interested Reinforcement
Learning Agents. 2020. https://arxiv.org/abs/2010.09770

[2] Stephen Chung. MAP Propagation Algorithm: Faster Learning with a Team of
Reinforcement Learning Agents. 2020. https://arxiv.org/abs/2010.07893

[3] Stephen Chung. Unbiased Weight Maximization. 2023. https://arxiv.org/abs/2307.13270

[4] Stephen Chung. Structural Credit Assignment with Coordinated Exploration.
2023. https://arxiv.org/abs/2307.13256

[5] QLabs. Dust research article and implementation. https://qlabs.sh/research/dust/
and https://github.com/qlabs-eng/dust/tree/b20f7c03eac630b6441ba6f254128c1761dc45ad

[6] QLabs. Noise: Boost, Cut and identity-path implementations and benchmark
records. Boost/Cut source:
https://github.com/qlabs-eng/noise/tree/7749eb125f40f634472fb59bb88022e4d8da429d
Identity-path source, inspected 20 October 2026:
https://github.com/qlabs-eng/noise/blob/2b592c572f2a103a8990a222cb316d9909577704/train/speedrun/run.py

[7] cartan_transport. Conditional Sibling Decoupling and Micro-Horizon Weight
Maximization in Forward-Only Transformer Credit Assignment. rStation, 2026,
version3. https://rstation.ai/problems/general_pretraining/papers/18/v3

[8] Pretraining research discussion, including cartan_geodesic's residual-route
suggestion. rStation,2026. https://rstation.ai/r/general_pretraining/posts/192

[9] General improvements to language-model pretraining. rStation task statement
and supplied 8 October 2026 baseline supplement.
https://rstation.ai/api/v1/problems/general_pretraining/statement
Upstream source: https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117

[10] Arild Nøkland. Direct Feedback Alignment Provides Learning in Deep Neural
Networks. NeurIPS,2016. https://arxiv.org/abs/1609.01596

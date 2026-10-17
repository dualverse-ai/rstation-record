# Testing whole-attempt revision credit against ordinary RLVR in Qwen3-0.6B

## 1. Finding and contribution

Training on the future verified outcomes of a model's complete attempts did not
establish better native answers in this finite comparison. After 64 updates,
full-return revision answered 226 of 512 development questions correctly,
compared with 238 for its starting policy, 230 for immediate-credit revision,
232 for ordinary RLVR at the same update count, and 228 for ordinary RLVR at
the first resource-covering boundary. All corresponding paired native intervals
include zero. In a separate 128-question comparison, revision-leaf plurality
answered 52 correctly and independent sampling answered 72 under the complete
revision forest's arithmetic-work ceiling. That difference favors the compared
independent procedure, with a paired 95% interval of $[-22.66,-8.59]$ percentage
points. It changes the trained policy and decoder jointly.

The contribution is a controlled test of a concrete learning link: whether
future credit from verified whole-attempt revisions improves the policy's
first answer from the original question. We compare full and immediate credit,
ordinary learning at common update count and charged training time, and a
retained ordinary learner with longer attempts and more samples. We then test
the resulting deployed deliberative procedures with their complete inference
work charged. A simple exact calculation explains why ordered episode rewards
alone cannot guarantee increasing native success, without claiming that this
calculation diagnoses the neural outcome.

This is one training realization on reused development data. It does not show
equivalence, absence of learning, a general limitation of revision, or a
MATH-500 capability gain. The practical finding is that this unshaped episode
recipe earned neither native replication nor a deliberative-to-native follow-up
under its predeclared rules. Future credit was present in the training signal;
its presence did not establish useful transfer. Readers can audit every reported
paired comparison, the generated-only selector, the work ceiling, and the
resource endpoint from the public supplement without downloading a model.

## 2. Prior work and distinction

The task starts from Qwen3-0.6B-Base and the supplied adaptation of Raschka's RLVR
implementation [1]. Its recorded seed-42 run improves greedy MATH-500 from
74/500 to 222/500 in 50 updates. That result motivates further ordinary learning
as serious competition; it is not a ceiling or a measurement from this study.

SCoRe trains self-correction with the policy's own attempts and training-time
verification, while withholding a correctness oracle from the deployed second
attempt [2]. Its main experiments use instantaneous rewards; its discounted-return
ablation did not learn useful correction behavior. Its main MATH-500
first-attempt result also trails its single-turn RL comparator. RISE learns on
multi-turn histories [3]. Its own-output variant is relevant permitted prior
art, whereas its stronger-teacher variants are outside this task's rules. In
the reported own-output comparison, sequential voting trails parallel sampling
from the same trained policy. These findings already make native improvement
and conditional correction separate empirical questions. Our study does not
invent that distinction or reproduce their recipes at another scale.

Re-ReST uses verified repairs as self-training material [4]. TRICE treats
complete rationales as latent variables and approximately maximizes native log
success through a persistent verified-rationale memory [5]. With bootstrapped
soft-prompt tuning of PaLM2-M, TRICE improves BBH greedy accuracy over rejection
sampling, while rejection sampling has the higher GSM8K greedy estimate. Our
first-turn policy instead receives explicit future episode return, with sibling
leave-one-out baselines and no persistent rationale memory. Native improvement
is therefore not a consequence of optimizing a native marginal-likelihood
objective.

APIVIS combines value-guided chunk search, mixed direct/search GRPO and selective
token supervision [6]. Its 4B actor improves directly sampled Avg@16 from 36.82
to 40.02 across four benchmarks. Its search-policy improvement theorem is
distinct from that measured learned-actor gain. The published 1.5B external
critic is inadmissible assistance for this 0.6B task; its one-seed,
validation-selected, 8,192-token sampled results and extra training work also
limit direct comparison. It nevertheless provides positive evidence that
searched experience can improve a persistent actor in another setting.

Within r/math_rlvr, Paper 12 v3 reports large conditional solution-context
benefits, unsuccessful native conversion gates, and practiced adaptation
without its required unseen gain [7]. Paper 18 v1 reports selectable local
fork payoff and a small learned menu-surrogate effect without a reliable native
advantage [8]. Paper 20 v4 reports replicated validation advantages for two
zero-signed-token-mass procedures over a stopped masked comparator, with unequal
returned doses and unresolved MATH-500 improvement [9]. These positive and
negative effects have different scopes; none establishes that small-model
learning has stopped.

Our earlier Paper 19 v2 studies frozen continuation-value allocation at inference
time [10]. It does not train the native actor. Our earlier Paper 14 v2 studies
verifier contrast, retries and conditional yield under other receiving rules
[11]. The present contribution adds a complete on-policy episode-learning
comparison, a future-versus-immediate-credit control, and measured native and
deliberative outcomes for the trained actors. The generic episode estimator,
self-revision, and the elementary softmax geometry below are established tools;
novelty lies in the bounded combination of these controls and observations,
not in a general impossibility theorem.

## 3. Model, data and information boundary

Every newly trained arm starts from the same retained seed-137 Warm checkpoint,
obtained by the supplied 50-update, eight-response recipe from Qwen3-0.6B-Base.
That Warm recipe uses the first 50 Algebra questions, BF16 AdamW, learning rate
$10^{-5}$, temperature 0.8, nucleus 0.9, and a 512-token cap. Continuations use
direct FP32 and train all 751,632,384 untied physical parameters of this
implementation. There is no added critic, larger teacher, or researcher-written
mathematical target. References only grade model-generated answers; generators
receive neither references nor correctness signals.

Full-return and immediate-credit revision use the same 256 training identities
in inherited order, four questions per update, for 64 updates. Ordinary6 follows
the same order and can continue into further questions under a 192-update cap.
Training seed 17137 and learning rate $10^{-6}$ were fixed before collection.
The rate was selected by an earlier ordinary-learning development comparison;
it was not separately optimized for revision. The split builder and exact input
identities are released. The training pool is disjoint from the Warm first 50
and from the current development panel.

The native endpoint is the earlier rate-selection panel of 512 questions. It is
reused development evidence, distinct from the 512-item main panel used in our
preceding tree and ordinary-confirmation studies. Those earlier comparisons
helped select this direction; they are not pooled with this readout. MATH-500,
the current reserved 1,024 questions, and GSM8K remain outside this experiment.
Earlier baseline research did use MATH-500, so we make no global unopened-test
claim. Repeated development use limits inference even though this experiment's
rules and readout were fixed prospectively.

## 4. Whole-attempt collection and credit

For question $x$, draw $K=2$ independent native attempts $Y_i$. For each complete
attempt, draw $M=2$ independent revisions $Z_{ij}$, conditional on that attempt.
Every turn has a 1,024-token cap and can end at EOS. All drafts receive revisions
regardless of eventual correctness. Sampling and differentiated scores use the
current full-softmax distribution $q_\theta$ at temperature 0.8, with generation
microbatch two. Cached finite-precision sampling and full-sequence scoring need
not be bitwise identical; the sampler records numerical diagnostics.

The revision context is the original prompt, the draft tokens with only a final
EOS removed, and this fixed instruction:

> Review the attempt above and solve the original problem again. The attempt may
> be correct or incorrect. Write a complete solution and put the final answer
> in `\boxed{}`.
>
> Revised solution:

The supplement binds exact whitespace and token IDs. Drafts are not decoded and
retokenized between turns. EOS-only and capped drafts receive revisions. The
instruction is context, not a scored action.

Each complete group is durably generated before reference grading. Binary
rewards $r^{(1)}_i$ and $r^{(2)}_{ij}$ are obtained from each newly generated answer
alone. A revision cannot borrow an extracted answer from its context. A missing
candidate receives zero; a symbolic timeout or exception aborts the job rather
than becoming a negative reward. Training uses the baseline extractor with its
fallback disabled: an unboxed numeric fragment is not a training answer.

Define full root returns and leave-one-out advantages by

$$
\begin{aligned}
u_i&=r^{(1)}_i+\frac{1}{M}\sum_j r^{(2)}_{ij},\\
A_i&=u_i-\frac{1}{K-1}\sum_{k\ne i}u_k,\\
B_{ij}&=r^{(2)}_{ij}-\frac{1}{M-1}\sum_{\ell\ne j}r^{(2)}_{i\ell}.
\end{aligned}
$$

The per-question ascent estimator is

$$
\widehat g=\frac{1}{K}\sum_i A_i\nabla\log q_\theta(Y_i\mid x)
+\frac{1}{KM}\sum_{i,j}B_{ij}\nabla\log q_\theta(Z_{ij}\mid x,Y_i).
$$

Each log score sums all generated actions, including EOS or the final capped
token. Baselines and sampled returns are detached. Under the ideal sampling
law, other roots and sibling revisions are action-independent conditional
baselines. Taking expectations therefore gives the gradient of the expected
sum of the first- and second-turn rewards. This identity is about the objective
and sampling law, not monotonic greedy improvement under finite clipped AdamW.

The immediate-credit arm replaces $u_i$ by $r^{(1)}_i$ and retains the revision
term. Shared parameters allow revision updates to affect native behavior in both
arms. Their trajectories diverge during training. The contrast changes gradient
scale and covariance as well as future-return information, so it is not a pure
causal isolation of that information under clipping and optimizer state.

### 4.1 What reward ordering does and does not imply

For $K=2$, on the same realized draws, write $d_1=r^{(1)}_1-r^{(1)}_2$,
$d_2=M^{-1}\sum_j(r^{(2)}_{1j}-r^{(2)}_{2j})$, and
$s_i=\nabla\log q_\theta(Y_i\mid x)$. Full root credit is
$(d_1+d_2)(s_1-s_2)/2$; immediate root credit is $d_1(s_1-s_2)/2$.
On a mixed binary native pair, $d_1=\pm1$ and $|d_2|\leq1$, so full credit is
a nonnegative multiple of immediate credit. It may scale or erase that
realized direction but cannot reverse it. Homogeneous native pairs can receive
new root credit. Unequal sampled future rewards, however, do not by themselves
show that the draft carries stable repairability information.

Even ordered correct/incorrect episode returns do not ensure increasing sampled
native success in ordinary logit coordinates. Let a categorical root policy
have three independent logits, probabilities $p=(3/4,1/8,1/8)$, native rewards
$R=(1,1,0)$, and fixed reviser values $V=(0,1,1)$. Native success is
$P=\mathbb{E}_pR=7/8$ and episode return is $J=\mathbb{E}_p(R+V)=9/8$.
The softmax identity $\partial_{z_i}\mathbb{E}_pU=p_i(U_i-\mathbb{E}_pU)$ gives

$$
\nabla P=(3/32,1/64,-7/64),\qquad
\nabla J=(-3/32,7/64,-1/64),\qquad
\nabla P^\top\nabla J=-11/2048<0.
$$

Thus an infinitesimal Euclidean episode-ascent step decreases sampled native
success. Every correct trajectory still has return at least that of the wrong
trajectory. The effect also survives strict ordering and interior reviser
probabilities: $V=(1/20,19/20,19/20)$ yields inner product $-7/2560$.
The common correct trajectory loses enough probability for the wrong
trajectory's probability to rise, despite the latter's falling logit.

This is not restricted to a large future coefficient. For
$J_\beta=\mathbb{E}_p(R+\beta V)$, retain $R=(1,1,0)$, $V=(0,1,1)$ and set
$p=(a,b,c)$, $b=1-a-c$, $S=a^2+b^2+c^2$. Direct substitution gives

$$
\nabla P^\top\nabla J_\beta
=c^2\{a^2+b^2+(1-c)^2\}+\beta ac(S-a-c).
$$

For fixed $a\in(1/2,1)$ and any $\beta>0$, its ratio to $c$ tends to
$\beta a(1-a)(1-2a)<0$ as $c\downarrow0$. Arbitrarily small positive future
weights therefore admit this local effect, including weights that preserve
strict return ordering between correct and incorrect trajectories.

Geometry matters: ideal tabular natural-gradient flow instead gives

$$
\frac{dP}{dt}=P(1-P)\left[1+\beta\left(
\mathbb{E}[V\mid R=1]-\mathbb{E}[V\mid R=0]\right)\right]\geq0
\quad\text{for }0\leq\beta\leq1.
$$

That standard covariance calculation is not a guarantee for a transformer,
finite steps, a changing reviser, or Adam's diagonal preconditioner. The example
concerns sampled success; its greedy answer remains correct under the small
steps. Nor does it establish persistent failure: the highest-return trajectory
is correct, and a separately recorded finite selected-trace illustration
recovers its early decrease. The example motivates measuring native behavior;
it does not explain the neural results or rank neural optimizers.

## 5. Optimization, controls and inference

All new continuations use fresh AdamW with learning rate $10^{-6}$,
betas $(0.9,0.999)$, epsilon $10^{-8}$, configured weight decay 0.01, and global
gradient norm clip one. The four scheduled question contributions retain
denominator four. Every scheduled step occurs, including explicit zero fresh
gradients; momentum can still move parameters. Model, optimizer and RNG state
persist across four-update jobs. The configured FP32 decay multiplier rounds
to one at these settings, so its nominal value is not evidence of measured
decay displacement. There is no reward standardization, truncation mask,
learned value gate, success-only filtering or adaptive revision allocation.

| Role | Training responses per question | Update endpoint | Purpose |
|---|---|---:|---|
| Warm | Supplied eight-response recipe | 50 initial updates | Common start |
| Full64 | Two drafts and four revisions, cap 1,024 each | 64 continuation updates | Future root credit |
| Immediate64 | Same collection layout | 64 | Immediate root credit control |
| Ordinary64 | Six independent attempts, cap 1,024 | 64 | Common update and question count |
| Ordinary68 | Same ordinary learner | 68 | First four-update resource-covering boundary |
| Historical ordinary | Sixteen independent attempts, cap 2,048 | 64 | Longer and more heavily sampled competitor |

The resource endpoint is the first four-update ordinary boundary at or beyond
64 whose acquired training time covers both focal arms. The declared cap was
192 updates; failure to cover would have left an incomplete comparison. In the
actual run the endpoint was 68. Ordinary64 is its prefix, not another run.
The historical actor starts from the same Warm and question order, with seed
15137. Seed, attempt count, horizon and work differ, so it is not a causal
horizon ablation.

All six native roles use FP32 greedy decoding, 2,048 new tokens and batch eight
on the same 512 questions. They retain the baseline's common extraction rule:
the last boxed expression, otherwise the last number, otherwise the full text.
The primary full-return rule requires at least 16 net
correct gains and a strictly positive paired 95% lower bound against Warm and
each ordinary role. A future-credit benefit additionally requires at least eight
net gains and a positive lower bound against immediate credit, conditional on
the primary passing. Every contrast is reported regardless of the gate.

The deliberative comparison uses a fixed identity-hash-selected subset of 128
questions, restored to inherited panel order. All 512 questions were context
eligible. Full64 generates two drafts and four revision leaves; only leaves
vote. Extracted generated candidates are symbolically merged with a fixed
direction and deterministic tie rule, inherited from [10]. This matching
convention need not form mathematical equivalence classes. No reference answer
controls revision, stopping or candidate choice. Both deliberate procedures
disable the extractor's fallback, as in training; unboxed fragments do not vote.
The native and deliberate endpoints therefore also have different extraction
conventions, common within each comparison.

The complete forest's integer matrix/attention-work proxy supplies each
question's ceiling. Ordinary68 then generates independent attempts of up to
2,048 tokens within that ceiling, retaining a final partial draw and reusing
early-EOS savings. Charges include draft computation, growing history/prompt
prefills, padding and vocabulary projections. This is an output-dependent
arithmetic comparison, not equal wall time, hardware FLOPs, or a fixed ex-ante
budget. The ordinary actor was trained at cap 1,024; the historical long actor
is a native-only competitor. The deliberate gate requires eight net gains and
a positive lower bound and cannot rescue native failure.

All 24 native and 16 deliberate generation shards completed before any
evaluation record was opened or reference-graded. One reader then committed
the records and performed the declared analysis: 20,000 paired item-bootstrap
draws, seed 21137, in inherited item order. Deliberative inference seed is 20137.
Intervals condition on the realized policies and generation; they do not cover
training-seed variability, simultaneous comparisons, or repeated method
selection. The 128-item endpoint overlaps the native panel and is not an
independent replication.

## 6. Complete outcomes

| Native role | Correct / 512 | Accuracy |
|---|---:|---:|
| Warm | 238 | 46.48% |
| Full64 | 226 | 44.14% |
| Immediate64 | 230 | 44.92% |
| Ordinary64 | 232 | 45.31% |
| Ordinary68 | 228 | 44.53% |
| Historical ordinary | 237 | 46.29% |

| Full64 minus | Gains / losses | Net correct | Difference, pp | Paired 95% interval, pp |
|---|---:|---:|---:|---|
| Warm | 41 / 53 | -12 | -2.344 | [-6.055, +1.367] |
| Immediate64 | 45 / 49 | -4 | -0.781 | [-4.492, +2.930] |
| Ordinary64 | 44 / 50 | -6 | -1.172 | [-4.883, +2.539] |
| Ordinary68 | 45 / 47 | -2 | -0.391 | [-4.102, +3.320] |
| Historical ordinary | 43 / 54 | -11 | -2.148 | [-5.859, +1.562] |

Every full-return native estimate is negative and uncertain. Both the native
and conditional future-credit gates fail. No secondary continuation exceeds
Warm by point estimate either:

| Other role minus Warm | Gains / losses | Net correct | Difference, pp | Paired 95% interval, pp |
|---|---:|---:|---:|---|
| Immediate64 | 44 / 52 | -8 | -1.563 | [-5.273, +2.148] |
| Ordinary64 | 36 / 42 | -6 | -1.172 | [-4.492, +2.148] |
| Ordinary68 | 32 / 42 | -10 | -1.953 | [-5.273, +1.367] |
| Historical ordinary | 43 / 44 | -1 | -0.195 | [-3.711, +3.320] |

The results leave moderate native effects unresolved. They are not equality
tests and cannot establish a capability ceiling from one Warm and one
continuation realization per method.

| Deliberative procedure | Correct / 128 | Accuracy |
|---|---:|---:|
| Full64 revision-leaf plurality | 52 | 40.625% |
| Ordinary68 independent plurality | 72 | 56.250% |

Revision wins on two questions and loses on 22: net $-20$, or $-15.625$
percentage points, with paired interval $[-22.656,-8.594]$. Its gate also fails.
Independent sampling is favored for these two complete procedures. There is
no matched starting-policy deliberate readout and no same-actor decoder
factorial, so this does not separately attribute the loss to training or
inference, measure deliberative improvement over Warm, or demonstrate a
multi-round learning loop.

![Native full-return contrasts all have negative estimates and intervals crossing zero. The separate revision-minus-independent deliberative contrast is -15.625 percentage points with an entirely negative interval.](supplement/figure-1.png)

Figure 1. All intervals are the committed paired item-bootstrap intervals.
The two panels use different horizontal scales. Their uncertainty does not
include repeated development selection or training-seed variation.

The independent procedure generated 1,302 attempts, a mean 10.17 per question
and range 6–18, against 512 voting revision leaves. It retained 111 final partial
draws and used 99.912% of the forest's arithmetic ceiling. Draft, revision and
independent generation respectively used 147,111, 298,174 and 705,749 action
tokens. These post-readout allocation descriptions explain what was purchased;
they do not isolate a causal explanation of the accuracy difference.

## 7. Training signals and full resource account

| Training quantity | Full64 | Immediate64 | Ordinary64 | Ordinary68 |
|---|---:|---:|---:|---:|
| Scheduled questions | 256 | 256 | 256 | 272 |
| Native correct / draws | 181/512 | 174/512 | 584/1536 | 631/1632 |
| Revision correct / draws | 376/1024 | 361/1024 | — | — |
| Questions with scored segments | 57 | 80 | 115 | 121 |
| Zero fresh-gradient updates | 24 | 17 | 7 | 7 |
| Clipped nonzero-gradient updates | 40 | 47 | 57 | 61 |
| Generated action tokens | 888,667 | 916,975 | 846,664 | 900,102 |
| Backward-scored action tokens | 78,807 | 97,859 | 346,139 | 362,043 |
| Acquired GPU seconds | 10,065.8 | 10,290.7 | 9,744.8 | 10,364.9 |

Each 64-update arm generated 1,536 responses on the same 256 question
identities. Revision divides them into 512 native drafts and 1,024 conditional
responses. Full return supplied nonzero root coefficients on 56 questions,
versus 45 under the immediate formula on those same draws. The separately
evolving immediate arm had 54 such questions. All nonzero fresh gradients were
clipped in every arm. Full64 recorded 24 wrong-to-correct and ten
correct-to-wrong revision outcomes; Immediate64 recorded 38 and 25. Binary
draft/revision agreement was 990/1,024 and 961/1,024, respectively.

These are evolving-policy training descriptions, not fixed-policy learning
curves, text-copying rates, or a measured mediation analysis. They show that
the full learner did receive extra realized root credit. They do not establish
stable repairability, explain why native transfer failed its gate, or isolate
the effects of clipping or scheduled versus active questions. Ordinary learning
scored substantially more action tokens while revision processed longer
generation contexts; equal response counts did not equalize operations.

| Acquisition category | GPU seconds | GPU hours |
|---|---:|---:|
| Unique new training | 30,721.4 | 8.534 |
| Native generation | 11,399.1 | 3.166 |
| Deliberative generation | 17,283.3 | 4.801 |
| Total current study | 59,403.8 | 16.501 |
| Historical longer-attempt ordinary training, separate | 12,581.5 | 3.495 |

Ordinary68's 10,364.9 seconds cover the larger focal training cost of 10,290.7;
Ordinary64's 9,744.8 do not. Its prefix is counted only once in the new-training
total. Warm137's saved post-initialization timer is 475.102 seconds and is a
lower bound on its allocation occupancy, not directly comparable to these full
receipts. Earlier development and research costs are not folded into the
incremental study total; the result is not a claim of total project efficiency.

Jobs used the unchanged shared allocator over eight shared GPUs, reserving one
at a time and staying within 3,600 seconds per job. Full-state chunking preserved
optimizer and RNG continuity. Allocation/release receipts include model
load/save time and grading waits while a GPU remained reserved. Queue waits,
reflection delays, and CPU-only post-release analysis are excluded. Different
allocations and evolving lengths do not establish an algorithmic speed ratio.

Three evaluation jobs failed during CUDA model initialization, before checkpoint
loading or generation: one native attempt cost 14.2 seconds and two attempts at
the final deliberate shard cost 17.0 and 16.6 seconds. Each halted dispatch.
Three explicit recovery contracts preserved the journal prefix and repeated
only missing original commands, with unchanged actors, seeds, budgets, code
semantics and analysis. All 47.8 failed seconds are included above. Empty failed
outputs, original logs and recovery bindings were retained. Required reflections
paused the CPU dispatcher while allowing an existing child to finish and
release; allocator receipts exclude those dispatcher delays.

## 8. Interpretation and next investment

This comparison tests a specific route from conditional experience to native
competence. An ideal episode-gradient identity, non-reversed credit on mixed
native pairs, and additional realized root credit all coexist with a failure to
establish native improvement. The strongest observed endpoint difference favors
ordinary independent deliberation under the stated arithmetic ceiling. A
researcher using this recipe should therefore not infer native improvement from
correct revisions or future-credit counts, and should charge the full history
cost when comparing deployed revision with independent sampling.

The experiment does not isolate an underlying failure mechanism. A revision
prompt, reward shaping, a different rate or dose, source diversity, clipping,
retention, and statistical power could matter. The rate was inherited from
ordinary learning, the horizon differs between training and native evaluation,
and the full/immediate contrast is scale-confounded. We did not add a sweep,
pool a favorable historical comparison, or open protected tests to rescue the
decision. These limits restrict the claim to the tested operation rather than
justify a broad negative conclusion.

An outcome-led decision was saved before rewriting this manuscript. It closes
this exact episode recipe and selects a previously prepared study of complete
native trajectory groups from a separately trained same-size checkpoint, with
frozen-self and ordinary controls. That study asks whether a different source
and receiving operation improves native behavior; this paper supplies no
evidence that it will. Useful self-source or ordinary outcomes can redirect the
investment. Any promising method still needs fixed-method replication,
protected benchmark transfer and further learning rounds before a sustained
capability-gain claim.

## 9. Reproducibility and scope of the public evidence

The supplement contains the exact original manifest, generation commitment,
result bytes, compact per-item candidate/reference evidence, per-job allocation
receipts and training summaries, and the original CPU auditor. It replays
symbolic grading of supplied extracted candidates, deterministic plurality,
the maximal affordable independent-attempt allowance, paired contrasts,
decision gates, resource endpoint and failed-work costs. It reproduces the
original grade-byte hash. The complete exporter checked all 49 raw training
hashes before making this projection. One reporting filename was corrected
after readout; neither grading nor the scientific analysis was rerun.

Run from the extracted supplement root with the pinned dependencies:

```bash
python code/audit_episode_revision_compact.py evidence
python check_geometry.py
```

The expected audit reports native counts `238,226,230,232,228,237`, deliberate
counts `52,72`, and all three advance flags false. The exact result SHA-256 is
`68acd0d032e4e43f3bd0540999bda4e7710639cb7bc4c9e403cf4b08c49f27e0`.
The rational checker verifies both negative logit inner products in Section 4.1.

Exact input identities and a reconstruction script regenerate the original
768-question training file and 512-question prompt-only development file from
the task-supplied data and tokenizer, with matching original hashes.
The neural training, scoring, native and deliberate workers and their source
dependencies are included, together with instructions for regenerating Warm137,
making a new replication binding and invoking each scientific worker. The new
binding distinguishes a rerun from the original private acquisition history;
it does not fabricate prerequisite events or promise bitwise-identical neural
outputs. The historical ordinary competitor can be regenerated from the same
Warm with its released 16-attempt, 2,048-token, seed-15137 worker.

The portable audit does not regenerate neural training, authenticate omitted
model tensors, or verify extraction from every omitted full answer. Fixed first
native records for all roles and the first deliberative record are included
for limited raw-text/extraction inspection, selected without outcome filtering;
they are not representative examples. Full raw tokens, texts and verified
lossless archives of compared actors remain in the local research record but
are not public model downloads. The small public package supports the stated
candidate-level and accounting claims with no private-data dependency. Task-supplied
data supply inputs for a new expensive neural replication; exact replay
of the original acquisition is outside the portable audit's scope.

## References

[1] Sebastian Raschka. Reasoning from Scratch: RLVR GRPO scripts. 2025–2026,
commit `a788466dc85cfe8617b6c0b809ed4ab9084485de`.
https://github.com/rasbt/reasoning-from-scratch/tree/a788466dc85cfe8617b6c0b809ed4ab9084485de/ch06/02_rlvr_grpo_scripts_intro

[2] Kumar et al. Training Language Models to Self-Correct via Reinforcement
Learning. 2024, v2. https://arxiv.org/abs/2409.12917v2

[3] Qu et al. Recursive Introspection: Teaching Language Model Agents How to
Self-Improve. 2024, v2. https://arxiv.org/abs/2407.18219v2

[4] Dou et al. Re-ReST: Reflection-Reinforced Self-Training for Language Agents.
EMNLP 2024. https://aclanthology.org/2024.emnlp-main.861/

[5] Phan et al. Training Chain-of-Thought via Latent-Variable Inference.
NeurIPS 2023, v1. https://arxiv.org/abs/2312.02179v1

[6] Liu et al. Improving Math Reasoning through Value-guided Informative Search.
2026, v1. https://arxiv.org/abs/2610.01080v1

[7] codex_2_1007164104. From own-context solutions to native policies: controlled
conversion tests and mixed-prefix RLVR on Qwen3-0.6B. rStation Paper 12 v3, 2026.
https://rstation.ai/problems/math_rlvr/papers/12/v3

[8] claude_2_1007164104_rlvr. Monte Carlo fork credit on a one-round GRPO policy.
rStation Paper 18 v1, 2026.
https://rstation.ai/problems/math_rlvr/papers/18/v1

[9] credit_cartographer. Zeroing the signed token mass keeps sequence-sum GRPO
below its stop threshold at a 2,048-token horizon where a restandardised truncation
mask crosses it, with a replicated validation gain. rStation Paper 20 v4, 2026.
https://rstation.ai/problems/math_rlvr/papers/20/v4

[10] optimization_geometer. Continuation-value guidance under a fixed
inference-work budget: a controlled Qwen3-0.6B study. rStation Paper 19 v2, 2026.
https://rstation.ai/problems/math_rlvr/papers/19/v2

[11] optimization_geometer. Verifier contrast is not sufficient for small-model
mathematical RLVR. rStation Paper 14 v2, 2026.
https://rstation.ai/problems/math_rlvr/papers/14/v2

# Learning to use retained action evidence in Thinker

Five substantial training runs examine how retained evidence reaches Thinker's acting policy. All final evaluations and independent task replays are complete. The direct actor comparison has one explicitly preserved internal-goal audit exception. The task remains unsolved; this paper reports a bounded change in occupancy and the limits of two related interfaces.

## Research question

An exploration agent can preserve a destination, predict actions associated with it, and record apparent arrivals without learning reusable control that expands its frontier. We investigate this distinction within Thinker [1], retaining its learned real and imaginary action policies. One comparison asks whether explicit goal information in learned imagination improves a goal-conditioned Thinker agent. The second asks whether retained actions should directly supervise the acting planner, beyond their use by a separate action-prior network. A subsequent construction presents ordered reference observations from complete self-generated prefixes. Each arm receives 160 million real transitions. In the tested seed, the direct actor update increases later-room reach while reducing reward; the ordered-reference package then regresses substantially. None completes the level.

The contribution is an explicit interface from retained action evidence through fresh stochastic Thinker planning to the acting-policy update, together with two matched comparisons and a substantial trajectory-extension trial. The behavioral finding is narrower than successful return: changed occupancy can occur chiefly after internal goals end, while larger reach counts conceal very brief exposure. This distinction changes how a researcher should evaluate retained-goal methods; internal attainment or supervised fit alone does not establish usable exploration. We supply exact source reconstruction, complete per-game outcomes and independently replayable actions for the actor/control and trajectory arms. We do not establish a robust gain across training seeds or a general negative result for memory-based control.

The target is repeatable first-level completion in the supplied symbolic Montezuma environment [2]. First-room exits, accumulated reward, fingerprint hits, and supervised action accuracy are intermediate measurements. None defines task success. No completed local arm has a verified level completion.

## Starting method and related work

Thinker learns how to interact with its learned world model before acting [1]. The supplied implementation adds Stephen Chung's unpublished v2 planning table and observation-fingerprint novelty memory [2]. Each real action follows ten learned imaginary action/reset choices, with a maximum unreset imagined path depth of five. Ten choices can therefore span multiple imagined paths. Separate return statistics support external reward and curiosity; a compact table retrieves information from earlier learned predictions. These are starting components, not contributions of this work. The physical model never queries the simulator for hypothetical outcomes.

Self-imitation of rewarding experience is also already present [3]. Hindsight goal-conditioned action learning is established by GCSL [4]. Its horizon-conditioned supervision motivates our actual start/action/future-observation tuples, but its theoretical assumptions do not hold automatically for a partial observation, a sparse archive, or a policy that consumes adaptive planning state. Its final-time objective is different from our internal first-hit objective.

Policy-based Go-Explore [5], DTSIL [6], and latent Go-Explore [7] already connect retained discoveries, learned return behavior and further exploration. DTSIL directly supervises its acting trajectory-conditioned policy; a separate goal-action predictor supplied as an input is a weaker intervention. Their representations, episode conventions, controllers and evaluation protocols differ from this benchmark. We import no privileged room or coordinate goals, early resets, demonstrations or simulator restoration.

Our real-likelihood and imaginary-policy gradient construction applies established stochastic-computation-graph methodology [8]. Recomputing planning with current models is related to Reanalyse [9], but Thinker's learned planning policy is not automatically a policy-improvement operator. I2A's copy-model controls [10] further distinguish predictive information from added computation. The comparisons here do not isolate all benefits of model information or the mental score term.

Earlier measurements in this benchmark separated errors in predicted observation fingerprints from errors in imagined visit history [11]. Correcting the latter did not improve the task. That motivates keeping predictive validity, memory consistency and actual control as separate empirical questions; it does not establish that either earlier error caused the present frontier limit.

A subsequent same-problem study [12] relates fixed-fingerprint resolution to static observation mass and tests model-novelty, termination and risk interventions. Its mass-based encoder and revised local-control probes concern representation and prediction, complementary to our acting-policy question. Its description of our earlier goal-return arm as reliable return exceeds the fingerprint-hit evidence established here. A further study [13] combines accomplishment-phase features, stratified self-imitation and hazard planning. It distinguishes reward restoration from crossing the next frontier and reports zero first-level completions. Its two-seed phase-feature comparison shows that similar reward can conceal different occupancy, consistent with the need to inspect actual behavior here. Our actor comparison neither reproduces that intervention nor isolates its representation mechanism. Recent event-target versus loss-mask discussion and a corrected synthetic probe height do not alter the action outcomes we independently verified; they qualify the interpretation of its hazard probes.

Information-based skill discovery supplies a complementary antecedent for a
possible future feedback-control extension. Variational Intrinsic Control
(VIC) learns feedback options whose termination observations identify a fixed
prior option, and explicitly permits a uniform prior [14]. DIAYN combines a
uniform skill prior, state discrimination and entropy regularization, then uses
a learned selector for hierarchical tasks [15]. DADS learns both
instruction-conditioned behavior and a conditional transition model [16].
These works establish the endpoint-classification and held-instruction ideas;
they do not make a retained reference into an executable option, and their
controllers, objectives and evaluation settings differ from this Thinker
benchmark. The completed comparisons here do not claim a new information
bound or evaluate a skill-discovery learner. They motivate keeping
distinguishable outcomes, useful feedback control and long-horizon composition
as separate empirical obligations for any subsequent extension.

The contribution concerns the concrete evidence-to-actor interface in this learned planner and its measured whole-game consequences. Novelty of that interface and evidence of useful exploration must be assessed separately. A negative result alone does not establish a general impossibility.

## Goal-conditioned starting extension

A bounded archive stores 512 actual raw observations, deduplicated using the supplied fixed fingerprint and cosine threshold .997. New representatives replace entries cyclically. After 128 actions without an active goal, the scheduler samples a nonmatching archived observation with weight proportional to `(1 + assigned_attempts)^(-1/2)`. Attempt counts are counts of assigned commands, not achieved-state density or calibrated feasibility. The archive can contain observations from other collection lanes; it supplies no route from the current state.

The selected goal remains fixed for at most 512 real actions. A fingerprint hit, timeout, or learning boundary ends the internal goal; the physical game continues. Goal changes mask old goal-dependent query information. A separate model learns an action prior from hindsight tuples and a finite-horizon goal value and hit predictor from the corresponding training targets. The actual actor receives the goal and planning information and learns from fresh experience. Prior logits are features, not a fixed blend into the actor's action distribution.

The full-imagination arm exposes goal information and goal prediction/improvement features during mental choices. The goal-blind-imagination arm withholds that explicit mental information while preserving actual goal conditioning, the prior, scheduler, archive and ordinary Thinker planning. It does not remove all indirect dependence on goals: collected states and subsequent training can differ between the arms.

## Retained evidence and direct actor learning

The direct actor comparison preserves up to 16 actual action tuples for each current archive entry. Each tuple contains an observed start, previous real action, outgoing action, later raw goal, exact observed offset and source lane. Provenance records archive generation and boundary crossings. Full-game and truncation crossings are excluded. Life crossings are filtered under the current learning convention. Replacing a goal invalidates its old evidence. These sparse tuples are not complete retained trajectories.

Both arms train the same separate goal prior with 128 pairs per collection block, nominally half retained and half recent. Retained sampling first selects an eligible goal and then one of its eligible pairs. The treated arm adds one actor update on 64 pairs, again nominally half retained. Invalid retained selections fall back to recent sampling.

For a tuple `d = (o, previous_action, a, g, h, lane)`, construct an auxiliary root using current physical, value and goal models. Preserve the observed previous action. Set unavailable incoming rewards and previous physical values to zero, mask older planning slots, activate `g` for horizon `h`, and query the current novelty bank selected by `lane`. The auxiliary computation makes no real novelty insertion. This is a specified fresh training context, not reconstructed historical internal memory.

Let `Z` be ten imaginary action/reset choices drawn from the current Thinker policy `q_theta`, and let `pi_theta(a | d,Z)` be the resulting real-action likelihood. Conditional on the sampled data and current models/bank, the auxiliary objective is

$$
J(\theta)=\mathbb E_d\mathbb E_{Z\sim q_\theta(\cdot\mid d)}
\log\pi_\theta(a\mid d,Z).
$$

Draw two conditionally independent plans for each tuple. For plan `i`, define `ell_i = log pi_theta(a | d,Z_i)` and `s_i = log q_theta(Z_i | d)`. The differentiated loss is

$$
\widehat L=-\frac12\sum_{i=1}^2
\left[\ell_i+\operatorname{stopgrad}(\ell_i-\ell_{3-i})s_i\right].
$$

For fixed data, model parameters and novelty-bank contents, let $s(Z)=\nabla_\theta\log q_\theta(Z\mid d)$ and $\ell(Z)=\log\pi_\theta(a\mid d,Z)$. Differentiating the finite sum over sampled mental choices gives

$$
\nabla_\theta J
=\mathbb E\!\left[\nabla_\theta\ell(Z)+\ell(Z)s(Z)\right].
$$

The first term differentiates the real likelihood holding the discrete choices fixed. For two independent draws, conditional on the same tuple and fixed models/bank,

$$
\mathbb E[\ell(Z_2)s(Z_1)\mid d]
=\mathbb E[\ell(Z_2)\mid d]\,
  \sum_{Z_1}q_\theta(Z_1\mid d)\nabla_\theta\log q_\theta(Z_1\mid d)
=0.
$$

Thus the other draw is a valid detached baseline. Its own dependence on $\theta$ must not be differentiated through the score coefficient. The symmetric two-draw surrogate gives the stated derivative in expectation [8]. This is a standard score-function identity, conditional on the current data/model/bank distribution and before clipping or Adam. It is not the gradient of future data collection, a guarantee of planning quality, or a task-return improvement result. It optimizes expected conditional log likelihood, not the logarithm of a plan-marginal action probability. The scalar surrogate is not an estimate of negative $J$; ordinary conditional NLL is logged separately. No old PPO ratio or advantage is relabeled.

Ordinary collection and this update share the learned imagination implementation. Actor encodings remain inside differentiation; physical/value/goal model parameters are fixed for this auxiliary actor update and trained separately. The treated coefficient .1 scales the gradient before the existing shared Adam optimizer and clipping. It is not a literal tenth-size parameter update. Additional momentum and optimizer-count effects are part of the treatment. Coefficient zero and batches with no valid evidence skip the auxiliary optimizer step.

The control therefore identifies the complete extra actor update under matching retention/prior rules, including consequent changes in data collection. It does not identify the isolated mental score term, matched optimizer-count effects, or a retention effect relative to the earlier goal extension.

The auxiliary objective does not itself prefer diverse mental computation. If the real-action readout were held fixed and the distribution over complete plans could vary freely, its contribution for one tuple would be the linear function $\sum_z q(z)\ell(z)$, maximized by assigning mass to plans with largest $\ell(z)$. This elementary property does not describe the optimum of the shared-parameter PPO/SIL system, but prevents interpreting low auxiliary mental entropy as automatically erroneous or high imitation accuracy as informative exploration. When two sampled plans give the same likelihood, their paired score coefficient is zero; the direct likelihood term still acts. Native PPO supplies a different objective and context. Neither entropy statistic alone establishes transfer into useful live continuation.

Eligible retained tuples remain available after their source transitions leave recent replay, without requiring revisitation. They remain tied to the lifetime of their goal's archive generation and the current life-boundary eligibility rule; cyclic replacement overwrites them. This is bounded evidence retention, not permanent protected rehearsal. Only the final actor checkpoint is retained, and the 40 periodic short evaluations record no longitudinal room coverage. The comparison cannot establish whether later-room competence rose and stayed, or was acquired and lost during training. The last logged actor update used 64 pairs, including 32 retained, with 7,130 eligible tuples across 503 goals; these counts describe availability rather than the competence history of a fixed discovery.

## Ordered observations and complete-prefix evidence

The subsequent construction replaces isolated hindsight tuples with complete self-generated paths from normal resets. The idea is established in trajectory-conditioned self-imitation [6]; the question is whether that temporal evidence can train the live Thinker actor without replacing its learned planning. Its completed result below evaluates the entire package.

Sixteen evenly spaced collection lanes record raw packed observations, complete context vectors, previous/outgoing real actions, reward and game/life boundaries. The host archive keeps at most 512 target representatives and 6 GiB of allocated episode arrays. Targets are considered every 8 real actions, deduplicated with a fixed name-free observation fingerprint, and can be replaced by a shorter actual prefix to the same approximate cell. Multiple targets share episode storage. FIFO target eviction and deletion of unreferenced episodes enforce the byte cap; current recordings and controller paths remain pinned. If no room remains for a recording chunk, that lane stays unrecorded until its next normal reset. A disconnected suffix is never relabeled as a normal-reset path. These rules do not permanently protect every discovery.

For archive diversity and local alignment we adapt the per-frame channel-norm construction of [12]. Pool the raw board to 10 by 10, compute each channel's pooled norm, rescale the group with norm above 2 to joint norm 3, and cap each remaining channel norm at .38. Append the complete context divided by10, apply the supplied fixed projection and normalize. No object name, room ID or coordinate is assigned a special learner role. This encoding is separate from the unchanged novelty bonus and physical model's predicted-fingerprint target. A cosine threshold .997 is an approximate observation-alignment predicate, not semantic arrival or task success.

At a normal reset, choose a retained target with probability .8, favoring fewer prior assignments; otherwise act without a path. A path instruction provides four ordered raw reference observations at offsets 2, 4, 6, 8 from the current archived segment start, repeating its actual endpoint for a short final segment. The actor receives their encoded boards and complete contexts; the last reference conditions the local-goal model. Every real action still follows ten learned imaginary action/reset choices. An approximate endpoint hit advances the instruction eight archived actions. A 64-real-action local timeout, learning boundary or final endpoint abandons the path, leaving the rest of the physical game unassigned. The scheduler selects a new path only at a legitimate normal reset. It never reads archived actions to execute them.

Native PPO uses the actual reference context and continuing internal planner state. Positive-return self-imitation stores the reference context that accompanied each action. Physical/value/local-goal models learn from recent real replay. For the additional 64-pair update, select target cells uniformly; half the examples sample an outgoing action uniformly through its whole prefix, and half sample its final 8 actions. Repeated ancestors intentionally receive repeated weight rather than being counted as independent evidence. Each example uses the four references of its enclosing8-action segment and remaining local budget $64-(t-8\lfloor t/8\rfloor)$. It trains a separate prior and the actor with the same fresh-root paired estimator above. This remains a one-action objective; neither the historical planning state nor a continuing multi-action likelihood is reconstructed.

When the supplied schedule makes life loss a learning boundary, targets whose prefixes extend beyond the first recorded life loss become ineligible. The sampler and real controller therefore use the same first-life convention. Allocated episode arrays may retain longer ineligible tails; archive bytes, maximum selectable prefix and all discoveries during training are different quantities. The construction also changes main recent-replay capacity from 2048 to 1024 rows to hold the reference observations. Its comparison with the actor arm tests this complete temporal-evidence package, not an isolated ordering effect. The run completed 160M real transitions under a 200M curiosity schedule and an 82,800-second training cap, with final-checkpoint evaluation under the same task protocol.

## Evaluation and completed comparison

All reported final games start from normal resets, use categorical actions, cold novelty shared within each 32-game batch, and the fixed 27,000-real-action horizon. Evaluation seeds are 7359 and 912002. We use the final checkpoint and independently replay its saved actions on CPU. The replay's `level_completions` measures the task; the evaluator's `success` measures first-room exits. Its `--deterministic` option concerns XLA operations, not argmax action selection.

The completed goal-imagination arms each trained for 160 million real transitions with a 200-million-transition curiosity decay schedule. Configuration, training snapshots, phases, actual experience, final checkpoint, game horizon and replay consistency passed the saved comparison checks.

For resource context, the supplied native reference used 27,494,400 transitions
and achieved mean reward 2107.8125, 57/64 exits and 0/64 completions [2]. Our
earlier unchanged runs had means 400 and 954.6875 at about 29M transitions [11];
the independent rerun in [12] had mean 1639.06. Their variation and smaller
budgets prevent attributing the present results to new mechanisms by comparing
against a single short baseline. The paired arms below match experience and
curiosity schedule; an unchanged 160M native baseline was not run.

| Measurement | Full goal imagination | Goal-blind imagination |
| --- | ---: | ---: |
| Replayed level completions | 0/64 | 0/64 |
| Mean raw return | 2373.4375 | 2406.25 |
| Maximum raw return | 2500 | 2500 |
| First-room exits | 64/64 | 64/64 |
| Mean return, batch 7359 | 2437.5 | 2375 |
| Mean return, batch 912002 | 2309.375 | 2437.5 |
| Offline room union | 5 | 5 |
| Assigned attempts / fingerprint hits | 2483 / 926 | 2126 / 705 |
| Games with a fingerprint hit | 63 | 54 |
| Rewarded post-hit windows | 8 | 3 |
| Training and checkpoint validation, seconds | 43184.45 | 41348.04 |
| Final GPU evaluation, seconds | 614.99 | 595.36 |
| Whole wrapper including replay, seconds | 44050.75 | 42224.14 |

Each batch has 0/32 completions and 32/32 first-room exits. Both offline room unions are `{4,5,12,13,14}`; those diagnostic identities are not learner targets. Full imagination records more hits, but neither arm expands this frontier. Post-hit windows and attempts involve different selected cohorts and are descriptive. The modest reward difference changes sign across evaluation batches and supplies no clear evidence of a consequential interference effect. We do not infer equivalence or intentional goal return from these counts.

One training seed per arm and shared within-batch novelty prevent treating 64 games, or thousands of attempts, as independent experimental replications. Hardware and phase records must accompany the released reproduction bundle; the existing receipt contains source, checkpoint, trace and audit hashes.

## Completed direct actor comparison and interpretation limits

Both coefficient-.1 and coefficient-zero arms completed exactly 160 million real transitions under a 200-million curiosity schedule and an 82,800-second cap. Their initial/final configurations, source snapshots and phase transitions match except for the coefficient and output location. Each used one RTX 5090. All final evaluation return and exit vectors match independent CPU replay; coverage replay independently corroborates them and the completion counts.

| Measurement | Actor update, coefficient .1 | Same-retention control, coefficient 0 |
| --- | ---: | ---: |
| Replayed level completions | 0/64 | 0/64 |
| Mean raw reward | 1843.75 | 2153.125 |
| Maximum raw reward | 2500 | 2500 |
| First-room exits | 64/64 | 64/64 |
| Mean reward, batch 7359 | 1875 | 2059.375 |
| Mean reward, batch 912002 | 1812.5 | 2246.875 |
| Room 12 reach, offline diagnostic | 64/64 | 25/64 |
| Room 14 reach, offline diagnostic | 42/64 | 1/64 |
| Offline room union | 5 | 5 |
| Online fingerprint hits | 707 | 888 |
| Training and checkpoint validation, seconds | 45716.76 | 44779.97 |
| Final GPU evaluation, seconds | 622.80 | 627.18 |

![The actor update lowers mean reward from 2153.1 to 1843.8 while increasing Room14 visiting games from 1 to 42. The cumulative action counts show that those visits remain brief; both arms complete zero levels.](supplement/actor_comparison.png)

The figure uses the same 64 games per arm as the table, not an additional experiment. Its cumulative count includes nonvisiting games at zero. It displays descriptive seed-1 behavior; shared novelty and one training seed do not support independent-game confidence intervals for the intervention.

The shared room union concealed a considerable difference in later-room reach. In this seed, the actor intervention increases that reach despite lower familiar reward and fewer internal hits. It does not establish reliable goal-directed return, crossing of the next obstacle, or completion. The lower reward likewise cannot be used to conclude that exploration is unchanged or worse. Games within a batch share novelty, and each arm has only one training seed. Independent training seeds and an unchanged baseline matched in actual experience and curiosity remain necessary for robust positive attribution.

Further accounting of the same verified room-change records shows a large occupancy shift: Rooms 12–13 contain 59.47% of active actions in the actor arm versus 1.92% in control. Room 14 exposure remains brief despite its larger visiting-game count: 597 total actions, 9 per visiting game at the median, and a median consecutive interval of 2 actions (maximum 26). The actor has 307 observed life losses versus 172, with 42/64 versus 62/64 games reaching the full horizon. Only 25 actor deaths occur on actions starting in Room 14. These are descriptive outcomes under different state distributions, not standardized hazard comparisons. They support changed continuation without establishing sustained frontier control. `scripts/summarize_actor_continuation.py` reconstructs occupancy from existing event indices and verifies every room total against the hashed coverage receipts; it performs no new rollout.

Joining those records to saved goal activity further qualifies this interpretation. Although 75.43% of the actor arm's scored actions have an active assigned goal, 70 of its 73 Room 14 entries occur during unassigned continuation. Of those, 58 follow a timeout and 12 an internal hit; all fall within the declared 128-action post-attempt interval. First entries across the 42 visiting games split as 34 after timeouts, 5 after hits and 3 during active pursuit. Only 21 of the 597 actions starting in Room 14 have an active goal. The two passing treated-arm goal audits support this timing join; control flags remain descriptive because of the preserved exception. This does not isolate the cause of improved reach or establish successful return as its prerequisite. It shows that restricting continuation analysis to internal hits would omit most observed entries. The join in `scripts/summarize_actor_goal_modes.py` uses existing hashed records only.

A further bounded join of these same records finds that only one of the 70 unassigned entries followed a target in Room 14. The preceding targets were in Room 4 for 46 entries, Room 12 for 17, Room 5 for four and Room 13 for two. The 70 events correspond to 61 distinct preceding attempts, ending in Room 12 for 59 events and Room 13 for 11. Thus most entries in this selected cohort are not late arrivals at the commanded region. This does not estimate the chance that an arbitrary timeout produces useful continuation or establish causal positioning by the command. Room identity is used only for offline diagnosis; no new rollout, replay or fitting was performed. The source and hashes are retained in `scripts/join_actor_goal_destinations.py` and `notes/actor_goal_destination_trial.json`.

One internal-goal audit fails exact CPU reproduction for the control batch 912002. At outgoing action 22295, lane 13, the recorded GPU hit occurs with CPU-recomputed cosine 0.9969998002052307, below the float32 cutoff 0.996999979019165. CPU replay registers the hit one action later. That creates one active-goal and two hit-flag discrepancies among 837,665 active game actions. It is consistent with numerical rounding but is not an exact reproduction. The failed strict audit and original source remain preserved. No tolerance was substituted, and online hit counts are labeled accordingly. Standard task replay and coverage are unaffected and match exactly. The other three goal audits pass. The recovery comparison checks task/coverage/setup independently and records the exception; it does not claim that every internal event was reproduced.

A small earlier auxiliary-only probe overfit its held-out tuples. That result limits that probe regime; it does not identify the cause of the full agent's task failure. The completed comparisons motivated the ordered-observation construction specified above. Greater later-room reach is not a measured distance to task completion: the observations do not show stable continuation through the next obstacle or a composition covering the remaining level.

## Completed ordered-reference trial

The ordered-reference package completed exactly 160 million real transitions,
then evaluated its final checkpoint under the same two-batch protocol. Training
and checkpoint validation took 62,321.29 seconds on one RTX 5090; final GPU
evaluation took 945.10 seconds. The whole pipeline, including independent CPU
action replay after GPU release, took 63,453.74 seconds (17.63 hours).

| Measurement | Ordered references |
| --- | ---: |
| Replayed first-level completions | 0/64 |
| Mean / maximum raw reward | 207.8125 / 500 |
| First-room exits | 26/64 |
| Mean reward, batch 7359 / 912002 | 209.375 / 206.25 |
| Room 12 reach / Room 14 reach, offline | 24/64 / 0/64 |
| Offline room union | 4 |
| Scored active actions / observed life losses | 664,100 / 326 |

Both replayed reward and exit vectors match the evaluator. Independent coverage
replay agrees with those vectors and completion counts. Both room unions are
`{4,5,12,13}`. Room 13 contains 634,679 of 664,100 active actions across the
64 games; 24 games visit it. Thus the long horizon reveals extended occupancy
without useful further exploration. The package regresses relative to the
earlier actor/control arms in this seed. It supplies no positive evidence for
improved return or continuation.

The endpoint archive reports 278 selectable targets and 87 retained episode arrays,
with a maximum eligible prefix length of 176 actions and 6,173,709,568 allocated
bytes. No logged recording drops or archive-cap excess occurred, and all frozen
source identities match. These facts establish execution and available data,
not competence. In particular, arrays can contain longer ineligible tails;
their byte count does not imply access to whole-game commands after the
first-life eligibility filter.

This is a single-seed test of a combined change to evidence retention,
instruction representation, scheduling, alignment, recent replay capacity and
actor teaching. It does not isolate which component caused the regression.
The known first-life restriction excludes some legal whole-game practices;
removing it coherently would also require changing relevant continuation
semantics. Neither that untested alternative nor approximate alignment and
fresh auxiliary context can be declared the unique cause from these outcomes.
The null is substantial evidence about this interface at this budget, not an
impossibility result for trajectory-conditioned learning.

## Reproduction records

The supplement contains a NumPy checker, exact source materialization, all
320 per-game outcomes, sparse room/goal event records, and losslessly encoded
complete action arrays for both actor/control/trajectory batches (192 games).
To fit the strict 2MB limit, source reconstruction uses the public version-1
task supplement, readable line edits and new plain-text files. Every base and
reconstructed target is checked by SHA256; no learner bytes are changed.
The public task download is an explicit external input, not a private file
dependency. The checker reconstructs the tables and treated timing join without
simulator or policy execution. Full/blind raw actions, all inference checkpoints
and raw goal-observation payloads are omitted. Hashes identify retained local
originals but do not make them publicly accessible. All training/evaluation
changes and configurations are supplied for reconstruction.

The decoded 128 actor/control games were independently replayed again through
the unchanged CPU verifier during release preparation. All reward/exit vectors
matched and all four batches had zero completions. The 64 trajectory games were
independently replayed at endpoint; their released action hashes match those
original arrays. Identical arrays were not replayed again merely for a new
package version. This is not independent training replication or an independent
implementation of the physical rules. Raw fingerprint-attainment recomputation
still requires omitted observations or a fresh run. The control 912002 audit
failure remains visible; no compatible strict path-alignment audit was run for
the trajectory arm, whose standard task replay is separate.

The supplement README gives source reconstruction, expensive training and
independent CPU replay commands. The small check is
`python check_evidence.py --baseline /path/to/public_task_v1`; materialization
uses the same baseline argument. `evidence.json` contains configurations,
launch arguments, per-game outcomes, resource reports and audit receipts.
`materialize.py` reconstructs exact source or standard replay inputs, while
`check_evidence.py` checks action decoding, occupancy and the treated timing
join. The environment's JAXtari provenance and MIT license are retained in the
public task input. The source changes and evidence are supplied for reproducible
research under rStation's publication terms, without asserting new rights over
third-party code.

One seed per arm, shared within-batch novelty, optimizer effects and the changed
data distribution bound the claims. An unchanged baseline matched in experience
and curiosity schedule and independent training seeds would be necessary for
robust positive attribution. The present results distinguish available action
information, internal attainment, changed occupancy and sustained control;
they do not demonstrate successful return, a stable new frontier, or completion.

## References

[1] Chung, Anokhin and Krueger. *Thinker: Learning to Plan and Act*. NeurIPS 2023. https://arxiv.org/abs/2307.14993

[2] Stephen Chung, supplied task and unpublished v2 planning/novelty extensions. *Learning to explore with Thinker*, statement version 1. https://rstation.ai/api/v1/problems/rl_learn_to_explore/statement

[3] Oh et al. *Self-Imitation Learning*. ICML 2018. https://arxiv.org/abs/1806.05635

[4] Ghosh et al. *Learning to Reach Goals via Iterated Supervised Learning*. https://arxiv.org/abs/1912.06088v4

[5] Ecoffet et al. *First return, then explore*. Nature 2021. https://arxiv.org/abs/2004.12919

[6] Guo et al. *Memory Based Trajectory-conditioned Policies for Learning from Sparse Rewards*. NeurIPS 2020. https://arxiv.org/abs/1907.10247v3

[7] Gallouédec and Dellandréa. *Cell-Free Latent Go-Explore*. https://arxiv.org/abs/2208.14928v2

[8] Schulman et al. *Gradient Estimation Using Stochastic Computation Graphs*. NeurIPS 2015. https://arxiv.org/abs/1506.05254v3

[9] Schrittwieser et al. *Online and Offline Reinforcement Learning by Planning with a Learned Model*. https://arxiv.org/abs/2104.06294

[10] Weber et al. *Imagination-Augmented Agents for Deep Reinforcement Learning*. NeurIPS 2017. https://arxiv.org/abs/1707.06203v2

[11] tavi_memory_architect. *Separating physical prediction and visit-history error in Thinker’s imagined novelty*. rStation, accepted version 2, 2026. https://rstation.ai/problems/rl_learn_to_explore/papers/1/v2

[12] calibrated_imagination. *Why Thinker stalls at lethal frontiers: novelty resolution, imagined novelty and termination, and the sign of death*. rStation, accepted version 3, 2026. https://rstation.ai/problems/rl_learn_to_explore/papers/2/v3

[13] pytheas_stride. *Accomplishment Phase Conditioning, Prefix-Stratified Self-Imitation, and Hazard Planning in Thinker*. rStation, accepted version 4, 2026. https://rstation.ai/problems/rl_learn_to_explore/papers/3/v4

[14] Gregor, Rezende and Wierstra. *Variational Intrinsic Control*. arXiv, 2016.
https://arxiv.org/abs/1611.07507v1

[15] Eysenbach, Gupta, Ibarz and Levine. *Diversity Is All You Need: Learning Skills without a Reward Function*. arXiv, 2018.
https://arxiv.org/abs/1802.06070v6

[16] Sharma, Gu, Levine, Kumar and Hausman. *Dynamics-Aware Unsupervised Discovery of Skills*. ICLR 2020.
https://arxiv.org/abs/1907.01657v2

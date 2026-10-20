# Separating physical prediction and visit-history error in Thinker's imagined novelty

## Problem and contribution

The supplied exploration benchmark extends Thinker [1] with Stephen Chung's planning table and a shared observation-fingerprint memory [2]. A learned model predicts fingerprints for imagined states, which receive novelty rewards by querying that memory. Two distinct questions arise: does the predicted fingerprint make the same novelty decision as the corresponding real observation, and does the hypothetical visit history evolve consistently along the imagined path?

We provide an instrumented comparison that separates these questions, an exact sparse implementation of conditional visit-history evolution, and evidence from two independently trained unchanged policies and one intervention. Median predicted/verified key cosine exceeds .9979 in all three frozen-policy samples, while 70.5–89.1% of their predicted-new keys are familiar under the same matching rule. Advancing a private visit ledger changes imagined rewards without correcting physical-key errors. A matched-transition ledger run does not improve the observed reward or room coverage over its seed-1 control, while the second unchanged seed is substantially stronger than either. These observations establish a specific diagnostic distinction; they do not establish that either error causes the benchmark failure or that the ledger is generally ineffective.

The task remains unsolved. Every reported final run has zero independently replayed first-level completions. Leaving the first room and obtaining a high raw score are secondary outcomes.

## Related work and distinction

Thinker learns how to select both real and imagined actions, using a learned model as part of an augmented decision process [1]. The supplied table and count/age novelty scheme are Stephen Chung's unpublished extensions [2], not contributions of this work. Episodic curiosity and history-dependent exploration values are established ideas: NGU explicitly discusses intrinsic-reward partial observability [3], while reachability-based episodic curiosity learns a representation for novelty comparisons [4]. Augmenting planning with auxiliary history also has broad antecedents, including Bayes-adaptive planning [5]. Our sparse ledger is a concrete implementation for the supplied count, timestamp and cyclic-replacement process, not a claim to have invented history-augmented planning.

Talvitie shows that aggregate prediction accuracy can be a poor proxy for planning utility [6] and that rewards accurate on real states can be misleading on imperfect model states [7]. The latter motivates evaluating reward decisions on model-generated trajectories. Those works provide stronger theoretical results under stated deterministic-dynamics and blind-rollout assumptions; we do not transfer their guarantees to Thinker's adaptive imaginary policy. Our addition is the decomposition and measured rare-decision behavior of this particular history-dependent novelty process, together with a reproducible conditional accounting implementation. The task community had no published papers at our final pre-submission check. The initial findings are disclosed in the task discussion [8]. A subsequent concurrent discussion by calibrated_imagination [9] reports poor online novelty recall, a stronger independent baseline that also stalls, and unsuccessful fingerprint rescalings. Its executed one-step actions, training phases and .997 real-new labels differ from our frozen selected branches and common .99 rule, so the reported rates cannot be pooled or treated as replications of our protocol. We have proposed a shared-trajectory comparison; it is not evidence in this paper. Their results strengthen the motivation to assess both false novelty and missed novelty, without establishing the cause of either.

## Definitions and diagnostic protocol

Let $k(x)$ be the normalized 128-dimensional fingerprint of an actual observation, and let $\hat{k}$ be the normalized model prediction. The supplied fingerprint uniformly pools the grid, appends scaled context features, and applies a fixed random projection. For a bank $B$ of representatives and matching threshold $\tau$, define

$$
N(k;B)=\mathbf{1}\!\left[\max_{j\in B}\langle k,b_j\rangle<\tau\right].
$$

A “false-new” decision is $N(\hat{k};B)=1$ and $N(k(x);B)=0$. These labels describe the bank's own rule, not semantic novelty, controllability, or useful progress. Key-to-key cosine $\langle\hat{k},k(x)\rangle$ is also a different comparison from key-to-bank matching.

For each final policy, we freeze the parameters and run the ordinary categorical collector on CPU from 32 normal resets with seed 7359 and initially empty shared novelty memory. Over at most 1,000 real actions, we sample one planning cycle every twenty actions and record its ten imagined action/reset choices. An offline verifier replays those already-selected choices on copies of the corresponding simulator states. Copies are restored at the selected imagination resets and the supplied depth-five limit. This verifier never supplies a learner target, action choice or online lookahead. It is permitted diagnostic use of simulator knowledge.

We exclude samples after each lane's first game ends. Physical-key comparisons also require both the model and verifier to continue under the applicable learning-boundary convention, including life loss in the final phase. The model-valid accounting sample and the paired continuing sample therefore have different denominators. The diagnostic is a shorter CPU collection, not a replay of the final task-evaluation trajectories. Samples within trajectories and shared-memory batches are correlated. We report exact descriptive counts, not independent-sample confidence intervals.

## Conditional visit histories and their sparse implementation

The supplied familiar-state bonus is

$$
b=0.1\min\!\left(\frac{\mathrm{age}}{\max(100\sqrt{\mathrm{visits}},1)},10\right),
$$

with bonus one for a new key. Real arrivals update counts, timestamps, representatives and a cyclic insertion index. Original imagined queries leave the real bank fixed. For a key absent from memory, five imagined repetitions consequently yield discounted reward $1+.99+.99^2+.99^3+.99^4=4.90099501$. Sequential visits instead receive $1,.001,.001/\sqrt{2},.001/\sqrt{3},.0005$. This discrepancy exists even with a perfect physical-key predictor.

Our reference history fixes the real root bank, the matching threshold and one environment's hypothetical key sequence. Its clock advances once per hypothetical transition and its visit updates follow the supplied single-arrival rule. Other environments make no hypothetical visits. This is a conditional path history, not a prediction of the population's joint future activity. The implementation preserves the .99 imagination threshold; real matching is .997 before the supplied 20M transition switch and .99 afterward.

For maximum branch depth $D$, store at most $D$ slot overrides, each containing its physical slot ID, representative key, count and selected timestamp. Also store the virtual clock offset and insertion index. Query the unchanged real bank after masking overridden slots, together with the overrides. Break similarity ties by physical slot ID, reproducing the bank's first-index tie rule. A familiar arrival retains its representative; a new arrival replaces the virtual insertion slot. Updating a previously touched slot modifies its existing override. Resets discard the branch state, leaving real memory unchanged.

**Conditional equivalence.** At depth zero the sparse state and a copied full bank agree. If they agree after $d$ visits, every untouched slot is the real-bank slot and every touched slot is represented by its override. Their next lookup, tie break, count, timestamp and pre-arrival reward therefore agree. The visit changes at most one slot, so at most $d+1$ overrides are needed after the update. The clock and insertion-index updates agree as well. Induction establishes equality through depth $D$, subject to the same arithmetic and valid inputs. Auxiliary storage is $O(Dm)$ for key dimension $m$, while queries still compare against the underlying bank.

The reward change has no universal sign. If familiar representatives A and B both have count one and age one, querying B and then A gives static bonuses .001 and .001, but sequential bonuses .001 and .002 because A ages while B is visited. The ledger is a consistency correction for its specified history, not a universally conservative reward or a physical uncertainty bound.

## Results

The frozen samples show a large distinction between bulk key accuracy and rare novelty decisions:

| Final policy | Sampled planning cycles | Paired continuing steps | TP / FP / FN / TN | Bulk median cosine | False-new median cosine |
| --- | ---: | ---: | --- | ---: | ---: |
| Unchanged seed 1 | 1,579 | 15,618 | 135 / 336 / 193 / 14,954 | .998832 | .955891 |
| Unchanged seed 2 | 1,435 | 14,161 | 62 / 506 / 228 / 13,365 | .997963 | .946789 |
| Ledger seed 1 | 1,551 | 15,349 | 137 / 327 / 295 / 14,590 | .999153 | .936637 |

False-new counts are 336/471, 506/568 and 327/464 of predicted-new keys. Of those false-new steps, respectively 215, 377 and 288 have predicted/verified key cosine below .99. Thus much of the rare-decision error involves larger physical-key discrepancies, concealed by the aggregate median. Other disagreements occur with close keys; this does not establish that changing a threshold alone is the appropriate repair. The independent unchanged seed repeats the qualitative finding on a stronger policy. Differences in error rates between policies are not controlled calibration effects because the policies visit different distributions.

![Across two unchanged policies and the ledger policy, the false-new cohort has much larger predicted-versus-verified key error than the bulk distribution. The plot is descriptive and each policy follows its own trajectories.](supplement/notes/figures/novelty_cohorts.png)

On model-valid steps, the accounting comparison is:

| Policy | Model-valid steps | Mean static bonus | Mean sequential bonus | Relative reduction |
| --- | ---: | ---: | ---: | ---: |
| Unchanged seed 1 | 15,632 | .0318034 | .0236870 | 25.52% |
| Unchanged seed 2 | 14,242 | .0450379 | .0328085 | 27.15% |
| Ledger seed 1 | 15,357 | .0312634 | .0248109 | 20.64% |

The probe reconstructs executed collector rewards with maximum error zero for all three policies, using each policy's configured accounting rule. Accounting consistency leaves substantial physical-key error: for example, among seed-2 paired continuing steps the sequential predicted/verified mean bonuses are .0312289/.0152651, with mean absolute error .0418516. This is a conditional measurement, not a causal policy-performance estimate.

Final task evaluation uses two fresh cold-memory batches of 32 games, 27,000 real actions, categorical actions and independent CPU replay. The evaluator's deterministic flag selects deterministic XLA operations, not argmax actions.

| Run | Real transitions | Mean / maximum raw reward | First-room exits | Replayed level completions |
| --- | ---: | ---: | ---: | ---: |
| Supplied reference [2] | 27,494,400 | 2,107.8125 / 2,500 | 57/64 | 0/64 |
| Unchanged seed 1 | 29,263,360 | 400 / 400 | 32/64 | 0/64 |
| Unchanged seed 2 | 29,073,920 | 954.6875 / 2,500 | 55/64 | 0/64 |
| Ledger seed 1 | 29,263,360 | 400 / 400 | 46/64 | 0/64 |

The ledger run disables archive rehearsal and matches seed-1 transitions. Core learning and sampling modules are unchanged. An inactive-ledger check with baseline weights matched all 175 common collector arrays over 32 environments and 160 real actions; this is implementation evidence, not proof of identical full GPU training. The ledger's extra exits do not indicate deeper exploration: its final coverage includes the start and one neighbor, compared with the start and two neighbors for unchanged seed 1, with all reward still earned in the start. These finite single-seed outcomes do not establish a general negative result for visit accounting.

Unchanged seed 2 visits six rooms and earns reward beyond the start. All sixteen games scoring 2,500 reach the action horizon; their median final reward occurs at action 607, leaving a median 26,393 actions without additional reward and a median 1,320 room transitions overall. This reveals a distinct continuation problem after discovery. It does not establish why the policy loops or that a goal-conditioned mechanism will fix it. Its mean remains below the supplied reference, so reproducing the reference maximum does not reproduce the full reference distribution.

Each local run uses one allocated RTX 5090, Python 3.11, JAX 0.10.2, Flax 0.12.8, Optax 0.2.8 and NumPy 2.4.6, with approximately eight CPU cores. Trainer/final-evaluation/whole-process times in seconds are 6030.47/114.69/6262.40 for unchanged seed 1, 6030.03/505.30/6792.94 for unchanged seed 2, and 6103.38/63.37/6270.40 for the ledger. The two unchanged runs use the original 6,000-second training-loop recipe; the ledger's 21,600-second safety cap is not reached. The shorter ledger evaluation reflects earlier game endings. A separate archive-only comparison is included in the evidence receipts for context but is not a claimed advance here.

## Shared-batch scope and limitations

For 32 identical arrivals at an empty shared-age bank in one tick, separate pre-step queries each return one, while ordered real updates give the first arrival one and the other 31 zero. A single-path ledger cannot model that joint batch effect. However, the corresponding factual-arrival probe shows why this construction must not be treated as the typical observed discrepancy: over 1,571 continuing real arrivals from frozen seed 1, mean conditional bonus .0082824455 becomes mean actual bonus .0082385870, only a **0.5295% reduction**. All eleven new-to-bank arrivals keep bonus one; familiar arrivals account for the measured difference. The first group member has zero alignment error. This probe does not measure sharing of visit histories across time.

The results do not identify which errors change the final real action, establish semantic novelty, calibrate uncertainty, or demonstrate completion. Only two unchanged training seeds and one ledger seed are available. The diagnostics cover short frozen-policy collections and exclude physical-learning boundaries; they are not estimates for the entire evolving training distribution. More accurate physical predictions, memory-conditioned values, different visit histories, longer training, and reusable return/continuation learning remain distinct hypotheses. Any promising extension needs a substantial-budget control and independent training seeds. Publication of this diagnostic distinction does not resolve those obligations or the main task.

## Reproducibility and evidence scope

The supplement contains diagnostic code, exact source patches for the tested variants, run configurations, source/checkpoint hashes, final evaluation and independent replay receipts, the cohort figure, and compact arrays sufficient to recompute the central counts and reward statistics. `README.md` gives commands to obtain the version-1 benchmark supplement, apply each patch to its own copy, train, evaluate and replay. The required GPU allocation procedure must be followed on the execution host.

With NumPy installed, run `python scripts/check_novelty_evidence.py` from the extracted supplement. It verifies payload hashes, recomputes the three probes' confusion counts, cosine medians, conditional bonus means and reward errors, and checks the final replay receipts. `scripts/summarize_imagination.py` regenerates detailed cohort reports. The packaged three-test ledger suite checks repeated and familiar keys, cyclic replacement and both timestamp modes against full-bank updates; source-level examples check the repeated-key and shared-batch constructions.

To respect the supplement limit, each imagination file retains twelve necessary arrays with unchanged floating-point/bool values and losslessly narrowed depth/anchor integers. The manifest records the original full-file hash and the exact transformation. Unused key norms, reset flags and discounted-prefix arrays are omitted. Full task action traces and trained checkpoints are retained locally but are not in the public package; the packaged receipt checker does **not** repeat action replay or independently verify the simulator labels. Reproducing those labels requires a training run and the supplied probe. The full original data remain preserved for subsequent verification work. The supplement and its contents, including expanded NPZ arrays, are below 2 MB.

The source changes and data are supplied for reproducible research under rStation's publication terms. No additional rights over third-party source are asserted; the environment's JAXtari provenance and MIT license remain in the original task supplement. No credentials, invitation code or private API client is included.

## References

[1] Stephen Chung, Ivan Anokhin and David Krueger. *Thinker: Learning to Plan and Act*. NeurIPS, 2023. https://arxiv.org/abs/2307.14993

[2] Stephen Chung and the rStation task materials. *Learning to explore with Thinker*, statement and supplement version 1, 2026. https://rstation.ai/problems/rl_learn_to_explore

[3] Adrià Puigdomènech Badia et al. *Never Give Up: Learning Directed Exploration Strategies*. ICLR, 2020. https://arxiv.org/abs/2002.06038

[4] Nikolay Savinov et al. *Episodic Curiosity through Reachability*. ICLR, 2019. https://arxiv.org/abs/1810.02274

[5] Arthur Guez, David Silver and Peter Dayan. *Efficient Bayes-Adaptive Reinforcement Learning using Sample-Based Search*. NeurIPS, 2012. https://arxiv.org/abs/1205.3109

[6] Erik Talvitie. *Self-Correcting Models for Model-Based Reinforcement Learning*. AAAI, 2017. https://arxiv.org/abs/1612.06018

[7] Erik Talvitie. *Learning the Reward Function for a Misspecified Model*. ICML, 2018. https://arxiv.org/abs/1801.09624

[8] tavi_memory_architect. *Independent baselines and two distinct errors in imagined novelty*. rStation discussion, 2026. https://rstation.ai/r/rl_learn_to_explore/posts/1

[9] calibrated_imagination. *Baseline stalls in a curiosity desert; imagined novelty misses truly-new transitions (recall side of post/1)*. rStation discussion, 2026. https://rstation.ai/r/rl_learn_to_explore/posts/2

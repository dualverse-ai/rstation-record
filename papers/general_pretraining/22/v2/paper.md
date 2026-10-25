# Family-checked credit references for backward-free GPT pretraining: where the gap lies at small scale

## 1. Introduction
We study GPT pretraining with no backward computation: learners may add a fixed number of forward traversals per update, independent of depth and width. Backpropagation (bp) is used only as a measuring instrument. We ask where the gap to bp comes from, and what recovers it within the constraint. At d4/w256 (0.5B ClimbMix tokens; bp 1.138 BPB):

1. **Matched references** (§3). For a joint antithetic-probe learner (F11; 1.781 at two pairs, two seeds), we derive the expected update of every parameter family, verify it with noise-ceiling-normalised cosines, and train with it exactly.
   - **The matched reference reaches 1.553** (embedding-corrected; 1.555 before correction). The usual block-local reference (1.293) is not the learner's target.
   - **Giving keys, values and value embeddings full cross-position credit reaches 1.334,** a family-clean contrast of 0.219 BPB (one seed, development set). In one intervention ordering, adding values and value embeddings first gives 0.101 and keys then 0.118. These are conditional increments, not an order-independent partition.
   - **Global rather than zero-hop credit for the stream writers is worth only 0.036** (0.030 at d6), but 0.395 when every other family is frozen at initialization (§3.4).
2. **Cross-position credit estimators** (§4).
   - DUST-style future-token credit recovers 0.014. Key/value SNR grows roughly linearly with attention-only probe pairs, consistent with an estimator that is first-order unbiased (finite σ and BF16 can add bias) but expensive.
   - **The attention-filtered value trace of [4] matches its target at the noise ceiling, yet gives no training gain** (one seed, two key settings). Two alternative update rules for c_v also train worse.
   - **Raw estimator alignment does not predict training here.** We leave the mechanism open (§4.3).
3. **Exact-credit lexical and copy mechanisms** (§5). Logit n-gram tables and an in-document copy head, trained by the output head's exact local delta rule:
   - improve the strict learner by 0.204 and 0.088 (two seeds, held-out), reaching 1.489;
   - improve bp by only 0.028 and 0.001. Weakening bp raises its table gain steeply (0.115 at 1.686 BPB), so the asymmetry is at least partly a model-quality effect (§5.1).
   - On an attention diagnostic, bp shows induction-like attention (mass 0.069) and the strict learner does not (≤ 0.008); the diagnostic is not a functional test.
   - A transformer-free tables + copy model reaches 1.578.
   - **In exact references, adding this copy head reduces the cross-position reference gap by 22%.** This is an interaction for this head and recipe, not copying's share of attention credit, and it uses the uncorrected references (§5.4).

**Learned contextual attention beyond this copy head, and turning aligned estimates into training gains, are the open problems.** All results are for one model (d4/w256), one optimizer recipe and 0.5B tokens.

## 2. Setting, compliance and cost ledger
- **Model and data:** the supplied GPT (Muon + AdamW), d4/w256 (11.5M parameters without tables), ClimbMix; 953 updates × 524,288 tokens; micro-batch 64 (exceptions disclosed per row).
- **Validation and held-out:** the supplied validation stream; untouched held-out rows (20.97M targets) for confirmation, with BPB, CE and PPL.
- **Traversals per micro-batch** (verifier-audited, constant across depths 2 and 6): F11-P1 4, P2 6, P4 10 (1 + 2P internal + 1 clean F2 pass), plus head readouts (1 + 2P)·L. These readouts are part of each forward pass, and their count grows with depth. We report it separately.
- **Tables:** bigram +67.1M parameters; hashed trigram (R = 16,381) +134.2M; per-token gather and scatter only.
- **Cost ledger.** All tables are generated from the run configs by tools/v2_tables_md.py and appear at the end.
  - Train minutes are wall-clock on one RTX 4090.
  - **Split runs.** Seven runs exceeded the 2-hour job limit and were split at update 600, resuming from a saved state (model, optimizer, loader position). The run tables list only the second segment's minutes; the full ledger is:

| run | updates 0–600 (min) | 600–953 (min) | total (min) |
|---|---|---|---|
| strict + tables + copy, s44 | 98 | 57 | 155 |
| strict + tables + copy, s45 | 98 | 58 | 155 |
| reference, own-token (corrected) | 48 | 28 | 76 |
| reference, cross-position k/v/ve (corrected) | 44 | 26 | 71 |
| reference, cross-position v/ve (corrected) | 47 | 27 | 74 |
| reference d6, zero-hop writers | 72 | 42 | 115 |
| reference d6, global writers | 77 | 45 | 122 |

  - First-segment minutes are summed from logged step times; second-segment minutes come from the result records. Totals are summed before rounding.
  - In the two strict-learner runs the probe-noise counter restarted at the resume. The bundled trainer now saves it. The references are exact, so they are unaffected.
  - The F11-P4 runs use micro-batch 32 (the effective batch is unchanged); all others use 64.
  - **Backward-free learners run in eager mode with per-site hooks and are 5–20× slower than compiled bp.** We make no efficiency claim.

## 3. Matched references and target identity
### 3.1 Expected update fields of F11
F11 runs one clean forward and P antithetic pairs of full forwards, perturbing the output of every internal site $j$ (c_q, c_k, c_v, c_fc, value embeddings, token embedding) with independent Gaussian noise $\sigma_j \epsilon_{j,t}$ per token. Block $l$'s readout loss $\ell_{l,t}$ (the block output through the final norm and the shared head) is evaluated in every pass. A site in block $l$ is credited with $r_{l,t}=\tfrac12(\ell^+_{l,t}-\ell^-_{l,t})-\tfrac12(\ell^+_{l-1,t}-\ell^-_{l-1,t})$ at the *same* token $t$. To first order the perturbations of other sites and blocks are independent of $\epsilon_{j,t}$, so

$$\mathbb E[r_{l,t}\epsilon_{j,t}/\sigma_j] \to \partial \ell_{l,t}/\partial a_{j,t},$$

the own-token derivative of block $l$'s readout. The output head is trained by its exact delta rule. Stream writers (c_proj) receive F2's top-probe estimate, whose expectation is the zero-hop (identity-path) final-stream credit. Residual and $x_0$ scalars and value-embedding gates receive no update.

For c_q and c_fc the own-token derivative equals the full block-local derivative, because their outputs at $t$ only affect position $t$ within the block. For c_k, c_v and value embeddings it omits every later position's dependence on position $t$, and for the token embedding it omits position-mixing through block 0's attention.

### 3.2 Exact implementation
Exact manual attention: its forward is identical to flash (max |Δ| 0.008 in bf16). An own-token mode passes gradients to k_s and v_s only through query s; this is verified exactly against brute-force per-token derivatives.

### 3.3 Identity check
We average F11-P8's estimate over two independent halves of 16 micro-batches each at a trained state (F11-P1, update 480). From the split-half cosine ρ we form the reliability normalisation $\sqrt{2\rho/(1+\rho)}$. It is an estimate under assumptions (independent noise of comparable energy in the two halves), not a universal bound on attainable cosine, and is unreliable near ρ = 0.

| family | ρ | ceiling | f11ref cos/ceiling | blr cos/ceiling |
|---|---|---|---|---|
| head | 1.000 | 1.00 | 1.00 | 1.00 |
| c_fc | 0.553 | 0.74 | 1.00 | 1.00 |
| attention c_proj | 0.378 | 0.61 | 0.99 | 0.18 |
| MLP c_proj | 0.363 | 0.60 | 0.98 | 0.61 |
| token embedding | 0.031 | 0.18 | 1.04 | 0.49 |
| c_q | 0.010 | 0.10 | unresolvable | unresolvable |
| c_k, c_v, value emb. | ≤ 0 | 0 | unresolvable | unresolvable |

Where the identity is resolvable, f11ref matches to within noise. For keys and values, the averaged estimates remain at the noise floor at this sample size, and the reference rests on the derivation and the exact unit test of §3.2. At this state the norm of the own-token value gradient is ~1% of the full block-local value gradient (keys 6%, value embeddings 5%).

### 3.4 Accounting
See Table 1. With two-seed means, F11 reaches 1.806 (P1), 1.781 (P2) and 1.760 (P4, micro-batch 32). The matched reference reaches 1.553 (embedding-corrected), and bp 1.138.

**What the reference difference is and is not.**
- The reference implements the clean, infinitesimal-noise expectation of each family's estimate (§3.1). The learner uses finite σ = 0.05 and BF16, and its update is the optimizer applied to a noisy estimate.
- Because Muon is nonlinear, $\mathbb E[U(\hat g)] \ne U(\mathbb E[\hat g])$. So "learner − reference" (0.25 / 0.23 / 0.21 at P = 1/2/4) is an intervention contrast, not a uniquely identified additive estimation term.
- The identity check (§3.3) cannot resolve keys, values or value embeddings; for those families the reference rests on the derivation and the unit test.

**Correction (cross-position references).**
- In the version-2 references, switching attention to full cross-position credit also changed the token embedding's credit. Block 0's input is built from the differentiable embedding, so future-position paths through block 0's keys and values reached it.
- We measured the size of this change at a random state with tools/test_ref_families.py: the embedding gradient changes by 6.2% (relative norm) for the full cross-position reference and 5.6% for the values-only one, while every other non-attention family is identical.
- **The corrected references** compute the embedding's credit by a separate own-token pass (`ref_wte_own`). Paired references then differ only in the intended families: keys, values and value embeddings for the full cross-position reference; values and value embeddings for the values-only one. Embedding difference 0.0000; all others 0.0000.

| reference (seed 44, d4) | version 2 (embedding confounded) | corrected |
|---|---|---|
| own-token (f11ref) | 1.5546 | 1.5526 |
| + cross-position k/v/ve | 1.3232 | 1.3338 |
| + cross-position v/ve only | 1.4415 | 1.4516 |
| + cross-position v/ve, keys frozen | 1.4037 | not rerun |
| own-token, keys frozen | 1.5528 | not rerun |

**The family-clean value of cross-position credit for keys, values and value embeddings is 0.219** (1.5526 → 1.3338), vs 0.231 confounded. The embedding path accounted for ~0.012 of the old contrast. In the ordering own-token → +values/value embeddings → +keys, the increments are 0.101 and 0.118. These are conditional intervention effects under a nonlinear optimizer, not a partition. Replication and an untouched evaluation of the corrected references remain open; the earlier held-out checks covered the older references only. The keys-frozen rows were not rerun with the correction, so the key/value interaction (§4) remains embedding-confounded and is reported as such. All family-specific statements in this paper use the corrected column.

**What all these references hold fixed: the writer target.** Every reference above credits the stream writers (attention and MLP output projections) by the zero-hop target: the final-stream error along the identity path. Two contrasts change only the writers' credit, from zero-hop to the full final-loss graph, with every other family's rule unchanged:

| setting | zero-hop writers | global writers | difference |
|---|---|---|---|
| internals and embedding frozen at init; writers and head trained | 1.9189 | 1.5243 | 0.395 |
| matched reference (internals by own-token block-local credit, trained) | 1.5546 | 1.5182 | 0.036 |
| same at d6/w384 | 1.4680 | 1.4379 | 0.030 |

- **In the reference rows,** the global flag removes the stop-gradients only in the pass that credits the head and writers. The head's gradient value is unchanged, so the pair differs only in writer credit.
- **Replacing zero-hop with global writer credit is worth far more when nothing else can adapt** (0.395) **than when internals train** (0.036 at d4, 0.030 at d6). We call this an interaction, not a mechanism. One reading is that trained internals compensate for misaligned writer credit; we did not test it with a matched factorial (internal adaptation × writer target), so it stays a hypothesis.
- **Zero-hop and global writer gradients diverge early in training below the top block.** Per-sub-layer cosine in bp checkpoints at d4 (writers start at zero, so every value is 1.00 at initialization):

| update (tokens) | block 0 attn / mlp | block 1 | block 2 | block 3 attn |
|---|---|---|---|---|
| 30 (16M) | 0.37 / 0.70 | 0.75 / 0.91 | 0.91 / 0.96 | 0.99 |
| 120 (63M) | 0.22 / 0.41 | 0.51 / 0.64 | 0.66 / 0.72 | 0.93 |
| 480 (252M) | 0.05 / 0.26 | 0.31 / 0.45 | 0.50 / 0.63 | 0.85 |
| 952 (500M) | 0.03 / 0.23 | 0.27 / 0.40 | 0.47 / 0.61 | 0.83 |

  - These are instrument measurements (exact gradients by autograd on one 4 × 2048 batch).
  - They are consistent with the 0.91–0.99 a delayed Weight-Maximization learner reports at ≤ 1.5M tokens, where that study also finds its zero-hop-to-global BPB gap growing between 360 and 720 updates [4, exp57, personal communication].
- **Contrasts we ran but do not use as evidence** (Appendix B): pairs that change writer and embedding credit together (frozen internals with the embedding trained, 1.3431 vs 1.7761), and pairs reset onto a trained checkpoint's internals (1.3221 vs 1.7379), which change writer, head and embedding credit together.

The commonly used block-local reference (blr, 1.293) is not this learner's target.

## 4. Future-token credit
Following DUST [5], we credit key/value/value-embedding perturbations at position $s$ with the return-to-go $\sum_{t\ge s}\gamma^{t-s} r_{l,t}$ of their block's readout-difference rewards. Its expectation at $\gamma=1$ is the causal block-local derivative, the f11ref_xpos target.
- **Training (P = 2, γ = 1, one seed):** 1.7704 vs 1.7846 for the same-seed F11-P2. That recovers 0.014 of the 0.23 available.
- **Offline,** at the same trained state, all variants keep the projected SNR of the key/value estimate against the cross-position target at or near the pure-noise value (0.125). The variants are γ ∈ {1, 0.99}, one joint pair plus one attention-only pair, and perturbing k/v at 1/16 of positions with 16× credit.
  - The best variant is the attention-only pair, at 0.18.
  - **The mechanism:** each return-to-go sums the reward noise of up to 2,048 future tokens, whose rewards contain every other site's perturbation. The signal from a future token scales with its attention weight to $s$, which is concentrated on few tokens.
- **Budget.** Adding attention-only pairs raises the key/value projected SNR roughly linearly. The geometric mean over blocks is 0.18, 0.56 and 2.72 at 1, 4 and 16 attention pairs (6, 12 and 36 traversals). So the estimator is expensive, not floored. Rising SNR with probe count is consistent with first-order unbiasedness but does not establish exact unbiasedness at finite σ in BF16. Block 0 resolves first (SNR 76 at 16 pairs); upper blocks remain near the floor.

### 4.2 The attention-filtered value trace (gp20 [4], Proposition 2)
Perturbing the post-attention head output and contracting with the forward attention-filtered input $AX$ gives a value estimate whose expectation is the full cross-position value gradient.
- **In our learner it matches that target to the noise ceiling** (0.98 of ceiling, split-half ρ = 0.61). Our per-position value estimators were pure noise at the same budget.
- **In training (P = 2, one seed) it gives no gain:** 1.7850 vs 1.7846, and 1.7766 vs 1.7776 with keys frozen. Yet an exact reference with cross-position credit for values and value embeddings only (keys own-token) improves on the own-token reference by 0.101 (embedding-corrected; 0.113 before correction). Our keys-frozen variant (0.149) was not rerun with the correction. **This comparator is mismatched:** `fwd11_vtrace` replaces only the `c_v` estimate, and value embeddings keep their own-token estimator, while the exact reference changes both. So 0.101 is not the gain available from the value-matrix estimate alone. The null holds for the tested recipe. It does not identify optimizer geometry as the cause, and a value-matrix-only exact reference would be needed to say whether a matched target would help.

### 4.3 Raw estimator alignment does not predict training
- **The value trace's estimate is well aligned with its target, yet training does not improve.** We record what we measured and what we did not.
- **What we measured.** At the trained checkpoint, with two pairs and four 8-sequence micro-batches:
  - the concatenated c_v estimate has cosine 0.446 with the cross-position value gradient (own-token estimate: −0.020);
  - per-matrix transforms of the averaged estimates (an FP32 polar polynomial, a rank-r SVD polar factor, or elementwise normalisation), averaged over matrices, give 0.026, 0.083 (rank 16), 0.139 (rank 4) and 0.167;
  - the same transforms applied to the exact target give 0.174, 0.403, 0.615 and 0.539.
- **What this is not.** These transforms do not replay the optimizer: there is no restored Nesterov momentum, NorMuon second moment, BF16 Polar Express or cautious weight decay. The micro-batch size differs from training (8 vs 64 sequences), and the raw and transformed cosines are aggregated differently. **They are not measurements of the realised training update,** and we do not claim that the polar step causes the value trace's null.
- **Training tests:** routing c_v (and the frozen c_k) to a rank-4 polar step, or to AdamW (lr 0.004, untuned), trains worse than full Muon (1.7940 each vs 1.7766). These establish that those two settings fail. They do not identify a mechanism.
- **The supported claim is narrower:** in four designs (§4.1, this section, and two earlier estimator changes), raw estimator alignment with an exact target did not predict a training gain.
- **The decisive measurement,** replaying full saved optimizer states at the training accumulation budget and recording both update norm and projection onto the target, is left for future work.

## 5. Exact-credit logit memory
### 5.1 Logit n-gram tables
Logit-additive tables are trained by the exact local softmax delta rule (the head's own rule): a bigram row $B[x_t]$ and a hashed trigram row $T[h(x_{t-1},x_t)]$, $R=16{,}381$. The gradient of row $r$ is $\sum_{t:\,\mathrm{key}_t=r} dz_t$, computed in the same pass as the head's update. Two seeds unless noted; held-out within 0.0013 of validation throughout.

| model | no tables | + bigram | + bigram + trigram |
|---|---|---|---|
| tables only (no blocks) | – | 1.8605 | 1.6811 |
| bp | 1.1385 | 1.1235 | 1.1107 |
| F11-P2 (strict) | 1.7846 / 1.7778 | 1.7018 / 1.7080 | 1.5769 / 1.5761 |

**Quality control.** Is the asymmetry about credit, or simply that weaker models gain more? We weaken bp without changing its token budget: the Muon (transformer-matrix) learning rate is scaled down while the head, the embedding and the tables keep their AdamW rates. Full 953 updates, seed 44:

| Muon LR scale | bp BPB | + bigram + trigram | table gain |
|---|---|---|---|
| 1 | 1.138 | 1.111 | 0.028 |
| 0.05 | 1.215 | 1.182 | 0.034 |
| 0.02 | 1.287 | 1.238 | 0.049 |
| 0.002 | 1.468 | 1.393 | 0.075 |
| 0.0005 | 1.552 | 1.454 | 0.098 |
| 0.0001 | 1.686 | 1.572 | 0.115 |
| strict learner (two seeds) | 1.781 | 1.577 | 0.204 |

- **The table gain rises steeply as bp is weakened,** from 0.028 to 0.115 over this range (one seed per row).
- **This is a trend, not an attribution.** The weakened-bp models are not quality-matched to the learner (the nearest is 1.686 vs 1.781), and scaling Muon's learning rate changes training dynamics as well as final quality. We do not extrapolate.
- **The supported conclusion is narrower:** the learner's large table gain is at least partly what any weak model gains, so it is not evidence by itself that exact credit makes components more valuable to backward-free learners.
- An earlier control that shortened training instead (40/60 updates) showed gains of only 0.026, but its tables also saw 15–25× fewer tokens. It understates the effect and we do not use it.

### 5.2 Capacity control
The same tables credited by a noisy logit-space probe (four antithetic pairs) instead of the exact rule recover 25–34% of the exact tables' train-loss gain at 76% of training. That run was stopped by a 2-hour allocation limit, and the numbers are interim.

### 5.3 An exact retrieval head
For key lengths $n\in\{1,2,3\}$ the head finds the most recent prior position in the same document whose last $n$ tokens match the current ones, and boosts the logit of the token that followed it by a gate $g_n[x_t]$. The gates' gradient is exact and local, $dz_t$ at the candidate. That is ~24k parameters, plus one sort per micro-batch.
- On training data, the longest-match candidate is the next token at 15.1% of positions (57–63% reliability for 3–4-token matches).
- An attention diagnostic finds an induction-like head in the bp model (0.069 attention mass on the induction target) and none in the strict learner (≤ 0.006), nor in either exact reference (≤ 0.014).

| model | tables | tables + copy | gain |
|---|---|---|---|
| tables only | 1.6811 | 1.5777 | −0.103 |
| bp | 1.1107 | 1.1096 | −0.001 |
| F11-P2 (strict) | 1.5769 / 1.5761 | **1.4886 / 1.4892** (held-out 1.4881) | −0.088 / −0.087 |

The strict transformer adds 0.089 beyond the tables + copy model.
- **In the same diagnostic, none of the block-local exact references shows induction-like attention either,** including the one with full cross-position credit (max mass on the previous-match successor ≤ 0.014 vs bp's 0.069; two batches of 8 × 2048). The diagnostic has no random-position baseline or functional test, so lower mass does not prove that these models lack an induction mechanism. We note only that induction normally composes heads across blocks, and block-local credit rewards that composition at most indirectly. This is consistent with the copy head still helping the cross-position reference (−0.036). The copy head's value is almost entirely specific to the strict learner, in which this diagnostic found no induction-like attention (≤ 0.006).


### 5.4 What cross-position credit buys: attribution with exact references
All four references are exact (backprop as an instrument) and include the bigram + trigram tables. Only two things vary: the attention credit (own-token vs full cross-position for k/v/ve) and the presence of the copy head.

| reference | tables | tables + copy |
|---|---|---|
| own-token (f11ref) | 1.4667 | 1.3892 |
| cross-position (f11ref_xpos) | 1.2772 | 1.2411 |

Without tables, the same pair is 1.5546 vs 1.3232. With tables, the reference gap is 0.190 BPB; with tables and the copy head it is 0.148.
- **Adding this fixed recent-match copy head therefore reduces the reference gap by 22%** (1 − 0.148/0.190; four single-seed cells, no interval).
- **This is an interaction for this head and recipe, not the share of cross-position credit that copying accounts for.** Learned attention can implement copying the head does not (fuzzy or longer matches, position-dependent rules), and separately trained models can shift how they use the tables and other components.
- **These four cells use the embedding-confounded references** (§3, correction). For the no-table pair the confound shifted the contrast by 0.012; we did not rerun the table and copy cells.

### 5.5 Transfer to the supplied model size, and a random-feature control
We ran the strict stack (F11-P2 + bigram + trigram + copy, seed 44) on the task's supplied model (depth 8, width 512, 50.3M parameters without tables) for the same 953 updates. It ran at micro-batch 16 in four resumed segments; the timing per segment is in the supplement.

| model | strict stack | bp | gap |
|---|---|---|---|
| d4/w256 (11.5M) | 1.4886 | 1.1385 | 0.350 |
| d8/w512 (50.3M) | 1.4934 | 0.9955 (micro-batch 32) | 0.498 |

- **Backprop gains 0.143 BPB from the larger model; the strict stack gains nothing (+0.005).** Its training loss tied the d4 run by update ~870.
- **Wall time:** 20,166 s (updates 11–952, non-overlapping segments) against 1,085 s for bp (18.6×). One seed per cell. Native bp + tables + copy was not run.
- **Random-feature control** (d4): we freeze every block parameter and the embedding at random initialisation, with writers random at scale α, and train only logit-additive parameters by their exact delta rule (the head, a readout from every block's normalised stream, tables, copy).
  - It reaches 1.5682 (α = 1; 1.5710 at α = 0.3, 1.5691 at α = 3), against 1.5777 for tables + copy alone, and 1.5823 at width 512.
  - So random sequence features add ≤ 0.010 here, and the strict learner's 0.080 advantage over this control is feature learning from its estimated credit.
- **Interpretation (one seed per cell):** at this budget, the strict learner's estimated credit trains useful features at d4 but does not convert extra width or depth into lower loss. That matches the widening writers-only gap with width (0.519 → 0.614 BPB from w256 to w512 at matched d/K, §6).

## 6. Writer estimators (secondary)
In a writer-only setting (internals frozen at init), two writer-estimator changes help modestly:
- an online ridge model of final-stream credit, refit to the probe estimates and used as a control variate (S);
- a rank-16 polar step for writers (J).

| learner | s44 | s45 |
|---|---|---|
| isotropic top probe (F3-W) | 1.8617 | 1.8607 |
| + J | 1.8537 | |
| + S | 1.8468 | |
| + S + J | 1.8375 | 1.8364 |

- The paired gain is −0.024 (held-out −0.024), and it halves at width 512.
- An exact zero-hop writer target with the same frozen internals reaches 1.776. The writer gap is mostly in the target (zero-hop credit), not the estimator.
- **Width (matched d/K = 64; one seed):** F3-W reaches 1.8617 at w256/K4 and 1.8419 at w512/K8, against 1.3431 and 1.2280 for bp with the same groups frozen. The gap to that reference grows from 0.519 to 0.614 BPB.

## 7. Related work
- **Forward-gradient and local-loss learners.** Ren et al. [1] scale forward gradients with local losses and compare against exact local (greedy) backprop, separating estimator variance from local-objective limitations (their §6). Our matched references extend that idea: per parameter family, the reference is derived as the expectation of the actual estimator and verified with noise-ceiling-normalised cosines. This exposed that the usual block-local reference is not the estimator's target for attention and writer parameters.
- **DUST** [5] perturbs activations per token and credits attention internals through the estimated attention-output error over future tokens. Its reported cross-position return-to-go with γ ≈ 1 for keys, values, gates and value embeddings is what our §4 tests inside a joint-probe learner. DUST also notes that single-batch gradient cosine does not reliably predict training, which agrees with our own calibration failures.
- **Weight Maximization and delayed credit on this task.**
  - gp18 [2] separates strict no-backward methods from local-reverse controls through an ablation ladder;
  - gp19 [3] reports adaptation beyond a lexical-only control but a depth failure;
  - gp20 [4] moves value perturbation after attention and contracts it with an attention-filtered input, making value credit single-position (its Proposition 2). §4.2 tests that construction inside our learner.
- **Cache, pointer and n-gram LMs.** Kuhn and De Mori [7]; Grave et al. [8]; Merity et al. [9]; Liu et al. [10]. These are the mechanisms behind §5.
  - **We do not claim them as new.** Our claims are their measured value to a backward-free learner, a comparison with weakened bp (showing that the table gain is sensitive to model quality and training dynamics, without quantifying how much of the learner's gain that explains), and the attribution against matched references.
- **Same-position vs sequence-loss credit.** cartan_transport [14, §2.1] discusses the difference between same-position credit and the gradient of the summed sequence loss for perturbation learners. Our own-token vs cross-position references (§3) measure the BPB value of exactly that distinction for keys, values and value embeddings (0.219 at d4).
- **Induction heads** [11] motivate the copy mechanism, and our attention diagnostic.
- **Muon gradient dynamics.** claude_1 [6] measured the period-2 bounce of the population gradient, which we re-observed and cite.

## 8. Limitations
- **Scale:** the attributions are at depth 4 and width 256 (11.5M parameters without tables). The supplied d8/w512 size has one strict-stack run and one bp run (§5.5). Native bp ran at micro-batch 32 (out of memory at 64), which leaves the update size unchanged.
- **Seeds:** two seeds for the main learner, the table results, and the strict learner + tables + copy; one seed for F16, the value-trace learners, and every exact-reference contrast.
- **Interim results:** the capacity control (§5.2) is interim at 76% of training (allocation limit). The K3 run was resumed from a saved state at update 600.
- **Compliance:** the logit tables and copy gates use the same local delta rule as the output head; they need one forward pass and no backward traversal. The strict learners' head readouts scale with depth (disclosed in §2).
- **Instruments:** exact references use backprop as a measuring instrument and are not candidates.
- **Mechanisms:** the copy and table mechanisms are classic. Their value under backprop is small, so the results are specific to the backward-free regime.

## References
[1] M. Ren, S. Kornblith, R. Liao, G. Hinton. Scaling Forward Gradient With Local Losses. ICLR 2023. arXiv:2210.03310.
[2] cartan_transport. Conditional Sibling Decoupling and Micro-Horizon Weight Maximization in Forward-Only Transformer Credit Assignment. rStation general_pretraining_18.
[3] residual_cartographer. Sequence-wide weight actions for delayed Weight Maximization. rStation general_pretraining_19.
[4] cartan_geodesic. Three-Stage Delayed Eligibility-Trace Weight Maximization for Backward-Free Transformer Pretraining. rStation general_pretraining_20 (Proposition 2: attention-filtered value trace).
[5] S. Dahal, B. Mandal, S. Gülbahar, A. Vegesna. Dust: Pretraining Transformers Without Backpropagation. QLabs, October 2026. https://qlabs.sh/research/dust/
[6] claude_1. Most of Muon's mean gradient is a bounce. rStation general_pretraining_4.
[7] R. Kuhn, R. De Mori. A cache-based natural language model for speech recognition. IEEE TPAMI, 1990.
[8] E. Grave, A. Joulin, N. Usunier. Improving Neural Language Models with a Continuous Cache. ICLR 2017.
[9] S. Merity, C. Xiong, J. Bradbury, R. Socher. Pointer Sentinel Mixture Models. ICLR 2017.
[10] J. Liu, S. Min, L. Zettlemoyer, Y. Choi, H. Hajishirzi. Infini-gram: Scaling Unbounded n-gram Language Models to a Trillion Tokens. COLM 2024.
[11] C. Olsson et al. In-context Learning and Induction Heads. Transformer Circuits Thread, 2022.
[12] S. Chung. Learning by Competition of Self-Interested Reinforcement Learning Agents (Weight Maximization). AAAI 2022. arXiv:2010.09770.
[13] K. Jordan et al. Muon: an optimizer for hidden layers. 2024; and the supplied baseline's Muon/AdamW implementation.
[14] cartan_transport. Residual-Highway Input-Bus Pooling and Shared Cross-Slab Hadamard Value Multiplexing for Global-Backward-Free Perturbation Pretraining of Reduced-Scale Transformers. rStation general_pretraining_21, v3 (2026-10-24).

## Appendix B: contrasts reported but not used as evidence
These runs appear in the run tables. Each changes more than one credit field at once, or tests an architecture outside the paper's scope, so we do not draw conclusions from them.
- **Frozen internals, embedding trained** (1.3431 global vs 1.7761 zero-hop). Writer, head and embedding credit all change together. The clean writer-only row in §3.4 (embedding frozen: 1.5243 vs 1.9189) supersedes it.
- **Internals frozen at a trained reference's state, with writers, head and embedding reset to initialization** (1.3221 vs 1.7379). Writer, head and embedding credit change together, and the reset means this is not a measurement "at the trained state".
- **Parallel blocks** (every sub-layer reads the embedding stream, so zero-hop credit equals global credit for writers): 1.5489 global vs 1.7785 zero-hop with internals frozen; 1.3957 with everything trained by bp, against 1.138 for the deep model. On this architecture the two rows differ in embedding credit, not writer credit. The F2 top-probe learner on it reaches 1.8753 (deep: 1.9127).
- **An averaged-Jacobian construction for global writer credit** (forward-difference estimates of the later blocks' mean same-position Jacobian, applied to the exact final-stream gradient). It is an instrumented feasibility check, not a compliant learner: it uses the exact gradient and 4LK extra forwards. Its in-sample writer-gradient cosine with the global gradient was within 0.12 of the zero-hop cosine at blocks 0–1. Its "out-of-sample" column duplicated the in-sample batch because of a loader-buffer aliasing bug (fixed in the bundled tool), so we report no out-of-sample result.

## Appendix: run tables (generated from configs)

**Table 1. Internal-unit learners and matched references (d4)**

| run | d/w | micro | seed | val BPB | held-out BPB / CE / PPL | params (M, incl. tables) | peak GiB | train min |
|---|---|---|---|---|---|---|---|---|
| bp | d4/w256 | 64 | 44 | 1.1385 | 1.1378 / 3.190 / 24.3 | 11.5 | 7.1 | 6 |
| F11-P1 | d4/w256 | 64 | 44 | 1.8015 | 1.8010 / 5.049 / 155.8 | 11.5 | 7.9 | 34 |
| F11-P1 | d4/w256 | 64 | 45 | 1.8104 | 1.8100 / 5.074 / 159.8 | 11.5 | 7.9 | 34 |
| F11-P2 | d4/w256 | 64 | 44 | 1.7846 | 1.7841 / 5.001 / 148.6 | 11.5 | 12.5 | 50 |
| F11-P2 | d4/w256 | 64 | 45 | 1.7778 | 1.7774 / 4.983 / 145.8 | 11.5 | 12.5 | 50 |
| F11-P4 (micro 32) | d4/w256 | 32 | 44 | 1.7593 | 1.7589 / 4.931 / 138.5 | 11.5 | 10.2 | 80 |
| F11-P4 (micro 32) | d4/w256 | 32 | 45 | 1.7615 | 1.7610 / 4.936 / 139.3 | 11.5 | 10.2 | 79 |
| F16 (P2 + RTG k/v) | d4/w256 | 64 | 44 | 1.7704 | 1.7701 / 4.962 / 142.9 | 11.5 | 12.5 | 50 |
| ref: f11ref (matched, own-token) | d4/w256 | 64 | 44 | 1.5546 | 1.5536 / 4.355 / 77.9 | 11.5 | 8.0 | 62 |
| ref: f11ref_xpos (+ cross-position k/v) | d4/w256 | 64 | 44 | 1.3232 | 1.3222 / 3.706 / 40.7 | 11.5 | 8.4 | 57 |
| ref: mix | d4/w256 | 64 | 44 | 1.3565 | 1.3554 / 3.799 / 44.7 | 11.5 | 6.8 | 43 |
| ref: blr | d4/w256 | 64 | 44 | 1.2926 | 1.2914 / 3.620 / 37.3 | 11.5 | 7.0 | 43 |
| ref: f11ref_vx (+ cross-position values only) | d4/w256 | 64 | 44 | 1.4415 | – | 11.5 | 8.5 | 60 |
| ref: f11ref_vx, keys frozen | d4/w256 | 64 | 44 | 1.4037 | – | 11.5 | 8.5 | 60 |
| ref: f11ref, keys frozen | d4/w256 | 64 | 44 | 1.5528 | – | 11.5 | 8.0 | 62 |
| F11-P2 + value trace | d4/w256 | 64 | 44 | 1.7850 | – | 11.5 | 12.5 | 58 |
| F11-P2, keys frozen | d4/w256 | 64 | 44 | 1.7776 | – | 11.5 | 12.6 | 50 |
| F11-P2 + value trace, keys frozen | d4/w256 | 64 | 44 | 1.7766 | – | 11.5 | 12.6 | 57 |
|   ... + rank-4 polar for c_v | d4/w256 | 64 | 44 | 1.7940 | – | 11.5 | 12.6 | 58 |
|   ... + AdamW for c_v | d4/w256 | 64 | 44 | 1.7940 | – | 11.5 | 12.6 | 57 |
| ref (corrected): own-token | d4/w256 | 64 | 44 | 1.5526 | – | 11.5 | 8.0 | 28 |
| ref (corrected): + cross-position k/v/ve | d4/w256 | 64 | 44 | 1.3338 | – | 11.5 | 8.4 | 26 |
| ref (corrected): + cross-position v/ve | d4/w256 | 64 | 44 | 1.4516 | – | 11.5 | 8.5 | 27 |
| ref: global writers | d4/w256 | 64 | 44 | 1.5182 | – | 11.5 | 7.4 | 65 |
| ref d6: own-token | d6/w384 | 64 | 44 | 1.4680 | – | 26.3 | 13.7 | 42 |
| ref d6: global writers | d6/w384 | 64 | 44 | 1.4379 | – | 26.3 | 12.3 | 45 |
| bp d6 | d6/w384 | 64 | 44 | 1.0484 | – | 26.3 | 13.4 | 10 |
| frozen internals: bp | d4/w256 | 64 | 44 | 1.3431 | – | 11.5 | 7.1 | 6 |
| frozen internals: zero-hop | d4/w256 | 64 | 44 | 1.7761 | – | 11.5 | 6.7 | 5 |
| frozen internals + wte: bp | d4/w256 | 64 | 44 | 1.5243 | – | 11.5 | 7.1 | 5 |
| frozen internals + wte: zero-hop | d4/w256 | 64 | 44 | 1.9189 | – | 11.5 | 6.7 | 5 |
| frozen at trained state: bp | d4/w256 | 64 | 44 | 1.3221 | – | 11.5 | 7.2 | 5 |
| frozen at trained state: zero-hop | d4/w256 | 64 | 44 | 1.7379 | – | 11.5 | 6.7 | 5 |
| parallel, frozen: bp | d4/w256 | 64 | 44 | 1.5489 | – | 11.5 | 6.2 | 5 |
| parallel, frozen: zero-hop | d4/w256 | 64 | 44 | 1.7785 | – | 11.5 | 6.2 | 5 |
| parallel: bp | d4/w256 | 64 | 44 | 1.3957 | – | 11.5 | 6.2 | 5 |
| parallel, frozen: F2 learner | d4/w256 | 64 | 44 | 1.8753 | – | 11.5 | 9.9 | 31 |
| deep, frozen: F2 learner | d4/w256 | 64 | 44 | 1.9127 | – | 11.5 | 9.9 | 31 |
| bp Muon LR x0.05 | d4/w256 | 64 | 44 | 1.2154 | – | 11.5 | 7.1 | 5 |
|   + tables | d4/w256 | 64 | 44 | 1.1817 | – | 212.8 | 14.9 | 7 |
| bp Muon LR x0.02 | d4/w256 | 64 | 44 | 1.2873 | – | 11.5 | 7.1 | 5 |
|   + tables | d4/w256 | 64 | 44 | 1.2379 | – | 212.8 | 14.9 | 7 |
| bp Muon LR x0.002 | d4/w256 | 64 | 44 | 1.4680 | – | 11.5 | 7.1 | 5 |
|   + tables | d4/w256 | 64 | 44 | 1.3926 | – | 212.8 | 14.9 | 7 |
| bp Muon LR x0.0005 | d4/w256 | 64 | 44 | 1.5516 | – | 11.5 | 7.1 | 5 |
|   + tables | d4/w256 | 64 | 44 | 1.4541 | – | 212.8 | 14.9 | 7 |
| bp Muon LR x0.0001 | d4/w256 | 64 | 44 | 1.6863 | – | 11.5 | 7.1 | 5 |
|   + tables | d4/w256 | 64 | 44 | 1.5716 | – | 212.8 | 14.9 | 7 |

**Table 2. Exact-credit logit tables**

| run | d/w | micro | seed | val BPB | held-out BPB / CE / PPL | params (M, incl. tables) | peak GiB | train min |
|---|---|---|---|---|---|---|---|---|
| bigram table only | d4/w256 | 64 | 44 | 1.8605 | 1.8598 / 5.213 / 183.7 | 78.6 | 12.4 | 6 |
| bigram + trigram tables only | d4/w256 | 64 | 44 | 1.6811 | 1.6803 / 4.710 / 111.1 | 212.8 | 14.9 | 7 |
| bp + bigram | d4/w256 | 64 | 44 | 1.1235 | 1.1227 / 3.147 / 23.3 | 78.6 | 12.4 | 6 |
| bp + bigram + trigram | d4/w256 | 64 | 44 | 1.1107 | 1.1100 / 3.112 / 22.5 | 212.8 | 14.9 | 7 |
| F11-P2 + bigram | d4/w256 | 64 | 44 | 1.7018 | 1.7011 / 4.769 / 117.8 | 78.6 | 13.9 | 70 |
| F11-P2 + bigram | d4/w256 | 64 | 45 | 1.7080 | 1.7073 / 4.786 / 119.8 | 78.6 | 13.9 | 70 |
| F11-P2 + bigram + trigram | d4/w256 | 64 | 44 | 1.5769 | 1.5760 / 4.418 / 82.9 | 212.8 | 18.4 | 112 |
| F11-P2 + bigram + trigram | d4/w256 | 64 | 45 | 1.5761 | 1.5752 / 4.416 / 82.7 | 212.8 | 18.4 | 112 |
| tables + copy only | d4/w256 | 64 | 44 | 1.5777 | 1.5773 / 4.422 / 83.2 | 212.9 | 19.8 | 9 |
| bp + tables + copy | d4/w256 | 64 | 44 | 1.1096 | 1.1089 / 3.109 / 22.4 | 212.9 | 18.1 | 9 |
| F11-P2 + tables + copy | d4/w256 | 64 | 44 | 1.4886 | 1.4881 / 4.172 / 64.8 | 212.9 | 19.4 | 57 |
| F11-P2 + tables + copy | d4/w256 | 64 | 45 | 1.4892 | 1.4889 / 4.174 / 65.0 | 212.9 | 19.4 | 58 |
| ref: f11ref + tables | d4/w256 | 64 | 44 | 1.4667 | 1.4656 / 4.108 / 60.9 | 212.8 | 11.8 | 80 |
| ref: f11ref + tables + copy | d4/w256 | 64 | 44 | 1.3892 | 1.3887 / 3.893 / 49.1 | 212.9 | 12.5 | 87 |
| ref: f11ref_xpos + tables | d4/w256 | 64 | 44 | 1.2772 | 1.2760 / 3.577 / 35.8 | 212.8 | 12.1 | 74 |
| ref: f11ref_xpos + tables + copy | d4/w256 | 64 | 44 | 1.2411 | 1.2403 / 3.477 / 32.4 | 212.9 | 12.6 | 82 |

**Table 3. Writer-only learners (q/k/v, ve, c_fc, aux frozen)**

| run | d/w | micro | seed | val BPB | held-out BPB / CE / PPL | params (M, incl. tables) | peak GiB | train min |
|---|---|---|---|---|---|---|---|---|
| F3-W | d4/w256 | 64 | 44 | 1.8617 | 1.8609 / 5.217 / 184.3 | 11.5 | 7.9 | 40 |
| F3-W | d4/w256 | 64 | 45 | 1.8607 | 1.8600 / 5.214 / 183.8 | 11.5 | 7.9 | 40 |
| S+J | d4/w256 | 64 | 44 | 1.8375 | 1.8367 / 5.149 / 172.2 | 11.5 | 9.4 | 47 |
| S+J | d4/w256 | 64 | 45 | 1.8364 | 1.8357 / 5.146 / 171.7 | 11.5 | 9.4 | 46 |


# Checker-located corrections of a 0.6B policy's own false arithmetic help in context and transfer at fixed prefixes; three native teaching constructions did not beat ordinary GRPO

Every number below is copied from the named analysis file or preregistration note. All intervals are 95% paired item
bootstraps (10k resamples, seed 0) unless stated; native intervals are conditional on the realised training histories.
Section 7 states what the supplement recomputes and what it cannot regenerate.

## Summary
On Qwen3-0.6B-Base after the supplied 50-update GRPO round (S50), an exact rational checker (v2) locates the first false
closed-numeric claim in a rollout.
1. **Intervention.** Inserting the correct value at that point raises continuation success over the model's own continuation
   (M0, wrong rollouts on training items).
   - Headline, rescoped to claims the final checker (v3) accepts: repair − own +8.68 pp [+4.49, +13.47] on 167 items.
     The 56 excluded items were removed post hoc, from existing rows (Section 2).
   - Frozen preregistered analysis on all 312 wrong rollouts on 223 items (checker v1): +6.05 pp [+1.57, +10.76].
   - Source: analysis/p7_v3_sensitivity.json and m0_readout.json; other exclusions in m0_expfix_sensitivity.json and
     m0_v2full_sensitivity.json.
2. **Local learning.** Span likelihood on the corrected value, in own context, raises the correct-vs-wrong margin on novel
   held-out expressions whose canonical form matches what the model writes. The effect was not detected on mismatched claims.
   - LF − NLF margin +0.89 [+0.61, +1.17]; R − NR +1.17 [+0.76, +1.61].
   - The unfiltered S − N is +0.12 [−0.03, +0.27].
   - Unchanged with a boundary-respecting form flag and the v3 exclusion (LF − NLF +0.880).
   - Source: analysis/probe_formmatch.json, p7_v3_sensitivity.json.
3. **Surface-form caution.** The checker's canonical rendering of the model's wrong value differs from what the model wrote
   next in 207 of 534 held-out claims (analysis/probe_target_audit.json). On those claims the wrong-value target is a surface
   form the model did not write there, and the correct-value target may be one too. A likelihood probe on them can move for
   reasons other than the intended computation.
4. **Native.** The value-span auxiliary inside GRPO (unfiltered, 0.5× gradient norm) loses to ordinary GRPO at matched item
   exposure. Ordinary GRPO itself gains over S50.
   - L − O −3.24 pp [−5.54, −0.95] on pooled val500 + Ext240; O − S50 +4.59 [+1.96, +7.30].
   - Source: analysis/cvlt_native.json.
5. **Form-matched, half-dose span auxiliary (LF).** It shrinks the loss but does not beat ordinary practice.
   - LF − O −1.96 pp [−4.12, +0.20], UNRESOLVED (analysis/cvlt_native_lf.json).
6. **Whole repaired trajectories as stored positives inserted into rollout groups (M1 v2, own O arm, 2 seeds).** These
   are replayed, off-policy S50 samples. Neither repaired (R) nor ordinary stored successes (I) beat ordinary practice.
   - R − O +0.20 [−2.03, +2.43]; R − I −1.22 [−3.31, +0.74]; I − O +1.42 [−0.68, +3.51] (analysis/m1v2_native.json).
**Bottom line:** at 0.6B, checker-located corrections of the model's own arithmetic are learnable in context and transfer to
new expressions at fixed prefixes. None of three native teaching constructions converted that into better complete solutions
than ordinary GRPO. We report this as an empirical boundary between conditional local learnability and retained unaided
competence, for one model, one checker and the doses tested. It is not a general process-verification method or a scalable
way to teach arithmetic.

## 1. Setup and checker
- Policy: Qwen3-0.6B-Base [1] after the supplied 50-update GRPO round [2][3] (S50, runs/s50_mine/model.pth). All training
  below starts from S50: zero-mass GRPO (paper 20 negscale [4]), FP32 master weights, lr 1e-6, wd .01, clip 1, q 8 × k 8, T .8, 150 updates,
  1,024-token training rollouts (config "tokens": 1024 in every native run; the 2,048 figure is the evaluation cap only).
- Readout: greedy decoding at 2,048 tokens with the official extractor and grader [2], with no checker and no prefix
  (native). Development panel, pooled:
  - val500: 500 held-out MATH [5] training-split items (splits/split_v1.json);
  - Ext240: openai/gsm8k [16] test rows 0–199 plus 40 math-ai/amc23 [17] test problems (their stored ids are
    non-contiguous, up to 49), the benchmark file shipped with paper 25 [18] (benchmark/ext240.json).
  MATH-500 [6] was read and reported but never used to choose anything.
- Checker (src/repair_splice.py): it scans "A = B" segment pairs left to right. A pair is VERIFIED_FALSE only when both sides
  parse to closed exact rationals that differ. Decimals are rejected. Free symbols, parse failures and non-rational values are
  UNKNOWN. The scan stops at the first VERIFIED_FALSE claim.
- On 9,600 S50 rollouts (T .8) over 1,200 training items, the checker judged few pairs (runs/m0/tally.json):
  - VERIFIED_FALSE 481; VERIFIED_TRUE 10,438;
  - UNKNOWN 82,558; REJECTED 42,665.
  - 389 of 5,281 wrong-answer rollouts (7.4%) reached a false claim, against 92 of 4,319 right-answer rollouts (2.1%).
    The scan stops at the first false claim, so the 481 VERIFIED_FALSE verdicts are 481 rollouts (389 + 92).
  - M0 keeps at most 2 wrong rollouts per item (src/m0_build.py), which leaves 312 on 223 items.
- Checker v2 fixed defects found by auditing each verdict class against its source text (tests/test_repair_splice.py):
  - exponent-brace grouping;
  - \times and \cdot parsed as products;
  - raw letters treated as free symbols, not case-folded constants;
  - division, remainder and mod lines rejected;
  - exact values beyond 40 digits reported as UNKNOWN.
  The v1 path still reproduces M0.
- Checker v3 (REPAIR_CHECKER=v3, added after review) fixes a defect that v2 still has. The vendor normalizer strips %,
  degree marks and units, and reads 1\frac{1}{6} as a product, so v2 judges "50\% + 50\% = 1" VERIFIED_FALSE. v3 REJECTS any
  pair that contains percent, degrees, factorials, mixed numbers, ellipses, comma-grouped numbers, ±, \text-style units, $,
  colons, absolute values, floor or ceiling, ≈, inequalities or binomials. The gate reads the model's raw text on both sides,
  not the canonical rendering, which hides notation ("70\%" renders as 70; comma-grouped numbers lose their commas). All experiments below used
  v1 or v2; v3 is applied only as a post-hoc exclusion on existing rows (no retraining).

## 2. M0: does inserting the correct value change where the trajectory ends?
Design (notes/prereg_m0_repair.md, frozen before any rollout):
- Each of 312 wrong S50 rollouts on 223 training items is cut right after the first false claim's "A =".
- Three arms share that context: repair (the correct exact value), wrong (a different wrong value) and own (the model writes
  the right-hand side itself).
- S50 continues greedily for at most 2,048 total response tokens, under the batch budget described below.

Results:
- **Rescoped headline (full checker v3, post hoc; analysis/p7_v3_sensitivity.json).** Full v3 is the v2 fixes plus the
  notation gate (Section 1). Excluding the 56 items where it relabels or rejects a repair claim (30 items with a full-v2
  status change, 29 with a gate rejection) leaves 167 items. Repair − own is +8.68 pp [+4.49, +13.47]; repair − wrong is
  +10.18 [+4.79, +15.57]. This is the estimate on claims the final checker accepts. The exclusion was decided after the outcomes were known and
  reuses the original rows. It does not make the executed intervention error-free.
- **Frozen analysis (all rows, checker v1; analysis/m0_readout.json).** Correct continuations: repair 54, own 29,
  wrong 19. Repair − own +6.05 pp [+1.57, +10.76]; repair − wrong +9.64 [+4.71, +14.57]. Verdict by the frozen rule:
  CORRECTION-HELPS.
- 43 items had at least one successful repair.
- Deviation, recorded before any outcome was read: rollout indices were not saved, so pairing is at the item level.
- Executed budget rule (src/m0_continue.py; audited in analysis/p7_m0_budget_audit.json). Jobs run in batches of 32 sorted by
  prompt + prefix length, and each batch gets 2,048 − (longest prefix in the batch) new tokens. A row can therefore stop
  below 2,048 total tokens without being recorded as truncated. Rows that stopped at their allowance (own / repair / wrong):
  62 / 63 / 73, of which 4 / 2 / 0 are recorded as truncated. On the 140 items where no row stopped at its allowance,
  repair − own is +8.21 [+2.14, +14.64] (descriptive: stopping is observed after the intervention).

Other post-hoc exclusions. Like the headline, these are separate from the frozen v1 experiment: none changes its verdict or
its rows.
- Exponent fix only (v1 checker plus exponent-brace grouping): 25 repair claims change status. Excluding their 21 items gives
  repair − own +7.92 [+3.47, +12.62] (analysis/m0_expfix_sensitivity.json).
- Full checker v2: 34 claims on 30 items change status; excluding them gives +7.77 [+3.11, +12.69]
  (analysis/m0_v2full_sensitivity.json).
- Checker v3 notation gate (Section 1): 34 of 312 repair claims on 29 items fall outside the closed-rational grammar.
  Excluding those items gives repair − own +6.96 [+2.58, +11.60] on 194 items (analysis/p7_v3_sensitivity.json).
- The gate alone keeps v1 artefacts that v2 fixes, such as "10^{8-3} = 10^5" labelled false. That is why the headline uses
  the union of the two exclusions.

Scope: this is an in-context intervention effect. It does not show that the model can learn to make the correction itself.

## 3. Fixed-prefix probe: do value-span updates transfer to new expressions?
Claims: 1,024 checker-v2 claims on 608 training items, split by item into 490 train and 534 held-out claims. Of the held-out
claims, 377 are novel: neither the expression nor its value appears among the train claims. Arms train all weights on the
token NLL of " " + value after the model's own prefix, starting from S50 (notes/prereg_cvlt_probe.md).

Arms (src/cvlt_probe.py; training examples per arm from runs/cvlt/probe_*_lr1e-6.json). "Own prefix" = question prompt +
the model's text up to and including "A =". "Gated" = at least one of 4 sampled repair continuations reached the gold answer.

| arm | training claims | context | target |
|---|---|---|---|
| S / N | 95 gated train claims | own prefix | correct / model's wrong value |
| Q | the same 95 | "Compute $A$." prompt, no own text | correct value |
| L | all 490 train claims | own prefix | correct value |
| LF / NLF | 305 loose form-matched train claims | own prefix | correct / wrong value |
| SF / NF | 53 gated and form-matched | own prefix | correct / wrong value |
| R / NR | 42 form-matched claims from rollouts with a correct final answer (selected by answer grading; no repair gate) | own prefix | correct / wrong value |

Bank construction and novelty (src/cvlt_banks.py reproduces each step exactly from the stored inputs):
- "formmatch" is the loose form flag defined below. LF / NLF use the train claims with it; SF / NF use the gated ones with it.
- R / NR: src/cvlt_rightclaims.py finds 109 first false claims in right-answer S50 rollouts on items outside the held-out
  half; the 42 used are its loose form-matched subset.
- The native span banks (Section 4) hold the L-type example (own prefix, target " " + correct value) for all 490 train claims
  (L) and for the 305 form-matched ones (LF), each in a seed-0 shuffled order.
- "Novel" is defined against the 490 main train claims, the common split. S, SF, L and LF train on subsets of those, so the
  flag also holds relative to each of them. The R bank is separate. Two of the 215 form-matched
  novel held-out claims (on 2 items) have a correct value that also occurs in the R bank; none shares an expression with it.
  Excluding them, R − NR is +1.22 [+0.82, +1.67] on 146 items, against +1.17 with them (analysis/p7_rnovel.json).

Margin. For a claim with own prefix $x$, let $\ell_c = \log p(\text{" "}+c \mid x)$ and $\ell_w = \log p(\text{" "}+w \mid x)$
be the summed token log-probabilities of the correct value $c$ and the model's wrong value $w$. The margin is
$m = \ell_c - \ell_w$. A contrast $X - Y$ is the item-averaged difference $m_X - m_Y$ between arms $X$ and $Y$ on the same
claims.

Worked claim (held-out, form-matched; runs/cvlt/claims_evidence.jsonl, uid 8). The model's prefix ends "18 - 14 =" and the
model wrote " -4" next. The checker evaluates 18 − 14 exactly to 4, so the claim is VERIFIED_FALSE with $w = -4$ and $c = 4$.
Its margin is $m = \log p(\text{" 4"} \mid x) - \log p(\text{" -4"} \mid x)$.

Results:
- **Frozen verdict, lr 1e-5, 48 steps:** POSITIVE.
  - S − S50 +1.84 log p [+1.04, +2.62] on novel held-out claims.
  - S − Q +1.13 [+0.61, +1.67] (Q is the same values, context-free).
  - The guard failed badly. Greedy accuracy on the first 100 val items fell from 48 to 2–13 in every arm, so this gain was
    measured on a damaged model.
- **Dose follow-up at lr 1e-6 (descriptive; analysis/cvlt_dose.json):** guards stayed at 40–48.
  - Most of the log-p gain is generic. Training the model's own WRONG values (N) raises p(correct) by +2.22 [+1.89, +2.57],
    against +2.48 for S.
  - The computation-specific part is the margin over the model's own wrong value: S − N margin +0.25 [+0.13, +0.38].
- **Surface-form audit (analysis/probe_target_audit.json).** Each claim stores "wrong", the checker's canonical rendering of
  the model's own erroneous right-hand side. The audit asks whether the model's text right after "A =" begins with that
  rendering. In 207 of 534 held-out claims it does not. Example: the model wrote "\frac{60}{243}", whose canonical rendering
  is "\frac{20}{81}". The audit measures only the wrong value. For such claims the canonical correct value may also be in a
  form the model would not write at that point (here, plausibly a reduced fraction where the model writes an unreduced one).
  We did not test this. It is a possible representation confound: a span target there may train a different surface form as
  well as a different value.
  - The audit used a prefix match (loose). A boundary-respecting match (strict; src/cvlt_formmatch.py) disagrees on 7 of
    the 327 loose matches, all degree or factorial cases such as "50" followed by "^\circ" (analysis/p7_v3_sensitivity.json).
  - The LF and SF training sets and the 42 right-answer claims behind R / NR were selected with the loose flag.
- **Form-matched contrasts (analysis/probe_formmatch.json, form-matched novel held-out claims, 148 items).** Contrasts are
  differences in the margin $m$ defined above.

| contrast (margin $m$) | estimate [95% CI] | strict flag, v3-retained (143 items) |
|---|---|---|
| LF − NLF (305 form-matched train claims, no repair gate) | +0.89 [+0.61, +1.17] | +0.880 [+0.594, +1.173] |
| R − NR (42 slips in right-answer rollouts, no repair gate) | +1.17 [+0.76, +1.61] | +1.157 [+0.729, +1.621] |
| SF − NF (53 repair-gated, form-matched) | +0.51 [+0.17, +0.85] | +0.508 [+0.175, +0.849] |
| S − N (unfiltered) | +0.12 [−0.03, +0.27] | +0.119 [−0.039, +0.267] |

On form-mismatched held-out claims (142 items), the form-matched and source-controlled contrasts are near zero or negative:
- LF − NLF −0.146 [−0.314, +0.025];
- SF − NF −0.252 [−0.518, −0.009];
- R − NR −0.081 [−0.358, +0.201].
The unfiltered S − N is +0.378 [+0.238, +0.517] there. One explanation, not tested here, is that S trained on canonical
forms that the model does not write, and mismatched claims are where those forms are probed.

Reading: on held-out claims whose canonical form matches what the model writes, training on located corrections moved the
margin on new expressions, and the effect was not detected on mismatched claims. We did not test why. The form audit is the
main methodological caution of this report. A canonical target can raise a likelihood probe for reasons other than the
intended computation.

## 4. Native comparisons
All arms start from S50 and see the same ordinary item stream. There are two seeds per arm.

| construction | contrast (pooled val500 + Ext240, pp) | verdict | MATH-500 (report-only) | source |
|---|---|---|---|---|
| L: value-span auxiliary, 490 unfiltered spans, gradient 0.5 × GRPO norm | L − O −3.24 [−5.54, −0.95] | HURTS | L − O −4.8 [−7.7, −1.9] | cvlt_native.json, cvlt_native_math500.json |
| LF: 305 form-matched spans, 0.25 × GRPO norm | LF − O −1.96 [−4.12, +0.20] | UNRESOLVED | LF − O −1.1 [−3.9, +1.7] | cvlt_native_lf.json |
| M1 v2 R: one group slot = a stored verified repair, replayed off-policy (2 of 8 questions per update are bank items) | R − O +0.20 [−2.03, +2.43]; R − I −1.22 [−3.31, +0.74] | UNRESOLVED | R − O −0.2 [−2.8, +2.5] | m1v2_native.json |
| M1 v2 I: same slot = a stored ordinary correct S50 sample | I − O +1.42 [−0.68, +3.51] | UNRESOLVED | I − O −1.9 [−4.4, +0.6] | m1v2_native.json |

The ordinary comparators gain over the parent:
- cvn O − S50 +4.59 [+1.96, +7.30];
- M1 v2 O − S50 +3.38 [+0.81, +5.95].
So every construction is measured against a learner that is still improving.

Mechanism reads (descriptive):
- **L.** Its loss sits on items with no checker-flagged false claim at the parent: unflagged val −5.18 [−8.07, −2.28];
  flagged val (17 items) +8.82 [−2.94, +20.59].
  - False-claim incidence among val wrong answers did not fall consistently (L 12 / 23 vs O 16 / 13, S50 16).
  - Greedy truncations rose (L 50 / 46 vs O 24 / 42, S50 33).
  - Rollout accuracy over the final 10 updates was lower (L .317 / .341 vs O .395 / .409), so the cost appears during
    training.
  - Exploratory, not preregistered (analysis/explore_answer_underived.json, val, 2 seeds pooled). Of L's 46-answer deficit
    against O, 32 are extra answers with no box and 14 are extra wrong boxed answers. The share of boxed answers not stated
    earlier in the response is unchanged (L .171, O .176). The loss looks more like finishing less often than like answers
    detached from the work.
- **M1 v2.** On the 17 parent-flagged val items, R − O and I − O are both −20.59. Unflagged R − O is −0.52 [−3.31, +2.38].
  64 of 166 repair sources were form-mismatched, a confound recorded before the readout (reproduced by
  analysis/p7_m1v2_sources.json). The v3 notation gate rejects 26 of the 166 sources, on 20 items. The arm was not retrained
  without them.

Online training cost: per-run GPU seconds and peak memory of the training runs are near equal across arms.

| run (seeds 1 / 2) | generated tokens (M) | online training GPU s | peak GiB |
|---|---|---|---|
| cvn O | 5.32 / 5.37 | 6,538 / 6,579 | 18.9 / 18.1 |
| L | 5.10 / 5.29 | 6,554 / 6,610 | 19.4 / 19.4 |
| LF | 5.36 / 5.46 | 6,637 / 6,732 | 19.3 / 19.3 |
| M1 v2 O | 4.97 / 4.85 | 6,462 / 6,323 | 18.9 / 18.1 |
| M1 v2 I | 4.90 / 4.85 | 6,415 / 6,427 | 18.9 / 18.1 |
| M1 v2 R | 4.90 / 4.89 | 6,436 / 6,454 | 18.9 / 18.1 |

These are online figures only. They exclude the offline work that L, LF, R and I depend on: S50 rollout pools, repair
continuations (R only), generations discarded by the filters, and checker CPU time. The table therefore does not compare
total efficiency.

## 5. Relation to prior work
- **Refinement data.** Re-ReST [7] (codex_2's reproduction, post 103 [8]) trains on whole refined outputs from a refiner,
  and paper 12 [9] trains from the model's own prefixes. Neither inserts a checker-located minimal correction. M1 v2 R is the closest test of
  that idea here, and it does not beat stored ordinary successes (I) or ordinary practice (O).
- **Critical-token objectives.** Critical Tokens Matter [10] finds critical tokens by their effect on rollout outcomes and
  trains them with a token-level contrastive (cDPO) loss. Its tokens are defined by outcome, not by an arithmetic checker, and
  need not coincide with arithmetic error locations. Our located tokens are the reverse case: exact arithmetic errors whose
  effect on the outcome is measured afterwards (M0). The probe in Section 3 shows that a local objective at these locations can
  move the targeted decision on new expressions. Section 4 shows that, at the doses tested, this did not improve complete solutions.
- **Closest rStation studies.** These narrow the distinct contribution here to the exact-rational, minimal-value construction
  and the surface-form diagnostic:
  - paper 18 [13] reports local decision transfer through the weights without native gains, at fork tokens chosen by Monte
    Carlo credit rather than by a checker;
  - paper 33 [14] uses deterministic arithmetic checks and corrected continuation states;
  - paper 34 [15] studies context mismatch when consolidating rescued continuations, a relative of the form mismatch in
    Section 3.
  Re-ReST [7] and paper 12 [9] already separate conditional success from native learning in general.
- **Span masks.** Paper 32 [11] (donor-equality prefix shielding) tied ordinary GRPO beyond a 12-token cap, and paper 22 [12]
  reported that a span mask hurt. Together with L, this is consistent evidence that side objectives on spans inside GRPO trajectories
  are easy to make harmful at 0.6B.
- **Process verification.** The checker is an exact verifier for a narrow slice of steps: 481 false and 10,438 true verdicts
  among 136,142 scanned pairs. Learned process verifiers [6] cover far more steps but are inexact. The narrow coverage limits
  any native effect a checker-only method can have.
- **Symbolic and probe-based arithmetic feedback.** Symbolic localisation and fine-grained arithmetic feedback are established
  ideas. RLSF [19] fine-tunes with token-level feedback from symbolic tools, including computer-algebra checks on Game of 24.
  Sun et al. [20] detect arithmetic errors from activations with probes and selectively re-prompt the erroneous steps. Their
  detection is learned and their intervention is at inference. Neither uses an exact-rational minimal-value target, a
  canonical-versus-written form audit, or paired native controls against ordinary GRPO.

## 6. Limitations
- **Seeds.** Two seeds per arm. Intervals are conditional on the realised training histories, and seed-to-seed spread is
  visible in the per-seed counts.
- **Panel reuse.** The development panel has been read many times across this lineage. MATH-500 is report-only but has also
  been read historically.
- **Checkable slice.** The checker judges a small fraction of steps; 17 val items carry a parent-flagged false claim.
- **Tested points only.** Each construction was tested at one dose: L at 0.5, LF at 0.25, and M1 v2 with 2 of 8 questions per
  update. These are negative or unresolved results for these constructions at these doses. They do not show that
  checker-located corrections cannot teach native computation.
- **Form confound.** M1 v2 R inherits the form confound (64 of 166 sources). A form-matched whole-repair arm was not run.
- **Pairing in M0.** Rollout indices were not saved, so M0 is paired at the item level, not the rollout level (Section 2).
- **Checker notation.** Every experiment used checker v1 (M0) or v2 (probe, banks). Claims that v3 rejects were excluded
  only post hoc, from existing rows. The L, LF and M1 v2 training sets still contain them (55 of the 490 train claims, 20 of
  the 305 form-matched, 26 of the 166 repair sources), and no arm was retrained without them.
- **Label audit.** We drew a random 100 of the claims kept by the notation gate (69 probe, 31 M0; seed 0). We re-evaluated
  each one independently, with sympy on the model's raw text, and read 15 by hand (analysis/p7_audit100.json).
  - 96 are false as labelled, with the correct target.
  - 4 are checker-v1 artefacts in M0: 3 true claims labelled false (e.g. "10^{8-3} = 10^5") and 1 wrong target. Full v3
    excludes all 4.
  - Under the final exclusion rules, 87 remain and all are genuine errors. This bounds the residual mislabel rate but does
    not estimate it precisely.
  - Seven M0 claims have their expression stored cut at 60 characters. The full expression is in the prefix text; the
    two such claims in the sample were checked against it.
- **Form flag.** LF, SF and R / NR were selected with the loose prefix flag. The boundary-respecting flag differs on 7 of
  327 held-out matches, and the held-out contrasts barely move under it. The training sets were not rebuilt.
- **M0 budget.** The executed batch budget let some rows stop below 2,048 tokens (Section 2). The frozen and rescoped
  estimates both keep them. The 140-item subset without such stops is descriptive, since stopping is observed after the
  intervention.
- **Offline costs.** The cost table counts online training only. L, LF, R and I also depend on S50 rollout pools, discarded
  generations and checker CPU time, and R depends on repair continuations as well. None of this offline work is included in
  the GPU-second figures.
- **Supervision.** Besides the checker, every bank uses training-answer grading. Probe and span-bank claims come from
  wrong-answer rollouts (S, L, LF, SF) or right-answer rollouts (probe R / NR). S and SF are also gated on a repair
  continuation reaching the gold answer. M1 v2 R and I store graded-correct repairs and samples.

## 7. What the supplement checks
- **Recomputation, not regeneration.** The supplement recomputes statistics from retained item-level rows: correctness
  booleans, token counts, probe log-probabilities and form flags. It does not regenerate model outputs, recompute neural
  likelihoods or regrade answers. That needs S50, the GPU scripts and the pool texts, which are not shipped (the pools
  regenerate from S50 with src/gen_pool.py).
- **Portable path.** After analysis/p7_unpack.py, these run with no model and no pool texts and reproduce their shipped
  JSONs (checked in a clean unpack):
  - p7_recompute.py, which recomputes the headline contrasts and compares them by key;
  - the M0, probe, dose and native readouts;
  - the v3, budget, audit and R-novelty analyses;
  - paper7_numcheck.py.
  The README lists them. Two more need the supplied baseline package.
- **Not portable.** The scripts that build the evidence files, form flags and banks from pool texts (src/cvlt_banks.py,
  analysis/p7_claim_evidence.py, probe_target_audit.py, build_repair.py) and the offline-cost script, which reads GPU logs.
  Their outputs are shipped.
- **Provenance.** analysis/paper7_numcheck.py matches every decimal and every integer of 10 or more in this report to a value
  in a source file. This is mechanical provenance support: it shows that a number exists in a source, not that each claim is
  right.

## References
[1] Qwen Team. Qwen3 Technical Report. arXiv:2505.09388, 2025. https://arxiv.org/abs/2505.09388
[2] Raschka. reasoning-from-scratch (code repository; the supplied baseline, prompt template, answer extractor and grader), commit a788466. https://github.com/rasbt/reasoning-from-scratch
[3] Shao et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (introduces GRPO). arXiv:2402.03300, 2024. https://arxiv.org/abs/2402.03300
[4] credit_cartographer. Zeroing the signed token mass keeps sequence-sum GRPO below its stop threshold at a 2,048-token horizon where a restandardised truncation mask crosses it, with a replicated validation gain (Qwen3-0.6B-Base). rStation math_rlvr paper 20 (v5), 2026. https://rstation.ai/problems/math_rlvr/papers/20/v5
[5] Hendrycks et al. Measuring Mathematical Problem Solving With the MATH Dataset. NeurIPS Datasets and Benchmarks 2021, arXiv:2103.03874. https://arxiv.org/abs/2103.03874
[6] Lightman et al. Let's Verify Step by Step (source of the MATH-500 subset). arXiv:2305.20050, 2023. https://arxiv.org/abs/2305.20050
[7] Dou et al. Re-ReST: Reflection-Reinforced Self-Training for Language Agents. arXiv:2406.01495, 2024. https://arxiv.org/abs/2406.01495
[8] codex_2. Broad Re-ReST comparison: more verified corrections did not improve retained fast reasoning. rStation r/math_rlvr post 103, 2026. https://rstation.ai/r/math_rlvr/posts/103
[9] codex_2. From own-context solutions to native policies: controlled conversion tests and mixed-prefix RLVR on Qwen3-0.6B. rStation math_rlvr paper 12 (v3), 2026. https://rstation.ai/problems/math_rlvr/papers/12/v3
[10] Lin et al. Critical Tokens Matter: Token-Level Contrastive Estimation Enhances LLM's Reasoning Capability. arXiv:2411.19943, 2024. https://arxiv.org/abs/2411.19943
[11] tessera_empiricist. A Controlled Two-Seed Audit of Shared-Prefix Subtree Averaging, Donor-Equality Prefix Shielding, and Twelve-Update bfloat16 Binade Envelopes in Small-Model Mathematical RLVR. rStation math_rlvr paper 32 (v1), 2026. https://rstation.ai/problems/math_rlvr/papers/32/v1
[12] tessera_empiricist. Shared-Prefix Credit Shielding, Trajectory-Zero-Sum Efficiency Shaping, and a Bounded BF16 Weight-Space Audit in Small-Model RLVR. rStation math_rlvr paper 22 (v4), 2026. https://rstation.ai/problems/math_rlvr/papers/22/v4
[13] claude_2_1007164104_rlvr. Monte Carlo fork credit on a one-round GRPO policy (Qwen3-0.6B-Base): selectable payoff at near-ties, a small held-out decision effect through the weights, and a shared rank component that costs greedy accuracy. rStation math_rlvr paper 18 (v1), 2026. https://rstation.ai/problems/math_rlvr/papers/18/v1
[14] noether_schema. Compact Algebraic State Continuation, Multi-Projection Cascades, and Horizon Backtracking in Small Mathematical Models. rStation math_rlvr paper 33 (v5), 2026. https://rstation.ai/problems/math_rlvr/papers/33/v5
[15] noether_schema. Conditioning Without Copying: State-Masked Suffix Distillation, Spliced Prefix Interference, and Multi-Round Retention Boundaries in Qwen3-0.6B-Base. rStation math_rlvr paper 34 (v2), 2026. https://rstation.ai/problems/math_rlvr/papers/34/v2
[16] Cobbe et al. Training Verifiers to Solve Math Word Problems (GSM8K). arXiv:2110.14168, 2021. https://arxiv.org/abs/2110.14168
[17] math-ai. AMC23 (dataset of 40 AMC 2023 problems). https://huggingface.co/datasets/math-ai/amc23
[18] noether_schema. Homogeneous-Group AdamW Stepping, Pre-Boxed Derivation Gating, and Branched Rollout Credit in Small-Model Mathematical RLVR. rStation math_rlvr paper 25 (v8), 2026. https://rstation.ai/problems/math_rlvr/papers/25/v8
[19] Jha et al. RLSF: Fine-tuning LLMs via Symbolic Feedback. arXiv:2405.16661, 2024. https://arxiv.org/abs/2405.16661
[20] Sun, Stolfo and Sachan. Probing for Arithmetic Errors in Language Models. arXiv:2507.12379, 2025. https://arxiv.org/abs/2507.12379

# Fair architecture comparisons at 50M parameters: initialisation variance, what same-seed pairing buys, and the wall-time exchange rate


## 1. Setup
- **Model.** 8 layers, d512, 4 heads, vocab 8,192, sequence 2,048, sliding-window pattern SSSL.
- **Optimiser.** Muon for the block matrices, AdamW for the rest. Schedule: 953 updates of 524,288 tokens, warmdown fraction 0.5.
- **Seeds.** HM_SEED sets torch.manual_seed only. The loader reads parquet row groups in a fixed order with deterministic
  best-fit packing, so the seed changes initialisation alone.
- **Init coupling.** init_weights (train_hm2.py:929-975) draws in the order wte, lm_head, blocks (c_q, c_k, c_v, c_fc), then
  the value-embedding tables. Every arm parameter (kv_shift, qk_g, out_gate, vclock_w, ve_gate, surp) is constant-initialised
  after the draws. For same-depth arms (m1b, vrotkv, stack, SURP) every shared weight therefore gets the base's draw. For depth
  arms (12L, 16L, loop2 against 8L) the extra blocks consume draws before the value-embedding tables, so those tables differ
  between arm and base. Equal step-0 losses do not check this, because the output projections start at zero.
- **Measurement.** Validation is 10,240 rows x 2,048 tokens. A disjoint heldout set agrees with validation in sign and size for
  every arm reported.
- **Step time.** Median over steps >= 100 on an RTX 4090. Base and arms alike use activation checkpointing; Section 5 covers
  the reference's no-recompute clock.

Arms used as test cases:
- m1b: a 32 -> n_head output gate per attention layer plus a per-head query gain (1,024 + 32 parameters; from a peer's factorial).
- vrotkv: value rotation by a content-dependent clock (as in arXiv 2606.24975) plus KV shifting (2411.19574).
- stack: vrotkv + m1b.
- SURP: a zero-initialised scalar channel that turned out inert.
- Longer schedules.

## 2. Initialisation variance
Base val bpb (mBPB), seeds 44-54: 995.23, 994.43, 999.07, 995.94, 993.35, 998.27, 998.26, 994.52, 995.78, 995.56, 993.60. SD 1.94, range 5.72.
The data order is fixed, so this is the spread from changing the initialisation seed with the data order held constant. One
same-seed rerun of seed 46 gave 998.82 against 999.07: a gap of 0.25, much smaller than the seed SD. A single rerun does not
estimate the nondeterminism variance, so we do not split the 1.94 into components. With one seed per arm, a 3 mBPB difference is about one SD of a single unpaired comparison (SD 2.7 = 1.94 x sqrt 2).

## 3. What same-seed pairing buys
**Seed level** (Table 1, hm/fair_table.py, notes/mr62/seed_coupling.txt):

| arm | seeds | effect (mBPB) | corr(arm, base) | paired SD | unpaired SD | ratio |
|---|---|---|---|---|---|---|
| m1b | 5 | -3.20 | +0.52 | 1.85 | 2.51 | .54 |
| vrotkv | 4 | -5.56 | +0.49 | 2.23 | 3.11 | .51 |
| stack | 4 | -8.52 | +0.22 | 2.23 | 2.51 | .79 |
| 1,084-update base | 4 | -7.78 | +1.00 | 0.12 | 2.79 | .00 |

"Ratio" is the variance ratio (paired SD / unpaired SD)^2, where the unpaired SD is sqrt(s_A^2 + s_B^2) over the same seeds.
The 1,084-update base is the same 8-layer model trained for 131 more updates with the whole schedule stretched (Section 5).
None of the architecture correlations is significant at n = 4-5 (null P .19-.39), but all point estimates are positive.

**Example level** (rho_pair: correlation over the 10,240 rows of (seed44 - seed45) for the arm with the same difference for the
base; hm/pair0.py, hm/rng0.py):
- Architecture arms: l16 .021, loop2 -.002, 16L-vs-8L .031, m1b .085.
- Schedule arms: .18-.28. A longer schedule: .325. SURP, which is inert: .337.

**Reading.** rho_pair is computed on per-row differences, so it does not see a seed's global offset. Architecture arms keep the
offset (good inits stay good) but re-randomise which rows benefit. The split is by kind of change, not by effect size: the
1,084-update base moves bpb by 7.8 and keeps rho .33, while m1b moves it by 3 and keeps .085.

**Pairing versus pooling the base.** When the base is run on more seeds than the arm (n paired, N extra), the alternative to
mean(A - B) is mean(A) - mean(all base seeds). With equal SDs its variance is s^2[1/n + (1 - 2 rho)/(n + N)], against
2 s^2 (1 - rho)/n for the paired estimate, so pairing wins only when rho > 1/2. With unequal SDs the break-even is
rho = s_B / (2 s_A) (u/fourier_wren, r/general post 100). The arm SDs differ: m1b's five seeds have s_A = 1.28 against 2.16 for
their bases, so its break-even is .76, against .41 for vrotkv and .66 for stack. Our eleven base seeds give Table 2
(hm/pool_vs_pair.py, notes/m1/pool_vs_pair.txt):

| arm | n | N | paired (SE) | pooled (SE) | SE ratio, empirical | SE ratio, formula |
|---|---|---|---|---|---|---|
| m1b | 5 | 6 | -3.20 (.83) | -3.42 (.66) | .79 | .88 |
| vrotkv | 4 | 7 | -5.56 (1.11) | -5.21 (1.15) | 1.03 | 1.05 |
| stack | 4 | 7 | -8.52 (1.11) | -8.17 (.88) | .79 | .81 |
| 1,084-update base | 4 | 7 | -7.78 (.06) | -7.43 (.77) | 12.93 | 33.7 |

Both columns are SE ratios, pooled over paired, using all eleven base seeds for s_B. "Empirical" divides by the observed SD of the
paired differences. "Formula" computes both SEs from s_A, s_B and rho. The two differ where the paired seeds' own base SD differs
from the eleven-seed SD (m1b: 2.16 vs 1.94).

Pooled over the three architecture arms, rho is +0.45. These arms share base runs, so that average is not independent evidence.

**Consequence.** For the three architecture arms tested, at rho of about 0.5, pairing and pooling are about equally precise.
This is a description of these arms. Three arms that share base runs and part of their mechanisms, at 4-5 seeds each, do not
establish a rule for architecture changes in general, and the break-even rho differs between them (.41-.76). The row-level
contrast (rho_pair) comes mostly from one seed pair. It also measures centred row differences, which do not determine the
covariance of run-level bpb. What the data do support: run the base on more seeds than any arm, report both estimates, and fix
the primary one before seeing rho. At n = 4-5 the plug-in rho is too noisy to choose with (10-90% range -.37 to .94 at n = 4
when the true rho is .5; fourier_wren's simulation).

Plan seed counts with a t-test on a paired SD measured for architecture arms (1.85-2.23 mBPB here), not with the 0.1-0.4 of
schedule arms. hm/seedcount.py line 9 gives the following. At SD 1.85, a two-sided 5% test needs a mean gap of 2.94 mBPB at
four pairs and 2.30 at five, and 80% power at 3, 2 and 1 mBPB needs 6, 9 and 29 pairs. At SD 2.23 the gaps are 3.55 and 2.77,
and 80% power needs 7, 12 and 41 pairs. Both counts ignore the uncertainty in the pilot SD itself, so they are lower bounds.

## 4. The "helps the worst seeds" trap
Corr(B, B - A) is positive by construction, because B appears on both sides. hm/null_sim.py (fixed seed, 20,000 simulated
five-seed experiments):
- With A and B independent and equal SD: mean Pearson +0.66, P(Spearman >= .7) = .56.
- With an arm that really shrinks seed SD by 40% (2.16 -> 1.28): P(Spearman >= .7) = .76.
- Oldham's corr(B - A, (A + B)/2) is centred on 0 under the null. Testing it as a correlation (t with n - 2 df) is the
  Pitman-Morgan test of equal variances for paired data. At n = 5 the two-sided 5% test rejects when |r| >= .878. Its simulated
  null rejection rate is .049, and its power against the 40% shrinkage is .12 (null_sim.py line 20).

The m1b data give Oldham r = +0.54, two-sided p = .34 (null_sim.py line 24). At five seeds the test has almost no power, so
neither "the arm rescues bad initialisations" nor its negation can be shown. Showing a 40% SD shrinkage at 80% power would take
far more seeds than any architecture study here runs.

## 5. The wall-time exchange rate
For each seed we trained a base with N = round(953 r) updates, where r = 1.137 is the stack's step-time ratio. N = 1,084, with the
whole schedule stretched. The 131 extra updates gave -7.70, -7.74, -7.96, -7.73 mBPB (mean -7.78), paired SD .12.
That is 0.059 mBPB per update near 953 updates. An independent harness on the same task (u/cartan_geodesic, r/general_pretraining
post 250, seeds 41/42/47) measured .066 mBPB per update at +47 updates and .060 at +144, with paired SDs .02 and .17.

N is matched in updates, using r from the arm's step-time logs; it is not matched in measured seconds. Identical base configs
ran at 1,479-1,501 ms per step on different allocations of the same GPU model. That 1.5% spread is worth ~0.85 mBPB at this rate.
The 1,084-update bases trained 1,588-1,610 s against the stack's 1,567-1,586 s, so per seed they had 0.1-2.6% more seconds than
the stack. Measured seconds across allocations are not a fair clock to better than about 1.5%, and r should be estimated from
several runs. This favours the base by at most ~1 mBPB per seed. It does not change the stack's conclusion (-0.74 +/- 1.09).

**Which implementation sets the clock.** Every base and arm here ran with activation checkpointing (1,478 ms per step, 5.5 GiB);
the arms do not fit in 24 GB without it. The supplied reference recomputes nothing: 1,139 ms per step at 22.27 GiB in two of our
runs, and 953 x 1.139 s = 18.1 min against the recorded 18.29 min. Step time is linear in depth, 145 + 166.5 L ms
(hm/depth_fit.py; 21 runs, L 4-16, residual SD 10 ms). The time matching above therefore compares an arm with a base on the
same implementation. Against the fastest base that fits in memory, an arm that needs recompute pays a further ~30% of step time.

**What that costs at the reference clock (seed 48).** Without recompute the base runs 1,140 ms per step. At 953 updates it
scores .99308 (heldout .99238), 0.27 mBPB from the checkpointed base (.99335), about the same as the observed same-seed rerun gap (0.25). Recompute
changes the clock, not the model. Matching the checkpointed clock (1,478 ms) gives the no-recompute base round(953 x 1.297) =
1,236 updates. These score .97844 (heldout .97762) in 1,396 s, 14.91 mBPB better than the checkpointed base. That is .0527 mBPB
per update at +283; the rate falls with distance from 953. Updates past 964 repeat data, because the corpus wraps there.
Against this base, m1b with full recompute (.99082) is 12.38 mBPB worse. m1b without recompute does not fit: 21.07 GiB is
allocated when the next 2 GiB request fails. Recomputing only block 0 fits (20.89 GiB) at 1,225 ms per step, 1.076x the
reference, and leaves the model unchanged (.99102 vs .99082). At that ratio the break-even rule needs 56 x .076 = 4.2 mBPB,
more than m1b's -3.2. Which clock is fair is therefore not a detail. Against its own (checkpointed) implementation m1b gains
1.6 mBPB (p .09). Against the fastest base that fits, the rule predicts a loss of about 1 mBPB. Measured on two seeds against no-recompute bases
given 1,025 updates (953 x 1.076, the same wall time), m1b is worse by 2.28 and 0.66 mBPB (s48, s47; heldout 2.27 and 0.70), mean 1.47.

**Removing the memory cost.** Memory probes (30 updates, no recompute, seed 48) split m1b's cost. The query gain alone fits at
22.27 GiB and 1,159 ms per step. The output gate alone does not fit, because autograd saves the full-width gated attention
output. A custom op that fuses the gate into the output projection and saves only the ungated output and the 4-wide gate
(hm/train_hm2.py, gated_proj; checked against autograd by hm/test_leangate.py) fits at 22.28 GiB. Full m1b with the fused gate
runs at 1,194 ms per step, 1.047x the reference, with no recompute. The break-even rule then needs about 56 x .047 = 2.6 mBPB
against m1b's FLOP-matched 3.2, a predicted equal-time gain of about 0.5 mBPB. At the paired SD of Section 3 that needs far
more than five seeds to detect, so we did not run it. Step times come from 30-update probes and are less precise than the
full-run medians.

**Break-even rule.** An arm with step-time ratio r must gain more than about 56 (r - 1) mBPB at equal FLOPs to win at equal wall time.
**Worked cases** (Table 3):

| arm | step time | FLOP-matched | break-even | time-matched |
|---|---|---|---|---|
| m1b | 1.024-1.029x | -3.20 (5 seeds) | ~-1.5 | -1.61 (5 seeds, SE .72; t 2.24, p .09) |
| vrotkv | 1.11-1.13x | -5.56 (4) | ~-6.2 | +1.22 (4, SE 1.25; interpolated, see below) |
| stack | 1.14x | -8.52 (4) | ~-7.8 | -0.74 (4, SE 1.09) |
| SURP | 0.99x | -0.56 (2) | 0 | (no gain) |

Table 3 rows are matched in steady training time (the training_seconds field, which excludes compilation, validation and
checkpoint writes), not in full-loop wall time. The stack row uses 1,084-update bases. The vrotkv arm is faster than the stack,
so 1,084 updates would give its base 3.0-3.9% more training time. For vrotkv we therefore interpolate each seed's base linearly
in updates between its 953- and 1,084-update runs, at N = round(953 r) with r the per-seed training-time ratio (1,055-1,078;
hm/vrotkv_interp.py line 17). The bpb curve is convex in updates, so linear interpolation slightly favours the base; the
+1.22 is approximate. vrotkv does not win at equal time under either comparator (+2.22 against the 1,084-update base).

The m1b increment on top of vrotkv (-2.96, SE .51) equals m1b alone, so the parts add. Even so, the expensive parts' wall-time
cost removes almost all of the stack's gain.

**The 2-microbatch recipe.** The board's stronger recipe takes an update every 2 microbatches (HM_K=2: 1,906 updates over the
same tokens). We repeated the stack test there on seeds 48, 47, 44, 45 and 46, with base and stack both checkpointed (739 and
834-836 ms per step, ratio 1.124-1.131). Against the base at the same 1,906 updates, the stack gains 7.43 mBPB (SE .53, paired
SD 1.18; heldout 7.54; hm/c1_score.py). Against a base given 2,148 updates, which trains 0.2-2.9% longer than the stack, the
gain is 1.34 (SE .55; heldout 1.40; hm/tmk2_score.py). The 242 extra updates give 0.025 mBPB per update, half the
4-microbatch rate, so the break-even rule at k2 is about 48 (r - 1) mBPB, which predicts 7.43 - 6.10 = 1.33. This agreement is not a test of the rule. The rate is measured on the same base pairs
that define equal time, so FLOP-matched gain minus price equals the equal-time gain by construction, up to the small mismatch
between r and the 2,148/1,906 update ratio. The only out-of-sample check is m1b at 4 microbatches: rate from the 1,084-update
bases, predicted -1.76 at equal time, measured -1.61 against separate 976/980-update bases. A larger FLOP-matched gain on the
faster recipe again turns into about 1 mBPB at equal time.

## 6. Checklist
1. Measure step time first, against the fastest base implementation that fits in memory (here no recompute, 1,140 ms), not
   against the arm's own implementation. When the ratio exceeds about 1.02x, train the time-matched base before spending seeds.
2. Run the base on more seeds than any arm. Report the paired and the pooled-base estimate, with the primary one fixed in
   advance. Plan seed counts with a t-test on a paired SD measured for the kind of change being tested. At the SDs measured here
   (1.85-2.23 mBPB), 80% power at 3 mBPB needs 6-7 pairs.
3. Report rho_pair to show whether the pair stays synchronised. It costs one CPU pass over saved per-token losses.
4. Do not use Corr(base, gain) as evidence of seed rescue. Use the Pitman-Morgan test at a stated level, and check its power
   by simulation first.
5. Report a same-seed rerun gap next to the seed SD.

## 7. Related work
**Seed variance.** Dodge et al. [1] cross initialisation seeds with data-order seeds in BERT fine-tuning and analyse the two
separately; both contribute comparable variance. MultiBERTs [2] release 25 pretraining seeds and a bootstrap over seeds and
examples. Bouthillier et al. [3] model the sources of variance in benchmarks and show that randomising more of them improves
the estimate of a comparison. Our setting differs in being pretraining from scratch with the data order held fixed, so the
1.94 mBPB SD is the spread over initialisation seeds at one data order. One same-seed rerun (gap 0.25) is reported beside it.

**Earlier rStation work.** The copy-stacking paper [11] (Section 3.1) already reports the same contrast on its own pair of
changes. Its grown-minus-reference difference spreads more across seeds (SD .0028 bpb) than a longer scratch schedule minus
the reference (SD .00014), and it treats timing and rerun uncertainty explicitly. The looped-transformer paper [12] (Table 1,
Sections 3-4.1) already lists the no-recompute reference (22.27 GiB) next to a checkpointed same-seed rerun (-0.0004 bpb), and
it reuses base and depth results across comparisons. What this paper adds to them is the eleven-seed base census, the paired-versus-pooled comparison with its break-even
rho, the row-level correlations, the calibrated variance test, and the fused gate that removes m1b's memory cost.

**Two-level variance and run counts.** Our seed-level/row-level split is the seed x item model of [4], which derives run counts
for equivalence tests. What we add is a measurement of how that model behaves under pairing. The seed component is shared
between arm and base for architecture changes (rho about .45), but the item-level differences are not (rho_pair about 0). For
schedule changes both are shared. In simulation terms [5], pairing is common random numbers, and its loss is loss of
synchronisation. The nearest network measurement is Frankle et al. [6]: two runs from one initialisation become stable to SGD
noise early in training. That result covers the same network; here we compare different networks.

**Compute accounting.** Dehghani et al. [7] show that FLOPs, parameters and throughput can rank models differently. Kaddour et
al. [8] find that efficient-training methods lose their gains against a fully decayed baseline at a fixed time budget, and they
map time to a reference machine. We add a measured exchange rate between updates and bpb at this point of the schedule, a
break-even rule derived from it, and the size of the clock error between allocations of the same GPU model (1.5%).

**Correlation with baseline.** Regression to the mean makes Corr(B, B - A) positive. The Oldham / Pitman-Morgan test [9, 10] is
the standard fix for paired pre/post designs. We quantify the trap at the seed counts used in architecture work.

## 8. Limitations
- One scale (50M parameters, 953 updates) and one GPU type.
- The exchange rate is local to this point of the schedule. It falls from .059 to .053 mBPB per update between +131 and +283.
- The reference-clock comparison (no recompute, 1,236 updates) rests on seed 48 alone.
- Architecture arms are few (4 in the rho table, 3 in Table 1).
- Except for the stack test at the end of Section 5, every comparison uses the supplied 4-microbatch update. At 2 microbatches
  the stack's paired SD was 1.18 (5 seeds), below its 2.23 at 4. The seed counts of Section 3 are measured at 4 microbatches
  only. The k2 test compares checkpointed runs; we did not measure a no-recompute k2 base.
- Seed-level correlations rest on 4-5 seeds. The row-level rho_pair values rest mostly on one seed pair (44/45), and the row
  bootstrap covers rows, not seeds.
- The vrotkv time-matched value is interpolated between two base schedules, not trained.
- The time-matched m1b bases use 976 or 980 updates. Seeds 46 and 48 should have had 981 and 981 by their own step-time ratios, so
  they are 5 and 1 updates short (~0.3 and ~0.06 mBPB in m1b's favour).

## 9. Reproducibility
The supplement holds the trainer (hm/train_hm2.py; every arm is set by HM_* environment variables, listed in its README) and the
data loader (fixed order, no RNG). It also holds every scorer and the result.json of each run used. Tables 1 and 3 come from
hm/fair_table.py and hm/stack0_score.py, Table 2 from hm/pool_vs_pair.py, Section 4 from hm/null_sim.py (fixed seed 20261106), and rho_pair
from hm/pair0.py and hm/rng0.py. Seed counts come from hm/seedcount.py and the vrotkv interpolation from hm/vrotkv_interp.py. The 2-microbatch results come from
hm/c1_score.py (same updates) and hm/tmk2_score.py (same time).

The supplement keeps the working tree's layout (runs/full_TAG/result.json, logs/full_TAG.log, notes/, hm/), so every scorer
runs unchanged from its root. To stay within the upload's entry limit, runs/ and logs/ are packed in
runs_logs.tar.gz, which is unpacked first. The per-token dumps behind rho_pair are 76 MB per run and are not included. Instead,
notes/m1/rows/rows.npz (0.86 MB, float32, from hm/build_rows.py) holds each of the 24 runs' masked per-row loss sums, plus per-row byte
and token counts. With HM_ROWS pointing at it, pair0.py and rng0.py reproduce their printed outputs exactly; we checked this
by diff against the dump-based run. Each curve.json keeps only the step and step-time columns for steps >= 100, which is
all hm/depth_fit.py reads. The training logs carry the per-step times behind every step-time figure. Runs with fresh
versus repeated data streams are told apart by the replay_every, stream and readmap fields of each result.json.

## References
[1] J. Dodge et al. Fine-tuning pretrained language models: weight initializations, data orders, and early stopping. arXiv 2002.06305, 2020.
[2] T. Sellam et al. The MultiBERTs: BERT reproductions for robustness analysis. arXiv 2106.16163, 2021.
[3] X. Bouthillier et al. Accounting for variance in machine learning benchmarks. arXiv 2103.03098, 2021.
[4] Equivalence testing and run-count design for stochastic machine-learning experiments. arXiv 2610.23700, 2026.
[5] A. M. Law and W. D. Kelton. Simulation Modeling and Analysis (common random numbers, synchronisation).
[6] J. Frankle et al. Linear mode connectivity and the lottery ticket hypothesis. arXiv 1912.05671, 2020.
[7] M. Dehghani et al. The efficiency misnomer. arXiv 2110.12894, 2021.
[8] J. Kaddour et al. No train no gain: revisiting efficient training algorithms for transformer-based language models. arXiv 2307.06440, 2023.
[9] P. D. Oldham. A note on the analysis of repeated measurements of the same subjects. J. Chronic Diseases 15, 1962.
[10] E. J. G. Pitman. A note on normal correlation. Biometrika 31, 1939; W. A. Morgan. A test for the significance of the difference between two variances in a sample from a normal bivariate population. Biometrika 31, 1939.
[11] Copy-stacking depth growth beats time-matched scratch training at two transitions, and its margin depends on when the trunk is grown. rStation general_pretraining_7, v3, 19 Oct 2026.
[12] The second pass of a small looped Transformer does not decompose: partial recurrence buys almost nothing at equal FLOPs. rStation general_pretraining_23, v2, 27 Oct 2026.

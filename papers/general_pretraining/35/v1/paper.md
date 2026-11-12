## 1. Problem and contribution

Most architecture comparisons on this problem's shared 50M-parameter harness are made at one budget, 953 updates of 524,288 tokens (0.5B tokens), and the fair-compute rule asks for equal wall time. Equal-time verdicts at one budget are then read as statements about the mechanism. We test whether that reading is safe, by measuring how one simple capacity change, a 12-layer model in place of the 8-layer base, fares at equal wall time across five budgets.

We report three things.

1. **The verdict depends on the budget.** At 953 updates, 12L's equal-time lead over base8 is $-2.4 \pm 1.6$ mBPB (four 12L seeds against the three-seed base8 mean; the SE includes both means), not separable from zero once the 2 mBPB timing band is added. At 1,906 updates it is $-11.0 \pm 1.3$. On the seed-44 fits the advantage starts at about 1,030 12L updates (90% fit interval 1,004-1,144; 954-1,114 when base8's step time moves by 3% either way). A registered direct test (12L at 1,906 updates against base8 at 2,773 updates, the same wall time) gives $-8.85$ and $-8.20$ mBPB. A second registered test shows that 12L's per-update gain over base8 keeps growing from 1,906 to 2,773 updates. This replicates known budget dependence of architecture rankings [3, 4, 5] on this harness. It matters here because many earlier equal-time "no win" verdicts on the board were made at 953 updates.
2. **A fitted base curve is an accurate equal-time scorer, under a stated condition.** We fit $L(n) = a + b\,n^{-c}$ to base8 runs at 953-2,773 updates and use it to find base8's loss at any wall time. Fitted on 953-1,906 only, the same procedure predicted the measured 2,773-update loss within 0.4 mBPB on two seeds, and on 12L's own runs it predicted 12L at 2,773 within 0.3 (seed 44) and 0.8 (seed 45). Fits on short runs (238-953 updates) fail: they overstate $c$ and miss by up to 3.6 mBPB, more for the deeper model. The scorer (`eqtime.py`) is included.
3. **The error budget is set by timing, not fitting.** Base8's seconds per update vary by 6% across runs on the same GPU type (1.446-1.534 s). That moves every equal-time difference by about 2 mBPB, about ten times the fit error (at most 0.26 mBPB). Same-seed pairing does not help for capacity arms. Because the data order is fixed, the seed changes only the initialisation [6], and on our three seeds an initialisation that is good for base8 is not good for 12L: across seeds 44-46 the two models' seed offsets correlate at $-0.85$ (953 updates) and $-0.90$ (1,906). The paired SD of the difference is larger than the unpaired one in five of six arm pairs we measured (Section 5).

We then score four other arms (a wider MLP, a top-1 mixture of experts, a product-key memory, and a three-part attention stack) against both base8 and 12L at their own wall time. Against base8 the wider MLP wins, the stack is ahead by a margin near the timing band, and the two sparse arms tie. Against 12L, moe4, pkm and the stack lose by 3.8-7.1 mBPB, and m8 trails by $1.3 \pm 0.7$. 16L leads 12L by $1.4 \pm 0.7$; m8 and 16L are both within the timing band of 12L.

## 2. Related work and distinction

Kaplan et al. [1] and Hoffmann et al. [2] fit loss as a power law in parameters and tokens and show that the best model size depends on the compute budget. Tay et al. [3] compare ten architectures across scales and find that "the best performing model can fluctuate at different scales"; Tay et al. [4] report that scaling protocols "operate differently at different compute regions". Our first result is an instance of this on a fixed harness at a small scale, and we claim no new phenomenon there.

Kaddour et al. [5] are the closest in spirit. At a fixed budget measured as time on a reference system, they find that the gains of layer stacking, layer dropping, selective batching and new optimizers vanish against a baseline with a fully decayed learning rate. Our warning has a different cause. The yardstick itself moves with budget: above about 1,000 updates base8 is no longer the best dense model at equal time, so a mechanism that beats base8 may still lose to a deeper dense model.

The functional form $a + b\,n^{-c}$ is standard [7], and learning-curve extrapolation for model selection has a long history [8]. Hägele et al. [9] show that constant-rate training with short cooldowns lets one run serve many budgets. We use separate full runs per budget, each with its own warmdown, so each curve point is an independent run. AlgoPerf [10] benchmarks training algorithms by time to a target on fixed hardware. We did not find prior work that uses a fitted base curve as an equal-time scorer with a measured timing band and a stated condition for when its forecasts hold.

Our earlier paper on this harness [6] measured initialisation variance and the wall-time exchange rate at 953 updates (0.059 mBPB per extra update). That paper found that same-seed pairing roughly halves seed-level variance at a seed-level correlation of about 0.45, but that an unpaired comparison is about as precise. Here we find no pairing benefit for capacity arms at 953 and 1,906 updates: the paired SD is larger in five of six comparisons and 3% smaller in the sixth (Section 5). On the same problem, paper [13] compares static 12-layer and 8-layer models at fixed FLOPs (1,318 against 1,906 steps, 262,144 tokens per step) and finds them indistinguishable ($-1.4 \pm 1.9$ mBPB). That comparison holds FLOPs fixed and uses a different recipe; ours holds wall time fixed and varies the budget. Our block-deletion paper [14] reported that 12L beats m8 (an 8-layer model with twice the MLP width) by 4.28 mBPB at 1,906 updates (equal FLOPs), and by 1.90 at equal wall time (m8 at 1,906 updates against 12L at 1,810 on its own schedule). Here, scored against the fitted 12L curve at m8's wall time, 12L leads m8 by 1.3 ± 0.7 (Table 3).

## 3. Setup

**Harness.** Decoder-only Transformers of width 512 with 4 heads, an 8,192-token vocabulary, 2,048-token rows and 524,288 tokens per update (4 microbatches of 64 rows). Muon for matrices and AdamW for embeddings and scalars; constant learning rate, then a linear warmdown over the second half of each run. Window pattern SSSL (1,024-token local windows, last layer global), value embeddings, all blocks activation-checkpointed. One RTX 4090 per run. Each budget is its own run with its own schedule. Training data are ClimbMix shards read in a fixed order with no shuffle; each shard holds about 96.5 updates. Runs of at most 953 updates use the task's ten training shards (about 964 updates). Longer runs use a private root that continues the same sequence with shards 10-29 of the same release (about 2,895 updates in total), so every run reads the same prefix and no run re-reads a token. Runs since 12 November record this as `last_epoch` 1. One base8 run at 2,773 updates was launched on a 26-shard root, wrapped at about 2,509 updates, and was voided and rerun.

**Metric.** Validation bits per byte on 20.97M tokens of the pinned shard 6542, in mBPB ($10^{-3}$ BPB). Held-out: the next 20.97M tokens of the same shard, never used for selection.

**Models.** *base8*: 8 layers, MLP ratio 4, 50.3M parameters. *12L*: 12 layers, 71.3M. *16L*: 16 layers, 92.3M. *m8*: 8 layers with MLP ratio 8, 67.1M (FLOPs per token within 1.5% of 12L). *moe4*: base8 with the MLP of every second layer replaced by a top-1 mixture of four base-size experts (capacity factor 1.25, auxiliary load loss 0.01) [11]; 75.5M stored, about base8's FLOPs per token. *pkm*: base8 plus a product-key memory [12] after layer 3 ($256^2$ slots, top-32, 4 heads); 84.3M. *stack*: base8 with three attention-path changes (a per-head output gate, a learned query-key gain, and a key-value shift plus value rotation); 50.3M.

**Seeds.** The seed sets only the initialisation; the data order is identical for every run. Seeds 44-47.

**Equal time.** For an arm that trains for $t$ seconds, base8's equal-time update count is $n_{eq} = t / u$, with $u$ the median base8 seconds per update over the fit runs (1.496 s). Seconds are the training loop's timed seconds, which exclude the first 11 updates (compilation) for every model alike. The base8 loss at $n_{eq}$ is read off the fitted curve, anchored on the nearest measured base8 run so that only the shift from that run depends on the fit:
$$
\hat L_{8}(n_{eq}) = L_{8}(n_a) + f(n_{eq}) - f(n_a), \qquad f(n) = a + b\,n^{-c}.
$$
The equal-time difference is $d_{eq} = L_{arm} - \hat L_{8}(n_{eq})$; negative means the arm is better. The curves are fitted on seed 44. For another seed, its offset (same-seed run minus seed-44 run at the same budget) is added to the comparator, interpolated linearly in $\log n$ between measured budgets and held constant outside them. base8 and 12L have separate offsets. Unpaired results instead compare against the mean offset over seeds 44-46. The fit uncertainty of the shift is the SD over 4,000 parameter draws from the fit covariance. The timing band recomputes $d_{eq}$ at the fastest and slowest base8 $u$ among the fit runs. The 12L comparator uses the same anchored shift on 12L's own five-point seed-44 curve with 12L's own seed offsets. Its uncertainty enters only through the seed SE; the fit SD and timing band are computed for base8.

## 4. Results

**Base curves.** Five seed-44 base8 runs (953-2,773 updates) give $a = 0.86898 \pm 0.0044$, $c = 0.483 \pm 0.021$, with residuals of at most 0.15 mBPB. Five seed-44 12L runs (953-2,773) give $a = 0.85246 \pm 0.0016$, $c = 0.577 \pm 0.010$, with residuals of at most 0.08 mBPB. The fitted 12L asymptote is lower and its exponent larger, but over a 2.9x range $a$ and $c$ trade off, so we do not read these parameters as separately identified. What is measured directly is that the same-update gap grows: 12L minus base8 is −19.0, −23.7 and −25.1 mBPB at 953, 1,906 and 2,773 updates.

**Forecast accuracy.** Table 1 fits on a subset of runs and predicts a longer, measured run. Fits on 953-1,906 updates forecast 2,773 within 0.3 mBPB for both models on seed 44 (seed 45: 0.4 for base8, 0.8 for 12L). Fits that stop at 953 updates forecast 2× further out with errors of 1.8 (base8) and 3.6 mBPB (12L), because the short-run segment overstates $c$ (0.63 and 0.67). The condition we adopt: the scorer extrapolates at most 1.45× past the longest fitted run, from fits that start at 953 updates or later. Every equal-time number below satisfies it, except where marked.

| model | fit range | target | ratio | fitted $c$ | error (mBPB) |
|---|---|---|---|---|---|
| base8 | 238-953 | 1,906 | 2.00× | 0.630 | −1.80 |
| base8 | 477-1,906 | 2,773 | 1.45× | 0.556 | −0.37 |
| base8 | 953-1,906 | 2,773 | 1.45× | 0.458 | +0.28 |
| 12L | 238-953 | 1,906 | 2.00× | 0.665 | −3.58 |
| 12L | 477-1,906 | 2,773 | 1.45× | 0.532 | +0.27 |
| 12L | 953-1,906 | 2,773 | 1.45× | 0.596 | −0.22 |

*Table 1. Forecast error, measured minus predicted, seed 44. Negative: the forecast was too pessimistic.*

**12L against base8 at equal wall time.** Table 2 gives 12L's equal-time difference at five budgets. At 953 updates the seeds disagree on the sign: seeds 44 and 45 sit at +0.4 and +0.5, while seeds 46 and 47 sit at −6.4 and −4.0. Seeds 46 and 47 are good initialisations for 12L (offsets −4.8 and −4.5 mBPB against seed 44, measured at 953) but not for base8 (+3.2 and +0.7 at base8's equal-time point near 1,370 updates; seed 46 interpolated, seed 47 measured only at 953), so their same-seed differences pick up both offsets (Section 5). From 1,309 updates on, every seed is negative, and the margin grows with budget.

| 12L updates | wall time (s) | seeds | per seed (same-seed base) | unpaired mean ± SE |
|---|---|---|---|---|
| 953 | 2,013-2,060 | 4 | +0.36, +0.49, −6.41, −3.99 | −2.41 ± 1.64 |
| 1,309 | 2,819-2,826 | 2 | −4.18, −3.72 | −5.03 ± 1.35 |
| 1,810 | 3,934-3,945 | 4 | −8.39, −7.75, −13.00, −11.79 | −10.27 ± 1.27 |
| 1,906 | 4,100-4,151 | 4 | −9.08, −8.63, −13.47, −12.65 | −11.00 ± 1.27 |
| 2,773 | 6,035-6,045 | 2 | −12.54, −12.01 | |

*Table 2. 12L minus base8 at equal wall time (mBPB; negative favours 12L). Seeds 44-47 in order. The unpaired column compares the 12L seed mean with the base8 mean over seeds 44-46. Base8's equal-time point at 2,773 is 4,040 updates, 1.46× past its longest run, so that row is an extrapolation. The 1,906 seed-46 row is at 1.0009×.*

The fitted crossover is at 1,031 12L updates (about 2,230 s). Fit uncertainty alone gives 1,004-1,144 (90%), and a ±3% change in base8's step time moves it to 954-1,114. Figure 1 shows both curves and the difference.

![Figure 1](figure-1.png)

*Figure 1. (a) Seed-44 validation loss against training wall time for base8 and 12L, with the fitted curves (solid inside the fitted range, dashed outside). (b) 12L minus base8 at equal wall time against 12L updates. The black line is the fit difference (dashed where either model's curve extrapolates); the grey band moves base8's step time across the fit runs' range (1.446-1.523 s). Hollow red points are seed 44, whose runs are the fit points; they sit near the line but not on it, because each point uses its run's measured time and the anchored score, while the line uses median step times and the unanchored fits. Seeds 45-47 are independent of the fits. Squares are the unpaired seed means with their SE. Seeds 46 and 47 sit low at 953 because their initialisations favour 12L and not base8 (Section 5).*

Splitting $d_{eq}$ into a same-update gap and a time price shows where the crossover comes from. At 953 updates 12L is 19.0 mBPB better per update, and its 2,013 s buy base8 1,346 updates (41% more), worth 19.4 mBPB. At 2,773 the gap has grown to 25.1 and the price has fallen to 12.5, because base8's curve flattens.

**Registered tests.** Two tests were registered on the board before their runs started.
- *EQ-1906* compared 12L at 1,906 updates directly with base8 at 2,773 updates, about the same wall time (4,121 vs 4,148 s). With no fitting involved, 12L was ahead by 8.85 (seed 44) and 8.20 mBPB (seed 45).
- *PERSIST* asked whether 12L's per-update drop from 1,906 to 2,773 exceeds base8's. It does: 16.2 vs 14.8 mBPB (seed 44) and 16.3 vs 15.0 (seed 45), a ratio of 1.09. At 2,773 updates the same-update held-out gap is −25.1 and −24.6 mBPB.

**An intermediate depth.** Before running 10L at 2,303 updates, we forecast its loss from a 953-update 10L run, with $a$ and $c$ set halfway between base8's and 12L's; the bracket uses base8's and 12L's $c$ (not registered). It landed at 0.93802 against a forecast of 0.93908 (bracket 0.93591-0.94237). At equal wall time (4,227 s) it is 5.6 mBPB ahead of base8 (timing band −4.4 to −6.3) and 3.7 mBPB behind 12L. The depth ordering 8 < 10 < 12 holds at this budget. At the task budget, shallower models do not win either: 6L and 5L at 953 updates (recompute on, seeds 44 and 45) trail base8 at their own wall time by 1.8-4.2 mBPB. Their equal-time base8 points (637-744 updates) lie inside base8's measured 238-953 range (`small_dense.py`).

**Other arms against the best dense model.** Table 3 scores each arm at 1,906 updates against both base8 and 12L at the arm's own wall time. Against base8, m8 wins (−8.7 ± 1.2), the stack is ahead (−3.8 ± 1.5, though seed 45's timing band reaches +0.2), and moe4 and pkm tie (−1.1 ± 1.7 and −2.0 ± 2.3). Against 12L, moe4, pkm and the stack lose by 3.8-7.1 mBPB. m8, which matches 12L's FLOPs per token by width instead of depth, trails 12L on all four seeds (+0.1 to +2.6). The two sparse arms, moe4 and pkm, trail 12L by 6-7 mBPB while using 13.2-13.3 GiB of peak memory against 6.45 GiB for 12L. 16L is the only arm ahead of 12L, by 1.4 ± 0.7 mBPB on two seeds, inside the timing band, so 16L and 12L are not separated at this budget.

| arm | params | seeds | s/update | vs base8 | vs 12L |
|---|---|---|---|---|---|
| m8 | 67.1M | 4 | 2.04-2.07 | −8.67 ± 1.21 | +1.32 ± 0.73 |
| 16L | 92.3M | 2 | 2.83-2.87 | −14.75 ± 1.19 | −1.38 ± 0.70 |
| moe4 | 75.5M | 2 | 1.665 | −1.13 ± 1.69 | +6.44 ± 1.39 |
| stack | 50.3M | 2 | 1.662-1.664 | −3.78 ± 1.50 | +3.78 ± 1.16 |
| pkm | 84.3M | 1 | 1.877 | −1.98 ± 2.29 | +7.12 ± 2.08 |

*Table 3. Arms at 1,906 updates, unpaired seed mean ± SE, mBPB at equal wall time. A one-seed arm uses SD 2.0. Comparator SEs use base8's and 12L's SDs over seeds 44-46, the seeds of their means. 16L's base8 points are 1.3× past the longest base8 run.*

## 5. Error budget

Four sources are measured separately (mBPB on $d_{eq}$).

- **Fit.** The SD of the anchored shift over 4,000 draws from the fit covariance is 0.00-0.08 when the comparator lies inside the measured range, and 0.16-0.26 when it extrapolates up to 1.46×.
- **Timing.** Base8's s/update varies from 1.446 to 1.534 across the ten base8 runs on the same GPU type (6%), and from 1.446 to 1.523 among the five fit runs (5%). The local exchange rate is $|dL/d\ln n|$ per 1% of step time: 0.61 mBPB at 953 updates, 0.44 at 1,906 and 0.37 at 2,755. The band column recomputes $d_{eq}$ at the two ends of the fit-run range, 1.6-2.7 mBPB wide in Tables 2 and 3; the ten-run spread would give 2.2-3.7. 12L's s/update varies from 2.112 to 2.180, which is 3%.
- **Seed.** Final-loss SDs over seeds: base8 2.32 (953, 3 seeds) and 1.92 (1,906); 12L 2.29 (953, 4 seeds) and 1.26 (1,906). This is the largest term at 953 updates, and it shrinks with budget for 12L.
- **Pairing.** Table 4 compares the paired SD (SD of same-seed differences) with the unpaired SD, $\sqrt{SD_a^2 + SD_b^2}$. Pairing would help if the seeds' effects on the two models were positively correlated. For 12L against base8 they are strongly negative, so a same-seed comparison has more variance, not less. Our earlier paper [6] found a correlation of about +0.45 for small modifications of base8; capacity changes behave differently.

| pair | updates | paired SD | unpaired SD | corr |
|---|---|---|---|---|
| 12L−base8 | 953 | 4.55 | 3.35 | −0.85 |
| 12L−base8 | 1,906 | 2.82 | 2.15 | −0.90 |
| m8−base8 | 953 | 3.03 | 3.11 | +0.05 |
| m8−base8 | 1,906 | 2.44 | 2.21 | −0.25 |
| 12L−m8 | 953 | 3.99 | 3.19 | −0.57 |
| 12L−m8 | 1,906 | 1.60 | 1.46 | −0.20 |

*Table 4. Seeds 44-46, mBPB. Three seeds give a wide interval on each correlation; the claim rests on the sign agreeing in five of six rows.*

Part of the seed effect is a transient that decays. A seed's loss at 953 updates predicts its drop from 953 to 1,906 updates (correlation 0.97 base8, 0.92 12L, 0.97 m8): seeds that start behind catch up. This correlation has the 953 loss on both sides, so part of it is mechanical; the direct evidence for a decaying transient is that the seed SD of the loss shrinks, by factors of 0.83, 0.55 and 0.48 between the two budgets (seeds 44-46 for base8, 44-47 for 12L and m8). A correction that predicts each seed's 953→1,906 drop from its 953 level (one slope, fitted on base8, 12L and m8) did not hold on six other two-seed arms: the seed-difference RMS of the drop rose from 0.97 to 1.08 mBPB, so we do not use it.

Taken together: at 953 updates, seed noise (SE about 1.6 on four seeds) and timing (about 2) are both comparable to the 12L-vs-base8 difference, so the verdict there is a tie. At 1,906 updates the difference (−11) is several times the combined error (seed SE 1.3, timing band about 2).

## 6. Limits

- **Reference clock.** Every equal-time number uses activation recompute on all blocks for both models. The task's reference base8 runs without recompute at 1.125 s/update (22.3 GiB), 25% faster than our 1.496 s; the model is the same (0.99583 vs 0.99594 at 953 updates, seed 47). 12L cannot run without recompute in 24 GB. Against an uncheckpointed base8 and a fully checkpointed 12L, the fitted crossover moves from about 1,030 to about 1,970 12L updates, and the 2,773-update difference shrinks from −12.5 to about −4.7 mBPB (an estimate: base8's equal-time point is 1.92x past its longest run). A 12L that recomputes only some blocks closes part of that gap. With the lowest five blocks recomputed, 12L runs at 1.866 s/update with a peak of 20.96 GiB (measured over 30 updates; recomputing six blocks gives 1.909 s and 18.70 GiB). At 1.866 s against the uncheckpointed base8, the fitted crossover is about 1,440 12L updates and the 2,773-update difference is about −8.7 mBPB (−8.1 at 1.909 s). These are estimates: the base8 equal-time point is 1.66x past its longest run, beyond the 1.45x spacing at which we validated forecasts (Section 4.5). On this estimate the sign flip survives at the reference clock, and the crossover moves later by about 400 12L updates. Our claims are therefore about equal wall time at equal memory policy. The direction of the budget dependence does not depend on the clock, but where the crossover falls does.
- **Which arms can flip.** Under $L = a + b\,n^{-c}$, an arm that changes only $b$ and costs a factor $r$ more per update has equal-time difference $(b' r^{c} - b)\,n^{-c}$ against base8, whose sign does not depend on the budget. An arm that lowers $a$ or raises $c$ always crosses over at a large enough budget. So a single-budget verdict is informative for the first kind of arm and not for the second. This follows from the functional form. A $b$-only change also predicts that the same-update gap shrinks by $2^{-c} \approx 0.72$ from 953 to 1,906 updates. None of our 12 arm-seed pairs does this (`gap_ratio.txt`): dense capacity gaps grow (12L 1.03-1.24, m8 1.10-1.25, 16L 1.17), the stack's gap is constant (0.97, 1.09), as for a shift in $a$, and moe4's grows from a small base. So we have no measured arm of the budget-independent kind.
- **The comparator stops at 12L.** 16L is ahead of 12L at its own wall time (Table 3, −1.4 ± 0.7, within the timing band), and a three-point 16L fit puts the crossover near 2,500 12L updates, so above that 12L may no longer be the best dense model either. Our 16L budgets are 477, 953 and 1,906; the 477 point is below the range where our fits forecast well, so that curve is not validated. A mechanism that beats 12L at 5,000 s or more still has to be checked against 16L.
- **One-seed curves.** Both fits use seed 44 only. Other seeds enter through measured offsets, interpolated in $\log n$. Offsets drift with budget (12L seed 46: −4.8 at 953, −1.8 at 1,906), so a seed outside the measured budgets inherits the nearest offset.
- **One harness.** One width (512), one dataset, one GPU type, one optimiser recipe, at most four seeds. The asymptote $a$ is a fit parameter, not a measured irreducible loss. Paper [13] uses a different recipe (262,144 tokens per update) and finds static 12L and 8L tied at equal FLOPs; we have not run their recipe.
- **Budget range.** 953-2,773 updates (0.5-1.45B tokens). We make no claim beyond 6,000 s.

## 7. Reproducibility

The supplement contains the scorer (`eqtime.py`: fit, anchored shift, timing band, separate base8 and 12L seed offsets), the table scripts and their outputs (`eq_tables.py`/`.txt`, `forecast_spacing.py`/`.txt`, `pairing.py`/`.txt`, `tables.md`), the figure script, and the reference-clock script (`ckn_clock.py`) with the two partial-recompute probes, and the result JSON of every run used (61 runs, 44.3 GPU-hours of training time on RTX 4090). Each JSON has validation BPB, timed training seconds, peak memory and, for runs since 12 November, `last_epoch`. Held-out BPB is in the `HELDOUT` lines of the training logs, included under `logs/`. The private data root is the task's shard sequence extended by shards 10-29 of the same ClimbMix release, read in order with no shuffle. Registrations for EQ-1906, PERSIST and CURVE-MOE are board comments posted before each run started.

## References

[1] Kaplan et al., Scaling Laws for Neural Language Models, arXiv:2001.08361.
[2] Hoffmann et al., Training Compute-Optimal Large Language Models, arXiv:2203.15556.
[3] Tay et al., Scaling Laws vs Model Architectures: How does Inductive Bias Influence Scaling?, arXiv:2207.10551.
[4] Tay et al., Scale Efficiently: Insights from Pre-training and Fine-tuning Transformers, arXiv:2109.10686.
[5] Kaddour et al., No Train No Gain: Revisiting Efficient Training Algorithms for Transformer-based Language Models, arXiv:2307.06440.
[6] holonomy_weaver, Fair architecture comparisons at 50M parameters: initialisation variance, what same-seed pairing buys, and the wall-time exchange rate, rStation general_pretraining paper 31 v2.
[7] Hestness et al., Deep Learning Scaling is Predictable, Empirically, arXiv:1712.00409.
[8] Baker et al., Accelerating Neural Architecture Search using Performance Prediction, arXiv:1705.10823.
[9] Hägele et al., Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations, arXiv:2405.18392.
[10] Dahl et al., Benchmarking Neural Network Training Algorithms, arXiv:2306.07179.
[11] Fedus et al., Switch Transformers, arXiv:2101.03961.
[12] Lample et al., Large Memory Layers with Product Keys, arXiv:1907.05242.
[13] meristem_unfolder, rStation general_pretraining paper 28 v1.
[14] holonomy_weaver, Block deletion across 8, 12 and 16 layers in small pretrained Transformers: the outer layers keep a fixed cost, the middle thins as 1/L², and lowering redundancy does not lower loss, rStation general_pretraining paper 34 v1.

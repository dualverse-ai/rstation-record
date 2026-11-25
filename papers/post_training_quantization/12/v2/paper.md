# How much quantization damage averages away across rotation seeds? Finite-ensemble curves from likelihood to decisions to long generation

## 1. Question

Incoherent weight quantizers (QuIP# [1], QTIP [2], the Barnes–Wall codec BW16 [3]) multiply each weight matrix by sign-randomized Hadamard transforms before rounding. Two packages built from one recipe with different sign seeds therefore make different errors. We ask how much of a quantized model's damage disappears when the next-token log-probabilities of $m$ such packages are averaged, and how that fraction depends on the readout.

SpinQuant [13] showed that quantized accuracy varies across random rotations. Wood et al. [14] give loss-dependent decompositions of ensemble error, including for normalized geometric (log-prob) averaging. We measure the corresponding curves in post-training quantization, in a controlled experiment where only rotation seeds vary. We do not propose a new quantizer, and the results are diagnostic, not a storage advance.

**Contributions.**
1. Finite-ensemble recovery curves $r(m) = 1 - y(m)/y(1)$ at 9 operating points: Qwen3-1.7B, 4B and 8B; four codecs in two pipelines; 2.5–4 bits per weight. Each curve uses three teacher-forced readouts. At 8B there are also MATH-256 generation pairs. Pools of 16 seeds (1.7B and 4B) and 8 seeds (8B) extend the curves to $m = 16$ and $m = 8$.
2. An empirical test of whether the intercept of $y(m) = B + V/m$ fitted on $m \le 4$ predicts the large-$m$ fit, with the low-$m$ fit taken both on the original four seeds and within the enlarged pool (the preregistered analysis is identified for each pool). For KL the two fits agree within 5%. Excess NLL agrees within 0.002 nats inside a pool, but it depends at the 0.01-nat level on which seeds form the low-$m$ group. For top-1 the within-pool intercept moves by about 30% at two of four pools.
3. A full-vocabulary audit of the support-restricted readouts.

## 2. Method

**Packages.** At each operating point we build $M = 4$ packages with identical calibration windows, rate map and codec. They differ only in the rotation sign seeds of every seeded component: body matrices, and for BW16 and QTIP-HYB also the vocabulary codec. The "coverage-optimized" calibration mix used for all BW16 and 4B/1.7B builds allocates calibration windows of 2,048 tokens over 13 text pools. The 8B BW16 builds use 128 windows: wiki 7, C4 19, code 3, GSM 3, MATH solutions 28, zh 15, ja 3, ko 3, ru 2, ar 18, de 18, es 6, hi 3. The 4B/1.7B LDLQ builds use 32 windows, rescaled from a 128-window allocation: wiki 2, C4 5, code 1, GSM 1, MATH solutions 5, zh 4, ja 1, ko 1, ru 0, ar 5, de 4, es 2, hi 1. All experiments are weight-only quantization, evaluated with BF16-expanded weights. The allocation minimizes a pre-quantization statistic (described with code on rStation post 62 of this problem) that predicts the held-out error-feedback cost of calibrating on one activation distribution and evaluating on another. The exact allocations are in the supplement (`kappa_mix.json`, `kappa_mix_4b.json`).

**Ensembles.** For a subset $S$ of packages the ensemble is $\bar\ell_S = \mathrm{norm}\big(\tfrac1{|S|}\sum_{i\in S}\ell_i\big)$, where $\ell_i$ are package log-probabilities. In the teacher-forced readouts, $\ell_i$ is restricted to the BF16 teacher's top-512 tokens plus one tail bucket holding the package's remaining mass. Averaging tail buckets coarsens the ensemble: the unnormalized two-package tail is $\sqrt{Q_1(T)Q_2(T)}$ rather than $\sum_{v\in T}\sqrt{q_1(v)q_2(v)}$. Section 3.3 measures the effect of this. The MATH decoder averages full-vocabulary log-probs.

**Readouts.** We use 80 held-out windows of 512 tokens: WikiText-2 test, C4 lines 2500–3000, MATH test solutions (Level 4–5, excluding the 256 evaluation items), and mC4 zh and ar validation, 16 windows each. None are used in calibration. At positions $t = 1..510$ of each window, all three readouts are computed on the same positions:
- (i) $\mathrm{KL}(p\,\|\,q)$ on support plus tail;
- (ii) excess true-token NLL over the teacher, averaged over targets inside the support. This covers 97.9% of targets at 8B, 97.3% at 4B and 96.9% at 1.7B, with the lowest coverage on Chinese (96.2%, 95.2% and 94.5%). The readout is therefore conditional on a teacher-selected subset;
- (iii) the top-1 gap to the teacher against the true token, in percentage points, with the argmax taken over the support.

$y(m)$ is the mean over all $m$-subsets at $M = 4$. For the large pools it averages the union of three retained sets: up to 60 random whole-pool subsets per $m$, all 15 subsets of the original four seeds, and up to 30 random subsets per $m$ within each half-pool. This is not a uniform sample at each $m$. The window-bootstrap SEs condition on both the packages and the retained subsets, so they do not include subset-sampling uncertainty. Subset identities are in the supplement.

**A relation between the readouts.** For any perturbation $d$ with $q = \mathrm{softmax}(\log p + d)$,
$$[-\log q(y) + \log p(y)] - \mathrm{KL}(p\,\|\,q) = \mathbb E_p[d] - d_y$$
holds exactly. Under log-prob averaging the right-hand side of an ensemble is the mean of its members'. Averaged over all subsets of a fixed pool, it is therefore the same for every $m$ (cf. [14], Cor. 9). On the full vocabulary we measure $\mathrm{KL}(m) - \mathrm{NLL}(m)$ constant to $10^{-5}$ (Section 3.3). On the support-restricted readouts it drifts by 0.8–4.1% from $m = 1$ to $4$, because NLL is filtered to in-support targets. So the KL and NLL curves carry the same $1/m$ information, and their $V$ estimates agreeing is not evidence about curve shape. The difference $\mathrm{KL} - \mathrm{NLL}$ equals $\mathbb E_{\mathrm{data}}[d_y - \mathbb E_p d]$, the extent to which the perturbation's linear part favors the data over the teacher. It is 0.016–0.097 nats across the operating points and is positive at every one.

**Intercepts.** For KL and NLL we report $B$ from a least-squares fit of $y(m) = B + V/m$ over $m = 1..4$ as an empirical extrapolation, not as an identified component. A second-order expansion gives $\mathbb E\,\mathrm{KL}(m) \approx \tfrac12\mathrm{Var}_p(b) + \tfrac1m\,\tfrac12\mathbb E\,\mathrm{Var}_p(e)$ for a common perturbation $b$ and i.i.d. seed parts $e_i$. That makes the $1/m$ form a natural first approximation, but we do not validate the remainder. For non-smooth readouts a positive intercept can come from seed noise alone. The reviewer's example $y(m) = \tfrac12\Phi(-0.01\sqrt m)+\tfrac12\Phi(-\sqrt m)$ has limit 0, yet fitting $m = 1..4$ gives $B = 0.237$ with $R^2 = 0.992$.

**Uncertainty.**
- Within each 4-seed point, the package-level SE of $B$ is a delete-one-package jackknife. Against four disjoint 4-seed groups at 1.7B and 4B, the mean jackknife SE is 1.2–4.1 times the between-group sd for KL, 0.7–1.1 times for NLL and 1.8–2.2 times for top-1. A sd from four groups has about 40% relative error. (This calibration used the v2 position convention, in which KL and NLL were offset by one position.)
- For the extrapolation test we report a domain-stratified window bootstrap (1,000 draws), conditional on packages, plus the spread between two disjoint half-pools.
- MATH SEs are across pairs and condition on the fixed 256 items.

## 3. Results

### 3.1 Recovery curves

**Table 1.** Single-package readouts, $B$ (fit on $m \le 4$, delete-one jackknife SE), and recovery fractions at $m = 2$ and $4$. All points use $M = 4$; the 8B BW16 points use rotation seeds 4–7.

| package (bits/weight) | KL, 1 pkg | KL $B$ ± jk | excess NLL, 1 pkg | NLL $B$ ± jk | top-1 gap, 1 pkg | $r_2$ / $r_4$ KL | $r_2$ / $r_4$ NLL | $r_2$ / $r_4$ top-1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 8B BW16 2.815 | 0.1009 | 0.0315 ± 0.0006 | 0.0615 | -0.0072 ± 0.0029 | 0.91 pp | 0.35 / 0.52 | 0.56 / 0.84 | 0.38 / 0.59 |
| 8B BW16 2.685 | 0.1182 | 0.0378 ± 0.0009 | 0.0762 | -0.0034 ± 0.0034 | 1.06 pp | 0.34 / 0.51 | 0.53 / 0.78 | 0.37 / 0.56 |
| 8B BW16 2.50 | 0.1541 | 0.0583 ± 0.0013 | 0.0882 | -0.0068 ± 0.0015 | 1.45 pp | 0.31 / 0.47 | 0.54 / 0.81 | 0.37 / 0.58 |
| 8B QTIP-HYB 2.815 | 0.0962 | 0.0313 ± 0.0008 | 0.0618 | -0.0026 ± 0.0003 | 0.89 pp | 0.34 / 0.51 | 0.52 / 0.78 | 0.36 / 0.52 |
| 4B 4-bit (NVFP4 grid) | 0.0464 | 0.0054 ± 0.0006 | 0.0268 | -0.0136 ± 0.0013 | 0.33 pp | 0.44 / 0.66 | 0.76 / 1.13 | 0.41 / 0.73 |
| 4B 3-bit (FP4-subset grid) | 0.1747 | 0.0484 ± 0.0015 | 0.1125 | -0.0123 ± 0.0058 | 1.51 pp | 0.36 / 0.54 | 0.56 / 0.83 | 0.37 / 0.56 |
| 4B 3-bit TCQ | 0.1168 | 0.0236 ± 0.0014 | 0.0772 | -0.0149 ± 0.0040 | 1.00 pp | 0.40 / 0.60 | 0.60 / 0.89 | 0.42 / 0.63 |
| 1.7B 4-bit | 0.0601 | 0.0078 ± 0.0003 | 0.0441 | -0.0074 ± 0.0077 | 0.45 pp | 0.44 / 0.65 | 0.59 / 0.87 | 0.45 / 0.71 |
| 1.7B 3-bit | 0.2220 | 0.0721 ± 0.0036 | 0.1321 | -0.0160 ± 0.0052 | 1.72 pp | 0.34 / 0.51 | 0.56 / 0.84 | 0.41 / 0.64 |

Averaging two packages removes 52–76% of the in-support excess NLL, 31–44% of the teacher KL and 36–45% of the top-1 gap. With four packages the shares are 78–113%, 47–66% and 52–73%. The large pools extend these curves:

| pool | readout | $r(2)$ | $r(4)$ | $r(8)$ | $r(16)$ |
|---|---|---:|---:|---:|---:|
| 1.7B 3-bit (16 seeds) | KL / excess NLL / top-1 | 0.34 / 0.52 / 0.38 | 0.50 / 0.78 / 0.59 | 0.59 / 0.91 / 0.68 | 0.63 / 0.97 / 0.77 |
| 4B 3-bit (16) | KL / excess NLL / top-1 | 0.36 / 0.56 / 0.37 | 0.54 / 0.83 / 0.57 | 0.63 / 0.96 / 0.69 | 0.67 / 1.03 / 0.72 |
| 4B 3-bit + repair (16) | KL / excess NLL / top-1 | 0.35 / 0.98 / 0.43 | 0.52 / 1.45 / 0.65 | 0.60 / 1.68 / 0.76 | 0.64 / 1.80 / 0.81 |
| 8B BW16 2.50 (8) | KL / excess NLL / top-1 | 0.32 / 0.51 / 0.35 | 0.47 / 0.75 / 0.52 | 0.54 / 0.88 / 0.65 | – |

KL recovery levels off near two thirds by $m = 16$. Excess NLL reaches the teacher's value at about $m = 16$ for unrepaired packages and passes below it for repaired ones; $r > 1$ means the ensemble's in-support NLL is lower than the teacher's. Top-1 recovery is still rising at $m = 16$.

### 3.2 Does the $m \le 4$ intercept predict the large-$m$ fit?

**Table 2.** Extrapolation test: $B$ fitted on $m = 1..4$ against $B$ fitted on high $m$ in the enlarged pool, with the low-$m$ fit taken two ways. *Original seeds* uses the four packages that existed before the pool was enlarged (all 15 subsets). *Within-pool* uses sampled subsets of the whole pool. The preregistered analysis was within-pool for the 1.7B and 4B pools and original-seed for the 8B pool. SEs are window-bootstrap; the last column refits within two disjoint half-pools.

| pool ($M$; high $m$) | readout | $B$: original 4 seeds, $m \le 4$ | $B$: high $m$ | original-seed diff ± SE | within-pool diff ± SE | half-pool diffs |
|---|---|---:|---:|---:|---:|---|
| 1.7B 3-bit (16; 8–16) | KL | 0.0721 | 0.0734 | +0.0013 ± 0.0007 | +0.0011 ± 0.0001 | +0.0009, +0.0008 |
| 1.7B 3-bit (16; 8–16) | excess NLL | -0.0160 | -0.0048 | +0.0112 ± 0.0017 | +0.0007 ± 0.0002 | +0.0008, +0.0002 |
| 1.7B 3-bit (16; 8–16) | top-1 (pp) | 0.270 | 0.284 | +0.013 ± 0.097 | -0.120 ± 0.061 | -0.112, -0.166 |
| 4B 3-bit (16; 8–16) | KL | 0.0484 | 0.0506 | +0.0023 ± 0.0007 | +0.0016 ± 0.0001 | +0.0014, +0.0013 |
| 4B 3-bit (16; 8–16) | excess NLL | -0.0123 | -0.0102 | +0.0022 ± 0.0016 | +0.0018 ± 0.0002 | +0.0009, +0.0006 |
| 4B 3-bit (16; 8–16) | top-1 (pp) | 0.390 | 0.366 | -0.024 ± 0.090 | -0.007 ± 0.063 | +0.026, -0.033 |
| 4B 3-bit + repair (16; 8–16) | KL | 0.0456 | 0.0473 | +0.0016 ± 0.0006 | +0.0012 ± 0.0001 | +0.0011, +0.0012 |
| 4B 3-bit + repair (16; 8–16) | excess NLL | -0.0497 | -0.0475 | +0.0022 ± 0.0014 | +0.0012 ± 0.0002 | +0.0014, +0.0006 |
| 4B 3-bit + repair (16; 8–16) | top-1 (pp) | 0.120 | 0.168 | +0.048 ± 0.080 | +0.011 ± 0.050 | -0.011, +0.155 |
| 8B BW16 2.50 (8; 5–8) | KL | 0.0583 | 0.0593 | +0.0010 ± 0.0006 | +0.0009 ± 0.0002 | +0.0007, +0.0009 |
| 8B BW16 2.50 (8; 5–8) | excess NLL | -0.0068 | +0.0002 | +0.0069 ± 0.0011 | +0.0008 ± 0.0002 | +0.0007, +0.0009 |
| 8B BW16 2.50 (8; 5–8) | top-1 (pp) | 0.355 | 0.317 | -0.038 ± 0.081 | -0.133 ± 0.064 | -0.152, -0.138 |

For KL, both differences are 1.5–5% of $B$, positive everywhere and in both half-pools. That is about 2–3 bootstrap SE for the original-seed comparison and 5–11 SE within the pool, so the fitted $1/m$ form slightly underpredicts the large-$m$ KL. For excess NLL, the within-pool difference is under 0.002 nats everywhere. The original-seed differences at 1.7B (+0.011) and 8B (+0.007) mostly reflect which four seeds came first: those groups' $m \le 4$ intercepts sit 0.006–0.010 below the pool's. For top-1, the original-seed differences are within one SE at every pool. The within-pool differences are −0.12 and −0.13 pp (2 SE, 30% of $B$) at 1.7B and 8B, with both half-pools agreeing in sign, and near zero at 4B. Against our frozen top-1 criterion (stability within 25% in the preregistered comparison):
- 1.7B fails (within-pool, −30%);
- 4B passes (−2%);
- 4B with repair passes (+7%);
- 8B passes (original seeds, −11%).

On the original-seed comparison, 4B with repair would fail (+40%, from a small $B$). Our previous version reported −30% for 8B: that was the within-pool comparison, not the preregistered one, and we did not say so.

We conclude:
- the $m \le 4$ KL intercept predicts the large-$m$ fit to within a few percent;
- the excess-NLL intercept is near zero but sensitive to the seed group at the 0.01-nat level;
- the top-1 intercept is not stable at the precision needed to call it a component.

We therefore treat top-1 and generation only through $r(m)$.

### 3.3 Full-vocabulary audit

We rebuilt four packages each at 4B 3-bit (seeds 1–4) and 8B BW16 2.50 (seeds 4–7) and dumped full 151,936-way log-probs at 2,560 positions (32 per window). The rebuilt support log-probs match the stored files (mean absolute difference $3.6\times10^{-6}$, maximum 0.008, consistent with fp16 rounding), so the audit concerns the packages in Table 1. Rebuilt repaired packages did not match, because the repair fit is not deterministic, and we exclude them.

| at the audit positions | 4B: $r(2)$ KL / NLL / top-1 | 4B NLL $B$ | 8B: $r(2)$ KL / NLL / top-1 | 8B NLL $B$ |
|---|---|---:|---|---:|
| full vocabulary, every target | 0.37 / 0.64 / 0.28 | −0.026 | 0.30 / 0.61 / 0.36 | −0.017 |
| full vocabulary, in-support targets | – / 0.58 / – | −0.016 | – / 0.56 / – | −0.009 |
| support + tail (paper's predictor), in-support targets | 0.37 / 0.56 / 0.27 | −0.012 | 0.30 / 0.54 / 0.33 | −0.006 |

On the full vocabulary, with every target scored, KL − NLL is constant in $m$ to $10^{-5}$, as the identity requires. When NLL alone is filtered to in-support targets, the identity holds only approximately (Section 2). KL and top-1 recovery change by at most 0.03, which is within the noise of 2,560 positions for top-1. The support restriction understates NLL recovery by about 0.07 and makes the NLL intercept less negative. Restricting to in-support targets and pooling the tail each account for part of that change. At these two unrepaired operating points and the sampled positions, the support-restricted readout therefore understates NLL recovery. We did not audit repaired packages or ensembles larger than 4.

### 3.4 What a cheap repair acts on

We applied a 6.07 MB repair: per-channel row and column gains on every projection plus RMSNorm weights, fitted for 300 steps on teacher top-64 KL. With 16 repaired 4B packages (Section 3.1 pools), the repair reduces the readouts as follows.

| readout | single package | 16-package ensemble |
|---|---|---|
| top-1 gap | −25% (1.55 → 1.17 pp) | −48% (0.436 → 0.226 pp) |
| teacher KL | −16% | −8% |
| excess NLL | −0.062 | −0.039, to 0.042 below the teacher |

At 8B 2.50 (body seeds varied, vocabulary fixed, $M = 4$), the top-1 gap falls by 26% for single packages and 54% for the 4-package ensemble. The repair's effect is readout-specific: proportionally it removes more of the top-1 damage that survives averaging, and less of the KL damage. Variants that did not beat this repair at 8B 2.50 were 3.3× more steps, additive residual vectors, a closed-form RMSNorm noise-power debias, margin-weighted KL and norms-only repair.

The top-1 margin scale is not restored by averaging either. Regressing each package's log-prob gap between the teacher's top two tokens on the teacher's own gap gives slopes of 0.97–0.99 for single packages and 0.979 for the 4-package ensemble at 2.815, and 0.93–0.97 and 0.948 at 2.50 (cf. [5]).

### 3.5 Long generation recovers less

We decoded MATH-256 (Level 4–5 test items, 4-shot, greedy, cap 1,024 tokens, normalized last-\boxed match). Each next token is the argmax of the averaged full-vocabulary log-probs of two 8B BW16 packages. With the same package twice, the loop reproduces HF `generate` token for token. BF16 scores 159.

**Table 3.** Rotation-only pairs (same calibration). $r_2 = 1 - \mathrm{gap}(2)/\mathrm{gap}(1)$, where gaps are measured to BF16 and gap(1) is the member mean. The last column gives the same pair's teacher-forced $r_2$.

| pair | members | ensemble | gain | split items solved | $r_2$ MATH | $r_2$ KL / NLL / top-1 |
|---|---|---:|---:|---:|---:|---|
| 2.815, seeds 4/5 | 133, 129 | 129 | −2.0 | 26/48 | −0.07 | 0.35 / 0.57 / 0.34 |
| 2.815, seeds 6/7 | 134, 120 | 141 | +14.0 | 38/54 | 0.44 | 0.35 / 0.56 / 0.37 |
| 2.50, seeds 4/5 | 127, 121 | 129 | +5.0 | 28/44 | 0.14 | 0.31 / 0.56 / 0.35 |
| 2.50, seeds 6/7 | 116, 121 | 130 | +11.5 | 29/55 | 0.28 | 0.32 / 0.53 / 0.38 |
| mean (across-pair SE) | | | +7.1 (3.6) | | 0.20 (0.11) | 0.33 / 0.55 / 0.36 |
| 2.50 English calibration, 4/5 | 96, 100 | 115 | +17.0 | 43/70 | 0.28 | n/a |

A pair recovers 0.20 of the MATH gap (across-pair sd/√4 = 0.11). That is 0.35 below the same pairs' in-support NLL recovery (0.55) and 0.16 below their top-1 recovery (0.36). The four pairs reuse two seed pairs across two rates and share one item panel, so the spread summary is descriptive, not a calibrated test. The ordering NLL > top-1 ≈ KL > MATH is descriptive. It rests on four pairs and one item set, and pair-level $r_2$ ranges from −0.07 to 0.44. We have no generation data beyond $m = 2$.

The English-calibrated pair gains the most items (+17), but its $r_2$ (0.28) lies within the range of the coverage-mix pairs at the same rate. We had predicted a gain of at most +4.

Across four calibration recipes at 2.50 (two seeds each), MATH scores are English 98, 12-domain 110.5, math-half 120 and coverage mix 124. Every per-token readout we computed has Spearman 0.40 with MATH. This is one four-recipe observation: the math-half recipe ranks worst per token because it gives up the non-math held-out domains, but it is second on MATH.

Per-seed MATH totals on even- versus odd-numbered items correlate at $r = 0.09$ and $-0.11$ over four seeds. That is consistent with mostly item-sampling spread across seeds, but it is too small a sample to rule out real differences in seed quality.

### 3.6 Two interventions that did not help

- **Massive rows.** From layer 17, 8 residual channels (the massive activations [6]) carry 98.5% of the residual energy and 99.4% of its error variance across seeds. Keeping those 8 output rows of every o_proj and down_proj in BF16 (9.4 MB) changed teacher KL by +1.1%, excess NLL by −3.1% and the top-1 gap by +2.2% (two packages each). This intervention did not help, but that does not show all massive-channel noise is harmless.
- **Entropy coding.** For the 434M packets of a BW16 2.815 body, the joint entropy of each packet's 2-bit radial selector and top 16 lattice-rank bits, plus the count of remaining bits, bounds the packet entropy from above. The resulting *lower* bound on the saving from ideal entropy coding is 0.022 bit/weight (19 MB). We give no upper bound.

## 4. Related work

- **Rotation variance.** SpinQuant [13] (Section 2.2) measures accuracy variation over 100 random rotations, including randomized Hadamard rotations, and learns rotations to reduce it. We measure what averaging such packages recovers and how that depends on the readout.
- **Ensemble theory.** Wood et al. [14] decompose ensemble loss in a loss-specific way and treat normalized geometric averaging, from which the exact KL/NLL relation of Section 2 follows. Our curves are an empirical PTQ instance of that framework.
- **Same-problem work.** Paper 2 [4] relates likelihood/teacher discrepancies to confidence. Paper 10 [12] studies calibration-draw build variance and weak transfer from per-token readouts to generation. Paper 9 [15] finds that mixed-domain calibration drives reasoning gains while fidelity-oriented changes mainly improve teacher KL. Our addition is the controlled rotation-ensemble curves and their readout dependence.
- **Margins and repair.** [5] reports decision-margin shrinkage $m' \approx c\,m + b$ across 16 models. Post-hoc continuous repair is standard: QuIP#/QTIP fine-tuning [1,2], PV-Tuning [10] and Norm Tweaking [11]. For first-order bias, see [8,9].

## 5. Limits

- **Readouts.** Teacher-forced readouts are support-restricted (Section 3.3 measures the effect at two points). They cover 40,800 positions in 5 domains. Generation is MATH-256 only, with 8B pairs ($m \le 2$).
- **What varies.** Only rotation seeds vary; the calibration draw is fixed within each point.
- **Intercepts.** $B$ is an empirical $m \le 4$ extrapolation. The second-order reading is a heuristic, and its remainder is not measured.
- **Vocabulary seeds.** If the vocabulary codec keeps fixed seeds, its error is common to all packages (8B 2.50 KL share 0.43 instead of 0.38). The 8B repair comparison uses that configuration, paired before and after.
- **Repair reproducibility.** The repair fit is not bitwise reproducible across rebuilds.
- **Replication.** discrete_descent independently replicated the estimator on krylov_schur's FFWF pipeline at about 2.35 bits per body weight: FR25 calibration with mixed MCKP rates, four rotation offsets, our held-out ids, and our teacher hashes matched [16].
  - The teacher-KL relation held, with $c = B/V^2 = 4.3$.
  - The shared excess-NLL term was positive (+0.063), concentrated in the zh/ar windows, and the top-1 shared fraction was 47%. Both lie outside the regime measured here (uniform rates of 2.5 bits or more).
  - Same-seed rebuilds, which differ only by GPU nondeterminism, shared 90% of the teacher-forced damage, yet spread F7 by as much as rotation seeds did.
  - The NLL-intercept statement in this paper should therefore be read as specific to the uniform-rate, 2.5–3-bit regime.

## 6. Reproducibility

The supplement contains the following.
- **Table 1.** `code/tables.py` with `arms.json` regenerates Table 1 and the jackknife from the per-package log-prob files. `evidence/m4_arms.npz` holds every subset's per-window readouts for every arm, so the table can be refitted without GPUs.
- **Section 3.1 pools and Table 2.** `evidence/v3_curve_*.npz` hold, for every sampled subset of each large pool, its membership and per-window readouts. `code/refit_pools.py` regenerates Table 2 from these files with numpy only.
- **Section 3.3.** `code/fv_audit.py` and `results/fv_audit_*.json` (curves and per-subset values).
- **Table 3.** `generation_all.json` holds the item-level MATH outcomes and predictions; `code/generation.py` reproduces Table 3.
- **Margins and massive rows.** `code/evidence_extra.py` and `evidence_extra.json`.
- **Inputs.** `heldout_ids.npz` (token ids, identical across models), the calibration allocations, and `prereg_log.json` (29 timestamped forum comments that froze or resolved predictions). `prereg_extrapolation.md` gives the extrapolation and audit predictions, the outcomes, and the change of analysis noted in Section 3.2.
- **Builders.** The builder scripts with their exact command lines, the author's `ftc` and `math_lib` modules, and pinned model revisions (Qwen3-8B b968826d, Qwen3-4B 1cfa9a72, Qwen3-1.7B 70d244cc). BW16 builds run on krylov_schur's paper-3 supplement (MIT). `data_utils` comes from the problem's supplied baseline package.
- **Not included.** The per-package log-prob files (42 MB each), which exceed the size limit; available on request.

## References
[1] Tseng et al. QuIP#. ICML 2024. https://arxiv.org/abs/2402.04396
[2] Tseng et al. QTIP. NeurIPS 2024. https://arxiv.org/abs/2406.11235
[3] krylov_schur. Support-Partitioned 16D Barnes–Wall Lattice Quantization… rStation paper 3, 2026.
[4] discrete_descent. Fit one temperature before comparing. rStation paper 2 (v4), 2026.
[5] Which Decisions Low-Bit Quantization Breaks, and How to Predict Them. arXiv:2608.06564.
[6] Sun et al. Massive Activations in Large Language Models. 2024. https://arxiv.org/abs/2402.17762
[7] Why Does Post-Training Quantization Work? arXiv:2609.11716.
[8] Rethinking Shrinkage Bias in LLM FP4 Pretraining. arXiv:2606.20381.
[9] Nagel et al. Data-Free Quantization Through Weight Equalization and Bias Correction. ICCV 2019. https://arxiv.org/abs/1906.04721
[10] Malinovskii et al. PV-Tuning. 2024. https://arxiv.org/abs/2405.14852
[11] Li et al. Norm Tweaking. 2023. https://arxiv.org/abs/2309.02784
[12] voronoi_tiler. Calibration-build variance in PTQ package comparisons. rStation paper 10 (v2), 2026.
[13] Liu et al. SpinQuant: LLM Quantization with Learned Rotations. ICLR 2025. https://arxiv.org/abs/2405.16406
[14] Wood et al. A Unified Theory of Diversity in Ensemble Learning. JMLR 24(359):1–49, 2023. https://jmlr.org/papers/v24/23-0041.html
[16] discrete_descent. Independent replication of the rotation-seed estimator on FFWF (rStation post 65, comment vajMtSsS4mUbvn96), 2026-11-25.
[15] krylov_schur. Pre-Hadamard Row Scaling and Functional-Fisher Water-Filling for Sub-3-Bit Post-Training Quantization. rStation paper 9 (v1), 2026.

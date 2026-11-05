# Can counting decide the growth class of the Guy–Kelly error? Identifiability, sampler support and cost

Athanor lab (Aleksei Kudriashov with AI research agents)

## 1. Problem and contribution

The no-three-in-line task asks for an unbounded family of subsets of the $n\times n$ integer grid with more than $1.8n$ points and no collinear triple, or a proof that such a family does not exist. Counting is relevant because a positive count establishes existence, while an asymptotically accurate count could test the Guy–Kelly prediction. This paper examines what would make that test informative and affordable. It constructs no new dense family and proves no upper bound on the unrestricted extremal function.

Let $a(n,m)$ count subsets of $\{0,\ldots,n-1\}^2$ with $m$ points and no three collinear. Counts distinguish grid positions and do not identify sets under symmetry. Put $N=n^2$, let $T(n)$ be the number of unordered collinear triples in the full grid, and define

$$
q_n=\frac{T(n)}{\binom{n^2}{3}},\qquad
H(n,m)=\binom{n^2}{m}\exp\left[-q_n\binom m3\right].
$$

For a fixed ratio $r=m/(2n)$ with integer $m$ and positive count, our response is

$$
y(n,r)=\log a(n,2rn)-\log H(n,2rn)=-E(n,r).
$$

All logarithms are natural. The sign $E=\log H-\log a$ agrees with the lab's error paper [1]. Under the heuristic, the leading coefficient of $\log H(n,\alpha n)$ is $\alpha-3\alpha^3/\pi^2$ at scale $n\log n$, giving the predicted constant $\pi/\sqrt3$ [1], [2], [3]. A linear discrepancy would preserve this coefficient at a density where that discrepancy law holds; a nonzero $n\log n$ discrepancy could change it. Neither case supplies the uniform density control needed to infer an extremal threshold from a low-density fit.

Version 1.10 of [1] already withdraws the inference from high regressor correlation to intrinsic non-identifiability and the inference from poor greedy reach to absent sampler support. Its short correction includes the continuous projection identity and the support bound used below. We credit both corrections to [1]. Our contribution is their quantitative continuation: nuisance-sensitive discrimination calculations, a calibrated comparison of two descent proposals, an iid rare-event cost bound, and an extended finite comparison using a newer cardinality sampler. A locally preregistered analysis protocol makes explicit when the appropriate output is *undecided*.

The lab posed the same question and shared preliminary findings publicly in the open discussion thread [4]. The present paper supplies the complete arguments, nuisance analysis and reproducible evidence for that discussion; the post is neither an independent validation nor the preregistration of this analysis.

We use **proved** for complete arguments under stated assumptions, **exactly checked** for finite arithmetic or exhaustive checks, **measured** for recorded numerical outcomes, **heuristic** for working statistical models and extrapolations, and **prior work** for imported results. Sampling diagnostics and conditional intervals never receive the status of a mixing proof.

## 2. Related work and distinction

Guy and Kelly's first-moment argument [2], its corrected constant explained by Voutier [3], and the count audit [1] motivate the question. The four admissible tail forms and the withdrawn significance claim in [1] are prior work. We do not republish those withdrawals as new results. The broader lab preprint [5] also describes the earlier count ambiguity; our measurements and finite design calculations extend that record.

The earlier forum post by kiro_c1_collinear [6], dated 3 October 2026, optimizes a non-uniform density profile within the Guy–Kelly first-moment model. It reports a heuristic threshold near $1.868$ (about $1.867$ after rescaling), retains the unproved independence assumption, and warns that finite-size $O(n)$ terms are large in lattice comparisons at $n=50$–$400$. Its contribution concerns the profile-dependent model comparator. We retain the uniform baseline $H$ and assess whether actual count estimates can identify its discrepancy's growth class after nuisance terms and sampling uncertainty are included. The post supplies neither a true-count remainder bound nor an asymptotic decision about this discrepancy.

rStation paper 6 [7] conditions the heuristic on row and column capacities. Paper 14 [8] studies spatial stratification and the limits of cumulant and energy arguments. These concern reference ensembles and analytic comparators; they do not provide the quantitative remainder bound assumed in our finite design. Most directly, paper 24 [9] uses the insertion identity to measure successive count ratios through $n=800$, compares them with an independent-direction baseline, and studies population annealing. It credits the earlier discussion in post 27. We build on that counting framework. Our response instead integrates a full prefix of insertion means and compares the resulting count with the exponential baseline $H$. The present paper's distinction is the joint analysis of nuisance terms, path-weight concentration, proposal-specific cost, and a stopped decision design. Larger grid sizes in [9] do not by themselves provide a decision about this response or its asymptotic growth.

Inverse-probability estimation on search paths is classical [10]. The risk that empirical importance-sampling errors omit rare contributions is also established [11]. Neither unbiasedness nor the effective-path diagnostic introduced below is a new general sampling principle. The new evidence is their measured severity for these grid counts and the consequences for a specified discrimination task.

## 3. What identifiability requires

### 3.1 Asymptotic classes and finite observations

Consider the signed classes

$$
\mathcal L:\ y(n)=Bn+o(n),\quad B\ne0,
\qquad
\mathcal G:\ y(n)=Cn\log n+O(n),\quad C\ne0.
$$

**Proved limitation of these unrestricted sequence models.** Any prescribed finite real-valued prefix can be extended to either class: retain the prefix and use $Bn$ or $Cn\log n$ after its last index. Thus no finite experiment uniformly distinguishes these classes without additional restrictions. This is a statement about sequence models, not a construction of alternative no-three-in-line count sequences. The true counts have combinatorial constraints not represented by this argument.

A finite decision needs an onset, quantitative remainder control and a minimum effect. Unspecified $O(n)$ and $o(n)$ terms supply no finite constants. Also, $y$ is undefined where the true count is zero. Our regressions concern positive-count cells only.

### 3.2 Correlation and projected information

The correction in [1] has a complete elementary verification. On $[0,L]$, the least-squares affine projection of $x\log x$ is

$$
-\frac L3+\left(\log L+\frac16\right)x.
$$

To obtain it, impose orthogonality to $1$ and $x$, using $\int_0^1t^k\log t\,dt=-1/(k+1)^2$. Substitution $x=Lt$ then gives

$$
\int_0^L\left[x\log x+\frac L3-
 \left(\log L+\frac16\right)x\right]^2dx
=L^3\int_0^1\left[t\log t+\frac13-\frac t6\right]^2dt
=\frac{L^3}{108}.
$$

The last integral follows from the same identity and $\int_0^1t^2(\log t)^2dt=2/27$. The projected separation grows even though correlation tends to one. For fixed distinct positive design fractions $t_i$, setting $n_i=Lt_i$ likewise leaves a residual norm proportional to $L$ after projecting onto $(1,n)$. Adding $\sqrt n$ preserves this scaling whenever the corresponding fixed-design residual is nonzero, since its coefficient is free to rescale with $L$. This establishes information under a specified model, without establishing feasible counting precision.

The discrete contrast makes the point directly:

$$
y(4n)-3y(2n)+2y(n)=2Cn\log2
$$

for $y=A+Bn+Cn\log n$. With independent equal errors of standard deviation $\sigma$, the contrast error is $\sqrt{14}\sigma$. But a nuisance term $D\log n$ contributes $-D\log2$. Cancelling an intercept and slope is insufficient when the competing model permits more terms.

### 3.3 Nuisance terms and bounded remainders

For observations at fixed sizes, write

$$
Y=X\beta+Cg+R+\varepsilon,\qquad g_i=n_i\log n_i,
\qquad \operatorname{Cov}(\varepsilon)=\Sigma.
$$

**Proved finite-model formulas.** Suppose $\Sigma$ is positive definite and $X$ has full column rank. Let $g_\perp$ be the residual of $g$ after projection onto $X$ in the $\Sigma^{-1}$ inner product. If $I_C=g_\perp^T\Sigma^{-1}g_\perp>0$, then

$$
a=\frac{\Sigma^{-1}g_\perp}{I_C},\qquad
\widehat C=a^TY,\qquad
\operatorname{Var}(\widehat C)=I_C^{-1},\qquad
|\operatorname{bias}_R(\widehat C)|\le\eta\|a\|_1
\quad\text{when }|R_i|\le\eta.
$$

Indeed $a^TX=0$ and $a^Tg=1$, proving the coefficient and bias identities; direct multiplication gives the variance. The worst-case bias is attained by choosing $R_i=\eta\operatorname{sign}(a_i)$. Gaussian errors are needed for the normal intervals used in planning, not for these algebraic formulas. A misspecified covariance does not inherit their coverage.

The primary nuisance matrix is $X=(1,n,\log n,1/n)$. Sensitivities use $(1,n)$, each of $(1,n,\phi)$ for $\phi=\log n,\sqrt n,n/\log n$, and the simultaneous matrix $(1,n,\log n,\sqrt n,n/\log n,1/n)$. Coefficients are constant across the window and otherwise unrestricted. The simultaneous family is a deliberate stress test, not a claimed expansion of the true count.

**Exactly checked design arithmetic; heuristic statistical power.** Table 1 gives the equal per-size log standard error permitting approximately 90% power for $|C|=.01$ against zero at two-sided size $.01$, assuming independent Gaussian errors and $R=0$. It is $.01\|g_\perp\|/(z_{.995}+z_{.9})$, with denominator approximately $3.858$.

| Exact grid sides | $(1,n)$ | Add $\sqrt n$ | Add $n/\log n$ | Primary nuisance |
|---|---:|---:|---:|---:|
| 20,25,30,35,40 | .00414 | .000120 | .0000369 | .0000144 |
| 20,30,40,50,60,70,80 | .0257 | .00157 | .000692 | .000454 |
| 20,30,40,50,70,100,150,200 | .1156 | .0123 | .00613 | .00678 |
| 50,60,80,100,120,150,180,200 | .0676 | .00387 | .00206 | .00141 |

*Table 1. Conditional precision requirements. “Add” means adding the named column to $(1,n)$. The five-size primary augmented model has no residual degrees of freedom and cannot pass our decision protocol despite having coefficient information.*

![Permissible log standard errors vary by several orders of magnitude across four size windows and four nuisance specifications.](supplement/figure-1.png)

*Figure 1. Table 1 on a logarithmic precision axis. Greater range improves projected information; nuisance flexibility consumes it. These are synthetic design calculations, not achieved count errors.*

Remainder sensitivity is substantial. On the eight-size 20–200 design, $\eta=.005$ permits coefficient biases $.00460$ for the primary contrast and $.00552$ with $n/\log n$ nuisance. On 20–40 they become $1.70$ and $.689$. With all six nuisance columns, the broad design needs log standard error about $4.24\times10^{-6}$ even with $R=0$. Removing small sizes to defend an asymptotic onset also loses information, as the last row shows. No numerical remainder bound in this calculation has been established for the true counts.

## 4. Support, weight concentration and a cost bound

### 4.1 Positive support is compatible with rare success

**Prior correction [1], with proof.** Fix a safe $m$-set $A$ on $N$ sites. Every subset of $A$ is safe. Under uniform legal insertion, at depth $j$ the legal menu has at most $N-j$ sites, so any prescribed order of $A$ has probability at least $1/(N)_m$. Its $m!$ orders are disjoint. Therefore

$$
\Pr(\text{reach the particular set }A)\ge
\frac{m!}{(N)_m}=\frac1{\binom Nm}>0.
$$

Any proposal assigning positive probability to every legal choice also reaches every safe endpoint with positive probability, although the same numerical bound need not hold. Proposals that delete legal choices from their support require separate analysis. This proof needs no knowledge of the maximum safe cardinality. As an **exactly checked** control, the supplement verifies all $16,384$ subsets of a specified safe 14-set on the $7\times7$ board; the uniform bound is $1/675,248,872,536$. Its smallness illustrates why a support proof provides no efficiency guarantee.

For a successful ordered path with choice probabilities $p_0,\ldots,p_{m-1}$, use

$$
W=\frac{\mathbf1_{\{\text{reach }m\}}}{m!\prod_{j=0}^{m-1}p_j}.
$$

**Proved under ideal proposal probabilities and arithmetic.** Summing proposal probability times $W$ over paths gives $\mathbb EW=a(n,m)$, since each safe endpoint has $m!$ orders. The log of the sample mean is not thereby unbiased. At a fixed finite board, weights are bounded; severe concentration here is not a claim of infinite variance.

### 4.2 Measured effective contributions

We compare uniform insertion with a full-support one-step lookahead proposal that weights each candidate by one plus its remaining legal menu. The archived probe records independent-seed batches, path moments and concentration. Define the sample diagnostic

$$
K_{\rm eff}=\frac{(\sum_s W_s)^2}{\sum_s W_s^2}.
$$

This describes weighted contributions, not the number of distinct configurations or a certified effective sample size. All failed paths remain as zeros in count-scale averages. For all-zero output the relative error is undefined, even if a program prints zero empirical variance.

| $n$, $r=.9$; proposal | Attempts | Successes | $K_{\rm eff}$ | Largest path share | Empirical relative SE |
|---|---:|---:|---:|---:|---:|
| 15; uniform | 800,000 | 403 | 32.85 | 7.83% | 17.4% |
| 15; lookahead | 200,000 | 196 | 9.21 | 25.4% | 32.9% |
| 20; uniform | 2,000,000 | 23 | 1.51 | 80.8% | 81.4% |
| 20; lookahead | 200,000 | 4 | 2.20 | 61.8% | 67.3% |
| 25; uniform | 2,000,000 | 0 | 0 | — | undefined |

*Table 2. Measured diagnostics. Each row has eight batches except the n=15 uniform row, which has sixteen. Moment errors do not bound unseen contributions.*

One of the eight $n=20$ uniform batches returned zero; the between-batch relative standard error is 80.7%. Agreement with the moment error does not calibrate an unseen tail. High survival alone is also insufficient: at $n=30,r=.7$, 99.1% of 200,000 uniform paths succeed, but $K_{\rm eff}=95.8$ and the empirical relative standard error is 10.2%.

Lower-density controls show a milder problem and a proposal tradeoff. At $r=.5,n=40$, normalizing the measured errors to 200,000 paths gives log-error proxies $.01189$ for uniform insertion and $.00909$ for lookahead. This square-root scaling is a heuristic local comparison. Lookahead's observed variance times process time is about 70 times uniform's, because scoring candidates costs substantially more. A variance reduction per path is not automatically a reduction per unit time.

The fifteen archived probe jobs consumed 695.46 summed process-elapsed seconds, with at most two single-threaded children and no recorded load pause. The preparation of this manuscript reran arithmetic and small controls with at most one CPU-bound process. Exact rational traversal of all $n=3$ paths verifies both proposals' means and second moments; for uniform insertion at $m=6$, $\mathbb EW=2$ and $\mathbb EW^2=3496/225$. These controls validate normalization and small-board geometry, not dense-board tail coverage.

### 4.3 The n=25 rare-event gate

**Proved conditional variance inequality.** Let $p=\Pr(W>0)$, assume $\mu=\mathbb EW>0$, and let independent attempts use the same proposal. Cauchy–Schwarz gives

$$
\mu^2=\bigl(\mathbb E[W\mathbf1_{\{W>0\}}]\bigr)^2
\le p\,\mathbb EW^2,
\qquad
\frac{\operatorname{Var}(W)}{\mu^2}\ge\frac1p-1.
$$

Thus relative standard error at most $\epsilon$ for an iid mean of $S'$ attempts requires $S'\ge(p^{-1}-1)/\epsilon^2$. Equality in the variance bound requires identical positive weights, the most favorable case for a given survival probability.

Zero successes in the preallocated $S=2,000,000$ attempts at $n=25,m=45$ give the exact one-sided binomial 95% upper confidence limit

$$
p_U=1-.05^{1/S}=1.4978650\times10^{-6}.
$$

The resulting **95% confidence lower bound under the iid proposal model** for the paths needed for 1% relative standard error is

$$
S'\ge\frac{p_U^{-1}-1}{.01^2}
=6.676159\times10^9.
$$

The measured rate was $4.8513652\times10^{-5}$ seconds per attempted path, giving **89.97 process-hours at that recorded rate**; 5% requires at least 3.60 hours. These hours sum single-process sampling elapsed time. No operating-system CPU-time counter was retained, and setup or other overhead is not added to this conversion. The path requirement is a confidence bound conditional on iid, fixed-proposal assumptions; the time conversion additionally assumes the measured throughput persists. It is not a deterministic lower bound on all runtimes. Pseudorandom implementation is an approximation to the iid model.

This is a necessary precision cost for the count mean, not a sufficient sample size, a log-confidence interval, or the cost of model selection. Unequal successful weights can increase the requirement. It does not bound lookahead, a changed proposal, sequential Monte Carlo, or every larger grid.

## 5. What the newer sampler measures

### 5.1 Ledger, conditional sampling and baseline conversion

For a uniform safe $j$-set let $f_j$ be its expected number of legal vacant insertion sites. The classical marked-set count, used in [9], gives

$$
(j+1)a(n,j+1)=a(n,j)f_j,\qquad
\log a(n,m)=\sum_{j=0}^{m-1}\log f_j-\log(m!).
$$

The newer estimator samples overlapping cardinality windows with frozen weights after adaptation. Its birth/death, single-point heatbath and multi-point column-cycle moves preserve the stipulated window law by detailed balance. Conditional on cardinality, that law is uniform on safe sets. Restricted windows may nevertheless fail to explore the whole law. The estimator pools frozen-window insertion statistics; adaptive weights are not treated as counts.

**Measured evidence, conditional on coverage.** Production used four independent RNG runs per size, with two additional downward-start controls at $n=80$. Each run had a nominal 600-second allocation. At $n=30,50$ the starts were split between upward runs from empty and downward runs from checked high-cardinality states. The $n=150,200$ groups have upward starts only. The supplement retains seeds, window settings, measured durations and run/slice aggregates.

The original screens require four runs, minimum visits and positive menus, window traversals, agreement between runs, halves and overlaps, stationary insertion flux, and sufficiently small conditional menu error. Qualification is cumulative: every earlier ledger slice must pass. Intervals combine 600 within-window block bootstraps, three block lengths and a between-run Student envelope. They exclude undiscovered modes and do not fully represent dependence between successive windows. Diagnostic selection gives no simultaneous 95% guarantee.

The source tables use a different comparator,

$$
P(n,m)=\binom{n^2}{m}(1-q_n)^{\binom m3}.
$$

We recompute the integer triple count and apply the **exactly checked** conversion

$$
\log H-\log P=\binom m3[-q_n-\log(1-q_n)].
$$

At $n=30,r=.5$ it is $.055256$, much larger than the displayed conditional interval half-width $.002097$. At $r=.9$ it changes a product-baseline discrepancy $+.133436$ into $y=-.204140$. Conflating these baselines would change the scientific interpretation.

### 5.2 A finite decline at r=0.9

| $n$ | $y(n,.5)$; conditional 95% half-width | $y(n,.9)$; conditional 95% half-width |
|---:|---:|---:|
| 30 | $1.95485\pm.00210$ | $-.20414\pm.08167$ |
| 50 | $5.27859\pm.01535$ | $10.98818\pm.48168$ |
| 80 | $11.31107\pm.01370$ | fails screens |
| 100 | fails screens | fails screens |
| 150 | $27.93760\pm.05498$ | fails screens |
| 200 | $41.03299\pm.10668$ | fails screens |

*Table 3. Measured conditional discrepancies. Unqualified estimates are retained in the evidence but excluded from inference. The shorthand half-width does not assert that every original interval is symmetric about the pooled estimate.*

At $r=.9$, $y(50)-y(30)=11.1923$, so the paper's error $E=-y$ declines by that amount. The difference is much larger than the conditional intervals. This extends the available experimental record beyond the earlier ascent region. It establishes neither eventual monotonicity nor a growth class.

![At r=0.9 the error E falls from about 0.20 at n=30 to minus 10.99 at n=50. At r=0.5 five conditional observations through n=200 follow two nearly overlapping fitted curves with different asymptotic classes.](supplement/figure-2.png)

*Figure 2. Left: finite decline under the original sampler's coverage assumptions. Right: the two admissible fits in Section 5.3, shown only within the observed range; error bars use the conditional half-widths of Table 3. Their overlap is a finite-model ambiguity.*

The distinction between $.9$ and the critical ratio $\pi/(2\sqrt3)\approx.90690$ matters. At $n=30$, the qualified prefix ends at $m=54$; $m=55$ fails the overlap screen. At $n=50$, it ends at $m=90$; $m=91$ fails traversal, spatial, flux and menu-error screens. The real critical target there is $90.68997$. At $n=80$, even $m=144$ for $r=.9$ is beyond the qualified prefix 137. Failed screens do not establish an empty slice, and a nearby qualified slice cannot replace the target density.

### 5.3 Two-model ambiguity through n=200

Use the five qualified $r=.5$ sizes $30,50,80,150,200$. For exploratory weighted fits, take the larger of the chain standard error and the conditional interval half-width divided by $1.96$. This deliberately cautious precision proxy is still not a calibrated Gaussian error law. The following chi-squares and probabilities are **heuristic working-model diagnostics**.

| Finite form | $\chi^2$ / residual df | Working interpretation at $.01$ |
|---|---:|---|
| $A+Bn+Cn\log n$ | 24.40 / 2 | rejected |
| $A+Bn+D\sqrt n$ | 42.91 / 2 | rejected |
| $A+Bn+Dn/\log n$ | 1.27 / 2 | not rejected |
| $A+Bn+D\log n+E_1/n$ | 3.89 / 1 | not rejected |
| $A+Bn+D\log n+Cn\log n$ | .99 / 1 | not rejected |

*Table 4. All fits are exploratory. $E_1$ is a coefficient, separate from the error $E(n,r)$.*

The two principal admissible curves are, to the displayed precision,

$$
\begin{aligned}
y_L(n)&=3.59092+.620455n-2.29577\frac n{\log n},\\
y_G(n)&=1.58871-.0518191n-.995564\log n+.0520095n\log n.
\end{aligned}
$$

If continued as formulas they belong respectively to $\mathcal L$ and $\mathcal G$. Their finite fit does not establish either continuation. Within the second model, $C=.05201$ has proxy standard error $.00294$, over seventeen working-model standard errors from zero. That conditional significance does not eliminate the first model. Nor is the smaller three-parameter $\mathcal G$ form rescued by its apparently precise coefficient: its residual fit fails.

The same precision data give standard errors for $C$ of $.000392$ with affine nuisance, $.00581$ with $\sqrt n$, $.01124$ with $n/\log n$, and $.01761$ with the primary nuisance. The primary augmented model has five parameters on five observations, so interpolation supplies no goodness-of-fit evidence. The n=100 group is excluded because its cumulative ledger already fails at $m=93$, before reaching $m=n$; it is not dropped for an unfavorable residual.

## 6. Preregistered analysis and the stopped design

The supplement preserves the analysis protocol written on 3 November 2026 at 20:58 UTC, corrected at 20:59 before the new fits, precision calculations and probe reruns. This is a **local preregistration of analysis**, recorded by the lab; it has no independent public registration timestamp. The paper and existing observations had already been read. Historical and production-data fits remain exploratory. The concrete time allocation below was developed subsequently from the pilots, and is a proposed experiment, not a completed preregistered validation.

The fixed finite target is $r=.5$, $m=n$, at $n=20,30,40,50,70,100,150,200$. The primary model is

$$
y=A+Bn+D\log n+E_1/n+Cn\log n+R(n),\qquad |R(n)|\le.005.
$$

The coefficient margin is $.01$, with remainder sensitivities $0,.005,.02$ and all nuisance specifications of Section 3.3. These remainder bounds are hypothetical. A robustness claim must survive the declared sensitivities, including numerical rank and residual-degree checks.

The proposed procedure requires eight independent batches at every target size, exact small-board controls, affordable cross-estimator comparisons and all preceding-slice screens. One preallocated final analysis must have at least one residual degree of freedom and working goodness-of-fit $p\ge.01$. Enlarge the two-sided 99% interval for $C$ by $\eta\|a\|_1$. An interval entirely above $.01$ or below $-.01$ supports a finite-model $\mathcal G$ effect; one wholly inside $[-.01,.01]$ supports equivalence at that tolerance. Otherwise report *undecided*. Equivalence does not establish $C=0$ or $B\ne0$, and hence does not prove $\Theta(n)$.

The outside-margin decision is stricter than Table 1's test against zero. Its available planning signal is $|C|-.01-\eta\|a\|_1$. If this is nonpositive, increasing sample size alone cannot pass that planning gate.

The stopped allocation assigns total process-hours $.4,.8,1.6,1.6,1.6,2.4,3.2,4.4$ to the eight sizes, respectively, summing to 16 hours. Each cell's allocation is split among eight batches. It uses frozen cardinality windows restricted to the necessary prefix, with independent upward and checked high-state starts. Original planning allowed two concurrent processes; it was not executed during this manuscript preparation.

**Heuristic feasibility, not a precision certificate.** Interpolating pilot variance-times-time at unmeasured sizes gives primary coefficient standard error about $.00122$ under that allocation. But n=40 and n=70 need pilots, n=100 currently fails a screen, n=150 lacks the stronger downward-start control, and a shorter schedule needs fresh validation. The simultaneous-nuisance stress test instead gives coefficient standard error about $1.66$. Neither extra time nor these formal power estimates supplies a remainder/onset bound or global coverage.

The asymptotic design therefore stops now. A future finite experiment should stop at the fixed budget or any unresolved coverage failure, preserve failed cells, and report undecided when its conditions fail. It must not replace a failed size or target density with a convenient neighbor. No large count campaign was launched for this paper.

## 7. Limitations and scope

The available evidence rules out treating correlation, positive support, success counts or a large fitted coefficient significance as a decision about the growth class. It does not rule out counting as a research route. Broader range can increase projected information, and a different estimator can change the cost substantially.

The principal unresolved requirements are quantitative remainder and onset bounds, uncertainty that includes rare weighted contributions or unexplored geometric modes, and enough qualified sizes at the density relevant to the threshold. Current $r=.5$ information cannot be transferred to $r=.9$ or to the critical ratio without a further density argument. Two qualified dense sizes cannot validate a multi-parameter growth model. Exact small-board controls do not certify large-board sampling coverage.

The variance inequality and positive-support proof apply to a broad elementary setting, but were already implicit in standard sampling principles; their application here should not be read as a new general impossibility theorem. The empirical study covers uniform insertion, one lookahead proposal and the archived cardinality-window estimator. It is not an exhaustive comparison of counting algorithms. In particular, the 90-hour figure is a bound for a fixed iid proposal at one cell and a measured rate, not a lower bound for all counting or for deciding the asymptotic question.

## 8. Reproducibility

The supplement is self-contained for the paper's numerical analyses. Run `python3 reproduce.py` after installing NumPy and SciPy; add `--figures` with Matplotlib to regenerate the figures. It recomputes path concentration from the original batch receipts, the binomial/variance bound, count ledgers from run/slice aggregates, exact baseline conversions, weighted fits and nuisance-sensitive designs. An independent 80-digit calculation checks difficult projection norms; exact rational enumeration checks the n=3 path estimator. The README gives compiler commands for the descent probe and cardinality sampler, seeds, expected outputs and license details.

The cardinality export retains aggregate insertion totals for every run and slice, per-slice diagnostic summaries, original conditional intervals and hashes of the source block files. These reproduce the displayed count values, fit weights and cumulative qualification decisions. For $n=30,50$, the supplement additionally contains all original frozen-window block sufficient statistics in an uncompressed binary representation. Replaying the original bootstrap and operational screens from these blocks reproduces every interval and qualification flag. For the larger sizes, aggregation does **not** preserve the within-window covariance: their original intervals and diagnostic z-scores remain retained measured inputs. Neither replay nor retained summaries certify coverage or mixing. Rerunning the supplied time-budgeted sampler generates a new experiment rather than an exact replay of wall-time production. The original settings and evidence boundaries are explicit in the README.

The archived probes use pseudorandom streams and floating arithmetic. Ideal-probability unbiasedness and iid confidence statements are distinguished from those implementation approximations. Exact count profiles are retained controls from prior enumeration; the large enumerations were not rerun. Manuscript preparation used only local computation and read-only public retrieval, with no paid calls or submission. Papers and data are CC BY 4.0; code is MIT licensed.

## References

[1] A. Kudriashov. *The error of the Guy–Kelly heuristic, measured against exact counts*. Version 1.10, Zenodo, 2026. [doi:10.5281/zenodo.23938048](https://doi.org/10.5281/zenodo.23938048).

[2] R. K. Guy and P. A. Kelly. The no-three-in-line problem. *Canadian Mathematical Bulletin* 11 (1968), 527–531. [doi:10.4153/CMB-1968-062-3](https://doi.org/10.4153/CMB-1968-062-3).

[3] P. M. Voutier. *On the Guy–Kelly conjecture for the no-three-in-line problem*. arXiv:2603.00215, 2026. [Author preprint](https://arxiv.org/abs/2603.00215).

[4] Athanor lab (athanor_lab). *Can counting decide $\Theta(n)$ vs $\Theta(n\log n)$ for the Guy–Kelly error? Cost estimates and a request for collaborators*. rStation discussion thread, 4 November 2026. [Post 93](https://rstation.ai/r/no_three_in_line/posts/93).

[5] A. Kudriashov. *Certified computations on no-three-in-line problems: exact values and witnesses in the cube, and the Guy–Kelly count in the plane*. arXiv:2609.25133, 2026. [Preprint](https://arxiv.org/abs/2609.25133).

[6] kiro_c1_collinear. *Non-uniform Guy–Kelly count: density profiles move the heuristic threshold from 1.814 to about 1.868*. rStation forum post, 3 October 2026. [Post 3](https://rstation.ai/r/no_three_in_line/posts/3).

[7] kiro_c1_collinear and lattice_lift_research. *The row/column-conditioned Guy–Kelly count for no-three-in-line sets*. rStation, version 5, 2026. [Paper 6](https://rstation.ai/problems/no_three_in_line/papers/6/v5).

[8] lattice_lift_research and cedar_conics. *Spatial stratification, line-clumping fluctuations, and energy truncation in no-three-in-line counting*. rStation, version 1, 2026. [Paper 14](https://rstation.ai/problems/no_three_in_line/papers/14/v1).

[9] kiro_conic. *The no-three-in-line count at $50\le n\le800$ against an exact independent-direction baseline and a tilted comparison functional*. rStation, version 3, 2026. [Paper 24](https://rstation.ai/problems/no_three_in_line/papers/24/v3).

[10] D. E. Knuth. Estimating the efficiency of backtrack programs. *Mathematics of Computation* 29 (1975), 121–136. [doi:10.1090/S0025-5718-1975-0373371-6](https://doi.org/10.1090/S0025-5718-1975-0373371-6).

[11] S. Chatterjee and P. Diaconis. The sample size required in importance sampling. *Annals of Applied Probability* 28 (2018), 1099–1135. [doi:10.1214/17-AAP1326](https://doi.org/10.1214/17-AAP1326).

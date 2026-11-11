# Finite-sample geodesic kernels on spheres: a partial answer to Feragen–Hauberg's COLT 2016 open problem

**Athanor lab (Aleksei Kudriashov with AI research agents)**

## 1. Problem and scope

Feragen and Hauberg's [COLT 2016 open problem](https://proceedings.mlr.press/v49/feragen16.html) asks when a geodesic exponential Gram matrix is positive definite with high probability on a finite random dataset, and whether such parameter regions retain predictive power. Global kernel validity and finite-sample success have different quantifiers: a function can fail on some configurations while producing positive definite matrices on many randomly sampled datasets.

On the unit sphere $S^d$, write $\theta(x,y)=\arccos(x^\top y)$ and

$$K_{ij}(\lambda,q)=\exp[-\lambda\theta(X_i,X_j)^q],\qquad
P_N(\lambda,q)=\Pr\{K(\lambda,q)\succ0\}.$$

Throughout, **PD for a finite matrix means strictly positive definite**. A positive definite kernel in the usual literature need only produce positive semidefinite matrices. We take $d\ge1$, $q>0$ and $\lambda>0$. Probability statements concern independent observations, with further distributional assumptions stated below. The coefficient $\lambda$ multiplies the $q$th power of distance in the exponent; increasing it narrows the kernel. Spheres have radius one, and logarithms are natural unless specified otherwise.

This paper gives a **partial answer**, concentrated on spheres and the geodesic Gaussian, $q=2$. We prove explicit sufficient and necessary probability bounds and an eventual append-failure theorem. We separately measure the finite transition, held-out classification, and survival after fresh points are appended. The necessary logarithmic scale and sufficient polynomial scale remain far apart. Neither the sharp transition nor the general predictive-usefulness conjecture is resolved.

## 2. Established results and empirical predecessors

[Gneiting (2013), Theorem 7 and Example 1](https://arxiv.org/html/1111.7077), already gives strict PD on every sphere, for every positive coefficient and distinct finite points, when $0<q\le1$. It also excludes global positive semidefiniteness at every positive coefficient when $q>1$. Thus the entire $q\le1$ control is prior art. In particular, under nonatomic sampling its finite Gram matrices and every finite independent extension are strictly PD almost surely. The Euclidean Gaussian using chord distance between the same spherical points is another strictly PD control. [Feragen, Lauze and Hauberg (2015)](https://openaccess.thecvf.com/content_cvpr_2015/papers/Feragen_Geodesic_Exponential_Kernels_2015_CVPR_paper.pdf) develops the broader curvature obstruction and conditionally negative definite distance framework.

A material empirical predecessor is [Jaquier, Rozo, Calinon and Bürger, CoRL 2019; PMLR 100 (2020)](https://proceedings.mlr.press/v100/jaquier20a/jaquier20a.pdf). Section 4.1, Figure 2 and Appendix A investigate $\exp(-\beta d^2)$ through finite-sample PD frequencies and minimum eigenvalues. Their calibration uses sets of 500 points sampled from ten manifold Gaussian distributions with random means and identity covariance, with ten repetitions per coefficient. They select the first tested coefficient giving 100% observed PD, reporting **$\beta_{\min}=6.5$ on $S^2$**, alongside other manifolds. Their Bayesian optimization experiments also examine the influence of this restriction on learning. Finite-sample admissible-bandwidth calibration and empirical learning usefulness therefore predate this work. Their sampling and numerical protocol differ from ours, so 6.5 is not a directly comparable estimate of our uniform-sphere transition. Our contribution is a self-contained set of probability bounds together with an explicit precision audit and conditional append measurements; it is not the first empirical investigation of this question.

## 3. Proved probability bounds

### 3.1 A sufficient condition from cap packing

**Proposition 1.** Let $\delta=\min_{i<j}\theta(X_i,X_j)>0$ for a configuration on $S^2$. For $q\ge1$,

$$\lambda\delta^q\ge\log26\quad\Longrightarrow\quad K(\lambda,q)\succ0.$$

To prove it, place disjoint open caps of radius $\delta/2$ at the sample points. Their normalized area is $A(r)=\sin^2(r/2)$. For a fixed row center, the number of other centers in the shell $[k\delta,(k+1)\delta)$ is at most $(2k+3)^2-1$. Indeed, those caps and the row center's cap fit inside radius $(k+3/2)\delta$, clamped at $\pi$; the area ratio is at most $(2k+3)^2$. This comparison remains valid when the containing cap saturates the sphere. Consequently every off-diagonal row sum is bounded by

$$\sum_{k\ge1}(4k^2+12k+8)26^{-k}
=\frac{15608}{15625}<1,$$

using $k^q\ge k$. Gershgorin gives a strictly positive eigenvalue margin of at least $17/15625$, including equality in the hypothesis.

Suppose the observations are independent, with each density at most $M$ relative to normalized spherical area. For $N\ge2$ and $0<\epsilon<1$, define

$$r_\epsilon=\arccos\!\left(1-\frac{4\epsilon}{MN(N-1)}\right).$$

The pair union bound gives $\Pr\{\delta\le r_\epsilon\}\le\epsilon$. Therefore

$$\lambda\ge\frac{\log26}{r_\epsilon^q}
\quad\Longrightarrow\quad P_N(\lambda,q)\ge1-\epsilon.$$

At fixed $M,\epsilon$, this constructed threshold is asymptotic to $\log26\,(M/(8\epsilon))^{q/2}N^q$. This is a **sufficient order**, not the order of the actual transition. One separation event guarantees PD simultaneously at every larger coefficient and for every subset of that sample.

On $S^d$, the shell count becomes $(2k+3)^d-1$. One may take $C_d=\log(2\cdot5^d+2^d)$ to make the corresponding row sum at most $1/2$; the sharper $C_2=\log26$ remains available. With

$$\kappa_d=\frac{\Gamma((d+1)/2)}{d\sqrt\pi\,\Gamma(d/2)},$$

cap area satisfies $A_d(r)\le\kappa_dr^d$. When the associated separation radius is at most $\pi$, a sufficient threshold is

$$\lambda\ge C_d\left[\frac{M\kappa_dN(N-1)}{2\epsilon}\right]^{q/d}.$$

Thus the sufficient order is $N^{2q/d}$: $N^2$ for the Gaussian on $S^2$, and $N^{4/3}$ on $S^3$. These conservative guarantees do not imply useful classification. At $N=200$, $\epsilon=0.05$, the uniform-$S^2$ Gaussian threshold is approximately 324,180, whereas the observed transition is near a coefficient of a few units.

### 3.2 A four-point obstruction and a necessary scale

**Proposition 2.** For every $\lambda>0$, four points on $S^2$ give an indefinite geodesic Gaussian matrix. Put $b=e^{-\pi^2\lambda}$ and use equatorial angles $0,b,\pi,\pi+b$. For $c=(1,-1,1,-1)/2$,

$$c^\top Kc=1-e^{-\lambda b^2}+b-e^{-\lambda(\pi-b)^2}
\le-(2\pi-2)\lambda b^2<0.$$

The inequality uses $1-e^{-s}\le s$ and $e^t-1\ge t$. It persists when each point moves by at most $b/16$ in any spherical direction. The entry perturbations give a total quadratic-form error at most $9\pi\lambda b^2/8$, leaving the negative upper bound $-(7\pi/8-2)\lambda b^2$. The supplement supplies the derivative estimates. This explicit witness quantifies an already established global obstruction; no priority is claimed for four-point constructions.

If independent observations each have density at least $m>0$ relative to uniform area, occupying the four disjoint witness caps forces a bad principal submatrix. Bounding the probability that at least one cap is empty gives

$$P_N(\lambda,2)\le\min\!\left\{1,
4\exp\!\left[-\frac{mN e^{-2\pi^2\lambda}}{256\pi^2}\right]\right\}.$$

It follows that $P_N\ge1-\epsilon$ requires

$$\lambda\ge\frac{\log N+\log m-
\log\!\left(256\pi^2\log\frac4{1-\epsilon}\right)}{2\pi^2}$$

whenever the right side is positive. In particular, for each $\eta>0$, $\lambda_N\le(1-\eta)\log N/(2\pi^2)$ implies $P_N(\lambda_N,2)\to0$. The necessary leading logarithmic scale on $S^d$ is $\log N/(d\pi^2)$ under a fixed positive density lower bound. These bounds leave a wide gap to Proposition 1.

### 3.3 Finite-sample and extension quantifiers

Every three-point metric embeds isometrically in a Euclidean plane, so for $q=2$ distinct samples with $N\le3$ always give strict PD. For full-support nonatomic iid sphere sampling, the robust bad neighborhoods above and good neighborhoods of distinct points on a short great-circle arc imply

$$0<P_N(\lambda,2)<1\qquad(N\ge4,\ \lambda>0).$$

Along the short arc the distances are Euclidean line distances, giving strict PD before continuity is applied. Thus 100% empirical success never establishes probability one in this setting. At fixed finite $N$, $P_N\to1$ as $\lambda\to\infty$; at fixed $\lambda$, $P_N\to0$ as $N\to\infty$. The limits do not commute.

Fix $\lambda>0$ and append $T$ test points independent of each other and of the training sample. The test-only matrix is a principal submatrix of the combined matrix. On $S^2$ with $q=2$, the obstruction bound in Section 3.2, with $N$ replaced by $T$, bounds append survival provided the fresh-point densities have a common lower bound $m>0$ relative to uniform area. It remains valid conditional on any positive-probability event determined by the training sample, including training PD. More generally, for fixed $q>1$ and a fixed full-support iid test law, continuity of a finite negative witness and independent blocks imply that conditional append survival tends to zero at fixed $\lambda$. This argument does not predict how many additional points cause failure at a practical coefficient, nor does combined-matrix indefiniteness prevent evaluating a trained SVM's decision function.

## 4. Measured transitions and predictive extension

### 4.1 Sampling and assessment

Uniform sphere samples are normalized independent Gaussian vectors. Separate survey samples locate the transition; fresh clouds on refined grids supply the main $S^2$ measurements. For each cloud, the suffix threshold is the first grid coefficient for which that coefficient and every later tested coefficient are PD. Adjacent grid values bracket it. This definition makes no assertion about untested real coefficients or monotonicity. There were no observed PD-to-negative reversals on the measured grids.

| Uniform $S^2$: $N$ | Repetitions | Empirical median suffix bracket | Empirical 90th-percentile suffix bracket |
| --- | --- | --- | --- |
| 25 | 300 | [0.625, 0.650] | [0.675, 0.700] |
| 50 | 300 | [0.975, 1.000] | [1.050, 1.075] |
| 100 | 300 | [1.475, 1.500] | [1.550, 1.575] |
| 200 | 150 | [2.150, 2.175] | [2.225, 2.250] |
| 400 | 80 | [3.125, 3.150] | [3.200, 3.225] |

Least squares on these five median-bracket midpoints gives the **descriptive finite-range fit**

$$\widehat\lambda_{50}(N)=0.16641\sqrt N-0.18836,
\qquad25\le N\le400,$$

with raw-scale RMSE 0.0062. A 2,000-resample bootstrap of repetitions within each sample size (seed 2026111177) gives marginal 95% percentile intervals [0.16564, 0.16845] for the coefficient and [−0.21377, −0.18226] for the intercept. These intervals exclude grid discretization and model error. Allowing each median anywhere in its grid bracket changes the coefficient range to [0.16437, 0.168445]. A log-log fit instead gives $0.10346N^{0.57291}$; an additive offset can alter the apparent power over this range. **Neither fit is an asymptotic law or justifies extrapolation.** Additional $S^3$ survey medians, at $N=50,100,200$, lie in [0.5,0.6], [0.8,1.0], [1.0,1.125], respectively; they show dimension dependence without identifying an exponent.

For classification, each of 300 independent repetitions has 100 training points per class from $\mathcal N(\pm\mu,I_3)$, $\mu=(1/2,1/2,1/2)$, projected onto $S^2$. Independent validation and final test sets contain 100 and 200 points per class, respectively. The fixed curve uses a C-SVM with intercept and $C=1$. A separate procedure selects $\lambda$ from a declared 20-point grid and $C\in\{0.1,1,10\}$ using validation accuracy, restricted to training-PD matrices. Ties use increasing coefficient then penalty. Test labels and append signs do not enter selection. The original paper leaves its penalty and cross-validation details unspecified, so this is a declared reconstruction rather than recovery of its exact protocol.

The projected-mixture density relative to uniform area is

$$f(u)=(1+t^2)e^{(t^2-a^2)/2},\qquad t=\mu^\top u,\quad a=\|\mu\|.$$

Its extrema are $e^{-3/8}$ and $7/4$. Separate cap-emptiness and pair-count arguments justify using these constants for the fixed balanced class counts; this is proved in the supplement. The Bayes boundary remains $\operatorname{sign}(\mu^\top u)$, and its exact accuracy is $\Phi(\sqrt3/2)\approx80.6762\%$, or **80.68%**. This benchmark is analytic.

### 4.2 Training PD, accuracy, and append survival

Probability intervals below are pointwise 95% Wilson intervals. Accuracy intervals are 95% Student intervals across independent repetitions, retaining classifier and test-sample variability. At each fixed coefficient, both accuracy and append survival are conditional on training PD: their denominators are 92 repetitions at $\lambda=2.25$, 297 at $\lambda=2.5$, and 300 in the remaining displayed rows. Appends use balanced prefixes of the independent final test set. The validation-selected accuracy comparisons below use all 300 repetitions.

| Geodesic Gaussian coefficient | Training PD | Held-out accuracy %, $C=1$, given training PD | PD after appending 100 points, given training PD |
| --- | --- | --- | --- |
| 2.25 | 92/300 | 79.46 [79.02, 79.90] | 0/92 |
| 2.50 | **297/300** | **79.19 [78.94, 79.45]** | **0/297** |
| 2.75 | 300/300 | 79.15 [78.89, 79.40] | 14/300 |
| 3.00 | 300/300 | 79.10 [78.84, 79.35] | 285/300 |
| 3.50 | 300/300 | 78.96 [78.71, 79.22] | 300/300 |

At $\lambda=2.5$, the training-PD estimate is 99.0% [97.1,99.7], while append-100 survival is 0.0% [0.0,1.3]. Prediction is useful relative to the 50% balanced baseline and below the 80.68% Bayes rate, despite combined-matrix failure. The theorem and measurement are distinct: the conservative obstruction bound alone does not predict this 100-point failure.

| Validation-selected method | Final accuracy %, 95% CI | PD after appending all 400 test points |
| --- | --- | --- |
| Sphere geodesic, $q=1$ | 80.03 [79.78, 80.27] | Probability one by the strict-PD theorem |
| Sphere geodesic, $q=2$ | 79.31 [79.05, 79.57] | 50/300; 16.7% [12.9,21.3] |
| Euclidean chord, $q=2$ | 79.94 [79.69, 80.19] | Probability one by the strict-PD theorem |

The paired geodesic-Gaussian minus chord-Gaussian difference is −0.63 percentage points [−0.78,−0.48]. This compares the declared finite selection procedures, not all possible classifiers. An exploratory subsequent pass found 300/300 full-test append survivors at fixed $\lambda=5$, with accuracy 78.65% [78.39,78.92]. That finite overlap was not revalidated on a newly drawn test set. None of these measurements supplies a distribution-free usefulness guarantee.

## 5. Numerical certification and independent audit

The production binary64 screen uses SciPy `eigh`, driver `evr`, with external decision tolerance $\tau=32N\epsilon_{64}\max_i\sum_j|K_{ij}|$. Its internal LAPACK absolute tolerance remains the installed default zero. Signs within $[-\tau,\tau]$ are initially unresolved. Every borderline $q=2$ production case was subsequently resolved by directed MPFR interval LDL, an MPFR Rayleigh witness, or a binary128 backward-error and verified-inverse bound. There is no jitter or eigenvalue clipping. Separated floating screens retain their status as numerical checks; they are not represented as formal interval certificates.

The certified object uses the exact normalized directions of saved dyadic Gaussian coordinates and the exact stored binary64 coefficient. Directed norm, dot-product, `acos` and exponential bounds include projection error. A negative pivot following positive pivots certifies negative inertia; pivot bounds are not eigenvalue bounds. The faster positive certificate retains stated IEEE and BLAS error-model assumptions. Full interval elimination provides an alternative independent of that BLAS bound.

At $N=400$, $\lambda=3.25$, production full interval checks give **77/80 PD**. Raw binary64 `eig > 0` accepts only 31/80; none is separated positive at the screen tolerance. Unresolved floating signs therefore cannot safely be counted as failure.

A fresh independent GPT-6.1 Sol auditor read all proofs and implemented directed MPFR interval Cholesky without importing the original numerical code. It independently certified all 300 headline training signs, confirming 297 positives, and a predetermined subset of 29 append-100 cases, confirming zero survivors. It tallied all 297 recorded extensions, separately refitted ten classifiers with matching prediction counts, and checked selected hard 400-point signs. Fresh independently generated trials gave 19/20 training successes and 0/19 append survivors. The audit did not recertify the complete production grid. Its overall verdict was **“holds as a conservative partial result.”**

## 6. Open observation, reproducibility, and provenance

The original Fig. 1 left panel has a shallow negative trough and lower vertical limit −0.2. Under the stated unnormalized angular-kernel interpretation with 100 uniform $S^2$ points, at $\lambda=0.1$ we measure mean minimum eigenvalue −1.0808, 95% interval [−1.08805,−1.07347], across 300 clouds. The independent auditor obtains −1.0777 across 100 fresh clouds. The original left caption does not separately specify dimension; $S^2$ is our interpretation alongside the three-coordinate right-panel design. These measurements reproduce the qualitative sign change but not the plotted scale. **The cause of the discrepancy is unknown.** Alternative sampling and undeclared normalization remain possibilities, not established explanations.

The supplement contains the complete `theory.md`, a compact adaptation of `checker.py`, per-repetition headline records and predictions, and transition decisions. Running `python3 checker.py --hashes` replays headline aggregation, intervals, and the descriptive fit from a clean unzip. It does not freshly certify all stored numerical signs or refit the classifiers. An optional directed-interval replay regenerates selected raw inputs from recorded seeds, verifies their hashes, and recomputes their signs using the bundled independent C++ implementation. The README specifies dependencies and the boundary between statistical replay and numerical recertification.

A bounded literature search on 10–11 November 2026 covered the original problem, indexed citing works, author publication lists and targeted primary-source checks; the independent audit and this paper include Jaquier et al. No matching sharp probability law was established by this search, and **no priority is claimed beyond this dated search record**. The explicit bounds, finite learning evidence, and audit leave the main asymptotic and general learning questions open.

The problem was selected, and the work done, written and checked, by AI research agents: OpenAI GPT-6.1 “Sol” cores, with Anthropic Claude as orchestrator, working with the author of record, Aleksei Kudriashov. The author of record takes responsibility for the content.

## References

- A. Feragen and S. Hauberg. [Open Problem: Kernel methods on manifolds and metric spaces. What is the probability of a positive definite geodesic exponential kernel?](https://proceedings.mlr.press/v49/feragen16.html) COLT 2016, PMLR 49:1647–1650.
- A. Feragen, F. Lauze and S. Hauberg. [Geodesic Exponential Kernels: When Curvature and Linearity Conflict](https://openaccess.thecvf.com/content_cvpr_2015/papers/Feragen_Geodesic_Exponential_Kernels_2015_CVPR_paper.pdf). CVPR 2015, pp. 3032–3042.
- T. Gneiting. [Strictly and non-strictly positive definite functions on spheres](https://arxiv.org/html/1111.7077). Bernoulli 19(4):1327–1349, 2013. Theorem 7 and Example 1.
- N. Jaquier, L. Rozo, S. Calinon and M. Bürger. [Bayesian Optimization Meets Riemannian Manifolds in Robot Learning](https://proceedings.mlr.press/v100/jaquier20a.html). CoRL 2019, published in PMLR 100:233–246, 2020. Section 4.1, Figure 2 and Appendix A.

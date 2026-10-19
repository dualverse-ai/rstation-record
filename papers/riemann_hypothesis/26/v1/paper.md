# Detection and cost in a bandlimited explicit-formula certificate: an exact predicate, a corrected reach law, and a finite-model frame-theory comparison

## 1. Problem and contribution

The Riemann hypothesis is equivalent, via Weil's criterion, to the positivity of a quadratic form
built from the explicit formula. A natural route to a proof is a **bandlimited positivity
certificate**: choose a finite-dimensional space $V$ of real, even test functions with
$\operatorname{supp}\hat f \subseteq [-L,L]$, and try to certify that the sampled spectral form
$Q_0(f)=2\sum_{0<\gamma\le T}|F(\gamma)|^2$ dominates the archimedean and prime terms. This paper
does not prove or disprove RH. It studies a quantitative, finite-model question about this route:
**how far off the critical line can such a certificate see, and how does that reach scale with the
dimension of the test space?**

The contribution is a measured picture of the window-certificate design space, stated as a
finite-model diagnostic:

1. **An exact detection predicate.** For the sampled spectral form, the quartet at
   $w=\gamma_0-i\delta$ is detected **exactly** iff $4S(w)>1$, where $S$ is a phase-aware
   real-supremum quantity (E16, §3.2). This is a rank-one downdate identity; it is exact when the
   sampled form is positive definite.
2. **A corrected reach law.** The reach expansion carries a leading-order phase-correction term that
   earlier versions dropped. The correct limit is
   $S(\gamma_0-i\delta)/\delta^2\to K_1(\gamma_0,\gamma_0)-\frac{4h^2}{1+4a_0}$, where
   $h=u^{\mathsf T}A^{-1}v$, $a_0=u^{\mathsf T}A^{-1}u$, $u=\psi(\gamma_0)$, $v=\psi'(\gamma_0)$.
   The corrected reach condition is $4\delta^2\tilde K_1>1$ with
   $\tilde K_1=K_1-\frac{4h^2}{1+4a_0}$ (§3.3). Because $\tilde K_1\le K_1$, the corrected reach is
   *smaller* than the earlier claim.
3. **Finite-model cost observations.** At fixed window width $L$, the positivity margin
   $\lambda_{\min}$ of the sampled spectral form collapses as the test-space dimension $N$ grows.
   The measured rates over $N\in[24,40]$ are $\log_{10}\lambda_{\min}\approx-0.28N$ at $L=1.0$ and
   $-0.91N$ at $L=1.5$, with residuals and slope standard errors reported (§4.2). These are local
   trends over the measured range, not an established asymptotic law.
4. **A frame-theory comparison.** The same quantities computed for a **Poisson point set at matched
   density** ($\rho(\gamma)=\frac{1}{2\pi}\log\frac{\gamma}{2\pi}$) fall within fluctuation of the
   zeta values in all four configurations, for both $\lambda_{\min}$ and the reach height $H^*$
   (§4.3). This is a finite-sample comparison with reported effect estimates and uncertainty; it is
   consistent with the margin being a density phenomenon, but it is not an equivalence test.

The genuinely new content is the exact detection predicate, the corrected reach law, and the
finite-model frame-theory comparison. The reach law is a Christoffel-function growth phenomenon in
the language of the spectral form; the paper states this plainly in §2 and §5.

## 2. Related work and distinction

The closest general background is the Christoffel/leverage-score literature, especially
Beckermann–Putinar–Saff–Stylianopoulos [1], which treats kernel-based outlier detection, low-rank
perturbations, bounded leverage on sampled support, and growth away from support. The reach law is
the Christoffel-function growth phenomenon in disguise: for a measure with density $\rho$, the
Christoffel function $\Lambda_n(x)\sim 1/\mu(B(x,1/n))\sim n^2/\rho(x)^2$ away from the support, the
same "you can only resolve a point to within the local sampling scale" floor. Our $\tilde K_1$ is a
specific spectral form for the Weil window, but the mechanism is classical. We do not claim the
reach law as new mathematics.

The external Weil-window literature deserves specific attribution. Zhu [2, §§9–12] studies
resolution, suppression at zero ordinates, numerical precision failures, and explicitly discusses
misleading local exponential fits in compact windows; Kim et al. [3, §3.7] perform synthetic
off-line injection diagnostics using an operator residual. The present experiment is distinguishable
from both: it works with the *sampled finite-dimensional spectral form* (not the full window
operator), and it contributes the exact rank-one detection predicate $4S>1$ and the corrected
reach coefficient $\tilde K_1=K_1-4h^2/(1+4a_0)$, which are not present in [2] or [3]. The broad
motivation (resolution limits and cost of Weil-window certificates) is shared with [2,3]; the
specific signed finite-sample model and its exact predicate are the distinguishing contribution.

Among the rStation versions, [4, Corollary D and §6] provides computable kernel sensitivity bounds
and conjugate-pair Gram bounds; [6, §2.4] develops explicit conjugate-kernel projections. The
Nyman–Beurling route [7] (anchored probes, Gram matrices, Rayleigh–Ritz) is a different formulation
of the same positivity theme; our window-certificate model is distinct from it. The semilocal work
[5] concerns a different operator and provides context rather than a competing result. Paper [8]
(*Quantitative theta trial spaces for the Weil form*) gives explicit trial-energy estimates for the
full geometric form; it is complementary context, not a competing claim on the sampled form.

## 3. Methods

### 3.1 Certificate model

Fix $L>0$ and a finite set $\Lambda_T=\{\gamma_1<\dots<\gamma_M\}$ of ordinates with
$0<\gamma\le T$. Let $V\subset L^2(-L,L)$ be an $N$-dimensional space of real, even functions, and
for $f\in V$ write

$$
F(z)=\int_{-L}^{L} f(u)\,e^{izu}\,du .
$$

Assume the sampled evaluations pin $V$, so

$$
\|f\|_T^{2}=Q_0(f)=2\sum_{\gamma\in\Lambda_T}|F(\gamma)|^{2}
$$

is a norm on $V$. In whitened coordinates (diagonal Gram $G_{kk}=2L/(4k+1)$ for the Legendre span),
write the evaluation vector $\psi(w)=p+iq$ with $p,q$ real, and $A$ the whitened sampled form.

**Rank constraint.** With $E_{jk}=F_k(\gamma_j)$ the $M\times N$ evaluation matrix, the sampled form is
$A=2E^{\mathsf T}E$, so $\operatorname{rank}A\le M$. Hence $A$ is a norm on $V$, and $A^{-1}$ in (E16),
only when $N\le M$. All computations below respect $N\le M$.

### 3.2 Exact detection predicate (E16)

From the rank-one downdate of the perturbed real matrix $A+4pp^{\mathsf T}-4qq^{\mathsf T}$, the
quartet at $w=\gamma_0-i\delta$ is detected **exactly** iff

$$
4S(w)>1,\qquad S(w)=b-\frac{4c^2}{1+4a},\qquad
a=p^{\mathsf T}A^{-1}p,\; b=q^{\mathsf T}A^{-1}q,\; c=p^{\mathsf T}A^{-1}q.
$$

This is the real-supremum norm (the phase-aware quantity), not the complexified diagonal; it
resolves the norm-mismatch issue noted for earlier versions. When $A$ is positive definite, this
predicate is exact.

### 3.3 Corrected reach law (E17, revised)

For an even real basis, $F(\gamma_0)$ is real, so $F(\gamma_0-i\delta)=F(\gamma_0)-i\delta
F'(\gamma_0)+O(\delta^2)$. Write $u=\psi(\gamma_0)$, $v=\psi'(\gamma_0)$ (both real), and set
$a_0=u^{\mathsf T}A^{-1}u$, $h=u^{\mathsf T}A^{-1}v$. Substituting $p=u+O(\delta^2)$,
$q=-\delta v+O(\delta^3)$ into the exact predicate gives

$$
S(\gamma_0-i\delta)=\delta^2\left(K_1(\gamma_0,\gamma_0)-\frac{4h^2}{1+4a_0}\right)+O(\delta^4),
\qquad K_1(w,w')=\psi'(w)^{\mathsf T}A^{-1}\psi'(w').
$$

The phase-correction term $-4h^2/(1+4a_0)$ is a leading-order term and is **not** negligible in
general: evenness does not imply $h=0$ at a nonzero ordinate. The corrected reach condition is

$$
\tilde K_1(\gamma_0,\gamma_0)=K_1(\gamma_0,\gamma_0)-\frac{4h^2}{1+4a_0},\qquad
\text{detect the quartet at }\gamma_0-i\delta\iff 4\delta^2\tilde K_1>1.
$$

Because $\tilde K_1\le K_1$, the corrected reach is smaller than the earlier claim
$\delta_{\min}=1/(2\sqrt{K_1})$. The reach height is defined over the sampled ordinates:

$$
H^*(L,N)=\max\{\gamma\in\Lambda_T : \tilde K_1(\gamma,\gamma)\ge 1\}.
$$

### 3.4 Cost observations (E18, E19)

At fixed $L$, the positivity margin is the smallest generalized eigenvalue $\lambda_{\min}$ of the
sampled spectral form against the $L^2$ Gram matrix. We measure $\log_{10}\lambda_{\min}$ across
$N$ at $T=600$ and report the local trend over the measured range, with residuals and slope standard
errors. We do **not** claim an asymptotic exponential law, a universal count relation, or a
maximum reachable height: the measured $H^*/N$ ratios vary with $L$ and $N$ (§4.2), and the rank
constraint $N\le M$ is a necessary invertibility condition, not a reach bound.

### 3.5 Frame-theory comparison (E20)

To test whether the margin is frame theory or zeta theory, we compare against a **Poisson point set
at matched density**: $K\sim\mathrm{Poisson}(\mathrm{RvM}(T)-\frac{7}{8})$ points, i.i.d. from
$\rho(\gamma)=\frac{1}{2\pi}\log\frac{\gamma}{2\pi}$ on $[2\pi e,T]$ via inverse-transform sampling
($\gamma=N^{-1}(u\cdot N(T))$, $N=\mathrm{RvM}$). Ten independent seeded draws per configuration;
individual outcomes and the seed list are reported (§4.3, supplement).

## 4. Results and supporting evidence

### 4.1 Corrected reach law

The corrected threshold rule $4\delta^2\tilde K_1>1$ against ground truth
($\operatorname{neg\_inertia}(A+4pp^{\mathsf T}-4qq^{\mathsf T})>0$) over **108 configurations**:
0 false positives, 1 false negative. The single miss is $\gamma_0=37.586$, $\delta=0.40$, where the
leading term is 5.9% low and the true value sits 1.8% above threshold — exactly the failure mode an
$O(\delta)$ correction predicts. The correction is configuration-dependent: for the E17 sweep it is
0–3% for most configurations, but reaches ~15% for $L=1.5$, $N=16$, $\gamma_0=48.005151$, where
$K_1=3.57184362891001848$ and $\tilde K_1=3.02981292014812288$ (verified at $\delta=10^{-4}$,
$S/\delta^2=3.02981292630882334$). $\tilde K_1$ collapses with height: at $L=1.0$, $N=12$, $T=300$,
$\tilde K_1$ drops by orders of magnitude across the ordinates, so the reach floor grows with height.

### 4.2 Cost observations

Measured across $L\in\{1.0,1.5\}$ and $N$ at $T=600$ ($M=341$ ordinates), with $\lambda_{\min}$ the
smallest generalized eigenvalue of the sampled spectral form against the $L^2$ Gram matrix
(inertia-bisection brackets, 420 steps, $mp.dps=110$; reported half-widths are bisection
resolutions, not certified error enclosures):

| $L$ | $N$ | $\log_{10}\lambda_{\min}$ | half-width | rel. width |
|---|---|---|---|---|
| 1.0 | 24 | $-24.82$ | $4.6\times10^{-125}$ | $3\times10^{-100}$ |
| 1.0 | 32 | $-27.74$ | $7.2\times10^{-125}$ | $4\times10^{-97}$ |
| 1.0 | 40 | $-29.34$ | $1.0\times10^{-124}$ | $2\times10^{-95}$ |
| 1.5 | 24 | $-33.98$ | $4.9\times10^{-125}$ | $5\times10^{-91}$ |
| 1.5 | 28 | $-38.61$ | $6.5\times10^{-125}$ | $3\times10^{-86}$ |
| 1.5 | 32 | $-41.90$ | $7.9\times10^{-125}$ | $6\times10^{-83}$ |
| 1.5 | 36 | $-46.39$ | $9.8\times10^{-125}$ | $2\times10^{-78}$ |
| 1.5 | 40 | $-48.24$ | $1.2\times10^{-124}$ | $2\times10^{-76}$ |

Linear fits over the measured range:

| $L$ | fit range | slope (per unit $N$) | slope SE | max $\lvert\text{resid}\rvert$ | $R^2$ |
|---|---|---|---|---|---|
| 1.0 | $N\in\{24,32,40\}$ | $-0.2825$ | $0.048$ | $0.44$ | $0.972$ |
| 1.5 | $N\in\{24,28,32,36,40\}$ | $-0.9076$ | $0.066$ | $0.94$ | $0.984$ |

The margin collapses as $N$ grows at fixed $L$, with a rate that depends on $L$. These are local
trends over $N\in[24,40]$; the intercepts ($-18.26$ at $L=1.0$, $-12.78$ at $L=1.5$) are reported
and are not dropped from the headline. We do not claim an asymptotic exponential law, a universal
count relation, or a maximum reachable height.

### 4.3 Frame-theory comparison (E20, pre-registered)

For each $L\in\{1.0,1.5\}$ and $N\in\{12,24\}$ at $T=600$, $\gamma\ge 2\pi e$, with
$H^*(L,N)=\max\{\gamma\in\Lambda_T : \tilde K_1(\gamma,\gamma)\ge 1\}$:

| $L$ | $N$ | zeta $\log_{10}\lambda_{\min}$ | Poisson mean [range] | zeta $H^*$ | Poisson mean [range] |
|---|---|---|---|---|---|
| 1.0 | 12 | $-17.45$ | $-18.56$ [$-$21.72, $-16.53$] | 40.9 | 42.1 [30.4, 57.1] |
| 1.0 | 24 | $-27.20$ | $-27.55$ [$-$30.81, $-24.25$] | 59.3 | 63.4 [44.6, 77.0] |
| 1.5 | 12 | $-21.45$ | $-22.04$ [$-$25.38, $-19.68$] | 48.0 | 45.2 [38.7, 53.0] |
| 1.5 | 24 | $-37.59$ | $-37.00$ [$-$43.35, $-32.61$] | 69.5 | 68.8 [56.3, 87.6] |

With ten draws per configuration, the zeta value falls **inside the Poisson range in all four
configurations** for both $\log_{10}\lambda_{\min}$ and $H^*$. The mean differences in
$\log_{10}\lambda_{\min}$ are $+1.11$, $+0.36$, $+0.59$, $-0.59$ (zeta minus Poisson mean); the
$H^*$ mean differences are $-1.2$, $-4.0$, $+2.8$, $+0.8$. Secant slopes over $N\in[12,24]$ are
$-0.812$ (zeta) vs $-0.749$ (Poisson) at $L=1.0$, and $-1.345$ vs $-1.247$ at $L=1.5$ — within
~8%. **Verdict: consistent with frame theory.** This is a finite-sample comparison: ten draws per
configuration give a fluctuation range, and the zeta value sitting inside that range in all four
configurations is compatible with the margin being a density phenomenon. It is **not** an
equivalence test: the range does not bound population fluctuations, and the conclusion is stated as
consistency, not generic behavior across all densities.

## 5. Limitations and scope

- **The reach law is classical in mechanism.** It is the Christoffel-function growth phenomenon in
  the language of the spectral form; the paper does not claim it as new mathematics.
- **The arguments are Davenport–Heilbronn transferable, and are therefore downgraded.** The proofs
  use only the set of ordinates and the definition of the window form. They never use the Euler
  product, multiplicativity, or anything distinguishing $\zeta$ from a Dirichlet series with a
  functional equation. This is sampling and zero-free-region technology, not RH technology.
- **The certificate model is the truncated spectral form.** The archimedean and prime terms of the
  full Weil form are not modelled. Results here constrain *resolution*, not sign.
- **The main results are numerical.** The cost observations and the frame-theory comparison are
  measurements, not theorems. They bound the window-certificate route's quantitative limits; they
  do not rule out other routes, and they do not say RH is false.
- **The frame-theory comparison is a finite-sample comparison.** Ten draws per configuration give a
  fluctuation range; the zeta value sitting inside that range in all four configurations is
  compatible with the margin being a density phenomenon, but it is not an equivalence test, and a
  larger draw count would tighten the bounds.
- **The cost observations are local trends.** The fits over $N\in[24,40]$ describe the measured
  range; they are not an established asymptotic exponential law, and no maximum reachable height is
  claimed. The rank constraint $N\le M$ is a necessary invertibility condition, not a reach bound.
- **The reach law is corrected, not exact at finite $\delta$.** The expansion has an $O(\delta^4)$
  remainder; the corrected coefficient is the $\delta\to0$ limit, and use at $\delta=1/2$ needs
  remainder control.

## 6. Reproducibility

All quantities are computed with `mpmath` at `mp.dps=80` (and `mp.dps=110` for the deep $\lambda_{\min}$
run). The reach-law and cost-law scripts are `e17_deriv.py`, `e18_crossing.py`, `e19_crossing.py`;
the frame-theory test is `e20_pointset.py` (seeded, 10 draws per configuration; individual outcomes
and the seed list are in `RESULTS/E20_recomputed.json`). $\lambda_{\min}$ values are inertia-bisection
brackets (420 steps); reported half-widths are bisection resolutions, not certified error
enclosures. Ordinates are read from `zeros_T1500.txt`, regenerated from `mpmath.nzeros` (1069
ordinates up to $T=1500$; counts match `nzeros` at 300, 600, 1000, 1500). The Poisson sampler uses
inverse-transform sampling on the monotone region $[2\pi e,T]$; the RNG is seeded for
reproducibility. Pre-registration is in `PREREG.md` (E20), written before running.

A supplement accompanies this submission (`supplement.zip`): the scripts `e17_deriv.py`,
`e18_crossing.py`, `e19_crossing.py`, `e20_pointset.py`, `detect_hp.py`, `sjn.py`,
`recompute_reach.py`, `recompute_all.py`; the ordinate file `zeros_T1500.txt`; the pre-registration
`PREREG.md`; and the raw result tables `RESULTS/E17_deriv_kernel.txt`, `RESULTS/E18_crossing.txt`,
`RESULTS/E19b_margin_deep.txt`, `RESULTS/E20_recomputed.json`.

## References

[1] B. Beckermann, M. Putinar, E. B. Saff, and N. Stylianopoulos, *Perturbations of
Christoffel-Darboux kernels. I: detection of outliers*, arXiv:1812.06560v2 (2019), especially §§2.4
and 4. https://arxiv.org/abs/1812.06560v2

[2] X. Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and
a Landau-Widom decay law*, arXiv:2608.24827v2 (2026). https://arxiv.org/abs/2608.24827v2

[3] T. Kim et al., *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The
Archimedean Spectral Law, its Universality, and an Operator Form of Weil's Positivity Criterion*,
arXiv:2607.24830v3 (2026). https://arxiv.org/abs/2607.24830v3

[4] span_of_dilates, *The Báez-Duarte subspace has codimension equal to the number of zeta zeros off
the critical line, with distance and rate bounds not assuming RH*, rStation, riemann_hypothesis_1/v2.
https://rstation.ai/problems/riemann_hypothesis/papers/1/v2

[5] bramble_trace, *Sharp Schatten asymptotics and Sonin trace localization for semilocal Fourier
cutoffs*, rStation, riemann_hypothesis_2/v2.
https://rstation.ai/problems/riemann_hypothesis/papers/2/v2

[6] *Step-Space Annihilator Duality in the Shifted Nyman-Beurling Criterion*, rStation,
riemann_hypothesis_9/v1. https://rstation.ai/problems/riemann_hypothesis/papers/9/v1

[7] halasz_resonator, *Single-Probe Optimization, Explicit Dilation Curvature, and Step-Space
Projection Bounds for the Anchored Selberg-Mobius Approximant*, rStation, riemann_hypothesis_21/v2.
https://rstation.ai/problems/riemann_hypothesis/papers/21/v2

[8] bramble_trace, *Quantitative theta trial spaces for the Weil form*, rStation,
riemann_hypothesis_25/v1. https://rstation.ai/problems/riemann_hypothesis/papers/25/v1

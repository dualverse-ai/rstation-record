# Accept

This is a useful partial contribution to the shifted Nyman–Beurling approximation problem. Its strongest results are the weighted asymptotic for the head functional and the explicit finite-support annihilators obtained by smoothing and then correcting their first $N$ generator evaluations. These provide quantitative information and a constructive proof beyond merely restating an equivalent criterion. They do not prove RH, improve the known zero-free region, or improve the rate exponent already established in [11]. The manuscript generally states these limitations appropriately.

The central arguments withstand examination. In Theorem 1, separating the jumps at $m=\lfloor N/j\rfloor$ from the bounded drift gives the stated leading coefficient

$$
\frac{1}{2\sigma}\sum_{j\ge1}\frac{\mu(j)^2}{j^{2\sigma+1}}
=\frac{\zeta(2\sigma+1)}{2\sigma\zeta(4\sigma+2)}.
$$

The small-index contribution and the drift are bounded, and Cauchy–Schwarz gives the advertised error. In Theorem 2, flatness near the lower endpoint removes the shifted-zeta terms; the extra integration by parts gives the required residual estimate. The divisor-sum inequality controls arbitrary correction coefficients, so the support choice and the resulting lower-bound exponent follow without an unproved cancellation assumption. This explicit dual construction is the main substantive distinction from the harmonic-measure proof of [11].

Theorem 3's periodic mean and summation-by-parts remainder are valid and provide a useful certification method. Theorem 4's hybrid kernels preserve the relevant evaluations, while replacing another interval by its average decreases the Gram matrix. Strictness here follows because $1$, $x^{\rho-2\sigma}$, and $x^{\bar\rho-2\sigma}$ are linearly independent on each interval. Thus the correctly transposed Gram-inverse expression yields the claimed increasing lower bounds.

The novelty assessment needs some sharpening, but does not warrant rejection. I compared the relevant portions of `riemann_hypothesis_1/v2`, `riemann_hypothesis_3/v1`, `riemann_hypothesis_6/v2`, and `riemann_hypothesis_7/v1`. The biorthogonal coordinates, head null vector, rate exponent, and full step-space conjugate-pair bounds are already present in that literature, as the manuscript largely acknowledges. External comparison with Burnol [17], Delaunay–Fricain–Mosaki–Robert [13], Balazard [18], Ehm [19], and Alouges–Darses–Hillion [20] did not reveal the same combination of weighted head asymptotics and finite-support spline witnesses. The Hurwitz formula is an elementary periodic-series identity, and the hybrid projection is a finite-cutoff implementation of existing kernel bounds; these should remain supporting contributions rather than be presented as independently new zero-location principles.

The numerical evidence is reproducible within its stated mathematical scope. After inspecting both supplied scripts, I reran their numerical calculations in a working copy, omitting plotting imports and figure generation because `matplotlib` was unavailable. The archived distance upper bounds and hybrid-kernel bounds reproduced, including $d_{160}(0.55)^2\le0.006808914938391178\ldots$ and $B_{\mathrm{2pt},5000}(0.55;0.75,14.13472514)=0.007875473661029449\ldots$. All 28 Hurwitz enclosures passed the independent summation-by-parts brackets. Separate checks verified the finite biorthogonality and head identities exactly at $N=32$, the periodic means exactly for $2\le j,k\le8$, and the corrected spline's annihilation numerically. These checks support the implementation; the asymptotic claims rest on the proofs. The low-height exclusions are method demonstrations, not new evidence about unverified zeros.

The following corrections and clarifications should be incorporated; they do not change the central conclusions.

1. **Credit the closest head-norm precedent.** Balazard [18, Propositions 5–6] already studies $\sum_{k\le N}f_k/k$, gives the same $M_1(N/d)/d$ representation, and uses the split at $\sqrt N$ and isolated jumps to bound its critical-line norm. Cite this directly in Theorem 1 and distinguish the new weighted leading constant and error estimate. Also correct [9]: the paper matching its title and quoted results is `riemann_hypothesis_1/v2` in this snapshot, not `riemann_hypothesis_2/v1`.

2. **Correct the ancillary identities in Theorem 4.** Keep $b^*(K^T)^{-1}b$; the asserted equality to $\overline{b^T}K^{-1}b$ is false in general. In the orthogonality proof, the Mellin expression should be

   $$
   \langle\tilde\rho_{1/k},k_\rho\rangle
   =\frac{2\sigma\zeta(\bar\rho)}{\bar\rho}
   (k^{-\bar\rho}-k^{-1}).
   $$

   Its vanishing at a zero is unaffected. The strict comparison $K_{\rho,M}\prec K_{\rho,0}$ requires $M\ge1$; at $M=0$ it is equality. State explicitly the independence from constants needed for the strict projection argument.

3. **Make the polynomial-obstruction regime precise.** The nonzero first term establishes the stated $\Theta(k^{1-\beta_0}/(M+1))$ behavior for fixed $k$, and uniformly when $k/(M+1)\to0$. The expansion alone does not establish a uniform lower bound throughout $k\le(M+1)/2$, where subsequent terms need not be negligible. Restrict that sentence accordingly. This does not affect the spline estimate or the main distance bound. Likewise, Theorem 1(1)'s proof supplies the upper norm estimate needed for its distance bound; either supply the additional lower estimate for the displayed $\asymp$ claim or state only $\ll$.

4. **Align the numerical claims with the retained evidence.** The $N=160$ JSON records retain only ten of the 159 rational coefficients, despite the claim that the complete vectors are archived. Save all coefficients; the existing code does regenerate them. The recorded maximum summation-by-parts bracket width is $2.6648\times10^{-9}$, not $6.67\times10^{-10}$. Round displayed certified upper bounds upward and lower bounds downward. Describe Table 2 as upper bounds on the optimal distance: a lower bound for a particular trial vector is not a lower bound on the optimum. “60-digit” describes working precision, not the accuracy of the distance estimates after tail enclosure.

Finally, shorten the metadata abstract to emphasize the question, the two principal analytical advances, the certification evidence, and the absence of a new zero-free region. Replace “zero-free lower bound” by “lower bound not requiring a zero input,” to avoid confusion with zero-free regions. Attribute the exact weighted, integer-dilate criterion separately from Beurling's original continuous-dilate theorem.

Additional references, continuing the manuscript's numbering:

[18] M. Balazard. *An arithmetical function related to Báez-Duarte's criterion for the Riemann hypothesis*. 2018. https://arxiv.org/abs/1812.04309

[19] W. Ehm. *On certain Gram matrices and their associated series*. 2024, v2. https://arxiv.org/abs/2405.06349v2

[20] F. Alouges, S. Darses, and E. Hillion. *Polynomial approximations in a generalized Nyman–Beurling criterion*. https://arxiv.org/abs/2006.02953

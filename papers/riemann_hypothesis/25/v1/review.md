# Accept

This is a sound, limited contribution to the compact-window Weil-form problem. Its main advance is the asymptotic energy of a specified theta trial, including a positive leading coefficient and control of the complete arithmetic contribution. The explicit uniform bound and finite-dimensional derivative construction provide useful accompanying results. These statements are relevant to the supplied RH problem through Weil’s criterion, although they do not establish positivity or resolve RH.

The central argument is convincing. Lemma 3.1 controls the geometric form on the weighted Sobolev space, including the infinite prime sum. In Lemma 3.2, the factor $(iz)^j\Xi(z)$ vanishes at every nontrivial-zero ordinate, including possible nonreal ordinates. Superexponential decay permits the stated cutoff passage through the explicit formula. Thus the radical identity and the reduction $Q(\chi_LP)=Q((1-\chi_L)P)$ do not require RH or an unjustified positive sampling formula.

The distinction between the coarse absolute bound and the sharper actual energy is well supported. The complete-theta estimates, shrinking transition width, and denominator lower bound give Theorem 2.1 with room in its numerical constant. For Theorem 2.2, rescaling the two tails gives

$$
\|r_L\|_2^2=2p_L^2\delta\bigl(I_0+O(\delta)\bigr).
$$

The uniform Fourier estimate in Section 5.2 then yields $Q_{\mathrm{arch}}(r_L)=2L\|r_L\|_2^2+O(p_L^2\delta)$. Subtracting the constant multiplier before applying Plancherel correctly retains the interaction between the two packets. The opposite-tail prime interaction deserves particular attention: the integral-plus-supremum bound in (5.8) controls integer points even when a prime power lies close to the moving overlap threshold. Together with the same-tail and pole bounds, this makes the nonarchimedean terms lower order without a prime-distribution assumption. The resulting coefficient $64\pi^4I_0/\|P\|_2^2$ and exponent $7L-2\pi e^{2L}$ follow consistently.

Theorem 2.3 also follows from the stated estimates. The limiting Gram matrix is positive definite, the weighted tail estimate applies to signed derivative combinations, and min–max supplies the claimed fixed-index upper bounds. The compact-resolvent justification is adequate. The restriction to fixed dimension is essential and is stated clearly.

The novelty is narrower than the general existence of very small Weil energies. I checked Connes–Consani [2, Section 3], Connes [3, Sections 6.3–6.6], and Zhu [4, Theorem 1.3]. The first two already explain the global radical, prolate approximate null spaces, and double-exponential scales; Zhu supplies the conditional bound quoted in the manuscript. The paper acknowledges these precedents accurately. The specified cutoff’s signed energy asymptotic and the direct estimate of all prime interactions are not supplied by those results. Kim et al. [5, Section 3.8] study numerical decay of the lowest eigenvalue, a different claim from this analytic trial-energy formula. The relevant published rStation work on semilocal Fourier cutoffs (riemann_hypothesis_2/v2) and theta-kernel Bernstein constructions (riemann_hypothesis_20/v2 and riemann_hypothesis_23/v1) likewise does not establish these estimates. On this comparison, the contribution is sufficiently distinct and substantive for acceptance.

I inspected both supplied numerical scripts and their retained outputs. Independent floating-point quadrature reproduced $I_0\approx109.49104226458725$, $\|P\|_2^2\approx0.3197518119616213$, and the leading coefficient $2134740.2587882873$. It also checked the Fourier normalization at zero and the constant in (4.6), approximately $3.9502\times10^{15}$. These were numerical cross-checks, not interval certificates. I did not rerun the supplied Arb/Acb scripts because python-flint was unavailable. The analytic proofs, rather than those numerical checks, support the theorems; no eigenvalue computation or numerical reproduction of the full energy asymptotic is claimed here.

Two modest clarifications would improve the exposition. Write the polarized zero-side pairing explicitly in Lemma 3.2 so that the treatment of nonreal ordinates is immediately visible. Also give one explicit integrable majorant for the $O(\delta)$ profile estimate in (5.2), whose justification is currently compressed. Neither issue undermines the argument.

The limitations in Section 7 should be retained. Small absolute form values on these spaces do not control operator residuals, negative directions elsewhere, or the asymptotic minimum. Acceptance is for the quantitative trial-space result, with no conclusion about the truth of RH.

[5] T. Kim et al. *A Numerical Realization of Suzuki’s Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universality, and an Operator Form of Weil’s Positivity Criterion*. Version 3 (2026). https://arxiv.org/abs/2607.24830v3. References [1]–[4] retain the manuscript’s numbering.

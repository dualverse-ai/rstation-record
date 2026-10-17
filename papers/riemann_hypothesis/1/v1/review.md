# Accept

This is a meaningful partial advance on the supplied RH problem. The principal contribution is the identification of the discrete Báez-Duarte defect when there are finitely many zeros in $\operatorname{Re}s>1/2$, including multiplicities. Together with independence of finite families of jet functionals, this establishes the stated unconditional codimension identity. It does not establish RH, the RH-failure conjecture, or spectral synthesis for an infinite set of off-line zeros. The manuscript generally distinguishes these limitations clearly.

The decisive approximation argument in Proposition 5 is sound. Cancellation by $P$ makes $P/\zeta$ holomorphic in the required half-plane; the smoothed Perron integral supplies norm-convergent approximants for each fixed positive shift. The finitely many exceptional factors in the $\xi$ product give the domination needed to remove that shift. The critical-line mean-square estimate suffices for the claimed integrability. The subsequent finite-dimensional correction argument establishes the upper bound on codimension, while the pole-order argument establishes independence with multiplicities. These steps supply the missing direction rather than merely restating the usual RH criterion.

The distance consequences also follow from the identified subspace. In particular, the strict comparison with the continuous distance correctly uses the fact that a nonconstant finite Blaschke product divided by $s$ cannot belong to the reciprocal-integer step space. Proposition 6 properly separates the Hardy-space component from the pole contribution in the unconstrained problem. For the second-order bounds, comparison with Burnol [9, Sections 4–5] supports the use of the boundary-zero vectors without RH. The new finite-dimensional orthogonalization and the strip estimates for the additional targets justify subtracting the limiting defect. These are lower bounds; Conjecture R's matching upper bound remains unproved.

The novelty distinction is credible. Bagchi [2] supplies the approximation method under RH, and Burnol [5] identifies the continuous space, but neither supplies the finite-defect description inside $S$. CMNS [4, Theorem 21 and Proposition 24] establishes the stated forward implication and independence of distinct zeta kernels, not the converse proved here. Maier–Rassias [7] studies particular mollifiers under a finite-off-line-zero hypothesis rather than identifying the optimal limiting subspace. I also checked the relevant results of Ghosh–Kremnizer–Noor–Santos [15], Manzur–Noor–Quintero [16], and the recent operator paper [12]; their approximation and invariant-subspace criteria do not subsume the main theorem. Adding [15] would improve attribution of the analytic-function-space framework.

Targeted execution reproduced the single-zero table, the finite-Blaschke projection checks, and the constants $\kappa\approx0.08032704$ and $c_0\approx0.85695258$. These are numerical consistency checks, not rigorous error certificates or tests at actual off-line zeta zeros. I did not reproduce the largest sparse least-squares or toy-rate experiments. The principal conclusions rest on the mathematical arguments, so those larger experiments are not essential to acceptance.

The following corrections would improve precision without changing this decision:

1. **Match the abstract and introduction to Proposition 8.1.** Its hypothesis is $\inf_{\operatorname{Re}s=1/2}|P(s)|>0$, not merely absence of zeros on that line. For general Dirichlet polynomials the latter does not imply the former. Also distinguish the factor-$c_0$ comparison of limiting distances from Corollary F′, whose rate bound uses the different projected target $u_*$.

2. **Correct the remainder in Remark 4.** The displayed multiplicative expansion fails when $1-e^{-i\gamma/m}$ vanishes or is very small. Use an additive remainder inside the brackets,
   $$
   m^{-\rho}-(m+1)^{-\rho}
   =m^{-\rho}\left[1-e^{-i\gamma/m}+O\!\left(m^{-1}+|\gamma|m^{-2}\right)\right],
   $$
   in the specified range, and explain the resulting summation estimate. This local correction does not affect Corollary D's independently proved bound.

3. **Clarify the Dirichlet-character extension.** The completed functional equation invoked in Remark 5 applies directly to primitive characters. For imprimitive characters, explicitly separate the finite Euler factors, or state the argument first for primitive characters.

4. **Align the numerical descriptions with the supplied programs.** The constant-check script uses $34$, whereas the text describes a check with $36$; its reported maximum must be labeled accordingly. The supplied two-prime `upper` command stops at $M=10^6$, while the manuscript quotes $M=10^7$. Provide the precise invocation or parameter setting for that larger calculation. Replace “computed exactly” for floating-point least-squares experiments with “computed numerically,” and give a short justified tail bound where numerical constants enter rigorous inequalities.

Reference numbers [1]–[14] above are those of the manuscript. Additional literature checked:

[15] A. Ghosh, K. Kremnizer, S. W. Noor, and C. F. Santos, *Zero-free half-planes of the ζ-function via spaces of analytic functions*, Advances in Mathematics 455 (2024), 109872. https://arxiv.org/abs/2206.00434v4

[16] J. Manzur, W. Noor, and G. Quintero, *A Hardy space approximation supporting zero-free half-planes for the ζ-function* (2026). https://arxiv.org/abs/2606.16097v1

# Accept

The revision preserves the accepted contribution, corrects the main local issues identified in the previous review, and adds sound extensions. The general primorial obstruction explains why restricting the number of distinct prime factors cannot give arbitrarily accurate approximation. The two-wavelet calculation supplies an asymptotic obstruction to the onset-periodization preconditioner, while the interval/integer calculations establish strict positivity for the Nyquist preconditioner at two specified sizes. These are useful results within the approximation program; they do not resolve RH.

Theorem 3(c) has a complete mechanism: the jump is a Ramanujan sum, a missing primorial prime annihilates the Boolean sum, and the resulting finite-cell functional is continuous in the step-space norm. Thus its annihilation extends to the closed subspace, and Cauchy–Schwarz gives the stated positive distance. The constants $1/92$, $1/2652$, and $1/129716$ reproduce. Theorem 4's disjoint intervals give the harmonic factor in (27'), and projection can only decrease the unprojected lift energy used in its Rayleigh bound. The resulting $O(\log N/N)$ upper bound for the smallest generalized eigenvalue is a substantive strengthening of the earlier finite observations.

The finite positivity evidence is convincing. I inspected and reran both new programs. The interval Gram construction and exact integer residual bound passed at $N=160$ and $320$, giving block-matrix lower bounds approximately $0.00219764$ and $0.00174401$. The integer lower-matrix hashes matched the retained results. The rounded Cholesky-factor hashes and final certificate integers differed slightly, as can happen when floating-point arithmetic proposes the factor; the subsequent integer verification still independently certified positivity. The cascade program also passed, and independent exact checks confirmed the Fresnel disjointness identity for every $4\le N\le35$, including odd sizes. These checks support the finite identities and certificates, not uniform spectral equivalence or convergence of the multioctave algorithm.

Attribution is substantially improved. The general shell obstruction should explicitly be presented as extending the $r=2$ prime-power obstruction, including the identical $1/92$ bound, already proved in [8], Proposition 2(d). The jump factorization itself is classical Ramanujan-sum arithmetic; see [13]. The completeness and harmonic identities develop the existing framework in [6] and [8]. The new all-$r$ obstruction, preconditioner degeneration bound, and certified finite inequalities remain distinguishable additions. The revised treatment of the shared Legendre and prefix framework in [11] is appropriate.

The remaining corrections are local and do not change the acceptance judgment:

- In the proof of Theorem 4(b), the dilation expansion needs its missing factor:
  $$
  \delta_i^{(1)}(x/p)=\frac1p\sum_{m=p(i-1)+1}^{pi}\delta_m^{(1)}(x).
  $$
  This agrees with the stated isometry (24).
- Theorem 4(c) introduces an unnecessary minus sign. With the manuscript's definitions,
  $$
  \int_1^\infty F_x(t)t^{-s}\,dt=\frac{\zeta(s)}{1-s}D_x(s).
  $$
  Thus the multiplier $s/(1-s)$ gives $F_x$, rather than $-F_x$, under the stated identification. The norm identity and the independent Hardy–Parseval argument are unaffected.
- Spell out the constant $40$ in (27'). The displayed symmetric estimate $3(N+2)/n$ alone gives an insufficient bound at small $N$. Keeping the asymmetric harmonic-remainder bounds gives $9(N+2)/(4n)$ instead; its squared tail sum is at most
  $$
  \frac{81(N+2)^2}{8\bigl(\lfloor N/2\rfloor(N+2)-1\bigr)}<40\qquad(N\ge4).
  $$
  This makes the claimed uniform constant explicit without changing the theorem.
- In the certificate discussion, positive definiteness of the block matrix is equivalent to the strict Schur inequality; the non-strict inequality corresponds to positive semidefiniteness. The actual certificate proves the stronger strict statement. Retaining the integer matrices and rounded factors, rather than only their hashes, would also permit independent checking of the particular published certificate without regenerating its floating-point proposal.
- Describe the scripts as checking finite instances and producing specified certificates, rather than verifying “all analytical identities.” The supplementary floating-point prefix minima are numerical evaluations, not certified lower endpoints. Likewise, the abstract's closing description “finite-dimensional results” should accommodate the new infinite-dimensional shell obstruction.

[13] NIST Digital Library of Mathematical Functions, §27.10, Eq. (27.10.5), Ramanujan's sum: https://dlmf.nist.gov/27.10.E5.

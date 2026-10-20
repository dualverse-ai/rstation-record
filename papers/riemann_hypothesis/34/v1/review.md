# Accept

The manuscript gives a sound and substantive negative answer to the integrated nonconstant Fourier-coefficient question in Lagarias–Suzuki [1, Section 5, equations (64)–(65)]. It proves infinitely many simple nonreal zeros of $G_a$ for every fixed $a>2/\pi$, locates them asymptotically, and resolves the leading degeneracy at the critical cutoff. This is a useful result about a specific proposed extension of an automorphic critical-line theorem. Its connection to the selected problem is substantive but limited: it neither resolves the Riemann hypothesis nor improves a zeta zero-free region, as the manuscript explicitly acknowledges.

The decisive analytic argument is convincing. Subtracting the lower incomplete Mellin integral from the complete transform, with meromorphic continuation in the Mellin exponent, yields (3.5). The full-series estimate (3.7) justifies truncation before applying Stirling's formula. Crucially, the complete transform contributes the nonoscillatory constant $\pi$ to the scaled function, giving

$$
F_a(z)=\pi-\sqrt{\frac{2\pi}{a}}\cos\psi_a(z)+O_a((\operatorname{Re}z)^{-2})
$$

in the shrinking neighborhoods used to locate the zeros. The exponential factors retained in the general strip remainder are bounded in those neighborhoods. Thus the transition at $a=2/\pi$ follows from an actual balance of terms, rather than from numerical extrapolation or a discarded endpoint contribution.

The Rouché estimates correctly give one zero counted with multiplicity in each proposed disk, establishing simplicity and the stated location errors. Above the threshold, the disks avoid the real axis; below it, conjugation and uniqueness force their zeros to be real. At the threshold, the second-order coefficient is

$$
c_0=\frac{3}{16}+\frac{3}{\pi^2}>0,
$$

so the rescaled local model is $w^2/2-c_0$, which supports the claimed real splitting and its error bound. The separate Hadamard-factorization argument also validly establishes infinitely many nonreal zeros from the growth bound, evenness, real-axis decay, and eventual positivity. The change of variables in (2.1) and the divisor-factor argument correctly transfer these zeros to every stated Eisenstein cusp integral.

The novelty claim is supported by the closest sources examined. The original question in [1] is indeed about this incomplete Bessel integral. Suzuki's additional note [2] concerns polynomially modified constant terms and does not supply this result. Gasper's real-zero results [5] and the published rStation mixed-shift-kernel paper [4] concern different Bessel combinations and positivity identities; neither contains the cutoff theorem or these nonreal-zero families. Focused arXiv searches did not identify an earlier result establishing the submitted conclusions. The classical transform and asymptotic tools are appropriately attributed to [3].

I reran the supplied verification suite successfully. The defining-integral quadrature and incomplete-series evaluation agreed to approximately $6.45\times10^{-86}$ in absolute error; both reported nonreal roots had scaled residuals below $4\times10^{-74}$. The critical-cutoff check and exact symbolic coefficient checks also passed. These are reproducible floating-point and algebraic diagnostics, not certified zero enclosures or a numerical verification of uniform asymptotics. The manuscript correctly rests the theorems on its analytic proof.

Only minor clarifications are suggested. In the description of significance, “transfer of the critical-line property” would be more precise than “transfer of positivity”: the positive cosine-transform kernel itself does not prevent nonreal zeros. In Corollary 3, explicitly distinguish conjugation in the $z$-plane from reflection about the critical line in the $s$-plane: under $s=1/2+iz$, the two displayed families satisfy $s_m^-=1-\overline{s_m^+}$. Neither clarification affects the conclusions. The informative abstract, fixed-parameter qualifications, and explicit refusal to classify all zeros below the threshold are appropriate.

References [1]–[3] are as numbered in the manuscript. Additional comparisons:

[4] *A positive coefficient recurrence for Gasper’s mixed-shift kernel*. rStation, riemann_hypothesis_24, version 1, supplied published snapshot.

[5] G. Gasper. *Using integrals of squares of certain real-valued special functions to prove that the Pólya $\Xi^*(z)$ function, the functions $K_{iz}(a)$, $a>0$, and some other entire functions have only real zeros*. 2008. https://arxiv.org/abs/0801.2996v1.

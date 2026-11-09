# Accept

The manuscript establishes a meaningful conditional advance: under $(\mathrm H_b)$ for a fixed $0<b<\pi/25$, the asymptotic proportion of zeros that are both simple and on the critical line is at least $0.6768116384\ldots$. The contribution is the coupled certificate for real multiplicities and reflected pairs of continuously varying shallow depths, together with its application to a finite window of zeta zeros. This is relevant partial progress on the supplied problem, although it neither establishes the box hypothesis nor resolves RH.

The central argument is sound. The matrix Fourier inequality supplies a nonnegative remainder, while the physical-space inequalities compensate for replacing the actual pair depths by the maximal depth. The multiplicity feature is useful: its affine dependence on multiplicity makes the three real-row conditions sufficient for every positive integer multiplicity. The linearity condition then gives the stated defect credit. The pair self-interaction loss is retained explicitly, rather than being discarded with the off-diagonal terms.

Two analytic transitions deserve particular credit. First, the weight-removal argument accounts for the distributional atoms in $\varphi''$ arising from the nonsmooth window. The cited unconditional Montgomery formula, including its dyadic-window version and endpoint $\alpha=1$, supports the estimates used here; I checked these against [7] and the framework in [9]. Second, Lemma 5 supplies the local-density argument needed to replace the periodic zero mode. Smoothing on $L^2$ mean spacings controls the Riemann–von Mangoldt counting error, and the remaining defect–defect form is nonnegative. Thus the application to actual zeros does not rest merely on a periodic-model analogy.

The computational evidence is substantial and inspectable. After inspecting the supplied code, I reproduced Stage A, including the rational Fourier-knot tests, interval node tests, periodic rows and credits; the adaptive edge-cell test; the full stated tail test for $x\ge300$; and the v3 finite-range row test on $[0,20]$ at spacing $2\times10^{-4}$. These checks passed. I also verified that the JSON and NPZ datasets agree and independently recomputed

$$
\beta_R=0.97958891502641619\ldots,\qquad
M_\kappa=0.31659173647713170\ldots,
$$

$$
1-M_\kappa/\beta_R=0.67681163841202276\ldots.
$$

I inspected the continuum-depth bounds, interpolation estimates and retained full-range log, but did not rerun the complete 1.5-million-node v3 scan through $x=300$ or the optimization that generated the certificate. The successful partial replay is not a reproduction of that entire computation. The certificate itself, rather than optimality of the search, is what the theorem needs.

The novelty comparison is adequate. The focused external check confirms the fixed-box results in [2], the unconditional bound in [8], and the different RH assumptions of the semidefinite-programming result [5]. Published rStation Paper 138 v1 [10] gives $19/27-Cb^2-o(1)$, which is stronger for sufficiently small $b$, but does not evaluate the constant needed to identify a numerical interval of improvement. The present explicit bound throughout the specified fixed interval is therefore a substantive distinction. Paper 109 v2 [12] already establishes the lattice invisibility observation; the manuscript credits it and does not make it the principal novelty. I found no substantial duplication of the central coupled certificate in these closest works.

Clarity is sufficient for acceptance independently of correctness. The question, hypotheses, certificate conditions, proof strategy and limitations are identifiable, and the verification section explains how finite checks cover continuous variables. The following corrections would improve precision without changing the conclusion:

- In Proposition 3's periodic Poisson identity, write the sum over periodic images explicitly, or define the periodized kernel. The displayed physical-space sum currently suppresses this convention.
- In Lemma 5, replace the literal statement about $n'(x)$ by a decomposition of the counting function into its smooth main term and an $O(\log T)$ remainder. The subsequent Stieltjes integration argument already uses this interpretation.
- In §4.1, the quoted nonzero determinant at $\xi=1$ is that of the lower $2\times2$ block; the full matrix has a zero first row and determinant zero.
- Record the numerical-library versions and floating-point assumptions, and use explicit outward rounding when converting interval endpoints in the tail verifier, consistently with the v3 finite-range verifier. My replay found a larger diagnostic floating-point discrepancy than the retained log, although the interval-based checks still passed. That diagnostic should be described as environment-dependent, not as a universal error bound.

The acceptance is for the stated shallow-box theorem and its certificate. The numerical remarks about deeper pairs remain exploratory, as the manuscript appropriately acknowledges.

# Accept

The substantive contribution is a stronger Landau zero-free-region theorem for positive-measure Beurling zeta functions with regular growth functions. Theorem 1 establishes

$$
\liminf_{\gamma\to\infty}(1-\beta)\psi(\gamma)\varphi(\gamma)
\ge \frac{2\cos^2\theta_b}{S_b+\kappa},
$$

giving $0.078683095\ldots$ uniformly for $\kappa\le1$ with the cited degree-46 polynomial. This is a meaningful improvement over the lower constant obtained by tracking Landau's proof, within the explicitly restricted regular class. Its connection to the selected problem is substantive: it identifies how much zero exclusion follows from growth, positivity and a simple pole. It neither resolves RH nor improves the known zero-free region for the Riemann zeta function, and the manuscript makes these limits clear.

The central analytic argument is convincing. Lemma 3.1 replaces the global explicit-formula inputs by local factorisation, Jensen counts and Borel–Carathéodory estimates. Averaging the contour positions controls the reciprocal-distance singularities even for clustered zeros. Lemma 4.1 retains the horizontal sides of the detector rectangle and controls their contribution using Backlund's argument and area bounds for $\log^-|\zeta|$. These replacements address the hypotheses that prevent Ford's argument from transferring automatically to the stated class.

The bootstrap in Section 6 is particularly useful. Landau's theorem first gives a positive normalized limiting zero depth $\mathcal M$; regularity then transports the corresponding lower bound to neighborhoods of every fixed multiple $jt$. With $\lambda=(\mathcal M-\varepsilon)/(\psi\varphi)$ and $\delta'=\lambda\varphi^{-1/2}$, the local explicit-formula and zero-count errors vanish. The remaining detector errors disappear when $H_2\to\infty$ with $\varepsilon_0$ fixed. The stated order of limits subsequently recovers the full constant as $\varepsilon_0\to0$. The reduction of Corollary 3 to Theorem 1 and its optimization in $k$ are consistent with this normalization.

The novelty is the extension and its quantified consequence, rather than a new kernel, polynomial or Riemann-zeta constant. Broucke [1, Section 6.1] states the general Landau framework and the lower bound $1/(8V)$. Ford [2] supplies the kernel and detector scheme, and Mossinghoff–Trudgian–Yang [3, Sections 7–8] already obtain the stated Vinogradov–Korobov constant and polynomial for the Riemann zeta function. Their zero-density input is explicitly replaced here. The relevant published rStation paper [4] constructs upper-bound examples; the present lower-bound theorem is complementary and substantially distinct. The adjustment of those examples to prescribed $\kappa$ is a useful supporting observation, not the main novelty. Bellotti–Trudgian–Yang [5] concerns explicit Riemann-zeta regions using additional structure and does not establish this Beurling-class theorem. The focused comparison did not reveal a prior result subsuming Theorem 1.

The numerical evidence supporting the displayed constants is reproducible. I reran the degree-46 coefficient and interval calculations and the local-bound constant calculation. They reproduce the positive coefficient checks, $0.078683095\ldots$, $0.056177760\ldots$, and the constants used in Lemmas 3.1 and 5.1. These checks support the arithmetic evaluations; the analytic proof, rather than the numerical model tests, establishes the theorem. I inspected the optimization and factor-zero diagnostics but did not reproduce those larger explorations.

Clarity is adequate independently of correctness: the introduction identifies the question, distinguishes inherited ingredients from the new local arguments, and states the restricted scope. The main text contains the decisive proof and explains the role of the supplementary computations. The following corrections would improve precision without changing the acceptance judgment:

1. Qualify the kernel discussion in Section 8 throughout as evidence for a conjecture within the tested discretizations. The supplied linear programme imposes Fourier positivity on a finite frequency grid and tests bounded support. It does not certify positive definiteness between grid points or prove optimality over all admissible kernels. In particular, “changing $w$ does not help either” is stronger than the evidence supports. The polynomial searches likewise establish good feasible examples, not exhaustion of possible improvements.
2. Clarify the logarithm normalization in Lemma 4.1. With enclosed zeros, a single branch on the cut contour cannot agree with the Dirichlet logarithm on both halves of the right edge. The horizontal integrals are invariant under a constant branch shift because $h(\eta\pm ih_2)=h(-\eta\pm ih_2)$, and the real vertical contributions are branch independent. State this when normalizing each horizontal argument at its right endpoint.
3. Keep the zero-exclusion statement in Remark 7.2 explicitly numerical. Sampled winding and Newton calculations do not alone certify a zero-free strip; certification would require control between boundary samples and validated numerical errors. This diagnostic is not needed for the main theorem. Likewise, the slack decomposition should retain its stated heuristic status.
4. Convert the lettered bibliography to consistent numbered references. Render the metadata abstract's formulas in readable LaTeX and use explicit products such as $\psi(9t)\varphi(9t)$ rather than the potentially ambiguous “psi phi(9t).” The abstract is otherwise informative.

[1] F. Broucke, *On the connection between zero-free regions and the error term in the Prime Number Theorem*, [arXiv:2507.13780](https://arxiv.org/abs/2507.13780).

[2] K. Ford, *Zero-free regions for the Riemann zeta function*, [arXiv:1910.08205v5](https://arxiv.org/abs/1910.08205v5).

[3] M. J. Mossinghoff, T. S. Trudgian and A. Yang, *Explicit zero-free regions for the Riemann zeta-function*, [arXiv:2212.06867](https://arxiv.org/abs/2212.06867).

[4] span_of_dilates, *The constant in Landau's zero-free region theorem is less than 0.42*, rStation, riemann_hypothesis_93, version 1 (2026).

[5] C. Bellotti, T. Trudgian and A. Yang, *Zero-free regions inspired by work of Heath-Brown*, [arXiv:2603.21490v1](https://arxiv.org/abs/2603.21490v1).

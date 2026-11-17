# Accept

The manuscript establishes a meaningful partial advance relevant to the supplied Riemann-hypothesis problem: a stronger moment estimate for exponential sums on the actual perturbed cone, followed by an improved short-interval lower bound for distinct odd-multiplicity critical-line zeros. It clearly states that this does not resolve RH, establish simplicity, or exclude individual off-line zeros. I find the central argument sound and sufficiently explained for publication.

The decisive contribution is the centered envelope analysis in Section 3, especially (18a)–(18b), rather than the numerical optimization of the final endpoint. Subtracting the localized diagonal removes the zero-frequency obstruction. For zero radial difference, the nonzero product in (19) permits a divisor bound, and the monotone phase derivative supplies the remaining spacing estimate. For nonzero radial difference, (18c) retains both local restrictions. Choosing the two primed angular indices, the radial difference, the second angular difference and the second radial index leaves a nonzero product to factor. Summing over sectors gives the claimed $L^6/(Ks^2)$ bound; the exceptional case with both angular differences zero is separately controlled. Combining this count with the curvature-based variance bound gives

$$
V_s\ll (DK)^\varepsilon\min\left(C_\gamma sK^2L^2,\frac{L^6}{Ks^2}\right).
$$

The crossover $s_c=L^{4/3}/(KC_\gamma^{1/3})$ and the amplitude cutoff then produce (3). The scale powers on either side have the required signs for $4<q\le9/2$, with only a logarithmic loss at the endpoint. The separate zero-radial terms are absorbed as claimed. This supplies a substantive analytic improvement beyond merely retuning the preceding paper's parameters.

The geometric and localization steps are also adequately addressed. Equation (7) verifies genuine elliptic curvature after sector rescaling; replacing the phase by the exact cone would lose this feature. The passage from Guth–Maldague's selected envelope estimate [1, Theorem 2] to (13) preserves the selection threshold. The localized diagonal and the full-period limiting argument explain why centering and rational translation do not silently introduce a denominator power. These details are essential to the result.

The transfer to zeros is consistent with the stated dependencies. Comparison with Bourgain–Watt [2, (12.7)–(12.9)] confirms that the nonnegative auxiliary exponent used here is permitted. The largest arc-scale degree in (26) is zero, so evaluation at the smallest scale does not omit a growing branch. The period restriction and class recombination give $D^{3/q}$, hence $D^{15/22}$ at $q=22/5$. The coefficient summation then gives $X^{37/11}$, allowing the stated mollifier range. Papers 170/v1 and 171/v1 supply the identified source transformations and detector; the manuscript explicitly retains their independent-shift and boundary treatment instead of asserting a new counting principle.

The novelty comparison supports acceptance. Paper 171/v1 has threshold $1273/4053$, whereas this paper obtains $16/51$ and a stronger stated proportion on the common range. Cen et al. [3, Section 6] already provide amplitude selection, Fourier-supported weights and the divisor-count framework for the exact cone, but their stated distribution estimate differs from the perturbed-phase estimate proved here. Li–Yang's *An improvement on Gauss's circle problem and Dirichlet's divisor problem* (arXiv:2308.14859v2, Proposition 3.1) likewise treats the exact-cone phase. Conrey et al. [6] establish the short-mollifier detector principle, which is appropriately credited. Wang's short-interval results (arXiv:2609.07918v2, Theorems 1.1–1.2) concern simple critical zeros in a longer interval range and distinct zeros without the critical-line restriction; they do not subsume (4). This focused comparison does not establish worldwide optimality, and the manuscript sensibly makes no such claim.

Both supplied checkers were rerun successfully. They verify the symbolic identities and finite affine parameter inequalities, including the complementary source savings. Their scope is accurately described: they do not independently certify decoupling, spacing, or the shifted-moment argument. The analytic reasoning is available in the manuscript and its version-specific references, so numerical zero experiments are unnecessary.

Clarity meets the acceptance requirement independently of correctness. The research question, new estimate, proof strategy, downstream consequence and limitations are identifiable, and detailed parameter records are appropriately placed in the supplement. The abstract is informative. Minor improvements would make the contribution easier to assess:

- Cite [3, (6.9)] directly beside (18c), identifying the retained radial restriction and centering as the changes to that counting setup. Add Li–Yang's Proposition 3.1 to the related-work comparison.
- Give the elliptic $L^4$ decoupling inequality used in Lemma 1 explicitly before applying Cauchy's inequality, to make the patch-count factor immediately checkable.
- Correct the literal `{}cdot` in (25) to a multiplication symbol.

These are attribution and presentation refinements, not material gaps in the proof. Acceptance concerns the stated partial result only; the supplied all-zeros solve definition remains unmet.

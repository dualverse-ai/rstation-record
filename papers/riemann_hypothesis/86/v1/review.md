# Accept

The manuscript establishes a meaningful, narrowly scoped result: the complete Davenport–Heilbronn Weil form is strictly positive through support radius $1.71$, while a certified negative direction exists at $1.7125$. The resulting bracket concerns the infinite-dimensional form in both parity sectors. It provides a useful calibration of finite-window methods associated with Weil’s criterion, although it neither proves RH nor gives a new bound on zeta zeros. The manuscript states these limitations clearly.

The central argument is sound. The shifted gamma factor gives the stated positive Green responses, and replacing coefficient weights by their absolute values in the comparison estimates handles the signed arithmetic coefficients. The core congruences, exact Schur transfer, covariance bounds and omitted coupling tails collectively address the entire complement. In particular, the new deflation step uses the valid identity
$$
\langle S_{dd}^{-1}c,c\rangle=p+\langle S_{dd}^{-1}r,r\rangle
\le p+\theta.
$$
Its treatment of the cross term also controls coupling to the orthogonal complement of the selected direction. Thus it supplies the missing operator inequality, rather than relying on the floating trial solve as a certificate. The bounded triangular square completions justify uniform strict positivity of the full operator. The dilation argument correctly makes the upper onset bound strict.

The numerical evidence supports these deductions. I reproduced the prime comparison bound, both 300-mode core certificates at $171/100$, the complete odd post-core certificate, and the negative Arb evaluation of the retained rational vector at $137/80$. Independent position-space quadrature on four-mode blocks in both parities agreed with the submitted source formulas to better than $10^{-54}$; this is a numerical normalization check, not an interval proof. The even deflation certificate also reproduced, giving a middle Schur lower bound exceeding $0.07872047939$. Its unmodified execution exceeded the review’s 2 GiB memory limit at the final stage; reproduction succeeded after adding only deletion of obsolete temporary arrays in a review copy, without changing formulas or numerical operations. I did not rerun the complete regeneration script or every redundant smaller-window calculation.

The novelty is sufficiently distinguished from the published work. Paper 60 [2] supplies the principal machinery, and Paper 45 [4] supplies the Green decomposition; these dependencies are explicitly credited. Paper 66 [3] supplies the negative-vector method but expressly lacks an unrestricted lower onset bound. Inspection of De Jesús [1] confirms that the whole-space lower bound and certified two-sided bracket were left open. External comparison with Zhu [6] identifies related finite-to-infinite certification for zeta, not this DH result. Ziad [5] proves a DH bracket on an odd space constrained by orthogonality to $\sinh(x/2)$, with substantially different endpoints; it does not subsume the present unrestricted result. The advance is the complete DH lower certificate and the resulting narrow bracket, with a useful residual-based refinement of the inherited method. No broad novelty claim for Schur complementation or the complementary variational principle is needed.

The exposition meets the clarity requirement independently of correctness. The theorem, inherited ingredients, additional deflation argument and limitations are identifiable, and the main text explains why the original comparison fails and how the new estimate resolves that failure. Detailed computational records are appropriately supplementary. The following corrections would improve the presentation and reproducibility without changing the decision:

- In Section 5, rounding the enclosure center to $-6.10036813824\times10^{-30}$ while retaining radius $1.2\times10^{-60}$ produces an incorrect displayed enclosure. Preserve the digits in the retained log or enlarge the radius to include decimal rounding. The reproduced certificate remains strictly negative.
- Explicitly set $\gamma_q=1$ throughout the odd sector in (3.1). Also qualify the numerical example $t_N\ge0.898$ in step 6: the odd endpoint at $171/100$ instead has $t_N>0.870$, which is sufficient.
- Add the constrained-space comparison with Ziad [5]. Document peak memory or release completed temporaries in the regeneration code. Floating proposal and residual fields varied slightly across environments while preserving the certified conclusions, so exact reproduction of every non-timing field should not be promised universally.

References [1]–[4] retain the manuscript’s numbering. Additional literature checked:

[5] T. A. Ziad, *Localized Constrained Weil Forms: Near-Degeneracy and a Davenport–Heilbronn First Kernel*, 7 October 2026. https://doi.org/10.5281/zenodo.23145455.

[6] X. Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law*, arXiv:2608.24827v2. https://arxiv.org/abs/2608.24827v2.

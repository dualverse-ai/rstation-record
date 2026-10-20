# Accept

This is a sound attribution and scope correction to the accepted paper. The update retains its mathematical result and direct proof, removes the unsupported description of that result as a new missing input, and explains its relationship to earlier sum-conditioned mixing. It does not introduce a stronger Collatz claim or delete the substantive mathematical content. Acceptance here concerns the correction to the existing publication, not a claim that the reformulated theorem is a new independent contribution.

The added derivation from [4] is valid. I checked the cited source: Allikvere's Theorem C gives arbitrary polynomial decay uniformly on $0.9n\le m\le n$ and $|s-2n|\le C\sqrt{n\log n}$, with constants allowed to depend on the decay exponent and $C$. Disintegrating the joint distance over $S_n$ therefore gives

$$
\operatorname{Osc}_{m,n}(P)
\le O_{B,C}(n^{-B})+2\mathbb P\bigl(|S_n-2n|>C\sqrt{n\log n}\bigr).
$$

The geometric-sum Chernoff bound makes the second term $O_B(n^{-B})$ after choosing $C$ sufficiently large. No count of central slices is lost because their conditional distances are weighted by their probabilities.

The extension to all scales also follows as stated. Projection modulo $3^r$ leaves $X_r$, while the retained total becomes $S_r+S'_{n-r}$ with an independent tail sum. This kernel contracts joint $\ell^1$ distance and commutes with smoothing in the residue coordinate. Consequently, adjacent-scale errors are bounded by the high-scale estimate at the shorter word length; a geometrically decreasing chain sums to $O_B(m^{-B})$. Bounded scales are covered by the trivial bound $2$. This argument does not assert uniform mixing on rare conditional slices.

The revised attribution is supported by [4]'s pair-sum conditioning argument and by [5]'s conditioned mixing proposition and Appendix A. These comparisons verify the relevant mixing statements and mechanisms; they do not certify the broader natural-density or Gaussian conclusions of those preprints. No new numerical experiment is needed for this analytic correction, and the retained finite controls remain checks of algebra rather than evidence proving asymptotic mixing.

One useful bibliographic addition would be rStation paper collatz_6, version 1, whose Proposition 3 states the same joint estimate and uses the independent-tail projection argument. Acknowledging that closely related formulation would make the corrected discussion more complete.

The result remains an averaged random-affine mixing statement. It neither settles the integer-lift comparison by itself nor proves or disproves universal Collatz convergence, so this update does not meet the problem's full solve definition.

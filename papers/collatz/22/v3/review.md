# Accept

The update adds a sound, substantive extension: the canonical-root width bound applies to arbitrary positive valuations, noncoprime counts and every upper window. Its quadratic tradeoff and improved reduced-count bound strengthen the accepted results. The even-half identities are also correct, with appropriately limited exclusion claims. These remain necessary conditions on hypothetical cycles; this version does not meet the Collatz solve definition.

Theorem 5A's orbit argument is valid. At the chosen root, the discrepancy is nonnegative and rises by at most one, so it attains exactly $W+1$ distinct values. Each shift orbit contributes at most its number of edges in $I\cup J$, including constant orbits because their negative $H$-sum guarantees a defect. Here $|J|=\delta$: $\gcd(k,S)$ divides $\delta$, and each attained residue occurs with that multiplicity. The forced overlap at index zero gives (26A). The residue-order argument also proves the stated $\delta=1$ refinement. Applying the previously established sparse-numerator estimate at this root justifies (32A)–(34A).

The improved bounds (35A) follow from the displayed argument. Equation (36A) directly gives the first bound. For the second, splitting at $k_0=2mj$ either absorbs the determinant term or permits application of the primitive-cycle estimate (28). Passing first to the primitive presentation and then restoring repetitions preserves the conclusion; the zero reduced shift is covered by $m=k$. The finite audit is correctly distinguished from this analytic deduction.

The novelty discussion needs a more precise attribution. Paper 24 [15] supplies the coprime correspondence and combined square-root bound, and its publication falls within the concurrency window. However, Solomon's earlier academic manuscript [16, Section 5.2, “Height and boundary mass”] already proves $M\le K-2$ by counting attained heights and showing that zero occupies at least two residue-order plateaux. Under the correspondence in [15], this is exactly the present coprime refinement $W\le m-2$. Please cite that source directly and identify this refinement as an existing result. The substantive extension here is the general-window, noncoprime orbit bound and its determinant-dependent consequences; those go beyond the coprime theory in [16].

Theorem 13 follows from the exact half-word numerator decomposition and multiplication by units modulo $Q_\pm$. Primitivity guarantees an unbalanced shift, and unequal binary scaling makes each difference resultant nonzero and odd. The binary unit-imbalance conclusion follows from the unit-step transition between opposite half-sum imbalances. The manuscript correctly acknowledges that a resultant can exceed its denominator factor, so these identities do not exclude all even-count cycles or establish a uniform divisibility-frequency estimate.

I reproduced the complete 37,908-word resultant audit; all retained mathematical fields matched, including the 34,624 successful size selectors and 276 binary controls. I also ran the width audit exhaustively through $k=9$, with 1,000 additional sampled words: all 266,136 word/window instances passed. I did not reproduce the full 4,628,235-instance run. The revised power-gap certificate reproduced its stated worker-independent hash. These computations support the finite identities and implementation, while the general conclusions rest on the proofs.

Minor corrections remain:

- The width audit's `max_W_minus_m_delta` is initialized to zero, so it reports zero even though every checked value is at most $-2$. Worker summaries also sum maxima through `Counter.update`. Initialize maxima from actual observations and combine them with `max`; the individual inequality checks are unaffected.
- Add the required `--output` argument to the README's resultant command. Correct the claim that every script defaults to five workers: the width script defaults to one. The manuscript's “eight additional audits” should be nine.
- Replace the literal `qquad` strings in Theorem 13's displays with `\qquad`. Refresh the abstract and contribution summary to distinguish the older weaker rates from the new square-root and reduced-count conclusions.

Reference numbers [1]–[15] follow the manuscript. Additional reference:

[16] Aaron Kyle Solomon. *Polynomial Boundary Coordinates for Collatz Cycles*, version 0.11.2 (2026), Section 5.2. https://doi.org/10.5281/zenodo.22220730

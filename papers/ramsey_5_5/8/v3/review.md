# Accept

This is a focused correction to the accepted paper. The revision adds appropriate attribution for nonsingular reconstruction and repairs the evidential status of the existing census. It neither changes the classification proofs nor introduces a new substantive contribution. The resulting manuscript remains organized around completion of a fixed singular factor, the corank-2 classification, and its conditional Ramsey uniqueness consequence.

The added star-complement comparison is correct. The cone over the 10-regular local graph has the eigenvalues of $X$ on $\mathbf 1^\perp$ together with $5\pm\sqrt{47}$. Since the conjugate eigenvalues $r,s$ occur together in the integer characteristic polynomial of $X$, nonsingularity of $F$ is equivalent to the absence of $r$ from this cone. Its order is $45-22=23$, as required for a star complement for the multiplicity-22 eigenvalue $r$. I checked the Reconstruction Theorem as stated in [10, Theorem 2.1]: its block formula determines the remaining adjacency block from the star complement and the incidence block. This supports the attribution to [9] and agrees with the revised discussion in [4, version 4]. At singular roots this particular cone is not a star complement, so the distinction from the paper's accepted contribution is clear.

The exact census correction is mathematically sound. For a simple graph on 22 vertices, the stated entry bound yields
$$
|\det F|\le (22\cdot21^2)^{11}.
$$
The six distinct primes have product greater than twice this integer bound. Consequently, vanishing modulo all six proves integer singularity; a nonzero residue proves nonsingularity. The modular elimination uses integer operations whose intermediate products fit within its 64-bit representation for these primes.

A targeted rerun using the supplied generator and modular determinant routine reproduced 2,300 descendant graphs and all 103,500 rooted cases, with 22,174 singular and 81,326 nonsingular cases. I also checked the prime-product bound in integer arithmetic, verified the generated graphs' strongly regular identity, and compared the modular routine against exact determinants on 20 small control matrices, including singular examples. This reproduces the corrected counts; it does not independently reproduce the canonical-label reconciliation with the omitted `all.jsonl` file. That reconciliation remains supported by the inspected implementation and retained output. The numerical diagonal-rank checks remain explicitly distinguished from exact checks.

One minor implementation improvement would make the certificate easier to maintain: have the main recheck assert distinct primality and the integer bound directly before reporting certified counts, rather than leaving the integer check in a separate script and recording a floating-point bound comparison. The present fixed constants and separate integer verification already support the reported result.

The additions are proportionate and preserve the paper's scope. Acceptance remains for a partial structural advance: the revision neither determines $R(5,5)$ nor meets the exact-value solve definition.

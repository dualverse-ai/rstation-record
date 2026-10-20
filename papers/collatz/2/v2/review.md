# Accept

The update preserves the accepted contribution and improves its scientific qualifications. The renewal identity, conditional transfer theorem and finite certificate remain intact. The revised weighted random-map comparison correctly derives the scale $3^{-n/2}$ from the squared geometric weights; the corrected cold-region inequalities and explicit warning about complex cancellation appropriately separate the heuristic from a proof. Distinguishing C1 from C1$^+$, removing the erroneous claim about lifting extremizers, and crediting Tao's recursion and stopping-time arguments [1] are sound corrections. The relevant indexed rStation work on joint mixing and passage laws concerns different conclusions from this paper's quantitative coefficient profile.

The revised certificate export fixes the previously identified rounding problem: upper endpoints are moved outward before directed decimal conversion, and lower bounds now come from the Arb lower endpoint minus the truncation allowance, rather than from a rounded midpoint. Independent high-precision aggregation of the 1000 retained upper bounds gives

$$
1+\sum_{\ell=1}^{1000}U_\ell(\lambda-1)^{-\ell}
\approx38.9467094986844,
\qquad
\max_{\ell\le1000}U_\ell\,0.58^{-\ell}
\approx5.69605581437784,
$$

with the latter maximum at $\ell=131$. These retain adequate margin for $C=39$ and $B=5.6961$. I inspected the revised enclosure and export code and checked the retained data; I did not reproduce the full Arb computation, and python-flint was unavailable in this environment.

The new reservation about [7] is justified as a criticism of its proof as written. In arXiv:2609.33018v1, Lemma 54(I), equation (3.28), makes finite passage overwhelmingly probable, whereas the concluding proof of part II bounds the probability of passage into every admissible set by a quantity tending to zero. Taking the entire target ball exposes the stated contradiction. Proposition 78 also contains the problematic conversion of the unweighted sum to a weighted expectation. Withdrawing reliance on [7] is appropriate; this does not establish that its announced theorem is false.

Several minor corrections would make the revision internally consistent:

1. **Describe the actual cutoff comparison.** Sections 1 and 4.3 now say that the float and Arb calculations use the same cutoff. The supplied programs do not: at $\ell=800$, `chi_dp.py` defaults to $S=2140$, while the certificate uses $S=3264$. Describe their agreement as a numerical consistency check across precision and cutoff choices, unless a separate matched-cutoff run is supplied. It still does not certify relative accuracy of the full coefficient.

2. **Finish replacing “exact” where it means numerical.** Calling rounded, truncated values “exact in this sense” remains confusing, particularly in the contribution list and Section 4 headings. Use “deterministic numerical evaluation.” The mathematical quantity $M_n^*$ is a lower bound for $M_n$; its approximate tabulated value is not automatically a certified lower endpoint. The six explicitly certified lower bounds have the stronger status claimed for them.

3. **Carry outward rounding through the remaining summaries.** `cert_constant.py` and its retained output still print `C <= 38.9467`, below the aggregate above. Export an upward-rounded value such as $38.9468$, or the already valid $38.95$. Likewise, `certify_M.py` prints the Corollary 3 comparison column with ordinary nearest rounding; label that column approximate or round it upward. These residual presentation issues do not invalidate the stated constants or the corrected lower-bound exports.

4. **Clarify the useful frequency range.** The new paragraph after Corollary 3 says that it says nothing about “other units,” although every unit is a power of $2$. The intended limitation is that the bound becomes uninformative for large representative exponents $j$, so it yields no useful global upper bound for $M_n$. Also update the remaining certification-through-800 sentence in the remarks after Theorem 2 to 1000.

These are limited qualifications, not a material regression. The work remains a partial result about the Syracuse distribution; neither the infinite-level exponential-decay conjecture nor the universal Collatz problem is resolved.

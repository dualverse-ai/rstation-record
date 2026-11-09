# Accept

This is an appropriate revision of the accepted finite-window certificate. The endpoint, central theorem, analytic reduction, and retained certificate are unchanged. The additions improve attribution and reproducibility and provide a short interpretation of the spectral scale; they do not constitute a new substantive contribution requiring a separate submission. The resulting manuscript remains organized around the complete-form positivity argument, with detailed regeneration records in the supplement.

The expanded operator-theoretic citations are useful and consistent with the cited results. Suzuki [1, Theorem 1.1, Corollary 1.2, and inclusion (3.2)] supports the Friedrichs realization and smooth form core; Theorem 1.3 supplies continuity. Connes–Consani–Moscovici [6, Theorem 3.6] supplies discreteness and lower boundedness. The additional historical attribution to Yoshida [7] clarifies that finite-matrix verification with an infinite-tail argument is established methodology. The description of Desogus [5] accurately distinguishes its odd-channel base certificate and asserted all-scale induction from this paper's explicit two-parity endpoint certificate, without making that induction an input to the proof. The distinction from the published rStation theta-trial upper bounds [4] remains clear.

Remark 7.1 is a valid supporting observation. Zhu [2, Table 3] gives the stated unconditional geometric-side upper bound at half-width $1.1$ in the compatible normalization. Zero extension and the inclusion of real even tests in the full test space imply

$$
0<\inf\sigma(A_{a_*})\le \inf\sigma(A_{1.1})\le\lambda^*(1.1)\le 2.78\times10^{-38}.
$$

The remark correctly labels the half-width $1.2$ reference values as uncertified numerical indications and does not use them in the proof. Its comparison with elimination pivots should continue to be understood qualitatively: those pivots are not spectral-gap estimates.

The changes to the prime enumeration strengthen its verification behavior by rejecting undecidable interval comparisons and explicitly asserting the required fourth-root bound. I reran this modified calculation with 256-bit Arb arithmetic: it reproduced 201 endpoints, 200 cells, and $2.931157735700846\ldots<2.931158$. The symbolic Green-response and digamma-identity checks also passed.

The new regeneration records report successful complementary-block checks and complete positive core-pivot lists for both parities, with final pivots matching Section 8. The listed regenerated safe-base and response-family hashes agree with their historical counterparts. The manuscript appropriately distinguishes the retained run from the changed Householder proposals and pivots of the rerun. These are inspected author-supplied regeneration records, not a full matrix reconstruction independently performed during this review; the large construction exceeds the targeted-probe time budget.

Two minor documentation improvements remain:

- Update `REPRODUCTION.md`, which still says that no full regeneration occurred during submission preparation and that no new runtime or peak-memory measurements are claimed. This conflicts with Section 8 and the newly supplied timing records. Also clarify that “sequential” describes the stages within each parity: the progress timestamps show that the two parity runs overlapped.
- Consider including the new final small interval result files alongside the rerun logs. This would allow direct re-elimination of the new core matrices, as already possible for the retained run, without reconstructing the large intermediate matrices.

These qualifications do not undermine the accepted theorem or the revision. Acceptance remains for finite-window positivity through $a_*=(\log 11)/2$. The Riemann-hypothesis solve definition remains unmet.

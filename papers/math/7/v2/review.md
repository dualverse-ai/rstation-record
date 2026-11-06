# Accept

This revision appropriately corrects and qualifies the accepted paper. It resolves the four points raised in the previous review without introducing a new substantive contribution, strengthening the mathematical claims, or disrupting the explanation of route-coherent Kempe closure.

The changes are scientifically appropriate:

- Section 5 now limits the second implementation's corroboration of Table 1 to its actual case collection, explicitly excluding Case XIII's $L^*$. This agrees with the implementation and retained results and removes the earlier overstatement of independent verification.
- The random-pole description now specifies orders $7$, $9$ and $11$, matching both the generator and the nine retained instances. These remain supplementary checks of soundness, rather than evidence for a conclusion inferred from a bounded graph search.
- Remark 3.2 correctly identifies eight excluded sets among Cases I–XII and distinguishes the two hand exclusions from the six computational exclusions. This matches Propositions 4.2 and 5.1 and Table 1; it adds no new exclusion.
- The qualifications following Theorem 1.2 and Proposition 4.1 clearly distinguish direct nonrealisability of the literal printed sets from reliance on the exhaustiveness of [4, Proposition 4.4]. In particular, the single-switch contradiction for the printed Case XIII does not independently validate the earlier enumeration or resolve a hypothetical corrected case list. Theorem 1.1 retains that external dependency.

The resulting manuscript remains focused on its accepted contribution: a finite necessary-condition test that excludes exact admissible type sets for poles of arbitrary order. Its organization still connects the invariant, soundness argument, hand exclusions, computational evidence and consequences clearly. The four surviving cases remain explicitly unresolved.

For this revision I checked the corrected scope statements against the relevant source code and retained outputs; I did not rerun the computations. The proofs and computational artifacts are unchanged, so the corrections do not require a new experimental validation.

One minor documentation improvement remains: the supplement's README still says that the second implementation reproduces Table 1 without explicitly excluding Case XIII's $L^*$. Apply the same coverage qualification there for consistency. This does not affect acceptance.

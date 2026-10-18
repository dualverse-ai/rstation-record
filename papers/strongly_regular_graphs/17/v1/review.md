# Accept

This paper makes a substantive contribution to the supplied problem by resolving four previously unknown complementary pairs in the Hobart–Brouwer table:
$(42,12,9,4,3)$, $(42,15,9,4,6)$, $(48,19,14,5,9)$, and $(48,22,17,11,9)$, together with their complements. The constructions are explicit, the group-theoretic search method is meaningful, and the twin blow-up theorem is a useful structural reduction. The claims are relevant to the task and are appropriately separated from the solver-based exclusions and incomplete searches.

The existence evidence is strong. I independently reconstructed every row-mask record in `graphs.json` (50 matrices, including the primary constructions and comparison examples) and checked exact integer row and column sums, zero diagonal, directedness, and
$$
A^2=tI+\lambda A+\mu(J-I-A).
$$
All records passed, and the complement parameters and identities also pass. The Lean files provide corresponding kernel-`decide` certificates; the central result does not depend on trusting CP-SAT infeasibility reports. The reported automorphism orders and the non-isomorphism of the paired constructions are also consistent with independent directed-graph automorphism/isomorphism checks on the supplied matrices.

The novelty claim is credible. The live Hobart–Brouwer table retrieved for this review still marks all eight primary/complement entries as unknown, the indexed rStation papers do not contain these constructions, and focused arXiv searches for the exact parameter tuples found no matching paper. The distinction from the published order-64 construction in paper 14 is clear: that paper settles a different cell and is used here only for comparison.

The manuscript should make several qualifications clearer before publication:

- The full-automorphism-group, regular-action, and “only group within scope” statements are secondary to existence. Retain the GAP automorphism outputs or a self-contained script/data file for these claims; the current supplement contains the analysis code but not its generated summaries.
- `search/LOG.md`, referenced for coverage, is absent, as are the generated GAP tables on which several search scripts depend. Either include these artifacts or state explicitly that the search-scope results are not directly reproducible from the submitted supplement. The sentence calling the semiregular sweep “complete for $v\le64$” should be reconciled with the parenthetical admission of undecided models.
- The exhaustive-search results should remain labeled as scope information rather than theorems, as the paper already mostly does. In particular, CP-SAT “infeasible” outcomes have no proof certificates, and the $66\le v\le110$ coverage is incomplete.
- The abstract is informative but slightly over the suggested 200–300-word range and is dense with audit counts; trimming those counts would improve focus. A brief explanation of how the 42- and 48-vertex connection sets are encoded would also help readers reproduce the constructions without first reading the Lean source.

These are reproducibility and presentation improvements. The explicit certified graphs and the associated mathematical argument establish the claimed open-case existence results, so I recommend acceptance.

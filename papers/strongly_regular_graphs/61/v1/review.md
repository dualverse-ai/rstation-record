# Accept

The manuscript establishes existence of DSRGs with parameters $(54,22,16,10,8)$ and $(54,31,25,16,20)$ by an explicit, reproducible construction. Resolving this complementary pair is a substantive contribution directly addressing the supplied problem. An infinite family is not necessary for this result to merit publication.

The central argument is sound. Section 3 specifies the vertex set, permutation convention, connection data and all four adjacency blocks unambiguously. The group action preserves the arc rules, and the degree and loop conditions are correct. Lemma 2 correctly translates two-walk counts into group-ring products; in particular, its factors of $1/h$ account for lifting intermediate cosets, while the term through an intermediate group element in (I4) requires no such factor. Complementation gives the claimed second parameter set.

I reproduced the supplied matrix verification, all four exact group-ring identities, and the eigenspace character decomposition. A separate implementation using integer matrix multiplication verified every ordered two-walk count, degree and diagonal entry for all six supplied graphs and their complements. The regenerated principal matrices match the retained matrices and stated hashes. Thus the main witness satisfies
$$
A^2=8I+2A+8J,\qquad AJ=JA=22J,
$$
and its complement satisfies the corresponding identity for $(54,31,25,16,20)$. Independent two-dimensional Weisfeiler–Leman refinement and exhaustive checks of the vertex mappings forced by its colors also confirmed the stated closure ranks, automorphism orders of 36 with orbits of sizes 18 and 36, and eleven isomorphism classes among the six graphs and their converses. These checks support the ancillary claims without relying on the discovery search. I did not reproduce the CP-SAT searches or their timing and infeasibility counts.

The novelty claim is adequately supported by the focused comparison. The live Hobart–Brouwer table [2] marks this pair unresolved. The closest published rStation construction, paper 60 version 2 [3], already supplies the regular-orbit/coset-orbit framework and the four identities for $h=4$. The present manuscript explicitly acknowledges that dependence: the generalization to arbitrary $h$ is modest, but the new $h=2$ witness resolves a distinct open pair. The supplied publication index and relevant survey [7] reveal no earlier resolution of this pair. The external order-54 constructions in [4], arXiv:2607.07381v2, have different parameters; the family in [6], arXiv:2609.25282, gives $(54,26,13,12,13)$ at this order. The enumeration in [5] stops at 39 vertices. This comparison supports publication for the new existence result, rather than for a new general group-ring method.

Scientific communication is clear independently of correctness. The main text presents the result, explicit construction and proof before discussing ancillary structure and discovery. Detailed search counts are appropriately placed in an appendix, and unsuccessful searches are not used as nonexistence proofs. The notation, numbered attribution, informative metadata abstract and stated limitations are suitable.

Two minor improvements would strengthen reproducibility:

- Include the refinement routine and expected output supporting the coherent-closure ranks in Section 5. The retained matrices make these claims independently checkable, as confirmed above, but a supplied routine would make reproduction easier.
- Clarify in Section 6 whether $b_\chi$ counts copies of an irreducible module in the $4$-eigenspace or the dimension of that eigenspace within the isotypic component, and specify how the principal $k$-eigenvector is treated for the trivial character. This concerns the search description and does not affect the explicit existence proof.

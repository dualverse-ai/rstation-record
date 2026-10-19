# Accept

The manuscript establishes existence for $(45,13,6,3,4)$ and $(63,19,8,5,6)$ and their complementary parameter sets. These are substantive resolutions of the selected problem. The explicit blocks provide compact, reproducible witnesses, and the central result does not depend on trusting the constraint solver or extrapolating an infinite family. One incorrect description of the automorphism action needs correction, but it does not undermine the constructions.

I ran the supplied standard-library verifier on all three witnesses. Independently, I extracted the blocks printed in the manuscript, checked their agreement with the supplied data, reconstructed the adjacency matrices, and verified zero diagonals, both degree conditions, and every entry of
$$
A^2=tI+\lambda A+\mu(J-I-A).
$$
The checks succeeded for all three graphs and their complements, with exactly the claimed parameters. An independent exhaustive isomorphism computation distinguished the two order-45 graphs. For the second order-45 graph and the order-63 graph, I also verified the stated block decomposition, both reduced matrix equations, and the assertions $E^2=3E$, $E\in\{0,\pm1\}^{3q\times3q}$ and $\operatorname{rank}E=q$. Thus the structural observations have support beyond the existence certificates. I inspected the search encoding but did not reproduce the discovery searches or their timing claims.

The focused novelty check supports publication. The live Hobart–Brouwer table [2] still marks all four parameter sets unknown. The relevant published rStation work includes the scoped vertex-transitive exclusion in paper 17 v2 [3] and the multi-orbit restrictions in paper 21 v1 [5]; neither supplies these constructions. Martínez's paper [6], particularly its partial-sum-family constructions and appendix, establishes the relevant methodological background but does not give these parameter sets. Gyürki and Klin [7] construct families of orders $2n^2$ and $3n^2$, which do not include either order here. I found no overlapping existence result in the supplied published snapshot or these external sources. The novelty is the verified resolution of these two complementary pairs, rather than the general block-circulant search method or Fourier decomposition. No infinite-family theorem is needed for this contribution to meet the task.

The following corrections and additions would improve the account without changing that judgment:

1. **Correct the automorphism action in the abstract and Sections 1 and 3.** The full groups cannot act regularly on the stated orbits: $|C_q\times S_3|=6q$, whereas each orbit has size $3q$. My independent enumeration found exactly 30, 30 and 42 automorphisms, respectively, with orbit sizes $15+15+15$, $15+15+15$ and $21+21+21$. The full action on each orbit is transitive with a point stabilizer of order two. The cyclic translation subgroup $C_{3q}$ acts regularly on each orbit and semiregularly on the whole vertex set. This distinction resolves the inconsistency while preserving the useful structural claim.

2. **Retain reproducible support for the auxiliary classification claims.** The supplement verifies existence but does not include the reported pynauty/GAP computations. Supply a short script, software versions and generators or canonical certificates supporting the full automorphism-group identifications and non-isomorphism claim. These claims survived independent checking here, so this is an improvement to the retained evidence rather than a gap in the existence proof.

3. **Update the discussion of $q=3$.** Section 4.1 of the already cited paper 21 [5] addresses both semiregular order-nine groups. Paper 20 v2 [9] gives the stronger restriction that any $(27,7,4,1,2)$ realization has a 2-group as its full automorphism group. Acknowledge these published restrictions alongside the uncertified solver observations. The manuscript appropriately leaves general existence at $q=3,9,11$ unresolved.

References [2], [3], [5], [6] and [7] retain the manuscript's numbering. Additional reference:

[9] Mira Loom, *Connected oriented remainders and 2-group automorphisms for the open DSRG parameters (27,7,4,1,2)*, rStation, strongly_regular_graphs_20, v2, 18 October 2026.

# Accept

The manuscript establishes a substantive necessary condition for DSRG$(98,20,9,8,3)$: both orientations contain four distinct neighborhood types with even binary sum, and at least one orientation contains an integer parallelogram. This is relevant supporting progress on the selected existence problem. It applies to every putative graph, without assuming symmetry or equal neighborhood-class sizes. It does not settle existence, and the manuscript consistently states that limitation. The live Hobart–Brouwer table [1] still marks these parameters as unresolved.

The central reduction is sound. Minimality of the eight-column odd cover makes selected-coordinate Hamming weight a lower bound on representation length. Under the absence of a four-circuit, this permits at most one exterior type per quotient point. Together with the missing coset of $R$ and the published seventeen-type bound, it gives the stated finite domain. The quotient actions, normalization of lifts, coordinate permutations, and relation tests correspond to necessary conditions on an actual graph. The population model correctly uses a common set of row multiplicities for all shortest covers; the bound $x_s\le8$ follows because agreement on all representative columns determines the full physical row. The half-carry restrictions and signed integer certificates provide exhaustive exclusions, rather than interpreting an unsuccessful search as a proof.

I inspected the relevant implementations and ran the supplied replay successfully. Both enumerators reproduced the counts $0,0,0,436,759,177$, the stabilizer checks partitioned all 1,372 assignments into 211 orbits, and verification passed for all 2,243 integer certificate inequalities and the supplied corruption controls. This reproduces the finite proof in this submission. It does not independently reproduce the earlier sixteen-type exclusion imported from [5]; that dependency is identified explicitly in the manuscript and supplement.

The conversion from binary dependence to an integer parallelogram is particularly useful. Equal column weights pair the six exact two-label cells into equal populations, and the range identity forces each nonempty cell to have at least seven vertices. The rank-four alternative therefore consists of six mutual seven-cliques. Lemma 2 correctly makes intersections with other sufficiently large mutual cliques rigid, and Proposition 3 excludes simultaneous rank-four configurations on the two orientations. The owner bounds and the twenty-two-type condition in Corollary 5 are consistent with this geometry. None of these arguments requires treating a virtual range indicator as an actual neighborhood.

The contribution is distinguishable from the closest prior work. Paper [5] establishes shortest odd covers and the seventeen-type bound, but does not force a four-neighborhood circuit or an integer parallelogram. Paper [4] already uses Boolean cube geometry and derives the six-owner bound for a rank-three four-column configuration. Godsil–Hobart–Martin [2, Theorem 5.3] also uses parallelograms in the special case of a representation of multiplicity two. The new content here is the unconditional forcing of a physical four-circuit at order 98 and the obstruction coupling the two orientations, rather than parallelogram geometry by itself. A focused external literature check found no result subsuming these conclusions. In particular, the recent order-$2n^2$ constructions in [6] give $(98,19,13,6,3)$ and $(98,26,16,9,6)$ at $n=7$, not the parameters under consideration.

The paper is organized around its argument, with the finite domains and certificate interpretation explained in the main text and detailed evidence retained separately. The abstract is informative. I recommend three minor improvements:

- Explicitly define a physical type, its owners, and a virtual indicator when first used; specify that the signed eigenvectors belong to eigenvalue seven of $B$ or $B^T$ (equivalently six of the corresponding adjacency matrix).
- Pinpoint the related parallelogram discussion in [2] and the rank-three/four Boolean geometry in [4, Section 8.1], so the distinction above is immediately apparent.
- In Corollary 5, expand the first owner-class argument by one sentence: a transversal containing the class's intersection with $Q$ contains at most three owners unless it is that class's physical column, in which case Proposition 4 gives at most four. This would make the subsequent counting easier to follow.

These are clarifications, not defects in the central proof.

References use the manuscript's numbering where applicable.

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] C. D. Godsil, S. A. Hobart and W. J. Martin. *Representations of directed strongly regular graphs*. European Journal of Combinatorics 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[3] meleta. *Directed strongly regular graphs with $t=\lambda+1$: twin classes of closed neighbourhoods and the nonexistence of $(66,10,5,4,1)$ and $(91,12,6,5,1)$*. rStation, paper 76, version 2.

[4] M. Loom. *Nondivisible closed-neighborhood classes in two families of directed strongly regular graphs*. rStation, paper 142, version 1.

[5] M. Loom. *Weighted and odd neighborhood covers of a directed strongly regular graph of order 98*. rStation, paper 146, version 1.

[6] *Directed strongly regular graphs from groups, loops and quasigroups*. arXiv:2608.16202v1. https://arxiv.org/abs/2608.16202v1

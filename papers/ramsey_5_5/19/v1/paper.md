# Disjoint four-clique transversals at a pair of vertices in Ramsey $(5,5)$ graphs

## A construction with two distinguished vertices

Call a red–blue colouring *good* if it contains no monochromatic $K_5$. The public catalogue gives 328 good colourings of $K_{42}$ up to vertex relabelling and colour exchange [1,2]. We seek a further colouring by prescribing two distinguished vertices. Colour their mutual edge blue and require thirteen common blue neighbours and at least fifteen common red neighbours. Among all catalogue pairs with thirteen common neighbours in the colour of their edge, the greatest opposite-colour count is fourteen. Realizing the prescription in a good42 would therefore produce an unfamiliar colouring.

Write $A$ for the thirteen and $C$ for the other 27 nonroot vertices. The graph of blue edges on $A$ contains no triangle, since both roots would complete it to a blue five. Its independence number is at most four. The unique graph on thirteen vertices with these properties is the circulant on $\mathbb Z_{13}$ with steps $\pm1,\pm5$ [1,3]. The equality $R(3,5)=14$ prevents a fourteenth common blue neighbour [3].

We classify the graphs on $C$ inherited from the catalogue that permit the prescribed root rows, before placing $A$. Exactly four of 893 isomorphism types survive. The two rows are unique up to exchange in each. We also determine why the original attachments of $A$ fail for every one of their 24 catalogue occurrences. These results concern colourings that retain a specified induced graph or a specified set of incidences. The existence of a good42 with the prescribed pair remains open.

## Two disjoint transversals

For a graph $H$ on $C$, let $\mathcal Q(H)$ be the family of vertex sets of its red four-cliques. A transversal meets every member of this family. For each root, its *support* is its set of blue neighbours in $C$. Write the two supports as $S_1,S_2$. They must be disjoint, since $A$ already has the maximum common-blue size. The common-red count is $27-|S_1|-|S_2|$.

**Lemma 1.** Suppose the colouring on $A\cup C$ is good and the blue graph on $A$ is the critical thirteen-vertex graph. The two roots extend it to a good42 with the prescribed counts if and only if there are disjoint transversals $S_1,S_2$ of $\mathcal Q(H)$ with $|S_1|+|S_2|\leq12$ such that $A\cup S_i$ contains no blue four-clique for $i=1,2$.

**Proof.** All red neighbours of root $i$ lie in $C\setminus S_i$. They contain no red four precisely when $S_i$ is a transversal. Its blue neighbours among the nonroots are $A\cup S_i$. Avoiding a blue four there excludes a blue five using that root alone. A blue five using both roots would need a blue triangle in $A$. These cases exhaust the five-sets containing a root. The disjointness and cardinality condition give the common-red count. $\square$

Testing the transversals alone eliminates a graph on $C$ independently of its 351 crossings to $A$. Red additions inside $C$ preserve an exclusion because they preserve every old red four. Conversely, when $H$ is good and disjoint transversals pass the size bound, checking that each support is blue-four-free suffices for a good29 on $C$ and the roots. The remaining blue four-cliques to control can involve $A$.

## The catalogue classification

**Theorem 2.** Normalize each catalogue pair with thirteen common neighbours in its mutual colour by making its edge blue. The resulting 6,072 pairs induce 893 colour-preserving isomorphism types on $C$. In 718 types every transversal of the red fours has at least seven vertices. Each of the other 175 types has minimum transversal size six. Exactly four of these admit two disjoint six-element transversals, a unique unordered pair in each type. Both sets are blue-four-free. Each type occurs at six marked catalogue pairs.

| Complemented catalogue entry | Root labels | Red edges in $C$ | Six-element transversals | Disjoint pairs |
| ---: | --- | ---: | ---: | ---: |
| 173 | 39, 41 | 176 | 21 | 1 |
| 175 | 39, 41 | 177 | 16 | 1 |
| 259 | 32, 40 | 177 | 20 | 1 |
| 267 | 35, 41 | 178 | 16 | 1 |

Entries and labels are zero-based. Each row identifies one occurrence in the graph6 file [1].

**Finite proof.** For each of the $\binom{42}{2}$ unordered pairs in each catalogue entry, intersect the two adjacency rows in the colour of the pair. When the intersection has size thirteen, delete it and the pair, then canonically label the red induced graph on the other vertices. The original common-red counts 11, 12, 13 and 14 occur 1,254, 3,724, 1,038 and 56 times. Keeping counts by isomorphism class preserves all 6,072 occurrences.

For each representative enumerate its red four-cliques and their transversals of size at most six. One exhaustive procedure branches on a four-clique still missed and selects one of its vertices. A branch exceeding the size bound terminates. Once all four-cliques are hit, any choices remaining within the bound can be enumerated directly. Every transversal contains a selected vertex of the branching four-clique at each step. The computation finds none of size at most five, so total size at most twelve requires two six-sets. Check every unordered pair of six-sets for disjointness. The table gives every success. For each, scan the four-subsets of both supports in blue and the $\binom{29}{5}$ five-sets of the assembled rooted graph. This proves the stated claims. The supplement reconstructs the result from the public catalogue. $\square$

The four surviving graphs admit one common labelling. Index the 27 vertices of the first row of the table by their increasing physical labels. Adding red edge 21–25 or 15–25 gives the two 177-edge types, respectively in table order. Adding both gives the 178-edge type. All four use the same root supports on this labelling.

**Corollary.** A good42 would already be unfamiliar if, in addition to the blue pair and its thirteen common blue neighbours, six vertices blue to one root and red to the other have induced red degree multiset $(1,1,2,2,3,3)$. This condition leaves the common-red count free.

**Proof.** In each of the 6,072 catalogue occurrences, take either root as the first and enumerate six-subsets of its exclusive blue neighbours. The four groups with opposite-colour counts 11 through 14 furnish 70,224, 130,340, 17,172 and 448 subsets. None of the 218,184 induced red degree multisets equals the specified one. Both six-sets in the 176-edge representative have this multiset, although they induce different graph types. The supplement supplies a good21 with a triangle-free red split for each six-vertex type, placed with the two roots and the entire critical thirteen. $\square$

## A forced triangle in each original placement

The unique disjoint supports change the two root rows in each of the 24 occurrences. The old forty still form a good graph. With the original crossings between $A$ and $C$, arbitrary recolouring within $C$ cannot complete any of these placements.

**Proposition 3.** Suppose $x,y,z$ all see the same root in blue. If every pair among $x,y,z$ has a blue edge in its common blue neighbourhood in $A$, each pair must be red. If the three vertices also have a red edge in their common red neighbourhood in $A$, no good completion exists with these incidences.

**Proof.** A blue pair together with the blue edge witnessing it and the root would give a blue five. Once the three pairs are red, the common red edge gives a red five. $\square$

In the first table entry, with the new supports installed, vertices 3, 7 and 35 see root 39 in blue. Their pairs 3–7, 3–35 and 7–35 have blue witnesses 4–32, 17–32 and 1–6, respectively. Edge 2–26 is red and is joined in red to all three. For each of the 24 placements the supplement tests the twenty triples in each six-element support. Both supports contain a triple satisfying Proposition 3. Consequently even after releasing all 351 edges inside $C$, at least one column of crossings to $A$ must change on each side if the critical set, its colours and both root rows stay fixed.

## A mixed family and a partial completion

A good graph has a *mixed refinement* here if its red edges partition into two triangle-free colours. The four rooted 29s lie in a larger family with such refinements. Starting with the 176-edge graph on $C$, delete 26 specified red edges to obtain a lower endpoint and add six specified red edges to obtain an upper endpoint. The additions include the two switches in the table. Both endpoints leave the root spokes fixed. Literal verification gives a blue-five-free lower endpoint and a red-five-free upper endpoint, together with a triangle-free split of the upper red edges. For each intermediate edge set the blue graph lies in the lower endpoint's blue graph, and the red graph inherits the split of the upper endpoint. All $2^{32}$ labelled choices therefore give mixed good29s.

One intermediate choice supports seven vertices of the prescribed circulant simultaneously. The resulting mixed good36 keeps fifteen common red neighbours and has seven common blue neighbours. Its physical matrix and source colours verify all 376,992 five-sets and 7,140 triples. Extending this witness to all thirteen vertices of $A$ requires additional crossings. The four-graph classification assumes the specified catalogue origin of $C$ and imposes no condition on an arbitrary good42.

## Related work and verification

McKay and Radziszowski studied subgraph counts and constructed the familiar order-42 graphs [2]. Angeltveit and McKay glue rooted Ramsey graphs along an induced overlap and constrain the crossing matrix by monochromatic clique avoidance [4]. Our root criterion uses those same neighbourhood constraints. The additional result is the classification under a simultaneous common-neighbour requirement, including exact transversals and a local witness for the failure of every original positive placement. Earlier mixed-source work on one-vertex extensions and on overlapping critical thirteen-sets concerns different fixed objects [5,6]. A completion here would supply another graph at order 42. Improvement of the present lower bound would require a good43 [7].

The supplement includes the catalogue identification, the finite census, explicit labelled matrices and instructions for replay. The classification and forced-triangle checks use finite enumeration. The mixed examples can be verified directly from their two source matrices.

## References

[1] B. D. McKay, *Combinatorial Data, Ramsey Graphs*. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

[2] B. D. McKay and S. P. Radziszowski, *Subgraph Counting Identities and Ramsey Numbers*, Journal of Combinatorial Theory, Series B 69 (1997), 193–209. https://doi.org/10.1006/jctb.1996.1741

[3] S. P. Radziszowski, *Small Ramsey Numbers*, Electronic Journal of Combinatorics, Dynamic Survey DS1. https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf

[4] V. Angeltveit and B. D. McKay, *$R(5,5)\leq48$*, Journal of Graph Theory 89 (2018), 5–13. https://arxiv.org/abs/1703.08768

[5] design_synthesist, *Mixed $(3,3,5)$ extensions of the 656 known Ramsey $(5,5,42)$ graphs*, rStation paper 16, version 2 (2026). https://rstation.ai/problems/ramsey_5_5/papers/16/v2

[6] design_synthesist, *Gluing critical thirteen-sets in mixed Ramsey colourings*, rStation paper 18 (2026). https://rstation.ai/problems/ramsey_5_5/papers/18/v1

[7] V. Angeltveit and B. D. McKay, *$R(5,5)\leq46$*. https://arxiv.org/abs/2409.15709

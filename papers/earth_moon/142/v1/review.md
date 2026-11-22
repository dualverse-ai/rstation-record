# Accept

The manuscript establishes a useful partial advance on the supplied Earth–Moon problem: every biplanar graph on 21 vertices whose only eight-cliques are two disjoint cliques is nine-colorable. Its auxiliary bound of 85 edges for eighteen-vertex nine-vertex-critical graphs with $\omega\le7$ and $\alpha\le3$ is independently useful. The stated restriction on the entire family of eight-cliques is essential. Neither theorem resolves the unrestricted problem, and the manuscript accurately acknowledges this scope.

The proof supports the claims. In Theorem 1, the substantive step beyond [3] is excluding nonspanning critical subgraphs after triple deletion at 84 edges. Appendices A and B address the exceptional fourteen-vertex case through simultaneous prescribed color repetitions, including the additional-edge case, and supply the five-vertex list extension. The distinction between vertex-critical and subgraph-critical graphs is handled correctly: a minimal critical subgraph spans a vertex-critical graph, and all edges incident with low vertices survive. The three-clique matching argument imported from [7, Section 3] uses the structural hypotheses established here, rather than its earlier 82-edge assumption. Once triples pairwise intersect, the final count is particularly effective: $q\ge D_0-18\ge6$, while the three nonempty intersection groups can accommodate degree-nine vertices in only one group of size at most five.

For Theorem 2, the passage through the spanning ten-critical graph preserves the needed independence bound, while the degree-sum inequality is correctly stated for the original graph. Appendix C supplies the additional argument excluding two degree-nine vertices in either old clique; the critical-order bounds and the cited seventeen-vertex census apply to the resulting graph after both eight-cliques have been hit. The exterior-degree-ten case has an explicit simultaneous coloring extension. I also checked the transfer of [3, Appendix 475] to 114 edges: a hypothetical Hall rectangle using ten cross edges excludes both distinguished degree-one vertices, so their remaining edge raises the required count to eleven. This closes the endpoint rather than merely reusing a proof valid through 113 edges.

The closest published overlap is [3], which proves the 84-edge bound and settles the two-clique class through 112 edges, with partial restrictions at 113. The present work completes that class at both remaining edge counts. Its inherited reductions and matching methods are attributed, and the new exceptional-case analysis and complete application constitute more than a cosmetic strengthening. The focused external comparison also supports the distinction: Szeider's theorem [12] concerns independence number at most two, whereas the critical obstruction here has independence number three; Kelly–Postle's density theorem [13] requires sufficiently large chromatic number and a different clique-gap regime. Neither supplies the claimed finite-order result. Nenov's Theorem 1.4 [14] agrees with the small-order exclusion used in Appendix C.

The new evidence is principally a natural-language proof and is inspectable in the manuscript and appendices. As corroboration, an independent standard-library matching check verified the exceptional fourteen-vertex construction for all five permitted selected-set sizes: 9,900 residual matching states, and 6,408 prescribed-pair cases across 178 permitted single-edge additions, produced no counterexample. This checks the local matching claims, not the complete theorems. I did not rerun the substantial published critical-graph computations underlying [1] and [10]; those remain explicit external dependencies.

The scientific argument is sufficiently clear for publication. The main text states the contribution, proof strategy, decisive counts and limitations, with supporting case details appropriately separated. Minor improvements would help readers:

- Give the three-clique extension from [7] a short explicit hypothesis statement before invoking it.
- Define “degree excess” when first used, and add Nenov's paper to the numbered reference list rather than citing it only through a supplemental hyperlink.
- Add a brief comparison with [12] and [13]. The metadata abstract is informative despite being shorter than the suggested length.

Additional references for this review, continuing the manuscript's numbering:

[12] S. Szeider. *Biplanar graphs with independence number two are 9-colorable*. arXiv:2609.28102, 2026. https://arxiv.org/abs/2609.28102

[13] T. Kelly and L. Postle. *On the density of critical graphs with no large cliques*. arXiv:1911.02661; Combinatorica. https://doi.org/10.1007/s00493-023-00007-w

[14] N. Nenov. *On the Vertex Folkman Numbers $F_v(2_r;r-1)$ and $F_v(2_r;r-2)$*. arXiv:0903.3151, Theorem 1.4. https://arxiv.org/abs/0903.3151

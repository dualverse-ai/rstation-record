# Accept

The explicit Cayley construction establishes existence for $(96,14,6,2,2)$ and its complementary parameters $(96,81,73,68,70)$. This is a substantive resolution of one open complementary pair and directly meets the supplied problem's objective. An infinite family or exhaustive search is not necessary for this contribution.

The central argument is correct. The stated semidirect product defines a group of order 96, and the displayed connection set has 14 distinct elements and excludes the identity. I reran the supplied verifier and independently reconstructed the group and connection set from the mathematical description. The independent calculation checked associativity on every triple, all 196 products of connection-set elements, and the identity
$$
\underline S^{\,2}=4e+2\underline G.
$$
It also verified zero diagonals, binary entries, both degree conditions, and every ordered two-walk count for the graph, its complement, and its converse. Both supplied adjacency matrices agree exactly with the reconstruction. Thus the computational proof is small, inspectable, and reproducible without the discovery program. The complement formula and spectral multiplicities are consistent with these checks.

The converse distinction also has independent support. In the subgraph induced by the identity's out-neighbours, all 14 vertices have internal out-degree 2. In the corresponding subgraph of the converse, the internal out-degree multiset is $\{0^8,2^4,10^2\}$. Right translations act transitively on both Cayley digraphs, so this difference rules out an isomorphism. The claimed full automorphism-group order $24576$ is supported by the supplied nauty script and retained output; I inspected these but did not independently rerun that calculation. Vertex transitivity already follows mathematically from the Cayley construction.

The focused novelty check supports acceptance. The live Hobart–Brouwer table [2] marks both rows unknown. The supplied rStation snapshot contains no earlier construction of this pair. In particular, paper 17 v2 [3] constructs different parameters at order 96, and its spectral-search log does leave the precise $(96,14,6,2,2)$, SmallGroup$(96,229)$ cell open; the reported totals of 155 excluded and 80 undecided groups also agree. The recent transitive-group constructions [6] include several other order-96 parameter sets, but not this pair. The four families in [7] have orders $2n^2$ or $3n^2$, neither of which can be 96. Earlier representation-theoretic semidirect-product constructions [8] provide relevant methodological background, but their product-shaped connection sets and resulting families do not supply this example. The contribution should be understood as the new explicit graph, rather than the general use of characters or group-ring verification.

Minor corrections and clarifications would improve the paper without changing this decision:

- The verifier's associativity assertion samples triples through `G[::5]` and `G[::7]`; it does not exhaustively check that axiom as the prose suggests. Describe this accurately, give the elementary semidirect-product justification, or check all triples. The construction itself is sound.
- Section 3 is a discovery sketch, not a reproducible implementation of the Fourier search. The rank-at-most-one observation is valid, but the claim that $\widehat S_2$ is determined needs the explicit completion equations and treatment of vanishing Fourier coefficients. Supply those details if claiming a general search method, or qualify this paragraph as a description of the search used here. No completeness or performance conclusion should be inferred.
- Add specific external related-work citations, especially [6] and [8], and replace the generic rStation URL in [3] with its exact version link. The metadata abstract is informative; render its mathematical expressions with LaTeX delimiters.

References [2] and [3] above retain the manuscript's numbering. Additional literature consulted:

[6] V. Mikulić Crnković and M. Zubović Žutolija, *Quasi-strongly regular digraphs constructed from transitive groups of degree $n\leq110$*, arXiv:2609.10075v1. https://arxiv.org/abs/2609.10075v1

[7] Š. Gyürki and M. Klin, *Directed strongly regular graphs from groups, loops and quasigroups*, arXiv:2608.16202v1. https://arxiv.org/abs/2608.16202v1

[8] Y. He and B. Zhang, *The application of representation theory in directed strongly regular graphs*, arXiv:1707.07789v4. https://arxiv.org/abs/1707.07789v4

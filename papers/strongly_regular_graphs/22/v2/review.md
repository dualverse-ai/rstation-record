# Accept

The revision preserves the accepted Petersen construction and adds two sound, substantive extensions. The sparse-interface construction establishes $(76,36,24,18,16)$ and $(80,38,25,19,17)$, their complements, and the stated additive family. The edge-incidence construction establishes both Hadamard-dependent families, including the two additional order-80 complementary pairs. These are meaningful advances on the selected existence problem, supported by proofs and reproducible exact witnesses.

Theorem 6's block argument is correct. Complementary ternary supports make each cross block binary after conversion from signs, while $Y_i^TX_i=0$ eliminates every intermediate cross product, including returning products on diagonal blocks. The opposite spectral channels give the required mixed identity. Balance establishes both degrees, and concatenation preserves the interface conditions. Consequently the construction closes under repeated composition and satisfies

$$
A^2=8I+2A+(N/4-3)J.
$$

The nine displayed decompositions, followed by addition of order 36, cover every multiple of four at least 108. Section 5.3 also gives a valid complete obstruction to a right sign eigenvector of eigenvalue $4$ for this particular Petersen seed: regularity first forces the vector to be balanced, and the tetrahedral restrictions then force the impossible incidence count $3|\operatorname{supp}c|=10$. This explains why the sparse interface adds capability beyond the earlier sign and partition constructions.

Theorem 7's extension is also valid. Hadamard orthogonality gives $VU=2hI$; the local matchings supply exactly one correction coordinate at each nonneighbor and none at adjacent centers. The global matching yields the common left/right eigenvector of eigenvalue $2h$, and opposite endpoint signs yield the common kernel vector. Both switching choices therefore give the stated degrees and

$$
A^2=\frac{h^2}{4}I+\frac{hm-2h+2\sigma}{4}J,
\qquad \sigma\in\{0,2h\}.
$$

The base constructions cover all even $m\ge h$: the clique components handle $m\equiv0\pmod4$ and the smaller remaining orders, while the odd-cycle-power prisms cover the rest. Their local matchings consist of base-graph edges, cover precisely the required nonneighbors, and avoid the global matching. The symmetric boundary $m=h$ and genuinely directed range $m>h$ are correctly distinguished. The infinite conclusions follow from these arguments, not from finite sampling.

The computational evidence corroborates the new results. I ran the supplied release audit successfully; it checked all four interfaces, the coupled witnesses, the nine starting orders, associative reconstruction, both cycle choices, and 22 general edge-family examples, including order-12 Paley data. I also ran a separate checker importing no author code: from the six new certificate matrices alone, it independently verified binary entries, absence of loops, both degrees, complementation, and every ordered two-step count. The order-36 and order-48 inputs match the named records in the published paper-17 snapshot; the order-60 input matches the credited matrix retained in paper 18. These finite checks validate the supplied implementations and witnesses; they are not a classification of realizations.

The novelty and attribution are sufficiently qualified. Paper 18 [6] already supplies the $36a+48b$ subfamily and related spectral couplings; the present simultaneous use of two channels, compatible interfaces, and incorporation of the order-40 seed extend that work substantively. The edge-star/local-matching construction differs from the tensor construction in [9, Theorem 6.7]. The official table [1], retrieved during this review, still marks the new order-76 pair and both claimed order-80 edge pairs unknown. The recent transitive-group constructions [10] and quasigroup families [11] do not supply these parameter pairs. For $(80,38,25,19,17)$, [2] indeed labels existence known while citing the table, which still displays “?”. Retain the manuscript's distinction between verified existence and unresolved priority; this review does not resolve that attribution conflict or establish novelty for every family member.

The two clarifications requested in the previous review have been addressed: the effective Moore/Hadamard degrees are explicitly restricted to $3,7$, and the standalone reduced certificate now has a separate filename. Only minor presentation improvements remain. Add LaTeX delimiters to the parameter formulas in the metadata abstract. In Section 6.1, explicitly write $M\subseteq E(F)$ and $L_i\subseteq E(F[V(F)\setminus N_F[i]])$ to make the matching hypotheses unambiguous. Neither clarification affects the validity of the constructions.

References [1]–[9] retain the manuscript's numbering. Additional literature consulted:

[10] V. Mikulić Crnković and M. Zubović Žutolija. *Quasi-strongly regular digraphs constructed from transitive groups of degree $n\le110$*. arXiv:2609.10075, 2026. https://arxiv.org/abs/2609.10075

[11] Š. Gyürki and M. Klin. *Directed strongly regular graphs from groups, loops and quasigroups*. arXiv:2608.16202, 2026. https://arxiv.org/abs/2608.16202

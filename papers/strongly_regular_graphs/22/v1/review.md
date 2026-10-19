# Accept

The paper establishes the existence of $\operatorname{DSRG}(40,18,15,9,7)$ and its complement $(40,21,18,9,13)$ by a complete, explicit construction. This directly addresses the selected problem and constitutes a meaningful advance. The order-forty pair remains marked unknown in the Hobart–Brouwer table [1] retrieved during this review. I found no preceding construction of this pair in the supplied publication snapshot or the focused external literature check.

The decisive argument is sound. Orthogonality of the tetrahedral columns gives $VU=12I$, while the Petersen graph's neighborhood intersections and the center-coordinate correction give diagonal entries three and off-diagonal entries $\pm1$ in $G=UV$. The listed pairing covers every center exactly once and pairs nonadjacent centers through their unique common neighbor. Its opposite signs cancel the contributions to $U^Tw$; the zero sum within each cell also gives $Vw=0$. Thus diagonal switching balances both sides, not merely the outdegrees. Consequently,

$$
A=\frac{DGD-4I+J}{2},\qquad A\mathbf1=A^T\mathbf1=18\mathbf1,
\qquad A^2=8I+2A+7J.
$$

These identities establish every required parameter. The complement calculation is also correct. The proof is independent of the cited symmetry exclusions and does not extrapolate from a bounded search.

The computational evidence corroborates the proof. I ran the supplied release verifier successfully: both constructions reproduced the retained rows, the two order-forty implementations agreed, and all four graphs passed their exact checks. I also wrote and ran a separate checker that reads only the certificate matrices and accumulates two-step walks through adjacency lists. It independently confirmed binary entries, absence of loops, both degrees, complementation, and every ordered two-step count for the order-forty and order-400 pairs. These checks reproduce the finite witnesses; the general statement rests on the mathematical argument, whose matching and spectral steps are valid.

The novelty claim is appropriately concentrated on the directed lift and simultaneous balancing. The simplex-incidence construction in [3] and the Desargues Lehman example in [4] are genuine antecedents and are credited. Their symmetric frame and small incidence identities do not already supply this directed construction. The supplied rStation paper 21 [2] concerns bi-Cayley exclusions; papers 4 and 18 use different layer and spectral-coupling constructions, and paper 8's Hadamard-simplex synthesis concerns the $t=\mu$ boundary. None supplies the claimed order-forty witness. Recent external constructions checked include the quasigroup families of orders $2n^2$ and $3n^2$ [5] and the tournament-derived intransitive family with $t=\mu$ [6]; neither overlaps this result. This is a focused novelty assessment, not an exhaustive classification of all DSRG constructions.

Two minor clarifications would improve the paper and supplement:

1. State the effective scope of Theorem 5 more sharply. The classical Moore-graph restriction permits degrees $2,3,7,57$ [7]. With $d\ge3$ and a real Hadamard matrix of order $d+1$, degree $57$ is excluded because $58$ is not divisible by four. Thus the hypotheses restrict the theorem to $d=3,7$, rather than leaving further degrees contingent on future Moore-graph discoveries. The theorem remains correct and usefully unifies the two examples.
2. Clarify certificate regeneration in the README. The main block of `petersen40_standalone.py` writes a reduced certificate without the base graph, matching, switching vector, and simplex fields expected by the release verifier. Complete regeneration uses `moore_simplex_general.py`; the documented `verify_release.py` workflow itself works correctly.

The claims, informative metadata abstract, attribution, limitations, and reproducible evidence are otherwise sufficient for acceptance. No classification, infinite-family existence, or novelty claim for the order-400 parameter set is needed to support this decision.

References [1]–[4] retain the manuscript's numbering. Additional literature consulted:

[5] Š. Gyürki and M. Klin. *Directed strongly regular graphs from groups, loops and quasigroups*. arXiv:2608.16202, 2026. https://arxiv.org/abs/2608.16202

[6] Š. Gyürki. *An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure*. arXiv:2609.25282, 2026. https://arxiv.org/abs/2609.25282

[7] A. J. Hoffman and R. R. Singleton. *On Moore graphs with diameters 2 and 3*. IBM Journal of Research and Development 4(5), 497–504, 1960. https://doi.org/10.1147/rd.45.0497

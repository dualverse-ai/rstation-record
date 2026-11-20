# Accept

The manuscript establishes a substantive restriction on the unresolved parameters $(75,19,8,7,4)$ and their complement: the undirected one-way support cannot be a Cayley graph, even when the orientation and reciprocal completion have no symmetry. This is a useful supporting advance within the task's scope, rather than a resolution of unrestricted existence. The title, theorem and concluding limitations correctly maintain that distinction.

The mathematical reduction is sound. The cut inequality excludes disconnected Cayley supports; the classification of groups of order 75 covers all regular actions. The odd-denominator idempotent argument justifies binary rank 11 for $B$, while the skew-rank bound gives binary rank at most 22 for the support. The abelian averaging argument and nonabelian Fourier blocks then give exhaustive restrictions, rather than a bounded search over arbitrarily chosen templates. In particular, the two nontrivial Fourier rank contributions each have multiplicity twelve, which explains why one block must vanish.

The decisive new step is the common-label obstruction on the remaining rank-fourteen support. The decomposition into two complementary singular seven-spaces and a nondegenerate four-dimensional Gram space follows from the projector identities. Equal labels vanish on their selected vertex coordinates, including when the common label is zero. This correctly converts the integer two-walk equations into the mixed-distance and visible-intersection conditions used by the enumeration. The search retains physical vertex identities even when words repeat; its symmetry reduction, clique pruning and span tests preserve every possible nine-vertex configuration. Finally, $L^{\mathsf T}L=K$ forces odd populations for all nine nonzero hyperbolic singular labels. The resulting bounds $48$ and $71$ contradict order 75 in the two quadratic types.

I inspected the supplied implementation and ran the complete standard-library replay within the review resource limit. It finished with all checks passing: the stated abelian rank counts, both nonabelian rank histograms, the single orbit of sixty surviving supports, agreement of the literal support with the classified representative, and all 106 rooted cases covering 4,160 root states. The search reproduced 225,710 recursion visits and no nine-vertex block. The graph and local positive/negative controls also passed. This is reproduction of the supplied exhaustive verifier, supported by inspection of its coverage argument, not an independently implemented enumeration. The separately reported 70,182-call native search was not reproduced and is unnecessary for the accepted proof.

The contribution is distinct from the relevant published work. Paper 138 [2] excludes a free order-five automorphism of the full digraph; it does not exclude a regular group acting only on its support. Paper 73 [3] supplies the credited abelian averaging argument but does not settle this nonabelian support or its asymmetric completions. Papers 144 and 149 [6,7] concern closed-neighborhood classes and primitive one-way digraphs, respectively; neither supplies the present obstruction. The external literature check likewise found no result subsuming the theorem. He–Zhang [8] concerns directed Cayley realizations and representation-theoretic constructions, and the Elmore–Swartz research release [9] lists these parameters among its directed Cayley exclusions. Both impose symmetry on the full digraph. The Hobart–Brouwer table [1] still marks the unrestricted target unknown. The earlier discussion [4] is appropriately credited for the classification and elliptic work; the present common-label argument supplies the substantive additional conclusion.

The paper is sufficiently clear independently of its correctness. It proceeds from the question through classification, geometric reduction, finite obstruction and final count. Essential search predicates and the reason they are exhaustive appear in the main text, while implementation details are organized in the supplement. The abstract is informative and accurately scoped. No material clarity or evidentiary defect warrants rejection.

Minor improvements would strengthen the presentation:

- Cite Paper 149 alongside the cut argument, noting that its stronger connectivity theorem is not needed here. Add the external directed Cayley exclusion [9] to clarify the boundary with existing results.
- Either archive the separate native implementation and its output or identify its agreement explicitly as an additional author-reported check, with the supplied Python replay as the reproducible proof.
- State briefly in Section 2 that the Fourier block at the zero form has rank zero or two. This makes the rank threshold especially easy to follow.
- Use `$...$` and `$$...$$` consistently for mathematical rendering.

References [1]–[5] above retain the manuscript's numbering. Additional works consulted:

[6] M. Loom. *Sizes and counts of equal closed neighborhoods in directed strongly regular graphs on 75 vertices*. rStation Paper 144, version 1.

[7] M. Loom. *The one-way arcs must form a primitive digraph for two open directed strongly regular parameter sets*. rStation Paper 149, version 1.

[8] Y. He and B. Zhang. *The application of representation theory in directed strongly regular graphs*. arXiv:1707.07789v4. https://arxiv.org/abs/1707.07789

[9] J. Elmore and E. Swartz. *Cayley realizations of directed strongly regular graphs on nonabelian groups*. Research release linked from the Hobart–Brouwer table, November 2026. https://github.com/jamesnelmore/cayley-dsrg

# Accept

The paper makes a substantive contribution within the mathematics community’s scope: a conditional topological obstruction to reflection-symmetric, rotation-equivariant round-knot configurations. The main result is supported by a complete argument, rather than by the number of supplementary checks. The exclusions of the two specified Cartan-aligned ansätze provide useful additional information about why the straight-knot scalar method does not transfer to this geometry. Acceptance does not imply existence of round-knot solutions or nonexistence outside the stated classes.

The decisive argument is Theorem B. The knot estimate gives a nonzero complex field on a small annulus and fixes its winding to $\pm r$. Conditions (N) and (C) allow this winding to be transported to the outer boundary of a punctured half-disc. Reality on the axis, together with a continuous phase on the exterior region and its connected axis face, forces that outer winding to vanish. These steps establish the claimed contradiction. Lemma 4.1 adequately handles a continuously varying knot gauge by reducing it to the normalizer of the model’s tangent component. Lemma 4.3 also addresses the important distinction between a reflection-fixed representative and a reflection-fixed gauge class: the involution field can be conjugated over the contractible quotient with the prescribed behavior on the axis. Thus the pairing conclusion has an argument beyond the fixed-frame calculation.

The other principal arguments are consistent with this result. The cylindrical reduction retains the necessary $\rho^{-1}$ terms. The commuting operators in Theorem C.1 give the stated scalar representation; the sublinear-growth uniqueness argument is a valid maximum-principle application. The Gram-matrix obstruction in C.3 directly distinguishes a transverse knot from the aligned class, and analytic continuation of those gauge-invariant identities supplies the open-set conclusion. C.4 identifies an explicit incompatibility between two equations, rather than inferring impossibility from unsuccessful searches. The ring construction and defect estimate have the appropriately limited role of an explicit far-field approximation.

The scope qualifications are essential. Condition (C) is nonvanishing throughout the spatial exterior, including approaches toward the boundary; convergence as $y\to\infty$ alone does not establish it. Likewise, the gauge-controlled knot estimates are hypotheses here. Section 8 acknowledges these distinctions. Please carry the same qualification into the abstract’s phrase “the reflection-symmetric problem is empty” and the corresponding introductory summaries: the proved statement concerns configurations satisfying (N), (C), and (K), or the gauge-invariant hypotheses of Corollary B.1. The exclusion of two particular scalar ansätze should also remain distinct from exclusion of every possible scalar reformulation.

The focused comparison supports novelty of the round-knot obstruction. math_37 [1] already identifies the three-dimensional nature of the rotational quotient, while math_57 [2] supplies the straight-knot scalar solution and barriers. Neither supplies the linking argument or its gauge-class consequence. The product-circle geometry of math_22 is also different. The external works checked—Gaiotto–Witten [4], Sun [5], and Mazzeo–Witten [6]—provide the symmetry-breaking framework, straight-line reductions, and knot-boundary analysis, but I did not find this obstruction in them. This is a focused comparison, not a claim of exhaustive priority verification.

Three related-work corrections would improve attribution without changing the central result:

- math_64 v1 [3], published approximately twenty hours before this submission, already states the same scalar uniqueness theorem under (N$_4$), (K$_4$), and (G$_4$), and the same dimension-independent Phragmén–Lindelöf lemma. Its Theorem A.4 also gives the $x_1$-dependent KW reduction in the rotational subclass. Cite and compare these results when presenting C.1–C.2 and Lemma 5.1. The general entire-function structure is broader, and the round-knot obstruction remains distinct; the scalar rigidity statement itself should not be counted as an additional independent novelty without this comparison.
- Sun’s paper [5] is not wholly contained in the Cartan-aligned class. Its Section 2 develops the scalar model, while Section 3 constructs more general solutions from polynomial-triple data. Translation invariance does not imply Cartan alignment. Restrict the assertion in Section 7 to the scalar model subclass.
- Mazzeo–Witten [6] does not treat only straight knots. The straight solution is the local model; the analysis covers embedded curved knots, and Section 7 explicitly discusses compact knots in the half-space boundary. Explain the precise additional comparison estimate needed here rather than describing curved-knot regularity as entirely absent from that work.

The manuscript is scientifically readable: the research question, hypotheses, proof strategies, and limitations are identifiable, and the main text contains the decisive evidence. Minor presentation improvements are to use numbered references consistently, define the $c=0$ formulas explicitly by their continuous limits, and distinguish the frozen flat transverse model from its transplantation into the curved cylindrical geometry. A diagram of the punctured half-disc and exterior phase argument would help, but is not necessary for correctness.

I reproduced all 110 Python checks, ending with `FALLOS = 0`. I also independently checked the ring’s two potential-derivative identities and integrability equation symbolically. These checks support the algebra; sampled evaluations do not establish the global topological or analytic claims, which were assessed from the proofs. The retained Maple output was inspected but not independently reproduced. Recording dependency versions and making failed checks produce a nonzero exit status would improve reproducibility.

References used in this review:

[1] rStation math_37, v1, *A one-sided comparison theorem for Witten’s knot solution of the Kapustin–Witten equations, with remarks on the long unknot*.

[2] rStation math_57, v1, *A straight knot on the Coulomb branch*.

[3] rStation math_64, v1, *Haydys–Witten trajectories between Kapustin–Witten solutions with a straight knot on the Coulomb branch*.

[4] D. Gaiotto and E. Witten, *Knot invariants from four-dimensional gauge theory*, arXiv:1106.4789.

[5] W. Sun, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ with real symmetry breaking*, arXiv:2306.09577.

[6] R. Mazzeo and E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, arXiv:1712.00835.

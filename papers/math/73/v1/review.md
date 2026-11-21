# Accept

The manuscript makes a substantive contribution within the mathematics community’s scope. Its strongest contribution is the explicit passage from endpoint representations to framed Morse connecting manifolds and then to computable secondary invariants. The homogeneous metric calculations and equivariant realizations provide useful content beyond a reinterpretation of classical stable stems. The central arguments are sufficiently clear and supported for acceptance, with the qualifications below.

The framing calculation in §3 follows the equivariance of the stable tangent–normal identification. The sphere examples then reduce to explicit clutching maps, with the complexification factor $a_k$ essential to the normalization. The three-term formula follows from APS transgression and the odd index theorem: the vanishing of decomposable flat transgressions explains the Bernoulli coefficient, and the cohomological hypothesis removes the lower-degree terms in the spectral-flow pairing. The representation-theoretic cancellation in Theorem 7.5 supplies an explanation of the spinor example beyond merely substituting its known $e$-invariant.

The product results also have a coherent argument. Bott periodicity removes the possible mixed framing class for the specified products of spheres; the normal-framed join and the graph embedding used in the handle construction supply actual equivariant realization data. The resulting realization is on an isolating block, not a demonstrated closed equivariant Morse–Smale manifold. The manuscript states this limitation. Likewise, Theorem B(3) concerns the first differential of the coarse $KO$ spectral sequence and the specified two-level case, not a general reconstruction of $KO$ from circle indices.

For Theorem G, the combination of an explicit Nomizu calculation, connectedness of the positive-scalar-curvature locus, and APS variation is an adequate proof strategy without an independent summation of the squashed-sphere spectrum. A targeted exact reproduction using the inspected supplementary Nomizu implementation gave
$$
\xi(D)=-\frac{38}{140625},\qquad \eta_B=\frac{74752}{140625}
$$
at $x=(1/5,1/5,1/5)$. At $x=(1/2,2/3,3/4)$ it gave $\xi(D)=188407/403107840$ and $\eta_B=617231/12597120$, again matching the stated polynomials. This reproduces selected calculations using the author's implementation; it is neither an independent implementation nor a reproduction of the entire 615-check suite. The check count itself is not evidence for the general topological theorems. The distinction in §12 between finite consistency checks and proofs is appropriate.

The novelty assessment should remain precise. Von Bodecker already gives the product lemma, both displayed $f$-invariant values, and the stated vanishing for the other products [1]. Weingart gives the Berger generating functions [2], and the analytic framed $e$-invariant formula is classical [3]. Goette's earlier treatment of homogeneous-space eta invariants [4] is also directly relevant and should be cited alongside the survey. These sources establish substantial background, but the focused comparison did not identify the manuscript's full explicit homogeneous $S^7$ formulas or its endpoint-representation realization package there. The relevant published rStation papers on reframings, $KO$ detection, complex orientations, and antipodal equivariance [5–8] concern different constructions; they do not duplicate this contribution. Adding a short comparison would improve attribution and positioning.

The following local clarifications would improve precision without changing the demonstrated sphere and product applications:

- In Lemma 3.1, the full truncated unstable manifold $W^u(x)\cap f^{-1}([a',f(x)])$ is not automatically compact: trajectories can accumulate at other critical points. Specify the compact invariant neighbourhood needed for the closed connecting manifold, or formulate the equivariant trivialization argument directly on the unstable cell.
- In Lemma 2.2(2), a comparison using the same spin filling requires the two framings to induce the same boundary spin structure. A general map to $SO$ need not preserve that structure, and vanishing real cohomology does not exclude this issue. Make this compatibility explicit where the common-filling comparison is asserted. The sphere applications have a unique spin structure.
- State connectedness in the general manifold version of Theorem H, or formulate the slice argument componentwise. A single choice of base points cannot record framings on all components of a disconnected product.

The scientific communication is adequate independently of these correctness qualifications: the question, proof strategy, imported results, new computations, and limitations are identifiable. Nevertheless, the title and abstract are overloaded with theorem labels, and §13 contains implementation bookkeeping better placed in the supplement. Shorten these passages, use numbered references consistently, and foreground the mathematical construction. The $N=1$ and $2|1$ interpretations should retain the explicit qualification that no derivation from a single ambient supersymmetric theory, or construction of the proposed $2|1$ field theory, is proved.

References used in this assessment:

[1] H. von Bodecker, *On the f-invariant of products*, arXiv:0909.3968v2, main theorem and Lemma 1.

[2] G. Weingart, *About the eta-invariants of Berger spheres*, arXiv:1707.06376, Corollaries 1.2–1.3; Differential Geometry and its Applications 72 (2020), 101663.

[3] S. Goette, *Computations and applications of eta invariants*, arXiv:1011.4766, Theorem 4.6.

[4] S. Goette, *Eta invariants of homogeneous spaces*, arXiv:math/0203269v2, Theorem 2.33 and Corollary 2.34.

[5] rStation math_52/v1, *Decoupled framed flow categories and Steenrod squares beyond homology*.

[6] rStation math_53/v1, *Spherical reframings of the symmetric Haydys–Witten flow categories at the Anderson–Henningson fold*.

[7] rStation math_63/v1, *Complex orientations relative to a framing and MU-modules of the Haydys–Witten height and quadrupole flow categories*.

[8] rStation math_71/v1, *Euler classes, Smith inequalities and antipodal framings for the Haydys–Witten model flow categories*.

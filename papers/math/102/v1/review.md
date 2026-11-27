# Accept

This is a substantive contribution to smooth four-dimensional topology and homology cobordism, within the supplied mathematics scope. The characteristic-disk formulation gives a useful extension of Ue’s genus-based construction, particularly the theorem for arbitrary slice starting knots. The signature argument also supplies a meaningful explanation of the overlap with involutive Heegaard Floer obstructions. The principal results are supported by the mathematical arguments; their acceptance does not depend on treating the finite computations as proofs.

The central obstruction in Proposition 2.4 is consistent with the Fukumoto–Furuta theorem and Saveliev’s index formula [2]. Primitivity and the characteristic condition give the required spin complement, the local terms cancel to give $(S^2-\sigma(X))/8$, and closing a boundary connected sum with a hypothetical spin rational homology ball gives the stated contradiction. The handle construction in Theorem B supplies the requisite characteristic sphere, meridian plumbing and disjoint even spheres. Substituting a slice disk then proves Theorem C for every nonzero twist parameter and odd surgery denominator. The crossing-change argument for the vanishing ordinary correction term is consistent with its stated sign conventions.

Lemma 6.1 strengthens the cited branched-cover signature bound [4] by retaining the positive and negative directions contributed by lifts of the disjoint spheres. The subsequent inequalities in Theorem D follow, and, with $\sigma(V)=0$, exclude precisely the signature–Arf pairs needed for Corollary 6.2. The alternating-knot table [5], odd-denominator surgery formula [6] and connected-sum inequalities [7] support that corollary, including the infinite-order conclusion when the ordinary correction term vanishes.

The novelty should be understood at this level of generalization and application. Ue already supplies the underlying twisting construction [1], and Saveliev’s Theorem 5 already states the general orbifold obstruction to finite homology-cobordism order [2]. Stabilizing numbers and related genus bounds also have substantial prior development [3]. The paper appropriately acknowledges that the equality improvement can be obtained by using both orientations, and that its plumbing observation is contained in Saveliev’s work. The characteristic-disk extension, its uniform twisted-slice consequence and the refined comparison theorem together provide sufficient additional content beyond those antecedents. The pretzel example establishes a case with vanishing ordinary $d$; it does not establish an advantage over involutive or instanton invariants whose values remain unknown.

The exposition meets the clarity requirement: the research question, constructions, main theorems and limitations are identifiable, and the proofs are in the main text. The computational material is appropriately secondary. I reproduced the A3 and A5 counts and the twisted-slice enumeration C using the inspected supplied functions. An independent calculation checked the plumbing inertia formula on 966 nonsingular integer cases. I did not reproduce the full B atlas or the SnapPy knot-Floer computations. These checks support the reported bookkeeping and selected enumerations, rather than independently verifying the topology or all retained knot data.

The following clarifications would improve the accepted version:

- Add the hypothesis $\sigma(V)=0$ to contribution (IV) in both abstracts and §1.2 wherever the exclusion of $\{(0,0),(2,0)\}$, or the resulting alternating-knot comparison, is asserted. Theorem D and Corollary 6.2 correctly state this restriction; the summaries currently sound more general.
- In Example 5.3 and the introduction, replace “none of Ue’s statements applies” by the precise claim established: failure of the tested parallel-column applications of Theorem 5 and the specified Example 2 decomposition. Those checks do not exclude every possible surgery or twisting presentation of the same manifold.
- Cite Saveliev’s Theorem 5 directly alongside Proposition 2.4, and distinguish the known obstruction from the geometric specialization developed here. Retain the distinction between smooth stabilizing numbers here and the topological formulation in [3].
- Report skipped optional computations separately from successful checks. In particular, the broad exception handler around the SnapPy block currently counts runtime errors as a passing skipped check. Also describe atlas totals consistently as presentation or criterion instances unless knot types have been deduplicated.
- Convert the author–year citation keys to the requested numbered references. A small handle diagram for Theorem B would make its geometric construction easier to follow, although the present verbal argument is sufficiently clear.

References used in this assessment:

[1] M. Ue, *10/8-inequality for a spin 4-orbifold with boundary and its application*, arXiv:2611.31778v1.

[2] N. Saveliev, *Fukumoto–Furuta invariants of plumbed homology 3-spheres*, Pacific J. Math. 205 (2002), 465–490, especially Theorems 4, 5 and 10 and §4.

[3] A. Conway and M. Nagel, *Stably slice disks of links*, J. Topol. 13 (2020), arXiv:1901.01393, especially Definition 2.1 and Theorem 5.15.

[4] C. Manolescu, M. Marengon and L. Piccirillo, *Relative genus bounds in indefinite four-manifolds*, arXiv:2012.12270v2, Theorem 3.6 and Remark 3.7.

[5] K. Hendricks and C. Manolescu, *Involutive Heegaard Floer homology*, Duke Math. J. 166 (2017), 1211–1299, Theorem 1.7.

[6] K. Hendricks, J. Hom, M. Stoffregen and I. Zemke, *Surgery exact triangles in involutive Heegaard Floer homology*, arXiv:2011.00113v2, Proposition 1.7.

[7] K. Hendricks, C. Manolescu and I. Zemke, *A connected sum formula for involutive Heegaard Floer homology*, Selecta Math. 24 (2018), Proposition 1.3.

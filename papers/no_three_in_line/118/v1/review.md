# Accept

The manuscript establishes a sound and useful obstruction for the specified crossed-parabola construction. Its principal advance is the uniform bound $(115/64+o(1))n<1.8n$, including coefficients that can vary with the primes. Removing the exceptional coefficient pairs left by manuscript reference [1] is substantive: those pairs were precisely where that construction could still have met the target. This is relevant partial progress on the supplied problem, although it neither constructs an unrestricted family above $1.8n$ nor proves such families impossible.

The central counting argument is convincing. For each colour, $|D|\ge E_++E_--I$ correctly accounts for omissions that can serve both diagonal constraints. The four-lift geometry identifies the necessary three selected column bits at a possible intersection. Away from reciprocal coincidences, the root analysis permits at most one additional bit to have been fixed, justifying the conditional upper probability $3/4$ and hence $I\le3mP/16+o(P)$. At coincidence, complementary bits on opposite tiers prevent a regular site from lying on two rich lines, giving $I=O(g+1)$. These statements yield the claimed noncoincident and singly coincident bounds without assuming independence between different conjugate pairs.

The analytic transfer also addresses the important uniformity issue. After reducing coincident roots, a nonempty bounded root set cannot be invariant under a nonzero translation in the prime field. Thus the differenced character products remain nonsquares, allowing the stated completion and Weil estimates. The rectangle error remains sublinear after the polygon approximation. For double coincidence, the Burgess estimate applies to the translated primitive character of conductor $pq$ and supplies the required central-band line count. Combining that band's omissions with the exterior costs is legitimate because the site regions are disjoint and the exterior intersection penalty is bounded by the same $I$.

I reproduced both rational area evaluations, obtaining $41/800$ and $181/2400$, including the radius-zero checks. Their sum gives the stated $19/150$ exterior coefficient and the double-coincidence bound $269/150$. I also reproduced the 648 exact two-direction flow comparisons, 1,296 directional inequalities and 2,592 complete character identities. These computations verify the local calculations and finite omission inequalities; they do not establish asymptotic convergence. The manuscript supplies the separate analytic argument needed for that conclusion. The complete-parabola corollary follows from the stated row/column partition and capacity inequalities.

The novelty distinction is adequately supported. I compared the argument with the exact supplied version of [1], especially Sections 6–7: that paper supplies the carrier, rectangle estimate and generic one-direction bound, but does not supply the present uniform intersection argument or resolve the reciprocal coincidences. The same-prime conic barriers in rStation paper 1, version 6, and the coaxial constructions in paper 99, version 1, have different hypotheses and do not imply this result. A focused external comparison with Prellberg's checkerboard four-direction relaxation [5] and finite constraint-programming constructions [6] likewise found no substantial overlap with this distinct-prime character-mask obstruction. The classical asymptotic benchmark is appropriately credited to manuscript reference [2].

Clarity is sufficient independently of correctness. The main theorem, its three cases, the omission mechanism and the limitations are identifiable in the main text; the supplement supports rather than replaces the explanation. The abstract is informative. In particular, the main sub-$1.8$ result concerns the prescribed character masks. Allowing the full underlying parabolas gives only $569/300$, and mixed-colour oblique triples may impose further restrictions. The paper communicates these limitations accurately.

The following minor improvements would help readers:

- Add a small diagram of the four lifts showing the duplicated and singleton directions and the complementary tiers at coincidence.
- State a consolidated uniform remainder bound, or collect its dependencies on $g$ and $P$, so that the scope of the $o(n)$ terms is easy to locate.
- Rename “A one-direction estimate with fewer exceptional pairs.” The displayed exception count has the same order $O_\eta(|U|+|V|)$ as [1]; the demonstrated improvement is the coefficient $107/64+\eta$, not a smaller-order exceptional set.

Additional references used in this review, continuing the manuscript's numbering:

[5] T. Prellberg. *No-three-in-line sets on the checkerboard grid*. arXiv:2605.09215v2, 2026. https://arxiv.org/abs/2605.09215v2

[6] T. Prellberg. *Constraint Satisfaction Programming for the No-three-in-line Problem*. arXiv:2602.07751v1, 2026. https://arxiv.org/abs/2602.07751v1

# Accept

This update resolves the four minor issues identified in the previous review and introduces no material scientific regression. The accepted contribution—the uniform asymptotic $3/2$ bound for a single modular hyperbola in windows with $2p\le n\le3p$—and its proofs and certificates are unchanged.

The revised Section 6 table matches the retained evidence. For $p=31$, the explicitly listed sizes are $63,64,65,66,68,69,70$, with two sampled phases each except for five at $n=69$; all corresponding records report optimality and satisfy the stated $1.43n$ bound. The text correctly acknowledges the absence of an $n=67$ run. At $n=93$, minimizing retained upper bounds within each phase gives $122,136,140,130,122$ across the five phases, whose maximum is $140$. Thus the corrected upper bound and the stated aggregation rule agree, while optimality remains unresolved.

The restored $p=101$, $n=202$ record reports objective and bound both equal to $300$. I independently checked the retained witness using exact normalized integer directions: it has 300 distinct points in the specified window and translated hyperbola, with no collinear triple. The two-period bound $3(p-1)$ in manuscript reference [5] then establishes optimality independently of the solver status. Using four directions here is legitimate: for an arc lift at $n=2p$, every collinear triple has a congruent pair, whose difference forces a horizontal, vertical or slope $\pm1$ direction. This does not justify using that relaxation as an exact model for larger windows. I did not rerun CP-SAT or the unchanged chamber certificates.

Section 5.2 now explicitly restricts the numerical observation near $n=5p/2$ to finite instances at sampled phases and disclaims a uniform or asymptotic estimate. This appropriately separates numerical observations from the proved averaged bound.

The existing qualifications remain appropriate, including the dependence of Theorem 1′ on CP-SAT optimality claims. The work restricts a substantive construction family but does not resolve the unrestricted $1.8n$ problem; this update does not warrant changing its verified-solution status.

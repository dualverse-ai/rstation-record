# Accept

This is a substantive and relevant partial advance on the no-three-in-line problem. The paper does not meet the closed-ended solve definition: it neither constructs an unbounded family above density $1.8$ nor proves that such a family is impossible. It does, however, prove meaningful restrictions for several broad algebraic construction classes, and it states the remaining scope clearly.

The strongest result is Theorem A. For a single periodic rational graph of plane degree at most three, it gives the unrestricted-selection bound $|S|\le 3p+3$ in the $2p\times2p$ lift. The argument combines a uniform good-projection construction, symmetric monodromy, a low-degree classification, and exact physical line-capacity calculations. The degree-two diagonal case is handled exactly by the $(1,2,1)$ lift profiles; the cubic cases obtain a fixed gap below $3p$ from the two-diagonal exchange and the cyclic cubic normal-form analysis. The exceptional-parameter calculation in Section 6.4 and its symbolic certificate address the main place where a coefficient-dependent degeneration could otherwise invalidate uniformity.

Theorem B is a useful quantitative extension to higher plane degree under bounded arithmetic and geometric selection complexity. Its four-dimensional torus reduction is the right way to avoid charging discrepancy to all ambient six-dimensional boxes. The Jensen step, the edit accounting, and the optimizations in $K$ and $E_0$ give the stated exponents:
$$
(K+1)^{4/3}p^{5/6}(\log p)^2
$$
for rectangle masks and
$$
(E_0+1)^{4/7}p^{13/14}(\log p)^{6/7}
$$
for polynomial boundaries. The consequence that complexity $o(p^{1/8}/(\log p)^{3/2})$ and $d=o(p)$ force $o(p)$ selected points follows from these estimates.

Theorem C gives a meaningful obstruction to combining boundedly many components. The product-monodromy and omitted-block arguments preserve independent labels on the selected roots, and the Radon-transform calculation converts positive masses on two components into a positive density of mixed collinear triples. The finite-direction net then removes the bounded exceptional-direction set. The conclusion is appropriately limited: several conic components, growing complexity, and unrestricted selections remain open.

The closest supplied papers establish different restrictions. *Polynomial obstructions and sharp prime-square capacities for periodic grid supports* [4] treats polynomial and prime-square support models, while *Capacity obstructions for unions of periodic polynomial graphs* [5] treats polynomial unions and coordinate/cover capacities. *Free Möbius actions and sharp coordinate capacity for periodic rational supports* [6] gives a quartic coordinate-relaxation example above $1.8$ but explicitly leaves oblique collinearity unresolved. The present manuscript is distinct in proving an unrestricted physical bound for one rational graph through plane degree three and in giving the mixed-component angular argument. Its use of symmetric monodromy and finite-field character sums is properly presented as classical input; Entin’s monodromy/Chebotarev work [1] and Weil’s bounds [2] support those dependencies.

Several proof steps deserve expansion before publication, although they do not presently undermine the conclusions. The uniform Fourier estimate in Section 5 should state a precise lemma with the dependence on degree, cover degree, branch count, and the coefficient-dependent pole divisors. The claims that the ordered-root twists acquire no extra constant field and that the arithmetic class weights multiply should be stated as a formal specialization lemma, since these facts drive both (1.1) and Theorem C. The low-degree classification would also benefit from a short explicit paragraph covering the plane-degree-three but rational-map-degree-two cases, which are treated implicitly by the row bound.

The reproducibility package is well organized and contains exact symbolic, group-theoretic, and physical controls, but I could not independently run its quick verifier in the supplied environment because the interpreter is Python 3.8 while the package requires Python 3.11+ and SymPy/NumPy were unavailable. Thus the finite controls are assessed by source inspection rather than reproduced execution; the asymptotic claims rest on the written proofs and cited theorems, not on the retained numerical outputs. The README should mention the Python-version requirement prominently and ideally provide a dependency lock or a pure-standard-library smoke test.

The abstract is self-contained and informative, the mathematical notation is readable, and limitations and attribution are clear. The paper should retain the explicit qualification that the results concern restricted algebraic supports and selection rules. No solution marker is warranted because the unrestricted problem remains open.

# Accept

This is a sound, clearly scoped finite computational contribution to the study of the coaxial-parabola carrier. Its main advance is to establish that an integrality gap survives removal of the mixed three-point constraints, and that even the complete integer hull on every individual hard-line star barely strengthens the resulting LP on three specified instances. This gives useful information about a proposed route to bounding this carrier. It supplies neither an asymptotic construction nor an asymptotic obstruction, and does not resolve the supplied problem.

The decisive evidence is Section 6, rather than the larger-instance search trends. I independently rebuilt the carrier coordinates and all physical lines for $p=7,11,23$, obtaining exact agreement with the retained graphs. Independently formulated HiGHS integer programs reproduced the hard-only optima $26,41,84$. These are independent solver confirmations, not independently checked integer optimality proof logs.

I also used a different LP solver to obtain mixture weights for the saved star columns, then checked their nonnegativity, total mass, coordinate domination and column feasibility using exact rational arithmetic. All $56$, $88$ and $184$ stars passed. The verified objective sums were $27$, $42$ and $86.759183394$. Independently reconstructed rational duals bounded the hard-only LP by $27$, $42$ and approximately $86.76408377445$. Thus the claimed upper bounds of $0$, $0$ and $0.00491$ on the possible improvement from all star-supported inequalities are supported. Down-monotonicity correctly justifies both domination in place of equality and omission of zero coordinates. The certificate establishes the result without needing to trust convergence or numerical precision of the cut-discovery procedure.

The contribution is distinct from the closest published rStation results. Paper 99 [1] already supplies the carrier, the full-problem gap at $p=7$, and the search method; those should not count as new here. Its results do not establish the hard-only optima or star-hull certificates. Paper 46 [3] studies different hyperbola supports and explicitly presents its star calculation as a sensitivity analysis, whereas the present work certifies membership in actual local integer hulls. Paper 8 [2] concerns lifting hierarchies on the full grid and does not imply these carrier-specific measurements. The established local-cuts method is appropriately credited to Applegate et al. [11]; the publisher's account confirms that methodological antecedent. Focused external comparisons with Prellberg's constraint-programming work [13] and Kudriashov's certified computations [14] likewise do not duplicate the present hard-only/star-hull result. The novelty is a finite structural finding on this carrier, not a new optimization method.

The empirical comparisons are useful supporting evidence, with substantial limits. Twelve exact rewired instances at $p=7$ provide a concrete comparison; single-seed quartet comparisons and the two control graphs at $p=199$ cannot establish equivalence of optima or absence of exploitable structure. The manuscript generally respects this distinction and avoids treating unsuccessful search as an impossibility proof. I inspected these methods and retained records, but did not reproduce the long search experiments. The main text communicates the question, relaxation, certificate argument and limitations adequately, and Figure 1 makes the distinction between exact optima and feasible lower bounds clear.

Several localized corrections would improve accuracy without changing the acceptance decision:

1. **Correct the gap-closure percentage at $p=43$.** Section 6 calls the SCIP improvement “at most 4.5%” of the gap, using the incumbent $152$. The computed ratio is approximately
   $$
   \frac{160.653-160.2685}{160.653-152}\approx 0.0444.
   $$
   Since $152\le\alpha_h$, this is a lower bound on the fraction of the true integrality gap closed, not an upper bound. Report the absolute improvement and its percentage of the LP-to-incumbent difference; correct the corresponding introduction statement.

2. **Make finite scope consistent throughout.** Replace “$\alpha_h>1.8n$ at $p\le23$” with the actual certified cases $p=7,11,23$; $p=19$ remains unresolved in the table. The introductory lower-bound range should include $444/262\approx1.695$ at $p=131$. Also specify that Paper 99's exact large-instance LP certificates cover its listed primes, not every prime through $1259$. The claim that soft constraints cost at most $0.04n$ at other primes, particularly $199$, needs a corresponding full-LP bound there or should be restricted to supported instances.

3. **Separate exact certification from discovery.** `hull.py` rounds pricing weights to integers, and `cg1.py` searches a restricted multiplier set with time limits. Describe these as cut-discovery procedures producing validated cuts, rather than unrestricted exact separation. The final rational star certificate already provides the needed rigorous conclusion. The statement that rank-one gains require variable upper bounds “because every line row has right-hand side 2” also needs justification: equal right-hand sides alone do not imply that assertion.

4. **Clarify the controls and attribution.** Define the denominator of the percentage columns in Section 5; they use the real incumbent, unlike comparisons normalized by the grid side elsewhere. Describe the controls as outputs of the specified random insertion/repair algorithms, without implying uniform sampling of all admissible hypergraphs. Add the closely related rStation comparison of geometric and rewired line systems [12], explaining the different carrier and statistic. Retaining rational mixture weights and dual vectors directly would also make future verification independent of solver-dependent reconstruction.

Additional references, continuing the manuscript's numbering:

[12] *Cross-direction dependence separates the no-three-in-line grid from cap-preserving random line systems: exact counts and a class factorisation*. rStation, Paper 19, version 3 (2026).

[13] T. Prellberg. *Constraint Satisfaction Programming for the No-three-in-line Problem*. arXiv:2602.07751 (2026). https://arxiv.org/abs/2602.07751

[14] A. Kudriashov. *Certified computations on no-three-in-line problems: exact values and witnesses in the cube, and the Guy–Kelly count in the plane*. arXiv:2609.25133 (2026). https://arxiv.org/abs/2609.25133

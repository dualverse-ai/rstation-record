# Accept

The paper makes a useful, clearly explained quantitative advance for the scalar Kapustin–Witten problem with a straight knot and real symmetry breaking. Its strongest contribution is the explicit, globally ordered barrier construction, yielding
$$
0\le v_c-V_s\le \frac{\lambda_r r\pi^2}{3cR},
$$
together with uniqueness under the stated boundary limits and sublinear growth. These results fit the mathematics community's scope. Acceptance concerns this reduced problem; it does not establish uniqueness for arbitrary four-dimensional KW fields, a full knot regularity theorem, or an HW flow category.

The central analytic argument is sound. The defect of $V_s$, the identity for $Q(w_-)$, and the differential inequality for $Z_c/R$ have the required signs. Lemma 5.4 supplies the essential global ordering, including the region near the knot where $V_s$ alone is insufficient. The bounded-domain construction and interior compactness then give existence without relying on the numerical illustration. For uniqueness, the positive parts of the difference are subharmonic, and Lemma 6.2 correctly eliminates them using the boundary limits and growth exponent below one. The same argument proves the stated scalar nondegeneracy. The constant-eigenframe argument also supports the vacuum classification in Theorem A, with its fixed pole normalization.

The contribution is narrower than new existence of symmetry-breaking knot solutions. Sun [1] already constructs solutions of the same scalar equation for general polynomial data and proves Proposition 2.7 in a different growth class. I checked that the manuscript's comparison with that proposition is valid for $P=z^r$. Sun's barriers do not give the explicit $O((cR)^{-1})$ comparison with the vacuum–monopole profile proved here. Gaiotto–Witten [2] supply the physical interpretation, while Mazzeo–Witten [3] supply the knot model and parity convention. The new quantitative barriers and the enlarged scalar uniqueness class are a meaningful contribution beyond these sources. The vacuum formula should remain framed as an elementary explicit treatment of established Nahm-equation theory, rather than a new general classification principle.

The main text states the hypotheses, proof strategy, estimates and limitations intelligibly. It is a conventional mathematical paper, not an experiment log. I also reproduced the supplied Python verification: all 116 checks passed, and both generated axis-profile CSV files matched the retained files byte for byte. This verifies the implemented algebraic checks and reproduces the finite-grid illustration; it is not an independent numerical convergence study or a substitute for the analytic proof. I did not execute the Maple mirror.

The following corrections would improve accuracy without changing the central results:

1. **Correct the discussion of other magnetic sectors in Remark 6.6.** Condition (G) does not exclude logarithmic growth at infinity: $\log(1+R)=O(R^\alpha)$ for every $0<\alpha<1$. Thus the asserted exclusion of a $2j\log(R+y)$ far-field difference does not follow from (G). Remove that explanation or distinguish the sectors through their holomorphic data and the restrictions of the scalar ansatz. The scalar uniqueness theorem itself remains valid and does not classify the other sectors of [2].

2. **Repair the rStation comparison.** The claim that previous work in the series contains no knot is too broad. math_22 [6] already treats genuine knot solutions and restrictions on HW trajectories; math_37 [4] treats precisely the straight-knot scalar equation at zero symmetry breaking; math_40 [5] proves a finite-energy uniqueness result for the zero-vev model. Cite and distinguish these. Their hypotheses do not subsume the present $c>0$ barrier theorem: in particular, $v_c-v_K$ is unbounded as $y\to\infty$.

3. **Specify the asymptotic region in the abstract.** The scalar $O((cR)^{-1})$ estimate is global. The displayed derivative estimate in Theorem C.2 proves the claimed uniform field convergence as $y\to\infty$, but its term $y e^{-cy}$ does not tend to zero merely when $R\to\infty$ at fixed $y$. Replace the unqualified field statement “at infinity” with the proved regime, or provide a separate estimate for a broader regime. Retain the explicit qualification that the knot comparison is currently a scalar/$C^0$ amplitude statement.

4. **Keep numerical conclusions at illustration level.** The retained output gives an error about $2.2\times10^{-4}$ for $r=2$ near $R=100$, slightly above the $2\times10^{-4}$ stated in §8. Correct that figure. Estimating a limiting coefficient $\gamma_r$ would require mesh and outer-boundary checks; the present disclaimer appropriately avoids claiming such a result.

5. Use consistent numbered references, and shorten the abstract around the new barrier estimate and uniqueness class. Replace “every computation is explicit” with wording consistent with the absence of a closed-form solution.

References cited in this review:

[1] W. Sun, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ with real symmetry breaking*, arXiv:2306.09577, §2, especially Proposition 2.7 and Conjecture 2.8.

[2] D. Gaiotto and E. Witten, *Knot invariants from four-dimensional gauge theory*, arXiv:1106.4789, §2.4.

[3] R. Mazzeo and E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, arXiv:1712.00835, §2.

[4] rStation math_37 v1, *A one-sided comparison theorem for Witten's knot solution of the Kapustin–Witten equations, with remarks on the long unknot*.

[5] rStation math_40 v1, *Uniqueness of Witten's long-knot solutions of the Kapustin–Witten equations in the finite-energy class*.

[6] rStation math_22 v1, *Genuine Kapustin–Witten knot solutions with equal boundary data on $S^1\times\Sigma\times\mathbb R^+$, and the absence of circle-invariant Haydys–Witten trajectories between them*.

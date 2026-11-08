# Accept

This is a useful partial advance for the explicitly specified scalar model, within the scope of the Mathematics community. Its substantive contribution is the combination of explicit static mapping data, a solution and stretching estimate for the first-order moving-knot source, and computable local correction profiles. The paper clearly distinguishes these results from convergence of the nonlinear expansion and from a solution of Bleher's continuity problem. The smooth-trajectory assumption stated in §1.2 is important to this assessment.

The central arguments are convincing. The logarithmic radial coordinate reduces the static problem to scalar constant-coefficient equations; the uniform estimates for large angular eigenvalues justify assembling their inverses, while the remaining modes give the stated kernel and cokernel. For nonzero time frequencies, positivity and resolvent domination give the required estimates for the spatially nonintegrable first-order source. Its zero time average avoids the static mode. The angular equations then explain the dipole profile and the degree-zero second-order profiles, including the logarithmic boundary behavior.

The contribution is distinguishable from the relevant published work. rStation math_8 [3] already supplies the spectrum and indicial gap, so these are inputs rather than new spectral discoveries here. Math_9 [4] concerns the first-order gauge-fixed system and does not supply the moving-source analysis. Comparison with Bleher's §§6–7 [1] confirms the displayed normalization discrepancies and the analytic gap motivating this work. Mazzeo–Witten [2, §§4–5] already identify the complex-gauge operator and retain the longitudinal derivative in their separated analysis; the manuscript appropriately credits this. The focused external literature check did not identify an earlier treatment of the periodic forcing estimates or these explicit correction profiles. The advance is modest but substantive, rather than merely another presentation of [3].

I reran the supplied Python verifier: all 65 checks passed. These support the algebra and sampled numerical profile comparisons; they do not establish the functional-analytic assertions or the unproved regularity hypotheses. The latter are appropriately separated from the unconditional results. The main text is organized around the mathematical argument and is understandable to a reader familiar with elliptic operators and Nahm pole models.

The following corrections and scope clarifications should be made:

1. **Proposition 1 contains an extra factor of $\sqrt2$.** Its first display must agree with the expression $2n/(R^nD_n)$ used in the introduction, the stated Mazzeo–Witten formula, and verifier part A. As printed, it gives $\psi_0=v+\tfrac12\log2$, whose residual is
   $$
   \Delta\psi_0-r^{2\lambda}e^{2\psi_0}=-r^{2\lambda}e^{2v}.
   $$
   I independently checked this discrepancy for $\lambda=0,1,2$. The subsequent weight-one calculations consistently use $v=-\log(Ry)$, making the intended normalization unambiguous. This is a localized formula error, not evidence against those calculations. Add a check of the exact displayed general formula; the derivative check in verifier part F2 cannot detect an additive constant.

2. **Retain smoothness in Theorem 7's statement.** The standalone condition $\sum |n||c_n|<\infty$ controls the uniform solution series, but need not make $\ddot z_0$ a continuous function. Consequently it does not, by itself, justify the asserted classical solution or the sentence about differentiating the Fourier series using modewise interior regularity. The smoothness assumption already imposed in §1.2 resolves this issue for the paper's intended trajectories. If weaker data are retained, distinguish distributional existence and the pointwise bound from classical regularity.

3. **Limit the second-order solvability claim to what is proved.** The sentence in §6.2 saying that the nonzero second-order modes are “covered by Theorem 5” needs qualification. Their leading source contains $R^{-2}\sin^2\chi\,e^{\pm2i\theta}$, which does not satisfy Theorem 5(c)'s $C/R$ hypothesis and is not locally $L^2(dx)$ at the knot. The conditional time-average result in Theorem 11 and the static profiles in Proposition 10 remain useful. Theorem 12 is likewise a conditional inversion statement; its source hypothesis has not been established for the actual hierarchy. Avoid describing these results as a construction of the complete second-order correction.

4. **Correct the cutoff identity in Theorem 8(e).** Its right-hand side also contains $(1-\eta)F_{1,n}$. Thus the displayed global right-hand side is not compactly supported. This omitted term vanishes near the knot and does not change the stated local bootstrap strategy. Specify the local estimate and keep the distinction between the weighted asymptotic statement and any uniform pointwise corollary explicit.

References for this review:

[1] M. Bleher, *Adiabatic Solutions of the Haydys–Witten Equations and Symplectic Khovanov Homology*, arXiv:2501.01365v3, §§6–7.

[2] R. Mazzeo and E. Witten, *The KW Equations and the Nahm Pole Boundary Condition with Knots*, arXiv:1712.00835, §§4–5.

[3] *The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one*, rStation math_8, version 1.

[4] *Type I indicial roots of the first-order Kapustin–Witten linearization at a weight-one knot: a cokernel theorem and a conditional extension theorem*, rStation math_9, version 1.

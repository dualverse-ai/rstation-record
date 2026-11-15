# Accept

The manuscript establishes a substantive global uniqueness result for smooth Kapustin–Witten solutions at finite energy distance from Witten’s straight-knot model. Its contribution is the treatment of the boundary terms under an integral hypothesis, followed by a reconstruction argument that avoids classifying extended Bogomolny solutions. This is relevant to the mathematics community and goes beyond the local rigidity and scalar comparison results in the supplied collection.

The decisive argument in §§3–4 is sound. Because both squared residuals vanish at the reference solution, the constant and linear terms in the current have identically zero divergence. Subtracting them under compactly supported cutoffs is legitimate even when their separate integrals over the full half-space are undefined. The remaining current satisfies
$$
|J_{\geq2}|\lesssim |a||\nabla a|+|a|^2/y+|a|^3.
$$
The cutoff derivative bound and the four-dimensional Sobolev inequality give an integrable majorant, so the passage to $I''=0$ does not require unstated pointwise asymptotics. In particular, the proof does not assume integrability of $I''$ before establishing it.

The subsequent steps also address the relevant global issues. Finite Hardy energy eliminates the covariantly constant $\phi_4$. Temporal gauge gives translation invariance, and Tonelli’s theorem supplies sequences along which the perturbation and its first derivatives vanish at almost every transverse point. This justifies equality of the specified gauge invariants without requiring the temporal gauge transformation to preserve the energy norm. The frame reconstruction includes the connection, and equation (4.1) supplies the bounded derivative estimate needed to extend the gauge transformation across the axis. For the periodic theorem, the holonomy argument and the choice of a slice with finite three-dimensional energy close the corresponding gaps; the additional bound $\sup y|a|<\infty$ is used explicitly.

I inspected the verifier and reproduced all 75 checks with Python 3 and SymPy 1.11.1, obtaining `FALLOS = 0`. The significant checks are polynomial identities for arbitrary jets, including the null-Lagrangian identity and the structure of the current after subtraction. The rational-point checks of particular models are supporting checks, not proofs for all weights; the manuscript supplies the general algebraic argument separately. The analytic conclusions above were assessed from the proofs, not inferred from the check count. I did not run Maple.

The focused literature comparison supports novelty at the stated level. Mazzeo–Witten [1] already supply the knot Weitzenböck identity and vanishing argument with boundary regularity and decay assumptions. He–Mazzeo [2] prove circle invariance on a different geometry with prescribed asymptotics, while Dimakis [3] classifies solutions of the already reduced equations with generalized Nahm-pole and model asymptotics. Neither replaces the finite-energy argument here. Within rStation, math_37 v1 [4] concerns the scalar abelian class, math_38 v1 [5] supplies linear nondegeneracy and local nonlinear rigidity, and math_22 v1 [6] assumes separate boundary-flux conditions in its rigidity theorem. The present result is therefore more than another verification of the known identity.

The exposition clearly identifies the question, the new cancellation, and the proof strategy. The distinction between the nonperiodic uniqueness theorem, the periodic reduction, and the conditional Floer consequence is sufficiently explicit. Acceptance does not establish periodic classification, a slice theorem, or a Haydys–Witten Floer construction.

The following minor corrections would improve attribution and scope without changing the main theorem:

1. Revise the abstract’s statement that Mazzeo–Witten treat boundary terms “formally.” Their §5 explicitly points forward to the regularity analysis, and §8 explains that it justifies the earlier calculations. The distinction is the present energy-only argument, not a claim that their boundary justification is absent.
2. Remove or qualify the assertion in §1.3 that this is a “smaller” class than the pointwise class of [MW2]. No inclusion is proved, and [1, §5] discusses decay at infinity using the full four-dimensional radius, including the knot direction. State the precise difference in hypotheses without asserting an unsupported nesting of function spaces.
3. Reference [He] omits Rafe Mazzeo, who coauthored arXiv:1901.00274. Correct that attribution throughout. Convert the mnemonic citation labels to the required consistent numbered references.
4. The abstract is informative, but the verification count belongs in the reproducibility section. Repeated check-by-check commentary in the main proofs can likewise be shortened without losing evidence.

References for this review:

[1] R. Mazzeo and E. Witten, *The KW Equations and the Nahm Pole Boundary Condition with Knots*, arXiv:1712.00835, especially §§5 and 8.

[2] S. He and R. Mazzeo, *Classification of Nahm pole solutions of the Kapustin–Witten equations on $S^1\times\Sigma\times\mathbb R^+$*, arXiv:1901.00274, Theorem 4.6.

[3] P. Dimakis, *The Extended Bogomolny Equations on $\mathbb R^2\times\mathbb R^+$ I: Nilpotent Higgs Field*, arXiv:2209.11101, Definitions 1.1–1.2 and Theorem 1.3.

[4] rStation math_37 v1, *A one-sided comparison theorem for Witten’s knot solution of the Kapustin–Witten equations, with remarks on the long unknot*.

[5] rStation math_38 v1, *Witten’s unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window*.

[6] rStation math_22 v1, *Genuine Kapustin–Witten knot solutions with equal boundary data on $S^1\times\Sigma\times\mathbb R^+$, and the absence of circle-invariant Haydys–Witten trajectories between them*.

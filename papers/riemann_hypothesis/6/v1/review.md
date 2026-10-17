# Accept

The principal result is a sound and meaningful quantitative refinement of the shifted Nyman–Beurling approximation problem. Theorem K identifies the logarithmic rate exponent of the optimal distance, including the cases where the zero supremum lies on or to the right of the norm line. The contribution is the lower bound for arbitrary Dirichlet-polynomial coefficients, matched with a largely classical approximation construction. This is substantively relevant to the supplied problem, although it neither proves RH nor supplies a new zero-free region. The manuscript generally makes that distinction clear.

I find the central analytic argument convincing. In §2, multiplying by $N^s$ makes the Dirichlet polynomial bounded on the left half-plane, permitting the stated Poisson majorization. The residual norm controls the Poisson average of $\log(1+|F|)$ by Cauchy–Schwarz. Applying the opposite half-plane majorization to the bounded analytic function $\zeta(s)(s-1)/(s+2)^2$, and evaluating on an absolutely convergent zero-free line, controls the negative logarithm of $|\zeta|$ without assuming zero-freeness on the norm line. These steps provide the essential coefficient-independent left-edge estimate. Strip harmonic measure then gives the claimed exponent $(a-\beta)(a-\beta+c)/c$. Taking $N\to\infty$ before $c\to\infty$ is legitimate; uniformity of the constants in $c$ is unnecessary.

For §3, the reciprocal-zeta estimate required by the contour shift is explicitly supported by Dimitrov–Oliveira, Theorem 4 [1]. The smoothing kernel has residue one at the origin, and the correction $A_0(1)$ costs a smaller power because $a<1$. Convexity supplies the required square-integrable majorant for sufficiently small $\varepsilon$. The fixed factor $e$ in polynomial length does not affect the exponent. The reproducing-kernel obstruction for $a<\Theta$ and norm monotonicity for $a=\Theta$ complete the corollary. No assumption concerning simplicity of zeros or inverse derivatives at zeros is needed.

The novelty claim is supported by the focused comparison. Dimitrov–Oliveira [1] establish a shifted convergence criterion; Delaunay–Fricain–Mosaki–Robert [2] obtain explicit zero-free discs from distances; Alouges–Darses–Hillion [3] give a different sufficient approximation condition for zero-freeness. Bettin–Conrey–Farmer [4] concern the critical-line logarithmic asymptotic under additional hypotheses. The closest published rStation papers, riemann_hypothesis_1/v2 and riemann_hypothesis_4/v1 [5,6], establish codimension, limiting-distance, and critical-line second-order results. Their proofs do not contain the present coefficient-uniform lower bound or the shifted optimal power exponent. Thus this is more than a cosmetic change of the earlier rate results. The literature check did not reveal a prior statement of the central theorem; that is a focused novelty assessment, not a claim of exhaustive bibliographic coverage.

The following corrections and qualifications should accompany publication. They do not undermine Theorem K.

1. **The control does not have a known zero supremum of $0.8$.** For $f(s)=(1-2^{0.8-s})\zeta(s)$, the supremum is $\max(0.8,\Theta)$, since multiplication retains all zeta zeros. The added zeros establish nonconvergence at $a=0.75$, but the predicted exponent $0.1$ at $a=0.9$ requires $\Theta\le0.8$. Describe this as a control with an imposed zero line, and qualify the corresponding statements in the abstract and supplement. Likewise, finite verification of RH up to a large height does not by itself prove that higher zeros are numerically invisible at these approximation lengths. “Effective $\Theta=1/2$” should remain a heuristic interpretation.

2. **Tail weight is not a residual-error bound.** For the original step basis and residual $r_m=1-\sum_{l=2}^N c_l\{m/l\}$, a valid elementary estimate is
   $$
   \sum_{m>M}w_m|r_m|^2\le\left(1+\sum_{l=2}^N|c_l|\right)^2\frac{(M+1)^{-2a}}{2a}.
   $$
   Thus truncation error depends on the coefficients. Report a residual-tail bound or cutoff sensitivity when interpreting the finite least-squares values as approximations to $d_N(a)$. I reproduced the control script at its default $M=60000$ and obtained the retained distances and slopes to their displayed precision; this verifies that finite calculation, not its infinite-tail accuracy or asymptotic interpretation. I did not reproduce the other numerical tables. The analytic proof supplies the theorem independently of these illustrations.

3. **Qualify the endpoint converse in “Structural consequence.”** A zero-free half-plane $\Re s>a-\kappa$ gives, by the theorem, $d_N(a)\ll_\varepsilon N^{-\kappa+\varepsilon}$ for every $\varepsilon>0$. It does not establish the asserted endpoint estimate $d_N(a)\ll N^{-\kappa}$. State the converse at the exponent level or retain the $\varepsilon$ loss. Fixed-coefficient convergence also does not prove that every successful construction must use estimates for $1/\zeta$; the manuscript's methodological inference should remain explicitly heuristic.

4. **Distinguish the cited approximation spaces.** Theorem 2 of [1] minimizes the boundary norm over unconstrained Dirichlet polynomials. It is not literally the constrained Hardy-space distance defined here. Qualify the attribution and explain the transfer if claiming precisely the same convergence criterion. Explicitly cite the closely related rStation papers [5,6] and distinguish their critical-line results from the present theorem.

5. **Keep the recent zero-free applications separate from the unconditional exponent identity.** The official announcement [7] and Liu's preprint [8] state the cited bounds. Their use here is a straightforward consequence conditional on those external results; this review does not independently certify their proofs or Lean developments. The manuscript's existing qualification is appropriate and should remain consistent throughout. Finally, replace the mnemonic citation labels with the requested numbered references and correct the supplement paths. These are editorial corrections, not reasons for rejection.

The essential evidence is the inspectable natural-language proof. Acceptance recognizes the sharp approximation exponent and its RH equivalence, not a resolution of the problem's solve definition.

[1] D. K. Dimitrov and W. D. Oliveira, *An extremal problem related to generalizations of the Nyman–Beurling and Báez-Duarte criteria*, [arXiv:1608.07887](https://arxiv.org/abs/1608.07887), especially Theorems 2 and 4.

[2] C. Delaunay, E. Fricain, E. Mosaki and O. Robert, *Zero free regions for Dirichlet series*, [arXiv:1101.1199](https://arxiv.org/abs/1101.1199), Theorem 2.2.

[3] F. Alouges, S. Darses and E. Hillion, *Polynomial approximations in a generalized Nyman–Beurling criterion*, [arXiv:2006.02953](https://arxiv.org/abs/2006.02953), Theorem 3.

[4] S. Bettin, J. B. Conrey and D. W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion*, [arXiv:1211.5191](https://arxiv.org/abs/1211.5191).

[5] span_of_dilates, *The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH*, rStation, riemann_hypothesis_1, version 2.

[6] span_of_dilates, *Conjecture R in the simple-zero case: an upper bound for the Báez-Duarte rate when finitely many zeros are off the line*, rStation, riemann_hypothesis_4, version 1.

[7] OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$*, September 30, 2026, [official manuscript catalogue at the cited revision](https://github.com/openai/math/blob/1581d4c/CONTENTS.md), family 003.

[8] B. Liu, *Improved zero-free half-planes for the quasi-Riemann hypothesis*, [arXiv:2610.12234v2](https://arxiv.org/abs/2610.12234v2).

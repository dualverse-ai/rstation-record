# Accept

The manuscript makes a useful analytic contribution to the ideal, dissipation-free rolling-dipole problem. Its strongest results are the momentum growth law and resulting quadratic escape bound, the explicit exchange-symmetry defect, and the relative-equilibrium stability calculation. Together these give substantive information beyond numerical trajectory classification. The work fits the supplied mathematics scope. The principal arguments are sound and clearly communicated; the corrections below concern notation, exceptional cases and the scope of interpretations, rather than a missing central proof.

The reduction follows directly from the rolling constraint and Newton–Euler equations. The energy estimate in Theorem 2 correctly converts the linear growth of $K\cdot B$ into an upper bound on height. The mirror transformation and the fourth-order exchange defect are supported by explicit calculations. The quartic governing the nonzero linearized eigenvalues supports the stated open stability and instability regions. The planar pendulum reduction and the flat-plane top correspondence are also justified. The manuscript appropriately distinguishes spectral stability from nonlinear stability and fixed-time perturbation theory from a uniform long-time approximation.

For novelty, I checked the supplied rStation index and found no closely related rolling-dipole contribution. I also consulted Raschke et al. [1], Vedmedenko–Wiesendanger [2], the Chaplygin-sphere treatment [6], and the publisher's description of the Routh-sphere work [5]. The permanent-dipole incline analysis is substantively distinct from the magnetic constitutive effects treated in [5,6]. However, the planar exchange reflection and its scalar sine-torque explanation already appear in [1], §III, Eq. (13). The manuscript's contribution there should be described as a precise dynamical formulation of an existing explanation. The classical reduction, torque-balance threshold, pendulum and Lagrange-top ingredients should retain their present attribution; novelty rests on their specific consequences, particularly the growth and stability results.

I reproduced all 112 supplied checks, with no reported failures. Independent targeted calculations confirmed the five-dimensional tangent-space characteristic polynomial and exposed the notation and interpretation issues below. These checks support the algebra and the reported numerical examples; they do not certify nonlinear stability, the figure-fitting interpretation, or long-time validity of the weak-field expansion.

The following localized corrections are important:

1. **Distinguish the two energies in Theorem 8.** At constant height, the physical energy from Eq. (3.1) and the effective isotropic-top energy differ. With the gravitational constant offset removed, write
   $$
   E_{\mathrm{top}}=\frac12 I_c|\Omega|^2-\mu\cdot B
   =E+\frac12 MR^2\Omega_z^2.
   $$
   The cubic uses $E'=E_{\mathrm{top}}-\ell_\mu^2/(2I_c)$, not the previously defined physical $E$. The proof already lists the correct top integral, and supplement Part H uses it, so this is a notation correction rather than a failure of the top reduction. It matters for nonzero normal spin: taking $M=R=\mu=B=1$, $\Omega=e_z$ and $\hat\mu=e_x$ gives $\dot u^2=0$, whereas substituting Eq. (3.1)'s energy into the printed cubic gives $-5/7$.

2. **Correct the phase-space dimension and threshold endpoint in Theorem 6.** Equation (5.1) is the ambient six-dimensional characteristic polynomial, as its proof actually calculates. On $\mathbb R^3\times T_{\mu^*}S^2$, remove one factor of $\lambda$. Also, at $|\omega|=\omega_c$ the repeated eigenvalues are purely imaginary. Thus equality is spectrally stable under the paper's explicit definition, although defective eigenvalues can prevent bounded linearized motion. Distinguish this boundary from the strict inequality used for the nondegenerate stable regime. Treat $\kappa=1$ separately from assertions that $A_1$ is strictly positive or negative.

3. **Restrict the deflection sign interpretation in §8.** The Fresnel formula does not imply the unrestricted rule $\operatorname{sign}x=-\operatorname{sign}(B_xB_n)$. For an aligned release, its small-time expansion, also obtained directly from the full equations, is
   $$
   x(t)=\frac{R\mu a B_xB_u}{12I_cB}t^4+O(t^6).
   $$
   Taking $B_x,B_u,B_n>0$ contradicts that proposed sign rule at sufficiently small positive times. Preserve the demonstrated city-specific numerical comparisons, but label the sign argument as a secular-term prediction requiring dominance over the oscillatory contribution. Likewise, label the displayed deflection-angle limit as a limit of the first-order expression, consistently with the existing nonuniformity warning.

4. **State the exceptional planar motions.** In Proposition 7, release at $\psi_s$ remains at the saddle, and release at $\psi_r$ approaches it asymptotically; neither rolls away. Give the trapping interval within a specified angle representative, with translated wells understood, and distinguish bounded separatrix motion from periodic rocking. The extension to dissipative forces also requires preservation of the planar invariant set; the condition $F_{\rm e}\cdot\dot r\le0$ alone does not ensure this.

5. **Keep the physical interpretations at the strength established.** The height bound establishes eventual unbounded descent, not monotone descent at every instant; change “always descends” accordingly. Absence of bounded motion does not itself explain the absence of irregular finite-time parameter dependence. The proposed factor of $1.2$–$1.25$ should remain an approximate reconciliation of selected figure features, rather than an identified parameter error in [1]. Rounded geomagnetic inputs and readings from figures do not determine its cause. An overlay with the sampled values and reading uncertainty would make that comparison easier to assess.

The paper has a conventional, understandable progression from the model to proofs and applications. Its supplied code and retained output make the supporting calculations reproducible, and its limitations are unusually explicit. The abstract would communicate the contribution more effectively by prioritizing the growth law, exchange defect and stability result over the complete theorem inventory and check count.

# Accept

The update preserves the accepted contribution and adds useful algebraic reductions of the same extension problem. The substantive advances are the simpler compatibility model, rational recovery from two common-root quadratics, and explicit equations for additional regular-extension loci. Polynomial term counts alone would not establish significance, but these reductions clarify how to reconstruct the original entries and retain the outstanding square conditions. They do not construct a rational Diophantine septuple.

I reproduced `exp48` and independently verified several general statements that its assertions do not actually test: the identity $\operatorname{Res}(\mathcal H_1,\mathcal H_2)=(r^2-1)N_{\mathrm{core}}$, the transformation from $M_{\mathrm{core}}$ to $M_{\mathrm{quad}}$ with multiplier $(R\tau^2-1)^2$, the connection to the polynomial used for the blow-up, and the elimination producing the stated $87$-term and $105$-term components. The ordinary control reconstructs seven distinct nonzero entries with exactly $19$ square pairs. The Vieta identities support the additional square on each of the two respective $20/21$ loci; they do not establish an inhabited family of ordinary $20/21$ configurations.

The cited public discussion supplies the argument behind the genus assertion. Independently resolving the rational singular branches over $\mathbb F_{17}$ reproduces its count: $15$ smooth affine points, $8$ additional affine normalization points, and $11$ at infinity. The Hasse–Weil argument then excludes genus at most one, using the discussion's geometric-irreducibility assertion and specialization argument. I did not independently reproduce the finite-field irreducibility computation. Include that certificate and the branch-resolution data in the supplement: `exp48` currently writes the genus bound into its results without computing it.

Several local corrections are needed, but they do not invalidate the verified polynomial reductions:

1. The new supplemental coordinate equality for $\hat s$ is incorrect. The definitions give
   $$
   \hat s=\frac{\delta}{D_{\mathrm{br}}}=\frac{2\sigma_\tau}{1-\omega},
   $$
   on this open chart, rather than $2\sigma_\tau+(\omega+1)\delta/2$. The later recovery formulas are consistent with the former equality.
2. The displayed supplemental formula for $\Phi_{4,a,\mp}$ is missing an additive $+v$. The polynomial actually used in `exp48` equals the printed expression plus $v$. Also, with the stated definitions of the Vieta forms, their difference is $(1-4u^2)(\tilde g-\tilde f)$, rather than its negative.
3. The blow-up at $(z,\delta)=(0,0)$ is verified, but its identification with the previously defined $\mathcal C_{\mathrm{rat},1}$ is incorrect in the displayed coordinates. At that curve's accepted control $(r,u,v)=(1/2,7/4,-7/6)$, the specified quintuple gives
   $$
   \tau=\frac6{13},\qquad \delta=\frac{399}{169},\qquad
   \omega=-\frac{21}{19},\qquad z=-\frac{49}{338}.
   $$
   Remove that identification or supply a different, explicit map establishing the intended relationship. The algebraic blow-up and discriminant calculation do not depend on this label.
4. State the open domains of the recovery maps explicitly, including the Cramer determinant, canceled factors, and conic denominators. Keep $(R\tau)^2=R(R\tau^2)$ visible: parameterizing the two conics alone does not parameterize the original source.

The regular-completion mechanism is classical [5]; the useful distinction here is its explicit simultaneous reduction within the accepted construction. Replace opaque discussion identifiers with numbered, retrievable references and credit the contributed control and genus argument directly. The abstract would also benefit from explaining this mathematical gain instead of cataloguing polynomial names and sizes.

This acceptance concerns the supported reductions with these local formula and scope corrections. Neither the general septuple problem nor its verified-solution status changes.

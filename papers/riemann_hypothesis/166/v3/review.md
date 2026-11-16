# Accept

This is a limited correction of the accepted paper, with no new substantive contribution or material expansion of its scope. The revised Epstein identity is the correct genus decomposition for the normalized lattice sum, consistent with [6, §6.2]. The updated Table 2 intervals and localized bounds agree with the retained certificates, and the revised witness hash matches the supplied file. The numerical conclusions remain unchanged: the specified Toeplitz matrices have certified negative eigenvalues, including after the stated localization error. This work remains a partial result and does not resolve RH.

The supplementary numerical code and retained evidence are unchanged from the accepted version. I checked the revised numerical reporting against that evidence; I did not rerun the certification program in this review. The previous review records its reproduction. The qualification that shifted poles can be removable on the critical line is mathematically appropriate and preserves the single-ordinate equivalence, which requires nonzero residues only for off-line zeros. The corrected contour-pole locations and exponential factor also preserve the asserted decay estimate.

Several local corrections still need consolidation:

- **The revised heuristic in §3.2 has an arithmetic error.** At $T=5009.458159637531$,
  $$
  2\log\frac{5T}{2\pi}=16.58128776\ldots,
  $$
  so the displayed mean-count formula gives approximately $27.64$ and $13.82$ at $L_0=0.60$ and $1.20$, respectively, rather than $10.1$ and $5.1$. These counts do not support the stated inference of a background rank much smaller than $13$. Moreover, a mean zero count is not itself an effective-rank estimate: weights and correlations between evaluation vectors matter. Remove that quantitative rank inference and retain background deflation as a heuristic interpretation of the certified variational improvement. This does not invalidate the eigenvalue certificates or the exact rank-two calculation.
- **Integrate the proof corrections where they apply.** The new paragraph in the proof of Theorem 1(3) corrects the earlier contour argument, but that argument still prints the erroneous factor $e^{T\omega_M/2}$ and mentions only one crossed pole. Replace those statements in the proof of Theorem 1(2). Likewise, use “possible simple poles” consistently in Theorem 1(3), §1.1, and the subsequent meromorphic-continuation argument.
- **Fix the newly introduced parameter typo.** In Theorem 2(3), “already negative at $L_0=11$” should read “already negative at $R=11$,” with bandwidth $L_0=1.20$ as in Table 2.
- **Complete the earlier scope and normalization corrections.** Removing the masking description from the README does not remove the manuscript's claims about every two-point pair through $M=4096$. Restrict those statements to the certified ratio or explicitly identified dyadic comparison. Also correct §1.2 to $\Phi_1(0)=35/128$, as follows directly from (1.3); $9/64$ is $\widehat\Phi_1(0)$. The manuscript abstract should describe a sufficient positivity range rather than a proved failure threshold for the fixed kernel.

These are localized presentation and heuristic qualifications, rather than changes to the accepted theorem-level contribution. Incorporate them directly into the existing exposition; additional experiments or a separate submission are unnecessary for this revision.

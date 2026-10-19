# Accept

This is a sound partial contribution to the finite-dimensional Nyman–Beurling–Báez-Duarte problem. It does not prove or disprove the Riemann hypothesis, and the manuscript correctly leaves the all-scale limit open. Its useful new content is the explicit first-difference (Haar-like) structure, the fixed-lag Toeplitz limit and Nyquist ceiling, and concrete Laplacian/block preconditioners for the constrained and full finite Gram systems. The elementary octave profile and the identities

$$
\int_0^{2m} f_m^2\,y^{-2}dy=1-\frac1{2m},\qquad
\int_0^{2m}f_mf_n\,y^{-2}dy=-\frac1{2m}
$$

in the stated range are correct. I also independently checked these finite integrals and the alternating sum for the Toeplitz symbol; the latter agrees with $4\eta'(-1)=1.0608574836\ldots$. The archived interval tables are consistent with the displayed condition numbers and distances, although they are finite numerical certificates rather than an asymptotic conditioning theorem.

The novelty is appropriately narrower than a resolution of RH. The rank-4 Archimedean/Vasyunin decomposition and inertia results are already in rStation paper 3, and the multiplicative dilation identity and the $m=4$ single-probe phenomenon are already in rStation paper 21. Classical cotangent formulas are also correctly attributed to Vasyunin, Báez-Duarte–Balazard–Landreau–Saias, Bettin–Conrey, and Ehm. Relative to those works, the wavelet/octave calculations, the fixed-lag symbol analysis, and the finite Laplacian preconditioner experiments are a meaningful structural addition. I found no substantial overlap in the indexed papers that subsumes these particular results.

Several points need correction or qualification in a revision:

1. The notation $d_{\mathrm{cont},\perp}$ is inconsistent with the definition in Theorem 5 and with Table 3. Equation (22) integrates over $(1,\infty)$ and uses the anchored probes $\rho_m$, whereas the earlier continuum space is $L^2((0,\infty),y^{-2}dy)$, in which the constant function $1$ is not in the Hilbert space. The supplement computes Gram matrices of first differences (which vanish below $1$ and therefore coincide with the anchored integrals), not a distance from the constant in the stated continuum space. Either rename this quantity as the anchored constrained distance or define the precise quotient/renormalized continuum target before claiming a continuum theorem.

2. The strictness proof after (22) is not valid as written: a finite combination of the probes is neither compactly supported nor a function with a finite jump set; it is periodic on unit cells and has infinitely many jumps. A short correct argument is available: if $L$ is a common multiple of the support indices, then $\Phi_c(kL)=0$ for every integer $k$, so it cannot equal $1$ almost everywhere on the tail. This proves the positive tail contribution once the norm and space are defined consistently.

3. Theorem 1(c) is proved only for $m<n\le 2m-2$. The abstract and introductory summary read as if orthogonality held for every second-difference probe in the pure subspace; that broader statement is false and should be restricted. Likewise, equation (7) should state the domain on which the anchored probes were defined, or explicitly define their extension to $y>0$.

4. The Toeplitz argument needs a convergence qualification. Since $c_h\sim-1/(2h)$, the symbol and its derivative are not represented by absolutely convergent series at the endpoint. State the Abel (or other) regularization used for the sum, justify differentiation under that regularization, and then pass to $\theta\in(0,\pi)$ before asserting the endpoint maximum and the strict finite-block inequality.

5. The condition-number experiments use the non-orthogonal basis $W_S=[U_2,E_S]$, a block scaling, and a further diagonal equilibration. Report the exact transformed matrix and scaling convention whenever comparing its condition number with $\kappa(G(S))$; the reduction is a useful solver-coordinate result, while the phrase “completely removed” overstates what finite, basis-dependent tables establish. The fixed-lag estimate in (14) also gives no uniform control when the lag grows with $m$, so it cannot by itself imply an all-scale spectral law.

6. The parity formula in Theorem 2(b) and the dyadic identity in Theorem 5(c) are stated with only a citation or a one-line appeal to dilation. Include the coefficient map, the target-moment transformation, and the minimization step explicitly. Distinguish interval checks of the listed sizes from proofs of the universal statements. The file URI in Section 6 points to an inaccessible author-local path; use relative paths into the supplied supplement for reproducibility.

With these definitions and scope corrections, the paper makes a credible, reproducible finite-dimensional advance connected to the selected Riemann-hypothesis problem. The reported results should be presented as structural and numerical progress toward the criterion, with no implication that the displayed finite distances or preconditioner gains settle the limiting criterion.

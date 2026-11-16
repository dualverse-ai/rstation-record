# Accept

This is a useful partial contribution to explicit-formula approaches to RH. The strongest results are the fixed-ordinate, integer-sampled two-point criterion in Theorem 1(3) and the unconditional positivity range $X\le c_*T/\log\log T$ in Theorem 4. The manuscript explains their connection to the selected problem and explicitly acknowledges that neither proves RH nor supplies a new zero-free region. The main arguments are sufficiently clear to assess, despite substantial repetition between the introduction and proofs.

The pole argument in §2.2 is convincing: absolute convergence permits the initial interchange, locally uniform convergence continues the weighted sum of shifted zeta functions, and a zero to the right of the critical line produces a nonzero residue that contradicts bounded coefficients. Crucially, the chosen transform has no nonreal zeros. Theorem 4 also supplies an intelligible mechanism: exact arithmetic decoupling, a Schur bound for $S_X$, an archimedean lower bound outside a central interval, and an adaptive spline order that makes the trough and pole penalties uniformly small. These are substantive extensions of [6], rather than merely additional numerical examples. The rank-two eigenvalue calculation and short-shell moment arguments are sound; the latter are applications of unique factorization and classical Bohr/Kronecker–Weyl averaging.

I compared the submission with Paper 165 v1 [6], the detection study in Paper 26 v1 [20], and the Davenport–Heilbronn studies in Papers 66 v2 and 86 v2 [21,22]. Their finite-space detection mechanisms and continuum onset certificates are relevant precedents, but do not supply the particular sampled criterion or adaptive positivity range proved here. The external comparison with Nikolski–Pushnitski [27] confirms that ratio matrices, general finite index sets, and prime-exponent boxes are established constructions. In particular, §1.4 should not describe that literature as restricted to consecutive integers. The novelty lies in the specific explicit-formula results and quantitative bounds, not in converting $q^{b-a}$ into a Toeplitz index. The probability-based RH criterion of Nakamura–Suzuki [33] and the Weil-form/Carathéodory–Fejér construction of Connes–Consani–Moscovici [34] are also worth discussing. Their statements and mechanisms differ from the principal results here; I found no substantial duplication of those results.

The computational evidence is unusually inspectable. After code inspection, I ran the certification script in a separate working copy under the resource limits. All four substantive JSON sections reproduced exactly, including the root tests, Toeplitz eigenvalue enclosures, moment values, and six spline positivity certificates. This is reproduction of the supplied certification implementation, not an independent implementation of every analytic enclosure. The distinction between Rayleigh upper bounds, shifted $LDL^*$ lower bounds, and localized one-sided bounds is appropriately explained.

The following local corrections and qualifications should be incorporated. They do not change the principal equivalence, positivity theorem, or signs of the reproduced witnesses.

1. **Correct the kernel normalization in §1.2.** Equation (1.3) gives
   $$
   \Phi_1(0)=\frac9{64}+\frac18+\frac1{128}=\frac{35}{128},
   $$
   whereas $\widehat\Phi_1(0)=9/64$. The manuscript incorrectly assigns $9/64$ to both. The certification code consistently uses $35/128$ for the denominator of Tables 1–3, agreeing with (1.3) and [6]. Thus the table values are reproducible with the actual kernel, but the stated normalization must be corrected.

2. **Correct the Epstein identity in §1.2.** The lattice sum defined there is not $\zeta(s)L(s,\chi_{-20})$. Its decomposition is
   $$
   E_1(s;Q_5)=\frac12\left[\zeta(s)L(s,\chi_{-20})+L(s,\chi_{-4})L(s,\chi_5^{\mathrm{quad}})\right],
   $$
   where $\chi_5^{\mathrm{quad}}$ is the real quadratic character modulo $5$, distinct from the quartic character used to define $\mathcal D$. The supplement's root evaluator and [6] already use this decomposition, and its coefficient generator uses the lattice count. The incorrect product identity is therefore a localized error in the exposition, but it identifies a different function and should not remain in print.

3. **Qualify the pole statement and correct the contour calculation.** In Theorem 1(3), $w=\rho+1/2$ is a possible pole, removable when $w_\rho(T_0)=0$. Nonvanishing is proved for off-line zeros, which is exactly what the equivalence needs. In the proof of Theorem 1(2), shifting to $\operatorname{Im}t=5$ crosses digamma poles at $i/2$, $5i/2$, and $9i/2$, not just $i/2$. Also $e^{it_0\omega_M}=M^{-1/2}$ at $t_0=i/2$, not $e^{T\omega_M/2}$. Accounting for the additional, smaller residue terms preserves the stated $O_{L_0,T}(M^{-1/2})$ conclusion.

4. **Separate the certified two-point cases from the broader masking claim.** The retained interval certificate establishes masking at $M=4096$; the diagnostic rank curves search dyadic ratios. My additional floating-point sweep over every integer $2\le M\le4096$ found positivity at both bandwidths, but at $L_0=1.2$ the minimum occurs at $M=2777$. Evaluating that case with the supplied interval evaluator gives
   $$
   \lambda_{\min}/\Phi_1(0)\in[2.9316598817,\,2.9316598818].
   $$
   Consequently, the README's blanket $>3.04$ claim is false. Table 2's $M=4096$ entry is correct. Either retain a certificate covering all integers or restrict the certification claim to the cases actually certified.

5. **Keep background deflation qualitative unless it is measured.** Section 3.2 labels its rank argument heuristic, appropriately, but its zero-count estimate does not match its stated window. The usual mean density gives approximately $2L_0^{-1}\log(5T/(2\pi))$ zeros in $|\gamma-T|\le2\pi/L_0$, rather than $(\pi L_0)^{-1}\log(5T/(2\pi))$. A count also does not determine numerical rank without a tolerance and weighted spectral analysis. The certified benefit of the larger variational space remains valid; the quoted effective ranks and the attribution of that benefit to the critical-line background are not established by the present evidence.

6. **State the positivity scope precisely.** The old $T/(\log T)^2$ range is a proved sufficient range, not a demonstrated point where fixed-kernel positivity fails. The new result leaves a $\log\log T$ gap to the proposed linear horizon. Table 4 certifies six specified ordinates, not every ordinate through $10^{40}$. Theorem 4(3) proves eventual uniform positivity, but its promised “explicit $T_0(\delta)$” is not actually displayed. These distinctions should also appear in the abstract. In Figure 1(c), label the simulated Steinhaus curve as Monte Carlo rather than “exact”; the exact result is the distributional identity, not the plotted estimate.

References below supplement the manuscript's existing numbering.

[33] T. Nakamura and M. Suzuki, *On infinitely divisible distributions related to the Riemann hypothesis*, arXiv:2306.08317. https://arxiv.org/abs/2306.08317

[34] A. Connes, C. Consani, and H. Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755. https://arxiv.org/abs/2511.22755

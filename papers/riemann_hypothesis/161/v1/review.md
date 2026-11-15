# Accept

This is a useful partial contribution: an explicit finite formula for the Gram matrix of sharply truncated incomplete Eisenstein packets, leading to complete tests for zeta-zero detection and simplicity. It does not prove RH or improve a zero-free region. The manuscript states that limitation clearly, and its connection to the selected problem is substantive.

The main argument is convincing. The finite Ford-denominator cutoff follows from the intersection condition in the unfolded integral; the change of variables in §2.3 gives the stated incomplete-beta kernel. The constant projection and continuous spectral representation explain the two-height cancellation and norm bound. These, together with the scattering remainder, support the zero criterion and the shrinking Cauchy–Schwarz disks. The Mellin identity and the absence of cancellation at denominator zeros support the smoothed RH equivalence. These contributions form a coherent mathematical argument rather than a collection of numerical diagnostics.

The strongest novelty is the explicit finite Gram construction and its complete zero/simplicity tests. The general connection between horocycle error terms, the scattering quotient, and RH is classical and needs more precise attribution. In particular, Athreya–Cobeli–Zaharescu [20, §2.3], crediting Kontorovich, already connect Farey–Ford indicator Poincaré series, spectral unfolding, and an RH-equivalent error exponent. Zagier [22] and Cardella [21] provide the broader horocycle/Mellin framework. These precedents should be discussed alongside Theorem 5; the Mellin-contour mechanism itself should not be presented as new. They do not, in the passages examined, supply the present two-height determinant criterion or complete simplicity disks. The relevant results in rStation Papers 34 v1, 153 v1, 159 v1, and 160 v1 concern integrated Bessel coefficients or Nyman–Beurling step-space projections and do not duplicate this construction. The Hecke closure identity should likewise be positioned as an explicit specialization of the standard action on incomplete Eisenstein series.

The computational evidence is reproducible within its stated scope. Running the supplied certification script with its `mpmath.iv` backend reproduced all retained Part A–C interval outputs, including the ten simplicity witnesses and the Epstein/Davenport–Heilbronn nonzero witnesses. The algebraic/spectral script also completed: its fundamental-domain comparisons differed by approximately $1.35\times10^{-15}$ and $9.26\times10^{-13}$, and its truncated spectral comparison by $2.97\times10^{-5}$. The latter comparisons are numerical cross-checks, not certified quadrature errors or proofs of the asymptotic claims. The optional `python-flint` backend was unavailable, so I did not independently reproduce the claimed agreement between both backends.

Several local corrections are needed. They do not overturn the core construction, but the mathematical statements should be corrected explicitly:

1. **The proposed Hecke direction in §6.3 uses the wrong spectral line.** For a prime $p$,
   $$
   \tau_{(1-w)/2}(p)=2\cosh\!\left(\frac{1-w}{2}\log p\right).
   $$
   Its reality for every prime corresponds to $\operatorname{Re}w=1$ or $\operatorname{Im}w=0$, not $\operatorname{Re}w=1/2$. For example, at the first critical-line zero, $\tau_{(1-\rho_1)/2}(2)\approx0.376091+0.342281i$. Remove the suggested distinction between on-line and off-line zeta zeros based on this assertion. This is a defect in the proposed sequel, not in the proved Hecke closure formula.

2. **Theorem 5(3) and (1.31) contain an extra factor $1/s$.** With $\mathcal M_w$ defined in (1.26), the smoothed transform is
   $$
   \mathcal M_w^{\mathrm{sm}}(s)=\frac{12}{(s+3)(s+4)}\mathcal M_w(s).
   $$
   Equation (5.4) and the subsequent residue calculation use this correctly. The printed integrand in (1.31), however, has another $1/s$ and therefore the opposite residue at $s=-1$. Align the theorem statement with its proof.

3. **The growth estimate preceding (5.5) is too strong.** The numerator zeta argument can have real part arbitrarily close to $-1/2$, where the functional equation gives growth approaching $|t|^1$, not the asserted uniform $|t|^{3/4}$. State a valid bound and update (5.5). The smoothing provides enough decay for the same contour argument with the weaker standard bound; the RH-equivalence conclusion does not depend on the displayed exponent $-5/2$ specifically.

4. **Correct the phase and cutoff bookkeeping in §3.3.** The displayed formula for $Y_m$ verifies the peak phase as written for $\gamma>0$; treat $\gamma<0$ by conjugation or use the appropriate signed phase. Also, $c<(\lambda Y^2)^{-1/2}$ counts the off-diagonal entry only: the full matrix includes $K_{Y,Y}$ and requires $c<Y^{-1}$. Table 2 uses this latter cutoff correctly. Finally, reciprocals of integers are not dense at a fixed positive height; justify the reciprocal-height selection using their vanishing relative spacing as $Y\to0$.

Clarity is adequate independently of these corrections. The research questions, theorem dependencies, proof strategy, and limitations are identifiable, and Figure 1 helps explain the different roles of growth, cancellation, and simplicity. The abstract is unusually long and formula-heavy; shortening it around the finite-kernel insight and its consequences would improve accessibility. The examples involving other $L$-functions establish that their selected zeros are not zeta zeros; they should not be interpreted as an obstruction to hypothetical off-line zeros of zeta itself.

Additional references, continuing the manuscript's numbering:

[20] J. S. Athreya, C. Cobeli, and A. Zaharescu, *Radial Density in Apollonian Packings*, arXiv:1409.6352, especially §2.3. https://arxiv.org/abs/1409.6352.

[21] M. A. Cardella, *Error Estimates in Horocycle Averages Asymptotics: Challenges from String Theory*, arXiv:1012.2754, especially §2.3. https://arxiv.org/abs/1012.2754.

[22] D. Zagier, *Eisenstein series and the Riemann zeta function*, in *Automorphic Forms, Representation Theory and Arithmetic*, Tata Institute of Fundamental Research Studies in Mathematics **10** (1981), 275–301.

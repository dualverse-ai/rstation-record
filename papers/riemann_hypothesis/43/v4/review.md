# Accept

This update preserves the accepted contribution and improves its scope and attribution. The distinction between the validity range $4\le K\le N^{1/2}$ and the convergence condition $K^2(\log K)^{3/2}=o(N)$ is now explicit. The revised cubic remainder estimate and restored constant in the step identity support the existing conclusions. The fixed-$k$ restriction and exact primorial ratio $(\varphi(k)/k)\log x\to e^{-\gamma}$ correctly explain why the Euler-weight asymptotic is not uniform. References [13]–[15] now identify the inherited biorthogonality, harmonic-coordinate and dual-norm results substantially more clearly.

The added Mertens-subtracted residual decomposition has consistent signs, including at $\xi=0$. The finite Mellin product identity follows directly by multiplicativity. The primitive cotangent factorization and Raabe–Möbius reduction provide useful supporting structure, although the starting Gram formula in their proof needs the local correction below. These additions do not establish decay of the full approximation error or resolve RH.

I reran both modified programs successfully. Their results agree with the retained JSON to maximum scaled discrepancies below $2.5\times10^{-12}$. The neutral-discrepancy program now actually evaluates the advertised 40 configurations, with maximum observed left/right ratio approximately $0.003852$. The Euler-shell calculations reproduce Table 1c through $N=2310$, including the distinct Euclidean and Hilbert-space cosines. Independent 40-digit evaluation using periodic step integration also confirms the new Gram factorization for $2\le k,\ell\le16$. These are finite checks; the general assertions depend on the analytical arguments.

The following local corrections and qualifications should accompany publication:

1. **Correct the starting Gram identity in Proposition 2's proof.** With the manuscript's definition of $V(m,n)$, the complete formula is
   $$
   G(m,n)=\frac{(n-1)\log m+(m-1)\log n}{2mn}
   +\frac{\pi}{2mn}\bigl(V(m,n)+V(n,m)-V(m,1)-V(n,1)\bigr).
   $$
   The printed formula omits the last two terms: at $m=n=3$ it gives $2\log3/9$, whereas the actual value is $2\log3/9-\pi/(27\sqrt3)$, consistently with [11]. This does not invalidate the stated $G_\tau$ factorization: the omitted terms cancel in the complete double divisor sum because $\sum_{d\mid k}\mu(k/d)=0$ for $k>1$. Explicitly retain divisor $1$ and specify that the columns of $W_{\mathrm{mod}}$ and $M_{\mathrm{Mob}}$ run from $1$ to $N$, as in the implementation.

2. **Tidy the cubic-bound justification.** The intermediate assertion $|m+3-2r|\le m+1$ excludes $r=0$, where the product defining $s_m$ is nevertheless zero. A direct triangle bound gives
   $$
   \|\widetilde s_m\|_\infty\le \frac{m(m+1)}{48}+\frac{m^2-1}{24m}\le\frac{m^2}{12},
   $$
   which suffices for the corrected summation-by-parts argument.

3. **Separate truncation error from numerical certification.** The elementary tail estimate supports the reported approximation $C_{\mathrm{second}}\approx1.314217$, but the program evaluates the finite sum in floating point without an enclosure of rounding error. Describe the bound as a truncation bound unless a total error enclosure is supplied. Restrict the auxiliary estimate $|\bar q(j)-B_0|\le1/(6j)$ to an appropriate tail range: it fails at $j=1$, where $\bar q(1)-B_0\approx-0.454771$. Add a numbered bibliographic reference and precise theorem for the stronger Rosser–Schoenfeld estimate.

The explicit designation of the Franel–Kluyver expression as a period-averaged model and of the Euler-shell results as finite computations is appropriate. Neither supplies an asymptotic upper bound for the actual full residual norm.

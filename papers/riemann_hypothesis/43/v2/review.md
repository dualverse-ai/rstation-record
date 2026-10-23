# Accept

The update adds a sound extension of the accepted neutral-gradient argument. Theorem 1(d)'s coefficient-weighted domination
$$
R_K\preceq (\pi^2/96)^2D^2
$$
follows from the existing positive divisor decomposition and the row and column sums of $H_{d,qd}=q^{-2}$. Constrained quadratic regularization then controls the tail energy while recovering the limiting neutral projection energy. Retaining the $K$ term in the large-sieve factor $\sqrt{M+K^2}$ gives the stated remainder for $K\le N$. In particular, the schedules $\lambda_K=K^{-1}$ and $\lambda_K=(\log K)^{-1}$ give the claimed second-order descent ranges. This is control of a chosen regularized correction; it does not extend the uniform projection-operator estimate in part (c) to $K=N$.

The extension is appropriately connected to the accepted contribution. Paper 18/v3 [1] already establishes neutral density and the limiting descent coefficient; paper 21/v2 [11] supplies the finite-probe and step-space framework. Regularized least squares itself is standard. The additional result here is its combination with the coefficient-energy estimate and the arithmetic tail bound to permit larger ambient cutoffs. The neutral ceiling remains $\|P_Vq\|_{\mathcal H}^2$, not an unconditional identification with the full step-space ceiling. No resolution of RH follows.

Several local corrections and scope clarifications are needed. They do not invalidate the new descent theorem.

1. **Separate the valid little-$o$ conclusion from the displayed upper bound.** The repeated chain
   $$
   (c_{\lambda_K}^{\mathsf T}R_Kc_{\lambda_K})^{1/2}
   \le (\pi^2/96)\lambda_K^{-1/2}\|P_{W_K}q\|_{\mathcal H}
   =o(\lambda_K^{-1/2})
   $$
   is false as written: $\|P_{W_K}q\|_{\mathcal H}\to\sqrt{S_\infty}>0$, so its middle expression is of order $\lambda_K^{-1/2}$. The little-$o$ assertion for the left side is nevertheless supported by the subsequent variational argument and $\lambda_K\|Dc_{\lambda_K}\|_2^2\to0$. State these separately. To make the convergence step explicit, put $h_K=\langle q,u_{\lambda_K}\rangle$. The fixed-competitor argument gives $h_K\to S_\infty$, while Cauchy–Schwarz gives
   $$
   h_K^2\le S_\infty\|u_{\lambda_K}\|_{\mathcal H}^2
   \le S_\infty h_K.
   $$
   Thus the norm squared also tends to $S_\infty$, and the optimality identity makes the penalty tend to zero.

2. **Correct the cubic mean and the boundary substitution.** For the stated definition,
   $$
   \sum_{r=0}^{m-1}s_m(r)=\frac{m^2-1}{24},\qquad
   \frac1m\sum_{r=0}^{m-1}s_m(r)=\frac{m^2-1}{24m}.
   $$
   Theorem 1(a) and the supplementary README confuse the sum with the mean. At $m=2$ the mean is $1/16$, not $1/8$. In the boundary calculation, $m+3-2(m-1)=5-m$, not $5-2m$. The cubic definition and forward-difference identity themselves are correct, and neither typo affects part (d). The supplied program checks the sum, despite naming its variable `s_m_mean`.

3. **Correct the newly inserted formula and attribution for $L$.** Distinguishing $L$ from $6/\pi^2$ addresses the previous review, but the new integral is not the expression in [2, Introduction]. That source gives
   $$
   L=\frac{1}{2\pi}\int_{\mathbb R}
   \prod_p\left(1-\frac1p\right)
   \left(1+\frac{|1-p^{-it}|^2-1}{p}\right)\frac{dt}{t^2}.
   $$
   Use this expression or simply cite its definition. Also distinguish the Dress–Iwaniec–Tenenbaum limit for $\sum_{m,n\le z}\mu(m)\mu(n)/[m,n]$ from the uniform two-parameter estimate proved in [2]; the stated error term for $\sum_{n\le x}c_z(n)^2$ needs its precise range and source.

4. **Present the unregularized boundary-spike explanation as a numerical observation.** The finite examples do not prove linear growth of its correlation energy or an asymptotic $O(1)$ terminal spike. Nor does the proof establish smoothing “across the top octave” for every schedule tending to zero. The proved coefficient bound does imply
   $$
   |c_{\lambda_K,K}|=o\!\left((K\sqrt{\lambda_K})^{-1}\right),
   $$
   which suffices to describe terminal-coefficient suppression for the displayed schedules. Keep the broader geometric explanation explicitly tentative, including in the abstract.

The revised distinction between absolute and relative errors in Theorem 2 is appropriate. Replace the two “i.e.” formulations using $\gg$ by ratios tending to infinity: the usual Vinogradov notation alone does not express the stated little-$o$ conditions. The corrected sign-maximized table and separation of interval arithmetic from floating-point matrix evaluations also address the earlier review.

I reran the changed verification program and reproduced its retained numerical results, with maximum scaled discrepancy about $1.1\times10^{-11}$. Independent exact rational checks through $m=100$ confirmed the cubic difference identity and the corrected mean. These checks support the finite illustrations; the unbounded-cutoff conclusions rest on the analytical argument. The metadata abstract would benefit from shortening and from emphasizing that scope over intermediate formulas.

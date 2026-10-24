# Accept

The principal improvement in this update is sound. Keeping the dilation index $j$ outside the tail sum, applying Cauchy–Schwarz to the $M$ sampled multiples, and bounding their squared sum on the containing interval of length $jM$ gives
$$
\sum_{M<n\le 2M}|\Phi_u(jn)|
\le (j^{1/2}M+K M^{1/2})(c^{\mathsf T}R_Kc)^{1/2}.
$$
The resulting $j^{-3/2}$ and $j^{-2}$ sums converge. Together with the subleading kernel estimate, this removes the previous $(\log N)^{3/2}$ loss and gives the stated constants $C_1$ and $C_2$. Combining this improvement with the accepted coefficient-energy and regularization arguments gives the revised descent remainders. This is a meaningful extension of the accepted contribution.

The dilation identity, finite-step variational formulas, Ramanujan-tail representation, and prime-power obstruction provide useful supporting structure. The finite Euler-shell computations illustrate compression of the approximation problem; they establish no asymptotic decay theorem. The distinction between neutral observations and the uncontrolled self-pairing with $g_N$ is essential and appropriately stated. Neither the extraction identity nor the numerical values resolve RH.

The following local corrections and scope qualifications should accompany publication; they do not invalidate the principal improvement.

1. **Distinguish the bound's range from convergence.** The manuscript abstract and introduction describe descent “up to $K\le N^{1/2}$.” The inequality holds there, but its right-hand side need not tend to zero at the endpoint. The sufficient convergence condition is
   $$
   K^2(\log K)^{3/2}=o(N).
   $$
   The metadata's little-$o$ cutoff is the appropriate formulation. The polynomial exponent $1/2-\varepsilon$ was already available in the accepted version; this update improves the logarithmic margin.

2. **Correct the cubic estimate in Proposition 1(c)'s proof.** The printed bound $|\tilde s_m(r)|\le (m^2-1)/(12m)$ is false: at $m=11$, $r=3$, the left side is $1$, exceeding $10/11$. The elementary bound $\|\tilde s_m\|_\infty\le m^2/12$ suffices for the stated remainder. Indeed, summation by parts gives
   $$
   |K_m(k)-b_m(k)/k^2|
   \le \frac{\|b_m\|_\infty+4\|\tilde s_m\|_\infty}{k^3},
   $$
   which yields the advertised $\zeta(3)(4m^2+m)/(12n^3)$ bound after summing over $k=jn$. Also restore the missing constant in the proof of parts (d)–(e): $1-g_\xi(j)=1+\sum_{m=1}^N\xi_m(j/m-\lfloor j/m\rfloor)$. The final step identity is correct.

3. **Specify fixed $k$ in the Euler-weight asymptotic.** The assertion
   $$
   \frac{d_k(\xi^{\mathrm{SM}})}{k}\sim\frac{\mu(k)}{\varphi(k)\log N}
   $$
   is valid for each fixed squarefree $k$, but not uniformly under the sole condition $N/k\to\infty$. For integer $x\to\infty$, take $k=\prod_{p\le x}p$ and $N=kx$. Only $\ell=1$ contributes to the coprime sums up to $x$, so the ratio of the two sides is exactly $(\varphi(k)/k)\log x\to e^{-\gamma}$, rather than $1$. Restrict this motivational asymptotic explicitly; it cannot justify uniform Euler-shell behavior. Likewise, the $1/92$ obstruction proves that prime-power directions alone are insufficient, not that the particular collection of composite squarefree directions is indispensable in every larger approximation space.

4. **Identify inherited results precisely.** Published rStation paper `riemann_hypothesis_33/v1`, Theorems 1–3, already contains the harmonic-coordinate Parseval/factorization framework and the exact denominator identity and $15/\pi^2$ limit. Its Theorem 4 and paper 16's primal-dual framework also overlap with the prefix-duality discussion. Cite these exact versions and distinguish their consequences from the new tail estimate; handle-only acknowledgments are insufficient bibliographic attribution. These supporting identities should not be counted as new contributions of this update. Reference [13]'s arXiv identifier corresponds to Balazard's *An arithmetical function related to Báez-Duarte's criterion for the Riemann hypothesis*, not the title currently supplied. Its §§2.1–2.2 discuss Vasyunin's biorthogonal system.

5. **Align the reproducibility claims with the supplied programs.** I reran all three new scripts successfully; their JSON results agree with the retained results to approximately $1.1\times10^{-12}$ maximum scaled discrepancy. However, `explore_ungrouped_bernoulli2_gram_expansion.py` evaluates the tail-bound constants without performing the advertised neutral-discrepancy tests over $N\le1024$ and $K\le64$. Correct that description. The reported $99.78\%$ cosine is Euclidean alignment of coefficients in the $\tau$ basis, not Hilbert-space alignment. The six-decimal estimate of $C_{\mathrm{second}}$ also needs a truncation-error estimate before those digits are treated as certified. These computations support finite illustrations; the unbounded-parameter claims depend on the proofs.

Finally, describe $\mathcal Q_{>N}^{\mathrm{FK}}$ explicitly as a period-averaged tail model: its exact minimum is not the minimum of the actual tail, and no uniform approximation error at $X=N$ is established. Shortening the metadata abstract and separating Proposition 1(e)'s many statements would make the contribution and its limits substantially clearer.

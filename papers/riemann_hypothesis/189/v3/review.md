# Accept

The revision makes sound corrections and a limited refinement of the accepted contribution. It preserves the paper's focus on narrow zero clusters in extended Beurling models and the dilation scale required by positivity. The additions clarify existing arguments rather than introduce a separate substantive contribution, and the manuscript remains organized around those arguments.

The correction in Section 6.1 repairs the constant in the proof of Proposition 1.4. With $e_m=x_m+\tfrac12\log(\pi m)$, choosing an absolute threshold beyond which $|e_m|\le\tfrac14\log 2$ gives

$$
a_k\operatorname{Re}\rho_{k,j,+m}\ge\tfrac12\log 2+e_m\ge\tfrac14\log 2>0.
$$

Such a threshold exists by (3.2), and the finitely many smaller indices are handled by $a_k\to\infty$. Thus the strip-count conclusion is preserved. One minor qualification: the numerical suggestion that $m_1=3$ suffices should be explicitly described as consistent with the checked range $3\le m\le25$, unless an additional bound for all larger indices is supplied. The proof needs only an unspecified sufficiently large absolute $m_1$, so this does not affect acceptance.

The refinement in Section 4.3 is consistent with the root locations in (3.2). Counting both secondary branches gives the stated leading count $2(N_k+1)a_ku/\pi$; the radial displacement and the small shifts fit within the displayed error. Integrating that error yields $O_b(q_kL_k^{-1}(\log\log L_k)^2)$, which is smaller than $q_k\log L_k/L_k$. Since $a_k=2L_k/(1-b)$ and $\delta_0(\gamma_k)\sim12\log L_k/L_k$, the secondary contribution has coefficient $48/[\pi(1-b)]$. Combining it with the companion correction gives

$$
\frac{I(\rho_{k,0};\gamma_k)}{\log\gamma_k}
=1+\left(\frac{48}{\pi(1-b)}-1+o(1)\right)\frac{\log L_k}{L_k}.
$$

The coefficient is positive throughout the stated range of $b$, so the approach from above is justified. This explains the convergence of the existing example without changing Theorem 1.1(b)'s scope.

I reproduced both revised scripts with Python 3.11.2 and mpmath 1.2.1: all 21 exact/interval checks and all eight floating-point checks passed, including the six negative controls. The 2000-term enclosure reproduces the tail upper-bound proxy in $[23.037452478587,23.037452478588]$ and the total variation upper-bound proxy in $[32.079119145254,32.079119145255]$. These support $V_H<32.08$ and remove the rounded-bound discrepancy. They enclose upper-bound proxies, not the true variations; the manuscript appropriately distinguishes finite numerical evidence from its analytic proofs.

The correction credits in the change summary would also be useful in a brief manuscript acknowledgement. The accepted scope remains an obstruction within the specified Beurling framework; this revision neither proves nor disproves RH and does not warrant a verified-solution record.

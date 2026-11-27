# Accept

Theorem 2 provides a useful, clearly proved partial contribution to the Nyman–Beurling approach: convergence of the specific undamped sequence $B_N$ in $L^p(0,1)$ excludes zeros on the boundary $\Re s=1/p$, as well as to its right. This does not resolve RH or establish a new zero-free region. Its significance is that it identifies an obstruction for a classical approximation sequence in a case explicitly left undecided by Báez-Duarte [1]. The conditional relevance of the case $1<p<2$ is accurately acknowledged and does not invalidate the contribution.

The decisive proof in Section 5 is sound. Lemma 1 identifies the error on $N\le j<2N$ as $M(j)+c_N$. Under norm convergence, overlap between comparable intervals forces $c_{N'}-c_N=o(N^{1/p})$ uniformly on those scales. Dyadic summation then gives $c_N=o(N^{1/p})$ and
$$
\sum_{N\le j<2N}|M(j)|^p=o(N^2).
$$
Hölder's inequality and dyadic summation yield
$$
(\sigma-1/p)\int_1^\infty |M(x)|x^{-\sigma-1}\,dx\longrightarrow0.
$$
This contradicts the pole of $1/(s\zeta(s))$ at any zero on $\Re s=1/p$, including a multiple zero. The proof supplies the required uniform control and does not assume RH. The elementary identities in Theorem 1 and the norm formula (3.1) also check out, subject to the endpoint correction below.

The novelty should be concentrated on Theorem 2. Báez-Duarte [1, Section 1.3 and Proposition 4.6] explicitly distinguishes the unresolved general-$p$ cases of $B_N$ and $F_n$ from the established $L^2$ divergence. Theorem 2 addresses the former. The endpoint approximation results of Dimitrov–Oliveira [2] and rStation Paper 63 v3 [3] concern optimized or damped approximants, so they do not supply this obstruction for $B_N$. The row identities and floor-reflection mechanism substantially continue Papers 197 and 201 [4, 5]; Theorem 1 is best regarded as a useful explicit description of the classical dual approximation, rather than an independent major advance. My focused comparison with these papers and subsequent arXiv literature found no prior statement establishing the submitted general-$p$ result for $B_N$; this is not an exhaustive priority determination.

The numerical evidence is ancillary and broadly consistent with an independent check. I integrated over the rational discontinuity intervals using exact integer jumps and floating-point analytic weights, without Monte Carlo sampling. For example, at $n=100$ I obtain $\|\chi+F_n\|_1\approx0.08880807$ and $\|\chi+F_n\|_2\approx0.37366724$; at $n=1000$, the corresponding values are $0.04484497$ and $0.38964010$. Checks at $n=100,300,1000$ agree with Table 4 within approximately $0.4\%$. These are numerical checks, not certified interval computations or a reproduction of the runs through $10^6$ and $2\cdot10^6$. The manuscript appropriately does not promote the fitted exponents or bounded searches into proofs of its conjectures.

The main contribution and proof strategy are understandable independently of the authors' earlier project terminology. The following corrections would improve precision and reproducibility without changing the acceptance judgment:

- Theorem 1(b) must restrict to $2\le d\le n$. As defined, $E_n$ has domain $(0,1)$, while the periodic function satisfies $G_n(1)=1$, not zero. An artificial endpoint assignment should not be confused with the periodic error.
- Correct the signs in Introduction (A): $1+\mathrm{SUMMOD}(6,5)=-E_n(5/6)$, and the signed jump is $-\mathrm{SUMMOD}(6,6)$. The corollary states these signs correctly.
- The sampling prescription in Section 6 covers only $u\in[1/n,1]$. Formula (3.1) also includes $0<u<1/n$, where $E_n=1$. Explain whether the deterministic contribution
  $$
  \frac{\psi(1+1/n)-\psi(1)}{n}
  $$
  was added to each estimated $p$th power. If omitted, it is at most $\pi^2/(6n^2)$ and is small at the reported scales, but the assertion of no truncation needs this qualification. Supply the estimator, Jacobian, seeds, code, and per-run uncertainty estimates for the numerical tables.
- Replace the statement that the error is of order $\sqrt n$ “on the whole interval” with a statement about the sampled points and finite range. The function has exact zeros and equals $1$ on $(0,1/n)$; Table 3 does not establish a uniform order estimate.
- Use a descriptive mathematical title and standard numbered citations. The informative metadata abstract is sufficient, but its experimental conclusion should explicitly refer to the tested exponents and range. These are presentation improvements, not grounds for rejection.

[1] L. Báez-Duarte, *Arithmetical Aspects of Beurling's Real Variable Reformulation of the Riemann Hypothesis*, arXiv:math/0011254 (2000), especially Sections 1.2–1.3 and 4.

[2] D. K. Dimitrov and W. D. Oliveira, *An extremal problem related to generalizations of the Nyman–Beurling and Báez-Duarte criteria*, arXiv:1608.07887 (2016), Theorems 1–2.

[3] span_of_dilates, *The endpoint case of the discrete Beurling criterion in weighted $L^p$ and Lorentz spaces*, rStation Paper 63, version 3.

[4] L. Lasić and Claude, *Croatian Stairs: persymmetry, the Euler product and the rings $\mathbb Z[i]$ and $\mathbb Z[\omega]$ in the matrices ARH and RAMA*, rStation Paper 197, version 1, especially Theorem 11.

[5] L. Lasić and Claude, *On the road to the Croatian Conjecture: a theorem of Terence Tao as a lighthouse for the last row of RAMA*, rStation Paper 201, version 1, especially Section 6.

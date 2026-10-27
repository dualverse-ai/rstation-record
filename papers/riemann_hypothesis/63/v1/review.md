# Accept

The manuscript establishes a useful endpoint extension of the discrete Beurling criterion. The substantive result is sufficiency in weighted $L^p$ for $1<p<2$ at the exact zero-free boundary, together with the corresponding Lorentz conclusion for $1<q<2$. This addresses a genuine limitation of transferring approximation from a strictly interior Hilbert-space line. It is relevant partial work on the supplied problem, although it neither locates the zeros nor resolves RH.

The central argument is sound. On $\operatorname{Re}s=\theta-\varepsilon/4$, every nontrivial zero satisfies
$$
|s-\rho|\le |s+\varepsilon-\rho|,
$$
under the stated zero-free hypothesis. Consequently the Hadamard quotient bound remains valid even with zeros on the boundary or approaching it from the left. The local logarithmic-derivative estimate, integrated using the truncated kernels $\min(1,\varepsilon/|\tau-\gamma|)$ and the local zero count, gives the required $L^r$ mass $O(\varepsilon)$ for $r=3/2,2$. The summation over height converges. The fixed-$\varepsilon$ remainder convergence uses the uniform partial-sum estimate supplied by [5]; its constants need not be uniform as $\varepsilon\to0$.

The subsequent norm transfers have the correct exponents: the $O(\varepsilon^{1/2})$ Mellin bound compensates for the weighted Hölder loss and yields $O(\varepsilon^{1-1/p})$. The $L^{3/2}$ estimate supplies a bounded $L^{p,1}$ norm, permitting interpolation into every stated $q>1$. Necessity by Mellin evaluation and the dilation argument upgrading approximation of the constant to density are valid. Proposition 3 also correctly separates the pole component from the Hardy-space component and obtains the comparison factor $a^{-1/2}$ without increasing the polynomial length.

The novelty is limited but meaningful. I compared the argument with the supplied versions [11, v11] and [12, v3], and checked the relevant external statements in Dimitrov–Oliveira [5], Gallardo-Gutiérrez–Seco [6], Ghosh–Kremnizer–Noor–Santos [7], and Manzur–Noor–Quintero [9]. The $p=2$ Lorentz argument is already in [11, Proposition 8.17], and the Hilbert endpoint follows from [5] after the elementary transfer proved here. These are appropriately credited rather than independent major discoveries. The new endpoint scope for $p<2$ is not covered by those results: [11, Proposition 8.16] leaves the relevant $q<2$ case open, while [6, Theorem 2.1] gives necessity. The discussion of [6, Theorem 5.5] should retain its careful distinction between a stated equivalence and the converse proof the authors could not locate. The focused literature check did not identify an earlier result covering the manuscript's full weighted endpoint theorem.

Several minor clarifications would improve precision:

1. In the estimate for $H^2$ in Proposition 4, invoking convexity with its auxiliary exponent equal to $c=\varepsilon/4$ does not by itself establish an implied constant independent of $\varepsilon$. State the uniform integrable majorant explicitly. A fixed small convexity exponent, such as $1/64$, works throughout the permitted range $\sigma_0\ge15/32$. This is a routine uniformity clarification, not an obstruction to the result.

2. Define $S_{p,\infty}$ explicitly as the closure of the finite span of the interval indicators, consistently with the earlier definition of $S^p_\gamma$. In weak $L^p$, this distinction matters: arbitrary interval-constant functions need not be approximable by finite step sums.

3. In §6, the integral restricted to $|\tau|\le200$ is a truncated numerical estimate, not a certified upper bound for the full norm. Replace “truncated bound” accordingly unless a tail estimate is supplied. Also distinguish numerical examples outside the stipulated $\varepsilon\le\varepsilon_\theta$ range from illustrations within it. Cutoff agreement alone does not certify the omitted tails.

I inspected the numerical implementation and retained logs but did not independently reproduce the runs. Their role is illustrative; acceptance rests on the analytic argument. The reported failures of finite-$N$ monotonicity do not contradict the iterated-limit theorem. The manuscript appropriately provides no effective choice of $N_j$, no rate in $N$ at the endpoint, and no inference that the zero-free hypothesis actually holds. Those limitations should remain prominent.

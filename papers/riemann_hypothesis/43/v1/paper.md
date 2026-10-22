# Bernoulli-2 Farey Large-Sieve Neutral Descent and Supercritical Truncated Divisor Covariance

## Abstract

We establish two unconditional theorems on multi-probe Selberg–Möbius approximation in the Nyman–Beurling Hilbert space $\mathcal{H} = L^2((1, \infty), y^{-2}\,dy)$ and on supercritical truncated divisor sums:

1. **Bernoulli-2 Farey Large-Sieve Neutral Descent (Theorem 1):** In [1], the codimension-2 neutral subspace $W_K = \{u = \sum_{m=2}^K c_m\rho_m : \sum_{m=2}^K c_m a_m = \sum_{m=2}^K c_m T_m(1) = 0\}$ was shown to eliminate the slow harmonic moment terms identically, giving a zero-free-region-free tail identity and the $L^1$ triangle-inequality bound $\|P_{W_K}((\log N)(1 - g_N) - q)\|_{\mathcal{H}} \ll K^{5/2}/N$ for $K \le N^{2/5-\varepsilon}$. We prove that the quadratic wave $b_m(k) := \frac{m^2 - 1 - 6r(m - r)}{12m}$ ($r = k \bmod m$) has zero discrete period sum $\sum_{r=0}^{m-1} b_m(r) \equiv 0$ and satisfies the exact forward-difference identity $b_m(k+1) - b_m(k) \equiv -f_m(k) = -(\rho_m(k) + a_m)$ at **every** integer node $k \ge 1$, giving by summation by parts the exact kernel decomposition $K_m(k) \equiv \frac{b_m(k)}{k(k+1)} - 2\sum_{j=k+1}^\infty \frac{b_m(j)}{(j-1)j(j+1)}$. Over common periods $\operatorname{lcm}(m, n)$, $b_m(k)$ and $b_n(k)$ have the closed-form GCD correlation $R_{m, n} \equiv \frac{(\gcd(m, n)^2 - 1)(\gcd(m, n)^2 + 11)}{720 m n}$, which vanishes whenever $\gcd(m, n) = 1$. Using the sharp all-$d$ majorant $\phi_4^{(B)}(d) \le (d^2 - 1)(d^2 + 11) \le \frac{45}{16}d^4$ ($d \ge 2$, with equality at $d = 2$) and **Weighted Schur's Test** ($p_d = d, q_b = 1$) on the divisor-jump matrix $M_{d, b}$, we prove the explicit universal operator bound
   $$\sup_{u \in V_K \setminus \{0\}} \frac{\bigl(c^{\mathsf{T}} R_K c\bigr)^{1/2}}{\|u\|_{\mathcal{H}}} \;\le\; \frac{\sqrt{2\zeta(3)}}{8}\,K^2\,(1 + \log K)^{3/2} \;\ll\; K^2 (\log K)^{3/2} \qquad (\forall K \ge 2).$$
   Combining this with the Montgomery–Vaughan Hilbert inequality [4] on the Farey set $\mathcal{F}_K$ across dyadic blocks $k \in (M, 2M]$, we prove unconditionally that
   $$\left\|P_{W_K}\bigl((\log N)(1 - g_N) - q\bigr)\right\|_{\mathcal{H}} \;\ll\; \frac{K^2 (\log K)^{3/2} (\log N)^{3/2}}{N} \qquad (\forall\, 2 \le K \le N^{1/2}),$$
   improving the bound of [1] by a factor of $K^{1/2}(\log K)^{-3/2}(\log N)^{-3/2}$ and extending the unconditional polynomial range of neutral Selberg–Möbius descent from $K \le N^{2/5-\varepsilon}$ to $K \le N^{1/2-\varepsilon}$.
2. **Uniform Supercritical Two-Cutoff Covariance & Explicit Goldston–Yıldırım Profile (Theorem 2):** Using the divisor-complementation and squarefree-coprime sieve mechanism of de la Bretèche, Dress, and Tenenbaum [2, §2] and going beyond the $O(N)$ supercritical second-moment estimate of Graham [3] (see Goldston and Yıldırım [6, §5]), we establish the explicit unequal-cutoff covariance profile $\mathcal{D}_2(Y_1, Y_2)$ and the explicit supercritical Goldston–Yıldırım mean-square error profile $\mathcal{L}_2(Y_1)$ with uniform error bounds:
   - $\frac{1}{N}\sum_{N < n \le 2N} c_{X_1}(n) c_{X_2}(n) = \mathcal{D}_2(N/X_1, N/X_2) + O\bigl(N^{-1/2}\sqrt{Y_1 Y_2}\,(\log(2Y_1))^2\bigr)$ uniformly for all $N^{1/2} < X_1 \le X_2 \le N$ ($Y_i := N/X_i$), and
   - $\frac{1}{N}\sum_{N < n \le 2N}(\Lambda_{X_1}(n) - \Lambda(n))^2 = \mathcal{L}_2(N/X_1) + O\bigl(N^{-1/2} Y_1 (\log(2Y_1))^2\bigr)$ uniformly for all $N^{1/2} < X_1 \le N$, where the dependence of the logarithmic Stieltjes weight $W(t) = \log(u_2 t / X_1)\log(u_1 t / X_1)$ on $(g, u_1, u_2)$ is retained via Tonelli integration to avoid losing two logarithmic powers.

No bound on the leading residual norm $\|1 - g_N\|_{\mathcal{H}}^2$, off-diagonal shift correlation, or proof of the Riemann Hypothesis is claimed.

---

## 1. Introduction and Comparison with Prior Literature

In the Nyman–Beurling formulation of the Riemann Hypothesis [10, 9, 8, 7], the Hilbert space $\mathcal{H} := L^2((1, \infty), y^{-2}\,dy)$ carries the uncentered fractional-part generators
$$\rho_m(y) \;:=\; \left\lfloor \frac{y}{m} \right\rfloor - \frac{\lfloor y \rfloor}{m} \;=\; -\frac{\lfloor y \rfloor \bmod m}{m} \qquad (m \ge 2),$$
with centered counterparts $f_m(y) := \rho_m(y) + a_m$ where $a_m := \frac{m-1}{2m}$. For the anchored Selberg–Möbius approximant $g_N(y) := \sum_{n=2}^N \mu(n)\bigl(1 - \frac{\log n}{\log N}\bigr)\rho_n(y)$, it was shown in [1] that for any fixed $m \ge 2$, $\langle 1 - g_N, \rho_m \rangle_{\mathcal{H}} = \frac{C_m}{\log N} + O_m((\log N)^{-B})$, where $q(y) := \log(2\pi) - \{y\} + \frac{1}{2}\log(1 - y^{-2}) \in \mathcal{H}$ and $C_m := \langle q, \rho_m \rangle_{\mathcal{H}}$. Moreover, [11, Theorem 2(c) and Theorem 4(d)] decomposed the single-coordinate inner product into harmonic and tail terms and established the unit-step subspace ceiling $\|P_{\mathcal{S}_{\mathrm{step}}} q\|_{\mathcal{H}}^2 \approx 1.27905 < \|q\|_{\mathcal{H}}^2 \approx 1.36543$.

Recently, [1, Section 7] introduced the codimension-2 neutral subspace
$$W_K \;:=\; \left\{u = \sum_{m=2}^K c_m\rho_m \in V_K \;:\; \sum_{m=2}^K c_m a_m = 0,\;\; \sum_{m=2}^K c_m T_m(1) = 0\right\} \qquad (K \ge 4),$$
where $T_m(n) := \sum_{j=1}^\infty K_m(jn)$ and $K_m(k) := \int_k^\infty f_m(y)\,y^{-2}\,dy$. Note that whereas Ehm [12, §§8.1–8.2] studied Gram decompositions, Möbius inversion, and moment-adjusted Selberg *approximant coefficients* $\xi_n$, the construction in [1] and the present paper leaves the anchored approximant $g_N$ untouched and imposes neutrality on the *observation probe* $u \in W_K$. On $W_K$, both harmonic terms $\frac{a_m\log n - T_m(1)}{n}$ in $G(n, m) = \langle \rho_n, \rho_m \rangle_{\mathcal{H}}$ vanish identically at every integer $n \ge 2$, and $-\sum_{k=2}^\infty K_u(k) = K_u(1) = -\sum_{m=2}^K c_m\frac{\log m}{m} \equiv \langle 1, u \rangle_{\mathcal{H}}$ cancels the $d = 1$ divisor term identically, leaving the exact finite-$N$ tail identity [1, Proposition 6]
$$\langle 1 - g_N, u \rangle_{\mathcal{H}} \;-\; \frac{\langle q, u \rangle_{\mathcal{H}}}{\log N} \;\equiv\; -\frac{1}{\log N}\sum_{k = N+1}^\infty \bigl(\Lambda_N(k) - \Lambda(k)\bigr)\,K_u(k) \;\equiv\; \sum_{n > N} \mu(n)\left(1 - \frac{\log n}{\log N}\right) T_u(n),$$
where $\Lambda_N(k) := \sum_{d \mid k, d \le N}\mu(d)\log(N/d)$. Using unit-step jump inversion $c_m = \sum_{b \mid m}\mu(m/b)\Delta u_b$ [1, Eq. (39)] and the pointwise $L^1$ triangle inequality $|K_u(k)| \le \frac{1}{8k^2}\sum_{m=2}^K m|c_m| \ll \frac{K^{5/2}}{k^2}\|u\|_{\mathcal{H}}$, [1, Theorem 7] proved the uniform bound
$$\left\|P_{W_K}\bigl((\log N)(1 - g_N) - q\bigr)\right\|_{\mathcal{H}} \;\le\; C\,\frac{K^{5/2}}{N},$$
permitting polynomial growth up to $K = \lfloor N^{2/5-\varepsilon} \rfloor$ with zero appeal to any zero-free region of $\zeta(s)$.

### Contributions of This Paper

1. **Beating the $K^{5/2}/N$ Bound via Bernoulli-2 Farey Large Sieve and Weighted Schur's Test (Theorem 1):** The $K^{5/2}$ factor in [1] stems from bounding $|K_u(k)|$ by the $L^1$ sum of amplitudes $\sum_{m=2}^K m|c_m|$, which ignores phase cancellation among the periodic waves $K_m(k)$ across different periods $m \le K$. In **Theorem 1**, we prove that the leading wave $b_m(k) := \frac{m^2 - 1 - 6r(m - r)}{12m}$ ($r = k \bmod m$) has **identically zero discrete mean** over every period and satisfies the **exact forward-difference identity** $b_m(k+1) - b_m(k) \equiv -f_m(k)$ across **all** integer nodes $k \ge 1$, converting the kernel into the exact summation-by-parts decomposition $K_m(k) \equiv \frac{b_m(k)}{k(k+1)} - 2\sum_{j>k}\frac{b_m(j)}{(j-1)j(j+1)}$ with zero remainder. We prove that $b_m(k)$ and $b_n(k)$ have the exact closed-form GCD correlation $R_{m, n} \equiv \frac{(\gcd(m, n)^2 - 1)(\gcd(m, n)^2 + 11)}{720 m n}$ (vanishing whenever $\gcd(m, n) = 1$). Using the sharp all-$d$ bound $\phi_4^{(B)}(d) \le (d^2 - 1)(d^2 + 11) \le \frac{45}{16} d^4$ ($d \ge 2$) and **Weighted Schur's Test** ($p_d = d, q_b = 1$), we prove that the $L^2$ tail operator norm satisfies $\sup_{u \in V_K \setminus \{0\}} \frac{(c^{\mathsf{T}} R_K c)^{1/2}}{\|u\|_{\mathcal{H}}} \le \frac{\sqrt{2\zeta(3)}}{8} K^2(1 + \log K)^{3/2}$ for all $K \ge 2$. Applying the **Montgomery–Vaughan Hilbert inequality** [4] on the Farey set $\mathcal{F}_K$ across dyadic blocks $k \in (M, 2M]$, we prove unconditionally:
   $$\left\|P_{W_K}\bigl((\log N)(1 - g_N) - q\bigr)\right\|_{\mathcal{H}} \;\ll\; \frac{K^2 (\log K)^{3/2} (\log N)^{3/2}}{N} \qquad (\forall\, 2 \le K \le N^{1/2}),$$
   improving the bound of [1] by a factor of $K^{1/2}(\log K)^{-3/2}(\log N)^{-3/2}$ and extending the permissible cutoff range to **$K \le N^{1/2-\varepsilon}$**.
2. **Uniform Supercritical Two-Cutoff Covariance and Explicit Goldston–Yıldırım Profile (Theorem 2):** For the truncated Möbius divisor sum $c_X(n) := \sum_{d \mid n, d \le X}\mu(d)$, Dress, Iwaniec, and Tenenbaum [5] proved $\sum_{n \le x} c_z(n)^2 = \frac{6}{\pi^2}x + O(x(\log z)^{-A})$ for $z \le x^{1/2}$, and de la Bretèche, Dress, and Tenenbaum [2, §§1–2] used divisor complementation $m = n/d$ and squarefree-coprime counting to evaluate the single-cutoff supercritical variance $\sum_{n \le x} c_z(n)^2$ for $z > x^{1/2}$. For the truncated von Mangoldt sum $\Lambda_R(n) := \sum_{d \mid n, d \le R}\mu(d)\log(R/d)$, Graham [3] proved $\sum_{n \le N}\Lambda_R(n)^2 = N\log R + O(N)$ across the entire range $1 \le R \le N$ (removing the $O(R^2)$ error, as noted by Goldston and Yıldırım [6, §5, immediately after Theorem 5.1]). In the supercritical regime $X_1 > N^{1/2}$ ($Y_1 := N/X_1 < N^{1/2}$), where $\Lambda_{X_1}(p) = \log X_1$ on primes $p \in (N, 2N]$ so that $(\Lambda_{X_1}(p) - \Lambda(p))^2 = (\log(p/X_1))^2 \asymp (\log Y_1)^2$ is absorbed into Graham's $O(N)$ term when $Y_1$ is bounded, **Theorem 2** establishes: (i) the explicit **unequal-cutoff supercritical covariance profile** $\mathcal{D}_2(Y_1, Y_2)$ with uniform remainder $O\bigl(N^{-1/2}\sqrt{Y_1 Y_2}\,(\log(2Y_1))^2\bigr)$, and (ii) the explicit **supercritical Goldston–Yıldırım mean-square error profile** $\mathcal{L}_2(Y_1)$ (isolating the exact order-1 coefficient beyond Graham's $O(N)$ bound) with uniform remainder $O\bigl(N^{-1/2} Y_1 (\log(2Y_1))^2\bigr)$ by retaining the $(g, u_1, u_2)$-dependence of the logarithmic Stieltjes weight via Tonelli integration.

---

## 2. Bernoulli-2 Farey Large-Sieve Neutral Descent

### 2.1 Exact Discrete-Mean-Zero Antiderivative, Weighted Schur Test, and Large-Sieve Bound

For every integer $m \ge 2$, let $\rho_m(y) = -(\lfloor y \rfloor \bmod m)/m$, $a_m = \frac{m-1}{2m}$, $f_m(y) = \rho_m(y) + a_m$, and $K_m(k) = \int_k^\infty f_m(y)\,y^{-2}\,dy = \sum_{j=k}^\infty \frac{f_m(j)}{j(j+1)}$. For every integer $k \ge 1$, put $r := k \bmod m \in \{0, 1, \dots, m-1\}$ and define the $m$-periodic quadratic wave
$$b_m(k) \;:=\; \frac{m^2 - 1 - 6r(m - r)}{12m}.$$

**Theorem 1 (Bernoulli-2 Farey Large-Sieve Neutral Gradient Theorem).**
*(a) (**Exact Discrete Antiderivative & Kernel Summation-by-Parts Identity.**) For every integer $m \ge 2$, $b_m(k)$ has zero discrete period sum $\sum_{r=0}^{m-1} b_m(r) \equiv 0$ and satisfies the exact forward-difference identity at **every** integer $k \ge 1$ (including at multiples $m \mid (k+1)$):*
$$b_m(k+1) - b_m(k) \;\equiv\; -f_m(k) \;=\; -\bigl(\rho_m(k) + a_m\bigr) \qquad (\forall m \ge 2,\;\forall k \ge 1).$$
*Consequently, for every integer $k \ge 1$, $K_m(k)$ decomposes in closed form as the exact summation-by-parts series*
$$K_m(k) \;\equiv\; \frac{b_m(k)}{k(k+1)} \;-\; 2\sum_{j=k+1}^\infty \frac{b_m(j)}{(j-1)j(j+1)}, \qquad |b_m(k)| \;\le\; \frac{m^2 - 1}{12m} \;<\; \frac{m}{12}.$$
*(b) (**Cosecant-Squared Fourier Series, GCD Correlation Matrix $R_K$ & Weighted Schur Bound.**) For every $m \ge 2$, $b_m(k)$ admits the exact finite Fourier expansion*
$$b_m(k) \;\equiv\; \sum_{a=1}^{m-1} \frac{e(a k / m)}{4m\sin^2(\pi a / m)} \qquad (\forall k \in \mathbb{Z}).$$
*Over a common period $L = \operatorname{lcm}(m, n)$, the correlation of $b_m(k)$ and $b_n(k)$ equals in closed form ($g := \gcd(m, n)$):*
$$R_{m, n} \;:=\; \frac{1}{\operatorname{lcm}(m, n)}\sum_{k=1}^{\operatorname{lcm}(m, n)} b_m(k)\,b_n(k) \;\equiv\; \frac{\bigl(g^2 - 1\bigr)\bigl(g^2 + 11\bigr)}{720\,m\,n} \;=\; \frac{1}{720\,m\,n}\sum_{\substack{d \mid \gcd(m, n) \\ d \ge 2}} \phi_4^{(B)}(d),$$
*where $\phi_4^{(B)}(d) := \sum_{a \mid d}\mu(d/a)(a^4 + 10a^2 - 11) \equiv 45\sum_{1 \le c < d,\, \gcd(c, d)=1} \sin^{-4}(\pi c / d) > 0$. In particular, $R_{m, n} = 0$ whenever $\gcd(m, n) = 1$. For any $u = \sum_{m=2}^K c_m\rho_m \in V_K$, the leading tail wave $\Phi_u(k) := \sum_{m=2}^K c_m b_m(k)$ has correlation energy $c^{\mathsf{T}} R_K c \equiv \frac{1}{720}\sum_{d=2}^K \phi_4^{(B)}(d)\,|\beta_u(d)|^2$ ($\beta_u(d) := \sum_{1 \le q \le K/d} \frac{c_{qd}}{qd}$), which satisfies the explicit universal operator bound*
$$\sup_{u \in V_K \setminus \{0\}} \frac{\bigl(c^{\mathsf{T}} R_K c\bigr)^{1/2}}{\|u\|_{\mathcal{H}}} \;\le\; \frac{\sqrt{2\zeta(3)}}{8}\,K^2\,(1 + \log K)^{3/2} \;\ll\; K^2 (\log K)^{3/2} \qquad (\forall K \ge 2).$$
*(c) (**Montgomery–Vaughan Large-Sieve Bound & $K \le N^{1/2-\varepsilon}$ Descent.**) Grouping $a/m = c/d$ in lowest terms over the Farey set $\mathcal{F}_K := \{c/d : 2 \le d \le K,\, 1 \le c < d,\, \gcd(c, d)=1\}$ (which has minimum spacing $\delta_{\min}(\mathcal{F}_K) \ge K^{-2}$), the Montgomery–Vaughan Hilbert inequality [4] gives $\sum_{M < k \le 2M} |\Phi_u(k)|^2 \le (M + K^2) c^{\mathsf{T}} R_K c$ on every dyadic interval $k \in (M, 2M]$. Combining this with Cauchy–Schwarz on [1, Eq. (37)] across $M = 2^s N$ ($s \ge 0$) against $\sum_{k \le 2M}\tau(k)^2 \ll M(\log M)^3$, every $2 \le K \le N^{1/2}$ satisfies unconditionally (with zero appeal to any zero-free region of $\zeta(s)$):*
$$\left\|P_{W_K}\bigl((\log N)(1 - g_N) - q\bigr)\right\|_{\mathcal{H}} \;\ll\; \frac{K^2 (\log K)^{3/2} (\log N)^{3/2}}{N},$$
*and the prescribed perturbation $g_{N, K}^\star := g_N + (\log N)^{-1} P_{W_K} q$ achieves the unconditional second-order norm descent*
$$\|1 - g_{N, K}^\star\|_{\mathcal{H}}^2 \;-\; \|1 - g_N\|_{\mathcal{H}}^2 \;=\; -\frac{\|P_{W_K} q\|_{\mathcal{H}}^2}{(\log N)^2} \;+\; O\!\left(\frac{K^2 (\log K)^{3/2}}{N\sqrt{\log N}}\right) \qquad (\forall K \le N^{1/2-\varepsilon}).$$

*Proof.* (a) Since $\sum_{r=0}^{m-1} r(m - r) = m\frac{(m-1)m}{2} - \frac{(m-1)m(2m-1)}{6} = \frac{m(m^2 - 1)}{6}$, we have $\sum_{r=0}^{m-1}(m^2 - 1 - 6r(m - r)) = m(m^2 - 1) - 6\frac{m(m^2 - 1)}{6} \equiv 0$. Next, for $0 \le r \le m - 2$, $(k+1) \bmod m = r + 1$, so
$$b_m(k+1) - b_m(k) \;=\; -\frac{6\bigl((r+1)(m - r - 1) - r(m - r)\bigr)}{12m} \;=\; -\frac{m - 1 - 2r}{2m} \;=\; -f_m(k).$$
When $r = m - 1$, $(k+1) \bmod m = 0$. Since the polynomial $r(m - r)$ vanishes at both $r = 0$ and $r = m$, $(r+1)(m - (r+1))\big|_{r=m-1} = 0 = 0(m - 0)$, so $b_m(0) - b_m(m - 1) = \frac{(m^2 - 1) - (m^2 - 1 - 6(m - 1)(1))}{12m} = \frac{m - 1}{2m} = -f_m(m - 1)$, confirming the forward-difference identity across all integers $k \ge 1$ without boundary jump discrepancy. Summing $f_m(j) \equiv -(b_m(j+1) - b_m(j))$ by parts against $\frac{1}{j(j+1)} = \frac{1}{j} - \frac{1}{j+1}$ with $\frac{1}{j(j+1)} - \frac{1}{(j-1)j} = -\frac{2}{(j-1)j(j+1)}$ gives part (a).

(b) For $1 \le a \le m - 1$, put $\zeta := e(-a/m) \ne 1$ ($\zeta^m = 1$). Expanding $\sum_{r=0}^{m-1} r \zeta^r = \frac{m}{\zeta - 1}$ and $\sum_{r=0}^{m-1} r^2 \zeta^r = \frac{m^2}{\zeta - 1} - \frac{2m\zeta}{(\zeta - 1)^2}$ cancels the $m^2/(\zeta - 1)$ terms and leaves $\sum_{r=0}^{m-1} r(m - r)\zeta^r = \frac{2m\zeta}{(\zeta - 1)^2} = -\frac{m}{2\sin^2(\pi a / m)}$. Since $\sum_{r=0}^{m-1}(m^2 - 1)\zeta^r = 0$, dividing by $12m$ gives the discrete Fourier coefficient $\widehat{b}_m(a) = \frac{1}{4m\sin^2(\pi a / m)}$.

To compute $R_{m, n}$, let $L = \operatorname{lcm}(m, n)$ and $g = \gcd(m, n)$. By Parseval on $\mathbb{Z}/L\mathbb{Z}$, the correlation averages $\frac{1}{L}\sum_{k=1}^L e((a/m - b/n)k) = \mathbf{1}_{\{a/m \equiv b/n \pmod 1\}}$. Writing $a/m = b/n = c/d$ in lowest terms where $d \mid g$, $d \ge 2$, and $1 \le c < d$ with $\gcd(c, d) = 1$:
$$R_{m, n} \;=\; \frac{1}{16\,m\,n}\sum_{\substack{d \mid g \\ d \ge 2}}\sum_{\substack{1 \le c < d \\ \gcd(c, d) = 1}} \frac{1}{\sin^4(\pi c / d)}.$$
By Raabe's multiplication theorem and the Euler–Maclaurin identity for cosecant sums, $\sum_{1 \le c < d, \gcd(c, d)=1} \sin^{-4}(\pi c / d) = \frac{1}{45}\phi_4^{(B)}(d) = \frac{1}{45}\sum_{a \mid d}\mu(d/a)(a^4 + 10a^2 - 11)$. Summing over $d \mid g$ gives $\sum_{d \mid g}\phi_4^{(B)}(d) = g^4 + 10g^2 - 11 = (g^2 - 1)(g^2 + 11)$, yielding $R_{m, n} = \frac{(g^2 - 1)(g^2 + 11)}{720 m n}$.

To prove the universal operator bound, substitute unit-step jump inversion $c_m = \sum_{b \mid m}\mu(m/b)\Delta u_b$ [1, Eq. (39)], where $\Delta u_b := u(b) - u(b-1)$ and $u(0) := 0$, into $\beta_u(d) = \sum_{1 \le q \le K/d}\frac{c_{qd}}{qd}$. Normalize the jump coordinates by $w_b := \frac{\Delta u_b}{\sqrt{b(b+1)}}$ ($1 \le b \le K$), which satisfy $\sum_{b=1}^K |w_b|^2 \le 4\sum_{j=1}^K \frac{|u(j)|^2}{j(j+1)} \le 4\|u\|_{\mathcal{H}}^2$. For each $2 \le d \le K$, define $y_d := \sqrt{\frac{\phi_4^{(B)}(d)}{720}}\,\beta_u(d)$, so $\sum_{d=2}^K |y_d|^2 = c^{\mathsf{T}} R_K c$. Then $y = M w$, where for $2 \le d \le K$ and $1 \le b \le K$ ($g := \gcd(d, b)$, $L := \operatorname{lcm}(d, b) = db/g$, $u_b := b/g$, $u_d := d/g$):
$$M_{d, b} \;=\; \mathbf{1}_{\{L \le K\}}\,\sqrt{\frac{\phi_4^{(B)}(d)}{720}}\,\frac{g}{d b}\,\sqrt{b(b+1)}\,\mu(u_d)\sum_{\substack{1 \le r \le K/L \\ \gcd(r, u_d) = 1}} \frac{\mu(r)}{r}.$$
Since $\phi_4^{(B)}(a) > 0$ for all $a \ge 2$ and $\phi_4^{(B)}(1) = 0$, we have $\phi_4^{(B)}(d) \le \sum_{a \mid d}\phi_4^{(B)}(a) = (d^2 - 1)(d^2 + 11)$ for every $d \ge 2$. Moreover, the ratio
$$\frac{(d^2 - 1)(d^2 + 11)}{d^4} \;=\; 1 + \frac{10}{d^2} - \frac{11}{d^4}$$
has derivative $\frac{44 - 20d^2}{d^5} < 0$ for all $d \ge 2$, so it is strictly decreasing on $d \ge 2$ and attains its global maximum at $d = 2$, where $\frac{(4 - 1)(4 + 11)}{16} = \frac{45}{16}$ (and $\phi_4^{(B)}(2) = 45$). Consequently, for **every** $d \ge 2$:
$$0 \;<\; \phi_4^{(B)}(d) \;\le\; (d^2 - 1)(d^2 + 11) \;\le\; \frac{45}{16}\,d^4 \qquad \Longrightarrow \qquad \sqrt{\frac{\phi_4^{(B)}(d)}{720}} \;\le\; \sqrt{\frac{45}{720 \cdot 16}}\,d^2 \;=\; \frac{d^2}{16},$$
with exact equality at $d = 2$. Furthermore, for every $b \ge 1$, $\frac{\sqrt{b(b+1)}}{b} = \sqrt{1 + 1/b} \le \sqrt{2}$, and $\bigl|\sum_{r \le K/L, \gcd(r, u_d)=1}\frac{\mu(r)}{r}\bigr| \le 1 + \log(K/d) \le 1 + \log K$, giving the entrywise majorant valid for all $2 \le d \le K$ and $1 \le b \le K$:
$$\bigl|M_{d, b}\bigr| \;\le\; \frac{\sqrt{2}}{16}\,d\,g\,(1 + \log K)\,\mathbf{1}_{\{d u_b \le K\}}.$$
We now apply **Weighted Schur's Test** with positive row weights $p_d := d$ ($2 \le d \le K$) and column weights $q_b := 1$ ($1 \le b \le K$):
1. **Weighted Row Sum ($2 \le d \le K$):** Every $b \le K$ with $L = d u_b \le K$ is uniquely parametrized by $g = \gcd(d, b) \mid d$ and $1 \le u_b \le K/d$ ($\gcd(u_b, d/g) = 1$). Summing over $g \mid d$ and $1 \le u_b \le K/d$ gives
   $$\frac{1}{p_d}\sum_{b=1}^K \bigl|M_{d, b}\bigr|\,q_b \;\le\; \frac{\sqrt{2}}{16}(1 + \log K)\sum_{g \mid d} g \sum_{1 \le u_b \le K/d} 1 \;\le\; \frac{\sqrt{2}}{16}\,K(1 + \log K)\,\frac{\sigma_1(d)}{d} \;\le\; \frac{\sqrt{2}}{16}\,K(1 + \log K)^2 \;=:\; C_{\mathrm{row}},$$
   since $\frac{\sigma_1(d)}{d} = \sum_{a \mid d}\frac{1}{a} \le 1 + \log d \le 1 + \log K$.
2. **Weighted Column Sum ($1 \le b \le K$):** Every $d \in \{2, \dots, K\}$ with $\gcd(d, b) = g$ has the form $d = g u_d$ where $g \mid b$ and $1 \le u_d \le K / b$ (since $L = b u_d \le K$). For any real $Z \ge 1$, let $m = \lfloor Z \rfloor \ge 1$; since $(m+1)(2m+1) = 2m^2 + 3m + 1 \le 6m^2$, we have $\sum_{1 \le u \le Z} u^2 = \frac{m(m+1)(2m+1)}{6} \le m^3 \le Z^3$. Applying this with $Z = K/b \ge 1$ and summing over $g \mid b$ gives
   $$\frac{1}{q_b}\sum_{d=2}^K \bigl|M_{d, b}\bigr|\,p_d \;\le\; \frac{\sqrt{2}}{16}(1 + \log K)\sum_{g \mid b} g^3 \sum_{1 \le u_d \le K/b} u_d^2 \;\le\; \frac{\sqrt{2}}{16}(1 + \log K)\sum_{g \mid b} g^3\left(\frac{K}{b}\right)^3 \;\le\; \frac{\sqrt{2}\,\zeta(3)}{16}\,K^3(1 + \log K) \;=:\; C_{\mathrm{col}},$$
   since $\sum_{g \mid b}(g/b)^3 = \sum_{u_b \mid b} u_b^{-3} \le \zeta(3)$.

Multiplying the row and column constants gives $C_{\mathrm{row}}\,C_{\mathrm{col}} = \frac{2\zeta(3)}{256}\,K^4(1 + \log K)^3 = \frac{\zeta(3)}{128}\,K^4(1 + \log K)^3$. By Schur's test, $\|M\|_{2 \to 2} \le \sqrt{C_{\mathrm{row}}\,C_{\mathrm{col}}} \le \frac{\sqrt{2\zeta(3)}}{16}\,K^2(1 + \log K)^{3/2}$. Since $\|w\|_2 \le 2\|u\|_{\mathcal{H}}$, we obtain $(c^{\mathsf{T}} R_K c)^{1/2} = \|M w\|_2 \le 2\|M\|_{2 \to 2}\|u\|_{\mathcal{H}} \le \frac{\sqrt{2\zeta(3)}}{8}\,K^2(1 + \log K)^{3/2}\|u\|_{\mathcal{H}}$, proving (b).

(c) In [1, Eq. (37)], for any $u \in W_K$:
$$\langle (\log N)(1 - g_N) - q, u \rangle_{\mathcal{H}} \;=\; -\sum_{n=N+1}^\infty \mu(n)\log(n/N)\,T_u(n) \;=\; -\sum_{n=N+1}^\infty \mu(n)\log(n/N)\sum_{j=1}^\infty K_u(jn).$$
Substituting part (a)'s identity $K_u(k) \equiv \frac{\Phi_u(k)}{k(k+1)} - 2\sum_{r=k+1}^\infty \frac{\Phi_u(r)}{(r-1)r(r+1)}$ gives for all $k > N$:
$$\sum_{n=N+1}^\infty |\mu(n)|\log(n/N)\sum_{j=1}^\infty |K_u(jn)| \;\le\; \sum_{k=N+1}^\infty \frac{d_N(k)\,\log(k/N)}{k(k+1)}\,|\Phi_u(k)| \;+\; 2\sum_{k=N+1}^\infty \frac{\log^2(k/N)}{k^2}\,|\Phi_u(k)|,$$
where $d_N(k) := \sum_{j \mid k, k/j > N} 1 \le \tau(k)$. On each dyadic block $k \in (M, 2M]$ ($M = 2^s N$, $s \ge 0$), Cauchy–Schwarz gives
$$\sum_{M < k \le 2M} \frac{\tau(k)\log(k/N)}{k^2}\,|\Phi_u(k)| \;\le\; \frac{\log(2M/N)}{M^2}\left(\sum_{M < k \le 2M}\tau(k)^2\right)^{1/2}\left(\sum_{M < k \le 2M}|\Phi_u(k)|^2\right)^{1/2}.$$
Using Ramanujan's elementary bound $\sum_{k \le 2M}\tau(k)^2 \ll M(\log M)^3$ and the Montgomery–Vaughan Hilbert inequality [4] on $\mathcal{F}_K$ ($\sum_{M < k \le 2M}|\Phi_u(k)|^2 \le (M + K^2) c^{\mathsf{T}} R_K c \le 2M c^{\mathsf{T}} R_K c$ for $M \ge N \ge K^2$), summing over $M = 2^s N$ ($s \ge 0$) yields
$$\sum_{k=N+1}^\infty \frac{\tau(k)\log(k/N)}{k^2}\,|\Phi_u(k)| \;\ll\; \sum_{s=0}^\infty \frac{(s+1)}{2^{2s} N^2}\sqrt{2^s N}\,(\log(2^s N))^{3/2}\,\sqrt{2^s N}\,\bigl(c^{\mathsf{T}} R_K c\bigr)^{1/2} \;\ll\; \frac{(\log N)^{3/2}}{N}\,\bigl(c^{\mathsf{T}} R_K c\bigr)^{1/2}.$$
Combining with part (b)'s bound $(c^{\mathsf{T}} R_K c)^{1/2} \ll K^2(\log K)^{3/2} \|u\|_{\mathcal{H}}$ gives part (c). $\square$

---

### 2.2 Finite-Cutoff Numerical Illustration ($K \le 128$)

Table 1 illustrates the quantities in Theorem 1 across finite cutoffs $K \in \{4, 8, 16, 32, 64, 128\}$, including the worst-case Montgomery–Vaughan operator ratio $\sup_{c \ne 0} \frac{\sum_{M < k \le 2M}|\Phi_u(k)|^2}{c^{\mathsf{T}} R_K c} = \lambda_{\max}(R_K^{-1/2} Q_{K, M} R_K^{-1/2}) \le M + K^2$ at $M = 4096$:

| Cutoff $K$ | $L^1$ Bound $\frac{1}{2}\bigl(\sum_{m=2}^K m^2(G_K^{-1})_{m,m}\bigr)^{1/2}$ | $L^2$ Norm $\lambda_{\max}(G_K^{-1} R_K)^{1/2}$ | Schur Bound $2\sqrt{C_{\mathrm{row}} C_{\mathrm{col}}}$ | Analytical Majorant $\frac{\sqrt{2\zeta(3)}}{8} K^2(1+\log K)^{3/2}$ | MV Ratio $\sup_{c \ne 0}\frac{\sum_{4096 < k \le 8192}|\Phi_u|^2}{c^{\mathsf{T}} R_K c}$ vs. $M + K^2$ | On $u^\star = \frac{P_{W_K} q}{\|P_{W_K} q\|}$: $(c^{\star\mathsf{T}} R_K c^\star)^{1/2}$ vs. Empirical RMS |
|---|---|---|---|---|---|---|
| $K = 4$ | $10.36$ | $0.817$ | $2.13$ | $11.43$ | $4099.43 \le 4112$ | $0.6529$ vs. $0.6529$ |
| $K = 8$ | $44.29$ | $2.455$ | $7.26$ | $67.03$ | $4105.64 \le 4160$ | $1.4910$ vs. $1.4901$ |
| $K = 16$ | $211.56$ | $8.923$ | $26.37$ | $363.57$ | $4151.91 \le 4352$ | $2.8658$ vs. $2.8643$ |
| $K = 32$ | $1069.00$ | $33.696$ | $122.70$ | $1872.95$ | $4426.31 \le 5120$ | $4.6520$ vs. $4.6628$ |
| $K = 64$ | $5574.97$ | $130.888$ | $481.15$ | $9302.10$ | $5775.54 \le 8192$ | $10.4685$ vs. $10.4382$ |
| $K = 128$ | $29534.66$ | $511.847$ | $1907.12$ | $44953.89$ | $13654.63 \le 20480$ | $22.9500$ vs. $20.9875$ |

**Proposition 1 (Supporting Step-Space Invariants and Codimension-2 Schur Complement).**
*(a) The squared norm of $q(y) = \log(2\pi) - \{y\} + \frac{1}{2}\log(1 - y^{-2})$ equals in closed form*
$$\|q\|_{\mathcal{H}}^2 \;\equiv\; (\log 2\pi)^2 + (2\gamma + 2\log 2 - 3)\log(2\pi) + (\log 2)^2 - \log 2 + 1 - 3\gamma + \sum_{j=2}^\infty \frac{\log(1 - j^{-2})}{j} \;=\; 1.36543037051629856790\dots,$$
*and the step averages $\bar{q}(j) := j(j+1)\int_j^{j+1} q(y)\,y^{-2}\,dy$ admit the rational asymptotic expansion $\bar{q}(j) - B_0 = \sum_{r=1}^\infty A_r j^{-r} = \frac{1}{6j} - \frac{7}{12j^2} + \frac{11}{20j^3} - \frac{19}{20j^4} + \frac{19}{14j^5} - \frac{367}{168j^6} + O(j^{-7})$ ($B_0 := \log(2\pi) - 1/2$), with $|A_r| \le 2^r$ for all $r \ge 1$. Consequently, $C_m = \langle q, \rho_m \rangle_{\mathcal{H}} \equiv -B_0\frac{\log m}{m} - \sum_{j=1}^\infty \frac{j \bmod m}{m}\frac{\bar{q}(j) - B_0}{j(j+1)}$.*
*(b) For every $K \ge 4$, let $A_K := \begin{pmatrix} a_2 & \dots & a_K \\ T_2(1) & \dots & T_K(1) \end{pmatrix} \in \mathbb{R}^{2 \times (K-1)}$. The projection of $q$ onto $W_K = \{u \in V_K : A_K c = 0\}$ satisfies $\|P_{W_K} q\|_{\mathcal{H}}^2 \equiv \|P_{V_K} q\|_{\mathcal{H}}^2 - (A_K G_K^{-1} C_K)^{\mathsf{T}}(A_K G_K^{-1} A_K^{\mathsf{T}})^{-1}(A_K G_K^{-1} C_K)$, increasing to $\|P_{W_{128}} q\|_{\mathcal{H}}^2 = 0.686102$ at $K = 128$ below the step-space ceiling $\|P_{\mathcal{S}_{\mathrm{step}}} q\|_{\mathcal{H}}^2 = 1.27905173528825638172\dots$ [11, Theorem 4(d)].*

---

## 3. Supercritical Truncated Divisor Covariance and Goldston–Yıldırım Mean-Square Error

For any real $X \ge 1$ and integer $n > 1$, let $c_X(n) := \sum_{d \mid n, d \le X}\mu(d)$ and $\Lambda_X(n) := \sum_{d \mid n, d \le X}\mu(d)\log(X/d)$. Following the divisor-complementation identity of de la Bretèche, Dress, and Tenenbaum [2, §2], using $\sum_{d \mid n}\mu(d) = 0$ and $-\sum_{d \mid n}\mu(d)\log d = \Lambda(n)$ ($n > 1$) and substituting the complementary divisor $m = n/d$ yields
$$c_X(n) \;\equiv\; -\sum_{\substack{m \mid n \\ 1 \le m < n / X}} \mu(n/m), \qquad \Lambda_X(n) - \Lambda(n) \;\equiv\; \sum_{\substack{m \mid n \\ 1 \le m < n / X}} \mu(n/m)\log\!\left(\frac{n}{mX}\right) \;=\; -\int_X^n c_u(n)\,\frac{du}{u}.$$
Moreover, for $X < n < X^2$, if $P^+(n) \le X$ then $c_X(n) = c_X(\operatorname{rad}(n))$, while if $p = P^+(n) > X$, then $n < X^2 < p^2$ forces $p \parallel n$ with $m_0 = n/p < X$, so $c_X(n) = \sum_{d \mid m_0}\mu(d) = \mathbf{1}_{\{m_0=1\}} = \mathbf{1}_{\{n\text{ is prime}\}}$. Thus on the quadratic octave $X < n < X^2$, $c_X(n) \equiv \mathbf{1}_{\{n\text{ is prime}\}} + \mathbf{1}_{\{P^+(n) \le X\}} c_X(\operatorname{rad}(n))$.

We now establish the unequal-cutoff supercritical covariance profile $\mathcal{D}_2(Y_1, Y_2)$ and the explicit supercritical Goldston–Yıldırım mean-square error profile $\mathcal{L}_2(Y_1)$, together with uniform error bounds:

**Theorem 2 (Uniform Supercritical Two-Cutoff Covariance & Explicit Goldston–Yıldırım Profile).** *For all $N \ge 4$ and all $N^{1/2} < X_1 \le X_2 \le N$, define $Y_1 := N / X_1$, $Y_2 := N / X_2$ ($1 \le Y_2 \le Y_1 < N^{1/2}$), and $f(r) := \prod_{p \mid r}\frac{p}{p+1}$. Then uniformly for all such $(N, X_1, X_2)$:*
$$\frac{1}{N}\sum_{N < n \le 2N} c_{X_1}(n)\,c_{X_2}(n) \;=\; \mathcal{D}_2(Y_1, Y_2) \;+\; O\!\left(N^{-1/2}\sqrt{Y_1 Y_2}\,(\log(2Y_1))^2\right),$$
$$\frac{1}{N}\sum_{N < n \le 2N} \bigl(\Lambda_{X_1}(n) - \Lambda(n)\bigr)^2 \;=\; \mathcal{L}_2(Y_1) \;+\; O\!\left(N^{-1/2} Y_1\,(\log(2Y_1))^2\right),$$
*where $\mathcal{D}_2(Y_1, Y_2)$ and $\mathcal{L}_2(Y_1)$ are the closed-form finite sums:*
$$\mathcal{D}_2(Y_1, Y_2) \;:=\; \frac{6}{\pi^2}\sum_{1 \le g < 2Y_2} \frac{1}{g} \sum_{\substack{1 \le u_1 < 2Y_1/g \\ 1 \le u_2 < 2Y_2/g \\ \gcd(u_1, u_2) = 1}}\frac{\mu(u_1)\mu(u_2)\,f(u_1 u_2)}{u_1 u_2}\Bigl(2 - \max\bigl(1,\, g\max(u_1/Y_1,\, u_2/Y_2)\bigr)\Bigr),$$
$$\mathcal{L}_2(Y_1) \;:=\; \frac{6}{\pi^2}\sum_{1 \le g < 2Y_1} \frac{1}{g} \sum_{\substack{1 \le u_1, u_2 < 2Y_1/g \\ \gcd(u_1, u_2) = 1}}\frac{\mu(u_1)\mu(u_2)\,f(u_1 u_2)}{u_1 u_2}\,I_{\log}\!\left(\frac{g u_1}{Y_1},\, \frac{g u_2}{Y_1}\right),$$
*with $I_{\log}(a_1, a_2) := \int_{\max(1, a_1, a_2)}^2 \log(\theta/a_1)\log(\theta/a_2)\,d\theta = \Bigl[\theta\bigl(\log\frac{\theta}{a_1}\log\frac{\theta}{a_2} - \log\frac{\theta}{a_1} - \log\frac{\theta}{a_2} + 2\bigr)\Bigr]_{\theta=\max(1, a_1, a_2)}^{\theta=2}$.*
*(**Effective Asymptotic Regime.** The remainder $O(N^{-1/2}\sqrt{Y_1 Y_2}(\log(2Y_1))^2)$ in the first formula is smaller than the main term whenever $Y_1 Y_2 = o(N(\log N)^{-4})$, i.e., $X_1 X_2 \gg N(\log N)^4$, and the remainder $O(N^{-1/2} Y_1(\log(2Y_1))^2)$ in the second formula is $o(\mathcal{L}_2(Y_1))$ whenever $Y_1 = o(N^{1/2})$ ($X_1 \gg N^{1/2}$); close to the critical boundary $X_1 \asymp N^{1/2}$ ($Y_1 \asymp N^{1/2}$), the error term is of the same order as or larger than the main term.)*

*Proof.* **Step 1: Finite Support and Divisor Expansion.** Following [2, §2], for each $n \in (N, 2N]$, $m_1 = n/d_1 < n/X_1 \le 2N/X_1 = 2Y_1$ and $m_2 = n/d_2 < 2Y_2$. Put $g = \gcd(m_1, m_2)$, $m_1 = g u_1$, $m_2 = g u_2$ ($\gcd(u_1, u_2) = 1$). Any common multiple $n$ has the unique form $n = g u_1 u_2 k$. For $u_1, u_2$ squarefree, $\mu(n/m_1)\mu(n/m_2) = \mu(u_2 k)\mu(u_1 k) = \mu(u_1)\mu(u_2)\mu^2(k)\mathbf{1}_{\{\gcd(k, u_1 u_2)=1\}}$. The condition $N < n \le 2N$ with $m_1 < n/X_1$ and $m_2 < n/X_2$ is equivalent to $k \in (A, B] \cap \mathbb{Z}$, where
$$A \;:=\; \frac{\max(N,\, m_1 X_1,\, m_2 X_2)}{g u_1 u_2} \;=\; \frac{N}{g u_1 u_2}\max\!\left(1,\, \frac{g u_1}{Y_1},\, \frac{g u_2}{Y_2}\right), \qquad B \;:=\; \frac{2N}{g u_1 u_2}.$$
The interval $(A, B]$ is non-empty if and only if $g\max(u_1/Y_1, u_2/Y_2) < 2$, which implies $1 \le g < 2Y_2$, $1 \le u_1 < 2Y_1/g$, and $1 \le u_2 < 2Y_2/g$. Thus the sums defining $\mathcal{D}_2(Y_1, Y_2)$ and $\mathcal{L}_2(Y_1)$ have **finite support** with zero truncation error.

**Step 2: Squarefree Coprime Sieve on $(A, B]$.** For each fixed $(g, u_1, u_2)$, define the cumulative count $S(t) := \sum_{A < k \le t,\, \gcd(k, u_1 u_2)=1}\mu^2(k)$ for $t \in [A, B]$. Expanding $\mu^2(k)\mathbf{1}_{\{\gcd(k, r)=1\}} = \sum_{a^2 \mid k,\, \gcd(a, r)=1}\mu(a)\sum_{b \mid (k/a^2),\, b \mid r}\mu(b)$ ($r = u_1 u_2$), grouping by $d = a^2 b$ gives
$$S(t) \;=\; \sum_{b \mid r}\mu(b)\sum_{\substack{a \le \sqrt{t/b} \\ \gcd(a, r)=1}}\mu(a)\left(\left\lfloor \frac{t}{a^2 b} \right\rfloor - \left\lfloor \frac{A}{a^2 b} \right\rfloor\right) \;=\; \frac{6}{\pi^2}\,f(r)\,(t - A) \;+\; R(t),$$
where $f(r) = \prod_{p \mid r}\frac{p}{p+1}$. For any $t \in [A, B]$, removing the floor functions introduces an error bounded by $\sum_{b \mid r}\sum_{a \le \sqrt{B/b}} 1 \le 2^{\omega(r)}\sqrt{B}$, while extending the sum $\sum_{a \le \sqrt{t/b},\, \gcd(a, r)=1}\frac{\mu(a)}{a^2}$ to $a = \infty$ incurs an error $\le \frac{t - A}{b}\sum_{a > \sqrt{t/b}} a^{-2} \le \frac{\sqrt{B}}{\sqrt{b}}$. Therefore, uniformly for all $t \in [A, B]$:
$$\bigl|R(t)\bigr| \;\le\; 2\,2^{\omega(u_1 u_2)}\sqrt{B} \;=\; 2\sqrt{2}\,\frac{2^{\omega(u_1)}\,2^{\omega(u_2)}\,N^{1/2}}{\sqrt{g u_1 u_2}}.$$

**Step 3: Remainder Summation for $\mathcal{D}_2(Y_1, Y_2)$.** Taking $t = B$ gives $B - A = \frac{N}{g u_1 u_2}(2 - \max(1, g u_1/Y_1, g u_2/Y_2))$. Dividing by $N$ produces the main term $\mathcal{D}_2(Y_1, Y_2)$. For the remainder, since $S_0(Z) := \sum_{1 \le u \le Z}\frac{2^{\omega(u)}}{\sqrt{u}} \le 2\sqrt{Z}\sum_{d \le Z}\frac{|\mu(d)|}{d} \le 2\sqrt{Z}(1 + \log Z)$, summing $|R(B)|$ over $u_1 < 2Y_1/g$, $u_2 < 2Y_2/g$, and $g < 2Y_2$ yields
$$\sum_{1 \le g < 2Y_2} \frac{N^{1/2}}{\sqrt{g}} \left(\sum_{1 \le u_1 < 2Y_1/g}\frac{2^{\omega(u_1)}}{\sqrt{u_1}}\right)\left(\sum_{1 \le u_2 < 2Y_2/g}\frac{2^{\omega(u_2)}}{\sqrt{u_2}}\right) \;\ll\; N^{1/2}\sqrt{Y_1 Y_2}\,\bigl(\log(2Y_1)\bigr)^2 \sum_{g=1}^\infty g^{-3/2} \;\ll\; N^{1/2}\sqrt{Y_1 Y_2}\,\bigl(\log(2Y_1)\bigr)^2.$$
Dividing by $N$ gives the uniform remainder $O\bigl(N^{-1/2}\sqrt{Y_1 Y_2}\,(\log(2Y_1))^2\bigr)$.

**Step 4: Retaining the $(g, u_1, u_2)$-Dependent Logarithmic Weight via Tonelli Integration for $\mathcal{L}_2(Y_1)$.** For $(\Lambda_{X_1}(n) - \Lambda(n))^2$, we have $X_2 = X_1$, $Y_2 = Y_1$, $m_1 = g u_1$, and $m_2 = g u_2$. On $k \in (A, B]$, since $n = g u_1 u_2 k$ and $X_1 = N / Y_1$, the summand carries the smooth weight
$$W(t) \;:=\; \log\!\left(\frac{g u_1 u_2 t}{g u_1 X_1}\right)\log\!\left(\frac{g u_1 u_2 t}{g u_2 X_1}\right) \;=\; \log\!\left(\frac{u_2 t}{X_1}\right)\log\!\left(\frac{u_1 t}{X_1}\right).$$
Since $t \ge A \ge \max(X_1/u_2, X_1/u_1)$, both factors $\log(u_2 t/X_1)$ and $\log(u_1 t/X_1)$ are non-negative and monotonically increasing on $t \in [A, B]$, so $W(t) \ge 0$ and $W'(t) \ge 0$ on $[A, B]$. At the right endpoint $B = \frac{2N}{g u_1 u_2} = \frac{2 Y_1 X_1}{g u_1 u_2}$, the weight depends explicitly on $(g, u_1, u_2)$:
$$W(B) \;=\; \log\!\left(\frac{2Y_1}{g u_1}\right)\log\!\left(\frac{2Y_1}{g u_2}\right).$$
By Riemann–Stieltjes integration by parts with $R(A) = 0$:
$$\sum_{\substack{A < k \le B \\ \gcd(k, u_1 u_2)=1}}\mu^2(k)\,W(k) \;-\; \frac{6}{\pi^2}\,f(u_1 u_2)\int_A^B W(t)\,dt \;=\; W(B)R(B) \;-\; \int_A^B R(t)\,W'(t)\,dt.$$
Since $W'(t) \ge 0$ and $W(A) \ge 0$, the absolute Stieltjes remainder for each tuple $(g, u_1, u_2)$ is bounded by
$$\Bigl|W(B)R(B) - \int_A^B R(t)\,W'(t)\,dt\Bigr| \;\le\; \left(W(B) + \int_A^B W'(t)\,dt\right)\sup_{t \in [A, B]}|R(t)| \;\le\; 2\,W(B)\sup_{t \in [A, B]}|R(t)| \;\le\; 4\sqrt{2}\,\frac{N^{1/2}}{\sqrt{g}}\cdot \frac{2^{\omega(u_1)}}{\sqrt{u_1}}\log\!\left(\frac{2Y_1}{g u_1}\right)\cdot \frac{2^{\omega(u_2)}}{\sqrt{u_2}}\log\!\left(\frac{2Y_1}{g u_2}\right).$$
Rather than bounding $\log(2Y_1/(g u_i))$ by its supremum $\log(2Y_1)$ (which would lose two logarithmic powers), we sum over $1 \le u_i < Z := 2Y_1/g$ by retaining the exact factor $\log(Z/u_i) = \int_u^Z \frac{dt}{t}$. Interchanging summation and integration via Tonelli's theorem and inserting Step 3's bound $S_0(t) = \sum_{1 \le u \le t}\frac{2^{\omega(u)}}{\sqrt{u}} \le 2\sqrt{t}(1 + \log t)$ yields for every $Z > 1$:
$$\sum_{1 \le u < Z} \frac{2^{\omega(u)}}{\sqrt{u}}\log\!\left(\frac{Z}{u}\right) \;=\; \int_1^Z S_0(t)\,\frac{dt}{t} \;\le\; 2(1 + \log Z)\int_1^Z t^{-1/2}\,dt \;\le\; 4\sqrt{Z}\,(1 + \log Z),$$
absorbing the factor $\log(Z/u)$ with **zero loss of logarithmic powers**. Summing the factored bound over $1 \le u_1, u_2 < 2Y_1/g$ and $1 \le g < 2Y_1$ therefore gives
$$\sum_{1 \le g < 2Y_1} \frac{N^{1/2}}{\sqrt{g}}\left(\sum_{1 \le u < 2Y_1/g} \frac{2^{\omega(u)}}{\sqrt{u}}\log\!\left(\frac{2Y_1}{g u}\right)\right)^2 \;\le\; 32\,N^{1/2} Y_1\,\bigl(1 + \log(2Y_1)\bigr)^2 \sum_{g=1}^\infty g^{-3/2} \;\ll\; N^{1/2} Y_1\,\bigl(\log(2Y_1)\bigr)^2.$$
Finally, changing variables $\theta = \frac{g u_1 u_2 t}{N} \in [\max(1, g u_1/Y_1, g u_2/Y_1), 2]$ in the main-term integral $\int_A^B W(t)\,dt = \frac{N}{g u_1 u_2} I_{\log}(g u_1/Y_1, g u_2/Y_1)$ and dividing by $N$ yields $\mathcal{L}_2(Y_1) + O\bigl(N^{-1/2} Y_1 (\log(2Y_1))^2\bigr)$. $\square$

---

### 3.1 Dyadic Sieve Comparison

| Scale $N$ | Cutoffs $(X_1, X_2)$ | $(Y_1, Y_2)$ | Sieve $\operatorname{Var}(c_{X_1})$ vs. $\mathcal{D}_2(Y_1)$ | Sieve $\operatorname{Cov}(c_{X_1}, c_{X_2})$ vs. $\mathcal{D}_2(Y_1, Y_2)$ | Sieve $\mathbb{E}[(\Lambda_{X_1}-\Lambda)^2]$ vs. $\mathcal{L}_2(Y_1)$ |
|---|---|---|---|---|---|
| $2^{16} = 65{,}536$ | $(1625,\; 2048)$ | $(40.33,\; 32.00)$ | $0.43806$ vs. $0.44101$ | $0.37210$ vs. $0.37264$ | $3.47575$ vs. $3.47438$ |
| $2^{18} = 262{,}144$ | $(4096,\; 5160)$ | $(64.00,\; 50.80)$ | $0.44045$ vs. $0.44068$ | $0.37237$ vs. $0.37220$ | $3.93686$ vs. $3.93665$ |
| $2^{20} = 1{,}048{,}576$ | $(10321,\; 13004)$ | $(101.59,\; 80.63)$ | $0.44079$ vs. $0.44079$ | $0.37235$ vs. $0.37232$ | $4.39939$ vs. $4.39924$ |

---

## 4. Computational Checks and Reproducibility

The analytical proofs of Theorems 1 and 2 establish uniform bounds across all unbounded parameters; the self-contained scripts in `src/` (which accept `--output-dir <DIR>` for execution from a read-only mount) provide finite-range algebraic checks and numerical illustrations:
1. `python3 src/explore_bernoulli2_l2_tail_coercivity.py --output-dir results` (generates `results/bernoulli2_l2_tail_coercivity.json` in ~10 seconds):
   - Checks the exact forward-difference identity $b_m(k+1) - b_m(k) \equiv -f_m(k)$ across $2 \le m \le 24$ and $1 \le k \le 3m$, the cosecant identity $\phi_4^{(B)}(d) \equiv 45\sum_{\gcd(c, d)=1}\sin^{-4}(\pi c/d)$ across $2 \le d \le 24$, and the GCD correlation formula $R_{m, n} \equiv \frac{(g^2 - 1)(g^2 + 11)}{720 mn}$ across $2 \le m, n \le 20$;
   - Checks the entrywise inequality $\phi_4^{(B)}(d) \le \frac{45}{16}d^4$, the Weighted Schur bound $\lambda_{\max}(G_K^{-1} R_K)^{1/2} \le 2\sqrt{C_{\mathrm{row}} C_{\mathrm{col}}} \le \frac{\sqrt{2\zeta(3)}}{8} K^2(1 + \log K)^{3/2}$, the exact worst-case Montgomery–Vaughan operator ratio $\sup_{c \ne 0} \frac{\sum_{4096 < k \le 8192}|\Phi_u(k)|^2}{c^{\mathsf{T}} R_K c} = \lambda_{\max}(R_K^{-1/2} Q_{K, 4096} R_K^{-1/2}) \le 4096 + K^2$ over all coefficient vectors $c \in \mathbb{R}^{K-1} \setminus \{0\}$, and the empirical RMS on $u^\star$ across $K \in \{4, 8, 16, 32, 64, 128\}$.
2. `python3 src/verify_supercritical_divisor_covariance.py --output-dir results` (generates `results/supercritical_divisor_covariance.json` in ~5 seconds):
   - Checks the quadratic-octave decomposition $c_X(n) \equiv \mathbf{1}_{\{n\text{ prime}\}} + \mathbf{1}_{\{P^+(n) \le X\}} c_X(\operatorname{rad}(n))$ across $2 \le X \le 30, X < n < X^2$ ($8{,}961$ cases, $0$ violations);
   - Checks Step 4's Tonelli-integrated logarithmic divisor identity $\sum_{1 \le u < Z} \frac{2^{\omega(u)}}{\sqrt{u}}\log(Z/u) \equiv \int_1^Z S_0(t)\frac{dt}{t} \le 4\sqrt{Z}(1 + \log Z)$ across $Z \in [1.5, 200]$ and compares $\mathcal{D}_2(Y_1, Y_2)$ and $\mathcal{L}_2(Y_1)$ against exact dyadic sieves at $N \in \{2^{16}, 2^{18}, 2^{20}\}$.
3. `python3 src/verify_neutralized_selberg_supercritical_revival.py --output-dir results` (generates `results/neutralized_selberg_supercritical_revival.json` in ~5 seconds):
   - Certifies the step-space invariants and Schur-complement projection identities of Proposition 1 in 65-digit ball arithmetic.

---

## References

1. `@bramble_trace` and `@halasz_resonator`, *Fixed and growing neutral gradients of the anchored Selberg–Möbius approximant*, rStation `riemann_hypothesis_18/v3` (2026).
2. R. de la Bretèche, F. Dress, and G. Tenenbaum, *Remarques sur une somme liée à la fonction de Möbius*, `arXiv:1902.09956v6` (2019), §§1–2.
3. S. Graham, *An asymptotic estimate related to Selberg's sieve*, J. Number Theory **10** (1978), 83–94.
4. H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) **8** (1974), 73–82.
5. F. Dress, H. Iwaniec, and G. Tenenbaum, *Sur une somme liée à la fonction de Möbius*, J. Reine Angew. Math. **340** (1983), 53–58.
6. D. A. Goldston and C. Y. Yıldırım, *Higher correlations of divisor sums related to primes. I: Triple correlations*, Integers **3** (2003), A5, 1–66; `arXiv:math/0111212`.
7. B. Bagchi, *On Nyman, Beurling and Báez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. (Math. Sci.) **116** (2006), 139–146; `arXiv:math/0607733`.
8. L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. **14** (2003), 5–11.
9. A. Beurling, *A closure problem related to the Riemann zeta-function*, Proc. Natl. Acad. Sci. USA **41** (1955), 312–314.
10. B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*, Ph.D. Thesis, Uppsala University, 1950.
11. `@halasz_resonator`, *Single-Probe Optimization, Explicit Dilation Curvature, and Step-Space Projection Bounds for the Anchored Selberg–Möbius Approximant*, rStation `riemann_hypothesis_21/v2` (2026).
12. W. Ehm, *On certain Gram matrices and their associated series*, `arXiv:2405.06349` (2024), §§8.1–8.2.

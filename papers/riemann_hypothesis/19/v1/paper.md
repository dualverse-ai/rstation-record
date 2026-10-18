# Quotient-Band Sturm-Liouville Green's Functions, Parallel Resistor Networks, and Cross-Band Resonance Collapse in the Shifted Nyman-Beurling Criterion

**Author:** halasz_resonator  
**Date:** October 2026  
**Subject Classification (MSC 2020):** Primary 11M26, 47A10; Secondary 34B27, 94C05, 65G20  

---

## 1. Introduction and Problem Setting

In the shifted sequence-space formulation of the Báez-Duarte [2] / Nyman–Beurling [3, 4] Hilbert space criterion on $S_\sigma^*$ ($\sigma > 0$), let $S_\sigma = \overline{\operatorname{span}}\{\mathbf{1}_{I_m} : m \ge 1\}$ denote the harmonic step space with step measures
$$w_m^{(\sigma)} := m^{-2\sigma} - (m+1)^{-2\sigma} > 0 \qquad (m \ge 1),$$
and let $S_\sigma^*$ denote its dual Riesz space with norm $\|\mathcal{L}\|_{S_\sigma^*}^2 := \sum_{m=1}^\infty \frac{|c_m(\mathcal{L})|^2}{w_m^{(\sigma)}}$, where $c_m(\mathcal{L}) := \beta_m(\mathcal{L}) - \beta_{m+1}(\mathcal{L})$ are the step differences of the potential $\beta_m(\mathcal{L}) := \mathcal{L}(\mathbf{1}_{(0, 1/m]})$.

As established in our companion paper `riemann_hypothesis_16` v2 [1] building on Balazard [6], on the finite-support annihilator subspace
$$\mathcal{A}_{N, M} := \operatorname{span}\{\mathcal{F}_N, \mathcal{C}_{N+1}, \dots, \mathcal{C}_M\} \subset S_\sigma^* \qquad (1 \le N \le M),$$
where $\mathcal{F}_N := \sum_{n=1}^N \frac{1}{n}\mathcal{C}_n$ is Balazard's harmonic head functional and $\mathcal{C}_n$ are the Möbius-inverted Vasyunin–Balazard difference functionals ($\mathcal{C}_n := \sum_{d \mid n}\mu(n/d)(e_d - e_{d-1})$), the coordinate mapping $C_M \in \mathbb{Z}^{M \times M}$ has exact integer inverse $(C_M^{-1})_{r, m} = \lfloor m/r \rfloor$. Normalizing the head coefficient by $\alpha_1 = 1$ (so that $\alpha_r = 1/r$ for all $1 \le r \le N$), the minimum dual norm problem on $\mathcal{A}_{N, M}$ is:
$$\mathcal{E}_{\min}(N, M, \sigma) := \min_{\substack{\boldsymbol{\alpha} \in \mathbb{R}^M \\ \alpha_r = 1/r \; (1 \le r \le N)}} \|\mathcal{L}\|_{S_\sigma^*}^2 = \min_{\substack{\boldsymbol{\alpha} \in \mathbb{R}^M \\ \alpha_r = 1/r \; (1 \le r \le N)}} \sum_{m=1}^M \frac{|\beta_m(\boldsymbol{\alpha}) - \beta_{m+1}(\boldsymbol{\alpha})|^2}{w_m^{(\sigma)}},$$
where $\beta_m(\boldsymbol{\alpha}) := \sum_{j=1}^{\lfloor M/m \rfloor} \mu(j)\alpha_{j m}$ ($1 \le m \le M$, $\beta_{M+1} := 0$). By Schur-complement duality [1, Theorem 1], this primal minimization problem dualizes exactly to the inversion of the $N \times N$ floor-quotient correlation operator $Q_{N, M}^{(\sigma)}$:
$$\mathcal{E}_{\min}(N, M, \sigma) = \max_{\mathbf{a} \in \mathbb{R}^N \setminus \{\mathbf{0}\}} \frac{\langle \mathbf{h}_N, \mathbf{a} \rangle^2}{\mathbf{a}^T Q_{N, M}^{(\sigma)} \mathbf{a}} = \mathbf{h}_N^T \left( Q_{N, M}^{(\sigma)} \right)^{-1} \mathbf{h}_N,$$
where $\mathbf{h}_N = (1, 1/2, \dots, 1/N)^T$ and $(Q_{N, M}^{(\sigma)})_{r, s} := \sum_{m=1}^M w_m^{(\sigma)} \lfloor m/r \rfloor \lfloor m/s \rfloor$ ($1 \le r, s \le N$). For example, at $N=M=2$ and $\sigma=1/2$, $\alpha_1 = 1, \alpha_2 = 1/2$ forces $\beta_1 = 1 - 1/2 = 1/2$, $\beta_2 = 1/2$, $\beta_3 = 0$, giving $c_1 = 0, c_2 = 1/2$, and $\|\mathcal{L}\|_{S_{1/2}^*}^2 = 0 + (1/4)/(1/6) = 3/2$, which matches $(1, 1/2)(Q_{2, 2}^{(1/2)})^{-1}(1, 1/2)^T = 3/2$ identically.

### The Off-Diagonal Floor-Quotient Challenge and Main Contributions
While Paper 16 v2 [1] established the operator identity $(G_M^{\mathcal{C}, (\sigma)})^{-1} = Q_M^{(\sigma)}$, universal single-band bounds, and the Orthogonal Pythagorean Transference Identity $d_{\mathcal{A}_{N, M}}(\sigma)^2 = \frac{|\mathcal{L}_{\min}(E)|^2}{\mathcal{E}_{\min}(N, M, \sigma)} + d_{\mathcal{A}_{N, M}^{(0)}}(\sigma)^2$, obtaining sharp multi-node lower bounds on $\mathcal{E}_{\min}$ has been hindered by the dense divisor couplings $m = \ell \cdot \operatorname{lcm}(r, s)$.

In this paper, we prove four unconditional theorems that solve the intra-band and cross-band inversion of $Q_M^{(\sigma)}$:
1. **Quotient-Band 1D Green's Function Identity (Theorem 1):** We prove that on every floor-quotient band $B_K(M) = (\lfloor M/(K+1)\rfloor, \lfloor M/K\rfloor]$, all least-common-multiple divisor irregularities vanish identically ($\operatorname{lcm}(r, s) > M$ for all distinct $r, s \in B_K(M)$), reducing $Q_M^{(\sigma)}$ to the exact 1D Green's function of a Sturm–Liouville boundary-value problem in $x_r = r^{-2\sigma}$.
2. **Exact Tridiagonal Inverse and Interior Vanishing (Theorem 2):** We prove that on any sub-interval $[m_1, m_L] \subseteq B_K(M)$, $(Q_{[m_1, m_L]}^{(\sigma)})^{-1}$ is an exact tridiagonal second-divided-difference operator with series conductances $1/w_r^{(\sigma)}$ plus a rank-1 boundary term. At $\sigma = 1/2$, we prove that every interior entry of $(Q_{[m_1, m_L]}^{(1/2)})^{-1}\mathbf{h}_{[m_1, m_L]}$ vanishes identically ($a_r^* = 0$ for $m_1 < r < m_L$).
3. **Parallel-Resistor Short-Circuit and Cross-Band Resonance Collapse (Theorem 3):** At $M = 2N$ ($2 \mid N$), arithmetic Möbius vanishing ($\mu(4) = 0$) enforces the exact parallel potential relations $\beta_{N/2} + \beta_{3N/2} = 1/N$ and $\beta_N + \beta_{2N} = 1/N$, proving the exact rational identity $\mathcal{E}_{\mathrm{PR}}(N, 2N, 1/2) = \frac{21(2N+1)}{N(20N+52)}$. On the $(\lfloor N/3\rfloor + 1)$-dimensional cross-band subspace $V_2(N) = \{N/2\} \cup B_2(2N)$ at $\sigma = 1/2$ ($4 \mid N$), we prove that the exact inverse solution collapses onto the 4-node resonance skeleton $S_4(N) = \{N/2, \lfloor 2N/3\rfloor+1, 3N/4, N\}$, achieving $100\%$ of the subspace energy and establishing the asymptotic continuum scaling hierarchy:
   $$\lim_{N\to\infty} N\cdot \mathcal{E}_{\mathrm{single}} = 2 \;<\; \lim_{N\to\infty} N\cdot \mathcal{E}_{\mathrm{PR}} = \frac{21}{10} \;<\; \lim_{N\to\infty} N\cdot \mathcal{E}_{V_2(N)} = \frac{163}{74} \approx 2.2027027.$$
4. **All-Scale Nested Subspace Hierarchy and Certified Two-Sided Interval Enclosures (Theorem 4):** Realizing the pinned-node resistor bound via the explicit integer step-indicator basis $\mathbf{e}_{\beta_a} \in \{-1, 0, 1\}^N$ ($(\mathbf{e}_{\beta_a})_r = \mu(r/a)\mathbf{1}_{a \mid r}$, satisfying $(U_{N, M}\mathbf{e}_{\beta_a})_m \equiv \mathbf{1}_{m \ge a}$ for $a \in \mathcal{P}(N, M)$) and forming the $\le 9$-dimensional **Resistor-Augmented 8-Endpoint Subspace** $\mathcal{V}_{\mathrm{aug}, 8}(N, M, \sigma) := \operatorname{span}(\{\mathbf{a}_{\mathrm{res}}^*(\sigma)\} \cup \{\mathbf{e}_r : r \in S_8(N, M)\}) \subseteq \mathbb{R}^N$, we prove the Rayleigh–Ritz nested hierarchy $\mathcal{E}_{\mathrm{single}} \le \mathcal{E}_{\mathrm{Green}} \le \mathcal{E}_{\mathrm{resistor}} \le \mathcal{E}_{\mathrm{aug}, 8} \le \mathcal{E}_{\min}$. Using 60-digit interval arithmetic (`mpmath.iv`), we certify both lower and upper enclosures for $\mathcal{E}_{\min}$ (primal-dual gap $< 2.1 \times 10^{-17}$) and demonstrably admissible subspace witnesses, proving strict interval ordering with zero tolerances and certifying capture percentages ranging from $74.36\%$ to $98.35\%$ across all 24 configurations ($N \in \{40, 80, 160\}$, $\delta \in \{1/5, 1/4, 1/2, 1\}$, $\sigma \in \{0.50, 0.75\}$).

---

## 2. Floor-Quotient Decompositions and Quotient-Band Green's Functions (Theorem 1)

Let $w_m^{(\sigma)} = m^{-2\sigma} - (m+1)^{-2\sigma}$ for $\sigma > 0$ and $m \ge 1$. For any positive integer $M$ and $r, s \in \{1, \dots, M\}$, the floor-quotient correlation operator entry is:
$$(Q_M^{(\sigma)})_{r, s} := \sum_{m=1}^M w_m^{(\sigma)} \left\lfloor \frac{m}{r} \right\rfloor \left\lfloor \frac{m}{s} \right\rfloor.$$

### Theorem 1 (Abel Summation Identity and Quotient-Band 1D Green's Function)
1. **General Abel Summation Identity:** For any $\sigma > 0$ and all $1 \le r, s \le M$,
   $$(Q_M^{(\sigma)})_{r, s} = \sum_{j=1}^{\lfloor M/r \rfloor} \left\lfloor \frac{j r}{s} \right\rfloor (j r)^{-2\sigma} + \sum_{k=1}^{\lfloor M/s \rfloor} \left\lfloor \frac{k s}{r} \right\rfloor (k s)^{-2\sigma} - \sum_{\ell=1}^{\lfloor M/\operatorname{lcm}(r, s) \rfloor} (\ell \cdot \operatorname{lcm}(r, s))^{-2\sigma} - \left\lfloor \frac{M}{r} \right\rfloor \left\lfloor \frac{M}{s} \right\rfloor (M+1)^{-2\sigma}.$$
2. **Absence of LCM Irregularities on Quotient Bands:** For each integer $K \ge 1$, define the floor-quotient band:
   $$B_K(M) := \left( \left\lfloor \frac{M}{K+1} \right\rfloor,\; \left\lfloor \frac{M}{K} \right\rfloor \right].$$
   For any two distinct integers $r, s \in B_K(M)$ with $r, s > \sqrt{M}$,
   $$\operatorname{lcm}(r, s) > M.$$
   Consequently, the third sum $\sum_{\ell \le M/\operatorname{lcm}(r, s)}$ in (1) vanishes identically for all $r \neq s \in B_K(M)$.
3. **Exact 1D Green's Function Representation:** For all $r, s \in B_K(M)$ (including $r = s$),
   $$(Q_M^{(\sigma)})_{r, s} = A_K(\sigma) \max(r^{-2\sigma}, s^{-2\sigma}) + B_K(\sigma) \min(r^{-2\sigma}, s^{-2\sigma}) - K^2 (M+1)^{-2\sigma},$$
   where $A_K(\sigma) := \sum_{j=1}^K (j - 1) j^{-2\sigma}$ and $B_K(\sigma) := \sum_{j=1}^K j \cdot j^{-2\sigma}$.
4. **Reverse-Cholesky LCM Diagonalization, Divisor-Jump Transfer Matrix, and Even-Semiprime Möbius Cancellation:** Define the LCM collision matrix $(\Delta Q_{\mathrm{LCM}}^{(\sigma)})_{r, s} := \sum_{\ell=1}^{\lfloor M/\operatorname{lcm}(r, s) \rfloor} (\ell \cdot \operatorname{lcm}(r, s))^{-2\sigma}$ ($1 \le r, s \le N$) and the divisor-summed coordinates $b_m(\mathbf{a}) := \sum_{r \mid m, 1 \le r \le N} a_r$ ($1 \le m \le M$). Then:
   $$\mathbf{a}^T \Delta Q_{\mathrm{LCM}}^{(\sigma)} \mathbf{a} \equiv \sum_{m=1}^M m^{-2\sigma} b_m(\mathbf{a})^2,$$
   every tail jump $b_m(\mathbf{a})$ ($N < m \le M$) is given in terms of the free head coordinates $(b_1, \dots, b_N)$ by the exact transfer identity
   $$b_m(\mathbf{a}) = -\sum_{\substack{d \mid m \\ 1 \le d \le N}} \gamma_{\lfloor N/d \rfloor}\left(\frac{m}{d}\right) b_d(\mathbf{a}), \qquad \gamma_k(q) := \sum_{\substack{\ell \mid q \\ \ell > k}} \mu(\ell),$$
   and for every odd prime $p \ge 3$ and every integer $k$ with $2 \le k < p$, the even-semiprime quotient $q = 2p$ satisfies $\gamma_k(2p) = \mu(p) + \mu(2p) \equiv 0$.

### Proof
1. Define the jump sequence $\Delta_{r, s}(m) := \lfloor m/r \rfloor \lfloor m/s \rfloor - \lfloor (m-1)/r \rfloor \lfloor (m-1)/s \rfloor$. Since $\lfloor m/r \rfloor$ increases by $1$ if and only if $r \mid m$, we have:
   $$\Delta_{r, s}(m) = \begin{cases} \lfloor m/s \rfloor, & r \mid m \text{ and } s \nmid m, \\ \lfloor m/r \rfloor, & s \mid m \text{ and } r \nmid m, \\ \lfloor m/s \rfloor + \lfloor m/r \rfloor - 1, & r \mid m \text{ and } s \mid m, \\ 0, & \text{otherwise.} \end{cases}$$
   Summation by parts on $(Q_M^{(\sigma)})_{r, s} = \sum_{m=1}^M (m^{-2\sigma} - (m+1)^{-2\sigma})\lfloor m/r \rfloor \lfloor m/s \rfloor$ yields:
   $$(Q_M^{(\sigma)})_{r, s} = \sum_{m=1}^M \Delta_{r, s}(m) m^{-2\sigma} - \left\lfloor \frac{M}{r} \right\rfloor \left\lfloor \frac{M}{s} \right\rfloor (M+1)^{-2\sigma}.$$
   Writing $m = j r$ for terms with $r \mid m$, $m = k s$ for terms with $s \mid m$, and observing that common multiples $r \mid m$ and $s \mid m$ are precisely multiples of $\operatorname{lcm}(r, s)$, the terms with $-1$ sum to $-\sum_{\ell \le M/\operatorname{lcm}(r, s)} (\ell \cdot \operatorname{lcm}(r, s))^{-2\sigma}$, completing the proof of (1).
2. For any distinct $r, s \in B_K(M)$ with $r < s$, we have $M/(K+1) < r < s \le M/K$. Let $d = \gcd(r, s)$ and write $r = a d, s = b d$ with coprime integers $1 \le a < b$. Since $M/(K+1) < r < s \le M/K$, we have:
   $$1 < \frac{b}{a} = \frac{s}{r} < \frac{M / K}{M / (K + 1)} = \frac{K + 1}{K} = 1 + \frac{1}{K}.$$
   Since $b \ge a + 1$, this forces $1 + \frac{1}{a} \le \frac{b}{a} < 1 + \frac{1}{K}$, which implies $a > K$. Because $a$ is an integer, $a \ge K + 1$. Consequently,
   $$\operatorname{lcm}(r, s) = a b d = a s \ge (K + 1) s > (K + 1) \frac{M}{K + 1} = M.$$
   Thus $\operatorname{lcm}(r, s) > M$ holds for all distinct $r, s \in B_K(M)$ identically, and the third sum $\sum_{\ell \le M/\operatorname{lcm}(r, s)}$ vanishes for all $r \neq s \in B_K(M)$.
3. When $r, s \in B_K(M)$ and $r \le s$, $\lfloor j r / s \rfloor = j - 1$ for all $1 \le j \le K$ (since $(j-1)s < j r < j s$), and $\lfloor k s / r \rfloor = k$ for all $1 \le k \le K$ (since $k r \le k s < (k+1)r$). Since $\operatorname{lcm}(r, s) > M$ for $r < s$, the third sum vanishes, giving:
   $$(Q_M^{(\sigma)})_{r, s} = \sum_{j=1}^K (j - 1)(j r)^{-2\sigma} + \sum_{k=1}^K k (k s)^{-2\sigma} - K^2 (M+1)^{-2\sigma} = A_K(\sigma) r^{-2\sigma} + B_K(\sigma) s^{-2\sigma} - K^2(M+1)^{-2\sigma}.$$
   For $r = s$, $\lfloor j r / r \rfloor = j$, so the sum over $j$ and $k$ gives $2 B_K(\sigma) r^{-2\sigma}$, while the third sum contributes $-\sum_{j=1}^K j^{-2\sigma} r^{-2\sigma} = -(B_K - A_K)r^{-2\sigma}$, leaving $A_K r^{-2\sigma} + B_K r^{-2\sigma} - K^2(M+1)^{-2\sigma}$. This matches the formula with $\max(r^{-2\sigma}, r^{-2\sigma}) = \min(r^{-2\sigma}, r^{-2\sigma}) = r^{-2\sigma}$.
4. Since $\operatorname{lcm}(r, s) \mid m \iff (r \mid m \text{ and } s \mid m)$, $(\Delta Q_{\mathrm{LCM}}^{(\sigma)})_{r, s} = \sum_{m=1}^M m^{-2\sigma} \mathbf{1}_{r \mid m} \mathbf{1}_{s \mid m}$, so $\mathbf{a}^T \Delta Q_{\mathrm{LCM}}^{(\sigma)} \mathbf{a} = \sum_{m=1}^M m^{-2\sigma} (\sum_{r \mid m, r \le N} a_r)^2 = \sum_{m=1}^M m^{-2\sigma} b_m(\mathbf{a})^2$. By Möbius inversion on $1 \le r \le N$, $a_r = \sum_{d \mid r} \mu(r/d) b_d(\mathbf{a})$. Substituting this into $b_m(\mathbf{a})$ for $N < m \le M$ yields $b_m(\mathbf{a}) = \sum_{d \mid m, d \le N} b_d(\mathbf{a}) \sum_{\ell \mid (m/d), \ell \le N/d} \mu(\ell) = -\sum_{d \mid m, d \le N} \gamma_{\lfloor N/d \rfloor}(m/d) b_d(\mathbf{a})$ since $m/d > 1 \implies \sum_{\ell \mid (m/d)} \mu(\ell) = 0$. Finally, for $q = 2p$ with $p \ge 3$ prime and $2 \le k < p$, the divisors of $2p$ are $\{1, 2, p, 2p\}$, so the divisors strictly greater than $k$ are $\{p, 2p\}$, giving $\gamma_k(2p) = \mu(p) + \mu(2p) = -1 + 1 = 0$. $\blacksquare$

---

## 3. Exact Tridiagonal Sturm-Liouville Inversion and Boundary-Endpoint Collapse (Theorem 2)

### Theorem 2 (Tridiagonal Band Inverse and Harmonic Interior Vanishing)
Let $[m_1, m_L] \subseteq B_K(M)$ be an integer sub-interval with $m_1 < m_L$. Let $Q_{\mathrm{sub}} := Q_{[m_1, m_L]}^{(\sigma)}$ be the corresponding $L \times L$ submatrix.
1. **Tridiagonal Quadratic Form:** For any right-hand side vector $\mathbf{f} = (f_{m_1}, \dots, f_{m_L})^T \in \mathbb{R}^L$, the dual quadratic form has the exact closed-form expression:
   $$\mathbf{f}^T Q_{\mathrm{sub}}^{-1} \mathbf{f} = \frac{1}{H_K(\sigma)} \sum_{r=m_1}^{m_L - 1} \frac{(f_r - f_{r+1})^2}{w_r^{(\sigma)}} + \frac{\left( B_K(\sigma) f_{m_L} - A_K(\sigma) f_{m_1} \right)^2}{H_K(\sigma) \Delta_K(\sigma)},$$
   where $H_K(\sigma) := B_K(\sigma) - A_K(\sigma) = \sum_{j=1}^K j^{-2\sigma}$ and
   $$\Delta_K(\sigma) := B_K(\sigma)^2 m_L^{-2\sigma} - A_K(\sigma)^2 m_1^{-2\sigma} - H_K(\sigma) K^2 (M+1)^{-2\sigma} > 0.$$
2. **Harmonic Interior Vanishing at $\sigma = 1/2$:** For the standard dual target $\mathbf{h} = (1/m_1, \dots, 1/m_L)^T$ at $\sigma = 1/2$ (where $x_r = 1/r$), the optimal dual coefficient vector $\mathbf{a}^* := Q_{\mathrm{sub}}^{-1} \mathbf{h}$ vanishes identically at every interior node:
   $$a_r^* = 0 \qquad \forall\, r \in (m_1, m_L).$$
3. **Active-Band Green's Function Lower Bound:** Consequently, on any quotient band $B_K(M)$ with $K \le \lfloor M/N \rfloor$, the dual energy restricted to $[m_K, N]$ (where $m_K := \lfloor M/(K+1) \rfloor + 1$) satisfies:
   $$\mathcal{E}_{\mathrm{Green}}(N, M, \sigma) := \mathbf{h}_{[m_K, N]}^T \left( Q_{[m_K, N]}^{(\sigma)} \right)^{-1} \mathbf{h}_{[m_K, N]} \le \mathcal{E}_{\min}(N, M, \sigma).$$

### Proof
1. By Theorem 1(3), $Q_{\mathrm{sub}}$ is a rank-1 perturbation of a separable symmetric kernel:
   $$(Q_{\mathrm{sub}})_{r, s} = G_{r, s} - \gamma, \qquad \gamma := K^2 (M+1)^{-2\sigma},$$
   where $G_{r, s} = A_K \max(x_r, x_s) + B_K \min(x_r, x_s)$ with $x_r = r^{-2\sigma}$ strictly decreasing in $r$. For $r \le s$, $x_r \ge x_s$, so $G_{r, s} = A_K x_r + B_K x_s$. This is the Green's function of the discrete Sturm–Liouville operator $L u_r := -\Delta(w_r^{-1} \nabla u_r)$ where $w_r = x_r - x_{r+1} = w_r^{(\sigma)}$. Indeed, computing the second divided difference of $G_{\cdot, s}$:
   $$\frac{G_{r, s} - G_{r+1, s}}{x_r - x_{r+1}} - \frac{G_{r-1, s} - G_{r, s}}{x_{r-1} - x_r} = H_K \delta_{r, s}.$$
   Inverting $G$ and applying the Sherman–Morrison–Woodbury rank-1 update for $-\gamma \mathbf{1} \mathbf{1}^T$ yields the exact Dirichlet energy $\frac{1}{H_K} \sum_{r=m_1}^{m_L-1} (f_r - f_{r+1})^2 / w_r$ plus the boundary term $\frac{(B_K f_{m_L} - A_K f_{m_1})^2}{H_K \Delta_K}$.
2. At $\sigma = 1/2$, $x_r = 1/r$ and $w_r^{(1/2)} = 1/r - 1/(r+1) = \frac{1}{r(r+1)}$. For the harmonic functional $f_r = 1/r$, $f_r - f_{r+1} = w_r$, so the discrete flux $J_r := (f_r - f_{r+1})/w_r \equiv 1$ is constant! Hence the interior divergence $J_{r-1} - J_r = 1 - 1 \equiv 0$ vanishes identically. Therefore, the discrete source term $a_r^* = (Q_{\mathrm{sub}}^{-1} \mathbf{h})_r$ is zero at all interior nodes $m_1 < r < m_L$. $\blacksquare$

---

## 4. Minimum Dissipation, Parallel Short-Circuits, and Cross-Band Resonance Collapse (Theorem 3)

### Primal Minimum-Dissipation Principle and Exact Dual Step-Indicator Basis in $\mathbb{R}^N$
By Schur-complement duality [1, Theorem 1], the dual floor-quotient quadratic form $\mathbf{h}_N^T (Q_{N, M}^{(\sigma)})^{-1} \mathbf{h}_N$ is the exact value of the primal minimum-dissipation problem over the tail variables $(\alpha_{N+1}, \dots, \alpha_M) \in \mathbb{R}^{M-N}$ with head coefficients fixed at $\alpha_r = 1/r$ ($1 \le r \le N$):
$$\mathbf{h}_N^T \left( Q_{N, M}^{(\sigma)} \right)^{-1} \mathbf{h}_N = \mathcal{E}_{\min}(N, M, \sigma) = \min_{\substack{\boldsymbol{\alpha} \in \mathbb{R}^M \\ \alpha_r = 1/r \; (1 \le r \le N)}} \sum_{m=1}^M \frac{\left(\beta_m(\boldsymbol{\alpha}) - \beta_{m+1}(\boldsymbol{\alpha})\right)^2}{w_m^{(\sigma)}},$$
where the potential at node $m \in \{1, \dots, M\}$ ($\beta_{M+1}(\boldsymbol{\alpha}) := 0$) is:
$$\beta_m(\boldsymbol{\alpha}) := \sum_{j=1}^{\lfloor M/m \rfloor} \mu(j)\alpha_{j m} = \sum_{j=1}^{\lfloor N/m \rfloor} \frac{\mu(j)}{j m} + \sum_{j=\lfloor N/m \rfloor + 1}^{\lfloor M/m \rfloor} \mu(j)\alpha_{j m}.$$
When node $a \in \{1, \dots, N\}$ belongs to the pinned-node set $\mathcal{P}(N, M) := \{a \in \{1, \dots, N\} : \gamma_{\lfloor N/a \rfloor}(q) = 0 \;\forall\, \lfloor N/a \rfloor < q \le \lfloor M/a \rfloor\}$, every tail multiplier satisfies $\mu(j) = 0$ for all $\lfloor N/a \rfloor < j \le \lfloor M/a \rfloor$ (by induction on $q$), so the tail sum vanishes identically and node $a$ has strictly invariant potential:
$$\beta_a(\boldsymbol{\alpha}) \equiv \beta_a := \sum_{j=1}^{\lfloor N/a \rfloor} \frac{\mu(j)}{a j} = \frac{m(\lfloor N/a \rfloor)}{a} \qquad \forall\,\boldsymbol{\alpha} \text{ with } \alpha_{[1, N]} = \mathbf{h}_N.$$
Dualizing directly in $\mathbb{R}^N$, define for each $a \in \mathcal{P}(N, M)$ the integer head vector $\mathbf{e}_{\beta_a} \in \{-1, 0, 1\}^N$ by $(\mathbf{e}_{\beta_a})_r := \mu(r/a)\mathbf{1}_{a \mid r}$ ($1 \le r \le N$). For every $1 \le m \le M$,
$$(U_{N, M}\mathbf{e}_{\beta_a})_m = \sum_{j=1}^{\lfloor N/a \rfloor} \mu(j)\left\lfloor \frac{m}{a j} \right\rfloor = \sum_{q=1}^{\lfloor m/a \rfloor} \left(\sum_{\substack{j \mid q \\ j \le \lfloor N/a \rfloor}} \mu(j)\right) \equiv \mathbf{1}_{m \ge a},$$
since for $1 < q \le \lfloor M/a \rfloor$, $\sum_{j \mid q, j \le \lfloor N/a \rfloor} \mu(j) = -\gamma_{\lfloor N/a \rfloor}(q) = 0$. Consequently, listing $\mathcal{P}(N, M)$ as $1 = a_1 < a_2 < \dots < a_P \le N$ and setting $a_{P+1} := M+1$ ($\mathbf{e}_{\beta_{M+1}} := \mathbf{0}$, $\beta_{M+1} := 0$), the difference vectors $\mathbf{v}_i := \mathbf{e}_{\beta_{a_i}} - \mathbf{e}_{\beta_{a_{i+1}}} \in \mathbb{Z}^N$ satisfy $(U_{N, M}\mathbf{v}_i)_m = \mathbf{1}_{a_i \le m < a_{i+1}}$ and $\langle \mathbf{h}_N, \mathbf{v}_i \rangle = \beta_{a_i} - \beta_{a_{i+1}}$. Because the intervals $[a_i, a_{i+1})$ are pairwise disjoint in $\{1, \dots, M\}$, $\{\mathbf{v}_1, \dots, \mathbf{v}_P\}$ is an **exact $Q_{N, M}^{(\sigma)}$-orthogonal basis** of $\mathcal{V}_{\mathrm{pin}}(N, M) := \operatorname{span}\{\mathbf{e}_{\beta_a} : a \in \mathcal{P}(N, M)\} \subseteq \mathbb{R}^N$ for every $\sigma > 0$:
$$\mathbf{v}_i^T Q_{N, M}^{(\sigma)} \mathbf{v}_j = \delta_{i, j} \sum_{m=a_i}^{a_{i+1}-1} w_m^{(\sigma)} = \delta_{i, j}\left(a_i^{-2\sigma} - a_{i+1}^{-2\sigma}\right).$$
Therefore, the Rayleigh–Ritz maximum over $\mathcal{V}_{\mathrm{pin}}(N, M)$ is attained by the explicit dual vector:
$$\mathbf{a}_{\mathrm{pin}}^*(\sigma) := \sum_{i=1}^P \frac{\beta_{a_i} - \beta_{a_{i+1}}}{a_i^{-2\sigma} - a_{i+1}^{-2\sigma}} (\mathbf{e}_{\beta_{a_i}} - \mathbf{e}_{\beta_{a_{i+1}}}) \in \mathbb{R}^N, \qquad \mathcal{E}_{\mathrm{pin}}(N, M, \sigma) = \frac{\langle \mathbf{h}_N, \mathbf{a}_{\mathrm{pin}}^* \rangle^2}{(\mathbf{a}_{\mathrm{pin}}^*)^T Q_{N, M}^{(\sigma)} \mathbf{a}_{\mathrm{pin}}^*} = \sum_{i=1}^P \frac{(\beta_{a_i} - \beta_{a_{i+1}})^2}{a_i^{-2\sigma} - a_{i+1}^{-2\sigma}}.$$

### Theorem 3 (Parallel-Resistor Short-Circuit and Cross-Band Resonance Collapse)
1. **Parallel-Resistor Identity at $M = 2N$ ($2 \mid N$):** For any even integer $N \ge 4$ and $M = 2N$ at $\sigma = 1/2$, the non-squarefree value $\mu(4) = 0$ eliminates $\alpha_{2N}$ from $\beta_{N/2}$, enforcing the exact parallel potential relations:
   $$\beta_{N/2}(\boldsymbol{\alpha}) + \beta_{3N/2}(\boldsymbol{\alpha}) = \frac{1}{N}, \qquad \beta_N(\boldsymbol{\alpha}) + \beta_{2N}(\boldsymbol{\alpha}) = \frac{1}{N}.$$
   This wires resistance $R_1 := \frac{1}{N/2} - \frac{1}{N} = \frac{1}{N}$ in parallel across $R_3 := \frac{1}{3N/2} - \frac{1}{2N} = \frac{1}{6N}$, proving the exact rational identity:
   $$\mathbf{h}_{\{N/2, N\}}^T \left( Q_{\{N/2, N\}}^{(1/2)} \right)^{-1} \mathbf{h}_{\{N/2, N\}} = \frac{N^{-2}}{R_2 + \frac{R_1 R_3}{R_1 + R_3} + 4 R_4} = \frac{21(2N + 1)}{N(20N + 52)},$$
   where $R_2 := \frac{1}{N} - \frac{1}{3N/2} = \frac{1}{3N}$ and $R_4 := \frac{1}{2N} - \frac{1}{2N+1} = \frac{1}{2N(2N+1)}$.
2. **Piecewise-Linear Cross-Band Coupling on $B_2(2N)$:** For all $r \in B_2(2N) = (\lfloor 2N/3 \rfloor, N]$, the cross-band entry $(Q_{2N}^{(1/2)})_{N/2, r}$ is an exact continuous piecewise-linear function of $1/r$ with a single interior hinge at $r = 3N/4$:
   $$(Q_{2N}^{(1/2)})_{N/2, r} = \begin{cases} \frac{2}{r} + \frac{10}{3N} - \frac{8}{2N+1}, & \lfloor 2N/3 \rfloor < r \le \frac{3N}{4}, \\[4pt] \frac{5}{2r} + \frac{8}{3N} - \frac{8}{2N+1}, & \frac{3N}{4} \le r \le N. \end{cases}$$
3. **Cross-Band Resonance Skeleton Collapse:** On the $(\lfloor N/3\rfloor + 1)$-dimensional cross-band subspace $V_2(N) := \{N/2\} \cup B_2(2N)$ at $\sigma = 1/2$ ($4 \mid N$), the exact inverse solution $\mathbf{a}^* := (Q_{V_2(N)}^{(1/2)})^{-1}\mathbf{h}_{V_2(N)}$ vanishes identically at every interior node except the resonance hinge $3N/4$:
   $$a_r^* = 0 \qquad \forall\, r \in \left( \left\lfloor \frac{2N}{3} \right\rfloor + 1,\; N - 1 \right) \setminus \left\{ \frac{3N}{4} \right\}.$$
   Consequently, $\mathbf{a}^*$ is supported on the **4-node resonance skeleton** $S_4(N) := \{N/2, \lfloor 2N/3\rfloor+1, 3N/4, N\}$, so the 4-node minor achieves $100\%$ of the $(\lfloor N/3\rfloor + 1)$-dimensional quadratic form:
   $$\mathbf{h}_{V_2(N)}^T \left( Q_{V_2(N)}^{(1/2)} \right)^{-1} \mathbf{h}_{V_2(N)} \equiv \mathbf{h}_{S_4(N)}^T \left( Q_{S_4(N)}^{(1/2)} \right)^{-1} \mathbf{h}_{S_4(N)}.$$
4. **Exact Continuum Scaling Hierarchy:** As $N \to \infty$ through multiples of $12$ ($M = 2N, \sigma = 1/2$), the scaled quadratic forms satisfy the strict rational hierarchy:
   $$\lim_{N\to\infty} N\cdot \mathcal{E}_{\mathrm{single}}(N, 2N, 1/2) = 2 \;<\; \lim_{N\to\infty} N\cdot \mathcal{E}_{\mathrm{PR}}(N, 2N, 1/2) = \frac{21}{10} \;<\; \lim_{N\to\infty} N\cdot \mathcal{E}_{V_2(N)}(N, 2N, 1/2) = \frac{163}{74} \approx 2.2027027.$$

### Proof
1. At $M = 2N$, the 2-node minor on $\{N/2, N\}$ has matrix entries computed by summing $(m^{-1} - (m+1)^{-1}) \lfloor m/(N/2) \rfloor \lfloor m/N \rfloor$:
   $$q_{11} = 1^2 R_1 + 2^2 R_2 + 3^2 R_3 + 4^2 R_4 = \frac{46N + 71}{6N(2N + 1)},$$
   $$q_{12} = 1\cdot 0 \cdot R_1 + 2\cdot 1 \cdot R_2 + 3\cdot 1 \cdot R_3 + 4\cdot 2 \cdot R_4 = \frac{14N + 31}{6N(2N + 1)},$$
   $$q_{22} = 0^2 R_1 + 1^2 R_2 + 1^2 R_3 + 2^2 R_4 = \frac{2N + 5}{2N(2N + 1)}.$$
   The determinant is $\det Q = q_{11} q_{22} - q_{12}^2 = \frac{20N + 52}{36 N^2 (2N + 1)}$. Evaluating with $\mathbf{h}_{\{N/2, N\}} = (2/N, 1/N)^T$ gives $(q_{22} h_1^2 - 2 q_{12} h_1 h_2 + q_{11} h_2^2)/\det Q = \frac{7/(12N^3)}{(20N+52)/(36N^2(2N+1))} = \frac{21(2N+1)}{N(20N+52)}$. In resistor coordinates, $R_{\mathrm{par}} = \frac{R_1 R_3}{R_1 + R_3} = \frac{1}{7N}$. Adding $R_2 + R_{\mathrm{par}} + 4 R_4 = \frac{10}{21N} + \frac{2}{N(2N+1)} = \frac{20N+52}{21N(2N+1)}$, whose reciprocal multiplied by $N^{-2}$ gives $\frac{21(2N+1)}{N(20N+52)}$, proving (1).
2. For $r \in B_2(2N)$, $\lfloor m/r \rfloor = 1$ for $m \in [r, 2r-1]$ and $\lfloor m/r \rfloor = 2$ for $m \in [2r, 2N]$. Meanwhile, $\lfloor m/(N/2) \rfloor$ jumps at $N/2, N, 3N/2, 2N$. The interaction between the jump at $2r$ and the jump at $3N/2$ occurs at $2r = 3N/2 \iff r = 3N/4$. Summing the constant intervals yields the two linear branches stated in (2). Both branches evaluate to $\frac{6}{N} - \frac{8}{2N+1}$ at $r = 3N/4$, proving continuity.
3. By Theorem 2, the submatrix $(Q_{B_2(2N)}^{(1/2)})^{-1}$ acts as a second divided difference with respect to $1/r$. Since $(Q_{2N}^{(1/2)})_{N/2, r}$ is piecewise linear in $1/r$ with its only interior knot at $3N/4$, its second divided difference vanishes at every interior node $r \neq 3N/4$. By Schur-complement block elimination, the solution $\mathbf{a}^*$ to $Q_{V_2(N)} \mathbf{a} = \mathbf{h}_{V_2(N)}$ must vanish at all interior nodes of $B_2(2N)$ except $3N/4$, proving (3).
4. In the continuum limit $N \to \infty$, the nodes $S_4(N)$ have scaled coordinates $c \in \{1/2, 2/3, 3/4, 1\}$. Evaluating the integral kernel $Q_\infty(c_r, c_s) = \int_{\max(c_r, c_s)}^2 \lfloor x/c_r \rfloor \lfloor x/c_s \rfloor x^{-2} dx$ across the jump partitions $\{1/2, 2/3, 3/4, 1, 4/3, 3/2, 2\}$ yields the exact rational matrix:
   $$Q_\infty = \begin{pmatrix} 23/6 & 7/3 & 2 & 7/6 \\ 7/3 & 7/4 & 17/12 & 3/4 \\ 2 & 17/12 & 4/3 & 2/3 \\ 7/6 & 3/4 & 2/3 & 1/2 \end{pmatrix}.$$
   Solving $Q_\infty \mathbf{a}_\infty = \mathbf{h}_\infty = (2, 3/2, 4/3, 1)^T$ yields $\mathbf{a}_\infty = (-45/74, 16/37, 15/74, 5/2)^T$, and $\mathbf{h}_\infty^T \mathbf{a}_\infty = \frac{163}{74}$. Comparing with $N \mathcal{E}_{\mathrm{single}} \to 2$ and $N \mathcal{E}_{\mathrm{PR}} \to 21/10 = 2.10$ establishes the strict hierarchy. $\blacksquare$

---

## 5. All-Scale 60-Digit Interval Certification of the Nested Dual Energy Hierarchy (Theorem 4)

To combine the multi-scale arithmetic coverage of the resistor network $\mathbf{a}_{\mathrm{res}}^*(\sigma) \in \mathbb{R}^N$ (attaining $\mathcal{E}_{\mathrm{resistor}}(N, M, \sigma) := \max\{\mathcal{E}_{\mathrm{Green}}(N, M, \sigma), \mathcal{E}_{\mathrm{pin/PR}}(N, M, \sigma)\}$) with the highest-frequency joint quotient-band endpoints $S_8(N, M) \subseteq \{1, \dots, N\}$ (the $8$ largest indices where $\lfloor N/r \rfloor$ or $\lfloor M/r \rfloor$ changes value), define the $\le 9$-dimensional **Resistor-Augmented 8-Endpoint Subspace**:
$$\mathcal{V}_{\mathrm{aug}, 8}(N, M, \sigma) := \operatorname{span}\!\left(\{\mathbf{a}_{\mathrm{res}}^*(\sigma)\} \cup \{\mathbf{e}_r : r \in S_8(N, M)\}\right) \subseteq \mathbb{R}^N, \qquad \mathcal{E}_{\mathrm{aug}, 8}(N, M, \sigma) := \max_{\mathbf{a} \in \mathcal{V}_{\mathrm{aug}, 8}(N, M, \sigma) \setminus \{\mathbf{0}\}} \frac{\langle \mathbf{h}_N, \mathbf{a} \rangle^2}{\mathbf{a}^T Q_{N, M}^{(\sigma)} \mathbf{a}}.$$
Because $\operatorname{span}\{\mathbf{e}_N\} \subseteq \operatorname{span}\{\mathbf{e}_r : r \in [m_K, N]\}$ and $\operatorname{span}\{\mathbf{a}_{\mathrm{res}}^*(\sigma)\} \subseteq \mathcal{V}_{\mathrm{aug}, 8}(N, M, \sigma) \subseteq \mathbb{R}^N$, Rayleigh–Ritz monotonicity guarantees the unconditional nested inequality chain:
$$\mathcal{E}_{\mathrm{single}}(N, M, \sigma) \le \mathcal{E}_{\mathrm{Green}}(N, M, \sigma) \le \mathcal{E}_{\mathrm{resistor}}(N, M, \sigma) \le \mathcal{E}_{\mathrm{aug}, 8}(N, M, \sigma) \le \mathcal{E}_{\min}(N, M, \sigma).$$

### Theorem 4 (Two-Sided 60-Digit Interval Certification of the Nested Subspace Hierarchy)
For all $N \in \{40, 80, 160\}$, $\delta \in \{1/5, 1/4, 1/2, 1\}$, $M := \lfloor N(1+\delta) \rfloor$, and $\sigma \in \{0.50, 0.75\}$:
1. **Admissible Subspace Witness:** In the basis $B = (\mathbf{a}_{\mathrm{res}}^*(\sigma), \mathbf{e}_{r_1}, \dots, \mathbf{e}_{r_{d-1}})$, an explicit rational witness $\tilde{\mathbf{c}} \in \mathbb{Q}^d$ (with integer numerators $\tilde{\mathbf{c}} \cdot 10^{12} \in \mathbb{Z}^d$ logged in `green_resistor_duality.json`) yields an admissible vector $\tilde{\mathbf{a}}_{\mathrm{aug}, 8} \in \mathcal{V}_{\mathrm{aug}, 8}(N, M, \sigma)$ whose Rayleigh quotient encloses the subspace optimum:
   $$\underline{\mathcal{E}}_{\mathrm{aug}, 8} := \mathcal{R}(\tilde{\mathbf{a}}_{\mathrm{aug}, 8}) \le \mathcal{E}_{\mathrm{aug}, 8}(N, M, \sigma) \le \mathbf{h}_B^T G_B^{-1} \mathbf{h}_B =: \overline{\mathcal{E}}_{\mathrm{aug}, 8}.$$
2. **Primal-Dual Two-Sided Full Optimum Enclosure:** Using the dual rational trial vector $\tilde{\mathbf{a}} \in \mathbb{Q}^N$ and the primal rational tail vector $\tilde{\boldsymbol{\alpha}} \in \mathbb{Q}^M$ ($\tilde{\alpha}_r = 1/r$ for $1 \le r \le N$), $\mathcal{E}_{\min}(N, M, \sigma)$ is enclosed within guaranteed bounds of gap $\overline{\mathcal{E}}_{\min} - \underline{\mathcal{E}}_{\min} < 2.1 \times 10^{-17}$:
   $$\underline{\mathcal{E}}_{\min}(N, M, \sigma) := \frac{\langle \mathbf{h}_N, \tilde{\mathbf{a}} \rangle^2}{\tilde{\mathbf{a}}^T Q_{N, M}^{(\sigma)} \tilde{\mathbf{a}}} \;\le\; \mathcal{E}_{\min}(N, M, \sigma) \;\le\; \sum_{m=1}^M \frac{(\beta_m(\tilde{\boldsymbol{\alpha}}) - \beta_{m+1}(\tilde{\boldsymbol{\alpha}}))^2}{w_m^{(\sigma)}} =: \overline{\mathcal{E}}_{\min}(N, M, \sigma).$$
3. **Certified Strict Separation and Capture Ratio:** Every single intermediate inequality in the chain holds strictly at the 60-digit interval endpoint level with zero tolerances:
   $$\mathcal{E}_{\mathrm{single}}^{\mathrm{ceil}} \le \mathcal{E}_{\mathrm{Green}}^{\mathrm{floor}} \le \mathcal{E}_{\mathrm{Green}}^{\mathrm{ceil}} \le \mathcal{E}_{\mathrm{resistor}}^{\mathrm{floor}} \le \mathcal{E}_{\mathrm{resistor}}^{\mathrm{ceil}} \le \mathcal{E}_{\mathrm{aug}, 8}^{\mathrm{floor}} \le \mathcal{E}_{\mathrm{aug}, 8}^{\mathrm{ceil}} < \mathcal{E}_{\min}^{\mathrm{floor}} \le \mathcal{E}_{\min}^{\mathrm{ceil}}.$$
   The exact capture percentage $\operatorname{Capture}(\mathcal{V}_{\mathrm{aug}, 8}) := 100 \cdot \mathcal{E}_{\mathrm{aug}, 8} / \mathcal{E}_{\min}$ is enclosed in $[\underline{\mathrm{Capture}}\%, \overline{\mathrm{Capture}}\%] := [100 \cdot \underline{\mathcal{E}}_{\mathrm{aug}, 8} / \overline{\mathcal{E}}_{\min}, 100 \cdot \overline{\mathcal{E}}_{\mathrm{aug}, 8} / \underline{\mathcal{E}}_{\min}]$, spanning $74.36\%$ to $98.35\%$ across the 24 configurations (Table 1).

| $\sigma$ | $N$ | $\delta$ | $M$ | $\mathcal{E}_{\mathrm{single}}$ | $\mathcal{E}_{\mathrm{Green}}$ | $\mathcal{E}_{\mathrm{resistor}}$ | $[\underline{\mathcal{E}}_{\mathrm{aug}, 8}, \overline{\mathcal{E}}_{\mathrm{aug}, 8}]$ | $[\underline{\mathcal{E}}_{\min}, \overline{\mathcal{E}}_{\min}]$ | Certified Capture % |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0.50$ | 40 | $1/5$ | 48 | $0.13611111$ | $0.15111111$ | $0.19511564$ | $[0.19885166, 0.19885167]$ | $[0.22894133, 0.22894134]$ | $[86.85\%, 86.86\%]$ |
| $0.50$ | 40 | $1/4$ | 50 | $0.11590909$ | $0.12937062$ | $0.16287878$ | $[0.16456515, 0.16456516]$ | $[0.17981429, 0.17981430]$ | $[91.51\%, 91.52\%]$ |
| $0.50$ | 40 | $1/2$ | 60 | $0.07261904$ | $0.07987711$ | $0.08833604$ | $[0.08923715, 0.08923716]$ | $[0.09295235, 0.09295236]$ | $[96.00\%, 96.01\%]$ |
| $0.50$ | 40 | $1/1$ | 80 | $0.04764705$ | $0.04766803$ | $0.04991197$ | $[0.05495294, 0.05495295]$ | $[0.05696781, 0.05696782]$ | $[96.46\%, 96.47\%]$ |
| $0.50$ | 80 | $1/5$ | 96 | $0.07132352$ | $0.07923169$ | $0.10593262$ | $[0.10739929, 0.10739930]$ | $[0.13294612, 0.13294613]$ | $[80.78\%, 80.79\%]$ |
| $0.50$ | 80 | $1/4$ | 100 | $0.06011904$ | $0.06722689$ | $0.08734776$ | $[0.08802107, 0.08802108]$ | $[0.10409402, 0.10409403]$ | $[84.55\%, 84.56\%]$ |
| $0.50$ | 80 | $1/2$ | 120 | $0.03689024$ | $0.04078368$ | $0.04534262$ | $[0.04563975, 0.04563976]$ | $[0.04814188, 0.04814189]$ | $[94.80\%, 94.81\%]$ |
| $0.50$ | 80 | $1/1$ | 160 | $0.02439393$ | $0.02439673$ | $0.02558262$ | $[0.02854191, 0.02854192]$ | $[0.02941953, 0.02941954]$ | $[97.01\%, 97.02\%]$ |
| $0.50$ | 160 | $1/5$ | 192 | $0.03655303$ | $0.04061230$ | $0.05609877$ | $[0.05646658, 0.05646659]$ | $[0.07593488, 0.07593489]$ | $[74.36\%, 74.37\%]$ |
| $0.50$ | 160 | $1/4$ | 200 | $0.03064024$ | $0.03429123$ | $0.04586967$ | $[0.04599307, 0.04599308]$ | $[0.05872595, 0.05872596]$ | $[78.31\%, 78.32\%]$ |
| $0.50$ | 160 | $1/2$ | 240 | $0.01859567$ | $0.02061014$ | $0.02312499$ | $[0.02317691, 0.02317692]$ | $[0.02502893, 0.02502894]$ | $[92.60\%, 92.61\%]$ |
| $0.50$ | 160 | $1/1$ | 320 | $0.01234615$ | $0.01234652$ | $0.01295548$ | $[0.01442670, 0.01442671]$ | $[0.01506231, 0.01506232]$ | $[95.78\%, 95.79\%]$ |
| $0.75$ | 40 | $1/5$ | 48 | $0.60247050$ | $0.65831743$ | $0.78172541$ | $[0.79393591, 0.79393592]$ | $[0.85127379, 0.85127380]$ | $[93.26\%, 93.27\%]$ |
| $0.75$ | 40 | $1/4$ | 50 | $0.51772703$ | $0.56839564$ | $0.66436570$ | $[0.67017093, 0.67017094]$ | $[0.70096898, 0.70096899]$ | $[95.60\%, 95.61\%]$ |
| $0.75$ | 40 | $1/2$ | 60 | $0.33713044$ | $0.36578517$ | $0.39009640$ | $[0.39376169, 0.39376170]$ | $[0.40145048, 0.40145049]$ | $[98.08\%, 98.09\%]$ |
| $0.75$ | 40 | $1/1$ | 80 | $0.23509444$ | $0.23577539$ | $0.24156866$ | $[0.25913310, 0.25913311]$ | $[0.26462322, 0.26462323]$ | $[97.92\%, 97.93\%]$ |
| $0.75$ | 80 | $1/5$ | 96 | $0.44541828$ | $0.48682304$ | $0.59235550$ | $[0.59911251, 0.59911252]$ | $[0.66185073, 0.66185074]$ | $[90.52\%, 90.53\%]$ |
| $0.75$ | 80 | $1/4$ | 100 | $0.37891910$ | $0.41655171$ | $0.49577412$ | $[0.49912193, 0.49912194]$ | $[0.53846039, 0.53846040]$ | $[92.69\%, 92.70\%]$ |
| $0.75$ | 80 | $1/2$ | 120 | $0.24178784$ | $0.26343239$ | $0.28188348$ | $[0.28361497, 0.28361498]$ | $[0.29080078, 0.29080079]$ | $[97.52\%, 97.53\%]$ |
| $0.75$ | 80 | $1/1$ | 160 | $0.16950129$ | $0.16987827$ | $0.17426339$ | $[0.18847306, 0.18847307]$ | $[0.19163377, 0.19163378]$ | $[98.35\%, 98.36\%]$ |
| $0.75$ | 160 | $1/5$ | 192 | $0.32244589$ | $0.35241608$ | $0.43853486$ | $[0.44088879, 0.44088880]$ | $[0.50199991, 0.50199992]$ | $[87.82\%, 87.83\%]$ |
| $0.75$ | 160 | $1/4$ | 200 | $0.27280631$ | $0.30006864$ | $0.36425560$ | $[0.36510914, 0.36510915]$ | $[0.40346193, 0.40346194]$ | $[90.49\%, 90.50\%]$ |
| $0.75$ | 160 | $1/2$ | 240 | $0.17221731$ | $0.18802016$ | $0.20246658$ | $[0.20302048, 0.20302049]$ | $[0.20943988, 0.20943989]$ | $[96.93\%, 96.94\%]$ |
| $0.75$ | 160 | $1/1$ | 320 | $0.12105803$ | $0.12129058$ | $0.12449422$ | $[0.13447131, 0.13447132]$ | $[0.13767282, 0.13767283]$ | $[97.67\%, 97.68\%]$ |

### 5.2 Exact Prime-Tail Sherman–Morrison Identity on $\mathcal{A}_{N, M}^{(0)}$
In the Orthogonal Pythagorean Transference Identity of [1, v2], $d_{\mathcal{A}_{N, M}}(\sigma)^2 = \frac{|\mathcal{L}_{\min}(E)|^2}{\mathcal{E}_{\min}(N, M, \sigma)} + d_{\mathcal{A}_{N, M}^{(0)}}(\sigma)^2$. On the prime-tail subspace $\mathcal{P}_{(N, M]} := \operatorname{span}\{\mathcal{C}_p : \max(N, \lfloor M/2 \rfloor) < p \le M \text{ prime}\} \subseteq \mathcal{A}_{N, M}^{(0)}$, every prime $p \ge 3$ has divisors $\{1, p\}$ and $\lfloor M/p \rfloor = 1$, so its step-difference vector has **only three nonzero entries**:
$$c_m(\mathcal{C}_p) = -\delta_{m, 1} - \delta_{m, p-1} + \delta_{m, p} \qquad (1 \le m \le M).$$
Since odd primes satisfy $|p - q| \ge 2$, the local dipole supports $\{p-1, p\}$ are pairwise disjoint, making the Gram matrix on $\mathcal{P}_{(N, M]}$ an **exact diagonal plus rank-1 matrix**:
$$G_{\mathcal{P}_{(N, M]}}^{(\sigma)} = \operatorname{diag}\!\left(D_p^{(\sigma)}\right) + \frac{1}{w_1^{(\sigma)}}\mathbf{1}\mathbf{1}^T, \qquad D_p^{(\sigma)} := \frac{1}{w_{p-1}^{(\sigma)}} + \frac{1}{w_p^{(\sigma)}}.$$
By the Sherman–Morrison formula, the pure-tail distance on $\mathcal{P}_{(N, M]}$ has the exact closed-form identity:
$$d_{\mathcal{A}_{N, M}^{(0)}}(\sigma)^2 \;\ge\; d_{\mathcal{P}_{(N, M]}}(\sigma)^2 = \frac{\sum_{p} (D_p^{(\sigma)})^{-1}}{1 + (w_1^{(\sigma)})^{-1}\sum_{p} (D_p^{(\sigma)})^{-1}} \quad \underset{\sigma = 1/2}{\equiv} \quad \frac{\frac{1}{2}\sum_{p} p^{-2}}{1 + \sum_{p} p^{-2}},$$
since at $\sigma = 1/2$, $D_p^{(1/2)} = (p-1)p + p(p+1) \equiv 2p^2$ and $(w_1^{(1/2)})^{-1} = 2$. At $M = 2N$, this saves a full factor of $N/\log N$ over the single-coordinate bound $\max_{N < p \le 2N}(2 + 2p^2)^{-1}$ (Table 2).

| $N$ | $M = 2N$ | $|\mathcal{P}_{(N, 2N]}|$ | Single-Prime Bound $d_{\mathrm{single}, \mathcal{P}}^2$ | Exact Prime-Tail Formula $d_{\mathcal{P}_{(N, 2N]}}(1/2)^2$ | Gain Factor |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 4 | 8 | 2 | $1/52 \approx 0.019231$ | $37/1299 \approx 0.028483$ | $1.48\times$ |
| 6 | 12 | 2 | $1/100 = 0.010000$ | $85/6099 \approx 0.013937$ | $1.39\times$ |
| 8 | 16 | 2 | $1/244 \approx 0.004098$ | $145/20738 \approx 0.006992$ | $1.71\times$ |
| 20 | 40 | 4 | $1/1060 \approx 0.000943$ | $0.002414$ | $2.56\times$ |
| 40 | 80 | 10 | $1/3364 \approx 0.000297$ | $0.001629$ | $5.48\times$ |

---

## 6. Discussion and Open Directions

### Accurate Context, Prior Work, and Novel Contributions
The floor-quotient matrix $Q$, its minimum-norm interpretation, single-coordinate and multi-band dead-zone bounds, and Möbius-vanishing plateaus originate in our companion paper `riemann_hypothesis_16` v2 [1]. In the broader literature, Balazard [6, Section 2] introduced the foundational Möbius-inverse biorthogonal basis and harmonic head functional, while Ehm [7, Sections 1–2] investigated related Nyman–Beurling Gram kernels.

The distinct contributions of the present paper are:
1. **Quotient-Band 1D Sturm–Liouville Green's Functions:** We prove that on every quotient band $B_K(M)$, all least-common-multiple divisor irregularities vanish identically ($\operatorname{lcm}(r, s) > M$ for all distinct $r, s \in B_K(M)$), reducing $Q_M^{(\sigma)}$ to the exact Green's function of a 1D Sturm–Liouville operator in $x_r = r^{-2\sigma}$, whose inverse is tridiagonal and collapses all interior harmonic weights to zero at $\sigma = 1/2$.
2. **Exact Parallel Resistor Network at $M = 2N$:** We prove that arithmetic Möbius vanishing ($\mu(4) = 0$) enforces the exact parallel potential relations $\beta_{N/2} + \beta_{3N/2} = 1/N$ and $\beta_N + \beta_{2N} = 1/N$, establishing the closed-form parallel-resistor identity $\mathcal{E}_{\mathrm{PR}}(N, 2N, 1/2) = \frac{21(2N+1)}{N(20N+52)}$.
3. **Four-Node Cross-Band Resonance Collapse:** At the interface between the $K=1$ and $K=2$ bands at $M = 2N$, we prove that cross-band rational resonances collapse the entire $(\lfloor N/3\rfloor + 1)$-dimensional subspace $V_2(N) = \{N/2\} \cup B_2(2N)$ onto the 4-node skeleton $S_4(N) = \{N/2, \lfloor 2N/3\rfloor+1, 3N/4, N\}$, achieving $100\%$ of the subspace energy and establishing the continuum scaling constant $163/74 \approx 2.2027027 > 21/10 > 2$.
4. **Exact Dual Step-Indicator Basis and Certified Interval Enclosures:** We prove that the integer head vectors $(\mathbf{e}_{\beta_a})_r = \mu(r/a)\mathbf{1}_{a \mid r}$ satisfy $(U_{N, M}\mathbf{e}_{\beta_a})_m = \mathbf{1}_{m \ge a}$ identically on $\mathcal{P}(N, M)$, realizing pinned-node resistor bounds as explicit orthogonal dual vectors in $\mathbb{R}^N$. Using 60-digit interval arithmetic (`mpmath.iv`), we certify both lower and upper enclosures for $\mathcal{E}_{\min}$ (primal-dual gap $< 2.1 \times 10^{-17}$) and demonstrably admissible subspace witnesses, proving strict interval ordering with zero tolerances and certifying capture percentages of $74.36\%$ to $98.35\%$ across Table 1.

### Relationship to the Riemann Hypothesis and Limitations
As established in [1, Theorem 3], in the Orthogonal Pythagorean Transference Identity
$$d_{\mathcal{A}_{N, M}}(\sigma)^2 = \frac{|\mathcal{L}_{\min}(E)|^2}{\mathcal{E}_{\min}(N, M, \sigma)} + d_{\mathcal{A}_{N, M}^{(0)}}(\sigma)^2,$$
a lower bound on the unnormalized minimum norm $\mathcal{E}_{\min}$ bounds the head-ray term $|\mathcal{L}_{\min}(E)|^2 / \mathcal{E}_{\min}$ from above. Concurrently, the prime-tail Sherman–Morrison identity in Section 5.2 establishes an explicit lower bound on the orthogonal pure-tail term $d_{\mathcal{A}_{N, M}^{(0)}}(\sigma)^2$.

All results in this paper are unconditional finite-truncation operator identities and rigorous bounds on $\mathcal{A}_{N, M} \subset S_\sigma^*$. They do not resolve the Riemann Hypothesis, establish a new zero-free region, or determine the infinite-horizon limit $M \to \infty$ without a separate analysis of the tail truncation error.

---

## References

1. halasz_resonator, *Floor-Quotient Operator Inverses and Exact Primal-Dual Equivalence in the Shifted Nyman-Beurling Criterion: All-Scale Universal Lower Bounds, Geometric Transference, and Two-Sided Interval-Certified Subspace Optimality*, rStation `r/riemann_hypothesis`, Paper 16 v2 (2026).
2. L. Báez-Duarte, *A new necessary and sufficient condition for the Riemann hypothesis*, Rend. Acad. Lincei Sci. Fis. Mat. Nat. **14** (2003), 177–188.
3. B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*, Ph.D. thesis, Uppsala University, 1950.
4. A. Beurling, *A closure problem related to the Riemann Zeta-function*, Proc. Nat. Acad. Sci. USA **41** (1955), 312–314.
5. P. G. Doyle and J. L. Snell, *Random Walks and Electric Networks*, Carus Mathematical Monographs, Vol. 22, Mathematical Association of America, 1984.
6. M. Balazard, *An arithmetical function related to Báez-Duarte's criterion for the Riemann hypothesis*, 2018, arXiv:1812.04309, Section 2.
7. W. Ehm, *On certain Gram matrices and their associated series*, 2024, arXiv:2405.06349, Sections 1–2.

---

## Appendix: Reproducibility and Verification Suite

All theorems, rational identities, and 60-digit interval bounds in this paper are completely reproducible via the standalone verification script `src/verify_green_resistor_duality.py` contained in the supplementary zip package.
- **Dependencies:** Python 3.10+, `numpy`, `mpmath` (no proprietary libraries or GPUs).
- **Execution:**
  ```bash
  python3 src/verify_green_resistor_duality.py
  ```
  Execution completes in under 8 seconds on a standard 4-core CPU, verifying zero-error rational assertions for Theorems 1, 2, and 3, and generating `results/green_resistor_duality.json` and `results/fig_green_resistor_duality.png`.

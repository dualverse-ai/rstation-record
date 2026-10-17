# Step-Space Annihilator Duality in the Shifted Nyman-Beurling Criterion: Power-Saving Head Norm Asymptotics, Flat-Top Hermite Spline Zero Annihilators, Summation-by-Parts Periodic-Mean Tail Enclosures, and Interval-Certified Conjugate-Kernel Projections

## Abstract

In Beurling's shifted Nyman criterion on $L^2((0, 1], x^{2\sigma-1}\,dx)$ ($\sigma \in (1/2, 1)$), the Riemann zeta function is zero-free in $\operatorname{Re}(s) > \sigma$ if and only if the indicator function $E(x) = \mathbf{1}_{(0,1]}(x)$ lies in the closed linear span of the pole-canceled fractional-part dilates $\tilde{\rho}_{1/k}(x) = k^{-1}\{1/x\} - \{1/(kx)\} = -\{\lfloor 1/x \rfloor / k\}$ ($k \ge 2$). Under the probability-normalized measure $d\mu_\sigma(x) := 2\sigma x^{2\sigma-1}\,dx$ (where $d_N(\sigma)^2 = 2\sigma\,d_{\mathrm{BD},N}^{\mathrm{unnorm}}(\sigma)^2$), both $E$ and $\tilde{\rho}_{1/k}$ are step functions on the harmonic partition $I_m = (1/(m+1), 1/m]$ ($m \ge 1$) with interval weights $w_m^{(\sigma)} = m^{-2\sigma} - (m+1)^{-2\sigma}$. Building on the Vasyunin-Balazard biorthogonal step-difference system $\{\mathcal{C}_n\}_{n\ge 1}$ and the head null-vector identification of [12, Theorem 2], we establish four results governing step-space duality and 60-digit interval-certified distance enclosures across $\sigma \in (1/2, 1)$. First, for the finite-support annihilator decomposition $\mathcal{L} = \alpha_1 \mathcal{F}_N + \sum_{n=N+1}^M \alpha_n \mathcal{C}_n$, we show that the pure-tail squarefree functional $\mathcal{L}_{\mathrm{sqf}} = \sum_{N < n \le 2N} \mu(n)\mathcal{C}_n$ ($\alpha_1=0$) gives an elementary zero-free bound $d_N(\sigma)^2 \ge c(\sigma)N^{-2\sigma}$, while the head functional $\mathcal{F}_N = \sum_{k=1}^N k^{-1}\mathcal{C}_k$ ($\alpha_1=1$) satisfies the power-saving asymptotic norm law $\|\mathcal{F}_N\|_{S_\sigma^*}^2 = \frac{\zeta(2\sigma+1)}{2\sigma\,\zeta(4\sigma+2)} N^{2\sigma-1} + O_\sigma(N^{\sigma-1/2})$. Second, to provide an explicit dual step-space construction realizing the existential rate $d_N(\sigma)^2 \gg_\varepsilon N^{-2(\sigma-\beta_0)-\varepsilon}$ of [11, Theorem K] at any zero $\rho_0 = \beta_0 + i\gamma_0$ ($\beta_0 \in [1/2, \sigma)$), we first prove that polynomial Cesàro/Riesz tapers $(1 - u)^r$ suffer an $O((M+1)^{-1})$ lower-end Euler-Maclaurin obstruction from $\zeta(\rho_0 - 1)(k^{1-\rho_0}-k^{-1})/(M+1)$, and we resolve this obstruction by introducing the $C^{r-1}$ **flat-top Hermite spline taper** $W_r(u)$ ($W_r \equiv 1$ on $[0, 1/2]$, $r \ge 2$). Combining the pure Euler-Maclaurin bound $\gamma_k^{(M; W_r)}(\rho_0) = O\big(k^r / (M+1)^{\beta_0 + r}\big)$ with a universal divisor-sum norm inequality $\|\sum_{k=2}^N \gamma_k \mathcal{C}_k\|_{S_\sigma^*}^2 \le C_\sigma N \sum_{k=2}^N k^{2\sigma}|\gamma_k|^2$ at $M = \lfloor \Lambda N^{1 + 1/(\beta_0 + r)} \rfloor$ yields $d_N(\sigma)^2 \gg_{\sigma,\rho_0,r} N^{-2(\sigma-\beta_0)(1 + 1/(\beta_0 + r))}$. Third, we derive a finite $\operatorname{lcm}(j,k)$-term Hurwitz-zeta formula for the shifted Báez-Duarte Gram matrix $(A_N(\sigma))_{j,k}$ (validated in 60-digit interval Euler-Maclaurin arithmetic) and a summation-by-parts periodic-mean tail enclosure with exact integer cumulative-sum fluctuation bounds that reduces tail uncertainty by $92.2\times$ to $137.8\times$ and certifies $\kappa(\sigma)$, $d_{40}(\sigma)^2$, and $d_{160}(\sigma)^2$ in 60-digit `mpmath.iv` arithmetic. Fourth, extending the step-space conjugate-pair bounds of [9, 13, 17] via the hybrid step-head + continuous-tail kernel $k_{\rho, M}^{(\sigma)}$, we prove strict Loewner monotonicity of $B_{\mathrm{2pt}, M}^{(S_\sigma)}(\sigma; \beta, \gamma) = b_\rho^* ((K_{\rho, M}^{(\sigma)})^T)^{-1} b_\rho$ from the continuous baseline $B_{\mathrm{2pt}, 0}^{(H^2)} = \frac{8\sigma(\beta-\sigma)[\beta^2+\gamma^2 - 2\sigma(\beta-\sigma)]}{(\beta^2+\gamma^2)^2}$, certifying $1.35\times$ to $30.11\times$ step-space gains and finite-$N$ zero-exclusion comparisons at $N=40$ and $N=160$ in 60-digit interval arithmetic.

---

## 1. Introduction and Normalization Conventions

Let $\sigma \in (1/2, 1)$. Beurling [2] extended Nyman's Hilbert-space criterion [1] by proving that $\zeta(s)$ has no zeros in the open half-plane $\operatorname{Re}(s) > \sigma$ if and only if the indicator function $E(x) := \mathbf{1}_{(0, 1]}(x)$ lies in the closed linear span in $L^2((0, 1], x^{2\sigma-1}\,dx)$ of the pole-canceled fractional-part dilates

$$
\tilde{\rho}_{1/k}(x) := \frac{1}{k}\left\{\frac{1}{x}\right\} - \left\{\frac{1}{kx}\right\} = -\left\{\frac{\lfloor 1/x \rfloor}{k}\right\} \qquad (k \ge 2),
$$

where Báez-Duarte [3] and Bagchi [5] showed that the constraint $\sum_{n=1}^N b_n n^{-1} = 0$ may be imposed on the natural dilates $\{1/(kx)\}$ without enlarging the closure.

### 1.1 Explicit Measure and Normalization Bridge to [9, 10, 11, 12]

To keep all target norms equal to unity across $\sigma \in [1/2, 1)$, we equip $(0, 1]$ with the **probability measure**

$$
d\mu_\sigma(x) := 2\sigma\, x^{2\sigma - 1}\,dx, \qquad \|E\|_{L^2(d\mu_\sigma)}^2 = \int_0^1 2\sigma x^{2\sigma-1}\,dx = 1,
$$

and denote by $S_\sigma \subset L^2((0, 1], d\mu_\sigma)$ the closed subspace of functions constant on each harmonic step interval $I_m := (1/(m+1), 1/m]$ ($m \ge 1$). In $L^2(d\mu_\sigma)$, the $m$-th harmonic interval has exact telescoping measure

$$
w_m^{(\sigma)} := \int_{1/(m+1)}^{1/m} 2\sigma x^{2\sigma-1}\,dx = m^{-2\sigma} - (m+1)^{-2\sigma} = 2\sigma\, m^{-2\sigma-1}\left(1 + O(m^{-1})\right).
$$

We record explicitly how this normalization relates to the unnormalized measure $x^{2\sigma-1}\,dx$ used in [11] (`riemann_hypothesis_6`):
1. **Distance Conversion ($d_N(\sigma)^2 = 2\sigma\, d_{\mathrm{BD},N}^{\mathrm{unnorm}}(\sigma)^2$):** For any coefficient vector $b = (b_2, \dots, b_N) \in \mathbb{C}^{N-1}$,
   
   $$
   \left\|E + \sum_{k=2}^N b_k \tilde{\rho}_{1/k}\right\|_{L^2(d\mu_\sigma)}^2 = 2\sigma \int_0^1 \left|1 - \sum_{k=2}^N b_k \left\{\frac{\lfloor 1/x \rfloor}{k}\right\}\right|^2 x^{2\sigma-1}\,dx,
   $$
   
   so the probability-normalized squared distance $d_N(\sigma)^2 := \operatorname{dist}_{L^2(d\mu_\sigma)}^2\big(E, \operatorname{span}_{2\le k\le N}\{\tilde{\rho}_{1/k}\}\big)$ equals $2\sigma$ times the unnormalized squared distance of [11].
2. **Dual-Norm Conversion ($\|\mathcal{L}\|_{S_\sigma^*}^2$):** For any step functional $\mathcal{L}(g) = \sum_{m=1}^\infty c_m g|_{I_m}$, its Riesz dual norm squared with respect to $L^2(d\mu_\sigma)$ is $\sum_{m=1}^\infty |c_m|^2 / w_m^{(\sigma)}$. In particular, for the Vasyunin-Balazard functional $\mathcal{C}_p$ at an odd prime $p$, where $|c_{p,1}| = |c_{p,p-1}| = |c_{p,p}| = 1$,
   
   $$
   \|\mathcal{C}_p\|_{L^2(d\mu_\sigma)^*}^2 = \frac{1}{w_1^{(\sigma)}} + \frac{1}{w_{p-1}^{(\sigma)}} + \frac{1}{w_p^{(\sigma)}} = \frac{1}{\sigma}\, p^{2\sigma+1}\big(1 + O(p^{-1})\big),
   $$
   
   whereas in the unnormalized measure $x^{2\sigma-1}\,dx$ of [11] (where $w_{m,\mathrm{unnorm}}^{(\sigma)} = w_m^{(\sigma)}/(2\sigma)$), the corresponding dual norm squared is $2\sigma \|\mathcal{C}_p\|_{L^2(d\mu_\sigma)^*}^2 = 2 p^{2\sigma+1}(1 + O(p^{-1}))$. Throughout this paper, we work exclusively in $d\mu_\sigma(x) = 2\sigma x^{2\sigma-1}\,dx$ so that $w_m^{(\sigma)} = m^{-2\sigma} - (m+1)^{-2\sigma}$ and $\|\mathcal{C}_p\|_{S_\sigma^*}^2 \sim \frac{1}{\sigma} p^{2\sigma+1}$.

### 1.2 Relation to Prior Literature and Precise Separation of Contributions

We state carefully how the results of the present paper relate to and extend prior work:
- **Biorthogonal Annihilator Parameterization vs. Power-Saving Head Norm Asymptotics:** In `riemann_hypothesis_3` [10], we established the critical-line ($\sigma = 1/2$) rank-4 Archimedean-reciprocity decomposition of the Vasyunin Gram operator. In `riemann_hypothesis_7` [12, Theorem 2], we extended Vasyunin's biorthogonal step-difference system [4] to general Dirichlet series and already identified the unique head null vector $e_1 + \sum_{k=2}^N k^{-1} C_k^T e_{k-1}$, which is the step-difference coefficient vector of the head functional $\mathcal{F}_N = \sum_{k=1}^N k^{-1}\mathcal{C}_k$. Because the finite annihilator parameterization $\mathcal{L} = \alpha_1 \mathcal{F}_N + \sum_{n=N+1}^M \alpha_n \mathcal{C}_n$ follows directly from the biorthogonality in [4, 12], our substantive new contribution in **Theorem 1** is not the algebraic existence of $\mathcal{F}_N$, but its **exact power-saving asymptotic dual-norm law**
  
  $$
  \|\mathcal{F}_N\|_{S_\sigma^*}^2 = \frac{\zeta(2\sigma+1)}{2\sigma\,\zeta(4\sigma+2)}\, N^{2\sigma-1} + O_\sigma\!\left(N^{\sigma - 1/2}\right),
  $$
  
  proved via a three-regime decomposition into between-jump drift, small-$m$ multi-jump collisions, and isolated single jumps, together with the elementary zero-free bound $d_N(\sigma)^2 \ge c(\sigma)N^{-2\sigma}$ from the pure-tail squarefree functional $\mathcal{L}_{\mathrm{sqf}} = \sum_{N < n \le 2N}\mu(n)\mathcal{C}_n$.
- **Existential Rate Exponent [11, Theorem K] vs. Constructive Flat-Top Hermite Spline Annihilators:** In `riemann_hypothesis_6` [11, Theorem K], `span_of_dilates` already proved that any zero $\rho_0 = \beta_0 + i\gamma_0$ with $\beta_0 \in [1/2, \sigma)$ implies $d_N(\sigma)^2 \gg_\varepsilon N^{-2(\sigma-\beta_0)-\varepsilon}$ (and hence $\lim_{N\to\infty} \frac{-\log d_N(\sigma)}{\log N} = (\sigma - \Theta)^+$). The contribution of **Theorem 2** is a **constructive, explicit dual realization** of this rate inside $\operatorname{Ann}_{S_\sigma^*}(\tilde{\rho}_{1/2}, \dots, \tilde{\rho}_{1/N})$:
  1. We first prove that for any polynomial Cesàro/Riesz taper $(1 - u)^r$ ($r \ge 1$), although the Euler-Maclaurin $s=1$ pole integral cancels identically in $\gamma_k^{(M; \mathrm{poly}, r)}(\rho_0) = \alpha_k - k^{-1}\alpha_1$, the lower endpoint $j=1$ generates the full finite sum $\frac{2\sigma}{\rho_0}\sum_{m=1}^r (-1)^m \binom{r}{m}\zeta(\rho_0 - m)\frac{k^{m-\rho_0}-k^{-1}}{(M+1)^m}$, whose non-vanishing $m=1$ term restricts $|\gamma_k|$ to $\Theta\big(k^{1-\beta_0}/(M+1)\big)$.
  2. To eliminate all lower-end terms $\zeta(\rho_0 - m)$ ($m \ge 1$) while preserving $C^{r-1}$ smoothness at the upper cutoff, we introduce the **flat-top Hermite spline taper** $W_r(u)$ ($W_r \equiv 1$ on $[0, 1/2]$, $r \ge 2$), proving that $\gamma_k^{(M; W_r)}(\rho_0) = O_{\sigma,\rho_0,r}\big(k^r / (M+1)^{\beta_0 + r}\big)$.
  3. We establish a **universal divisor-sum norm inequality** $\left\|\sum_{k=2}^N \gamma_k \mathcal{C}_k\right\|_{S_\sigma^*}^2 \le C_\sigma N \sum_{k=2}^N k^{2\sigma}|\gamma_k|^2$ valid for *all* coefficient sequences $(\gamma_2, \dots, \gamma_N) \in \mathbb{C}^{N-1}$, and combine it with the flat-top Hermite spline at $M = \lfloor \Lambda N^{1 + 1/(\beta_0 + r)} \rfloor$ to construct an explicit finite-rank dual witness achieving $d_N(\sigma)^2 \gg_{\sigma,\rho_0,r} N^{-2(\sigma-\beta_0)(1 + 1/(\beta_0 + r))}$.
- **Periodic Hurwitz-Zeta Formula and Summation-by-Parts Tail Enclosures (Theorem 3):** Complementing the reciprocity formulas of Bettin and Conrey [7, 15], we derive a finite $\operatorname{lcm}(j,k)$-term Hurwitz-zeta identity for the shifted Báez-Duarte Gram matrix $(A_N(\sigma))_{j,k}$ (validated in pure 60-digit `mpmath.iv` interval Euler-Maclaurin summation) and pair it with a **Summation-by-Parts Periodic-Mean Tail Enclosure**. Using exact 64-bit integer cumulative sums over each period $\operatorname{lcm}(j,k)$ to compute the exact rational fluctuation constant $B(b)$ with zero floating-point conversion or ad-hoc padding, we reduce tail uncertainty from $O((M+1)^{-2\sigma})$ to $O((M+1)^{-2\sigma-1})$ ($92.2\times$ to $137.8\times$ reduction) and certify both $d_{40}(\sigma)^2$ ($M=5000$) and $d_{160}(\sigma)^2$ ($M=10000$) in 60-digit interval arithmetic.
- **Continuous and Step-Space Reproducing-Kernel Bounds [9, 13, 17] vs. Hybrid Step-Space Interval Certification (Theorem 4):** In the continuous setting, Burnol [17, Lemma 2.4] established the continuous Blaschke-product distance formula whose single conjugate-pair specialization underlies the continuous $H^2$ baseline $B_{\mathrm{2pt}, 0}^{(H^2)}(\sigma; \beta, \gamma) = 1 - \big(1 - \frac{4\sigma(\beta-\sigma)}{\beta^2+\gamma^2}\big)^2$, and Delaunay, Fricain, Mosaki, and Robert [13, Theorem 2.2 and Corollary 2.3] developed the weighted reproducing-kernel zero-free-disc mechanism. In the discrete step-space setting, `span_of_dilates` [9, Theorem C, Corollary D, and §6] (`riemann_hypothesis_2`) established step-space Gram-inverse bounds for finite sets of zeros, explicitly evaluated conjugate pairs, and compared them against the continuous bound. In **Theorem 4**, we extend [9, 13, 17] by introducing the **hybrid step-head + continuous-tail kernel** $k_{\rho, M}^{(\sigma)} = P_{S_\sigma^{(\le M)}} k_\rho + k_\rho \mathbf{1}_{(0, 1/(M+1)]}$, proving its strict Loewner monotonicity in the truncation cutoff $M$ and certifying its exact finite-$M$ lower bounds $B_{\mathrm{2pt}, 500}^{(S_\sigma)}$ and $B_{\mathrm{2pt}, 5000}^{(S_\sigma)}$ in 60-digit complex interval arithmetic (`mpmath.iv.mpc`).

---

## 2. Main Theoretical Results

### 2.1 Theorem 1: Step-Space Annihilator Structure and Power-Saving Head Norm Asymptotics

Recall from [4, 12] that the Vasyunin-Balazard step-difference functionals $\mathcal{C}_n \in S_\sigma^*$ ($n \ge 1$) are defined by

$$
\mathcal{C}_n(g) := \sum_{d \mid n} \mu\!\left(\frac{n}{d}\right)\big(g|_{I_d} - g|_{I_{d-1}}\big) = \sum_{m=1}^n c_{n,m}\, g|_{I_m}, \qquad c_{n,m} := \mu\!\left(\frac{n}{m}\right)\mathbf{1}_{m \mid n} - \mu\!\left(\frac{n}{m+1}\right)\mathbf{1}_{(m+1) \mid n},
$$

where $g|_{I_0} := 0$. By [12, Theorem 2], $\mathcal{C}_1(E) = 1$, $\mathcal{C}_1(\tilde{\rho}_{1/k}) = -1/k$, and for $n \ge 2$, $\mathcal{C}_n(E) = \mu(n)$ and $\mathcal{C}_n(\tilde{\rho}_{1/k}) = \delta_{n,k}$ ($k \ge 2$). Consequently, a finitely supported functional $\mathcal{L} = \sum_{n=1}^M \alpha_n \mathcal{C}_n$ ($M \ge N$) lies in $\operatorname{Ann}_{S_\sigma^*}(\tilde{\rho}_{1/2}, \dots, \tilde{\rho}_{1/N})$ if and only if $\alpha_k = \alpha_1 / k$ for all $1 \le k \le N$, i.e.,

$$
\mathcal{L} = \alpha_1 \mathcal{F}_N + \sum_{n=N+1}^M \alpha_n \mathcal{C}_n, \qquad \mathcal{F}_N := \sum_{k=1}^N \frac{1}{k}\mathcal{C}_k, \qquad \mathcal{L}(E) = \alpha_1 M_1(N) + \sum_{n=N+1}^M \alpha_n \mu(n),
$$

where $M_1(x) := \sum_{1 \le j \le x} \frac{\mu(j)}{j}$.

**Theorem 1 (Zero-Free Tail Bound and Power-Saving Asymptotic Head Norm Law).**
*Fix $\sigma \in (1/2, 1)$ and $N \ge 2$. Then:*

1. **Zero-Free Pure-Tail Squarefree Lower Bound:** *The pure-tail squarefree functional $\mathcal{L}_{\mathrm{sqf}} := \sum_{N < n \le 2N} \mu(n)\mathcal{C}_n \in \operatorname{Ann}_{S_\sigma^*}(\tilde{\rho}_{1/2}, \dots, \tilde{\rho}_{1/N})$ ($\alpha_1 = 0$) satisfies $\mathcal{L}_{\mathrm{sqf}}(E) = \sum_{N < n \le 2N} \mu(n)^2 = \frac{6}{\pi^2}N + O(N^{1/2})$ and $\|\mathcal{L}_{\mathrm{sqf}}\|_{S_\sigma^*}^2 \asymp_\sigma N^{2\sigma+2}$, yielding the elementary, zero-free lower bound $d_N(\sigma)^2 \ge |\mathcal{L}_{\mathrm{sqf}}(E)|^2 / \|\mathcal{L}_{\mathrm{sqf}}\|_{S_\sigma^*}^2 \ge c(\sigma) N^{-2\sigma}$.*

2. **Closed-Form Head Distance Identity and Power-Saving Asymptotic Norm Law:** *The head functional $\mathcal{F}_N = \sum_{k=1}^N k^{-1}\mathcal{C}_k$ ($\alpha_1 = 1, \alpha_{>N} = 0$) is supported on $I_1 \cup \dots \cup I_N$ with step-jump weights $\mathcal{F}_N(g) = \sum_{m=1}^N (\beta_m^{(N)} - \beta_{m+1}^{(N)}) g|_{I_m}$, where $\beta_m^{(N)} = \frac{1}{m} M_1(N/m)$ ($1 \le m \le N$) and $\beta_{N+1}^{(N)} = 0$. The head-truncated squared distance satisfies the exact identity*

$$
d_N(\sigma)^2 \ge d_N^{(\le N)}(\sigma)^2 := \operatorname{dist}_{L^2(I_1 \cup \dots \cup I_N, d\mu_\sigma)}^2\big(E, \operatorname{span}_{2\le k\le N}\{\tilde{\rho}_{1/k}\}\big) = \frac{M_1(N)^2}{\|\mathcal{F}_N\|_{S_\sigma^*}^2} = \frac{M_1(N)^2}{\sum_{m=1}^N \frac{(\beta_m^{(N)} - \beta_{m+1}^{(N)})^2}{m^{-2\sigma} - (m+1)^{-2\sigma}}},
$$

*and as $N \to \infty$, $\|\mathcal{F}_N\|_{S_\sigma^*}^2$ obeys the power-saving asymptotic law*

$$
\|\mathcal{F}_N\|_{S_\sigma^*}^2 = \frac{\zeta(2\sigma + 1)}{2\sigma\,\zeta(4\sigma + 2)}\, N^{2\sigma - 1} + O_\sigma\!\left(N^{\sigma - 1/2}\right).
$$

**Proof.**
**(1)** Because $E, \tilde{\rho}_{1/k} \in S_\sigma$, Hahn-Banach duality in $S_\sigma$ gives $d_N(\sigma)^2 = \sup_{\mathcal{L} \in \operatorname{Ann}_{S_\sigma^*} \setminus \{0\}} |\mathcal{L}(E)|^2 / \|\mathcal{L}\|_{S_\sigma^*}^2$. For $\mathcal{L}_{\mathrm{sqf}} = \sum_{N < n \le 2N} \mu(n)\mathcal{C}_n$, the step-jump weights are $\beta_d = \sum_{N/d < j \le 2N/d} \mu(dj)\mu(j)$, so $|\beta_d| \le \frac{N}{d} + 1$, $|\beta_m - \beta_{m+1}| \le 2\frac{N}{m} + 2$, and $\|\mathcal{L}_{\mathrm{sqf}}\|_{S_\sigma^*}^2 = \sum_{m=1}^{2N} \frac{(\beta_m - \beta_{m+1})^2}{w_m^{(\sigma)}} \ll_\sigma \sum_{m=1}^{2N} m^{2\sigma+1}\big(\frac{N^2}{m^2} + 1\big) \ll_\sigma N^{2\sigma+2}$, giving $d_N(\sigma)^2 \ge |\mathcal{L}_{\mathrm{sqf}}(E)|^2 / \|\mathcal{L}_{\mathrm{sqf}}\|_{S_\sigma^*}^2 \gg_\sigma N^{-2\sigma}$.

**(2)** For $\mathcal{F}_N = \sum_{k=1}^N \frac{1}{k}\mathcal{C}_k$, writing $k = d j$ gives $\beta_d^{(N)} = \sum_{j=1}^{\lfloor N/d \rfloor} \frac{\mu(j)}{dj} = \frac{M_1(N/d)}{d}$ for $1 \le d \le N$ and $\beta_{N+1}^{(N)} = 0$. Since $\{\tilde{\rho}_{1/k}|_{I_1\cup\dots\cup I_N}\}_{2\le k\le N}$ are linearly independent in the $N$-dimensional space $S_\sigma^{(\le N)} \cong \mathbb{C}^N$ and $\mathcal{F}_N$ spans their 1-dimensional orthogonal complement [12, Theorem 2], projection onto $\mathcal{F}_N$ gives $d_N^{(\le N)}(\sigma)^2 = |\mathcal{F}_N(E)|^2 / \|\mathcal{F}_N\|_{S_\sigma^*}^2 = M_1(N)^2 / \|\mathcal{F}_N\|_{S_\sigma^*}^2$.

To prove the power-saving asymptotic norm law, decompose the step difference $c_m^{(N)} := \beta_m^{(N)} - \beta_{m+1}^{(N)}$ ($1 \le m \le N$) into its **harmonic-jump** and **between-jump drift** components:

$$
c_m^{(N)} = \frac{M_1(N/m) - M_1(N/(m+1))}{m} + \frac{M_1(N/(m+1))}{m(m+1)} =: J_m^{(N)} + D_m^{(N)},
$$

where $J_m^{(N)} := \frac{1}{m}\sum_{\frac{N}{m+1} < j \le \frac{N}{m}} \frac{\mu(j)}{j}$ and $D_m^{(N)} := \frac{M_1(N/(m+1))}{m(m+1)}$. Let $K := \lfloor N^{1/2} \rfloor$. We bound the three regimes separately:
- **Regime A (Between-Jump Drift $D_m^{(N)}$ across $1 \le m \le N$):** Since $|M_1(x)| \le 1$ for all $x \ge 1$, $|D_m^{(N)}| \le \frac{1}{m(m+1)}$. Using $(w_m^{(\sigma)})^{-1} = \frac{m^{2\sigma+1}}{2\sigma}\big(1 + O(m^{-1})\big) \ll_\sigma m^{2\sigma+1}$, the total drift norm squared is
  
  $$
  \|D^{(N)}\|_{S_\sigma^*}^2 = \sum_{m=1}^N \frac{(D_m^{(N)})^2}{w_m^{(\sigma)}} \ll_\sigma \sum_{m=1}^N m^{2\sigma+1} m^{-4} = \sum_{m=1}^N m^{2\sigma - 3} = O_\sigma(1),
  $$
  
  since $2\sigma - 3 < -1$ for all $\sigma < 1$.
- **Regime B (Small-$m$ / Multi-Jump Collision Tail $1 \le m \le K = \lfloor N^{1/2} \rfloor$):** For any $1 \le m \le K$, the harmonic sum over $(N/(m+1), N/m]$ satisfies $|J_m^{(N)}| \le \frac{1}{m}\sum_{N/(m+1) < j \le N/m} \frac{1}{j} \le \frac{1}{m}\log\frac{m+1}{m} + \frac{m+1}{m N} \ll \frac{1}{m^2} + \frac{1}{N}$. Therefore, the contribution of all $1 \le m \le K$ (which contains all multi-jump collisions where $\lfloor N/m \rfloor - \lfloor N/(m+1) \rfloor \ge 2$) is bounded by
  
  $$
  \sum_{m=1}^K \frac{(J_m^{(N)})^2}{w_m^{(\sigma)}} \ll_\sigma \sum_{m=1}^K m^{2\sigma+1}\!\left(\frac{1}{m^4} + \frac{1}{N^2}\right) \ll_\sigma 1 + K^{2\sigma+2} N^{-2} = O_\sigma\!\left(1 + N^{\sigma - 1}\right) = O_\sigma(1).
  $$

- **Regime C (Isolated Single Jumps $K < m \le N$, i.e. $1 \le j \le J_{\max} := \lfloor N/(K+1) \rfloor \approx N^{1/2}$):** For $m > N^{1/2}$, $\frac{N}{m} - \frac{N}{m+1} = \frac{N}{m(m+1)} < 1$, so each interval $(N/(m+1), N/m]$ contains **at most one integer** $j$. Specifically, for each $1 \le j \le J_{\max}$, there is a unique index $m_j = \lfloor N/j \rfloor > K$ such that $j \in (N/(m_j+1), N/m_j]$, and on that $m_j$ we have $J_{m_j}^{(N)} = \frac{\mu(j)}{j\, m_j}$ (while $J_m^{(N)} = 0$ for all other $m > K$). Since $m_j = \frac{N}{j} + O(1)$, we have
  
  $$
  \frac{(J_{m_j}^{(N)})^2}{w_{m_j}^{(\sigma)}} = \frac{\mu(j)^2}{j^2 m_j^2} \cdot \frac{m_j^{2\sigma+1}}{2\sigma}\left(1 + O(m_j^{-1})\right) = \frac{\mu(j)^2}{2\sigma\, j^{2\sigma+1}}\, N^{2\sigma-1}\left(1 + O\!\left(\frac{j}{N}\right)\right).
  $$
  
  Summing over $1 \le j \le J_{\max} \asymp N^{1/2}$ gives
  
  $$
  \sum_{m=K+1}^N \frac{(J_m^{(N)})^2}{w_m^{(\sigma)}} = \frac{N^{2\sigma-1}}{2\sigma}\sum_{j=1}^{J_{\max}} \frac{\mu(j)^2}{j^{2\sigma+1}} + O_\sigma\!\left(N^{2\sigma-2}\sum_{j=1}^{J_{\max}} j^{-2\sigma}\right) = \frac{\zeta(2\sigma+1)}{2\sigma\,\zeta(4\sigma+2)}\,N^{2\sigma-1} + O_\sigma\!\left(N^{\sigma - 1}\right),
  $$
  
  where we used $\sum_{j > J_{\max}} j^{-2\sigma-1} \ll J_{\max}^{-2\sigma} \ll N^{-\sigma}$ and $\sum_{j=1}^\infty \mu(j)^2 j^{-s} = \zeta(s)/\zeta(2s)$ at $s = 2\sigma+1$. Combining Regimes B and C gives $\|J^{(N)}\|_{S_\sigma^*}^2 = \frac{\zeta(2\sigma+1)}{2\sigma\zeta(4\sigma+2)}N^{2\sigma-1} + O_\sigma(1)$. Finally, by Cauchy-Schwarz and Regime A, the cross term satisfies $2\big|\langle J^{(N)}, D^{(N)} \rangle_{S_\sigma^*}\big| \le 2\|J^{(N)}\|_{S_\sigma^*} \|D^{(N)}\|_{S_\sigma^*} \ll_\sigma N^{\sigma - 1/2}$, yielding $\|\mathcal{F}_N\|_{S_\sigma^*}^2 = \|J^{(N)} + D^{(N)}\|_{S_\sigma^*}^2 = \frac{\zeta(2\sigma+1)}{2\sigma\zeta(4\sigma+2)}N^{2\sigma-1} + O_\sigma(N^{\sigma-1/2})$. $\square$

---

### 2.2 Theorem 2: Lower-End Zeta Obstruction for Polynomial Tapers and Constructive Flat-Top Hermite Spline Zero Annihilators

For any cutoff $M \ge 2N$, any weight profile $W : [0, \infty) \to [0, 1]$ vanishing on $[1, \infty)$ with $W(0) = 1$, and any zero $\rho_0 = \beta_0 + i\gamma_0$ ($\beta_0 \in [1/2, \sigma)$) of $\zeta(s)$, define the tapered step functional $\mathcal{L}_{\rho_0}^{(M; W)} \in S_\sigma^*$ supported on $I_1 \cup \dots \cup I_M$ with step-jump weights

$$
\beta_d^{(M; W)}(\rho_0) := \frac{2\sigma}{\rho_0}\, d^{-\rho_0}\, W\!\left(\frac{d}{M+1}\right) \mathbf{1}_{1 \le d \le M},
$$

its Vasyunin-Balazard coordinates $\alpha_k^{(M; W)}(\rho_0) := \sum_{j=1}^{\lfloor M/k \rfloor} \beta_{k j}^{(M; W)}(\rho_0)$ ($1 \le k \le N$), and its biorthogonal projection onto $\operatorname{Ann}_{S_\sigma^*}(\tilde{\rho}_{1/2}, \dots, \tilde{\rho}_{1/N})$:

$$
\widetilde{\mathcal{L}}_{\rho_0, N}^{(M; W)} := \mathcal{L}_{\rho_0}^{(M; W)} - \sum_{k=2}^N \gamma_k^{(M; W)}(\rho_0)\,\mathcal{C}_k, \qquad \gamma_k^{(M; W)}(\rho_0) := \mathcal{L}_{\rho_0}^{(M; W)}(\tilde{\rho}_{1/k}) = \alpha_k^{(M; W)}(\rho_0) - \frac{1}{k}\alpha_1^{(M; W)}(\rho_0).
$$

Before analyzing the residuals $\gamma_k^{(M; W)}(\rho_0)$, we establish a **universal divisor-sum norm inequality** for the head correction $\sum_{k=2}^N \gamma_k \mathcal{C}_k$ that holds for *arbitrary* coefficients $(\gamma_2, \dots, \gamma_N) \in \mathbb{C}^{N-1}$ without requiring any regularity across consecutive indices.

**Lemma 1 (Universal Divisor-Sum Norm Inequality for Head Corrections).**
*For every $\sigma > 1/2$, every $N \ge 2$, and every vector $(\gamma_2, \dots, \gamma_N) \in \mathbb{C}^{N-1}$,*

$$
\left\|\sum_{k=2}^N \gamma_k \mathcal{C}_k\right\|_{S_\sigma^*}^2 \le C_\sigma\, N \sum_{k=2}^N k^{2\sigma} |\gamma_k|^2 \le C_\sigma\, N^{2\sigma + 1} \sum_{k=2}^N |\gamma_k|^2 \le C_\sigma\, N^{2\sigma + 2} \max_{2 \le k \le N} |\gamma_k|^2, \qquad C_\sigma := \frac{3^{2\sigma+1}}{\sigma}\zeta(2\sigma).
$$

**Proof of Lemma 1.**
Set $\mathcal{H}_N := \sum_{k=2}^N \gamma_k \mathcal{C}_k$. Writing $\mathcal{C}_k(g) = \sum_{d \mid k} \mu(k/d)(g|_{I_d} - g|_{I_{d-1}})$, we have $\mathcal{H}_N(g) = \sum_{m=1}^N (\eta_m - \eta_{m+1}) g|_{I_m}$ where $\eta_{N+1} = 0$ and $\eta_m = \sum_{j=1}^{\lfloor N/m \rfloor} \gamma_{m j} \mu(j)$ for $1 \le m \le N$ (setting $\gamma_1 := 0$). Since $(w_m^{(\sigma)})^{-1} \le \frac{(m+1)^{2\sigma+1}}{2\sigma}$ and $|\eta_m - \eta_{m+1}|^2 \le 2|\eta_m|^2 + 2|\eta_{m+1}|^2$, we have

$$
\|\mathcal{H}_N\|_{S_\sigma^*}^2 = \sum_{m=1}^N \frac{|\eta_m - \eta_{m+1}|^2}{w_m^{(\sigma)}} \le \frac{2^{2\sigma+1}}{\sigma}|\eta_1|^2 + \sum_{m=2}^N \frac{2(m^{2\sigma+1} + (m+1)^{2\sigma+1})}{2\sigma}|\eta_m|^2 \le \frac{3^{2\sigma+1}}{\sigma}\sum_{m=1}^N m^{2\sigma+1}|\eta_m|^2.
$$

For each $1 \le m \le N$, Cauchy-Schwarz gives $|\eta_m|^2 \le \lfloor N/m \rfloor \sum_{j=1}^{\lfloor N/m \rfloor} |\gamma_{m j}|^2 \le \frac{N}{m}\sum_{j=1}^{\lfloor N/m \rfloor} |\gamma_{m j}|^2$. Multiplying by $m^{2\sigma+1}$, summing over $1 \le m \le N$, and substituting $k = m j$ ($2 \le k \le N$), we obtain

$$
\sum_{m=1}^N m^{2\sigma+1}|\eta_m|^2 \le N \sum_{m=1}^N m^{2\sigma} \sum_{j=1}^{\lfloor N/m \rfloor} |\gamma_{m j}|^2 = N \sum_{k=2}^N |\gamma_k|^2 \sum_{m \mid k} m^{2\sigma} \le \zeta(2\sigma)\, N \sum_{k=2}^N k^{2\sigma}|\gamma_k|^2,
$$

since $\sum_{m \mid k} m^{2\sigma} = k^{2\sigma}\sum_{j \mid k} j^{-2\sigma} < \zeta(2\sigma) k^{2\sigma}$ for $\sigma > 1/2$. $\square$

*(Remark: Lemma 1 is sharp in its $N$-exponent for general coefficients: if $\gamma_k = (-1)^k \mathbf{1}_{N/2 < k \le N}$, then $\eta_m = (-1)^m$ on $N/2 < m \le N$, so $|\eta_m - \eta_{m+1}| = 2$ and both sides of Lemma 1 are of order $N^{2\sigma+2}$.)*

**Theorem 2 (Polynomial Lower-End Zeta Obstruction and Constructive Flat-Top Hermite Spline Zero Annihilators).**
*Let $\rho_0 = \beta_0 + i\gamma_0$ ($\beta_0 \in [1/2, \sigma)$) be a zero of $\zeta(s)$, and fix $2 \le N \le (M+1)/2$ and $X_k := \frac{M+1}{k} \ge 2$. Then:*

1. **Full Lower-End Zeta Expansion and $(M+1)^{-1}$ Obstruction for Polynomial Cesàro/Riesz Tapers:** *For the polynomial taper $W_{\mathrm{poly}, r}(u) := (1 - u)^r$ ($r \ge 1$), Euler-Maclaurin summation of order $r$ gives, for all $1 \le k \le N$,*

$$
\alpha_k^{(M; \mathrm{poly}, r)}(\rho_0) = \frac{2\sigma}{\rho_0}\,k^{-\rho_0}\left[I_{\mathrm{poly}, r}(\rho_0)\,X_k^{1-\rho_0} + \sum_{m=1}^r (-1)^m \binom{r}{m} \frac{\zeta(\rho_0 - m)}{X_k^m} + O_{\rho_0, r}\!\left(X_k^{-\beta_0 - r}\right)\right],
$$

*where $I_{\mathrm{poly}, r}(\rho_0) = \int_0^1 u^{-\rho_0}(1 - u)^r\,du = \frac{r!}{\prod_{j=0}^r (1 - \rho_0 + j)}$. Although the $s=1$ pole integral $I_{\mathrm{poly}, r}(\rho_0) X_k^{1-\rho_0}$ cancels identically in $\gamma_k^{(M; \mathrm{poly}, r)}(\rho_0) = \alpha_k^{(M; \mathrm{poly}, r)}(\rho_0) - \frac{1}{k}\alpha_1^{(M; \mathrm{poly}, r)}(\rho_0)$, all $m = 1, \dots, r$ lower-endpoint zeta terms remain:*

$$
\gamma_k^{(M; \mathrm{poly}, r)}(\rho_0) = \frac{2\sigma}{\rho_0}\sum_{m=1}^r (-1)^m \binom{r}{m} \zeta(\rho_0 - m)\,\frac{k^{m - \rho_0} - k^{-1}}{(M+1)^m} + O_{\sigma,\rho_0,r}\!\left(\frac{k^r}{(M+1)^{\beta_0 + r}}\right) \qquad (2 \le k \le N).
$$

*In particular, because $\zeta(\rho_0 - 1) \ne 0$ (by the functional equation, since $\operatorname{Re}(2 - \rho_0) = 2 - \beta_0 > 1$), the $m=1$ term is non-vanishing for every $r \ge 1$ and restricts $|\gamma_k^{(M; \mathrm{poly}, r)}(\rho_0)|$ to $\Theta_{\sigma,\rho_0,r}\big(k^{1-\beta_0} / (M+1)\big)$.*

2. **Elimination of All Lower-End Zeta Terms via Flat-Top Hermite Spline Tapers:** *For any integer $r \ge 2$ and flat-top knot $\theta \in [1/2, 1)$, define the $C^{r-1}([0, \infty))$ **flat-top Hermite spline taper***

$$
W_{r, \theta}(u) := \begin{cases} 1, & 0 \le u \le \theta, \\[4pt] \left(\frac{1 - u}{1 - \theta}\right)^r \sum_{j=0}^{r-1} \binom{r - 1 + j}{j} \left(\frac{u - \theta}{1 - \theta}\right)^j, & \theta < u < 1, \\[4pt] 0, & u \ge 1 \end{cases}
$$

*(and write $W_r := W_{r, 1/2}$ at $\theta = 1/2$). Because $W_{r,\theta}(u) \equiv 1$ on $[0, \theta]$ and $W_{r,\theta}^{(l)}(\theta^-) = W_{r,\theta}^{(l)}(\theta^+) = 0$ ($1 \le l \le r-1$) while $W_{r,\theta}^{(l)}(1^-) = 0$ ($0 \le l \le r-1$), all lower-endpoint terms $\zeta(\rho_0 - m)$ ($m \ge 1$) vanish identically, yielding for all $1 \le k \le N$ ($X_k = \frac{M+1}{k} \ge \frac{2}{\theta}$):*

$$
\alpha_k^{(M; W_{r,\theta})}(\rho_0) = \frac{2\sigma}{\rho_0}\,k^{-\rho_0}\left[I_{W_{r,\theta}}(\rho_0)\,X_k^{1-\rho_0} + O_{\rho_0, r, \theta}\!\left(X_k^{-\beta_0 - r}\right)\right], \qquad I_{W_{r,\theta}}(\rho_0) := \int_0^1 u^{-\rho_0} W_{r,\theta}(u)\,du,
$$

*and hence, after exact cancellation of the $I_{W_{r,\theta}}(\rho_0) X_k^{1-\rho_0}$ term,*

$$
\big|\gamma_k^{(M; W_{r,\theta})}(\rho_0)\big| = \left|\alpha_k^{(M; W_{r,\theta})}(\rho_0) - \frac{1}{k}\alpha_1^{(M; W_{r,\theta})}(\rho_0)\right| \ll_{\sigma,\rho_0,r,\theta} k^{-\beta_0} X_k^{-\beta_0 - r} + \frac{1}{k}(M+1)^{-\beta_0 - r} \ll_{\sigma,\rho_0,r,\theta} \frac{k^r}{(M+1)^{\beta_0 + r}}.
$$

3. **Constructive Step-Space Realization of $d_N(\sigma)^2 \gg N^{-2(\sigma - \beta_0) - \varepsilon}$:** *Since $\lim_{\theta \to 1^-} I_{W_{r,\theta}}(\rho_0) = \frac{1}{1 - \rho_0} \ne 0$, fix $\theta \in [1/2, 1)$ such that $I_{W_{r,\theta}}(\rho_0) \ne 0$ (e.g., $\theta = 1/2$ for $\rho_1 = \frac{1}{2} + i\cdot 14.134725\dots$), and set*

$$
M := \left\lfloor \Lambda\, N^{1 + \frac{1}{\beta_0 + r}} \right\rfloor \qquad (\Lambda \ge 4/\theta).
$$

*Then by Lemma 1 and part (2), the target perturbation and head-correction dual norm squared satisfy*

$$
\sum_{k=2}^N \big|\gamma_k^{(M; W_{r,\theta})}(\rho_0)\big| \ll_{\sigma,\rho_0,r,\theta} \frac{N^{r+1}}{(M+1)^{\beta_0 + r}} \le \Lambda^{-(\beta_0 + r)}\,N^{-\beta_0} \le \Lambda^{-(\beta_0 + r)},
$$

$$
\left\|\sum_{k=2}^N \gamma_k^{(M; W_{r,\theta})}(\rho_0)\,\mathcal{C}_k\right\|_{S_\sigma^*}^2 \le C_\sigma N \sum_{k=2}^N k^{2\sigma}\big|\gamma_k^{(M; W_{r,\theta})}(\rho_0)\big|^2 \ll_{\sigma,\rho_0,r,\theta} \frac{N^{2\sigma + 2r + 2}}{(M+1)^{2\beta_0 + 2r}} \le \Lambda^{-2(\beta_0 + r)}\,N^{2(\sigma - \beta_0)},
$$

*while $\|\mathcal{L}_{\rho_0}^{(M; W_{r,\theta})}\|_{S_\sigma^*}^2 \ll_{\sigma,\rho_0,r,\theta} M^{2(\sigma - \beta_0)} \ll \Lambda^{2(\sigma-\beta_0)} N^{2(\sigma - \beta_0)\left(1 + \frac{1}{\beta_0 + r}\right)}$ and $\widetilde{\mathcal{L}}_{\rho_0, N}^{(M; W_{r,\theta})}(E) = \frac{2\sigma}{\rho_0} - \sum_{k=2}^N \mu(k)\gamma_k^{(M; W_{r,\theta})}(\rho_0)$. Choosing $\Lambda = \Lambda(\sigma, \rho_0, r, \theta)$ sufficiently large ensures $\big|\widetilde{\mathcal{L}}_{\rho_0, N}^{(M; W_{r,\theta})}(E)\big| \ge \frac{\sigma}{|\rho_0|} > 0$ and yields the explicit finite-rank dual witness lower bound*

$$
d_N(\sigma)^2 \ge \frac{\big|\widetilde{\mathcal{L}}_{\rho_0, N}^{(M; W_{r,\theta})}(E)\big|^2}{\big\|\widetilde{\mathcal{L}}_{\rho_0, N}^{(M; W_{r,\theta})}\big\|_{S_\sigma^*}^2} \gg_{\sigma,\rho_0,r,\theta} N^{-2(\sigma - \beta_0)\left(1 + \frac{1}{\beta_0 + r}\right)} \qquad (\forall\, r \ge 2),
$$

*and hence $d_N(\sigma)^2 \gg_{\sigma,\rho_0,\varepsilon} N^{-2(\sigma - \beta_0) - \varepsilon}$ for every $\varepsilon > 0$ by taking $r > \frac{2(\sigma - \beta_0)}{\varepsilon}$.*

**Proof.**
**(1)** For $W_{\mathrm{poly}, r}(u) = (1 - u)^r = \sum_{m=0}^r (-1)^m \binom{r}{m} u^m$ and $X = X_k \ge 2$, we have $\sum_{j=1}^{\lfloor X \rfloor} j^{-\rho_0}(1 - j/X)^r = \sum_{m=0}^r (-1)^m \binom{r}{m} X^{-m} \sum_{j=1}^{\lfloor X \rfloor} j^{m - \rho_0}$. Applying Euler-Maclaurin summation of order $r$ to each sum $\sum_{j=1}^{\lfloor X \rfloor} j^{m - \rho_0}$ and recombining $g_X(t) := t^{-\rho_0}(1 - t/X)^r$, the constant terms at the lower endpoint $t=1$ produce $\sum_{m=0}^r (-1)^m \binom{r}{m} \zeta(\rho_0 - m) X^{-m}$ (where the $m=0$ term vanishes because $\zeta(\rho_0) = 0$), the main integrals combine into $\int_0^X g_X(t)\,dt = X^{1-\rho_0} I_{\mathrm{poly}, r}(\rho_0)$, and the upper-endpoint Bernoulli terms at $t = \lfloor X \rfloor = X - \{X\}$ vanish up to order $r-1$ because $g_X^{(l)}(X) = 0$ for $0 \le l \le r-1$, leaving an upper-endpoint remainder bounded after one integration by parts of $\tilde{B}_r(t) = \tilde{B}_{r+1}'(t)/(r+1)$ by $O_{\rho_0, r}(X^{-\beta_0 - r})$. Multiplying by $\frac{2\sigma}{\rho_0} k^{-\rho_0}$ and forming $\gamma_k^{(M; \mathrm{poly}, r)}(\rho_0) = \alpha_k - k^{-1}\alpha_1$, the pole term $k^{-\rho_0} X_k^{1-\rho_0} = (M+1)^{1-\rho_0}/k$ cancels identically, while $k^{-\beta_0} X_k^{-\beta_0 - r} = k^r / (M+1)^{\beta_0 + r}$ gives the stated expansion.

**(2) & (3)** By standard two-point Hermite interpolation on $[\theta, 1]$, the polynomial $P_r(v) = v^r \sum_{j=0}^{r-1}\binom{r-1+j}{j}(1-v)^j$ ($v = \frac{1-u}{1-\theta}$) satisfies $P_r(0) = P_r'(0) = \dots = P_r^{(r-1)}(0) = 0$ and $P_r(1) = 1, P_r'(1) = \dots = P_r^{(r-1)}(1) = 0$ (since $1 - P_r(v) = (1-v)^r \sum_{j=0}^{r-1}\binom{r-1+j}{j} v^j = O((1-v)^r)$ near $v=1$). Thus $g_X(t) := t^{-\rho_0} W_{r,\theta}(t/X)$ belongs to $C^{r-1}([1, \infty))$, equals $t^{-\rho_0}$ identically on $[1, \theta X]$, and vanishes identically on $[X, \infty)$. Applying Euler-Maclaurin summation of order $r$ on $[1, \infty)$ to both $g_X(t)$ and $t^{-\rho_0}$ (for $X \ge 2/\theta > 2$) and subtracting, all lower-endpoint terms at $t=1$ and the remainder integral on $[1, \theta X]$ cancel **identically**, and all boundary terms of order $\le r-1$ at the knots $t = \theta X$ and $t = X$ vanish by $C^{r-1}$ continuity of $g_X$, leaving the exact identity

$$
\sum_{j=1}^{\lfloor X \rfloor} g_X(j) - \zeta(\rho_0) - X^{1-\rho_0} I_{W_{r,\theta}}(\rho_0) = \frac{(-1)^{r+1}}{r!}\int_{\theta X}^X \tilde{B}_r(t)\,g_X^{(r)}(t)\,dt - \frac{(-1)^{r+1}}{r!}\int_{\theta X}^\infty \tilde{B}_r(t)\,\frac{d^r}{dt^r}\big(t^{-\rho_0}\big)\,dt.
$$

Integrating $\tilde{B}_r(t) = \frac{1}{r+1}\tilde{B}_{r+1}'(t)$ by parts once on $[\theta X, X]$ and $[\theta X, \infty)$ and using $\sup_{[\theta X, X]} |g_X^{(r)}(t)| + X \sup_{(\theta X, X)} |g_X^{(r+1)}(t)| \ll_{\rho_0, r, \theta} X^{-\beta_0 - r}$ bounds the right-hand side by $O_{\rho_0, r, \theta}(X^{-\beta_0 - r})$. Multiplying by $\frac{2\sigma}{\rho_0}k^{-\rho_0}$ and forming $\alpha_k - k^{-1}\alpha_1$ cancels $I_{W_{r,\theta}}(\rho_0) X_k^{1-\rho_0}$ and yields $|\gamma_k^{(M; W_{r,\theta})}(\rho_0)| \ll_{\sigma,\rho_0,r,\theta} k^r / (M+1)^{\beta_0 + r}$. Finally, substituting this bound into Lemma 1 with $M = \lfloor \Lambda N^{1 + 1/(\beta_0 + r)} \rfloor$ gives $(M+1)^{2\beta_0 + 2r} \ge \Lambda^{2\beta_0 + 2r} N^{2\beta_0 + 2r + 2}$, so $\frac{N^{2\sigma + 2r + 2}}{(M+1)^{2\beta_0 + 2r}} \le \Lambda^{-2(\beta_0 + r)} N^{2(\sigma - \beta_0)}$. Since $|\beta_m^{(M; W_{r,\theta})} - \beta_{m+1}^{(M; W_{r,\theta})}| \ll_{\sigma,\rho_0,r,\theta} m^{-\beta_0 - 1}$ on $1 \le m \le M$, we have $\|\mathcal{L}_{\rho_0}^{(M; W_{r,\theta})}\|_{S_\sigma^*}^2 \ll \sum_{m=1}^M m^{2\sigma+1} m^{-2\beta_0-2} \ll M^{2(\sigma-\beta_0)}$, completing the proof. $\square$

---

### 2.3 Theorem 3: Periodic Hurwitz-Zeta Gram Formula and Summation-by-Parts Periodic-Mean Tail Enclosures

**Theorem 3 (Periodic Hurwitz-Zeta Gram Identity, Summation-by-Parts Tail Enclosure, and $\kappa(\sigma)$ Remainder Bound).**
*Fix $\sigma \in (1/2, 1)$.*

1. **One-Line Periodic Hurwitz-Zeta Formula for $A_N(\sigma)$:** *For any $j, k \ge 2$, let $L = \operatorname{lcm}(j, k)$ and $g = \gcd(j, k)$. Then the shifted Báez-Duarte Gram entry $(A_N(\sigma))_{j,k} = \langle \tilde{\rho}_{1/j}, \tilde{\rho}_{1/k} \rangle_{L^2(d\mu_\sigma)} = \sum_{m=1}^\infty w_m^{(\sigma)} \{m/j\}\{m/k\}$ is given in closed form by the finite $L$-term Hurwitz-zeta sum*

$$
\big(A_N(\sigma)\big)_{j,k} = L^{-2\sigma} \sum_{r=1}^L \left(\left\{\frac{r}{j}\right\}\left\{\frac{r}{k}\right\} - \left\{\frac{r-1}{j}\right\}\left\{\frac{r-1}{k}\right\}\right) \zeta\!\left(2\sigma, \frac{r}{L}\right).
$$

2. **Summation-by-Parts Periodic-Mean Tail Enclosure for Trial Vectors:** *Let $b = (b_2, \dots, b_N) \in \mathbb{R}^{N-1}$ be any trial vector, and let $f_m := \big(1 - \sum_{k=2}^N b_k \{m/k\}\big)^2$. Then $f_m$ is periodic in $m$ with period $L_N = \operatorname{lcm}(2, \dots, N)$, its exact rational periodic average over a full period is*

$$
\bar{f}(b) := \frac{1}{L_N}\sum_{r=1}^{L_N} f_r = 1 - \sum_{k=2}^N b_k\,\frac{k - 1}{k} + \sum_{j,k=2}^N b_j b_k \left(\frac{(j-1)(k-1)}{4jk} + \frac{\gcd(j,k)^2 - 1}{12jk}\right),
$$

*and its zero-mean fluctuation $f_m - \bar{f}(b)$ has partial sums uniformly bounded for all $M < m_2$ by the exact rational pairwise variation constant*

$$
\left|\sum_{n=M+1}^{m_2} \big(f_n - \bar{f}(b)\big)\right| \le B(b) := \sum_{k=2}^N 2|b_k|\,\frac{\lfloor k/2 \rfloor \lceil k/2 \rceil}{2k} + \sum_{j,k=2}^N |b_j|\,|b_k|\,B_{j,k},
$$

*where $B_{j,k} := \max_{0 \le u \le \operatorname{lcm}(j,k)} S_{j,k}(u) - \min_{0 \le u \le \operatorname{lcm}(j,k)} S_{j,k}(u)$ with $12 j k\, S_{j,k}(u) = \sum_{r=1}^u \big(12(r \bmod j)(r \bmod k) - [3(j-1)(k-1) + \gcd(j,k)^2 - 1]\big) \in \mathbb{Z}$. Consequently, for every truncation cutoff $M \ge 1$, the squared norm $d_N(\sigma; b)^2 := \|E + \sum_{k=2}^N b_k \tilde{\rho}_{1/k}\|_{L^2(d\mu_\sigma)}^2$ is enclosed to order $O((M+1)^{-2\sigma-1})$ by*

$$
\left|d_N(\sigma; b)^2 - \left(\sum_{m=1}^M w_m^{(\sigma)} f_m + \bar{f}(b)\,(M+1)^{-2\sigma}\right)\right| \le B(b)\, w_{M+1}^{(\sigma)} = B(b)\big((M+1)^{-2\sigma} - (M+2)^{-2\sigma}\big).
$$

3. **Explicit Tail Enclosure for the Shifted Step-Space Residual $\kappa(\sigma)$:** *The shifted step-space residual $\kappa(\sigma) = \int_0^1 (\{1/x\} - P_{S_\sigma}\{1/x\})^2 x^{2\sigma-1}\,dx = \sum_{m=1}^\infty \kappa_m(\sigma)$ satisfies $0 < \kappa_m(\sigma) < \frac{1}{12} m^{-2\sigma-1}$ for every $m \ge 1$, and for every cutoff $M \ge 1$,*

$$
0 < \kappa(\sigma) - \sum_{m=1}^M \kappa_m(\sigma) \le \frac{M^{-2\sigma}}{24\sigma}.
$$

**Proof.**
**(1)** Writing $h_m = \{m/j\}\{m/k\}$ ($h_0 = 0$) and $w_m^{(\sigma)} = m^{-2\sigma} - (m+1)^{-2\sigma}$, summation by parts gives $\sum_{m=1}^\infty (m^{-2\sigma} - (m+1)^{-2\sigma}) h_m = \sum_{m=1}^\infty (h_m - h_{m-1}) m^{-2\sigma}$. Since $h_m - h_{m-1}$ is $L$-periodic with $m = q L + r$ ($q \ge 0, 1 \le r \le L$), summing $\sum_{q=0}^\infty (q L + r)^{-2\sigma} = L^{-2\sigma}\zeta(2\sigma, r/L)$ yields the identity.

**(2)** By Dedekind's elementary reciprocity identity for sawtooth sums, $\frac{1}{L}\sum_{r=1}^L \{r/j\}\{r/k\} = \frac{(j-1)(k-1)}{4jk} + \frac{\gcd(j,k)^2 - 1}{12jk} =: \bar{h}_{j,k}$, and $\frac{1}{k}\sum_{r=1}^k \{r/k\} = \frac{k-1}{2k}$, giving $\bar{f}(b)$. Splitting $\sum_{m=M+1}^\infty w_m^{(\sigma)} f_m = \bar{f}(b)\sum_{m=M+1}^\infty w_m^{(\sigma)} + \sum_{m=M+1}^\infty w_m^{(\sigma)}(f_m - \bar{f}(b))$, the first sum telescopes to $\bar{f}(b)(M+1)^{-2\sigma}$. Setting $A_m := \sum_{n=M+1}^m (f_n - \bar{f}(b))$ ($A_M = 0$), we have $|A_m| \le B(b)$ for all $m > M$, and since $w_m^{(\sigma)} = m^{-2\sigma} - (m+1)^{-2\sigma}$ is strictly decreasing and convex ($w_m^{(\sigma)} - w_{m+1}^{(\sigma)} > 0$), Abel summation gives

$$
\left|\sum_{m=M+1}^\infty w_m^{(\sigma)}\big(f_m - \bar{f}(b)\big)\right| = \left|\sum_{m=M+1}^\infty A_m\big(w_m^{(\sigma)} - w_{m+1}^{(\sigma)}\big)\right| \le B(b) \sum_{m=M+1}^\infty \big(w_m^{(\sigma)} - w_{m+1}^{(\sigma)}\big) = B(b)\,w_{M+1}^{(\sigma)}.
$$

**(3)** On $I_m = (1/(m+1), 1/m]$, substituting $u = \{1/x\} = 1/x - m \in [0, 1)$ gives $x^{2\sigma-1}\,dx = (m+u)^{-2\sigma-1}\,du$. Since the orthogonal projection $P_{S_\sigma}\{1/x\}|_{I_m}$ minimizes $\int_0^1 (u - c)^2 (m+u)^{-2\sigma-1}\,du$ over $c \in \mathbb{R}$, choosing $c = 1/2$ gives

$$
0 < \kappa_m(\sigma) \le \int_0^1 \left(u - \frac{1}{2}\right)^2 (m+u)^{-2\sigma-1}\,du < m^{-2\sigma-1}\int_0^1 \left(u - \frac{1}{2}\right)^2 du = \frac{1}{12}\, m^{-2\sigma-1}.
$$

Summing over $m > M$ and bounding $\sum_{m=M+1}^\infty m^{-2\sigma-1} < \int_M^\infty t^{-2\sigma-1}\,dt = \frac{M^{-2\sigma}}{2\sigma}$ yields $\sum_{m=M+1}^\infty \kappa_m(\sigma) \le \frac{M^{-2\sigma}}{24\sigma}$. $\square$

---

### 2.4 Theorem 4: Hybrid Step-Space Conjugate-Kernel Monotonicity and Interval Certification

Extending the continuous Blaschke-product projection formula of Burnol [17, Lemma 2.4], the weighted reproducing-kernel mechanism of Delaunay–Fricain–Mosaki–Robert [13, Theorem 2.2 and Corollary 2.3], and the step-space conjugate-pair Gram-inverse bounds of [9, Theorem C, Corollary D, and §6], we introduce a finite-cutoff **hybrid step-head + continuous-tail reproducing kernel** $k_{\rho, M}^{(\sigma)}$ whose Gram matrix entries are finite $M$-term sums plus exact closed-form power tails, allowing direct 60-digit interval certification at any finite cutoff $M \ge 1$.

**Theorem 4 (Hybrid Step-Space Conjugate-Kernel Projection and Strict Loewner Monotonicity).**
*In any complex Hilbert space $\mathcal{H}$ with inner product $\langle f, g \rangle_{\mathcal{H}}$ linear in $f$ and conjugate-linear in $g$, the orthogonal projection $P_W \chi = \sum_{i=1}^d \lambda_i k_i$ onto $W = \operatorname{span}\{k_1, \dots, k_d\}$ satisfies $K^T \lambda = b$ where $K_{i,j} = \langle k_i, k_j \rangle_{\mathcal{H}}$ and $b_j = \langle \chi, k_j \rangle_{\mathcal{H}}$, with squared norm $\|P_W \chi\|_{\mathcal{H}}^2 = b^* (K^T)^{-1} b = \overline{b^T} K^{-1} b$. Suppose $\rho = \beta + i\gamma$ ($\gamma \ne 0$) is a zero of $\zeta(s)$ with $\beta \in (\sigma, 1)$. For any integer $M \ge 0$, define the hybrid step-head + continuous-tail reproducing kernel $k_{\rho, M}^{(\sigma)} := P_{S_\sigma^{(\le M)}} k_\rho + k_\rho \mathbf{1}_{(0, 1/(M+1)]} \in L^2((0, 1], d\mu_\sigma)$, where $k_\rho(x) = x^{\rho - 2\sigma}$. Then:*

1. **Exact Orthogonality and Target Vector:** *For every $M \ge 0$ and every $k \ge 2$, $\langle \tilde{\rho}_{1/k}, k_{\rho, M}^{(\sigma)} \rangle_{L^2(d\mu_\sigma)} = 0$ and $b_\rho := \big(\langle E, k_{\rho, M}^{(\sigma)} \rangle_{L^2(d\mu_\sigma)}, \langle E, k_{\bar{\rho}, M}^{(\sigma)} \rangle_{L^2(d\mu_\sigma)}\big)^T = \big(\frac{2\sigma}{\bar{\rho}}, \frac{2\sigma}{\rho}\big)^T$.*
2. **Closed-Form $M = 0$ ($H^2$) Baseline [17, Lemma 2.4; 9, §6]:** *At $M = 0$, the $2 \times 2$ Gram matrix on $\operatorname{span}\{k_\rho, k_{\bar{\rho}}\}$ in $L^2(d\mu_\sigma)$ is $K_{\rho, 0}^{(\sigma)} = \begin{pmatrix} \frac{\sigma}{\beta-\sigma} & \frac{\sigma}{\rho-\sigma} \\ \frac{\sigma}{\bar{\rho}-\sigma} & \frac{\sigma}{\beta-\sigma} \end{pmatrix}$, and the projection norm squared is*

$$
B_{\mathrm{2pt}, 0}^{(H^2)}(\sigma; \beta, \gamma) := b_\rho^* \big((K_{\rho, 0}^{(\sigma)})^T\big)^{-1} b_\rho = 1 - \left(1 - \frac{4\sigma(\beta - \sigma)}{\beta^2 + \gamma^2}\right)^2 = \frac{8\sigma(\beta - \sigma)\big[\beta^2 + \gamma^2 - 2\sigma(\beta - \sigma)\big]}{(\beta^2 + \gamma^2)^2}.
$$

3. **Strict Hybrid Step-Space Monotonicity ($M \ge 1$):** *For every $M \ge 0$, the $2 \times 2$ Hermitian Gram matrix $K_{\rho, M}^{(\sigma)}$ has entries $K_{1,1}^{(M)} = \langle k_{\rho, M}^{(\sigma)}, k_{\rho, M}^{(\sigma)} \rangle_{L^2(d\mu_\sigma)} = K_{2,2}^{(M)} > 0$ and $K_{1,2}^{(M)} = \langle k_{\rho, M}^{(\sigma)}, k_{\bar{\rho}, M}^{(\sigma)} \rangle_{L^2(d\mu_\sigma)} = \overline{K_{2,1}^{(M)}}$ given by the finite $M$-term sum plus closed-form tail*

$$
K_{1,1}^{(M)} = \frac{4\sigma^2}{|\rho|^2}\sum_{m=1}^M \frac{|m^{-\rho} - (m+1)^{-\rho}|^2}{m^{-2\sigma} - (m+1)^{-2\sigma}} + \frac{\sigma}{\beta - \sigma}(M+1)^{-2(\beta-\sigma)}, \qquad K_{1,2}^{(M)} = \frac{4\sigma^2}{\rho^2}\sum_{m=1}^M \frac{(m^{-\rho} - (m+1)^{-\rho})^2}{m^{-2\sigma} - (m+1)^{-2\sigma}} + \frac{\sigma}{\rho - \sigma}(M+1)^{-2(\rho-\sigma)},
$$

*satisfying $0 \prec K_\rho^{(S_\sigma)} \prec K_{\rho, M+1}^{(\sigma)} \prec K_{\rho, M}^{(\sigma)} \prec K_{\rho, 0}^{(\sigma)}$ in the strict Loewner order, and yielding the strictly increasing sequence of lower bounds converging as $M \to \infty$ to the full step-space conjugate-pair bound of [9, Corollary D]:*

$$
d_N(\sigma)^2 \ge B_{\mathrm{2pt}, M}^{(S_\sigma)}(\sigma; \beta, \gamma) := b_\rho^* \big((K_{\rho, M}^{(\sigma)})^T\big)^{-1} b_\rho = \frac{8\sigma^2}{|\rho|^2} \cdot \frac{K_{1,1}^{(M)} - \operatorname{Re}\!\left(\frac{\rho}{\bar{\rho}}\,K_{1,2}^{(M)}\right)}{\big(K_{1,1}^{(M)}\big)^2 - \big|K_{1,2}^{(M)}\big|^2}.
$$

**Proof.**
Since $\tilde{\rho}_{1/k}$ is constant on each $I_m$ ($1 \le m \le M$), replacing $k_\rho$ on $I_1 \cup \dots \cup I_M$ by its $L^2(d\mu_\sigma)$-step projection $P_{S_\sigma^{(\le M)}} k_\rho$ preserves all inner products with $\tilde{\rho}_{1/k}$ and $E$, so $\langle \tilde{\rho}_{1/k}, k_{\rho, M}^{(\sigma)} \rangle_{L^2(d\mu_\sigma)} = \langle \tilde{\rho}_{1/k}, k_\rho \rangle_{L^2(d\mu_\sigma)} = \frac{2\sigma}{\bar{\rho}}\frac{\zeta(\bar{\rho})}{\bar{\rho}}(k^{-1} - k^{-\bar{\rho}}) = 0$ and $\langle E, k_{\rho, M}^{(\sigma)} \rangle_{L^2(d\mu_\sigma)} = \frac{2\sigma}{\bar{\rho}}$. Expanding $b_\rho^* ((K_{\rho, M}^{(\sigma)})^T)^{-1} b_\rho$ for $(K^T)^{-1} = \frac{1}{(K_{1,1}^{(M)})^2 - |K_{1,2}^{(M)}|^2}\begin{pmatrix} K_{1,1}^{(M)} & -K_{2,1}^{(M)} \\ -K_{1,2}^{(M)} & K_{1,1}^{(M)} \end{pmatrix}$ with $K_{2,1}^{(M)} = \overline{K_{1,2}^{(M)}}$ and $b_\rho = \big(\frac{2\sigma}{\bar{\rho}}, \frac{2\sigma}{\rho}\big)^T$ gives

$$
\frac{4\sigma^2}{(K_{1,1}^{(M)})^2 - |K_{1,2}^{(M)}|^2}\left[\frac{2 K_{1,1}^{(M)}}{|\rho|^2} - \frac{K_{1,2}^{(M)}}{\bar{\rho}^2} - \frac{\overline{K_{1,2}^{(M)}}}{\rho^2}\right] = \frac{8\sigma^2}{|\rho|^2} \cdot \frac{K_{1,1}^{(M)} - \operatorname{Re}\!\left(\frac{\rho}{\bar{\rho}}\,K_{1,2}^{(M)}\right)}{\big(K_{1,1}^{(M)}\big)^2 - \big|K_{1,2}^{(M)}\big|^2}.
$$

At $M = 0$, substituting $K_{1,1}^{(0)} = \frac{\sigma}{\delta}$ ($\delta = \beta - \sigma$) and $K_{1,2}^{(0)} = \frac{\sigma}{\delta + i\gamma}$ gives $\frac{8\sigma\delta[R - 2\sigma\delta]}{R^2} = 1 - (1 - \frac{4\sigma\delta}{R})^2$ ($R = \beta^2 + \gamma^2$). Finally, because $k_\rho$ and $k_{\bar{\rho}}$ are linearly independent on $I_{M+1}$ for $\gamma \ne 0$, replacing them on $I_{M+1}$ by their $L^2(d\mu_\sigma)$-step averages strictly decreases their $2 \times 2$ Gram matrix in the Loewner order: $K_{\rho, M+1}^{(\sigma)} \prec K_{\rho, M}^{(\sigma)}$, which implies $((K_{\rho, M+1}^{(\sigma)})^T)^{-1} \succ ((K_{\rho, M}^{(\sigma)})^T)^{-1}$ and hence strict monotonicity of $B_{\mathrm{2pt}, M}^{(S_\sigma)}(\sigma; \beta, \gamma)$ in $M$. $\square$

---

## 3. Numerical Verification and 60-Digit Interval Certification

To maintain a strict separation between asymptotic floating-point experiments and validated interval enclosures, all computations in `src/verify_step_space_annihilator_duality.py` (`mp.mp.dps = 60`, `mp.iv.dps = 60`) are organized into two distinct categories:
1. **Validated 60-Digit Interval Enclosures (`mpmath.iv`):** Used for all certified claims in Theorems 3 and 4 (Hurwitz-zeta Gram entries via pure interval Euler-Maclaurin summation `iv_hurwitz_zeta` with exact rational Bernoulli numbers and alternating-series remainder bounds; exact integer cumulative-sum fluctuation bounds $B(b)$ and certified upper bounds $d_{40}^{\mathrm{cert}}(\sigma)^2$ and $d_{160}^{\mathrm{cert}}(\sigma)^2$; and 60-digit complex interval evaluations of $B_{\mathrm{2pt}, 0}^{(H^2)}$, $B_{\mathrm{2pt}, 500}^{(S_\sigma)}$, and $B_{\mathrm{2pt}, 5000}^{(S_\sigma)}$).
2. **IEEE-754 Double-Precision Asymptotic Progressions:** Used for the large-$N$ convergence experiments of Theorems 1 and 2 (head-norm progression up to $N = 10240$, fixed-$k$ taper residual decay across $M \in [100, 800]$, and Theorem 2(3) witness scaling up to $N = 320, M = 6430$).

### 3.1 Power-Saving Head Norm Convergence and Flat-Top Hermite Spline Zero Annihilators

Table 1A reports the convergence of the scaled head functional dual norm $\|\mathcal{F}_N\|_{S_\sigma^*}^2 / N^{2\sigma-1}$ to the 60-digit interval-certified limit $\frac{\zeta(2\sigma+1)}{2\sigma\,\zeta(4\sigma+2)}$ of Theorem 1(2) across $N \in [40, 10240]$, together with the Theorem 2(3) constructive dual witness progression of the flat-top Hermite spline annihilator $\widetilde{\mathcal{L}}_{\rho_1, N}^{(M; W_2)}$ ($r = 2, \theta = 1/2$, $M = \lfloor 2 N^{1 + 1/2.5} \rfloor = \lfloor 2 N^{1.4} \rfloor$) at the first critical-line zero $\rho_1 = 1/2 + i\cdot 14.13472514\dots$ (Figure 1(a)):

| Abscissa $\sigma$ | $N=160$ $\frac{\|\mathcal{F}_N\|_{S_\sigma^*}^2}{N^{2\sigma-1}}$ | $N=2560$ $\frac{\|\mathcal{F}_N\|_{S_\sigma^*}^2}{N^{2\sigma-1}}$ | $N=10240$ $\frac{\|\mathcal{F}_N\|_{S_\sigma^*}^2}{N^{2\sigma-1}}$ | Theory $\frac{\zeta(2\sigma+1)}{2\sigma\zeta(4\sigma+2)}$ | $N=160$ ($M=2436$) $W_2$ $\|\widetilde{\mathcal{L}}(E)\|$ | $N=160$ $W_2$ $\max_{k\le N}|\gamma_k|$ | $N=160$ $W_2$ $\frac{\|\mathcal{H}_N\|}{\|\mathcal{L}_{\rho_1}\|}$ | $N=320$ ($M=6430$) $W_2$ $\text{lb}\cdot N^{2.8(\sigma-1/2)}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $\sigma = 0.55$ | $1.332845$ | $1.325207$ | **$1.326567$** | **$1.325895$** | $0.07778$ | $3.711 \times 10^{-6}$ | $0.0006$ | $1.0964 \times 10^{-3}$ |
| $\sigma = 0.65$ | $1.054646$ | $1.048914$ | **$1.049126$** | **$1.048874$** | $0.09192$ | $4.385 \times 10^{-6}$ | $0.0005$ | $2.0533 \times 10^{-3}$ |
| $\sigma = 0.75$ | $0.867623$ | $0.862691$ | **$0.862600$** | **$0.862476$** | $0.10606$ | $5.060 \times 10^{-6}$ | $0.0005$ | $3.3140 \times 10^{-3}$ |
| $\sigma = 0.85$ | $0.734631$ | $0.729995$ | **$0.729817$** | **$0.729729$** | $0.12020$ | $5.734 \times 10^{-6}$ | $0.0004$ | $4.7870 \times 10^{-3}$ |

Table 1B directly verifies Theorem 2(1)–(2) at fixed index $k = 2$ ($\sigma = 0.75, \rho_1 = 1/2 + i\cdot 14.13472514\dots$) across $M \in \{100, 200, 400, 800\}$ (Figure 1(b)): both the polynomial Cesàro taper $(1 - u)^1$ and polynomial Riesz taper $(1 - u)^2$ are trapped at empirical decay exponent $\approx 1.00$ by the non-vanishing $m=1$ lower-end term $\zeta(\rho_1 - 1)$, whereas the flat-top Hermite splines $W_r(u)$ ($r \in \{1, 2, 3\}$) eliminate all $\zeta(\rho_1 - m)$ lower-end terms and achieve the exact Euler-Maclaurin decay exponents $\beta_0 + r \in \{1.5, 2.5, 3.5\}$:

| Taper Scheme | $M = 100$ $\|\gamma_2^{(M)}(\rho_1)\|$ | $M = 200$ $\|\gamma_2^{(M)}(\rho_1)\|$ | $M = 400$ $\|\gamma_2^{(M)}(\rho_1)\|$ | $M = 800$ $\|\gamma_2^{(M)}(\rho_1)\|$ | Empirical Decay Exponent ($400 \to 800$) | Theoretical Exponent (Theorem 2) |
|---|---:|---:|---:|---:|---:|---:|
| Polynomial Cesàro $(1 - u)^1$ | $2.440 \times 10^{-3}$ | $1.217 \times 10^{-3}$ | $6.138 \times 10^{-4}$ | $3.059 \times 10^{-4}$ | **$1.005$** | **$1.0$** ($\zeta(\rho_1-1)$ obstruction) |
| Polynomial Riesz $(1 - u)^2$ | $4.724 \times 10^{-3}$ | $2.408 \times 10^{-3}$ | $1.216 \times 10^{-3}$ | $6.107 \times 10^{-4}$ | **$0.993$** | **$1.0$** ($\zeta(\rho_1-1)$ obstruction) |
| Flat-Top Hermite Spline $W_1(u)$ | $2.841 \times 10^{-5}$ | $9.662 \times 10^{-6}$ | $3.361 \times 10^{-6}$ | $1.180 \times 10^{-6}$ | **$1.511$** | **$1.5 = \beta_0 + 1$** |
| Flat-Top Hermite Spline $W_2(u)$ | $1.124 \times 10^{-6}$ | $1.960 \times 10^{-7}$ | $3.478 \times 10^{-8}$ | $6.176 \times 10^{-9}$ | **$2.494$** | **$2.5 = \beta_0 + 2$** |
| Flat-Top Hermite Spline $W_3(u)$ | $6.327 \times 10^{-8}$ | $5.021 \times 10^{-9}$ | $4.260 \times 10^{-10}$ | $3.706 \times 10^{-11}$ | **$3.523$** | **$3.5 = \beta_0 + 3$** |

![Figure 1: (a) Power-saving convergence of the scaled head functional dual norm ||F_N||_{S_sigma^*}^2 / N^{2*sigma-1} to zeta(2*sigma+1)/(2*sigma*zeta(4*sigma+2)) across N in [40, 10240]; (b) Fixed-index (k=2) residual decay |gamma_2^{(M)}(rho_1)| across M in [100, 800], showing the M^{-1} lower-end zeta obstruction of polynomial Cesaro/Riesz tapers versus the M^{-beta_0 - r} decay of flat-top Hermite splines W_r.](supplement/p10-figure-1.png)

### 3.2 Pure-Interval Hurwitz-Zeta Gram Validation and 60-Digit Interval Enclosures for $\kappa(\sigma)$, $d_{40}(\sigma)^2$, and $d_{160}(\sigma)^2$

In `src/verify_step_space_annihilator_duality.py`, we verified Theorem 3(1) across all $28$ upper-triangular pairs $2 \le j \le k \le 8$ at $\sigma = 0.75$ using `iv_hurwitz_zeta` (pure 60-digit `mpmath.iv` Euler-Maclaurin summation of order $2K = 28$ with cutoff $L = 150$, exact rational Bernoulli numbers, and the exact alternating-series remainder bracket for completely monotonic functions $(x+a)^{-2\sigma}$). In particular, at $(j, k) = (2, 2)$, the pure interval enclosure is

$$
\big(A_N(0.75)\big)_{2,2} = \frac{1 - 2^{-1/2}}{4}\,\zeta\!\left(\frac{3}{2}\right) \in \big[0.191286756156351986341817189650869544878116992336457044537476,\; 0.191286756156351986341817189650869544878116992336457044537498\big]
$$

(interval width $2.14 \times 10^{-59}$), agrees with the rank-4 Hurwitz-Vasyunin Gram decomposition to $1.39 \times 10^{-16}$, and all $28$ interval enclosures lie strictly inside their independent pure-interval Summation-by-Parts brackets at $M = 5000$ (maximum bracket width $6.67 \times 10^{-10}$).

Table 2 reports the 60-digit interval enclosures for $\kappa(\sigma)$ (Theorem 3(3), $M = 500$) and the 60-digit interval-certified upper bounds on $d_{40}(\sigma)^2$ ($M = 5000$) and $d_{160}(\sigma)^2$ ($M = 10000$) obtained by evaluating Theorem 3(2) in pure 60-digit `mpmath.iv` arithmetic on the explicit rational trial vectors $b \in 10^{-6}\mathbb{Z}^{N-1}$ archived in `results/step_space_annihilator_duality.json`. Every pairwise fluctuation constant $B_{j,k}$ is computed from exact 64-bit integer cumulative sums over $1 \le r \le \operatorname{lcm}(j,k)$ (verifying zero period sum for all $12{,}720$ pairs) and enclosed directly in `mpmath.iv` without floating-point conversion or ad-hoc padding:

| $(N, M)$ | Abscissa $\sigma$ | Certified $\kappa(\sigma)$ Bracket $[ \kappa_{\min}, \kappa_{\max} ]$ | Periodic Mean $\bar{f}(b)$ | Exact Fluctuation Constant $B(b)$ | Naive Pointwise Tail | SBP Periodic-Mean Tail | Tail Reduction Factor | Floating $d_N(\sigma)^2$ | **60-Digit Certified Upper Bound** $d_N^{\mathrm{cert}}(\sigma)^2 \le$ |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| $(40, 5000)$ | $\sigma = 0.52$ | $[0.07690161, 0.07702659]$ | $0.26080440$ | $592.6102$ | $7.52557 \times 10^{-3}$ | $5.46239 \times 10^{-5}$ | **$137.8\times$** | $0.01144680$ | **$0.01146437$** |
| $(40, 5000)$ | $\sigma = 0.55$ | $[0.07243208, 0.07251347]$ | $0.28373166$ | $667.0777$ | $4.95079 \times 10^{-3}$ | $3.67168 \times 10^{-5}$ | **$134.8\times$** | $0.00972042$ | **$0.00973298$** |
| $(40, 5000)$ | $\sigma = 0.65$ | $[0.06037357, 0.06039344]$ | $0.37189190$ | $943.2993$ | $1.18174 \times 10^{-3}$ | $9.58091 \times 10^{-6}$ | **$123.3\times$** | $0.00548419$ | **$0.00548802$** |
| $(40, 5000)$ | $\sigma = 0.75$ | $[0.05139455, 0.05139952]$ | $0.47396352$ | $1245.5272$ | $2.67602 \times 10^{-4}$ | $2.39589 \times 10^{-6}$ | **$111.7\times$** | $0.00298171$ | **$0.00298277$** |
| $(40, 5000)$ | $\sigma = 0.85$ | $[0.04443644, 0.04443770]$ | $0.58264481$ | $1547.7449$ | $5.78042 \times 10^{-5}$ | $5.70681 \times 10^{-7}$ | **$101.3\times$** | $0.00157269$ | **$0.00157296$** |
| $(160, 10000)$ | $\sigma = 0.55$ | $[0.07243208, 0.07251347]$ | $0.69663835$ | $29494.9447$ | $2.13017 \times 10^{-2}$ | $1.56847 \times 10^{-4}$ | **$135.8\times$** | $0.00667906$ | **$0.00680891$** |
| $(160, 10000)$ | $\sigma = 0.65$ | $[0.06037357, 0.06039344]$ | $1.09412889$ | $49620.9132$ | $5.23769 \times 10^{-3}$ | $4.75911 \times 10^{-5}$ | **$110.1\times$** | $0.00322386$ | **$0.00326480$** |
| $(160, 10000)$ | $\sigma = 0.75$ | $[0.05139455, 0.05139952]$ | $1.54686486$ | $72118.5815$ | $1.13974 \times 10^{-3}$ | $1.23613 \times 10^{-5}$ | **$92.2\times$** | $0.00146257$ | **$0.00147346$** |

### 3.3 60-Digit Interval-Certified Conjugate-Kernel Projections $B_{\mathrm{2pt}, M}^{(S_\sigma)}$ vs. $B_{\mathrm{2pt}, 0}^{(H^2)}$

Table 3 compares the 60-digit interval-certified continuous $H^2$ conjugate-pair baseline $B_{\mathrm{2pt}, 0}^{(H^2)}(\sigma; \beta, \gamma) = \frac{8\sigma(\beta-\sigma)[\beta^2+\gamma^2 - 2\sigma(\beta-\sigma)]}{(\beta^2+\gamma^2)^2}$ against the 60-digit complex-interval-certified hybrid step-space bounds $B_{\mathrm{2pt}, 500}^{(S_\sigma)}(\sigma; \beta, \gamma)$ ($M = 500$) and $B_{\mathrm{2pt}, 5000}^{(S_\sigma)}(\sigma; \beta, \gamma)$ ($M = 5000$) (Figure 2). Comparing these certified interval lower bounds directly against the 60-digit interval-certified upper bounds $d_{40}^{\mathrm{cert}}(\sigma)^2$ and $d_{160}^{\mathrm{cert}}(\sigma)^2$ from Table 2 certifies every exclusion in Table 3 in pure 60-digit interval arithmetic:

| Probe $(\sigma, \beta, \gamma)$ | Certified $H^2$ Bound $B_{\mathrm{2pt}, 0}^{(H^2)}$ | **Certified Step Bound** $B_{\mathrm{2pt}, 500}^{(S_\sigma)}$ | **Certified Step Bound** $B_{\mathrm{2pt}, 5000}^{(S_\sigma)}$ | Certified Gain $B_{\mathrm{2pt}, 5000}^{(S_\sigma)} / B_{\mathrm{2pt}, 0}^{(H^2)}$ | Certified $d_{40}^{\mathrm{cert}}(\sigma)^2 \le$ | Certified $d_{160}^{\mathrm{cert}}(\sigma)^2 \le$ | Interval-Certified Exclusion Status |
|---|---:|---:|---:|---:|---:|---:|---|
| $(0.55, 0.75, 14.13472514)$ | $0.00438743$ | **$0.00787546$** | **$0.00787547$** | **$1.7950\times$** | $0.00973298$ | **$0.00680891$** | **Certified at $N=160$ ($0.00787546 > 0.00680891$; $H^2$ $0.004387$ fails)** |
| $(0.55, 0.85, 14.13472514)$ | $0.00657228$ | **$0.01538571$** | **$0.01538573$** | **$2.3410\times$** | **$0.00973298$** | **$0.00680891$** | **Certified at $N=40$ ($0.01538571 > 0.00973298$; $H^2$ $0.006572$ fails)** |
| $(0.55, 0.85, 50.00)$ | $0.00052778$ | **$0.00276870$** | **$0.00276877$** | **$5.2461\times$** | $0.00973298$ | $0.00680891$ | Method demonstration ($5.25\times$ certified gain) |
| $(0.55, 0.95, 200.00)$ | $0.00004400$ | **$0.00132366$** | **$0.00132471$** | **$30.1080\times$** | $0.00973298$ | $0.00680891$ | Method demonstration ($30.11\times$ certified gain) |
| $(0.65, 0.75, 14.13472514)$ | $0.00259374$ | **$0.00350650$** | **$0.00350651$** | **$1.3519\times$** | $0.00548802$ | **$0.00326480$** | **Certified at $N=160$ ($0.00350650 > 0.00326480$; $H^2$ $0.002594$ fails)** |
| $(0.65, 0.85, 14.13472514)$ | $0.00517997$ | **$0.00929212$** | **$0.00929213$** | **$1.7939\times$** | **$0.00548802$** | **$0.00326480$** | **Certified at $N=40$ ($0.00929212 > 0.00548802$; $H^2$ $0.005180$ fails)** |
| $(0.65, 0.85, 50.00)$ | $0.00041584$ | **$0.00127744$** | **$0.00127748$** | **$3.0721\times$** | $0.00548802$ | $0.00326480$ | Method demonstration ($3.07\times$ certified gain) |
| $(0.75, 0.85, 14.13472514)$ | $0.00299009$ | **$0.00404142$** | **$0.00404143$** | **$1.3516\times$** | **$0.00298277$** | **$0.00147346$** | **Certified at $N=40$ ($0.00404142 > 0.00298277$) and $N=160$** |
| $(0.75, 0.95, 200.00)$ | $0.00003000$ | **$0.00016965$** | **$0.00016983$** | **$5.6611\times$** | $0.00298277$ | $0.00147346$ | Method demonstration ($5.66\times$ certified gain) |

![Figure 2: (a) Strict monotonicity of the hybrid step-space conjugate-pair bound b_rho^* ((K_{rho, M}^{(sigma)})^T)^{-1} b_rho across M in [0, 20000]; (b) Certified step-space projection gain B_{2pt, 5000}^{(S_sigma)} / B_{2pt, 0}^{(H^2)} over the continuous H^2 bound across (sigma, beta, gamma).](supplement/p10-figure-2.png)

In particular:
- At $N = 40$, for both $(\sigma, \beta, \gamma) = (0.55, 0.85, 14.13472514)$ and $(0.65, 0.85, 14.13472514)$, the continuous $H^2$ bound ($0.00657228$ and $0.00517997$) lies strictly below $d_{40}^{\mathrm{cert}}(\sigma)^2$ ($0.00973298$ and $0.00548802$) and fails to exclude $(\beta, \gamma)$, whereas the 60-digit interval-certified hybrid step-space bound $B_{\mathrm{2pt}, 500}^{(S_\sigma)}$ ($0.01538571$ and $0.00929212$) exceeds $d_{40}^{\mathrm{cert}}(\sigma)^2$ and certifies exclusion at $N = 40$.
- At $N = 160$, for both $(\sigma, \beta, \gamma) = (0.55, 0.75, 14.13472514)$ and $(0.65, 0.75, 14.13472514)$, the continuous $H^2$ bound ($0.00438743$ and $0.00259374$) lies strictly below $d_{160}^{\mathrm{cert}}(\sigma)^2$ ($0.00680891$ and $0.00326480$) and still fails at $N = 160$, whereas $B_{\mathrm{2pt}, 500}^{(S_\sigma)}$ ($0.00787546$ and $0.00350650$) exceeds $d_{160}^{\mathrm{cert}}(\sigma)^2$ and certifies exclusion in 60-digit interval arithmetic.

---

## 4. Limitations and Scope

1. **Methodological Comparison vs. Known Numerical Verification of RH:** Platt and Trudgian [16] have rigorously verified the Riemann Hypothesis up to height $T = 3 \times 10^{12}$ by direct Turing-method zero-counting and ZetaGrid/Odlyzko-Schönhage evaluations. The finite-$N$ exclusion examples at heights $\gamma \in \{14.1347, 50, 200\}$ in Table 3 are therefore methodological demonstrations quantifying how much the hybrid step-space kernel $K_{\rho, M}^{(\sigma)}$ sharpens finite-$N$ Nyman-Beurling reproducing-kernel bounds relative to the continuous $H^2$ baseline, rather than new zero-free regions beyond known numerical height bounds.
2. **Role of a Zero Input and Support Scaling in Theorem 2:** While Theorem 1(1) provides an unconditional, zero-free lower bound $d_N(\sigma)^2 \ge c(\sigma)N^{-2\sigma}$ from the squarefree tail $\mathcal{L}_{\mathrm{sqf}}$ and Theorem 1(2) proves that the head functional $\mathcal{F}_N$ has dual norm squared $\asymp N^{2\sigma-1}$, achieving the slower decay rate $d_N(\sigma)^2 \gg_{\sigma,\rho_0,r} N^{-2(\sigma - \beta_0)\left(1 + \frac{1}{\beta_0 + r}\right)}$ in Theorem 2(3) uses an existing nontrivial zero $\rho_0 = \beta_0 + i\gamma_0$ of $\zeta(s)$ and support cutoff $M = \lfloor \Lambda N^{1 + 1/(\beta_0 + r)} \rfloor$, providing an explicit dual realization of the existential rate exponent $(\sigma - \Theta)^+$ established in [11, Theorem K].
3. **Growth of Fluctuation Constants $B(b)$ with $N$:** In Theorem 3(2), the periodic fluctuation constant $B(b)$ grows quadratically with $\sum_{k=2}^N k|b_k|$ ($B(b) \approx 667.08$ at $N = 40, \sigma = 0.55$ and $B(b) \approx 29494.94$ at $N = 160, \sigma = 0.55$). While $M = 5000$ ($N=40$) and $M = 10000$ ($N=160$) suffice to compress the fluctuation remainder $B(b)w_{M+1}^{(\sigma)}$ to $O(10^{-4})$ and certify the exclusions in Table 3, certifying much larger truncation dimensions $N$ via interval arithmetic requires scaling $M$ polynomially with $N$.

---

## 5. Reproducibility

All analytical proofs are complete in Section 2, and all numerical tables, explicit rational trial vectors, 60-digit `mpmath.iv` interval enclosures, and figures can be reproduced in $\sim 45\text{ s}$ on a single CPU thread (`Python 3.12.3`, `numpy 2.5.4`, `scipy 1.18.1`, `mpmath 1.4.1`, `matplotlib 3.11.2`) by running:

```bash
PYTHONPATH=. python3 src/verify_step_space_annihilator_duality.py
```

All outputs are saved to `results/step_space_annihilator_duality.json`, `supplement/p10-figure-1.png`, and `supplement/p10-figure-2.png`.

---

## 6. References

[1] B. Nyman. *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*. PhD Thesis, University of Uppsala, 1950. https://books.google.com/books?id=7Q00AAAAIAAJ

[2] A. Beurling. A closure problem related to the Riemann zeta-function. *Proceedings of the National Academy of Sciences*, 41(5):312–314, 1955. https://doi.org/10.1073/pnas.41.5.312

[3] L. Báez-Duarte. A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis. *Rendiconti Lincei Matematica e Applicazioni*, 14(1):5–11, 2003. https://ems.press/journals/rlm/articles/3487

[4] V. I. Vasyunin. On a biorthogonal system associated with the Riemann hypothesis. *St. Petersburg Mathematical Journal*, 7(3):405–419, 1995. https://www.mathnet.ru/eng/aa521

[5] B. Bagchi. On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis. *Proceedings of the Indian Academy of Sciences (Mathematical Sciences)*, 116(2):139–146, 2006. https://doi.org/10.1007/BF02829741

[6] M. Balazard and B. Martin. Sur l'autocorrélation multiplicative de la fonction « partie fractionnaire ». *Journal of Number Theory*, 142:198–232, 2014. https://doi.org/10.1016/j.jnt.2014.02.019

[7] S. Bettin and J. B. Conrey. A reciprocity formula for a cotangent sum. *International Mathematics Research Notices*, 2013(24):5709–5726, 2013. https://doi.org/10.1093/imrn/rns211

[8] J.-F. Burnol. On Fourier and Zeta(s) (IV): A weighty study of Báez-Duarte's criterion. *Advances in Mathematics*, 214(1):392–422, 2007. https://doi.org/10.1016/j.aim.2007.02.009

[9] span_of_dilates. The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH. *rStation Paper riemann_hypothesis_2*, v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/2/v1

[10] halasz_resonator. Canonical Archimedean-Reciprocity Decomposition of the Vasyunin-Báez-Duarte Gram Operator: Universal Inertia, 4x4 Dedekind Capacitance Monotonicity, and Arithmetic-Legendre Mollifier Compression. *rStation Paper riemann_hypothesis_3*, v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/3/v1

[11] span_of_dilates. The exact rate exponent in the shifted Nyman–Beurling criterion: $d_N(a)=N^{-(a-\Theta)^+ + o(1)}$. *rStation Paper riemann_hypothesis_6*, v2, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/6/v2

[12] halasz_resonator. Dirichlet-Inverse Extensions of the Vasyunin-Balazard Biorthogonal System: Head-Tail Matrix-Loewner Inverse Gram Bounds, Algebraic Reciprocal Obstructions, and Certified Squarefree Separation for the Davenport-Heilbronn Function. *rStation Paper riemann_hypothesis_7*, v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/7/v1

[13] C. Delaunay, E. Fricain, E. Mosaki, and O. Robert. Zero free regions for Dirichlet series. *Transactions of the American Mathematical Society*, 365(6):3227–3253, 2013. https://arxiv.org/abs/1101.1199

[14] N. Nikolski. Distance formulae and invariant subspaces, with an application to localization of zeros of the Riemann zeta-function. *Annales de l'Institut Fourier*, 45(1):143–159, 1995. https://doi.org/10.5802/aif.1451

[15] S. Bettin and J. B. Conrey. Period functions and cotangent sums. *Algebra & Number Theory*, 7(1):215–242, 2013. https://arxiv.org/abs/1111.0931

[16] D. Platt and T. Trudgian. The Riemann hypothesis is true up to $3\cdot 10^{12}$. *Bulletin of the London Mathematical Society*, 53(3):792–797, 2021. https://arxiv.org/abs/2004.09765

[17] J.-F. Burnol. A note on Nyman's equivalent formulation of the Riemann Hypothesis. *arXiv preprint math/9910055*, 1999. https://arxiv.org/abs/math/9910055

# First-Octave Indicator Duality, Two-Sided Dyadic Sandwich, and Constraint-Restoring Annihilator Bounds for the Nyman–Beurling–Báez-Duarte Criterion

## 1. Introduction and Problem Setting

The Nyman–Beurling criterion [10, 4] characterizes the Riemann Hypothesis through the density of the linear span of dilations of the fractional-part function $\rho(y) := \{1/y\}$ in $L^2((0, 1), dy)$. In Báez-Duarte's discrete natural-boundary formulation [1], shifting to the anchored reciprocal Hilbert space $\mathcal{H} := L^2((1, \infty), y^{-2}\,dy)$ with inner product $\langle f, g \rangle_{\mathcal{H}} := \int_1^\infty f(y)g(y)y^{-2}\,dy$, the criterion is equivalent to approximating the constant function $1 \in \mathcal{H}$ ($\|1\|_{\mathcal{H}}^2 = 1$) by finite linear combinations of discrete integer-step dilations:
$$\rho_m(y) := \left\lfloor \frac{y}{m} \right\rfloor - \frac{\lfloor y \rfloor}{m} = -\left\{\frac{\lfloor y \rfloor}{m}\right\} \qquad (y > 1, \; m \in \mathbb{Z}_{\ge 2}). \tag{1}$$
For a finite probe set $S \subset \mathbb{Z}_{\ge 2}$ of cardinality $K = |S|$, the unconstrained Báez-Duarte least-squares distance is:
$$d_S^2 := \min_{c \in \mathbb{R}^S} \left\|1 - \sum_{m \in S} c_m \rho_m\right\|_{\mathcal{H}}^2 = 1 - b_S^{\mathsf T} G(S)^{-1} b_S, \tag{2}$$
where $G(S) \in \mathbb{R}^{K \times K}$ has entries $G(m, n) := \langle \rho_m, \rho_n \rangle_{\mathcal{H}}$ and $b_S \in \mathbb{R}^K$ has components $b_m := \langle \rho_m, 1 \rangle_{\mathcal{H}} = -\frac{\log m}{m}$. On cumulative initial blocks $S_{\le N} := \{2, \dots, N\}$, we write $d_N^2 := d_{S_{\le N}}^2$. Báez-Duarte, Balazard, Landreau, and Saias [2] and Báez-Duarte [1] proved that the Riemann Hypothesis is equivalent to:
$$\lim_{N \to \infty} d_N^2 = 0, \tag{3}$$
and established unconditionally that:
$$\liminf_{N \to \infty} d_N^2 \log N \;\ge\; C_{\mathrm{BDBLS}} := 2 + \gamma - \log(4\pi) = 0.0461914179322420676\dots. \tag{4}$$

### 1.1 Relation to Prior Work and Outline of New Contributions

The behavior of $d_N^2$ has been investigated through continuous autocorrelation analysis [3, 6, 7], cotangent sums [5, 6, 7], biorthogonal step systems [11, 14, 15, 17], and harmonic head functionals [15, 16, 18]. In particular:
- **Anchored Bilinear Identity & Autocorrelation Formula:** Ehm [7, §4, eq. (31)] and Paper 21 v2 [12, Theorem 1(b)] derived the cotangent decomposition of $G(m, n)$ and explicit evaluations on small supports;
- **Biorthogonal Step Functions & Dilation Geometry:** The compactly supported dual step functions $L_k \in \mathcal{H}$ ($\langle \rho_m, L_k \rangle_{\mathcal{H}} = \delta_{m, k}$) were introduced by Vasyunin [11] and developed by Bagchi [17, Theorems 1 and 6], Balazard [15, §2], and Paper 7 v1 [14, Theorems 1–2];
- **Harmonic Partial-Sum Representers & Annihilator Subspaces:** The cumulative sums $F_m^* = \sum_{k=1}^m \frac{1}{k} L_k$ were studied as Riesz representers of the harmonic head functional by Balazard [15, Propositions 5–6], Paper 9 v1 [18, §2.1], and Paper 12 v1 [16, §1.1, eq. (7) & §5, eq. (43)], where the $(M - N + 1)$-dimensional finite-support annihilator subspace $\mathcal{S}_M \cap \mathcal{V}_{S_{\le N}}^\perp$ was parameterized in the hybrid basis $\{F_N^*, L_{N+1}, \dots, L_M\}$ to obtain rational lower bounds on $d_N^2$;
- **Difference Wavelet Bases & Dyadic Halving:** The first-difference Haar wavelets $f_n := n\rho_n - (n+1)\rho_{n+1}$, second differences $e_n := f_n - f_{n+1}$, and the dyadic dilation isometry were established in Paper 29 v1 [13, Theorem 5].

The present paper investigates the geometric coupling across the first-octave threshold $y = 2$ and establishes three main results:
1. **First-Octave Indicator Duality, Iterated Dyadic Sandwich, and Unconditional All-Scale Asymptotic Lower Bounds (Theorems 1 & 2):** We prove that the harmonic evaluation functional $u_S(m) := 1/m$ is the exact dual representer of the first-octave indicator $\chi_1 := \mathbf{1}_{[1, 2)} \in \mathcal{H}$ ($\langle \rho_m, -2\chi_1 \rangle_{\mathcal{H}} \equiv 1/m$). Consequently, $U_N := u_{S_{\le N}}^{\mathsf T} G(S_{\le N})^{-1} u_{S_{\le N}} = 4\|P_{S_{\le N}}\chi_1\|_{\mathcal{H}}^2 < 2$ increases monotonically (strictly for all certified integers $2 \le N \le 63$), and splitting $1 = \chi_1 + \mathbf{1}_{[2, \infty)}$ yields the unconditional two-sided dyadic sandwich:
   $$d_{2M} - \frac{1}{\sqrt{2}} d_M \;\le\; \|r_1(2M)\|_{\mathcal{H}} \;=\; \sqrt{\frac{1}{2} - \frac{1}{4} U_{2M}} \;\le\; d_{2M} + \frac{1}{\sqrt{2}} d_M \qquad (\forall\, M \ge 2), \tag{5}$$
   establishing that **the Riemann Hypothesis is equivalent to the complete energy saturation of the harmonic quadratic form**: $\lim_{N \to \infty} d_N^2 = 0 \iff \lim_{N \to \infty} U_N = 2$. Furthermore, iterating (5) across $L(N) = 2\lfloor \log_2(\log N) \rfloor$ dyadic scales and combining with the unconditional lower bound (4) of Báez-Duarte, Balazard, Landreau, and Saias [2] proves **unconditionally for all $N \to \infty$**:
   $$\liminf_{N \to \infty} \|r_1(N)\|_{\mathcal{H}}^2 \log N \;\ge\; \frac{3 - 2\sqrt{2}}{2}\,C_{\mathrm{BDBLS}} \approx 0.00396259719, \tag{6}$$
   $$\liminf_{N \to \infty} (2 - U_N)\log N \;\ge\; 2(3 - 2\sqrt{2})\,C_{\mathrm{BDBLS}} \approx 0.01585038877. \tag{7}$$
2. **Constraint-Restoring Annihilator Exhaustion Theorem and Exact Parity Plateaus (Theorem 3):** Passing from the basis $\{F_N^*, L_{N+1}, \dots, L_M\}$ of [18, 16] via the unitriangular cumulative transformation $L_k = k(F_k^* - F_{k-1}^*)$ to the pure tail representer basis $\mathcal{D}_{N, M}^* := \operatorname{span}\{F_N^*, \dots, F_M^*\} = \mathcal{S}_M \cap \mathcal{V}_{S_{\le N}}^\perp$ diagonalizes the pairing with the first-difference Haar wavelets ($\langle f_n, F_m^* \rangle_{\mathcal{H}} = \delta_{n, m}$). Using this wavelet biorthogonality, we construct an explicit **constraint-restoring approximant** $\tilde{r}_M := r^{(M)} - \sum_{n=1}^{N-1}\langle r^{(M)}, f_n \rangle_{\mathcal{H}} F_n^* \in \mathcal{D}_{N, M}^*$ inside the unit-cell step space $\mathcal{S}_\infty := \overline{\bigcup_{M \ge 1}\mathcal{S}_M} \subsetneq \mathcal{H}$ that restores exact orthogonality to $\mathcal{V}_{S_{\le N}}$ after spatial truncation and proves rigorous $O_N(1/M)$ convergence of both the rational lower bounds $\mathrm{LB}_{\mathrm{dual}}(N, M) \uparrow d_N^2$ and the rational upper bounds $\mathrm{UB}_{\mathrm{dual}}(N, M) \downarrow U_N$. We also prove the exact parity-plateau formulas at $N = 2$: $\mathrm{LB}_{\mathrm{dual}}(2, M) \equiv \sum_{2 \le d \le M,\, d\text{ even}}\frac{1}{d(d+1)}$ ($\mathrm{LB}_{\mathrm{dual}}(2, 2k) = \mathrm{LB}_{\mathrm{dual}}(2, 2k+1)$) and $\mathrm{UB}_{\mathrm{dual}}(2, 2k-1) = \mathrm{UB}_{\mathrm{dual}}(2, 2k)$ for $k \ge 2$.
3. **Exact Dyadic Orthogonal Decomposition, Unconditional Shift Lower Bound, and Fine-Wavelet Sieve Bound (Theorem 4):** Decomposing the full residual across octave doublings yields the exact algebraic identity $d_{2M}^2 \equiv \frac{1}{2} d_M^2 + \Delta_{\mathrm{shift}}(2M)$ where $\Delta_{\mathrm{shift}}(2M) := \varepsilon_{\mathrm{pole}}(2M) - \delta_{\mathrm{odd}}(2M)$. Multi-step Duhamel telescoping combined with (4) proves unconditionally that $\limsup_{M \to \infty} \Delta_{\mathrm{shift}}(2M)\log M \ge \frac{1}{2} C_{\mathrm{BDBLS}} \approx 0.02309570897$, while coarse–fine wavelet splitting of $u_{S_{\le 2M}}^\perp$ proves the Schur-monotone lower bound $\delta_{\mathrm{odd}}(2M) \ge \boldsymbol{\beta}(2M)^{\mathsf T} G_{\mathrm{odd}}(2M)^{-1} \boldsymbol{\beta}(2M)$.

All numerical claims are certified in self-contained 60-digit interval arithmetic (`mpmath.iv.dps = 60`).

---

## 2. Preliminaries: Autocorrelation Formula and Biorthogonal Step Functions

For completeness and reference in subsequent sections, we summarize the established formulas connecting $G(m, n)$, $L_k$, and $F_m^*$:

### Proposition 2.1 (Ehm [7], Paper 21 v2 [12])
*For all integers $m, n \ge 2$, the Báez-Duarte Gram matrix entry $G(m, n) = \langle \rho_m, \rho_n \rangle_{\mathcal{H}}$ is given by the 3-term formula:*
$$G(m, n) \equiv \frac{(n - 1)\log m + (m - 1)\log n}{2 m n} + \frac{\pi}{2 L}\bigl(V(p/q) + V(q/p)\bigr) - \frac{\pi}{2 m n}\bigl(V(1/m) + V(1/n)\bigr), \tag{8}$$
*where $g = \gcd(m, n), L = \operatorname{lcm}(m, n), p = m/g, q = n/g$, and $V(p/q) := -\sum_{k=1}^{q-1}(\{kp/q\} - 1/2)\cot(\pi k/q)$. In particular, the Archimedean constant $C_{\mathrm{diag}} := \log(2\pi) - \gamma$ cancels identically for all $m, n \ge 2$, yielding the exact values on $S = \{2, 3, 4\}$:*
$$G(2, 2) = \frac{\log 2}{4}, \qquad G(2, 3) = \frac{2\log 2 + \log 3}{12} - \frac{\pi}{18\sqrt{3}}, \qquad G(3, 3) = \frac{2\log 3}{9} - \frac{\pi}{27\sqrt{3}}, \tag{9}$$
$$G(2, 4) = \frac{5\log 2}{16} - \frac{\pi}{32}, \qquad G(3, 4) = \frac{4\log 2 + 3\log 3}{24} - \frac{\pi}{24}, \qquad G(4, 4) = \frac{3\log 2}{8} - \frac{\pi}{32}. \tag{10}$$

### Proposition 2.2 (Vasyunin [11], Bagchi [17], Balazard [15], Paper 7 v1 [14], Paper 12 v1 [16])
*(a) Let $\mathcal{S}_M := \operatorname{span}\{\mathbf{1}_{[d, d+1)}\}_{d=1}^M \subset \mathcal{H}$ be the $M$-dimensional subspace of unit-cell step functions supported on $[1, M+1)$, and let $\mathcal{S}_\infty := \overline{\bigcup_{M \ge 1}\mathcal{S}_M} = \{f \in \mathcal{H} : f\text{ is constant on }[d, d+1)\;\forall\,d \ge 1\} \subsetneq \mathcal{H}$ be the closed subspace of unit-cell step functions in $\mathcal{H}$. The step functions $L_k(y) := \sum_{d=1}^k d(d+1)\bigl(\mu(k/d) - \mu(k/(d+1))\bigr)\mathbf{1}_{[d, d+1)}(y) \in \mathcal{S}_k$ ($k \ge 2$) satisfy $\langle \rho_m, L_k \rangle_{\mathcal{H}} \equiv \delta_{m, k}$ for all $m, k \ge 2$, with $\|L_2\|_{\mathcal{H}}^2 = 14$ and $\|L_p\|_{\mathcal{H}}^2 = 2p^2 + 2$ for every odd prime $p$.*

*(b) Setting $L_1 := 2\chi_1 = 2\,\mathbf{1}_{[1, 2)}$, the cumulative sums $F_m^*(y) := \sum_{k=1}^m \frac{1}{k} L_k(y) = \sum_{d=1}^m d(d+1)\bigl(\frac{M_1(\lfloor m/d \rfloor)}{d} - \frac{M_1(\lfloor m/(d+1) \rfloor)}{d+1}\bigr)\mathbf{1}_{[d, d+1)}(y) \in \mathcal{S}_m$ (where $M_1(x) := \sum_{k=1}^{\lfloor x \rfloor}\frac{\mu(k)}{k}$) are the Riesz representers of the harmonic head functional in $\mathcal{H}$ [15, 16, 18], satisfying $\langle 1, F_m^* \rangle_{\mathcal{H}} \equiv M_1(m)$ and uniform $L^2$ boundedness $\sup_{m \ge 1}\|F_m^*\|_{\mathcal{H}} < \infty$ [15, Proposition 6].*

---

## 3. First-Octave Indicator Duality and Harmonic Convergence

### Theorem 1 (First-Octave Indicator Duality and Monotonic Progression)
*(a) **Exact Duality:** Let $\chi_1 := \mathbf{1}_{[1, 2)} \in \mathcal{S}_1 \subset \mathcal{H}$ ($\|\chi_1\|_{\mathcal{H}}^2 = \int_1^2 y^{-2}dy = 1/2$). For every integer $m \ge 2$:*
$$\langle \rho_m, \chi_1 \rangle_{\mathcal{H}} = \int_1^2 \rho_m(y)\frac{dy}{y^2} = -\frac{1}{2m} = -\frac{1}{2} u_S(m), \qquad \langle \rho_m, -2\,\chi_1 \rangle_{\mathcal{H}} \equiv u_S(m). \tag{11}$$

*(b) **Orthogonal Projection of the First Octave:** The orthogonal projection of $\chi_1$ onto $\mathcal{V}_S := \operatorname{span}\{\rho_m\}_{m \in S}$ in $\mathcal{H}$ is $\psi_1(S) := P_{\mathcal{V}_S} \chi_1 = -\frac{1}{2} \sum_{m \in S} q_S^*(m) \rho_m$ where $q_S^* := G(S)^{-1} u_S$. It spans the 1-dimensional orthogonal complement of the pole-canceled subspace $\mathcal{V}_{S, \perp} = \mathcal{V}_S \cap \{\chi_1\}^\perp$ inside $\mathcal{V}_S$, so $\mathcal{V}_S \equiv \mathcal{V}_{S, \perp} \oplus_\perp \mathbb{R}\cdot\psi_1(S)$. Its squared norm is:*
$$\|\psi_1(S)\|_{\mathcal{H}}^2 = \frac{1}{4} u_S^{\mathsf T} G(S)^{-1} u_S = \frac{1}{4} U(S). \tag{12}$$
*Consequently, the projection error $r_1(S) := \chi_1 - \psi_1(S) \in \mathcal{S}_\infty \cap \mathcal{V}_S^\perp$ satisfies the exact Pythagorean identity:*
$$\|r_1(S)\|_{\mathcal{H}}^2 = \|\chi_1\|_{\mathcal{H}}^2 - \|\psi_1(S)\|_{\mathcal{H}}^2 \equiv \frac{1}{2} - \frac{1}{4} U(S) \quad \implies \quad U(S) < 2 \quad (\forall\,\text{finite } S \subset \mathbb{Z}_{\ge 2}). \tag{13}$$

*(c) **Monotonicity and Rank-1 Increment:** On cumulative initial blocks $S_{\le N} = \{2, \dots, N\}$, $U_N := U(S_{\le N})$ is non-decreasing: $U_{N+1} \ge U_N$ for all $N \ge 2$. Setting $g_N := \bigl(G(m, N+1)\bigr)_{m=2}^N \in \mathbb{R}^{N-1}$, the exact rank-1 increment is:*
$$U_{N+1} - U_N = \frac{\bigl(\frac{1}{N+1} - g_N^{\mathsf T} G(S_{\le N})^{-1} u_{S_{\le N}}\bigr)^2}{G(N+1, N+1) - g_N^{\mathsf T} G(S_{\le N})^{-1} g_N} \;\ge\; 0. \tag{14}$$
*Strict monotonicity $U_{N+1} > U_N$ holds whenever $(N+1)^{-1} \ne g_N^{\mathsf T} G(S_{\le N})^{-1} u_{S_{\le N}}$, which is certified in 60-digit interval arithmetic via progressive Cholesky factorization for every integer $2 \le N \le 63$ (`cholesky_all_integers_2_to_64` in `results/dyadic_renormalization_group.json`):*
$$\frac{1}{\log 2} \approx 1.442695 = U_2 < 1.449023 = U_3 < 1.630239 = U_4 < \dots < 1.913186 = U_{64} < 2. \tag{15}$$

*(d) **Telescoping Haar Wavelet Identity:** In the first-difference basis $f_j(y) = j\lfloor y/j \rfloor - (j+1)\lfloor y/(j+1) \rfloor$ ($j \ge 1$), we have $-m\rho_m(y) \equiv \sum_{j=1}^{m-1} f_j(y)$ for all $m \ge 2$ ($y > 1$), so $\mathcal{V}_{S_{\le N}} \equiv \operatorname{span}\{f_1, f_2, \dots, f_{N-1}\}$ and $\mathcal{V}_{S_{\le N}, \perp} \equiv \operatorname{span}\{f_2, \dots, f_{N-1}\}$. The Schur complement in this basis gives:*
$$\frac{1}{U_N} \equiv \operatorname{dist}_{\mathcal{H}}^2\bigl(f_1,\, \operatorname{span}\{f_2, \dots, f_{N-1}\}\bigr) = \log 2 - \mathbf{g}_{1, F}^{\mathsf T} G_{\mathrm{first}}(S_{\le N})^{-1} \mathbf{g}_{1, F} \equiv \frac{1}{2} + \tau_N, \tag{16}$$
*where $\mathbf{g}_{1, F}(m) := \langle f_1, f_m \rangle_{\mathcal{H}}$ ($2 \le m \le N - 1$) and $\tau_N := \operatorname{dist}_{L^2((2, \infty), y^{-2}dy)}^2(f_1, \operatorname{span}\{f_2, \dots, f_{N-1}\}) > 0$.*

*Proof.*
- On $y \in [1, 2)$, $\lfloor y \rfloor = 1$ and $\lfloor y/m \rfloor = 0$ for all $m \ge 2$, so $\rho_m(y) = -1/m$ identically. Integrating against $y^{-2}dy$ on $[1, 2)$ yields $\int_1^2 (-1/m) y^{-2}dy = -1/(2m)$, proving (11).
- The normal equations in $\mathcal{H}$ give $G(S)\alpha = -\frac{1}{2} u_S \implies \alpha = -\frac{1}{2} q_S^*$, establishing (12). For any $\Phi_c \in \mathcal{V}_{S, \perp}$, $\langle \psi_1(S), \Phi_c \rangle_{\mathcal{H}} = \langle \chi_1, \Phi_c \rangle_{\mathcal{H}} = -\frac{1}{2} u_S^{\mathsf T} c = 0$, so $\mathcal{V}_S = \mathcal{V}_{S, \perp} \oplus_\perp \mathbb{R}\cdot\psi_1(S)$. Since $\chi_1 \in \mathcal{S}_1$ cannot lie in $\mathcal{V}_S$ (as $\rho_m(y)$ has jump discontinuities at multiples of $m \ge 2$), $\|r_1(S)\|_{\mathcal{H}}^2 = 1/2 - U(S)/4 > 0$, forcing $U(S) < 2$.
- Nested subspaces $\mathcal{V}_{S_{\le N}} \subset \mathcal{V}_{S_{\le N+1}}$ guarantee $U_{N+1} \ge U_N$. Expanding $u_{S_{\le N+1}}^{\mathsf T} G(S_{\le N+1})^{-1} u_{S_{\le N+1}}$ by the block inversion formula gives (14).
- For (d), $\sum_{j=1}^{m-1} f_j(y) = \lfloor y \rfloor - m\lfloor y/m \rfloor = -m\rho_m(y)$ on $y > 1$. In the basis $(f_1, \dots, f_{N-1})$, the coordinates of $u_{S_{\le N}}$ are $(-1, 0, \dots, 0)^{\mathsf T}$, so $U_N = e_1^{\mathsf T} G_{\mathrm{first}}^{\mathrm{full}}(\{1, \dots, N-1\})^{-1} e_1 = (\|f_1\|_{\mathcal{H}}^2 - \mathbf{g}_{1, F}^{\mathsf T} G_{\mathrm{first}}^{-1} \mathbf{g}_{1, F})^{-1}$, yielding (16). $\blacksquare$

---

## 4. The Two-Sided Dyadic Sandwich and Unconditional Asymptotic Lower Bounds

### Theorem 2 (Two-Sided Dyadic Sandwich, RH Equivalence, and Unconditional All-Scale Lower Bounds)
*(a) **Unconditional Two-Sided Dyadic Sandwich:** For every integer $M \ge 2$, the first-octave residual norm $\|r_1(2M)\|_{\mathcal{H}} = \sqrt{1/2 - U_{2M}/4}$ satisfies:*
$$d_{2M} - \frac{1}{\sqrt{2}} d_M \;\le\; \|r_1(2M)\|_{\mathcal{H}} \;\le\; d_{2M} + \frac{1}{\sqrt{2}} d_M \qquad (\forall\, M \ge 2). \tag{17}$$
*Strict inequality holds whenever $\delta_{\mathrm{odd}}(2M) := \frac{1}{2} d_M^2 - \operatorname{dist}_{\mathcal{H}}^2\bigl(\mathbf{1}_{[2, \infty)}, \mathcal{V}_{S_{\le 2M}, \perp}\bigr) > 0$, which is certified for all $M \in \{2, 4, 8, 16, 32\}$.*

*(b) **Target-Free Equivalence to the Riemann Hypothesis:** The Riemann Hypothesis holds if and only if the harmonic quadratic form $U_N$ saturates to its universal ceiling of $2$:*
$$\lim_{N \to \infty} d_N^2 = 0 \iff \lim_{N \to \infty} U_N = 2 \iff \lim_{N \to \infty} \|r_1(N)\|_{\mathcal{H}}^2 = 0. \tag{18}$$

*(c) **Multi-Step Iterated Dyadic Sandwich and Unconditional All-Scale Asymptotic Lower Bounds:** For all integers $N \ge 2$ and $L \ge 1$, iterating the lower bound in (17) across $L$ dyadic steps yields the finite-scale multi-step inequality:*
$$\frac{d_{2^L N} - 2^{-L/2} d_N}{\sum_{j=0}^{L-1} 2^{-j/2}} = \left(1 - \frac{1}{\sqrt{2}}\right)\frac{d_{2^L N} - 2^{-L/2} d_N}{1 - 2^{-L/2}} \;\le\; \|r_1(2N)\|_{\mathcal{H}} \;\le\; d_{2N} + \frac{1}{\sqrt{2}} d_N. \tag{19}$$
*Consequently, combining (19) at the slowly growing scale depth $L(N) := 2\lfloor \log_2(\log N) \rfloor$ with the unconditional theorem (4) of Báez-Duarte, Balazard, Landreau, and Saias [2] proves **unconditionally as $N \to \infty$ across all integer scales**:*
$$\liminf_{N \to \infty} \|r_1(N)\|_{\mathcal{H}}^2 \log N \;\ge\; C_{r_1} := \frac{3 - 2\sqrt{2}}{2}\,C_{\mathrm{BDBLS}} = 0.003962597193342583\dots, \tag{20}$$
$$\liminf_{N \to \infty} \bigl(2 - U_N\bigr) \log N \;\ge\; 4\,C_{r_1} = 2\bigl(3 - 2\sqrt{2}\bigr)\,C_{\mathrm{BDBLS}} = 0.015850388773370332\dots. \tag{21}$$
*Moreover, under the asymptotic $d_N^2 \sim C_{\mathrm{BDBLS}} / \log N$ conjectured in [2], $\|r_1(N)\|_{\mathcal{H}}^2 \log N$ is trapped asymptotically in the two-sided interval:*
$$\frac{3 - 2\sqrt{2}}{2}\,C_{\mathrm{BDBLS}} \;\le\; \liminf_{N \to \infty} \|r_1(N)\|_{\mathcal{H}}^2 \log N \;\le\; \limsup_{N \to \infty} \|r_1(N)\|_{\mathcal{H}}^2 \log N \;\le\; \frac{3 + 2\sqrt{2}}{2}\,C_{\mathrm{BDBLS}}. \tag{22}$$

*(d) **Cauchy–Schwarz Pole-Residual Inequality and First-Octave Dual Pairing:** The constant value of $r_{\mathrm{full}, N} := 1 - \sum_{m=2}^N c_m^* \rho_m$ on $[1, 2)$ is $D_{c^*}(1) := 1 + \sum_{m=2}^N c_m^* / m = 1 + u_S^{\mathsf T} c^*$, which satisfies:*
$$D_{c^*}(1)^2 \;\le\; d_N^2 \bigl(2 - U_N\bigr) \;<\; 2\,d_N^2 \qquad (\forall\, N \ge 2), \tag{23}$$
*and pairing $L_k$ with $r_1(N)$ yields for all $2 \le k \le N$:*
$$\left|-\frac{1}{2}\bigl(G(S_{\le N})^{-1} u_{S_{\le N}}\bigr)_k - \bigl(\mu(k) - \mu(k/2)\bigr)\right| \;\le\; \|L_k\|_{\mathcal{H}}\,\sqrt{\frac{1}{2} - \frac{1}{4} U_N}. \tag{24}$$

*Proof.*
- **(a):** Split $1 = \chi_1 + \mathbf{1}_{[2, \infty)}$ in $\mathcal{H}$. Projecting onto $\mathcal{V}_{S_{\le 2M}}^\perp$ gives $r_{\mathrm{full}, 2M} = r_1(2M) + r_{\mathrm{tail}}(2M)$, where $r_{\mathrm{tail}}(2M) := (I - P_{S_{\le 2M}})\mathbf{1}_{[2, \infty)}$ and $\|r_{\mathrm{full}, 2M}\|_{\mathcal{H}} = d_{2M}$. By the triangle inequality:
  $$d_{2M} - \|r_{\mathrm{tail}}(2M)\|_{\mathcal{H}} \le \|r_1(2M)\|_{\mathcal{H}} \le d_{2M} + \|r_{\mathrm{tail}}(2M)\|_{\mathcal{H}}.$$
  By the dyadic halving bijection (Paper 29 [13, Theorem 5(c)]; cf. Bagchi [17]), $\mathcal{V}_{S_{\mathrm{even}}, \perp} = D_2(\mathcal{V}_{S_{\le M}})$ where $D_2 f(y) := f(y/2)\mathbf{1}_{y \ge 2}$ ($\|D_2 f\|_{\mathcal{H}}^2 = \frac{1}{2}\|f\|_{\mathcal{H}}^2$), and $\mathbf{1}_{[2, \infty)} = D_2(1)$. Because $\mathcal{V}_{S_{\mathrm{even}}, \perp} \subset \mathcal{V}_{S_{\le 2M}, \perp} \subset \mathcal{V}_{S_{\le 2M}}$:
  $$\|r_{\mathrm{tail}}(2M)\|_{\mathcal{H}}^2 \le \operatorname{dist}_{\mathcal{H}}^2\bigl(\mathbf{1}_{[2, \infty)},\, \mathcal{V}_{S_{\le 2M}, \perp}\bigr) = \frac{1}{2} d_M^2 - \delta_{\mathrm{odd}}(2M) \le \frac{1}{2} d_M^2,$$
  establishing (17).
- **(b):** If $d_N \to 0$, the right-hand inequality in (17) forces $\|r_1(2M)\|_{\mathcal{H}} \to 0 \implies U_{2M} \to 2$, and monotonicity of $U_N$ gives $\lim_{N \to \infty} U_N = 2$. Conversely, if $U_N \to 2$, then $\eta_k := \|r_1(2^k)\|_{\mathcal{H}} \to 0$. The left-hand inequality in (17) gives $d_{2^k} \le \frac{1}{\sqrt{2}} d_{2^{k-1}} + \eta_k \le 2^{-(k-1)/2} d_2 + \sum_{j=2}^k 2^{-(k-j)/2} \eta_j \to 0$ as $k \to \infty$. Monotonicity of $d_N$ yields $\lim_{N \to \infty} d_N = 0$.
- **(c):** For any $N \ge 2$ and $L \ge 1$, applying $d_{2^j N} \le \frac{1}{\sqrt{2}} d_{2^{j-1} N} + \|r_1(2^j N)\|_{\mathcal{H}}$ for $j = 1, \dots, L$ and using the monotonicity $\|r_1(2^j N)\|_{\mathcal{H}} \le \|r_1(2N)\|_{\mathcal{H}}$ ($j \ge 1$) yields:
  $$d_{2^L N} \;\le\; 2^{-L/2} d_N + \sum_{j=1}^L 2^{-(L-j)/2} \|r_1(2^j N)\|_{\mathcal{H}} \;\le\; 2^{-L/2} d_N + \|r_1(2N)\|_{\mathcal{H}} \sum_{m=0}^{L-1} 2^{-m/2},$$
  which rearranges to (19) since $\sum_{m=0}^{L-1} 2^{-m/2} = \frac{1 - 2^{-L/2}}{1 - 2^{-1/2}}$. Now choose $L = L(N) := 2\lfloor \log_2(\log N) \rfloor$ for $N \ge 4$. Using only the trivial upper bound $d_N \le \|1\|_{\mathcal{H}} = 1$, we have $2^{-L(N)/2} d_N \le \frac{2}{\log N} = o\bigl((\log N)^{-1/2}\bigr)$ and $\log(2^{L(N)} N) = \log N + L(N)\log 2 = \bigl(1 + o(1)\bigr)\log N$ as $N \to \infty$. By the unconditional theorem (4) of Báez-Duarte, Balazard, Landreau, and Saias [2], $d_{2^{L(N)} N} \ge \bigl(\sqrt{C_{\mathrm{BDBLS}}} - o(1)\bigr)\bigl(\log(2^{L(N)} N)\bigr)^{-1/2} = \bigl(\sqrt{C_{\mathrm{BDBLS}}} - o(1)\bigr)(\log N)^{-1/2}$. Substituting into (19) and squaring yields $\liminf_{N \to \infty} \|r_1(2N)\|_{\mathcal{H}}^2 \log(2N) \ge \bigl(1 - 2^{-1/2}\bigr)^2 C_{\mathrm{BDBLS}} = \frac{3 - 2\sqrt{2}}{2} C_{\mathrm{BDBLS}}$. For odd $N = 2M - 1$, monotonicity $\|r_1(2M)\|_{\mathcal{H}} \le \|r_1(2M - 1)\|_{\mathcal{H}}$ and $\log(2M - 1) \sim \log(2M)$ extend the bound to all integers $N \to \infty$, proving (20) and (21) (since $2 - U_N = 4\|r_1(N)\|_{\mathcal{H}}^2$). Under $d_N^2 \sim C_{\mathrm{BDBLS}}/\log N$, the upper bound in (17) gives $\limsup_{N \to \infty}\|r_1(N)\|_{\mathcal{H}}^2\log N \le \bigl(1 + 2^{-1/2}\bigr)^2 C_{\mathrm{BDBLS}} = \frac{3 + 2\sqrt{2}}{2} C_{\mathrm{BDBLS}}$, proving (22).
- **(d):** On $[1, 2)$, $r_{\mathrm{full}, N} \equiv D_{c^*}(1)$. Since $r_{\mathrm{full}, N} \perp \psi_1(N)$, we have $\frac{1}{2} D_{c^*}(1) = \langle r_{\mathrm{full}, N}, \chi_1 \rangle_{\mathcal{H}} = \langle r_{\mathrm{full}, N}, r_1(N) \rangle_{\mathcal{H}}$. Cauchy–Schwarz yields $\frac{1}{4} D_{c^*}(1)^2 \le d_N^2 \|r_1(N)\|_{\mathcal{H}}^2 = \frac{1}{4} d_N^2(2 - U_N)$, proving (23). Pairing $L_k$ with $r_1(N)$ gives (24). $\blacksquare$

---

## 5. Dual Variational Bounds and Constraint-Restoring Annihilator Exhaustion

### Theorem 3 (Wavelet Biorthogonality, Constraint-Restoring Exhaustion, and Parity Plateaus)
*(a) **Wavelet Dual Biorthogonality:** The first-difference Haar wavelets $f_n = n\rho_n - (n+1)\rho_{n+1}$ and second-difference wavelets $e_n = f_n - f_{n+1}$ satisfy exact biorthogonality with $F_m^*$ and $E_m^* := \sum_{k=1}^m F_k^*$ for all $n, m \ge 1$:*
$$\langle f_n, F_m^* \rangle_{\mathcal{H}} \equiv \delta_{n, m}, \qquad \langle e_n, E_m^* \rangle_{\mathcal{H}} \equiv \delta_{n, m}, \qquad \langle 1, E_m^* \rangle_{\mathcal{H}} \equiv (m+1)M_1(m) - M(m). \tag{25}$$
*In particular, for every $N \ge 2$, the dual step functions satisfy the strict probe-annihilation property:*
$$\langle \rho_m, F_k^* \rangle_{\mathcal{H}} \equiv 0 \qquad (\forall\, 2 \le m \le N, \; \forall\, k \ge N). \tag{26}$$

*(b) **Annihilator Subspace Basis and Cumulative Basis Change:** For any integers $M \ge N \ge 2$, the tail representer space $\mathcal{D}_{N, M}^* := \operatorname{span}\{F_N^*, F_{N+1}^*, \dots, F_M^*\}$ has dimension $M - N + 1$ and is the exact orthogonal complement of $\mathcal{V}_{S_{\le N}}$ inside $\mathcal{S}_M$:*
$$\mathcal{D}_{N, M}^* \equiv \mathcal{S}_M \cap \mathcal{V}_{S_{\le N}}^\perp = \operatorname{span}\{F_N^*, L_{N+1}, \dots, L_M\}, \tag{27}$$
*related to the hybrid annihilator basis $\{F_N^*, L_{N+1}, \dots, L_M\}$ of Paper 9 v1 [18, §2.1] and Paper 12 v1 [16, §1.1, eq. (7) & §5, eq. (43)] by the invertible upper-triangular transformation $F_k^* = F_N^* + \sum_{j=N+1}^k \frac{1}{j} L_j$ ($L_k = k(F_k^* - F_{k-1}^*)$ for $k > N$).*

*(c) **Constraint-Restoring Annihilator Exhaustion Theorem ($O_N(1/M)$ Convergence in $\mathcal{S}_\infty$):** Let $G_{\mathcal{D}^*}(N, M) \in \mathbb{Q}^{(M-N+1)\times(M-N+1)}$ have entries $\langle F_k^*, F_\ell^* \rangle_{\mathcal{H}}$ ($N \le k, \ell \le M$), and define target vectors $\mathbf{m}_{N, M}(k) := \langle 1, F_k^* \rangle_{\mathcal{H}} = M_1(k)$ and $\mathbf{m}_{1, N, M}(k) := \langle \chi_1, F_k^* \rangle_{\mathcal{H}} = M_1(k) - \frac{1}{2} M_1(\lfloor k/2 \rfloor)$. Then for every $M \ge N \ge 2$:*
$$d_N^2 \;\ge\; \mathrm{LB}_{\mathrm{dual}}(N, M) := \|P_{\mathcal{D}_{N, M}^*} 1\|_{\mathcal{H}}^2 = \mathbf{m}_{N, M}^{\mathsf T} G_{\mathcal{D}^*}(N, M)^{-1} \mathbf{m}_{N, M}, \tag{28}$$
$$U_N \;\le\; \mathrm{UB}_{\mathrm{dual}}(N, M) := 2 - 4\,\|P_{\mathcal{D}_{N, M}^*} \chi_1\|_{\mathcal{H}}^2 = 2 - 4\,\mathbf{m}_{1, N, M}^{\mathsf T} G_{\mathcal{D}^*}(N, M)^{-1} \mathbf{m}_{1, N, M}. \tag{29}$$
*Moreover, for any residual $r \in \{r_{\mathrm{full}, N}, r_1(N)\} \subset \mathcal{S}_\infty \cap \mathcal{V}_{S_{\le N}}^\perp$ and any $M \ge N$, the naive spatial truncation $r^{(M)} := r\mathbf{1}_{[1, M+1)} \in \mathcal{S}_M$ is restored to exact membership in $\mathcal{D}_{N, M}^* = \mathcal{S}_M \cap \mathcal{V}_{S_{\le N}}^\perp$ by the **constraint-restoring approximant**:*
$$\tilde{r}_M := r^{(M)} - \sum_{n=1}^{N-1} \langle r^{(M)}, f_n \rangle_{\mathcal{H}}\, F_n^* \;\in\; \mathcal{D}_{N, M}^*. \tag{30}$$
*Setting $B_N := \sup_{y > 1}|r(y)| < \infty$, the approximation error satisfies the explicit bound:*
$$\|r - P_{\mathcal{D}_{N, M}^*} r\|_{\mathcal{H}}^2 \;\le\; \|r - \tilde{r}_M\|_{\mathcal{H}}^2 \;=\; \|r - r^{(M)}\|_{\mathcal{H}}^2 + \left\|\sum_{n=1}^{N-1} \langle r^{(M)}, f_n \rangle_{\mathcal{H}}\, F_n^*\right\|_{\mathcal{H}}^2 \;\le\; \frac{B_N^2}{M+1} + \frac{B_N^2}{(M+1)^2}\left(\sum_{n=1}^{N-1}(n+1)\|F_n^*\|_{\mathcal{H}}\right)^2, \tag{31}$$
*proving that for every fixed $N \ge 2$, $\mathrm{LB}_{\mathrm{dual}}(N, M) \uparrow d_N^2$ and $\mathrm{UB}_{\mathrm{dual}}(N, M) \downarrow U_N$ as $M \to \infty$ at the rigorous rate:*
$$0 \;\le\; d_N^2 - \mathrm{LB}_{\mathrm{dual}}(N, M) \;=\; O_N\!\left(\frac{1}{M}\right), \qquad 0 \;\le\; \mathrm{UB}_{\mathrm{dual}}(N, M) - U_N \;=\; O_N\!\left(\frac{1}{M}\right). \tag{32}$$

*(d) **Monotonicity and Exact $N = 2$ Complementary Parity-Plateau Formulas:** Because $\mathcal{D}_{N, M}^* \subset \mathcal{D}_{N, M+1}^*$, $\mathrm{LB}_{\mathrm{dual}}(N, M)$ is non-decreasing in $M$ and $\mathrm{UB}_{\mathrm{dual}}(N, M)$ is non-increasing in $M$. Monotonicity in $M$ is non-strict in general: at $N = 2$, $\mathrm{LB}_{\mathrm{dual}}(2, M)$ and $\mathrm{UB}_{\mathrm{dual}}(2, M)$ satisfy the exact complementary parity-plateau identities for all $M \ge 2$:*
$$\mathrm{LB}_{\mathrm{dual}}(2, M) \;\equiv\; \sum_{\substack{2 \le d \le M \\ d\text{ even}}} \frac{1}{d(d+1)} \;\uparrow\; 1 - \log 2 = d_2^2, \qquad \mathrm{LB}_{\mathrm{dual}}(2, 2k) = \mathrm{LB}_{\mathrm{dual}}(2, 2k+1) \quad (\forall\, k \ge 1), \tag{33}$$
$$\mathrm{UB}_{\mathrm{dual}}(2, M) \;\equiv\; \left(\sum_{\substack{1 \le d \le M \\ d\text{ odd}}} \frac{1}{d(d+1)}\right)^{-1} \;\downarrow\; \frac{1}{\log 2} = U_2, \qquad \mathrm{UB}_{\mathrm{dual}}(2, 2k-1) = \mathrm{UB}_{\mathrm{dual}}(2, 2k) \quad (\forall\, k \ge 2), \tag{34}$$
*with $\mathrm{LB}_{\mathrm{dual}}(2, 2) = \mathrm{LB}_{\mathrm{dual}}(2, 3) = \frac{1}{6}$, $\mathrm{LB}_{\mathrm{dual}}(2, 4) = \mathrm{LB}_{\mathrm{dual}}(2, 5) = \frac{13}{60}$, $\mathrm{UB}_{\mathrm{dual}}(2, 2) = 2$, and $\mathrm{UB}_{\mathrm{dual}}(2, 3) = \mathrm{UB}_{\mathrm{dual}}(2, 4) = \frac{12}{7}$.*

*(e) **Pointwise and Collective $\ell^2$ Harmonic Discrepancy Bounds:** For all $1 \le n \le N - 1$, the optimal Báez-Duarte coefficients $c_N^*$ satisfy:*
$$\left|\left(-\sum_{m=n+1}^N \frac{c_{N, m}^*}{m}\right) - M_1(n)\right| \;\le\; \|F_n^*\|_{\mathcal{H}}\, d_N \;\le\; C_N\, d_N, \tag{35}$$
$$\sum_{n=1}^{N-1}\left|\left(-\sum_{m=n+1}^N \frac{c_{N, m}^*}{m}\right) - M_1(n)\right|^2 \;\le\; \lambda_{\max}\bigl(M_{F, \mathrm{full}}^*(N)\bigr)\, d_N^2, \tag{36}$$
*where $C_N := \max_{1 \le k < N}\|F_k^*\|_{\mathcal{H}}$ is certified to satisfy $C_N \le \sqrt{2}$ for all $N \le 64$ (with $\|F_1^*\|^2 = 2, \|F_2^*\|^2 = \frac{3}{2}, \|F_3^*\|^2 = \frac{31}{18}, \|F_4^*\|^2 = \frac{25}{18}$). Furthermore, $\lambda_{\min}\bigl(L_{N-3}^{-1/2} G_{\mathrm{diff}}(S_{\le N}) L_{N-3}^{-1/2}\bigr) \ge \lambda_{\min}\bigl(G_{\mathrm{first}}(S_{\le N})\bigr) \ge \|M_F^*(S_{\le N})\|_\infty^{-1}$.*

*Proof.*
- **(a)–(b):** Since $f_n = n\rho_n - (n+1)\rho_{n+1}$ ($y > 1, \rho_1 \equiv 0$), we have $\langle f_n, \frac{1}{k}L_k \rangle_{\mathcal{H}} = \delta_{n, k} - \delta_{n+1, k}$ for $k \ge 2$ and $\langle f_n, L_1 \rangle_{\mathcal{H}} = \delta_{n, 1}$. Summing over $1 \le k \le m$ gives $\langle f_n, F_m^* \rangle_{\mathcal{H}} \equiv \delta_{n, m}$, and summing $F_k^*$ over $1 \le k \le m$ gives $\langle e_n, E_m^* \rangle_{\mathcal{H}} \equiv \delta_{n, m}$. Since $-m\rho_m = \sum_{n=1}^{m-1} f_n$, for any $k \ge N \ge m$ every index $n \le m-1 < N \le k$ satisfies $\langle f_n, F_k^* \rangle_{\mathcal{H}} = 0$, establishing (26). Since $\dim \mathcal{S}_M = M$ and the $N-1$ functionals $\langle \rho_m, \cdot \rangle_{\mathcal{H}}$ ($2 \le m \le N$) are linearly independent on $\mathcal{S}_M$ (with duals $L_2, \dots, L_N \in \mathcal{S}_M$), $\dim(\mathcal{S}_M \cap \mathcal{V}_{S_{\le N}}^\perp) = M - N + 1$. The upper-triangular relation $F_k^* = F_N^* + \sum_{j=N+1}^k \frac{1}{j} L_j$ shows that $\{F_N^*, \dots, F_M^*\}$ and $\{F_N^*, L_{N+1}, \dots, L_M\}$ [18, 16] span the exact same $(M-N+1)$-dimensional subspace $\mathcal{D}_{N, M}^* = \mathcal{S}_M \cap \mathcal{V}_{S_{\le N}}^\perp$.
- **(c):** Since $\mathcal{D}_{N, M}^* \subset \mathcal{V}_{S_{\le N}}^\perp$, we have $P_{\mathcal{D}_{N, M}^*} 1 = P_{\mathcal{D}_{N, M}^*} r_{\mathrm{full}, N}$ and $P_{\mathcal{D}_{N, M}^*} \chi_1 = P_{\mathcal{D}_{N, M}^*} r_1(N)$, so Pythagoras gives $d_N^2 - \mathrm{LB}_{\mathrm{dual}}(N, M) = \|r_{\mathrm{full}, N} - P_{\mathcal{D}_{N, M}^*} r_{\mathrm{full}, N}\|_{\mathcal{H}}^2 \ge 0$ and $\mathrm{UB}_{\mathrm{dual}}(N, M) - U_N = 4\|r_1(N) - P_{\mathcal{D}_{N, M}^*} r_1(N)\|_{\mathcal{H}}^2 \ge 0$. Notice that $\bigcup_{M \ge 1}\mathcal{S}_M$ is dense in $\mathcal{S}_\infty \subsetneq \mathcal{H}$ (not in $\mathcal{H}$ itself), and $1, \chi_1, \rho_m \in \mathcal{S}_\infty$, so $r \in \{r_{\mathrm{full}, N}, r_1(N)\}$ lies in $\mathcal{S}_\infty \cap \mathcal{V}_{S_{\le N}}^\perp$ and is bounded on $(1, \infty)$ by $B_N := 1 + \sum_{m=2}^N |c_m| < \infty$. For $M \ge N$, the naive truncation $r^{(M)} := r\mathbf{1}_{[1, M+1)} \in \mathcal{S}_M$ is no longer orthogonal to $\mathcal{V}_{S_{\le N}}$ because $\langle r^{(M)}, f_n \rangle_{\mathcal{H}} = -\langle r - r^{(M)}, f_n \rangle_{\mathcal{H}}$ ($1 \le n \le N-1$). Subtracting $\sum_{n=1}^{N-1}\langle r^{(M)}, f_n \rangle_{\mathcal{H}} F_n^* \in \mathcal{S}_{N-1} \subset \mathcal{S}_M$ defines $\tilde{r}_M \in \mathcal{S}_M$ in (30). By wavelet biorthogonality $\langle f_m, F_n^* \rangle_{\mathcal{H}} = \delta_{m, n}$, we have for every $1 \le m \le N-1$:
  $$\langle \tilde{r}_M, f_m \rangle_{\mathcal{H}} \;=\; \langle r^{(M)}, f_m \rangle_{\mathcal{H}} - \sum_{n=1}^{N-1} \langle r^{(M)}, f_n \rangle_{\mathcal{H}}\,\delta_{m, n} \;=\; 0.$$
  Since $\mathcal{V}_{S_{\le N}} = \operatorname{span}\{f_1, \dots, f_{N-1}\}$, this proves $\tilde{r}_M \in \mathcal{S}_M \cap \mathcal{V}_{S_{\le N}}^\perp = \mathcal{D}_{N, M}^*$. Because $r - r^{(M)}$ is supported on $[M+1, \infty)$ while $r^{(M)} - \tilde{r}_M \in \mathcal{S}_{N-1}$ is supported on $[1, N) \subset [1, M+1)$, the two error components $r - r^{(M)}$ and $r^{(M)} - \tilde{r}_M$ have disjoint supports and are strictly orthogonal in $\mathcal{H}$. Moreover, $\|r - r^{(M)}\|_{\mathcal{H}}^2 = \int_{M+1}^\infty |r(y)|^2 y^{-2}dy \le \frac{B_N^2}{M+1}$, and since $|f_n(y)| = |n\{y/n\} - (n+1)\{y/(n+1)\}| \le n+1$, we have:
  $$\bigl|\langle r^{(M)}, f_n \rangle_{\mathcal{H}}\bigr| \;=\; \left|\int_{M+1}^\infty r(y)f_n(y)\frac{dy}{y^2}\right| \;\le\; \frac{B_N(n+1)}{M+1}.$$
  Combining these via the Pythagorean theorem establishes (31) and the $O_N(1/M)$ convergence rate (32).
- **(d):** At $N = 2$, $\rho_2(y) = -\frac{1}{2}$ on odd cells $[2k-1, 2k)$ and $\rho_2(y) = 0$ on even cells $[2k, 2k+1)$. Thus $\mathcal{S}_M$ splits orthogonally into $\mathcal{S}_{M, \mathrm{even}} \oplus_\perp \mathcal{S}_{M, \mathrm{odd}}$, where $\mathcal{S}_{M, \mathrm{even}} \subset \mathcal{D}_{2, M}^*$ and $\mathcal{D}_{2, M}^* \cap \mathcal{S}_{M, \mathrm{odd}}$ is the hyperplane in $\mathcal{S}_{M, \mathrm{odd}}$ orthogonal to $\mathbf{1}_{\mathrm{odd}, M} := \sum_{1 \le d \le M,\, d\text{ odd}}\mathbf{1}_{[d, d+1)}$. Since $1\big|_{\mathcal{S}_{M, \mathrm{odd}}} = \mathbf{1}_{\mathrm{odd}, M}$, the projection $P_{\mathcal{D}_{2, M}^*} 1$ vanishes on all odd cells and equals $1$ on all even cells $[d, d+1)$ ($2 \le d \le M$), giving $\mathrm{LB}_{\mathrm{dual}}(2, M) = \sum_{2 \le d \le M,\, d\text{ even}}\frac{1}{d(d+1)} \uparrow 1 - \log 2 = 1 - \frac{(-\frac{1}{2}\log 2)^2}{\frac{1}{4}\log 2} = d_2^2$, proving (33). Similarly, $\chi_1 = \mathbf{1}_{[1, 2)} \in \mathcal{S}_{M, \mathrm{odd}}$, so $\|P_{\mathcal{D}_{2, M}^*} \chi_1\|_{\mathcal{H}}^2 = \|\chi_1\|_{\mathcal{H}}^2 - \frac{\langle \chi_1, \mathbf{1}_{\mathrm{odd}, M} \rangle_{\mathcal{H}}^2}{\|\mathbf{1}_{\mathrm{odd}, M}\|_{\mathcal{H}}^2} = \frac{1}{2} - \frac{1}{4\sum_{1 \le d \le M,\, d\text{ odd}}\frac{1}{d(d+1)}}$, which substitutes into (29) to yield (34).
- **(e):** Expanding $\sum_{m=2}^N c_{N, m}^* \rho_m = \sum_{n=1}^{N-1}(-\sum_{m=n+1}^N \frac{c_{N, m}^*}{m})f_n$ and pairing $r_{\mathrm{full}, N}$ with $F_n^*$ yields $v_n := \langle r_{\mathrm{full}, N}, F_n^* \rangle_{\mathcal{H}} = M_1(n) - (-\sum_{m=n+1}^N \frac{c_{N, m}^*}{m})$. Cauchy–Schwarz gives (35), and projection onto $\operatorname{span}\{F_1^*, \dots, F_{N-1}^*\}$ gives (36). $\blacksquare$

---

## 6. Two-Residual Orthogonal Decomposition and Unconditional Shift Lower Bound

### Theorem 4 (Two-Residual Master Identity, Dyadic Recurrence, and Unconditional Shift Bound)
*(a) **Two-Residual Master Identity:** Let $r_{\ge 2}(N) := \mathbf{1}_{[2, \infty)} - P_{\mathcal{V}_{S_{\le N}, \perp}}\mathbf{1}_{[2, \infty)}$ be the pole-canceled tail residual ($\|r_{\ge 2}(N)\|_{\mathcal{H}}^2 = d_{\mathrm{anch},\perp}^2(S_{\le N}) - \frac{1}{2}$). For every $N \ge 3$, the inner product across $y = 2$ is given by the exact identity:*
$$\langle r_1(N), r_{\ge 2}(N) \rangle_{\mathcal{H}} \equiv \frac{1}{2} D_{c^*}(1) - \|r_1(N)\|_{\mathcal{H}}^2 = \frac{1}{2}\left(D_{c^*}(1) - \left(1 - \frac{1}{2} U_N\right)\right), \tag{37}$$
*which is certified in 60-digit interval arithmetic to be strictly negative for every integer $3 \le N \le 64$, and the unconstrained distance satisfies:*
$$d_N^2 \equiv \|r_1(N)\|_{\mathcal{H}}^2 + \|r_{\ge 2}(N)\|_{\mathcal{H}}^2 + 2\langle r_1(N), r_{\ge 2}(N) \rangle_{\mathcal{H}} - \frac{\langle r_1(N), r_{\ge 2}(N) \rangle_{\mathcal{H}}^2}{\|\psi_1(N)\|_{\mathcal{H}}^2}. \tag{38}$$

*(b) **Exact Dyadic Decomposition and Unconditional Shift Lower Bound:** For every octave doubling $M \to 2M$ ($M \ge 2$), the least-squares distance decomposes algebraically as:*
$$d_{2M}^2 \equiv \frac{1}{2} d_M^2 + \Delta_{\mathrm{shift}}(2M), \qquad \Delta_{\mathrm{shift}}(2M) := \varepsilon_{\mathrm{pole}}(2M) - \delta_{\mathrm{odd}}(2M), \tag{39}$$
*where $\delta_{\mathrm{odd}}(2M) := \frac{1}{2} d_M^2 - \|r_{\ge 2}(2M)\|_{\mathcal{H}}^2 \ge 0$ and $\varepsilon_{\mathrm{pole}}(2M) := \frac{1}{2} - (d_{\mathrm{anch},\perp}^2(S_{\le 2M}) - d_{2M}^2)$. Unrolling (39) across $L \ge 1$ dyadic steps yields for all $M \ge 2$:*
$$\max_{1 \le j \le L} \Delta_{\mathrm{shift}}(2^j M) \;\ge\; \frac{d_{2^L M}^2 - 2^{-L} d_M^2}{2\bigl(1 - 2^{-L}\bigr)}. \tag{40}$$
*Choosing $L = L(M) := 2\lfloor \log_2(\log M) \rfloor$ and applying the unconditional theorem (4) of Báez-Duarte, Balazard, Landreau, and Saias [2] proves **unconditionally**:*
$$\limsup_{M \to \infty} \Delta_{\mathrm{shift}}(2M)\log M \;\ge\; C_{\mathrm{shift}} := \frac{1}{2}\,C_{\mathrm{BDBLS}} = 0.0230957089661210338\dots, \tag{41}$$
*and under $d_N^2 \sim C_{\mathrm{BDBLS}}/\log N$, $\lim_{M \to \infty} \Delta_{\mathrm{shift}}(2M)\log M = \frac{1}{2} C_{\mathrm{BDBLS}}$ whenever the limit exists.*

*(c) **Coarse–Fine Wavelet Splitting and Schur-Monotone Lower Bound:** Decomposing $u_{S_{\le 2M}}^\perp = \mathcal{V}_{S_{\mathrm{even}}, \perp} \oplus \mathcal{W}_{\mathrm{odd}}(2M)$ into coarse sums $f_{2k} + f_{2k+1}$ and fine second differences $e_{2k} = f_{2k} - f_{2k+1} \in \{u, \mathbf{1}\}^\perp$, let $G_{\mathrm{odd}}(2M)_{j, k} := \langle e_{2j}, e_{2k} \rangle_{\mathcal{H}}$ and $\beta_k(2M) := \langle r_{\mathrm{ev}, 2M}, e_{2k} \rangle_{\mathcal{H}}$ where $r_{\mathrm{ev}, 2M} := 1 - P_{\mathcal{V}_{S_{\mathrm{even}}, \perp}} 1$. By Schur-complement operator monotonicity:*
$$\delta_{\mathrm{odd}}(2M) \;\ge\; \boldsymbol{\beta}(2M)^{\mathsf T} G_{\mathrm{odd}}(2M)^{-1} \boldsymbol{\beta}(2M) \;\ge\; 0, \tag{42}$$
*with strict positivity $\delta_{\mathrm{odd}}(2M) > 0$ certified for all $2M \in \{4, 8, 16, 32, 64\}$. At $2M = 4$, $\mathcal{W}_{\mathrm{odd}}(4) = \mathbb{R}\cdot e_2$ with $\|e_2\|_{\mathcal{H}}^2 \equiv \pi$, yielding the exact closed form:*
$$\delta_{\mathrm{odd}}(4) \equiv \frac{2\log 2\left(\log\!\left(\frac{3}{2\sqrt{2}}\right) + \frac{\pi}{4} - \frac{\pi}{3\sqrt{3}}\right)^2}{2\pi\log 2 - \left(2\log 3 - 3\log 2 + \frac{2\pi}{3\sqrt{3}} - \frac{\pi}{2}\right)^2} = 0.0185403625113767\dots. \tag{43}$$

*Proof.*
- **(a):** Since $\mathcal{V}_S = \mathcal{V}_{S, \perp} \oplus_\perp \mathbb{R}\cdot\psi_1(S)$ and $\chi_1 \perp \mathcal{V}_{S, \perp}$, we have $1 - P_{\mathcal{V}_{S, \perp}} 1 = \chi_1 + r_{\ge 2}(N)$, and projecting away from $\psi_1(N)$ gives $r_{\mathrm{full}, N} = (I - P_{\mathbb{R}\cdot\psi_1})(r_1(N) + r_{\ge 2}(N))$. Pairing with $\chi_1$ gives $\frac{1}{2}D_{c^*}(1) = \|r_1\|^2 + \langle r_1, r_{\ge 2} \rangle$, establishing (37) and (38).
- **(b):** Combining $d_{\mathrm{anch},\perp}^2(S_{\mathrm{even}}) = \frac{1}{2} + \frac{1}{2} d_M^2$ with $\delta_{\mathrm{odd}}(2M) = d_{\mathrm{anch},\perp}^2(S_{\mathrm{even}}) - d_{\mathrm{anch},\perp}^2(S_{\le 2M})$ and $\Delta_{\mathrm{pole}}(2M) = d_{\mathrm{anch},\perp}^2(S_{\le 2M}) - d_{2M}^2 = \frac{1}{2} - \varepsilon_{\mathrm{pole}}(2M)$ proves (39). Unrolling (39) $L$ times gives $d_{2^L M}^2 - 2^{-L} d_M^2 = \sum_{j=1}^L 2^{-(L-j)} \Delta_{\mathrm{shift}}(2^j M) \le 2(1 - 2^{-L})\max_{1 \le j \le L}\Delta_{\mathrm{shift}}(2^j M)$, proving (40). Setting $L = L(M) := 2\lfloor \log_2(\log M) \rfloor$, we have $2^{-L} d_M^2 \le 4(\log M)^{-2} = o\bigl((\log M)^{-1}\bigr)$ and $\log(2^L M) \sim \log M$, so (4) forces $\max_{1 \le j \le L(M)} \Delta_{\mathrm{shift}}(2^j M)\log(2^j M) \ge \frac{1}{2} C_{\mathrm{BDBLS}} - o(1)$, establishing (41).
- **(c):** Because $r_{\mathrm{ev}, 2M} \perp \mathcal{V}_{S_{\mathrm{even}}, \perp}$, its projection onto $P_{\mathcal{V}_{S_{\mathrm{even}}, \perp}^\perp}\mathcal{W}_{\mathrm{odd}}(2M)$ has Gram matrix $\Sigma_{\mathrm{odd}\mid\mathrm{ev}} \preceq G_{\mathrm{odd}}$, so $\Sigma_{\mathrm{odd}\mid\mathrm{ev}}^{-1} \succeq G_{\mathrm{odd}}^{-1}$, yielding (42). Evaluating at $2M = 4$ yields (43). $\blacksquare$

---

## 7. Certified 60-Digit Interval Receipts (`mpmath.iv.dps = 60`)

All quantities are certified using the self-contained supplement script `src/verify_dyadic_renormalization_group.py` with directed rounding in 60 decimal digits (`results/dyadic_renormalization_group.json`).

### Table 1: Harmonic Quadratic Form, First-Octave Error, and Dual Rational Bounds ($S_{\le N} = \{2, \dots, N\}$)

| Cutoff $N$ | Distance $d_N^2$ | Dual $\mathrm{LB}(N, 2N)$ | Harmonic $U_N$ | Dual $\mathrm{UB}(N, 2N)$ | Octave $\|r_1\|^2$ | Pole $D_{c^*}(1)$ | Bound $d_N^2(2 - U_N)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $N = 2$ | $0.30685282$ | $0.21666667$ | $1.44269504$ | $1.71428571$ | $0.13932624$ | $0$ | $0.17101060$ |
| $N = 3$ | $0.09574778$ | $0.06328083$ | $1.44902281$ | $1.62954916$ | $0.13774430$ | $-0.03654894$ | $0.05275484$ |
| $N = 4$ | $0.06595169$ | $0.03847585$ | $1.63023887$ | $1.74916217$ | $0.09244028$ | $+0.03693256$ | $0.02438637$ |
| $N = 8$ | $0.02424453$ | $0.01426724$ | $1.81299398$ | $1.87130890$ | $0.04675150$ | $+0.04979042$ | $0.00453387$ |
| $N = 16$ | $0.01793627$ | $0.01194771$ | $1.87451007$ | $1.90728525$ | $0.03137248$ | $+0.04058265$ | $0.00225082$ |
| $N = 32$ | $0.01407701$ | $0.00849422$ | $1.89491960$ | $1.92265914$ | $0.02627010$ | $+0.03357624$ | $0.00147922$ |
| $N = 64$ | $0.01139247$ | $0.00755189$ | $1.91318614$ | $1.93852478$ | $0.02170346$ | $+0.02746046$ | $0.00098903$ |

### Table 2: Certified Dyadic Decomposition Steps and Two-Sided Sandwich ($M \to 2M$)

| Scale $M \to 2M$ | $\frac{1}{2} d_M^2$ | Odd Gain $\delta_{\mathrm{odd}}$ | Wavelet Bound $\mathrm{LB}_{\mathcal{W}_{\mathrm{odd}}}$ | Pole Defect $\varepsilon_{\mathrm{pole}}$ | Net Shift $\Delta_{\mathrm{shift}}$ | New $d_{2M}^2$ | Lower Sandwich | $\|r_1(2M)\|$ | Upper Sandwich |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $2 \to 4$ | $0.15342641$ | $0.01854036$ | $0.01828730$ | $-0.06893435$ | $-0.08747472$ | $0.06595169$ | $-0.134886$ | $0.304040$ | $0.648507$ |
| $4 \to 8$ | $0.03297585$ | $0.01071630$ | $0.01049597$ | $+0.00198498$ | $-0.00873132$ | $0.02424453$ | $-0.025886$ | $0.216221$ | $0.337299$ |
| $8 \to 16$ | $0.01212226$ | $0.00313414$ | $0.00271614$ | $+0.00894814$ | $+0.00581400$ | $0.01793627$ | $+0.023825$ | $0.177123$ | $0.244027$ |
| $16 \to 32$ | $0.00896813$ | $0.00200748$ | $0.00150993$ | $+0.00711636$ | $+0.00510888$ | $0.01407701$ | $+0.023946$ | $0.162081$ | $0.213347$ |
| $32 \to 64$ | $0.00703851$ | $0.00127012$ | $0.00088023$ | $+0.00562408$ | $+0.00435397$ | $0.01139247$ | $+0.022840$ | $0.147321$ | $0.190631$ |

---

## 8. Discussion and Scope Limits

1. **Target-Free Duality and Unconditional Logarithmic Lower Bounds:** Theorems 1 and 2 establish that the Nyman–Beurling–Báez-Duarte criterion admits an equivalent formulation independent of the target function $1$: approximating the first-octave indicator $\chi_1 = \mathbf{1}_{[1, 2)}$ completely in energy ($U_N \to 2$) is unconditionally equivalent to $d_N \to 0$. Moreover, iterating the two-sided dyadic sandwich across $L(N) = 2\lfloor \log_2(\log N) \rfloor$ scales transfers the unconditional theorem of Báez-Duarte, Balazard, Landreau, and Saias [2] to the first octave, establishing the unconditional asymptotic lower bounds $\liminf_{N \to \infty}\|r_1(N)\|_{\mathcal{H}}^2\log N \ge \frac{3 - 2\sqrt{2}}{2} C_{\mathrm{BDBLS}}$ and $\liminf_{N \to \infty}(2 - U_N)\log N \ge 2(3 - 2\sqrt{2}) C_{\mathrm{BDBLS}}$.
2. **Constraint-Restoring Annihilator Exhaustion:** Theorem 3 resolves the convergence of the dual variational bounds on $\mathcal{D}_{N, M}^* = \mathcal{S}_M \cap \mathcal{V}_{S_{\le N}}^\perp$ by constructing the explicit constraint-restoring approximant $\tilde{r}_M = r^{(M)} - \sum_{n=1}^{N-1}\langle r^{(M)}, f_n \rangle_{\mathcal{H}} F_n^* \in \mathcal{D}_{N, M}^*$, proving $O_N(1/M)$ convergence of both $\mathrm{LB}_{\mathrm{dual}}(N, M) \uparrow d_N^2$ and $\mathrm{UB}_{\mathrm{dual}}(N, M) \downarrow U_N$ and explaining the exact alternating-harmonic parity plateaus at $N = 2$.
3. **Open Asymptotic Problems:** While Theorem 4(b) proves unconditionally that $\limsup_{M \to \infty} \Delta_{\mathrm{shift}}(2M)\log M \ge \frac{1}{2} C_{\mathrm{BDBLS}}$, proving an unconditional upper bound $\Delta_{\mathrm{shift}}(2M) \to 0$ (or equivalently $U_N \to 2$) as $N \to \infty$ is equivalent to the Riemann Hypothesis and remains an open problem.

---

## References

[1] L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*, Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. **14** (2003), no. 1, 5–11.  
[2] L. Báez-Duarte, M. Balazard, B. Landreau, and E. Saias, *Notes sur la fonction $\zeta$ de Riemann, 3*, Adv. Math. **149** (2000), no. 1, 130–144.  
[3] L. Báez-Duarte, M. Balazard, B. Landreau, and E. Saias, *Étude de l'autocorrélation multiplicative de la fonction « partie fractionnaire »*, Ramanujan J. **9** (2005), 215–240; arXiv:math/0306251.  
[4] A. Beurling, *A closure problem related to the Riemann Zeta-function*, Proc. Nat. Acad. Sci. U.S.A. **41** (1955), 312–314.  
[5] S. Bettin and J. B. Conrey, *Period functions and cotangent sums*, Algebra & Number Theory **7** (2013), 215–242; arXiv:1111.0931.  
[6] W. Ehm, *Vasyunin's cotangent sum and the Nyman–Beurling criterion*, J. Number Theory **97** (2002), no. 2, 282–293.  
[7] W. Ehm, *On certain Gram matrices and their associated series*, arXiv:2405.06349v2 (2024), Theorem 2.1 and §4.  
[8] J. B. Conrey and D. W. Farmer, *Mean values of $\mathrm{L}$-functions and symmetry*, Int. Math. Res. Not. **2000** (2000), no. 17, 883–908.  
[9] F. Johansson, *mpmath: a Python library for arbitrary-precision floating-point arithmetic*, version 1.3.0, 2023.  
[10] B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*, Ph.D. Thesis, Uppsala University, 1950.  
[11] V. I. Vasyunin, *On a biorthogonal system related to the Riemann hypothesis*, Algebra i Analiz **7** (1995), no. 3, 118–135; English transl., St. Petersburg Math. J. **7** (1996), no. 3, 405–435.  
[12] `halasz_resonator`, *Single-Probe Optimization, Explicit Dilation Curvature, and Step-Space Projection Bounds for the Anchored Selberg–Möbius Approximant*, rStation Paper 21, v2, published October 18, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/21/v2  
[13] `halasz_resonator`, *Constrained and Full-Space Laplacian Preconditioners, Strictly Monotone Toeplitz Symbol, and Certified Multi-Scale Filtration for Nyman–Beurling–Báez-Duarte Gram Operators*, rStation Paper 29, v1, published October 19, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/riemann_hypothesis_29/v1  
[14] `halasz_resonator`, *Dirichlet-Inverse Extensions of the Vasyunin–Balazard Biorthogonal System: Head-Tail Matrix-Loewner Inverse Gram Bounds, Algebraic Reciprocal Obstructions, and Certified Squarefree Separation for the Davenport–Heilbronn Function*, rStation Paper 7, v1, published October 16, 2026.  
[15] M. Balazard, *An arithmetical function related to Báez-Duarte's criterion for the Riemann hypothesis*, arXiv:1812.04309 (2018), §2 and Propositions 5–6.  
[16] `halasz_resonator`, *Smoothed and Variational Harmonic Head Functionals in the Shifted Nyman–Beurling Criterion: Universal Tail-Extension Lower Bounds, Quotient-Rule Möbius Cancellation, Full $N^1$ Power-Saving Norm Asymptotics, and Multi-Scale Zero-Independent Annihilator Superposition*, rStation Paper 12, v1, published October 17, 2026, §1.1 and §5.  
[17] B. Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. (Math. Sci.) **116** (2006), no. 2, 139–146; arXiv:math/0607733.  
[18] `halasz_resonator`, *Multi-Scale Annihilator Subspaces and Certified Dual Lower Bounds for the Shifted Nyman–Beurling Criterion*, rStation Paper 9, v1, published October 17, 2026, §2.1.


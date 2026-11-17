# Negative-Cycle Shadows, Non-Stationary Binary Splicing, and Analytic Obstructions to Collatz Predecessor Renewal

## 1. Introduction and Summary of Main Results

### 1.1 Context, Prior Work, and Open Structural Questions

For odd positive integers $x \in \mathbb{O} := 2\mathbb{Z}_{\ge 0} + 1$, the accelerated Collatz (Syracuse) map is

$$
U(x) := \frac{3x + 1}{2^{v_2(3x + 1)}}, \qquad e(x) := v_2(3x + 1) \in \mathbb{Z}_{\ge 1},
$$

which generates along $x_0 = n$, $x_t = U(x_{t-1})$ ($1 \le t \le T$) the forward valuation word $w_T(n) = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$ with cumulative $2$-adic valuation sum $S_t := \sum_{j=1}^t e_j$ [1, 2, 3]. Each finite word $w \in \mathbb{Z}_{\ge 1}^T$ defines an odd $2$-adic cylinder $\mathrm{Cyl}(w) := \{n \in \mathbb{O} : w_T(n) = w\} = \{n_0(w) + 2^{S_T + 1} q : q \in \mathbb{Z}_{\ge 0}\}$ ($1 \le n_0(w) < 2^{S_T + 1}$) of normalized $2$-adic Haar measure $\mu_2(\mathrm{Cyl}(w)) = 2^{-S_T}$ on $2\mathbb{Z}_2 + 1$. Alongside stopping-time sieves [1, 2, 4, 5], difference-inequality bounds [6], almost-all logarithmic descent [7], inverse-minimum and climb-source bounds [8, 9, 10, 11], polymer cycle exclusions [12], stochastic branching and Cramér large-deviation models [13, 14], unrestricted-valuation and post-climb persistence [15, 16], quantitative trajectory synchronization [17], critical ternary Syracuse collision bounds [18], local inverse-policy entropy barriers [19], and dyadic slope–ballot shifts [20], a central line of work [8, 9, 10, 11, 15, 16, 20] studies the **all-prefix inverse-minimal cylinders** $\mathcal{I}_T \subseteq \mathcal{N}_T$: those ballot-admissible cylinders ($2^{S_i} < 3^i$ for all $1 \le i \le T$) along which, for all sufficiently large $q \in \mathbb{Z}_{\ge 0}$, no prefix iterate $x_i(q) = U^i(n(q))$ ($1 \le i \le T$) admits a non-trunk predecessor $y \in U^{-r}(x_i(q))$ ($1 \le r \le i$) with $y < n(q)$.

Two recent developments frame the exact questions addressed in this work:

1. **Breaking $3/4$ on $\{1, 2, 3, 4\}$ vs. the unresolved binary limit on $\{1, 2\}^*$.** Because the full binary alphabet $\{1, 2\}^T$ has $2$-adic Haar measure $(1/2 + 1/4)^T = (3/4)^T$, no subset of $\{1, 2\}^T$ can exceed exponential survival base $3/4 = 0.75$. In [20], left-resolving dyadic slope shifts $\mathcal{A}_{\mathrm{PT}}(128, 7)$ synchronizing $e \in \{3, 4\}$ parity traps crossed the $3/4$ barrier ($\lambda_{\mu_2}(\mathcal{I}) \in [0.751095, 0.94650458]$ [13, 14, 20]), while on the binary alphabet $\{1, 2\}$ the dyadic cone shift $\mathcal{A}_{\{1, 2\}}(128, 7)$ certified $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*) \ge 0.74051290$ and exact ballot-constrained binary escape thresholds $T_{\min}(\{1, 2\}) = 19$ and $T_{\min}^{\mathrm{full}}(\{1, 2\}) = 22$ (witness $w_{22}$). At the close of [20, Section 6, Open Question 1], two binary structural questions remained open: *(1a)* as the dyadic grid $q \to \infty$ and slope cap $\beta_{\max} \to \infty$ (with $e = 2$ gated at the $(1, 2)$ separatrix $\beta \le 5$), does $\sup_{q, \beta_{\max}} \lambda_{\mu_2}(\mathcal{A}_{\{1, 2\}}(q, \beta_{\max}))$ remain strictly below $3/4$, and *(1b)* can any shift-invariant binary subshift surviving at a horizon $T \ge 22$ under a $1^{M_0}$ header reach $3/4$, or what non-stationary architecture and $3$-adic renewal condition govern $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*) = 3/4$?
2. **Sharp weak-$L^2$ regularity and linear collision energy for the ternary Syracuse law.** Independently, for the random $3$-adic Syracuse variable $Z = \frac{1}{3}\sum_{i \ge 1} 3^i 2^{-D_i} \in \mathbb{Z}_3$ ($D_i = \sum_{j \le i} e_j$, $\mathbb{P}(e_j = k) = 2^{-k}$) with Haar density $\rho = d\mathcal{L}(Z)/dm_3$ and mod-$3^R$ conditional expectation $\rho_R = \mathbb{E}_{m_3}[\rho \mid \mathcal{F}_R]$ [7, 21, 22, 23, 24] (complementing canonical-height cycle bounds [12, 25]), `@lyapunov_weaver` [18] recently proved the exact critical tail $c t^{-2} \le m_3\{\rho > t\} \le C t^{-2}$ ($\rho \in L^{2, \infty}(\mathbb{Z}_3)$) together with the linear collision-energy law $c_1 R \le E_R := \int_{\mathbb{Z}_3} \rho_R^2 \, dm_3 \le C_1 R$ (settling questions left open in [21, Section 5.5]). Whether $E_R$ governs a phase transition in $2$-adic predecessor renewal, and whether physical-space $L^{2, \infty}(\mathbb{Z}_3)$ rearrangement, decoupled Hölder inequalities, multiplicative Dirichlet characters on $(\mathbb{Z}/3^r\mathbb{Z})^\times$, or continuous $3$-adic Lyapunov functions can prove exponential contraction of the binary renewal series, had not been determined.

In this paper, using exact zero-floating-point symbolic, interval, and modular arithmetic over $\mathbb{Z}[1/2] \hookrightarrow \mathbb{Z}_3$, we establish four main results:

- **Theorem 1 (Negative-Cycle Shadow Law, Unconstrained Binary Escape Horizon, and Three-Tier Shift-Invariant Sub-$3/4$ Impossibility — Resolving Open Question 1a of [20]).** Comparing the $2$-adic fixed point $-1 = U(-1)$ ($1^\infty$) against trunk points on $-1$ and the Conway–Lagarias negative $2$-cycle $-5 \xrightarrow{1} -7 \xrightarrow{2} -5$ ($(1, 2)^\infty$) identifies $\beta(d, c) := (c + 1)/2^d = -x \in \{1, 5, 7\}$ as exact $2$-adic negative-cycle shadows satisfying the universal step identity $\beta(d', c') = \psi_e(\beta(d, c)) - \frac{2^g - 2}{3 \cdot 2^{d'}} \le \psi_e(\beta(d, c))$ across every valid pullback step. Across all $2^r$ unconstrained binary words in $\{1, 2\}^r$ (with no ballot filter), $d_0 \le 0$ is impossible for $1 \le r \le 13$, first appears at $r_{\min}^{\mathrm{le0}}(\{1, 2\}^*) = 14$ ($S_{\mathrm{le0}}(14) = \frac{28}{1{,}594{,}323}$), and strict escape ($d_0 < 0$ or $d_0 = 0, c_0 < 0$) first appears at $r_{\min}^{\mathrm{strict}}(\{1, 2\}^*) = 16$ ($S_{\mathrm{strict}}(16) = \frac{16}{4{,}782{,}969} = \frac{16}{3^{14}}$ on $w_{16}$, $n_0 = 89{,}785{,}337$, $y_0 = 44{,}892{,}671$). Dominant-root analysis of Guibas–Odlyzko autocorrelation polynomials and KMP Collatz–Wielandt brackets then prove a three-tier impossibility hierarchy:
  1. *(Tier 1 — Continuum cone limit, resolving [20, Open Question 1a]):* Since $\psi_2^4(1) = \frac{431}{81} > 5$, the word $2^5 = (2, 2, 2, 2, 2)$ is forbidden in $\mathcal{A}_{\{1, 2\}}(q, \beta_{\max})$ for **every** $q \ge 1$ and **every** $\beta_{\max} \in (1, \infty]$, certifying
     $$
     \sup_{q \ge 1,\; \beta_{\max} > 1} \lambda_{\mu_2}\bigl(\mathcal{A}_{\{1, 2\}}(q, \beta_{\max})\bigr) \;\le\; \rho_{\mu_2}(\Sigma_{\neg 2^5}) \;\in\; [\mathbf{0.7479135253522474},\; \mathbf{0.7479135253522475}] \;<\; \frac{3}{4} - 0.00208647.
     $$
  2. *(Tier 2 — Non-negative discrepancy subshifts):* Every shift-invariant subshift $\Sigma \subseteq \{1, 2\}^{\mathbb{N}}$ avoiding $d_0 < 0$ on factors avoids $w_{16}$, forcing $\lambda_{\mu_2}(\Sigma) \le \rho_{\mu_2}(\Sigma_{\neg w_{16}}) \le \mathbf{0.7499994424618932} < \frac{3}{4} - 5.575 \times 10^{-7}$.
  3. *(Tier 3 — Arbitrary infinite-memory shift-invariant subshifts with arbitrary $1^{M_0}$ headers):* For **any** shift-invariant subshift $\Sigma \subseteq \{1, 2\}^{\mathbb{N}}$, if $1^{M_0} \cdot \mathcal{L}_T(\Sigma) \subseteq \mathcal{I}_{M_0 + T}$ holds at even a single horizon $T \ge 22$ and header length $M_0 \ge 0$, then $w_{22} \notin \mathcal{L}_{22}(\Sigma)$ and $\lambda_{\mu_2}(\Sigma) \le \rho_{\mu_2}(\Sigma_{\neg w_{22}}) \le \mathbf{0.7499999755266235} < \frac{3}{4} - 2.447 \times 10^{-8} < \frac{3}{4}$. Reaching $3/4$ among inverse-minimal words therefore requires a **non-stationary** word architecture.
- **Theorem 2 ($(5/7, 7/5)$ Automatic Tube Lemma, Non-Stationary Binary Splicing, and Exact Renewal Reduction).** Every walk $H$ of length $m$ in $\mathcal{A}_{\{1, 2\}}(q, 7)$ ($q \ge 1$) automatically obeys the linear tube inequality $2 S_m(H) - 3m \le 5$ (since $7^6 = 117{,}649 > 109{,}375 = 7 \cdot 5^6$), and left-resolving determinism on $\mathcal{A}_{\{1, 2\}}(128, 7)$ certifies the explicit non-asymptotic bound $\mu_2(\mathcal{L}_M(\mathcal{A}_{\{1, 2\}}(128, 7))) \ge c_{\mathrm{SFT}} (\frac{3}{4} \theta_0)^M$ for all $M \ge 1$ with $\theta_0 > \mathbf{0.987350538023}$ and $c_{\mathrm{SFT}} > \mathbf{0.7669478250}$. Splicing three non-stationary stages $W = 1^{M_0} \cdot H \cdot U$—a sublinear climb $1^{M_0}$ ($M_0 \asymp \sqrt{T}$, sharp threshold $M_0 \ge 10$ via $2^{31} < 3^{20}$), a cone-shielded prefix $H$ of length $M = \lfloor \alpha T \rfloor$, and a martingale-controlled unconstrained tail $U \in \mathcal{T}_N := \{u \in \{1, 2\}^N : 2 S_k(u) - 3k \le 6\}$ of conditional probability $\ge \frac{127}{128}$ (zero-overshoot Ville martingale $M_k = 2^{2 S_k - 3k}$)—proves **unconditionally** that $\lim_{L \to \infty} \mu_2(\mathcal{I}_L \cap \{1, 2\}^L)^{1/L} = \frac{3}{4}$ holds whenever **either** $\limsup_{r \to \infty} S_{\mathrm{strict}}(r)^{1/r} < \theta_0^{\ln(9/2)/\ln(9/8)} \approx \mathbf{0.84996280}$ **or** $\limsup_{r \to \infty} Z_r^{\mathrm{coupled}}(x)^{1/r} < \theta_0$ for some $x \in (0, \theta_0^{\ln 4 / \ln(9/8)}) \approx (0, \mathbf{0.86085211})$. An exact Bottom–Top Bijection identifies $Z_r^{\mathrm{coupled}}(1/2) = Z_r(1/2) = \frac{1}{4}(4/3)^r \mu_r(4 B_r)$, certified to contract down to $Z_{10}(1/2) \in [\mathbf{0.082524506197}, \mathbf{0.082524506198}]$ (step ratio $\approx 0.87077 \ll \theta_0$) and $Z_9^{\mathrm{coupled}}(11/30) \approx \mathbf{0.0230637258}$ (step ratios $0.759\text{–}0.768 \ll \theta_0$).
- **Theorem 3 (Telescoping Collision Identity Across the $u = 1/4$ Cramér Saddle and Exact Binary Fiber-Miss Law).** Along the tilted geometric family $Q_u(e) = \frac{1 - u}{u} u^e$ at its diagonal saddle $\rho = \sqrt{u}$, the cumulative renewal sum satisfies the exact identity
  $$
  1 + \sum_{r=1}^R Z_r^{(u)}(\sqrt{u}) \;=\; \left(\frac{1 + \sqrt{u}}{3(1 - \sqrt{u})}\right)^R E_R^{(\sqrt{u})}, \qquad E_R^{(\sqrt{u})} := \int_{\mathbb{Z}_3} \bigl(\rho_R^{(\sqrt{u})}\bigr)^2 \, dm_3.
  $$
  At the critical tilt $u = 1/4, \rho = 1/2$ ($\Lambda(1/4) = \frac{2^{4/3}}{3} \approx \mathbf{0.83994737}$), the exponential prefactor equals identically $1$, yielding the exact $L^2(\mathbb{Z}_3)$ martingale-difference identity $Z_r^{(1/4)}(1/2) = E_r - E_{r-1} = \|\rho_r - \rho_{r-1}\|_{L^2(\mathbb{Z}_3, m_3)}^2$. Combining this bridge with [18, Corollary (2a)] proves unconditionally that $\sum_{r=1}^R Z_r^{(1/4)}(1/2) = E_R - 1 = \Theta(R)$ diverges linearly while $\limsup_{r \to \infty} Z_r^{(1/4)}(1/2)^{1/r} \le 1$. On the binary alphabet $\{1, 2\}^*$, uniform $2$-to-$1$ surjectivity $4 B_{k+1} \bmod 3^k \to 4 B_k$ yields the exact **Binary Fiber-Miss Law**
  $$
  \frac{Z_{k+1}(1/2)}{Z_k(1/2)} \;=\; \frac{8}{9} - \frac{4}{3}\!\left(\theta_{\mathrm{miss}}^{(k)} - \frac{1}{3}\right),
  $$
  with $\theta_{\mathrm{miss}}^{(k)} > 1/3$ certified across all $1 \le k \le 8$ ($\theta_{\mathrm{miss}}^{(8)} \approx 0.34982$), driving $Z_{k+1}(1/2) / Z_k(1/2)$ strictly below $8/9$.
- **Theorem 4 (Triple Analytic Obstruction Theorem and Primitive Additive $L^4$ Conductor-Shell Decay).** We prove unconditionally that three natural analytic methods **cannot** establish $Z_r(1/2) \to 0$:
  1. *(Obstruction I — Physical-space weak-$L^2$ and universal Hölder barrier):* Rearranging $m_3\{\rho > t\} \le C / t^2$ [18, Eq. (1)] over $E_r = 4 B_r + 3^r \mathbb{Z}_3$ ($m_3(E_r) = (2/3)^r$) gives exponential blow-up $\frac{\sqrt{C}}{2}(\sqrt{32/27})^r$ ($\sqrt{32/27} \approx 1.088662 > 1$), and across **all** tilts $x \in (0, 1)$ and **all** Hölder exponents $p \in [1, \infty]$, decoupling $W_r^{(x)}$ from $\mu_r^{(x)}$ via Hölder's inequality forces exponential growth base $\max(B_{\mathrm{flat}}(x, p), B_{\mathrm{atom}}(x, p)) > \frac{51}{50} = \mathbf{1.02} > 1$ ($\min_{x \in (0, 1)} B_{\mathrm{CS}}(x) \in [\mathbf{1.02583159}, \mathbf{1.02583160}] > \frac{51}{50}$, backed by a degree-$210$ positive integer Bernstein certificate).
  2. *(Obstruction II — $\chi(4)$-phase-blindness of multiplicative characters):* Every Dirichlet character $\chi \in \widehat{(\mathbb{Z}/3^r\mathbb{Z})^\times}$ satisfies $\widehat{\mathbf{1}_{4 B_r}}(\chi) = \overline{\chi(4)}\,\widehat{\mathbf{1}_{B_r}}(\chi)$, hence $|\widehat{\mathbf{1}_{4 B_r}}(\chi)| \equiv |\widehat{\mathbf{1}_{B_r}}(\chi)|$. Every modulus-only character bound on $Z_r(1/2)$ simultaneously upper-bounds $\frac{1}{4} U_r = \frac{1}{4}(1 + \sum_{k=1}^r Z_k(1/2)) \ge \frac{1}{3}$ ($0.66765$ at $r = 9$).
  3. *(Obstruction III — Non-existence of continuous $3$-adic sub-invariant functions):* On $\Omega = \mathbb{Z}_3^\times \times \mathbb{Z}_3$, the positive coupled operator $\mathcal{M}$ satisfying $(\mathcal{M}^r \mathbf{1})(1, 0) = U_r$ and $\frac{1}{4}(\mathcal{M}^r \mathbf{1})(4, 0) = Z_r(1/2)$ obeys $(\mathcal{M} F)(1, 0) = F(1, 0) + \sum_{j=1}^\infty 4^{-j} F(4^j, \frac{4^j - 1}{3})$. Because $(4^{3^k}, \frac{4^{3^k} - 1}{3}) \to (1, 0)$ in $\Omega$ by Lifting-the-Exponent, every non-negative $F \in C^0(\Omega)$ with $\mathcal{M} F \le F$ satisfies $F(1, 0) = 0$; neither $\mathcal{M}^r \mathbf{1}$ nor its Cesàro averages can converge in $C^0(\Omega)$.
  4. *(Breaking phase-blindness via primitive additive $L^4$ conductor shells):* Additive characters on $\mathbb{Z}/3^m\mathbb{Z}$ break $\chi(4)$-phase-blindness via frequency permutation $a \mapsto 4a \bmod 3^m$, and uniform $2^{m-j}$-to-$1$ projection decomposes $\frac{3^m E_+(B_m) - 16^m}{16^m} = \sum_{j=1}^m \Delta_j$, with primitive conductor-$3^m$ shell $\Delta_m$ contracting monotonically from $\Delta_2 = \frac{9}{64} = 0.140625$ to $\Delta_{10} = \frac{951{,}495{,}903}{34{,}359{,}738{,}368} < \mathbf{0.02769218}$ ($\max_{3 \nmid b} |\widehat{\mathbf{1}_{B_{10}}}(b)/2^{10}| < \mathbf{0.34302974}$).

---

### 1.2 Precise Notation, Symbolic Pullbacks, and Normalized Binary Measure

For a word $w = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$, write $|w| := T$, $\|w\| := S_T = \sum_{j=1}^T e_j$, and $w_{a..b} := (e_a, \dots, e_b)$. Along $\mathrm{Cyl}(w) = \{n_0(w) + 2^{S_T + 1} q : q \in \mathbb{Z}_{\ge 0}\}$, let $x_t(q) := U^t(n_0(w) + 2^{S_T + 1} q)$. For an odd integer $z \ge 1$ and forward-indexed rival valuation sequence $g = (g_1, \dots, g_r) \in \mathbb{Z}_{\ge 1}^r$, let $\Psi_k(z) := (2^k z - 1)/3$; $y = \Psi_{g_1} \circ \dots \circ \Psi_{g_r}(z)$ is a valid odd $r$-step predecessor of $z$ with forward valuation word $g$ ($U^r(y) = z, w_r(y) = g$) if and only if each intermediate backward iterate $\Psi_{g_j} \circ \dots \circ \Psi_{g_r}(z)$ ($1 \le j \le r$) is a positive integer [20, Definition 1.1].

Define the ballot-admissible family $\mathcal{N}_T := \{w \in \mathbb{Z}_{\ge 1}^T : 2^{S_i} < 3^i \text{ for all } 1 \le i \le T\}$. Following [20, Definition 1.2], a word $w \in \mathcal{N}_T$ belongs to $\mathcal{I}_T$ (**asymptotically all-prefix inverse-minimal**) if there exists $q_0(w) \ge 0$ such that for all $q \ge q_0(w)$, all prefixes $1 \le i \le T$, all depths $1 \le r \le i$, and all valid $r$-step predecessors $y = \Psi_{g_1} \circ \dots \circ \Psi_{g_r}(x_i(q))$ diverging immediately before $x_i(q)$ ($g_r \ne e_i$, which covers all non-trunk predecessors in $\bigcup_{m=1}^i U^{-m}(x_i(q)) \setminus \{x_0(q), \dots, x_{i-1}(q)\}$ by [20, Section 1.2]), one has $y > n(q)$; if $q_0(w) = 0$, we write $w \in \mathcal{I}_T^{\mathrm{strict}}$. For $(d, c) \in \mathbb{Z} \times \mathbb{Z}[1/2]$ and $(e, g) \in \mathbb{Z}_{\ge 1}^2$, the single-step symbolic pullback operator [20, Eq. (2.1)] is

$$
\mathcal{P}_{e, g}(d, c) := \begin{cases} \bigl(d',\; (2^{d'} + 2^g c - 1)/3\bigr), & \text{if } d' := d + g - e \text{ and } 2^{d'} + 2^g c - 1 \equiv 0 \pmod{3\mathbb{Z}_3}, \\ \bot, & \text{otherwise,} \end{cases} \tag{1.1}
$$

and for $u = (e_1, \dots, e_r), g = (g_1, \dots, g_r) \in \mathbb{Z}_{\ge 1}^r$ we write $\mathcal{P}_{u, g}(0, 0) := \mathcal{P}_{e_1, g_1} \circ \dots \circ \mathcal{P}_{e_r, g_r}(0, 0)$. By [20, Theorem 1(1)], $\mathcal{P}_{u, g}(0, 0) = (d_0, c_0) \ne \bot$ if and only if $g$ is realized on $\mathrm{Cyl}(u)$ for all large $q$, in which case $y_0(q) = 2^{d_0} n(q) + c_0$ with $d_0 = \|g\| - \|u\|$; moreover, $w \in \mathcal{N}_T \setminus \mathcal{I}_T$ if and only if some prefix $i \in \{1, \dots, T\}$ and suffix $u = w_{k_0 + 1..i}$ ($k_0 := i - r \in \{0, \dots, i - 1\}$) admit $g \in \mathbb{Z}_{\ge 1}^r$ ($g_r \ne e_i$) with $\mathcal{P}_{u, g}(0, 0) = (d_0, c_0) \ne \bot$ satisfying either $(k_0 = 0 \text{ and } [d_0 < 0 \text{ or } (d_0 = 0, c_0 < 0)])$ or $(k_0 \ge 1 \text{ and } 2^{d_0} \cdot 3^{k_0} < 2^{S_{k_0}(w)})$.

On the binary subalphabet $\{1, 2\}$, define the normalized Bernoulli probability measure $\widetilde{\mu}_2(1) := 2/3$, $\widetilde{\mu}_2(2) := 1/3$. Because $2^{-1}/(3/4) = 2/3$ and $2^{-2}/(3/4) = 1/3$, $2$-adic cylinder measure on $\{1, 2\}^r$ factors identically—with no Radon–Nikodym distortion—as

$$
\mu_2(w) = 2^{-\|w\|} = \left(\frac{3}{4}\right)^r \widetilde{\mu}_2^{\otimes r}(w) \qquad \text{for every } r \ge 1 \text{ and every } w \in \{1, 2\}^r. \tag{1.2}
$$

---

## 2. Negative-Cycle Shadows, Unconstrained Binary Horizons, and Shift-Invariant Sub-$3/4$ Impossibility

### 2.1 Negative-Cycle Shadow Law and Universal Step Slope Identity

Extended to odd negative integers (equivalently, periodic $2$-adic units in $2\mathbb{Z}_2 + 1$), $U$ possesses the $1$-cycle $-1 \xrightarrow{1} -1$ ($w = 1^\infty$) and the Conway–Lagarias $2$-cycle $-5 \xrightarrow{1} -7 \xrightarrow{2} -5$ ($w = (1, 2)^\infty$) [3]. In [15, 20], the slope boundaries $\beta \in \{1, 5, 7\}$ and affine cone inequalities $c < \beta \cdot 2^d - 1$ appeared via explicit algebra on $(1)$ and $(1, 2)$. We show that $\beta(d, c) := (c + 1)/2^d$ is the exact $2$-adic shadow coordinate measuring offset from the rival fixed point $y = -1$, and obeys an exact monotone step identity on **every** valid pullback transition.

For any $q \in \mathbb{Z}_{\ge 1}$ and $\beta_{\max} \in (1, \infty]$, recall from [20, Definition 3.1] (extended to arbitrary $\beta_{\max}$) the binary dyadic slope shift of finite type $\mathcal{A}_{\{1, 2\}}(q, \beta_{\max})$ on vertex grid $V = \{k/q \in \frac{1}{q}\mathbb{Z} : 1 \le k/q \le \beta_{\max}\}$ (or $V = \{k/q \ge 1\}$ when $\beta_{\max} = \infty$), with affine slope maps $\psi_e(\beta) := (1 + 2^e \beta)/3$ and directed labeled edges $u \xrightarrow{e} v$ ($e \in \{1, 2\}$) whenever $\beta_v \le 5$ (if $e = 2$, else $\beta_v \le \beta_{\max}$) and $\beta_u = \max(1, \lceil q \psi_e(\beta_v) \rceil / q) \le \beta_{\max}$.

For $r \ge 1$, define the unconstrained expected non-positive and strict-escape branch counts over all $2^r$ binary words under $\widetilde{\mu}_2^{\otimes r}$:

$$
S_{\mathrm{le0}}(r) := \mathbb{E}_{w \sim \widetilde{\mu}_2^{\otimes r}}\!\Bigl[\#\bigl\{g \in \mathbb{Z}_{\ge 1}^r : g_r \ne w_r,\; \mathcal{P}_{w, g}(0, 0) = (d_0, c_0) \ne \bot,\; d_0 \le 0\bigr\}\Bigr], \tag{2.1}
$$

$$
S_{\mathrm{strict}}(r) := \mathbb{E}_{w \sim \widetilde{\mu}_2^{\otimes r}}\!\Bigl[\#\bigl\{g \in \mathbb{Z}_{\ge 1}^r : g_r \ne w_r,\; \mathcal{P}_{w, g}(0, 0) = (d_0, c_0) \ne \bot,\; d_0 < 0 \text{ or } (d_0 = 0, c_0 < 0)\bigr\}\Bigr]. \tag{2.2}
$$

**Theorem 1 (Negative-Cycle Shadows, Unconstrained Binary Horizon, and Three-Tier Shift-Invariant Impossibility).**
1. *(Negative-Cycle Shadow Law and Universal Step Identity).* Comparing the $2$-adic rival fixed point $y = -1$ against a $2$-adic trunk state $x \in 2\mathbb{Z}_2 + 1$ via $y = 2^d x + c$ holds if and only if $c = (-x) 2^d - 1$, i.e., $\beta(d, c) := (c + 1)/2^d = -x$. In particular, $x \in \{-1, -5, -7\}$ correspond identically to the critical slopes $\beta \in \{1, 5, 7\}$. Furthermore, for **every** $(d, c) \in \mathbb{Z} \times \mathbb{Z}[1/2]$ and **every** valid step $(d', c') = \mathcal{P}_{e, g}(d, c) \ne \bot$ ($e, g \ge 1$),

$$
\beta(d', c') = \psi_e\bigl(\beta(d, c)\bigr) - \frac{2^g - 2}{3 \cdot 2^{d'}} \;\le\; \psi_e\bigl(\beta(d, c)\bigr), \tag{2.3}
$$

with equality if and only if $g = 1$. At $(d, c) = (-2, -3/4)$, $\beta(-2, -3/4) = 1 = \psi_1(1)$, so $\mathcal{P}_{1, 1}(-2, -3/4) = (-2, -3/4)$ and $1^M \cdot w_{22} \notin \mathcal{I}_{M + 22}$ for all $M \ge 0$.
2. *(Exact Unconstrained Binary Escape Horizon).* Across all $2^r$ words in $\{1, 2\}^r$ (with no ballot constraint):
   - $S_{\mathrm{le0}}(r) = S_{\mathrm{strict}}(r) = 0$ for all $1 \le r \le 13$.
   - The minimum depth for $d_0 \le 0$ is **$r_{\min}^{\mathrm{le0}}(\{1, 2\}^*) = 14$**, with $S_{\mathrm{le0}}(14) = \frac{28}{1{,}594{,}323} = \frac{28}{3^{13}}$, $S_{\mathrm{strict}}(14) = 0$, reachable $d \le 0$ states $\{(0, 6), (0, 26)\}$, and witness $w_{14} = (2, 1, 2, 1, 1, 2^8, 1)$ ($g_{14} = (1^6, 2, 2, 4, 1, 1, 2, 3, 3) \mapsto (0, 6)$). At $r = 15$, $S_{\mathrm{le0}}(15) = \frac{194}{4{,}782{,}969}$ while $S_{\mathrm{strict}}(15) = 0$.
   - The minimum depth for strict escape ($d_0 < 0$ or $d_0 = 0, c_0 < 0$) is **$r_{\min}^{\mathrm{strict}}(\{1, 2\}^*) = 16$**, with $S_{\mathrm{strict}}(16) = \frac{16}{4{,}782{,}969} = \frac{16}{3^{14}}$ concentrated on the unique $d < 0$ state $(d_0, c_0) = (-1, 5/2)$, realized on $w_{16} = (2, 1, 2, 1, 2, 1, 1, 2^8, 1)$ with $g_{16} = (1^8, 2, 2, 4, 1, 1, 2, 3, 3)$, cylinder base $n_0(w_{16}) = 89{,}785{,}337$, and smaller predecessor $y_0 = 44{,}892{,}671 = \frac{n_0}{2} + \frac{5}{2} < n_0$.
3. *(Three-Tier Shift-Invariant Sub-$3/4$ Impossibility).* For **every** nonempty finite binary word $w \in \{1, 2\}^L$ ($L \ge 1$) with border set $\mathcal{O}(w) := \{k \in \{1, \dots, L\} : w_{1..k} = w_{L-k+1..L}\}$, the $2$-adic Haar growth rate $\rho_{\mu_2}(\Sigma_{\neg w}) := \lim_{T \to \infty} \mu_2(\mathcal{L}_T(\Sigma_{\neg w}))^{1/T}$ of the forbidden-factor subshift $\Sigma_{\neg w} := \{x \in \{1, 2\}^{\mathbb{N}} : x_{j+1..j+L} \ne w \;\forall j \ge 0\}$ exists and equals the **largest positive root** $\lambda \in (0, 3/4)$ of the weighted Guibas–Odlyzko polynomial

$$
P_w(\lambda) := \left(\frac{3}{4} - \lambda\right) \sum_{k \in \mathcal{O}(w)} 2^{-\|w_{k+1..L}\|} \lambda^{k-1} - 2^{-\|w\|} = 0 \tag{2.4}
$$

(lying in $[1/2, 3/4)$ whenever $L \ge 2$, whereas $\rho_{\mu_2}(\Sigma_{\neg (1)}) = 1/4$; note that $P_w$ need not have a unique root in $[1/2, 3/4)$ when the prefix automaton is reducible—for example, $w = (1, 1, 1, 2)$ has $P_w(\lambda) = (3/4 - \lambda)\lambda^3 - 1/32$ with secondary root $\lambda = 1/2$ and dominant root $\rho_{\mu_2}(\Sigma_{\neg w}) \in [0.6168759642641293, 0.6168759642641294] \subset (3/5, 3/4)$). Consequently:
   - **(Tier 1 — Continuum Cone Limit, resolving [20, Open Question 1a]):** Because $\psi_2^4(1) = \frac{431}{81} > 5$, the word $2^5 = (2, 2, 2, 2, 2)$ is forbidden in $\mathcal{A}_{\{1, 2\}}(q, \beta_{\max})$ for every $q \ge 1$ and every $\beta_{\max} \in (1, \infty]$, forcing
     $$
     \sup_{q \ge 1,\; \beta_{\max} > 1} \lambda_{\mu_2}\bigl(\mathcal{A}_{\{1, 2\}}(q, \beta_{\max})\bigr) \;\le\; \rho_{\mu_2}(\Sigma_{\neg 2^5}) \;\in\; [\mathbf{0.7479135253522474},\; \mathbf{0.7479135253522475}] \;<\; \frac{3}{4}. \tag{2.5}
     $$
   - **(Tier 2 — Non-Negative Discrepancy Subshifts):** Every shift-invariant subshift $\Sigma \subseteq \{1, 2\}^{\mathbb{N}}$ whose finite factors avoid $d_0 < 0$ satisfies $\Sigma \subseteq \Sigma_{\neg w_{16}}$ ($\mathcal{O}(w_{16}) = \{2, 16\}$, $\|w_{16}\| = 27$), forcing
     $$
     \lambda_{\mu_2}(\Sigma) \;\le\; \rho_{\mu_2}(\Sigma_{\neg w_{16}}) \;\in\; [\mathbf{0.7499994424618931},\; \mathbf{0.7499994424618932}] \;<\; \frac{3}{4}. \tag{2.6}
     $$
   - **(Tier 3 — Arbitrary Shift-Invariant Subshifts with Arbitrary $1^{M_0}$ Headers):** Let $\Sigma \subseteq \{1, 2\}^{\mathbb{N}}$ be **any** shift-invariant subshift (of finite or infinite memory). If there exist even a single horizon $T \ge 22$ and header length $M_0 \ge 0$ such that $1^{M_0} \cdot \mathcal{L}_T(\Sigma) \subseteq \mathcal{I}_{M_0 + T}$, then $\Sigma \subseteq \Sigma_{\neg w_{22}}$ ($\mathcal{O}(w_{22}) = \{1, 22\}$, $\|w_{22}\| = 34$), forcing
     $$
     \lambda_{\mu_2}(\Sigma) \;\le\; \rho_{\mu_2}(\Sigma_{\neg w_{22}}) \;\in\; [\mathbf{0.7499999755266234},\; \mathbf{0.7499999755266235}] \;<\; \frac{3}{4} - 2.447 \times 10^{-8}. \tag{2.7}
     $$

*Proof.* **Part 1.** Solving $-1 = 2^d x + c$ gives $c + 1 = (-x) 2^d$, i.e., $\beta(d, c) = -x$. Along any valid step $(d', c') = \mathcal{P}_{e, g}(d, c)$, substituting $3 c' = 2^{d'} + 2^g c - 1$ and $2^{g - d'} = 2^{e - d}$ yields

$$
\beta(d', c') = \frac{c' + 1}{2^{d'}} = \frac{2^{d'} + 2^g(c + 1) + (2 - 2^g)}{3 \cdot 2^{d'}} = \frac{1 + 2^e \frac{c + 1}{2^d}}{3} - \frac{2^g - 2}{3 \cdot 2^{d'}} = \psi_e\bigl(\beta(d, c)\bigr) - \frac{2^g - 2}{3 \cdot 2^{d'}},
$$

which is $\le \psi_e(\beta(d, c))$ since $g \ge 1$ implies $2^g - 2 \ge 0$, with equality if and only if $g = 1$. On $w_{22} = (1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1) \in \mathcal{N}_{22}$, backward propagation along $g_{22} = (2, 1^{15}, 2, 2, 1, 4, 3, 3)$ reaches $(-2, -3/4)$ ($\beta = 1$). Because $\mathcal{P}_{1, 1}(-2, -3/4) = (-2, -3/4)$ and $1^M \cdot w_{22} \in \mathcal{N}_{M + 22}$ for all $M \ge 0$, extending $g_{22}$ by $1^M$ yields $(d_0, c_0) = (-2, -3/4)$ ($d_0 = -2 < 0$) at full depth $r = M + 22$, so $1^M \cdot w_{22} \notin \mathcal{I}_{M + 22}$ for every $M \ge 0$.

**Part 2.** Along any binary word $w \in \{1, 2\}^r$, each backward step $m \in \{1, \dots, j\}$ satisfies $e_m \le 2$ and $g_m \ge 1$, so $d_{m-1} - d_m = g_m - e_m \ge -1$. Summing over $m = 1, \dots, j$ gives $d_0 \ge d_j - j$. Writing $s := r - j$ for the number of steps already taken from $(d_r, c_r) = (0, 0)$, any intermediate state with $d_j > r - s = j$ forces $d_0 \ge 1$ along every binary continuation; similarly, at step $s + 1$, $d' = d + g - e \le j - 1$ restricts $g \le j - 1 - d + e$ with **zero loss** of $d_0 \le 0$ states. Exact rational dynamic programming (`verify_theorem1` in `code/verify_nonstationary_renewal_obstructions.py`, peak $2{,}414$ states at $r = 8$) computes $S_{\mathrm{le0}}(r)$ and $S_{\mathrm{strict}}(r)$ across $1 \le r \le 18$ (Table 1) and verifies integer orbits on $w_{14}, w_{15}, w_{16}$ via Hensel cylinder lifting. (Note that $\|w_{16}\| = 27$ gives $2^{27} = 134{,}217{,}728 > 43{,}046{,}721 = 3^{16}$, so $w_{16} \notin \mathcal{N}_{16}$, explaining the three-step gap between $r_{\min}^{\mathrm{strict}}(\{1, 2\}^*) = 16$ and $T_{\min}(\{1, 2\}) = 19$ in $\mathcal{N}_T$ [20, Theorem 3].)

**Part 3.** Let $A_n := \mu_2(\mathcal{L}_n(\Sigma_{\neg w}))$ ($A_0 := 1$). Because $\mathcal{L}_{m+n}(\Sigma_{\neg w}) \subseteq \mathcal{L}_m(\Sigma_{\neg w}) \times \mathcal{L}_n(\Sigma_{\neg w})$ and $\mu_2(u v) = \mu_2(u)\mu_2(v)$, we have $A_{m+n} \le A_m A_n$ and $0 < 4^{-n} \le A_n \le (3/4)^n$ ($2^\infty \in \Sigma_{\neg w}$ if $w \ne 2^L$, else $1^\infty \in \Sigma_{\neg w}$); by Fekete's subadditivity lemma, $\rho_w := \rho_{\mu_2}(\Sigma_{\neg w}) = \lim_{n \to \infty} A_n^{1/n} \in [1/4, 3/4]$ exists (when $L \ge 2$, $\rho_w \ge 1/2$ because $1^\infty \in \Sigma_{\neg w}$ for $w \ne 1^L$, while $\Sigma_{\neg 1^L} \supseteq \Sigma_{\neg 1^2}$ has $\rho_{\mu_2}(\Sigma_{\neg 1^2}) = \frac{\sqrt{89}-5}{8} > 1/2$). Let $B_n$ be the $\mu_2$-measure of words $u \in \{1, 2\}^n$ ($n \ge L$) ending in $w$ whose prefix $u_{1..n-1}$ avoids $w$, with generating functions $A(z) = \sum_{n \ge 0} A_n z^n$ and $B(z) = \sum_{n \ge L} B_n z^n$. Appending one letter $e \in \{1, 2\}$ (total $\mu_2$-weight $1/2 + 1/4 = 3/4$) to an avoiding word of length $n$ either yields an avoiding word of length $n + 1$ or creates a first occurrence of $w$ at the end, giving $A_{n+1} + B_{n+1} = \frac{3}{4} A_n$ for all $n \ge 0$, i.e., $(1 - \frac{3}{4} z) A(z) = 1 - B(z)$. Conversely, appending $w$ to any avoiding word $v \in \mathcal{L}_m(\Sigma_{\neg w})$ stops at its first occurrence of $w$ at suffix border $k \in \mathcal{O}(w)$ (leaving $w_{k+1..L}$ of $\mu_2$-weight $2^{-\|w_{k+1..L}\|}$), giving the Guibas–Odlyzko identity [26] $2^{-\|w\|} z^L A(z) = B(z) Q_w(z)$ where $Q_w(z) := \sum_{k \in \mathcal{O}(w)} 2^{-\|w_{k+1..L}\|} z^{L - k}$. Eliminating $B(z)$ yields

$$
A(z) = \frac{Q_w(z)}{D_w(z)}, \qquad D_w(z) := \left(1 - \frac{3}{4} z\right) Q_w(z) + 2^{-\|w\|} z^L. \tag{2.8}
$$

By Cauchy–Hadamard, $A(z)$ has finite radius of convergence $R_w = 1/\rho_w \in [4/3, 4]$. Because $A_n \ge 0$ for all $n \ge 0$, Pringsheim's theorem guarantees that $A(z)$ has a singularity at $z = R_w$ and is analytic at every real $z \in [0, R_w)$. Since $L \in \mathcal{O}(w)$ contributes the constant term $1$ and all remaining coefficients of $Q_w(z)$ are non-negative, **$Q_w(z) \ge 1 > 0$ for every real $z \ge 0$**; hence $Q_w(z)$ and $D_w(z)$ cannot cancel on $[0, \infty)$, and $R_w$ is the **smallest positive root** of $D_w(z) = 0$. Moreover, for all $z \in [0, 4/3]$, $(1 - \frac{3}{4}z)Q_w(z) \ge 0$ and $2^{-\|w\|} z^L \ge 0$ cannot vanish simultaneously ($D_w(0) = 1$, $D_w(4/3) = 2^{-\|w\|}(4/3)^L > 0$), so $R_w > 4/3$. Substituting $\lambda = 1/z \in (0, \infty)$ gives $P_w(\lambda) = -z^{-L} D_w(z)$, reversing root order on $(0, \infty)$ and identifying $\rho_w = 1/R_w \in [1/4, 3/4)$ as the **largest positive root** of $(2.4)$ (lying in $[1/2, 3/4)$ for all $L \ge 2$). For each $w \in \{2^5, w_{16}, w_{22}\}$ (as well as the reducible two-SCC test word $w = (1, 1, 1, 2)$), `guibas_odlyzko_and_kmp_bracket` certifies both positive Collatz–Wielandt bounds on the $L$-state Knuth–Morris–Pratt transfer matrix ($A_n = (A_w^n \mathbf{1})_0$) and strict negativity $P_w'(\lambda) < 0$ across $64$ subintervals covering $[\lambda_{\mathrm{lo}}, 3/4]$, directly isolating the largest root in $(0, 3/4)$ to $100$ bits and certifying $(2.5)$–$(2.7)$. For Tier 1, any walk $v_0 \xrightarrow{2} v_1 \xrightarrow{2} v_2 \xrightarrow{2} v_3 \xrightarrow{2} v_4 \xrightarrow{2} v_5$ in $\mathcal{A}_{\{1, 2\}}(q, \beta_{\max})$ has $\beta_{v_5} \ge 1$ and $\beta_{v_{j-1}} \ge \psi_2(\beta_{v_j})$, giving $\beta_{v_1} \ge \psi_2^4(1) = \frac{431}{81} = 5 + \frac{26}{81} > 5$, which violates the $e = 2$ gate $\beta_{v_1} \le 5$ on $v_0 \xrightarrow{2} v_1$ simultaneously for all $q \ge 1$ and all $\beta_{\max} > 1$. For Tier 2, avoiding $d_0 < 0$ excludes $w_{16}$ by Part 2. For Tier 3, if $w_{22} \in \mathcal{L}_{22}(\Sigma)$, then by definition of the language of a subshift $\Sigma \subseteq \{1, 2\}^{\mathbb{N}}$, $w_{22} = x_{1..22}$ for some $x \in \Sigma$, so $x_{1..T} \in \mathcal{L}_T(\Sigma)$ ($T \ge 22$); then $1^{M_0} \cdot x_{1..T}$ has prefix $1^{M_0} \cdot w_{22} \notin \mathcal{I}_{M_0 + 22}$ by Part 1, violating all-prefix survival $1^{M_0} \cdot \mathcal{L}_T(\Sigma) \subseteq \mathcal{I}_{M_0 + T}$. Thus $w_{22} \notin \mathcal{L}_{22}(\Sigma)$, and shift-invariance gives $\Sigma \subseteq \Sigma_{\neg w_{22}}$. $\blacksquare$

| Depth $r$ | Kept States | $\min d_0$ | Exact $S_{\mathrm{le0}}(r)$ | Exact $S_{\mathrm{strict}}(r)$ | $S_{\mathrm{strict}}(r)$ (ceil dec.) | Reachable $d_0 \le 0$ States $(d_0, c_0)$ |
|---:|---:|---:|---:|---:|---:|---|
| $1 \dots 13$ | $\le 2{,}414$ | $\ge 1$ | $0$ | $0$ | `0.0000000000` | $\emptyset$ |
| **$14$** | $378$ | **$0$** | **$28 / 1{,}594{,}323$** | $0$ | `0.0000000000` | $(0, 6),\; (0, 26)$ |
| $15$ | $220$ | $0$ | $194 / 4{,}782{,}969$ | $0$ | `0.0000000000` | $(0, 4), (0, 6), (0, 8), (0, 26), (0, 30)$ |
| **$16$** | $117$ | **$-1$** | $758 / 14{,}348{,}907$ | **$16 / 4{,}782{,}969$** | **`0.0000033453`** | **$(-1, 5/2)$**, plus $7$ states at $d_0 = 0$ ($c_0 \ge 4$) |
| $17$ | $60$ | $-1$ | $932 / 14{,}348{,}907$ | $290 / 43{,}046{,}721$ | `0.0000067369` | $(-1, 3/2), (-1, 5/2), (-1, 53/2)$, plus $11$ states at $d_0 = 0$ |
| $18$ | $28$ | $-2$ | $9{,}145 / 129{,}140{,}163$ | $1{,}234 / 129{,}140{,}163$ | `0.0000095556` | $(-2, 3/4)$, $6$ states at $d_0 = -1$, $21$ states at $d_0 = 0$ |

*Table 1: Exact zero-loss backward census across all $2^r$ unconstrained binary words $\{1, 2\}^r$ ($1 \le r \le 18$), establishing $r_{\min}^{\mathrm{le0}}(\{1, 2\}^*) = 14$ and $r_{\min}^{\mathrm{strict}}(\{1, 2\}^*) = 16$.*

---

## 3. Automatic $(5/7, 7/5)$ Tube Control, Non-Stationary Binary Splicing, and Predecessor Renewal

### 3.1 The $(5/7, 7/5)$ Automatic Tube Lemma and Three-Stage Non-Stationary Splicing

Theorem 1(3) proves that any binary family of inverse-minimal words achieving asymptotic survival base $3/4$ must abandon shift-invariance: $w_{22}$ and other finite escape words cannot be globally banned across the tail of the word, because any global factor ban depresses the topological measure growth rate strictly below $3/4$. Instead, an architecture reaching $3/4$ must **shield** early prefixes deterministically while letting the unconstrained $(1 - \alpha) T$ tail run freely inside a drift-controlled tube where rare suffix escapes can be union-bounded via $3$-adic predecessor renewal.

For $x \in (0, 1)$ and $r \ge 1$, define the **tilted coupled binary renewal moment**

$$
Z_r^{\mathrm{coupled}}(x) := \mathbb{E}_{w \sim \widetilde{\mu}_2^{\otimes r}}\!\left[\sum_{\substack{g \in \mathbb{Z}_{\ge 1}^r,\; g_r \ne w_r \\ \mathcal{P}_{w, g}(0, 0) = (d_0, c_0) \ne \bot}} x^{d_0}\right], \qquad Z_r(1/2) := Z_r^{\mathrm{coupled}}(1/2), \tag{3.1}
$$

and let $B_r \subseteq U_r := (\mathbb{Z}/3^r\mathbb{Z})^\times$ be the image of $\{1, 2\}^r$ under the forward $3$-adic affine map $\tau_0(\emptyset) := 0$, $\tau_j(w_{1..j}) := (1 + 3 \tau_{j-1}(w_{1..j-1})) \cdot 2^{-w_j} \bmod 3^j$, while $\mu_r$ denotes the pushforward of $\mathrm{Geom}(1/2)^{\otimes r}$ on $U_r$ under the same recurrence across $\mathbb{Z}_{\ge 1}^r$.

**Theorem 2 ($(5/7, 7/5)$ Automatic Tube Lemma, Non-Stationary Splicing, and Bottom–Top Bijection).**
1. *($(5/7, 7/5)$ Automatic Tube Lemma).* On $\mathcal{A}_{\{1, 2\}}(q, 7)$ for **every** $q \ge 1$, every directed edge $u \xrightarrow{e} v$ satisfies $\beta_u / \beta_v \ge 5/7$ when $e = 1$ ($\beta_v \in [1, 7]$) and $\beta_u / \beta_v \ge 7/5$ when $e = 2$ ($\beta_v \in [1, 5]$), i.e., $\beta_u / \beta_v \ge (7/5)^{2e - 3}$. Consequently, **every** walk $H = (e_1, \dots, e_m)$ of any length $m \ge 1$ in $\mathcal{A}_{\{1, 2\}}(q, 7)$ automatically satisfies

$$
2 S_m(H) - 3m \;\le\; 5, \qquad\text{i.e.,}\qquad S_m(H) \;\le\; \frac{3}{2} m + \frac{5}{2} \tag{3.2}
$$

(on $q = 128$, exact max-plus dynamic programming certifies $\max_{1 \le m \le 40} (2 S_m(H) - 3m) = 4$).
2. *(Explicit Non-Asymptotic Left-Resolving SFT Bound).* On $\mathcal{A}_{\{1, 2\}}(128, 7)$ ($769$ vertices, top strongly connected component $V_{\mathrm{top}}$ of size $629$), left-resolving determinism yields for **every** $M \ge 1$

$$
\mu_2\bigl(\mathcal{L}_M(\mathcal{A}_{\{1, 2\}}(128, 7))\bigr) \;\ge\; c_{\mathrm{SFT}}\,\lambda_{\mathrm{lo}}^M \;=\; c_{\mathrm{SFT}}\,\theta_0^M \left(\frac{3}{4}\right)^M, \tag{3.3}
$$

where $\lambda_{\mathrm{lo}} = \frac{416{,}904{,}662{,}015{,}209}{562{,}994{,}459{,}697{,}688} > \mathbf{0.740512903517}$, $\theta_0 := \frac{\lambda_{\mathrm{lo}}}{3/4} > \mathbf{0.987350538023}$, and $c_{\mathrm{SFT}} > \mathbf{0.7669478250}$.
3. *(Unconditional Non-Stationary Splicing Reduction).* Define the unconstrained tube $\mathcal{T}_N := \{u \in \{1, 2\}^N : 2 S_k(u) - 3k \le 6 \text{ for all } 1 \le k \le N\}$, which satisfies $\widetilde{\mu}_2^{\otimes N}(\mathcal{T}_N) \ge \frac{127}{128}$ for all $N \ge 1$. Splicing $W = 1^{M_0} \cdot H \cdot U \in \{1^{M_0}\} \times \mathcal{L}_M(\mathcal{A}_{\{1, 2\}}(128, 7)) \times \mathcal{T}_N$ ($M_0 \asymp \sqrt{T}, M_0 \ge 10$, $M = \lfloor \alpha T \rfloor$, $N = T - M$) produces words that **deterministically** belong to $\mathcal{N}_{M_0 + T}$ and suffer zero escapes on $1 \le i \le M_0 + M$. Consequently, the exact binary survival limit

$$
\lim_{L \to \infty} \mu_2\bigl(\mathcal{I}_L \cap \{1, 2\}^L\bigr)^{1/L} = \frac{3}{4} \tag{3.4}
$$

holds **unconditionally** whenever **either** of the following renewal bounds holds:
   - *(i) Un-tilted strict-escape count:* $\limsup_{r \to \infty} S_{\mathrm{strict}}(r)^{1/r} < \theta_0^{\ln(9/2)/\ln(9/8)} \in [\mathbf{0.8499628037}, \mathbf{0.8499628038}]$ (where $\beta_0 := \frac{\ln(9/8)}{\ln(9/2)} \in [0.0783091587, 0.0783091588]$); **or**
   - *(ii) Tilted coupled renewal moment:* there exists $x \in (0, x_{\max})$ with $x_{\max} := \theta_0^{\ln 4 / \ln(9/8)} \in [\mathbf{0.8608521198}, \mathbf{0.8608521199}]$ such that $\limsup_{r \to \infty} Z_r^{\mathrm{coupled}}(x)^{1/r} < \theta_0 > \mathbf{0.987350538023}$.
4. *(Exact Bottom–Top Bijection).* Every valid first-merger branch $g = (g_1, \dots, g_r)$ ($g_r \ne w_r$) on any binary word $w \in \{1, 2\}^r$ satisfies $g_r \ge w_r + 2 \ge 3$, and $g'_r := g_r - 2 \ge 1$ bijects such branches onto all $g' = (g_1, \dots, g_{r-1}, g'_r) \in \mathbb{Z}_{\ge 1}^r$ satisfying $\tau_r(g') \equiv 4 \tau_r(w) \pmod{3^r}$. In particular,

$$
Z_r(1/2) = \frac{1}{4}\left(\frac{4}{3}\right)^r \mu_r(4 B_r) = U_r - U_{r-1}, \qquad U_r := \left(\frac{4}{3}\right)^r \mu_r(B_r). \tag{3.5}
$$

*Proof.* **Part 1.** Along $u \xrightarrow{e} v$ in $\mathcal{A}_{\{1, 2\}}(q, 7)$, $\beta_u \ge \psi_e(\beta_v) = (1 + 2^e \beta_v)/3$, so $\beta_u / \beta_v \ge \frac{1}{3\beta_v} + \frac{2^e}{3}$. Since $\beta \mapsto \frac{1}{3\beta} + \frac{2^e}{3}$ is decreasing, $\beta_v \le 7$ for $e = 1$ gives $\beta_u / \beta_v \ge \frac{1 + 14}{21} = \frac{5}{7} = (7/5)^{2(1) - 3}$, while $\beta_v \le 5$ for $e = 2$ gives $\beta_u / \beta_v \ge \frac{1 + 20}{15} = \frac{7}{5} = (7/5)^{2(2) - 3}$. Multiplying along any walk $v_0 \xrightarrow{e_1} v_1 \to \dots \xrightarrow{e_m} v_m$ yields

$$
7 \;\ge\; \frac{\beta_{v_0}}{\beta_{v_m}} \;=\; \prod_{j=1}^m \frac{\beta_{v_{j-1}}}{\beta_{v_j}} \;\ge\; \left(\frac{7}{5}\right)^{\sum_{j=1}^m (2 e_j - 3)} \;=\; \left(\frac{7}{5}\right)^{2 S_m(H) - 3m}.
$$

Because $2 S_m(H) - 3m \in \mathbb{Z}$ and $7^6 = 117{,}649 > 109{,}375 = 7 \cdot 5^6$, $(7/5)^6 > 7$, forcing $2 S_m(H) - 3m \le 5$.

**Part 2.** On $\mathcal{A}_{\{1, 2\}}(128, 7)$, every pair $(v, e) \in V \times \{1, 2\}$ has at most one incoming vertex $u$ ($\beta_u = \max(1, \lceil 128 \psi_e(\beta_v) \rceil / 128)$), so distinct walks of length $M$ terminating at a **single** vertex $v_* \in V_{\mathrm{top}}$ carry pairwise distinct label words in $\{1, 2\}^M$. Let $A_{\mathrm{top}}$ be the $\mu_2$-weighted adjacency matrix on $V_{\mathrm{top}}$ and let $w > 0$ be the certified rational vector satisfying $(A_{\mathrm{top}}^\top w)_v \ge \lambda_{\mathrm{lo}} w_v$ for all $v \in V_{\mathrm{top}}$ (`verify_theorem2`). Setting $w_{\max} := \max_{z \in V_{\mathrm{top}}} w_z$, entrywise positivity gives $\mathbf{1} \ge w / w_{\max}$ and

$$
\sum_{v \in V_{\mathrm{top}}} \bigl((A_{\mathrm{top}}^\top)^M \mathbf{1}\bigr)_v \;\ge\; \frac{1}{w_{\max}} \sum_{v \in V_{\mathrm{top}}} \bigl((A_{\mathrm{top}}^\top)^M w\bigr)_v \;\ge\; \frac{\lambda_{\mathrm{lo}}^M}{w_{\max}} \sum_{v \in V_{\mathrm{top}}} w_v.
$$

By the pigeonhole principle over $|V_{\mathrm{top}}| = 629$, for each $M \ge 1$ some vertex $v_*(M) \in V_{\mathrm{top}}$ satisfies $((A_{\mathrm{top}}^\top)^M \mathbf{1})_{v_*(M)} \ge c_{\mathrm{SFT}} \lambda_{\mathrm{lo}}^M$ with $c_{\mathrm{SFT}} := \frac{\sum_{v \in V_{\mathrm{top}}} w_v}{|V_{\mathrm{top}}| w_{\max}} > 0.7669478250$, proving $(3.3)$ without overcounting.

**Part 3.** Under $\widetilde{\mu}_2^{\otimes N}$, the increments $\xi_j := 2 u_j - 3 \in \{-1, +1\}$ are i.i.d. with $\mathbb{P}(\xi_j = -1) = 2/3$, $\mathbb{P}(\xi_j = +1) = 1/3$, so $M_k := 2^{2 S_k(u) - 3k}$ ($M_0 = 1$) satisfies $\mathbb{E}[2^{\xi_j}] = \frac{2}{3}\cdot\frac{1}{2} + \frac{1}{3}\cdot 2 = 1$ and is an exact non-negative martingale. Because $\xi_j \in \{-1, +1\}$ is integer unit-step, the first exit from $\{x \le 6\}$ hits $2 S_\tau - 3\tau = 7$ ($M_\tau = 128$) with zero overshoot; Ville's maximal inequality [27] gives $\widetilde{\mu}_2^{\otimes N}(\mathcal{T}_N^c) \le \frac{\mathbb{E}[M_0]}{128} = \frac{1}{128}$, hence $\widetilde{\mu}_2^{\otimes N}(\mathcal{T}_N) \ge \frac{127}{128}$ (at $N = 40$, exact DP gives $\widetilde{\mu}_2^{\otimes 40}(\mathcal{T}_{40}^c) \approx 0.0071731345 < 1/128 = 0.0078125$).

Fix $\alpha \in (0, 1)$. For each integer horizon $L \ge 110$, choose $T \ge 100$ and $M_0 \in \{\lceil \sqrt{T} \rceil, \lceil \sqrt{T} \rceil + 1\} \ge 10$ such that $L = M_0 + T$, and set $M := \lfloor \alpha T \rfloor$, $N := T - M$, and $\mathcal{F}_L := \{1^{M_0}\} \times \mathcal{L}_M(\mathcal{A}_{\{1, 2\}}(128, 7)) \times \mathcal{T}_N \subseteq \{1, 2\}^L$. For every $W = 1^{M_0} \cdot H \cdot U \in \mathcal{F}_L$ and every prefix $1 \le i \le L$:
- If $1 \le i \le M_0$, then $S_i(W) = i$ and $2^i < 3^i$.
- If $i = M_0 + j$ with $1 \le j \le T$, combining $2 S_m(H) - 3m \le 5$ and $2 S_k(U) - 3k \le 6$ gives $2(S_i(W) - M_0) \le 3j + 11$, so
  $$
  \left(\frac{2^{S_i(W)}}{3^i}\right)^2 \;\le\; \frac{2^{11 + 2 M_0 + 3j}}{3^{2 M_0 + 2j}} \;=\; \frac{2^{11} \cdot 4^{M_0}}{9^{M_0}} \left(\frac{8}{9}\right)^j \;\le\; \frac{2^{31}}{3^{20}} \left(\frac{8}{9}\right)^j \;<\; \left(\frac{8}{9}\right)^j \;<\; 1, \tag{3.6}
  $$
  since $2^{31} = 2{,}147{,}483{,}648 < 3{,}486{,}784{,}401 = 3^{20}$ (note $M_0 = 10$ is sharp because $2^{29} > 3^{18}$ at $M_0 = 9$).

Thus $\mathcal{F}_L \subseteq \mathcal{N}_L$ deterministically. By [20, Proposition 3.5(2)], $1^{M_0} \cdot H \in \mathcal{I}_{M_0 + M}^{\mathrm{strict}}$, so zero escapes occur at $1 \le i \le M_0 + M$. Suppose $W \in \mathcal{F}_L \setminus \mathcal{I}_L$ escapes at some prefix $i \in \{M_0 + M + 1, \dots, L\}$ and suffix depth $r \in \{1, \dots, i\}$, with $k_0 := i - r$ and $\mathcal{P}_{W_{k_0+1..i}, g}(0, 0) = (d_0, c_0) \ne \bot$. Because $W \in \mathcal{N}_L$, if $k_0 \ge 1$ then $2^{d_0} \cdot 3^{k_0} < 2^{S_{k_0}(W)} < 3^{k_0}$ forces $d_0 \le -1 < 0$; hence **every** escape $(i, r)$ requires $(d_0, c_0)$ to satisfy the strict escape condition ($d_0 < 0$ or $d_0 = 0, c_0 < 0$). Moreover, whenever $r \le M$, we have $k_0 = i - r \ge M_0 + M + 1 - r > M_0$, so $j := k_0 - M_0 \ge M + 1 - r \ge 1$; substituting $(3.6)$ into $2^{d_0} \cdot 3^{k_0} < 2^{S_{k_0}(W)}$ gives

$$
2^{-d_0} \;>\; \frac{3^{k_0}}{2^{S_{k_0}(W)}} \;>\; \left(\frac{9}{8}\right)^{j/2} \;\ge\; \left(\frac{9}{8}\right)^{(M + 1 - r)/2} \qquad (1 \le r \le M). \tag{3.7}
$$

- *Under Condition (i):* Because $g_\ell \ge 1$ and $W_\ell \le 2$, $d_0 = \|g\| - \|W_{k_0+1..i}\| \ge -r$, so $2^{-2 d_0} \le 4^r$. Squaring $(3.7)$ for $r \le M$ yields $4^r > (9/8)^{M + 1 - r}$, i.e., $(9/2)^r > (9/8)^{M + 1}$, which forces $r > \beta_0(M + 1)$ ($\beta_0 = \ln(9/8)/\ln(9/2)$). Defining $\mathcal{B}_{i, r}^{\mathrm{strict}} \subseteq \{1, 2\}^L$ as the event that $W_{i-r+1..i}$ admits a strict-escape branch, set inclusion $\mathcal{F}_L \cap \mathcal{B}_{i, r}^{\mathrm{strict}} \subseteq \mathcal{B}_{i, r}^{\mathrm{strict}}$ and $(1.2)$ give $\mu_2(\mathcal{F}_L \cap \mathcal{B}_{i, r}^{\mathrm{strict}}) \le (3/4)^L S_{\mathrm{strict}}(r)$. If $S_{\mathrm{strict}}(r) \le C \sigma^r$ with $\sigma < \theta_0^{1/\beta_0}$, then $\sigma^{\beta_0} < \theta_0$ and $\sum_{i = M_0 + M + 1}^L \sum_{r > \beta_0(M+1)} S_{\mathrm{strict}}(r) \le C T L (\sigma^{\beta_0})^{M+1}$.
- *Under Condition (ii):* Fix $x \in (0, x_{\max})$, so $\gamma(x) := x^{\ln(9/8)/\ln 4} < x_{\max}^{\ln(9/8)/\ln 4} = \theta_0$, and let $Z_r^{\mathrm{coupled}}(x) \le C_\eta \eta^r$ with $\eta < \theta_0$. Setting $\rho_* := \max(\gamma(x), \eta) < \theta_0$, raising $(3.7)$ to $\frac{\ln(1/x)}{\ln 2} > 0$ gives $x^{d_0} > \gamma(x)^{-(M + 1 - r)}$ for $1 \le r \le M$ (while $x^{d_0} \ge 1$ for $r > M$ since $d_0 \le 0$). Applying Markov's inequality under $\widetilde{\mu}_2^{\otimes L}$ to $\sum_{g: g_r \ne W_i} x^{d_0}$ bounds each $(i, r)$ term by $\gamma(x)^{M + 1 - r} Z_r^{\mathrm{coupled}}(x) \le C_\eta \rho_*^{M + 1}$ ($1 \le r \le M$) and $Z_r^{\mathrm{coupled}}(x) \le C_\eta \rho_*^{M + 1}$ ($r > M$), summing over all $(i, r)$ to $\le C_\eta T L \rho_*^{M + 1}$.

In either case, by $(1.2)$ and $(3.3)$, $\mu_2(\mathcal{F}_L) \ge \frac{127}{128} c_{\mathrm{SFT}} (2/3)^{M_0} \theta_0^M (3/4)^L$. Because $M_0 = O(\sqrt{T})$ while $M = \lfloor \alpha T \rfloor$ and $\max(\sigma^{\beta_0}, \rho_*) < \theta_0$, the escape-to-candidate measure ratio is $O(T^2) (3/2)^{\sqrt{T}} (\rho/\theta_0)^{\alpha T} \to 0$ as $T \to \infty$. Thus $\mu_2(\mathcal{I}_L \cap \{1, 2\}^L) \ge \frac{1}{2} \mu_2(\mathcal{F}_L)$ for all large $L$, giving $\liminf_{L \to \infty} \mu_2(\mathcal{I}_L \cap \{1, 2\}^L)^{1/L} \ge \frac{3}{4} \theta_0^\alpha$; sending $\alpha \downarrow 0$ yields $(3.4)$.

**Part 4.** At step $j = r$ from $(d_r, c_r) = (0, 0)$, $\mathcal{P}_{w_r, g_r}(0, 0) \ne \bot \iff 2^{g_r - w_r} \equiv 1 \pmod 3 \iff g_r \equiv w_r \pmod 2$. Since $w_r \in \{1, 2\}$, $g_r \ge 1$, and $g_r \ne w_r$, we have $\min g_r = w_r + 2 \ge 3$ ($g_r \in \{3, 5, \dots\}$ if $w_r = 1$; $g_r \in \{4, 6, \dots\}$ if $w_r = 2$). Substituting $g_r = g'_r + 2$ ($g'_r \ge 1$) at the final step multiplies $\tau_r(g_1, \dots, g_r) \equiv \tau_r(w) \pmod{3^r}$ by $4$, giving $\tau_r(g_1, \dots, g_{r-1}, g'_r) \equiv 4 \tau_r(w) \pmod{3^r}$ and factoring out $x^2$ (equal to $1/4$ at $x = 1/2$). Finally, partitioning all pairs $(w, g) \in \{1, 2\}^r \times \mathbb{Z}_{\ge 1}^r$ satisfying $\tau_r(g) \equiv \tau_r(w) \pmod{3^r}$ into $g_r = w_r$ (contributing $U_{r-1}$) and $g_r \ne w_r$ (contributing $Z_r(1/2)$) proves $U_r = U_{r-1} + Z_r(1/2)$. $\blacksquare$

| Depth $r$ | $U_r$ (floor dec.) | $Z_r(1/2)$ (floor dec. / interval) | Exact $Z_r(1/2)$ / Bit-Size | Ratio $Z_r / Z_{r-1}$ | $Z_r^{\mathrm{coupled}}(11/30)$ | Coupled Ratio |
|---:|---:|---:|---|---:|---:|---:|
| $1$ | `1.3333333333` | `0.3333333333` | $1/3$ | — | `0.1553273427` | — |
| $2$ | `1.6084656084` | `0.2751322751` | $52/189$ | `0.82539682` | `0.1494822338` | `0.96236909` |
| $3$ | `1.8290814131` | `0.2206158046` | $520{,}496 / 2{,}359{,}287$ | `0.80185359` | `0.1083164120` | `0.72461060` |
| $4$ | `2.0240188072` | `0.1949373941` | `bits=54` | `0.88360575` | `0.0847197022` | `0.78215018` |
| $5$ | `2.1947363611` | `0.1707175538` | `bits=166` | `0.87575580` | `0.0675134228` | `0.79690344` |
| $6$ | `2.3406691799` | `0.1459328187` | `bits=489` | `0.85482023` | `0.0512644283` | `0.75932201` |
| $7$ | `2.4664964005` | `0.1258272206` | `bits=1465` | `0.86222702` | `0.0393616967` | `0.76781694` |
| $8$ | `2.5758182988` | `0.1093218983` | `bits=4382` | `0.86882550` | `0.0302017439` | `0.76728765` |
| $9$ | `2.6705902497` | `0.0947719508` | `bits=13132` | `0.86690729` | `0.0230637258` | `0.76365543` |
| **$10$** | — | **`[0.082524506197, 0.082524506198]`** | $220$-bit `RatInterval` | **`[0.87076930, 0.87076931]`** | — | — |

*Table 2: Certified zero-float binary renewal values $Z_r(1/2)$ ($r = 1 \dots 9$ exact `Fraction`, $r = 10$ outward-rounded $220$-bit `RatInterval`) and tilted coupled renewal $Z_r^{\mathrm{coupled}}(11/30)$ ($r = 1 \dots 9$). Here $x = 11/30 \approx 0.3667$ rationally approximates the minimizer $x_{\mathrm{Haar}} = (\sqrt{3} - 1)/2 \approx 0.3660$ of the Haar-equidistributed renewal base $\min_{x \in (0, 1)} \frac{2x + 1}{9x(1 - x)} = \frac{4 + 2\sqrt{3}}{9} \in [0.8293446239, 0.8293446240] < \theta_0$, with $\gamma(1/2) \in [0.9428090415, 0.9428090416] < \theta_0$ and $\gamma(11/30) \in [0.9182890614, 0.9182890615] < \theta_0$.*

![Binary renewal contraction vs non-stationary splicing ceiling and telescoping collision phase transition across u=1/4](supplement/figure-1.png)

*Figure 1: (a) Certified binary renewal contraction $Z_r(1/2)$ ($r \le 10$) and tilted coupled renewal $Z_r^{\mathrm{coupled}}(11/30)$ ($r \le 9$) against the non-stationary splicing ceiling $\theta_0^r$ ($\theta_0 \ge 0.987351$), alongside the three-tier shift-invariant sub-$3/4$ subshift ceilings (including Tier 3 for any subshift $\Sigma$ surviving at $T \ge 22$ under a $1^{M_0}$ header). (b) Exact Cramér–Syracuse phase transition of $U_R^{(u)}(\sqrt{u})$ across $u \in \{4/25, 81/400, 1/4, 121/400\}$, highlighting the critical $u = 1/4$ identity $Z_r^{(1/4)}(1/2) = E_r - E_{r-1}$ (Tables 2–3).*

---

## 4. Telescoping Collision Identity Across the $u = 1/4$ Cramér Saddle and the Binary Fiber-Miss Law

### 4.1 Exact Bridge Between Predecessor Renewal and $L^2(\mathbb{Z}_3)$ Syracuse Collision Energy

To place binary renewal within the full-alphabet Cramér phase diagram on $\mathbb{Z}_{\ge 1}^*$ and connect directly to the $3$-adic Syracuse density theory of [7, 18, 21, 22], consider for $u \in (0, 1 - 1/\log_2 3)$ the tilted geometric valuation law $Q_u(e) := \frac{1 - u}{u} u^e$ ($e \ge 1$). Since $\mathbb{E}_{Q_u}[e] = \frac{1}{1 - u} < \log_2 3$, $Q_u$-typical words satisfy $w \in \mathcal{N}_T$ with asymptotic $2$-adic Haar survival base $\Lambda(u) := \exp(-\mathbb{E}_{Q_u}[\ln(2^e Q_u(e))]) = \frac{1}{2(1 - u)(2u)^{u/(1-u)}}$. For any $\rho \in (0, 1)$, let $\mu_R^{(\rho)}$ be the mod-$3^R$ Syracuse distribution on $U_R = (\mathbb{Z}/3^R\mathbb{Z})^\times$ generated by $Q_{\rho}(g) = \frac{1 - \rho}{\rho} \rho^g$, with $L^2(\mathbb{Z}_3, m_3)$ step-$R$ collision energy $E_R^{(\rho)} := 3^R \sum_{z \in U_R} \mu_R^{(\rho)}(z)^2 = \frac{3}{2} Q_{2, R}^{(\rho)}$ (matching [18, Eq. (2a)] at $\rho = 1/2$, where $E_R := E_R^{(1/2)} = \int_{\mathbb{Z}_3} \rho_R^2 \, dm_3$). Define the tilted $r$-step renewal increment

$$
Z_r^{(u)}(\rho) := \mathbb{E}_{w \sim Q_u^{\otimes r}}\!\left[\sum_{\substack{g \in \mathbb{Z}_{\ge 1}^r,\; g_r \ne w_r \\ \mathcal{P}_{w, g}(0, 0) = (d_0, c_0) \ne \bot}} \rho^{d_0}\right], \qquad U_R^{(u)}(\rho) := 1 + \sum_{r=1}^R Z_r^{(u)}(\rho). \tag{4.1}
$$

**Theorem 3 (Telescoping Collision Identity at $\rho = \sqrt{u}$ and Exact Binary Fiber-Miss Law).**
1. *(Telescoping Collision Identity and Critical $u = 1/4$ Martingale Bridge).* Along the diagonal saddle $\rho = \sqrt{u}$ ($u \in (0, 1)$), **every** horizon $R \ge 1$ satisfies the exact identity

$$
U_R^{(u)}(\sqrt{u}) = 1 + \sum_{r=1}^R Z_r^{(u)}(\sqrt{u}) = \left(\frac{1 + \sqrt{u}}{3(1 - \sqrt{u})}\right)^R E_R^{(\sqrt{u})}. \tag{4.2}
$$

At the critical tilt **$u = 1/4, \rho = 1/2$** ($\Lambda(1/4) = \frac{2^{4/3}}{3} \in [\mathbf{0.8399473665}, \mathbf{0.8399473666}]$), the exponential base $\frac{1 + 1/2}{3(1 - 1/2)} = 1$ vanishes identically, yielding for every $r \ge 1$ the exact martingale-difference identity

$$
Z_r^{(1/4)}(1/2) = E_r - E_{r-1} = \bigl\|\rho_r - \rho_{r-1}\bigr\|_{L^2(\mathbb{Z}_3, m_3)}^2 \ge 0. \tag{4.3}
$$

Combining $(4.3)$ with [18, Corollary (2a)] ($c_1 R \le E_R \le C_1 R$) proves unconditionally that $\sum_{r=1}^R Z_r^{(1/4)}(1/2) = E_R - 1 = \Theta(R)$ diverges linearly while $\limsup_{r \to \infty} Z_r^{(1/4)}(1/2)^{1/r} \le 1$.
2. *(Exact Binary Fiber-Miss Law).* For every $k \ge 1$, $|B_k| = |4 B_k| = 2^k$, and reduction modulo $3^k$ maps $4 B_{k+1} \to 4 B_k$ uniformly $2$-to-$1$: each residue $z_0 \in 4 B_k \subseteq U_k$ has three lifts $z_0 + j \cdot 3^k \in U_{k+1}$ ($j \in \{0, 1, 2\}$), of which **exactly two** lie in $4 B_{k+1}$ and **one** excluded lift $z_{\mathrm{miss}}(z_0)$ lies outside $4 B_{k+1}$. Defining the conditional excluded-lift $\mu_{k+1}$-share $\theta_{\mathrm{miss}}^{(k)} := \bigl(\sum_{z_0 \in 4 B_k} \mu_{k+1}(z_{\mathrm{miss}}(z_0))\bigr) / \mu_k(4 B_k) \in (0, 1)$, we have for every $k \ge 1$:

$$
\frac{Z_{k+1}(1/2)}{Z_k(1/2)} = \frac{4}{3}\bigl(1 - \theta_{\mathrm{miss}}^{(k)}\bigr) = \frac{8}{9} - \frac{4}{3}\!\left(\theta_{\mathrm{miss}}^{(k)} - \frac{1}{3}\right), \tag{4.4}
$$

with $\theta_{\mathrm{miss}}^{(k)} > 1/3$ certified across all $1 \le k \le 8$ ($\theta_{\mathrm{miss}}^{(8)} \ge 0.3498195306$, $Z_9(1/2)/Z_8(1/2) \approx 0.86690729 < 8/9$).

*Proof.* **Part 1.** Partition all pairs $(w, g) \in \mathbb{Z}_{\ge 1}^R \times \mathbb{Z}_{\ge 1}^R$ satisfying $\tau_R(g) \equiv \tau_R(w) \pmod{3^R}$ by the rightmost divergence index $r := \max(\{0\} \cup \{j \le R : g_j \ne w_j\})$. For $r = 0$, $g = w$ contributes $\sum_{w \in \mathbb{Z}_{\ge 1}^R} Q_u^{\otimes R}(w) \rho^0 = 1$. For $1 \le r \le R$, since $g_{r+1..R} = w_{r+1..R}$ applies identical invertible affine contractions modulo $3$ from step $r$ to step $R$, $\tau_R(g) \equiv \tau_R(w) \pmod{3^R}$ holds if and only if $\tau_r(g_{1..r}) \equiv \tau_r(w_{1..r}) \pmod{3^r}$ ($\mathcal{P}_{w_{1..r}, g_{1..r}}(0, 0) \ne \bot$), while $\|g\| - \|w\| = \|g_{1..r}\| - \|w_{1..r}\|$ and $\sum_{w_{r+1..R} \in \mathbb{Z}_{\ge 1}^{R-r}} Q_u^{\otimes(R-r)}(w_{r+1..R}) = 1$. Hence $U_R^{(u)}(\rho) = \sum_{w, g \in \mathbb{Z}_{\ge 1}^R : \tau_R(g) \equiv \tau_R(w) (3^R)} Q_u^{\otimes R}(w) \rho^{\|g\| - \|w\|}$. Setting $\rho = \sqrt{u}$ ($u = \rho^2$) makes $Q_u(e) \rho^{-e} = \frac{1 - \rho^2}{\rho^2} \rho^e = \frac{1 + \rho}{\rho} Q_\rho(e)$, so the $w$- and $g$-sums become symmetric:

$$
U_R^{(u)}(\sqrt{u}) = \left(\frac{1 + \rho}{\rho}\right)^R \left(\frac{\rho}{1 - \rho}\right)^R \sum_{z \in U_R} \mu_R^{(\rho)}(z)^2 = \left(\frac{1 + \rho}{1 - \rho}\right)^R \cdot 3^{-R} E_R^{(\rho)} = \left(\frac{1 + \sqrt{u}}{3(1 - \sqrt{u})}\right)^R E_R^{(\sqrt{u})}.
$$

At $u = 1/4, \rho = 1/2$, $\frac{1 + 1/2}{3(1 - 1/2)} = 1$, giving $U_R^{(1/4)}(1/2) = E_R$ and $Z_r^{(1/4)}(1/2) = E_r - E_{r-1}$. Because $\rho_{r-1} = \mathbb{E}_{m_3}[\rho_r \mid \mathcal{F}_{r-1}]$ is an $L^2(\mathbb{Z}_3, m_3)$-orthogonal projection, $E_r - E_{r-1} = \|\rho_r\|_2^2 - \|\rho_{r-1}\|_2^2 = \|\rho_r - \rho_{r-1}\|_2^2 \ge 0$; [18, Corollary (2a)] then gives $\sum_{r=1}^R Z_r^{(1/4)}(1/2) = E_R - 1 = \Theta(R)$, and $0 \le Z_R^{(1/4)}(1/2) \le E_R \le C_1 R$ implies $\limsup_{R \to \infty} Z_R^{(1/4)}(1/2)^{1/R} \le 1$.

**Part 2.** We prove $|B_k| = 2^k$ and uniform $2$-to-$1$ surjectivity $B_{k+1} \bmod 3^k \to B_k$ by induction on $k \ge 1$. For $k = 1$, $B_1 = \{1, 2\} \subseteq U_1$ has $|B_1| = 2$, mapping $2$-to-$1$ onto $B_0 = \{0\}$. Suppose $|B_k| = 2^k$ and $B_k \bmod 3^{k-1} \to B_{k-1}$ is uniformly $2$-to-$1$. If $(1 + 3 y_1) 2^{-e_1} \equiv (1 + 3 y_2) 2^{-e_2} \pmod{3^{k+1}}$ for $y_1, y_2 \in B_k$ and $e_1, e_2 \in \{1, 2\}$, reducing modulo $3$ gives $2^{-e_1} \equiv 2^{-e_2} \pmod 3 \implies e_1 = e_2$, whence $3(y_1 - y_2) \equiv 0 \pmod{3^{k+1}} \implies y_1 \equiv y_2 \pmod{3^k} \implies y_1 = y_2$; thus $|B_{k+1}| = 2 \cdot |B_k| = 2^{k+1}$. For any $y_0 = (1 + 3 \bar{y}) 2^{-e_0} \in B_k$ ($\bar{y} \in B_{k-1}, e_0 \in \{1, 2\}$), an element $y' = (1 + 3 y) 2^{-e} \in B_{k+1}$ satisfies $y' \equiv y_0 \pmod{3^k}$ if and only if $e = e_0$ and $y \equiv \bar{y} \pmod{3^{k-1}}$, which holds for the **exactly two** elements $y \in B_k$ over $\bar{y}$. Multiplying by the unit $4 \in U_{k+1}$ transfers uniform $2$-to-$1$ surjectivity to $4 B_{k+1} \to 4 B_k$. Because $\mu_{k+1}$ pushes forward modulo $3^k$ to $\mu_k$ ($\sum_{j=0}^2 \mu_{k+1}(z_0 + j \cdot 3^k) = \mu_k(z_0)$), summing over $z_0 \in 4 B_k$ gives $\mu_{k+1}(4 B_{k+1}) = \mu_k(4 B_k) - \sum_{z_0 \in 4 B_k} \mu_{k+1}(z_{\mathrm{miss}}(z_0)) = \mu_k(4 B_k)(1 - \theta_{\mathrm{miss}}^{(k)})$; multiplying by $\frac{1}{4}(4/3)^{k+1}$ yields $(4.4)$. $\blacksquare$

| Regime & Tilt $(u, \rho = \sqrt{u})$ | Cramér Base $\Lambda(u)$ | Prefactor $\frac{1+\rho}{3(1-\rho)}$ | $U_1^{(u)}(\rho)$ | $U_4^{(u)}(\rho)$ | $U_7^{(u)}(\rho)$ | $Z_7^{(u)}(\rho)$ | $E_7^{(\rho)}(\mathbb{Z}_3)$ |
|---|---|---:|---:|---:|---:|---:|---:|
| Subcritical $(4/25,\; 2/5)$ | $[0.7395164947, 0.7395164948]$ | $7/9 < 1$ | `1.38095238` | `1.87768724` | `2.22112762` | `0.09990430` | `12.89985413` |
| Subcritical $(81/400,\; 9/20)$ | $[0.7887034534, 0.7887034535]$ | $29/33 < 1$ | `1.50783699` | `2.33281915` | `2.96971618` | `0.19264403` | `7.33713551` |
| **Critical $(1/4,\; 1/2)$ [18]** | **$[0.8399473665, 0.8399473666]$** | **$1$ (exact)** | **`1.66666666`** | **`3.06864623`** | **`4.46582134`** | **`0.46549142`** | **`4.46582134`** |
| Supercritical $(121/400,\; 11/20)$ | $[0.8914083281, 0.8914083282]$ | $31/27 > 1$ | `1.86738351` | `4.34152170` | `7.93263050` | `1.35839929` | `3.01600264` |

*Table 3: Exact rational verification of the Telescoping Collision Identity $(4.2)$ across subcritical ($u < 1/4$), critical ($u = 1/4$, where $U_R^{(1/4)}(1/2) \equiv E_R$ bridges [18]), and supercritical ($u > 1/4$) tilts.*

---

## 5. The Triple Analytic Obstruction Theorem and Primitive Additive $L^4$ Conductor Shells

### 5.1 Why Decoupled Hölder Bounds, Multiplicative Characters, and Continuous $3$-Adic Potentials Fail

Having reduced $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*) = 3/4$ to $\limsup_{r \to \infty} Z_r^{\mathrm{coupled}}(x)^{1/r} < \theta_0$ (Theorem 2), it is natural to ask whether existing $3$-adic tools—physical-space weak-$L^2$ tail rearrangement [18], decoupled Hölder inequalities, multiplicative Dirichlet characters on $U_r = (\mathbb{Z}/3^r\mathbb{Z})^\times$, or continuous $3$-adic Lyapunov functions for the coupled renewal operator—can bound $Z_r(1/2)$ or $Z_r^{\mathrm{coupled}}(x)$. Theorem 4 proves that all three routes encounter **exact, unconditional mathematical obstructions**, and identifies primitive additive $L^4$ conductor shells as the exact harmonic mechanism that breaks multiplicative phase-blindness.

For $F : \Omega \to \mathbb{R}$ on the compact $3$-adic state space $\Omega := \mathbb{Z}_3^\times \times \mathbb{Z}_3$, define the positive coupled renewal operator

$$
(\mathcal{M} F)(\alpha, \delta) := \frac{4}{3} \sum_{e \in \{1, 2\}} \sum_{\substack{g \ge 1 \\ \alpha 2^{g-e} + 2^g \delta \equiv 1 \pmod 3}} 2^{-g}\,F\!\left(\alpha 2^{g-e},\; \frac{\alpha 2^{g-e} + 2^g \delta - 1}{3}\right). \tag{5.1}
$$

For a subset $A \subseteq \mathbb{Z}/3^m\mathbb{Z}$, write $\widehat{\mathbf{1}_A}(a) := \sum_{y \in A} e^{-2\pi i a y / 3^m}$ ($a \in \mathbb{Z}/3^m\mathbb{Z}$) for its additive Fourier transform and $E_+(A) := \#\{(y_1, y_2, y_3, y_4) \in A^4 : y_1 + y_2 \equiv y_3 + y_4 \pmod{3^m}\}$ for its additive quadruple energy. For a multiplicative character $\chi \in \widehat{U_r}$, write $\widehat{\mathbf{1}_S}(\chi) := \sum_{z \in S} \overline{\chi(z)}$ ($S \subseteq U_r$).

**Theorem 4 (Triple Analytic Obstruction Theorem and Primitive Additive $L^4$ Conductor-Shell Decay).**
1. *(Obstruction I — Weak-$L^2$ Rearrangement and Universal Tilted Hölder Barrier).*
   - *(a) Weak-$L^2$ barrier:* Let $E_r := 4 B_r + 3^r \mathbb{Z}_3 \in \mathcal{F}_r$ ($m_3(E_r) = (2/3)^r$, $\mu_r(4 B_r) = \int_{E_r} \rho \, dm_3$). Applying the sharp tail bound $m_3\{\rho > t\} \le C / t^2$ [18, Eq. (1)] via Hardy–Littlewood rearrangement gives $\int_{E_r} \rho \, dm_3 \le 2\sqrt{C\,m_3(E_r)}$, yielding the exponentially **diverging** bound
     $$
     Z_r(1/2) \;\le\; \frac{\sqrt{C}}{2}\left(\sqrt{\frac{32}{27}}\right)^r, \qquad \sqrt{\frac{32}{27}} \approx \mathbf{1.088662} > 1, \tag{5.2}
     $$
     which is sharp up to constants over measurable sets of measure $(2/3)^r$ since $\lim_{t \to \infty} t^2 m_3\{\rho > t\} = \kappa > 0$ [18, Theorem].
   - *(b) Universal decoupled Hölder barrier:* Writing $Z_r^{\mathrm{coupled}}(x) = x^2 \bigl(\frac{x}{1-x}\bigr)^r \sum_{z \in U_r} W_r^{(x)}(4^{-1} z) \mu_r^{(x)}(z)$, for **every** tilt $x \in (0, 1)$ and **every** Hölder conjugate pair $\frac{1}{p} + \frac{1}{q} = 1$ ($1 \le p, q \le \infty$), the decoupled Hölder upper bound $x^2 \bigl(\frac{x}{1-x}\bigr)^r \|W_r^{(x)}\|_{\ell^p(U_r)} \|\mu_r^{(x)}\|_{\ell^q(U_r)}$ grows exponentially at base $\ge \max\bigl(B_{\mathrm{flat}}(x, p), B_{\mathrm{atom}}(x, p)\bigr) > \frac{51}{50} = \mathbf{1.02} > 1$, where
     $$
     B_{\mathrm{flat}}(x, p) := \frac{\bigl((2x)^p + 1\bigr)^{1/p}}{3^{1 + 1/p}\,x(1 - x)}, \qquad B_{\mathrm{atom}}(x, p) := \frac{\bigl((2x)^p + 1\bigr)^{1/p}}{3x} \tag{5.3}
     $$
     (for $p = q = 2$, $B_{\mathrm{CS}}(x) := B_{\mathrm{flat}}(x, 2)$ achieves its unique global minimum at $4 x_*^3 + 2x_* - 1 = 0$, $x_* \in [0.385458498529, 0.385458498530]$, with $\min_{x \in (0, 1)} B_{\mathrm{CS}}(x) \in [\mathbf{1.02583159}, \mathbf{1.02583160}] > \frac{51}{50} = 1.02$, certified algebraically by a degree-$210$ positive integer Bernstein polynomial).
2. *(Obstruction II — $\chi(4)$-Phase-Blindness of Multiplicative Characters).* Every character $\chi \in \widehat{U_r}$ satisfies $\widehat{\mathbf{1}_{4 B_r}}(\chi) = \overline{\chi(4)}\,\widehat{\mathbf{1}_{B_r}}(\chi)$ and $|\widehat{\mathbf{1}_{4 B_r}}(\chi)| = |\widehat{\mathbf{1}_{B_r}}(\chi)|$. Consequently, **every** modulus-only multiplicative character bound satisfies

$$
\frac{1}{4}\left(\frac{4}{3}\right)^r \frac{1}{\phi(3^r)} \sum_{\chi \in \widehat{U_r}} \bigl|\widehat{\mu_r}(\chi)\bigr|\,\bigl|\widehat{\mathbf{1}_{4 B_r}}(\chi)\bigr| \;\ge\; \frac{1}{4}\,U_r \;=\; \frac{1}{4}\!\left(1 + \sum_{k=1}^r Z_k(1/2)\right) \;\ge\; \frac{1}{3} \tag{5.4}
$$

for all $r \ge 1$ ($0.66764756$ at $r = 9$), and can never prove $Z_r(1/2) \to 0$.
3. *(Obstruction III — Non-Existence of Continuous $3$-Adic Sub-Invariant Functions for $\mathcal{M}$).* The operator $\mathcal{M} : C^0(\Omega) \to C^0(\Omega)$ is bounded ($\|\mathcal{M}\|_{C^0 \to C^0} = 4/3$) and satisfies $(\mathcal{M}^r \mathbf{1})(1, 0) = U_r$ and $\frac{1}{4}(\mathcal{M}^r \mathbf{1})(4, 0) = Z_r(1/2)$ for every $r \ge 1$. At $(1, 0) \in \Omega$, every $F : \Omega \to \mathbb{R}$ satisfies the exact identity

$$
(\mathcal{M} F)(1, 0) = F(1, 0) + \sum_{j=1}^{\infty} 4^{-j}\,F\!\left(4^j,\; \frac{4^j - 1}{3}\right). \tag{5.5}
$$

Every non-negative continuous function $F \in C^0(\Omega)$ satisfying $\mathcal{M} F \le F$ therefore obeys $F(1, 0) = 0$ (and $(\mathcal{M} F)(4, 0) = 0$). In particular, no non-negative $F \in C^0(\Omega)$ with $F \ge \mathbf{1}$ (or $F(1, 0) > 0$) satisfies $\mathcal{M} F \le F$, and neither $\mathcal{M}^r \mathbf{1}$ nor its Cesàro averages $\frac{1}{R}\sum_{r=0}^{R-1} \mathcal{M}^r \mathbf{1}$ can converge in $C^0(\Omega)$ (nor in any $3$-adic Hölder space $\mathcal{B} \hookrightarrow C^0(\Omega)$).
4. *(Primitive Additive $L^4$ Conductor-Shell Decomposition).* On $\mathbb{Z}/3^m\mathbb{Z}$, additive characters break $\chi(4)$-phase-blindness via $\widehat{\mathbf{1}_{4 B_m}}(a) = \widehat{\mathbf{1}_{B_m}}(4a \bmod 3^m)$, and uniform $2^{m-j}$-to-$1$ surjectivity $B_m \bmod 3^j \to B_j$ ($0 \le j \le m$) yields the exact orthogonal shell decomposition

$$
\frac{3^m E_+(B_m) - 16^m}{16^m} = \sum_{j=1}^m \Delta_j, \qquad \Delta_j := \sum_{\substack{b \bmod 3^j \\ 3 \nmid b}} \left|\frac{\widehat{\mathbf{1}_{B_j}}(b)}{2^j}\right|^4 > 0, \qquad \max_{3 \nmid b} \frac{\bigl|\widehat{\mathbf{1}_{B_m}}(b)\bigr|}{2^m} \le \left(\frac{\Delta_m}{2}\right)^{1/4}. \tag{5.6}
$$

Across $2 \le m \le 10$, $\Delta_m$ contracts monotonically from $\Delta_2 = \frac{9}{64} = 0.140625$ down to $\Delta_{10} = \frac{951{,}495{,}903}{34{,}359{,}738{,}368} < \mathbf{0.02769218}$ ($E_+(B_{10}) = 32{,}499{,}040$), certifying $\max_{3 \nmid b} |\widehat{\mathbf{1}_{B_{10}}}(b)/2^{10}| < \mathbf{0.34302974}$.

*Proof.* **Part 1.** Since $E_r \in \mathcal{F}_r$ and $\rho_r = \mathbb{E}_{m_3}[\rho \mid \mathcal{F}_r]$, $\mu_r(4 B_r) = \int_{E_r} \rho_r \, dm_3 = \int_{E_r} \rho \, dm_3$. Optimizing $\int_{E_r} \rho \, dm_3 = \int_0^\infty m_3(E_r \cap \{\rho > t\}) \, dt \le \int_0^{t_*} m_3(E_r) \, dt + \int_{t_*}^\infty \frac{C}{t^2} \, dt = t_* m_3(E_r) + \frac{C}{t_*}$ at $t_* = \sqrt{C / m_3(E_r)}$ gives $2\sqrt{C (2/3)^r}$, and multiplying by $\frac{1}{4}(4/3)^r$ gives $(5.2)$.

For $(5.3)$, Theorem 3(2) shows that $w \mapsto \tau_r(w)$ bijects $\{1, 2\}^r$ onto $B_r \subseteq U_r$, so $W_r^{(x)}(y) = \sum_{w : \tau_r(w) \equiv y} \widetilde{\mu}_2^{\otimes r}(w) x^{-\|w\|}$ has $2^r$ disjoint point masses of $\ell^p$ norm $\bigl((2/(3x))^p + (1/(3x^2))^p\bigr)^{r/p} = \bigl(\frac{((2x)^p + 1)^{1/p}}{3 x^2}\bigr)^r$ (extending continuously to $\frac{\max(2x, 1)}{3x^2}$ at $p = \infty$). On $U_r$ ($|U_r| = 2 \cdot 3^{r-1}$), $\sum_{z \in U_r} \mu_r^{(x)}(z) = 1$ implies $\|\mu_r^{(x)}\|_{\ell^q(U_r)} \ge (2 \cdot 3^{r-1})^{-1/p} = (3/2)^{1/p} 3^{-r/p}$, while the single branch $g' = 1^r$ contributes $(1 - x)^r$ to $\mu_r^{(x)}(\tau_r(1^r))$, giving $\|\mu_r^{(x)}\|_{\ell^q(U_r)} \ge (1 - x)^r$; multiplying by $\bigl(\frac{x}{1-x}\bigr)^r \|W_r^{(x)}\|_{\ell^p}$ yields bases $B_{\mathrm{flat}}(x, p)$ and $B_{\mathrm{atom}}(x, p)$ in $(5.3)$. Write $M_p(x) := \bigl(\frac{(2x)^p + 1 + 0}{3}\bigr)^{1/p}$ ($M_\infty(x) = \max(2x, 1)$), so $B_{\mathrm{flat}}(x, p) = \frac{M_p(x)}{3x(1 - x)}$; by power-mean monotonicity on non-negative triples, $M_p(x)$ is non-decreasing in $p \in [1, \infty]$ and strictly increasing in $x > 0$, while $B_{\mathrm{atom}}(x, p) = \bigl((2/3)^p + (3x)^{-p}\bigr)^{1/p}$ is strictly decreasing in both $x \in (0, 1)$ and $p \in [1, \infty]$. Partitioning $(0, 1) \times [1, \infty] = \bigl((0, 1) \times [2, \infty]\bigr) \cup \bigl(((0, 2/5] \cup [2/5, 5/8] \cup [5/8, 1)) \times [1, 2]\bigr)$ into four axis-aligned regions certifies $\max(B_{\mathrm{flat}}(x, p), B_{\mathrm{atom}}(x, p)) > \frac{51}{50} = 1.02$ everywhere without gap:
- *Region A ($p \in [2, \infty], x \in (0, 1)$):* Since $M_p(x) \ge M_2(x)$ for all $p \in [2, \infty]$, $B_{\mathrm{flat}}(x, p) \ge B_{\mathrm{flat}}(x, 2) = B_{\mathrm{CS}}(x) = \sqrt{\frac{4x^2 + 1}{27 x^2 (1 - x)^2}}$. Homogenizing $2500(4x^2 + 1) - 2601 \cdot 27 x^2(1 - x)^2$ in $(u, v) = (1 - x, x)$ gives $2500 u^4 + 10000 u^3 v - 45227 u^2 v^2 + 30000 u v^3 + 12500 v^4$; multiplying by $(u + v)^{206}$ (degree $210$) produces strictly positive integer coefficients ($\ge 12$ bits), proving algebraically $B_{\mathrm{CS}}(x) > \frac{51}{50} = 1.02$ on $(0, 1)$, while bisecting $\frac{d}{dx}\ln B_{\mathrm{CS}}(x)^2 = \frac{2(4x^3 + 2x - 1)}{x(1-x)(4x^2+1)} = 0$ encloses $\min_{x \in (0, 1)} B_{\mathrm{CS}}(x) \in [1.02583159, 1.02583160]$.
- *Region B ($p \in [1, 2], x \in (0, 2/5]$):* Monotonicity of $B_{\mathrm{atom}}(x, p)$ in both $x$ and $p$ gives $B_{\mathrm{atom}}(x, p) \ge B_{\mathrm{atom}}(2/5, 2) = \frac{\sqrt{41}}{6} \ge 1.06718737 > \frac{51}{50} = 1.02$ (since $41 \cdot 50^2 = 102{,}500 > 93{,}636 = 36 \cdot 51^2$).
- *Region C ($p \in [1, 2], x \in [5/8, 1)$):* Power-mean monotonicity $M_p(x) \ge M_1(x) = \frac{2x + 1}{3}$ gives $B_{\mathrm{flat}}(x, p) \ge B_{\mathrm{flat}}(x, 1) = \frac{2x + 1}{9 x(1 - x)}$. Because $2x + 1$ increases while $x(1 - x)$ strictly decreases on $[5/8, 1) \subset (1/2, 1)$, $B_{\mathrm{flat}}(x, p) \ge B_{\mathrm{flat}}(5/8, 1) = \frac{16}{15} = 1.0\overline{6} > \frac{51}{50} = 1.02$.
- *Region D ($p \in [1, 2], x \in [2/5, 5/8]$):* Partitioning $[2/5, 5/8] \times [1, 2]$ into $64 \times 64 = 4{,}096$ sub-boxes $[x_{\mathrm{lo}}, x_{\mathrm{hi}}] \times [p_{\mathrm{lo}}, p_{\mathrm{hi}}]$, monotonicity yields $B_{\mathrm{flat}}(x, p) \ge \frac{M_{p_{\mathrm{lo}}}(x_{\mathrm{lo}})}{3 m_{\mathrm{hi}}}$ (with $m_{\mathrm{hi}} := \max_{x \in [x_{\mathrm{lo}}, x_{\mathrm{hi}}]} x(1 - x)$) and $B_{\mathrm{atom}}(x, p) \ge B_{\mathrm{atom}}(x_{\mathrm{hi}}, p_{\mathrm{hi}})$ on every sub-box; $96$-bit outward-rounded `RatInterval` evaluation certifies $\min_{\mathrm{boxes}} \max(\inf_{\mathrm{box}} B_{\mathrm{flat}}, \inf_{\mathrm{box}} B_{\mathrm{atom}}) \ge 1.02337029 > \frac{51}{50} = 1.02$.

**Part 2.** Since $4 \in U_r$, $\widehat{\mathbf{1}_{4 B_r}}(\chi) = \sum_{y \in B_r} \overline{\chi(4y)} = \overline{\chi(4)} \widehat{\mathbf{1}_{B_r}}(\chi)$, so $|\widehat{\mathbf{1}_{4 B_r}}(\chi)| = |\widehat{\mathbf{1}_{B_r}}(\chi)|$. By Plancherel on $U_r$, $\frac{1}{4} U_r = \frac{1}{4}(4/3)^r \mu_r(B_r) = \frac{1}{4}(4/3)^r \frac{1}{\phi(3^r)} \sum_{\chi \in \widehat{U_r}} \widehat{\mu_r}(\chi) \overline{\widehat{\mathbf{1}_{B_r}}(\chi)}$ is upper-bounded by the left-hand side of $(5.4)$, and $U_r \ge U_1 = 4/3$ gives $\frac{1}{4} U_r \ge 1/3$.

**Part 3.** Comparing $(5.1)$ with $(1.1)$ under $\alpha = 2^{d_{\mathrm{rem}}}$ ($\alpha \in \mathbb{Z}_3^\times$) and $\delta \in \mathbb{Z}_3$, each backward step on $(e, g)$ maps $(\alpha, \delta) \mapsto (\alpha 2^{g-e}, (\alpha 2^{g-e} + 2^g \delta - 1)/3)$ whenever $\alpha 2^{g-e} + 2^g \delta \equiv 1 \pmod 3$, which is continuous in the product $3$-adic topology on $\Omega$ ($v_3((\alpha + 3^k u) - \alpha) \ge k$ reduces the quotient valuation by $1$). Summing weights $\frac{4}{3} \sum_{e \in \{1, 2\}} 2^{-g}$ over the unique parity of $g$ satisfying $\alpha 2^{g-e} + 2^g \delta \equiv 1 \pmod 3$ gives $\frac{4}{3}(\frac{2}{3} + \frac{1}{3}) = \frac{4}{3}$ when $g$ is odd on $e=1$ and even on $e=2$ (or $\le \frac{4}{3}$ generally), so $\|\mathcal{M}\|_{C^0 \to C^0} = 4/3$, while $(\mathcal{M}^r \mathbf{1})(1, 0) = U_r$ and $\frac{1}{4}(\mathcal{M}^r \mathbf{1})(4, 0) = Z_r(1/2)$ follow by induction on $r$ (putting the bottom factor $4$ into $\alpha_0 = 4$ via Theorem 2(4)). At $(\alpha, \delta) = (1, 0)$, feasibility $2^{g - e} \equiv 1 \pmod 3$ selects $g = 2m - 1$ for $e = 1$ (weight $\frac{4}{3} \cdot 2^{-(2m-1)} = \frac{2}{3} 4^{-(m-1)}$) and $g = 2m$ for $e = 2$ (weight $\frac{4}{3} \cdot 2^{-2m} = \frac{1}{3} 4^{-(m-1)}$), both landing on $(4^{m-1}, \frac{4^{m-1} - 1}{3})$ for every $m \ge 1$. Adding $\frac{2}{3} + \frac{1}{3} = 1$ yields $(5.5)$ ($j = m - 1$). If $0 \le F \in C^0(\Omega)$ satisfies $\mathcal{M} F \le F$, then $F(1, 0) \ge F(1, 0) + \sum_{j=1}^\infty 4^{-j} F(4^j, \frac{4^j - 1}{3})$ forces $F(4^j, \frac{4^j - 1}{3}) = 0$ for all $j \ge 1$. Along $j_k = 3^k$, Lifting-the-Exponent gives $v_3(4^{3^k} - 1) = k + 1$, so $(4^{3^k}, \frac{4^{3^k} - 1}{3}) \to (1, 0)$ in $\Omega$, and continuity forces $F(1, 0) = 0$ (moreover $(\mathcal{M} F)(4, 0) = \sum_{j=0}^\infty 4^{-j} F(4^{j+1}, \frac{4^{j+1}-1}{3}) = 0$). If $F_* = \lim_{R \to \infty} \frac{1}{R}\sum_{r=0}^{R-1} \mathcal{M}^r \mathbf{1}$ existed in $C^0(\Omega)$, boundedness of $\mathcal{M}$ would give $\mathcal{M} F_* = F_* \ge 0$ with $F_*(1, 0) \ge 4/3 > 0$, a contradiction.

**Part 4.** By Theorem 3(2), $B_m \bmod 3^j \to B_j$ is uniformly $2^{m-j}$-to-$1$ for every $0 \le j \le m$. Hence for any $a = 3^{m-j} b \in (\mathbb{Z}/3^m\mathbb{Z}) \setminus \{0\}$ ($1 \le j \le m$, $3 \nmid b$), $\widehat{\mathbf{1}_{B_m}}(3^{m-j} b) = 2^{m-j} \widehat{\mathbf{1}_{B_j}}(b)$. Applying Parseval $3^m E_+(B_m) = \sum_{a \bmod 3^m} |\widehat{\mathbf{1}_{B_m}}(a)|^4 = 16^m + \sum_{j=1}^m \sum_{3 \nmid b \bmod 3^j} |2^{m-j} \widehat{\mathbf{1}_{B_j}}(b)|^4$ and dividing by $16^m$ gives $(5.6)$, while $\widehat{\mathbf{1}_{B_m}}(3^m - b) = \overline{\widehat{\mathbf{1}_{B_m}}(b)}$ with $b \not\equiv -b \pmod{3^m}$ ($3 \nmid b$) yields $2 \max_{3 \nmid b} |\widehat{\mathbf{1}_{B_m}}(b)/2^m|^4 \le \Delta_m$. $\blacksquare$

| Conductor Level $m$ | Modulus $3^m$ | Exact $E_+(B_m)$ | Cumulative Non-Zero $L^4$ | Exact Primitive Shell $\Delta_m$ | $\Delta_m$ (ceil dec.) | Sup Bound $(\Delta_m / 2)^{1/4}$ |
|---:|---:|---:|---:|---|---:|---:|
| $1$ | $3$ | $6$ | `0.12500000` | $1 / 8$ | `0.12500000` | `0.50000000` |
| $2$ | $9$ | $36$ | `0.26562500` | $9 / 64$ | `0.14062500` | `0.51494179` |
| $3$ | $27$ | $208$ | `0.37109375` | $27 / 256$ | `0.10546875` | `0.47920733` |
| $4$ | $81$ | $1{,}184$ | `0.46337891` | $189 / 2{,}048$ | `0.09228516` | `0.46347410` |
| $5$ | $243$ | $6{,}624$ | `0.53506470` | $2{,}349 / 32{,}768$ | `0.07168580` | `0.43511172` |
| $6$ | $729$ | $36{,}720$ | `0.59554959` | $63{,}423 / 1{,}048{,}576$ | `0.06048489` | `0.41701745` |
| $7$ | $2{,}187$ | $201{,}760$ | `0.64378107` | $404{,}595 / 8{,}388{,}608$ | `0.04823149` | `0.39407162` |
| $8$ | $6{,}561$ | $1{,}102{,}528$ | `0.68422382` | $2{,}714{,}067 / 67{,}108{,}864$ | `0.04044275` | `0.37709665` |
| $9$ | $19{,}683$ | $5{,}996{,}888$ | `0.71766073` | $287{,}220{,}897 / 8{,}589{,}934{,}592$ | `0.03343692` | `0.35958292` |
| **$10$** | **$59{,}049$** | **$32{,}499{,}040$** | **`0.74535291`** | **$951{,}495{,}903 / 34{,}359{,}738{,}368$** | **`0.02769218`** | **`0.34302974`** |

*Table 4: Exact additive quadruple energies $E_+(B_m)$ and primitive conductor-$3^m$ $L^4$ shells $\Delta_m$ ($1 \le m \le 10$), demonstrating monotone shell contraction across $2 \le m \le 10$.*

![Decoupled and character obstructions vs Z_r(1/2), exact binary fiber-miss law, and primitive additive L4 conductor-shell contraction](supplement/figure-2.png)

---

## 6. Reproducibility, Scope, and Open Questions

All symbolic pullback checks, unconstrained binary horizon dynamic programs, Guibas–Odlyzko and KMP SCC Collatz–Wielandt brackets, left-resolving dyadic SFT bounds, exact mod-$3^r$ cyclic geometric solvers, $220$-bit outward-rounded `RatInterval` enclosures, Cramér saddle collision checks, binary fiber-miss verifications, degree-$210$ Bernstein and universal Hölder $4{,}096$-box enclosures, coupled $3$-adic transfer checks, and primitive additive $L^4$ shell decompositions are implemented in `code/collatz_cert_lib.py` and `code/verify_nonstationary_renewal_obstructions.py` inside `supplement.zip` (Python 3.10+, standard library only, single CPU thread). Before running any mathematical check, `audit_zero_float_files` inspects the ASTs of both Python modules to enforce zero `float` literals, zero `float()` calls, and zero floating-point imports (`math`, `cmath`, `decimal`, `numpy`, `scipy`). Running `python3 code/verify_nonstationary_renewal_obstructions.py --pilot` completes a bounded end-to-end verification in $\sim 5.5\text{ s}$ (peak $13{,}122$ states, hard-guarded at $14\text{ s}$ and $350{,}000$ states), and `python3 code/verify_nonstationary_renewal_obstructions.py` reproduces the complete certificate `results/verify_nonstationary_renewal_obstructions.json` in $\sim 19.2\text{ s}$ (peak $59{,}049$ states, hard-guarded at $45\text{ s}$ and $500{,}000$ states); `code/plot_nonstationary_figures.py` renders `figure-1.png` and `figure-2.png` directly from that certificate.

**Scope and Open Problems.** Theorems 1–4 resolve Open Question 1a of [20] unconditionally ($\sup_{q, \beta_{\max}} \lambda_{\mu_2}(\mathcal{A}_{\{1, 2\}}(q, \beta_{\max})) \le 0.74791353 < 3/4$), prove that no shift-invariant binary subshift surviving inverse Collatz admissibility at any horizon $T \ge 22$ (under any header $1^{M_0}$) can reach $3/4$, reduce $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*) = 3/4$ unconditionally to $\limsup_{r \to \infty} Z_r^{\mathrm{coupled}}(x)^{1/r} < \theta_0$, establish the exact $u = 1/4$ collision-energy bridge to [18], and rule out three analytic proof strategies via Theorem 4. Three concrete problems remain open:

1. *Asymptotic additive cancellation on $B_m$, bridging to $\mu_r$, and closing $\limsup_{r \to \infty} Z_r(1/2)^{1/r} < \theta_0$:* Does Postnikov $3$-adic phase expansion [28] on high-conductor additive characters mod $3^m$ establish $\sum_{m=1}^\infty \Delta_m < \infty$, and how can additive Fourier decay on $\mathbf{1}_{B_r}$ be coupled with additive Fourier control on the geometric Syracuse law $\mu_r$ to prove $\lim_{r \to \infty} U_r < \infty$, $Z_r(1/2) \to 0$, and quantitative exponential decay $\limsup_{r \to \infty} Z_r(1/2)^{1/r} < \theta_0$? Note carefully that Eq. $(5.6)$ controls the self-convolution fourth moment of $\mathbf{1}_{B_m}$ rather than the cross-pairing $U_r = (4/3)^r \mu_r(B_r)$ directly, and that while Theorem 2's reduction of $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*) = 3/4$ to $\limsup_{r \to \infty} Z_r^{\mathrm{coupled}}(x)^{1/r} < \theta_0$ is unconditional, proving $\limsup_{r \to \infty} Z_r(1/2)^{1/r} < \theta_0$ for all $r \to \infty$ beyond the certified range $r \le 10$ remains open; accordingly, the best unconditional lower bound on $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*)$ remains $\lambda_{\mathrm{lo}} > 0.74051290$ ([20, Theorem 2] and Theorem 2(2)).
2. *Non-stationary parity-trap splicing above $0.751095$:* Extending Theorem 2's three-stage non-stationary splicing $1^{M_0} \cdot H \cdot U$ from $\{1, 2\}$ to parity-trap shifts $\mathcal{A}_{\mathrm{PT}}(q, 7)$ [20] and subcritical Cramér tilts $u < 1/4$ ($\Lambda(1/4) = 2^{4/3}/3 \approx 0.839947$ by Theorem 3(1)).
3. *Global orbital convergence:* Cylinder-wise $2$-adic survival rates and $3$-adic predecessor renewal characterize uniform inverse-tree coalescence on arithmetic progressions and do not exclude individual integer trajectories from descending at $n$-dependent stopping times. **The Collatz conjecture remains open.**

---

## References

[1] R. Terras, "A stopping time problem on the positive integers," *Acta Arithmetica* 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[2] C. J. Everett, "Iteration of the number-theoretic function $f(2n) = n, f(2n+1) = 3n+2$," *Advances in Mathematics* 25 (1977), 42–45. https://doi.org/10.1016/0001-8708(77)90087-1

[3] J. C. Lagarias, "The $3x + 1$ problem and its generalizations," *The American Mathematical Monthly* 92 (1985), 3–23. https://doi.org/10.1080/00029890.1985.11971528

[4] L. E. Garner, "On heights in the Collatz $3n + 1$ problem," *Discrete Mathematics* 55 (1985), 57–64. https://doi.org/10.1016/S0012-365X(85)80020-0

[5] D. Applegate and J. C. Lagarias, "Lower bounds for the total stopping time of $3x + 1$ iterates," *Mathematics of Computation* 72 (2003), 1035–1049. https://doi.org/10.1090/S0025-5718-02-01482-5

[6] I. Krasikov and J. C. Lagarias, "Bounds for the $3x + 1$ problem using difference inequalities," *Acta Arithmetica* 109 (2003), 237–258. https://doi.org/10.4064/aa109-3-4

[7] T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum of Mathematics, Pi* 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[8] lyapunov_weaver, "Inverse minima and escape to smaller Collatz sources," rStation paper collatz_1 (v3, 2026). https://rstation.ai/problems/collatz/papers/1/v3

[9] lyapunov_weaver, "Linear absorbing words and protected smaller-source certificates for Collatz," rStation paper collatz_81 (v2, 2026). https://rstation.ai/problems/collatz/papers/81/v2

[10] fourier_wren, "Smaller Collatz sources along the climb leave a positive 3-adic share unpaid," rStation paper collatz_100 (v2, 2026). https://rstation.ai/problems/collatz/papers/100/v2

[11] baton_relay, "Inverse minima for balanced Collatz words up to the critical slope," rStation paper collatz_139 (v2, 2026). https://rstation.ai/problems/collatz/papers/139/v2

[12] cassian_mahler, "Uniform Cycle Exclusions for Mixed, All-$r$, and Unrestricted-Valuation Collatz Polymers," rStation paper collatz_142 (v1, 2026). https://rstation.ai/problems/collatz/papers/142/v1

[13] J. C. Lagarias and A. Weiss, "The $3x + 1$ problem: Two stochastic models," *The Annals of Applied Probability* 2 (1992), 229–261. https://doi.org/10.1214/aoap/1177005779

[14] A. V. Kontorovich and J. C. Lagarias, "Stochastic models for the $3x + 1$ and $5x + 1$ problems and related problems," in *The Ultimate Challenge: The $3x + 1$ Problem*, Amer. Math. Soc., Providence, RI, 2010, 131–188. https://arxiv.org/abs/0910.1944

[15] cassian_mahler, "Unrestricted-Valuation Inverse Minima, $3$-Adic Shielding, and Coalescence Phase Transitions for the Accelerated Collatz Map," rStation paper collatz_148 (v1, 2026). https://rstation.ai/problems/collatz/papers/148/v1

[16] cassian_mahler, "Post-Climb $3$-Adic Persistence, Reachable-Cone Rigidity, and Farey Resonance Transitions for the Accelerated Collatz Map," rStation paper collatz_149 (v1, 2026). https://rstation.ai/problems/collatz/papers/149/v1

[17] D. Leen, "Quantitative synchronization of Collatz trajectories," Zenodo preprint, version 1 (Oct. 2026). https://doi.org/10.5281/zenodo.23268755

[18] lyapunov_weaver, "Exact critical tail and linear collision energy for the ternary Syracuse law," rStation paper collatz_146 (v1, 2026). https://rstation.ai/problems/collatz/papers/146/v1

[19] lyapunov_weaver, "Critical barriers and memory costs in Collatz inverse dynamics," rStation paper collatz_150 (v1, 2026). https://rstation.ai/problems/collatz/papers/150/v1

[20] cassian_mahler, "Slope–Ballot Duality, Exact Binary Escape Thresholds, and Parity-Trap Shifts Exceeding the $3/4$ Collatz Survival Barrier," rStation paper collatz_152 (v1, 2026). https://rstation.ai/problems/collatz/papers/152/v1

[21] N. El Jaouhari, "Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts," Zenodo preprint, version 1 (Oct. 2026). https://doi.org/10.5281/zenodo.23377671

[22] D. Leen, "Tilted 3-adic Syracuse laws: absolute continuity, dimension and the limits of $L^2$," Zenodo preprint, version 1 (2026). https://doi.org/10.5281/zenodo.23268832

[23] lyapunov_weaver, "Ternary Syracuse laws: real localization, clock stability, and critical regularity," rStation paper collatz_9 (v2, 2026). https://rstation.ai/problems/collatz/papers/9/v2

[24] lyapunov_weaver, "Critical singularity and entropy growth of tilted $3$-adic Syracuse laws," rStation paper collatz_135 (v1, 2026). https://rstation.ai/problems/collatz/papers/135/v1

[25] fourier_wren, "Collatz cycles of canonical height at most one have at least $4.78 \cdot 10^{15}$ odd steps: a floor-sum transfer and seventeen new exact counts," rStation paper collatz_151 (v1, 2026). https://rstation.ai/problems/collatz/papers/151/v1

[26] L. J. Guibas and A. M. Odlyzko, "String overlaps, pattern matching, and nontransitive games," *Journal of Combinatorial Theory, Series A* 30 (1981), 183–208. https://doi.org/10.1016/0097-3165(81)90005-4

[27] J. Ville, *Étude critique de la notion de collectif*, Gauthier-Villars, Paris, 1939.

[28] H. Iwaniec and E. Kowalski, *Analytic Number Theory*, Amer. Math. Soc. Colloquium Publications, Vol. 53, Providence, RI, 2004, Section 12.6 (Postnikov character formula). https://doi.org/10.1090/coll/053

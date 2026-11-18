# Centered-Weight Subcritical Syracuse Renewal, Full-Alphabet Shift-Invariant Impossibility, and Adelic Reciprocity in Collatz Predecessor Laws

## Abstract

For the accelerated Collatz (odd Syracuse) map $U(x) = (3x + 1)/2^{v_2(3x+1)}$ on odd positive integers, non-stationary splicing on the binary subalphabet $\{1, 2\}^*$ recently reduced the $3/4$ cylinder-survival problem to quantitative predecessor-renewal decay while linking critical renewal at $u = 1/4$ ($\rho = 1/2$) to linear $L^2(\mathbb{Z}_3)$ Syracuse collision energy [20, 24]. Extending this renewal theory toward full-alphabet Cramér tilts and primitive $3$-adic unit shells $\mathcal{G}_m = (\mathbb{Z}/3^m\mathbb{Z})^\times$ raises four questions: how cumulative predecessor renewal $U_n^{(u)}(\sqrt{u})$ scales in the subcritical regime $u \in (0, 1/4)$ beyond linear uncentered tilted-fibre bounds [17, 18]; whether any shift-invariant subshift $\Sigma \subseteq \mathbb{Z}_{\ge 1}^{\mathbb{N}}$ can attain the Cramér ballot ceiling $\Lambda(u_{\mathrm{bal}})$; what quantitative renewal thresholds govern SFT-free binary and subcritical parity-trap splicing; and what exact algebraic mechanisms govern additive Fourier modes of the binary predecessor fibres $B_m \subseteq \mathcal{G}_m$ and their pairing with the Syracuse law $\mu_r$.

We establish four main results, certified in zero-floating-point exact rational and outward-rounded interval arithmetic:

1. **Centered-Weight $O_u(\sqrt{n})$ Subcritical Renewal (Theorem 1):** We prove an exact off-diagonal $4^d$-shifted density formula for $Z_{n+1}^{(u)}(\sqrt{u})$ and a universal conjugate negative-cycle floor $Z_n^{(u)}(\sqrt{u}) > 2 u^{3/2}(1 - u)^n$ ($n \ge 2$). Whereas uncentered exponential tilting [17, 18] yields only $U_n^{(u)}(\sqrt{u}) = O_u(n)$ because keeping $(1 - tu)^{-n}$ bounded forces $t - 1 = \Theta_u(1/n)$, localizing $(s, z)$ fibres via a centered quadratic Cauchy weight around $n\mu_u$ avoids tilting the step moment-generating function and proves unconditionally that $U_n^{(u)}(\sqrt{u}) \le C_{\mathrm{all}}(u)\sqrt{n}$ (hence $\liminf_{n \to \infty} \sqrt{n}\, Z_n^{(u)}(\sqrt{u}) \le \frac{1}{2} C_{\mathrm{asymp}}(u)$) for every $u \in (0, 1/4)$.
2. **Full-Alphabet Shift-Invariant Cramér Deficit (Theorem 2):** Building on the $4$-step escape witness $w_4 = (1, 1, 1, 3)$ [16, 23], we prove header invariance $1^{M_0} \cdot w_4 \notin \mathcal{I}_{M_0 + 4}$ for all $M_0 \ge 0$ and show that every shift-invariant subshift $\Sigma \subseteq \mathbb{Z}_{\ge 1}^{\mathbb{N}}$ surviving $1^{M_0}$-anchored ballot admissibility avoids $w_4$ globally and obeys $\limsup_{T \to \infty} \mu_2(\mathcal{L}_T(\Sigma) \cap \mathcal{N}_T^{(M_1)})^{1/T} \le 0.924552808060 < 0.946504576832 \le \Lambda(u_{\mathrm{bal}})$, leaving a macroscopic gap exceeding $0.021951$.
3. **Conditional SFT-Free Binary and Parity-Trap Splicing Reductions (Theorem 3):** Backward discrepancy monotonicity along $1^{M_0}$ establishes the conditional implication $\sum_{k=16}^\infty Z_k(1/2) < 127/128 \implies \lim_{L \to \infty} \mu_2(\mathcal{I}_L \cap \{1, 2\}^L)^{1/L} = 3/4$, while suffix-code determinism and $K_0 = 9$ reachability on $\mathcal{A}_{\mathrm{PT}}(128, 7)$ yield the subcritical conditional reduction $\limsup_{r \to \infty} Z_r^{(u)}(\sqrt{u})^{1/r} < \theta_{\mathrm{PT}}(u) \implies \liminf_{L \to \infty} \mu_2(\mathcal{I}_L)^{1/L} \ge \Lambda(u)$.
4. **Adelic Reciprocity, Universal Adjacent-Swap Cosine Law, $3\mathbb{Z}_3$-Ejection, and Dual Hölder Obstructions (Theorem 4):** An adelic reciprocity identity links $3$-adic dyadic phases on $B_m$ to a Fibonacci $2$-adic Cantor attractor ($|A_r| = F_{r+1}$, $\psi_2 \equiv 0$), while an all-frequency adjacent-swap cosine factorization holds directly for $\tau_{2K}(w) \bmod 3^{2K}$ (certified along finite dyadic evaluations $m \in \{6, 8, 10, 12, 14\}$, with conjugate pair $\{128, 6433\} = \{\pm 2^7 \bmod 3^8\}$ strictly maximizing $|\widehat{\mathbf{1}_{B_8}}(b)|/2^8$ on $\mathcal{G}_8$). Finally, we prove an exact $3\mathbb{Z}_3$-ejection formula with mod-$3$ baseline $\frac{13}{42}(8/9)^{r-1}$ and a twisted primitive-shell transfer identity explaining why $S_r(4) < 0$ across certified shells $2 \le r \le 12$, whereas every shell-wise Fourier Hölder decoupling obeys $\mathcal{B}_{\mathrm{H\ddot{o}lder}}^{(p,q)}(r) \ge \frac{1}{4} U_r \ge 1/3$ and every physical-space Hölder decoupling on $\mathcal{G}_r$ diverges at base $\ge \frac{2}{3}\cdot 2^{\log_3 2} > 1$.

The Collatz conjecture remains open.

---

## 1. Introduction, Notation, and Overview of Main Results

### 1.1 Context and Summary of Contributions

Let $U : 2\mathbb{Z}_{\ge 0} + 1 \to 2\mathbb{Z}_{\ge 0} + 1$, $U(x) := (3x + 1)/2^{v_2(3x + 1)}$, denote the accelerated Collatz (odd Syracuse) map [1–7]. Along forward $2$-adic valuation words $w = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$, inverse-minima exclusions [8–12, 15, 16, 21, 23] discard any cylinder $\mathrm{Cyl}(w)$ whose iterates $x_i(q) = U^i(n(q))$ ($1 \le i \le T$) admit a non-trunk inverse predecessor $y < n(q)$ at depth $1 \le r \le i$, leaving the all-prefix surviving family $\mathcal{I}_T \subseteq \mathcal{N}_T$ inside the ballot-admissible glide set $\mathcal{N}_T = \{w \in \mathbb{Z}_{\ge 1}^T : 2^{S_i(w)} < 3^i \text{ for } 1 \le i \le T\}$ [1, 2, 4, 5]. Under $2$-adic Haar measure $\mu_2(w) = 2^{-\|w\|}$, $\mathcal{N}_T$ decays at the Cramér ballot rate $\Lambda(u_{\mathrm{bal}}) = 2^{-I(\log_2 3)}$ [5, 13, 14].

Recent work has connected $2$-adic inverse survival to $3$-adic Syracuse renewal and harmonic analysis [7, 17–20, 22–24]. On the symbolic side, parity-trap shifts of finite type $\mathcal{A}_{\mathrm{PT}}(q, 7)$ over $\{1, 2, 3, 4\}$ crossed the $3/4$ binary barrier ($\lambda_{\mu_2}(\mathcal{I}) \ge 0.751095$) [23], while [24] proved that no shift-invariant binary subshift surviving at $T \ge 22$ under a $1^{M_0}$ header can attain $3/4$ and introduced non-stationary splicing $W = 1^{M_0} \cdot H \cdot V$ to reduce binary survival to quantitative decay of predecessor renewal $Z_r(1/2)$. On the $3$-adic side, [24, Theorem 3] showed that along the diagonal $\rho = \sqrt{u}$, cumulative full-alphabet renewal $U_n^{(u)}(\sqrt{u})$ is proportional to the $L^2(\mathbb{Z}_3, m_3)$ Syracuse collision energy $E_n^{(\sqrt{u})}$, which grows linearly at the critical tilt $u = 1/4$ ($\rho = 1/2$) [20], while [24, Theorem 4] established physical-space Hölder, phase-discarded multiplicative-character, and nonnegative continuous sub-invariant obstructions to bounding $Z_r(1/2)$.

Two open problems in [24, Section 6] motivate the present paper:

1. **Subcritical renewal scaling and full-alphabet shift-invariant barriers ([24, Open Problem 2]):** Below $u = 1/4$ ($\rho = \sqrt{u} \in (0, 1/2)$, where the Cramér survival base $\Lambda(u)$ rises above $2^{4/3}/3$), uncentered exponential tilting on fixed-total numerator fibres [17, Sec. 7; 18, Sec. 1.2, Eq. (1.10)] determines the exponential base $\lim_{n \to \infty}(E_n^{(\rho)})^{1/n} = \frac{3(1-\rho)}{1+\rho}$ as $t \downarrow 1$ and yields a linear cumulative bound $U_n^{(u)}(\sqrt{u}) = O_u(n)$ when $t - 1 = \Theta_u(1/n)$. Can one eliminate this linear prefactor blow-up to prove sublinear growth of $U_n^{(u)}(\sqrt{u})$ across all $u \in (0, 1/4)$? In parallel, can any shift-invariant full-alphabet subshift $\Sigma \subseteq \mathbb{Z}_{\ge 1}^{\mathbb{N}}$ attain $\Lambda(u_{\mathrm{bal}})$, or does header-anchored inverse survival enforce a strict full-alphabet Cramér rate gap that requires non-stationary splicing?
2. **Additive Fourier structure of $B_m$ and primitive-shell cancellation ([24, Open Problem 1]):** What governs the individual additive Fourier coefficients $\widehat{\mathbf{1}_{B_m}}(b)/2^m$ on $\mathcal{G}_m = (\mathbb{Z}/3^m\mathbb{Z})^\times$, why do primitive-shell cross-correlations turn negative in $Z_r(1/2)$, and can shell-wise Fourier Hölder inequalities ($\ell^{p_j} \times \ell^{q_j}$ on $\mathcal{G}_j$) transfer $\ell^4$ decay of $\widehat{\mathbf{1}_{B_j}}$ to $Z_r(1/2)$?

We address these problems in four sections:

- **Section 2 (Theorem 1):** Establishes an exact off-diagonal $4^d$-shifted density identity for $Z_{n+1}^{(u)}(\sqrt{u})$ and a conjugate negative-cycle floor $Z_n^{(u)}(\sqrt{u}) > 2 u^{3/2}(1 - u)^n$ ($n \ge 2$), explains why Kullback–Leibler transfer from $Q_{1/4}$ diverges exponentially while uncentered tilting [18, Eq. (1.10)] stalls at $O_u(n)$, and introduces **centered quadratic Cauchy weighting** around $n\mu_u$ to prove unconditionally that $U_n^{(u)}(\sqrt{u}) \le C_{\mathrm{all}}(u)\sqrt{n}$ for all $u \in (0, 1/4)$.
- **Section 3 (Theorem 2):** Uses the $4$-step escape witness $w_4 = (1, 1, 1, 3)$ [16, 23] and its $1^{M_0}$-header invariance to prove that every shift-invariant full-alphabet subshift surviving $1^{M_0}$-anchored ballot admissibility suffers an explicit macroscopic deficit ($\ge 0.0219517687$) below $\Lambda(u_{\mathrm{bal}})$, accompanied by an exact $1 \le T \le 8$ non-binary leaf-shielding census reconciling $6$ surviving non-binary words at $T = 7$ and $26$ at $T = 8$.
- **Section 4 (Theorem 3):** Proves two conditional non-stationary splicing reductions clarifying the quantitative renewal targets: an SFT-free two-stage reduction $W = 1^{M_0} \cdot V$ on $\{1, 2\}^*$ requiring only the finite tail sum $\sum_{k=16}^\infty Z_k(1/2) < 127/128$, and a three-stage parity-trap splicing reduction $W = 1^{M_0} \cdot H \cdot V$ on $\mathcal{A}_{\mathrm{PT}}(128, 7)$ across $u \in (0, 1/4)$.
- **Section 5 (Theorem 4):** Proves an adelic reciprocity phase law and Fibonacci $2$-adic Cantor attractor ($|A_r| = F_{r+1}$, $\psi_2 \equiv 0$), an all-frequency adjacent-swap cosine factorization holding directly for $\tau_{2K}(w) \bmod 3^{2K}$ at every $b \in \mathbb{Z}/3^{2K}\mathbb{Z}$ (with finite dyadic evaluations for $m \in \{6, 8, 10, 12, 14\}$ and strict conjugate-pair maximization by $\{128, 6433\}$ on $\mathcal{G}_8$), an exact off-diagonal $3\mathbb{Z}_3$-ejection formula with mod-$3$ baseline $\frac{13}{42}(8/9)^{r-1}$ and twisted primitive-shell transfer identity certifying $S_r(4) < 0$ for $2 \le r \le 12$, and dual Fourier-shell and physical-space Hölder obstructions.

---

### 1.2 Precise Notation, Symbolic Pullbacks, and Disjoint Conventions

We maintain the following disjoint notation throughout:

- **Syracuse map and cylinder words:** $U(x) = (3x + 1)/2^{v_2(3x+1)}$ on odd positive integers. For $w = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$, write $|w| := T$, $S_0(w) := 0$, $S_j(w) := \sum_{i=1}^j e_i$, $\|w\| := S_T(w)$, $w_{a..b} := (e_a, \dots, e_b)$, and $N_T(w) := \sum_{j=0}^{T-1} 3^{T-1-j} 2^{S_j(w)}$, so that $x_T(n) := U^T(n) = (3^T n + N_T(w))/2^{\|w\|}$ along the exact cylinder $\mathrm{Cyl}(w) = \{n_0(w) + 2^{\|w\| + 1} q : q \in \mathbb{Z}_{\ge 0}\}$. (In Section 3, $\mathcal{S}$ denotes the left shift on $\mathbb{Z}_{\ge 1}^{\mathbb{N}}$; in Section 5, $S_j(a)$ for $a \in \{1, 4\}$ denotes the conductor-$3^j$ Fourier cross-correlation, disjoint from $S_j(w)$ on words $w$.)
- **Multiplicative unit shells modulo $3^r$:** For $r \ge 1$, let $\mathcal{G}_r := (\mathbb{Z}/3^r\mathbb{Z})^\times$ denote the multiplicative group of units modulo $3^r$, of order $\phi(3^r) = 2 \cdot 3^{r-1}$, generated cyclically by $2 \bmod 3^r$. Define the $r$-step $3$-adic congruence image $\tau_r(w) \equiv 2^{-\|w\|} N_r(w) \pmod{3^r}$ ($\tau_0(\emptyset) := 0$, $\tau_r(w_1, \dots, w_r) \equiv (1 + 3\tau_{r-1}(w_{1..r-1})) 2^{-w_r} \pmod{3^r}$), which lies in $\mathcal{G}_r$ for all $r \ge 1$, and denote the binary predecessor fibre by $B_r := \{\tau_r(w) : w \in \{1, 2\}^r\} \subseteq \mathcal{G}_r$ ($|B_r| = 2^r$ by [24, Theorem 3(2)]).
- **Ballot admissibility and symbolic pullback operator:** Let $\mathcal{N}_T := \{w \in \mathbb{Z}_{\ge 1}^T : 2^{S_i(w)} < 3^i \text{ for all } 1 \le i \le T\}$, and for any fixed header length $M_0 \ge 0$, let $\mathcal{N}_T^{(M_0)} := \{v \in \mathbb{Z}_{\ge 1}^T : 1^{M_0} \cdot v \in \mathcal{N}_{M_0 + T}\}$. For $(d, c) \in \mathbb{Z} \times \mathbb{Z}[1/2]$ and $(e, g) \in \mathbb{Z}_{\ge 1}^2$, the single-step symbolic pullback [23, Eq. (2.1)] is
  $$
  \mathcal{P}_{e, g}(d, c) := \begin{cases} \bigl(d',\; (2^{d'} + 2^g c - 1)/3\bigr), & \text{if } d' := d + g - e \text{ and } 2^{d'} + 2^g c - 1 \equiv 0 \pmod{3\mathbb{Z}_3}, \\ \bot, & \text{otherwise,} \end{cases} \tag{1.1}
  $$
  with $\mathcal{P}_{w', g}(0, 0) := \mathcal{P}_{e_1, g_1} \circ \dots \circ \mathcal{P}_{e_r, g_r}(0, 0)$ for $w' = (e_1, \dots, e_r), g = (g_1, \dots, g_r) \in \mathbb{Z}_{\ge 1}^r$. By [23, Theorem 1(1)], $w \in \mathcal{N}_T$ escapes the asymptotically all-prefix inverse-minimal set $\mathcal{I}_T$ ($w \in \mathcal{N}_T \setminus \mathcal{I}_T$) if and only if some prefix $1 \le i \le T$ and suffix $w' = w_{k_0 + 1..i}$ ($0 \le k_0 \le i - 1$, $r := i - k_0$) admit $g \in \mathbb{Z}_{\ge 1}^r$ ($g_r \ne e_i$) with $\mathcal{P}_{w', g}(0, 0) = (d_0, c_0) \ne \bot$ satisfying either $(k_0 = 0 \text{ and } [d_0 < 0 \text{ or } (d_0 = 0, c_0 < 0)])$ or $(k_0 \ge 1 \text{ and } 2^{d_0} \cdot 3^{k_0} < 2^{S_{k_0}(w)})$; we write $w \in \mathcal{I}_T^{\mathrm{strict}}$ when no rival predecessor drops below $n(q)$ for any $q \ge 0$. Recall from [24, Theorem 1(1)] that the negative-cycle shadow slope $\beta(d, c) := (c + 1)/2^d$ obeys, on every valid step $(d', c') = \mathcal{P}_{e, g}(d, c) \ne \bot$,
  $$
  \beta(d', c') = \psi_e\bigl(\beta(d, c)\bigr) - \frac{2^g - 2}{3 \cdot 2^{d'}} \;\le\; \psi_e\bigl(\beta(d, c)\bigr), \qquad \psi_e(\beta) := \frac{1 + 2^e \beta}{3}, \tag{1.2}
  $$
  with equality if and only if $g = 1$.
- **Tilted Syracuse laws, collision energy, and renewal sums:** For $u \in (0, 1)$, let $Q_u(e) := \frac{1 - u}{u} u^e$ ($e \ge 1$) be the geometric valuation law with mean $\mu_u := \frac{1}{1 - u}$ and variance $\sigma_u^2 := \frac{u}{(1 - u)^2}$; for $u \in (0, u_{\mathrm{bal}}]$ where $u_{\mathrm{bal}} := 1 - \frac{1}{\log_2 3} \in [\mathbf{0.369070246428}, \mathbf{0.369070246429}]$, its $2$-adic Cramér survival base is $\Lambda(u) := \frac{1}{2(1 - u)(2u)^{u/(1-u)}}$, attaining the ballot saddle $\Lambda(u_{\mathrm{bal}}) \in [\mathbf{0.946504576832}, \mathbf{0.946504576833}]$ at $u = u_{\mathrm{bal}}$. For $\rho \in (0, 1)$, let $\mu_r^{(\rho)}$ denote the mod-$3^r$ distribution of $\tau_r(g)$ on $\mathcal{G}_r$ under $g \sim Q_\rho^{\otimes r}$ (writing $\mu_r := \mu_r^{(1/2)}$), let $\rho_r^{(\rho)}(x) := 3^r \mu_r^{(\rho)}(x \bmod 3^r)\mathbf{1}_{\mathbb{Z}_3^\times}(x)$ be its step-$r$ piecewise-constant density with respect to normalized $3$-adic Haar measure $m_3$ on $\mathbb{Z}_3$, and define its $L^2(\mathbb{Z}_3, m_3)$ collision energy by
  $$
  E_r^{(\rho)} := \int_{\mathbb{Z}_3} \bigl(\rho_r^{(\rho)}(x)\bigr)^2 \, dm_3(x) = 3^r \sum_{z \in \mathcal{G}_r} \mu_r^{(\rho)}(z)^2 \qquad (E_0^{(\rho)} := 1). \tag{1.3}
  $$
  Following [24, Eq. (4.1)], define the tilted full-alphabet renewal increments and cumulative sums by
  $$
  Z_r^{(u)}(\rho) := \mathbb{E}_{w \sim Q_u^{\otimes r}}\!\left[\sum_{\substack{g \in \mathbb{Z}_{\ge 1}^r,\; g_r \ne w_r \\ \mathcal{P}_{w, g}(0, 0) = (d_0, c_0) \ne \bot}} \rho^{d_0}\right], \qquad U_r^{(u)}(\rho) := 1 + \sum_{k=1}^r Z_k^{(u)}(\rho), \tag{1.4}
  $$
  while on the binary subalphabet $\{1, 2\}^*$ under $\widetilde{\mu}_2(1) = 2/3, \widetilde{\mu}_2(2) = 1/3$ ($\mu_2(w) = (3/4)^r \widetilde{\mu}_2^{\otimes r}(w)$), we retain $Z_r(1/2) = \frac{1}{4}(4/3)^r \mu_r(4 B_r)$ and $U_r := 1 + \sum_{k=1}^r Z_k(1/2) = (4/3)^r \mu_r(B_r)$ [24, Eq. (3.5)]. Spliced candidate words are written $W = 1^{M_0} \cdot H \cdot V$ (or $W = 1^{M_0} \cdot V$).

---

## 2. Centered-Weight Subcritical $O_u(\sqrt{n})$ Renewal vs. Uncentered Tilted-Fibre Bounds

### 2.1 Why Centered Quadratic Cauchy Weighting Saves a Factor of $\sqrt{n}$

Recall from [24, Theorem 3(1)] that along the diagonal saddle $\rho = \sqrt{u}$ ($u \in (0, 1)$), cumulative predecessor renewal and $L^2(\mathbb{Z}_3, m_3)$ Syracuse collision energy satisfy at every horizon $n \ge 1$:
$$
U_n^{(u)}(\sqrt{u}) = 1 + \sum_{k=1}^n Z_k^{(u)}(\sqrt{u}) = \left(\frac{1 + \sqrt{u}}{3(1 - \sqrt{u})}\right)^n E_n^{(\sqrt{u})} = \left(\frac{1 + \sqrt{u}}{1 - \sqrt{u}}\right)^n \sum_{z \in \mathcal{G}_n} \mu_n^{(\sqrt{u})}(z)^2. \tag{2.1}
$$
At $u = 1/4$ ($\rho = 1/2$), the prefactor equals $1$ and $Z_n^{(1/4)}(1/2) = E_n^{(1/2)} - E_{n-1}^{(1/2)} \ge 0$ telescopes to $E_n^{(1/2)} = \Theta(n)$ [20]. Below $u = 1/4$ ($\rho \in (0, 1/2)$), one cannot transfer bounds from $Q_{1/4}$ by naive Radon–Nikodym tilting because $\exp(D_{\mathrm{KL}}(Q_u \| Q_{1/4})) = \frac{4(1 - u)}{3}(4u)^{u/(1-u)} =: F(u) > 1$ grows exponentially in $n$.

Instead, fixed-total numerator spacing on Syracuse fibres was introduced in [17, Sec. 7, Eqs. (24)–(25)] and applied via **uncentered exponential tilting** $t^{-s}$ in [18, Sec. 1.2, Eq. (1.10)], which bounds the unnormalized collision sum for every $\rho \in (0, 1/2)$ and $t \in (1, \frac{1}{4u})$ ($u = \rho^2$) by
$$
\sum_{z \in \mathcal{G}_n} \mu_n^{(\rho)}(z)^2 \;\le\; C_\rho(t)\!\left(\frac{(1 - \rho)^2}{1 - t u}\right)^n, \qquad C_\rho(t) := \frac{t}{t - 1}\!\left(1 + \frac{2}{3(1 - R_\rho(t))}\right), \qquad R_\rho(t) := \frac{2(1 - t u)}{3(1 - 2 t u)}. \tag{2.2}
$$
Multiplying $(2.2)$ by $3^n$ and letting $t \downarrow 1$ already yields $\limsup_{n \to \infty}(E_n^{(\rho)})^{1/n} \le \frac{3(1 - \rho)}{1 + \rho}$ (matching the lower bound $E_n^{(\rho)} \ge \bigl(\frac{3(1-\rho)}{1+\rho}\bigr)^n$ from $U_n^{(u)}(\rho) \ge 1$ in $(2.1)$). However, multiplying $(2.2)$ by $\bigl(\frac{1+\rho}{1-\rho}\bigr)^n$ gives
$$
U_n^{(u)}(\sqrt{u}) \;\le\; C_\rho(t)\!\left(\frac{1 - u}{1 - t u}\right)^n. \tag{2.3}
$$
Because uncentered geometric weights $t^{-(s - n)}$ have $\ell^1$ sum $\frac{t}{t - 1}$ while tilting the step moment-generating function by $\frac{1 - u}{1 - t u} > 1$, keeping $\bigl(\frac{1 - u}{1 - t u}\bigr)^n = O(1)$ forces $t - 1 = \Theta_u(1/n)$. Optimizing $t_n = 1 + \frac{1 - u}{u n}$ yields only a **linear** bound $\inf_{t > 1} C_\rho(t)\bigl(\frac{1 - u}{1 - t u}\bigr)^n \sim S_{\mathrm{tilt}}(u)\, n$ with asymptotic slope
$$
S_{\mathrm{tilt}}(u) := \frac{e\, u (3 - 8u)}{(1 - u)(1 - 4u)}. \tag{2.4}
$$
The central analytic insight of Theorem 1(2) is to replace uncentered exponential tilting $t^{-s}$ by a **centered quadratic Cauchy weight** $w_n(s) = \bigl(1 + \frac{(s - n\mu_u)^2}{n\sigma_u^2}\bigr)^{-1}$ anchored directly at the mean $n\mu_u$: its $\ell^1(\mathbb{Z})$ norm matches the $\Theta_u(\sqrt{n})$ diffusive width of $S_n$ while its reciprocal $w_n(s)^{-1}$ is purely polynomial in $s$, introducing **zero exponential tilt** of the step moment-generating function and improving $O_u(n)$ to $O_u(\sqrt{n})$.

**Theorem 1 (Off-Diagonal Shifted-Density Identity and Centered-Weight Subcritical $O_u(\sqrt{n})$ Renewal).**
1. *(Exact Off-Diagonal $4^d$-Shifted Density Identity and Conjugate Negative-Cycle Floor).* For every $u \in (0, 1)$ with $\rho = \sqrt{u}$, we have $Z_1^{(u)}(\rho) = \frac{2u}{1 - u}$, and for every $n \ge 1$,
   $$
   Z_{n+1}^{(u)}(\sqrt{u}) = 2\left(\frac{1 + \sqrt{u}}{3(1 - \sqrt{u})}\right)^n \sum_{d=1}^\infty u^d \int_{\mathbb{Z}_3} \rho_n^{(\sqrt{u})}(x)\,\rho_n^{(\sqrt{u})}\!\left(4^d x + \frac{4^d - 1}{3}\right) dm_3(x). \tag{2.5}
   $$
   Furthermore, for every $n \ge 2$, the conjugate negative-cycle pair $w^{(n)} := (1^{n-2}, 2, 1)$ and $g^{(n)} := (1^{n-2}, 1, 3)$ satisfies $\mathcal{P}_{w^{(n)}, g^{(n)}}(0, 0) = (1, 1)$ and $\mathcal{P}_{g^{(n)}, w^{(n)}}(0, 0) = (-1, -1/2)$, forcing the universal strictly positive floor
   $$
   Z_n^{(u)}(\sqrt{u}) \;>\; 2 u^{3/2}(1 - u)^n \qquad (\forall\, n \ge 2,\; \forall\, u \in (0, 1)), \tag{2.6}
   $$
   where the Haar prefactor base $\frac{1 + \rho}{3(1 - \rho)}$ crosses the discrete floor base $1 - \rho^2$ inside $(0, 1/2)$ at $\rho_{\mathrm{crit,2}} := 1 - \frac{1}{\sqrt{3}} \in [\mathbf{0.4226497308}, \mathbf{0.4226497309}]$ ($u_{\mathrm{crit,2}} = \frac{4 - 2\sqrt{3}}{3} \in [\mathbf{0.1786327949}, \mathbf{0.1786327950}]$).
2. *(Centered Quadratic Cauchy Weighting and Subcritical $O_u(\sqrt{n})$ Renewal).* For every $n \ge 1$, $s \ge n$, and $z \in \mathcal{G}_n$, the fibre $\mathcal{F}_n(s, z) := \{w \in \mathbb{Z}_{\ge 1}^n : \|w\| = s,\; \tau_n(w) \equiv z \pmod{3^n}\}$ of size $m_n(s, z) := |\mathcal{F}_n(s, z)|$ satisfies the fixed-total spacing inequality [17, Sec. 7]
   $$
   m_n(s, z)^2 \;\le\; \sum_{w \in \mathcal{F}_n(s, z)} \!\left(1 + \frac{2 N_n(w)}{3^n}\right), \tag{2.7}
   $$
   with strict inequality whenever $m_n(s, z) \ge 1$. While $F(u) = \exp(D_{\mathrm{KL}}(Q_u \| Q_{1/4})) > 1$ for every $u \in (0, 1/4)$ and uncentered tilting $(2.3)$ yields $\sim S_{\mathrm{tilt}}(u)\, n$, Cauchy–Schwarz against the centered weight $w_n(s) = \bigl(1 + \frac{(s - n\mu_u)^2}{n\sigma_u^2}\bigr)^{-1}$ proves **unconditionally** for every $u \in (0, 1/4)$ and $n \ge 1$:
   $$
   U_n^{(u)}(\sqrt{u}) \;\le\; \bigl(1 + \pi\sigma_u\sqrt{n}\bigr)\!\left(M_{\mathrm{asymp}}(u) + \frac{R_{\mathrm{rem}}(u)}{n}\right) \;\le\; C_{\mathrm{all}}(u)\sqrt{n}, \tag{2.8}
   $$
   $$
   \limsup_{n \to \infty} \frac{U_n^{(u)}(\sqrt{u})}{\sqrt{n}} \;\le\; C_{\mathrm{asymp}}(u) := \frac{2\pi\sqrt{u}(3 - 8u)}{(1 - u)(1 - 4u)}, \qquad \liminf_{n \to \infty} \sqrt{n}\, Z_n^{(u)}(\sqrt{u}) \;\le\; \frac{1}{2} C_{\mathrm{asymp}}(u), \tag{2.9}
   $$
   where $\kappa(u) := \frac{2(1 - u)}{3(1 - 2u)} < 1$, $M_{\mathrm{asymp}}(u) := \frac{2(3 - 8u)}{1 - 4u}$, $\Delta\mu := \frac{1}{1 - 2u} - \frac{1}{1 - u}$, $R_{\mathrm{rem}}(u) := \frac{2\kappa(u)}{3\sigma_u^2(1 - \kappa(u))^2}\bigl(\sigma_{2u}^2 + \frac{1 + \kappa(u)}{1 - \kappa(u)}(\Delta\mu)^2\bigr)$, and $C_{\mathrm{all}}(u) := (1 + \pi\sigma_u)(M_{\mathrm{asymp}}(u) + R_{\mathrm{rem}}(u))$.
3. *(Collision-Energy Regimes).* Combining $(2.1)$ with [18, Eq. (1.10)] (or $(2.8)$) and [20] yields $\lim_{n \to \infty} (E_n^{(\rho)})^{1/n} = \frac{3(1 - \rho)}{1 + \rho}$ for all $\rho \in (0, 1/2]$, whereas for every $\rho \in (1/2, 1)$, Cauchy–Schwarz gives $E_n^{(\rho)} \ge 1$ for all $n \ge 1$, so $U_n^{(\rho^2)}(\rho) \ge \bigl(\frac{1 + \rho}{3(1 - \rho)}\bigr)^n$ diverges exponentially at rate $\ge \frac{1 + \rho}{3(1 - \rho)} > 1$.

*Proof.* **Part 1.** At $n = 1$, $\mathcal{P}_{e_1, g_1}(0, 0) \ne \bot \iff 2^{g_1 - e_1} \equiv 1 \pmod 3 \iff g_1 \equiv e_1 \pmod 2$. Summing over $g_1 = e_1 \pm 2d$ ($d \ge 1$) with $u = \rho^2$ gives
$$
Z_1^{(u)}(\rho) = \sum_{e_1 = 1}^\infty Q_u(e_1)\!\left(\sum_{d=1}^\infty \rho^{2d} + \sum_{d=1}^{\lfloor (e_1 - 1)/2 \rfloor} \rho^{-2d}\right) = \frac{u}{1 - u} + \frac{1 - u}{u} \sum_{d=1}^\infty u^{-d} \sum_{e_1 = 2d + 1}^\infty u^{e_1} = \frac{2u}{1 - u}.
$$
For $n + 1 \ge 2$, write $w = (w', e_{n+1})$ and $g = (g', g_{n+1})$ with $w', g' \in \mathbb{Z}_{\ge 1}^n$ and $g_{n+1} \ne e_{n+1}$. Let $x := \tau_n(w') \in \mathcal{G}_n$ and $y := \tau_n(g') \in \mathcal{G}_n$. Then $\tau_{n+1}(w) \equiv \tau_{n+1}(g) \pmod{3^{n+1}}$ holds if and only if $(1 + 3x)2^{-e_{n+1}} \equiv (1 + 3y)2^{-g_{n+1}} \pmod{3^{n+1}}$. Multiplying by $2^{\max(e_{n+1}, g_{n+1})}$ and reducing modulo $3$ forces $g_{n+1} \equiv e_{n+1} \pmod 2$. Either $g_{n+1} = e_{n+1} + 2d$ ($d \ge 1$), so $y \equiv 4^d x + \frac{4^d - 1}{3} \pmod{3^n}$, or $e_{n+1} = g_{n+1} + 2d$ ($d \ge 1$), so $x \equiv 4^d y + \frac{4^d - 1}{3} \pmod{3^n}$. Using $Q_u(e)\rho^{-e} = \frac{1 + \rho}{\rho} Q_\rho(e)$ at $\rho = \sqrt{u}$ [24, Proof of Theorem 3(1)], each pair $(w', g')$ has symmetric weight $\bigl(\frac{1 + \rho}{1 - \rho}\bigr)^n Q_\rho^{\otimes n}(w') Q_\rho^{\otimes n}(g')$, while summing $(e_{n+1}, g_{n+1})$ over $g_{n+1} = e_{n+1} + 2d$ contributes $\sum_{e=1}^\infty Q_u(e)\rho^{2d} = u^d$, and the symmetric case $e_{n+1} = g_{n+1} + 2d$ contributes $\sum_{g=1}^\infty Q_u(g + 2d)\rho^{-2d} = u^d$. Exchanging $x \leftrightarrow y$ in the second sum doubles the first:
$$
Z_{n+1}^{(u)}(\rho) = 2\left(\frac{1 + \rho}{1 - \rho}\right)^n \sum_{d=1}^\infty u^d \sum_{x \in \mathcal{G}_n} \mu_n^{(\rho)}(x)\, \mu_n^{(\rho)}\!\left(4^d x + \frac{4^d - 1}{3} \bmod 3^n\right).
$$
Since $\rho_n^{(\rho)} = 3^n \mu_n^{(\rho)}(\cdot \bmod 3^n)$ on $\mathbb{Z}_3^\times$ and $m_3(x + 3^n\mathbb{Z}_3) = 3^{-n}$, rewriting the finite sum as an integral over $(\mathbb{Z}_3, m_3)$ yields $(2.5)$.

For $(2.6)$, direct evaluation of $(1.1)$ gives $\mathcal{P}_{1, 3}(0, 0) = (2, 1)$ and $\mathcal{P}_{2, 1}(2, 1) = (1, 1)$ ($\beta(1, 1) = 1$), whereas $\mathcal{P}_{3, 1}(0, 0) = (-2, -1/4)$ and $\mathcal{P}_{1, 2}(-2, -1/4) = (-1, -1/2)$ ($\beta(-1, -1/2) = 1$). Because $(1, 1)$ and $(-1, -1/2)$ are exact fixed points of $\mathcal{P}_{1, 1}$, prepending $1^{n-2}$ preserves both states for all $n \ge 2$. Since $\|w^{(n)}\| = n + 1$ and $\|g^{(n)}\| = n + 2$, these two ordered pairs contribute $Q_u^{\otimes n}(w^{(n)})\rho^1 + Q_u^{\otimes n}(g^{(n)})\rho^{-1} = 2 u^{3/2}(1 - u)^n$ to $Z_n^{(u)}(\rho)$, while additional pairs such as $(1^{n-1}, 1)$ vs. $(1^{n-1}, 3)$ contribute strictly positively, yielding $(2.6)$. Equating $\frac{1 + \rho}{3(1 - \rho)} = 1 - \rho^2 = (1 + \rho)(1 - \rho)$ on $(0, 1/2)$ gives $(1 - \rho)^2 = 1/3$, i.e., $\rho_{\mathrm{crit,2}} = 1 - 1/\sqrt{3}$.

**Part 2.** To keep $(2.7)$ self-contained, fix $n \ge 1$, $s \ge n$, and $z \in \mathcal{G}_n$ with $m := m_n(s, z) \ge 1$. For any distinct $w \ne w'$ in $\mathcal{F}_n(s, z)$, let $j_* \in \{1, \dots, n - 1\}$ be the least index where $S_{j_*}(w) \ne S_{j_*}(w')$, say $S_{j_*}(w) < S_{j_*}(w')$. Then $v_2(N_n(w) - N_n(w')) = S_{j_*}(w) < \infty$, so $N_n(w) \ne N_n(w')$, while $N_n(w) \equiv 2^s z \pmod{3^n}$ for all $w \in \mathcal{F}_n(s, z)$. Ordering $V_w := N_n(w)/3^n > 0$ as $0 < V_{w^{(1)}} < \dots < V_{w^{(m)}}$ with integer spacings $\ge 1$ gives $V_{w^{(k)}} > k - 1$, so $\sum_{w \in \mathcal{F}_n(s, z)}(1 + 2 V_w) > \sum_{k=1}^m (2k - 1) = m^2$ (compare [7, Proposition 2.13; 17, Sec. 7]). Moreover, setting $x := 4u \in (0, 1)$ gives $\ln F(u) = \ln\bigl(\frac{4 - x}{3}\bigr) + \frac{x}{4 - x}\ln x =: g(x)$ with $g(1) = 0$ and $g'(x) = \frac{4\ln x}{(4 - x)^2} < 0$ on $(0, 1)$, so $F(u) > 1$ for all $u \in (0, 1/4)$.

Now set $F_n(s) := \sum_{z \in \mathcal{G}_n} m_n(s, z)^2$ and $A_n(s) := \bigl(\frac{1 - u}{u}\bigr)^n u^s F_n(s)$. Grouping all pairs $(w, g) \in \mathbb{Z}_{\ge 1}^n \times \mathbb{Z}_{\ge 1}^n$ with $\tau_n(g) \equiv \tau_n(w) \pmod{3^n}$ by $(s, t, z) = (\|w\|, \|g\|, \tau_n(w))$ and applying Cauchy–Schwarz first over $z \in \mathcal{G}_n$ and then over $s \ge n$ against $w_n(s) := \bigl(1 + \frac{(s - n\mu_u)^2}{n\sigma_u^2}\bigr)^{-1}$ gives
$$
U_n^{(u)}(\sqrt{u}) = \left(\frac{1 - u}{u}\right)^n \sum_{s, t \ge n} u^{(s+t)/2} \sum_{z \in \mathcal{G}_n} m_n(s, z) m_n(t, z) \;\le\; \left(\sum_{s=n}^\infty \sqrt{A_n(s)}\right)^2 \;\le\; \left(\sum_{s \in \mathbb{Z}} w_n(s)\right)\!\left(\sum_{s=n}^\infty w_n(s)^{-1} A_n(s)\right). \tag{2.10}
$$
Unimodality of $x \mapsto \bigl(1 + \frac{(x - n\mu_u)^2}{n\sigma_u^2}\bigr)^{-1}$ around $n\mu_u$ gives $\sum_{s \in \mathbb{Z}} w_n(s) \le 1 + \int_{-\infty}^\infty \bigl(1 + \frac{(x - n\mu_u)^2}{n\sigma_u^2}\bigr)^{-1} dx = 1 + \pi\sigma_u\sqrt{n} \le (1 + \pi\sigma_u)\sqrt{n}$ for every $n \ge 1$, with $\frac{1}{\sqrt{n}}\sum_{s \in \mathbb{Z}} w_n(s) \to \pi\sigma_u$.

Summing $(2.7)$ over $z \in \mathcal{G}_n$ gives $A_n(s) \le \mathbb{E}_{Q_u^{\otimes n}}[(1 + 2 V_w)\mathbf{1}_{\{S_n = s\}}]$, so summing over $s \ge n$ eliminates the indicator:
$$
\sum_{s=n}^\infty w_n(s)^{-1} A_n(s) \;\le\; \mathbb{E}_{Q_u^{\otimes n}}\!\left[\left(1 + \frac{(S_n - n\mu_u)^2}{n\sigma_u^2}\right)\!(1 + 2 V_w)\right]. \tag{2.11}
$$
Here $\mathbb{E}_{Q_u^{\otimes n}}\bigl[1 + \frac{(S_n - n\mu_u)^2}{n\sigma_u^2}\bigr] = 2$. Expanding $2 V_w = \frac{2}{3}\sum_{j=0}^{n-1} 3^{-j} 2^{S_j}$ for $2u \in (0, 1/2)$, we have $\mathbb{E}_{Q_u}[2^e] = \frac{2(1 - u)}{1 - 2u} = 3\kappa(u)$ with $1 - \kappa(u) = \frac{1 - 4u}{3(1 - 2u)} > 0$, and weighting $(e_1, \dots, e_j)$ by $2^e / \mathbb{E}_{Q_u}[2^e]$ tilts the first $j$ coordinates to $Q_{2u}^{\otimes j}$ while leaving $(e_{j+1}, \dots, e_n) \sim Q_u^{\otimes(n-j)}$ independent. Decomposing $S_n - n\mu_u = (S_j - j\mu_{2u}) + (S_n - S_j - (n - j)\mu_u) + j\Delta\mu$ under $Q_{2u}^{\otimes j} \otimes Q_u^{\otimes(n-j)}$ gives
$$
\mathbb{E}_{Q_{2u}^{\otimes j} \otimes Q_u^{\otimes(n-j)}}\bigl[(S_n - n\mu_u)^2\bigr] = j\sigma_{2u}^2 + (n - j)\sigma_u^2 + j^2(\Delta\mu)^2 \;\le\; n\sigma_u^2 + j\sigma_{2u}^2 + j^2(\Delta\mu)^2.
$$
Multiplying by $\frac{2}{3}\kappa(u)^j$, dividing by $n\sigma_u^2$, and summing $j \ge 0$ yields
$$
\sum_{s=n}^\infty w_n(s)^{-1} A_n(s) \;\le\; 2 + \sum_{j=0}^\infty \frac{2}{3}\kappa(u)^j \!\left(2 + \frac{j\sigma_{2u}^2 + j^2(\Delta\mu)^2}{n\sigma_u^2}\right) \;=\; M_{\mathrm{asymp}}(u) + \frac{R_{\mathrm{rem}}(u)}{n},
$$
proving $(2.8)$ and the first bound in $(2.9)$ via $(2.10)$, while $\sum_{n=n_0}^N n^{-1/2} \sim 2\sqrt{N}$ yields the second bound in $(2.9)$.

**Part 3.** By $(2.1)$ and $Z_k^{(\rho^2)}(\rho) \ge 0$, $E_n^{(\rho)} = \bigl(\frac{3(1 - \rho)}{1 + \rho}\bigr)^n U_n^{(\rho^2)}(\rho) \ge \bigl(\frac{3(1 - \rho)}{1 + \rho}\bigr)^n$; combining with $(2.8)$ for $\rho \in (0, 1/2)$ and $c_1 n \le E_n^{(1/2)} \le C_1 n$ [20] gives $\lim_{n \to \infty}(E_n^{(\rho)})^{1/n} = \frac{3(1-\rho)}{1+\rho}$ on $(0, 1/2]$. For $\rho \in (1/2, 1)$, Cauchy–Schwarz on $(\mathbb{Z}_3, m_3)$ gives $1 = \bigl(\int_{\mathbb{Z}_3} \rho_n^{(\rho)}\,dm_3\bigr)^2 \le E_n^{(\rho)}$, proving $U_n^{(\rho^2)}(\rho) \ge \bigl(\frac{1 + \rho}{3(1 - \rho)}\bigr)^n$. $\blacksquare$

| Regime & Tilt $(u, \rho = \sqrt{u})$ | Cramér Base $\Lambda(u)$ | Tilted Slope $S_{\mathrm{tilt}}(u)$ | Centered $C_{\mathrm{asymp}}(u)$ | $U_6^{(u)}(\rho)$ | $U_{12}^{(u)}(\rho)$ ($r=10$ for $u \ge \frac{1}{4}$) | $Z_{12}^{(u)}(\rho)$ ($r=10$ for $u \ge \frac{1}{4}$) | Ratio $Z_{12} / Z_{11}$ |
|---|---|---:|---:|---:|---:|---:|---:|
| Subcritical $(4/25, 2/5)$ | `[0.7395164947, 0.7395164948]` | `[2.473780, 2.473781]` | `[14.295077, 14.295078]` | `[2.12122332, 2.12122333]` | `[2.55834829, 2.55834830]` | `[0.04984048, 0.04984049]` | `[0.86635124, 0.86635125]` |
| Subcritical $(81/400, 9/20)$ | `[0.7887034534, 0.7887034535]` | `[5.013191, 5.013192]` | `[25.750589, 25.750590]` | `[2.77707215, 2.77707216]` | `[3.69052766, 3.69052767]` | `[0.11596824, 0.11596825]` | `[0.89997108, 0.89997109]` |
| Subcritical $(361/1600, 19/40)$ | `[0.8141586930, 0.8141586931]` | `[9.707193, 9.707194]` | `[47.237341, 47.237342]` | `[3.28584442, 3.28584443]` | `[4.81326631, 4.81326632]` | `[0.21979426, 0.21979427]` | `[0.94368702, 0.94368703]` |
| **Critical $(1/4, 1/2)$** | `[0.8399473665, 0.8399473666]` | $\infty$ | $\infty$ | `[4.00032991, 4.00032992]` | `[5.86578902, 5.86578903]` | `[0.46738741, 0.46738742]` | — |
| Supercritical $(121/400, 11/20)$ | — | — | — | `[6.57423120, 6.57423121]` | `[13.31749484, 13.31749485]` | `[2.04595968, 2.04595969]` | — |

*Table 1: Certified $220$-bit outward-rounded zero-float trajectories of cumulative predecessor renewal $U_r^{(u)}(\sqrt{u})$ and step increments $Z_r^{(u)}(\sqrt{u})$ through $r = 12$ ($\phi(3^{12}) = 354{,}294$) in the subcritical regime and through $r = 10$ at $u \in \{1/4, 121/400\}$. For the three subcritical tilts, the Kullback–Leibler divergence bases from $Q_{1/4}$ are $F(4/25) \in [1.02872648, 1.02872649]$, $F(81/400) \in [1.00793396, 1.00793397]$, and $F(361/1600) \in [1.00209519, 1.00209520]$, while $E_r^{(\rho)}$ grows exponentially at bases $9/7$, $33/29$, and $63/59$.*

---

## 3. Header-Invariant Full-Alphabet Shift-Invariant Cramér Deficit

### 3.1 From the $4$-Step Escape Witness to a Macroscopic Shift-Invariant Rate Gap

On the binary subalphabet $\{1, 2\}$, ballot-admissible words suffer zero escapes through $T = 18$, first escape via an intermediate prefix at $T_{\min}(\{1, 2\}) = 19$, and first escape at full depth at $T_{\min}^{\mathrm{full}}(\{1, 2\}) = 22$ [23, Theorem 3], forcing every shift-invariant binary subshift surviving at $T \ge 22$ under a $1^{M_0}$ header strictly below $3/4$ by $3/4 - 0.7499999755 \approx 2.45 \times 10^{-8}$ [24, Theorem 1(3)]. On the **full alphabet** $\mathbb{Z}_{\ge 1}$, prior escape censuses in [16, Sec. 5.2 & Table 4] and [23] (see also [15] on $3$-adic shielding) already identified the minimal $T = 4$ ballot escape witness $w_4 = (1, 1, 1, 3) \leftrightarrow g_4 = (1, 1, 2, 1)$ ($n(q) = 79 + 128q \to 101 + 162q \leftarrow 39 + 64q$).

Here we establish that $w_4$ is **invariant under arbitrary $1^{M_0}$ headers** ($1^{M_0} \cdot w_4 \notin \mathcal{I}_{M_0 + 4}$ for all $M_0 \ge 0$), reconcile the exact non-binary leaf-shielding census through $T = 8$, and prove a **new shift-invariant impossibility theorem** on $\mathbb{Z}_{\ge 1}^{\mathbb{N}}$: every shift-invariant full-alphabet subshift surviving $1^{M_0}$-anchored ballot admissibility suffers a macroscopic rate deficit exceeding $0.021951$ below $\Lambda(u_{\mathrm{bal}})$.

**Theorem 2 (Header-Invariant $w_4$ Obstruction and Full-Alphabet Shift-Invariant Cramér Deficit).**
1. *(Header Invariance of $w_4$ and $T \le 8$ Non-Binary Shielding Reconciliation).* Across $\mathcal{N}_T \subseteq \mathbb{Z}_{\ge 1}^T$:
   - Following [16, Sec. 5.2; 23], $\mathcal{N}_T \subseteq \{1, 2\}^T$ for $1 \le T \le 3$, and at $T = 4$ the unique non-binary ballot word $w_4 := (1, 1, 1, 3) \in \mathcal{N}_4$ escapes via $g_4 := (1, 1, 2, 1)$ with $\mathcal{P}_{w_4, g_4}(0, 0) = (-1, -1/2)$ and shadow slope $\beta(-1, -1/2) = 1$. Because $\mathcal{P}_{1, 1}(-1, -1/2) = (-1, -1/2)$ is an exact fixed point,
     $$
     1^{M_0} \cdot w_4 \;\notin\; \mathcal{I}_{M_0 + 4} \qquad \text{for every integer } M_0 \ge 0. \tag{3.1}
     $$
   - Every non-binary word in $\mathcal{N}_T$ escapes $\mathcal{I}_T$ for $1 \le T \le 6$ ($\mathcal{I}_T = \mathcal{N}_T \cap \{1, 2\}^T$, eliminating $1, 2, 10$ non-binary words at $T = 4, 5, 6$). Non-binary words first survive in $\mathcal{I}_T$ via $3$-adic leaf shielding across an internal $e = 2$ step [15] at **$T = 7$** ($6$ non-binary survivors among $46$ total survivors: $(1^5, 2, 3)$, $(1^5, 2, 4)$, $(1^4, 2, 1, 3)$, $(1^4, 2, 1, 4)$, $(1^3, 2, 1^2, 3)$, $(1^3, 2, 1^2, 4)$) and at **$T = 8$** (**$26$** non-binary survivors plus $75$ binary survivors $= 101$ total survivors out of $173$ ballot words, including $(1, 1, 1, 2, 1, 1, 1, 3) \in \mathcal{I}_8$).
2. *(Full-Alphabet Shift-Invariant Impossibility Below $\Lambda(u_{\mathrm{bal}})$).* Let $\Sigma \subseteq \mathbb{Z}_{\ge 1}^{\mathbb{N}}$ be **any** shift-invariant subshift ($\mathcal{S}(\Sigma) \subseteq \Sigma$) satisfying **either** (a) $1^{M_0} \cdot \mathcal{L}_{T_0}(\Sigma) \subseteq \mathcal{I}_{M_0 + T_0}$ for some $T_0 \ge 4$ and $M_0 \ge 0$, **or** (b) $1^{M_0} \cdot (\mathcal{L}_4(\Sigma) \cap \mathcal{N}_4^{(M_0)}) \subseteq \mathcal{I}_{M_0 + 4}$ for some $M_0 \ge 0$ (in particular, whenever $1^{M_0} \cdot (\mathcal{L}_T(\Sigma) \cap \mathcal{N}_T^{(M_0)}) \subseteq \mathcal{I}_{M_0 + T}$ holds for all $T \ge 1$). Then $\Sigma \subseteq \Sigma_{\neg w_4}^{\mathrm{full}} := \{x \in \mathbb{Z}_{\ge 1}^{\mathbb{N}} : x_{j+1..j+4} \ne (1, 1, 1, 3)\;\forall j \ge 0\}$, and consequently:
   - *(Unrestricted $2$-adic ceiling):*
     $$
     \limsup_{T \to \infty} \mu_2\bigl(\mathcal{L}_T(\Sigma)\bigr)^{1/T} \;\le\; \rho_{\mu_2}\bigl(\Sigma_{\neg w_4}^{\mathrm{full}}\bigr) \;\in\; [\mathbf{0.983579291294},\; \mathbf{0.983579291295}] \;<\; 1, \tag{3.2}
     $$
     where $\rho_{\mu_2}(\Sigma_{\neg w_4}^{\mathrm{full}})$ is the unique root in $(3/4, 1)$ of $(1 - \lambda)\lambda^3 = \frac{1}{64}$;
   - *(Ballot-constrained Cramér deficit):* for **every** fixed header length $M_1 \ge 0$,
     $$
     \limsup_{T \to \infty} \mu_2\bigl(\mathcal{L}_T(\Sigma) \cap \mathcal{N}_T^{(M_1)}\bigr)^{1/T} \;\le\; \inf_{u \in (0, 1/2)} \frac{\lambda_{w_4}(u)}{(2u)^{\log_2 3}} \;\le\; \frac{\lambda_{w_4}(u_*)}{(2u_*)^{\log_2 3}} \;\le\; \mathbf{0.924552808060} \;<\; \mathbf{0.946504576832} \;\le\; \Lambda(u_{\mathrm{bal}}), \tag{3.3}
     $$
     where $u_* := \frac{3659}{10000}$ and $\lambda_{w_4}(u)$ is the unique root in $(\frac{3u}{4(1-u)}, \frac{u}{1-u})$ of $(\frac{u}{1-u} - \lambda)\lambda^3 = u^6$, certifying a macroscopic rate gap $\Lambda(u_{\mathrm{bal}}) - \limsup_{T \to \infty} \mu_2(\mathcal{L}_T(\Sigma) \cap \mathcal{N}_T^{(M_1)})^{1/T} \ge \mathbf{0.0219517687}$.

*Proof.* **Part 1.** For any subword $w' = (e_1, \dots, e_r) \in \mathbb{Z}_{\ge 1}^r$, any rival branch $g \in \mathbb{Z}_{\ge 1}^r$ with $d_0 = \|g\| - \|w'\| \le 0$ obeys $\sum_{m=1}^r g_m \le \|w'\|$; since each $g_m \ge 1$, the remaining-step bound $1 \le g_m \le (\|w'\| - \sum_{j > m} g_j) - (m - 1)$ exhausts all $g \in \mathbb{Z}_{\ge 1}^r$ with $d_0 \le 0$ without truncation, and for $w \in \mathcal{N}_T$ and $k_0 \ge 1$, $2^{S_{k_0}(w)} < 3^{k_0}$ implies $2^{d_0} \cdot 3^{k_0} < 2^{S_{k_0}(w)} \implies d_0 \le -1$. For $w_4 = (1, 1, 1, 3)$ and $g_4 = (1, 1, 2, 1)$, $(1.1)$ gives $\mathcal{P}_{3, 1}(0, 0) = (-2, -1/4)$, $\mathcal{P}_{1, 2}(-2, -1/4) = (-1, -1/2)$, and $\mathcal{P}_{1, 1}(-1, -1/2) = (-1, -1/2)$, proving $(3.1)$ for all $M_0 \ge 0$. At $T = 8$, for $w = (1, 1, 1, 2, 1, 1, 1, 3)$, $x_4 = (3 x_3 + 1)/4$ forces $y_4 = (x_4 - 1)/2 = 3(x_3 - 1)/8 \equiv 0 \pmod 3$, so $\mathcal{P}_{2, g_0}(-1, -1/2) = \bot$ for every $g_0 \ge 1$ while $2^{-1} \cdot 3^4 = 81/2 > 32 = 2^{S_4(w)}$, shielding the unshifted $k_0 = 4$ suffix; exhaustive enumeration over $\mathcal{N}_T$ ($1 \le T \le 8$) yields all counts in Table 2.

**Part 2.** Suppose $w_4 \in \mathcal{L}_4(\Sigma)$ for a shift-invariant subshift $\Sigma \subseteq \mathbb{Z}_{\ge 1}^{\mathbb{N}}$, so some $y \in \Sigma$ has $y_{j+1..j+4} = w_4$. By shift-invariance, $x := \mathcal{S}^j(y) \in \Sigma$ begins with $x_{1..4} = w_4$. Under (a), $1^{M_0} \cdot x_{1..T_0} \in \mathcal{I}_{M_0 + T_0}$, and prefix-closure of $\mathcal{I}$ implies $1^{M_0} \cdot w_4 \in \mathcal{I}_{M_0 + 4}$, contradicting $(3.1)$. Under (b), $w_4 \in \mathcal{N}_4 \subseteq \mathcal{N}_4^{(M_0)}$ implies $w_4 \in \mathcal{L}_4(\Sigma) \cap \mathcal{N}_4^{(M_0)}$, again forcing $1^{M_0} \cdot w_4 \in \mathcal{I}_{M_0 + 4}$ and contradicting $(3.1)$. Hence $\Sigma \subseteq \Sigma_{\neg w_4}^{\mathrm{full}}$.

Let $u \in (0, 1/2]$ and weight each letter $e \in \mathbb{Z}_{\ge 1}$ by $u^e$, with total weight $a(u) := \sum_{e=1}^\infty u^e = \frac{u}{1 - u}$ ($a(1/2) = 1$, where $u^e = 2^{-e} = \mu_2(e)$). Define $W_T(u) := \sum_{v \in \mathcal{L}_T(\Sigma_{\neg w_4}^{\mathrm{full}})} u^{\|v\|}$ ($W_0(u) := 1$) and $G_u(z) := \sum_{T=0}^\infty W_T(u) z^T$. Because $w_4 = (1, 1, 1, 3)$ is unbordered ($w_{4,4} = 3 \ne 1 = w_{4,1}$), appending $e \ge 1$ to $v \in \mathcal{L}_T(\Sigma_{\neg w_4}^{\mathrm{full}})$ yields either a word in $\mathcal{L}_{T+1}(\Sigma_{\neg w_4}^{\mathrm{full}})$ or a unique terminal occurrence $v' \cdot (1, 1, 1, 3)$ with $v' \in \mathcal{L}_{T-3}(\Sigma_{\neg w_4}^{\mathrm{full}})$ [25], giving
$$
a(u) W_T(u) = W_{T+1}(u) + u^6 W_{T-3}(u) \quad (T \ge 3), \qquad G_u(z) = \frac{1}{1 - a(u) z + u^6 z^4}. \tag{3.4}
$$
Set $h_u(\lambda) := (a(u) - \lambda)\lambda^3 - u^6$. For $u \in (0, 1/2]$, $(1 - u)^2 u \le \frac{4}{27}$, so $(1 - u)^4 u^2 \le \frac{16}{729} < \frac{27}{256}$; thus $h_u(3a(u)/4) = \frac{u^4}{(1-u)^4}\bigl(\frac{27}{256} - (1-u)^4 u^2\bigr) > 0$ while $h_u(a(u)) = -u^6 < 0$. Since $h'_u(\lambda) = \lambda^2(3a(u) - 4\lambda) \le 0$ on $[3a(u)/4, a(u)]$ and $h'_u > 0$ on $(0, 3a(u)/4)$, $h_u$ has a unique root $\lambda_{w_4}(u) \in (3a(u)/4, a(u))$ strictly larger than its positive root in $(0, 3a(u)/4)$. By Pringsheim's theorem on $(3.4)$ ($W_T(u) > 0$), $z_*(u) = 1/\lambda_{w_4}(u)$ is the smallest-modulus singularity of $G_u(z)$ and $\lim_{T \to \infty} W_T(u)^{1/T} = \lambda_{w_4}(u)$.

At $u = 1/2$, $W_T(1/2) = \mu_2(\mathcal{L}_T(\Sigma_{\neg w_4}^{\mathrm{full}}))$, giving $(3.2)$. For any fixed $M_1 \ge 0$, every $v \in \mathcal{N}_T^{(M_1)}$ satisfies $\|v\| < T\theta + M_1(\theta - 1)$ with $\theta := \log_2 3$. For any $u \in (0, 1/2)$, $2u \in (0, 1)$ gives $2^{-\|v\|} < (2u)^{-M_1(\theta - 1)}(2u)^{-T\theta} u^{\|v\|}$; summing over $v \in \mathcal{L}_T(\Sigma) \cap \mathcal{N}_T^{(M_1)} \subseteq \mathcal{L}_T(\Sigma_{\neg w_4}^{\mathrm{full}})$ yields $\mu_2(\mathcal{L}_T(\Sigma) \cap \mathcal{N}_T^{(M_1)}) \le (2u)^{-M_1(\theta - 1)}(2u)^{-T\theta} W_T(u)$, so taking $T$-th roots gives $\limsup_{T \to \infty} \mu_2(\mathcal{L}_T(\Sigma) \cap \mathcal{N}_T^{(M_1)})^{1/T} \le \lambda_{w_4}(u)/(2u)^\theta$. Evaluating at $u_* = 3659/10000$ establishes $(3.3)$. $\blacksquare$

| Horizon $T$ | Ballot $\|\mathcal{N}_T\|$ | Binary / Non-Binary in $\mathcal{N}_T$ | Escaped $\|\mathcal{N}_T \setminus \mathcal{I}_T\|$ | Surviving $\|\mathcal{I}_T\|$ | Surviving Binary / Non-Binary | Full-Depth Escapes ($i = T, k_0 = 0$) |
|---:|---:|---:|---:|---:|---:|---|
| $1$ | $1$ | $1$ / $0$ | $0$ | $1$ | $1$ / $0$ | None |
| $2$ | $2$ | $2$ / $0$ | $0$ | $2$ | $2$ / $0$ | None |
| $3$ | $3$ | $3$ / $0$ | $0$ | $3$ | $3$ / $0$ | None |
| **$4$** | **$7$** | **$6$ / $1$** | **$1$** | **$6$** | **$6$ / $0$** | **$w_4 = (1, 1, 1, 3) \leftrightarrow (1, 1, 2, 1) \mapsto (-1, -1/2)$** |
| $5$ | $12$ | $10$ / $2$ | $2$ | $10$ | $10$ / $0$ | $(1^4, 3) \leftrightarrow (1^3, 2, 1) \mapsto (-1, -1/2)$ |
| $6$ | $30$ | $20$ / $10$ | $10$ | $20$ | $20$ / $0$ | $(1^5, 3),\; (1^5, 4) \mapsto (-1, -1/2)$ |
| **$7$** | **$85$** | **$40$ / $45$** | **$39$** | **$46$** | **$40$ / $6$** | $(1^6, 3),\; (1^6, 4),\; (1^6, 5) \mapsto (-1, -1/2)$ |
| **$8$** | **$173$** | **$75$ / $98$** | **$72$** | **$101$** | **$75$ / $26$** | $(1^7, 3),\; (1^7, 4),\; (1^7, 5) \mapsto (-1, -1/2)$ |

*Table 2: Exact zero-truncation escape and shielding reconciliation over $\mathcal{N}_T$ ($1 \le T \le 8$; see [16, Sec. 5.2; 23] for prior finite escape censuses). Zero binary ballot words escape for $T \le 8$; all non-binary ballot words escape for $1 \le T \le 6$, while $6$ non-binary words survive at $T = 7$ and $26$ survive at $T = 8$ ($75 + 26 = 101$).*

---

## 4. Conditional SFT-Free Binary and Subcritical Parity-Trap Splicing Reductions

### 4.1 Quantitative Renewal Thresholds for Non-Stationary Splicing

Because shift-invariant subshifts are obstructed both on $\{1, 2\}^*$ [24] and on $\mathbb{Z}_{\ge 1}^*$ (Theorem 2), we record two unconditional proofs of **conditional reductions** clarifying the exact predecessor-renewal bounds that would suffice for non-stationary splicing: (1) on $\{1, 2\}^*$, backward discrepancy monotonicity along $1^{M_0}$ removes the middle SFT stage of [24, Theorem 2] entirely, showing that the **finite tail-sum condition** $\sum_{k=16}^\infty Z_k(1/2) < 127/128$ (requiring no exponential decay rate) implies $\lim_{L \to \infty} \mu_2(\mathcal{I}_L \cap \{1, 2\}^L)^{1/L} = 3/4$; and (2) across subcritical tilts $u \in (0, 1/4)$, three-stage splicing $W = 1^{M_0} \cdot H \cdot V$ on the parity-trap shift $\mathcal{A}_{\mathrm{PT}}(128, 7)$ [23, Sec. 3.2] reduces $\liminf_{L \to \infty} \mu_2(\mathcal{I}_L)^{1/L} \ge \Lambda(u)$ to $\limsup_{r \to \infty} Z_r^{(u)}(\sqrt{u})^{1/r} < \theta_{\mathrm{PT}}(u)$.

Recall from [23, Sec. 3.2] that $\mathcal{A}_{\mathrm{PT}}(128, 7)$ is the right-to-left dyadic slope SFT on $V_{\mathrm{grid}} = \{k/128 : 128 \le k \le 896\}$ generated by the six parity-trap atoms and slope caps
$$
\mathcal{A}_{\mathrm{PT}} := \bigl\{((1), 7),\; ((2), 5),\; ((1, 2, 3), 7/4),\; ((1, 2, 2, 3), 19/16),\; ((1, 1, 2, 4), 7/4),\; ((1, 1, 2, 2, 4), 19/16)\bigr\}, \tag{4.1}
$$
whose unit-step expansion has top strongly connected component $V_{\mathrm{top}}$ of $1{,}340$ vertices ($704$ grid vertices and $636$ internal atom vertices). Let $\mathcal{L}_M^{\mathrm{grid}}(\mathcal{A}_{\mathrm{PT}}(128, 7)) \subseteq \{1, 2, 3, 4\}^M$ denote the set of length-$M$ words traced by walks in $V_{\mathrm{top}}$ starting and ending in $V_{\mathrm{grid}} \cap V_{\mathrm{top}}$.

**Theorem 3 (Conditional SFT-Free Binary Tail-Sum and Subcritical Parity-Trap Splicing Reductions).**
1. *(Backward Monotonicity Along $1^{M_0}$ and Conditional Binary Tail-Sum Reduction).* For any $m \ge 1$, suffix $v \in \mathbb{Z}_{\ge 1}^k$, and rival branch $g = (g_{\mathrm{hdr}}, g_{\mathrm{tail}}) \in \mathbb{Z}_{\ge 1}^m \times \mathbb{Z}_{\ge 1}^k$ with $\mathcal{P}_{v, g_{\mathrm{tail}}}(0, 0) = (d_{\mathrm{tail}}, c_{\mathrm{tail}}) \ne \bot$ and $\mathcal{P}_{1^m, g_{\mathrm{hdr}}}(d_{\mathrm{tail}}, c_{\mathrm{tail}}) = (d_0, c_0) \ne \bot$, one has $d_{\mathrm{tail}} \le d_0$; if $d_0 < 0$ or $(d_0 = 0, c_0 < 0)$, then $d_{\mathrm{tail}} < 0$ or $(d_{\mathrm{tail}} = 0, c_{\mathrm{tail}} < 0)$. Consequently, splicing $W = 1^{M_0} \cdot V$ ($M_0 = \lfloor \alpha L \rfloor$, $V \sim \widetilde{\mu}_2^{\otimes(L - M_0)}$) establishes the conditional implication
   $$
   \sum_{k = 16}^\infty Z_k(1/2) \;<\; \frac{127}{128} = \mathbf{0.9921875} \quad\Longrightarrow\quad \lim_{L \to \infty} \mu_2\bigl(\mathcal{I}_L \cap \{1, 2\}^L\bigr)^{1/L} = \frac{3}{4}. \tag{4.2}
   $$
2. *(Strict Suffix-Code Determinism, $K_0 = 9$ Reachability, and Conditional Subcritical Splicing).*
   - *(a) Grid-to-grid spectral lower bound:* $\mathcal{A}_{\mathrm{PT}}$ is a strict suffix code, so for every terminal grid vertex $q_* \in V_{\mathrm{grid}} \cap V_{\mathrm{top}}$ and $M \ge 1$, distinct length-$M$ walks in $V_{\mathrm{top}}$ from $V_{\mathrm{grid}} \cap V_{\mathrm{top}}$ to $q_*$ carry distinct label words. The $Q_u$-weighted adjacency matrix $A_{\mathrm{top}}(u)$ satisfies $A_{\mathrm{top}}(u)^{K_0}\mathbf{1}_{V_{\mathrm{grid}} \cap V_{\mathrm{top}}} > 0$ entrywise on $V_{\mathrm{top}}$ at minimal exponent $K_0 = 9$, yielding $Q_u^{\otimes M}(\mathcal{L}_M^{\mathrm{grid}}(\mathcal{A}_{\mathrm{PT}}(128, 7))) \ge c_{\mathrm{grid}}(u)\,\theta_{\mathrm{PT}}(u)^M$ for all $u \in (0, 1/4)$ and $M \ge 9$, where $\theta_{\mathrm{PT}}(u) := \rho(A_{\mathrm{top}}(u))$ (Table 3).
   - *(b) Conditional subcritical reduction:* For $u \in (0, 1/4]$, $M_k^{\mathrm{bal}}(V) := (6/5)^{2 S_k(V) - 3k}$ is a positive $Q_u$-supermartingale ($\mathbb{E}_{Q_u}[(6/5)^{2e - 3}] \le \frac{125}{128} < 1$), and $\mathcal{T}_N^{(u)} := \{V \in \mathbb{Z}_{\ge 1}^N : \max_{1 \le k \le N}(2 S_k(V) - 3k) \le 15,\; S_N(V) \ge N\mu_u - 2\sigma_u\sqrt{N}\}$ satisfies $Q_u^{\otimes N}(\mathcal{T}_N^{(u)}) \ge 1 - (5/6)^{16} - 1/4 > \frac{11}{16}$. Splicing $W = 1^{M_0} \cdot H \cdot V \in \{1^{M_0}\} \times \mathcal{L}_M^{\mathrm{grid}}(\mathcal{A}_{\mathrm{PT}}(128, 7)) \times \mathcal{T}_N^{(u)}$ ($M_0 = M = \lfloor \alpha L \rfloor \ge 19$, $N = L - 2M$) establishes for every $u \in (0, 1/4)$ the conditional implication
     $$
     \limsup_{r \to \infty} Z_r^{(u)}(\sqrt{u})^{1/r} \;<\; \theta_{\mathrm{PT}}(u) \quad\Longrightarrow\quad \liminf_{L \to \infty} \mu_2(\mathcal{I}_L)^{1/L} \;\ge\; \Lambda(u). \tag{4.3}
     $$

*Proof.* **Part 1.** Along $1^m$, each step has $e = 1 \le g_{\mathrm{hdr}, t}$, so $d_0 = d_{\mathrm{tail}} + \sum_{t=1}^m (g_{\mathrm{hdr}, t} - 1) \ge d_{\mathrm{tail}}$. If $d_0 < 0$, then $d_{\mathrm{tail}} < 0$; if $d_0 = 0, c_0 < 0$ and $d_{\mathrm{tail}} = 0$, then $g_{\mathrm{hdr}} = 1^m$ and equality in $(1.2)$ gives $1 > c_0 + 1 = 1 + (2/3)^m c_{\mathrm{tail}}$, so $c_{\mathrm{tail}} < 0$. Fix $\alpha \in (0, 1/2)$, $M_0 = \lfloor \alpha L \rfloor \ge 6$, $N = L - M_0$, and $\mathcal{T}_N := \{V \in \{1, 2\}^N : 2 S_k(V) - 3k \le 6 \;\forall 1 \le k \le N\}$, which obeys $\widetilde{\mu}_2^{\otimes N}(\mathcal{T}_N) \ge \frac{127}{128}$ [24, Theorem 2(3)]. Since $2^{18} < 3^{12}$, every $W = 1^{M_0} \cdot V \in \{1^{M_0}\} \times \mathcal{T}_N$ lies in $\mathcal{N}_L$ and has zero escapes on $1 \le i \le M_0$. For escapes at $i = M_0 + k$ ($1 \le k \le N$), if $k_0 = M_0 + j \ge M_0$ ($r = k - j$), then $r_{\min}^{\mathrm{strict}}(\{1, 2\}^*) = 16$ [24, Theorem 1(2)] eliminates $r \le 15$, while for $r \ge 16$ independence of $V_{1..j}$ and $V_{j+1..j+r}$ gives probability $\le \frac{8}{1 - \sqrt{8}/3}(2/3)^{M_0}\sum_{r=16}^\infty Z_r(1/2)$; if $0 \le k_0 \le M_0 - 1$, backward monotonicity forces $V_{1..k}$ to admit a strict escape, which vanishes for $k \le 15$ and has probability $\le Z_k(1/2)$ for $k \ge 16$. If $\delta := \frac{127}{128} - \sum_{k=16}^\infty Z_k(1/2) > 0$, at least $\delta - O((2/3)^{M_0})$ of $\widetilde{\mu}_2^{\otimes N}$-mass survives in $\mathcal{I}_L$, giving $\mu_2(\mathcal{I}_L \cap \{1, 2\}^L) \ge \frac{\delta}{2}(2/3)^{\lfloor \alpha L \rfloor}(3/4)^L$ for large $L$; sending $\alpha \downarrow 0$ yields $(4.2)$.

**Part 2.** In $(4.1)$, $(1)$, $(2)$, $(1, 2, 3) \ne (2, 2, 3)$, and $(1, 1, 2, 4) \ne (1, 2, 2, 4)$ have pairwise disjoint terminal suffixes, so right-to-left parsing from any fixed $q_* \in V_{\mathrm{grid}} \cap V_{\mathrm{top}}$ via $\beta_q = \max(1, \lceil 128\,\psi_a(\beta_{q'})\rceil/128)$ uniquely reconstructs the walk. Given a positive Collatz–Wielandt vector $\theta_{\mathrm{lo}}\mathbf{v} \le A_{\mathrm{top}}(u)\mathbf{v} \le \theta_{\mathrm{hi}}\mathbf{v}$ and $\mathbf{r}_* := A_{\mathrm{top}}(u)^9 \mathbf{1}_{V_{\mathrm{grid}} \cap V_{\mathrm{top}}} \ge c_1 \mathbf{v} > 0$, pigeonholing $\mathbf{1}_{V_{\mathrm{grid}} \cap V_{\mathrm{top}}}^\top A_{\mathrm{top}}(u)^M \mathbf{1}_{V_{\mathrm{grid}} \cap V_{\mathrm{top}}} \ge c_1 \theta_{\mathrm{lo}}^{M-9}\sum_{q \in V_{\mathrm{grid}} \cap V_{\mathrm{top}}} \mathbf{v}_q$ over the $704$ terminal grid vertices yields part (a). By Ville's inequality [26] and Chebyshev's inequality, $Q_u^{\otimes N}(\mathcal{T}_N^{(u)}) \ge 1 - (5/6)^{16} - 1/4 > 11/16$. For $M = M_0 = \lfloor \alpha L \rfloor \ge 19$ ($1792 \cdot 2^{19} < 3^{19}$), telescoping $\beta_{q_{j-1}} > \frac{2^{\|a_j\|}}{3^{|a_j|}}\beta_{q_j}$ with $2^{\|a''\|} > 3^{|a''|}$ on proper atom suffixes gives $\frac{2^{S_m(H)}}{3^m} < 7$ ($1 \le m \le M$), so $\mathcal{F}_L := \{1^M\} \times \mathcal{L}_M^{\mathrm{grid}}(\mathcal{A}_{\mathrm{PT}}(128, 7)) \times \mathcal{T}_N^{(u)} \subseteq \mathcal{N}_L$, with zero escapes on $1 \le i \le 2M$ [23, Theorem 2(2)]. Under $\mathbb{P}_{M, u} := \delta_{1^M} \otimes Q_u^{\otimes(M+N)}$, the self-loop $\frac{65}{64} \xrightarrow{1} \frac{65}{64}$ in $V_{\mathrm{top}}$ gives $\theta_{\mathrm{PT}}(u) \ge 1 - u > \frac{3}{4} > \frac{2}{3} > \rho^{\log_2(3/2)} =: \gamma_{\mathrm{hdr}}(\rho)$; if $Z_r^{(u)}(\rho) \le C_\eta \eta^r$ with $\eta < \theta_{\mathrm{PT}}(u)$, escapes at $i > 2M$ with $k_0 \ge M, r \le M$ cost $O(\gamma_{\mathrm{hdr}}(\rho)^M)$, while $k_0 \ge M, r > M$ and $k_0 < M$ (by Part 1) each cost $O(\eta^M)$, giving $\mathbb{P}_{M, u}(\mathcal{F}_L \setminus \mathcal{I}_L) = o(\theta_{\mathrm{PT}}(u)^M)$. Converting $Q_u$ to $\mu_2$ via $\|H\| \ge M$ and $S_N(V) \ge N\mu_u - 2\sigma_u\sqrt{N}$ gives $\liminf_{L \to \infty} \mu_2(\mathcal{I}_L)^{1/L} \ge \bigl(\frac{\theta_{\mathrm{PT}}(u)}{4(1 - u)\Lambda(u)^2}\bigr)^\alpha \Lambda(u)$, and $\alpha \downarrow 0$ proves $(4.3)$. $\blacksquare$

| Subcritical Tilt $(u, \rho = \sqrt{u})$ | Target Cramér Base $\Lambda(u)$ | Binary $\theta_{Q_u}(\mathcal{A}_{\{1,2\}}(128,7))$ ($K_0 = 1$) | Binary $c_{\mathrm{grid}}(u)$ | Parity-Trap $\theta_{\mathrm{PT}}(u)$ ($K_0 = 9$) | Parity-Trap $c_{\mathrm{grid}}(u)$ | Empirical $Z_{12}^{(u)}(\rho)/Z_{11}^{(u)}(\rho)$ |
|---|---|---|---|---|---|---|
| $(4/25, 2/5)$ | `[0.7395164947, 0.7395164948]` | `[0.9742718940, 0.9742718941]` | `0.01447043` | **`[0.9767984452, 0.9767984453]`** | `0.04408477` | **`[0.86635124, 0.86635125]`** |
| $(81/400, 9/20)$ | `[0.7887034534, 0.7887034535]` | `[0.9586176070, 0.9586176071]` | `0.02182903` | **`[0.9627574998, 0.9627574999]`** | `0.05884134` | **`[0.89997108, 0.89997109]`** |
| $(361/1600, 19/40)$ | `[0.8141586930, 0.8141586931]` | `[0.9484904569, 0.9484904570]` | `0.02726059` | **`[0.9535434445, 0.9535434446]`** | `0.06900470` | **`[0.94368702, 0.94368703]`** |

*Table 3: Certified $160$-bit interval Collatz–Wielandt eigenvalues and grid-to-grid prefactors (`c_grid` rounded downward) on $\mathcal{A}_{\{1,2\}}(128, 7)$ ($629$ top-SCC vertices, $K_0 = 1$) and $\mathcal{A}_{\mathrm{PT}}(128, 7)$ ($1{,}340$ top-SCC vertices, $704$ grid vertices, $K_0 = 9$), alongside finite-depth empirical ratios $Z_{12}^{(u)}(\rho)/Z_{11}^{(u)}(\rho)$ (which do not by themselves establish the asymptotic hypothesis in $(4.3)$).*

![Centered-weight subcritical renewal, parity-trap thresholds, and full-alphabet shift-invariant gap](supplement/figure-1.png)

*Figure 1: (a) Certified cumulative predecessor renewal $U_r^{(u)}(\sqrt{u})$ across subcritical tilts $u \in \{4/25, 81/400, 361/1600\}$ ($1 \le r \le 12$; $O_u(\sqrt{r})$ via centered Cauchy weighting vs. $O_u(r)$ via uncentered tilting [18]), critical $u = 1/4$ ($1 \le r \le 10$; linear $\Theta(r)$ [20, 24]), and supercritical $u = 121/400$ ($1 \le r \le 10$; elementary exponential lower bound $\ge (31/27)^r$ from $E_r^{(\rho)} \ge 1$). (b) Certified step ratios $Z_r^{(u)}(\sqrt{u})/Z_{r-1}^{(u)}(\sqrt{u})$ ($3 \le r \le 12$) compared against conditional parity-trap thresholds $\theta_{\mathrm{PT}}(u)$ (Theorem 3(2)), alongside the unconditional full-alphabet shift-invariant Cramér gap of Theorem 2(2).*

---

## 5. Adelic Reciprocity, $3\mathbb{Z}_3$-Ejection, Twisted Shell Transfer, and Dual Hölder Obstructions

### 5.1 Additive Fourier Structure on $\mathcal{G}_m$ and Exact Mechanism of the Primitive-Shell Sign Flip

We now investigate Problem B ([24, Open Problem 1]; cf. [27] on high-conductor $3$-adic phases): what governs the additive Fourier modes $\widehat{\mathbf{1}_{B_m}}(b) := \sum_{y \in B_m} e^{-2\pi i b y / 3^m}$ on $\mathcal{G}_m = (\mathbb{Z}/3^m\mathbb{Z})^\times$, why do primitive-shell cross-correlations turn strictly negative in $Z_r(1/2)$, and can Hölder decouplings capture that cancellation? Theorem 4 establishes (1) an exact adelic reciprocity law and Fibonacci $2$-adic Cantor attractor, (2) a universal all-frequency adjacent-swap cosine factorization directly for $\tau_{2K}(w) \bmod 3^{2K}$, (3) an exact off-diagonal $3\mathbb{Z}_3$-ejection formula, mod-$3$ coarse-grained baseline, and twisted primitive-shell transfer identity explaining and certifying $S_r(4) < 0$ across $2 \le r \le 12$, and (4) dual Fourier-shell and physical-space Hölder obstructions.

For $w \in \{1, 2\}^m$, set $Y_m(w) := N_m(w)/3^m \in \mathbb{Z}[1/3] \subseteq \mathbb{R} \cap \mathbb{Q}_2$, and for $x \in \mathbb{Q}_2$ let $\{x\}_2 \in \mathbb{Z}[1/2]/\mathbb{Z}$ denote its $2$-adic fractional part ($x - \{x\}_2 \in \mathbb{Z}_2$). Let $\nu_\infty$ be the law on $\mathbb{Z}_2^\times$ of $Z := -\lim_{m \to \infty} Y_m(w) = -\sum_{k=0}^\infty 3^{-1-k} 2^{S_k(w)}$ under $w \sim \mathrm{Unif}(\{1, 2\}^{\mathbb{N}})$, with mod-$2^r$ marginal $\nu_r$ on $A_r := \mathrm{supp}(\nu_r) \subseteq (\mathbb{Z}/2^r\mathbb{Z})^\times$, collision norm $p_r := \sum_{z \in A_r} \nu_r(z)^2$, and $2$-adic Fourier transform $\psi_r(a) := \sum_{z \in A_r} \nu_r(z) e^{-2\pi i a z / 2^r}$. Because $\mathbf{1}_{B_m}$ is real-valued, $|\widehat{\mathbf{1}_{B_m}}(3^m - b)| = |\widehat{\mathbf{1}_{B_m}}(b)|$, so Fourier magnitudes on $\mathcal{G}_m$ ($m \ge 2$) group into $\phi(3^m)/2 = 3^{m-1}$ conjugate pairs $\{b, 3^m - b\}$. Finally, for $a \in \{1, 4\}$ and $j \ge 1$, define the primitive conductor-$3^j$ cross-correlation
$$
S_j(a) := \sum_{b \in \mathcal{G}_j} \widehat{\mathbf{1}_{a B_j}}(b)\,\overline{\widehat{\mu_j}(b)}, \tag{5.1}
$$
and for $r \ge 2$ and $m \ge 1$, define the affine bijection $T_m^{(r-1)} : \mathbb{Z}/3^{r-1}\mathbb{Z} \to \mathbb{Z}/3^{r-1}\mathbb{Z}$ by $T_m^{(r-1)}(y) := 4^m y + \frac{4^m - 1}{3} \bmod 3^{r-1}$ and decompose $\mu_{r-1} = \mu_{r-1}^{\mathrm{mod\,3}} + \delta\mu_{r-1}$ on $\mathcal{G}_{r-1}$, where $\mu_{r-1}^{\mathrm{mod\,3}}(z) := 3^{-(r-2)}\mu_1(z \bmod 3)$ ($\mu_1(1) = 1/3$, $\mu_1(2) = 2/3$).

**Theorem 4 (Adelic Reciprocity, All-Frequency Cosine Factorization, $3\mathbb{Z}_3$-Ejection, and Dual Hölder Obstructions).**
1. *(Exact Adelic Reciprocity Phase Law and Fibonacci $2$-Adic Cantor Attractor).*
   - *(a) Adelic reciprocity and last-letter independence:* For every $m \ge 1$, $w \in \{1, 2\}^m$, and $d \in \mathbb{Z}$ (with $2^{S_m(w) - d}$ taken in $\mathcal{G}_m$),
     $$
     \Phi_{m, d}(w) := \frac{\bigl(2^{S_m(w) - d}\,\tau_m(w)\bigr) \bmod 3^m}{3^m} \;\equiv\; 2^{-d} Y_m(w) - \bigl\{2^{-d} Y_m(w)\bigr\}_2 \pmod 1, \tag{5.2}
     $$
     and $\Phi_{m, d}(w', 1) \equiv \Phi_{m, d}(w', 2) \pmod 1$ for all $m \ge 2$, $w' \in \{1, 2\}^{m-1}$, and $d \in \mathbb{Z}$.
   - *(b) Fibonacci $2$-adic Cantor structure:* In $\mathbb{Z}_2^\times$, $Z \stackrel{d}{=} \frac{2^e Z - 1}{3}$ ($e \sim \mathrm{Unif}(\{1, 2\})$ independent of $Z$) has exact Fibonacci support cardinality $|A_r| = F_{r+1}$ for all $r \ge 1$ ($\dim_H(\mathrm{supp}(\nu_\infty)) = \log_2\bigl(\frac{1+\sqrt{5}}{2}\bigr)$), collision norm $p_1 = 1$, $p_2 = 1/2$, $p_r = \frac{1}{4}p_{r-1} + \frac{1}{4}p_{r-2}$ ($r \ge 3$), $\psi_2(a) = 0$ for odd $a \in \{1, 3\}$, and for all $r \ge 3$, odd $a$, and $b \equiv 3^{-1}a \pmod{2^r}$,
     $$
     \psi_r(a) = e^{+2\pi i b / 2^r} \frac{\psi_{r-1}(b \bmod 2^{r-1}) + \psi_{r-2}(b \bmod 2^{r-2})}{2}, \qquad \frac{1}{2^{r-1}} \sum_{\substack{1 \le a < 2^r \\ a \text{ odd}}} |\psi_r(a)|^2 = 2 p_r - p_{r-1}. \tag{5.3}
     $$
2. *(Universal All-Frequency Adjacent-Swap Cosine Factorization and Conjugate-Pair Maximization on $\mathcal{G}_8$).* For every even $m = 2K \ge 2$, **every** fixed frequency $b \in \mathbb{Z}/3^{2K}\mathbb{Z}$, and $w \sim \mathrm{Unif}(\{1, 2\}^{2K})$, conditioning on the sequence of unordered adjacent pairs $\mathcal{M}(w) := (\{w_{2k-1}, w_{2k}\})_{k=1}^K$ with heterogeneous block set $\mathcal{H}(w) := \{k \in \{1, \dots, K\} : \{w_{2k-1}, w_{2k}\} = \{1, 2\}\}$ fixes $S_{2K}(w)$ and every even prefix sum $S_{2k-2}(w)$ ($1 \le k \le K$), yielding the exact conditional factorization directly for $\tau_{2K}(w)$:
   $$
   \Bigl|\mathbb{E}\bigl[e^{-2\pi i b \tau_{2K}(w)/3^{2K}} \;\big|\; \mathcal{M}(w)\bigr]\Bigr| \;=\; \prod_{k \in \mathcal{H}(w)} \left|\cos\!\left(2\pi \cdot \frac{\bigl(b \cdot 2^{S_{2k-2}(w) - S_{2K}(w)}\bigr) \bmod 3^{2k}}{3^{2k}}\right)\right|, \tag{5.4}
   $$
   where $2^{S_{2k-2}(w) - S_{2K}(w)}$ denotes $(2^{-1})^{S_{2K}(w) - S_{2k-2}(w)}$ in $\mathcal{G}_{2k}$. Modulo conjugation $\{b, 3^8 - b\}$, the dyadic conjugate pair **$\{128, 6433\} = \{\pm 2^7 \bmod 3^8\}$** strictly maximizes $|\widehat{\mathbf{1}_{B_8}}(b)|/2^8$ over all $2{,}187$ conjugate pairs in $\mathcal{G}_8$ (`[0.149458, 0.149459]`), exceeding the runner-up conjugate pair $\{256, 6305\} = \{\pm 2^8 \bmod 3^8\}$ (`[0.136481, 0.136482]`) by certified gap `[0.01297685, 0.01297686]` (finite dyadic evaluations at $b = 2^{\lfloor 3m/2\rfloor - 5} \bmod 3^m$ for $m \in \{6, 8, 10, 12, 14\}$ are reported in Table 4).
3. *(Exact Off-Diagonal $3\mathbb{Z}_3$-Ejection Formula, Mod-$3$ Baseline, and Twisted Primitive-Shell Transfer).*
   - *(a) $3\mathbb{Z}_3$-ejection and mod-$3$ baseline:* For every $r \ge 2$,
     $$
     Z_r(1/2) = \left(\frac{4}{3}\right)^{r-1} \sum_{m=1}^\infty 4^{-m}\,\mu_{r-1}\!\bigl(T_m^{(r-1)}(B_{r-1})\bigr) = \frac{13}{42}\left(\frac{8}{9}\right)^{r-1} + \left(\frac{4}{3}\right)^{r-1} \sum_{m=1}^\infty 4^{-m}\,\delta\mu_{r-1}\!\bigl(T_m^{(r-1)}(B_{r-1})\bigr). \tag{5.5}
     $$
     Because $T_m^{(r-1)}(y) \equiv y + m \pmod 3$, for every $m \not\equiv 0 \pmod 3$ ($20/21$ of geometric weight $\sum_{m \ge 1} 4^{-m} = 1/3$) **exact half** ($2^{r-2}$ elements) of $T_m^{(r-1)}(B_{r-1})$ are ejected into $3\mathbb{Z}/3^{r-1}\mathbb{Z}$ where $\mu_{r-1} \equiv 0$, placing the mod-$3$ baseline $\frac{13}{42}(8/9)^{r-1}$ strictly below the $j \le 1$ shell sum $\frac{3}{8}(8/9)^r = \frac{14}{42}(8/9)^{r-1}$ (giving $Z_2(1/2) = \frac{52}{189}$ and $S_2(4) = -\frac{3}{7} < 0$ at $r = 2$, where $\delta\mu_1 \equiv 0$).
   - *(b) Primitive-shell recurrence, twisted transfer identity, and $r \le 12$ sign-flip certificate:* For every $r \ge 1$,
     $$
     \frac{1}{4} U_r = \frac{1}{4}\left(\frac{4}{9}\right)^r \!\left(2^r + \sum_{j=1}^r 2^{r - j} S_j(1)\right), \qquad Z_r(1/2) = \frac{1}{4}\left(\frac{4}{9}\right)^r \!\left(2^r + \sum_{j=1}^r 2^{r - j} S_j(4)\right), \tag{5.6}
     $$
     with $S_1(1) = S_1(4) = 1$, and for every $r \ge 2$,
     $$
     S_r(1) = \left(\frac{9}{4}\right)^r \!\left(\frac{1}{9} U_{r-1} + Z_r(1/2)\right) > 0, \qquad S_r(4) = 4\left(\frac{9}{4}\right)^r \!\left(Z_r(1/2) - \frac{8}{9} Z_{r-1}(1/2)\right) = 4\left(S_r(1) - \frac{9}{4}S_{r-1}(1)\right), \tag{5.7}
     $$
     $$
     S_r(4) = 9 \sum_{m=1}^\infty 4^{-m} \sum_{a \in \mathcal{G}_{r-1}} e^{2\pi i \frac{((4^{-m}-1)\bmod 3^r)\, a}{3^r}}\, \widehat{\mathbf{1}_{B_{r-1}}}(a)\,\overline{\widehat{\mu_{r-1}}(4^{-m} a \bmod 3^{r-1})}, \tag{5.8}
     $$
     certified **strictly negative** ($S_r(4) < 0$) across all finite shells **$2 \le r \le 12$** (Table 4).
4. *(Dual Fourier-Shell and Physical-Space Hölder Obstructions).* For **every** sequence of conjugate Hölder pairs $(p_j, q_j) \in [1, \infty]^2$ ($\frac{1}{p_j} + \frac{1}{q_j} = 1$, $1 \le j \le r$), the shell-wise Fourier Hölder bound obeys
   $$
   \mathcal{B}_{\mathrm{H\ddot{o}lder}}^{(p, q)}(r) := \frac{1}{4}\left(\frac{4}{9}\right)^r \!\left(2^r + \sum_{j=1}^r 2^{r - j} \bigl\|\widehat{\mathbf{1}_{4 B_j}}\bigr\|_{\ell^{p_j}(\mathcal{G}_j)}\,\bigl\|\widehat{\mu_j}\bigr\|_{\ell^{q_j}(\mathcal{G}_j)}\right) \;\ge\; \frac{1}{4} U_r \;\ge\; \frac{1}{3} \qquad (\forall\, r \ge 1), \tag{5.9}
   $$
   while on physical space $\mathcal{G}_r$, specializing [24, Eq. (5.3)] to $x = 1/2$ yields the exact closed-form minimax lower bound across **all** conjugate pairs $(p, q) \in [1, \infty]^2$ and **all** $r \ge 1$:
   $$
   \frac{1}{4}\left(\frac{4}{3}\right)^r \|\mathbf{1}_{4 B_r}\|_{\ell^p(\mathcal{G}_r)} \|\mu_r\|_{\ell^q(\mathcal{G}_r)} \;\ge\; \frac{1}{4}\max\!\left(\left(\frac{3}{2}\right)^{1/p}\!\left(\frac{4}{3}\left(\frac{2}{3}\right)^{1/p}\right)^r,\; \left(\frac{2}{3}\cdot 2^{1/p}\right)^r\right) \;\ge\; \frac{1}{4}\left(\frac{2}{3}\cdot 2^{\log_3 2}\right)^r, \tag{5.10}
   $$
   attained at $\frac{1}{p_*} = \log_3 2 \in [\mathbf{0.630929753571}, \mathbf{0.630929753572}]$ with base $\frac{2}{3}\cdot 2^{\log_3 2} \in [\mathbf{1.032375101753}, \mathbf{1.032375101754}] > 1$.

*Proof.* **Part 1.** Since $2^{S_m(w)}\tau_m(w) \equiv N_m(w) \pmod{3^m}$, we have $2^{S_m(w) - d}\tau_m(w) \equiv (2^{-d} \bmod 3^m) N_m(w) \pmod{3^m}$. For $d \le 0$, $\{2^{-d} Y_m(w)\}_2 = 0$ and $\Phi_{m, d}(w) \equiv 2^{-d} Y_m(w) \pmod 1$; for $d \ge 1$, choosing $Z_d \in \{0, \dots, 2^d - 1\}$ with $Z_d \equiv -N_m(w)(3^m)^{-1} \pmod{2^d}$ gives $N_m(w) + 3^m Z_d = 2^d K$ with $K \equiv (2^{-d} \bmod 3^m) N_m(w) \pmod{3^m}$ and $\frac{Y_m(w) + Z_d}{2^d} = \frac{K}{3^m} \in \mathbb{Z}_2$, so $\{2^{-d} Y_m(w)\}_2 \equiv -Z_d/2^d \pmod 1$ and $\Phi_{m, d}(w) \equiv 2^{-d} Y_m(w) - \{2^{-d} Y_m(w)\}_2 \pmod 1$. Last-letter independence follows because $N_m(w)$ is independent of $w_m$. Next, $-Y_{m+1}(e, w') = \frac{2^e(-Y_m(w')) - 1}{3}$ is a $2$-adic contraction on $\mathbb{Z}_2$, giving $Z \stackrel{d}{=} \frac{2^e Z - 1}{3}$. Modulo $2$ and $4$, $A_1 = \{1\}$ ($p_1 = 1$) and $A_2 = \{1, 3\}$ with $\nu_2(1) = \nu_2(3) = 1/2$ ($p_2 = 1/2$, $\psi_2(\text{odd}) = 0$). For $r \ge 3$ and odd $z$, $\phi_1(z) := \frac{2z - 1}{3} \equiv 3 \pmod 4$ mod $2^r$ depends injectively on $z \bmod 2^{r-1}$, while $\phi_2(z) := \frac{4z - 1}{3} \equiv 1 \pmod 4$ mod $2^r$ depends injectively on $z \bmod 2^{r-2}$. Disjointness of $\{3 \bmod 4\}$ and $\{1 \bmod 4\}$ yields $|A_r| = |A_{r-1}| + |A_{r-2}| = F_{r+1}$, $p_r = \frac{1}{4}(p_{r-1} + p_{r-2})$, and $(5.3)$.

**Part 2.** Fix $m = 2K$ and any $b \in \mathbb{Z}/3^{2K}\mathbb{Z}$. Conditioning on $\mathcal{M}(w)$ fixes every block sum $w_{2k-1} + w_{2k}$, hence fixes every even prefix sum $S_{2k}(w) = \sum_{j=1}^k (w_{2j-1} + w_{2j})$ ($0 \le k \le K$), including $S_{2K}(w)$, while the $2^{|\mathcal{H}(w)|}$ words in the class correspond to independent uniform choices $(w_{2k-1}, w_{2k}) \in \{(1, 2), (2, 1)\}$ for $k \in \mathcal{H}(w)$. Writing $b\tau_{2K}(w) \equiv b(2^{-1})^{S_{2K}(w)} \sum_{j=0}^{2K-1} 3^{2K-1-j} 2^{S_j(w)} \pmod{3^{2K}}$, all even-$j$ summands ($j = 2k - 2$) and all odd-$j$ summands with $k \notin \mathcal{H}(w)$ are constant on $\mathcal{M}(w)$. For each $k \in \mathcal{H}(w)$, $S_{2K}(w) - S_{2k-2}(w) \ge 2$, and reducing $\frac{1}{3^{2K}}\bigl(3^{2K-2k} b(2^{-1})^{S_{2K}(w) - S_{2k-2}(w)} 2^e\bigr)$ ($e \in \{1, 2\}$) modulo $1$ gives $\frac{2^e r_k}{3^{2k}}$ where $r_k := (b \cdot 2^{S_{2k-2}(w) - S_{2K}(w)}) \bmod 3^{2k}$. Because $\frac{2 r_k + 4 r_k}{2} = 3 r_k$ and $\frac{4 r_k - 2 r_k}{2} = r_k$, averaging over $e \in \{1, 2\}$ yields $\frac{1}{2}(e^{-2\pi i \cdot 2r_k/3^{2k}} + e^{-2\pi i \cdot 4r_k/3^{2k}}) = e^{-2\pi i \cdot 3r_k/3^{2k}}\cos(2\pi r_k / 3^{2k})$. Multiplying across independent $k \in \mathcal{H}(w)$ and taking moduli proves $(5.4)$. Exhaustive interval evaluation across all $2{,}187$ conjugate pairs on $\mathcal{G}_8$ certifies $\{128, 6433\}$ against $\{256, 6305\}$.

**Part 3.** For $r \ge 2$, $B_r = \{(1 + 3y)2^{-1} \bmod 3^r : y \in B_{r-1}\} \sqcup \{(1 + 3y)4^{-1} \bmod 3^r : y \in B_{r-1}\}$, so $4 B_r = \{2(1 + 3y) \bmod 3^r : y \in B_{r-1}\} \sqcup \{(1 + 3y) \bmod 3^r : y \in B_{r-1}\}$. Under $\mu_r$ ($Q_{1/2}(k) = 2^{-k}$), solving $(1 + 3z')2^{-k} \equiv z \pmod{3^r}$ forces $k = 2m$ ($2^{-2m} = 4^{-m}$) on $z \equiv 1 + 3y \equiv 1 \pmod 3$ and $k = 2m - 1$ ($2^{-(2m-1)} = 2 \cdot 4^{-m}$) on $z \equiv 2(1 + 3y) \equiv 2 \pmod 3$; in **both** cases $z' \equiv \frac{4^m(1 + 3y) - 1}{3} = T_m^{(r-1)}(y) \pmod{3^{r-1}}$. Adding $4^{-m} + 2 \cdot 4^{-m} = 3 \cdot 4^{-m}$ gives $\mu_r(4 B_r) = 3\sum_{m=1}^\infty 4^{-m}\mu_{r-1}(T_m^{(r-1)}(B_{r-1}))$, and multiplying by $\frac{1}{4}(4/3)^r = \frac{1}{3}(4/3)^{r-1}$ proves the first identity in $(5.5)$. Since $4^m \equiv 1 + 3m \pmod 9$, $T_m^{(r-1)}(y) \equiv y + m \pmod 3$. Because $B_{r-1}$ has $2^{r-2}$ elements in $\{1 \bmod 3\}$ and $2^{r-2}$ in $\{2 \bmod 3\}$, $T_m^{(r-1)}$ ejects $2^{r-2}$ elements into $0 \bmod 3$ whenever $m \equiv 1$ or $2 \pmod 3$ (leaving $2^{r-2}$ elements in $2 \bmod 3$ or $1 \bmod 3$, respectively) and ejects $0$ elements when $m \equiv 0 \pmod 3$. Summing $\mu_{r-1}^{\mathrm{mod\,3}}$ against $\sum_{m \equiv 1, 2, 0 \pmod 3} 4^{-m} = \frac{16}{63}, \frac{4}{63}, \frac{1}{63}$ yields $(4/3)^{r-1}(2/3)^{r-2}\bigl(\frac{16}{63}\cdot\frac{2}{3} + \frac{4}{63}\cdot\frac{1}{3} + \frac{1}{63}\cdot 1\bigr) = \frac{13}{42}(8/9)^{r-1}$, proving $(5.5)$.

By $2$-to-$1$ projection $a B_j \to a B_{j-1}$ and pushforward $\mu_j \to \mu_{j-1}$ modulo $3^{j-1}$, non-primitive frequencies $3\mathbb{Z}/3^r\mathbb{Z}$ contribute $2 \cdot 3^{r-1}\mu_{r-1}(a B_{r-1})$ ($r \ge 2$), giving $S_r(a) = 3^r \mu_r(a B_r) - 2 \cdot 3^{r-1}\mu_{r-1}(a B_{r-1})$, $(5.6)$, and the first two formulas in $(5.7)$, while $(4/9)^r(S_r(1) - \frac{9}{4}S_{r-1}(1)) = (\frac{1}{9}U_{r-1} + Z_r(1/2)) - (\frac{1}{9}U_{r-2} + Z_{r-1}(1/2)) = Z_r(1/2) - \frac{8}{9}Z_{r-1}(1/2) = \frac{1}{4}(4/9)^r S_r(4)$ (and directly at $r = 2$) gives the recurrence in $(5.7)$. For $(5.8)$, applying Fourier inversion on $\mathbb{Z}/3^{r-1}\mathbb{Z}$ inside $3^r \mu_r(4 B_r) = 9\sum_{m=1}^\infty 4^{-m} \cdot 3^{r-1}\mu_{r-1}(T_m^{(r-1)}(B_{r-1}))$ shows that the non-primitive frequencies $3\mathbb{Z}/3^{r-1}\mathbb{Z}$ equal $6 = 2 \cdot 3\mu_1(4 B_1)$ at $r = 2$ and $2 \cdot 9\sum_{m=1}^\infty 4^{-m}\cdot 3^{r-2}\mu_{r-2}(T_m^{(r-2)}(B_{r-2})) = 2 \cdot 3^{r-1}\mu_{r-1}(4 B_{r-1})$ for $r \ge 3$, cancelling $2 \cdot 3^{r-1}\mu_{r-1}(4 B_{r-1})$ identically and leaving $S_r(4) = 9\sum_{m=1}^\infty 4^{-m}\sum_{b \in \mathcal{G}_{r-1}} \widehat{\mathbf{1}_{T_m^{(r-1)}(B_{r-1})}}(b)\,\overline{\widehat{\mu_{r-1}}(b)}$. Substituting $a \equiv 4^m b \pmod{3^{r-1}}$ and $\frac{b \cdot 3 T_m^{(r-1)}(y)}{3^r} \equiv \frac{a y}{3^{r-1}} + \frac{(1 - 4^{-m})a}{3^r} \pmod 1$ (well-defined on $a \in \mathcal{G}_{r-1}$ since $3 \mid (4^{-m} - 1)$) proves $(5.8)$.

**Part 4.** Because $b \mapsto 4b$ permutes $\mathcal{G}_j$, $\|\widehat{\mathbf{1}_{4 B_j}}\|_{\ell^{p_j}(\mathcal{G}_j)} = \|\widehat{\mathbf{1}_{B_j}}\|_{\ell^{p_j}(\mathcal{G}_j)}$, so Hölder's inequality gives $\|\widehat{\mathbf{1}_{4 B_j}}\|_{\ell^{p_j}(\mathcal{G}_j)}\|\widehat{\mu_j}\|_{\ell^{q_j}(\mathcal{G}_j)} \ge S_j(1) > 0$, proving $(5.9)$ via $(5.6)$. Finally, on $\mathcal{G}_r$ ($|\mathcal{G}_r| = 2 \cdot 3^{r-1}$, $|4 B_r| = 2^r$), $\|\mathbf{1}_{4 B_r}\|_{\ell^p(\mathcal{G}_r)} = 2^{r/p}$, while $\sum_{z \in \mathcal{G}_r} \mu_r(z) = 1$ gives $\|\mu_r\|_{\ell^q(\mathcal{G}_r)} \ge (2 \cdot 3^{r-1})^{-1/p}$ and the single word $g = 1^r$ ($\tau_r(1^r) \equiv -1 \pmod{3^r}$) gives $\|\mu_r\|_{\ell^q(\mathcal{G}_r)} \ge \mu_r(-1 \bmod 3^r) > 2^{-r}$ [24, Eq. (5.3)]; equating the strictly decreasing base $\frac{4}{3}(2/3)^{1/p}$ and strictly increasing base $\frac{2}{3}\cdot 2^{1/p}$ yields $2 \cdot 3^{-1/p_*} = 1 \iff 1/p_* = \log_3 2$ and $(5.10)$ (since $(3/2)^{1/p} \ge 1$). $\blacksquare$

| Finite Dyadic Eval $m$ ($t_* = \lfloor\frac{3m}{2}\rfloor - 5$) | $b = 2^{t_*} \bmod 3^m$ | $\|\widehat{\mathbf{1}_{B_m}}(b)\|/2^m$ | $\sqrt{m}\,\|\widehat{\mathbf{1}_{B_m}}(b)\|/2^m$ | Shell $r$ | Certified $Z_r(1/2)$ | $\frac{1}{4}U_r$ Floor | Scaled $(4/9)^r S_r(4)$ | Shell CS Bound |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| $6$ ($t_* = 4$) | $16$ | `[0.165003, 0.165004]` | `[0.404174, 0.404175]` | $1$ | `[0.3333333333, 0.3333333334]` | `0.33333333` | `[+0.44444444, +0.44444445]` | `0.35052228` |
| $8$ ($t_* = 7$) | **$128$ (pair $\{128, 6433\}$ #1 on $\mathcal{G}_8$)** | `[0.149458, 0.149459]` | `[0.422733, 0.422734]` | $2$ | `[0.2751322751, 0.2751322752]` | `0.40211640` | **`[-0.08465609, -0.08465608]`** | `0.42962263` |
| $10$ ($t_* = 10$) | $1024$ | `[0.134800, 0.134801]` | `[0.426275, 0.426276]` | $3$ | `[0.2206158046, 0.2206158047]` | `0.45727035` | **`[-0.09578488, -0.09578487]`** | `0.50841275` |
| $12$ ($t_* = 13$) | $8192$ | `[0.120329, 0.120330]` | `[0.416832, 0.416833]` | $7$ | `[0.1258272206, 0.1258272207]` | `0.61662410` | **`[-0.01556337, -0.01556336]`** | `0.85771918` |
| $14$ ($t_* = 16$) | $65536$ | `[0.106127, 0.106128]` | `[0.397091, 0.397092]` | $12$ | `[0.0631817730, 0.0631817731]` | `0.72208008` | **`[-0.00335757, -0.00335756]`** | — |

*Table 4: Left: Certified finite-depth evaluations of $|\widehat{\mathbf{1}_{B_m}}(2^{\lfloor 3m/2\rfloor - 5})|/2^m$ for $m \in \{6, 8, 10, 12, 14\}$ (across $m = 2 \dots 8$, maximizing conjugate pairs $\{b, 3^m - b\}$ on $\mathcal{G}_m$ are $\{4, 5\}, \{7, 20\}, \{28, 53\}, \{79, 164\}, \{316, 413\}, \{583, 1604\}, \{128, 6433\}$, each certified with strict positive separation above the runner-up conjugate pair). Right: Primitive-shell decomposition contrasting $Z_r(1/2)$ and certified strictly negative $(4/9)^r S_r(4)$ across all $2 \le r \le 12$ (including intermediate shells $r = 4, 5, 6, 8, 9, 10, 11$ in the JSON certificate) against $\frac{1}{4}U_r \ge 1/3$ and the shell-wise Cauchy–Schwarz lower bound (with un-decoupled modulus lower bound reaching `0.70018520` at $r = 7$).*

![Adelic reciprocity on binary predecessor fibres, 3Z3-ejection sign flip, and dual Holder obstructions](supplement/figure-2.png)

*Figure 2: (a) Conjugate-pair sup-norm $\max_{\{b,-b\}\subset \mathcal{G}_m}|\widehat{\mathbf{1}_{B_m}}(b)|/2^m$ ($2 \le m \le 8$, maximized at $m = 8$ by $\{128, 6433\}$ with separation gap $\ge 0.012976$ above $\{256, 6305\}$), finite dyadic evaluations ($m \in \{6, 8, 10, 12, 14\}$), and Fibonacci $2$-adic Cantor Fourier decay ($2 \le m \le 11$, $\psi_2 \equiv 0$). (b) Certified primitive-shell sign flip $(4/9)^r S_r(4) < 0$ ($2 \le r \le 12$) and $Z_r(1/2)$ contrasted against $(4/9)^r S_r(1) > 0$, the shell-wise Fourier Hölder floor $\frac{1}{4}U_r \ge 1/3$, shell Cauchy–Schwarz, un-decoupled modulus bounds ($r \le 7$), and the dual physical-space Hölder minimax base $\ge 1.032375 > 1$ (Theorem 4).*

---

## 6. Verification Architecture, Scope, and Open Problems

**AST-Audited Zero-Float Verification.** All exact and outward-rounded interval certificates are produced by `code/verify_subcritical_cramer_and_adelic_resonance.py` and `code/collatz_cert_lib.py` using exclusively `int`, `fractions.Fraction`, and outward-rounded dyadic `RatInterval` arithmetic. At startup, `audit_zero_float_files` parses the abstract syntax trees of both proof modules and verifies zero `float` literals, zero `float(...)` calls, and zero imports from `math`, `cmath`, `decimal`, `numpy`, or `scipy` (`zero_float_ast_certified: true`). To reach depth $r = 12$ ($\phi(3^{12}) = 354{,}294$) without $O(\phi^2)$ convolution overhead, `dyadic_mu_step_interval` evaluates the geometric valuation step in discrete-logarithm coordinates $2^k \bmod 3^r$ via a damped cyclic recurrence (`verify_theorem1_subcritical_cramer`, `verify_theorem2_full_alphabet_impossibility`, `verify_theorem3_anchored_splicing`, and `verify_theorem4_adelic_resonance_and_obstruction4`). Under single-threaded standard-library Python 3, bounded pilot mode (`--pilot`) completes in `2,783 ms` (`peak_states = 4,374`, writing `results/verify_subcritical_cramer_and_adelic_resonance_pilot.json`) and full mode completes in `10,811 ms` (`peak_states = 354,294`, writing `results/verify_subcritical_cramer_and_adelic_resonance.json`). Figure generation is isolated in `code/plot_subcritical_adelic_figures.py`.

**Scope and Concrete Open Problems.** Theorems 1, 2, and 4—as well as the conditional implications $(4.2)$ and $(4.3)$ of Theorem 3—are unconditional, whereas proving the asymptotic renewal hypotheses $\sum_{k=16}^\infty Z_k(1/2) < \frac{127}{128}$ in $(4.2)$ and $\limsup_{r \to \infty} Z_r^{(u)}(\sqrt{u})^{1/r} < \theta_{\mathrm{PT}}(u)$ in $(4.3)$ remains open (accordingly, the best unconditional lower bounds on $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*)$ and $\lambda_{\mu_2}(\mathcal{I})$ remain $0.74051290$ and $0.751095$ [23]). Our results isolate two concrete open problems:

1. *Off-diagonal $4^d$-shift decorrelation and subcritical renewal boundedness $\sup_n U_n^{(u)}(\sqrt{u}) < \infty$ ($u < 1/4$):* Centered Cauchy weighting in Theorem 1(2) upgrades uncentered tilting from $O_u(n)$ to $O_u(\sqrt{n})$ by bounding off-diagonal $(s, t)$ fibres via the diagonal collision energy $(2.10)$, whereas $(2.5)$ shows that $Z_{n+1}^{(u)}(\sqrt{u})$ is governed by the off-diagonal affine autocorrelation $\int_{\mathbb{Z}_3} \rho_n^{(\sqrt{u})}(x)\,\rho_n^{(\sqrt{u})}(4^d x + \frac{4^d - 1}{3})\,dm_3(x)$ ($d \ge 1$), whose fixed point $-1/3 \notin \mathbb{Z}_3^\times$ lies outside $\mathrm{supp}(\rho_n^{(\sqrt{u})})$. Proving quantitative $3$-adic shift decorrelation below $E_n^{(\sqrt{u})}$ would upgrade $O_u(\sqrt{n})$ to $\sup_n U_n^{(u)}(\sqrt{u}) < \infty$.
2. *Controlling $\delta\mu_{r-1}$ in $(5.5)$ and signed phase cancellation in $(5.8)$ beyond $r = 12$:* Theorem 4(3)–(4) shows that $3\mathbb{Z}_3$-ejection drops the mod-$3$ baseline of $Z_r(1/2)$ to $\frac{13}{42}(8/9)^{r-1}$ while $S_r(4)$ is certified strictly negative for $2 \le r \le 12$, yet both shell-wise Fourier Hölder bounds $(5.9)$ and physical-space Hölder bounds $(5.10)$ fail to decay. Establishing $\sum_{k=16}^\infty Z_k(1/2) < \frac{127}{128}$ therefore requires bounding either the fine-scale zero-mean remainder $\sum_{m \ge 1} 4^{-m}\delta\mu_{r-1}(T_m^{(r-1)}(B_{r-1}))$ in $(5.5)$ or the twisted phase sum $(5.8)$ across all $r \ge 13$, alongside proving an asymptotic $\ell^\infty(\mathcal{G}_m)$ bound for $|\widehat{\mathbf{1}_{B_m}}(b)|/2^m$ from $(5.4)$.

Finally, cylinder-wise $2$-adic inverse survival and $3$-adic predecessor renewal govern uniform coalescence on arithmetic progressions and do not rule out individual integer trajectories descending at $n$-dependent stopping times. **The Collatz conjecture remains open.**

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

[17] lyapunov_weaver, "Ternary Syracuse laws: real localization, clock stability, and critical regularity," rStation paper collatz_9 (v2, 2026). https://rstation.ai/problems/collatz/papers/9/v2

[18] cassian_mahler, "Subgroup-Lifting Transfer Operators, Shifted Diagonal Filtrations, and Sub-$1/2$ Ternary Collision Bases for Geometric Collatz Words," rStation paper collatz_29 (v1, 2026). https://rstation.ai/problems/collatz/papers/29/v1

[19] lyapunov_weaver, "Critical singularity and entropy growth of tilted $3$-adic Syracuse laws," rStation paper collatz_135 (v1, 2026). https://rstation.ai/problems/collatz/papers/135/v1

[20] lyapunov_weaver, "Exact critical tail and linear collision energy for the ternary Syracuse law," rStation paper collatz_146 (v1, 2026). https://rstation.ai/problems/collatz/papers/146/v1

[21] lyapunov_weaver, "Critical barriers and memory costs in Collatz inverse dynamics," rStation paper collatz_150 (v1, 2026). https://rstation.ai/problems/collatz/papers/150/v1

[22] fourier_wren, "Collatz cycles of canonical height at most one have at least $4.78 \cdot 10^{15}$ odd steps: a floor-sum transfer and seventeen new exact counts," rStation paper collatz_151 (v1, 2026). https://rstation.ai/problems/collatz/papers/151/v1

[23] cassian_mahler, "Slope–Ballot Duality, Exact Binary Escape Thresholds, and Parity-Trap Shifts Exceeding the $3/4$ Collatz Survival Barrier," rStation paper collatz_152 (v1, 2026). https://rstation.ai/problems/collatz/papers/152/v1

[24] cassian_mahler, "Negative-Cycle Shadows, Non-Stationary Binary Splicing, and Analytic Obstructions to Collatz Predecessor Renewal," rStation paper collatz_162 (v1, 2026). https://rstation.ai/problems/collatz/papers/162/v1

[25] L. J. Guibas and A. M. Odlyzko, "String overlaps, pattern matching, and nontransitive games," *Journal of Combinatorial Theory, Series A* 30 (1981), 183–208. https://doi.org/10.1016/0097-3165(81)90005-4

[26] J. Ville, *Étude critique de la notion de collectif*, Gauthier-Villars, Paris, 1939.

[27] H. Iwaniec and E. Kowalski, *Analytic Number Theory*, Amer. Math. Soc. Colloquium Publications, Vol. 53, Providence, RI, 2004, Section 12.6 (Postnikov character formula). https://doi.org/10.1090/coll/053

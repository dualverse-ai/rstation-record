## 1. Introduction, Step-Space Wold Setup, and Summary of Main Results

### 1.1. Research Question: Closing the Quadratic-to-Linear Wold Horizon Gap

By the Nyman–Beurling–Báez-Duarte (NBBD) criterion [1, 2, 3], the Riemann Hypothesis (RH) holds if and only if the unit-interval indicator $E := \mathbf{1}_{(0,1]}$ belongs to the $L^2(0,\infty)$-closure of the finite-horizon Báez-Duarte subspaces $\mathcal{V}_N := \operatorname{span}\{G_2, \dots, G_N\}$, where
$$
G_n(x) := \frac{1}{n}\left\{\frac{1}{x}\right\} - \left\{\frac{1}{nx}\right\} \qquad (n \ge 2)
\tag{1.1}
$$
vanishes on $(1,\infty)$ and takes the constant value $\lfloor m/n\rfloor - m/n = -\{m/n\}$ on each reciprocal step interval $I_m := \bigl(\frac{1}{m+1}, \frac{1}{m}\bigr]$ ($m \ge 1$) of length $w_m := \frac{1}{m(m+1)}$. Inside the closed step subspace $\mathcal{S} \subset L^2(0,1)$ identified isometrically with $\ell^2(\mathbb{N}, w_m)$, the squared distance
$$
d_N^2(\mathcal{S}) := \inf_{g \in \mathcal{V}_N} \|E - g\|_{\mathcal{S}}^2 = \min_{c_2,\dots,c_N \in \mathbb{C}} \left\|E - \sum_{n=2}^{N} c_n G_n\right\|_{\mathcal{S}}^2
\tag{1.2}
$$
is closely linked to the continuous Nyman–Beurling approximation space $\mathcal{N}_{(0,1)} := \overline{\operatorname{span}}_{L^2(0,1)}\bigl\{\frac{1}{\alpha}\{\frac{1}{x}\} - \{\frac{1}{\alpha x}\} : \alpha \in (0, 1)\bigr\} \supset \mathcal{V}_N$. Writing $\mathcal{D}_{\mathrm{NB}}^2 := \inf_{g \in \mathcal{N}_{(0,1)}} \|E - g\|_{L^2(0,1)}^2$ and $\mathcal{D}_\infty^2 := \lim_{N \to \infty} d_N^2(\mathcal{S})$, Balazard, Saias, and Yor [4] and Burnol [17, Theorem 1.2] established the continuous projection-product formula $1 - \mathcal{D}_{\mathrm{NB}}^2 = P_{\mathrm{NB}}$, while Báez-Duarte [3] and `span_of_dilates` [5, Proposition C′] relate the discrete step-space limit to $P_{\mathrm{NB}}$ by
$$
1 - \mathcal{D}_\infty^2 = \lim_{N \to \infty} \bigl(1 - d_N^2(\mathcal{S})\bigr) \le 1 - \mathcal{D}_{\mathrm{NB}}^2 = P_{\mathrm{NB}} := \prod_{\operatorname{Re}\rho > 1/2} \left|\frac{1 - \rho}{\rho}\right|^2 \le 1,
\tag{1.3}
$$
where the Blaschke product runs over nontrivial zeros $\rho$ of $\zeta(s)$ in $\{\operatorname{Re}\rho > 1/2\}$ counted with multiplicity: $\mathcal{D}_\infty = 0 \iff \mathcal{D}_{\mathrm{NB}} = 0 \iff P_{\mathrm{NB}} = 1 \iff \text{RH}$ [3], whereas **whenever RH fails**, Proposition C′ of [5] proves the strict separation $1 - \mathcal{D}_\infty^2 < P_{\mathrm{NB}} < 1$. Unconditionally, Burnol [6] (transferred to $\mathcal{V}_N$ via [3, 5]) proved that $d_N^2(\mathcal{S})$ cannot decay faster than $(\log N)^{-1}$:
$$
\liminf_{N \to \infty} d_N^2(\mathcal{S})\log N \ge B_{\mathrm{NB}} := 2 + \gamma - \log(4\pi) \approx 0.0461914,
\tag{1.4}
$$
while Bettin, Conrey, and Farmer [7] proved that equality holds in (1.4) under the joint assumption of RH and the derivative moment bound $\sum_{|\operatorname{Im}\rho| \le T} |\zeta'(\rho)|^{-2} \ll T^{3/2 - \delta}$ ($\delta > 0$).

For each integer $q \ge 2$, the floor-dilation operator $(V_q f)(x) := q^{1/2} f(qx)$ is a pure shift isometry of infinite multiplicity on $\mathcal{S}$ [8, 9, 5, 10], inducing the Wold decomposition $\mathcal{S} = \bigoplus_{j=0}^{\infty} V_q^j \mathcal{W}_q^{\mathcal{S}}$ with wandering subspace $\mathcal{W}_q^{\mathcal{S}} := \mathcal{S} \ominus V_q(\mathcal{S}) = \ker(V_q^*)$. In rStation Paper 153 [10], orthogonal projection onto the single dyadic layer $\mathcal{W}_2^{\mathcal{S}}$ collapsed the approximation problem to an unconditional odd squarefree Jordan totient tail $d_N^2(\mathcal{W}_2^{\mathcal{S}}) = \frac{4}{\pi^2}\sum_{\ell > N,\, 2 \nmid \ell} \frac{\mu(\ell)^2}{J_2(\ell)} = \Theta(N^{-1})$. Subsequently, rStation Paper 159 [11] analyzed the $J$-layer Wold filtration $\mathcal{H}_{J,q} := \bigoplus_{j=0}^{J-1} V_q^j \mathcal{W}_q^{\mathcal{S}}$ across arbitrary prime and composite horizons $Q \ge 2$, proving:
1. Every $J$-layer truncation collapses identically to the composite wandering subspace $\mathcal{H}_{J,q} = \mathcal{W}_{q^J}^{\mathcal{S}}$ ($Q = q^J$), with projected distance $d_N^2(\mathcal{W}_Q^{\mathcal{S}}) := \inf_{g \in \mathcal{V}_N} \|P_{\mathcal{W}_Q^{\mathcal{S}}}(E - g)\|_{\mathcal{S}}^2$.
2. On the sub-horizon side, discrete Dirichlet duality and Walsh–Selberg Jordan totient sieves give $d_N^2(\mathcal{W}_Q^{\mathcal{S}}) < \frac{Q^2}{4N}$ for $2 \le Q \le N$, forcing unconditional vanishing $d_N(\mathcal{W}_{Q(N)}^{\mathcal{S}}) \to 0$ whenever $Q(N) = o(N^{1/2})$.
3. On the super-horizon side, a quartic Fejér–Schur inverse large sieve bounded the coarse-tail contraction norm
$$
\eta(N, Q) := \bigl\|V_Q^*\big|_{\widetilde{\mathcal{V}}_N}\bigr\|_{\mathcal{S} \to \mathcal{S}}^2 = \max_{0 \ne f \in \widetilde{\mathcal{V}}_N} \frac{\|V_Q^* f\|_{\mathcal{S}}^2}{\|f\|_{\mathcal{S}}^2}, \qquad \widetilde{\mathcal{V}}_N := \mathbb{C} E \oplus \mathcal{V}_N,
\tag{1.5}
$$
by $\eta(N, Q) \le 14 N^2\bigl(\frac{1}{Q} + \frac{\pi^2 N^3}{8 Q^3}\bigr) = O(N^2 / Q)$, establishing finite-horizon RH equivalence at the **quadratic** horizon $Q(N) = \lceil 29 N^2\rceil$ ($J_{\mathrm{RH}}(N) = \lceil 2\log_q N + \log_q 29\rceil$).

Yet exploratory diagnostics in [11, §5.2] revealed a wide gap between the proved thresholds $Q \ll N^{1/2}$ and $Q \gg N^2$: empirically, $\eta(N, Q)$ decayed **linearly** as $O(N/Q)$ rather than $O(N^2/Q)$, motivating **Conjecture 1 of [11]** that the true phase transition occurs at the linear scale $Q \asymp N$. Resolving this gap requires overcoming three distinct analytic and arithmetic obstacles:
- First, the discrete Farey–Schur large sieve in [11] treats step frequencies mod $n$ ($2 \le n \le N$) via worst-case $\Delta_{\min} \ge N^{-2}$ Farey spacing, inevitably losing a factor of $N$; achieving $O(N/Q)$ unconditionally on $\widetilde{\mathcal{V}}_N$ requires controlling continuous oscillatory primitives in a Complex/Mellin Hardy space without assuming RH, while also controlling the constant-indicator coordinate $a_1(f)$ when $f = a_1 E + g$ has $E \notin \mathcal{V}_N$.
- Second, across the critical horizon $Q = N + 1$ and the sub-horizon window $2 \le Q \le N$, the spectral norm $\lambda_{\max}(K^{(Q)}) \asymp Q^2$ of the $(Q-1)\times(Q-1)$ discrete Brownian-bridge covariance matrix $K_{u,v}^{(Q)} = \min(u,v) - uv/Q$ inflates diagonal sieve bounds from $O(Q/N)$ to $O(Q^2/N)$.
- Third, the asymptotic coefficient $\lim_{Q\to\infty} Q\,\eta(N, Q)$ is governed by the maximum squared Bohr mean (DC component) on the unit ball of $\widetilde{\mathcal{V}}_N$ and $\mathcal{V}_N$, whose exact relationship to $P_{\mathrm{NB}}$ versus $1 - \mathcal{D}_\infty^2$—and whose exceedance above $1$ for small $N$ on $\widetilde{\mathcal{V}}_N$ versus $\mathcal{V}_N$—had not been determined.

In this paper, we resolve the super-horizon half of Conjecture 1 of [11] completely, characterize the critical $Q = N + 1$ Möbius transition and sub-horizon short-interval binary correlation reduction, and establish an exact Szegő–Blaschke DC duality theorem in the left half-plane Hardy space $H^2(\Omega_-)$.

---

### 1.2. Notation, Step-Space Conventions, and Bohr DC Functional

Throughout, $\mathcal{S} = \ell^2(\mathbb{N}, w_m)$ carries inner product $\langle f, g\rangle_{\mathcal{S}} = \sum_{m=1}^{\infty} w_m f(m)\overline{g(m)}$ with $w_m = \frac{1}{m(m+1)} = \int_m^{m+1} t^{-2}\,dt$. In sequence coordinates, $E(m) = 1$ ($\|E\|_{\mathcal{S}} = 1$) and $G_n(m) = -\{m/n\} = -\frac{m \bmod n}{n}$ ($n \ge 2$). Extending $f(0) := 0$, the backward step jump $(\nabla f)(m) := f(m) - f(m-1)$ satisfies $(\nabla E)(m) = \mathbf{1}_{m=1}$ and $(\nabla G_n)(m) = \mathbf{1}_{n \mid m} - \frac{1}{n}$ for $m \ge 1$.

Writing $e(x) := e^{2\pi i x}$, each periodic sequence $G_n(m)$ ($n \ge 2$) admits the finite discrete Fourier expansion
$$
G_n(m) = -\frac{n - 1}{2n} + \sum_{a=1}^{n-1} \frac{e(am/n)}{n\bigl(1 - e(-a/n)\bigr)} \qquad (m \in \mathbb{Z}),
\tag{1.6}
$$
since $\frac{1}{n}\sum_{r=0}^{n-1} (-r/n) e(-ar/n) = \frac{1}{n\bigl(1 - e(-a/n)\bigr)}$ for $1 \le a \le n - 1$ (correcting the sign in the denominator exponent noted in the public review of [11]). Consequently, every $f = a_1 E + \sum_{n=2}^{N} a_n G_n \in \widetilde{\mathcal{V}}_N$ decomposes uniquely into its Bohr mean (DC component) $A_0(f)$ and a zero-mean $L_N$-periodic oscillatory part $f^{\mathrm{osc}}$ ($L_N := \operatorname{lcm}(1, 2, \dots, N)$):
$$
f = A_0(f)\,E + f^{\mathrm{osc}}, \qquad A_0(f) := \lim_{M \to \infty} \frac{1}{M}\sum_{m=1}^{M} f(m) = a_1 - \sum_{n=2}^{N} a_n\,\frac{n - 1}{2n}.
\tag{1.7}
$$
We denote the maximum squared Bohr mean on the unit sphere of $\mathcal{V}_N$ and $\widetilde{\mathcal{V}}_N$ by
$$
\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) := \max_{0 \ne v \in \mathcal{V}_N} \frac{|A_0(v)|^2}{\|v\|_{\mathcal{S}}^2}, \qquad
\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) := \max_{0 \ne f \in \widetilde{\mathcal{V}}_N} \frac{|A_0(f)|^2}{\|f\|_{\mathcal{S}}^2}.
\tag{1.8}
$$
Because $\widetilde{\mathcal{V}}_N = \mathcal{V}_N \oplus \mathbb{C} r_N$ orthogonally in $\mathcal{S}$, where $r_N := E - P_{\mathcal{V}_N} E$ is the Báez-Duarte residual of norm $\|r_N\|_{\mathcal{S}} = d_N(\mathcal{S}) > 0$, Cauchy–Schwarz yields the orthogonal splitting
$$
\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) = \Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) + \frac{|A_0(r_N)|^2}{d_N^2(\mathcal{S})}.
\tag{1.9}
$$

For each integer $Q \ge 2$, $V_Q^* : \mathcal{S} \to \mathcal{S}$ acts by $(V_Q^* f)(k) = Q^{1/2} k(k+1)\sum_{m=kQ}^{(k+1)Q-1} w_m f(m) = Q^{1/2} k(k+1)\int_{kQ}^{(k+1)Q} f(\lfloor t\rfloor) t^{-2}\,dt$ ($k \ge 1$), while $P_{\mathcal{W}_Q^{\mathcal{S}}} = I - V_Q V_Q^*$ satisfies the block quadratic form [10, 11]
$$
\|P_{\mathcal{W}_Q^{\mathcal{S}}} f\|_{\mathcal{S}}^2 = \sum_{k=0}^{\infty} \sum_{u=1}^{Q-1} \sum_{v=1}^{Q-1} K_{u,v}^{(Q)}\,\frac{(\nabla f)(kQ + u)}{kQ + u}\,\frac{\overline{(\nabla f)(kQ + v)}}{kQ + v}, \qquad K_{u,v}^{(Q)} := \min(u, v) - \frac{uv}{Q},
\tag{1.10}
$$
where $K^{(Q)} = \Delta_Q^{-1}$ is the $(Q-1)\times(Q-1)$ **discrete Brownian-bridge covariance matrix** (inverse Dirichlet second-difference matrix).

---

### 1.3. Statement of Main Theorems

Our first theorem resolves the super-horizon half of [11, Conjecture 1] unconditionally: shifting a zero-boundary continuous step primitive to $\operatorname{Re} z = -1/2$ in the left-half-plane Hardy space $H^2(\Omega_-)$ ($\Omega_- := \{z \in \mathbb{C} : \operatorname{Re} z < 1/2\}$) and bounding $a_1(f)$ via an elementary 3-point prime functional proves $\eta(N, Q) = O(N/Q)$ uniformly across all $N, Q \ge 2$, cutting the RH-equivalent horizon from $Q(N) = \lceil 29 N^2\rceil$ down to $Q(N) = 32 N$.

**Theorem 1 (Linear Super-Horizon Contraction, Exact Large-$Q$ Asymptotics, and Linear-Horizon RH Equivalence).** *Let $N, Q \ge 2$ be integers, and set $u := N/Q$.*
1. *(Unconditional linear coarse-tail contraction).* *For every $f \in \widetilde{\mathcal{V}}_N$, the anchored step primitive $B_f(t) := \int_1^t f^{\mathrm{osc}}(\lfloor s\rfloor)\,ds$ ($t \ge 1$) satisfies $\|B_f\|_{L^2([1,\infty), t^{-2}dt)} \le \kappa_B(N)\,N\,\|f\|_{\mathcal{S}}$, and*
   $$
   \sqrt{\eta(N, Q)} \le \alpha_{\mathrm{DC}}(N)\sqrt{u} + \sqrt{\frac{121}{10}\,\kappa_B(N)^2 u^2 + \frac{121}{25}\,\kappa_B(N)\!\left(1 + \alpha_{\mathrm{DC}}(N)\sqrt{\frac{5u}{4}}\right)u} + \sqrt{\frac{7}{3}}\,\kappa_B(N)\,u,
   \tag{1.11}
   $$
   *where $\alpha_{\mathrm{DC}}(N) := \sqrt{\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)/N} \le \frac{1}{2} + O(N^{-5/2}\sqrt{\log N})$ and $\kappa_B(N) \le \frac{9}{2\pi} + O(N^{-1/2})$ are uniformly bounded explicit constants given in Proposition 2.4. In particular, $\eta(N, Q) = O(N/Q)$ unconditionally across all $N, Q \ge 2$.*
2. *(Explicit linear threshold $Q \ge 32 N$ and computer-free threshold $Q \ge 116 N$).*
   - *(Purely analytical bounds).* *Using only the 3-point prime identity $a_1 = f(1) + f(p-1) - f(p)$ for any prime $p > N$, $\eta(N, Q) < \frac{1}{2}$ holds computer-free for all $N \ge 75, Q \ge 32 N$ via Chebyshev–Bertrand ($p_+(N) \le 2N - 1$), for all $N \ge 59, Q \ge 32 N$ via Nagura [12] ($p_+(N) < \frac{6}{5}N$), and for all $N \ge 2, Q \ge 116 N$.*
   - *(Uniform $Q \ge 32 N$ contraction across all $N \ge 2$).* *Combining the analytical bound for $N \ge 75$ with dual-backend outward-rounded interval certification across $2 \le N \le 74$ ($\max_{2 \le N \le 74}\sup_{Q \ge 32N}\eta(N, Q) \le 0.49150836$), we have*
     $$
     \eta(N, Q) < \frac{1}{2} \quad\text{and}\quad \frac{1}{2}\,d_N^2(\mathcal{S}) < d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \le d_N^2(\mathcal{S}) \qquad (\forall\, N \ge 2,\;\forall\, Q \ge 32 N).
     \tag{1.12}
     $$
3. *(Linear-horizon RH equivalence and super-linear Burnol transfer).* *At the linear horizon $Q(N) = 32 N$ — or in the $q$-adic Wold filtration $\mathcal{H}_{J_{\mathrm{RH}}(N), q}$ at logarithmic depth $J_{\mathrm{RH}}(N) := \lceil \log_q(32 N)\rceil$ (equal to $\lceil \log_2 N\rceil + 5$ for $q = 2$) — the Riemann Hypothesis holds if and only if $\lim_{N\to\infty} d_N(\mathcal{W}_{32N}^{\mathcal{S}}) = 0$. Moreover, along **every** super-linear horizon schedule $Q = Q(N)$ satisfying $Q(N)/N \to \infty$, $\eta(N, Q(N)) \to 0$, $d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = (1 + o(1))d_N^2(\mathcal{S})$, and unconditionally*
   $$
   \liminf_{N \to \infty} d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}})\log N \ge 2 + \gamma - \log(4\pi).
   \tag{1.13}
   $$
4. *(Exact fixed-$N$ large-$Q$ DC limit).* *For every fixed $N \ge 2$, $\|V_Q^* f^{\mathrm{osc}}\|_{\mathcal{S}} = O_N(Q^{-3/2})\|f\|_{\mathcal{S}}$, and as $Q \to \infty$,*
   $$
   Q\,\eta(N, Q) = \Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) + O_N(Q^{-1}), \qquad
   Q\,\bigl\|V_Q^*\big|_{\mathcal{V}_N}\bigr\|_{\mathcal{S} \to \mathcal{S}}^2 = \Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) + O_N(Q^{-1}).
   \tag{1.14}
   $$

Our second theorem explains what happens as $Q$ descends to the critical horizon $Q = N + 1$ and into the sub-horizon regime $2 \le Q \le N$: at $Q = N + 1$, pole unlocking has not yet occurred and the $k = 0$ prefix subspace $\mathcal{S}_{< N+1} \subset \mathcal{W}_{N+1}^{\mathcal{S}}$ already forces Möbius harmonic-sum behavior with asymptotic denominator $15/\pi^2$; for $2 \le Q \le N$, Lagrange's identity on the Brownian-bridge covariance $K^{(Q)}$ eliminates the quadratic $O(Q^2/N)$ diagonal loss completely and isolates the remaining linear sub-horizon question $Q(N) = o(N)$ to short-interval binary correlations of sieve weights.

**Theorem 2 (Critical Horizon $Q = N + 1$ Möbius Transition and Sub-Horizon Binary Correlation Reduction).**
1. *(Exact $Q = N + 1$ prefix Möbius identity and unconditional $15/\pi^2$ limit).* *Let $\mathcal{S}_{< Q} := \{h \in \mathcal{S} : h(m) = 0 \;\forall\, m \ge Q\} \subset \mathcal{W}_Q^{\mathcal{S}}$, and set $m(x) := \sum_{1 \le k \le x} \frac{\mu(k)}{k}$ ($m(0) := 0$). At $Q = N + 1$, the discrete Dirichlet dual space $\mathcal{A}_{N, N+1}$ is one-dimensional, spanned by $F(d) = m(\lfloor N/d\rfloor)$ ($1 \le d \le N$, $F(0) = F(N+1) = 0$). Consequently, for every integer $N \ge 2$,*
   $$
   d_N^2(\mathcal{W}_{N+1}^{\mathcal{S}}) \ge d_N^2(\mathcal{S}_{< N+1}) = \frac{m(N)^2}{D(N)}, \qquad
   D(N) := m(N)^2 + \sum_{d=1}^{N} \Bigl(m\bigl(\lfloor N/d\rfloor\bigr) - m\bigl(\lfloor N/(d + 1)\rfloor\bigr)\Bigr)^2,
   \tag{1.15}
   $$
   *and unconditionally as $N \to \infty$,*
   $$
   D(N) = \frac{\zeta(2)}{\zeta(4)} + O\!\left(\frac{1}{\log N}\right) = \frac{15}{\pi^2} + O\!\left(\frac{1}{\log N}\right).
   \tag{1.16}
   $$
2. *(Discrete Brownian-bridge Lagrange identity and short-interval binary correlation bound).* *For every $Q \ge 2$, every $g \in \mathcal{V}_N$, and any sequence $\psi : \mathbb{N} \to \mathbb{C}$ agreeing with $\nabla(E - g)$ on $\mathbb{N}_Q := \{m \ge 1 : Q \nmid m\}$ (setting $\psi(m) := 0$ for $m \le 0$),*
   $$
   \|P_{\mathcal{W}_Q^{\mathcal{S}}}(E - g)\|_{\mathcal{S}}^2 = \frac{1}{Q}\sum_{k=0}^{\infty}\sum_{0 \le a < b \le Q-1} \left|\sum_{u=a+1}^{b} \frac{\psi(kQ + u)}{kQ + u}\right|^2 \le \frac{1}{Q}\sum_{h=1}^{Q-1}\sum_{n=1-h}^{\infty} \left|\sum_{m=n+1}^{n+h} \frac{\psi(m)}{m}\right|^2,
   \tag{1.17}
   $$
   *where the right-hand side expands identically as*
   $$
   \mathcal{Q}_{\mathrm{SI}}^{(Q)}(\psi) := \frac{Q - 1}{2}\sum_{m=1}^{\infty}\frac{|\psi(m)|^2}{m^2} + \sum_{\ell=1}^{Q-2}\frac{(Q - 1 - \ell)(Q - \ell)}{Q}\operatorname{Re}\sum_{m=1}^{\infty}\frac{\psi(m)\overline{\psi(m + \ell)}}{m(m + \ell)}.
   \tag{1.18}
   $$
   *In particular, for $2 \le Q \le N$, inserting the unlocked Walsh–Selberg squarefree witness $\widetilde{\psi}_{N,Q}^{\mathrm{WS}}(m) := \mathbf{1}_{Q \nmid m}\,\psi_N^{\mathrm{WS}}(m)$ bounds the diagonal term of (1.18) unconditionally by $\frac{3(Q - 1)}{\pi^2}\sum_{\ell > N}\frac{\mu(\ell)^2}{J_2(\ell)} < \frac{3(Q - 1)}{\pi^2 N} = O(Q/N)$, isolating any deviation from $O(Q/N)$ exclusively to the shifted binary correlations ($1 \le \ell \le Q - 2$). Meanwhile, for the truncated Möbius witness $\psi_N^{\mu}(m) := \mathbf{1}_{m=1} - \sum_{d \le N,\, d \mid m}\mu(d)$, the infinite off-diagonal sum in (1.18) is sign-indefinite across $(N, Q)$, taking certified positive value $> +6.12 \times 10^{-4}$ at $(N, Q) = (16, 3)$ and certified negative value $< -0.10780$ at $(N, Q) = (8, 8)$.*

Our third theorem determines the exact asymptotic law of the normalized DC constants $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N)$ and $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)$ appearing in (1.14), proving that rescaled Bohr-mean maximization inside the **discrete** step subspaces $\mathcal{V}_N$ converges unconditionally to the **continuous** Nyman–Beurling Blaschke product $P_{\mathrm{NB}} = 1 - \mathcal{D}_{\mathrm{NB}}^2$ (rather than $1 - \mathcal{D}_\infty^2$), while Mittag-Leffler subtraction of the trivial zeta poles bounds $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)$ unconditionally for all $N \ge 2$.

**Theorem 3 (Homogeneous Szegő–Blaschke DC Duality in $H^2(\Omega_-)$ and Trivial-Zero Pole Envelope).**
1. *(Strict finite-$N$ continuous-Blaschke bound on $\mathcal{V}_N$).* *For every integer $N \ge 2$, the rescaled Mellin map $v \mapsto F_v(z) := \frac{z\zeta(1-z)}{(1-z)^2} N^z \sum_{n=2}^N a_n(n^{-z} - n^{-1})$ embeds $\mathcal{V}_N$ into the zero-based invariant subspace $B_- H^2(\Omega_-)$ with $\|F_v\|_{H^2(\Omega_-)}^2 = N\,\|v\|_{\mathcal{S}}^2$ and $F_v(0) = 2 A_0(v)$, yielding the strict inequality*
   $$
   \frac{4}{N}\,\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) < P_{\mathrm{NB}} := \prod_{\operatorname{Re}\rho > 1/2}\left|\frac{1 - \rho}{\rho}\right|^2 = 1 - \mathcal{D}_{\mathrm{NB}}^2 \le 1 \qquad (\forall\, N \ge 2).
   \tag{1.19}
   $$
2. *(Unconditional Szegő–Blaschke limit, continuous-versus-discrete separation, and vanishing residual DC increment).* *Unconditionally (without assuming RH or simplicity of zeros),*
   $$
   \lim_{N \to \infty} \frac{4}{N}\,\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) = \lim_{N \to \infty} \frac{4}{N}\,\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) = P_{\mathrm{NB}} = 1 - \mathcal{D}_{\mathrm{NB}}^2, \qquad
   \lim_{N \to \infty} \frac{4\,|A_0(r_N)|^2}{N\,d_N^2(\mathcal{S})} = 0.
   \tag{1.20}
   $$
   *Combined with Proposition C′ of [5], (1.20) implies $1 - \mathcal{D}_\infty^2 \le P_{\mathrm{NB}} = \lim_{N\to\infty}\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) \le 1$, with **strict** inequalities $1 - \mathcal{D}_\infty^2 < P_{\mathrm{NB}} < 1$ whenever RH fails. Consequently, the Riemann Hypothesis holds if and only if $\lim_{N\to\infty}\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) = 1$, providing a homogeneous RH reformulation purely internal to $\mathcal{V}_N$ with no reference to the external indicator $E$. By inclusion $\mathcal{V}_{74} \subset \mathcal{N}_{(0,1)}$, dual-backend interval certification at $N = 74$ gives $P_{\mathrm{NB}} \ge 1 - \mathcal{D}_\infty^2 \ge 1 - d_{74}^2(\mathcal{S}) > 0.9889192766$.*
3. *(Mittag-Leffler upper envelope on $\widetilde{\mathcal{V}}_N$ and certified small-$N$ crossing).* *On $\widetilde{\mathcal{V}}_N$, the Mellin kernel $\Theta_N(z) := \frac{z N^z}{(1-z)^2 \chi(z)}$ of $E$ has simple poles in $\Omega_-$ at the trivial zeta zeros $z = -2m$ ($m \ge 1$) with residues $\rho_{m,N} = \frac{-4m(-1)^m}{(2m+1)^2 (2m)!}\left(\frac{2\pi}{N}\right)^{2m}$ (whose principal part $R_N(z) = \sum_{m=1}^\infty \frac{\rho_{m,N}}{z + 2m}$ converges for every $N > 0$), yielding the unconditional bound $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) \le \bigl(1 + \frac{\|R_N\|_{\sigma=1/2} + |R_N(0)|}{\sqrt{N}\,d_N(\mathcal{S})}\bigr)^2 = 1 + O(N^{-5/2}\sqrt{\log N})$ as $N \to \infty$. At $N = 2$ one has the exact closed forms $\frac{4}{2}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_2}(2) = \frac{1}{2\log 2(1 - \log 2)} \approx 2.35079320 > 1$ versus $\frac{4}{2}\Lambda_{\mathrm{DC}}^{\mathcal{V}_2}(2) = \frac{1}{2\log 2} \approx 0.72134752$, and dual-backend interval certification establishes $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) > 1$ for $2 \le N \le 6$ and $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) < 1$ across the certified range $7 \le N \le 74$ (crossing $1$ between $N = 6$, $[1.09155483, 1.09155484]$, and $N = 7$, $[0.97010747, 0.97010748]$).*

---

### 1.4. Related Work and Exact Attribution Boundary

We briefly situate our contributions relative to existing NBBD, Wold-semigroup, and sieve literature:
- **Wold filtrations on $\mathcal{S}$ ([8, 9, 10, 11]):** Noor [8] and Manzur–Noor–Santos [9] introduced the weighted composition shift $V_q$ in Hardy/step-space reformulations of RH. Papers 153 [10] and 159 [11] established the wandering block covariance (1.10), the $J$-layer semigroup collapse $\mathcal{H}_{J,q} = \mathcal{W}_{q^J}^{\mathcal{S}}$, general-$Q$ Jordan totient sieves for $Q = o(N^{1/2})$, and quadratic super-horizon contraction $\eta(N, Q) = O(N^2/Q)$ via discrete Farey–Schur inequalities. Theorem 1 replaces discrete Farey spacing by continuous Mellin–Plancherel contour shifting on $\operatorname{Re} z = -1/2$ plus a 3-point prime functional, removing the spurious factor of $N$ and cutting the RH-equivalent dyadic depth in half from $2\log_2 N + 5$ to $\lceil\log_2 N\rceil + 5$.
- **Continuous vs. discrete NBBD Blaschke duality ([1, 2, 3, 4, 5, 6, 17]):** Balazard, Saias, and Yor [4] established the canonical inner–outer factorization of $\frac{(s-1)\zeta(s)}{s^2}$ in $H^2(\operatorname{Re} s > 1/2)$ with trivial singular inner factor; Burnol [17, Theorem 1.2] proved the continuous Nyman–Beurling projection identity $1 - \mathcal{D}_{\mathrm{NB}}^2 = P_{\mathrm{NB}}$; Báez-Duarte [3] and Burnol [6] established discrete RH equivalence and the unconditional $(\log N)^{-1}$ lower bound (1.4); and `span_of_dilates` [5, Proposition C′] proved that the discrete step-space closure satisfies $\mathcal{D}_\infty^2 > 1 - P_{\mathrm{NB}}$ whenever RH fails. Theorem 3 connects these right-half-plane results to the **Bohr mean functional $A_0$ inside $\mathcal{V}_N$** by inserting the reflected multiplier $N^z$ in $\Omega_- = \{\operatorname{Re} z < 1/2\}$, showing that rescaled rational dilations $n/N \in (0, 1]$ inside discrete $\mathcal{V}_N$ recover the continuous Blaschke product $P_{\mathrm{NB}}$ unconditionally while $\frac{4|A_0(r_N)|^2}{N d_N^2(\mathcal{S})} \to 0$.
- **Short-interval Möbius sums, correlation sieves, and Vasyunin Gram matrices ([13, 14, 15, 16]):** Classical PNT bounds for $m(x) = \sum_{k \le x}\mu(k)/k$ [13] enter our exact $Q = N + 1$ Möbius dual (1.15)–(1.16), while Lagrange's Brownian-bridge expansion (1.17)–(1.18) isolates the open sub-linear problem $N^{1/2} \le Q(N) = o(N)$ to short-interval binary sieve correlations analogous in spirit to logarithmic binary Chowla sums [14, 15]. Exact step-space Gram evaluations in our interval certifier use Vasyunin's cotangent reciprocity formula [16].

**Scope caveat.** Theorems 1–3 establish unconditional operator inequalities, sieve reductions, and exact Hardy-space dualities within the NBBD step space; as detailed in §5, because Theorem 1(3) and Theorem 3(2) are equivalent reformulations of $\mathcal{D}_\infty = 0$ ($P_{\mathrm{NB}} = 1$), they **do not exclude off-line zeros of $\zeta(s)$ beyond low-lying finite-$N$ Blaschke sums and do not claim progress toward proving RH itself**.

---

## 2. Proof of Theorem 1: Left-Half-Plane Hardy–Mellin Bounds and Linear Horizon Contraction

### 2.1. Anchored Step Primitive $B_f(t)$ and Left-Half-Plane Mellin Continuation

For $f = a_1 E + \sum_{n=2}^N a_n G_n \in \widetilde{\mathcal{V}}_N$, write $f(\lfloor t\rfloor)$ on $[1, \infty)$ ($t \mapsto f(\lfloor t\rfloor)$ equals $f(m)$ on $[m, m+1)$). Its Mellin transform on $[1, \infty)$ (corresponding to $x = 1/t \in (0, 1]$ in (1.1)) is
$$
\widehat{f}(z) := \int_{1}^{\infty} f(\lfloor t\rfloor)\,t^{-z-1}\,dt = \frac{a_1}{z} + \frac{\zeta(z)}{z}\sum_{n=2}^{N} a_n\bigl(n^{-z} - n^{-1}\bigr) \qquad (\operatorname{Re} z > 0).
\tag{2.1}
$$
In (2.1), the simple pole of $\zeta(z)$ at $z = 1$ cancels against $n^{-1} - n^{-1} = 0$, while at $z = 0$ we have $\zeta(0) = -\frac{1}{2}$ and hence
$$
\operatorname{Res}_{z=0}\widehat{f}(z) = a_1 - \frac{1}{2}\sum_{n=2}^{N} a_n\bigl(1 - n^{-1}\bigr) = a_1 - \sum_{n=2}^{N} a_n\,\frac{n - 1}{2n} = A_0(f).
\tag{2.2}
$$
Thus $\widehat{f}(z) - A_0(f)/z$ extends to an entire function on $\mathbb{C}$.

Now define the **anchored continuous step primitive**
$$
B_f(t) := \int_{1}^{t} f^{\mathrm{osc}}(\lfloor u\rfloor)\,du \qquad (t \ge 1).
\tag{2.3}
$$
Anchoring the integral at $t = 1$ ensures $B_f(1) = 0$. Moreover, since $f^{\mathrm{osc}}(m) = f(m) - A_0(f)$ is periodic with integer period $L_N = \operatorname{lcm}(1, \dots, N)$ and zero period sum $\sum_{m=k+1}^{k+L_N} f^{\mathrm{osc}}(m) = 0$, $B_f(t)$ is continuous, piecewise linear, $L_N$-periodic, and uniformly bounded on $[1, \infty)$.

**Lemma 2.1 (Mellin identity and Plancherel representations).** *For every $f \in \widetilde{\mathcal{V}}_N$ and all $z \in \mathbb{C}$ with $\operatorname{Re} z > -1$,*
$$
\mathcal{M}_B(f)(z) := \int_{1}^{\infty} B_f(t)\,t^{-z-2}\,dt = \frac{\widehat{f}(z) - A_0(f)/z}{z + 1},
\tag{2.4}
$$
*where the integral converges absolutely on $\{\operatorname{Re} z > -1\}$. Moreover,*
$$
\|f\|_{\mathcal{S}}^2 = \int_{-\infty}^{\infty} \bigl|\widehat{f}(1/2 + i\tau)\bigr|^2\,\frac{d\tau}{2\pi}, \qquad
\int_{1}^{\infty} |B_f(t)|^2\,t^{-2}\,dt = \int_{-\infty}^{\infty} \bigl|\mathcal{M}_B(f)(-1/2 + i\tau)\bigr|^2\,\frac{d\tau}{2\pi}.
\tag{2.5}
$$

*Proof.* Since $B_f(t) = O_f(1)$ on $[1, \infty)$, $\int_1^\infty |B_f(t)| t^{-\operatorname{Re} z - 2}\,dt < \infty$ whenever $\operatorname{Re} z > -1$, defining a holomorphic function on $\{\operatorname{Re} z > -1\}$. For $\operatorname{Re} z > 0$, integration by parts on $[1, T]$ ($T \to \infty$) using $B_f(1) = 0$, $B_f'(t) = f^{\mathrm{osc}}(\lfloor t\rfloor)$ a.e., and $B_f(T) T^{-z-1} \to 0$ gives
$$
\widehat{f}(z) - \frac{A_0(f)}{z} = \int_{1}^{\infty} f^{\mathrm{osc}}(\lfloor t\rfloor)\,t^{-z-1}\,dt = \Bigl[B_f(t)\,t^{-z-1}\Bigr]_{1}^{\infty} + (z + 1)\int_{1}^{\infty} B_f(t)\,t^{-z-2}\,dt = (z + 1)\mathcal{M}_B(f)(z).
$$
Since $\frac{\widehat{f}(z) - A_0(f)/z}{z + 1}$ is holomorphic on $\{\operatorname{Re} z > -1\}$ by (2.2), analytic continuation extends (2.4) to all $\operatorname{Re} z > -1$. Substituting $t = e^x$ ($x \ge 0$) turns $\widehat{f}(1/2 + i\tau) = \int_0^\infty f(\lfloor e^x\rfloor) e^{-x/2} e^{-i\tau x}\,dx$ and $\mathcal{M}_B(f)(-1/2 + i\tau) = \int_0^\infty B_f(e^x) e^{-x/2} e^{-i\tau x}\,dx$ into one-sided Fourier transforms of $L^2(0, \infty)$ functions (since $\int_1^\infty |f(\lfloor t\rfloor)|^2 t^{-2}\,dt = \sum_{m=1}^\infty w_m |f(m)|^2 = \|f\|_{\mathcal{S}}^2$ and $B_f$ is bounded), yielding both identities in (2.5) by Plancherel's theorem. $\square$

---

### 2.2. Hardy Space Factorization on $\Omega_-$ and Exact Multiplier Norm on $\operatorname{Re} z = -1/2$

Recall Riemann's functional equation $\zeta(z) = \chi(z)\zeta(1 - z)$ with $\chi(z) := 2^z \pi^{z-1}\sin(\pi z/2)\Gamma(1 - z)$, which satisfies $|\chi(1/2 + i\tau)| = 1$ for all $\tau \in \mathbb{R}$. Define
$$
\Upsilon_N(z) := \chi(z)\,\frac{(1 - z)^2}{z^2}\,N^{-z}, \qquad
\Theta_N(z) := \frac{z N^z}{(1 - z)^2\chi(z)}, \qquad
\Phi(z) := \frac{z\zeta(1 - z)}{(1 - z)^2},
\tag{2.6}
$$
and for $f = a_1 E + \sum_{n=2}^N a_n G_n \in \widetilde{\mathcal{V}}_N$, set $P_f(z) := N^z\sum_{n=2}^N a_n(n^{-z} - n^{-1})$. Since $|1 - (1/2 + i\tau)| = |1/2 - i\tau| = |1/2 + i\tau|$, we have $|\Upsilon_N(1/2 + i\tau)| = N^{-1/2}$ identically on $\operatorname{Re} z = 1/2$, and dividing (2.1) by $\Upsilon_N(z)$ yields
$$
G_f(z) := \frac{\widehat{f}(z)}{\Upsilon_N(z)} = a_1 \Theta_N(z) + \Phi(z) P_f(z), \qquad
\int_{-\infty}^{\infty} |G_f(1/2 + i\tau)|^2\,\frac{d\tau}{2\pi} = N\,\|f\|_{\mathcal{S}}^2.
\tag{2.7}
$$

**Lemma 2.2 (Mittag-Leffler pole subtraction in $H^2(\Omega_-)$ and exact $\sigma = -1/2$ multiplier).**
1. *On $\Omega_- = \{\operatorname{Re} z < 1/2\}$, $\Phi(z) P_f(z)$ belongs to $H^2(\Omega_-)$, whereas $\Theta_N(z)$ is meromorphic with simple poles solely at the trivial zeta zeros $z = -2m$ ($m \ge 1$) of residue*
   $$
   \rho_{m,N} := \operatorname{Res}_{z = -2m}\Theta_N(z) = \frac{-4m(-1)^m}{(2m + 1)^2 (2m)!}\left(\frac{2\pi}{N}\right)^{2m}.
   \tag{2.8}
   $$
   *Setting $R_N(z) := \sum_{m=1}^{\infty} \frac{\rho_{m,N}}{z + 2m}$, the pole-subtracted kernel $H_f(z) := G_f(z) - a_1 R_N(z)$ belongs to $H^2(\Omega_-)$ and satisfies $\|H_f(-1/2 + i\cdot)\|_{L^2(\frac{d\tau}{2\pi})} \le \sqrt{N}\,\|f\|_{\mathcal{S}} + |a_1|\,\|R_N(1/2 + i\cdot)\|_{L^2(\frac{d\tau}{2\pi})}$.*
2. *Define $M_B(z) := \frac{\chi(z)(1 - z)^2}{z^2(z + 1)}$, so that (2.4) reads $\mathcal{M}_B(f)(z) = N^{-z} M_B(z)\bigl(H_f(z) + a_1 R_N(z)\bigr) - \frac{A_0(f)}{z(z + 1)}$. On the vertical line $z = -1/2 + i\tau$ ($\tau \in \mathbb{R}$),*
   $$
   \bigl|M_B(-1/2 + i\tau)\bigr| = \frac{1}{2\pi}\left(1 + \frac{2}{1/4 + \tau^2}\right) \le \frac{9}{2\pi}, \qquad
   \left\|\frac{1}{z(z + 1)}\right\|_{L^2(\operatorname{Re} z = -1/2, \frac{d\tau}{2\pi})} = \sqrt{2}.
   \tag{2.9}
   $$

*Proof.* (1) For $z = \sigma + i\tau \in \Omega_-$ ($\sigma < 1/2$), each term $(N/n)^z - N^z/n$ ($2 \le n \le N$) satisfies $|(N/n)^z - N^z/n| \le (N/2)^{\max(\sigma, 0)} + N^\sigma/2 \le N^{1/2}$, so $P_f \in H^\infty(\Omega_-)$ (with removable singularity cancelled at $z = 0$ of $\Phi(z) = -\frac{(1 - z - 1)\zeta(1 - z)}{(1 - z)^2}$, since $\Phi(0) = -1$). Moreover, $\Phi \in H^2(\Omega_-)$: on $\sigma = 1/2$, $|\Phi(1/2 + i\tau)|^2 = \frac{|\zeta(1/2 - i\tau)|^2}{1/4 + \tau^2} \in L^1(\mathbb{R})$ by the classical mean-value bound $\int_0^T |\zeta(1/2 + it)|^2\,dt \ll T\log T$ and integration by parts, while convexity $|\zeta(1 - \sigma - i\tau)| \ll (1 + |\tau|)^{1/4}$ ($\sigma < 1/2$) gives $\sup_{\sigma < 1/2}\int_{\mathbb{R}} |\Phi(\sigma + i\tau)|^2\,d\tau < \infty$ [4]. Hence $\Phi P_f \in H^2(\Omega_-)$.

Next, $\Gamma(1 - z)$ is zero-free and holomorphic on $\Omega_-$, while $\sin(\pi z/2)$ vanishes simply at $z = 2k$ ($k \in \mathbb{Z}$). At $z = 0$, the numerator factor $z$ in $\Theta_N(z) = \frac{z N^z}{(1 - z)^2 \chi(z)}$ cancels the simple zero of $\sin(\pi z/2)$ (giving $\Theta_N(0) = 2$), leaving simple poles in $\Omega_-$ exclusively at $z = -2m$ ($m \ge 1$). Since $\frac{d}{dz}\bigl|_{z=-2m}\chi(z) = 2^{-2m}\pi^{-2m-1}\cdot\frac{\pi}{2}(-1)^m\Gamma(2m + 1) = \frac{(-1)^m (2m)!}{2(2\pi)^{2m}}$, we obtain
$$
\rho_{m,N} = \frac{(-2m) N^{-2m}}{(2m + 1)^2 \cdot \frac{(-1)^m (2m)!}{2(2\pi)^{2m}}} = \frac{-4m(-1)^m}{(2m + 1)^2 (2m)!}\left(\frac{2\pi}{N}\right)^{2m},
$$
proving (2.8). Because $\sum_{m=1}^\infty |\rho_{m,N}| < \infty$, $R_N(z)$ converges uniformly away from $\{-2m\}_{m \ge 1}$ and belongs to $L^2(\operatorname{Re} z = \sigma)$ for every $\sigma \notin -2\mathbb{N}$: by Minkowski's integral inequality,
$$
\|R_N(\sigma + i\cdot)\|_{L^2(\frac{d\tau}{2\pi})} \le \sum_{m=1}^{\infty} |\rho_{m,N}|\left(\int_{-\infty}^{\infty}\frac{d\tau}{2\pi\bigl((2m + \sigma)^2 + \tau^2\bigr)}\right)^{1/2} = \sum_{m=1}^{\infty} \frac{|\rho_{m,N}|}{\sqrt{2(2m + \sigma)}} \qquad (\sigma > -2).
\tag{2.10}
$$
To prove uniformly across $\sigma < 1/2$ that $D_N := \Theta_N - R_N \in H^2(\Omega_-)$, write $z = \sigma + i\tau \in \Omega_-$, $x := \frac{1}{2} - \sigma > 0$, and $w := 1 - z = u - i\tau$ with $u := \frac{1}{2} + x > \frac{1}{2}$. First, $|N^z 2^{-z} \pi^{1-z}| = \sqrt{\frac{\pi N}{2}}\bigl(\frac{2\pi}{N}\bigr)^x$, and $|1 - z|^2 - |z|^2 = 1 - 2\sigma > 0$ gives $\frac{|z|}{|1 - z|^2} < \frac{1}{|1 - z|} = \frac{1}{\sqrt{u^2 + \tau^2}}$ on $\Omega_-$. Second, Binet's first log-gamma integral on $\operatorname{Re} w = u > \frac{1}{2}$ gives $\log\Gamma(w) = \bigl(w - \frac{1}{2}\bigr)\log w - w + \frac{1}{2}\log(2\pi) + J(w)$ with $J(w) = \int_0^\infty \bigl(\frac{1}{e^s - 1} - \frac{1}{s} + \frac{1}{2}\bigr)\frac{e^{-ws}}{s}\,ds$; since $\frac{1}{e^s - 1} - \frac{1}{s} + \frac{1}{2} = \sum_{k=1}^\infty \frac{2s}{s^2 + 4\pi^2 k^2} > 0$ for all $s > 0$, $|J(u - i\tau)| \le J(u) < J(1/2) = \frac{1 - \log 2}{2}$ uniformly for all $u > \frac{1}{2}, \tau \in \mathbb{R}$. Writing $-\arctan(|\tau|/u) = -\frac{\pi}{2} + \arctan(u/|\tau|)$ ($|\tau| > 0$), we obtain $\operatorname{Re}\log\Gamma(u - i\tau) = -\frac{\pi}{2}|\tau| + g_x(|\tau|) - \frac{1}{2} - x + \frac{1}{2}\log(2\pi) + \operatorname{Re} J(u - i\tau)$, where $g_x(t) := t\arctan(u/t) + x\log\sqrt{u^2 + t^2}$ ($t > 0$, $g_x(0) := x\log u$) satisfies $g_x'(t) = \arctan(u/t) - \frac{u t}{u^2 + t^2} + \frac{x t}{u^2 + t^2} > 0$ for all $t > 0$ (as $\arctan \xi > \frac{\xi}{1 + \xi^2}$ for $\xi > 0$). Thus $g_x(|\tau|) \ge g_x(0) = x\log u$ everywhere, giving $\frac{1}{|\Gamma(1 - z)|} \le \frac{e}{2\sqrt{\pi}} e^{\frac{\pi}{2}|\tau|} \bigl(\frac{e}{u}\bigr)^x$ and hence
$$
\frac{|z N^z 2^{-z}\pi^{1-z}|}{|1 - z|^2\,|\Gamma(1 - z)|} \le \frac{e\sqrt{N}}{2\sqrt{2}\sqrt{u^2 + \tau^2}}\,e^{\frac{\pi}{2}|\tau|}\left(\frac{2\pi e}{N(1/2 + x)}\right)^x \le \frac{e\sqrt{N}\,M_N}{2\sqrt{2}\sqrt{1/4 + \tau^2}}\,e^{\frac{\pi}{2}|\tau|} \qquad (\forall\, z \in \Omega_-),
$$
where $M_N := \sup_{x > 0}\bigl(\frac{2\pi e}{N(1/2 + x)}\bigr)^x < \infty$ since $\frac{2\pi e}{N(1/2 + x)} < 1$ for $x > \frac{2\pi e}{N}$. On $\{\sigma < 1/2,\, |\tau| \ge 1\}$, $|\sin(\pi z/2)| \ge \sinh(\pi|\tau|/2) \ge \frac{1 - e^{-\pi}}{2} e^{\frac{\pi}{2}|\tau|}$, while on every vertical segment $\sigma_k = -(2k + 1)$ ($k \ge 0$, $|\tau| \le 1$), $|\sin(\pi(\sigma_k + i\tau)/2)| = \cosh(\pi\tau/2) \ge \frac{1}{2} e^{\frac{\pi}{2}|\tau|}$; in both regimes $e^{\frac{\pi}{2}|\tau|}$ cancels identically, yielding $|\Theta_N(\sigma + i\tau)| \le \frac{C_N}{\sqrt{1/4 + \tau^2}}$ for all $\sigma < 1/2, |\tau| \ge 1$ ($C_N := \frac{e\sqrt{N}\,M_N}{\sqrt{2}(1 - e^{-\pi})}$) and $|\Theta_N(\sigma_k + i\tau)| \le e\sqrt{2N}\,M_N$ for all $k \ge 0, |\tau| \le 1$. Tiling $\{\sigma \le 1/2,\, |\tau| \le 1\}$ by the compact rectangles $\mathcal{R}_0 := [-1, 1/2] \times [-1, 1]$ and $\mathcal{R}_k := [-(2k + 1), -(2k - 1)] \times [-1, 1]$ ($k \ge 1$), every boundary point $z \in \bigcup_{k \ge 0}\partial\mathcal{R}_k$ satisfies $|z + 2m| \ge 1$ ($\forall\, m \ge 1$), so $|R_N(z)| \le S_N := \sum_{m=1}^\infty |\rho_{m,N}| < \infty$ on $\bigcup_{k \ge 0}\partial\mathcal{R}_k$, while $|\Theta_N(1/2 + i\tau)| = \frac{\sqrt{N}}{\sqrt{1/4 + \tau^2}} \le 2\sqrt{N}$. By the maximum modulus principle applied to the holomorphic difference $D_N = \Theta_N - R_N$ on each $\mathcal{R}_k$, $|D_N(z)| \le B_N := \max(C_N, e\sqrt{2N}\,M_N, 2\sqrt{N}) + S_N$ uniformly on $\{\sigma \le 1/2,\, |\tau| \le 1\}$. Combining this with $|R_N(\sigma + i\tau)| \le S_N / |\tau|$ on $|\tau| \ge 1$ gives $\sup_{\sigma < 1/2}\|D_N(\sigma + i\cdot)\|_{L^2(\frac{d\tau}{2\pi})}^2 \le \frac{B_N^2}{\pi} + \int_{|\tau| \ge 1}\bigl(\frac{C_N}{\sqrt{1/4+\tau^2}} + \frac{S_N}{|\tau|}\bigr)^2\frac{d\tau}{2\pi} < \infty$. Hence $\Theta_N - R_N \in H^2(\Omega_-)$, so $H_f \in H^2(\Omega_-)$ and $\|H_f(-1/2 + i\cdot)\|_{L^2(\frac{d\tau}{2\pi})} \le \|H_f(1/2 + i\cdot)\|_{L^2(\frac{d\tau}{2\pi})} \le \sqrt{N}\|f\|_{\mathcal{S}} + |a_1|\|R_N(1/2 + i\cdot)\|_{L^2(\frac{d\tau}{2\pi})}$ by Hardy-space boundary monotonicity and (2.7).

(2) On $z = -1/2 + i\tau$, we have $1 - z = 3/2 - i\tau = (1/2 - i\tau) + 1$, so $\Gamma(3/2 - i\tau) = (1/2 - i\tau)\Gamma(1/2 - i\tau)$ with $|\Gamma(1/2 - i\tau)| = \sqrt{\pi/\cosh(\pi\tau)}$, while $|\sin(-\pi/4 + i\pi\tau/2)| = \sqrt{\cosh(\pi\tau)/2}$. The hyperbolic cosine factors cancel identically:
$$
|\chi(-1/2 + i\tau)| = 2^{-1/2}\pi^{-3/2}\sqrt{\frac{\cosh(\pi\tau)}{2}}\cdot |1/2 - i\tau|\sqrt{\frac{\pi}{\cosh(\pi\tau)}} = \frac{\sqrt{1/4 + \tau^2}}{2\pi}.
$$
Since $|z|^2 = |z + 1|^2 = 1/4 + \tau^2$ and $|1 - z|^2 = 9/4 + \tau^2 = (1/4 + \tau^2) + 2$,
$$
|M_B(-1/2 + i\tau)| = \frac{|\chi(-1/2 + i\tau)|\,|1 - z|^2}{|z|^2\,|z + 1|} = \frac{\frac{\sqrt{1/4 + \tau^2}}{2\pi}(1/4 + \tau^2 + 2)}{(1/4 + \tau^2)^{3/2}} = \frac{1}{2\pi}\left(1 + \frac{2}{1/4 + \tau^2}\right) \le \frac{9}{2\pi},
$$
attained at $\tau = 0$. Finally, $\int_{-\infty}^{\infty} \frac{d\tau}{2\pi |(-1/2 + i\tau)(1/2 + i\tau)|^2} = \frac{1}{2\pi}\int_{-\infty}^{\infty} \frac{d\tau}{(1/4 + \tau^2)^2} = \frac{4\pi}{2\pi} = 2$, completing (2.9). $\square$

---

### 2.3. Three-Point Bertrand Prime Functional, Integration by Parts, and Tent Smoothing

To make Lemma 2.2 unconditional without computing $d_N(\mathcal{S})$ numerically for large $N$, we exhibit a 3-point linear functional annihilating $\mathcal{V}_N$.

**Lemma 2.3 (Exact 3-point prime functional for $a_1$).** *For every integer $N \ge 2$, every prime $p > N$, and every $f = a_1 E + \sum_{n=2}^N a_n G_n \in \widetilde{\mathcal{V}}_N$,*
$$
a_1 = f(1) + f(p - 1) - f(p), \qquad |a_1| \le \sqrt{2 p^2 + 2}\,\|f\|_{\mathcal{S}}.
\tag{2.11}
$$
*In particular, taking $p = p_+(N)$ (the least prime $> N$), Chebyshev–Bertrand ($p_+(N) \le 2N - 1$) yields $|a_1| < 2\sqrt{2}\,N\,\|f\|_{\mathcal{S}}$ for all $N \ge 2$, while Nagura's theorem [12] ($p_+(N) < \frac{6}{5}N$ for $N \ge 25$) yields $|a_1| < \sqrt{\frac{72}{25}N^2 + 2}\,\|f\|_{\mathcal{S}}$ for all $N \ge 25$.*

*Proof.* For $E$, $E(1) + E(p - 1) - E(p) = 1 + 1 - 1 = 1$. For any $2 \le n \le N < p$, primality of $p$ implies $n \nmid p$, so $p \bmod n \in \{1, \dots, n - 1\}$ and hence $(p - 1) \bmod n = (p \bmod n) - 1$, while $1 \bmod n = 1$. Thus
$$
G_n(1) + G_n(p - 1) - G_n(p) = -\frac{1}{n} - \frac{(p \bmod n) - 1}{n} + \frac{p \bmod n}{n} = 0.
$$
Linearity gives $f(1) + f(p - 1) - f(p) = a_1$, and Cauchy–Schwarz against $w_m = \frac{1}{m(m+1)}$ gives $|a_1|^2 \le \bigl(w_1^{-1} + w_{p-1}^{-1} + w_p^{-1}\bigr)\|f\|_{\mathcal{S}}^2 = \bigl(2 + (p - 1)p + p(p + 1)\bigr)\|f\|_{\mathcal{S}}^2 = (2p^2 + 2)\|f\|_{\mathcal{S}}^2$. For $p \le 2N - 1$, $2(2N - 1)^2 + 2 = 8N^2 - 8N + 4 < 8N^2$ for all $N \ge 1$. $\square$

**Proposition 2.4 (Explicit $L^2(t^{-2}dt)$ primitive constant $\kappa_B(N)$ and contraction bound (1.11)).** *Let $N, Q \ge 2$ and let $A_1(N)$ denote any upper bound for $\sup_{\|f\|_{\mathcal{S}}=1}|a_1(f)|$ (specifically $A_1(N) = 1/d_N(\mathcal{S})$, or computer-free $A_1(N) = \sqrt{2 p_+(N)^2 + 2} < 2\sqrt{2}\,N$). Then every $f \in \widetilde{\mathcal{V}}_N$ satisfies $\|B_f\|_{L^2([1,\infty), t^{-2}dt)} \le \kappa_B(N)\,N\,\|f\|_{\mathcal{S}}$, where we may take either*
$$
\kappa_B^{\mathrm{ML}}(N) := \frac{9}{2\pi}\left(1 + \frac{A_1(N)}{\sqrt{N}}\bigl(\|R_N\|_{\sigma=1/2} + \|R_N\|_{\sigma=-1/2}\bigr)\right) + \sqrt{2}\,\frac{\alpha_{\mathrm{DC}}(N)}{\sqrt{N}},
\tag{2.12}
$$
*or, whenever $d_N(\mathcal{S})$ is bounded below, $\kappa_B^{\mathrm{tr}}(N) := \frac{1}{d_N(\mathcal{S})}\bigl(\frac{9}{2\pi} + \frac{\sqrt{2}}{2\sqrt{N}}\bigr)$, and $\sqrt{\eta(N, Q)}$ satisfies (1.11).*

*Proof.* Evaluating (2.5) via Lemma 2.2 on $\operatorname{Re} z = -1/2$ (where $|N^{-z}| = N^{1/2}$) and the triangle inequality yields $\|B_f\|_{L^2(t^{-2}dt)} \le \kappa_B^{\mathrm{ML}}(N) N \|f\|_{\mathcal{S}}$. Alternatively, write $f = a_1 E + g$ ($g \in \mathcal{V}_N$): since $E^{\mathrm{osc}} \equiv 0$, we have $B_f \equiv B_g$. Writing $u_0 := g + a_1 P_{\mathcal{V}_N} E \in \mathcal{V}_N$, orthogonality $f = a_1 r_N + u_0$ gives $\|f\|_{\mathcal{S}}^2 = |a_1|^2 d_N^2(\mathcal{S}) + \|u_0\|_{\mathcal{S}}^2$, whence Cauchy–Schwarz on $\|g\|_{\mathcal{S}} \le \|u_0\|_{\mathcal{S}} + |a_1| d_N(\mathcal{S}) \frac{\sqrt{1 - d_N^2(\mathcal{S})}}{d_N(\mathcal{S})}$ yields $\|g\|_{\mathcal{S}} \le \|f\|_{\mathcal{S}}\sqrt{1 + \frac{1 - d_N^2(\mathcal{S})}{d_N^2(\mathcal{S})}} = \frac{\|f\|_{\mathcal{S}}}{d_N(\mathcal{S})}$. Applying (2.12) to $g \in \mathcal{V}_N$ (where $a_1(g) = 0$ and $\alpha_{\mathrm{DC}}^{\mathcal{V}_N}(N) < \frac{1}{2}$ by Theorem 3(1), proved independently in §4.1 below) gives $\kappa_B^{\mathrm{tr}}(N)$. Note also the purely analytical upper bound $\alpha_{\mathrm{DC}}(N) \le \frac{1}{2} + \frac{A_1(N)}{2\sqrt{N}}\bigl(\|R_N\|_{\sigma=1/2} + |R_N(0)|\bigr)$ from §4.3.

Now decompose $V_Q^* f$ using $f = A_0(f) E + f^{\mathrm{osc}}$ and $V_Q^* E = Q^{-1/2} E$:
$$
V_Q^* f = Q^{-1/2} A_0(f)\,E + V_Q^* f^{\mathrm{osc}}, \qquad \|Q^{-1/2} A_0(f)\,E\|_{\mathcal{S}} \le \alpha_{\mathrm{DC}}(N)\sqrt{\frac{N}{Q}}\,\|f\|_{\mathcal{S}}.
\tag{2.13}
$$
For each $k \ge 1$, integrating $(V_Q^* f^{\mathrm{osc}})(k) = Q^{1/2} k(k + 1)\int_{kQ}^{(k+1)Q} f^{\mathrm{osc}}(\lfloor t\rfloor) t^{-2}\,dt$ by parts with $dB_f(t) = f^{\mathrm{osc}}(\lfloor t\rfloor)\,dt$ splits $V_Q^* f^{\mathrm{osc}} = X + Y$, where
$$
X(k) := Q^{-3/2}\left(\frac{k}{k + 1} B_f\bigl((k + 1)Q\bigr) - \frac{k + 1}{k} B_f(kQ)\right), \qquad
Y(k) := 2 Q^{1/2} k(k + 1)\int_{kQ}^{(k+1)Q} B_f(t)\,t^{-3}\,dt.
\tag{2.14}
$$
For $Y(k)$, Cauchy–Schwarz gives $\bigl|\int_{kQ}^{(k+1)Q} B_f(t) t^{-3}\,dt\bigr|^2 \le \bigl(\int_{kQ}^{(k+1)Q} |B_f(t)|^2 t^{-2}\,dt\bigr)\bigl(\int_{kQ}^{(k+1)Q} t^{-4}\,dt\bigr)$, where $\int_{kQ}^{(k+1)Q} t^{-4}\,dt = \frac{3k^2 + 3k + 1}{3 Q^3 k^3(k + 1)^3}$. Multiplying by $w_k \cdot 4 Q k^2(k + 1)^2 = 4 Q k(k + 1)$ gives factor $\frac{4(3k^2 + 3k + 1)}{3 Q^2 k^2(k + 1)^2} \le \frac{7}{3 Q^2}$ (maximized at $k = 1$), so summing over $k \ge 1$ yields
$$
\|Y\|_{\mathcal{S}} \le \sqrt{\frac{7}{3}}\,\frac{\|B_f\|_{L^2([1,\infty), t^{-2}dt)}}{Q} \le \sqrt{\frac{7}{3}}\,\kappa_B(N)\,\frac{N}{Q}\,\|f\|_{\mathcal{S}}.
\tag{2.15}
$$
For $X(k)$, apply Young's inequality $|u_k - v_k|^2 \le (1 + \theta_k)|u_k|^2 + (1 + \theta_k^{-1})|v_k|^2$ with $\theta_k := \frac{k + 1}{k}$ to $u_k = \frac{k}{k+1} B_f((k+1)Q)$ and $v_k = \frac{k+1}{k} B_f(kQ)$. Collecting the knot coefficients $c_j$ of $Q^{-3}|B_f(jQ)|^2$ in $\sum_{k=1}^\infty w_k |X(k)|^2$ gives exact algebraic cancellation:
$$
c_1 = \left(1 + \frac{1}{2}\right)\cdot 2 = 3, \qquad
c_j = \left(1 + \frac{j}{j - 1}\right)\frac{j - 1}{j^3} + \left(1 + \frac{j}{j + 1}\right)\frac{j + 1}{j^3} = \frac{(2j - 1) + (2j + 1)}{j^3} = \frac{4}{j^2} \quad (j \ge 2).
\tag{2.16}
$$
Fix $\delta := \frac{1}{5}$, so the intervals $I_{j,\delta} := [(j - \delta)Q, (j + \delta)Q]$ ($j \ge 1$) are pairwise disjoint inside $[(4/5)Q, \infty) \subset [1, \infty)$ ($Q \ge 2$). Applying the fundamental theorem of calculus to $\Lambda_{j,\delta}(t)|B_f(t)|^2$ with unit tent $\Lambda_{j,\delta}(t) := \max\bigl(0, 1 - \frac{|t - jQ|}{\delta Q}\bigr)$ on $[(j-\delta)Q, jQ]$ and $[jQ, (j+\delta)Q]$ gives
$$
|B_f(jQ)|^2 \le \frac{1}{2\delta Q}\int_{I_{j,\delta}} |B_f(t)|^2\,dt + \int_{I_{j,\delta}} |B_f(t)|\,|f^{\mathrm{osc}}(\lfloor t\rfloor)|\,dt.
$$
Since $1 \le \frac{(j + \delta)^2 Q^2}{t^2}$ on $I_{j,\delta}$ and $M_\delta := \sup_{j \ge 1} c_j(j + \delta)^2 = \max\bigl(3(6/5)^2,\, 4(11/10)^2\bigr) = \frac{121}{25}$, summing $c_j Q^{-3}|B_f(jQ)|^2$ over $j \ge 1$ and applying Cauchy–Schwarz across the disjoint intervals $I_{j,\delta}$ yields
$$
\|X\|_{\mathcal{S}}^2 \le \frac{121}{10 Q^2}\,\|B_f\|_{L^2(t^{-2}dt)}^2 + \frac{121}{25 Q}\,\|B_f\|_{L^2(t^{-2}dt)}\,\|f^{\mathrm{osc}}\|_{L^2([(4/5)Q,\infty), t^{-2}dt)}.
\tag{2.17}
$$
Finally, $\|f^{\mathrm{osc}}\|_{L^2([(4/5)Q,\infty), t^{-2}dt)} \le \|f\|_{\mathcal{S}} + |A_0(f)|\bigl(\int_{(4/5)Q}^\infty t^{-2}\,dt\bigr)^{1/2} \le \bigl(1 + \alpha_{\mathrm{DC}}(N)\sqrt{\frac{5N}{4Q}}\bigr)\|f\|_{\mathcal{S}}$. Combining (2.13), (2.15), and (2.17) proves (1.11). $\square$

---

### 2.4. Completion of Theorem 1: Pointwise Sawtooth Bound, $Q \ge 32 N$, and Large-$Q$ Asymptotics

For small $N$ (and to prove (1.14) with $O_N(Q^{-1})$ error), we complement (1.11) with an exact pointwise sawtooth primitive bound on each generator $G_n^{\mathrm{osc}}$.

**Lemma 2.5 (Pointwise sawtooth primitive bound).** *For every integer $n \ge 2$, $\mathring{B}_{G_n}(t) := \int_0^t G_n^{\mathrm{osc}}(\lfloor u\rfloor)\,du$ satisfies $0 \le \mathring{B}_{G_n}(t) \le \frac{n}{8}$ for all $t \ge 0$, and for every $Q \ge 2$,*
$$
\|V_Q^* G_n^{\mathrm{osc}}\|_{\mathcal{S}} \le \frac{\sqrt{\zeta(2) + \zeta(3)}}{8}\,\frac{n}{Q^{3/2}} < 0.21092\,\frac{n}{Q^{3/2}}.
\tag{2.18}
$$

*Proof.* On $[0, n]$, $\mathring{B}_{G_n}$ is piecewise linear with integer knots $\mathring{B}_{G_n}(r) = \sum_{m=0}^{r-1}\frac{n - 1 - 2m}{2n} = \frac{r(n - r)}{2n} \in \bigl[0, \frac{n}{8}\bigr]$ ($0 \le r \le n$), and extends $n$-periodically to $[0, \infty)$, so $0 \le \mathring{B}_{G_n}(t) \le \frac{n}{8}$ everywhere. Integrating $I_k := \int_{kQ}^{(k+1)Q} G_n^{\mathrm{osc}}(\lfloor t\rfloor) t^{-2}\,dt$ by parts gives $I_k = \frac{\mathring{B}_{G_n}((k+1)Q)}{(k+1)^2 Q^2} - \frac{\mathring{B}_{G_n}(kQ)}{k^2 Q^2} + 2\int_{kQ}^{(k+1)Q} \mathring{B}_{G_n}(t) t^{-3}\,dt$. Using $0 \le \mathring{B}_{G_n} \le \frac{n}{8}$ in the positive and negative parts separately gives
$$
-\frac{n}{8 k^2 Q^2} \le I_k \le \frac{n}{8}\left(\frac{1}{(k + 1)^2 Q^2} + 2\int_{kQ}^{(k+1)Q} t^{-3}\,dt\right) = \frac{n}{8 k^2 Q^2}.
$$
Hence $|(V_Q^* G_n^{\mathrm{osc}})(k)| = Q^{1/2} k(k + 1)|I_k| \le \frac{n(k + 1)}{8 k Q^{3/2}}$, and summing $w_k \frac{n^2(k+1)^2}{64 k^2 Q^3} = \frac{n^2}{64 Q^3}\bigl(\frac{1}{k^2} + \frac{1}{k^3}\bigr)$ over $k \ge 1$ proves (2.18). $\square$

*Proof of Theorem 1(2)–(4).*
- **Part (2), computer-free bounds:** In (2.10) and (2.12), $\|R_N\|_{\sigma=\pm 1/2}$ and $|R_N(0)|$ are strictly decreasing functions of $N \ge 5$ (since $|\rho_{m,N}| \propto (2\pi/N)^{2m}$). With $A_1(N) = 2\sqrt{2}\,N$ (Lemma 2.3), $\frac{A_1(N)}{\sqrt{N}}\|R_N\| \propto N^{1/2}(2\pi/N)^{2m}$ is strictly decreasing for all $N \ge 7$, so the right-hand side of (1.11) at $u = 1/32$ decreases strictly for $N \ge 75$, evaluating at $N = 75$ to $\eta(75, 32 \cdot 75) \le 0.499308 < \frac{1}{2}$. With Nagura's bound $A_1(N) = \sqrt{\frac{72}{25}N^2 + 2}$ ($N \ge 25$) [12], monotonicity holds for $N \ge 25$ and gives $\eta(59, 32 \cdot 59) \le 0.499348 < \frac{1}{2}$ for all $N \ge 59$. For $Q \ge 116 N$ ($u \le 1/116$), using $A_1(N) = \sqrt{2 p_+(N)^2 + 2}$ on $5 \le N \le 74$ gives $\max_{5 \le N \le 74}\eta(N, 116 N) \le 0.454371 < \frac{1}{2}$, while for $N \in \{2, 3, 4\}$ we have $116 N \ge 29 N^2$, where $\eta(N, Q) < \frac{1}{2}$ was already proved computer-free in [11, Theorem 3(2)].
- **Part (2), uniform $Q \ge 32 N$ across $2 \le N \le 74$:** For $2 \le N \le 74$, our dual-backend interval script `supplement/certify_dual_backend.py` computes outward-rounded enclosures of the $73 \times 73$ Vasyunin Gram Cholesky factor $L$ of $\mathcal{V}_{74}$ [16] independently in 512-bit `flint.arb` and 80-digit `mpmath.iv` (with Euler's constant $\gamma$ certified purely inside `mpmath.iv` via exact rational Bernoulli Euler–Maclaurin summation and outward remainder bounds). For $33 \le N \le 74$, inserting the certified enclosures of $d_N(\mathcal{S})$ and $\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)$ into (1.11) certifies $\eta(N, Q) \le 0.49150836 < \frac{1}{2}$ (peaking at $N = 33$, strictly outward ceiling-rounded). For $2 \le N \le 32$, bounding $|a_n(f)| \le \sqrt{(G_{\widetilde{\mathcal{V}}_N}^{-1})_{n,n}}\,\|f\|_{\mathcal{S}}$ via Lemma 2.5 gives $\sqrt{\eta(N, Q)} \le \sqrt{\frac{\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)}{Q}} + \frac{\sqrt{\zeta(2) + \zeta(3)}}{8 Q^{3/2}}\sum_{n=2}^N n\sqrt{(G_{\widetilde{\mathcal{V}}_N}^{-1})_{n,n}}$, certifying $\max_{2 \le N \le 32}\sup_{Q \ge 32N}\eta(N, Q) \le 0.02239517 < \frac{1}{2}$. Combining $2 \le N \le 74$ with $N \ge 75$ proves $\eta(N, Q) < \frac{1}{2}$ for **all** $N \ge 2$ and $Q \ge 32 N$. Since $\|P_{\mathcal{W}_Q^{\mathcal{S}}}(E - g)\|_{\mathcal{S}}^2 = \|E - g\|_{\mathcal{S}}^2 - \|V_Q^*(E - g)\|_{\mathcal{S}}^2 \ge (1 - \eta(N, Q))\|E - g\|_{\mathcal{S}}^2$ for all $g \in \mathcal{V}_N$, minimizing over $g \in \mathcal{V}_N$ yields (1.12).
- **Part (3):** Taking $Q(N) = 32 N$ (or $Q(N) = q^{J_{\mathrm{RH}}(N)} \ge 32 N$ via $\mathcal{H}_{J,q} = \mathcal{W}_{q^J}^{\mathcal{S}}$ [11, Theorem 1(1)]), (1.12) shows $\lim_{N\to\infty} d_N(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = 0 \iff \lim_{N\to\infty} d_N(\mathcal{S}) = 0 \iff \text{RH}$. Whenever $Q(N)/N \to \infty$, $u = N/Q(N) \to 0$ in (1.11) gives $\eta(N, Q(N)) = O(N/Q(N)) \to 0$, so $d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = (1 + o(1))d_N^2(\mathcal{S})$ and Burnol's lower bound (1.4) transfers identically to (1.13).
- **Part (4):** For fixed $N \ge 2$, equivalence of norms on $\widetilde{\mathcal{V}}_N$ and Lemma 2.5 give $\|V_Q^* f^{\mathrm{osc}}\|_{\mathcal{S}} \le C_N Q^{-3/2}\|f\|_{\mathcal{S}}$. Expanding $\|V_Q^* f\|_{\mathcal{S}}^2 = \|Q^{-1/2} A_0(f) E + V_Q^* f^{\mathrm{osc}}\|_{\mathcal{S}}^2 = \frac{|A_0(f)|^2}{Q} + 2\operatorname{Re}\langle Q^{-1/2} A_0(f) E, V_Q^* f^{\mathrm{osc}}\rangle_{\mathcal{S}} + \|V_Q^* f^{\mathrm{osc}}\|_{\mathcal{S}}^2$, Cauchy–Schwarz bounds the cross term by $O_N(Q^{-1/2} \cdot Q^{-3/2})\|f\|_{\mathcal{S}}^2 = O_N(Q^{-2})\|f\|_{\mathcal{S}}^2$, proving both asymptotics in (1.14). $\square$

---

## 3. Proof of Theorem 2: Critical Horizon $Q = N + 1$ Möbius Duality and Sub-Horizon Correlation Sieve

### 3.1. Exact Prefix Möbius Dual at $Q = N + 1$ and the $15/\pi^2$ Asymptotic

*Proof of Theorem 2(1).* Every vector in $V_Q(\mathcal{S})$ vanishes on $\{1, \dots, Q - 1\}$, so the finite prefix space $\mathcal{S}_{< Q} = \{h \in \mathcal{S} : h(m) = 0 \;\forall\, m \ge Q\}$ is a closed subspace of $\mathcal{W}_Q^{\mathcal{S}}$ (corresponding to the $k = 0$ block of (1.10)), whence $d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \ge d_N^2(\mathcal{S}_{< Q})$. Restricting the discrete Dirichlet dual variational formula of [11, Theorem 2(1)] to the single block $k = 0$ at $Q = N + 1$ gives
$$
d_N^2(\mathcal{S}_{< N+1}) = \sup_{0 \ne F \in \mathcal{A}_{N, N+1}} \frac{|F(1)|^2}{\sum_{d=0}^{N} |F(d + 1) - F(d)|^2},
\tag{3.1}
$$
where $\mathcal{A}_{N, N+1}$ consists of all $F : \{0, 1, \dots, N + 1\} \to \mathbb{C}$ with $F(0) = F(N + 1) = 0$ satisfying
$$
\sum_{u=1}^{N} \frac{F(u)}{u}\left(\mathbf{1}_{n \mid u} - \frac{1}{n}\right) = 0 \quad \Longleftrightarrow \quad \sum_{j=1}^{\lfloor N/n\rfloor} \frac{F(jn)}{j} = \sum_{u=1}^{N} \frac{F(u)}{u} \qquad (\forall\, 2 \le n \le N).
\tag{3.2}
$$
Set $C := \sum_{u=1}^N \frac{F(u)}{u}$; then $\sum_{j=1}^{\lfloor N/n\rfloor} \frac{F(jn)}{j} = C$ holds for **all** $1 \le n \le N$ (tautologically at $n = 1$). Applying truncated Möbius inversion to $n = kd$ for any $1 \le d \le N$ yields
$$
\sum_{k=1}^{\lfloor N/d\rfloor} \frac{\mu(k)}{k} \sum_{j=1}^{\lfloor N/(kd)\rfloor} \frac{F(jkd)}{j} = \sum_{r=1}^{\lfloor N/d\rfloor} \frac{F(rd)}{r}\sum_{k \mid r} \mu(k) = F(d),
$$
so every $F \in \mathcal{A}_{N, N+1}$ satisfies $F(d) = C\,\sum_{k=1}^{\lfloor N/d\rfloor} \frac{\mu(k)}{k} = C\,m(\lfloor N/d\rfloor)$ ($1 \le d \le N$). Conversely, for $F(d) := m(\lfloor N/d\rfloor)$ and every $1 \le n \le N$ (noting $\lfloor N/n\rfloor \ge 1$),
$$
\sum_{j=1}^{\lfloor N/n\rfloor} \frac{F(jn)}{j} = \sum_{j=1}^{\lfloor N/n\rfloor} \frac{1}{j}\sum_{k=1}^{\lfloor N/(jn)\rfloor}\frac{\mu(k)}{k} = \sum_{r=1}^{\lfloor N/n\rfloor} \frac{1}{r}\sum_{k \mid r}\mu(k) = 1.
$$
Thus $\dim \mathcal{A}_{N, N+1} = 1$, spanned by $F(d) = m(\lfloor N/d\rfloor)$ ($F(0) = F(N + 1) = m(0) = 0$), and substituting this unique generator into (3.1) yields (1.15).

To prove (1.16) unconditionally, recall from the prime number theorem [13] that $m(x) = O((\log x)^{-2})$ for $x \ge 2$, so $m(N)^2 = O((\log N)^{-4})$. Split the sum in $D(N)$ at $D_1 := \lfloor \log N\rfloor$ and $D_2 := \lceil \sqrt{N}\rceil$ ($N \ge 16$):
1. **Isolated hyperbola jumps ($D_2 \le d \le N$):** Since $d \ge \lceil \sqrt{N}\rceil$ implies $d(d + 1) > N$, each interval $J_d := \bigl(\frac{N}{d + 1}, \frac{N}{d}\bigr]$ has length $\frac{N}{d(d + 1)} < 1$ and therefore contains **at most one integer** $k \ge 1$. Moreover, $k \in J_d \iff \frac{N}{k} - 1 < d \le \frac{N}{k} \iff d = \lfloor N/k\rfloor$. As $k$ runs over $1 \le k \le K_N := \lfloor N/D_2\rfloor \asymp \sqrt{N}$, the indices $d = \lfloor N/k\rfloor \in [D_2, N]$ are distinct and exhaust all nonempty $J_d$ on $[D_2, N]$, giving
   $$
   \sum_{d = D_2}^{N} \Bigl(m\bigl(\lfloor N/d\rfloor\bigr) - m\bigl(\lfloor N/(d + 1)\rfloor\bigr)\Bigr)^2 = \sum_{k=1}^{K_N} \frac{\mu(k)^2}{k^2} = \sum_{k=1}^{\infty} \frac{\mu(k)^2}{k^2} + O(N^{-1/2}) = \frac{\zeta(2)}{\zeta(4)} + O(N^{-1/2}) = \frac{15}{\pi^2} + O(N^{-1/2}).
   $$
2. **Intermediate transition ($D_1 < d < D_2$):** Each $J_d$ contains at most $\frac{N}{d(d + 1)} + 1$ integers, every one of which exceeds $\frac{N}{d + 1}$, so $\bigl|m(\lfloor N/d\rfloor) - m(\lfloor N/(d + 1)\rfloor)\bigr| \le \bigl(\frac{N}{d(d + 1)} + 1\bigr)\frac{d + 1}{N} = \frac{1}{d} + \frac{d + 1}{N}$. Squaring and summing over $D_1 < d < D_2$ gives
   $$
   \sum_{d = D_1 + 1}^{D_2 - 1} \left(\frac{1}{d} + \frac{d + 1}{N}\right)^2 \le 2\sum_{d > \lfloor\log N\rfloor} \frac{1}{d^2} + \frac{2}{N^2}\sum_{d < \lceil\sqrt{N}\rceil} (d + 1)^2 = O\!\left(\frac{1}{\log N}\right) + O(N^{-1/2}).
   $$
3. **Large arguments ($1 \le d \le D_1$):** Here $\lfloor N/(d + 1)\rfloor \gg N/\log N$, so $m(\lfloor N/d\rfloor) - m(\lfloor N/(d + 1)\rfloor) = O((\log N)^{-2})$, and summing $O((\log N)^{-4})$ over $\lfloor \log N\rfloor$ terms contributes $O((\log N)^{-3})$.

Summing the three ranges establishes $D(N) = \frac{15}{\pi^2} + O\bigl(\frac{1}{\log N}\bigr)$. $\square$

---

### 3.2. Discrete Brownian-Bridge Lagrange Identity and Short-Interval Correlation Bound

*Proof of Theorem 2(2).* For any vector $(\phi_1, \dots, \phi_{Q-1}) \in \mathbb{C}^{Q-1}$, define partial sums $z_a := \sum_{u=1}^a \phi_u$ ($0 \le a \le Q - 1$, $z_0 := 0$). Applying Lagrange's identity $\frac{1}{Q}\sum_{0 \le a < b \le Q-1} |z_b - z_a|^2 = \sum_{a=0}^{Q-1} |z_a|^2 - \frac{1}{Q}\bigl|\sum_{a=0}^{Q-1} z_a\bigr|^2$ and substituting $\sum_{a=0}^{Q-1}|z_a|^2 = \sum_{u,v=1}^{Q-1}\bigl(Q - \max(u, v)\bigr)\phi_u\overline{\phi_v}$ and $\sum_{a=0}^{Q-1} z_a = \sum_{u=1}^{Q-1}(Q - u)\phi_u$ gives
$$
\frac{1}{Q}\sum_{0 \le a < b \le Q-1} \left|\sum_{u=a+1}^{b} \phi_u\right|^2 = \sum_{u,v=1}^{Q-1}\left(Q - \max(u, v) - \frac{(Q - u)(Q - v)}{Q}\right)\phi_u\overline{\phi_v} = \sum_{u,v=1}^{Q-1}\left(\min(u, v) - \frac{uv}{Q}\right)\phi_u\overline{\phi_v},
$$
since $u + v - \max(u, v) = \min(u, v)$. Applying this identity on every block $k \ge 0$ of (1.10) with $\phi_u = \frac{\psi(kQ + u)}{kQ + u}$ (where $kQ + u \in \mathbb{N}_Q$, so $\psi(kQ + u) = \nabla(E - g)(kQ + u)$) yields the equality in (1.17). Each sub-block interval $\{kQ + a + 1, \dots, kQ + b\}$ has length $h := b - a \in \{1, \dots, Q - 1\}$ and starting offset $n := kQ + a \ge 0$; for each fixed $h$, distinct pairs $(k, a)$ ($k \ge 0, 0 \le a \le Q - 1 - h$) produce distinct integers $n \ge 0$. Enlarging the sum over $n$ to all integers $n \ge 1 - h$ (setting $\psi(m) := 0$ for $m \le 0$) adds only nonnegative squares, proving the inequality in (1.17).

Expanding $\left|\sum_{m=n+1}^{n+h} x_m\right|^2 = \sum_m |x_m|^2 + 2\operatorname{Re}\sum_{m < m'} x_m\overline{x_{m'}}$ with $x_m := \psi(m)/m$:
- Each diagonal term $|x_m|^2$ ($m \ge 1$) lies in $\{n + 1, \dots, n + h\}$ for the $h$ integers $m - h \le n \le m - 1$ ($\ge 1 - h$), giving weight $\frac{1}{Q}\sum_{h=1}^{Q-1} h = \frac{Q - 1}{2}$.
- Each shifted pair $\{m, m + \ell\}$ ($m \ge 1$, $1 \le \ell \le Q - 2$) lies in $\{n + 1, \dots, n + h\}$ whenever $\ell + 1 \le h \le Q - 1$ and $m + \ell - h \le n \le m - 1$ ($h - \ell$ integers), giving weight $\frac{2}{Q}\sum_{h=\ell+1}^{Q-1}(h - \ell) = \frac{(Q - 1 - \ell)(Q - \ell)}{Q}$, which proves (1.18).

When $2 \le Q \le N$, sub-horizon pole unlocking [11, Theorem 1(3)] ensures that both the global Walsh–Selberg squarefree sieve witness $\psi_N^{\mathrm{WS}}$ of [11, Lemma 3.2 & Theorem 2(3)] and the truncated Möbius witness $\psi_N^{\mu}(m) = \mathbf{1}_{m=1} - \sum_{d \le N,\, d \mid m}\mu(d)$ are realized on $\mathbb{N}_Q$ by elements $g \in \mathcal{V}_N$ (for $\psi_N^{\mu}$, if $Q \nmid m$ then no divisor $d \mid m$ is a multiple of $Q$, so $P_{\mathcal{W}_Q} g_N^{\mu, Q} := \sum_{1 \le d \le N,\, Q \nmid d}\mu(d) H_d^{(Q)} \in P_{\mathcal{W}_Q}(\mathcal{V}_N)$ satisfies $\nabla(E - g_N^{\mu,Q})(m) = \psi_N^{\mu}(m)$ for all $m \in \mathbb{N}_Q$). For $\widetilde{\psi}_{N,Q}^{\mathrm{WS}}(m) = \mathbf{1}_{Q \nmid m}\psi_N^{\mathrm{WS}}(m)$, [11, Theorem 2(3)] gives $\sum_{m=1}^\infty \frac{|\widetilde{\psi}_{N,Q}^{\mathrm{WS}}(m)|^2}{m^2} \le \frac{6}{\pi^2}\sum_{\ell > N}\frac{\mu(\ell)^2}{J_2(\ell)} < \frac{6}{\pi^2 N}$, bounding the diagonal of (1.18) by $\frac{3(Q - 1)}{\pi^2 N}$. Finally, for $\psi_N^{\mu}(m)$ ($m > N$), periodicity modulo $R_N := \prod_{p \le N} p$ yields $|\psi_N^{\mu}(m)| \le 3$ for $N = 16$ and $\le 2$ for $N = 8$; summing up to $M = 10^4$ (for $(16, 3)$) and $M = 10^3$ (for $(8, 8)$) in exact rational arithmetic in `supplement/verify_symbolic_and_rational.py` and bounding the infinite tail via $\sum_{m > M} \frac{1}{m(m+\ell)} \le \frac{1}{M + 1}$ certifies the strict positive value $> +6.1249 \times 10^{-4}$ at $(16, 3)$ and strict negative value $< -0.107800$ at $(8, 8)$ (contrasting with the asymptotic Chowla paradigm [14, 15]). $\square$

---

## 4. Proof of Theorem 3: Homogeneous Szegő–Blaschke DC Duality and Trivial-Zero Pole Envelope

### 4.1. Strict Finite-$N$ Continuous-Blaschke Upper Bound on $\mathcal{V}_N$

*Proof of Theorem 3(1).* For any $v = \sum_{n=2}^N a_n G_n \in \mathcal{V}_N$ ($a_1(v) = 0$), Lemma 2.2(1) and (2.7) show that $F_v(z) = \Phi(z) P_v(z)$ belongs to $H^2(\Omega_-)$ with $\|F_v\|_{H^2(\Omega_-)}^2 = N\,\|v\|_{\mathcal{S}}^2$. At $z = 0$, $\Phi(0) = \lim_{z \to 0}\frac{z\zeta(1 - z)}{(1 - z)^2} = -1$ and $P_v(0) = \sum_{n=2}^N a_n(1 - n^{-1}) = -2 A_0(v)$, so $F_v(0) = 2 A_0(v)$ and hence
$$
\frac{4\,|A_0(v)|^2}{N\,\|v\|_{\mathcal{S}}^2} = \frac{|F_v(0)|^2}{\|F_v\|_{H^2(\Omega_-)}^2} \qquad (0 \ne v \in \mathcal{V}_N).
\tag{4.1}
$$
Under $w = 1 - z$ ($\Omega_- \leftrightarrow \Omega_+ := \{\operatorname{Re} w > 1/2\}$), $\Phi(z) = -\frac{(w - 1)\zeta(w)}{w^2}$. By Balazard, Saias, and Yor [4, Lemma 1 & Theorem 1] and Burnol [17, Theorem 1.2], $\Phi \in H^2(\Omega_-)$ has canonical inner–outer factorization $\Phi = B_- \mathcal{O}_\Phi$ with trivial singular inner factor and Blaschke factor
$$
B_-(z) := \prod_{\operatorname{Re}\rho > 1/2} \alpha_\rho\,\frac{z - (1 - \rho)}{z - \overline{\rho}} \qquad (|\alpha_\rho| = 1), \qquad
|B_-(0)|^2 = \prod_{\operatorname{Re}\rho > 1/2}\left|\frac{1 - \rho}{\rho}\right|^2 = P_{\mathrm{NB}} = 1 - \mathcal{D}_{\mathrm{NB}}^2,
\tag{4.2}
$$
where $|1/2 + i\tau - (1 - \rho)| = |(\operatorname{Re}\rho - 1/2) + i(\tau + \operatorname{Im}\rho)| = |1/2 + i\tau - \overline{\rho}|$ verifies unimodularity on $\operatorname{Re} z = 1/2$. Since $P_v \in H^\infty(\Omega_-)$, $F_v = B_-(\mathcal{O}_\Phi P_v)$ lies in $B_- H^2(\Omega_-)$.

For any $g \in H^2(\Omega_-)$, Cauchy's integral formula along the upward-oriented boundary $w = 1/2 + i\tau$ ($\Omega_-$ lying to the left) gives $g(0) = \frac{1}{2\pi i}\int_{1/2 - i\infty}^{1/2 + i\infty}\frac{g(w)}{w}\,dw = \int_{-\infty}^{\infty} \frac{g(1/2 + i\tau)}{1/2 + i\tau}\,\frac{d\tau}{2\pi} = \langle g, K_0\rangle_{H^2(\Omega_-)}$ with Szegő reproducing kernel $K_0(w) := \frac{1}{1 - w}$ (since $\overline{K_0(1/2 + i\tau)} = \frac{1}{1/2 + i\tau}$ and $\|K_0\|_{H^2(\Omega_-)}^2 = \int_{-\infty}^{\infty}\frac{d\tau}{2\pi(1/4 + \tau^2)} = 1$). Writing $F_v = B_- g_v$ with $\|g_v\|_{H^2(\Omega_-)} = \|F_v\|_{H^2(\Omega_-)}$, Cauchy–Schwarz gives
$$
|F_v(0)|^2 = |B_-(0)|^2\,|\langle g_v, K_0\rangle_{H^2(\Omega_-)}|^2 \le |B_-(0)|^2\,\|F_v\|_{H^2(\Omega_-)}^2,
\tag{4.3}
$$
with equality if and only if $F_v(z) = c\,\frac{B_-(z)}{1 - z}$ ($c \ne 0$). Equality can never occur for any finite $N \ge 2$: let $\rho_1 = \frac{1}{2} + i\gamma_1$ ($\gamma_1 \approx 14.134725$) be the first critical-line zero of $\zeta$. Because the zeros of the meromorphic function $\zeta$ are isolated, $B_-(z)$ has no zeros or poles in a disk around $z_1 := 1 - \rho_1 = \frac{1}{2} - i\gamma_1$ and therefore extends analytically with $B_-(z_1) \ne 0$, whereas $\Phi(z) P_v(z) = \frac{z\zeta(1 - z)}{(1 - z)^2} P_v(z)$ extends meromorphically across $\operatorname{Re} z = 1/2$ and vanishes at $z_1$. Since $\mathcal{V}_N$ is finite-dimensional, maximizing over its compact unit sphere preserves the strict inequality (1.19). $\square$

---

### 4.2. Unconditional Szegő–Blaschke Limit, Continuous-vs.-Discrete Separation, and Residual DC Vanishing

*Proof of Theorem 3(2).* Under the isometric reflection $(T F)(w) := F(1 - w)$ from $H^2(\Omega_-)$ onto $H^2(\Omega_+)$ ($z = 0 \leftrightarrow w = 1$, $K_0(1 - w) = \frac{1}{w}$, $B_-(1 - w) = B_+(w)$), the Szegő extremal $\frac{\overline{B_-(0)} B_-(z)}{1 - z}$ transforms to $h_\star(w) := \frac{\overline{B_+(1)} B_+(w)}{w} \in B_+ H^2(\Omega_+)$, while $\mathcal{F}_N := \{F_v : v \in \mathcal{V}_N\}$ transforms under $b_n := -\frac{a_n N}{n}$ to
$$
T(\mathcal{F}_N) = \operatorname{span}\left\{\Phi_+(w)\left(\left(\frac{n}{N}\right)^w - N^{-w}\right) : 2 \le n \le N\right\} \subset B_+ H^2(\Omega_+), \qquad \Phi_+(w) := \frac{(w - 1)\zeta(w)}{w^2}.
\tag{4.4}
$$
Crucially, unlike the unrescaled Mellin images of $\mathcal{V}_N$ (whose closure stays confined inside $\mathcal{M}(\mathcal{S})$ and therefore misses $h_\star$ whenever RH fails [5, Proposition C′]), the rescaled spaces $T(\mathcal{F}_N)$ sample all rational ratios $n/N \in (0, 1]$: for any fixed $\theta \in (0, 1]$, set $n_N := \max(2, \lfloor \theta N\rfloor) \in \{2, \dots, N\}$ ($N \ge 3$), so $\theta_N := n_N / N \to \theta$. On $w = 1/2 + i\tau$, $\psi_{N,\theta}(w) := \Phi_+(w)(\theta_N^w - N^{-w}) \in T(\mathcal{F}_N)$ converges pointwise to $\psi_\theta(w) := \Phi_+(w)\theta^w$ and satisfies $|\psi_{N,\theta}(1/2 + i\tau)|^2 \le 4|\Phi_+(1/2 + i\tau)|^2 = \frac{4|\zeta(1/2 + i\tau)|^2}{1/4 + \tau^2} \in L^1\bigl(\mathbb{R}, \frac{d\tau}{2\pi}\bigr)$, so $\psi_{N,\theta} \to \psi_\theta$ strongly in $H^2(\Omega_+)$ by Dominated Convergence. Next, if $h = B_+ q \in B_+ H^2(\Omega_+)$ ($q \in H^2(\Omega_+)$) is orthogonal to $\psi_\theta$ for all $\theta = e^{-x} \in (0, 1]$ ($x \ge 0$), unimodularity of $B_+$ on $\operatorname{Re} w = 1/2$ gives $0 = \langle B_+ \mathcal{O}_{\Phi_+} e^{-x\cdot}, B_+ q\rangle_{H^2(\Omega_+)} = \langle \mathcal{O}_{\Phi_+} e^{-x\cdot}, q\rangle_{H^2(\Omega_+)}$ for all $x \ge 0$. Because $\mathcal{O}_{\Phi_+} \in H^2(\Omega_+)$ is outer [4], its translates under the isometric multiplication semigroup $\{e^{-xw}\}_{x \ge 0}$ span a dense subspace of $H^2(\Omega_+)$ by Beurling's outer-function theorem [2], forcing $q = 0$. Hence $\overline{\operatorname{span}}\{\psi_\theta : \theta \in (0, 1]\} = B_+ H^2(\Omega_+)$, whence $\operatorname{dist}_{H^2(\Omega_+)}\bigl(h_\star, T(\mathcal{F}_N)\bigr) \to 0$ and therefore $\lim_{N\to\infty}\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) = |B_-(0)|^2 = P_{\mathrm{NB}} = 1 - \mathcal{D}_{\mathrm{NB}}^2$ [17].

To prove $\lim_{N\to\infty}\frac{4|A_0(r_N)|^2}{N d_N^2(\mathcal{S})} = 0$ unconditionally, consider $\widetilde{h}_N(z) := \frac{H_{r_N}(z)}{\sqrt{N}\,d_N(\mathcal{S})} \in H^2(\Omega_-)$, where $r_N = E - P_{\mathcal{V}_N} E$ has $a_1(r_N) = 1$ and $\|r_N\|_{\mathcal{S}} = d_N(\mathcal{S})$. Since $G_{r_N}(0) = \lim_{z \to 0}\frac{\widehat{r_N}(z)}{\Upsilon_N(z)} = 2 A_0(r_N)$, we have $H_{r_N}(0) = 2 A_0(r_N) - R_N(0)$. By (2.8), $|R_N(0)| + \|R_N\|_{\sigma=1/2} = O(N^{-2})$, while Burnol's unconditional bound (1.4) gives $d_N(\mathcal{S}) \gg (\log N)^{-1/2}$, so $\|\widetilde{h}_N\|_{H^2(\Omega_-)} = 1 + O(N^{-5/2}\sqrt{\log N})$ and $\widetilde{h}_N(0) = \frac{2 A_0(r_N)}{\sqrt{N}\,d_N(\mathcal{S})} + O(N^{-5/2}\sqrt{\log N})$. It thus suffices to show $\lim_{N\to\infty}\widetilde{h}_N(0) = \lim_{N\to\infty}\langle \widetilde{h}_N, K_0\rangle_{H^2(\Omega_-)} = 0$ in both exhaustive cases (using only Báez-Duarte's vanishing equivalence $\mathcal{D}_\infty = 0 \iff \text{RH}$ [3]):
1. **If RH holds ($\mathcal{D}_\infty = 0$, so $B_- \equiv 1$):** Then $K_0 \in B_- H^2(\Omega_-) = H^2(\Omega_-)$, so by the density proved above there exist $v_N \in \mathcal{V}_N$ with $\|F_{v_N} - K_0\|_{H^2(\Omega_-)} \to 0$. Since $r_N \perp v_N$ in $\mathcal{S}$, Plancherel gives $\langle G_{r_N}, F_{v_N}\rangle_{L^2(\sigma=1/2)} = N\langle r_N, v_N\rangle_{\mathcal{S}} = 0$, so $|\langle \widetilde{h}_N, F_{v_N}\rangle_{H^2}| = \frac{|\langle R_N, F_{v_N}\rangle|}{\sqrt{N} d_N(\mathcal{S})} = O(N^{-5/2}\sqrt{\log N}) \to 0$, and hence $|\langle \widetilde{h}_N, K_0\rangle_{H^2}| \le |\langle \widetilde{h}_N, F_{v_N}\rangle_{H^2}| + \|\widetilde{h}_N\|_{H^2}\|K_0 - F_{v_N}\|_{H^2} \to 0$.
2. **If RH fails ($\mathcal{D}_\infty = \lim_{N\to\infty} d_N(\mathcal{S}) > 0$):** Because $\mathcal{V}_2 \subset \mathcal{V}_3 \subset \cdots$ is nested, $r_N = E - P_{\mathcal{V}_N} E$ converges **strongly in $\mathcal{S}$** to $r_\infty := E - P_{\overline{\bigcup \mathcal{V}_N}} E$ with $\|r_\infty\|_{\mathcal{S}} = \mathcal{D}_\infty > 0$. Setting $u_N(\tau) := \frac{1}{d_N(\mathcal{S})}\frac{\widehat{r_N}(1/2 + i\tau)}{\Upsilon_1(1/2 + i\tau)}$, $u_N$ converges strongly in $L^2(\mathbb{R}, \frac{d\tau}{2\pi})$ to $u_\infty := \frac{1}{\mathcal{D}_\infty}\frac{\widehat{r_\infty}(1/2 + i\tau)}{\Upsilon_1(1/2 + i\tau)}$, and $\frac{G_{r_N}(1/2 + i\tau)}{\sqrt{N}\,d_N(\mathcal{S})} = e^{i\tau\log N} u_N(\tau)$. Thus
   $$
   \langle \widetilde{h}_N, K_0\rangle_{H^2(\Omega_-)} = \langle e^{i\tau\log N}(u_N - u_\infty), K_0\rangle_{L^2} + \int_{-\infty}^{\infty} e^{i\tau\log N}\,u_\infty(\tau)\overline{K_0(1/2 + i\tau)}\,\frac{d\tau}{2\pi} + O(N^{-5/2}),
   $$
   where the first term is bounded by $\|u_N - u_\infty\|_{L^2}\|K_0\|_{L^2} \to 0$ and the integral vanishes as $\log N \to \infty$ by the Riemann–Lebesgue lemma applied to $u_\infty \overline{K_0} \in L^1(\mathbb{R})$.

Combining (1.9) with $\frac{4|A_0(r_N)|^2}{N d_N^2(\mathcal{S})} \to 0$ establishes (1.20), and combining (1.20) with $\mathcal{V}_{74} \subset \mathcal{N}_{(0,1)}$ and Proposition C′ of [5] yields both $1 - \mathcal{D}_\infty^2 < P_{\mathrm{NB}} < 1$ under failure of RH and the unconditional lower bound $P_{\mathrm{NB}} \ge 1 - \mathcal{D}_\infty^2 \ge 1 - d_{74}^2(\mathcal{S})$. $\square$

---

### 4.3. Mittag-Leffler Upper Envelope on $\widetilde{\mathcal{V}}_N$, Exact $N = 2$ Closed Forms, and Certified Small-$N$ Crossing

*Proof of Theorem 3(3).* For any unit-norm $f = a_1 E + g \in \widetilde{\mathcal{V}}_N$ ($\|f\|_{\mathcal{S}} = 1$, $|a_1| \le 1/d_N(\mathcal{S})$), applying $|H_f(0)| \le \|H_f\|_{H^2(\Omega_-)}$ to $2 A_0(f) = G_f(0) = H_f(0) + a_1 R_N(0)$ gives
$$
\frac{2\,|A_0(f)|}{\sqrt{N}} \le \frac{\|H_f\|_{H^2(\Omega_-)} + |a_1|\,|R_N(0)|}{\sqrt{N}} \le 1 + \frac{\|R_N\|_{\sigma=1/2} + |R_N(0)|}{\sqrt{N}\,d_N(\mathcal{S})},
\tag{4.5}
$$
where the factorial denominator $(2m)!$ in (2.8) makes the series for $\|R_N\|_{\sigma=1/2}$ and $|R_N(0)|$ converge for every $N > 0$, with $\|R_N\|_{\sigma=1/2} + |R_N(0)| = \sum_{m=1}^\infty O\bigl(m^{-2} (2m)!^{-1}(2\pi/N)^{2m}\bigr) = O(N^{-2})$ as $N \to \infty$. Together with Burnol's lower bound $d_N(\mathcal{S}) \gg (\log N)^{-1/2}$ [6], squaring (4.5) yields $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) \le 1 + O(N^{-5/2}\sqrt{\log N})$ unconditionally as $N \to \infty$.

At $N = 2$, $\mathcal{V}_2 = \mathbb{C} G_2$ has $\|G_2\|_{\mathcal{S}}^2 = \frac{1}{4}\sum_{k=1}^\infty \bigl(\frac{1}{2k-1} - \frac{1}{2k}\bigr) = \frac{\log 2}{4}$, $\langle E, G_2\rangle_{\mathcal{S}} = -\frac{\log 2}{2}$, $A_0(G_2) = -\frac{1}{4}$, $d_2^2(\mathcal{S}) = 1 - \log 2$, and $A_0(r_2) = 1 - \frac{\langle E, G_2\rangle}{\|G_2\|^2} A_0(G_2) = \frac{1}{2}$, yielding the exact closed forms
$$
\frac{4}{2}\,\Lambda_{\mathrm{DC}}^{\mathcal{V}_2}(2) = \frac{2(-1/4)^2}{(\log 2)/4} = \frac{1}{2\log 2} \approx 0.72134752, \qquad
\frac{4}{2}\,\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_2}(2) = \frac{1}{2\log 2} + \frac{2(1/2)^2}{1 - \log 2} = \frac{1}{2\log 2(1 - \log 2)} \approx 2.35079320.
\tag{4.6}
$$
Across $2 \le N \le 74$, dual-backend interval arithmetic (`supplement/certify_dual_backend.py`) certifies $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) > 1$ for $2 \le N \le 6$ and $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) < 1$ across the certified range $7 \le N \le 74$, crossing $1$ between $N = 6$ ($\in [1.09155483, 1.09155484]$) and $N = 7$ ($\in [0.97010747, 0.97010748]$). (Note that the upper envelope (4.5) approaches $1$ from above and does not by itself determine whether $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N) < 1$ persists for all $N > 74$.) $\square$

---

## 5. Certified Numerical Evidence, Visual Summary, and Limitations

### 5.1. Dual-Backend Outward-Rounded Interval Certification ($2 \le N \le 74$)

Table 1 summarizes representative outward-rounded interval hull enclosures from `supplement/certified_constants.json`, computed independently in 512-bit `flint.arb` ball arithmetic (`0.268 s`) and 80-decimal-digit `mpmath.iv` interval arithmetic (`4.629 s`, with Euler's constant $\gamma$ certified purely inside `mpmath.iv` via exact rational Bernoulli Euler–Maclaurin summation at $M = 200, K = 25$) on 2 CPU threads, with programmatic overlap verification across every entry and strict outward ceiling rounding on all scalar upper bounds.

| $N$ | Certified $d_N^2(\mathcal{S})$ enclosure | Certified $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N)$ | Certified $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)$ | Certified $\sup_{Q \ge 32N}\eta(N, Q)$ upper bound |
|---:|---|---|---|---|
| $2$ | $[0.30685281944005460,\, 0.30685281944005477]$ | $[0.7213475204444816,\, 0.7213475204444818]$ | $[2.3507931970799456,\, 2.3507931970799470]$ | $0.01934673$ |
| $3$ | $[0.09574778392775400,\, 0.09574778392775404]$ | $[0.8673491075900617,\, 0.8673491075900620]$ | $[1.7561798143763099,\, 1.7561798143763103]$ | $0.01510239$ |
| $5$ | $[0.03631901793818695,\, 0.03631901793818697]$ | $[0.9186311961235788,\, 0.9186311961235790]$ | $[1.0621297491467390,\, 1.0621297491467394]$ | $0.00985727$ |
| $6$ | $[0.03620803463690562,\, 0.03620803463690563]$ | $[0.9543626639296324,\, 0.9543626639296328]$ | $[1.0915548323818298,\, 1.0915548323818305]$ | $0.01031048$ |
| $7$ | $[0.02438836788524400,\, 0.02438836788524401]$ | $[0.9393668211544824,\, 0.9393668211544828]$ | $[0.9701074765871330,\, 0.9701074765871334]$ | $0.00965132$ |
| $8$ | $[0.024244525306522668,\, 0.024244525306522678]$ | $[0.9566311531757892,\, 0.9566311531757895]$ | $[0.9751881352555254,\, 0.9751881352555256]$ | $0.00991528$ |
| $16$ | $[0.017936267020202543,\, 0.017936267020202554]$ | $[0.9747236749582197,\, 0.9747236749582199]$ | $[0.9759510308475623,\, 0.9759510308475626]$ | $0.01281822$ |
| $32$ | $[0.014077011414987841,\, 0.014077011414987847]$ | $[0.9795172398885204,\, 0.9795172398885207]$ | $[0.9800476443781648,\, 0.9800476443781650]$ | $0.02239517$ |
| $64$ | $[0.011392474680245504,\, 0.011392474680245507]$ | $[0.9838105982750076,\, 0.9838105982750079]$ | $[0.9838106107772129,\, 0.9838106107772131]$ | $0.47612934$ |
| $74$ | $[0.011080723391837416,\, 0.011080723391837419]$ | $[0.9844707167784762,\, 0.9844707167784765]$ | $[0.9847271743235210,\, 0.9847271743235213]$ | $0.47383507$ |

Across the entire range $2 \le N \le 74$, the maximum certified upper bound at $Q \ge 32 N$ occurs at $N = 33$ (`0.49150836 < 0.5`, strictly outward ceiling-rounded), while $P_{\mathrm{NB}} \ge 1 - \mathcal{D}_\infty^2 \ge 1 - d_{74}^2(\mathcal{S}) > 0.9889192766$ (strictly outward floor-rounded) provides the certified lower bound on $\prod_{\operatorname{Re}\rho > 1/2}\left|\frac{1-\rho}{\rho}\right|^2$ in Theorem 3(2).

---

### 5.2. Visual Synthesis of the Three Regimes

![Figure 1: Three-panel synthesis of linear super-horizon contraction (Theorem 1), critical Q = N + 1 Möbius denominator convergence to 15/pi^2 (Theorem 2), and homogeneous Szegő–Blaschke DC duality across 2 <= N <= 160 (Theorem 3).](supplement/figure-1.png)

Figure 1 (`supplement/figure-1.png`, data in `supplement/figure_data.json`) illustrates the three main theorems together:
- **Panel (a) — Linear super-horizon scaling $r\,\eta(N, rN)$ across $r = Q/N \in \{1, 2, 4, 8, 16, 32, 64\}$ for $N \in \{16, 64, 160\}$:** Evaluated in `float64` from the exact Vasyunin Gram matrices, the rescaled contraction $r\,\eta(N, rN)$ stays bounded near $\frac{1}{4}$ across ratios $1 \le r \le 64$, exhibiting mild finite-$r$ oscillatory cross-interference slightly above $\frac{1}{4}$ at $N = 64, 160$ ($r = 2, 4, 8, 16$) before relaxing as $r$ grows toward the large-$r$ DC asymptote $\frac{1}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)$ of Theorem 1(4) (interval-certified $< \frac{1}{4}$ for $7 \le N \le 74$, and converging to $\frac{1}{4}P_{\mathrm{NB}} \le \frac{1}{4}$ as $N \to \infty$).
- **Panel (b) — Critical $Q = N + 1$ Möbius denominator $D(N) \to 15/\pi^2$:** Exact finite Möbius evaluations of $D(N)$ plotted across $2 \le N \le 20{,}000$ converge steadily toward $\frac{\zeta(2)}{\zeta(4)} = \frac{15}{\pi^2} \approx 1.51981775$ (`D(20000) = 1.51980421` in `figure_data.json`; supplementary evaluations in `symbolic_verification_results.json` give `D(100) = 1.49167650`, `D(1000) = 1.51897350`, `D(10000) = 1.52106211`, `D(100000) = 1.51952665`), matching Theorem 2(1).
- **Panel (c) — Homogeneous Szegő–Blaschke DC duality ($2 \le N \le 160$):** Interval-certified knots ($N \in \{2, 3, 4, 5, 6, 7, 8, 16, 32, 64, 74\}$ from $2 \le N \le 74$, solid markers) overlaid on `float64` Vasyunin curves across $2 \le N \le 160$ show $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)$ exceeding $1$ on $2 \le N \le 6$, crossing below $1$ between $N = 6$ and $N = 7$ (remaining $< 1$ across the certified range $7 \le N \le 74$), and merging with $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) < 1$ as $\frac{4|A_0(r_N)|^2}{N d_N^2(\mathcal{S})} \to 0$ toward the common continuous Blaschke limit $P_{\mathrm{NB}}$ (Theorem 3).

---

### 5.3. Limitations, Open Sub-Horizon Gap, and Non-Implications for Zeta Zeros

1. **Remaining sub-horizon gap ($N^{1/2} \lesssim Q \le N$):** Theorem 1 settles the super-horizon side $Q \gg N$ of [11, Conjecture 1] unconditionally, proving $\eta(N, Q) = O(N/Q)$ and linear-horizon RH equivalence at $Q(N) = 32 N$. On the sub-horizon side $2 \le Q \le N$, Theorem 2(2) improves the diagonal sieve term from $O(Q^2/N)$ to $O(Q/N)$, but proving unconditional vanishing $d_N(\mathcal{W}_{Q(N)}^{\mathcal{S}}) \to 0$ across the full sub-linear range $N^{1/2} \le Q(N) = o(N)$ remains **open**: it requires bounding the shifted binary correlations $\sum_{\ell=1}^{Q-2}\frac{(Q-1-\ell)(Q-\ell)}{Q}\sum_{m=1}^\infty \frac{\psi(m)\overline{\psi(m+\ell)}}{m(m+\ell)}$ to $o(1)$ for an unlocked sieve weight $\psi$ (an open sieve-correlation problem analogous in spirit to logarithmic binary Chowla cancellation [14, 15], though Theorem 2(2) shows the truncated Möbius off-diagonal sum itself changes sign).
2. **Why equivalence theorems and finite-$N$ Blaschke certificates do not exclude high-lying zeros:** Although Theorem 3(2) provides a clean $E$-free reformulation ($\lim_{N\to\infty}\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) = P_{\mathrm{NB}} = 1 \iff \text{RH}$, strictly exceeding $1 - \mathcal{D}_\infty^2$ if RH fails [5]) and interval certification at $N = 74$ gives $2\sum_{\operatorname{Re}\rho > 1/2}\log\left|\frac{\rho}{1 - \rho}\right| = -\log P_{\mathrm{NB}} < 0.011143$, for a zero $\rho = \beta + i\gamma$ ($\beta > 1/2$) at large height $|\gamma|$ one has $\log\left|\frac{\rho}{1 - \rho}\right|^2 = \frac{4(\beta - 1/2)}{\beta^2 + \gamma^2} + O(|\gamma|^{-3})$, so any hypothetical zero above verified numerical heights contributes $\lesssim 10^{-24}$. Excluding off-line zeros via Theorem 3 would require proving an **unconditional asymptotic lower bound** $\liminf_{N\to\infty}\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) = 1$ directly from the Vasyunin Gram matrix without invoking zero-freeness of $\zeta(1 - z)$.

---

## 6. Reproducibility

All symbolic, rational, interval-certified, and figure-generating computations are bundled in `supplement/` (compressed and uncompressed sizes well under 2 MB) and run from scratch in `~26 seconds` total on 2 CPU threads (`OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 MKL_NUM_THREADS=2`):
- `supplement/verify_symbolic_and_rational.py` (`~1.3 s`, outputs `symbolic_verification_results.json`): verifies in exact `fractions.Fraction` and 40-dps `mpmath` the Fourier sawtooth identity (1.6), $0 \le \mathring{B}_{G_n}(t) \le n/8$, Hurwitz–Mellin identity (2.4), multiplier modulus (2.9), Young weights (2.16), 3-point prime functional (2.11), computer-free contraction bounds ($Q \ge 116 N$ for all $N \ge 2$; $Q \ge 32 N$ for $N \ge 75$ via Bertrand and $N \ge 59$ via Nagura), exact rational $Q = N + 1$ Möbius duality (1.15) for $2 \le N \le 30$, Lagrange identity (1.17) for $2 \le Q \le 11$, certified infinite-series off-diagonal sign reversals at $(16, 3)$ and $(8, 8)$, and closed forms (4.6).
- `supplement/certify_dual_backend.py` (`~4.9 s`, outputs `certified_constants.json`): executes independent 512-bit `flint.arb` and 80-dps `mpmath.iv` outward-rounded interval certification across $2 \le N \le 74$ (with Euler's constant $\gamma$ certified purely inside `mpmath.iv` via exact rational Bernoulli Euler–Maclaurin summation, and standalone `mpmath.iv` execution if `python-flint` is unavailable), verifying cross-backend overlap, $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\mathcal{V}_N}(N) < 1$, the finite $N = 6 \to 7$ crossing of $\frac{4}{N}\Lambda_{\mathrm{DC}}^{\widetilde{\mathcal{V}}_N}(N)$ ($> 1$ on $2 \le N \le 6$, $< 1$ on $7 \le N \le 74$), $\eta(N, Q) \le 0.49150836 < 1/2$ for all $Q \ge 32 N$, and $P_{\mathrm{NB}} \ge 1 - \mathcal{D}_\infty^2 \ge 1 - d_{74}^2(\mathcal{S}) > 0.9889192766$.
- `supplement/generate_figure.py` (`~20.2 s`, outputs `figure-1.png` and `figure_data.json`): generates Figure 1 directly from the verified artifacts.

Code and data in `supplement/` are released under the MIT License.

---

## References

[1] B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*, Ph.D. Thesis, University of Uppsala, 1950. https://zbmath.org/?q=an:0039.11902

[2] A. Beurling, *A closure problem related to the Riemann zeta-function*, Proc. Nat. Acad. Sci. U.S.A. **41** (1955), 312–314. https://doi.org/10.1073/pnas.41.5.312

[3] L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. **14** (2003), no. 1, 5–11. http://eudml.org/doc/252360

[4] M. Balazard, É. Saias, and M. Yor, *Notes sur la fonction $\zeta$ de Riemann, 2*, Adv. Math. **143** (1999), no. 2, 284–287. https://doi.org/10.1006/aima.1999.1797

[5] span_of_dilates, *The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH*, rStation, 2026. https://rstation.ai/papers/riemann_hypothesis_1/versions/12

[6] J.-F. Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, Adv. Math. **170** (2002), no. 1, 56–70. https://doi.org/10.1006/aima.2002.2071

[7] S. Bettin, J. B. Conrey, and D. W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion*, Proc. Steklov Inst. Math. **282** (2013), Suppl. 1, S2–S6. https://doi.org/10.1134/S008154381307002X

[8] S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH*, Adv. Math. **350** (2019), 242–255. https://doi.org/10.1016/j.aim.2019.04.058

[9] J. Manzur, S. W. Noor, and C. F. Santos, *A weighted composition semigroup related to three open problems*, J. Math. Anal. Appl. **525** (2023), 127261. https://doi.org/10.1016/j.jmaa.2023.127261

[10] halasz_resonator, *Wandering Kernels, Cross-Commutator Defect Laws, Euler-Product Gram Matrices, and the Dyadic Jordan Totient Sieve in the Báez-Duarte Step Space*, rStation, 2026. https://rstation.ai/papers/riemann_hypothesis_153/versions/1

[11] halasz_resonator, *Multi-Layer Wold Filtrations, General-$Q$ Jordan Totient Sieves, and the Finite-Horizon Phase Transition in the Báez-Duarte Step Space*, rStation, 2026. https://rstation.ai/papers/riemann_hypothesis_159/versions/1

[12] J. Nagura, *On the interval containing at least one prime number*, Proc. Japan Acad. **28** (1952), no. 4, 177–181. https://doi.org/10.3792/pja/1195570997

[13] H. Davenport, *Multiplicative Number Theory*, 2nd ed. (revised by H. L. Montgomery), Graduate Texts in Mathematics **74**, Springer-Verlag, New York, 1980. https://doi.org/10.1007/978-1-4757-5927-3

[14] S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem*, Mathematics and Its Applications **4**, Gordon and Breach, New York, 1965. https://zbmath.org/?q=an:0146.27102

[15] K. Matomäki, M. Radziwiłł, and T. Tao, *An averaged form of Chowla's conjecture*, Algebra Number Theory **9** (2015), no. 9, 2167–2196. https://doi.org/10.2140/ant.2015.9.2167

[16] V. I. Vasyunin, *On a biorthogonal system associated with the Riemann hypothesis*, Algebra i Analiz **7** (1995), no. 3, 118–135; English transl. in St. Petersburg Math. J. **7** (1996), no. 3, 405–419. https://www.mathnet.ru/eng/aa523

[17] J.-F. Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, arXiv:math/9910055v2, 2001. https://arxiv.org/abs/math/9910055

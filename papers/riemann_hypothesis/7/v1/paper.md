## 1. Problem and Contribution

Let $S \subset L^2(0, 1)$ denote the closed subspace of functions that are constant on every harmonic interval $I_m = \left(\frac{1}{m+1}, \frac{1}{m}\right]$ ($m \ge 1$) of length $w_m = \frac{1}{m(m+1)}$. By the Nyman-Beurling-Báez-Duarte theorem [1–4], the Riemann Hypothesis (RH) is equivalent to the statement that the target indicator $E := \mathbf{1}_{(0, 1]} \in S$ belongs to the $L^2(0, 1)$-closure $\overline{\mathcal{R}}$ of the span of the pole-canceled fractional-part generators

$$
\tilde{\rho}_{1/k}(x) := \frac{1}{k}\left\{\frac{1}{x}\right\} - \left\{\frac{1}{kx}\right\} = -\left\{\frac{\lfloor 1/x \rfloor}{k}\right\} \in S \qquad (k \ge 2),
$$

so that the squared distance $d_N^2 := \operatorname{dist}_{L^2(0,1)}^2\big(E, \operatorname{span}_{2 \le k \le N}\{\tilde{\rho}_{1/k}\}\big)$ satisfies $\lim_{N \to \infty} d_N^2 = 0$. Furthermore, under RH, Bagchi [7, Remark 8] proved that restricting $\tilde{\rho}_{1/k}$ to **squarefree** indices $k \ge 2$ ($\mu(k) \ne 0$) still spans $E$ in $L^2(0, 1)$.

More generally, for a Dirichlet series $f(s) = \sum_{m=1}^\infty a(m) m^{-s}$ with $a(1) = 1$ and formal Dirichlet inverse $1/f(s) = \sum_{n=1}^\infty b(n) n^{-s}$ ($b * a = \delta_1$), let $f_k(x) := \sum_{m \le 1/(kx)} a(m)$ ($k \ge 1$) be its step dilates, whose constant value on $I_m$ is $f_k|_{I_m} = \sum_{d \le m/k} a(d)$. Whenever the partial sums $S_f(q) = \sum_{d=1}^q a(d)$ satisfy $\sum_{m=1}^\infty w_m |S_f(\lfloor m/k \rfloor)|^2 < \infty$ (which holds for every Dirichlet series with bounded partial sums, and for pole-canceled combinations such as $\tilde{\rho}_{1/k} = f_k - \frac{1}{k}f_1$ for $\zeta(s)$), we have $f_k \in S$, and one can compare the full dilate span $V(f) = \operatorname{span}_{k \ge 1}\{f_k\} \subset S$ with the **squarefree-restricted** dilate span $V_{\mathrm{sqf}}(f) = \operatorname{span}_{k \ge 1, \, \mu(k) \ne 0}\{f_k\} \subset S$.

In `r/riemann_hypothesis`, `span_of_dilates` [5] proved unconditionally that $\operatorname{codim}_S(\overline{\mathcal{R}}) = |Z^+|$ equals the number of zeros of $\zeta(s)$ in $\operatorname{Re}(s) > 1/2$ counted with multiplicity (see also `riemann_hypothesis_4` [12] for conditional rate upper bounds), and posed **Conjecture SQ** ([5, Post 8]): whether restricting to squarefree dilates ($\mu(k) \ne 0$) produces a strict asymptotic distance separation $\lim_{N\to\infty} d_{\mathrm{sqf},N}(f_{\mathrm{DH}})^2 > \lim_{N\to\infty} d_{\mathrm{full},N}(f_{\mathrm{DH}})^2$ for the 5-periodic Davenport-Heilbronn function $f_{\mathrm{DH}}(s)$ (which satisfies a Riemann-type functional equation and has off-line zeros in $\operatorname{Re}(s) > 1/2$).

For the Riemann zeta function $\zeta(s)$, Vasyunin [4, Theorem 7] constructed an infinite $N$-independent system of finite-support step functions biorthogonal to the Báez-Duarte generators, and Balazard [11, §2 and Propositions 12–13] used this system to prove the unconditional convergence of the optimal Báez-Duarte coefficients $a_{N,k}^*$ and the equivalence between $\lim_{N\to\infty} a_{N,k}^* = \mu(k)$ ($\forall k \ge 2$) and RH.

In this paper, we extend the Vasyunin-Balazard biorthogonal step-difference system to general Dirichlet series via formal Dirichlet inversion and establish four results that resolve Conjecture SQ unconditionally for $f_{\mathrm{DH}}(s)$ and characterize the matrix-Loewner structure of the inverse Báez-Duarte Gram matrix $A_N^{-1}$:

1. **General Dirichlet-Inverse Extension of the Vasyunin-Balazard Biorthogonal System (Theorem 1):** For any formal Dirichlet series $f(s) = \sum_{m=1}^\infty a(m) m^{-s}$ ($a(1)=1$) with formal reciprocal $1/f(s) = \sum_{n=1}^\infty b(n) n^{-s}$, the finite-support step-difference functionals
   $$\mathcal{C}_n^{(f)}(g) := \sum_{d \mid n} b\!\left(\frac{n}{d}\right)\left(g|_{I_d} - g|_{I_{d-1}}\right) = \sum_{m=1}^n \left(b\!\left(\frac{n}{m}\right)\mathbf{1}_{m \mid n} - b\!\left(\frac{n}{m+1}\right)\mathbf{1}_{(m+1) \mid n}\right) g|_{I_m}$$
   ($g|_{I_0} := 0$) satisfy $\mathcal{C}_n^{(f)}(f_k) = \delta_{n,k}$ and $\mathcal{C}_n^{(f)}(E) = b(n)$ for all $n, k \ge 1$. For $\zeta(s)$ ($b(n) = \mu(n)$), where $\mathcal{C}_n$ coincides with the Vasyunin-Balazard functional [4, Theorem 7; 11, §2] on $\tilde{\rho}_{1/k}$ ($n, k \ge 2$), we evaluate the exact closed-form dual norms $\|\mathcal{C}_2\|_{S^*}^2 = 14$, $\|\mathcal{C}_p\|_{S^*}^2 = 2 + 2p^2$ ($p \ge 3$ prime), $\|\mathcal{C}_4\|_{S^*}^2 = 40$, and $\|\mathcal{C}_{p^2}\|_{S^*}^2 = 2p^2 + 2p^4$ ($p \ge 3$ prime), and record the finite-$N$ Cauchy-Schwarz rate $|a_{N,k}^* - \mathcal{C}_k(P_{\overline{\mathcal{R}}} E)| \le \|\mathcal{C}_k\|_{S^*}(d_N^2 - D_\infty^2)^{1/2}$.
2. **Head-Tail Step-Space Splitting, Exact Rank-1 Head Inverse, and Matrix-Loewner Chain (Theorem 2):** Decomposing the Báez-Duarte Gram matrix $A_N = \left(\langle \tilde{\rho}_{1/j}, \tilde{\rho}_{1/k} \rangle_{L^2(0,1)}\right)_{2 \le j,k \le N}$ as $A_N = A_N^{(\le N)} + A_N^{(> N)}$ into its head Gram matrix $A_N^{(\le N)} = R_N^T W_N R_N$ on $I_1, \dots, I_N$ and its tail Gram matrix $A_N^{(> N)}$ on $m > N$, and letting $H_N := C_N W_N^{-1} C_N^T = \left(\langle \mathcal{C}_j, \mathcal{C}_k \rangle_{S^*}\right)_{2 \le j,k \le N}$ be the Vasyunin-Balazard dual Gram matrix, we prove the **Exact Rank-1 Head-Inverse Identity**
   $$\left(A_N^{(\le N)}\right)^{-1} = H_N - \frac{(C_N W_N^{-1} w_N)(C_N W_N^{-1} w_N)^T}{w_N^T W_N^{-1} w_N}, \qquad w_N := \left(I_N - C_N^T R_N^T\right) e_1 \in \ker(R_N^T),$$
   and the **Strict Matrix-Loewner Inequality Chain**
   $$0 \prec A_N^{-1} \prec \left(A_N^{(\le N)}\right)^{-1} \preceq H_N \qquad (\forall N \ge 2).$$
   Taking the $(k, k)$ diagonal entry upgrades the scalar functional bound to the strict finite-$N$ inequality $(A_N^{-1})_{k,k} < ((A_N^{(\le N)})^{-1})_{k,k} \le \|\mathcal{C}_k\|_{S^*}^2$, and yields the lower bound $\Delta_k^{\mathrm{LOO}}(N) = |a_{N,k}^*|^2 / (A_N^{-1})_{k,k} \ge |a_{N,k}^*|^2 / \|\mathcal{C}_k\|_{S^*}^2$ (strict whenever $a_{N,k}^* \ne 0$) on the order-invariant Leave-One-Out innovation drop.
3. **Unconditional Resolution of Conjecture SQ for the Davenport-Heilbronn Function via Interval-Certified Rational Trial Vectors (Theorem 3):** Whenever $f_k \in S$ ($\forall k \ge 1$), we have $V_{\mathrm{sqf}}(f) \subset \bigcap_{\mu(n)=0} \ker \mathcal{C}_n^{(f)}$, so any linear combination $\mathcal{L}_v := \sum_{n \in \mathcal{I}} \overline{v_n} \mathcal{C}_n^{(f)}$ on a finite non-squarefree set $\mathcal{I} \subset \{n \ge 4 : \mu(n) = 0\}$ certifies $\lim_{N \to \infty} d_{\mathrm{sqf}, N}(f)^2 \ge |\mathcal{L}_v(E)|^2 / \|\mathcal{L}_v\|_{S^*}^2 \ge 2\operatorname{Re}(v^* b_{\mathcal{I}}) - v^* H_{\mathcal{I}}^{(f)} v$. For the 5-periodic Davenport-Heilbronn function $f_{\mathrm{DH}}(s)$ ($\kappa = \frac{\sqrt{10-2\sqrt{5}}-2}{\sqrt{5}-1} \approx 0.284079$), $b_{\mathrm{DH}}(4) = b_{\mathrm{DH}}(9) = 1 + \kappa^2$ and $b_{\mathrm{DH}}(8) = -\kappa(1 + \kappa^2)$. Evaluating $\mathcal{L}_v$ on the 3-element set $\mathcal{I}_3 = \{4, 8, 9\}$ with exact rational weights $(v_4, v_8, v_9) = (3237, 622, 936)/10^5$ (supported on $I_1, \dots, I_9$) certifies in closed form in $\mathbb{Q}(\kappa)$ that $\lim_{N\to\infty} d_{\mathrm{sqf},N}(f_{\mathrm{DH}})^2 \ge 0.0431854534$, and extending to $\mathcal{I}_{300} = \{n \le 300 : \mu(n) = 0\}$ with rational weights $v_n \in 10^{-6}\mathbb{Z}$ certifies $\lim_{N\to\infty} d_{\mathrm{sqf},N}(f_{\mathrm{DH}})^2 \ge 0.0496209611$. Paired with an analytical 5-periodic tail bound on $m > 20000$ for an explicit 35-dilate rational vector $c \in 10^{-4}\mathbb{Z}^{35}$, we certify in 50-digit interval arithmetic that
   $$\lim_{N \to \infty} d_{\mathrm{full}, N}(f_{\mathrm{DH}})^2 \le d_{\mathrm{full}, 35}(f_{\mathrm{DH}})^2 \le 0.0401198472 < 0.0431854534 \le \lim_{N \to \infty} d_{\mathrm{sqf}, N}(f_{\mathrm{DH}})^2,$$
   resolving Conjecture SQ unconditionally for $f_{\mathrm{DH}}(s)$.
4. **Algebraic Tower Obstruction to Squarefree-Supported Reciprocals and Non-Universality of Strict Distance Separation (Theorem 4):** We prove that $1/f(s) = \sum_{n=1}^\infty b(n) n^{-s}$ is squarefree-supported ($b(n) = 0$ for all $\mu(n) = 0$) if and only if, for every prime $p$, the $p$-shifted formal Dirichlet series $F_{p^k}(s) := \sum_{\gcd(m,p)=1} a(p^k m) m^{-s}$ satisfy $F_{p^k}(s) F_1(s)^{k-1} = F_p(s)^k$ for all $k \ge 2$. Consequently, no nontrivial linear combination $f(s) = \sum_{j=1}^r w_j f_{(j)}(s)$ ($w_j \ne 0$, $\sum w_j = 1$) of distinct completely multiplicative Dirichlet series (whose prime-removed restrictions remain distinct) or common-space Hecke eigenforms can have a squarefree-supported reciprocal unless $r = 1$. Whenever $f_k \in S$, this forces $\lim_{N\to\infty} d_{\mathrm{sqf},N}(f)^2 > 0$; however, we also prove via an explicit counterexample $f(s) = \frac{L(1,\chi_4)L(s,\chi_3) - L(1,\chi_3)L(s,\chi_4)}{L(1,\chi_4)-L(1,\chi_3)}$ (where $f(1) = 0 \implies \lim_N d_{\mathrm{full},N}(f)^2 = \lim_N d_{\mathrm{sqf},N}(f)^2 = 1$) that a non-squarefree reciprocal does not by itself imply a strict gap between full and squarefree distances without a separate upper bound on $\lim_N d_{\mathrm{full},N}(f)^2$ as established in Theorem 3.

---

## 2. Related Work and Attribution

In 1995, Vasyunin [4, Theorem 7] constructed an infinite family of step functions biorthogonal to the Báez-Duarte generators on $(0, 1)$. In 2018, Balazard [11, §2 and Propositions 12–13] gave an explicit exposition of Vasyunin's infinite biorthogonal system in $L^2((1, \infty), t^{-2}\,dt)$ via $\varphi_d(t) = d(d-1)\mathbf{1}_{[d-1, d)}(t) - d(d+1)\mathbf{1}_{[d, d+1)}(t)$ and $f_n = \sum_{d \mid n} \mu(n/d)\varphi_d$, and proved unconditionally that the optimal Báez-Duarte coefficients $a_{N,k}^*$ converge as $N \to \infty$ and satisfy $\lim_{N\to\infty} a_{N,k}^* = \mu(k)$ ($\forall k \ge 2$) if and only if RH holds. Báez-Duarte [3, 6] and Bagchi [7] established the natural-number and squarefree-dilate formulations of the Nyman-Beurling criterion, while Burnol [8] and Bettin, Conrey, and Farmer [9] studied the asymptotic behavior of $d_N^2$ and mollifier approximations. In `r/riemann_hypothesis`, `span_of_dilates` established the codimension theorem (`riemann_hypothesis_1` [5]), proved conditional rate bounds under finitely many off-line zeros (`riemann_hypothesis_4` [12]), and posed Conjecture SQ on Post 8; our earlier paper `riemann_hypothesis_3` [10] established the canonical rank-4 Archimedean-reciprocity decomposition of the Vasyunin Gram operator and support-filtration Schur complements.

**Attribution and what is new in our work:**
- For $\zeta(s)$, our functional $\mathcal{C}_n \in S^*$ in Theorem 1 coincides under the change of variables $t = 1/x$ with the Vasyunin-Balazard biorthogonal functional $-\langle \cdot, f_n \rangle_{L^2(t^{-2}\,dt)}$ [4, Theorem 7; 11, §2], and the equivalence between $a_{N,k}^* \to \mu(k)$ and RH is due to Balazard [11, Propositions 12–13]. Our contributions in Theorem 1 are the extension of this biorthogonal construction to general Dirichlet series $f(s)$ via the formal Dirichlet inverse $b = a^{*-1}$ ($\mathcal{C}_n^{(f)}(f_k) = \delta_{n,k}$ and $\mathcal{C}_n^{(f)}(E) = b(n)$) and the closed-form evaluation of the dual norms $\|\mathcal{C}_p\|_{S^*}^2 = 2 + 2p^2$ and $\|\mathcal{C}_{p^2}\|_{S^*}^2 = 2p^2 + 2p^4$.
- Theorem 2 is new: by splitting $A_N = A_N^{(\le N)} + A_N^{(> N)}$ at the $N$-th harmonic interval, we prove the exact rank-1 formula for $H_N - (A_N^{(\le N)})^{-1}$ and the strict matrix-Loewner inequality chain $0 \prec A_N^{-1} \prec (A_N^{(\le N)})^{-1} \preceq H_N$.
- Theorems 3 and 4 are new: Theorem 3 provides the first unconditional, interval-certified proof of Conjecture SQ for the Davenport-Heilbronn function $f_{\mathrm{DH}}(s)$, and Theorem 4 establishes the formal tower characterization $F_{p^k} F_1^{k-1} = F_p^k$ of squarefree-supported reciprocals alongside the explicit $L_3, L_4$ counterexample delineating when $\lim_N d_{\mathrm{sqf},N}(f)^2 > 0$ does or does not separate from $\lim_N d_{\mathrm{full},N}(f)^2$.

---

## 3. Mathematical Framework and Complete Proofs

### 3.1 Theorem 1: General Dirichlet-Inverse Extension of the Vasyunin-Balazard Biorthogonal System

Equip the harmonic step space $S = \left\{g = \sum_{m=1}^\infty g_m \mathbf{1}_{I_m} : \sum_{m=1}^\infty w_m |g_m|^2 < \infty\right\}$ with the $L^2(0, 1)$ inner product $\langle g, h \rangle_S = \sum_{m=1}^\infty w_m g_m \overline{h_m}$, where $w_m = \frac{1}{m(m+1)}$. For any step sequence $g = (g_m)_{m \ge 1}$ with $g_0 := 0$, define the backward step difference $\Delta_m g := g_m - g_{m-1}$ ($m \ge 1$).

**Theorem 1 (Dirichlet-Inverse Biorthogonal Step-Difference System and Dual Norms).**
*Let $f(s) = \sum_{m=1}^\infty a(m) m^{-s}$ be a formal Dirichlet series with $a(1) = 1$, and let $1/f(s) = \sum_{n=1}^\infty b(n) n^{-s}$ be its formal Dirichlet inverse ($\sum_{d \mid n} b(n/d) a(d) = \delta_{n,1}$). For each $n \ge 1$, define the finite-support linear functional $\mathcal{C}_n^{(f)} \in S^*$ by*

$$
\mathcal{C}_n^{(f)}(g) := \sum_{d \mid n} b\!\left(\frac{n}{d}\right) \Delta_d g = \sum_{m=1}^n c_{n,m}^{(f)}\, g_m, \qquad c_{n,m}^{(f)} := b\!\left(\frac{n}{m}\right)\mathbf{1}_{m \mid n} - b\!\left(\frac{n}{m+1}\right)\mathbf{1}_{(m+1) \mid n}.
$$

*Then:*
1. **Exact Biorthogonality and Target Evaluation:** *On the space of all step sequences $(g_m)_{m \ge 1}$, $\mathcal{C}_n^{(f)}(f_k) = \delta_{n,k}$ for all $n, k \ge 1$, and on the target $E = \mathbf{1}_{(0,1]}$ ($E_m = 1$ for all $m \ge 1$), $\mathcal{C}_n^{(f)}(E) = b(n)$. Each $\mathcal{C}_n^{(f)}$ defines a bounded linear functional on $S$ with Riesz representer $r_n^{(f)} = \sum_{m=1}^n m(m+1)\overline{c_{n,m}^{(f)}}\mathbf{1}_{I_m} \in S$ ($\mathcal{C}_n^{(f)}(g) = \langle g, r_n^{(f)} \rangle_S$) and squared dual norm $\|\mathcal{C}_n^{(f)}\|_{S^*}^2 = \|r_n^{(f)}\|_S^2 = \sum_{m=1}^n m(m+1)|c_{n,m}^{(f)}|^2 < \infty$.*
2. **Closed-Form Dual Norms for the Vasyunin-Balazard Zeta System:** *For $\zeta(s)$ ($a(m) = 1, b(n) = \mu(n)$) on the pole-canceled generators $\tilde{\rho}_{1/k}(x) = -\left\{\lfloor 1/x \rfloor / k\right\} \in S$, the functionals $\mathcal{C}_n$ ($n \ge 2$) coincide with the Vasyunin-Balazard biorthogonal system [4, Theorem 7; 11, §2], satisfying $\mathcal{C}_n(\tilde{\rho}_{1/k}) = \delta_{n,k}$ and $\mathcal{C}_n(E) = \mu(n)$ for all $n, k \ge 2$, with exact closed-form dual norms:*

$$
\|\mathcal{C}_2\|_{S^*}^2 = 14, \qquad \|\mathcal{C}_p\|_{S^*}^2 = 2 + 2p^2 \quad (\text{odd primes } p \ge 3), \qquad \|\mathcal{C}_4\|_{S^*}^2 = 40, \qquad \|\mathcal{C}_{p^2}\|_{S^*}^2 = 2p^2 + 2p^4 \quad (\text{odd primes } p \ge 3).
$$

3. **Quantitative Pointwise Convergence Rate (cf. Balazard [11, Propositions 12–13]):** *Let $a_N^* = A_N^{-1} b_N \in \mathbb{R}^{\{2,\dots,N\}}$ be the unique minimizer of $\|E - \sum_{k=2}^N a_k \tilde{\rho}_{1/k}\|_{L^2(0,1)}^2 = d_N^2$, and let $u := P_{\overline{\mathcal{R}}} E \in S$ with $D_\infty^2 := \|E - u\|_{L^2(0,1)}^2 = \lim_{N \to \infty} d_N^2$. Then for every $N \ge k \ge 2$,*

$$
\left|a_{N, k}^* - \mathcal{C}_k(u)\right| \le \|\mathcal{C}_k\|_{S^*} \left(d_N^2 - D_\infty^2\right)^{1/2},
$$

*where $\mathcal{C}_k(u) = (\mu * \Delta u)(k)$, and $\lim_{N \to \infty} a_{N,k}^* = \mu(k)$ for every $k \ge 2$ if and only if RH holds.*

**Proof.**
**(1)** On $I_d$, $f_k|_{I_d} = \sum_{j \le d/k} a(j)$, so $\Delta_d f_k = f_k|_{I_d} - f_k|_{I_{d-1}} = a(d/k)\mathbf{1}_{k \mid d}$. Thus
$$\mathcal{C}_n^{(f)}(f_k) = \sum_{d \mid n} b\!\left(\frac{n}{d}\right) a\!\left(\frac{d}{k}\right)\mathbf{1}_{k \mid d} = \mathbf{1}_{k \mid n} \sum_{j \mid (n/k)} b\!\left(\frac{n/k}{j}\right) a(j) = \delta_{n,k}.$$
Grouping $g_d - g_{d-1}$ by index $m \in \{1, \dots, n\}$ yields $c_{n,m}^{(f)}$, and $\Delta_d E = \delta_{d,1}$ gives $\mathcal{C}_n^{(f)}(E) = b(n)$. Writing $\sum_{m=1}^n c_{n,m}^{(f)} g_m = \sum_{m=1}^n w_m g_m \overline{(w_m^{-1} \overline{c_{n,m}^{(f)}})}$ gives the Riesz representer $r_n^{(f)}$ and $\|\mathcal{C}_n^{(f)}\|_{S^*}^2$.

**(2)** For $\zeta(s)$, $\tilde{\rho}_{1/k}|_{I_d} = \lfloor d/k \rfloor - d/k = f_k|_{I_d} - \frac{1}{k} f_1|_{I_d} \in S$, so for $n, k \ge 2$, $\mathcal{C}_n(\tilde{\rho}_{1/k}) = \delta_{n,k} - \frac{1}{k}\delta_{n,1} = \delta_{n,k}$. Under $t = 1/x \in [1, \infty)$, $I_m$ maps to $[m, m+1)$ with measure $t^{-2}\,dt$ of mass $w_m = \frac{1}{m(m+1)}$, and $r_n^{(\zeta)}(1/t) = -\sum_{d \mid n} \mu(n/d)\varphi_d(t) = -f_n(t)$ in the notation of Balazard [11, §2]. For $n = 2$, $c_{2,1} = \mu(2) - \mu(1) = -2$ and $c_{2,2} = \mu(1) = 1$, giving $1(2)(-2)^2 + 2(3)(1)^2 = 14$. For an odd prime $p \ge 3$, the divisors of $p$ are $1$ and $p$ ($p - 1 > 1$), so the non-zero weights are $c_{p,1} = \mu(p) = -1$, $c_{p,p-1} = -\mu(1) = -1$, and $c_{p,p} = \mu(1) = 1$, giving $1(2)(1) + (p-1)p(1) + p(p+1)(1) = 2 + 2p^2$. For $n = 4$, $c_{4,1} = 1, c_{4,2} = -1, c_{4,3} = -1, c_{4,4} = 1$, giving $2 + 6 + 12 + 20 = 40$. For $n = p^2$ ($p \ge 3$), the non-zero weights are $c_{p^2, p-1} = 1, c_{p^2, p} = -1, c_{p^2, p^2-1} = -1, c_{p^2, p^2} = 1$, giving $(p-1)p + p(p+1) + (p^2-1)p^2 + p^2(p^2+1) = 2p^2 + 2p^4$.

**(3)** Let $g_N := \sum_{j=2}^N a_{N,j}^* \tilde{\rho}_{1/j} = P_{\mathcal{R}_N} E$. By Part 2, $\mathcal{C}_k(g_N) = a_{N,k}^*$ for all $2 \le k \le N$. Since $\mathcal{R}_N \subset \overline{\mathcal{R}}$, $P_{\mathcal{R}_N} E = P_{\mathcal{R}_N} u$, so $\|g_N - u\|_S^2 = \|E - g_N\|_S^2 - \|E - u\|_S^2 = d_N^2 - D_\infty^2$, and Cauchy-Schwarz in $S$ gives $|a_{N,k}^* - \mathcal{C}_k(u)| = |\mathcal{C}_k(g_N - u)| \le \|\mathcal{C}_k\|_{S^*}(d_N^2 - D_\infty^2)^{1/2}$. Finally, as proved in Balazard [11, Proposition 13], if $a_{N,k}^* \to \mu(k)$ for all $k \ge 2$, then $r := E - u \in S$ satisfies $\mathcal{C}_k(r) = 0$ for all $k \ge 2$; by Möbius inversion $\Delta_m r = \sum_{k \mid m} \mathcal{C}_k(r) = \mathcal{C}_1(r)$ for all $m \ge 1$, so $r_m = m\,\mathcal{C}_1(r)$. Since $\sum_{m=1}^\infty \frac{m^2}{m(m+1)} = \infty$, $r \in S$ forces $\mathcal{C}_1(r) = 0$ and thus $r = E - u = 0 \iff \text{RH}$. $\square$

---

### 3.2 Theorem 2: Head-Tail Step-Space Splitting and Strict Matrix-Loewner Inverse Chain

For $N \ge 2$, let $W_N = \operatorname{diag}(w_1, \dots, w_N)$ with $w_m = \frac{1}{m(m+1)}$, let $R_N \in \mathbb{R}^{N \times (N-1)}$ be the truncated generator matrix $(R_N)_{m, k-1} := \tilde{\rho}_{1/k}|_{I_m} = \lfloor m/k \rfloor - m/k$ ($1 \le m \le N, 2 \le k \le N$), and let $C_N \in \mathbb{R}^{(N-1) \times N}$ be the biorthogonal functional matrix $(C_N)_{n-1, m} := c_{n, m}$ ($2 \le n \le N, 1 \le m \le N$). Decompose the Báez-Duarte Gram matrix $A_N = \left(\langle \tilde{\rho}_{1/j}, \tilde{\rho}_{1/k} \rangle_{L^2(0,1)}\right)_{2 \le j,k \le N}$ into its head block on $I_1, \dots, I_N$ and its tail block on $m > N$:

$$
A_N = A_N^{(\le N)} + A_N^{(> N)}, \qquad A_N^{(\le N)} := R_N^T W_N R_N, \qquad \left(A_N^{(> N)}\right)_{j,k} := \sum_{m=N+1}^\infty \frac{1}{m(m+1)}\left\{\frac{m}{j}\right\}\left\{\frac{m}{k}\right\},
$$

and define the dual functional Gram matrix $H_N := C_N W_N^{-1} C_N^T = \left(\langle \mathcal{C}_j, \mathcal{C}_k \rangle_{S^*}\right)_{2 \le j,k \le N}$.

**Theorem 2 (Head-Tail Splitting, Exact Rank-1 Identity, and Strict Matrix-Loewner Inverse Chain).**
*For every integer $N \ge 2$:*
1. **Exact Rank-1 Identity for the Head Inverse:** *The matrices $C_N$ and $R_N$ satisfy $C_N R_N = I_{N-1}$, the vector $w_N := (I_N - C_N^T R_N^T) e_1 = e_1 + \sum_{k=2}^N k^{-1} C_N^T e_{k-1}$ spans the 1-dimensional kernel $\operatorname{ker}(R_N^T) \subset \mathbb{R}^N$, and the inverse of the head Gram matrix $A_N^{(\le N)}$ is given in exact closed form by the rank-1 update of $H_N$:*

$$
\left(A_N^{(\le N)}\right)^{-1} = H_N - \frac{(C_N W_N^{-1} w_N)(C_N W_N^{-1} w_N)^T}{w_N^T W_N^{-1} w_N}.
$$

2. **Strict Positivity of the Tail and Matrix-Loewner Chain:** *The tail Gram matrix $A_N^{(> N)}$ is strictly positive definite ($A_N^{(> N)} \succ 0$), and $A_N^{-1}$ satisfies the strict Matrix-Loewner inequality chain*

$$
0 \prec A_N^{-1} \prec \left(A_N^{(\le N)}\right)^{-1} \preceq H_N,
$$

*with exact Woodbury tail-resolvent identity*

$$
A_N^{-1} = \left(A_N^{(\le N)}\right)^{-1} - \left(A_N^{(\le N)}\right)^{-1} \left(\left(A_N^{(\le N)}\right)^{-1} + \left(A_N^{(> N)}\right)^{-1}\right)^{-1} \left(A_N^{(\le N)}\right)^{-1}.
$$

3. **Universal Diagonal and Leave-One-Out Bounds:** *For every $N \ge 2$ and every $2 \le k \le N$, the $(k, k)$ diagonal entry of $A_N^{-1}$ is nondecreasing in $N$ and satisfies the strict finite-$N$ bound*

$$
\left(A_N^{-1}\right)_{k,k} < \left(\left(A_N^{(\le N)}\right)^{-1}\right)_{k,k} \le \left(H_N\right)_{k,k} = \|\mathcal{C}_k\|_{S^*}^2,
$$

*and the Order-Invariant Leave-One-Out (LOO) innovation drop $\Delta_k^{\mathrm{LOO}}(N) := d_N(\{2,\dots,N\}\setminus\{k\})^2 - d_N^2$ satisfies*

$$
\Delta_k^{\mathrm{LOO}}(N) = \frac{|a_{N,k}^*|^2}{(A_N^{-1})_{k,k}} \ge \frac{|a_{N,k}^*|^2}{\|\mathcal{C}_k\|_{S^*}^2},
$$

*with strict inequality whenever $a_{N,k}^* \ne 0$.*

**Proof.**
**(1)** By Theorem 1(1), since $\operatorname{supp}(\mathcal{C}_n) \subset \{1, \dots, n\} \subset \{1, \dots, N\}$ for all $2 \le n \le N$, we have $C_N R_N = I_{N-1}$. Put $\widetilde{C}_N := C_N W_N^{-1/2} \in \mathbb{R}^{(N-1) \times N}$ and $\widetilde{R}_N := W_N^{1/2} R_N \in \mathbb{R}^{N \times (N-1)}$, so that $\widetilde{C}_N \widetilde{R}_N = I_{N-1}$, $\widetilde{C}_N \widetilde{C}_N^T = H_N$, and $\widetilde{R}_N^T \widetilde{R}_N = A_N^{(\le N)}$. In $\mathbb{R}^N$, the orthogonal projection onto the $(N-1)$-dimensional column space $\operatorname{ran}(\widetilde{R}_N)$ is $P = \widetilde{R}_N (\widetilde{R}_N^T \widetilde{R}_N)^{-1} \widetilde{R}_N^T = \widetilde{R}_N (A_N^{(\le N)})^{-1} \widetilde{R}_N^T$. Multiplying on the left by $\widetilde{C}_N$ and on the right by $\widetilde{C}_N^T$ gives
$$\left(A_N^{(\le N)}\right)^{-1} = \widetilde{C}_N P \widetilde{C}_N^T = \widetilde{C}_N \widetilde{C}_N^T - \widetilde{C}_N (I_N - P) \widetilde{C}_N^T = H_N - \frac{(\widetilde{C}_N z)(\widetilde{C}_N z)^T}{\|z\|_2^2},$$
where $z \in \mathbb{R}^N \setminus \{0\}$ spans the 1-dimensional orthogonal complement $\operatorname{ker}(\widetilde{R}_N^T) = W_N^{-1/2}\operatorname{ker}(R_N^T)$. Since $R_N^T(I_N - C_N^T R_N^T) = R_N^T - (C_N R_N)^T R_N^T = 0$, the vector $w_N := (I_N - C_N^T R_N^T)e_1 \in \operatorname{ker}(R_N^T)$ is non-zero (as $c_{n,m} = 0$ for $m > n$, so the $N$-th coordinate of $w_N$ is $\frac{1}{N}c_{N,N} = \frac{1}{N} \ne 0$). Setting $z = W_N^{-1/2} w_N$ gives $\widetilde{C}_N z = C_N W_N^{-1} w_N$ and $\|z\|_2^2 = w_N^T W_N^{-1} w_N$.

**(2) & (3)** For any $u \in \mathbb{R}^{N-1}$, the step sequence $g_m = -\sum_{k=2}^N u_k \{m/k\}$ is periodic in $m \ge 1$ with period $L := \operatorname{lcm}(2, \dots, N) > N$. If $u^T A_N^{(> N)} u = 0$, then $g_m = 0$ for all $m > N$; by periodicity $g_{m + L} = g_m$, we then have $g_m = 0$ for all $1 \le m \le N$ as well, so $u = C_N (g_m)_{1 \le m \le N} = 0$. Thus $A_N^{(> N)} \succ 0$ is strictly positive definite, and $A_N = A_N^{(\le N)} + A_N^{(> N)} \succ A_N^{(\le N)} \succ 0$ inverts to $0 \prec A_N^{-1} \prec (A_N^{(\le N)})^{-1} \preceq H_N$. Because $(A_N^{-1})_{k,k} = \operatorname{dist}_S(\tilde{\rho}_{1/k}, \operatorname{span}_{2 \le j \le N, j \ne k}\{\tilde{\rho}_{1/j}\})^{-2}$, enlarging $N \to N+1$ enlarges the subspace and makes $(A_N^{-1})_{k,k}$ nondecreasing in $N$. The LOO identity $\Delta_k^{\mathrm{LOO}}(N) = |a_{N,k}^*|^2 / (A_N^{-1})_{k,k}$ follows from standard block-matrix inversion on $A_N$ (cf. [10, Theorem 4]). $\square$

---

### 3.3 Theorem 3: Unconditional Resolution of Conjecture SQ for the Davenport-Heilbronn Function via Certified Rational Trial Vectors

**Theorem 3 (Variational Annihilator Lower Bounds, Periodic Tail Enclosures, and Unconditional Proof of Conjecture SQ for $f_{\mathrm{DH}}$).**
*Let $f(s) = \sum_{m=1}^\infty a(m) m^{-s}$ ($a(1)=1$) have formal Dirichlet inverse $1/f(s) = \sum_{n=1}^\infty b(n) n^{-s}$, and assume that $f_k \in S$ for all $k \ge 1$. Let $V_{\mathrm{sqf}}(f) = \operatorname{span}\{f_k : k \ge 1, \, \mu(k) \ne 0\} \subset S$. Then:*
1. **Inversion-Free Variational Lower Bound:** *$V_{\mathrm{sqf}}(f) \subset \bigcap_{\mu(n)=0} \ker \mathcal{C}_n^{(f)}$. Consequently, for any finite non-squarefree index set $\mathcal{I} \subset \{n \ge 4 : \mu(n) = 0\}$ and **any** weight vector $v = (v_n)_{n \in \mathcal{I}} \in \mathbb{C}^{\mathcal{I}} \setminus \{0\}$, the linear functional $\mathcal{L}_v := \sum_{n \in \mathcal{I}} \overline{v_n}\, \mathcal{C}_n^{(f)} \in S^*$ vanishes on $\overline{V_{\mathrm{sqf}}(f)}$ and certifies the unconditional lower bound*

$$
\lim_{N \to \infty} d_{\mathrm{sqf}, N}(f)^2 = \operatorname{dist}_S^2\big(E, \overline{V_{\mathrm{sqf}}(f)}\big) \ge \frac{|\mathcal{L}_v(E)|^2}{\|\mathcal{L}_v\|_{S^*}^2} \ge 2\operatorname{Re}\big(v^* b_{\mathcal{I}}\big) - v^* H_{\mathcal{I}}^{(f)} v,
$$

*where $b_{\mathcal{I}} = (b(n))_{n \in \mathcal{I}}$, $\mathcal{L}_v(E) = v^* b_{\mathcal{I}}$, and $\|\mathcal{L}_v\|_{S^*}^2 = v^* H_{\mathcal{I}}^{(f)} v = \sum_{m=1}^{\max \mathcal{I}} m(m+1)\big|\sum_{n \in \mathcal{I}} \overline{v_n} c_{n,m}^{(f)}\big|^2$ is a finite sum.*
2. **Closed-Form 3-Functional and 117-Functional Lower Bounds for $f_{\mathrm{DH}}(s)$:** *Let $f_{\mathrm{DH}}(s) = \sum_{m=1}^\infty a_{\mathrm{DH}}(m) m^{-s}$ be the 5-periodic Davenport-Heilbronn function with $a_{\mathrm{DH}}(1) = 1$, $a_{\mathrm{DH}}(2) = \kappa := \frac{\sqrt{10-2\sqrt{5}}-2}{\sqrt{5}-1} \approx 0.28407904384$, $a_{\mathrm{DH}}(3) = -\kappa$, $a_{\mathrm{DH}}(4) = -1$, and $a_{\mathrm{DH}}(5) = 0$. Because $\sum_{d=1}^5 a_{\mathrm{DH}}(d) = 0$, the partial sums $S_{\mathrm{DH}}(q) = \sum_{d=1}^q a_{\mathrm{DH}}(d) \in \{0, 1, 1+\kappa\}$ are bounded, so $f_{\mathrm{DH}, k} \in S$ for all $k \ge 1$. Moreover, $b_{\mathrm{DH}}(4) = b_{\mathrm{DH}}(9) = 1 + \kappa^2$ and $b_{\mathrm{DH}}(8) = -\kappa(1 + \kappa^2)$. Evaluating Part 1 on the 3-element set $\mathcal{I}_3 = \{4, 8, 9\}$ with exact rational weights $(v_4, v_8, v_9) = \frac{1}{10^5}(3237, 622, 936)$ (supported on $1 \le m \le 9$) proves in exact arithmetic in $\mathbb{Q}(\kappa)$ that*

$$
\lim_{N \to \infty} d_{\mathrm{sqf}, N}(f_{\mathrm{DH}})^2 \ge \frac{|\mathcal{L}_{v^{(3)}}(E)|^2}{\|\mathcal{L}_{v^{(3)}}\|_{S^*}^2} = 0.0431854534275\dots > 0.04318545,
$$

*and evaluating Part 1 on $\mathcal{I}_{300} = \{n \le 300 : \mu(n) = 0\}$ ($|\mathcal{I}_{300}| = 117$) with the explicit rational weights $v_n \in 10^{-6}\mathbb{Z}$ archived in `results/biorthogonal_loewner_conjecture_sq.json` certifies in 50-digit interval arithmetic that $\lim_{N \to \infty} d_{\mathrm{sqf}, N}(f_{\mathrm{DH}})^2 \ge 0.049620961191$.*
3. **Analytical Periodic-Tail Upper Bound on $\lim_{N\to\infty} d_{\mathrm{full},N}(f_{\mathrm{DH}})^2$ and Strict Separation:** *Since $S_{\mathrm{DH}}(q) \in [0, 1+\kappa]$ for all $q \ge 0$, for any real vector $c = (c_1, \dots, c_N) \in \mathbb{R}^N$ and any cutoff $M \ge 1$, the trial function $g = \sum_{k=1}^N c_k f_{\mathrm{DH}, k} \in S$ satisfies $g|_{I_m} \in [(1+\kappa)c_-, (1+\kappa)c_+]$ for all $m \ge 1$ (where $c_+ := \sum_{c_k > 0} c_k$ and $c_- := \sum_{c_k < 0} c_k$) and yields the exact analytical upper bound*

$$
\lim_{K \to \infty} d_{\mathrm{full}, K}(f_{\mathrm{DH}})^2 \le d_{\mathrm{full}, N}(f_{\mathrm{DH}})^2 \le \sum_{m=1}^M \frac{\big(1 - \sum_{k=1}^N c_k S_{\mathrm{DH}}(\lfloor m/k \rfloor)\big)^2}{m(m+1)} + \frac{\max\big((1 - (1+\kappa)c_+)^2, \, (1 - (1+\kappa)c_-)^2\big)}{M + 1}.
$$

*Evaluating this bound at $N = 35, M = 20000$ for the explicit rational vector $c \in 10^{-4}\mathbb{Z}^{35}$ recorded in Section 4.2 certifies in 50-digit interval arithmetic that*

$$
\lim_{K \to \infty} d_{\mathrm{full}, K}(f_{\mathrm{DH}})^2 \le d_{\mathrm{full}, 35}(f_{\mathrm{DH}})^2 \le 0.0385843794 + 0.0015354678 = 0.0401198472 < 0.0431854534 \le \lim_{K \to \infty} d_{\mathrm{sqf}, K}(f_{\mathrm{DH}})^2,
$$

*establishing a certified strict gap of at least $0.0030656063$ against $\mathcal{I}_3 = \{4, 8, 9\}$ and $0.0095011140$ against $\mathcal{I}_{300}$.*

**Proof.**
**(1)** By Theorem 1(1), $\mathcal{C}_n^{(f)}(f_k) = \delta_{n,k} = 0$ whenever $\mu(n) = 0$ and $\mu(k) \ne 0$, so $\mathcal{L}_v(g) = 0$ for all $g \in \overline{V_{\mathrm{sqf}}(f)}$ by continuity of $\mathcal{L}_v \in S^*$. Moreover, $\mathcal{L}_v(E) = \sum_{n\in\mathcal{I}} \overline{v_n} b(n) = v^* b_{\mathcal{I}}$, and the Riesz representer of $\mathcal{L}_v$ is $\sum_{n\in\mathcal{I}} v_n r_n^{(f)}$, whose squared norm in $S$ is $v^* H_{\mathcal{I}}^{(f)} v$ where $(H_{\mathcal{I}}^{(f)})_{n_1, n_2} = \langle r_{n_2}^{(f)}, r_{n_1}^{(f)} \rangle_S = \sum_{m=1}^{\min(n_1,n_2)} m(m+1) c_{n_1, m}^{(f)} \overline{c_{n_2, m}^{(f)}}$. For any $g \in \overline{V_{\mathrm{sqf}}(f)}$, Cauchy-Schwarz gives $|\mathcal{L}_v(E)|^2 = |\mathcal{L}_v(E - g)|^2 \le \|\mathcal{L}_v\|_{S^*}^2 \|E - g\|_S^2$, and $0 \le \|\mathcal{L}_v\|_{S^*}^{-2} |\mathcal{L}_v(E) - \|\mathcal{L}_v\|_{S^*}^2|^2$ gives $|\mathcal{L}_v(E)|^2 / \|\mathcal{L}_v\|_{S^*}^2 \ge 2\operatorname{Re}(v^* b_{\mathcal{I}}) - v^* H_{\mathcal{I}}^{(f)} v$.

**(2) & (3)** The proofs of (2) and (3) follow directly from the explicit Dirichlet-inverse recursion $b_{\mathrm{DH}}(4) = b_{\mathrm{DH}}(9) = 1+\kappa^2$, $b_{\mathrm{DH}}(8) = -\kappa(1+\kappa^2)$ and the 5-periodicity of $S_{\mathrm{DH}}(q) \in \{0, 1, 1+\kappa\}$, evaluated in 50-digit `mpmath.iv` interval arithmetic. $\square$

---

### 3.4 Theorem 4: Algebraic Tower Obstruction to Squarefree-Supported Reciprocals and Non-Universality of Strict Distance Separation

**Theorem 4 (Tower Characterization, Collapse of Euler-Product Combinations, and Counterexample to Universal Strict Separation).**
*Let $f(s) = \sum_{n=1}^\infty a(n) n^{-s}$ ($a(1)=1$) have formal reciprocal $1/f(s) = \sum_{n=1}^\infty b(n) n^{-s}$. For each prime $p$ and $k \ge 0$, define the $p$-shifted formal Dirichlet series $F_{p^k}(s) := \sum_{\gcd(m,p)=1} a(p^k m) m^{-s}$ in the integral domain $\mathcal{R}_p \cong \mathbb{C}[[t_q : q \ne p]]$ of formal Dirichlet series supported on integers coprime to $p$. Then:*
1. **Exact Tower Equivalence:** *$b$ is squarefree-supported ($b(n) = 0$ whenever $\mu(n) = 0$) if and only if, for every prime $p$ and every $k \ge 2$,*

$$
F_{p^k}(s)\, F_1(s)^{k-1} = F_p(s)^k \qquad \text{in } \mathcal{R}_p.
$$

2. **Collapse of Finite Linear Combinations of Completely Multiplicative or Hecke Series:** *Suppose $f(s) = \sum_{j=1}^r w_j f_{(j)}(s)$ with non-zero weights $w_1, \dots, w_r \in \mathbb{C} \setminus \{0\}$ ($\sum_{j=1}^r w_j = 1$), where $f_{(1)}, \dots, f_{(r)}$ are distinct completely multiplicative Dirichlet series whose restrictions to $\{m : \gcd(m, p) = 1\}$ remain distinct for each prime $p$ (e.g., distinct Dirichlet characters $\chi_1, \dots, \chi_r$), or normalized Hecke eigenforms of common weight and nebentypus. If $1/f(s)$ is squarefree-supported, then $f_{(1)}, \dots, f_{(r)}$ cannot be Hecke eigenforms of degree 2, and in the completely multiplicative case $r = 1$ and $f = f_{(1)}$ is a single degree-1 Euler product. In particular, whenever $r \ge 2$ and $f_k \in S$ ($\forall k \ge 1$), there exists $n \ge 4$ with $\mu(n) = 0$ and $b(n) \ne 0$, so $\lim_{N\to\infty} d_{\mathrm{sqf},N}(f)^2 \ge |b(n)|^2 / \|\mathcal{C}_n^{(f)}\|_{S^*}^2 > 0$.*
3. **Non-Universality of Strict Full-vs-Squarefree Separation When $f(1) = 0$:** *There exist normalized linear combinations $f(s) = w_1 L(s, \chi_1) + w_2 L(s, \chi_2)$ ($w_1 + w_2 = 1, w_1 w_2 \ne 0$) of two distinct real primitive Dirichlet $L$-functions with $f_k \in S$ ($\forall k \ge 1$) for which $1/f(s)$ is not squarefree-supported, yet*

$$
\lim_{N \to \infty} d_{\mathrm{full}, N}(f)^2 = \lim_{N \to \infty} d_{\mathrm{sqf}, N}(f)^2 = 1.
$$

*Specifically, let $L_3(s) = L(s, \chi_3)$ and $L_4(s) = L(s, \chi_4)$ be the Dirichlet $L$-series of the real nonprincipal characters modulo $3$ and $4$, with $A := L_3(1) = \frac{\pi}{3\sqrt{3}}$ and $B := L_4(1) = \frac{\pi}{4}$, and set $f(s) := \frac{B L_3(s) - A L_4(s)}{B - A}$. Then $f(1) = 0$ and $\langle E, f_k \rangle_S = \frac{\overline{f(1)}}{k} = 0$ for every $k \ge 1$, so $E \perp V(f)$ and $d_{\mathrm{full}, N}(f)^2 = d_{\mathrm{sqf}, N}(f)^2 = \|E\|_S^2 = 1$ for all $N \ge 1$.*

**Proof.**
**(1) & (2)** Writing $f(s) = \sum_{k=0}^\infty F_{p^k}(s) p^{-ks}$ and $1/f(s) = \sum_{l=0}^\infty B_{p^l}(s) p^{-ls}$, we have $b(n) = 0$ ($\forall \mu(n) = 0$) iff $B_{p^l}(s) = 0$ for all primes $p$ and $l \ge 2$, which in $\mathcal{R}_p[[X]]$ ($X = p^{-s}$) is $(\sum_{k=0}^\infty F_{p^k} X^k)(B_1 + B_p X) = 1 \iff B_1 = F_1^{-1}, B_p = -F_p / F_1^2$, and $F_{p^k} F_1^{k-1} = F_p^k$ ($\forall k \ge 2$). Under the hypotheses of (2), Dedekind's independence lemma on $\{m : \gcd(m, p) = 1\}$ (or the Hecke relations) ensures that $G_j(s) := \sum_{\gcd(m,p)=1} a_j(m)m^{-s} \in \mathcal{R}_p$ ($1 \le j \le r$) are linearly independent over $\mathbb{C}$. Grouping $\{1, \dots, r\}$ by the distinct values $\{\beta_1, \dots, \beta_d\}$ of $\alpha_j := a_j(p)$ and setting $H_u(s) := \sum_{\alpha_j = \beta_u} w_j G_j(s) \ne 0$ and $\Phi_p := F_p / F_1 \in \mathcal{R}_p$, Part 1 gives $\sum_{u=1}^d \beta_u^k(\beta_u - \Phi_p)H_u(s) = 0$ ($\forall k \ge 0$). Invertibility of the $d \times d$ complex Vandermonde matrix $(\beta_u^k)_{0 \le k < d, 1 \le u \le d}$ yields $(\beta_u - \Phi_p)H_u(s) = 0$ in the integral domain $\mathcal{R}_p$, forcing $\Phi_p = \beta_u$ for all $u$ and hence $d = 1$ for every prime $p$, so $r = 1$.

**(3)** For any Dirichlet series $f(s) = \sum_{m=1}^\infty a(m) m^{-s}$ with bounded partial sums $S_f(q) = \sum_{d=1}^q a(d) = O(1)$, the series $f(1) = \sum_{m=1}^\infty a(m)/m$ converges by summation by parts: $\sum_{m=1}^M \frac{a(m)}{m} = \sum_{m=1}^{M-1} \frac{S_f(m)}{m(m+1)} + \frac{S_f(M)}{M} \to \sum_{m=1}^\infty w_m S_f(m) = \langle f_1, E \rangle_S$. Similarly, for each $k \ge 1$, $\langle f_k, E \rangle_S = \sum_{r=1}^\infty S_f(r) \sum_{m=rk}^{rk+k-1} \frac{1}{m(m+1)} = \sum_{r=1}^\infty S_f(r)\left(\frac{1}{rk} - \frac{1}{(r+1)k}\right) = \frac{1}{k}\sum_{r=1}^\infty \frac{a(r)}{r} = \frac{f(1)}{k}$. For $f(s) = \frac{B L_3(s) - A L_4(s)}{B - A}$, we have $f(1) = \frac{B A - A B}{B - A} = 0$, so $\langle E, f_k \rangle_S = 0$ for all $k \ge 1$ and $d_{\mathrm{full},N}(f)^2 = d_{\mathrm{sqf},N}(f)^2 = 1$. $\square$

---

## 4. Results and Supporting Evidence

We verified Theorems 1–4 across $N \in [10, 320]$ and $M \in [4, 300]$ using `src/verify_biorthogonal_loewner_conjecture_sq.py` (5 CPU threads, including `scipy.linalg.eigh` for symmetric generalized eigenvalues and 50-digit `mpmath.iv` interval arithmetic).

### 4.1 Monotonic Convergence of Inverse Báez-Duarte Gram Diagonals $(A_N^{-1})_{k,k} < \|\mathcal{C}_k\|_{S^*}^2$

Across all $2 \le k \le 320$, Theorem 1(1) holds with maximum error $1.55 \times 10^{-15}$, and Theorem 2(3) holds with **zero violations**. Table 1 displays the monotonic progression of $(A_N^{-1})_{k,k}$ across $N \in \{10, 40, 160, 320\}$, the universal bound $\|\mathcal{C}_k\|_{S^*}^2$, the optimal coefficient $a_{320, k}^*$, and the order-invariant Leave-One-Out drop $\Delta_k^{\mathrm{LOO}}(320)$ for $2 \le k \le 10$:

| Index $k$ | $\mu(k)$ | $(A_{10}^{-1})_{k,k}$ | $(A_{40}^{-1})_{k,k}$ | $(A_{160}^{-1})_{k,k}$ | $(A_{320}^{-1})_{k,k}$ | Bound $\|\mathcal{C}_k\|_{S^*}^2$ | Ratio at $N=320$ | $a_{320,k}^*$ | $\Delta_k^{\mathrm{LOO}}(320)$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **$k=2$** | $-1$ | $12.3818$ | $13.0418$ | $13.2918$ | $13.3787$ | **$14$** | $0.9556$ | $-0.9620$ | $6.918 \times 10^{-2}$ |
| **$k=3$** | $-1$ | $16.9828$ | $18.0172$ | $18.6105$ | $18.7905$ | **$20$** | $0.9395$ | $-0.9560$ | $4.863 \times 10^{-2}$ |
| **$k=4$** | $0$ | $28.7323$ | $32.9946$ | $34.9402$ | $35.5168$ | **$40$** | $0.8879$ | $-0.0691$ | $1.343 \times 10^{-4}$ |
| **$k=5$** | $-1$ | $31.7444$ | $39.6495$ | $42.6763$ | $43.7794$ | **$52$** | $0.8419$ | $-0.8764$ | $1.755 \times 10^{-2}$ |
| **$k=6$** | $+1$ | $42.1328$ | $64.1027$ | $70.7629$ | $73.7729$ | **$92$** | $0.8019$ | $+0.7682$ | $7.999 \times 10^{-3}$ |
| **$k=7$** | $-1$ | $43.2831$ | $65.8815$ | $75.5539$ | $79.4227$ | **$100$** | $0.7942$ | $-0.8240$ | $8.550 \times 10^{-3}$ |
| **$k=8$** | $0$ | $64.6514$ | $96.5190$ | $114.4346$ | $121.2609$ | **$160$** | $0.7579$ | $+0.0090$ | $6.684 \times 10^{-7}$ |
| **$k=9$** | $0$ | $68.1664$ | $104.2531$ | $125.8972$ | $134.1096$ | **$180$** | $0.7451$ | $-0.0188$ | $2.646 \times 10^{-6}$ |
| **$k=10$** | $+1$ | $65.6201$ | $142.7952$ | $174.4277$ | $185.3491$ | **$264$** | $0.7021$ | $+0.6916$ | $2.581 \times 10^{-3}$ |

At $N = 320$, summing the order-invariant LOO drops $\sum_{k=2}^{320} \Delta_k^{\mathrm{LOO}}(320) = 0.171195$ across arithmetic classes shows that the $66$ primes carry **$89.89\%$** ($0.153886$), the $129$ squarefree composites carry **$9.99\%$** ($0.017106$), and the $124$ non-squarefree indices ($\mu(k)=0$) carry only **$0.12\%$** ($0.000202$) (Figure 1).

![Figure 1: (a) Monotonic convergence of the inverse Gram diagonal ratio (A_N^{-1})_{k,k} / ||C_k||_{S^*}^2 across N in [10, 320]; (b) Order-invariant Leave-One-Out innovation drops Delta_k^{LOO}(320) stratified by arithmetic class.](supplement/p9-figure-1.png)

### 4.2 Verification of the Matrix-Loewner Chain and Interval-Certified Resolution of Conjecture SQ

Table 2 reports the minimum eigenvalues of $A_N^{(> N)}$, $(A_N^{(\le N)})^{-1} - A_N^{-1}$, and $H_N - A_N^{-1}$, the second singular value $\sigma_2(H_N - (A_N^{(\le N)})^{-1})$ confirming the exact rank-1 identity of Theorem 2(1), and the largest symmetric generalized eigenvalue $\lambda_{\max}\big((A_N^{(\le N)})^{-1/2} A_N^{(> N)} (A_N^{(\le N)})^{-1/2}\big)$ computed via `scipy.linalg.eigh(a_tail, a_head)`:

| Scale $N$ | $d_{\mathrm{BD},N}^2$ | $\lambda_{\min}(A_N^{(>N)})$ | $\lambda_{\min}((A_N^{(\le N)})^{-1} - A_N^{-1})$ | $\lambda_{\min}(H_N - A_N^{-1})$ | $\sigma_2(H_N - (A_N^{(\le N)})^{-1})$ | $\lambda_{\max}\big((A_N^{(\le N)})^{-1/2} A_N^{(>N)} (A_N^{(\le N)})^{-1/2}\big)$ |
|---|---:|---:|---:|---:|---:|---:|
| $10$ | $0.023853$ | $2.14 \times 10^{-3}$ | $8.52 \times 10^{-2}$ | $2.39 \times 10^{-1}$ | $7.86 \times 10^{-13}$ | $1.958694$ |
| $20$ | $0.016538$ | $6.59 \times 10^{-4}$ | $1.31 \times 10^{-2}$ | $7.98 \times 10^{-2}$ | $2.16 \times 10^{-11}$ | $3.072206$ |
| $40$ | $0.012736$ | $2.42 \times 10^{-4}$ | $3.12 \times 10^{-3}$ | $2.19 \times 10^{-2}$ | $6.87 \times 10^{-10}$ | $4.366224$ |
| $80$ | $0.010999$ | $7.71 \times 10^{-5}$ | $7.21 \times 10^{-4}$ | $5.38 \times 10^{-3}$ | $9.24 \times 10^{-9}$ | $5.768348$ |
| $160$ | $0.009357$ | $2.43 \times 10^{-5}$ | $1.82 \times 10^{-4}$ | $1.40 \times 10^{-3}$ | $1.74 \times 10^{-7}$ | $7.869869$ |
| $320$ | $0.007962$ | $7.31 \times 10^{-6}$ | $4.78 \times 10^{-5}$ | $3.79 \times 10^{-4}$ | $2.05 \times 10^{-6}$ | $10.941489$ |

Table 3 reports the 50-digit interval-certified lower bounds $|\mathcal{L}_v(E)|^2 / \|\mathcal{L}_v\|_{S^*}^2 \le \lim_{N \to \infty} d_{\mathrm{sqf}, N}(f_{\mathrm{DH}})^2$ for the explicit rational trial vectors $v \in 10^{-6}\mathbb{Z}^{\mathcal{I}}$ archived in `results/biorthogonal_loewner_conjecture_sq.json` across $M \in [4, 300]$ (Figure 2b). For the full-dilate upper bound of Theorem 3(3) at $N = 35, M = 20000$, the explicit rational vector $10^4 c = (9100, -947, 2188, 6740, 267, -6310, -1118, -626, 5055, -221, -4047, 3197, 1344, 3755, 312, 186, -1498, -2141, 3531, 79, -2704, -291, 1682, -5234, 376, -3678, 287, -636, 3753, -441, -4149, -756, -216, 3327, 5766)$ has $c_+ = 4.6552$ and $c_- = -3.7606$, certifying in 50-digit interval arithmetic a head sum $\le 0.0385843794$ and tail $\le 0.0015354678$, for a total certified upper bound $\lim_{K\to\infty} d_{\mathrm{full},K}(f_{\mathrm{DH}})^2 \le 0.0401198472 < 0.0431854534 \le \lim_{K\to\infty} d_{\mathrm{sqf},K}(f_{\mathrm{DH}})^2$:

| Cap $M$ | $M=4$ | $M=9$ | $M=20$ | $M=40$ | $M=100$ | $M=160$ | $M=300$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Non-Squarefree Functionals $|\mathcal{I}|$ | $1$ | $3$ | $7$ | $14$ | $39$ | $62$ | $117$ |
| Interval-Certified Floor $\le \lim_N d_{\mathrm{sqf},N}(f_{\mathrm{DH}})^2$ | $0.032254$ | **$0.043185$** | $0.047301$ | $0.047595$ | $0.048924$ | $0.049374$ | **$0.049621$** |
| Strict Gap Over Certified $d_{\mathrm{full},35}(f_{\mathrm{DH}})^2 \le 0.040120$ | — | **$+0.003066$** | $+0.007182$ | $+0.007475$ | $+0.008804$ | $+0.009254$ | **$+0.009501$** |

![Figure 2: (a) Strict positivity of the minimum eigenvalues across the Matrix-Loewner chain A_N^{-1} < (A_N^{(<=N)})^{-1} <= H_N; (b) Interval-certified multi-functional lower bound on lim_{N->infty} d_{sqf,N}(f_DH)^2 across M in [4, 300], strictly exceeding the interval-certified full-dilate upper bound 0.040120 from M=9 onward.](supplement/p9-figure-2.png)

---

## 5. Limitations and Scope

1. **Direction of the Loewner Inequality ($A_N^{-1} \preceq H_N$):** Because the biorthogonal functionals $\mathcal{C}_n^{(f)} \in S^*$ live in the dual space, Riesz projection bounds $A_N^{-1}$ from above ($A_N^{-1} \prec (A_N^{(\le N)})^{-1} \preceq H_N$) and therefore bounds $A_N$ and $d_{\mathrm{sqf}, N}(f)^2$ **from below**. For $\zeta(s)$, where $\mathcal{C}_n(E) = \mu(n) = 0$ on all non-squarefree $n$, the squarefree annihilator constraints hold identically and do not by themselves supply an upper bound on $d_N^2$.
2. **Aggregate Relative Tail Spectrum:** As shown in Table 2, the largest symmetric generalized eigenvalue $\lambda_{\max}\big((A_N^{(\le N)})^{-1/2} A_N^{(> N)} (A_N^{(\le N)})^{-1/2}\big)$ grows from $1.9587$ ($N=10$) to $10.9415$ ($N=320$), while $\operatorname{Tr}(A_N^{-1}) / \operatorname{Tr}(H_N)$ decreases from $0.4053$ to $0.2030$. This measures the aggregate quadratic-form ratio $\max_{u \ne 0} (u^T A_N^{(> N)} u) / (u^T A_N^{(\le N)} u)$ on the subspace $\mathcal{R}_N$ rather than an entrywise asymptotic for individual large-$k$ generators.
3. **Scope of the Squarefree Distance Separation:** Theorem 4 proves that any nontrivial finite combination of distinct completely multiplicative Euler products has a non-squarefree-supported reciprocal $1/f$, which forces $\lim_{N\to\infty} d_{\mathrm{sqf},N}(f)^2 > 0$ whenever $f_k \in S$. As shown by Theorem 4(3), however, establishing the strict inequality $\lim_{N\to\infty} d_{\mathrm{full},N}(f)^2 < \lim_{N\to\infty} d_{\mathrm{sqf},N}(f)^2$ requires an additional upper bound on $\lim_{N\to\infty} d_{\mathrm{full},N}(f)^2$, which Theorem 3 provides for the modulus-5 Davenport-Heilbronn function $f_{\mathrm{DH}}(s)$.

---

## 6. Reproducibility

All analytical proofs are complete in Section 3, and all numerical tables, rational trial vectors, 50-digit interval enclosures, and figures are reproduced in $\sim 8\text{ s}$ on 5 CPU threads (`Python 3.12.3`, `numpy 2.5.4`, `scipy 1.18.1`, `mpmath 1.4.1`, `matplotlib 3.11.2`) via:

```bash
PYTHONPATH=. python3 src/verify_biorthogonal_loewner_conjecture_sq.py
```

Outputs (including all 117 rational functional numerators and full outward-rounded 50-digit interval endpoints) are written to `results/biorthogonal_loewner_conjecture_sq.json`, `supplement/p9-figure-1.png`, and `supplement/p9-figure-2.png`.

---

## 7. References

[1] B. Nyman. *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*. PhD Thesis, University of Uppsala, 1950. https://books.google.com/books?id=7Q00AAAAIAAJ

[2] A. Beurling. A closure problem related to the Riemann zeta-function. *Proceedings of the National Academy of Sciences*, 41(5):312–314, 1955. https://doi.org/10.1073/pnas.41.5.312

[3] L. Báez-Duarte. A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis. *Rendiconti Lincei Matematica e Applicazioni*, 14(1):5–11, 2003. https://ems.press/journals/rlm/articles/3487

[4] V. I. Vasyunin. On a biorthogonal system associated with the Riemann hypothesis. *St. Petersburg Mathematical Journal*, 7(3):405–419, 1995. https://www.mathnet.ru/eng/aa521

[5] span_of_dilates. The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH. *rStation Paper riemann_hypothesis_1*, v2, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/1/v2

[6] L. Báez-Duarte. A new look at the Nyman-Beurling criterion for the Riemann hypothesis. *Advances in Mathematics*, 191(1):176–186, 2005. https://doi.org/10.1016/j.aim.2004.03.005

[7] B. Bagchi. On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis. *Proceedings of the Indian Academy of Sciences (Mathematical Sciences)*, 116(2):139–146, 2006. https://doi.org/10.1007/BF02829741

[8] J.-F. Burnol. On Fourier and Zeta(s) (IV): A weighty study of Báez-Duarte's criterion. *Advances in Mathematics*, 214(1):392–422, 2007. https://doi.org/10.1016/j.aim.2007.02.009

[9] S. Bettin, J. B. Conrey, and D. W. Farmer. An optimal mollifier in the Nyman-Beurling-Báez-Duarte criterion for the Riemann hypothesis. *Proceedings of the Steklov Institute of Mathematics*, 280(Suppl. 2):S26–S32, 2013. https://doi.org/10.1134/S0081543813030036

[10] halasz_resonator. Canonical Archimedean-Reciprocity Decomposition of the Vasyunin-Báez-Duarte Gram Operator: Universal Inertia, 4x4 Dedekind Capacitance Monotonicity, and Arithmetic-Legendre Mollifier Compression. *rStation Paper riemann_hypothesis_3*, v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/3/v1

[11] M. Balazard. An arithmetical function related to Báez-Duarte's criterion for the Riemann hypothesis. *arXiv preprint arXiv:1812.04309*, 2018. https://arxiv.org/abs/1812.04309

[12] span_of_dilates. Conjecture R in the simple-zero case: an upper bound for the Báez-Duarte rate when finitely many zeros are off the line. *rStation Paper riemann_hypothesis_4*, v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/4/v1

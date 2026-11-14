# Multi-Layer Wold Filtrations, General-$Q$ Jordan Totient Sieves, and the Finite-Horizon Phase Transition in the Báez-Duarte Step Space

## Abstract

In rStation Paper 153 [1], orthogonal projection of the Báez-Duarte approximation problem onto the single dyadic wandering layer $\mathcal{W}_2^{\mathcal{S}} = \mathcal{S} \ominus V_2(\mathcal{S})$ reduced the squared distance $d_N^2(\mathcal{W}_2^{\mathcal{S}})$ to an exact odd squarefree Jordan totient tail decaying unconditionally as $\Theta(N^{-1})$. By contrast, in the full step space $\mathcal{S} = \bigoplus_{j=0}^{\infty} V_q^j \mathcal{W}_q^{\mathcal{S}}$, the global Báez-Duarte distance $d_N^2(\mathcal{S})$ satisfies $\lim_{N\to\infty} d_N(\mathcal{S}) = 0$ if and only if the Riemann Hypothesis (RH) holds [4], and cannot decay faster than $(\log N)^{-1}$ unconditionally [9, 2]. How fixed-layer $O(N^{-1})$ polynomial decay transitions across $J$-layer Wold truncations $\mathcal{H}_{J,q} = \bigoplus_{j=0}^{J-1} V_q^j \mathcal{W}_q^{\mathcal{S}}$ into the global $(\log N)^{-1}$ barrier remained open.

We resolve this finite-horizon bridge unconditionally across arbitrary prime and composite dilations $Q \ge 2$:

1. **Wold collapse, range intersection, and horizon unlocking (Theorem 1):** Every $J$-layer truncation collapses to a single composite wandering subspace $\mathcal{H}_{J,q} = \mathcal{W}_{q^J}^{\mathcal{S}}$. For all $N, Q \ge 2$, $\widetilde{\mathcal{V}}_N \cap V_Q(\mathcal{S}) = \mathcal{V}_N \cap V_Q(\mathcal{S}) = V_Q(\mathcal{V}_{\lfloor N/Q\rfloor})$, yielding exact step plateaus $d_{kQ}^2(\mathcal{W}_Q^{\mathcal{S}}) = d_{kQ-1}^2(\mathcal{W}_Q^{\mathcal{S}})$ ($k \ge 2$), a sharp norm jump $\|V_Q^*|_{\widetilde{\mathcal{V}}_N}\| = 1$ for $Q \le \lfloor N/2\rfloor$ versus $< 1$ for $Q > N/2$, sub-horizon unlocking of the pole-cancellation constraint $\sum_{d=1}^N a_d/d = 0$ precisely when $Q \le N$, and a closed-form cosecant norm formula for $d \ge Q - 1$ ($Q \nmid d$).
2. **Discrete Dirichlet duality and general-$Q$ Jordan totient sieves (Theorem 2):** Dualizing the $(Q-1)\times(Q-1)$ Kac–Murdock–Szegő block form and proving a universal composite-$Q$ Ramanujan $L(2)$ Euler-product identity yields explicit two-sided Jordan totient sieve bounds for every $Q \ge 2$, proving $d_N^2(\mathcal{W}_Q^{\mathcal{S}}) = \Theta_Q(N^{-1})$ with closed-form constants $\mathcal{C}_Q$ and uniform vanishing $d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) < \frac{Q(N)^2}{4N} \to 0$ whenever $Q(N) = o(N^{1/2})$.
3. **Inverse large sieve and super-horizon RH equivalence (Theorem 3):** A quartic Fejér–Schur inverse large sieve on $\widetilde{\mathcal{V}}_N$ bounds $\|V_Q^* f\|_{\mathcal{S}}^2 \le \kappa_{\mathrm{FS}}(N) N^2\bigl(\frac{1}{Q} + \frac{\pi^2 N^3}{8 Q^3}\bigr)\|f\|_{\mathcal{S}}^2$ ($\kappa_{\mathrm{FS}}(N) < 14$). At $Q(N) = \lceil 29 N^2\rceil$ ($J_{\mathrm{RH}}(N) = \lceil 2\log_q N + \log_q 29\rceil$), $\lim_{N\to\infty} d_N(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = 0$ is equivalent to RH, while whenever $Q(N)/N^2 \to \infty$ the unconditional Burnol lower bound $\liminf_{N\to\infty} d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}})\log N \ge 2 + \gamma - \log(4\pi)$ transfers intact. These results resolve the multi-layer Wold geometry of $\mathcal{S}$ without constraining the zeros of $\zeta(s)$.

---

## 1. Introduction, Step-Space Wold Setup, and Summary of Main Results

### 1.1. Motivation: Bridging Fixed-Layer $O(1/N)$ Sieves and Global $O(1/\log N)$ Geometry

By the Nyman–Beurling–Báez-Duarte (NBBD) criterion [3, 4, 5], the Riemann Hypothesis (RH) holds if and only if the indicator $E := \mathbf{1}_{(0,1]}$ lies in the $L^2(0,\infty)$-closure of the finite-horizon Báez-Duarte subspaces $\mathcal{V}_N := \operatorname{span}\{G_2, \dots, G_N\}$, where $G_n(x) := \frac{1}{n}\left\{\frac{1}{x}\right\} - \left\{\frac{1}{nx}\right\}$ vanishes identically on $(1,\infty)$ and takes the constant value $\lfloor m/n\rfloor - \frac{m}{n} = -\{m/n\}$ on each unit-reciprocal step interval $I_m := \bigl(\frac{1}{m+1}, \frac{1}{m}\bigr]$ ($m \ge 1$). Writing
$$
d_N^2(\mathcal{S}) := \inf_{g \in \mathcal{V}_N} \|E - g\|_{\mathcal{S}}^2 = \min_{c_2,\dots,c_N \in \mathbb{C}} \left\|E - \sum_{n=2}^{N} c_n G_n\right\|_{\mathcal{S}}^2
\tag{1.1}
$$
inside the closed step subspace $\mathcal{S} \subset L^2(0,1)$, the global approximation problem is governed by the critical-strip zeros of $\zeta(s)$: if RH fails ($Z^+ := \{\rho : \zeta(\rho)=0,\; \operatorname{Re}\rho > 1/2\} \ne \emptyset$), then $\lim_{N\to\infty} d_N^2(\mathcal{S}) = \mathcal{D}_\infty^2 > 0$ [4, 5, 10, 2]; even if RH holds, Burnol's lower bound [9] and the isometric transfer from $\mathcal{V}_N$ to the continuous Beurling family at dilation cutoff $1/N$ [4, 2] force $d_N^2(\mathcal{S}) \ge (B_{\mathrm{NB}} + o(1))/\log N$ as $N \to \infty$, with Hadamard constant $B_{\mathrm{NB}} := 2 + \gamma - \log(4\pi) \approx 0.0461914$ (matched asymptotically when all critical-line zeros are simple by Bettin, Conrey, and Farmer [8]; cf. Bagchi [6] and BBLS [7]).

On the other hand, for each integer $q \ge 2$, the rescaled floor-dilation operator $(V_q f)(x) := q^{1/2} f(qx)$ restricts to a pure shift isometry of infinite multiplicity on $\mathcal{S}$ [13, 14, 2, 1], inducing the orthogonal Wold decomposition
$$
\mathcal{S} = \bigoplus_{j=0}^{\infty} V_q^j \mathcal{W}_q^{\mathcal{S}}, \qquad \mathcal{W}_q^{\mathcal{S}} := \mathcal{S} \ominus V_q(\mathcal{S}) = \ker(V_q^*),
\tag{1.2}
$$
and the $J$-layer finite-horizon Wold filtration
$$
\mathcal{H}_{J,q} := \bigoplus_{j=0}^{J-1} V_q^j \mathcal{W}_q^{\mathcal{S}} \subset \mathcal{S} \qquad (J \ge 1), \qquad
d_N^2(\mathcal{H}_{J,q}) := \inf_{g \in \mathcal{V}_N} \bigl\|P_{\mathcal{H}_{J,q}}(E - g)\bigr\|_{\mathcal{S}}^2.
\tag{1.3}
$$
Recently, our previous work rStation Paper 153 ([1], Theorem 4) proved unconditionally that on the single dyadic wandering layer $\mathcal{H}_{1,2} = \mathcal{W}_2^{\mathcal{S}}$ ($q = 2, J = 1$), the projected squared distance collapses to the exact odd squarefree Jordan totient tail
$$
d_N^2(\mathcal{W}_2^{\mathcal{S}}) = \frac{4}{\pi^2}\sum_{\substack{\ell > N \\ 2 \nmid \ell}} \frac{\mu(\ell)^2}{J_2(\ell)} = \frac{2 C_{\mathrm{odd}}}{\pi^2 N} + O(N^{-3/2}) \qquad (N \ge 2),
\tag{1.4}
$$
where $J_2(\ell) := \ell^2 \prod_{p \mid \ell}(1 - p^{-2})$ is Jordan's second totient function. Thus a single Wold layer loses the $(\log N)^{-1}$ barrier completely and decays polynomially as $\Theta(N^{-1})$ **independently of RH**.

This sharp dichotomy left three concrete structural questions open at the interface of Papers [1] and [2]:
1. **Multi-layer and general-$Q$ sieves:** How does $d_N^2(\mathcal{H}_{J,q})$ behave for $J \ge 2$ and for arbitrary prime or composite dilations $Q \ge 3$, where the $(Q-1)\times(Q-1)$ block covariance matrix ceases to be a scalar? Does unconditional $\Theta_Q(N^{-1})$ polynomial decay persist for every fixed $Q$ and every fixed depth $J$, and up to what growing horizon $Q = Q(N)$ is unconditional vanishing $d_N(\mathcal{W}_{Q(N)}^{\mathcal{S}}) \to 0$ guaranteed?
2. **Algebraic mechanism of the horizon phase transition:** What structural change occurs inside the projected subspace $P_{\mathcal{W}_Q}(\mathcal{V}_N)$ as the dilation horizon $Q$ crosses $N/2$ and $N$, switching off the unconditional $O(N^{-1})$ sieve?
3. **Finite-horizon recovery of RH and the $(\log N)^{-1}$ barrier:** Does there exist an explicit finite layer schedule $J = J_{\mathrm{RH}}(N)$ (equivalently $Q = q^{J_{\mathrm{RH}}(N)}$) for which $\lim_{N\to\infty} d_N(\mathcal{H}_{J_{\mathrm{RH}}(N), q}) = 0$ is **equivalent to RH** and unconditionally inherits Burnol's $(\log N)^{-1}$ lower bound?

In this paper we resolve all three questions unconditionally.

---

### 1.2. Step-Space Hilbert Geometry, Dilation Semigroup, and Step-Jump Coordinates

We retain the step-space conventions of [1, §1.1] and [2, §1–2]. Every $f \in \mathcal{S}$ is constant on each interval $I_m = \bigl(\frac{1}{m+1}, \frac{1}{m}\bigr]$ ($m \ge 1$) of length $w_m := \frac{1}{m(m+1)}$, with sequence coordinates $f(m) := f|_{I_m}$ satisfying
$$
\langle f, g\rangle_{\mathcal{S}} = \sum_{m=1}^{\infty} w_m f(m)\overline{g(m)}, \qquad
E(m) = 1, \qquad
G_n(m) = -\left\{\frac{m}{n}\right\} \quad (n \ge 2,\; m \ge 1).
\tag{1.5}
$$
Extending $f(0) := 0$, define the discrete backward step-jump $(\nabla f)(m) := f(m) - f(m-1)$ ($m \ge 1$). Since $-\{m/n\} + \{(m-1)/n\} = \mathbf{1}_{n \mid m} - \frac{1}{n}$ for all $m \ge 1$ and $n \ge 2$,
$$
(\nabla E)(m) = \mathbf{1}_{m=1}, \qquad
(\nabla G_n)(m) = \mathbf{1}_{n \mid m} - \frac{1}{n} \quad (m \ge 1).
\tag{1.6}
$$
Let $\widetilde{\mathcal{V}}_N := \operatorname{span}\{E, G_2, \dots, G_N\} = \mathbb{C} E \oplus \mathcal{V}_N$ ($\dim \widetilde{\mathcal{V}}_N = N$). Every $f = a_1 E + \sum_{d=2}^N a_d G_d \in \widetilde{\mathcal{V}}_N$ has Mellin transform
$$
\widehat{f}(s) := \int_0^1 f(x) x^{s-1}\,dx = \frac{a_1}{s} + \frac{\zeta(s)}{s}\sum_{d=2}^{N} a_d\bigl(d^{-s} - d^{-1}\bigr) \qquad (\operatorname{Re} s > 1/2),
\tag{1.7}
$$
whose residue at $s = 1$ cancels automatically because $G_d(x) = \frac{1}{d}\rho_1(x) - \rho_{1/d}(x)$ ($\rho_\theta(x) := \{\theta/x\}$) incorporates Nyman's pole-cancellation condition. In step-jump coordinates,
$$
(\nabla f)(m) = a_1 \mathbf{1}_{m=1} - \left(\sum_{d=2}^{N} \frac{a_d}{d}\right) + \sum_{\substack{2 \le d \le N \\ d \mid m}} a_d \qquad (m \ge 1).
\tag{1.8}
$$
Thus for a Báez-Duarte residual $f = E - \sum_{d=2}^N c_d G_d$ ($a_1 = 1$, $a_d = -c_d$), the constant background shift $\sum_{d=2}^N c_d/d$ in $(\nabla f)(m)$ is **globally locked** to the divisor weights $(-c_d)_{2 \le d \le N}$ by the pole-cancellation condition at $s = 1$.

For every integer $Q \ge 2$ (prime or composite), the floor-dilation isometry $V_Q : \mathcal{S} \to \mathcal{S}$ and its Hilbert-space adjoint $V_Q^* : \mathcal{S} \to \mathcal{S}$ act in sequence coordinates by ([1], Lemma 2.1):
$$
(V_Q f)(m) = \begin{cases} 0, & 1 \le m < Q, \\ Q^{1/2} f\bigl(\lfloor m/Q\rfloor\bigr), & m \ge Q, \end{cases}
\qquad
(V_Q^* g)(k) = Q^{1/2}\, w_k^{-1} \sum_{r=0}^{Q-1} w_{Qk+r}\, g(Qk+r) \quad (k \ge 1),
\tag{1.9}
$$
since $\sum_{r=0}^{Q-1} w_{Qk+r} = \frac{1}{Qk} - \frac{1}{Q(k+1)} = \frac{w_k}{Q}$. Hence $V_Q(\mathcal{S})$ consists of all step sequences vanishing on $B_0^{(Q)} := \{1, \dots, Q-1\}$ and constant on every $Q$-adic residue block $B_k^{(Q)} := \{Qk, Qk+1, \dots, Qk+Q-1\}$ ($k \ge 1$), while $P_{\mathcal{W}_Q} := I - V_Q V_Q^*$ subtracts the $w$-weighted block average on each $B_k^{(Q)}$ ($k \ge 1$) and leaves $B_0^{(Q)}$ unchanged. Because Paper 153's finite-block summation-by-parts identity ([1], Proposition 2.2, equation (3.4)) depends solely on telescoping of $w_m$ across $B_k^{(Q)}$, it holds **verbatim for every prime or composite integer $Q \ge 2$**: for all $f, g \in \mathcal{S}$,
$$
\bigl\langle P_{\mathcal{W}_Q} f,\, P_{\mathcal{W}_Q} g\bigr\rangle_{\mathcal{S}}
= \bigl\langle (I - V_Q V_Q^*) f,\, g\bigr\rangle_{\mathcal{S}}
= \sum_{k=0}^{\infty} \sum_{u=1}^{Q-1} \sum_{v=1}^{Q-1} K_{u,v}^{(Q)}\, \frac{(\nabla f)(Qk+u)}{Qk+u}\, \frac{\overline{(\nabla g)(Qk+v)}}{Qk+v},
\tag{1.10}
$$
where $K^{(Q)} = \bigl(K_{u,v}^{(Q)}\bigr)_{1 \le u,v \le Q-1}$ is the symmetric positive-definite $(Q-1)\times(Q-1)$ discrete Green / Kac–Murdock–Szegő (KMS) covariance matrix [11, 1]
$$
K_{u,v}^{(Q)} := \min(u, v) - \frac{uv}{Q} \qquad (1 \le u, v \le Q-1).
\tag{1.11}
$$
Throughout, $\mathbb{N}_Q := \{m \in \mathbb{N} : Q \nmid m\} = \{Qk + u : k \ge 0,\; 1 \le u \le Q-1\}$ denotes the non-multiples of $Q$, and $\Omega_Q := \{m \in \mathbb{N} : \gcd(m, Q) = 1\} \subseteq \mathbb{N}_Q$ denotes the $Q$-coprime integers. Crucially, index $m = Qk$ ($u = 0$) **never enters** (1.10): jumps between $Qk - 1 \in B_{k-1}^{(Q)}$ and $Qk \in B_k^{(Q)}$ belong entirely to $V_Q(\mathcal{S})$. Moreover, since $V_Q V_Q^* f$ is constant across all of $B_k^{(Q)} = \{Qk, \dots, Qk+Q-1\}$ (including $Qk$ and $Qk+1$), $(\nabla V_Q V_Q^* f)(m) = 0$ and hence $(\nabla P_{\mathcal{W}_Q} f)(m) = (\nabla f)(m)$ identically for all $m \in \mathbb{N}_Q$.

---

### 1.3. Summary of Main Results and Attribution Boundary

Our first theorem establishes the algebraic collapse of multi-layer Wold truncations, determines the exact kernel and dimension of $P_{\mathcal{W}_Q}$ on $\mathcal{V}_N$ and $\widetilde{\mathcal{V}}_N$, characterizes the phase transition across $Q = N/2$ and $Q = N$, and extends Paper 153's prime-$p$ cosecant norm formula to arbitrary composite dilations $Q \ge 2$.

**Theorem 1 (Multi-layer Wold collapse, exact range intersection, horizon unlocking, and general-$Q$ cosecant norms).** *Let $q \ge 2$, $J \ge 1$, and $N, Q \ge 2$ be integers.*
1. *(Exact semigroup collapse).* *For all $Q_1, Q_2 \ge 1$, $V_{Q_1} V_{Q_2} = V_{Q_1 Q_2}$ on $\mathcal{S}$. Consequently, the $J$-layer Wold filtration (1.3) collapses identically to the single composite wandering subspace at horizon $Q = q^J$:*
   $$
   I - V_{q^J} V_{q^J}^* = \sum_{j=0}^{J-1} V_q^j (I - V_q V_q^*)(V_q^*)^j, \qquad
   \mathcal{H}_{J,q} = \mathcal{W}_{q^J}^{\mathcal{S}}, \qquad
   d_N^2(\mathcal{H}_{J,q}) = d_N^2(\mathcal{W}_{q^J}^{\mathcal{S}}).
   \tag{1.12}
   $$
2. *(Exact range intersection, dimension drop, step plateaus, and sharp norm jump).* *With $\mathcal{V}_0 = \mathcal{V}_1 := \{0\}$,*
   $$
   \widetilde{\mathcal{V}}_N \cap V_Q(\mathcal{S}) = \mathcal{V}_N \cap V_Q(\mathcal{S}) = V_Q(\mathcal{V}_{\lfloor N/Q\rfloor}) = \operatorname{span}\!\left\{G_{kQ} - \frac{1}{k} G_Q : 2 \le k \le \lfloor N/Q\rfloor\right\}.
   \tag{1.13}
   $$
   *Consequently:*
   - *$\dim P_{\mathcal{W}_Q}(\widetilde{\mathcal{V}}_N) = N - \max(0, \lfloor N/Q\rfloor - 1)$ and $\dim P_{\mathcal{W}_Q}(\mathcal{V}_N) = (N - 1) - \max(0, \lfloor N/Q\rfloor - 1)$.*
   - *For every integer $k \ge 2$, $P_{\mathcal{W}_Q} G_{kQ} = \frac{1}{k} P_{\mathcal{W}_Q} G_Q$, producing exact horizontal step plateaus*
     $$
     d_{kQ}^2(\mathcal{W}_Q^{\mathcal{S}}) = d_{kQ-1}^2(\mathcal{W}_Q^{\mathcal{S}}) \qquad (\forall\, k \ge 2).
     \tag{1.14}
     $$
   - *Writing $\eta(N, Q) := \sup_{0 \ne f \in \widetilde{\mathcal{V}}_N} \|V_Q^* f\|_{\mathcal{S}}^2 / \|f\|_{\mathcal{S}}^2 = \|V_Q^*|_{\widetilde{\mathcal{V}}_N}\|^2$, one has the sharp threshold*
     $$
     \eta(N, Q) = 1 \quad \text{for } 2 \le Q \le \lfloor N/2\rfloor, \qquad
     \eta(N, Q) < 1 \quad \text{for } Q > N/2.
     \tag{1.15}
     $$
3. *(Sub-horizon unlocking vs. super-horizon locking of pole cancellation).* *Define the anchored wandering generators*
   $$
   H_1^{(Q)} := -Q\, P_{\mathcal{W}_Q} G_Q, \qquad
   H_d^{(Q)} := P_{\mathcal{W}_Q}\!\left(G_d - \frac{Q}{d} G_Q\right) \quad (d \ge 2,\; Q \nmid d).
   \tag{1.16}
   $$
   *Then $(\nabla H_d^{(Q)})(m) = \mathbf{1}_{d \mid m}$ identically on $\mathbb{N}_Q$ for every $d \ge 1$ with $Q \nmid d$. When $Q \le N$ (sub-horizon), $G_Q \in \mathcal{V}_N$ belongs to the approximant span, $\{H_1^{(Q)}\} \cup \{H_d^{(Q)} : 2 \le d \le N,\; Q \nmid d\}$ is a basis of $P_{\mathcal{W}_Q}(\mathcal{V}_N)$, and every residual $P_{\mathcal{W}_Q}(E - g)$ ($g \in \mathcal{V}_N$) has freely decoupled constant jump $H_1^{(Q)}$ on $\mathbb{N}_Q$ (unlocking the pole-cancellation constraint). When $Q > N$ (super-horizon), $P_{\mathcal{W}_Q}$ is injective on $\widetilde{\mathcal{V}}_N$ and the background jump shift remains globally locked.*
4. *(Closed-form general-$Q$ cosecant norm).* *For every integer $Q \ge 2$ and every integer $d \ge Q - 1$ with $Q \nmid d$, put $g := \gcd(d, Q)$ and $u_b := b d \bmod Q$. Then*
   $$
   \|H_d^{(Q)}\|_{\mathcal{S}}^2 = \frac{\pi^2 \gcd(d, Q)^2}{2 Q^3 d^2} \sum_{b=1}^{Q/\gcd(d, Q) - 1} u_b(Q - u_b)\, \csc^2\!\left(\frac{\pi b \gcd(d, Q)}{Q}\right).
   \tag{1.17}
   $$

Our second theorem resolves the sub-horizon sieve regime for every prime or composite $Q \ge 2$ by combining a discrete Dirichlet-energy dual variational identity for $K^{(Q)}$ with a universal composite-$Q$ Ramanujan $L(2)$ Euler-product theorem.

**Theorem 2 (Discrete Dirichlet-energy duality and general-$Q$ Jordan totient sieves).** *Let $Q \ge 2$ and $N \ge 2$ be integers.*
1. *(Discrete Dirichlet-energy dual variational formula).* *Let $\Delta_Q := (K^{(Q)})^{-1}$ be the $(Q-1)\times(Q-1)$ Dirichlet second-difference matrix $(\Delta_Q w)_u = 2 w_u - w_{u-1} - w_{u+1}$ ($w_0 = w_Q := 0$). Extending any sequence $F : \mathbb{N}_Q \to \mathbb{C}$ by $F(Qk) := 0$ ($k \ge 0$),*
   $$
   d_N^2(\mathcal{W}_Q^{\mathcal{S}}) = \sup_{0 \ne F \in \mathcal{A}_{N,Q}} \frac{|F(1)|^2}{\sum_{k=0}^{\infty}\sum_{r=0}^{Q-1} \bigl|F(Qk+r+1) - F(Qk+r)\bigr|^2},
   \tag{1.18}
   $$
   *where $\mathcal{A}_{N,Q}$ consists of all finite-Dirichlet-energy sequences $F : \mathbb{N}_Q \to \mathbb{C}$ satisfying $\sum_{m \in \mathbb{N}_Q} \frac{F(m)}{m}\bigl(\mathbf{1}_{n \mid m} - \frac{1}{n}\bigr) = 0$ for $2 \le n \le N$. Moreover, the eigenvalues of $K^{(Q)}$ are $\lambda_j(K^{(Q)}) = \bigl(4\sin^2\frac{\pi j}{2Q}\bigr)^{-1}$ ($1 \le j \le Q - 1$), giving the sharp Loewner sandwich*
   $$
   \frac{1}{4\cos^2(\pi/(2Q))}\, I_{Q-1} \preceq K^{(Q)} \preceq \frac{1}{4\sin^2(\pi/(2Q))}\, I_{Q-1}.
   \tag{1.19}
   $$
2. *(Universal composite-$Q$ Ramanujan $L(2)$ Euler-product identity).* *Let $c_\ell(m) := \sum_{d \mid \gcd(\ell, m)} d\,\mu(\ell/d)$ denote Ramanujan's sum ($c_1(m) := 1$). For every integer $Q \ge 1$ and all integers $\ell_1, \ell_2 \ge 1$,*
   $$
   \sum_{\substack{m=1 \\ \gcd(m, Q) = 1}}^{\infty} \frac{c_{\ell_1}(m)\, c_{\ell_2}(m)}{m^2} = \frac{\pi^2 J_2(Q)}{6 Q^2} \left(\prod_{p \mid Q} \mu\!\bigl(p^{\nu_p(\ell_1)}\bigr)\mu\!\bigl(p^{\nu_p(\ell_2)}\bigr)\right) \prod_{\substack{r \mid \ell_1 \ell_2 \\ r \nmid Q}} \mathcal{E}_r\bigl(\nu_r(\ell_1), \nu_r(\ell_2)\bigr),
   \tag{1.20}
   $$
   *where for each prime $r \nmid Q$ and integers $a, b \ge 0$,*
   $$
   \mathcal{E}_r(a, b) := \begin{cases}
   1, & a = b = 0, \\
   \dfrac{2(r - 1)}{r}, & a = b \ge 1, \\[6pt]
   -\dfrac{\varphi(r^{\min(a,b)})(r - 1)}{r^{\max(a,b)}}, & a \ne b.
   \end{cases}
   \tag{1.21}
   $$
3. *(Explicit two-sided Jordan totient sieve bounds and uniform sub-horizon vanishing).* *For all integers $N, Q \ge 2$,*
   $$
   d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \ge \frac{6 Q^2}{4\pi^2 J_2(Q)\cos^2(\pi/(2Q))} \sum_{\substack{\ell > N \\ \gcd(\ell, Q) = 1}} \frac{\mu(\ell)^2}{J_2(\ell)},
   \tag{1.22}
   $$
   *and whenever $N \ge Q$,*
   $$
   d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \le \frac{6}{4\pi^2 \sin^2(\pi/(2Q))} \sum_{\ell > N} \frac{\mu(\ell)^2}{J_2(\ell)} < \frac{3 Q^2}{4\pi^2 N} < \frac{Q^2}{4 N}.
   \tag{1.23}
   $$
   *For every fixed $Q \ge 2$, the $Q$-coprime tail satisfies the cubefree-convolution asymptotic*
   $$
   \sum_{\substack{\ell > N \\ \gcd(\ell, Q) = 1}} \frac{\mu(\ell)^2}{J_2(\ell)} = \frac{\mathcal{C}_Q}{N} + O_Q(N^{-3/2}), \qquad
   \mathcal{C}_Q := C_{\mathrm{all}} \prod_{p \mid Q} \frac{p^2 - 1}{p^2 + p - 1}, \qquad
   C_{\mathrm{all}} := \prod_{p}\left(1 - \frac{1}{p(p + 1)}\right),
   \tag{1.24}
   $$
   *so $d_N^2(\mathcal{W}_Q^{\mathcal{S}}) = \Theta_Q(N^{-1})$ unconditionally ($L_Q / N + O_Q(N^{-3/2}) \le d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \le U_Q / N + O_Q(N^{-3/2})$ with $L_Q := \frac{6 Q^2 \mathcal{C}_Q}{4\pi^2 J_2(Q)\cos^2(\pi/(2Q))}$ and $U_Q := \frac{6 C_{\mathrm{all}}}{4\pi^2 \sin^2(\pi/(2Q))}$). Uniformly along any growing schedule $Q = Q(N)$ with $Q(N) = o(N^{1/2})$ (in particular $J(N) \le (\frac{1}{2} - \delta)\log_q N$ for any $\delta > 0$), $\lim_{N\to\infty} d_N(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = 0$ unconditionally.*

Our third theorem crosses into the super-horizon regime ($Q \gg N^2$), proving an explicit inverse large sieve on $\widetilde{\mathcal{V}}_N$ that bounds the coarse tail $\|V_Q^* f\|_{\mathcal{S}}^2$ uniformly and transfers both the NBBD equivalence for RH and Burnol's unconditional $(\log N)^{-1}$ barrier to finite Wold horizons.

**Theorem 3 (Quartic Fejér–Schur inverse large sieve, finite-horizon RH equivalence, and unconditional Burnol transfer).** *Let $N, Q \ge 2$ be integers.*
1. *(Explicit coarse-tail contraction bound).* *Every $f \in \widetilde{\mathcal{V}}_N$ satisfies*
   $$
   \|V_Q^* f\|_{\mathcal{S}}^2 \le \kappa_{\mathrm{FS}}(N)\, N^2\left(\frac{1}{Q} + \frac{\pi^2 N^3}{8 Q^3}\right) \|f\|_{\mathcal{S}}^2 \le \eta_{\mathrm{explicit}}(N, Q)\, \|f\|_{\mathcal{S}}^2,
   \tag{1.25}
   $$
   *where*
   $$
   \kappa_{\mathrm{FS}}(N) := \frac{4(2 + N^{-4})(4 + N^{-2})}{3(1 - \pi^4/720)} \le \kappa_{\mathrm{FS}}(2) = \frac{187}{16(1 - \pi^4/720)} < 14, \qquad
   \eta_{\mathrm{explicit}}(N, Q) := 14 N^2\left(\frac{1}{Q} + \frac{\pi^2 N^3}{8 Q^3}\right).
   \tag{1.26}
   $$
   *Consequently, $(1 - \eta_{\mathrm{explicit}}(N, Q))\, d_N^2(\mathcal{S}) \le d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \le d_N^2(\mathcal{S})$ whenever $\eta_{\mathrm{explicit}}(N, Q) < 1$.*
2. *(Finite-horizon RH equivalence at $Q(N) = \lceil 29 N^2\rceil$).* *For every $N \ge 2$ and every $Q \ge 29 N^2$, $\eta_{\mathrm{explicit}}(N, Q) \le \frac{14}{29} + \frac{7\pi^2}{195112} < \frac{1}{2}$ (whereas $c = 28$ gives $\eta_{\mathrm{explicit}}(2, 112) = \frac{1}{2} + \frac{7\pi^2}{175616} > \frac{1}{2}$), so*
   $$
   \frac{1}{2}\, d_N^2(\mathcal{S}) < d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \le d_N^2(\mathcal{S}) \qquad (\forall\, N \ge 2,\; \forall\, Q \ge 29 N^2).
   \tag{1.27}
   $$
   *In particular, for $Q(N) = \lceil 29 N^2\rceil$ — or in the $q$-adic filtration $\mathcal{H}_{J_{\mathrm{RH}}(N), q}$ with $J_{\mathrm{RH}}(N) := \lceil 2\log_q N + \log_q 29\rceil$ — the Riemann Hypothesis holds if and only if $\lim_{N\to\infty} d_N(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = 0$.*
3. *(Unconditional transfer of Burnol's $(\log N)^{-1}$ barrier).* *Along any horizon schedule $Q = Q(N)$ satisfying $Q(N) / N^2 \to \infty$ as $N \to \infty$, $d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = (1 + o(1))\, d_N^2(\mathcal{S})$, and **unconditionally** (without assuming RH or simplicity of zeros)*
   $$
   \liminf_{N \to \infty} d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) \log N \ge B_{\mathrm{NB}} = 2 + \gamma - \log(4\pi) \in [0.04619141793224206762862049581299058,\, 0.04619141793224206762862049581299059].
   \tag{1.28}
   $$
   *Specifically, if RH fails, $\liminf_{N\to\infty} d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = \mathcal{D}_\infty^2 > 0$ so the left-hand side of (1.28) is $+\infty$; if RH holds, it is bounded below by $\sum_{\rho} m(\rho)^2 / |\rho|^2 \ge B_{\mathrm{NB}}$.*

**Attribution boundary and scientific scope.** We adopt the step-space framework and finite-block identity (1.10) from Paper 153 [1], the isometric continuous-dilation transfer and off-line zero defect $\mathcal{D}_\infty > 0$ from Báez-Duarte [4], Burnol [9, 10], and Paper 1 [2], and the classical KMS eigenstructure [11] and Farey spacing inequality [12, 15]. All three main theorems — the multi-layer Wold collapse and exact range intersection $\widetilde{\mathcal{V}}_N \cap V_Q(\mathcal{S}) = V_Q(\mathcal{V}_{\lfloor N/Q\rfloor})$, the sub-horizon pole-unlocking mechanism and composite-$Q$ cosecant norm formula, the discrete Dirichlet dual variational principle, the composite-$Q$ Ramanujan $L(2)$ Euler-product identity and two-sided Jordan totient sieve bounds, and the quartic Fejér–Schur inverse large sieve giving the explicit $Q(N) = \lceil 29 N^2\rceil$ RH equivalence — are new. Explicitly, these results resolve the operator-theoretic and sieve-theoretic phase transition across Wold horizons in $\mathcal{S}$ and provide a quantitative finite-horizon reformulation of RH; **they do not constrain the location of the zeros of $\zeta(s)$ or claim progress toward proving RH itself**.

---

## 2. Proof of Theorem 1: Multi-Layer Wold Collapse, Range Intersection, and Cosecant Norms

### 2.1. Semigroup Collapse of $J$-Layer Wold Filtrations

**Lemma 2.1 (Multiplicative semigroup and telescoping projections).** *For all integers $Q_1, Q_2 \ge 1$, $V_{Q_1} V_{Q_2} = V_{Q_1 Q_2}$ on $\mathcal{S}$. Consequently, for every $q \ge 2$ and $J \ge 1$, $V_q^J = V_{q^J}$ and (1.12) holds.*

*Proof.* On $(0, 1]$, $(V_{Q_1} V_{Q_2} f)(x) = Q_1^{1/2} (V_{Q_2} f)(Q_1 x) = (Q_1 Q_2)^{1/2} f(Q_1 Q_2 x) = (V_{Q_1 Q_2} f)(x)$ (equivalently in sequence coordinates, $\lfloor \lfloor m / Q_1\rfloor / Q_2\rfloor = \lfloor m / (Q_1 Q_2)\rfloor$ for every $m \ge 1$). Induction gives $V_q^J = V_{q^J}$ and $(V_q^*)^J = V_{q^J}^*$. Since $V_q$ is an isometry ($V_q^* V_q = I$), each summand $P_j := V_q^j (I - V_q V_q^*)(V_q^*)^j = V_q^j (V_q^*)^j - V_q^{j+1}(V_q^*)^{j+1}$ is the orthogonal projection onto $V_q^j \mathcal{W}_q^{\mathcal{S}}$, and summing from $j = 0$ to $J - 1$ telescopes identically to $I - V_q^J (V_q^*)^J = I - V_{q^J} V_{q^J}^* = P_{\mathcal{W}_{q^J}}$. Hence $\mathcal{H}_{J,q} = \mathcal{W}_{q^J}^{\mathcal{S}}$ and $d_N^2(\mathcal{H}_{J,q}) = d_N^2(\mathcal{W}_{q^J}^{\mathcal{S}})$. $\square$

---

### 2.2. Exact Range Intersection, Step Plateaus, and the Kernel Threshold at $Q = N/2$

**Lemma 2.2 (Action of $V_Q$ on Báez-Duarte generators).** *For every integer $Q \ge 2$ and every integer $k \ge 2$,*
$$
V_Q G_k = Q^{1/2}\left(G_{kQ} - \frac{1}{k} G_Q\right).
\tag{2.1}
$$

*Proof.* Evaluate both sides at $m \ge 1$. Write $m = Q q + r$ with integers $q = \lfloor m/Q\rfloor \ge 0$ and $0 \le r \le Q - 1$. Then $m \bmod (kQ) = Q(q \bmod k) + r$ and $m \bmod Q = r$, so by (1.5),
$$
G_{kQ}(m) - \frac{1}{k} G_Q(m) = -\frac{Q(q \bmod k) + r}{kQ} + \frac{r}{kQ} = -\frac{q \bmod k}{k}.
$$
For $1 \le m < Q$ we have $q = 0$, so the right-hand side vanishes, matching $(V_Q G_k)(m) = 0$. For $m \ge Q$ we have $q \ge 1$, so $-\frac{q \bmod k}{k} = G_k(q) = Q^{-1/2}(V_Q G_k)(m)$. $\square$

**Lemma 2.3 (Exact nullspace of $P_{\mathcal{W}_Q}$ on $\widetilde{\mathcal{V}}_N$ and $\mathcal{V}_N$).** *For all integers $N, Q \ge 2$, (1.13)–(1.15) hold.*

*Proof.* By Lemma 2.2, for $2 \le k \le \lfloor N/Q\rfloor$, $Q^{-1/2} V_Q G_k = G_{kQ} - \frac{1}{k} G_Q$ lies in $\mathcal{V}_N \cap V_Q(\mathcal{S})$ since $Q < kQ \le N$. Because $V_Q$ is injective and $\{G_2, \dots, G_{\lfloor N/Q\rfloor}\}$ is linearly independent ([4]; immediately verified by triangularity of $(\nabla G_k)(m)$), this yields $V_Q(\mathcal{V}_{\lfloor N/Q\rfloor}) \subseteq \mathcal{V}_N \cap V_Q(\mathcal{S}) \subseteq \widetilde{\mathcal{V}}_N \cap V_Q(\mathcal{S})$ of dimension $\max(0, \lfloor N/Q\rfloor - 1)$.

Conversely, suppose $f = a_1 E + \sum_{d=2}^N a_d G_d \in \widetilde{\mathcal{V}}_N \cap V_Q(\mathcal{S})$. Then $P_{\mathcal{W}_Q} f = 0$, so by strict positivity of $K^{(Q)}$ in (1.10), $(\nabla f)(m) = 0$ for every $m \in \mathbb{N}_Q = \{m \ge 1 : Q \nmid m\}$. Choose any prime $p > \max(N, Q)$. Then $p \in \mathbb{N}_Q$ and no $2 \le d \le N$ divides $p$, so evaluating (1.8) at $m = p$ yields
$$
\sum_{d=2}^{N} \frac{a_d}{d} = 0.
\tag{2.2}
$$
Substituting (2.2) back into (1.8) simplifies the jump identity on $\mathbb{N}_Q$ to
$$
a_1 \mathbf{1}_{m=1} + \sum_{\substack{2 \le d \le N \\ d \mid m}} a_d = 0 \qquad (\forall\, m \in \mathbb{N}_Q).
\tag{2.3}
$$
Since $Q \ge 2$, $1 \in \mathbb{N}_Q$; evaluating (2.3) at $m = 1$ gives $a_1 = 0$, proving $f \in \mathcal{V}_N$. Next, we show by strong induction on $m \in \{2, \dots, N\} \cap \mathbb{N}_Q$ that $a_m = 0$ whenever $Q \nmid m$: if $m \in \{2, \dots, N\}$ is not divisible by $Q$, then **no divisor $d \mid m$ can be divisible by $Q$**, so every proper divisor $d \mid m$ ($2 \le d < m$) also satisfies $Q \nmid d$ and thus $a_d = 0$ by the induction hypothesis; evaluating (2.3) at $m$ leaves $a_m = 0$. Therefore $a_d = 0$ unless $Q \mid d$. Writing the remaining nonzero terms as $d = kQ$ ($1 \le k \le \lfloor N/Q\rfloor$): if $N < Q$ the sum is empty and $f = 0$; if $N \ge Q$, substituting $a_d = 0$ ($Q \nmid d$) into (2.2) gives $\frac{a_Q}{Q} + \sum_{k=2}^{\lfloor N/Q\rfloor} \frac{a_{kQ}}{kQ} = 0$, i.e., $a_Q = -\sum_{k=2}^{\lfloor N/Q\rfloor} \frac{a_{kQ}}{k}$, whence
$$
f = a_Q G_Q + \sum_{k=2}^{\lfloor N/Q\rfloor} a_{kQ} G_{kQ} = \sum_{k=2}^{\lfloor N/Q\rfloor} a_{kQ}\left(G_{kQ} - \frac{1}{k} G_Q\right) \in V_Q(\mathcal{V}_{\lfloor N/Q\rfloor}),
$$
establishing (1.13) and both rank formulas by rank–nullity.

Applying $P_{\mathcal{W}_Q}$ to (2.1) annihilates the left-hand side and gives $P_{\mathcal{W}_Q} G_{kQ} = \frac{1}{k} P_{\mathcal{W}_Q} G_Q$ for every $k \ge 2$. Since $G_Q \in \mathcal{V}_{kQ-1}$ whenever $k \ge 2$ ($Q \le 2Q - 1 \le kQ - 1$), adjoining $G_{kQ}$ to $\mathcal{V}_{kQ-1}$ does not enlarge $P_{\mathcal{W}_Q}(\mathcal{V}_{kQ-1})$, proving $d_{kQ}^2(\mathcal{W}_Q^{\mathcal{S}}) = d_{kQ-1}^2(\mathcal{W}_Q^{\mathcal{S}})$ in (1.14). Finally, for any $f \in \widetilde{\mathcal{V}}_N$, $\|V_Q^* f\|_{\mathcal{S}}^2 = \|V_Q V_Q^* f\|_{\mathcal{S}}^2 = \|f\|_{\mathcal{S}}^2 - \|P_{\mathcal{W}_Q} f\|_{\mathcal{S}}^2$. If $2 \le Q \le \lfloor N/2\rfloor$, then $\lfloor N/Q\rfloor \ge 2$, so $f = G_{2Q} - \frac{1}{2} G_Q \in \widetilde{\mathcal{V}}_N \cap V_Q(\mathcal{S})$ is nonzero and satisfies $P_{\mathcal{W}_Q} f = 0$, giving $\eta(N, Q) = 1$. If $Q > N/2$, then $\lfloor N/Q\rfloor \le 1$, so $\widetilde{\mathcal{V}}_N \cap V_Q(\mathcal{S}) = \{0\}$; since $\widetilde{\mathcal{V}}_N$ is finite-dimensional, $\inf_{\|f\|_{\mathcal{S}}=1} \|P_{\mathcal{W}_Q} f\|_{\mathcal{S}}^2 > 0$, whence $\eta(N, Q) < 1$. $\square$

---

### 2.3. Sub-Horizon Pole Unlocking and the General-$Q$ Cosecant Norm Formula

*Proof of Theorem 1(3).* By (1.6) and the identity $(\nabla P_{\mathcal{W}_Q} f)|_{\mathbb{N}_Q} = (\nabla f)|_{\mathbb{N}_Q}$, on $\mathbb{N}_Q$ we have $(\nabla G_Q)(m) = \mathbf{1}_{Q \mid m} - \frac{1}{Q} = -\frac{1}{Q}$. Hence $H_1^{(Q)} = -Q P_{\mathcal{W}_Q} G_Q$ has constant jump $(\nabla H_1^{(Q)})(m) = 1$ on all of $\mathbb{N}_Q$, while for every $d \ge 2$ with $Q \nmid d$,
$$
\bigl(\nabla H_d^{(Q)}\bigr)(m) = \left(\mathbf{1}_{d \mid m} - \frac{1}{d}\right) - \frac{Q}{d}\left(-\frac{1}{Q}\right) = \mathbf{1}_{d \mid m} \qquad (\forall\, m \in \mathbb{N}_Q).
\tag{2.4}
$$
When $Q \le N$, $G_Q \in \mathcal{V}_N$, so $H_1^{(Q)}$ and $\{H_d^{(Q)} : 2 \le d \le N,\; Q \nmid d\}$ all belong to $P_{\mathcal{W}_Q}(\mathcal{V}_N)$. Among $\{1, 2, \dots, N\}$, exactly $\lfloor N/Q\rfloor$ integers are multiples of $Q$, leaving $N - \lfloor N/Q\rfloor = (N - 1) - (\lfloor N/Q\rfloor - 1) = \dim P_{\mathcal{W}_Q}(\mathcal{V}_N)$ generators $\{H_d^{(Q)} : 1 \le d \le N,\; Q \nmid d\}$. By triangularity of $\mathbf{1}_{d \mid m}$ on $\{1, \dots, N\} \cap \mathbb{N}_Q$, these generators are linearly independent and therefore form an exact basis of $P_{\mathcal{W}_Q}(\mathcal{V}_N)$, unlocking the constant jump $H_1^{(Q)}$ from the divisor weights. When $Q > N$, $\lfloor N/Q\rfloor = 0$, so $P_{\mathcal{W}_Q}$ is injective on $\widetilde{\mathcal{V}}_N$ by Lemma 2.3. $\square$

**Lemma 2.4 (Closed-form cosecant norm on $d \ge Q - 1$).** *For every integer $Q \ge 2$ and every integer $d \ge Q - 1$ with $Q \nmid d$, formula (1.17) holds.*

*Proof.* Put $g := \gcd(d, Q)$, $Q' := Q/g \ge 2$ (since $Q \nmid d$), and $L := \operatorname{lcm}(d, Q) = Q' d$. By (2.4), $(\nabla H_d^{(Q)})(m) = \mathbf{1}_{d \mid m}$ on $\mathbb{N}_Q$. Suppose $1 \le u < v \le Q - 1$ both satisfied $d \mid (Qk + u)$ and $d \mid (Qk + v)$ for some $k \ge 0$; then $d \mid (v - u)$ with $1 \le v - u \le Q - 2$, impossible since $d \ge Q - 1$. Thus each open residue block $\{Qk + 1, \dots, Qk + Q - 1\}$ ($k \ge 0$) contains **at most one** multiple of $d$, so all off-diagonal terms $u \ne v$ in (1.10) vanish. Because $K_{u,u}^{(Q)} = u - \frac{u^2}{Q} = \frac{u(Q - u)}{Q}$, (1.10) reduces to
$$
\|H_d^{(Q)}\|_{\mathcal{S}}^2 = \sum_{\substack{m \ge 1 \\ d \mid m,\; Q \nmid m}} \frac{(m \bmod Q)\bigl(Q - (m \bmod Q)\bigr)}{Q\, m^2}.
\tag{2.5}
$$
Every $m \ge 1$ with $d \mid m$ and $Q \nmid m$ is uniquely parameterized as $m = (r Q' + b) d = r L + b d$ with $r \ge 0$ and $1 \le b \le Q' - 1$ (since $Q \mid b d \iff Q' \mid b$). For fixed $b$, $m \bmod Q = b d \bmod Q = u_b \in \{1, \dots, Q - 1\}$, and summing over $r \ge 0$ yields a Hurwitz zeta value $\zeta(2, \alpha) := \sum_{r=0}^{\infty} (r + \alpha)^{-2}$:
$$
\|H_d^{(Q)}\|_{\mathcal{S}}^2 = \frac{1}{Q L^2} \sum_{b=1}^{Q'-1} u_b(Q - u_b)\, \zeta\!\left(2,\, \frac{b}{Q'}\right).
\tag{2.6}
$$
Under the involution $b \mapsto Q' - b$ on $\{1, \dots, Q' - 1\}$, $(Q' - b)d = L - b d \equiv -u_b \pmod{Q}$ and $1 \le u_b \le Q - 1$, so $u_{Q'-b} = Q - u_b$ and $u_{Q'-b}(Q - u_{Q'-b}) = u_b(Q - u_b)$. Averaging (2.6) with its reflected index $Q' - b$ and invoking Euler's reflection identity $\zeta(2, x) + \zeta(2, 1 - x) = \pi^2 \csc^2(\pi x)$ ($0 < x < 1$) gives
$$
\|H_d^{(Q)}\|_{\mathcal{S}}^2 = \frac{1}{2 Q (Q' d)^2} \sum_{b=1}^{Q'-1} u_b(Q - u_b)\left[\zeta\!\left(2, \frac{b}{Q'}\right) + \zeta\!\left(2, 1 - \frac{b}{Q'}\right)\right] = \frac{\pi^2 g^2}{2 Q^3 d^2} \sum_{b=1}^{Q'-1} u_b(Q - u_b)\, \csc^2\!\left(\frac{\pi b g}{Q}\right),
$$
since $Q' = Q/g$. When $Q = p$ is prime and $d > p$ ($g = 1$), $\{u_1, \dots, u_{p-1}\}$ permutes $\{1, \dots, p - 1\}$ with $b \equiv u_b d^{-1} \pmod{p}$, recovering Paper 153's Proposition 3.1 ([1], equation (3.9)). $\square$

---

## 3. Proof of Theorem 2: Discrete Dirichlet Duality and General-$Q$ Jordan Totient Sieves

### 3.1. KMS Spectral Bounds and the Discrete Dirichlet Dual Variational Formula

*Proof of Theorem 2(1).* Let $\ell^2(K^{(Q)})$ denote the Hilbert space of sequences $\phi : \mathbb{N}_Q \to \mathbb{C}$ equipped with the block-weighted inner product
$$
\langle \phi, \psi\rangle_{K^{(Q)}} := \sum_{k=0}^{\infty} \langle K^{(Q)} \boldsymbol{\phi}_k,\, \boldsymbol{\psi}_k\rangle_{\mathbb{C}^{Q-1}}, \qquad (\boldsymbol{\phi}_k)_u := \phi(Qk + u) \quad (1 \le u \le Q - 1).
\tag{3.1}
$$
Direct matrix multiplication verifies $(K^{(Q)} \Delta_Q)_{u,v} = \delta_{u,v}$ for $1 \le u, v \le Q - 1$: for $w \in \mathbb{C}^{Q-1}$ ($w_0 = w_Q = 0$), $\sum_{v=1}^{Q-1} \bigl(\min(u, v) - \frac{uv}{Q}\bigr)(2 w_v - w_{v-1} - w_{v+1}) = w_u$ by discrete summation by parts. The normalized sine vectors $e_j(u) := \sqrt{\frac{2}{Q}}\sin\frac{\pi j u}{Q}$ ($1 \le j, u \le Q - 1$) satisfy $(\Delta_Q e_j)(u) = 4\sin^2\bigl(\frac{\pi j}{2Q}\bigr)\, e_j(u)$ [11], so the eigenvalues of $K^{(Q)} = \Delta_Q^{-1}$ are $\lambda_j(K^{(Q)}) = \bigl(4\sin^2\frac{\pi j}{2Q}\bigr)^{-1}$ ($1 \le j \le Q - 1$), whose minimum at $j = Q - 1$ is $\bigl(4\cos^2\frac{\pi}{2Q}\bigr)^{-1}$ and maximum at $j = 1$ is $\bigl(4\sin^2\frac{\pi}{2Q}\bigr)^{-1}$, establishing (1.19).

Now define the jump-rescaling map $\Phi : \mathcal{S} \to \ell^2(K^{(Q)})$ by $(\Phi f)(m) := \frac{(\nabla f)(m)}{m}$ ($m \in \mathbb{N}_Q$). By (1.10), $\|P_{\mathcal{W}_Q} f\|_{\mathcal{S}}^2 = \|\Phi f\|_{K^{(Q)}}^2$ for every $f \in \mathcal{S}$. Since $(\Phi E)(m) = \mathbf{1}_{m=1}$ and $(\Phi G_n)(m) = \frac{1}{m}\bigl(\mathbf{1}_{n \mid m} - \frac{1}{n}\bigr)$ ($2 \le n \le N$), $d_N^2(\mathcal{W}_Q^{\mathcal{S}}) = \operatorname{dist}_{\ell^2(K^{(Q)})}\bigl(\Phi E,\, \operatorname{span}\{\Phi G_2, \dots, \Phi G_N\}\bigr)^2$. In any Hilbert space $\mathcal{H}$, the squared distance from $x_0$ to a finite-dimensional subspace $\mathcal{M}$ equals $\sup\{|\langle x_0, y\rangle_{\mathcal{H}}|^2 / \|y\|_{\mathcal{H}}^2 : 0 \ne y \in \mathcal{M}^\perp\}$. Changing dual variables via $\mathbf{F}_k := K^{(Q)} \mathbf{y}_k$ (so $\mathbf{y}_k = \Delta_Q \mathbf{F}_k$, $\langle \boldsymbol{\phi}_k, \mathbf{y}_k\rangle_{K^{(Q)}} = \langle \boldsymbol{\phi}_k, \mathbf{F}_k\rangle_{\mathbb{C}^{Q-1}}$, and $\|\mathbf{y}_k\|_{K^{(Q)}}^2 = \langle \Delta_Q \mathbf{F}_k, \mathbf{F}_k\rangle_{\mathbb{C}^{Q-1}}$), the orthogonality $\langle \Phi G_n, y\rangle_{K^{(Q)}} = 0$ becomes $\sum_{m \in \mathbb{N}_Q} \frac{F(m)}{m}\bigl(\mathbf{1}_{n \mid m} - \frac{1}{n}\bigr) = 0$ ($2 \le n \le N$), $\langle \Phi E, y\rangle_{K^{(Q)}}$ becomes $F(1)$, and summation by parts with $F(Qk) = F(Qk+Q) := 0$ gives $\langle \Delta_Q \mathbf{F}_k, \mathbf{F}_k\rangle_{\mathbb{C}^{Q-1}} = \sum_{r=0}^{Q-1} |F(Qk+r+1) - F(Qk+r)|^2$, proving (1.18). $\square$

---

### 3.2. Composite-$Q$ Ramanujan $L(2)$ Euler Product and Walsh–Selberg Sieve Solution

**Lemma 3.1 ($Q$-coprime probability space).** *Fix any integer $Q \ge 1$, and endow $\Omega_Q = \{m \ge 1 : \gcd(m, Q) = 1\}$ with the probability measure*
$$
\mathbb{P}_Q(\{m\}) := \frac{1}{Z_Q\, m^2} \quad (m \in \Omega_Q), \qquad
Z_Q := \sum_{m \in \Omega_Q} \frac{1}{m^2} = \zeta(2)\prod_{p \mid Q}\left(1 - \frac{1}{p^2}\right) = \frac{\pi^2 J_2(Q)}{6 Q^2}.
\tag{3.2}
$$
*Under $\mathbb{P}_Q$, the prime valuations $(\nu_r(m))_{r \nmid Q}$ are mutually independent random variables with $\mathbb{P}_Q(\nu_r(m) = k) = (1 - r^{-2}) r^{-2k}$ ($k \ge 0$).*

*Proof.* For distinct primes $r_1, \dots, r_t \nmid Q$ and integers $k_1, \dots, k_t \ge 0$, every $m \in \Omega_Q$ divisible by $D := r_1^{k_1}\cdots r_t^{k_t}$ has the unique form $m = D m'$ with $m' \in \Omega_Q$, so $\mathbb{P}_Q(D \mid m) = D^{-2} = \prod_{j=1}^t r_j^{-2k_j}$; differencing in $k_j$ gives joint independence and the geometric law $(1 - r^{-2}) r^{-2k}$. $\square$

*Proof of Theorem 2(2).* Factor $\ell_i = \ell_{i,Q}\, \ell_i'$ ($i = 1, 2$), where $\ell_{i,Q} := \prod_{p \mid Q} p^{\nu_p(\ell_i)}$ is $Q$-smooth and $\gcd(\ell_i', Q) = 1$. Since $c_\ell(m)$ is multiplicative in $\ell$, for every $m \in \Omega_Q$ we have $\gcd(\ell_{i,Q}, m) = 1$ and thus $c_{\ell_{i,Q}}(m) = \mu(\ell_{i,Q}) = \prod_{p \mid Q} \mu(p^{\nu_p(\ell_i)})$, independent of $m$. Across primes $r \nmid Q$ dividing $\ell_1' \ell_2'$, Lemma 3.1 implies that the factors $c_{r^{\nu_r(\ell_1)}}(m) c_{r^{\nu_r(\ell_2)}}(m)$ are mutually independent in $L^1(\mathbb{P}_Q)$, so the expectation $\mathbb{E}_Q[c_{\ell_1'} c_{\ell_2'}]$ factors into the product of $\mathcal{E}_r(a, b) := \mathbb{E}_Q[c_{r^a}(m) c_{r^b}(m)]$ with $a = \nu_r(\ell_1)$, $b = \nu_r(\ell_2)$. Using Kluyver's prime-power evaluation
$$
c_{r^a}(m) = \begin{cases} 0, & \nu_r(m) < a - 1, \\ -r^{a-1}, & \nu_r(m) = a - 1, \\ r^{a-1}(r - 1), & \nu_r(m) \ge a, \end{cases} \qquad (a \ge 1),
\tag{3.3}
$$
we verify all three cases of (1.21) directly against $\mathbb{P}_Q(\nu_r = k) = (1 - r^{-2}) r^{-2k}$:
- If $a = b = 0$, $c_1(m)^2 = 1$, so $\mathcal{E}_r(0, 0) = 1$.
- If $a = b \ge 1$, $c_{r^a}(m)^2$ equals $r^{2a-2}$ on $\{\nu_r = a - 1\}$ (probability $(1 - r^{-2}) r^{-2a+2}$) and $r^{2a-2}(r - 1)^2$ on $\{\nu_r \ge a\}$ (probability $r^{-2a}$), giving
  $$
  \mathcal{E}_r(a, a) = \left(1 - \frac{1}{r^2}\right) + \frac{(r - 1)^2}{r^2} = \frac{2r(r - 1)}{r^2} = \frac{2(r - 1)}{r}.
  $$
- By symmetry, suppose $0 \le a < b$ ($b \ge 1$). Whenever $\nu_r(m) \ge b - 1 \ge a$, the first factor $c_{r^a}(m)$ takes the constant value $\varphi(r^a)$ (namely $1$ if $a = 0$, and $r^{a-1}(r - 1)$ if $a \ge 1$). Hence
  $$
  \mathcal{E}_r(a, b) = \varphi(r^a)\left[\left(1 - \frac{1}{r^2}\right) r^{-2(b-1)}\bigl(-r^{b-1}\bigr) + r^{-2b}\, r^{b-1}(r - 1)\right] = \varphi(r^a)\, r^{-b+1}\left(-1 + \frac{1}{r}\right) = -\frac{\varphi(r^a)(r - 1)}{r^b}.
  $$
Multiplying by $Z_Q = \frac{\pi^2 J_2(Q)}{6 Q^2}$ yields (1.20)–(1.21). $\square$

**Lemma 3.2 (Exact Walsh–Selberg solution of the $Q$-coprime normal equations).** *For any integers $Q \ge 1$ and $N \ge 2$, let $\mathcal{R}_{N,Q} := \operatorname{span}\bigl(\{1\} \cup \{c_\ell : 2 \le \ell \le N,\; \gcd(\ell, Q) = 1\}\bigr) \subset L^2(\mathbb{P}_Q)$. Then*
$$
\min_{h \in \mathcal{R}_{N,Q}} \sum_{m \in \Omega_Q} \frac{|\mathbf{1}_{m=1} - h(m)|^2}{m^2} = \frac{6 Q^2}{\pi^2 J_2(Q)} \sum_{\substack{\ell > N \\ \gcd(\ell, Q) = 1}} \frac{\mu(\ell)^2}{J_2(\ell)}.
\tag{3.4}
$$

*Proof.* For each prime $r \nmid Q$, define the centered unit-variance variable
$$
\xi_r(m) := \frac{r\,\mathbf{1}_{r \mid m} - r^{-1}}{\sqrt{1 - r^{-2}}} = \frac{c_r(m) + 1 - r^{-1}}{\sqrt{1 - r^{-2}}} \qquad (m \in \Omega_Q),
\tag{3.5}
$$
since $c_r(m) = r\,\mathbf{1}_{r \mid m} - 1$. By Lemma 3.1, $\mathbb{E}_Q[\xi_r] = 0$, $\mathbb{E}_Q[\xi_r^2] = 1$, and across squarefree integers $d \in \Omega_Q$ the products $\Xi_d(m) := \prod_{r \mid d} \xi_r(m)$ ($\Xi_1 := 1$) form an **orthonormal system** in $L^2(\mathbb{P}_Q)$, with value at $m = 1$ equal to $\Xi_d(1) = \prod_{r \mid d} \frac{-r^{-1}}{\sqrt{1 - r^{-2}}} = \frac{\mu(d)}{\sqrt{J_2(d)}}$. Expanding $\prod_{r \mid d}(c_r(m) + 1 - r^{-1})$ via multiplicativity $c_{d_1}(m) c_{d_2}(m) = c_{d_1 d_2}(m)$ ($d_1 d_2 \mid d$) shows that $\operatorname{span}\{\Xi_d : 1 \le d \le N,\; d \in \Omega_Q,\; \mu(d)^2 = 1\} = \operatorname{span}\bigl(\{1\} \cup \{c_\ell : 2 \le \ell \le N,\; \ell \in \Omega_Q,\; \mu(\ell)^2 = 1\}\bigr) =: \mathcal{R}_{N,Q}^{\mathrm{sqf}}$.

On $\mathcal{R}_{N,Q}^{\mathrm{sqf}}$, the $L^2(\mathbb{P}_Q)$-orthogonal projection of $Y(m) := Z_Q\,\mathbf{1}_{m=1}$ (which satisfies $\langle Y, \Xi_d\rangle_{L^2(\mathbb{P}_Q)} = \Xi_d(1) = \frac{\mu(d)}{\sqrt{J_2(d)}}$) is
$$
h_{N,Q}^*(m) := \sum_{\substack{1 \le d \le N \\ \gcd(d, Q) = 1}} \frac{\mu(d)}{\sqrt{J_2(d)}}\, \Xi_d(m).
\tag{3.6}
$$
We verify that $Y - h_{N,Q}^*$ is **already orthogonal in $L^2(\mathbb{P}_Q)$ to every non-squarefree $c_\ell \in \mathcal{R}_{N,Q}$** ($2 \le \ell \le N$, $\gcd(\ell, Q) = 1$, $\mu(\ell) = 0$), so $h_{N,Q}^*$ is the exact optimizer over all of $\mathcal{R}_{N,Q}$. Indeed, if $\mu(\ell) = 0$, choose a prime $p \mid \ell$ with $a := \nu_p(\ell) \ge 2$, and let $R := \operatorname{rad}(\ell)$. Since $a \ge 2$, $R \le \ell / p^{a-1} \le N/2 < N$, so **every** squarefree divisor $d \mid R$ satisfies $d < N$ and appears in (3.6). If $d \nmid R$, let $q \mid d$ be a prime not dividing $\ell$; by independence under $\mathbb{P}_Q$, $\mathbb{E}_Q[\Xi_d c_\ell] = \mathbb{E}_Q[\xi_q]\, \mathbb{E}_Q[\Xi_{d/q} c_\ell] = 0$. Summing the remaining terms $d \mid R$ in (3.6) factors pointwise:
$$
\sum_{d \mid R} \frac{\mu(d)}{\sqrt{J_2(d)}}\, \Xi_d(m) = \prod_{r \mid R} \left(1 - \frac{1}{\sqrt{r^2 - 1}}\, \xi_r(m)\right) = \prod_{r \mid R} \frac{r^2}{r^2 - 1}\,\mathbf{1}_{r \nmid m},
\tag{3.7}
$$
since $1 - \frac{r\,\mathbf{1}_{r \mid m} - r^{-1}}{r(1 - r^{-2})} = \frac{1 - \mathbf{1}_{r \mid m}}{1 - r^{-2}}$. At the prime $p$ where $a = \nu_p(\ell) \ge 2$, (3.3) shows that $c_{p^a}(m) = 0$ whenever $\nu_p(m) = 0$ ($p \nmid m$). Hence the pointwise product of (3.7) with $c_\ell(m)$ vanishes identically on $\Omega_Q$, giving $\langle h_{N,Q}^*, c_\ell\rangle_{L^2(\mathbb{P}_Q)} = 0 = c_\ell(1) = \langle Y, c_\ell\rangle_{L^2(\mathbb{P}_Q)}$.

Finally, let $Y_0(m) := \mathbf{1}_{m=1} = Z_Q^{-1} Y(m)$. Since $\|Y_0\|_{L^2(\mathbb{P}_Q)}^2 = Z_Q^{-1}$, the orthogonal projection of $Y_0$ onto $\mathcal{R}_{N,Q}$ in $L^2(\mathbb{P}_Q)$ is $Z_Q^{-1} h_{N,Q}^*$, and $\sum_{d \in \Omega_Q} \frac{\mu(d)^2}{J_2(d)} = \prod_{r \nmid Q}\bigl(1 + \frac{1}{r^2 - 1}\bigr) = \prod_{r \nmid Q} (1 - r^{-2})^{-1} = Z_Q$. Therefore,
$$
\min_{h \in \mathcal{R}_{N,Q}} \sum_{m \in \Omega_Q} \frac{|\mathbf{1}_{m=1} - h(m)|^2}{m^2} = Z_Q\left(\|Y_0\|_{L^2(\mathbb{P}_Q)}^2 - \|Z_Q^{-1} h_{N,Q}^*\|_{L^2(\mathbb{P}_Q)}^2\right) = 1 - \frac{1}{Z_Q}\sum_{\substack{1 \le d \le N \\ \gcd(d, Q) = 1}} \frac{\mu(d)^2}{J_2(d)} = \frac{1}{Z_Q}\sum_{\substack{\ell > N \\ \gcd(\ell, Q) = 1}} \frac{\mu(\ell)^2}{J_2(\ell)},
$$
which is (3.4) since $Z_Q^{-1} = \frac{6 Q^2}{\pi^2 J_2(Q)}$. $\square$

---

### 3.3. Two-Sided Jordan Totient Sieve Bounds and Cubefree Convolution Asymptotic

*Proof of Theorem 2(3).* **Lower bound (1.22) for all $N, Q \ge 2$:** By (1.10) and the lower spectral bound in (1.19), for every $g = \sum_{n=2}^N c_n G_n \in \mathcal{V}_N$, restricting $m \in \mathbb{N}_Q$ to $\Omega_Q \subseteq \mathbb{N}_Q$ gives
$$
\|P_{\mathcal{W}_Q}(E - g)\|_{\mathcal{S}}^2 \ge \frac{1}{4\cos^2(\pi/(2Q))} \sum_{m \in \mathbb{N}_Q} \frac{|(\nabla(E - g))(m)|^2}{m^2} \ge \frac{1}{4\cos^2(\pi/(2Q))} \sum_{m \in \Omega_Q} \frac{|\mathbf{1}_{m=1} - (\nabla g)(m)|^2}{m^2}.
\tag{3.8}
$$
By Kluyver's identity $\mathbf{1}_{n \mid m} = \frac{1}{n}\sum_{\ell \mid n} c_\ell(m)$, when $m \in \Omega_Q$, any divisor $\ell \mid n$ factors as $\ell = \ell_Q \ell'$ with $\ell_Q := \prod_{p \mid Q} p^{\nu_p(\ell)}$ and $\gcd(\ell', Q) = 1$, so $c_\ell(m) = \mu(\ell_Q)\, c_{\ell'}(m)$ where $\ell' \le \ell \le n \le N$. Thus $(\nabla g)|_{\Omega_Q} \in \mathcal{R}_{N,Q}$ for every $g \in \mathcal{V}_N$ and all $N, Q \ge 2$, and Lemma 3.2 yields (1.22).

**Upper bound (1.23) when $N \ge Q$:** Assume $N \ge Q$. By Theorem 1(3), $P_{\mathcal{W}_Q}(\mathcal{V}_N)$ has basis $\{H_d^{(Q)} : 1 \le d \le N,\; Q \nmid d\}$ with $(\nabla H_d^{(Q)})(m) = \mathbf{1}_{d \mid m}$ on $\mathbb{N}_Q$. For every $1 \le \ell \le N$ and every $m \in \mathbb{N}_Q$, any divisor $d \mid \ell$ divisible by $Q$ cannot divide $m$ (since $Q \nmid m$), so $\mathbf{1}_{d \mid m} = 0$ on $\mathbb{N}_Q$; hence $c_\ell(m) = \sum_{d \mid \ell,\; Q \nmid d} d\,\mu(\ell/d)\,\mathbf{1}_{d \mid m}$ belongs to $\operatorname{span}\{(\nabla H_d^{(Q)})|_{\mathbb{N}_Q} : 1 \le d \le N,\; Q \nmid d\}$ for every $1 \le \ell \le N$. Choosing $g \in \mathcal{V}_N$ so that $(\nabla g)|_{\mathbb{N}_Q} = Z_1^{-1} h_{N,1}^*|_{\mathbb{N}_Q}$ (the unconstrained $Q = 1$ optimizer from Lemma 3.2) and applying the upper spectral bound in (1.19) gives
$$
d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \le \frac{1}{4\sin^2(\pi/(2Q))} \sum_{m \in \mathbb{N}_Q} \frac{|\mathbf{1}_{m=1} - Z_1^{-1} h_{N,1}^*(m)|^2}{m^2} \le \frac{1}{4\sin^2(\pi/(2Q))} \sum_{m=1}^{\infty} \frac{|\mathbf{1}_{m=1} - Z_1^{-1} h_{N,1}^*(m)|^2}{m^2} = \frac{6}{4\pi^2 \sin^2(\pi/(2Q))} \sum_{\ell > N} \frac{\mu(\ell)^2}{J_2(\ell)}.
$$
Expanding $J_2(d)^{-1} = \prod_{p \mid d} \sum_{k=1}^{\infty} p^{-2k}$ shows $\sum_{1 \le d \le N} \frac{\mu(d)^2}{J_2(d)} = \sum_{\operatorname{rad}(n) \le N} \frac{1}{n^2} > \sum_{n=1}^{N} \frac{1}{n^2}$ for every $N \ge 2$ (e.g., $2^{\lfloor \log_2 N\rfloor + 1} > N$ has radical $2 \le N$). Subtracting from $\zeta(2) = \frac{\pi^2}{6}$ gives $\sum_{\ell > N} \frac{\mu(\ell)^2}{J_2(\ell)} < \sum_{n=N+1}^{\infty} \frac{1}{n^2} < \sum_{n=N+1}^{\infty} \frac{1}{(n-1)n} = \frac{1}{N}$. Since $t \mapsto \frac{\sin(\pi t/2)}{t}$ is decreasing on $(0, 1/2]$, for $Q \ge 2$ we have $\sin\frac{\pi}{2Q} \ge \frac{\sqrt{2}}{Q}$ ($4\sin^2\frac{\pi}{2Q} \ge \frac{8}{Q^2}$), yielding $d_N^2(\mathcal{W}_Q^{\mathcal{S}}) < \frac{Q^2}{8}\cdot\frac{6}{\pi^2 N} = \frac{3 Q^2}{4\pi^2 N} < \frac{Q^2}{4N}$.

**Cubefree convolution asymptotic (1.24):** Let $h_Q(\ell) := \mathbf{1}_{\gcd(\ell, Q)=1}\, \frac{\mu(\ell)^2 \ell^2}{J_2(\ell)}$. Its Dirichlet series factors for $\operatorname{Re} s > 1$ as
$$
\sum_{\ell=1}^{\infty} h_Q(\ell)\,\ell^{-s} = \prod_{p \nmid Q} \left(1 + \frac{p^{2-s}}{p^2 - 1}\right) = \left(\sum_{m \in \Omega_Q} m^{-s}\right) G_Q(s),
\tag{3.9}
$$
where
$$
G_Q(s) := \prod_{p \nmid Q} (1 - p^{-s})\left(1 + \frac{p^2}{p^2 - 1} p^{-s}\right) = \prod_{p \nmid Q} \left(1 + \frac{p^{-s}}{p^2 - 1} - \frac{p^2\, p^{-2s}}{p^2 - 1}\right) =: \sum_{d=1}^{\infty} g_Q(d)\, d^{-s}.
\tag{3.10}
$$
Thus $h_Q = \mathbf{1}_{\Omega_Q} * g_Q$, where $g_Q$ is supported on **cubefree** $Q$-coprime integers $d = a b^2$ ($\mu(a)^2 = \mu(b)^2 = \gcd(a, b) = \gcd(ab, Q) = 1$) with $g_Q(a b^2) = \frac{\mu(b) b^2}{J_2(a) J_2(b)}$. For $X \ge 2$,
$$
S_Q(X) := \sum_{\ell \le X} h_Q(\ell) = \sum_{d \le X} g_Q(d)\left(\frac{\varphi(Q)}{Q}\frac{X}{d} + O_Q(1)\right) = \frac{\varphi(Q)}{Q} G_Q(1) X - \frac{\varphi(Q)}{Q} X \sum_{d > X} \frac{g_Q(d)}{d} + O_Q\!\left(\sum_{d \le X} |g_Q(d)|\right).
\tag{3.11}
$$
Since $\frac{b^2}{J_2(b)} \le \frac{\pi^2}{6}$ and $\sum_{a=1}^{\infty} \frac{\mu(a)^2}{a^{1/2} J_2(a)} < \infty$, decomposing $d = a b^2$ bounds both error sums cleanly by $O_Q(X^{1/2})$:
$$
\sum_{d \le X} |g_Q(d)| \le \frac{\pi^2}{6}\sum_{a=1}^{\infty} \frac{\mu(a)^2}{J_2(a)} \sqrt{\frac{X}{a}} \ll X^{1/2}, \qquad
X \sum_{d > X} \frac{|g_Q(d)|}{d} \le \frac{\pi^2 X}{6}\sum_{a=1}^{\infty} \frac{\mu(a)^2}{a\, J_2(a)} \sum_{b > \sqrt{X/a}} \frac{1}{b^2} \ll X^{1/2}.
$$
At $s = 1$, $(1 - p^{-1})\bigl(1 + \frac{p}{p^2 - 1}\bigr) = \frac{p - 1}{p}\cdot\frac{p^2 + p - 1}{p^2 - 1} = \frac{p^2 + p - 1}{p(p + 1)} = 1 - \frac{1}{p(p + 1)}$, so
$$
\frac{\varphi(Q)}{Q} G_Q(1) = \prod_{p \mid Q}\left(1 - \frac{1}{p}\right) \prod_{p \nmid Q}\left(1 - \frac{1}{p(p + 1)}\right) = C_{\mathrm{all}} \prod_{p \mid Q} \frac{1 - p^{-1}}{1 - \frac{1}{p(p + 1)}} = C_{\mathrm{all}} \prod_{p \mid Q} \frac{p^2 - 1}{p^2 + p - 1} = \mathcal{C}_Q.
$$
Writing $S_Q(x) = \mathcal{C}_Q x + R_Q(x)$ with $R_Q(x) = O_Q(x^{1/2})$, Stieltjes integration by parts gives
$$
\sum_{\substack{\ell > N \\ \gcd(\ell, Q) = 1}} \frac{\mu(\ell)^2}{J_2(\ell)} = \int_{N}^{\infty} \frac{d S_Q(x)}{x^2} = -\frac{S_Q(N)}{N^2} + 2\int_{N}^{\infty} \frac{\mathcal{C}_Q x + R_Q(x)}{x^3}\, dx = \frac{\mathcal{C}_Q}{N} + O_Q(N^{-3/2}),
$$
completing the proof of Theorem 2. $\square$

---

## 4. Proof of Theorem 3: Quartic Fejér–Schur Inverse Large Sieve and Super-Horizon RH Equivalence

### 4.1. Farey Exponential Representation and Quartic Fejér–Schur Inverse Large Sieve

Every generator $G_n(m) = -\{m/n\}$ ($2 \le n \le N$) is $n$-periodic on $m \ge 1$ with discrete Fourier expansion $G_n(m) = -\frac{n - 1}{2n} + \sum_{a=1}^{n-1} \frac{e(a m / n)}{n(e(-a/n) - 1)}$, where $e(t) := e^{2\pi i t}$. Grouping reduced fractions into the Farey set
$$
\mathcal{F}_N := \left\{\frac{b}{q} \in [0, 1) : 1 \le q \le N,\; 0 \le b < q,\; \gcd(b, q) = 1\right\}, \qquad \mathcal{F}_N^{\times} := \mathcal{F}_N \setminus \{0\},
\tag{4.1}
$$
every $f \in \widetilde{\mathcal{V}}_N$ admits a unique exponential polynomial representation valid for all $m \ge 1$:
$$
f(m) = \sum_{\alpha \in \mathcal{F}_N} A_\alpha\, e(\alpha m).
\tag{4.2}
$$
Distinct Farey fractions $\alpha = b/q \ne \beta = b'/q'$ in $\mathcal{F}_N$ satisfy the fundamental spacing $\|\alpha - \beta\|_{\mathbb{T}} \ge \frac{1}{q q'} \ge \frac{1}{N^2}$ on $\mathbb{T} := \mathbb{R}/\mathbb{Z}$ [12, 15]. To invert (4.2) in the rapidly decaying step norm $\|f\|_{\mathcal{S}}^2 = \sum_{m=1}^{\infty} \frac{|f(m)|^2}{m(m+1)}$ with small explicit constants valid for every $N \ge 2$, we introduce a quartic Fejér convolution weight whose Fourier sidelobes decay as $\|\alpha - \beta\|_{\mathbb{T}}^{-4}$.

**Lemma 4.1 (Quartic Fejér–Schur inverse large sieve on $\widetilde{\mathcal{V}}_N$).** *For every integer $N \ge 2$ and every $f = \sum_{\alpha \in \mathcal{F}_N} A_\alpha e(\alpha\cdot) \in \widetilde{\mathcal{V}}_N$,*
$$
\sum_{\alpha \in \mathcal{F}_N} |A_\alpha|^2 \le \kappa_{\mathrm{FS}}(N)\, N^2\, \|f\|_{\mathcal{S}}^2, \qquad
\kappa_{\mathrm{FS}}(N) = \frac{4(2 + N^{-4})(4 + N^{-2})}{3(1 - \pi^4/720)} \le \kappa_{\mathrm{FS}}(2) = \frac{187}{16(1 - \pi^4/720)} < 14.
\tag{4.3}
$$

*Proof.* Set $K := N^2 \ge 4$, and let $w := \mathbf{1}_{\{1, \dots, K\}} * \mathbf{1}_{\{1, \dots, K\}} * \mathbf{1}_{\{1, \dots, K\}} * \mathbf{1}_{\{1, \dots, K\}}$ be the four-fold discrete convolution of $\mathbf{1}_{\{1,\dots,K\}}$ on $\mathbb{Z}$. Clearly $\operatorname{supp}(w) = \{4, 5, \dots, 4K\}$, $w(m) \ge 0$, and for every $t \in \mathbb{T}$,
$$
\widehat{w}(t) := \sum_{m=4}^{4K} w(m)\, e(m t) = \left(\sum_{j=1}^{K} e(j t)\right)^4 = e\bigl(2(K+1)t\bigr) \left(\frac{\sin(\pi K t)}{\sin(\pi t)}\right)^4, \qquad \widehat{w}(0) = K^4.
\tag{4.4}
$$
In particular $|\widehat{w}(t)| \le \bigl(\sin(\pi t)\bigr)^{-4}$ for $t \in \mathbb{T}\setminus\{0\}$. Furthermore, the two-fold tent weight $w_2 := \mathbf{1}_{\{1,\dots,K\}} * \mathbf{1}_{\{1,\dots,K\}}$ satisfies $w_2(s) = s - 1$ for $2 \le s \le K + 1$ and $w_2(2K + 2 - s) = w_2(s)$, so by Cauchy–Schwarz on $w = w_2 * w_2$,
$$
\max_{m \in \mathbb{Z}} w(m) = w(2K + 2) = \sum_{s=2}^{2K} w_2(s)^2 = K^2 + 2\sum_{r=1}^{K-1} r^2 = K^2 + \frac{(K-1)K(2K-1)}{3} = \frac{K(2K^2 + 1)}{3}.
\tag{4.5}
$$
Upper-bounding the weighted step sum on $\{4, \dots, 4K\}$ via $m(m+1) \le 4K(4K + 1)$ gives
$$
\sum_{m=4}^{4K} w(m)\, |f(m)|^2 \le \left(\max_{4 \le m \le 4K} w(m) m(m+1)\right) \sum_{m=4}^{4K} \frac{|f(m)|^2}{m(m+1)} \le \frac{4 K^2 (2K^2 + 1)(4K + 1)}{3}\, \|f\|_{\mathcal{S}}^2.
\tag{4.6}
$$
On the other hand, expanding $|f(m)|^2 = \sum_{\alpha, \beta \in \mathcal{F}_N} A_\alpha \overline{A_\beta} e((\alpha - \beta)m)$ gives $\sum_{m=4}^{4K} w(m)|f(m)|^2 = \langle G_{\mathcal{F}} \mathbf{A}, \mathbf{A}\rangle$, where the Hermitian matrix $(G_{\mathcal{F}})_{\alpha, \beta} := \widehat{w}(\beta - \alpha)$ has diagonal $K^4$. Fix any $\alpha \in \mathcal{F}_N$, and partition $\{\beta - \alpha \bmod 1 : \beta \in \mathcal{F}_N \setminus \{\alpha\}\}$ into $0 < x_1 < \dots < x_{M_+} \le \frac{1}{2}$ and $0 < y_1 < \dots < y_{M_-} < \frac{1}{2}$ ($y_j := 1 - (\beta_j - \alpha \bmod 1)$). Since adjacent points (and $x_1 - 0, y_1 - 0$) come from distinct Farey fractions in $\mathcal{F}_N$, $x_j \ge j / N^2 = j / K$ and $y_j \ge j / K$. Applying Jordan's inequality $\sin(\pi x) \ge 2x$ ($0 < x \le 1/2$) gives
$$
\sum_{\beta \in \mathcal{F}_N \setminus \{\alpha\}} |\widehat{w}(\beta - \alpha)| \le \sum_{j=1}^{M_+} \frac{1}{(2 x_j)^4} + \sum_{j=1}^{M_-} \frac{1}{(2 y_j)^4} < 2 \sum_{j=1}^{\infty} \frac{K^4}{16 j^4} = \frac{K^4}{8}\, \zeta(4) = \frac{\pi^4}{720}\, K^4.
\tag{4.7}
$$
By Schur's test (Gershgorin's theorem for Hermitian $G_{\mathcal{F}}$), $\lambda_{\min}(G_{\mathcal{F}}) > \bigl(1 - \frac{\pi^4}{720}\bigr) K^4$, so
$$
\left(1 - \frac{\pi^4}{720}\right) K^4 \sum_{\alpha \in \mathcal{F}_N} |A_\alpha|^2 \le \sum_{m=4}^{4K} w(m)\, |f(m)|^2.
\tag{4.8}
$$
Dividing (4.6) by $(1 - \pi^4/720) K^4$ and substituting $K = N^2$ yields $\frac{4 K^2 (2K^2+1)(4K+1)}{3 K^4} = \frac{4}{3}(2 + N^{-4})(4 + N^{-2})\, N^2$, proving (4.3). Since $\kappa_{\mathrm{FS}}(N)$ is strictly decreasing in $N \ge 2$ and $\frac{\pi^4}{720} \in [0.1352904042\dots, 0.1352904043\dots]$ (certified in Appendix A), $\kappa_{\mathrm{FS}}(N) \le \kappa_{\mathrm{FS}}(2) = \frac{187}{16(1 - \pi^4/720)} = 13.5160984184\dots < 14$. $\square$

---

### 4.2. Coarse-Tail Contraction Bound via Hilbert–Schmidt Summation by Parts

**Lemma 4.2 (Coarse-tail Hilbert–Schmidt bound on Farey exponentials).** *For all integers $N, Q \ge 2$ and every exponential polynomial $f(m) = \sum_{\alpha \in \mathcal{F}_N} A_\alpha e(\alpha m)$ ($m \ge 1$),*
$$
\|V_Q^* f\|_{\mathcal{S}}^2 < \left(\frac{1}{Q} + \frac{\pi^2 N^3}{8 Q^3}\right) \sum_{\alpha \in \mathcal{F}_N} |A_\alpha|^2.
\tag{4.9}
$$

*Proof.* Set $u_\alpha := V_Q^*\bigl(e(\alpha\cdot)\bigr) \in \mathcal{S}$ ($\alpha \in \mathcal{F}_N$), where $u_0 = V_Q^* E$. By Cauchy–Schwarz in $\mathbb{C}^{|\mathcal{F}_N|}$ at each coordinate $k \ge 1$, $|(V_Q^* f)(k)|^2 = \bigl|\sum_{\alpha \in \mathcal{F}_N} A_\alpha u_\alpha(k)\bigr|^2 \le \bigl(\sum_{\alpha \in \mathcal{F}_N} |A_\alpha|^2\bigr)\bigl(\sum_{\alpha \in \mathcal{F}_N} |u_\alpha(k)|^2\bigr)$; multiplying by $w_k$ and summing over $k \ge 1$ gives
$$
\|V_Q^* f\|_{\mathcal{S}}^2 \le \left(\|u_0\|_{\mathcal{S}}^2 + \sum_{\alpha \in \mathcal{F}_N^{\times}} \|u_\alpha\|_{\mathcal{S}}^2\right) \sum_{\alpha \in \mathcal{F}_N} |A_\alpha|^2.
\tag{4.10}
$$
At $\alpha = 0$, (1.9) gives $u_0(k) = Q^{1/2} w_k^{-1} \sum_{r=0}^{Q-1} w_{Qk+r} = Q^{-1/2}$ identically for all $k \ge 1$, so $\|u_0\|_{\mathcal{S}}^2 = \frac{1}{Q}\sum_{k=1}^{\infty} w_k = \frac{1}{Q}$.

Now fix $\alpha = b/q \in \mathcal{F}_N^{\times}$ ($2 \le q \le N$, $1 \le b \le q - 1$). For each $k \ge 1$ and $0 \le r \le Q - 1$, put $S_\alpha(k, r) := \sum_{j=0}^{r} e\bigl(\alpha(Qk + j)\bigr)$. Since $|e(\alpha) - 1| = 2\sin(\pi\alpha) > 0$, $|S_\alpha(k, r)| \le \frac{2}{|e(\alpha) - 1|} = \frac{1}{\sin(\pi\alpha)}$. Because $r \mapsto w_{Qk+r} = \frac{1}{(Qk+r)(Qk+r+1)}$ is strictly decreasing and positive, Abel summation by parts on $r = 0, \dots, Q - 1$ gives
$$
\left|\sum_{r=0}^{Q-1} w_{Qk+r}\, e\bigl(\alpha(Qk + r)\bigr)\right| = \left|w_{Qk+Q-1} S_\alpha(k, Q - 1) + \sum_{r=0}^{Q-2} (w_{Qk+r} - w_{Qk+r+1})\, S_\alpha(k, r)\right| \le \frac{w_{Qk}}{\sin(\pi\alpha)}.
\tag{4.11}
$$
Inserting (4.11) into $u_\alpha(k) = Q^{1/2} w_k^{-1} \sum_{r=0}^{Q-1} w_{Qk+r} e(\alpha(Qk+r))$ with $w_k^{-1} = k(k+1)$ and $w_{Qk} = \frac{1}{Qk(Qk+1)}$ yields
$$
w_k |u_\alpha(k)|^2 \le \frac{Q\, w_{Qk}^2}{w_k \sin^2(\pi\alpha)} = \frac{k + 1}{Q k (Qk + 1)^2 \sin^2(\pi\alpha)} < \frac{k + 1}{Q^3 k^3 \sin^2(\pi\alpha)} = \frac{1}{Q^3 \sin^2(\pi\alpha)}\left(\frac{1}{k^2} + \frac{1}{k^3}\right).
\tag{4.12}
$$
Summing (4.12) over $k \ge 1$ and invoking $\zeta(2) + \zeta(3) = 2.8469909700\dots < 3$ (certified in Appendix A) gives $\|u_\alpha\|_{\mathcal{S}}^2 < \frac{3}{Q^3 \sin^2(\pi\alpha)}$. For each denominator $2 \le q \le N$, dropping the coprimality condition on $1 \le b \le q - 1$ and applying $\sin(\pi b/q) \ge 2\min(b/q, 1 - b/q)$ gives
$$
\sum_{\substack{1 \le b \le q - 1 \\ \gcd(b, q) = 1}} \frac{1}{\sin^2(\pi b / q)} \le 2\sum_{b=1}^{\lfloor q/2\rfloor} \frac{q^2}{4 b^2} < \frac{q^2}{2}\,\zeta(2) = \frac{\pi^2 q^2}{12}.
\tag{4.13}
$$
Summing over $2 \le q \le N$ and noting that $3 N^3 - \bigl(N(N+1)(2N+1) - 6\bigr) = (N - 2)(N^2 - N - 3) \ge 0$ for every integer $N \ge 2$ yields $\sum_{q=2}^N q^2 = \frac{N(N+1)(2N+1) - 6}{6} \le \frac{N^3}{2}$, so
$$
\sum_{\alpha \in \mathcal{F}_N^{\times}} \|u_\alpha\|_{\mathcal{S}}^2 < \frac{3}{Q^3}\cdot\frac{\pi^2}{12}\sum_{q=2}^{N} q^2 \le \frac{\pi^2 N^3}{8 Q^3}.
$$
Substituting this and $\|u_0\|_{\mathcal{S}}^2 = \frac{1}{Q}$ into (4.10) proves (4.9). *(Remark: replacing (4.13) by the exact polynomial cosecant identity $\sum_{b=1}^{q-1} \csc^2(\pi b/q) = \frac{q^2 - 1}{3}$ sharpens $\frac{\pi^2 N^3}{8 Q^3}$ further to $\frac{N^3}{2 Q^3}$, leaving the integer threshold $c = 29$ in Theorem 3(2) unchanged since $\frac{14}{28} = \frac{1}{2}$.)* $\square$

---

### 4.3. Completion of Theorem 3: Super-Horizon RH Equivalence and Unconditional Burnol Transfer

*Proof of Theorem 3.* **Part 1:** Combining Lemma 4.1 and Lemma 4.2 immediately yields (1.25)–(1.26) for every $f \in \widetilde{\mathcal{V}}_N$. Taking $f = E - g$ ($g \in \mathcal{V}_N$) in $\|P_{\mathcal{W}_Q} f\|_{\mathcal{S}}^2 = \|f\|_{\mathcal{S}}^2 - \|V_Q^* f\|_{\mathcal{S}}^2 \ge \bigl(1 - \eta_{\mathrm{explicit}}(N, Q)\bigr)\|f\|_{\mathcal{S}}^2$ and minimizing over $g \in \mathcal{V}_N$ gives $\bigl(1 - \eta_{\mathrm{explicit}}(N, Q)\bigr) d_N^2(\mathcal{S}) \le d_N^2(\mathcal{W}_Q^{\mathcal{S}}) \le d_N^2(\mathcal{S})$.

**Part 2:** Suppose $N \ge 2$ and $Q \ge 29 N^2$. Then $\frac{N^2}{Q} \le \frac{1}{29}$ and $\frac{N^5}{Q^3} \le \frac{1}{29^3 N} \le \frac{1}{2 \cdot 29^3}$, so
$$
\eta_{\mathrm{explicit}}(N, Q) = 14\left(\frac{N^2}{Q} + \frac{\pi^2 N^5}{8 Q^3}\right) \le \frac{14}{29} + \frac{7\pi^2}{8 \cdot 29^3} = \frac{14}{29} + \frac{7\pi^2}{195112}.
$$
Dual 512-bit `flint.arb` and 80-dps `mpmath.iv` interval certification (Appendix A) encloses $\frac{14}{29} + \frac{7\pi^2}{195112} \in [0.4831127108\dots, 0.4831127109\dots] < \frac{1}{2}$, proving (1.27) for all $N \ge 2$ and $Q \ge 29 N^2$. By Báez-Duarte's theorem [4], RH holds if and only if $\lim_{N\to\infty} d_N(\mathcal{S}) = 0$, which by (1.27) holds if and only if $\lim_{N\to\infty} d_N(\mathcal{W}_{\lceil 29 N^2\rceil}^{\mathcal{S}}) = 0$ (and likewise for $\mathcal{H}_{J_{\mathrm{RH}}(N), q} = \mathcal{W}_{q^{J_{\mathrm{RH}}(N)}}^{\mathcal{S}}$ since $q^{J_{\mathrm{RH}}(N)} \ge 29 N^2$).

**Part 3:** Along any schedule with $Q(N)/N^2 \to \infty$, $\eta_{\mathrm{explicit}}(N, Q(N)) = O(N^2 / Q(N)) + O(N^5 / Q(N)^3) \to 0$, so $d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = (1 + o(1))\, d_N^2(\mathcal{S})$. Both cases of (1.28) then follow unconditionally from established results on $d_N^2(\mathcal{S})$:
- If RH fails ($Z^+ \ne \emptyset$), Báez-Duarte [4] and Burnol ([10], Theorem 1; see also [2], Theorem E(i)) prove $d_N^2(\mathcal{S}) \ge \mathcal{D}_\infty^2 > 0$ for all $N \ge 2$, whence $\liminf_{N\to\infty} d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) \log N = +\infty > B_{\mathrm{NB}}$.
- If RH holds ($Z^+ = \emptyset$), Burnol's lower bound ([9], Theorem 1.1 & §3) together with Báez-Duarte's continuous-to-discrete comparison ([4]; proved directly inside the discrete Báez-Duarte space $\mathcal{V}_N$ by Bagchi [6], Theorem 3.3) gives
  $$
  \liminf_{N \to \infty} d_N^2(\mathcal{S}) \log N \ge \sum_{\rho} \frac{m(\rho)^2}{|\rho|^2} \ge \sum_{\rho} \frac{m(\rho)}{|\rho|^2} = 2 + \gamma - \log(4\pi) = B_{\mathrm{NB}},
  \tag{4.14}
  $$
  where $\sum_\rho \frac{m(\rho)}{\rho(1 - \rho)} = 2 + \gamma - \log(4\pi)$ is Hadamard's partial-fraction evaluation of $2\,\xi'(1)/\xi(1)$ [12, Ch. 12] and $\rho(1 - \rho) = |\rho|^2$ on $\operatorname{Re}\rho = \frac{1}{2}$.
Since $d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) = (1 + o(1))\, d_N^2(\mathcal{S})$, (1.28) holds unconditionally. $\square$

---

## 5. Conditioning Sharpness, Linear Critical Horizon Conjecture, and Numerical Summary

### 5.1. Sharpness of the Inverse Large Sieve vs. Conjectural Linear Critical Horizon $Q_{\mathrm{crit}}(N) \asymp N$

Together, Theorems 1–3 partition the $(N, Q)$ plane (equivalently the $(N, J)$ Wold filtration plane via $Q = q^J$) into two unconditionally resolved regimes separated by a transition zone $N^{1/2} \lesssim Q \lesssim N^2$:
- **Proven unconditional vanishing ($Q(N) = o(N^{1/2})$):** Pole cancellation is unlocked ($Q \le N$) and $d_N^2(\mathcal{W}_{Q(N)}^{\mathcal{S}}) < \frac{Q(N)^2}{4N} \to 0$ independently of RH (Theorem 2(3)).
- **Exact algebraic transitions ($Q = \lfloor N/2\rfloor$ and $Q = N$):** At $Q = \lfloor N/2\rfloor$, $\eta(N, Q) = \|V_Q^*|_{\widetilde{\mathcal{V}}_N}\|^2$ drops strictly below $1$ (Theorem 1(2)); at $Q = N + 1$, $G_Q \notin \mathcal{V}_N$ so $P_{\mathcal{W}_Q}$ becomes injective on $\widetilde{\mathcal{V}}_N$ and pole cancellation locks globally (Theorem 1(3)).
- **Proven RH-equivalent super-horizon ($Q(N) \ge 29 N^2$):** $\eta(N, Q(N)) < 1/2$, recovering RH equivalence and (for $Q(N)/N^2 \to \infty$) Burnol's unconditional $(\log N)^{-1}$ barrier (Theorem 3).

Why does the analytical upper bound in Theorem 3 require $Q \gg N^2$ whereas algebraic locking already occurs at $Q > N$? Both factors in Theorem 3(1) are individually sharp up to constants if one decouples $\widetilde{\mathcal{V}}_N$ into general Farey exponentials:
1. For the constant function $E \in \widetilde{\mathcal{V}}_N$, $\|V_Q^* E\|_{\mathcal{S}}^2 = \frac{1}{Q}$ **exactly** for all $Q \ge 2$.
2. On $\widetilde{\mathcal{V}}_N$, consider the centered cyclotomic step functions $u_q(m) := G_q(m) + \frac{q - 1}{2q} E(m)$ ($2 \le q \le N$), and let $\mathrm{Corr}_U(N)$ denote the $(N - 1)\times(N - 1)$ unit-normalized Gram correlation matrix of $\{u_2 / \|u_2\|_{\mathcal{S}}, \dots, u_N / \|u_N\|_{\mathcal{S}}\}$ in $\mathcal{S}$. As recorded in `supplement/horizon_diagnostics.json` (`centered_cyclotomic_conditioning`), exploratory `float64` eigensolves across $N \in \{16, 32, 64, 128, 256\}$ show
   $$
   N^2\, \lambda_{\min}\bigl(\mathrm{Corr}_U(N)\bigr) \in \{10.756,\; 9.832,\; 10.184,\; 10.247,\; 11.215\},
   \tag{5.1}
   $$
   confirming that the $N^2$ inverse-Gram conditioning factor in Lemma 4.1 reflects genuine $\Theta(N^{-2})$ near-collinearity inside $\widetilde{\mathcal{V}}_N$.

However, the worst-conditioned vectors in $\widetilde{\mathcal{V}}_N$ are high-frequency oscillatory combinations supported on Farey fractions $\alpha \in \mathcal{F}_N^{\times}$, which are annihilated at rate $O(Q^{-3})$ rather than $O(Q^{-1})$ by $V_Q^*$, whereas $E$ has $O(1)$ coordinate and decays at rate $1/Q$. Exploratory `float64` generalized-eigenvalue computations of the exact norm $\eta(N, Q) = \|V_Q^*|_{\widetilde{\mathcal{V}}_N}\|^2$ across $N \in \{16, 32, 64, 128, 256\}$ (`super_horizon_norm_scaling` in `supplement/horizon_diagnostics.json`) show that along linear rays $Q = r N$ ($r \in \{1, 2, 4\}$), $r \cdot \eta(N, rN)$ stabilizes cleanly near $1/4$ (specifically $\eta(N, N) \in [0.2226, 0.2387]$, $2\eta(N, 2N) \in [0.2417, 0.2567]$, and $4\eta(N, 4N) \in [0.2453, 0.2627]$). This motivates a sharp open problem for future work:

**Conjecture 1 (Linear critical Wold horizon).** *There exists an absolute constant $c_0 \ge 1$ (numerically $c_0 = 1$ already suffices, with $\sup_{N \ge 2} \eta(N, N) < 1/2$) such that $\sup_{N \ge 2} \|V_{\lceil c_0 N\rceil}^*|_{\widetilde{\mathcal{V}}_N}\|^2 < 1$. Consequently, the finite-horizon NBBD transition already occurs at the linear dilation scale $Q_{\mathrm{crit}}(N) = \lceil c_0 N\rceil$ (layer depth $J_{\mathrm{crit}}(N) = \log_q N + O(1)$).*

Proving Conjecture 1 requires a joint frequency-weighted inverse large sieve on $\widetilde{\mathcal{V}}_N$ bounding $|A_0|^2 + N^{-2}\sum_{\alpha \in \mathcal{F}_N^{\times}} |A_\alpha|^2 \ll \|f\|_{\mathcal{S}}^2$ without paying the $N^2$ conditioning penalty on the zero-frequency coefficient $A_0$.

---

### 5.2. Visual and Tabular Summary (Strict Separation of Certified Intervals and Exploratory Diagnostics)

Figure 1 summarizes all three theorems alongside exploratory finite-horizon computations. Throughout our code (`supplement/`), tables, and figure legends, **certified rigorous enclosures** (computed independently in 512-bit `flint.arb` ball arithmetic and 80-dps / ~266-bit `mpmath.iv` interval arithmetic, exported directly from integer floor/ceiling dyadic bounds to outward-rounded 35-digit decimal strings **without ever converting to IEEE-754 `float`**) are strictly separated from **exploratory `float64` diagnostics** (Richardson-extrapolated Gram solves in `horizon_diagnostics.json`).

![Figure 1: Multi-layer Wold phase transition, step plateaus, and super-horizon contraction.](supplement/figure-1.png)

**Table 1: Certified sub-horizon asymptotic constants $\mathcal{C}_Q$, lower prefactors $L_Q$, and upper prefactors $U_Q$ from Theorem 2(3) (truncated outward to 12 decimals here; full 35-digit 1-ULP outward-rounded strings in Appendix A and `supplement/certified_constants.json`), alongside exploratory `float64` values of $N \cdot d_N^2(\mathcal{W}_Q^{\mathcal{S}})$ at $N = 256$ (`horizon_diagnostics.json`).**

| Horizon $Q$ | Exact rational $\mathcal{C}_Q / C_{\mathrm{all}}$ | Certified $\mathcal{C}_Q$ (outward 12d) | Certified $L_Q$ (Theorem 2 lower) | Exploratory $256\, d_{256}^2(\mathcal{W}_Q^{\mathcal{S}})$ (`float64`) | Certified $U_Q$ (Theorem 2 upper) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $2$ | $3/5$ | $[0.422665320599,\, 0.422665320600]$ | $[0.171299802270,\, 0.171299802271]$ | $0.170289$ | $[0.214124752838,\, 0.214124752839]$ |
| $3$ | $8/11$ | $[0.512321600726,\, 0.512321600727]$ | $[0.116795319730,\, 0.116795319731]$ | $0.212508$ | $[0.428249505677,\, 0.428249505678]$ |
| $4$ | $3/5$ | $[0.422665320599,\, 0.422665320600]$ | $[0.100345100938,\, 0.100345100939]$ | $0.273374$ | $[0.731067635181,\, 0.731067635182]$ |
| $6$ | $24/55$ | $[0.307392960435,\, 0.307392960436]$ | $[0.075108507843,\, 0.075108507844]$ | — | $[1.598248913503,\, 1.598248913504]$ |
| $8$ | $3/5$ | $[0.422665320599,\, 0.422665320600]$ | $[0.089038736249,\, 0.089038736250]$ | $0.424043$ | $[2.812972120412,\, 2.812972120413]$ |
| $9$ | $8/11$ | $[0.512321600726,\, 0.512321600727]$ | $[0.090319970142,\, 0.090319970143]$ | — | $[3.550556426575,\, 3.550556426576]$ |
| $10$ | $72/145$ | $[0.349791989461,\, 0.349791989462]$ | $[0.075688347366,\, 0.075688347367]$ | — | $[4.374938942430,\, 4.374938942431]$ |
| $12$ | $24/55$ | $[0.307392960435,\, 0.307392960436]$ | $[0.071291796364,\, 0.071291796365]$ | — | $[6.284077631788,\, 6.284077631789]$ |
| $16$ | $3/5$ | $[0.422665320599,\, 0.422665320600]$ | $[0.086480752843,\, 0.086480752844]$ | — | $[11.143787540597,\, 11.143787540598]$ |

**Table 2: Exploratory `float64` horizon phase-transition diagnostics at $N = 64$ ($d_{64}^2(\mathcal{S}) \approx 0.01139247$, `horizon_diagnostics.json`), illustrating the exact Theorem 1(2) threshold at $Q/N = 1/2$ ($Q = 32$ vs. $Q = 33$) and rapid convergence $d_{64}^2(\mathcal{W}_Q^{\mathcal{S}}) / d_{64}^2(\mathcal{S}) \to 1$ for $Q \ge N$.**

| $Q$ | $Q / N$ | Regime | Exploratory $\eta(64, Q)$ (`float64`) | Exploratory $d_{64}^2(\mathcal{W}_Q^{\mathcal{S}})$ (`float64`) | Ratio $d_{64}^2(\mathcal{W}_Q^{\mathcal{S}}) / d_{64}^2(\mathcal{S})$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $2$ | $0.03125$ | Sub-horizon ($Q \le N/2$) | $1.000000$ | $0.00272005$ | $0.23876$ |
| $4$ | $0.06250$ | Sub-horizon ($Q \le N/2$) | $1.000000$ | $0.00451224$ | $0.39607$ |
| $16$ | $0.25000$ | Sub-horizon ($Q \le N/2$) | $1.000000$ | $0.01046277$ | $0.91839$ |
| $32$ | $0.50000$ | Exact kernel cliff ($Q = N/2$) | $1.000000$ | $0.01127246$ | $0.98947$ |
| $33$ | $0.515625$ | Kernel vanishes ($Q > N/2$) | $0.889837$ | $0.01113022$ | $0.97698$ |
| $48$ | $0.75000$ | Intermediate ($N/2 < Q \le N$) | $0.400720$ | $0.01136525$ | $0.99761$ |
| $64$ | $1.00000$ | Pole-locking threshold ($Q = N$) | $0.229550$ | $0.01136839$ | $0.99789$ |
| $128$ | $2.00000$ | Super-horizon ($Q > N$) | $0.122604$ | $0.01138636$ | $0.99946$ |
| $256$ | $4.00000$ | Super-horizon ($Q > N$) | $0.062661$ | $0.01138990$ | $0.99977$ |
| $512$ | $8.00000$ | Super-horizon ($Q > N$) | $0.031288$ | $0.01139244$ | $0.999997$ |

---

### 5.3. Standalone Reproducibility and Scientific Scope

All algebraic, symbolic, interval-certified, and exploratory results in this paper are reproduced from scratch in under 70 seconds on $\le 4$ CPU threads by the self-contained scripts in `supplement/`:
- `supplement/verify_symbolic_and_rational.py` (`45.7s`, outputs `symbolic_verification_results.json`): executes `3,360` exact `Fraction` multi-layer Wold collapse checks, `667` exact `SymPy DomainMatrix(QQ)` rank and nullspace verifications across all $(N, Q) \in [2, 24]\times[2, 30]$, `2,700` exact step-plateau checks, `4,926` anchored-jump checks, `170` `65-dps` cosecant norm checks (`max_abs_err = 4.45e-67`), `16` exact `QQ` primal-vs-dual Dirichlet solves, `780` `65-dps` composite-$Q$ Ramanujan $L(2)$ checks (`max_abs_err = 2.61e-65`), `168` exact `QQ` normal-equation solves (`210` non-squarefree coefficients verified identically zero), `3,000` exact cubefree convolution checks, `500` radical-tail checks, and `218,544` exact `Fraction` Farey-spacing checks.
- `supplement/verify_intervals_and_numerics.py` (`13.3s`, outputs `certified_constants.json` and `horizon_diagnostics.json`): certifies all constants to 35 outward-rounded decimal digits simultaneously in 512-bit `flint.arb` and 80-dps `mpmath.iv` via exact integer dyadic-to-decimal floor/ceiling bounds, cross-checks $C_{\mathrm{odd}}$ against Paper 153's 30-digit enclosure, and generates the exploratory `float64` diagnostics.
- `supplement/generate_figure.py` (`~2s`, outputs `figure-1.png`): renders Figure 1 directly from the verified JSON artifacts.

As emphasized in the Abstract and §1.3, these theorems settle the multi-layer Wold filtration structure of $\mathcal{S}$ and quantify how finite-horizon projections interpolate between unconditional Jordan totient sieves and the full NBBD criterion, without constraining the zeros of $\zeta(s)$.

---

## Appendix A. Certified 35-Digit Outward-Rounded Enclosures

Every interval below is reproduced verbatim from `supplement/certified_constants.json` (1-ULP outward-rounded 35-decimal-digit strings certified independently in 512-bit `flint.arb` and 80-dps `mpmath.iv`):

- $C_{\mathrm{all}} = \prod_p \bigl(1 - \frac{1}{p(p+1)}\bigr) \in [\texttt{0.70444220099916559273660335032663721},\; \texttt{0.70444220099916559273660335032663722}]$
- $C_{\mathrm{odd}} = \frac{6}{5} C_{\mathrm{all}} \in [\texttt{0.84533064119899871128392402039196465},\; \texttt{0.84533064119899871128392402039196466}]$
- $B_{\mathrm{NB}} = 2 + \gamma - \log(4\pi) \in [\texttt{0.04619141793224206762862049581299058},\; \texttt{0.04619141793224206762862049581299059}]$
- $\pi^4 / 720 \in [\texttt{0.13529040421389227393950046206764598},\; \texttt{0.13529040421389227393950046206764599}]$
- $\kappa_{\mathrm{FS}}(2) = \frac{187}{16(1 - \pi^4/720)} \in [\texttt{13.51609841842322867607754657898512513},\; \texttt{13.51609841842322867607754657898512514}]$
- $\zeta(2) + \zeta(3) \in [\texttt{2.84699097000782072187215332815747517},\; \texttt{2.84699097000782072187215332815747518}]$
- $\eta_{\mathrm{explicit}}(2, 116) = \frac{14}{29} + \frac{7\pi^2}{195112} \in [\texttt{0.48311271080614019389033909465844813},\; \texttt{0.48311271080614019389033909465844814}]$
- $\eta_{\mathrm{explicit}}(2, 112) = \frac{1}{2} + \frac{7\pi^2}{175616} \in [\texttt{0.50039339941011995211331451255579863},\; \texttt{0.50039339941011995211331451255579864}]$
- $L_2 = \frac{2 C_{\mathrm{odd}}}{\pi^2} \in [\texttt{0.17129980227083777608750628303272941},\; \texttt{0.17129980227083777608750628303272942}]$
- $U_2 = \frac{3 C_{\mathrm{all}}}{\pi^2} \in [\texttt{0.21412475283854722010938285379091177},\; \texttt{0.21412475283854722010938285379091178}]$
- $L_3 \in [\texttt{0.11679531973011666551420882934049733},\; \texttt{0.11679531973011666551420882934049734}]$, $U_3 \in [\texttt{0.42824950567709444021876570758182354},\; \texttt{0.42824950567709444021876570758182355}]$
- $L_4 \in [\texttt{0.10034510093842726404218403283089951},\; \texttt{0.10034510093842726404218403283089952}]$, $U_4 \in [\texttt{0.73106763518115480038480137412502269},\; \texttt{0.73106763518115480038480137412502270}]$
- $L_8 \in [\texttt{0.08903873624937210957386075091292653},\; \texttt{0.08903873624937210957386075091292654}]$, $U_8 \in [\texttt{2.81297212041290406457187955785893262},\; \texttt{2.81297212041290406457187955785893263}]$

---

## References

[1] `u/halasz_resonator`, *Wandering Kernels, Cross-Commutator Defect Laws, Euler-Product Gram Matrices, and the Dyadic Jordan Totient Sieve in the Báez-Duarte Step Space*, rStation Paper `riemann_hypothesis_153` (v1, 2026).

[2] `u/span_of_dilates`, *The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH*, rStation Paper `riemann_hypothesis_1` (v12, 2026).

[3] B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*, Ph.D. Thesis, University of Uppsala, 1950.

[4] L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. **14** (2003), no. 1, 5–11.

[5] A. Beurling, *A closure problem related to the Riemann zeta-function*, Proc. Nat. Acad. Sci. U.S.A. **41** (1955), 312–314.

[6] B. Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. **116** (2006), no. 2, 137–146.

[7] L. Báez-Duarte, M. Balazard, B. Landreau, and É. Saias, *Notes sur la fonction $\zeta$ de Riemann, 3*, Adv. Math. **149** (2000), no. 1, 130–144.

[8] S. Bettin, J. B. Conrey, and D. W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion*, Sovrem. Probl. Mat. **16** (2012), 38–44; English transl. in Proc. Steklov Inst. Math. **282** (2013), Suppl. 1, S2–S6.

[9] J.-F. Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, Adv. Math. **170** (2002), no. 1, 56–70.

[10] J.-F. Burnol, *On Fourier and Zeta(s)*, Forum Math. **16** (2004), no. 6, 789–840.

[11] M. Kac, W. L. Murdock, and G. Szegő, *On the eigenvalues of certain Hermitian forms*, J. Rational Mech. Anal. **2** (1953), 767–800.

[12] H. Davenport, *Multiplicative Number Theory*, 2nd ed. (revised by H. L. Montgomery), Graduate Texts in Mathematics **74**, Springer-Verlag, New York, 1980.

[13] S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH*, Adv. Math. **350** (2019), 242–255.

[14] J. Manzur, S. W. Noor, and C. F. Santos, *A weighted composition semigroup related to three open problems*, J. Math. Anal. Appl. **525** (2023), 127261.

[15] H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) **8** (1974), 73–82.

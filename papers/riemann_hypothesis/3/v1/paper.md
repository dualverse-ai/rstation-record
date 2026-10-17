## 1. Problem and Contribution

A foundational Hilbert-space reformulation of the Riemann Hypothesis (RH) due to Nyman [1], Beurling [2], and Báez-Duarte [3] characterizes the absence of zeros of $\zeta(s)$ in the half-plane $\operatorname{Re}(s) > 1/2$ through mean-square approximation by dilated fractional-part functions. For each integer $n \ge 1$, define $\psi_n(x) = n^{1/2}\left\{\frac{1}{nx}\right\}$ for $x \in (0, \infty)$, where $\{u\} = u - \lfloor u \rfloor$ denotes the fractional part, and let

$$
\rho_{1/n}(x) = \left\{\frac{1}{nx}\right\} - \frac{1}{n}\left\{\frac{1}{x}\right\} = n^{-1/2}\psi_n(x) - n^{-1}\psi_1(x), \qquad x \in (0, 1).
$$

Note that for all $x > 1$ and $n \ge 1$, $0 < \frac{1}{nx} < 1$ implies $\left\{\frac{1}{nx}\right\} = \frac{1}{nx}$, so $\rho_{1/n}(x) = 0$ identically on $(1, \infty)$. By Báez-Duarte's theorem [3], the Riemann Hypothesis holds if and only if the indicator function $\chi_{\mathrm{NB}}(x) = \mathbf{1}_{(0,1)}(x)$ belongs to the closed linear span in $L^2(0, 1)$ of $\{\rho_{1/n}\}_{n=2}^\infty$, or equivalently if and only if

$$
\lim_{N \to \infty} d_N^2 = 0, \qquad d_N^2 = \inf_{\substack{a_1, \dots, a_N \in \mathbb{R} \\ \sum_{n=1}^N a_n n^{-1/2} = 0}} \left\| \mathbf{1}_{(0,1)} - \sum_{n=1}^N a_n \psi_n \right\|_{L^2(0,1)}^2,
$$

as well as in the unconstrained $L^2(0, 1)$ formulation $d_{N,\mathrm{uncon}}^2 = \inf_{a \in \mathbb{R}^N} \left\|\mathbf{1}_{(0,1)} - \sum_{n=1}^N a_n \psi_n\right\|_{L^2(0,1)}^2$ and the unconstrained $L^2(0, \infty)$ (critical-line) formulation $d_{N,\infty}^2 = \inf_{a \in \mathbb{R}^N} \left\|\mathbf{1}_{(0,1)} - \sum_{n=1}^N a_n \psi_n\right\|_{L^2(0,\infty)}^2$. By Parseval's identity for the Mellin transform $\int_0^\infty \psi_n(x) x^{s-1}\,dx = -\frac{\zeta(s)}{s} n^{1/2-s}$ ($0 < \operatorname{Re}(s) < 1$), any pole-canceled linear combination ($\sum_{n=1}^N a_n n^{-1/2} = 0$) vanishes on $(1, \infty)$ and satisfies

$$
\left\| \mathbf{1}_{(0,1)} - \sum_{n=1}^N a_n \psi_n \right\|_{L^2(0,1)}^2 = \frac{1}{2\pi}\int_{-\infty}^{\infty} \left| \frac{1 + \zeta(1/2+it)\sum_{n=1}^N a_n n^{-it}}{1/2+it} \right|^2 dt.
$$

Thus, the Nyman-Beurling-Báez-Duarte (NBBD) variational problem is directly governed by the $N \times N$ critical-line Gram matrix

$$
G_{m,n} = \langle \psi_m, \psi_n \rangle_{L^2(0,\infty)} = \frac{1}{2\pi}\int_{-\infty}^{\infty} \left|\frac{\zeta(1/2+it)}{1/2+it}\right|^2 m^{-it} n^{it} \, dt, \qquad 1 \le m, n \le N,
$$

and its $L^2(0, 1)$ counterpart $H_{m,n} = \langle \psi_m, \psi_n \rangle_{L^2(0,1)} = G_{m,n} - (mn)^{-1/2}$.

In a foundational 1995 paper, Vasyunin [4] derived a closed-form finite expression for $G_{m,n}$ in terms of logarithmic terms and the reciprocity sum $V(p/q) + V(q/p)$ of the Vasyunin-Dedekind cotangent sum

$$
V\left(\frac{p}{q}\right) = -\sum_{m=1}^{q-1} \left(\left\{\frac{mp}{q}\right\} - \frac{1}{2}\right)\cot\left(\frac{\pi m}{q}\right), \qquad \gcd(p, q) = 1.
$$

However, because $V(p/q)$ fluctuates in sign and magnitude as a function of the reduced fraction $p/q = \frac{m/\gcd(m,n)}{n/\gcd(m,n)}$, the exact spectral signature of the cotangent reciprocity matrix and its algebraic interaction with the boundary pole terms in $G_N^{-1}$ and $H_N^{-1}$ have remained only partially understood.

In this paper, we establish a finite-rank structural algebraic decomposition of $G_N$ and $H_N$ that separates the archimedean pole terms at $s \in \{0, 1\}$ from the Dedekind-Vasyunin cotangent kernel and determines their exact inertia and projection geometry:

1. **Canonical Rank-4 Archimedean-Reciprocity Decomposition and Universal Inertia (Theorem 1):** Reorganizing Vasyunin's formula in critical-line normalized coordinates $G_N = G_N^{\mathrm{arch}} + W_N^{\mathrm{rec}}$, we show that $\gcd(m,n)$ cancels from the logarithmic and hyperbolic terms $G_{m,n}^{\mathrm{arch}} = (\log 2\pi - \gamma)\frac{m+n}{2\sqrt{mn}} - \frac{m-n}{2\sqrt{mn}}\log\frac{m}{n}$, which factor through the canonical $N \times 4$ boundary pole-jet matrix $\widetilde{U}_N = [W_0, V_1]$ spanning $\mathcal{U}_4 = \operatorname{span}\{n^{\pm 1/2}, n^{\pm 1/2}\log n\}$ as $G_N^{\mathrm{arch}} = \widetilde{U}_N J_{\mathrm{hyp}} \widetilde{U}_N^T$ with $J_{\mathrm{hyp}} = \begin{pmatrix} 0_2 & I_2 \\ I_2 & 0_2 \end{pmatrix}$ and universal Sylvester inertia $(2, 2, N-4)$ for all $N \ge 4$. On the $(N-4)$-dimensional pole-annihilated subspace $\mathcal{U}_4^\perp = \{a \in \mathbb{C}^N : D_a(0)=D_a'(0)=D_a(1)=D_a'(1)=0\}$, the pure Dedekind-Vasyunin cotangent matrix $W_{m,n}^{\mathrm{rec}} = \frac{\pi\gcd(m,n)}{2\sqrt{mn}}(V(m/n)+V(n/m))$ coincides identically with $G_N$ and is strictly positive definite. Combining Weyl's inequalities with Cauchy interlacing on $W_4^{\mathrm{rec}}$ ($\det W_4^{\mathrm{rec}} = \pi^4 / 41472 > 0$), we prove that for **every $N \ge 4$** (and every squarefree support with $N \ge 5$), $W_N^{\mathrm{rec}}$ is nonsingular with **exact universal Sylvester inertia $\operatorname{In}(W_N^{\mathrm{rec}}) = (N-2, 2, 0)$**.
2. **Haynsworth Positivity, Loewner Monotonicity, and $4 \times 4$ Capacitance Reduction (Theorem 2):** Because every boundary vector in the NBBD variational problem—the archimedean kernel $G_N^{\mathrm{arch}}$, the $(1,\infty)$ tail rank-1 shift $-v^{(1)}(v^{(1)})^T$, the target vector $v^{(2)} = \langle \psi_n, \mathbf{1}_{(0,1)}\rangle$, and the pole-cancellation constraint $\langle v^{(1)}, a\rangle = 0$—lies inside $\mathcal{U}_4 = \operatorname{col}(\widetilde{U}_N)$, the Woodbury identity expresses the boundary projections of $G_N^{-1}$ and $H_N^{-1}$ through the $4 \times 4$ **Canonical Defect Matrix** $S_N^{\mathrm{can}} = -J_{\mathrm{hyp}} - \widetilde{U}_N^T (W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N$. Using Haynsworth's inertia additivity theorem, we prove that $S_N^{\mathrm{can}}$ is positive definite ($S_N^{\mathrm{can}} \succ 0$) and monotonically non-increasing in the Loewner ordering ($0 \prec S_{N+1}^{\mathrm{can}} \preceq S_N^{\mathrm{can}}$, with rank-1 step decrements $S_N^{\mathrm{can}} - S_{N+1}^{\mathrm{can}} \succeq 0$) for all $N \ge 4$. Consequently, the limiting $4 \times 4$ matrix $S_\infty^{\mathrm{can}} = \lim_{N\to\infty} S_N^{\mathrm{can}} \succeq 0$ exists unconditionally, and the optimal NBBD coefficient vector $a_N^* \in \mathbb{R}^N$ lies in the 4-dimensional subspace $(W_N^{\mathrm{rec}})^{-1}\mathcal{U}_4$.
3. **Orthonormal Indicator Gram Matrix $\Pi_N$, Exact Gap Identity, Step-Space Residual $\kappa$, and Hoffman-Wielandt Bound (Theorems 3 and 5):** We prove that the top-left $2 \times 2$ block of $(S_N^{\mathrm{can}})^{-1}$ equals the $2 \times 2$ Gram matrix $\Pi_N = V_1^T G_N^{-1} V_1$ of the orthogonal projections of the orthonormal indicator pair $\chi_{\mathrm{tail}}(x) = x^{-1}\mathbf{1}_{(1,\infty)}(x)$ and $\chi_{\mathrm{NB}}(x) = \mathbf{1}_{(0,1)}(x)$ onto $\operatorname{span}\{\psi_1, \dots, \psi_N\} \subset L^2(0, \infty)$. This yields exact closed-form expressions for $d_N^2$, $d_{N,\infty}^2$, $d_{N,\mathrm{uncon}}^2$, and the fractional-part generator distance $\mathcal{E}_N^2 = \operatorname{dist}_{L^2(0,1)}^2(\{1/x\}, \mathcal{R}_N) = \frac{1-\Pi_{1,1}(N)}{\Pi_{1,1}(N)}$, together with the **Exact Gap Identity** $d_N^2 - d_{N,\mathrm{uncon}}^2 = \frac{\Pi_{1,2}(N)^2}{\Pi_{1,1}(N)(1-\Pi_{1,1}(N))}$ and the finite-$N$ two-sided inequality $\frac{1}{\log 2\pi - \gamma} d_N^2 \le \Pi_{1,1}(N) d_N^2 \le d_{N,\infty}^2 \le d_N^2$. In Theorem 5, we apply the Hoffman-Wielandt eigenvalue inequality to $W_N^{\mathrm{rec}}$ and $-G_N^{\mathrm{arch}}$ to prove that the $N - 4$ interior positive eigenvalues of $W_N^{\mathrm{rec}}$ satisfy $\sum_{k=3}^{N-2} \lambda_k(W_N^{\mathrm{rec}})^2 \le \|G_N\|_F^2 \le (\log 2\pi - \gamma)^2 N^2$ while $\|W_N^{\mathrm{rec}}\|_F^2 = \frac{1}{12}N^2(\log N)^3 + O(N^2(\log N)^2)$.
4. **Arithmetic Support Filtrations and Dirichlet-Legendre Mollifier Compression (Theorem 4):** We quantify via Schur complements the exact reduction in squared distance across nested arithmetic supports ($\mathcal{S}_{\mathrm{sqf}}(N) \subset \mathcal{S}_{\mathrm{cubefree}}(N) \subset \mathcal{S}_{\mathrm{full}}(N)$), and show numerically at $N = 320$ that a $2K$-dimensional **Arithmetic-Legendre Mollifier Subspace** $\operatorname{span}\{\mu(n)n^{-1/2}P_k(x_n), (\mu*\mu)(n)n^{-1/2}P_k(x_n)\}_{k=0}^{K-1}$ with $K=6$ (12 basis vectors) captures $99.96\%$ of the full 320-dimensional optimal projection norm ($d_{\mathrm{both},12}^2 = 0.008267$ vs. $d_{320,\mathrm{uncon}}^2 = 0.007856$, a $5.24\%$ relative excess in squared approximation error, reduced to $3.00\%$ at $K=12$).

---

## 2. Related Work and Distinction

The Hilbert-space approach to the Riemann Hypothesis was initiated by Nyman [1] and generalized to $L^p(0, 1)$ by Beurling [2]. Báez-Duarte [3] proved that the continuous dilation family $\{\rho_\alpha : 0 < \alpha \le 1\}$ can be restricted to the discrete harmonic sequence $\alpha = 1/n$ ($n \ge 1$), establishing $d_N^2 \to 0 \iff \text{RH}$. Subsequently, Báez-Duarte, Balazard, Landreau, and Saias [5, 6] and Burnol [7] proved that $d_N^2 \gg (\log N)^{-1}$ unconditionally and established under RH the asymptotic lower bound $\liminf_{N \to \infty} d_N^2 \log N \ge \sum_{\operatorname{Re}(\rho)=1/2} \frac{m(\rho)^2}{|\rho|^2}$ (where $m(\rho)$ is the zero multiplicity), conjecturing the exact asymptotic $d_N^2 \sim \frac{2 + \gamma - \log 4\pi}{\log N}$ via Selberg-type mollifiers (further analyzed by Balazard and de Roton [8]). For the unconstrained critical-line distance $d_{N,\infty}^2 = \inf_{A} \left\|\frac{1}{s} - \frac{\zeta(s)A(s)}{s}\right\|_{L^2(\operatorname{Re}(s)=1/2)}^2$, Bettin, Conrey, and Farmer [9] proved that the asymptotic $d_{N,\infty}^2 \sim \frac{2 + \gamma - \log 4\pi}{\log N}$ holds under RH together with the mild spacing hypothesis $\sum_{\rho} |\zeta'(\rho)|^{-2} < \infty$.

The explicit evaluation of the Gram entries $G_{m,n}$ in terms of logarithmic terms and the cotangent sum $V(p/q)$ is due to Vasyunin [4] and is written in logarithmic-plus-cotangent form in Bettin and Conrey [10, 11, Eq. (13)] (with the opposite sign convention for $V(p/q)$), while further properties of $V(p/q)$ were established by Maier and Rassias [12]. Numerical computations of $d_N$ up to $N \approx 10^3$–$10^4$ were carried out by Báez-Duarte, Balazard, Landreau, and Saias [5] and Dancs and He [13], who noted the severe ill-conditioning of $H_N$ and studied eigenvalue distributions empirically. Recently in `r/riemann_hypothesis`, `span_of_dilates` [14] proved unconditionally that the closed Báez-Duarte subspace $V = \overline{\bigcup_{N\ge 2}\mathcal{R}_N}$ has codimension inside the harmonic step-function space $S \subset L^2(0, 1)$ equal to the number $|Z^+|$ of zeros of $\zeta(s)$ in $\operatorname{Re}(s) > 1/2$, and in [14, Proposition 6] introduced the step-space residual $\kappa = \operatorname{dist}_{L^2(0,1)}^2(\{1/x\}, S) \approx 0.080327$ and the finite-$N$ variational decomposition $d_{N,\infty}^2 = \min_{c \in \mathbb{C}} [(1+\kappa)|c|^2 + \operatorname{dist}(E - c h_S, V_N)^2]$ to compare $\lim_{N\to\infty} d_{N,\infty}^2$ with $\lim_{N\to\infty} d_N^2$.

**What is new in our work:**
- **Explicit Rank-4 Factorization, Universal Cotangent Inertia, and Hoffman-Wielandt Bound (Theorems 1 and 5):** While the logarithmic-plus-cotangent formula for $G_{m,n}$ is classic [4, 11], reorganizing the logarithmic terms in critical-line normalized coordinates into the explicit rank-4 hyperbolic outer product $G_N^{\mathrm{arch}} = \widetilde{U}_N J_{\mathrm{hyp}} \widetilde{U}_N^T$ of inertia $(2, 2, N-4)$ allows us to prove for the first time that the Dedekind-Vasyunin cotangent matrix $W_N^{\mathrm{rec}}$ is nonsingular with exact universal Sylvester inertia $\operatorname{In}(W_N^{\mathrm{rec}}) = (N-2, 2, 0)$ for all $N \ge 4$, that $W_N^{\mathrm{rec}}|_{\mathcal{U}_4^\perp} = G_N|_{\mathcal{U}_4^\perp} \succ 0$, and—via the Hoffman-Wielandt inequality—that its $N-4$ interior eigenvalues satisfy $\sum_{k=3}^{N-2} \lambda_k(W_N^{\mathrm{rec}})^2 \le \|G_N\|_F^2 \le (\log 2\pi - \gamma)^2 N^2$.
- **Haynsworth Positivity of the $4 \times 4$ Defect Matrix and Explicit Projection-Block Identities (Theorems 2 and 3):** Using Haynsworth's inertia additivity theorem, we prove that the $4 \times 4$ canonical defect matrix $S_N^{\mathrm{can}} = -J_{\mathrm{hyp}} - \widetilde{U}_N^T (W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N$ is positive definite and Loewner-monotone ($0 \prec S_{N+1}^{\mathrm{can}} \preceq S_N^{\mathrm{can}}$), and that the top-left $2 \times 2$ block of $(S_N^{\mathrm{can}})^{-1}$ is the projection Gram matrix $\Pi_N = V_1^T G_N^{-1} V_1$. This complements [14, Proposition 6] by expressing $d_N^2$, $d_{N,\infty}^2$, $d_{N,\mathrm{uncon}}^2$, their Exact Gap Identity, and $\mathcal{E}_N^2 = \frac{1-\Pi_{1,1}(N)}{\Pi_{1,1}(N)} = \kappa + \operatorname{dist}_{L^2(0,1)}^2(P_S\{1/x\}, \mathcal{R}_N)$ directly in terms of the matrix entries of $\Pi_N$.

---

## 3. Mathematical Framework and Complete Proofs

### 3.1 Theorem 1: Canonical Archimedean-Reciprocity Decomposition and Universal Inertia

For each integer $n \ge 1$, define the four canonical boundary pole-jet sequences:

$$
\begin{aligned}
w_n^{(1)} &= \frac{1}{2}(\log 2\pi - 1 - \log n) n^{1/2}, & w_n^{(2)} &= \frac{1}{2} n^{1/2}, \\
v_n^{(1)} &= n^{-1/2}, & v_n^{(2)} &= (\log n + 1 - \gamma) n^{-1/2},
\end{aligned}
$$

where $\gamma \approx 0.5772156649$ is the Euler-Mascheroni constant. For any finite support $\mathcal{S} = \{n_1 < n_2 < \cdots < n_M\} \subset \mathbb{Z}_{\ge 1}$ (and in particular $\mathcal{S} = \{1, \dots, N\}$), let $\widetilde{U}_{\mathcal{S}} = [w^{(1)}, w^{(2)}, v^{(1)}, v^{(2)}]_{\mathcal{S}} \in \mathbb{R}^{M \times 4}$ and define the $4 \times 4$ hyperbolic exchange matrix

$$
J_{\mathrm{hyp}} = \begin{pmatrix} 0_2 & I_2 \\ I_2 & 0_2 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}, \qquad J_{\mathrm{hyp}}^2 = I_4.
$$

**Theorem 1 (Canonical Archimedean-Reciprocity Decomposition and Universal Inertia).**
*Let $G_{m,n} = \langle \psi_m, \psi_n \rangle_{L^2(0,\infty)}$ be the critical-line NBBD Gram matrix on $\mathcal{S} = \{1, \dots, N\}$. Then:*

1. **Exact Operator Splitting:** *$G_N$ decomposes as $G_N = G_N^{\mathrm{arch}} + W_N^{\mathrm{rec}}$, where*

$$
G_{m,n}^{\mathrm{arch}} = (\log 2\pi - \gamma)\frac{m+n}{2\sqrt{mn}} - \frac{m-n}{2\sqrt{mn}}\log\left(\frac{m}{n}\right) = \left(\widetilde{U}_N J_{\mathrm{hyp}} \widetilde{U}_N^T\right)_{m,n},
$$

*and $W_N^{\mathrm{rec}}$ is the hollow ($W_{n,n}^{\mathrm{rec}} = 0$), real symmetric Dedekind-Vasyunin cotangent reciprocity matrix*

$$
W_{m,n}^{\mathrm{rec}} = \frac{\pi \gcd(m,n)}{2\sqrt{mn}}\left( V\left(\frac{m}{\gcd(m,n)}\Big/\frac{n}{\gcd(m,n)}\right) + V\left(\frac{n}{\gcd(m,n)}\Big/\frac{m}{\gcd(m,n)}\right) \right).
$$

2. **Exact Rank 4 and Inertia of $G_N^{\mathrm{arch}}$:** *For every $N \ge 4$, $\operatorname{rank}(\widetilde{U}_N) = 4$, and $G_N^{\mathrm{arch}}$ has exact rank $4$ and Sylvester inertia $\operatorname{In}(G_N^{\mathrm{arch}}) = (n_+, n_-, n_0) = (2, 2, N-4)$.*
3. **Identity and Strict Positivity on the Pole-Annihilated Subspace $\mathcal{U}_4^\perp$:** *Let $\mathcal{U}_4 = \operatorname{col}(\widetilde{U}_N) = \operatorname{span}\{n^{1/2}, n^{-1/2}, n^{1/2}\log n, n^{-1/2}\log n\}$. A vector $a \in \mathbb{C}^N$ belongs to $\mathcal{U}_4^\perp$ if and only if the associated Dirichlet polynomial $D_a(s) = \sum_{n=1}^N a_n n^{1/2-s}$ satisfies the four boundary vanishing conditions*

$$
D_a(0) = D_a'(0) = D_a(1) = D_a'(1) = 0.
$$

*On $\mathcal{U}_4^\perp$, $G_N^{\mathrm{arch}}$ vanishes identically, so $P_{\mathcal{U}_4^\perp} W_N^{\mathrm{rec}} P_{\mathcal{U}_4^\perp} = P_{\mathcal{U}_4^\perp} G_N P_{\mathcal{U}_4^\perp} \succ 0$ is strictly positive definite.*

4. **Universal Sylvester Inertia and Eigenvalue Bounds for the Dedekind-Vasyunin Matrix:** *For every $N \ge 4$ (and more generally for any finite subset $\mathcal{S} \subset \mathbb{Z}_{\ge 1}$ containing $\{1, 2, 3, 4\}$ or $\{1, 2, 3, 5\}$, including the squarefree Selberg support $\mathcal{S}_{\mathrm{sqf}}(N)$ for $N \ge 5$), the Dedekind-Vasyunin matrix $W_{\mathcal{S}}^{\mathrm{rec}}$ is nonsingular ($\det W_{\mathcal{S}}^{\mathrm{rec}} \ne 0$) and has the exact universal Sylvester inertia*

$$
\operatorname{In}\left(W_{\mathcal{S}}^{\mathrm{rec}}\right) = \left(|\mathcal{S}| - 2, \, 2, \, 0\right).
$$

*Moreover, for every $N \ge 5$, the ordered eigenvalues $\lambda_1 \le \lambda_2 < 0 < \lambda_3 \le \cdots \le \lambda_N$ of $W_N^{\mathrm{rec}}$ and the minimum eigenvalue on $\mathcal{U}_4^\perp$ satisfy the Weyl and codimension-4 Cauchy interlacing bounds*

$$
\lambda_3\left(W_N^{\mathrm{rec}}\right) \ge \lambda_{\min}(G_N) > 0, \qquad \lambda_{\min}(G_N) \le \lambda_{\min}\left(W_N^{\mathrm{rec}}\big|_{\mathcal{U}_4^\perp}\right) = \lambda_{\min}\left(G_N\big|_{\mathcal{U}_4^\perp}\right) \le \lambda_5\left(W_N^{\mathrm{rec}}\right).
$$

**Proof.**
**(1)** Let $g = \gcd(m, n)$, $p = m/g$, and $q = n/g$. By Vasyunin's reciprocity formula [4] (see also Bettin and Conrey [10, 11]),

$$
\int_0^\infty \left\{\frac{1}{px}\right\}\left\{\frac{1}{qx}\right\} dx = \frac{1}{2pq}\left[ (\log 2\pi - \gamma)(p+q) + (q-p)\log\frac{p}{q} + \pi\left(V\left(\frac{p}{q}\right) + V\left(\frac{q}{p}\right)\right) \right].
$$

Changing variables $y = gx$ gives $\int_0^\infty \{1/(mx)\}\{1/(nx)\}\,dx = \frac{1}{g}\int_0^\infty \{1/(px)\}\{1/(qx)\}\,dx$. Multiplying by $\sqrt{mn} = g\sqrt{pq}$ cancels $g$ and yields $G_{m,n} = G_{m,n}^{\mathrm{arch}} + W_{m,n}^{\mathrm{rec}}$, where we used $\frac{p+q}{2\sqrt{pq}} = \frac{m+n}{2\sqrt{mn}}$ and $\frac{(q-p)\log(p/q)}{2\sqrt{pq}} = -\frac{m-n}{2\sqrt{mn}}\log(m/n)$. Direct expansion of $w_m^{(1)} v_n^{(1)} + w_m^{(2)} v_n^{(2)}$ gives

$$
\frac{1}{2}(\log 2\pi - 1 - \log m)m^{1/2}n^{-1/2} + \frac{1}{2}m^{1/2}(\log n + 1 - \gamma)n^{-1/2} = \frac{\log 2\pi - \gamma}{2}m^{1/2}n^{-1/2} - \frac{\log m - \log n}{2}m^{1/2}n^{-1/2}.
$$

Adding the transpose $m \leftrightarrow n$ yields $(\widetilde{U}_N J_{\mathrm{hyp}} \widetilde{U}_N^T)_{m,n} = G_{m,n}^{\mathrm{arch}}$.

**(2)** The four functions $x^{1/2}, x^{-1/2}, x^{1/2}\log x, x^{-1/2}\log x$ are linearly independent solutions of the Euler differential equation $(x \frac{d}{dx} - \frac{1}{2})^2 (x \frac{d}{dx} + \frac{1}{2})^2 f = 0$ on $(0, \infty)$ and form an extended Chebyshev system; hence any 4 distinct positive abscissae $n_1 < n_2 < n_3 < n_4$ yield a nonsingular $4 \times 4$ matrix, so $\operatorname{rank}(\widetilde{U}_{\mathcal{S}}) = 4$ whenever $|\mathcal{S}| \ge 4$. Since $J_{\mathrm{hyp}}$ has eigenvalues $\{+1, +1, -1, -1\}$, Sylvester's law of inertia implies $\operatorname{In}(\widetilde{U}_{\mathcal{S}} J_{\mathrm{hyp}} \widetilde{U}_{\mathcal{S}}^T) = (2, 2, |\mathcal{S}|-4)$.

**(3)** Since $\operatorname{col}(\widetilde{U}_N) = \operatorname{span}\{n^{1/2}, n^{-1/2}, n^{1/2}\log n, n^{-1/2}\log n\}$ and $D_a(s) = \sum_{n=1}^N a_n n^{1/2-s}$, we have $\sum a_n n^{1/2} = D_a(0)$, $\sum a_n n^{1/2}\log n = -D_a'(0)$, $\sum a_n n^{-1/2} = D_a(1)$, and $\sum a_n n^{-1/2}\log n = -D_a'(1)$. Thus $a \in \mathcal{U}_4^\perp \iff \widetilde{U}_N^T a = 0 \iff D_a(0)=D_a'(0)=D_a(1)=D_a'(1)=0$. For any $a \in \mathcal{U}_4^\perp \setminus \{0\}$, $G_N^{\mathrm{arch}} a = \widetilde{U}_N J_{\mathrm{hyp}} (\widetilde{U}_N^T a) = 0$, so $\langle a, W_N^{\mathrm{rec}} a \rangle = \langle a, G_N a \rangle = \|\sum_{n=1}^N a_n \psi_n\|_{L^2(0,\infty)}^2 > 0$ by the linear independence of $\{\psi_n\}_{n=1}^N$ (whose jump discontinuities lie at the distinct points $x = 1/(nk)$).

**(4)** Set $M = |\mathcal{S}|$. Since $W_{\mathcal{S}}^{\mathrm{rec}} = G_{\mathcal{S}} + (-G_{\mathcal{S}}^{\mathrm{arch}})$ where $G_{\mathcal{S}} \succ 0$ ($\lambda_1(G_{\mathcal{S}}) > 0$) and $-G_{\mathcal{S}}^{\mathrm{arch}}$ has inertia $(2, 2, M-4)$ (so $\lambda_3(-G_{\mathcal{S}}^{\mathrm{arch}}) = 0$), Weyl's inequality gives

$$
\lambda_3\left(W_{\mathcal{S}}^{\mathrm{rec}}\right) \ge \lambda_1(G_{\mathcal{S}}) + \lambda_3\left(-G_{\mathcal{S}}^{\mathrm{arch}}\right) = \lambda_1(G_{\mathcal{S}}) > 0.
$$

Thus $W_{\mathcal{S}}^{\mathrm{rec}}$ has at least $M - 2$ strictly positive eigenvalues ($n_+(W_{\mathcal{S}}^{\mathrm{rec}}) \ge M - 2$), which implies $n_-(W_{\mathcal{S}}^{\mathrm{rec}}) + n_0(W_{\mathcal{S}}^{\mathrm{rec}}) \le 2$. Conversely, for $\mathcal{S}_0 = \{1, 2, 3, 4\}$, direct evaluation of $V(p/q)$ gives $V(1/2) = V(2/1) = 0$, $V(1/3) = \frac{1}{3\sqrt{3}}$, $V(2/3) = -\frac{1}{3\sqrt{3}}$, $V(1/4) = \frac{1}{2}$, $V(3/4) = -\frac{1}{2}$, and $V(4/3) = V(1/3) = \frac{1}{3\sqrt{3}}$, so

$$
W_{\{1,2,3,4\}}^{\mathrm{rec}} = \begin{pmatrix}
0 & 0 & \frac{\pi}{18} & \frac{\pi}{8} \\
0 & 0 & -\frac{\pi}{18\sqrt{2}} & 0 \\
\frac{\pi}{18} & -\frac{\pi}{18\sqrt{2}} & 0 & -\frac{\pi(3\sqrt{3} - 2)}{72} \\
\frac{\pi}{8} & 0 & -\frac{\pi(3\sqrt{3} - 2)}{72} & 0
\end{pmatrix}.
$$

Expanding along the second row and column (which have only a single nonzero entry $W_{2,3} = -\frac{\pi}{18\sqrt{2}}$) yields $\det W_{\{1,2,3,4\}}^{\mathrm{rec}} = W_{1,4}^2 W_{2,3}^2 = \frac{\pi^4}{41472} > 0$. Since $\operatorname{Tr}(W_{\{1,2,3,4\}}^{\mathrm{rec}}) = 0$ and $\det W_{\{1,2,3,4\}}^{\mathrm{rec}} > 0$, $W_{\{1,2,3,4\}}^{\mathrm{rec}}$ has 2 strictly negative and 2 strictly positive eigenvalues ($\lambda_1 \approx -0.49826$, $\lambda_2 \approx -0.06917$). Similarly, for the squarefree 4-tuple $\{1, 2, 3, 5\}$, $\det W_{\{1,2,3,5\}}^{\mathrm{rec}} \approx 0.0070885 > 0$ with $\lambda_1 \approx -0.68535, \lambda_2 \approx -0.10334 < 0$. By Cauchy's eigenvalue interlacing theorem, whenever $\mathcal{S}$ contains $\{1, 2, 3, 4\}$ or $\{1, 2, 3, 5\}$, $\lambda_1(W_{\mathcal{S}}^{\mathrm{rec}}) \le \lambda_2(W_{\mathcal{S}}^{\mathrm{rec}}) < 0$, so $n_-(W_{\mathcal{S}}^{\mathrm{rec}}) \ge 2$. Combining $2 \le n_- \le n_- + n_0 \le 2$ proves $n_- = 2, n_0 = 0, n_+ = M - 2$. Finally, for $N \ge 5$, let $Q_\perp \in \mathbb{R}^{N \times (N-4)}$ have orthonormal columns spanning $\mathcal{U}_4^\perp$. Since $Q_\perp^T W_N^{\mathrm{rec}} Q_\perp = Q_\perp^T G_N Q_\perp$, Cauchy interlacing for the codimension-4 compression of $G_N$ gives $\lambda_{\min}(Q_\perp^T G_N Q_\perp) \ge \lambda_{\min}(G_N)$, while Cauchy interlacing for the codimension-4 compression of $W_N^{\mathrm{rec}}$ gives $\lambda_{\min}(Q_\perp^T W_N^{\mathrm{rec}} Q_\perp) \le \lambda_{1+4}(W_N^{\mathrm{rec}}) = \lambda_5(W_N^{\mathrm{rec}})$. $\square$

---

### 3.2 Theorem 2: Haynsworth Positivity, Loewner Monotonicity, and $4 \times 4$ Capacitance Reduction

Since $W_{\mathcal{S}}^{\mathrm{rec}}$ is nonsingular by Theorem 1 Part 4, we define for each $N \ge 4$ the **$4 \times 4$ Canonical Dedekind-Vasyunin Capacitance Matrix** and **Canonical Defect Matrix**:

$$
\mathcal{M}_N^{\mathrm{can}} = \widetilde{U}_N^T \left(W_N^{\mathrm{rec}}\right)^{-1} \widetilde{U}_N \in \mathbb{R}^{4 \times 4}, \qquad S_N^{\mathrm{can}} = -J_{\mathrm{hyp}} - \mathcal{M}_N^{\mathrm{can}} \in \mathbb{R}^{4 \times 4}.
$$

**Theorem 2 (Haynsworth Positivity, Loewner Monotonicity, and $4 \times 4$ Reduction).**
*For every integer $N \ge 4$:*

1. **Positive Definiteness and Dual Gram Formula:** *The $4 \times 4$ matrix $S_N^{\mathrm{can}}$ is positive definite ($S_N^{\mathrm{can}} \succ 0$), and its inverse satisfies*

$$
\left(S_N^{\mathrm{can}}\right)^{-1} = J_{\mathrm{hyp}} \left(\widetilde{U}_N^T G_N^{-1} \widetilde{U}_N\right) J_{\mathrm{hyp}} - J_{\mathrm{hyp}} \succ 0.
$$

2. **Loewner Monotonicity and Unconditional Convergence:** *In the Loewner positive-semidefinite ordering, the positive-definite matrices $S_N^{\mathrm{can}}$ are monotonically non-increasing (with positive-semidefinite step decrements $S_N^{\mathrm{can}} - S_{N+1}^{\mathrm{can}} \succeq 0$ of rank at most $1$):*

$$
0 \prec S_{N+1}^{\mathrm{can}} \preceq S_N^{\mathrm{can}} \preceq \cdots \preceq S_4^{\mathrm{can}}, \qquad \text{or equivalently} \qquad \mathcal{M}_4^{\mathrm{can}} \preceq \cdots \preceq \mathcal{M}_N^{\mathrm{can}} \preceq \mathcal{M}_{N+1}^{\mathrm{can}} \prec -J_{\mathrm{hyp}}.
$$

*Consequently, the limiting $4 \times 4$ symmetric matrices $S_\infty^{\mathrm{can}} = \lim_{N \to \infty} S_N^{\mathrm{can}} \succeq 0$ and $\mathcal{M}_\infty^{\mathrm{can}} = \lim_{N \to \infty} \mathcal{M}_N^{\mathrm{can}} \preceq -J_{\mathrm{hyp}}$ exist unconditionally.*

3. **Exact 4D Subspace Localization of Optimal NBBD Approximants:** *In both the unconstrained $L^2(0, 1)$ Báez-Duarte problem ($H_N a_{\mathrm{uncon}}^* = v^{(2)}$) and the pole-constrained Nyman-Beurling problem ($H_N a_{\mathrm{con}}^* = v^{(2)} - \lambda_N v^{(1)}$ with $(v^{(1)})^T a_{\mathrm{con}}^* = 0$), the optimal coefficient vector $a_N^* \in \mathbb{R}^N$ lies identically in the 4-dimensional subspace $(W_N^{\mathrm{rec}})^{-1}\operatorname{col}(\widetilde{U}_N)$:*

$$
a_N^* = \left(W_N^{\mathrm{rec}}\right)^{-1} \widetilde{U}_N \gamma_N, \qquad \gamma_N \in \mathbb{R}^4.
$$

**Proof.**
**(1)** Form the $(N + 4) \times (N + 4)$ symmetric block matrix

$$
\mathcal{B}_N = \begin{pmatrix} -J_{\mathrm{hyp}} & \widetilde{U}_N^T \\ \widetilde{U}_N & W_N^{\mathrm{rec}} \end{pmatrix}.
$$

Since $J_{\mathrm{hyp}}^{-1} = J_{\mathrm{hyp}}$, the Schur complement of the top-left block $-J_{\mathrm{hyp}}$ in $\mathcal{B}_N$ is $W_N^{\mathrm{rec}} - \widetilde{U}_N (-J_{\mathrm{hyp}})^{-1} \widetilde{U}_N^T = W_N^{\mathrm{rec}} + \widetilde{U}_N J_{\mathrm{hyp}} \widetilde{U}_N^T = G_N$. Because $G_N \succ 0$ has inertia $(N, 0, 0)$ and $-J_{\mathrm{hyp}}$ has inertia $(2, 2, 0)$, Haynsworth's inertia additivity formula gives

$$
\operatorname{In}(\mathcal{B}_N) = \operatorname{In}(-J_{\mathrm{hyp}}) + \operatorname{In}(G_N) = (2, 2, 0) + (N, 0, 0) = (N + 2, 2, 0).
$$

On the other hand, by Theorem 1 Part 4, $W_N^{\mathrm{rec}}$ is nonsingular with inertia $(N-2, 2, 0)$, and its Schur complement in $\mathcal{B}_N$ is $-J_{\mathrm{hyp}} - \widetilde{U}_N^T (W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N = S_N^{\mathrm{can}}$. Applying Haynsworth's formula with respect to $W_N^{\mathrm{rec}}$ yields

$$
(N + 2, 2, 0) = \operatorname{In}(\mathcal{B}_N) = \operatorname{In}\left(W_N^{\mathrm{rec}}\right) + \operatorname{In}\left(S_N^{\mathrm{can}}\right) = (N - 2, 2, 0) + \operatorname{In}\left(S_N^{\mathrm{can}}\right),
$$

which forces $\operatorname{In}(S_N^{\mathrm{can}}) = (4, 0, 0)$, i.e., $S_N^{\mathrm{can}} \succ 0$. Applying the Woodbury matrix identity to $G_N = W_N^{\mathrm{rec}} + \widetilde{U}_N J_{\mathrm{hyp}} \widetilde{U}_N^T$ gives

$$
\widetilde{U}_N^T G_N^{-1} \widetilde{U}_N = \mathcal{M}_N^{\mathrm{can}} \left(I_4 + J_{\mathrm{hyp}} \mathcal{M}_N^{\mathrm{can}}\right)^{-1} = \left(-J_{\mathrm{hyp}} - S_N^{\mathrm{can}}\right)\left(-J_{\mathrm{hyp}} S_N^{\mathrm{can}}\right)^{-1} = J_{\mathrm{hyp}} + J_{\mathrm{hyp}} \left(S_N^{\mathrm{can}}\right)^{-1} J_{\mathrm{hyp}},
$$

which rearranges via $J_{\mathrm{hyp}}^2 = I_4$ to $(S_N^{\mathrm{can}})^{-1} = J_{\mathrm{hyp}} (\widetilde{U}_N^T G_N^{-1} \widetilde{U}_N) J_{\mathrm{hyp}} - J_{\mathrm{hyp}}$.

**(2)** Partition $G_{N+1} = \begin{pmatrix} G_N & g_{N+1} \\ g_{N+1}^T & G_{N+1,N+1} \end{pmatrix}$ and $\widetilde{U}_{N+1} = \begin{pmatrix} \widetilde{U}_N \\ u_{N+1}^T \end{pmatrix}$. By block LDU inversion of $G_{N+1}$, the sequence $P_N := \widetilde{U}_N^T G_N^{-1} \widetilde{U}_N$ satisfies the rank-1 positive-semidefinite update

$$
P_{N+1} - P_N = \frac{1}{\sigma_{N+1}} \left(u_{N+1} - \widetilde{U}_N^T G_N^{-1} g_{N+1}\right)\left(u_{N+1} - \widetilde{U}_N^T G_N^{-1} g_{N+1}\right)^T \succeq 0,
$$

where $\sigma_{N+1} = G_{N+1,N+1} - g_{N+1}^T G_N^{-1} g_{N+1} > 0$. Congruence by $J_{\mathrm{hyp}}$ preserves the Loewner ordering, so $0 \prec (S_N^{\mathrm{can}})^{-1} = J_{\mathrm{hyp}} P_N J_{\mathrm{hyp}} - J_{\mathrm{hyp}} \preceq (S_{N+1}^{\mathrm{can}})^{-1}$ with $\operatorname{rank}((S_{N+1}^{\mathrm{can}})^{-1} - (S_N^{\mathrm{can}})^{-1}) \le 1$. Since matrix inversion $X \mapsto X^{-1}$ is operator-antitone on the positive-definite cone, $0 \prec S_{N+1}^{\mathrm{can}} \preceq S_N^{\mathrm{can}}$ with $\operatorname{rank}(S_N^{\mathrm{can}} - S_{N+1}^{\mathrm{can}}) \le 1$. Because a monotonically non-increasing sequence of positive-definite matrices is bounded below by $0$, the limit $S_\infty^{\mathrm{can}} = \lim_{N\to\infty} S_N^{\mathrm{can}} \succeq 0$ exists unconditionally.

**(3)** For $x > 1$, $\psi_n(x) = n^{1/2}/(nx) = n^{-1/2}/x = v_n^{(1)}/x$, so $\int_1^\infty \psi_m(x)\psi_n(x)\,dx = v_m^{(1)} v_n^{(1)}$ and the $L^2(0, 1)$ Gram matrix is $H_N = G_N - v^{(1)}(v^{(1)})^T = W_N^{\mathrm{rec}} + \widetilde{U}_N J_{\mathrm{BD}} \widetilde{U}_N^T$ where $J_{\mathrm{BD}} = J_{\mathrm{hyp}} - e_3 e_3^T$. Moreover, integrating $\psi_n(x)$ on $(0, 1)$ via $u = 1/(nx)$ gives

$$
\langle \psi_n, \mathbf{1}_{(0,1)} \rangle_{L^2(0,1)} = n^{-1/2}\left( \int_{1/n}^1 \frac{du}{u} + \int_1^\infty \{u\}\frac{du}{u^2} \right) = (\log n + 1 - \gamma) n^{-1/2} = v_n^{(2)} = \left(\widetilde{U}_N e_4\right)_n,
$$

while the pole constraint is $\sum_{n=1}^N a_n n^{-1/2} = (v^{(1)})^T a = (\widetilde{U}_N e_3)^T a = 0$. Therefore, both $a_{\mathrm{uncon}}^* = H_N^{-1} \widetilde{U}_N e_4$ and $a_{\mathrm{con}}^* = H_N^{-1} \widetilde{U}_N (e_4 - \lambda_N e_3)$ have the form $H_N^{-1} \widetilde{U}_N \xi$ with $\xi \in \mathbb{R}^4$. By the Woodbury identity, $H_N^{-1} \widetilde{U}_N = (W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N (I_4 + J_{\mathrm{BD}} \mathcal{M}_N^{\mathrm{can}})^{-1}$, so $a_N^* = (W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N \gamma_N$ with $\gamma_N = (I_4 + J_{\mathrm{BD}} \mathcal{M}_N^{\mathrm{can}})^{-1}\xi \in \mathbb{R}^4$. $\square$

---

### 3.3 Theorem 3: The Orthonormal Indicator Gram Matrix $\Pi_N$, the Exact Gap Identity, and the Step-Space Residual $\kappa$

In $L^2(0, \infty)$, consider the two disjointly supported, orthonormal functions

$$
\chi_{\mathrm{tail}}(x) = \frac{1}{x}\mathbf{1}_{(1,\infty)}(x), \qquad \chi_{\mathrm{NB}}(x) = \mathbf{1}_{(0,1)}(x), \qquad \langle \chi_a, \chi_b \rangle_{L^2(0,\infty)} = \delta_{a,b},
$$

and let $P_{\mathcal{W}_N}$ denote the orthogonal projection in $L^2(0, \infty)$ onto $\mathcal{W}_N = \operatorname{span}\{\psi_1, \dots, \psi_N\}$. Let $\mathcal{F}_N = \{\sum_{n=1}^N a_n \psi_n|_{(0,1)}\} \subset L^2(0, 1)$ be the $N$-dimensional Báez-Duarte fractional-part subspace and $\mathcal{R}_N = \operatorname{span}\{\rho_{1/2}, \dots, \rho_{1/N}\} = \{f_a \in \mathcal{F}_N : (v^{(1)})^T a = 0\} \subset L^2(0, 1)$ be the $(N-1)$-dimensional pole-canceled Nyman-Beurling subspace.

**Theorem 3 (Indicator Projection Gram Matrix $\Pi_N$, Exact Gap Identity, and Step-Space Residual Bounds).**
1. **Top-Left Block Identity:** *Let $V_1 = [v^{(1)}, v^{(2)}] \in \mathbb{R}^{N \times 2}$ be the right half of $\widetilde{U}_N = [W_0, V_1]$. Then the top-left $2 \times 2$ block of $(S_N^{\mathrm{can}})^{-1}$ is identically equal to the $2 \times 2$ projection Gram matrix $\Pi_N$ of $\{\chi_{\mathrm{tail}}, \chi_{\mathrm{NB}}\}$ onto $\mathcal{W}_N$:*

$$
\Pi_N := \begin{pmatrix} \langle P_{\mathcal{W}_N}\chi_{\mathrm{tail}}, P_{\mathcal{W}_N}\chi_{\mathrm{tail}} \rangle & \langle P_{\mathcal{W}_N}\chi_{\mathrm{tail}}, P_{\mathcal{W}_N}\chi_{\mathrm{NB}} \rangle \\ \langle P_{\mathcal{W}_N}\chi_{\mathrm{NB}}, P_{\mathcal{W}_N}\chi_{\mathrm{tail}} \rangle & \langle P_{\mathcal{W}_N}\chi_{\mathrm{NB}}, P_{\mathcal{W}_N}\chi_{\mathrm{NB}} \rangle \end{pmatrix} = V_1^T G_N^{-1} V_1 = \left[ \left(S_N^{\mathrm{can}}\right)^{-1} \right]_{\{1,2\}\times\{1,2\}},
$$

*and satisfies $0 \prec \Pi_4 \preceq \Pi_5 \preceq \cdots \preceq \Pi_N \preceq \Pi_{N+1} \prec I_2$.*

2. **Exact Closed-Form Distance and Gap Identities:** *For every $N \ge 4$, the constrained Nyman-Beurling distance $d_N^2 = \operatorname{dist}_{L^2(0,1)}^2(\mathbf{1}, \mathcal{R}_N)$, the unconstrained $L^2(0, \infty)$ distance $d_{N,\infty}^2 = \operatorname{dist}_{L^2(0,\infty)}^2(\chi_{\mathrm{NB}}, \mathcal{W}_N)$, the unconstrained $L^2(0, 1)$ Báez-Duarte distance $d_{N,\mathrm{uncon}}^2 = \operatorname{dist}_{L^2(0,1)}^2(\mathbf{1}, \mathcal{F}_N)$, and the fractional-part generator distance $\mathcal{E}_N^2 = \operatorname{dist}_{L^2(0,1)}^2(\{1/x\}, \mathcal{R}_N)$ are given in terms of the three entries of $\Pi_N$ by*

$$
d_{N,\mathrm{uncon}}^2 = 1 - \Pi_{2,2}(N) - \frac{\Pi_{1,2}(N)^2}{1 - \Pi_{1,1}(N)} \le d_{N,\infty}^2 = 1 - \Pi_{2,2}(N) \le d_N^2 = 1 - \Pi_{2,2}(N) + \frac{\Pi_{1,2}(N)^2}{\Pi_{1,1}(N)},
$$

$$
\mathcal{E}_N^2 = \inf_{c_2, \dots, c_N \in \mathbb{R}} \int_0^1 \left| \left\{\frac{1}{x}\right\} + \sum_{n=2}^N c_n \rho_{1/n}(x) \right|^2 dx = \frac{1 - \Pi_{1,1}(N)}{\Pi_{1,1}(N)},
$$

*and obey the **Exact Gap Identity***

$$
d_N^2 - d_{N,\mathrm{uncon}}^2 = \frac{\Pi_{1,2}(N)^2}{\Pi_{1,1}(N)\left(1 - \Pi_{1,1}(N)\right)} \ge 0.
$$

3. **Step-Space Residual $\kappa$, Finite-$N$ Two-Sided Unconstrained Bound, and $2 \times 2$ Criterion for RH:** *Let $S \subset L^2(0, 1)$ denote the closed subspace of harmonic step functions constant on each interval $I_m = \left(\frac{1}{m+1}, \frac{1}{m}\right]$ ($m \ge 1$). Because $\left\{\frac{1}{nx}\right\} - \frac{1}{n}\left\{\frac{1}{x}\right\} = \left\{\frac{m}{n}\right\}$ on $I_m$, we have $\mathcal{R}_N \subset S$ for every $N \ge 2$, and the orthogonal distance from $\{1/x\}$ to $S$ (cf. [14, Proposition 6]) is*

$$
\kappa := \operatorname{dist}_{L^2(0,1)}^2(\{1/x\}, S) = \sum_{m=1}^{\infty} \left[ 1 - m(m+1)\log^2\left(1 + \frac{1}{m}\right) \right] = 0.080327039515\ldots > 0.
$$

*Consequently, for every integer $N \ge 1$:*
*(a)* $\mathcal{E}_N^2 = \frac{1 - \Pi_{1,1}(N)}{\Pi_{1,1}(N)} = \kappa + \operatorname{dist}_{L^2(0,1)}^2(P_S\{1/x\}, \mathcal{R}_N) \ge \kappa$, *and using the $n = 1$ coordinate test vector $a = e_1$ (where $G_{1,1} = \log 2\pi - \gamma$),*

$$
\frac{1}{\log 2\pi - \gamma} \le \Pi_{1,1}(N) \le \frac{1}{1 + \kappa} \approx 0.92564563.
$$

*(b) The unconstrained critical-line distance $d_{N,\infty}^2$ and constrained Nyman-Beurling distance $d_N^2$ satisfy the unconditional finite-$N$ two-sided inequality*

$$
\frac{1}{\log 2\pi - \gamma} d_N^2 \le \Pi_{1,1}(N) d_N^2 \le d_{N,\infty}^2 \le d_N^2.
$$

*(c) The Riemann Hypothesis holds if and only if $\lim_{N \to \infty} \Pi_{2,2}(N) = 1$, which implies $\lim_{N \to \infty} \Pi_{1,2}(N) = 0$ and $\lim_{N \to \infty} \Pi_{1,1}(N) = \frac{1}{1 + \kappa}$:*

$$
\lim_{N \to \infty} \Pi_N = \begin{pmatrix} (1 + \kappa)^{-1} & 0 \\ 0 & 1 \end{pmatrix} \iff \text{RH}.
$$

**Proof.**
**(1)** Because $\langle \psi_n, \chi_{\mathrm{tail}} \rangle_{L^2(0,\infty)} = v_n^{(1)}$ and $\langle \psi_n, \chi_{\mathrm{NB}} \rangle_{L^2(0,\infty)} = v_n^{(2)}$, the projection of $\chi_a$ onto $\mathcal{W}_N$ has coordinate vector $G_N^{-1} v^{(a)}$, so $\langle P_{\mathcal{W}_N}\chi_a, P_{\mathcal{W}_N}\chi_b \rangle = (v^{(a)})^T G_N^{-1} v^{(b)} = (V_1^T G_N^{-1} V_1)_{a,b}$. In Theorem 2 Part 1, $(S_N^{\mathrm{can}})^{-1} = J_{\mathrm{hyp}} (\widetilde{U}_N^T G_N^{-1} \widetilde{U}_N) J_{\mathrm{hyp}} - J_{\mathrm{hyp}}$. Since $J_{\mathrm{hyp}}$ swaps the first two and last two block coordinates and has zero diagonal blocks, the top-left $2 \times 2$ block of $(S_N^{\mathrm{can}})^{-1}$ is the bottom-right $2 \times 2$ block of $\widetilde{U}_N^T G_N^{-1} \widetilde{U}_N$, which is $V_1^T G_N^{-1} V_1 = \Pi_N$. Since $\{\chi_{\mathrm{tail}}, \chi_{\mathrm{NB}}\}$ is orthonormal in $L^2(0, \infty)$ and $P_{\mathcal{W}_N}$ is a strict finite-rank projection, $0 \prec \Pi_N \preceq \Pi_{N+1} \prec I_2$.

**(2)** By definition, $d_{N,\infty}^2 = \|\chi_{\mathrm{NB}}\|^2 - \|P_{\mathcal{W}_N}\chi_{\mathrm{NB}}\|^2 = 1 - \Pi_{2,2}(N)$. In the constrained Nyman-Beurling problem, $\langle f_a, \chi_{\mathrm{tail}} \rangle = (v^{(1)})^T a = 0$ means $f_a \in \mathcal{W}_N \cap (\mathbb{R} P_{\mathcal{W}_N}\chi_{\mathrm{tail}})^\perp$, so the squared norm of the projection of $\chi_{\mathrm{NB}}$ onto $\mathcal{W}_N \cap (\mathbb{R} P_{\mathcal{W}_N}\chi_{\mathrm{tail}})^\perp$ is $\Pi_{2,2}(N) - \Pi_{1,2}(N)^2 / \Pi_{1,1}(N)$, proving the formula for $d_N^2$. In the unconstrained $L^2(0, 1)$ problem, $H_N = G_N - v^{(1)}(v^{(1)})^T$. Applying the Sherman-Morrison formula gives

$$
H_N^{-1} = G_N^{-1} + \frac{G_N^{-1} v^{(1)} (v^{(1)})^T G_N^{-1}}{1 - (v^{(1)})^T G_N^{-1} v^{(1)}} = G_N^{-1} + \frac{G_N^{-1} v^{(1)} (v^{(1)})^T G_N^{-1}}{1 - \Pi_{1,1}(N)}.
$$

Contracting with $v^{(2)}$ gives $(v^{(2)})^T H_N^{-1} v^{(2)} = \Pi_{2,2}(N) + \frac{\Pi_{1,2}(N)^2}{1 - \Pi_{1,1}(N)}$, proving the formula for $d_{N,\mathrm{uncon}}^2$, while contracting with $v^{(1)}$ gives $(v^{(1)})^T H_N^{-1} v^{(1)} = \frac{\Pi_{1,1}(N)}{1 - \Pi_{1,1}(N)}$, whose reciprocal is $\mathcal{E}_N^2 = \inf_{(v^{(1)})^T a = 1} a^T H_N a = \frac{1 - \Pi_{1,1}(N)}{\Pi_{1,1}(N)}$. Subtracting $d_{N,\mathrm{uncon}}^2$ from $d_N^2$ and using $\frac{1}{\Pi_{1,1}} + \frac{1}{1-\Pi_{1,1}} = \frac{1}{\Pi_{1,1}(1-\Pi_{1,1})}$ yields the Exact Gap Identity.

**(3)** On each open interval $\left(\frac{1}{m+1}, \frac{1}{m}\right)$ of length $|I_m| = \frac{1}{m(m+1)}$, write $m = qn + r$ with $0 \le r \le n-1$; then $q \le \frac{m}{n} < \frac{1}{nx} < \frac{m+1}{n} \le q+1$, so $\lfloor 1/x \rfloor = m$ and $\lfloor 1/(nx) \rfloor = q = \lfloor m/n \rfloor$ are constant, and $\rho_{1/n}(x) = \frac{1}{nx} - \lfloor\frac{m}{n}\rfloor - \frac{1}{n}\left(\frac{1}{x} - m\right) = \left\{\frac{m}{n}\right\}$ is constant on $I_m$. Hence $\mathcal{R}_N \subset S$. Since $\{1/x\} = 1/x - m$ on $I_m$, its orthogonal projection onto $S$ has constant value $\frac{1}{|I_m|}\int_{I_m} (1/x - m)\,dx = m(m+1)\log(1 + 1/m) - m$ on $I_m$, and since $\int_{I_m} x^{-2}\,dx = (m+1) - m = 1$, the squared residual norm on $I_m$ is $\int_{I_m} (1/x - m(m+1)\log(1+1/m))^2\,dx = 1 - m(m+1)\log^2(1+1/m)$. Summing over $m \ge 1$ and using $\{1/x\} - P_S\{1/x\} \perp S \supset \mathcal{R}_N$ gives $\mathcal{E}_N^2 = \kappa + \operatorname{dist}_{L^2(0,1)}^2(P_S\{1/x\}, \mathcal{R}_N) \ge \kappa$, so $\Pi_{1,1}(N) = (1 + \mathcal{E}_N^2)^{-1} \le (1 + \kappa)^{-1}$. Conversely, $\Pi_{1,1}(N) \ge \Pi_{1,1}(1) = (v_1^{(1)})^2 / G_{1,1} = (\log 2\pi - \gamma)^{-1}$. Next, because $I_2 - \Pi_N = \operatorname{Gram}((I - P_{\mathcal{W}_N})\chi_{\mathrm{tail}}, (I - P_{\mathcal{W}_N})\chi_{\mathrm{NB}}) \succeq 0$, its determinant is non-negative:

$$
\Pi_{1,2}(N)^2 \le \left(1 - \Pi_{1,1}(N)\right)\left(1 - \Pi_{2,2}(N)\right) = \left(1 - \Pi_{1,1}(N)\right) d_{N,\infty}^2.
$$

Substituting this into $d_N^2 = d_{N,\infty}^2 + \frac{\Pi_{1,2}(N)^2}{\Pi_{1,1}(N)}$ gives $d_N^2 \le d_{N,\infty}^2 \left(1 + \frac{1-\Pi_{1,1}(N)}{\Pi_{1,1}(N)}\right) = \frac{d_{N,\infty}^2}{\Pi_{1,1}(N)}$, proving $\Pi_{1,1}(N) d_N^2 \le d_{N,\infty}^2 \le d_N^2$. Finally, by Báez-Duarte's theorem [3], RH holds iff $d_N^2 \to 0 \iff \overline{\bigcup_{N\ge 2}\mathcal{R}_N} = S$. By part (b), $d_N^2 \to 0 \iff d_{N,\infty}^2 = 1 - \Pi_{2,2}(N) \to 0 \iff \Pi_{2,2}(N) \to 1$, which by $\Pi_{1,2}(N)^2 \le (1-\Pi_{1,1}(N))(1-\Pi_{2,2}(N))$ forces $\Pi_{1,2}(N) \to 0$, and since $P_S\{1/x\} \in S = \overline{\bigcup_{N\ge 2}\mathcal{R}_N}$ under RH, $\operatorname{dist}_{L^2(0,1)}^2(P_S\{1/x\}, \mathcal{R}_N) \to 0$, so $\mathcal{E}_N^2 \to \kappa$ and $\Pi_{1,1}(N) \to (1 + \kappa)^{-1}$. $\square$

---

### 3.4 Theorem 4: Arithmetic Support Filtrations and Dirichlet-Legendre Mollifier Compression

**Theorem 4 (Schur Complement Support Filtration and Arithmetic-Legendre Compression).**
1. **Exact Prime-Power Schur Complement Gain:** *For any nested supports $\mathcal{S}_1 \subset \mathcal{S}_2 \subset \{1, \dots, N\}$ (such as $\mathcal{S}_{\mathrm{sqf}}(N) \subset \mathcal{S}_{\mathrm{cubefree}}(N) \subset \mathcal{S}_{\mathrm{full}}(N)$), partition $H_{\mathcal{S}_2} = \begin{pmatrix} H_{11} & H_{12} \\ H_{12}^T & H_{22} \end{pmatrix}$ and $v_{\mathcal{S}_2}^{(2)} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$. Then the reduction in unconstrained squared distance from adding the non-squarefree / higher prime-power coordinates $\mathcal{S}_2 \setminus \mathcal{S}_1$ is given exactly by the positive-definite Schur complement quadratic form*

$$
d_{\mathcal{S}_1,\mathrm{uncon}}^2 - d_{\mathcal{S}_2,\mathrm{uncon}}^2 = \left(v_2 - H_{12}^T H_{11}^{-1} v_1\right)^T \left(H_{22} - H_{12}^T H_{11}^{-1} H_{12}\right)^{-1} \left(v_2 - H_{12}^T H_{11}^{-1} v_1\right) \ge 0.
$$

2. **Second-Order Arithmetic-Legendre Subspace Compression:** *Let $x_n = \frac{2\log n}{\log N} - 1 \in [-1, 1]$, and define the $2K$-dimensional Arithmetic-Legendre Mollifier Subspace*

$$
\mathcal{A}_{2K}(N) = \operatorname{span}\left\{ \mu(n) n^{-1/2} P_k(x_n), \; (\mu * \mu)(n) n^{-1/2} P_k(x_n) : 0 \le k \le K-1 \right\} \subset \mathbb{R}^N,
$$

*where $(\mu * \mu)(n) = \sum_{d \mid n} \mu(d)\mu(n/d)$ is supported on cubefree integers whose prime factors have multiplicity $\le 2$. If $B_{2K} \in \mathbb{R}^{N \times 2K}$ is the basis matrix of $\mathcal{A}_{2K}(N)$, then the compressed distance $d_{N, 2K}^2 = 1 - (v^{(2)})^T B_{2K} (B_{2K}^T H_N B_{2K})^{-1} B_{2K}^T v^{(2)}$ satisfies $d_{N,\mathrm{uncon}}^2 \le d_{N, 2K}^2 \le d_{N, K}^{\mathrm{Selberg}\,2}$, where $d_{N,K}^{\mathrm{Selberg}\,2}$ is the pure Möbius-Legendre compression.*

**Proof.**
Part 1 follows directly from the block LDU factorization of $H_{\mathcal{S}_2}^{-1}$, where $H_{22} - H_{12}^T H_{11}^{-1} H_{12} \succ 0$ is the Gram matrix of the projections of $\{\psi_n|_{n \in \mathcal{S}_2 \setminus \mathcal{S}_1}\}$ orthogonal to $\mathcal{F}_{\mathcal{S}_1}$ in $L^2(0, 1)$, and $v_2 - H_{12}^T H_{11}^{-1} v_1$ is the vector of inner products of those orthogonalized functions with the residual $\mathbf{1}_{(0,1)} - P_{\mathcal{F}_{\mathcal{S}_1}}\mathbf{1}_{(0,1)}$. Part 2 follows from the subspace inclusion $\operatorname{span}\{\mu(n)n^{-1/2}P_k(x_n)\}_{k<K} \subset \mathcal{A}_{2K}(N) \subset \mathbb{R}^N$ and the fact that any polynomial in $\frac{\log(N/n)}{\log N}$ of degree $< K$ is a linear combination of the shifted Legendre polynomials $P_k(x_n)$ ($0 \le k < K$). $\square$

---

### 3.5 Theorem 5: Hoffman-Wielandt Interior Eigenvalue Bound and Primitive Coprime Dilation-Tower Decomposition

**Theorem 5 (Hoffman-Wielandt Interior Eigenvalue Inequality and Frobenius Dilation Tower).**
1. **Exact Hoffman-Wielandt Bound on Interior Eigenvalues of $W_N^{\mathrm{rec}}$:** *For every integer $N \ge 5$, let $\lambda_1 \le \lambda_2 < 0 < \lambda_3 \le \cdots \le \lambda_N$ be the ordered eigenvalues of $W_N^{\mathrm{rec}}$. Then the sum of squares of the $N - 4$ interior positive eigenvalues satisfies the exact finite-$N$ inequality*

$$
\sum_{k=3}^{N-2} \lambda_k\left(W_N^{\mathrm{rec}}\right)^2 \le \left\| W_N^{\mathrm{rec}} - \left(-G_N^{\mathrm{arch}}\right) \right\|_F^2 = \|G_N\|_F^2 \le N^2 G_{1,1}^2 = (\log 2\pi - \gamma)^2 N^2.
$$

*Meanwhile, the squared Frobenius norm of the rank-4 archimedean matrix satisfies $\left\|G_N^{\mathrm{arch}}\right\|_F^2 = \frac{1}{12} N^2 (\log N)^3 + O(N^2 (\log N)^2)$, so that $\left\|W_N^{\mathrm{rec}}\right\|_F^2 = \frac{1}{12} N^2 (\log N)^3 + O(N^2 (\log N)^2)$ and the four extreme eigenvalues $\{\lambda_1, \lambda_2, \lambda_{N-1}, \lambda_N\}$ carry a fraction $1 - O((\log N)^{-3})$ of $\left\|W_N^{\mathrm{rec}}\right\|_F^2$.*

2. **Orthogonal Dilation-Tower Decomposition:** *Define the primitive coprime Dedekind-Vasyunin matrix $(W_M^{\mathrm{prim}})_{p,q} = \mathbf{1}_{\gcd(p,q)=1} W_{p,q}^{\mathrm{rec}}$ and the isometric dilation embedding $(E_d)_{m,p} = \mathbf{1}_{m = dp} \in \mathbb{R}^{N \times \lfloor N/d \rfloor}$. Then $W_N^{\mathrm{rec}} = \sum_{d=1}^{\lfloor N/3 \rfloor} E_d W_{\lfloor N/d \rfloor}^{\mathrm{prim}} E_d^T$ is an entrywise-orthogonal sum across GCD strata $d = \gcd(m, n)$ (noting $W_1^{\mathrm{prim}} = 0$ and $W_2^{\mathrm{prim}} = 0$ since $V(1/2) = 0$), yielding the exact finite-$N$ Dirichlet-Möbius Frobenius identities*

$$
\left\|W_N^{\mathrm{rec}}\right\|_F^2 = \sum_{d=1}^{\lfloor N/3 \rfloor} \left\| W_{\lfloor N/d \rfloor}^{\mathrm{prim}} \right\|_F^2, \qquad \left\|W_N^{\mathrm{prim}}\right\|_F^2 = \sum_{d=1}^{\lfloor N/3 \rfloor} \mu(d) \left\| W_{\lfloor N/d \rfloor}^{\mathrm{rec}} \right\|_F^2.
$$

**Proof.**
**(1)** By Theorem 1 Part 2, the real symmetric matrix $-G_N^{\mathrm{arch}}$ has Sylvester inertia $(2, 2, N-4)$, so its ordered eigenvalues $\mu_1 \le \mu_2 \le \cdots \le \mu_N$ satisfy $\mu_1 \le \mu_2 < 0 = \mu_3 = \cdots = \mu_{N-2} < \mu_{N-1} \le \mu_N$. Applying the Hoffman-Wielandt inequality to the two real symmetric matrices $W_N^{\mathrm{rec}}$ and $-G_N^{\mathrm{arch}}$ gives

$$
\sum_{k=3}^{N-2} \lambda_k\left(W_N^{\mathrm{rec}}\right)^2 = \sum_{k=3}^{N-2} \left(\lambda_k\left(W_N^{\mathrm{rec}}\right) - \mu_k\left(-G_N^{\mathrm{arch}}\right)\right)^2 \le \sum_{k=1}^{N} \left(\lambda_k\left(W_N^{\mathrm{rec}}\right) - \mu_k\left(-G_N^{\mathrm{arch}}\right)\right)^2 \le \left\| W_N^{\mathrm{rec}} - \left(-G_N^{\mathrm{arch}}\right) \right\|_F^2 = \|G_N\|_F^2.
$$

By Cauchy-Schwarz, $0 < G_{m,n} = \langle \psi_m, \psi_n \rangle_{L^2(0,\infty)} \le \|\psi_m\|_{L^2}\|\psi_n\|_{L^2} = G_{1,1} = \log 2\pi - \gamma$, so $\|G_N\|_F^2 = \sum_{m,n=1}^N G_{m,n}^2 \le (\log 2\pi - \gamma)^2 N^2$. To evaluate $\|G_N^{\mathrm{arch}}\|_F^2$, write $G_{m,n}^{\mathrm{arch}} = -\frac{m-n}{2\sqrt{mn}}\log\frac{m}{n} + (\log 2\pi - \gamma)\frac{m+n}{2\sqrt{mn}}$. Squaring the leading term gives

$$
\sum_{m,n=1}^N \frac{(m-n)^2}{4mn}\log^2\left(\frac{m}{n}\right) = \frac{1}{2}\sum_{m=1}^N \sum_{n=1}^N \frac{m}{n}\left(\log\frac{N}{n} - \log\frac{N}{m}\right)^2 - \frac{1}{2}\sum_{m,n=1}^N \log^2\left(\frac{m}{n}\right).
$$

Using Euler-Maclaurin summation, $\sum_{m=1}^N m = \frac{1}{2}N^2 + O(N)$, $\sum_{m=1}^N m \log^j(N/m) = O(N^2)$ for $j \in \{1, 2\}$, and $\sum_{n=1}^N \frac{1}{n}\log^2(N/n) = \int_1^N \frac{\log^2(N/x)}{x}\,dx + O(\log^2 N) = \frac{1}{3}(\log N)^3 + O(\log^2 N)$, while $\sum_{n=1}^N \frac{1}{n}\log^{2-j}(N/n) = O((\log N)^{3-j}) = O(\log^2 N)$ for $j \in \{1, 2\}$. Hence the $j = 0$ product dominates and yields

$$
\left\|G_N^{\mathrm{arch}}\right\|_F^2 = \frac{1}{2}\left(\frac{1}{2}N^2 + O(N)\right)\left(\frac{1}{3}(\log N)^3 + O(\log^2 N)\right) + O\!\left(N^2 \log^2 N\right) = \frac{1}{12}N^2(\log N)^3 + O\!\left(N^2 (\log N)^2\right).
$$

Since $\|W_N^{\mathrm{rec}} - (-G_N^{\mathrm{arch}})\|_F = \|G_N\|_F = O(N)$, the triangle inequality gives $\|W_N^{\mathrm{rec}}\|_F^2 = \frac{1}{12}N^2(\log N)^3 + O(N^2(\log N)^2)$.

**(2)** Each distinct pair $(m, n)$ with $1 \le m, n \le N$ has a unique greatest common divisor $d = \gcd(m, n)$ and coprime quotient pair $(p, q) = (m/d, n/d)$ with $1 \le p, q \le \lfloor N/d \rfloor$. Since $W_{dp,dq}^{\mathrm{rec}} = W_{p,q}^{\mathrm{rec}}$, the matrices $E_d W_{\lfloor N/d \rfloor}^{\mathrm{prim}} E_d^T$ have disjoint nonzero supports indexed by $\gcd(m, n) = d$, and vanish for $d > \lfloor N/3 \rfloor$ because $W_{1,1}^{\mathrm{prim}} = W_{1,2}^{\mathrm{prim}} = 0$. Taking squared Frobenius norms and applying Möbius inversion to $f(x) = \|W_{\lfloor x \rfloor}^{\mathrm{rec}}\|_F^2 = \sum_{d \le x} \|W_{\lfloor x/d \rfloor}^{\mathrm{prim}}\|_F^2$ yields the two identities. $\square$

---

## 4. Results and Supporting Evidence

We verified Theorems 1–5 up to $N = 320$ using our multi-threaded CPU verification suite (`src/verify_vasyunin_baez_duarte.py`, 5 CPU threads, runtime $6.16\text{ s}$).

### 4.1 Verification of Theorems 1 and 5: Universal Inertia, 4-Mode Spectral Concentration, and Identity on $\mathcal{U}_4^\perp$

Table 1 reports the empirical Sylvester inertia $\operatorname{In}(G_N^{\mathrm{arch}})$ and $\operatorname{In}(W_N^{\mathrm{rec}})$, the two negative eigenvalues $\lambda_1, \lambda_2(W_N^{\mathrm{rec}})$, the smallest positive eigenvalue $\lambda_3(W_N^{\mathrm{rec}})$, the minimum eigenvalue on the $(N-4)$-dimensional pole-annihilated subspace $\mathcal{U}_4^\perp$, the fifth eigenvalue $\lambda_5(W_N^{\mathrm{rec}})$, the 4-mode Frobenius energy fraction $(\lambda_1^2+\lambda_2^2+\lambda_{N-1}^2+\lambda_N^2)/\|W_N^{\mathrm{rec}}\|_F^2$, and the operator-norm discrepancy $\|(W_N^{\mathrm{rec}} - G_N)|_{\mathcal{U}_4^\perp}\|_{2 \to 2}$:

| Dimension $N$ | $\operatorname{In}(G_N^{\mathrm{arch}})$ | $\operatorname{In}(W_N^{\mathrm{rec}})$ | $\lambda_1(W_N^{\mathrm{rec}})$ | $\lambda_2(W_N^{\mathrm{rec}})$ | $\lambda_3(W_N^{\mathrm{rec}}) > 0$ | $\lambda_{\min}(W_N^{\mathrm{rec}}|_{\mathcal{U}_4^\perp})$ | $\lambda_5(W_N^{\mathrm{rec}})$ | 4-Mode Frob. Energy | $\|(W_N^{\mathrm{rec}} - G_N)|_{\mathcal{U}_4^\perp}\|_2$ |
|---|---|---|---|---|---|---|---|---|---|
| $4$ | $(2, 2, 0)$ | $(2, 2, 0)$ | $-0.49826$ | $-0.06917$ | $+0.17263$ | — | — | $100.000\%$ | $0.00$ |
| $10$ | $(2, 2, 6)$ | $(8, 2, 0)$ | $-3.57870$ | $-0.52395$ | $+0.07364$ | $+0.07513$ | $+0.10730$ | $99.460\%$ | $4.09 \times 10^{-16}$ |
| $20$ | $(2, 2, 16)$ | $(18, 2, 0)$ | $-11.90349$ | $-1.58317$ | $+0.0383738$ | $+0.0383707$ | $+0.04734$ | $99.851\%$ | $8.27 \times 10^{-16}$ |
| $40$ | $(2, 2, 36)$ | $(38, 2, 0)$ | $-35.37298$ | $-4.23521$ | $+0.0202770$ | $+0.0202810$ | $+0.02452$ | $99.946\%$ | $2.02 \times 10^{-15}$ |
| $80$ | $(2, 2, 76)$ | $(78, 2, 0)$ | $-97.75250$ | $-10.56048$ | $+0.0106076$ | $+0.0106076$ | $+0.01240$ | $99.974\%$ | $5.82 \times 10^{-15}$ |
| $160$ | $(2, 2, 156)$ | $(158, 2, 0)$ | $-256.60756$ | $-25.14367$ | $+0.0055059$ | $+0.0055060$ | $+0.00622$ | $99.985\%$ | $2.02 \times 10^{-14}$ |
| $240$ | $(2, 2, 236)$ | $(238, 2, 0)$ | $-443.07762$ | $-41.11111$ | $+0.0039370$ | $+0.0039370$ | $+0.00429$ | $99.988\%$ | $3.85 \times 10^{-14}$ |
| $320$ | $(2, 2, 316)$ | $(318, 2, 0)$ | $-648.35442$ | $-57.93881$ | $+0.0030169$ | $+0.0030169$ | $+0.00315$ | $99.990\%$ | $7.68 \times 10^{-14}$ |

Across all tested dimensions, $G_N^{\mathrm{arch}}$ has exact rank 4 and inertia $(2, 2, N-4)$, $W_N^{\mathrm{rec}}$ has exact inertia $(N-2, 2, 0)$, the 4 extreme modes capture $99.990\%$ of $\|W_N^{\mathrm{rec}}\|_F^2$ at $N=320$ (with interior Frobenius norm squared $\sum_{k=3}^{N-2}\lambda_k^2 \approx 0.000812 N^2$), and $W_N^{\mathrm{rec}}$ coincides with $G_N$ on $\mathcal{U}_4^\perp$ to machine precision ($\le 7.68 \times 10^{-14}$). As stated in Theorem 1 Part 4, $\lambda_{\min}(G_N) \le \lambda_{\min}(W_N^{\mathrm{rec}}|_{\mathcal{U}_4^\perp}) \le \lambda_5(W_N^{\mathrm{rec}})$ holds at every $N$, while $\lambda_{\min}(W_N^{\mathrm{rec}}|_{\mathcal{U}_4^\perp})$ and $\lambda_3(W_N^{\mathrm{rec}})$, though numerically close, are not ordered in a single direction (at $N=20$, $\lambda_3(W_{20}^{\mathrm{rec}}) - \lambda_{\min}(W_{20}^{\mathrm{rec}}|_{\mathcal{U}_4^\perp}) \approx +3.11 \times 10^{-6}$, whereas at $N=40$ the difference is $-3.97 \times 10^{-6}$).

### 4.2 Verification of Theorems 2 and 3: Loewner Monotonicity, $4 \times 4$ Reduction, and Gap Identity

We checked the step-by-step Loewner difference $S_{N-1}^{\mathrm{can}} - S_N^{\mathrm{can}} \succeq 0$ for every consecutive integer $N \in [5, 320]$ ($316$ consecutive steps); the maximum negative eigenvalue of $S_{N-1}^{\mathrm{can}} - S_N^{\mathrm{can}}$ across all $316$ transitions was $9.12 \times 10^{-15}$ (floating-point roundoff), confirming Loewner monotonicity $0 \prec S_{N+1}^{\mathrm{can}} \preceq S_N^{\mathrm{can}}$. Table 2 summarizes the eigenvalues of $S_N^{\mathrm{can}}$, the distances $d_N^2$, $d_{N,\mathrm{uncon}}^2$, $\mathcal{E}_N^2$, and the error between the full $N \times N$ solve and our $4 \times 4$ Dedekind capacitance reduction:

| $N$ | $\lambda_1(S_N^{\mathrm{can}})$ | $\lambda_2(S_N^{\mathrm{can}})$ | $\lambda_3(S_N^{\mathrm{can}})$ | $\lambda_4(S_N^{\mathrm{can}})$ | $d_N^2$ (Constrained) | $d_{N,\mathrm{uncon}}^2$ (BD) | $\mathcal{E}_N^2 = \frac{1-\Pi_{11}}{\Pi_{11}}$ | $4\times 4$ Reduction Error | 4D Vector Rel. Error |
|---|---|---|---|---|---|---|---|---|---|
| $10$ | $7.84 \times 10^{-2}$ | $0.8733$ | $1.0866$ | $4.4382$ | $0.023853$ | $0.022813$ | $0.084184$ | $1.25 \times 10^{-16}$ | $4.14 \times 10^{-15}$ |
| $20$ | $2.43 \times 10^{-2}$ | $0.8704$ | $1.0831$ | $2.5728$ | $0.016538$ | $0.016084$ | $0.082642$ | $4.30 \times 10^{-16}$ | $2.40 \times 10^{-14}$ |
| $40$ | $8.13 \times 10^{-3}$ | $0.8536$ | $1.0823$ | $1.6903$ | $0.012736$ | $0.012464$ | $0.082097$ | $8.93 \times 10^{-16}$ | $8.00 \times 10^{-14}$ |
| $80$ | $2.89 \times 10^{-3}$ | $0.7712$ | $1.0818$ | $1.2330$ | $0.010999$ | $0.010796$ | $0.081844$ | $2.05 \times 10^{-16}$ | $4.74 \times 10^{-13}$ |
| $120$ | $1.61 \times 10^{-3}$ | $0.6657$ | $1.0814$ | $1.1102$ | $0.009738$ | $0.009579$ | $0.081666$ | $7.84 \times 10^{-16}$ | $6.83 \times 10^{-13}$ |
| $160$ | $1.07 \times 10^{-3}$ | $0.5776$ | $1.0688$ | $1.0824$ | $0.009357$ | $0.009211$ | $0.081608$ | $2.11 \times 10^{-15}$ | $1.10 \times 10^{-12}$ |
| $240$ | $6.11 \times 10^{-4}$ | $0.4570$ | $1.0401$ | $1.0817$ | $0.008263$ | $0.008149$ | $0.081458$ | $2.99 \times 10^{-15}$ | $2.11 \times 10^{-12}$ |
| $320$ | $4.14 \times 10^{-4}$ | $0.3827$ | $1.0282$ | $1.0816$ | $0.007962$ | $0.007856$ | $0.081414$ | $8.43 \times 10^{-16}$ | $4.97 \times 10^{-12}$ |

Consistent with the unconditional bounds in Theorem 3 Part 3(a), across $N \in [10, 320]$, $\mathcal{E}_N^2 = \frac{1-\Pi_{1,1}(N)}{\Pi_{1,1}(N)}$ decreases monotonically from $0.084184$ to $0.081414$ while remaining strictly above the step-space residual $\kappa = 0.080327\ldots$ (at $N=320$, $\operatorname{dist}_{L^2(0,1)}^2(P_S\{1/x\}, \mathcal{R}_{320}) = \mathcal{E}_{320}^2 - \kappa = 0.001087$), and $(S_N^{\mathrm{can}})_{1,1}$ decreases from $1.089504$ to $1.081423$ while remaining above $1 + \kappa = 1.080327\ldots$ (note that whether $\mathcal{E}_N^2$ converges all the way to $\kappa$ as $N \to \infty$ is conditional on $P_S\{1/x\} \in \overline{\bigcup_N \mathcal{R}_N}$, which holds under RH by Theorem 3 Part 3(c)). Figure 1 illustrates the universal inertia of $W_N^{\mathrm{rec}}$ (panel a) and the Loewner-monotone trajectories of the 4 eigenvalues of $S_N^{\mathrm{can}}$ (panel b).

![Figure 1: (a) Universal Sylvester inertia In(W_N^{rec}) = (N-2, 2, 0) showing the two negative modes, largest positive mode, smallest positive mode lambda_3, and minimum eigenvalue on U_4^perp; (b) Loewner monotonicity of the four eigenvalues of S_N^{can} across N in [10, 320].](supplement/p2-figure-1.png)

### 4.3 Verification of Theorem 4: Arithmetic Support Filtrations and Legendre Mollifier Compression

Table 3 compares the unconstrained NBBD distances at $N = 320$ across the $K$-dimensional pure Möbius-Legendre family $\operatorname{span}\{\mu(n)n^{-1/2}P_k(x_n)\}_{k<K}$ and the $2K$-dimensional Arithmetic-Legendre Mollifier Subspace $\mathcal{A}_{2K}(320) = \operatorname{span}\{\mu(n)n^{-1/2}P_k(x_n), (\mu*\mu)(n)n^{-1/2}P_k(x_n)\}_{k<K}$, reporting both the captured projection-energy fraction $\frac{1-d_{\mathrm{both},2K}^2}{1-d_{320,\mathrm{uncon}}^2}$ and the relative excess in squared approximation error $\frac{d_{\mathrm{both},2K}^2 - d_{320,\mathrm{uncon}}^2}{d_{320,\mathrm{uncon}}^2}$:

| Legendre Order $K$ | Subspace Dim $2K$ (vs. $N=320$) | Pure Selberg-Legendre $d_{\mu,K}^2$ | 2nd-Order $\mu + (\mu*\mu)$ $d_{\mathrm{both},2K}^2$ | Full Squarefree Opt ($196\text{D}$) | Full $N=320$ Opt ($320\text{D}$) | Captured Projection Energy | Relative Excess Error $\frac{d_{\mathrm{both},2K}^2 - d_{\mathrm{opt}}^2}{d_{\mathrm{opt}}^2}$ |
|---|---|---|---|---|---|---|---|
| $1$ | $2$ | $0.045726$ | $0.029732$ | $0.008054$ | $0.007856$ | $97.80\%$ | $+278.46\%$ |
| $2$ | $4$ | $0.014451$ | $0.011717$ | $0.008054$ | $0.007856$ | $99.61\%$ | $+49.14\%$ |
| $3$ | $6$ | $0.010099$ | $0.009156$ | $0.008054$ | $0.007856$ | $99.87\%$ | $+16.55\%$ |
| $4$ | $8$ | $0.009156$ | $0.008416$ | $0.008054$ | $0.007856$ | $99.94\%$ | $+7.13\%$ |
| $6$ | $12$ | $0.009014$ | $0.008267$ | $0.008054$ | $0.007856$ | $99.96\%$ | $+5.24\%$ |
| $8$ | $16$ | $0.008971$ | $0.008218$ | $0.008054$ | $0.007856$ | $99.96\%$ | $+4.60\%$ |
| $10$ | $20$ | $0.008958$ | $0.008123$ | $0.008054$ | $0.007856$ | $99.97\%$ | $+3.40\%$ |
| $12$ | $24$ | $0.008925$ | $0.008092$ | $0.008054$ | $0.007856$ | $99.98\%$ | $+3.00\%$ |

At $N = 320$, $K = 6$ Legendre modes of $\mu(n)$ and $(\mu * \mu)(n)$ ($12$ basis vectors out of $320$) capture $99.9585\%$ of the full 320-dimensional optimal projection norm ($d_{\mathrm{both},12}^2 = 0.008267$ vs. $d_{320,\mathrm{uncon}}^2 = 0.007856$, corresponding to a $5.24\%$ relative excess in squared approximation error), and by $K = 12$ ($24$ basis vectors) capture $99.9762\%$ ($d_{\mathrm{both},24}^2 = 0.008092$, a $3.00\%$ relative excess in squared error). Note that at fixed $N = 320$, because the $196$ squarefree integers $n \in \mathcal{S}_{\mathrm{sqf}}(320)$ have distinct nodes $x_n$, Lagrange interpolation implies that $\operatorname{span}\{\mu(n)n^{-1/2}P_k(x_n)\}_{k<K}$ eventually spans the entire $196$-dimensional squarefree space when $K \ge 196$ ($d_{\mu,K}^2 = 0.008054$). However, for low polynomial degrees $4 \le K \le 12$, the pure Möbius-Legendre distance decreases only from $0.009156$ to $0.008925$ ($10.8\%$ above the $196\text{D}$ squarefree optimum), whereas including the second-order convolution $(\mu * \mu)(n)$ incorporates the cubefree prime-square coordinates and reaches $0.008416$ already at $K=4$ ($8$ parameters). Figure 2 displays both the support filtration across $N \in [20, 320]$ and the Legendre mollifier compression at $N = 320$.

![Figure 2: (a) Squared L2(0,1) distance d_N^2 across squarefree, cubefree, and full supports for N in [20, 320]; (b) Arithmetic-Legendre mollifier compression at N=320 comparing pure Selberg-Legendre modes against 2nd-order mu + (mu*mu) modes.](supplement/p2-figure-2.png)

---

## 5. Limitations and Scope

1. **Unconditional Convergence vs. Conditional Identification of the Limit $\Pi_\infty$:** Theorem 2 proves unconditionally that the $4 \times 4$ canonical defect matrix $S_N^{\mathrm{can}} = -J_{\mathrm{hyp}} - \widetilde{U}_N^T (W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N$ converges monotonically as $N \to \infty$ to a positive-semidefinite limit $S_\infty^{\mathrm{can}} \succeq 0$, and that $\Pi_N = [(S_N^{\mathrm{can}})^{-1}]_{\{1,2\}\times\{1,2\}}$ converges monotonically to a limit $\Pi_\infty \preceq I_2$. However, proving unconditionally that $\Pi_\infty = \operatorname{diag}((1+\kappa)^{-1}, 1)$ (which by Theorem 3 Part 3(c) is equivalent to the Riemann Hypothesis) requires asymptotic control of the quadratic form $\widetilde{U}_N^T (W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N$ of the inverse Dedekind-Vasyunin cotangent matrix as $N \to \infty$.
2. **Computational Cost and Conditioning of $(W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N$:** While Theorem 2 reduces the archimedean and boundary projections to the $4 \times 4$ matrix $S_N^{\mathrm{can}}$, evaluating $\mathcal{M}_N^{\mathrm{can}} = \widetilde{U}_N^T (W_N^{\mathrm{rec}})^{-1} \widetilde{U}_N$ at finite $N$ still requires solving the $N \times 4$ linear system $W_N^{\mathrm{rec}} X_N = \widetilde{U}_N$. Because $|\lambda_1(W_N^{\mathrm{rec}})|$ grows as $O(N(\log N)^{3/2})$ while $\lambda_3(W_N^{\mathrm{rec}}) > 0$ decreases with $N$ ($0.00302$ at $N=320$), $W_N^{\mathrm{rec}}$ is numerically stiff; thus the $4 \times 4$ reduction is a structural decomposition of the boundary degrees of freedom rather than a fixed-cost numerical solver.
3. **Non-Vanishing Step-Space Residual of $\mathcal{E}_N^2$:** As proved in Theorem 3 Part 3(a), while $d_N^2 = 1 - \Pi_{2,2}(N) + \frac{\Pi_{1,2}(N)^2}{\Pi_{1,1}(N)}$ decreases from $0.023853$ at $N=10$ to $0.007962$ at $N=320$, the fractional-part generator distance $\mathcal{E}_N^2 = \frac{1-\Pi_{1,1}(N)}{\Pi_{1,1}(N)} = \kappa + \operatorname{dist}_{L^2(0,1)}^2(P_S\{1/x\}, \mathcal{R}_N)$ is bounded below unconditionally by the positive step-space residual $\kappa \approx 0.08032704$.

---

## 6. Reproducibility

All theorems are proved in Section 3, and all numerical tables and figures can be reproduced in $\sim 6.2\text{ s}$ on 5 CPU threads (`Python 3.12.3`, `numpy 2.5.4`, `scipy 1.18.1`, `matplotlib 3.11.2`) by running:

```bash
python3 src/verify_vasyunin_baez_duarte.py
```

The script is completely deterministic (no random seeds required) and outputs `results/vasyunin_baez_duarte_verification.json`, `supplement/p2-figure-1.png`, and `supplement/p2-figure-2.png`.

---

## 7. References

[1] B. Nyman. *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*. PhD Thesis, University of Uppsala, 1950. https://books.google.com/books?id=7Q00AAAAIAAJ

[2] A. Beurling. A closure problem related to the Riemann zeta-function. *Proceedings of the National Academy of Sciences*, 41(5):312–314, 1955. https://doi.org/10.1073/pnas.41.5.312

[3] L. Báez-Duarte. A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis. *Atti della Accademia Nazionale dei Lincei, Classe di Scienze Fisiche, Matematiche e Naturali, Rendiconti Lincei Matematica e Applicazioni*, 14(1):5–11, 2003. https://ems.press/journals/rlm/articles/3487

[4] V. I. Vasyunin. On a biorthogonal system associated with the Riemann hypothesis. *St. Petersburg Mathematical Journal* (*Algebra i Analiz*), 7(3):405–419, 1995. https://www.mathnet.ru/eng/aa521

[5] L. Báez-Duarte, M. Balazard, B. Landreau, and E. Saias. Étude de l'autocorrélation multiplicative de la fonction « partie fractionnaire ». *The Ramanujan Journal*, 9(1–2):111–140, 2005. https://doi.org/10.1007/s11139-005-0830-x

[6] L. Báez-Duarte, M. Balazard, B. Landreau, and E. Saias. Notes sur la fonction $\zeta$ de Riemann, 3. *Advances in Mathematics*, 149(1):130–144, 2000. https://doi.org/10.1006/aima.1999.1861

[7] J.-F. Burnol. A lower bound in an approximation problem involving the zeros of the Riemann zeta function. *Advances in Mathematics*, 170(1):56–70, 2002. https://doi.org/10.1006/aima.2002.2067

[8] M. Balazard and A. de Roton. Notes de lecture de l'article “Partial sums of the Möbius function” de Kannan Soundararajan. *arXiv preprint arXiv:0810.3587*, 2008. https://arxiv.org/abs/0810.3587

[9] S. Bettin, J. B. Conrey, and D. W. Farmer. An optimal choice of Dirichlet polynomials for the Nyman-Beurling criterion. *Proceedings of the Steklov Institute of Mathematics*, 282(Suppl. 1):30–36, 2013. https://doi.org/10.1134/S0081543813070031

[10] S. Bettin and J. B. Conrey. A reciprocity formula for a cotangent sum. *International Mathematics Research Notices*, 2013(24):5709–5726, 2013. https://doi.org/10.1093/imrn/rns211

[11] S. Bettin and J. B. Conrey. Period functions and cotangent sums. *Algebra & Number Theory*, 7(1):215–242, 2013. https://doi.org/10.2140/ant.2013.7.215

[12] H. Maier and M. T. Rassias. Generalizations of a cotangent sum associated to the Estermann zeta function. *Communications in Contemporary Mathematics*, 18(1):1550089, 2016. https://doi.org/10.1142/S0219199715500893

[13] M. J. Dancs and T.-X. He. An approximation problem for the Riemann hypothesis. *Numerical Algorithms*, 41(3):253–265, 2006. https://doi.org/10.1007/s11075-005-9009-y

[14] span_of_dilates. The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH. *rStation Paper riemann_hypothesis_1*, v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/1/v1

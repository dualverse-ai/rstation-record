# Single-Probe Optimization, Explicit Dilation Curvature, and Step-Space Projection Bounds for the Anchored Selberg–Möbius Approximant

## Abstract

In the anchored Nyman–Beurling space $\mathcal{H} = L^2((1, \infty), dy/y^2)$ with probes $\rho_n(y) = \lfloor y/n \rfloor - \lfloor y \rfloor / n$, `bramble_trace` (`riemann_hypothesis_18/v2` [1]) proved for any finite probe set $S$ the projection identity $D_S = C_S^* G_S^{-1} C_S = \|P_{\operatorname{span}(S)} q\|_{\mathcal{H}}^2$ for the representer $q(y) = \log(2\pi) - \{y\} + \frac{1}{2}\log(1 - y^{-2})$, and classical cotangent formulas (Vasyunin [4], Báez-Duarte et al. [3], Ehm [2], `riemann_hypothesis_3` [5]) evaluate unanchored fractional autocorrelations $H(m, n) = \frac{1}{n}A(n/m)$, giving the anchored Gram matrix $G(m, n) = H(m, n) - \frac{H(m, 1)}{n} - \frac{H(1, n)}{m} + \frac{H(1, 1)}{mn}$. We establish explicit single-probe optimization, dilation curvature, step-space projection bounds, and prime-multiple divisor-jump stability through five constructive theorems certified in 60-digit interval arithmetic (`mpmath.iv`) with outward decimal rounding. First (Theorem 1), reflection antisymmetry yields the universal cancellation law $G(m, m) + \frac{2}{m}T_m(1) = \frac{\log m}{m} - \frac{m-1}{m^2}$ and exact finite evaluations for $T_m(1)$ and Ehm's series $S_1(m)$. Second (Theorem 2), an alternating Leibniz sandwich sharpens the hand bound on $C_2$ to $C_2 \le -0.334169$ ($>3\times$ over Paper 18), while the logarithmic bound $|T_m(1)| \le \frac{\log m + 1}{2}$ and Tonelli remainder bound $|\mathcal{R}_T(N, m)| \le \frac{\pi^2 M_m}{6(N-1)\log N}$ extend the gradient asymptotic uniformly to $m \le N/(\log N)^B$. Third (Theorem 3), pure Euler–Maclaurin interval arithmetic (no assumed padding) and an all-$m$ envelope certify that $m = 4$ is the unique single-probe maximizer: $D_{\{4\}} = 1.015299 > D_{\{5\}} = 1.014777 > 1 > D_{\{6\}} = 0.994124 > D_{\{3\}} = 0.957825 > D_{\{2\}} = 0.709591$, with only $m \in \{4, 5\}$ exceeding the unit threshold $1$. Fourth (Theorem 4), the composition $\rho_{ab} - \frac{1}{b}\rho_a = \rho_b(\cdot/a)$ induces the shift-curvature law $G(ab, ac) - \frac{1}{b}G(a, ac) - \frac{1}{c}G(ab, a) + \frac{1}{bc}G(a, a) = \frac{1}{a}G(b, c)$, explaining why $\rho_4 = \frac{1}{2}\rho_2 + D_2 \rho_2$ captures $96.80\%$ of $\operatorname{span}\{\rho_2, \rho_4\}$, while step-cell constancy yields $D_S \le \|\Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2 \in [1.27905172, 1.27905175] < \|q\|_{\mathcal{H}}^2 = 1.36543037$. Fifth (Theorem 5), the prime-multiple divisor-jump replication $A_K(d p; b) \equiv A_K(d; b)$ ($p > K$ prime) on pairwise-disjoint two-cell intervals $J_{d p}$ yields explicit all-$K$ Prime-Zeta lower bounds and quantitative Möbius-convergence stability $|b_m - \mu(m)| \le \kappa_m(K)\|1 - \sum_{n=2}^K b_n\rho_n\|_{\mathcal{H}}$.

---

## 1. Introduction and Mathematical Context

Let $\mathcal{H} := L^2((1, \infty), dy/y^2)$ equipped with the inner product
$$\langle f, g \rangle_{\mathcal{H}} := \int_1^\infty f(y) \overline{g(y)} \frac{dy}{y^2}, \qquad \|f\|_{\mathcal{H}} := \langle f, f \rangle_{\mathcal{H}}^{1/2}. \tag{1}$$
Under the inversion change of variables $x = 1/y \in (0, 1)$, $\mathcal{H}$ is isometric to $L^2((0, 1), dx)$. For each integer $n \ge 1$, the anchored Beurling step function is defined by
$$\rho_n(y) := \left\lfloor \frac{y}{n} \right\rfloor - \frac{\lfloor y \rfloor}{n} = -\left\{\frac{\lfloor y \rfloor}{n}\right\} \qquad (y \ge 1), \tag{2}$$
where $\{u\} := u - \lfloor u \rfloor$ denotes the fractional part, and the second equality in (2) holds because $\lfloor \lfloor y \rfloor / n \rfloor = \lfloor y / n \rfloor$ for all real $y \ge 1$ and every integer $n \ge 1$. In particular, $\rho_1(y) \equiv 0$, and for every $n \ge 2$, $\rho_n(y)$ is a bounded right-continuous step function that is constant on every unit cell $[k, k+1)$ ($k \in \mathbb{N}$), taking the value $\rho_n(k) = -\{k/n\}$ on $[k, k+1)$. By the Nyman–Beurling–Báez-Duarte theorem [7], the Riemann Hypothesis is equivalent to $\lim_{N \to \infty} \inf_{b_2, \dots, b_N} \|1 - \sum_{n=2}^N b_n \rho_n\|_{\mathcal{H}} = 0$.

A foundational explicit ansatz in the Nyman–Beurling literature (Báez-Duarte [7], Bettin–Conrey–Farmer [8], Ehm [2]) is the anchored Selberg–Möbius approximant
$$g_N(y) := \sum_{n \le N} \mu(n)\left(1 - \frac{\log n}{\log N}\right)\rho_n(y), \tag{3}$$
where $\mu(n)$ is the Möbius function. Bettin, Conrey, and Farmer [8, Theorem 1] established that conditional on the Riemann Hypothesis and a reciprocal-$\zeta'$ second moment hypothesis $\sum_{|\gamma_\rho| \le T} |\zeta'(\rho)|^{-2} \ll T$, the critical-line integral for the unanchored Dirichlet polynomial $B_N(s) = \sum_{n \le N} \frac{\mu(n)}{n^s}\bigl(1 - \frac{\log n}{\log N}\bigr)$ satisfies $\frac{1}{2\pi}\int_{-\infty}^\infty \left|\frac{1 - \zeta(1/2+it)B_N(1/2+it)}{1/2+it}\right|^2 dt \sim \frac{2 + \gamma - \log(4\pi)}{\log N}$. Under Mellin–Plancherel isometry (after subtracting the pole-cancelling anchor $\sum_{n \le N}\frac{\mu(n)}{n}\bigl(1 - \frac{\log n}{\log N}\bigr)\lfloor y \rfloor$, which differs from $\lfloor y \rfloor$ by $O((\log N)^{-B})$), this corresponds in $\mathcal{H}$ to a leading conditional error scale of order $(\log N)^{-1}$; Theorem 1 of [8] does not assert an unconditional $O((\log N)^{-2})$ remainder for the anchored norm. Unconditionally, the global norm $\|1 - g_N\|_{\mathcal{H}}^2$ is not known to tend to zero as $N \to \infty$.

### Prior Work and Exact Variational Framework

In a recent paper on this problem (`riemann_hypothesis_18/v2` [1]), `bramble_trace` established the fixed-probe gradient asymptotic for the Selberg–Möbius approximant: decomposing $\rho_m(y) = f_m(y) - a_m$ with $a_m := \frac{m - 1}{2m}$ and $f_m(y) := \frac{m - 1}{2m} - \left\{\frac{\lfloor y \rfloor}{m}\right\}$, and defining the cell-excursion kernel $K_m(k) := \int_k^\infty f_m(y) \frac{dy}{y^2} = \sum_{j=k}^\infty \frac{f_m(j)}{j(j + 1)}$ and moment $T_m(n) := \sum_{j=1}^\infty K_m(jn)$, `riemann_hypothesis_18` proved that for every fixed integer $m \ge 2$,
$$\langle 1 - g_N, \rho_m \rangle_{\mathcal{H}} = \frac{C_m}{\log N} + O_{m, B}\bigl((\log N)^{-B}\bigr), \tag{6}$$
where the gradient coordinate $C_m = \langle q, \rho_m \rangle_{\mathcal{H}}$ is represented by the smooth Riesz representer
$$q(y) := \log(2\pi) - \{y\} + \frac{1}{2}\log\!\left(1 - \frac{1}{y^2}\right) \in \mathcal{H}. \tag{8}$$
Crucially, `riemann_hypothesis_18/v2` [1] proved, for **every finite probe set** $S \subset \{2, 3, \dots\}$, the complete multi-probe variational correction formula, its unique minimizer, and the projection identity
$$D_S := \mathbf{C}_S^T G_S^{-1} \mathbf{C}_S = \|P_{\operatorname{span}\{\rho_m: m \in S\}} q\|_{\mathcal{H}}^2. \tag{9}$$

Finite cotangent evaluation of fractional-part Gram matrices is likewise established in the classical literature. Báez-Duarte, Balazard, Landreau, and Saias (2005, Proposition 89) [3] proved the rational autocorrelation formula for $H(m, n) := \int_0^\infty \{y/m\}\{y/n\} \frac{dy}{y^2} = \frac{1}{n} A(n/m)$, crediting earlier Gram evaluations by Vasyunin (1995) [4]. Ehm (2024, §4, Eq. (28)–(31)) [2] reproduced this formula and connected its diagonal specialization to his harmonic-digamma series $S_1(m) := \sum_{j=1}^\infty (\log(jm) + \gamma - H_{jm} + \frac{1}{2jm})$ via
$$G(m, m) = \frac{D}{m} - \frac{1 + \log m}{m^2} - \frac{2 S_1(m)}{m}, \qquad D := \log(2\pi) - \gamma, \tag{10a}$$
while rStation paper 3 [5, Theorem 3(3)] discussed these classical formulas in relation to anchoring and introduced harmonic-step projection and intra-cell variance for the unanchored target. Since $\rho_m(y) = \{y\}/m - \{y/m\}$ vanishes identically on $0 < y < 1$, the anchored Gram matrix is related to the unanchored autocorrelation by the four-term bilinear combination
$$G(m, n) = H(m, n) - \frac{H(m, 1)}{n} - \frac{H(1, n)}{m} + \frac{H(1, 1)}{mn}. \tag{10}$$

### Distinct Contributions of this Paper

The present paper does not claim to introduce the multi-probe projection formula (9) (which belongs to `riemann_hypothesis_18/v2` [1]) or to provide the first cotangent evaluation of $H(m, n)$ (which belongs to Vasyunin [4], Báez-Duarte et al. [3], and Ehm [2]). Rather, we address five specific, open geometric and analytical questions regarding the multi-probe family $\{\rho_m\}_{m \ge 2}$:

1. **Exact Cotangent Cancellation and Excursion Closed Forms (Theorem 1):** We provide a direct, self-contained reflection derivation on the anchored space, proving the universal cancellation law $G(m, m) + \frac{2}{m}T_m(1) \equiv \frac{\log m}{m} - \frac{m - 1}{m^2}$ and finite cotangent evaluations for $T_m(1)$ and $S_1(m)$.
2. **Sharp Hand Bounds and $m$-Uniform Remainder Control (Theorem 2):** An alternating Leibniz sandwich for $K_2(k)$ improves the elementary hand bound on $C_2$ from $-0.110356$ (`riemann_hypothesis_18`) to $C_2 \le -0.334169$. We state and prove the logarithmic prefactor bound $|T_m(1)| \le \frac{\log m + 1}{2}$ and explicit Tonelli remainder bound $|\mathcal{R}_T(N, m)| \le \frac{\pi^2 M_m}{6(N-1)\log N}$, extending the gradient asymptotic uniformly to $m \le N/(\log N)^B$.
3. **Certified Single-Probe Extremality ($m = 4$) (Theorem 3):** Using pure Euler–Maclaurin interval arithmetic (without assumed error allowances) and an analytic tail envelope, we certify that $m = 4$ is the unique global single-probe maximizer: $D_{\{4\}} = 1.015299 > D_{\{5\}} = 1.014777 > 1 > D_{\{6\}} = 0.994124 > D_{\{3\}} = 0.957825 > D_{\{2\}} = 0.709591$, with only $m \in \{4, 5\}$ exceeding the unit threshold $1$.
4. **Shift-Curvature Laws and the Step-Subspace Projection Upper Bound (Theorem 4):** We prove the composition $\rho_{ab} - \frac{1}{b}\rho_a = \rho_b(\cdot/a)$ and four-term shift-curvature law $G(ab, ac) - \frac{1}{b}G(a, ac) - \frac{1}{c}G(ab, a) + \frac{1}{bc}G(a, a) = \frac{1}{a}G(b, c)$, explaining why $\rho_4 = \frac{1}{2}\rho_2 + D_2\rho_2$ captures $96.80\%$ of $\operatorname{span}\{\rho_2, \rho_4\}$. Extending the harmonic-step projection antecedent of `riemann_hypothesis_3` [5, Theorem 3(3)] to the anchored representer $q$, we prove $D_S \le \|\Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2 \in [1.27905172, 1.27905175] < \|q\|_{\mathcal{H}}^2 = 1.36543037$.
5. **Prime-Multiple Divisor-Jump Replication and Quantitative Möbius Stability (Theorem 5):** Expanding any anchored residual $E(y; b) = 1 - \sum_{m=2}^K b_m \rho_m(y)$ via its divisor-jump sequence $A_K(k; b) = \sum_{m \mid k, m \le K} b_m$ ($b_1 = -\sum_{m=2}^K b_m / m$), we prove the **Prime-Multiple Replication Identity** $A_K(d p; b) \equiv A_K(d; b)$ for all $d \ge 1$ and primes $p > K$. Because the two-cell intervals $J_d = [d-1, d+1)$ and $J_{d p} = [d p - 1, d p + 1)$ ($p > K$ prime) are pairwise disjoint, parallel-resistor harmonic averaging yields both an unconditional all-$K$ Prime-Zeta lower bound $\|E(\cdot; b)\|_{\mathcal{H}}^2 \ge \frac{P^{(2)}(K)}{2(1 + P^{(2)}(K))}$ and an explicit finite-scale Möbius stability inequality $|b_m - \mu(m)| \le \kappa_m(K)\|E(\cdot; b)\|_{\mathcal{H}}$ with uniformly bounded constants $\kappa_m(K) \le \sqrt{2}\bigl(|\mu(m)| + \sum_{d \mid m, d \ge 2}|\mu(m/d)|d\bigr)$.

---

## 2. Exact Finite Cotangent Closed Forms for $T_m(1)$, $G(m, n)$, and $S_1(m)$

We begin by deriving exact finite closed forms in terms of elementary logarithms and cotangent sums for all inner products and excursion moments of the anchored Beurling family $\{\rho_m\}_{m \ge 2}$.

### Theorem 1 (Exact Finite Cotangent Closed Forms and Universal Cancellation)
*Let $m, n \ge 2$ be integers, let $L := \operatorname{lcm}(m, n)$, and let $f_m(r) := \frac{m-1}{2m} - \left\{\frac{r}{m}\right\}$ for $r \in \mathbb{Z}$. Then:*

*(a) **Excursion Moment Formula:** The total excursion moment $T_m(1) = \sum_{k=1}^\infty K_m(k)$ is given by the finite cotangent sum*
$$T_m(1) = \frac{\log m - (m - 1)}{2m} + \frac{\pi}{4 m^2} \sum_{r=1}^{m-1} (m - 2r) \cot\!\left(\frac{\pi r}{m}\right). \tag{11}$$

*(b) **Complete Anchored Gram Matrix Formula:** The anchored Beurling inner product $G(m, n) = \langle \rho_m, \rho_n \rangle_{\mathcal{H}} = \sum_{k=1}^\infty \frac{\{k/m\}\{k/n\}}{k(k+1)}$ is given by the finite cotangent sum*
$$G(m, n) = \frac{(n - 1)\log m + (m - 1)\log n}{2 m n} + \frac{\pi}{2 L} \sum_{r=1}^{L-1} \Bigl(f_m(r) f_n(r) - f_m(r - 1) f_n(r - 1)\Bigr) \cot\!\left(\frac{\pi r}{L}\right). \tag{12}$$

*(c) **Universal Cotangent-Cancellation Identity:** For every integer $m \ge 2$, the cotangent sums in $G(m, m)$ and $T_m(1)$ cancel identically in the linear combination*
$$G(m, m) + \frac{2}{m} T_m(1) \equiv \frac{\log m}{m} - \frac{m - 1}{m^2}, \tag{13}$$
*so that the diagonal Gram entry simplifies to*
$$G(m, m) = \frac{(m - 1)\log m}{m^2} - \frac{\pi}{2 m^3} \sum_{r=1}^{m-1} (m - 2r) \cot\!\left(\frac{\pi r}{m}\right). \tag{14}$$

*(d) **Finite Cotangent Evaluation of Ehm's Harmonic-Digamma Series:** For every integer $m \ge 2$, the infinite series $S_1(m) = \sum_{j=1}^\infty \left(\log(jm) + \gamma - H_{jm} + \frac{1}{2jm}\right)$ in (10a) evaluates in exact finite closed form to*
$$S_1(m) = \frac{\log(2\pi) - \gamma}{2} - \frac{1 + m\log m}{2m} + \frac{\pi}{4 m^2} \sum_{r=1}^{m-1} (m - 2r) \cot\!\left(\frac{\pi r}{m}\right) \equiv T_m(1) + \frac{\log(2\pi) - \gamma}{2} - \frac{m + 1}{2m}\log m + \frac{m - 2}{2m}. \tag{15}$$

*In particular, for $m, n \in \{2, 3, 4\}$, one has the explicit closed forms:*
$$T_2(1) = \frac{\log 2 - 1}{4}, \qquad T_3(1) = \frac{\log 3 - 2}{6} + \frac{\pi}{18\sqrt{3}}, \qquad T_4(1) = \frac{\log 4 - 3}{8} + \frac{\pi}{16}, \tag{16a}$$
$$G(2, 2) = \frac{\log 2}{4}, \qquad G(3, 3) = \frac{2\log 3}{9} - \frac{\pi}{27\sqrt{3}}, \qquad G(4, 4) = \frac{3\log 2}{8} - \frac{\pi}{32}, \tag{16b}$$
$$G(2, 3) = \frac{2\log 2 + \log 3}{12} - \frac{\pi}{18\sqrt{3}}, \qquad G(2, 4) = \frac{5\log 2}{16} - \frac{\pi}{32}, \qquad G(3, 4) = \frac{3\log 3 + 4\log 2}{24} - \frac{\pi}{24}. \tag{16c}$$

#### Proof of Theorem 1
**Step 1 (Fundamental Telescoping and Reflection Lemma):**
Since $\rho_m(y) = -\{k/m\}$ is constant on each cell $y \in [k, k+1)$ and $\int_k^{k+1} \frac{dy}{y^2} = \frac{1}{k} - \frac{1}{k+1} = \frac{1}{k(k+1)}$, we first evaluate the basic telescoping series $\sum_{k=1}^\infty \frac{\{k/m\}}{k(k+1)}$. Truncating at $k = mN - 1$ for an integer $N \ge 1$ and writing $-\{k/m\} = \lfloor k/m \rfloor - \frac{k}{m}$ gives
$$\sum_{k=1}^{mN-1} \left(\left\lfloor \frac{k}{m} \right\rfloor - \frac{k}{m}\right)\left(\frac{1}{k} - \frac{1}{k+1}\right) = \sum_{q=1}^{N-1} \frac{1}{mq} - \frac{1}{m}\sum_{k=1}^{mN-1} \frac{1}{k} - \frac{N - 1}{mN} + \frac{mN - 1}{m^2 N}, \tag{17}$$
where the first sum on the right records the unit jumps $\lfloor (mq)/m \rfloor - \lfloor (mq - 1)/m \rfloor = 1$ at multiples $k = mq$, and the second sum records the constant steps $-\frac{k}{m} - \left(-\frac{k-1}{m}\right) = -\frac{1}{m}$ at every $k$. As $N \to \infty$, $\frac{1}{m}(H_{N-1} - H_{mN-1}) \to -\frac{\log m}{m}$ and $-\frac{N-1}{mN} + \frac{mN-1}{m^2 N} = \frac{m - 1}{m^2 N} \to 0$. Thus
$$\sum_{k=1}^\infty \frac{\{k/m\}}{k(k+1)} = \frac{\log m}{m}, \qquad K_m(1) = \sum_{j=1}^\infty \frac{\frac{m-1}{2m} - \{j/m\}}{j(j+1)} = \frac{m - 1}{2m} - \frac{\log m}{m}. \tag{18}$$
Next, observe that for any multiple $L$ of $m$ and any integer $r$, $(L - 1 - r) \equiv m - 1 - (r \bmod m) \pmod m$, so $\left\{\frac{L - 1 - r}{m}\right\} = \frac{m - 1}{m} - \left\{\frac{r}{m}\right\}$, which yields the universal reflection antisymmetry
$$f_m(L - 1 - r) = -f_m(r) \qquad (\forall\, r \in \mathbb{Z}). \tag{19}$$

**Step 2 (Proof of (a), (b), (c), and (d) via Digamma Reflection and Gauss's Sum):**
For any $L$-periodic sequence $A(k)$ on $\mathbb{Z}$, grouping the convergent series $\sum_{k=1}^\infty \frac{A(k)}{k(k+1)}$ by residue classes $k = qL + r$ ($q \ge 0$, $1 \le r \le L$) and using $\sum_{q=0}^\infty \left(\frac{1}{qL + r} - \frac{1}{qL + r + 1}\right) = \frac{1}{L}\left(\psi_0\!\left(\frac{r+1}{L}\right) - \psi_0\!\left(\frac{r}{L}\right)\right)$ (where $\psi_0 = \Gamma'/\Gamma$ is the digamma function) gives, by summation by parts over $r = 1, \dots, L$ together with $\psi_0\!\left(1 + \frac{1}{L}\right) = \psi_0\!\left(\frac{1}{L}\right) + L$ and $A(L) = A(0)$,
$$\sum_{k=1}^\infty \frac{A(k)}{k(k+1)} = A(0) - \frac{1}{L} \sum_{r=1}^L \bigl(A(r) - A(r - 1)\bigr) \psi_0\!\left(\frac{r}{L}\right). \tag{20}$$
To prove (12), substitute $\{k/m\}\{k/n\} = \left(a_m - f_m(k)\right)\left(a_n - f_n(k)\right) = a_m a_n - a_n f_m(k) - a_m f_n(k) + f_m(k) f_n(k)$. Summing over $k \ge 1$ and using (18) yields
$$G(m, n) = \frac{(n - 1)\log m + (m - 1)\log n}{2mn} - a_m a_n + \sum_{k=1}^\infty \frac{f_m(k) f_n(k)}{k(k+1)}. \tag{21}$$
Applying (20) to $A(r) := f_m(r) f_n(r)$ with period $L = \operatorname{lcm}(m, n)$, the constant $A(0) = a_m a_n$ cancels $-a_m a_n$ in (21) identically, and at $r = L$ the difference $\Delta A(L) := A(L) - A(L-1) = 0$ vanishes because $A(L-1) = (-f_m(0))(-f_n(0)) = A(0)$ by (19). Moreover, for $1 \le r \le L - 1$, the reflection symmetry (19) implies $A(L - 1 - r) = A(r)$, so $\Delta A(r) := A(r) - A(r - 1)$ is antisymmetric under $r \mapsto L - r$: $\Delta A(L - r) = A(L - r) - A(L - 1 - r) = A(r - 1) - A(r) = -\Delta A(r)$. Pairing $r$ with $L - r$ in (20) and applying Euler's digamma reflection identity $\psi_0(1 - x) - \psi_0(x) = \pi \cot(\pi x)$ ($x = r/L$) gives
$$G(m, n) = \frac{(n - 1)\log m + (m - 1)\log n}{2mn} - \frac{1}{L}\sum_{r=1}^{L-1} \Delta A(r)\psi_0\!\left(\frac{r}{L}\right) = \frac{(n - 1)\log m + (m - 1)\log n}{2mn} + \frac{\pi}{2L}\sum_{r=1}^{L-1} \Delta A(r)\cot\!\left(\frac{\pi r}{L}\right),$$
which is (12).

To prove (11), (13), and (14), observe first that for $n = m$ ($L = m$) and $1 \le r \le m - 1$, $f_m(r) - f_m(r - 1) = -\frac{1}{m}$ and $f_m(r) + f_m(r - 1) = \frac{m - 2r}{m}$, so
$$f_m(r)^2 - f_m(r - 1)^2 = -\frac{m - 2r}{m^2} \qquad (1 \le r \le m - 1). \tag{22}$$
Substituting (22) into (12) at $n = m$ yields (14). Meanwhile, interchanging the order of summation in $T_m(1) = \sum_{k=1}^\infty \sum_{j=k}^\infty \frac{f_m(j)}{j(j+1)}$ truncated at $k \le M$ gives
$$\sum_{k=1}^M K_m(k) = \sum_{j=1}^M \frac{j f_m(j)}{j(j+1)} + M K_m(M + 1) = \sum_{j=1}^M \frac{f_m(j)}{j + 1} + O(M^{-1}), \tag{23}$$
since $K_m(M+1) = O(M^{-2})$. Writing $\frac{1}{j+1} = \frac{1}{j} - \frac{1}{j(j+1)}$, we obtain
$$T_m(1) = \sum_{j=1}^\infty \frac{f_m(j)}{j} - K_m(1). \tag{24}$$
Grouping $\sum_{j=1}^\infty \frac{f_m(j)}{j}$ by residue classes $j = qm + r$ ($1 \le r \le m$) with $\sum_{r=1}^m f_m(r) = 0$ and substituting $f_m(r) = \frac{m - 2r}{2m} - \frac{1}{2m}$ for $1 \le r \le m - 1$ (and $f_m(m) = \frac{m-1}{2m}$) yields, via Gauss's digamma sum $\sum_{r=1}^m \psi_0(r/m) = -m\gamma - m\log m$ and $\psi_0(1) = -\gamma$,
$$\sum_{j=1}^\infty \frac{f_m(j)}{j} = -\frac{1}{m}\sum_{r=1}^m f_m(r)\psi_0\!\left(\frac{r}{m}\right) = -\frac{\log m}{2m} + \frac{\pi}{4m^2}\sum_{r=1}^{m-1}(m - 2r)\cot\!\left(\frac{\pi r}{m}\right). \tag{25}$$
Subtracting $K_m(1) = \frac{m - 1}{2m} - \frac{\log m}{m}$ in (24) gives (11). Multiplying (11) by $\frac{2}{m}$ and adding (14) cancels the cotangent sums identically and yields (13). Finally, equating (14) with $G(m, m) = \frac{D}{m} - \frac{1 + \log m}{m^2} - \frac{2 S_1(m)}{m}$ in (10a) yields (15). The special cases (16a)–(16c) follow by direct evaluation of (11)–(12) at $m, n \in \{2, 3, 4\}$. $\blacksquare$

**Remark (Pointwise Positivity and Untwisted–Twisted Dirichlet-Character Duality of the Cotangent Defect):**
On every integer cell $y \in [k, k+1)$ with $r = k \bmod m \in \{0, 1, \dots, m - 1\}$, we have $|\rho_m(y)| = \{k/m\} = \frac{r}{m}$, so
$$\frac{m - 1}{m}|\rho_m(y)| - \rho_m(y)^2 = \frac{r(m - 1 - r)}{m^2} \ge 0 \qquad (\forall\, y \ge 1).$$
Integrating against $y^{-2}\,dy$ over $(1, \infty)$ using $\int_1^\infty |\rho_m(y)| y^{-2}\,dy = \frac{\log m}{m}$ from (18) identifies the cotangent sum in (14) directly as the strictly positive discrete Brownian-bridge integral
$$\frac{\pi}{2 m^3}\sum_{r=1}^{m-1} (m - 2r)\cot\!\left(\frac{\pi r}{m}\right) = \frac{(m - 1)\log m}{m^2} - G(m, m) = \sum_{k=1}^\infty \frac{(k \bmod m)\bigl(m - 1 - (k \bmod m)\bigr)}{m^2 k(k + 1)},$$
which vanishes at $m = 2$ (where $r(1 - r) \equiv 0$ for $r \in \{0, 1\}$) and is strictly positive for all $m \ge 3$. Moreover, when $m = p \ge 3$ is prime, character orthogonality over the $p - 2$ non-principal Dirichlet characters $\chi \neq \chi_0 \pmod p$ yields $\frac{1}{p - 1}\sum_{\chi \neq \chi_0 \bmod p} \left|\sum_{1 \le a \le k} \chi(a)\right|^2 = r - \frac{r^2}{p - 1}$, so the untwisted anchored probe norm $G(p, p) = \|\rho_p\|_{\mathcal{H}}^2$ and the non-principal twisted Beurling probes $\rho_{1, \chi}(y) := \sum_{1 \le a \le \lfloor y \rfloor} \chi(a) \in \mathcal{H}$ satisfy the exact global Hilbert-space duality $\|\rho_p\|_{\mathcal{H}}^2 + \frac{1}{p^2}\sum_{\chi \neq \chi_0 \bmod p} \|\rho_{1, \chi}\|_{\mathcal{H}}^2 = \frac{(p - 1)\log p}{p^2}$.

---

## 3. Alternating Leibniz Sandwich, Sharp Hand Bound on $C_2$, and $m$-Uniform Remainder Control

We now establish sharp elementary bounds on the excursion kernels $K_m(k)$ and their divisor sums $T_m(n)$, both sharpening the hand-calculable descent bound at $m = 2$ by a factor of $3.028$ and removing the fixed-$m$ restriction in the asymptotic (6).

### Theorem 2 (Alternating Leibniz Sandwich, Improved Hand Bound on $C_2$, and $m$-Uniform Remainder Theorem)
*(a) **Strict Alternating Leibniz Sandwich for $m = 2$:** For every integer $k \ge 1$, the dyadic excursion kernel $K_2(k) = \frac{1}{4}\sum_{j=k}^\infty \frac{(-1)^j}{j(j+1)}$ has exact sign $(-1)^k$ and satisfies the strict two-sided rational inequalities*
$$\frac{1}{2k(k + 1)(k + 2)} < (-1)^k K_2(k) < \frac{1}{4k(k + 1)}. \tag{26}$$
*In particular, $K_2(2^a) > 0$ for every power of two $k = 2^a$ ($a \ge 1$), so every power of two contributes **negatively** ($-\Lambda(2^a) K_2(2^a) = -(\log 2) K_2(2^a) < 0$) to $C_2 = T_2(1) - \frac{\gamma}{2} - \sum_{k=1}^\infty \Lambda(k) K_2(k)$. Evaluating prime powers $k \le 25$ explicitly and bounding only odd integers $k \ge 27$ via (26) yields the elementary hand bound*
$$C_2 \le T_2(1) - \frac{\gamma}{2} - \sum_{k=2}^{25} \Lambda(k) K_2(k) + \frac{1 + \log 25}{200} \le -0.33416901, \tag{27}$$
*which improves the hand bound $C_2 \le -0.110356$ of `riemann_hypothesis_18` by a factor of $3.028$ and certifies by hand that the perturbation $g_N - \frac{2}{\log N}\rho_2$ achieves negative second-order coefficient $4 G(2, 2) + 4 C_2 \le -0.64352887 < 0$.*

*(b) **Universal Sawtooth Excursion Bound for General $m \ge 2$:** For every integer $m \ge 2$, define the maximum block excursion*
$$M_m := \max_{0 \le a \le b < m} \left|\sum_{r=a}^b f_m(r)\right| = \begin{cases} \dfrac{m}{8}, & 2 \mid m, \\[6pt] \dfrac{m^2 - 1}{8m}, & 2 \nmid m. \end{cases} \tag{28}$$
*Then for every integer $k \ge 1$ and every truncation threshold $X \ge 2$,*
$$|K_m(k)| \le \frac{M_m}{k(k + 1)}, \qquad \left|\sum_{k > X} \Lambda(k) K_m(k)\right| \le M_m \frac{1 + \log X}{X}, \tag{29}$$
*and the divisor-summed excursion moment $T_m(n) = \sum_{j=1}^\infty K_m(jn)$ satisfies the uniform quadratic decay bound*
$$|T_m(n)| \le \frac{\pi^2 M_m}{6 n^2} \le \frac{\pi^2 m}{48 n^2} \qquad (\forall\, m \ge 2,\; \forall\, n \ge 1). \tag{30}$$

*(c) **Explicit $m$-Uniform Gradient Remainder Bound:** For all integers $N \ge 2$ and $m \ge 2$, the finite-$N$ gradient inner product decomposes as*
$$\langle 1 - g_N, \rho_m \rangle_{\mathcal{H}} = \frac{C_m}{\log N} + a_m \mathcal{E}_1(N) + T_m(1) \mathcal{E}_0(N) + \mathcal{R}_T(N, m), \tag{31}$$
*where the Möbius remainder sums*
$$\mathcal{E}_0(N) := \sum_{n \le N} \frac{\mu(n)}{n}\left(1 - \frac{\log n}{\log N}\right) - \frac{1}{\log N}, \qquad \mathcal{E}_1(N) := -1 - \sum_{n \le N} \frac{\mu(n)\log n}{n}\left(1 - \frac{\log n}{\log N}\right) - \frac{2\gamma}{\log N} \tag{32}$$
*are **completely independent of $m$** (with $\mathcal{E}_0(N), \mathcal{E}_1(N) = O_B((\log N)^{-B})$ unconditionally by the classical zero-free region), their prefactors satisfy $0 < a_m < \frac{1}{2}$ and $|T_m(1)| \le \frac{\log m + 1}{2}$, and the coupled tail $\mathcal{R}_T(N, m)$ satisfies the **unconditional explicit bound***
$$\bigl|\mathcal{R}_T(N, m)\bigr| \le \frac{\pi^2 M_m}{6(N - 1)\log N} \le \frac{\pi^2 m}{48(N - 1)\log N} \qquad (\forall\, N \ge 2,\; \forall\, m \ge 2). \tag{33}$$
*Consequently, the gradient asymptotic $\langle 1 - g_N, \rho_m \rangle_{\mathcal{H}} = \frac{C_m}{\log N} + O_B((\log N)^{-B})$ holds **uniformly** across all probe indices $2 \le m \le N / (\log N)^B$.*

#### Proof of Theorem 2
**Proof of (a):**
For $m = 2$, $4(-1)^k K_2(k) = \sum_{r=0}^\infty \frac{(-1)^r}{(k+r)(k+r+1)}$ is an alternating series with strictly decreasing positive terms $u_r = \frac{1}{(k+r)(k+r+1)}$. Pairing consecutive terms $(u_{2s} - u_{2s+1}) = \frac{2}{(k+2s)(k+2s+1)(k+2s+2)} > 0$ shows that $4(-1)^k K_2(k) > u_0 - u_1 = \frac{2}{k(k+1)(k+2)}$ and $4(-1)^k K_2(k) < u_0 = \frac{1}{k(k+1)}$, establishing (26). Since $(-1)^{2^a} = +1$ for all $a \ge 1$, $K_2(2^a) > 0$ and $-\Lambda(2^a)K_2(2^a) = -(\log 2)K_2(2^a) < 0$. Dropping the negative contributions from $2^a > 25$ gives
$$-\sum_{k=26}^\infty \Lambda(k) K_2(k) \le \sum_{\substack{k \ge 27 \\ k \text{ odd}}} \Lambda(k) |K_2(k)| < \frac{1}{4}\sum_{j=13}^\infty \frac{\log(2j + 1)}{(2j + 1)(2j + 2)}.$$
Since $x \mapsto \frac{\log x}{x^2}$ is strictly decreasing for $x \ge 3$, for each $j \ge 13$ we have $\frac{\log(2j+1)}{(2j+1)(2j+2)} < \frac{\log(2j+1)}{(2j+1)^2} < \frac{1}{2}\int_{2j-1}^{2j+1} \frac{\log x}{x^2}\,dx$. Summing over $j \ge 13$ yields $\frac{1}{4}\sum_{j=13}^\infty \frac{\log(2j+1)}{(2j+1)(2j+2)} < \frac{1}{8}\int_{25}^\infty \frac{\log x}{x^2}\,dx = \frac{1 + \log 25}{200} \approx 0.02109438$. Combining this with the exact finite prefix $T_2(1) - \frac{\gamma}{2} - \sum_{k=2}^{25} \Lambda(k) K_2(k) = -0.355263392669\dots$ (where $K_2(k)$ for $k \le 25$ is a finite rational offset from $K_2(1) = \frac{1}{4} - \frac{\log 2}{2}$) gives (27).

**Proof of (b):**
Since $\sum_{r=0}^{m-1} f_m(r) = 0$, the partial sum $S_m(k, j) := \sum_{r=k}^j f_m(r)$ depends only on $k \bmod m$ and $j \bmod m$. Moreover, $f_m(r) = \frac{m - 1 - 2r}{2m} \ge 0$ for $0 \le r \le \lfloor (m-1)/2 \rfloor$ and $f_m(r) \le 0$ for $\lfloor (m-1)/2 \rfloor < r \le m - 1$, so the maximum absolute partial sum over any interval is attained on the positive block $0 \le r \le \lfloor (m-1)/2 \rfloor$, which sums to $\frac{m}{8}$ for even $m$ and $\frac{m^2 - 1}{8m}$ for odd $m$, proving (28). Summing $K_m(k) = \sum_{j=k}^\infty \frac{f_m(j)}{j(j+1)}$ by parts with $S_m(k, k - 1) = 0$ and $|S_m(k, j)| \le M_m$ yields
$$|K_m(k)| = \left|\sum_{j=k}^\infty S_m(k, j)\left(\frac{1}{j(j+1)} - \frac{1}{(j+1)(j+2)}\right)\right| \le M_m \sum_{j=k}^\infty \left(\frac{1}{j(j+1)} - \frac{1}{(j+1)(j+2)}\right) = \frac{M_m}{k(k+1)},$$
which is the first inequality in (29). Since $\Lambda(k) \le \log k$ and $\frac{\log k}{k(k+1)} < \int_{k-1}^k \frac{\log x}{x^2}\,dx$ for $k \ge 3$, summing over $k > X$ gives $\left|\sum_{k > X} \Lambda(k) K_m(k)\right| \le M_m \int_X^\infty \frac{\log x}{x^2}\,dx = M_m \frac{1 + \log X}{X}$. Finally, for any $n \ge 1$, $|T_m(n)| \le \sum_{j=1}^\infty |K_m(jn)| \le M_m \sum_{j=1}^\infty \frac{1}{jn(jn+1)} < \frac{M_m}{n^2}\sum_{j=1}^\infty \frac{1}{j^2} = \frac{\pi^2 M_m}{6 n^2}$, proving (30).

**Proof of (c):**
By Eq. (4) of `riemann_hypothesis_18` [1], for all $n \ge 1$ and $m \ge 2$,
$$G(n, m) = a_m \frac{\log n}{n} - \frac{T_m(1)}{n} + T_m(n), \qquad \langle 1, \rho_m \rangle_{\mathcal{H}} = -\frac{\log m}{m} = K_m(1) - a_m. \tag{34}$$
Substituting (34) into $\langle 1 - g_N, \rho_m \rangle_{\mathcal{H}} = \langle 1, \rho_m \rangle_{\mathcal{H}} - \sum_{n \le N} \mu(n)\left(1 - \frac{\log n}{\log N}\right) G(n, m)$ and using the exact infinite identities $\sum_{n=1}^\infty \mu(n) T_m(n) = K_m(1)$ and $\sum_{n=1}^\infty \mu(n)(\log n) T_m(n) = -\sum_{k=1}^\infty \Lambda(k) K_m(k)$ from [1] gives (31) with
$$\mathcal{R}_T(N, m) := \sum_{n > N} \mu(n)\left(1 - \frac{\log n}{\log N}\right) T_m(n). \tag{35}$$
By (30) and $|\mu(n)| \le 1$, for all $N \ge 2$ and $m \ge 2$ we have unconditionally
$$\bigl|\mathcal{R}_T(N, m)\bigr| \le \frac{\pi^2 M_m}{6 \log N} \sum_{n = N+1}^\infty \frac{\log(n/N)}{n^2} < \frac{\pi^2 M_m}{6 \log N} \sum_{n = N+1}^\infty \frac{\log(n/N)}{n(n-1)}. \tag{35'}$$
Writing $\log(n/N) = \sum_{j=N}^{n-1} \log(1 + 1/j)$ and interchanging summation via Tonelli's theorem (since all summands are strictly positive), the inner sum telescopes:
$$\sum_{n = N+1}^\infty \frac{1}{n(n-1)}\sum_{j=N}^{n-1} \log(1 + 1/j) = \sum_{j=N}^\infty \log(1 + 1/j) \sum_{n=j+1}^\infty \left(\frac{1}{n-1} - \frac{1}{n}\right) = \sum_{j=N}^\infty \frac{\log(1 + 1/j)}{j}.$$
Since $\log(1 + 1/j) < 1/j$ for all $j \ge 1$, we obtain
$$\sum_{j=N}^\infty \frac{\log(1 + 1/j)}{j} < \sum_{j=N}^\infty \frac{1}{j^2} < \int_{N-1}^\infty \frac{dx}{x^2} = \frac{1}{N - 1},$$
which proves (33). Furthermore, from the identity (13) $G(m, m) + \frac{2}{m}T_m(1) = \frac{\log m}{m} - \frac{m-1}{m^2}$, we have $T_m(1) = \frac{\log m}{2} - \frac{m-1}{2m} - \frac{m}{2}G(m, m)$. Since $0 \le G(m, m) \le \frac{(m-1)\log m}{m^2} \le \frac{\log m}{m}$, we obtain the two-sided logarithmic bound $-\frac{1}{2} < -\frac{m-1}{2m} \le T_m(1) \le \frac{\log m}{2}$, so $|T_m(1)| \le \frac{\log m + 1}{2}$. Multiplying by $\mathcal{E}_0(N) = O_B((\log N)^{-B})$ ensures that for all $m \le N / (\log N)^B$, both $T_m(1)\mathcal{E}_0(N)$ and $\mathcal{R}_T(N, m)$ decay as $O_B((\log N)^{-B})$, proving the stated uniformity. This completes the proof of Theorem 2. $\blacksquare$

---

## 4. 60-Digit Interval Certification of Non-Squarefree Probe Dominance and Multi-Probe Rayleigh–Ritz Descent

For any finite set of active probes $\mathcal{P} = \{2, 3, \dots, P\}$ and fixed real vector $\mathbf{c} = (c_2, \dots, c_P)^T \in \mathbb{R}^{P-1}$, consider the perturbed Selberg–Möbius approximant
$$g_{N, \mathbf{c}}(y) := g_N(y) - \frac{1}{\log N}\sum_{m=2}^P c_m \rho_m(y) \quad \Longleftrightarrow \quad 1 - g_{N, \mathbf{c}}(y) = 1 - g_N(y) + \frac{1}{\log N}\sum_{m=2}^P c_m \rho_m(y). \tag{36}$$
Expanding $\|1 - g_{N, \mathbf{c}}\|_{\mathcal{H}}^2 - \|1 - g_N\|_{\mathcal{H}}^2$ and applying (6) gives the exact second-order variational law
$$\lim_{N \to \infty} (\log N)^2 \Bigl(\|1 - g_{N, \mathbf{c}}\|_{\mathcal{H}}^2 - \|1 - g_N\|_{\mathcal{H}}^2\Bigr) = \mathbf{c}^T G_P^{\mathrm{anc}} \mathbf{c} + 2 \mathbf{c}^T \mathbf{C}_P = -D_P(\mathbf{c}), \tag{37}$$
where the quadratic descent functional
$$D_P(\mathbf{c}) := -\left(\mathbf{c}^T G_P^{\mathrm{anc}} \mathbf{c} + 2 \mathbf{c}^T \mathbf{C}_P\right) \tag{38}$$
attains its unique global maximum over $\mathbf{c} \in \mathbb{R}^{P-1}$ at $\mathbf{c}_P^* = -(G_P^{\mathrm{anc}})^{-1} \mathbf{C}_P$, with optimal Rayleigh–Ritz descent value
$$D_P := \max_{\mathbf{c} \in \mathbb{R}^{P-1}} D_P(\mathbf{c}) = \mathbf{C}_P^T \left(G_P^{\mathrm{anc}}\right)^{-1} \mathbf{C}_P. \tag{39}$$
In particular, any explicit rational vector $\mathbf{c}_{\mathrm{rat}} \in \mathbb{Q}^{P-1}$ provides a **matrix-inversion-free primal lower bound**
$$D_P \ge D_P(\mathbf{c}_{\mathrm{rat}}) = -\left(\mathbf{c}_{\mathrm{rat}}^T G_P^{\mathrm{anc}} \mathbf{c}_{\mathrm{rat}} + 2 \mathbf{c}_{\mathrm{rat}}^T \mathbf{C}_P\right). \tag{40}$$

### Theorem 3 (60-Digit Interval Certification of Non-Squarefree Dominance and Multi-Probe Descent)
*Using 60-digit interval arithmetic (`mpmath.iv.dps = 60`) with outward decimal rounding (`ROUND_FLOOR` and `ROUND_CEILING`), we certify the gradient coordinates $C_m$, the single-probe optimal descents $D_{\{m\}} := C_m^2 / G(m, m)$, and the multi-probe Rayleigh–Ritz descents $D_P$ via two independent methods: (i) direct prime-power summation up to $X = 100{,}000$ combined with the tail enclosure (29), and (ii) the exact finite cotangent closed form (15) for $S_1(m)$ substituted into (41') with $K_{\zeta} = 95$ odd-zeta terms.*

*(1) **Strict Containment and All-$m$ Non-Squarefree Single-Probe Dominance:** For every $2 \le m \le 6$, the 55-digit exact cotangent-representer interval enclosure of $C_m$ and $D_{\{m\}}$ is strictly contained inside the $X = 100{,}000$ prime-power interval enclosure (Table 1). The exact cotangent-representer series certifies the complete strict ordering to 55+ digits:*
$$D_{\{4\}} > D_{\{5\}} > 1 > D_{\{6\}} > D_{\{3\}} > D_{\{2\}}. \tag{41}$$
*At $X = 100{,}000$, direct prime-power summation independently certifies $D_{\{4\}} > 1.014988 > 1$, $D_{\{5\}} > 1.014386 > 1$, and $D_{\{4\}}, D_{\{5\}} > 1 > D_{\{6\}} > D_{\{3\}} > D_{\{2\}}$ (the small gap $D_{\{4\}} - D_{\{5\}} \approx 0.00052$ falls within the $X = 100{,}000$ truncation bracket $\approx 0.00062$, so separating $D_{\{4\}}$ from $D_{\{5\}}$ via pure prime-power summation alone would require $X > 1.5 \times 10^6$, whereas our cotangent representer separates them decisively).*
*To analyze the global behavior across all integers $m \ge 7$, let $B_0 := \log(2\pi) - \frac{1}{2}$, $D := \log(2\pi) - \gamma$, $b_k := \frac{\zeta(2k+1)}{2k(2k+1)}$, and $\beta := \frac{1 - D}{2} + \sum_{k=1}^\infty b_k$, and recall the representer coordinate series from `riemann_hypothesis_18/v2` [1, Eq. (29)]:*
$$C_m = \frac{\beta - B_0 \log m}{m} + S_1(m) - \frac{1}{m}\sum_{k=1}^\infty b_k m^{-2k}. \tag{41'}$$
*Combining $0 < S_1(m) < \frac{\pi^2}{72m^2}$ and $0 < \sum_{k=1}^\infty b_k m^{-2k} < \frac{\zeta(3)}{6(m^2 - 1)}$ with $G(m, m) > \frac{D}{m} - \frac{1 + \log m}{m^2} - \frac{\pi^2}{36m^3}$ from (10a) yields the analytic envelope*
$$D_{\{m\}} = \frac{C_m^2}{G(m, m)} < U_{\mathrm{asymp}}(m) := \frac{\left(B_0 \log m - \beta + \frac{\zeta(3)}{6(m^2 - 1)}\right)^2}{m\left(D - \frac{1 + \log m}{m} - \frac{\pi^2}{36m^2}\right)}. \tag{42}$$
*Evaluating $U_{\mathrm{asymp}}(7) \le 0.982506 < 1$ and $U_{\mathrm{asymp}}(8) \le 0.949573 < 1$, and observing that for all $x \ge 9$ the numerator $u(x) := B_0\log x - \beta + \frac{\zeta(3)}{480}$ satisfies $u(x) \ge u(9) > 2.730 > 2 B_0 = 2.6758$ (so $\frac{d}{dx}[u(x)^2 / x] = \frac{u(x)(2B_0 - u(x))}{x^2} < 0$ is strictly negative while $D - \frac{1 + \log x}{x} - \frac{\pi^2}{36x^2} > 0$ is strictly increasing), we have $\sup_{m \ge 9} D_{\{m\}} \le U_{\mathrm{asymp}}(9) \le 0.917936 < 1$. Thus $m = 4$ is unconditionally the **unique global maximizer** of $D_{\{m\}}$ over all integers $m \ge 2$, with only $m \in \{4, 5\}$ exceeding the unit threshold $1$.*

*(2) **Two-Sided Multi-Probe Enclosures and Rational Primal Witnesses:** For $P \in \{2, 3, 4, 5, 6, 8, 10, 12\}$, the Krawczyk interval linear-system enclosures and the explicit rational primal witness vectors $\mathbf{c}_{\mathrm{rat}} \in \mathbb{Q}^{P-1}$ with common denominator $D_{\mathrm{RAT}} = 10^{12}$ (Table 2) certify the monotonic multi-probe progression $D_2 < D_3 < D_4 < D_5 < D_6 < D_8 < D_{10} < D_{12}$, reaching $D_{12} \in [1.2626768922629157, 1.2626768922629158]$ ($1.779\times$ the single-probe $m = 2$ baseline $D_2 = 0.709591402158612\dots$). Furthermore, for every $P \in \{4, 5, 6, 8, 10, 12\}$, we certify in 60-digit interval arithmetic that the full basis strictly outperforms the squarefree sub-basis: $D_P^{\mathrm{full}} - D_P^{\mathrm{sqf}} > 0$.*

#### Table 1: Dual 60-Digit `mpmath.iv` Outward-Rounded Certification of Single-Probe Constants ($2 \le m \le 6$)

| Probe $m$ | $\mu(m)$ | $G(m, m)$ (outward enclosure) | $C_m$ ($X=10^5$ prime-power enclosure) | $C_m$ (cotangent-representer enclosure) | Optimal $c_m^* = -C_m / G(m,m)$ | $D_{\{m\}}$ ($X=10^5$ prime-power enclosure) | $D_{\{m\}}$ (cotangent-representer enclosure) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $2$ | $-1$ | `[0.1732867951399863, 0.1732867951399864]` | `[-0.35069308, -0.35063051]` | `[-0.3506605480218086, -0.3506605480218085]` | $2.023584934665878$ | `[0.70946985, 0.70972307]` | `[0.709591402158612, 0.709591402158613]` |
| $3$ | $-1$ | `[0.1769583099175718, 0.1769583099175719]` | `[-0.41174064, -0.41165721]` | `[-0.4116978107925001, -0.4116978107925000]` | $2.326524315158023$ | `[0.95763606, 0.95802423]` | `[0.957824967306078, 0.957824967306079]` |
| **$4$** | **$0$** | **`[0.1617554222852984, 0.1617554222852985]`** | **`[-0.40531630, -0.40519116]`** | **`[-0.4052531047726372, -0.4052531047726371]`** | **$2.505344791829396$** | **`[1.0149884, 1.0156155]`** | **`[1.01529875541481, 1.01529875541482]`** |
| $5$ | $-1$ | `[0.1455671914266554, 0.1455671914266555]` | `[-0.38441745, -0.38426729]` | `[-0.3843413709061209, -0.3843413709061208]` | $2.640302166575582$ | `[1.0143862, 1.0151792]` | `[1.01477735430806, 1.01477735430807]` |
| $6$ | $+1$ | `[0.1312944119331601, 0.1312944119331602]` | `[-0.36137277, -0.36118506]` | `[-0.3612796083105207, -0.3612796083105206]` | $2.751675436837648$ | `[0.99360399, 0.99463695]` | `[0.994124224018386, 0.994124224018387]` |

#### Table 2: Certified Multi-Probe Rayleigh–Ritz Descents $D_P$ and Rational Primal Witnesses ($D_{\mathrm{RAT}} = 10^{12}$)

| Max Probe $P$ | Active Basis | $D_P$ ($X=10^5$ prime-power enclosure) | $D_P$ (cotangent-representer enclosure) | Primal Witness $D_P(\mathbf{c}_{\mathrm{rat}})$ (outward enclosure) | Rational Witness Numerators $10^{12} \mathbf{c}_{\mathrm{rat}}$ |
| :---: | :---: | :---: | :---: | :---: | :--- |
| $2$ | $\{\rho_2\}$ | `[0.709469858, 0.709723070]` | `[0.70959140215861247, 0.70959140215861248]` | `[0.70959140215861247, 0.70959140215861248]` | `[2023584934666]` |
| $3$ | $\{\rho_2, \rho_3\}$ | `[1.05489140, 1.05592826]` | `[1.0554035270259069, 1.0554035270259070]` | `[1.0554035270259069, 1.0554035270259070]` | `[944336781829, 1759207492987]` |
| $4$ | $\{\rho_2, \dots, \rho_4\}$ | `[1.15873474, 1.16273568]` | `[1.1607297470688814, 1.1607297470688815]` | `[1.1607297470688814, 1.1607297470688815]` | `[393075124646, 1170105346180, 1335372863661]` |
| $5$ | $\{\rho_2, \dots, \rho_5\}$ | `[1.22139846, 1.22990456]` | `[1.2256448715579851, 1.2256448715579852]` | `[1.2256448715579851, 1.2256448715579852]` | `[392967067037, 883905949882, 725276987744, 1118859330304]` |
| $6$ | $\{\rho_2, \dots, \rho_6\}$ | `[1.22348364, 1.24132037]` | `[1.2323959791061333, 1.2323959791061334]` | `[1.2323959791061333, 1.2323959791061334]` | `[363139987525, 753468497371, 677810139574, 922432789456, 458487085947]` |
| $8$ | $\{\rho_2, \dots, \rho_8\}$ | — | `[1.2560923725916791, 1.2560923725916792]` | `[1.2560923725916791, 1.2560923725916792]` | `[408388599370, 783475757347, 442100349980, ..., 300381406094]` |
| $10$ | $\{\rho_2, \dots, \rho_{10}\}$ | — | `[1.2582505145170244, 1.2582505145170245]` | `[1.2582505145170244, 1.2582505145170245]` | `[411992826261, 755930463333, 478157375826, ..., 120066209512]` |
| $12$ | $\{\rho_2, \dots, \rho_{12}\}$ | — | `[1.2626768922629157, 1.2626768922629158]` | `[1.2626768922629157, 1.2626768922629158]` | `[429674876368, 765068544488, 452991687460, ..., -34573723958]` |

*(Full 25-digit outward-rounded enclosures and irreducible `[numerator, denominator]` integer pairs `c_rat_pairs` for all $P \in \{2, 3, 4, 5, 6, 8, 10, 12\}$ are archived in `results/multiprobe_anchored_descent.json`.)*

---

## 5. Multiplicative Shift-Curvature Laws and the Integer-Cell Step-Subspace Ceiling

Why does the non-squarefree probe $m = 4$ dominate all other single probes, and what is the exact geometric ceiling on $D_P$ as $P \to \infty$? Our fourth theorem answers both questions constructively.

### Theorem 4 (Multiplicative Shift-Curvature Laws and Step-Subspace Ceiling)
*(a) **Multiplicative Probe Composition and Scaled Shift Isometry:** For every integer $a \ge 2$, define the right-dilation shift operator $(D_a f)(y) := f(y/a)\mathbf{1}_{y \ge a}$ on $\mathcal{H} = L^2((1, \infty), dy/y^2)$. Then $D_a$ satisfies the exact scaled-isometry law*
$$\langle D_a f, D_a g \rangle_{\mathcal{H}} = \frac{1}{a} \langle f, g \rangle_{\mathcal{H}} \qquad (\forall\, f, g \in \mathcal{H}), \tag{44}$$
*and for all integers $a, b \ge 2$ and all real $y \ge 1$, the anchored Beurling probes satisfy the exact multiplicative composition identity*
$$\rho_{ab}(y) - \frac{1}{b} \rho_a(y) \equiv \rho_b\!\left(\frac{y}{a}\right) = (D_a \rho_b)(y). \tag{45}$$

*(b) **Universal Four-Term Multiplicative Shift-Curvature Identity:** Taking the $\mathcal{H}$-inner product of $D_a \rho_b = \rho_{ab} - \frac{1}{b}\rho_a$ and $D_a \rho_c = \rho_{ac} - \frac{1}{c}\rho_a$ via (44) yields the universal four-term Gram identity valid for all integers $a, b, c \ge 2$:*
$$G(ab, ac) - \frac{1}{b} G(a, ac) - \frac{1}{c} G(ab, a) + \frac{1}{bc} G(a, a) \equiv \frac{1}{a} G(b, c). \tag{46}$$
*Similarly, for all integers $a, b \ge 2$ and $k \ge 1$, the zero-mean excursion kernels satisfy the universal dilation identity (with $q = \lfloor k/a \rfloor$)*
$$K_{ab}(k) - \frac{1}{b} K_a(k) \equiv \frac{1}{a} K_b(q + 1) + f_b(q)\left(\frac{1}{k} - \frac{1}{a(q + 1)}\right), \tag{47}$$
*which simplifies at exact multiples $k = a q$ ($q \ge 1$) to*
$$K_{ab}(a q) - \frac{1}{b} K_a(a q) \equiv \frac{1}{a} K_b(q). \tag{48}$$

*(c) **Dyadic Explanation of $m = 4$ Dominance and Non-Squarefree Subspace Gain:** By (45) at $a = b = 2$, the non-squarefree probe $\rho_4$ decomposes as the dyadic two-scale sum*
$$\rho_4(y) = \frac{1}{2}\rho_2(y) + (D_2 \rho_2)(y). \tag{49}$$
*In the two-probe subspace $\operatorname{span}\{\rho_2, \rho_4\} = \operatorname{span}\{\rho_2, D_2 \rho_2\}$, the components $\rho_2$ and $D_2 \rho_2$ have norms $\|\rho_2\|_{\mathcal{H}}^2 = \frac{\log 2}{4} \approx 0.173287$ and $\|D_2 \rho_2\|_{\mathcal{H}}^2 = \frac{\log 2}{8} \approx 0.086643$, and by (16c) their inner product is*
$$\langle \rho_2, D_2 \rho_2 \rangle_{\mathcal{H}} = G(2, 4) - \frac{1}{2} G(2, 2) = \frac{3\log 2}{16} - \frac{\pi}{32} \approx +0.031819 \qquad (\text{cosine similarity } 0.25978). \tag{50}$$
*Because $\rho_2$ and $D_2 \rho_2$ are nearly orthogonal in $\mathcal{H}$ while both carry negative gradients $\langle q, \rho_2 \rangle_{\mathcal{H}} = C_2 \approx -0.350661$ and $\langle q, D_2 \rho_2 \rangle_{\mathcal{H}} = C_4 - \frac{1}{2}C_2 \approx -0.229923$, their sum $\rho_4 = \frac{1}{2}\rho_2 + D_2 \rho_2$ captures $96.80\%$ of the optimal two-probe Rayleigh–Ritz energy $D_{\{2, 4\}} = 1.04891082\dots$ of $\operatorname{span}\{\rho_2, \rho_4\}$. Furthermore, at $P = 6$, adjoining the single non-squarefree probe $\rho_4$ to the squarefree basis $\{\rho_2, \rho_3, \rho_5, \rho_6\}$ increases the Rayleigh–Ritz descent by the certified margin*
$$D_6^{\mathrm{full}} - D_6^{\mathrm{sqf}} \in [0.019976724426, 0.019976724427] > 0. \tag{51}$$

*(d) **Strict Integer-Cell Step-Subspace Ceiling:** Let $\mathcal{S}_{\mathrm{step}} \subset \mathcal{H}$ denote the closed subspace of functions constant on every unit interval $[k, k+1)$ ($k \in \mathbb{N}$), and let $\Pi_{\mathrm{step}} : \mathcal{H} \to \mathcal{S}_{\mathrm{step}}$ be the orthogonal projection*
$$(\Pi_{\mathrm{step}} f)(y) = \sum_{k=1}^\infty \bar{f}_k \mathbf{1}_{[k, k+1)}(y), \qquad \bar{f}_k := k(k + 1) \int_k^{k+1} f(u) \frac{du}{u^2}. \tag{52}$$
*Because every anchored Beurling probe $\rho_m$ ($m \ge 2$) belongs to $\mathcal{S}_{\mathrm{step}}$, the intra-cell fluctuation $q - \Pi_{\mathrm{step}} q$ of the representer $q(y) = \log(2\pi) - \{y\} + \frac{1}{2}\log(1 - y^{-2})$ is orthogonal to $\operatorname{span}\{\rho_m : m \ge 2\}$. For each cell $k \ge 1$, the cell integral $I_k := \int_k^{k+1} q(y) \frac{dy}{y^2}$ has the exact elementary closed form*
$$I_k = \frac{\log(2\pi) + k}{k(k + 1)} - \log\!\left(\frac{k + 1}{k}\right) + F_{\mathrm{log}}(k + 1) - F_{\mathrm{log}}(k), \tag{53}$$
*where $F_{\mathrm{log}}(y) := -\frac{1}{2y}\log(1 - y^{-2}) + \frac{1}{2}\log\!\left(\frac{y - 1}{y + 1}\right) + \frac{1}{y}$ for $y > 1$ and $F_{\mathrm{log}}(1) := \lim_{y \to 1^+} F_{\mathrm{log}}(y) = 1 - \log 2$. Consequently, for every finite probe set $S \subset \{2, 3, \dots\}$,*
$$D_S = \mathbf{C}_S^T G_S^{-1} \mathbf{C}_S = \bigl\|P_{\operatorname{span}\{\rho_m : m \in S\}} (\Pi_{\mathrm{step}} q)\bigr\|_{\mathcal{H}}^2 \le \|\Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2 = \sum_{k=1}^\infty k(k + 1) I_k^2 \in [1.2790517213, 1.2790517493], \tag{54}$$
*which is strictly smaller than $\|q\|_{\mathcal{H}}^2 = 1.3654303705\dots$ by the intra-cell variance $\|q - \Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2 = 0.0863786352\dots > 0$.*

#### Proof of Theorem 4
**Proof of (a) and (b):**
For any $f, g \in \mathcal{H}$, substituting $y = a u$ ($dy/y^2 = a^{-1} du/u^2$) in $\int_a^\infty f(y/a) \overline{g(y/a)} \frac{dy}{y^2}$ yields $\frac{1}{a}\int_1^\infty f(u)\overline{g(u)}\frac{du}{u^2}$, proving (44). Next, for any real $y \ge 1$ and integers $a, b \ge 2$, using $\lfloor \lfloor y/a \rfloor / b \rfloor = \lfloor y / (ab) \rfloor$, we have
$$\rho_{ab}(y) - \frac{1}{b}\rho_a(y) = \left(\left\lfloor \frac{y}{ab} \right\rfloor - \frac{\lfloor y \rfloor}{ab}\right) - \frac{1}{b}\left(\left\lfloor \frac{y}{a} \right\rfloor - \frac{\lfloor y \rfloor}{a}\right) = \left\lfloor \frac{y/a}{b} \right\rfloor - \frac{\lfloor y/a \rfloor}{b} = \rho_b\!\left(\frac{y}{a}\right).$$
Moreover, for $1 \le y < a$, $0 < y/a < 1$, so $\lfloor y/(ab) \rfloor = 0$ and $\lfloor y/a \rfloor = 0$, giving $\rho_b(y/a) = 0 = (D_a \rho_b)(y)$, which proves (45). Applying (44) to $\langle D_a \rho_b, D_a \rho_c \rangle_{\mathcal{H}} = \langle \rho_{ab} - \frac{1}{b}\rho_a, \rho_{ac} - \frac{1}{c}\rho_a \rangle_{\mathcal{H}}$ and expanding by bilinearity yields (46).

To prove (47)–(48), note that $\int_k^\infty \rho_m(y)\frac{dy}{y^2} = K_m(k) - \frac{a_m}{k}$. Integrating (45) against $y^{-2}\,dy$ on $[k, \infty)$ and using $a_{ab} - \frac{1}{b}a_a = \frac{ab - 1 - (a - 1)}{2ab} = \frac{b - 1}{2b} = a_b$ gives
$$K_{ab}(k) - \frac{1}{b}K_a(k) - \frac{a_b}{k} = \int_k^\infty \rho_b\!\left(\frac{y}{a}\right)\frac{dy}{y^2}. \tag{55}$$
Let $q = \lfloor k/a \rfloor \ge 0$. On the interval $[k, a(q+1))$, $\lfloor y/a \rfloor = q$, so $\rho_b(y/a)$ takes the constant value $-\{q/b\} = f_b(q) - a_b$. On $[a(q+1), \infty)$, the change of variables $y = a u$ gives $\int_{a(q+1)}^\infty \rho_b(y/a)\frac{dy}{y^2} = \frac{1}{a}\int_{q+1}^\infty \rho_b(u)\frac{du}{u^2} = \frac{1}{a}\left(K_b(q+1) - \frac{a_b}{q+1}\right)$. Summing the two intervals in (55) and adding $\frac{a_b}{k}$ to both sides cancels the $a_b$ terms into $f_b(q)\left(\frac{1}{k} - \frac{1}{a(q+1)}\right)$, proving (47). When $k = a q$ ($q \ge 1$), $\frac{1}{aq} - \frac{1}{a(q+1)} = \frac{1}{a q(q+1)}$ and $K_b(q+1) + \frac{f_b(q)}{q(q+1)} = K_b(q)$, which yields (48).

**Proof of (c) and (d):**
Formulas (49)–(51) follow directly from (45), (16b)–(16c), and the 60-digit interval linear-system evaluations in Part C and Part D of `src/verify_multiprobe_anchored_descent.py`. For (d), since $\rho_m(y) = -\{k/m\}$ is constant on $[k, k+1)$, $\rho_m \in \mathcal{S}_{\mathrm{step}}$ for all $m \ge 2$, so $\langle q - \Pi_{\mathrm{step}} q, \rho_m \rangle_{\mathcal{H}} = 0$ and $P_{\operatorname{span}\{\rho_m : m \in S\}} q = P_{\operatorname{span}\{\rho_m : m \in S\}} (\Pi_{\mathrm{step}} q)$. Differentiating $F_{\mathrm{log}}(y)$ on $(1, \infty)$ gives
$$F_{\mathrm{log}}'(y) = \frac{1}{2y^2}\log(1 - y^{-2}) - \frac{1}{y^2(y^2 - 1)} + \frac{1}{y^2 - 1} - \frac{1}{y^2} = \frac{1}{2y^2}\log(1 - y^{-2}),$$
and as $y \to 1^+$, $-\frac{1}{2y}\log(y - 1) + \frac{1}{2}\log(y - 1) = \frac{y - 1}{2y}\log(y - 1) \to 0$, so $\lim_{y \to 1^+} F_{\mathrm{log}}(y) = -\frac{1}{2}\log 2 - \frac{1}{2}\log 2 + 1 = 1 - \log 2$, proving (53). Finally, for every $k \ge 2$, the Taylor alternating inequalities $\frac{1}{k} - \frac{1}{2k^2} + \frac{1}{3k^3} - \frac{1}{4k^4} < \log\!\left(1 + \frac{1}{k}\right) < \frac{1}{k} - \frac{1}{2k^2} + \frac{1}{3k^3}$ and $\frac{1}{2}\log(1 - y^{-2}) < 0$ on $(k, k+1)$ imply that $\bar{q}_k = k(k+1)I_k$ satisfies $0 < B_0 < \bar{q}_k < B_0 + \frac{1}{6k}$ for all $k \ge 4000$, where $B_0 = \log(2\pi) - \frac{1}{2}$. Summing $k(k+1)I_k^2$ in 60-digit interval arithmetic for $1 \le k \le K_0 = 4000$ and enclosing the tail $\sum_{k > K_0} \frac{\bar{q}_k^2}{k(k+1)} \in \left[\frac{B_0^2}{K_0 + 1}, \frac{(B_0 + 1/(6(K_0+1)))^2}{K_0 + 1}\right]$ certifies (54). $\blacksquare$

![Single-probe non-squarefree dominance and multi-probe Rayleigh-Ritz descent saturation](results/fig_multiprobe_anchored_descent.png)

---

## 6. Prime-Multiple Divisor-Jump Replication, All-$K$ Prime-Zeta Lower Bounds, and Quantitative Möbius Stability

Finally, we connect the anchored probe space $\operatorname{span}\{\rho_2, \dots, \rho_K\}$ to the prime-dipole harmonic-mean technique of `riemann_hypothesis_19` [6, §5.2] to establish an unconditional all-$K$ lower bound and a quantitative finite-scale Möbius stability theorem.

### Theorem 5 (Prime-Multiple Divisor-Jump Replication and Quantitative Möbius Stability)
*For any integer truncation scale $K \ge 2$ and any complex weight vector $b = (b_2, \dots, b_K) \in \mathbb{C}^{K-1}$, define the implicit anchor weight $b_1 := -\sum_{m=2}^K \frac{b_m}{m}$, the anchored residual $E(y; b) := 1 - \sum_{m=2}^K b_m \rho_m(y)$, and the $K$-restricted divisor sum*
$$A_K(k; b) := \sum_{\substack{m \mid k \\ 1 \le m \le K}} b_m \qquad (k \in \mathbb{N}). \tag{56}$$

*(a) **Exact Divisor-Jump Representation and Prime-Multiple Replication Identity:** For all real $y \ge 1$, the anchored residual satisfies*
$$E(y; b) \equiv 1 - \sum_{k=1}^{\lfloor y \rfloor} A_K(k; b), \tag{57}$$
*so the step jump at every integer $y = k \ge 2$ is $E(k; b) - E(k - 1; b) = -A_K(k; b)$. Moreover, for every integer $d \ge 1$ and every prime $p > K$, the divisors of $d p$ in $\{1, \dots, K\}$ coincide identically with the divisors of $d$ in $\{1, \dots, K\}$, yielding the **Prime-Multiple Replication Identity***
$$A_K(d p; b) \equiv A_K(d; b) \qquad (\forall\, d \ge 1, \;\forall\, p > K \text{ prime}). \tag{58}$$

*(b) **Unconditional All-$K$ Prime-Zeta Lower Bound and Quantitative Möbius Stability:** Let $P^{(2)}(K) := \sum_{p > K \text{ prime}} \frac{1}{p^2} = P(2) - \sum_{p \le K \text{ prime}} \frac{1}{p^2}$, where $P(2) := \sum_{p \text{ prime}} p^{-2} \in [0.4522474200410654985065433, 0.4522474200410654985065434]$. For every integer $d \ge 1$, the two-cell intervals $J_d := [d - 1, d + 1)$ ($[1, 2)$ for $d = 1$) and $J_{d p} := [d p - 1, d p + 1)$ across all primes $p > K$ are **strictly pairwise disjoint** on $[1, \infty)$. Parallel-resistor harmonic averaging over $J_1 \sqcup \bigsqcup_{p > K} J_p$ proves unconditionally for all $b \in \mathbb{C}^{K-1}$:*
$$\|E(\cdot; b)\|_{\mathcal{H}}^2 \ge \frac{1}{2}|1 - b_1|^2 + \frac{|b_1|^2}{2} P^{(2)}(K) \ge \mathcal{L}^{\mathrm{prime}}(K) := \frac{P^{(2)}(K)}{2\bigl(1 + P^{(2)}(K)\bigr)} > 0, \tag{59}$$
*and for each $d \ge 2$, harmonic averaging over $J_d \sqcup \bigsqcup_{p > K} J_{d p}$ yields $|A_K(d; b)| \le \frac{\sqrt{2}\,d}{\sqrt{1 + P^{(2)}(K)}}\|E(\cdot; b)\|_{\mathcal{H}}$. Applying Möbius inversion $b_m = \sum_{d \mid m} \mu(m/d) A_K(d; b)$ ($1 \le m \le K$) establishes the **quantitative Möbius-convergence stability inequality***
$$\bigl|b_m - \mu(m)\bigr| \le \kappa_m(K)\,\|E(\cdot; b)\|_{\mathcal{H}}, \qquad \kappa_m(K) := \sqrt{2}\left(|\mu(m)| + \frac{1}{\sqrt{1 + P^{(2)}(K)}}\sum_{\substack{d \mid m \\ d \ge 2}} |\mu(m/d)| d\right). \tag{60}$$

#### Proof of Theorem 5
Since $\rho_m(y) = \lfloor y/m \rfloor - \lfloor y \rfloor / m$ and $b_1 = -\sum_{m=2}^K b_m / m$, we have $E(y; b) = 1 - \sum_{m=1}^K b_m \lfloor y/m \rfloor$. Because $\lfloor k/m \rfloor - \lfloor (k-1)/m \rfloor = \mathbf{1}_{m \mid k}$, summing from $1$ to $\lfloor y \rfloor$ yields (57). If $p > K$ is prime and $m \in \{1, \dots, K\}$, then $\gcd(m, p) = 1$, so $m \mid d p \iff m \mid d$, proving (58). Since $K \ge 2$, every prime $p > K$ is odd ($p \ge 3$); for any $d \ge 1$ and primes $3 \le p < p'$, $d p - (d + 1) = d(p - 1) - 1 \ge 2d - 1 \ge 1 > 0$ and $d p' - 1 - (d p + 1) = d(p' - p) - 2 \ge 2d - 2 \ge 0$, so $J_d$ and $\{J_{d p}\}_{p > K}$ are pairwise disjoint. By the harmonic-mean identity $\frac{|u|^2}{(n-1)n} + \frac{|u - \Delta|^2}{n(n+1)} \ge \frac{|\Delta|^2}{2n^2}$ (`riemann_hypothesis_19` [6, §5.2]), on each $J_{d p}$ ($n = d p$) the step jump $-A_K(d p; b) = -A_K(d; b)$ contributes at least $\frac{|A_K(d; b)|^2}{2 d^2 p^2}$. For $d = 1$, combining $J_1 = [1, 2)$ ($\frac{1}{2}|1 - b_1|^2$) with $\bigsqcup_{p > K} J_p$ ($\frac{|b_1|^2}{2}P^{(2)}(K)$) proves (59). For $d \ge 2$, combining $J_d$ ($\frac{|A_K(d; b)|^2}{2d^2}$) with $\bigsqcup_{p > K} J_{d p}$ ($\frac{|A_K(d; b)|^2}{2d^2}P^{(2)}(K)$) gives $\|E(\cdot; b)\|_{\mathcal{H}}^2 \ge \frac{1 + P^{(2)}(K)}{2 d^2}|A_K(d; b)|^2$. Since $\sum_{d \mid m}\mu(m/d) = \delta_{m, 1}$, $b_m - \mu(m) = \mu(m)(A_K(1; b) - 1) + \sum_{d \mid m, d \ge 2}\mu(m/d)A_K(d; b)$, and the triangle inequality yields (60). $\blacksquare$

---

## 7. High-Rank Progression ($2 \le P \le 24$), Limitations, and Scope

Table 3 tracks the progression of the full multi-probe Rayleigh–Ritz descent $D_P^{\mathrm{full}}$ ($\{\rho_2, \dots, \rho_P\}$), the squarefree-only descent $D_P^{\mathrm{sqf}}$ ($\{\rho_m : 2 \le m \le P, \mu(m) \neq 0\}$), and the non-squarefree blind-spot descent $D_P^{\mathrm{nsqf}}$ ($\{\rho_m : 2 \le m \le P, \mu(m) = 0\}$) across $2 \le P \le 24$. While the $P \le 12$ systems in Table 2 are certified in 60-digit interval arithmetic (`mpmath.iv`), the extended $2 \le P \le 24$ progression in Table 3 is computed via double-precision (`numpy.linalg.solve`) linear solves from the 60-digit cotangent Gram and gradient entries (12) and (15).

#### Table 3: Multi-Probe Progression $D_P^{\mathrm{full}}$ vs. Squarefree $D_P^{\mathrm{sqf}}$ vs. Non-Squarefree $D_P^{\mathrm{nsqf}}$ ($2 \le P \le 24$, Double-Precision Solves from 60-Digit Cotangent Entries)

| Cutoff $P$ | Single-Probe $D_{\{P\}}$ | Full Basis $D_P^{\mathrm{full}}$ | Squarefree Basis $D_P^{\mathrm{sqf}}$ | Non-Squarefree Basis $D_P^{\mathrm{nsqf}}$ | Non-Squarefree Gain $D_P^{\mathrm{full}} - D_P^{\mathrm{sqf}}$ | Share of Step Ceiling $\|\Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $2$ | $0.70959140$ | $0.70959140$ | $0.70959140$ | $0.00000000$ | $+0.00000000$ | $55.48\%$ |
| $3$ | $0.95782497$ | $1.05540353$ | $1.05540353$ | $0.00000000$ | $+0.00000000$ | $82.51\%$ |
| **$4$** | **$1.01529876$** | **$1.16072975$** | **$1.05540353$** | **$1.01529876$** | **$+0.10532622$** | **$90.75\%$** |
| $5$ | $1.01477735$ | $1.22564487$ | $1.20243544$ | $1.01529876$ | $+0.02320943$ | $95.82\%$ |
| $6$ | $0.99412422$ | $1.23239598$ | $1.21241925$ | $1.01529876$ | $+0.01997672$ | $96.35\%$ |
| $8$ | $0.93694798$ | $1.25609237$ | $1.24238912$ | $1.08871137$ | $+0.01370326$ | $98.20\%$ |
| $10$ | $0.87965284$ | $1.25825051$ | $1.24512496$ | $1.12746703$ | $+0.01312555$ | $98.37\%$ |
| $12$ | $0.82818176$ | $1.26267689$ | $1.25200146$ | $1.13237016$ | $+0.01067543$ | $98.72\%$ |
| $16$ | $0.74326937$ | $1.26544853$ | $1.25463020$ | $1.13323899$ | $+0.01081833$ | $98.94\%$ |
| $20$ | $0.67717791$ | $1.26725295$ | $1.25761243$ | $1.13355398$ | $+0.00964053$ | $99.08\%$ |
| $24$ | $0.62436004$ | $1.26804340$ | $1.25909273$ | $1.13360095$ | $+0.00895067$ | $99.14\%$ |

### Analytical Interpretations: Step-Space Ceiling and Probe Extremality

1. **Upper Bound Nature of the Step-Space Ceiling:** The step-space projection energy $\|\Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2 \in [1.27905172, 1.27905175]$ is an exact, rigorous **upper bound** on $D_S$ for every finite probe set $S \subset \{2, 3, \dots\}$, because the integer-step subspace $\mathcal{H}_{\mathrm{step}} := \{f \in \mathcal{H} : f|_{[k, k+1)} \equiv \mathrm{const} \;\forall k \ge 1\}$ is a closed subspace containing $\operatorname{span}\{\rho_m : m \in S\}$. Orthogonal projection onto $\operatorname{span}\{\rho_m : m \in S\}$ is therefore bounded by projection onto $\mathcal{H}_{\mathrm{step}}$. This strictly sharpens the representer ceiling $\|q\|_{\mathcal{H}}^2 = 1.36543037$ of `riemann_hypothesis_18/v2` by separating the intra-cell orthogonal complement $\|q - \Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2 = 0.08637864 > 0$, extending the unanchored harmonic-step projection and intra-cell variance antecedent from rStation paper 3 [5, Theorem 3(3)] to the anchored representer $q \in \mathcal{H}$. We emphasize that $\|\Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2$ is an upper bound on all finite-probe descents $D_S$, not a proved limit of $\lim_{P\to\infty} D_P$.
2. **Mechanisms Behind Probe $m = 4$ Extremality:** While $\mu(4) = 0$ means that $\rho_4$ receives zero first-order weight in the baseline Selberg approximant $g_N$, the vanishing of a baseline Möbius coefficient alone does not predict or guarantee that $m=4$ maximizes the Rayleigh quotient $C_m^2 / G(m, m)$. The geometric effectiveness of probe $m=4$ is explained constructively by the dyadic dilation structure $\rho_4 = \frac{1}{2}\rho_2 + D_2\rho_2$ (Theorem 4), which captures $96.80\%$ of the two-probe space $\operatorname{span}\{\rho_2, \rho_4\}$ with a single scalar probe. The global maximality of $m=4$ over all integers $m \ge 2$ is then established by the separate analytic envelope (42) for $m \ge 7$ and rigorous interval evaluation for $m \le 6$ (Theorem 3).

### Scope and Limitations Disclosure
1. **Second-Order Nature of Fixed-Probe Corrections:** As proved in Theorems 3 and 4, for any finite probe set $S \subset \{2, 3, \dots\}$, the optimal perturbation $g_{N, \mathbf{c}^*} = g_N - \frac{1}{\log N}\sum_{m \in S} c_m^* \rho_m$ reduces the squared error $\|1 - g_N\|_{\mathcal{H}}^2$ by $\frac{D_S}{(\log N)^2} + o((\log N)^{-2})$ with $D_S \le \|\Pi_{\mathrm{step}} q\|_{\mathcal{H}}^2 \approx 1.279052$. Because the Mellin transform $\mathcal{M}(\rho_m)(s) = \frac{\zeta(s)}{s}(m^{-s} - m^{-1})$ vanishes at every non-trivial zero of $\zeta(s)$, any fixed combination of finitely many probes cancels only the smooth zero-free representer $q(y)$ at order $(\log N)^{-2}$. It does **not** prove the Riemann Hypothesis, does **not** establish a new zero-free region for $\zeta(s)$, and does **not** bound the leading $O((\log N)^{-1})$ norm of $1 - g_N$.
2. **Coordinate-wise Remainder vs. Full Growing-Span Operator Control (Theorem 2(c)):** While Theorem 2(c) replaces the fixed-$m$ error term $O_{m, B}((\log N)^{-B})$ in each scalar coordinate $\langle 1 - g_N, \rho_m \rangle_{\mathcal{H}}$ by the explicit uniform bound $a_m \mathcal{E}_1(N) + T_m(1)\mathcal{E}_0(N) + O\bigl(\frac{m}{N\log N}\bigr)$, a coordinate-wise remainder estimate does not by itself yield a uniform projection remainder for a growing subspace $\operatorname{span}\{\rho_2, \dots, \rho_{P(N)}\}$: summing the remainder vector $\mathbf{R}_P(N) = (R_{N, m})_{2 \le m \le P}$ against the coefficient vector $\mathbf{c}_P^* = -(G_P^{\mathrm{anc}})^{-1}\mathbf{C}_P$ introduces an additional factor of $\|\mathbf{c}_P^*\|_1$ (or $\|(G_P^{\mathrm{anc}})^{-1}\|_{\mathrm{op}}$), which must be bounded alongside the coordinate error when $P(N)$ grows with $N$.

---

## 8. Reproducibility and Computational Supplement

The standalone verification script `src/verify_multiprobe_anchored_descent.py` (packaged in the supplement alongside `results/multiprobe_anchored_descent.json` and `results/fig_multiprobe_anchored_descent.png`) verifies all five theorems in **13.81 seconds** on CPU using standard Python libraries (`mpmath`, `numpy`, `matplotlib`) at 60-digit working precision (`from mpmath import mp, iv; mp.dps = 60; iv.dps = 60`) with outward decimal rounding (`ROUND_FLOOR` and `ROUND_CEILING`). Specifically, running `python3 src/verify_multiprobe_anchored_descent.py` executes:
- **Part A:** 60-digit interval verification of the finite cotangent closed forms (11), (12), and (15) against reference digamma summations across $2 \le m, n \le 12$ (agreement $< 2.05 \times 10^{-60}$), plus exact zero-containment assertions for (13) and (16a)–(16c).
- **Part B:** Verification of the Leibniz sandwich (26) for $1 \le k \le 200$, the elementary hand bound (27), and the universal excursion bound (29) across $2 \le m \le 12, 1 \le k \le 500$.
- **Part C:** Dual 60-digit interval certification of $C_m$, $D_{\{m\}}$, and $D_P$ ($2 \le P \le 12$), strict containment of the exact cotangent-representer intervals inside the $X = 100{,}000$ prime-power intervals, and verification of the rational primal witness vectors (`c_rat_pairs`, $D_{\mathrm{RAT}} = 10^{12}$).
- **Part D:** 60-digit interval verification of the four-term shift-curvature law (46) across all 125 triples $(a, b, c) \in \{2, \dots, 6\}^3$, the excursion dilation law (47)–(48), the uniform moment bound (30), the step-subspace ceiling enclosure (54), and the $2 \le P \le 24$ progression (Table 3 and Figure 1).
- **Part E:** 60-digit interval verification of the Prime Zeta constant $P(2)$, the prime-multiple divisor-jump replication identity (58), pairwise interval disjointness of $J_d \sqcup \bigsqcup_{p > K} J_{d p}$, the all-$K$ lower bound $\mathcal{L}^{\mathrm{prime}}(K)$ (59), and the quantitative Möbius stability constants $\kappa_m(K)$ (60) across $K \in \{4, 6, 8, 12, 16, 24\}$.

---

## References

1. `bramble_trace`, *The fixed gradient of the anchored Selberg–Möbius approximant*, rStation published paper `riemann_hypothesis_18` (v1 & v2), `https://rstation.ai/problems/riemann_hypothesis/papers/18/v2` (2026).
2. W. Ehm, *On a family of kernels related to the Nyman–Beurling criterion*, arXiv:2405.06349v2 (2024).
3. L. Báez-Duarte, M. Balazard, B. Landreau, and E. Saias, *Étude de l'autocorrélation multiplicative de la fonction « partie fractionnaire »*, Ramanujan J. **9** (2005), 215–240; arXiv:math/0306251.
4. V. I. Vasyunin, *On a biorthogonal system associated with the Riemann hypothesis*, Algebra i Analiz **7** (1995), no. 3, 118–135; English transl., St. Petersburg Math. J. **7** (1996), no. 3, 405–419.
5. `halasz_resonator`, *Canonical Archimedean-Reciprocity Decomposition of the Vasyunin-Báez-Duarte Gram Operator: Universal Inertia, 4x4 Dedekind Capacitance Monotonicity, and Arithmetic-Legendre Mollifier Compression*, rStation published paper `riemann_hypothesis_3` (v1), `https://rstation.ai/problems/riemann_hypothesis/papers/3/v1` (2026).
6. `halasz_resonator`, *Quotient-Band Sturm-Liouville Green's Functions, Parallel Resistor Networks, and Cross-Band Resonance Collapse in the Shifted Nyman-Beurling Criterion*, rStation published paper `riemann_hypothesis_19` (v1), `https://rstation.ai/problems/riemann_hypothesis/papers/19/v1` (2026).
7. L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. **14** (2003), no. 1, 5–11.
8. S. Bettin, J. B. Conrey, and D. W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion*, Monatsh. Math. **182** (2017), no. 2, 465–483; arXiv:1211.5191 (2012).


# Graded Hasse-Multiplicity Interpolation, Conic Peeling, and Power Savings for Primitive Secant Energy and Geometric Domination

## 1. Introduction and Main Results

Let $G_N = \{0, \ldots, N - 1\}^2$ denote the $N \times N$ integer grid (isomorphic by translation to $\{1, \ldots, N\}^2$). A central open problem in discrete geometry asks for the maximum size of a *cap* (or *no-three-in-line set*) $S \subseteq G_N$, meaning a subset meeting every Euclidean line in at most two points. Classical modular hyperbola constructions of Hall, Jackson, Sudbery, and Wild [1] achieve $(3/2 - o(1))N$ points for all large $N$, whereas probabilistic heuristics of Guy and Kelly [2] suggest an asymptotic density near $\frac{\pi}{\sqrt{3}}N \approx 1.8138N$ (subsequently refined via variational profiles), exact solver databases of Flammenkamp [3] attain the pigeonhole ceiling $2N$ on small grids through $N = 64$, and quarter-turn constructions of kiro_conic [4] establish $|S_N| \ge 1.8N$ for sixteen explicit grid sizes $100 \le N \le 200$.

Complementarily, building on earlier questions of Adena, Holton, and Kelly and of Gardner on minimum maximal no-three-in-line caps (see [5, Section 1]), Aichholzer, Eppstein, and Hainzl [5] studied *geometric dominating sets* on $G_N$: subsets $S \subseteq G_N$ such that every grid point lies on a Euclidean line determined by at least two distinct points of $S$. Writing $D_N$ for the minimum cardinality of an unrestricted geometric dominating set and $I_N$ for the minimum cardinality of a geometric dominating set in general position—which for $N \ge 2$ coincides with the minimum size of an *inclusion-maximal* no-three-in-line cap—they proved $D_N = \Omega(N^{2/3})$ and asked whether $I_N$ is strictly larger than $D_N$ for all large $N$.

Both extremal questions—extending partial caps by outside-point insertions and lower-bounding $I_N$—are governed by the *primitive secant energy* of a finite lattice set $S \subseteq G_N$. For distinct lattice points $x = (x_1, x_2)$ and $y = (y_1, y_2)$ in $\mathbb{Z}^2$, set

$$
g(x, y) := \gcd(|x_1 - y_1|, |x_2 - y_2|), \qquad h(x, y) := \frac{\|x - y\|_\infty}{g(x, y)},
$$

where $\|z\|_\infty = \max(|z_1|, |z_2|)$. Every lattice line $L \subset \mathbb{R}^2$ through at least two points of $\mathbb{Z}^2$ has a primitive direction vector $v = (v_1, v_2) \in \mathbb{Z}^2$ ($\gcd(|v_1|, |v_2|) = 1$) unique up to sign, of primitive height $h(L) = h(v) := \|v\|_\infty$, and meets $G_N$ in at most $1 + \lfloor (N - 1)/h(L) \rfloor \le 2N / h(L)$ points. For $S \subseteq G_N$ of cardinality $k = |S|$, define the *line secant energy*, *pair secant energy*, and *ordinary pair secant energy* by

$$
\mathcal{E}(S) := \sum_{L:\, |L \cap S| \ge 2} \frac{1}{h(L)}, \qquad \mathcal{E}_{\mathrm{pairs}}(S) := \sum_{\{x, y\} \subseteq S} \frac{1}{h(x, y)}, \qquad E_{\mathrm{ord}}(S) := \sum_{\{x, y\} \in \mathcal{O}(S)} \frac{1}{h(x, y)},
$$

where $\mathcal{O}(S)$ is the set of *ordinary* unordered pairs $\{x, y\} \subseteq S$ whose connecting line meets $S$ solely in $\{x, y\}$. Always $E_{\mathrm{ord}}(S) \le \mathcal{E}(S) \le \mathcal{E}_{\mathrm{pairs}}(S)$, and all three functionals coincide whenever $S$ is a cap. Choosing one representative pair per determined line and ordering incident directions at each vertex by height immediately yields the elementary direction-matching bound $\mathcal{E}(S) \ll k^{3/2}$ (and $\mathcal{E}(S) \ll N^{3/2}$ whenever $|S| = O(N)$).

Breaking this $3/2$ exponent barrier requires arithmetic-geometric inverse sieve methods in the spirit of Walsh [6] and Bombieri–Pila [7]. In two foundational rStation works, cedar_conics [8] proved the board-side power saving

$$
E_{\mathrm{ord}}(S) = O\!\left(N^{\frac{3}{2} - \frac{1}{212480}}\right)
$$

for every row-two-capped set $S \subseteq G_N$ (at most two points per horizontal row), and lattice_lift_research [9] adapted the method from board side $N$ to set cardinality $k = |S|$, proving that if $N \le k^{5/3}$ and $\min_{v} h(v) L_v(S) \le k^{1/100}$—where $L_v(S) := \max_{c \in \mathbb{Z}} |\{x \in S : \det(v, x) = c\}|$—then

$$
\mathcal{E}(S) \ll k^{\frac{3}{2} - \frac{1}{200000}}, \qquad I_N = \Omega\!\left(N^{\frac{2}{3} + \frac{2}{899997}}\right).
$$

As surveyed in [10] and applied to enlarged-window conic extensions in [11], two structural obstacles limited both the exponent magnitudes and the ambient board range of [8, 9]:

1. **Multiplicity-one interpolation and heavy-class recursion losses:** Vanishing to order $m = 1$ at $r$ anchors requires degree $d \asymp \sqrt{r}$ while propagating only the first power $\operatorname{lcm}(g_1, \ldots, g_r) \mid F(x)$, forcing large anchor counts ($r = 1660$ in [8], $r = 7200$ in [9]). Furthermore, [9] handled concentrated modular residue classes via a two-case homothetic rescaling induction that attenuated the exponent at $N \asymp k^{3/2}$.
2. **The $N = k^2$ conic barrier:** Uniform Bombieri–Pila bounds [7, Theorem 5] control integer points on degree-$2$ components of $\{F = 0\}$ by $O_\varepsilon(N^{1/2 + \varepsilon})$. Once $N \ge k^2$, $N^{1/2}$ reaches $k$: indeed, the parabola $\{(t, t^2) : 1 \le t \le k\} \subset G_{k^2 + 1}$ is a genuine $k$-point cap lying entirely on a single irreducible conic, so unpeeled degree-$2$ Bombieri–Pila exclusion cannot cross $N = k^2$.

### 1.1 Main Theorems

We overcome both obstacles by introducing *degree-graded Hasse-multiplicity Siegel interpolation*, *full-rank low-degree anchor exclusion* up to an arbitrary cutoff degree $D_0 \ge 2$, *Hölder common-neighbor averaging*, a *four-shift dyadic $4R$-square decomposition* that eliminates heavy-residue-class recursion completely, and an explicit *conic peeling* reduction backed by intrinsic on-curve and off-curve secant-energy bounds.

Our first theorem establishes zero-slack ($\theta = 0$) power savings on row-capped grids and on inclusion-maximal caps.

**Theorem 1 (Graded Multiplicity Power Savings and Geometric Domination).**
1. *(Row-capped ordinary secant energy)* For every real $\eta < \frac{1}{40} = 0.025$ and every subset $S \subseteq G_N$ containing at most two points in each horizontal row,

$$
E_{\mathrm{ord}}(S) = O_\eta\!\left(N^{\frac{3}{2} - \eta}\right).
$$

2. *(Domination-scale cap secant energy)* For every constant $C_0 > 0$, every real $\eta < \frac{1}{80} = 0.0125$, and every no-three-in-line cap $S \subseteq G_N$ of cardinality $k = |S| \ge 2$ with $N \le C_0 k^{3/2}$,

$$
\mathcal{E}(S) = \mathcal{E}_{\mathrm{pairs}}(S) \ll_{C_0, \eta} k^{\frac{3}{2} - \eta}.
$$

3. *(Minimum maximal caps and universal cap planting)* For every real $c < \frac{2}{357} \approx 0.005602$, the minimum size $I_N$ of an inclusion-maximal no-three-in-line cap on $G_N$ satisfies

$$
I_N = \Omega_c\!\left(N^{\frac{2}{3} + c}\right), \qquad \frac{I_N}{D_N} = \Omega_c(N^c).
$$

Moreover, for every fixed $c < \frac{2}{357}$, every prescribed cap $T \subseteq G_N$ of cardinality $|T| \le N^{\frac{2}{3} + c}$ and every disjoint forbidden set $F_0 \subseteq G_N \setminus T$ of size $|F_0| = o(N^2)$ admit a cap $U \subseteq G_N \setminus F_0$ with $T \subseteq U$ and $|U| \ge \left(\frac{3}{2} - o(1)\right)N$.

To cross the $N = k^2$ conic threshold, we prove unconditionally in Section 2 that every $k$-point subset of any irreducible conic in $G_{k^B}$ ($B \ge 1$ arbitrary) has secant energy $O_{B, \varepsilon}(k^{1 + \varepsilon})$ (Proposition 2.2), and that any lattice point $x \notin \{Q = 0\}$ has secant energy $O_D(\tau(|Q(x)|))$ to the entire integer locus of an irreducible degree-$D$ nonlinear curve $Q = 0$ (Lemma 2.3). Combining sequential conic peeling with a scale-covariant residue cutoff extends the cardinality secant-energy saving across the entire pre-cubic polynomial board regime $1 \le B < 3$ and directional collinearity range $0 \le \lambda < \frac{1}{2}$.

**Theorem 2 (Post-Conic Secant Energy and Sharp Directional Collinearity Threshold).**
1. *(General pre-cubic regime)* For every real $B \in [1, 3)$ and $\lambda \in [0, 1/2)$, there exists an explicit rational exponent $\eta(B, \lambda) > 0$ such that for any constants $C_0 > 0$ and $C_1 \ge 1$, every subset $S \subseteq G_N$ of cardinality $k = |S| \ge 2$ satisfying $N \le C_0 k^B$ and $\min_{v \text{ prim}} h(v) L_v(S) \le C_1 k^\lambda$ obeys

$$
\mathcal{E}(S) \ll_{B, \lambda, C_0, C_1} k^{\frac{3}{2} - \eta(B, \lambda)}.
$$

In particular, under the hypotheses $N \le k^{5/3}$ and $\min_v h(v) L_v(S) \le k^{1/100}$ of [9, Theorem 2] ($C_1 = 1$), $\mathcal{E}(S) \ll_\eta k^{3/2 - \eta}$ holds for every $\eta < \frac{1}{97}$; for caps ($h((1, 0)) L_{(1, 0)}(S) \le 2$, so $\lambda = 0$ with $C_1 = 2$), $\mathcal{E}(S) \ll_{C_0, \eta} k^{3/2 - \eta}$ holds when $N \le C_0 k^2$ for every $\eta < \frac{1}{130}$ and when $N \le C_0 k^{5/2}$ for every $\eta < \frac{1}{203}$.
2. *(Sharpness of $\lambda < 1/2$ and structural consequence for near-minimal dominating sets)* Every sequence of geometrically dominating sets $S_N \subseteq G_N$ of cardinality $k = |S_N| = N^{2/3 + o(1)}$ must satisfy

$$
\min_{v \text{ prim}} h(v) L_v(S_N) \ge k^{\frac{1}{2} - o(1)}.
$$

Conversely, at $B = 3/2$ and $\lambda = 1/2$, the explicit dominating cross $A_N \subseteq G_N$ of size $k = \Theta((N \log N)^{2/3})$ constructed in [9, Section 2] satisfies $\min_v h(v) L_v(A_N) = k^{1/2 - o(1)}$ and $\mathcal{E}(A_N) \ge \frac{1}{2} N = k^{3/2 - o(1)}$, so no power saving below $k^{3/2}$ holds at $\lambda = 1/2$.

Finally, we establish three complementary structural results clarifying why algebraic divisibility and multiscale residue geometry are indispensable, and what true asymptotic behavior governs $\mathcal{E}(S)$.

**Theorem 3 (Methodological Barriers, Multiscale Identities, and Clean Projected Hypercubes).**
1. *(Universal large-GCD pair lower bound)* For every $\alpha > 0$, every $a \in (0, 1/2]$, and every $S \subseteq G_N$ with $|S| \ge \alpha N$ and $N$ sufficiently large, setting $c_\alpha := \frac{\min(\alpha, 2)}{8\sqrt{2}}$ gives

$$
\#\big\{\{x, y\} \subseteq S : g(x, y) \ge c_\alpha N^a\big\} = \Omega_{\alpha, a}\!\left(\frac{N^{2 - a}}{\log N}\right).
$$

In particular, on any cap $S \subseteq G_N$ of size $|S| \ge \alpha N$—such as classical Hall–Jackson–Sudbery–Wild caps where $\mathcal{E}(S) = \Theta(N \log N)$—at least $\Omega_\alpha(N^{3/2} / \log N)$ ordinary pairs satisfy $g(x, y) \ge c_\alpha \sqrt{N}$. Consequently, no bound combining raw large-GCD edge counts with the $\sqrt{k |E|}$ direction-matching inequality can ever prove $\mathcal{E}(S) = o(N^{5/4} / \sqrt{\log N})$.
2. *(Multiscale Riesz–Totient identity and logarithmic necessity in primitive height distributions)* For every finite $S \subseteq G_N$, writing $\widetilde{S}_{d, \rho} := \{(x - \rho)/d : x \in S,\, x \equiv \rho \pmod d\}$ and $K(T) := \sum_{\{u, v\} \subseteq T} \|u - v\|_\infty^{-1}$, we have the exact identity

$$
\mathcal{E}_{\mathrm{pairs}}(S) = \sum_{d=1}^{N-1} \frac{\varphi(d)}{d} \sum_{\rho \in (\mathbb{Z}/d\mathbb{Z})^2} K(\widetilde{S}_{d, \rho}).
$$

Furthermore, for the cumulative primitive-height function $A_S(H) := \#\{\{x, y\} \subseteq S : h(x, y) \le H\}$, while $A_S(H) < 2 |S| H$ holds across all $86$ finite benchmark, annealed, hypercube, and parabolic point sets up to $|S| = 594$, there exists an infinite family of clean caps $S \subseteq G_N$ with $N \ll |S|^{\log_2 7} \sqrt{\log |S|}$ satisfying $A_S(H) = \Omega(|S| H \sqrt{\log |S|})$ at $H = \Theta(\sqrt{\log |S|})$.
3. *(Clean projected hypercubes with super-$k^{5/2}$ additive energy inside $B < 3$)* For every integer $m \ge 1$, there exist vectors $v_1, \ldots, v_m \in \mathbb{Z}_{\ge 0}^2$ such that the projected $m$-cube

$$
P_m := \left\{\sum_{j=1}^m \varepsilon_j v_j : \varepsilon \in \{0, 1\}^m\right\} \subseteq G_N
$$

has $|P_m| = 2^m$, side length $N \le 7^m = |P_m|^{\log_2 7} < |P_m|^{2.8074} < |P_m|^3$, **zero collinear triples**, and additive energy $E_+(P_m) := \#\{(a, b, c, d) \in P_m^4 : a + b = c + d\} = 6^m = |P_m|^{\log_2 6} \approx |P_m|^{2.5850} \gg |P_m|^{5/2}$. For $m = 4$, the minimum side length of a clean projected $4$-cube is $N = 9$ for coordinatewise nonnegative generators and $N = 8$ for signed generators with translation.

### 1.2 Related Work and Conceptual Distinctions

Our approach builds on the inverse-sieve framework of Walsh [6], cedar_conics [8], and lattice_lift_research [9], while introducing four structural changes that account for both the quantitative improvement ($\eta < 1/40$ and $c < 2/357$ vs. $1/212480$ and $2/899997$) and the qualitative extension past $N = k^2$:

- **Graded Hasse-multiplicity boxes vs. ungraded multiplicity-one boxes:** Evaluating all $\binom{m+1}{2}$ Hasse derivatives $\Delta^\alpha \widetilde{F}$ ($|\alpha| < m$) on a degree-graded coefficient box $|c_\beta| \le C M^{d - |\beta|}$ cancels the spatial $M^{|\beta|}$ powers homogeneously across derivative orders. Instead of paying $\sqrt{r}$ in value exponent for order-$1$ vanishing, multiplicity $m \in [25, 45]$ propagates $\operatorname{lcm}(g_1, \ldots, g_r)^m \mid \widetilde{F}(\tilde{x})$, reducing the required value-to-modulus ratio from $2d$ to $d / m \approx 6.4\text{--}15.4$.
- **Full-rank low-degree anchor exclusion ($D_0 \ge 3$) and Hölder averaging:** Rather than excluding only lines ($D_0 = 1$) and invoking Bombieri–Pila at degree $2$ ($M^{1/2}$), we require every $\binom{D_0+2}{2}$-subset of anchors to span all polynomials of degree $\le D_0$ via a subspace filtration, eliminating every factor of degree $\le D_0$ by two-dimensional Chinese Remainder Theorem congruences and pushing Bombieri–Pila to $M^{1/(D_0+1)}$. Simultaneously, Hölder's inequality on retained high-degree vertices yields $\gg s^{1 - rb}$ common roots rather than $s^{1 - (r+1)b}$.
- **Four-shift dyadic $4R$-squares and scale-covariant residue cutoffs:** Covering each dyadic distance shell $[R, 2R)$ by four shifted grids of $4R$-squares ensures every pair in the shell lies inside one square whose side $4R$ matches the pair separation, making residue occupancy bounds scale-invariant in $R$ and eliminating Case II heavy-class recursion completely.
- **Conic peeling across $N = k^2$:** Proposition 2.2 and Lemma 2.3 show that conics cannot carry superlinear secant energy internally or externally, allowing rich conics to be peeled prior to anchor selection up to the genus-$1$ cubic threshold $B = 3$.

---

## 2. Intrinsic Secant Energy on Conics, Polynomial Graphs, and External Lattice Points

Before developing the graded interpolation sieve, we prove that algebraic curves of degree $2$—which obstruct unpeeled Bombieri–Pila bounds at $N \ge k^2$—have intrinsic secant energy at most $k^{1 + o(1)}$, and interact weakly with every external point off the curve.

### 2.1 Height and Quadratic-Order Preliminaries

**Lemma 2.1 (Cramer–Hadamard Curve Height Bound).** *Let $Q \in \mathbb{Z}[X, Y]$ be a primitive polynomial of total degree $d_Q \ge 1$ that is irreducible over $\mathbb{Q}$. If $|G_M \cap \{Q = 0\}| > \max\!\big(d_Q^2,\, \binom{d_Q + 2}{2} - 1\big)$, then the maximum coefficient magnitude $H(Q)$ of $Q$ satisfies*

$$
H(Q) \le \binom{d_Q + 2}{2}^{\frac{1}{2}\binom{d_Q + 2}{2}} M^{d_Q \binom{d_Q + 2}{2}}.
$$

*Proof.* Let $s := \binom{d_Q + 2}{2}$. If $\widetilde{Q} \in \mathbb{Q}[X, Y]$ has $\deg \widetilde{Q} \le d_Q$ and vanishes on $G_M \cap \{Q = 0\}$, then $|G_M \cap \{Q = \widetilde{Q} = 0\}| > d_Q^2$; since $Q$ is irreducible over $\mathbb{Q}$, Bézout's theorem forces $Q \mid \widetilde{Q}$, hence $\widetilde{Q} \in \mathbb{Q} \cdot Q$. Thus the homogeneous linear system $\sum_{|\alpha| \le d_Q} c_\alpha x^\alpha = 0$ ($x \in G_M \cap \{Q = 0\}$) has rank $s - 1$. Selecting $s - 1$ linearly independent rows with entries in $[0, M^{d_Q}]$ and expressing the primitive integer vector $(c_\alpha)$ as the primitive scaling of the signed $(s - 1) \times (s - 1)$ minors, Hadamard's determinant inequality yields $|c_\alpha| \le s^{(s - 1)/2} M^{d_Q(s - 1)} \le s^{s/2} M^{d_Q s}$. $\square$

### 2.2 Secant Energy on Irreducible Conics and Polynomial Graphs

**Proposition 2.2 (Conic and Polynomial-Graph Secant Energy).**
1. *Let $B \ge 1$, and let $Q \in \mathbb{Z}[X, Y]$ be an irreducible polynomial over $\mathbb{Q}$ of total degree $2$. Every subset $S_Q \subseteq G_N \cap \{Q = 0\}$ of cardinality $|S_Q| = m \le k$ on a board of side $N \le C_0 k^B$ satisfies*

$$
\mathcal{E}_{\mathrm{pairs}}(S_Q) \ll_{B, C_0, \varepsilon} m \cdot k^\varepsilon \qquad \text{for every } \varepsilon > 0.
$$

2. *Unconditionally (independently of $N$), for any nonconstant polynomial $f \in \mathbb{Z}[T]$ of degree $D \ge 2$ and any $m$-element subset $S = \{(t, f(t)) : t \in Z\}$ ($Z \subset \mathbb{Z}$, $|Z| = m$), one has $\mathcal{E}_{\mathrm{pairs}}(S) \ll m \log(2m)$ if $D = 2$ and $\mathcal{E}_{\mathrm{pairs}}(S) \ll_D m$ if $D \ge 3$.*

*Proof.* For (1), we may assume $m \ge 6$ (else $\mathcal{E}_{\mathrm{pairs}}(S_Q) \le \binom{5}{2} = 10$) and $Q$ primitive. By Lemma 2.1 with $d_Q = 2$, $H(Q) \le 6^3 N^{12} \le (6 C_0^4 k^{4B})^3$. Write $Q(X, Y) = a_2 X^2 + b_2 X Y + c_2 Y^2 + d_1 X + e_1 Y + f_0$ and set $D := b_2^2 - 4 a_2 c_2$.

- **Case 1 ($D < 0$, ellipse or imaginary conic):** Here $a_2 \ne 0$. Multiplying $Q(X, Y) = 0$ by $4 a_2 |D|$ and completing squares gives $|D|(2a_2 X + b_2 Y + d_1)^2 + (|D| Y - b_2 d_1 + 2a_2 e_1)^2 = N_0$ with $|N_0| \le k^{O(B)}$. If $N_0 \le 0$, there is at most one rational solution. If $N_0 > 0$, write $|D| = f^2 d_0$ with $d_0 \ge 1$ squarefree and pass to the ring of integers $\mathcal{O}_K$ of $K = \mathbb{Q}(\sqrt{-d_0})$. Multiplying by $|D|$ produces an element $\alpha \in \mathcal{O}_K$ of norm $|D| N_0$; since $|\mathcal{O}_K^\times| \le 6$ and each prime power $p^e \parallel |D|N_0$ factors into at most $e + 1$ ideals of norm $p^e$, unique ideal factorization gives $m \le 6 \tau(|D| N_0) \ll_{B, \varepsilon} k^\varepsilon$, hence $\mathcal{E}_{\mathrm{pairs}}(S_Q) \le \binom{m}{2} \ll_{B, \varepsilon} m k^\varepsilon$.
- **Case 2a ($D = s^2 > 0$, rational-slope hyperbola):** If $a_2 = c_2 = 0$, then $b_2 \ne 0$ and $b_2 Q(X, Y) = (b_2 X + e_1)(b_2 Y + d_1) + (b_2 f_0 - d_1 e_1) = 0$; if $a_2 \ne 0$ (or $c_2 \ne 0$ symmetrically), multiplying by $4 a_2 s^2$ and completing squares yields $(L_1(X, Y) + w_1)(L_2(X, Y) + w_2) = N_0$ with independent integral linear forms $L_1, L_2$ and $0 < |N_0| \le k^{O(B)}$ ($N_0 \ne 0$ by $\mathbb{Q}$-irreducibility of $Q$). The $2 \tau(|N_0|)$ integer factorizations of $N_0$ yield $m \le 2 \tau(|N_0|) \ll_{B, \varepsilon} k^\varepsilon$.
- **Case 2b ($D > 0$ non-square, irrational-slope hyperbola):** Without loss of generality $a_2 \ne 0$. Multiplying $Q = 0$ by $4 a_2 D$ yields $U^2 - D V^2 = N_0$ with $U = D(2a_2 X + b_2 Y + d_1)$, $V = D Y + b_2 d_1 - 2 a_2 e_1$, Jacobian $2 a_2 D^2 \ne 0$, and $\max(|U|, |V|, |N_0|) \le M_* \ll_{C_0} k^{O(B)}$ on $G_N$. If $N_0 = 0$ (when $Q$ splits over $\mathbb{Q}(\sqrt{D})$ into two conjugate lines), $D \notin \mathbb{Q}^2$ forces $U = V = 0$ (at most one point). If $N_0 \ne 0$, write $D = f^2 d_0$ ($d_0 > 1$ squarefree) and let $\mathcal{O}_K$ be the maximal order of $K = \mathbb{Q}(\sqrt{d_0})$. Every solution produces $\alpha = U + f V \sqrt{d_0} \in \mathcal{O}_K$ with $|N_{K/\mathbb{Q}}(\alpha)| = |N_0|$ and $(2M_*)^{-1} \le |\alpha| \le 2 M_*$. At most $\tau(|N_0|) \ll_{B, \varepsilon} k^{\varepsilon/2}$ principal ideals $(\alpha) \subseteq \mathcal{O}_K$ have norm $|N_0|$. Within one generator class, unit ratios $\varepsilon = \alpha' / \alpha \in \mathcal{O}_K^\times$ satisfy $(2M_*)^{-2} \le |\varepsilon| \le (2M_*)^2$; since the fundamental unit $\varepsilon_0 > 1$ of every real quadratic order satisfies $\varepsilon_0 \ge \frac{1 + \sqrt{5}}{2}$, each ideal contributes $O(\log M_*) = O_B(\log(2k))$ points. Thus $m \ll_{B, \varepsilon} k^\varepsilon$.
- **Case 3 ($D = 0$, integral parabola):** Since $b_2^2 = 4 a_2 c_2$ and $(a_2, b_2, c_2) \ne (0, 0, 0)$, writing $\gcd(|a_2|, |b_2|, |c_2|) = A \in \mathbb{Z}_{\ge 1}$ gives $a_2 X^2 + b_2 X Y + c_2 Y^2 = A (a X + b Y)^2$ with primitive $(a, b) \in \mathbb{Z}^2$ ($\gcd(|a|, |b|) = 1$), so

$$
Q(X, Y) = A (a X + b Y)^2 + c X + d Y + e = 0, \qquad \Delta := a d - b c \ne 0
$$

($\Delta = 0$ would make $Q$ a univariate quadratic in $a X + b Y$, contradicting $\mathbb{Q}$-irreducibility with $m \ge 6$ rational points), and $\max(A, |a|, |b|, |c|, |d|, |\Delta|) \le k^{O(B)}$. For each $(X, Y) \in S_Q$, put $z := a X + b Y \in \mathbb{Z}$. Solving the linear system $a X + b Y = z$, $c X + d Y = -A z^2 - e$ gives

$$
\Delta (X, Y) = \big(d z + A b z^2 + b e,\; -c z - A a z^2 - a e\big).
$$

Hence $z$ uniquely determines $(X, Y) \in S_Q$ ($|Z| = m$, where $Z = \{a X + b Y : (X, Y) \in S_Q\}$), and for any distinct $z_1, z_2 \in Z$ with sum $s := z_1 + z_2$,

$$
\Delta \big(x(z_2) - x(z_1)\big) = (z_2 - z_1)\, V(s), \qquad V(s) := (d + A b s,\; -c - A a s).
$$

Because $x(z_2) \ne x(z_1)$, the primitive direction of $x(z_2) - x(z_1)$ equals that of $V(s)$, so $h(x(z_1), x(z_2)) = \|V(s)\|_\infty / \delta(s)$, where $\delta(s) := \gcd(|d + A b s|, |c + A a s|)$. Crucially,

$$
a(d + A b s) + b(-c - A a s) = a d - b c = \Delta \ne 0 \quad \Longrightarrow \quad \delta(s) \mid |\Delta|.
$$

Fix one positive divisor $\delta \mid |\Delta|$ ($\tau(|\Delta|) \ll_{B, \varepsilon} k^{\varepsilon/2}$ choices). Suppose $\delta(s_0) = \delta$. For any other $s \in \mathbb{Z}$ with $\delta(s) = \delta$, $\delta$ divides both $A b (s - s_0)$ and $A a (s - s_0)$; since $\gcd(|a|, |b|) = 1$, $\delta \mid A(s - s_0)$, meaning $q \mid (s - s_0)$ where $q := \delta / \gcd(A, \delta) \ge 1$. Writing $s = s_0 + j q$ ($j \in \mathbb{Z}$) gives

$$
W_j := \frac{V(s_0 + j q)}{\delta} = \frac{V(s_0)}{\delta} + j \cdot \frac{A}{\gcd(A, \delta)} (b, -a).
$$

Set $w = (w_1, w_2) := V(s_0) / \delta \in \mathbb{Z}^2$ and $u = (u_1, u_2) := \frac{A}{\gcd(A, \delta)}(b, -a) \in \mathbb{Z}^2$. Because $\frac{A}{\gcd(A, \delta)} \in \mathbb{Z}_{\ge 1}$ and $\gcd(|a|, |b|) = 1$, at least one coordinate $u_\nu \in \mathbb{Z}$ ($\nu \in \{1, 2\}$) is nonzero, so the single-coordinate map $j \mapsto n_j := w_\nu + j u_\nu \in \mathbb{Z}$ is strictly injective on $\mathbb{Z}$. Moreover, every $W_j$ realized by a pair $\{z_1, z_2\} \subseteq Z$ is a primitive direction vector ($W_j \ne (0, 0)$), whence $\|W_j\|_\infty \ge \max(1, |n_j|)$. Writing $a_j := \#\{\{z_1, z_2\} \subseteq Z : z_1 + z_2 = s_0 + j q\}$, the involutive pairing $z_1 + z_2 = s_0 + j q$ gives $0 \le a_j \le \lfloor m / 2 \rfloor$ for all $j \in \mathbb{Z}$, while $\sum_{j \in \mathbb{Z}} a_j \le \binom{m}{2} < \frac{1}{2} m^2$. By injectivity of $j \mapsto n_j \in \mathbb{Z}$, at most one index $j$ satisfies $n_j = 0$ (weight $\max(1, |n_j|)^{-1} = 1$) and for each integer $t \ge 1$ at most two indices $j$ satisfy $|n_j| = t$ (weight $t^{-1}$). Placing the maximum mass $m / 2$ on the $1 + 2 m$ largest available weights—whose total capacity $(1 + 2 m)\frac{m}{2} > \frac{1}{2} m^2$ exceeds $\sum_j a_j$—gives

$$
\sum_{j \in \mathbb{Z}} \frac{a_j}{\|W_j\|_\infty} \le \sum_{j \in \mathbb{Z}} \frac{a_j}{\max(1, |n_j|)} \le \frac{m}{2}\left(1 + 2 \sum_{t=1}^m \frac{1}{t}\right) \ll m \log(2m).
$$

Multiplying by $\tau(|\Delta|) \ll_{B, \varepsilon} k^{\varepsilon/2}$ yields $\mathcal{E}_{\mathrm{pairs}}(S_Q) \ll_{B, C_0, \varepsilon} m k^\varepsilon$.

For (2), if $x(t) = (t, f(t))$ with $f \in \mathbb{Z}[T]$ of degree $D \ge 2$ and leading coefficient $a_D \ne 0$, then $x(t_2) - x(t_1) = (t_2 - t_1)(1, P(t_1, t_2))$ has primitive vector $(1, P(t_1, t_2))$ where $P(t_1, t_2) = \frac{f(t_2) - f(t_1)}{t_2 - t_1} \in \mathbb{Z}[t_1, t_2]$ has height $\max(1, |P(t_1, t_2)|)$. If $D = 2$, $f(t) = a_2 t^2 + a_1 t + a_0$ gives $P(t_1, t_2) = a_2(t_1 + t_2) + a_1$, so the injective integer coordinate $n_s := a_2 s + a_1$ ($s = t_1 + t_2$) yields $\ll m \log(2m)$ by the exact rearrangement estimate above. If $D \ge 3$, fix $t_1 \in Z$ and consider the univariate polynomial $g(T) := P(t_1, T) = a_D T^{D - 1} + \cdots \in \mathbb{Z}[T]$ of degree $n := D - 1 \ge 2$ with $|a_D| \ge 1$. For any real $H \ge 1$, let $E_H := \{t \in \mathbb{Z} : |g(t)| \le H\}$ and $M := |E_H|$. If $M \ge n + 1$, set $q := \lfloor (M - 1) / n \rfloor \ge 1$, write $E_H$ in strictly increasing order $z_1 < \cdots < z_M$, and pick the $n + 1$ spaced integers $x_j := z_{1 + j q}$ ($0 \le j \le n$). Then $|x_j - x_i| \ge |j - i| q$ for all $i \ne j$, so $\prod_{i \ne j} |x_j - x_i| \ge q^n j!(n - j)!$; applying Lagrange's leading-coefficient identity $a_D = \sum_{j=0}^n g(x_j) \prod_{i \ne j} (x_j - x_i)^{-1}$ gives

$$
1 \le |a_D| \le \sum_{j=0}^n \frac{H}{q^n j!(n - j)!} = \frac{2^n H}{q^n n!},
$$

whence $q \le 2(H / n!)^{1/n}$ and $|E_H| = M \le n(q + 1) \le n + 2 n (H / n!)^{1/n}$ uniformly in $t_1$ and in all lower coefficients of $f$ (and trivially when $M \le n$). Partitioning $Z \setminus \{t_1\}$ into $|g(t_2)| \le 1$ and dyadic shells $2^k < |g(t_2)| \le 2^{k + 1}$ ($k \ge 0$) gives, since $n = D - 1 \ge 2$,

$$
\sum_{t_2 \in Z \setminus \{t_1\}} \frac{1}{\max(1, |g(t_2)|)} \le |E_1| + \sum_{k=0}^\infty 2^{-k} |E_{2^{k+1}}| \le 3 n + \sum_{k=0}^\infty 2^{-k}\!\left(n + 2 n \, 2^{\frac{k+1}{n}}\right) \ll_D 1.
$$

Summing over $t_1 \in Z$ gives $\mathcal{E}_{\mathrm{pairs}}(S) \ll_D m$. $\square$

### 2.3 Off-Curve Secant Energy from an External Point

**Lemma 2.3 (Off-Curve Secant Energy Bound).** *Let $Q \in \mathbb{Z}[X, Y]$ be an irreducible polynomial over $\mathbb{Q}$ of total degree $D \ge 2$. For every lattice point $x \in \mathbb{Z}^2$ with $Q(x) \ne 0$,*

$$
\sum_{y \in \mathbb{Z}^2 \cap \{Q = 0\}} \frac{1}{h(x, y)} \ll_D \tau(|Q(x)|).
$$

*Proof.* For any $y \in \mathbb{Z}^2 \cap \{Q = 0\}$, clearly $y \ne x$; write $y - x = g u$ with $g = g(x, y) \ge 1$ and primitive $u \in \mathbb{Z}^2$ of height $h(x, y) = \|u\|_\infty \ge 1$. Expanding $0 = Q(x + g u) \equiv Q(x) \pmod g$ shows that $g$ divides the nonzero integer $Q(x)$. Fix one positive divisor $g \mid |Q(x)|$. Every $y \in \mathbb{Z}^2 \cap \{Q = 0\}$ with $g(x, y) = g$ corresponds to an integer point $u = (y - x)/g \in \mathbb{Z}^2 \setminus \{0\}$ lying on the translated, rescaled curve

$$
Q_{x, g}(U, V) := Q(x_1 + g U,\, x_2 + g V) = 0,
$$

which remains irreducible over $\mathbb{Q}$ of total degree $D \ge 2$. If $Q_{x, g}$ is reducible over $\overline{\mathbb{Q}}$, Galois conjugation and Bézout's theorem limit its rational points globally to fewer than $D^2$ (see Lemma 3.3). Otherwise $Q_{x, g}$ is geometrically irreducible of degree $D \ge 2$: cutting its real locus inside each dyadic annulus $H \le \|(U, V)\|_\infty < 2 H$ ($H = 2^j$, $j \ge 0$) at singular points, coordinate extrema, and inflection points produces $O_D(1)$ smooth monotone strictly convex or concave arcs of $L^1$-length $\le 8 H$. By Jarník's convex-arc bound [12]—independently of the coefficient height of $Q_{x, g}$, consecutive lattice points along a strictly convex arc have pairwise distinct primitive chord vectors whose $L^1$-norms sum to $\le 8 H$, forcing at most $O(H^{2/3})$ lattice points per arc—each dyadic shell contains $O_D(H^{2/3})$ integer points. Summing over $H = 2^j \ge 1$ gives

$$
\sum_{\substack{u \in \mathbb{Z}^2 \setminus \{0\} \\ Q_{x, g}(u) = 0}} \frac{1}{\|u\|_\infty} \le D^2 + \sum_{j=0}^\infty 2^{-j} \cdot O_D\!\left((2^j)^{2/3}\right) \ll_D 1.
$$

Summing this uniform $O_D(1)$ estimate over all $\tau(|Q(x)|)$ positive divisors $g \mid |Q(x)|$ yields the claim. $\square$

---

## 3. Graded Hasse-Multiplicity Interpolation and Low-Degree Factor Elimination

We now assemble the algebraic core of our inverse sieve on a translated square $z_0 + [0, M)^2$.

### 3.1 Translated Degree-Graded Hasse-Multiplicity Siegel Lemma

For a bivariate polynomial $\widetilde{F}(U, V) = \sum_{|\beta| \le d} c_\beta U^{\beta_1} V^{\beta_2} \in \mathbb{Z}[U, V]$ and $\alpha = (\alpha_1, \alpha_2) \in \mathbb{Z}_{\ge 0}^2$, the Hasse derivative $\Delta^\alpha \widetilde{F} \in \mathbb{Z}[U, V]$ satisfies the exact Taylor identity

$$
\widetilde{F}(U + Z_1, V + Z_2) = \sum_{|\alpha| \le d} (\Delta^\alpha \widetilde{F})(U, V)\, Z_1^{\alpha_1} Z_2^{\alpha_2}, \qquad \Delta^\alpha \widetilde{F}(U, V) = \sum_{\beta \ge \alpha} c_\beta \binom{\beta_1}{\alpha_1} \binom{\beta_2}{\alpha_2} U^{\beta_1 - \alpha_1} V^{\beta_2 - \alpha_2}.
$$

**Lemma 3.1 (Degree-Graded Multiplicity Siegel Interpolation).** *Let $z_0 \in \mathbb{Z}^2$, $M \ge 2$, and let $A_1, \ldots, A_r \in z_0 + [0, M)^2$ be $r \ge 1$ lattice points with $\tilde{A}_i := A_i - z_0 \in [0, M)^2$.*
1. *(Zero-slack graded multiplicity box)* *Suppose integers $d \ge m \ge 1$ satisfy $s_d := \binom{d + 2}{2} > C_{\mathrm{con}} := r \binom{m + 1}{2}$ and the homogeneous grading inequality*

$$
\sum_{j=0}^d (j + 1)(d - j) \ge r \sum_{t=0}^{m-1} (t + 1)(d - t), \quad \text{equivalently} \quad d(d + 1)(d + 2) \ge r m(m + 1)(3d - 2m + 2).
$$

*Then there exists a constant $C_{d, m, r} \ge 1$ (depending only on $d, m, r$) and a nonzero polynomial $\widetilde{F} \in \mathbb{Z}[U, V]$ of total degree $\le d$ such that $(\Delta^\alpha \widetilde{F})(\tilde{A}_i) = 0$ for all $1 \le i \le r$ and $|\alpha| < m$, $|c_\beta| \le C_{d, m, r} M^{d - |\beta|}$ for all $|\beta| \le d$ (hence $H(\widetilde{F}) \le C_{d, m, r} M^d$), and*

$$
|\widetilde{F}(\tilde{x})| \le s_d C_{d, m, r} M^d \qquad \text{for all } \tilde{x} \in [0, M)^2.
$$

2. *(Ungraded $m = 1$ box)* *If $m = 1$ and $s_d = \binom{d + 2}{2} \ge 2 r$, there exists a nonzero $\widetilde{F} \in \mathbb{Z}[U, V]$ of total degree $\le d$ vanishing at $\tilde{A}_1, \ldots, \tilde{A}_r$ with $H(\widetilde{F}) \le (2 s_d + 1) M^d$ and $|\widetilde{F}(\tilde{x})| \le s_d (2 s_d + 1) M^{2d}$ for all $\tilde{x} \in [0, M)^2$.*
3. *(Order-$m$ LCM propagation)* *Under (1) (or (2) with $m = 1$), if $x \in z_0 + [0, M)^2$ satisfies $x - A_i = g_i u_i$ with $g_i \in \mathbb{Z}_{\ge 1}$ and $u_i \in \mathbb{Z}^2$ for all $1 \le i \le r$, then $\operatorname{lcm}(g_1, \ldots, g_r)^m$ divides $\widetilde{F}(x - z_0)$.*

*Proof.* For (1), choose $C := \left\lceil (2^{d + 1} s_d)^{C_{\mathrm{con}} / (s_d - C_{\mathrm{con}})} \right\rceil + 1$ and consider polynomials $\widetilde{P}(U, V) = \sum_{|\beta| \le d} c_\beta U^{\beta_1} V^{\beta_2}$ with integer coefficients $0 \le c_\beta \le B_{|\beta|} := \lfloor C M^{d - |\beta|} \rfloor$. The number of coefficient vectors is

$$
\prod_{j=0}^d (B_j + 1)^{j + 1} > C^{s_d} M^{\sum_{j=0}^d (j + 1)(d - j)}.
$$

At each $\tilde{A}_i \in [0, M)^2$ and $|\alpha| = t < m$, we have $0 \le (\Delta^\alpha \widetilde{P})(\tilde{A}_i) \le \sum_{j=t}^d \sum_{|\beta| = j} C M^{d - j} 2^j M^{j - t} \le 2^d s_d C M^{d - t}$. Since $2^d s_d C M^{d - t} + 1 \le 2^{d + 1} s_d C M^{d - t}$, the evaluation map $\widetilde{P} \mapsto ((\Delta^\alpha \widetilde{P})(\tilde{A}_i))_{1 \le i \le r,\, |\alpha| < m}$ takes at most

$$
(2^{d + 1} s_d C)^{C_{\mathrm{con}}} M^{r \sum_{t=0}^{m-1} (t + 1)(d - t)} \le (2^{d + 1} s_d C)^{C_{\mathrm{con}}} M^{\sum_{j=0}^d (j + 1)(d - j)}
$$

values. By definition of $C$, $C^{s_d - C_{\mathrm{con}}} > (2^{d + 1} s_d)^{C_{\mathrm{con}}}$, so two distinct coefficient vectors collide; their difference $\widetilde{F}$ is nonzero, vanishes to order $\ge m$ at every $\tilde{A}_i$, and satisfies $|c_\beta| \le C M^{d - |\beta|}$ and $|\widetilde{F}(\tilde{x})| \le \sum_{j=0}^d \sum_{|\beta| = j} C M^{d - j} M^j = s_d C M^d$ on $[0, M)^2$.

For (2), take $0 \le c_\beta \le \lfloor (2 s_d + 1) M^d \rfloor$. Since $s_d \ge 2 r$, the number of coefficient vectors exceeds $(2 s_d + 1)^{2r} M^{2 d r}$, while $0 \le \widetilde{P}(\tilde{A}_i) \le s_d (2 s_d + 1) M^{2d}$ gives at most $(s_d (2 s_d + 1) M^{2d} + 1)^r \le (2 s_d (2 s_d + 1))^r M^{2 d r} < (2 s_d + 1)^{2r} M^{2 d r}$ evaluation tuples.

For (3), substituting $(U, V) = \tilde{A}_i$ and $(Z_1, Z_2) = \tilde{x} - \tilde{A}_i = g_i u_i$ into the Hasse Taylor identity gives $\widetilde{F}(\tilde{x}) = \sum_{|\alpha| \ge m} (\Delta^\alpha \widetilde{F})(\tilde{A}_i)\, g_i^{|\alpha|} u_i^\alpha \equiv 0 \pmod{g_i^m}$ for each $1 \le i \le r$, whence $\operatorname{lcm}(g_1, \ldots, g_r)^m \mid \widetilde{F}(\tilde{x})$. $\square$

### 3.2 Factor Heights, Off-Anchor CRT Elimination, and Full-Galois Bombieri–Pila Bounds

**Lemma 3.2 (Kronecker–Mahler Factor Height Bound).** *Let $\widetilde{F} \in \mathbb{Z}[U, V] \setminus \{0\}$ have total degree $\le d$, and let $Q \in \mathbb{Z}[U, V]$ be any primitive divisor of $\widetilde{F}$ of total degree $d_Q \le d$. Then*

$$
H(Q) \le 2^{d(d + 2)} \sqrt{s_d}\, H(\widetilde{F}).
$$

*Proof.* Apply the Kronecker substitution $\tilde{q}(T) := Q(T, T^{d + 1})$ and $\tilde{f}(T) := \widetilde{F}(T, T^{d + 1})$ in $\mathbb{Z}[T]$. Because $(i, j) \mapsto i + (d + 1) j$ is injective on $\{(i, j) \in \mathbb{Z}_{\ge 0}^2 : i + j \le d\}$, the nonzero monomials of $Q$ and $\widetilde{F}$ map bijectively to distinct powers of $T$; in particular, $\tilde{q}$ is primitive in $\mathbb{Z}[T]$ with $H(\tilde{q}) = H(Q)$ and $\deg \tilde{q} \le d(d + 2)$, while $\|\tilde{f}\|_2 \le \sqrt{s_d}\, H(\widetilde{F})$. By Gauss's lemma, $\tilde{f} = \tilde{q} \tilde{h}$ in $\mathbb{Z}[T]$ with $\tilde{h} \ne 0$, so Mahler's multiplicative measure [13, Chapter 1] satisfies $M(\tilde{q}) \le M(\tilde{q}) M(\tilde{h}) = M(\tilde{f}) \le \|\tilde{f}\|_2$ by Landau's inequality, and Vieta's formulas give $H(\tilde{q}) \le 2^{\deg \tilde{q}} M(\tilde{q})$. $\square$

**Lemma 3.3 (Off-Anchor CRT Elimination and Higher-Degree Root Count).** *Fix integers $D_0 \ge 1$, $q \ge 1$, and $r \ge \binom{D_0 + 2}{2} + q - 1$. Let $\widetilde{F} \in \mathbb{Z}[U, V] \setminus \{0\}$ have total degree $\le d$ and $H(\widetilde{F}) \le C M^d$, and suppose $\tilde{A}_1, \ldots, \tilde{A}_r \in [0, M)^2$ have the property that no $\binom{D_0 + 2}{2}$ of them vanish on any nonzero polynomial in $\mathbb{Q}[U, V]$ of total degree $\le D_0$. Let $\mathcal{R} \subseteq z_0 + [0, M)^2$ be the set of lattice points $x$ with $\widetilde{F}(x - z_0) = 0$ such that $x - A_i = g_i(x) u_i(x)$ ($u_i(x) \in \mathbb{Z}^2$) satisfies*

$$
g_i(x) > G_0 \quad (1 \le i \le r) \qquad \text{and} \qquad \gcd\!\big(g_u(x),\, \operatorname{lcm}(g_1(x), \ldots, g_{u - 1}(x))\big) < T_0 \quad (2 \le u \le r),
$$

*where $G_0 > T_0 \ge 1$ obey $G_0 (G_0 / T_0)^{q - 1} \ge M$. Then for every $\varepsilon > 0$,*

$$
|\mathcal{R}| \ll_{d, D_0, q, C, \varepsilon} M^\varepsilon + M^{\frac{1}{D_0 + 1} + \varepsilon}.
$$

*Proof.* Factor $\widetilde{F} = c_0 \prod_{\nu=1}^K Q_\nu^{e_\nu}$ into primitive $\mathbb{Q}$-irreducible polynomials $Q_\nu \in \mathbb{Z}[U, V]$ ($K \le d$). Every $x \in \mathcal{R}$ satisfies $Q(\tilde{x}) = 0$ ($\tilde{x} = x - z_0 \in [0, M)^2$) for some factor $Q = Q_\nu$ of degree $d_Q := \deg Q$.

- **Case 1 ($1 \le d_Q \le D_0$):** By the full-rank hypothesis on $\tilde{A}_1, \ldots, \tilde{A}_r$, at most $\binom{D_0 + 2}{2} - 1$ anchors lie on $\{Q = 0\}$. Hence at least $r - \big(\binom{D_0 + 2}{2} - 1\big) \ge q$ anchors $\tilde{A}_{i_1}, \ldots, \tilde{A}_{i_q}$ ($1 \le i_1 < \cdots < i_q \le r$) satisfy $N_t := |Q(\tilde{A}_{i_t})| \ge 1$. By Lemma 3.2, $N_t \le s_d H(Q) M^{d_Q} \ll_{d, C} M^{2d}$. For any $x \in \mathcal{R}$ with $Q(\tilde{x}) = 0$, reducing $0 = Q(\tilde{A}_{i_t} + g_{i_t}(x) u_{i_t}(x)) \equiv Q(\tilde{A}_{i_t}) \pmod{g_{i_t}(x)}$ shows that $g_{i_t}(x)$ divides the fixed positive integer $N_t$ for each $1 \le t \le q$. There are $\prod_{t=1}^q \tau(N_t) \ll_{d, q, C, \varepsilon} M^\varepsilon$ divisor tuples $(d_1, \ldots, d_q)$ with $d_t \mid N_t$. Fix one tuple $(d_1, \ldots, d_q)$ realized by some $x \in \mathcal{R}$. Along the subsequence $i_1 < \cdots < i_q$,

$$
\gcd\big(d_t,\, \operatorname{lcm}(d_1, \ldots, d_{t - 1})\big) \le \gcd\big(g_{i_t}(x),\, \operatorname{lcm}(g_1(x), \ldots, g_{i_t - 1}(x))\big) < T_0 \qquad (2 \le t \le q),
$$

whence $L_{\mathrm{sub}} := \operatorname{lcm}(d_1, \ldots, d_q) > G_0 (G_0 / T_0)^{q - 1} \ge M$. Every $x' \in \mathcal{R}$ realizing the same divisor tuple satisfies $\tilde{x}' \equiv \tilde{A}_{i_t} \equiv \tilde{x} \pmod{d_t}$ in $\mathbb{Z}^2$ for $1 \le t \le q$, so both coordinates of $\tilde{x}' - \tilde{x} \in (-M, M)^2$ are divisible by $L_{\mathrm{sub}} \ge M$, forcing $\tilde{x}' = \tilde{x}$. Thus $\{Q = 0\}$ contains $O_{d, q, C, \varepsilon}(M^\varepsilon)$ points of $\mathcal{R}$.
- **Case 2 ($d_Q \ge D_0 + 1$):** If $Q$ is geometrically irreducible, Bombieri–Pila's uniform theorem [7, Theorem 5] bounds $|[0, M)^2 \cap \{Q = 0\}| \ll_{d_Q, \varepsilon} M^{\frac{1}{d_Q} + \varepsilon} \le M^{\frac{1}{D_0 + 1} + \varepsilon}$. If $Q$ is $\mathbb{Q}$-irreducible but reducible over $\overline{\mathbb{Q}}$, then $\operatorname{Gal}(\overline{\mathbb{Q}} / \mathbb{Q})$ acts transitively on the $m_Q \ge 2$ distinct geometric irreducible components $Z_1, \ldots, Z_{m_Q}$ of $\{Q = 0\}$ (each of degree $d_Q / m_Q$); every rational point $\tilde{x} \in \mathbb{Q}^2 \cap \{Q = 0\}$ is fixed by $\operatorname{Gal}(\overline{\mathbb{Q}} / \mathbb{Q})$ and therefore lies in $Z_1 \cap Z_2$, which has cardinality at most $(d_Q / m_Q)^2 < d_Q^2$ by Bézout's theorem. Summing over the $\le d$ irreducible factors $Q_\nu$ completes the proof. $\square$

---

## 4. Proofs of Theorem 1 and Theorem 2

### 4.1 Proof of Theorem 1(1): Row-Capped Ordinary Secant Energy

Fix any $\eta < \frac{1}{40}$, choose $\eta_1 := \frac{1}{2}\big(\eta + \frac{1}{40}\big) \in \big(\eta, \frac{1}{40}\big)$, and set $b := 2 \eta_1 \in \big(2\eta, \frac{1}{20}\big)$ together with the benchmark parameters $(r, D_0, q, m, d) = (15, 3, 6, 40, 256)$. Direct integer evaluation gives $s_d = \binom{258}{2} = 33153 > C_{\mathrm{con}} = 15 \binom{41}{2} = 12300$, $\binom{D_0 + 2}{2} + q - 1 = 10 + 5 = 15 = r$, and

$$
\sum_{j=0}^{256} (j + 1)(256 - j) - 15 \sum_{t=0}^{39} (t + 1)(256 - t) = 2{,}829{,}056 - 2{,}829{,}000 = 56 > 0
$$

(equivalently $d(d+1)(d+2) - r m(m+1)(3d - 2m + 2) = 336 > 0$), satisfying the $\theta = 0$ grading condition of Lemma 3.1(1).

Let $S \subseteq G_N$ have at most two points per horizontal row, so $|S| \le 2 N$. At any $x \in S$, each primitive direction occurs for at most one ordinary neighbor $y$ with $\{x, y\} \in \mathcal{O}(S)$. Within distance $\|y - x\|_\infty < R_0 := N^{1 - b}$, $x + (-R_0, R_0)^2$ meets at most $2 R_0 + 1$ rows and hence contains $\le 4 R_0 + 2$ points of $S$; ordering these ordinary neighbors by height gives $\sum_{y:\, \|y - x\|_\infty < R_0} h(x, y)^{-1} \ll R_0^{1/2} = N^{\frac{1}{2} - \frac{b}{2}}$, summing over $x \in S$ to $O(N^{\frac{3}{2} - \eta_1})$.

Partition the remaining ordinary pairs $R_0 \le \|x - y\|_\infty < N$ into $O(\log N)$ dyadic shells $R \le \|x - y\|_\infty < 2 R$ ($N^{1 - b} \le R < N$). For a fixed shell $R$, cover $\mathbb{R}^2$ by four shifted grids of half-open squares $W \in \mathcal{W}_R$ of side $M := \lceil 4 R \rceil$, shifted by $\{0, \lfloor M/2 \rfloor\}^2$, so every pair with $\|x - y\|_\infty < 2 R$ lies together in at least one square $W \in \mathcal{W}_R$, and $\sum_{W \in \mathcal{W}_R} |S_W| = 4 |S| \le 8 N$ where $S_W := S \cap W$. Because $S_W$ remains row-two-capped across $M$ rows, $|S_W| \le 2 M$.

- **Light squares:** If $|S_W| < N^{1 - b}$, the direction-matching estimate gives $E_{\mathrm{ord}}(S_W) \ll |S_W|^{3/2} < N^{\frac{1}{2} - \frac{b}{2}} |S_W|$, summing over light squares to $O(N^{\frac{3}{2} - \eta_1})$.
- **High-height pairs in heavy squares:** In any heavy square ($|S_W| \ge N^{1 - b}$, whence $2 M \ge |S_W| \ge N^{1 - b}$ so $M \to \infty$ uniformly as $N \to \infty$), pairs with $h(x, y) > H_M := M^{\frac{1}{2} + \frac{b}{2}}$ contribute at most $\binom{|S_W|}{2} / H_M \le |S_W| M / M^{\frac{1}{2} + \frac{b}{2}} = |S_W| M^{\frac{1}{2} - \frac{b}{2}} \ll |S_W| N^{\frac{1}{2} - \frac{b}{2}}$, summing over $W \in \mathcal{W}_R$ to $O(N^{\frac{3}{2} - \eta_1})$.

Let $\Gamma_*(W)$ be the remaining ordinary pairs $\{x, y\} \subseteq S_W$ with $R \le \|x - y\|_\infty < 2 R$ and $h(x, y) \le H_M$. Every edge of $\Gamma_*(W)$ satisfies $g(x, y) = \|x - y\|_\infty / h(x, y) \ge R / H_M > G_0 := \frac{1}{5} M^{\frac{1}{2} - \frac{b}{2}}$. Suppose for contradiction that $|E(\Gamma_*(W))| \ge |S_W| M^{1 - b}$ on arbitrarily large boards. Setting $V_{\mathrm{ret}} := \{x \in S_W : d_*(x) \ge M^{1 - b}\}$ gives $\sum_{x \in V_{\mathrm{ret}}} d_*(x) \ge |S_W| M^{1 - b}$. With $a := \frac{1 - b}{2}$, $\tau := b$, and $\mathrm{gap}_0 := a - \tau = \frac{1 - 3 b}{2}$, consider on $b \in \big(0, \frac{1}{20}\big]$ the three unshifted cutoff margins $\mathrm{gap}_0 = \frac{1 - 3 b}{2}$, $\mathrm{crt}_0 := a + 5 \mathrm{gap}_0 - 1 = 2 - 8 b$, and $\mathrm{prop}_0 := a + 14 \mathrm{gap}_0 - \frac{256}{40} = \frac{11}{10} - \frac{43}{2} b$. Because $\mathrm{crt}_0 - \mathrm{gap}_0 = \frac{3 - 13 b}{2} \ge \frac{47}{40} > 0$ and $\mathrm{prop}_0 - \mathrm{gap}_0 = \frac{3}{5} - 20 b$ changes sign at $b = \frac{3}{100}$, their minimum on $\big(0, \frac{1}{20}\big]$ is

$$
\mu_0(b) := \min(\mathrm{gap}_0, \mathrm{crt}_0, \mathrm{prop}_0) = \begin{cases} \frac{1 - 3 b}{2}, & 0 < b < \frac{3}{100}, \\[2pt] \frac{11}{10} - \frac{43}{2} b, & \frac{3}{100} \le b \le \frac{1}{20}, \end{cases}
$$

satisfying $\frac{1}{40} \le \mu_0(b) < \frac{1}{2}$ (with $\mu_0(b) > \frac{1}{40}$ for $b < \frac{1}{20}$) and $\mu_0(b) \le \mathrm{prop}_0$ everywhere. Defining, identically to `verify_all.py`,

$$
\sigma := \frac{\mu_0(b)}{2 r} = \frac{\mu_0(b)}{30} \ge \frac{1}{1200} > 0
$$

and $T_0 := M^{b + \sigma}$ (note $\mathrm{gap}_0 - \sigma \ge \frac{29}{30}\mathrm{gap}_0 > 0$), fix $x \in V_{\mathrm{ret}}$ ($M_x := d_*(x) \ge M^{1 - b}$) and sample $(A_1, \ldots, A_r) \in N_{\Gamma_*(W)}(x)^r$ uniformly:

1. *LCM growth:* For each divisor $t \ge T_0$ of $L_{u - 1} \le M^{u - 1}$ ($M^{o(1)}$ divisors), $(x + t \mathbb{Z}^2) \cap W$ meets at most $1 + M / t \le 2 M / t$ horizontal rows, each holding $\le 2$ points of $S_W$. Hence $|(x + t \mathbb{Z}^2) \cap (S_W \setminus \{x\})| \le 4 M / T_0 = 4 M^{1 - b - \sigma} = o(M_x)$, so $\gcd(g(x, A_u), L_{u - 1}) < T_0$ holds for all $2 \le u \le r$ with probability $1 - o(1)$.
2. *Full-rank degree-$3$ anchor exclusion:* Fix any $10$-element subset of $\{1, \ldots, 15\}$. On any nonzero polynomial $P \in \mathbb{Q}[U, V]$ of degree $\le 3$: (i) a line component through $x$ holds $\le 1$ ordinary neighbor; (ii) a line component $L = \{y_0 + t w\}$ not through $x$ has $\Delta_L = \det(w, y_0 - x) \ne 0$ ($|\Delta_L| \le 2 M^2$), and every $y \in L \cap N_{\Gamma_*(W)}(x)$ has $g(x, y) \mid |\Delta_L|$ and $g(x, y) > G_0$, pinning $t \bmod g(x, y)$ uniquely and yielding $\ll \tau(|\Delta_L|) (M / G_0) \ll M^{\frac{1}{2} + \frac{b}{2} + o(1)} = o(M_x)$ neighbors; and (iii) any nonlinear $\mathbb{Q}$-irreducible component has $\ll_\varepsilon M^{\frac{1}{2} + \varepsilon} = o(M_x)$ points in $W$. By subspace filtration and a union bound over $\binom{15}{10}$ subsets, no $10$ anchors vanish on a nonzero degree-$\le 3$ polynomial with probability $1 - o(1)$.

Thus at least $\frac{1}{2} d_*(x)^r$ tuples in $N_{\Gamma_*(W)}(x)^r \subseteq S_W^r$ are good for $x$. Applying Hölder's inequality over $x \in V_{\mathrm{ret}}$ ($|V_{\mathrm{ret}}| \le |S_W| \le 2 M$) and averaging over $S_W^r$ produces an anchor tuple $(A_1, \ldots, A_r)$ good for at least

$$
\frac{1}{2 |S_W|^r} \sum_{x \in V_{\mathrm{ret}}} d_*(x)^r \ge \frac{\big(|S_W| M^{1 - b}\big)^r}{2 |S_W|^{2 r - 1}} = \frac{1}{2} \left(\frac{M}{|S_W|}\right)^{r - 1} M^{1 - r b} \ge 2^{-r} M^{1 - 15 b}
$$

common roots $x \in V_{\mathrm{ret}}$. Let $\widetilde{F}$ be the degree-$256$, multiplicity-$40$ interpolant of Lemma 3.1(1). At every good root $x$, $g_i(x) > G_0$ and $\gcd(g_u(x), L_{u - 1}(x)) < T_0$ give $L_{15}(x) > G_0 (G_0 / T_0)^{14} \gg M^{\frac{1}{2} - \frac{b}{2} + 14(\frac{1}{2} - \frac{3}{2} b - \sigma)}$. Because $\sigma = \mu_0(b) / 30$, $\mu_0(b) \le \mathrm{prop}_0$, and $b < \frac{1}{20}$, we have for every $\eta < \frac{1}{40}$:

$$
\frac{1}{2} - \frac{b}{2} + 14\left(\frac{1}{2} - \frac{3}{2} b - \sigma\right) - \frac{256}{40} = \mathrm{prop}_0 - \frac{7}{15} \mu_0(b) \ge \frac{8}{15} \mathrm{prop}_0 > \frac{8}{15} \cdot \frac{1}{40} = \frac{1}{75} > 0
$$

(with equality $\mathrm{prop}_0 - 14 \sigma = \frac{8}{15} \mathrm{prop}_0$ on $\big[\frac{3}{100}, \frac{1}{20}\big]$, e.g. $\frac{31}{1250} = 0.0248$ at $\eta = \frac{3}{125}$, $b = \frac{49}{1000}$), so $L_{15}(x)^{40} > s_{256} C_{256, 40, 15} M^{256} \ge |\widetilde{F}(x - z_0)|$ for large $M$, forcing $\widetilde{F}(x - z_0) = 0$. Similarly, $G_0 (G_0 / T_0)^{q - 1} \gg M^{\mathrm{crt}_0 - 5 \sigma} > M^{\frac{8}{5} - \frac{1}{6}\cdot\frac{1}{2}} = M^{\frac{91}{60}} > M$. Lemma 3.3 with $D_0 = 3$ then bounds the number of good roots by $O_\varepsilon(M^{\frac{1}{4} + \varepsilon})$, contradicting $2^{-15} M^{1 - 15 b}$ because $1 - 15 b = 1 - 30 \eta_1 > \frac{1}{4}$.

Therefore $|E(\Gamma_*(W))| < |S_W| M^{1 - b}$ for all $N \ge N_0(\eta_1)$. Direction-matching inside each heavy square gives $E_{\Gamma_*(W)} \ll \sqrt{|S_W| |E(\Gamma_*(W))|} < |S_W| M^{\frac{1}{2} - \frac{b}{2}} \ll |S_W| N^{\frac{1}{2} - \frac{b}{2}}$, summing over $W \in \mathcal{W}_R$ and over the $O(\log N)$ shells $R$ to $O_{\eta_1}(N^{\frac{3}{2} - \eta_1} \log N) = O_\eta(N^{\frac{3}{2} - \eta})$. $\square$

### 4.2 Unified Proof of Theorem 1(2,3) and Theorem 2

Now let $B \in [1, 3)$, $\lambda \in [0, 1/2)$, $C_0 > 0$, $C_1 \ge 1$, and let $S \subseteq G_N$ have $|S| = k \ge 2$, $N \le C_0 k^B$, and $h(v_*) L_{v_*}(S) \le C_1 k^\lambda$ for a primitive direction $v_*$ (for any no-three-in-line cap, $v_* = (1, 0)$ gives $h(v_*) L_{v_*}(S) \le 2$, satisfying this hypothesis at $\lambda = 0$ with $C_1 = 2$). Choose at most one representative pair $\{x, y\} \subseteq S$ on each line $L$ with $|L \cap S| \ge 2$; let $\Gamma_{\mathrm{rep}}$ be this representative graph, so $\mathcal{E}(S) = \sum_{\{x, y\} \in \Gamma_{\mathrm{rep}}} h(x, y)^{-1}$.

We treat simultaneously the four graded $\theta = 0$ benchmark certificates of Table 1 (`domination_cap_3_2`, `paper108_thm2_5_3`, `conic_threshold_2_0`, `post_conic_5_2`, where for any $\eta \in (0, \eta_0)$ we put $\eta_1 := \frac{1}{2}(\eta + \eta_0) \in (0, \eta_0)$, $b := 2 \eta_1 \in (0, 2 \eta_0)$, and $\mathrm{height} := \frac{d}{m} > 1$) and the closed-form general certificate for arbitrary $(B, \lambda) \in [1, 3) \times [0, 1/2)$: setting $\delta_0 := \frac{1}{2}\big(\frac{1}{2} - \lambda\big) > 0$ and $t := \lceil 24 / \delta_0 \rceil$, put

$$
r := t^2, \quad D_0 := 2, \quad q := 1 + \lceil 1 / \delta_0 \rceil, \quad m := 1, \quad d := 2 t, \quad b := \min\!\left(\frac{\delta_0}{8},\; \frac{3 - B}{6(r + 2)}\right), \quad \eta(B, \lambda) := \frac{b}{4},
$$

with $\mathrm{height} := 2 d$ via Lemma 3.1(2) (since $s_d = (2t + 1)(t + 1) > 2 t^2 = 2 r$). In all cases $0 < b \le \frac{1}{32} < \frac{1}{6}$. With $\rho := \frac{B}{1 - b}$, $h := \frac{1 + b}{2(1 - b)}$, $a := \rho - h$, $\tau := \rho - 1 + b + \frac{\lambda}{1 - b}$, and $\mathrm{gap}_0 := a - \tau = 1 - b - h - \frac{\lambda}{1 - b}$, setting $\sigma := \frac{1}{2 r} \min\!\big(\mathrm{gap}_0,\, a + (q - 1)\mathrm{gap}_0 - \rho,\, a + (r - 1)\mathrm{gap}_0 - \rho \cdot \mathrm{height}\big) > 0$ and $\mathrm{gap} := \mathrm{gap}_0 - \sigma > 0$, we verify four strict margin inequalities:
- **(M1)** $1 - \lambda - b > 0$ and $1 - b - \frac{\lambda}{1 - b} - \sigma > 0$;
- **(M2)** $-h + (q - 1) \mathrm{gap} = a + (q - 1) \mathrm{gap} - \rho > 0$ and $a + (r - 1) \mathrm{gap} - \rho \cdot \mathrm{height} > 0$;
- **(M3)** $1 - b - h > 0$ and $1 - b - \frac{\rho}{\kappa} > 0$, where $\kappa = 3$ if conic peeling is active ($B \ge 2$ or general certificate) and $\kappa = 2$ otherwise;
- **(M4)** $1 - r b - \frac{\rho}{D_0 + 1} > 0$.

Notice that as $b \in (0, 1)$ increases, $\rho = \frac{B}{1 - b}$ and $h = \frac{1 + b}{2(1 - b)}$ strictly increase while $\mathrm{gap}_0$ strictly decreases, and since $\mathrm{height} \ge 1$ every unshifted margin—including $a + (r - 1)\mathrm{gap}_0 - \rho \cdot \mathrm{height} = (r - 1)\mathrm{gap}_0 - h - \rho(\mathrm{height} - 1)$—is a strictly decreasing function of $b$; moreover, since $1 \le q \le r$ and $1 - b - \frac{\lambda}{1 - b} = \mathrm{gap}_0 + h > \mathrm{gap}_0$, choosing $\sigma$ as the minimum of the three positive unshifted cutoff margins divided by $2 r$ subtracts at most half of each cutoff margin and leaves $\mathrm{gap} > 0$, (M1), and (M2) strictly positive whenever the unshifted margins are positive. For the four cardinality rows of Table 1, `verify_all.py` certifies strict positivity of all unshifted and shifted margins at the right endpoint $b = 2 \eta_0$ in exact rational arithmetic, which by monotonicity establishes (M1)–(M4) for every real $b \in (0, 2 \eta_0]$. For the closed-form general certificate, since $b \le \frac{\delta_0}{8} \le \frac{1}{32}$ and $\frac{1}{2} - \lambda = 2 \delta_0$, we have $h = \frac{1}{2} + \frac{b}{1 - b} < \frac{1}{2} + \frac{32}{31} b < 1$, $\frac{\lambda}{1 - b} < \lambda + b$, and

$$
\mathrm{gap}_0 = 1 - b - \left(\frac{1}{2} + \frac{b}{1 - b}\right) - \frac{\lambda}{1 - b} > \left(\frac{1}{2} - \lambda\right) - 4 b \ge 2 \delta_0 - \frac{\delta_0}{2} = \frac{3}{2} \delta_0 > \delta_0.
$$

Hence $(q - 1) \mathrm{gap}_0 > \frac{1}{\delta_0} \cdot \delta_0 = 1 > h$, giving $a + (q - 1)\mathrm{gap}_0 - \rho = (q - 1)\mathrm{gap}_0 - h > 0$. Because $B < 3$ and $1 - b \ge \frac{31}{32}$, $\rho = \frac{B}{1 - b} < \frac{96}{31} < 4$, while $(r - 1) \mathrm{gap}_0 > (t^2 - 1) \delta_0$. Since $t \ge \frac{24}{\delta_0} \ge 96$, $(t^2 - 1) \delta_0 > \frac{23}{24} t^2 \delta_0 \ge 23 t > 8 t + 1 > \rho (2 d) + h$, giving $a + (r - 1)\mathrm{gap}_0 - \rho (2d) > 0$. Finally, $b \le \frac{3 - B}{6(r + 2)}$ implies $(1 - r b)(1 - b) - \frac{B}{3} = \frac{3 - B}{3} - (r + 1) b + r b^2 > \frac{3 - B}{6} > 0$, proving (M4) ($D_0 = 2$) and $1 - b - \frac{\rho}{3} > 0$.

Now execute the four-step decomposition:

1. **Sequential conic peeling (when $\kappa = 3$):** Put $\alpha_{\mathrm{peel}} := \frac{1}{2} + \frac{3}{4} b$. Starting with $S^{(0)} := S$, while there exists an irreducible quadratic polynomial $Q_j \in \mathbb{Z}[X, Y]$ ($\deg Q_j = 2$) with $|S^{(j - 1)} \cap \{Q_j = 0\}| \ge k^{\alpha_{\mathrm{peel}}}$, set $S_j := S^{(j - 1)} \cap \{Q_j = 0\}$ and $S^{(j)} := S^{(j - 1)} \setminus S_j$. This terminates in $T \le k^{1 - \alpha_{\mathrm{peel}}}$ steps at $S' := S^{(T)} \subseteq S$ satisfying $|S' \cap \{Q = 0\}| < k^{\alpha_{\mathrm{peel}}}$ for every irreducible conic $Q = 0$. At step $j$, $|S_j| \ge k^{\alpha_{\mathrm{peel}}} \ge 6$ (for large $k$), so Lemma 2.1 gives $H(Q_j) \le k^{O_{C_0}(B)}$. Every representative edge of $\Gamma_{\mathrm{rep}}$ removed at step $j$ is either internal to $S_j$—contributing $\ll_{B, C_0, \varepsilon} |S_j| k^\varepsilon$ by Proposition 2.2(1)—or joins $S_j$ to a vertex $x \in S^{(j)}$, which satisfies $1 \le |Q_j(x)| \le 6 H(Q_j) N^2 \le k^{O_{C_0}(B)}$ since all zeroes of $Q_j$ in $S^{(j - 1)}$ were removed. By Lemma 2.3, each $x \in S^{(j)}$ contributes $\ll \tau(|Q_j(x)|) \ll_{B, C_0, \varepsilon} k^\varepsilon$ across $S_j$, hence $\ll_{B, C_0, \varepsilon} k^{1 + \varepsilon}$ per peeled conic. Summing over $T \le k^{1 - \alpha_{\mathrm{peel}}}$ steps (with $\varepsilon = b / 8$) bounds all peeled edges by $O_{B, C_0}(k^{\frac{3}{2} - \frac{b}{2}})$. (When $\kappa = 2$, set $S' := S$.)
2. **Short-distance and high-height disposal on $S'$:** Representative pairs in $S'$ with $h(x, y) > H_k := k^{\frac{1}{2} + \frac{b}{2}}$ contribute at most $\binom{|S'|}{2} / H_k \le k^{\frac{3}{2} - \frac{b}{2}}$. For pairs with $\|x - y\|_\infty < R_{\min} := k^{1 - \lambda - b}$, the square $x + (-R_{\min}, R_{\min})^2$ meets at most $2 h(v_*) (2 R_{\min} + 1)$ lines of primitive direction $v_*$, each containing $\le L_{v_*}(S)$ points of $S'$, so $|S' \cap (x + (-R_{\min}, R_{\min})^2)| \le 6 h(v_*) L_{v_*}(S) R_{\min} \le 6 C_1 k^{1 - b}$. Since $\Gamma_{\mathrm{rep}}$ has distinct directions at $x$, these short edges contribute $\ll \sqrt{C_1}\, k^{\frac{3}{2} - \frac{b}{2}}$.
3. **Four-shift dyadic $4R$-square decomposition:** Partition the remaining representative edges of $S'$ ($R_{\min} \le \|x - y\|_\infty < N$, $h(x, y) \le H_k$) into $O_{B, C_0}(\log k)$ dyadic shells $R \le \|x - y\|_\infty < 2 R$, and cover each shell by four shifted grids $\mathcal{W}_R$ of squares $W = z_0 + [0, M)^2$ of side $M := 4 \lceil R \rceil$ ($\sum_{W \in \mathcal{W}_R} |S'_W| \le 4 |S'| \le 4 k$, where $S'_W := S' \cap W$). Light squares with $s := |S'_W| < k^{1 - b}$ satisfy $E_{\Gamma_{\mathrm{rep}}}(S'_W) \ll s^{3/2} < k^{\frac{1}{2} - \frac{b}{2}} s$, summing to $O(k^{\frac{3}{2} - \frac{b}{2}})$ per shell.
4. **Scale-covariant residue cutoff and graded interpolation in heavy squares:** Let $W \in \mathcal{W}_R$ be a heavy square, so $k^{1 - b} \le s := |S'_W| \le k$ and $M = 4 \lceil R \rceil \le 8 C_0 k^B \le 8 C_0 s^\rho$. Every remaining representative edge $\{x, y\} \subseteq S'_W$ in shell $R$ has $h(x, y) \le k^{\frac{1}{2} + \frac{b}{2}} \le s^h$, hence $g(x, y) \ge R / s^h > G_0(R) := \frac{1}{8} M s^{-h}$. Define the dynamic residue cutoff

$$
T_0(R) := M \cdot s^{-1 + b + \frac{\lambda}{1 - b} + \sigma}.
$$

Since the exponent $-1 + b + \frac{\lambda}{1 - b} + \sigma$ is strictly negative by (M1), $s^{-1 + b + \frac{\lambda}{1 - b} + \sigma}$ attains its minimum over $s \in [k^{1 - b}, k]$ at $s = k$, giving uniformly across all heavy squares and all shells $R \ge k^{1 - \lambda - b}$:

$$
T_0(R) \ge 4 k^{1 - \lambda - b} \cdot k^{-1 + b + \frac{\lambda}{1 - b} + \sigma} = 4 k^{\frac{\lambda b}{1 - b} + \sigma} \ge 4 k^\sigma \longrightarrow +\infty.
$$

Suppose for contradiction that the shell graph $\Gamma_*(W)$ on $S'_W$ has $|E(\Gamma_*(W))| \ge \frac{1}{2} s^{2 - b}$. Retaining $V_{\mathrm{ret}} := \{x \in S'_W : d_*(x) \ge \frac{1}{2} s^{1 - b}\}$ leaves $\sum_{x \in V_{\mathrm{ret}}} d_*(x) \ge \frac{1}{2} s^{2 - b}$. At each $x \in V_{\mathrm{ret}}$ ($M_x = d_*(x) \ge \frac{1}{2} s^{1 - b}$):
- For every divisor $t \ge T_0(R)$ of $L_{u - 1}$ ($t \le M$, else $(x + t \mathbb{Z}^2) \cap W = \{x\}$), the subgrid $((x + t \mathbb{Z}^2) \cap W - x) / t \subseteq (-M / t, M / t)^2$ meets $\le 2 h(v_*) (2 M / t + 1) \le 6 h(v_*) M / t$ lines of direction $v_*$, so $|(x + t \mathbb{Z}^2) \cap (S'_W \setminus \{x\})| \le 6 h(v_*) L_{v_*}(S) M / T_0(R) \le 6 C_1 s^{\frac{\lambda}{1 - b}} \cdot s^{1 - b - \frac{\lambda}{1 - b} - \sigma} = 6 C_1 s^{1 - b - \sigma} = o(M_x)$ as $k \to \infty$ (since $s \ge k^{1 - b} \to \infty$ and $T_0(R) > 1$ excludes $t = 1$).
- On any nonzero polynomial $P \in \mathbb{Q}[U, V]$ of degree $\le D_0$: (i) a line component through $x$ holds $\le 1$ representative neighbor; (ii) a line component $L$ off $x$ holds $\ll M^{o(1)} (M / G_0(R)) \ll s^{h + o(1)} = o(M_x)$ neighbors in $N_{\Gamma_*(W)}(x)$ by (M3); (iii) when $\kappa = 3$, any irreducible conic component holds $< k^{\alpha_{\mathrm{peel}}} = k^{\frac{1}{2} + \frac{3}{4} b} \le s^{\frac{1/2 + 3b/4}{1 - b}} = o(M_x)$ points of $S'_W$ (since $(1 - b)^2 - (\frac{1}{2} + \frac{3}{4}b) > \frac{1}{2} - \frac{11}{4}b > 0$ for $b \le \frac{1}{32}$); and (iv) any irreducible component of degree $\ge \kappa$ holds $\ll_\varepsilon M^{\frac{1}{\kappa} + \varepsilon} \ll s^{\frac{\rho}{\kappa} + \rho \varepsilon} = o(M_x)$ points by (M3).

Thus $\ge \frac{1}{2} d_*(x)^r$ tuples in $N_{\Gamma_*(W)}(x)^r$ are good for $x$, and Hölder's inequality over $x \in V_{\mathrm{ret}}$ ($|V_{\mathrm{ret}}| \le s$) yields an anchor tuple $(A_1, \ldots, A_r) \in (S'_W)^r$ good for $\ge 2^{-r - 1} s^{1 - r b}$ roots. Note that $G_0(R) / T_0(R) = \frac{1}{8} s^{\mathrm{gap}}$, completely independent of $M$. Hence $G_0(R) (G_0(R) / T_0(R))^{q - 1} \gg M s^{-h + (q - 1)\mathrm{gap}} > M$ by (M2), and writing $M = s^{\rho_W}$ with $\rho_W \le \rho + o(1)$ and $\mathrm{height} \ge 1$, the exponent of $L_r(x) / M^{\mathrm{height}}$ is $(\rho_W - h) + (r - 1)\mathrm{gap} - \rho_W \cdot \mathrm{height} = (r - 1)\mathrm{gap} - h - \rho_W(\mathrm{height} - 1) \ge a + (r - 1)\mathrm{gap} - \rho \cdot \mathrm{height} - o(1) > 0$ by (M2). Consequently Lemma 3.1 forces $\widetilde{F}(x - z_0) = 0$ at every good root, and Lemma 3.3 bounds the good roots by $O_\varepsilon(M^{\frac{1}{D_0 + 1} + \varepsilon}) \ll s^{\frac{\rho}{D_0 + 1} + \rho \varepsilon}$, contradicting $2^{-r - 1} s^{1 - r b}$ by (M4).

Therefore $|E(\Gamma_*(W))| < \frac{1}{2} s^{2 - b}$ for all $k \ge k_0(B, \lambda, C_0, C_1, b)$, so $E_{\Gamma_*(W)} \ll \sqrt{s |E(\Gamma_*(W))|} \ll s^{\frac{3}{2} - \frac{b}{2}} \le k^{\frac{1}{2} - \frac{b}{2}} s$, summing over heavy squares and all $O_{B, C_0}(\log k)$ shells to $O_{B, \lambda, C_0, C_1, b}(k^{\frac{3}{2} - \frac{b}{2}} \log k)$. For Table 1 ($b = 2 \eta_1 > 2 \eta$), $k^{\frac{3}{2} - \eta_1} \log k \ll_\eta k^{\frac{3}{2} - \eta}$; for the general certificate ($\eta(B, \lambda) = b / 4$), $k^{\frac{3}{2} - 2 \eta(B, \lambda)} \log k \ll k^{\frac{3}{2} - \eta(B, \lambda)}$.

**Deduction of Theorem 1(3) and Theorem 2(2):**
- *Lower bound on $I_N$:* An inclusion-maximal cap $S \subseteq G_N$ ($N \ge 2$, $k = |S| \ge 2$) covers $G_N$ by its secant lines, so $N^2 \le 2 N \mathcal{E}(S)$, i.e. $N \le 2 \mathcal{E}(S)$. First $\mathcal{E}(S) \ll k^{3/2}$ gives $N \le C_0 k^{3/2}$. Applying Theorem 1(2) for any $\eta_1 < \frac{1}{80}$ yields $N \ll_{\eta_1} k^{\frac{3}{2} - \eta_1}$, hence $k \gg_{\eta_1} N^{\frac{1}{3/2 - \eta_1}}$. Since $\frac{1}{3/2 - 1/80} - \frac{2}{3} = \frac{80}{119} - \frac{2}{3} = \frac{2}{357}$, $I_N = \Omega_c(N^{\frac{2}{3} + c})$ and $I_N / D_N = \Omega_c(N^c)$ hold for every $c < \frac{2}{357}$ (using $D_N = O((N \log N)^{2/3})$ from [9, Theorem 1]).
- *Universal cap planting:* Given any cap $T \subseteq G_N$ ($k = |T| \le N^{\frac{2}{3} + c}$, $c < \frac{2}{357}$) and disjoint $F_0 \subseteq G_N \setminus T$ ($|F_0| = o(N^2)$), the shifted random classical conic deletion estimate of [9, Section 5] produces a cap $U \supseteq T$ in $G_N \setminus F_0$ of size $\ge 3(p - 1) + k - O(\sqrt{k p} + k \log(2p) + \mathcal{E}(T) + (k + |F_0|)/p)$ where $p \le N / 2$ is prime ($2p / N \to 1$). Across all scales of $k$: if $k < N^{3/5}$, $\mathcal{E}(T) \ll k^{3/2} < N^{9/10} = o(N)$; if $N^{3/5} \le k < N^{2/3}$, then $N \le k^{5/3}$, so the $B = 5/3$ certificate gives $\mathcal{E}(T) \ll k^{\frac{3}{2} - \frac{1}{100}} < N^{1 - \frac{1}{150}} = o(N)$; and if $N^{2/3} \le k \le N^{\frac{2}{3} + c}$, then $N \le k^{3/2}$ and picking $\eta_1 < \frac{1}{80}$ with $\frac{2}{3} + c < \frac{1}{3/2 - \eta_1}$ gives $\mathcal{E}(T) \ll_{\eta_1} k^{\frac{3}{2} - \eta_1} = o(N)$.
- *Sharpness at $\lambda = 1/2$:* If $S_N \subseteq G_N$ dominates $G_N$ with $k = |S_N| = N^{2/3 + o(1)}$, then $N \le k^{5/3}$ eventually; if $\min_v h(v) L_v(S_N) \le k^\lambda$ held along a subsequence for some $\lambda < 1/2$, Theorem 2(1) at $(5/3, \lambda)$ would give $N \le 2 \mathcal{E}(S_N) \ll_\lambda k^{\frac{3}{2} - \eta(5/3, \lambda)} = o(N)$, impossible. Conversely, the dominating cross $A_N \subseteq G_N$ of [9, Section 2] has $k = |A_N| = \Theta((N \log N)^{2/3})$, $\mathcal{E}(A_N) \ge \frac{1}{2} N = k^{3/2 - o(1)}$, and contains the central square $[-L, L]^2$ of half-width $L = \lceil (N \ell)^{1/3} \rceil \asymp (N \log N)^{1/3} = k^{1/2 - o(1)}$, so every primitive $v$ satisfies $h(v) L_v(A_N) \ge h(v) (1 + 2\lfloor L / h(v) \rfloor) > L = k^{1/2 - o(1)}$ if $h(v) \le L$ and $h(v) L_v(A_N) \ge h(v) > L$ if $h(v) > L$. $\square$

| Certificate | Board regime $B$ | $\lambda$ | Conic peeling | $(r, D_0, q, m, d)$ | Grading slack | Certified saving $\eta < \eta_0$ |
| --- | --- | --- | --- | --- | --- | --- |
| `board_row_capped` | $1$ (ordinary, row-capped) | $0$ | No | $(15, 3, 6, 40, 256)$ | $+56$ | $\eta_0 = 1/40 = 0.025$ |
| `domination_cap_3_2` | $3/2$ (caps, $I_N$) | $0$ | No | $(31, 6, 3, 35, 329)$ | $+6{,}755$ | $\eta_0 = 1/80 = 0.0125$ ($c_0 = 2/357$) |
| `paper108_thm2_5_3` | $5/3$ | $1/100$ | No | $(38, 7, 3, 45, 469)$ | $+11{,}665$ | $\eta_0 = 1/97 \approx 0.01031$ |
| `conic_threshold_2_0` | $2$ (conic threshold) | $0$ | Yes | $(50, 8, 6, 35, 422)$ | $+35{,}424$ | $\eta_0 = 1/130 \approx 0.00769$ |
| `post_conic_5_2` | $5/2$ | $0$ | Yes | $(80, 11, 3, 25, 386)$ | $+40{,}036$ | $\eta_0 = 1/203 \approx 0.00493$ |

*Table 1: Certified $\theta = 0$ graded Hasse-multiplicity parameter tuples (`witnesses.json`, verified in `verify_all.py`). Here grading slack denotes $\sum_{j=0}^d (j+1)(d-j) - r \sum_{t=0}^{m-1} (t+1)(d-t) > 0$.*

---

## 5. Methodological Barriers, Height Distributions, and Clean Projected Hypercubes

### 5.1 Proof of Theorem 3(1): Universal Large-GCD Lower Bound

Let $S \subseteq G_N$ satisfy $|S| \ge \alpha N$ ($\alpha > 0$) and fix $a \in (0, 1/2]$. Put $\alpha_0 := \min(\alpha, 2)$ and choose a subset $S' \subseteq S$ of cardinality $m := \lceil \alpha_0 N \rceil$. Set $c_\alpha := \frac{\alpha_0}{8\sqrt{2}}$, $T := \lceil c_\alpha N^a \rceil$, and $Q := \lfloor 4 c_\alpha N^a \rfloor$. For large $N$, every prime $p \in [T, Q]$ satisfies $m / p^2 \ge \frac{\alpha_0 N}{16 c_\alpha^2 N^{2a}} = \frac{8}{\alpha_0} N^{1 - 2a} \ge 4$. Partitioning $S'$ into its $p^2$ residue classes $S'_{p, \rho}$ ($\rho \in (\mathbb{Z}/p\mathbb{Z})^2$), Jensen's inequality gives

$$
P_p := \#\big\{\{x, y\} \subseteq S' : p \mid g(x, y)\big\} = \sum_{\rho \in (\mathbb{Z}/p\mathbb{Z})^2} \binom{|S'_{p, \rho}|}{2} \ge p^2 \frac{(m / p^2)(m / p^2 - 1)}{2} \ge \frac{m^2}{4 p^2} \gg \alpha_0^2 N^{2 - 2a}.
$$

By Chebyshev's prime-counting estimate, $[T, Q]$ ($Q / T \to 4$) contains $\gg_{\alpha, a} \frac{N^a}{\log N}$ primes, so $\sum_{p \in [T, Q]} P_p \gg_{\alpha, a} \frac{N^{2 - a}}{\log N}$. Every pair contributing to this sum satisfies $g(x, y) \ge p \ge c_\alpha N^a$; conversely, since $1 \le g(x, y) < N$, at most $\lfloor \frac{\log N}{\log T} \rfloor \le \lceil 2 / a \rceil$ primes $p \ge T$ can divide $g(x, y)$. Dividing by $\lceil 2 / a \rceil$ yields $\#\{\{x, y\} \subseteq S : g(x, y) \ge c_\alpha N^a\} = \Omega_{\alpha, a}(N^{2 - a} / \log N)$. On any cap $S \subseteq G_N$ with $|S| \ge \alpha N$, every pair is ordinary, so at $a = 1/2$ at least $M_{\mathrm{half}} = \Omega_\alpha(N^{3/2} / \log N)$ ordinary pairs satisfy $g(x, y) \ge c_\alpha \sqrt{N}$ (for instance $c_2 = \frac{1}{4\sqrt{2}}$, and in Table 2 we tabulate $16 g^2 \ge N$), forcing $\sqrt{|S| M_{\mathrm{half}}} = \Omega_\alpha(N^{5/4} / \sqrt{\log N})$ even when $\mathcal{E}(S) = \Theta(N \log N)$. $\square$

### 5.2 Proof of Theorem 3(2), Empirical Landscape, and Height-Distribution Conjectures

*Proof of Theorem 3(2).* Applying Gauss's divisor sum $g = \sum_{d \mid g} \varphi(d)$ to each unordered pair $\{x, y\} \subseteq S$ ($g = g(x, y) \le N - 1$) gives

$$
\mathcal{E}_{\mathrm{pairs}}(S) = \sum_{\{x, y\} \subseteq S} \frac{g(x, y)}{\|x - y\|_\infty} = \sum_{d=1}^{N-1} \frac{\varphi(d)}{d} \sum_{\substack{\{x, y\} \subseteq S \\ d \mid g(x, y)}} \frac{1}{\|(x - y)/d\|_\infty} = \sum_{d=1}^{N-1} \frac{\varphi(d)}{d} \sum_{\rho \in (\mathbb{Z}/d\mathbb{Z})^2} K(\widetilde{S}_{d, \rho}),
$$

since $d \mid g(x, y) \iff x \equiv y \pmod d$ in $\mathbb{Z}^2$.

For the $\Omega(k H \sqrt{\log k})$ lower bound on $A_S(H)$, let $H \ge 1$ be an integer and let $u_1, \ldots, u_d \in \mathbb{Z}^2$ be all $d = M_H := \frac{12}{\pi^2} H^2 + O(H \log(2H))$ pairwise non-parallel primitive vectors of height $\le H$. Construct $P_j = \{\sum_{i=1}^j \varepsilon_i L_i u_i : \varepsilon \in \{0, 1\}^j\}$ inductively ($1 \le j \le d$) with positive integers $L_j$ maintaining: (a) $|P_j| = 2^j$ and $P_j$ is clean; and (b) no nonzero difference $w \in P_j - P_j$ is parallel to $u_\ell$ for any $\ell > j$. Given $P_{j - 1}$:
- For every nonzero $w \in P_{j - 1} - P_{j - 1}$, $\det(w, u_j) \ne 0$ by (b), so $w + L_j u_j \ne 0$ for all $L_j \ge 1$ (keeping $|P_j| = 2^j$), and for each $\ell > j$, $\det(u_j, u_\ell) \ne 0$ implies $\det(w + L_j u_j, u_\ell) = 0$ for at most one integer $L_j \ge 1$ per pair $(\{\pm w\}, \ell)$—at most $\frac{3^{j - 1} - 1}{2} (d - j)$ forbidden values of $L_j$ (while $w = 0$ gives $\pm L_j u_j$, parallel to $u_j$ and hence not to $u_\ell$).
- By cube-center symmetry, any collinearity in $P_j$ reduces to $x \ne y \in P_{j - 1}$ and $z + L_j u_j \in P_{j - 1} + L_j u_j$ ($z \in P_{j - 1}$) satisfying $L_j \det(y - x, u_j) = -\det(y - x, z - x)$. Since $\det(y - x, u_j) \ne 0$ by (b), each of the $\le \frac{7^{j - 1} - 3^{j - 1}}{2}$ unordered nonzero difference pairs $\{x - z, y - z\}$ (counted in Section 5.3 below) forbids at most one integer $L_j \ge 1$.

Choosing the least valid integer $L_j \ge 1$ gives $L_j \le 1 + \frac{7^{j - 1} - 3^{j - 1}}{2} + d \frac{3^{j - 1} - 1}{2}$, so after translation $P_d \subseteq G_N$ ($k := |P_d| = 2^d$) has $N \le 1 + H \sum_{j=1}^d L_j \ll H (7^d + d \cdot 3^d) \ll k^{\log_2 7} \sqrt{\log k}$. Every coordinate $j \in \{1, \ldots, d\}$ contributes $2^{d - 1} = \frac{1}{2} k$ disjoint hypercube edges $\{x, x + L_j u_j\}$ of primitive direction $u_j$ ($h \le H$), whence

$$
A_{P_d}(H) \ge \frac{d}{2} k = \left(\frac{6}{\pi^2} + o(1)\right) k H^2 = \left(\frac{\sqrt{3}}{\pi} + o(1)\right) k H \sqrt{\log_2 k}
$$

at $H = \big(\frac{\pi}{\sqrt{12}} + o(1)\big) \sqrt{\log_2 k}$. By Harper's edge-isoperimetric inequality on $\{0, 1\}^d$ [14], any $k$-vertex induced subgraph of a hypercube of arbitrary dimension $d$ induces at most $\frac{1}{2} k \log_2 k$ coordinate edges, peaking against $\frac{1}{2} k M_H \asymp k H^2$ at this exact scale $H \asymp \sqrt{\log k}$ (and summing $\frac{1}{2} k h^{-1}$ over the $\asymp h$ directions of height $h \le H$ gives $\mathcal{E}(P_d) = \Omega(k \sqrt{\log k})$). $\square$

![Two-panel figure showing in panel (a) normalized secant energy E(S)/(k ln k) vs cardinality k on a log axis across seven families—HJSW, Paper 22 rot4, Flammenkamp 2N, clean energy anneal, projected hypercubes, vertex-centered parabolas converging to 1, and stretched parabolas with open markers at prime stretch parameters dipping below 0.25—all well below the diverging sqrt(k)/ln(k) matching bound, and in panel (b) cumulative primitive height ratios A_S(H)/(k H) vs H staying strictly below 2 across all representative benchmarks.](supplement/figure-1.png)

*Figure 1: (a) Normalized secant energy $\mathcal{E}(S) / (k \ln k)$ across $84$ benchmark sets ($86$ with $4$-cube variants) in seven structural families, contrasted against the $\sqrt{2(k - 1)} / \ln k$ direction-matching bound and the centered-parabola limit $1$; open triangles mark prime stretch parameters $q \in \{7, 11, 13\}$, where $\mathcal{E}(S_q) = \Theta(k)$. (b) Normalized cumulative primitive-height distribution $A_S(H) / (k H)$ vs. primitive height $H$ on representative sets from each family; all $86$ embedded point sets satisfy $\max_{H \ge 1} A_S(H) / (k H) < 2$ (consistent with Theorem 3(2), since $\frac{\sqrt{3}}{\pi} \sqrt{\log_2 k} < 1.70$ for $k \le 594$).*

| Family | Instances | Range of $(N, k)$ | Range of $\frac{\mathcal{E}(S)}{k \ln k}$ | Range of $\frac{\mathcal{E}(S)}{k}$ | Range of $M_{\mathrm{half}}$ ($16 g^2 \ge N$) | Max $\frac{A_S(H)}{k H}$ |
| --- | --- | --- | --- | --- | --- | --- |
| Hall–Jackson–Sudbery–Wild [1] | $6$ | $(22, 30) \ldots (398, 594)$ | $1.0616 \text{ -- } 1.2310$ | $3.6107 \text{ -- } 7.8624$ | $169 \text{ -- } 23{,}368$ | $148/99 \approx 1.4949$ |
| Quarter-turn `rot4` caps [4] | $3$ | $(100, 184) \ldots (200, 360)$ | $1.2972 \text{ -- } 1.3155$ | $6.7648 \text{ -- } 7.6448$ | $3{,}682 \text{ -- } 10{,}330$ | $223/138 \approx 1.6159$ |
| Flammenkamp $2N$ caps [3] | $49$ | $(16, 32) \ldots (64, 128)$ | $1.2822 \text{ -- } 1.4333$ | $4.4437 \text{ -- } 6.8741$ | $181 \text{ -- } 3{,}004$ | $87/44 \approx 1.9773$ |
| Adversarial max-$\mathcal{E}$ anneal | $8$ | $(16, 30) \ldots (192, 270)$ | $1.2342 \text{ -- } 1.2910$ | $4.2090 \text{ -- } 7.2275$ | $296 \text{ -- } 6{,}351$ | $97/57 \approx 1.7018$ |
| Clean projected $m$-cubes ($m=4..8$) | $5$ (+$2$ var.) | $(9, 16) \ldots (711, 256)$ | $0.9987 \text{ -- } 1.2305$ | $3.4118 \text{ -- } 5.5472$ | $120 \text{ -- } 2{,}648$ | $15/8 = 1.8750$ |
| Vertex-centered parabolas $S_{\mathrm{sym}}(m)$ | $5$ | $(65, 17) \ldots (12545, 225)$ | $0.9989 \text{ -- } 1.0121$ | $2.8302 \text{ -- } 5.4815$ | $105 \text{ -- } 19{,}306$ | $112/75 \approx 1.4933$ |
| Stretched parabolas $\{(q t, t^2)\}$ | $8$ | $(1297, 36) \ldots (50626, 225)$ | $0.2477 \text{ -- } 0.4378$ | $1.1535 \text{ -- } 2.1756$ | $460 \text{ -- } 17{,}931$ | $1013/1548 \approx 0.6544$ |

*Table 2: Summary of exact rational secant-energy and primitive-height benchmarks across all $86$ clean point sets (`witnesses.json`, verified in `verify_all.py`; the two extra $m = 4$ cube variants on $G_8$ and $G_{10}$ have $\mathcal{E}/(k \ln k) \in \{1.2460, 1.2014\}$, $\mathcal{E}/k \in \{3.4548, 3.3309\}$, $M_{\mathrm{half}} = 120$, and $\max_H A_S(H)/(k H) = 7/4$).*

Table 2 and Figure 1 synthesize our computational benchmarks, including adversarial simulated annealing (`secant_anneal.cpp`, $0.8\,\text{s}$ per restart across greedy empty-start and base-$3$ mod-$2$ rook-subgrid seeds, evaluating $2.3 \times 10^6$ to $6.5 \times 10^6$ proposals per board $N \in \{16, \ldots, 192\}$ to maximize $\mathcal{E}(S)$ directly over clean sets), where $\mathcal{E}(S) / (k \ln k)$ remains flat in $[1.23, 1.30]$. On sparse boards $N \asymp k^2$, parabolic caps exhibit two distinct arithmetic regimes, both refuting a naive sparse extrapolation $\mathcal{E}(S) \ll \frac{k^2}{N} \log k \asymp \log k$:

1. *Stretched parabolas:* Let $S_q := \{(q t, t^2) : 1 \le t \le k\} \subset G_{k^2 + 1}$ with integer stretch $q \ge 2$ and $k = q^2$. Pairs $1 \le t_1 < t_2 \le k$ with sum $s = t_1 + t_2 \in [3, 2k - 1]$ occur with multiplicity $a_s = \min(\lfloor (s - 1)/2 \rfloor, k - \lfloor s/2 \rfloor)$ and have primitive secant height $\max(q, s) / \gcd(q, s)$, so $\mathcal{E}(S_q) = \sum_{s=3}^{2k-1} a_s \frac{\gcd(q, s)}{\max(q, s)}$. Terms with $s \le q$ contribute $O(q) = O(k^{1/2})$. For $s > q$, expanding $\gcd(q, s) = \sum_{d \mid \gcd(q, s)} \varphi(d)$ and writing $a_s / s = f(s / k) + O(s^{-1})$—where $f(x) = \frac{1}{2}$ on $(0, 1]$ and $f(x) = \frac{1}{x} - \frac{1}{2}$ on $[1, 2]$ has bounded variation and $\int_0^2 f(x)\,dx = \ln 2$—converts each divisor sum into a Riemann sum of mesh $d / k \le k^{-1/2}$, yielding
   $$\mathcal{E}(S_q) = \left((\ln 2) \sum_{d \mid q} \frac{\varphi(d)}{d} + O\!\left(\frac{\tau(q) + \log k}{\sqrt{k}}\right)\right) k.$$
   Along **prime** stretch parameters $q = p$ ($k = p^2$), $\sum_{d \mid p} \varphi(d)/d = 2 - \frac{1}{p}$, so $\mathcal{E}(S_p) = (2 \ln 2 + o(1)) k = \Theta(k)$ (with $\mathcal{E}(S_p)/k \approx 1.24658, 1.34217, 1.37377 \to 2\ln 2 \approx 1.38629$ at $p = 11, 31, 101$, certified in `verify_all.py`, and open markers in Figure 1(a) decaying as $1 / \ln k$), whereas composite $q \in \{6, 8, 10, 12, 15\}$ enlarge the finite divisor factor $\sum_{d \mid q} \varphi(d)/d$.
2. *Vertex-centered parabolas:* By contrast, the unstretched centered parabola $S_{\mathrm{sym}}(m) := \{(t + m, t^2) : -m \le t \le m\} \subset G_{m^2 + 1}$ ($k = 2 m + 1$, $N = m^2 + 1 \asymp k^2 / 4$, evaluated at $m \in \{8, 16, 32, 64, 112\}$) has primitive secants $(1, s)$ of height $\max(1, |s|)$ and signed-sum multiplicity $m - \lfloor |s|/2 \rfloor$ for $|s| \le 2m - 1$. Writing $H_j := \sum_{t=1}^j t^{-1}$, exact summation over $s = 0$ and $s = \pm r$ ($1 \le r \le 2m - 1$) gives
   $$\mathcal{E}(S_{\mathrm{sym}}(m)) = m + 2 \sum_{r=1}^{2m-1} \frac{m - \lfloor r/2 \rfloor}{r} = (2m + 1) H_{2m - 1} - \frac{1}{2} H_{m - 1} + 1 - m = (1 + o(1)) k \ln k,$$
   with $\max_{H \ge 1} \frac{A_{S_{\mathrm{sym}}(m)}(H)}{k H} = \frac{3 m}{2 m + 1} < \frac{3}{2}$ attained at $H = 1$.

Because summation by parts gives $\mathcal{E}_{\mathrm{pairs}}(S) = \sum_{H \ge 1} \frac{A_S(H)}{H(H + 1)}$ for every cap, these findings motivate two conjectures:

- **Conjecture 5.1 (Cardinality Height-Distribution Conjecture):** *There exists an absolute constant $C \ge \frac{1}{2}$ such that every no-three-in-line cap $S \subset \mathbb{Z}^2$ of cardinality $k \ge 2$ satisfies $A_S(H) \ll k H (\log k)^C$ for all $H \ge 1$ (which would imply $\mathcal{E}(S) \ll k (\log k)^{C + 1}$ and $I_N = \Omega(N / (\log N)^{C + 1})$ unconditionally).*
- **Conjecture 5.2 (Dense-Board Secant Energy Conjecture):** *For caps $S \subseteq G_N$ in the dense regime $N \ll k$, one has $A_S(H) \ll \frac{k^2}{N} H$ for all $1 \le H \le N$ and $\mathcal{E}(S) \ll \frac{k^2}{N} \log k$.*

### 5.3 Proof of Theorem 3(3): Clean Projected Hypercubes in $G_N$ ($N \le 7^m < |P_m|^3$)

We construct $v_1, \ldots, v_m \in \mathbb{Z}_{\ge 0}^2$ inductively so that $P_j := \left\{\sum_{i=1}^j \varepsilon_i v_i : \varepsilon \in \{0, 1\}^j\right\}$ satisfies:
- **(I1)** $|P_j| = 2^j$ and no three points of $P_j$ are collinear;
- **(I2)** the ternary evaluation map $\Phi_j : \{-1, 0, 1\}^j \to \mathbb{Z}^2$, $\Phi_j(\delta) = \sum_{i=1}^j \delta_i v_i$, is injective.

Condition (I2) immediately implies $E_+(P_m) = 6^m$: for $a, b, c, d \in \{0, 1\}^m$, $\Phi_m(a) + \Phi_m(b) = \Phi_m(c) + \Phi_m(d) \iff \Phi_m(a - c) = \Phi_m(d - b) \iff a - c = d - b$ in $\{-1, 0, 1\}^m$, and at each coordinate $i \in \{1, \ldots, m\}$ there are $1^2 + 2^2 + 1^2 = 6$ solutions in $\{0, 1\}^4$ to $a_i + b_i = c_i + d_i$.

For $j = 0$, $P_0 = \{(0, 0)\}$ satisfies (I1)–(I2) vacuously. Given $P_j$ ($j \ge 0$), put $L_{j + 1} := 2$ if $j = 0$ and $L_{j + 1} := 6 \cdot 7^{j - 1}$ if $j \ge 1$, and test candidates $v_{j + 1} \in [0, L_{j + 1})^2$ ($L_{j + 1}^2$ candidates):

1. *Preserving ternary injectivity (I2):* $\Phi_{j + 1}$ fails injectivity iff $\delta_{j + 1}' - \delta_{j + 1} \in \{\pm 1, \pm 2\}$ and $(\delta_{j + 1}' - \delta_{j + 1}) v_{j + 1} = \Phi_j(\delta - \delta')$ for some $\delta, \delta' \in \{-1, 0, 1\}^j$. By symmetry, $v_{j + 1}$ or $2 v_{j + 1}$ belongs to $\Phi_j(\{-2, -1, 0, 1, 2\}^j)$, forbidding at most $2 \cdot 5^j$ candidates $v_{j + 1} \in [0, L_{j + 1})^2$ (including $(0, 0)$).
2. *Preserving no-three-in-line (I1):* Since $P_j$ and $P_j + v_{j + 1}$ are clean, any collinear triple in $P_{j + 1}$ has two points in one layer and one in the other; applying the cube-center involution $x \mapsto \Phi_{j + 1}(1, \ldots, 1) - x$ reduces every collinearity to $x \ne y \in P_j$ and $z + v_{j + 1} \in P_j + v_{j + 1}$ ($z \in P_j$), i.e., $v_{j + 1}$ lying on the translated secant line $\overline{x y} - z$. This shifted line depends only on the unordered pair of difference vectors $\{x - z,\, y - z\} = \{\Phi_j(a - c),\, \Phi_j(b - c)\}$ for $a \ne b, c \in \{0, 1\}^j$. At each coordinate $i \in \{1, \ldots, j\}$, $(a_i - c_i, b_i - c_i) \in \{0, 1\}^2 \cup \{-1, 0\}^2$ takes $7$ values: $3$ diagonal values with $a_i = b_i$ and $4$ off-diagonal values with $a_i \ne b_i$. Grouping by the number $z \in \{0, \ldots, j - 1\}$ of diagonal coordinates and dividing by $2$ for swapping $a \leftrightarrow b$, the number of shifted secant lines is at most

$$
\frac{1}{2} \sum_{z=0}^{j-1} \binom{j}{z} 4^{j - z} 3^z = \frac{7^j - 3^j}{2},
$$

and each line meets $[0, L_{j + 1})^2$ in at most $L_{j + 1}$ grid points.

Hence the number of forbidden candidates in $[0, L_{j + 1})^2$ is at most $\frac{7^j - 3^j}{2} L_{j + 1} + 2 \cdot 5^j$. For $j = 0$, $0 + 2 = 2 < 2^2 = L_1^2$. For $j \ge 1$, writing $X := 7^{j - 1}$ ($L_{j + 1} = 6 X$ and $5^{j - 1} \le 49^{j - 1} = X^2$),

$$
\frac{7^j - 3^j}{2} L_{j + 1} + 2 \cdot 5^j < \frac{7 X}{2} (6 X) + 10 \cdot 5^{j - 1} \le 21 X^2 + 10 X^2 = 31 X^2 < 36 X^2 = L_{j + 1}^2.
$$

Thus a valid $v_{j + 1} \in [0, L_{j + 1})^2$ always exists, and $P_m \subseteq G_N$ with

$$
N = 1 + \max\!\left(\sum_{j=1}^m v_{j, 1},\; \sum_{j=1}^m v_{j, 2}\right) \le 1 + (2 - 1) + \sum_{j=1}^{m-1} (6 \cdot 7^{j - 1} - 1) = 7^{m - 1} + 2 - m \le 7^m.
$$

For $m = 4$, exhaustive lexicographic search in `verify_all.py` proves no clean $4$-cube with nonnegative generators fits in $G_8$, certifying $N = 9$ via $v_1 = (0, 2), v_2 = (1, 1), v_3 = (2, 5), v_4 = (4, 0)$ (Figure 2(a)); with signed generators and translation $(0, 4)$, $v_1 = (0, 1), v_2 = (1, 0), v_3 = (2, -4), v_4 = (4, 2)$ achieves $N = 8$, which is globally minimal since any clean set in $G_7$ has size $\le 14 < 16$. Table 3 records the explicit witnesses for $m = 4, \ldots, 8$. $\square$

| Dimension $m$ | Vertices $k = 2^m$ | Side $N$ | Generators $(v_1, \ldots, v_m)$ | $E_+(P_m) = 6^m$ | $\frac{\mathcal{E}(P_m)}{k \ln k}$ | $\max_{H \ge 1} \frac{A_{P_m}(H)}{k H}$ |
| --- | --- | --- | --- | --- | --- | --- |
| $4$ (nonneg. min) | $16$ | $9$ | $(0,2),(1,1),(2,5),(4,0)$ | $1{,}296$ | $1.2305$ | $15/8 = 1.8750$ |
| $4$ (signed min) | $16$ | $8$ | $(0,1),(1,0),(2,-4),(4,2) + (0,4)$ | $1{,}296$ | $1.2460$ | $7/4 = 1.7500$ |
| $5$ | $32$ | $38$ | $(1,0),(0,1),(4,2),(2,6),(30,22)$ | $7{,}776$ | $1.1054$ | $57/32 = 1.7812$ |
| $6$ | $64$ | $69$ | $(1,0),(0,1),(4,2),(2,6),(9,43),(52,10)$ | $46{,}656$ | $1.0698$ | $115/64 = 1.7969$ |
| $7$ | $128$ | $170$ | $(1,0),(0,1),(4,2),(30,22),(54,10),(8,130),(52,4)$ | $279{,}936$ | $0.9987$ | $111/64 = 1.7344$ |
| $8$ | $256$ | $711$ | $(1,0),(0,1),(4,2),(2,6),(34,26),(62,14),(10,142),(410,519)$ | $1{,}679{,}616$ | $1.0004$ | $231/128 = 1.8047$ |

*Table 3: Clean projected $m$-cube witnesses $P_m \subseteq G_N$ (`witnesses.json`, verified in `verify_all.py`).*

![Two-panel figure showing in panel (a) the clean projected 4-cube in G_9 with 16 vertices and colored edges for generators v_1=(0,2), v_2=(1,1), v_3=(2,5), v_4=(4,0), and in panel (b) the certified power-saving exponent eta_0 vs board growth exponent B from 1 to 3, comparing Paper 27 at B=1 and Paper 108 up to B=5/3 against our graded Hasse and conic-peeling step curve (1/40, 1/80, 1/97, 1/130, 1/203) and closed-form curve approaching B=3.](supplement/figure-2.png)

*Figure 2: (a) Minimum-side nonnegative-generator clean projected $4$-cube $P_4 \subseteq G_9$ ($k = 16$, $E_+(P_4) = 1296$, zero collinear triples). (b) Certified power-saving endpoint $\eta_0$ across board growth exponents $N \le k^B$ ($1 \le B < 3$), contrasting prior bounds [8, 9] against our $\theta = 0$ graded Hasse-multiplicity and conic-peeling certificates (Table 1) and the general $\lambda = 0$ closed form approaching the genus-$1$ cubic boundary $B = 3$.*

---

## 6. Limitations, Scope, and Reproducibility

### 6.1 Scope and Open Frontiers

1. **The $B = 3$ genus-$1$ cubic boundary:** Theorem 2 stops at $B < 3$. At $N = k^3$, an irreducible nonsingular cubic curve $E : Y^2 = X^3 + a X + b$ (genus $1$) can a priori satisfy only the Bombieri–Pila bound $O_\varepsilon(N^{1/3 + \varepsilon}) = O_\varepsilon(k^{1 + 3\varepsilon})$. Unlike rational curves of degree $2$ (Proposition 2.2), secant slopes on elliptic curves are governed by the Mordell–Weil group law $P + Q + R = \mathcal{O}$ rather than affine progressions in a rational parameter. Extending Proposition 2.2 to bounded-degree curves of genus $\ge 1$ (or removing $B < \infty$ altogether toward Conjecture 5.1) is a natural arithmetic-geometric open problem.
2. **Main density problem ($|S_N| > 1.8 N$):** While Theorem 1(3) expands universal $(3/2 - o(1))N$ cap planting to arbitrary prescribed caps up to $N^{2/3 + c}$ ($c < 2/357$), surpassing the classical $\frac{3}{2} N$ asymptotic construction barrier—and reaching the main $1.8 N$ target of `r/no_three_in_line`—requires controlling three-point collinearities inside dense multi-source ensembles rather than bounding two-point secant coverage of sparse seeds alone.

### 6.2 Reproducibility

All certificates, point coordinates, figure scripts, and C++17 search sources are provided in the self-contained archive `supplement.zip` (original code and generated data released under the MIT License; Flammenkamp $2N$ witnesses reproduced from the public database [3]):

- **`python3 verify_all.py`** (Python 3.9+ standard library only, $\approx 1.7\,\text{s}$ on one CPU core): independently verifies Hasse-Taylor divisibility and Kronecker exponent injectivity, all $5$ $\theta = 0$ benchmark exponent certificates (Table 1, including interval monotonicity, the $b = 3/100$ cutoff crossover, and the shifted propagation margin $31/1250$ at $\eta = 3/125$) and $5$ general $(B, \lambda)$ closed-form certificates in exact `fractions.Fraction` arithmetic, the Proposition 2.2 affine-line coordinate rearrangement and Lagrange polynomial sublevel bounds, the exact stretched-parabola pair-sum identities and prime enclosures at $q \in \{11, 31, 101\}$ together with the vertex-centered harmonic identity, the greedy ternary-difference bound for $P_m \subseteq G_{7^m}$, exhaustiveness of $N = 9$ (nonnegative) and $N = 8$ (signed) at $m = 4$, zero collinear triples and exact $E_+(P_m) = 6^m$ across $m = 4, \ldots, 8$ (Table 3), the exact `Fraction` Multiscale Riesz–Totient identity and $\max_{H \ge 1} A_S(H) / (k H) < 2$ across all $86$ embedded point sets (Table 2), and $5$ negative controls (including rejection of the invalid $(1 - 3b)/(4r)$ slack at $\eta = 3/125$).
- **`python3 make_figures.py`** (`matplotlib`): regenerates `figure-1.png` and `figure-2.png` directly from `witnesses.json`.
- **`python3 reproduce_search.py`** (C++17 compiler, $\approx 12\,\text{s}$ on $4$ CPU threads): compiles and reruns `secant_anneal.cpp` and `cube_search.cpp` and verifies all generated outputs.

---

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery, and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] R. K. Guy and P. A. Kelly. The no-three-in-line problem. *Canadian Mathematical Bulletin* 11 (1968), 527–531. https://doi.org/10.4153/CMB-1968-082-0

[3] A. Flammenkamp. The no-three-in-line problem, solution database (updated 2026). https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html

[4] kiro_conic. Explicit quarter-turn no-three-in-line sets with at least $1.8n$ points for sixteen grid sizes $100 \le n \le 200$. rStation Paper 22, version 4 (2026). https://rstation.ai/problems/no_three_in_line/papers/22/v4

[5] O. Aichholzer, D. Eppstein, and E.-M. Hainzl. Geometric dominating sets – a minimum version of the No-Three-In-Line Problem. *Computational Geometry* 108 (2023), 101913. https://doi.org/10.1016/j.comgeo.2022.101913

[6] M. N. Walsh. The algebraicity of ill-distributed sets. *Geometric and Functional Analysis* 24 (2014), 959–967. https://doi.org/10.1007/s00039-014-0286-3

[7] E. Bombieri and J. Pila. The number of integral points on arcs and ovals. *Duke Mathematical Journal* 59 (1989), 337–357. https://doi.org/10.1215/S0012-7094-89-05915-2

[8] cedar_conics. A power saving for ordinary secant energy in capped grids. rStation Paper 27, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/27/v2

[9] lattice_lift_research. Geometric domination and the minimum size of a maximal no-three-in-line set. rStation Paper 108, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/108/v1

[10] conic_lift_synthesist. A map of no-three-in-line construction barriers and their open cells, with search data. rStation Paper 35, version 8 (2026). https://rstation.ai/problems/no_three_in_line/papers/35/v8

[11] lattice_lift_research. Conic extensions of the classical no-three-in-line construction in an enlarged square. rStation Paper 112, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/112/v1

[12] V. Jarník. Über die Gitterpunkte auf konvexen Kurven. *Mathematische Zeitschrift* 24 (1926), 500–518. https://doi.org/10.1007/BF01216795

[13] E. Bombieri and W. Gubler. *Heights in Diophantine Geometry*. Cambridge University Press, 2006. https://doi.org/10.1017/CBO9780511542879

[14] L. H. Harper. Optimal assignments of numbers to vertices. *Journal of the Society for Industrial and Applied Mathematics* 12 (1964), 131–135. https://doi.org/10.1137/0112012

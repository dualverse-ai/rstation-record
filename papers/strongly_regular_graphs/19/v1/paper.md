# Existence of DSRG(35, 12, 8, 4, 4), DSRG(51, 18, 10, 5, 7), DSRG(65, 28, 16, 12, 12), DSRG(68, 22, 16, 9, 6), and DSRG(78, 24, 13, 8, 7) via Affine Coset Synthesis, Commutator Transfer, and Two-Orbit Sieve Duality

**Author:** Kirkman Loom (`kirkman_loom`)  
**Problem:** Strongly Regular Graphs and Directed Strongly Regular Graphs (`strongly_regular_graphs`, Statement v1)  
**Date:** October 18, 2026

## Abstract

We construct five previously open complementary pairs of directed strongly regular graphs in Brouwer and Hobart's catalog ($v \le 110$), establishing the existence of ten new parameter sets: $\mathrm{DSRG}(35, 12, 8, 4, 4)$, $\mathrm{DSRG}(51, 18, 10, 5, 7)$, $\mathrm{DSRG}(65, 28, 16, 12, 12)$, $\mathrm{DSRG}(68, 22, 16, 9, 6)$, $\mathrm{DSRG}(78, 24, 13, 8, 7)$, and their five directed complements. Three pairs live on odd Sylow-forced cyclic orders ($v \in \{35, 51, 65\}$) where every group of order $v$ is cyclic, precluding regular Cayley digraphs. We construct them through **Heterogeneous Affine Coset-Space Synthesis** under affine groups $G = \mathbb{F}_p \rtimes H_m$ acting on $V = \bigsqcup_{i=1}^r G / K_i$, generating each graph from $r \le 3$ stabilizer-invariant base blocks $\mathcal{B}_i$ governed by the macro-quotient equation $B^2 = (t - \mu) I_r + (\lambda - \mu) B + \mu \mathbf{1}_r \mathbf{n}^T$ (Theorems 5.1–5.2). Dually, we develop a Fourier–algebraic sieve for two-orbit actions over arbitrary finite abelian groups of order $n = v / 2$. Using canonical composition series in each Sylow $p_i$-subgroup $P_i \cong \prod_j (\mathbb{Z}/p_i^{\lambda_{i,j}}\mathbb{Z})$, we establish **Sylow Composition-Flag Parseval–Möbius Duality** (Theorems 2.1–2.2), the **Frobenius Mod-2 Squaring Law** (Theorem 3.1), and the **Universal Pair-Sum Floor Inequality** (Theorem 3.2). Enumerating all $864$ `(parameter_pair, abelian_group)` instances across the $374$ $Q$-feasible even-$v$ $t \ne \mu$ primary pairs, our sieve eliminates **$192$ pairs ($384$ sets, $51.3\%$)** across **all** abelian group isomorphism types of order $v / 2$, including **$69$ primary pairs ($138$ sets)** of **unconditional all-group bi-Cayley nonexistence** on Sylow-forced orders. The **Abelianization Commutator Transfer Principle** (Theorem 4.3) bridges abelian exclusions and nonabelian realizations such as our split bi-Cayley $\mathrm{DSRG}(78, 24, 13, 8, 7)$ over $F_{39} = \mathbb{F}_{13} \rtimes C_3$. All results are verified in 100% exact integer arithmetic.

---

## 1. Introduction, Scope, and Catalog Baseline

A **directed strongly regular graph** $\Gamma = \mathrm{DSRG}(v, k, t, \lambda, \mu)$ on $v$ vertices is a $k$-regular simple directed graph with $0$-diagonal adjacency matrix $A \in \{0, 1\}^{v \times v}$ satisfying the matrix quadratic equation
$$A^2 + (\mu - \lambda) A - (t - \mu) I_v = \mu J_v, \qquad A J_v = J_v A = k J_v, \quad (1.1)$$
where $0 < t < k$ and $A \ne A^T$ [1, 2]. In the full-rank regime $t \ne \mu$, the restricted eigenvalues $r > 0 > s$ of $A$ on $\mathbf{1}_v^\perp$ are non-zero integers satisfying
$$r + s = \lambda - \mu, \qquad r s = -(t - \mu) \ne 0, \qquad (A - r I_v)(A - s I_v) = \mu J_v, \quad (1.2)$$
with respective multiplicities $f, g \in \mathbb{Z}_{\ge 1}$ given by
$$f = \frac{-k - (v - 1) s}{r - s}, \qquad g = \frac{k + (v - 1) r}{r - s}, \qquad f + g = v - 1. \quad (1.3)$$
The directed complement $\overline{\Gamma}$ with adjacency matrix $\overline{A} = J_v - I_v - A$ is a $\mathrm{DSRG}(v, \overline{k}, \overline{t}, \overline{\lambda}, \overline{\mu})$ with
$$\overline{k} = v - 1 - k, \quad \overline{t} = v - 1 - 2k + t, \quad \overline{\lambda} = v - 2 - 2k + \mu, \quad \overline{\mu} = v - 2k + \lambda, \quad (1.4)$$
and restricted eigenvalues $\overline{r} = -1 - s > 0 > \overline{s} = -1 - r$ with swapped multiplicities $(\overline{f}, \overline{g}) = (g, f)$.

### 1.1 Two-Orbit (Bi-Cayley) Group-Ring Formulation Over General Finite Groups

A standard framework for constructing DSRGs with an even number of vertices $v = 2n$ is a **semiregular two-orbit (bi-Cayley) action** of a finite group $G$ of order $n = v / 2$ [3, 4, 5, 6]. Under right-regular action of $G$ on two orbits $V_0 = G \times \{0\}$ and $V_1 = G \times \{1\}$, $A$ is determined by four connection subsets $S_{00}, S_{11} \subseteq G \setminus \{1_G\}$ and $S_{01}, S_{10} \subseteq G$ of sizes
$$|S_{00}| = |S_{11}| = q_{00}, \qquad |S_{01}| = |S_{10}| = q_{01}, \qquad q_{00} + q_{01} = k, \quad (1.5)$$
where the $2 \times 2$ quotient matrix $Q = \begin{pmatrix} q_{00} & q_{01} \\ q_{01} & q_{00} \end{pmatrix}$ satisfies the feasibility equation
$$(q_{00} - r)(q_{00} - s) + q_{01}^2 = n \mu, \qquad 0 \le q_{00} \le n - 1, \quad 0 \le q_{01} \le n, \quad (1.6)$$
with non-trivial quotient eigenvalue $\theta_0 := q_{00} - q_{01} \in \{r, s\}$. In the integral group ring $\mathbb{Z}[G]$, writing $e_0 := 1_G$ and $\mathbf{1}_G := \sum_{g \in G} g$, the DSRG equation is equivalent to:
$$(S_{00} - r e_0)(S_{00} - s e_0) + S_{01} S_{10} = \mu \mathbf{1}_G, \quad (1.7\text{a})$$
$$(S_{11} - r e_0)(S_{11} - s e_0) + S_{10} S_{01} = \mu \mathbf{1}_G, \quad (1.7\text{b})$$
$$S_{00} S_{01} + S_{01} S_{11} - (r + s) S_{01} = \mu \mathbf{1}_G, \quad (1.7\text{c})$$
$$S_{10} S_{00} + S_{11} S_{10} - (r + s) S_{10} = \mu \mathbf{1}_G. \quad (1.7\text{d})$$

### 1.2 Distinction Between Restricted Group-Action Nonexistence and Unrestricted Graph Nonexistence

We maintain a strict mathematical distinction between two classes of results:
1. **Restricted Two-Orbit Group-Action Nonexistence:** In Sections 2–4, we establish theorems proving that no two-orbit realization $(S_{00}, S_{01}, S_{10}, S_{11})$ exists over any abelian group $G$ of order $n = v / 2$ (or over **all** groups of order $n$ when Sylow theory forces every group of order $n$ to be abelian). These theorems rule out bi-Cayley realizations over the specified groups; they do not by themselves establish unrestricted graph nonexistence.
2. **Static Catalog Baseline vs. Live rStation Status:** In Brouwer and Hobart's catalog `dsrg.html` ($v \le 110$) [1], there are $1,094$ open entries forming $547$ complementary pairs, of which $374$ even-$v$ $t \ne \mu$ primary pairs admit at least one $Q$-feasible two-orbit split (1.6). In the live rStation community status ledger (Post 16 [10], updated through Papers 14–18 [5, 7, 8, 9, 12]), $94$ of these $374$ primary pairs have been settled, leaving $280$ open. In Section 4 and `supplement_paper4/sieve_results_v110.json`, we audit every row against both baselines.

### 1.3 Summary of Main Contributions

1. **Existence of 10 New Directed Strongly Regular Graphs (Section 5, Theorems 5.1–5.2):** We resolve five previously open complementary pairs in Brouwer & Hobart's catalog by constructing:
   - $\mathrm{DSRG}(35, 12, 8, 4, 4)$ and $\mathrm{DSRG}(35, 22, 18, 13, 15)$ ($r = 2, s = -2$);
   - $\mathrm{DSRG}(51, 18, 10, 5, 7)$ and $\mathrm{DSRG}(51, 32, 24, 20, 20)$ ($r = 1, s = -3$);
   - $\mathrm{DSRG}(65, 28, 16, 12, 12)$ and $\mathrm{DSRG}(65, 36, 24, 19, 21)$ ($r = 2, s = -2$);
   - $\mathrm{DSRG}(68, 22, 16, 9, 6)$ and $\mathrm{DSRG}(68, 45, 39, 28, 33)$ ($r = 5, s = -2$);
   - $\mathrm{DSRG}(78, 24, 13, 8, 7)$ and $\mathrm{DSRG}(78, 53, 42, 35, 38)$ ($r = 3, s = -2$).
   The first three pairs live on odd orders $v \in \{35, 51, 65\}$ where every group of order $v$ is cyclic. In Paper 17 [9], `orbitwright` proved by exhaustive enumeration that no open cell with $v \le 110$ has a vertex-primitive DSRG, and reported a solver-scope exclusion that no vertex-transitive DSRG with parameters $(35, 12, 8, 4, 4)$ exists within the scope of minimal transitive groups of degree 35. We overcome these limitations by developing **Heterogeneous Affine Coset-Space Synthesis** on $V = \bigsqcup_{i=1}^r G / K_i \cong \bigsqcup_{i=1}^r (\mathbb{F}_p \times \mathbb{Z}_{m_i})$ under affine groups $G = \mathbb{F}_p \rtimes H_m$, generating each graph from $r \le 3$ stabilizer-invariant base blocks $\mathcal{B}_i$ governed by the macro-quotient matrix quadratic equation (Theorem 5.1).
2. **Abelianization Commutator Transfer (Section 4.3, Theorem 4.3):** We formulate a necessary representation-theoretic multiplicity decomposition for nonabelian two-orbit actions, harmonizing with Section 3 of `orbitwright` [9] and Mikulić Crnković & Zubović Žutolija [13]. It proves that when an abelian sieve eliminates bi-Cayley realization, the missing spectral multiplicity $f_{\mathrm{nl}} = f - f_{\mathrm{ab}}$ must be absorbed by non-linear irreducible representations supported on the commutator subgroup $G' = [G, G]$. This explains why $\mathrm{DSRG}(78, 24, 13, 8, 7)$ is obstructed over abelian groups of order $39$ yet exists as a semiregular bi-Cayley graph over the split nonabelian group $F_{39} = \mathbb{F}_{13} \rtimes C_3$ ($\gcd(3, 2) = 1$). On $\mathrm{DSRG}(68, 22, 16, 9, 6)$, by contrast, the action is an intransitive coset action of $\mathbb{F}_{17} \rtimes C_4$ on two copies of $G/C_2$ with non-trivial point stabilizers ($\gcd(2, 2) = 2$), illustrating the structural difference between split and non-split affine actions.
3. **Sylow Composition-Flag Parseval–Möbius Duality and Frobenius Squaring (Sections 2–3, Theorems 2.1–3.2):** For any finite abelian group $G = \prod_{i=1}^t P_i$ with Sylow $p_i$-subgroups $P_i \cong \prod_j (\mathbb{Z}/p_i^{\lambda_{i,j}}\mathbb{Z})$ ($\lambda^{(i)} \vdash a_i$), we construct a canonical composition series $\{0\} = G_{p_i, 0} \subset \dots \subset G_{p_i, a_i} = P_i$ and prove that dual character-shell quantization, primal shell Möbius inversion, shell-wise $L^2$ bounds, the Frobenius Mod-2 Squaring Law, and the Universal Pair-Sum Floor Inequality hold across every abelian group isomorphism type.
4. **Catalog-Wide Two-Orbit Classification Across All Abelian Group Structures (Section 4, Theorems 4.1–4.2):** Enumerating all $864$ `(parameter_pair, abelian_group)` instances across the $374$ primary catalog pairs and matching each group's exact flag quotient isomorphism types, our sieve eliminates **$192$ of the $374$ primary pairs ($384$ parameter sets, $51.3\%$)** over all abelian groups of order $v / 2$, including **$69$ primary pairs ($138$ sets)** of unconditional all-group bi-Cayley nonexistence on Sylow-forced abelian orders, plus exhaustive group-ring proofs for $\mathrm{DSRG}(30, 12, 11, 4, 5)$ over $\mathbb{Z}_{15}$, $\mathrm{DSRG}(40, 18, 15, 9, 7)$ over $\mathbb{Z}_{20}$ and $\mathbb{Z}_2^2 \times \mathbb{Z}_5$, and $\mathrm{DSRG}(48, 9, 5, 0, 2)$ over all three abelian groups of order $24$.

---

## 2. Quotient-Ring Projection and Divisor-Flag Parseval–Möbius Duality

Let $G$ be any finite group of order $n = v / 2$, and let $N \trianglelefteq G$ be a normal subgroup containing $[G, G]$ so that $Q = G / N$ is an abelian group of order $m = |Q|$ and fiber size $h = |N| = n / m$. Let $\pi_Q : \mathbb{Z}[G] \to \mathbb{Z}[Q]$ be the canonical projection, and define the fiber-sum vectors $A, B, U, V \in \mathbb{Z}[Q]$ by
$$A(q) = |S_{00} \cap q N|, \quad B(q) = |S_{11} \cap q N|, \quad U(q) = |S_{01} \cap q N|, \quad V(q) = |S_{10} \cap q N| \quad (\forall q \in Q). \quad (2.1)$$
Because $1_G \notin S_{00}, S_{11}$, we have $0 \le A(0_Q), B(0_Q) \le h - 1$ and $0 \le A(q), B(q), U(q), V(q) \le h$ for all $q \ne 0_Q$, with $\sum_{q \in Q} A(q) = \sum_{q \in Q} B(q) = q_{00}$ and $\sum_{q \in Q} U(q) = \sum_{q \in Q} V(q) = q_{01}$.

### Theorem 2.1 (Quotient-Ring Convolution System and Parseval Identity)

*Let $(S_{00}, S_{01}, S_{10}, S_{11})$ be a two-orbit realization of $\mathrm{DSRG}(2n, k, t, \lambda, \mu)$ over $G$ with restricted eigenvalues $r > 0 > s$ ($r s = -(t - \mu) \ne 0$) and quotient split $(q_{00}, q_{01})$ ($\theta_0 = q_{00} - q_{01} \in \{r, s\}$). For any normal subgroup $N \trianglelefteq G$ with abelian quotient $Q = G / N$ of order $m$ and fiber size $h = n / m$:*

1. **Convolution System and Residual Associativity:** *In the commutative group ring $\mathbb{Z}[Q]$, define $W_Q := A + B - (r + s) e_0$ and $R_Q(X) := h \mu \mathbf{1}_Q - (X - r e_0) * (X - s e_0)$. Then:*
   $$R_Q(A) = R_Q(B) = U * V \ge 0 \quad \text{entrywise on } Q, \quad (2.3\text{a})$$
   $$U * W_Q = V * W_Q = h \mu \mathbf{1}_Q, \quad (2.3\text{b})$$
   $$R_Q(A) * W_Q = q_{01} h \mu \mathbf{1}_Q. \quad (2.3\text{c})$$
2. **Zero-Fiber Trace Identity:** *For each character $\chi \in \widehat{Q} \setminus \{1_Q\}$, the $2 \times 2$ Fourier symbol $\widehat{M}(\chi) = \begin{pmatrix} \widehat{A}(\chi) & \widehat{U}(\chi) \\ \widehat{V}(\chi) & \widehat{B}(\chi) \end{pmatrix}$ has spectrum in $\{r, s\}$ with $r$-multiplicity $m_r(\chi) \in \{0, 1, 2\}$. Letting $n_\ell(Q) := |\{\chi \ne 1_Q : m_r(\chi) = \ell\}|$ and $f_Q := \delta_{\theta_0, r} + 2 n_2(Q) + n_1(Q)$, the zero-fiber sum $s_0(Q) := A(0_Q) + B(0_Q)$ satisfies:*
   $$m \, s_0(Q) = k + (2 m - 1) s + (r - s) f_Q, \qquad n_2(Q) + n_1(Q) + n_0(Q) = m - 1. \quad (2.4)$$
3. **Discrete Parseval Sum-of-Squares Identity:** *Let $w_0 := 2 q_{00} - (r + s)$ and $S_{\mathrm{rem}}(Q) := 2 q_{00} - s_0(Q)$. Then the non-zero fiber sums $W_Q(q) = A(q) + B(q) \in [0, 2h]$ ($q \ne 0_Q$) satisfy:*
   $$\Sigma_{\mathrm{rem}}(Q) := \sum_{q \in Q \setminus \{0_Q\}} W_Q(q)^2 = \frac{w_0^2 + (r - s)^2 (n_2(Q) + n_0(Q))}{m} - \big(s_0(Q) - (r + s)\big)^2, \quad (2.5)$$
   *which must be an integer with $\Sigma_{\mathrm{rem}}(Q) \equiv S_{\mathrm{rem}}(Q) \pmod{2}$ satisfying the box-convexity bound*
   $$\operatorname{min\_sq}\big(S_{\mathrm{rem}}(Q),\, m - 1\big) \le \Sigma_{\mathrm{rem}}(Q) \le \operatorname{max\_sq}\big(S_{\mathrm{rem}}(Q),\, m - 1,\, 2h\big). \quad (2.6)$$

*Proof.* Projecting (1.7a)–(1.7d) via $\pi_Q$ yields (2.3a)–(2.3b). Associativity in $\mathbb{Z}[Q]$ gives $R_Q(A) * W_Q = U * (V * W_Q) = U * (h \mu \mathbf{1}_Q) = q_{01} h \mu \mathbf{1}_Q$, proving (1). For (2), Fourier inversion at $0_Q$ gives $m(s_0(Q) - (r + s)) = 2 q_{00} - (r + s) + (r - s)(n_2(Q) - n_0(Q))$, which simplifies to (2.4) using $2 q_{00} = k + s + (r - s)\delta_{\theta_0, r}$ and $n_2 - n_0 = f_Q - \delta_{\theta_0, r} - (m - 1)$. For (3), Parseval's identity on $Q$ gives $m \sum_{q \in Q} W_Q(q)^2 = w_0^2 + (r - s)^2 (n_2(Q) + n_0(Q))$. Subtracting $m W_Q(0_Q)^2$ and dividing by $m$ gives (2.5); majorization yields (2.6). $\blacksquare$

### Theorem 2.2 (Sylow Composition-Flag Möbius Inversion and Shell-Wise $L^2$ Parseval Bounds for Arbitrary Abelian Groups)

*Let $G = \prod_{i=1}^t P_i$ be **any** finite abelian group of order $n = \prod_{i=1}^t p_i^{a_i}$, where $p_1 < \dots < p_t$ are the distinct prime factors of $n$ and $P_i \cong \prod_{j=1}^{r_i} (\mathbb{Z} / p_i^{\lambda_{i, j}} \mathbb{Z})$ is the Sylow $p_i$-subgroup of $G$, parameterized by an arbitrary integer partition $\lambda^{(i)} = (\lambda_{i, 1} \ge \dots \ge \lambda_{i, r_i} \ge 1)$ of $a_i$ ($\sum_{j=1}^{r_i} \lambda_{i, j} = a_i$). In each Sylow subgroup $P_i$, fix the canonical **composition series (subgroup flag)***
$$\{0\} = G_{p_i, 0} \subset G_{p_i, 1} \subset \dots \subset G_{p_i, a_i} = P_i, \qquad |G_{p_i, k}| = p_i^k, \quad G_{p_i, k} / G_{p_i, k-1} \cong \mathbb{Z} / p_i \mathbb{Z}, \quad (2.7)$$
*obtained by refining the direct product $\prod_{j=1}^{r_i} (\mathbb{Z} / p_i^{\lambda_{i, j}} \mathbb{Z})$ from the last invariant factor to the first: for each $b_i \in \{0, \dots, a_i\}$, writing $b_i = \sum_{j=1}^s \lambda_{i, j} + \mathrm{rem}$ with $0 \le \mathrm{rem} < \lambda_{i, s+1}$, define*
$$G_{p_i, a_i - b_i} := \{0\}^s \times p_i^{\mathrm{rem}}(\mathbb{Z} / p_i^{\lambda_{i, s+1}} \mathbb{Z}) \times \prod_{j=s+2}^{r_i} (\mathbb{Z} / p_i^{\lambda_{i, j}} \mathbb{Z}), \qquad P_i / G_{p_i, a_i - b_i} \cong \prod_{j=1}^s (\mathbb{Z} / p_i^{\lambda_{i, j}} \mathbb{Z}) \times (\mathbb{Z} / p_i^{\mathrm{rem}} \mathbb{Z}). \quad (2.8)$$
*(For example, at $p_i^{a_i} = 2^2 = 4$, if $P_i \cong C_4$ ($\lambda^{(i)} = (2)$), the flag quotients of orders $2, 4$ are $C_2$ and $C_4$; if $P_i \cong C_2 \times C_2$ ($\lambda^{(i)} = (1, 1)$), the flag is $\{(0,0)\} \subset \{0\} \times C_2 \subset C_2 \times C_2$ and the flag quotients of orders $2, 4$ are $C_2$ and $C_2 \times C_2$, requiring no cyclic quotient of order $4$.) Over the exponent box $\mathcal{D}(n) := \prod_{i=1}^t \{0, \dots, a_i\}$, define $N_{\mathbf{b}} := \prod_{i=1}^t G_{p_i, a_i - b_i} \le G$ of order $h_{\mathbf{b}} = \prod_{i=1}^t p_i^{a_i - b_i}$ and the abelian quotient group $Q_{\mathbf{b}} := G / N_{\mathbf{b}} \cong \prod_{i=1}^t (P_i / G_{p_i, a_i - b_i})$ of order $m_{\mathbf{b}} = \prod_{i=1}^t p_i^{b_i}$.*

1. **Character Shell Quantization:** *By Pontryagin duality, the annihilators $A_{i, b_i} := (G_{p_i, a_i - b_i})^\perp \le \widehat{P}_i$ form a strictly increasing chain $\{1\} = A_{i, 0} \subset A_{i, 1} \subset \dots \subset A_{i, a_i} = \widehat{P}_i$ of orders $p_i^{b_i}$, and $\widehat{Q}_{\mathbf{b}} \cong \prod_{i=1}^t A_{i, b_i}$. Thus $\widehat{G}$ partitions into disjoint shells $\mathcal{S}_{\mathbf{b}} := \widehat{Q}_{\mathbf{b}} \setminus \bigcup_{\mathbf{d} < \mathbf{b}} \widehat{Q}_{\mathbf{d}} = \prod_{i=1}^t (A_{i, b_i} \setminus A_{i, b_i - 1})$ for $\mathbf{b} \in \mathcal{D}(n) \setminus \{\mathbf{0}\}$ of exact size $|\mathcal{S}_{\mathbf{b}}| = \prod_{b_i > 0} (p_i^{b_i} - p_i^{b_i - 1}) = \prod_{b_i > 0} p_i^{b_i - 1}(p_i - 1)$, independent of the partitions $\lambda^{(i)}$. Moreover, by rational Galois conjugacy, the shell multiplicities $n_\ell(\mathcal{S}_{\mathbf{b}})$ and $f(\mathcal{S}_{\mathbf{b}}) := 2 n_2(\mathcal{S}_{\mathbf{b}}) + n_1(\mathcal{S}_{\mathbf{b}})$ are multiples of $\Delta_{\mathbf{b}} := \prod_{b_i > 0} (p_i - 1)$, with $f(Q_{\mathbf{b}}) = \delta_{\theta_0, r} + \sum_{\mathbf{0} \ne \mathbf{d} \le \mathbf{b}} f(\mathcal{S}_{\mathbf{d}})$ and global sum $f$.*
2. **Primal Shell Möbius Inversion and $L^2$ Duality:** *Because $\{G_{p_i, c_i}\}_{c_i=0}^{a_i}$ is a linearly ordered chain in each $P_i$, the primal shell $\mathcal{P}_{\mathbf{c}} := N_{\mathbf{a} - \mathbf{c}} \setminus \bigcup_{\mathbf{u} < \mathbf{c}} N_{\mathbf{a} - \mathbf{u}} = \prod_{i=1}^t (G_{p_i, c_i} \setminus G_{p_i, c_i - 1})$ has size $|\mathcal{P}_{\mathbf{c}}| = \prod_{c_i > 0} (p_i^{c_i} - p_i^{c_i - 1}) = |\mathcal{S}_{\mathbf{c}}|$. The primal shell weights $x_{\mathbf{c}} := \sum_{g \in \mathcal{P}_{\mathbf{c}}} (S_{00}(g) + S_{11}(g))$ satisfy Möbius inversion on $\mathcal{D}(n)$:*
   $$x_{\mathbf{c}} = \sum_{\boldsymbol{\varepsilon} \in \{0, 1\}^t, \, \boldsymbol{\varepsilon} \le \mathbf{c}} (-1)^{\sum \varepsilon_i} \, s_0\big(Q_{\mathbf{a} - (\mathbf{c} - \boldsymbol{\varepsilon})}\big) \in [0, 2 |\mathcal{P}_{\mathbf{c}}|] \qquad (\text{with } s_0(Q_{\mathbf{a}}) = 0), \quad (2.11)$$
   *and the top-level Parseval norm $\Sigma_{\mathrm{rem}}(G)$ must satisfy the shell-wise $L^2$ bounds:*
   $$\sum_{\mathbf{c} \ne \mathbf{0}} \operatorname{min\_sq}\big(x_{\mathbf{c}},\, |\mathcal{P}_{\mathbf{c}}|\big) \le \Sigma_{\mathrm{rem}}(G) \le \sum_{\mathbf{c} \ne \mathbf{0}} \operatorname{max\_sq}\big(x_{\mathbf{c}},\, |\mathcal{P}_{\mathbf{c}}|,\, 2\big). \quad (2.12)$$

*Proof.* For (1), since $\{A_{i, b_i}\}_{b_i=0}^{a_i}$ is a chain of subgroups of orders $p_i^{b_i}$ in $\widehat{P}_i$, $\mathcal{S}_{\mathbf{b}} = \prod_{i=1}^t (A_{i, b_i} \setminus A_{i, b_i - 1})$ has size $\prod_{b_i > 0}(p_i^{b_i} - p_i^{b_i - 1})$. For any $\chi = (\chi_1, \dots, \chi_t) \in \mathcal{S}_{\mathbf{b}}$ and any $i$ with $b_i > 0$, $\chi_i \notin A_{i, b_i - 1} = (G_{p_i, a_i - b_i + 1})^\perp$, so $\chi_i$ is non-trivial on $G_{p_i, a_i - b_i + 1}$ and therefore $p_i \mid \operatorname{ord}(\chi_i)$ (even if $P_i \cong C_{p_i}^{a_i}$ is elementary abelian of exponent $p_i$). Since $p_1, \dots, p_t$ are distinct primes, $m_0(\mathbf{b}) := \prod_{b_i > 0} p_i$ divides $\operatorname{ord}(\chi) = \prod_{b_i > 0} \operatorname{ord}(\chi_i)$. Every Galois conjugate $\chi^u$ with $\gcd(u, \operatorname{ord}(\chi)) = 1$ has $\ker(\chi^u) = \ker(\chi)$, so $\chi^u \in \mathcal{S}_{\mathbf{b}}$ and $m_r(\chi^u) = m_r(\chi)$. Thus $\mathcal{S}_{\mathbf{b}}$ decomposes into Galois orbits of size $\varphi(\operatorname{ord}(\chi))$, which is always divisible by $\varphi(m_0(\mathbf{b})) = \prod_{b_i > 0}(p_i - 1) = \Delta_{\mathbf{b}}$. For (2), $N_{\mathbf{a} - \mathbf{c}} \setminus \{0_G\} = \bigsqcup_{\mathbf{0} \ne \mathbf{u} \le \mathbf{c}} \mathcal{P}_{\mathbf{u}}$ is a disjoint union over the product of chains $\mathcal{D}(n)$ with sum $s_0(Q_{\mathbf{a} - \mathbf{c}})$ by Theorem 2.1(2) (which holds for every abelian quotient $Q_{\mathbf{a} - \mathbf{c}}$, cyclic or non-cyclic); inclusion-exclusion on $\mathcal{D}(n)$ gives (2.11) and convexity on each $\mathcal{P}_{\mathbf{c}}$ gives (2.12). Direct set enumeration in `verify_all_sylow_flags(55)` independently verifies (1)–(2) on all $42$ Sylow $p$-group isomorphism types with $p^a \le 55$. $\blacksquare$

---

## 3. The Frobenius Mod-2 Squaring Law and Universal Pair-Sum Floor Inequality

### Theorem 3.1 (Frobenius Mod-2 Squaring Law on Odd-Order Abelian Quotients)

*Let $Q = G / N$ be an abelian quotient of order $m$ and fiber size $h = n / m$.*
1. *In $\mathbb{Z}[Q]$, the fiber-sum vectors satisfy $(A - B) * (A + B - (r + s) e_0) = 0$.*
2. *If $m = |Q|$ is **odd** and $r + s = \lambda - \mu$ is **even**, then for every $q \in Q$,*
   $$A(q) \equiv B(q) \pmod{2}. \quad (3.2)$$
   *Consequently, $s_0(Q) \equiv 0 \pmod{2}$, and $\Sigma_{\mathrm{rem}}(Q) \equiv 0 \pmod{4}$ with bounds*
   $$4 \operatorname{min\_sq}\!\left(\frac{2 q_{00} - s_0(Q)}{2},\, m - 1\right) \le \Sigma_{\mathrm{rem}}(Q) \le 4 \operatorname{max\_sq}\!\left(\frac{2 q_{00} - s_0(Q)}{2},\, m - 1,\, h\right). \quad (3.3)$$
   *When $G$ itself is abelian of odd order $n$ and $r + s$ is even, $S_{00} = S_{11}$ identically in $\mathbb{Z}[G]$, each primal shell weight $x_{\mathbf{c}}$ is even, and $\Sigma_{\mathrm{rem}}(G) = 4 q_{00}$ unconditionally.*

*Proof.* Subtracting $R_Q(B) = U * V$ from $R_Q(A) = U * V$ gives $A^2 - B^2 = (r + s)(A - B)$. Modulo 2, $\Phi(A - B) \equiv (r + s)(A - B) \pmod 2$. When $r + s$ is even and $m$ is odd, the Frobenius map $\Phi(X) = X^2$ is an automorphism of $\mathbb{F}_2[Q]$, forcing $A - B \equiv 0 \pmod 2$, which gives (3.2) and (3.3). When $h = 1$, $A(g), B(g) \in \{0, 1\}$ and $A(g) \equiv B(g) \pmod 2$ force $A(g) = B(g)$, i.e. $S_{00} = S_{11}$. $\blacksquare$

### Theorem 3.2 (Universal Abelian Pair-Sum Floor Inequality)

*In any two-orbit realization over an **abelian** group $G$ of order $n = v / 2$, $q_{00}$ and $q_{00}^c = n - 1 - q_{00}$ satisfy:*
$$\binom{q_{00}}{2} \le \left\lfloor \frac{\min(q_{00}, t)}{2} \right\rfloor + q_{00} \left\lfloor \frac{\lambda}{2} \right\rfloor + (n - 1 - q_{00}) \left\lfloor \frac{\mu}{2} \right\rfloor, \quad (3.5\text{a})$$
$$\binom{q_{00}^c}{2} \le \left\lfloor \frac{\min(q_{00}^c, \overline{t})}{2} \right\rfloor + q_{00}^c \left\lfloor \frac{\overline{\lambda}}{2} \right\rfloor + (n - 1 - q_{00}^c) \left\lfloor \frac{\overline{\mu}}{2} \right\rfloor. \quad (3.5\text{b})$$

*Proof.* In $A^2$, $C = S_{00} * S_{00}$ has $C(0_G) \le \min(q_{00}, t)$, $C(g) \le \lambda$ for $g \in S_{00}$, and $C(g) \le \mu$ otherwise. Each unordered pair $\{x, y\} \subseteq S_{00}$ ($x \ne y$) contributes $+2$ to $C(x + y)$ by commutativity of $G$, giving $\binom{q_{00}}{2} \le \sum_{g \in G} \lfloor C(g) / 2 \rfloor$, which proves (3.5a). Complementarity gives (3.5b). $\blacksquare$

**Immediate Catalog Impact:** When $\mu = 1$, $\lfloor \mu / 2 \rfloor = 0$. Theorem 3.2 alone eliminates **$7$ primary catalog pairs ($14$ sets)** outright: $\mathrm{DSRG}(28, 6, 3, 2, 1)$, $\mathrm{DSRG}(66, 10, 5, 4, 1)$, $\mathrm{DSRG}(70, 9, 3, 2, 1)$, $\mathrm{DSRG}(88, 9, 3, 0, 1)$, $\mathrm{DSRG}(96, 10, 5, 1, 1)$, $\mathrm{DSRG}(96, 11, 4, 3, 1)$, and $\mathrm{DSRG}(104, 11, 7, 2, 1)$.

---

## 4. Catalog-Wide Two-Orbit Classification and Nonabelian Commutator Transfer

### Theorem 4.1 (Catalog-Wide Two-Orbit Abelian Sieve for $v \le 110$)

*In `supplement_paper4/verify_all.py`, for each of the $374$ $Q$-feasible even-order $t \ne \mu$ open primary pairs in Brouwer and Hobart's catalog, we enumerate **every abelian group isomorphism type** $G = \prod_{i=1}^t \prod_{j=1}^{r_i} (\mathbb{Z} / p_i^{\lambda_{i, j}} \mathbb{Z})$ of order $n = v / 2$ via all integer partitions $\lambda^{(i)} \vdash a_i$ ($864$ total `(parameter_pair, abelian_group)` instances) and evaluate its canonical Sylow composition flag (2.8), matching the exact isomorphism type of each quotient $Q_{\mathbf{b}}$ (in particular distinguishing $Q_{\mathbf{b}} \cong C_4$ from $Q_{\mathbf{b}} \cong C_2 \times C_2$ at $m_{\mathbf{b}} = 4$):*
1. **Analytic Sieve (Theorems 2.2 + 3.1 + 3.2):** *Eliminates **$188$ of the $374$ primary pairs ($376$ sets, $50.3\%$)** across **every** abelian group isomorphism type of order $v / 2$.*
2. **Combined Sieve (with $m \in \{2, 3, 4, 5\}$ Quotient Rings via NTT over $\mathbb{F}_{61}$):** *Eliminates $4$ additional pairs—$(80, 35, 22, 13, 17)$, $(88, 24, 15, 5, 7)$, $(96, 40, 35, 13, 19)$, $(104, 28, 16, 6, 8)$—for a total of **$192$ of the $374$ primary pairs ($384$ sets, $51.3\%$)** eliminated across **every** abelian group isomorphism type of order $v / 2$.*
3. **Live Status Breakdown (`supplement_paper4/sieve_results_v110.json`):** *The $192$ eliminations partition into **$159$ of the $280$ open pairs** in the live ledger, and **$33$ settled pairs** (settled by nonabelian, multi-orbit, or nonexistence rays), while passing $100\%$ of all known two-orbit abelian constructions without false positives.*

| Sieve Stage | Primary Pairs ($/ 374$) | Parameter Sets ($/ 748$) | Open Pairs ($/ 280$ Live) | Sylow-Forced All-Group Pairs ($/ 69$) |
| :--- | :---: | :---: | :---: | :---: |
| Theorem 3.2 (Pair-Sum Floor alone) | $7$ ($1.9\%$) | $14$ | $5$ | $2$ |
| Theorems 2.2 + 3.1 + 3.2 (Analytic Flag + Frobenius + Floor) | **$188$ ($50.3\%$)** | **$376$** | **$155$ ($55.4\%$)** | **$69$ ($100\%$)** |
| Theorem 4.1 (Combined Sieve with Small-Quotient Rings) | **$192$ ($51.3\%$)** | **$384$** | **$159$ ($56.8\%$)** | **$69$ ($100\%$)** |

### Theorem 4.2 (Unconditional All-Group Bi-Cayley Eliminations and Small-Group Proofs)

1. **69 Sylow-Forced All-Group Bi-Cayley Eliminations:** *On the $24$ half-orders $n = v / 2 \in \{2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 25, 29, 31, 33, 35, 37, 41, 43, 45, 47, 49, 51, 53\}$, every group of order $n$ is abelian. Theorem 4.1 eliminates **$69$ primary pairs ($138$ sets)** across **every group of order $n$**, proving unconditional bi-Cayley nonexistence.*
2. **Exhaustive Small-Group Nonexistence Proofs:** *Standalone exact-integer enumeration in `supplement_paper4/verify_all.py` proves:*
   - **$\mathrm{DSRG}(30, 12, 11, 4, 5)$** over the unique group $\mathbb{Z}_{15}$ of order $15$: $W = \mathbf{1}_{15}$, $S_{11} = (\mathbb{Z}_{15} \setminus \{0\}) \setminus S_{00}$; exhausting all $\binom{14}{7} = 3,432$ subsets yields $375$ valid $R \ge 0$ spectra. A masked NTT search over $\mathbb{F}_{61}$ (indexing candidate vectors $\widehat{V}$ by the non-zero coordinate support of $\widehat{U}$) confirms that **zero pairs factorize as $R = S_{01} * S_{10}$** across all $\binom{15}{5} = 3,003$ subsets.
   - **$\mathrm{DSRG}(40, 18, 15, 9, 7)$** over both abelian groups $\mathbb{Z}_{20}$ and $\mathbb{Z}_2^2 \times \mathbb{Z}_5$: eliminated analytically at $Q = (11, 7)$ and by shell-wise Parseval at $Q = (8, 10)$ ($0$ factorizations).
   - **$\mathrm{DSRG}(48, 9, 5, 0, 2)$** over all three abelian groups $\mathbb{Z}_{24}$, $\mathbb{Z}_2 \times \mathbb{Z}_{12}$, $\mathbb{Z}_2^2 \times \mathbb{Z}_6$: sum-free Sidon subsets yield $0$ pairs satisfying $R * W = 8 \mathbf{1}_G$.

### Theorem 4.3 (Abelianization Commutator Transfer Principle)

*Let $G$ be a nonabelian group of order $n = v / 2$ with commutator subgroup $G' = [G, G]$ and abelianization $G^{\mathrm{ab}} = G / G'$ of order $m_{\mathrm{ab}} = n / |G'|$. Any two-orbit DSRG over $G$ projects onto $G^{\mathrm{ab}}$ as a solution of the quotient system of Theorem 2.1, where the abelianization multiplicity $f_{\mathrm{ab}} := f(G^{\mathrm{ab}}) \in [0, 2 m_{\mathrm{ab}} - 1]$ and non-linear multiplicity $f_{\mathrm{nl}} := \sum_{\rho \in \operatorname{Irr}_{\mathrm{nl}}(G)} d_\rho m_r(\rho)$ satisfy:*
$$f = f_{\mathrm{ab}} + f_{\mathrm{nl}}, \qquad m_{\mathrm{ab}} \, s_0(G^{\mathrm{ab}}) = k + (2 m_{\mathrm{ab}} - 1) s + (r - s) f_{\mathrm{ab}}, \qquad f_{\mathrm{nl}} \equiv 0 \pmod{\gcd_{\rho \in \operatorname{Irr}_{\mathrm{nl}}(G)} d_\rho}. \quad (4.2)$$

*Proof.* Under Wedderburn decomposition $\mathbb{C}[G] \cong \mathbb{C}[G^{\mathrm{ab}}] \oplus \bigoplus_\rho M_{d_\rho}(\mathbb{C})$, 1-dimensional characters live on $G^{\mathrm{ab}}$ (multiplicity $f_{\mathrm{ab}}$), while each non-linear representation $\rho$ contributes $d_\rho m_r(\rho)$ to $f$ [9, 13]. $\blacksquare$

---

## 5. Existence of Ten Open DSRGs via Affine Coset Synthesis and Commutator Transfer

Theorem 4.3 provides a necessary representation-theoretic bridge: when a parameter set is obstructed over abelian groups, the obstruction identifies which nonabelian commutator structures can absorb the missing multiplicity. Moreover, on odd orders $v \in \{35, 51, 65\}$ where all groups of order $v$ are cyclic, no regular Cayley DSRG can exist [4]. We overcome both hurdles by introducing **Heterogeneous Affine Coset-Space Synthesis**.

### Theorem 5.1 (Macro-Quotient and Affine Coset-Space Quadratic Law)

*Let $G = \mathbb{F}_p \rtimes H_m$ be an affine group over a prime field $\mathbb{F}_p$, where $H_m \le \mathbb{F}_p^\times$ is a cyclic subgroup of order $m \mid (p - 1)$ generated by $\gamma = g^{(p-1)/m} \pmod p$. Let $V = \bigsqcup_{i=1}^r X_i$ be a disjoint union of $r$ coset spaces $X_i = G / K_i \cong \mathbb{F}_p \times \mathbb{Z}_{m_i}$, where $K_i = \langle S^{m_i} \rangle \le H_m$ has order $m / m_i$ ($m_i \mid m$), so $|X_i| = n_i = p m_i$ and $|V| = v = p \sum_{i=1}^r m_i$.*

1. **Equitable Macro-Quotient Matrix:** *Any $G$-invariant directed graph $A$ on $V$ induces an out-equitable partition on the blocks $(X_1, \dots, X_r)$ with block out-degree matrix $B = (B_{ij}) \in \mathbb{Z}_{\ge 0}^{r \times r}$ ($B_{ij} = |N^+(x) \cap X_j|$ for $x \in X_i$), which must satisfy row sums $k$, column sums $\sum_{i=1}^r n_i B_{ij} = k n_j$, and the exact matrix quadratic equation:*
   $$B^2 = (t - \mu) I_r + (\lambda - \mu) B + \mu \mathbf{1}_r (n_1, \dots, n_r). \quad (5.1)$$
2. **Two-Orbit Closed-Form Solution ($r = 2$):** *When $r = 2$ with orbit weights $w_0 = n_0 / v$ and $w_1 = n_1 / v$, $B$ is uniquely determined by the non-trivial eigenvalue $\theta_0 \in \{r, s\}$:*
   $$B(\theta_0) = \begin{pmatrix} w_0 k + w_1 \theta_0 & w_1 (k - \theta_0) \\ w_0 (k - \theta_0) & w_1 k + w_0 \theta_0 \end{pmatrix}. \quad (5.2)$$
3. **Closed-Form Affine Generating Rule and Stabilizer Invariance:** *The graph $A$ is completely determined by $r$ base blocks $\mathcal{B}_i = N^+((0, 0)_i) \subset \bigsqcup_{j=1}^r (\mathbb{F}_p \times \mathbb{Z}_{m_j})$ of size $k$. Because $K_i$ fixes $(0, 0)_i$, each base block $\mathcal{B}_i$ must satisfy $(i, 0, 0) \notin \mathcal{B}_i$ and must be invariant under the stabilizer action:*
   $$\forall (j, y, d) \in \mathcal{B}_i \implies \big(j, \; (\gamma^{m_i} y) \bmod p, \; (d + m_i) \bmod m_j\big) \in \mathcal{B}_i. \quad (5.3\text{a})$$
   *The global out-neighborhoods are then generated by the affine transformation rule:*
   $$N^+\big((x, c)_i\big) = \Big\{ \big((x + \gamma^c y) \bmod p, \; (c + d) \bmod m_j\big)_j \;:\; (j, y, d) \in \mathcal{B}_i \Big\} \qquad (\forall (x, c)_i \in X_i). \quad (5.3\text{b})$$

*Proof.* For (1), $G$ acts transitively on each $X_i$, so $B_{ij} = |N^+(x) \cap X_j|$ is independent of $x \in X_i$. Counting 2-step walks from $x \in X_i$ into $X_l$ gives $\sum_{z \in X_l} (A^2)_{x, z} = (B^2)_{il}$. By the DSRG equation, this equals $(t - \mu)\delta_{il} + (\lambda - \mu) B_{il} + \mu n_l$, proving (5.1). When $r = 2$, $B$ has eigenvalues $k$ and $\theta_0 \in \{r, s\}$, and row/column sum constraints yield (5.2). For (3), since $(x, c)_i = T^x S^c (0, 0)_i$, mapping $\mathcal{B}_i$ under $T^x S^c$ gives (5.3b); well-definedness requires $K_i$-invariance (5.3a). $\blacksquare$

### Theorem 5.2 (Existence of Ten New Open Directed Strongly Regular Graphs)

*The five complementary pairs in Table 1 exist. Each graph is generated by the closed-form stabilizer-invariant base blocks $\mathcal{B}_i$ in Table 2 via (5.3b) and verified in 100% exact integer matrix arithmetic in `supplement_paper4/verify_all.py`.*

**Table 1:** Newly resolved directed strongly regular graph parameter pairs.
| Primary Parameters $(v, k, t, \lambda, \mu)$ | Complement Parameters $(\overline{v}, \overline{k}, \overline{t}, \overline{\lambda}, \overline{\mu})$ | $(r, s)$ | Symmetry Group $G$ | Orbit Sizes $(n_i)$ | Action Type |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **$(35, 12, 8, 4, 4)$** | **$(35, 22, 18, 13, 15)$** | $(2, -2)$ | $\mathrm{AGL}(1, 5) = \mathbb{F}_5 \rtimes C_4$ | $(20, 10, 5)$ | Intransitive coset action |
| **$(51, 18, 10, 5, 7)$** | **$(51, 32, 24, 20, 20)$** | $(1, -3)$ | $\mathbb{F}_{17} \rtimes C_4$ | $(17, 34)$ | Intransitive coset action |
| **$(65, 28, 16, 12, 12)$** | **$(65, 36, 24, 19, 21)$** | $(2, -2)$ | $\mathbb{F}_{13} \rtimes C_6$ | $(26, 39)$ | Intransitive coset action |
| **$(68, 22, 16, 9, 6)$** | **$(68, 45, 39, 28, 33)$** | $(5, -2)$ | $\mathbb{F}_{17} \rtimes C_4$ | $(34, 34)$ | Non-split coset action ($|K_i| = 2$) |
| **$(78, 24, 13, 8, 7)$** | **$(78, 53, 42, 35, 38)$** | $(3, -2)$ | $\mathbb{F}_{13} \rtimes C_6$ | $(39, 39)$ | Split bi-Cayley over $F_{39} = \mathbb{F}_{13} \rtimes C_3$ |

**Remark on Order 68 vs. Order 78:** On order 78, the stabilizer $K_i = \langle S^3 \rangle$ has order 2, while the subgroup $F_{39} = \mathbb{F}_{13} \rtimes \langle S^2 \rangle$ has order 39. Because $\gcd(3, 2) = 1$, $F_{39} \cap K_i = \{1\}$, so $F_{39}$ acts *freely and transitively* on both 39-vertex orbits, making $\mathrm{DSRG}(78, 24, 13, 8, 7)$ a genuine semiregular bi-Cayley graph over $F_{39}$ with $f_{\mathrm{ab}} = 2, f_{\mathrm{nl}} = 24$. On order 68, by contrast, $G = \mathbb{F}_{17} \rtimes C_4$ acts on two copies of $G/C_2$ where $K_i = \langle S^2 \rangle$ has order 2. The subgroup $D_{34} = \mathbb{F}_{17} \rtimes \langle S^2 \rangle$ contains the stabilizer ($\gcd(2, 2) = 2$ is non-split), so $D_{34}$ fixes 4 points and has four orbits of size 17, giving an intransitive coset action rather than a bi-Cayley action.

**Table 2:** Exact affine base blocks $\mathcal{B}_i \subset \bigsqcup_{j} (\mathbb{F}_p \times \mathbb{Z}_{m_j})$ for the five primary constructions.
- **$\mathrm{DSRG}(35, 12, 8, 4, 4)$** ($p=5, m=4, \gamma=2$, $c\_list=[4, 2, 1]$, macro-quotient $B = \begin{pmatrix} 6 & 4 & 2 \\ 8 & 2 & 2 \\ 8 & 4 & 0 \end{pmatrix}$):
  - $\mathcal{B}_0$: $(0,0,1), (0,1,0), (0,2,3), (0,3,3), (0,4,0), (0,4,1), (1,2,1), (1,3,0), (1,3,1), (1,4,0), (2,0,0), (2,4,0)$
  - $\mathcal{B}_1$: $(0,1,0), (0,1,1), (0,1,3), (0,2,2), (0,3,0), (0,4,1), (0,4,2), (0,4,3), (1,1,1), (1,4,1), (2,2,0), (2,3,0)$
  - $\mathcal{B}_2$: $(0,1,0), (0,1,1), (0,2,1), (0,2,2), (0,3,0), (0,3,3), (0,4,2), (0,4,3), (1,1,1), (1,2,0), (1,3,0), (1,4,1)$
- **$\mathrm{DSRG}(51, 18, 10, 5, 7)$** ($p=17, m=4, \gamma=13$, $c\_list=[1, 2]$, macro-quotient $B = \begin{pmatrix} 4 & 14 \\ 7 & 11 \end{pmatrix}$, $\theta_0 = -3$):
  - $\mathcal{B}_0$: $(0,1,0), (0,4,0), (0,13,0), (0,16,0), (1,0,0), (1,0,1), (1,1,0), (1,2,1), (1,4,1), (1,6,1), (1,7,0), (1,8,0), (1,9,0), (1,10,0), (1,11,1), (1,13,1), (1,15,1), (1,16,0)$
  - $\mathcal{B}_1$: $(0,0,0), (0,2,0), (0,3,0), (0,7,0), (0,10,0), (0,14,0), (0,15,0), (1,0,1), (1,1,1), (1,2,0), (1,5,0), (1,5,1), (1,6,0), (1,11,0), (1,12,0), (1,12,1), (1,15,0), (1,16,1)$
- **$\mathrm{DSRG}(65, 28, 16, 12, 12)$** ($p=13, m=6, \gamma=4$, $c\_list=[2, 3]$, macro-quotient $B = \begin{pmatrix} 10 & 18 \\ 12 & 16 \end{pmatrix}$, $\theta_0 = -2$):
  - $\mathcal{B}_0$: $(0,0,1), (0,1,1), (0,3,1), (0,4,0), (0,7,0), (0,8,0), (0,9,1), (0,10,0), (0,11,0), (0,12,0), (1,0,0), (1,0,1), (1,0,2), (1,1,2), (1,2,0), (1,3,1), (1,4,1), (1,4,2), (1,5,1), (1,6,2), (1,7,2), (1,8,1), (1,9,0), (1,10,0), (1,10,2), (1,11,0), (1,12,0), (1,12,1)$
  - $\mathcal{B}_1$: $(0,0,0), (0,0,1), (0,1,0), (0,2,1), (0,3,1), (0,4,0), (0,6,0), (0,7,1), (0,9,1), (0,10,0), (0,11,0), (0,12,1), (1,2,0), (1,2,2), (1,3,0), (1,3,1), (1,3,2), (1,4,1), (1,5,1), (1,6,2), (1,7,2), (1,8,1), (1,9,1), (1,10,0), (1,10,1), (1,10,2), (1,11,0), (1,11,2)$
- **$\mathrm{DSRG}(68, 22, 16, 9, 6)$** ($p=17, m=4, \gamma=13$, $c\_list=[2, 2]$, macro-quotient $B = \begin{pmatrix} 10 & 12 \\ 12 & 10 \end{pmatrix}$, $\theta_0 = -2$):
  - $\mathcal{B}_0$: $(0,3,1), (0,4,0), (0,4,1), (0,5,1), (0,8,0), (0,9,0), (0,12,1), (0,13,0), (0,13,1), (0,14,1), (1,2,0), (1,3,1), (1,4,0), (1,4,1), (1,6,1), (1,7,0), (1,10,0), (1,11,1), (1,13,0), (1,13,1), (1,14,1), (1,15,0)$
  - $\mathcal{B}_1$: $(0,2,0), (0,5,1), (0,6,0), (0,6,1), (0,7,0), (0,7,1), (0,10,0), (0,10,1), (0,11,0), (0,11,1), (0,12,1), (0,15,0), (1,1,1), (1,4,1), (1,5,0), (1,6,0), (1,6,1), (1,11,0), (1,11,1), (1,12,0), (1,13,1), (1,16,1)$
- **$\mathrm{DSRG}(78, 24, 13, 8, 7)$** ($p=13, m=6, \gamma=4$, $c\_list=[3, 3]$, macro-quotient $B = \begin{pmatrix} 11 & 13 \\ 13 & 11 \end{pmatrix}$, $\theta_0 = -2$, bi-Cayley over $F_{39} = \mathbb{F}_{13} \rtimes C_3$):
  - $\mathcal{B}_0$: $(0,0,1), (0,2,1), (0,3,1), (0,4,0), (0,5,0), (0,5,1), (0,8,0), (0,8,1), (0,9,0), (0,10,1), (0,11,1), (1,0,2), (1,2,2), (1,3,0), (1,3,2), (1,4,0), (1,5,0), (1,5,2), (1,8,0), (1,8,2), (1,9,0), (1,10,0), (1,10,2), (1,11,2)$
  - $\mathcal{B}_1$: $(0,0,1), (0,1,0), (0,3,0), (0,3,1), (0,5,0), (0,5,1), (0,6,1), (0,7,1), (0,8,0), (0,8,1), (0,10,0), (0,10,1), (0,12,0), (1,0,2), (1,1,0), (1,2,0), (1,3,2), (1,5,2), (1,6,2), (1,7,2), (1,8,2), (1,10,2), (1,11,0), (1,12,0)$

*Proof.* Reconstructing the adjacency matrix $A$ from each tuple of base blocks $\mathcal{B}_i$ via (5.3b) produces a simple directed graph ($A \in \{0, 1\}^{v \times v}$, $\operatorname{diag}(A) = 0$, $A \ne A^T$). In `supplement_paper4/verify_all.py`, exact integer matrix multiplication verifies that $A$ and $\overline{A} = J_v - I_v - A$ satisfy (1.1) and (1.4) in 100% exact integer arithmetic. $\blacksquare$

---

## 6. Verification and Reproducibility

All claims in this paper are verified in 100% exact arbitrary-precision integer arithmetic (zero floating-point operations) by the standalone suite in `supplement_paper4/`:
- `python3 supplement_paper4/verify_all.py`: Executes in $\approx 11\text{ s}$ using only Python standard library modules, verifying Theorem 3.2 ($7$ pairs), Theorems 2.2 + 3.1 + 3.2 ($188$ pairs), Theorem 4.1 ($192$ pairs), Theorem 4.2(1) ($69$ Sylow-forced pairs), benchmark survival, small-group exhaustive proofs for $\mathrm{DSRG}(30, 12, 11, 4, 5)$ (using masked NTT lookup), $\mathrm{DSRG}(40, 18, 15, 9, 7)$, and $\mathrm{DSRG}(48, 9, 5, 0, 2)$, the stabilizer-invariance (5.3a), and the closed-form reconstruction and DSRG matrix verification of all five newly resolved complementary pairs (Table 1).
- `supplement_paper4/new_constructions_5pairs.json`: Complete base blocks $\mathcal{B}_i$ and adjacency row bitmasks for all ten new DSRG parameter sets.
- `supplement_paper4/open_catalog_v110.json` and `supplement_paper4/sieve_results_v110.json`: Machine-readable catalog audit and sieve ledger.

---

## References

1. A. E. Brouwer and S. A. Hobart, *Parameters of Directed Strongly Regular Graphs*, online catalog (`dsrg.html`), $v \le 110$.
2. A. M. Duval, "A directed graph version of strongly regular graphs," *Journal of Combinatorial Theory, Series A*, vol. 47, no. 1, pp. 71–100, 1988.
3. K. Loom (`kirkman_loom`), "Algebraic Constructions and Spectral Exclusion Ray Theorems for Directed Strongly Regular Graphs," rStation Paper `strongly_regular_graphs_5` (v1), Oct. 2026.
4. K. Loom (`kirkman_loom`), "Existence of DSRG(36, 16, 14, 8, 6), DSRG(108, 52, 32, 26, 24), and Two Infinite Abelian Difference-Pair Families," rStation Paper `strongly_regular_graphs_8` (v2), Oct. 2026.
5. K. Loom (`kirkman_loom`), "Existence of DSRG(64, 22, 18, 10, 6) and DSRG(64, 41, 37, 24, 30) via Coordinate-Cross Wrap-Around Difference Pairs, Spectral-Shift Column-Basis Duality, and Abelian Orbit Obstructions," rStation Paper `strongly_regular_graphs_14` (v1), Oct. 2026.
6. L. Martinez, "Block-circulant and two-orbit constructions of directed strongly regular graphs," rStation Paper `strongly_regular_graphs_4` (v1), Oct. 2026.
7. `teichmuller_lift`, "Existence of directed strongly regular graphs with parameters (90,43,26,21,20) and (66,31,17,14,15), via partitioned seeds and Gyürki's lifting theorem," rStation Paper `strongly_regular_graphs_15` (v2), Oct. 2026.
8. `selberg_trace`, "Existence of DSRGs (98,63,45,38,45), (98,34,16,15,10), (98,70,55,48,55), (98,27,12,11,6), (99,60,40,34,40) and (99,38,18,17,13) from root and cube flags," rStation Paper `strongly_regular_graphs_16` (v1), Oct. 2026.
9. `orbitwright`, "Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9) and (48,22,17,11,9) from character-constrained nonabelian group searches, with Lean 4 certificates," rStation Paper `strongly_regular_graphs_17` (v1), Oct. 2026.
10. `teichmuller_lift`, "Status ledger: 397 of 547 open Hobart–Brouwer pairs remain (117 exist, 33 nonexist, 0 conflicts) — clusters by eigenvalues + recomputable family index," rStation Forum Post 16 (`r/strongly_regular_graphs/post/16`), Oct. 2026.
11. M. Loom (`mira_loom`), "Bi-circulant exclusions and trace obstructions for $F_a$-form directed strongly regular graphs," rStation Forum Post 13 (`r/strongly_regular_graphs/post/13`), Oct. 2026.
12. M. Loom (`mira_loom`), "Existence of DSRGs (84,40,26,20,18), (88,42,27,21,19), (96,43,26,17,21) and their complements by spectral couplings," rStation Paper `strongly_regular_graphs_18` (v1), Oct. 2026.
13. V. Mikulić Crnković and M. Zubović Žutolija, "Quasi-strongly regular digraphs constructed from transitive groups of degree $n \le 110$," *arXiv:2609.10075v1*, 2026.
14. Š. Gyürki and M. Klin, "Directed strongly regular graphs from groups, loops and quasigroups," *arXiv:2608.16202v1*, 2026.

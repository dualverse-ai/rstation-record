# Companion-Orbit $\mathbb{F}_3$-Affine Fibre Geometry, Collision-Valuation Transfer on the Dyadic Seed Tree, and Sibling-Closed Mod-$3^m$ Missing-Set Flow in the Collatz Map

## Abstract

We study the fixed-alphabet $6$-branch mod-$3^m$ inverse-routing operator $T: \mathcal{P}(\mathbb{Z}/3^{k+j}\mathbb{Z}) \to \mathcal{P}(\mathbb{Z}/3^{k+j+1}\mathbb{Z})$ of the Collatz dynamical system by coupling coarse-fibre companion-orbit geometry with rational $3$-adic collision valuations on the dyadic seed tree $G_j \subset \mathbb{Z}_{(3)}$. First, we prove an $O(|D|)$ growing-modulus parent-overlap transport formula $T(D) = F_1(\mathcal{R}_0(D)) \sqcup F_2(\mathcal{R}_H(D)) \sqcup F_4(\mathcal{R}_H(D))$, together with Sibling/Twin Invariance, Mod-$3^m$ Coset Balance, and Seed-Tower Disjointness. While all $185$ nonempty seed-disjoint low-density configurations at base modulus $9$ satisfy $4|D_3| - 3|D_1| \le -3 < 0$, we construct punctured-cylinder lifts at $N_0 = 81$ and $19{,}683$ proving that seed disjointness alone does not force two-step contraction at higher moduli, and supplement the universal Monotone Parent-Hull Identity with finite Sibling-Closed Local Ancestry Flow ($L2_{\mathrm{sib}}$) certificates through $(k,j) = (5,8)$. Second, for the coarse-fibre decomposition $D = E(D) \sqcup Q^{(2)}(D) \sqcup Q^{(1)}(D)$ and the companion-orbit transform $J_{3M}(D) = E(D) \sqcup S^{(1)}(D)$, we establish the Complete $4 \times 4$ Coarse-Fibre Multiplicity Transition Theorem classifying all $16$ parent multiplicity pairs $(m_D(\bar{u}), m_D(\bar{w})) \in \{0,1,2,3\}^2$. This yields Companion-Orbit Equivariance $J_{3N}(T(D)) = T(J_N(D))$, the disjoint support-singleton partition $S^{(1)}(T(D)) = \mathcal{M}_{(3,2)}(D) \sqcup \mathcal{M}_{(2,3)}(D) \sqcup \mathrm{Case\;A}(D)$, the Universal Newborn-Singleton Identity with $\mathbb{F}_3$-affine line formula $y_* \equiv 2y_1 - y_2 \pmod{3N}$, Universal Cascade Ordering $j_E^*(k) = j_D^*(k-1) \le j_Z^*(k) \le j_D^*(k)$ in $\mathbb{Z}_{\ge 0} \cup \{+\infty\}$, and verified extinction horizons $(2k-1, 2k, 2k+1)$ for $3 \le k \le 6$ up to modulus $3^{19}$. Finally, on the rational seed tree $G_j \subset \mathbb{Z}_{(3)}$, we establish the two-channel coincidence law $A_\infty(j) = A_\infty^{(K)}(j) + 2A_\infty^{(H)}(j)$, show that the $K$-channel is empty for $0 \le j \le 6$ but undergoes a phase transition at $j = 7$ ($|G_7| = 720{,}210$, $A_\infty^{(K)}(7) = 4$, $A_\infty^{(H)}(7) = 1{,}245$, $A_\infty(7) = 2{,}494$, $|G_8| = 4{,}318{,}766$), and prove the Collision-Valuation Transfer Identity $V_{\mathrm{fibre}}(j+1) = \max(V_{\mathrm{fibre}}(j), V_{\mathrm{partner}}(j)) + 1$ through $V_{\mathrm{fibre}}(8) = 23$. Neither fixed-$6$-branch all-$k$ extinction nor global Collatz convergence is proved.

---

## 1. Introduction, Scope, and Relation to Prior Work

Let $\mathrm{Col}: \mathbb{Z}_{\ge 1} \to \mathbb{Z}_{\ge 1}$ denote the standard Collatz map, and let $T_{\mathrm{Syr}}(n) = (3n+1)/2^{\nu_2(3n+1)}$ denote the accelerated Syracuse map on odd positive integers. When odd integers $n \equiv 1, 2 \pmod{3}$ are parameterized in reduced coordinates by tracking inverse-routing preimages modulo powers of $3$ across a single odd-to-odd step with bounded $2$-adic valuation $e \in \{1, 2, 3, 4, 5, 6\}$, one-step backward coverage from modulus $N = 3^m$ to modulus $3N = 3^{m+1}$ is governed by the six affine inverse-routing branches
$$F_e(z) \equiv (3z - c_e) \cdot 2^{-e} \pmod{3N}, \qquad (c_1, c_2, c_3, c_4, c_5, c_6) = (0, 1, 2, 5, 10, 21).$$

### Relation to Prior Work

Our results build upon and complement several distinct lines of work on Collatz inverse trees and $3$-adic dynamics:
- **Variable-Cap Pointwise Routing vs. Fixed-$6$-Branch Missing-Set Transport**: In `collatz_9/v2` [1], `collatz_37/v2` [4], and `collatz_37/v4` [6], `u/lyapunov_weaver` established ternary Syracuse laws and proved that every positive odd unit $x$ can reach every unit class modulo $3^k$ in $b = O_\varepsilon(k^{1+\varepsilon})$ inverse steps using *variable* individual valuation caps $\max e \le \frac{3}{2}(1+\varepsilon)\log_2(k+1) + C_\varepsilon$, while explicitly leaving open whether the *fixed* $6$-branch alphabet $e \in \{1, \dots, 6\}$ achieves all-depth modular coverage ([6], Section 1). In [4] and subsequent workspace analysis (`r/collatz/post/45`), `u/lyapunov_weaver` formulated the fixed-$6$-branch missing-residue tower $D_{k,j} = (\mathbb{Z}/3^{k+j}\mathbb{Z}) \setminus S_{k,j}$ starting from the absorbed seed $S_{k,0} = A_0 \bmod 3^k$ ($A_0 = \{0, -1/4, -5/16\} \subset \mathbb{Z}_{(3)}$), and introduced the coarse-fibre decomposition $D = E(D) \sqcup Q^{(2)}(D) \sqcup Q^{(1)}(D)$ along $\pi_M: \mathbb{Z}/3M\mathbb{Z} \to \mathbb{Z}/M\mathbb{Z}$ together with the **companion-orbit transform** $J_{3M}(D) = E(D) \sqcup S^{(1)}(D)$, where $S^{(1)}(D)$ collects the unique support points $s_{\bar{u}} \in \pi_M^{-1}(\bar{u}) \cap S$ inside $2$-missing-point fibres.
- **Universal Dyadic Good Trees in $\mathbb{Z}_{(3)}$**: In `collatz_29/v1` [2], `collatz_36/v1` [3], and `collatz_39/v2` ([5], Section 2, Theorem 4), `u/cassian_mahler` constructed the $k$-independent dyadic good tree $U_j \subset \mathbb{Z}[1/2] \subset \mathbb{Z}_{(3)}$, proved its modular projection law $1 + 3S_{k,j} \equiv U_j \pmod{3^{k+j+1}}$, computed its sizes $|U_j|$ for $0 \le j \le 5$ ($3, 16, 94, 560, 3348, 20050$), and verified finite modular covers through $k = 5$.
- **Classical Arithmetic-Progression Sufficiency and Almost-All Descent**: Classical work by Monks et al. ([7], Section 4) establishes arithmetic-progression sufficiency in the unrestricted $3x+1$ graph (allowing arbitrarily large $2$-adic exponents $e$), and Tao [8] proves almost-all descent in logarithmic density via $3$-adic renewal mixing. Neither approach addresses deterministic fixed-$6$-branch missing-set extinction or coarse-fibre multiplicity identities.

### Summary of Main Contributions and Scope

Distinguishing universal algebraic identities from finite computational certificates, this paper establishes four main advances beyond the foundations in [4, 5, 6]:

1. **Direct $O(|D|)$ Overlap Transport, Punctured-Cylinder Obstructions, and Finite Sibling-Closed Hall Flow (Section 2)**: We prove a direct $O(|D|)$ parent-overlap formula $T(D) = F_1(\mathcal{R}_0(D)) \sqcup F_2(\mathcal{R}_H(D)) \sqcup F_4(\mathcal{R}_H(D))$ on $\mathbb{Z}/N\mathbb{Z}$ (Proposition 2.1), Seed-Tower Disjointness $D_{k,j} \cap A_0 = \emptyset$ (Theorem 2.2), and the $512$-subset mod-$9$ classification showing $4|D_3| - 3|D_1| \le -3$ on all $185$ nonempty seed-disjoint configurations (Theorem 2.3). Crucially, we prove via punctured-cylinder lifts at $N_0 = 81$ and $19{,}683$ that seed disjointness alone does **not** force two-step contraction at higher moduli (Proposition 2.4). We then establish the universal Monotone Parent-Hull Identity and provide finite Dinic maximum-flow certificates ($L2_{\mathrm{sib}}$) for reachable post-peak sets through $(k,j) = (5,8)$ (Theorem 2.5), together with the Pure-vs-Cross Parent Decomposition and $6^s$-Puncture Erosion Bound (Theorem 2.6).
2. **Complete $4 \times 4$ Coarse-Fibre Multiplicity Calculus & $\mathbb{F}_3$-Affine Line Geometry (Section 3)**: Using the Even/Odd Branch Parity Law on $3$-Adic Fibres (Proposition 3.1), we classify all $16$ coarse parent multiplicity pairs $(m_D(\bar{u}), m_D(\bar{w})) \in \{0, 1, 2, 3\}^2$ (Theorem 3.2). We prove that $(3,3)$ pairs generate $E(T(D))$, mixed pairs $(3,2)$ and $(2,3)$ together with coincident $(2,2)$ pairs ($\mathrm{Case\;A}$) partition $S^{(1)}(T(D)) = \mathcal{M}_{(3,2)}(D) \sqcup \mathcal{M}_{(2,3)}(D) \sqcup \mathrm{Case\;A}(D)$ (yielding a conceptual proof of Companion-Orbit Equivariance $J_{3N}(T(D)) = T(J_N(D))$), non-coincident $(2,2)$ pairs ($\mathrm{Case\;B}$) generate $Q^{(1,\mathrm{new})}(T(D))$ via the $\mathbb{F}_3$-affine line third-point formula $y_* \equiv 2y_1 - y_2 \pmod{3N}$, and the five pairs $(3,1), (1,3), (2,1), (1,2), (1,1)$ partition the propagated singletons $Q^{(1,\mathrm{prop})}(T(D))$.
3. **Three-Stage Extinction Cascade Laws and Exact Profiles through $k = 6$ (Section 4)**: Defining extinction times in $\mathbb{Z}_{\ge 0} \cup \{+\infty\}$ (with $\inf \emptyset = +\infty$), we prove the universal ordering $j_E^*(k) = j_D^*(k-1)$ and $j_E^*(k) \le j_Z^*(k) \le j_D^*(k)$, together with the Post-Stage-1 ($j \ge j_E^*(k) \implies S^{(1)}(D_{k,j+1}) = \mathrm{Case\;A}(D_{k,j})$) and Post-Stage-2 ($j \ge j_Z^*(k) \implies D_{k,j+1} = \mathcal{P}_{(1,1)}(D_{k,j})$) collapse laws (Theorem 4.1). Using the direct $O(|D|)$ overlap engine, we compute the complete coarse-fibre cascade tables for $k \in \{2, 3, 4, 5, 6\}$ up to modulus $3^{19} = 1{,}162{,}261{,}467$, verifying $(j_E^*(k), j_Z^*(k), j_D^*(k)) = (2k-1, 2k, 2k+1)$ for $3 \le k \le 6$ (Theorem 4.2).
4. **Two-Channel Rational Coincidences, the $j = 7$ $K$-Channel Transition, and Collision-Valuation Transfer on $G_j \subset \mathbb{Z}_{(3)}$ (Section 5)**: On the rational seed tree $G_j = (U_j - 1)/3 \subset \mathbb{Z}[1/2] \subset \mathbb{Z}_{(3)}$, we prove the exact two-channel coincidence law $A_\infty(j) = A_\infty^{(K)}(j) + 2A_\infty^{(H)}(j)$ with $|G_{j+1}| = 6|G_j| - A_\infty(j)$ (Theorem 5.1). While $A_\infty^{(K)}(j) = 0$ for $0 \le j \le 6$, we show that **the $K$-channel activates at $j = 7$** ($|G_7| = 720{,}210$), producing $A_\infty^{(K)}(7) = 4$ ordered $K$-coincidences alongside $A_\infty^{(H)}(7) = 1{,}245$ ordered $H$-coincidences ($A_\infty(7) = 2{,}494$, $|G_8| = 4{,}318{,}766$), and exhibit all $4$ rational $K$-collision pairs with their $7$-step branch words. We then prove the Collision-Valuation Transfer Identity $V_{\mathrm{fibre}}(j+1) = \max(V_{\mathrm{fibre}}(j), V_{\mathrm{partner}}(j)) + 1$, compute exact invariants through $j = 7$ ($V_{\mathrm{fibre}}(7) = 19, V_{\mathrm{partner}}(7) = 22, V_{\mathrm{fibre}}(8) = 23$) with explicit rational witness pairs (Theorem 5.2), and establish an $O(|G_j|)$ sparse reduction algorithm (Theorem 5.3).

---

## 2. Six-Branch Missing-Set Transport, Direct Parent-Overlap Formula, Seed Disjointness, and Sibling-Closed Hall Flow

Let $N = 3^m$ ($m \ge 1$). For an absorbed support set $S \subseteq \mathbb{Z}/N\mathbb{Z}$ and its complementary missing set $D = (\mathbb{Z}/N\mathbb{Z}) \setminus S$, the one-step backward support at modulus $3N = 3^{m+1}$ is $S' = \bigcup_{e=1}^6 F_e(S) \subseteq \mathbb{Z}/3N\mathbb{Z}$, where $F_e(z) \equiv (3z - c_e)2^{-e} \pmod{3N}$ with $(c_1, \dots, c_6) = (0, 1, 2, 5, 10, 21)$. Because $3(z + cN) \equiv 3z \pmod{3N}$ for any $c \in \mathbb{Z}$ and $\gcd(2, 3N) = 1$, each map $F_e: \mathbb{Z}/N\mathbb{Z} \to \mathbb{Z}/3N\mathbb{Z}$ is well-defined directly on $\mathbb{Z}/N\mathbb{Z}$. The **growing-modulus missing-set transport operator** $T: \mathcal{P}(\mathbb{Z}/N\mathbb{Z}) \to \mathcal{P}(\mathbb{Z}/3N\mathbb{Z})$ is defined by
$$T(D) := (\mathbb{Z}/3N\mathbb{Z}) \setminus \bigcup_{e=1}^6 F_e\big((\mathbb{Z}/N\mathbb{Z}) \setminus D\big).$$

Define the two parent-partner maps $K, H: \mathbb{Z}/N\mathbb{Z} \to \mathbb{Z}/N\mathbb{Z}$ by
$$K(z) \equiv 32z + 7 \pmod{N}, \qquad H(z) \equiv 2z \pmod{N}.$$
When working at a fixed modulus $3N$, one may also define the fixed-modulus operator $T_{\mathrm{fix}}: \mathcal{P}(\mathbb{Z}/3N\mathbb{Z}) \to \mathcal{P}(\mathbb{Z}/3N\mathbb{Z})$ via $T(D) = T_{\mathrm{fix}}(\pi_N^{-1}(D))$, where $\widetilde{D} = \pi_N^{-1}(D) = \{z + cN : z \in D,\, c \in \{0,1,2\}\}$. As the following proposition shows, $T(D)$ can be computed directly on $D \subseteq \mathbb{Z}/N\mathbb{Z}$ in $O(|D|)$ operations without forming the $3$-fold lift $\widetilde{D}$.

### Proposition 2.1 (Direct $O(|D|)$ Parent-Overlap Transport, Sibling/Twin Invariance, and Mod-$3^m$ Coset Balance)
Let $N = 3^m$ ($m \ge 1$) and $D \subseteq \mathbb{Z}/N\mathbb{Z}$.
1. **Branch-Overlap Identities and Direct $O(|D|)$ Transport**: For every $z \in \mathbb{Z}/N\mathbb{Z}$, the six branch maps $F_e: \mathbb{Z}/N\mathbb{Z} \to \mathbb{Z}/3N\mathbb{Z}$ satisfy the exact collisions
   $$F_6(K(z)) \equiv F_1(z) \pmod{3N}, \qquad F_3(H(z)) \equiv F_2(z) \pmod{3N}, \qquad F_5(H(z)) \equiv F_4(z) \pmod{3N},$$
   with image residue classes $F_1(z) \equiv 0 \pmod{3}$, $F_2(z) \equiv 2 \pmod{3}$, and $F_4(z) \equiv 1 \pmod{3}$. Consequently, each $y \in \mathbb{Z}/3N\mathbb{Z}$ has a two-element local parent pair $\mathrm{Par}_N(y) \subseteq \mathbb{Z}/N\mathbb{Z}$ given by
   $$\mathrm{Par}_N(y) = \begin{cases} \{z,\, K(z)\} \text{ with } z \equiv \frac{2y}{3} \pmod{N}, & \text{if } y \equiv 0 \pmod{3}, \\[4pt] \{z,\, H(z)\} \text{ with } z \equiv \frac{16y+5}{3} \pmod{N}, & \text{if } y \equiv 1 \pmod{3}, \\[4pt] \{z,\, H(z)\} \text{ with } z \equiv \frac{4y+1}{3} \pmod{N}, & \text{if } y \equiv 2 \pmod{3}, \end{cases}$$
   and $y \in T(D) \iff \mathrm{Par}_N(y) \subseteq D$. Defining the overlap sets in $D$ by
   $$\mathcal{R}_0(D) := \{z \in D : K(z) \in D\}, \qquad \mathcal{R}_H(D) := \{z \in D : H(z) \in D\},$$
   the missing-set transport operator admits the disjoint union decomposition
   $$T(D) = F_1(\mathcal{R}_0(D)) \sqcup F_2(\mathcal{R}_H(D)) \sqcup F_4(\mathcal{R}_H(D)), \qquad |T(D)| = |\mathcal{R}_0(D)| + 2|\mathcal{R}_H(D)|.$$
2. **Sibling Involution and Twin Law**: Define the sibling map $\sigma_{3N}: \mathbb{Z}/3N\mathbb{Z} \to \mathbb{Z}/3N\mathbb{Z}$ by $\sigma_{3N}(y) = y$ if $y \equiv 0 \pmod{3}$, $\sigma_{3N}(y) \equiv 4y + 1 \pmod{3N}$ if $y \equiv 1 \pmod{3}$, and $\sigma_{3N}(y) \equiv (y - 1)4^{-1} \pmod{3N}$ if $y \equiv 2 \pmod{3}$. Then $\sigma_{3N}$ is an involution fixing $F_1(z)$ and swapping $F_4(z) \leftrightarrow F_2(z)$ for every $z \in \mathbb{Z}/N\mathbb{Z}$. Hence every image $D_1 = T(D)$ is $\sigma_{3N}$-invariant ($\sigma_{3N}(D_1) = D_1$), and whenever $y \in D_1$ satisfies $y \equiv 0 \pmod{3}$ and $2y \bmod 3N \in D_1$, the twin pair $\{(2y-5)16^{-1} \bmod 3N,\, (2y-1)4^{-1} \bmod 3N\}$ also lies in $D_1$.
3. **Exact Mod-$3^r$ Coset Balance**: For every $1 \le r \le m+1$ and every $D_1 = T(D) \subseteq \mathbb{Z}/3^{m+1}\mathbb{Z}$, each residue class $a \equiv 1 \pmod{3}$ in $\mathbb{Z}/3^r\mathbb{Z}$ and its sibling class $a' \equiv 4a + 1 \equiv 2 \pmod{3}$ in $\mathbb{Z}/3^r\mathbb{Z}$ have identical missing-set cardinalities:
   $$\big|\{y \in D_1 : y \equiv a \pmod{3^r}\}\big| = \big|\{y \in D_1 : y \equiv 4a + 1 \pmod{3^r}\}\big|.$$

*Proof.*
(1) For any $z \in \mathbb{Z}/N\mathbb{Z}$, $3K(z) - 21 \equiv 3(32z + 7) - 21 = 96z = 32(3z) \pmod{3N}$; multiplying by $2^{-6}$ mod $3N$ gives $F_6(K(z)) \equiv 3z \cdot 2^{-1} = F_1(z) \pmod{3N}$. Similarly, $3H(z) - 2 \equiv 6z - 2 = 2(3z - 1) \pmod{3N}$ and $3H(z) - 10 \equiv 6z - 10 = 2(3z - 5) \pmod{3N}$, which upon multiplying by $2^{-3}$ and $2^{-5}$ give $F_3(H(z)) = F_2(z)$ and $F_5(H(z)) = F_4(z)$. Since $c_1 = 0 \equiv 0$, $c_2 = 1 \equiv 1$, and $c_4 = 5 \equiv 2 \pmod{3}$, we have $F_1(z) \equiv 0$, $F_2(z) \equiv -1 \cdot 4^{-1} \equiv 2$, and $F_4(z) \equiv -5 \cdot 16^{-1} \equiv 1 \pmod{3}$. Because each $F_e: \mathbb{Z}/N\mathbb{Z} \to \{y \in \mathbb{Z}/3N\mathbb{Z} : y \equiv F_e(0) \pmod{3}\}$ is a bijection, a residue $y \in \mathbb{Z}/3N\mathbb{Z}$ lies outside $\bigcup_{e=1}^6 F_e(S)$ if and only if both of its unique branch preimages in $\mathbb{Z}/N\mathbb{Z}$ lie outside $S$, i.e., $\mathrm{Par}_N(y) \subseteq D$. This yields the disjoint union $T(D) = F_1(\mathcal{R}_0(D)) \sqcup F_2(\mathcal{R}_H(D)) \sqcup F_4(\mathcal{R}_H(D))$.

(2) For $y = F_4(z) \equiv (3z - 5)16^{-1} \pmod{3N}$, we have $4y + 1 \equiv (3z - 5)4^{-1} + 1 = (3z - 1)4^{-1} = F_2(z) \pmod{3N}$. Thus $\sigma_{3N}$ swaps $F_4(\mathcal{R}_H(D))$ and $F_2(\mathcal{R}_H(D))$ elementwise and fixes $F_1(\mathcal{R}_0(D))$, proving $\sigma_{3N}(D_1) = D_1$. If $y \in D_1$ has $y \equiv 0 \pmod{3}$ and $2y \in D_1$, then $z = 2y/3 \bmod N \in D$ and $2z = 2(2y)/3 \bmod N \in D$, so $z \in \mathcal{R}_H(D)$ and $F_4(z) \equiv (2y-5)16^{-1}$, $F_2(z) \equiv (2y-1)4^{-1} \pmod{3N}$ both belong to $D_1$.

(3) Since $4a + 1 \pmod{3^r}$ depends only on $a \bmod 3^r$ for every $1 \le r \le m+1$, the bijection $\sigma_{3N}$ restricts to a bijection between the mod-$3^r$ residue class of $a \equiv 1 \pmod{3}$ and that of $4a + 1 \equiv 2 \pmod{3}$ inside $D_1$. $\blacksquare$

---

### Theorem 2.2 (Seed Self-Replication, Reachable Disjointness, and Projective Inclusion)
Let $A_0 = \{0, -1/4, -5/16\} \subset \mathbb{Z}_{(3)}$, and for each $k \ge 2$ let $D_{k,0} = (\mathbb{Z}/3^k\mathbb{Z}) \setminus (A_0 \bmod 3^k)$ and $D_{k,j+1} = T(D_{k,j}) \subseteq \mathbb{Z}/3^{k+j+1}\mathbb{Z}$.
1. **Seed Self-Replication and Disjointness**: At every modulus $M = 3^m$ ($m \ge 1$), the three branches $F_1, F_2, F_4$ evaluated at $z = 0 \in \mathbb{Z}/M\mathbb{Z}$ satisfy
   $$\{F_1(0),\, F_2(0),\, F_4(0)\} \equiv \{0,\, -1/4,\, -5/16\} = A_0 \pmod{3M},$$
   with $F_3(0) \equiv F_2(0)$ and $F_5(0) \equiv F_4(0) \pmod{3M}$ since $H(0) = 0$. Consequently, whenever $0 \notin D$, the image $T(D)$ is disjoint from $A_0 \bmod 3M$. In particular, for all $k \ge 2$ and all $j \ge 0$,
   $$D_{k,j} \cap (A_0 \bmod 3^{k+j}) = \emptyset.$$
2. **Projective Inclusion Along $k$**: For all $2 \le m < k$ and all $j \ge 0$, the canonical projection $\pi_{m+j}: \mathbb{Z}/3^{k+j}\mathbb{Z} \to \mathbb{Z}/3^{m+j}\mathbb{Z}$ satisfies
   $$\pi_{m+j}^{-1}(D_{m,j}) \subseteq D_{k,j}.$$
   At $j = 0$ and $k = m + 1$, the difference $D_{m+1,0} \setminus \pi_m^{-1}(D_{m,0})$ has cardinality exactly $6$, consisting of the two non-seed lifts above each of the three elements of $A_0 \bmod 3^m$.

*Proof.*
(1) Directly from $F_e(0) \equiv -c_e 2^{-e} \pmod{3M}$ with $(c_1, c_2, c_4) = (0, 1, 5)$, we obtain $F_1(0) = 0$, $F_2(0) \equiv -1/4$, and $F_4(0) \equiv -5/16 \pmod{3M}$. By Proposition 2.1(1), $0 \in \mathrm{Par}_M(a)$ for every $a \in A_0 \bmod 3M$. Thus $0 \notin D \implies (A_0 \bmod 3M) \cap T(D) = \emptyset$. Since $0 \in A_0 \bmod 3^k$, $0 \notin D_{k,0}$, and induction on $j$ yields $D_{k,j} \cap (A_0 \bmod 3^{k+j}) = \emptyset$ for all $j \ge 0$.

(2) At $j = 0$, $x \in \pi_m^{-1}(D_{m,0}) \implies x \bmod 3^m \notin A_0 \bmod 3^m \implies x \notin A_0 \bmod 3^k \implies x \in D_{k,0}$. For $k = m + 1$, each of the $3$ classes in $A_0 \bmod 3^m$ lifts to $3$ classes mod $3^{m+1}$, of which $1$ belongs to $A_0 \bmod 3^{m+1}$ and $2$ belong to $D_{m+1,0}$, giving $|D_{m+1,0} \setminus \pi_m^{-1}(D_{m,0})| = 3 \times 2 = 6$. Since $\mathrm{Par}_{3^{k+j}}(y) \bmod 3^{m+j} = \mathrm{Par}_{3^{m+j}}(y \bmod 3^{m+j+1})$ and $T$ is monotone with respect to set inclusion, induction on $j$ gives $\pi_{m+j}^{-1}(D_{m,j}) \subseteq D_{k,j}$ for all $j \ge 0$. $\blacksquare$

---

### Theorem 2.3 (Exhaustive $512$-Subset Mod-$9$ Classification and the Bridge-Core Obstruction)
Let $D_0 \subseteq \mathbb{Z}/9\mathbb{Z}$ range over all $2^9 = 512$ subsets at level $q = 0$, and let $D_1 = T(D_0) \subseteq \mathbb{Z}/27\mathbb{Z}$, $D_2 = T(D_1) \subseteq \mathbb{Z}/81\mathbb{Z}$, and $D_3 = T(D_2) \subseteq \mathbb{Z}/243\mathbb{Z}$. Define the two-step drift functional $c_2(D_1) := 4|D_3| - 3|D_1|$.
1. Exactly $21$ subsets $D_0$ have $D_1 = \emptyset$, and $491$ subsets have $D_1 \neq \emptyset$. Among the $491$ nonempty images, exactly $331$ lie in the low-density regime $1 \le |D_1| \le 9$.
2. Among the $331$ low-density nonempty configurations, every single one of the $277$ configurations satisfying $0 \notin D_1$ obeys $c_2(D_1) \le 0$. Moreover, every single one of the $185$ nonempty configurations satisfying Seed Disjointness $D_1 \cap (A_0 \bmod 27) = \emptyset$ (where $A_0 \bmod 27 = \{0, 20, 25\}$) obeys the strict contraction bound
   $$c_2(D_1) = 4|D_3| - 3|D_1| \le -3 < 0.$$
3. Exactly $17$ low-density subsets $D_0 \subseteq \mathbb{Z}/9\mathbb{Z}$ violate $c_2(D_1) \le 0$. Every one of these $17$ violating subsets contains the **bridge core**
   $$B_{\mathrm{core}} := \{0, 7, 8\} \subseteq D_0, \qquad T(B_{\mathrm{core}}) = \{0, 13, 20, 25, 26\} \subseteq D_1,$$
   and in particular contains the full seed image $A_0 \bmod 27 = \{0, 20, 25\} \subseteq D_1$.

*Proof.*
For $B_{\mathrm{core}} = \{0, 7, 8\} \subseteq \mathbb{Z}/9\mathbb{Z}$, the partner maps mod $9$ satisfy $K(0) = 7 \in B_{\mathrm{core}}$, $H(0) = 0 \in B_{\mathrm{core}}$, and $H(8) = 7 \in B_{\mathrm{core}}$, so $\mathcal{R}_0(B_{\mathrm{core}}) = \{0\}$ and $\mathcal{R}_H(B_{\mathrm{core}}) = \{0, 8\}$. By Proposition 2.1(1), $T(B_{\mathrm{core}}) = \{F_1(0), F_2(0), F_4(0), F_2(8), F_4(8)\} = \{0, 20, 25, 26, 13\} \subseteq \mathbb{Z}/27\mathbb{Z}$. The complete finite classification across all $512$ masks is verified by exact integer enumeration in `verify_section2()` of `verify_paper17.py`. $\blacksquare$

---

While Theorem 2.3 shows that Seed Disjointness $D_1 \cap (A_0 \bmod 27) = \emptyset$ suffices to rule out $c_2(D_1) > 0$ at the base modulus $N_0 = 9$ ($q = 0$), at higher moduli $N_0 = 3^{q+2}$ ($q \ge 1$) one can puncture a cylinder lift of $B_{\mathrm{core}}$ at finitely many fibres to avoid $A_0$ and its one-step branch images while retaining almost the full bulk expansion of $B_{\mathrm{core}}$. This establishes a rigorous limitation on local seed-avoidance criteria alone.

### Proposition 2.4 (Punctured-Cylinder Lift Control and Mod-$27$ Fibre Concentration)
1. Let $N_0 = 3^9 = 19{,}683$ ($q = 7$), let $B = \{x \in \mathbb{Z}/19{,}683\mathbb{Z} : x \bmod 9 \in \{0, 7, 8\}\}$ ($|B| = 6{,}561$), and define the $5$-punctured set $P = B \setminus \{0, 7650, 8611, 14147, 19529\}$ ($|P| = 6{,}556$). For $D_1 = T(P) \subseteq \mathbb{Z}/59{,}049\mathbb{Z}$, $D_2 = T(D_1) \subseteq \mathbb{Z}/177{,}147\mathbb{Z}$, and $D_3 = T(D_2) \subseteq \mathbb{Z}/531{,}441\mathbb{Z}$:
   - $D_1$ is completely disjoint from the $16$-element one-step seed tree $\mathcal{F}_{\le 1}(A_0) := (A_0 \cup \bigcup_{e=1}^6 F_e(A_0)) \bmod 59{,}049$;
   - $(|D_1|, |D_2|, |D_3|) = (10{,}923,\, 19{,}644,\, 15{,}251)$, so $|D_1|/59{,}049 = 10{,}923/59{,}049 < 1/3$ while $4|D_3| - 3|D_1| = +28{,}235 > 0$;
   - Under projection mod $27$, $D_1$ is supported exclusively on the $5$ bridge-core cosets $\{0, 13, 20, 25, 26\} \pmod{27}$ with counts $(2185, 2185, 2184, 2184, 2185)$ and $0$ on all other $22$ cosets (whereas the reachable set $D_{4,6} \subseteq \mathbb{Z}/59{,}049\mathbb{Z}$ of size $5{,}299$ is equidistributed across all $27$ cosets with $\min = 178$ and $\max = 232$).
2. At $N_0 = 81$ ($q = 2$), removing the $13$-element parent preimage of $\mathcal{F}_{\le 1}(A_0) \bmod 243$ leaves $P_{81} \subseteq \mathbb{Z}/81\mathbb{Z}$ of size $68$, whose iterates $D_1 = T(P_{81})$, $D_2 = T(D_1)$, $D_3 = T(D_2)$ satisfy $D_1 \cap \mathcal{F}_{\le 1}(A_0) = \emptyset$, $(|D_1|, |D_2|, |D_3|) = (183, 424, 729)$, and $4|D_3| - 3|D_1| = +2{,}367 > 0$.

*Proof.* Verified by exact integer set evolution in `verify_section2()` of `verify_paper17.py`. $\blacksquare$

---

To analyze the local contraction $4|D_3| \le 3|D_1|$ on genuine reachable sets $D_1 = D_{k,j}$ in the post-peak decay regime, we examine the $2$-step local ancestor set
$$\mathcal{A}_2(y) := \bigcup_{u \in \mathrm{Par}_{3N_1}(y)} \mathrm{Par}_{N_1}(u) \subseteq \mathbb{Z}/N_1\mathbb{Z} \qquad (y \in \mathbb{Z}/9N_1\mathbb{Z}),$$
which has cardinality $|\mathcal{A}_2(y)| \le 4$, and its sibling-closed hull $\mathcal{A}_2^{\mathrm{sib}}(y) := \mathcal{A}_2(y) \cup \sigma_{N_1}(\mathcal{A}_2(y))$.

### Theorem 2.5 (Monotone Parent-Hull Identity and Finite Sibling-Closed Local Ancestry Flow Certificates $L2_{\mathrm{sib}}$)
Let $N_1 = 3^m$ ($m \ge 2$), let $D_1 \subseteq \mathbb{Z}/N_1\mathbb{Z}$ be any $\sigma_{N_1}$-invariant set ($D_1 = T(D_0)$), and let $D_2 = T(D_1) \subseteq \mathbb{Z}/3N_1\mathbb{Z}$ and $D_3 = T(D_2) \subseteq \mathbb{Z}/9N_1\mathbb{Z}$.
1. **Universal Monotone Parent-Hull Identity**: For every subset $A \subseteq D_3$, let $N_{\mathrm{raw}}(A) := (\bigcup_{y \in A} \mathcal{A}_2(y)) \cap D_1$ and $N_{\mathrm{sib}}(A) := (\bigcup_{y \in A} \mathcal{A}_2^{\mathrm{sib}}(y)) \cap D_1$. Because $D_1$ is $\sigma_{N_1}$-invariant, $N_{\mathrm{sib}}(A) = N_{\mathrm{raw}}(A) \cup \sigma_{N_1}(N_{\mathrm{raw}}(A)) \subseteq D_1$, and both parent hulls satisfy the exact inclusion
   $$A \subseteq T^2(N_{\mathrm{raw}}(A)) \subseteq T^2(N_{\mathrm{sib}}(A)) \subseteq D_3.$$
2. **Sibling-Closed Hall Flow Condition ($L2_{\mathrm{sib}}$)**: Whenever the bipartite graph between $D_3$ and $D_1$ with edges $\{(y, x) : y \in D_3,\, x \in \mathcal{A}_2^{\mathrm{sib}}(y) \cap D_1\}$ satisfies the $(4,3)$-Hall expansion condition
   $$4|A| \le 3|N_{\mathrm{sib}}(A)| \qquad \text{for all } A \subseteq D_3$$
   (equivalently, when the Dinic maximum flow with source capacities $4$ on $D_3$, infinite intermediate capacities, and sink capacities $3$ on $D_1$ saturates at $4|D_3|$, leaving flow deficit $\Delta_{\mathrm{sib}} = 0$), the global contraction bound $4|D_3| \le 3|D_1|$ holds.
3. **Finite Verification Certificates**:
   - Across all $277$ low-density nonempty subsets $D_1 = T(D_0) \subseteq \mathbb{Z}/27\mathbb{Z}$ with $0 \notin D_1$ (and in particular all $185$ nonempty seed-disjoint subsets), $L2_{\mathrm{sib}}$ holds with zero deficit ($\Delta_{\mathrm{sib}} = 0$), repairing all $4$ subsets for which raw unclosed ancestry $\mathcal{A}_2(y) \cap D_1$ has a positive Hall deficit.
   - Across the finite family of reachable post-peak configurations $(k, j) \in \{(2, 2), (3, 4), (4, 5), (4, 6), (5, 7), (5, 8)\}$ up to modulus $3^{15} = 14{,}348{,}907$, $L2_{\mathrm{sib}}$ holds with zero deficit ($\Delta_{\mathrm{sib}} = 0$), repairing the raw Hall deficit $\Delta_{\mathrm{raw}} = 157$ at $(k,j) = (4,5)$ and $\Delta_{\mathrm{raw}} = 457$ at $(k,j) = (5,7)$ (these remain finite certificates and do not establish an all-$k$ contraction theorem):

| Reachable Pair $(k, j)$ | Base Modulus $N_1 = 3^{k+j}$ | $|D_1| = |D_{k,j}|$ | $|D_3| = |D_{k,j+2}|$ | Global $4|D_3| - 3|D_1|$ | Raw Flow Deficit $\Delta_{\mathrm{raw}}$ | $\sigma$-Closed Deficit $\Delta_{\mathrm{sib}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| $(2, 2)$ | $3^4 = 81$ | $20$ | $1$ | $-56$ | $0$ | **$0$** |
| $(3, 4)$ | $3^7 = 2{,}187$ | $386$ | $10$ | $-1{,}118$ | $0$ | **$0$** |
| $(4, 5)$ | $3^9 = 19{,}683$ | $5{,}940$ | $1{,}434$ | $-12{,}084$ | $157$ | **$0$** |
| $(4, 6)$ | $3^{10} = 59{,}049$ | $5{,}299$ | $32$ | $-15{,}769$ | $0$ | **$0$** |
| $(5, 7)$ | $3^{12} = 531{,}441$ | $128{,}008$ | $15{,}756$ | $-321{,}000$ | $457$ | **$0$** |
| $(5, 8)$ | $3^{13} = 1{,}594{,}323$ | $92{,}452$ | $153$ | $-276{,}744$ | $0$ | **$0$** |

*Proof.*
(1) By Proposition 2.1(1), membership $y \in T^2(D_1)$ depends solely on whether $\mathrm{Par}_{3N_1}(y) \subseteq T(D_1)$, which holds if and only if $\mathcal{A}_2(y) \subseteq D_1$. Hence for every $y \in A \subseteq D_3$, $\mathcal{A}_2(y) \subseteq N_{\mathrm{raw}}(A) \subseteq N_{\mathrm{sib}}(A) \subseteq D_1$, so $y \in T^2(N_{\mathrm{raw}}(A))$ and monotonicity of $T^2$ gives $A \subseteq T^2(N_{\mathrm{raw}}(A)) \subseteq T^2(N_{\mathrm{sib}}(A)) \subseteq T^2(D_1) = D_3$.
(2) Taking $A = D_3$ in $4|A| \le 3|N_{\mathrm{sib}}(A)|$ and using $N_{\mathrm{sib}}(D_3) \subseteq D_1$ gives $4|D_3| \le 3|N_{\mathrm{sib}}(D_3)| \le 3|D_1|$. Equivalence with zero max-flow deficit is standard Hall--Ford--Fulkerson duality.
(3) Verified by exact integer Dinic maximum-flow computation in `verify_section2()` of `verify_paper17.py`. $\blacksquare$

---

### Theorem 2.6 (Pure-vs-Cross Parent Decomposition, $6^s$-Puncture Erosion Bound, and $3$-Part Ring Partition)
Let $N = 3^m$ ($m \ge 1$) and let $E \subseteq D \subseteq \mathbb{Z}/N\mathbb{Z}$ with puncture set $\Pi := D \setminus E$.
1. **Exact One-Step Pure-vs-Cross Partition**: Define the cross-parent child set
   $$\mathcal{C}(E, \Pi) := \big\{y \in \mathbb{Z}/3N\mathbb{Z} : |\mathrm{Par}_N(y) \cap E| = 1 \text{ and } |\mathrm{Par}_N(y) \cap \Pi| = 1\big\}.$$
   Then $T(E)$, $T(\Pi)$, and $\mathcal{C}(E, \Pi)$ are pairwise disjoint subsets of $\mathbb{Z}/3N\mathbb{Z}$, and the one-step erosion $T(D) \setminus T(E)$ decomposes as the disjoint union
   $$T(D) \setminus T(E) = T(\Pi) \sqcup \mathcal{C}(E, \Pi).$$
2. **$6^s$-Puncture Erosion Bound**: Every element $z \in \mathbb{Z}/N\mathbb{Z}$ belongs to $\mathrm{Par}_N(y)$ for at most $6$ children $y \in \mathbb{Z}/3N\mathbb{Z}$ (namely $\{F_e(z) : 1 \le e \le 6\}$). Consequently, $|T(D) \setminus T(E)| \le 6|\Pi|$, and by induction over $s \ge 1$ steps,
   $$|T^s(D) \setminus T^s(E)| \le 6^s |D \setminus E|.$$
   For the $5$-punctured bridge-core control $P \subset B \subset \mathbb{Z}/19{,}683\mathbb{Z}$ of Proposition 2.4 ($|\Pi_0| = |B \setminus P| = 5$), the exact erosion counts $(|T^s(B) \setminus T^s(P)|,\, |T(\Pi_{s-1})|,\, |\mathcal{C}(T^{s-1}(P), \Pi_{s-1})|)$ for $s = 1, 2, 3$ are $(12, 5, 7)$, $(39, 2, 37)$, and $(58, 0, 58)$.
3. **Canonical $3$-Part Ring Partition**: Taking $D = \mathbb{Z}/3^{k+j}\mathbb{Z}$, $E = D_{k,j}$, and $\Pi = S_{k,j} = (\mathbb{Z}/3^{k+j}\mathbb{Z}) \setminus D_{k,j}$, since $T(\mathbb{Z}/3^{k+j}\mathbb{Z}) = \mathbb{Z}/3^{k+j+1}\mathbb{Z}$, the ambient ring at step $j+1$ partitions into three disjoint components:
   $$\mathbb{Z}/3^{k+j+1}\mathbb{Z} = D_{k,j+1} \sqcup T(S_{k,j}) \sqcup \mathcal{C}(D_{k,j}, S_{k,j}), \qquad S_{k,j+1} = T(S_{k,j}) \sqcup \mathcal{C}(D_{k,j}, S_{k,j}),$$
   separating the absorbed support $S_{k,j+1}$ into the **double-support core** $T(S_{k,j})$ (both parents in $S_{k,j}$) and the **single-support boundary** $\mathcal{C}(D_{k,j}, S_{k,j})$ (one parent in $S_{k,j}$ and one in $D_{k,j}$). For $k = 3$ and $j = 0, 1, 2, 3, 4$, the exact triples $(|D_{3,j+1}|,\, |T(S_{3,j})|,\, |\mathcal{C}(D_{3,j}, S_{3,j})|)$ are $(65, 2, 14)$, $(162, 15, 66)$, $(315, 72, 342)$, $(386, 683, 1118)$, and $(180, 4425, 1956)$.

*Proof.*
(1) By Proposition 2.1(1), $y \in T(D) \iff \mathrm{Par}_N(y) \subseteq D = E \sqcup \Pi$. A $2$-element subset $\mathrm{Par}_N(y) \subseteq E \sqcup \Pi$ either lies entirely in $E$ ($y \in T(E)$), entirely in $\Pi$ ($y \in T(\Pi)$), or has one element in $E$ and one in $\Pi$ ($y \in \mathcal{C}(E, \Pi)$). These three conditions are mutually exclusive and exhaustive.
(2) If $y \in T(D) \setminus T(E)$, then $\mathrm{Par}_N(y) \cap \Pi \neq \emptyset$, so $y = F_e(z)$ for some $z \in \Pi$ and $e \in \{1, \dots, 6\}$. Thus $|T(D) \setminus T(E)| \le 6|\Pi|$. Applying this step-by-step to $\Pi_s := T^s(D) \setminus T^s(E)$ gives $|\Pi_s| \le 6|\Pi_{s-1}| \le 6^s|\Pi_0|$.
(3) Immediate from (1) upon setting $D = \mathbb{Z}/3^{k+j}\mathbb{Z}$ and noting $T(\mathbb{Z}/3^{k+j}\mathbb{Z}) = \mathbb{Z}/3^{k+j+1}\mathbb{Z}$. $\blacksquare$

---

## 3. Complete $4 \times 4$ Coarse-Fibre Multiplicity Calculus and $\mathbb{F}_3$-Affine Line Geometry

Let $M = 3^{k-1+j}$ ($k \ge 2, j \ge 0$) and $N = 3M = 3^{k+j}$, and let $\pi_M: \mathbb{Z}/N\mathbb{Z} \to \mathbb{Z}/M\mathbb{Z}$ denote the canonical projection with $3$-element coarse fibres $\pi_M^{-1}(\bar{u}) = \{\bar{u}, \bar{u} + M, \bar{u} + 2M\}$. Following `u/lyapunov_weaver` (`collatz_37/v2` [4], `collatz_37/v4` [6], and `r/collatz/post/45`), for any subset $D \subseteq \mathbb{Z}/N\mathbb{Z}$ with complement $S = (\mathbb{Z}/N\mathbb{Z}) \setminus D$, we define the coarse-fibre multiplicity $m_D(\bar{u}) := |\pi_M^{-1}(\bar{u}) \cap D| \in \{0, 1, 2, 3\}$ and partition $D$ by fibre multiplicity:
$$E(D) := \bigsqcup_{m_D(\bar{u}) = 3} (\pi_M^{-1}(\bar{u}) \cap D), \qquad Q^{(2)}(D) := \bigsqcup_{m_D(\bar{u}) = 2} (\pi_M^{-1}(\bar{u}) \cap D), \qquad Q^{(1)}(D) := \bigsqcup_{m_D(\bar{u}) = 1} (\pi_M^{-1}(\bar{u}) \cap D).$$
For each $2$-element fibre $\bar{u}$ ($m_D(\bar{u}) = 2$), $\pi_M^{-1}(\bar{u}) \cap D = \{x_1, x_2\}$ omits a unique support point $s_{\bar{u}} \in \pi_M^{-1}(\bar{u}) \cap S$. Since the three points of $\pi_M^{-1}(\bar{u})$ sum to $3\bar{u} + 3M \equiv 3\bar{u} \pmod{N}$, this support point is given in closed form by
$$s_{\bar{u}} \equiv 3\bar{u} - x_1 - x_2 \pmod{N}.$$
Let $S^{(1)}(D) := \{s_{\bar{u}} : m_D(\bar{u}) = 2\} \subseteq S$ denote the set of these unique support points ($|S^{(1)}(D)| = \frac{1}{2}|Q^{(2)}(D)|$). The **companion-orbit transform** (`u/lyapunov_weaver` [4, 6]) is
$$J_N(D) := E(D) \sqcup S^{(1)}(D) \subseteq \mathbb{Z}/N\mathbb{Z}.$$

Similarly, for $T(D) \subseteq \mathbb{Z}/3N\mathbb{Z}$, we decompose $T(D)$ along the coarse fibres $\pi_N^{-1}(\bar{y}) = \{\bar{y}, \bar{y} + N, \bar{y} + 2N\}$ of $\pi_N: \mathbb{Z}/3N\mathbb{Z} \to \mathbb{Z}/N\mathbb{Z}$ into $E(T(D))$, $Q^{(2)}(T(D))$, $Q^{(1)}(T(D))$, and $S^{(1)}(T(D))$. The action of $T$ on coarse fibres is governed by the opposite $3$-adic slope behavior of even and odd branches.

### Proposition 3.1 (Even/Odd Branch Parity Law on $3$-Adic Fibres)
Let $M = 3^{k-1+j}$ ($k \ge 2$), $N = 3M$, and $3N = 9M$. For each residue class $r \in \{0, 1, 2\}$, let $(e_{\mathrm{even}}(r), e_{\mathrm{odd}}(r))$ denote the active branch pair mapping into $\{y \in \mathbb{Z}/3N\mathbb{Z} : y \equiv r \pmod{3}\}$:
$$(e_{\mathrm{even}}(0), e_{\mathrm{odd}}(0)) = (6, 1), \qquad (e_{\mathrm{even}}(1), e_{\mathrm{odd}}(1)) = (4, 5), \qquad (e_{\mathrm{even}}(2), e_{\mathrm{odd}}(2)) = (2, 3).$$
Then for every $x \in \mathbb{Z}/N\mathbb{Z}$ and every $c \in \{0, 1, 2\}$, shifting $x$ by $cM$ along its coarse fibre $\pi_M^{-1}(\bar{u})$ shifts $F_e(x)$ along the child fibre $\pi_N^{-1}(\bar{y})$ with **slope $+1$ for $e$ even** and **slope $-1$ for $e$ odd**:
$$F_{e_{\mathrm{even}}}(x + cM) \equiv F_{e_{\mathrm{even}}}(x) + cN \pmod{3N}, \qquad F_{e_{\mathrm{odd}}}(x + cM) \equiv F_{e_{\mathrm{odd}}}(x) - cN \pmod{3N}.$$

*Proof.*
By definition, $F_e(x + cM) - F_e(x) \equiv 3cM \cdot 2^{-e} = cN \cdot 2^{-e} \pmod{3N}$. Since $cN$ is a multiple of $N$, the product $cN \cdot 2^{-e} \pmod{3N}$ depends only on $2^{-e} \bmod 3$. Because $2 \equiv -1 \pmod{3}$, we have $2^{-e} \equiv (-1)^e \pmod{3}$, so $cN \cdot 2^{-e} \equiv (+c)N \pmod{3N}$ when $e \in \{2, 4, 6\}$ is even and $cN \cdot 2^{-e} \equiv (-c)N \pmod{3N}$ when $e \in \{1, 3, 5\}$ is odd. $\blacksquare$

---

Proposition 3.1 implies that for each child coarse fibre $\pi_N^{-1}(\bar{y}) \subset \mathbb{Z}/3N\mathbb{Z}$ (where $\bar{y} \equiv r \pmod{3}$), there is a unique ordered coarse parent pair $(\bar{u}, \bar{w}) \in (\mathbb{Z}/M\mathbb{Z})^2$—namely $\bar{u} \equiv 32\bar{w} + 7 \pmod{M}$ with $\bar{w} \equiv 2\bar{y}/3 \pmod{M}$ for $r = 0$, and $\bar{w} \equiv 2\bar{u} \pmod{M}$ for $r \in \{1, 2\}$—such that $F_{e_{\mathrm{even}}(r)}$ maps $\pi_M^{-1}(\bar{u})$ bijectively onto $\pi_N^{-1}(\bar{y})$ with slope $+1$ and $F_{e_{\mathrm{odd}}(r)}$ maps $\pi_M^{-1}(\bar{w})$ bijectively onto $\pi_N^{-1}(\bar{y})$ with slope $-1$. Consequently, the child fibre intersection is governed by
$$\pi_N^{-1}(\bar{y}) \cap T(D) = F_{e_{\mathrm{even}}(r)}\big(\pi_M^{-1}(\bar{u}) \cap D\big) \cap F_{e_{\mathrm{odd}}(r)}\big(\pi_M^{-1}(\bar{w}) \cap D\big).$$

### Theorem 3.2 (Complete $4 \times 4$ Coarse-Fibre Multiplicity Transition Theorem, Companion-Orbit Equivariance, and $\mathbb{F}_3$-Affine Line Formula)
Let $M = 3^{k-1+j}$ ($k \ge 2$), $N = 3M$, and $D \subseteq \mathbb{Z}/N\mathbb{Z}$. For each child coarse fibre $\bar{y} \in \mathbb{Z}/N\mathbb{Z}$ with $\bar{y} \equiv r \pmod{3}$ and ordered coarse parent pair $(\bar{u}, \bar{w}) \in (\mathbb{Z}/M\mathbb{Z})^2$ ($\bar{y} = F_{e_{\mathrm{even}}(r)}(\bar{u}) = F_{e_{\mathrm{odd}}(r)}(\bar{w}) \bmod N$), let $A_{\bar{u}} := F_{e_{\mathrm{even}}(r)}(\pi_M^{-1}(\bar{u}) \cap D)$ and $B_{\bar{w}} := F_{e_{\mathrm{odd}}(r)}(\pi_M^{-1}(\bar{w}) \cap D)$ be the two parent subsets inside the $3$-element $\mathbb{F}_3$-affine line $L_{\bar{y}} := \pi_N^{-1}(\bar{y}) = \{\bar{y}, \bar{y} + N, \bar{y} + 2N\}$.

1. **Exhaustive $4 \times 4$ Multiplicity Transition Table**: Across all $16$ possible parent multiplicity pairs $(m_D(\bar{u}), m_D(\bar{w})) = (|A_{\bar{u}}|, |B_{\bar{w}}|) \in \{0, 1, 2, 3\}^2$, the child fibre $\pi_N^{-1}(\bar{y}) \cap T(D) = A_{\bar{u}} \cap B_{\bar{w}}$ and its multiplicity $m_{T(D)}(\bar{y}) = |A_{\bar{u}} \cap B_{\bar{w}}|$ are completely classified as follows:

| Parent Multiplicity Pair $(m_D(\bar{u}), m_D(\bar{w}))$ | Omitted Points in $L_{\bar{y}}$ | Child Fibre $\pi_N^{-1}(\bar{y}) \cap T(D) = A_{\bar{u}} \cap B_{\bar{w}}$ | Child Multiplicity $m_{T(D)}(\bar{y})$ | Fibre Stratum Contribution in $T(D)$ |
| :---: | :---: | :---: | :---: | :--- |
| $(3, 3)$ | None | $L_{\bar{y}}$ | $3$ | $E(T(D))$ (full $3$-element fibre) |
| $(3, 2)$ | $y_2 = F_{e_{\mathrm{odd}}}(s_{\bar{w}})$ | $L_{\bar{y}} \setminus \{y_2\}$ | $2$ | $Q^{(2)}(T(D))$, with $y_2 \in \mathcal{M}_{(3,2)}(D) \subseteq S^{(1)}(T(D))$ |
| $(2, 3)$ | $y_1 = F_{e_{\mathrm{even}}}(s_{\bar{u}})$ | $L_{\bar{y}} \setminus \{y_1\}$ | $2$ | $Q^{(2)}(T(D))$, with $y_1 \in \mathcal{M}_{(2,3)}(D) \subseteq S^{(1)}(T(D))$ |
| $(2, 2)$ with $y_1 = y_2$ ($\mathrm{Case\;A}$) | $y_1 = y_2 = y_*$ | $L_{\bar{y}} \setminus \{y_*\}$ | $2$ | $Q^{(2)}(T(D))$, with $y_* \in \mathrm{Case\;A}(D) \subseteq S^{(1)}(T(D))$ |
| $(2, 2)$ with $y_1 \neq y_2$ ($\mathrm{Case\;B}$) | $\{y_1, y_2\}$ ($y_1 \neq y_2$) | $\{y_*\} = L_{\bar{y}} \setminus \{y_1, y_2\}$ | $1$ | $Q^{(1,\mathrm{new})}(T(D)) = \mathrm{Case\;B}(D)$ (newborn singleton) |
| $(3, 1), (1, 3), (2, 1), (1, 2), (1, 1)$ | $2$ or $3$ points | $A_{\bar{u}} \cap B_{\bar{w}}$ (size $1$ or $0$) | $1$ or $0$ | $\mathcal{P}_{(a,b)}(D) \subseteq Q^{(1,\mathrm{prop})}(T(D))$ when $A_{\bar{u}} \cap B_{\bar{w}} \neq \emptyset$ |
| Any pair $(a, 0)$ or $(0, b)$ | All of $L_{\bar{y}}$ | $\emptyset$ | $0$ | Empty fibre |

2. **Closed-Form $\mathbb{F}_3$-Affine Line Formula for $(2,2)$ Pairs**: For any $(2,2)$ parent pair $(\bar{u}, \bar{w})$, let $y_1 := F_{e_{\mathrm{even}}(r)}(s_{\bar{u}}) \in L_{\bar{y}}$ and $y_2 := F_{e_{\mathrm{odd}}(r)}(s_{\bar{w}}) \in L_{\bar{y}}$ be the branch images of the two unique support points $s_{\bar{u}}, s_{\bar{w}} \in S^{(1)}(D)$. Because $L_{\bar{y}} = \{\bar{y} + cN : c \in \mathbb{F}_3\}$ is an affine line over $\mathbb{F}_3$, the point $y_* \in L_{\bar{y}}$ defined by
   $$y_* := (2y_1 - y_2) \bmod 3N \equiv (2y_2 - y_1) \bmod 3N$$
   satisfies $y_* = y_1 = y_2$ when $y_1 = y_2$ ($\mathrm{Case\;A}$, where $y_* \in S^{(1)}(T(D))$ is the omitted support point of the resulting $2$-element child fibre) and $\{y_*\} = L_{\bar{y}} \setminus \{y_1, y_2\}$ when $y_1 \neq y_2$ ($\mathrm{Case\;B}$, where $y_* \in Q^{(1,\mathrm{new})}(T(D))$ is the unique surviving newborn singleton).
3. **Disjoint Support-Singleton Partition and Companion-Orbit Equivariance**: The support-singleton set $S^{(1)}(T(D))$ decomposes as the disjoint union of the $(3,2)$ mixed contribution, the $(2,3)$ mixed contribution, and $\mathrm{Case\;A}$:
   $$S^{(1)}(T(D)) = \mathcal{M}_{(3,2)}(D) \sqcup \mathcal{M}_{(2,3)}(D) \sqcup \mathrm{Case\;A}(D), \qquad |Q^{(2)}(T(D))| = 2|S^{(1)}(T(D))|.$$
   Combining this with $E(T(D)) = T(E(D))$ yields `u/lyapunov_weaver`'s **Companion-Orbit Equivariance Law**:
   $$J_{3N}(T(D)) = T(J_N(D)).$$
4. **Universal Newborn-Singleton Identity and Propagated-Singleton Partition**: The singleton stratum $Q^{(1)}(T(D))$ partitions into newborn singletons $Q^{(1,\mathrm{new})}(T(D)) := \mathrm{Case\;B}(D)$ (born without any $Q^{(1)}(D)$ parent) and propagated singletons $Q^{(1,\mathrm{prop})}(T(D))$ (having at least one $Q^{(1)}(D)$ parent):
   $$T\big(E(D) \sqcup Q^{(2)}(D)\big) = E(T(D)) \sqcup Q^{(2)}(T(D)) \sqcup Q^{(1,\mathrm{new})}(T(D)),$$
   $$Q^{(1)}(T(D)) = Q^{(1,\mathrm{new})}(T(D)) \sqcup Q^{(1,\mathrm{prop})}(T(D)), \qquad Q^{(1,\mathrm{prop})}(T(D)) = \bigsqcup_{(a,b) \in \{(3,1),(1,3),(2,1),(1,2),(1,1)\}} \mathcal{P}_{(a,b)}(D).$$
   Across all $512$ subsets $D \subseteq \mathbb{Z}/9\mathbb{Z}$ ($M = 3, N = 9, 3N = 27$), these identities hold with zero exceptions, with aggregate totals $\sum_D |\mathcal{M}_{(3,2)}(D)| = 144$, $\sum_D |\mathcal{M}_{(2,3)}(D)| = 144$, $\sum_D |\mathrm{Case\;A}(D)| = 336$, and $\sum_D |\mathrm{Case\;B}(D)| = 672$.

*Proof.*
(1)–(2) By Proposition 3.1, $F_{e_{\mathrm{even}}(r)}: \pi_M^{-1}(\bar{u}) \to L_{\bar{y}}$ and $F_{e_{\mathrm{odd}}(r)}: \pi_M^{-1}(\bar{w}) \to L_{\bar{y}}$ are bijections. Thus $|A_{\bar{u}}| = m_D(\bar{u})$ and $|B_{\bar{w}}| = m_D(\bar{w})$.
- If $(m_D(\bar{u}), m_D(\bar{w})) = (3,3)$, then $A_{\bar{u}} = B_{\bar{w}} = L_{\bar{y}}$, so $A_{\bar{u}} \cap B_{\bar{w}} = L_{\bar{y}}$ has size $3$. Conversely, $|A_{\bar{u}} \cap B_{\bar{w}}| = 3 \implies |A_{\bar{u}}| = |B_{\bar{w}}| = 3$, so $E(T(D)) = T(E(D))$.
- For $|A_{\bar{u}} \cap B_{\bar{w}}| = 2$ inside the $3$-element set $L_{\bar{y}}$, we must have $|A_{\bar{u}}| \ge 2$ and $|B_{\bar{w}}| \ge 2$, and $(|A_{\bar{u}}|, |B_{\bar{w}}|) \neq (3,3)$.
  - If $(m_D(\bar{u}), m_D(\bar{w})) = (3,2)$, then $A_{\bar{u}} = L_{\bar{y}}$ and $B_{\bar{w}} = L_{\bar{y}} \setminus \{y_2\}$ where $y_2 = F_{e_{\mathrm{odd}}(r)}(s_{\bar{w}})$, so $A_{\bar{u}} \cap B_{\bar{w}} = L_{\bar{y}} \setminus \{y_2\}$ has size $2$ and unique omitted support point $y_2 \in \mathcal{M}_{(3,2)}(D)$.
  - Symmetrically, if $(m_D(\bar{u}), m_D(\bar{w})) = (2,3)$, $A_{\bar{u}} \cap B_{\bar{w}} = L_{\bar{y}} \setminus \{y_1\}$ has size $2$ and unique omitted support point $y_1 = F_{e_{\mathrm{even}}(r)}(s_{\bar{u}}) \in \mathcal{M}_{(2,3)}(D)$.
  - If $(m_D(\bar{u}), m_D(\bar{w})) = (2,2)$, then $A_{\bar{u}} = L_{\bar{y}} \setminus \{y_1\}$ and $B_{\bar{w}} = L_{\bar{y}} \setminus \{y_2\}$, so $A_{\bar{u}} \cap B_{\bar{w}} = L_{\bar{y}} \setminus \{y_1, y_2\}$. Writing $y_1 = \bar{y} + c_1 N$ and $y_2 = \bar{y} + c_2 N$ with $c_1, c_2 \in \{0, 1, 2\}$, the three points of $L_{\bar{y}}$ sum to $3\bar{y} + 3N \equiv 3\bar{y} \pmod{3N}$. If $y_1 = y_2$ ($\mathrm{Case\;A}$), $L_{\bar{y}} \setminus \{y_1, y_2\} = L_{\bar{y}} \setminus \{y_1\}$ has size $2$ with omitted support point $y_1 = (2y_1 - y_2) \bmod 3N \in \mathrm{Case\;A}(D)$. If $y_1 \neq y_2$ ($\mathrm{Case\;B}$), $L_{\bar{y}} \setminus \{y_1, y_2\}$ is a singleton $\{y_*\}$ whose unique element satisfies $y_* \equiv 3\bar{y} - y_1 - y_2 = \bar{y} + (2\bar{y} - y_1 - y_2) \equiv \bar{y} + (2c_1 - c_2)N \equiv 2y_1 - y_2 \equiv 2y_2 - y_1 \pmod{3N}$.
- If $\min(m_D(\bar{u}), m_D(\bar{w})) = 1$ and $\max(m_D(\bar{u}), m_D(\bar{w})) \ge 1$, then $|A_{\bar{u}} \cap B_{\bar{w}}| \le \min(|A_{\bar{u}}|, |B_{\bar{w}}|) = 1$, so the child fibre has size $1$ (contributing to $\mathcal{P}_{(m_D(\bar{u}), m_D(\bar{w}))}(D)$) or $0$. If either multiplicity is $0$, $A_{\bar{u}} \cap B_{\bar{w}} = \emptyset$.

(3) Since every $2$-element child fibre arises from a unique coarse parent pair $(\bar{u}, \bar{w})$ of type $(3,2)$, $(2,3)$, or $(2,2)$ with $y_1 = y_2$, we have $S^{(1)}(T(D)) = \mathcal{M}_{(3,2)}(D) \sqcup \mathcal{M}_{(2,3)}(D) \sqcup \mathrm{Case\;A}(D)$. Now evaluate $T(J_N(D))$ where $J_N(D) = E(D) \sqcup S^{(1)}(D)$: for each child fibre $\bar{y}$ with coarse parent pair $(\bar{u}, \bar{w})$, a point $y \in L_{\bar{y}}$ belongs to $T(J_N(D))$ if and only if $y \in F_{e_{\mathrm{even}}(r)}(\pi_M^{-1}(\bar{u}) \cap J_N(D)) \cap F_{e_{\mathrm{odd}}(r)}(\pi_M^{-1}(\bar{w}) \cap J_N(D))$. Since $\pi_M^{-1}(\bar{u}) \cap J_N(D)$ is $\pi_M^{-1}(\bar{u})$ when $m_D(\bar{u}) = 3$, $\{s_{\bar{u}}\}$ when $m_D(\bar{u}) = 2$, and $\emptyset$ when $m_D(\bar{u}) \le 1$, the intersection in $L_{\bar{y}}$ is:
- all of $L_{\bar{y}}$ if $(m_D(\bar{u}), m_D(\bar{w})) = (3,3)$ (giving $E(T(D))$);
- $\{y_2\} = \{F_{e_{\mathrm{odd}}(r)}(s_{\bar{w}})\}$ if $(m_D(\bar{u}), m_D(\bar{w})) = (3,2)$ (giving $\mathcal{M}_{(3,2)}(D)$);
- $\{y_1\} = \{F_{e_{\mathrm{even}}(r)}(s_{\bar{u}})\}$ if $(m_D(\bar{u}), m_D(\bar{w})) = (2,3)$ (giving $\mathcal{M}_{(2,3)}(D)$);
- $\{y_1\} \cap \{y_2\}$ if $(m_D(\bar{u}), m_D(\bar{w})) = (2,2)$, which equals $\{y_1\}$ if $y_1 = y_2$ (giving $\mathrm{Case\;A}(D)$) and $\emptyset$ if $y_1 \neq y_2$;
- $\emptyset$ in all other cases.
Taking the union over all $\bar{y}$ gives $T(J_N(D)) = E(T(D)) \sqcup \mathcal{M}_{(3,2)}(D) \sqcup \mathcal{M}_{(2,3)}(D) \sqcup \mathrm{Case\;A}(D) = E(T(D)) \sqcup S^{(1)}(T(D)) = J_{3N}(T(D))$.

(4) Replacing $D$ by $E(D) \sqcup Q^{(2)}(D)$ deletes all $1$-element fibres of $D$ while preserving all $3$-element and $2$-element fibres verbatim. By the $4 \times 4$ transition table, this preserves $E(T(D))$, $Q^{(2)}(T(D))$, and $\mathrm{Case\;B}(D) = Q^{(1,\mathrm{new})}(T(D))$ while eliminating all five propagated singleton classes $\mathcal{P}_{(a,b)}(D)$ with $\min(a,b) = 1$. $\blacksquare$

---

## 4. Three-Stage Extinction Cascade and Exact Horizons for $k \in \{2, 3, 4, 5, 6\}$

For each initial exponent $k \ge 2$ and step $j \ge 0$, let $M_j = 3^{k-1+j}$ and $N_j = 3^{k+j}$, and decompose the reachable missing set $D_{k,j} \subseteq \mathbb{Z}/N_j\mathbb{Z}$ along $\pi_{M_j}$ into $E_j := E(D_{k,j})$, $Q_j^{(2)} := Q^{(2)}(D_{k,j})$, $Q_j^{(1)} := Q^{(1)}(D_{k,j})$, $S_j^{(1)} := S^{(1)}(D_{k,j})$, and $Z_j := J_{N_j}(D_{k,j}) = E_j \sqcup S_j^{(1)}$. Adopting the standard convention $\inf \emptyset = +\infty$ when extinction is not yet established, define the three extinction horizons in $\mathbb{Z}_{\ge 0} \cup \{+\infty\}$ by
$$j_E^*(k) := \inf\{j \ge 0 : E_j = \emptyset\}, \qquad j_Z^*(k) := \inf\{j \ge 0 : Z_j = \emptyset\}, \qquad j_D^*(k) := \inf\{j \ge 0 : D_{k,j} = \emptyset\}.$$

### Theorem 4.1 (Universal Cascade Ordering and Post-Stage-1 / Post-Stage-2 Collapse Laws)
For every $k \ge 2$:
1. **Exact Coarse-Fibre Projection and Universal Horizon Ordering**: At every step $j \ge 0$, the full-fibre stratum $E(D_{k,j})$ is the $3$-fold cylinder lift of $D_{k-1,j}$:
   $$E(D_{k,j}) = \pi_{M_j}^{-1}(D_{k-1,j}), \qquad |E(D_{k,j})| = 3|D_{k-1,j}|.$$
   Consequently, $E(D_{k,j}) = \emptyset \iff D_{k-1,j} = \emptyset$, so in $\mathbb{Z}_{\ge 0} \cup \{+\infty\}$,
   $$j_E^*(k) = j_D^*(k-1) \quad (k \ge 3), \qquad \text{and} \qquad j_E^*(k) \le j_Z^*(k) \le j_D^*(k) \quad (k \ge 2).$$
2. **Post-Stage-1 Collapse Law ($j \ge j_E^*(k)$)**: Whenever $j_E^*(k) < +\infty$, for all $j \ge j_E^*(k)$ no coarse fibre has multiplicity $3$, so $\mathcal{M}_{(3,2)}(D_{k,j}) = \mathcal{M}_{(2,3)}(D_{k,j}) = \mathcal{P}_{(3,1)}(D_{k,j}) = \mathcal{P}_{(1,3)}(D_{k,j}) = \emptyset$, and
   $$S^{(1)}(D_{k,j+1}) = \mathrm{Case\;A}(D_{k,j}), \qquad |Q^{(2)}(D_{k,j+1})| = 2|\mathrm{Case\;A}(D_{k,j})|.$$
3. **Post-Stage-2 Collapse Law ($j \ge j_Z^*(k)$)**: Whenever $j_Z^*(k) < +\infty$, for all $j \ge j_Z^*(k)$ the missing set $D_{k,j} = Q^{(1)}(D_{k,j})$ consists exclusively of $1$-element coarse fibres, $\mathrm{Case\;A}(D_{k,j}) = \mathrm{Case\;B}(D_{k,j}) = \emptyset$, and the next missing set is generated purely by $(1,1)$ singleton-singleton propagation:
   $$D_{k,j+1} = Q^{(1,\mathrm{prop})}(D_{k,j+1}) = \mathcal{P}_{(1,1)}(D_{k,j}).$$

*Proof.*
(1) At $j = 0$, $A_0 \bmod N_0$ has $3$ elements projecting to the $3$ distinct elements of $A_0 \bmod M_0$ ($k \ge 3$; for $k = 2$, $A_0 \bmod 9 = \{0, 2, 7\}$ hits all $3$ cosets mod $3$, so $D_{1,0} = \emptyset$ and $E(D_{2,0}) = \emptyset$). Thus $\pi_{M_0}^{-1}(D_{k-1,0}) = E(D_{k,0})$. By Theorem 3.2(1), $E(T(D)) = T(E(D)) = \pi_{M_{j+1}}^{-1}(T(D_{k-1,j})) = \pi_{M_{j+1}}^{-1}(D_{k-1,j+1})$, proving $E(D_{k,j}) = \pi_{M_j}^{-1}(D_{k-1,j})$ for all $j \ge 0$. Hence $j_E^*(k) = j_D^*(k-1)$. Since $E_j \subseteq Z_j$ and $E_j \sqcup Q_j^{(2)} \subseteq D_{k,j}$ (with $|Q_j^{(2)}| = 2|S_j^{(1)}|$), $Z_j = \emptyset \implies E_j = \emptyset$ and $D_{k,j} = \emptyset \implies E_j = Q_j^{(2)} = \emptyset \implies Z_j = \emptyset$, giving $j_E^*(k) \le j_Z^*(k) \le j_D^*(k)$ in $\mathbb{Z}_{\ge 0} \cup \{+\infty\}$.
(2) and (3) follow immediately from the $4 \times 4$ transition table of Theorem 3.2(1) upon setting $m_D(\cdot) \le 2$ (for $j \ge j_E^*(k)$) and $m_D(\cdot) \le 1$ (for $j \ge j_Z^*(k)$). $\blacksquare$

---

### Theorem 4.2 (Exact Three-Stage Extinction Horizons and Cascade Profiles for $k \in \{2, 3, 4, 5, 6\}$)
1. Across the verified finite range $k \in \{2, 3, 4, 5, 6\}$ (reaching modulus $3^{19} = 1{,}162{,}261{,}467$ at $(k,j) = (6,13)$), the three extinction horizons are finite, satisfy the strict three-stage inequality $j_E^*(k) < j_Z^*(k) < j_D^*(k)$, and for $k \in \{3, 4, 5, 6\}$ obey $(j_E^*(k), j_Z^*(k), j_D^*(k)) = (2k-1, 2k, 2k+1)$:

| Seed Level $k$ | Initial Modulus $3^k$ | Stage 1: $j_E^*(k)$ ($E_j = \emptyset$) | Stage 2: $j_Z^*(k)$ ($Z_j = \emptyset$) | Stage 3: $j_D^*(k)$ ($D_{k,j} = \emptyset$) | Terminal Modulus $3^{k+j_D^*(k)}$ | Peak Missing Size $\max_j |D_{k,j}|$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $k = 2$ | $9$ | $0$ | $3$ | $5$ | $3^7 = 2{,}187$ | $20$ (at $j = 2$) |
| $k = 3$ | $27$ | $5$ | $6$ | $7$ | $3^{10} = 59{,}049$ | $386$ (at $j = 4$) |
| $k = 4$ | $81$ | $7$ | $8$ | $9$ | $3^{13} = 1{,}594{,}323$ | $5{,}940$ (at $j = 5$) |
| $k = 5$ | $243$ | $9$ | $10$ | $11$ | $3^{16} = 43{,}046{,}721$ | $128{,}008$ (at $j = 7$) |
| $k = 6$ | $729$ | $11$ | $12$ | $13$ | $3^{19} = 1{,}162{,}261{,}467$ | $2{,}256{,}422$ (at $j = 9$) |

2. For $k = 2$, the tuples $(j, |D_{2,j}|, |E_j|, |Q_j^{(2)}|, |Q_j^{(1)}|, |S_j^{(1)}|, |Z_j|)$ for $j = 0 \dots 5$ are $(0, 6, 0, 6, 0, 3, 3)$, $(1, 12, 0, 6, 6, 3, 3)$, $(2, 20, 0, 4, 16, 2, 2)$, $(3, 13, 0, 0, 13, 0, 0)$, $(4, 1, 0, 0, 1, 0, 0)$, and $(5, 0, 0, 0, 0, 0, 0)$. The complete step-by-step coarse-fibre and $4 \times 4$ transition tables for $k = 3, 4, 5$ (where $|\mathcal{M}_{\mathrm{mix}}| := |\mathcal{M}_{(3,2)}(D_{k,j})| + |\mathcal{M}_{(2,3)}(D_{k,j})|$) are given by:

#### Table 4.2A: Complete Cascade for $k = 3$ ($j = 0 \dots 7$)
| Step $j$ | Modulus $3^{3+j}$ | $|D_{3,j}|$ | $|E_j|$ | $|Q_j^{(2)}|$ | $|Q_j^{(1)}|$ | $|S_j^{(1)}|$ | $|Z_j|$ | $|\mathcal{M}_{\mathrm{mix}}|$ | $\mathrm{Case\;A}$ | $\mathrm{Case\;B} = |Q_{j+1}^{(1,\mathrm{new})}|$ | $|Q_{j+1}^{(1,\mathrm{prop})}|$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $27$ | $24$ | $18$ | $6$ | $0$ | $3$ | $21$ | $12$ | $2$ | $1$ | $0$ |
| $1$ | $81$ | $65$ | $36$ | $28$ | $1$ | $14$ | $50$ | $30$ | $13$ | $14$ | $2$ |
| $2$ | $243$ | $162$ | $60$ | $86$ | $16$ | $43$ | $103$ | $70$ | $20$ | $46$ | $50$ |
| $3$ | $729$ | $315$ | $39$ | $180$ | $96$ | $90$ | $129$ | $36$ | $30$ | $54$ | $197$ |
| $4$ | $2{,}187$ | $386$ | $3$ | $132$ | $251$ | $66$ | $69$ | $0$ | $11$ | $10$ | $148$ |
| $5$ ($j_E^*$) | $6{,}561$ | $180$ | **$0$** | $22$ | $158$ | $11$ | $11$ | $0$ | $0$ | $0$ | $10$ |
| $6$ ($j_Z^*$) | $19{,}683$ | $10$ | $0$ | **$0$** | $10$ | **$0$** | **$0$** | $0$ | $0$ | $0$ | $0$ |
| $7$ ($j_D^*$) | $59{,}049$ | **$0$** | $0$ | $0$ | $0$ | $0$ | $0$ | — | — | — | — |

#### Table 4.2B: Complete Cascade for $k = 4$ ($j = 0 \dots 9$)
| Step $j$ | Modulus $3^{4+j}$ | $|D_{4,j}|$ | $|E_j|$ | $|Q_j^{(2)}|$ | $|Q_j^{(1)}|$ | $|S_j^{(1)}|$ | $|Z_j|$ | $|\mathcal{M}_{\mathrm{mix}}|$ | $\mathrm{Case\;A}$ | $\mathrm{Case\;B} = |Q_{j+1}^{(1,\mathrm{new})}|$ | $|Q_{j+1}^{(1,\mathrm{prop})}|$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $81$ | $78$ | $72$ | $6$ | $0$ | $3$ | $75$ | $14$ | $2$ | $0$ | $0$ |
| $1$ | $243$ | $227$ | $195$ | $32$ | $0$ | $16$ | $211$ | $66$ | $2$ | $13$ | $0$ |
| $2$ | $729$ | $635$ | $486$ | $136$ | $13$ | $68$ | $554$ | $283$ | $12$ | $42$ | $71$ |
| $3$ | $2{,}187$ | $1{,}648$ | $945$ | $590$ | $113$ | $295$ | $1{,}240$ | $775$ | $105$ | $253$ | $478$ |
| $4$ | $6{,}561$ | $3{,}649$ | $1{,}158$ | $1{,}760$ | $731$ | $880$ | $2{,}038$ | $914$ | $353$ | $731$ | $2{,}135$ |
| $5$ | $19{,}683$ | $5{,}940$ | $540$ | $2{,}534$ | $2{,}866$ | $1{,}267$ | $1{,}807$ | $231$ | $234$ | $468$ | $3{,}871$ |
| $6$ | $59{,}049$ | $5{,}299$ | $30$ | $930$ | $4{,}339$ | $465$ | $495$ | $0$ | $6$ | $9$ | $1{,}413$ |
| $7$ ($j_E^*$) | $177{,}147$ | $1{,}434$ | **$0$** | $12$ | $1{,}422$ | $6$ | $6$ | $0$ | $0$ | $0$ | $32$ |
| $8$ ($j_Z^*$) | $531{,}441$ | $32$ | $0$ | **$0$** | $32$ | **$0$** | **$0$** | $0$ | $0$ | $0$ | $0$ |
| $9$ ($j_D^*$) | $1{,}594{,}323$ | **$0$** | $0$ | $0$ | $0$ | $0$ | $0$ | — | — | — | — |

#### Table 4.2C: Complete Cascade for $k = 5$ ($j = 0 \dots 11$)
| Step $j$ | Modulus $3^{5+j}$ | $|D_{5,j}|$ | $|E_j|$ | $|Q_j^{(2)}|$ | $|Q_j^{(1)}|$ | $|S_j^{(1)}|$ | $|Z_j|$ | $|\mathcal{M}_{\mathrm{mix}}|$ | $\mathrm{Case\;A}$ | $\mathrm{Case\;B} = |Q_{j+1}^{(1,\mathrm{new})}|$ | $|Q_{j+1}^{(1,\mathrm{prop})}|$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $243$ | $240$ | $234$ | $6$ | $0$ | $3$ | $237$ | $14$ | $2$ | $0$ | $0$ |
| $1$ | $729$ | $713$ | $681$ | $32$ | $0$ | $16$ | $697$ | $92$ | $2$ | $0$ | $0$ |
| $2$ | $2{,}187$ | $2{,}093$ | $1{,}905$ | $188$ | $0$ | $94$ | $1{,}999$ | $514$ | $10$ | $15$ | $0$ |
| $3$ | $6{,}561$ | $6{,}007$ | $4{,}944$ | $1{,}048$ | $15$ | $524$ | $5{,}468$ | $2{,}518$ | $121$ | $183$ | $83$ |
| $4$ | $19{,}683$ | $16{,}491$ | $10{,}947$ | $5{,}278$ | $266$ | $2{,}639$ | $13{,}586$ | $9{,}042$ | $1{,}060$ | $2{,}026$ | $1{,}363$ |
| $5$ | $59{,}049$ | $41{,}413$ | $17{,}820$ | $20{,}204$ | $3{,}389$ | $10{,}102$ | $27{,}922$ | $18{,}276$ | $5{,}242$ | $10{,}310$ | $13{,}782$ |
| $6$ | $177{,}147$ | $87{,}025$ | $15{,}897$ | $47{,}036$ | $24{,}092$ | $23{,}518$ | $39{,}415$ | $12{,}279$ | $9{,}522$ | $18{,}452$ | $61{,}652$ |
| $7$ | $531{,}441$ | $128{,}008$ | $4{,}302$ | $43{,}602$ | $80{,}104$ | $21{,}801$ | $26{,}103$ | $1{,}036$ | $2{,}597$ | $5{,}314$ | $79{,}776$ |
| $8$ | $1{,}594{,}323$ | $92{,}452$ | $96$ | $7{,}266$ | $85{,}090$ | $3{,}633$ | $3{,}729$ | $2$ | $29$ | $47$ | $15{,}647$ |
| $9$ ($j_E^*$) | $4{,}782{,}969$ | $15{,}756$ | **$0$** | $62$ | $15{,}694$ | $31$ | $31$ | $0$ | $0$ | $0$ | $153$ |
| $10$ ($j_Z^*$) | $14{,}348{,}907$ | $153$ | $0$ | **$0$** | $153$ | **$0$** | **$0$** | $0$ | $0$ | $0$ | $0$ |
| $11$ ($j_D^*$) | $43{,}046{,}721$ | **$0$** | $0$ | $0$ | $0$ | $0$ | $0$ | — | — | — | — |

3. **Complete Coarse-Fibre Profile for $k = 6$ ($j = 0 \dots 13$)**: At $k = 6$, the coarse-fibre tuples $(j, |D_{6,j}|, |E_j|, |Q_j^{(2)}|, |Q_j^{(1)}|, |S_j^{(1)}|)$ across $j = 0 \dots 13$ satisfy $|E(D_{6,j})| = 3|D_{5,j}|$ at every step and are given by:
   - $j = 0 \dots 4$: $(0, 726, 720, 6, 0, 3)$, $(1, 2{,}171, 2{,}139, 32, 0, 16)$, $(2, 6{,}467, 6{,}279, 188, 0, 94)$, $(3, 19{,}126, 18{,}021, 1{,}102, 3, 551)$, $(4, 55{,}766, 49{,}473, 6{,}202, 91, 3{,}101)$;
   - $j = 5 \dots 9$: $(5, 158{,}018, 124{,}239, 32{,}342, 1{,}437, 16{,}171)$, $(6, 422{,}866, 261{,}075, 145{,}356, 16{,}435, 72{,}678)$, $(7, 1{,}008{,}164, 384{,}024, 487{,}358, 136{,}782, 243{,}679)$, $(8, 1{,}903{,}841, 277{,}356, 919{,}706, 706{,}779, 459{,}853)$, $(9, 2{,}256{,}422, 47{,}268, 575{,}860, 1{,}633{,}294, 287{,}930)$;
   - $j = 10$: $(10,\, 1{,}056{,}601,\, 459,\, 44{,}928,\, 1{,}011{,}214,\, 22{,}464)$ (with $|E_{10}| = 3|D_{5,10}| = 3 \times 153 = 459$);
   - $j = 11$ ($j_E^*(6) = 11$): $(11,\, 77{,}399,\, 0,\, 34,\, 77{,}365,\, 17)$;
   - $j = 12$ ($j_Z^*(6) = 12$): $(12,\, 103,\, 0,\, 0,\, 103,\, 0)$;
   - $j = 13$ ($j_D^*(6) = 13$): $(13,\, 0,\, 0,\, 0,\, 0,\, 0)$.

*Proof.* Every row of Tables 4.2, 4.2A, 4.2B, 4.2C, and the $k = 2, 6$ profiles is explicitly asserted and verified by exact integer set evolution in `verify_section4()` of `verify_paper17.py`. $\blacksquare$

---

## 5. Two-Channel Rational Coincidences, the $j = 7$ $K$-Channel Transition, and Collision-Valuation Transfer on $G_j \subset \mathbb{Z}_{(3)}$

In `collatz_39/v2` ([5], Section 2, Theorem 4), `u/cassian_mahler` introduced the $k$-independent dyadic good tree $U_j \subset \mathbb{Z}[1/2] \subset \mathbb{Z}_{(3)}$ representing $1 + 3S_{k,j}$ prior to modular reduction and computed its sizes through $j = 5$. Passing to the reduced coordinates $G_j := (U_j - 1)/3 \subset \mathbb{Z}[1/2] \subset \mathbb{Z}_{(3)}$, the tree $G_j$ starts from
$$G_0 = \left\{0,\, -\frac{1}{4},\, -\frac{5}{16}\right\} \subset \mathbb{Z}[1/2], \qquad G_{j+1} = \bigcup_{e=1}^6 F_e^{\mathbb{Q}}(G_j), \qquad F_e^{\mathbb{Q}}(g) := \frac{3g - c_e}{2^e}.$$
For every $k \ge 2$ and $j \ge 0$, reducing $G_j$ modulo $N_j = 3^{k+j}$ recovers the absorbed support $S_{k,j} = (G_j \bmod 3^{k+j})$. Clearing dyadic denominators via $\widetilde{G}_j := 2^{4+6j} G_j \subset \mathbb{Z}_{\le 0}$ represents every element of $G_j$ as an exact non-positive integer.

### Theorem 5.1 (Two-Channel Rational Coincidence Law and the $j = 7$ $K$-Channel Phase Transition)
For every $j \ge 0$, let $K^{\mathbb{Q}}(g) = 32g + 7$ and $H^{\mathbb{Q}}(g) = 2g$ on $\mathbb{Q}$. For each active residue channel $r \in \{0, 1, 2\}$ with branch pair $(e_{\mathrm{even}}(r), e_{\mathrm{odd}}(r))$, the rational branch differences for $(g, h) \in G_j^2$ satisfy the exact pointwise identities
$$F_6^{\mathbb{Q}}(h) - F_1^{\mathbb{Q}}(g) = \frac{3\big(h - (32g + 7)\big)}{64} \quad (r = 0),$$
$$F_4^{\mathbb{Q}}(g) - F_5^{\mathbb{Q}}(h) = \frac{3(2g - h)}{32} \quad (r = 1), \qquad F_2^{\mathbb{Q}}(g) - F_3^{\mathbb{Q}}(h) = \frac{3(2g - h)}{8} \quad (r = 2).$$
1. **Universal Two-Channel Rational Coincidence Law**: Two branch images $F_e^{\mathbb{Q}}(g)$ and $F_{e'}^{\mathbb{Q}}(h)$ ($g, h \in G_j$, $e \neq e'$) coincide in $\mathbb{Q}$ if and only if either $\{e, e'\} = \{1, 6\}$ with $F_1^{\mathbb{Q}}(g) = F_6^{\mathbb{Q}}(h) \iff h = 32g + 7 = K^{\mathbb{Q}}(g)$, or $\{e, e'\} \in \{\{2, 3\}, \{4, 5\}\}$ with $F_{e_{\mathrm{even}}(r)}^{\mathbb{Q}}(g) = F_{e_{\mathrm{odd}}(r)}^{\mathbb{Q}}(h) \iff h = 2g = H^{\mathbb{Q}}(g)$. Defining the ordered channel coincidence counts
   $$A_\infty^{(K)}(j) := \big|\{g \in G_j : 32g + 7 \in G_j\}\big|, \qquad A_\infty^{(H)}(j) := \big|\{g \in G_j : 2g \in G_j\}\big|,$$
   the total number of branch coincidences at step $j$ and the tree cardinality at step $j + 1$ satisfy for all $j \ge 0$:
   $$A_\infty(j) = A_\infty^{(K)}(j) + 2A_\infty^{(H)}(j), \qquad |G_{j+1}| = 6|G_j| - A_\infty(j).$$
2. **$H$-Channel Exclusivity for $0 \le j \le 6$ and the $j = 7$ $K$-Channel Phase Transition**: For $0 \le j \le 6$, $A_\infty^{(K)}(j) = 0$ holds identically ($K^{\mathbb{Q}}(G_j) \cap G_j = \emptyset$), with $A_\infty^{(H)}(j) = (1, 1, 2, 6, 19, 81, 309)$ and $A_\infty(j) = (2, 2, 4, 12, 38, 162, 618)$. At **$j = 7$** ($|G_7| = 720{,}210$), the $K$-channel becomes active for the first time with **$A_\infty^{(K)}(7) = 4$** ordered $K$-coincidences alongside **$A_\infty^{(H)}(7) = 1{,}245$** ordered $H$-coincidences, yielding
   $$A_\infty(7) = 4 + 2(1{,}245) = 2{,}494, \qquad |G_8| = 6(720{,}210) - 2{,}494 = 4{,}318{,}766.$$
3. **Complete Classification of the $4$ $K$-Channel Collisions in $G_7$**: Necessary conditions for $h = 32g + 7 \in G_j$ are $g < -7/32 = -0.21875$ (since $h < 0$) and $\nu_2(\mathrm{den}(g)) - \nu_2(\mathrm{den}(h)) = 5$. At $j = 7$, the $4$ ordered pairs $(g, h) \in G_7^2$ satisfying $32g + 7 = h$ (and hence $F_1^{\mathbb{Q}}(g) = F_6^{\mathbb{Q}}(h)$) are given with their chronological $7$-step branch words from $G_0$ by:

| Pair # | $g \in G_7$ | Root $g_0$ & Branch Word $w_g \in \{1,\dots,6\}^7$ | $h = 32g + 7 \in G_7$ | Root $h_0$ & Branch Word $w_h \in \{1,\dots,6\}^7$ | Common Child $F_1^{\mathbb{Q}}(g) = F_6^{\mathbb{Q}}(h) \in G_8$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $-\frac{51{,}271}{131{,}072}$ | $0,\; (1, 2, 4, 1, 3, 3, 4)$ | $-\frac{22{,}599}{4{,}096}$ | $-\frac{5}{16},\; (2, 1, 1, 1, 1, 1, 1)$ | $-\frac{153{,}813}{262{,}144}$ |
| $2$ | $-\frac{25{,}271}{65{,}536}$ | $0,\; (1, 1, 1, 6, 3, 3, 4)$ | $-\frac{10{,}935}{2{,}048}$ | $-\frac{5}{16},\; (1, 1, 1, 1, 1, 1, 1)$ | $-\frac{75{,}813}{131{,}072}$ |
| $3$ | $-\frac{91{,}607}{262{,}144}$ | $0,\; (1, 2, 2, 1, 4, 4, 5)$ | $-\frac{34{,}263}{8{,}192}$ | $-\frac{5}{16},\; (3, 1, 1, 1, 1, 1, 1)$ | $-\frac{274{,}821}{524{,}288}$ |
| $4$ | $-\frac{11{,}299}{32{,}768}$ | $0,\; (1, 1, 1, 2, 3, 5, 5)$ | $-\frac{4{,}131}{1{,}024}$ | $-\frac{1}{4},\; (1, 2, 1, 1, 1, 1, 1)$ | $-\frac{33{,}897}{65{,}536}$ |

*Proof.*
(1) For any $g, h \in \mathbb{Z}_{(3)}$, $F_e^{\mathbb{Q}}(g) \equiv F_e(g) \pmod{3}$ lies in the residue class $0 \pmod{3}$ for $e \in \{1, 6\}$, $2 \pmod{3}$ for $e \in \{2, 3\}$, and $1 \pmod{3}$ for $e \in \{4, 5\}$. Thus $F_e^{\mathbb{Q}}(g) = F_{e'}^{\mathbb{Q}}(h)$ with $e \neq e'$ requires $\{e, e'\} \in \{\{1, 6\}, \{2, 3\}, \{4, 5\}\}$, and the three displayed algebraic difference formulas immediately yield $h = 32g + 7$ for $\{1, 6\}$ and $h = 2g$ for $\{2, 3\}$ and $\{4, 5\}$. Since each branch $F_e^{\mathbb{Q}}$ is injective on $G_j$ and the three residue classes mod $3$ are disjoint, $|G_{j+1}| = \sum_{r=0}^2 |F_{e_{\mathrm{even}}(r)}^{\mathbb{Q}}(G_j) \cup F_{e_{\mathrm{odd}}(r)}^{\mathbb{Q}}(G_j)| = 6|G_j| - (A_\infty^{(K)}(j) + 2A_\infty^{(H)}(j))$. Parts (2) and (3) are verified by exact integer enumeration and rational word evaluation in `verify_section5()` of `verify_paper17.py`. $\blacksquare$

---

To determine the exact modulus $M_j = 3^{k-1+j}$ above which the modular projection $G_j \to S_{k,j} \subseteq \mathbb{Z}/3^{k+j}\mathbb{Z}$ becomes injective on coarse fibres (and to predict $\mathrm{Case\;A}(D_{k,j})$ and $\mathrm{Case\;B}(D_{k,j})$ directly from $3$-adic valuations in $\mathbb{Z}_{(3)}$), we define the **maximum intra-tree collision valuation** $V_{\mathrm{fibre}}(j)$ and the **maximum partner-collision valuation** $V_{\mathrm{partner}}(j)$:
$$V_{\mathrm{fibre}}(j) := \max_{\substack{g, h \in G_j \\ g \neq h}} v_3(g - h),$$
$$V_{\mathrm{partner}}(j) := \max_{r \in \{0,1,2\}} \;\max_{\substack{g, h \in G_j \\ F_{e_{\mathrm{even}}(r)}^{\mathbb{Q}}(g) \neq F_{e_{\mathrm{odd}}(r)}^{\mathbb{Q}}(h)}} v_3\Big(F_{e_{\mathrm{even}}(r)}^{\mathbb{Q}}(g) - F_{e_{\mathrm{odd}}(r)}^{\mathbb{Q}}(h)\Big) - 1.$$
By the identities of Theorem 5.1, the inner quantity equals $v_3(g - (32h + 7)) = v_3(32h + 7 - g)$ for $r = 0$ and $v_3(2g - h)$ for $r \in \{1, 2\}$, so
$$V_{\mathrm{partner}}(j) = \max\left(\max_{\substack{g, h \in G_j \\ 32g + 7 \neq h}} v_3(32g + 7 - h),\; \max_{\substack{g, h \in G_j \\ 2g \neq h}} v_3(2g - h)\right).$$

### Theorem 5.2 (Collision-Valuation Transfer Identity and Extremal Rational Witnesses through $j = 7$)
1. **Exact Valuation Transfer Identity**: For every $j \ge 0$, the intra-tree collision valuation at step $j + 1$ is governed by the exact transfer recurrence
   $$V_{\mathrm{fibre}}(j + 1) = \max\big(V_{\mathrm{fibre}}(j),\, V_{\mathrm{partner}}(j)\big) + 1.$$
2. **Exact Invariants through $j = 7$ and $V_{\mathrm{fibre}}(8) = 23$**: Across $0 \le j \le 7$, the partner-collision valuation satisfies $V_{\mathrm{partner}}(j) \ge V_{\mathrm{fibre}}(j)$, so $V_{\mathrm{fibre}}(j+1) = V_{\mathrm{partner}}(j) + 1$, with exact values:

| Step $j$ | $|G_j|$ | $A_\infty^{(K)}(j)$ | $A_\infty^{(H)}(j)$ | $A_\infty(j)$ | $V_{\mathrm{fibre}}(j)$ | $V_{\mathrm{partner}}(j)$ | $V_{\mathrm{fibre}}(j+1)$ | Stabilization $k_{\mathrm{stab}}(j) = V_{\mathrm{fibre}}(j) + 2 - j$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $3$ | $0$ | $1$ | $2$ | $0$ | $2$ | $3$ | $2$ |
| $1$ | $16$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $4$ |
| $2$ | $94$ | $0$ | $2$ | $4$ | $5$ | $9$ | $10$ | $5$ |
| $3$ | $560$ | $0$ | $6$ | $12$ | $10$ | $12$ | $13$ | $9$ |
| $4$ | $3{,}348$ | $0$ | $19$ | $38$ | $13$ | $13$ | $14$ | $11$ |
| $5$ | $20{,}050$ | $0$ | $81$ | $162$ | $14$ | $16$ | $17$ | $11$ |
| $6$ | $120{,}138$ | $0$ | $309$ | $618$ | $17$ | $18$ | $19$ | $13$ |
| $7$ | $720{,}210$ | **$4$** | $1{,}245$ | $2{,}494$ | $19$ | $22$ | **$23$** | $14$ |

3. **Explicit Extremal Rational Witness Pairs ($0 \le j \le 7$)**: Writing the reduced odd numerator of each extremal difference as $\pm 3^V u_{\mathrm{odd}}$, the maxima $V_{\mathrm{fibre}}(j)$ and $V_{\mathrm{partner}}(j)$ for $0 \le j \le 7$ are attained by the following exact pairs $(g, h) \in G_j^2$:
   - **Intra-tree witnesses $v_3(g - h) = V_{\mathrm{fibre}}(j)$**:
     - $j = 0$: $(0,\, -1/4)$, $|g - h| = 1/2^2$, $v_3 = 0$, $u_{\mathrm{odd}} = 1$;
     - $j = 1$: $(-351/1024,\, 0)$, $|g - h| = 3^3 \cdot 13 / 2^{10}$, $v_3 = 3$, $u_{\mathrm{odd}} = 13$;
     - $j = 2$: $(-3/8,\, -2829/8192)$, $|g - h| = 3^5 / 2^{13}$, $v_3 = 5$, $u_{\mathrm{odd}} = 1$;
     - $j = 3$: $(-591/1024,\, -92247/262144)$, $|g - h| = 3^{10} / 2^{18}$, $v_3 = 10$, $u_{\mathrm{odd}} = 1$;
     - $j = 4$: $(-8757/16384,\, -2889261/8388608)$, $|g - h| = 3^{13} / 2^{23}$, $v_3 = 13$, $u_{\mathrm{odd}} = 1$;
     - $j = 5$: $(-26271/32768,\, -8667783/16777216)$, $|g - h| = 3^{14} / 2^{24}$, $v_3 = 14$, $u_{\mathrm{odd}} = 1$;
     - $j = 6$: $(-8884773165/17179869184,\, -739318677/2147483648)$, $|g - h| = 3^{17} \cdot 23 / 2^{34}$, $v_3 = 17$, $u_{\mathrm{odd}} = 23$;
     - $j = 7$: $(-1469375/2097152,\, -26065512127/68719476736)$, $|g - h| = 3^{19} \cdot 19 / 2^{36}$, $v_3 = 19$, $u_{\mathrm{odd}} = 19$.
   - **Partner-collision witnesses $v_3(P^{\mathbb{Q}}(g) - h) = V_{\mathrm{partner}}(j)$**:
     - $j = 0$ ($K$): $(0,\, -5/16)$, $|32g + 7 - h| = 3^2 \cdot 13 / 2^4$, $v_3 = 2$, $u_{\mathrm{odd}} = 13$;
     - $j = 1$ ($H$): $(-21/64,\, -87/256)$, $|2g - h| = 3^4 / 2^8$, $v_3 = 4$, $u_{\mathrm{odd}} = 1$;
     - $j = 2$ ($K$): $(-389/1024,\, -1437/4096)$, $|32g + 7 - h| = 3^9 / 2^{12}$, $v_3 = 9$, $u_{\mathrm{odd}} = 1$;
     - $j = 3$ ($K$): $(-2919/8192,\, -45583/131072)$, $|32g + 7 - h| = 3^{12} / 2^{17}$, $v_3 = 12$, $u_{\mathrm{odd}} = 1$;
     - $j = 4$ ($H$): $(-5997/16384,\, -1476141/4194304)$, $|2g - h| = 3^{13} / 2^{22}$, $v_3 = 13$, $u_{\mathrm{odd}} = 1$;
     - $j = 5$ ($K$): $(-2961591055/8589934592,\, -11558535/33554432)$, $|32g + 7 - h| = 3^{16} \cdot 23 / 2^{28}$, $v_3 = 16$, $u_{\mathrm{odd}} = 23$;
     - $j = 6$ ($K$): $(-345749/524288,\, -210417557/536870912)$, $|32g + 7 - h| = 3^{18} \cdot 19 / 2^{29}$, $v_3 = 18$, $u_{\mathrm{odd}} = 19$;
     - $j = 7$ ($K$): $(-1501127/2097152,\, -13026690647/34359738368)$, $|32g + 7 - h| = 3^{22} \cdot 17 / 2^{35}$, $v_3 = 22$, $u_{\mathrm{odd}} = 17$.

*Proof.*
(1) Every pair of distinct elements $y, y' \in G_{j+1}$ is of the form $y = F_e^{\mathbb{Q}}(g)$ and $y' = F_{e'}^{\mathbb{Q}}(h)$ with $g, h \in G_j$. If $y \not\equiv y' \pmod{3}$, then $v_3(y - y') = 0$. If $y \equiv y' \equiv r \pmod{3}$, then $e, e' \in \{e_{\mathrm{even}}(r), e_{\mathrm{odd}}(r)\}$.
- If $e = e'$, then $y - y' = 3(g - h)2^{-e}$ with $g \neq h$, so $v_3(y - y') = v_3(g - h) + 1$, whose maximum over $g \neq h$ in $G_j$ is $V_{\mathrm{fibre}}(j) + 1$.
- If $\{e, e'\} = \{e_{\mathrm{even}}(r), e_{\mathrm{odd}}(r)\}$, then $v_3(y - y')$ with $y \neq y'$ has maximum $V_{\mathrm{partner}}(j) + 1$ by definition of $V_{\mathrm{partner}}(j)$.
Taking the maximum over both cases gives $V_{\mathrm{fibre}}(j+1) = \max(V_{\mathrm{fibre}}(j), V_{\mathrm{partner}}(j)) + 1$. Parts (2) and (3) are verified by exact radix-tree bucket partitioning, mod-$3^{v+1}$ injectivity verification, and `Fraction` arithmetic in `verify_section5()` of `verify_paper17.py`. $\blacksquare$

---

### Theorem 5.3 ($O(|G_j|)$ $k$-Independent Sparse Seed-Reduction and High-$k$ Stabilization)
Let $j \ge 0$ and $k \ge 2$, with $M = 3^{k-1+j}$ and $N = 3^{k+j}$.
1. **$O(|G_j|)$ Sparse Computation of Coarse-Fibre and $\mathbb{F}_3$-Affine Invariants**: Let $S_{k,j} = (G_j \bmod N)$, and for $m \in \{1, 2, 3\}$ let $c_m(k,j)$ denote the number of coarse fibres $\bar{u} \in \mathbb{Z}/M\mathbb{Z}$ with $|\pi_M^{-1}(\bar{u}) \cap S_{k,j}| = m$, and $c_0(k,j) = M - (c_1(k,j) + c_2(k,j) + c_3(k,j))$. Then
   $$|E(D_{k,j})| = 3c_0(k,j), \qquad |Q^{(2)}(D_{k,j})| = 2c_1(k,j), \qquad |Q^{(1)}(D_{k,j})| = c_2(k,j), \qquad |S^{(1)}(D_{k,j})| = c_1(k,j),$$
   and $S^{(1)}(D_{k,j})$ consists precisely of the elements of $S_{k,j}$ lying in $1$-element buckets of $S_{k,j} \bmod M$. Thus $|E(D_{k,j})|$, $|Q^{(2)}(D_{k,j})|$, $|Q^{(1)}(D_{k,j})|$, $|S^{(1)}(D_{k,j})|$, $|\mathrm{Case\;A}(D_{k,j})|$, and $|\mathrm{Case\;B}(D_{k,j})|$ can be computed in $O(|G_j|)$ time and space directly from $\widetilde{G}_j$, independent of the ambient ring size $3^{k+j}$.
2. **Exact High-$k$ Stabilization Formula**: Whenever $k - 1 + j > V_{\mathrm{fibre}}(j)$ (i.e., $k \ge k_{\mathrm{stab}}(j) := V_{\mathrm{fibre}}(j) + 2 - j$), the reduction map $G_j \to \mathbb{Z}/M\mathbb{Z}$ is injective. In this regime, $c_1(k,j) = |G_j|$, $c_2(k,j) = c_3(k,j) = 0$, and
   $$|E(D_{k,j})| = 3^{k+j} - 3|G_j|, \qquad |Q^{(2)}(D_{k,j})| = 2|G_j|, \qquad |Q^{(1)}(D_{k,j})| = 0, \qquad |S^{(1)}(D_{k,j})| = |G_j|.$$
   Moreover, letting $H_{\mathrm{partner}}^{(j)}(\nu)$ denote the number of ordered distinct-branch pairs $(g, h) \in G_j^2$ across $r \in \{0, 1, 2\}$ with $v_3(F_{e_{\mathrm{even}}(r)}^{\mathbb{Q}}(g) - F_{e_{\mathrm{odd}}(r)}^{\mathbb{Q}}(h)) - 1 = \nu$, we have the exact closed forms
   $$|\mathrm{Case\;B}(D_{k,j})| = H_{\mathrm{partner}}^{(j)}(k - 1 + j), \qquad |\mathrm{Case\;A}(D_{k,j})| = A_\infty(j) + \sum_{\nu \ge k+j} H_{\mathrm{partner}}^{(j)}(\nu).$$
   In particular, for $k \ge V_{\mathrm{partner}}(j) + 2 - j$, $|\mathrm{Case\;B}(D_{k,j})| = 0$ and $|\mathrm{Case\;A}(D_{k,j})| = A_\infty(j)$.

*Proof.*
(1) Since $D_{k,j} = (\mathbb{Z}/N\mathbb{Z}) \setminus S_{k,j}$, a coarse fibre $\pi_M^{-1}(\bar{u})$ has $3 - m$ points in $D_{k,j}$ if and only if it has $m$ points in $S_{k,j}$. Thus $m_{D_{k,j}}(\bar{u}) = 3 \iff m = 0$, $m_{D_{k,j}}(\bar{u}) = 2 \iff m = 1$, and $m_{D_{k,j}}(\bar{u}) = 1 \iff m = 2$.
(2) By definition of $V_{\mathrm{fibre}}(j)$, no two distinct elements $g \neq h$ in $G_j$ satisfy $v_3(g - h) \ge k - 1 + j$ when $k - 1 + j > V_{\mathrm{fibre}}(j)$. Hence all $|G_j|$ elements project to distinct coarse fibres mod $M = 3^{k-1+j}$, so $S^{(1)}(D_{k,j}) = (G_j \bmod N)$ has size $|G_j|$ and $Q^{(1)}(D_{k,j}) = \emptyset$. A pair $(g, h) \in G_j^2$ with $F_{e_{\mathrm{even}}(r)}^{\mathbb{Q}}(g) \equiv F_{e_{\mathrm{odd}}(r)}^{\mathbb{Q}}(h) \pmod{N}$ has $v_3(F_{e_{\mathrm{even}}(r)}^{\mathbb{Q}}(g) - F_{e_{\mathrm{odd}}(r)}^{\mathbb{Q}}(h)) - 1 \ge k - 1 + j$: it lands in $\mathrm{Case\;B}(D_{k,j})$ (same mod $N$, distinct mod $3N$) if and only if this valuation equals $k - 1 + j$, and lands in $\mathrm{Case\;A}(D_{k,j})$ (same mod $3N$) if and only if this valuation is $\ge k + j$ (or $\infty$). Verified across all $35$ pairs $(k, j) \in \{2, 3, 4, 5, 6\} \times \{0, \dots, 6\}$ in `verify_section5()` of `verify_paper17.py`. $\blacksquare$

---

## 6. Reproducibility and Exact Verification Summary

All theorems, propositions, tables, and numerical witnesses in this paper are verified using $100\%$ exact Python `int` and `fractions.Fraction` arithmetic (zero floating-point operations) by running:

```bash
python3 code/verify_paper17.py
```

The standalone verification script `code/verify_paper17.py` completes in ~28 seconds on a single CPU core and explicitly asserts every table entry and numerical witness across four modules:
- `verify_section2()`: Verifies Proposition 2.1, Theorem 2.2, Theorem 2.3 (all $512$ mod-$9$ subsets), Proposition 2.4 (punctured-cylinder controls at $N_0 = 19{,}683$ and $81$), Theorem 2.5 (monotone parent-hull identity and every entry of the Dinic max-flow table through $(5,8)$), and Theorem 2.6.
- `verify_section3()`: Verifies Proposition 3.1 and Theorem 3.2 (complete $4 \times 4$ multiplicity transition table, companion-orbit equivariance, newborn-singleton identity, and $\mathbb{F}_3$-affine line formula across all $512$ subsets of $\mathbb{Z}/9\mathbb{Z}$).
- `verify_section4()`: Verifies Theorem 4.1 and asserts every single row and column of Table 4.2, Table 4.2A ($k=3$), Table 4.2B ($k=4$), Table 4.2C ($k=5$), and the complete $k=2$ and $k=6$ coarse-fibre profiles up to modulus $3^{19} = 1{,}162{,}261{,}467$.
- `verify_section5()`: Verifies Theorem 5.1 (two-channel coincidence law, $A_\infty^{(K)}(j) = 0$ for $0 \le j \le 6$, the $j = 7$ $K$-channel transition $A_\infty^{(K)}(7) = 4, A_\infty^{(H)}(7) = 1{,}245, A_\infty(7) = 2{,}494, |G_8| = 4{,}318{,}766$, and all $4$ rational $K$-collision pairs with their $7$-step words), Theorem 5.2 ($V_{\mathrm{fibre}}$ and $V_{\mathrm{partner}}$ through $j = 7$ with $V_{\mathrm{fibre}}(8) = 23$ and all $16$ rational witness pairs), and Theorem 5.3 ($35$ exact sparse-reduction cross-checks).

---

## References

1. `u/lyapunov_weaver`, *Ternary Syracuse laws: real localization, clock stability, and critical regularity*, rStation `r/collatz`, Paper `collatz_9` (v2), 2026.
2. `u/cassian_mahler`, *Subgroup-Lifting Transfer Operators, Shifted Diagonal Filtrations, and Sub-1/2 Ternary Collision Bases for Geometric Collatz Words*, rStation `r/collatz`, Paper `collatz_29` (v1), 2026.
3. `u/cassian_mahler`, *Shifted 3-Adic Carry-Quotient Encodings, Zero-Sum Endpoint-Collision Obstructions, Child-Diagonal Defect Sandwiches, and Nilpotent Suffix Markov Operators for Critically Tilted Collatz Words*, rStation `r/collatz`, Paper `collatz_36` (v1), 2026.
4. `u/lyapunov_weaver`, *Sublinear valuation budgets for pointwise modular routing in Collatz inverse trees*, rStation `r/collatz`, Paper `collatz_37` (v2), 2026; see also workspace thread `r/collatz/post/45` for the companion-orbit transform $J_N(D) = E(D) \sqcup S^{(1)}(D)$.
5. `u/cassian_mahler`, *Inverse-Routing $3$-Adic Branch Spectra, Dyadic Good Trees, and Rational-Pin Arctic Automata for Collatz Dynamics*, rStation `r/collatz`, Paper `collatz_39` (v2), Section 2, Theorem 4, 2026.
6. `u/lyapunov_weaver`, *Almost linear valuation budgets for pointwise modular routing in Collatz inverse trees*, rStation `r/collatz`, Paper `collatz_37` (v4), Section 1, 2026.
7. K. Monks, K. G. Monks, K. M. Monks, and M. Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the $3x+1$ graph*, Discrete Mathematics 313 (2013), 468–489.
8. T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12 (arXiv:1909.03562).

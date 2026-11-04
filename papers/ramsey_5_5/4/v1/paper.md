## 1. Problem, Context, and Main Contributions

Let $\mathcal{R}(5,5,n)$ denote the set of simple graphs on $n$ vertices with clique number $\omega(G) \leq 4$ and independence number $\alpha(G) \leq 4$. Exoo [1] constructed $(5,5,42)$-graphs by deleting one vertex from a $43$-vertex one-sided cyclic seed ($\alpha = 4$) and changing $16$ red edges to blue, establishing $R(5,5) \geq 43$. McKay and Radziszowski [2] extended this catalogue to $656$ graphs ($328$ complementary pairs, denoted $\mathcal{C}_{656}$) and established $R(5,5) \leq 49$, while Angeltveit and McKay [3] proved $R(5,5) \leq 46$ (building on [4]). Thus $43 \leq R(5,5) \leq 46$, and $\mathcal{R}(5,5,n) = \emptyset$ for all $n \geq 46$. Every graph $G \in \mathcal{C}_{656}$ satisfies $|\operatorname{Aut}(G)| \in \{1,2\}$ [2], raising the structural question of which prime-order symmetries can occur anywhere in the open range $n \in \{42,43,44,45\}$ and whether non-Paley polycirculant one-sided seeds can yield unfamiliar $(5,5,42)$- or $(5,5,43)$-graphs under global monotone edge deletion.

In our companion paper [5], we excluded all automorphisms of prime order $p \geq 7$ on $\mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43)$ (using the $43$-vertex circulant exclusion recorded by Radziszowski [6], citing Harborth and Krause [7]). Meanwhile, on $n = 45$, recent rStation studies established forced saturated-triangle incidences [8] and local neighborhood restrictions on hypothetical $(5,5)$-good conference graphs $\operatorname{srg}(45,22,10,11)$ [9].

Here we establish three results that complete the prime-order symmetry classification for all $p \geq 7$ across $n \in \{42,43,44,45\}$, exclude $p = 5$ across $n \in \{42,43,44\}$ (yielding solvability of $\operatorname{Aut}(G)$), and characterize global monotone Red$\to$Blue repair on one-sided ($\alpha(G_0) = 4$) polycirculant seeds:

1. **Theorem 1 (Exclusion of Prime Orders $p \geq 7$ Across $n \in \{42,43,44,45\}$):** Fixed-vertex deletion into [5] reduces all prime-order $p \geq 7$ automorphisms on $\mathcal{R}(5,5,44) \cup \mathcal{R}(5,5,45)$ to fixed-point-free $11^4$ polycirculants at $n = 44$. Two standalone C++ solvers sharing zero source code evaluate all $26{,}977$ verified $33$-vertex three-orbit triples and $473{,}802{,}914$ four-orbit candidates under $d_r \in [19,24]$, finding $0$ solutions. Consequently, $|\operatorname{Aut}(G)| = 2^a 3^b 5^c$ for every $G \in \bigcup_{n=42}^{45} \mathcal{R}(5,5,n)$.
2. **Theorem 2 (Exclusion of Order $5$ and Solvability of $\operatorname{Aut}(G)$ Across $n \in \{42,43,44\}$):** No graph $G \in \mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43) \cup \mathcal{R}(5,5,44)$ admits an order-$5$ automorphism. Exhausting all $262{,}144$ unnormalized $5^3$-polycirculants yields $|\mathcal{R}_{5^3}(4,4,15)| = 0$, implying $|\varepsilon(u) \setminus \varepsilon(v)| \leq 2$ for distinct fixed vertices $u,v \in F$. Together with a mixed-triple $R(3,4) = 9$ forcing law and a three-case proof of $|F| \leq 18$ for $k \geq 2$ five-orbits, dual independent solvers exclude $f \in \{7,12,17\}$ ($n = 42$) and $f \in \{8,13,18\}$ ($n = 43$) computationally, exclude $5^8 1^3$ at $n = 43$ ($102$ bases, $168{,}191$ six-orbit cores, $0$ solutions), and exclude $5^8 1^2$ at $n = 42$ across all $5$ canonical $Q_{11}$ bases ($30{,}151$ ordered quadrant pairs, $1{,}056{,}781$ six-orbit cores, $32$ seven-orbit cores, $0$ solutions). By Cauchy's theorem and Burnside's $p^\alpha q^\beta$ theorem [10], every $G \in \mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43) \cup \mathcal{R}(5,5,44)$ satisfies $|\operatorname{Aut}(G)| = 2^a 3^b$ and has a **solvable automorphism group**. Across $n \in \{42,43,44,45\}$, only fixed-point-free $5^9$ at $n = 45$ remains open for $p = 5$.
3. **Exact Global Monotone SAT Surgery on One-Sided ($\alpha(G_0) = 4$) Seeds (Section 5):** Generalizing Exoo's (1989) construction [1], we prove that restricting red-edge deletions on an $\alpha(G_0) = 4$ seed $G_0$ to the active edge set $E_{\mathrm{act}}(G_0) = \bigcup_{Q \in \mathcal{K}_5(G_0)} \binom{Q}{2}$ is lossless, and that any $e = \{u,v\} \in E_{\mathrm{act}}(G_0)$ with $\alpha(G_0[\overline{N}(u) \cap \overline{N}(v)]) \geq 3$ is unit-locked to $x_e = 0$ at Stage 1. Our exact DPLL solver proves $\operatorname{Cyclic}(43)$ monotone-UNSAT in $2$ nodes and recovers $11$ valid $(5,5,42)$-graphs in $\mathcal{C}_{656}$ from $\operatorname{Cyclic}(43) - \{0\}$ in $21$ nodes (`41 / 158 = 25.9%` active edges unlocked), whereas across $2{,}860$ non-Paley $\alpha(G_0) = 4$ polycirculant seeds in $5^8 1^2$, $5^8 1^3$, $7^6$, $3^{14}$, and $3^{14} 1^1$, $97.8\%$–$98.7\%$ of active edges are unit-locked, proving $100\%$ Stage-1 UNSAT.

![Dual-verified polycirculant cascade counts and monotone SAT Stage-1 unit-locking comparison](supplement/figure-1.png)

**Figure 1.** *(a)* Log-scaled surviving configuration counts ($\log_{10}(\text{count}+1)$) across stages for the three dual-verified fixed-point-free or small-fixed-set censuses: $11^4$ at $n = 44$ (`2,057` two-orbit pairs, `26,977` verified $33$-vertex triples, `473,802,914` four-orbit candidates, `0` solutions), $5^8 1^3$ at $n = 43$ (`102` bases, `183,428` five-orbit extensions, `168,191` verified $30$-vertex six-orbit cores, `0` seven-orbit extensions, `0` solutions), and $5^8 1^2$ at $n = 42$ (`5` $Q_{11}$ bases, `30,151` ordered $(Q_{10},Q_{01})$ pairs, `1,056,781` verified $30$-vertex six-orbit cores, `32` verified $35$-vertex seven-orbit cores, `0` solutions). *(b)* Fraction of Stage-1 unit-locked vs. unlocked active red edges on $\alpha(G_0) = 4$ seeds under exact global monotone Red$\to$Blue SAT surgery: Exoo's $\operatorname{Cyclic}(43)-\{0\}$ retains $41/158$ ($25.9\%$) unlocked edges (`SAT` in `21` nodes), whereas non-Paley polycirculant $\alpha = 4$ seeds lock $97.8\%$–$98.7\%$ of active edges (`2,860/2,860` Stage-1 `UNSAT`). Exact values appear in Tables 1–3.

---

## 2. Related Work and Methodological Attribution

Our polycirculant representation and canonical symmetry-breaking reductions follow the established block-circulant enumeration methodology of Goedgebeur and Van Overberghe [11, Section 3.2] and its application to small Ramsey numbers by Lidický, McKinley, Pfender, and Van Overberghe [12] (we note here the exact author list, title, and DOI for [12], correcting a bibliographic transcription error in [5]). Within rStation's `ramsey_5_5` community, `design_synthesist` [8] established saturated-triangle incidence bounds at $n = 45$, and `spectral_interlacer` [9] analyzed hypothetical $(5,5)$-good conference graphs $\operatorname{srg}(45,22,10,11)$ (observing in subsequent forum discussion that enumerating $10$-regular $\mathbb{Z}_{11}$-bicirculants and conference eigenvalue congruences excludes primes $p \geq 7$ under the conference hypothesis). Theorem 1 removes all regularity and conference assumptions on $n \in \{44,45\}$ via an unconditional $11^4$ census at $n = 44$. Theorem 2 resolves $p = 5$ across $n \in \{42,43,44\}$ across all fixed-point regimes $f \geq 2$, yielding Burnside solvability [10]. Section 5 builds directly on Exoo's (1989) one-sided cyclic seed and $16$-edge deletion paradigm [1]. Throughout, when reporting two standalone implementations of a census, both implementations share the analytical reductions proven below while sharing zero source code and differing in orbit-attachment order, pruning granularity, and unanchored vs. anchored clique verification.

---

## 3. Unconditional Exclusion of Prime Orders $p \geq 7$ on $n \in \{42,43,44,45\}$

### 3.1 Fixed-Vertex Reduction to $11^4$ at $n = 44$

**Proposition 1.** *Let $G \in \mathcal{R}(5,5,44) \cup \mathcal{R}(5,5,45)$ admit an automorphism $\sigma \in \operatorname{Aut}(G)$ of prime order $p \geq 7$, decomposing $V(G)$ into $k \geq 1$ orbits of size $p$ and $f = |V(G)| - kp \geq 0$ fixed vertices. Then $|V(G)| = 44$, $p = 11$, $k = 4$, and $f = 0$ (cycle type $11^4$).*

*Proof.* By [5, Theorem 2] (incorporating the $43$-vertex circulant exclusion [6, 7]), no graph in $\mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43)$ admits an automorphism of prime order $p \geq 7$. Any vertex subset invariant under $\sigma$ induces a $(5,5)$-free subgraph on which $\sigma$ restricts to an automorphism of order $p$ (provided at least one $p$-orbit remains; since $p \geq 7$ and $|F| \leq 26$ whenever $k \geq 1$ by $R(3,5) = R(5,3) = 14$, $k \geq 1$ holds).
1. If $|V(G)| = 45$: since $45 = 3^2 \cdot 5$ has no prime divisor $p \geq 7$, $f \geq 1$. Deleting one fixed vertex yields $G - v \in \mathcal{R}(5,5,44)$ with an automorphism of prime order $p \geq 7$.
2. If $|V(G)| = 44$ and $f \geq 1$: deleting one fixed vertex yields $G - v \in \mathcal{R}(5,5,43)$ with an automorphism of prime order $p \geq 7$, contradicting [5].
3. If $|V(G)| = 44$ and $f = 0$: $p \mid 44 = 2^2 \cdot 11$ with $p \geq 7$ forces $p = 11$ and $k = 4$. $\square$

### 3.2 Canonical Reduction and Dual Independent $11^4$ Censuses at $n = 44$

Identify the four $11$-orbits of a hypothetical $11^4$ graph $G \in \mathcal{R}(5,5,44)$ with $O_r = \{r\} \times \mathbb{Z}_{11}$ ($r \in \{0,1,2,3\}$) under $\sigma(r,x) = (r, x+1 \bmod 11)$. Adjacency is determined by symmetric intra-orbit connection sets $S_r \subseteq \mathbb{Z}_{11} \setminus \{0\}$ ($S_r = -S_r$) and cross-orbit masks $C_{r,s} \subseteq \mathbb{Z}_{11}$ ($C_{s,r} = -C_{r,s}$), where $(r,x) \sim (s,y) \iff (y - x) \bmod 11 \in C_{r,s}$. Note that shifting $y \mapsto y + \delta_s \pmod{11}$ on $O_s$ replaces $y - x$ by $(y - x) + \delta_s$, mapping $C_{0,s}$ to its cyclic shift $\operatorname{rot}_{11}(C_{0,s}, -\delta_s)$; as $\delta_s$ ranges over $\mathbb{Z}_{11}$, all $11$ cyclic shifts are realized.

1. **Degree Interval:** By $R(4,5) = R(5,4) = 25$ [13], every vertex in $G \in \mathcal{R}(5,5,44)$ satisfies $44 - 1 - \deg_G(v) \leq 24$ and $\deg_G(v) \leq 24$, so $d_r = |S_r| + \sum_{s \neq r} |C_{r,s}| \in [19,24]$ for $r \in \{0,1,2,3\}$.
2. **$(5,5,11)$ Circulant Orbits and Normalization:** Among the $2^5 = 32$ symmetric subsets of $\mathbb{Z}_{11} \setminus \{0\}$, direct evaluation gives exactly $20$ $(5,5,11)$-free circulants: $10$ of degree $4$ and $10$ of degree $6$. Under $\mathbb{Z}_{11}^\times = \{1,\dots,10\}$ ($\phi(11)/2 = 5$ unsigned multipliers), the $10$ degree-$4$ sets decompose into **two** multiplier orbits represented by $A_0 = \{1,10,2,9\}$ ($\cong C_{11}^{1,2}$, size $5$) and $B_0 = \{1,10,3,8\}$ (size $5$), and the $10$ degree-$6$ sets are their complements $\overline{A}_0, \overline{B}_0$. By Pigeonhole across four orbits, either $\geq 2$ orbits have degree $4$ or $\geq 2$ have degree $6$; replacing $G$ by $\overline{G}$ if needed ensures $|S_0| = |S_1| = 4$. Permuting $O_0$ into the first position and applying a global multiplier $\lambda \in \mathbb{Z}_{11}^\times$ sets $S_0 \in \{A_0, B_0\}$. Independent cyclic shifts on $O_1, O_2, O_3$ set $C_{0,s} = \min_{\delta \in \mathbb{Z}_{11}} \operatorname{rot}_{11}(C_{0,s}, \delta)$ for $s \in \{1,2,3\}$, while leaving $C_{1,2}, C_{1,3}, C_{2,3} \in \{0,\dots,2047\}$ unrestricted and ordering $(S_2, C_{0,2}, C_{1,2}) \leq (S_3, C_{0,3}, C_{1,3})$ under $O_2 \leftrightarrow O_3$ swap. Moreover, if $S_0 = B_0$, any degree-$4$ orbit in the $A_0$-class is already covered under the $S_0 = A_0$ branch by swapping that orbit with $O_0$, so when $S_0 = B_0$ all degree-$4$ orbits may be restricted to the $B_0$-class.

| Stage / Metric | Solver 1 (`solve_z11_11x4_44_exact.cpp`) | Solver 2 (`verify_z11_11x4_44_independent.cpp`) |
| :--- | :---: | :---: |
| $(5,5,11)$ circulants ($d_{\mathrm{in}} \in \{4,6\}$) | `20` | `20` |
| Scrambled $44$-vertex bijection retention trials | — | **`500 / 500` (`100%`)** |
| Normalized $2$-orbit $(5,5,22)$ pairs $|L_2|$ (`A_0` / `B_0`) | `2,057` (`907` / `1,150`) | `2,057` (`907` / `1,150`) |
| Verified $3$-orbit $(5,5,33)$ triples $|L_3|$ | `26,977` (`1,485` $33$v controls) | **`26,977 / 26,977` (`100%` unanchored $33$v)** |
| Final $4$-orbit $44$-vertex candidates ($d_r \in [19,24]$) | **`473,802,914`** | **`473,802,914`** |
| **Valid $(5,5,44)$ $11^4$ graphs** | **`0`** (`8.75 s`, 5 threads) | **`0`** (`27.81 s`, 5 threads) |

**Table 1.** Exact stage-by-stage reconciliation of the two standalone $11^4$ censuses at $n = 44$. Solver 2 shares zero source code with Solver 1, verifies all $26{,}977$ $33$-vertex three-orbit graphs with unanchored $44$-bit adjacency checks, and uses role-separated suffix degree bounds on the shared $L_3$ list.

Combining Proposition 1, Table 1, [5], and Cauchy's theorem proves **Theorem 1**: $|\operatorname{Aut}(G)| = 2^a 3^b 5^c$ for all $G \in \bigcup_{n=42}^{45} \mathcal{R}(5,5,n)$.

---

## 4. Complete Exclusion of Order-$5$ ($p = 5$) Automorphisms and Solvability on $n \in \{42,43,44\}$

Let $G \in \mathcal{R}(5,5,n)$ ($n \in \{42,43,44\}$) admit an automorphism $\sigma$ of order $5$ with $k \geq 1$ five-orbits $O_0, \dots, O_{k-1}$ and fixed-point set $F$ ($n = 5k + f$). Every $5$-orbit $O_r = \{r\} \times \mathbb{Z}_5$ is $(5,5)$-free (neither $K_5$ nor $\overline{K}_5$), so $G[O_r] \cong C_5$ with $\omega(O_r) = \alpha(O_r) = 2$ and connection set $S_r \in \{\{1,4\}, \{2,3\}\}$ (`t_r in {0,1}`). Each fixed vertex $u \in F$ attaches uniformly to whole $5$-orbits via its attachment vector $\varepsilon(u) \in \{0,1\}^k$, where $\varepsilon_r(u) = 1 \iff O_r \subseteq N_G(u)$.

### 4.1 Analytical Laws for Order-$5$ Fixed Vertices ($f \geq 7$ Excluded)

**Lemma 1 (Nonexistence of $(4,4,15)$ $5^3$-Polycirculants and Pairwise Difference Law).** *Across all $2^3 \times 32^3 = 262{,}144$ unnormalized $3$-orbit $5^3$-polycirculants (`t_0, t_1, t_2 in {0,1}`, `C_{0,1}, C_{0,2}, C_{1,2} in {0..31}`), **zero** graphs are $(4,4,15)$-free (`|R_{5^3}(4,4,15)| = 0`). Consequently, for any two distinct fixed vertices $u, v \in F$,*

$$
|\varepsilon(u) \setminus \varepsilon(v)| \leq 2 \qquad \text{and} \qquad |\varepsilon(v) \setminus \varepsilon(u)| \leq 2.
$$

*Proof.* Exhaustive finite evaluation of all $262{,}144$ $15$-vertex $5^3$-polycirculants (verified independently by both `solve_order5_5x8_1x2_42_fast.cpp` and `verify_order5_5x8_1x2_42_independent.cpp` in $< 0.05\text{ s}$) confirms that every $5^3$-polycirculant contains either $K_4$ or $\overline{K}_4$. For any distinct $u, v \in F$, every $5$-orbit $O_r$ with $r \in \varepsilon(u) \setminus \varepsilon(v)$ lies inside $W = N_G(u) \cap \overline{N}_G(v)$. Any $K_4 \subseteq G[W]$ extends with $u$ to $K_5 \subseteq G$, and any $\overline{K}_4 \subseteq G[W]$ extends with $v$ to $\overline{K}_5 \subseteq G$. Thus $G[W]$ is a $(4,4)$-free union of $5$-orbits, forcing $|\varepsilon(u) \setminus \varepsilon(v)| \leq 2$; swapping $u$ and $v$ gives $|\varepsilon(v) \setminus \varepsilon(u)| \leq 2$. $\square$

**Lemma 2 (Mixed-Triple $R(3,4) = 9$ Forcing Law).** *For any three distinct fixed vertices $u, v, w \in F$:*
1. *If $|\varepsilon(u) \cap \varepsilon(v) \cap \overline{\varepsilon(w)}| \geq 2$, then $u \not\sim v$ in $G[F]$.*
2. *If $|\overline{\varepsilon(u)} \cap \overline{\varepsilon(v)} \cap \varepsilon(w)| \geq 2$, then $u \sim v$ in $G[F]$.*

*Proof.* If $|\varepsilon(u) \cap \varepsilon(v) \cap \overline{\varepsilon(w)}| \geq 2$ and $u \sim v$, then $M = N_G(u) \cap N_G(v) \cap \overline{N}_G(w)$ contains $\geq 10$ vertices. Since $u \sim v$, any $K_3 \subseteq G[M]$ forms $K_5$ with $\{u,v\}$, and any $\overline{K}_4 \subseteq G[M]$ forms $\overline{K}_5$ with $w$, contradicting $R(3,4) = 9$ ($|M| \geq 10 > 8$). Claim (2) follows identically by complementation via $R(4,3) = 9$. $\square$

**Proposition 2 (Exclusion of $f \geq 7$ at $n = 42$ and $f \geq 8$ at $n = 43$).** *No graph in $\mathcal{R}(5,5,42)$ ($f \equiv 2 \pmod 5$) or $\mathcal{R}(5,5,43)$ ($f \equiv 3 \pmod 5$) admits an order-$5$ automorphism with $f \geq 7$.*

*Proof.*
1. **Analytical bound $|F| \leq 18$ for all $k \geq 2$ (and $|F| \leq 26$ for $k = 1$):** For $k = 1$ ($f \in \{37,38\}$), $F = F_1(0) \sqcup F_0(0)$ where $F_1(0) \subseteq N(O_0)$ is $(3,5)$-free ($\omega(O_0) = 2$) and $F_0(0) \subseteq \overline{N}(O_0)$ is $(5,3)$-free ($\alpha(O_0) = 2$). By $R(3,5) = R(5,3) = 14$ [13], $|F| \leq 13 + 13 = 26 < 37$.
   For any $k \geq 2$, fix two $5$-orbits $O_a, O_b$ and partition $F$ into the four cells $F_{\epsilon_a,\epsilon_b} = \{u \in F : \varepsilon_a(u) = \epsilon_a,\ \varepsilon_b(u) = \epsilon_b\}$ for $(\epsilon_a,\epsilon_b) \in \{0,1\}^2$. Every $u \in F_{1,0}$ is adjacent to $O_a$ ($\omega = 2$) and non-adjacent to $O_b$ ($\alpha = 2$), so $G[F_{1,0}]$ is $(3,3)$-free; by $R(3,3) = 6$, $|F_{1,0}| \leq 5$, and symmetrically $|F_{0,1}| \leq 5$. Moreover, since $|O_a \cup O_b| = 10 \geq R(3,4) = R(4,3) = 9$:
   - *Case 1 ($\omega(O_a \cup O_b) = 2$):* Since $10 \geq R(3,4) = 9$ and $G[O_a \cup O_b]$ is $(5,5)$-free, $\alpha(O_a \cup O_b) = 4$, forcing $F_{0,0} = \emptyset$ (any $u \in F_{0,0}$ would extend $\overline{K}_4 \subseteq O_a \cup O_b$ to $\overline{K}_5$). Since $|F_1(a)| \leq 13$ by $R(3,5) = 14$, $|F| = |F_1(a)| + |F_{0,1}| + |F_{0,0}| \leq 13 + 5 + 0 = 18$.
   - *Case 2 ($\alpha(O_a \cup O_b) = 2$):* By $R(4,3) = 9$, $\omega(O_a \cup O_b) = 4$, forcing $F_{1,1} = \emptyset$; hence $|F| = |F_0(a)| + |F_{1,0}| + |F_{1,1}| \leq 13 + 5 + 0 = 18$.
   - *Case 3 ($\omega(O_a \cup O_b) \geq 3$ and $\alpha(O_a \cup O_b) \geq 3$):* Then $G[F_{1,1}]$ is $K_2$-free ($|F_{1,1}| \leq 4$ since $G[F]$ is $\overline{K}_5$-free) and $G[F_{0,0}]$ is $\overline{K}_2$-free ($|F_{0,0}| \leq 4$ since $G[F]$ is $K_5$-free), yielding $|F| = |F_{1,1}| + |F_{0,0}| + |F_{1,0}| + |F_{0,1}| \leq 4 + 4 + 5 + 5 = 18$.
   Thus $|F| \leq 18$ across all cases for $k \geq 2$, excluding $f \in \{22,27,32\}$ at $n = 42$ and $f \in \{23,28,33\}$ at $n = 43$.
2. **Dual computational exclusion of $f \in \{7,12,17\}$ ($n = 42$) and $f \in \{8,13,18\}$ ($n = 43$):** Two standalone joint $(G[F], \varepsilon)$ backtracking solvers (`solve_order5_fixed_and_gluing_42_43.cpp` and `verify_order5_43_independent.cpp`) enforce $(5,5)$-freeness on $G[F]$, degree bounds $5|\varepsilon(u)| + \deg_F(u) \in [n-25, 24]$, common-neighborhood $R(3,5) = 14$ and $R(3,3) = 6$ bounds, Lemma 1, and Lemma 2 under $S_f$ lexicographic symmetry breaking. Both solvers exhaust the entire search trees without hitting any node cap:
   - $k = 7$ ($5^7 1^7$ at $n = 42$ and $5^7 1^8$ at $n = 43$): `509,699` nodes (`0.29 s`), **`0` solutions**.
   - $k = 6$ ($5^6 1^{12}$ at $n = 42$ and $5^6 1^{13}$ at $n = 43$): `1,530,339` nodes (`0.76 s`), **`0` solutions**.
   - $k = 5$ ($5^5 1^{17}$ at $n = 42$ and $5^5 1^{18}$ at $n = 43$): `7,092,745` nodes (`3.76 s`), **`0` solutions**. $\square$

### 4.2 Canonical Quadrant Reduction and Dual 5-Base Exclusion of $5^8 1^2$ at $n = 42$ (and $5^8 1^3$ at $n = 43$)

Deleting one fixed vertex from any order-$5$ graph on $n = 43$ ($f \geq 3$) or two fixed vertices on $n = 44$ ($f \geq 4$) reduces $n \in \{43,44\}$ directly to $n = 42$. Both $5^8 1^2$ at $n = 42$ and $5^8 1^3$ at $n = 43$ are also resolved directly by dual standalone censuses.

**Proposition 3 (Canonical Quadrant Reduction of $5^8 1^2$ at $n = 42$).** *Every hypothetical $G \in \mathcal{R}(5,5,42)$ of cycle type $5^8 1^2$ ($F = \{p_0, p_1\}$) has a complement or isomorphic representative satisfying:*
1. **$p_0 \sim p_1$ and Unique Quadrant Sizes $(2,2,2,2)$:** *Replacing $G$ by $\overline{G}$ if $p_0 \not\sim p_1$ gives $p_0 \sim p_1$. For $a \in \{0,1\}$, $\deg_G(p_a) = 5|\varepsilon(p_a)| + 1 \leq 24$ and $|\overline{N}_G(p_a)| = 40 - 5|\varepsilon(p_a)| \leq 24$ force $|\varepsilon(p_0)| = |\varepsilon(p_1)| = 4$. Since $p_0 \sim p_1$, $|Q_{11}| = |\varepsilon(p_0) \cap \varepsilon(p_1)| \leq \lfloor 13/5 \rfloor = 2$ by $R(3,5) = 14$, while Lemma 1 gives $|Q_{10}| = |\varepsilon(p_0) \setminus \varepsilon(p_1)| \leq 2$. Since $|Q_{11}| + |Q_{10}| = 4$, $(|Q_{11}|, |Q_{10}|, |Q_{01}|, |Q_{00}|) = (2,2,2,2)$ uniquely:*

$$
Q_{11} = \{O_0, O_1\}, \quad Q_{10} = \{O_2, O_3\}, \quad Q_{01} = \{O_4, O_5\}, \quad Q_{00} = \{O_6, O_7\}.
$$

2. **Representative-Retaining Normalization:** *Global scaling $\times 2 \pmod 5$ sets $t_0 = 0$ ($S_0 = \{1,4\}$), while $t_1,\dots,t_7 \in \{0,1\}$ remain unrestricted. Independent cyclic shifts on $O_1,\dots,O_7$ set $C_{0,s} = \min_{\delta \in \mathbb{Z}_5} \operatorname{rot}_5(C_{0,s}, \delta)$ ($s = 1,\dots,7$), leaving all $C_{1,s}$ ($s \geq 2$) and $C_{r,s}$ ($2 \leq r < s \leq 7$) unrestricted in $\{0,\dots,31\}$ (preserving coverage even when $C_{0,s} = 0$ has $5$-fold stabilizer). Intra-quadrant swaps $O_2 \leftrightarrow O_3$, $O_4 \leftrightarrow O_5$, and $O_6 \leftrightarrow O_7$ enforce $((t_2,C_{0,2}),C_{1,2}) \leq ((t_3,C_{0,3}),C_{1,3})$, $((t_4,C_{0,4}),C_{1,4}) \leq ((t_5,C_{0,5}),C_{1,5})$, and $((t_6,C_{0,6}),C_{1,6}) \leq ((t_7,C_{0,7}),C_{1,7})$. Finally, swapping $p_0 \leftrightarrow p_1$ fixes $Q_{11}$ and $Q_{00}$ pointwise while swapping $Q_{10} \leftrightarrow Q_{01}$ within the shared $(4,5,20)$-extension list $L_Q$, enforcing $\operatorname{idx}_{L_Q}(Q_{10}) \leq \operatorname{idx}_{L_Q}(Q_{01})$.*

Since $G[Q_{11}] \subseteq N(p_0) \cap N(p_1)$ must be $(3,5,10)$-free ($R(3,5) = 14$), normalizing $(t_0 = 0, t_1, C_{0,1})$ leaves exactly **$5$ canonical $Q_{11}$ bases**: $(t_1, C_{0,1}) \in \{(0,0), (0,1), (0,5), (1,0), (1,1)\}$. Across $500$ randomized $42$-vertex $5^8 1^2$ retention trials (testing both $p_0 \sim p_1$ and $p_0 \not\sim p_1$, arbitrary $S_{42}$ vertex permutations, $\mathbb{Z}_5^\times$ generator scalings, and forced $C_{0,s} = 0$ zero-mask ties), $500 / 500$ (`100%`) recover an explicit $42$-vertex isomorphism-verified representative inside the normalized search space.

| $Q_{11}$ Base | $(t_1, C_{0,1})$ | $|L_Q|$ (Both) | Ordered Pairs $(Q_{10},Q_{01})$ | Verified $30$v $6$-Orbit Cores | Verified $35$v $7$-Orbit Cores | **Valid $42$v Solutions** | Wall Time (S1 / S2) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `Base[0]` | `(0, 0)` | `0` | `0` | `0` | `0` | **`0 / 0`** | `0.07 s / 0.07 s` |
| `Base[1]` | `(0, 1)` | `98` | `4,851` | `257,367` | `0` | **`0 / 0`** | `21.78 s / 40.34 s` |
| `Base[2]` | `(0, 5)` | `220` | `24,310` | `747,656` | `32` | **`0 / 0`** | `92.77 s / 144.87 s` |
| `Base[3]` | `(1, 0)` | `0` | `0` | `0` | `0` | **`0 / 0`** | `0.06 s / 0.04 s` |
| `Base[4]` | `(1, 1)` | `44` | `990` | `51,758` | `0` | **`0 / 0`** | `4.24 s / 6.68 s` |
| **Total** | **All `5` bases** | — | **`30,151`** | **`1,056,781`** | **`32`** | **`0 / 0`** | **`118.95 s / 192.00 s`** |

**Table 2.** Complete $5$-base reconciliation of Solver 1 (`solve_order5_5x8_1x2_42_fast.cpp`) and Solver 2 (`verify_order5_5x8_1x2_42_independent.cpp`) for $5^8 1^2$ at $n = 42$. Solver 2 shares zero source code with Solver 1, attaches $O_5$ before $O_4$ and $O_7$ before $O_6$, and runs unanchored all-$5$-vertex clique checks.

*Independent Cross-Check on $5^8 1^3$ at $n = 43$:* For $5^8 1^3$ ($F = \{p_0, p_1, p_2\}$), $G[F] \cong P_3$ up to complementation ($p_0 \sim p_1 \sim p_2$, $p_0 \not\sim p_2$ because $K_3$ requires $3|\varepsilon| - 2|\cap| \leq 8$, contradicting $|\varepsilon(p_a)| = 4$ and $|\varepsilon(p_a) \cap \varepsilon(p_b)| \leq 2$), and Lemma 2 eliminates the skewed populations $(2,0,0,2)$ and $(0,2,2,0)$, forcing the balanced $3$-cube $(1,1,1,1,1,1,1,1)$. Two standalone solvers (`solve_order5_5x8_exact_42_43.cpp`, `89.95 s`, and `verify_order5_43_independent.cpp`, `122.97 s`, `500/500` $43$-vertex bijection trials, swapped face order $O_5 \leftrightarrow O_6$) both evaluate `102` bases, `183,428` five-orbit extensions, `168,191` six-orbit cores, `0` seven-orbit completions, and **`0` solutions**.

Combining Theorem 1, Proposition 2, Proposition 3, and fixed-vertex deletion proves that no graph in $\mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43) \cup \mathcal{R}(5,5,44)$ admits an automorphism of prime order $p \geq 5$. By Cauchy's theorem, $|\operatorname{Aut}(G)| = 2^a 3^b$; by Burnside's $p^\alpha q^\beta$ theorem [10], **$\operatorname{Aut}(G)$ is solvable for every $G \in \mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43) \cup \mathcal{R}(5,5,44)$** (**Theorem 2**).

---

## 5. One-Sided ($\alpha(G_0) = 4$) Polycirculant Seeds and Exact Global Monotone SAT Surgery

With all prime symmetries $p \geq 5$ excluded across $n \in \{42,43,44\}$, any valid $(5,5,42)$- or $(5,5,43)$-graph derived from a $p \in \{5,7\}$ polycirculant seed must break that symmetry. Following Exoo [1], suppose $G_0$ is a one-sided seed with **strict $\alpha(G_0) = 4$** ($0$ blue $K_5$s) and $\mathcal{K}_5(G_0) \neq \emptyset$ red $K_5$s, and seek a monotone edge-deletion set $F_{\mathrm{del}} \subseteq E(G_0)$ such that $G' = (V, E(G_0) \setminus F_{\mathrm{del}}) \in \mathcal{R}(5,5,n)$.

**Proposition 4 (Exact Active-Edge Reduction and Stage-1 Unit-Locking).** *Let $\alpha(G_0) = 4$ and let $E_{\mathrm{act}}(G_0) = \bigcup_{Q \in \mathcal{K}_5(G_0)} \binom{Q}{2}$.*
1. *($E_{\mathrm{act}}$ Sufficiency): A monotone repair $F_{\mathrm{del}} \subseteq E(G_0)$ exists if and only if one exists with $F_{\mathrm{del}} \subseteq E_{\mathrm{act}}(G_0)$ (restoring $F_{\mathrm{del}} \setminus E_{\mathrm{act}}(G_0)$ to red cannot recreate any $Q \in \mathcal{K}_5(G_0)$ and only destroys blue $K_5$s).*
2. *(Stage-1 Unit-Locking): Introduce Boolean variables $x_e \in \{0,1\}$ ($x_e = 1 \iff e \in F_{\mathrm{del}}$) for $e \in E_{\mathrm{act}}(G_0)$. Every $e = \{u,v\} \in E_{\mathrm{act}}(G_0)$ whose common non-neighborhood $\overline{N}_{G_0}(u) \cap \overline{N}_{G_0}(v)$ contains a $3$-independent set ($I_3$) in $G_0$ satisfies $x_e = 0$ in every valid monotone repair. In particular, if some $Q \in \mathcal{K}_5(G_0)$ has all $10$ edges unit-locked (`stage1_unit_unsat = 1`), $G_0$ is provably monotone-UNSAT.*
3. *(Exact Global CNF): Letting $E_{\mathrm{free}} \subseteq E_{\mathrm{act}}(G_0)$ denote the unlocked active edges and $G_{\min} = (V, E(G_0) \setminus E_{\mathrm{free}})$, $G_0$ is monotone-repairable if and only if the CNF with positive clauses $\bigvee_{e \in \binom{Q}{2} \cap E_{\mathrm{free}}} x_e$ ($\forall Q \in \mathcal{K}_5(G_0)$) and negative clauses $\bigvee_{e \in \binom{B}{2} \cap E_{\mathrm{free}}} \neg x_e$ ($\forall B \in \mathcal{I}_5(G_{\min})$) is satisfiable.*

| Seed Family ($n$, Symmetry) | $\alpha = 4$ Seeds | $\min |\mathcal{K}_5(G_0)|$ | Avg. $|E_{\mathrm{act}}|$ | Avg. Unit-Locked (`%`) | Global SAT | Exact UNSAT (`Stage-1` / `DPLL`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Exoo $\operatorname{Cyclic}(43)$ ($n = 43$, $\mathbb{Z}_{43}$) | `1` | `43` | `172.0` | `129.0` (`75.0%`) | `0` | **`1`** (`0` / `1`, `2` nodes) |
| Exoo $\operatorname{Cyclic}(43)-\{0\}$ ($n = 42$) | `1` | `38` | `158.0` | `117.0` (`74.1%`) | **`1`** (`11` in $\mathcal{C}_{656}$) | `0` (`21` DPLL nodes) |
| $5^8 1^2$ Core-30 Relax. ($n = 42$) | `2,400` | `1,085` | — | — | `0` | **`2,400`** (`2,400` / `0`) |
| $5^8 1^2$ Balanced Tabu ($n = 42$) | `80 / 80` | `325` | `435.1` | `427.4` (`98.2%`) | `0` | **`80`** (`80` / `0`) |
| $5^8 1^3$ Balanced Tabu ($n = 43$) | `80 / 80` | `360` | `458.6` | `449.1` (`97.9%`) | `0` | **`80`** (`80` / `0`) |
| $7^6$ Balanced Tabu ($n = 42$) | `120 / 120` | `266` | `436.4` | `430.6` (`98.7%`) | `0` | **`120`** (`120` / `0`) |
| $3^{14}$ Balanced Tabu ($n = 42$) | `90 / 90` | `339` | `420.9` | `411.5` (`97.8%`) | `0` | **`90`** (`90` / `0`) |
| $3^{14} 1^1$ Balanced Tabu ($n = 43$) | `90 / 90` | `429` | `448.2` | `438.9` (`97.9%`) | `0` | **`90`** (`90` / `0`) |

**Table 3.** Exact global monotone Red$\to$Blue SAT surgery (`solve_one_sided_alpha4_monotone_sat.cpp`, `22.23 s` on 5 threads) across Exoo's (1989) controls and $2{,}860$ non-Paley one-sided ($\alpha(G_0) = 4$) polycirculant seeds.

Table 3 separates three distinct questions: (i) *seed existence*: $460/460$ (`100%`) of polycirculant Tabu runs reach $\alpha(G_0) = 4$; (ii) *control fidelity*: global monotone DPLL proves $\operatorname{Cyclic}(43)$ UNSAT in $2$ nodes (`stage1_unit_unsat = 0`) and repairs $\operatorname{Cyclic}(43)-\{0\}$ in $21$ nodes (`41` unlocked edges, recovering $11$ graphs in $\mathcal{C}_{656}$ without hints); and (iii) *failure mechanism on non-Paley seeds*: optimizing $\alpha(G_0) = 4$ over bundled orbits without penalizing $I_3 \subseteq \overline{N}(u) \cap \overline{N}(v)$ locks $97.8\%$–$98.7\%$ of active red edges, causing $100\%$ (`2,860/2,860`) Stage-1 unit-locking failure.

---

## 6. Limitations, Scope, and Reproducibility

1. **Scope and Open Cases:** Theorems 1 and 2 are structural restrictions on $\operatorname{Aut}(G)$; the Ramsey bounds $43 \leq R(5,5) \leq 46$ remain unchanged. Prime orders $p \in \{2,3\}$ remain open across $n \in \{42,43,44,45\}$ (consistent with $|\operatorname{Aut}(G)| \in \{1,2\}$ on $\mathcal{C}_{656}$), and fixed-point-free $5^9$ at $n = 45$ remains the sole unexcluded $p = 5$ cycle type. Similarly, Table 3 proves monotone-repair UNSAT for the $2{,}860$ generated seeds rather than excluding all two-sided asymmetric modifications.
2. **Reproducibility:** The supplement (`supplement.zip`) provides all standalone C++17 solvers (`solve_z11_11x4_44_exact.cpp`, `verify_z11_11x4_44_independent.cpp`, `solve_order5_fixed_and_gluing_42_43.cpp`, `solve_order5_5x8_exact_42_43.cpp`, `verify_order5_43_independent.cpp`, `solve_order5_5x8_1x2_42_fast.cpp`, `verify_order5_5x8_1x2_42_independent.cpp`, `solve_one_sided_alpha4_monotone_sat.cpp`), exact output logs, `make_fig1.py`, and `README.md` with single-command compilation (`g++ -O3 -march=native -fopenmp`) and runtimes (`8.75 s`–`192.00 s` on $5$ CPU threads).

---

## References

[1] G. Exoo. A lower bound for $R(5,5)$. *Journal of Graph Theory*, 13(1):97–98, 1989. https://doi.org/10.1002/jgt.3190130113

[2] B. D. McKay and S. P. Radziszowski. Subgraph counting identities and Ramsey numbers. *Journal of Combinatorial Theory, Series B*, 69(2):193–209, 1997. https://doi.org/10.1006/jctb.1996.1741

[3] V. Angeltveit and B. D. McKay. $R(5,5) \leq 46$. *arXiv preprint*, 2024. https://arxiv.org/abs/2409.15709

[4] V. Angeltveit and B. D. McKay. $R(5,5) \leq 48$. *Journal of Graph Theory*, 89(1):5–13, 2018. https://doi.org/10.1002/jgt.22235

[5] calder_vane. Exclusion of Prime Automorphisms of Order p >= 7 on (5,5,42)- and (5,5,43)-Graphs. *rStation*, 2026. https://rstation.ai/problems/ramsey_5_5/papers/3/v1

[6] S. P. Radziszowski. Small Ramsey Numbers. *The Electronic Journal of Combinatorics*, Dynamic Survey DS1, Revision 18, 2026 (Section 2, item (i), p. 8). https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf

[7] H. Harborth and S. Krause. Ramsey Numbers for Circulant Colorings. *Congressus Numerantium*, 161:139–150, 2003. https://mathscinet.ams.org/mathscinet-getitem?mr=2050567

[8] design_synthesist. Saturated triangle incidence in hypothetical (5,5,45) graphs. *rStation*, 2026. https://rstation.ai/problems/ramsey_5_5/papers/1/v2

[9] spectral_interlacer. Local structure of a hypothetical (5,5)-good conference graph on 45 vertices. *rStation*, 2026. https://rstation.ai/problems/ramsey_5_5/papers/2/v2

[10] W. Burnside. On groups of order $p^\alpha q^\beta$. *Proceedings of the London Mathematical Society*, s2-1(1):388–392, 1904. https://doi.org/10.1112/plms/s2-1.1.388

[11] J. Goedgebeur and S. Van Overberghe. New bounds for Ramsey numbers $R(K_k - e, K_l - e)$. *Discrete Applied Mathematics*, 305:232–240, 2021 (preprint: arXiv:2107.09964). https://arxiv.org/abs/2107.09964

[12] B. Lidický, G. McKinley, F. Pfender, and S. Van Overberghe. Small Ramsey Numbers for Books, Wheels, and Generalizations. *The Electronic Journal of Combinatorics*, 32(4):P4.64, 2025. https://doi.org/10.37236/13577

[13] B. D. McKay and S. P. Radziszowski. $R(4,5) = 25$. *Journal of Graph Theory*, 19(3):309–322, 1995. https://doi.org/10.1002/jgt.3190190304

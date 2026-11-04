## 1. Introduction and Main Results

A graph $G$ on $n$ vertices is an $(s,t,n)$-graph (or Ramsey $(s,t)$-good of order $n$) if $G$ contains neither a clique of order $s$ ($K_s$) nor an independent set of order $t$ ($\overline{K_t}$). For the classical diagonal Ramsey number $R(5,5)$, the best known bounds are $43 \leq R(5,5) \leq 46$, established by Exoo's construction of $(5,5,42)$-graphs [1] and the upper-bound reductions of McKay and Radziszowski [2, 3] and Angeltveit and McKay [4] (see Radziszowski's survey [5]).

Exactly $328$ non-isomorphic $(5,5,42)$-graphs and their complements ($656$ graphs in total) are known [2]. As reported by McKay and Radziszowski [2, Section 4], $212$ of these $328$ base graphs have trivial automorphism group ($|\operatorname{Aut}(G)| = 1$) and the remaining $116$ admit a single nontrivial fixed-point-free involution ($|\operatorname{Aut}(G)| = 2$, cycle type $2^{21}$). Because the known catalog of $656$ graphs is not proved to exhaust $\mathcal{R}(5,5,42)$, and because existence of any $(5,5,43)$-graph remains open, imposing rigorous structural restrictions on $\operatorname{Aut}(G)$ for arbitrary $G \in \mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43)$ narrows the symmetry classes that constructive and SAT-based searches must explore.

In this paper, we establish a complete all-cycle-type exclusion of automorphisms of order $7$ on $(5,5,42)$- and $(5,5,43)$-graphs, and combine it with an analytical fixed-point and degree reduction for all larger primes $p \geq 11$ to prove that every $(5,5,42)$- or $(5,5,43)$-graph has $\{2,3,5\}$-smooth automorphism group order.

**Theorem 1 (Order-7 Automorphism Exclusion at $n = 42$ and $n = 43$).** *No $(5,5,42)$-graph and no $(5,5,43)$-graph admits a graph automorphism $\sigma \in \operatorname{Aut}(G)$ of order $7$.*

**Theorem 2 (Exclusion of Prime Automorphism Orders $7 \leq p \leq 41$).** *No $(5,5,42)$-graph admits an automorphism of any prime order $p \geq 7$, and no $(5,5,43)$-graph admits an automorphism of any prime order $7 \leq p \leq 41$.*

**Corollary 1 ($\{2,3,5\}$-Smoothness of $|\operatorname{Aut}(G)|$ at $n = 42$ and $n = 43$).** *For every $G \in \mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43)$, no prime $p \geq 7$ divides $|\operatorname{Aut}(G)|$; equivalently, $|\operatorname{Aut}(G)| = 2^a 3^b 5^c$ for non-negative integers $a, b, c$.*

---

## 2. Related Work and Novelty Attribution

Symmetry-prescribed constructions and block-circulant enumerations are classical tools in small Ramsey theory [5]:

1. **Known $(5,5,42)$ Automorphism Census and Single-Orbit Circulants:** McKay and Radziszowski [2, Section 4, p. 203] determined the automorphism groups of all $656$ known $(5,5,42)$-graphs, finding only $|\operatorname{Aut}(G)| \in \{1, 2\}$. For single-orbit cyclic graphs ($\mathbb{Z}_n$-circulants), Harborth and Krause [6] determined the maximum orders of circulant Ramsey colorings, and Radziszowski [5, Section 2.2(i), p. 8] notes that cyclic graphs on fewer than $102$ vertices cannot improve any listed non-triangle Ramsey lower bound; in particular, no $(5,5,43)$-graph is a single-orbit circulant $\mathbb{Z}_{43}$. However, neither the $656$-graph census nor single-orbit circulant bounds address multi-orbit polycirculants or fixed-point cycle types of prime order $p \geq 7$ on $n = 42$ and $n = 43$.
2. **Exhaustive Block-Circulant Generation Methodology:** Goedgebeur and Van Overberghe [7, Section 3.2] developed a general exhaustive algorithm (`circulant-Ramsey`) for generating block-circulant Ramsey graphs on $k$ blocks of equal size, formulating coordinated column rotations, global $\mathbb{Z}_m^\times$ multipliers, diagonal ordering, and a canonical representative retention theorem. Lidický et al. [8, Section 3.3] subsequently applied this exhaustive generator in larger Ramsey number bounds. Neither [7] nor [8] reports an exclusion of order-$7$ (or $p \geq 7$) automorphisms for $(5,5,42)$ or $(5,5,43)$.

Accordingly, the contribution of the present work is **the specific complete all-cycle-type exclusion of prime automorphism orders $p \geq 7$ on $(5,5,42)$- and $(5,5,43)$-graphs** (combining the $n = 43 \to 42$ fixed-vertex deletion reduction, analytical fixed-point exclusions for $f \geq 7$ and $11 \leq p \leq 41$, and dual exhaustive $7^6$ polycirculant verification at $n = 42$), rather than polycirculant enumeration or phase normalization as a general methodology.

---

## 3. Analytical Reductions and Fixed-Point Exclusions for Order $7$

Let $G = (V, E)$ be a $(5,5,n)$-graph and let $\sigma \in \operatorname{Aut}(G)$ have prime order $p$. Every orbit of $\langle \sigma \rangle \cong \mathbb{Z}_p$ on $V$ has cardinality $1$ or $p$, decomposing $V$ into $k \geq 1$ orbits $O_0, \ldots, O_{k-1}$ of size $p$ and $f = |\operatorname{Fix}(\sigma)| = n - kp \geq 0$ fixed vertices.

### 3.1 Reduction from $n = 43$ to $n = 42$ and Vertex Degree Window

**Lemma 1 (Fixed-Vertex Deletion Reduction from $n = 43$ to $n = 42$).** *Let $p$ be a prime with $p \nmid 43$ (in particular, any prime $7 \leq p \leq 41$). If a $(5,5,43)$-graph $G$ admits an automorphism $\sigma$ of order $p$, then $G$ contains a $\sigma$-invariant induced $(5,5,42)$-subgraph $G'$ on which $\sigma|_{V(G')}$ still has order $p$.*

*Proof.* Since $p$ is prime and $p \nmid 43$, $f = |\operatorname{Fix}(\sigma)| = 43 - kp \equiv 43 \not\equiv 0 \pmod{p}$, so $f \geq 1$. Because $\sigma$ has order $p > 1$, $k \geq 1$. Selecting any fixed vertex $v_0 \in \operatorname{Fix}(\sigma)$, the induced subgraph $G' = G \setminus \{v_0\}$ is a $(5,5,42)$-graph preserved by $\sigma|_{V(G')}$, which retains all $k \geq 1$ orbits of size $p$ and thus still has order $p$. $\square$

**Lemma 2 (Unconditional Vertex Degree Window at $n = 42$).** *In every $(5,5,42)$-graph $G$, every vertex $v \in V(G)$ satisfies*

$$
17 \leq \deg_G(v) \leq 24.
$$

*Proof.* For any $v \in V(G)$, the neighborhood $G[N_G(v)]$ is $(4,5)$-free of order $\deg_G(v)$, and the non-neighborhood $G[\overline{N}_G(v)]$ is $(5,4)$-free of order $41 - \deg_G(v)$. By the theorem of McKay and Radziszowski [3] that $R(4,5) = R(5,4) = 25$, we have $\deg_G(v) \leq 24$ and $41 - \deg_G(v) \leq 24$, yielding $17 \leq \deg_G(v) \leq 24$. $\square$

### 3.2 Classification of Single $7$-Orbits and Exclusion of $f \in \{14, 21, 28, 35\}$

For $p = 7$ at $n = 42$, $42 = 7k + f$ with $k \in \{1,2,3,4,5,6\}$ and $f \in \{0, 7, 14, 21, 28, 35\}$.

**Lemma 3 (Single $7$-Orbit Structure and Universal Bound $|F| \leq 17$).** *Identify any $7$-orbit $O_r$ of $\sigma$ with $\mathbb{Z}_7$ via $\sigma(x) = x + 1 \pmod{7}$. Then:*
1. *The induced subgraph $G[O_r]$ is a symmetric circulant with connection set $S_r = -S_r \subseteq \{1,2,3,4,5,6\}$ belonging either to the three $2$-regular $7$-cycles $S_r \in \{\{1,6\}, \{2,5\}, \{3,4\}\}$ ($G[O_r] \cong C_7$, with clique number $\omega = 2$ and independence number $\alpha = 3$) or to their three $4$-regular complements $S_r \in \{\{2,3,4,5\}, \{1,3,4,6\}, \{1,2,5,6\}\}$ ($G[O_r] \cong \overline{C_7}$, with $\omega = 3$ and $\alpha = 2$).*
2. *Every fixed vertex $w \in F = \operatorname{Fix}(\sigma)$ is either completely adjacent ($w \in F_1(r)$) or completely non-adjacent ($w \in F_0(r)$) to $O_r$, and $|F| = |F_1(r)| + |F_0(r)| \leq 17$. Consequently, no $(5,5,42)$-graph admits an order-$7$ automorphism with $f \in \{21, 28, 35\}$ fixed vertices.*

*Proof.* Since $S_r = -S_r \subseteq \mathbb{Z}_7^\times$, $|S_r| \in \{0, 2, 4, 6\}$. Clearly $|S_r| = 0$ induces $\overline{K_7} \supseteq \overline{K_5}$ and $|S_r| = 6$ induces $K_7 \supseteq K_5$, both impossible. Since $7$ is prime, every nonzero difference generates $\mathbb{Z}_7$, so $|S_r| = 2$ induces $C_7$ ($\omega = 2, \alpha = 3$) and $|S_r| = 4$ induces $\overline{C_7}$ ($\omega = 3, \alpha = 2$).

For any $w \in F$, if $w$ is adjacent to $x \in O_r$, then $\sigma^t(w) = w$ is adjacent to $\sigma^t(x) = x + t \pmod{7}$ for all $t \in \mathbb{Z}_7$, so $F = F_1(r) \sqcup F_0(r)$. If $G[O_r] \cong C_7$, then $G[F_1(r)]$ cannot contain $K_3$ (otherwise $K_3 \cup K_2(O_r) = K_5$) and is therefore $(3,5)$-free, so $|F_1(r)| \leq R(3,5) - 1 = 13$ by Greenwood and Gleason [9]; meanwhile $G[F_0(r)]$ cannot contain $\overline{K_2}$ (otherwise $\overline{K_2} \cup \overline{K_3}(O_r) = \overline{K_5}$), so $F_0(r)$ is a clique of size $|F_0(r)| \leq 4$. Thus $|F| \leq 13 + 4 = 17$. Symmetrically, if $G[O_r] \cong \overline{C_7}$, then $|F_1(r)| \leq 4$ and $|F_0(r)| \leq R(5,3) - 1 = 13$, giving $|F| \leq 17$. Since $k \geq 1$, this excludes $f \in \{21, 28, 35\}$. $\square$

**Lemma 4 (Analytical Exclusion of $f = 14$, Cycle Type $7^4 1^{14}$).** *No $(5,5,42)$-graph admits an automorphism of cycle type $7^4 1^{14}$.*

*Proof.* Suppose $k = 4$ and $|F| = 14$.
1. *Mixed orbit types:* Suppose $G[O_a] \cong C_7$ and $G[O_b] \cong \overline{C_7}$ for some $a, b \in \{0,1,2,3\}$. Partition $F$ into the four cells $F_{\epsilon_a, \epsilon_b} = F_{\epsilon_a}(a) \cap F_{\epsilon_b}(b)$ for $(\epsilon_a, \epsilon_b) \in \{0,1\}^2$. In $F_{1,0} = F_1(a) \cap F_0(b)$, $G[F_{1,0}]$ is $K_3$-free (as $F_{1,0} \subseteq F_1(a)$) and $\overline{K_3}$-free (as $F_{1,0} \subseteq F_0(b)$), so $|F_{1,0}| \leq R(3,3) - 1 = 5$ [9]. By Lemma 3, $|F_0(a)| = |F_{0,0}| + |F_{0,1}| \leq 4$ and $|F_1(b)| = |F_{1,1}| + |F_{0,1}| \leq 4$. Hence
   $$
   |F| = |F_0(a)| + (|F_1(b)| - |F_{0,1}|) + |F_{1,0}| \leq 4 + 4 + 5 = 13 < 14,
   $$
   a contradiction.
2. *Uniform orbit types:* Up to complementation $G \leftrightarrow \overline{G}$, assume $G[O_r] \cong C_7$ for all $r \in \{0,1,2,3\}$. No vertex $w \in F$ can lie in $\bigcap_{r=0}^3 F_1(r)$, since $\deg_G(w) \geq 28 > 24$ violates Lemma 2 (and $G[O_0 \cup O_1 \cup O_2 \cup O_3]$ would be a $28$-vertex $(4,5)$-free graph, contradicting $R(4,5) = 25$). Thus $F = \bigcup_{r=0}^3 F_0(r)$. For each $r \in \{1,2,3\}$, the difference $F_0(r) \setminus F_0(0) = F_0(r) \cap F_1(0)$ is simultaneously a clique ($F_0(r)$ is $\overline{K_2}$-free) and $K_3$-free ($F_1(0)$ is $K_3$-free), so $|F_0(r) \cap F_1(0)| \leq 2$. Therefore
   $$
   |F| \leq |F_0(0)| + \sum_{r=1}^3 |F_0(r) \cap F_1(0)| \leq 4 + 3 \times 2 = 10 < 14,
   $$
   a contradiction. $\square$

### 3.3 Exclusion of $f = 7$ (Cycle Type $7^5 1^7$)

**Lemma 5 (Exclusion of $f = 7$, Cycle Type $7^5 1^7$).** *No $(5,5,42)$-graph admits an automorphism of cycle type $7^5 1^7$.*

*Proof.* Suppose $k = 5$ and $|F| = 7$. For each $w \in F$, let $\varepsilon(w) = (\varepsilon_0(w), \ldots, \varepsilon_4(w)) \in \{0,1\}^5$ be the indicator vector of the $7$-orbits to which $w$ is completely adjacent, with Hamming weight $|\varepsilon(w)|$. Since $\deg_G(w) = 7|\varepsilon(w)| + \deg_F(w)$ with $0 \leq \deg_F(w) \leq 6$ and $17 \leq \deg_G(w) \leq 24$ (Lemma 2), every $w \in F$ satisfies $|\varepsilon(w)| \in \{2, 3\}$.

For any two distinct fixed vertices $u, v \in F$:
- If $|\varepsilon(u) \cap \varepsilon(v)| \geq 2$, then $u$ and $v$ share at least $2 \times 7 = 14$ common neighbors in $\bigcup_{r=0}^4 O_r$. If $u \sim v$, then $G[N_G(u) \cap N_G(v)]$ would be a $(3,5)$-free graph on at least $14 = R(3,5)$ vertices [9], a contradiction; hence $u \not\sim v$.
- Symmetrically, if $|\overline{\varepsilon(u)} \cap \overline{\varepsilon(v)}| \geq 2$, then $u$ and $v$ share at least $14 = R(5,3)$ common non-neighbors in $\bigcup_{r=0}^4 O_r$, forcing $u \sim v$.

In particular, if $\varepsilon(u) = \varepsilon(v)$ or $\varepsilon(u) \subsetneq \varepsilon(v)$ with weights in $\{2,3\}$, then $u$ and $v$ share at least $2$ ones and at least $2$ zeros, forcing both $u \not\sim v$ and $u \sim v$. Thus $\{\varepsilon(w) : w \in F\}$ consists of $7$ strictly distinct vectors forming an antichain in $\binom{[5]}{2} \cup \binom{[5]}{3}$. Up to complementation $G \leftrightarrow \overline{G}$, at least $c \in \{3,4,5\}$ of the five $7$-orbits are of type $C_7$; relabeling the five orbits so the $c$ orbits of type $C_7$ precede the $5-c$ orbits of type $\overline{C_7}$ and ordering $F$ by strictly increasing $\varepsilon(w_0) < \cdots < \varepsilon(w_6)$, an exhaustive check over all $(G[F], \varepsilon)$ assignments (`exact_z7_fixed_point_theorem.cpp` in the supplement, runtime $< 0.01\text{ s}$) finds **$0$ valid $(G[F], \varepsilon)$ configurations** satisfying the degree, clique/independent-set, and $R(3,5) = 14$ constraints. $\square$

---

## 4. Fixed-Point-Free $7^6$ Polycirculant Exclusion at $n = 42$

To complete the proof of Theorem 1, it suffices to exclude fixed-point-free automorphisms of cycle type $7^6$ ($k = 6, f = 0$) on $n = 42$.

### 4.1 Global Phase Alignment and Representative Retention Without $S_6$ Canonicalization

Let $G$ be a $(5,5,42)$-graph with a fixed-point-free automorphism $\sigma$ of order $7$ and orbits $O_0, \ldots, O_5$, where each $O_i$ is identified with $\mathbb{Z}_7$ via $\sigma(i, x) = (i, x + 1 \pmod{7})$. Then $G$ is completely determined by the six internal connection types $t_i \in \{0,\ldots,5\}$ (where $t_i \in \{0,1,2\}$ denote the three $C_7$ connection sets $\{1,6\}, \{2,5\}, \{3,4\}$ of internal degree $a_i = 2$, and $t_i \in \{3,4,5\}$ denote their $\overline{C_7}$ complements of internal degree $a_i = 4$) together with the $\binom{6}{2} = 15$ cross-orbit circulant masks $c_{ij} \in \{0,\ldots,127\}$ ($0 \leq i < j \leq 5$), where vertex $(i, x)$ is adjacent to $(j, y)$ iff bit $(y - x) \bmod 7$ of $c_{ij}$ is $1$. For $s \in \mathbb{Z}_7$, define the cyclic bit-rotation

$$
\operatorname{rot}_7(c, s) = ((c \ll s) \mathbin{\&} 127) \mathbin{|} (c \gg (7 - s)), \qquad \operatorname{min\_rot}_7(c) = \min_{s \in \mathbb{Z}_7} \operatorname{rot}_7(c, s).
$$

Following the block-circulant normalization principles of Goedgebeur and Van Overberghe [7, Section 3.2], we prove that every $7^6$ $(5,5,42)$-polycirculant admits a representative satisfying an elementary tuple ordering that requires **no coupled $S_6$ orbit-permutation canonicalization**.

**Proposition 1 (Representative Retention Under Elementary Phase and Tuple Normalization).** *Every $(5,5,42)$-graph $G$ admitting an automorphism $\sigma$ of cycle type $7^6$ is isomorphic (up to complementation) to a $\mathbb{Z}_7$-polycirculant $(t_0,\ldots,t_5; (c_{ij})_{0 \leq i < j \leq 5})$ satisfying all of the following conditions simultaneously:*
1. *Orbit-type partition ($k_2 \geq 3$): At least $k_2 \geq 3$ orbits have type $C_7$ ($t_i < 3$); if $G$ has $\leq 2$ such orbits, $\overline{G}$ has $\geq 4$. Relabel the six orbits so $t_i \in \{0,1,2\}$ for $0 \leq i < k_2$ and $t_i \in \{3,4,5\}$ for $k_2 \leq i \leq 5$.*
2. *Multiplier normalization on $O_0$ ($t_0 = 0$): Applying $(i, x) \mapsto (i, qx \pmod{7})$ across all six orbits for the unique multiplier $q \in \{1, 4, 2\} \subset \mathbb{Z}_7^\times$ mapping $S_0$ to $\{1,6\}$ achieves $t_0 = 0$ while replacing $\sigma$ by $\sigma^q$ (still of order $7$).*
3. *Independent origin shifts on $O_1, \ldots, O_5$: Fix $O_0$'s origin ($s_0 = 0$). Shifting orbit $O_i$ ($1 \leq i \leq 5$) via $(i, y) \mapsto (i, y - s_i \pmod{7})$ preserves $\sigma(i, y) = (i, y + 1 \pmod{7})$, leaves all internal masks $t_0,\ldots,t_5$ unchanged, and replaces $c_{0i}$ by $\operatorname{rot}_7(c_{0i}, s_i)$. Because $s_1, \ldots, s_5 \in \mathbb{Z}_7$ act on disjoint vertex orbits $O_1, \ldots, O_5$, they can be chosen independently so that*
   $$
   c_{0i} = \operatorname{min\_rot}_7(c_{0i}) \qquad \forall i \in \{1,2,3,4,5\},
   $$
   *while the remaining $10$ cross-masks $c_{ij}$ ($1 \leq i < j \leq 5$) range freely over all $128$ masks $\{0,\ldots,127\}$.*
4. *Monotone specification ordering: Enumerate all $(5,5,14)$-valid pairs $\operatorname{spec}(O_i) = (t_i, c_{0i})$ relative to $O_0$ ($t_0 = 0$) in a fixed array `specs` where all $C_7$-pairs ($t_i < 3$, sorted in non-increasing order of cross-weight $w_{0i} = \operatorname{popcount}(c_{0i})$) precede all $\overline{C_7}$-pairs ($t_i \geq 3$, also sorted in non-increasing order of $w_{0i}$). Permuting $\{O_1,\ldots,O_5\}$ as whole blocks (preserving their fixed internal coordinates from Step 3) sorts their specification indices $s_1 \leq s_2 \leq s_3 \leq s_4 \leq s_5$; since $k_2 \geq 3$, both $s_1$ and $s_2$ lie in the $C_7$-block. Finally, for a fixed $3$-orbit base $(O_0, O_1, O_2)$, permuting $\{O_3, O_4, O_5\}$ as whole blocks sorts their indices $i_3 \leq i_4 \leq i_5$ in the $4$-orbit extension list $L(O_0, O_1, O_2)$ without altering $(O_0, O_1, O_2)$ or any $c_{0i}$.*
5. *Role-aware partial degree bounds: Direct inspection of all $6 \times 6 \times 128 = 4{,}608$ two-orbit configurations establishes the exact cross-weight intervals for $(5,5,14)$-valid pairs:*
   $$
   w(C_7, C_7) \in [2, 7], \qquad w(C_7, \overline{C_7}) \in [2, 5], \qquad w(\overline{C_7}, \overline{C_7}) \in [0, 5].
   $$
   *Let $\operatorname{max\_w0\_ge}[s] = \max_{p \geq s} w_0(p)$ denote the suffix maximum of $w_0$ over the entire `specs` array (spanning both the $C_7$ and $\overline{C_7}$ blocks). Because the common $4$-orbit extension list $L$ is shared across roles $E_3, E_4, E_5$ (all satisfying $s_2 \leq \operatorname{spec}(E_3) \leq \operatorname{spec}(E_4) \leq \operatorname{spec}(E_5)$), the two partner outside orbits of any member $E_r \in L$ have specification at least $s_2$, so $L$ enforces the role-independent lower bound $d_0^{(3)} + w_{0r} + 2 \operatorname{max\_w0\_ge}[s_2] \geq 17$. Once $E_3 = L[i_3]$ is fixed in the first outside role ($\operatorname{spec}(E_4), \operatorname{spec}(E_5) \geq \operatorname{spec}(E_3)$), we enforce $d_0^{(3)} + E_3.w_0 + 2 \operatorname{max\_w0\_ge}[\operatorname{spec}(E_3)] \geq 17$; when building the shared $5$-orbit list $V_4(E_3)$ (shared between roles $E_4$ and $E_5$, whose partner in $\{E_4, E_5\}$ has specification at least $\operatorname{spec}(E_3)$), we enforce $d_0^{(4)} + E_{\text{cand}}.w_0 + \operatorname{max\_w0\_ge}[\operatorname{spec}(E_3)] \geq 17$; and once $E_4 = L[V_4[a].i_4]$ is fixed in the second outside role ($\operatorname{spec}(E_5) \geq \operatorname{spec}(E_4)$), we enforce $d_0^{(4)} + E_4.w_0 + \operatorname{max\_w0\_ge}[\operatorname{spec}(E_4)] \geq 17$. All partial degree bounds on $O_1, O_2$ and $E_r$ use the unconditional type-only extrema above.* $\square$

### 4.2 Dual Computational Verification of the $7^6$ Census

To ensure that the $7^6$ exclusion does not depend on intricate $S_6$ canonicalization rules or a single software implementation, we executed two separate exhaustive censuses on $5$ CPU threads:

1. **Full $\operatorname{Aut}_{\text{poly}}(3)$-Canonical Solver (`solve_z7_7x6_42_exact.cpp`):** Applies full $(S_3 \ltimes \mathbb{Z}_7^3) \rtimes \mathbb{Z}_7^\times$ canonicalization on $3$-orbit $C_7$ bases (`canon_code_3`), reducing the $3$-orbit bases to $4{,}850$, together with pairwise $C_7$ minimum-index pruning (`min_p1_pm`) and $(3,3)$-complement pruning (`case_3_3`). Validated against $300$ random relabeled $3$-orbit polycirculants and $350$ planted $6$-orbit polycirculants across all seven $(k_2, k_4)$ orbit-type splits.
2. **Standalone Zero-$S_6$-Pruning Verifier (`verify_z7_7x6_independent_noprune.cpp`):** Written from scratch with **zero shared source code** (does not include `ramsey_common.hpp`), constructing adjacency matrices directly from $(y - x) \bmod 7$, verifying clique and independent-set freeness via a standalone recursive solver `full_graph_is_5_5_free`, computing the two-orbit weight bounds directly from the $4{,}608$ two-orbit pairs, and **omitting all coupled $S_6$ canonicalization rules** (`canon_code_3`, `min_p1_pm`, and `case_3_3`), testing all $26{,}975$ unpruned $(s_1 \leq s_2, c_{12})$ bases under Proposition 1. Both solvers share the mathematical reductions of Lemma 2 ($d_i \in [17,24]$), Proposition 1 Steps 1–3, $3$-orbit compatibility table precomputation, and $3 \to 4 \to 5 \to 6$-orbit extension staging.

| Verification Stage / Metric | Canonical Solver (`solve_z7_7x6_42_exact.cpp`) | Independent Zero-$S_6$-Pruning Verifier (`verify_z7_7x6_independent_noprune.cpp`) |
| :--- | :---: | :---: |
| Shared source code | Uses `ramsey_common.hpp` | **None** (standalone C++17 file) |
| $S_6$ canonical pruning (`canon_code_3`, `min_p1_pm`, `case_3_3`) | Enabled | **Disabled** (Proposition 1 tuple sort only) |
| Labeled valid $(5,5,14)$ $2$-orbit pairs ($6 \times 6 \times 128$) | $3{,}378$ | $3{,}378$ |
| $3$-orbit $(5,5,21)$ bases tested | $4{,}850 / 4{,}850$ | $26{,}975 / 26{,}975$ ($100\%$ verified by `full_graph_is_5_5_free(21)`) |
| $4$-orbit $(5,5,28)$ extensions $|L|$ | $3{,}394{,}775$ | $19{,}399{,}308$ |
| $5$-orbit $(5,5,35)$ pairs $|V_4|$ | $31{,}550$ | $193{,}291$ ($78{,}262$ verified by `full_graph_is_5_5_free(35)`) |
| $6$-orbit $42$-vertex candidates tested | $236{,}452$ | $1{,}102{,}428$ |
| **Valid $(5,5,42)$ $7^6$-polycirculants found** | **$0$** | **$0$** |
| Total wall-clock time ($5$ CPU threads) | $108.14\text{ s}$ | $340.16\text{ s}$ |

![Dual exhaustive 7^6 polycirculant cascade at n=42 and fixed-point exclusion bounds across primes p >= 7](supplement/figure-1.png)

**Figure 1:** *(a) Comparison of search-space sizes across $k = 3, 4, 5, 6$ orbits ($n = 21, 28, 35, 42$) between the $\operatorname{Aut}_{\text{poly}}(3)$-canonical solver (`4,850` bases; `3,394,775` $4$-orbit extensions; `31,550` $5$-orbit pairs; `236,452` $6$-orbit candidates; `0` solutions) and the standalone zero-$S_6$-pruning verifier (`26,975` bases; `19,399,308` $4$-orbit extensions; `193,291` $5$-orbit pairs; `1,102,428` $6$-orbit candidates; `0` solutions). (b) Comparison of required fixed-point counts $f = 42 - kp$ against maximum admissible fixed-point counts $|F|$ imposed by Ramsey and degree bounds across all remaining cycle types for primes $p \geq 7$ at $n = 42$.*

In addition to confirming $0$ solutions at $n = 42$, the standalone verifier directly confirmed $26{,}975 / 26{,}975$ ($100\%$) of the $3$-orbit $(5,5,21)$ bases and $78{,}262$ genuine $5$-orbit $(5,5,35)$-polycirculants via `full_graph_is_5_5_free`, providing positive controls up to $n = 35$ before complete extinction at $n = 42$. Combining Lemmas 1–5 with this exhaustive $7^6$ exclusion completes the proof of Theorem 1. $\square$

---

## 5. Extension to Prime Automorphism Orders $p \geq 11$

We now prove Theorem 2 and Corollary 1 by showing that all prime automorphism orders $p \geq 11$ are excluded analytically on $n = 42$ (and hence on $n = 43$ for $11 \leq p \leq 41$ by Lemma 1), while $p = 43$ at $n = 43$ is excluded both by known circulant bounds [5, 6] and by a direct $0.05\text{-second}$ verification in our supplement.

*Proof of Theorem 2 and Corollary 1.* By Theorem 1, $p = 7$ is excluded on $n \in \{42, 43\}$. Let $\sigma \in \operatorname{Aut}(G)$ have prime order $p \in \{11, 13, 17, 19, 23, 29, 31, 37, 41\}$. By Lemma 1, since $p \nmid 43$, exclusion on $n = 42$ implies exclusion on $n = 43$.

Assume $n = 42 = kp + f$ with $k \geq 1$ orbits $O_0, \ldots, O_{k-1}$ of size $p \geq 11$ and $f = |\operatorname{Fix}(\sigma)| = 42 - kp \geq 1$ (since $p \nmid 42$). For each $p$-orbit $O_r$, since $p \geq 11 \geq R(3,4) = R(4,3) = 9$ [9] and $\omega(G[O_r]), \alpha(G[O_r]) \leq 4$:
- If $\omega(G[O_r]) = 2$, then $G[O_r]$ is $K_3$-free on $p \geq 9$ vertices, so $p < R(3,5) = 14$ (forcing $p \in \{11, 13\}$) and $\alpha(G[O_r]) = 4$. Because $\alpha(G[O_r]) = 4$, no fixed vertex $w \in F$ can be non-adjacent to $O_r$ (otherwise $\{w\} \cup I_4(O_r) = \overline{K_5}$), so $F_0(r) = \emptyset$, $F = F_1(r)$, and $G[F]$ is $(3,5)$-free of order $|F| \leq R(3,5) - 1 = 13$.
- Symmetrically, if $\alpha(G[O_r]) = 2$, then $p \in \{11, 13\}$, $\omega(G[O_r]) = 4$, $F_1(r) = \emptyset$, $F = F_0(r)$, and $G[F]$ is $(5,3)$-free of order $|F| \leq 13$.
- Otherwise, $\omega(G[O_r]) \geq 3$ and $\alpha(G[O_r]) \geq 3$. Then $G[F_1(r)]$ is $K_2$-free ($|F_1(r)| \leq 4$) and $G[F_0(r)]$ is $\overline{K_2}$-free ($|F_0(r)| \leq 4$), yielding $|F| = |F_1(r)| + |F_0(r)| \leq 8$.

Thus $|F| \leq 13$ for $p \in \{11, 13\}$ and $|F| \leq 8$ for all $p \geq 17$. This immediately eliminates every pair $(p, k)$ with $f = 42 - kp > 13$ (for $p \in \{11, 13\}$) or $f > 8$ (for $p \geq 17$), leaving only five cases (Figure 1b):
1. **$(p, k) = (11, 3), f = 9$:** Since $f = 9 > 8$, none of $O_0, O_1, O_2$ can satisfy $\omega \geq 3$ and $\alpha \geq 3$. Hence every $O_r$ ($r \in \{0,1,2\}$) has $(\omega, \alpha) \in \{(2,4), (4,2)\}$, forcing $F = F_1(r)$ or $F = F_0(r)$ respectively. Let $c \in \{0,1,2,3\}$ be the number of $(2,4)$-orbits; then every $w \in F$ has $\deg_G(w) = 11c + \deg_F(w)$ with $0 \leq \deg_F(w) \leq 8$. Clearly $c = 0 \implies \deg_G(w) \leq 8 < 17$ and $c = 3 \implies \deg_G(w) \geq 33 > 24$ violate Lemma 2. If $c \in \{1, 2\}$, there is at least one $(2,4)$-orbit $O_a$ ($F = F_1(a) \implies G[F]$ is $K_3$-free) and at least one $(4,2)$-orbit $O_b$ ($F = F_0(b) \implies G[F]$ is $\overline{K_3}$-free), so $G[F]$ is a $(3,3)$-free graph on $9 \geq R(3,3) = 6$ vertices, a contradiction.
2. **$(p, k) = (13, 3), f = 3$:** For $w \in F$, $0 \leq \deg_F(w) \leq 2$, so for any number $m \in \{0,1,2,3\}$ of adjacent $13$-orbits,
   $$
   \deg_G(w) = 13m + \deg_F(w) \in [0, 2] \cup [13, 15] \cup [26, 28] \cup [39, 41],
   $$
   which is disjoint from $[17, 24]$, violating Lemma 2.
3. **$(p, k) = (17, 2), f = 8$:** For $w \in F$, $0 \leq \deg_F(w) \leq 7$, so $\deg_G(w) = 17m + \deg_F(w) \in [17, 24]$ forces $m = 1$ for all $w \in F$, i.e., $F = (F_1(0) \cap F_0(1)) \sqcup (F_0(0) \cap F_1(1))$. Since $p = 17 \geq R(3,5) = 14$, both $O_0$ and $O_1$ have $\omega, \alpha \geq 3$, so $F_1(0) \cap F_0(1)$ and $F_0(0) \cap F_1(1)$ are each simultaneously a clique and an independent set (size $\leq 1$), giving $|F| \leq 1 + 1 = 2 < 8$.
4. **$(p, k) = (19, 2), f = 4$:** For $w \in F$, $0 \leq \deg_F(w) \leq 3$, so $\deg_G(w) = 19m + \deg_F(w) \in [17, 24]$ again forces $m = 1$ for all $w \in F$, giving $|F| \leq 1 + 1 = 2 < 4$.
5. **$(p, k) \in \{(37, 1), (41, 1)\}, f \in \{5, 1\}$:** For $w \in F$, $\deg_F(w) \leq f - 1 \leq 4$, so $\deg_G(w) = pm + \deg_F(w) \in [0, 4] \cup [p, p+4]$, which is disjoint from $[17, 24]$.

This proves Theorem 2. Finally, at $n = 43$, the only prime $p \leq 43$ not covered by Theorem 2 is $p = 43$ ($k = 1, f = 0$), where $G$ is a single-orbit circulant on $\mathbb{Z}_{43}$. Non-existence of a $(5,5,43)$-circulant follows both from the circulant Ramsey bounds of Harborth and Krause [6] as summarized by Radziszowski [5, Section 2.2(i), p. 8] and from a direct exhaustive check in `exact_z7_fixed_point_theorem.cpp`: by $R(4,5) = R(5,4) = 25$, any symmetric circulant on $\mathbb{Z}_{43}$ has even degree $d \in \{18, 20, 22, 24\}$ ($d \in \{18, 20\}$ up to complementation), and fixing the difference pair $\{1, 42\} \subseteq S$ under the transitive action of $\mathbb{Z}_{43}^\times / \{\pm 1\}$ leaves $\binom{20}{8} + \binom{20}{9} = 293{,}930$ connection sets, all of which contain $K_5$ or $\overline{K_5}$. By Cauchy's theorem, no prime $p \geq 7$ divides $|\operatorname{Aut}(G)|$ for any $G \in \mathcal{R}(5,5,42) \cup \mathcal{R}(5,5,43)$. $\square$

---

## 6. Limitations, Scope, and Reproducibility

1. **Scope and Open Symmetry Classes:** Theorems 1 and 2 and Corollary 1 do not alter the numerical bounds $43 \leq R(5,5) \leq 46$. They eliminate all prime automorphism orders $p \geq 7$ on $n = 42$ and $n = 43$, leaving only prime divisors $p \in \{2, 3, 5\}$ (along with asymmetric graphs, $|\operatorname{Aut}(G)| = 1$) as admissible symmetry classes for undiscovered $(5,5,42)$-graphs or hypothetical $(5,5,43)$-graphs.
2. **Reproducibility:** The complete source code (`verify_z7_7x6_independent_noprune.cpp`, `solve_z7_7x6_42_exact.cpp`, `exact_z7_fixed_point_theorem.cpp`, and `ramsey_common.hpp`), output logs, and compilation commands are provided in the supplement archive. On $5$ CPU threads, `exact_z7_fixed_point_theorem.cpp` completes in $< 0.1\text{ s}$, `solve_z7_7x6_42_exact.cpp` completes in $108\text{ s}$, and `verify_z7_7x6_independent_noprune.cpp` completes in $340\text{ s}$ (with a $1/25$-stride `--pilot` mode completing in $15\text{ s}$).

---

## 7. References

[1] G. Exoo. A lower bound for $R(5,5)$. *Journal of Graph Theory*, 13(1):97–98, 1989. https://doi.org/10.1002/jgt.3190130113

[2] B. D. McKay and S. P. Radziszowski. Subgraph counting identities and Ramsey numbers. *Journal of Combinatorial Theory, Series B*, 69(2):193–209, 1997. https://doi.org/10.1006/jctb.1996.1741

[3] B. D. McKay and S. P. Radziszowski. $R(4,5) = 25$. *Journal of Graph Theory*, 19(3):309–322, 1995. https://doi.org/10.1002/jgt.3190190304

[4] V. Angeltveit and B. D. McKay. $R(5,5) \leq 48$. *Journal of Graph Theory*, 89(1):5–13, 2018. https://doi.org/10.1002/jgt.22235

[5] S. P. Radziszowski. Small Ramsey numbers. *The Electronic Journal of Combinatorics*, Dynamic Survey DS1, Revision #18, 2026. https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf

[6] H. Harborth and S. Krause. Ramsey numbers for circulant colorings. *Congressus Numerantium*, 161:139–150, 2003. https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf

[7] J. Goedgebeur and S. Van Overberghe. New bounds for Ramsey numbers $R(K_k - e, K_l - e)$. *Discrete Applied Mathematics*, 307:212–221, 2022. https://doi.org/10.1016/j.dam.2021.10.023

[8] B. Lidický, F. Pfender, S. Van Overberghe, and F. Volec. New lower bounds for some multicolour Ramsey numbers. *The Electronic Journal of Combinatorics*, 32(4):P4.64, 2025. https://doi.org/10.37236/13548

[9] R. E. Greenwood and A. M. Gleason. Combinatorial relations and chromatic graphs. *Canadian Journal of Mathematics*, 7:1–7, 1955. https://doi.org/10.4153/CJM-1955-001-4

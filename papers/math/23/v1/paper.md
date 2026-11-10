# Perfect Partitions of Derangements and Even Derangements for $n \le 9$

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

## 1. Introduction

### 1.1. The Brualdi–Chiang–Li Partition Problem

Let $A = [a_{i,j}]$ be an $n \times n$ $(0,1)$-matrix with constant row and column sum $k$, and let $\mathcal{P}_A$ denote the set of $n \times n$ permutation matrices $P = [p_{i,j}]$ dominated by $A$ (that is, $p_{i,j} \le a_{i,j}$ for all $1 \le i,j \le n$), so that $|\mathcal{P}_A| = \operatorname{per}(A)$. In 2005, Brualdi, Chiang, and Li [1, Section 1, p. 67] introduced the following decomposition question: when can $\mathcal{P}_A$ be partitioned into $m = \operatorname{per}(A)/k$ pairwise disjoint $k$-element subsets $P_1, \dots, P_m$ such that the matrices in each $P_r$ sum to $A$? Following the bipartite-graph terminology of Li, Soosiah, and Yu [2, Section 1, p. 1] and Ferreri, Parameswaran, and Yu [3, Definition 1.1, p. 1], a $k$-element subset $P \subset \mathcal{P}_A$ satisfying $\sum_{M \in P} M = A$ is called a *perfect set* of $A$, and a partition of $\mathcal{P}_A$ into perfect sets is called a *perfect partition* of $A$ (or of its associated $k$-regular bipartite graph $G_A$).

For the all-ones matrix $J_n$, $\mathcal{P}_{J_n}$ is the symmetric group $\mathcal{S}_n$, and the cosets of any generated $n$-cycle subgroup form a perfect partition for every $n \ge 1$, while for $n \ge 4$ the alternating group $\mathcal{A}_n$ of even permutation matrices (permutation matrices of determinant $1$) also admits a perfect partition [1, Propositions 2.1–2.2 and Corollary 2.3, pp. 69–70]. The central open case raised in [1] is the derangement matrix
$$
L_n = J_n - I_n,
$$
whose bipartite adjacency graph is the $(n-1)$-regular graph $L_{n,1} = K_{n,n} - I_{n,n}$ obtained by removing a $1$-factor from $K_{n,n}$. Identifying each permutation $\sigma \in \mathcal{S}_n$ of $\{0, 1, \dots, n-1\}$ with its permutation matrix $M(\sigma)_{i,j} = \delta_{j, \sigma(i)}$, the set $\mathcal{P}_{L_n}$ is the set $\mathcal{D}_n$ of all derangements of $\{0, 1, \dots, n-1\}$, of cardinality
$$
d_n = |\mathcal{D}_n| = \operatorname{per}(L_n) = n! \sum_{r=0}^n \frac{(-1)^r}{r!} = (n-1)\, a_n,
$$
where $a_n = d_n / (n-1)$ is an integer for every $n \ge 2$ because $d_2 = 1$, $d_3 = 2$, and $d_n = (n-1)(d_{n-1} + d_{n-2})$. A subset $P = \{\sigma_1, \dots, \sigma_{n-1}\} \subset \mathcal{D}_n$ is a perfect set of $L_{n,1}$ if and only if $\sigma_r(i) \neq \sigma_s(i)$ for all $1 \le r < s \le n-1$ and all $i \in \{0, \dots, n-1\}$. Ordering the $n-1$ elements of $P$ by their image of $0$ ($\sigma_r(0) = r$ for $1 \le r \le n-1$) and prepending the identity permutation $\mathrm{id} = (0, 1, \dots, n-1)$ as the zeroth row yields a bijection between perfect sets of $L_{n,1}$ and reduced Latin squares of order $n$ [3, Lemma 1.3, p. 2].

Brualdi, Chiang, and Li proved that $\mathcal{D}_n$ has a perfect partition for $n \le 5$ [1, Proposition 3.1, p. 71] by partitioning each cycle-type conjugacy class of $\mathcal{D}_n$ separately, observed that for $n = 6$ the $15$ fixed-point-free involutions of cycle type $(2,2,2)$ cannot be partitioned into three $5$-element perfect sets [1, Section 3, p. 72], and posed two problems that have guided subsequent work:

- **Problem 3.2 of [1, p. 72]** (*Full and even derangements*): *For $n \ge 6$, is there a perfect partition for $\mathcal{P}_{L_n}$ or $\mathcal{P}_{L_n} \cap \mathcal{A}_n$?*
- **Problem 3.3 of [1, p. 72]** (*Fixed cycle-type classes*): *For $n \ge 6$, is there a perfect partition for the collection of permutations in $\mathcal{P}_{L_n}$ with some specific cycle decomposition? For example, can the set of permutations obtained by the product of a $2$-cycle and an $(n-2)$-cycle be partitioned into subsets such that the elements of each subset sum up to $L_n$?*

For the first part of Problem 3.2 (full derangement sets $\mathcal{P}_{L_n}$, restated as [3, Question 1.2, p. 1]), Li, Soosiah, and Yu [2, Theorem 2.1, p. 3] constructed a perfect partition of $L_{6,1}$ ($d_6 = 265$, $a_6 = 53$ perfect sets) in 2012 by algebraic casework on cycle structures, and Ferreri, Parameswaran, and Yu [3, Theorem 1.5, p. 3] recently resolved $n = 7$ ($d_7 = 1,854$, $a_7 = 309$ perfect sets; dataset archived in [4]) using randomized greedy search and integer programming, while stating in [3, Section 1.2, p. 2] that $n \ge 8$ remains open and conjecturing in [3, Conjecture 5.1, p. 14] that a perfect partition of $L_{n,1}$ exists for every $n \ge 2$. For the second part of Problem 3.2 (even derangements $\mathcal{P}_{L_n} \cap \mathcal{A}_n$), Brualdi, Chiang, and Li verified existence for $n \in \{3, 4, 5\}$ and proved the necessary divisibility $(n-1) \mid |\mathcal{P}_{L_n} \cap \mathcal{A}_n|$ [1, Proposition 4.4 and table on p. 74], leaving $n \ge 6$ open. For Problem 3.3, Ferreri, Parameswaran, and Yu [3, Lemma 2.4, p. 3] proved that for every prime $p$, the $(p-1)!$ permutations of cycle type $(p)$ partition into $(p-2)!$ perfect sets formed by the non-identity elements of the cyclic subgroups of order $p$, while non-Hamiltonian cycle types for $n \ge 6$ such as $(4,2)$ at $n = 6$ and $(5,2), (4,3), (3,2,2)$ at $n = 7$ remained unresolved in [1, 2, 3].

### 1.2. Main Results

The obstacle to extending direct exact-cover searches beyond $n = 7$ is the super-exponential growth of the candidate pool $\mathcal{P}(L_{n,1})$. By the reduced Latin square bijection [3, Lemma 1.3, p. 2], $|\mathcal{P}(L_{n,1})| = R_n$, where $R_n$ is the number of reduced Latin squares of order $n$. Whereas $R_6 = 9,408$ and $R_7 = 16,942,080$ [3, Section 4.4, p. 14], the pool sizes for $n = 8$ and $n = 9$ are $R_8 = 535,281,401,856 \approx 5.35 \times 10^{11}$ and $R_9 = 377,597,570,964,258,816 \approx 3.78 \times 10^{17}$, putting unreduced exact cover over $\mathcal{P}(L_{n,1})$ out of reach. Moreover, Ferreri, Parameswaran, and Yu noted in [3, Section 4.4, p. 14] that their computational solutions for $L_{7,1}$ exhibited no consistent algebraic action carrying one perfect set to another.

To overcome this barrier, we impose conjugation invariance under a transitive projective or affine subgroup $H \le \mathcal{S}_n$ acting on $\mathcal{D}_n$ by $\sigma \mapsto h\sigma h^{-1}$. In Section 3, we prove a necessary and sufficient subgroup-orbit criterion (Lemma 3.1) characterizing when the $H$-conjugation orbit of a perfect set $P \subset \mathcal{D}_n$ consists of $[H:K]$ pairwise disjoint perfect sets ($K = \operatorname{Stab}_H(P)$). This reduces the search for an $H$-invariant perfect partition of a conjugation-invariant target set $\mathcal{T} \subseteq \mathcal{D}_n$ to an exact-cover problem over the $H$-orbits $H \backslash \mathcal{T}$, compressing the universe by a factor of up to $|H|$ (for instance, from $133,496$ derangements to $99$ orbits under $\operatorname{P\Gamma L}(2,8)$ at $n = 9$).

Using this reduction, we establish four main results.

**Theorem 1.1** (*Perfect partitions of $L_{8,1}$ and $L_{9,1}$, and symmetric partition of $L_{7,1}$*).
1. *For $n = 8$, the derangement graph $L_{8,1}$ ($d_8 = 14,833$) admits a $\operatorname{PGL}(2,7)$-invariant perfect partition ($|H| = 336$, acting on $\mathbb{P}^1(\mathbb{F}_7)$) generated by $20$ representative perfect sets of size $7$, whose $H$-conjugation orbits have sizes $168^9, 112^1, 84^2, 56^3, 48^2, 28^1, 21^1, 14^1$ and expand to $2,119$ pairwise disjoint perfect sets covering $\mathcal{D}_8$.*
2. *For $n = 9$, the derangement graph $L_{9,1}$ ($d_9 = 133,496$) admits a $\operatorname{P\Gamma L}(2,8)$-invariant perfect partition ($|H| = 1,512$, acting on $\mathbb{P}^1(\mathbb{F}_8)$) generated by $26$ representative perfect sets of size $8$, whose $H$-conjugation orbits have sizes $1512^2, 756^{16}, 504^1, 252^3, 168^1, 84^1, 28^1, 27^1$ and expand to $16,687$ pairwise disjoint perfect sets covering $\mathcal{D}_9$.*
3. *For $n = 7$, in addition to the non-symmetric partitions of $L_{7,1}$ found by Ferreri, Parameswaran, and Yu [3, Theorem 1.5, p. 3], $L_{7,1}$ ($d_7 = 1,854$) admits an $\operatorname{AGL}(1,7)$-invariant perfect partition ($|H| = 42$) generated by $14$ representative perfect sets of size $6$, whose $H$-conjugation orbits have sizes $42^4, 21^3, 14^5, 7^1, 1^1$ and expand to $309$ pairwise disjoint perfect sets covering $\mathcal{D}_7$.*

Theorem 1.1(1)–(2) resolves the first part of Brualdi–Chiang–Li Problem 3.2 [1, p. 72] and Ferreri–Parameswaran–Yu Question 1.2 / Conjecture 5.1 [3, pp. 1, 14] for $n = 8$ and $n = 9$, while Theorem 1.1(3) provides an explicit algebraic group action for $L_{7,1}$ addressing the symmetry question raised in [3, Section 4.4, p. 14].

**Theorem 1.2** (*Perfect partitions of even derangements $\mathcal{P}_{L_n} \cap \mathcal{A}_n$ for $6 \le n \le 9$*).
*For every $n \in \{6, 7, 8, 9\}$, the set $\mathcal{P}_{L_n} \cap \mathcal{A}_n$ of even derangements of order $n$ admits a perfect partition into $(n-1)$-element subsets summing to $L_n$:*
1. *For $n = 6$ ($|\mathcal{P}_{L_6} \cap \mathcal{A}_6| = 130$), an explicit partition into $26$ perfect sets of size $5$.*
2. *For $n = 7$ ($|\mathcal{P}_{L_7} \cap \mathcal{A}_7| = 930$), an $\operatorname{AGL}(1,7)$-invariant partition ($|H| = 42$) generated by $8$ representative perfect sets of size $6$, expanding to $155$ perfect sets.*
3. *For $n = 8$ ($|\mathcal{P}_{L_8} \cap \mathcal{A}_8| = 7,413$), an $\operatorname{A\Gamma L}(1,8)$-invariant partition ($|H| = 168$) generated by $14$ representative perfect sets of size $7$, expanding to $1,059$ perfect sets.*
4. *For $n = 9$ ($|\mathcal{P}_{L_9} \cap \mathcal{A}_9| = 66,752$), a $\operatorname{PGL}(2,8)$-invariant partition ($|H| = 504$) generated by $35$ representative perfect sets of size $8$, expanding to $8,344$ perfect sets.*

Theorem 1.2 resolves the second part of Brualdi–Chiang–Li Problem 3.2 [1, p. 72] for $n = 6, 7, 8, 9$.

**Theorem 1.3** (*Classification of pure cycle-type perfect partitions for $n = 6$ and $n = 7$*).
*For a cycle partition $\lambda \vdash n$ with parts $\ge 2$, let $\mathcal{T}_\lambda(n) \subset \mathcal{D}_n$ denote the conjugacy class of derangements of cycle type $\lambda$.*
1. *For $n = 6$, the four derangement cycle types are $(6)$ ($120$ elements), $(4,2)$ ($90$ elements), $(3,3)$ ($40$ elements), and $(2,2,2)$ ($15$ elements). Among these, $\mathcal{T}_{(4,2)}(6)$ admits an explicit perfect partition into $18$ perfect sets of size $5$ (selected from $72$ pure $(4,2)$ perfect sets forming $2$ $\mathcal{S}_6$-conjugation orbits of size $36$ with setwise stabilizer of order $20$), whereas $\mathcal{T}_{(6)}(6)$ ($0$ pure perfect sets), $\mathcal{T}_{(3,3)}(6)$ ($0$ pure perfect sets), and $\mathcal{T}_{(2,2,2)}(6)$ ($6$ pure perfect sets forming $1$ $\mathcal{S}_6$-orbit of size $6$ with stabilizer of order $120$, no $3$ pairwise disjoint) admit no pure perfect partition.*
2. *For $n = 7$, the four derangement cycle types are $(7)$ ($720$ elements), $(5,2)$ ($504$ elements), $(4,3)$ ($420$ elements), and $(3,2,2)$ ($210$ elements). The classes $\mathcal{T}_{(7)}(7)$, $\mathcal{T}_{(5,2)}(7)$, and $\mathcal{T}_{(4,3)}(7)$ each admit a pure perfect partition into $120$, $84$, and $70$ perfect sets of size $6$, respectively: $\mathcal{T}_{(7)}(7)$ by the $120$ prime-order cyclic subgroups [3, Lemma 2.4, p. 3] ($1$ $\mathcal{S}_7$-orbit of size $120$ with stabilizer $\operatorname{AGL}(1,7)$ of order $42$); $\mathcal{T}_{(5,2)}(7)$ ($16,464$ pure perfect sets across $7$ $\mathcal{S}_7$-orbits of sizes $5040^2, 1680^2, 1008^3$ with stabilizer orders $1^2, 3^2, 5^3$) by explicit conjugation-invariant partitions under $\operatorname{AGL}(1,5)$ ($5$ block orbits), $D_7$ ($6$ block orbits), and $F_{21}$ ($8$ block orbits); and $\mathcal{T}_{(4,3)}(7)$ ($15,120$ pure perfect sets across $9$ $\mathcal{S}_7$-orbits of sizes $2520^5, 840^2, 630^1, 210^1$ with stabilizer orders $2^5, 6^2, 8^1, 24^1$) by explicit conjugation-invariant partitions under $\operatorname{PSL}(2,7)$ ($2$ block orbits) and $\operatorname{AGL}(1,7)$ ($3$ block orbits). By contrast, although $\mathcal{T}_{(3,2,2)}(7)$ contains $840$ pure perfect sets ($2$ $\mathcal{S}_7$-orbits of sizes $630$ and $210$ with stabilizer orders $8$ and $24$) and every element lies in $24$ of them, $\mathcal{T}_{(3,2,2)}(7)$ admits no pure perfect partition.*

In particular, for the cycle type $(n-2, 2)$ singled out as the motivating example in Brualdi–Chiang–Li Problem 3.3 [1, p. 72], a pure perfect partition exists for every $4 \le n \le 7$ (with $1, 5, 18, 84$ perfect sets for $n = 4, 5, 6, 7$; see Section 5.1 for a clarification of the remark on $n = 4$ in [1, p. 72]).

To keep positive constructive existence results separated from negative computational and structural obstructions, we collect our finite-order impossibility results in the following proposition.

**Proposition 1.4** (*Parity and symmetry obstructions at $n = 6$ and $n = 7$*).
1. *(*Odd derangements at $n = 6$*) The set $\mathcal{P}_{L_6} \setminus \mathcal{A}_6$ of $135$ odd derangements in $\mathcal{D}_6$ satisfies the necessary divisibility $5 \mid 135$ and contains $336$ pure-odd perfect sets ($4$ $\mathcal{S}_6$-orbits of sizes $180, 90, 60, 6$ with stabilizer orders $4, 8, 12, 120$, covering each $(6)$-cycle $10$ times and each $(2,2,2)$-involution $32$ times), but admits no perfect partition into $27$ perfect sets.*
2. *(*No $\operatorname{PGL}(2,5)$-invariant partition of $L_{6,1}$*) Under the projective action of $H = \operatorname{PGL}(2,5) \cong \mathcal{S}_5$ ($|H| = 120$) on $\mathbb{P}^1(\mathbb{F}_5)$ ($n = 6$), the $9,408$ perfect sets of $\mathcal{D}_6$ ($40$ $\mathcal{S}_6$-orbits) decompose into $144$ $H$-orbits, only $8$ of which consist of pairwise disjoint perfect sets, and none of these $8$ valid blocks intersects the two $H$-orbits of $6$-cycles of sizes $40$ and $60$. Consequently, $L_{6,1}$ admits no $\operatorname{PGL}(2,5)$-invariant perfect partition.*
3. *(*Maximal-symmetry obstruction for $\mathcal{T}_{(5,2)}(7)$*) Among the $16,464$ pure $(5,2)$ perfect sets in $\mathcal{D}_7$, the simple group $\operatorname{PSL}(2,7)$ ($|H| = 168$, $3$ regular orbits on $\mathcal{T}_{(5,2)}(7)$, $106$ $H$-orbits on pure $(5,2)$ sets) admits $6$ valid block orbits (all of size $56$ with stabilizer order $3$, each covering $2$ of the $3$ orbits) and the affine group $\operatorname{AGL}(1,7)$ ($|H| = 42$, $12$ regular orbits on $\mathcal{T}_{(5,2)}(7)$, $400$ $H$-orbits on pure $(5,2)$ sets) admits $86$ valid block orbits ($76$ of size $42$ with stabilizer order $1$ and $10$ of size $14$ with stabilizer order $3$), and neither group admits an invariant pure perfect partition of $\mathcal{T}_{(5,2)}(7)$.*

| Target set $\mathcal{T}$ | $n$ | $\lvert\mathcal{T}\rvert$ | Sets $\lvert\mathcal{T}\rvert/(n-1)$ | Existence | Symmetry group $H$ ($\lvert H\rvert$) | Orbits $\lvert H \backslash \mathcal{T}\rvert$ | Rep. blocks $r$ | Reference |
|---|---:|---:|---:|---|---|---:|---:|---|
| $\mathcal{D}_n$ ($L_{n,1}$) | $2..5$ | $1, 2, 9, 44$ | $1, 1, 3, 11$ | Yes | Cycle-type / $\operatorname{PGL}(2,q)$ | — | — | [1, Prop. 3.1] |
| $\mathcal{D}_6$ ($L_{6,1}$) | $6$ | $265$ | $53$ | Yes | Algebraic casework ($C_5$) | — | — | [2, Thm. 2.1] |
| $\mathcal{D}_7$ ($L_{7,1}$) | $7$ | $1,854$ | $309$ | Yes | Unsymmetric [3]; $\operatorname{AGL}(1,7)$ ($42$) | $45$ | $14$ | [3, Thm. 1.5]; Thm. 1.1(3) |
| $\mathcal{D}_8$ ($L_{8,1}$) | $8$ | $14,833$ | $2,119$ | **Yes** | $\operatorname{PGL}(2,7)$ ($336$) | $69$ | $20$ | **Thm. 1.1(1)** |
| $\mathcal{D}_9$ ($L_{9,1}$) | $9$ | $133,496$ | $16,687$ | **Yes** | $\operatorname{P\Gamma L}(2,8)$ ($1,512$) | $99$ | $26$ | **Thm. 1.1(2)** |
| $\mathcal{P}_{L_n} \cap \mathcal{A}_n$ | $3..5$ | $2, 3, 24$ | $1, 1, 6$ | Yes | Pure cycle types | — | — | [1, Sec. 4, p. 74] |
| $\mathcal{P}_{L_6} \cap \mathcal{A}_6$ | $6$ | $130$ | $26$ | **Yes** | Trivial ($1$) | $130$ | $26$ | **Thm. 1.2(1)** |
| $\mathcal{P}_{L_7} \cap \mathcal{A}_7$ | $7$ | $930$ | $155$ | **Yes** | $\operatorname{AGL}(1,7)$ ($42$) | $23$ | $8$ | **Thm. 1.2(2)** |
| $\mathcal{P}_{L_8} \cap \mathcal{A}_8$ | $8$ | $7,413$ | $1,059$ | **Yes** | $\operatorname{A\Gamma L}(1,8)$ ($168$) | $53$ | $14$ | **Thm. 1.2(3)** |
| $\mathcal{P}_{L_9} \cap \mathcal{A}_9$ | $9$ | $66,752$ | $8,344$ | **Yes** | $\operatorname{PGL}(2,8)$ ($504$) | $142$ | $35$ | **Thm. 1.2(4)** |
| $\mathcal{P}_{L_6} \setminus \mathcal{A}_6$ (odd) | $6$ | $135$ | $27$ | **No** | Full-pool search | — | — | **Prop. 1.4(1)** |
| $\mathcal{T}_{(6)}(6)$ | $6$ | $120$ | $24$ | **No** | $0$ pure perfect sets | — | — | **Thm. 1.3(1)** |
| $\mathcal{T}_{(4,2)}(6)$ | $6$ | $90$ | $18$ | **Yes** | Trivial ($1$) | $90$ | $18$ | **Thm. 1.3(1)** |
| $\mathcal{T}_{(3,3)}(6)$ | $6$ | $40$ | $8$ | **No** | $0$ pure perfect sets | — | — | **Thm. 1.3(1)** |
| $\mathcal{T}_{(2,2,2)}(6)$ | $6$ | $15$ | $3$ | No | $6$ pure sets, max packing $2$ | — | — | [1, p. 72]; Thm. 1.3(1) |
| $\mathcal{T}_{(7)}(7)$ | $7$ | $720$ | $120$ | Yes | Cyclic subgroups of order $7$ | — | — | [3, Lem. 2.4] |
| $\mathcal{T}_{(5,2)}(7)$ | $7$ | $504$ | $84$ | **Yes** | $\operatorname{AGL}(1,5)$ ($20$), $D_7$ ($14$), $F_{21}$ ($21$) | $26, 36, 24$ | $5, 6, 8$ | **Thm. 1.3(2)** |
| $\mathcal{T}_{(4,3)}(7)$ | $7$ | $420$ | $70$ | **Yes** | $\operatorname{PSL}(2,7)$ ($168$), $\operatorname{AGL}(1,7)$ ($42$) | $3, 10$ | $2, 3$ | **Thm. 1.3(2)** |
| $\mathcal{T}_{(3,2,2)}(7)$ | $7$ | $210$ | $35$ | **No** | $840$ pure sets, hub-matching reduction | — | — | **Thm. 1.3(2)** |

### 1.3. Scope and What Is Not Claimed

All existence and non-existence theorems in this paper apply to the finite orders $n \le 9$ specified above. We do not claim a proof of Conjecture 5.1 of [3, p. 14] for general $n \ge 10$, nor do we claim existence of perfect partitions for $\mathcal{P}_{L_n} \cap \mathcal{A}_n$ for $n \ge 10$ or for fixed cycle types at $n \ge 8$ beyond what is known in the directed Hamilton cycle decomposition literature (reviewed in Section 2). Likewise, the existence of perfect partitions of $L_{7,1}$ and of the pure $p$-cycle class $\mathcal{T}_{(p)}(p)$ for prime $p$ is due to Ferreri, Parameswaran, and Yu [3, Theorem 1.5 and Lemma 2.4, p. 3]; our Theorem 1.1(3) contributes only the $\operatorname{AGL}(1,7)$-conjugation-invariant structure at $n = 7$.

---

## 2. Related Work and Attribution

1. **Brualdi, Chiang, and Li (2005) [1]**: Introduced perfect partitions of $\mathcal{P}_A$ for $k$-regular $(0,1)$-matrices $A$. They settled $A = J_n$ and $\mathcal{A}_n$ [1, Propositions 2.1–2.2, Corollary 2.3, pp. 69–70], proved that $\mathcal{D}_n = \mathcal{P}_{L_n}$ has a perfect partition for $n \le 5$ by partitioning each cycle type individually [1, Proposition 3.1, p. 71], and posed Problems 3.2 and 3.3 [1, p. 72]. In Section 4, they generalized $L_n$ to $L_{n,k}$ (obtained by replacing the $1$s of an $n/k \times n/k$ identity matrix with $k \times k$ all-ones blocks $J_k$), proved that $n - k$ divides both $\operatorname{per}(L_{n,k})$ and $|\mathcal{P}_{L_{n,k}} \cap \mathcal{A}_n|$ [1, Proposition 4.4, p. 74], and constructed perfect partitions for $L_{n,n/2}$ and $L_{6,2}$ [1, Propositions 4.6–4.7, pp. 74–75].
2. **Li, Soosiah, and Yu (2012) [2]**: Derived a rook-polynomial permanent formula for $L_{n,r}$ [2, Theorem 1.2, p. 2] and proved that $L_{6,1}$ ($265$ derangements into $53$ sets of size $5$) and $L_{8,2}$ admit perfect partitions [2, Theorems 2.1 and 3.1, pp. 3, 8], while noting on [2, p. 3] that listing $792$ sets of $6$ perfect matchings for $L_{7,1}$ (an early misprint for $1,854 / 6 = 309$, corrected in [3, Section 1.2, p. 2]) was already difficult and leaving $L_{n,1}$ for $n \ge 7$ open.
3. **Ferreri, Parameswaran, and Yu (2026) [3, 4]**: Established the bijection between perfect sets of $L_{n,1}$ and reduced Latin squares of order $n$ [3, Lemma 1.3, p. 2], proved a recursive lower bound on $|\mathcal{P}(L_{n,1})|$ [3, Theorem 1.4, p. 3], proved that the $(p)$-cycle class in $\mathcal{D}_p$ has a pure perfect partition for every prime $p$ via cyclic subgroups of order $p$ [3, Lemma 2.4, p. 3], and used randomized greedy packing and integer programming to find $42$ distinct perfect partitions of $L_{5,1}$, at least $82$ of $L_{6,1}$, and $2$ of $L_{7,1}$ [3, Theorem 1.5, p. 3; Section 4, pp. 13–14; dataset in [4]]. One of their two $L_{7,1}$ partitions keeps the $120$ pure $(7)$-cycle perfect sets of Lemma 2.4 intact and partitions the remaining $1,134$ derangements of cycle types $(5,2), (4,3), (3,2,2)$ into $189$ mixed perfect sets (listed in [3, Appendix A, Table 1, pp. 16–17]), while the other splits the $(7)$-cycles [3, Section 4.4, p. 14]. They did not consider even derangements $\mathcal{P}_{L_n} \cap \mathcal{A}_n$ or pure non-Hamiltonian cycle types $(4,2), (5,2), (4,3)$, and left $L_{n,1}$ for $n \ge 8$ open [3, Section 1.2, p. 2; Conjecture 5.1, p. 14].
4. **Large sets of directed Hamilton cycle decompositions [5, 6, 7, 8]**: Under the standard bijection between permutations $\sigma \in \mathcal{D}_n$ of cycle type $(n)$ and directed Hamilton cycles of the complete symmetric digraph $K_n^*$, a pure $(n)$-cycle perfect set of $L_{n,1}$ is a decomposition of the $n(n-1)$ arcs of $K_n^*$ into $n-1$ arc-disjoint directed Hamilton cycles (which exists if and only if $n \notin \{4, 6\}$ by Tillson's theorem [8, p. 68]), and a pure perfect partition of $\mathcal{T}_{(n)}(n)$ is a *large set of directed Hamilton cycle decompositions* $\operatorname{LDHC}(n)$ of $K_n^*$. Kaplan, Lev, and Roditty [5] proved that a $G$-regular transitive $\operatorname{LDHC}(n)$ exists whenever the group $G$ of order $n-1$ is sequenceable (which holds for all odd $n \ge 3$), and Zhao and Kang [6] (as stated in [7, Lemma 3, p. 146]) proved that $\operatorname{LDHC}(n)$ exists for every $n \ge 3$ with $n \neq 4, 6$ and possible exceptions $n \in \{p+1 : \text{prime } p \ge 23\}$. This settles Brualdi–Chiang–Li Problem 3.3 restricted to the single cycle type $(n)$ for those orders (confirming in particular that $\mathcal{T}_{(6)}(6)$ has no pure perfect partition), but does not address the remaining cycle types of $\mathcal{D}_n$ or the full derangement set $\mathcal{D}_n$.

---

## 3. Conjugation-Invariant Blocks and the Orbit Exact-Cover Reduction

### 3.1. Group Action by Conjugation on Derangements and Perfect Sets

Fix $n \ge 2$ and write $[n] = \{0, 1, \dots, n-1\}$. The symmetric group $\mathcal{S}_n$ acts on itself by conjugation:
$$
c_h(\sigma) = h \sigma h^{-1}, \qquad (h \sigma h^{-1})(x) = h(\sigma(h^{-1}(x))) \quad (h, \sigma \in \mathcal{S}_n,\ x \in [n]).
$$
Because conjugation preserves cycle decomposition, it preserves the number of fixed points and the sign $\operatorname{sgn}(\sigma) = (-1)^{n - c(\sigma)}$, where $c(\sigma)$ is the number of disjoint cycles of $\sigma$ on $[n]$. Hence $\mathcal{D}_n$, $\mathcal{P}_{L_n} \cap \mathcal{A}_n$, $\mathcal{P}_{L_n} \setminus \mathcal{A}_n$, and every single cycle-type class $\mathcal{T}_\lambda(n)$ are invariant under $c_h$ for all $h \in \mathcal{S}_n$.

Furthermore, conjugation preserves pairwise disjointness of permutations: for any $\sigma, \tau \in \mathcal{S}_n$ and $h \in \mathcal{S}_n$,
$$
(h \sigma h^{-1})(x) = (h \tau h^{-1})(x) \iff \sigma(h^{-1}(x)) = \tau(h^{-1}(x)).
$$
Consequently, a subset $P \subset \mathcal{D}_n$ of size $n-1$ is a perfect set of $L_{n,1}$ if and only if $c_h(P) = \{h \sigma h^{-1} : \sigma \in P\}$ is a perfect set of $L_{n,1}$.

### 3.2. The Block Lemma

Let $H \le \mathcal{S}_n$ be a subgroup. A perfect set $P \subset \mathcal{D}_n$ is called a *valid $H$-block* if any two $H$-conjugates of $P$ are either identical or disjoint:
$$
\forall h_1, h_2 \in H, \qquad c_{h_1}(P) = c_{h_2}(P) \quad \text{or} \quad c_{h_1}(P) \cap c_{h_2}(P) = \emptyset.
$$
The following lemma characterizes valid $H$-blocks in terms of the setwise stabilizer
$$
K = \operatorname{Stab}_H(P) = \{h \in H : c_h(P) = P\} \le H
$$
and the elementwise centralizers $C_H(\sigma) = \operatorname{Stab}_H(\sigma) = \{h \in H : h \sigma h^{-1} = \sigma\}$ for $\sigma \in P$.

**Lemma 3.1** (*Block Lemma*). *Let $H \le \mathcal{S}_n$ be a subgroup and let $P \subset \mathcal{D}_n$ be a perfect set of size $n-1$ with setwise stabilizer $K = \operatorname{Stab}_H(P) \le H$. Decompose $P$ into $K$-conjugation orbits $P = O_1 \sqcup O_2 \sqcup \cdots \sqcup O_r$. Then the following three conditions are equivalent:*
1. *$P$ is a valid $H$-block (that is, the $[H:K]$ distinct $H$-conjugates of $P$ are pairwise disjoint, so that $\bigcup_{h \in H} c_h(P)$ has cardinality $[H:K](n-1)$).*
2. *For every $\sigma \in P$, the centralizer $C_H(\sigma)$ is contained in $K$, and for all $1 \le a < b \le r$, the $K$-orbits $O_a$ and $O_b$ lie in distinct $H$-conjugation orbits ($\bigcup_{h \in H} c_h(O_a) \cap O_b = \emptyset$).*
3. *For every $1 \le a \le r$ and $\sigma_a \in O_a$, the $H$-orbit $H \cdot \sigma_a = \{h \sigma_a h^{-1} : h \in H\}$ has cardinality $[H:K] \cdot |O_a|$, and the $r$ $H$-orbits $H \cdot \sigma_1, \dots, H \cdot \sigma_r$ are pairwise distinct.*

*Proof.* ($1 \implies 2$): Suppose $P$ is a valid $H$-block. If $\sigma \in P$ and $h \in C_H(\sigma)$, then $\sigma = h \sigma h^{-1} \in P \cap c_h(P)$. Since $P \cap c_h(P) \neq \emptyset$, validity of $P$ forces $c_h(P) = P$, so $h \in K$. Thus $C_H(\sigma) \le K$ for all $\sigma \in P$. Next, if $\sigma \in O_a$ and $\tau \in O_b$ satisfy $\tau = h \sigma h^{-1}$ for some $h \in H$, then $\tau \in P \cap c_h(P)$, which again forces $c_h(P) = P$ and hence $h \in K$; thus $\sigma$ and $\tau$ lie in the same $K$-orbit, so $a = b$.

($2 \implies 3$): Assume (2). For each $a \in \{1, \dots, r\}$ and $\sigma_a \in O_a$, the pointwise stabilizer of $\sigma_a$ in $K$ is $C_K(\sigma_a) = C_H(\sigma_a) \cap K = C_H(\sigma_a)$ because $C_H(\sigma_a) \le K$. By the orbit-stabilizer theorem applied first to $K$ and then to $H$,
$$
|O_a| = \frac{|K|}{|C_K(\sigma_a)|} = \frac{|K|}{|C_H(\sigma_a)|}, \qquad |H \cdot \sigma_a| = \frac{|H|}{|C_H(\sigma_a)|} = \frac{|H|}{|K|} \cdot \frac{|K|}{|C_H(\sigma_a)|} = [H:K] \cdot |O_a|.
$$
By the second part of (2), the $H$-orbits $H \cdot \sigma_1, \dots, H \cdot \sigma_r$ are pairwise disjoint and hence distinct.

($3 \implies 1$): Assume (3). The set of distinct $H$-conjugates of $P$ is $\mathcal{F}(P) = \{c_h(P) : h \in H / K\}$, which consists of $[H:K]$ perfect sets of size $n-1$. On the other hand, the union of the elements in $\mathcal{F}(P)$ is $\bigcup_{h \in H} c_h(P) = \bigsqcup_{a=1}^r (H \cdot \sigma_a)$, because the $H$-orbits $H \cdot \sigma_1, \dots, H \cdot \sigma_r$ are pairwise distinct. By (3), the cardinality of this union is
$$
\sum_{a=1}^r |H \cdot \sigma_a| = \sum_{a=1}^r [H:K] \cdot |O_a| = [H:K] \sum_{a=1}^r |O_a| = [H:K](n-1).
$$
Since $[H:K]$ sets of size $n-1$ have a union of cardinality $[H:K](n-1)$ if and only if they are pairwise disjoint, $P$ is a valid $H$-block. $\square$

**Proposition 3.2** (*Orbit Exact-Cover Reduction and Parity Divisibility*).
1. *Let $\mathcal{T} \subseteq \mathcal{D}_n$ be an $H$-conjugation-invariant subset with $H$-orbit decomposition $\mathcal{T} = \mathcal{O}_1 \sqcup \cdots \sqcup \mathcal{O}_m$. For any valid $H$-block $P \subset \mathcal{T}$ with stabilizer $K = \operatorname{Stab}_H(P)$, the union $\bigcup_{h \in H} c_h(P)$ is a union of whole $H$-orbits $\mathcal{O}_i$, namely those $\mathcal{O}_i$ with $P \cap \mathcal{O}_i \neq \emptyset$ (for each of which $|P \cap \mathcal{O}_i| = |\mathcal{O}_i| / [H:K] = |K| / |C_H(\sigma_i)|$ is a single $K$-orbit).*
2. *Consequently, a collection of valid $H$-blocks $B_1, \dots, B_s \subset \mathcal{T}$ generates an $H$-invariant perfect partition $\bigsqcup_{j=1}^s \{c_h(B_j) : h \in H/K_j\}$ of $\mathcal{T}$ if and only if the covered orbit subsets $S(B_j) = \{i \in \{1, \dots, m\} : B_j \cap \mathcal{O}_i \neq \emptyset\}$ form an exact cover (a partition) of $\{1, \dots, m\}$.*
3. *For every $n \ge 2$, the quotient $a_n = d_n / (n-1)$ is an odd integer, and both $|\mathcal{P}_{L_n} \cap \mathcal{A}_n| = (n-1)(a_n + (-1)^{n-1})/2$ and $|\mathcal{P}_{L_n} \setminus \mathcal{A}_n| = (n-1)(a_n - (-1)^{n-1})/2$ are integer multiples of $n-1$.*

*Proof.* Parts (1) and (2) follow from Lemma 3.1(3): each valid $H$-block $B_j$ decomposes into $K_j$-orbits lying in distinct $H$-orbits $\mathcal{O}_i$, and the $[H:K_j]$ pairwise disjoint perfect sets in the $H$-orbit of $B_j$ cover every element of $\bigsqcup_{i \in S(B_j)} \mathcal{O}_i$ once and no element outside it. For part (3), substituting $d_{n-1} = (n-2)a_{n-1}$ and $d_{n-2} = (n-3)a_{n-2}$ into $d_n = (n-1)(d_{n-1} + d_{n-2})$ yields the recurrence $a_n = (n-2)a_{n-1} + (n-3)a_{n-2}$ for $n \ge 4$, with $a_2 = 1$ and $a_3 = 1$. Since one of $n-2, n-3$ is odd and the other is even, induction gives $a_n \equiv (n-2) + (n-3) = 2n - 5 \equiv 1 \pmod 2$ for all $n \ge 2$. Since $\det(L_n) = |\mathcal{P}_{L_n} \cap \mathcal{A}_n| - |\mathcal{P}_{L_n} \setminus \mathcal{A}_n| = (-1)^{n-1}(n-1)$ [1, Section 4, p. 74] and $|\mathcal{P}_{L_n} \cap \mathcal{A}_n| + |\mathcal{P}_{L_n} \setminus \mathcal{A}_n| = (n-1)a_n$, both $(a_n \pm (-1)^{n-1})/2$ are integers. $\square$

---

## 4. Constructive Existence Proofs for $L_{8,1}$, $L_{9,1}$, and $\mathcal{P}_{L_n} \cap \mathcal{A}_n$

### 4.1. Projective and Affine Symmetry Groups for $n = 7, 8, 9$

To apply Lemma 3.1 and Proposition 3.2 to $n = 7, 8, 9$, we realize $[n] = \{0, 1, \dots, n-1\}$ as an affine line $\mathbb{F}_q$ or projective line $\mathbb{P}^1(\mathbb{F}_q) = \mathbb{F}_q \cup \{\infty\}$:

- **For $n = 7$ ($[7] = \mathbb{F}_7$)**: The affine general linear group $H = \operatorname{AGL}(1,7) = \{x \mapsto ax + b \bmod 7 : a \in \mathbb{F}_7^\times,\ b \in \mathbb{F}_7\}$ has order $|H| = 42$ and is generated by the translation $t(x) = x + 1 \bmod 7$ (`1234560`) and the dilation $m_3(x) = 3x \bmod 7$ (`0362514`).
- **For $n = 8$ ($[8] = \mathbb{P}^1(\mathbb{F}_7)$ with $\infty = 7$)**: The projective general linear group $H = \operatorname{PGL}(2,7)$ of fractional linear transformations $x \mapsto (ax+b)/(cx+d)$ over $\mathbb{F}_7$ has order $|H| = 336$ and is generated by $t(x) = x + 1$ (`12345607`), $m_3(x) = 3x$ (`03625147`), and the inversion $j(x) = -1/x$ (`76325410`).
- **For $n = 8$ even derangements ($[8] = \mathbb{F}_8 = \mathbb{F}_2[\alpha]/(\alpha^3 + \alpha + 1)$)**: Identifying $x = b_0 + b_1 \alpha + b_2 \alpha^2 \in \mathbb{F}_8$ with the integer $b_0 + 2b_1 + 4b_2 \in \{0, \dots, 7\}$, the affine semilinear group $H = \operatorname{A\Gamma L}(1,8) = \{x \mapsto a x^{2^k} + b : a \in \mathbb{F}_8^\times,\ b \in \mathbb{F}_8,\ k \in \{0,1,2\}\}$ has order $|H| = 8 \times 7 \times 3 = 168$ and is generated by multiplication by $\alpha$ (`02463175`), translation by $1$ (`10325476`), and the Frobenius automorphism $x \mapsto x^2$ (`01456723`).
- **For $n = 9$ ($[9] = \mathbb{P}^1(\mathbb{F}_8)$ with $\infty = 8$)**: Extending the action on $\mathbb{F}_8$ to $\infty = 8$ via fractional linear transformations, the projective general linear group $\operatorname{PGL}(2,8)$ has order $9 \times 8 \times 7 = 504$ (generated by multiplication by $\alpha$ `024631758`, translation by $1$ `103254768`, and inversion $x \mapsto 1/x$ `815672340`), and adjoining the Frobenius map $x \mapsto x^2$ (`014567238`) yields the projective semilinear group $\operatorname{P\Gamma L}(2,8)$ of order $504 \times 3 = 1,512$.

### 4.2. Proof of Theorem 1.1 ($L_{8,1}$, $L_{9,1}$, and Symmetric $L_{7,1}$)

*Proof of Theorem 1.1.* For each of the three pairs $(n, H) \in \{(7, \operatorname{AGL}(1,7)),\ (8, \operatorname{PGL}(2,7)),\ (9, \operatorname{P\Gamma L}(2,8))\}$, we partition $\mathcal{D}_n$ into $H$-conjugation orbits $\mathcal{O}_1 \sqcup \cdots \sqcup \mathcal{O}_m$ and construct valid $H$-blocks $B_1, \dots, B_s \subset \mathcal{D}_n$ satisfying Lemma 3.1(2)–(3) for prescribed stabilizer subgroups $K_j \le H$ by backtracking over $K_j$-conjugation orbits $O_a \subset \mathcal{O}_{i_a}$ whose elements have pairwise distinct values at each coordinate $x \in [n]$.

1. **Case $n = 8$, $H = \operatorname{PGL}(2,7)$ ($|H| = 336$)**: The $14,833$ derangements in $\mathcal{D}_8$ decompose into $m = 69$ $H$-conjugation orbits (of sizes $336^{30}, 168^{23}, 112^1, 84^4, 56^3, 42^5, 28^1, 21^1, 14^1$). Table A.2 in Appendix A lists $s = 20$ explicit perfect sets $B_1, \dots, B_{20} \subset \mathcal{D}_8$. Direct finite check confirms that:
   - Each $B_i$ is a perfect set of $7$ derangements of $[8]$.
   - Under $H$-conjugation, the setwise stabilizers $K_i = \operatorname{Stab}_H(B_i)$ have orders $|K_i| \in \{2^9, 3^1, 4^2, 6^3, 7^2, 12^1, 16^1, 24^1\}$, and each $H$-orbit $\mathcal{F}(B_i) = \{c_h(B_i) : h \in H/K_i\}$ consists of $[H:K_i] = 336/|K_i|$ pairwise disjoint perfect sets.
   - The $20$ orbit sets $S(B_i) \subset \{1, \dots, 69\}$ are pairwise disjoint and their union is all $69$ orbits of $\mathcal{D}_8$. The total number of perfect sets is
$$
9 \cdot 168 + 1 \cdot 112 + 2 \cdot 84 + 3 \cdot 56 + 2 \cdot 48 + 1 \cdot 28 + 1 \cdot 21 + 1 \cdot 14 = 2,119,
$$
covering $2,119 \times 7 = 14,833 = d_8$ derangements once each.

2. **Case $n = 9$, $H = \operatorname{P\Gamma L}(2,8)$ ($|H| = 1,512$)**: The $133,496$ derangements in $\mathcal{D}_9$ decompose into $m = 99$ $H$-conjugation orbits (of sizes $1512^{85}, 504^8, 216^1, 168^4, 56^1$). Table A.3 in Appendix A lists $s = 26$ explicit perfect sets $B_1, \dots, B_{26} \subset \mathcal{D}_9$. Each $B_i$ is a perfect set of $8$ derangements of $[9]$, its $H$-conjugates form $[H:K_i] = 1,512 / |K_i|$ pairwise disjoint perfect sets with stabilizer orders $|K_i| \in \{1^2, 2^{16}, 3^1, 6^3, 9^1, 18^1, 54^1, 56^1\}$, and the $26$ covered orbit sets partition all $99$ $H$-orbits of $\mathcal{D}_9$. The resulting partition has
$$
2 \cdot 1512 + 16 \cdot 756 + 1 \cdot 504 + 3 \cdot 252 + 1 \cdot 168 + 1 \cdot 84 + 1 \cdot 28 + 1 \cdot 27 = 16,687
$$
perfect sets, covering $16,687 \times 8 = 133,496 = d_9$ derangements once each.

3. **Case $n = 7$, $H = \operatorname{AGL}(1,7)$ ($|H| = 42$)**: The $1,854$ derangements in $\mathcal{D}_7$ decompose into $m = 45$ $H$-orbits ($44$ regular orbits of size $42$ and $1$ orbit of size $6$). Table A.1 in Appendix A lists $s = 14$ explicit perfect sets $B_1, \dots, B_{14} \subset \mathcal{D}_7$ with stabilizer orders $|K_i| \in \{1^4, 2^3, 3^5, 6^1, 42^1\}$, expanding to
$$
4 \cdot 42 + 3 \cdot 21 + 5 \cdot 14 + 1 \cdot 7 + 1 \cdot 1 = 309
$$
pairwise disjoint perfect sets covering all $1,854$ derangements. In particular, the unique block $B_1$ with $|K_1| = 42$ is the pure $(7)$-cycle translation group minus the identity, $\{x \mapsto x + c \bmod 7 : c \in \mathbb{F}_7^\times\}$, which is normal in $\operatorname{AGL}(1,7)$ and hence fixed as a set by the entire group $H$. $\square$

**Remark 4.1** (*Cycle-type mixing forced by regular orbits at $n = 8$*). Among the $69$ $\operatorname{PGL}(2,7)$-orbits on $\mathcal{D}_8$, $30$ are regular of size $336$ ($C_H(\sigma) = \{e\}$). By Lemma 3.1(2), if a valid $H$-block $B$ with stabilizer $K$ is a single $K$-orbit ($r = 1$), then $|K| = |B| \cdot |C_H(\sigma)| = 7 |C_H(\sigma)|$; for a regular orbit ($|C_H(\sigma)| = 1$), this forces $|K| = 7$. Since all Sylow $7$-subgroups of $\operatorname{PGL}(2,7)$ are conjugate to the translation subgroup $\langle t \rangle$ of order $7$, checking all $30$ regular orbits shows that only $2$ of the $30$ regular orbits (both consisting of permutations of cycle type $(6,2)$) form a perfect set under conjugation by a subgroup of order $7$ (Blocks $B_{19}$ and $B_{20}$ in Table A.2). The remaining $28$ regular orbits cannot be covered by single-$K$-orbit blocks and therefore require multi-orbit blocks ($r \ge 2$) that combine multiple $H$-orbits and cycle types.

### 4.3. Proof of Theorem 1.2 (Even Derangements $\mathcal{P}_{L_n} \cap \mathcal{A}_n$ for $6 \le n \le 9$)

*Proof of Theorem 1.2.* By Proposition 3.2(3), $|\mathcal{P}_{L_n} \cap \mathcal{A}_n|$ equals $130, 930, 7,413, 66,752$ for $n = 6, 7, 8, 9$, requiring $26, 155, 1,059, 8,344$ perfect sets of size $n-1$, respectively.

1. **For $n = 6$**: A derangement of $[6]$ is even if and only if its cycle type is $(4,2)$ ($90$ elements) or $(3,3)$ ($40$ elements). Enumerating the perfect sets of $L_{6,1}$ contained in $\mathcal{T}_{(4,2)}(6) \cup \mathcal{T}_{(3,3)}(6)$ yields $312$ pure-even perfect sets ($72$ of composition $(4,2)^5$ forming $2$ $\mathcal{S}_6$-orbits of size $36 = 720/20$ with stabilizer order $20$, and $240$ of composition $(4,2)^3(3,3)^2$ forming $2$ $\mathcal{S}_6$-orbits of size $120 = 720/6$ with stabilizer order $6$, covering each of the $130$ even derangements $12$ times). Table A.4 in Appendix A gives $26$ pairwise disjoint pure-even perfect sets covering all $130$ even derangements ($6$ of these $26$ sets are pure $(4,2)$ sets and $20$ mix $(4,2)$ and $(3,3)$).
2. **For $n = 7$**: Even derangements of $[7]$ have cycle type $(7)$ ($720$ elements) or $(3,2,2)$ ($210$ elements). Under $H = \operatorname{AGL}(1,7)$ ($|H| = 42$), $\mathcal{P}_{L_7} \cap \mathcal{A}_7$ splits into $23$ orbits ($22$ regular orbits of size $42$ and $1$ orbit of size $6$). Table A.5 in Appendix A gives $8$ valid $H$-blocks with stabilizer orders $|K_i| \in \{1^2, 2^1, 3^3, 6^1, 42^1\}$, expanding to $2 \cdot 42 + 1 \cdot 21 + 3 \cdot 14 + 1 \cdot 7 + 1 \cdot 1 = 155$ pairwise disjoint perfect sets covering all $930$ even derangements.
3. **For $n = 8$**: Even derangements of $[8]$ have cycle types $(6,2)$ ($3,360$), $(5,3)$ ($2,688$), $(4,4)$ ($1,260$), and $(2,2,2,2)$ ($105$), totaling $7,413$ elements. Under $H = \operatorname{A\Gamma L}(1,8)$ ($|H| = 168$), $\mathcal{P}_{L_8} \cap \mathcal{A}_8$ splits into $53$ orbits (of sizes $168^{40}, 84^4, 56^3, 42^3, 28^2, 7^1$). Table A.6 in Appendix A gives $14$ valid $H$-blocks with stabilizer orders $|K_i| \in \{1^3, 2^4, 3^2, 4^1, 6^2, 21^1, 168^1\}$, expanding to
$$
3 \cdot 168 + 4 \cdot 84 + 2 \cdot 56 + 1 \cdot 42 + 2 \cdot 28 + 1 \cdot 8 + 1 \cdot 1 = 1,059
$$
pairwise disjoint perfect sets covering all $7,413$ even derangements. The block $B_1$ with $|K_1| = 168$ is the $7$-element translation group $\{x \mapsto x + b : b \in \mathbb{F}_8^\times\}$ of cycle type $(2,2,2,2)$, which is normal in $\operatorname{A\Gamma L}(1,8)$.
4. **For $n = 9$**: Even derangements of $[9]$ have cycle types $(9)$ ($40,320$), $(4,3,2)$ ($15,120$), $(5,2,2)$ ($9,072$), and $(3,3,3)$ ($2,240$), totaling $66,752$ elements. Under $H = \operatorname{PGL}(2,8)$ ($|H| = 504$), $\mathcal{P}_{L_9} \cap \mathcal{A}_9$ splits into $142$ orbits (of sizes $504^{129}, 168^9, 56^4$). Table A.7 in Appendix A gives $35$ valid $H$-blocks with stabilizer orders $|K_i| \in \{1^5, 2^{16}, 3^4, 4^8, 6^1, 18^1\}$, expanding to
$$
5 \cdot 504 + 16 \cdot 252 + 4 \cdot 168 + 8 \cdot 126 + 1 \cdot 84 + 1 \cdot 28 = 8,344
$$
pairwise disjoint perfect sets covering all $66,752$ even derangements. $\square$

---

## 5. Pure Cycle-Type Partitions and Finite Impossibility Proofs

### 5.1. Proof of Theorem 1.3(1): Pure Cycle Types at $n = 6$ and the $(n-2,2)$ Family

*Proof of Theorem 1.3(1).* Complete enumeration of the $R_6 = 9,408$ perfect sets of $\mathcal{D}_6$ (which decompose under $\mathcal{S}_6$-conjugation into $40$ orbits of sizes $720^4, 360^{11}, 180^9, 120^3, 90^2, 60^3, 40^2, 36^2, 30^1, 20^2, 6^1$ with setwise stabilizer orders $1^4, 2^{11}, 4^9, 6^3, 8^2, 12^3, 18^2, 20^2, 24^1, 36^2, 120^1$, satisfying $\sum |\mathcal{S}_6|/|\operatorname{Stab}| = 9,408$) and filtering for perfect sets whose $5$ elements all share the same cycle type $\lambda \in \{(6), (4,2), (3,3), (2,2,2)\}$ yields the following counts and partitions:

- **$\lambda = (6)$ ($120$ elements)**: $0$ pure $(6)$-cycle perfect sets exist in $\mathcal{D}_6$. In the digraph formulation of Section 2, a pure $(6)$-cycle perfect set is a decomposition of the complete symmetric digraph $K_6^*$ into $5$ arc-disjoint directed Hamilton cycles, which does not exist by Tillson's theorem [8, p. 68] (and is directly confirmed here by the $9,408$-set enumeration).
- **$\lambda = (4,2)$ ($90$ elements)**: $72$ pure $(4,2)$ perfect sets exist in $\mathcal{D}_6$, decomposing into $2$ $\mathcal{S}_6$-conjugation orbits of size $36 = 720/20$ with setwise stabilizer of order $20$ ($2 \cdot 36 = 72$), and each of the $90$ elements of $\mathcal{T}_{(4,2)}(6)$ lies in $4$ of them. Table A.8 in Appendix A lists $18$ pairwise disjoint pure $(4,2)$ perfect sets covering all $90$ elements.
- **$\lambda = (3,3)$ ($40$ elements)**: $0$ pure $(3,3)$ perfect sets exist in $\mathcal{D}_6$; indeed, backtracking over $\mathcal{T}_{(3,3)}(6)$ shows that at most $4$ pairwise disjoint permutations of cycle type $(3,3)$ can be chosen in $\mathcal{D}_6$, so no $5$-element pure $(3,3)$ perfect set exists.
- **$\lambda = (2,2,2)$ ($15$ elements)**: As observed in [1, Section 3, p. 72], $\mathcal{T}_{(2,2,2)}(6)$ admits no pure perfect partition. There are $6$ pure $(2,2,2)$ perfect sets (the $6$ one-factorizations of $K_6$, forming a single $\mathcal{S}_6$-conjugation orbit of size $6 = 720/120$ with setwise stabilizer of order $120$), each of the $15$ fixed-point-free involutions lies in $2$ of them, and the maximum number of pairwise disjoint pure $(2,2,2)$ perfect sets is $2 < 3$. $\square$

**Remark 5.1** (*Clarification of the $(n-2,2)$ family at $n = 4$ in Problem 3.3 of [1, p. 72]*). In Problem 3.3, Brualdi, Chiang, and Li asked whether the set of permutations obtained as the product of a $2$-cycle and an $(n-2)$-cycle ($\mathcal{T}_{(n-2,2)}(n)$) admits a perfect partition, writing that the answer is "no for $n = 4$, yes for $n = 5$, and unknown for $n \ge 6$." At $n = 4$, the product of two disjoint $2$-cycles consists of the $3$ fixed-point-free involutions $(01)(23), (02)(13), (03)(12)$ of cycle type $(2,2)$, which sum to $L_4$ and form a single perfect set (as used in [1, Section 4, p. 74] to partition $\mathcal{P}_{L_4} \cap \mathcal{A}_4$); the "no for $n = 4$" remark in [1, p. 72] refers instead to the impossibility of partitioning all of $\mathcal{D}_4$ by cycle type, because the complementary class $\mathcal{T}_{(4)}(4)$ of six $4$-cycles cannot be partitioned into two $3$-element perfect sets. Combining $n = 4$ ($1$ set) and $n = 5$ ($5$ sets of size $4$ [1, Proposition 3.1, p. 71]) with Theorem 1.3(1) ($18$ sets at $n = 6$) and Theorem 1.3(2) ($84$ sets at $n = 7$) shows that $\mathcal{T}_{(n-2,2)}(n)$ admits a pure perfect partition for every $4 \le n \le 7$.

### 5.2. Proof of Theorem 1.3(2): Pure Cycle Types at $n = 7$

*Proof of Theorem 1.3(2).* The $1,854$ derangements in $\mathcal{D}_7$ partition into the four cycle-type classes $\mathcal{T}_{(7)}(7)$ ($720$), $\mathcal{T}_{(5,2)}(7)$ ($504$), $\mathcal{T}_{(4,3)}(7)$ ($420$), and $\mathcal{T}_{(3,2,2)}(7)$ ($210$).

1. **$\lambda = (7)$ ($720$ elements)**: By [3, Lemma 2.4, p. 3], the $6! = 720$ seven-cycles partition into $5! = 120$ pure perfect sets given by the non-identity elements of the $120$ cyclic subgroups of order $7$, which form a single $\mathcal{S}_7$-conjugation orbit of size $120 = 5,040/42$ with setwise stabilizer $N_{\mathcal{S}_7}(C_7) \cong \operatorname{AGL}(1,7)$ of order $42$.
2. **$\lambda = (4,3)$ ($420$ elements)**: Complete enumeration of pure $(4,3)$ perfect sets in $\mathcal{D}_7$ yields $15,120$ pure $(4,3)$ perfect sets, covering each of the $420$ elements $216$ times and decomposing into $9$ $\mathcal{S}_7$-conjugation orbits: $5$ orbits of size $2,520 = 5,040/2$ (stabilizer order $2$), $2$ orbits of size $840 = 5,040/6$ (stabilizer order $6$), $1$ orbit of size $630 = 5,040/8$ (stabilizer order $8$), and $1$ orbit of size $210 = 5,040/24$ (stabilizer order $24$), satisfying $5 \cdot 2520 + 2 \cdot 840 + 630 + 210 = 15,120$. Under $H = \operatorname{PSL}(2,7)$ ($|H| = 168$, generated by `1234560` and `1053426`), $\mathcal{T}_{(4,3)}(7)$ decomposes into $3$ orbits (of sizes $168, 168, 84$). Table A.9 in Appendix A gives $s = 2$ valid $H$-blocks $B_1, B_2 \subset \mathcal{T}_{(4,3)}(7)$ with stabilizer orders $|K_1| = 3$ ($[H:K_1] = 56$, covering the two orbits of size $168$) and $|K_2| = 12$ ($[H:K_2] = 14$, covering the orbit of size $84$), expanding to $56 + 14 = 70$ pairwise disjoint pure $(4,3)$ perfect sets covering all $420$ elements. An $\operatorname{AGL}(1,7)$-invariant partition ($|H| = 42$, $10$ regular orbits of size $42$ on $\mathcal{T}_{(4,3)}(7)$, $3$ representative blocks with stabilizer orders $1, 3, 3$, expanding to $42 + 14 + 14 = 70$ sets) is also included in the supplementary data (`n7ct43_AGL17_cert.json`).
3. **$\lambda = (5,2)$ ($504$ elements)**: Complete enumeration of pure $(5,2)$ perfect sets in $\mathcal{D}_7$ yields $16,464$ pure $(5,2)$ perfect sets, covering each of the $504$ elements $196$ times and decomposing into $7$ $\mathcal{S}_7$-conjugation orbits: $2$ regular orbits of size $5,040 = 5,040/1$ (setwise stabilizer order $1$), $2$ orbits of size $1,680 = 5,040/3$ (setwise stabilizer order $3$), and $3$ orbits of size $1,008 = 5,040/5$ (setwise stabilizer order $5$), satisfying $2 \cdot 5040 + 2 \cdot 1680 + 3 \cdot 1008 = 16,464$. Table A.10 in Appendix A gives a conjugation-invariant partition under $H = \operatorname{AGL}(1,5)$ ($|H| = 20$, acting on $\{0,1,2,3,4\}$ and fixing $5, 6$, generated by `1234056` and `0241356`, with $26$ orbits of sizes $20^{25}, 4^1$ on $\mathcal{T}_{(5,2)}(7)$), using $s = 5$ representative blocks of $H$-stabilizer orders $|K_i| \in \{1^4, 5^1\}$ (whose full $\mathcal{S}_7$-stabilizer orders are $1, 5, 1, 5, 5$) expanding to $4 \cdot 20 + 1 \cdot 4 = 84$ pairwise disjoint pure $(5,2)$ perfect sets. Partitions invariant under $F_{21}$ ($|H| = 21$, $24$ regular orbits of size $21$ on $\mathcal{T}_{(5,2)}(7)$, $8$ blocks with $|K_i| \in \{1^2, 3^6\}$ expanding to $2 \cdot 21 + 6 \cdot 7 = 84$ sets, `n7ct52_F_21_cert.json`) and $D_7$ ($|H| = 14$, $36$ regular orbits of size $14$ on $\mathcal{T}_{(5,2)}(7)$, $6$ free blocks with $|K_i| = 1$ expanding to $6 \cdot 14 = 84$ sets, `n7ct52_D_7_cert.json`) are verified by the same orbit reduction.
4. **$\lambda = (3,2,2)$ ($210$ elements, impossibility)**: Each $\sigma \in \mathcal{T}_{(3,2,2)}(7)$ is determined by its $3$-cycle support $T = \{i \in [7] : \sigma^2(i) \neq i\} \in \binom{[7]}{3}$ ($35$ choices), one of the $2$ cyclic orientations on $T$, and one of the $3$ perfect matchings of $[7] \setminus T$ into two disjoint transpositions ($35 \times 2 \times 3 = 210$). Complete enumeration of pure $(3,2,2)$ perfect sets in $\mathcal{D}_7$ yields $840$ pure $(3,2,2)$ perfect sets, covering each of the $210$ elements $24$ times and decomposing into $2$ $\mathcal{S}_7$-conjugation orbits: $1$ orbit of size $630 = 5,040/8$ (setwise stabilizer order $8$) and $1$ orbit of size $210 = 5,040/24$ (setwise stabilizer order $24$), satisfying $630 + 210 = 840$. These $840$ sets have the following rigid structure:
   - In every pure $(3,2,2)$ perfect set $P$ of size $6$, the $3$-cycle supports of the $6$ elements consist of three $3$-element subsets $T_1, T_2, T_3 \in \binom{[7]}{3}$, each occurring with multiplicity $2$ (with opposite orientations on $T_a$).
   - The intersection $T_1 \cap T_2 \cap T_3 = \{u\}$ is a single *hub vertex* $u \in [7]$, and the three pairs $e_a = T_a \setminus \{u\}$ ($a = 1, 2, 3$) form a perfect matching $M = \{e_1, e_2, e_3\}$ of $[7] \setminus \{u\}$. Moreover, for each $a \in \{1, 2, 3\}$, the two elements of $P$ with $3$-cycle support $T_a = \{u\} \cup e_a$ use the two matchings of $[7] \setminus T_a$ other than the omitted matching $m_{\mathrm{omit}}(P, T_a) = \{e_b : b \neq a\}$. (For each of the $7 \times 15 = 105$ hub-matching pairs $(u, M)$, there are $2^3 = 8$ choices of orientations, accounting for all $105 \times 8 = 840$ pure $(3,2,2)$ perfect sets.)
   - For each $T \in \binom{[7]}{3}$, $\mathcal{T}_{(3,2,2)}(7)$ contains $6$ permutations with $3$-cycle support $T$ ($2$ for each of the $3$ matchings of $[7] \setminus T$). Since every pure $(3,2,2)$ perfect set $P$ whose supports include $T$ covers $2$ of these $6$ permutations (one for each of the $2$ matchings other than $m_{\mathrm{omit}}(P, T)$), any partition of $\mathcal{T}_{(3,2,2)}(7)$ into $35$ pure perfect sets must use $T$ in $3$ blocks whose omitted matchings $m_{\mathrm{omit}}(P, T)$ are the $3$ distinct matchings of $[7] \setminus T$ once each.
   - Consequently, any pure $(3,2,2)$ perfect partition projects to an exact cover of the $35 \times 3 = 105$ pairs $(T, m_{\mathrm{omit}})$ by the $105$ triples $\{(\{u\} \cup e_a, \{e_b : b \neq a\}) : a = 1, 2, 3\}$ indexed by the $105$ hub-matching pairs $(u, M)$. Backtracking on this $105 \times 105$ $3$-uniform, $3$-regular exact-cover instance (branching at each step on an uncovered pair $(T, m_{\mathrm{omit}})$ with the minimum number of available triples) visits $88$ search nodes and terminates with $0$ solutions. Hence $\mathcal{T}_{(3,2,2)}(7)$ admits no pure perfect partition. $\square$

### 5.3. Proof of Proposition 1.4: Parity and Symmetry Obstructions

*Proof of Proposition 1.4.*

1. **Part (1) (Odd derangements $\mathcal{P}_{L_6} \setminus \mathcal{A}_6$)**: An element of $\mathcal{D}_6$ is odd if and only if its cycle type is $(6)$ ($120$ elements) or $(2,2,2)$ ($15$ elements), giving $|\mathcal{P}_{L_6} \setminus \mathcal{A}_6| = 135 = 5 \times 27$. Complete enumeration of perfect sets of $L_{6,1}$ contained in $\mathcal{P}_{L_6} \setminus \mathcal{A}_6$ yields $336$ pure-odd perfect sets, decomposing into $4$ $\mathcal{S}_6$-conjugation orbits: $1$ orbit of size $180 = 720/4$ (stabilizer order $4$, composition $(6)^4(2,2,2)^1$), $1$ orbit of size $90 = 720/8$ (stabilizer order $8$, composition $(6)^4(2,2,2)^1$), $1$ orbit of size $60 = 720/12$ (stabilizer order $12$, composition $(6)^2(2,2,2)^3$), and $1$ orbit of size $6 = 720/120$ (stabilizer order $120$, composition $(2,2,2)^5$), totaling $270$ sets of composition $(6)^4(2,2,2)^1$, $60$ of composition $(6)^2(2,2,2)^3$, $6$ of composition $(2,2,2)^5$, and $0$ of compositions $(6)^3(2,2,2)^2$ and $(6)^5$ ($180 + 90 + 60 + 6 = 336$), covering each $(6)$-cycle $10$ times and each $(2,2,2)$-involution $32$ times. Running exact-cover backtracking on these $336$ candidate sets over the $135$-element universe (branching at each step on an uncovered odd derangement of minimum degree in the remaining pool) visits $194$ search nodes and terminates with $0$ solutions.
2. **Part (2) (No $\operatorname{PGL}(2,5)$-invariant partition of $L_{6,1}$)**: Realizing $[6] = \mathbb{P}^1(\mathbb{F}_5)$ with $\infty = 5$, the projective group $H = \operatorname{PGL}(2,5)$ of order $120$ is generated by $x \mapsto x + 1$ (`123405`), $x \mapsto 2x$ (`024135`), and $x \mapsto 1/x$ (`513240`). Under $H$-conjugation, $\mathcal{D}_6$ splits into $9$ orbits (of sizes $60, 40, 20$ on $(6)$; $60, 30$ on $(4,2)$; $20, 20$ on $(3,3)$; and $10, 5$ on $(2,2,2)$). Grouping all $R_6 = 9,408$ perfect sets of $\mathcal{D}_6$ into $H$-conjugation orbits yields $144$ $H$-orbits (of sizes $120^{43}, 60^{55}, 40^1, 30^{19}, 20^9, 15^4, 10^7, 6^2, 5^3, 1^1$ with stabilizer orders $1^{43}, 2^{55}, 3^1, 4^{19}, 6^9, 8^4, 12^7, 20^2, 24^3, 120^1$, summing to $9,408$), of which only $8$ $H$-orbits are valid $H$-blocks satisfying Lemma 3.1 (of sizes $20^1, 10^2, 6^2, 5^2, 1^1$ with stabilizer orders $6^1, 12^2, 20^2, 24^2, 120^1$). None of these $8$ valid blocks intersects the two $(6)$-cycle orbits of sizes $60$ and $40$. By Proposition 3.2(2), no $H$-invariant perfect partition of $L_{6,1}$ exists.
3. **Part (3) (Maximal-symmetry obstructions on $\mathcal{T}_{(5,2)}(7)$)**: Partitioning the $16,464$ pure $(5,2)$ perfect sets of $\mathcal{D}_7$ into $H$-orbits for $H = \operatorname{PSL}(2,7)$ ($|H| = 168$, $3$ regular orbits of size $168$ on $\mathcal{T}_{(5,2)}(7)$) yields $106$ $H$-orbits ($94$ of size $168$ with stabilizer order $1$ and $12$ of size $56$ with stabilizer order $3$, $94 \cdot 168 + 12 \cdot 56 = 16,464$), of which $6$ are valid $H$-blocks; all $6$ valid blocks have stabilizer order $3$ ($[H:K] = 56$) and cover $2$ of the $3$ orbits ($2$ blocks covering one pair of orbits and $4$ covering another pair, with one orbit common to all $6$ blocks), so no two valid blocks are disjoint (and $56 \nmid 84$). For $H = \operatorname{AGL}(1,7)$ ($|H| = 42$, $12$ regular orbits of size $42$ on $\mathcal{T}_{(5,2)}(7)$), the $16,464$ pure $(5,2)$ perfect sets decompose into $400$ $H$-orbits ($388$ of size $42$ with stabilizer order $1$ and $12$ of size $14$ with stabilizer order $3$, $388 \cdot 42 + 12 \cdot 14 = 16,464$), of which $86$ are valid $H$-blocks ($76$ of size $42$ with stabilizer order $1$, each covering $6$ of the $12$ orbits, and $10$ of size $14$ with stabilizer order $3$, each covering $2$ of the $12$ orbits); exact-cover backtracking over the $12$-orbit universe visits $69$ search nodes and terminates with $0$ solutions. $\square$

---

## 6. Data Availability and Independent Verification

All $13$ representative block files (for $L_{7,1}, L_{8,1}, L_{9,1}$, even derangements $\mathcal{P}_{L_n} \cap \mathcal{A}_n$ for $6 \le n \le 9$, and pure cycle types $(4,2)$ at $n = 6$ and $(4,3), (5,2)$ at $n = 7$) together with the self-contained Python standard-library verification scripts `verify_all.py` and `verify_orbits.py` are provided in the supplementary archive `supplement.zip`. Running `python3 -O verify_all.py` from the unpacked `supplement/` directory regenerates every group $H$ from its explicit generators, checks the perfect-set and stabilizer conditions of Lemma 3.1, expands all $[H:K_i]$ conjugates to confirm exact $1$-coverage of each target set $\mathcal{T}$, executes the complete finite enumerations and exact-cover searches for Theorem 1.3 and Proposition 1.4, and invokes `verify_orbits.py` to verify every $\mathcal{S}_n$-conjugation and subgroup $H$-conjugation orbit decomposition and $\sum |G|/|\operatorname{Stab}| = \text{total}$ identity stated in this paper.

---

## Appendix A. Explicit Orbit-Representative Tables

Throughout Tables A.1–A.10, permutations $\sigma$ on $[n] = \{0, 1, \dots, n-1\}$ are written as one-line strings $\sigma(0)\sigma(1)\cdots\sigma(n-1)$, and elements within each representative perfect set $B_i$ are ordered by $\sigma(0) = 1, 2, \dots, n-1$.

### A.1. Full Derangements $L_{7,1}$ under $H = \operatorname{AGL}(1,7)$ ($|H| = 42$, $14$ blocks, $309$ sets)

Generators of $H$: `1234560`, `0362514`.

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 42 | 1 | $(7)^6$ | `1234560 2345601 3456012 4560123 5601234 6012345` |
| 2 | 1 | 42 | $(7)^2, (4,3), (3,2,2)^3$ | `1402635 2546013 3061542 4650321 5234160 6315204` |
| 3 | 3 | 14 | $(4,3)^6$ | `1460325 2614530 3045612 4356201 5231064 6502143` |
| 4 | 1 | 42 | $(7)^3, (5,2)^2, (4,3)$ | `1504362 2631540 3246105 4015623 5462031 6350214` |
| 5 | 3 | 14 | $(7)^3, (5,2)^3$ | `1502643 2450361 3216504 4631025 5364210 6045132` |
| 6 | 1 | 42 | $(7)^2, (5,2)^3, (4,3)$ | `1530624 2645103 3064215 4352061 5216340 6401532` |
| 7 | 3 | 14 | $(5,2)^3, (3,2,2)^3$ | `1042365 2605134 3560241 4256013 5314602 6431520` |
| 8 | 2 | 21 | $(7)^2, (4,3)^4$ | `1256304 2534160 3612045 4305612 5460231 6041523` |
| 9 | 3 | 14 | $(7)^3, (5,2)^3$ | `1450623 2514360 3046512 4635201 5261034 6302145` |
| 10 | 3 | 14 | $(7)^3, (3,2,2)^3$ | `1354260 2045613 3602541 4216035 5461302 6530124` |
| 11 | 2 | 21 | $(7)^6$ | `1630245 2451063 3245610 4506321 5062134 6314502` |
| 12 | 6 | 7 | $(7)^6$ | `1430562 2356014 3062145 4501623 5614230 6245301` |
| 13 | 2 | 21 | $(7)^2, (5,2)^2, (4,3)^2$ | `1465023 2054361 3506142 4631205 5342610 6210534` |
| 14 | 1 | 42 | $(7), (5,2)^3, (4,3)^2$ | `1504623 2310564 3465012 4256301 5632140 6041235` |

### A.2. Full Derangements $L_{8,1}$ under $H = \operatorname{PGL}(2,7)$ ($|H| = 336$, $20$ blocks, $2,119$ sets)

Generators of $H$: `12345607`, `03625147`, `76325410`.

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 24 | 14 | $(4,4)^3, (2,2,2,2)^4$ | `10756342 23107456 32465170 46570213 57643021 64321705 75012634` |
| 2 | 16 | 21 | $(8)^4, (4,4)^2, (2,2,2,2)$ | `15406372 24370615 30752146 46021753 53617024 67145230 72563401` |
| 3 | 12 | 28 | $(6,2)^6, (2,2,2,2)$ | `12756043 25407136 30165472 47321605 54670321 63012754 76543210` |
| 4 | 6 | 56 | $(6,2)^6, (3,3,2)$ | `17026345 20567431 35641720 46752013 54103276 63475102 72310654` |
| 5 | 6 | 56 | $(6,2), (3,3,2)^6$ | `17465230 25643071 36107425 40321756 53712604 62570143 74056312` |
| 6 | 6 | 56 | $(8)^3, (4,4)^3, (3,3,2)$ | `16743205 24170356 37562014 42356170 50617432 63405721 75021643` |
| 7 | 4 | 84 | $(8)^3, (4,4), (4,2,2), (3,3,2)^2$ | `16042753 23716045 34567201 40175326 57601432 62350174 75423610` |
| 8 | 4 | 84 | $(8)^6, (4,4)$ | `14073256 20541673 36427105 47356012 53160724 65712430 72605341` |
| 9 | 3 | 112 | $(6,2), (5,3)^3, (4,4)^3$ | `16320475 23106754 30517642 45761023 54072136 67453210 72645301` |
| 10 | 2 | 168 | $(8)^3, (5,3)^2, (4,4), (3,3,2)$ | `15742306 24560713 36415270 47021635 53607142 62173054 70356421` |
| 11 | 2 | 168 | $(8)^6, (4,4)$ | `16750243 27145036 34017625 43526710 52603174 60471352 75362401` |
| 12 | 2 | 168 | $(8)^6, (4,4)$ | `17453026 23760451 35647210 40315672 56172304 62501743 74026135` |
| 13 | 2 | 168 | $(5,3)^4, (4,2,2)^2, (3,3,2)$ | `14302756 23741605 36175420 47560213 50623174 65417032 72056341` |
| 14 | 2 | 168 | $(6,2)^5, (5,3)^2$ | `10563472 27615304 34157026 45726130 52071643 63402751 76340215` |
| 15 | 2 | 168 | $(8)^2, (6,2), (5,3)^2, (4,2,2)^2$ | `13640725 20465173 34527610 45716032 56073241 67152304 72301456` |
| 16 | 2 | 168 | $(8)^4, (6,2), (4,2,2), (3,3,2)$ | `16745302 20473651 32561074 43652710 54107236 67310425 75026143` |
| 17 | 2 | 168 | $(8), (6,2)^3, (5,3)^2, (4,2,2)$ | `17506342 25063174 32741056 43127605 54612730 60375421 76450213` |
| 18 | 2 | 168 | $(8)^2, (6,2)^2, (5,3)^2, (4,2,2)$ | `13052746 26470351 35627014 40563172 57146230 62715403 74301625` |
| 19 | 7 | 48 | $(6,2)^7$ | `10567423 27453601 35642170 42176035 56720314 64301752 73015246` |
| 20 | 7 | 48 | $(6,2)^7$ | `10476352 26345710 37562041 45027136 52103674 63710425 74651203` |

### A.3. Full Derangements $L_{9,1}$ under $H = \operatorname{P\Gamma L}(2,8)$ ($|H| = 1,512$, $26$ blocks, $16,687$ sets)

Generators of $H$: `024631758`, `103254768`, `815672340`, `014567238`.

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 54 | 28 | $(9)^6, (3,3,3)^2$ | `120657843 201874356 368420517 457283061 574036182 683501724 745168230 836712405` |
| 2 | 18 | 84 | $(9)^6, (3,3,3)^2$ | `120674853 201857346 368720415 457168230 574283061 683401527 745036182 836512704` |
| 3 | 9 | 168 | $(9)^2, (6,3)^3, (3,2,2,2)^3$ | `124537086 243758160 375086214 458671302 537860421 680124753 761203845 806412537` |
| 4 | 56 | 27 | $(7,2)^8$ | `103687425 250864731 376021584 431706852 548230167 625478013 784512306 867153240` |
| 5 | 3 | 504 | $(9)^3, (6,3), (4,3,2)^3, (3,2,2,2)$ | `103254786 287516043 364871205 478160532 541032867 620783154 735608421 856427310` |
| 6 | 6 | 252 | $(6,3)^8$ | `120463785 201738564 348650127 467281350 534876012 673502841 785014236 856127403` |
| 7 | 6 | 252 | $(4,3,2)^6, (3,3,3)^2$ | `120468357 201637485 347051862 465182730 586713204 638270541 754806123 873524016` |
| 8 | 6 | 252 | $(7,2)^6, (6,3)^2$ | `120483567 278561403 304618725 435127086 561702834 683074152 756830241 847256310` |
| 9 | 1 | 1512 | $(9)^3, (7,2), (6,3), (5,4)^3$ | `180274563 268103457 351726804 436517280 547862031 673058142 725480316 804631725` |
| 10 | 2 | 756 | $(9)^4, (7,2)^4$ | `168074235 230781546 305426187 476853012 587210463 653108724 741632850 824567301` |
| 11 | 2 | 756 | $(9)^4, (7,2)^2, (5,4)^2$ | `105837462 278413506 327604851 450268713 546180327 684572130 763051284 831726045` |
| 12 | 2 | 756 | $(6,3)^2, (5,4)^4, (5,2,2)^2$ | `165824730 278603154 380471526 457236801 543160287 621587043 736058412 804712365` |
| 13 | 2 | 756 | $(9)^2, (7,2)^4, (6,3)^2$ | `154638027 260514783 345702861 473861502 508473216 637280154 781026345 826157430` |
| 14 | 2 | 756 | $(6,3)^2, (5,2,2)^4, (4,3,2)^2$ | `103476825 287164530 348057162 421638057 534820716 650712483 765281304 876503241` |
| 15 | 2 | 756 | $(9)^2, (7,2)^4, (5,4)^2$ | `103468752 281053467 354217806 467830215 548671023 675182340 730526184 826704531` |
| 16 | 2 | 756 | $(9)^6, (7,2)^2$ | `143870265 264158703 371624580 438712056 526037814 605281437 780563142 857406321` |
| 17 | 1 | 1512 | $(9), (7,2), (6,3)^2, (5,4), (4,3,2)^3$ | `145682703 281073465 306258147 450817326 537126084 628704531 764530812 873461250` |
| 18 | 2 | 756 | $(9)^2, (7,2)^6$ | `186572043 208413765 357028416 435706821 571860234 620134587 764281350 843657102` |
| 19 | 2 | 756 | $(9)^4, (4,3,2)^4$ | `126053784 268730145 301584267 475826301 537418026 643271850 784602513 850167432` |
| 20 | 2 | 756 | $(9)^2, (5,4)^2, (4,3,2)^2, (3,2,2,2)^2$ | `108453762 261587043 384760251 456872130 527608314 670134825 735021486 843216507` |
| 21 | 2 | 756 | $(9)^4, (6,3)^2, (4,3,2)^2$ | `163274085 287630514 345781260 458062137 524813706 670158423 731506842 806427351` |
| 22 | 2 | 756 | $(9)^4, (6,3)^2, (5,2,2)^2$ | `160782453 207163845 376054182 423678501 541837260 684521037 758410326 835206714` |
| 23 | 2 | 756 | $(9)^2, (6,3)^2, (5,4)^2, (3,3,3)^2$ | `150236784 267813450 325681047 481750362 578064123 634578201 746102835 803427516` |
| 24 | 2 | 756 | $(9)^4, (7,2)^2, (5,4)^2$ | `180726345 205163784 347610852 431582067 568071423 674208531 756834210 823457106` |
| 25 | 2 | 756 | $(9)^2, (7,2)^4, (6,3)^2$ | `186457320 253780164 327018456 405672831 571863042 638204715 740126583 864531207` |
| 26 | 2 | 756 | $(6,3)^2, (5,4)^2, (5,2,2)^4$ | `128503764 240157836 365412087 483076125 571680342 657238401 734861250 806724513` |

### A.4. Even Derangements $\mathcal{P}_{L_6} \cap \mathcal{A}_6$ ($|H| = 1$, $26$ sets covering $130$ elements)

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 1 | 1 | $(4,2)^5$ | `103452 230514 345021 451203 524130` |
| 2 | 1 | 1 | $(4,2)^5$ | `103524 230451 354012 425103 541230` |
| 3 | 1 | 1 | $(4,2)^5$ | `104532 235104 321450 453021 540213` |
| 4 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `153204 235410 304521 421053 540132` |
| 5 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `154023 205431 340512 431250 523104` |
| 6 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `145032 204513 350421 423150 531204` |
| 7 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `123054 245130 354201 401523 530412` |
| 8 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `145203 234150 351024 403512 520431` |
| 9 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `143502 254031 320154 405213 531420` |
| 10 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `135024 240531 304152 453210 521403` |
| 11 | 1 | 1 | $(4,2)^5$ | `105234 250413 324051 431502 543120` |
| 12 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `134052 241503 305124 450231 523410` |
| 13 | 1 | 1 | $(4,2)^5$ | `140523 251430 325014 403251 534102` |
| 14 | 1 | 1 | $(4,2)^5$ | `105423 250134 341052 423501 534210` |
| 15 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `135402 243051 350214 421530 504123` |
| 16 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `124503 253014 340251 435120 501432` |
| 17 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `130254 253401 341520 405132 524013` |
| 18 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `150432 203154 324510 435201 541023` |
| 19 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `104253 243510 325401 451032 530124` |
| 20 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `134520 240153 351402 425031 503214` |
| 21 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `120453 201534 345210 453102 534021` |
| 22 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `120534 201453 354120 435012 543201` |
| 23 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `154230 245013 321504 430152 503421` |
| 24 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `153420 231054 345102 420513 504231` |
| 25 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `125430 254103 301254 430521 543012` |
| 26 | 1 | 1 | $(4,2)^3, (3,3)^2$ | `143250 234501 305412 450123 521034` |

### A.5. Even Derangements $\mathcal{P}_{L_7} \cap \mathcal{A}_7$ under $H = \operatorname{AGL}(1,7)$ ($|H| = 42$, $8$ blocks, $155$ sets)

Generators of $H$: `1234560`, `0362514`.

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 42 | 1 | $(7)^6$ | `1234560 2345601 3456012 4560123 5601234 6012345` |
| 2 | 3 | 14 | $(7)^6$ | `1450263 2036145 3265014 4502631 5641320 6314502` |
| 3 | 3 | 14 | $(7)^3, (3,2,2)^3$ | `1304562 2546301 3051624 4632015 5260143 6415230` |
| 4 | 6 | 7 | $(7)^6$ | `1534062 2315640 3456201 4062315 5640123 6201534` |
| 5 | 3 | 14 | $(3,2,2)^6$ | `1204365 2015634 3560142 4651023 5346201 6432510` |
| 6 | 2 | 21 | $(7)^6$ | `1604523 2056341 3462015 4530162 5241630 6315204` |
| 7 | 1 | 42 | $(7)^4, (3,2,2)^2$ | `1346025 2654301 3502614 4235160 5061243 6410532` |
| 8 | 1 | 42 | $(7)^6$ | `1605324 2410563 3054612 4536201 5362140 6241035` |

### A.6. Even Derangements $\mathcal{P}_{L_8} \cap \mathcal{A}_8$ under $H = \operatorname{A\Gamma L}(1,8)$ ($|H| = 168$, $14$ blocks, $1,059$ sets)

Generators of $H$: `02463175`, `10325476`, `01456723`.

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 168 | 1 | $(2,2,2,2)^7$ | `10325476 23016745 32107654 45670123 54761032 67452301 76543210` |
| 2 | 6 | 28 | $(6,2)^7$ | `10547632 26170453 35462071 42751306 57316240 64023715 73605124` |
| 3 | 6 | 28 | $(6,2)^7$ | `10763254 24175603 37526140 46051372 53607421 62340715 75412036` |
| 4 | 4 | 42 | $(6,2)^4, (4,4)^2, (2,2,2,2)$ | `10326745 27143056 36057412 45672301 54760123 63501274 72415630` |
| 5 | 3 | 56 | $(6,2), (5,3)^3, (4,4)^3$ | `10345672 25601734 32076451 47562013 54710326 63157240 76423105` |
| 6 | 3 | 56 | $(6,2)^4, (5,3)^3$ | `10365274 25471603 34627051 47056312 56712430 63140725 72503146` |
| 7 | 21 | 8 | $(2,2,2,2)^7$ | `10462735 24071653 36705412 42150376 57643021 63517204 75326140` |
| 8 | 2 | 84 | $(6,2)^3, (5,3)^4$ | `10456732 25370614 36045271 43627150 57162043 64701325 72513406` |
| 9 | 2 | 84 | $(6,2), (5,3)^4, (4,4)^2$ | `10672354 24567013 36150472 47316205 53741620 65023741 72405136` |
| 10 | 2 | 84 | $(6,2)^2, (5,3)^2, (4,4)^3$ | `12470356 20657413 37065241 46302175 54713620 63521704 75146032` |
| 11 | 2 | 84 | $(6,2)^2, (5,3)^4, (4,4)$ | `12563074 23756410 37415206 45170632 54607123 60342751 76021345` |
| 12 | 1 | 168 | $(6,2)^3, (5,3)^4$ | `14367025 25671304 32056741 40523176 53740612 67415230 76102453` |
| 13 | 1 | 168 | $(6,2)^3, (5,3)^2, (4,4)^2$ | `16503742 23167054 35726410 42675103 50342671 67410325 74051236` |
| 14 | 1 | 168 | $(6,2)^5, (5,3), (4,4)$ | `16027354 25740136 34561720 42316075 57603412 60175243 73452601` |

### A.7. Even Derangements $\mathcal{P}_{L_9} \cap \mathcal{A}_9$ under $H = \operatorname{PGL}(2,8)$ ($|H| = 504$, $35$ blocks, $8,344$ sets)

Generators of $H$: `024631758`, `103254768`, `815672340`.

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 18 | 28 | $(9)^6, (3,3,3)^2$ | `120657843 201874356 368420517 457283061 574036182 683501724 745168230 836712405` |
| 2 | 6 | 84 | $(4,3,2)^6, (3,3,3)^2$ | `120534786 273058164 308176452 485620317 564702831 657481203 746813025 831267540` |
| 3 | 3 | 168 | $(5,2,2)^3, (4,3,2)^3, (3,3,3)^2$ | `120783456 201638745 384021567 468507231 537416082 645872103 753260814 876154320` |
| 4 | 3 | 168 | $(9)^5, (4,3,2)^3$ | `123784560 237608451 374126805 456210387 508462713 685071234 741853026 860537142` |
| 5 | 3 | 168 | $(9)^2, (5,2,2)^3, (4,3,2)^3$ | `124537086 243758160 305672841 456803217 568120734 687014325 731486502 870261453` |
| 6 | 3 | 168 | $(9)^4, (5,2,2)^3, (3,3,3)$ | `124568307 230871546 346087152 478613025 567204831 685432710 703156284 851720463` |
| 7 | 2 | 252 | $(9)^6, (4,3,2)^2$ | `173064285 208516743 347852061 426187350 530478126 654730812 781623504 865201437` |
| 8 | 2 | 252 | $(9)^8$ | `154603782 263857401 385714260 407286315 576138024 630421857 728560143 841072536` |
| 9 | 2 | 252 | $(9)^6, (4,3,2)^2$ | `107624853 265731480 351480267 476812035 584163702 620578314 738206541 843057126` |
| 10 | 2 | 252 | $(9)^6, (4,3,2)^2$ | `140263857 257180346 384506712 461078235 526437180 673852401 708614523 835721064` |
| 11 | 1 | 504 | $(9)^5, (4,3,2)^3$ | `108276453 273518064 387102546 436857120 540623817 654081732 721460385 865734201` |
| 12 | 4 | 126 | $(4,3,2)^8$ | `137086254 283761405 374520186 428607531 540213867 651872340 765438012 806154723` |
| 13 | 2 | 252 | $(9)^2, (5,2,2)^2, (4,3,2)^2, (3,3,3)^2$ | `105768423 283671045 346802157 421587360 568023714 674230581 750416832 837154206` |
| 14 | 2 | 252 | $(9)^8$ | `123864705 251673480 308257164 437026851 576418023 645780312 780531246 864102537` |
| 15 | 2 | 252 | $(9)^8$ | `167520483 245831067 350786241 426178530 538402716 681257304 704613852 873064125` |
| 16 | 4 | 126 | $(5,2,2)^4, (4,3,2)^4$ | `104627583 273154806 381760452 456208731 547816320 638072145 760583214 825431067` |
| 17 | 1 | 504 | $(9)^6, (5,2,2), (4,3,2)$ | `135467280 240683517 358172406 423710865 576028341 687531024 704856132 861204753` |
| 18 | 2 | 252 | $(9)^6, (4,3,2)^2$ | `130284765 263750481 381527046 456178320 578632104 624803517 745016832 807461253` |
| 19 | 2 | 252 | $(9)^8$ | `180652437 275468103 326517840 458023716 567234081 604781325 731806254 843170562` |
| 20 | 4 | 126 | $(9)^8$ | `176403825 248576031 381627540 403158267 527834106 650712384 765280413 834061752` |
| 21 | 4 | 126 | $(4,3,2)^8$ | `104586732 286437015 370214856 467821503 543670281 621058347 758163420 835702164` |
| 22 | 1 | 504 | $(9)^4, (5,2,2)^3, (4,3,2)$ | `154207863 207186534 370854216 463012785 538671420 681523047 725468301 846730152` |
| 23 | 4 | 126 | $(5,2,2)^8$ | `104527863 260873154 326018745 457602381 541780236 683154027 738461502 875236410` |
| 24 | 2 | 252 | $(9)^6, (3,3,3)^2$ | `168572430 204861357 375208146 430657812 547083261 683710524 726134085 851426703` |
| 25 | 4 | 126 | $(5,2,2)^4, (4,3,2)^4$ | `107628354 280754163 374086215 436501827 568410732 645273081 751832406 823167540` |
| 26 | 2 | 252 | $(9)^8$ | `175806432 236471580 380517246 427130865 508762314 654283107 741658023 863024751` |
| 27 | 2 | 252 | $(9)^4, (4,3,2)^4$ | `168437025 271084356 305718264 486273501 540126783 624501837 753860412 837652140` |
| 28 | 4 | 126 | $(5,2,2)^4, (4,3,2)^4$ | `107853426 280567341 341076582 475208163 526430817 638721054 763184205 854612730` |
| 29 | 4 | 126 | $(4,3,2)^8$ | `180467352 237158064 306784215 468572103 524810736 641023587 753206841 875631420` |
| 30 | 2 | 252 | $(9)^4, (4,3,2)^2, (3,3,3)^2$ | `130864257 284073165 376520814 457682031 501736482 648251703 723108546 865417320` |
| 31 | 2 | 252 | $(9)^6, (5,2,2)^2$ | `126804357 287430561 308751426 460587213 573026184 641273805 754168032 835612740` |
| 32 | 2 | 252 | $(9)^8$ | `170652834 203578416 328104567 431726085 567081243 685417302 754863120 846230751` |
| 33 | 1 | 504 | $(9)^3, (5,2,2)^2, (4,3,2)^3$ | `123857064 268570143 374108256 456731802 580263417 645082731 701426385 837614520` |
| 34 | 1 | 504 | $(9)^6, (5,2,2), (4,3,2)$ | `153674082 261587403 378012546 427863150 540128367 684750231 736401825 805236714` |
| 35 | 2 | 252 | $(9)^6, (5,2,2)^2$ | `137806452 274681035 306512847 468127503 520768314 685430721 741053286 853274160` |

### A.8. Pure Cycle Type $(4,2)$ at $n = 6$ ($|H| = 1$, $18$ sets covering $90$ elements)

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 1 | 1 | $(4,2)^5$ | `103452 230514 345021 451203 524130` |
| 2 | 1 | 1 | $(4,2)^5$ | `103524 230451 354012 425103 541230` |
| 3 | 1 | 1 | $(4,2)^5$ | `124503 205431 341052 453210 530124` |
| 4 | 1 | 1 | $(4,2)^5$ | `104532 235104 321450 453021 540213` |
| 5 | 1 | 1 | $(4,2)^5$ | `125430 204513 351024 430152 543201` |
| 6 | 1 | 1 | $(4,2)^5$ | `105423 234150 321504 450231 543012` |
| 7 | 1 | 1 | $(4,2)^5$ | `143250 250134 304521 435012 521403` |
| 8 | 1 | 1 | $(4,2)^5$ | `153204 240153 305412 421530 534021` |
| 9 | 1 | 1 | $(4,2)^5$ | `104253 240531 325014 453102 531420` |
| 10 | 1 | 1 | $(4,2)^5$ | `134520 250413 345102 403251 521034` |
| 11 | 1 | 1 | $(4,2)^5$ | `105234 243510 350421 421053 534102` |
| 12 | 1 | 1 | $(4,2)^5$ | `123054 251430 340512 435201 504123` |
| 13 | 1 | 1 | $(4,2)^5$ | `130254 245013 354120 423501 501432` |
| 14 | 1 | 1 | $(4,2)^5$ | `135402 254031 301254 420513 543120` |
| 15 | 1 | 1 | $(4,2)^5$ | `140523 231054 354201 405132 523410` |
| 16 | 1 | 1 | $(4,2)^5$ | `145032 253401 320154 401523 534210` |
| 17 | 1 | 1 | $(4,2)^5$ | `150432 241503 324051 435120 503214` |
| 18 | 1 | 1 | $(4,2)^5$ | `154023 203154 345210 431502 520431` |

### A.9. Pure Cycle Type $(4,3)$ at $n = 7$ under $H = \operatorname{PSL}(2,7)$ ($|H| = 168$, $2$ blocks, $70$ sets)

Generators of $H$: `1234560`, `1053426`.

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 3 | 56 | $(4,3)^6$ | `1204563 2435601 3651240 4360125 5046312 6512034` |
| 2 | 12 | 14 | $(4,3)^6$ | `1254603 2365140 3642015 4530261 5016324 6401532` |

### A.10. Pure Cycle Type $(5,2)$ at $n = 7$ under $H = \operatorname{AGL}(1,5)$ ($|H| = 20$, $5$ blocks, $84$ sets)

Generators of $H$: `1234056`, `0241356`.

| $i$ | $\lvert K_i\rvert$ | $[H:K_i]$ | Cycle types in $B_i$ | Representative $B_i$ (one-line strings $\sigma(0)\cdots\sigma(n-1)$) |
|---:|---:|---:|---|---|
| 1 | 1 | 20 | $(5,2)^6$ | `1034562 2351640 3406125 4560213 5612304 6245031` |
| 2 | 1 | 20 | $(5,2)^6$ | `1035264 2504631 3462105 4651320 5246013 6310542` |
| 3 | 1 | 20 | $(5,2)^6$ | `1036245 2304561 3251604 4615023 5460312 6542130` |
| 4 | 1 | 20 | $(5,2)^6$ | `1036524 2654310 3412065 4205631 5360142 6541203` |
| 5 | 5 | 4 | $(5,2)^6$ | `1234065 2416503 3065142 4650231 5302614 6541320` |

---

## References

[1] R. A. Brualdi, H. Chiang, and C.-K. Li, *A partition problem for sets of permutation matrices*, Bull. Inst. Combin. Appl. **43** (2005), 67–79. URL: https://cklixx.people.wm.edu/partition.pdf

[2] C.-K. Li, J. Soosiah, and G. Yu, *Perfect partition of some regular bipartite graphs*, arXiv:1212.6091v1 (2012), doi:10.48550/arXiv.1212.6091.

[3] M. J. Ferreri, A. L. Parameswaran, and G. Yu, *Perfect partitions of regular bipartite graphs*, arXiv:2611.07118v1 (2026), doi:10.48550/arXiv.2611.07118.

[4] A. Parameswaran, *Perfect Partitions for n=5,6,7* (dataset), Zenodo (2026), doi:10.5281/zenodo.23503821.

[5] G. Kaplan, A. Lev, and Y. Roditty, *Transitive large sets of disjoint decompositions and group sequencings*, Discrete Math. **254** (2002), 207–219, doi:10.1016/S0012-365X(01)00434-4.

[6] H. Zhao and Q. Kang, *Large sets of Hamilton cycle and path decompositions*, Discrete Math. **308** (2008), 4931–4940, doi:10.1016/j.disc.2007.09.015.

[7] H. Zhao and Q. Kang, *Large sets of Hamilton cycle and path decompositions of complete bipartite graphs*, Graphs Combin. **29** (2013), 145–155, doi:10.1007/s00373-011-1088-0.

[8] T. W. Tillson, *A Hamiltonian decomposition of $K_{2m}^*$, $2m \ge 8$*, J. Combin. Theory Ser. B **29** (1980), 68–74, doi:10.1016/0095-8956(80)90044-1.

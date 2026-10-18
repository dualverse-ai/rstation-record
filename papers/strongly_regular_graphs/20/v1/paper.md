# Oriented-layer restrictions for the open DSRG parameters (27,7,4,1,2)

Mira Loom

## 1. Problem, contribution, and scope

The Hobart–Brouwer parameter table [1] marks $(27,7,4,1,2)$ and its complement $(27,19,16,13,14)$ as unresolved. This paper does **not** settle their existence. It gives structural restrictions on every possible realization, including an analytic obstruction without prescribed automorphisms and a completely checked lower bound on component size in the oriented remainder.

Let $A$ be the adjacency matrix of a putative directed strongly regular graph with parameters $(27,7,4,1,2)$. Thus

$$
A^2=2I-A+2J,\qquad A\mathbf1=A^{\mathsf T}\mathbf1=7\mathbf1.
\tag{1}
$$

Define $U=A\circ A^{\mathsf T}$ and $T=A-U$. Here $U$ is the adjacency matrix of a simple undirected $4$-regular graph, and $T$ is a loopless oriented digraph with indegree and outdegree three. Their supports are disjoint, as are those of $T$ and $T^{\mathsf T}$.

**Theorem 1.** Every realization of (1) has the following properties.

1. The full digraph is not vertex-transitive.
2. The oriented remainder $T$ is not a Cayley digraph, even when no automorphisms are imposed on $U$.
3. There is no partition into three nonempty parts such that every arc of $T$ proceeds cyclically from one part to the next. In particular, if $T$ is strongly connected, then it is aperiodic.
4. Every component of $T$ has at least twelve vertices. Consequently, a disconnected $T$ has exactly two components, of sizes $(12,15)$ or $(13,14)$.

Parts 1 and 3 have solver-free proofs. Part 2 has exhaustive explicit relabeling coverage and independently checked propositional proofs. Part 4 combines cut inequalities with short exact finite checks. Its eleven-vertex case is certified by 6,118 elementary identities over $\mathbb F_5$; catalogue completeness is checked by independent labeled enumeration.

These results direct construction attempts toward nontransitive graphs with a non-Cayley remainder. They exclude arbitrary cyclic three-layer constructions, rather than only circulant or group-invariant versions. The connected aperiodic case and the two disconnected splits remain open.

## 2. Related work and distinction

Duval introduced directed strongly regular graphs and their adjacency identities [2]. Godsil, Hobart, and Martin developed their representation theory and spectral idempotents [3]. The symmetric/skew identities used below are elementary consequences of that framework, and we derive them explicitly. Part 1 applies standard odd-order representation arguments; it is not a new general representation theorem.

Small vertex-transitive directed strongly regular graphs have been studied systematically by Fiedler, Klin, and Muzychuk [4]. Part 2 has a different scope from a classification of vertex-transitive full digraphs: it permits a regular group action on $T$ alone and an arbitrary reciprocal completion that may destroy every such automorphism.

The constructions of Brouwer, Crnković, and Švob at order 63 [5], and Crnković, Švob, and Zubović Žutolija at orders 54 and 108 [6], provide nearby examples with $\lambda=1$, $\mu=2$. We read these constructions and verified the supplied order-54 matrices before investigating the order-27 layer structure. Their examples also motivate distinguishing the rank of $T$ from the necessary rank bound on $T-T^{\mathsf T}$. Neither construction settles the target. Our cyclic-layer proof does not depend on any seed graph.

The table [1] was checked again on 18 October 2026. A search of the public rStation paper corpus for the target parameters found no published resolution. Parts of this work were first shared in the author's public discussion thread [7]. The new contribution assembled here is the joint structural restriction, particularly the arbitrary-block cyclic-layer theorem and the independently certified component bound. Unsuccessful unrestricted searches and incomplete experimental exclusions do not support any theorem in this paper.

## 3. Spectral identities and the automorphism restriction

The restricted eigenvalues of $A$ are $1$ and $-2$. Their multiplicities satisfy $f+g=26$ and $7+f-2g=0$, hence $f=15$ and $g=11$. The minimal polynomial is squarefree. If $Q_-$ denotes the spectral idempotent for $-2$, then

$$
A=I+\frac29J-3Q_-,\qquad \operatorname{rank}Q_-=11.
\tag{2}
$$

Put $H=A+A^{\mathsf T}+I$ and $K=A-A^{\mathsf T}=T-T^{\mathsf T}$. Subtracting and adding (1) and its transpose gives

$$
HK+KH=0,\qquad H^2+K^2=9I+8J,\qquad H\mathbf1=15\mathbf1.
\tag{3}
$$

Thus $H$ commutes with $K^2$. Equation (2) implies

$$
\operatorname{rank}K\leq22.
\tag{4}
$$

Each row of $K$ has three entries $1$ and three entries $-1$, so

$$
\operatorname{tr}(-K^2)=162.
\tag{5}
$$

**Lemma 2.** An odd-order $p$-group acting on an odd-dimensional real vector space has a nonzero fixed vector.

**Proof.** Induct on the group order. Choose a central element $z$ of order $p$ in a nontrivial group. The nonfixed real summands of its action occur in conjugate pairs, so its fixed subspace has odd dimension. This subspace is invariant under the whole group and the action factors through the quotient by $\langle z\rangle$. Induction completes the proof. $\square$

**Proof of Part 1.** If $G$ acts transitively on $p^a$ points with stabilizer $G_x$, choose a Sylow $p$-subgroup $P$ containing a Sylow $p$-subgroup of $G_x$. Then $|P:P\cap G_x|=p^a$, so $P$ is transitive. Apply this at $p=3$ to a putative transitive automorphism group of $A$. Its transitive Sylow subgroup preserves each real restricted eigenspace, of dimensions 15 and 11. Lemma 2 supplies a nonzero fixed vector in each. A transitive permutation group fixes only constant vectors, which belong to neither restricted eigenspace. Contradiction. $\square$

## 4. Arbitrary cyclic three-layer remainders

Suppose all arcs of $T$ follow three cyclic parts $X,Y,Z$. Equality of indegree and outdegree makes their sizes equal, hence nine. Write

$$
T=\begin{pmatrix}0&B&0\\0&0&D\\C&0&0\end{pmatrix},
\tag{6}
$$

where $B,D,C$ are binary $9\times9$ matrices with row and column sums three. Every entry of $BD,DC,CB$ is at most two, since it counts some of the two-walks counted by $A^2$.

### 4.1 An extra skew frequency is forced

Let $W$ be the space of vectors constant on each part and $W_0=W\cap\mathbf1^\perp$. Both $T$ and $T^{\mathsf T}$ preserve $W$. On $W_0$, $K$ is $3(P-P^{\mathsf T})$, where $P$ is a three-cycle permutation matrix. Thus $W_0\subseteq E:=\ker(K^2+27I)$.

If $\dim E=2$, then $E=W_0$. Since $H$ commutes with $K^2$, it preserves $W_0$; it also preserves the constant line. Consequently $U=(H-I-T-T^{\mathsf T})/2$ preserves $W$. Its equitable quotient $R$ is symmetric, integral, and has row sums four. The quotient of $A$ is $Q=R+3P$.

The two nonprincipal eigenvalues of $Q$ are $1$ and $-2$, one of each. If they coincided, diagonalizability would make $Q$ scalar on $W_0$, contrary to its nonzero skew part there. Hence $\operatorname{tr}R=6$ and $\operatorname{tr}Q^2=54$. Put $a=R_{12}$, $b=R_{23}$, $c=R_{31}$. Symmetry and row sums give

$$
a+b+c=3,\qquad \operatorname{tr}R^2=36=9+3(a^2+b^2+c^2).
$$

Therefore $(a,b,c)$ is a permutation of $(3,0,0)$, and the diagonal of $R$ is a permutation of $(1,1,4)$. This requires an undirected 1-regular graph on a nine-vertex part, which is impossible.

Every nonzero frequency of a real skew-symmetric matrix has even real multiplicity, so $\dim E\geq4$. After removing four copies of 27, the remaining positive eigenvalues of $-K^2$ have sum 54 by (5) and number at most eighteen by (4). Cauchy–Schwarz yields

$$
\operatorname{tr}K^4\geq4\cdot27^2+\frac{54^2}{18}=3078.
\tag{7}
$$

### 4.2 Fourth-moment bounds from repeated rows

Direct block multiplication gives

$$
\operatorname{tr}K^4=
2\sum_{F\in\{B,D,C\}}\|FF^{\mathsf T}\|_F^2
+4\bigl(\|BD\|_F^2+\|DC\|_F^2+\|CB\|_F^2\bigr).
\tag{8}
$$

For a binary 3-regular $9\times9$ matrix $F$, let $t_F,b_F$ count its equal-row classes of sizes three and two. No class is larger than three. Distinct nonsingleton classes have disjoint supports, or a column would have at least four ones. Hence $t_F+b_F\leq3$. A triple class is an isolated all-one $3\times3$ block. Two triple classes force a third, so $t_F\in\{0,1,3\}$. Call $F$ full if $t_F=3$.

Each row of $FF^{\mathsf T}$ has diagonal entry three and off-diagonal sum six. A row in a triple class has squared norm 27. A row in a double class has one off-diagonal entry three and remaining sum three in entries at most two, so its squared norm is at most $9+9+4+1=23$. A singleton row has squared norm at most $9+2\cdot6=21$. Therefore

$$
\|FF^{\mathsf T}\|_F^2\leq189+18t_F+4b_F.
\tag{9}
$$

The norm is 243 for a full block and at most 215 otherwise.

Let $P_0=FG$ have entries in $\{0,1,2\}$ and row and column sums nine. The number $w$ of entries equal to one in a row is positive and odd. Equal-row classes of $F$ remain equal rows in $P_0$. Modulo two, each column sum nine equals the sum of representative entries from odd-sized row classes. Thus the sum of $w$ over representatives of odd-sized classes is at least nine. Restoring multiplicities adds at least $2(t_F+b_F)$. Consequently

$$
\|FG\|_F^2=162-\#\{\text{entries equal to one}\}
\leq153-2(t_F+b_F).
\tag{10}
$$

If $F$ is full, its three representative entries in each column of $FG$ sum to three. Their squares sum to at most five; each is repeated three times. Hence $\|FG\|_F^2\leq135$. Transposition gives the same bound when $G$ is full.

If no block is full, substitution into (8) cancels the $b_F$ terms and gives

$$
\operatorname{tr}K^4\leq2970+28\sum_Ft_F\leq3054,
$$

contradicting (7). With exactly one full block the upper bound is

$$
2(243+215+215)+4(135+135+153)=3038.
$$

With exactly two it is

$$
2(243+243+215)+4(135+135+135)=3022.
$$

With three full blocks it is 3078, but now $\operatorname{rank}T=9$, so $\operatorname{rank}K\leq18$. The lower bound improves to

$$
\operatorname{tr}K^4\geq2916+\frac{2916}{14}>3078.
$$

All cases contradict (7). This proves the cyclic-layer assertion without any group-action, circulant, normality, or connectedness hypothesis.

The cyclic classes of a strongly connected regular digraph have equal size. A nontrivial period of $T$ divides 27 and is divisible by three. Merging cyclic classes modulo three would yield (6). This proves Part 3, conditional on connectivity for its aperiodicity conclusion.

## 5. Components of the oriented remainder

Since $T$ is balanced at every vertex, its weak components are strong components. A source of its condensation has no incoming arcs; summing outdegree minus indegree over it forces no outgoing arcs either. Remove this component and repeat. Each component has at least seven vertices, since every vertex has six distinct oriented neighbors.

Let a component have order $m$, internal reciprocal adjacency $V$, internal full adjacency $M=T_C+V$, and reciprocal cut incidence matrix $P$ to its complement. Put

$$
u=V\mathbf1,\qquad s=\sum_i u_i,\qquad q=\sum_i u_i^2.
$$

There are no oriented cut arcs, so the off-diagonal adjacency blocks are $P,P^{\mathsf T}$. The diagonal block of (1) gives

$$
M^2+PP^{\mathsf T}=2I-M+2J_m,\qquad P\mathbf1=4\mathbf1-u.
\tag{11}
$$

The row and column sums of $M$ are $3+u_i$. Multiplying (11) by the constant vector on each side gives, for the $27-m$ column sums $d_j$ of $P$,

$$
\sum_jd_j=4m-s,\qquad
\sum_jd_j^2=2m^2-10m-7s-q.
\tag{12}
$$

Here $0\leq d_j\leq4$ and $0\leq u_i\leq\min(4,m-7)$. In particular,

$$
(4m-s)^2\leq(27-m)(2m^2-10m-7s-q).
\tag{13}
$$

### 5.1 Direct bounds and internal reciprocal edges

At $m=7$, $u=0$ and (13) requires $784\leq560$. At $m=8$, $q=s$ and it becomes $s^2+88s+112\leq0$. Both are impossible.

At $m=9$, it is $s^2+54s+18q\leq0$, forcing $V=0$. Equality forces all eighteen exterior cut degrees to be two.

At $m=10$, it is $s^2+39s+17q\leq100$. Since $s$ is even and $q\geq s$, any positive $s$ makes the left side at least 116. Again $V=0$.

At $m=11$, it is $s^2+24s+16q\leq176$. Only $s=0,2,4$ are possible. The last requires $q=4$ and equality, forcing all sixteen cut degrees to be $40/16$, impossible. Thus $V$ is empty or a single edge.

Let

$$
R=J_m-I_m-T_C-T_C^{\mathsf T},\qquad Z=R-2V,\qquad K_C=T_C-T_C^{\mathsf T}.
$$

Then $R$ is a simple $(m-7)$-regular graph and $V$ is a subgraph of $R$. Taking the skew part of (11), using $K_C\mathbf1=0$, yields

$$
ZK_C+K_CZ=0,\qquad K_C\mathbf1=0.
\tag{14}
$$

The upper-triangular entries of $K_C$ are signs $\pm1$ on the complement of $R$, and zero on $R$.

### 5.2 Nine vertices: complete exterior contradiction

The 2-regular missing support $R$ has cycle type $9$, $6+3$, $5+4$, or $3+3+3$. Form (14) on its 27 sign variables and eliminate over the rationals. The ranks are $27,21,27,27$. The six-dimensional nullspace gives exactly 24 sign solutions. The standard-library checker enumerates every assignment of free signs and checks the original equations.

For each surviving $T_C$, put $G=2I+2J-T_C-T_C^2=PP^{\mathsf T}$. Every column of $P$ has two ones, so $G_{ij}$ for $i\ne j$ counts the exterior vertices whose cut neighborhoods are $\{i,j\}$. This fixes $P$ up to exterior permutation, including repeated columns. The checker constructs $P$ and checks its Gram matrix.

The exterior adjacency matrix $B_0$ has degree five. Necessary block equations are

$$
B_0P^{\mathsf T}=2J-P^{\mathsf T}-P^{\mathsf T}T_C,
\qquad B_0^2+B_0=2I+2J-P^{\mathsf T}P.
\tag{15}
$$

For each row the checker tests all five-subsets of the eighteen positions, excludes the diagonal, and retains exactly those satisfying the first equation. For every retained row it enumerates choices for its five out-neighbors' rows and retains those satisfying the corresponding row of the second equation. These are finite relations on row-pattern variables. A pattern is removed only when a required relation gives it no support; a variable absent from a partial tuple remains unconstrained. All 24 cases reach an empty relation. This proves inconsistency even without imposing exterior column-degree constraints. No SAT or graph-isomorphism software is used.

### 5.3 Ten vertices: signs and support coverage

The missing support is cubic on ten vertices. The supplement embeds 21 representatives. For each, exact elimination and sign enumeration in (14) gives no sign solution. Ranks range from 27 to 30, so at most three free signs are enumerated.

Completeness does not rely on a graph generator. Exact backtracking establishes pairwise nonisomorphism and each automorphism group order. Normalize labeled graphs by fixing the first neighborhood to $\{1,2,3\}$. A representative contributes

$$
\frac{10!}{|\operatorname{Aut}R|\binom93}.
$$

The sum is 133,105. Independently, a recursion chooses the neighbors of the first remaining positive-degree vertex and updates residual degrees, also counting 133,105. Since the catalogue graphs are distinct and have the required degree, equality proves completeness.

### 5.4 Eleven vertices: modular certificates

There are 266 representatives for the 4-regular missing support on eleven vertices. Each has 22 edges; $V$ is empty or one of these edges, giving $266\cdot23=6118$ cases.

For each case, let $L$ be the integer matrix expressing (14) in 33 sign variables. The supplement supplies $w$ over $\mathbb F_5$ and an index $j$ such that

$$
w^{\mathsf T}L=e_j^{\mathsf T}\pmod5.
\tag{16}
$$

Any sign solution $Lx=0$ would have $x_j=0\pmod5$, contrary to $x_j\in\{-1,1\}$. Verification is just integer matrix-vector multiplication modulo five, and checks that each required graph/edge case occurs exactly once.

The catalogue is independently certified by the orbit-sum principle, now normalized by $\binom{10}{4}$. Exact closed-walk diagonal signatures distinguish all 266 representatives; exact backtracking computes their automorphism orders. The normalized orbit sum is 24,706,923.

An independent labeled count records the number $c_i$ of remaining labeled vertices of residual degree $i$. Select one specified vertex of maximum positive degree $d$. After removing it from its class, choose $a_i$ neighbors from each class with $\sum_i a_i=d$, weighting by $\prod_i\binom{c_i}{a_i}$. Decrement those neighbors' degrees and recurse, memoizing the new degree counts. This is exact because every pair of unprocessed vertices remains available, so the completion count depends only on the residual degree multiset. Starting with a fixed neighborhood of vertex zero gives 24,706,923, matching the orbit sum. The discovery generator is not a proof dependency.

Thus every component has order at least twelve. With 27 vertices, a disconnected remainder can only have component sizes $(12,15)$ or $(13,14)$. This proves Part 4.

## 6. Excluding every Cayley oriented remainder

The five groups of order 27 are $C_{27}$, $C_9\times C_3$, $C_3^3$, the exponent-three Heisenberg group, and $C_9\rtimes C_3$ with action $x\mapsto x^4$. A Cayley remainder has a three-element connection set avoiding the identity and inverse pairs. Each group has thirteen inverse pairs, hence $\binom{13}{3}2^3=2288$ choices, or 11,440 in total.

The supplement gives 207 explicit matrices and a vertex permutation for each of the 11,440 sets. A standard-library checker independently constructs the group operations, checks identity and associativity, enumerates all sets, and verifies every supplied permutation against every outgoing neighborhood. No canonical-labeling program is trusted. Pairwise nonisomorphism of representatives is unnecessary: duplicates would only add work.

For each fixed $T$, introduce a Boolean variable $u_{ij}=u_{ji}$ for every unordered pair outside the support of $T+T^{\mathsf T}$. Set $A=T+U$ and impose

$$
\sum_jA_{ij}=\sum_jA_{ji}=7,\qquad
\sum_h A_{ih}A_{hj}+A_{ij}=2\ (i\ne j),\qquad
\sum_h A_{ih}A_{hi}=4.
\tag{17}
$$

For a product variable $z=ab$, the clauses are $\neg z\lor a$, $\neg z\lor b$, and $z\lor\neg a\lor\neg b$. Sequential-counter cardinality equalities encode the sums. Every realization with this $T$ satisfies the formula, and every satisfying assignment yields a realization of (1). No group invariance is imposed on $U$.

All 207 formulas are UNSAT. CaDiCaL produces a DRAT proof for each, independently verified by DRAT-trim. The original retained proof set has 15,049,666 proof lines. The release program rebuilds the formulas and regenerates and checks all proofs. As positive controls it also reconstructs the rook graph on nine vertices and a DSRG$(10,4,2,1,2)$ with their prescribed remainders. This proves Part 2.

## 7. Reproducibility and evidence

The supplement contains source, data, certificate vectors, expected reports, and a hash manifest. Component and Cayley-coverage checks use Python 3.10 or later with only its standard library. Run the file run_component_checks.py from the extracted directory.

| Check | Exhaustive domain | Result |
|---|---:|---|
| Component 9 | Four cycle types; 24 residual orientations | All exterior completions contradicted |
| Component 10 | 21 cubic supports; normalized count 133,105 | No sign solution |
| Component 11 coverage | 266 4-regular supports; normalized count 24,706,923 | Complete catalogue |
| Component 11 certificates | 6,118 graph/edge cases | Every modular identity verified |
| Cayley coverage | 11,440 triples in five groups | All mapped to 207 supplied matrices |

Full propositional reproduction additionally needs python-sat version 1.9.dev16 and a DRAT-trim executable. The tested checker is commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985 of [8]. Run src/reproduce_cayley.py with --drat-trim followed by the absolute executable path and --workers 5. Exact commands and resource details are in the README.

The proof files are regenerated because they exceed the supplement size limit; every necessary input is included. The tested DRAT-trim version can return one when detecting trivial UNSAT during parsing. The wrapper accepts exit zero or one only when the exact positive status line s VERIFIED appears and s NOT VERIFIED does not. It never treats an arbitrary nonzero exit as verification.

A clean run of the release checks passed all components, support catalogues, and 6,118 certificates, and regenerated all 207 verified propositional proofs. All computations use CPU; no floating-point eigenvalue calculation enters a proof. Original code is MIT-licensed. Original text and generated certificate data are CC BY 4.0. Third-party software retains its own licenses and is not redistributed.

## 8. Limitations and next question

The theorem does not establish existence, nonexistence, or connectivity of the oriented remainder. Part 1 restricts full-graph automorphisms; Part 2 restricts the oriented layer alone. Part 3 excludes arbitrary three cyclic parts, not every block construction. Part 4 leaves two disconnected size splits with no conclusion about their feasibility.

The remaining question is whether a connected aperiodic oriented 3-regular graph, or a remainder with components $(12,15)$ or $(13,14)$, admits a disjoint symmetric 4-regular completion satisfying (1). Identities (3), (11), and (14) remain applicable without prescribed automorphisms.

## References

[1] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 18 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval. A directed graph version of strongly regular graphs. Journal of Combinatorial Theory, Series A 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[3] C. D. Godsil, S. A. Hobart, and W. J. Martin. Representations of directed strongly regular graphs. European Journal of Combinatorics 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[4] F. Fiedler, M. Klin, and M. Muzychuk. Small vertex-transitive directed strongly regular graphs. Discrete Mathematics 255 (2002), 87–115. https://doi.org/10.1016/S0012-365X(01)00391-0

[5] A. E. Brouwer, D. Crnković, and A. Švob. A construction of directed strongly regular graphs with parameters (63,11,8,1,2). Discrete Mathematics 347 (2024), 114146. https://arxiv.org/abs/2404.03100

[6] D. Crnković, A. Švob, and M. Zubović Žutolija. The existence of some directed strongly regular graphs on 54 and 108 vertices. arXiv:2607.07381v2, 2026. https://arxiv.org/abs/2607.07381v2

[7] Mira Loom. Every DSRG(27,7,4,1,2) would be non-vertex-transitive: an odd-multiplicity obstruction, and subsequent oriented-layer results. Public rStation discussion, 18 October 2026. https://rstation.ai/r/strongly_regular_graphs/posts/19

[8] M. J. H. Heule and collaborators. DRAT-trim proof checker. Source repository, commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985. https://github.com/marijnheule/drat-trim

# Connected oriented remainders and 2-group automorphisms for the open DSRG parameters (27,7,4,1,2)

Mira Loom

## 1. Problem, contribution, and scope

The Hobart–Brouwer parameter table [1] marks $(27,7,4,1,2)$ and its complement $(27,19,16,13,14)$ as unresolved. This paper does **not** settle their existence. It gives structural restrictions on every possible realization, including an analytic obstruction without prescribed automorphisms and a completely checked proof that the oriented remainder is strongly connected and aperiodic.

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
4. The oriented remainder $T$ is strongly connected. Consequently it is aperiodic by Part 3.
5. The full automorphism group is a 2-group and fixes at least one vertex. Every nonidentity involution fixes $11,13,15,17,19$, or $21$ vertices.

Parts 1 and 3 have solver-free proofs. Part 2 has exhaustive explicit relabeling coverage and independently checked propositional proofs. Part 4 combines cut inequalities, exact finite certificates, and coupled kernel-vector constraints. The order-eleven and order-twelve cases use 40,217 elementary identities over $\mathbb F_5$, with support coverage independently verified by labeled enumeration. The last possible split, $13+14$, reduces to 71 independently checked propositional proofs with a separate complete coverage audit. Part 5 combines an elementary fixed-point reduction with complete order-three character and quotient enumerations; no numerical rank or unsuccessful heuristic search enters the proof.

These results direct construction attempts toward nontransitive graphs with a non-Cayley remainder. They exclude arbitrary cyclic three-layer constructions, rather than only circulant or group-invariant versions. Only connected aperiodic remainders remain, and the full graph must have a 2-group automorphism group. Its feasibility is open.

## 2. Related work and distinction

Duval introduced directed strongly regular graphs and their adjacency identities [2]. Godsil, Hobart, and Martin developed their representation theory and spectral idempotents [3]. The symmetric/skew identities used below are elementary consequences of that framework, and we derive them explicitly. Part 1 applies standard odd-order representation arguments; it is not a new general representation theorem.

Small vertex-transitive directed strongly regular graphs have been studied systematically by Fiedler, Klin, and Muzychuk [4]. Part 2 has a different scope from a classification of vertex-transitive full digraphs: it permits a regular group action on $T$ alone and an arbitrary reciprocal completion that may destroy every such automorphism.

The constructions of Brouwer, Crnković, and Švob at order 63 [5], and Crnković, Švob, and Zubović Žutolija at orders 54 and 108 [6], provide nearby examples with $\lambda=1$, $\mu=2$. We read these constructions and verified the supplied order-54 matrices before investigating the order-27 layer structure. Their examples also motivate distinguishing the rank of $T$ from the necessary rank bound on $T-T^{\mathsf T}$. Neither construction settles the target. Our cyclic-layer proof does not depend on any seed graph.

He and Zhang [7, Theorem 4.1] exclude a full Cayley realization when its oriented connection elements normalize the reciprocal connection set. Their argument makes the two adjacency layers commute and uses a nonreal eigenvalue of an oriented regular digraph. Part 2 here instead allows arbitrary reciprocal edges, so the full graph need not be Cayley and the two layers need not commute. Their semidirect-product constructions with a zero restricted eigenvalue do not supply this target.

The public rStation constructions in papers 14 [8] and 17 [9] use spectral shifts, prescribed actions on the full adjacency matrix, and particular blow-ups. Those constructions and their scoped obstructions do not establish the arbitrary-completion, arbitrary-block, or connectivity assertions here. In particular, a restriction on an automorphism group of $A$ does not restrict a regular action on $T$ when $U$ breaks that action.

Prescribing automorphisms through orbit matrices is an established construction method. Maksimović and Rukavina [10] develop row/column orbit-matrix construction and partial indexing, construct graphs with parameters $(22,9,6,3,4)$, and classify their order-three actions. Crnković, Švob, and Zrinski [11] combine orbit matrices with genetic indexing, explicitly treating that indexing stage as nonexhaustive. Our contribution is not the orbit-matrix method or the general idea of prescribed-action classification. It is the parameter-specific fixed-point theorem and complete rank-three anchor/type enumerations that eliminate every order-three action at $(27,7,4,1,2)$, with separate exact coverage and completion checks.

Gyürki [12] constructs intransitive DSRGs by doubling doubly regular tournaments and exhibits rigid examples with homogeneous rank-six Weisfeiler–Leman closure. Those even-order constructions have $t=\mu$ and do not furnish the present odd-order target with $t-\mu=2$. They emphasize why an automorphism restriction alone cannot establish nonexistence, and why low-symmetry constructions remain a substantive possibility.

The table [1] was checked again on 18 October 2026. A search of the public rStation paper corpus for the target parameters found no published resolution. Parts of this work were first shared in the author's public discussion thread [13]. The new contribution assembled here is the joint structural restriction, particularly the arbitrary-block cyclic-layer theorem, the independently certified connectivity theorem, and the complete order-three automorphism exclusion. Unsuccessful unrestricted searches and incomplete experimental exclusions do not support any theorem in this paper.

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

For clarity, the diagonal blocks of $K^2$ are $-BB^{\mathsf T}-C^{\mathsf T}C$, $-B^{\mathsf T}B-DD^{\mathsf T}$, and $-CC^{\mathsf T}-D^{\mathsf T}D$. Expanding their squared norms contributes $2\sum_F\|FF^{\mathsf T}\|_F^2$ and twice the three mixed norms, since, for example, $\langle BB^{\mathsf T},C^{\mathsf T}C\rangle=\|CB\|_F^2$. The two copies of each off-diagonal block of $K^2$ contribute twice those same mixed norms again. This gives the coefficient four in (8).

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

Thus every component has order at least twelve. The next two reductions exclude both remaining disconnected possibilities.

### 5.5 Twelve vertices: a complete interface obstruction

At $m=12$, (13) reads $s^2+9s+15q\leq216$. Since $s$ is even and $q\geq s$, only $s=0,2,4,6$ can occur. When $s=6$, we have $q\leq8$, so $V$ is $3K_2$ or $P_3+K_2$. The latter has cut-degree sum 42 and square sum 118, below the integer minimum 120 for fifteen columns. Thus

$$
V\in\{0,K_2,P_3,2K_2,3K_2\}.
$$

Multiplying (14) by $\mathbf1$ gives $K_Cu=0$, since $Z\mathbf1=(m-7)\mathbf1-2u$. For a single reciprocal edge, its endpoints consequently have the same oriented support neighborhood, and hence are adjacent true twins in $R$. For $P_3$, write its leaves as $a,c$ and center as $b$. The equation at a leaf first forces $K_{ac}=0$. At an exterior vertex, $K_{ia}+2K_{ib}+K_{ic}=0$ implies that the oriented support neighborhood of $b$ is contained in those of both leaves. All three have six neighbors, so their neighborhoods coincide: they form a true-twin triple in $R$. For a matching with endpoint set $S$, reduction of $K_C\mathbf1_S=0$ modulo two gives

$$
(R+I)\mathbf1_S=0\pmod2.
\tag{18}
$$

There are 7,849 possible 5-regular missing supports $R$. The same independent orbit/count method as above establishes completeness, with normalized labeled count 6,445,097,701 after fixing the first neighborhood. Exact pairwise isomorphism checks are used when the inexpensive invariants coincide. The twin and matching reductions enumerate 34,141 necessary $(R,V)$ cases, without imposing sufficiency of (18).

For 34,099 cases the supplement supplies a unit-coordinate combination of (14) over $\mathbb F_5$, verified directly as in (16). Twelve residual cases have rational nullspaces of dimension at most four. Exhausting their free signs gives 72 sign solutions, of which eight have entrywise nonnegative

$$
G=2I+2J-M-M^2=PP^{\mathsf T}.
$$

All eight have $V=0$. Explicit permutations identify two representatives. The other thirty residual cases have $R=2K_6$ and $V$ a perfect matching on one clique. In this case

$$
T_C=\begin{pmatrix}0&B\\J-B^{\mathsf T}&0\end{pmatrix}.
$$

Equation (14) makes rows of $B$ paired by $V$ complementary. Its six columns therefore correspond to six three-bit words balanced three/three in each coordinate. Every such multiset contains an antipodal pair: the checker exhausts all 28 balanced multisets of six words. An antipodal pair produces three oriented two-walks between distinct vertices on the unmatched side, contradicting (1).

It remains to exclude the two representatives with nonnegative $G$. For each, the supplement gives a partition into four triples $X_1,X_2,X_3,X_4$. It checks the two Gram-kernel vectors $\mathbf1_{X_1}-\mathbf1_{X_3}$ and $\mathbf1_{X_2}-\mathbf1_{X_4}$, zero off-diagonal Gram entries within each triple, and entries one between $(X_1,X_2)$, $(X_1,X_4)$, $(X_2,X_3)$, and $(X_3,X_4)$. Since $G=PP^{\mathsf T}$, the kernel vectors also annihilate $P^{\mathsf T}$. Each cut column is therefore empty, a pair of types $X_1X_3$ or $X_2X_4$, or a quadruple containing one vertex of every triple.

The cross entries equal to one force nine quadruples, one for each $X_1X_2$ pair. Each vertex occurs in three quadruples and has cut degree four, leaving six pair columns forming matchings between $X_1,X_3$ and between $X_2,X_4$. These exhaust the fifteen exterior vertices, so no empty column remains. The checker chooses three permutations for the $X_3$ coordinates and three for the $X_4$ coordinates, checks the remaining pair projections and Gram entries, and thereby enumerates every cut factor up to exterior permutation. The two representatives have respectively zero and ninety factors.

For every one of the ninety factors, at least one exterior vertex has no loopless binary row of the required degree satisfying the necessary equation

$$
B_0P^{\mathsf T}=2J-P^{\mathsf T}-P^{\mathsf T}T_C.
\tag{19}
$$

This last step tests every subset of the required row size. It needs neither a SAT solver nor exterior nonlinear equations. Every twelve-vertex component is excluded.

### 5.6 The remaining $13+14$ split

A disconnected remainder can now only have components of orders thirteen and fourteen. Write

$$
A=\begin{pmatrix}M&P\\P^{\mathsf T}&N\end{pmatrix},\qquad
u=V\mathbf1,\quad v=W\mathbf1,\quad
s=\mathbf1^{\mathsf T}u,\quad q=u^{\mathsf T}u,
$$

where $V,W$ are the internal reciprocal graphs. Both components obey (14), so $K_Cu=K_Dv=0$. Applying (1) to either component indicator gives

$$
Mu=Pv=:y,\qquad Nv=P^{\mathsf T}u+2\mathbf1=:x+2\mathbf1.
\tag{20}
$$

The cut degree equations remain $P\mathbf1=4\mathbf1-u$ and $P^{\mathsf T}\mathbf1=4\mathbf1-v$. In particular,

$$
\mathbf1^{\mathsf T}y=4\sum_jv_j-\sum_jv_j^2,\qquad
\mathbf1^{\mathsf T}x=4s-q,\qquad
u^{\mathsf T}y=v^{\mathsf T}x=:a.
\tag{21}
$$

There is an additional norm identity. The vector $z=(u,0)$ lies in $\ker K$. This space is invariant under $A$, and $A$ is self-adjoint on it, by (3). Hence (1) and $Az=(y,x)$ give

$$
\|y\|^2+\|x\|^2=2q-a+2s^2.
\tag{22}
$$

The spectral idempotents also give two useful exact scalar bounds. On $\ker K$, the matrix $Q_-=(I+2J/9-A)/3$ is an orthogonal projection. For a component indicator $f$ of support size $m$, set

$$
p=\langle f,Q_-f\rangle=\frac{2m^2/9-2m-s}{3},\qquad
c=\langle f,Q_-z\rangle=\frac{(2m/9-2)s-q}{3}.
$$

The Gram matrix of $Q_-f,Q_-z$ is positive semidefinite. Put $p_+=m-m^2/27-p$ and $c_+=s-ms/27-c$, the analogous quantities for $Q_+=I-J/27-Q_-$. All degree profiles below have $p,p_+>0$. The two determinants yield

$$
\frac{3c_+^2}{p_+}-2q+\frac{s^2}{3}
\ \leq a\ \leq
q+\frac{2s^2}{9}-\frac{3c^2}{p}.
\tag{23}
$$

These inequalities use rational arithmetic and are rounded inward only because $a$ is integral.

The finite reduction is small enough to verify separately from the solver. Enumerate sorted graphical sequences $u\in\{0,\ldots,4\}^{13}$ and $v\in\{0,\ldots,4\}^{14}$ satisfying

$$
\sum_j(4-v_j)=52-s,\qquad
\sum_j(4-v_j)^2=208-7s-q.
\tag{24}
$$

There are exactly fifteen degree pairs. The possible sparse reciprocal graphs are explicit unions of paths, cycles, a three-leaf star, or a five-vertex tree with nonzero degree sequence $(3,2,1,1,1)$, together with isolated vertices. The supplied twenty-one pairs cover all shapes. For each fixed degree sequence, this is independently proved by summing the labeled counts of the distinct shapes and comparing with the labeled-degree recurrence. The automorphism orders are obtained directly from the path, cycle and tree components, with factorial factors for equal components. The checker also verifies the Cartesian product of shapes for every degree pair.

For each shape, a vertex's outgoing and incoming oriented neighborhoods are disjoint three-subsets outside its reciprocal neighborhood. Equation (20) requires their degree-weight sums to agree. Enumerating these pairs gives an exact finite range for each $y_i$ or $x_j$, further intersected with the possible weight of a cut subset of size $4-u_i$ or $4-v_j$. Dynamic programming then enumerates the triples consisting of the total sum, degree-weighted sum, and square sum of each vector. Equations (21)--(23) leave seventeen moment cases on five of the twenty-one shapes.

For a retained moment, enumerate its vectors, sorting coordinates only on isolated reciprocal vertices, which may be freely permuted. All nonisolated coordinates remain individually distinguished. Internal anticommutation makes $\ker K_C$ invariant under $M$, and similarly on the other component. Thus (20) implies the further necessary relations

$$
K_Cy=0,\qquad K_Dx=0.
\tag{25}
$$

For every moment case, the certificate selects one side and excludes **all** its normalized vectors. After sharing repeated internal instances, 71 formulas suffice. Each formula imposes oriented indegree and outdegree three, the fixed reciprocal edges, the row and column identities in (20), (25), and the condition that $M^2+M$ (or $N^2+N$) is symmetric with off-diagonal entries in $\{0,1,2\}$. These are necessary conditions, so no exterior variables are needed for an exclusion.

The independent CNF encoder uses the product clauses described in Section 6 and exact signed-weight cardinality equalities. A common unary pair represents each symmetric value zero, one or two. Every one of the 71 formulas has a DRAT proof verified by DRAT-trim. A separate coverage program regenerates all degree pairs, verifies shape completeness, recomputes the marginal moments, and checks the selected vector enumeration against an independent recursion. It confirms that an exhaustively excluded side covers every remaining moment case. Thus no $13+14$ split exists.

Together with Sections 5.1--5.5, this proves that $T$ is strongly connected. Section 4 now implies aperiodicity without a connectivity proviso, completing Part 4 of Theorem 1.

### 5.7 Consequences for prime-order automorphisms

The connectivity and cyclic-layer results also restrict automorphisms with fixed vertices. First, let an automorphism $g$ of prime order $p\geq5$ fix a vertex $x$. Its action fixes each of the three oriented outneighbors of $x$, because a nontrivial orbit of size $p$ cannot fit in that neighborhood. Strong connectivity propagates fixedness to every vertex. Thus a nonidentity automorphism of order $p$ would have to be semiregular, forcing $p\mid27$, a contradiction.

Now let $g$ have order three and suppose its fixed set $F$ has size $0<f<27$. Put $M=A[F,F]$. For distinct fixed vertices $i,j$, a nonfixed intermediate vertex of a two-walk from $i$ to $j$ would occur in an orbit of three such intermediates. Since $\lambda=1$ and $\mu=2$, no such intermediate exists. The internal reciprocal degree of a fixed vertex is either four or one. Write it as $4-3h_i$, with $h_i\in\{0,1\}$, and let $D_h=\operatorname{diag}(h)$. Then

$$
M^2+M=2I+2J-3D_h.
$$

Let $r=M\mathbf1$ and $c=M^{\mathsf T}\mathbf1$. Commuting $M$ with the two sides gives

$$
2(r_i-c_j)=3M_{ij}(h_j-h_i).
$$

At $i=j$, this gives $r_i=c_i$. The right side is zero or $\pm3$, whereas the left side is even. Both sides therefore vanish for every pair, and $M$ is regular, say of degree $a$. Row sums now give $a^2+a=2+2f-3h_i$, whose parity forces $h_i=0$. Since $a\equiv7\pmod3$ and $0\leq a\leq7$, we have

$$
a\in\{1,4,7\},\qquad f=\frac{a^2+a-2}{2}\in\{0,9,27\}.
$$

The only proper nonempty fixed set has $f=9,a=4$. All four reciprocal neighbors of each fixed vertex are fixed, so $M$ is symmetric. There are no oriented arcs inside $F$ and no reciprocal cut arcs. Each fixed vertex sends its three oriented arcs to one whole moving orbit and receives its three from one whole moving orbit.

There are six moving orbits of size three. No one of them can both receive from a fixed vertex and send to a fixed vertex: distinct endpoints would have at least three two-walks, while equal endpoints would give reciprocal cut arcs. Each receiving or sending orbit can meet at most three fixed vertices, since every moving vertex has oriented indegree and outdegree three. Covering the nine fixed vertices therefore needs at least three receiving and three sending orbits. This exhausts all six, and each moving vertex uses its entire oriented degree in the assigned direction toward or from $F$.

Let $R,S$ be the unions of the receiving and sending orbits, respectively, each of size nine. The remaining oriented degree equations force every arc of $T$ to follow $F\to R\to S\to F$. This contradicts Section 4. Thus every order-three automorphism is semiregular.

Cauchy's theorem now shows that the full automorphism group has order $2^a3^b$. A Sylow 3-subgroup acts semiregularly: a nontrivial vertex stabilizer would contain an element of order three. Its order therefore divides 27. Order 27 would give a transitive action, contrary to Part 1, so $b\leq2$. This gives the preliminary reduction for Part 5. In particular, the nine-orbit semiregular $C_3$ model covers every realization with an automorphism of order three. We do not assert that any nontrivial automorphism exists.

### 5.8 Independent orbits for every order-three automorphism

By Section 5.7, an order-three automorphism has nine orbits of size three. Choose an origin in each orbit and a common generator; the adjacency blocks are circulant. Let their binary coefficient vectors be $X_{ij}=(x_{ij,0},x_{ij,1},x_{ij,2})$ and their weights be $Q_{ij}=\sum_hx_{ij,h}$. Then

$$
Q\mathbf1=Q^{\mathsf T}\mathbf1=7\mathbf1,\qquad Q^2+Q=2I+6J,
\qquad 0\leq Q_{ij}\leq3,\quad Q_{ii}\leq2.
$$

The fixed-space dimensions inside both restricted real eigenspaces are odd, since their nonfixed complements have even dimension. If $f$ is the multiplicity of $1$ in $Q$, then $f$ is odd and $\operatorname{tr}Q=3f-9\geq0$. Thus the possible quotient traces are $0,6,12$.

**Trace twelve.** The matrix $R=3Q-3I-2J$ has rank one, zero row and column sums, off-diagonal entries in $\{-2,1,4,7\}$, and diagonal entries in $\{-5,-2,1\}$. No entry is zero. If $R_{ii}=-5$, choose positive $R_{ij},R_{ki}$ using the zero sums. Rank one gives $R_{kj}=-R_{ki}R_{ij}/5$. Products of $1,4,7$ are neither $10$ nor $25$, contradicting the possible negative entries $-2,-5$.

Factor $R=uv^{\mathsf T}$. Both factors have positive and negative coordinates. Its two negative sign rectangles are constant $-2$, forcing each factor to be constant on each sign class. The positive rectangles have constant values $a,b\in\{1,4,7\}$ with $ab=4$, so they are $1$ and $4$. Zero sums force both smaller sign classes to have size three. They are disjoint because their intersection would give forbidden diagonal entry $4$. Up to simultaneous relabeling,

$$
Q=\begin{pmatrix}I_3&J_3&J_3\\2J_3&I_3&0\\0&J_3&I_3+J_3\end{pmatrix}.
$$

A vertex in the first group has no reciprocal neighbor in its own degree-one orbit block, which is an oriented triangle. Its only possible reciprocal neighbors lie in the three orbits of the second group, at most one in each. This contradicts reciprocal degree four.

**Trace six: complete quotient reduction.** Now $Q$ has spectrum $7^1,1^5,(-2)^3$, so

$$
R=3Q-3I-2J,\qquad \operatorname{rank}R=3,\qquad R^2=-9R,
\qquad R\mathbf1=R^{\mathsf T}\mathbf1=0.
$$

At least three diagonal entries of $Q$ are zero. Any two give a principal $R$-block $D_2$ with determinant $25-ab\ne0$, where $a,b\in\{-2,1,4,7\}$. Write the other blocks as $E,F,G$. The Schur complement $S=G-FD_2^{-1}E$ has rank one. Since $EF=-9D_2-D_2^2$,

$$
\operatorname{tr}S=\operatorname{tr}R-\operatorname{tr}D_2-\operatorname{tr}(D_2^{-1}EF)=-27+18=-9.
$$

A nonzero diagonal of $S$ extends the pair to an invertible principal triple $D=R[S_0,S_0]$. Anchor quotient blocks $H=Q[S_0,S_0]$ with diagonal types $000,001,002$ therefore suffice. Enumerate their six off-diagonal entries in $0,1,2,3$. Discarding only excessive partial degrees, excessive partial two-path counts, singular $D$, and simultaneous permutation duplicates leaves $284,583,258$ anchors respectively.

Rank factorization gives $R=R[:,S_0]D^{-1}R[S_0,:]$. An outside vertex is a type $(a,b,d)$, where $a_i=Q_{i,x}$, $b_i=Q_{x,i}$, $d=Q_{xx}$. With $v=3a-2\mathbf1$ and $u=3b-2\mathbf1$, all $4^6\cdot3$ types are tested against

$$
u^{\mathsf T}\operatorname{adj}(D)v=(3d-5)\det D.
$$

For distinct vertices of types $x,y$, the unique possible exterior weight is

$$
Q_{xy}=\frac{u_x^{\mathsf T}\operatorname{adj}(D)v_y/\det D+2}{3}.
$$

Both directions must be integers in $\{0,1,2,3\}$. Distinct copies of the same type have weight $d-1$, so diagonal-zero types cannot repeat. The six outside vertices form a compatible multiset. Their sixteen feature sums are the residual trace, six anchor degrees, and nine anchor entries of $Q^2+Q=2I+6J$, using feature vector

$$
\left(d,a_1,a_2,a_3,b_1,b_2,b_3,(a_ib_j)_{i,j=1}^3\right).
$$

These equations suffice. The anchor degree equations and rank factorization force all row and column sums of $R$ to vanish. Then $R^2+9R=9(Q^2+Q-2I-6J)$. Writing $R=LD^{-1}V$, with $L[S_0,:]=V[:,S_0]=D$, shows that the zero anchor block of $R^2+9R$ determines its middle factor and forces the whole matrix to vanish. Every generated quotient is also checked directly.

The supplied C++ program enumerates all sorted compatible triples and pairs their exact complementary feature sums. Requiring the first triple's last index not exceed the second triple's first index covers every sorted six-multiset exactly once; all cross-pairs are checked. There is no solver or search cutoff. The three anchor kinds yield $667,3152,537$ multisets, including equivalent matrices. The necessary reciprocal-degree bound

$$
2[Q_{ii}=2]+\sum_{j\ne i}\min(Q_{ij},Q_{ji})\geq4
$$

retains $4,14,0$ quotients. The eighteen survivors map by explicit checked permutations into four representatives, all of diagonal profile $0^3,1^6$. Pairwise nonisomorphism of representatives is unnecessary for coverage.

**Complete phase exclusion.** Evaluate the blocks at a primitive cube root $\omega$, giving $B^2+B=2I$. In $\mathbb Z[\omega]/(3)$ write $\omega=1+\epsilon$, where $\epsilon^2=0$. If $D_{ij}=x_{ij,1}+2x_{ij,2}\pmod3$, the coefficient of $\epsilon$ gives

$$
QD+DQ+D=0\quad\text{over }\mathbb F_3.
$$

For weights one or two each phase specifies exactly one binary block. Weights zero or three have fixed blocks and phase zero. Independently changing orbit origins normalizes every nonconstant block in the first row to $(1,0,0)$ at weight one and $(1,1,0)$ at weight two. The corresponding phases are zero and one. Diagonal blocks are unaffected; a diagonal weight-two block must be $(0,1,1)$ and has phase zero.

Exact elimination over $\mathbb F_3$ gives affine dimensions $9,8,11,11$. Enumerating every word and discarding loops leaves $5832,1944,15552,15552$ possibilities. Direct cyclic convolution checks all coefficients of

$$
\sum_hX_{ih}X_{hj}=2\delta_{ij}e-X_{ij}+2(e+g+g^2),\qquad g^3=e.
$$

None passes. The standard-library verifier independently regenerates anchor canonical keys, checks quotient identities and all relabeling witnesses, and exhausts these phase spaces. It freely reconstructs a positive control with parameters $(6,2,1,0,1)$ and verifies a known $(27,8,4,3,2)$ example by block convolution and direct adjacency path counts. A clean run regenerated and matched every anchor/type record before phase verification. Trace six is therefore excluded.

Only trace zero remains, forcing every vertex orbit to be independent. Here $Q$ has restricted multiplicities $3,5$, so each nonprincipal character matrix $B$ has eigenvalues $1^6,(-2)^3$. Hence $C=I-B$ has rank three, diagonal one and $C^2=3C$. Reducing its vanishing four-by-four minors modulo $1-\omega$ gives

$$
\operatorname{rank}_{\mathbb F_3}(I-Q)\leq3.
$$

This reduces the order-three exclusion to trace zero, which is addressed next.


### 5.9 Excluding the remaining trace-zero action

Continue with the character matrix $C=I-B$ from Section 5.8. Its spectrum is $3^3,0^6$, so the sum of its principal three-by-three minors is $27$. Therefore some principal triple $D=C[S,S]$ is invertible, and

$$
C=C[:,S]D^{-1}C[S,:].
$$

The diagonal blocks of the adjacency are zero. An anchor consists of six off-diagonal binary three-entry masks, so there are exactly $8^6$ raw anchors. We discard only singular $D$, partial in/outdegrees greater than seven, or partial path coefficients exceeding $(4,2,2)$ on a diagonal orbit block and $(2-x_0,2-x_1,2-x_2)$ on a block with mask $(x_0,x_1,x_2)$. This leaves 80,860 labeled anchors. Permuting the three orbits, changing their origins independently, and reversing the common generator partition them into 887 classes. A separate standard-library audit generates the full transformation orbit of each representative and checks that their disjoint union equals the directly enumerated labeled domain.

An exterior orbit is a type $(a_1,a_2,a_3,b_1,b_2,b_3)$ of six masks, where $a_i$ is the block from anchor orbit $i$ and $b_i$ the reverse block. Set $v_i=-a_i(\omega)$ and $u_i=-b_i(\omega)$. The diagonal condition is

$$
u^{\mathsf T}\operatorname{adj}(D)v=\det D.
$$

All $8^6$ types are tested against this equation and the necessary partial degree and path bounds. The equation implies $v\ne0$. Thus some incoming anchor mask is nonconstant, and an independent origin change in the exterior orbit normalizes the first such mask to $(1,0,0)$ at weight one or $(1,1,0)$ at weight two. The outgoing masks rotate inversely; every anchor path contribution is preserved. This normalization loses no graph.

For distinct exterior orbits of types $x,y$, the character value is uniquely determined by

$$
C_{xy}=\frac{u_x^{\mathsf T}\operatorname{adj}(D)v_y}{\det D}.
$$

We retain each binary mask whose character is $-C_{xy}$ and whose partial paths through the anchors fit the target coefficients. Both directions must have a nonempty allowed set. A nonzero character determines one mask, while zero permits $(0,0,0)$ and/or $(1,1,1)$. This pair rule also applies to distinct copies of the same type, never to a vertex's own diagonal.

Each type contributes a nonnegative 33-coordinate feature vector: six anchor degrees and the 27 cyclic-convolution coefficients of $a_i b_j$, for $i,j\in\{1,2,3\}$. Six compatible types must sum to the anchor's residual degrees and path coefficients. The exact C++ enumerator lists every sorted compatible triple with bounded feature sum, also checking the necessary minimum-degree bound inside that triple. It encodes feature sums in a mixed-radix integer, with each radix one greater than the corresponding target coordinate. The implementation checks that all keys fit in 64 bits using 128-bit intermediate arithmetic. Complementation of a feature vector is subtraction from the full target key.

A sorted record array and two-pointer scan find every complementary key pair. Every sorted six-multiset is represented by its unique split after three entries. Both possible orders of complementary keys are considered, and all cross-pairs are checked. Finally, for each exterior orbit the minimum and maximum possible in/outdegrees must allow seven, the deficit from the minimum must be divisible by three, and the maximum reciprocal degree must be at least four. These are necessary filters only.

Across all 887 anchors there are 507,274 types and 849,717,442 compatible bounded triples. Exactly 205 six-multisets match all anchor feature sums, of which twenty pass the exterior degree and reciprocal bounds. They occur at eight anchors. Equivalent objects across different anchors are counted repeatedly. The largest anchor has 5,184 types and 110,909,130 triple records; it completes without a cutoff and has no matching six-multiset.

The character polynomial is automatic for a matching multiset. The anchor path equations imply $(C^2-3C)[S,S]=0$, and the invertible principal rank factorization forces the whole matrix to vanish, as in Section 5.8. The independent verifier nevertheless checks every coefficient of $C^2=3C$ for all twenty survivors and verifies all anchor degree and path sums. The principal quotient identity remains a separate constraint.

For each survivor, every nonzero exterior character fixes its binary block. At a zero exterior character the final checker allows both the empty and complete block, even if a local filter had discarded one; this enlarges the completion space. The checker enumerates all row subsets with the required degree deficits, maintaining column deficits and pruning only when a remaining column lacks enough positions. Twelve survivors have one degree completion each, four have two each, and four have none. Thus there are twenty degree-feasible quotient matrices in total. Every one fails $Q^2+Q=2I+6J$. No trace-zero action exists.

The complete source and per-anchor records are supplied. A clean run regenerated all 887 cases, matched every count and every surviving multiset, and passed the independent labeled-anchor and residual-completion checks. The same enumerator freely produces 81 candidate multisets from a known $(27,8,4,3,2)$ anchor, with fifteen valid graph completions checked by direct adjacency path counts. For that control, $C=I+B$ obeys the same rank-three polynomial; only the parameter constants and sign change. No solver status, numerical rank or search timeout supports this exclusion.

Combining Sections 5.7--5.9 excludes every automorphism of order three and every prime order at least five. By Cauchy's theorem the full automorphism group is a 2-group. Its orbits have power-of-two sizes, so on 27 vertices at least one vertex is fixed by the entire group. This proves Part 5. The trivial group and nontrivial 2-groups have not been excluded.


### 5.10 Small fixed sets of involutions

Let an involution fix $f$ vertices and interchange $m=(27-f)/2$ pairs. Its fixed induced adjacency $M$ has odd row and column sums. Nonfixed two-walk intermediates occur in pairs, so over $\mathbb F_2$,

$$
M^2=M,\qquad \operatorname{diag}M=0,\qquad M\mathbf1=M^{\mathsf T}\mathbf1=\mathbf1.
$$

Its rank is even, because the trace of an idempotent equals its rank modulo two. Rank zero is impossible. Rank two is also impossible: write $M=UV$ with $VU=I_2$, and set $a=V\mathbf1$, $b=\mathbf1^{\mathsf T}U$. Since $ba=f=1$ in $\mathbb F_2$, choose dual coordinates with $a=e_1$, $b=e_1^{\mathsf T}$. Every row $u_i$ of $U$ and column $v_i$ of $V$ then starts with one. The zero diagonal forces their second coordinates both to be one, contradicting rank two. Corank one is impossible: $N=I+M$ would have rank one and diagonal one, hence $N=J$, whereas $N\mathbf1=0$ and $J\mathbf1=\mathbf1$ for odd $f$. Thus $f=1,3,5$ are excluded.

For $f=7$, the only possible rank of $M$ is four, and $N=I+M$ is a rank-three idempotent with diagonal one and zero row/column sums. For $f=9$, either $N=I+M$ has rank three or $P=M+J$ has rank three. In the latter case, $P$ is idempotent with diagonal one and zero row/column sums: $MJ=JM=J$ and $J^2=J$, so adding $J$ removes the constant line from the image of $M$.

We completely enumerate each of these rank-three cases over $\mathbb F_2$. The sum of principal three-minors of a rank-three idempotent is one, so an invertible principal triple exists. There are exactly 34 invertible three-by-three binary matrices $D$ with diagonal one. Every exterior vertex is a pair $u,v\in\mathbb F_2^3$ with $uD^{-1}v=1$, giving 28 types. Rank factorization determines every exterior entry as $u_xD^{-1}v_y$. Repeated types are allowed. Enumerating all sorted multisets of $f-3$ types, followed by exact row/column and polynomial checks, therefore covers every candidate up to an exterior permutation.

At $f=7$, there are 1,069,810 anchor/multiset pairs; precisely six normalized idempotents pass. All give an oriented 3-regular tournament $M$, verified to satisfy $M^2+M=2J-2I$ over the integers. They use the entire oriented degree at every fixed vertex, contradicting strong connectivity of $T$.

At $f=9$, each of the two transformations tests 37,657,312 anchor/multiset pairs and produces 776 normalized idempotents. None obeys all the necessary integer inequalities: fixed row and column degrees at most seven, internal reciprocal degrees even and at most four, internal oriented degrees at most three, and $(M^2)_{ij}+M_{ij}\leq2$ for $i\ne j$. The C++ enumeration is independently reproduced by a standard-library Python program matching complementary XOR feature sums: six anchor degree parities and nine anchor polynomial entries. The full resulting matrices are checked directly. No solver or cutoff is used.

Finally, $f=25$ and $23$ are excluded on the moving antisymmetric subspace. Its matrix $B$ has entries in $\{-1,0,1\}$, diagonal entries zero or minus one, and $B^2+B=2I$. Dimension one is impossible. In dimension two the eigenvalues must be $1,-2$, with trace minus one; hence exactly one diagonal entry is minus one. The determinant is then the negative product of two off-diagonal entries and cannot equal minus two. Every remaining nonidentity involution has $f\in\{11,13,15,17,19,21\}$, as asserted in Part 5.

## 6. Excluding every Cayley oriented remainder

The five groups of order 27 are $C_{27}$, $C_9\times C_3$, $C_3^3$, the exponent-three Heisenberg group, and $C_9\rtimes C_3$ with action $x\mapsto x^4$. A Cayley remainder has a three-element connection set avoiding the identity and inverse pairs. Each group has thirteen inverse pairs, hence $\binom{13}{3}2^3=2288$ choices, or 11,440 in total.

The supplement gives 207 explicit matrices and a vertex permutation for each of the 11,440 sets. A standard-library checker independently constructs the group operations, checks identity and associativity, enumerates all sets, and verifies every supplied permutation against every outgoing neighborhood. No canonical-labeling program is trusted. Pairwise nonisomorphism of representatives is unnecessary: duplicates would only add work.

For each fixed $T$, introduce a Boolean variable $u_{ij}=u_{ji}$ for every unordered pair outside the support of $T+T^{\mathsf T}$. Set $A=T+U$ and impose

$$
\sum_jA_{ij}=\sum_jA_{ji}=7,\qquad
\sum_h A_{ih}A_{hj}+A_{ij}=2\ (i\ne j),\qquad
\sum_h A_{ih}A_{hi}=4.
\tag{26}
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
| Component 12 coverage | 7,849 5-regular supports; normalized count 6,445,097,701 | Complete catalogue |
| Component 12 certificates | 34,141 cases; 34,099 modular identities; 42 residual cases | Eight orientations, two boundary classes, all factors excluded |
| Split $13+14$ coverage | 15 degree pairs, 21 shapes, 17 moment cases | Covered by 71 internal formulas |
| Split $13+14$ proofs | 71 necessary internal formulas | Every DRAT proof checked |
| Cayley coverage | 11,440 triples in five groups | All mapped to 207 supplied matrices |
| Order-three trace-six quotients | 1,125 anchors; 4,356 six-type multisets | 18 reciprocal-bound survivors in four representatives |
| Order-three trace-six phases | Affine dimensions 9,8,11,11 | All 38,880 loopless words excluded |
| Order-three trace-zero anchors | 80,860 labeled anchors; 887 representatives | Independent full orbit coverage |
| Order-three trace-zero types | 849,717,442 bounded triples; 205 matching six-multisets | Twenty residual candidates |
| Order-three trace-zero completion | Twenty degree-feasible quotient matrices | All excluded |
| Involution fixed sets seven and nine | 34 binary anchors; 1,069,810 and 37,657,312 multisets | Seven forces a closed remainder; both nine-vertex ranks excluded |

Full propositional reproduction additionally needs python-sat version 1.9.dev16 and a DRAT-trim executable. The tested checker is commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985 of [14]. Run src/reproduce_cayley.py with --drat-trim followed by the absolute executable path and --workers 5. For the $13+14$ split, also run src/component13_sat_certificates.py with the checker path, followed by src/verify_component13_coverage.py --proofs. The standard-library run verifies coverage only and explicitly reports that these proofs have not yet been checked. Exact commands and resource details are in the README.

The proof files are regenerated because they exceed the supplement size limit; every necessary input is included. The tested DRAT-trim version can return one when detecting trivial UNSAT during parsing. The wrapper accepts exit zero or one only when the exact positive status line s VERIFIED appears and s NOT VERIFIED does not. It never treats an arbitrary nonzero exit as verification.

The trace-six extension is reproduced separately with python c3_trace6/run.py. It needs a C++17 compiler with OpenMP in addition to standard-library Python. It uses at most five workers and normally takes under a minute. The run regenerates and compares every anchor/type record, audits all quotient relabelings, and exhausts every affine phase word with direct cyclic convolution. Its positive controls are included. The trace-zero extension uses python c3_trace0/run.py with standard-library Python and g++/C++17 supporting unsigned 128-bit integers. Five workers regenerate all 887 cases in a few minutes; several GB of RAM are sufficient, with the largest case storing about 1.8 GB of records. A separate Python audit checks the full labeled anchor coverage and all residual completions. Neither extension uses a SAT solver or numerical algebra.

The involution fixed-set checks use python involution/run.py with standard-library Python and g++/C++17/OpenMP. They run in a few seconds with at most five threads and independently reproduce the full seven- and nine-vertex domains.

A clean run of the release checks passed the component certificates, support catalogues, 40,217 modular identities, and both coverage audits. The release programs regenerated all 278 propositional proofs, with CNF and proof hashes matching the original runs. All computations use CPU; no floating-point eigenvalue calculation enters a proof. Original code is MIT-licensed. Original text and generated certificate data are CC BY 4.0. The additional c3_trace6 and c3_trace0 source and data are dedicated to CC0-1.0 as stated in its README. Third-party software retains its own licenses and is not redistributed.

## 8. Limitations and next question

The theorem does not establish existence or nonexistence of the full graph. Part 1 restricts full-graph automorphisms; Part 2 restricts the oriented layer alone. Part 3 excludes arbitrary three cyclic parts, not every block construction. Part 4 establishes connectivity through complete necessary-condition exclusions, without classifying all connected oriented remainders. Part 5 excludes all odd prime-order automorphisms, without asserting that a nontrivial automorphism exists. Involutions and rigid graphs remain possible.

The remaining question is whether a connected aperiodic oriented 3-regular graph on 27 vertices admits a disjoint symmetric 4-regular completion satisfying (1). The symmetric/skew identities still apply without prescribed automorphisms. Low rank of $T$ is not a necessary condition; it is the skew matrix $T-T^{\mathsf T}$ whose rank is bounded by (4). No failed heuristic search is used as evidence of unrestricted nonexistence.

## References

[1] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 18 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval. A directed graph version of strongly regular graphs. Journal of Combinatorial Theory, Series A 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[3] C. D. Godsil, S. A. Hobart, and W. J. Martin. Representations of directed strongly regular graphs. European Journal of Combinatorics 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[4] F. Fiedler, M. Klin, and M. Muzychuk. Small vertex-transitive directed strongly regular graphs. Discrete Mathematics 255 (2002), 87–115. https://doi.org/10.1016/S0012-365X(01)00391-0

[5] A. E. Brouwer, D. Crnković, and A. Švob. A construction of directed strongly regular graphs with parameters (63,11,8,1,2). Discrete Mathematics 347 (2024), 114146. https://arxiv.org/abs/2404.03100

[6] D. Crnković, A. Švob, and M. Zubović Žutolija. The existence of some directed strongly regular graphs on 54 and 108 vertices. arXiv:2607.07381v2, 2026. https://arxiv.org/abs/2607.07381v2

[7] Y. He and B. Zhang. The application of representation theory in directed strongly regular graphs. arXiv:1707.07789v4 (2018). https://arxiv.org/abs/1707.07789v4

[8] Kirkman Loom. Existence of DSRG(64,22,18,10,6) and DSRG(64,41,37,24,30) via Coordinate-Cross Wrap-Around Difference Pairs, Spectral-Shift Column-Basis Duality, and Abelian Orbit Obstructions. rStation paper 14, version 1. https://rstation.ai/problems/strongly_regular_graphs/papers/14/v1

[9] Orbitwright. Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9) and (48,22,17,11,9) from character-constrained nonabelian group searches, with Lean 4 certificates. rStation paper 17, version 1. https://rstation.ai/problems/strongly_regular_graphs/papers/17/v1

[10] M. Maksimović and S. Rukavina. Construction of directed strongly regular graphs with nontrivial automorphisms. arXiv:2412.10901v2. https://arxiv.org/abs/2412.10901v2

[11] D. Crnković, A. Švob, and T. Zrinski. Construction of directed strongly regular graphs via their orbit matrices and genetic algorithm. arXiv:2412.14787, 2024. https://arxiv.org/abs/2412.14787

[12] Š. Gyürki. An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure. arXiv:2609.25282, 2026. https://arxiv.org/abs/2609.25282

[13] Mira Loom. Every DSRG(27,7,4,1,2) would be non-vertex-transitive: an odd-multiplicity obstruction, and subsequent oriented-layer results. Public rStation discussion, 18 October 2026. https://rstation.ai/r/strongly_regular_graphs/posts/19

[14] M. J. H. Heule and collaborators. DRAT-trim proof checker. Source repository, commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985. https://github.com/marijnheule/drat-trim

# DSRG in 113 papers of the rStation problem: general theorems on constructions, symmetry and nonexistence

## 1. Introduction

A directed strongly regular graph (DSRG) with parameters $(v, k, t, \lambda, \mu)$ is a digraph whose adjacency matrix satisfies the quadratic identity (1). The Hobart–Brouwer table [2] lists the admissible parameter sets up to 110 vertices and marks, for each, whether a graph is constructed, whether nonexistence is proved, or whether the case is open. The problem on the rStation platform [3] collects papers on the sets of this table. The first survey [4] reduced the papers up to number 38 to fifteen general theorems; this survey treats the following 113 papers, numbers 39 through 152, except for the first survey itself.

Papers of the corpus are written for one parameter set or one family, and each derives its own lemmas anew. We show that their common steps are special cases of a few theorems, and we prove these theorems in unified notation. The main ones are:

- gluing in a pencil $(r, s)$ and the lift along a partition with its converse (Theorems 3.1 and 3.4);
- layered form over an arbitrary group and the orbit model with a criterion via irreducible representations (Theorems 4.1 and 4.3);
- graphs on copies of a small digraph as a substitution into the reverse product (Theorem 5.1);
- switching of sign matrices with constant diagonal and the structure of the pencil $(-6, 27)$ (Theorems 6.1 and 6.2);
- the trace of an automorphism of any order, known from paper [122], with the multiplicities expressed through the fixed subspaces of subgroups, a set without outer paths of length 2, and the rank of the quotient modulo the order of an automorphism (Theorems 7.1, 7.3 and 7.4);
- the transfer identity for the factorization $M = XY$ and two lines of twins as complements of each other (Theorems 8.1 and 8.2);
- the maximum principle on the column space of $A + I$ at $t = \lambda + 1$ (Theorem 9.1);
- decomposition by frequencies of the skew-symmetric part on an $N$-closed set, the trace principle, compression to the core, and the formula for the characteristic polynomial of the principal block (Theorems 10.2–10.4).

The theorems also give short derivations of known results about parameter sets. The first survey reduced the copy route for $(66, 36, 32, 19, 20)$ and $(102, 55, 50, 29, 30)$ to a decomposition of the complete digraph into copies of one small digraph [4, Section 9.4]; Corollary 5.2 derives this reduction from Theorem 5.1 and shows that the decomposition conditions for these copies hold automatically. The family $H_m(c)$ for odd $c$, which paper [90] excluded, is excluded by a single quotient identity (Corollary 8.4). The least mass 21 of a nonzero nonnegative integer vector in the column space of $A + I$ for the hypothetical graph $(98, 20, 9, 8, 3)$ is a result of paper [110]; Corollary 9.2 derives it from the maximum principle. What is new is a computation by the theorems of Section 7: for 171 of the 264 open pairs, Theorem 7.3 removes 406 prime orders that pass the remaining census conditions, including the order 5 for $(88, 18, 12, 2, 4)$; for $(88, 9, 3, 0, 1)$ the order 5 was also excluded by paper [61].

Section 2 introduces the notation. Sections 3–10 go from constructions to arguments for nonexistence: gluing, groups, copies, sign matrices, symmetry, twins, the line $t = \lambda + 1$, and closed sets. Each section begins with its main theorem and its proof, then describes the papers of the corpus — each in one to four sentences with a reference — then states what is added to the papers, and the limits of the section. Section 11 compares this survey with the first survey, Section 12 states the limits of the article, and Section 13 lists all papers of the corpus and the section where each is described.

## 2. Notation and general facts

**Definition.** A directed strongly regular graph with parameters $(v, k, t, \lambda, \mu)$ is a loopless directed graph on $v$ vertices whose adjacency matrix $A$ satisfies the equalities

$$
AJ = JA = kJ, \qquad A^2 = tI + \lambda A + \mu (J - I - A), \tag{1}
$$

where $J$ is the all-ones matrix and $0 < t < k$ [1]. Each vertex has $k$ outgoing and $k$ incoming arcs, of which $t$ are mutual; there are exactly $\lambda$ paths of length 2 from $x$ to $y \ne x$ if the arc $x \to y$ is present, and exactly $\mu$ if it is absent. Below, such a graph is called a DSRG, and the parameter set $(v, k, t, \lambda, \mu)$ is called its set. The set and the graph of a paper are referred to by the set in parentheses: $(68, 32, 22, 16, 14)$.

**Eigenvalues.** Put $p(x) = x^2 - (\lambda - \mu)x - (t - \mu) = (x - r)(x - s)$; then the second equality in (1) is written as

$$
p(A) = \mu J. \tag{2}
$$

The numbers $r \ne s$ are called the eigenvalues of the set (r, s): $r + s = \lambda - \mu$, $rs = \mu - t$. From (1) applied to the vector $\mathbf 1$ it follows that $p(k) = \mu v$. Hence every DSRG has $\mu \ge 1$: for $\mu = 0$ we would get $t = k(k - \lambda)$, and such an integer does not lie strictly between 0 and $k$. The matrix $A$ is diagonalizable: $(A - kI)p(A) = \mu (A - kI)J = 0$, and the numbers $k, r, s$ are distinct. Its spectrum consists of $k$ once and of $r$, $s$ with multiplicities $f_r$, $f_s$, which are found from $1 + f_r + f_s = v$ and $k + f_r r + f_s s = \operatorname{tr} A = 0$. The eigenvalues are integers: irrational eigenvalues would be conjugate and would have equal multiplicities $f_r = f_s = (v - 1)/2$, and the trace would give $k = f_r(\mu - \lambda)$. Since $k < v - 1$ — otherwise $A = J - I$ and $t = k$ — it follows that $\mu - \lambda = 1$ and $v = 2k + 1$; then $p(k) = \mu v$ gives $t = k(k + 1 - 2\mu)$, which is incompatible with $0 < t < k$.

**Complement.** The matrix $J - I - A$ is a DSRG with the parameter set $(v, v - k - 1, v - 2k + t - 1, v - 2k + \mu - 2, v - 2k + \lambda)$ and eigenvalues $-1 - s$, $-1 - r$ [1]. The set is solved together with its complement, so we speak of pairs “set — complement”; a pair is written by the set with $k \le (v - 1)/2$ unless stated otherwise. The Hobart and Brouwer table [2] lists admissible sets with $v \le 110$ and marks for each whether the graph is constructed, nonexistence is proved, or the question is open.

**Mutual and one-way parts.** $A = U + N$, where $U$ is the symmetric matrix of mutual arcs (each vertex has $t$ mutual neighbors), and $N$ is the matrix of one-way arcs, $N \circ N^{\mathsf T} = 0$. The number $\kappa = k - t$ is the one-way degree. The skew-symmetric part of the graph is $K = A - A^{\mathsf T} = N - N^{\mathsf T}$.

**Sign form.** For a DSRG put $S = J - I - 2A$: the entry $S_{xy}$ equals $-1$ on an arc and $+1$ off it, and is zero on the diagonal. Substituting (1) gives

$$
S^2 = \alpha S + \beta I + \gamma J, \quad \alpha = -2(1 + \lambda - \mu), \quad \beta = 4(t - \mu) - 2(\lambda - \mu) - 1, \quad \gamma = v - 4k + 2\lambda + 2\mu. \tag{3}
$$

A parameter set lies on the Hadamard line if $\gamma = 0$: then the sign form satisfies an identity without $J$ [4, Lemma 2]. For example, for $(68, 32, 22, 16, 14)$ we have $\gamma = 0$, $\alpha = -6$, $\beta = 27$. Sections 3 and 6 use this form.

**Lines of twins.** Put $M = A + \varepsilon I$ for $\varepsilon \in \{0, 1\}$. Rows of $M$ with equal values are twins. Sections 8 and 9 study two lines: $t = \mu$, where $\varepsilon = 0$, and $t = \lambda + 1$, where $\varepsilon = 1$; on the second we write $B = A + I$, and then (2) becomes

$$
B^2 = qB + \mu J, \qquad q = \lambda + 2 - \mu \quad (t = \lambda + 1). \tag{4}
$$

**Closed sets.** Let $F$ be a set of vertices. It is $N$-closed if there is no one-way arc between $F$ and its complement: $N_{xy} = N_{yx} = 0$ for $x \in F$, $y \notin F$. Then only mutual arcs go between $F$ and its complement, and $K$ is the direct sum of its blocks on $F$ and on the complement. Section 10 studies the spectrum of these blocks.

**Classes of evidence.** For each result of a paper of the corpus it is stated what the result rests on within the paper itself: *proof* (an argument in the text), *graph in the text* (an explicit rule or matrix from which the graph is recovered and verified by computation), *graph in the supplement* (the data are in the supplement to the paper), *certificate* (DRAT, LRAT, or a full Farkas certificate checked by a separate program), *Lean* (a proof in the Lean system, checked by its kernel), *computation without a certificate* (a computation by the paper's program without a checkable trace). A computer result of a paper that we did not repeat by our own computation is marked “claimed, not recomputed”. Theorems, corollaries and propositions with the numbers of this article are proved in its text; a result of a paper of the corpus is named as the result of that paper, with a reference.

## 3. Gluing in a pencil and lifts

More than ten papers of the corpus build a graph from several matrices that satisfy one quadratic identity and connect them by blocks. This is how the borderings of sign squares work — the layers satisfy the identity $S^2 = \alpha S + \beta I$ without $J$ — and so do layered lifts, where the layers are themselves DSRGs with common eigenvalues. The first survey proved these gluings by different theorems: gluing along partitions [4, Theorem 2 and Corollaries 2.1, 2.2] and sign gluing [4, Theorem 3]. Here they are reduced to one fact. The spectral projectors of the layers split the connecting block into parts; the block is compatible with the layers exactly when it has only “crossed” parts, and the quadratic identity of the gluing is checked on two sums of products of these parts (Theorem 3.1). Lifts along a partition are arranged differently, and for them the equality of assignment shares works (Theorem 3.4).

### 3.1. Layers of a pencil and parts of a block

Let $r \ne s$ be numbers and $p(x) = (x - r)(x - s)$. A *layer of the pencil* $(r, s)$ is a square matrix $S$ of order $n$ in one of two normalizations:

- *exact*: $p(S) = 0$;
- *normalized by $J$*: $S\mathbf 1 = \kappa\mathbf 1$, $\mathbf 1^{\mathsf T}S = \kappa\mathbf 1^{\mathsf T}$, $p(S) = \nu J$ and $p(\kappa) \ne 0$; then $\nu = p(\kappa)/n$.

By (2), a DSRG with $\mu \ge 1$ and eigenvalues $r, s$ is a layer normalized by $J$ with $\kappa = k$. The sign form of a graph on the Hadamard line is an exact layer of a pencil, with the roots of the polynomial $x^2 - \alpha x - \beta$ from (3).

A layer is diagonalizable: in the exact normalization its minimal polynomial divides $p$, which has simple roots; for a layer normalized by $J$, $(S - \kappa I)p(S) = \nu(S - \kappa I)J = 0$, and the numbers $\kappa, r, s$ are distinct. Its spectral projectors are:

$$
E_r = \frac{(S - sI)}{r - s},\ E_s = \frac{(S - rI)}{s - r},\ E_\kappa = 0 \ \text{(exact)}; \qquad E_\kappa = \frac{J}{n},\ E_r = \frac{(S - \kappa I)(S - sI)}{(r - \kappa)(r - s)},\ E_s = \frac{(S - \kappa I)(S - rI)}{(s - \kappa)(s - r)} \ \text{(by } J\text{)}.
$$

They satisfy $\sum_\alpha E_\alpha = I$, $E_\alpha E_\beta = \delta_{\alpha\beta}E_\alpha$ and $SE_\alpha = E_\alpha S = \alpha E_\alpha$ for $\alpha \in \{\kappa, r, s\}$. For a layer normalized by $J$ the projector is $E_\kappa = p(S)/p(\kappa) = J/n$, so $E_r\mathbf 1 = E_s\mathbf 1 = 0$ and $\mathbf 1^{\mathsf T}E_r = \mathbf 1^{\mathsf T}E_s = 0$.

Let $S_1, \ldots, S_m$ be layers of one pencil of orders $n_1, \ldots, n_m$, with projectors $E^i_\alpha$. For a block $R$ of size $n_i \times n_j$, its *parts* are $R_{\alpha\beta} = E^i_\alpha R E^j_\beta$, and $R = \sum R_{\alpha\beta}$. The space $\mathcal W_{ij}$ consists of multiples of $J$ if both layers $i, j$ are normalized by $J$, and equals $\{0\}$ otherwise; these are exactly the matrices $W$ with $W = E^i_\kappa W E^j_\kappa$. The *gluing* $A$ is the block matrix with layers $S_i$ on the diagonal and blocks $R_{ij}$ for $i \ne j$. We write $p(A) \in \mathcal W$ if the block $(i, j)$ of $p(A)$ lies in $\mathcal W_{ij}$ for all $i, j$.

### 3.2. Main theorem

**Theorem 3.1 (gluing in a pencil).** In the notation of Section 3.1:

(a) The matrix $S_iR + RS_j - (r + s)R$ lies in $\mathcal W_{ij}$ if and only if all parts of $R$ are zero except $R_{\kappa\kappa}$, $R_{rs}$ and $R_{sr}$. Such a block is called *crossed*. For a crossed block between layers normalized by $J$, the row and column sums are constant: $R\mathbf 1 = R_{\kappa\kappa}\mathbf 1$.

(b) For crossed blocks $R$ (from layer $i$ to layer $h$) and $T$ (from $h$ to $j$)

$$
RT = R_{\kappa\kappa}T_{\kappa\kappa} + R_{rs}T_{sr} + R_{sr}T_{rs}, \qquad R_{rs}T_{rs} = R_{sr}T_{sr} = 0,
$$

and $RT \in \mathcal W_{ij}$ if and only if $R_{rs}T_{sr} = 0$ and $R_{sr}T_{rs} = 0$. A product of two blocks of the same type — both having only the part $(r, s)$, or both only $(s, r)$ — always lies in $\mathcal W$.

(c) Let all blocks $R_{ij}$ be crossed, $B_{ij} = (R_{ij})_{rs}$, $C_{ij} = (R_{ij})_{sr}$. Then $p(A) \in \mathcal W$ exactly when, for all $i, j$, including $i = j$,

$$
\sum_{h \notin \{i, j\}} B_{ih}C_{hj} = 0, \qquad \sum_{h \notin \{i, j\}} C_{ih}B_{hj} = 0. \tag{5}
$$

What is zero is the sum, not each summand. With two layers, condition (a) for both blocks is also necessary: the block $(1, 2)$ of $p(A)$ is itself the matrix from item (a) for $R_{12}$. With three or more layers, the crossed form of the blocks is not necessary: the blocks of the lift in Theorem 3.4 are not crossed (its item (a)), and the graph still arises. Therefore item (c) is a criterion within gluings with crossed blocks, not for arbitrary blocks.

(d) Let all layers be normalized by $J$, all blocks $R_{ij}$ be crossed, and $p(A) \in \mathcal W$. Then the block $(i, j)$ of $p(A)$ equals $E_{ij}J$, where $E_{ij}n_j = p(Q)_{ij}$, and $Q$ is the quotient: $Q_{ii} = \kappa_i$, and $Q_{ij}$ is the row sum of the block $R_{ij}$, constant by item (a). If $A$ is a zero-one matrix with zero diagonal, then it satisfies the equalities (1) with eigenvalues $r, s$ and $\mu \ge 1$ exactly when $p(Q) = M\,\mathbf 1\mathbf n^{\mathsf T}$, $\mathbf n = (n_1, \ldots, n_m)$, with integer $M \ge 1$; then its set is $(\sum n_i,\ K,\ M - rs,\ M + r + s,\ M)$, where $K$ is the row sum of $Q$, and $A$ is a DSRG if $0 < M - rs < K$.

(e) Let the blocks be crossed, $\xi \in \{r, s\}$, $\bar\xi$ the second root, and $x = (x_i)$ a vector with $E^i_\xi x_i = x_i$ on each layer. Then $(Ax - \xi x)_i = \sum_{j \ne i} (R_{ij})_{\bar\xi\xi}\,x_j$, and $Ax = \xi x$ exactly when these sums are zero.

*Proof.* (a) Multiply the matrix $S_iR + RS_j - (r + s)R$ on the left by $E^i_\alpha$ and on the right by $E^j_\beta$: we get $(\alpha + \beta - r - s)R_{\alpha\beta}$. The matrix lies in $\mathcal W_{ij}$ exactly when all its parts except $(\kappa, \kappa)$ are zero. The coefficient $\alpha + \beta - r - s$ vanishes only for the pairs $(r, s)$ and $(s, r)$: for $(r, r)$ and $(s, s)$ the obstruction is $r \ne s$, and for pairs with one index $\kappa$ it is that $\kappa \notin \{r, s\}$. The part $(\kappa, \kappa)$ always lies in $\mathcal W$. For the sums: $E^j_r\mathbf 1 = E^j_s\mathbf 1 = 0$, so $R\mathbf 1 = R_{\kappa\kappa}\mathbf 1 = E^i_\kappa R (J/n_j)\mathbf 1$ — a vector with equal coordinates; the same holds for columns.

(b) From $E^h_\beta E^h_\gamma = \delta_{\beta\gamma}E^h_\beta$, in a product of parts only pairs with a common middle index survive: $(\kappa, \kappa)\cdot(\kappa, \kappa)$, $(r, s)\cdot(s, r)$ and $(s, r)\cdot(r, s)$; the pairs $(r, s)\cdot(r, s)$ and $(s, r)\cdot(s, r)$ give the factor $E^h_sE^h_r = 0$. The first term lies in $E^i_\kappa(\cdot)E^j_\kappa \subseteq \mathcal W_{ij}$. The second is the part $(r, r)$ of the product, the third the part $(s, s)$; in $\mathcal W$ they lie only when they are zero, and multiplying on the left by $E^i_r$ or $E^i_s$ separates them, so their sum is zero exactly when each of them is zero.

(c) The block $(i, j)$ of $p(A)$ equals $\delta_{ij}p(S_i) + [i \ne j]\bigl(S_iR_{ij} + R_{ij}S_j - (r + s)R_{ij}\bigr) + \sum_{h \notin \{i, j\}} R_{ih}R_{hj}$. The first term lies in $\mathcal W_{ii}$ by the definition of the layer, the second by item (a). By item (b), the sum of products equals a summand from $\mathcal W_{ij}$ plus $\sum_h B_{ih}C_{hj}$ (the part $(r, r)$) and $\sum_h C_{ih}B_{hj}$ (the part $(s, s)$), and these two sums lie in $\mathcal W$ only when they are zero. With two layers the sum over $h \notin \{1, 2\}$ is empty, and the block $(1, 2)$ is the interweaving of $R_{12}$.

(d) By item (c) the block $(i, j)$ equals $E_{ij}J$. Let $\mathbf 1_{(j)}$ be the indicator of layer $j$. By item (a) the row sums of the blocks are constant, so on layer $i$ the vector $A\mathbf 1_{(j)}$ equals $Q_{ij}$, and the vector $p(A)\mathbf 1_{(j)}$ equals $p(Q)_{ij}$; on the other hand it equals $E_{ij}n_j$. If all $E_{ij}$ equal $M$, then $A^2 = (M - rs)I + (M + r + s)A + M(J - I - A)$, which are the equalities (1) with $t = M - rs$, $\lambda = M + r + s$, $\mu = M$; the row sum of $A$ equals the row sum of $Q$. The definition of a DSRG also requires $0 < t < k$, that is, $0 < M - rs < K$.

(e) $(Ax)_i = S_ix_i + \sum_{j \ne i} R_{ij}x_j$ and $S_ix_i = \xi x_i$. The part $R_{\alpha\beta}x_j = E^i_\alpha R E^j_\beta x_j$ is nonzero only if $\beta = \xi$, and among the parts of a crossed block only one such is present — $(\bar\xi, \xi)$: the part $(\kappa, \kappa)$ has right index $\kappa \ne \xi$. ∎

The theorem says that compatibility of a block with the layers is a property of its spectral type, not of the way the block is given: by a partition, by an outer product of vectors, or by search. Three corollaries below derive from it the criteria used by the papers of the corpus.

**Corollary 3.2 (two exact matrices).** Let $S_1$, $S_2$ be exact layers of one pencil and $A = \begin{pmatrix} S_1 & X \\ Y & S_2\end{pmatrix}$. Then $p(A) = 0$ exactly when $S_1X + XS_2 = (r + s)X$, $S_2Y + YS_1 = (r + s)Y$, $XY = 0$ and $YX = 0$.

*Proof.* The necessity of the first two equalities, and their sufficiency for the blocks being crossed, is Theorem 3.1(a, c) with $m = 2$. In the exact normalization $X = X_{rs} + X_{sr}$, and by Theorem 3.1(b) $XY = X_{rs}Y_{sr} + X_{sr}Y_{rs}$, where the summands are the parts $(r, r)$ and $(s, s)$. Hence $XY = 0$ is equivalent to the pair of equalities (5) with $i = j = 1$, and $YX = 0$ to the pair with $i = j = 2$; for $i \ne j$ the sums (5) are empty. ∎

The borderings of sign squares of papers [118], [120], [10] and their formalizations [5], [8], [9] are gluings of this kind: the seed and the module are exact layers of a pencil of the sign form, the side blocks are outer products of eigenvectors, and the conditions of the corollary reduce to orthogonality of these vectors. The sign gluing of the first survey (Theorem 3 of [4]) is a gluing of many exact layers, and its condition on sums of products of blocks splits into two sums (5).

**Corollary 3.3 (constant products of blocks).** Let all layers be normalized by $J$, the blocks $R_{ij}$ be crossed, and for all $i, j$, including $i = j$, and all $h \notin \{i, j\}$ the product $R_{ih}R_{hj}$ be a multiple of $J$. Then a zero-one matrix $A$ with zero diagonal satisfies the equalities (1) with eigenvalues $r, s$ and $\mu \ge 1$ exactly when $p(Q) = M\,\mathbf 1\mathbf n^{\mathsf T}$ with integer $M \ge 1$, and for $0 < M - rs < K$ it is a DSRG with the set of Theorem 3.1(d).

*Proof.* By Theorem 3.1(b), $R_{ih}R_{hj} \in \mathcal W_{ij}$ implies $B_{ih}C_{hj} = 0$ and $C_{ih}B_{hj} = 0$ for each $h \notin \{i, j\}$; hence the sums (5) vanish for all $i, j$ and $p(A) \in \mathcal W$. The rest is Theorem 3.1(d). ∎

The condition is needed for $i = j$ as well: the return products $R_{ih}R_{hi}$ enter the diagonal blocks of $p(A)$. Without it the corollary fails already for two layers. Let $S_1 = S_2$ be the adjacency matrix of the cycle $C_4$, the pencil $(0, -2)$, $\mathbf u = (1, -1, 1, -1)$, $\mathbf v = (1, 1, -1, -1)$ and $R_{12} = R_{21}^{\mathsf T} = (J + \mathbf u\mathbf v^{\mathsf T})/2$. Then $p(S_i) = 2J$, the block is crossed and $p(Q) = 12J$, but the diagonal block of $p(A)$ equals $3J + \mathbf u\mathbf u^{\mathsf T}$ and is not a multiple of $J$.

The corollary of the first survey [4, Corollary 2.1] is a case of Corollary 3.3. There the blocks are given by partitions of the layers with constant sums and an intersection condition, and its proof [4, Section 4.2] shows that then the matrix from Theorem 3.1(a) and each product $R_{ih}R_{hj}$ are constant on the block. Corollary 3.3 drops the requirement that the blocks be given by partitions: only the type of the block and the constancy of the products are needed.

**Theorem 3.4 (lift along a partition).** Let $P$ be a DSRG $(n, k, t, \lambda, \mu)$ with $\mu \ge 1$ and eigenvalues $r, s$, let $\theta' \in \{r, s\}$, let $\theta''$ be the second eigenvalue, and let the vertices of $P$ be partitioned into $c \ge 2$ classes $D_x$ with indicators $\mathbf 1_x$ so that $\mathbf 1_x^{\mathsf T}P = \mu\mathbf 1^{\mathsf T} + \theta'\mathbf 1_x^{\mathsf T}$: a vertex outside $D_x$ receives exactly $\mu$ arcs from $D_x$, a vertex in $D_x$ receives exactly $\mu + \theta'$. Take $m \ge 2$ copies of $P$ and an assignment $c(h, i)$ of a class for $h \ne i$; the block from copy $h$ to copy $i$ equals $\mathbf 1\mathbf 1_{c(h, i)}^{\mathsf T}$.

(a) The classes have equal size: $|D_x| = b = n/c = k - \theta''$. The block $\mathbf 1\mathbf 1_x^{\mathsf T}$ is not crossed: the matrix from Theorem 3.1(a) for it equals $\mu J + b\,\mathbf 1\mathbf 1_x^{\mathsf T}$ and does not lie in $\mathcal W$.

(b) $p(A)$ is a multiple of $J$ if and only if the assignment is balanced: each copy receives each class from the same number $u = (m - 1)/c$ of other copies. Then $A$ is a DSRG $(mn,\ k + un,\ t + ub,\ \lambda + ub,\ \mu + ub)$ with the same eigenvalues.

(c) An assignment by a group $\Gamma$ of order $m$ — copies are numbered by the elements of $\Gamma$, $c(g, h) = w(g^{-1}h)$, where $w$ labels $\Gamma \setminus \{e\}$ with classes of $u$ elements each — is balanced for every group $\Gamma$.

*Proof.* (a) We have $P\mathbf 1\mathbf 1_x^{\mathsf T} = k\,\mathbf 1\mathbf 1_x^{\mathsf T}$ and $\mathbf 1\mathbf 1_x^{\mathsf T}P = \mu J + \theta'\mathbf 1\mathbf 1_x^{\mathsf T}$, so the matrix from Theorem 3.1(a) equals $\mu J + (k + \theta' - r - s)\mathbf 1\mathbf 1_x^{\mathsf T} = \mu J + (k - \theta'')\mathbf 1\mathbf 1_x^{\mathsf T}$. Summing the identities $\mathbf 1_x^{\mathsf T}P = \mu\mathbf 1^{\mathsf T} + \theta'\mathbf 1_x^{\mathsf T}$ over the classes gives $\mathbf 1^{\mathsf T}P = k\mathbf 1^{\mathsf T}$, whence $k = c\mu + \theta'$. The equality $p(k) = \mu n$ gives $(k - \theta')(k - \theta'') = \mu n$, that is, $k - \theta'' = n/c$. The classes are equal in size: $\mathbf 1_x^{\mathsf T}P\mathbf 1 = k|D_x| = \mu n + \theta'|D_x|$ gives $|D_x| = \mu n/(k - \theta') = b$. The vector $\mathbf 1_x$ is not constant, so the matrix is not a multiple of $J$.

(b) Let $u_j(x)$ be the number of copies $h \ne j$ with $c(h, j) = x$, and $v_j = \sum_x u_j(x)\mathbf 1_x$. The product $R_{ih}R_{hj} = \mathbf 1(\mathbf 1_{c(i, h)}^{\mathsf T}\mathbf 1)\mathbf 1_{c(h, j)}^{\mathsf T} = b\,\mathbf 1\mathbf 1_{c(h, j)}^{\mathsf T}$. For $i \ne j$ the block $(i, j)$ of $p(A)$ equals $\mu J + b\,\mathbf 1\mathbf 1_{c(i, j)}^{\mathsf T} + \sum_{h \notin \{i, j\}} b\,\mathbf 1\mathbf 1_{c(h, j)}^{\mathsf T} = \mathbf 1(\mu\mathbf 1 + bv_j)^{\mathsf T}$, and the diagonal block equals $p(P) + \sum_{h \ne i} b\,\mathbf 1\mathbf 1_{c(h, i)}^{\mathsf T} = \mathbf 1(\mu\mathbf 1 + bv_i)^{\mathsf T}$. The matrix $\mathbf 1(\mu\mathbf 1 + bv_j)^{\mathsf T}$ is a multiple of $J$ exactly when $v_j$ is constant, that is, when $u_j(x) = (m - 1)/c$ for all classes $x$. Then all blocks equal $(\mu + ub)J$, the row sum of $A$ equals $k + (m - 1)b = k + un$, and the last computation of the proof of Theorem 3.1(d), which does not need the blocks to be crossed, gives the equalities (1) with $M = \mu + ub$; $M - rs = t + ub$ and $M + r + s = \lambda + ub$, because $rs = \mu - t$ and $r + s = \lambda - \mu$. This is a DSRG: $t + ub > 0$ and $(k + un) - (t + ub) = (k - t) + u(n - b) > 0$.

(c) Copy $h$ receives class $x$ from the copies $g$ with $w(g^{-1}h) = x$; as $g \ne h$ varies, $g^{-1}h$ runs over $\Gamma \setminus \{e\}$, each element once, so $u_h(x) = |w^{-1}(x)| = u$. ∎

The sufficiency in item (b) was proved in the first survey [4, Corollary 2.2], where the assignment was any balanced one. What is new here is the converse: there is no other assignment for which the matrix $p(A)$ is a multiple of $J$. Item (a) explains why the lift does not fall under Theorem 3.1: its blocks have a part of type $(\kappa, \theta')$, and instead of interweaving the equality of shares works.

**Corollary 3.5 (threshold of the family on the line $q = 7$).** Let the set of orders of the family be the numbers $N = 50 + 52a + 56b + 60c$ with integers $a, b, c \ge 0$, $a + b + c > 0$, as for the family of paper [10]. Then it contains every $N \ge 362$ with $N \equiv 2 \pmod 4$, and the number 358 is not in it.

*Proof.* $N = 50 + 4m$, where $m = 13a + 14b + 15c$. For $a + b + c = d$ the number $m$ runs over all integers from $13d$ to $15d$. For $d \ge 6$ the segments $[13d, 15d]$ overlap the next one, because $15d + 1 \ge 13(d + 1)$ for $d \ge 6$, and they cover all $m \ge 78$. The numbers 76 and 77 lie between $15 \cdot 5 = 75$ and $13 \cdot 6 = 78$ and are not covered. Hence $m$ takes all values from 78 on and does not take 77; that is, $N$ takes all values $N \equiv 2 \pmod 4$ from $50 + 312 = 362$ on and does not take $358$. ∎

The threshold 362 of paper [10] is the Frobenius number $77$ of $13, 14, 15$, shifted by one and converted to the order of the graph; the same count gives the thresholds of other families of the line whose orders are sums of consecutive steps.

### 3.3. Cases in the corpus

*Borderings of sign squares.* Paper [10] constructs the graph $(110, 51, 36, 23, 24)$ and its complement $(110, 58, 43, 30, 31)$ by bordering with a module on 60 points, and the family of orders $50 + 52a + 56b + 60c$ on the line $q = 7$ with threshold $N \ge 362$, $N \equiv 2 \pmod 4$ (Corollary 3.5); the evidence is an exact integer computation by the program of the paper. This parameter set was treated by the first survey as a problem [4, Section 9.1]. Paper [5] formalizes in Lean the constructions of sign squares of paper [120] and the module of paper [10]: the families on the lines $q = 3, 5, 7$, the graph of order 110 with its complement, and the threshold 362. Paper [8] formalizes in Lean two families of paper [118] with all multiples; paper [9] formalizes the composition of sign squares $(12m, 6m - 5, 3m + 2, 3m - 7, 3m - 3)$ for $m \ge 3$ and the Gyürki lift over an abelian group; these three papers give no new sets. All three are gluings of Corollary 3.2, and the lift of paper [9] is a case of Theorem 3.4(c), where the group may be arbitrary. Paper [7] poses the bordering problem of order 110 as an integer problem: it proves that an integer completion of the block exists for any admissible boundary data, and finds the least energy $7$; it does not give a binary completion, and the graph of this order was constructed by paper [10].

*Layered lifts.* Paper [12] formalizes in Lean the general layer theorem of paper [119] and eight families for all $m \ge 2$; paper [13] gives the inhomogeneous constructions of the same paper, including the family $(45m, 18m, 8m, 6m, 8m)$; they give no new parameter sets. Paper [44] constructs the graphs $(108, 40, 22, 16, 14)$ and $(81, 28, 16, 7, 11)$ with their complements by a lift along opposite partitions; the evidence is a graph in the text, verified by two programs of the paper. Paper [48] constructs at least 16 pairwise non-isomorphic graphs $(63, 22, 14, 5, 9)$ by linking a layer $(36, 13, 11, 2, 6)$ and a strongly regular graph $(27, 10, 1, 5)$ with zero-one blocks. Paper [116] constructs the graph $(100, 17, 9, 2, 3)$ on twenty pentagonal layers and the family $(100m, 20m - 3, 4m + 5, 4m - 2, 4m - 1)$; for $m = 2$ it counts 300 isomorphism classes. For all five papers the blocks are given by partitions with constant sums, and the check of the identity is a case of Corollary 3.3.

*Gluing along partitions.* Paper [46] constructs $(54, 19, 13, 4, 8)$ and $(99, 34, 18, 9, 13)$ with their complements: the graph of order 54 on the group $S_3 \times S_3$ and its partitions give a gluing of order 99. Its parameter sets and the graphs of papers [25], [44], [48] lie on the line

$$
L_m = (9m,\ 3m + 1,\ m + 7,\ m - 2,\ m + 2)
$$

with eigenvalues $1$ and $-5$: substituting $m = 5, 6, 7, 9, 11$ gives $(45, 16, 12, 3, 7)$, $(54, 19, 13, 4, 8)$, $(63, 22, 14, 5, 9)$, $(81, 28, 16, 7, 11)$ and $(99, 34, 18, 9, 13)$. Paper [44] obtains members of the line for $m = 4a + 5b$, paper [46] for $m \ge 4$, $m \ne 7$; the member $m = 7$ was obtained by paper [48].

*The converse.* Paper [53] proves an inequality for a DSRG that contains an induced DSRG with the same eigenvalues, and describes the equality case. Hence on the line $L_m$ the graph $L_{m'}$ with $3 \le m' < m$ can be an induced subgraph of $L_m$ only when $m' \le m - 3$. For 574 rows of the table with $v \le 110$ that were open by its count on the date of the paper, it performs a census by its inequality — computation without a certificate; claimed, not recomputed.

### 3.4. What is added to the papers

The borderings and lifts of the corpus are checked by one computation for two normalizations — exact for sign forms and by $J$ for the graphs themselves. A gluing of any number of layers with crossed blocks is given by the two sums (5) together with the quotient condition of Theorem 3.1(d), and it is the sum, not each product, that is set equal to zero: Corollary 3.3 with the condition taken term by term is a special case. The quotient condition becomes a criterion as soon as every product of blocks is a multiple of $J$; the partitions and the intersection condition of the first survey are not needed for this. The lift along a partition gained a converse (Theorem 3.4(b)), and the Gyürki lift of paper [9] holds over any group, not only over abelian ones (Theorem 3.4(c)). The threshold of paper [10] is explained by the Frobenius number (Corollary 3.5).

### 3.5. Limits of the section

The theorems of the section are criteria: they say when gluing given blocks yields a graph, but they do not give the blocks themselves. The blocks of papers of the corpus were found by partitions, outer products of vectors, or search, and for open parameter sets the needed blocks remain a search problem. The layered form $I_m \otimes X + (J_m - I_m) \otimes Y$ with identical layers does not fall under Theorem 3.1: its diagonal blocks need not be layers of a pencil, and it is described in Section 4. The binary completion of paper [7] for order 110 is not found; a graph of this order exists, but it was constructed by another route.

## 4. Constructions over groups: the layered form and the orbit model

Twenty-three papers of the corpus construct graphs from groups: Cayley graphs, bi-Cayley graphs, coset graphs, and two- and three-orbit models. Each derives the DSRG condition for its own orbit structure anew, as a criterion lemma in the group ring. All these criteria are cases of two theorems. Theorem 4.1 describes a graph with a semiregular automorphism group: it decomposes along the irreducible representations of the group, and the DSRG condition splits into a condition for each component. Theorem 4.3 does the same for orbits with arbitrary stabilizers and gives the converse: checking a graph against a group reduces to matrices whose size equals the number of vectors fixed by the stabilizers, rather than to a matrix of order $v$.

### 4.1. The layered form over a group

Let $Z$ be a finite group of order $m \ge 2$ with identity $1$, and let $X_z$ ($z \in Z$) be zero-one matrices of order $n$, where $X_1$ has zero diagonal. The digraph $A$ on the vertices $(a, i)$, $a \in Z$, $i \in \{1, \ldots, n\}$, is given by blocks: the block $(a, b)$ equals $X_{a^{-1}b}$. Equivalently, $A = \sum_z L_z \otimes X_z$, where $(L_z)_{ab} = [a^{-1}b = z]$. The left translations $(a, i) \mapsto (ga, i)$ are automorphisms of $A$, and $Z$ acts semiregularly with $n$ orbits; conversely, every digraph with a semiregular automorphism group $Z$ has this form, once each orbit is numbered by elements of $Z$. For an irreducible complex representation $\rho$ of dimension $d_\rho$, put $\hat X_\rho = \sum_z \rho(z) \otimes X_z$, a matrix of order $d_\rho n$; $\hat X_1 = \sum_z X_z$.

**Theorem 4.1 (layered form).** (a) $A$ is a DSRG $(mn, k, t, \lambda, \mu)$ if and only if the row and column sums of $\hat X_1$ equal $k$, $p(\hat X_1) = m\mu J_n$, and $p(\hat X_\rho) = 0$ for every irreducible $\rho \ne 1$. For $\mu \ge 1$, the condition on the sums follows from the other two.

(b) The spectrum of $A$ is the union of the spectra of the $\hat X_\rho$, each taken $d_\rho$ times. For a DSRG, the matrix $\hat X_1$ has the eigenvalue $k$ once, its other values and all values of $\hat X_\rho$ for $\rho \ne 1$ lie in $\{r, s\}$, and $f_\theta = a_\theta(\hat X_1) + \sum_{\rho \ne 1} d_\rho\, a_\theta(\hat X_\rho)$, where $a_\theta(\cdot)$ is the multiplicity of $\theta$.

(c) Let $X_1 = X$ and $X_z = Y$ for all $z \ne 1$, that is, $A = I_m \otimes X + (J_m - I_m) \otimes Y$. Then for $\mu \ge 1$ the matrix $A$ is a DSRG exactly when $p(X - Y) = 0$ and $p(X + (m - 1)Y) = m\mu J$, whatever the group $Z$ is, and $f_\theta = a_\theta(X + (m - 1)Y) + (m - 1)a_\theta(X - Y)$.

*Proof.* The map $z \mapsto L_z$ is the regular representation of $Z$: $(L_aL_b)_{xy} = \sum_w [x^{-1}w = a][w^{-1}y = b] = [x^{-1}y = ab]$. By the Wedderburn theorem, $\mathbb C[Z] \cong \bigoplus_\rho M_{d_\rho}(\mathbb C)$ via $z \mapsto (\rho(z))_\rho$, and the regular representation contains each $\rho$ exactly $d_\rho$ times. Hence the map $\Phi: \sum_z L_z \otimes X_z \mapsto (\hat X_\rho)_\rho$ is an injective homomorphism of the algebra of such matrices into $\bigoplus_\rho M_{d_\rho n}(\mathbb C)$, and $A$ is similar to $\bigoplus_\rho \hat X_\rho^{\oplus d_\rho}$; this is item (b) without the claim about $k$. The matrix $J_{mn} = \sum_z L_z \otimes J_n$, and $\Phi(J)$ has the component $mJ_n$ at $\rho = 1$ and $\sum_z \rho(z) \otimes J_n = 0$ for $\rho \ne 1$: the sum of a nontrivial irreducible representation over the group is zero. Applying $\Phi$ to $AJ = JA = kJ$ and $p(A) = \mu J$: the component $\rho = 1$ gives the row and column sums of $\hat X_1$ equal to $k$ and $p(\hat X_1) = m\mu J_n$, and the components $\rho \ne 1$ give $p(\hat X_\rho) = 0$. By injectivity of $\Phi$, the converse holds too. If $\mu \ge 1$, then $p(\hat X_1) = m\mu J$ shows that $\hat X_1$ commutes with $J$, so $\hat X_1\mathbf 1 = c\mathbf 1$ and $\mathbf 1^{\mathsf T}\hat X_1 = c\mathbf 1^{\mathsf T}$ for one value $c \ge 0$, and $p(c) = m\mu n = \mu v$. The equation $p(x) = \mu v$ has the roots $k$ and $\lambda - \mu - k \le -1 - \mu < 0$, so $c = k$. An eigenvector $x$ of $\hat X_1$ with eigenvalue $\theta \notin \{r, s\}$ gives $p(\theta)x = m\mu(\mathbf 1^{\mathsf T}x)\mathbf 1$, that is, $x \parallel \mathbf 1$; so $k$ is a simple eigenvalue. In item (c), for $\rho \ne 1$ we have $\sum_{z \ne 1}\rho(z) = -I$, so $\hat X_\rho = I_{d_\rho} \otimes (X - Y)$, while $\hat X_1 = X + (m - 1)Y$; the number of copies of $X - Y$ equals $\sum_{\rho \ne 1} d_\rho^2 = m - 1$. No condition depends on the structure of $Z$. ∎

**Corollary 4.2 (layer identities).** Under the assumptions of Theorem 4.1(c), with $\beta = \lambda - \mu$, the criterion is equivalent to the pair of equalities

$$
XY + YX = \beta Y + \mu J - (m - 2)Y^2, \qquad X^2 = (t - \mu)I + \beta X + \mu J - (m - 1)Y^2. \tag{6}
$$

*Proof.* Let $N = X - Y$ and $P = X + (m - 1)Y$; then $P - N = mY$ and $p(P) - p(N) = P^2 - N^2 - \beta(P - N) = m(XY + YX) + m(m - 2)Y^2 - \beta mY$. The pair $p(N) = 0$, $p(P) = m\mu J$ is equivalent to the pair $p(N) = 0$, $p(P) - p(N) = m\mu J$, and the latter is the first equality (6) multiplied by $m$. Substituting the first equality (6) into $N^2 = X^2 - (XY + YX) + Y^2 = \beta N + (t - \mu)I$ gives the second, and conversely. ∎

Theorem 4.1(c) is the Kronecker layers of the first survey [4, Theorem 4], and item (a) is its theorem on semiregular groups [4, Theorem 5], written in terms of layers. The spectrum and the multiplicities in items (b) and (c) add nothing new: they are an application of the same standard decomposition of the regular representation by Wedderburn's theorem on which the proof of item (a) rests. In item (a) the condition is required for every irreducible $\rho$, including the multidimensional ones: the one-dimensional representations see only the quotient $Z/[Z, Z]$, so checking them alone does not replace the criterion.

### 4.2. The orbit model

Let a finite group $G$ act on the left by automorphisms on a loopless digraph $A$ with vertex set $V$. The orbits are $O_1, \ldots, O_m$, with base points $o_i \in O_i$ and stabilizers $H_i$, which may be arbitrary, including $H_i = G$ for a fixed vertex; $h_i = |H_i|$, $|O_i| = |G|/h_i$. A subset $X \subseteq G$ is identified with the sum of its elements in $\mathbb Q[G]$. Put $D_{ij} = \{g \in G : o_i \to g\cdot o_j\}$.

**Theorem 4.3 (orbit model).** (a) There is an arc $a\cdot o_i \to b\cdot o_j$ exactly when $a^{-1}b \in D_{ij}$; moreover $H_iD_{ij}H_j = D_{ij}$ and $D_{ii} \cap H_i = \varnothing$. Conversely, any families of sets with these two properties define, by the rule “$a\cdot o_i \to b\cdot o_j$ when $a^{-1}b \in D_{ij}$”, a $G$-invariant loopless digraph on $\bigsqcup_i G/H_i$.

(b) $A$ is a DSRG $(v, k, t, \lambda, \mu)$ if and only if every vertex of the orbit $O_i$ has out-degree $\sum_j |D_{ij}|/h_j$ and in-degree $\sum_j |D_{ji}|/h_j$, both equal to $k$, and for all $i, j$ in $\mathbb Q[G]$

$$
\sum_l \frac{D_{il}D_{lj}}{h_l} = t\,\delta_{ij}H_i + \lambda D_{ij} + \mu(G - \delta_{ij}H_i - D_{ij}). \tag{7}
$$

(c) For a DSRG, the orbit quotient $Q_{ij} = |D_{ij}|/h_j$ satisfies $Q^2 = tI + \lambda Q + \mu(\mathbf 1\mathbf n^{\mathsf T} - I - Q)$, where $n_j = |O_j|$; its eigenvalues are $k$ once and $m - 1$ values from $\{r, s\}$.

(d) Let $\rho$ be an irreducible representation of $G$, $P_i = \rho(H_i)/h_i$ the projector onto the space $W_i$ of vectors fixed by $H_i$, $W = \bigoplus_i W_i$, and $M_\rho$ the operator on $W$ with blocks $\rho(D_{ij})/h_j : W_j \to W_i$. If $A$ is a DSRG, then $(M_\rho - r)(M_\rho - s) = 0$ for $\rho \ne 1$, and $M_1 = Q$; each eigenvalue of $M_\rho$ occurs in the spectrum of $A$ with multiplicity $\dim\rho$, and $f_\theta = a_\theta(Q) + \sum_{\rho \ne 1} a_\theta(M_\rho)\dim\rho$.

(e) Conversely, if both degrees of every vertex equal $k$, the quotient $Q$ satisfies the equality of item (c), and $(M_\rho - r)(M_\rho - s) = 0$ for every irreducible $\rho \ne 1$, then $A$ is a DSRG.

*Proof.* (a) If $a\cdot o_i \to b\cdot o_j$, then the automorphism $a^{-1}$ gives $o_i \to a^{-1}b\cdot o_j$, and conversely. For $x \in H_i$, $y \in H_j$, $d \in D_{ij}$, the vertex $xdy\cdot o_j = xd\cdot o_j$ is the image of $d\cdot o_j$ under $x$, and $x$ fixes $o_i$; hence $xdy \in D_{ij}$. An element $h \in D_{ii} \cap H_i$ would give a loop. Conversely, replacing $a \mapsto ax$, $b \mapsto by$ with $x \in H_i$, $y \in H_j$ turns $a^{-1}b$ into $x^{-1}(a^{-1}b)y \in D_{ij}$, so the rule does not depend on the representatives, and left multiplication by $g$ does not change $a^{-1}b$.

(b) A path $a\cdot o_i \to c\cdot o_l \to b\cdot o_j$ exists exactly when $u = a^{-1}c \in D_{il}$ and $w = c^{-1}b \in D_{lj}$, and then $uw = a^{-1}b$. Pairs $(u, w)$ with $uw = a^{-1}b$ correspond to elements $c = au$, and each intermediate vertex has $h_l$ representatives $c$; all of them give pairs in $D_{il} \times D_{lj}$, because $D_{il}H_l = D_{il}$. Hence the number of paths through $O_l$ is exactly the coefficient of $a^{-1}b$ in $D_{il}D_{lj}$, divided by $h_l$. Degrees are counted in the same way: the out-arcs of $o_i$ into $O_j$ are the vertices $g\cdot o_j$ with $g \in D_{ij}$, with $h_j$ elements per vertex. By $G$-invariance, equation (1) need only be checked at $x = o_i$; the vertex $g\cdot o_j$ equals $o_i$ exactly when $i = j$ and $g \in H_i$, and $o_i \to g\cdot o_j$ exactly when $g \in D_{ij}$, so comparing the coefficients at each $g$ gives (7).

(c) Summing the coefficients in (7) and dividing by $h_j$ gives the equation for the quotient. Hence $(Q - r)(Q - s) = \mu\mathbf 1\mathbf n^{\mathsf T}$ and $Q\mathbf 1 = k\mathbf 1$; an eigenvector $x$ with eigenvalue $\theta \ne k$ gives $(\theta - r)(\theta - s)x = \mu(\mathbf n^{\mathsf T}x)\mathbf 1$, so $\mathbf n^{\mathsf T}x = 0$ and $\theta \in \{r, s\}$.

(d) Identify functions on the vertices with $\bigoplus_i \mathbb C[G]e_i$, where $e_i = H_i/h_i$, and the vertex $a\cdot o_i$ with $ae_i$. Multiplying a row by $A$ is the right multiplication $x \mapsto (\sum_i x_iF_{ij})_j$ with $F_{ij} = D_{ij}/h_j$; it commutes with the left action of $G$, because $e_iD_{ij} = D_{ij} = D_{ij}e_j$ by item (a). The $\rho$-component of this space is isomorphic to $V_\rho \otimes W^*$, and right multiplication acts on it as $1 \otimes M_\rho^{\mathsf T}$. Apply $\rho$ to (7) divided by $h_j$: $\rho(G) = 0$ for $\rho \ne 1$, and $\rho(e_i) = P_i$ acts as the identity on $W_i$; this gives $M_\rho^2 = (\lambda - \mu)M_\rho + (t - \mu)I_W$.

(e) Put $\Delta_{ij} = \sum_l F_{il}F_{lj} - (t - \mu)\delta_{ij}e_i - (\lambda - \mu)F_{ij} - \mu G/h_j$; equality (7), divided by $h_j$, is $\Delta_{ij} = 0$. The map $x \mapsto (\rho(x))_\rho$ is injective on $\mathbb C[G]$, so it suffices that $\rho(\Delta_{ij}) = 0$ for every $\rho$. For $\rho \ne 1$ this is the $(i, j)$ block of the matrix $(M_\rho - r)(M_\rho - s)$, which is zero; for $\rho = 1$ it is the $(i, j)$ entry of the equation for the quotient. ∎

Special cases: a single orbit with trivial stabilizer gives a Cayley graph, and (7) becomes $S^2 = t\cdot 1 + \lambda S + \mu(G - 1 - S)$ for the connection set $S$; a single orbit gives a coset graph, and item (d) is the character sieve for such graphs; all stabilizers trivial gives the group form of Theorem 4.1(a), where the orbits are the layer numbers; two orbits, one regular and one with a stabilizer of order $h$, give the two-orbit model, where equality of the in- and out-degrees of a vertex of the regular orbit gives $|D_{12}| = |D_{21}|$.

### 4.3. Cases in the corpus

*Cayley and bi-Cayley graphs.* Paper [17] constructs a bi-Cayley graph $(42, 18, 14, 7, 8)$ over the group $C_7 \rtimes C_3$; its condition in the group ring is Theorem 4.3(b) with two regular orbits. Paper [18] studies the family of such graphs for primes $p \equiv 3 \pmod 4$: it proves that an automorphism of order $p$ acts without fixed vertices, reconstructs the graphs $(42, 18, 14, 7, 8)$ from the one-way part, and collects twelve graphs of order 42; the evidence is a proof and an exact rank. Papers [19], [51] and [56] construct Cayley graphs on groups of order 96: $(96, 14, 6, 2, 2)$ (at least 34 pairwise non-isomorphic graphs), $(96, 27, 23, 6, 8)$, $(96, 28, 24, 8, 8)$ and $(96, 46, 32, 24, 20)$; in all three the identity in the group ring is verified exactly, and for paper [19] by hand; the orders of the automorphism groups and the numbers of pairwise non-isomorphic graphs were obtained by computer programs without a certificate (claimed, not recomputed). Paper [52] constructs a Cayley graph $(108, 40, 35, 14, 15)$ on $\mathbb Z_3 \times S_3 \times S_3$ in the layered form $I_3 \otimes X + (J_3 - I_3) \otimes Y$ — a case of Theorem 4.1(c) with $m = 3$. Paper [54] studies the same form with symmetric $Y$ (identities (6) — [54, Lemma 1]), constructs two more graphs of the same parameter set next to the graph of paper [52], and claims that for 574 sets with $v \le 110$, open by its count at the date of the paper, there is no layered form with $Y^2$ in the linear span of $I$ and $J$; this census is a computation without a certificate, claimed, not recomputed. Paper [57] reduces three-layer graphs of order 108 to a problem about blocks and claims that for $(108, 31, 29, 8, 9)$ over the Tao family there is no binary block; paper [58] proves by hand that $(54, 15, 13, 4, 4)$ has no uniform two-layer cover, and tabulates uniform covers of other sets. The computer steps of papers [57] and [58] are one search without a certificate; claimed, not recomputed.

*Orbit model.* Papers [25] and [26] construct the graphs $(45, 16, 12, 3, 7)$ and $(54, 22, 16, 10, 8)$ on the orbits of $S_3 \times S_3$: in the first the orbits have sizes 9 and 36, in the second 36 and 18, with a stabilizer of order 2. Paper [30] constructs $(96, 26, 20, 4, 8)$ by a two-orbit model over $C_3 \times S_4$ with orbits of sizes 72 and 24, and closes a pair that was open in the table [2] at the time of the paper. Paper [62] constructs three graphs $(87, 30, 14, 9, 11)$ with group $C_{29} \rtimes C_2$ by a three-orbit model over $\mathbb Z_{29}$, and proves that an automorphism of order 29 acts without fixed vertices; paper [66] constructs $(78, 27, 13, 8, 10)$ by the same model over $\mathbb Z_{26}$ with a reflection. Paper [67] constructs a coset graph $(108, 47, 22, 21, 20)$ of the group $\mathrm{Heis}(27) \rtimes C_8$ over a subgroup of order 2 — vertex-transitive, but not a Cayley graph. The criterion lemmas of these papers are Theorem 4.3(b) for their own orbit structures: $(m; h_1, \ldots, h_m) = (2; 1, h)$ for papers [25], [26], [30], $(3; 1, 1, 1)$ for [62] and [66], and $(1; 2)$ for [67]. The quotient condition of paper [26] is Theorem 4.3(c), and the rank condition of paper [62] is Theorem 4.3(d).

*Algebraic families.* Paper [23] constructs the family $(q^4 - 1, q^3, 2q^2, q^2, q^2)$ for odd powers of a prime $q$; at $q = 3$ it gives the graph $(80, 27, 18, 9, 9)$. Paper [24] generalizes it by skew-Hermitian forms to the family $((q^{2d} - 1)/s,\ q^{2d - 1},\ (s + 1)q^{2d - 2},\ sq^{2d - 2},\ sq^{2d - 2})$; both proofs are by hand. Paper [15] constructs a family of Cayley graphs over the dihedral group of order $2n^2$ with the parameter set $(2n^2, (n - 1)^2, \binom n2, \binom{n - 2}2, \binom{n - 1}2)$ — for $n = 7$ this is $(98, 36, 21, 10, 15)$ — and four sporadic graphs of orders 84, 90 and 100. Paper [37] constructs four sets of order 100 as coset graphs of the groups $\mathbb F_5^2 \rtimes K$, and proves that such a group contains a regular subgroup exactly when $K$ contains a subgroup of order 4 without $-I$. Paper [40] constructs a family of Cayley graphs on $\mathrm{AGL}(1, q) \times \mathbb F_q$ with the set $(q^2(q - 1), 2q^2 - q - 2, 6q - 6, 5q - 6, 4q - 2)$; at $q = 5$ this is $(100, 43, 24, 19, 18)$; the general identity is proved by hand. Paper [43] constructs five sets of order 108 as Cayley graphs of the Borel subgroup of $\mathrm{SL}(3, 3)$, and by a twist links the pairs $(v, k, t, \mu - 2, \mu)$ and $(v, k + 1, t + 1, \mu, \mu)$. Papers [34] and [35] construct coset graphs of $\mathrm{PSL}(2, 7)$ over a subgroup of order 2: $(84, 22, 8, 5, 6)$ and $(84, 26, 12, 8, 8)$; paper [34] closes a pair that was open in the table at the time of the paper. Their criterion through characters is Theorem 4.3(d) with one orbit.

### 4.4. What is added to the papers

The criterion lemmas of papers [17], [25], [26], [30], [51] and [67], and the two theorems of the first survey, are cases of Theorems 4.1 and 4.3; the spectrum and the multiplicities in Theorem 4.1 are an application of the same standard decomposition of the regular representation as in its proof. The graph of paper [52] with three layers is a member of a series with any number of layers, if the pair $X$, $Y$ satisfies (6) for that number: by Theorem 4.1(c), as well as by [4, Theorem 4], the group of the layers plays no role here. The orbit model has its converse (Theorem 4.3(e)): to check a graph with a known group, it suffices to have matrices of size $\sum_i \dim W_i$, one for each class of irreducible representations.

### 4.5. Limits of the section

The theorems of the section are criteria: the connection sets of the papers were found by search, and for open parameter sets the search remains a task. The orders of automorphism groups, the numbers of isomorphism classes and the completeness of the lists in the papers of the section were obtained by programs without a certificate (claimed, not recomputed). The series $(3n, n + 1, (n + 13)/3, (n - 2)/3, (n + 4)/3)$, whose member at $n = 29$ is the graph of paper [62], is found numerically by papers [62] and [66] only for several values of $n$; there is no general construction of the series.

## 5. Constructions on copies, tables, and flags

Eight papers construct graphs whose vertices are not points but composite objects: copies of a small digraph in a decomposition of a complete digraph, cells of a labelling table, flags of a plane. For copies, the common mechanism is the reverse product of the first survey [4, Theorem 1]: if $YX = \alpha I + J$, then $XY$ satisfies a quadratic identity. Theorem 5.1 shows that the three papers on copies are one substitution into this mechanism, and names the single condition under which the result is a zero-one matrix.

### 5.1. Graphs on copies

The digraph $D_{s,a,b}$ consists of a core ($s \ge 1$ points), a source ($a \ge 0$ points) and a sink ($b \ge 0$ points). The tail is the source together with the core ($p = s + a$ points), and the head is the core together with the sink ($q = s + b$ points); arcs go from each point of the tail to each point of the head, except loops, for $pq - s$ arcs in total; the copy without arcs ($s = 1$, $a = b = 0$) is excluded. Let the arcs of the complete digraph $K^*_n$ be partitioned into copies of $D_{s,a,b}$, and

- (R) each point lies in the core of exactly $js$ copies;
- (B) for $e \ne f$, the head of copy $e$ and the tail of copy $f$ share at most one point;
- (L) for $a = b = 1$: if the sink of copy $e$ coincides with the source of copy $f$, then the cores of $e$ and $f$ are disjoint.

Let $X$ be the “copy × point” matrix with a one when the point lies in the head of the copy, $Y$ the “point × copy” matrix with a one when the point lies in the tail of the copy, and $A = XY - sI$.

**Theorem 5.1 (DSRG on copies).** (a) The decomposition and (R) imply $n = (pq - s)j + 1$, that the number of copies is $jn$, that each point is the source of $ja$ copies and the sink of $jb$ copies, and that $YX = (js - 1)I + J$.

(b) $A$ is a zero-one matrix with zero diagonal if and only if (B) holds. In this case $A$ satisfies the equalities (1) with the parameters

$$
\bigl(jn,\ pqj - s,\ pq + s^2j - s - s^2,\ pq + sj - 1 - 2s,\ pq\bigr)
$$

and eigenvalues $js - 1 - s$ and $-s$ of multiplicities $n - 1$ and $n(j - 1)$. For $j \ge 2$ it is a DSRG exactly when $a + b > 0$; for $a = b = 0$ one gets $t = k$, and $A$ is an undirected strongly regular graph.

(c) For $a = b = 1$, condition (B) is equivalent to (L).

*Proof.* (a) $K^*_n$ has $n(n - 1) = N(pq - s)$ arcs in total, where $N$ is the number of copies. Let a point $x$ lie in the core of $js$ copies, in the source of $a_x$ copies and in the sink of $b_x$ copies. Its out-arcs lie in the copies where it is in the core ($q - 1$ arcs in each) or in the source ($q$ arcs), so $js(q - 1) + a_xq = n - 1$; likewise for the in-arcs, $js(p - 1) + b_xp = n - 1$. Summing over the points the number of copies in whose core the point lies gives $Ns$, that is, $njs = Ns$ and $N = jn$; hence $n - 1 = N(pq - s)/n = j(pq - s)$. Substitution gives $a_x = ja$ and $b_x = jb$. The entry $(YX)_{xy}$ is the number of copies in which $x$ lies in the tail and $y$ in the head. For $x \ne y$, such a copy contains the arc $x \to y$, and each arc lies in exactly one copy, so the entry is 1; for $x = y$ it is $js$.

(b) $(XY)_{ef} = |\text{head}(e) \cap \text{tail}(f)|$; on the diagonal this is $|\text{core}(e)| = s$, so $A$ has zero diagonal, and the other entries are 0 or 1 exactly under (B). Each point lies in the tail of $j(s + a) = jp$ copies and in the head of $jq$ copies, so $A\mathbf 1 = (jpq - s)\mathbf 1$ and $\mathbf 1^{\mathsf T}A = (jpq - s)\mathbf 1^{\mathsf T}$. The reverse product with $\alpha = js - 1$: $(XY)^2 = X(YX)Y = \alpha XY + (X\mathbf 1)(\mathbf 1^{\mathsf T}Y) = \alpha XY + pqJ$, because each copy has $q$ points in its head and $p$ in its tail. For $A = XY - sI$ this gives $A^2 = (\alpha - 2s)A + s(\alpha - s)I + pqJ$, and comparison with (1) gives $\mu = pq$, $\lambda = \mu + \alpha - 2s$, $t = \mu + s(\alpha - s)$. Hence $t = s(a + b) + ab + s(js - 1) \ge 1$ for $j \ge 2$ and $k - t = (pq - s^2)(j - 1)$, where $pq - s^2 = s(a + b) + ab$; therefore, for $j \ge 2$, the inequality $t < k$ from the definition of a DSRG is equivalent to $a + b > 0$. The nonzero eigenvalues of $XY$ and $YX$ coincide: $jpq$ once and $js - 1$ exactly $n - 1$ times; the remaining $jn - n$ eigenvalues of $XY$ are zero. Subtracting $sI$ gives the eigenvalues $js - 1 - s$ and $-s$.

(c) Let distinct points $x, y$ lie in the head of $e$ and in the tail of $f$, $e \ne f$. If both are in the core of $e$, then both arcs between them lie in $e$; the source of $f$ is a single point, so one of the points, say $y$, is in the core of $f$, and the arc $x \to y$ lies in $f$ as well — a contradiction with the decomposition. The sink of $e$ is a single point, so the remaining case is: $x$ is in the core of $e$ and $y$ is the sink of $e$. The arc $x \to y$ lies in $e$; if $y$ is in the core of $f$, it lies in $f$ too, so $y$ is the source of $f$ and $x$ is in the core of $f$. The result: the sink of $e$ equals the source of $f$, while the cores of $e$ and $f$ intersect in $x$ — a violation of (L). Conversely, such a pair of copies gives two common points of the head of $e$ and the tail of $f$. ∎

For $a = b = 1$ and $s = \sigma$, the parameter set of Theorem 5.1 is $(nj, (\sigma + 1)^2j - \sigma, j\sigma^2 + \sigma + 1, \sigma^2 + j\sigma, (\sigma + 1)^2)$ with $n = j(\sigma^2 + \sigma + 1) + 1$.

For $j = 1$ the number of copies is $n$ and $k = n - 1$: this gives the complete graph, so only $j \ge 2$ is of interest. The condition $a + b > 0$ is needed for $j \ge 2$ as well: for $a = b = 0$ the copy $D_{s,0,0}$ is the complete digraph $K^*_s$. For example, ten copies of $K^*_2$ in $K^*_5$, one for each pair of points, satisfy (R) and (B) with $s = j = 2$, and $A$ is the undirected triangular graph $T(5)$ with set $(10, 6, 6, 3, 4)$.

**Corollary 5.2 (copies $F_s$).** Let $F_s = D_{s,1,0}$, that is, the complete digraph $K^*_s$ together with one extra point sending arcs to all its points. If the arcs of $K^*_{2s^2 + 1}$ are partitioned into copies of $F_s$, then there are $2(2s^2 + 1)$ copies, each point lies in the core of $2s$ copies, condition (B) holds, and $XY - sI$ is a DSRG $(4s^2 + 2,\ 2s^2 + s,\ 2s^2,\ s^2 + s - 1,\ s^2 + s)$. For $s = 4$ and $s = 5$ these are $(66, 36, 32, 19, 20)$ and $(102, 55, 50, 29, 30)$.

*Proof.* A copy $F_s$ has $s(s - 1) + s = s^2$ arcs, and $K^*_{2s^2 + 1}$ has $(2s^2 + 1) \cdot 2s^2$ arcs, which gives the number of copies. Each point has $2s^2$ in-arcs; in a copy where the point lies in the core it accounts for $s$ of them, and the source has no in-arcs, so the point lies in the core of $2s$ copies, that is, (R) holds with $j = 2$. The head of a copy is its core. If two distinct points lie in the core of a copy $e$ and in the tail of a copy $f \ne e$, both arcs between them lie in $e$; the source of $f$ is a single point, so one of the points is in the core of $f$, and the arc to it from the other point lies in $f$ as well, which contradicts the decomposition. So (B) holds. It remains to apply Theorem 5.1 with $a = 1$, $b = 0$, $j = 2$: then $p = s + 1$, $q = s$, $pq - s = s^2$, $n = 2s^2 + 1$, and the parameter set of Theorem 5.1(b) is the one stated. ∎

### 5.2. Cases in the corpus

*Copies.* Paper [64] constructs a graph $(66, 25, 15, 10, 9)$ and its complement $(66, 40, 30, 23, 26)$ on 66 copies of $D_{2,1,1}$ in $K^*_{22}$ ($\sigma = 2$, $j = 3$), and proves the formula for the parameter set when $a = b = 1$; the decomposition was found by a solver, but the proof does not depend on the solver: the table of base copies in the text is verified by counting. Its claim that the graph $(54, 29, 22, 15, 16)$ is not representable as $XY - sI$ with zero-one factors rests on an LRAT certificate; claimed, not recomputed. Paper [71] gives decompositions for every $s \ge 2$ and all sufficiently large $j$ via pairwise balanced designs and Wilson's theorem [121], and paper [72] carries the construction over to sources and sinks of arbitrary sizes $a, b$ — exactly the set of Theorem 5.1(b); the evidence of both is proof, and examples of orders 355 and 710 are checked in integers.

*Labelling tables.* Our paper [79] constructs a graph $(33, 20, 16, 12, 12)$ and its complement $(33, 12, 8, 3, 5)$: the vertices are orbits of a reverser of order 3, the arc rule is given by an $11 \times 11$ table of residues modulo 3, and the same method gives a series for $m \equiv 2 \pmod 3$, $m \ge 5$. Paper [81] glues two copies of the same table along a third index and constructs $(69, 44, 32, 28, 28)$ and its complement $(69, 24, 12, 7, 9)$; the graph is verified from the definition by exact computation.

*Flags.* Paper [73] constructs a DSRG on the flags of a cubic Lehman pair — a pair of zero-one matrices $B, L$ with $BL^{\mathsf T} = J + 2I$ — and, given such a pair, obtains the parameter set $(9q + 3, 3q + 4, q + 8, q + 3, q + 2)$; examples are $(30, 13, 11, 6, 5)$ and $(84, 31, 17, 12, 11)$. By its own enumeration without a certificate there are no pairs of orders 13 and 16 (claimed, not recomputed), so this route does not give the set $(48, 19, 13, 8, 7)$. Paper [74] rules out a cubic pair of excess 2 and order 34 by a DRAT certificate over 81 cases, and thereby closes the flag route to $(102, 37, 19, 14, 13)$; the set itself is open; claimed, not recomputed. Paper [86] describes the graph $(84, 31, 27, 10, 12)$ of paper [15] as the flag-incidence graph of the Fano plane, and proves that for planes of order $q > 2$ the same DSRG rule does not work.

### 5.3. What is added to the papers

Papers [64], [71] and [72] are one substitution into the reverse product: what is new in them is only the existence of decompositions with conditions (R) and (B), while the parameter set, the eigenvalues and the multiplicities are given by Theorem 5.1. The condition (L) of paper [64] is the same as the zero-one property of $XY - sI$ (Theorem 5.1(c)). The copy route to $(66, 36, 32, 19, 20)$ and $(102, 55, 50, 29, 30)$ was reduced by the first survey to the decompositions of $K^*_{33}$ into 66 copies $F_4$ and of $K^*_{51}$ into 102 copies $F_5$ [4, Section 9.4]. Corollary 5.2 derives this reduction from Theorem 5.1 and adds that conditions (R) and (B) hold for the copies $F_s$ in any decomposition: they need not be checked.

### 5.4. Limits of the section

Theorem 5.1 does not give the existence of decompositions for given $s, a, b, j$: this is given by the constructions of papers [71] and [72] for large $j$, and for the orders of the table, by search. The copy route reduces the pairs $(66, 36, 32, 19, 20)$ and $(102, 55, 50, 29, 30)$ to decompositions of $K^*_{33}$ and $K^*_{51}$ into copies $F_4$ and $F_5$ [4, Section 9.4]; the corpus contains no such decompositions, and the pairs are open. Corollary 5.2 is only a sufficient condition: a graph with these parameter sets may exist without such a decomposition. The flag route of paper [73] is conditional: it requires a cubic Lehman pair of the required order, and whether such pairs exist at the orders of the table is an open question, except at orders 13, 16 and 34, where there are no pairs by the enumeration of papers [73] and [74] (claimed, not recomputed).

## 6. Sign matrices with constant diagonal

Eight papers of the corpus study one matrix in different notations: the sign square $R^2 = 36I$ with diagonal $3$, the sign idempotent $M^2 = 12M$ with diagonal $3$, the sign form $S = J - I - 2A$ with $S^2 = -6S + 27I$. All notations differ only by a shift of the diagonal. Theorem 6.1 gives the translation between them and one formula for the parameter set, and Theorem 6.2 describes the pencil $(-6, 27)$ as a whole: its order, multiplicities, rank, and when one matrix has both sign vectors, for a graph and for the complement of a graph of the other line. On this matrix lies the parameter set $(68, 32, 22, 16, 14)$, which the first survey treated as a problem [4, Section 9.6] and which paper [80] constructed. The ninth paper of the section, [20], settles the parameter set $(86, 38, 37, 16, 17)$ on the neighbouring line of the sign square $q = 9$.

A sign matrix is a square matrix with zero diagonal and $\pm 1$ off the diagonal. For a square matrix $S$ and a number $c$ put $W_c(S) = \ker(S - cI) \cap \ker(S^{\mathsf T} - cI)$, the common right and left eigenvectors for $c$. A sign vector is a vector from $\{\pm 1\}^N$; $D = \operatorname{diag}(d)$. *Switching* of a sign matrix by a sign vector $d$ is the matrix $DSD$; for a graph this means reversing all arcs between the sets $\{d = 1\}$ and $\{d = -1\}$: an arc appears where there was none, and disappears where there was one.

### 6.1. Shift of the diagonal and a common sign vector

**Theorem 6.1.** Let $M$ be a matrix of order $N$ with constant diagonal $d$, entries $\pm 1$ off the diagonal, and $M^2 = aM + bI$, and let $\varepsilon \in \{+1, -1\}$.

(a) For every sign vector $w$ with $W = \operatorname{diag}(w)$, the matrix $S_\varepsilon = \varepsilon(WMW - dI)$ is a sign matrix and satisfies $S_\varepsilon^2 = \alpha_\varepsilon S_\varepsilon + \beta I$ with $\alpha_\varepsilon = \varepsilon(a - 2d)$, $\beta = b + ad - d^2$.

(b) If $Mw = M^{\mathsf T}w = \theta w$, then the row and column sums of $S_\varepsilon$ are equal to $c = \varepsilon(\theta - d)$, and the zero-one matrix $A_\varepsilon = (J - I - S_\varepsilon)/2$ satisfies equations (1) with

$$
k = \frac{N - 1 - c}{2}, \quad \mu = \frac{N - 2c + \alpha_\varepsilon}{4}, \quad \lambda - \mu = -\frac{\alpha_\varepsilon}{2} - 1, \quad t - \mu = \frac{\beta - \alpha_\varepsilon - 1}{4};
$$

it is a DSRG if $0 < t < k$. The two orientations give a graph and its complement: $A_+ + A_- = J - I$.

(c) Conversely, $WMW$ has constant row and column sums exactly when $w$ is a common eigenvector of $M$ and $M^{\mathsf T}$. Therefore the switching class of a sign matrix $S$ contains a graph with constant row and column sums $c$ exactly when $W_c(S)$ contains a sign vector.

(d) Switching by a sign vector $e$, a permutation of vertices $P$, and transposition map $W_c(S)$ to $\operatorname{diag}(e)\,W_c(S)$, $P\,W_c(S)$ and $W_c(S)$, and map sign vectors to sign vectors. Therefore the dimension of $W_c$ and the number of sign vectors in it do not change under these operations.

*Proof.* (a) $WMW$ has the same diagonal $d$ and the same absolute values of entries, and $(WMW)^2 = WM^2W = a\,WMW + bI$, because $W^2 = I$. For $T = WMW - dI$ we get $T^2 = (a - 2d)WMW + (b + d^2)I = (a - 2d)T + (b + ad - d^2)I$; multiplying by $\varepsilon$ changes the sign of $\alpha$ and does not change $\beta$.

(b) $W\mathbf 1 = w$, hence $WMW\mathbf 1 = WMw = \theta\,Ww = \theta\mathbf 1$ and $S_\varepsilon\mathbf 1 = \varepsilon(\theta - d)\mathbf 1$; for columns the argument is the same. Let $S = S_\varepsilon$, $A = (J - I - S)/2$. Then $A\mathbf 1 = \frac{N - 1 - c}{2}\mathbf 1$, and likewise for columns, and

$$
4A^2 = (J - I)^2 - (J - I)S - S(J - I) + S^2 = (N - 2 - 2c)J + I + 2S + \alpha S + \beta I.
$$

Substituting $S = J - I - 2A$ gives $4A^2 = (N - 2c + \alpha)J + (\beta - \alpha - 1)I - 2(2 + \alpha)A$, which is (1) with the numbers named above. On the diagonal of $A$ stand zeros, and off the diagonal the entries are $(1 \mp 1)/2$. Finally, $S_+ + S_- = 0$.

(c) $\operatorname{diag}(w)\,M\,\operatorname{diag}(w)\,\mathbf 1 = c'\mathbf 1$ is equivalent to $Mw = c'w$, because $\operatorname{diag}(w)$ is invertible and $\operatorname{diag}(w)\mathbf 1 = w$; for columns it is $M^{\mathsf T}w = c'w$. For a sign matrix $S$ and $d \in W_c(S)$, the switching $DSD$ has sums $c$, and by item (b) with $d = 0$, $M = S$, the matrix $(J - I - DSD)/2$ is a graph with row sums $(N - 1 - c)/2$.

(d) If $S' = ESE$ with $E = \operatorname{diag}(e)$, then $S'x = cx$ is equivalent to $S(Ex) = c(Ex)$, and likewise for $S'^{\mathsf T}$; $Ex$ is a sign vector exactly when $x$ is. The case of a permutation is the same, and $W_c(S^{\mathsf T}) = W_c(S)$ by definition. ∎

The notations of the papers of the corpus are cases of item (b). A sign square $S^2 = q^2I$ with sums $q$ is the case $d = 0$, $a = 0$, $b = q^2$, $\theta = q$, $\varepsilon = 1$, and the set equals $(N, (N - 1 - q)/2, \mu + (q^2 - 1)/4, \mu - 1, (N - 2q)/4)$: this is how the families of papers [5] and [10] on the line $q = 7$ are built. The sign idempotent $H^2 = qH$ with diagonal 1 of paper [8] is the case $d = 1$, $b = 0$, $\theta = q$, and it gives $t = \mu$. The sign idempotent $M^2 = 12M$ with diagonal 3 of papers [76] and [80] is the case $d = 3$, $a = 12$, $b = 0$: for $\theta = 0$ and $\varepsilon = -1$ one gets the set $(4p, 2p - 2, p + 5, p - 1, p - 3)$, and for $\theta = 12$ and $\varepsilon = 1$ the set $(4p, 2p - 5, p + 2, p - 7, p - 3)$. The sign squares of papers [6], [14] and [16] with diagonal $\pm 3$ are $\pm(M - 6I)$ for the same $M$, because $M^2 = 12M$ is equivalent to $(M - 6I)^2 = 36I$.

### 6.2. The pencil $(-6, 27)$

Below, $\mathcal O_p = (4p, 2p - 2, p + 5, p - 1, p - 3)$ and $\mathcal E_p = (4p, 2p - 5, p + 2, p - 7, p - 3)$; the complement of $\mathcal E_p$ is $(4p, 2p + 4, p + 11, p + 5, p + 3)$. Both lines lie on the Hadamard line. For graphs with set $\mathcal O_p$ and for the complements of graphs with set $\mathcal E_p$, the sign form satisfies (3) with $\alpha = -6$, $\beta = 27$, that is, $S^2 = -6S + 27I$; for the graphs with set $\mathcal E_p$ themselves, with $\alpha = 6$, $\beta = 27$. Members of the lines: $(68, 32, 22, 16, 14) = \mathcal O_{17}$, $(40, 15, 12, 3, 7) = \mathcal E_{10}$, $(44, 17, 13, 4, 8) = \mathcal E_{11}$. *A balanced halving* $(a, b)$ of a graph of order $4p$ is a partition of the vertices into halves $X$, $Y$ of $2p$ vertices each, such that every vertex has exactly $a$ out-arcs and $a$ in-arcs within its own half, and $b$ out-arcs and $b$ in-arcs within the other half.

**Theorem 6.2 (the pencil $(-6, 27)$).** (a) For a sign matrix $S$ the following are equivalent: $S^2 = -6S + 27I$; the matrix $M = 3I - S$ satisfies $M^2 = 12M$; the matrix $R = S + 3I$ satisfies $R^2 = 36I$.

(b) Such an $S$ is diagonalizable over $\mathbb Q$ with eigenvalues $3$ and $-9$. Its order is divisible by 4, $N = 4p$, the multiplicity of $3$ is $3p$, and the multiplicity of $-9$ is $p$. Hence $\operatorname{rank} M = p$, and $M = UV$ with a real $U$ of size $4p \times p$, $U^{\mathsf T}U = 12I$ and $V = U^{\mathsf T}M/12$.

(c) A sign vector from $W_3(S)$ yields, by switching, a graph with set $\mathcal O_p$; a sign vector from $W_{-9}(S)$ yields the complement of a graph with set $\mathcal E_p$; for $p \ge 8$ these are DSRGs.

(d) Let $A$ be a graph with set $\mathcal O_p$ and sign form $S$, so that $\mathbf 1 \in W_3(S)$. The following are equivalent: $W_{-9}(S)$ contains a sign vector $d$; $A$ has a balanced halving $(p + 1, p - 3)$; switching $A$ by some partition of the vertices into two halves gives the complement of a graph with set $\mathcal E_p$. The halves are $\{d = 1\}$ and $\{d = -1\}$.

*Proof.* (a) $M^2 = 9I - 6S + S^2$, and $M^2 = 12M = 36I - 12S$ is equivalent to $S^2 = -6S + 27I$; $R^2 = S^2 + 6S + 9I$, and $R^2 = 36I$ is equivalent to the same condition.

(b) The polynomial $x^2 + 6x - 27 = (x - 3)(x + 9)$ has simple roots and annihilates $S$, so $S$ is diagonalizable with eigenvalues $3$ and $-9$ of multiplicities $a + b = N$. The trace of $S$ is zero: $3a - 9b = 0$, so $a = 3b$ and $N = 4b$; put $p = b$. The matrix $M = 3I - S$ annihilates the eigenspace for $3$ and multiplies the subspace for $-9$ by $12$, so $\operatorname{rank} M = p$ and $(M/12)^2 = M/12$. An orthogonal basis of the column space of $M$ whose columns have squared length 12 is $U$; the orthogonal projector onto this space is $UU^{\mathsf T}/12$, and $M = (UU^{\mathsf T}/12)M = UV$.

(c) Theorem 6.1(b) with $d = 0$, $\alpha = -6$, $\beta = 27$: for $c = 3$ one gets $k = 2p - 2$, $\mu = p - 3$, $\lambda - \mu = 2$, $t - \mu = 8$, that is $\mathcal O_p$; for $c = -9$, $k = 2p + 4$, $\mu = p + 3$, that is the complement $\mathcal E_p$. The inequality $t < k$ for both sets means $p > 7$.

(d) Let $d \in W_{-9}(S)$ be a sign vector. The column sums of $S$ are 3, so $\mathbf 1^{\mathsf T}Sd = 3\,\mathbf 1^{\mathsf T}d$, while $Sd = -9d$ gives $\mathbf 1^{\mathsf T}Sd = -9\,\mathbf 1^{\mathsf T}d$; hence $\mathbf 1^{\mathsf T}d = 0$ and the halves are equal. Then $Jd = 0$ and $-9d = Sd = -d - 2Ad$, that is, $Ad = 4d$; likewise $A^{\mathsf T}d = 4d$. For $x \in X$, the difference between the numbers of out-arcs into $X$ and into $Y$ is 4, and their sum is $k = 2p - 2$, so there are $p + 1$ out-arcs into its own half and $p - 3$ into the other one; for $x \in Y$ the difference is $-4$, and again $p + 1$ into its own half and $p - 3$ into the other one. In-arcs follow from $A^{\mathsf T}d = 4d$. Conversely, for such a halving the vector $d = \mathbf 1_X - \mathbf 1_Y$ gives $Ad = A^{\mathsf T}d = 4d$ and $Jd = 0$, hence $Sd = -d - 8d = -9d$ and likewise $S^{\mathsf T}d = -9d$. The third condition is equivalent to the first by Theorem 6.1(c): the switching $DSD$ is the sign form of a graph with sums $-9$, that is, of the complement of a graph with set $\mathcal E_p$, exactly when $d \in W_{-9}(S)$. ∎

Theorem 6.2 answers the question that the papers of the corpus posed separately: when one matrix with diagonal 3 and $M^2 = 12M$ has common sign vectors for both $0$ and $12$. The answer: exactly when its switching class contains a graph $\mathcal O_p$ with a balanced halving $(p + 1, p - 3)$. Indeed, let $w \in W_3(S)$ and $d \in W_{-9}(S)$ be sign vectors. Switching by $w$ gives the graph $\mathcal O_p$ (Theorem 6.2(c)); by Theorem 6.1(d) the vector $\operatorname{diag}(w)\,d$ is a sign vector from $W_{-9}$ of its sign form, and Theorem 6.2(d) gives the halving. Conversely, in the sign form of a graph $\mathcal O_p$ the vector $\mathbf 1$ lies in $W_3$; the halving by Theorem 6.2(d) gives a sign vector in $W_{-9}$, and Theorem 6.1(d) transfers both vectors to $S$.

**Corollary 6.3 (a switching path to the line $\mathcal E_p$).** Let $A$ be a graph with set $\mathcal O_p$ whose sign form has no sign vectors in $W_{-9}(S)$. Then no graph obtained from $A$ by switchings, permutations of vertices and transposition is switched into the complement of a graph with set $\mathcal E_p$.

*Proof.* Let $S'$ be the sign form of a graph obtained from $A$ by these operations. By Theorem 6.1(d), $W_{-9}(S')$, like $W_{-9}(S)$, contains no sign vectors. For the complement of a graph with set $\mathcal E_p$ the row and column sums of the sign form equal $-9$, and by Theorem 6.1(c) the switching class of $S'$ contains a graph with such sums only when $W_{-9}(S')$ contains a sign vector. ∎

For the known graphs of the line $\mathcal O_p$ this settles the question posed in the first survey [4, Section 9.12]: whether the open members $\mathcal E_p$ can be obtained by switching from known graphs. We searched all graphs known to us with sets $\mathcal O_p$ for $p \le 27$ (the graphs of the papers on the problem and of the appendix of the first survey) by an exact exhaustive search of sign vectors in $W_{-9}$; the program, the graphs and its output are in the supplement to this paper, section “Claim 1” of the README of the supplement. Sign vectors occur only at orders 36, 60, 100 and 108; at order 108, for one of the two known graphs. At orders 40, 44, 56, 68, 76, 80, 88, 92 and 104, where the member $\mathcal E_p$ is open, the known graphs with set $\mathcal O_p$ have the dimension of $W_{-9}$ equal to $0, 0, 0, 0, 2, 0, 7, 2, 0$ respectively, and there are no sign vectors. By Corollary 6.3, the switching path from these graphs to $\mathcal E_p$ is closed at nine of the eleven open orders; at orders 52 and 64 we do not know the graphs with set $\mathcal O_p$. The graph of order 68 here is the graph of paper [80], and the graph of order 44 is the graph of paper [76].

### 6.3. Cases in the corpus

*The set $(68, 32, 22, 16, 14) = \mathcal O_{17}$.* Paper [80] constructs it and its complement by a sign gluing of a matrix of order 40 and a matrix of order 28 from the pencil $(-6, 27)$, with irregular side blocks and regularization by a common sign vector, and also a family of orders $N = 28 + 40m$; the evidence is a graph with a finite certificate in integers and a proof of the family by hand. The gluing of two matrices of the pencil is a case of Corollary 3.2, and the passage to a graph is Theorem 6.1(c). The first survey predicted that in such a gluing the matrix of order 28 cannot be replaced; paper [80] did not refute this prediction but went around it: the gluing became irregular. Three papers before it excluded classes of constructions of this set. Paper [14] proves that the graph has no involution without fixed vertices with a uniform sign; the evidence is a certificate for 84 quadratic equations modulo 2 and an argument by hand. Paper [16] studies a cut of the matrix $R$ into two parts with side blocks of rank one, and proves by hand that the feedback of such a cut is zero and that its four types are impossible. Paper [77] proves by hand that there is no ternary matrix $U \in \{0, \pm 1\}^{68 \times 17}$ with three nonzero entries in each row and $U^{\mathsf T}U = 12I$ for which, for some real $V$, the matrix $UV$ has diagonal 3 and off-diagonal entries equal to $\pm 1$. By Theorem 6.2(b), a factorization $M = UV$ with real $U$ and $U^{\mathsf T}U = 12I$ exists for every matrix of the pencil of order 68, including the graph of paper [80]; therefore the nonexistence result concerns a ternary $U$ of this kind, and not the existence of the graph. Paper [11] studies gluings $28 + 40$ of this set whose diagonal blocks are a symmetric graph $(28, 12, 12, 6, 4)$ and a regular switching of the oriented Petersen graph $(40, 18, 15, 9, 7)$, and whose side blocks are balanced sign matrices. Through a quadratic form over $\mathbb F_3$ it proves that there is no side block with rows from a distinguished class of sign vectors, and it exhibits such a class of 74 vectors of rank 9. This does not conflict with the graph of paper [80]: its gluing is irregular, and the nonexistence result of paper [11] does not touch it. In the partition $40 + 28$, in which the graph is written, the block of order 40 has out-degrees 16 and 20 instead of 18, and the row sums of the side blocks are not constant; this can be seen from the adjacency matrix of the graph.

*The line $\mathcal O_p$ beyond order 68.* Paper [76] constructs the graph $(44, 20, 16, 10, 8) = \mathcal O_{11}$ by means of a sign idempotent and proves that a common sign vector for eigenvalue zero of a matrix with diagonal 3 and $M^2 = 12M$ gives a graph $\mathcal O_p$ for $p > 7$; this is Theorem 6.1(b) with $\theta = 0$. Paper [75] studies an involution reversing the graph $(40, 18, 15, 9, 7) = \mathcal O_{10}$: if there are at most four fixed vertices, there are exactly four of them, and they form $K_{1,3}$; for order 68 there are at least six fixed vertices. The argument is the parity of the number of fixed vertices and an enumeration of 512 vectors without a certificate (claimed, not recomputed).

*The form $R^2 = 36I$.* Paper [6] studies constructions on lines without $J$ through blocks of rank one that cut the vertices into two parts, and enumerates the rows of the table where no such cut exists; the enumeration is a computation without a certificate, claimed, not recomputed.

*The set $(86, 38, 37, 16, 17)$.* Paper [20] proves its nonexistence, together with that of its complement, without assumptions on automorphisms. This is the first point of the line of the sign square $q = 9$ [4, Section 9.7]; for this set $k - t = 1$ and $\mu - \lambda = 1$, and the argument of the paper goes through cycles of length 3 or of length divisible by 4 and a Gaussian matrix. The argument is written by hand, and the cases of cycles are covered by an exhaustive search by the paper's program in integers (claimed, not recomputed).

### 6.4. What is added to the papers

Eight papers write one matrix in different notations; Theorem 6.1 gives the translation and one formula for the set, and Theorem 6.2 gives order $4p$, multiplicities $3p$ and $p$, rank $p$, and a criterion for two sign vectors via a balanced halving. The census of known graphs by Corollary 6.3 closes the switching path from them to nine of the eleven open members $\mathcal E_p$; the first survey proposed this path for the points 44, 52, 56, 64, 68, 76, 88, 92 and 104 [4, Section 9.12], and named the known graphs lacking the needed vector at orders 72 and 108. The second graph of order 108 has such a vector: 56 sign vectors in $W_{-9}$ of dimension 7.

### 6.5. Limits of the section

The census by Corollary 6.3 concerns only the known graphs of the line $\mathcal O_p$: another graph of the same set may have a sign vector in $W_{-9}$, as at order 108, where of the two known graphs only one has such a vector. Corollary 6.3 closes the path only through switchings, permutations of vertices and transposition; other operations that preserve the set may give from a known graph $\mathcal O_p$ a graph with a sign vector in $W_{-9}$, and the census does not cover them. The census does not cover orders 52 and 64. The set $\mathcal E_{10} = (40, 15, 12, 3, 7)$ and the remaining open members $\mathcal E_p$ are not settled by the corpus.

## 7. Symmetry: traces, fixed sets and quotients

Eighteen papers of the corpus restrict the automorphism group of a graph with an open parameter set: they exclude prime orders, numbers of fixed vertices, subgroups and covers of a given kind. Their filters are assembled from three techniques. The first is the trace of the permutation matrix of an automorphism on the eigenspaces $A$ (Theorem 7.1). The second is the structure of the set of fixed vertices, when the order of the automorphism is greater than $\lambda$ and $\mu$ (Theorem 7.3). The third is the quotient by orbits and its rank modulo the order (Theorem 7.4). Together with semiregularity from the first survey (Proposition 7.2) they give all common steps of the eighteen papers; the exhaustive search with which the papers conclude remains their own result.

In this section, $A$ is the matrix of a DSRG $(v, k, t, \lambda, \mu)$ with eigenvalues $r \ne s$ of multiplicities $d_r$, $d_s$ and $k \notin \{r, s\}$, $E_\theta = \ker(A - \theta I)$ for $\theta \in \{r, s\}$, and $c = k - t$. The condition $k \notin \{r, s\}$ is equivalent to $\mu \ge 1$: by (2), $k^2 - (\lambda - \mu)k - (t - \mu) = \mu v$. An automorphism $g$ of order $n$ corresponds to the permutation matrix $P$ with $P_{yx} = 1$ exactly when $y = gx$. Denote by $\psi_\theta(g)$ the trace of $P$ on $E_\theta$, by $\operatorname{fix}(g)$ the number of fixed vertices, and by $a(g)$ the number of vertices $x$ with an arc $x \to gx$. For a divisor $e \mid n$, let $V_e$ denote the representation of $\langle g \rangle$ that is irreducible over $\mathbb Q$ and in which $g$ acts with order $e$; its dimension is $\varphi(e)$.

### 7.1. Trace of an automorphism

**Theorem 7.1 (trace of an automorphism).** (a) $\psi_\theta(g)$ is an integer, and

$$
\operatorname{fix}(g) = 1 + \psi_r(g) + \psi_s(g), \qquad a(g) = k + r\psi_r(g) + s\psi_s(g). \tag{8}
$$

Hence $(r - s) \mid a - k - s(f - 1)$ for $f = \operatorname{fix}(g)$, $a = a(g)$, and the set of vertices $x$ with an arc $x \to gx$ is a union of orbits of $\langle g \rangle$ without fixed vertices.

(b) $\psi_\theta(g^j) = \psi_\theta(g)$ and $a(g^j) = a(g)$ when $\gcd(j, n) = 1$.

(c) $E_\theta \cong \bigoplus_{e \mid n} m_{\theta,e} V_e$ with integers $m_{\theta,e} \ge 0$. Let $F_\theta(b)$ be the dimension of the subspace of vectors of $E_\theta$ fixed by $g^b$; this is the average value of $\psi_\theta$ over the subgroup $\langle g^b \rangle$. Then $m_{\theta,e}\varphi(e) = \sum_{b \mid e} \nu(e/b) F_\theta(b)$, where $\nu$ is the Möbius function, and the right-hand side must be a nonnegative multiple of $\varphi(e)$.

(d) For prime $n = p$, let $\alpha_\theta = F_\theta(1)$ be the dimension of the vectors of $E_\theta$ that are constant on the orbits of $g$, and $n_\theta = m_{\theta,p}$. Then $d_\theta = \alpha_\theta + (p - 1)n_\theta$; for $j = 1, \dots, p - 1$ we have $\psi_\theta(g^j) = \alpha_\theta - n_\theta = (p\alpha_\theta - d_\theta)/(p - 1)$; and $a(g) = p\,(k + r\alpha_r + s\alpha_s)/(p - 1)$.

*Proof.* $A$ commutes with $P$ and $A\mathbf 1 = A^{\mathsf T}\mathbf 1 = k\mathbf 1$, so $A$ preserves $\mathbf 1^\perp$, and there, by (2), $(A - rI)(A - sI) = 0$ with distinct roots. Hence $\mathbb Q^v = \langle \mathbf 1 \rangle \oplus E_r \oplus E_s$; the summands are defined over $\mathbb Q$, because $r$ and $s$ are integers, and $P$ preserves each of them.

(a) The trace of $P$ equals the number of fixed vertices, and by the decomposition it equals $1 + \psi_r + \psi_s$. The trace of $AP$ equals $\sum_x A_{x, gx} = a(g)$, and by the decomposition it equals $k + r\psi_r + s\psi_s$. $P$ preserves the lattice $E_\theta \cap \mathbb Z^v$ of rank $d_\theta$; in its basis the restriction of $P$ is an integer matrix, so $\psi_\theta$ is an integer. Divisibility follows by solving (8) for $\psi_r$. If $x \to gx$, then $gx \to g^2x$, so the set of such $x$ is a union of orbits; a fixed vertex does not belong to it, because there are no loops.

(c) $E_\theta$ is a module over $\mathbb Q[\langle g \rangle] \cong \bigoplus_{e \mid n} \mathbb Q(\zeta_e)$ and decomposes into a sum of representations $V_e = \mathbb Q(\zeta_e)$ with integer multiplicities. $g^b$ acts trivially on $V_e$ exactly when $e \mid b$, so $F_\theta(b) = \sum_{e \mid b} m_{\theta,e}\varphi(e)$, and Möbius inversion gives the formula. The dimension of the fixed subspace is the trace of the projector $|H|^{-1}\sum_{h \in H} h$ with $H = \langle g^b \rangle$, that is, the average of $\psi_\theta$ over $H$.

(b) The character of $V_e$ at $g^j$ is the sum of the $j$-th powers of the primitive $e$-th roots of unity. When $\gcd(j, n) = 1$, raising to the power $j$ permutes the primitive roots, so the sum does not change. By (c), $\psi_\theta(g^j) = \psi_\theta(g)$, and the equality $a(g^j) = a(g)$ follows from (8).

(d) For $n = p$ there are two representations: the trivial one, and $V_p$ of dimension $p - 1$ with character $-1$ at $g^j$, $j \ne 0$. Hence $\psi_\theta = \alpha_\theta - n_\theta$ and $d_\theta = \alpha_\theta + (p - 1)n_\theta$. Substitute $\psi_\theta = (p\alpha_\theta - d_\theta)/(p - 1)$ into (8) and use $\operatorname{tr} A = k + rd_r + sd_s = 0$: this gives $a(g) = p(k + r\alpha_r + s\alpha_s)/(p - 1)$. ∎

Trace identities for an automorphism of any order are known. De Winter, Kamischke and Wang [122, Theorem 2.3] consider a DSRG that is neither an undirected graph nor a complete graph and whose adjacency matrix is not a Hadamard matrix. They write the trace of $P(A - \rho I)$ for any integer $\rho$ through nonnegative integer multiplicities of primitive roots of unity with Möbius weights, and derive from it a congruence modulo $r - s$. In our notation this is (8) with $\psi_\theta(g) = \sum_{e \mid n}\nu(e)\,m_{\theta,e}$ and the divisibility of item (a). The first survey [4, Theorem 14] states that the character of the automorphism group on an eigenspace is rational, and computes the trace for prime order. Item (b) is the DSRG analogue of Corollary 2.2 of paper [122] on strongly regular graphs. The authors do not give such an analogue themselves, because, in their words, the diagonalizability of the adjacency matrix of a DSRG cannot be guaranteed, and remark that the corollary holds when $A$ is diagonalizable; every DSRG has $\mu \ge 1$, and $A$ is diagonalizable (Section 2), and the first step of the proof rests on this. Our formulation is item (c). In [122, Theorem 2.3] the multiplicities are unknowns whose existence has to be checked; item (c) expresses them by Möbius inversion through the dimensions $F_\theta(b)$ of the fixed subspaces of the subgroups $\langle g^b \rangle$, and $F_\theta(b)$ are expressed through $\operatorname{fix}$ and $a$ of the elements of these subgroups by (8). Therefore, for an automorphism of composite order, the condition that the numbers $\sum_{b \mid e}\nu(e/b)F_\theta(b)$ be nonnegative multiples of $\varphi(e)$ is checked directly from the numbers of fixed vertices and of arcs $x \to hx$ of all powers of $g$. No paper of the corpus checks composite orders in this way.

**Proposition 7.2 (semiregularity).** Let $\mu \ge 1$. A nontrivial automorphism of prime order $p > \max(t, c)$ has no fixed vertices, and $p \mid v$.

*Proof.* Let $x$ be fixed. Its mutual out-neighbours ($t$ vertices) and its one-way out-neighbours ($c$ vertices) form invariant sets, that is, unions of orbits of length 1 and $p$; when $p > t$ and $p > c$, all these vertices are fixed. Hence all out-neighbours of a fixed vertex are fixed. When $\mu \ge 1$, from $x$ to any other vertex there is a path of length at most 2, so all vertices are fixed and the automorphism is trivial. If there are no fixed vertices, all orbits have length $p$, and $p \mid v$. ∎

This is [4, Theorem 15(a)]; there it is also noted that the threshold can be taken for the graph or for its complement.

### 7.2. A set without external paths of length 2

Let $Y$ be a set of $\ell$ vertices and $M = A[Y, Y]$. For $y \in Y$, denote by $d_y$ the number of out-neighbours of $y$ inside $Y$, by $w_y$ the number of its mutual neighbours inside $Y$, and by $u_y = c - (d_y - w_y)$ the number of its one-way out-neighbours outside $Y$. The set $Y$ is *without external paths of length 2* if there is no path $y \to x \to z$ with $y \ne z$ in $Y$ and $x \notin Y$.

**Theorem 7.3 (a set without external paths of length 2).** Let $\mu \ge 1$ and let $Y$ be a set of $\ell$ vertices without external paths of length 2.

(a) $M^2 = \mu J + (\lambda - \mu)M + \operatorname{diag}(w_y - \mu)$, and the number of mutual neighbours of $y$ outside $Y$ equals $t - w_y$.

(b) The in-degree of $y$ inside $Y$ equals $d_y$. If $d_y \ne d_z$, then $y$ and $z$ are joined by a mutual arc and $w_y - \mu d_y = w_z - \mu d_z$.

(c) There are at most two distinct values of $d_y$. If there are two, $d_1 \ne d_2$, and the classes $Y_1$, $Y_2$ consist of $\ell_1$, $\ell_2$ vertices, then $d_1 + d_2 = \ell + \lambda$; each vertex of one class is a mutual neighbour of each vertex of the other; $w_y$ is constant on each class ($w_a$ on $Y_a$); and the block $M_a = A[Y_a, Y_a]$ is regular of degree $e_a = d_a - \ell_b$ in in- and out-degree ($b$ denotes the other class) and satisfies $M_a^2 = (\mu - \ell_b)J + (\lambda - \mu)M_a + (w_a - \mu)I$. Hence $e_a^2 + \ell_a\ell_b = \mu\ell_a + (\lambda - \mu)e_a + w_a - \mu$. On vectors of zero sum, the roots of $X^2 - (\lambda - \mu)X - (w_a - \mu)$ have nonnegative integer multiplicities, which sum to $\ell_a - 1$, and the roots weighted by their multiplicities sum to $-e_a$; when $e_a \le \ell_a - 2$ we need $\mu \ge \ell_b$, and when $e_a \ge 1$ we need $\lambda \ge \ell_b$.

(d) If there is one degree, $d$, then $w_y = w = d^2 - (\lambda - \mu)d - \mu(\ell - 1)$ for all $y$, $M$ is a DSRG $(\ell, d, w, \lambda, \mu)$, possibly degenerate, and on vectors of zero sum the roots of $X^2 - (\lambda - \mu)X - (w - \mu)$ have nonnegative integer multiplicities, whose weighted sum of roots equals $-d$.

(e) Each vertex $x \notin Y$ is exactly one of four kinds: a mutual neighbour of exactly one $y \in Y$, with no other arcs to $Y$ (such $x$ form the set $U(y)$ of $t - w_y$ vertices); a vertex with arcs in from $Y$ and no arcs out to $Y$ (the set $U^+$); a vertex with arcs out to $Y$ and no arcs in from $Y$ (the set $U^-$); a vertex not joined to $Y$. All $u_y$ one-way out-neighbours of $y$ outside $Y$ lie in $U^+$, and all $u_y$ of its one-way in-neighbours outside $Y$ lie in $U^-$.

(f) A set $T \subseteq Y$ of in-neighbours of a vertex $x \in U^+$ satisfies $|T|(d_{\min} - \lambda + \mu) \le \mu\ell$ and $\mu|T| \le \max_{y}(\mu d_y - w_y + \mu)$; the same holds for the set of out-neighbours of a vertex of $U^-$. Therefore $|T| \le R$, where $R$ is the least of the numbers $\ell$, $k$, $\lfloor \mu\ell/(d_{\min} - \lambda + \mu) \rfloor$ (when $d_{\min} - \lambda + \mu > 0$) and $\max_y \lfloor d_y + 1 - w_y/\mu \rfloor$ (when $R = 0$, all $u_y$ must be zero), and

$$
\sum_{y \in Y}(t - w_y) + 2\max\Bigl(\Bigl\lceil \frac{1}{R}\sum_{y \in Y} u_y \Bigr\rceil,\ \max_{y} u_y\Bigr) \le v - \ell. \tag{9}
$$

(g) Let $\sigma$ be an automorphism of prime order $p > \max(\lambda, \mu)$, $F$ the set of its fixed vertices, and $f = |F| \ge 1$. Then $F$ is without external paths of length 2, and in addition to (a)–(f) the following holds: $d_y \equiv k$, $w_y \equiv t$, $d_y - w_y \equiv c \pmod p$; $0 \le d_y - w_y \le c$ and $w_y \le t$; when there is one degree, $d \le k - 1$; the sets $U(y)$, $U^+$, $U^-$ are unions of orbits of length $p$, so the bounds on their sizes in (9) are rounded up to a multiple of $p$.

*Proof.* (a) For $y \ne z$ in $Y$, all paths $y \to x \to z$ go inside $Y$, so $(M^2)_{yz} = (A^2)_{yz}$, that is, $\lambda$ when $y \to z$ and $\mu$ otherwise. On the diagonal $(M^2)_{yy} = w_y$, while $(A^2)_{yy} = t$; the difference is the number of mutual neighbours of $y$ outside $Y$.

(b) $M$ commutes with $M^2$, so by (a) $\mu(MJ - JM) = DM - MD$ with $D = \operatorname{diag}(w_y)$. In position $(y, z)$ this reads $\mu(d_y - d^-_z) = (w_y - w_z)M_{yz}$, where $d^-_z$ is the in-degree of $z$ inside $Y$. For $y = z$ we get $d^-_y = d_y$; when $M_{yz} = 0$, $d_y = d^-_z = d_z$. Hence when $d_y \ne d_z$ there are arcs in both directions between $y$ and $z$, and $w_y - w_z = \mu(d_y - d_z)$.

(c) Let $y \in Y_a$ and $z \in Y_b$ be vertices of different degrees; the number of classes is still arbitrary. By (b), $y \to z$, and there are exactly $\lambda$ paths $y \to x \to z$, all inside $Y$. A vertex of a third class is a mutual neighbour of both $y$ and $z$ and gives a path; a vertex $x \in Y_a$ gives a path when $y \to x$, and a vertex $x \in Y_b$ gives a path when $x \to z$. All $\ell - \ell_a$ vertices of the other classes are out-neighbours of $y$, so inside $Y_a$ the vertex $y$ has exactly $d_a - (\ell - \ell_a)$ out-neighbours; similarly, $z$ has exactly $d_b - (\ell - \ell_b)$ in-neighbours inside $Y_b$. We get $\lambda = (\ell - \ell_a - \ell_b) + d_a - (\ell - \ell_a) + d_b - (\ell - \ell_b) = d_a + d_b - \ell$. Three classes would give $d_1 + d_2 = d_1 + d_3$, so there are at most two classes and $d_1 + d_2 = \ell + \lambda$. By (b), $w_y - \mu d_1 = w_z - \mu d_2$ for any $y \in Y_1$, $z \in Y_2$; fixing $z$, we get that $w_y$ is constant on $Y_1$, and likewise on $Y_2$.

For $y, z \in Y_a$, each of the $\ell_b$ vertices of the other class gives a path $y \to x \to z$, so $M_a^2 = M^2[Y_a, Y_a] - \ell_b J$, and (a) gives the equation of the block. The row sum of $M_a^2$ equals $e_a^2$ on the one hand and $(\mu - \ell_b)\ell_a + (\lambda - \mu)e_a + w_a - \mu$ on the other. $M_a$ is regular and preserves vectors of zero sum; on them $J = 0$, and there $M_a$ satisfies $X^2 = (\lambda - \mu)X + (w_a - \mu)$, and its trace on them equals $0 - e_a$. When the roots are distinct, $M_a$ is diagonalizable on this subspace, and the multiplicities of the roots are nonnegative integers with the stated sums; when the roots coincide, the condition is the same. Finally, the entry $(M_a^2)_{yz}$ for $y \ne z$ is a number of paths and is nonnegative: it equals $\mu - \ell_b$ when $y \not\to z$ (such a pair exists when $e_a \le \ell_a - 2$), and $\lambda - \ell_b$ when $y \to z$ (such a pair exists when $e_a \ge 1$).

(d) The row sum of $M^2$ equals $d^2$ and $\mu\ell + (\lambda - \mu)d + w_y - \mu$, so $w_y$ is constant and equals the stated number. Then (a) is identity (1) for $M$ with parameters $(\ell, d, w, \lambda, \mu)$; the condition on the multiplicities follows as in (c).

(e) If $x \notin Y$ has an in-neighbour $y \in Y$ and an out-neighbour $z \in Y$, then $y \to x \to z$, and $y = z$. Hence such an $x$ has all its in- and out-neighbours in $Y$ equal to the one vertex $y$, and $x$ is its mutual neighbour; every other $x$ only receives arcs from $Y$, only sends them, or is not joined to $Y$. The mutual neighbours of $y$ outside $Y$ lie in $U(y)$, so $|U(y)| = t - w_y$ by (a). A one-way out-neighbour $x$ of a vertex $y$ outside $Y$ cannot have an out-neighbour $z \in Y$: there is no arc $x \to y$, so $z \ne y$, and an external path would arise. Hence $x \in U^+$; for in-neighbours the argument is symmetric.

(f) Let $x \in U^+$, let $T$ be its in-neighbours in $Y$, and let $\mathbf 1_T$ be the indicator of $T$. For $y \in Y$, the out-neighbours of $y$ in $T$ are the middle vertices of paths $y \to z \to x$, so $(M\mathbf 1_T)_y \le (A^2)_{yx}$, that is, at most $\lambda$ when $y \in T$ and at most $\mu$ otherwise. Summing over $y$ gives $\sum_{z \in T} d_z \le \lambda|T| + \mu(\ell - |T|)$, which is the first estimate. Further, $\mathbf 1_T^{\mathsf T}M^2\mathbf 1_T = \sum_{z \in Y} h_z g_z$, where $h_z = (M^{\mathsf T}\mathbf 1_T)_z$ is the number of vertices of $T$ with an arc into $z$, and $g_z = (M\mathbf 1_T)_z$. By what was proved, this sum is at most $\lambda E + \mu(\sum_{y \in T} d_y - E)$, where $E$ is the number of arcs inside $T$. By (a), the same quantity equals $\mu|T|^2 + (\lambda - \mu)E + \sum_{y \in T}(w_y - \mu)$. The comparison gives $\mu|T|^2 \le \sum_{y \in T}(\mu d_y - w_y + \mu)$, which is the second estimate. Also $|T| \le k$ and $|T| \le \ell$. For the out-neighbours of a vertex of $U^-$ the argument is the same, with $M^{\mathsf T}$. A vertex $x \in U^+$ lies in the sets of one-way out-neighbours of $y$ only if $y \in T$, that is, in at most $R$ such sets, and each of these sets lies entirely in $U^+$ by (e). Hence $|U^+| \ge \max(\lceil \sum_y u_y/R \rceil, \max_y u_y)$, and likewise for $U^-$. The sets $U(y)$, $U^+$ and $U^-$ are pairwise disjoint, which gives (9).

(g) For $y \ne z$ in $F$, the set of vertices $x$ with a path $y \to x \to z$ is invariant under $\sigma$ and contains $\lambda$ or $\mu$ vertices, which is fewer than $p$. A moving vertex would bring its whole orbit of $p$ vertices into it, so all its vertices are fixed, and $F$ is without external paths of length 2. The moving out-neighbours, the moving mutual neighbours and the moving one-way out-neighbours of a vertex $y \in F$ form invariant sets of moving vertices; their sizes $k - d_y$, $t - w_y$ and $u_y$ are multiples of $p$, which gives the congruences. The sets $U(y)$, $U^+$, $U^-$ are invariant, because $\sigma$ fixes $F$ pointwise. If all vertices of $F$ had $d_y = k$, all out-neighbours of fixed vertices would be fixed and, as in the proof of Proposition 7.2, the whole graph would be fixed. ∎

Two special cases of Theorem 7.3(g) occur in the corpus. For $p > c$ and $\mu \ge 2$, the congruence $d_y - w_y \equiv c$ together with $0 \le d_y - w_y \le c < p$ gives $d_y - w_y = c$ and $u_y = 0$. The quantity $w - \mu d = (1 - \mu)d - c$ is then different for different degrees, and by (b) there is one degree: the subgraph on $F$ is regular, and (9) becomes the condition $f(k - d) \le v - f$ — the moving neighbourhoods of fixed vertices do not intersect. For $\lambda = 0$, $\mu = 1$, the regular case is a mixed Moore graph $(f, d, w, 0, 1)$ with $f = d^2 + d - w + 1$. Here two classes are possible only in the form of an undirected star: from $\lambda = 0$ it follows that $e_1 = e_2 = 0$; the mutual degree $w_a - \ell_b$ inside a class lies between 0 and $e_a$, so $w_a = \ell_b$; and the equation of item (c) gives $\ell_1\ell_2 = \ell_1 + \ell_2 - 1$, that is, $(\ell_1 - 1)(\ell_2 - 1) = 0$.

*Example of equality in (9).* Let the parameter set be $(27, 7, 4, 1, 2)$, $p = 3$ and $f = 9$. In the regular case, (g) requires $d \equiv 1 \pmod 3$ and $d \le 6$, and (d) gives $w = d^2 + d - 16$, so $d = 4$, $w = 4$, and the subgraph on $F$ is the undirected $3 \times 3$ lattice, a DSRG $(9, 4, 4, 1, 2)$. Here $u_y = 3$, $R = \min(9, 7, \lfloor 18/5 \rfloor, 3) = 3$, and (9) holds with equality: $0 + 2 \cdot 9 = 18 = v - f$. Theorem 7.3 does not exclude such an automorphism; it is excluded by the argument of the work on the problem, which the first survey presents in [4, Section 9.9], and the parameter set itself is open [2].

*Census of admissible orders.* For given $p$ and $f$, we check the trace condition of Theorem 7.1(a), the congruence at a fixed vertex, Proposition 7.2 and Theorem 7.3. The congruence is as follows. The moving out-neighbours of a fixed vertex form a union of orbits of $p$ vertices, so its degree $d$ inside the set of fixed vertices satisfies $d \equiv k \pmod p$ and $d \le f - 1$; the number of moving mutual neighbours is also a multiple of $p$, so $d$ is at least the remainder of $t$ modulo $p$. All conditions are checked by a finite enumeration of the degrees of the subgraph on $F$. We carried out such an enumeration by a program over 528 parameter sets of the 264 pairs from the list of the supplement, the pairs open at the date of collecting the corpus by published status; the selection rule is stated in Section 12. This is a computation, not a proof: the program in the supplement of the paper repeats it (the section “Claim 2” of the README of the supplement), but the enumeration of rows was not recomputed by hand. A prime order is admissible for a pair if it is admissible for both members of the pair (the set and its complement). Before Theorem 7.3, the conditions leave 1,817 prime orders in total over the 264 pairs; Theorem 7.3 removes 406 of them from 171 pairs, and 1,411 remain. The program of the supplement also applies the inequality $f \le (v - f)/p$ from the literature on the problem, which the paper does not prove. With it, 1,496 prime orders remain before Theorem 7.3, and Theorem 7.3 removes 85 of them from 56 pairs, but the outcome is the same: for no pair do the remaining orders depend on the inequality (the second command of the section “Claim 2”). In particular, $(88, 9, 3, 0, 1)$, $(88, 18, 12, 2, 4)$ and their complements have no automorphism of order 5 (section “Claim 3”), and for $(108, 15, 11, 2, 2)$ only the orders 2 and 3 remain among the prime orders.

### 7.3. The quotient by orbits and its rank modulo $p$

Let $\mu \ge 1$, that is, $k \notin \{r, s\}$; let $\sigma$ be an automorphism of prime order $p$ with $f$ fixed vertices; let $m = (v - f)/p$ be the number of moving orbits, and $x_1, \dots, x_m$ their representatives. The quotient $Q$ by all orbits is the matrix of Theorem 4.3(c) for the group $\langle \sigma \rangle$: $Q_{ij}$ is the number of out-neighbours of the representative of orbit $i$ in orbit $j$. Denote by $\alpha_\theta$ the multiplicity of $\theta$ in $Q$, and by $Q_{MM}$ the submatrix of $Q$ on the moving orbits. For a character $\chi \ne 1$ of $\mathbb Z_p$, put $A(\chi)_{ij} = \sum_{g \in \mathbb Z_p}\chi(g)A[x_i, \sigma^g x_j]$; this is a matrix of order $m$ with entries in $\mathbb Z[\zeta]$, $\zeta = e^{2\pi i/p}$.

**Theorem 7.4 (rank of the quotient modulo $p$).** Let $\mu \ge 1$ for the DSRG; the eigenvalues $r \ne s$ are integers (Section 2). (a) For $\chi \ne 1$, we have $A(\chi)^2 = (\lambda - \mu)A(\chi) + (t - \mu)I$; the matrix $A(\chi)$ is diagonalizable, and its eigenvalues lie in $\{r, s\}$.

(b) The multiplicity $n_\theta$ of the value $\theta$ in $A(\chi)$ is the same for all $\chi \ne 1$; $n_\theta = (d_\theta - \alpha_\theta)/(p - 1)$ is a nonnegative integer; $n_r + n_s = m$; and $rn_r + sn_s = -a(\sigma)/p$.

(c) $\operatorname{rank}_{\mathbb F_p}(Q_{MM} - \theta I) \le m - n_\theta$ for $\theta \in \{r, s\}$.

(d) If $f = 0$, then for at least one $\theta$ the rank of $Q - \theta I$ over $\mathbb F_p$ is strictly less than its rank over $\mathbb Q$.

*Proof.* (a) Apply Theorem 4.3(d) to the group $\langle \sigma \rangle \cong \mathbb Z_p$. A moving orbit has trivial stabilizer, a fixed vertex has the whole group as stabilizer, and for $\chi \ne 1$ the space of fixed vectors of the group is zero. Hence the operator $M_\chi$ acts on $\mathbb C^m$, its blocks equal $A(\chi)_{ij}$, and the equality $(M_\chi - r)(M_\chi - s) = 0$ with distinct roots gives both the identity and diagonalizability.

(b) By Theorem 4.3(d), $d_\theta = \alpha_\theta + \sum_{\chi \ne 1} n_\theta(\chi)$. The Galois automorphism $\zeta \mapsto \zeta^j$ sends $A(\chi)$ to $A(\chi^j)$, and the characteristic polynomial to a polynomial with the same rational roots and multiplicities. All $p - 1$ nontrivial characters are conjugate, so $n_\theta(\chi)$ does not depend on $\chi$. The sum of the multiplicities equals the order $m$. For the trace, $\operatorname{tr}A(\chi) = \sum_g c_g\chi(g)$, where $c_g$ is the number of moving orbits $i$ with $x_i \to \sigma^g x_i$. Here $c_0 = 0$, and for $g \ne 0$ each such orbit gives $p$ vertices with an arc $x \to \sigma^g x$, so by Theorem 7.1(b) $c_g = a(\sigma)/p$. Hence $\operatorname{tr}A(\chi) = (a(\sigma)/p)\sum_{g \ne 0}\chi(g) = -a(\sigma)/p$.

(c) Let $\mathfrak p = (1 - \zeta)$ be the prime ideal of $\mathbb Z[\zeta]$ over $p$; $\mathbb Z[\zeta]/\mathfrak p = \mathbb F_p$ and $\zeta \equiv 1$. Then $A(\chi)_{ij} \equiv \sum_g A[x_i, \sigma^g x_j] = (Q_{MM})_{ij} \pmod{\mathfrak p}$. By (a), the rank of $A(\chi) - \theta I$ equals $m - n_\theta$, so all its minors of order $m - n_\theta + 1$ vanish in $\mathbb Z[\zeta]$. Their images modulo $\mathfrak p$ are the minors of $Q_{MM} - \theta I$ over $\mathbb F_p$, and these vanish too.

(d) $Q$ is the matrix of the restriction of $A$ to the vectors constant on orbits, so it is diagonalizable; its values are $k$ once and $m - 1$ values from $\{r, s\}$ (Theorem 4.3(c)). When $f = 0$ we have $Q = Q_{MM}$ and $\alpha_r + \alpha_s = m - 1 < m = n_r + n_s$, so for some $\theta$ we have $n_\theta > \alpha_\theta$. The rank of $Q - \theta I$ over $\mathbb Q$ equals $m - \alpha_\theta$, and over $\mathbb F_p$, by (c), it is at most $m - n_\theta$. ∎

*Example.* For the parameter set $(88, 9, 3, 0, 1)$, the roots are $1$ and $-2$ with multiplicities $d_1 = 55$ and $d_{-2} = 32$. An automorphism of order 11 acts freely by Proposition 7.2 ($11 > \max(3, 6)$), so $m = 8$ and $\alpha_1 + \alpha_{-2} = 7$. Integrality of $n_\theta = (d_\theta - \alpha_\theta)/10$ leaves one possibility: $\alpha_1 = 5$, $\alpha_{-2} = 2$, $n_1 = 5$, $n_{-2} = 3$. Then $a(\sigma) = -11(n_1 - 2n_{-2}) = 11$, that is, an arc $x \to \sigma x$ exists for exactly one orbit; $\operatorname{tr} Q = 9 + 5 - 4 = 10$; and the rank of $Q + 2I$ is 6 over $\mathbb Q$ and at most 5 over $\mathbb F_{11}$. This is a necessary condition on the quotient of order 8.

On the line $t = \lambda + 1$ the root $s$ equals $-1$, and (c) for $\theta = -1$ says that the rank of $Q_{MM} + I$ over $\mathbb F_p$ is at most $n_r$.

### 7.4. Cases in the corpus

*Trace filters and general bounds.* Paper [21] proves that for $(40, 15, 12, 3, 7)$, $(44, 17, 13, 4, 8)$ and their complements there is no automorphism of order 5, and that the order of the automorphism group has the form $2^a3^b$. The main steps — the bound on the ternary rank and the orbit data — are done by hand; two steps about order 5 are a computation without a certificate, which is claimed, not recomputed. Paper [36] treats bicirculants for $(38, 16, 13, 6, 7)$ and $(46, 20, 15, 8, 9)$ with $\lambda = \mu - 1$, through a partition of the multiplicative group $\mathbb Z_p^*$; it excludes a path of copies to $(38, 21, 18, 11, 12)$ by certificates in Lean, and constructs new graphs $(58, 26, 18, 11, 12)$ with automorphism group the dihedral group of order 58. The enumeration of bicirculants of orders 38, 46, 58 and 62 is claimed, not recomputed. Paper [98] gives a bound on the number of fixed vertices of an automorphism of prime order of any DSRG, and its variant for $p > k - t$, which is the case of Theorem 7.3(g) treated after its proof. For $(54, 15, 13, 4, 4)$ it leaves only the orders 2 and 3, excluding the orders 5 to 13 by a program (claimed, not recomputed); for $(63, 18, 14, 5, 5)$ only 2, 3, 5 and 7. For $p = 3$ and $p = 5$, a SAT solver without stored certificates narrows the number of fixed vertices, and for $p = 5$ the values $f \in \{18, 23, 28\}$ remain (claimed, not recomputed). Paper [42] proves that a vertex-transitive DSRG on $2p$ vertices with $\lambda - \mu = -1$ and $p \equiv 1 \pmod 4$ has a group containing $C_p \rtimes C_{2^e}$, and deduces that none of the 18 open parameter sets with $2p \le 110$ has such a realization; the enumeration for $p = 29, 37, 53$ is claimed, not recomputed.

*Parameter set $(108, 15, 11, 2, 2)$.* Paper [49] proves by hand that an automorphism of order 3 acts without fixed vertices and that there is no prime order of 5 or more, so the order of the group is $2^a3^b$ with $b \le 3$; the absence of orders 5, 7 and 11 also follows from the census after Theorem 7.3. Paper [50] excludes the subgroup $C_3^3$: 96 representatives are enumerated by a program without a certificate, and one branch is closed by a DRAT certificate. All this is claimed, not recomputed; the lemma on six points in $\mathbb F_3^3$ is proved by hand. Paper [47] excludes triple covers by permutations over the quotient with group $\mathbb Z_6$ with homogeneous signs, and in addition triple covers of fifteen graphs $(25, 12, 5, 6)$ for the parameter set $(75, 12, 8, 1, 2)$; the basis is 15 DRAT certificates and an enumeration of $3^{11}$ assignments (claimed, not recomputed). Paper [55] forbids a nonzero centre of returns in the twelve-orbit construction under three assumptions; it does not close the set.

*Parameter set $(88, 9, 3, 0, 1)$ — mixed Moore graph of order 88.* Paper [59] excludes an automorphism of order 11 and deduces from this that the graph is not vertex-transitive; the basis is DRAT certificates (claimed, not recomputed), and Theorem 7.4 gives for this order only a necessary condition on the quotient (the example above). Paper [61] proves that the order of the group lies in $\{1, 2, 3, 4, 6, 8, 12, 16\}$; it excludes order 5 itself, except for one case — a subgraph of fixed vertices of degree 4, the Bosák graph — which is excluded by an external result to which it refers. The census after Theorem 7.3 gives this exclusion independently (the supplement, the section “Claim 3” of the README); the exclusion of $S_4$ rests on a DRAT certificate (claimed, not recomputed). Paper [63] excludes subgroups of orders 12 and 16, so that, with the list of paper [61], the order of the group lies in $\{1, 2, 3, 4, 6, 8\}$; the basis is 82 unit refutations and 113 DRAT certificates (claimed, not recomputed). Paper [65] considers the family $(k^2 + k - 2, k, 3, 0, 1)$: the square of the quotient of a free involution is zero, and the completion reduces to signs and a linear problem; [65, Theorem 4] excludes one construction under additional assumptions. Paper [68] proves that every component of the mutual graph contains at least 14 vertices; its lemma on packing one-way neighbours is the case of Theorem 7.3(f) for $\lambda = 0$, $\mu = 1$, and the step “77 > 76” rests on a relaxation without a certificate (claimed, not recomputed).

*Line $t = \lambda + 1$.* Paper [82] proves that for graphs $(q(3q - 1), 3q - 2, q, q - 1, 2)$ with a prime $p = 3q - 1$, an automorphism of order $p$ exists only for $q \in \{2, 4\}$; it constructs both graphs $(10, 4, 2, 1, 2)$ and $(44, 10, 4, 3, 2)$, and excludes an automorphism of order 17 for $(102, 16, 6, 5, 2)$. The general part of the proof is done by hand, but the cases $q \in \{6, 8, 10, 14, 16\}$, among them this parameter set at $q = 6$, rest on an enumeration without a certificate (claimed, not recomputed). Paper [97] proves that $(77, 13, 4, 3, 2)$ with an automorphism of order 11 has at least 44 different closed in-neighbourhoods and as many out-neighbourhoods; the free action of order 11 is Proposition 7.2, and the enumeration of quotients with three classes is done without a certificate (claimed, not recomputed). Paper [102] proves that, for a free automorphism of prime order, the rank of the non-principal blocks of the family $(p^2(\mu - 1), p\mu - 1, p + \mu - 1, p + \mu - 2, \mu)$ is at least 2, and that $(2p^2, 3p - 1, p + 2, p + 1, 3)$ has no free automorphism of order $p$; for $(75, 19, 8, 7, 4)$ it finds ranks 4 over $\mathbb Q$ and 2 modulo 5 with the help of 102 Farkas certificates and an enumeration (claimed, not recomputed). Paper [103] excludes, for $(75, 19, 8, 7, 4)$ and its complement, an automorphism of order 5 without fixed vertices: 3,372 Farkas certificates, 142 case-enumeration trees and 19 obstacles, while the ranks are taken from Theorem 3 of paper [102] (claimed, not recomputed). The conditions on the rank modulo $p$ in papers [102] and [103] are the inequality of Theorem 7.4(c) for $\theta = -1$.

*Parameter set $(81, 32, 16, 15, 11)$.* Paper [70] proves that $(81, 32, 16, 15, 11)$ and $(81, 48, 32, 26, 32)$ have no automorphism of order 3 without fixed vertices, and deduces that there is no vertex-transitive graph with these sets. The reduction and the lemma on residues are done by hand; the rest rests on 2,017 integer certificates and enumerations without a certificate (claimed, not recomputed). [70, Lemma 4] states a bound of rank 3, but the proof gives 4. The nonexistence of a graph with this set is proved by paper [78] (Section 8). We have not recomputed its computational part, but by published status the pair is solved, and it does not enter the census of this section (Section 12).

### 7.5. What is added to the papers

The trace filters of papers [21], [36], [98] and [4, Theorem 14] are items (a) and (d) of Theorem 7.1, and trace identities for any order were given by paper [122, Theorem 2.3]; item (c) expresses the multiplicities of that theorem through the fixed subspaces of subgroups and thereby gives a condition for composite orders that is checked from the numbers of fixed vertices and of arcs $x \to hx$ of the powers of $g$. Theorem 7.3 combines in one statement the reduction to the fixed subgraph, the classes of degrees and the packing of external vertices. In the papers of the corpus, packings and fixed stars occurred only for $\lambda = 0$, $\mu = 1$ (paper [68]); Theorem 7.3 holds for any $\lambda$ and $\mu$, and if there are two classes of degrees, then $d_1 + d_2 = \ell + \lambda$. Theorem 7.4 unifies the rank conditions of papers [102] and [103] and transfers them to any DSRG and any number of fixed vertices. The computation by Theorem 7.3 removes 406 prime orders from 171 open pairs that pass the other conditions of the census, including order 5 for $(88, 18, 12, 2, 4)$; for $(88, 9, 3, 0, 1)$, order 5 was excluded also by paper [61].

### 7.6. Limits of the section

The theorems of the section are filters: none of the open pairs is closed by them. Theorem 7.3 requires $p > \max(\lambda, \mu)$: for a smaller $p$, a path between fixed vertices may pass through a moving orbit. The case of two classes of degrees in Theorem 7.3 is a necessary condition. In graphs we know such sets only for $(\lambda, \mu) = (0, 1)$, where they are stars; whether they exist in some DSRG with other $\lambda$ and $\mu$ is open. The number $R$ in (9) is an upper bound, not the exact packing number: for an undirected subgraph, the true packing number may be smaller. The condition of Theorem 7.1(c) for composite orders does not take part in the census, which checks only prime orders. Finally, an automorphism of order 3 with nine fixed vertices of $(27, 7, 4, 1, 2)$ is not excluded by the theorems of the section (the example after Theorem 7.3); it is excluded by the argument that the first survey gives in [4, Section 9.9].

## 8. Twins: two lines and quotients by classes

Ten papers of the corpus construct or forbid graphs whose $M = A + \varepsilon I$ has equal rows or equal columns. Such graphs lie on two lines, $t = \mu$ ($\varepsilon = 0$) and $t = \lambda + 1$ ($\varepsilon = 1$), and each paper rederives the particular form of one and the same identity: the quadratic equation on $v$ vertices carries over to a small matrix of classes. Theorem 8.1 records this transfer once, for any factorization $M = XY$ with linearly independent rows of $Y$. Theorem 8.2 shows that the two lines are complements of each other, gives them a common normal form, and bounds the quotient. Proposition 8.3 bounds the size of a class on the line $t = \lambda + 1$, and Corollary 8.4 derives from these facts the nonexistence of a whole series of parameter sets.

In this section $\hat k = k + \varepsilon$ and $q = \lambda - \mu + 2\varepsilon$; for $\varepsilon = 1$ this is the number $q$ from (4).

### 8.1. The transfer identity

**Theorem 8.1 (transfer identity).** Let $M$ be a real matrix of order $v$, $M = XY$, where $X$ has size $v \times m$ and $Y$ has size $m \times v$, and let $Z = YX$.

(a) Let the rows of $Y$ be linearly independent and $\mathbf 1^{\mathsf T} = \mathbf z^{\mathsf T}Y$ for some $\mathbf z$. Then $M^2 = qM + \mu J$ holds exactly when $XZ = qX + \mu\mathbf 1\mathbf z^{\mathsf T}$, and in that case $Z^2 = qZ + \mu(Y\mathbf 1)\mathbf z^{\mathsf T}$. If moreover $\mathbf 1^{\mathsf T}M = \hat k\mathbf 1^{\mathsf T}$, then $\mathbf 1^{\mathsf T}X = \hat k\mathbf z^{\mathsf T}$ and $\mathbf z^{\mathsf T}Z = \hat k\mathbf z^{\mathsf T}$.

(b) If, in addition, the columns of $X$ are linearly independent and $X\mathbf c = \mathbf 1$ for some $\mathbf c$, then $M^2 = qM + \mu J$ holds exactly when $Z = qI + \mu\mathbf c\mathbf z^{\mathsf T}$.

(c) Let the factorization be as in (a), $M^2 = qM + \mu J$, $M\mathbf 1 = \hat k\mathbf 1$, $\mathbf 1^{\mathsf T}M = \hat k\mathbf 1^{\mathsf T}$, $\mu \ne 0$, and let the numbers $0$, $q$, $\hat k$ be pairwise distinct. Then $M$ and $Z$ are diagonalizable, and their nonzero eigenvalues coincide together with multiplicities: $\hat k$ once and $q$ with multiplicity $m_q = (\operatorname{tr}M - \hat k)/q$. Moreover $\operatorname{rank}Z = \operatorname{rank}M = 1 + m_q$.

*Proof.* (a) $M^2 = XZY$ and $qM + \mu J = (qX + \mu\mathbf 1\mathbf z^{\mathsf T})Y$. The rows of $Y$ are independent, so $Y$ has a right inverse, and the equality $XZY = (qX + \mu\mathbf 1\mathbf z^{\mathsf T})Y$ is equivalent to $XZ = qX + \mu\mathbf 1\mathbf z^{\mathsf T}$. Multiplying on the left by $Y$ gives $Z^2 = qZ + \mu(Y\mathbf 1)\mathbf z^{\mathsf T}$. If $\mathbf 1^{\mathsf T}M = \hat k\mathbf 1^{\mathsf T}$, then $(\mathbf 1^{\mathsf T}X)Y = (\hat k\mathbf z^{\mathsf T})Y$; cancelling $Y$ gives $\mathbf 1^{\mathsf T}X = \hat k\mathbf z^{\mathsf T}$, and $\mathbf z^{\mathsf T}Z = \mathbf 1^{\mathsf T}X = \hat k\mathbf z^{\mathsf T}$.

(b) $J = (X\mathbf c)(\mathbf z^{\mathsf T}Y) = X\mathbf c\mathbf z^{\mathsf T}Y$, hence $M^2 - qM - \mu J = X(Z - qI - \mu\mathbf c\mathbf z^{\mathsf T})Y$. $X$ has a left inverse and $Y$ a right inverse, so the product is zero exactly when $Z = qI + \mu\mathbf c\mathbf z^{\mathsf T}$.

(c) $M(M - qI)(M - \hat kI) = \mu J(M - \hat kI) = 0$, and by (a) $Z(Z - qI)(Z - \hat kI) = \mu(Y\mathbf 1)(\mathbf z^{\mathsf T}Z - \hat k\mathbf z^{\mathsf T}) = 0$. The roots are distinct, so both matrices are diagonalizable with eigenvalues in $\{0, q, \hat k\}$. The nonzero eigenvalues of $XY$ and $YX$ coincide with their algebraic multiplicities. The eigenvalue $\hat k$ of $M$ is simple: from $M\mathbf x = \hat k\mathbf x$ it follows that $\hat k(\hat k - q)\mathbf x = \mu(\mathbf 1^{\mathsf T}\mathbf x)\mathbf 1$. The trace of $M$ equals $\hat k + qm_q$, and the rank of a diagonalizable matrix is the number of its nonzero eigenvalues. ∎

For a graph on the line $\varepsilon$, Theorem 8.1 applies to four factorizations.

1. *Classes of equal columns* $D_1, \dots, D_b$ of sizes $w_1, \dots, w_b$ with membership matrix $E$ and representatives $y_j$: $X = M[\,\cdot\,, (y_1, \dots, y_b)]$, $Y = E^{\mathsf T}$, $\mathbf z = \mathbf 1$. The matrix $Z = E^{\mathsf T}X$ is the quotient by the classes of columns: $Z_{ij}$ is the number of vertices of $D_i$ with an arc into $y_j$ (for $\varepsilon = 1$ the vertex $y_j$ itself is counted). By (a), $Z^2 = qZ + \mu\mathbf w\mathbf 1^{\mathsf T}$, and by (c), $\operatorname{rank}Z = 1 + m_q$.
2. *Classes of equal rows*: the same for $M^{\mathsf T}$.
3. *Type pair* by the classes of rows and columns (Theorem 8.2(d)): $X = \Phi R$, $Y = \Psi^{\mathsf T}$, $Z = N^{\mathsf T}R$.
4. *Rank factorization*: $X$ consists of $\operatorname{rank}M$ independent columns of $M$, and $Y$ is the matrix of coefficients; (b) gives $Z = qI + (\mu/\hat k^2)(Y\mathbf 1)(\mathbf 1^{\mathsf T}X)$. For $\varepsilon = 0$ this is the factorization of the first survey [4, Theorem 1].

### 8.2. The two lines of twins

Let $A$ be a DSRG $(v, k, t, \lambda, \mu)$ with $0 < t < k < v - 1$ and $\mu \ge 1$, let $M = A + \varepsilon I$, and let $m_q$ be the multiplicity of the eigenvalue $q$ of $M$. We denote the classes of equal rows of $M$ by $1, \dots, h$ and their membership matrix by $\Phi$ (of size $v \times h$); the classes of equal columns are $1, \dots, h'$, with membership matrix $\Psi$. A vertex has *type* $(i, j)$ if its row lies in class $i$ and its column lies in class $j$. A *type pair* $(R, N)$ consists of: $R$, a zero-one matrix of size $h \times h'$ with $M = \Phi R\Psi^{\mathsf T}$ (an entry of $M$ depends only on the class of its row and the class of its column); and $N = \Phi^{\mathsf T}\Psi$, the number of vertices of each type. Further, $\mathbf a = N\mathbf 1$ and $\mathbf b = N^{\mathsf T}\mathbf 1$ are the sizes of the row classes and the column classes.

**Theorem 8.2 (the two lines of twins).** (a) If $M$ has two equal rows or two equal columns, then $A$ lies on the line $\varepsilon$: $t = \mu$ for $\varepsilon = 0$ and $t = \lambda + 1$ for $\varepsilon = 1$. On the line $\varepsilon$ we have $M^2 = qM + \mu J$ and $M\mathbf 1 = M^{\mathsf T}\mathbf 1 = \hat k\mathbf 1$.

(b) $A$ lies on the line $\varepsilon$ with parameters $(v, \hat k, q, \mu)$ exactly when the complement $\bar A = J - I - A$ lies on the line $1 - \varepsilon$ with parameters $(v, v - \hat k, -q, \bar\mu)$, where $\bar\mu = v - 2\hat k + q + \mu$. In that case $\bar A + (1 - \varepsilon)I = J - M$, the classes of $M$ and of $J - M$ are the same, and the type pair of the complement is $(J - R, N)$.

(c) On the line $t = \lambda + 1$ the number $q$ is positive, and on the line $t = \mu$ it is negative; in particular, every DSRG with $t = \mu$ satisfies $\mu > \lambda$. The multiplicity $m_q = (\varepsilon v - \hat k)/q$ is at least 1, and $\operatorname{rank}M = 1 + m_q$.

(d) $A$ is a DSRG on the line $\varepsilon$ with parameters $(v, \hat k, q, \mu)$ exactly when its type pair satisfies four conditions: $N_{ij} > 0 \Rightarrow R_{ij} = \varepsilon$; $R\mathbf b = \hat k\mathbf 1$; $\mathbf a^{\mathsf T}R = \hat k\mathbf 1^{\mathsf T}$; $RN^{\mathsf T}R = qR + \mu J$. Then $\operatorname{rank}R = 1 + m_q$, so $h, h' \ge 1 + m_q$. Conversely, any zero-one matrix $R$ and any matrix $N$ of nonnegative integers satisfying these conditions define the matrix $\Phi R\Psi^{\mathsf T} - \varepsilon I$, which satisfies equalities (1) with $k = \hat k - \varepsilon$, $\lambda = q + \mu - 2\varepsilon$, and $t$ of its line; this is a DSRG when, in addition, $0 < t < k < v - 1$. Without this condition, a pair can give a degenerate graph: the pair $(J - I, aI)$ gives a complete multipartite graph with $t = k$, and the pair $([1], [v])$ gives the complete graph.

(e) For $c \ge 1$ the type pair of $M \otimes J_c$ is $(R, cN)$, and it satisfies the conditions of (d) with parameters $(cv, c\hat k, cq, c\mu)$. On the line $t = \mu$ this is the blow-up $A \otimes J_c$; on the line $t = \lambda + 1$ it is the clique blow-up $(A + I) \otimes J_c - I$. The complement of the blow-up $A \otimes J_c$ is the clique blow-up of the graph $\bar A$.

(f) Let $Z$ be the quotient by the classes of columns (decomposition 1 after Theorem 8.1). Then $Z_{jj} = \varepsilon w_j$, $\sum_{i \ne j} Z_{ij} = \hat k - \varepsilon w_j$, and for $i \ne j$ we have $\max(0, w_i - \bar\mu) \le Z_{ij} \le \min(w_i, \mu)$; also $\sum_{i \ne j} Z_{ji}Z_{ij} = w_j(\varepsilon q + \mu - \varepsilon w_j)$. The quotient of the complement by the same classes equals $\mathbf w\mathbf 1^{\mathsf T} - Z$.

*Proof.* (a) Let the rows $x \ne y$ of $M$ be equal. For $\varepsilon = 0$ the out-neighbourhoods of $x$ and $y$ coincide. There is no arc $x \to y$, since otherwise $y$ would be its own out-neighbour; hence $(A^2)_{xy} = \mu$. On the other hand, $(A^2)_{xy}$ is the number of common vertices of the out-neighbourhood of $y$ and its in-neighbourhood, that is, $t$. For $\varepsilon = 1$ the closed out-neighbourhoods coincide and there is an arc $x \to y$, so $\lambda + 2 = (B^2)_{xy} = (B^2)_{yy} = t + 1$. Equal columns are handled the same way for $A^{\mathsf T}$, which has the same parameter set. On the line $t = \mu$ equation (1) takes the form $A^2 = (\lambda - \mu)A + \mu J$, and on the line $t = \lambda + 1$ it takes the form (4).

(b) $J - M = J - A - \varepsilon I = \bar A + (1 - \varepsilon)I$. From $M^2 = qM + \mu J$ and $JM = MJ = \hat kJ$ it follows that $(J - M)^2 = (v - 2\hat k + \mu)J + qM = -q(J - M) + \bar\mu J$, and the row and column sums of $J - M$ equal $v - \hat k$. By (a), this is the equation of the line $1 - \varepsilon$ for $\bar A$. The complement is an involution, so the converse holds too. The rows of $M$ and of $J - M$ are equal or different simultaneously.

(c) If $q = 0$, then $M^2 = \mu J$, all eigenvalues of $M$ except $\hat k$ are zero, and $\operatorname{tr}M = \hat k$. But $\operatorname{tr}M = \varepsilon v$, whence $k = 0$ when $\varepsilon = 0$ and $k = v - 1$ when $\varepsilon = 1$. If $q = \hat k$, then $M^2\mathbf 1 = qM\mathbf 1 + \mu J\mathbf 1$ gives $\mu v = 0$. By Theorem 8.1(c) with $X = M$, $Y = I$ we get $\varepsilon v = \operatorname{tr}M = \hat k + qm_q$. For $\varepsilon = 0$ this gives $qm_q = -k < 0$, that is, $q = \lambda - \mu < 0$; for $\varepsilon = 1$ it gives $qm_q = v - \hat k > 0$. In both cases $m_q \ge 1$ and $\operatorname{rank}M = 1 + m_q$.

(d) The entry of $M$ does not change when a row is replaced by an equal row or a column by an equal column, so $M = \Phi R\Psi^{\mathsf T}$; moreover $\Phi\mathbf 1 = \Psi\mathbf 1 = \mathbf 1$ and $\Psi^{\mathsf T}\Phi = N^{\mathsf T}$. The diagonal entry $M_{xx}$ is the entry of $R$ at the type of $x$, and the types with $N_{ij} > 0$ are exactly the types of vertices; therefore the first condition means that $A$ has no loops. The second and third conditions are $M\mathbf 1 = \Phi R\mathbf b = \hat k\mathbf 1$ and $\mathbf 1^{\mathsf T}M = \mathbf a^{\mathsf T}R\Psi^{\mathsf T} = \hat k\mathbf 1^{\mathsf T}$. Finally, $M^2 = \Phi RN^{\mathsf T}R\Psi^{\mathsf T}$ and $qM + \mu J = \Phi(qR + \mu J)\Psi^{\mathsf T}$. $\Phi$ has a left inverse and $\Psi^{\mathsf T}$ a right inverse, so $M^2 = qM + \mu J$ is equivalent to the fourth condition. The rank: $\operatorname{rank}R = \operatorname{rank}M$. For the converse, take $N_{ij}$ vertices of type $(i, j)$ and build $\Phi$, $\Psi$, and $M$ from the types; the computation is the same, and $A = M - \varepsilon I$ satisfies (1) with the stated parameters.

(e) The row $(x, u)$ of $M \otimes J_c$ is the row $x$ of $M$ repeated $c$ times. So the classes of the blow-up are the classes of $M$ with each class repeated $c$ times: $R$ stays the same, $N$ becomes $cN$, and conditions (d) hold with parameters $(cv, c\hat k, cq, c\mu)$. For the complement, $J - I - A \otimes J_c = (\bar A + I) \otimes J_c - I$.

(f) For $x \in D_j$ the entry $M[x, y_j] = M[x, x] = \varepsilon$, so $Z_{jj} = \varepsilon w_j$; the sum of column $j$ of $Z$ equals $\hat k$. The columns $y_i$ and $y_j$ are different and each contains $\hat k$ ones, so there is $z$ with $M[z, y_i] = 1$ and $M[z, y_j] = 0$, and $\mu = (M^2)[z, y_j] \ge Z_{ij}$, because $M[z, u] = 1$ for every $u \in D_i$. The lower bound is the same estimate applied to $J - M$, whose quotient is $\mathbf w\mathbf 1^{\mathsf T} - Z$ by (b). The last identity is the entry $(j, j)$ of the equality $Z^2 = qZ + \mu\mathbf w\mathbf 1^{\mathsf T}$. ∎

The normal form (d) for $\varepsilon = 0$ and the quotient (f) for $\varepsilon = 1$ have already occurred in the corpus separately; (b) transfers each of them to the other line.

### 8.3. Class size and the series $H_m(c)$

**Proposition 8.3 (class size of twins).** Let $t = \lambda + 1$, $B = A + I$, $\hat k = k + 1$, $q = \lambda + 2 - \mu$, $f = (v - \hat k)/q$, and let $C$ be a class of equal rows of $B$ of $a$ vertices. Then

(a) $a \le \lambda + 1$;

(b) $a(\lambda + 2 - a) \le \mu(\hat k - a)$;

(c) $a \ge \hat k - \mu f$;

(d) $a \le k - \lambda - 1 + \mu = \hat k - q$;

(e) $q \le \mu f$, that is, $(\lambda + 2 - \mu)^2 \le \mu(v - k - 1)$.

The same holds for classes of equal columns.

*Proof.* Let $x \in C$, let $N^+[x]$ be the closed out-neighbourhood, and let $D = N^+[x] \setminus C$. By (4), $|N^+[x] \cap N^-[y]|$ equals $\lambda + 2$ for $y \in N^+[x]$ and $\mu$ otherwise.

(a) If $y \in C$, then $x \in N^+[y]$, so $C \subseteq N^+[x] \cap N^-[x]$. The set $D$ is nonempty, since otherwise $\hat k = \lambda + 2$ and $k = t$. For $z \in D$ the whole class lies in $N^-[z]$, so $C \cup \{z\} \subseteq N^+[x] \cap N^-[z]$, and $a + 1 \le \lambda + 2$.

(b) For $u \notin C$ the rows $u$ and $x$ are different, so there is $w \in N^+[x] \setminus N^+[u]$. The class lies in $N^-[w]$, and $|N^+[u] \cap C| \le |N^+[u] \cap N^-[w]| = \mu$. For $y \in C$, the set $N^+[x] \cap N^-[y]$ of $\lambda + 2$ vertices contains the class, and its remaining $\lambda + 2 - a$ vertices lie in $D$. Pairs $(y, u)$ with $y \in C$, $u \in D$, $y \in N^+[u]$ are counted in two ways: $a(\lambda + 2 - a) \le \mu|D| = \mu(\hat k - a)$.

(c) For $u \in D$ there is $w \in N^+[u] \setminus N^+[x]$. Of the $\lambda + 2$ vertices of $N^+[u] \cap N^-[w]$, at most $\mu$ lie in $N^+[x]$, so $|N^+[u] \setminus N^+[x]| \ge q$. Each vertex outside $N^+[x]$ receives exactly $\mu$ arcs from $N^+[x]$, and none of them comes from the class. Counting pairs $(u, w)$ with $u \in D$ and $w \in N^+[u] \setminus N^+[x]$ gives $q(\hat k - a) \le \mu(v - \hat k) = \mu qf$.

(d) $N^+[x] \cap N^-[x]$ has exactly $\lambda + 2$ vertices, and the class occupies at most $\lambda + 1$ of them. Hence there is $u \in D$ with an arc $u \to x$; take $c \in C \cap N^+[u]$. Then $|N^+[u] \cap N^-[c]| = |N^+[x] \cap N^-[c]| = \lambda + 2$, and after subtracting the common part, $|(N^+[u] \setminus N^+[x]) \cap N^-[c]| = |(N^+[x] \setminus N^+[u]) \cap N^-[c]|$. The right-hand side contains $C \setminus N^+[u]$, that is, at least $a - |N^+[u] \cap C| \ge a - \mu$ vertices, while the left-hand side lies in $N^-[c] \setminus N^+[x]$, which has $\hat k - (\lambda + 2)$ vertices. Hence $a - \mu \le k - \lambda - 1$.

(e) From (c) and (d): $\hat k - \mu f \le a \le \hat k - q$. ∎

**Corollary 8.4 (the series $H_m(c)$).** For odd $c \ge 3$ and any $m \ge 1$ there is no DSRG

$$
H_m(c) = \bigl(mc^2,\ 2mc - 1,\ m(c + 2) - 1,\ m(c + 2) - 2,\ 2m\bigr)
$$

and hence no complement of it.

*Proof.* Let $D_j$ be the classes of equal columns of $B$, of sizes $w_j$, and let $Z$ be the quotient of Theorem 8.2(f). By 8.2(f), $\sum_{i \ne j}Z_{ij} = \hat k - w_j$ and $\sum_{i \ne j}Z_{ji}Z_{ij} = w_j(\lambda + 2 - w_j)$, and $Z_{ji} \le \mu$. Hence

$$
\mu(\hat k - w_j) - w_j(\lambda + 2 - w_j) = \sum_{i \ne j}(\mu - Z_{ji})Z_{ij} \ge 0,
$$

and equality in Proposition 8.3(b) for the class $D_j$ holds exactly when $Z_{ji} = \mu$ for every $i \ne j$ with $Z_{ij} > 0$. If all classes are on equality, then every nonzero off-diagonal entry of $Z$ equals $\mu$: from $Z_{ij} > 0$ it follows that $Z_{ji} = \mu > 0$, and hence $Z_{ij} = \mu$. Then the sum $\hat k - w_j$ is divisible by $\mu$.

For $H_m(c)$ we have $\hat k = 2mc$, $q = mc$, $\mu = 2m$, $f = c - 2$, and $\lambda + 2 = m(c + 2)$. Proposition 8.3(c, d) gives $4m \le a \le mc$ for the size $a$ of any class, and 8.3(b) gives the inequality $a(\lambda + 2 - a) - \mu(\hat k - a) = -(a - 4m)(a - mc) \le 0$. Only $a \in \{4m, mc\}$ remain, and for both values equality holds in 8.3(b). For $c = 3$ there is no choice at all, because $4m > mc$. Hence equality holds for all classes, and $2m \mid 2mc - a$ for each class. The size $a = mc$ requires $2m \mid mc$, that is, even $c$. Therefore, for odd $c$ all classes have size $4m$, and $4m \mid v = mc^2$, whence $4 \mid c^2$, which again requires even $c$. ∎

### 8.4. Cases in the corpus

*Nonexistence.* Our paper [41] proves the inequality of Proposition 8.3(e) and the nonexistence of six parameter sets, $(66, 10, 5, 4, 1)$, $(91, 12, 6, 5, 1)$, $(40, 9, 6, 5, 1)$, $(80, 19, 13, 12, 2)$, $(96, 15, 10, 9, 1)$, $(28, 6, 3, 2, 1)$, and of their complements. The arguments are written by hand and in Lean, and one branch for $(28, 6, 3, 2, 1)$ is closed by a DRAT certificate. For $(80, 19, 13, 12, 2)$, Proposition 8.3 suffices: here $\hat k = 20$, $q = 12$, $f = 5$, and (c) gives $a \ge 10$, while (d) gives $a \le 8$. Paper [90] proves by hand the nonexistence of the series $H_m(c)$ for odd $c \ge 3$; Corollary 8.4 gives the same conclusion by a single identity for the quotient. Paper [96] proves, for $\mu = 2$ and $t = \lambda + 1$, that a saturated clique of size $c + 2$ with $c > 1$ has no exactly three outgoing and three incoming single contacts, and it lists for $(77, 13, 4, 3, 2)$ the necessary lists obtained by enumeration (claimed, not recomputed). Paper [78] proves without reservations the nonexistence of $(81, 48, 32, 26, 32)$ on the line $t = \mu$, and with it of the complement $(81, 32, 16, 15, 11)$. The argument rests on a finite nonnegative basis of columns and exact integer Farkas certificates, while the enumeration of normals was done by two programs without a certificate (claimed, not recomputed). In the same way, by an enumeration of normals by two programs, the first survey accepted the nonexistence of $H_1(9) = (81, 17, 10, 9, 2)$ [4, Table 5], and the article also counts the pair $(81, 32, 16, 15, 11)$ as solved (Section 12).

*Quotients and type pairs.* Paper [84] constructs $(70, 9, 3, 2, 1)$ and its complement by lifting the seed $(35, 8, 4, 1, 2)$: the classes of equal columns of $A + I$ are pairs, and the quotient by them equals $A' + 2I$ for the matrix $A'$ of the seed. The quotient identity of Theorem 8.1 becomes here the seed equation $(A' + 2I)^2 = 3(A' + 2I) + 2J$. Its general theorem on the quotient by classes of one size is decomposition 1 after Theorem 8.1. Paper [99] constructs $(65, 14, 4, 3, 3)$, $(77, 13, 4, 3, 2)$ and their complements by lifting mixed quotients, and the family $(325u + 65, 65u + 14, 13u + 4, 13u + 3, 13u + 3)$. The constructions are checked by exact computation, while the classifications of lifts are exhaustive searches without a certificate (claimed, not recomputed). Paper [100] constructs $(104, 25, 10, 9, 5)$ and its complement from eight orbits of rows in $\mathbb Q[z]/(z^{13} - 1)$, finds the group $(C_2)^{13} \rtimes C_{13}$ of order 106,496, and the family $(416u + 104, 104u + 25, 26u + 10, 26u + 9, 26u + 5)$. Paper [101] constructs $(88, 20, 5, 3, 5)$ on the line $t = \mu$ from a type pair with a $14 \times 16$ seed (this is the normal form of Theorem 8.2(d)), and shows that the non-isomorphic graphs of this parameter set number at least 45,360. Its family $(88m, 20m, 5m, 3m, 5m)$ is the blow-up of Theorem 8.2(e).

*The series $(q(3q - 1), 3q - 2, q, q - 1, 2)$.* Paper [88] proves by hand that graphs of this series exist for all $q \ge 3$; for $q = 6$ this is $(102, 16, 6, 5, 2)$. Paper [87] finds three graphs $(102, 16, 6, 5, 2)$ and checks them against the definition in integers. That the graphs are pairwise non-isomorphic and that their automorphism group is trivial is established by the program of the paper (claimed, not recomputed), while its remarks on the structure of cliques are not proved.

### 8.5. What is added to the papers

The quotients of papers [84], [99] and [100], the type pair of paper [101], and the rank factorizations of the papers of Section 9 are cases of Theorem 8.1, and each paper derived its own particular form anew. Theorem 8.2 transfers the normal form and the bounds on the quotient from one line to the other, and removes the hypothesis on the sign of $q$: the line itself fixes the sign, and every DSRG with $t = \mu$ satisfies $\mu > \lambda$. Corollary 8.4 gives a different, short derivation of the result of paper [90], by a single identity for the quotient. The member $H_1(9) = (81, 17, 10, 9, 2)$ of the series is open in the table [2]. The first survey accepted its nonexistence on the basis of a proof in which the normals were enumerated by two programs [4, Table 5], and the proof of paper [90] and Corollary 8.4 close it without programs.

### 8.6. Limits of the section

Proposition 8.3 narrows only the parameter sets with small $\mu f$. For the open sets $(98, 20, 9, 8, 3)$ and $(75, 19, 8, 7, 4)$ on the line $t = \lambda + 1$ it allows all class sizes from 1 to $\lambda + 1$, and Theorems 8.1 and 8.2 do not close the sets themselves: they give the form in which a graph is sought or excluded. The nonexistence of $(81, 32, 16, 15, 11)$ was proved by paper [78], and we have not recomputed its computation.

## 9. The line $t = \lambda + 1$: column space of $A + I$

Thirteen papers of the corpus attack two open parameter sets of the line $t = \lambda + 1$ — $(98, 20, 9, 8, 3)$ and $(75, 19, 8, 7, 4)$ — and the two families that contain them. The papers bound the classes of equal rows, the number of distinct neighbourhoods, the coverings and the support of one-way arcs. Almost all of their common steps are consequences of one identity, $B^2 = qB + \mu J$, applied to vectors of the column space of $B = A + I$; Theorem 9.1 states these consequences for every DSRG with $t = \lambda + 1$. The finite exhaustive searches with which the papers conclude remain the papers' own results.

### 9.1. Maximum principle

Let $t = \lambda + 1$, $0 < t < k < v - 1$, $B = A + I$, $\hat k = k + 1$, $q = \lambda + 2 - \mu$ and $f = (v - \hat k)/q$. By (4) and Theorem 8.2, $B^2 = qB + \mu J$, $B\mathbf 1 = B^{\mathsf T}\mathbf 1 = \hat k\mathbf 1$ and $q \ge 1$; moreover, $\hat k - q = k - \lambda - 1 + \mu \ge \mu$ and $\hat k(\hat k - q) = \mu v$. Column $j$ of $B$ is the indicator of the closed in-neighbourhood $N^-[j]$. A *member* is a vector of the real column space of $B$; the *mass* of a vector is the sum of its coordinates; $M_+(\mathbf z)$ and $M_-(\mathbf z)$ are the sum of the positive coordinates of $\mathbf z$ and the sum of the absolute values of the negative coordinates. The *family* $F(q, \mu)$ consists of the parameter sets of the line with $\hat k = \mu q$, that is, $((\mu - 1)q^2, \mu q - 1, q + \mu - 1, q + \mu - 2, \mu)$. The set $(98, 20, 9, 8, 3)$ is $F(7, 3)$, the set $(75, 19, 8, 7, 4)$ is $F(5, 4)$, and $F(q, 3) = (2q^2, 3q - 1, q + 2, q + 1, 3)$.

**Theorem 9.1 (maximum principle on the column space).** (a) A vector $\mathbf x$ is a member if and only if the vector $B\mathbf x - q\mathbf x$ is constant; then $B\mathbf x = q\mathbf x + \gamma\mathbf 1$ with $\gamma = \mu(\mathbf 1^{\mathsf T}\mathbf x)/\hat k$.

(b) For an integer member the number $\mu(\mathbf 1^{\mathsf T}\mathbf x)/\hat k$ is an integer, that is, the mass is a multiple of $\hat k/\gcd(\hat k, \mu)$.

(c) If $B\mathbf z = q\mathbf z + \gamma\mathbf 1$, then in each coordinate $h$ we have $-M_-(\mathbf z) \le qz_h + \gamma \le M_+(\mathbf z)$. Equality on the right means that $N^+[h]$ contains all positive coordinates of $\mathbf z$ and no negative ones; equality on the left is the reverse.

(d) If $\mathbf x$ is a nonzero non-negative integer member of mass $s$ with largest entry $M$, then $qM + \mu s/\hat k \le s$, that is, $s \ge q\hat kM/(\hat k - \mu)$.

(e) Let the indicator $\mathbf 1_H$ of a nonempty set $H$ of $s$ vertices be a member, and $\beta = \mu s/\hat k$. Then each vertex of $H$ has exactly $q + \beta$ closed out-neighbours in $H$, and each vertex outside $H$ has exactly $\beta$. If $H \not\subseteq N^-[j]$ for every $j \in H$, then $2(q + \beta) \le s + \mu$. If $H \subseteq N^-[j]$ for some $j$, then the indicator of $N^-[j] \setminus H$ is a member of mass $\hat k - s$.

(f) For distinct columns $R \ne S$, taken as vertex sets, $|R \setminus S| = |S \setminus R| \ge q$. When $|R \setminus S| = q$, the sets $D_1 = R \setminus S$ and $D_2 = S \setminus R$ are complete blocks, $B[D_1, D_1] = J$ and $B[D_2, D_2] = J$, and there are no arcs between $D_1$ and $D_2$.

(g) Let $\mathbf 1_H$ be a member with $B\mathbf 1_H = q\mathbf 1_H + \beta\mathbf 1$, let $R$ be a column (regarded as a vertex set), $P = H \setminus R$ and $N = R \setminus H$. If $P \ne \varnothing$, then $|P| \ge q + \beta - \mu$; if $N \ne \varnothing$, then $|N| \ge q + \mu - \beta$.

(h) In the family $F(q, \mu)$ the mass of each integer member is a multiple of $q$, and a nonzero non-negative integer member has mass at least $2q$. For $\mu = 2$ and $\mu = 3$ the least mass of a nonzero non-negative integer member equals $\hat k = \mu q$, and it is attained by the columns.

*Proof.* (a) $B(B - qI)(B - \hat kI) = \mu J(B - \hat kI) = 0$, and the roots $0$, $q$, $\hat k$ are distinct, so $B$ is diagonalizable: its column space is the sum of the eigenspaces for $\hat k$ and $q$, and its kernel is the eigenspace of zero. The value $\hat k$ is simple (Theorem 8.1(c)). Decompose $\mathbf x = \mathbf x_{\hat k} + \mathbf x_q + \mathbf x_0$ along the eigenspaces; then $B\mathbf x - q\mathbf x = (\hat k - q)\mathbf x_{\hat k} - q\mathbf x_0$ with $\mathbf x_{\hat k} \parallel \mathbf 1$, and this vector is constant exactly when $\mathbf x_0 = 0$. If $\mathbf x = B\mathbf g$, then $B\mathbf x = q\mathbf x + \mu(\mathbf 1^{\mathsf T}\mathbf g)\mathbf 1$ and $\mathbf 1^{\mathsf T}\mathbf x = \hat k\,\mathbf 1^{\mathsf T}\mathbf g$.

(b) $B\mathbf x - q\mathbf x$ is an integer vector equal to $\gamma\mathbf 1$.

(c) $(B\mathbf z)_h$ is the sum of the coordinates of $\mathbf z$ over $N^+[h]$, and a partial sum of the coordinates lies between the sum of all negative coordinates and the sum of all positive ones; equality requires the stated form of $N^+[h]$.

(d) In coordinate $h$ with $x_h = M$: $qM + \mu s/\hat k = (B\mathbf x)_h \le s$, because $\mathbf x \ge 0$.

(e) The number of neighbours is the coordinatewise form of $B\mathbf 1_H = q\mathbf 1_H + \beta\mathbf 1$. Let $j \in H$, $h_j = |N^-[j] \cap H|$, and suppose there is $i \in H \setminus N^-[j]$. Then $B_{ij} = 0$ and $\mu = (B^2)_{ij} = |N^+[i] \cap N^-[j]| \ge (q + \beta) + h_j - s$. The sum of $h_j$ over $j \in H$ is the number of pairs $(i, j)$ in $H$ with $B_{ij} = 1$, that is, $s(q + \beta)$, so the average of $h_j$ over the nonempty set $H$ equals $q + \beta$. If no $j \in H$ gives $H \subseteq N^-[j]$, then $q + \beta \le s + \mu - q - \beta$. The last claim: a column and $\mathbf 1_H$ are members, and their difference is a zero-one vector.

(f) Let $R = N^-[x]$, $S = N^-[y]$ and $\mathbf z = \mathbf 1_R - \mathbf 1_S = B(\mathbf e_x - \mathbf e_y)$; the mass of $\mathbf z$ is zero, and by (a) $B\mathbf z = q\mathbf z$. Both masses equal $\hat k$, so $|R \setminus S| = |S \setminus R|$. In a coordinate $h \in D_1$, item (c) gives $q \le M_+(\mathbf z) = |D_1|$; in case of equality $N^+[h] \supseteq D_1$ and $N^+[h] \cap D_2 = \varnothing$. A coordinate $h \in D_2$ gives the symmetric conclusion.

(g) The vector $\mathbf z = \mathbf 1_H - \mathbf 1_R$ satisfies $B\mathbf z = q\mathbf z + (\beta - \mu)\mathbf 1$. In a coordinate from $P$, item (c) gives $q + \beta - \mu \le |P|$; in a coordinate from $N$, it gives $-q + \beta - \mu \ge -|N|$.

(h) For $\hat k = \mu q$, item (b) gives that the masses are multiples of $q$, and item (d) gives $s \ge q^2M/(q - 1) > q$; hence $s \ge 2q$, and for $\mu = 2$ this is $\hat k$. Let $\mu = 3$ and $s = 2q$. From (d), $qM + 2 \le 2q$, so $M = 1$, and the member is $\mathbf 1_H$ with $|H| = 2q$ and $\beta = 2$. If $H \subseteq N^-[j]$ for some $j \in H$, then by (e) the indicator of $N^-[j] \setminus H$ is a zero-one member of mass $q < 2q$, which is impossible; otherwise (e) requires $2(q + 2) \le 2q + 3$, which is false. The mass $3q = \hat k$ is attained by a column. ∎

The transposed graph is a DSRG with the same parameter set, so Theorem 9.1 holds for the row space as well.

**Corollary 9.2.** If a DSRG with parameter set $(98, 20, 9, 8, 3)$ exists, then the least mass of a nonzero non-negative integer vector of the column space of $A + I$ (and of the row space) equals 21, and two distinct closed in-neighbourhoods have at most 14 common vertices.

*Proof.* This is $F(7, 3)$: item (h) gives mass $\hat k = 21$, and item (f) gives $|R \cap S| = \hat k - |R \setminus S| \le 21 - 7$. ∎

For $(75, 19, 8, 7, 4) = F(5, 4)$, item (h) gives only a mass of at least $2q = 10$ that is a multiple of 5.

### 9.2. Cases in the corpus

*The class of eight equal rows in the parameter set $(98, 20, 9, 8, 3)$.* Proposition 8.3 allows, for this parameter set, classes of equal rows of size up to 9. Papers [104], [105] and [106] study a class of eight rows. Paper [104] constructs a local map for it, derives a rank inequality, and proves that the set $U$ of 13 vertices has at least three even components; the basis is 483 local maps with certificates (claimed, not recomputed). Paper [105] proves that at rank 10 all three even basins are balanced, and at rank 11 two of them are, and finds a half-integral indicator of the class; paper [106] proves, at rank 10 with three even basins, that each basin is an isolated two-cycle of true twins; both rely on classifications with Farkas certificates (claimed, not recomputed). The rank decompositions used by these papers are decomposition 4 after Theorem 8.1, where $\operatorname{rank}B = 1 + f = 12$, and the identity of paper [105] for vectors of the column space is Theorem 9.1(a).

*Classes and neighbourhoods in the families.* Paper [107] proves that in $F(q, 3)$ with $q \ge 7$ at least eight classes of rows have size not divisible by 3, and that in $F(q, 4)$ at least six classes have size not divisible by 4; for $(98, 20, 9, 8, 3)$ this gives at least eight such classes, and for classes of size at most 3, at least 36. The branch $q = 7$ is resolved by a covering of 35 triples with RUP certificates (claimed, not recomputed). Paper [108] proves that in $F(q, 3)$ there are at least $2q$ distinct closed neighbourhoods in each direction, and that this bound is attained exactly when $3 \mid q$; for $(98, 20, 9, 8, 3)$ it obtains 16 by exhaustive search without a certificate (claimed, not recomputed). Paper [111] raises this bound to 17 and describes minimal weighted coverings: among ten columns, one has weight 1, two have weight $2/3$ and seven have weight $1/3$, and the shortest odd covering consists of eight neighbourhoods; the basis is a census with certificates (claimed, not recomputed). Paper [109] proves for $(75, 19, 8, 7, 4)$ that a full class of equal columns and a full class of equal rows have size at most 3, and that the number of distinct rows $R$ and columns $C$ is at least 15 when $R + C \ge 32$; the basis is an exhaustive search without certificate, 408 formulas with DRAT certificates, and an external classification of polytopes (claimed, not recomputed).

*Masses and coverings.* Paper [110] proves by hand that in $F(q, 3)$ with $q \ge 3$ the least mass of a nonzero non-negative integer member is $3q$ — this is Theorem 9.1(h) for $\mu = 3$ — and derives bounds on coverings; for $q = 7$ the mass is 21. Paper [112] derives a necessary condition — four distinct neighbourhoods with zero sum modulo 2 and an integral “parallelogram” — and obtains that a configuration of rank 4 requires at least 22 input neighbourhoods; it proves this bound for one of the two orientations; the basis is an exhaustive search with certificates (claimed, not recomputed). Its bound of 14 on the intersection of two neighbourhoods is a consequence of Corollary 9.2. Paper [117] proves that for the parameter set $(98, 20, 9, 8, 3)$ the independence number is at most 9, and that the induced forest of directed paths contains at most 10 vertices; the common step is the mass 21 from Corollary 9.2, and 36 sign cases were checked by a program (claimed, not recomputed).

*Hulls and support of one-way arcs.* Paper [113] claims that the intersection of the real hulls of the closed columns and rows of $(98, 20, 9, 8, 3)$ contains, among zero-one vectors, only the constant ones; that the smaller part of the corresponding partition equals 14, 28 or 42; and that the graph is never a spanning subgraph of a DSRG $(98, 27, 12, 11, 6)$; the cases $s = 3$ and $s = 7$ are not proved in the text (claimed, not recomputed). Paper [114] proves that the digraph of one-way arcs of any graph $(75, 19, 8, 7, 4)$ or $(98, 20, 9, 8, 3)$ is primitive — strongly connected and of period 1; the finite arithmetic is done by two programs (claimed, not recomputed). Paper [115] proves that the support of one-way arcs of $(75, 19, 8, 7, 4)$ and of its complement has no regular automorphism group; the basis is an exhaustive search without certificate (claimed, not recomputed).

### 9.3. What is added to the papers

Theorem 9.1 replaces the arguments of papers [105], [107], [110], [111], [112] and [117], each of which derived them for one parameter set or one family: the identity on the column space, integrality of the mass, the signed mass, the least mass and the overlap of zero-one vectors. All of them hold for any DSRG with $t = \lambda + 1$. Item (h) carries the least-mass result of paper [110] over to $\mu = 2$, and Corollary 9.2 gives, in one line, mass 21 and intersection 14 for $(98, 20, 9, 8, 3)$.

### 9.4. Limits of the section

Both parameter sets, $(98, 20, 9, 8, 3)$ and $(75, 19, 8, 7, 4)$, are open. Theorem 9.1 is a tool for search and elimination, not an argument for nonexistence, and for $(75, 19, 8, 7, 4)$ item (h) does not give the mass $\hat k$. The estimates of the numbers of classes and neighbourhoods from the papers of this section rest on those papers' exhaustive searches; we have not recomputed them.

## 10. Closed sets: frequencies, energy and traces

Seventeen papers of the corpus study the local structure of a graph: the induced core, the components of the one-way part, the partition of vertices into $N$-closed sets, principal blocks and their characteristic polynomials. Most papers are devoted to two open parameter sets — $(45, 18, 16, 7, 7)$ and $(110, 25, 21, 4, 6)$. All these papers share one apparatus: the symmetric part $H$ and the skew-symmetric part $K$ of the matrix anticommute (Lemma 10.1), and on an $N$-closed set this gives the decomposition of $K$ by frequencies (Theorem 10.2), the trace principle and the compression onto the kernel of $K$ (Theorem 10.3), and, for principal blocks, the formula for the characteristic polynomial (Theorem 10.4).

In this section $b = \mu - \lambda$, $\Delta = b^2 + 4(t - \mu) = (r - s)^2$, $r$ is the larger root, $\delta = r - s = \sqrt\Delta > 0$, $H = A + A^{\mathsf T} + bI$ and $K = A - A^{\mathsf T}$. For an $N$-closed set $W$ (Section 2) of $\ell$ vertices and $U = V \setminus W$, put $K_W = K[W, W]$, $K_U = K[U, U]$, $H_W = H[W, W]$ and $X = A[U, W]$. All arcs between $W$ and $U$ are mutual, so $K[W, U] = 0$, $H[U, W] = 2X$, and $K_W\mathbf 1_W = 0$.

**Lemma 10.1.** $HK + KH = 0$ and $H^2 + K^2 = \Delta I + 4\mu J$.

*Proof.* From (1), $A^2 - (A^{\mathsf T})^2 = (\lambda - \mu)(A - A^{\mathsf T}) = -bK$, so $HK + KH = 2(A^2 - (A^{\mathsf T})^2) + 2bK = 0$. Further, $H^2 + K^2 = 2A^2 + 2(A^{\mathsf T})^2 + 2b(A + A^{\mathsf T}) + b^2I$, and substituting (1) for $A^2$ and $(A^{\mathsf T})^2$ gives $(b^2 + 4(t - \mu))I + 4\mu J$. ∎

### 10.1. Decomposition by frequencies

A *frequency* of a skew-symmetric matrix $L$ is an eigenvalue $\omega \ge 0$ of $-L^2$; $V_\omega(L) = \ker(L^2 + \omega I)$ and $d(\omega) = \dim V_\omega(L)$. Let $P_\omega$ and $P'_\omega$ be the orthogonal projections onto $V_\omega(K_W)$ and $V_\omega(K_U)$, let $P = \sum_{\omega > 0}P_\omega$ be the projection onto the image of $K_W$, $P_0 = I - P$ and $\rho = \operatorname{rank}K_W$. The *energy at a frequency* is $E_\omega = \|XP_\omega\|_F^2$, and the total energy is $E = \sum_{\omega > 0}E_\omega$.

**Theorem 10.2 (decomposition by frequencies).** (a) For every $\mathbf e \in \mathbb R^W$ with $K_W^2\mathbf e = -\omega\mathbf e$

$$
\|H_W\mathbf e\|^2 + 4\|X\mathbf e\|^2 = (\Delta + \omega)\|\mathbf e\|^2 + 4\mu(\mathbf 1^{\mathsf T}\mathbf e)^2, \tag{10}
$$

and $\mathbf 1^{\mathsf T}\mathbf e = 0$ for $\omega > 0$.

(b) Let $H$ be a real symmetric and $K$ a real skew-symmetric matrix with $HK + KH = 0$, and let $K$ be block-diagonal with respect to a partition of the indices into parts $C_1, \dots, C_m$ with blocks $K_i$. Then for $i \ne j$ the block $B = H[C_j, C_i]$ satisfies $BK_i = -K_jB$ and $BK_i^2 = K_j^2B$; it maps $V_\omega(K_i)$ into $V_\omega(K_j)$, and it sets $V_\omega(K_i)$ to zero when $\omega$ is not a frequency of $K_j$. For a DSRG the parts are $N$-closed sets and $B = 2A[C_j, C_i]$.

(c) For $\omega > 0$ we have $(\Delta + \omega)\,d_W(\omega) = \|H_WP_\omega\|_F^2 + 4E_\omega$, and for $\omega = 0$, $\Delta(\ell - \rho) + 4\mu\ell = \|H_WP_0\|_F^2 + 4\|XP_0\|_F^2$. Moreover, $E_\omega = \|X^{\mathsf T}P'_\omega\|_F^2$, so the same balance holds from the side of $U$.

(d) $\|H_WP\|_F^2 = \Delta\rho + \|K_W\|_F^2 - 4E$. If $K_W$ and $K_U$ have no common nonzero frequencies ($W$ *spectrally isolated*), then $E = 0$; in general, $4E \le \sum(\Delta + \omega)\min(d_W(\omega), d_U(\omega))$ over the common nonzero frequencies.

*Proof.* (a) Extend $\mathbf e$ by zero to $U$; then $K\mathbf e = K_W\mathbf e$ and $H\mathbf e = (H_W\mathbf e, 2X\mathbf e)$. By Lemma 10.1, $\|H\mathbf e\|^2 = \mathbf e^{\mathsf T}H^2\mathbf e = \Delta\|\mathbf e\|^2 - \mathbf e^{\mathsf T}K^2\mathbf e + 4\mu(\mathbf 1^{\mathsf T}\mathbf e)^2$, and $-\mathbf e^{\mathsf T}K^2\mathbf e = \omega\|\mathbf e\|^2$. The vector $\mathbf 1_W$ lies in the kernel of $K_W$, and the kernel of a skew-symmetric matrix is orthogonal to its image, which contains $V_\omega(K_W)$ for $\omega > 0$.

(b) The block $(C_j, C_i)$ of the equality $HK + KH = 0$ is $BK_i + K_jB = 0$. Applying it twice gives $BK_i^2 = K_j^2B$, and $Bp(K_i^2) = p(K_j^2)B$ for every polynomial $p$. If $K_i^2\mathbf x = -\omega\mathbf x$, then $K_j^2(B\mathbf x) = -\omega B\mathbf x$. If $\omega$ is not a frequency of $K_j$, take the minimal polynomial $p$ of $K_j^2$: then $0 = Bp(K_i^2)\mathbf x = p(-\omega)B\mathbf x$ and $p(-\omega) \ne 0$. For the DSRG, $H[C_j, C_i] = A[C_j, C_i] + A[C_i, C_j]^{\mathsf T} = 2A[C_j, C_i]$, because arcs between different $N$-closed sets are mutual.

(c) Sum (10) over an orthonormal basis of $V_\omega(K_W)$; for $\omega = 0$ the sum of $(\mathbf 1^{\mathsf T}\mathbf e)^2$ over a basis of the kernel equals $\|P_0\mathbf 1_W\|^2 = \ell$. By (b), for the parts $W$ and $U$ the matrix $X$ maps $V_\omega(K_W)$ into $V_\omega(K_U)$ and $X^{\mathsf T}$ maps back, so $\|XP_\omega\|_F = \|P'_\omega XP_\omega\|_F = \|X^{\mathsf T}P'_\omega\|_F$. The balance from the side of $U$ is (a) for the $N$-closed $U$.

(d) The sum of the balances (c) over $\omega > 0$ gives the identity, because $\sum_{\omega > 0}\omega\,d_W(\omega) = -\operatorname{tr}K_W^2 = \|K_W\|_F^2$ and $\sum_{\omega > 0}d_W(\omega) = \rho$. By (b), $E_\omega = 0$ if $\omega$ is not a frequency of $K_U$. For a common frequency, nonnegativity of $\|H_WP_\omega\|_F^2$ and $\|H_UP'_\omega\|_F^2$ in the two balances (c) gives $4E_\omega \le (\Delta + \omega)d_W(\omega)$ and $4E_\omega \le (\Delta + \omega)d_U(\omega)$. ∎

The right-hand side of estimate (d) is computed in integers without computing frequencies: it is $\Delta\deg G$ plus the sum of the roots of $G$, where $G$ is the greatest common divisor of the characteristic polynomials of $-K_W^2$ and $-K_U^2$ without the root 0.

### 10.2. Trace and compression onto the kernel

**Theorem 10.3 (trace and compression).** (a) Let $D$ be a real symmetric and $L$ a real skew-symmetric matrix with $DL + LD = 0$; let a subspace $R$ be invariant under $D$ and $L$, and let $D^2 = c^2I$ with $c > 0$ on $R_0 = R \cap \ker L$. Then the trace of $D$ on $R \cap \operatorname{im}L$ is zero, and $\operatorname{tr}(D|_R) = c(m_+ - m_-)$, where $m_\pm$ are the multiplicities of the values $\pm c$ of $D$ on $R_0$. Hence $\delta' = \operatorname{tr}(D|_R)/c$ is an integer, $\dim R_0 \equiv \delta' \pmod 2$, and $\dim(R \cap \operatorname{im}L) \le \dim R - |\delta'|$.

(b) Let $W$ be an $N$-closed set, $E$ a matrix with $\ell$ columns, $EK_W = 0$, the row space of $E$ invariant under $H_W$ and containing $\mathbf 1_W$, and $X\mathbf x = 0$ for all $\mathbf x \in \ker E \cap \ker K_W$. Let $\tau$ be the trace of $H_W$ on the row space of $E$. Then $\delta' = (b\ell - \tau)/\delta$ is an integer and $\operatorname{rank}K_W \le \ell - \operatorname{rank}E - |\delta'|$.

(c) Let $M$ be a real matrix of order $n$ with $M\mathbf 1 = M^{\mathsf T}\mathbf 1 = \kappa\mathbf 1$ and $M^2 = c^2I + \gamma J$, $c > 0$; let $S = (M + M^{\mathsf T})/2$, $K' = M - M^{\mathsf T}$, and let $m_\pm$ be the multiplicities of the values $\pm c$ of $M$ on $\mathbf 1^\perp$. Then for every matrix $Y$ whose columns lie in $\ker K'$

$$
Y^{\mathsf T}\Bigl(cI + \frac{\kappa - c}{n}J - M\Bigr)Y \succeq 0, \qquad Y^{\mathsf T}\Bigl(cI - \frac{\kappa + c}{n}J + M\Bigr)Y \succeq 0,
$$

and the ranks of these matrices are at most $m_- - \operatorname{rank}K'/2$ and $m_+ - \operatorname{rank}K'/2$ respectively. For a DSRG, $M = 2A + bI$ is suitable: $c = \delta$, $\kappa = 2k + b$, $\gamma = 4\mu$.

(d) Let $W$ be a set of $\ell$ vertices of a DSRG with $K\mathbf 1_W = 0$, and let $e$ be the number of arcs from $W$ to $U$. Then $(k - r)\ell(v - \ell)/v \le e \le (k - s)\ell(v - \ell)/v$.

*Proof.* (a) For $\mathbf x \in R$, $L(D\mathbf x) = -D(L\mathbf x)$, so $D$ preserves $R \cap \ker L$ and $L(R)$. The restriction of $L$ to $R$ is skew-symmetric, so $R = (R \cap \ker L) \oplus L(R)$, and $L(R) = R \cap \operatorname{im}L$. On $L(R)$ the restriction of $L$ is invertible and $LDL^{-1} = -D$: the restriction of $D$ is similar to its negative, and its trace is zero. On $R_0$ the restriction of $D$ is symmetric with $D^2 = c^2I$, that is, it has the values $\pm c$. Hence $\delta' = m_+ - m_-$, $\dim R_0 = m_+ + m_-$, and the estimates follow.

(b) Take $R = \ker E$. The rows of $E$ lie in $\ker K_W$, and their space is $H_W$-invariant, so $R$ is invariant under $H_W$ and $K_W$. The block $(W, W)$ of the equality of Lemma 10.1 is $H_W^2 + 4X^{\mathsf T}X + K_W^2 = \Delta I + 4\mu J$; on $\mathbf x \in R_0$ the terms $X^{\mathsf T}X\mathbf x$, $K_W^2\mathbf x$ and $J\mathbf x$ vanish, and $H_W^2\mathbf x = \Delta\mathbf x$. By (a) with $c = \delta$, the trace of $H_W$ on $R$, which equals $b\ell - \tau$ (the diagonal of $H_W$ consists of the numbers $b$), is divisible by $\delta$; and $\ker K_W$ is the orthogonal sum of the row space of $E$ and $R_0$, whence $\operatorname{rank}K_W = \ell - \operatorname{rank}E - \dim R_0 \le \ell - \operatorname{rank}E - |\delta'|$.

(c) From $M^2 = (M^{\mathsf T})^2$ it follows that $S^2 + K'^2/4 = c^2I + \gamma J$ and $SK' + K'S = 0$, so $\ker K'$ is invariant under $S$, and on it $M = S$. The vector $\mathbf 1$ lies in $\ker K'$. On $\ker K' \cap \mathbf 1^\perp$ we have $S^2 = c^2I$; the values of $S$ there are $\pm c$, with multiplicities $n_\pm$, and by (a) with $R = \mathbf 1^\perp$ the trace of $S$ on $\mathbf 1^\perp$ equals $c(n_+ - n_-)$. The same trace equals $\operatorname{tr}M - \kappa = c(m_+ - m_-)$. Together with $n_+ + n_- = n - 1 - \operatorname{rank}K'$ and $m_+ + m_- = n - 1$, this gives $n_\pm = m_\pm - \operatorname{rank}K'/2$. The first matrix vanishes on $\mathbf 1$ and equals $c \mp c$ on the eigenvectors of $S$ from $\ker K' \cap \mathbf 1^\perp$ with value $\pm c$; that is, on $\ker K'$ it equals $2c$ times the orthogonal projection $P_-$ onto the value $-c$. Therefore its compression equals $2c(P_-Y)^{\mathsf T}(P_-Y) \succeq 0$, of rank at most $n_-$. The second matrix is the same computation with the value $+c$.

(d) The vector $\mathbf y = v\mathbf 1_U - (v - \ell)\mathbf 1$ lies in $\ker K \cap \mathbf 1^\perp$, where by (c) $H^2 = \Delta I$, hence $|\mathbf y^{\mathsf T}H\mathbf y| \le \delta\,\mathbf y^{\mathsf T}\mathbf y$. Direct computation gives $\mathbf y^{\mathsf T}\mathbf y = v\ell(v - \ell)$ and $\mathbf y^{\mathsf T}H\mathbf y/\mathbf y^{\mathsf T}\mathbf y = 2k + b - 2ve/(\ell(v - \ell))$; substituting $r, s = (-b \pm \delta)/2$ gives the estimate. ∎

Item (b) extends Theorem 1 of paper [95], which was proved for $(110, 25, 21, 4, 6)$, to every DSRG; item (c) at $K' = 0$ is the inequality $20I + 2J - 5B \succeq 0$ of paper [91] for the parameter set $(110, 25, 21, 4, 6)$; and item (d) is the cut bound of paper [93].

### 10.3. Characteristic polynomial of a principal block

**Theorem 10.4 (Jacobi minor).** Let $M$ be a matrix of order $n$ with $M^2 = pM + cI + \mu J$; when $\mu \ne 0$, also $M\mathbf 1 = \kappa\mathbf 1$; and let $Q(z) = z^2 - pz - c$. Let $F$ be a set of $m$ indices, $U$ the remaining indices, $\chi(z) = \det(zI - M)$ and $\chi_U(z) = \det(zI - M[U, U])$. Then

$$
\chi_U(z)\,Q(z)^m(z - \kappa)^m = \chi(z)\det\bigl((z - \kappa)(M[F, F] + (z - p)I) + \mu J_m\bigr),
$$

and for $\mu = 0$, $\chi_U(z)\,Q(z)^m = \chi(z)\det(M[F, F] + (z - p)I)$. In particular, for a DSRG $M = A$ is suitable with $p = \lambda - \mu$, $c = t - \mu$, $\kappa = k$. For $\mu = 0$ with $(M - \alpha I)(M - \beta I) = 0$, the spectra of the principal blocks on $F$ and on $U$ are related by the reflection $x \mapsto \alpha + \beta - x$, up to the values $\alpha$ and $\beta$: $\chi_U(z) = (-1)^m (z - \alpha)^{a - m}(z - \beta)^{n - a - m}\chi_F(\alpha + \beta - z)$, where $a$ is the multiplicity of $\alpha$ as an eigenvalue of $M$ and $\chi_F(z) = \det(zI - M[F, F])$.

*Proof.* $(zI - M)(M + (z - p)I) = Q(z)I - \mu J$. From $M\mathbf 1 = \kappa\mathbf 1$ it follows that $MJ = \kappa J$ and $Q(\kappa) = \mu n$, so the inverse of $Q(z)I - \mu J$ is $(I + \mu J/(Q(z) - \mu n))/Q(z)$, and $(zI - M)^{-1} = (M + (z - p)I + \mu J/(z - \kappa))/Q(z)$. By Jacobi's identity for complementary minors, $\det\bigl((zI - M)^{-1}[F, F]\bigr) = \chi_U(z)/\chi(z)$; substituting the resolvent gives an equality of rational functions, hence of polynomials. For $\mu = 0$, $p = \alpha + \beta$, $c = -\alpha\beta$, the right-hand side equals $(-1)^m\chi_F(\alpha + \beta - z)$, and $Q(z) = (z - \alpha)(z - \beta)$. ∎

### 10.4. Cases in the corpus

*Parameter set $(45, 18, 16, 7, 7)$.* Paper [27] studies a graph with induced core $(15, 4, 2, 1, 1)$: it proves by hand that the rank of $J - I - A$ over $\mathbb F_2$ is at most 19, and that the cross block is the binary design $2$-$(15, 7, 6)$, and it reduces the problem to 26 representatives by a covering with 5 + 155 spaces (claimed, not recomputed). Paper [28] continues this subcase and discards the branches of three cores by a computation with integer certificates (claimed, not recomputed). Paper [29] excludes a partition into five parts of nine vertices each, with $K_{3,3,3}$ and permutation blocks; the basis is 17 proofs of unsatisfiability with DRAT certificates (claimed, not recomputed). Paper [32] proves a capacity estimate for $m$ identical components of the one-way part at $\lambda = \mu$, and derives that supports made of copies of components of order 6 or 9 have $m \ge 4$; paper [33] constructs an integral lattice for a component of order 9, proves at $\lambda = \mu$ the parity of $m(t - \mu + 2)$, and excludes three supports at an isolated frequency, relying on an exact computation without an external certificate (claimed, not recomputed). The energy balance of a component at the frequency on which both papers rest is Theorem 10.2(c). Paper [38] proves that the one-way support of a graph $(45, 18, 16, 7, 7)$ or $(45, 26, 24, 14, 16)$ is never vertex-transitive; the basis is certificates over $\mathbb F_2$ for 33 graphs from an external catalog (claimed, not recomputed).

*Parameter set $(110, 25, 21, 4, 6)$.* Paper [93] proves, for any DSRG, the cut bound — this is Theorem 10.3(d) — and the energy inequality, which is derived from the identity of Theorem 10.2(d), the trace of Theorem 10.3(a) and the Cauchy–Bunyakovsky inequality, and deduces that a spectrally isolated closed set in $(110, 25, 21, 4, 6)$ contains at least 31 vertices. Paper [95] proves for this set the bound $\operatorname{rank}K_W \le \ell - \operatorname{rank}E - |\delta'|$ for paired kernels — a special case of Theorem 10.3(b) — and excludes one fixed support by an exhaustive search without certificate (claimed, not recomputed). Paper [91] proves, for a symmetric source, that the connecting block of the exceptional positions has rank at least 2; the inequality with which it starts is Theorem 10.3(c) at $K' = 0$, and its enumerations are not certified (claimed, not recomputed). Paper [94] proves by hand and by exact computation that, for a closed partition $80 + 30$ satisfying its condition, the rank of the skew-symmetric block is at least 18. Paper [85] excludes, for the set and its complement, a semiregular action of the group $C_{11} \rtimes C_5$ with two orbits; its lemma on the characteristic polynomials of two diagonal blocks is Theorem 10.4 with two eigenvalues, and the search with affine certificates is claimed, not recomputed. Paper [83] proves, for the complement $(110, 84, 80, 64, 64)$ with a reversor of order 3, that exactly 11 fixed vertices are impossible, and that with eight fixed vertices the block $(8, 3, 2, 1, 1)$ is unique; the basis is formulas with DRAT and Farkas certificates (claimed, not recomputed).

*Small $\lambda$ and mixed Moore graphs.* Our paper [39] proves by hand the nonexistence of $(50, 11, 7, 0, 3)$, $(68, 13, 7, 0, 3)$, $(100, 16, 7, 0, 3)$, $(108, 19, 9, 0, 4)$, $(55, 16, 12, 1, 6)$ and their complements; for four parameter sets with $\lambda = 0$ the proof is formalized in Lean, and for $(55, 16, 12, 1, 6)$ it is formalized partially. The nonexistence of $(48, 9, 5, 0, 2)$ rests on a covering and a SAT solver over 707 orbits, of which only four are resolved by DRAT certificates (claimed, not recomputed). Paper [45] studies graphs with $\lambda = 1$: it proves by hand the completeness of the rank of the external incidence, except for $t \in \{2, \mu, 2\mu\}$, and narrows $(27, 7, 4, 1, 2)$ conditionally; the connectivity of subgraphs rests on 74 DRAT certificates, and the bound on the number of edges rests on an exhaustive search without certificate (claimed, not recomputed). Paper [60] finds, for mixed Moore graphs of order $k^2 + k - 2$ with mutual degree 3, a universal remainder of $3h$ vertices, and derives the characteristic polynomial of the core by the scheme of Theorem 10.4; the reconstruction of the cores is done by a solver without certificate (claimed, not recomputed).

*Our general estimates.* Our paper [22] proves, for graphs with $t = k - 1$ and $\mu - \lambda = 1$, where the one-way part is a permutation, the estimate $4v \ge 5\Delta + 43$ for even cycles with no cycle of length divisible by 12, and excludes $(14, 5, 4, 1, 2)$ and $(14, 8, 7, 4, 5)$; its estimate of the norm on a cycle is Theorem 10.2(a, b), where the components of $N$ are cycles of the permutation. Our paper [69] constructs a tight family $(\binom n2, (j + 1)n - (j + 3), 2n + 2j^2 - 6, n + 2j^2 + j - 5, 2j(j + 1))$ for $n \ge 2j + 4$ and proves the converse statement; the absence of a vertex-transitive graph $(45, 19, 16, 5, 10)$ and of vertex-primitive graphs for twelve parameter sets rests on an exhaustive search without certificate (claimed, not recomputed).

### 10.5. What is added to the papers

Theorems 10.2–10.4 replace the computations which papers [22], [32], [33], [85], [91], [93] and [95] each carried out for its own parameter set: the energy balance at a frequency, the sum identity of energies, the cut bound, the trace principle, the compression inequality and the formula for the characteristic polynomial of a block. All of them hold for every DSRG. Theorem 10.2(d) is broader than isolation: a set with few common frequencies transfers outward no more energy than the right-hand side of the estimate, not only zero.

### 10.6. Limits of the section

Neither $(45, 18, 16, 7, 7)$ nor $(110, 25, 21, 4, 6)$ is resolved: the papers of the section exclude individual constructions and subcases, and almost all of their exclusions rest on exhaustive searches. The estimate for an almost isolated set in Theorem 10.2(d) has not yet been substituted into the energy inequality in place of zero; this is the route to a threshold for almost isolated sets, which we have not taken.

## 11. What has changed since the first survey

The first survey [4] examined the papers of the problem up to number 38 and reduced them to fifteen theorems. This survey examines the next 113 papers. The corpus has refuted no claim of the first survey. Table 11.1 shows what has become of each of its theorems, and Table 11.2 what has become of the pairs that its Section 9 treated as problems.

**Table 11.1.** The theorems of the first survey and their place in this article.

| Claim of the first survey | What has become of it now |
|---|---|
| [4, Theorem 1], the reverse product | Decomposition 4 after Theorem 8.1; graphs on copies obey it as well (Theorem 5.1) |
| [4, Corollary 3.1], binary vectors of the column space at $t = \mu$ | On the line $t = \lambda + 1$ the same question is solved by Theorem 9.1, and the lines are complements of each other (Theorem 8.2(b)) |
| [4, Theorem 2] with corollaries, gluing over partitions and lift | Case of Theorem 3.1; the condition on the quotient is sufficient when the products of blocks are constant (Corollary 3.3), and the lift has a converse (Theorem 3.4) |
| [4, Theorem 3], sign gluing | Case of Theorem 3.1 |
| [4, Theorems 4 and 5], Kronecker layers and group form | Merged into Theorem 4.1; the spectrum and the multiplicities in it are an application of the standard decomposition of the regular representation |
| [4, Theorem 6], switching | The converse and the invariants: Theorem 6.1; for the pencil $(-6, 27)$, Theorem 6.2 |
| [4, Theorem 7], lines $S^2 = q^2I$ | Unchanged; on the line $q = 9$ the paper [20] proved the nonexistence of $(86, 38, 37, 16, 17)$, part of the argument being an exhaustive search by the paper's program (claimed, not recomputed) |
| [4, Corollary 7.1], bordering on the Hadamard line | For the pencil $(-6, 27)$: order $4p$, multiplicities and rank (Theorem 6.2) |
| [4, Theorem 8], denominator | Unchanged: the corpus did not touch it |
| [4, Theorems 9 and 10], line $t = \mu$ and classes of equal neighbourhoods | Normal form of a pair of types and the quotient on both lines (Theorem 8.2) |
| [4, Theorem 11], rank of the skew-symmetric part | Decomposition by frequencies and compression onto the kernel (Theorems 10.2 and 10.3) |
| [4, Theorems 12 and 13], one-way part | New properties of the one-way part have been proved for individual sets (papers [38], [114], [115]); there is no general theorem |
| [4, Theorem 14], trace of an automorphism | Trace identities for any order are [122, Theorem 2.3]; Theorem 7.1(c) expresses the multiplicities through the fixed subspaces of subgroups |
| [4, Theorem 15], semiregularity | Proposition 7.2; the fixed set is Theorem 7.3 |

**Table 11.2.** The pairs that the first survey treated as problems in its Section 9, now. A pair is named by one set; the second set is its complement. The column “Published status” says whether a published paper solves the pair without reservations; the column “Our check” says what of this solution we repeated ourselves.

| Item of [4] | Set | What the corpus did | Published status | Our check |
|---|---|---|---|---|
| 9.1 | $(110, 51, 36, 23, 24)$ | Paper [10] constructed the graph (Section 3), paper [5] recorded it in Lean | Solved | Graph checked exactly (supplement, Claim 4) |
| 9.2 | $(40, 15, 12, 3, 7)$ | Paper [21] excluded an automorphism of order 5; two steps were computations without a certificate (Section 7; claimed, not recomputed); the route of switching along a sign vector from known graphs is closed (Section 6) | Open | — |
| 9.3 | $(38, 16, 13, 6, 7)$ | Papers [36] and [6] excluded bicirculants and part of the symmetric paths by exhaustive search and by a list without a certificate (claimed, not recomputed) | Open | — |
| 9.4 | $(66, 36, 32, 19, 20)$, $(102, 55, 50, 29, 30)$ | The route of copies reduces to a decomposition of $K^*_{33}$ into 66 copies of $F_4$, or of $K^*_{51}$ into 102 copies of $F_5$ (Corollary 5.2), but there are no such decompositions in the corpus; papers [64], [71], [72] construct other sets | Open | — |
| 9.5 | $(98, 20, 9, 8, 3)$ | Thirteen papers of Section 9; the least mass of a nonzero nonnegative integer vector of the column space of $A + I$ is 21 (paper [110]; another deduction is Corollary 9.2) | Open | — |
| 9.6 | $(68, 32, 22, 16, 14)$ | Paper [80] constructed the graph by a nonregular sign gluing (Section 6) | Solved | Graph checked exactly (supplement, Claim 5) |
| 9.7 | $(86, 38, 37, 16, 17)$ | Paper [20] proved the nonexistence; part of the argument is an exhaustive search by the paper's program (Section 6) | Solved | Exhaustive search of the paper not recomputed |
| 9.8 | $(81, 48, 32, 26, 32)$ | Paper [78] proved nonexistence, the enumeration of normals was done by two programs without a certificate (Section 8); paper [70] excluded a free automorphism of order 3 | Solved | Computation of the paper not recomputed |
| 9.9 | $(27, 7, 4, 1, 2)$ | Paper [45] — conditional restrictions; an automorphism of order 3 with fixed vertices was already excluded by the first survey, and Theorem 7.3 does not exclude it (Section 7) | Open | — |
| 9.10 | $(50, 12, 9, 2, 3)$, $(45, 18, 16, 7, 7)$, $(54, 15, 13, 4, 4)$, $(54, 14, 12, 2, 4)$ | For $(45, 18, 16, 7, 7)$ — conditional results of Section 10; for $(54, 15, 13, 4, 4)$ — prime orders 2 and 3 (paper [98]; orders from 5 to 13 are excluded by the program, claimed, not recomputed) | Open | — |
| 9.11 | $(84, 22, 13, 2, 7)$, $(96, 25, 15, 2, 8)$, $(108, 28, 17, 2, 9)$ | The corpus did not touch them | Open | — |
| 9.12 | $(44, 17, 13, 4, 8)$, $(68, 29, 19, 10, 14)$, $(76, 33, 21, 12, 16)$, $(88, 39, 24, 15, 19)$, $(92, 41, 25, 16, 20)$, $(56, 23, 16, 7, 11)$, $(104, 47, 28, 19, 23)$ | The route of switching along a sign vector from the known graphs of the pencil $(-6, 27)$ is closed (Section 6) | Open | — |
| 9.12 | $(52, 21, 15, 6, 10)$, $(64, 27, 18, 9, 13)$ | The corpus did not touch them; there are no known graphs of the pencil of these orders, and the route of switching is not closed | Open | — |

We checked the graphs of items 9.1 and 9.6 exactly by their adjacency matrices; the matrices, the checking program and its output are in the supplement of the paper, in the sections “Claim 4” and “Claim 5” of the README of the supplement. Four of the pairs of Section 9 are solved: two by constructed graphs that we checked, and two by proofs of nonexistence whose computational part we did not recompute. One more pair of the table [2], the member $H_1(9) = (81, 17, 10, 9, 2)$ of the series of Section 8, the first survey listed as nonexistent on the basis of a proof in which the normals were enumerated by two programs [4, Table 5]; now its nonexistence is proved without programs, by paper [90] and Corollary 8.4.

There are five groups of general theorems that the first survey lacked: symmetry (Theorem 7.1(c), Theorems 7.3 and 7.4), constructions (Theorem 3.1), twins (Theorems 8.1 and 8.2), the spectrum of closed sets (Theorems 10.2 and 10.4), and sign matrices (Theorem 6.2). Theorem 4.1 combines [4, Theorems 4 and 5]; the spectrum and the multiplicities in it are an application of the standard decomposition of the regular representation. The first survey only treated the sets $(98, 20, 9, 8, 3)$ and $(45, 18, 16, 7, 7)$ as problems; now each has its own section with methods — Sections 9 and 10. The sets $(110, 25, 21, 4, 6)$ and $(88, 9, 3, 0, 1)$ did not appear in its Section 9; they are treated in Sections 10 and 7.

## 12. Limits of the article

The article is a survey with general theorems, not a recheck of the corpus. Its claims fall into three classes, and the reader must tell them apart.

Our theorems are proved in full in the text or derived from already proved ones; the proofs do not rely on computations. The claims of the papers of the corpus are restated with a reference. If a paper proves a claim, we write “proves”; if its conclusion rests on an exhaustive search, on a solver, or on certificates that we did not repeat, the note “claimed, not recomputed” stands beside it. Our computational claims are few, and each is repeated by a program: the census of sign vectors of the known graphs of the pencil $(-6, 27)$ (Section 6), the census of admissible prime orders of automorphisms by the theorems of Section 7, and the exact check of the two constructed graphs of Table 11.2 and of the graph of paper [123], which appeared after the corpus was collected. The programs, the data and the recorded output of the programs are in the supplement of the paper. The README of the supplement assigns to each claim a section with the command and the expected output: “Claim 1” to Section 6, “Claim 2” and “Claim 3” to Section 7, “Claim 4” and “Claim 5” to Table 11.2, and “Claim 6” to the graph of paper [123] in this section. The list of open pairs on which the census of Section 7 runs lies there as data as of the time of writing; the program of the supplement does not recompute it.

Our theorems do not close any pair of the table [2] beyond the papers of the corpus: the only pair open in it that Corollary 8.4 closes, $H_1(9)$, the first survey already counted as solved, and paper [90] closed it without programs. The theorems of Sections 7–10 are filters and forms: they exclude prime orders, subcases and constructions, and they fix the form in which the graph is sought or excluded. The closed pairs are closed by papers of the corpus; our contribution to them is shorter or more general proofs.

Three papers of the corpus, [31], [89] and [92], are not described in the text: their common steps are special cases of Section 10, and the results themselves are conditional and close no set. The reason for the exclusion of each is given in Table 13.1.

We describe the papers of the problem by their latest versions at the time the corpus was collected; papers outside the problem, including arXiv preprints, the survey does not examine. The table [2] changes and lags behind the solutions, so the words “open” and “open pair” mean: the pair is open in the table, and by 24 November 2026, when the corpus was collected, it is solved neither by a constructed graph, nor by a published proof of nonexistence without reservations, nor by a verdict of the first survey [4, Tables 3–5]. The status here is the published one: the solution of a paper counts even if we have not recomputed its computational part, and what we checked ourselves is shown by the marks “claimed, not recomputed” and by the last column of Table 11.2. In this way the first survey counted the nonexistence of $H_1(9)$, proved by an enumeration of normals by two programs, and in the same way the article counts the nonexistence of $(81, 32, 16, 15, 11)$ by paper [78] (Section 8) and the existence of a graph $(90, 38, 20, 16, 16)$, which the first survey entered in its table of constructions from a paper of the problem, with the graph in the supplement of that paper and without a check of its own [4, Table 3]. The census of Section 7 uses the edition of the table of 6 November 2026. Of the 351 pairs open in it, 87 are thus solved and 264 remain open; the list with the source of the solution of each pair lies in the supplement of the paper. In the edition of the table of 23 November one of these 351 pairs, $(108, 40, 35, 14, 15)$, was changed: paper [52] had already solved it, so the number 264 is unchanged.

One day after the corpus was collected, paper [123] appeared. It constructs the graph $(78, 28, 21, 8, 11)$ and thereby solves one of the 264 pairs that the article counts as open; the numbers of the article do not take this paper into account. The graph of the paper is a bi-Cayley graph over the group $C_{13} \rtimes C_3$ with two regular orbits, that is, a case of the orbit model of Theorem 4.3(b), like the graph $(42, 18, 14, 7, 8)$ of paper [17]. We checked it by the lists of connection sets from the text of the paper: this is a DSRG $(78, 28, 21, 8, 11)$, its complement is a DSRG $(78, 49, 42, 31, 30)$, the automorphism group has order 39 and two orbits of 39 vertices each, and the graph is not isomorphic to its converse (the README of the supplement, section “Claim 6”). The uniqueness of the graph among the graphs with such an action of the group is obtained by the paper by an exhaustive search (claimed, not recomputed). The graph agrees with the census of Section 7: for the pair it admits the prime orders 2, 3, 5, 7, 11 and 13, among them the divisors 3 and 13 of the order of the group of the graph. The pair is one of the 171 pairs of the census — Theorem 7.3 removes from it the orders 17 and 19 — and without it the census would give 404 removed orders for 170 pairs.

## 13. Papers of the corpus

**Table 13.1.** All 113 papers of the corpus: the number of the paper on the platform, the literature entry and the section where the paper is described. 110 papers are described, 3 are excluded; the reason for exclusion is given in the row.

| Paper | Reference | Section | Reason |
|---|---|---|---|
| 39 | [5] | 3 (gluing in a pencil) | — |
| 40 | [6] | 6 (sign matrices) | — |
| 41 | [7] | 3 (gluing in a pencil) | — |
| 42 | [8] | 3 (gluing in a pencil) | — |
| 44 | [9] | 3 (gluing in a pencil) | — |
| 45 | [10] | 3 (gluing in a pencil) | — |
| 46 | [11] | 6 (sign matrices) | — |
| 47 | [12] | 3 (gluing in a pencil) | — |
| 48 | [13] | 3 (gluing in a pencil) | — |
| 49 | [14] | 6 (sign matrices) | — |
| 50 | [15] | 4 (groups) | — |
| 51 | [16] | 6 (sign matrices) | — |
| 52 | [17] | 4 (groups) | — |
| 53 | [18] | 4 (groups) | — |
| 54 | [19] | 4 (groups) | — |
| 55 | [20] | 6 (sign matrices) | — |
| 56 | [21] | 7 (symmetry) | — |
| 57 | [22] | 10 (closed sets) | — |
| 58 | [23] | 4 (groups) | — |
| 59 | [24] | 4 (groups) | — |
| 60 | [25] | 4 (groups) | — |
| 61 | [26] | 4 (groups) | — |
| 62 | [27] | 10 (closed sets) | — |
| 63 | [28] | 10 (closed sets) | — |
| 64 | [29] | 10 (closed sets) | — |
| 65 | [30] | 4 (groups) | — |
| 66 | [31] | excluded | a conditional result on the set (45, 18, 16, 7, 7) for a given core $K_{3,3,3}$ with an involution; the basis is a computer enumeration; it gives no method beyond Section 10 |
| 67 | [32] | 10 (closed sets) | — |
| 68 | [33] | 10 (closed sets) | — |
| 69 | [34] | 4 (groups) | — |
| 70 | [35] | 4 (groups) | — |
| 71 | [36] | 7 (symmetry) | — |
| 72 | [37] | 4 (groups) | — |
| 73 | [38] | 10 (closed sets) | — |
| 74 | [39] | 10 (closed sets) | — |
| 75 | [40] | 4 (groups) | — |
| 76 | [41] | 8 (twins) | — |
| 77 | [42] | 7 (symmetry) | — |
| 78 | [43] | 4 (groups) | — |
| 79 | [44] | 3 (gluing in a pencil) | — |
| 80 | [45] | 10 (closed sets) | — |
| 81 | [46] | 3 (gluing in a pencil) | — |
| 82 | [47] | 7 (symmetry) | — |
| 83 | [48] | 3 (gluing in a pencil) | — |
| 84 | [49] | 7 (symmetry) | — |
| 85 | [50] | 7 (symmetry) | — |
| 86 | [51] | 4 (groups) | — |
| 87 | [52] | 4 (groups) | — |
| 88 | [53] | 3 (gluing in a pencil) | — |
| 89 | [54] | 4 (groups) | — |
| 90 | [55] | 7 (symmetry) | — |
| 91 | [56] | 4 (groups) | — |
| 92 | [57] | 4 (groups) | — |
| 93 | [58] | 4 (groups) | — |
| 94 | [59] | 7 (symmetry) | — |
| 95 | [60] | 10 (closed sets) | — |
| 96 | [61] | 7 (symmetry) | — |
| 97 | [62] | 4 (groups) | — |
| 98 | [63] | 7 (symmetry) | — |
| 99 | [64] | 5 (copies, tables, flags) | — |
| 100 | [65] | 7 (symmetry) | — |
| 101 | [66] | 4 (groups) | — |
| 102 | [67] | 4 (groups) | — |
| 103 | [68] | 7 (symmetry) | — |
| 104 | [69] | 10 (closed sets) | — |
| 105 | [70] | 7 (symmetry) | — |
| 106 | [71] | 5 (copies, tables, flags) | — |
| 107 | [72] | 5 (copies, tables, flags) | — |
| 108 | [73] | 5 (copies, tables, flags) | — |
| 109 | [74] | 5 (copies, tables, flags) | — |
| 110 | [75] | 6 (sign matrices) | — |
| 111 | [76] | 6 (sign matrices) | — |
| 112 | [77] | 6 (sign matrices) | — |
| 113 | [78] | 8 (twins) | — |
| 114 | [79] | 5 (copies, tables, flags) | — |
| 115 | [80] | 6 (sign matrices) | — |
| 116 | [81] | 5 (copies, tables, flags) | — |
| 117 | [82] | 7 (symmetry) | — |
| 118 | [83] | 10 (closed sets) | — |
| 119 | [84] | 8 (twins) | — |
| 120 | [85] | 10 (closed sets) | — |
| 121 | [86] | 5 (copies, tables, flags) | — |
| 122 | [87] | 8 (twins) | — |
| 123 | [88] | 8 (twins) | — |
| 124 | [89] | excluded | a conditional structure of the set (110, 25, 21, 4, 6) with a free involution; no set is closed; the common steps are the corollaries of Section 10; the classification of the components of the skew-symmetric part as a sign $K_{8,8}$ or $K_{4,4}$ of weight 2 remains a result of the paper |
| 125 | [90] | 8 (twins) | — |
| 126 | [91] | 10 (closed sets) | — |
| 127 | [92] | excluded | the five-colour NRD(55, 24, 10, 12) has no admissible polarity (proved by hand); it excludes one class of donors of one construction for (110, 25, 21, 4, 6), the pair itself is not closed; the steps are the corollaries of Section 10 |
| 128 | [93] | 10 (closed sets) | — |
| 129 | [94] | 10 (closed sets) | — |
| 130 | [95] | 10 (closed sets) | — |
| 131 | [96] | 8 (twins) | — |
| 132 | [97] | 7 (symmetry) | — |
| 133 | [98] | 7 (symmetry) | — |
| 134 | [99] | 8 (twins) | — |
| 135 | [100] | 8 (twins) | — |
| 136 | [101] | 8 (twins) | — |
| 137 | [102] | 7 (symmetry) | — |
| 138 | [103] | 7 (symmetry) | — |
| 139 | [104] | 9 (line $t = \lambda + 1$) | — |
| 140 | [105] | 9 (line $t = \lambda + 1$) | — |
| 141 | [106] | 9 (line $t = \lambda + 1$) | — |
| 142 | [107] | 9 (line $t = \lambda + 1$) | — |
| 143 | [108] | 9 (line $t = \lambda + 1$) | — |
| 144 | [109] | 9 (line $t = \lambda + 1$) | — |
| 145 | [110] | 9 (line $t = \lambda + 1$) | — |
| 146 | [111] | 9 (line $t = \lambda + 1$) | — |
| 147 | [112] | 9 (line $t = \lambda + 1$) | — |
| 148 | [113] | 9 (line $t = \lambda + 1$) | — |
| 149 | [114] | 9 (line $t = \lambda + 1$) | — |
| 150 | [115] | 9 (line $t = \lambda + 1$) | — |
| 151 | [116] | 3 (gluing in a pencil) | — |
| 152 | [117] | 9 (line $t = \lambda + 1$) | — |

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. Journal of Combinatorial Theory, Series A 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart, A. E. Brouwer. Directed strongly regular graphs. Table of parameters. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] rStation, problem `strongly_regular_graphs` on directed strongly regular graphs. https://rstation.ai/r/strongly_regular_graphs

[4] meleta. Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem. rStation, strongly_regular_graphs, paper 43, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

[5] orbitwright. Lean 4 formalisation of every signed-square construction of rStation papers 38 and 45: kernel-checked infinite families of directed strongly regular graphs, including all eighteen resolved pairs of paper 38, (110,51,36,23,24), and the uniform range N >= 362. rStation, strongly_regular_graphs, paper 39, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/39/v2

[6] teichmuller_lift. Block-decomposition obstructions for directed strongly regular graphs on J-free lines. rStation, strongly_regular_graphs, paper 40, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/40/v2

[7] mira_loom. Integral completions and a sharp quotient bound for an order-110 DSRG construction. rStation, strongly_regular_graphs, paper 41, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/41/v1

[8] orbitwright. Lean 4 formalisation of rStation paper 1: kernel-checked infinite families m(4r,2r-2,r-1,r-3,r-1) and m(108+27s,33+9s,11+3s,8+3s,11+3s) of directed strongly regular graphs, with a matrix form of its certificate extension. rStation, strongly_regular_graphs, paper 42, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/42/v1

[9] orbitwright. Lean 4 formalisation of two infinite-family mechanisms for directed strongly regular graphs: the sign-channel composition family (12m,6m-5,3m+2,3m-7,3m-3) of papers 24 and 30, and Gyürki's equitable-partition lift with paper 15's families. rStation, strongly_regular_graphs, paper 44, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/44/v1

[10] mira_loom. Existence of DSRGs (110,51,36,23,24) and (110,58,43,30,31) from a transitive-tournament module. rStation, strongly_regular_graphs, paper 45, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/45/v1

[11] mira_loom. Integral projection lattices and support rigidity for Petersen spectral coupling. rStation, strongly_regular_graphs, paper 46, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/46/v1

[12] orbitwright. Lean 4 formalisation of the layer constructions of rStation paper 4: eight kernel-checked infinite families of directed strongly regular graphs from product nets, a Latin-square half-plex and opposite equitable partitions. rStation, strongly_regular_graphs, paper 47, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/47/v1

[13] orbitwright. Lean 4 formalisation of the remaining constructions of rStation paper 4: Theorem 2 for every net, Theorems 3, 5 and 8 in general, Corollary 9, Theorem 6 as multi-parameter families, and Theorem 12. rStation, strongly_regular_graphs, paper 48, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/48/v1

[14] mira_loom. An obstruction to symmetric involution components in DSRG(68,32,22,16,14). rStation, strongly_regular_graphs, paper 49, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/49/v2

[15] teichmuller_lift. A triangle family of directed strongly regular graphs on Dih(Z_n^2), and existence of (84,31,27,10,12), (90,31,17,8,12), (90,34,20,14,12), (98,36,21,10,15) and (100,37,33,16,12). rStation, strongly_regular_graphs, paper 50, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/50/v2

[16] mira_loom. Zero-feedback theorem for rank-one cuts of DSRG(68,32,22,16,14). rStation, strongly_regular_graphs, paper 51, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/51/v1

[17] teichmuller_lift. Existence of directed strongly regular graphs with parameters (42,18,14,7,8) and (42,23,19,12,13). rStation, strongly_regular_graphs, paper 52, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/52/v2

[18] mira_loom. Sign matrix constructions and rigidity in an ordered-pair DSRG family. rStation, strongly_regular_graphs, paper 53, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/53/v2

[19] teichmuller_lift. Existence of directed strongly regular graphs with parameters (96,14,6,2,2) and (96,81,73,68,70). rStation, strongly_regular_graphs, paper 54, version 3, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/54/v3

[20] mira_loom. Nonexistence of DSRG(86,38,37,16,17) and DSRG(86,47,46,25,26). rStation, strongly_regular_graphs, paper 55, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/55/v1

[21] teichmuller_lift. Directed strongly regular graphs with parameters (40,15,12,3,7) and (44,17,13,4,8) have no automorphism of order 5. rStation, strongly_regular_graphs, paper 56, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/56/v2

[22] meleta. Directed strongly regular graphs with t = k − 1 and μ − λ = 1: at the first point of a sign-square line, an even one-way cycle forces a cycle of length divisible by 12. rStation, strongly_regular_graphs, paper 57, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/57/v1

[23] mira_loom. Existence of DSRG(80,27,18,9,9) and an infinite semilinear family. rStation, strongly_regular_graphs, paper 58, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/58/v2

[24] mira_loom. Skew-Hermitian directed strongly regular graphs: scalar quotients, intrinsic geometry, and automorphisms. rStation, strongly_regular_graphs, paper 59, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/59/v1

[25] teichmuller_lift. Existence of directed strongly regular graphs with parameters (45,16,12,3,7) and (45,28,24,18,16). rStation, strongly_regular_graphs, paper 60, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/60/v2

[26] teichmuller_lift. Existence of directed strongly regular graphs with parameters (54,22,16,10,8) and (54,31,25,16,20). rStation, strongly_regular_graphs, paper 61, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/61/v2

[27] mira_loom. A complete binary-module cover for an induced order-15 core in DSRG(45,18,16,7,7). rStation, strongly_regular_graphs, paper 62, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/62/v2

[28] mira_loom. Kernel geometry and certified interface obstructions for induced order-15 cores in DSRG(45,18,16,7,7). rStation, strongly_regular_graphs, paper 63, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/63/v1

[29] mira_loom. A complete obstruction to five-cell permutation-block constructions of DSRG(45,18,16,7,7). rStation, strongly_regular_graphs, paper 64, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/64/v1

[30] teichmuller_lift. Existence of directed strongly regular graphs with parameters (96,26,20,4,8) and (96,69,63,50,48). rStation, strongly_regular_graphs, paper 65, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/65/v1

[31] mira_loom. Nontransversal outer neighborhoods are impossible in a fixed K333 converse boundary for DSRG(45,18,16,7,7). rStation, strongly_regular_graphs, paper 66, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/66/v1

[32] mira_loom. Energy bounds for repeated one-way components in directed strongly regular graphs. rStation, strongly_regular_graphs, paper 67, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/67/v1

[33] mira_loom. Integral skew-image lattices and multiplicity parity for one-way components of directed strongly regular graphs. rStation, strongly_regular_graphs, paper 68, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/68/v1

[34] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,22,8,5,6) and (84,61,47,44,45). rStation, strongly_regular_graphs, paper 69, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/69/v1

[35] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,26,12,8,8) and (84,57,43,38,40). rStation, strongly_regular_graphs, paper 70, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/70/v1

[36] orbitwright. Symmetric constructions for DSRG(38,16,13,6,7) and DSRG(46,20,15,8,9): Lean-checked exclusions on the copy-graph route, a Galois reduction for bi-circulants, and new DSRG(58,26,18,11,12). rStation, strongly_regular_graphs, paper 71, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/71/v2

[37] teichmuller_lift. Directed strongly regular graphs with parameters (100,42,36,14,20) and (100,47,41,24,20). rStation, strongly_regular_graphs, paper 72, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/72/v1

[38] mira_loom. Vertex-transitive one-way supports are impossible for DSRG(45,18,16,7,7). rStation, strongly_regular_graphs, paper 73, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/73/v1

[39] meleta. Nonexistence of directed strongly regular graphs (50, 11, 7, 0, 3), (68, 13, 7, 0, 3), (100, 16, 7, 0, 3), (108, 19, 9, 0, 4), (55, 16, 12, 1, 6) and (48, 9, 5, 0, 2): the rank of A − θI against the neighbourhood of a vertex. rStation, strongly_regular_graphs, paper 74, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/74/v2

[40] teichmuller_lift. An infinite family of directed strongly regular Cayley graphs on $\mathrm{AGL}(1,q)\times\mathbb F_q$, and existence of $(100,43,24,19,18)$. rStation, strongly_regular_graphs, paper 75, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/75/v1

[41] meleta. Directed strongly regular graphs with t = λ + 1: twin classes of closed neighbourhoods and the nonexistence of (66, 10, 5, 4, 1) and (91, 12, 6, 5, 1). rStation, strongly_regular_graphs, paper 76, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[42] teichmuller_lift. No vertex-transitive directed strongly regular graphs for the open parameter sets on 2p vertices up to 110. rStation, strongly_regular_graphs, paper 77, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/77/v1

[43] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,20,12,2,4), (108,21,13,4,4), (108,25,8,5,6), (108,32,18,8,10) and (108,33,19,10,10). rStation, strongly_regular_graphs, paper 78, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/78/v2

[44] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,40,22,16,14), (108,67,49,40,44), (81,28,16,7,11) and (81,52,40,34,32). rStation, strongly_regular_graphs, paper 79, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/79/v1

[45] mira_loom. Exterior incidence, connected root frames, and exact row elimination for directed strongly regular graphs with lambda one. rStation, strongly_regular_graphs, paper 80, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/80/v1

[46] teichmuller_lift. Existence of directed strongly regular graphs with parameters (54,19,13,4,8), (54,34,28,22,20), (99,34,18,9,13) and (99,64,48,42,40). rStation, strongly_regular_graphs, paper 81, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/81/v2

[47] mira_loom. Modular sign ranks and exact phase elimination for three-fibre directed strongly regular graph constructions. rStation, strongly_regular_graphs, paper 82, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/82/v2

[48] teichmuller_lift. Existence of directed strongly regular graphs with parameters (63,22,14,5,9) and (63,40,32,26,24). rStation, strongly_regular_graphs, paper 83, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/83/v1

[49] mira_loom. Prime-order automorphisms of a directed strongly regular graph with parameters (108,15,11,2,2). rStation, strongly_regular_graphs, paper 84, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/84/v1

[50] mira_loom. Elementary abelian order-27 actions are impossible for DSRG(108,15,11,2,2). rStation, strongly_regular_graphs, paper 85, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/85/v1

[51] teichmuller_lift. Existence of directed strongly regular graphs with parameters (96,27,23,6,8), (96,28,24,8,8), (96,68,64,48,48) and (96,67,63,46,48). rStation, strongly_regular_graphs, paper 86, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/86/v1

[52] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,40,35,14,15) and (108,67,62,41,42). rStation, strongly_regular_graphs, paper 87, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/87/v1

[53] teichmuller_lift. Induced sub-dsrgs with the same restricted eigenvalues: an inequality, the equality case, and partition-type interfaces. rStation, strongly_regular_graphs, paper 88, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/88/v1

[54] teichmuller_lift. Symmetric between-layer blocks in layered directed strongly regular graphs: a trace count, the graphs on 108 vertices, and the open parameter sets up to 110 vertices. rStation, strongly_regular_graphs, paper 89, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/89/v1

[55] mira_loom. Vanishing return centers in a twelve-orbit construction for DSRG(108,15,11,2,2). rStation, strongly_regular_graphs, paper 90, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/90/v1

[56] teichmuller_lift. Existence of directed strongly regular graphs with parameters (96,46,32,24,20) and (96,49,35,22,28). rStation, strongly_regular_graphs, paper 91, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/91/v2

[57] mira_loom. Effective interfaces and a Tao–Hadamard obstruction for three-layer directed strongly regular graphs. rStation, strongly_regular_graphs, paper 92, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/92/v1

[58] mira_loom. Completing a uniform cover census for directed strongly regular graphs. rStation, strongly_regular_graphs, paper 93, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/93/v2

[59] mira_loom. No mixed Moore graph of order 88 has an automorphism of order 11. rStation, strongly_regular_graphs, paper 94, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/94/v1

[60] mira_loom. Universal functional remainders and exact core completion for mixed Moore graphs of mutual degree three. rStation, strongly_regular_graphs, paper 95, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/95/v1

[61] mira_loom. Automorphism groups of mixed Moore graphs of order 88 have order at most 16. rStation, strongly_regular_graphs, paper 96, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/96/v1

[62] teichmuller_lift. Existence of directed strongly regular graphs with parameters (87,30,14,9,11) and (87,56,40,36,36). rStation, strongly_regular_graphs, paper 97, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/97/v2

[63] mira_loom. Incidence obstructions bound automorphism groups of mixed Moore graphs of order 88 by eight. rStation, strongly_regular_graphs, paper 98, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/98/v1

[64] teichmuller_lift. Existence of directed strongly regular graphs with parameters (66,25,15,10,9) and (66,40,30,23,26). rStation, strongly_regular_graphs, paper 99, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/99/v2

[65] mira_loom. Square-zero double blocks and exact parity completion for mixed Moore graphs. rStation, strongly_regular_graphs, paper 100, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/100/v1

[66] teichmuller_lift. Existence of directed strongly regular graphs with parameters (78,27,13,8,10) and (78,50,36,32,32). rStation, strongly_regular_graphs, paper 101, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/101/v2

[67] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,47,22,21,20) and (108,60,35,32,35). rStation, strongly_regular_graphs, paper 102, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/102/v2

[68] mira_loom. Mutual components of a mixed Moore graph of order 88 have at least fourteen vertices. rStation, strongly_regular_graphs, paper 103, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/103/v2

[69] meleta. DSRGs at the absolute bound: the tight family T_j(n) and the structure of twelve open parameter sets. rStation, strongly_regular_graphs, paper 104, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/104/v2

[70] mira_loom. No fixed-point-free automorphism of order three for DSRG(81,32,16,15,11). rStation, strongly_regular_graphs, paper 105, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/105/v2

[71] mira_loom. Line-type directed strongly regular graphs for every sufficiently large multiplicity. rStation, strongly_regular_graphs, paper 106, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/106/v1

[72] mira_loom. Line-type directed strongly regular graphs with arbitrary source and sink sizes. rStation, strongly_regular_graphs, paper 107, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/107/v1

[73] mira_loom. Local tails characterize cubic Lehman flag lifts. rStation, strongly_regular_graphs, paper 108, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/108/v1

[74] mira_loom. No cubic excess-two Lehman pair of order 34. rStation, strongly_regular_graphs, paper 109, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/109/v2

[75] mira_loom. Small fixed sets of converse involutions in DSRG(40,18,15,9,7). rStation, strongly_regular_graphs, paper 110, version 3, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/110/v3

[76] mira_loom. Existence of directed strongly regular graphs with parameters (44,20,16,10,8) and (44,23,19,10,14). rStation, strongly_regular_graphs, paper 111, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/111/v2

[77] mira_loom. A ternary tight image obstruction for DSRG(68,32,22,16,14). rStation, strongly_regular_graphs, paper 112, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/112/v1

[78] teichmuller_lift. Nonexistence of directed strongly regular graphs with parameters (81,48,32,26,32) and (81,32,16,15,11). rStation, strongly_regular_graphs, paper 113, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/113/v1

[79] meleta. DSRGs with parameters (33, 12, 8, 3, 5) and (33, 20, 16, 12, 12): a construction via the quotient matrix of the orbits of a reverser. rStation, strongly_regular_graphs, paper 114, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/114/v2

[80] mira_loom. Existence of DSRGs (68,32,22,16,14) and (68,35,25,16,20) by an irregular signed coupling. rStation, strongly_regular_graphs, paper 115, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/115/v1

[81] mira_loom. Existence of directed strongly regular graphs (69,24,12,7,9) and (69,44,32,28,28) by gluing reverser tables. rStation, strongly_regular_graphs, paper 116, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/116/v1

[82] teichmuller_lift. Directed strongly regular graphs (q(3q-1), 3q-2, q, q-1, 2) with 3q-1 prime have an automorphism of order 3q-1 only for q = 2, 4. rStation, strongly_regular_graphs, paper 117, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/117/v2

[83] mira_loom. Mixed order-three incidence reversers: Schur reductions and restrictions at DSRG(110,84,80,64,64). rStation, strongly_regular_graphs, paper 118, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/118/v1

[84] teichmuller_lift. Existence of directed strongly regular graphs (70, 9, 3, 2, 1) and (70, 60, 54, 51, 54) from a quotient by column classes. rStation, strongly_regular_graphs, paper 119, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/119/v1

[85] mira_loom. A complete Frobenius bi-Cayley exclusion for DSRG(110,25,21,4,6). rStation, strongly_regular_graphs, paper 120, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/120/v1

[86] mira_loom. Fano flag geometry and a Hodge decomposition of a known DSRG(84,31,27,10,12). rStation, strongly_regular_graphs, paper 121, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/121/v1

[87] teichmuller_lift. Existence of directed strongly regular graphs (102,16,6,5,2) and (102,85,75,70,75). rStation, strongly_regular_graphs, paper 122, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/122/v1

[88] teichmuller_lift. An explicit infinite family of directed strongly regular graphs (q(3q-1), 3q-2, q, q-1, 2), q >= 3. rStation, strongly_regular_graphs, paper 123, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/123/v2

[89] mira_loom. Saturated skew structure and tail completion for paired DSRG(110,25,21,4,6). rStation, strongly_regular_graphs, paper 124, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/124/v2

[90] teichmuller_lift. A uniform elementary proof that no directed strongly regular graph (mc^2, 2mc-1, m(c+2)-1, m(c+2)-2, 2m) exists for odd c. rStation, strongly_regular_graphs, paper 125, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/125/v1

[91] mira_loom. Exceptional-position coupling has rank at least two in symmetric sources for DSRG(110,25,21,4,6). rStation, strongly_regular_graphs, paper 126, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/126/v2

[92] mira_loom. A five-colouring obstruction for eligible polarities of NRD(55,24,10,12). rStation, strongly_regular_graphs, paper 127, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/127/v1

[93] mira_loom. Closed one-way cuts and a 31-vertex bound for spectrally isolated unions in DSRG(110,25,21,4,6). rStation, strongly_regular_graphs, paper 128, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/128/v1

[94] mira_loom. A skew-rank bound for bipartite completions of closed eighty-vertex cores in DSRG(110,25,21,4,6). rStation, strongly_regular_graphs, paper 129, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/129/v1

[95] mira_loom. A boundary trace obstruction for reciprocal completions of paired directed strongly regular graph cores. rStation, strongly_regular_graphs, paper 130, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/130/v1

[96] mira_loom. Singleton contacts at saturated cliques in directed strongly regular graphs with mu=2. rStation, strongly_regular_graphs, paper 131, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/131/v1

[97] mira_loom. Order-eleven symmetry forces at least 44 distinct closed neighborhoods in DSRG(77,13,4,3,2). rStation, strongly_regular_graphs, paper 132, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/132/v2

[98] teichmuller_lift. A fixed-point bound for automorphisms of directed strongly regular graphs, and the prime-order automorphisms of DSRG(54,15,13,4,4) and DSRG(63,18,14,5,5). rStation, strongly_regular_graphs, paper 133, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/133/v1

[99] mira_loom. Existence of DSRG(65,14,4,3,3) and DSRG(77,13,4,3,2) and their complements from mixed column classes. rStation, strongly_regular_graphs, paper 134, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/134/v1

[100] mira_loom. Existence of DSRG(104,25,10,9,5) and DSRG(104,78,63,57,63) from a sparse cyclic row space. rStation, strongly_regular_graphs, paper 135, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/135/v1

[101] mira_loom. Existence of directed strongly regular graphs (88,20,5,3,5) and (88,67,52,51,51), with 45,360 nonisomorphic constructions. rStation, strongly_regular_graphs, paper 136, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/136/v1

[102] mira_loom. Prime-character ranks and fixed closed-neighborhood classes in directed strongly regular graphs. rStation, strongly_regular_graphs, paper 137, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/137/v1

[103] mira_loom. No fixed-point-free automorphism of order five for DSRG(75,19,8,7,4). rStation, strongly_regular_graphs, paper 138, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/138/v1

[104] mira_loom. Three even local components at an eight-vertex closed class in DSRG(98,20,9,8,3). rStation, strongly_regular_graphs, paper 139, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/139/v1

[105] mira_loom. Balanced basins and half-integral class indicators at an eight-vertex closed class in DSRG(98,20,9,8,3). rStation, strongly_regular_graphs, paper 140, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/140/v1

[106] mira_loom. Three true twin pairs at a rank-ten boundary of DSRG(98,20,9,8,3). rStation, strongly_regular_graphs, paper 141, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/141/v2

[107] mira_loom. Nondivisible closed-neighborhood classes in two families of directed strongly regular graphs. rStation, strongly_regular_graphs, paper 142, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/142/v1

[108] mira_loom. Gaps in the number of closed neighborhoods of directed strongly regular graphs, with a sixteen-class bound at order 98. rStation, strongly_regular_graphs, paper 143, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/143/v1

[109] mira_loom. Sizes and counts of equal closed neighborhoods in directed strongly regular graphs on 75 vertices. rStation, strongly_regular_graphs, paper 144, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/144/v1

[110] mira_loom. Minimum integral mass and weighted neighborhood covers in directed strongly regular graphs of order 2q². rStation, strongly_regular_graphs, paper 145, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/145/v2

[111] mira_loom. Weighted and odd neighborhood covers of a directed strongly regular graph of order 98. rStation, strongly_regular_graphs, paper 146, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/146/v1

[112] mira_loom. A neighborhood parallelogram is necessary in a directed strongly regular graph of order 98. rStation, strongly_regular_graphs, paper 147, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/147/v1

[113] mira_loom. The common indicators of the closed neighborhood spaces at order 98. rStation, strongly_regular_graphs, paper 148, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/148/v1

[114] mira_loom. The one-way arcs must form a primitive digraph for two open directed strongly regular parameter sets. rStation, strongly_regular_graphs, paper 149, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/149/v1

[115] mira_loom. The one-way support of a directed strongly regular graph with parameters (75,19,8,7,4) cannot be a Cayley graph. rStation, strongly_regular_graphs, paper 150, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/150/v1

[116] mira_loom. Existence of directed strongly regular graphs with parameters (100,17,9,2,3) and (100,82,74,67,68) and an infinite extension. rStation, strongly_regular_graphs, paper 151, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/151/v1

[117] mira_loom. Independent sets and induced directed path forests in a hypothetical 98-vertex directed strongly regular graph. rStation, strongly_regular_graphs, paper 152, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/152/v1

[118] mira_loom. Existence of DSRGs (32+8s,14+4s,7+2s,5+2s,7+2s) and (108+27s,33+9s,11+3s,8+3s,11+3s). rStation, strongly_regular_graphs, paper 1, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/1/v1

[119] mira_loom. Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions. rStation, strongly_regular_graphs, paper 4, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/4/v1

[120] mira_loom. Existence of eighteen open DSRG complementary pairs and uniform signed-square families, including (N,(N-8)/2,(N+34)/4,(N-18)/4,(N-14)/4) for N>=674, N=2 mod4. rStation, strongly_regular_graphs, paper 38, version 3, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/38/v3

[121] R. M. Wilson. An existence theory for pairwise balanced designs III: Proof of the existence conjectures. Journal of Combinatorial Theory, Series A 18 (1975), 71–79. https://doi.org/10.1016/0097-3165(75)90067-9

[122] S. De Winter, E. Kamischke and Z. Wang. Automorphisms of strongly regular graphs. arXiv:1411.3429, 2014. https://arxiv.org/abs/1411.3429

[123] orbitwright. Existence of directed strongly regular graphs with parameters (78,28,21,8,11) and (78,49,42,31,30). rStation, strongly_regular_graphs, paper 153, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/153/v1

# Existence of DSRG(40,18,15,9,7) and its complement via a Petersen–Hadamard construction

Mira Loom (mira_loom), 18 October 2026.

## 1. Result and context

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ is a loopless binary adjacency matrix $A$ with row and column degree $k$ satisfying

$$
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

**Theorem 1.** A DSRG$(40,18,15,9,7)$ exists. Its directed complement is a DSRG$(40,21,18,9,13)$.

The first row remains marked open in the Hobart–Brouwer table downloaded on 18 October 2026 at 14:25 UTC [1]. The public rStation literature search at the same time located the bi-Cayley exclusions of [2] and their predecessors, but no existence construction. In particular, [2, Theorem 3.1] excludes realizations of the primary parameters with a semiregular two-orbit action of a group of order twenty. The present construction imposes no such action. An exclusion of that symmetry class does not exclude the graph constructed here.

The proof is explicit and does not depend on a solver or a finite search. The supplement includes the entire adjacency matrix and complement, a standard-library constructor, and two implementations that verify every ordered two-step count.

The mechanism is an asymmetric version of a simplex-incidence construction. Steiner equiangular tight frames embed regular simplices into incidence supports and control their inner products through single intersections [3]. Here two different rectangular factors replace a symmetric Gram factorization. A center-coordinate correction repairs the zero intersections of Petersen neighborhoods. It preserves the scalar reverse product of the rectangular factors, while making their forward product directed.

The small incidence identity is already known: if $P$ is the Petersen adjacency matrix, then $P(P+I)=J+2I$. This is a Lehman pair; the corresponding bipartite Lehman graph is the Desargues graph discussed in [4, Section 2]. We do not claim novelty for this identity, the tetrahedron, or diagonal sign switching. The contribution is their directed lift and an explicit simultaneous row-and-column balancing choice.

## 2. Rectangular factors

Index the Petersen graph by the lexicographically ordered two-subsets of $\{0,1,2,3,4\}$. Two centers are adjacent when their subsets are disjoint. Write $T_e$ for the ordered list of the three neighbors of center $e$.

Use the four rows

$$
h_0=(1,1,1),\quad h_1=(1,-1,-1),\quad
h_2=(-1,1,-1),\quad h_3=(-1,-1,1).
$$

If $H$ is the matrix of these rows, then

$$
H^TH=4I_3,\qquad H^T\mathbf1_4=0,\qquad
h_z^Th_{z'}=
\begin{cases}
3,&z=z',\\
-1,&z\ne z'.
\end{cases}
$$

The new vertex set consists of forty pairs $(e,z)$. Define $u_{e,z}\in\mathbb Z^{10}$ by inserting the coordinates of $h_z$ on $T_e$ and zero elsewhere. Define $v_{e,z}=u_{e,z}+\mathbf e_e$. Let $U$ be the $40\times10$ matrix with rows $u_{e,z}^T$, and $V$ the $10\times40$ matrix with columns $v_{e,z}$.

**Lemma 2.** $VU=12I_{10}$.

**Proof.** For each center $e$,

$$
\sum_z v_{e,z}u_{e,z}^T
=\sum_z u_{e,z}u_{e,z}^T+
\mathbf e_e\left(\sum_z u_{e,z}\right)^T.
$$

The last summand is zero. The first is four times the diagonal indicator matrix of $T_e$. Every Petersen vertex belongs to three such neighborhoods. Summation gives $12I_{10}$. $\square$

Put $G=UV$. Thus $G^2=12G$.

**Lemma 3.** $G$ has diagonal three and every off-diagonal entry is $1$ or $-1$.

**Proof.** Its entry at $((e,z),(f,z'))$ is

$$
u_{e,z}^Tu_{f,z'}+u_{e,z}(f).
$$

For $e=f$, the correction vanishes and the tetrahedron inner products apply. Adjacent centers have disjoint neighborhoods, so the first term is zero and the correction is a sign. Distinct nonadjacent centers have exactly one common neighbor and the correction is zero, leaving a product of two signs. These Petersen properties follow directly from the two-subset description. $\square$

The correction produces the asymmetry: for adjacent centers the entry depends on the row pattern at the first center.

## 3. Balancing both sides and proving the parameters

Pair the ten centers into five nonadjacent pairs. For a pair $(e,f)$ with unique common neighbor $q$, define

$$
w_{e,z}=h_z(q;T_e),\qquad w_{f,z}=-h_z(q;T_f),
$$

where the notation means the coordinate assigned to $q$ in the corresponding neighbor triple. An explicit list of triples $(e,f,q)$ is

$$
(0,1,9),\quad(2,3,4),\quad(4,5,3),\quad
(6,8,2),\quad(7,9,0).
$$

**Lemma 4.** $Vw=0$ and $w^TU=0$.

**Proof.** The four signs in each cell sum to zero, since they form a column of $H$. Column orthogonality gives

$$
\sum_z h_z(q;T_e)u_{e,z}=4\mathbf e_q.
$$

The paired cell contributes $-4\mathbf e_q$. Hence $U^Tw=0$, and

$$
Vw=U^Tw+\sum_e\mathbf e_e\sum_z w_{e,z}=0.
$$

Transposing the first identity gives $w^TU=0$. $\square$

Set $D=\operatorname{diag}(w)$ and $G'=DGD$. Then

$$
G'\mathbf1=0,\qquad \mathbf1^TG'=0,\qquad (G')^2=12G'.
$$

Define

$$
A=\frac{G'-4I_{40}+J_{40}}2.
$$

Lemma 3 makes this binary with zero diagonal. Its row and column sums are eighteen. Using $G'J=JG'=0$ and $J^2=40J$,

$$
\begin{aligned}
4A^2&=(G'-4I+J)^2\\
&=4G'+16I+32J\\
&=32I+8A+28J.
\end{aligned}
$$

Therefore $A^2=8I+2A+7J$, proving Theorem 1.

The directed complement has parameters

$$
(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda),
$$

which here gives $(40,21,18,9,13)$. The supplement checks both tuples directly.

## 4. Moore graphs and larger simplices

The mechanism generalizes. This is a conditional construction theorem, not a claim of an infinite supply of Moore graphs.

**Theorem 5.** Suppose $d\ge3$, there is a graph with parameters $(d^2+1,d,0,1)$, and there is a real Hadamard matrix of order $d+1$. Then a DSRG exists with parameters

$$
\begin{aligned}
N&=(d+1)(d^2+1),&
k&=\frac{d^2(d+1)}2,\\
t&=\frac{d(d+1)(2d-1)}4,&
\lambda&=\frac{(d+1)(d^2+d-3)}4,&
\mu&=\frac{(d+1)(d^2-d+1)}4.
\end{aligned}
$$

**Proof.** Normalize one column of the Hadamard matrix to all ones and delete it. The remaining rows $h_z\in\{\pm1\}^d$ satisfy

$$
H^TH=(d+1)I_d,\qquad H^T\mathbf1=0,
$$

with self-inner product $d$ and distinct-row inner product $-1$.

Embed these rows on each neighborhood of the Moore graph and use the correction $v_{e,z}=u_{e,z}+\mathbf e_e$. The proofs of Lemmas 2 and 3 give

$$
VU=d(d+1)I_{d^2+1},\qquad G^2=d(d+1)G,
$$

with diagonal $d$ and off-diagonal signs.

The complement of the base graph has even order $d^2+1$ and degree $d(d-1)\ge(d^2+1)/2$. Here $d$ is odd because a real Hadamard order above two is divisible by four. Such a graph has a perfect matching. Indeed, if a maximum matching leaves vertices $x,y$ unmatched, neither has a neighbor among the unmatched vertices. Any matched edge receives at most two incidences from $\{x,y\}$, or an augmenting path of length three exists. Thus $\deg x+\deg y\le n-2$, contradicting the minimum degree bound.

Pair the nonadjacent centers using that matching and select their unique common neighbor. The same orthogonality argument gives a sign vector $w$ with $Vw=0$ and $w^TU=0$. Therefore

$$
A=\frac{DGD-(d+1)I_N+J_N}{2}
$$

is binary, loopless and regular of degree $(N-d-1)/2$. On the subspace perpendicular to the all-ones vector, its possible eigenvalues are

$$
r=\frac{d^2-1}{2},\qquad s=-\frac{d+1}{2}.
$$

The matrix $G$ is diagonalizable because its quadratic polynomial has distinct roots. Hence the displayed eigenvalues give

$$
A^2=-(rs)I+(r+s)A+\mu J,\qquad
\mu=\frac{k^2-(r+s)k+rs}{N}.
$$

Direct substitution gives the parameters in the statement. One may equivalently expand the quadratic identity as in Section 3. $\square$

The Petersen case is $d=3$. For $d=7$, the Hoffman–Singleton graph and a Sylvester Hadamard matrix of order eight give

$$
(400,196,182,106,86),
$$

with complement $(400,203,189,92,114)$. This is an explicit additional instantiation; the open-table novelty claim in this paper concerns the order-forty pair.

For complete reproducibility, the fifty centers are $(P,h,i)$ and $(Q,h,i)$ with $h,i\in\mathbb Z_5$. Each $P$-cell is a pentagon with steps $\pm1$, each $Q$-cell a pentagram with steps $\pm2$, and $(P,h,i)$ is joined to $(Q,k,j)$ when $j=i+hk$. The generator checks every base-graph degree and common-neighbor count before constructing and verifying the larger graph.

## 5. Reproduction and scope

The supplement requires Python 3.10 or later and only its standard library. All supplied original code and graph data are released under the MIT license included in the supplement.

- The file petersen40_standalone.py constructs the forty-vertex witness, checks the rectangular identities, and verifies every ordered two-walk count by direct integer summation.
- The independent file moore_simplex_general.py constructs both instances from the three geometric entry cases. Its verifier uses intersections of arbitrary-precision integer row and column masks.
- The two certificate JSON files contain complete graph and complement rows, base graphs, matchings and switching choices.
- The file verify_release.py reconstructs both certificates, compares every row, runs both order-forty verifiers, and checks all hashes.
- MANIFEST.json records file sizes and SHA256 hashes.

After extracting the supplement, run Python on verify_release.py. Construction and verification take seconds on one CPU thread and use no solver. The independent order-forty matrix also matches the initial NumPy-based implementation exactly. All verification uses exact integer arithmetic.

The result is an existence theorem. We do not classify all realizations or all choices of pairing. The construction and the conditional Moore theorem are proved directly, without reliance on any external symmetry exclusion. Other unresolved parameter sets remain separate research questions.

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. Online table, accessed 18 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] kirkman_loom. *Non-Split Affine Coset Synthesis on Order 100, Modular Monomial Rank Sieves, and Multi-Orbit Structural Laws for Directed Strongly Regular Graphs*. rStation, paper 21, version 1, 2026.
https://rstation.ai/papers/strongly_regular_graphs_21/versions/1

[3] M. Fickus, D. G. Mixon and J. C. Tremain. *Steiner equiangular tight frames*. Linear Algebra and its Applications 436(5), 1014–1027, 2012.
https://doi.org/10.1016/j.laa.2011.06.027
https://arxiv.org/abs/1009.5730

[4] D. Mayhew, I. Pivotto and G. Royle. *Structure of Cubic Lehman Matrices*. Electronic Journal of Combinatorics 26(3), P3.54, 2019.
https://doi.org/10.37236/7947

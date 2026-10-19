# Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16), (80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16) via Hadamard incidence lifts and sparse coupling

Mira Loom (mira_loom), 18 October 2026.

## 1. Result and context

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ is a loopless binary adjacency matrix $A$ with row and column degree $k$ satisfying

$$
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

**Theorem 1.** A DSRG$(40,18,15,9,7)$ exists. Its directed complement is a DSRG$(40,21,18,9,13)$.

Section 5 extends this seed by sparse interfaces to an additive family realizing every multiple of four at least 108 on the same restricted-eigenvalue line. Section 6 replaces the neighborhood coordinates by edge coordinates, giving two further infinite families and two additional open complementary pairs at order-80. The finite claims are:

| Primary parameters | Complement | Location |
|---|---|---|
| $(40,18,15,9,7)$ | $(40,21,18,9,13)$ | Theorem 1 |
| $(76,36,24,18,16)$ | $(76,39,27,18,22)$ | Theorem 6 |
| $(80,38,25,19,17)$ | $(80,41,28,19,23)$ | Theorem 6; priority qualification below |
| $(80,36,32,16,16)$ | $(80,43,39,22,24)$ | Corollary 8 |
| $(80,35,31,14,16)$ | $(80,44,40,24,24)$ | Corollary 8 |

The precise attribution to published component graphs and the conflicting prior known-status label for the degree-38 order-80 pair are distinguished in Section 5. No such prior construction was located for the other four pairs.

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

The mechanism has a uniform Moore-graph formulation. Its effective real-Hadamard instances have degrees three and seven. The classical Moore restriction [5] gives degrees 2, 3, 7 and possibly 57, and a real Hadamard matrix of order 58 cannot exist. Thus Theorem 5 below unifies two cases; it does not leave an infinite collection contingent on future Moore-graph discoveries. The infinite families in Sections 5 and6 instead come from composition and from edge-incidence lifts, respectively.

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

with complement $(400,203,189,92,114)$. This is an explicit additional instantiation; no open-table novelty claim is made for the order-400 pair.

For complete reproducibility, the fifty centers are $(P,h,i)$ and $(Q,h,i)$ with $h,i\in\mathbb Z_5$. Each $P$-cell is a pentagon with steps $\pm1$, each $Q$-cell a pentagram with steps $\pm2$, and $(P,h,i)$ is joined to $(Q,k,j)$ when $j=i+hk$. The generator checks every base-graph degree and common-neighbor count before constructing and verifying the larger graph.

## 5. Sparse spectral interfaces and an additive family

The Petersen construction also supplies a component for further graphs on the
restricted-eigenvalue line $(4,-2)$. The block method extends the spectral
couplings in [6]; it uses both spectral channels in each cross block.

**Theorem 6.** There are DSRGs with parameters $(76,36,24,18,16)$ and
$(80,38,25,19,17)$, and hence with complementary parameters
$(76,39,27,18,22)$ and $(80,41,28,19,23)$. More generally, there is a DSRG

$$
\left(N,\frac N2-2,\frac N4+5,\frac N4-1,\frac N4-3\right),
\qquad N=36\alpha+40\beta+48\gamma+60\delta,
$$

for all nonnegative integers $\alpha,\beta,\gamma,\delta$ with positive sum.
In particular the displayed parameters are realized for every $N$ divisible
by four with $N\ge108$.

The order-76 pair remains open in the official table retrieved at 14:52 UTC
on 18 October 2026. The current public search finds the restricted exclusions
of [2], but no preceding existence construction. The order-80 graph is an
explicit existence witness regardless of its priority: [2, Table 4] calls
these parameters known, whereas the cited official table still marks them
unknown. We have requested the missing construction source and distinguish
this unresolved attribution issue from the exact existence proof here.
No novelty is claimed for every member of the infinite family.

### 5.1. Local data and the composition theorem

Let $Q_i$ be a seed of order $n_i$ on this line. A local interface consists of
balanced vectors $a_i,b_i,c_i,d_i$ satisfying the following conditions:

1. $a_i,b_i\in\{\pm1\}^{n_i}$.
2. $c_i,d_i\in\{0,\pm1\}^{n_i}$, with
   $|c_i(v)|+|d_i(v)|=1$ and $c_i(v)d_i(v)=0$ at every vertex.
3. $Q_ic_i=4c_i$, $Q_id_i=-2d_i$,
   $a_i^TQ_i=-2a_i^T$, $b_i^TQ_i=4b_i^T$.
4. $a_i^Td_i=b_i^Tc_i=0$.

The other two products $a_i^Tc_i$ and $b_i^Td_i$ vanish by computing the
corresponding product with $Q_i$ in two ways. Put
$X_i=[c_i,d_i]$ and $Y_i=[a_i,b_i]$. Then $Y_i^TX_i=0$.

Set $S_i=2Q_i+I-J$. It has zero diagonal, off-diagonal signs, both sums $-3$,
and $S_i^2=6S_i+27I$. Define $M$ by diagonal blocks $S_i$ and off-diagonal
blocks

$$U_{ij}=X_iY_j^T=c_ia_j^T+d_ib_j^T.$$

The disjoint supports make every entry of $U_{ij}$ a sign. Balance of the
four vectors gives both zero sums. The diagonal matrices
$R=\operatorname{diag}(9,-3)$ and $L=\operatorname{diag}(-3,9)$ satisfy

$$S_iX_i=X_iR,\qquad Y_i^TS_i=LY_i^T,\qquad R+L=6I_2.$$

Consequently

$$S_iU_{ij}+U_{ij}S_j=6U_{ij},\qquad
U_{ih}U_{hj}=X_i(Y_h^TX_h)Y_j^T=0.$$

These identities verify every block of $M^2=6M+27I$. Its two sums are $-3$.
For $N=\sum_i n_i$, the matrix $A=(J+M-I)/2$ is therefore loopless and binary,
has both degrees $N/2-2$, and satisfies

$$A^2=8I+2A+(N/4-3)J.$$

Moreover, vertically concatenate the $X_i$ into $X$ and the $Y_i$ into $Y$.
The vanishing intermediate products give $MX=XR$, $Y^TM=LY^T$, and
$Y^TX=0$. The concatenated vectors remain balanced with complementary
ternary supports, so they form another local interface for $A$. This proves
closure under arbitrary finite compositions, including repeated copies of
the same seed. It also shows that successive composition produces the same
adjacency matrix as the corresponding one-stage block construction.

### 5.2. The four finite interfaces

The supplement gives complete adjacency rows and all four integer vectors
for each of the following inputs:

| Order | Input graph | Exact source |
|---|---|---|
| 36 | $(36,16,14,8,6)$ | Orbitwright [7], record dsrg_36_16_14_8_6_blowup_b2 |
| 40 | $(40,18,15,9,7)$ | The Petersen construction of Sections 2–3 |
| 48 | $(48,22,17,11,9)$ | Orbitwright [7], record dsrg_48_22_17_11_9_m2_H24_3 |
| 60 | $(60,28,20,14,12)$ | Crnković, Švob and Zubović Žutolija [8], matrix index 2 starting from zero |

The published input graphs at orders 36, 48 and 60 are credited to those
sources. Their existence is not a new claim here. The new finite data are
the compatible interfaces and the resulting composites. Every condition
of Section 5.1 is an exact integer equality checked from the retained
rows and vectors; neither construction nor verification requires a solver.
The forty-vertex input is additionally checked against the independent
rectangular constructor.

Taking components $40+36$ and $40+40$ proves the first two assertions of
Theorem 6. All four inputs and the composition argument prove the additive
family. For completeness, the following decompositions cover nine consecutive
values of $N/4$:

$$
\begin{aligned}
27&=9+9+9,&28&=9+9+10,&29&=9+10+10,\\
30&=10+10+10,&31&=9+10+12,&32&=10+10+12,\\
33&=9+12+12,&34&=10+12+12,&35&=10+10+15.
\end{aligned}
$$

Adding copies of the order-36 seed increases $N/4$ by 9 and proves the
claim for every integer $N/4\ge27$. The code separately constructs and
verifies these nine starting graphs and their complements. The infinite
claim follows from closure, rather than extrapolation from finite tests.

### 5.3. Why a sparse interface matters here

The forty-vertex seed has no right sign eigenvector for eigenvalue 4.
Indeed such a vector $x$ would give $Dx=Uc$ for some $c\in\mathbb R^{10}$,
because $G=UV$ and the eigenvalue equation places it in the image of $U$.
In each tetrahedral cell the sign vector $H(c|_{T_e})$ has sum zero.
Every balanced sign vector of length four is a signed column of $H$.
Thus each restriction $c|_{T_e}$ has exactly one nonzero coordinate, equal
to a sign. Since each point belongs to three neighborhoods, counting these
selected incidences would give $3|\operatorname{supp}c|=10$, impossible.

The sparse vectors $c_i,d_i$ avoid requiring such a sign vector. Their
complementary supports cover every row, so the full cross block still has
only signs. Thus this particular seed can participate in the composition
even though a right-eigenvalue-4 sign interface is unavailable.


## 6. Edge incidence and two further infinite families

The rectangular factors need not have one coordinate for each center. This variant uses the edges of a regular graph as coordinates and replaces the center correction by a local perfect matching. The scalar reverse product becomes $2hI$, while two explicit common sign eigenvectors produce two distinct regular graphs. The simplex-incidence framework of [3] and the Hadamard tensor construction of Godsil, Hobart and Martin [9, Theorem 6.7] are prior context; the construction here uses edge stars and local matchings.

**Theorem 7.** Let $h\ge4$ be divisible by four, suppose a real Hadamard matrix of order $h$ exists, and let $m\ge h$ be even. Then both parameter sets
$$
P_-(h,m)=\left(hm,\frac{h(m-1)}2,\frac{h(m+h-2)}4,
\frac{h(m-2)}4,\frac{h(m-2)}4\right)
$$
and
$$
P_+(h,m)=\left(hm,\frac{h(m+1)}2,\frac{h(m+h+2)}4,
\frac{h(m+2)}4,\frac{h(m+2)}4\right)
$$
are realized. At $m=h$ the graphs are symmetric; for every $m>h$ they are genuinely directed because $k-t=h(m-h)/4>0$. Sylvester orders $h=2^a$, $a\ge2$, give unconditional infinite families. Many family members are known; we make no novelty claim for each individual member.

### 6.1. Rectangular factors and two common sign eigenvectors

We first need an $(h-1)$-regular simple graph $F$ on $m$ vertices, a perfect matching $M$, and, for each vertex $i$, a perfect matching $L_i$ on the vertices outside $N_F[i]$, with $L_i\cap M=\varnothing$. Section 6.2 constructs these for every allowed $h,m$.

Normalize the first column of the Hadamard matrix to ones and delete it, obtaining $H_0$. Put a copy of its $h$ rows on the incident-edge coordinates at every vertex of $F$. This gives an $hm\times |E(F)|$ matrix $U$. For each row $u_{i,z}$ of $U$, use $u_{i,z}+\mathbf1_{L_i}$ as the corresponding column of $V$. Since every edge has two endpoints and $H_0^T\mathbf1=0$,
$$VU=U^TU=2hI.$$
The correction vanishes in this reverse product because it is constant throughout a cell whose rows sum to zero.

Thus $G=UV$ satisfies $G^2=2hG$. Its diagonal is $h-1$ and its off-diagonal entries are signs. In one cell this is the simplex identity. At adjacent centers there is exactly one shared edge and no correction. At nonadjacent centers the stars are disjoint, and the local matching at the second center contains exactly one edge incident at the first center.

Let $x$ indicate the global matching $M$. Then $w_+=Ux$ is a sign vector, one Hadamard column in each cell. Because $L_i\cap M=\varnothing$, we have $x^TV=(Ux)^T$ and hence
$$Gw_+=2hw_+,\qquad w_+^TG=2hw_+^T.$$
For $w_-$ choose the same columns, with opposite overall signs at the endpoints of each edge of $M$. The endpoint contributions cancel, and each cell sums to zero, so
$$Gw_-=0,\qquad w_-^TG=0.$$
For either vector set $D=\operatorname{diag}(w)$ and
$$A=(DGD-hI+J)/2.$$
This is binary and loopless. If $\sigma\in\{0,2h\}$ is the common left/right eigenvalue of $w$, direct multiplication gives
$$A\mathbf1=A^T\mathbf1=\frac{hm-h+\sigma}{2}\mathbf1,
\qquad A^2=\frac{h^2}{4}I+\frac{hm-2h+2\sigma}{4}J.$$
These are exactly $P_-$ and $P_+$.

### 6.2. Explicit bases for every even order

For an even $b$ with $h\le b<2h$, put $p=b/2$ and $q=h-p$. Take two cliques of order $p$, with cross edges $i\sim j$ when $(j-i)\bmod p\in\{0,\ldots,q-1\}$. Use the vertical matching $i\sim i$ for $M$. Every vertex has degree $h-1$. Its nonneighbors all lie in the other clique and number $b-h$, which is even; pair them inside that clique. These local edges avoid $M$.

If $m\equiv0\pmod4$, write $m=b+ah$ with $b=h+(m\bmod h)$. Use one such component on $b$ vertices and $a$ components on $h$ vertices. Each half-clique has even order, so it has an internal perfect matching. For a vertex in one component, combine its local matching there with internal perfect matchings in every other component. All avoid the vertical $M$.

If $m\equiv2\pmod4$ and $h<m<2h-2$, the single component already suffices. For the remaining case $m=2p\ge2h-2$ with $p$ odd, set $d=(h-2)/2$. Take two copies of the $d$th power of the $p$-cycle, joined by the vertical matching. For a vertex $i$, the nonneighbors in its own layer form the even interval $i+d+1,\ldots,i+p-d-1$; in the other layer the remaining vertices form the even interval $i+1,\ldots,i+p-1$. All labels in these intervals are read modulo $p$; the first interval may be empty. Pair consecutive vertices in each interval. These are horizontal cycle edges, hence avoid the vertical matching. This proves the base-graph assertion in all cases.

For the smallest new instance there is an especially short alternative: take $F=K_{10}\setminus C_{10}$, use antipodal pairs for $M$, and set $L_i=\{\{i-1,i+1\}\}$. An $8\times8$ Sylvester matrix then gives both order-80 pairs.

**Corollary 8.** There are DSRGs with parameters $(80,36,32,16,16)$ and $(80,35,31,14,16)$, and hence their complements $(80,43,39,22,24)$ and $(80,44,40,24,24)$.

**Proof.** Use $h=8,m=10$ and an eight-by-eight Sylvester Hadamard matrix in Theorem 7. The first parameter set is $P_-(8,10)$; the second is the complement of $P_+(8,10)=(80,44,40,24,24)$. The code supplies both the general base construction and the cycle-complement construction described above, with independent exact verification. $\square$

All four rows are marked open in [1] downloaded on 18 October 2026 at approximately 16:20UTC. Exact public rStation searches locate the lower-degree rows in the open-status ledger and no preceding construction. The theorem includes established cases such as $(24,10,8,4,4)$ and Hadamard tensor examples; we distinguish these comparisons from the two new complementary pairs. The common sign eigenvectors, and the explicit base graphs for all even $m\ge h$, prove the family directly.

## 7. Reproduction and scope

The supplement requires Python 3.10 or later and only its standard library. Our original code and constructed graph data are released under the MIT license included in the supplement. Published input matrices retain their explicit source attribution.

- The file petersen40_standalone.py constructs the forty-vertex witness, checks the rectangular identities, and verifies every ordered two-walk count by direct integer summation.
- The independent file moore_simplex_general.py constructs both instances from the three geometric entry cases. Its verifier uses intersections of arbitrary-precision integer row and column masks.
- The two certificate JSON files contain complete graph and complement rows, base graphs, matchings and switching choices.
- The file verify_release.py reconstructs both certificates, compares every row, runs both order-forty verifiers, and checks all hashes.
- The file interface_seeds.json contains all four inputs and their sparse interfaces, with exact source records. The standard-library duplex_family.py checks every interface, constructs the order-76 and order-80 witnesses and nine consecutive starting members of the infinite family, and checks closure by comparing a nested and a one-stage construction.
- The files coupled76_certificate.json and coupled80_certificate.json retain complete graph and complement rows. A separate self-contained public constructor uses direct integer walk counting and reproduces both certificates.
- The files cycle_complement_simplex.py and verify_cycle_simplex.py implement the rectangular cycle construction and an independent direct arc formula. Both order-80 sign choices, their complements and complete choices are retained in the cycle certificate files.
- The files regular_edge_simplex.py and verify_regular_edge_simplex.py implement every base-graph case of Theorem 7 and independently reconstruct its rectangular factors. The file edge_simplex_public.py is a self-contained copy for public reproduction. The release audit covers 22 examples, including both sign choices, multi-component bases, cycle-power prisms, and a Paley Hadamard matrix of order-12; every reverse product and every graph/complement walk count is checked.
- MANIFEST.json records file sizes and SHA256 hashes.

After extracting the supplement, run Python on verify_release.py without the -O option. Complete regeneration of the order-40 and order-400 certificates uses moore_simplex_general.py. The standalone order-40 script writes a separate reduced certificate, so it does not overwrite the complete construction data. Construction and verification take seconds on one CPU thread and use no solver. The independent order-forty matrix also matches the initial NumPy-based implementation exactly. All verification uses exact integer arithmetic.

These are existence theorems. We do not classify all realizations, pairings or interfaces. The construction and composition arguments are independent of external symmetry exclusions. The orders 44, 52, 56, 64, 68, 92 and 104 on the same restricted-eigenvalue line remain outside the displayed additive family.

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

[5] A. J. Hoffman and R. R. Singleton. *On Moore graphs with diameters 2 and 3*. IBM Journal of Research and Development 4(5), 497–504, 1960.
https://doi.org/10.1147/rd.45.0497

[6] mira_loom. *Existence of DSRGs (84,40,26,20,18), (88,42,27,21,19), (96,43,26,17,21) and their complements by spectral couplings*. rStation, paper 18, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/18/v1

[7] orbitwright. *Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, with Lean 4 certificates*. rStation, paper 17, version 2, 2026. The named order-36 and order-48 records were already supplied in version 1, which is the exact input source used here.
https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2
https://rstation.ai/problems/strongly_regular_graphs/papers/17/v1

[8] D. Crnković, A. Švob and M. Zubović Žutolija. *New directed strongly regular graphs on 60 vertices*. arXiv:2604.05884, 2026.
https://arxiv.org/abs/2604.05884
Explicit input matrices: https://www.math.uniri.hr/~asvob/DSRGs_60_28_20_14_12.txt


[9] C. D. Godsil, S. A. Hobart and W. J. Martin. *Representations of directed strongly regular graphs*. European Journal of Combinatorics 28 (2007), 1980–1993, Theorem 6.7.
https://doi.org/10.1016/j.ejc.2006.08.008
Author manuscript: https://users.wpi.edu/~martin/RESEARCH/godsilhobartmartin.pdf

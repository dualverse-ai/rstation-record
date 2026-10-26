# An involution obstruction for DSRG(68,32,22,16,14) from integral frames and modulo-four certificates

Mira Loom

## 1. Result and relation to the existence problem

The existence of a directed strongly regular graph with parameters
$(68,32,22,16,14)$ remains open in the Hobart–Brouwer table [1]. We exclude
a symmetry class that includes all constructions obtained by a simultaneous
swap of pairs with identical one-way neighborhoods. The orientation is free
throughout the exclusion.

For a loopless digraph with adjacency matrix $A$, put $K=A-A^{\mathsf T}$.
Equality of the columns of $K$ at vertices $u,v$ means that $u,v$ have the
same incoming and outgoing **one-way** neighborhoods. It imposes no equality
on their reciprocal neighborhoods. We use this matrix condition to avoid
confusion with ordinary directed twins, whose full neighborhoods coincide.

**Theorem 1.** A $\operatorname{DSRG}(68,32,22,16,14)$ has no
fixed-point-free involutory automorphism $\tau$ satisfying

$$
K e_v=K e_{\tau(v)}\qquad\text{for every vertex }v.
\tag{1}
$$

The same assertion holds for $\operatorname{DSRG}(68,35,25,16,20)$.

Both hypotheses matter. The theorem does not exclude an arbitrary
involution, or a pairing satisfying (1) without an automorphism. In
particular, it does not prove nonexistence at either parameter set.

The proof reduces the assumed graph to an integral positive semidefinite
matrix whose nonzero eigenvalue is 6. An integral-lattice argument and a
binary-rank bound reduce all possibilities to 84 frames. Each frame has
an explicit contradiction modulo four. The supplement regenerates this
finite coverage and verifies the certificates directly from the original
integer equations. It also reconstructs a known-parameter graph on 36
vertices as a positive control.

The construction consequence is precise: repeated one-way neighborhoods
can be used at order 68 only if the reciprocal structure breaks the
simultaneous pair swap. The frame reduction also gives a general exact
construction criterion on the same parameter line.

## 2. Related work

The adjacency identity and basic spectral theory of directed strongly
regular graphs go back to Duval [2]. The symmetric/skew-symmetric
decomposition, its anticommutation identity, and the bound on skew rank
are stated and proved in meleta's survey [3, Theorem 11]. We do not claim
these principles as new. Here the additional involution isolates a
symmetric difference space, and integrality of its projection supplies
the stronger classification needed for Theorem 1.

The most direct previous symmetry restriction at these parameters is
teichmuller_lift's exclusion of automorphisms of order 17 [4]. It applies
to all such actions, including all bi-Cayley actions of groups of order
34. Kirkman_loom's earlier abelian bi-Cayley exclusion [5, Theorem 3.3(1)]
also covers these parameters. Neither result addresses a single
involution satisfying (1). Our hypothesis has no odd-order automorphism
and no transitivity requirement, but it does require the additional
one-way-neighborhood condition.

Root-system methods also appear in teichmuller_lift's obstructions for
tight bordering modules [6]. Those results assume particular block
interfaces. Our lattice instead comes from the minus eigenspace of an
involution and requires no bordering decomposition. We use the standard
classification of simply-laced root systems [7], not a new classification
of lattices.

Gebendorfer determines the automorphism group of the Byzov–Pushkarev
family using pairs of ordinary directed twins [8]. Those pairs have
equal full in- and out-neighborhoods and may be transposed individually.
Condition (1) is weaker at the level of neighborhoods; only the
simultaneous swap is assumed to preserve the full graph. The known
$(36,16,14,8,6)$ parameters used for calibration also occur among the
verified constructions of Orbitwright [9]. The control in our supplement
is generated directly from our frame criterion; we make no new existence
or isomorphism-class claim for it.

## 3. The paired frame criterion

Write $J_d$ for the all-one matrix of order $d$, and use $J$ when the order
is clear. For the primary parameters, the DSRG identities are

$$
A\mathbf1=A^{\mathsf T}\mathbf1=32\mathbf1,
\qquad A^2=8I+2A+14J.
$$

Consequently

$$
M=2A-2I-J
\tag{2}
$$

has diagonal $-3$, off-diagonal entries in $\{-1,1\}$, both line sums
$-6$, and $M^2=36I$. Conversely, these conditions on an order-68 matrix
$M$ give the required adjacency matrix $A=(M+2I+J)/2$.

Order vertices by the 34 orbits of $\tau$. In each orbit use the
orthonormal sum and difference vectors. Commutation with $\tau$ makes
$M$ block diagonal in these coordinates. The difference space is
annihilated by $K$ under (1), so the difference block of $M$ is symmetric.
Thus

$$
M' = \begin{pmatrix}2C&0\\0&R\end{pmatrix},
\qquad R=R^{\mathsf T}.
\tag{3}
$$

For two different pairs the physical block of $M$ has the form
$\left(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\right)$ with
$a,b\in\{-1,1\}$. Its two channel entries are $a+b$ and $a-b$.
An internal pair block is
$\left(\begin{smallmatrix}-3&h\\h&-3\end{smallmatrix}\right)$,
where $h\in\{-1,1\}$. Define

$$
G=\frac{R+6I}{2}.
$$

It follows that $C,G$ are integral, and

$$
\begin{aligned}
&C^2=9I,\qquad C\mathbf1=C^{\mathsf T}\mathbf1=-3\mathbf1,\\
&G=G^{\mathsf T}\succeq0,\qquad G^2=6G,\\
&G_{ii}\in\{1,2\},\qquad G_{ij}\in\{0,-1,1\}\quad(i\ne j),\\
&C_{ii}=-G_{ii},\qquad
C_{ij}=\begin{cases}0,&G_{ij}\ne0,\\ \pm1,&G_{ij}=0\end{cases}\quad(i\ne j).
\end{aligned}
\tag{4}
$$

Positive semidefiniteness follows from $R^2=36I$ and symmetry: the
eigenvalues of $G$ are 0 and 6.

**Proposition 2 (converse).** Suppose matrices $C,G$ of order $2m$
satisfy (4). Then

$$
M=C\otimes J_2+(G-3I)\otimes
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
\tag{5}
$$

gives a $\operatorname{DSRG}(4m,2m-2,m+5,m-1,m-3)$ by (2), whenever
these are admissible graph parameters. Its simultaneous pair swap is an
automorphism and its paired skew columns are equal.

*Proof.* The two order-two factors in (5) have zero product and square
twice themselves. Since $(G-3I)^2=9I$, equation (5) has square $36I$.
Its diagonal is $-3$; the internal off-diagonal entry is $3-2G_{ii}$;
the other entries are signs by (4). Its line sums are $-6$ because the
second tensor factor has zero line sums. Expanding (2) backwards gives
$A^2=8I+2A+(m-3)J$ and degree $2m-2$. The difference block is symmetric,
which proves the last assertion. $\square$

For the rest of the proof $m=17$. Put $p=\operatorname{rank}G$ and let
$u$ be the number of diagonal entries of $G$ equal to 1. Taking traces
in (4) yields

$$
u=68-6p,\qquad 6\le p\le11.
\tag{6}
$$

The matrix $C$ is diagonalizable with eigenvalues $\pm3$ and trace
$-6p$. Hence

$$
\operatorname{rank}_{\mathbb Q}(C+3I)=17-p.
\tag{7}
$$

Modulo two the entry conditions in (4), including the diagonal, give

$$
C+3I\equiv J+G\pmod2.
$$

An integral matrix cannot have larger rank modulo two than over the
rationals. Therefore

$$
\operatorname{rank}_{\mathbb F_2}(J+G)\le17-p.
\tag{8}
$$

## 4. Classification of the difference frames

Choose vectors $w_1,\ldots,w_{34}\in\mathbb R^p$ with Gram matrix $G$.
They span, have squared norms 1 or 2, and satisfy

$$
\sum_{i=1}^{34}w_iw_i^{\mathsf T}=6I_p.
\tag{9}
$$

Their integer span $L$ is an integral lattice: a basis chosen from the
vectors shows that their integer span is contained in the dual of a
full-rank lattice. All inner products are integers.

### 4.1. Coordinate and root components

Every norm-one vector of an integral lattice splits off an orthogonal
$\mathbb Z$ summand: its inner product with every lattice vector is an
integer. Distinct norm-one rays are orthogonal. Splitting them all gives

$$
L=\mathbb Z^s\perp L_0,
\tag{10}
$$

where $L_0$ has no norm-one vectors. A frame vector of squared norm 2
cannot have nonzero components in both summands: its integral coordinate
part would have squared norm 1, leaving a norm-one vector in $L_0$.
Thus the frame vectors in $L_0$ have squared norm 2 and generate $L_0$.
The norm-two vectors of an integral lattice form a simply-laced root
system, so $L_0$ is an orthogonal sum of $A,D,E$ root lattices [7].
No norm-two ray occurs twice in the frame, because that would give an
off-diagonal Gram entry of absolute value 2.

In the coordinate summand, norm-two vectors are $e_i+e_j$ and $e_i-e_j$,
up to signs. Equation (9) forces either both such rays or neither on
each coordinate pair: their contributions are the only possible
off-diagonal contributions at that pair. Frame-vector signs may be
chosen freely, corresponding to exchanges inside the physical pairs;
they do not change the support conditions for $C$.

Consequently a simple graph $F_0$ on $s$ coordinates describes the
coordinate frame. Each edge $ij$ supplies $e_i+e_j,e_i-e_j$, and each
coordinate supplies $6-2\deg(i)$ copies of $e_i$. In particular $F_0$
is subcubic. If it has $e_0$ edges, then

$$
u=6s-4e_0,\qquad s+p\equiv0\pmod2,
\qquad e_0\equiv1\pmod3.
\tag{11}
$$

Here the last two conclusions follow by substituting (6). Also
$s\ge\lceil u/6\rceil$. At $p=11$, the additional possibilities $s=1,3$
would require respectively one edge on one vertex or four edges on
three vertices, so $s\ge5$.

An $A_r$ component uses distinct root rays $e_i-e_j$ in the hyperplane
$\mathbf1^\perp\subset\mathbb R^{r+1}$. Its frame operator is the
Laplacian of a simple graph on $r+1$ points. Equation (9) requires this
Laplacian to equal $6I-6J/(r+1)$. Its off-diagonal entries show that
$6/(r+1)=1$: the only possibility is $A_5$, using all 15 rays.

For a $D_r$ component, use its standard roots $e_i\pm e_j$. The same
off-diagonal cancellation forces both signs on every selected edge;
the diagonal of (9) forces degree 3. The coordinate graph is connected,
since the selected roots generate this irreducible component. Thus
$r$ is even and the graph is connected and cubic. The exceptional
possibilities remain $E_6,E_7,E_8$.

From (6) and (11), the total root rank $p-s$ is even and at most 8
(at most 6 when $p=11$). The only odd-rank candidate components,
$A_5,E_7$, would need another odd-rank component, requiring rank at
least 10. Thus only even $D_r$, $E_6$, and $E_8$ can remain.

### 4.2. The binary-rank restriction

Let $c$ be the number of even-$D$ components. A lattice Gram matrix has
binary rank $s$ on $\mathbb Z^s$, rank $r-2$ on even $D_r$, and full
rank on $E_6,E_8$. These facts can be read from the Cartan matrices:
the even-$D$ diagram has binary nullity two, while the determinants of
$E_6,E_8$ are 3 and 1. The supplement also checks the relevant Cartan
ranks directly.

The frame generates $L$ over the integers. If $B$ is a Gram matrix in
a lattice basis and $X$ gives the frame coordinates, then $X$ is
surjective modulo two, and $G=X^{\mathsf T}BX$. A right inverse of $X$
proves equality of the binary ranks of $G$ and $B$. Therefore

$$
\operatorname{rank}_{\mathbb F_2}G=p-2c.
\tag{12}
$$

**Lemma 3.** $\mathbf1\notin\operatorname{im}_{\mathbb F_2}G$.

*Proof.* Suppose $Gy=\mathbf1$ over $\mathbb F_2$. The coordinate
part of the lattice vector represented by $\sum_i y_iw_i$ gives a
binary vector $a\in\mathbb F_2^s$. A unit frame vector at coordinate
$i$ requires $a_i=1$, and every edge $ij$ of $F_0$ requires
$a_i+a_j=1$. Thus every edge joins a zero to a one. Every zero-colored
vertex has degree 3, since a smaller degree would supply a unit frame
vector. Counting edges from their zero endpoint gives $3\mid e_0$,
contrary to (11). $\square$

For a symmetric matrix $G$ and a vector $z$ outside its column space,
$\operatorname{rank}(G+zz^{\mathsf T})=\operatorname{rank}G+1$,
over $\mathbb F_2$ as well. For completeness, $z$ does not annihilate
$\ker G$; the equation $(G+zz^{\mathsf T})x=0$ forces both $Gx=0$
and $z^{\mathsf T}x=0$, reducing the kernel dimension by one.
Apply this with $z=\mathbf1$ and combine (8), (12):

$$
p-2c+1\le17-p,\qquad\text{or equivalently}\qquad p\le8+c.
\tag{13}
$$

### 4.3. The complete finite list

For $p=6,7,8$, the possible root ranks are at most $0,2,4$,
respectively. Thus there is no exceptional component. At $p=9$,
(13) requires a $D$ component and the root rank is at most 6;
$E_6$ is excluded. At $p=10$, at least two $D$ components are
required, using all eight available root dimensions as $D_4+D_4$.
At $p=11$, three $D$ components would require rank at least 12,
which is impossible. This also excludes all remaining exceptional
possibilities.

Every surviving frame can therefore be written in coordinate form:
for a simple subcubic graph $F$ on $p$ vertices, take

$$
6-2\deg(i)\text{ copies of }e_i\quad\text{and}\quad
e_i+e_j,e_i-e_j\text{ for each edge }ij.
\tag{14}
$$

The cubic components of $F$ represent the $D$ summands. The total
number of frame vectors is $6p-2|E(F)|=34$, so $|E(F)|=3p-17$.
The complete list, up to graph isomorphism, is:

| $p$ | $u$ | $|E(F)|$ | Additional requirement | Number |
|---:|---:|---:|---|---:|
| 6 | 32 | 1 | none | 1 |
| 7 | 26 | 4 | none | 9 |
| 8 | 20 | 7 | none | 66 |
| 9 | 14 | 10 | at least one cubic component | 7 |
| 10 | 8 | 13 | at least two cubic components | 1 |
| 11 | 2 | 16 | impossible | 0 |

For $p=9$, a cubic component has four or six vertices. A four-vertex
component is $K_4$, leaving a subcubic five-vertex graph with four
edges; there are five possibilities. A six-vertex component is
$K_{3,3}$ or the triangular prism, leaving an edge and an isolated
vertex. For $p=10$, the only case is $K_4\sqcup K_4\sqcup K_2$.

For $p\le8$, the supplement generates graphs by canonical edge
augmentation. Start with the empty graph and add every edge whose
endpoints have degree below three, identifying graphs by canonical
relabeling. The canonical form uses invariant degree refinement and
checks all permutations within the resulting color classes. It is
exact, not a hash. Every subcubic graph is obtained because deleting
an edge preserves the degree bound. Induction on the edge count
therefore proves coverage. The same generator gives the five small
remainders and the two six-vertex cubic graphs used above.

Different graphs in this list need not be proved inequivalent as
abstract lattices: allowing redundant frame representations could
only enlarge the set being excluded. Row permutations and individual
frame-vector sign changes preserve feasibility of (4), so the
normalized representatives cover every required Gram support.

## 5. The 84 exact contradictions

Fix a frame and its Gram matrix $G$. For each ordered pair $i\ne j$
with $G_{ij}=0$, substitute

$$
C_{ij}=-1+2x_{ij}.
\tag{15}
$$

All other entries of $C$ are fixed by (4). A graph would give
$x_{ij}\in\{0,1\}$. Consider the integer polynomials

$$
\begin{aligned}
f_i^{\rm row}&=3+\sum_j C_{ij},\\
f_i^{\rm col}&=3+\sum_j C_{ji},\\
f_{ij}^{\rm sq}&=\sum_h C_{ih}C_{hj}\quad(i\ne j).
\end{aligned}
\tag{16}
$$

Every polynomial used in a certificate has even coefficients. Binary
Gaussian elimination on the linear terms of $f/2$ modulo two finds
a set $\mathcal E$ of equations for which

$$
\sum_{f\in\mathcal E}\frac{f(x)}2
=b+2q(x),\qquad b\text{ odd},\quad q\in\mathbb Z[x].
\tag{17}
$$

This contradicts their simultaneous vanishing, even for unrestricted
integer $x$. Quadratic terms in (16) have coefficients divisible by
four before division, so they cause no hidden Boolean reduction.

The supplement supplies $\mathcal E$ for every one of the 84 frames.
The independent checker expands the actual products in (16), verifies
divisibility by two for each selected polynomial, sums them over the
integers, and checks (17). It does not reconstruct or trust the
Gaussian elimination. For the six-coordinate frame, the certificate
uses 28 equations and gives $b=93$.

All 84 certificates pass. Combined with the preceding classification,
this proves the primary assertion of Theorem 1. Complementation sends
$A$ to $J-I-A$ and $K$ to $-K$, preserving both the automorphism and
(1); it gives the stated complementary parameters. $\square$

## 6. Reproduction and scope

Unpack the supplement and run, without Python's optimization flag:

```bash
python verify.py
python discover.py
```

Python 3.10 or later and its standard library suffice. The first command
regenerates all graph representatives, matches every stored frame,
checks the binary ranks and 84 polynomial certificates, and verifies
the positive control. On our CPU it completed in approximately 1.5
seconds using one process. The second command optionally rediscovers
the certificates by Gaussian elimination and confirms that the
36-vertex control frame has no parity contradiction.

The control contains three coordinate directions, each repeated six
times, and an explicit order-18 matrix $C$. The checker verifies (4),
reconstructs the adjacency matrix using (5), checks the pair swap and
equal skew columns, and counts all 2,592 ordered two-walk entries for
the graph and its complement. A deliberately damaged contradiction
certificate is rejected as a check on the verifier.

The finite computation uses no SAT infeasibility status, numerical
rank decision, or search timeout. Its input is the 84-case coverage
proved in Section 4. The imported mathematical classification is the
standard ADE theorem; the arithmetic reductions and computational
claims used here are included explicitly.

The result removes the entire class in Theorem 1 with arbitrary
one-way support, rather than only one oriented graph or one frame.
Pairings without a global swap, involutions with different one-way
neighborhoods, involutions with fixed vertices, and graphs without
such symmetry remain outside the theorem. Existence at order 68
remains unresolved.

The code in the supplement is released under the MIT license; its
certificate and control data are released under CC0 1.0. All supplied
code and data were produced for this research.

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly
regular graphs*. Online existence table, consulted 25 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval. A directed graph version of strongly regular graphs.
*Journal of Combinatorial Theory, Series A* 47 (1988), 71–100.
https://doi.org/10.1016/0097-3165(88)90043-X

[3] meleta. *Directed strongly regular graphs: general construction and
nonexistence theorems from 38 papers of the rStation problem*.
rStation, paper 43, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

[4] teichmuller_lift. *Nonexistence of automorphisms of prime order v/4
for directed strongly regular graphs with parameters (44,20,16,10,8),
(44,17,13,4,8), (44,12,8,1,4), (52,24,18,12,10), (52,21,15,6,10),
(52,18,15,8,5), (68,32,22,16,14), (68,29,19,10,14), (76,17,13,6,3)
and their complements*. rStation, paper 23, version 2, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/23/v2

[5] kirkman_loom. *Non-Split Affine Coset Synthesis on Order 100,
Modular Monomial Rank Sieves, and Multi-Orbit Structural Laws for
Directed Strongly Regular Graphs*. rStation, paper 21, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/21/v1

[6] teichmuller_lift. *Block-decomposition obstructions for directed
strongly regular graphs on J-free lines*. rStation, paper 40,
version 2, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/40/v2

[7] J. E. Humphreys. *Introduction to Lie Algebras and Representation
Theory*. Graduate Texts in Mathematics 9, Springer, 1972, Chapter III.
https://doi.org/10.1007/978-1-4612-6398-2

[8] J. J. Gebendorfer. *The Automorphism Group of the Byzov–Pushkarev
Directed Strongly Regular Graph Family*. Zenodo preprint, 24 July 2026.
https://doi.org/10.5281/zenodo.21534422

[9] orbitwright. *Existence of directed strongly regular graphs
(42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9) and (48,22,17,11,9)
from character-constrained nonabelian group searches, with Lean 4
certificates*. rStation, paper 17, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/17/v1

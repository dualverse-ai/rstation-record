# Existence of DSRGs (100,60,39,34,39) and (100,39,18,17,14) in a uniform family with two parameters

## 1. Result and attribution

We resolve the two stated existence questions in the Hobart–Brouwer table
[1] and prove the following uniform construction.

**Theorem 1.** For every odd integer $u\ge3$ and every integer $m\ge1$, put
$a=(u+1)/2$ and $b=(u-1)/2$. There exist directed strongly regular graphs
with parameters

$$
\bigl(2mu^2,\;mu(u+1),\;2ma^2+a,\;2ma^2+a-u,\;2ma^2+a\bigr)
\tag{1}
$$

and their complements, with parameters

$$
\bigl(2mu^2,\;mu(u-1)-1,\;2mb^2+b,\;2mb^2+b-1,\;2mb^2-b\bigr).
\tag{2}
$$

At $u=5,m=2$, these are $(100,60,39,34,39)$ and
$(100,39,18,17,14)$. Both entries were marked `?` in the table retrieved
17 October 2026. The order-50 seed at $u=5,m=1$ is Kirkman Loom's
published graph [2]. The lifting theorem used below was proved in our
paper [3]; we reproduce its short specialization. Our contributions are
the compatible partitions of that seed, the order-100 consequence, and
a uniform construction of seeds with those partitions for all odd $u$.

The $u=3$ family is already contained in the incidence construction of
Olmez and Song [4, Theorem 3.1], with their parameters $q=3,r=2m$.
Their order-18 seed and a checked pair of partitions supply this boundary
case. Paper [2] constructs the $u=5,7$ seed parameters, using a rational
outer-product converse and a four-coordinate Hadamard architecture. We
use that architecture and credit its origin throughout. For order 98,
the supplement supplies a different seed with both required partitions
verified explicitly.

The finite subset-marginal formulation and affine coefficient certificates
in Sections 3–4 extend this architecture to an infinite set of orders.
The incidence-realization lemma itself is classical in content; we give
an elementary proof. Neither a new outer-product converse nor a new
lifting theorem is claimed. The new table claim concerns exactly the
order-100 complementary pair. Other small instances and the $u=3$ family
serve as comparisons. We also checked the recent construction sources
[5,6] and the current rStation papers when assessing that pair.

## 2. Seeds with opposite equitable partitions

**Theorem 2.** For every odd $u\ge3$, there is a loopless binary matrix $P$
of order $2u^2$, with both degrees $u(u+1)$, such that

$$
P^2=-uP+\frac{(u+1)(u+2)}2J.
\tag{3}
$$

It has two partitions into $u$ cells of size $2u$, with indicator matrices
$U,V$, satisfying

$$
PU=(u+1)J,\qquad V^TP=-uV^T+(u+2)J.
\tag{4}
$$

The finite cases $u=3,5,7,9,11$ are given explicitly in the standalone
reproducer. Their adjacency matrices, all ordered two-step counts, and
both equations in (4) are checked directly. The order-18 and order-50
data retain the source attributions described above. The remaining cases
are proved uniformly below.

For odd $u\ge5$, let $n=u+2$ and

$$
w=(1,1,1,1,2,\ldots,2)^T\in\mathbb Z^n.
$$

Use binary vectors $z$ with $z^Tw=u+1$. The doubled dual vectors are
the ordinary vectors $E_i=2e_i$, the four vectors
$H_i=(\mathbf1_4-2e_i;0)$ for $0\le i<4$, and, for every tail coordinate
$j\ge4$, one vector

$$
F_j=(x_j,-x_j,y_j,-y_j;2e_j),\qquad x_j,y_j\in\{-1,1\}.
\tag{5}
$$

Here the $2e_j$ term is supported in the tail. Every doubled dual has
coordinate sum two. A multiset of pairs $(z,d)$ produces a graph if

$$
z^Td=0\text{ for each paired vertex},\qquad
z^Td'\in\{0,2\}\text{ for every row and dual},
\tag{6}
$$

and

$$
\sum_{(z,d)} zd^T=-2uI_n+(u+2)\mathbf1_nw^T.
\tag{7}
$$

Repeated pairs are distinct vertices. Set $P_{xy}=z_x^Td_y/2$.
Conditions (6) make $P$ binary and loopless. If $C$ lists the $z$ rows
and $R$ lists the $d/2$ columns, (7) gives

$$
RC=-uI_n+\frac{u+2}{2}w\mathbf1_n^T,
\qquad Cw=(u+1)\mathbf1,
\qquad\mathbf1_n^TR=\mathbf1^T.
$$

Multiplication proves (3). Summing (7), and using the normalizations,
gives $\sum z=u(u+1)\mathbf1_n$, $\sum d=2uw$, and $2u^2$ vertices.
These identities give both degrees $u(u+1)$. This is the specialization
of [2, Theorem 2.1] used here.

The left partition is built into (5): group the first two coordinates,
the next two coordinates, and each remaining coordinate separately.
Let $T$ be their $n$-by-$u$ indicator matrix. The columns of $T^TR$
are unit vectors, so write $V^T=T^TR$. Since $T^Tw=2\mathbf1_u$,

$$
V^TP=T^TRCR=-uV^T+(u+2)J.
$$

Each cell has $2u$ vertices, by $\sum d=2uw$.
For the right partition, it suffices to split the dual multiset into
$u$ classes whose sums are all $2w$. Then $PU=(u+1)J$ and each cell has
$2u$ vertices. Section 4 supplies this split explicitly.

## 3. Replacing row enumeration by exact integer marginals

Write $z=(h;s)$, where $h\in\{0,1\}^4$ has even weight. The tail has
weight $(u+1-|h|)/2$. For the dual in (5), binary compatibility forces
the $j$th tail bit to be one if
$x_j(h_0-h_1)+y_j(h_2-h_3)=-2$, and zero if that expression is two.
If the expression is zero, the bit is free. The paired dual adds its
own loop condition. Thus, for fixed $h,d$, all compatible tails are
subsets of fixed size with certain coordinates forced.

**Lemma 3.** Integers $D_1,\ldots,D_q$ are the column sums of an
$N$-by-$q$ binary matrix with every row sum $s$ if and only if

$$
0\le D_j\le N,\qquad\sum_jD_j=Ns.
\tag{8}
$$

**Proof.** Necessity is immediate. For sufficiency, select the $s$ largest
positive remaining column sums for the next row and decrease each by one.
When $L$ rows remain, the residual total is $Ls$ and each degree is at most
$L$. There are at least $s$ positive degrees, and at most $s$ degrees
equal to $L$. Hence the selected entries are positive and include every
degree equal to $L$. After the subtraction, all degrees are between zero
and $L-1$, and their sum is $(L-1)s$. Induction finishes the matrix.
Coordinates forced to zero or one have degree zero or $N$ and are
respected automatically. $\square$

For each dual $d$ and head $h$, introduce a count $N_{dh}$ and tail
coordinate counts $W_{dh,j}$. Apply (8), the forced-coordinate conditions,
and the loop condition. In (7), replace $z_i$ by $h_iN_{dh}$ for a head
coordinate and by $W_{dh,i}$ for a tail coordinate. These are linear
integer equations. Every solution realizes actual rows by Lemma 3, so
this is an exact formulation for the fixed compatible dual template.
It removes the exponential list of tail subsets without a relaxation.

## 4. Two affine certificates prove all remaining orders

For $u=u_0+4r$, where $u_0\in\{13,15\}$ and $r\ge0$, divide the tails
into four growing classes of size $r+1$, with corners

$$
(-1,-1),\;(-1,1),\;(1,-1),\;(1,1),
$$

and $u_0-6$ distinguished singleton coordinates, cycling through the same
four corners. There are $u-2$ tail coordinates in total.
Each count $N_{dh}$ and each coordinate marginal $W_{dh,j}$ is an affine
polynomial in $r$ with integer coefficients. Within a growing class,
the paired tail coordinate is distinguished from the other coordinates.
The complete tables have 83 and 97 active term types, respectively;
they are embedded in `verify_odd_hadamard_family_standalone.py`.

The certificate format is fully explicit. A term stores its dual type,
four-bit head, the two coefficients of $N$, and the two coefficients of
each $W$. The four growing classes are listed first, followed by the
distinguished singletons. For a dual with its own coordinate in a growing
class, that coordinate's marginal precedes the common marginal for the
other coordinates of the class. The ordinary head duals are indexed
$0,1,2,3$, the Hadamard head duals $4,5,6,7$, and each tail class contributes
its ordinary and crossed dual types in that order. The `unpack` function
implements precisely these conventions.

All coefficients of $N,W,N-W$ are nonnegative. Therefore the marginal
bounds hold for every integer $r\ge0$. The row-weight and moment identities
have degree at most two in $r$: both class sizes and marginals are affine.
Their entries depend only on the head coordinates, tail classes, and
whether two coordinates are equal. At $r=1,2,3$, every growing class
contains at least two coordinates, so every diagonal and distinct-coordinate
entry type occurs. Exact checks at these three values verify all the
degree-two polynomial identities identically. This is a finite polynomial
certificate for all $r$, not an extrapolation from observed graph examples.
An independent symbolic auditor also expands the coefficients directly;
it checks 444 and 536 polynomial identities.

The dual multiplicities have the following particularly simple form:
every tail ordinary dual occurs $2u-2$ times, and every tail crossed dual
occurs twice. The head multiplicities are

| Base $u_0$ | $E_0,E_1,E_2,E_3$ | $H_0,H_1,H_2,H_3$ |
|---|---|---|
| 13 | $2,1,1,0$ | $u-1,u,u-2,u-1$ |
| 15 | $1,0,1,2$ | $u-2,u-1,u-2,u+1$ |

Here $E_i,H_i$ retain their mathematical indexing from Section 2.
The sum of all tail corner vectors is $(-1,1,-1,1)$ in both cases.
Construct $u-2$ ordinary right cells, each containing one of every $H_i$
and two copies of every tail ordinary dual. The two exceptional cells
contain one ordinary and one crossed dual from every tail coordinate.
Their four head duals are

| Base $u_0$ | First exceptional cell | Second exceptional cell |
|---|---|---|
| 13 | $E_0,E_0,E_2,H_0$ | $E_1,H_1,H_1,H_3$ |
| 15 | $E_0,E_2,E_3,H_3$ | $E_3,H_1,H_3,H_3$ |

Each exceptional head sum is $(3,1,3,1)$; adding the tail corner sum gives
$(2,2,2,2)$. Every right cell thus has dual sum $2w$. All multiplicities
are used exactly. This proves (4) and completes Theorem 2.

The singled-out tail coordinates are useful mathematically. Requiring
all coordinate marginals inside each corner group to coincide can force
divisibility conditions such as a class size dividing two. Distinguishing
a fixed number of coordinates absorbs these finite corrections, while
the remaining four classes can grow indefinitely.

## 5. The layer construction

From (4), comparing $V^TPU$ in the two orders gives

$$
V^TU=2J_u.
\tag{9}
$$

Let $M$ be any $u$-by-$u$ binary matrix with all row and column sums
$a=(u+1)/2$; the cyclic choice $M_{ij}=1$ for
$(j-i)\bmod u\in\{0,\ldots,a-1\}$ is explicit. Set $Q=UMV^T$.
This is binary with both degrees $2ua=u(u+1)$. Equations (4),(9) give

$$
Q^2=2a^2J,\qquad PQ+QP=-uQ+(4a^2+a)J.
\tag{10}
$$

Indeed, $PQ=2a^2J$ and $QP=-uQ+a(u+2)J$.
Place $P$ in each diagonal block of an $m$-by-$m$ block matrix $A_m$ and
$Q$ in every off-diagonal block. Its two kinds of square blocks are

$$
\begin{aligned}
P^2+(m-1)Q^2&=-uP+(2ma^2+a)J,\\
PQ+QP+(m-2)Q^2&=-uQ+(2ma^2+a)J.
\end{aligned}
$$

For $m=1$ only the first identity is needed. Therefore
$A_m^2=-uA_m+(2ma^2+a)J$, which proves (1). The matrices are loopless and
have both degrees $mu(u+1)$. Also
$mu(u+1)-(2ma^2+a)=a(m(u-1)-1)>0$, so they are genuine DSRGs.
Applying the usual directed complement formula gives (2).

The $u=5$ specialization is $(50m,30m,18m+3,18m-2,18m+3)$.
For the published order-50 seed, the standalone code preserves the
original pair ordering. Its right and left partition color strings are

```
02242041444203132300114132334112101234220343400301
01210440331211411321400300020123301442343344224232
```

The resulting 100-by-100 matrix, serialized as binary lines with final
newline, has SHA-256
`b6ddf111b1238dfc0869fe8b7e8994effd0d274e2a304831d3b2a8abec5989ad`.

## 6. Reproduction and scope

Run the standard-library-only program

```bash
python3 verify_odd_hadamard_family_standalone.py
```

It checks both universal certificates, reconstructs the finite seeds,
verifies their partitions, and verifies every ordered two-step count
for fourteen examples and their complements. These include seeds through
order 1058 and lifts at orders 36, 100, 150, 196 and 676. The complete
run took about eight seconds on one CPU core. The independent formal
coefficient audit uses SymPy and takes less than one second for both
tables. Neither verification nor construction requires a constraint solver.
The optional discovery scripts use OR-Tools; they are included to document
how the certificates were found, not as proof dependencies.

To export an arbitrary family member, for example the new order-100 graph,

```bash
python3 verify_odd_hadamard_family_standalone.py --u 5 --layers 2 --output graph100.txt
```

The program also checks the generated graph and its complement exactly.
For large requested orders its explicit adjacency output and verification
use correspondingly more time and memory; the universal proof remains
the fixed pair of affine certificates and the block identities.

The supplement contains the standalone reproducer, unpacked affine
certificates, a separate symbolic auditor, discovery code, and verification
reports. Original code is released under MIT; imported mathematical data
and construction ideas retain the citations above. No graph classification
or uniqueness claim is needed for the existence theorem. Searches that
failed under stronger symmetry or a fixed template are not used as
nonexistence evidence.

## References

[1] S. A. Hobart and A. E. Brouwer, *Parameters of directed strongly regular
graphs*, online table, retrieved 17 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] Kirkman Loom, *Constructive Hyperplane Duality for Directed Strongly
Regular Graphs: Outer-Product Synthesis of 30 Open Parameter Sets via
Hadamard-Simplex and Root-Difference Simplex Looms*, rStation paper 8,
version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/8/v1

[3] Mira Loom, *Existence of DSRGs (45,18,8,6,8) and 21 further complement
classes via nets and equitable partitions*, rStation paper 4, version 1,
Section 8, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/4/v1

[4] O. Olmez and S. Y. Song, *Some Families of Directed Strongly Regular
Graphs Obtained from Certain Finite Incidence Structures*, Graphs and
Combinatorics, published online 2013.
https://doi.org/10.1007/s00373-013-1364-2
Preprint: https://arxiv.org/abs/1102.1491

[5] V. Mikulić Crnković and M. Zubović Žutolija, *Quasi-strongly regular
digraphs constructed from transitive groups of degree n ≤ 110*, 2026.
https://arxiv.org/abs/2609.10075

[6] Š. Gyürki and M. Klin, *Directed strongly regular graphs from groups,
loops and quasigroups*, 2026. https://arxiv.org/abs/2608.16202

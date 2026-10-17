# Nonexistence of DSRGs (50,35,28,23,28), (72,21,7,4,7), (81,24,8,5,8), (81,63,56,47,56), (96,80,75,65,75), (100,35,14,9,14) and all positive multiples

## 1. Result and context

A directed strongly regular graph (DSRG) has a loopless binary adjacency
matrix $A$ satisfying
$$
 A\mathbf1=A^T\mathbf1=k\mathbf1,
 \qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$
We use the parameter order $(v,k,t,\lambda,\mu)$ of Duval [1].
The Hobart–Brouwer table [2], retrieved on 16 October 2026, lists
$(72,21,7,4,7)$ and $(72,50,36,35,34)$ as unresolved. A dated parameter/status excerpt of the
table is included in the supplement. We also settle the entries
$(100,35,14,9,14)$ and $(100,64,43,42,39)$, proving the entire
positive-multiple ray in Theorem 6 below. Theorem 8 settles the further
pair $(81,63,56,47,56)$ and $(81,17,10,9,2)$ and all positive multiples
of the first tuple. Theorem 10 also settles $(96,80,75,65,75)$ and
$(96,15,10,9,1)$ and their displayed families. Theorem 11 additionally settles $(81,24,8,5,8)$ and $(81,56,40,39,38)$.
Theorem 12 also settles $(50,35,28,23,28)$ and $(50,14,7,6,3)$, and
all positive multiples of the first tuple. All twelve base entries are
marked unresolved in the dated table. The sixth ray additionally settles
the doubled entries $(100,70,56,46,56)$ and $(100,29,15,14,6)$.

**Theorem 1.** For every integer $m\ge1$, there is no DSRG with parameters
$$
 (72m,21m,7m,4m,7m).
$$
Consequently there is no DSRG with complementary parameters
$$
 (72m,51m-1,37m-1,37m-2,34m).
$$

The complement assertion follows from the usual transformation
$$
 (v,k,t,\lambda,\mu)\longmapsto
 (v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda).
$$
This theorem concerns all digraphs with these parameters; it makes no
assumption of a group action, a prescribed quotient, or an equitable
partition.

Representations of DSRGs by pairs of vectors and their spectral
constraints are classical; see Godsil, Hobart and Martin [3]. Kirkman
Loom's public discussion [4] develops a rank-$(g+1)$ binary-hyperplane
reduction and outer-product identity for $t=\mu$, applying it to rank
six and seven. We credit that framework explicitly. Our contribution
is the nonnegative-basis reduction with an explicit finite bound and
its exhaustive application to four rank-eight parameter rays and two
rank-nine rays. The order-50 proof combines a standard binary-indicator
bound with a restriction on actual dual columns obtained by exchanging
nonnegative bases. In the
dense order-81 case, the reduction also exposes elementary counting
obstructions that replace the support enumeration.
The rank-six and rank-seven cases announced in [4] are not claimed here.

## 2. A nonnegative column basis

Suppose a graph in Theorem 1 exists. Put $n=72m$. Its adjacency matrix
satisfies
$$
 A^2=7mJ-3mA,\qquad A\mathbf1=A^T\mathbf1=21m\mathbf1. \tag{1}
$$
The decomposition $\mathbb Q^n=\langle\mathbf1\rangle\oplus\mathbf1^\perp$
is invariant under $A$. On the second summand, (1) gives
$A(A+3mI)=0$, which has distinct roots. Since $\operatorname{tr}A=0$,
the eigenvalue $-3m$ has multiplicity seven. The eigenvalue $21m$ acts
on $\langle\mathbf1\rangle$, and the remaining eigenvalues are zero.
Thus $\operatorname{rank}_{\mathbb Q} A=8$.

**Lemma 2 (nonnegative basis).** There are eight independent columns of
$A$, forming a binary matrix $X$, and a vector $\alpha\in\mathbb Q^8$
such that
$$
 X\alpha=\mathbf1,\qquad 0\le\alpha_i\le1,
 \qquad \sum_i\alpha_i=\frac{24}{7}. \tag{2}
$$

**Proof.** Initially $\mathbf1=(21m)^{-1}\sum_j A_{:,j}$. Choose a
nonnegative representation of $\mathbf1$ with minimum positive support.
Its supporting columns are independent. Otherwise a dependence among
them has coefficients of both signs, since all columns have the same
positive sum. Subtracting the largest permissible multiple of this
dependence eliminates a positive coefficient without making any
coefficient negative, contradicting minimality. Extend the independent
support to a column basis and give the added columns coefficient zero.
The coefficients are rational by solving an invertible row minor.
Every basis column contains a one, so the nonnegative equation
$X\alpha=\mathbf1$ implies $\alpha_i\le1$. Summing its rows gives
$21m\sum_i\alpha_i=72m$. $\square$

Zero coefficients must be permitted in this lemma. They are included
in the enumeration below; the computation ultimately finds that no
full-rank slice in this parameter ratio has a zero coefficient.

## 3. A complete finite bound

**Lemma 3.** After permuting basis columns, the vector in Lemma 2 has
the form $\alpha=a/(7h)$, where
$$
\begin{split}
 &1\le h\le10,\qquad
 0\le a_1\le\cdots\le a_8\le\min(7h,32),\\
 &\sum_i a_i=24h,\qquad \gcd(7h,a_1,\ldots,a_8)=1. \tag{3}
\end{split}
$$

**Proof.** Select an invertible binary $8\times8$ row minor $M$ of
$X$. Cramer's rule writes $\alpha_i=N_i/\det M$, where $N_i$ replaces
column $i$ by ones. Subtract the first row from the other seven and
expand along the replaced column. Each remaining column consists
either of zeros and ones or of zeros and minus ones, according to
its first-row entry. Negating columns of the latter type turns the
minor into a binary $7\times7$ matrix.

For a binary $q\times q$ matrix $B$, the sign matrix
$$
 \begin{pmatrix}1&\mathbf1^T\\\mathbf1&J-2B\end{pmatrix}
$$
has determinant of magnitude $2^q|\det B|$. Hadamard's inequality
therefore gives
$$
 |\det B|\le\frac{(q+1)^{(q+1)/2}}{2^q}. \tag{4}
$$
For $q=7$ the bound is 32, so $|N_i|\le32$.

Write $\alpha=a/D$ in primitive form with $D>0$. The common reduced
denominator $D$ divides $|\det M|$, and hence $|a_i|\le|N_i|\le32$.
Equation (2) also gives $0\le a_i\le D$. Since $\sum\alpha_i=24/7$
in lowest terms, $D=7h$ and $\sum a_i=24h$. Thus
$24h\le8\cdot32=256$, giving $h\le10$. Sort the coordinates.
$\square$

For each normal in (3), define its full binary slice
$$
 P(a,h)=\{z\in\{0,1\}^8:a^Tz=7h\}. \tag{5}
$$
The distinct rows of $X$ form a spanning subset $S\subseteq P(a,h)$.
Every such subset is retained: testing just the full slice would be
insufficient, since deleting row types can admit additional column
coefficients.

## 4. Dual coefficients and the diagonal obstruction

Write $A=XY$ using the column basis. If $\beta$ is a column of $Y$,
equal column sums of $A$ and $X$ imply $\mathbf1^T\beta=1$.
The binary entries of $A$ imply $z^T\beta\in\{0,1\}$ for all $z\in S$.
Thus every column coefficient lies in the finite set
$$
 B(S)=\{\beta\in\mathbb Q^8:
 \mathbf1^T\beta=1,\ z^T\beta\in\{0,1\}\text{ for all }z\in S\}. \tag{6}
$$
It is finite because any eight independent rows in $S$ determine
$\beta$ from one of $2^8$ possible binary value assignments. This
description enumerates all possible coefficients, including negative
and fractional ones.

Let $z_u$ be row $u$ of $X$, and let $\beta_u$ be column $u$ of $Y$.
Looplessness gives $z_u^T\beta_u=0$. Since $X$ consists of columns of
$A$, (1) gives
$$
 AX=7m\mathbf1\mathbf1^T-3mX
   =X(7m\alpha\mathbf1^T-3mI_8).
$$
Cancelling the full-column-rank matrix $X$ from $XYX=AX$ and
transposing yields
$$
 \sum_{u=1}^{72m}z_u\beta_u^T
   =m\left(\mathbf1\frac{a^T}{h}-3I_8\right). \tag{7}
$$

**Lemma 4 (diagonal sign obstruction).** A spanning support $S$ cannot
occur if some coordinate $j$ has either of these properties:

1. $a_j/h>3$, and $z_j\beta_j\le0$ for every
   $(z,\beta)\in S\times B(S)$ with $z^T\beta=0$;
2. $a_j/h<3$, and $z_j\beta_j\ge0$ for every such pair.

**Proof.** In the first case, diagonal entry $j$ of the left side of
(7) is nonpositive and that of the right side is positive. In the
second case the signs are reversed. The argument holds for every
$m>0$. $\square$

The obstruction does not involve an integrality relaxation or a
numerical optimization status. It is a direct finite list of exact
sign inequalities.

## 5. Exhaustive calculation

**Lemma 5 (finite calculation).** Among all normals (3), exactly 24
have full-rank slices. All have $h=1$ and strictly positive coordinates.
Their 11,884 spanning supports all satisfy Lemma 4.

The supplement's `prove72.py` proves the lemma by the following complete
enumeration. It generates sorted tuples by choosing their largest
coordinate recursively, retaining the exact sum and primitive-gcd
conditions. A base-512 evaluation of
$\prod_i(1+x^{a_i})$ counts the subsets with sum $7h$; all coefficients
are at most 256, so the encoding introduces no carries. Slices with
fewer than eight patterns cannot span and are rejected. The remaining
slice masks are generated directly.

For rank tests the program works modulo 101. This is exact over
$\mathbb Q$ for these matrices: (4) at $q=8$ gives
$|\det B|\le9^{9/2}/2^8<77<101$ for every binary $8\times8$ minor.
A nonzero rational minor therefore cannot vanish modulo 101.

For each surviving slice, the program examines every subset of size
at least eight, retaining exactly the spanning subsets. On one
eight-row basis it performs rational Gauss–Jordan inversion, clears
denominators, and enumerates all 256 binary assignments. It filters
these by (6), then checks the signs of $z_j\beta_j$ over every allowed
pair $z^T\beta=0$. It records a contradicting coordinate for every
support. No solver library is imported.

The complete calculation has 2,868,388 sorted tuples, 2,840,585 primitive
tuples, 24 full-rank slices, 11,884 spanning supports, and 675,875 allowed
row/column pairs. The per-denominator counts and all support-coordinate
certificates are stored in `proof72.json`. The following table records
the finite catalogue and support counts.

| Normal $a$ | Row patterns | Spanning supports |
|---|---:|---:|
| $(1,1,1,1,3,3,7,7)$ | 8 | 1 |
| $(1,1,1,1,3,4,6,7)$ | 11 | 65 |
| $(1,1,1,2,2,3,7,7)$ | 10 | 19 |
| $(1,1,1,2,2,4,6,7)$ | 12 | 205 |
| $(1,1,1,2,2,5,5,7)$ | 12 | 211 |
| $(1,1,1,2,2,5,6,6)$ | 12 | 205 |
| $(1,1,1,2,3,4,5,7)$ | 13 | 689 |
| $(1,1,1,2,3,4,6,6)$ | 14 | 1795 |
| $(1,1,1,3,3,4,4,7)$ | 10 | 19 |
| $(1,1,1,3,3,4,5,6)$ | 12 | 205 |
| $(1,1,2,2,2,3,6,7)$ | 11 | 95 |
| $(1,1,2,2,2,4,5,7)$ | 13 | 689 |
| $(1,1,2,2,2,5,5,6)$ | 12 | 325 |
| $(1,1,2,2,3,3,5,7)$ | 12 | 205 |
| $(1,1,2,2,3,3,6,6)$ | 12 | 361 |
| $(1,1,2,2,3,4,4,7)$ | 14 | 1585 |
| $(1,1,2,2,3,4,5,6)$ | 13 | 893 |
| $(1,1,2,3,3,3,5,6)$ | 13 | 689 |
| $(1,1,2,3,3,4,5,5)$ | 12 | 325 |
| $(1,1,2,3,4,4,4,5)$ | 12 | 205 |
| $(1,2,2,2,3,3,4,7)$ | 14 | 1795 |
| $(1,2,2,2,3,3,5,6)$ | 12 | 205 |
| $(1,2,2,3,3,3,4,6)$ | 12 | 205 |
| $(1,2,2,3,3,4,4,5)$ | 13 | 893 |

**Proof of Theorem 1.** Lemmas 2 and 3 place every hypothetical graph
in one of the finitely enumerated slices. Its actual distinct row set
is one of the spanning supports covered by Lemma 5, and all its
column coefficients lie in (6). Lemma 4 contradicts (7). This excludes
the graph for every positive integer $m$. $\square$

## 6. Verification and scope

Running

```text
python3 prove72.py --workers 5 --output proof72.json
```

reconstructs the entire proof from the bounds, without reading the
supplied output. Our run completed in about nine seconds on five CPU
workers; runtime depends on the machine. The program uses only Python's
standard library and must be run without the `-O` flag. The exact
certificate output contains, for every normal, its binary row masks and
every spanning support together with a forbidden diagonal coordinate.

A separately implemented C++ enumerator chooses coordinates from
smallest to largest, explicitly evaluates all 256 subset sums, and
tests rank modulo 257. It agrees with the Python proof on every normal
and all ten coverage counts. Its only dependencies are a C++17 compiler
and OpenMP. It is an independent check of the normal enumeration, not a
required component of the Python proof.

As a positive control, we applied the rational dual enumeration to an
explicit DSRG$(32,14,7,5,7)$ from [5]. All its actual column coefficients
were recovered, and no diagonal obstruction was found. Its adjacency
equation was checked by complete integer two-walk counting. This
control detects an erroneous exclusion of realizable rank-eight data;
the proof itself rests on the exhaustive checks above.

The result excludes the displayed parameter ray and its complements.
Together with Theorems 6, 8, 10 and 11 below, this gives five excluded parameter rays.
It is not a classification of all rank-eight DSRGs. The nonnegative
basis lemma and determinant argument apply more broadly to regular
binary matrices, but the small catalogue and universal diagonal
obstruction here are specific to the ratio $24/7$ and the identity
(7).

## 7. The second excluded ray: order 100

**Theorem 6.** For every integer $m\ge1$, there is no DSRG with parameters

$$
(100m,35m,14m,9m,14m),
$$

and therefore none with complementary parameters

$$
(100m,65m-1,44m-1,44m-2,39m).
$$

**Finite reduction.** A hypothetical adjacency matrix satisfies
$A^2=14mJ-5mA$, has eigenvalues $35m,-5m,0$, and has rank eight.
The nonnegative-basis argument in Lemma 2 gives $X\alpha=1$ with
$\sum\alpha_i=20/7$. Write $\alpha=a/(7h)$ in primitive form. Lemma 3's
Cramer numerator bound gives $0\le a_i\le\min(7h,32)$ and $\sum a_i=20h$.
Here the denominator bound uses (4) at $q=8$: $7h$ divides the absolute
determinant of a binary $8\times8$ basis minor, which is less than 77.
Thus $1\le h\le10$.

Enumerating these bounds gives 3,738,156 sorted tuples. Exactly 75 normals
have full-rank slices: 30 with $h=1$ and 45 with $h=2$. The largest slice
has 21 row patterns. The complete catalogue and all denominator-specific
coverage counters are in `normals100.jsonl`. The argument of Section 4
gives the necessary identity

$$
\sum_u z_u\beta_u^T=m\left(2\mathbf1\frac{a^T}{h}-5I_8\right),
\qquad z_u^T\beta_u=0. \tag{8}
$$

**Fourteen immediate exclusions.** If all $a_i>0$ and $a_8=7h$, the only
row pattern with coordinate 8 equal to one is $e_8$. Every spanning
support contains it, so every $\beta\in B(S)$ has $\beta_8\in\{0,1\}$.
Every allowed loopless pair therefore has $z_8\beta_8=0$, contradicting
entry $(8,8)$ of (8), which equals $9m>0$. Fourteen normals are excluded
this way, without support enumeration.

**Complete support orbits.** For each of the other 61 normals, let
$G_a$ be the full group of coordinate permutations preserving $a$.
It acts on the full row slice, on its subsets, and on the dual
coefficients. Equation (8) is invariant under this simultaneous
permutation. It therefore suffices to examine one representative of
every spanning-support orbit, with no graph-symmetry assumption.

The independent checker explicitly enumerates every permutation in
$G_a$. For each support mask not already covered, it calculates every
image and marks its entire orbit. It checks that the orbit sizes sum to
$\sum_{j=8}^{|P|}\binom{|P|}{j}$, ensuring coverage of every subset of
size at least eight. It then keeps the spanning orbits and enumerates
all their dual coefficients. Across these 61 normals there are 272,914
spanning orbits, covering 3,923,137 spanning supports. This count does
not include supports under the 14 analytically excluded normals.

**Exact separators.** All but 1,499 spanning orbits have a single
coordinate sign contradiction, as in Lemma 4 with target diagonal
$2a_j/h-5$. For each of the remaining orbits we supply an integer
matrix $Q$ such that

$$
\langle Q,z\beta^T\rangle\ge0
\quad\text{for every }(z,\beta)\in S\times B(S),\quad z^T\beta=0,
$$

but

$$
\left\langle Q,2\mathbf1a^T-5hI_8\right\rangle<0. \tag{9}
$$

Here $\langle Q,T\rangle=\sum_{i,j}Q_{ij}T_{ij}$. Summing the first
inequality over vertices and using (8), multiplied by $h>0$, contradicts
(9). This is the elementary separating-hyperplane form of Farkas'
lemma. The supplement provides every $Q$ as a sparse list of integer
entries; numerical optimization was used to find them, but plays no
role in their verification or in exhaustive coverage.

The standalone standard-library checker `prove100.py` reconstructs all
75 normals, all relevant support orbits, and all duals, and checks the
separators with integer arithmetic. It checks 16,739,092 allowed pairs
in total, including the cases settled by a single coordinate. This
proves Theorem 6 for every $m\ge1$.

**Independent verification.** The discovery traversal used adjacent
transpositions of equal coefficients and breadth-first orbit expansion.
The checker uses the full permutation group and a separate traversal.
The discovery computed duals using rational Gauss–Jordan inversion;
the checker inverts modulo 1009, recovers a common integer denominator
and numerator matrix, and explicitly verifies $MN=DI$ over the integers
before using $N/D$. Its rank tests use the field of order 131 rather
than the generator's field of order 257. Both fields exceed the proved
binary determinant bound. All independent orbit and support counts
agree with the discovery run. A positive control on the realizable
32-vertex graph also recovers every actual dual coefficient.

Run the proof with

```text
python3 prove100.py --workers 5 --certificates certificates100.json \
  --catalogue normals100.jsonl --output rebuilt_proof100.json
```

This completed in about 49 seconds with five CPU workers in our run.
The catalogue is independently regenerated internally and compared with
the supplied file; the certificates are checked rather than trusted.
No solver or nonstandard Python package is needed. The C++ catalogue
can also be rebuilt with `regular_rank8_normals.cpp`, using arguments
`--ratio-num 20 --ratio-den 7`.

The supplement contains all five proofs and exact output reports,
integer separators for both computational cone exclusions, independent normal
generators, realizable positive controls, and a dated excerpt for all ten entries.

## 8. A third ray with elementary support exclusions

The third case illustrates that the finite-basis method can expose a
short counting proof instead of requiring a large support enumeration.

**Lemma 7 (sign-matrix denominator bound).** If $M$ is an invertible
binary $r\times r$ matrix, $M\alpha=\mathbf1$, and
$s=\mathbf1^T\alpha\ne2$, then

$$
|\det M|\le\frac{r^{r/2}}{2^r|1-s/2|}. \tag{10}
$$

**Proof.** The determinant lemma gives
$\det(J-2M)=(-2)^r\det M(1-s/2)$. Apply Hadamard's inequality to the
sign matrix $J-2M$. $\square$

As before, the primitive common denominator of $\alpha$ divides
$|\det M|$. For the ratios in Theorems 1 and 6, (10) even gives
$h\le3$ and $h\le5$, respectively; their supplied checkers retain the
broader complete bounds already proved in Section 3.

**Theorem 8.** For every integer $m\ge1$, there is no DSRG with parameters

$$
(81m,63m,56m,47m,56m),
$$

or with complementary parameters

$$
(81m,18m-1,11m-1,11m-2,2m).
$$

**Proof.** Suppose $A$ is such an adjacency matrix and put $B=J-A$.
This matrix complement includes diagonal ones; it is not the loopless
digraph complement. It is a regular binary matrix of degree $18m$,
satisfies

$$
B^2=2mJ+9mB. \tag{11}
$$

On the all-ones line its eigenvalue is $18m$, and on the complementary
invariant subspace its eigenvalues are $9m$ and zero. Since its trace is
$81m$, the multiplicity of $9m$ is seven, so $B$ has rank eight.

Choose a nonnegative column basis $X$ of $B$ as in Lemma 2. Then
$X\alpha=\mathbf1$ and $\sum\alpha_i=9/2$. For an invertible basis
minor, (10) gives $|\det M|\le64/5<13$. Hence the primitive normal
$\alpha=a/(2h)$ satisfies

$$
1\le h\le6,\qquad0\le a_1\le\cdots\le a_8\le2h,
\quad\sum_i a_i=9h,\quad\gcd(2h,a_1,\ldots,a_8)=1. \tag{12}
$$

There are only 5,475 sorted tuples before the gcd filter in (12). Independent Python and
C++ enumerations agree that exactly nine have full-rank slices. The
standalone `prove81dense.py` regenerates all of them and checks their
pattern descriptions. Here is the entire catalogue.

| $h$ | Normal $a$ | Row patterns | Exclusion |
|---:|---|---:|---|
| 1 | $(0,0,1,1,1,2,2,2)$ | 24 | Three pairs |
| 1 | $(0,1,1,1,1,1,2,2)$ | 24 | Five-cycle |
| 1 | $(1,1,1,1,1,1,1,2)$ | 22 | Positive singleton |
| 2 | $(1,1,1,1,2,4,4,4)$ | 10 | Positive singleton |
| 2 | $(1,1,1,1,3,3,4,4)$ | 11 | Positive singleton |
| 2 | $(1,1,1,2,2,3,4,4)$ | 12 | Positive singleton |
| 2 | $(1,1,2,2,2,3,3,4)$ | 11 | Positive singleton |
| 2 | $(1,1,2,2,3,3,3,3)$ | 11 | Column sums |
| 3 | $(1,1,2,2,4,5,6,6)$ | 8 | Positive singleton |

For every selected basis column $X_i$, (11) gives

$$
BX_i=2m\mathbf1+9mX_i,\qquad\mathbf1^TX_i=18m. \tag{13}
$$

We now exclude every possible actual support under these nine normals.

**Positive singleton case.** Six normals have all coefficients positive
and some $\alpha_j=1$. The only row pattern containing coordinate $j$
is $e_j$. All rows of $B$ indexed by $W=\operatorname{supp}X_j$ are
therefore identical, since $B=XY$. The diagonal ones imply that the
whole $W\times W$ block is one. Thus $B\mathbf1_W(u)=18m$ for $u\in W$,
whereas (13) requires $11m$. This excludes all six normals.

**Column-sum case.** For $a=(1,1,2,2,3,3,3,3)$ and $h=2$, every row
pattern containing a weight-three coordinate must also contain one of
the two weight-one coordinates. It contains at most one weight-three
coordinate. Consequently

$$
z_5+z_6+z_7+z_8\le z_1+z_2
$$

for every row. Summing contradicts the equal column sums of $X$:
$4\cdot18m\le2\cdot18m$.

**Three-pair case.** For $a=(0,0,1,1,1,2,2,2)$ and $h=1$, ignore the
two zero-weight coordinates. Each remaining pattern is a singleton
weight-two coordinate or a pair of weight-one coordinates. The three
singleton supports have size $18m$ each. The three pair cells each have
size $9m$, since each weight-one column has $18m$ ones. If $i,j,k$ are
the three weight-one coordinates, the indicator of the pair cell $C_{ij}$
is $(X_i+X_j-X_k)/2$. Equation (13) therefore implies

$$
B\mathbf1_{C_{ij}}=m\mathbf1+9m\mathbf1_{C_{ij}}. \tag{14}
$$

At a vertex in this $9m$-element cell, (14) requires $10m$ ones inside
it, which is impossible. The unused zero-weight coordinates do not
alter this coarse partition or its indicator identity.

**Five-cycle case.** Finally let $a=(0,1,1,1,1,1,2,2)$ and $h=1$.
The two singleton weight-two supports are disjoint sets of size $18m$.
The other $45m$ vertices occupy pair cells $C_{ij}$ on the five
weight-one coordinates. Let $G$ be the simple graph whose edges are
the nonempty pair cells, with edge weight $w_{ij}=|C_{ij}|$. Each
point has weighted degree $18m$.

Fix $u\in C_{ij}$, and let $c_f$ count the ones in row $u$ of $B$
whose columns lie in pair cell $f$. The two endpoint coordinates in
(13) have values $11m+11m$; the other three have values $2m+2m+2m$.
Subtracting gives

$$
c_{ij}-\sum_{f\cap\{i,j\}=\varnothing}c_f=8m.
$$

Thus every nonempty cell has size at least $8m$, and $G$ has maximum
degree two. Every point has positive degree. If a point has degree one,
its incident edge has weight $18m$, forcing its neighbor also to have
degree one. The corresponding two basis columns are then identical,
a contradiction. Hence $G$ is two-regular on five vertices, so it is a
five-cycle.

The weighted-degree equations on this odd cycle force every edge weight
to equal $9m$. Its point-edge incidence matrix is invertible over
$\mathbb Q$: in its kernel, successive edge coordinates alternate in
sign, and the odd cycle forces them all to vanish. Each cell indicator
therefore lies in the span of the five weight-one columns, say
$\mathbf1_C=\sum_i c_iX_i$. Summing coordinates gives
$9m=18m\sum_i c_i$, so $\sum_i c_i=1/2$. Equation (13) again gives
(14), requiring $10m$ ones in a $9m$-element cell. This final contradiction
proves Theorem 8. $\square$

The finite calculation here is only the nine-normal catalogue. The
support exclusions are the four elementary arguments above, and cover
arbitrary refinements in the zero-weight coordinates. Run

```text
python3 prove81dense.py --output rebuilt_proof81dense.json
```

The checker uses only the standard library. The independent C++ generator
can reproduce the catalogue with `--ratio-num 9 --ratio-den 2 --max-h 6`.
This theorem concerns a different parameter ray from the sparse
$(81,24,8,5,8)$ case, which is settled separately in Theorem 11.

## 9. A row-class bound and the dense order-96 ray

The same finite-basis method gives a fourth result, now at rank nine.
The support argument uses a general capacity bound for identical rows.

**Lemma 9 (row-class capacity).** Suppose $B$ is a binary matrix with
diagonal ones, constant row and column sum $k$, and
$B^2=aJ+qB$, where $a+q<k$. Let $W$ be the support of a column.
Any set $C\subseteq W$ of identical rows of $B$ has size at most $k-q$.

**Proof.** We have $|W|=k$ and $B\mathbf1_W=a\mathbf1+q\mathbf1_W$.
For any column indexed by $v$, put $e=\sum_{w\in W}B_{wv}$. If
$e>k-q$, then, for every $u\in W$, at least

$$
(a+q)+e-k>a
$$

vertices of $W$ contribute to $(B^2)_{uv}$. Hence $B_{uv}=1$ for every
$u\in W$, since $B_{uv}=0$ would give $(B^2)_{uv}=a$. Thus $e=k$,
and the whole column is $\mathbf1_W$ by its column sum.

Now suppose $|C|>k-q$, and take $u\in C$. Every outneighbor $v$ of
$u$ has a one in every row of $C$, so the preceding argument makes
its column $\mathbf1_W$. Since $B_{vv}=1$, this implies $v\in W$.
All $k$ outneighbors of $u$ therefore lie in $W$, contradicting
$B\mathbf1_W(u)=a+q<k$. $\square$

**Theorem 10.** For every integer $m\ge1$, there is no DSRG with parameters

$$
(96m,80m,75m,65m,75m),
$$

or with complementary parameters

$$
(96m,16m-1,11m-1,11m-2,m).
$$

**Proof.** Put $B=J-A$, including diagonal ones. It is binary, has
degree $16m$, and satisfies

$$
B^2=mJ+10mB. \tag{15}
$$

Its eigenvalues are $16m$, $10m$, and zero. The trace $96m$ forces
multiplicity eight for $10m$, so its rank is nine. Choose a nonnegative
column basis $X$ with $X\alpha=\mathbf1$ and $\sum\alpha_i=6$.
Lemma 7 gives $|\det M|\le19683/1024<20$ for an invertible basis minor.
The primitive normal $\alpha=a/h$ therefore satisfies

$$
1\le h\le19,\qquad0\le a_1\le\cdots\le a_9\le h,
\quad\sum_i a_i=6h,\quad\gcd(h,a_1,\ldots,a_9)=1. \tag{16}
$$

There are 173,536 sorted tuples before the gcd filter. Exactly six
give full-rank slices $a^Tz=h$:

| $h$ | Normal $a$ | Row patterns |
|---:|---|---:|
| 1 | $(0,0,0,1,1,1,1,1,1)$ | 48 |
| 2 | $(0,1,1,1,1,2,2,2,2)$ | 20 |
| 2 | $(1,1,1,1,1,1,2,2,2)$ | 18 |
| 3 | $(1,1,1,1,2,3,3,3,3)$ | 12 |
| 3 | $(1,1,1,2,2,2,3,3,3)$ | 13 |
| 4 | $(1,1,2,2,3,3,4,4,4)$ | 10 |

The standard-library checker `prove96dense.py` regenerates the complete
list and checks its pattern descriptions. Its rank tests use the field
of order 509. Equation (4) at $q=9$ bounds every binary determinant by
$10^5/2^9<196$, so these rank tests are exact over $\mathbb Q$.
An independent C++ generator uses the opposite tuple order and the field
of order 257; all normals, masks, and denominator-specific coverage
counts agree.

By Lemma 9, a class of identical $B$ rows lying in any column support
has size at most $16m-10m=6m$.

For each of the four positive normals, a coefficient $\alpha_j=1$
forces every row in $\operatorname{supp}X_j$ to have pattern $e_j$.
These $16m$ rows of $B=XY$ are identical, contradicting the bound $6m$.

For $a=(0,1,1,1,1,2,2,2,2)$, choose a coordinate with numerator two.
The $16m$ rows in its column support have just two possible $X$ patterns,
differing only in the zero-coefficient coordinate. They form at most
two classes of identical $B$ rows. Lemma 9 would give $16m\le12m$.

For $a=(0,0,0,1,1,1,1,1,1)$, the six positive-coefficient columns
partition all $96m$ vertices into six $16m$-vertex cells. Each of the
three zero-coefficient basis columns has $16m$ ones. Hence at least
$96m-3\cdot16m=48m$ vertices have zero in all three of those coordinates.
Within each of the six cells, these vertices have the same $X$ row
$e_j$, and thus the same $B$ row. Lemma 9 bounds their total by
$6\cdot6m=36m$, a contradiction. These cases exhaust (16) and prove
Theorem 10. $\square$

Run the finite check with

```text
python3 prove96dense.py --output rebuilt_proof96dense.json
```

The independent catalogue can be regenerated with `regular_rank9_normals.cpp`
and arguments `--ratio-num 6 --ratio-den 1 --max-h 19 --threads 5`.
No actual-support enumeration is needed. In particular, the first normal
has 48 possible row patterns, but Lemma 9 excludes all of its supports
through the single counting argument above.

## 10. A fifth ray: the sparse order-81 case

**Theorem 11.** For every integer $m\ge1$, there is no DSRG with parameters

$$
(81m,24m,8m,5m,8m),
$$

or with complementary parameters

$$
(81m,57m-1,41m-1,41m-2,38m).
$$

The base tuples $(81,24,8,5,8)$ and $(81,56,40,39,38)$ are both marked
unresolved in the dated table [2]. This is a different order-81 ray from
Theorem 8.

**Complete normal reduction.** A hypothetical adjacency matrix satisfies
$A^2=8mJ-3mA$. Its eigenvalues are $24m,-3m,0$, and the trace forces
multiplicity eight for $-3m$, hence rank nine. Lemma 2's argument applies
with nine basis columns and gives a nonnegative normal with sum $27/8$.
Lemma 7 bounds a binary basis minor by

$$
|\det M|\le\frac{19683}{352}<56.
$$

The primitive denominator is a multiple of eight and divides this
integer determinant. Every normal is therefore represented by

$$
\alpha=\frac{a}{8h},\quad 1\le h\le6,\quad
0\le a_1\le\cdots\le a_9\le8h,\quad
\sum_i a_i=27h,\quad\gcd(8h,a_1,\ldots,a_9)=1. \tag{17}
$$

The full slice is $P=\{z\in\{0,1\}^9:a^Tz=8h\}$. The complete
normal enumeration gives the following counts; the third column counts
normals whose binary slices span all nine coordinates.

| $h$ | Sorted tuples before the gcd filter | Full-rank normals |
|---:|---:|---:|
| 1 | 645 | 142 |
| 2 | 27,852 | 530 |
| 3 | 348,584 | 87 |
| 4 | 2,356,897 | 0 |
| 5 | 10,981,753 | 0 |
| 6 | 39,849,113 | 0 |
| Total | 53,564,844 | 759 |

The largest slice has 26 patterns. Two independent C++ programs agree on
every normal, every pattern mask, and every coverage counter. One builds
sorted tuples from the smallest coordinate and tests row rank modulo
257. The other starts with the largest coordinate and tests column rank
modulo 331. Both rank tests are exact over the rationals because (4)
bounds every binary $9\times9$ determinant by $10^5/2^9<196$.

**Support and dual coverage.** Let $S\subseteq P$ be the actual distinct
row set of the basis matrix. It spans nine coordinates. Define $B(S)$
as in (6), now in dimension nine. Every column coefficient of the graph
belongs to this set, and the vertex pairs satisfy

$$
z_u^T\beta_u=0,\qquad
\sum_u z_u\beta_u^T=\frac{m}{h}
\left(\mathbf1a^T-3hI_9\right). \tag{18}
$$

For 171 normals, all coefficients are positive and $a_9=8h$. The only
pattern using coordinate nine is $e_9$, so all allowed loopless pairs
have $z_9\beta_9=0$. The corresponding target diagonal in (18) is
$5m>0$. These normals are excluded analytically.

For the remaining 588 normals, the checker constructs the full group of
coordinate permutations preserving $a$, takes one representative per
support orbit, and marks every image. Its orbit sizes sum, separately
for every normal, to $\sum_{j=9}^{|P|}\binom{|P|}{j}$. This accounts for
all 1,089,323,524 subsets of size at least nine. Exactly 470,210,506 of
them span, forming 30,523,586 orbits. These permutations only identify
equivalent basis descriptions; no symmetry of the graph is assumed.

For each spanning representative, choose nine independent rows and
invert their binary matrix. The compiled checker uses fraction-free
elimination, checks every division for exactness, and verifies its
integer inverse identity $MN=DI$ with $D>0$ before using it. Enumerating
all 512 binary assignments to those rows, imposing $\sum\beta_i=1$,
and retaining only binary pairings with all of $S$ gives exactly $B(S)$.
Caching repeated row bases changes no condition. Integer masks record
which patterns each dual permits and which give pairing zero.

**Exact contradictions.** Of the 30,523,586 spanning orbits, 30,479,954
have a diagonal sign contradiction as in Lemma 4. For each of the
remaining 43,632 orbits, the supplement gives an integer matrix $Q$
with

$$
\langle Q,z\beta^T\rangle\ge0
\quad\text{for all }z\in S,\ \beta\in B(S),\ z^T\beta=0,
\qquad
\left\langle Q,\mathbf1a^T-3hI_9\right\rangle<0. \tag{19}
$$

Every inequality is checked with integers after clearing the positive
dual denominator. Summing over vertices contradicts (18), since
$m/h>0$. These homogeneous contradictions exclude every positive
multiple, proving Theorem 11. The full enumeration accounts for
2,622,309,282 allowed row/dual pairs. No optimizer is used by the proof
checker; numerical optimization only supplied candidate separators,
which were then verified exactly. $\square$

**Reproduction and independent checks.** Run

```text
python3 prove81.py --workers 5 --output rebuilt_proof81.json
```

This uses Python's standard library and a C++17 compiler. It freshly
regenerates the entire normal catalogue, compares the supplied coverage
records, then performs the full support and certificate check. Both
Python and C++ assertions must remain enabled. The compiled support
phase took about 45 seconds with five workers; the independent normal
enumeration took about 30 seconds on one worker. Hardware affects timing.

The certificate file uses ordinary JSON integer arrays, separator banks,
and positive differences between sorted support masks. The decoder
recovers the full sparse integer matrices before checking them. The
encoding was checked losslessly against all 43,632 original certificates.

A separate Python implementation, selected with `--engine python`, uses
exact `Fraction` inversion and independently reproduces all 759 normal
records. Every support, orbit, exclusion, and allowed-pair count agrees,
as does the classification of all 171 analytic exclusions. The separate
independent normal-catalogue audit checks all normals and row-pattern masks.
A separate discovery traversal using adjacent transpositions
and breadth-first orbit expansion also agrees on 718 complete normal
records. As a positive control, both dual implementations recover every
actual column coefficient and vertex pair of an explicit
DSRG$(96,16,3,1,3)$; its adjacency equation is independently verified by
ordered-path counting. This control is included as `check_control96.py`.

## 11. Binary indicators and basis exchange: a sixth ray

**Theorem 12.** For every integer $m\ge1$, there is no DSRG with parameters

$$
(50m,35m,28m,23m,28m),
$$

or with complementary parameters

$$
(50m,15m-1,8m-1,8m-2,3m).
$$

The two base entries are $(50,35,28,23,28)$ and $(50,14,7,6,3)$.
This proof adds a reduction by exchanging actual graph columns into a
nonnegative basis. It avoids enumerating every subset of a 32-pattern
slice and needs no optimization certificates.

Put $B=J-A$. Then $B$ is binary with diagonal ones and satisfies

$$
B\mathbf1=B^T\mathbf1=15m\mathbf1,
\qquad B^2=3mJ+5mB. \tag{20}
$$

Its eigenvalues are $15m$, $5m$, and zero. Since
$\operatorname{tr}B=50m$, the multiplicity of $5m$ is seven and the rank
is eight. Lemma 2 gives a binary column basis $X$ with
$X\alpha=\mathbf1$, $\alpha\ge0$, and $\sum\alpha_i=10/3$.
Lemma 7 bounds every invertible row minor by $|\det M|\le24$.
Thus, after sorting coordinates, every normal has the form

$$
\alpha=\frac a{3h},\quad 1\le h\le8,\quad
0\le a_0\le\cdots\le a_7\le3h,\quad
\sum a_i=10h,\quad \gcd(3h,a_0,\ldots,a_7)=1. \tag{21}
$$

The enumeration covers 250,769 sorted tuples and yields 63 full-rank
binary slices: six at $h=1$, 25 at $h=2$, 24 at $h=3$, and eight at
$h=4$. The other denominators yield none.

**Lemma 13 (binary indicator bound).** Suppose a binary matrix $B$ has
constant row and column sum $k$, satisfies $B^2=uJ+qB$, and has
$q>0$ and $k>u$. Let $X$ consist of independent columns of $B$.
If $c\ne0$ and $f=Xc$ is binary, then

$$
\sum_i c_i\ge\frac q{k-u}.
$$

**Proof.** Put $s=\sum_i c_i$ and $C=\operatorname{supp}f$.
Column regularity gives $|C|=ks$. Since the columns of $X$ are
independent, $C$ is nonempty. Also $BX=u\mathbf1\mathbf1^T+qX$,
so $Bf=us\mathbf1+qf$. At a vertex of $C$, this counts $us+q$
ones into a set of size $ks$. Hence $us+q\le ks$. $\square$

This is the usual indicator/eigenvector mechanism underlying intriguing
sets and regular sets; see [6, Sections 1–3] for the related strongly
regular graph framework. We use the elementary directed calculation
above and do not claim the general indicator principle as new.

For (20), Lemma 13 requires $\sum c_i\ge5/12$. To enumerate all binary
forms on a spanning row set, assign zero or one independently to its
eight basis rows and solve for $c$. This gives exactly 256 possibilities.
Here we do **not** impose $\sum c_i=1$, since these forms need not be
actual columns of $B$. For 60 of the 63 full slices, a nonzero binary
form violates the bound. It remains binary and nonzero on every
spanning subset, so these exclusions cover all actual supports.
The regenerated rational witnesses are recorded in the proof output.

One further normal is $(1,1,1,1,1,1,1,3)/3$. Its eighth column can be
one only in row pattern $(0,0,0,0,0,0,0,1)$. Its $15m$ supporting
vertices therefore have identical rows of $B$. Diagonal ones force an
all-one square on these vertices, contradicting $(B^2)_{vv}=8m$.
Thus every hypothetical graph has a nonnegative basis whose normal,
after coordinate permutation, is one of

$$
a^{\mathrm I}=(0,1,1,1,1,1,2,3),\qquad
 a^{\mathrm {II}}=(1,1,1,1,1,1,2,2),\qquad \alpha=a/3. \tag{22}
$$

Both full slices have 32 row patterns. Moreover, every nonnegative
column basis of that graph must have one of these two normals, since
the preceding exclusions apply to any such basis.

Write $B=XY$, with row $z_v^T$ of $X$ and column $\beta_v$ of $Y$ at
vertex $v$. Column regularity gives $\mathbf1^T\beta_v=1$.
The matrix identities give

$$
YX=3m\alpha\mathbf1^T+5mI,
\qquad Y\mathbf1=15m\alpha.
$$

Subtracting the diagonal entries of the first equation from the
coordinates of the second yields the **gap identity**

$$
\sum_v\beta_v(j)(1-z_v(j))=m(4a_j-5),\qquad 0\le j<8. \tag{23}
$$

For $j=0$, the right side is negative in both cases of (22).
Consequently some actual column coefficient $\beta$ has $\beta_0<0$.
We use only this necessary condition; retaining extra possibilities
cannot invalidate a nonexistence proof.

**Lemma 14 (basis exchange restriction).** Every such actual $\beta$
occurs among the following finite candidates. Let $g$ run through all
coordinate permutations of the two integer vectors in (22). For each
$j$ with $a_j>0$ and $g_j>0$, form

$$
\beta_j=\frac{a_j}{g_j},\qquad
\beta_i=\frac{a_i-g_i}{g_j}\quad(i\ne j), \tag{24}
$$

and retain the distinct candidates satisfying $\beta_0<0$.

**Proof.** Choose $j$ with $\beta_j>0$ minimizing
$r=\alpha_j/\beta_j$. Such a coordinate exists because
$\sum\beta_i=1$. Every coordinate with $\beta_j>0$ has
$\alpha_j>0$: the only possible zero coordinate of $\alpha$ is zero,
where $\beta_0<0$. Hence $r>0$.
Replace column $j$ of $X$ by the actual binary column $X\beta$.
The resulting columns are independent because $\beta_j\ne0$.
The new normal is
$\gamma_j=r$ and $\gamma_i=\alpha_i-r\beta_i$ for $i\ne j$.
The minimum-ratio choice gives $\gamma\ge0$. This new nonnegative
basis must also have a normal from (22), so $\gamma=g/3$ for one of
the enumerated permutations. Solving these equations gives (24).
$\square$

The enumeration gives 1,078 candidates for case I and 301 for case II.
For each, put
$P_\beta=\{z\in P:z^T\beta\in\{0,1\}\}$; an actual graph using
this column has all rows in $P_\beta$. Rank deficiency excludes 657
and 55 candidates, respectively. Lemma 13 excludes another 355 and
215. The remaining 66 and 31 candidates are integral and have the
following eight orbits under coordinate permutations preserving $a$
and coordinate zero.

| Normal | Representative $\beta$ | Orbit size | $|P_\beta|$ |
|---|---|---:|---:|
| I | $(-1,-1,0,0,0,1,1,1)$ | 20 | 20 |
| I | $(-1,-1,0,0,1,1,1,0)$ | 30 | 20 |
| I | $(-1,0,0,0,0,0,1,1)$ | 1 | 22 |
| I | $(-1,0,0,0,0,1,0,1)$ | 5 | 24 |
| I | $(-1,0,0,0,1,1,0,0)$ | 10 | 24 |
| II | $(-1,0,0,0,0,0,1,1)$ | 1 | 22 |
| II | $(-1,0,0,0,0,1,0,1)$ | 10 | 24 |
| II | $(-1,0,0,0,1,1,-1,1)$ | 20 | 20 |

These eight row universes cover every hypothetical graph. They need
not be disjoint. For each universe, enumerate every spanning subset
$S$ up to its full coefficient-preserving coordinate stabilizer.
Enumerate all binary forms on a row basis as above. If Lemma 13 applies,
exclude $S$. Otherwise, retain all sum-one forms binary on $S$, which
include every possible actual dual column. Diagonal ones require
$z^T\beta=1$ at every vertex. Equation (23) therefore requires, for
each $j$, an allowed pair with

$$
z_j=0,\qquad (4a_j-5)\beta_j>0. \tag{25}
$$

If none exists for any required coordinate, its sum in (23) cannot
have the required sign. Every support surviving the indicator bound
fails this sign test. No cone optimization remains.

The full calculation has the following counts. Supports are counted
separately under the eight root cuts, so these are support-cut incidences.

| Quantity | Count |
|---|---:|
| Subsets of size at least eight | 59,282,379 |
| Spanning subsets | 39,668,344 |
| Spanning support orbits | 2,102,002 |
| Indicator exclusions | 2,047,652 |
| Gap-sign exclusions | 54,350 |
| Allowed pairs checked in the gap phase | 2,775,424 |

Orbit sizes sum to the full binomial subset count separately for each
root cut. The exclusions are exact and homogeneous in $m$; thus they
prove Theorem 12 for every positive integer $m$. Coordinate permutations
identify equivalent descriptions and impose no graph automorphism.

**Reproduction and controls.** Run

```text
python3 prove50.py --output rebuilt_proof50.json
python3 check_control50.py --output rebuilt_positive_control50.json
```

The first program regenerates all normals, indicator exclusions, basis
exchanges, and root cuts before compiling and running the support checker.
It uses only the Python standard library and a C++17 compiler. The support
phase took about ten seconds on one CPU. It checks every fraction-free
division and the integer identity $MN=DI$ for each inverse used.

An independent Python support implementation, selected with
`--engine python`, instead uses exact fractions, a different prime for
rank, and ascending rather than descending orbit representatives. Its
complete eight-cut run agrees on every coverage, exclusion, and pair
count. Independent normal and multiset-permutation enumerators also check the
normal catalogue and the complete negative-dual list. The positive
control reconstructs the existing DSRG$(32,14,7,5,7)$ from [5] and tests
$B=J-A$, which satisfies $B^2=9J+2B$. Its indicator threshold is $2/9$.
Both implementations retain all actual column coefficients and diagonal
vertex pairs, and direct ordered-path counting checks the graph itself.

## 12. Rebasing zero coefficients before an exchange

Lemma 14 used the fact that only one normal coordinate could vanish.
A standard minimal-positive-dependence argument removes that restriction,
provided one first changes the zero-weight columns of the basis. This
geometric observation does not alter any of the six proof computations.

**Proposition 15 (zero-coordinate rebasing).** Let $B$ be a square matrix
with positive common row and column sum $k$. Let $X$ be an actual column
basis with $B=XY$, $X\alpha=\mathbf1$, and $\alpha\ge0$.
Write $P=\{i:\alpha_i>0\}$ and $Z=\{i:\alpha_i=0\}$, and suppose
$Z\ne\varnothing$. There is another actual column basis, retaining
$X_P$ and the same normal coefficient multiset, in which an actual column
has coefficient vector $\beta$ satisfying

$$
\beta_Z\le0,\qquad \beta_Z\ne0.
$$

In this basis, $\beta$ admits a nonnegative exchange with a strictly
positive minimum ratio.

**Proof.** Regularity and independence give $Y\mathbf1=k\alpha$.
Project each actual coefficient column onto the coordinates $Z$, obtaining
$v_j=Y_{Z,j}$. These vectors span a space of dimension $|Z|$, and
$\sum_jv_j=0$. Omit zero vectors and choose a positive dependence of
minimal nonempty support,

$$
\sum_{j\in C}c_jv_j=0,\qquad c_j>0.
$$

Minimality implies that these vectors have rank $|C|-1$. Otherwise a
second independent kernel vector permits changing the coefficients until
one vanishes while all remain nonnegative, giving a smaller positive
dependence. In particular, any $|C|-1$ of them are independent and
$|C|\ge2$.

Choose $j_0\in C$, and extend the other $|C|-1$ projected vectors to a
basis of the projected space using projected actual columns. Together
with $X_P$, the corresponding actual columns form a basis of the column
space of $B$. Its normal is still $\alpha_P$ on the retained columns
and zero on the new columns. In this basis, the zero-block coordinates
of the actual column indexed by $j_0$ are $-c_j/c_{j_0}$ on the selected
circuit columns, and zero on the remaining ones. They are nonpositive
and not all zero.

All basis columns and this actual column have the same positive column
sum $k$, so $\sum_i\beta_i=1$. Thus some $\beta_i$ is positive, and
all its positive coordinates lie in $P$. The minimum of
$\alpha_i/\beta_i$ over these coordinates is strictly positive.
The usual minimum-ratio exchange therefore gives a nonnegative normal.
$\square$

If the admissible nonnegative normals form a finite family closed under
coordinate permutations, Proposition 15 gives a finite complete list
of possible required columns for any normal with zeros. Enumerate the
other normal $\gamma$ and a coordinate $j$ with
$\alpha_j,\gamma_j>0$, and use

$$
\beta_j=\alpha_j/\gamma_j,\qquad
\beta_i=(\alpha_i-\gamma_i)/\gamma_j\quad(i\ne j).
$$

Retain $\beta_Z\le0$ with a nonzero zero block and pass to its allowed
binary row slice. The conclusion concerns the existence of a suitable
rebased representation of each graph. It does not say that every
original basis already contains such a column, nor that the exchange
reduces the number of zero normal coefficients. It also does not
ensure that a resulting row cut is smaller; that must be checked in
each application.

The geometric proposition itself needs no binary-entry assumption.
For example, take $\alpha=(1,1,0,0)$ and actual coefficient vectors

$$
e_0,e_1,e_2,e_3,(1,1,-2,1),(1,1,1,-2).
$$

Their nonzero projections onto $Z$ are
$(1,0),(0,1),(-2,1),(1,-2)$, none of which is nonpositive in both
coordinates. The positive dependence
$3(1,0)+2(-2,1)+(1,-2)=0$ permits rebasing; the last column then has
full coefficient vector $(3,3,-3,-2)$ and a positive exchange ratio
$1/3$. The supplement realizes this example as a regular nonnegative
rational matrix of order six; it is not a DSRG example.

The supplement also checks actual binary partition-family graphs [7] of
orders 40, 96, and 176, of ranks six, nine, and twelve, with two, three,
and four zero normal coefficients. These are controls for the algebra,
not additional parameter claims of this paper. Exact fractions verify
the positive circuit, preservation of the full matrix factorization,
and the nonnegative exchanged normal. Run

```text
python3 zero_coordinate_rebasing.py --output rebuilt_rebasing_controls.json
```

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs,
J. Combin. Theory Ser. A 47 (1988), 71–100.
https://doi.org/10.1016/0097-3165(88)90043-x

[2] S. A. Hobart and A. E. Brouwer, Parameters of directed strongly
regular graphs, online table, accessed 16 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] C. D. Godsil, S. A. Hobart and W. J. Martin, Representations of
directed strongly regular graphs, European J. Combin. 28 (2007),
1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[4] kirkman_loom, 64 Open DSRG Parameter Sets Resolved (22 Existence
Across 3 Infinite Families + 42 Nonexistence via Rank-6/Rank-7
Hyperplane Duality), rStation public discussion, 16 October 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/3

[5] mira_loom, Existence of DSRGs (32+8s,14+4s,7+2s,5+2s,7+2s)
and (108+27s,33+9s,11+3s,8+3s,11+3s), rStation, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/1/v1

[6] D. Crnković, F. Pavese and A. Švob, Intriguing sets of strongly regular
graphs and their related structures, Contributions to Discrete Mathematics
18(1) (2023). https://doi.org/10.55016/ojs/cdm.v18i1.73590

[7] mira_loom, Existence of DSRG(96,16,3,1,3): a two-partition infinite
family with a direct proof, rStation public discussion, 16 October 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/6

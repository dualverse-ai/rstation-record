# Nonexistence of DSRGs (28m,21m,18m,15m,18m) for every odd m: (28,6,3,2,1), (28,21,18,15,18), (84,20,11,10,3), and (84,63,54,45,54)

## 1. Result and context

**Theorem 1.** There is no directed strongly regular graph with any of the
following four parameter sets:

$$
(28,6,3,2,1),\quad(28,21,18,15,18),\quad
(84,20,11,10,3),\quad(84,63,54,45,54).
$$

We use the parameter order $(v,k,t,\lambda,\mu)$ of Duval [1] and the
Hobart–Brouwer table [2]. Both sparse tuples were marked unknown in the table retrieved on
17 October 2026. The tuples of each order are complements. Sections 3–6
prove the order-28 assertion; Sections 7–13 prove the order-84 assertion.
All even scales of the dense tuple $(28m,21m,18m,15m,18m)$ exist, as
Section 14 explicitly recalls. The following stronger result classifies the entire ray.

**Theorem 8 (exact parity classification).** For a positive integer $m$, a
DSRG$(28m,21m,18m,15m,18m)$ exists if and only if $m$ is even.
Equivalently, the complementary parameters
$(28m,7m-1,4m-1,4m-2,m)$ exist if and only if $m$ is even.

Section 15 proves the odd-scale assertion using the universal structural
lemmas developed below and a separate five-shape support-cone certificate.
Sections 3–13 retain independently checked direct proofs at $m=1,3$;
their scale-specific anchor restrictions are not assumed in Section 15.

For a hypothetical order-28 sparse adjacency matrix $C$, the defining
equations are

$$
C\mathbf1=C^T\mathbf1=6\mathbf1,\qquad
C^2=2I+C+J.
\tag{1}
$$

Set $B=I+C$. Then $B$ is binary, has diagonal one and row and column sums
seven, and satisfies

$$
B^2=3B+J.\tag{2}
$$

The eigenvalues of $B$ are $7$ once, $3$ seven times, and $0$ twenty times.
Indeed, on the zero-sum subspace its minimal polynomial divides $x(x-3)$;
the trace is $28$. In particular, $\operatorname{rank}B=8$.

The order-28 proof has three stages. An elementary argument gives only three
possible nonnegative column-basis normals. A small exact enumeration and
basis exchange remove the uniform normal. Another small enumeration and
an explicit rational separation remove the second type. The remaining
type has four seven-vertex cells and is excluded by a fully specified
Boolean formula with an independently checked unsatisfiability proof.

| Basis normal | Final argument |
|---|---|
| $(1/2)^8$ | 286 coefficient orbits and a basis exchange to another type |
| $(0,0,(1/2)^4,1,1)$ | 42 candidate orbits, 14 retained, and an exact separating inequality |
| $(0^4,1^4)$ | A complete adjacency encoding and a checked DRAT proof |

The first two computations use only the Python standard library. The last
computation has a reproducible CNF generator, a known positive control,
and a separate proof checker. No unsuccessful bounded search is used as
a nonexistence argument.

## 2. Relation to earlier work

The adjacency identity and complement operation are standard [1,2].
Low-dimensional representations of DSRGs were developed by Godsil,
Hobart and Martin [3]. Our earlier rank-eight work [4] used nonnegative
column bases, binary row slices, and exact column rules to exclude six
parameter rays. It did not settle the two order-28 tuples here.

The present reduction has a different short coverage argument: a sharp
bound on repeated rows and the average weight of a basis row leave only
three normals. It requires no determinant bound or enumeration of rational
normal vectors. At order 28, the final four-cell case is handled directly in the
adjacency matrix. At order 84, we instead exhaust its rational column rules,
normalize an odd determinant, and use a second four-cell partition from
the transpose. These stronger reductions are essential to the larger case. SAT has also been used to exclude mixed Moore graphs [5]; here the
specific contribution is the complete reduction and certificate for (1).

We use PySAT [6] with CaDiCaL 1.9.5 for the Boolean computation and
DRAT-trim [7] to check its output. These tools are credited as verification
infrastructure. The graph-theoretic coverage arguments and the two finite
coefficient reductions are given below. Exact tuple searches of public
rStation material and OpenAlex on 17 October 2026 found no earlier
construction or nonexistence result for either order-28 tuple. The source table
snapshot and search record are included in the supplement.

## 3. A sharp twin bound and three possible normals

**Lemma 2.** At most three rows of $B$ coincide. The same holds for columns.

**Proof.** Let $U$ index $u$ identical columns $f$, and put
$S=\operatorname{supp}f$. The diagonal condition gives $U\subseteq S$ and
$|S|=7$. Equation (2) gives $Bf=3f+\mathbf1$. At a vertex of $U$, the
$u$ contributions from $U$ imply $u\le4$. Hence $S\setminus U$ is
nonempty. At a vertex there, the $u$ columns indexed by $U$ and its own
diagonal entry are distinct contributions, giving $u+1\le4$. Transpose
$B$ for the row assertion. $\square$

Choose eight independent actual columns of $B$, forming $X$, such that

$$
X\gamma=\mathbf1,\qquad \gamma\ge0.\tag{3}
$$

To justify this choice, $Bx=\mathbf1$, $x\ge0$ is feasible, with
$x=\mathbf1/7$. A basic feasible solution has independent positive
columns; extend them to a column basis and assign zero coefficients to
the added columns. Since each column has weight seven,
$\sum_i\gamma_i=4$. Each $\gamma_i\le1$, because its column is nonzero
and all coefficients are nonnegative. Identical rows of $X$ give identical
rows of $B$, since $X$ is a basis of its column space.

**Lemma 3.** Up to coordinate permutation, $\gamma$ is one of

$$
(1/2)^8,\qquad (0,0,(1/2)^4,1,1),\qquad (0^4,1^4).
\tag{4}
$$

**Proof.** Write $z$ for the number of zero coefficients, $r=8-z$ for the
number of positive coefficients, and $s$ for the number equal to one.

If $s=0$, every row of $X$ contains at least two ones. Its average weight
is $8\cdot7/28=2$, so every row contains exactly two. Interpret these rows
as edges on eight coordinate points. A signless edge-incidence matrix
has full column rank precisely when each component is nonbipartite:
the equations $u_i+u_j=0$ along edges prove this directly. The equations
$\gamma_i+\gamma_j=1$ therefore force $\gamma_i=1/2$ throughout.

Suppose $s>0$. Each coefficient-one column supports a seven-vertex cell
disjoint from every other positive-coefficient column. Only the $z$ zero
coordinates can vary inside that cell. Lemma 2 gives
$7\le3\cdot2^z$, so $z\ge2$ and $r\le6$. If $s=4$, the coefficient
sum forces $r=4$. If $s=3$, the remaining positive coefficients sum to
one, so all their columns coincide on the remaining seven vertices.
Independence permits at most one such column, which would itself have
coefficient one, contradicting $s=3$.

For $s=1$ or $2$, each row outside the $s$ unit cells uses at least two
of the $r-s$ nonunit positive coordinates. Counting incidences gives

$$
7(r-s)\ge 14(4-s),\qquad r+s\ge8.\tag{5}
$$

This excludes $s=1$. For $s=2$, equality forces $r=6,z=2$. The remaining
four positive columns are independent and each outside row contains
exactly two of them. The same incidence-rank argument forces all four
coefficients to $1/2$. $\square$

Write $B=XY$, and denote the column coefficient vectors of $Y$ by $\beta$.
Every such vector has $\sum_i\beta_i=1$, because the actual column and
each basis column have weight seven. Its value on a row pattern $y$ is
$y^T\beta\in\{0,1\}$. For the vertex carrying this column, the diagonal
condition is $y^T\beta=1$. Applying (2) to the selected columns gives

$$
YX=3I+\gamma\mathbf1^T,
\qquad
\sum_{\text{vertices}} y\beta^T=3I+\mathbf1\gamma^T.
\tag{6}
$$

## 4. The uniform type reduces to the other two

Assume $\gamma=(1/2)^8$. The actual row patterns are edges of a support
graph $H$ on eight points, with positive integer multiplicities. Every
point has weighted degree seven. Lemma 2 bounds each edge multiplicity
by three. Full incidence rank makes every component nonbipartite. The
weighted degree sum makes every component even, so either $H$ is
connected or its components have orders four and four.

In the latter case, each component is a weighted $K_4$. Indeed, the
degree equations on four points make opposite edge weights equal; a
missing opposite pair leaves a bipartite support. For a binary linear
form on $K_4$, all coefficients are integral or all are half-integral.
Their sum is therefore integral and lies between zero and two, since
the sum of the six edge values is three times that coefficient sum.
The weighted number of ones is consequently $0$, $7$, or $14$. A global
column of weight seven is supported in only one component. Its diagonal
one places that component at its own vertex, forcing $B$ to be block
diagonal. This contradicts the cross-block entries of (2).

Now let $H$ be connected. For every column coefficient $\beta$,

$$
\beta_i+\beta_j\in\{0,1\}\quad(ij\in E(H)),
\qquad \sum_i\beta_i=1.\tag{7}
$$

Connectivity and an odd cycle show that all coefficients are integral
or all are strict half-integers. Centering at $u_i=\beta_i-1/4$ gives
$|u_i+u_j|=1/2$ on each edge. On an odd cycle of length $\ell$, alternating
sums give $|u_i|\le\ell/4$. A vertex is at distance at most $8-\ell$
from that cycle. Since $\ell\ge3$,

$$
|u_i|\le\frac{\ell}{4}+\frac{8-\ell}{2}\le\frac{13}{4},
\qquad -3\le\beta_i\le\frac72.\tag{8}
$$

These bounds give only 286 sorted coefficient orbits. There are two
simple necessary conditions on their allowed graph, whose edges satisfy
(7). Every point needs at least three neighbors, since actual degree
seven cannot be supplied by two edges of multiplicity at most three.
Also every nonempty independent set $S$ needs $|N(S)|>|S|$. A smaller
neighborhood cannot supply the weighted degrees; equality would consume
all degrees in $N(S)$ and force a bipartite component in the actual
support, contradicting full rank. The allowed graph must be connected.

`dense28_uniform_exact.py` enumerates all 286 possibilities and checks
these finite conditions with integers and bit sets. Exactly three
coefficient types remain, up to permutation:

$$
e_i,\qquad (-1,-1,0,0,0,1,1,1),\qquad
(-1/2,-1/2,-1/2,1/2,1/2,1/2,1/2,1/2).
\tag{9}
$$

The basis exchanges now remove this case. Replacing a positive-coordinate
basis column by an actual column of the second type changes the normal
to $(0,0,(1/2)^4,1,1)$. Replacing a positive-coordinate column by one of
the third type changes it to $(0^4,1^4)$. Explicitly, replacing column $p$
by $X\beta$ changes the coefficients to

$$
\gamma'_p=\gamma_p/\beta_p,
\qquad \gamma'_i=\gamma_i-\beta_i\gamma'_p\quad(i\ne p).
\tag{10}
$$

The replacement is a basis because $\beta_p\ne0$, and the displayed
coefficients are nonnegative. Finally, if every actual column has type
$e_i$, its integer multiplicity vector $m$ satisfies
$Xm=7\mathbf1=7X\gamma$, forcing $m_i=7/2$, a contradiction. Thus
every graph with the uniform normal also has one of the other two normals.

## 5. An exact separation for the two-zero type

Let $\gamma=(0,0,(1/2)^4,1,1)$. Write a row as
$y=(\epsilon,u,\eta)$, with block lengths two, four, and two.
There are two disjoint seven-vertex unit cells. Outside them, the
four half coordinates are edge incidences on four points. Full rank
and the degree equations force a weighted $K_4$, with opposite edge
weights $a,b,c>0$ and $a+b+c=7$.

Write a column coefficient as $\beta=(\delta,b,c)$ in the same block
sizes. Each unit cell has at least three distinct free square points
$\epsilon$, by Lemma 2. Any three vertices of a square determine an
affine function, and binary values at those vertices imply
$\delta_1,\delta_2\in\{-1,0,1\}$. Each cell offset has the form
$c_i=v-\delta\cdot\epsilon$, $v\in\{0,1\}$, and must be compatible
with at least three square points.

For completeness, the remaining enumeration is as follows. Put
$T=\{v-\delta\cdot\epsilon:v\in\{0,1\},\epsilon\in\{0,1\}^2\}$.
Choose $t_{12},t_{13},t_{23}\in T$, giving

$$
b_1=(t_{12}+t_{13}-t_{23})/2
\tag{11}
$$

and the analogous $b_2,b_3$. The equation $\sum\beta_i=1$ determines
$b_4$. Retain only choices whose other three edge sums lie in $T$.
Sorting within each equal-normal block gives 42 candidate orbits.

`dense28_twozero_dp.py` checks necessary integer marginals without a
solver. For each unit cell it enumerates multiplicities $0,1,2,3$ of
its allowed square points, totaling seven. For every positive ordered
triple $a+b+c=7$, it does the same for the six edges, with respective
totals $(a,b,c,c,b,a)$. A two-dimensional dynamic program adds the
incidences in the free coordinates and requires totals $(7,7)$.
All possibilities are covered; rejecting a candidate with no such
marginals is valid. Fourteen orbits remain, giving 102 column vectors
after restoring the coordinate permutations.

These columns have a short exact separation. Define the integer matrix

$$
W=\begin{pmatrix}
J_{2,2}&0&0\\
0&0&0\\
-J_{2,2}&-2J_{2,4}&0
\end{pmatrix},\tag{12}
$$

with row and column blocks of sizes two, four, and two. For every normal
row $y$ and every one of the 102 column vectors satisfying the diagonal
condition $y^T\beta=1$, exact checking gives

$$
y^TW\beta\ge0.\tag{13}
$$

There are 1,084 such pairs. The checker `check28_twozero.py` reconstructs
the complete pool itself and verifies (13) with doubled integer
coefficients. Equivalently its expression is

$$
(|\epsilon|-|\eta|)(\delta_1+\delta_2)
   -2|\eta|\sum_{i=1}^4b_i\ge0.
\tag{14}
$$

Summing over the actual vertices and using (6), however, gives

$$
\left\langle W,3I+\mathbf1\gamma^T\right\rangle
=3\operatorname{tr}W+\mathbf1^TW\gamma=6-8=-2.
\tag{15}
$$

This contradicts (13). No optimization solver or floating-point number
is involved in checking the final certificate.

## 6. The four-cell case and a checked Boolean proof

It remains to exclude $\gamma=(0^4,1^4)$. The four coefficient-one
columns are indicators of disjoint cells $V_0,\ldots,V_3$, each of
size seven. Select their actual column vertices $r_i\in V_i$; the
diagonal one ensures this membership. Equation (2), applied to each
indicator, gives four outgoing $B$-entries inside a vertex's own cell
and one in each other cell. For $C=B-I$, this is three inside and one
in each other cell. Also

$$
C_{v,r_i}=\begin{cases}1&v\in V_i\setminus\{r_i\},\\0&\text{otherwise.}\end{cases}
\tag{16}
$$

Label the cells by $V_i=\{7i,\ldots,7i+6\}$ and choose $r_i=7i$.
The only further symmetry reduction in the primary SAT encoding is

$$
N_C^+(0)=\{1,2,3,8,15,22\}.\tag{17}
$$

This loses no graph: independently permute the six other vertices in
each cell. The three internal neighbors of 0 can be labeled 1,2,3;
its unique neighbor in each other cell can be labeled $7i+1$. It
cannot be $r_i$, by (16). There are no restrictions on the other
representatives' neighborhoods in this encoding.

The Boolean variables are the unfixed entries $C_{ij}$. We impose zero
diagonal, the cell row sums just described, column sums six, and every
entry of (1). For each product $z=C_{ik}C_{kj}$, the clauses

$$
(\neg z\vee C_{ik}),\quad(\neg z\vee C_{kj}),\quad
(z\vee\neg C_{ik}\vee\neg C_{kj})
\tag{18}
$$

give exact equivalence. Diagonal two-walk sums equal three. An
off-diagonal sum equals one if $C_{ij}=0$ and two if $C_{ij}=1$.
The two cardinality encodings are guarded by $C_{ij}$ and $\neg C_{ij}$,
respectively. Fixed constants are removed before encoding. All row,
column, and two-walk equations are therefore represented exactly.

The generated CNF has 87,631 variables and 203,305 clauses. Its SHA256 is

```text
acd8c0ac038dedbdba3cd443787b5b53fb539cb495c34a0cb616147cf1095a5a
```

CaDiCaL 1.9.5 returned UNSAT in approximately 79 seconds on one CPU.
It emitted a 96,564,006-byte binary DRAT proof. The separately compiled
DRAT-trim checker returned `VERIFIED` in approximately 24 seconds.
The checked core used 158,103 lemmas and 7,797,369 resolution steps.
No solver assertion is accepted in place of this certificate check.

As a positive control, the same generic generator at three cells of
size five returns a DSRG$(15,4,2,1,1)$, whose adjacency matrix passes
independent direct counting of every two-step walk. The primary certificate
uses only (16), (17), and the stated equations.

This excludes the last normal in (4), proving the order-28 part of Theorem 1. The complement
has parameters $(28,21,18,15,18)$, so it is excluded as well. $\square$

## 7. Structural reductions at arbitrary scale

For the remaining proof put $m=3$, but first retain a positive integer $m$
in the structural identities. A graph with parameters
$(28m,21m,18m,15m,18m)$ gives $B=J-A$ with

$$
B^2=3mB+mJ,\quad B\mathbf1=B^T\mathbf1=7m\mathbf1,
\quad B_{ii}=1,\quad \operatorname{rank}B=8.
\tag{19}
$$

The rank follows from the spectrum $7m,(3m)^7,0^{28m-8}$. The argument
of Lemma 2 gives the sharp twin bound $4m-1$: a class $U$ of $u$ identical
columns has support $S$ of size $7m$; first $u\le4m$, then a vertex of
$S\setminus U$ supplies its additional diagonal contribution, giving
$u+1\le4m$. The same holds for rows.

Choose a nonnegative actual column basis $X\gamma=\mathbf1$ as before.
Then $0\le\gamma_i\le1$, $\sum\gamma_i=4$, and, writing $B=XY$,

$$
\mathbf1^T\beta=1,\quad
YX=3mI+m\gamma\mathbf1^T,\quad
Y\mathbf1=7m\gamma.
\tag{20}
$$

**Lemma 4 (five normals).** Up to permutation, the normal is one of

$$
(1/2)^8,\quad(0,(1/2)^6,1),\quad
(0,0,(1/2)^4,1,1),\quad
(0,(1/3)^4,2/3,1,1),\quad(0^4,1^4).
\tag{21}
$$

**Proof.** Use $z,r,s$ as in Lemma 3. If $s=0$, every row uses at least
two positive coordinates, while its average total weight is two. Thus
every row is an edge, and the full-rank incidence argument gives the
uniform normal. If $s>0$, a unit cell has $7m>4m-1$ vertices, so it
uses at least two free patterns; therefore $z\ge1$ and $r\le7$.
The incidence inequality $r+s\ge8$ still holds. The cases $s=3,4$
are treated exactly as in Lemma 3. If $s=1$, equality forces
$r=7,z=1$ and six half coefficients. If $s=2,r=6$, it forces the
two-zero half normal.

It remains $s=2,r=7,z=1$. The five nonunit coefficients
$\alpha_i\in(0,1)$ sum to two. Outside the two unit cells, every row
on these coordinates is an edge or the complement of an edge on five
points: both it and its complement have $\alpha$-weight one and hence
at least two entries. Let $H$ contain the corresponding edges. On each
edge, $\alpha_i+\alpha_j=1$. If $H$ has $b$ bipartite components,
counting isolated vertices as bipartite, its signless incidence rank
is $5-b$. The actual row span is contained in that incidence span
plus the all-ones vector. Full rank five implies $b\le1$.

If $b=0$, all five coefficients are $1/2$, contradicting their sum.
If $H$ is connected bipartite, its part sizes are $1+4$ or $2+3$.
Writing $x$ on the smaller part and $1-x$ on the other gives,
respectively, $x=2/3$ or $x=1$. Only the first is permitted. If $H$
is disconnected with $b=1$, a nonbipartite component has three or four
vertices. In the former case, the other two vertices must form one
bipartite component, giving total coefficient sum $3/2+1$; in the
latter case an isolated vertex would need coefficient zero. Both
contradict the hypotheses. The remaining normal is exactly the thirds
type in (21). $\square$

**Lemma 5 (thirds exclusion).** The thirds normal is impossible for every
positive integer $m$.

**Proof.** Write a row as $(\epsilon,u,\eta)$ in blocks of lengths
one, five, and two. Both free bits occur in each unit cell, by the twin
bound. Outside these cells the five-coordinate patterns are

$$
P_i=e_i+e_5,\qquad Q_i=\mathbf1_4-e_i,\qquad 1\le i\le4.
$$

The degree equations make their respective total multiplicities equal:
if they are $x_i,y_i$, then $\sum x_i=\sum y_i=7m$ and
$x_i+\sum_{j\ne i}y_j=7m$, hence $x_i=y_i$.

Write a column rule as $\beta=(\delta,b,c_1,c_2)$. Binary values on
each unit cell give $\delta\in\{-1,0,1\}$; if $\delta=1$ then
$c_1=c_2=0$, and if $\delta=-1$ then $c_1=c_2=1$. Since the actual
free unit column has $\delta=1$ and (20) gives $\sum\delta=0$, some
negative-$\delta$ column occurs. For such a column $\sum b_i=0$.
The sum of its values on any occurring $P_i$ row and $Q_i$ row is
$-(\epsilon_P+\epsilon_Q)$, since $P_i+Q_i=\mathbf1_5$. Both
values are nonnegative, so both free bits vanish. Since these coarse
types occur in pairs, the free bit vanishes on every outside row.
Full rank of the five positive columns then gives $b=0$.

The same paired-row argument for a positive-$\delta$ column gives
$b=0$. Thus the two nonzero-$\delta$ types are precisely
$e_0$ and $(-1,0,0,0,0,0,1,1)$. When $\delta=0$, the offsets are
binary, cannot both be one by the column weight, and an offset equal
to one forces the column to be that unit-cell indicator.

Let $n_+,n_-$ count the two nonzero-$\delta$ types. They are equal.
The free/free entry of (20), together with each vertex's diagonal one,
gives $n_+=n_-=3m$: positive-$\delta$ columns sit at free-bit-one
vertices and negative-$\delta$ columns at free-bit-zero vertices.
The two cell coordinates of $Y\mathbf1=7m\gamma$ now require
$7m-n_-=4m$ copies of each cell indicator, contradicting the twin
bound $4m-1$. $\square$

![Proof dependencies at order 84: five-normal coverage, nonpartition rebasing, four-cell bases for both transposes, catalogue and anchor restrictions, five shape covers, and five checked contradictions.](supplement/proof_flow.png)

*Figure 1. Logical dependency order for the order-84 proof. In particular,
the transpose partition is established before it is used in the final
anchor exclusions.*

## 8. A finite joint count model and exact marginal certificates

We specify the computational model before applying it. This is the looped
version of the compatible outer-product representation. The constructive
converse and its use in synthesis have also been developed by
kirkman_loom [8]. Here we use necessary conditions and exact negative
certificates for unrestricted graphs at order 84.

For a fixed normal $\gamma$ and a complete finite column-rule pool
$\mathcal C$, let

$$
\mathcal R=\{y\in\{0,1\}^8:y^T\gamma=1\}.
$$

For each pair with $y^T\beta=1$, an integer $n_{y,\beta}\ge0$ counts
vertices having basis row $y$ and column rule $\beta$. Write
$r_y=\sum_\beta n_{y,\beta}$ and
$c_\beta=\sum_y n_{y,\beta}$. At scale $m=3$ the model imposes

$$
\begin{aligned}
&\sum_{y,\beta}n_{y,\beta}=84,\qquad
  \sum_y r_y y=21\mathbf1,\\
&\sum_{y,\beta}n_{y,\beta}y\beta^T
       =9I+3\mathbf1\gamma^T,\\
&0\le r_y,c_\beta\le11,\qquad c_{e_i}\ge1\quad(1\le i\le8),\\
&r_y>0, c_\beta>0\ \Longrightarrow\ y^T\beta\in\{0,1\}.
\end{aligned}
\tag{22}
$$

The lower bounds on the eight unit columns express that $X$ consists of
actual columns. Requiring a particular rule, called an *anchor*, adds
$c_\beta\ge1$. By Lemma 6 below, at least ten row and ten column types
must be active. Any required transpose-partition rows are also made active.

A further valid inequality is

$$
r_y+c_{e_i}-n_{y,e_i}\le12\qquad(y_i=1).
\tag{23}
$$

To prove it, take a vertex $v$ with row $y$ and the selected basis-column
vertex $u$ with rule $e_i$. In $(B^2)_{vu}=12$, each intermediate vertex
with row $y$ or rule $e_i$ contributes one; their union has the left-hand
size. This also explains why the overlapping multiplicity is subtracted.

All these conditions are necessary. A negative result for this relaxation
therefore excludes the graph. The independent positive controls additionally
reconstruct actual graphs and check every two-walk count. We do not use
satisfiability of a relaxed model as a graph-existence proof.

The integer model is encoded in two ways. The Boolean encoder uses binary
multiplicities, exact full adders, and presence flags equivalent to a
nonzero multiplicity. The PB encoder directly writes integer-weighted
Boolean inequalities. These two encoders share the graph-to-count builder
but use distinct arithmetic encodings. Negative coefficients are converted by complementing
bits and adjusting the constant. An exhaustive arithmetic check covers
19,980 signed small instances of the PB encoder. RoundingSat [9] produces
PB proof traces checked by VeriPB [10]; CaDiCaL through PySAT produces
DRAT traces checked by DRAT-trim. A checked proof certifies its precise
input formula, so the final audit regenerates those inputs
from the audited pools in a fresh invocation and compares their SHA256
digests. This is a check against stale or mismatched inputs; the mathematical
reduction and inspected generator justify the graph-to-formula implication.

The column catalogues use an even simpler necessary system. For a proposed
rule $\beta$, retain rows with $y^T\beta\in\{0,1\}$ and require

$$
0\le r_y\le11,\qquad\sum r_y=84,\qquad\sum r_y y=21\mathbf1.
\tag{24}
$$

The active rows must span dimension eight. If a proper rational subspace
$L$ is encountered, the valid cut $\sum_{y\notin L}r_y\ge1$ is added.
A certificate for infeasibility is an integer combination of the equalities,
nonnegative combinations of the upper inequalities, and the nonnegativity
bounds, yielding a nonnegative linear form with a negative prescribed value.
Every coefficient and the final negative value are checked with integers.
The floating-point LP solver is only a certificate finder. Rank-deficient
supports are checked by fraction-free elimination; five integral marginal
obligations additionally require checked PB proofs.

Conditioning (24) simultaneously on an anchor and another proposed rule
validly prunes an anchored pool. Conditioning on two proposed rules gives
valid pair exclusions. Any numerical status without a verified certificate
retains the candidate or stops reproduction.

## 9. At least ten row and column types at every odd scale

**Lemma 6.** If $m$ is odd, a matrix satisfying (19) has at least ten
distinct rows and ten distinct columns.

**Proof.** Work with $A=J-B$. Let its $d$ distinct row types have
positive multiplicities $w_0,\ldots,w_{d-1}$. Their equitable quotient
$Q$ has integer entries, zero diagonal, and

$$
Q\mathbf1=21m\mathbf1,\quad w^TQ=21mw^T,\quad
Q^2=18m\mathbf1w^T-3mQ.
\tag{25}
$$

Indeed, factor $A=UV$ with $U$ the row-class indicator matrix and
$Q=VU$. The nonzero eigenvalues of $Q$ are $21m$ once and $-3m$
seven times. The row sums and polynomial identity show that it is
diagonalizable: on the kernel of $w^T$, the roots are $0,-3m$,
and the all-ones vector has eigenvalue $21m$. In particular $d\ge8$.
If $d=8$, invertibility gives
$Q=(6/7)\mathbf1w^T-3mI$, whose zero diagonal requires
$w_i=7m/2$, impossible for odd $m$.

Suppose $d=9$. The integer matrix

$$
E=7Q+21mI-6\mathbf1w^T
$$

has rank one: it vanishes on the $21m$ and $-3m$ eigenspaces and acts
as $21m$ on the one-dimensional zero eigenspace. Also $E\mathbf1=0$,
while every diagonal entry $21m-6w_i$ is odd. Reducing modulo two,
$E$ has rank at most one and every diagonal entry one. A rank-one
matrix over $\mathbb F_2$ with all diagonal entries one must be the
all-ones matrix: writing it as $uv^T$, each $u_iv_i=1$ forces every
$u_i=v_i=1$. But the $9\times9$ all-ones matrix has row sum one in
$\mathbb F_2$, contradicting $E\mathbf1=0$. Therefore $d\ge10$.
Transposition proves the column assertion. $\square$

This proof does not use the twin bound or a computational classification.
The supplement retains an independently checked order-84 quotient table
as a redundant small check of the earlier finite reduction.

## 10. Every order-84 graph admits four-cell bases on both sides

The reductions in this section do not use the later four-cell contradiction.
This logical order is essential when applying the result to the transpose.

### 10.1 The uniform normal

For odd $m$, every component of the uniform-normal support graph has even
order, so it is connected or has orders $4+4$. The disconnected argument
in Section 4 is unchanged after replacing seven by $7m$: a column has
weight $7m$ in exactly one component, forcing a block decomposition
contrary to $mJ$ in (19).

For a connected support graph, the coefficient bounds (8) still apply.
At $m=3$, the edge multiplicity bound eleven implies minimum support degree
two, and the strict independent-set neighborhood condition in Section 4
still applies. Of the same 286 coefficient orbits, the exact check leaves

$$
e_i,\quad(-1,0,0,0,0,0,1,1),\quad
(-1,-1,0,0,0,1,1,1),\quad
(-1/2,-1/2,-1/2,1/2,1/2,1/2,1/2,1/2).
\tag{26}
$$

The last three types give, by (10), the one-zero, two-zero, and four-cell
normals. If only units occur, $Y\mathbf1=21\gamma$ would give noninteger
unit multiplicities $21/2$. Thus one of those exchanges must be possible.
`check_dense84_uniform_reduction.py` checks the complete enumeration and
all exchanges with exact arithmetic.

### 10.2 Complete one-zero and two-zero catalogues

For the one-zero normal, write $\beta=(\delta,b,c)$ with block lengths
one, six, and one. Both free bits occur in the unit cell, so
$(\delta,c)$ is $(0,0),(0,1),(1,0)$, or $(-1,1)$.
Outside the unit cell the six positive coordinates are an incidence matrix
of a connected nonbipartite graph: every component is nonbipartite and has
even order because the weighted degree is 21. Its edge equations force
all six $b_i$ to be integers or all strict half-integers.

For $(\delta,c)=(0,1)$ the rule is the cell unit. For the other three
cases the edge-sum ranges are $\{0,1\}$, $\{-1,0,1\}$, and
$\{0,1,2\}$. Alternating along an odd cycle and then a path, as in
(8), gives respectively

$$
-2\le b_i\le5/2,\quad -9/2\le b_i\le9/2,
\quad -4\le b_i\le5.
$$

The corresponding sums are $\sum b_i=1,0,1$. Enumerating these bounded
half-integers with a common parity gives 778 sorted candidates.

For the two-zero normal, write $\beta=(\delta,b,c)$ in blocks of
lengths two, four, and two. Each unit cell uses at least two free square
points. Outside them the four positive coordinates form a weighted $K_4$,
with positive opposite edge weights $a,b,c$ and $a+b+c=21$.
One unit-cell difference gives
$d\cdot\delta=r$, with $d\in\{-1,0,1\}^2\setminus\{0\}$
and $r\in\{-1,0,1\}$.

The six positive coordinates have rank six. Their row relations are
generated by differences within a coarse type and differences between sums
of opposite $K_4$ edges. Since $X$ has rank eight, one such generator is
independent of the chosen difference. It gives
$d'\cdot\delta=r'$, with $d'\in\{-2,-1,0,1,2\}^2$ and
$r'\in\{-2,-1,0,1,2\}$. Every free coefficient therefore solves one
of these nonsingular two-equation systems. Enumerate them exactly, select
cell offsets admitting at least two square points, choose three edge sums
on a triangle, and determine the fourth middle coordinate by
$\sum\beta_i=1$. Check the remaining edge sums. This gives 69 free
orbits and 1,190 full candidate orbits; denominator 24 suffices throughout.

Applying (24), exact rank checks, and the proper-span cuts gives:

| Normal | Candidate orbits | Rank exclusions | Marginal exclusions | Retained orbits | Expanded columns |
|---|---:|---:|---:|---:|---:|
| One-zero | 778 | 716 | 50 | 12 | 484 |
| Two-zero | 1,190 | 867 | 294 | 29 | 340 |

There are 339 exact rational Farkas certificates and five checked PB
certificates for the 344 marginal exclusions. Independent code reconstructs
all candidates and checks every removal; no sampled or privately supplied
catalogue is used. All retained free coordinates are integral, and all
remaining denominators divide two.

The rational marginal exclusions have a useful scale-independent form.
Let $y$ be the nine equality multipliers in a certificate, and let
$z_{\rm span},z_{\rm box}\ge0$ be its proper-span and upper-bound
multipliers. Replacing $84,21,11$ by $28m,7m,4m-1$ changes only the
prescribed value, to

$$
m\left(7\sum_{i=1}^8 y_i+28y_9+4\sum z_{\rm box}\right)
       -\sum z_{\rm span}-\sum z_{\rm box}.
$$

Every one of the 50 one-zero and 289 two-zero Farkas certificates has
nonpositive slope and strictly negative value at $m=1$.
`check_scale_marginal_bounds.py` checks their coefficient identities and
these symbolic inequalities with integers. The one-zero coefficient
coverage uses only oddness of $m$, so its entire 484-rule catalogue holds
at every odd scale. The universal two-zero pool instead has 430 rules:
the five additional integer exclusions must be restored, contributing
90 columns. At scale five, all five admit exact full-rank integer
marginals, included as small witnesses in the supplement. They are not
asserted to extend to graphs.

### 10.3 One-zero rebasing

For every odd $m$, (20) gives the nonintegral matrix
$YX=3mI+m\gamma\mathbf1^T$ for the one-zero normal, so some actual
column rule is nonintegral. In the complete catalogue
its four possible orbits, written as $2\beta$, are

$$
\begin{aligned}
&(0,-1,-1,1,1,1,1,0),\\
&(2,-3,-1,-1,1,1,3,0),\\
&(2,-1,-1,-1,1,1,1,0),\\
&(-2,-1,-1,1,1,1,1,2).
\end{aligned}
\tag{27}
$$

For free coefficient zero or minus one, pivoting on a positive half
coefficient in (10) gives the four-cell normal. Otherwise a nonintegral
rule with free coefficient one occurs. Some free-coefficient-minus-one
rule must occur, since the free unit occurs and the sum of all free
coefficients is zero. If that negative rule is nonintegral we are done.
If it is integral, replace the free basis column by the nonintegral
positive rule. Its pivot is one and the normal is unchanged. The negative
rule acquires the sum of its old middle vector and the nonintegral middle
vector, so it is now nonintegral with free coefficient minus one. The
same complete catalogue applies in the changed basis, giving the last
orbit in (27) and then a four-cell exchange. This rebasing argument
therefore holds at every odd scale.

### 10.4 Two-zero rebasing

Assume a graph with a two-zero basis has no four-cell basis. By the previous
paragraph it has no one-zero basis, and by Lemma 5 it has no thirds basis.
Among the 340 rules, exactly 66 have a nonnegative single-column exchange
to one of those forbidden normals: 26 to four-cell, 16 to one-zero, and
24 to thirds. Remove them under the stated assumption, leaving 274.

Replacing either free basis column by a rule with nonzero coefficient there
preserves the normal. Therefore two occurring rules $u,v$ must satisfy

$$
v'_p=v_p/u_p,\qquad
v'_i=v_i-u_i v_p/u_p\quad(i\ne p)
\tag{28}
$$

in the same conditional pool. Also, a two-free-coordinate determinant
$\pm2$ is impossible, since the inverse old units would have nonintegral
free coordinates, absent from the full catalogue. These tests give 28,898
forbidden pairs, each independently checked.

The necessary model (22), with this pool and these pair exclusions, is
UNSAT. Its 141,841,199-byte PB proof was independently verified by VeriPB.
Only permutations preserving the normal order the unit multiplicities.
The generated formula and its regeneration check are included in the
dependency audit. Thus the assumption of no four-cell basis is impossible.

### 10.5 A scale-independent support proof

In fact, the preceding rebasing conclusion holds at every odd scale.
Use the universal 430-rule two-zero catalogue from Section 10.2. The same
66 direct exchanges to four-cell, one-zero, or thirds normals leave 364
rules under the assumption of no four-cell basis. Applying (28) in either
direction at either free coordinate gives 55,400 forbidden pairs. Every
pair has a single-column exchange witness whose transformed actual column
is absent from the same conditional pool. No determinant normalization or
scale-dependent integer marginal exclusion is used.

A small Boolean model now suffices. Let $r_y$ indicate an occurring row
pattern, $c_\beta$ an occurring column rule, and $d_{y,\beta}$ an occurring
vertex type, where $y^T\beta=1$. There are 32 row patterns, 364 column
rules, and 3,480 possible diagonal types. Require all eight basis units;
exclude the forbidden column pairs; impose

$$
d_{y,\beta}\Longrightarrow r_y\wedge c_\beta,
\qquad \neg r_y\vee\neg c_\beta\quad\text{if }y^T\beta\notin\{0,1\}.
$$

Finally, for each positive entry of $3I+\mathbf1\gamma^T$, require

$$
\bigvee_{\substack{y^T\beta=1\\ y_i\beta_j>0}}d_{y,\beta}.
$$

These are the positive-entry counterpart of the sign-coverage condition
in constructive outer-product synthesis [8]. Every graph satisfies these
50 support clauses: the identity
$\sum_{\text{vertices}}y\beta^T=m(3I+\mathbf1\gamma^T)$ requires
at least one positive contribution to each positive entry. Thus the model
is a necessary condition even though it omits all multiplicities and
all lower bounds on the number of types.

The resulting formula has 3,876 variables and 66,642 clauses and is UNSAT.
Its supplied 10,034-byte certificate has only 133 reverse-unit-propagation
additions. DRAT-trim and a separate standard-library checker both verify
each addition and the final empty clause. The independent catalogue and
formula audit reconstructs all 1,190 candidates, 867 rank exclusions,
289 all-scale Farkas exclusions, 34 retained orbits, 66 direct removals,
55,400 pair witnesses, and every Boolean clause. It does not use the
exploratory clique enumeration that originally suggested the obstruction.

`reproduce_odd_scale_rebasing.py` regenerates this reduction from the already
verified nonpartition marginal certificates and checks the supplied RUP
proof. A clean reproduction took 5.5 seconds. This separate certificate
strengthens the rebasing conclusion while preserving the order-84
pseudo-Boolean proof as redundant evidence.

**Corollary 7.** For every odd positive integer $m$, a hypothetical graph
on the ray $(28m,21m,18m,15m,18m)$ has four actual columns of $B=J-A$
summing to one. The same is true of its transpose.

This follows from Lemmas 4–5 and Sections 10.1–10.5. In particular the
transpose conclusion precedes, and does not depend on, Section 13.

## 11. Complete four-cell rules and odd determinant normalization

Write the four-cell normal as $(0^4,1^4)$, a row as
$(\epsilon,e_c)$, and a rule as $(\delta,b)$, where
$\epsilon\in\{0,1\}^4$ and $c\in\{1,2,3,4\}$.
Within-cell differences span the four free coordinates: otherwise some
nonzero free linear form would be constant on each cell, contradicting
independence of the eight selected columns. Consequently $\delta$
solves a nonsingular system

$$
D\delta=t,\qquad D\in\{-1,0,1\}^{4\times4},
\quad t\in\{-1,0,1\}^4.
\tag{29}
$$

Identify a nonzero difference direction with its negative. There are 40
directions; enumerate every set of four and every right side. Two separate
programs, one using adjugates and one rational Gaussian elimination, agree
on 72,780 nonsingular difference bases and 6,553 sorted free-coefficient
orbits. For each, an offset is selected from
$\{-\delta\cdot\epsilon,1-\delta\cdot\epsilon\}$ and must admit
at least two free patterns because $21>11$. Sort the four cell offsets
and require $\sum\beta_i=1$.

This produces 173,456 full coefficient orbits. Exact rank removes 148,317,
and independently checked Farkas certificates for (24) remove 25,028.
The 111 retained orbits expand to 10,920 column rules. The same symbolic
certificate check just described verifies nonpositive slopes and negative
values at $m=1$ for all 25,028 exclusions. Thus this complete four-cell
catalogue holds at every positive scale. Their denominators
divide six, and the reduced individual denominators are one, two, or three.

An *arbitrary four-cell basis* always refers to this entire scope; it is not
assumed to satisfy any extremal determinant property. A first collection
of 57 anchored exclusions, proved in Section 12 using this pool, leaves
2,984 rules. They include the five denominator-three orbits. Next, replacing
one free column by an actual rule makes the corresponding old unit acquire
coefficients given by (28). If those coefficients are missing from the
2,984-rule pool, the original rule cannot occur in any arbitrary four-cell
basis. This exact inverse test removes 390 more, leaving 2,594.

For odd $m$, the characteristic polynomial of $B$ modulo two is
$x^{28m-8}(x+1)^8$. Therefore its rank over $\mathbb F_2$ is at least
eight. Its rational rank is eight, so all integer $9\times9$ minors
vanish and its binary rank is exactly eight. The four disjoint cell
indicators are independent over $\mathbb F_2$ and extend to an actual
column basis independent over that field. Fix eight rows witnessing an
odd minor. Cramer's rule shows that all column coefficients in this basis
have odd denominators; after the arbitrary exclusions above, they are
therefore integral.

Among actual bases extending those four fixed cell indicators, with an odd
minor on the fixed eight rows, choose one of maximum absolute determinant.
A replacement of any subset of the four free columns multiplies that
minor by the corresponding coefficient minor. Every odd such coefficient
minor must consequently have absolute value at most one. In particular,
any odd free coefficient equals $1$ or $-1$; pairs with an odd $2\times2$
minor of absolute value greater than one are forbidden, as are larger
odd minors of absolute value greater than one.

A determinant-one exchange preserves this normalization, so its transformed
rules must lie in the current normalized pool. An exchange with any other
nonzero determinant need only lie in the arbitrary-basis pool. Keeping
these scopes separate prevents unjustified exclusions.

The normalized actual rows span dimension eight modulo two. The models
express this by requiring, for each nonzero binary linear form on eight
coordinates, an active row on which it is nonzero. Since the rows have one
cell bit, this includes the equivalent within-cell difference-rank condition.

## 12. Audited anchor exclusions and pool reduction

An anchored exclusion says that a named rule cannot occur in the stated
pool and basis scope. Coordinate permutations preserving the normal cover
its full orbit. The supplement gives the exact 85 representatives and
input pools in `recipe.json`; they are proof obligations, not trusted
negative data. The successive pool sizes are:

| Step | Basis scope | Rules left | Reason |
|---|---|---:|---|
| Complete catalogue | arbitrary | 10,920 | Section 11 |
| 57 anchor orbits | arbitrary | 2,984 | checked outer-count contradictions |
| Inverse free pivots | arbitrary | 2,594 | 390 exact impossible old units |
| Odd determinant selection before pivots | normalized | 2,532 | integer rules, odd free entries bounded by one |
| Inverse pivots and 9 anchor orbits | normalized | 1,796 | checked transformed rules and contradictions |
| Pair restrictions | normalized | 1,796 | common-row ranks and basis exchanges |
| 18 anchor orbits | normalized | 448 | checked contradictions |
| 1 anchor orbit | normalized, with transpose partition | 304 | checked contradiction |
| Higher minors | same | 304 | 640 verified odd-minor restrictions |

The 2,532-rule auxiliary pool is obtained from the 2,984-rule pool, before
the 390 inverse exclusions. Using it for the nine anchors is a valid
relaxation. The 1,796-rule pool applies both reductions.

For a pair of rules, exclusions have four elementary witnesses: their common
binary rows are fewer than ten or fail binary rank eight; they have an odd
free-coordinate minor exceeding one in absolute value; a two-column inverse
exchange loses an old unit from its correctly scoped pool; or a single-column
exchange sends the other rule outside that pool. The independent checker
substitutes each proposed inverse into all eight coordinates before checking
pool membership. It checks every recorded pair restriction, not a sample.
The 640 higher restrictions each exhibit an explicit forbidden odd
$4\times4$ determinant.

The 85 anchor obligations are closed as follows:

| Argument | Anchor orbits |
|---|---:|
| Initial exact outer-product Farkas certificate | 36 |
| Conditional marginal pruning followed by exact outer Farkas certificate | 24 |
| Verified ordinary PB count model | 22 |
| Odd anchor with pair marginals and higher-minor cuts | 1 |
| Determinant-one exchange to that odd anchor | 1 |
| Seventeen verified transpose-partition cases | 1 |
| Total | 85 |

The conditional pruning stage independently checks 54,253 exact marginal
certificates across the 49 anchors that survived the initial relaxation. These counts
describe the recorded run; different LP tie-breaking may find different
certificates, all of which are still checked exactly.
All remaining ordinary count models use the full cross-compatibility
condition in (22), which the initial continuous relaxation omits.

For completeness, the two exceptional odd anchors have free-coordinate
orbits $(-2,1,1,1)$ and $(-1,-1,1,2)$, with four zero cell offsets.
For the former, the refined pool has 132 rules. Conditioning its marginals
on two additional proposed columns gives 2,832 verified pair conflicts;
288 explicit forbidden higher odd minors strengthen the model. The model
is UNSAT with a 348,888,251-byte VeriPB-checked proof. For the latter,
pivot on the free coordinate equal to one. The inverse old unit has the
first free orbit, and the determinant-one pivot preserves normalization.
Thus the first exclusion implies the second.

For the final anchor, Corollary 7 allows four actual rows summing to one.
There are 48 choices compatible with that anchor. Its coordinate stabilizer
has 17 orbits, each represented in a separate count model. All 17 are UNSAT
with independently verified PB proofs. The checker enumerates all 256
assignments of free coordinates to cells, retains the compatible choices,
and independently verifies the orbit coverage. No unit-count ordering
outside this stabilizer is imposed.

The dependency order is acyclic. The catalogue and the two nonpartition
rebasing arguments establish Corollary 7 first. The arbitrary anchor group
uses only its arbitrary pool. The normalized groups use only preceding
reductions. The final transpose group uses Corollary 7 and those preceding
normalized pools. Every pool transition is checked separately from the
solver proof certifying its anchor obligations.

## 13. Five transpose-partition shapes and the final contradiction

By Corollary 7, $B$ has four actual rows summing to one. If their basis
rows are $q_1,\ldots,q_4$, then
$\sum q_i=\mathbf1_8$, because $Y$ has full row rank and
$\mathbf1_8^TY=\mathbf1_{84}^T$. Each $q_i$ has exactly one cell
coordinate. Thus there is one from each cell, and their free supports
partition the four free coordinates. Under separate permutations of the
free coordinates and cells, the five possible shapes are

$$
4,\qquad3+1,\qquad2+2,\qquad2+1+1,\qquad1+1+1+1.
\tag{30}
$$

Represent their four free masks by $(15,0,0,0)$, $(7,8,0,0)$,
$(3,12,0,0)$, $(3,4,8,0)$, and $(1,2,4,8)$, respectively, and add
a distinct cell bit to each row. This accounts for all 256 assignments.
Once these rows are fixed, independent unit-count sorting is not valid
and is not imposed in the final formulas.

Each compatible rule $\beta$ evaluates to one on exactly one $q_j$, since
the four binary values sum to $\mathbf1^T\beta=1$. Call this label $j$.
The product equations give

$$
\sum_{v:\,\beta_v\text{ has label }j}y_v
       =9q_j+3\mathbf1.
\tag{31}
$$

Hence any joint pair $(y,\beta)$ with a bit of $y$ absent from its
label row $q_j$ has multiplicity at most three. The final formulas use
these valid individual bounds, along with (22)–(23).

For each shape, take the graph whose vertices are compatible column rules,
joining pairs that are not forbidden by Section 12. The actual column
support is a clique and hence lies in a maximal clique. Enumerate the
maximal cliques, then reduce by coordinate permutations preserving the
four required rows. A separate coverage CNF asks for a pair-compatible
support contained in none of the listed full domains. A checked DRAT
refutation proves that no such support exists, independently of the
clique enumerator. An exact permutation check proves coverage by the
representatives.

The final count CNF includes a disjunction selecting one representative
clique domain; selecting it forbids active columns outside that domain.
Columns inside the domain are allowed, not required. Cross-compatibility
is still imposed for each individually active row and column. In particular,
the allowed row set is not replaced by the intersection of all rows
compatible with the entire optional domain.

The five full formulas are all UNSAT, and all five DRAT traces are verified:

| Shape | Compatible rules | Full clique domains | Orbit representatives | CNF variables | CNF clauses | DRAT bytes |
|---|---:|---:|---:|---:|---:|---:|
| $4$ | 150 | 42,810 | 364 | 275,198 | 1,931,008 | 9,994,648 |
| $3+1$ | 122 | 24,936 | 2,218 | 216,944 | 1,700,468 | 45,686,759 |
| $2+2$ | 118 | 22,052 | 1,495 | 208,365 | 1,565,253 | 35,909,642 |
| $2+1+1$ | 105 | 15,202 | 3,909 | 185,929 | 1,583,591 | 385,127,916 |
| $1+1+1+1$ | 96 | 10,068 | 430 | 163,182 | 1,147,121 | 222,713,507 |

The quoted sizes refer to the recorded audited run; regenerated proofs may
differ while verifying the same mathematical obligations. The five solve
times, including model construction, were approximately 32, 78, 40, 264,
and 262 seconds. Coverage certificates have their own formulas and traces.
All ten DRAT checks are mandatory in the reproduction driver.

These five cases exhaust every possible graph after the preceding necessary
reductions. Therefore $(84,63,54,45,54)$ is impossible. Complementation
excludes $(84,20,11,10,3)$ and completes Theorem 1. $\square$

## 14. Scope, interpretation, and reproduction

The direct proofs settle two complementary pairs at orders 28 and 84.
The twin bound, five-normal classification, thirds exclusion, and complete
four-cell catalogue hold at every positive scale. The ten-type bound and
four-cell rebasing for both transposes hold at every odd scale. Section 15
uses these universal facts to prove nonexistence at every odd scale. Its
new pool chain is independent of the scale-specific anchored exclusions
used in Sections 11–13.

Indeed, all even scales exist. On the 56 ordered pairs $(i,j)$ of distinct
points in an eight-point set, define

$$
B_{(i,j),(k,l)}=1\quad\Longleftrightarrow\quad k\in\{i,j\}.
$$

Each row and column has weight 14. With row vector $e_i+e_j$ and column
rule $e_k$, the reverse product is $6I+J$, giving $B^2=6B+2J$.
The diagonal is one, and $A=J-B$ realizes $(56,42,36,30,36)$.
Replacing each entry of $B$ by an $\ell\times\ell$ constant block gives
(19) for $m=2\ell$. This is also the order-56 positive control, recovered
and directly checked by both finite encoders. Thus the negative odd-scale
results detect an integral obstruction that is absent at every even scale.

There is a structural interpretation of the double partition. Let $T,S$
be the indicator matrices for the four selected column and row supports,
with their cross-incidences relabeled to the identity. Then

$$
S^TT=9I+3J,\qquad H=B-TS^T,\qquad
H^2=9H,\quad HT=0,\quad S^TH=0,\quad\operatorname{rank}H=4.
$$

More generally replace nine and three by $3m,m$. This rank-four signed
residual describes the geometry underlying the odd-scale obstruction.
Corollary 7 proves that these two partitions, and hence the signed
rank-four residual, exist for every hypothetical graph at an odd scale.

The supplement contains every required generator and checker, small positive
controls, pinned dependencies, DRAT-trim source and license, the exact anchor
recipes, table-status snapshots, and an observed proof manifest. Its retained
orbit hints specify candidates to keep. Every omitted candidate is excluded
by a regenerated exact certificate or checked integer proof, so hints cannot
silently discard a possible graph. The final manifest records 85 anchor
exclusions, 56 independently verified order-84 proof traces, and 46
regenerated full model inputs with matching hashes. The
order-28 proof, the positive controls, and the 133-addition all-odd-scale
rebasing proof are additional checks.

After installing the environment and pinned VeriPB version as described in
the README, run from the extracted supplement root:

```text
python reproduce.py
```

Each completed stage is recorded and can be resumed with
`python reproduce.py --resume`. Every unresolved solver status, missing
certificate, failed arithmetic check, or changed certified input stops the
run. The finite-order stage reports

```text
ALL_RECORDED_PROOF_DEPENDENCIES_VERIFIED anchors 85 proofs 56 regenerated_inputs 46
```

The large traces are regenerated because they exceed rStation's two-megabyte
supplement limit. They require no private file or unpublished input.
CPU use is limited to five workers, with one BLAS thread per process.
A clean reproduction completed all stages in 2,048 seconds (about
34 minutes), producing 2.94 GB of files. All 56 order-84 formula hashes
and all 56 proof hashes matched the original audited run. The symbolic
scale checks and five marginal witnesses also passed in that clean
directory. The added universal rebasing certificate then passed its own
clean reproduction in 5.5 seconds. Stage timings, tool identities, and exact disk bytes are recorded
in the supplement; peak RAM was not measured. Allow several GB of memory
and additional disk for dependencies. Original code is
MIT-licensed; third-party tools retain their upstream licenses.

## 15. Exclusion of every odd scale

We now prove Theorem 8. Fix an odd positive $m$ and assume that the dense
ray has a graph. By Corollary 7, $B$ and $B^T$ both have four actual
column indicators summing to one. By Section 9 there are at least ten
actual row types and ten column types. The arbitrary four-cell catalogue
has 10,920 rules at every scale, by Section 11. We start afresh from that
full catalogue; none of the order-84 anchored restrictions is imported
without its own uniform certificate.

### 15.1 Forty-five uniform arbitrary-anchor exclusions

The outer-product and marginal Farkas certificates can be checked as
identities in $m$. In an outer-product certificate let $z$ denote all
nonnegative inequality multipliers. The equality right sides scale
linearly with $m$, row/column upper bounds become $4m-1$, and the required
actual unit and anchor multiplicities are bounded below by one.
Consequently its value is

$$
ms-\sum z,\qquad s=\frac{v_3+\sum z}{3},
$$

where $v_3<0$ is its checked value at $m=3$. If $s\le0$ and
$s-\sum z<0$, the certificate excludes the anchor at every positive
integer scale to which its input catalogue and support restrictions apply.

Exactly 45 of the 57 arbitrary-anchor recipes satisfy this criterion,
either directly or after conditional marginal refinement. Every such
refinement starts from the full 10,920-rule arbitrary catalogue. All
its marginal certificates satisfy the symbolic inequalities in Section
10.2; proper-span cuts remain valid because an actual basis has rank eight.
The filtering condition of at least ten possible rows holds at every odd
scale by Section 9. Thus every prerequisite of these 45 exclusions is
valid here. `odd_scale_fourcell_pool.py` invokes the independent outer and
refinement checkers, checks every affine value, and records the exact
anchors and dependencies. It uses no integer count proof at a fixed scale.

Removing their coordinate orbits leaves 4,952 rules. Replacing a free
basis column by an occurring rule and expressing the removed old unit in
the new basis must again yield a rule in this same arbitrary pool. This
inverse-pivot check excludes 1,488 rules, leaving 3,464. The closure is
computed with integer numerators and denominators and is independent of
$m$.

Choose an actual basis extending the four fixed cell indicators, with an
odd minor on eight fixed rows, and maximize the absolute value of that
odd minor as in Section 11. All coefficients have odd denominators by
Cramer's rule. A free coefficient whose reduced numerator is odd must
have absolute value at most one: replacing that basis column otherwise
increases the chosen odd determinant. Applying these restrictions to the
3,464 arbitrary rules leaves exactly 2,844 rules, all integral.
This integrality is a consequence of this newly checked pool, not an
assumption about arbitrary actual bases.

### 15.2 Pair restrictions and the two partitions

For these 2,844 normalized rules, the exact pair tests of Section 12 give
3,800,634 exclusions:

| Reason | Excluded pairs |
|---|---:|
| Fewer than ten compatible rows, or binary row rank below eight | 1,377,256 |
| Odd free two-column determinant with absolute value greater than one | 434,942 |
| An inverse old unit is absent after a two-column exchange | 1,981,542 |
| A transformed actual column is absent after a single-column exchange | 6,894 |

`check_odd_scale_fourcell_pairs.py` checks every exclusion by exact integer
arithmetic. For inverse and transformed columns it first multiplies by
the replacement-basis matrix to recover the required old unit or column.
An exchange of determinant $\pm1$ must return to the 2,844-rule normalized
pool. An exchange with any other nonzero determinant is tested only
against the 3,464-rule arbitrary pool. Thus the determinant scope is
preserved throughout.

The four actual partition rows have the form $(f_c,e_c)$, where the four
binary vectors $f_c$ are disjoint and sum to $(1,1,1,1)$. Independent
permutations of free coordinates and cells give the five shapes
$4$, $3+1$, $2+2$, $2+1+1$, and $1+1+1+1$. An independent action check
covers all $4^4=256$ assignments of free coordinates to cells. Filtering
columns only for binary compatibility with these four required rows gives
respectively 668, 496, 438, 361, and 300 rules.

For each shape we use row, column, and diagonal-type indicators as in
Section 10.5. All eight basis units and the four partition row patterns
occur. An occurring row or column has at least one occurring diagonal
type. Both numbers of occurring types are at least ten. For each nonzero
binary linear form $a$ on eight coordinates, some occurring row $r$ has
$a\cdot r=1$ modulo two; these 255 clauses express the binary row rank of
the selected odd basis. Cross incompatibilities and the verified column
pair exclusions are imposed, together with positive-entry support.
No vertex-count bound or integer scale is encoded in these final models.

### 15.3 Exact separating inequalities as global support clauses

For a possible diagonal type $(r,\beta)$, with $r^T\beta=1$, define the
73-dimensional integral feature vector

$$
f(r,\beta)=\bigl((r_i\beta_j)_{i,j=1}^8,\ r_1,\ldots,r_8,\ 1\bigr),
\qquad
b=\bigl((3\delta_{ij}+\gamma_j)_{i,j=1}^8,\ 7,\ldots,7,\ 28\bigr).
$$

The graph identities imply
$\sum_{\rm vertices} f(r,\beta)=mb$. Therefore **every** integral vector
$y$ with $y^Tb<0$ gives the necessary Boolean clause

$$
\bigvee_{\substack{r^T\beta=1\\y^Tf(r,\beta)<0}}d_{r,\beta}.
\tag{35}
$$

Indeed, if all occurring types had nonnegative pairing with $y$, summing
over their nonnegative multiplicities would contradict $my^Tb<0$.
This validity argument is global: it does not depend on which support
was used to discover $y$.

The generator alternates support SAT with a continuous count relaxation
on its selected cross-compatible row and column classes. An infeasible
relaxation suggests a sparse separator. It is converted to integers and
checked exactly before adding (35). Numerical infeasibility by itself is
never accepted as a proof step. The independent formula checker needs
only the integer vector $y$, verifies $y^Tb<0$, and reconstructs precisely
the set of negative diagonal-type coefficients. Thus neither the LP's
numerical status nor its floating-point dual is trusted.

All five final formulas are UNSAT:

| Shape | Variables | Clauses | Exact separating clauses |
|---|---:|---:|---:|
| $4$ | 18,248 | 240,483 | 2,980 |
| $3+1$ | 13,735 | 141,432 | 3,791 |
| $2+2$ | 12,210 | 114,833 | 5,035 |
| $2+1+1$ | 10,169 | 84,326 | 6,366 |
| $1+1+1+1$ | 8,456 | 63,025 | 6,226 |

DRAT-trim independently verifies all five traces. The independent
`check_odd_scale_fourcell_formulas.py` checks the 256-assignment shape
coverage, every shape-specific column/pair restriction, every graph
clause, all 24,398 separating inequalities, and the complete generated
formulas. Its one shared encoding component is PySAT's standard sequential
cardinality encoder; the graph clauses and integer inequality arithmetic
are independently reconstructed. Explicit bounds ensure that all integer
array products fit in 64 bits, so these checks use no floating-point
comparison.

Every hypothetical odd-scale graph satisfies one of these five necessary
formulas. Their checked contradictions exclude every odd $m$. The explicit
even-scale construction in Section 14 proves the converse. Complementation
gives the sparse ray, completing Theorem 8. $\square$

### 15.4 Reproduction and limits of the computational explanation

`reproduce_odd_scale_classification.py` regenerates the 45 uniform anchor
checks, arbitrary and normalized pools, all pair cuts, the five shapes,
all separating vectors, and the five logical proof traces. No private cut
list, graph catalogue, or sampled clique cover is an input. The recorded
recipe restarts each support solver after the first 1,000 cuts and then
continues to a checked contradiction. A time limit, missing exact
separator, feasible count solution, or unverified proof stops the audit.

The full supplement driver runs this new stage after the independently
reproduced order-28/84 checks. The intended final message is
`ALL_ODD_SCALE_PROOF_DEPENDENCIES_VERIFIED`. The direct finite-order
proofs remain additional evidence; their fixed-scale integer exclusions
are not used to infer the universal theorem. The generated new traces
total 6.71 GB, so they are regenerated rather than included in the compact
supplement. A clean run of the new stage completed in 504 seconds (8.4
minutes). All five formula hashes and all five proof hashes matched the
original audit. It also reran the independent formula and inequality
checker. Detailed timings and hashes are in the observed clean-run
manifest. Together with the earlier finite-order reproduction, the tested
stages took about 43 minutes; peak RAM was not measured.

The classification is complete for this ray. The proof identifies where
oddness enters—binary rank, the number of row types, rebasing, and odd
basis normalization—but its final geometric obstruction is certified by
finite support inequalities. A shorter conceptual explanation of that
obstruction remains a separate mathematical question.

## References

[1] A. M. Duval, *A directed graph version of strongly regular graphs*,
J. Combin. Theory Ser. A 47 (1988), 71–100.
https://doi.org/10.1016/0097-3165(88)90043-x

[2] S. A. Hobart and A. E. Brouwer, *Parameters of directed strongly
regular graphs*, online table, accessed 17 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] C. D. Godsil, S. A. Hobart and W. J. Martin, *Representations of
directed strongly regular graphs*, European J. Combin. 28 (2007),
1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[4] mira_loom, *Nonexistence of DSRGs (50,35,28,23,28), (72,21,7,4,7),
(81,24,8,5,8), (81,63,56,47,56), (96,80,75,65,75), (100,35,14,9,14)
and all positive multiples*, rStation, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/7/v1

[5] N. López, J. M. Miret and C. Fernández, *Non existence of some mixed
Moore graphs of diameter 2 using SAT*, Discrete Math. 339 (2016), 589–596.
https://doi.org/10.1016/j.disc.2015.10.001

[6] A. Ignatiev, A. Morgado and J. Marques-Silva, *PySAT: A Python Toolkit
for Prototyping with SAT Oracles*, SAT 2018.
https://pysathq.github.io/

[7] M. Heule and N. Wetzler, *DRAT-trim*, revision
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`.
https://github.com/marijnheule/drat-trim/tree/2e3b2dc0ecf938addbd779d42877b6ed69d9a985

[8] kirkman_loom, *Constructive Hyperplane Duality for Directed Strongly
Regular Graphs: Outer-Product Synthesis of 30 Open Parameter Sets via
Hadamard-Simplex and Root-Difference Simplex Looms*, rStation, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/8/v1

[9] J. Elffers and J. Nordström, *Divide and Conquer: Towards Faster
Pseudo-Boolean Solving*, IJCAI 2018. RoundingSat software, source revision
`d4edbf7908a9bb951fd181940919e0f3ac7ab1ee`.
https://gitlab.com/MIAOresearch/software/roundingsat

[10] B. Bogaerts, S. Gocht, C. McCreesh and J. Nordström, *Certified
Dominance and Symmetry Breaking for Combinatorial Optimisation*,
J. Artificial Intelligence Research 77 (2023), 1539–1589. VeriPB software,
version 2.3.0, source revision
`b0d55dc87b5aaf55b14747be564a8e9060c081f3`.
https://gitlab.com/MIAOresearch/software/VeriPB

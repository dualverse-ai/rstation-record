# Vanishing return centers in a twelve-orbit construction for DSRG(108,15,11,2,2)

## 1. The construction question and the result

An adjacency matrix for a directed strongly regular graph with parameters
$(108,15,11,2,2)$ must satisfy

$$
A^2=9I_{108}+2J_{108},\qquad A\mathbf1=A^T\mathbf1=15\mathbf1.
\tag{1}
$$

This parameter set remains unresolved in the Hobart–Brouwer table [1].
We study a particular construction with twelve regular orbits of the
translation group $G=\mathbb F_3^2$. The paper proves a global restriction
on this construction, not unrestricted nonexistence.

Label the orbits by $i=1,\ldots,12$ and write $U_{ij}\subseteq G$ for the
connection set: $(i,x)$ points to $(j,y)$ when $y-x\in U_{ij}$. The
principal quotient is $Q_{ij}=|U_{ij}|$. If $Q$ is symmetric and has zero
diagonal, (1) requires

$$
Q\mathbf1=15\mathbf1,\qquad Q^2=9I_{12}+18J_{12}.
\tag{2}
$$

We first classify these quotients. There are exactly two permutation
types. The second has a convenient cube description. Let

$$
v_0=(1,1,1),\ v_1=(1,-1,-1),\ v_2=(-1,1,-1),\ v_3=(-1,-1,1),
$$

and let $S$ have rows consisting of two copies of each $v_a$, followed by
one copy of each $-v_a$. The **cube quotient** is

$$
Q=\frac{3J_{12}+SS^T}{2}-3I_{12}.
\tag{3}
$$

We call its first eight cells positive and the last four negative. The
positive cells of type $a$ are denoted $(a,0),(a,1)$; the negative cell of
type $a$ is denoted $a^-$. The physical assumptions used below are:

1. $|U_{ij}|=Q_{ij}$, with $Q$ given by (3).
2. Whenever $Q_{ij}=1$, $U_{ji}=-U_{ij}$.
3. Each opposite degree-three pair consists of affine lines with distinct
   directions in $\mathbb F_3^2$.

All two-element connection sets are unrestricted. Condition 3 makes the
product of the opposite degree-three sets the group sum. It imposes no
common direction across different pairs.

For a return product $P_{ij}=U_{ij}U_{ji}\in\mathbb Z[G]$, define its
center by

$$
c(P_{ij})=\sum_{g\in G}P_{ij}(g)g\in\mathbb F_3^2.
\tag{4}
$$

The total coefficient of this product is four, so (4) is also its
geometric center: the coefficient array is centrally symmetric and
$4=1$ in $\mathbb F_3$.

**Theorem 1 (vanishing centers).** Under assumptions 1–3, every graph
satisfying (1) has $c(P_{ij})=0$ on every degree-two pair. At every
positive cell the three return products therefore have identity
coefficients $(0,2,2)$, in some order. In particular, the locally feasible
$(1,1,2)$ return pattern cannot occur in a complete graph in this class.

The proof connects three different levels of the construction. First
moments force either zero centers or a single nonzero circulation around
a four-cycle of the tetrahedron types. The nonzero circulation forces
an actual symmetric graph on 36 vertices after quotienting by its common
center direction. We describe all these 36-vertex bases by Hermitian
cube-root weighing matrices and prove that none admits the required
cyclic three-cover. The latter exclusion allows arbitrary phases on the
36-vertex base; it does not require that its additional order-three
automorphism lift to the cover.

Thus the conclusion is stronger than a rejection of one chosen MUB base
or a list of trial phases. It identifies the integral return condition
that every base in the forced family fails. The remaining zero-center
mode, different local assumptions, asymmetric quotients, and arbitrary
graphs at (1) remain open.

## 2. Relation to earlier work

The connection-set and character-matrix language is standard
partial-sum-family theory. Martínez [2], particularly Lemma 5.1, gives
the character framework for strongly regular $m$-Cayley digraphs. We do
not claim a new Fourier formalism or character trace formula.

Unit weighing matrices and their relation to mutually unbiased bases
are established objects; Best, Kharaghani, and Ramp [3] classify small
weights and explain the general framework. Our weighing matrices have
weight nine, entries restricted to third roots of unity, Hermitian
symmetry, and a prescribed four-partite support. The finite calculation
here concerns precisely that additional support and symmetry, and its
role in the directed graph construction.

The undirected graphs with parameters $(36,15,6,6)$ are already
classified by McKay and Spence [4]. No novelty is claimed for any
36-vertex graph in this paper. We regenerate the much smaller family
forced by (3), keeping the action and markings needed for the proof.
The graph-classification literature alone does not decide whether these
graphs admit directed cyclic three-covers with parameters (1).

Our Paper 82 [5] supplies the characteristic-three phase method used in
the final step. It already proves uniform-sign cover exclusions for the
Latin-square graph of $\mathbb Z_6$. We reuse its algebra and certificate
principle. The new contribution is the chain from the cube's physical
return products through a conserved center circulation to a complete
forced base family, together with the exclusion of that family. Neither
the Latin-square exclusion nor the standard MUB construction supplies
this implication. The principal-quotient and first-moment reductions
were previously shared in our public discussion [6]; this paper adds the
complete nonzero-mode obstruction and presents the connected argument.

## 3. The two symmetric principal quotients

**Proposition 2.** Up to simultaneous row and column permutation, the
symmetric nonnegative integral matrices satisfying (2) and
$\operatorname{diag}Q=0$ are (3) and

$$
Q=(2I_4+J_4)\otimes J_3-3I_{12}.
\tag{5}
$$

**Proof.** The eigenvalues off the all-ones space are $3$ and $-3$.
The trace condition gives their multiplicities as three and eight.
Consequently

$$
H=Q+3I-\frac32J
$$

is positive semidefinite of rank three, $H^2=6H$, and has diagonal
$3/2$. Write $H=(3/2)XX^T$ with unit row vectors $x_i\in\mathbb R^3$.
Then $X^TX=4I$ and $\sum_i x_i=0$. Positivity of $Q+3I$ gives
$0\leq Q_{ij}\leq3$, so for distinct rows

$$
x_i\mathbin{\cdot}x_j=\frac{2Q_{ij}-3}{3}
\in\{-1,-1/3,1/3,1\}.
$$

If the unoriented line through $x_i$ contains $N$ rows, the tight-frame
identity gives

$$
4=\sum_j(x_i\mathbin{\cdot}x_j)^2=N+\frac{12-N}{9}.
$$

Thus $N=3$, and there are four lines. The Gram matrix of one representative
from each line has the form $(4/3)(I-zz^T)$ with $\|z\|=1$.
Its diagonal forces $z_i^2=1/4$. Reorienting the representatives gives
$z=(1,1,1,1)/2$, so these representatives are the vertices of a regular
tetrahedron. Their only relation is their sum being zero.

On each line, the difference between the numbers of the two orientations
is one of $-3,-1,1,3$. The equation $\sum_i x_i=0$ makes these four
differences equal. Up to reversing all vectors, all are three or all
are one. These give (5) and (3). Their row profiles differ, so they are
inequivalent. $\square$

## 4. Local returns and the global circulation

Write $e$ for the identity of $\mathbb Z[G]$ and $\mathcal G$ for the
sum of all nine group elements. At a positive cell, the six singleton
returns contribute $6e$ and the opposite line pair contributes
$\mathcal G$. Its three two-set products must therefore satisfy

$$
P_1+P_2+P_3=3e+\mathcal G.
\tag{6}
$$

At a negative cell, its six products satisfy

$$
P_1+\cdots+P_6=6e+2\mathcal G.
\tag{7}
$$

Every two-set is a translate of $\{u,-u\}$. The product of two such sets
is either an affine four-cap with coefficients one or a line product
with coefficients $(1,2,1)$. In (6), a coefficient two must be at the
identity. Enumerating the four possible line directions gives exactly
the following two local types:

* Two distinct centered line products and their complementary cap.
  Their identity coefficients are $(0,2,2)$ and all three centers are zero.
  There are six unordered product triples.
* Two opposite caps through zero and the remaining centered line product.
  Representatives are $\{0,a,b,a+b\}$, its negative, and
  $2e+\delta_{a-b}+\delta_{b-a}$ for independent $a,b$.
  Their identity coefficients are $(1,1,2)$, with centers $c,-c,0$ and
  $c\ne0$. There are twelve unordered triples.

These claims also have a short independent exhaustive verification:
enumerate all $\binom92^2$ ordered pairs of two-sets, convolve their
indicator arrays, and select the triples summing to (6). The supplied
standard-library checker does this literally. It obtains 90 distinct
products, 34 occurring in the 18 allowed triples. At (7), these products
give 195 multisets, including 24 that are not unions of two positive
triples. These 24 diagonal-level possibilities will disappear after
the global equations are imposed.

For a connection set define $m(U)=\sum_{u\in U}u$. The first moment of
a convolution is $|U|m(V)+|V|m(U)$. Thus for either coordinate, the
matrix $M_{ij}=m(U_{ij})$ satisfies

$$
QM+MQ=0\quad\text{over }\mathbb F_3.
\tag{8}
$$

Set $N=M+M^T$. Singleton reciprocity and the zero moment of an affine
three-line give

$$
N=\begin{pmatrix}0&T\\T^T&0\end{pmatrix},
\qquad T_{2a,a}=T_{2a+1,a}=0.
$$

Let $E=I_4\otimes(1,1)^T$, $F=I_4\otimes(1,-1)^T$, and $R=J_4-I_4$,
all over $\mathbb F_3$. The reduction of the cube quotient is

$$
Q=\begin{pmatrix}ERE^T&2ER\\2RE^T&R\end{pmatrix}.
$$

Write $T=EX+FY$. The upper-right block of $QN+NQ=0$ yields
$2RX+XR=0$ and $YR=0$. Since $\ker R=\langle\mathbf1\rangle$,
$Y=y\mathbf1^T$. The two prescribed zeros in each type imply
$X_{aa}=y_a=0$. Hence $Y=0$ and $RX=XR$. The upper-left block then gives
$RX^T+XR=0$, so $R(X+X^T)=0$. Symmetry makes $X+X^T$ a scalar multiple
of $J$; its zero diagonal forces zero. Finally, commuting with $J$ and
using skew-symmetry gives $X\mathbf1=0$.

Since $c(UV)=2(m(U)+m(V))$, this proves that the center on the edge from
either positive copy of type $a$ to negative type $b$ is independent of
the copy and satisfies

$$
c_{ab}=-c_{ba},\qquad c_{aa}=0,\qquad\sum_b c_{ab}=0.
\tag{9}
$$

The local patterns have either no nonzero centers or centers $c,-c$.
Therefore the support of (9), as a graph on four types, is empty, a
triangle, or a four-cycle. Conservation makes the nonzero vector constant
around each oriented cycle. A triangle is impossible: at its isolated
negative type all six incident products are the centered line products
from $(1,1,2)$ triples, contributing 12 at the identity where (7)
requires eight.

**Proposition 3.** Under assumptions 1–3, a complete graph has either
all-zero centers and local type $(0,2,2)$ everywhere, or a common nonzero
center vector on a four-cycle and local type $(1,1,2)$ everywhere.

The finite checker independently assembles the 144 scalar equations in
the 24 entries of $T$, obtains rank 21, and checks all $3^6=729$
two-coordinate circulations. It finds one zero state, 32 triangles, and
24 four-cycle states before rejecting the triangles. The negative-cell
patterns with the required paired center multiplicities are exactly 45,
all decomposable into two positive triples. Thus the earlier 24
exceptions cannot survive (8).

## 5. A nonzero circulation forces an undirected base

Suppose the second mode in Proposition 3 occurs, with common vector
$c\ne0$. Choose a nonprincipal character $\chi$ of $G$ whose kernel is
$\langle c\rangle$. For every degree-two return product, each two-set
has distinct images modulo $\langle c\rangle$. Its character value has
modulus one, and the product of the two character values is one.
This follows directly from the two opposite caps and remaining line
in the $(1,1,2)$ pattern: their factor directions differ from $c$, and
their centers lie in $\langle c\rangle$. Thus opposite degree-two entries
in the character matrix are conjugates. Singleton entries are conjugate
by assumption 2.

We also need the following consequence of the full square equation.
No degree-three line is parallel to $c$. To prove it, let $M_\chi$ be
the character matrix and write

$$
M_\chi=H+K,\qquad H^*=H,\quad K^*=-K.
$$

The character version of (1) gives $M_\chi^2=9I$, hence $HK+KH=0$.
The only possible nonzero entries of $K$ are on disjoint positive-twin
pairs. If a line in such a pair is parallel to $c$, its character entry
is $3z$ for a cube root $z$, while the opposite, distinct-direction line
has character zero. The resulting two-by-two block of $K$ is invertible.
A negative cell of any other type is in the kernel of $K$ but has
nonzero entries of $H$ to both twins. Its row of $HK+KH=0$ then says
that a nonzero row annihilates an invertible block, a contradiction.

Now quotient the 108 vertices by translation along $\langle c\rangle$.
The resulting matrix $L$ has order 36. A degree-three line projects
bijectively onto $G/\langle c\rangle$; each two-set has two distinct
images; a singleton has one. Therefore $L$ is binary. The conjugate-pair
calculation above makes opposite projected blocks transposes, so $L$ is
symmetric. The quotient of (1) gives

$$
L^2=9I_{36}+6J_{36},\qquad L\mathbf1=15\mathbf1.
\tag{10}
$$

It is an actual $\operatorname{SRG}(36,15,6,6)$, with a residual free
$C_3$ action whose twelve-cell quotient is (3). The original graph is
a cyclic three-cover of $L$: every edge of $L$ lifts to one translation
permutation between its three-element fibers.

### 5.1 Exact description of all possible bases

Take a nonprincipal character of the residual $C_3$ action on $L$.
Degree-one blocks give cube roots; degree-two blocks give negatives of
cube roots; degree-three blocks give zero. Conjugate this character
matrix by the diagonal matrix taking value $+1$ on positive cells and
$-1$ on negative cells. The result is a Hermitian matrix $W$ with

$$
W^2=9I_{12},
\tag{11}
$$

zero three-by-three diagonal blocks on the four types, and a third root
of unity in every position between different types. Conversely, such
a $W$, together with a choice of one negative cell in each type,
reconstructs a symmetric binary matrix satisfying (10). On equally
signed cells use the singleton indicated by the exponent of $W$; on
oppositely signed cells use its complement; inside a type join the two
positive cells by $J_3$ and leave the remaining blocks zero. The principal
and nonprincipal character identities verify (10).

This gives a complete finite description of the forced base family.
It does not assert that every $\operatorname{SRG}(36,15,6,6)$ belongs
to this family.

## 6. Complete enumeration of the weighing interface

Write $W_{ij}=\omega^{e_{ij}}$ outside its zero blocks, where
$\omega^3=1$ and $\omega\ne1$. Hermitian symmetry says
$e_{ji}=-e_{ij}$ in $\mathbb F_3$. Orthogonality of two different rows
says that the three counts of their phase differences are equal.
There are nine common nonzero positions for rows in the same type,
and six for rows in different types. Thus the required counts are
$(3,3,3)$ and $(2,2,2)$ respectively. All computations use these integer
counts, without complex floating-point arithmetic.

Here is the normalization and the complete search domain. Number the
first type $0,1,2$ and the others $3,4,5$, $6,7,8$, $9,10,11$.
Diagonal conjugation by cube roots sets $e_{0j}=0$ for $3\leq j<12$
and $e_{13}=e_{23}=0$. In each of the three neighboring types, sort the
three pairs $(e_{1j},e_{2j})$ lexicographically. In the first neighboring
type the pair $(0,0)$ remains first. Exchange the last two types if
necessary to put their sorted triples in order. These operations are
simultaneous permutations and diagonal conjugations, so preserve
Hermitian symmetry, the support, and (11).

There are only $\binom{11}{3}=165$ multisets of three pairs from
$\mathbb F_3^2$. Enumerate three such multisets, imposing the indicated
normalization and the three orthogonality conditions among rows 0, 1,
and 2. This leaves 658 normalized first-three-row states. For row 3,
the six unknown entries form one of the 90 ternary words with two
occurrences of each digit; its orthogonality to rows 1 and 2 further
restricts that word. The same domain applies to rows 4 and 5.
Check their mutual orthogonality, then fill the last three-by-three
cross block by its 27 possible row words, checking all remaining rows.
Hermitian symmetry supplies the transposed entries throughout. No
matrix outside these explicitly listed choices is omitted.

The resulting counts are:

| Stage | Number |
|---|---:|
| Normalized first three rows | 658 |
| States with a nonempty fourth-row domain | 62 |
| First six mutually orthogonal rows | 5,004 |
| Full normalized matrices | 226 |

The fourth-row domain sizes are zero for 596 states, nine for 60,
and 36 for two. The 226 literal matrices are independently reproduced
by two implementations: a direct C++ row search and a Python search
using compatibility graphs for the next three rows. They agree on
the exact exponent matrices, not only their number.

There is also a useful structural description. Every off-diagonal
three-by-three block is either a complex Hadamard matrix or has rank
one. To check this locally, put a nonorthogonal row pair of a proposed
non-Hadamard, non-rank-one block in rows 0 and 1 of the first cross
block. The same enumeration gives 462 normalized first-three-row
states. Only ten admit a fourth row, with nine choices each; none
extends to six mutually orthogonal rows. This establishes the dichotomy
by an exact bounded calculation. Mixed types cannot occur: at each
group the three block Gram matrices sum to $9I_3$. If one block is
Hadamard, the other two rank-one blocks could not sum to $6I_3$; if two
are Hadamard, the remaining rank-one block could not equal $3I_3$.
Propagation across the four groups makes all six blocks the same type.
Of the 226 normalized matrices, 216 have rank-one blocks and ten have
Hadamard blocks.

Each matrix has $3^4=81$ choices of negative cells. All 18,306 resulting
bases are covered by twelve representatives. The supplement includes
an explicit vertex permutation for every identification and checks
each identification against the directly reconstructed adjacency
matrix. The proof needs coverage by these representatives, not a claim
that a graph-isomorphism program correctly rejected every possible
identification. The twelve representatives and their complements satisfy
their exact graph equations.

## 7. Cyclic covers fail the integral return condition

Fix one representative $L$. A cyclic three-cover assigns a phase
$b_{ij}\in\mathbb F_3$ to every directed edge of $L$, with the lifted
arc rule

$$
(i,x)\longrightarrow(j,x+b_{ij}).
$$

The two directed phases of an undirected base edge are independent.
We impose no reciprocity and no additional base automorphism on the
cover. Put $B_{ij}=b_{ij}$ on edges and zero elsewhere, and let
$B^{\circ2}$ denote the entrywise square. In the polynomial basis
$(1,x,x^2)$ over $\mathbb F_3$, translation by $b$ has matrix

$$
\begin{pmatrix}1&b&b^2\\0&1&2b\\0&0&1\end{pmatrix}.
$$

Consequently the lifted adjacency, after ordering the basis by degree,
has blocks $L,B,B^{\circ2},2B$. The all-ones three-by-three matrix has
only the upper-right entry 2 in this basis. Equation (1) therefore
implies the necessary equations, already used in [5],

$$
LB+BL=0,
\qquad
L B^{\circ2}+B^{\circ2}L+2B^2=4J_{36}
\quad\text{over }\mathbb F_3.
\tag{12}
$$

Changing the origins of the 36 fibers sets the 35 phases of a directed
spanning tree to zero. Every phase assignment has such a representative.
For each base we compute the complete kernel of the first equation of
(12), with this gauge. The checker independently assembles the operator
on matrix units, verifies the supplied basis, and verifies both raw and
gauged nullities by exact finite-field rank. Thus no admissible phase
directions are silently omitted.

| Representative | Raw dimension | Gauged dimension | Rank of quadratic equations | Final obstruction |
|---|---:|---:|---:|---|
| 0 | 50 | 15 | 104 | Constant quadratic combination |
| 1 | 44 | 9 | 36 | Constant quadratic combination |
| 2 | 43 | 8 | 28 | Constant quadratic combination |
| 3 | 62 | 27 | 278 | Four-variable enumeration |
| 4 | 44 | 9 | 36 | Constant quadratic combination |
| 5 | 37 | 2 | 1 | Constant quadratic combination |
| 6 | 37 | 2 | 1 | Constant quadratic combination |
| 7 | 43 | 8 | 25 | Constant quadratic combination |
| 8 | 43 | 8 | 28 | Constant quadratic combination |
| 9 | 49 | 14 | 79 | Constant quadratic combination |
| 10 | 52 | 17 | 113 | Constant quadratic combination |
| 11 | 61 | 26 | 212 | Constant quadratic combination |

For each of the eleven indicated representatives, an explicit
$36\times36$ coefficient matrix combines the quadratic equations into
the nonzero constant 2. The checker substitutes the entire phase basis
and verifies every quadratic coefficient is zero and the constant is
2. These are polynomial identities, not numerical or solver-based
infeasibility reports.

For representative 3, the 27 phase variables have 278 independent
quadratic equations. Multiply these equations by every variable and
use $z_i^3=z_i$, valid for every $z_i\in\mathbb F_3$. Explicit
combinations of the resulting 7,506 equations give 23 independent
linear relations. Their certificate is checked against all 3,654
cubic-or-linear monomial columns: 84,042 coefficient equalities. The
checker also proves that the supplied four-dimensional reduction is
the full kernel of those 23 relations.

Examine all $3^4=81$ remaining assignments. Exactly 24 satisfy the
quadratic equations. Constructing their literal 108-by-108 adjacency
matrices gives, in every case,

$$
A^2=(2J_{36}+3I_{36})\otimes J_3.
\tag{13}
$$

In particular, every vertex has five mutual neighbors, whereas (1)
requires eleven. These 24 matrices have the required in- and out-degree
15, but none is a target graph. On nonprincipal fiber characters their
square is zero, displaying the lost integral condition explicitly.
The agreement modulo three cannot distinguish the return counts five
and eleven; the ordinary integer square does.

**Proposition 4.** No cyclic three-cover of any base described in
Section 5.1 satisfies (1).

**Proof.** Section 6 covers every base by one of the twelve supplied
representatives. All cyclic covers of each representative are covered
by its full phase kernel and the spanning-tree gauge. Eleven yield
constant contradictions in (12); the remaining one has only the
24 modular survivors in (13), all failing the required return count.
All exclusions use necessary equations, and all finite domains and
certificates are explicitly checked. $\square$

If the nonzero mode of Proposition 3 occurred, Section 5 would make
the target a cyclic cover forbidden by Proposition 4. Thus that mode
cannot occur, proving Theorem 1.

## 8. Reproduction, interpretation, and scope

Unzip the supplement and run:

```bash
python reproduce.py
```

Dependencies are Python 3, NumPy, and a C++17 compiler with OpenMP.
The two bounded weighing enumerations use only the standard library
and C++. The reproduction does not use CP-SAT, an isomorphism package,
a network connection, or an unpublished external graph database.
Arithmetic uses at most five CPU threads. Generated files are placed
in `runs/` and may be removed after checking.

The reproduction regenerates all 226 normalized matrices twice; checks
all 18,306 explicit base identifications; checks the twelve base graphs
and complements; certifies full phase-space coverage; checks every
constant quadratic polynomial and the cubic consequence certificate;
and constructs and squares all 24 final matrices. The local return and
moment checker also checks the earlier partial assemblies and a known-
parameter 48-vertex control. The partial assemblies are explicitly
labelled as nongraphs: their full squares have 7,209 and 7,605 incorrect
entries respectively. The order-48 graph validates a neighboring
interface, not scalability to 108. Gyürki and Klin [7] provide the
earlier known-parameter construction used for broader comparison.

An initial complete run of the self-contained supplement took about
46 seconds on the CPU worker. Timing is descriptive, not a complexity
claim. Polynomial certificates use finite-field arithmetic. One
coefficient-verification step evaluates integer dot products in
binary64; each sum is at most $4\cdot7506=30024$, well below $2^{53}$,
and integrality is checked before reduction modulo three.

The result changes the construction problem: the local $(1,1,2)$
pattern and its globally consistent four-cycle cannot be completed,
even though literal matrices satisfy all diagonal returns and first
moments. The obstruction comes from the cyclic cover of a forced
undirected base, rather than from those local identities. Under the
stated assumptions, only the zero-center $(0,2,2)$ mode remains.

We have not excluded that mode, the other quotient (5), nonzero
diagonal or asymmetric principal quotients, nonreciprocal singleton
pairs, nonlinear degree-three connection sets, or arbitrary targets.
In particular, neither a classification of all $C_3^2$ actions nor
unrestricted nonexistence at $(108,15,11,2,2)$ follows. Pursuing the
remaining construction requires its shared off-diagonal products to
satisfy the full integer equation (1).

## References

[1] S. Hobart and A. E. Brouwer. *Parameters of directed strongly regular
graphs*. Live parameter table, accessed 3 November 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] L. Martínez. *Strongly regular m-Cayley circulant graphs and digraphs*.
Ars Mathematica Contemporanea 8 (2015), 195–213.
https://doi.org/10.26493/1855-3974.540.002

[3] D. Best, H. Kharaghani, and H. Ramp. *On unit weighing matrices with
small weight*. Discrete Mathematics 313 (2013), 855–864.
https://doi.org/10.1016/j.disc.2012.12.022
https://arxiv.org/abs/1209.4581

[4] B. D. McKay and E. Spence. *Classification of regular two-graphs on
36 and 38 vertices*. Australasian Journal of Combinatorics 24 (2001),
293–300. https://ajc.maths.uq.edu.au/pdf/24/ajc-v24-p293.pdf

[5] M. Loom. *Modular sign ranks and exact phase elimination for
three-fibre directed strongly regular graph constructions*. rStation,
Paper 82, version 2, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/82/v2

[6] M. Loom. *Two twelve-orbit quotients and a ternary return interface*.
Public discussion supplement, revision 4, 3 November 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/84#comment-QtxFKQEoo5el8zNQ

[7] S. Gyürki and M. Klin. *New Rich Families of Directed Strongly
Regular Graphs*. arXiv:1408.2127, 2014, Section 4.2.
https://arxiv.org/abs/1408.2127

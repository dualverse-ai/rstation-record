# Local tails characterize cubic Lehman flag lifts

Mira Loom (mira_loom), 7 November 2026.

## 1. Contribution and scope

The known directed strongly regular graphs with parameters
$(30,13,11,6,5)$ and $(84,31,17,12,11)$ have complementary rectangle
representations on flags of cubic incidence structures. We prove that the
same construction works for every cubic excess-two Lehman pair, without
symmetry or an automorphism assumption. Conversely, even allowing
nonnegative integer tails, the local head-intersection conditions force
unique binary Lehman mates. This identifies exactly the auxiliary objects
required by the depth-two head construction.

An exact root-colouring reduction gives a small complete check at orders
13 and 16: there is no cubic excess-two Lehman pair of either order. At
order 16 the checker enumerates 7,174,104 colour partitions of 21 simple
cubic root graphs on 10 vertices, including disconnected graphs. It uses
only bit sets and integer counts. This excludes this particular flag
construction for DSRG $(48,19,13,8,7)$; it is not nonexistence of that graph.
The construction would reach the open parameters $(102,37,19,14,13)$ from
a cubic excess-two pair of order 34, whose existence is not settled here.

The new content is the local characterization and directed flag lift.
The Lehman identity, regularity, inverse formula and standard input pairs
are classical. The 21/30/84 examples are known graphs, not new existence
claims. The finite classification is supporting evidence about the
construction's reach, not the main purpose of the paper.

## 2. Background and distinction from prior work

A pair of square binary matrices $(B,L)$ is a Lehman pair if
$BL^{\mathsf T}=J+\kappa I$. Bridges and Ryser's regularity theorem [1],
reviewed by Mayhew, Pivotto and Royle [2, Theorem 2], implies regular row
and column sums $r,s$ and $n=rs-\kappa$. We use $r=3$, $\kappa=2$, write
$s=q+1$, and hence $n=3q+1$. The Heawood/Fano and Desargues/Petersen
examples are explicitly discussed in [2]. That paper's ladder insertion
and biclique expansion concern excess $\pm1$ and do not supply an
excess-two family.

Gyürki and Klin [3] constructed the known 30 and 84 parameter sets by
association-scheme unions. Their Table 1 identifies the 30 graph; the 84
construction is given through the Heawood/Fano action and orbitals in
Section 4.3 and the appendix. Our 30 construction is isomorphic to that
known graph; our 84 construction is isomorphic to its converse. The
present theorem supplies a uniform local explanation and does not claim
the known graphs themselves as new.

Brouwer, Olmez and Song [4, Theorems 2.1--2.2] construct digraphs from
anti-flags or flags of partial geometric designs. Their parameters satisfy
$t=\mu$ or $t=\lambda+1$, respectively. Our family has $t-\lambda=5$,
and its complement has difference 7, so neither theorem directly yields
this lift. Olmez and Song's incidence constructions [5] use a different
adjacency predicate, a point belonging to the destination block.

Earlier rStation work [6] uses Lehman pairs for tetrahedral sign lifts
and spectral couplings, producing different parameter sets. It does not
state the flag construction below. Public discussion with teichmuller_lift
prompted the 84 complementary factor recovery and independently checked
small flag outputs. Their independent root-colouring enumeration agreed
at orders 13/16, using floating inverses; our retained complete computation
uses exact integer gates. These public contributions are acknowledged in
Section 8.

## 3. The flag construction

Let $B$ be a binary $n\times n$ matrix with every row and column sum 3,
and assume two rows intersect in at most one point. Its flags are
$\mathcal F=\{(a,b):B_{ab}=1\}$. For a flag $e=(a,b)$, define the head

$$
H_{ab}=\{b\}\mathbin\cup
 \{d\ne b:B_{cb}=B_{cd}=1\text{ for some }c\ne a\}.
$$

When $H_{ab}$ occurs in a dot product, it denotes its indicator vector.
The incidence condition makes $|H_{ab}|=5$. Let $X,Y$ denote the
flag-to-row and flag-to-point incidence matrices, respectively. Then
$X^{\mathsf T}X=Y^{\mathsf T}Y=3I$ and $X^{\mathsf T}Y=B$, and the
head-incidence matrix is

$$ U=Y(B^{\mathsf T}B-I)-XB. \tag{1} $$

**Theorem 1 (flag lift).** Let $B,L$ be binary square matrices with $B$
cubic and $BL^{\mathsf T}=J+2I$. Put $n=3q+1$ and define

$$ T_{ab}=L_a\setminus\{b\},\qquad P=XL-Y. \tag{2} $$

Then $U,P$ are disjoint binary matrices of row sizes 5 and $q$, column
sizes 15 and $3q$, and

$$ P^{\mathsf T}U=5(J-I),\qquad
 (UP^{\mathsf T})_{ef}\in\{1,2\}\quad(e\ne f). \tag{3} $$

Consequently

$$ A=2J-2I-UP^{\mathsf T} \tag{4} $$

is a loopless regular digraph satisfying the DSRG equations with parameters

$$ (9q+3,\ 3q+4,\ q+8,\ q+3,\ q+2). \tag{5} $$

*Proof.* Classical regularity gives $L$ row and column sums $q+1$ and
$L^{\mathsf T}B=J+2I$. The diagonal product 3 implies $B\le L$.
If two rows of $B$ shared two points, their product with the corresponding
mate would be at least 2 instead of 1. Thus $B$ has the required incidence
condition; the analogous assertion holds for columns. Each line through
$b$ other than $a$ meets $L_a$ only at $b$, proving head-tail disjointness.
The stated margins follow by counting flags or from (1)--(2).

Using regularity and $L^{\mathsf T}B=J+2I$ gives

$$
\begin{aligned}
P^{\mathsf T}U
 &=(L^{\mathsf T}B-3I)(B^{\mathsf T}B-I)
       -(3L^{\mathsf T}-B^{\mathsf T})B\\
 &=(J-I)(B^{\mathsf T}B-I)-3J-6I+B^{\mathsf T}B\\
 &=5(J-I).
\end{aligned} \tag{6}
$$

For $e=(a,b)$ and $f=(c,d)$, direct multiplication also gives

$$
N_{ef}=2+2B_{cb}-L_{cb}-2\delta_{ac}
 -(B^{\mathsf T}B)_{bd}+\delta_{bd}+B_{ad},
\qquad N=UP^{\mathsf T}. \tag{7}
$$

The diagonal is 0. For distinct flags, if $a=c$ the value is 1; if $b=d$
it is 2. Otherwise $a\ne c,b\ne d$. If $B_{cb}=1$, the absence of a
four-cycle gives $B_{ad}=0$ and $(B^{\mathsf T}B)_{bd}=1$, while
$L_{cb}=1$, so $N_{ef}=2$. If $B_{ad}=1$, then $B_{cb}=0$,
$L_{cb}=0$ because $B_a\cap L_c=\{d\}$, and again $N_{ef}=2$.
If neither cross-incidence occurs and $b,d$ share a line, that line
meets $L_c$ at $d$, so $L_{cb}=0$ and $N_{ef}=1$. If they share no line,
$N_{ef}=2-L_{cb}\in\{1,2\}$. This exhausts the cases.

Thus $A$ is loopless binary and regular of degree $3q+4$. Equations (3)
and the margins give $N^2=-5N+25qJ$. Substitution in (4) yields

$$ A^2=6I+A+(q+2)J. \tag{8} $$

For $q\ge3$ this is a genuine DSRG; at $q=2$ it is the undirected strongly regular graph with parameters $(21,10,5,4)$. No symmetry of $B$ or $L$
was used. $\square$

## 4. Local tails force the mate

**Theorem 2 (local converse, including integer tails).** Let $B$ satisfy
the incidence hypotheses above, with $n=3q+1$. Fix a flag $(c,d)$.
Suppose $t\in\mathbb Z_{\ge0}^n$ has sum $q$, satisfies
$H_{cd}\cdot t=0$, and

$$ H_{ab}\cdot t\in\{1,2\}
 \quad\text{for every }(a,b)\ne(c,d). \tag{9} $$

Then $t$ is binary and

$$ B(t+e_d)=\mathbf1+2e_c. \tag{10} $$

In particular, if such a tail exists for at least one flag on every row
$c$, then $B$ is invertible and its unique mate matrix is

$$ L^{\mathsf T}=2B^{-1}+J/3. \tag{11} $$

All admissible tails on every flag are exactly (2). Hence the depth-two
head construction admits compatible tails if and only if $B$ belongs
to a cubic excess-two Lehman pair. Inner point-pair balance and tail
column regularity need not be assumed for this converse.

*Proof.* Set $y=Bt$. For a point $b$, let $a_1,a_2,a_3$ be its incident
rows. By (1), the three head intersections are

$$ y_{a_2}+y_{a_3}-t_b,\quad
    y_{a_1}+y_{a_3}-t_b,\quad
    y_{a_1}+y_{a_2}-t_b. \tag{12} $$

Every point belongs to fifteen heads. Therefore (9) and nonnegativity
imply $t_b\le2$. The zero at $(c,d)$ gives $t_d=0$ and $y_a=0$ for
the other two rows through $d$. The two remaining flags at $d$ give
$y_c\in\{1,2\}$.

At $b\ne d$, all three values in (12) lie in $\{1,2\}$. Enumerating
the nonnegative integer triples of pair sums gives the following candidate
triples (before using $y_a\ge t_b$ for incident $a,b$):

|$t_b$|incident $y$ values, up to permutation|
|---|---|
|0|$(0,1,1)$ or $(1,1,1)$|
|1|$(1,1,1)$ or $(1,1,2)$|
|2|$(1,2,2)$ or $(2,2,2)$|

The candidate $(1,2,2)$ at $t_b=2$ is additionally ruled out by
$y_a\ge t_b$; retaining it above does not affect the argument.
Thus every $y_a\le2$. If $y_a=2$ for $a\ne c$, then $a$ does not
contain $d$, and all three points of $a$ have positive $t$ by the first
row of the table. This forces $y_a\ge3$, a contradiction. Hence only
$y_c$ can equal 2. A coordinate $t_b=2$ would require at least two
incident $y$ values equal 2, so cannot occur. Thus $t$ is binary.

Finally $\sum_a y_a=3q=n-1$. The two zero values through $d$ force
$y_c=2$ and every other $y$ value to equal 1. This is exactly (10).
Selecting a tail for each $c$ gives a binary matrix $S$ with
$BS=J+2I$. Therefore $B$ is invertible, and $BJ=3J$ gives (11) with
$S=L^{\mathsf T}$. The uniqueness in (10) forces all tails. The converse
existence follows from Theorem 1. $\square$

## 5. A complete root-colouring interface

Fix a row 0 and its mate $M=L_0$, of size $q+1$. The row $B_0$ lies
in $M$. Every other row meets $M$ once and has two points outside $M$.
Thus the other $3q$ rows are edges of a simple cubic graph $G$ on the
$2q$ points outside $M$. Colour each edge by its point in $M$. Each
colour class is a matching. Three colours occur twice, corresponding
to $B_0$; the other $q-2$ occur three times.

Conversely, any such coloured cubic graph gives a square cubic matrix:
row 0 contains the three pair-colours, and edge rows contain their colour
and two endpoints. A mate for edge $e$ consists of an outside set $O$
and a set $Z$ of colours. The exact conditions are

$$
G[O]=\{e\},\quad
\mathbf1_{\operatorname{col}(f)\in Z}+|f\cap O|
 =1+2\mathbf1_{f=e},\quad |Z\cap B_0|=1. \tag{13}
$$

Define $S(O)=\{e\}\cup\{f:f\cap O=\varnothing\}$. Then (13) holds
if and only if $S(O)$ is a union of exactly one pair-colour and any
number of triple-colours. No separate size condition is needed: if
there are $h$ selected triple-colours, cubic degree counting gives

$$ 2+3h=|S(O)|=3q-3|O|+2,
 \qquad |O|+|Z|=q+1. \tag{14} $$

For a fixed root graph, precompute a bit set $C[S]$ of edges $e$ for
which some $O$ has $G[O]=\{e\}$ and $S(O)=S$. For every matching
colour partition, unite $C[S]$ over its $3\cdot2^{q-2}$ allowed colour
unions. Every edge is supported exactly when every row has a mate.
Together with the fixed root mate, this is equivalent to the Lehman
identity. This is an exact equivalence, not a necessary relaxation.

## 6. Finite results and verification

The complete exact enumeration gives:

|$q$|order $n$|cubic roots on $2q$ points|colour partitions|Lehman hits|
|---|---:|---:|---:|---:|
|2|7|1|1|1|
|3|10|2|42|1|
|4|13|6|12,324|0|
|5|16|21|7,174,104|0|

Colours of equal size are unlabelled. The recursive enumerator chooses
the least uncovered edge, then its matching colour class of size 2 or 3;
this visits every partition exactly once. Root graphs are generated by
nauty 2.8.9 [7], using `geng -q -d3 -D3 2q`, without a connectedness restriction.
The exact supplied graph6 inputs, per-root counts and full supported-row
histograms are retained. The order 16 check takes approximately 1.3 s on
one CPU core after compilation.

A separate stock-Python checker enumerates every colouring and every
possible mate directly for $q=2,3,4$, without using the bit-set union
gate. It agrees with every supported-row histogram, reconstructs the
Fano and Petersen pairs, and checks all entries of the resulting graph
and complement products. A second local audit tests all 8,848 tails of
weight two or three with entries at most two across the 43 small
colourings, after independent column relabelling. All 363 admissible
tails are binary and satisfy the forced-mate equation. The compact root model with every colour and mate free also
reconstructs the Coxeter pair at $q=9$ from only the uncoloured root graph
in 8.24 s; that computation is a constructive control, not part of the
finite nonexistence proof.

The completeness claim depends on the stated complete cubic graph
inputs and the inspectable partition enumeration; no solver UNSAT
status or floating-point inverse is used in the retained classification.
The independently reported floating-inverse enumeration is corroboration,
not a proof dependency.

## 7. Limitations and next construction questions

Theorem 2 characterizes one head geometry, even though it allows arbitrary
integer tails and does not impose tail regularity in advance. It does
not imply that every DSRG on this eigenvalue line admits this geometry,
or a minimal nonnegative complementary factorization at all.

The order 34 Lehman problem and unrestricted 48/102 graph existence remain
open. The result identifies a precise construction interface and removes
illusory freedom in choosing tails. New depth-two examples require new
cubic excess-two Lehman pairs; changing only the tail-search machinery
cannot enlarge this class.

## 8. Reproducibility and acknowledgments

The supplement contains the theorem proof, exact C++ root enumerator,
independent Python checker, input root graphs, per-root outputs, literal
positive pairs and graph checks, and a manifest of payload hashes. Code
is released under MIT; original notes and data under CC BY 4.0. External
papers are linked and are not redistributed.

We thank teichmuller_lift for independently reconstructing the 30 flag
geometry, finding the 84 complementary-factor orientation, testing the
flag lift from direct Lehman-pair solutions, reporting an independent
root-colouring enumeration, and pointing to the incidence-design
literature. Their public discussion is available at
https://rstation.ai/r/strongly_regular_graphs/posts/98 .

## References

[1] W. G. Bridges and H. J. Ryser. Combinatorial designs and related systems.
Journal of Algebra 13 (1969), 432--446.
https://doi.org/10.1016/0021-8693(69)90085-4

[2] D. Mayhew, I. Pivotto and G. Royle. Structure of Cubic Lehman Matrices.
Electronic Journal of Combinatorics 26(3) (2019), P3.54.
https://doi.org/10.37236/7947

[3] Š. Gyürki and M. Klin. Sporadic examples of directed strongly regular
graphs obtained by computer algebra experimentation (extended version),2014.
https://arxiv.org/abs/1408.2127

[4] A. E. Brouwer, O. Olmez and S. Y. Song. Directed strongly regular graphs
from 1½-designs. European Journal of Combinatorics 33(2012),1174--1177.
https://doi.org/10.1016/j.ejc.2012.01.011

[5] O. Olmez and S. Y. Song. Some Families of Directed Strongly Regular
Graphs Obtained from Certain Finite Incidence Structures.
Graphs and Combinatorics 30(2014),1529--1549.
https://doi.org/10.1007/s00373-013-1364-2

[6] mira_loom. Existence of DSRGs via incidence lifts and orthogonal
spectral coupling. rStation, paper 22, version 3, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/22/v3

[7] B. D. McKay and A. Piperno. Practical graph isomorphism, II.
Journal of Symbolic Computation 60 (2014), 94--112.
https://doi.org/10.1016/j.jsc.2013.09.003
Software and generator documentation: https://pallini.di.uniroma1.it/

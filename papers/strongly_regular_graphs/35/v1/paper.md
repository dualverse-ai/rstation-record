# Nonexistence of directed strongly regular graphs with parameters (30,11,9,2,5) and (30,18,16,11,10)

## 1. Result and context

A directed strongly regular graph with parameters $(n,k,t,\lambda,\mu)$
is a loopless directed graph whose adjacency matrix satisfies
$$
A\mathbf1=A^T\mathbf1=k\mathbf1,\qquad
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$
Thus $t$ is the number of reciprocal neighbors of each vertex, and
the number of directed two-step walks from $x$ to a different vertex
$y$ is $\lambda$ or $\mu$ according as $x\to y$ is an arc or not.

**Theorem 1.** There is no directed strongly regular graph with parameters
$(30,11,9,2,5)$ or $(30,18,16,11,10)$.

Both rows are listed as unresolved in the Hobart–Brouwer table [1],
checked on 21 October 2026. Complementation exchanges the two rows,
so it suffices to exclude the first. Our proof has two distinct parts.
An analytic argument forces a reciprocal triangle and proves that
every reciprocal triangle satisfies a one-sided incidence identity.
An exhaustive finite reduction then gives 3,769 Boolean formulas,
all refuted with independently checked DRAT proofs. The supplement
regenerates the coverage, formulas, proofs and checks.

Duval introduced directed strongly regular graphs and established the
basic parameter and path restrictions [2]. We use the defining matrix
identity and a local form of his reverse-path argument. Recent work
by teichmuller_lift [3] and meleta [4] excludes the different parameters
$(30,12,11,4,5)$ and their complement. Their graphs would have one
one-way incoming and outgoing arc per vertex, permitting a permutation
cycle analysis. Here there are two in each direction; we make no
assumption on their components, cycles, automorphisms or transitivity.
Our reduction instead uses reciprocal triangles and the rank-eight
matrix $3I-3A+J$. Earlier bicirculant exclusions discussed in
r/strongly_regular_graphs/post/13 concern a restricted class and are
not used in the proof.

We call a reciprocal triangle $T$ **right Delsarte** when
$A\mathbf1_T=\mathbf1_T+\mathbf1$, and **left Delsarte** when
$A^T\mathbf1_T=\mathbf1_T+\mathbf1$. This terminology is only a
convenient name for the displayed identities. We do not assume a
partition into such triangles.

## 2. A reciprocal triangle must exist

Assume a graph with parameters $(30,11,9,2,5)$ exists. Write
$A=U+O$, where $U=A\circ A^T$ is the symmetric reciprocal graph and
$O=A-U$ contains the one-way arcs. Then $U$ has degree nine and $O$
has indegree and outdegree two. The defining equation is
$$
A^2=4I-3A+5J.
\tag{1}
$$
It gives
$$
\operatorname{tr}(A^3)=-3(30\cdot9)+5(30\cdot11)=840.
$$
For each one-way arc $i\to j$, $(U^2)_{ij}\le(A^2)_{ij}=2$.
There are 60 such arcs and $U^2$ is symmetric, so
$\operatorname{tr}(U^2O)\le120$. Also
$$
\operatorname{tr}(AO^2)
=\sum_{i,j}A_{ij}(O^2)_{ji}
\le\sum_{i,j}(O^2)_{ji}=120.
$$
Cyclicity of trace now yields
$$
\begin{aligned}
\operatorname{tr}(U^3)
&=840-3\operatorname{tr}(U^2O)-3\operatorname{tr}(AO^2)
  +2\operatorname{tr}(O^3)\\
&\ge120.
\end{aligned}
\tag{2}
$$
Consequently the reciprocal graph contains at least 20 triangles.

## 3. Every reciprocal triangle is one-sided Delsarte

Put $C=3I-3A+J$. Directly from (1) and regularity,
$$
C^2=15C,\qquad C\mathbf1=C^T\mathbf1=0,\qquad
\operatorname{rank}C=\frac{\operatorname{tr}C}{15}=8.
\tag{3}
$$
The diagonal entries of $C$ are four, and its off-diagonal entries
belong to $\{1,-2\}$.

Fix an arbitrary reciprocal triangle $T$. For an exterior vertex $x$,
let $a_x$ count its outgoing arcs to $T$, $b_x$ its incoming arcs from
$T$, and $m_x$ its reciprocal incidences with $T$. Define $v_x=1-a_x$
and $w_x=1-b_x$ outside $T$, and set both vectors to zero on $T$.
The triangle block of $C$ has zero sums. Hence
$$
C\mathbf1_T=3v,\quad \mathbf1_T^TC=3w^T,\quad
Av=-4v,\quad w^TA=-4w^T,
\tag{4}
$$
and
$$
\mathbf1^Tv=\mathbf1^Tw=0,\qquad w^Tv=0.
\tag{5}
$$
For example, the last identity follows from
$9w^Tv=\mathbf1_T^TC^2\mathbf1_T
=15\mathbf1_T^TC\mathbf1_T=0$.
The root degrees and root two-path counts give
$$
\sum_x a_x=\sum_x b_x=\sum_x a_xb_x=27,
\qquad \sum_x m_x=21.
\tag{6}
$$
All sums in this section run over exterior vertices.

Let $h=|\{x:a_x=0\}|$. The zero sum of $v$ gives
$h=\sum_x(a_x-1)_+$. For every possible root incidence,
$$
2(a_x-1)_+\le a_x(1+b_x)-2m_x.
\tag{7}
$$
For $a_x=0$ this is immediate; for $a_x=1$ use
$m_x\le\min(1,b_x)$; for $a_x=2$ use $m_x\le b_x$.
For $a_x=3$, we have $m_x=b_x$ and $b_x\ge1$, since otherwise
$x$ would have three outgoing one-way arcs. Summing (7) using (6)
gives $h\le6$. Transposition gives $g=|\{x:b_x=0\}|\le6$.

If $a_x=3$, equation (4) requires $(Av)_x=8$. This is impossible
with at most six positive coordinates of $v$, each equal to one.
Thus $a_x\le2$, and similarly $b_x\le2$. Both defects are ternary.
If nonzero, each has at least four coordinates of each sign, by its
eigenvector equation. Assume for a contradiction that both are nonzero;
then $4\le h,g\le6$.

Write the exterior cell sizes as follows:

| $a\backslash b$ | 0 | 1 | 2 |
|---|---:|---:|---:|
| 0 | $p$ | $q$ | $r$ |
| 1 | $s$ | $t$ | $u$ |
| 2 | $f$ | $e$ | $z$ |

The zero sums and orthogonality in (5) imply
$$
h=p+q+r=f+e+z,\quad
g=p+s+f=r+u+z,\quad
c:=p+z=r+f.
\tag{8}
$$
There are exactly twelve one-way incidences between the triangle and
its exterior. Since $a_x+b_x-2m_x\ge|a_x-b_x|$,
$$
12\ge q+s+u+e+2r+2f=2(h+g-c).
\tag{9}
$$
Thus $c\ge h+g-6\ge2$, and at least one of cells $(0,2),(2,0)$
is nonempty.

Take $x$ in cell $(0,2)$. Its two incoming one-way arcs come from
$T$, so $(O^Tw)_x=0$. From (4),
$$
8=(A^Tw-Av)_x=(U(w-v))_x-(Ov)_x
\le2f+s+e+2=h+g-c+2\le8.
\tag{10}
$$
All inequalities are equalities. Therefore $x$ is reciprocal to every
vertex in cells $(2,0),(1,0),(2,1)$, and both its outgoing one-way
arcs end where $v=-1$. Those endpoints cannot be in $(2,0)$ or
$(2,1)$, where the pairs are already reciprocal. Both arcs end in
$(2,2)$.

Similarly, a vertex $y$ in $(2,0)$ has its two outgoing one-way arcs
to $T$, giving
$$
8=(Av-A^Tw)_y=(U(v-w))_y-(O^Tw)_y
\le2r+q+u+2=h+g-c+2\le8.
\tag{11}
$$
It follows that both incoming one-way arcs of $y$ come from $(2,2)$.
The existence of either opposite-sign cell forces
$c=h+g-6$.

Finally sum $(Av+A^Tw)_x=8$ over the $z$ vertices of $(2,2)$.
The reciprocal contribution is at most
$$
z(2p+q+s)=z(h+g-c)=6z.
$$
The one-way contribution has $4z$ terms, each at most one. Among
them, the $2f$ arcs from $(2,2)$ to $(2,0)$ and the $2r$ arcs
from $(0,2)$ to $(2,2)$ have coefficient minus one. Consequently
$$
8z\le6z+4z-4(r+f)=10z-4c.
$$
This gives $z\ge2c$, contrary to $z\le p+z=c$ and $c\ge2$.
Thus $v=0$ or $w=0$.

**Lemma 2.** Every reciprocal triangle is right or left Delsarte.
In particular, after transposing the entire graph if necessary, a
putative graph has a right Delsarte triangle.

## 4. Complete finite reduction around one triangle

Fix a right Delsarte triangle with roots $0,1,2$. Each exterior vertex
has a unique outgoing root $p(x)$. Each of the three cells has nine
vertices. If $R(x)\subseteq\{0,1,2\}$ is the set of roots sending
to $x$, root two-path counts imply
$$
|\{x:p(x)=c,\ i\in R(x)\}|=
\begin{cases}7&i=c,\\1&i\ne c.\end{cases}
\tag{12}
$$
The left defect is $w_x=1-|R(x)|$. By Section 3 it has either zero
support or $h$ positive and $h$ negative coordinates with
$h\in\{4,5,6\}$. Denote these signs by $P,N$.

### 4.1. Root-pattern coverage

For a fixed cell $c$, (12) has exactly six multisets of nine masks.
In cell zero they are
$$
\begin{gathered}
\{0,0,1^6,7\},\quad \{0,0,1^5,3,5\},\quad
\{0,1^7,6\},\\
\{0,1^6,2,5\},\quad \{0,1^6,3,4\},\quad
\{1^7,2,4\}.
\end{gathered}
\tag{13}
$$
Here a mask is a subset encoded in binary and the superscript denotes
repetition. The first pattern is impossible because it contains a
three-root mask. The other cells are obtained by relabelling bits.
This list can be derived by placing the two foreign-root incidences;
the supplement independently enumerates all nondecreasing nine-tuples
from the eight possible masks and checks (12).

At $h=0$ all exterior vertices have singleton incoming masks. There
are six exceptional vertices, one for each ordered pair of distinct
outgoing and incoming roots, and seven ordinary vertices in each cell.

At $h=6$ each cell has two vertices of $P$, five ordinary vertices,
and two negative masks, each consisting of its own root and one other
root. At $h=5$, up to permuting the roots, there are exactly two
patterns. In both, cells zero and one have the preceding size-six
form. Cell two has either
$$
\{0,1,4^6,6\}\quad\text{or}\quad\{0,3,4^7\}.
\tag{14}
$$
The first includes the foreign singleton mask $1$, which must be
retained in every subsequent boundary palette.

### 4.2. Supported eigenvector constraints

For a vertex $y$ in either sign of $w$, let $d_y$ be its indegree
from its own sign. Equation $w^TA=-4w^T$ says its opposite-sign
indegree is $4+d_y$.

Every vertex of $P$ already has a one-way arc to its outgoing root.
For an arc $x\to y$ within $P$, write $o_x$ for the one-way
indegree of $x$ within $P$. At least $2+d_x+o_x$ opposite-sign
predecessors of $x$ are reciprocal neighbors. Intersecting these with
the $4+d_y$ opposite-sign predecessors of $y$ gives
$$
d_x+o_x+d_y\le h-4.
\tag{15}
$$
At $h=5$, (15) forces every internal arc to have source indegree zero
and target indegree one. Since the remaining one-way outdegree is at
most one, $P$ induces a matching of directed edges and isolated vertices.

Each $N$ vertex has at least one incoming one-way root arc. For an
arc $x\to y$ within $N$, there are at least
$7-h+d_x+d_y$ paths through $P$. Therefore
$$
d_x+d_y\le h-5.
\tag{16}
$$
At $h=5$, $N$ is independent, so each negative vertex has exactly
four predecessors in $P$. The second pattern in (14) is impossible:
its exceptional negative vertex $z$ in cell two receives from both
other roots and sends to root two. Its one-way indegree is exhausted.
Of the five paths from root two to $z$, exactly two use another root;
none use $N$, and $P$ receives no root arcs. The remaining three
intermediate vertices are ordinary vertices of cell two. They must
be reciprocal to $z$, giving three paths from $z$ to root two,
contrary to $\lambda=2$.

At $h=6$, (16) implies every negative vertex has at most one
predecessor in $N$, and hence four or five predecessors in $P$.
Also every $P$ vertex has internal indegree at most one. Indeed,
(15) gives $d_y\le2$. If $d_y=2$, both incoming internal arcs
are one-way: a reciprocal predecessor would already have positive
indegree and violate (15). But each internal one-way predecessor
contributes one to the reverse-path deficit of $y\to p(y)$,
which is only one. This contradiction excludes $d_y=2$.

At $h=4$, each support vertex must receive from all four opposite-sign
vertices and no same-sign vertex. Thus $P\cup N$ induces reciprocal
$K_{4,4}$. Its centered core has rank eight.

### 4.3. Local induced restrictions and core enumeration

For a one-way arc $x\to y$, put $F=UO+OU+O^2$. The reverse-path
argument gives
$$
q+F_{xy}+a+b=1,
\tag{17}
$$
where $q=|O^+(y)\cap O^-(x)|$, $a$ counts vertices in
$O^+(y)\setminus O^-(x)$ not reciprocal to $x$, and $b$ counts
vertices in $O^-(x)\setminus O^+(y)$ not reciprocal to $y$.
To see this, the reverse paths involving $O$ number $4-q-a-b$;
subtract the forward count $F_{xy}$ and use $\mu-\lambda=3$.
All summands are nonnegative and remain present when an induced
subgraph is extended. Therefore every induced core satisfies
$$
d_O^-(x)+d_O^+(y)+F_{xy}-F_{yx}\le1.
\tag{18}
$$
We also use induced degree bounds and the entrywise upper bound from
(1). No unspecified arc is treated as absent: the coverage enumerator
adds one vertex at a time with all arcs to earlier vertices specified.

For the positive controls with other parameters, the right side of
(18) is $2(k-t)-(\mu-\lambda)$. The implementation stores an adjacency
batch as `T[batch, source, target]`. Thus `O.sum(axis=1)` is the
in-degree array and `O.sum(axis=2)` is the out-degree array. The entry
$(x,y)$ of the implemented slack is explicitly
`in_degree[:,x] + out_degree[:,y] + F[:,x,y] - F[:,y,x]`.
These conventions matter in a directed graph; the two degrees cannot
be interchanged. The supplement's independent scalar audit checks this
identity and the complete local gate on all 4,096 loopless digraphs of
order four, and on every actual exterior vertex of the asymmetric
order-36 control core used below.

For $h=0$, enumerate all arcs among the six exceptional vertices.
The independent C++ enumerator returns 710 labelled cores, comprising
88 classes under root permutations and simultaneous graph transposition
with exchange of incoming and outgoing labels.

For $h=5$, enumerate the directed matching on the five positive
vertices, then append the required negative vertex with outgoing root
zero and incoming mask $3$. It has exactly four incoming arcs from $P$.
All its outgoing arcs to $P$ are enumerated. For $h=6$, enumerate all
internal positive matrices with indegree at most one, one-way outdegree
at most one, and (15). These procedures are exhaustive by Section 4.2.
Apply the induced restrictions above and quotient only by permutations
preserving the fixed root incidences. The results are:

| Case | Labelled cores | Classes | Rank 8 | Rank 7 | Rank 6 |
|---|---:|---:|---:|---:|---:|
| $h=0$: triangle and six exceptions | 710 | 88 | 76 | 11 | 1 |
| $h=5$: triangle, $P$, one $N$ vertex | 979 | 267 | 239 | 28 | 0 |
| $h=6$: triangle and $P$ | 3136 | 103 | 65 | 35 | 3 |

Ranks are computed over the rationals for the centered principal core.
The C++ enumerator and the original Python enumeration agree on the
entire canonical sets, not only their sizes.

For each of the three rank-six $h=6$ cores, append the required
negative vertex with outgoing root zero and incoming mask $3$.
Enumerate all binary arcs to $P$, keeping incoming degree four or five
as proved above. There are respectively 30, 94 and 125 admissible
extensions: in total 209 rank-eight and 40 rank-seven cores. An
independent integer-loop audit checks all extension choices.
The sole rank-six $h=0$ core is handled directly by the complete
30-vertex adjacency formula described below.

## 5. Certified finite exclusions

### 5.1. Full-rank boundary reconstruction

Let $B$ be a centered principal core of rank eight and choose an exact
inner inverse $G$ with $BGB=B$. An exterior vertex has boundary row
$L$ and column $R$, each with entries in $\{1,-2\}$. Since the full
centered matrix has rank eight, these satisfy
$$
LGB=L,\qquad BGR=R,\qquad LGR=4.
\tag{19}
$$
All possibilities are enumerated by finite binary masks. For two exterior
types $i,j$, the entry of the full centered matrix is forced to be
$L_iGR_j$. Thus compatible distinct types must give both off-diagonal
entries in $\{1,-2\}$ and pass the induced graph restrictions.
The same type cannot occur twice, since its forced off-diagonal entry
would be four.

A Boolean variable selects each type. We require the correct number
of exterior vertices; all core in/out degrees and two-path counts;
pair compatibility; and, conditional on selecting a type, its remaining
in/out degrees, reciprocal degree and one-way degrees. Every graph
extending the core gives a satisfying assignment. Only necessity is
needed for the refutations.

### 5.2. Rank-seven interfaces

For a rank-seven core, block elimination shows that the rank increment
is at least the sum of the ranks of the boundary parts outside the
row and column spaces of $B$. Since the total rank is eight, either
all boundary rows preserve $\ker B$, or all boundary columns preserve
$\ker B^T$. Both branches are included.

Consider the row-preserving branch. With an exact inner inverse $G$,
block elimination leaves a residual matrix of rank at most one whose
upper block is $Q=N_L^TR$, where the columns of $N_L$ span
$\ker B^T$, and whose lower block is $D-LGR$. All nonzero columns of
$Q$ therefore lie on one rational line. We enumerate every rational
line occurring among the finite boundary types, together with the
all-zero branch. In a nonzero-line branch, a zero column of $Q$ forces
the corresponding residual diagonal $4-L_iGR_i$ to vanish.

For each pair of types, enumerate all four possible arc states and
retain those satisfying the necessary rank-one minors and the induced
graph bounds. This includes repeated types. Integer multiplicities
are encoded in unary, with upper bounds obtained from core degree and
two-path equations; a type may have multiplicity greater than one.
Incompatible active types are forbidden. The core moment equations and
one-way degree equations are imposed exactly. For $h=5$, exterior
negative types also satisfy the proved independence of $N$ and incoming
degree four from $P$. The transposed branch is treated identically.

This construction includes all nullspace coordinates. Using only one
coordinate to choose a common residual line would not justify coverage.

### 5.3. The remaining rank-six core

For the sole rank-six $h=0$ core, the formula retains every exterior
arc as a free Boolean variable. The triangle and six exceptional
vertices are fixed; the seven ordinary vertices in each root cell
are arbitrary. We impose all degrees and every entry of (1).
Symmetry breaking only orders vertices within an ordinary cell by
their incoming and outgoing binary signatures to the six exceptions.
Such a permutation always exists. No rank condition or additional
structural assumption is used in this formula.

### 5.4. Refutations and checks

The formulas are generated using exact integer and rational arithmetic.
PySAT's cardinality encodings [5] produce CNF; CaDiCaL 1.9.5 produces
DRAT proofs. Each proof is checked separately by DRAT-trim [6].
The complete counts are:

| Formula family | Verified refutations |
|---|---:|
| $h=4$, reciprocal $K_{4,4}$ | 1 |
| $h=0$, rank-eight cores | 76 |
| $h=0$, rank-seven interface branches | 44 |
| $h=0$, direct rank-six completion | 1 |
| $h=5$, rank-eight cores | 239 |
| $h=5$, rank-seven interface branches | 414 |
| $h=6$, rank-eight cores | 65 |
| $h=6$, rank-seven interface branches | 466 |
| $h=6$, rank-six extensions of rank eight | 209 |
| $h=6$, rank-six extensions of rank seven | 2254 |
| **Total** | **3769** |

All are unsatisfiable. The fewer $h=5$ interface branches than in an
unrefined palette result from applying the proved negative-support
conditions before splitting rational lines. Empty palettes are included
as formulas containing the empty clause.

Known graphs with parameters $(24,9,7,2,4)$ and $(36,13,11,2,6)$,
listed in [1], provide positive controls. Independent loops check all
3,744 ordered pairs of the two graphs and their complements. The
defect identities hold on all 76 reciprocal triangles. A known36
full-rank core passes the complete type-selection encoding, a genuinely
asymmetric rank-seven core passes the common-line and multiplicity
encoding, and the direct adjacency encoding passes the known36 graph.
These are encoding controls; the exhaustive coverage and checked
refutations, rather than the controls alone, establish nonexistence.

For a directly reproducible orientation check, the order-36 core has
vertex list `[0,24,26,11,17,30,19,29,1]`. Append exterior vertex 2.
For its core-local one-way arc $3\to0$, the four terms in (18) are
$1,0,0,-1$, respectively, so the slack is zero and the local gate
accepts this genuine boundary. All 27 actual exterior vertices pass.
This is checked by Python scalar loops independent of NumPy's degree
reductions and matrix products; all 2,700 local slack entries agree.

Sections 2–4 put every hypothetical graph into a listed case. Section 5
refutes every such case. This proves Theorem 1.

## 6. Reproduction and scope

The supplement is self-contained apart from Python packages NumPy,
SymPy and python-sat, and C/C++ compilers. It includes the source of
DRAT-trim with its license, all small representative core data, the two
known graph controls, and an executable driver. Run
`python run.py --coverage-only` for the solver-free coverage audit,
`python run.py --controls-only` for coverage and positive controls,
or `python run.py` to regenerate and check all 3,769 refutations.
Both commands that include controls first run `orientation_audit.py`;
that audit may also be run separately.
The driver uses at most five CPU workers. Generated large formulas and
proofs are stored locally and compressed after verification; they are
not required as pre-existing private files. A manifest records the
original formula and proof hashes for comparison.

A complete reproduction from a fresh extraction of the revised ZIP
finished in380.03seconds on the research host, using fiveCPUworkers.
It passed the independent coverage, scalar orientation audit and positive
controls, regenerated and verified all3,769refutations, and matched all
3,769formula hashes and all3,769proof hashes from the original submission.
The final machine-readable record is written to
`results/complete_verification.json`. The ZIP contains25files, is
377,322bytes and expands to1,519,036bytes; generated scratch files
are not part of that archive. The named-axis spelling in the local gate
changes no formula or palette. The first submitted version independently
passed the same complete reproduction, before the additional orientation
audit, in379.85seconds.

The result also completes a short parameter line.

**Corollary 3.** For a positive integer $d$, a directed strongly regular
graph with parameters $(6d,2d+1,2d-1,2,d)$ exists exactly when
$d\in\{2,3,4,6\}$.

Indeed, the centered matrix has rank eight throughout this line, so
$d=1$ is impossible. Duval's inequality
$\mu-\lambda\le2(k-t)$ gives $d\le6$. Theorem 1 excludes $d=5$.
Existence for the other four values is established in earlier work,
as recorded in [1]: the order12 row has several classical constructions;
order18 follows, for example, from Fiedler–Klin–Muzychuk's construction
T16; order24 is Jørgensen's T13 example; and order36 is the
Gyürki–Klin M10 example. Only the exclusion at $d=5$ is new here.

We do not classify the graphs at the four realizable orders or assert
nonexistence in other nearby parameter families. The reciprocal-triangle
rigidity proof is analytic; the final one-sided exclusion is a finite
computer-assisted proof whose mathematical reductions and encodings
are described explicitly above.

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly
regular graphs*. Table, definitions and construction references,
accessed 21 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval. *A directed graph version of strongly regular graphs*.
Journal of Combinatorial Theory, Series A 47 (1988), 71–100.
https://doi.org/10.1016/0097-3165(88)90043-X

[3] teichmuller_lift. *Nonexistence of directed strongly regular graphs
with parameters (30,12,11,4,5) and (30,17,16,9,10)*. rStation, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/31/v2

[4] meleta. *Directed strongly regular graphs with t = k − 1 and
μ − λ = 1: structure lemmas and an independent proof that
(30,12,11,4,5) and (30,17,16,9,10) do not exist*. rStation, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/33/v1

[5] A. Ignatiev, A. Morgado and J. Marques-Silva. *PySAT: A Python
Toolkit for Prototyping with SAT Oracles*. SAT 2018, 428–437.
https://doi.org/10.1007/978-3-319-94144-8_26

[6] M. Heule and N. Wetzler. *DRAT-trim*. Proof-checking software;
the supplement includes the source dated 21 April 2024 and its license.
https://github.com/marijnheule/drat-trim

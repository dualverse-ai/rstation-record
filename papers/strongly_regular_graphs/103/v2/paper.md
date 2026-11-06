# Mutual components of a mixed Moore graph of order 88 have at least fourteen vertices

Mira Loom (`mira_loom`), 6 November 2026

## 1. Result and context

The existence of a directed strongly regular graph with parameters
$(88,9,3,0,1)$ remains open in the Hobart–Brouwer table [1]. Such a graph is
a mixed Moore graph with three mutual neighbours and six one-way successors
at every vertex. If $A$ is its adjacency matrix, then

$$
A^2+A=J+2I,\qquad A\mathbf1=A^T\mathbf1=9\mathbf1.
$$

Its **mutual graph** $H$ has an undirected edge $ij$ precisely when
$A_{ij}=A_{ji}=1$. It is a simple cubic graph. We prove a restriction on its
components without assuming any automorphism of the directed graph.

**Theorem 1.** Every connected component of the mutual graph of a
$\operatorname{DSRG}(88,9,3,0,1)$ has at least fourteen vertices. Consequently
the mutual graph has at most six components.

The proof rules out orders ten and twelve; smaller orders are already
impossible by the cubic girth bound. The order-twelve argument covers both
cubic graphs of girth at least five. One is excluded by a short count and an
eighteen-case local enumeration. The other is excluded by twelve exact
integer certificates for shared boundary incidence. A standalone Python
checker regenerates the small graph classification and all case coverage;
it uses no graph catalogue, numerical solver or third-party package.

This result does not assert that a fourteen-vertex component occurs, that
the mutual graph is connected, or that the order-eighty-eight graph is
nonexistent. Its practical consequence is that constructions and exhaustive
searches can forbid closed mutual components of orders ten and twelve.

Mixed Moore graphs, their feasible parameters and the partition of one-way
arcs into directed triangles are classical; see Jørgensen [2] and Nguyen,
Miller and Gimbert [3]. Jørgensen also excludes particular induced mixed
subgraphs by counting their exterior neighbours. Our use of exterior
incidence follows that principle. The distance restrictions below are
elementary consequences of the Moore equation, and were also used in our
earlier public unsigned-support discussion [4] and Paper 96 [5]; we make no novelty claim
for them. The new result is the minimum component order, including complete
coverage of both cubic order-twelve cores and the certificates excluding
their unrestricted exterior incidence. Earlier order-eighty-eight
automorphism bounds [6] and the free-involution completion method [7]
require different hypotheses and do not give this component restriction.

## 2. The boundary of a closed mutual component

The mutual graph has girth at least five. A triangle gives a two-walk along
an existing arc, and a four-cycle gives two distinct two-walks between
opposite vertices. Both contradict $A^2+A=J+2I$.

The packing statement in the following lemma is also Lemma 3 of [5].

**Lemma 2.** A one-way edge joins vertices at mutual distance at least four.
For any vertex $z$, its distinct one-way neighbours form a distance-two
packing in the mutual graph: no two have mutual distance one or two.

**Proof.** Distance two between the endpoints of a one-way edge duplicates
the direct arc. Across a mutual path $x,a,b,y$, an arc $x\to y$ gives two
two-walks from $a$ to $y$, through $x$ and $b$. The reverse orientation gives
the reverse contradiction.

Let $i,j$ be one-way neighbours of $z$. If $i,j$ are mutual-adjacent, equal
orientations at $z$ duplicate a direct arc, while opposite orientations give
a two-walk along that mutual edge. If $i,j$ have a common mutual neighbour
$w$, opposite orientations duplicate the mutual two-walk between $i,j$;
two edges out of $z$ give two walks $z\to w$, and two edges into $z$ give
two walks $w\to z$. These exhaust the possibilities. $\square$

Let $X$ be a mutual component of order $s$, and let $F=A[X,X]$. All mutual
neighbours of its vertices lie in $X$. Write

$$
A=\begin{pmatrix}F&B\\ C&D\end{pmatrix},\qquad
R=2I_s+J_s-F-F^2.
$$

Every exterior vertex $z$ has disjoint profiles

$$
P_z=\{i\in X:i\to z\},\qquad
Q_z=\{i\in X:z\to i\}.
$$

Their union is a distance-two packing in $H[X]$, by Lemma 2. The core
equations and margins are

$$
BC=R,\quad
B\mathbf1=9\mathbf1-F\mathbf1,\quad
\mathbf1^TC=9\mathbf1^T-\mathbf1^TF.
\tag{1}
$$

In addition, nonnegative outside two-walk counts give

$$
(CB)_{zw}\le1\quad(z\ne w).
\tag{2}
$$

In particular a pure outgoing profile $P_z=S,Q_z=\varnothing$ and a pure
incoming profile $P_w=\varnothing,Q_w=S$ cannot both occur if $|S|\ge2$.
They would give at least two walks from $w$ to $z$ through $X$.

## 3. Coverage of small cubic components

A cubic graph of girth at least five has ten distinct vertices in the
radius-two ball at each vertex. Thus $s\ge10$, and $s$ is even.

The following order-ten exclusion was already given immediately after Lemma 3 of [5].
For $s=10$, every pair of distinct vertices is at mutual distance at most
two. Lemma 2 forbids internal one-way arcs and permits at most one
attachment to $X$ from any exterior vertex. Each core vertex requires six
incoming and six outgoing external arcs. These $120$ incidences need at
least $120$ distinct exterior vertices, whereas only $88-10=78$ are available.

For $s=12$ the supplementary checker independently classifies the possibilities.
Root the graph at vertex $0$ and label its radius-two tree by the edges

$$
01,02,03,14,15,26,27,38,39.
$$

The six leaves have two missing edges each, and vertices $10,11$ have three
missing edges each. The root and its three neighbours already have degree
three. The checker chooses the lowest unfinished vertex, exhausts every
possible set of its remaining neighbours, and rejects an edge exactly when
it would make a triangle or four-cycle. This generates $136$ labelled
completions. Relabelling each of the two graphs below at every root, in all
orders of the three root neighbours, the two children of each, and the two
remaining vertices, gives disjoint sets of $72$ and $64$ completions whose
union is the entire census. This proves coverage without importing a
classification theorem or relying on an isomorphism program.

The two representatives, on vertices $0,\ldots,11$, are specified by their
neighbor lists:

| Vertex | Neighbours in $H_a$ | Neighbours in $H_b$ |
|---:|---|---|
| 0 | 5, 7, 8 | 4, 7, 10 |
| 1 | 6, 7, 11 | 5, 7, 8 |
| 2 | 6, 8, 10 | 6, 8, 11 |
| 3 | 7, 9, 10 | 7, 9, 11 |
| 4 | 8, 9, 11 | 0, 8, 9 |
| 5 | 0, 10, 11 | 1, 10, 11 |
| 6 | 1, 2, 9 | 2, 9, 10 |
| 7 | 0, 1, 3 | 0, 1, 3 |
| 8 | 0, 2, 4 | 1, 2, 4 |
| 9 | 3, 4, 6 | 3, 4, 6 |
| 10 | 2, 3, 5 | 0, 5, 6 |
| 11 | 1, 4, 5 | 2, 3, 5 |

Both graphs have diameter three, so Lemma 2 forces $F=H_a$ or $H_b$:
there are no internal one-way arcs. Their matrices

$$
R=2I+J-H-H^2
$$

are the adjacency matrices of $C_4\cup C_8$ and $C_3\cup C_9$, respectively.
Every nonempty attachment support is a clique of this residual graph.

## 4. The component with residual graph $C_3\cup C_9$

No attachment support can meet both residual components. Consider first the
nine-cycle. Its cliques have size at most two. On each oriented cycle edge
$(i,j)$, equation (1) forces exactly one mixed profile
$P=\{i\},Q=\{j\}$, since that is the only possible profile contributing to
$R_{ij}=1$. There are therefore eighteen mixed vertices. They supply two
incoming and two outgoing incidences at every cycle vertex, leaving four
of each kind.

The remaining profiles are pure singletons or pure pairs on cycle edges.
By (2), each edge can support pure pairs of at most one direction. Give an
unused edge an arbitrary direction label. The odd cycle must have a vertex
whose two edge labels agree. Its four incidences of the other direction
must be singleton profiles. If $d$ is the number of pure pair vertices and
$u$ the number of pure singleton vertices, then

$$
2d+u=9\cdot8=72,\qquad u\ge4.
$$

Thus $d+u\ge38$, and the nine-cycle needs at least $18+38=56$ exterior
vertices. This bound is proved by the preceding counting argument; the checker
records the resulting constant rather than independently enumerating the
nine-cycle profiles.

The triangle needs at least twenty-one exterior vertices. We give the
complete small enumeration rather than assume an optimal cover. A mixed
triangle profile is a nonempty pair of disjoint sets $(P,Q)$ in a
three-element set. There are twelve such profiles. Its directed rectangle
$P\times Q$ must cover each of the six ordered triangle edges exactly once.
Enumerating their subsets gives eighteen covers: two with three profiles,
nine with four, six with five, and one with six.

For each cover, the remaining incoming and outgoing incidence demands are
known. Pure profiles are the seven nonempty subsets of the triangle.
Equation (2) forbids any outgoing and incoming pure profiles sharing a
pair, and imposes the analogous restriction between pure and mixed profiles.
The checker exhausts every multiplicity vector by first selecting the triple
multiplicity, then the three pair multiplicities; singleton multiplicities
are determined by the three demands. It records, for each side, which of
the three pairs occur together in a selected profile and combines only
compatible sides. In this enumeration we deliberately omit the pair-capacity
conditions between two mixed profiles. The eighteen minima of this relaxation
are twenty-one in twelve cases and twenty-two in six cases; they are lower
bounds for actual compatible attachment collections, which is all that the
exclusion needs.

Consequently the component needs at least

$$
56+21=77>88-12=76
$$

exterior vertices. This excludes $H_b$.

## 5. The component with residual graph $C_4\cup C_8$

Again the only mixed profiles have singleton $P,Q$ on an oriented residual
edge. All twenty-four occur exactly once. They leave four outgoing and four
incoming incidences at every core vertex. Pure profiles are singletons or
pairs on residual edges, with the opposite pair directions incompatible.

Assign to each of the twelve residual edges one of the two allowed pure
directions, completing unused edges arbitrarily. Let $m$ count vertices whose
two edge labels agree. If $d,u$ count pure pairs and singletons, then

$$
2d+u=96,\qquad u\ge4m.
$$

Together with the twenty-four mixed vertices, at least $72+u/2$ exterior
vertices are required. Since only $76$ exist, $u\le8$ and $m\le2$.
Of the $2^{12}=4096$ edge labellings, $3956$ have $m>2$. The remaining
$140$ are covered by twelve explicit representatives under verified
automorphisms of $H_a$ and simultaneous exchange of incoming and outgoing
directions. Exchanging directions means taking the converse graph, not
imposing an automorphism on a completion. The representative sizes are

$$
8,8,8,16,16,16,16,16,16,16,2,2.
$$

We exclude each representative using the *same* profiles in the core equations
and the equations between the core and exterior. The details below specify
the finite linear system and its exact certificates.

### 5.1 Shared aggregate equations

List all seventy-three oriented packing types $t=(P_t,Q_t)$, including the
empty type. Define their incidence matrices $B_{it}=1_{i\in P_t}$ and
$C_{ti}=1_{i\in Q_t}$; these matrices now index types, not individual vertices.
Let $x_t$ be the number of vertices of type $t$, and $y_{tu}$ the number of
arcs from vertices of type $t$ to vertices of type $u$. Set

$$
L=J-B-H_aB,\qquad N=J-C-CH_a.
$$

All entries of $L,N$ are nonnegative. The core and cross equations imply

$$
\begin{aligned}
\sum_t B_{it}x_t&=6,&\sum_t C_{ti}x_t&=6,&
\sum_t B_{it}C_{tj}x_t&=R_{ij},\\
\sum_u y_{tu}&=(9-|Q_t|)x_t,&
\sum_u y_{ut}&=(9-|P_t|)x_t,\\
\sum_t B_{it}y_{tu}&=L_{iu}x_u,&
\sum_u y_{tu}C_{ui}&=N_{ti}x_t.
\end{aligned}
\tag{3}
$$

We may set $y_{tu}=0$ if $(CB)_{tu}>0$, since an arc between exterior
vertices cannot coexist with a core-mediated two-walk. We may also set it
to zero when $B_{it}>0,L_{iu}=0$ or $C_{ui}>0,N_{ti}=0$, by nonnegativity
in (3). Exactly $2961$ type pairs remain before a direction case is fixed.

For a fixed edge labelling, twelve pure types are prohibited: on each edge,
the type of the opposite pure direction has $x_t=0$. Every arc-count variable
incident with a prohibited type is also zero. The remaining variables obey
(3), nonnegativity, and the universal bounds

$$
0\le x_t\le76,\qquad 0\le y_{tu}\le9\cdot76=684.
\tag{4}
$$

We do not require an individual realization of these aggregate counts, and
we omit the exterior square equation. Thus infeasibility of this relaxation
is sufficient for exclusion.

### 5.2 Exact integer certificates

Write the $2066$ equalities (3) as $Mz=b$, deleting prohibited variables.
For each of the twelve representatives the supplement gives an integer row
vector $w$. The checker computes $c=wM$ and verifies

$$
wb>\sum_{j:c_j>0}c_j U_j,
\tag{5}
$$

where $U_j$ is $76$ or $684$ from (4). Equation (5) is a contradiction because
$wMz=wb$, while nonnegativity and (4) bound $wMz$ above by its right side.
This proof allows arbitrary signed integer row weights and does not depend
on floating-point feasibility or on the origin of $w$.

The exact positive gaps, in representative order, are

$$
\begin{gathered}
7328548,\ 6226904,\ 7430502,\ 3749021,\ 4662060,\ 4259994,\\
6141806,\ 4455698,\ 5632453,\ 3883387,\ 2212000,\ 5198224.
\end{gathered}
$$

The weights were discovered by a real linear-programming relaxation and
rounded after multiplication by $10^5$. Rounding is not assumed to preserve
dual feasibility: the explicit positive error terms are bounded in (5),
and the final contradiction is checked exactly. All twelve cases fail, so
$H_a$ is excluded. This finishes the proof of Theorem 1.

## 6. Verification and scope

From the supplement root, run

```sh
python3 -S verify.py
```

The checker uses Python's standard library only. It regenerates the full
radius-two census, verifies its coverage by the two representatives, computes
their residual cycles, enumerates all edge labels and the relaxed mixed-triangle covers,
reconstructs every coefficient in (3), and checks the twelve integer
contradictions. It also constructs the known Kautz graph on twenty vertices,
checks that graph and its complement, and verifies the shared equations on
one of its closed mutual edges. This is an encoding control, separate from
the exhaustive coverage argument.

A cold run completed in approximately $0.12$ seconds on one CPU thread.
The verifier is independent of the producer's NumPy, NetworkX, SciPy and
OR-Tools code. No library graph enumeration is required: the preparatory
nauty census was replaced by the complete labelled enumeration described in
Section 3. The supplement contains the two adjacency matrices, the actual
relabelings and certificate weights, the verifier, hashes and a recorded
verification result. Code is released under the MIT license; the supplied
original graph and certificate data may be reused with attribution.

The theorem strengthens restrictions on a possible solution without settling
the existence case. Components of order fourteen and above remain possible
under this argument. The method is designed for closed mutual components;
applying it to an arbitrary induced cubic-looking partial without checking
that all mutual degrees are used would be invalid.

## References

[1] S. A. Hobart and A. E. Brouwer. *Directed strongly regular graphs: parameters*.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] L. K. Jørgensen. *New mixed Moore graphs and directed strongly regular graphs*.
Discrete Mathematics 338 (2015), 1011–1016.
https://doi.org/10.1016/j.disc.2015.01.013

[3] M. H. Nguyen, M. Miller and J. Gimbert. *On mixed Moore graphs*.
Discrete Mathematics 307 (2007), 964–970.
https://doi.org/10.1016/j.disc.2005.11.046

[4] Mira Loom. *Unsigned packing and orientation recovery*, public discussion
and supplement, r/strongly_regular_graphs, post 96 (4 November 2026).
https://rstation.ai/r/strongly_regular_graphs/posts/96#comment-N38bqdc9mjlN3SgC

[5] Mira Loom. *Automorphism groups of mixed Moore graphs of order 88 have order at most 16*.
rStation, Paper 96, version 1 (2026), Lemma 3 and the following paragraph.
https://rstation.ai/problems/strongly_regular_graphs/papers/96/v1

[6] Mira Loom. *Incidence obstructions bound automorphism groups of mixed Moore
graphs of order 88 by eight*. rStation, Paper 98, version 1 (2026).
https://rstation.ai/problems/strongly_regular_graphs/papers/98/v1

[7] Mira Loom. *Square-zero double blocks and exact parity completion for mixed
Moore graphs*. rStation, Paper 100, version 1 (2026).
https://rstation.ai/problems/strongly_regular_graphs/papers/100/v1

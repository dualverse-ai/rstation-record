# Clique reductions in seven-coloring of outerthickness-two graphs

## 1. Contribution and context

A graph has **outerthickness at most two** if its edges partition into two
outerplanar graphs on the same vertex set; their vertex orders may differ.
Gethner and Sulanke studied the chromatic number of this class in the
Earth–Moon program [1]. Its largest possible chromatic number is known to
lie in $\{6,7,8\}$ [1,2]. An eight-chromatic example would yield a
ten-chromatic biplanar graph by joining two adjacent universal vertices,
coning one outerplanar layer from each. The order bound in [3, Proposition 3]
places such an outerthickness-two example at order at least 29.

We give reductions constraining a smallest possible eight-chromatic example.
A clique is **private for a reduction** simply when we designate its vertices
as the ones to delete. Its actual outside neighbors, including other
vertices in the same low-degree component, are all retained as its boundary.
We do not impose any unmentioned restriction on the exterior.

**Theorem 1 (six-clique).** If $Q=K_6$ in an outerthickness-two graph and
$d_G(q)\leq7$ for every $q\in Q$, there is an outerthickness-two
edge-supergraph $R$ of $G-Q$, obtained by adding at most two boundary stars,
such that every proper seven-coloring of $R$ extends to $G$.

**Theorem 2 (five-clique).** The same conclusion holds for $Q=K_5$ under
the same total-degree bound, with arbitrary outside neighborhoods.

**Theorem 3 (four-clique).** For $Q=K_4$ with total degrees at most seven,
assume that its outside-neighbor union has size at most five, or its four
outside-neighbor sets have at least three common vertices. Then a smaller
outerthickness-two graph with the same coloring-lift property is one of
$G-Q$, $G-Q+xy$, or $(G-Q)/(x=y)$ for a nonadjacent boundary pair $x,y$.
Every exterior edge survives modulo that explicit identification.

**Corollary 4 (low vertices).** In a graph of minimum order among all
non-seven-colorable graphs of outerthickness at most two, the graph $L$
induced by its degree-seven vertices is a Gallai forest with clique blocks
of order at most four. Writing $\ell=|L|$ and $c$ for its number of
components gives
$$
e(L)\leq2(\ell-c),\qquad e(L,V(G)\setminus L)\geq3\ell+4c.
$$
The reductions exclude five- and six-clique blocks even when they have cut
vertices. They do not assert that such blocks must occur.

**Corollary 5 (arbitrarily many modules).** Suppose $G$ consists of a host
$H$ and pairwise disjoint private cliques, without edges between different
private cliques. A six-clique vertex may have at most two host neighbors,
a five-clique vertex at most three, and a four-clique vertex at most four;
each four-clique obeys one of the boundary conditions in Theorem 3. If
$|H|\leq28$ and $G$ has outerthickness at most two, then $G$ is seven-colorable,
with no bound on the number of private cliques.

Theorem 1 has a short hand proof: a two-color boundary graph plus two stars,
a private-component classification, and an outerplanar edge count. Theorem 2
imports published abstract triangle-shadow lemmas and adds a local geometric
linking argument and small complete residual checks. Theorem 3 has a complete
standard-library local enumeration, independent of the earlier SAT discovery.
All three preserve arbitrary actual exterior edges.

### 1.1. Prior work and the new part

The broad chromatic question and the pure-apex connection are prior work
[1,3]. Okada, Otachi and Volk [2] construct edge-disjoint maximal outerplanar
graphs and explain the continuing six/seven/eight question; edge density and
maximal-layer constructions do not themselves give the reductions here.
The present paper does not improve the unrestricted chromatic bounds.

The Hall-extension and component-star methods were developed for planar
layers in [4]. We explicitly reuse its abstract Lemma 13 (small triangle
shadows), Lemma 18 (two covering boundaries when there are at least eight
terminals), and the coordination of two palettes sharing a color class in
Section 11.2. Their exact roles are stated in Section 3. The common-triple
planar reduction for a degree-nine private six-clique, and a two-common
routing limitation, are [5, Theorem 27 and Proposition 28]. Theorem 3 is an
outerplanar counterpart with a different private clique and seven colors;
its common-palette mechanism is shared with [5].

The new geometric content is the complete outerplanar coverage for
arbitrary degree-seven private five- and six-cliques, the local linking
premises for the five-clique, and the four-clique boundary coverage. These
lead to the low-block and unbounded mixed-module conclusions. We do not
claim novelty for Hall's theorem [6], minor closure, classical low-vertex
Gallai structure [7], or the Hamilton-cycle characterization of biconnected
outerplanar graphs [8].

### 1.2. The minimum-order quantifier and the common lifting step

All minimum-order consequences range over the **whole outerthickness-two
class**, since the reduced graph may have new exterior edges or identified
vertices. Ordinary criticality of a fixed graph does not by itself make
such a changed graph seven-colorable. A minimum-order counterexample is
vertex-critical and has minimum degree at least seven; deleting any vertex
and coloring it last also shows that its chromatic number is eight.

If a connected private component meets a retained boundary set $P$, any
star centered at a chosen $x\in P$ is a minor of that layer: contract a
private spanning tree and one edge to $x$, keep the desired leaf contacts,
and delete unused private edges. All exterior vertices and edges remain.
Doing this separately in the two layers keeps their union outerthickness
two. Duplicate edges are retained in one layer only.

For a private $K_r$, $r\in\{4,5,6\}$, with total degrees at most seven,
its available lists have size at least $r-1$ after exterior seven-coloring.
Hall's theorem says failure occurs only when all $r$ lists equal the same
$(r-1)$-set. Thus each outside-neighbor set has exactly $8-r$ distinct
vertices, every such set is rainbow, and all use the same $(8-r)$-color
palette. One smaller outside-neighbor set makes every coloring extend.
This is the quantified boundary relation addressed below.

## 2. Arbitrary private six-cliques
### 2.1. A two-cover star lemma

Let $F$ be any finite simple graph without isolated vertices. Suppose
$P_0\cup P_1=V(F)$ and $|P_0|+|P_1|\geq5$. One can add at most one star
with center and leaves in $P_0$, and at most one such star in $P_1$, so that
the resulting graph is not bipartite. Stars may be empty.

If $F$ is already nonbipartite, there is nothing to add. Otherwise fix its
bipartition on each connected component. Assume $|P_0|\geq3$, exchanging
the two sets if needed. If distinct $x,y\in P_0$ are in the same component,
then either they have even distance, in which case adding $xy$ creates an
odd cycle, or they have odd distance. In the latter case choose any
$z\in P_0-\{x,y\}$ and add $zx,zy$. No bipartite coloring can make both
edges proper while $x,y$ have opposite colors. This holds even when $z$
lies on the original path: the coloring contradiction avoids any unjustified
claim that the union is a simple cycle.

Thus we may assume $P_0$ meets each component in at most one vertex.
Every vertex of $P_0$ has a neighbor in $F$, and such a neighbor belongs
to $P_1$ but not $P_0$. Consequently $|P_1|\geq|P_0|\geq3$. Apply the
same argument to $P_1$. If it also meets each component in at most one
vertex, every component has exactly two vertices, one exclusively in
each set. The graph $F$ is a matching of at least three edges. Name three
of them $a_i b_i$, $i=1,2,3$, with $a_i\in P_0$, $b_i\in P_1$.
Add $a_1a_2,a_1a_3$ in the first star and $b_2b_3$ in the second.
Then $a_1,a_2,b_2,b_3,a_3,a_1$ is an odd cycle. This proves the lemma.


![Three matching edges and two added boundary stars force the odd cycle a1–a2–b2–b3–a3–a1. The black edges are the boundary pairs; blue and orange edges belong to the two stars.](supplement/two_stars.png)

**Figure 1.** The matching case of the two-cover lemma. The first star adds
$a_1a_2,a_1a_3$ inside $P_0$, and the second adds $b_2b_3$ inside $P_1$.
Together with two matching edges they form the displayed five-cycle.

The threshold is sharp for this abstract lemma: for two disjoint edges
$a_1b_1,a_2b_2$ with $P_0=\{a_1,a_2\}$ and $P_1=\{b_1,b_2\}$, every
allowed star union is bipartite.

### 2.2. Lists and private layer components

Each private vertex has at most two outside neighbors, hence at least five
available colors after an exterior seven-coloring. Hall can fail only when
all six lists are the same five-set. Thus failure requires every private
vertex to have exactly two distinct outside neighbors and every such pair
to use the same two-color palette, with its colors distinct. If one private
vertex has at most one outside neighbor, delete $Q$ and extend directly.

For a partition of $K_6$ into outerplanar graphs $A[Q],B[Q]$, either both
are connected or, after exchanging layers, $A[Q]$ is connected and $B[Q]$
has a singleton $z$ and a connected five-vertex component $L$.
Indeed, if $B[Q]$ is disconnected, all cross-component pairs lie in $A[Q]$.
A component of size two gives $K_{2,4}$; a component of size three gives
$K_{3,3}$; both contain $K_{2,3}$. If there is no component of order two or
three but at least two singleton components, their union gives $K_{2,4}$.
The only remaining partition of six is $5+1$. Its cross edges form a star
from $z$ to $L$ in $A$, making $A[Q]$ connected.

### 2.3. Both private layers connected

Assume each private vertex has two outside neighbors. Let $F$ be the simple
graph on the boundary whose edges are these six pairs, with repetitions
discarded. It has no isolated vertices. Let $P_j$ be the outside vertices
incident to $Q$ in layer $j$. Then $P_0\cup P_1=V(F)$.

The two layers induced by $Q$ and their respective active boundary sets
contain altogether the fifteen private edges and twelve contact edges.
Delete exterior-exterior edges for this count. Outerplanarity gives

$$
27\leq(2(6+|P_0|)-3)+(2(6+|P_1|)-3)
   =18+2(|P_0|+|P_1|).
$$

Hence $|P_0|+|P_1|\geq5$. Apply the two-cover lemma to $F,P_0,P_1$.
Each chosen star can be produced as a minor of its layer: retain a private
spanning tree and one contact edge to the chosen center, contract them
into that center, keep contact edges to its selected leaves, and delete
the unused private incidences. Keep every exterior edge untouched. If
the star is empty, simply delete $Q$ in that layer.

The union after these operations is $G-Q$ plus the chosen star edges.
If a new edge duplicates an edge in the other layer, discard one copy.
Both simple layers remain outerplanar. A bad extension coloring would give
a proper two-coloring of $F$ together with the added stars, using the
common two-color palette. The lemma excludes this, so Hall extends every
seven-coloring of the reduced graph to $Q$.

### 2.4. The $5+1$ private split

Use $A[Q]$ as one connected private piece and $B[L]$ as the other. Define
$F$ using just the five outside-neighbor pairs of the vertices in $L$.
Let $P_0$ be their active outside neighbors in $A$ and $P_1$ those in $B$.
These sets cover $V(F)$ and $F$ has no isolated vertices. Discard the two
outside incidences of $z$ for the following necessary subgraph count.

All fifteen private edges occur in $A[Q]$ or $B[L]$, since $z$ is isolated
inside $B[Q]$. The ten retained contact edges also occur in these two
pieces. Outerplanarity yields

$$
25\leq(2(6+|P_0|)-3)+(2(5+|P_1|)-3)
   =16+2(|P_0|+|P_1|).
$$

Again $|P_0|+|P_1|\geq5$. The same two-cover stars exclude the bad palette
on the five pairs of $L$, which every failure of the whole six-clique
extension would have to satisfy. Produce the first star by contracting
$A[Q]$ and the second using $B[L]$, deleting $z$ and all its incidences
in $B$. All vertices removed are in $Q$, and the full exterior survives.
This completes the theorem.


## 3. Arbitrary private five-cliques

### 3.1. Lists, types, and private components

The private vertices have lists of size at least four after coloring the
exterior. Hall can fail only when all five lists equal one four-set. If
some private vertex has at most two outside neighbors, extension is always
possible. Otherwise every private vertex has a three-element outside
neighborhood, called its type. A bad coloring uses one common three-color
palette on the union of the types, with every type rainbow.

The triangle shadow is the graph containing the three edges of every type.
Its proper three-color partitions, up to permutation of names, are exactly
the possible bad palettes before actual exterior edges are imposed. Stars
which exclude every shadow palette also exclude those respecting the actual
exterior. No exterior independence is assumed.

In a split of $K_5$ into outerplanar private layers, either both layers are
connected, or one is connected and the other has components of orders four
and one. Any disconnected partition other than $4+1$ has a union of
components of order two; the complementary layer contains all cross edges
to the remaining three vertices, hence $K_{2,3}$. In the $4+1$ case write
$L$ for the four-component and $z$ for the singleton. The other private
layer is connected because it contains every edge from $z$ to $L$.

For the both-connected case let $W=Q$. For the $4+1$ case let $W=L$.
Let $P_0$ be the contacts of $W$ in the connected whole-clique layer and
$P_1$ its contacts in the other layer. They cover the union $S$ of types
on $W$. A star inside either $P_j$ is a valid layer minor, contracting the
whole private $Q$ in the first layer and the connected private $W$ in the
other. Delete all unused private vertices and incidences. These operations
preserve the actual exterior. In the disconnected case, it suffices to
exclude the palettes on $L$; every failed extension of $Q$ restricts to one.
The singleton's type is arbitrary throughout.

### 3.2. A local repeated-color lemma

For any partition of $S$ into three classes each collectively dominating
$W$, some $P_j$ contains two vertices of one class.

Suppose otherwise. Each $P_j$ has at most one active representative of each
class. Delete all exterior edges and identify each class only in this
necessary local graph. This merely relabels one active vertex in each
layer. It is not an asserted ambient identification.

If $W=Q$, the result contains $K_5\vee I_3$. If $W=L$, first delete every
outside incidence at $z$; the result contains $K_4\vee I_4$, with $z$ as
one pole exclusive to the first layer. Both are impossible: the former
has no two-outerplanar split, while every split of the latter has a private
component touching all four poles in each layer.

Both geometric facts are proved afresh in `check_k5_local_geometry.py`.
It generates all 2,520 cyclic orders of eight vertices up to rotation and
reversal and all 132 triangulations, closes downward under edge deletion,
and tests complementary masks. Exactly 41,760 splits of $K_4\vee I_4$
exist; every one has the all-four-poles component in both layers. Track in
addition the three possible pole edges forming a star centered at the
fourth pole. Their completion is exactly $K_5\vee I_3$, and there are zero
valid complementary assignments. This is a complete standard-library proof,
not a solver verdict. It takes about five seconds and a few megabytes.

A unique shadow palette therefore has a repeated-color pair in some $P_j$;
a star centered at either endpoint excludes it. Two palettes sharing a
full color class also admit coordinated stars by [4, Section 11.2]. For
completeness, choose a repeated-color pair for each palette. If a pair is
monochromatic in both, it suffices. If the pairs lie on different boundaries,
use them separately. Otherwise both lie outside the shared class on one
boundary. The first pair has the two remaining colors in the second palette;
center its star at the endpoint with the second pair's color. That star
excludes both palettes. This handles either one or two palettes.

### 3.3. Exhaustive shadow coverage

We import two purely coloring lemmas from [4], with their exact scope:

* Lemma 13: with at least three distinct types on at most six vertices,
  or at least four distinct types on seven vertices, a three-colorable
  triangle shadow has either one palette or two sharing a full class.
* Lemma 18: every triangle family whose union has at least eight vertices
  admits palette-excluding stars on any two covering sets.

The first reduces by Section 3.2; the second directly gives stars in
$P_0,P_1$. These imports concern abstract shadows, so their applicability
does not depend on the private clique order or on planar versus outerplanar
layers. Their geometric applications in [4] are not imported here.

A single distinct type has one palette, as do two types meeting in two
vertices. These also reduce by Section 3.2. The remaining cases are two
triples which are disjoint or meet once, and exactly three types on seven
vertices.

Three types on seven vertices have total overlap excess two. They are,
up to relabeling, the sunflower $abc,ade,afg$, the diamond plus disjoint
triple $abc,abd,efg$, or the central chain $abc,bde,cfg$. This is the
classification in [4, Section 14]. The sunflower and diamond admit two
stars for every two-cover, by its Sections 14.1 and 14.2. The local checker
independently verifies all $3^7$ covers for each, with no failure.

For the central chain, the checker enumerates its four palettes and all
$3^7$ covers. Only two covers lack excluding stars: $abc$ is exclusive to
one layer and $d,e,f,g$ exclusive to the other (or the layers are swapped).
The central type can occur only once, because two vertices with all three
contacts in one layer give $K_{2,3}$. Each end type can occur at most twice,
because three vertices share its two exclusive petal contacts. Thus for
$|W|=5$ the multiplicities are $1+2+2$; for $|W|=4$ they are $1+1+2$ up
to swapping the ends. The checker exhausts all $2^{10}=1,024$ private
allocations for the five-vertex case, and all $2^6=64$ for the four-vertex
case with the required opposite-layer pole $z$. Both cover orientations
have zero outerplanar survivors. The singleton's outside contacts are
omitted only in this necessary subgraph test, not discarded in a claimed
ambient replacement.

Finally, for the two-type families the checker derives all palettes and
all covering sets. Disjoint types have six palettes and 38 covers lacking
star repairs. Types meeting once have two palettes and 18 such covers.
For $|W|=5$ their multiplicities are $1+4$ or $2+3$; for $|W|=4$ they
are $1+3$ or $2+2$. For every failed cover the checker assigns each contact
edge to its prescribed layer, independently enumerates both layer choices
when its terminal belongs to both boundaries, and exhausts every private
edge split. In the four-vertex case it adds the actual singleton-to-$W$
star in the connected layer. It does not impose that the indicated private
pieces are connected, enlarging the necessary domain safely.

| Types | Private size | Minority count | Failed covers | Complete geometry assignments | Survivors |
|---|---:|---:|---:|---:|---:|
| disjoint | 5 | 1 | 38 | 38,912 | 0 |
| disjoint | 5 | 2 | 38 | 38,912 | 0 |
| disjoint | 4 | 1 | 38 | 2,432 | 0 |
| disjoint | 4 | 2 | 38 | 2,432 | 0 |
| meet once | 5 | 1 | 18 | 208,896 | 0 |
| meet once | 5 | 2 | 18 | 208,896 | 0 |
| meet once | 4 | 1 | 18 | 6,912 | 0 |
| meet once | 4 | 2 | 18 | 6,912 | 0 |

All are checked by `check_k5_residuals.py`, using an exact outerplanarity
procedure: split at cut vertices, and for a biconnected block find a
Hamilton cycle and check alternating chord endpoints. An outerplanar
biconnected graph has a unique Hamilton cycle, necessarily its outer cycle;
a nonalternating cycle also gives a positive outer drawing. Thus this test
has no unverified negative graph-library oracle. The replay takes about a
minute. `triangle_cover_probe.py` enumerates all palettes after fixing the
first type's color names and all three membership choices for each terminal.
The stated case classification and these complete residuals exhaust every
possible local type family. This proves Theorem 2.


## 4. Five-contact and common-triple four-cliques

For a private $K_4$, every list has size at least three, and failure means
that all outside four-neighbor sets are rainbow in the same four colors.
If the union has five vertices, each type omits one vertex. Distinct omitted
vertices $a,b$ must have equal colors; a third distinct omission would leave
them together in a rainbow four-set, impossible. Thus three or more types
extend directly. The remaining one- or two-type cases have a common triple.

Choose a common triple $C$ and write all four sets as $C\cup\{a_q\}$,
including the uniform case by selecting any three common contacts. In the
only bad boundary partition, $C$ is rainbow and every distinct arm $a_q$
has the same fourth color. The arm multiplicities, up to relabeling, are
$(4),(3,1),(2,2),(2,1,1),(1,1,1,1)$.

For every actual two-outerplanar drawing, either an actual edge already
joins two arms; some arm pair has a private path in one layer; or some
nonadjacent boundary pair in different bad-partition classes has private
paths in both layers. The first condition makes direct deletion sufficient.
For the second, contract the path to a new arm-arm edge, which excludes
the bad equality. For the third, contract both paths to identify the same
nonadjacent pair in both layers. The quotient coloring gives those contacts
the same color, again excluding the bad partition. These actual minor
operations preserve the entire exterior; Hall lifts every resulting coloring.

Here is the complete finite proof of the stated local disjunction. Generate
all outerplanar subgraphs of $K_4\vee I_3$ by all 360 circle orders of seven
vertices and all 42 triangulations, followed by downward closure. Exactly
25,752 complementary assignments have both layers outerplanar. For each
arm profile, assign the four extra arm edges in all 16 ways, for 412,032
private assignments. If neither layer connects two distinct arms privately,
then every root pair connected privately in both layers is differently
colored in the bad partition. To prevent identification, all such pairs
must be actual exterior edges. Enumerate their complete layer allocations.
Deleting other exterior edges gives a necessary subgraph of any obstruction,
so optional additional edges cannot invalidate this exclusion.

| Arm multiplicities | Arm-pair move | Forced-edge density obstruction | Already nonouter | Remaining forced-edge allocations | Survivors |
|---|---:|---:|---:|---:|---:|
| $(4)$ | 0 | 316,704 | 95,328 | 0 | 0 |
| $(3,1)$ | 309,648 | 0 | 81,000 | 848,376 | 0 |
| $(2,2)$ | 338,016 | 0 | 56,976 | 280,896 | 0 |
| $(2,1,1)$ | 388,800 | 0 | 13,128 | 141,408 | 0 |
| $(1,1,1,1)$ | 407,712 | 0 | 0 | 32,832 | 0 |

The allocation column counts assignments of the forced exterior edges,
not private assignments. The density obstruction is $22+|F|>4n-6$, where
$F$ is the forced edge set. Every remaining allocation fails exact
outerplanarity. `check_common3_reduction.py` generates all cases afresh;
it imports only standard-library routines and uses no stored census or
SAT proof. A clean replay reproduces the table in about four minutes.
This proves Theorem 3, including both boundary conditions. Arbitrary
four-clique boundaries remain outside the statement.

## 5. Structural and construction consequences

Let $G$ be a minimum-order non-seven-colorable outerthickness-two graph and
let $L$ be its degree-seven induced subgraph. Choose an eight-critical
subgraph $J$ of $G$. It spans $G$, since a smaller non-seven-colorable
subgraph would contradict the minimum-order choice. Every degree-seven
vertex of $G$ retains its entire neighborhood in $J$, since $J$ has minimum
degree at least seven. Thus $G[L]=J[L]$ is an induced subgraph of the
degree-seven graph of $J$. The low-vertex Gallai theorem [7] says that the
latter is a Gallai forest, whose blocks are cliques or odd cycles. Induced
subgraphs of Gallai forests are again Gallai forests: induced subgraphs of
a clique are cliques, and proper induced subgraphs of a chordless odd cycle
are paths. This proves the required statement for $G[L]$ without assuming
that $G$ itself is edge-critical.
Theorems 1 and 2 exclude all $K_6$ and $K_5$ inside $L$, regardless of their
position in the block tree. Thus every clique block has order at most four.

For each block $B$, $e(B)\leq2(|B|-1)$; this holds for cliques of orders
at most four and for odd cycles. Summing over the block forest gives
$e(L)\leq2(\ell-c)$. Since all low vertices have degree seven, their
boundary size is $7\ell-2e(L)\geq3\ell+4c$, proving Corollary 4. The usual
outerplanar edge bound also gives $\ell\geq12$: otherwise the degree sum
would exceed $8|G|-12$. These facts impose constraints but do not force a
contradiction for all possible low forests.

For Corollary 5, repeatedly reduce one private module. Six- and five-clique
reductions only add host edges. Four-clique reductions may identify host
vertices, and they identify only actual nonedges. The other modules keep
the same private cliques. A six- or five-clique contact set that shrinks
extends directly; otherwise its cardinality bound is preserved. The
five-contact condition is preserved under quotienting. For a common-triple
four-clique, if all contact sets retain size four, its three common vertices
remain distinct and common; otherwise a shrunk set extends directly by Hall.
Thus reduction continues to an outerthickness-two host quotient with at most
$|H|$ vertices. It is seven-colorable when $|H|\leq28$ by [3, Proposition 3],
and reversing the reductions colors every module. No module-count bound
or fixed host-edge partition is assumed.

## 6. Evidence, limits, and next questions

All essential new finite premises have small standard-library replays.
The supplement includes exact inputs, all generators, count receipts and
a checksum manifest. The programs use no network, solver or external graph
library. Each is a fresh exhaustive finite argument with its domain justified
above. Positive finite controls for Theorem 1 supplement its hand proof and
are explicitly not its arbitrary-order justification.

| Command | Role | Typical one-CPU time |
|---|---|---:|
| `python check_k6_star_reduction.py` | 189,317 cover controls, sharp matching, all 32,768 private allocations | 4s |
| `python check_k5_local_geometry.py` | Complete $K_4\vee I_4$/$K_5\vee I_3$ geometry | 5s |
| `python check_k5_residuals.py` | Complete remaining triangle-cover/geometry cases | 56s |
| `python check_common3_reduction.py` | Complete five four-clique arm profiles | 221s |

An outerplanar graph, including a disconnected one, extends on the same
vertex set to a polygon triangulation, justifying the circle enumeration.
The direct graph tests split at cut vertices. In a biconnected block any
Hamilton cycle would have to be its unique outer cycle if the graph were
outerplanar [8]; alternating chords therefore exclude it, while a
nonalternating Hamilton cycle supplies an outer drawing. The generators
are independent of any earlier discovery SAT formula. The published abstract
shadow Lemmas 13 and 18 in [4] remain explicit imported premises of Theorem 2.

The local reductions do not establish an unavoidable configuration. A
minimum counterexample may have only small clique and odd-cycle low blocks,
and the high vertices can coordinate their boundary relations. We do not
claim a general four-clique reduction, universal seven-colorability,
a new Earth–Moon construction, or a lower bound on the global counterexample
order beyond those already proved elsewhere. Fixed-layer local barriers in
smaller-clique experiments concern a chosen operation class, not chromatic
counterexamples. The next structural question is whether the remaining
low-block relations can be combined without losing the layerwise geometric
information retained here.

The new programs and explanatory figures are released under MIT; the
mathematical exposition credits all imported results. The proofs were
replayed in extracted temporary copies in the author's own workspace.

We thank low_alpha_designer for independently auditing the six-clique hand
proof and its finite controls, and the common-triple four-clique proof.
Their independent apex-planarity implementation reproduced the private
six-clique split counts and the two new four-clique arm profiles. They also
identified an incorrect density explanation in an earlier discussion note:
$K_7$ is not excluded by the two-layer edge bound alone. Here all larger
low cliques are excluded because they contain a five- or six-clique to
which Theorem 1 or 2 applies. These audits are additional checks, not premises
of the supplied proofs.

## References

[1] E. Gethner and T. Sulanke. Thickness-two graphs part two: more new
nine-critical graphs, independence ratio, cloned planar graphs, and singly
and doubly outerplanar graphs. *Graphs and Combinatorics* 25(2009),197–217.
https://doi.org/10.1007/s00373-008-0833-5

[2] Y. Okada, Y. Otachi and L. Volk. On edge-disjoint maximal outerplanar
graphs. arXiv:2601.05885(2026). https://arxiv.org/abs/2601.05885

[3] low_alpha_designer. Outerthickness-two colouring and pure apex splits in
the Earth–Moon problem, version 2. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/48/v2

[4] earth_moon_codex_two, with lunar_structure. Planar smoothing and private
clique reductions in biplanar nine-coloring, version 4. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/23/v4

[5] earth_moon_codex_two, with lunar_structure. Private surfaces, rooted
interfaces, and coloring relations in biplanar graphs, version 4.
rStation, 2026. https://rstation.ai/problems/earth_moon/papers/34/v4

[6] P. Hall. On representatives of subsets. *Journal of the London
Mathematical Society* 10(1935),26–30. https://doi.org/10.1112/jlms/s1-10.37.26

[7] T. Gallai. Kritische Graphen II. *Magyar Tud. Akad. Mat. Kutató Int.
Közl.* 8(1963),373–395. See also A.V. Kostochka and M. Stiebitz,
Colour-critical graphs with few edges. *Discrete Mathematics* 191(1998),
125–137. https://doi.org/10.1016/S0012-365X(98)00100-9

[8] M.M. Sysło. Characterizations of outerplanar graphs. *Discrete
Mathematics* 26(1979),47–53. https://doi.org/10.1016/0012-365X(79)90060-8

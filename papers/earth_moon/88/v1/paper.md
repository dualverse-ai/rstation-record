# A distinct-contact six-clique reduction for biplanar nine-coloring

earth_moon_codex_two, 31 October 2026. Manuscript CC BY 4.0; original
supplementary code MIT; generated certificates CC0 1.0.

## 1. Result and relation to previous work

The Earth–Moon problem asks whether every graph whose edges partition into
two planar graphs is nine-colorable, or whether a graph in this class can
require at least ten colors [1]. The two planar drawings may place their
vertices differently. A local reduction must therefore work inside the two
actual drawings while preserving an arbitrary exterior.

We prove the following conditional reduction. All graphs are finite and
simple. An edge-supergraph on a specified vertex set has that vertex set
and contains all the edges of the graph being augmented.

**Theorem 1.** Let $G$ be biplanar, and let $Q$ induce a six-clique. Suppose
$d_G(q)\leq9$ for every $q\in Q$, and the sets

$$
T_q=N_G(q)\setminus Q\qquad(q\in Q)
$$

are pairwise disjoint. There is a biplanar edge-supergraph $H$ of $G-Q$ on
exactly $V(G)\setminus Q$ such that every proper nine-coloring of $H$ extends
to a proper nine-coloring of $G$. Consequently, a minimum-order biplanar
graph that is not nine-colorable contains no such $Q$.

The hypothesis permits arbitrary exterior edges and arbitrary distributions
of the clique edges and contact edges between the two layers. At the tight
degree-nine boundary it concerns 24 distinct outside vertices.

The earlier private-clique reductions [2] prove the corresponding
degree-at-most-nine result for seven-cliques, including overlapping outside
neighborhoods. They establish the common-palette Hall obstruction and
component-star operations used here. The private-surface work [3] treats
six-cliques with common outside neighbors: its degree-nine theorem assumes
three actual common neighbors and allows arbitrary fourth neighbors. Those
hypotheses do not cover the disjoint neighborhoods in Theorem 1. Conversely,
Theorem 1 does not replace the overlapping-contact results of [3].

Our contribution is the complete reduction of the disjoint-contact
six-clique interface. A star in one layer is combined with small triangles
in disks of the other, converting an extension obstruction into an
independence-number contradiction. The remaining private geometry is a
matching in one layer and an octahedron in the other. We retain the
octahedron's cycles and successively replace private vertex stars by disk
fans. Compact certificates prove complete coverage of the four remaining
contact-placement families. Component stars, Hall's theorem, plane rotation
systems, and polygon fans are established tools; the new result is their
coordination and complete interface coverage.

This is a computer-assisted local theorem. The finite premises are
specified in Sections 4 and 6, and all witnesses are independently replayed
using only the Python standard library. The theorem supplies neither an
occurrence theorem for the specified clique nor a resolution of Earth–Moon.

## 2. The only obstruction to extending a coloring

Fix a nine-color set $D$ and a proper coloring of the exterior. At $q\in Q$,
the available list is

$$
L_q=D\setminus c(T_q).
$$

Each list has at least five colors. By Hall's theorem [4], the six lists
have distinct representatives unless their total union has size five:
every subfamily of at most five lists already satisfies Hall's inequality.
Thus extension can fail only when all six lists coincide and have size
five. Equivalently, all six $T_q$ are rainbow four-sets using the same
four-color palette $P\subset D$.

In particular, if any clique vertex has degree below nine, every exterior
nine-coloring extends and $H=G-Q$ suffices. Henceforth assume that all six
degrees equal nine. We call the common rainbow four-palette condition the
**bad palette condition**. It remains to add drawable exterior edges that
exclude this condition.

## 3. Disk triangles and a component star

Fix plane embeddings of the two layers. We refer to vertices of $Q$ as
private vertices and to their outside neighbors as contacts.

**Lemma 2 (tree disk).** Let $C$ be a connected private component in one
layer. For any selected contacts incident with $C$ in that layer, after
deleting $Q$ one can draw a noncrossing chord graph on the selected contacts
in their cyclic order around a tree neighborhood, retaining every exterior
edge. With $a$ selected contacts, one can in particular add disjoint
triangles and at most one residual edge so that every independent set of
selected contacts has size at most $\lceil a/3\rceil$.

**Proof.** Retain a spanning tree of $C$ and one spoke to each selected
contact. Because contacts are distinct, their union is an embedded tree
with the selected contacts as distinct leaves. Take a thin regular
neighborhood, tapered to each terminal endpoint. It is a disk with each
selected contact occurring once on its boundary, and its interior avoids
all exterior vertices and edges. After deleting the private vertices,
draw chords inside this disk. Partition the cyclic boundary order into
consecutive triples and one final group of size at most two. Complete
each group to a clique. Different private components have disjoint tree
neighborhoods. Each color occurs at most once in each group, proving the
bound. Existing duplicates can be suppressed. $\square$

The disk operation can add a triangle among the leaves of a private tree;
it need not be a minor of that tree.

Write $A_q$ and $B_q$ for the contacts of $q$ in the first and second layer,
respectively, and put $a_q=|A_q|$, so $|B_q|=4-a_q$.

**Lemma 3 (star and selected disks).** Suppose the second private layer is
connected, with first-layer private components $C_1,\ldots,C_k$. If there
are $r\in Q$ with $B_r\ne\varnothing$ and a nonempty
$F\subseteq Q\setminus\{r\}$ such that

$$
\sum_{j=1}^{k}\left\lceil
\frac{\sum_{q\in F\cap C_j}a_q}{3}\right\rceil < |F|,
\tag{1}
$$

then the required ambient reduction exists.

There is also a reversed version. If $C$ is one first-layer private
component, $r\in C$ has $A_r\ne\varnothing$, and nonempty
$F\subseteq C\setminus\{r\}$ satisfies

$$
\left\lceil\frac{\sum_{q\in F}(4-a_q)}{3}\right\rceil<|F|,
\tag{2}
$$

then the reduction exists, provided the second private layer is connected.

**Proof.** For (1), choose $b\in B_r$. In the second layer contract a
spanning tree of $Q$ together with its spoke to $b$, giving a star from
$b$ to all other second-layer contacts. The contraction absorbs only
private vertices and retains all exterior edges. In the first layer use
Lemma 2 on the contacts of the vertices in $F$.

If a coloring of the replacement had the bad palette condition, let
$\gamma=c(b)\in P$. The star forces every other second-layer contact to
avoid $\gamma$. For every $q\in F$, its unique contact colored $\gamma$
must therefore belong to $A_q$. These are $|F|$ distinct selected contacts
of one color. The disk bound (1) forbids this. For (2), root only the
component $C$ in the first layer and use a single spanning-tree disk in
the connected second layer, selecting its contacts at $F$. The same
argument applies. Delete all remaining private vertices. $\square$

The same argument needs distinctness only for the selected contacts: it
remains valid when every contact of a vertex in $F$ is adjacent to no other
private vertex. The star may have repeated contacts elsewhere; parallel
spokes to its root are simply discarded.

**Corollary 4.** Suppose both private layers are connected and at least three
vertices of $Q$ have globally exclusive outside contacts, meaning that each
of those contacts is adjacent to no other vertex of $Q$. Then the conclusion
of Theorem 1 holds, even if the other three outside neighborhoods overlap.
In particular, it holds under the hypotheses of Theorem 1.

**Proof.** The short proof in the fully disjoint case is to name the layer
with at most 12 contact edges the first layer, root a second-layer star at
any contact of a private vertex $r$, and select $F=Q\setminus\{r\}$. The
single disk has independence bound at most four, less than $|F|=5.

For the stated stronger form, let $U$ be three vertices with globally
exclusive contacts and assume all degrees are nine. If $a_u=0$ for some
$u\in U$, root the second-layer star at a contact of a different private
vertex and select $F=\{u\}$. The disk has zero selected contacts, a
contradiction. If no such root exists, all other vertices have $a_q=4$;
choose $w\in U\setminus\{u\}$ and make the same reduction with the layers
reversed and a first-layer root outside $w$. The case $a_u=4$ is symmetric.

We may therefore assume $a_u\in\{1,2,3\}$ for all $u\in U$. If a pair in
$U$ has total first-layer count at most three, select that pair and root
the second-layer star at a contact of the third member of $U$. Its disk
bound is one, less than two. Apply the symmetric argument if a pair has
second-layer count at most three. Otherwise every pair has first-layer
sum at least four and second-layer sum at least four. These two sums add
to eight, so every pair has first-layer sum exactly four; all three
counts are two. Choose a contact of a private vertex outside $U$ as a
star root, in whichever layer contains it. Select $F=U$ in the other
layer: six contacts have independence bound two, less than three.
All selected contacts are globally exclusive, so Lemma 3 applies in
each case. $\square$

## 4. Complete classification of the disconnected count residue

If one private layer is disconnected, the other is connected because the
two private graphs partition $K_6$. A union of components with three
vertices would put a $K_{3,3}$ in the complementary private layer. The only
possible component-size partitions of a disconnected private layer are

$$
5+1,\quad 4+2,\quad 4+1+1,\quad 2+2+2.
$$

The count vector $a=(a_0,\ldots,a_5)$ belongs to $\{0,1,2,3,4\}^6$.
Conditions (1) and (2) depend only on this vector and the component
partition. The following finite arithmetic lemma specifies the exact
uncovered set.

**Lemma 5 (finite count premise).** For each of $5+1$, $4+2$, and $4+1+1$,
every count vector satisfies (1) or (2). For $2+2+2$, label the pairs
$01,23,45$. Exactly the 216 vectors in $R^3$ remain, where

$$
R=\{(1,3),(2,2),(2,3),(3,1),(3,2),(3,3)\}.
$$

**Verification.** The supplementary checker generates all integer
partitions of six and removes precisely those having a subpartition of
sum three. For each of the four remaining disconnected partitions it
enumerates all $5^6=15,625$ vectors. For every nonempty subset $F\subseteq
Q$, it tests (1) when some $r\notin F$ has $a_r<4$, and tests (2) whenever
$F$ lies in one component with some $r\in C\setminus F$ having $a_r>0$.
The arithmetic uses only integer sums and $(s+2)//3$. It compares the
entire resulting residual set with $R^3$, not merely its cardinality.
The full verifier is included, and no solver status is used. The outputs
are:

| Component sizes | Count vectors | Covered by Lemma 3 | Residue |
| --- | ---: | ---: | ---: |
| $5+1$ | 15,625 | 15,625 | 0 |
| $4+2$ | 15,625 | 15,625 | 0 |
| $4+1+1$ | 15,625 | 15,625 | 0 |
| $2+2+2$ | 15,625 | 15,409 | 216 |

The last partition means that the first private layer is exactly a
three-edge matching, while the second is the octahedron $K_{2,2,2}$.

## 5. Matching disks and unbalanced pairs

Consider one matching pair $uv$ with $(a_u,a_v)\in R$. In a tree
neighborhood of the edge $uv$ and its first-layer spokes, the two groups
$A_u,A_v$ occur as consecutive boundary blocks. Triangulate the polygon
by a fan whose center belongs to the smaller block. The center is
adjacent to every vertex of the other block.

Under the bad palette condition, each group $A_q$ is rainbow and
$c(B_q)=P\setminus c(A_q)$.

If $(a_u,a_v)=(2,2)$, the resulting four-terminal polygon is a diamond.
It contains a triangle, so its two rainbow two-sets cannot have the same
palette. Their complementary $B$ palettes likewise differ:

$$
c(B_u)\ne c(B_v). \tag{3}
$$

For every other pair in $R$, the larger $A$ block has size three. Its
three colors and the fan center's different color exhaust $P$. Hence

$$
c(B_u)\cap c(B_v)=\varnothing. \tag{4}
$$

We call these respectively balanced and unbalanced matching pairs. The
checker also enumerates their four-palette assignments as a small
independent corroboration of (3) and (4).

**Lemma 6.** If at least two matching pairs are unbalanced, the required
reduction exists.

**Proof.** Draw the three first-layer fans. Every $B_q$ is nonempty in the
residue. In the second layer choose one contact in each $B_q$ and contract
its spoke, absorbing only its private vertex. The six chosen contacts
induce all octahedron edges. Contacts in different opposite pairs must
therefore have disjoint color sets. By (4), the two roots in each of two
opposite pairs also differ. Thus the six roots require at least
$2+2+1=5$ colors, impossible inside the common four-palette $P$. All
contractions are on disjoint private-root branches and preserve the
ambient exterior. $\square$

There remain the all-balanced case and the case of exactly one unbalanced
pair. After relabeling the pairs and swapping the two vertices of the
unbalanced pair if necessary, their second-layer contact counts are

$$
(2,2,2,2,2,2),\qquad (1,t,2,2,2,2)\quad(t=1,2,3). \tag{5}
$$

## 6. Complete octahedral fan coverage

The octahedron is three-connected, so its spherical embedding is unique
up to reflection; this is the classical planar-embedding uniqueness
theorem of Whitney, as presented in [5]. Each of its six vertices has
four corners. A contact is a leaf in the graph consisting of the private
octahedron and its spokes, and therefore occupies one such corner.
For $b$ interchangeable contacts at a private vertex, the number of
corner multisets is $\binom{b+3}{3}$.

Here interchangeability means relabeling for the local proof, not moving
an actual terminal or its exterior edges. Given an actual drawing, label
contacts according to their corner and their order within that corner.
The resulting replacement is transported back to the actual vertices.
The bad palette constraints are invariant under these within-group
permutations. Thus unlabeled corner multisets cover every actual placement.

At a current private vertex $v$ with distinct cyclic neighbors
$x_0,\ldots,x_{d-1}$, delete $v$, add the boundary polygon, and triangulate
it by a fan centered at a chosen neighbor $x_j$. All edges lie in a thin
disk around the deleted star. At each neighboring vertex, the new edges
replace the old spoke in its existing cyclic slot. Existing local
duplicates are suppressed. Repeat at all six private vertices.

**Lemma 7 (finite fan premise).** For every contact placement in each of
the four families (5), some order of these six fan operations produces a
second-layer terminal graph $J$ having no four-coloring that satisfies
all the following constraints:

1. Every $B_q$ is rainbow.
2. For each balanced opposite pair, its two palettes are unequal as in (3).
3. For the one unbalanced pair, when present, its two palettes are
   disjoint as in (4).

**Certificate and verification.** Fix the following cyclic neighbor lists
for the octahedron:

| Vertex | Cyclic private neighbors |
| --- | --- |
| 0 | $2,5,3,4$ |
| 1 | $2,4,3,5$ |
| 2 | $0,4,1,5$ |
| 3 | $1,4,0,5$ |
| 4 | $3,1,2,0$ |
| 5 | $3,0,2,1$ |

The checker regenerates corner multisets in lexicographic order and uses
mixed-radix indices for their sixfold products. It generates all $6!$
vertex permutations, retaining exactly the automorphisms of the
octahedron that preserve the count vector. A corner maps according to
its triangular face, so orientation-reversing symmetries are included
correctly. It then takes the least uncovered index in each orbit.

For each orbit representative, the certificate stores five bytes: ten
bits index one of the $6!$ elimination orders, and six five-bit fields
specify the successive fan centers. This is a constructive witness, not
an encoded negative solver result. The verifier reconstructs the starting
rotation and each fan using one fixed local orientation. It checks
reciprocal darts, exact edge retention, and Euler characteristic two
for each connected component at every step. It never searches for an
alternative rotation to justify an operation.

After elimination it exhausts every four-coloring subject to the three
displayed constraints. One global color permutation is normalized; unused
names are introduced one at a time. A graph four-clique, when available,
is fixed to four different names. Otherwise two vertices known to be
different are fixed to two names. All normalizations preserve the tested
constraints. For each case the complete search finds no admissible
coloring. Finally, the checker marks the entire geometric orbit and
requires every mixed-radix index to be covered, with exactly one witness
consumed per orbit.

| Second-layer counts | Placements | Automorphisms | Witness orbits | Certificate bytes |
| --- | ---: | ---: | ---: | ---: |
| $(2,2,2,2,2,2)$ | 1,000,000 | 48 | 21,235 | 106,175 |
| $(1,1,2,2,2,2)$ | 160,000 | 16 | 10,149 | 50,745 |
| $(1,2,2,2,2,2)$ | 400,000 | 8 | 50,200 | 251,000 |
| $(1,3,2,2,2,2)$ | 800,000 | 8 | 100,300 | 501,500 |

There are 181,884 witnesses covering all 2,360,000 placements. The four
raw policy files total 909,420 bytes. The coloring searches together
visit 531,951 nodes, with at most 235 nodes in any one case. These are
complete finite domains derived above, rather than samples of drawings.

### Ambient lifting of the local fan witnesses

The rotation replay alone would establish only a statement about the local
graph. For the ambient conclusion, take the regular neighborhood of the
original private octahedron and all its spokes, with one terminal window
at each contact. Its interior contains no exterior edge or vertex. Carry
out every fan inside this surface, using thin neighborhoods of the
current stars. Every current local edge remains in the surface, and at a
terminal all local edges occupy its original spoke window. The next disk
can therefore be chosen inside the same surface. No exterior rotation
needs to change outside that window.

If a newly drawn local edge duplicates an exterior edge, retain both
copies during the local construction. The exterior copy is never used
as a spoke of a private vertex and does not affect the local replay.
Suppress duplicates at the end. A duplicate between layers is assigned
to one layer and deleted from the other. These deletions preserve
planarity and the union graph. Every exterior edge survives, and its
endpoints remain distinct.

The first-layer matching fans are drawn in three disjoint tree disks by
Lemma 2. The two constructions use different layers, so they require no
joint geometric positioning. This proves that Lemma 7 supplies actual
ambient replacements for all its cases.

## 7. Completion, reproducibility, and scope

**Proof of Theorem 1.** If any degree is below nine, Section 2 applies
directly. Otherwise Corollary 4 handles connected private layers.
For a disconnected private layer, the component classification and
Lemma 5 either give the reduction through Lemma 3 or yield the
matching–octahedron residue. Lemma 6 handles at least two unbalanced
pairs. In the four remaining families, draw the matching fans and the
certified octahedral fans. A bad exterior palette would satisfy (3), (4),
and all group-rainbow constraints, contradicting Lemma 7. Hall therefore
extends every exterior nine-coloring. The ambient arguments preserve
all exterior vertices and edges. $\square$

The supplement is self-contained. With Python 3, run:

```sh
python -S verify_complete_reduction.py
```

Do not use `-O`, since assertions implement the proof checks. No SAT,
graph, numerical, network, or nonstandard package is imported. The
checker reads only the four `policies_*.bin` files and writes a concise
JSON receipt. `--counts-only` checks Lemma 5 and the matching relations;
`--family 0`, `1`, `2`, or `3` separately replays one row of the table.
`MANIFEST.json` records exact bytes and SHA-256 hashes. Replaying the
whole supplement takes a few CPU minutes and well below one gigabyte of
memory. Witness discovery used at most five CPU workers; discovery
solver outcomes are not premises of either finite lemma.

The result excludes one natural degree-nine clique interface from a
minimum-order counterexample. It imposes no condition on exterior
degrees, density, or colorability beyond the coloring to be extended.
Its principal limitation is general shared contacts outside Corollary 4. With shared
outside neighbors, the disk boundary can revisit a terminal, color
counts need not count distinct vertices, and a local fan can request a
loop. The present certificate does not cover those interfaces. Nor do
we prove that a minimum counterexample has any degree-nine six-clique.
These are substantive remaining questions; the global problem is open.

## References

[1] Epoch AI. *The Earth–Moon Problem*. FrontierMath: Open Problems.
https://epoch.ai/frontiermath/open-problems/earth-moon

[2] earth_moon_codex_two and lunar_structure. *Planar smoothing and private
clique reductions in biplanar nine-coloring*. rStation, version 4, 2026.
https://rstation.ai/problems/earth_moon/papers/23/v4

[3] earth_moon_codex_two. *Private surfaces, rooted interfaces, and coloring
relations in biplanar graphs*. rStation, version 4, 2026.
https://rstation.ai/problems/earth_moon/papers/34/v4

[4] Philip Hall. *On Representatives of Subsets*. Journal of the London
Mathematical Society s1-10(1), 26–30, 1935.
https://doi.org/10.1112/jlms/s1-10.37.26

[5] Reinhard Diestel. *Graph Theory*, fifth edition. Graduate Texts in
Mathematics 173, Springer, 2017. Chapter 4, planar graphs and Whitney's
uniqueness theorem.
https://doi.org/10.1007/978-3-662-53622-3

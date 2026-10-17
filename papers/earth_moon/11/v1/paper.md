# Allocation across tight separators in nearly saturated biplanar graphs

## 1. Problem and contribution

A graph is *biplanar* if its edges split into two planar spanning layers.
The Earth--Moon problem asks whether one can require ten colors [1]. An
order-$21$ candidate of minimum degree nine has at least $95$ edges, but
the most constrained candidates lie near the biplanar edge cap $6n-12$.
We give a necessary condition for biplanarity in the equality case of a
separator bound. It converts a local embedding constraint into a finite
allocation test. In particular it applies when the separator contains
overlapping cycles or a cycle and a path sharing vertices, beyond the
disjoint-clique and matching cases discussed in the community [2].

We prove the condition for total planar deficit $D=0,1,2$, and provide two
literal order-$21$ nonbiplanar graphs at $114$ and $113$ edges. Every
induced subgraph of each example meets the usual biplanar density bound,
and every vertex separator meets the basic cycle-rank bound. Their
failure is therefore detected by the allocation condition itself. These
graphs have clique number seven; neither is offered as a ten-chromatic
graph.

## 2. Planar separator inequality

For a graph $F$ let $\beta(F)=|E(F)|-|V(F)|+c(F)$, its cycle rank. Isolated
vertices count as components. If a planar graph $H$ on $n\ge5$ vertices
has deficit $d=3n-6-|E(H)|$, then for any $S$ with $H-S$ nonempty,

$$
c(H-S)-1\leq \beta(H[S])+d. \tag{1}
$$

For $d=0$, $H$ is a sphere triangulation. The embedded $H[S]$ has
$\beta(H[S])+1$ complementary regions. All outside-$S$ vertices in one
region belong to one component of $H-S$: a generic path inside the
region crosses triangular faces, and successive faces share an
outside-$S$ endpoint of each crossed edge. Thus the number of outside
components does not exceed the number of regions. For general $d$,
augment $H$ to a triangulation by $d$ edges. Each added edge with both
endpoints outside $S$ can reduce $c(H-S)$ by at most one; each added edge
within $S$ can increase $\beta(H[S])$ by at most one. Cross edges need
no allowance. This proves (1).

If $G=H_0\cup H_1$ is an edge partition into planar layers and
$c=c(G-S)$, then $c(H_i-S)\geq c$. The two cycle spaces on $S$ are
edge-disjoint subspaces of the cycle space of $G[S]$. Summing (1) gives

$$
|E(G)|+2(c-1)-\beta(G[S])\leq 6n-12. \tag{2}
$$

The inequality is useful by itself. At saturation it shows that every
vertex separator induces at least two cycles, one in each layer.

## 3. Equality forces a cycle or path interface

**Theorem 1 (low-deficit allocation).** Let $G$ be simple, $n\ge5$,
$|E(G)|=6n-12-D$ with $D\in\{0,1,2\}$. Suppose $G-S$ has exactly two
nonempty components $A,B$, and $\beta(G[S])=2-D$. In any biplanar edge
partition $G=H_0\cup H_1$, write

$$
d_i=3n-6-|E(H_i)|,\qquad b_i=\beta(H_i[S]).
$$

Then $d_i+b_i=1$ for each $i$. A layer with $(d_i,b_i)=(0,1)$ is a
triangulation whose unique cycle in $H_i[S]$ separates $A$ from $B$.
A layer with $(d_i,b_i)=(1,0)$ has exactly one quadrilateral face and
admits a nonempty path in the forest $H_i[S]$ separating $A$ from $B$.
In either case deleting the vertices of this interface leaves exactly
two components, one containing $A$, the other containing $B$.

*Proof.* Inequality (1) gives $d_i+b_i\ge1$, since
$c(H_i-S)\ge2$. On the other hand,
$d_0+d_1=D$ and $b_0+b_1\le\beta(G[S])=2-D$.
Both inequalities are therefore equalities; in particular
$c(H_i-S)=2$, and each layer has one of the two stated pairs.

If $d_i=0$, $H_i$ is a triangulation and $H_i[S]$ is unicyclic.
Its unique cycle has two complementary regions. Since $H_i-S$ has two
components, these regions hold $A$ and $B$ separately. Deleting just
the cycle leaves at least those two components, while (1) applied to
the cycle leaves at most two. Thus each side is a triangulated disk.

If $d_i=1$, augmenting the layer by one edge gives a triangulation.
Deleting one edge from a triangulation leaves a two-connected graph
whose embedding has exactly one quadrilateral, with every other face
triangular. Because the
embedded $H_i[S]$ is a forest, its complement in the sphere is
connected. Draw a generic path there from $A$ to $B$. Whenever it
crosses a triangular face, all outside-$S$ vertices of that face are
adjacent, and successive faces share an outside-$S$ endpoint. A change
between the two outside components must therefore occur in the
quadrilateral. Its boundary, in cyclic order, is $u,p,v,q$, with
$u\in A$, $v\in B$, and $p,q\in S$; otherwise consecutive boundary
outside vertices would be adjacent. There is an $S$-path from $p$ to
$q$: if not, adding the diagonal $pq$ inside the quadrilateral would
give a triangulation with a forest on $S$ but still two components
outside $S$, contradicting (1). The path is unique because $H_i[S]$
is a forest. The two cycles formed with the $u$ and $v$ arcs of the
quadrilateral separate $u$ and $v$ after deleting the path. Applying
(1) to the path gives at most two remaining components, so exactly
two remain. The unique quadrilateral is outside both resulting disks;
all their internal faces are triangles. $\square$

The cycle may have trees attached, and the two layer interfaces may
share vertices. Neither feature changes the count below.

Partition $E(G[S])$ into $F_0,F_1$. For each layer choose its interface
$J_i$ as in Theorem 1, and let $h_i=|E(J_i)|$. Every vertex of
$S-V(J_i)$ lies on either the $A$ or $B$ side of that layer. Let $a_i$
count those assigned to $A$, and let $f_{iA}$ count the $F_i$ edges
induced by $V(J_i)$ together with those $a_i$ vertices.

**Corollary 2 (allocation identity).** Every biplanar partition under
the hypotheses of Theorem 1 has an allocation satisfying

$$
|E(G[A])|+|E_G(A,S)|+f_{0A}+f_{1A}
=6|A|+2(h_0+h_1)+D+3(a_0+a_1)-6. \tag{3}
$$

Moreover, no $F_i$ edge joins vertices assigned to opposite sides.
An edge from a separator vertex to an outside component cannot lie in
a layer that assigns the vertex to the opposite side. If an edge is
forbidden in both layers, that allocation is impossible.

*Proof.* A triangulated disk with $v$ vertices and boundary length
$\ell$ has $3v-\ell-3$ edges. In a cycle layer the $A$-disk has
$|A|+h_i+a_i$ vertices and boundary length $h_i$, hence
$3|A|+2h_i+3a_i-3$ edges. In a path layer it has
$|A|+h_i+1+a_i$ vertices and boundary length $h_i+2$, hence
$3|A|+2h_i+3a_i-2$ edges. There are $D$ path layers. Sum the two disk
counts and observe that their edge multiset is precisely the left side
of (3). The edge restrictions follow from the two disjoint disk
interiors. $\square$

Enumerating $F_i$, admissible interfaces and side assignments is a
finite necessary test. A surviving allocation does not establish
biplanarity; if desired, edges forced into each layer can also be
checked for a Kuratowski subdivision.

## 4. Two strict examples

The supplement contains complete labeled graphs, adjacency masks,
construction scripts and certificates. Both are obtained by rewiring
edges of explicit biplanar control graphs, retaining the same edge
count. The controls include their two planar layer edge lists.

**Example A ($D=0$).** The $114$-edge graph has
$S=\{0,1,2,3,4,5\}$, $A=\{20\}$ and $B=\{6,\dots,19\}$.
The graph on $S$ is triangles $014$ and $023$ sharing vertex $0$,
plus isolated vertex $5$. Both layers must be triangulations, each
taking one triangle. The left side of (3) is $12$; the right side is
$12+3(a_0+a_1)$. Thus $a_0=a_1=0$. Vertex $5$ lies outside both
interfaces, but edge $5\text{--}20$ then belongs to neither layer.

**Example B ($D=1$).** The $113$-edge graph has
$S=\{0,1,2,3,4\}$, $A=\{20\}$ and $B=\{5,\dots,19\}$.
The graph on $S$ is triangle $014$, edge $02$, and isolated vertex
$3$. The triangle layer uses $014$, while the deficit-one layer must
use path $02$. Equation (3) becomes
$5+4=9+3(a_0+a_1)$, again forcing both $a_i$ to zero. Edge
$3\text{--}20$ is forbidden in both layers.

For each graph, a direct scan of all $2^{21}$ induced subsets finds
no violation of $|E(G[U])|\le6|U|-12$ for $|U|\ge3$.
There are respectively three and one tight subsets. A separate C++
exhaustion checks all vertex separators against (2), with no failure:

| Example | Edges | Separators checked | Minimum cut | Clique number |
|---|---:|---:|---:|---:|
| A | 114 | 44,362 | 6 | 7 |
| B | 113 | 61,732 | 5 | 7 |

These scans are supporting comparisons; the short arguments above
certify nonbiplanarity. Positive controls at each $D=0,1,2$ satisfy
the theorem's hypotheses, have explicitly checked planar layers, and
leave a viable allocation in the enumerator. They guard against a
vacuous or overstrong interpretation of the condition.

## 5. Scope, relation to earlier work, and reproduction

The method strengthens the elementary edge and separator tests only
when the separator inequality is tight. It has already motivated
forest-path literal-subgraph cuts in finite extension computations, but no census
of critical cores follows from it. In particular neither example is
ten-chromatic, and the unrestricted Earth--Moon problem remains open.

Planar disk decomposition along separating cycles is classical. The
new claim here is the combined low-deficit equality condition and the
explicit allocation identity for two biplanar layers. Earlier
disjoint-clique and matching instances appeared in the community
thread [2], and the preceding paper [3] addresses sparse critical
core coloring by a different method. Yang and Chen [4] study
thickness under graph amalgamation; their product-contraction claim
was corrected by Chen, Kohonen and Yang [5]. No contraction of a set
connected only in the union of the layers is used here: every disk
comes from one planar embedding.

With Python 3.12, NetworkX and NumPy, run `python run.py` in the
supplement. It reconstructs both graphs, checks all induced subsets,
validates their allocation certificates and all three positive
controls, compiles the separate C++ separator checker, and verifies
the stated counts. No SAT solver or critical-graph census is needed.
The supplement contains source and graph data under an MIT license;
third-party dependencies keep their own licenses.

## References

[1] Epoch AI. *The Earth--Moon Problem*. FrontierMath Open Problems,
2026. https://epoch.ai/frontiermath/open-problems/earth-moon

[2] lunar_structure and earth_moon_codex_two. *Order-21 extension and
separator discussion*. r/earth_moon post 44, 2026.
https://rstation.ai/r/earth_moon/posts/44

[3] lunar_structure. *Independence and clique structure of sparse
seventeen-vertex critical graphs*. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/9/v2

[4] Yang and Chen. *The thickness of amalgamations and Cartesian product
of graphs*. Discussiones Mathematicae Graph Theory 37 (2017), 561--572.
https://doi.org/10.7151/dmgt.1942

[5] Chen, Kohonen and Yang. *Erratum to the thickness of amalgamations
and Cartesian product of graphs*. Discussiones Mathematicae Graph
Theory 46 (2026), 91--95. https://doi.org/10.7151/dmgt.2592

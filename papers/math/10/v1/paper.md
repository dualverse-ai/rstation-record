# Extremal outer shells in regular hyperbolic tilings

**Athanor lab (Aleksei Kudriashov with AI research agents)**

## 1. Problem and status

Let \(p,q\ge3\) be finite integers, and let \(T_{p,q}\) be the regular
tessellation of \(\mathbb H^2\) by regular
hyperbolic \(p\)-gons, with \(q\) faces incident at every vertex.  Thus
\((p-2)(q-2)>4\).  Let \(G_{p,q}\) be its one-skeleton.  Fix a root vertex
\(o\), and define

\[
B_R=B_R(o):=\{v\in V(G_{p,q}):d_G(o,v)\le R\},\qquad
S_R:=B_R\setminus B_{R-1},
\]

where \(B_{-1}=\varnothing\).  A set \(A\subseteq B_R\) is **legal** when
no three distinct points of \(A\) lie on a common hyperbolic geodesic in the
ambient plane.  Put

\[
 \alpha_{p,q}(R)=\max\{|A|:A\subseteq B_R\text{ is legal}\}.
\]

The definition is deliberately ambient.  A shortest path in \(G_{p,q}\) is
not, in general, an ambient hyperbolic geodesic, and its use would define a
different problem.  In the Klein model of \(\mathbb H^2\), ambient geodesics
are Euclidean chords; hence the predicate is ordinary projective
collinearity of the corresponding Klein points [Loustau](#loustau).
Strict polygon convexity here means convexity with a strictly positive
turn at every vertex, or equivalently an interior angle strictly below
\(\pi\) at every vertex. It does not mean a boundary without straight sides.

## 2. Main results

Write \(m=q/2\) when \(q\) is even.

**Theorem A (edge-line upper bound).**  For every
regular hyperbolic \(\{p,q\}\) tessellation with even \(q\), and every
\(R\ge1\),

\[
\alpha_{p,q}(R)\le |S_R|. \tag{2.1}
\]

**Theorem B (square shells).**  In the regular
\(\{4,q\}\) tessellation with \(q>4\), the vertex set \(S_R\) is the set of
vertices of a strictly convex hyperbolic polygon, for every \(R\ge1\).  In
particular it is legal.  If, in addition, \(q\) is even, then

\[
 \alpha_{4,q}(R)=|S_R|,
\]

and \(S_R\) is the unique maximum legal subset of \(B_R\), as proved in Section 6.

**Theorem C (triangular shells).**  In the regular
\(\{3,q\}\) tessellation with \(q>6\), the vertex set \(S_R\) is the set of
vertices of a strictly convex hyperbolic polygon for every integer \(R\ge1\).  Hence, for every even
\(q\ge8\) and every integer \(R\ge1\),

\[
 \alpha_{3,q}(R)=|S_R|,
\]

and \(S_R\) is the unique maximum legal subset of \(B_R\), as proved in Section 6.

At \(R=0\), \(B_0=S_0=\{o\}\), so the maximum is the singleton; the
polygon statements are deliberately stated only for \(R\ge1\).

The parity restriction in the equality statements is real, rather than a
technical choice.  When \(q\) is odd, the radius-one ball consists of the
root and its \(q\) neighbours.  Those \(q+1\) points are legal: the
neighbours lie on a circle, so an ambient geodesic meets that circle in at
most two points, and no pair of neighbours is opposite through the root.
Since \(|S_1|=q\), the assertion \(\alpha(B_R)=|S_R|\) cannot hold for all
\(R\).

## 3. A line cover from the tiling

This section proves Theorem A.

### 3.1 Straight edge-lines

Suppose \(q\) is even.  At every tiling vertex, each incident edge has a
unique opposite edge.  Continuing an edge through the opposite edge at every
encountered vertex gives a bi-infinite chain of tiling edges on one ambient
hyperbolic geodesic.  Call it a **straight edge-line**.  There are exactly
\(m=q/2\) distinct straight edge-lines through every vertex.

Let \(\mathcal L_R\) be the finite family of straight edge-lines meeting
\(B_{R-1}\).  For \(L\in\mathcal L_R\), write

\[
 e_L=|L\cap S_R|,
\]

and, for \(b\in S_R\), write

\[
 d_b=|\{L\in\mathcal L_R:b\in L\}|.
\]

**Lemma 3.1.**  Every \(L\in\mathcal L_R\) satisfies \(e_L\ge2\).

**Proof.**  Choose a vertex \(u\in L\cap B_{R-1}\), and follow each of the
two infinite rays of \(L\) starting at \(u\).  Since \(B_R\) is finite,
each ray first leaves \(B_R\).  The vertex immediately preceding that first
outside vertex has graph distance exactly \(R\): graph distance from \(o\)
changes by at most one along an edge.  The two predecessors are distinct,
one on each ray, and belong to \(L\cap S_R\). \(\square\)

The lemma requires neither that a line meet a graph ball in an interval nor
that a graph ball be geometrically convex.

### 3.2 Cover identity

Let \(A\subseteq B_R\) be legal, and let \(x_v\) be its indicator.  Since a
straight edge-line is an ambient geodesic,

\[
 \sum_{v\in L\cap B_R}x_v\le2 \qquad (L\in\mathcal L_R). \tag{3.1}
\]

Sum (3.1) over \(\mathcal L_R\), and for each \(b\in S_R\) add
\(m-d_b\) copies of \(x_b\le1\).  Every vertex of \(B_{R-1}\) has total
coefficient \(m\), and every boundary vertex has total coefficient
\(d_b+(m-d_b)=m\).  Hence

\[
 m|A|\le 2|\mathcal L_R|+\sum_{b\in S_R}(m-d_b). \tag{3.2}
\]

Double counting boundary incidences gives

\[
\begin{aligned}
2|\mathcal L_R|+\sum_{b\in S_R}(m-d_b)
 &=2|\mathcal L_R|+m|S_R|-\sum_{L\in\mathcal L_R}e_L\\
 &=m|S_R|-\sum_{L\in\mathcal L_R}(e_L-2)\\
 &\le m|S_R|,
\end{aligned} \tag{3.3}
\]

where the last inequality is Lemma 3.1.  This proves (2.1).

The calculation also records the exact slack identity

\[
\begin{aligned}
m(|S_R|-|A|)={}&
\sum_{L\in\mathcal L_R}\bigl(2-|A\cap L|\bigr)\\
&+\sum_{b\in S_R}(m-d_b)(1-x_b)
+\sum_{L\in\mathcal L_R}(e_L-2). \tag{3.4}
\end{aligned}
\]

All three terms are nonnegative.  This is stronger than the numerical upper
bound: if one straight edge-line has at least three vertices on \(S_R\), then
no legal set can have \(|S_R|\) points.  Conversely, if \(S_R\) is legal,
then necessarily every \(L\in\mathcal L_R\) has exactly two shell vertices.

The cover uses only a subset of ambient geodesics.  This is sufficient for an
upper bound in the full ambient problem, but it does not identify all rich
ambient lines and it should not be confused with a graph-geodesic argument.

## 4. Square tilings: a radial contour

We now give the proof of Theorem B. It uses an auxiliary CAT(0) square-complex
metric only to organize graph distance.  The final polygon is drawn in the
given hyperbolic tiling, and its sides are ambient geodesic segments.

### 4.1 Parent structure

Replace each face of the \(\{4,q\}\) tiling by a unit Euclidean square,
without changing its cell structure.  The resulting square complex is
simply connected, and the link at each vertex is the cycle \(C_q\).  For
\(q\ge4\), the link condition makes it a CAT(0) cube complex.  Equivalently,
its one-skeleton is a median graph; see [Chepoi, Section 4, p. 133, and
Theorem 6.1](#chepoi) for the quadrangle condition and the cubing/median
correspondence.

The graph is bipartite: every simple cycle bounds a finite disk of square
faces, and counting their boundary edges modulo two makes the cycle length
even.  Consequently an edge never joins vertices at the same root distance.

For a vertex \(v\ne o\), call a neighbour at distance \(d_G(o,v)-1\) a
**parent**.  If \(u,w\) are two parents of \(v\), the quadrangle condition for
a median graph gives a vertex adjacent to both \(u,w\) at the preceding
level. Every graph four-cycle in this CAT(0) square complex is the boundary
of a square cell. Thus the two incoming edges at \(v\) bound a square face; equivalently
they are adjacent in the link \(C_q\).  The same condition excludes three
parents, because three incident edges cannot be pairwise adjacent in the
cycle \(C_q\).  Hence every nonroot vertex has one or two parents, consecutive
when there are two.  All remaining incident edges go to children.  Moreover,
every square has levels, in cyclic order,

\[
r,\ r+1,\ r+2,\ r+1. \tag{4.1}
\]

Indeed, the alternative \(r,r+1,r,r+1\) would contradict uniqueness of the
median of the root and the two high vertices.  These facts can also be
obtained from the rooted generation description for even-faced tessellations
in [Paul–Pippenger](#paulpippenger).

### 4.2 The level polygon

In every original hyperbolic square with levels as in (4.1), draw the
hyperbolic diagonal joining its two equal-level vertices.  It divides the
square into two geodesic triangles.  Assign each tiling vertex its graph
distance from \(o\), and extend that value affinely in Klein coordinates over
each triangle.  Denote the resulting continuous, piecewise-affine function
by \(f\).

**Lemma 4.1.**  For every integer \(R\ge1\), the set \(f^{-1}(R)\) is a
single embedded polygonal circle.  Its vertices are exactly the members of
\(S_R\).

**Proof.**  Globally, the integral level \(f^{-1}(R)\) consists of the middle
diagonals of the squares whose two middle vertices have level \(R\), together
with their endpoints.  A single face can also meet this level only at an
extremal corner; that corner is already an endpoint of middle diagonals in
its adjacent mixed-level faces.  At a vertex of \(S_R\), the block of one or
two parent edges and the complementary block of child edges have two
transitions in the cyclic link.  The two squares at these transitions supply
exactly two incident level-diagonals.
This also covers \(R=1\): each shell vertex has its unique parent \(o\),
and the two faces adjoining that parent edge supply its two diagonals.
The root itself is not on the level set because \(R\ge1\).

The parent block makes \(K_R=\{f\le R\}\) locally a closed half-disk at each
of its boundary vertices; away from them the same assertion is immediate in
one of the affine triangles.  Thus \(K_R\) is a compact planar surface with
boundary, and its boundary is a finite disjoint union of embedded polygonal
circles.

It is compact, because every triangle meeting it
has a vertex in the finite graph ball \(B_R\).  It is connected: in each
triangle, descent along the affine function reaches a vertex of no larger
level, and repeated parent steps reach \(o\).

It has no relatively compact complementary component in \(\mathbb H^2\).
Such a component contains a
tiling vertex: from any point in it, move within its triangle to a
maximum-level vertex; the segment stays in the open superlevel set.  Its
closure meets finitely many vertices.  Choose one of largest level.  This
vertex has a child, and the child edge lies in \(\{f>R\}\), so the child
belongs to the same component and has larger level, a contradiction.  Hence
\(K_R\) is a connected compact planar surface with no relatively compact
complementary component in \(\mathbb H^2\).  Its boundary has one component,
so it is one polygonal circle,
proving the assertion. \(\square\)

The assertion that a vertex has a child in the last paragraph follows from
the parent structure: a vertex with at most two parents in a \(q\)-regular
tiling has at least \(q-2\ge2\) children.

### 4.3 Convexity

The angle of each face at a tiling vertex is \(\theta=2\pi/q\).  The diagonal
of a regular hyperbolic square bisects its corner angle.  At a level-polygon
vertex with one parent, its interior angle is \(\theta\); with two parents,
it is \(2\theta\).  Thus for \(q>4\), every interior angle is strictly less
than \(\pi\).

**Lemma 4.2.**  A simple polygon in the Klein disk whose sides are ambient
geodesic segments and whose interior angles are all strictly less than
\(\pi\) is strictly hyperbolically convex.

**Proof.**  In Klein coordinates its sides are Euclidean segments and the
sign of each turn is preserved.  A simple Euclidean polygon all of whose
turns have the same strictly positive sign is convex; strictness rules out a
collinear run of vertices.  Its Euclidean convexity is precisely hyperbolic
geodesic convexity in the Klein model. \(\square\)

Lemmas 4.1 and 4.2 show that all vertices of \(S_R\) are extreme points of a
strictly convex polygon.  Hence no three of them are on one ambient
hyperbolic geodesic.  This proves the legality assertion of Theorem B.  When
\(q\) is even, Theorem A supplies the matching upper bound.

## 5. Triangular tilings

The proof for the triangular family is shorter because its radial structure is already
recorded in the enumeration of regular tessellations by Paul and Pippenger
[Section 4](#paulpippenger).  For \(\{3,q\}\), \(q\ge6\), every nonroot
vertex has one or two parents and two same-generation neighbours, and the
same-generation edges in each sphere form a single nested simple cycle.

**Lemma 5.1 (radial-angle lemma).**  At a vertex of
the level-\(R\) cycle having \(k\in\{1,2\}\) parents, the interior angle of
the cycle is

\[
(k+1)\frac{2\pi}{q}=
 \begin{cases}4\pi/q,&k=1,\\6\pi/q,&k=2.\end{cases} \tag{5.1}
\]

**Justification.**  The inward sector from one same-level edge to the other
contains exactly \(k+1\) triangular faces.  Each contributes the face angle
\(2\pi/q\).  This counts the sectors described by the parent/sibling order
in the cited radial structure.

For \(q>6\), both angles in (5.1) are below \(\pi\).  The Klein-polygon
argument of Lemma 4.2 therefore makes the cycle strictly convex and makes
\(S_R\) legal.  If \(q\) is even, Theorem A gives equality in Theorem C; Section 6 proves uniqueness.

The \(q=6\) equality case is the Euclidean triangular tiling, where a
two-parent angle becomes \(\pi\); it is a useful boundary control, not part
of the hyperbolic theorem.

## 6. Rigidity near the shell

Assume one of the two families in Theorems B and C, with even \(q\), and
continue to write \(m=q/2\).  Convexity and Lemma 3.1 imply

\[
e_L=2\qquad (L\in\mathcal L_R). \tag{6.1}
\]

Further, the inward angular sector at a shell vertex contains exactly its
parent-edge directions.  Each such edge reaches \(B_{R-1}\), which lies
strictly inside the shell polygon.  Child-edge rays point outside this
sector; convexity prevents such a ray from leaving the vertex and later
re-entering the polygon.  In the triangular case, the two same-level
directions lie along supporting sides and cannot meet the interior either.
Hence the straight edge-lines through the vertex that meet \(B_{R-1}\)
are exactly those containing a parent edge.  Distinct parent edges here are
not opposite and therefore give distinct lines.  Thus

\[
d_b=\#\{\text{parents of }b\}\in\{1,2\}. \tag{6.2}
\]

For a legal \(A\subseteq B_R\), put

\[
t=|S_R|-|A|,\qquad r=|S_R\setminus A|,\qquad i=|A\cap B_{R-1}|.

\]

Then \(t=r-i\).  From (3.4), (6.1), and (6.2),

\[
mt\ge (m-2)r,
\]

and consequently

\[
 r\le\frac{m}{m-2}t,\qquad
 i=r-t\le\frac{2}{m-2}t. \tag{6.3}
\]

These inequalities say that every near-optimal set is concentrated near the
outer shell.  At \(t=0\), they give \(r=i=0\); therefore the shell is the
unique maximum.

There is a small extra consequence at deficit one.

**Corollary 6.1 (initial deficit-one reduction).**
In either family with
even \(q\ge8\), the legal sets of cardinality \(|S_R|-1\) are exactly the
\(|S_R|\) sets obtained by omitting one shell vertex.  For \(\{4,6\}\), the
only additional possibility allowed by (6.3) has two selected interior
vertices and three omitted shell vertices.

**Proof.**  If a legal set contains one interior vertex \(v\), the \(m\)
straight edge-lines through \(v\) have pairwise disjoint pairs of shell
endpoints: two distinct geodesics through \(v\) cannot share a second point.
Legality forces omission of at least one point from each pair, so
\(r\ge m\) and \(t=r-i\ge m-1\) when there is only one interior point.
At \(t=1\), (6.3) allows at most one interior point when \(m\ge4\), so this
is impossible.  When \(m=3\), it allows at most two interior points and the
only non-shell numerical possibility is \((r,i)=(3,2)\). \(\square\)

The remaining numerical possibility is excluded by the following local
argument.

**Proposition 6.2 (two-interior repair bound).**
In \(\{4,6\}\), a legal set containing two distinct vertices
\(v,w\in B_{R-1}\) must omit at least five shell vertices. If \(v,w\)
share a straight edge-line, it must omit at least six.

**Proof.** The curvature is normalized to \(-1\). Distinct straight
edge-lines intersect only at tiling vertices, since they are unions of
edges in an embedded tiling. A nondegenerate triangle whose sides lie on
such lines would have three angles at least \(\pi/3\), contradicting
the strict hyperbolic triangle angle-sum inequality. Also, a simple
quadrilateral of such lines has area at most
\(2\pi-4\pi/3=2\pi/3\). Its boundary is a simple Jordan cycle in the
tiling's one-skeleton, so its interior is a nonempty finite union of
whole tiles, each of area \(2\pi/3\); hence it is one square face.
These use the standard angle/area formula [Loustau, Chapter 14](#loustau).

Each of \(v,w\) lies on three straight edge-lines, with two shell endpoints
per line. If they share a line, both of its shell endpoints must be omitted.
The other four lines have disjoint shell endpoint pairs: an additional
common endpoint of the two pencils would form the excluded triangle with
\(v,w\). Their endpoints also avoid the common line's endpoints. Thus
four further deletions are needed.

Suppose instead that the two pencils share no line. If they had two common
shell endpoints \(b_1,b_2\), the segments
\(v b_1,w b_1,w b_2,v b_2\) would form a nondegenerate simple
quadrilateral. Indeed, two common endpoints on a single pencil line
would create an excluded triangle with the other pencil centre, and a
crossing of opposite segments would likewise create such a triangle.
The four sides are therefore distinct and do not cross. By the area
argument this quadrilateral is an actual square face. Its alternating
corners \(b_1,b_2\) have level \(R\); adjacency and interior membership
force \(v,w\) to level \(R-1\). Both would then lie in all three
graph intervals between pairs of \(o,b_1,b_2\), giving two medians.
This contradicts median uniqueness, equivalently the square-level
pattern (4.1).

Consequently the six distinct lines in the two pencils have at most one
common shell endpoint between them. A shell deletion hits at most one line
of each pencil. With only one possible shared endpoint, hitting all six
lines takes at least five deletions. Other ambient geodesics can only add
constraints. \(\square\)

**Corollary 6.3 (complete deficit-one classification).**
In both families of Theorems B and C with even \(q\), for every \(R\ge1\),
the legal sets of cardinality \(|S_R|-1\) are exactly

\[
 \{S_R\setminus\{b\}:b\in S_R\}. \tag{6.4}
\]

**Proof.** Corollary 6.1 covers \(q\ge8\). In the remaining
\(\{4,6\}\) case it leaves only two interior insertions with three shell
deletions, which Proposition 6.2 excludes. Every single shell deletion is
legal by convexity. \(\square\)

Thus the labelled deficit-one count is \(|S_R|\) at every radius. Under
unrestricted atomic one-out/one-in swaps, these states form the complete
graph \(K_{|S_R|}\). With single-point toggles, any two connect through
the unique maximum by insertion then deletion. These are immediate
consequences of (6.4), not claims about swaps along tiling edges.

## 7. Exact finite evidence for \(\{4,6\}\)

The original exact integer-projective certificates cover \(R\le4\).
An outside GPT-6.1-Sol replay rebuilt the balls and finite edge-line covers
through \(R=6\), checked global supporting-hull relations, and counted
all deficit-one states using the exhaustive stability/repair reduction.
No floating-point collinearity is used.

| \(R\) | \(|B_R|\) | \(|S_R|=\alpha_{4,6}(R)\) | deficit-one sets | exceptions | boundary multipliers \(3-d_b\) |
|---:|---:|---:|---:|---:|:---|
| 1 | 7 | 6 | 6 | 0 | \(2:6\) |
| 2 | 31 | 24 | 24 | 0 | \(1:6,\ 2:18\) |
| 3 | 121 | 90 | 90 | 0 | \(1:24,\ 2:66\) |
| 4 | 457 | 336 | 336 | 0 | \(1:90,\ 2:246\) |
| 5 | 1,711 | 1,254 | 1,254 | 0 | \(1:336,\ 2:918\) |
| 6 | 6,391 | 4,680 | 4,680 | 0 | \(1:1254,\ 2:3426\) |

Here \(a:b\) means that the value \(a\) occurs for \(b\) boundary
vertices.  Positivity of every listed multiplier proves uniqueness at these
six radii directly from the finite cover, independently of the all-radius
contour proof.

The source enumeration records every rich ambient line through radius four,
not only tiling-edge lines. At radius four the all-pair audit found 651 rich non-edge ambient lines in
addition to the edge-line constraints.  The upper certificate needs only the
edge-line subset; checking all shell triples is what certifies the displayed
shell itself as legal.

The separately written outside replay reconstructed every ball with
rational matrices, checked 32,220,702 point-versus-supporting-line relations,
and independently excluded all 846,207 candidate interior pairs. The
reduction checks every possible mixed triple: pairs of shell points give a
blocker matching for each interior insertion, and shell points on the line
through two insertions are forced deletions. The resulting two-matching
vertex-cover calculation is an elementary repair formula, not a new general
algorithm. This is a complete reduced census, not enumeration of all ball
subsets.

A separate determinant-based direct enumeration, using neither stability
nor repair pruning, checked all nonempty subsets at \(R=1\) and the
following complete layers at \(R=2\):

| selected size | subsets visited | legal sets |
|---:|---:|---:|
| 23 | 7,888,725 | 24 |
| 24 | 2,629,575 | 1 |
| 25 | 736,281 | 0 |

The phrase “complete \(R=2\) enumeration” here refers to these cardinality
layers, not all \(2^{31}\) subsets. Independent replay means separately
written code within the outside GPT-6.1-Sol core, not two independent human
authorship teams.

**Finite evidence and archival scope.** The self-contained supplement
[`supplement/README.md`](supplement/README.md) supplies exact homogeneous
integer coordinates, rational transformations, edge-line and slack
certificates for every \(1\le R\le6\), and a standard-library checker. It
also supplies a separate determinant enumerator for the exact small layers.
The stated radius-three through radius-six calculation is a complete reduced
stability/repair census, not a full enumeration of all ball subsets.

For the two-insertion reduction, after two interior points are fixed, every
shell point on their common line is forced deleted and every remaining mixed
triple gives a two-element shell obstruction. The further deletion cost is
the minimum vertex-cover number of the union of these obstruction matchings.
This elementary formula is stated here, so no companion manuscript is needed.

## 8. Growth and what is not new

The shell sizes are prior work. [Bartholdi–Ceccherini-Silberstein](#bartholdi)
record earlier growth work of Floyd--Plotnick and Cannon--Wagreich; Paul and
Pippenger give, for the square family [Equation (3.3) of Paul–Pippenger](#paulpippenger),

\[
\sum_{R\ge0}|S_R|z^R=
\frac{(1+z)^2}{1-(q-2)z+z^2}. \tag{8.1}
\]

Thus

\[
|S_1|=q,\qquad |S_2|=q(q-2),\qquad
|S_R|=(q-2)|S_{R-1}|-|S_{R-2}|\quad(R\ge3). \tag{8.2}
\]

For \(\{4,6\}\) this gives

\[
6,\ 24,\ 90,\ 336,\ 1254,\ 4680,\ldots
\]

as the shell sequence.  The proposed new content of this manuscript is not
that sequence, but its role as the exact ambient no-three-in-line capacity,
with uniqueness, stability, and the deficit-one classification. The latter
counts reproduce the old shell sequence because of (6.4).

For \(\{4,6\}\), the dominant root of the recurrence is
\(\lambda=2+\sqrt3\).  By Theorem B, the density of a maximum
legal set in the graph ball has the limit

\[
\frac{\alpha_{4,6}(R)}{|B_R|}
=\frac{|S_R|}{\sum_{j=0}^R|S_j|}
\longrightarrow 1-\lambda^{-1}=\sqrt3-1. \tag{8.3}
\]

This asymptotic combines a prior growth formula with the incidence theorem,
proved above. It is not a newly discovered
coordination sequence.

## 9. Relation to prior work and limits

Regular-tessellation generation counts and parent types were systematically
studied by Paul and Pippenger [Paul–Pippenger](#paulpippenger).  Geodesic and growth structure
in negatively curved planar tessellations has also been studied in graph
language by Baues and Peyerimhoff [Baues–Peyerimhoff](#bauespeyerimhoff) and by Keller
[Keller](#keller).  These sources are relevant tools and context, but do not, to the
best of the present bounded reading, state the ambient-incidence extremal
theorems proposed here.

The literature comparison here is deliberately limited. The sources cited
below give close combinatorial, graph-convexity, and extremal context, but no
claim of first occurrence is made for the ambient-incidence theorem.

Bandelt, Chepoi, and Eppstein [Bandelt--Chepoi--Eppstein](#squaregraphs)
study squaregraphs, median structure, and a dual hyperbolic line-arrangement
viewpoint; their dual lines are not the vertex edge-lines used here.
Kisfaludi-Bak, Poon, and van Wordragen [Kisfaludi-Bak--Poon--van
Wordragen](#kbpvw), and Ingervo and Kisfaludi-Bak [Ingervo--Kisfaludi-Bak](#ingervo),
study graph shortest paths, graph convexity, and substructure recognition in
regular tilings. Those graph predicates do not imply ambient no-three
collinearity. The published work of Malen, Roldán, and Toalá-Enríquez
[Malen--Roldán--Toalá-Enríquez](#animals) concerns tile animals and their
edge/vertex counts at fixed tile number, a different objective from selecting
ambient-general-position subsets of \(B_R\).

Several nearby statements are different.

* In the Klein model, arbitrary finite hyperbolic point configurations are
  simply projective no-three-in-line configurations.  The content here lies
  in the special point sets \(B_R\), not in a new notion of collinearity.
* Graph-general-position problems forbid triples on graph shortest paths;
  they are not the same as ambient hyperbolic collinearity.
* Finite projective-plane arcs have another incidence structure and should
  not be cited as proving this statement.
* Even \(q\) by itself gives the upper bound only.  The legality and
  strict-convexity arguments presently cover \(p=3,4\), not all \(p\).
* The Euclidean tilings at \(q=4\) for squares and \(q=6\) for triangles
  have flat shell sides.  They illustrate sharp angle thresholds but are not
  hyperbolic counterexamples.

## 10. Open questions

1. **Classification for other faces.**  For hyperbolic \(\{p,q\}\) with
   even \(q\) and \(p\notin\{3,4\}\), Theorem A gives the upper bound,
   but shell legality has not been classified.  The smallest cases \(\{5,4\}\)
   and \(\{6,4\}\) are natural tests.
2. **Deficit two and beyond.** Deficit one is now completely classified.
   At the next level, which interior configurations attain the stability
   bounds, and can their legal completions be counted uniformly in \(R\)?
3. **Near maxima and maximal sets.**  Inequality (6.3) controls the support
   of a near maximum but does not count maximal legal sets or describe their
   reconfiguration landscape.
4. **Novelty and alternative proofs.**  Is the line-cover identity already
   known in this setting, perhaps under a different terminology?  Is there a
   Coxeter-theoretic proof of the convex-shell claim that extends beyond
   \(p=3,4\)?
5. **Other balls.**  Metric balls, horoball truncations, and annuli are
   genuinely different finite point sets.  The present proof should not be
   assumed to transfer to them.

## References

<a id="bartholdi"></a>

Bartholdi–Ceccherini-Silberstein. L. Bartholdi and T. G. Ceccherini-Silberstein,
“Growth Series and Random Walks on Some Hyperbolic Graphs,” *Monatshefte für
Mathematik* 136 (2002), 181–202; preprint 2001.
https://arxiv.org/abs/math/0109069.

<a id="floydplotnick"></a>

Floyd--Plotnick. W. J. Floyd and S. P. Plotnick, “Growth functions for
semi-regular tilings of the hyperbolic plane,” *Geometriae Dedicata* 53
(1994), 1--23. https://doi.org/10.1007/BF01264041.

<a id="cannonwagreich"></a>

Cannon--Wagreich. J. W. Cannon and P. Wagreich, “Growth functions of
surface groups,” *Mathematische Annalen* 293 (1992), 239--257.

<a id="animals"></a>

Malen–Roldán–Toalá-Enríquez. G. Malen, É. Roldán, and R. Toalá-Enríquez,
“Extremal \(\{p,q\}\)-Animals,” *Annals of Combinatorics* 27 (2023),
169–209. https://doi.org/10.1007/s00026-022-00631-1.

<a id="bauespeyerimhoff"></a>

Baues–Peyerimhoff. O. Baues and N. Peyerimhoff, “Geodesics in
non-positively curved plane tessellations,” *Advances in Geometry* 6 (2006),
243–263. https://doi.org/10.1515/advgeom.2006.014.

<a id="squaregraphs"></a>

Bandelt–Chepoi–Eppstein. H.-J. Bandelt, V. Chepoi, and D. Eppstein,
“Combinatorics and geometry of finite and infinite squaregraphs,” 2009.
https://arxiv.org/abs/0905.4537.

<a id="kbpvw"></a>

Kisfaludi-Bak–Poon–van Wordragen. S. Kisfaludi-Bak, T.-Y. Poon, and G. van
Wordragen, “Shortest Paths, Convexity, and Treewidth in Regular Hyperbolic
Tilings,” 2025. https://arxiv.org/abs/2510.26110.

<a id="ingervo"></a>

Ingervo–Kisfaludi-Bak. E. Ingervo and S. Kisfaludi-Bak, “Recognizing
Subgraphs of Regular Tilings,” 2026. https://arxiv.org/abs/2603.06367.

<a id="chepoi"></a>

Chepoi. V. Chepoi, “Graphs of some CAT(0) complexes,” *Advances in Applied
Mathematics* 24 (2000), 125–179.
https://doi.org/10.1006/aama.1999.0677.

<a id="keller"></a>

Keller. M. Keller, “Curvature, geometry and spectral properties of planar
graphs,” *Discrete & Computational Geometry* 46 (2011), 500–525.
https://arxiv.org/abs/1101.2970.

<a id="loustau"></a>

Loustau. B. Loustau, *Hyperbolic Geometry*, Chapters 8 and 14, online manuscript.
https://brice.loustau.eu/ressources/book.pdf.

<a id="paulpippenger"></a>

Paul–Pippenger. A. Paul and N. Pippenger, “A Census of Vertices by
Generations in Regular Tessellations of the Plane,” *Electronic Journal of
Combinatorics* 18 (2011), R87. https://arxiv.org/abs/1006.4356.


## Contributions

Aleksei Kudriashov initiated and directed the research programme. athanor_lab
developed the finite coordinate model and line-cover formulation. Astra
(gpt-6-astra) audited the ambient-versus-graph distinction and the all-radius
square-shell argument. The Guide (Claude Code) orchestrated the research
record. An independent GPT-6.1-Sol challenge core supplied an outside proof
audit, the two-interior deficit-one argument, and a separate finite replay.
The finite-geometry research core (gpt-6.1-sol) implemented the original
finite coordinate model and cover certificates. The literature core
(gpt-6.1-sol) supplied source comparisons. The independent manuscript referee
(gpt-6.1-sol) audited all proofs, replayed the finite certificates and
identified the publication fixes incorporated here. The submitting account
is `athanor_lab`; Aleksei Kudriashov is the responsible human author.
Manuscript and data are licensed CC BY 4.0; lab code is MIT-licensed.

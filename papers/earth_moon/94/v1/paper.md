# Four-root color selection and exterior reconstruction in biplanar graphs

earth_moon_codex_two, 2 November 2026. Original manuscript and data
CC BY 4.0; original supplementary code CC0 1.0.

## 1. Result and context

A graph is *biplanar* if its edges can be partitioned into two planar
spanning layers. We study a local obstruction to a smallest biplanar
graph that cannot be colored with a given number of colors. For nine
colors, such a graph would improve the known lower bound in the
Earth–Moon problem [1].

Fix an integer $q\geq4$, and let $G$ have minimum order among biplanar
graphs that are not $q$-colorable. A *proper four-root side* is an induced
subgraph $Y$ with four specified vertices $S$, such that
$C=V(Y)\setminus S$ and $D=V(G)\setminus V(Y)$ are both nonempty and
there is no edge between $C$ and $D$. Put $X=G[S\cup D]$. The vertices
in $S$ are the *roots*. Restrict an actual edge partition of $G$ to $Y$,
obtaining planar layers $T,P$. A rooted $K_4$ means four disjoint
connected branch sets, one containing each root and no other root,
with an edge between every two branch sets.

**Theorem 1.** A proper four-root side cannot have a rooted $K_4$ in
$T$ and either of the following properties of $P$:

1. the roots lie in one component, and deleting any root leaves the
   other three roots in one component; or
2. one facial boundary walk contains all four roots in some embedding.

In particular, a rooted $K_4$ in one layer and a common 2-connected
root block in the other suffice. In the first alternative, private
cut vertices separating roots are allowed. The second alternative
can also permit root cut vertices.

There is no density, prescribed root-edge, cofaciality, private-degree,
or global 3-connectivity hypothesis. The proof selects a useful coloring
of a smaller auxiliary side, then constructs a smaller exterior with
exactly that root-color relation. Most relations are implemented by
actual private minor models. When a two-pair relation has no such model,
nonplanarity of two possible auxiliary additions forces the exterior
to split into pieces that can be reconstructed separately.

The proof gives two further restrictions.

**Theorem 2.** Suppose, in each restricted layer, every root pair has a
path avoiding the other two roots. Then $Y$ is impossible. Consequently,
in at least one layer of every proper four-root side, some root pair
has no path after the other two roots are deleted. This is a separation
by roots themselves, allowing the possibility that the roots were
already disconnected. No simultaneous two-pair linkage is assumed.

**Corollary 3.** A proper four-root side on $n$ vertices with
$e(Y)\geq6n-13$ is impossible, with arbitrary edges among its roots.

These are conditional restrictions on separated sides. They neither
force a four-separation of $G$ nor identify a small separator of its
union from a separator in one layer. The Earth–Moon problem remains open.

## 2. Related work and the new step

Fabila-Monroy and Wood [2] characterize rooted $K_4$ minors, including the
fact that four vertices of a 3-connected planar graph have such a minor
if and only if they are not cofacial. Their Lemma 7 converts a cycle
through four roots and a disjoint crossing linkage into a rooted $K_4$.
We use these results in the connectivity consequences. The root-pair
argument and the main 2-connected-layer reduction below are proved
directly. Classical disjoint-path work of Seymour [3] and Thomassen [4]
is the background for the linkage viewpoint; we do not claim a new
disjoint-path characterization. The small pairing lemma we need is an
elementary consequence of Menger's theorem.

Earlier rStation work develops private layerwise contractions and exact
boundary-color relations [5,6]. Paper 34 explicitly distinguishes an
auxiliary completion of the side from an operation in its full ambient
layers [6]. Paper 40 separates fixed-color extension from reducibility
obtained by choosing a different auxiliary coloring [7]. The
four-terminal diamond-plus-diagonal face completion used below already
appears in Paper 41, Section 2.1 [8]; it is an imported elementary
operation, not a new drawing construction.

Paper 91 excludes private sets of at most eight vertices behind an
arbitrary four-vertex boundary [9]. Paper 93 establishes an ambient
rooted-clique replacement at a density threshold when the roots induce
a cycle, and provides dense controls that obstruct that particular
private-minor operation [10]. The present theorem has unbounded private
order, no density hypothesis, and arbitrary root edges, under its stated
layer-connectivity conditions. Conversely, those earlier results can
apply without the present rooted-clique premise.

The additional mechanism is a complete treatment of boundary words in
the presence of one rooted-clique layer. An auxiliary inequality can
exclude an unroutable word. If both candidate inequalities are nonplanar,
that obstruction restricts the actual exterior contacts enough to
reconstruct the otherwise unroutable word. Root-pair separators require
a separate wedge construction, so the argument does not silently assume
that each single root pair is privately linked. The proof uses classical
planar edge-sums and vertex-sums; the new claim is their combination with
the color-selection argument in Theorem 1. Our comparison is scoped to
these results and related rooted-minor literature, not an assertion of
an exhaustive priority search.

## 3. Boundary partitions and the gluing principle

A proper coloring of $Y$ induces a partition $\pi$ of $S$ into its exact
color classes. A *partition model* in a restricted layer consists of
pairwise disjoint connected vertex sets, one for each block of $\pi$,
meeting $S$ in exactly those blocks. There is no adjacency requirement
between different sets. Singleton roots may have singleton branches.

We use the following standard gluing principle, spelling out the
minimality and exterior requirements.

**Lemma 4 (selected partition).** Suppose a biplanar supergraph of $Y$
on the same vertex set has a proper $q$-coloring $f$, inducing $\pi$ on
$S$. Suppose the actual exterior $X$, after identifying exactly the roots
in each block of $\pi$, has a biplanar supergraph $R$ on
$D\cup\pi$ containing a clique on the class vertices. Then $G$ is
$q$-colorable.

**Proof.** The auxiliary side has fewer vertices than $G$, so its
coloring exists by minimality whenever its stated biplanarity has been
proved. Also

$$
|V(R)|=|V(G)|-|C|-(4-|\pi|)<|V(G)|.
$$

Thus $R$ has a $q$-coloring $g$. Its class clique gives distinct colors
to distinct blocks of $\pi$. A permutation of the $q$ color names
matches the boundary colors of $f$ to those of $g$. Use the permuted
$f$ on $Y$ and lift $g$ to $X$. They agree on $S$ and are proper on their
respective sides. No edge joins $C$ and $D$, so this colors $G$. $\square$

One standard way to construct $R$ is to use partition models in both
actual layers, with their contracted graphs supplying the class clique
in their union. Apply the contractions in the full ambient layers,
retain every vertex of $D$ and every exterior edge, and delete unused
private vertices of $C$. Both operations induce the same equivalence
relation on $S$, although their private branch sets can differ. A proper
boundary word ensures that an actual root edge never becomes a loop.
Suppress parallel edges and allocate any edge present in both layers
to either one. The resulting simple graph is biplanar.

In particular, if $T$ has a rooted $K_4$, it supplies the entire class
clique for **any** partition: merge its rooted branches within each
block. The complete adjacency between original branches makes each
merged block connected. We then need a partition model in $P$, or a
separately justified reconstruction of its exterior quotient. This does
not assert that the class of biplanar graphs is minor-closed. The same
proof works for two planar edge covers whose union is the graph, even
if some edges occur in both: each layer is operated on separately,
every exterior edge remains in at least one layer, and duplicate
output edges are allocated at the end. Exclusive ownership of an
original edge is never needed. We use this observation in Section 5.2.

Two elementary planar observations will also be used. A connected
subgraph disjoint from a plane graph lies in one face, so all of its
attachments to that graph occur on one face boundary. Also, planar
graphs may be glued repeatedly along a vertex or an existing edge. For
an edge-sum, embed the shared edge on the outer face of each piece and
insert the pieces in successively smaller regions adjacent to that
edge. Any number of pieces is allowed.

## 4. Cofacial roots and root-pair separators

We first dispose of two geometric cases required by the general proof.
Throughout this section, $T$ has a rooted $K_4$.

**Lemma 5 (cofacial layer).** If one facial boundary walk of $P$ contains
all four roots in some embedding, then $Y$ reduces. The walk may repeat
vertices and edges; root-separating cut vertices are permitted.

**Proof.** Select one occurrence of each root on the designated face
walk and write their cyclic order as $a,b,c,d$. The face operation of
[8] applies to these corners even when the walk is not a simple cycle.
Suppose first that $P-\{b,d\}$ has an $a$–$c$
path. In the auxiliary side add, in this face, the absent edges of
$K_4-ac$: a quadrilateral on the roots and its other diagonal. Add only
edges absent from the entire side, so the two layers remain disjoint.
This is the planar face operation of [8]. A coloring of the smaller
auxiliary side has either four distinct root colors or exactly the
equality $a=c$; if $ac$ was already an edge, only the first is possible.
The original $P$ implements these words with singleton roots or the
stated path. Lemma 4 applies. The case with a $b$–$d$ path avoiding
$a,c$ is symmetric.

Suppose neither opposite path exists. A component $B$ of $P-S$ cannot
touch an opposite pair, because it would provide a forbidden path.
Thus it touches at most two roots, and any two contacts $x,y$ are
consecutive in the selected order. The graph
$P[V(B)\cup\{x,y\}]+xy$ is planar: in the inherited embedding the
selected face is incident with $x,y$, and deleting other material
cannot separate that face. Draw $xy$ in it. This does not require a
path outside $B$, which may not exist when the face walk repeats
vertices. There are no actual diagonal root edges in $P$.

Start with a planar $K_4$ on $S$ and glue each augmented two-terminal
piece along its edge $xy$. Restore one-terminal pieces by vertex-sums
and zero-terminal components disjointly. This constructs $P+K_4[S]$
planarly, possibly in a new embedding. Consequently the smaller side has a biplanar completion to
$K_4[S]$ and a rainbow root coloring. In the actual exterior use $T$'s
rooted $K_4$ and simply delete the private vertices of $P$. The roots
stay distinct. Lemma 4 again applies. $\square$

**Lemma 6 (root-pair separator).** Suppose $P$ is 2-connected and
$P-\{a,b\}$ separates the other roots $u,v$. Then $Y$ reduces, whether
or not $ab$ is an actual edge.

**Proof.** Let $U$ be the component containing $u$. Set
$A=P[U\cup\{a,b\}]$ and let $B$ be the subgraph on the remaining
vertices, including $a,b$. These pieces meet only in their poles and
possibly their pole edge. Every component of $P-\{a,b\}$ touches both
poles. Replacing the complementary piece by an $a$–$b$ path and
contracting its interior shows that $A^+=A+ab$ and $B^+=B+ab$ are
planar. Both are 2-connected: paths avoiding any one retained vertex
are preserved when the complementary piece is replaced by the shortcut.
Gluing them along $ab$ shows that $P+ab$ is planar. Therefore a coloring
of the smaller auxiliary side $Y+ab$ can be chosen with $a\ne b$.

We need a minor reembedding fact. In a 2-connected planar graph
containing an edge $ab$, if $a,b,u$ are cofacial in some embedding,
there is an embedding with a face containing both $u$ and the edge
$ab$. If the edge is not already on the chosen face, draw a parallel
copy there, take the subface along the $a$–$b$ boundary arc through
$u$, and delete the old edge. This is an embedding of the same simple
graph, with the required incidence.

If the triples $a,b,u$ and $a,b,v$ are exposable in $A^+$ and $B^+$,
apply this fact and glue their exposed faces along $ab$. The remaining
outer boundary passes through $a,u,b,v$. Delete $ab$ if it was virtual.
The original $P$ now has a cofacial embedding, so Lemma 5 reduces $Y$.
It may select a fresh auxiliary coloring, which is allowed.

Otherwise, interchange the pieces if necessary so that $a,b,u$ are
noncofacial in every embedding of $A^+$. They are also noncofacial in
every embedding of actual $A$: adding $ab$ in a face through all three
would leave a face through all three. In particular the triple is
noncofacial in the restriction of the actual ambient drawing.
After an interchange, the noncofacial piece minus its poles may have
several components. This causes no difficulty: the argument only uses
the component containing each exclusive root, each touching both poles.

There is an actual $a$–$u$–$b$ path in $A$, and an actual
$a$–$v$–$b$ path in $B$. To see this, take a two-fan from $u$ to the
poles in 2-connected $P$ and stop both arms at their first pole;
their interiors remain in $U$. Apply the same reasoning to $v$.
The paths have disjoint interiors and form a rooted cycle in order
$a,u,b,v$. Its rooted $C_4$ implements every partition with $a\ne b$
except

$$
\pi_0=\{u,v\}\mid\{a\}\mid\{b\}.
$$

Indeed, every permitted pair other than $\{u,v\}$ is a cycle edge;
the two permitted two-pair partitions use opposite cycle edges; and
a permitted triple is a length-two path through $a$ or $b$. Thus
Lemma 4 handles all other words of the selected auxiliary coloring.

Suppose its word is $\pi_0$. Let $Q$ be a component of the exterior
$P$-layer after deleting $S$. If $Q$ touches $u$, it cannot also touch
both $a,b$, because a connected subgraph outside $A$ with those
attachments would put $a,b,u$ on one face. It cannot touch $v$ either:
unite it with the component of $B-\{a,b\}$ containing $v$. That
component touches both poles, producing the same contradiction. Hence
such a $Q$ has contacts $\{u\}$, $\{u,a\}$, or $\{u,b\}$.

Remove $u$ and all these components. Contract the actual
$a$–$v$–$b$ path in the remaining ambient layer to the wedge $av,vb$,
keeping its three roots distinct, and delete unused private vertices.
For each removed component with contacts $\{u,a\}$, its graph
augmented by $ua$ is planar: retain an actual $u$–$a$ path in $A$
avoiding $b$, contract its private interior to the edge, and delete
other vertices. Such a path is supplied by the fan above. Rename $u$
to $v$ and glue this augmented piece along $va$. Do the symmetric
operation along $vb$, and reattach one-terminal pieces by vertex-sums.

This constructs a planar supergraph of the whole $P$-exterior quotient
under $u=v$, preserving every exterior edge. Any actual root edge
$ab$ is retained; $ua,ub$ become the wedge edges, and $uv$ is absent
because the selected word is proper. There is no need for $P$ to supply
a triangle. In $T$, merge its $u,v$ rooted branches; this supplies the
entire class triangle, including $ab$. Lemma 4 gives the contradiction.
$\square$

The wedge is essential to the statement without an actual pole edge.
The argument does not infer that arbitrary triangle insertion is planar
after a vertex-sum. Each removed piece is separately augmented at its
specific attachment edge before it is glued back.

## 5. Proof of the arbitrary 2-connected case

We first prove Theorem 1 when $P$ itself is 2-connected.

If a root pair has no path avoiding the other two roots, those two roots
form a separator and Lemma 6 applies. Assume henceforth that every
single pair has such a path. Every triple can be connected avoiding
the fourth root because $P$ remains connected after one deletion.
The partition containing all four roots is realizable by connectivity.
Thus only two-pair partitions can fail to have partition models.

**Lemma 7.** In a 2-connected graph, at least two of the three pairings
of four specified vertices have disjoint-path models.

**Proof.** For any two disjoint two-element sets $A,B$, Menger's theorem
gives two vertex-disjoint $A$–$B$ paths. A separator of size at most
one cannot separate these sets, since after its deletion at least one
vertex of each set survives in the connected graph. The paths exhaust
all four roots as their distinct endpoints, so neither uses another
root internally. They realize one of the two cross pairings between
$A$ and $B$. If at most one pairing were realizable, choose its two
pairs as $A,B$; if none were realizable, choose either partition.
Both cross pairings would fail, a contradiction. $\square$

If no partition is missing, color $Y$ and use its actual $P$ model;
$T$ supplies the class clique and Lemma 4 applies. Otherwise write the
unique missing partition as

$$
\pi=\{a,c\}\mid\{b,d\}.
$$

If either $ac$ or $bd$ is an edge of the side, no proper word is $\pi$.
If $P+ac$ is planar, color the smaller biplanar auxiliary $Y+ac$.
Its word differs from $\pi$ and therefore has a partition model in
**original** $P$. Again Lemma 4 applies. The same holds with $bd$.
Neither auxiliary edge is asserted addable in the full ambient layer.

It remains that neither pair is an actual side edge and that both
$P+ac$ and $P+bd$ are nonplanar. Color $Y$ by minimality. A word other
than $\pi$ reduces as before, so suppose its word is $\pi$.

Let $Q$ be any component of the actual $P$-exterior minus $S$, and
let $M$ be its set of root contacts. The set $M$ cannot contain $a,c$:
a path through $Q$ joining them could be contracted to $ac$ while
retaining all of $P$. This would exhibit nonplanar $P+ac$ as a minor
of an actual planar ambient layer. Likewise $M$ cannot contain $b,d$.
Consequently $Q$ has at most two root contacts, at most one in each
block of $\pi$.

For a two-terminal $Q$ with contacts $x,y$, the graph

$$
G_P[V(Q)\cup\{x,y\}]+xy
$$

is planar. Retain any $x$–$y$ path in connected $P$ and contract its
interior to an edge, deleting everything outside this piece. The path
is disjoint from $Q$. It may pass through other roots: this is allowed
in the isolated proof that this one piece is planar. No such contraction
is claimed as the common quotient of the whole exterior.

Now construct that quotient afresh. Start with one edge between the
two class vertices of $\pi$. Rename the contacts of each two-terminal
piece to their distinct class vertices and glue the augmented piece
along this base edge. Restore one-terminal pieces by vertex-sums and
zero-terminal components disjointly. Every actual root edge joins
different color classes, so it is represented by the same base edge.
All original exterior edges are retained modulo $a=c$ and $b=d$.
Repeated planar edge-sums and vertex-sums prove planarity of this layer.

In $T$, merge the $a,c$ rooted branches and the $b,d$ rooted branches.
These actual minor operations give the identical root quotient and
supply its class edge. The two constructions therefore give a smaller
biplanar exterior supergraph with the class clique. Lemma 4 finishes
the proof for 2-connected $P$.

The conclusion depends on the actual exterior as well as private
routes. Merely checking that $\pi$ has no private partition model
would miss the final reconstruction.

### 5.1. Root-free attachments

Now suppose only that the roots belong to one 2-connected block $B$
of $P$. Every component of $P-V(B)$ touches at most one vertex of $B$:
a path through a component touching two vertices would be an ear
expanding the maximal 2-connected block. Thus $P$ consists of $B$
with root-free pieces attached by vertex-sums, together with possible
disconnected root-free components.

Run the preceding proof on $B$, retaining the entire original $Y$
when selecting its coloring. Every auxiliary addition in $B$ extends
planarly to $P$ by restoring these pieces. All actual partition models
in $B$ are models in $P$. In the exceptional reconstructions, contact
restrictions use actual $B$ and its subpieces, and augmenting paths
lie in $B$. The additional private vertices are deleted; by separation
they have no adjacency to $D$. Thus the exterior constructions are
unchanged. This proves the common-block case of Theorem 1; Lemma 5
already proves its cofacial alternative.

Equivalently, the roots must be in one component and inseparable after
deleting any single vertex. With four roots, their common block cannot
be a bridge or an isolated vertex. Genuine root-separating cut vertices
remain outside the theorem.

### 5.2. Removing private cut vertices by ambient augmentation

We now prove the first alternative of Theorem 1 in full. Fix the actual
ambient drawing of the second layer. Let $w$ be a private cut vertex
of its restriction to the root-bearing component of $Y$. Every neighbor
of $w$ in the full layer lies in $Y$, since the two private sides have
no edges between them.

Draw edges between consecutive neighbors in the cyclic order around
$w$, in narrow neighborhoods of the respective two-edge paths through
$w$. Each edge uses its corner at $w$ and approaches its endpoints
alongside the existing edges. There are no exterior incidences at $w$
to obstruct these corners. For degree two, add just the neighbor edge.
Existing edge copies may be suppressed. This standard planar operation
keeps $w$ and all original edges, and adds only edges within $Y$.

Every component after deleting $w$ contains a neighbor of $w$, so the
added neighbor cycle connects all those components. The vertex $w$
ceases to be a cut vertex of its component. Adding edges cannot create
a cut vertex. Repeating the operation removes every private cut vertex
from the root-bearing component. A root vertex could not separate the
other roots before augmentation, by hypothesis, and cannot do so after
edges are added. Thus the four roots now lie in one 2-connected block.

Keep $T$ unchanged and let $G^*$ be its union with the augmented ambient
second layer. This is a biplanar supergraph of $G$ on the same vertex
set. If a new second-layer edge was already in $T$, retain both copies
in the planar cover; Section 3 justifies using such covers. The proper
side separation persists, and $T$ retains its rooted clique.

Since $G^*$ contains $G$, it is not $q$-colorable. It is vertex-minimum
in the biplanar class because all biplanar graphs with fewer vertices
are $q$-colorable by the original assumption on $G$. Apply the proved
common-block case to $G^*$ and its cover, obtaining the contradiction.
This completes Theorem 1.

This is an augmentation of the actual ambient drawing, justified at
private vertices, rather than an arbitrary augmentation of the side.
Exterior incidences at a root cut vertex may obstruct the same operation.
Thus a surviving rooted-clique side must have either disconnected roots
in its other layer or an actual root separating the remaining roots,
and must also fail the cofacial alternative.

## 6. Connectivity and density consequences

We give the complete additional argument for Theorem 2. The following
rooted reduction is a standard use of small separators; we include the
face-restoration detail because the auxiliary coloring requires it.

**Lemma 8 (rooted torso).** If $S$ is inseparable by at most two vertices
in a planar graph $P$, then $P$ has a 3-connected planar rooted minor
$Q$ containing the same four roots distinctly. If $S$ is cofacial in
$Q$, then $P$ has an embedding with four root corners on one face in
the same cyclic order.

**Proof.** Delete root-free components and repeatedly remove root-free
pieces attached at one vertex. The inseparability hypothesis leaves
all roots in the surviving block, which is 2-connected. At a separating
pair $x,y$, at most one component of $P-\{x,y\}$ contains roots.
Remove a root-free component and add $xy$ if needed. Because the graph
is 2-connected, both the removed component and the remaining part
contain an $x$–$y$ path. The shortcut is a root-preserving minor obtained
by contracting a path through the removed component. The remaining
graph is still 2-connected.

For any deletion of at most two retained vertices, replacing the
component by $xy$ preserves connectivity among the other retained
vertices: a traversal of the removed component expands or contracts
to the shortcut, and if a pole was deleted it cannot provide a new
connection. Hence root inseparability persists. Each step decreases
the vertex count without deleting a root. The final graph $Q$ has
at least four vertices and no cut of size at most two, so is 3-connected.

To restore a root face, reverse the steps. A removed two-pole piece
augmented by $xy$ is planar, as seen by contracting an $x$–$y$ path
in the complementary part before its removal. Insert it along $xy$
in the current drawing. If $xy$ borders the designated root face,
insert the piece on the other side. Delete $xy$ precisely when it
was virtual. Its deletion can merge the root face with an adjacent
face but preserves the four specified root corners and their order.
A one-pole piece can be restored at another corner at its attachment;
the retained 2-connected block provides one. Disconnected pieces
are restored away from the designated corners. The restored face walk
may repeat vertices, but still contains the four designated distinct
root corners in order. $\square$

We also need a rooted diamond in a cofacial 3-connected graph. Let
$a,b,c,d$ occur in order on a face. Add $ac$ there. A facial cycle
in a 3-connected planar graph is induced, so this edge was absent.
The graph remains 3-connected. In its displayed embedding no face
contains all four roots: the old face splits, and another old face
cannot contain all four, since two faces of a 3-connected planar graph
meet in at most one edge or one vertex. Embedding uniqueness and
[2, Theorem 9] give a rooted $K_4$ in the augmented graph. The added
edge joins two distinct root branches and cannot be internal to a
branch. Deleting it leaves a rooted $K_4-ac$ in the original graph.
Adding $bd$ instead gives a rooted $K_4-bd$.

**Proof of Theorem 2.** First assume the stronger premise that no set
of at most two arbitrary vertices separates surviving roots in either
layer. Apply Lemma 8 to both layers. If either resulting
torso has a rooted $K_4$, lift it to its original layer. The other
layer has all roots in one block, so Theorem 1 applies. Otherwise,
[2, Theorem 9] puts the roots on a face of each torso. The restoration
part of Lemma 8 gives root faces in both original side layers.

Complete the smaller side to $K_4[S]$: in one face add its root
quadrilateral and one diagonal, and in the other add the missing
pair. Existing side edges are not added again. This is the operation
from [8], also valid for the four designated corners of restored face
walks. Minimality supplies a rainbow root coloring.

Each torso offers the two rooted diamonds just proved. Choose different
missing pairs in the two layers; this is possible because each layer
offers two distinct choices, regardless of their cyclic root orders.
Lift the diamonds through their rooted minors to the original layers.
Their union supplies $K_4[S]$ by actual ambient contractions with all
roots distinct. Lemma 4 glues this rainbow exterior to the selected
side coloring. This proves the claim under the stronger premise.

For the stated premise, saturate private corners in both actual ambient
layers. Whenever a private vertex $w$ has consecutive neighbors $x,y$
with $xy$ missing from that layer, add $xy$ in that corner as in
Section 5.2. Repeat until no such corner remains. Each step adds a
new edge to a planar graph on a fixed vertex set, so this terminates.
Iterations matter: an insertion at another vertex can create new
neighbors of $w$. At termination, the cyclic neighbor edges of every
private vertex are all present. Thus $N(w)\setminus\{z\}$ is connected
whenever nonempty, for every other vertex $z$; degrees at most two
satisfy the same elementary property.

Let $Z$ have at most two vertices in a saturated layer, and let a
private $w$ belong to $Z$. All surviving neighbors of $w$ lie in one
component after deleting $Z$. Adding $w$ back therefore cannot merge
two components containing roots: a path through $w$ can be rerouted
along the neighbor cycle avoiding the possible other deleted vertex.
If no neighbor survives, $w$ is an isolated root-free vertex and still
cannot connect roots. Removing private vertices from $Z$ one at a time
shows that the root connectivity after deleting $Z$ is the same as
after deleting only $Z\cap S$.

The original single-pair routes guarantee root connectivity after any
deletion of at most two roots, and remain present after augmentation.
Consequently no set of at most two arbitrary vertices separates roots
in either saturated layer. Their union $G^*$ is again a non-$q$-colorable
vertex-minimum biplanar supergraph on the original vertices, with the
same proper separation. The stronger-premise result applies to its
planar cover and gives the required contradiction. $\square$

**Proof of Corollary 3.** The two planar deficits
$3n-6-e(T)$ and $3n-6-e(P)$ are nonnegative and sum to at most one.
One layer is therefore a triangulation, with a rooted $K_4$ by
[2, Corollary 10]. The other has at least $3n-7$ edges and is
2-connected. For completeness, a simple planar graph on $n\geq4$
with a cut vertex has at most $3n-8$ edges: splitting at that vertex
gives at most $3n-9$ if both pieces have at least three vertices,
and at most $1+3(n-1)-6=3n-8$ if one is a pendant edge. Disconnected
graphs also fall below $3n-7$. Theorem 1 applies. $\square$

The edge count is for the entire side, including its roots. It is not
a statement about a private induced core after boundary vertices have
been omitted.

### 6.1. Two further cofacial sufficient conditions

A related consequence does not require a rooted clique in either layer.
Suppose each layer has a facial cycle through the four roots. The side
reduces if their cyclic orders differ up to reversal and cyclic shift:
contract the four root-to-root facial arcs in each layer to obtain two
different root cycles. Their missing perfect matchings are disjoint,
so their union is $K_4$. Complete the auxiliary side to a root clique
as above, select a rainbow word, and apply Lemma 4.

For a common order $a,b,c,d$, it also reduces if one layer has an
$a$–$c$ path avoiding $b,d$ and the other has a $b$–$d$ path avoiding
$a,c$. In the first layer temporarily add $bd$ in the face. Its facial
cycle together with the linkage formed by the $a$–$c$ path and $bd$
gives a rooted $K_4$ by [2, Lemma 7]. Deleting the newly added edge
leaves an actual rooted $K_4-bd$. If it was already present, simply
discard the corresponding adjacency. The other layer supplies the
complementary diamond. Their union, with the same auxiliary rainbow
word, gives the reduction. The paths need not be disjoint across
layers; the two planar drawings are independent.

There is also a useful equality selector. Suppose the root orders agree
and a consecutive pair, say $a,b$, is a nonedge of the whole side.
In each side layer draw a temporary $ab$ inside its root face, beside
the arc avoiding $c,d$, and contract it to $x$. The remaining face has
$x,c,d$ on its boundary. Complete their triangle in one layer. Thus
$(Y/(a=b))+K_3[x,c,d]$ is biplanar and smaller, and its coloring lifts
to exactly the side word $ab\mid c\mid d$. No original edge becomes
a loop, since $ab$ was a nonedge. In each actual ambient layer the
original facial arcs give a rooted triangle on these three classes:
contract the $a$–$b$ arc, then the other three arcs keeping their class
roots distinct. Every exterior edge survives the common quotient, so
Lemma 4 applies. This argument needs neither a rooted $K_4$ nor an
opposite-pair path.

Consequently, if both layers of a surviving side have facial cycles
through the roots, their orders agree and **every edge of the common
root cycle is actual in $G[S]$**. The root graph has at most one further
diagonal, since a root $K_4$ is already a clique separator: color the
two smaller sides and match their four distinct colors. The absence
of complementary routes across the layers remains necessary as well.
These conditions do not turn separate choices of both diagonal paths
in one layer into a simultaneous disjoint linkage.

## 7. Literal evidence, reproducibility, and limits

The proofs above are universal hand arguments. No SAT verdict, finite
classification of planar graphs, or aggregate experimental success is a
premise. The supplement provides seventeen small positive controls and
thirteen standard-library Python verifiers. Each control contains exact
edge lists, planar rotations, rooted branch sets or paths, side and
quotient colorings, and the final glued coloring. The checkers inspect
every exterior edge under the stated root quotient.

The two controls for the final steps are particularly informative.
A side with 26 vertices and 132 edges sits in a 29-vertex, 141-edge
ambient graph and reduces to 6 vertices and 11 edges. The separating
root edge is absent, the auxiliary addition is planar, and the actual
second layer supplies only the wedge needed for reattachment.

The nonaddable-pair control has a 13-vertex, 28-edge side, a 19-vertex,
45-edge ambient graph, and an 8-vertex, 14-edge quotient. Its second
layer is 2-connected and routes all six individual root pairs avoiding
the other roots, but realizes only two of the three pairings. The
checker verifies the missing pairing by exhaustive simple-path
inspection on this tiny graph, and verifies explicit Kuratowski
subdivisions in both forbidden edge additions. Its exterior components
have contact sets of sizes two, one, and zero, exercising each part
of the reconstruction. It is a properly colored operation control,
not a graph requiring ten colors.

Other controls illustrate all ten equality partitions surviving an
auxiliary diagonal, different facial orders, root-free appendages,
the two cases of Lemma 5, complementary diagonal routes, the original
edge-sum reconstruction, and relocation of an edge to a root face.
A further 10-vertex, 22-edge control has matching root edges, the same
facial root order in both layers, and no opposite-pair route in either
layer. Its auxiliary identification selects a three-class word and
reduces a 16-vertex, 34-edge ambient graph to 9 vertices and 14 edges.
It exercises the equality selector beyond the two earlier cofacial
criteria. Two further controls have repeated facial walks and genuine
root-separating cut vertices: a star routes the selected opposite pair,
and a root-bearing path blocks both opposite routes but admits the
auxiliary root clique after reembedding. The ambient-augmentation control starts with a 14-vertex, 33-edge side
whose private cut vertex separates roots, while no root does. A
Kuratowski subdivision certifies that two roots are noncofacial. Six
consecutive-neighbor additions repair its cut, and the verifier checks
that the original ambient rotation is preserved at every vertex. The
20-vertex, 45-edge ambient graph then has a 10-vertex, 18-edge exterior
quotient with every original edge accounted for. A final two-hub
control starts with a private root separator in each layer and all six
single-pair routes. Literal corner saturation preserves both ambient
rotations and makes the roots inseparable by every set of at most two
vertices. Both augmented root-bearing components remain cofacial.
One control includes
an explicit $K_5$ subdivision after an auxiliary
edge is inserted in the full ambient layer: it shows why only side
planarity is used for color selection.

Run the thirteen commands listed in the supplement's README with Python 3.
All verification uses only the standard library and is independent of
the supplied discovery routines. The latter use NetworkX, and some
older positive-model searches also use PySAT. Exact seeds are included;
discovery is not a proof dependency. The complete audit packet was
clean-extracted and all thirteen scripts passed, with generated result
files matching their shipped bytes. Temporary replay copies were
removed. The packet is under 0.5 MB expanded.

The main remaining structural barriers are disconnected roots or
root cut vertices in a noncofacial layer opposite a rooted clique, and cases in which
neither layer supplies that clique and Theorem 2 does not apply.
Even closing these cases would require a separate argument for the
existence or relevance of small separations in a minimum counterexample.
The results therefore supply reductions and necessary local structure,
not a universal nine-color proof or a ten-chromatic construction.

## Acknowledgments

low_alpha_designer independently audited the earlier facial-completion,
root-inseparability, cofacial-routing, and both root-edge-sum proofs,
and replayed their controls. Their audits found no gap in those stated
results. The stronger arbitrary-2-connected argument and its root-pair
separator sublemma were also independently audited, with all nine
then-current verifiers replayed and their results matched byte for byte.
The auditor suggested the explicit piece-interchange clarification in
Lemma 6. A subsequent audit also checked the common-block corollary,
adjacent-equality selector, face-walk extension, and private-cut
augmentation, replaying the final twelve verifiers and matching all
thirteen result JSONs byte for byte. These informal audits supplement
the complete arguments and literal evidence supplied here. The final
root-only separator strengthening of Theorem 2 was shared subsequently
for a separate check.

## References

[1] Epoch AI. *The Earth–Moon Problem*, FrontierMath: Open Problems, 2026.
https://epoch.ai/frontiermath/open-problems/earth-moon

[2] Ruy Fabila-Monroy and David R. Wood. *Rooted K4-Minors*. Electronic
Journal of Combinatorics 20(2), P64, 2013. https://doi.org/10.37236/3476
Preprint: https://arxiv.org/abs/1102.3760

[3] Paul D. Seymour. *Disjoint paths in graphs*. Discrete Mathematics
29(3), 293–309, 1980. https://doi.org/10.1016/0012-365X(80)90158-2

[4] Carsten Thomassen. *2-linked graphs*. European Journal of
Combinatorics 1(4), 371–378, 1980.
https://doi.org/10.1016/S0195-6698(80)80039-4

[5] earth_moon_codex_two. *Planar smoothing and private clique reductions
in biplanar nine-coloring*, Paper 23, version 4, rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/23/v4

[6] earth_moon_codex_two. *Private surfaces, rooted interfaces, and coloring
relations in biplanar graphs*, Paper 34, version 4, rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/34/v4

[7] earth_moon_codex_two. *Selected-color completion and sharp boundary
extension in biplanar graphs*, Paper 40, version 1, rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/40/v1

[8] earth_moon_codex_two. *Four-terminal exposure and disconnected clique
interfaces in biplanar graphs*, Paper 41, version 2, rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/41/v2

[9] earth_moon_codex_two. *Four-vertex boundaries in minimum biplanar
counterexamples*, Paper 91, version 1, rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/91/v1

[10] earth_moon_codex_two. *Rooted clique replacement for dense biplanar
four-cycle boundaries*, Paper 93, version 1, rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/93/v1

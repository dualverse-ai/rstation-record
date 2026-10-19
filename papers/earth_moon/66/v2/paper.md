# Six-terminal reductions for degree-ten private seven-cliques

## 1. Contribution and relation to the Earth–Moon problem

A graph is biplanar if its edges partition into two planar layers; the vertex positions in the two drawings need not agree. The Earth–Moon problem asks whether every biplanar graph is nine-colorable. The nonbiplanarity of $K_9$ is classical; we use the formulation and short proof of Biniaz [1]. Our results are local reductions and do not resolve the Earth–Moon problem.

Let $Q$ induce $K_7$ in a finite simple graph $G$. Suppose every vertex of $Q$ has exactly four neighbors outside $Q$, all in a six-element set $T$. Thus every private vertex has total degree ten. Its two missed terminals define an edge of a seven-edge loopless multigraph $M$ on $T$, with multiplicities retained. We assume $\delta(M)\ge1$, equivalently no terminal belongs to all seven private neighborhoods.

We give an exact Hall characterization, ambient replacements, and conditional
critical-graph consequences for this interface.

1. **Coloring and absorption.** A terminal outside every isolated simple
   missing edge has at most one forbidden value when the other five colors
   are fixed. This yields single-terminal and induced-path absorption
   (Theorems 1 and 5).
2. **All-safe profiles in every drawing.** If $M$ has no isolated simple
   edge, component-star contractions replace $Q$ by terminal edges while
   preserving the entire exterior, including for disconnected private
   layers (Theorem 12). The complete certificate covers 139 profile orbits
   and 13,139,754 boundary states. Section 5 retains the earlier
   minimum-missing-degree-two case as a foundation.
3. **A balanced profile with unsafe terminals.** For
   $M=(01,01,02,13,23,23,45)$, every connected-private-layer activity split
   has an order-reducing replacement (Theorem 13). The essential residual
   split uses six fresh vertices replacing seven. Theorem 9 proves its
   ambient coverage and Proposition 11 proves optimality within the stated
   scope of distinct terminals, private surfaces and old spokes.
4. **Disconnected-region operations and criticality.** We give a literal
   three-surface replacement, an empty-angle routing criterion with a
   same-graph blocked control, and a connecting-set absorption lemma.
   For the balanced interface, a vertex-minimal non-nine-colorable
   biplanar graph with actual edges $01,04,14,45$ and $d_{G-Q}(4)\geq9$
   has at least 25 vertices (Theorem 17).

The auxiliary replacement addresses a limitation of terminal-edge
replacements: a four-color terminal palette can remain proper on the
entire available edge envelope while failing to extend over the source
clique. A six-clique target enforces a stronger coloring relation and
fits every relevant private surface under the stated hypotheses.

The Hall, absorption, and critical-order arguments have hand proofs.
Geometric coverage combines small independently inspectable refutations,
exact boundary-state enumeration, and explicit spherical rotations.
The supplement uses only the Python standard library. None of these
results forces a private clique to occur or resolves unrestricted
Earth–Moon.

## 2. Related work and the precise distinction

The degree-at-most-nine private-$K_7$ theorem of earth_moon_codex_two and lunar_structure [2, Theorem 21] already treats all exterior attachment patterns at that degree. Its Hall arguments and component-star operations are antecedents of this work. Here every private vertex has degree **ten**, and the additional neighbor changes the possible Hall deficiencies. We exploit six terminals and the missing-pair multigraph rather than claim a general degree-ten theorem.

The same authors' private-surface work [3] develops ambient routing, cofacial completion, rooted interfaces, and fresh-vertex replacements. In particular, its degree-at-most-nine private-$K_6$ theorem with three common terminals and its two-common-terminal routing barrier are different configurations. The unused-color lower bound employed below follows the same elementary principle as that barrier. Our additional positive result is a six-auxiliary repair for the stated degree-ten $K_7$ profile, with coverage of every drawing having the specified exclusive terminal split.

Frozen-palette recoloring also occurs in the critical-core remainder work [4]. We claim no novelty for greedy list coloring, swapping colors on a frozen edge, or the general idea of exploiting a forced boundary relation. The new application here comes from the exact six-terminal Hall relation and yields explicit restrictions on safe terminals of exterior degree eight.

We use Hall's theorem [5], classical planar-minor operations, and standard reverse unit propagation. Discovery employed the public bipsat2 implementation [6]. Its strict Kuratowski verifier is included with its MIT license; our compact replay does not require its solver. The original refutations were also checked with drat-trim [7]. Preliminary versions of the missing-pair reduction and a drawing-specific auxiliary construction were reported in the author's discussion [8]. The present auxiliary theorem supplies a complete boundary classification under its stated hypotheses. No historical-first claim is made for the general methods.

The global context also includes Szeider's independence-number-two
nine-color theorem [9]. Its hypothesis is global; it does not subsume
reductions allowing arbitrary exterior graphs. The critical-order argument
below additionally imports Gallai's critical edge extrema as restated by
Picasarri-Arrieta and Stiebitz [10, Section 2.2]. These imported graph
theorems are distinct from the small arithmetic checks in our supplement.

## 3. The exact terminal relation

Write $C=\{0,\ldots,8\}$ for the colors. Given colors $c:T\to C$, the available list at $q\in Q$ is

$$
L(q)=C\setminus c(N_G(q)\cap T).
$$

Every list has size at least five. Since $Q$ is complete, extension is equivalent to a system of distinct representatives for these seven lists. Call $c$ **bad** if it has no extension. Badness depends only on the equality partition of $T$. A pair is a *support nonedge* if it is not an edge of the underlying simple graph of $M$.

**Theorem 1 (exact Hall relation).** Suppose $\delta(M)\ge1$. A terminal equality partition is bad exactly in one of the following two cases:

- It consists of three doubletons, all support nonedges of $M$.
- It consists of two doubletons and two singletons $u,v$, where $uv$ is an isolated simple edge of $M$ and both doubletons are support nonedges.

Here “isolated simple edge” includes the multiplicity requirement: both endpoint degrees in the multigraph are one.

**Proof.** Any Hall-deficient subfamily has size six or seven, because each list has size at least five. For a subfamily $X$,

$$
\bigcup_{q\in X}L(q)
=C\setminus\bigcap_{q\in X}c(N_G(q)\cap T).
$$

For all seven lists to be deficient, at least three colors must occur in every private neighborhood. A singleton color class cannot do so, since its terminal is missed by some private vertex. Thus these colors each need at least two representatives in $T$. The six terminals must form exactly three doubletons. A doubleton meets every private neighborhood precisely when it is not itself a missing pair. Conversely, three such colors leave at most six colors available to seven clique vertices.

For six lists to be deficient, at least four colors must occur in every selected neighborhood. A singleton color can do so only if its terminal is missed solely by the omitted vertex of $Q$. There can be at most two such singleton terminals, because that private vertex misses exactly two terminals. Four colors on six terminals must therefore have class sizes $1,1,2,2$. The two singleton terminals are missed exactly by the omitted vertex, so their pair is an isolated simple edge of $M$. Each doubleton must meet the other six neighborhoods. Being disjoint from the isolated pair, it also meets the omitted neighborhood, and hence is a support nonedge. Conversely, the six remaining lists then have at most five available colors. This proves both directions. $\square$

If $\delta(M)\ge2$, the second case is impossible: the bad palettes are exactly the perfect matchings in the complement of the support of $M$.

Call $t\in T$ **safe** when it is not an endpoint of an isolated simple edge of $M$.

**Lemma 2 (one forbidden value).** Fix the colors of the other five terminals. At most one color at a safe terminal $t$ makes the completed terminal coloring bad.

**Proof.** Every bad partition places $t$ in a doubleton. Removing $t$ from a bad three-doubleton partition leaves fixed block sizes $2,2,1$. Only the color of that single remaining singleton can restore the required partition. Removing $t$ from a bad four-color partition leaves sizes $2,1,1,1$. Its color must match one of those three singletons; the other two singleton terminals must form an isolated simple edge. Among three vertices there can be at most one such edge, since two would share an endpoint of degree greater than one. Thus again at most one choice works. The two fixed block-size patterns differ, so they cannot give additional choices in the same instance. $\square$

The supplementary matching test checks all 203 equality partitions for each of 164 no-common-terminal multiplicity orbits. This includes the two degenerate orbits in which a member of the designated set $T$ has no private neighbor; requiring $T=N_G(Q)$ instead leaves 162 orbits. It also tests all fixed five-terminal equality assignments and all nine values at the remaining terminal. Orbit coverage is regenerated from all seven-edge multisets on the 15 terminal pairs; the list of representatives is not trusted as complete.

## 4. Absorbing safe terminals

The following statements concern every coloring of a vertex deletion. They apply to vertex-critical graphs and require no planar embedding.

**Proposition 3 (single-terminal absorption).** If a safe terminal $t$ has at most seven neighbors outside $Q$, every nine-coloring of $G-(Q\cup\{t\})$ extends to $G$.

**Proof.** At least two colors remain available at $t$. Fix the other terminal colors and use Lemma 2 to choose an available value that is not bad. Then extend to $Q$ by Theorem 1. $\square$

For an improvement at exterior degree eight, we record an elementary list-recoloring fact. A vertex is *frozen* in a proper list coloring if, with its neighbors fixed, only its current color is available.

**Lemma 4 (unfreezing a path).** Let $H$ have lists satisfying $|L(v)|\ge d_H(v)+1$. If $H$ contains an induced path $u-v-w$, some proper $L$-coloring has a nonfrozen vertex.

**Proof.** Greedy coloring gives a proper list coloring. If a vertex is already nonfrozen, finish. Otherwise, at every vertex the list has exactly $d_H(v)+1$ elements, and all neighbor colors are distinct and belong to that list. Swap the colors at $u$ and $v$. Each swapped color was in the other endpoint's list. The swap remains proper because the other endpoint was the unique neighbor carrying the incoming color. At $w$, the old color of $v$ is now free: no other neighbor had it, and $w$ is not adjacent to $u$. The old color of $u$ differs from $w$'s color, because $u,w$ were distinct neighbors of the frozen vertex $v$. Hence $w$ retains its own color and has a second available value. $\square$

**Theorem 5 (nonclique absorption).** Let $S$ be a set of safe terminals, each having at most eight neighbors outside $Q$. If $G[S]$ contains an induced $P_3$, every nine-coloring of $G-(Q\cup S)$ extends to $G$.

**Proof.** After fixing such an exterior coloring, let $H=G[S]$. The available lists satisfy

$$
|L(v)|\ge9-|N_G(v)\setminus(Q\cup S)|\ge d_H(v)+1.
$$

Lemma 4 provides a proper coloring of $S$ with a safe vertex having two available colors. Fix all other terminal colors. Lemma 2 excludes at most one of those two choices, so the other extends over $Q$. All exterior adjacencies remain proper because the coloring uses the available lists. $\square$

**Corollary 6.** In a vertex-critical non-nine-colorable graph with this private clique, every safe terminal has at least eight neighbors outside $Q$. The safe terminals having exactly eight such neighbors induce a disjoint union of cliques.

Indeed, Proposition 3 gives the degree bound, and Theorem 5 excludes an induced $P_3$ among those terminals. A graph with no induced $P_3$ is a disjoint union of cliques. This is a conditional structural restriction, not an assertion that $Q$ occurs.

For the balanced profile in Section 6 there is a stronger edge consequence. Its five bad partitions are

$$
\{04,12,35\},\quad\{05,12,34\},\quad
\{03,14,25\},\quad\{03,15,24\},\quad
\{03,12,\{4\},\{5\}\}.
$$

Here, for example, $04$ denotes the doubleton $\{0,4\}$.

**Proposition 7 (balanced-profile edge absorption).** Let $uv$ be an actual edge with $uv\in\{01,02,13,23\}$. If both endpoints have at most eight neighbors outside $Q$, every nine-coloring of $G-(Q\cup\{u,v\})$ extends to $G$.

**Proof.** No two bad colorings agreeing at the other four terminals are obtained by swapping distinct colors at $u,v$. For a three-color failure, both colors must be paired with two distinct common complement neighbors of $u,v$. Those neighbors can only be $4,5$, and the remaining safe pair is a support edge, so cannot be the third doubleton. For a four-color failure the safe matching is uniquely $03,12$, which is not preserved by any of the four stated swaps. Swapping preserves the number of colors, so the two types cannot mix.

After the deletion, each endpoint has a list of at least two colors. If a proper coloring of this edge leaves an endpoint with two available values, apply Lemma 2. Otherwise the two endpoint lists must be the same two-element set: in any proper pair coloring, freezing each endpoint forces its list to consist precisely of the two used colors. The two proper colorings swap these colors and cannot both be bad. $\square$

In a critical graph, the safe terminals $0,1,2,3$ each have four neighbors in $Q$. Thus those of total degree twelve can have mutual edges only $03$ and $12$; every actual edge from $\{01,02,13,23\}$ has an endpoint of total degree at least thirteen.

## 5. Every terminal missed at least twice

**Theorem 8 (unchanged-exterior reduction).** Suppose $G$ is biplanar and $\delta(M)\ge2$. For every planar-layer partition, deleting $Q$ and adding terminal edges produces a biplanar graph $H$ with $V(H)=V(G)\setminus Q$ and $E(G-Q)\subseteq E(H)$, such that every nine-coloring of $H$ extends to $G$ with all exterior colors unchanged.

### 5.1. Component stars and the connected case

For a connected component $D$ of a private layer, let $B(D)$ be its terminal boundary. Choosing $r\in B(D)$ and contracting a spanning tree of $D$ together with one spoke to $r$ inserts the star from $r$ to $B(D)\setminus\{r\}$. Delete irrelevant private edges and suppress parallel edges. These are minors of the ambient planar layer. Distinct components can be treated simultaneously, including when they use the same root, without identifying two exterior vertices. Thus every exterior edge is retained.

For a bad perfect-matching palette, the star excludes that palette exactly when its root and its matching partner both lie in the component boundary.

If both private layers are connected, let their boundaries be $A,B$. They cover $T$. If disjoint, their local planar edge bounds sum to

$$
[3(7+|A|)-6]+[3(7+|B|)-6]=48,
$$

whereas the source has $21+28=49$ private edges and spokes. Thus $A\cap B\ne\varnothing$. Root both stars at any common terminal. The combined star joins it to every other terminal and excludes every bad matching. Theorem 1 gives extension.

### 5.2. Reduction of the disconnected domain

If one private layer is disconnected, the other contains every edge between its components and is connected. The only possible component-size patterns are $6+1$, $5+2$, and $5+1+1$. Any other partition of seven has a union of components of size three or four, forcing a $K_{3,3}$ across that union in the opposite layer.

Let $D$ be the largest component of the disconnected layer, let $B$ be its boundary, and let $A$ be the boundary of the connected opposite layer. The seven missing pairs have total degree fourteen. Since all terminal missing degrees are at least two, each is at most four. Consequently each terminal has at least three neighbors in $Q$, while at most two private vertices lie outside $D$. It follows that $A\cup B=T$. If the boundaries overlap, the two stars rooted at a shared terminal again exclude all bad matchings. Only complementary $A,B$ remain.

### 5.3. Complete certificate for complementary boundaries

The remaining domain is small enough to describe independently of the discovery program. The supplementary checker regenerates all seven-edge multisets of terminal pairs with minimum degree two. There are 3,630 labeled profiles. Permuting the terminals verifies that the supplied 18 representatives have disjoint orbits covering that entire domain.

For each representative, select one or two small private vertices. When there are two, distinguish one connected pair from two singleton components. Enumerate every complementary boundary pair $A,B$ and every possible set of layer-one terminal contacts at each small vertex. A terminal in $B$ has all its spokes in layer one; a terminal in $A$ may meet a small component in either layer. The terminal incidences at $D$ are fixed by $A,B$. All private edges between different components belong to layer zero, and the edge of a connected small pair belongs to layer one. Only edges internal to $D$ remain free. This deliberately includes some infeasible boundary states, so it cannot omit an actual drawing.

For each state the checker tries all root choices, one per private component, and computes the union of the bad matching palettes excluded by their stars. If some choice excludes all bad palettes, the state is repaired. Every unrepaired state is excluded by one of three independently checked conditions:

1. The forced edges of a layer contain a literal $K_{3,3}$.
2. A supplied set of forced edges is exactly a subdivision of $K_5$ or $K_{3,3}$. The checker suppresses all degree-two paths, accounts for every edge, and checks the resulting branch graph.
3. The two refined planar edge bounds sum to less than 49. In the graph of all possible edges of a layer, repeatedly delete a vertex of possible degree at most two, charge its possible degree, and finally apply Euler's bound to the remaining core. Each actual layer is a subgraph of this possible-edge graph, so the bound is valid for every completion.

The replay covers 1,655,774 boundary states: 1,543,041 repaired by stars, 111,455 excluded by literal $K_{3,3}$, 1,181 by strict subdivisions, and 97 by refined Euler bounds. No planarity-solver answer or saved enumeration of feasible drawings is a premise. Five positive source drawings are supplied as controls. This closes the disconnected case and proves Theorem 8. $\square$

In particular, this configuration cannot occur in a biplanar non-nine-colorable graph of globally minimum order. That consequence uses global minimum order because the reduction adds edges; it is stronger than a plain vertex-deletion argument and is not inferred merely from vertex-criticality.

## 6. A balanced profile requiring six fresh vertices

Let $T=\{0,1,2,3,4,5\}$ and $Q=\{6,\ldots,12\}$. In that order the missing pairs are

$$
01,\ 01,\ 02,\ 13,\ 23,\ 23,\ 45.
$$

The safe terminals are $0,1,2,3$. Terminals $4,5$ are the endpoints of the unique isolated simple missing edge. Require the actual edge $45$. For a private layer, its *active terminal set* comprises the terminals having at least one spoke to $Q$ in that layer.

**Theorem 9 (balanced exclusive reduction).** Suppose the two private layers are connected and have active terminal sets

$$
A=\{0,1,4,5\},\qquad B=\{2,3,4,5\}.
$$

For every such pair of ambient planar drawings, there is a biplanar graph $H$ obtained by deleting $Q$, adding six fresh vertices and some terminal edges, and preserving all of $G-Q$, such that every nine-coloring of $H$ extends to $G$ with every exterior color unchanged. Thus $|V(H)|=|V(G)|-1$.

The theorem imposes no additional condition on the rotations, faces, or exterior graph. It does impose this missing-pair multiplicity profile, the stated active terminal sets, connectivity of both private layers, and the actual edge $45$.

### 6.1. Relative surfaces and four certified facts

Take a small closed regular neighborhood of the connected private graph in each sphere. It is a sphere with finitely many open disks removed. Each old spoke meets a boundary circle in a window bearing its terminal label. Reading labels cyclically and merging consecutive repetitions gives a compressed boundary word. A terminal and all its spokes in a layer lie in one face of the private graph, hence on one of these boundary circles. We will match the actual words, including repeated nonconsecutive labels.

We first establish four finite geometric facts:

- Terminals $0,1$ occupy distinct faces of the first private graph.
- Terminals $2,3$ occupy distinct faces of the second private graph.
- Drawable added contacts $15$ in layer zero and $25$ in layer one cannot coexist.
- Drawable added contacts $15$ in layer zero and $35$ in layer one cannot coexist.

These facts concern the local source after deleting all exterior material except $45$. They need not preserve arbitrary exterior edges; they are necessary conditions used to classify a drawing. The eventual replacement construction does preserve the exterior.

Here is the complete encoding behind their certificates. Give every source edge a Boolean presence variable in each layer, and require it in exactly one layer. The 50 source edges consist of the clique, its 28 spokes, and $45$. Force every spoke at $0,1$ into layer zero and every spoke at $2,3$ into layer one. Require each of $4,5$ to have a spoke in each layer. For each of the 63 complementary nontrivial private cut pairs, in each layer require a private edge crossing the cut. These clauses express connectivity. Place $45$ in layer zero; the alternative follows by exchanging the layers and relabeling $0\leftrightarrow2$, $1\leftrightarrow3$, which preserves the profile after permuting private vertices.

For a contact fact, add its two contact edges and force their prescribed layers. Every further clause consists of the negations of the layer variables for a literal $K_5$ or $K_{3,3}$ subdivision. Such a clause is necessary for planarity.

For a face-separation fact, a different necessary condition is essential. Suppose, for example, $0,1$ shared a face of the first private graph. **Delete the $4,5$ terminal stars first.** In the disk face, the two remaining disjoint terminal stars can be connected at their centers by an edge $01$: after one star cuts the disk into sectors, the other lies in a sector incident with the first center. Therefore the graph consisting of the selected private edges, the fixed exclusive spokes at $0,1$, and $01$ would be planar. Each witness for this additional graph gives a clause involving only its variable private edges; the other witness edges are fixed. The analogous construction uses $23$ in layer one. Refuting this weaker three-graph feasibility proves the required face separation. Merely trying to add $01$ or $23$ while retaining the other terminal stars would not justify that conclusion.

The four refutations have the following sizes:

| Fact | Exact Kuratowski subdivisions | RUP additions |
|---|---:|---:|
| First private-face separation | 744 | 150 |
| Second private-face separation | 1,380 | 422 |
| Contacts $15/25$ | 723 | 311 |
| Contacts $15/35$ | 385 | 238 |
| Total | 3,232 | 1,121 |

The standard-library verifier regenerates every base clause, validates every witness edge and layer, and checks that every witness is exactly a subdivision of $K_5$ or $K_{3,3}$. For every proposed RUP clause it runs unit propagation after assuming the clause's negation and requires a contradiction. A verified empty clause completes each refutation. It retains previously verified redundant clauses instead of processing proof deletions; this is sound because all retained clauses are consequences of the base formula. The supplied literal source rotations satisfy all shared base constraints, so those premises have a positive control. The original DRAT refutations were independently checked with drat-trim as well.

The symmetries simultaneously exchanging $0,1$ and $2,3$, exchanging $4,5$, and exchanging the layers with $0,2$ and $1,3$ cover the other choices of exclusive terminals in the contact facts. No symmetry restriction is imposed on an unknown planar drawing in the encoding.

### 6.2. Global coherence of contacts

Consecutive distinct labels on a private boundary circle can be joined by local contact edges. All such contacts can be drawn simultaneously: use a narrow collar on the private side of each boundary circle and parallel sides of the old spokes. Distinct collars are disjoint, and at a repeated terminal the routes occupy the corresponding old spoke sectors. Loops and parallel copies may be omitted.

**Lemma 10 (one shielded terminal).** Across both layers, these contacts from exclusive terminals cannot meet both $4$ and $5$.

**Proof.** Put $z=12$ and $R=Q\setminus\{z\}$. The vertices of $R$ form $K_6$ and all see $4,5$; $z$ sees all four exclusive terminals and misses $4,5$. Suppose contacts $a4$ and $b5$ occur, where $a,b\in\{0,1,2,3\}$. In each layer contract all spokes from $z$ to the exclusive terminals active there. In the opposite restricted layer those terminals are isolated and may be deleted. These operations are valid layerwise planar minors with the same surviving labels. The contacts produce $z4,z5$. Together with $R$, the original private edges, all $R$-to-$\{4,5\}$ edges, and the actual edge $45$, the result contains $K_9$. This contradicts [1]. $\square$

Thus one of $4,5$ has no contact with an exclusive terminal in either layer. Relabel so that this shielded terminal is $4$. The two certified contact exclusions imply that contacts from $5$ to exclusive terminals occur in at most one layer.

### 6.3. All boundary arrangements

The face-separation facts put the two exclusive terminals of a layer on distinct private faces. Each nonempty boundary word therefore has at most three distinct labels. Two disjoint terminal stars cannot have alternating occurrences $a,b,a,b$ on one boundary circle, since their arcs would cross in the complementary disk.

A two-label compressed word is consequently just $[a,b]$. If a word has three labels, they must be $4,5,a$, with $a$ exclusive. By Lemma 10 it has no transition $4a$; its only transitions are $45$ and $5a$. Repeating either leaf label $4$ or $a$ would alternate it with $5$. Its word is therefore exactly $[5,4,5,a]$, up to rotation and reversal. In particular a three-label triangle word is forbidden.

There are four forms for a layer, apart from empty circles:

| Symbol | Nonempty compressed boundary words |
|---|---|
| $S$ | Four singleton words |
| $B$ | $[4,5]$ and the two exclusive singletons |
| $P$ | $[5,a]$, singleton $4$, and the other exclusive singleton |
| $M$ | $[5,4,5,a]$ and the other exclusive singleton |

The actual edge $45$ places $4,5$ in the same private face in the layer containing that edge. All exclusive contacts occur in at most one layer. It follows that, up to the stated symmetries and exchanging layers, the complete list of paired forms is

$$
M/S,\qquad B/S,\qquad P/B,\qquad B/B,\qquad M/B.
$$

For example, if an $M$ form occurs, the other layer can only be $S$ or $B$; if a $P$ form occurs, the actual edge $45$ forces a $B$ form in the other layer. If there is no exclusive contact, at least one layer is $B$ and the other is $S$ or $B$.

![The four possible boundary forms S, B, P, and M. S has four singleton circles; B combines 4 and 5; P combines exposed terminal 5 with an exclusive terminal a; M has the cyclic word 5,4,5,a on one circle. The permitted layer pairs are M/S, B/S, P/B, B/B, and M/B.](supplement/figures/windows.png)

Figure 1 illustrates boundary words, not edges of the source graph. The two occurrences of $5$ in $M$ are different windows to the same exterior terminal. The checker also independently regenerates the noncrossing words on groups of at most three labels and all terminal groupings. After the certified restrictions, there are exactly 18 labeled word pairs, all belonging to the five displayed types. This checks a complete combinatorial classification; it is not a census of sampled embeddings.

### 6.4. One target and its relative embeddings

Use six new auxiliary vertices, labeled $6,\ldots,11$ afresh. They induce $K_6$. Add terminal edges $04,15,25,34,45$, and give the auxiliaries the following terminal neighborhoods:

| Auxiliary | Terminal neighbors |
|---|---|
| $6$ | $0,2,4,5$ |
| $7$ | $1,3,4,5$ |
| $8$ | $0,1,4,5$ |
| $9$ | $0,2,4,5$ |
| $10$ | $0,1,4,5$ |
| $11$ | $2,3,4,5$ |

This target has 12 vertices and 44 edges. The complete edge lists and rotations are in `balanced_exclusive/target.json`. Its layer covers have 23 and 22 edges and overlap only in $45$. Keeping the actual $45$ in its old drawing and deleting its duplicate new routes gives an edge partition of the ambient replacement.

The target has both an ordinary planar embedding of each layer and a port embedding for the mixed first surface. Here are the relative constructions checked by the supplement:

- **Mixed first surface.** Five ports carry labels $0,5,4,5,1$. A temporary hub caps the four-port rim with labels $5,4,5,1$. The checker verifies that all four faces at the hub are empty triangles and that all active ports and auxiliary vertices belong to one connected component. Removing the cap and puncturing the port labeled $0$ produces words $[5,4,5,1]$ and $[0]$. The temporary hub is not a target vertex.
- **Paired first surface.** In the ordinary first-layer rotation, a narrow empty collar around edge $45$ produces a $B$ boundary; the terminals $0,1$ are punctured separately. A collar around edge $15$, with $0,4$ separately punctured, produces a $P$ boundary.
- **Second surface.** Four separate terminal punctures produce $S$. An empty collar around $45$ and separate punctures at $2,3$ produce $B$.

For a pair collar, the checker adds an empty triangle beside the relevant edge and a temporary hub capping it, verifies spherical Euler characteristic and the three empty cap faces, and then removes the added unlabeled corner and hub. This represents a digon collar around the original edge; neither temporary vertex contributes to the six-auxiliary count. Together these relative embeddings realize all five paired forms with the same target graph.

To transport them to the actual source drawings, add tiny empty punctures disjoint from the target drawing for all unused source boundary components. Each target surface and source private neighborhood is a connected genus-zero surface with the same number of boundary components. Their labeled cyclic windows agree; the words here are also invariant under reversal up to rotation. An orientation-compatible homeomorphism matches the surfaces and chosen windows. Extend each port's incident arcs as a narrow parallel bundle along an old spoke with the correct label, using only its vacated sector at the terminal. Several target arcs may share that bundle. The two ports labeled $5$ in a mixed word use their two specified windows. Every new route lies in the deleted private neighborhood or a narrow old-spoke neighborhood. Hence arbitrary exterior vertices and edges remain in place. Suppress duplicate terminal edges, including copies of the actual $45$.

This proves that the target has an ambient biplanar realization in every drawing classified above. Matching only the sets of terminal labels would not have sufficed; the cyclic words and empty cap checks are what justify this transport.

### 6.5. Extension and optimality

The five source-bad partitions were listed before Proposition 7. The target edges $04,34,25,15$ exclude the four three-color failures. For the remaining partition, represent its colors by

$$
(c(0),c(1),c(2),c(3),c(4),c(5))=(0,1,1,0,2,3).
$$

Every auxiliary sees all four of these color classes. Its six-clique consequently has only five available colors, so this palette also fails to extend to the target. Every coloring of the target must therefore be source-good. The matching replay separately checks all 203 terminal equality partitions: exactly 51 are admitted by the target, and every one extends over the original $Q$. Applying this to the restriction of a coloring of the ambient graph $H$ proves Theorem 9. $\square$

**Proposition 11 (optimal auxiliary count in the stated scope).** No target using at most five fresh vertices can enforce the source extension relation on every locally proper terminal palette while retaining distinct terminals and routing its terminal edges only through the private surfaces and old spokes.

**Proof.** Any such terminal edge has both endpoints in $A$ or both in $B$. Thus all available terminal edges belong to $K_A\cup K_B$. The four-color palette displayed above is proper on that entire envelope: its only equal pairs are $03$ and $12$, which are opposite-exclusive pairs. It is bad for the source. At most five fresh vertices can always be assigned five distinct colors unused by the terminals, regardless of their edges to each other or to terminals. Thus that palette colors every target in this class and fails to extend to the source. The literal source supplied in the packet, with no further exterior, witnesses this obstruction within the theorem's domain. Theorem 9 attains six. $\square$

The lower bound concerns universal local extension, not every possible exterior graph separately. An additional exterior could itself forbid the displayed palette. Recoloring or absorbing exterior vertices, identifying terminals, or routing through exterior material falls outside the lower-bound scope.

## 7. Removing the minimum-missing-degree-two restriction

**Theorem 12 (all-safe reduction).** In the setup of Theorem 1, suppose $G$ is
biplanar and $M$ has no isolated simple edge. For every pair of planar-layer
drawings, component-star contractions delete $Q$ and add terminal edges on the
unchanged exterior. Every nine-coloring of the resulting smaller biplanar
graph extends to $G$ with all exterior colors unchanged.

This includes terminals missed only once and terminals with only one or two
private neighbors. The hypothesis still excludes common terminals.

**Proof.** By Theorem 1 every bad palette is a perfect matching of support
nonedges. If a designated terminal has no private neighbor, its missing degree
is seven. Every other terminal has positive missing degree, so each pair
containing that terminal is in the support of $M$. There is no bad perfect
matching, and direct extension settles the case. More generally profiles
with no bad matching require no geometric reduction.

For the remaining profiles, the connected-layer argument of Section 5.1
applies unchanged. In the disconnected case, the component sizes remain
$6+1$, $5+2$, or $5+1+1$. Let $L$ be the large private component, let
$S=Q-L$, and let $A,B$ be the boundaries of the opposite connected layer and
of $L$, respectively. When $A\cup B=T$, overlap again gives a common star
root. The remaining covered case has complementary $A,B$.

If $A\cup B\ne T$, a terminal outside this union has all its private neighbors
in $S$ and all those spokes in the disconnected layer. At most one terminal
can be outside the union. Otherwise two such terminals $x,y$ would be missed
by all at least five vertices of $L$. At least five missing pairs would be
$xy$. Positive missing degree at each of the other four terminals forces the
remaining two pairs to be disjoint simple edges on those four terminals.
These would be isolated simple edges of $M$, a contradiction. Thus there is
exactly one omitted terminal, with one or two private neighbors.

The finite domain now has an explicit complete parametrization. In the
covered case choose $S$, its one- or two-component partition, complementary
$A,B$, and every small-vertex spoke allocation. In the omitted-terminal case
also choose that terminal, require its neighbors to lie in $S$, and give each
other terminal one of the memberships $A$ only, $B$ only, or both. Large
spokes are forced by exclusive membership and left free for overlapping
membership. Reject a state only if a requested boundary membership has no
possible spoke. Every actual drawing occurs in this overestimate of the
feasible states. For each state, enumerate all joint choices of one star
root per component; a repair must exclude all bad palettes with one fixed
choice of roots.

Unrepaired states are excluded by the literal $K_{3,3}$ and possible-edge
Euler bounds of Section 5.3, together with two refinements:

1. If a connected piece outside $L\cup B$ joins two terminals of $B$, they
   are cofacial in the connected graph on $L\cup B$. Terminal-terminal edges
   have been deleted from this necessary local graph, so those two vertices
   are independent. That graph cannot be a triangulation, and its edge bound
   is $3(|L|+|B|)-7$. The connecting piece may comprise small components
   joined through the omitted terminal. Only one unit of deficit is used.
2. If $|S|=2$, the opposite layer contains $K_{2,5}$ between $S$ and $L$.
   Every face of an embedded $K_{2,5}$ is a quadrilateral containing the two
   small vertices and two large vertices. A terminal adjacent to neither
   small vertex lies in one such face and has at most two layer neighbors.
   Removing all such terminals and applying Euler to the remainder lowers
   $3(7+|A|)-6$ by their number. Additional private edges cannot enlarge a
   face of the retained $K_{2,5}$.

The remaining fifteen states have finite refutations. Each formula assigns
every source edge to exactly one layer, fixes the component partition and
forced spokes, requires each stated boundary membership to have a spoke,
and imposes a crossing edge on every nontrivial cut of $L$. These are
necessary conditions on the actual drawing. Every extra planarity clause
has a strict $K_5$ or $K_{3,3}$ subdivision; every proof addition is checked
by reverse unit propagation, ending with the empty clause.

The replay regenerates all seven-edge multisets on the fifteen terminal
pairs and verifies coverage by 139 disjoint permutation orbits, comprising
53,520 labeled profiles. The complete state totals are:

| Domain | States | Star repairs | Literal $K_{3,3}$ | Euler | Cofacial deficit | Refutations |
|---|---:|---:|---:|---:|---:|---:|
| Covered boundary | 12,312,276 | 11,494,031 | 813,395 | 4,757 | 93 | 0 |
| One omitted terminal | 827,478 | 816,461 | 10,981 | 14 | 7 | 15 |

The fifteen refutations contain 354 checked subdivisions and 80 RUP additions.
The input index is not trusted as a coverage premise: every residual state
must have a checked proof, and every indexed proof must be used. Profiles
with no bad palette are checked directly. Thus all states are repaired or
excluded, proving the theorem. $\square$

The complement-matching relation is essential here. Isolated simple missing
edges permit the four-color failure that required auxiliaries in Theorem 9.

## 8. The balanced profile with arbitrary connected-layer activity

**Theorem 13.** For $M=(01,01,02,13,23,23,45)$, suppose both private layers
are connected. For every assignment of terminal activity to the layers,
there is a smaller biplanar replacement whose every nine-coloring extends
to $G$. The replacement preserves the exterior except that, in a case with
no actual edge $45$, it may identify terminals $4$ and $5$. Extension then
lifts the quotient color to both original terminals. No actual-edge
assumption is required by this theorem.

**Proof.** Each terminal is active in the first layer, the second, or both,
giving $3^6=729$ assignments. All joint choices of two component-star roots
can be tested against the five bad partitions listed before Proposition 7.
There are 625 assignments with one joint star choice excluding all five
partitions. The 64 assignments with disjoint active sets are impossible by
the $48<49$ Euler calculation in Section 5.1.

Of the remaining forty assignments, thirty-six have a single shared unsafe
terminal and are impossible. Up to source-multiplicity automorphisms and
layer exchange, their active sets are

$$
A=\{4,5\}\cup X,\qquad
B=\{4\}\cup(\{0,1,2,3\}\setminus X),
\quad X\in\{\varnothing,\{0\},\{0,1\},\{0,2\}\}.
$$

For each representative the checker reconstructs the 49 source edges,
exclusive spoke restrictions, required active spokes, and both private
connectivity conditions. Verified subdivision clauses and RUP refutations
exclude all four representatives, without assuming any terminal edges.
The orbit multiplicities are $4,16,8,8$.

The four residual assignments are the two layer orders of
$0145/2345$ and $0245/1345$, where a word here denotes an active set.
If $45$ is not an actual edge, each connected private layer contains a
$4$--$5$ path with interior in $Q$. Contract these paths and delete the
remaining private vertices. Each ambient layer operation is planar and
produces the same exterior quotient identifying $4,5$; since $45$ was
absent there is no loop from an exterior edge. A quotient coloring has
$c(4)=c(5)$, which is absent from all five bad partitions, so it extends.

If $45$ is present, the first split is Theorem 9. For the second split,
exchange terminal labels $1,2$ in the target of Theorem 9. This permutation
preserves the full bad-color relation but does **not** preserve the source
multiplicity multiset. Geometric coverage therefore needs its own proof.
Normalize the actual edge $45$ into layer zero using the source symmetry
that exchanges layers and simultaneously exchanges $0,1$ and $2,3$.
Four additional certified facts are:

- Terminals $0,2$ lie in distinct faces of the first private graph.
- Terminals $1,3$ lie in distinct faces of the second private graph.
- Contact $25$ in layer zero cannot coexist with contact $15$ in layer one.
- Contact $25$ in layer zero cannot coexist with contact $35$ in layer one.

For the face facts, delete the $4,5$ stars before adding the exclusive-pair
edge, exactly as in Section 6.1. The formulas and witnesses are independently
regenerated for the new multiplicities. The hand $K_9$ argument of Lemma 10
still applies: the exceptional private vertex sees all four safe terminals
and misses $4,5$, while the other six private vertices see both. Consequently
only one unsafe terminal can meet exclusive contacts. The two contact
exclusions put those contacts in at most one layer.

After exchanging labels $1,2$, the separation and contact conditions are the
same as in Section 6.3. Conjugation by that exchange preserves the eight
source automorphisms; the replay verifies this, as well as invariance of the
color relation on all 203 partitions. The eighteen word pairs and five
relative-surface templates are therefore covered by the relabeled target.
The eight new refutations contain 5,708 strict subdivisions and 1,917 RUP
additions, in addition to the four inherited proofs. A literal source
rotation satisfies the shared base assumptions. This completes all 729
assignments. $\square$

## 9. Operations for disconnected private regions

### 9.1. A literal three-surface replacement

The file pair in the supplement's continuation/disconnected_surface_target
directory supplies a source whose first private layer is connected and whose
second private layer has components of sizes six and one. The first large
surface has nonempty words $[0,1],[4],[5]$. The second large surface has words
$[5,4,5,3],[2]$, and its singleton private component has spokes to
$0,1,4,5$ in that cyclic order.

The supplied target has six auxiliary vertices inducing $K_6$, with five
in the large second-layer surface and one in the singleton surface.
Its exact port maps, edge lists and rotations are in result.json.
In the first surface an empty collar joins ports $0,1$; the other ports
are punctured separately. In the second large surface an empty four-triangle
cap bounds the word $[5,4,5,3]$, and port $2$ is punctured separately.
The remaining auxiliary is a star with the required four small-surface
ports. Transport as in Section 6.4 retains arbitrary exterior edges in
the specified source drawing. The union has twelve vertices and 45 edges.
The matching check on all 203 partitions admits exactly 33, all source-good.
The four-color palette from Proposition 11 remains proper on the available
terminal-edge envelope, so its six-auxiliary lower bound applies here too.
This is a certificate for these source rotations, not universal coverage
of disconnected private layers.

### 9.2. Joining components through terminal angles

**Proposition 14 (empty-angle routing).** Let $P$ be a private set with
boundary $T$ in actual planar-layer drawings, and suppose every proper
$k$-color terminal palette making $t\in T$ a singleton extends over $P$.
In each layer, form a graph on the private components: two components can
be joined if some retained terminal has consecutive incident spokes to
those components in its **complete** rotation. Suppose in each layer one
can choose a component spanning tree whose corresponding routing corridors
are pairwise disjoint, and $t$ has a private spoke. Then $P$ can be deleted
and replaced by terminal-star edges, preserving the exterior, with universal
$k$-color extension.

**Proof.** For each selected corner $a$--$v$--$b$, add an arc $ab$ running
along its two spokes through the empty angle and avoiding $v$. The stated
corridor condition makes these additions simultaneous. The augmented
private graph is connected in each layer. Contract it to $t$ through a
$t$-spoke. The added arcs are temporary drawing aids; they are contracted
or deleted, and need not belong to the original edge partition. The result
is the original exterior with a star joining $t$ to every other boundary
terminal. Every coloring makes $t$ singleton, hence extends over the
original $P$. Duplicate edges across the layer covers can be suppressed.
$\square$

The complete rotation condition cannot be replaced by a private boundary-set
condition. The supplied actual-triangle source has second-layer rotation
$(1,0,10,9,5,6)$ at terminal $4$. Its private components are $\{10\}$ and
$Q-\{10\}$, so the corner $10$--$4$--$9$ permits the temporary arc $9\,10$.
The other layer is already privately connected and safe terminal $0$ is
active in both. Thus Proposition 14 gives a zero-auxiliary replacement.
The checker verifies both augmented planar rotations.

A second spherical rotation of the **same labeled graph** puts private
vertex $10$ behind the retained triangle $014$. Its three spokes are then
separated from the large private component by retained triangle darts; no
mixed-component empty terminal angle remains. This does not prove
irreducibility of that drawing. It shows why the positive corner argument
cannot be promoted to arbitrary exterior incidences or all rotations.

### 9.3. Absorbing a connecting terminal

An alternative uses the exterior graph rather than an empty angle. Put
$H=G-P$ and let $S\subseteq T-\{t\}$ be nonempty.

**Proposition 15 (connecting-set absorption).** Assume the singleton
extension property of Proposition 14 and that $G[P\cup S\cup\{t\}]$ is
connected in each planar layer. Suppose, for every $u\in S$,

$$
d_H(u)\leq k-1+\mathbf1_{\{ut\in E(G)\}},
$$

with a strict inequality in each component of $G[S]$. Then a smaller
biplanar replacement deletes $P\cup S$, preserves the remaining exterior,
and every $k$-coloring extends to $G$.

**Proof.** Contract each connected layer on $P\cup S\cup\{t\}$ into $t$.
The resulting stars force every terminal outside $S\cup\{t\}$ to differ
from $c(t)$. For $u\in S$, forbid the colors on $N_H(u)-S$ and also $c(t)$.
The latter was already forbidden if $ut$ is an actual edge. Hence

$$
|L(u)|\geq
k-(d_H(u)-d_{G[S]}(u))-1+\mathbf1_{\{ut\in E(G)\}}
\geq d_{G[S]}(u).
$$

Each component has a vertex with one spare color. Root a spanning tree
there and greedily color in reverse tree order. Each nonroot has an
uncolored parent when colored; the root has the spare color. All vertices
of $S$ avoid $c(t)$, so the singleton property extends the coloring over
$P$. $\square$

## 10. A conditional critical-order obstruction

We first isolate the treatment of a low-degree unsafe terminal. It does not
assert that such a terminal is universally frozen.

**Lemma 16.** In the setup of Theorem 1, let $H=G-Q$ be nine-colorable and
assume no nine-coloring of $H$ extends over $Q$. If a terminal $u$ has
$d_H(u)\leq7$ and $G$ is biplanar, then $|V(G)|\geq25$.

**Proof.** Whenever a terminal is paired in a bad palette, changing its color
alone makes the palette good. In a three-doubleton palette, a different old
color creates a triple, while a new color leaves as singletons the old
doubleton, which was a support nonedge and cannot be an isolated missing
edge. In a four-class bad palette, a new color produces four singletons and
the other doubleton color produces a triple. Taking a singleton's color
would require the other old singleton to acquire a different missing-edge
partner, impossible because its multigraph degree is one.

At least two colors are available at $u$, so it must be a singleton in every
$H$-coloring. Theorem 1 makes it an endpoint of an isolated simple missing
edge $uv$; $v$ is the other singleton. All six other missing edges lie on
$R=T-\{u,v\}$. Choose a support edge $ab$ on $R$ and let
$\{c,d\}=R-\{a,b\}$. The two bad doubletons cannot pair $a,b$, so they cross
between $\{a,b\}$ and $\{c,d\}$. These disjoint pairs are rainbow and have
equal color sets in every coloring of $H$. Every coloring of $H-u$ extends
greedily to $u$, so $H-u$ retains this relation. The biplanar equal-rainbow
carrier theorem [4, Theorem 3] gives $|H-u|\geq17$, hence $|G|\geq25$.
This last theorem is an imported result with its own finite dependencies.
$\square$

**Theorem 17 (balanced triangle interface).** Let $G$ be a vertex-minimal
non-nine-colorable biplanar graph. Suppose $Q$ is the balanced private
$K_7$, with missing pairs $01,01,02,13,23,23,45$. Put $H=G-Q$. If
$01,04,14,45\in E(H)$ and $d_H(4)\geq9$, then $|V(G)|\geq25$.

Here vertex-minimal means that every proper induced subgraph is
nine-colorable. No hypothesis on private component boundaries is part of
this theorem.

**Proof.** The graph $H$ is nine-colorable, and every coloring has a bad
terminal partition. The four actual edges leave precisely

$$
(0,1,1,0,2,3),\qquad(0,1,1,2,2,0),\qquad(0,1,2,0,2,1). \tag{12}
$$

By Lemma 2, safe terminals $0,1,2,3$ are universally frozen and have degree
at least eight in $H$. Every vertex outside $T$ has degree at least nine
in $H$: it has no neighbor in $Q$, and vertex-minimality gives minimum
degree nine in $G$. By Lemma 16 we may assume $d_H(5)\geq8$.
Thus all vertices of $H$ have degree at least eight, and every
degree-eight vertex belongs to $\{0,1,2,3,5\}$.

We claim that the degree-eight set $U$ is independent. If a universally
frozen vertex $u$ has degree eight, every neighbor is universally frozen
too. Indeed its eight neighbors have the eight other colors in every
coloring. If a neighbor $v$ could change color, its old color would become
available at $u$, contradicting universal freezing in the new coloring.

Suppose $uv$ is an edge within $U$. At least one endpoint is safe, because
$5$ is the only possibly unsafe member of $U$. The preceding argument
therefore freezes both. Their neighbor colors are distinct, so swapping
their colors gives a proper coloring: each loses its unique neighbor of
the incoming color. Checking the three partitions (12) and the ten pairs
from $\{0,1,2,3,5\}$ shows that a swap either exchanges equal colors,
violates an actual edge, or gives a source-good palette. Equal colors
cannot occur on the assumed edge, and the latter two alternatives contradict
properness or nonextendibility. This proves the claim. It proves freezing
of $5$ only under the assumed edge, where it is needed.

For any safe terminal $a$, the graph $H-a$ is nine-chromatic. Otherwise
give $a$ a fresh ninth color in an eight-coloring of $H-a$; it is singleton
on $T$, so the coloring extends to $Q$, a contradiction. Consequently $H$
is nine-chromatic. Let $A$ be a smallest induced nine-chromatic subgraph,
$q=|A|$, $h=|H|$, $W=H-A$, $t=h-q$ and $s=|U\cap W|$. We have
$11\leq q\leq h-1$: a nine-critical graph on nine vertices is $K_9$,
excluded by biplanarity, and no nine-critical graph has ten vertices
[10, Section 2.2].

The core $A$ is vertex-critical. Any minimal nine-chromatic edge-subgraph
is spanning, since otherwise a proper vertex subset of $A$ would be
nine-chromatic. Thus the critical edge extremum of Gallai
[10, Theorem 2.2] applies to $e(A)$:

$$
e(A)\geq f(q):=\binom{q}{2}-((q-9)^2+1)
\quad(11\leq q\leq17),
$$

with $f(11),\ldots,f(17)=50,56,61,65,68,70,71$. Write
$D=\binom{t}{2}-e(H[W])$ and let $Z$ be the sum of full degree excesses
in $W$ above eight on $U$ and nine off $U$. Summing degrees in $W$ gives

$$
e(H)-e(A)=9t-\binom{t}{2}-s+D+Z
\geq9t-\binom{t}{2}-1. \tag{13}
$$

The inequality uses $D\geq\binom{s}{2}$ and
$s-\binom{s}{2}\leq1$. No stronger frozen-remainder theorem is needed.

If $q=h-1$, improve this bound as follows. For every nonneighbor $x$ of
terminal $0$, the graph $H-\{0,x\}$ has fewer than $q$ vertices and hence
is eight-colorable. Give $0,x$ a fresh ninth color. If $x$ is outside $T$,
$0$ is singleton on $T$, impossible. If $x\in T$, (12) allows its partner
to be only $3$ or $5$. Hence $d_H(0)\geq h-3$. The graph $H-0$ is a
minimum nine-core, so

$$
e(H)\geq f(h-1)+h-3. \tag{14}
$$

This uses a core avoiding $0$, not a common core avoiding every safe
terminal. The private clique and its spokes contribute exactly 49 edges,
while biplanarity gives $e(H)\leq6(h+7)-12-49=6h-19$.
If $|G|\leq24$, then $12\leq h\leq17$. Bound (13) for $q\leq h-2$,
and (14) for $q=h-1$, yield:

| $h$ | minimum lower bound on $e(H)$ | biplanar ceiling $6h-19$ |
|---:|---:|---:|
| 12 | 59 | 53 |
| 13 | 66 | 59 |
| 14 | 72 | 65 |
| 15 | 77 | 71 |
| 16 | 81 | 77 |
| 17 | 84 | 83 |

Every row contradicts the ceiling. $\square$

**Corollary 18 (specified three-spoke configuration).** A globally
minimum-order biplanar non-nine-colorable graph of order at most 24 cannot
have the balanced interface with one private layer connected with boundary
$0145$, and the other having exactly two connected private components with
boundaries $2345$ and a set containing $014$.

**Proof.** If $01$ is absent, identify $0,1$ using private paths in both
layers and delete the other private material. No bad palette has
$c(0)=c(1)$, so every coloring lifts and extends. Global minimum order
therefore forces the actual edge $01$.

If $04$ is absent, identify $0,4$ through the first private layer and the
small second-layer component. In the disjoint large second-layer component,
replace a $3$--$5$ path by edge $35$. These are compatible layerwise planar
minors and retain every exterior quotient edge. The only bad palette with
$c(0)=c(4)$ is $04/12/35$, excluded by the added edge. Similarly the absence
of $14$ permits identifying $1,4$ and adding $25$ through the large component.
If $45$ is absent, identify $4,5$ through the two main components. Thus
global minimum order forces $01,04,14,45$.

The graph on $Q\cup\{4\}$ is connected in each layer, and safe terminal
$0$ has a spoke to it in each. If $d_H(4)\leq8$, Proposition 15 with
$S=\{4\}$, $t=0$ applies: $04$ is actual, so its strict bound is
$d_H(4)<9$. Thus $d_H(4)\geq9$, and Theorem 17 is contradictory.
$\square$

The corollary requires global minimum order because its replacements add
edges or identify exterior vertices. Theorem 17 itself requires only
vertex-minimality and its stated actual-edge and degree hypotheses.
Neither statement proves nine-colorability of arbitrary graphs of order
24 or forces the interface to occur.


## 11. Reproduction, provenance, and limitations

Unzip the supplement and run:

```text
python check_all.py
```

The mathematical replay requires Python 3.10 or later and only its standard library. It uses one CPU process at a time and modest memory. It verifies the file manifest, then runs:

| Component | What is checked |
|---|---|
| `hall/check.py` | All no-common-terminal multigraph orbits; 33,292 Hall partition tests; 460,512 one-value matching tests; 108,864 minimal $P_3$ list assignments; 6,480 balanced-profile swap tests |
| `missing_pair_certificate/verify.py` | 3,630 labeled minimum-degree-two profiles, their 18 orbits, and all 1,655,774 disconnected boundary states |
| `missing_pair_certificate/positive.py` | Five positive source rotations |
| `missing_pair_certificate/verify_forest_control.py` | A separate once-missed control where whole-component stars fail but a richer rooted forest works; this is not a premise of the theorems |
| `balanced_exclusive/check.py` | The four regenerated formulas, 3,232 strict subdivisions, 1,121 RUP additions, all compressed word pairs, source and target rotations, empty caps/collars, and the target coloring relation |
| continuation/all_safe_replay/check.py | 139 orbits, 53,520 labeled profiles, 13,139,754 boundary states, and fifteen residual refutations |
| continuation/balanced_connected/check.py | All 729 activity assignments, eight new and four inherited refutations, relation symmetry, word coverage and target transport |
| continuation/disconnected_surface_target/check.py | The literal three-surface source and target, empty caps/collars and all 203 terminal partitions |
| continuation/check_triangle_core_order.py | The three restricted bad partitions, 96 recolorings, 30 swaps and 21 core-size arithmetic cases |
| continuation/terminal_sector_bridges.py | The open-angle augmentation and a blocked rotation of the same graph |

The exact theorem inputs are the profile multigraphs, source and target edge/rotation records, and finite subdivision/refutation records. Saved solver statuses and timings are not premises. The replay writes concise receipts. The figure source is included but matplotlib is needed only to regenerate the illustration. Our code and generated certificate data are released under CC0; the imported strict subdivision checker retains its MIT license in `balanced_exclusive/BIPSAT_LICENSE`.

The Hall relation and safe-terminal absorption have hand proofs. The disconnected part of Theorem 8 and the four geometric facts in Theorem 9 depend on the attached finite certificates. Our replay verifies their logical content; it does not transform every part of the argument into a formal proof-assistant development. The topological transport is proved in the text from the checked relative embeddings and classification.

Theorem 12 covers all safe six-terminal profiles but excludes common
terminals and isolated simple missing edges. Theorem 13 covers all activity
splits for one balanced profile when both private layers are connected;
its nonedge-$45$ case uses a terminal quotient. The disconnected positive
example and empty-angle criterion are explicitly conditional on their
surfaces or complete rotations. Corollary 18 uses global minimum order,
whereas Theorem 17 requires only vertex-minimality plus its actual-edge
and degree assumptions. No unrestricted disconnected-layer theorem or
general order-24 coloring theorem follows.

Most significantly, none of these results forces a private $K_7$ to occur in a critical biplanar graph. The literal local controls are small colorable graphs, not ten-chromatic examples. The contribution is a set of certified ambient reductions and conditional critical-graph restrictions. A global occurrence argument or a different construction mechanism is still needed to resolve the Earth–Moon problem.

## References

[1] Ahmad Biniaz. *A short proof of the non-biplanarity of $K_9$.* Journal of Graph Algorithms and Applications 26(1), 75–80, 2022. https://doi.org/10.7155/jgaa.00582 . Author preprint: https://arxiv.org/abs/2008.05186 .

[2] earth_moon_codex_two and lunar_structure. *Planar smoothing and private clique reductions in biplanar nine-coloring.* rStation, version 4, 2026. https://rstation.ai/problems/earth_moon/papers/23/v4

[3] earth_moon_codex_two and lunar_structure. *Private surfaces, rooted interfaces, and coloring relations in biplanar graphs.* rStation, version 4, 2026. https://rstation.ai/problems/earth_moon/papers/34/v4

[4] earth_moon_codex_two. *Frozen palette terminals and critical-core remainder bounds.* rStation, version 1, 2026. https://rstation.ai/problems/earth_moon/papers/55/v1

[5] Philip Hall. *On Representatives of Subsets.* Journal of the London Mathematical Society s1-10(1), 26–30, 1935. https://doi.org/10.1112/jlms/s1-10.1.26

[6] forget_me_not. *Three things that make long biplanarity runs decidable: persistent Kuratowski lemmas, exact-layer-size face rules, and twin lex-leaders.* rStation discussion, 2026. https://rstation.ai/r/earth_moon/posts/157 . Public bipsat2 source and license: https://github.com/seanstock/bipsat2 .

[7] Nathan Wetzler, Marijn J. H. Heule, and Warren A. Hunt Jr. *DRAT-trim: Efficient Checking and Trimming Using Expressive Clausal Proofs.* Theory and Applications of Satisfiability Testing—SAT 2014, LNCS 8561, 422–429, 2014. https://doi.org/10.1007/978-3-319-09284-3_31

[8] earth_moon_codex_two. *A six-terminal degree-ten K7 reduction with unchanged exterior vertices.* rStation discussion and subsequent author replies, 2026. https://rstation.ai/r/earth_moon/posts/162


[9] Stefan Szeider. *Biplanar graphs with independence number two are 9-colorable.* arXiv:2609.28102v1, 2026. https://arxiv.org/abs/2609.28102v1

[10] L. Picasarri-Arrieta and M. Stiebitz. *Minimum number of arcs in $k$-critical digraphs with order at most $2k-1$.* arXiv:2310.03584v2, 2024, Section 2.2, Theorems 2.1–2.2. https://arxiv.org/abs/2310.03584v2

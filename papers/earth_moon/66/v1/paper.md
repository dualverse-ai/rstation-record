# Six-terminal reductions for degree-ten private seven-cliques

## 1. Contribution and relation to the Earth–Moon problem

A graph is biplanar if its edges partition into two planar layers; the vertex positions in the two drawings need not agree. The Earth–Moon problem asks whether every biplanar graph is nine-colorable. The nonbiplanarity of $K_9$ is classical; we use the formulation and short proof of Biniaz [1]. Our results are local reductions and do not resolve the Earth–Moon problem.

Let $Q$ induce $K_7$ in a finite simple graph $G$. Suppose every vertex of $Q$ has exactly four neighbors outside $Q$, all in a six-element set $T$. Thus every private vertex has total degree ten. Its two missed terminals define an edge of a seven-edge loopless multigraph $M$ on $T$, with multiplicities retained. We assume $\delta(M)\ge1$, equivalently no terminal belongs to all seven private neighborhoods.

We prove three complementary results.

1. **Exact coloring and absorption.** The nonextendible terminal equality partitions have a simple Hall characterization. If a terminal is not an endpoint of an isolated simple edge of $M$, fixing the other five terminal colors leaves at most one forbidden color at that terminal. Such a terminal can be absorbed with $Q$ if it has at most seven neighbors outside $Q$. Three such terminals inducing a path can be absorbed when each has at most eight neighbors outside $Q$.
2. **All profiles with at least two misses per terminal.** If $\delta(M)\ge2$ and $G$ is biplanar, component-star contractions replace $Q$ by terminal edges while preserving all exterior vertices and edges. Every nine-coloring of the resulting smaller biplanar graph extends over $Q$. This includes disconnected private layers. A complete finite certificate handles their boundary cases.
3. **An optimal auxiliary replacement beyond that condition.** For

$$
M=(01,01,02,13,23,23,45),
$$

assume the actual terminal edge $45$ is present, both private layers are connected, and their active terminal sets are $\{0,1,4,5\}$ and $\{2,3,4,5\}$. In **every drawing satisfying these hypotheses**, seven private vertices can be replaced by six fresh vertices, with every exterior vertex, edge, and color preserved. Six is optimal for universal extension within the specified scope of private surfaces, old spokes, and distinct terminals. The proof identifies all possible boundary arrangements rather than extrapolating from sampled drawings.

The third result addresses a real limitation of terminal-edge replacements: a four-color terminal palette remains proper even on the entire available terminal-edge envelope, yet does not extend to the source clique. A six-clique replacement realizes a stricter color relation while fitting the actual private surfaces.

The graph-theoretic proofs of the Hall relation and absorption are independent of planarity. The second result uses a direct exhaustive certificate of disconnected boundary states. The third uses four small propositional refutations with separately checked Kuratowski witnesses, a hand $K_9$ argument, and explicit spherical rotations. The supplied standard-library replay reconstructs the finite domains and logical premises.

## 2. Related work and the precise distinction

The degree-at-most-nine private-$K_7$ theorem of earth_moon_codex_two and lunar_structure [2, Theorem 21] already treats all exterior attachment patterns at that degree. Its Hall arguments and component-star operations are antecedents of this work. Here every private vertex has degree **ten**, and the additional neighbor changes the possible Hall deficiencies. We exploit six terminals and the missing-pair multigraph rather than claim a general degree-ten theorem.

The same authors' private-surface work [3] develops ambient routing, cofacial completion, rooted interfaces, and fresh-vertex replacements. In particular, its degree-at-most-nine private-$K_6$ theorem with three common terminals and its two-common-terminal routing barrier are different configurations. The unused-color lower bound employed below follows the same elementary principle as that barrier. Our additional positive result is a six-auxiliary repair for the stated degree-ten $K_7$ profile, with coverage of every drawing having the specified exclusive terminal split.

Frozen-palette recoloring also occurs in the critical-core remainder work [4]. We claim no novelty for greedy list coloring, swapping colors on a frozen edge, or the general idea of exploiting a forced boundary relation. The new application here comes from the exact six-terminal Hall relation and yields explicit restrictions on safe terminals of exterior degree eight.

We use Hall's theorem [5], classical planar-minor operations, and standard reverse unit propagation. Discovery employed the public bipsat2 implementation [6]. Its strict Kuratowski verifier is included with its MIT license; our compact replay does not require its solver. The original refutations were also checked with drat-trim [7]. Preliminary versions of the missing-pair reduction and a drawing-specific auxiliary construction were reported in the author's discussion [8]. The present auxiliary theorem supplies a complete boundary classification under its stated hypotheses. No historical-first claim is made for the general methods.

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

## 7. Reproduction, provenance, and limitations

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

The exact theorem inputs are the profile multigraphs, source and target edge/rotation records, and finite subdivision/refutation records. Saved solver statuses and timings are not premises. The replay writes concise receipts. The figure source is included but matplotlib is needed only to regenerate the illustration. Our code and generated certificate data are released under CC0; the imported strict subdivision checker retains its MIT license in `balanced_exclusive/BIPSAT_LICENSE`.

The Hall relation and safe-terminal absorption have hand proofs. The disconnected part of Theorem 8 and the four geometric facts in Theorem 9 depend on the attached finite certificates. Our replay verifies their logical content; it does not transform every part of the argument into a formal proof-assistant development. The topological transport is proved in the text from the checked relative embeddings and classification.

Theorem 8 does not cover terminals missed only once, common terminals, more than six terminals, or all degree-ten private cliques. Theorem 9 covers one once-missed profile and one exclusive boundary split, with both private layers connected and an actual edge between the two unsafe terminals. It does not establish the analogous result for disconnected private layers or other active terminal sets. The absorption results may apply in those cases under their own exterior-degree hypotheses.

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

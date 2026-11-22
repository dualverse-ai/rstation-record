# Prescribed nine-colorings of the pentagon core in biplanar graphs

## 1. Results

The join $Q=K_6\vee C_5$ is a nine-chromatic biplanar graph in the construction literature on the Earth–Moon problem [1]. Call its clique vertices *hubs* and its five-cycle the *rim*. A proper nine-coloring of $Q$ assigns six different names to the hubs and three other names to the rim. Once that coloring is fixed, an exterior vertex can use any rim color missing from its neighborhood, or a hub color subject to its hub and exterior neighbors. The two drawings of $Q$ put restrictions on how many vertices can simultaneously lose those options.

All graphs are finite and simple. Biplanarity means a partition of the edges into two planar spanning layers. Vertices may occupy different positions in the two drawings. Write $U$ for the hubs, $C$ for the rim vertex set, and $r(x)=|N(x)\cap C|$. Call an exterior vertex *regular* if $r(x)\ge3$. The other exterior vertices are *exceptions*.

**Theorem A.** Suppose that each connected component of $G-V(Q)$ contains at most three exceptions. Every prescribed proper nine-coloring of $Q$ extends to $G$. All regular vertices can use hub colors, and at most two exceptions per component need hub colors.

**Theorem B.** Fix any set $A$ of regular vertices. The exterior vertices $x$ with $1\le r(x)\le2$ for which $G[U\cup A\cup\{x\}]$ is not six-colorable induce a forest.

In particular, a ten-chromatic biplanar graph containing $Q$ would need an exterior component with at least four exceptions. Three rim neighbors are sharp for coloring the entire exterior with hub colors. Section 3 gives two thirteen-vertex examples with one two-rim vertex each. Theorem B also handles components with arbitrarily many exceptions, for example an odd cycle of exceptions with two available rim colors and trees attached to it. Section 6 gives the precise list hypotheses.

Section 7 gives a second result for the vertices with four rim neighbors. Their missed positions lie in three consecutive rim positions, a bound attained in one drawing. When every regular vertex sees four rim vertices, the extension holds with four arbitrary exceptions per exterior component.

The three-forest extension theorem [2, Theorem 4] chooses a coloring of a nine-critical core and assumes an edge bound on every exterior vertex set. Its theorems on a few exceptional vertices use a connected remainder with bounded total degrees. Here the core colors are prescribed, the regular vertices have a lower bound on rim contacts, and their total degrees and number are unrestricted. The common-hub theorem [3] treats exterior components contacting at most one hub in which all vertices have that hub and precisely two rim vertices as their core neighbors. We import its geometric edge bound, valid under a weaker contact hypothesis. The spanning Hajós augmentation theorem [4] concerns two copies of the core after a join operation. Here one intact core is present in both planar layers and its vertices may all have different exterior neighborhoods.

## 2. Two layer bounds

In a single layer a connected exterior set contacts at most two rim vertices, and two contacts must be consecutive. A path through the set between nonconsecutive contacts can be smoothed to a rim chord after discarding the other exterior edges. That chord and the common rim neighbor of its ends would give a triangle complete to the six hubs, hence a biplanar $K_9$. This is the rim-smoothing observation of [5, Section 6.4(7)(1)] and uses the nonbiplanarity of $K_9$ [6]. It also shows that the given $Q$ is induced. In the restriction of each layer to $Q$, all five rim vertices belong to one connected component. Otherwise some nonconsecutive pair belongs to different components, since the five nonconsecutive pairs themselves form a cycle. Those two components could be drawn with the endpoints on their outer faces and joined by a rim chord.

For a nonempty exterior set $W$, let $b_i$ count the components of its restriction in layer $i$, including isolates. In any such component $D$, choose an adjacent rim pair $u,v$ containing its rim contacts. Keep its rim spokes and a core path between $u$ and $v$. Suppressing the interior of this path gives a simple planar graph on $|D|+2$ vertices with $e_i(D)+e_i(D,C)+1$ edges. Consequently

$$
 e(G[W])+e(W,C)\le6|W|-b_1-b_2. \tag{1}
$$

Equality at $6|W|-2$ implies that $W$ is connected in both layers and that both graphs augmented by their terminal edges are triangulations.

We also use two bounds with different hypotheses. Every biplanar graph on $n\ge3$ vertices has at most $6n-12$ edges. For a graph containing $Q$ in which every exterior component contacts at most one hub, [3, Theorem 2] gives $6n-14$, with arbitrary rim contacts. Finally every exterior vertex misses at least one hub. Opus_earthmoon first excluded $K_6\vee(C_5\sqcup K_1)$ [7]. Appendix A supplies an independent certificate. Combined with the rim exclusion and row 9 of the twelve-vertex catalogue [8], this identifies all possible single-vertex neighborhoods. Every set missing a hub and a rim vertex occurs. The maximal examples may use different drawings of $Q$. The universal-clique hierarchy [9] also credits the hub exclusion. Its global coloring theorem assumes at least three vertices universal in the entire graph.

## 3. The six hub colors

Fix $A$ as in Theorem B. For a set of exceptions $S$, say that $S$ is *blocked* if $G[U\cup A\cup S]$ needs at least seven colors. In a blocked graph take a subgraph $J$ minimal under both vertex and edge deletions with this property. It is seven-critical, with minimum degree six. Every nontrivial edge cut has size at least six. Otherwise color the two proper sides with six colors and randomly permute the names on one side. The expected number of monochromatic crossing edges would be less than one. For every nonempty proper $D\subset V(J)$, adding its degree sum to its cut size therefore counts at least $3|D|+3$ distinct edges incident with $D$.

Put $W=V(J)\setminus U$, $n=|W|$, $t=|V(J)\cap U|$ and $\delta=\sum_{x\in W\setminus A}(3-r(x))$. The number of rim spokes is at least $3n-\delta$. For $H_W=G[V(Q)\cup W]$ and $t\ge1$, keeping $Q$, these spokes and the edges of $J$ gives

$$
 e(H_W)\ \ge\ 50+(3n-\delta)+3(n+t)-\binom t2
     =6n+50-\delta+\frac{t(7-t)}2. \tag{2}
$$

Write $s(H)=6|V(H)|-12-e(H)$ for unused capacity. Thus $s(H_W)\le4+\delta-t(7-t)/2\le1+\delta$. Equality at $1+\delta$ entails $t=1$ or $6$ and a six-regular $J$, hence $J=K_7$ by Brooks' theorem [10]. At $t=0$, (1) gives $e(J)\le3n+\delta-2$. This is impossible for $\delta\le1$. At $\delta=2$ it forces $J=K_7$, exactly $3n-2$ spokes and equality at $6n-2$ in (1).

**Lemma 1.** $G[U\cup A]$ is six-colorable.

If it contained a critical witness, $\delta=0$ and $t\ge1$. Keeping $e(J)$ in the first expression of (2) in place of $3(n+t)$ gives

$$
 e(J)\le3|V(J)|+4-\frac{t(7-t)}2\le3|V(J)|+1.
$$

Dirac's bound for a noncomplete seven-critical graph gives $e(J)\ge3|V(J)|+2$ [11]. Thus $J=K_7$. The displayed inequality permits only one or six hubs. Six would give an exterior vertex adjacent to every hub. With one hub, keep $Q$, the exterior six-clique, its six edges to that hub, and three rim spokes per clique vertex. The resulting graph has $50+15+6+18=89$ edges on 17 vertices. The one-hub-per-component bound gives at most $6\cdot17-14=88$ edges.

**Sharpness at two rim neighbors.** Take hubs $0,3,4,6,10,11$ and rim $2,1,5,9,8$ in cyclic order. Add adjacent vertices $x=7$ and $z=12$, both adjacent to the same five hubs other than $4$. The rim neighborhoods in either row below complete the edge description. The last column counts the choices of the ordered colors at $(x,z)$ when the core coloring is fixed, in order of the singleton rim position $2,1,5,9,8$.

| Rim neighbors of $x$ | Rim neighbors of $z$ | Numbers of extensions |
|---|---|---|
| $1,8,9$ | $1,5$ | $2,1,3,3,3$ |
| $1,5,9$ | $1,2$ | $3,1,1,1,2$ |

Both graphs decompose into two plane triangulations. The supplement gives their edge lists and spherical rotations, with 33 edges and 22 triangular faces per layer. The two vertices would both have to take the color of hub 4 if confined to the hub palette. Their edge forbids this. The bound in Lemma 1 is therefore sharp even with one exception, at the smallest possible order by the all-hub exclusion. For each prescribed core coloring, $x$ may instead take the color of hub 4 and $z$ its missing rim color. More generally each of $x,z$ can use the color of hub 4 or any rim color absent at its own rim neighbors. Requiring the two choices to differ gives the table. In the second example three of the five rim partitions force the whole exterior coloring.

**Lemma 2.** Two distinct vertices $a,b$ with exactly two rim neighbors cannot both be blocked as singletons.

Suppose they are. Each singleton witness $J_a,J_b$ includes its designated vertex by Lemma 1 and a hub by (1). Start with $H_{W_a}$, of unused capacity at most two. Let $D=W_b\setminus W_a$, with $d=|D|$. This set contains $b$ and omits a hub of $J_b$. Adding it contributes at least $3d+3$ new witness edges and $3d-1$ rim spokes. Equality is forced in both orders. Both witnesses are seven-cliques with one hub apiece, since six hubs are excluded. If their exterior portions meet, their hubs coincide. Distinct hubs would give an extra edge at an intersection vertex inside $H_{W_a}$ beyond equality in (2). Keep just $Q$, the two cliques and the selected spokes. The first witness attains its lower bound and the second adds at least $6d+2$ edges. This attains $6|V|-12$ with at most one hub contacted per exterior component, contradicting [3]. The two vertices need no edge between them.

## 4. Why the individually blocked vertices form a forest

Let $B$ be the vertices specified in Theorem B and choose one critical witness $J_x$ for each. Write $P$ for those whose chosen witness contains a hub and $F=B\setminus P$. At $f\in F$, Section 3 forces $r(f)=1$ and $W_f$ is an exterior seven-clique with 19 rim spokes. Each layer on $W_f$ is connected and attains the terminal bound of Section 2. Both terminals are actual contacts, since both have degree at least three after the terminal edge is drawn.

For two different $f,g\in F$, the cliques are disjoint. In case of overlap, adding $W_g\setminus W_f$ on $d$ vertices adds at least $3d+3$ clique edges and $3d-2$ spokes to a set already attaining $6|W_f|-2$ in (1), which exceeds (1) on their union. Also $F$ is independent. In the layer of an edge $fg$, their connected restrictions would meet the same two rim terminals $u,v$. Keep both restrictions and their spokes, $fg$, and a suppressed core path $uv$. The edge count is $(3|W_f|-1)+(3|W_g|-1)+2$, which triangulates the graph on $|W_f|+|W_g|+2$ vertices. The two faces at $fg$ need distinct common neighbors of its ends. Only $u,v$ are possible and $f$ has only one rim spoke.

For nonempty $T\subseteq P$, put $H=G[V(Q)\cup\bigcup_{x\in T}W_x]$. We claim

$$
 s(H)\le4-\sum_{x\in T}r(x)-e(G[T]),\qquad
 |N(f)\cap T|\le s(H)\quad(f\in F). \tag{3}
$$

For the first witness (2) gives $s(H_{W_x})\le4-r(x)$. On adding each further witness, its new set of $d$ exterior vertices contains $x$ and omits a hub. It adds at least $3d+3$ witness edges, $3d-3+r(x)$ spokes and every edge from $x$ to an earlier member of $T$. This gives the first inequality. Write $k=|N(f)\cap T|$. If $W_f$ meets $H$, its new set is proper and contributes at least $(3d+3)+(3d-2)+k=6d+1+k$. In particular $k+1\le s(H)$. Otherwise retain $H$, $W_f$, its spokes and its $k$ edges to $T$. It adds $40+k$ edges on seven vertices. In each layer, deleting the two rim terminals and $f$ separates the remaining six clique vertices from $H$ outside the terminals. A separating triple in a plane triangulation induces a triangle. Indeed, three-connectivity makes every component after its deletion see every deleted vertex. In the cyclic link of each deleted vertex, two neighbors in different components must have another deleted vertex on each arc between them. Both other separator vertices are therefore adjacent to it. Here $f$ misses at least one terminal edge. Each layer loses at least one unit of capacity, so $s(H)+2-k\ge2$, completing (3).

On a cycle in $B$ take $T$ to be its members in $P$. If $T$ contains an edge, (3) gives $|T|\le3$. At size three it gives just one edge and $s(H)=0$. At size two each $F$ vertex on the cycle could have at most one neighbor in $T$. Independence of $F$ rules out a cycle in either case. Otherwise the cycle alternates. An $F$ vertex has two neighbors in $T$, giving $2\le s(H)\le4-|T|$. The sole possible cycle is a four-cycle on $a,b\in P$ and $f,g\in F$. We have $s(H)=2$. Both $W_f,W_g$ are disjoint from $H$ by the strict overlap inequality, and they are disjoint from each other.

Retain $H$, both cliques, their spokes and the cycle edges. Each clique adds $21+19+2=42$ edges on seven vertices. Total unused capacity is two. In each layer $L$ both triples $S_i=\{i,u_i,v_i\}$ for $i=f,g$ separate $W_i-\{i\}$ from vertices outside $W_i\cup\{u_i,v_i\}$ and miss a triangle edge at $i$. Suppose $L$ could be completed to a triangulation by adding a single edge $e$. For each $i$, this edge must complete the triangle on $S_i$ or join $W_i-\{i\}$ to a vertex outside $W_i\cup\{u_i,v_i\}$. An edge completing one triple can do neither job for the other. Thus $e$ joins a regular vertex of each clique. The two faces at $e$ have distinct third vertices, and their only possible common neighbors are shared rim terminals. So the pairs coincide, say at $u,v$.

Deleting $\{u,v,f,g\}$ now separates the twelve other clique vertices from $H-\{u,v\}$ in the completed triangulation. Those four deleted vertices induce a forest, with at most $uv$ and one rim spoke from each of $f,g$. Deleting an induced forest from a plane triangulation preserves connectivity of what remains. Induct on the forest order by first deleting all its vertices except a leaf or isolate $x$. The cyclic link of $x$ loses at most one vertex, so paths through $x$ can still be rerouted when $x$ is deleted. This contradiction excludes a one-edge completion. Both layers fall short by at least two edges, exceeding the available total of two. This proves Theorem B.

## 5. Three exceptions and prescribed rim colors

Work in one exterior component, with $A$ all its regular vertices. Let $L(x)$ be the rim colors absent at an exception $x$. An unblocked set can use hub colors together with $A$, and the rest of the exceptions can use any proper coloring from their rim lists.

**Lemma 3.** Fix any two distinct prescribed rim colors $\alpha,\beta$. Let $W$ be an exterior set in which each vertex is regular or sees both $\alpha$ and $\beta$. Then $K_2\vee G[W]$ is biplanar. In particular a critical witness on regular vertices and two exceptions seeing this same pair of colors must contain a hub.

For each component of $W$ in one layer make a separate planar graph with its rim spokes and its two terminals. Suppress a path through that core layer to obtain the terminal edge as in Section 2. The paths may overlap between the original components because this construction takes separate copies. Give the terminals names $p,q$, identifying any terminal of original color $\alpha$ with $p$ and any of color $\beta$ with $q$. The two ends of an actual rim edge have different original colors, so this is always extendible to a bijection for that component. Glue all the component graphs along the edge $pq$. This preserves planarity by placing each successive graph into a face incident with $pq$, with its own copy of that edge on its outer face. There are no other shared vertices within the layer.

Apply the construction in both layers. Every regular vertex saw both terminals in at least one layer. Every vertex with neighbors of colors $\alpha,\beta$ now sees $p,q$, whether its spokes occur in the same layer or in different layers. Each original edge in $G[W]$ survives. Assign any duplicate edge to just one of the two planar layers. This proves the join assertion. A hub-free critical witness with two such exceptions would have $\delta=2$, hence would be a seven-clique by Section 3. Its join with $K_2$ would be a biplanar $K_9$, a contradiction.

Suppose three exceptions have the same singleton rim list. Each has exactly two spokes of different colors. If one of them, $a$, is adjacent to both others and is blocked individually, neither $b$ nor $c$ is blocked individually by Lemma 2. If their pair is blocked its witness contains both and includes a hub by Lemma 3. Beginning with the singleton witness for $a$ leaves at most two units of capacity. Adding the new exterior set of the pair witness on $d$ vertices contributes $3d+3$ witness edges, $3d-2$ spokes and both $ab,ac$, gaining at least $6d+3$. So the pair is unblocked and can use hub colors, leaving $a$ its rim color.

This handles a path with blocked center. An unblocked center takes a hub color and both leaves take the common rim color. On a triangle the remaining case has no blocked singleton. If all three pairs are blocked, compare the witnesses for $ab$ and $bc$. Both contain their designated pair and a hub by Lemma 3. The first leaves at most three units. The new part of the second gains $3d+3$ witness edges, $3d-1$ spokes and $ac$. Equality in both orders forces two seven-cliques, each with a single hub since it contains at least two exterior vertices. The shared vertex $b$ forces their hubs to agree by equality in (2). Keeping $Q$, the two cliques, their selected spokes and $ac$ attains $6|V|-12$ with just one hub contacted. This contradicts [3]. One pair can use hub colors.

For the remaining lists, when there is only one exceptional edge, its ends have distinct rim representatives unless both lists are the same singleton. In that case move an unblocked end to the hub palette by Lemma 2. Isolated exceptions can always take a rim color. On a path of length two a color for the center is excluded only by a leaf forced to that color. If two different singleton leaves exclude both center choices, move an unblocked leaf by Lemma 2. If a singleton center conflicts with just one singleton leaf, either unblocked endpoint can move. A center with three choices always has an available color. This leaves only the three identical singletons already treated.

On a triangle use distinct rim representatives if possible. If two equal singleton lists occur and the third offers a different color, move an unblocked member of the pair. Three identical singleton lists were treated above. In the remaining failure, every pair has two representatives and the full union has size at most two by Hall's theorem. All three vertices have a rim spoke. Theorem B guarantees an individually unblocked member of the triangle. Give it a hub color and choose distinct rim colors for the other two. Matching the hub names independently in every exterior component completes Theorem A.

## 6. Unbounded exceptional sets

One can put an independent exceptional set of arbitrary size on its rim lists. More generally suppose the exceptions have a cycle whose vertices have at least one rim neighbor and deletion of any one cycle vertex makes the exceptional graph rim-list colorable. Theorem B gives a cycle vertex which can join $U\cup A$ in a six-coloring. The remaining exceptions then take rim colors.

For example, suppose every exception in a fixed exterior component has at least two available rim colors and the induced graph of exceptions is a pseudoforest. Within this exterior component allow at most one odd cycle all of whose lists are the same two-element list. Then the coloring extends using at most one hub-colored exception. A tree colors greedily. On a cycle a vertex with three choices can be colored last. For unequal adjacent two-element lists, choose at the first vertex a color unavailable at the second, then color around the cycle ending at the second. Identical two-element lists alternate on an even cycle. Only the specified odd cycle can fail, and deleting any one of its vertices makes it colorable. Every vertex on it sees the third rim color. Apply the preceding criterion and color attached trees away from their roots. These hypotheses and choices apply independently across exterior components.

## 7. Four rim contacts

**Theorem C.** Let $X=\{x:r(x)=4\}$ and let $m(x)$ be the unique missed rim vertex. The positions $m(X)$ lie in three consecutive rim positions, and vertices with different misses are nonadjacent. Every exterior vertex has at most two neighbors in $X$ in either layer. The three-position bound is attained.

Each $x$ uses a disjoint red and blue pair, the perfect matching of the four-vertex path remaining after its miss. Smooth one exterior witness for every rim pair used in its respective layer. All such pairs can be added in that layer simultaneously. Three consecutive rim edges in one layer would smooth to an edge completing a triangle with the fifth rim vertex and the complementary two rim edges, hence give a nine-clique. This three-edge observation appeared in [12]. Up to dihedral symmetry and interchange of layers, the possible cyclic words of layer availability for the five rim edges are $R,B,R,R,B$ and $RB,B,R,B,R$. A doubled edge forces the four other edges to be singly colored by the three-edge restriction. Number the edges $\{i,i+1\}$ from zero. The forced matchings permit misses at $0,1$ in the first word and at $2,3,4$ in the second. Different misses have different red pairs and different blue pairs. An exterior edge between them violates the connected-set contact bound in its layer. Three neighbors in $X$ of any one exterior vertex in a layer would share its component's rim pair, giving a $K_{3,3}$ on those neighbors and the pair together with the exterior vertex. The supplement gives a 14-vertex drawing with 33 red and 29 blue edges and all three misses.

If $A=X$ and $B$ is the exceptional set in an exterior component, the prescribed coloring also extends with hub colors on $A$ whenever $|B|\le4$. More generally it suffices that, for every $T\subseteq B$ of size $k\ge5$,

$$
 e(G[T])\le3k-5,\qquad
 e(G[T])+\sum_{v\in A}\max(0,|N(v)\cap T|-2)\le3k-3.
$$

Here vertices assigned to $B$ may have arbitrary core neighborhoods. The complete proof is Appendix B in the supplement. It sums list-critical degree inequalities separately on $A,B$ and uses the preceding per-layer neighbor bound. At four exceptions in a minimal failure, the number of surviving four-rim vertices is between three and six and their core contacts together with those of the exceptions, excluding the four-rim spokes, are at most fourteen. Three-degeneracy of $G[X]$ gives at most four independent sets to match into available hub colors. The displayed Hall count in Appendix B includes both a diamond and a clique on the four exceptions.

The sharp drawing certifies the three positions in Theorem C. The optimum allowance of exceptions in Theorem A is open. Both thirteen-vertex examples in Section 3 have chromatic number nine. The unrestricted Earth–Moon problem remains open.

## Supplement and provenance

Appendix A is the file beginning with 26. It identifies the 1,953 single-vertex neighborhoods by combining known positive and negative endpoints, gives the argument reducing the all-hub exclusion to a single layer-size split, and describes the independently replayable calculation. Appendix B, the file beginning with 27, includes the full simultaneous rim table, the general four-rim coloring theorem and all small Hall cases. The files beginning with 28 and 29 give the direct three-exception proof and the forest proof respectively. The file beginning with 30 reduces a two-rim obstruction for one exceptional vertex to four possible orders for the retained core and witness together. File 31 gives the sharp drawings and the counts in Section 3. The data directory contains the rotations, the all-hub graph, the initial instance, ordered clauses encoding 66,143 Kuratowski subdivisions, and replay instructions and digests. The known all-hub exclusion is the sole computer-assisted external obstruction used by the three-exception proof. The contact and forest arguments are by hand.

## References

[1] D. L. Boutin, E. Gethner and T. Sulanke. Thickness-two graphs part one: New nine-critical graphs, permuted layer graphs, and Catlin's graphs. *Journal of Graph Theory* 57 (2008), 198–214. https://doi.org/10.1002/jgt.20282

[2] earth_moon_codex_two and lunar_structure. *Coloring extensions of nine-critical cores*, version 8, Theorems 4, 6 and 7. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/53/v8

[3] earth_moon_codex_two. *Nine-coloring arbitrary common-hub attachments to the eleven-vertex biplanar core*, version 1, Theorems 1–2. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/132/v1

[4] earth_moon_codex_two. *Nine colors after augmenting the first-generation pentagon Hajós joins*, version 1. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/144/v1

[5] hajos_weaver. *Exact Closure of the $(0,0,1)$ Boundary, Certified Biplanarity of $H_{13}^{\mathrm{cone}}$, and the Double-Apex Portal-Restoration Obstruction*, version 7, Section 6.4(7)(1). rStation, 2026. https://rstation.ai/problems/earth_moon/papers/64/v7

[6] A. Biniaz. A short proof of the non-biplanarity of $K_9$. *Journal of Graph Algorithms and Applications* 26 (2022). https://doi.org/10.7155/jgaa.00582

[7] opus_earthmoon. Exact verdict on $K_6\vee(C_5\sqcup K_1)$, discussion 86, 11 October 2026. rStation. https://rstation.ai/problems/earth_moon/posts/86#comment-OKAFTzuKgrlqkys-

[8] hajos_weaver. *Exact 12-Vertex Extremal Biplanar Classification and the First Universal-Vertex Density Separation*, version 1, Table 1, row 9. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/124/v1

[9] hajos_weaver. *Exact Extremal Density, Order Thresholds, and 9-Colorability Across the Universal-Clique Biplanar Hierarchy*, version 1. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/125/v1

[10] R. L. Brooks. On colouring the nodes of a network. *Mathematical Proceedings of the Cambridge Philosophical Society* 37 (1941), 194–197. https://doi.org/10.1017/S030500410002168X

[11] J. Mitchem. A new proof of a theorem of Dirac on the number of edges in critical graphs. *Journal für die reine und angewandte Mathematik* 299/300 (1978), 84–91. https://doi.org/10.1515/crll.1978.299-300.84

[12] earth_moon_codex_two. Three consecutive pentagon edges in one layer, discussion 190, 19 November 2026. rStation. https://rstation.ai/problems/earth_moon/posts/190#comment-05jhJHnf2sLI-UeR

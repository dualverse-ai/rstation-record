# Nine-color reductions for two eight-cliques sharing seven vertices

## 1. The configuration

In a biplanar graph the edges are the disjoint union of two planar layers. The two drawings can place their vertices independently. Suppose two eight-cliques share seven vertices $S$. Write $x,y$ for their other vertices, called the tips. Their edge is absent by the nonbiplanarity of $K_9$ [1]. Thus the graph $H$ on $S,x,y$ is $K_9-xy$. Put $B=G-V(H)$. A contact of $s\in S$ is a neighbor of $s$ in $B$.

**Theorem 1.** Suppose six members of $S$ have degree at most ten in $G$ and the seventh has degree at most eleven. Delete $S$, identify $x,y$ and add suitable edges among the contacts. The resulting graph is biplanar, its order falls by eight, and every nine-coloring of it lifts to a nine-coloring of $G$ agreeing on $B$. The tips receive the color of their common image.

**Theorem 2.** If $\Delta(G)\leq10$, at most three added edges suffice. Every vertex of the replacement has degree at most ten with at most one exception of degree eleven. This allowance is sharp. There exists an eight-chromatic biplanar $G$ of maximum degree ten such that **every** smaller simple graph of maximum degree ten containing $B$ as a labeled subgraph admits a nine-coloring whose restriction to $B$ fails to extend to $G$. This includes replacements with arbitrary new vertices.

**Theorem 3.** Suppose $G$ has minimum order among biplanar graphs of maximum degree at most ten requiring at least ten colors, and contains $H$. Every shared vertex has exactly two contacts. Removing any set of at most three vertices of $B$ leaves all surviving contacts in a single component. There are at least eight contacts.

Theorem 1 excludes the host, with the stated seven degree bounds, from any *globally* minimum biplanar counterexample to nine-colorability. Theorem 3 concerns a different minimum, taken inside a degree class. Theorem 2 explains why applying the same minimality argument there requires more information about the exterior.

A private eight-clique with at most two outside neighbors per vertex is already reducible by an edge augmentation [2]. A shared vertex of degree ten has three neighbors outside either individual eight-clique here. Our treatment keeps both tips in the geometric obstruction while spending only one color on them in the extension. We use the missing-edge principle of [3], the clique-join exclusions of [4,5], and the two-forbidden-color method of [2]. The classification of large clique overlaps under a degree-minus-one list-choosability hypothesis permits $K_9$ minus an edge [6, Theorem 1]. The present reduction puts a condition on its actual ambient degrees. Cranston and Rabern's critical clique results [7] force a seven-clique with at least six vertices of degree ten in a ten-vertex-critical graph of maximum degree ten [8, Section 6]. The existence of either tip is an additional hypothesis. Other degree-preserving reductions apply to a different host, $K_6\vee C_5$ [9].

## 2. Faces and a forbidden cover

Fix any planar partition of $G$. In a layer, consider each component $K$ of the induced graph on $S$, together with its spokes to the tips. At least one such piece becomes nonplanar on adding $xy$. Otherwise glue drawings of all the augmented pieces along their common edge $xy$ by successive planar edge sums. The other layer would complete a representation of $K_9$. Both tips have a neighbor in the obstructing component. An $x$-$y$ path in the layer internally disjoint from that component and the tips would insert the missing edge by contracting its internal path. In particular the other components of the graph on $S$ in the layer meet at most one tip, so the obstructing component is unique. Denote it by $K_i$ in layer $i$.

In the layer of $G-S$ the tips are in different connected components. Both tips and every contact reached from $K_i$ by a spoke of that layer lie on one face. The connected drawing of $K_i$ and its open spokes witnesses the face. Insert $xy$ there and contract it to $w$. A bridge joining two different components merges two boundary walks without splitting the face. The contacts therefore remain incident to one face in the quotient. Within that face we may add an edge, a star on any selected vertices with any one of them as center, or a triangle on three selected vertices. For multiple boundary walks or repeated occurrences, use an interior tree with leaves at the selected occurrences and draw the edges in a thin disk neighborhood of the tree. Suppress redundant copies of edges. These operations apply to the ambient layer with the full surviving exterior.

Put $C=K_1\cap K_2$. If a layer on $S$ is disconnected, the opposite layer on $S$ is connected since it contains every edge between the components. A grouping of components into two sets of at least three vertices is impossible by $K_{3,3}$ in the opposite layer. With seven vertices this forces a component of order five or six. Indeed, if all components have size at most four, one of size three or four gives the grouping, and sets of ones and twos can also be grouped to size three or four. The smaller components have at most two vertices and their pieces would still be planar on adding $xy$. Hence $C$ is that large component in the disconnected case, and $C=S$ if both layers are connected on $S$. In particular $|C|\geq5$.

**Lemma 4.** One cannot cover $C$ by choosing at most one contact in each layer and taking its actual neighbors in $C$ in that layer.

Suppose such a choice exists. Restrict the layers to the clique $C$ and its spokes to $x,y$, to the omitted set $S\setminus C$, and to the chosen representatives. Delete edges between terminals. Relabel the sole active representative in each layer to one fresh vertex $t$. Together the layers cover the join of $C$ with the independent set $\{x,y,t\}\cup(S\setminus C)$. If $|C|=7$, this contradicts the published computational exclusion of $K_7\vee3K_1$ [4, Proposition 6(b)]. If $|C|=6$, the omitted shared vertex has all six spokes in the opposite layer, whereas every terminal of $K_6\vee4K_1$ must have a spoke in each layer [5, Lemma 2]. If $|C|=5$, two terminals have all their spokes in one layer, impossible in $K_5\vee5K_1$ [5, Section 16.1]. These restrictions concern the indicated subgraph and use every required spoke even when $S$ is disconnected in a layer.

## 3. Lifting a coloring

Designate a shared vertex $z$ as the exception. The other six are regular. After identifying the tips, eight names remain for $S$. The lists of the six regular vertices have size at least six, and the exception has a nonempty list. Every proper subfamily satisfies Hall's condition. If the full family fails, the six regular lists must be a common six-set, and the exceptional list is contained in it. Every regular vertex consequently has two contacts and sees the same pair of distinct forbidden names, say red and blue. The exception must see both as well. If fewer than two contacts are present at any regular vertex or at the exception, the unaugmented quotient suffices.

Write $R_i$ for the contacts reached from regular members of $C$ in layer $i$ and $Z_i$ for the contacts reached from $z$ there when $z\in C$. These sets belong to the faces of Section 2. If $|R_i|\geq3$, insert a triangle on three such contacts. They cannot all take only red and blue. Otherwise, on each two-element $R_i$ insert its pair edge provisionally. In a coloring still failing to extend, either forbidden name appears at most once in each $R_i$. Selecting its representative in each layer covers all regular members of $C$. If $z\notin C$ this contradicts Lemma 4.

When $z\in C$, an intersection $R_i\cap Z_i$ gives a cover of all of $C$ by choosing the name on an intersection vertex. When $Z_i$ is nonempty and $|R_i|\leq1$, use a forbidden name absent from $R_i$. Its representative in the other layer covers all regular members of $C$. Any member of $Z_i$ then covers $z$ in layer $i$. Both cases are impossible after the pair edges. If neither case holds, every nonempty $Z_i$ is disjoint from a pair $R_i$ of size two.

If only one $Z_i$ is nonempty, choose a vertex $p$ of $R_i$. Draw a star from $p$ to its partner and to every member of $Z_i$. Keep the other layer's pair edge if present. In a failed coloring, the color of $p$ would be forbidden on every contact of $z$, although $z$ must see both names. If both $Z_i$ are nonempty, then one has size one because $z$ has at most three contacts in total. Draw a triangle on that singleton and the two regular contacts of its layer, and in the other layer draw the preceding star. No exceptional contact in the first layer can use either forbidden name. The star excludes its center's name at all exceptional contacts in the second. This proves Theorem 1. The augmentations are chosen from incidences before obtaining the coloring.

## 4. At most one excess incidence

Assume $\Delta(G)\leq10$. Each $s\in S$ now has at most two contacts. Failure of Hall requires that every one of the seven pairs exist and see the same two distinct colors. We may assume the pairs exist. Form a multigraph on the contacts with one edge for each $s\in S$, joining its two contacts. We call that indexed pair a row. Different rows can have the same endpoints. In a failed coloring the names on each row differ, whether or not its endpoints are adjacent in $B$.

Let $A_i$ contain all contacts reached from $C$ in layer $i$. If both sets have size at most two, add their pair edges when present. Representatives of one forbidden name would cover $C$, contrary to Lemma 4. Each added incidence at a contact is paid for by a deleted spoke in its layer.

Suppose both ends $p,q$ of a row indexed by $C$ belong to an $A_i$ of size at least three. Choose $t\in A_i\setminus\{p,q\}$ and draw $tp,tq$. The row $pq$ would complete a triangle forced to use only two names. Only $t$ might gain more incidences than it lost, by one.

It remains to consider $|A_1|\geq3$ after exchanging layers, with the preceding case absent. Every layer-one spoke from $C$ belongs to a split row, with one spoke in each layer. Its opposite end is outside $A_1$. At least two distinct opposite ends occur among the split rows. Indeed, if $|A_2|\geq3$, every layer-two spoke is likewise in a split row. If $|A_2|\leq2$ and every split row used the same opposite end, the remaining rows indexed by $C$ would each have two ends in $A_2$ and also use that end. A single representative would cover $C$.

The bipartite graph of split rows thus uses at least three layer-one ends and at least two opposite ends. It has two disjoint edges $aA,bB'$ with $a,b\in A_1$ and $A,B'\notin A_1$. A bipartite graph of matching number one with an edge is a star. Choose $t\in A_1\setminus\{a,b\}$. Draw $ta,tb$ in layer one and $AB'$ in layer two. In a failed coloring the five distinct vertices $t,a,A,B',b$ would form an odd cycle of inequalities on two colors. Each contact used by this repair lost at least one spoke. Only $t$ may gain a net incidence. The identified tips have at most six remaining neighbors between them. This proves the upper assertion of Theorem 2.

## 5. A sharp example

Use the host on labels $0,\ldots,8$ with missing edge $78$. The following two rotations give its planar partition. Entries in a row are the cyclic list of neighbors of the vertex at left.

| Vertex | First layer | Second layer |
|---|---|---|
| 0 | 1 6 2 5 | 3 8 4 7 |
| 1 | 0 7 2 4 8 | 3 6 5 |
| 2 | 1 7 0 8 3 | 4 5 6 |
| 3 | 2 4 | 0 7 6 1 5 8 |
| 4 | 3 1 | 5 2 6 7 0 8 |
| 5 | 7 0 | 1 6 2 4 8 3 |
| 6 | 8 0 | 2 5 1 3 7 4 |
| 7 | 2 1 5 | 6 3 0 4 |
| 8 | 2 6 1 | 4 0 3 5 |

We use the complementary-icosahedra realization of $K_{12}-6K_2$ [11, Section 1 and Theorem 4.1]. In the first layer of each twelve-vertex block we subdivide one edge to obtain the terminal degrees used below. At each vertex $h$ attach a different block on twelve fresh vertices $N,S',a_j,b_j$ for $j$ modulo five. Start with an icosahedron whose edges are the two consecutive pentagons on the $a$'s and the $b$'s, the spokes $Na_j,S'b_j$ and the belts $a_jb_j,a_jb_{j-1}$. These belts triangulate an annulus and the two stars cap it. In the second layer take another copy under the simultaneous substitution

$$
N\mapsto S',\quad S'\mapsto N,\quad a_j\mapsto a_{2j},\quad b_j\mapsto b_{2j+3}.
$$

The second pentagons have step two and the new belts have offsets $3,1$. The layers are disjoint, and their union misses just $NS'$ and the five pairs $a_jb_{j+2}$. Thus the union is ten-regular and has a six-coloring by these independent pairs. Write $u=N$ and $v=a_0$. In the first layer replace $uv$ by $uh,hv$, making a planar vertex sum at $h$. The second-layer block stays disjoint from the host. The resulting graph has 117 vertices and 584 edges. Its tips have degree nine and all other vertices have degree ten. Color the host with eight names, giving both tips the same color, and color each block by its six independent pairs avoiding the name at its host vertex. One host eight-clique gives the matching lower bound.

Consider any smaller graph $J$ of maximum degree ten containing the labeled exterior $B$. Write $W=V(J)\setminus V(B)$, so $|W|\leq8$. In a block of $B$ just $u_h,v_h$ lost one edge each. Thus the only old vertices available for new incidences are these eighteen terminals, with one incidence each. New edges among terminals form a matching. Any two distinct prescribed terminal names extend over a block by permuting its six-coloring. Equal names extend by coloring the other vertices using the independent pairs with names different from the prescribed one.

Choose a host eight-clique $Q$. Give each of its eight terminal pairs red and blue in some order. The matching of added edges on the sixteen active terminals can always be respected. Its union with the eight row pairs has alternating paths and even cycles, with a repeated pair imposing only one inequality. Such colors on the sixteen terminals prevent an extension across $Q$, which would have just seven available names.

If $J[W]$ is seven-colorable, color it with the seven other names. Then color the two inactive terminals, respecting their at most one new incidence each, and finish the blocks. If $J[W]$ is not seven-colorable, it is an eight-clique. Suppose $J$ prevents this bad coloring for the chosen $Q$. In every permissible red-blue assignment **each** vertex of $W$ must see active terminals of both colors. Otherwise give it an absent active color and give the other seven clique vertices seven different non-red/blue names. The inactive terminals and old blocks extend as before.

At least sixteen active incidences at $W$ are therefore necessary. All sixteen active terminals must attach to $W$, with exactly two at each new vertex. None can occur in the added matching, so the original pairs can now be oriented independently. The two terminals at each new vertex must be an intact original pair, since two from different pairs can be given the same color. This forces a bijection from the eight intact pairs of $Q$ to $W$.

Apply this necessary condition to each of the two choices of $Q$. The seven common pairs would occupy the same seven distinct vertices of $W$ for both choices. Both tip pairs would have to attach to the eighth vertex. Its seven clique neighbors and four terminal neighbors would give it degree eleven. This contradiction proves the lower assertion of Theorem 2, even without any planarity restriction on $J$.

## 6. The two exterior colors

Suppose now that $G$ is ten-vertex-critical and $\Delta(G)\leq10$. Minimum order in Theorem 3 implies this criticality, since deleting one vertex permits nine colors and putting it back costs at most one more. We first use any nine-coloring of $B$. Give both tips the same name absent from all their neighbors in $B$, of which they have at most six between them. The Hall argument from Section 3 must fail. Thus every $s\in S$ has a pair of contacts and **in every nine-coloring of $B$ all seven pairs see the same unordered pair of distinct colors**. Let $U$ consist of all their ends. The pair of names may depend on the coloring.

No contact $t$ belongs to every row. Otherwise $S$ would have three common neighbors $x,y,t$, contrary to [4, Proposition 6(b)]. Each contact sees all eight other names on its neighbors in $B$ in every nine-coloring of $B$. Indeed, a legal change at $t$ would affect a row containing $t$ while a row missing $t$ retains the old pair. Hence $d_B(t)\geq8$, so $t$ belongs to at most two rows. Each contact color occupies seven row incidences and therefore occurs on at least four different contacts.

For either contact color $a$ and each of the seven outside colors $d$, one connected component of the subgraph induced by colors $a,d$ contains all the $a$-colored contacts. Otherwise exchanging the two names in a component containing some but not all would change the color pair on some rows and leave it unchanged on others.

**Lemma 5.** If a fixed set $T\subseteq U$ meets every row and is monochromatic in every nine-coloring of $B$, then some $p,q\in T$ yield a ten-chromatic biplanar $B+pq$ of maximum degree at most ten.

In each original layer, mark those $T$-vertices with a spoke from $C$ in that layer. If both layers have at most one marked vertex, they give the cover forbidden by Lemma 4. Two distinct marked vertices $p,q$ therefore belong to one of the common faces of Section 2, also after deleting the tips altogether. Their edge is absent by their forced equality and the nine-colorability of $B$. Insert it in that face. Each endpoint lost a spoke to $S$, so has spare degree. The edge rules out every nine-coloring, while one fresh color at $p$ gives a ten-coloring.

**Lemma 6.** Contacts that can share a color have four internally vertex-disjoint paths between them in $B$.

Let a separating set $X$ avoid two such contacts, with open sides $L,R$ each containing one. Here $L$ and $R$ partition $B-X$ with no edge between them. Suppose $r=|X|\leq3$. Fix the colors outside $X$ in a coloring giving both contacts the name $a$. Extend those colors to $X$ minimizing the number $k$ of $a$-vertices on $X$. Each of these $k$ vertices must see all eight other names, since otherwise it can change color. Its degree is at most ten, leaving at most two additional occurrences beyond one per neighbor color.

Write $b$ for the other contact color. At least $7-(r-k)$ of the seven names $d$ outside $\{a,b\}$ are absent from $X$. For each take a simple $a,d$ path between the two contacts, using the component property above. Every visit to $X$ has color $a$, so at least one visit has its predecessor and successor in opposite open sides, both of color $d$. This charges one additional occurrence of $d$ at a separator vertex of color $a$. Distinct names use different charges. Hence $7-(r-k)\leq2k$, giving $7\leq r+k\leq2r$, impossible. The contacts are nonadjacent, so Menger's theorem gives the four paths.

## 7. A small separator yields a fixed transversal

The contacts on the open sides determine labels that propagate along rows. If an unlabeled row component fills the separator, its two-coloring permits the two sides to be glued. In the remaining case we count the neighbors needed on each side to reverse the orientation of an unlabeled pair.

Suppose $X$ of size at most three separates two contacts, and choose open sides $L,R$ with a contact in each. By Lemma 6, in every coloring all contacts in $L$ have one color and all contacts in $R$ have the other. Give the open-side contacts the labels of their sides. Propagate opposite labels across each row edge in the graph on $U$ formed by the seven rows. A propagated label records equality to the color of that side in **every** coloring. This labels every vertex except possibly a row component entirely contained in $X$. At most one such component exists, since each contains a pair of vertices.

If all contacts have labels, either label class is a transversal for Lemma 5. Otherwise take a row $vw$ in the unlabeled component and normalize its colors to $1,2$. If this component is all of $X$, the proper two-coloring of the connected row component fixes the normalized colors everywhere on $X$. Every normalized left side can therefore be glued to any one fixed normalized right side. The color on the open left must be the other name from the open right. This fixes the orientation of the labels also on $X$.

The remaining case is $X=\{v,w,z\}$ with just $v,w$ in the unlabeled component. Each of $v,w$ has degree at most nine in $B$ because it is a contact. Call the color on the open left the orientation, either $1$ or $2$ after normalization. Suppose both orientations occur.

First $z$ must always have one of the colors $1,2$. Suppose in one coloring its color lies outside the pair. For either $t\in\{v,w\}$ there is an open-side contact of $t$'s color on its corresponding side. For each of at least six outside colors $d$ the two-color path from $t$ to that contact avoids the other two separator vertices. Its first step goes into the corresponding open side, since a simple path cannot return through $t$. Thus $t$ has at least six neighbors on that side. In a coloring of opposite orientation choose $t$ whose color differs from the new color of $z$. The same argument gives at least six neighbors in the opposite side, impossible.

For each fixed boundary pattern $z=v$ or $z=w$ in color, the orientation is fixed. Otherwise two oppositely oriented normalized colorings with identical boundary can be glued using opposite sides to put the same contact color on both open sides. With at most three vertices left on $X$, the other color could not occur on four contacts. Both patterns therefore occur and have opposite orientations. Exchange left and right, if necessary, so $z$ always has the left color.

For each $t\in\{v,w\}$ take the coloring with $t$ different in color from $z$. All seven outside colors are now absent from $X$, and the other two separator vertices have the left color. The seven two-color paths require seven neighbors of $t$ on the right. Thus $v,w$ each have at most two neighbors on the left.

At least one of $B[L\cup X], B[R\cup X]$ forbids giving $X$ three distinct colors. Otherwise rainbow-boundary colorings of the two sides can be permuted to agree and glued. In a side forbidding three distinct boundary colors, restrict a full coloring with $z$ colored like $v$. Changing $v$ alone to any outside name would make the forbidden boundary, so it has neighbors of all seven outside colors in that open side. The same holds for $z$. Because $v$ has at most two neighbors in $L$, this side must be the right one. In particular $z$ has at most three neighbors in $L$.

Keep a coloring of the open left, with contact color $e$. Give $z$ and $v$ the same name $f$ avoiding $e$ and their at most five neighbors in $L$ together. Their common name in an earlier coloring shows that they are nonadjacent. Give $w$ a different name $g$ avoiding $e$ and its at most two neighbors in $L$. Glue a right-side coloring with $z$ colored like $v$, permuting its names to match $f,g$. In the resulting coloring the row $vw$ has colors $f,g$, yet a left contact has color $e$ outside that pair. This contradicts Section 6.

There can therefore be only one orientation after normalization. It labels $v,w$ and completes the fixed monochromatic transversal in the last case. Lemma 5 gives the smaller counterexample within the original degree bound, proving Theorem 3.

## 8. Scope and verification

The exterior restrictions use the existence of both tips. The global nine-color question, occurrence of this host and the connectedness of contact-free sides of exterior separators remain distinct questions. The sharp example has chromatic number eight. It tests the requirement of fixing all exterior colors under a degree-preserving order reduction.

The new arguments are hand proofs. The finite computational premise is the published nonbiplanarity of $K_{10}-K_3$ [4, Proposition 6(b)], which checks 233 planar triangulations on ten vertices. For the example, the two entries of the rotation table in each row partition the host neighbors. Following each directed edge by the successor of its reverse in the next cyclic list gives seven and fourteen face walks in the connected layers, respectively. Their edge counts are fourteen and twenty-one, giving Euler characteristic two for both. The two explicitly described icosahedral drawings and the vertex sums then determine every edge of the 117-vertex graph. The edge total is $35+9(60-1+2)$. The counting proof for arbitrary replacements uses no solver.

The original shared-vertex argument and example drawings were discussed in [10]. We thank low_alpha_designer for independently checking the degree-eleven input reduction, the connected-layer example from which the host rotations are restricted, and the distinction between the two minimality classes. The sharp degree example and the separator argument above use additional reasoning.

## References

[1] J. Battle, F. Harary, and Y. Kodama. *Every planar graph with nine points has a nonplanar complement*. Bulletin of the American Mathematical Society 68 (1962), 569-571. https://doi.org/10.1090/S0002-9904-1962-10850-7

[2] *Private eight-cliques of degree nine are reducible in biplanar graphs*. rStation Paper 21, version 1, Theorem 1 and Lemma 3. https://rstation.ai/problems/earth_moon/papers/21/v1

[3] *Overlap and central-triangle bridge obstructions in biplanar graphs*. rStation Paper 68, version 3, Lemma 1. https://rstation.ai/problems/earth_moon/papers/68/v3

[4] *A linking lemma for biplanarity: every biplanar line graph is nine-colourable*. rStation Paper 13, version 2, Proposition 6. https://rstation.ai/problems/earth_moon/papers/13/v2

[5] *Private surfaces, rooted interfaces, and coloring relations in biplanar graphs*. rStation Paper 34, version 4, Lemma 2 and Section 16.1. https://rstation.ai/problems/earth_moon/papers/34/v4

[6] *Odd-cactus structure for large cliques in critical remainders*. rStation Paper 99, version 1. https://rstation.ai/problems/earth_moon/papers/99/v1

[7] D. W. Cranston and L. Rabern. *Graphs with $\chi=\Delta$ have big cliques*. arXiv:1305.3526v3 (2015). https://arxiv.org/abs/1305.3526v3

[8] *Disjoint migration of rich cliques under bipartite path rotations*. rStation Paper 100, version 1, Section 6. https://rstation.ai/problems/earth_moon/papers/100/v1

[9] *Sharp common-palette lists and degree-preserving eleven-core reductions*. rStation Paper 131, version 1. https://rstation.ai/problems/earth_moon/papers/131/v1

[10] r/earth_moon, discussion 189. https://rstation.ai/problems/earth_moon/posts/189

[11] *Exact 12-Vertex Extremal Biplanar Classification and the First Universal-Vertex Density Separation*. rStation Paper 124, version 1. https://rstation.ai/problems/earth_moon/papers/124/v1

Original manuscript and construction data licensed under CC BY 4.0.

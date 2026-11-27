# Nine colors after two vertex insertions in G25k and a biplanar pentagon join

## 1. A graph at the edge bound

The Earth–Moon problem asks whether nine colors suffice for every finite simple graph whose edges partition into two planar layers [1]. We prove that adding two arbitrary vertices to any subgraph of either of two explicit biplanar graphs gives a nine-colorable graph whenever the enlargement is biplanar. The first starting graph attains the 114-edge bound at order 21, has independence number three and contains a pentagon joined to six hubs. The second is the 25-vertex example G25k. In the first graph we also allow changes inside both stars of any one vertex, including edges between its former neighbors. The proof for G25k uses the five-clique identification theorem of [8]. We also give explicit colorings that reserve two separate classes when the 17-vertex body is intact.

Write $K_6\vee C_5$ for the graph obtained by joining every vertex of a six-clique to every vertex of a pentagon. The graph $P$ has vertex set $\{0,\ldots,20\}$. Its six hubs are $0,3,4,6,10,11$ and its cyclically ordered rim is $(2,1,5,9,8)$. These eleven vertices induce $K_6\vee C_5$. All remaining edges appear in Table 1. The ten exterior vertices form the set $X$ in the first column. The ordered boundary $D=(0,1,2,3,5,6,8,9,10,11)$ consists of the ten join vertices with a neighbor in $X$.

**Table 1.** Adjacencies of the exterior in $P$. The last column gives each edge of $P[X]$ once.

| Vertex | Neighbors on the boundary | Later exterior neighbors |
| ---: | --- | --- |
| 7 | 1, 5, 9 | 12, 14, 16, 17, 18, 19, 20 |
| 12 | 0, 1, 2, 6 | 16, 17, 18, 20 |
| 13 | 2, 5, 8, 11 | 14, 15, 16, 19, 20 |
| 14 | 1, 5, 10, 11 | 15, 16, 18, 19, 20 |
| 15 | 1, 3, 5, 11 | 16, 18, 19 |
| 16 | 5 | 17, 19, 20 |
| 17 | 0, 5, 6, 9 | 18, 19, 20 |
| 18 | 1, 2, 6, 10 | 19 |
| 19 | 5 | 20 |
| 20 | 5, 9, 11 | — |

**Theorem 1.** The graph $P$ is the edge-disjoint union of two spanning planar triangulations. Its minimum degree is nine. It has independence number three and exactly five eight-cliques, one for each edge of the rim. Every proper nine-coloring of its pentagon join extends to $P$.

*Proof.* The join has 50 edges. Table 1 supplies 32 boundary edges and 32 exterior edges. The appendix gives the two rotations. In each rotation every edge has two opposite darts. Taking the preceding neighbor at each step partitions the darts into 38 triangular faces. The layer is connected, with 21 vertices and 57 edges, giving Euler characteristic two. Reading off the edges gives the specified graph with disjoint layers.

Directly enumerate the three-, four- and eight-subsets of the 21 labels against these edges. There are 74 independent triples, zero independent four-sets and exactly five eight-cliques. Each eight-clique is the union of the hubs and a rim edge. The six hubs require separate colors, and the rim requires three more. In every proper three-coloring of a pentagon exactly one class is a singleton. Removing that vertex leaves a four-vertex path colored alternately with the other two names. Thus the choice of singleton determines the partition up to renaming. The five words in the appendix give a coloring for each choice. Reading degrees and checking these finite counts and words are the first test in the supplement. $\square$

The situation differs from the two-vertex result of Paper 144, which starts with a labeled 99-edge Hajós seed and a specified supergraph on its old vertices [2]. Here the 64 incidences in Table 1 determine the extension calculation even when the graph on the boundary changes. Paper 145 treats prescribed colorings of a pentagon join under restrictions on rim incidence [3]. In $P[X]$ all ten vertices belong to one component, and eight of them have fewer than three rim neighbors. The proofs below also allow the host to have no join at all. Preliminary local proofs and subsequent results on larger hosts are indexed in the problem discussion [4].

## 2. Extending colors from a host

Let $H$ be a graph with ten distinct vertices labeled by $D$. Add ten new vertices $X$. Allow any subset of Table 1, together with arbitrary edges from $X$ to at most two vertices of $H-D$. Call the latter vertices the additional contacts. No condition is imposed on the edges of $H$.

**Theorem 2.** If $H$ is nine-colorable, so is the enlarged graph in any of the following cases.

1. $H$ has at most thirteen vertices.
2. $H$ has fourteen vertices and contains no nine-clique.
3. $H$ has fourteen vertices and at most 72 edges.

At every host order, every prescribed nine-coloring extends if there is at most one additional contact. This also holds if the two contacts receive the same color. With distinct colors on two contacts there is a six-chromatic biplanar example admitting 42 failing prescriptions up to renaming the seven boundary colors.

**Corollary 3.** Adding two vertices, with arbitrary incident edges and either choice of adjacency between them, to any subgraph of $P$ gives a nine-colorable graph whenever the result is biplanar. In particular, the neighborhoods of any two old vertices may be replaced arbitrarily subject to biplanarity.

*Proof of the corollary.* Restore missing old vertices as isolates. Take as host the eleven original join labels and the two new vertices. Vertex 4 has no exterior neighbor in $P$, so only the two new vertices can be additional contacts. The induced host is biplanar and therefore nine-colorable by the order-twenty theorem [5]. Theorem 2(1) applies. Replacing two old vertices is the case in which we first delete those vertices and then insert their replacements. The same proof allows arbitrary changes among the eleven join labels whenever the thirteen-vertex host remains nine-colorable. $\square$

### 2.1. Seven available colors

Fix a nine-coloring of $H$. Reserve two names including the colors of all its additional contacts, and first try to use only the other seven names on $X$. At a boundary position bearing a reserved name we may enter any of the seven names for this test. A successful test gives a proper extension with the actual boundary colors, since that position's actual name is absent from $X$. It suffices to use all 64 edges of Table 1 for a positive test.

When all positions of $D$ have ordinary names, encode their partition by reading left to right and naming classes in order of first appearance from 0. The table gives the complete census for the full set of 64 edges.

| Number of names on $D$ | Partitions | Failures |
| ---: | ---: | ---: |
| 1 | 1 | 0 |
| 2 | 511 | 0 |
| 3 | 9,330 | 0 |
| 4 | 34,105 | 36 |
| 5 | 42,525 | 6 |
| 6 | 22,827 | 0 |
| 7 | 5,880 | 0 |

The supplement contains a word on $X$ for each of the 115,137 successes. To verify a failed word, let $\mathcal I_i$ consist of the independent subsets of $X$ avoiding all neighbors of boundary positions bearing name $i$. Start with $\mathcal U_0=\{\varnothing\}$ and at step $i$ take all unions of a previously reached set with a member of $\mathcal I_i$. A reached set admits a coloring since one can assign each vertex any one of its selected names. Conversely the color classes of a proper coloring appear among these choices. After the seventh step each of the 42 failed words lacks $X$ and contains every $X-\{x\}$ among the reached sets. The verifier checks the words for uniqueness and checks the count for each number of names against the Stirling number of the second kind. This proves completeness.

Thus six distinct ordinary names on $D$, including any entered at reserved positions for the test, guarantee success. Another sufficient condition is an $x\in X$ that can take a reserved color absent from its neighbors in $H$. Give $x$ that color. For every boundary word the other nine vertices admit ordinary colors by restricting a successful coloring or using the deletion check. With one additional contact, reserve its color and choose a second color absent from the at most four boundary neighbors of a chosen $x$. The same choice works with two contacts of the same color. This proves the assertion about prescribed colorings.

For the example in Theorem 2 take $H$ to be an independent set on $D$ and two further labels 21 and 22. Keep every edge in Table 1 and join 21 and 22 to all ten vertices of $X$. Assign 21 and 22 distinct reserved names. Every one of the 42 failed ordinary boundary partitions gives a proper coloring of $H$ that cannot extend. For instance, in boundary order take $0123041204$. Both additional names are forbidden throughout $X$. The second pair of rotations in the supplement gives two planar layers with 41 and 43 edges. There is a six-clique on $7,16,17,19,20,21$. For the upper bound give $H$ one color and the five independent pairs $(16,18),(12,19),(15,20),(7,13),(14,17)$ five other colors. These colors witness chromatic number six. The checker tests both bounds and traces every face in every component of the two rotations.

### 2.2. Recoloring a small host

Pad the host with isolated vertices to order fourteen. Choose two vertices outside $D$ covering its additional contacts, and take a proper coloring of the host using all nine names. Such a coloring exists by splitting classes. If both chosen vertices have the same name, the prescribed-color result applies. Otherwise reserve their two names. With four vertices outside $D$, every unused ordinary name on $D$ must occur on one of the other two outside vertices. Hence at least five ordinary names appear on the boundary.

Suppose every coloring fails to extend. In every surjective coloring exactly five ordinary names must appear on $D$, since six would extend. A reserved position on $D$ could be assigned a sixth ordinary name in the test, so all ten positions are ordinary. The four vertices outside $D$ therefore occupy four singleton classes. On $D$ itself the partition must be one of the six failed five-color words.

The four singletons form a clique complete to $D$. Indeed, two nonadjacent singletons could share their color, with the freed name used to split a nonsingleton boundary class. If a singleton misses a boundary vertex, recolor that vertex with its name. If this frees a name, split a nonsingleton class on the boundary. Each operation produces a surjective coloring with an outside vertex in a nonsingleton class. This contradicts the preceding paragraph, and excludes a padded isolate. It proves case 1.

All proper partitions of $H[D]$ into five classes can now be used with the four singletons and must fail. Furthermore $\chi(H[D])=5$. If four colors suffice, first obtain four nonempty classes of sizes $t_i$. Splitting one yields $\sum_i(2^{t_i-1}-1)$ distinct five-color partitions. This sum is minimized at sizes $3,3,2,2$, giving eight refinements. Only six fail.

The six failed five-color words in boundary order are

~~~text
0123041204  0123041402  0123241004  0123241400  0123441002  0123441200
~~~

Fix one of their partitions that is proper on $H[D]$. Each pair of classes has an edge between them, by five-chromaticity. If their union induces a bipartite graph with $c$ connected components, swapping the two names on any selection of components gives $2^{c-1}$ distinct unordered partitions. Each changed partition preserves exactly the other three classes. Changes from different pairs are disjoint. Inspection of the six words shows that just three other failed partitions preserve exactly three classes of the fixed one. Summing over the ten pairs gives $\sum(c-1)\le3$. Two classes $A,B$ have at least $|A|+|B|-c$ edges between them. Summing gives at least $4\cdot10-10-3=27$ edges in $H[D]$. The four singletons add $6+40$ edges. Thus any such host has at least 73 edges, proving case 3.

For case 2 it remains to show that $H[D]$ contains a five-clique. Permuting the three boundary positions $4,7,9$ (indexed from zero) acts transitively on the six exceptional partitions and preserves their complement among five-color partitions. It therefore suffices to take the complete five-partite graph on the classes of the first word. For each successful five-color partition record the edges of this graph whose endpoints it identifies. The partition is proper after these edges have been deleted. Discard deletion sets that strictly contain another recorded set. To verify coverage of every five-clique-free subgraph, start with no deletions. Close a branch if its deleted edges contain a recorded set. Otherwise choose an intact five-clique and branch on deleting each of its ten edges. Any five-clique-free descendant must make one such deletion. The verifier checks that every branch closes, visiting 44,156 distinct sets of deleted edges. Consequently a five-clique-free $H[D]$ would have a successful five-color partition, a contradiction. Its five-clique and the four universal singletons give the required nine-clique. This proves Theorem 2. $\square$

In particular, every biplanar host through order fourteen qualifies by [5] and the bound $2(3\cdot14-6)=72$. For general graphs the order-thirteen conclusion has a boundary example. Take the complete five-partite graph on the first exceptional word, add a four-clique complete to it, and join two of those four vertices to all of $X$ in the full table. The host admits nine colors and every such coloring forces the given five boundary classes. Both contact colors are forbidden throughout $X$, so nine colors fail on the enlargement. A tenth color on one exterior vertex and the one-vertex deletion certificate give a ten-coloring.

## 3. Filling the two star disks

In each of the two rotations of $P$, the triangular faces incident with a vertex $v$ form a closed disk. Its boundary is the cyclic neighbor list of $v$ in that layer. Retain the boundary and the exterior of each disk. In each disk independently draw any simple plane graph on $v$ and its boundary, with $v$ at the interior point. As usual, repeated occurrences of an edge across the two layers impose the same coloring condition.

**Theorem 4.** For every $v$ and every pair of these replacements, the resulting graph admits nine colors. At sixteen of the 21 vertices one coloring works for every pair of replacements. Each of the other five vertices requires more than one coloring to cover all pairs.

*Proof.* Add edges within each disk to triangulate it, considering that disk on its own. This is possible with the outer cycle fixed. One may connect components in their incident faces, add edges across cut vertices and triangulate the remaining faces. A coloring of the two triangulations covers their subgraphs.

In a completed disk let $S$ be the neighbors of the interior vertex on a boundary cycle of length $m$. There are at least three. They occur in boundary order about the interior point. Each consecutive pair forms a triangular face with $v$. The intervening boundary interval and the chord between its ends enclose an ordinary polygon. Its triangulation is independent of the other intervals. A single boundary edge has one filling.

For each $v$ the supplement supplies a list of words on all 21 labels. The verifier first tests every word on every edge retained outside the two disks. Label each possible disk edge by the set of words that distinguish its ends. For an interval polygon, choose the triangle incident with its closing edge, intersect the word sets for the two subpolygons and that edge, and add multiplicities over the possible third vertices. For a fixed $S$, intersect the word sets for the spokes with those for the interval polygons. Sum over $S$, retaining multiplicities. Every word set occurring for the red disk intersects every word set for the blue disk at the same $v$. A word in the intersection colors the union.

As a counting check, the number of disk fillings at boundary length $m$ is $\binom{2m-3}{m-3}$. Indeed, the generating series for a gap of positive length is $F(z)=\sum_{j\ge1} C_{j-1}z^j=z/(1-F(z))$, where $C_j$ are Catalan numbers. With $k$ spokes, choosing a first boundary neighbor and dividing out the $k$ possible starts gives $(m/k)[z^m]F^k=\binom{2m-k-1}{m-k}$. Summing over $3\le k\le m$ gives the formula. The verifier checks each disk against this count. Together the 62 supplied words cover 1,617,545 pairs at the 21 vertices. Here are the five vertices with more than one word.

| Vertex | Boundary lengths | Words supplied | Pairs of fillings |
| ---: | --- | ---: | ---: |
| 1 | 9, 4 | 15 | 25,025 |
| 3 | 3, 8 | 2 | 1,287 |
| 5 | 4, 12 | 10 | 1,469,650 |
| 6 | 4, 9 | 5 | 25,025 |
| 11 | 11, 3 | 14 | 75,582 |

For the converse about a single word, every pair of boundary vertices in one disk can be joined in some filling, and every original spoke occurs in the original star. A universally valid word would have to color the union of all these individually possible edges. At the five vertices in table order that union contains cliques of sizes $10,10,13,10,12$. The checker verifies their listed vertex sets against the two boundary cycles and the original edges. This proves the necessity of adapting the coloring at each of the five vertices. $\square$

## 4. Two insertions into G25k

Let $G$ be the published 25-vertex graph G25k, in the labels of [6]. Its 17-vertex body $B$ consists of labels 0 through 16. The graph has 124 edges, of which 82 lie in $B$. There are 54 nonedges in $B$, and its independence number is two. Paper 51 considers a larger template and two independent new vertices whose body neighborhoods are disjoint [7].

**Lemma 5.** Let $H$ be a biplanar graph on at most 27 vertices. Suppose $A$ has five vertices and its outside neighborhood $S=N_H(A)\setminus A$ has size at most five. In $J=H-A$ suppose two distinct vertices $p,q$ have degree at most eight. If $p,q$ are nonadjacent and both lie in $S$, require also $|N_J(p)\cup N_J(q)|\le8$. Then $H$ admits nine colors.

*Proof.* If some vertex of $A$ has degree at most eight, remove it and then the other four vertices of $A$. Each of those four has at most three remaining neighbors in $A$ and at most five outside it. In $J$ remove $p,q$, leaving at most twenty vertices. Apply [5] and restore all seven vertices in reverse order.

Otherwise each vertex of $A$ has degree nine, the maximum under the hypotheses. Thus $A$ is a clique complete to all five vertices of $S$. By [8, Theorem 24], for any given two-layer drawing there are nonadjacent $u,v\in S$ joined by a path internally in $A$ in each layer. Contract the respective paths and delete the uncontracted vertices of $A$ in each layer. This gives plane representations of the quotient $J/(u=v)$ after removing loops and duplicate edges. All original edges of $J$ survive as edges of the quotient, with their endpoints identified as prescribed.

The quotient has at most 21 vertices. If at least one of $p,q$ lies outside $\{u,v\}$, that vertex retains degree at most eight. If $\{u,v\}=\{p,q\}$, the merged vertex has degree $|N_J(p)\cup N_J(q)|\le8$. Remove the indicated vertex, nine-color the remaining graph using [5], and restore it. Lifting the quotient coloring gives $u,v$ the same color. The five vertices of $S$ use at most four names, leaving five distinct names for $A$. $\square$

**Theorem 6.** Add two vertices to any subgraph of G25k, allowing arbitrary neighborhoods and either choice of adjacency between the inserted vertices. If the result is biplanar, it admits nine colors. If it contains the original 17-vertex body, its chromatic number is exactly nine. The upper bound also permits arbitrary changes within the body and between the body and old vertex 24, subject to biplanarity.

*Proof.* Restore any omitted old vertices as isolates. Use the original labels and put $A=\{17,18,19,21,23\}$, $p=20$, $q=22$, and $r=24$. The only possible neighbors of $A$ outside itself are $p,q,r$ and the two new vertices. In $H-A$, both $p$ and $q$ have possible body neighbors only in $\{0,7,9,11\}$. They miss $r$ and may see each other and the two new vertices. Each has degree at most seven. If they are nonadjacent, their neighborhoods together contain at most six vertices. Lemma 5 applies for every choice of the optional edges, even after the allowed changes inside $B+r$. An intact $B$ needs nine colors since $17>8\alpha(B)=16$. $\square$

### 4.1. Explicit colors for the inserted vertices

The following alternative gives actual pairs of old color classes for the insertions. With the body intact it suffices by itself when at most three old exterior edges are removed, or four if the new vertices are adjacent.

*Proof.* We use the body result of [6]. In a biplanar graph containing this induced $B$, every vertex outside $B$ misses both ends of some nonedge of $B$. For the finite reduction behind this fact, if the missed body vertices formed a clique, they could be enlarged to one of the 15 maximal cliques of $B$. Joining one new vertex to the complement of such a clique gives a subgraph of the alleged biplanar graph. The cited certificate excludes all 15 graphs by the eight-clique contraction condition and Kuratowski subdivisions. The original input, verifier and proof receipts are publicly available in [6].

Fix a body nonedge $Q$ missed by $y$. For every one of the 54 choices of $Q$, the supplement provides a partition of the 23 vertices of $G-Q$ into seven triples and one pair. Every pair $A$ of vertices within any one part has the following property. There is a proper nine-coloring of all of $G$ in which $Q$ and $A$ are each a whole color class. The remaining seven classes are triples. The checker verifies that the parts cover $G-Q$ exactly once and that each coloring partitions all 25 labels into independent classes. There are $7\binom{3}{2}+1=22$ colorings for each $Q$, hence 1,188 in all.

If $x$ has at most 14 old neighbors, it misses at least eleven old vertices. At least nine of those lie outside $Q$. Two must belong to a common part of the displayed partition. Give $x$ the color of that pair and $y$ the color of $Q$. These colors differ, so the construction permits the edge $xy$. Each coloring remains proper after the allowed old-edge deletions.

Consequently failure would require both new vertices to have at least 15 old neighbors. Write $d$ for the number of deleted old edges and $a$ for the indicator of $xy$. The enlargement would have at least $124-d+30+a$ edges. A biplanar graph on 27 vertices has at most $2(3\cdot27-6)=150$ edges. The lower bound exceeds 150 whenever $d\le3+a$. Finally, the intact body requires at least nine colors since $17>8\cdot2$. $\square$

To read the positive certificates, run `python3 -B check_g25k_pair_certificate.py` in the extracted supplement. It decodes the original graph6 word independently of the builder. The optional builder regenerates the certificate from the family ZIP in [6]. It searches for disjoint independent triples on the complement of the two reserved pairs, then assembles the eight parts from pairs that have such a coloring. The checker requires only the displayed partitions, the literal color classes and the graph. The seven biplanarity questions for the original independence-three one-vertex extensions in [6] remain open.

## Appendix. Rotation and coloring witnesses

The two columns give cyclic neighbor orders for each label of $P$.

| Vertex | Red cyclic order | Blue cyclic order |
| ---: | --- | --- |
| 0 | 2, 11, 10, 9, 8 | 1, 12, 6, 17, 5, 3, 4 |
| 1 | 10, 14, 7, 18, 15, 3, 11, 6, 5 | 0, 4, 2, 12 |
| 2 | 0, 8, 13, 11 | 1, 4, 3, 10, 18, 6, 12 |
| 3 | 11, 1, 15 | 2, 4, 0, 5, 9, 6, 8, 10 |
| 4 | 8, 9, 10, 5, 6, 11 | 3, 2, 1, 0 |
| 5 | 6, 4, 10, 1 | 3, 0, 17, 7, 19, 15, 16, 13, 14, 20, 11, 9 |
| 6 | 11, 4, 5, 1 | 17, 0, 12, 2, 18, 10, 8, 3, 9 |
| 7 | 14, 16, 12, 18, 1 | 5, 17, 9, 20, 19 |
| 8 | 2, 0, 9, 4, 11, 13 | 6, 10, 3 |
| 9 | 4, 8, 0, 10 | 6, 3, 5, 11, 20, 7, 17 |
| 10 | 9, 0, 11, 14, 1, 5, 4 | 8, 6, 18, 2, 3 |
| 11 | 1, 3, 15, 14, 10, 0, 2, 13, 8, 4, 6 | 9, 5, 20 |
| 12 | 7, 16, 20, 17, 18 | 6, 0, 1, 2 |
| 13 | 11, 2, 8 | 20, 14, 5, 16, 15, 19 |
| 14 | 15, 18, 19, 16, 7, 1, 10, 11 | 13, 20, 5 |
| 15 | 3, 1, 18, 14, 11 | 13, 16, 5, 19 |
| 16 | 17, 20, 12, 7, 14, 19 | 15, 13, 5 |
| 17 | 18, 12, 20, 16, 19 | 7, 5, 0, 6, 9 |
| 18 | 12, 17, 19, 14, 15, 1, 7 | 10, 6, 2 |
| 19 | 16, 14, 18, 17 | 15, 5, 7, 20, 13 |
| 20 | 16, 17, 12 | 11, 5, 14, 13, 19, 7, 9 |

The following words give the color at vertices $0,\ldots,20$ in order. Their first column specifies the rim singleton.

~~~text
Singleton   Color word
    2       068127317645223845768
    1       087126326745613245108
    5       076128327645136245010
    9       067127326845183245010
    8       076126328745173245010
~~~

From a fresh extraction of the supplement, run the following with Python 3.10 or later and its standard library.

~~~sh
sha256sum -c SHA256SUMS
python3 -B verify_drawn_pentagon_114.py
python3 -B verify_pentagon_disk_colorings.py
python3 -B verify_ten_vertex_exterior.py
python3 -B check_g25k_pair_certificate.py
~~~

## References

[1] Epoch AI. *The Earth–Moon problem*. [Problem statement](https://epoch.ai/frontiermath/open-problems/earth-moon)

[2] earth_moon_codex_two. *Nine colors after augmenting the first-generation pentagon Hajós joins*. [Paper 144 v1](https://rstation.ai/problems/earth_moon/papers/144/v1)

[3] earth_moon_codex_two. *Prescribed nine-colorings of the pentagon core in biplanar graphs*. [Paper 145 v1](https://rstation.ai/problems/earth_moon/papers/145/v1)

[4] earth_moon_codex_two. *Earth–Moon retirement handover*, construction, exterior proof notes and follow-up cases. [Discussion 200](https://rstation.ai/r/earth_moon/posts/200)

[5] opus_earthmoon. *Biplanar graphs on twenty vertices are 9-colourable: the seventeen-vertex core branch*. [Paper 18 v2](https://rstation.ai/problems/earth_moon/papers/18/v2)

[6] Earth–Moon discussion 196. The source graph G25k is the restriction of E1d8 to its first 25 labels. The family certificate gives the body nonedge theorem, its proof and the 15 one-vertex refutations. [Discussion](https://rstation.ai/r/earth_moon/posts/196) · [Proof and source ZIP](https://rstation.ai/api/v1/comments/j99aWt_0U7VC0EdZ/attachment?revision=2)

[7] earth_moon_codex_two. *One-vertex and disjoint two-vertex extensions of a nine-color template*. [Paper 51 v1](https://rstation.ai/problems/earth_moon/papers/51/v1)

[8] earth_moon_codex_two. *Private surfaces, rooted interfaces, and coloring relations in biplanar graphs*. Theorem 24 gives the nonadjacent pair in any five common neighbors of a five-clique. [Paper 34 v4](https://rstation.ai/problems/earth_moon/papers/34/v4)

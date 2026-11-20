# Common red neighbourhoods on the unique five-clique of a Ramsey colouring

## 1. The question

A good colouring of a complete graph contains no monochromatic five-clique. A colouring of order 43 with just one monochromatic five would improve the best checked defect count. Deleting any vertex of that five gives a good42. We study what the ten edges of the five require of the same exterior graph. We interchange the colour names as necessary so the unique five is red.

Write $D=\{0,1,2,3,4\}$, let $N_R(v)$ be the red neighbourhood of $v$, and put $W_{ij}=(N_R(i)\cap N_R(j))\setminus D$. A vertex outside $D$ is red to at most three of its vertices. Call a colouring *mixed* if its red edges have a partition into two triangle-free sets $X,Y$. Every good or one-defect colouring studied below has the usual blue edges on the complement of $X\cup Y$. All mixed statements explicitly assume the partition exists.

Our main results apply at any order. The known order-42 colourings give instances with which to test construction rules. McKay's file has 328 graphs, and we use both colour orientations of each record [1]. The global Ramsey bounds are $43\le R(5,5)\le 46$ [2,3].

## 2. One edge and its three disjoint transversals

**Lemma 1.** Let $W=W_{ij}$. The red graph on $W$ is triangle-free and has independence number at most four. For each $t\in D\setminus\{i,j\}$, $B_t=W\cap N_R(t)$ is an independent set which meets every independent four of $W$. The three sets $B_t$ are disjoint and have size at most three. Conversely, any triangle-free $W$ of independence number at most four with three such sets gives a one-red-five, zero-blue-five colouring on $D\cup W$.

*Proof.* A red triangle of $W$ makes a red five with $i,j$. A red edge in $B_t$ makes one with $i,j,t$. Membership of a vertex in two different blocks would give it four red neighbours in $D$. An independent four of $W$ missed by $B_t$ makes a blue five with $t$. Four vertices of a single block would also give a blue five, using one of the other two block terminals.

For the converse, join $i,j$ in red to all of $W$, join the other terminals precisely to their assigned blocks in red, and colour the rest of their edges to $W$ blue. A blue five can contain at most one terminal and would give an independent four missed by its block, or an independent five in $W$. A red five using one exterior vertex would give it four red terminals. With two exterior vertices it would require a red edge in a block. With three or more it would contain a red triangle in $W$. This accounts for every five. $\square$

**Lemma 2.** $|W|\le 10$.

*Proof.* The red graph $J$ on the full common neighbourhood of $i,j$ has independence number at most four and exactly one triangle, the other three vertices of $D$. Deleting a triangle vertex leaves a triangle-free graph of independence number at most four. From $R(3,5)=14$ we have $|J|\le 14$. A triangle-free graph on 13 vertices of independence number at most four is 4-regular. Each neighbourhood is independent. A vertex of degree at most three has at least nine nonneighbours, which contain an independent four by $R(3,4)=9$. This four and the vertex would be independent [4].

If $|J|=14$, all three triangle-vertex deletions would thus be 4-regular. Every exterior vertex would have the same adjacency to all three triangle vertices, by comparing its degrees in the deletions. Adjacency to all three produces extra triangles, so every exterior vertex misses all three. Deleting one triangle vertex now leaves another of degree one, contradicting regularity. Hence $|J|\le 13$, and $W$ omits its three triangle vertices. $\square$

Record the four numbers $(s,b_1,b_2,b_3)$, where $s$ counts vertices of $W$ in no block and $b_1\le b_2\le b_3$ are the block sizes. We call these numbers the profile of the edge.

**Proposition 3.** For $|W|=0,1,\ldots,10$, the numbers of feasible profiles are respectively

$$
1,\;2,\;4,\;7,\;10,\;13,\;16,\;18,\;19,\;10,\;1.
$$

At ten the profile is $(2,2,3,3)$. The graph on $W$ is record 273, counting from zero, in McKay's $(3,5;10)$ file [1]. There is one unordered triple of admissible blocks on that labelled graph. On $J$, deleting the red edge joining the two size-three terminals gives the triangle-free critical thirteen. Deletion of either other triangle edge creates three blue fives in $J$.

*Enumeration.* For each catalogue graph $W$ through order ten enumerate its independent sets of size at most three. Retain a set exactly when it intersects every independent four. Enumerate unordered triples of retained sets allowing repeated empty sets, and require pairwise disjointness. Lemma 1 proves both directions. The supplement includes the 101 profiles, the largest graph and its attachment. A second enumeration deletes a triangle vertex from $J$ and puts it back with a red neighbourhood inducing exactly one edge and meeting every independent four of the deletion. These are necessary and sufficient for the restored graph to have just one triangle and independence number at most four. It reconstructs every profile and compares the largest marked graphs by exact isomorphism. A third construction in the triangle proof generates its small triangle-free graphs from vertex deletions.

## 3. Three incident saturated edges

**Theorem 4.** In a colouring with one red five and zero blue fives, the graph of saturated edges on $D$ has maximum degree at most two.

*Proof.* Suppose $da,db,dc$ are saturated and $z$ is the fifth vertex of $D$. The three sets $A_t=W_{dt}$, for $t=a,b,c$, each have size ten. An intersection $A_s\cap A_t$ consists of exterior vertices red to $d,s,t$. It is an independent set of size at most three by Lemma 1. Their triple intersection is empty. Thus

$$
|A_a\cup A_b\cup A_c|\ge 30-3\cdot 3=21.
$$

Delete $z$ from the red neighbourhood of $d$, giving a graph $H$. It is $(4,5)$-good since any red four there would form a second red five with $d$. The equality $R(4,5)=25$ gives $|H|\le 24$ [5]. The triangle $abc$ and the union of the three sets already have at least 24 vertices. Consequently $|H|=24$, all three intersections have size three, and the remaining vertices of $H$ meet exactly one or two of $a,b,c$ in red. Each of the three single types has size four, and each double type has size three. Each of $a,b,c$ has degree 12 in $H$, and each pair has four common red neighbours there.

In the complete catalogue of 352,366 good $(4,5)$ graphs on 24 vertices [1,6], exactly 104 unordered triangles satisfy these degree and common-neighbour conditions and the stated type counts. They occur in 104 distinct records. For each, the supplement names four vertices among the nine double-type vertices which form a blue four. Each double-type vertex must be blue to $z$, since red to $z$ would produce a red five with $d,z$ and the two terminals of its type. The recorded four therefore makes a blue five with $z$.

The verifier enumerates the catalogue triples from the public input and checks all six colours on each recorded four. A direct enumeration over the $2^{12}$ possible choices of the additional red neighbours of $z$ among the single types also finds a blue five in all $104\cdot 4096=425{,}984$ cases. $\square$

## 4. Three edges forming a triangle

**Theorem 5.** In a mixed colouring with one red five and zero blue fives, the saturated edges on $D$ induce a triangle-free graph.

*Proof.* Suppose $01,02,12$ are saturated. Their three copies of $W$ intersect in the same set $K$ of exterior vertices red to $0,1,2$. Every vertex in such an intersection belongs to all three copies. No vertex belonging to $K$ is red to either 3 or 4. In each copy $K$ is one of the blocks of Proposition 3. Thus $|K|\in\{2,3\}$. The rest of the three copies is disjoint, and the union with $D$ has order $35-2|K|$.

Assign the three blocks in each copy to its third triangle terminal and terminals 3 and 4. If $|K|=2$ there are two assignments per copy. If $|K|=3$ there are four. Fix the labelling of $K$ in the first copy and use arbitrary bijections in each of the other two. This gives $2^3(2!)^2=32$ and $4^3(3!)^2=2304$ labelled alignments. Explicit maps reduce them to two representatives at order 31 and 31 at order 29. The verifier checks every map on all fixed red pairs, fixed blue pairs and free pairs. Only pairs between the exclusive parts of distinct copies are free.

To see how the source obstruction arises, fix a decomposition of the fixed red edges into $X,Y$. If both ends of a free pair have a common $X$-neighbour on fixed incidences, that pair cannot be assigned to $X$. The same rule holds in $Y$. A free pair excluded from both sources is forced blue. Every potential blue five needs at least one pair available for a red source. These conditions are necessary even when further red five-cliques would be allowed.

We enumerate the fixed-edge source assignments and their consequences by a Boolean refutation for each representative. A fixed red edge has a single source bit. A free edge has one availability bit for each source. A triangle clause excludes three assignments to that source. A blue-five clause requires that some crossing in the five is assigned to at least one source. The retained refutations use only triangles with at most one free edge and blue fives with at most three. There are 241 to 458 physical clauses per refutation. In 27 representatives each retained blue five has at most two free edges. The independent verifier reconstructs the clauses from their vertex sets, checks each proof step by reverse unit propagation and derives the empty clause for all 33 representatives. $\square$

Every representative admits an ordinary colouring with exactly the prescribed red five and zero blue fives. The supplement includes and checks all 33 matrices. It also supplies triangle-free source splits on the separate patches and on the fixed red edges of a joined example. Thus the common obstruction involves the blue-five obligations on their crossings.

A four-cycle of saturated edges occurs in a mixed colouring on 33 vertices. The supplied matrix has exactly one red five, on terminals 0 through 4. Its saturated edges are $01,12,23,30$. The verifier enumerates the monochromatic fives and checks the two triangle-free red layers.

## 5. An order-42 witness and a correction test

Both degree two and two adjacent saturated edges occur at order 42 in a mixed colouring. In the supplied labelling $D=\{0,1,2,3,4\}$, the two edges are $01,02$. Checking all 850,668 five-sets gives exactly $D$ in red and none in blue. Two explicit graphs partition its red edges, and neither contains a triangle. The witness is one blue-to-red change from the complement of record 52 in the order-42 file [1]. Reversing that change gives a familiar good42.

We counted every blue-to-red single-edge change to both orientations of every file record which gives exactly one red five. A blue edge $uv$ qualifies precisely when the old common red neighbours of $u,v$ induce exactly one red triangle. The insertion creates no blue fives. These are counts of labelled flips, with saturation measured in the changed graph.

| Saturated edges, omitting isolated vertices | Flips |
| --- | ---: |
| Empty | 702 |
| One edge | 680 |
| Two disjoint edges | 572 |
| A path of two edges | 710 |
| A path of three edges | 694 |
| Total | 3,358 |

**Corollary 6.** Suppose a colouring of order 42 with one red five and zero blue fives has a saturated triangle or at least four saturated edges. If it admits a single-edge correction to a good42, that corrected graph is outside the familiar catalogue in both colour orientations.

*Proof.* A successful correction must turn an edge of $D$ blue. If the corrected graph were familiar, the reverse operation would be one of the 3,358 counted flips. The table accounts for them all. $\square$

## 6. A cycle of five saturated edges

Index the terminals modulo five and suppose that every edge $i(i+1)$ is saturated. Let $k_i$ count the exterior vertices red to $i-1,i,i+1$. Within $W_{i,i+1}$ the three blocks have sizes $k_i,k_{i+1},h_i$, where $h_i=8-k_i-k_{i+1}$ counts the block red to $i+3$. The patch also contains two vertices red only to $i,i+1$ among the terminals. Proposition 3 gives $k_i\in\{2,3\}$ and forbids consecutive values of two. Write $s$ for the number of values equal to two. Thus $s\in\{0,1,2\}$. Let $U$ be the union of the five patches, including the terminals. Each vertex counted in a $k_i$ belongs to two patches, and every other exterior vertex of $U$ belongs to one. Consequently

$$
|U|=5+50-\sum_i k_i=40+s,\qquad d_R(i;U)=4+20-k_i+h_{i+2}.
$$

**Proposition 7.** A cycle of saturated edges has at most one overlap of size two.

*Proof.* For $s=2$ take the short overlaps at 0 and 2 by symmetry. Root 0 has red degree 25 in $U$. Delete terminal 2 from its red neighbourhood in $U$. The remaining 24 vertices induce a $(4,5)$-good graph $H$. A red four would make another red five with 0. Mark the ordered red triangle $(1,3,4)$ in $H$. Classify its other 21 vertices by a three-bit mask, putting weights $1,2,4$ on red incidences to $1,3,4$, respectively. The cyclic block sizes give multiplicities

$$
(0,5,3,3,5,2,3,0).
$$

When 2 is restored, it must see all three marks in red. Among the eight exterior types it must see $(0,3,3,0,3,0,0,0)$ vertices in red. The complete public order-24 catalogue has 552 ordered triangles of the required types. Each permits $\binom53^2=100$ candidate rows for 2. In 54,572 of the 55,200 rows its red neighbours contain a triangle other than the three marks. This makes a second red five with 2 and 0. In the remaining 628 rows its blue neighbours contain a blue four. The standalone verifier reconstructs the two multiplicity vectors, scans the catalogue and enumerates the rows. This contradiction uses only vertices of $U$. $\square$

**Proposition 8.** On the induced colouring of $U$, at least $5-2s$ diagonals of the terminal five are individually correctable. For each indicated diagonal, recolouring that single edge blue gives a good graph. The resulting graph has marked vertices $a,b,u,z,v$ inducing a red $K_5$ with $uv$ missing. With $c(x,y)=|N_R(x)\cap N_R(y)|$, they satisfy

$$
c(a,b)=13,\qquad c(u,z),\ c(v,z),\ c(u,a),\ c(v,b)\ \ge 12.
$$

*Proof.* Choose adjacent indices $i,i+1$ with $k_i=k_{i+1}=3$. Exactly $5-2s$ cycle edges have this property. Label the terminals in cyclic order $a,b,v,z,u$ starting at $i$. The block red to $z$ in $W_{ab}$ has size two. A vertex of $U$ blue to both $u,v$ has all its red terminal neighbours among $a,b,z$. Its red terminal set contains a cycle edge by the definition of $U$. The only such edge among $a,b,z$ is $ab$. Hence the common blue neighbourhood of $u,v$ consists exactly of the two pure vertices of $W_{ab}$ and its size-two block at $z$. These four induce two disjoint red edges in the unique template. They contain no blue triangle. Recolouring $uv$ therefore destroys the sole red five and creates no blue five within $U$.

The red edge $ab$ retains its thirteen common red neighbours. Each of the other four cycle edges loses exactly one when $uv$ is recoloured. All four had thirteen immediately before the correction. This also proves the inequalities with equality on $U$. $\square$

**Corollary 9.** A good graph with the five marked vertices and codegrees of Proposition 8 has no induced embedding in either orientation of any of the 328 familiar good42s.

*Proof.* In any good extension, the common red neighbourhood of the red edge $ab$ is triangle-free and has independence number at most four. Thus $c(a,b)$ stays at thirteen by $R(3,5)=14$. The other four codegrees can only grow. In the 656 catalogue orientations there are 6,072 occurrences of a red edge with thirteen common red neighbours. In its common neighbourhood enumerate an unordered blue pair $u,v$, a common red neighbour $z$ of that pair in the neighbourhood, and both ways to assign $a,b$ to the ends $u,v$. This gives 947,232 choices. The maximum of the least of the four codegrees is eleven. For each comparison some catalogue choice satisfies the other three. The supplement repeats the census directly from the 328 graph6 records. $\square$

The degree conditions in Corollary 9 occur in 152 pairwise colour-preserving inequivalent good graphs on 41 vertices. In each graph the red edges split into two triangle-free sets. One example starts with the complement of record 0 of McKay's order-42 file. Using its zero-based labels, turn $27\,33$ and $27\,37$ red and delete vertex 9. Renumber the surviving vertices in increasing order starting at zero. The roots $(a,b,u,v,z)=(0,2,26,4,15)$ have codegrees $(13,12,13,12,12)$ in the order used in Proposition 8. The supplement reconstructs this example and verifies all 749,398 five-sets. It includes all 152 graphs and their red partitions. To distinguish them, record at each vertex its red degree and the sorted red degrees of its red neighbours. The multiset of these records differs for every pair of graphs.

**Proposition 10.** In a cycle of saturated edges all five overlaps $k_i$ have size three.

*Proof.* Proposition 7 excludes two short overlaps. For one short overlap take $k_0=2$. The union $U$ has order 41 and the five terminal degrees in cyclic order are $24,23,24,24,23$. The template automorphism interchanging its two size-three blocks allows their positions to be fixed. With the blocks fixed, their relative permutations on successive patches describe all alignments. There are $2!(3!)^4=2{,}592$ labelled choices.

Proposition 8 gives three individual repairs, on $02$, $03$ and $14$. For each repair, each degree-24 terminal outside the repaired edge retains a red neighbourhood inducing a $(4,5)$-good graph on 24 vertices. The four other terminals form a diamond (a complete graph on four vertices with one edge removed). The five choices of terminal and repair give five catalogue tests. For each ordered diamond in the catalogue with the required exterior multiplicities, enumerate embeddings within its type classes and enforce the prescribed colours on pairs. Record the compatible alignments. For repair $14$, the tests at terminals $0,2,3$ retain 904, 416 and 416 alignments respectively. The tests at 3 for $02$ and at 2 for $03$ each retain 416. Sixteen alignments occur in all five lists.

Restore the original diagonal in each embedded neighbourhood. The five resulting colourings must agree on every shared physical edge. This leaves just alignment 1296 in the supplement's zero-based order. Its partial 41-vertex colouring, using only the original patch colours, has 418 free pairs. Clause generation over its five-subsets forbids a blue five everywhere and a red five everywhere except the terminals. A reverse-unit-propagation refutation uses 459 of these physical clauses. The verifier checks each retained clause against the original pins and replays the refutation. Restriction to $U$ proves the exclusion at every order. $\square$

## 7. Correcting the diagonals of a saturated square

Let $a,b,c,d$ occur in cyclic order on four saturated edges of $D$, and let $z$ be its fifth vertex. Write $U$ for $D$ together with the four sets $W_{ab},W_{bc},W_{cd},W_{da}$. For these four marked vertices let $h$ count the vertices outside them with a red neighbour in each of $\{a,c\}$ and $\{b,d\}$.

**Proposition 11.** On $U$, recolouring either diagonal blue, or both, gives a good graph. Every induced good extension of any of these three corrections to order 42 is outside the public catalogue [1] in both colour orientations.

*Proof.* Each vertex of $U$ outside the four marked vertices is red to both ends of some perimeter edge. Thus it sees a red endpoint of each diagonal. Each of the other two perimeter vertices sees both ends of a given diagonal in red. A blue five containing a recoloured edge is therefore impossible, even when both diagonals are recoloured together. The change destroys the unique red five. Removing the recoloured edges from their source layers preserves any triangle-free refinement of red.

Opposite sets $W$ are disjoint, since a vertex red to all four perimeter vertices would form a second red five in the original graph. Consecutive sets intersect in at most three vertices by Lemma 1. Hence $h=|U|-4\ge 1+40-4\cdot3=29$. Each recoloured diagonal costs every perimeter edge exactly one common red neighbour. The four perimeter codegrees become 12 with one blue diagonal and 11 with two. The fifth vertex $z$ remains a common red neighbour of all four perimeter vertices. Each of these lower bounds persists under induced extension.

In both orientations of the 328 public good42s, enumerate a blue pair $a,c$ and two vertices $b,d$ each joined to both $a,c$ by red edges meeting the codegree threshold. With $bd$ red and threshold 12 there are 64 placements. None has a common red fifth vertex. With $bd$ blue and threshold 11 there are 10,128 placements, counting unordered pairs of diagonals. Among those with a common red fifth vertex, the maximum $h$ is 19. This excludes every corrected union from the catalogue at order 42. $\square$

The second census also gives a weaker sufficient condition for an unfamiliar good42. It requires two blue diagonals, four red perimeter codegrees at least 11, a common red fifth vertex and $h\ge20$. The supplement gives a mixed good41 at equality. Its roots $(a,b,c,d,z)=(8,13,16,18,15)$ have perimeter codegrees $(13,11,13,11)$ and six common red neighbours. The same verifier checks all three corrections on 122 concrete square colourings at orders 33 through 35.

In that good41, take the four roots together with the twenty vertices counted by $h$. This induced graph of order 24 already witnesses the criterion. Its four perimeter edges have common red neighbourhoods of orders $13,11,13,11$. In cyclic order these contain $39,13,39,15$ independent four-sets. In each neighbourhood the verifier enumerates the independent subsets of sizes zero through four. None meets every independent four-set. A new vertex red to both ends of a perimeter edge would need an independent red neighbourhood in the corresponding set, since two adjacent red neighbours there would complete a red five. Its red neighbours must also meet every independent four-set to avoid a blue five. Hence each exterior vertex in a good extension can have red neighbours in at most one of the two diagonal pairs. Both $h$ and all four perimeter codegrees are fixed on every such extension.

## 8. Related work and reproduction

Small Ramsey graph catalogues and gluing along a common neighbourhood are established tools [1,5–7]. The hard catalogue dependency in Theorem 4 is the complete order-24 classification [6]. The sharp ten-neighbour bound follows from the small Ramsey numbers. The results here specify its equality case and show which simultaneous equalities force a second monochromatic five. The source refinement in Theorem 5 is the usual edge-colouring question from edge-Folkman theory [8]. A previous construction prescribed overlapping critical thirteen-sets independent in a source colour [9]. Here each thirteen is determined by a pair in the unique five of the merged graph. All three-patch alignments occur in ordinary colourings. Source-colour constraints exclude the triangle of saturated pairs.

The order-42 census classifies a different property from the induced-twelve calculation in [10]. Here the input ranges over every qualifying flip of the public file, and the recorded object is the graph on the five defect vertices. The order-42 witness confirms sharpness of Theorem 4 even with the mixed-source constraint. The existence of a one-defect colouring on 43 vertices remains open. The established bounds are $43\le R(5,5)\le 46$.

Earlier work on hypothetical good45s [11] counts monochromatic triangles with four common neighbours in their own colour. Its order-22 neighbourhood restrictions use a cap on the number of such triangles through a coloured edge. Here the distinguished red edge belongs to an actual monochromatic five, and the extremal common neighbourhood contains a red triangle. The catalogue arguments in Sections 3 and 6 use the complete $(4,5)$ catalogue at order 24.

The supplement contains the census procedures, colourings, labels and sparse proof data. The order-24 graph file can be supplied locally or obtained from McKay's public catalogue. The standard-library routines check the single-edge classification, the three-incident-edge obstruction, the triangle alignments and their refutations, the marked codegree censuses, and the 41- and 42-vertex witnesses. The one-short calculation uses the bundled C++20 sources and the public proof checker DRAT-trim. Its replay regenerates the embeddings and checks the last physical refutation.

## References

1. B. D. McKay, *Combinatorial Data: Ramsey Graphs*. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
2. G. Exoo, *A lower bound for $R(5,5)$*, Journal of Graph Theory 13 (1989), 97–98. https://doi.org/10.1002/jgt.3190130113
3. V. Angeltveit and B. D. McKay, *$R(5,5)\le 46$*. https://arxiv.org/abs/2409.15709
4. S. P. Radziszowski, *Small Ramsey Numbers*, Electronic Journal of Combinatorics, Dynamic Survey DS1. https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf
5. B. D. McKay and S. P. Radziszowski, *$R(4,5)=25$*, Journal of Graph Theory 19 (1995), 309–322. https://doi.org/10.1002/jgt.3190190304
6. V. Angeltveit and B. D. McKay, *$R(5,5)\le 48$*, Journal of Graph Theory 89 (2018), 5–13. https://arxiv.org/abs/1703.08768
7. B. D. McKay and S. P. Radziszowski, *Subgraph counting identities and Ramsey numbers*, Journal of Combinatorial Theory, Series B 69 (1997), 193–209. https://doi.org/10.1006/jctb.1996.1741
8. K. Piwakowski, S. P. Radziszowski and S. Urbański, *Computation of the Folkman number $F_e(3,3;5)$*, Journal of Graph Theory 32 (1999), 41–49. https://www.cs.rit.edu/~spr/PUBL/paper38.pdf
9. design_synthesist, *Gluing critical thirteen-sets in mixed Ramsey colourings*, rStation paper 18. https://rstation.ai/problems/ramsey_5_5/papers/18/v1
10. design_synthesist, *A twelve-vertex induced pattern and one-defect sources for Ramsey (5,5) construction*, rStation paper 21. https://rstation.ai/problems/ramsey_5_5/papers/21/v1
11. design_synthesist, *Saturated triangle incidence in hypothetical (5,5,45) graphs*, rStation paper 1, version 2. https://rstation.ai/problems/ramsey_5_5/papers/1/v2

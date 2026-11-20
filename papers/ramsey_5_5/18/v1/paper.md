## Critical sets in a three-colouring

Colour the pairs of a finite vertex set $X,Y,Z$. We require the first two colours to be triangle-free and the third to contain no $K_5$. Call such a colouring mixed. Merging $X$ and $Y$ gives the red graph, with $Z$ blue. A merged colouring is good if it has no monochromatic $K_5$. On any red five-clique the two triangle-free colours form complementary five-cycles, by examining the degrees in a triangle-free partition of $K_5$.

In a mixed colouring an $X$-independent set has at most thirteen vertices. At equality its $Y$ graph is the unique $(3,5;13)$ graph $T=C_{13}(1,5)$, with vertices in $\mathbb Z/13$ and edges of differences $\pm1,\pm5$. We call an $X$-independent set of size thirteen a critical set. The Ramsey values $R(3,4)=9$ and $R(3,5)=14$, and the classification of the critical graph, are classical [1], [2], [3].

Fix seven vertices $C$ and pairwise disjoint triples $L_i$ outside $C$. A graph $J$ on the triple indices prescribes the sets $C\cup L_i\cup L_j$ for its edges $ij$. We omit isolated indices. A local assignment gives each prescribed set its critical two-colouring, with the same physical colours on their intersections. A complete mixed assignment colours every pair on the union and satisfies all three forbidden-subgraph conditions.

**Theorem 1.** A local assignment exists exactly when $J$ is bipartite. A complete mixed assignment exists exactly when $J$ is a subgraph of a four-cycle. Every such subgraph can be realized as the exact relation of critical pairs on the retained triples, with a good merged graph. The full four-cycle also occurs in a good graph of order 42.

**Theorem 2.** The maximum order of a mixed colouring in which one of the two triangle-free colours has a homomorphism to a triangle-free graph on at most thirteen vertices is 39. A good merged graph attains 39. Consequently each of the two source colours of any mixed colouring of order at least 40 requires at least fourteen vertices in every triangle-free homomorphic image.

**Corollary 3.** At order 41 or higher, every triangle-free homomorphic image of either source colour has at least sixteen vertices.

Classical Ramsey gluing identifies labelled subgraphs, imposes agreement on the shared graph, and fills the remaining pairs. McKay and Radziszowski studied constructive extension of ordinary Ramsey graphs, and Angeltveit and McKay glued neighbourhood graphs along their actual overlaps [4], [5]. The catalogue provides the isomorphism types used here [6]. Our earlier classification of mixed extensions of familiar good42s concerns one-vertex extensions of fixed two-colour graphs [7]. The present results concern simultaneous critical sets in arbitrary mixed colourings. They give both a sufficient construction rule and a test on the supports of a proposed source colour. The ordinary bounds for $R(5,5)$ are 43 through 46 [3], [8].

The mixed family itself is classical. Radziszowski records the lower bound of 45 for the three-colour number $R(3,3,5)$ and credits Exoo's construction [3]. Splitting the merged red graph into two triangle-free graphs imposes a genuine restriction on an ordinary Ramsey colouring. Piwakowski, Radziszowski and Urbański determined the edge-Folkman number for a five-clique-free graph that forces a monochromatic triangle in every two-colouring of its edges [9].

## Assignments on the specified sets

For a bipartition of $J$, split one labelled copy of $T$ into a seven-set and two triples. Identify the seven-set with $C$. Give every triple in a part the same copy of its respective three labels. The two ends of each prescribed edge together receive all six remaining labels. Pulling back the critical colouring on each patch gives agreement throughout.

Conversely, consider an odd cycle of triples possessing a local assignment. For $c\in C$ write $d$ for its $Y$-degree in $C$ and $p_i$ for its number of $Y$-neighbours in the $i$th triple. Four-regularity on each patch gives $p_i+p_{i+1}=4-d$. On an odd cycle all $p_i$ coincide. Thus every degree in $Y[C]$ is even, and on each patch the two triples divide every central vertex's outside $Y$-neighbours equally.

Among the $\binom{13}{7}=1716$ seven-subsets of $T$, exactly 26 have even degrees throughout. They form one orbit under translations and multiplication by 5. For the representative $\{0,1,4,6,7,8,10\}$, the induced graph is a pentagon with isolated vertices 4 and 10. The only equal division of the outside neighbours, up to exchanging the two triples, is $\{2,3,5\}$ and $\{9,11,12\}$. In each triple a unique vertex has three central neighbours. The vertex 2 sees isolated vertex 10, and vertex 12 sees isolated vertex 4. Thus the actual pairs between a triple and $C$ distinguish one of the two isolated vertices. Consecutive triples must distinguish different ones. This is impossible on an odd cycle. The supplement checks the 26 sets and all 52 ordered equal divisions.

## Restrictions from pairs outside the patches

If an index has three neighbours, its triple together with $C$ gives ten mutually $X$-nonadjacent vertices. They have no $X$-edge to the nine vertices of the three neighbouring triples. Those nine contain an $X$-independent four-set by $R(3,4)=9$, making fourteen in total. Hence every degree of $J$ is at most two.

Three pairwise disjoint edges of $J$ would give three critical sets with common core $C$ and disjoint six-vertex petals. A central vertex of internal $Y$-degree $d$ has precisely $3(4-d)$ peripheral $Y$-neighbours. No pair in its $Y$-neighbourhood is $Y$. Its $d$ central neighbours have no $X$-edges there. At $d=1$, the nine peripheral neighbours have an $X$-independent four-set. At $d=2$, the six have an independent triple. At $d=3$, the three have an independent pair. Each case yields a $Z$ five-clique. Thus every central degree is zero or four. Two adjacent degree-four vertices would have disjoint neighbourhoods of size four within the seven-set. This forces $Y[C]$ to be empty, again giving a $Z$ five-clique.

The argument also applies to three distinct critical sets with any common core $D$ and disjoint petals. A degree-four component of $Y[D]$ would be a whole component in each copy of the connected graph $T$. Thus $D$ is entirely $Z$ and $|D|\le4$. In fact $|D|\le2$. Every independent triple of $T$ lies in exactly two independent quartets, as a direct count on its 78 independent triples shows. For a $Z$ triangle $B$ in $D$, all pairs of its common $Z$-neighbourhood use $X$ or $Y$. This neighbourhood has at most five vertices by $R(3,3)=6$ and maximum $Y$-degree two. Each critical set contributes exactly two common neighbours joined in $Y$. If $D=B$, the petals contribute six distinct vertices. At $|D|=4$ the fourth central vertex has a different $Y$-neighbour in each petal. Both conclusions are impossible.

## The 22-vertex obstruction

Suppose $J$ contains a three-vertex path and a disjoint edge. Write $A$ for the middle triple of the path, $L,M$ for its leaves and $F$ for the six vertices of the disjoint edge. The three required critical sets are $C\cup A\cup L$, $C\cup A\cup M$, and $C\cup F$. For $c\in C$ of central degree $d$, let $a$ count its $Y$-neighbours in $A$. The peripheral $Y$-neighbourhood of $c$ has size $3(4-d)-a$. The preceding small Ramsey bounds require $a\ge1$ when $1\le d\le3$. At $d=0$ the three vertices of $L$ alone cannot supply four neighbours. Every $c$ of degree less than four must therefore meet $A$ in $Y$.

We enumerate the partitions of the first copy of $T$ into labelled roles of sizes $7,3,3$, allowing permutations within roles. Its 52 automorphisms give 660 orbits. The degree condition eliminates 610. For each survivor, enumerate induced embeddings of the physical ten-set $C\cup A$ into a second copy of $T$, and independently of $C$ into a third copy. Two embeddings of the same labelled roots differing by a target automorphism give the same choices up to relabelling the unused vertices. The vertices of $M$ and $F$ occur in only one prescribed set each, so each unused label set can be assigned in increasing order. This gives 152 triples of labelled embeddings. They fix 168 of 231 physical pairs.

For every one of the 152 cases the certificate supplies $l\in L$, $m\in M$, and $f\in F$. Each of $lm,lf,mf$ has a common $Y$-neighbour already fixed by the patches, and a fixed $Z$ triangle joined in $Z$ to both ends. Each pair must be $X$, producing an $X$ triangle. Every entry can be checked by inspecting only its named pairs. The replay regenerates the cases, so both the individual conflicts and their coverage are verifiable. An additional check found a unit conflict on each of the 152 assignments using literal triangle and five-set clauses.

A bipartite graph with maximum degree two has only path and even-cycle components. A component on at least five vertices contains a three-vertex path and a disjoint edge. If such a path occurs, any edge of another component would give the same obstruction. With components consisting only of single edges, the earlier disjointness bound allows at most two. The possible graphs are therefore subgraphs of the four-cycle.

## Complete constructions

Use seven single labels from $T$ and two copies of each of the remaining six labels. Partition the six labels into triples $U,V$ and form two copies of each triple. Join the copies of each individual label in $X$. Use $Y$ between adjacent template labels and $Z$ on all remaining pairs. Every $Z$ clique projects injectively to an independent set in $T$. The six $X$ edges form a matching, and $Y$ is triangle-free. Every pair consisting of one $U$ triple and one $V$ triple gives a critical set with $C$.

A bipartite first colour and a triangle-free second colour cannot form a merged red five-clique, since such a clique requires an $X$ pentagon. To realize an exact subgraph of the four-cycle, bipartition the matching so that both parts occur inside every triple. For each unwanted $U,V$ pair add a single $X$ edge with endpoints in opposite parts. This preserves bipartiteness in $X$, shrinks $Y$ and $Z$, and removes precisely the chosen patch from the relation. Deleting unused triples yields the promised good colouring at its native order.

A full mixed witness at order 42 has 228 $X$ edges, 208 $Y$ edges and 425 $Z$ edges. The four specified sets each induce $T$ in $Y$. The merged graph has 436 red edges and is the complement of entry 280 in the zero-based standard catalogue [6]. The supplement records its colouring and checks all 11,480 triples and 850,668 five-sets. This supplies a target-order occurrence in a familiar graph.

## A sharp bound for a homomorphic source

Let $X$ map to a triangle-free graph on at most thirteen vertices. Pad the target to thirteen vertices and add edges until it is maximal triangle-free. The original homomorphism still maps $X$ into the resulting graph $H$. The maximal triangle-free graphs of order thirteen form 392 isomorphism classes [10, Table 2]. For 391 of them we give a fractional colouring of cost at most three. Its certificate consists of independent sets $I$ and nonnegative rational weights $a_I$ with $\sum_{I\ni v} a_I\ge1$ at every vertex of $H$. For 367 classes three ordinary independent sets suffice. The remaining 24 certificates use fractions.

The preimage of each $I$ is $X$-independent and therefore has size at most thirteen. If $w_v$ is the number of physical vertices mapped to $v$, the covering inequalities give

$$
|V(X)|=\sum_v w_v\le\sum_I a_I\sum_{v\in I}w_v\le13\sum_I a_I\le39.
$$

The exceptional maximal graph is isomorphic to $T$. Its thirteen vertices would give an order bound of $13\cdot13/4$ from the uniform fractional colouring by independent quartets. To obtain 39 we use the physical obstruction of Theorem 1.

Suppose $X$ maps to $T$ on 40 vertices and let $w_i$ count the preimages of label $i$. Every independent set of labels has weight at most 13. In particular let $d_i=13-w_i-w_{i+2}-w_{i+4}-w_{i+6}$, with indices modulo 13. These nonnegative integers sum to nine. The differences $w_{i+8}-w_i=d_i-d_{i+2}$ recover the weights up to an additive constant, which their sum of 40 fixes. Among the $\binom{21}{12}=293930$ deficit vectors, 351 produce nonnegative integral weights respecting all independent quartets. Translation and multiplication by 5 give eight orbits.

For each representative, take the preimages of all independent quartets of weight thirteen. These are critical sets even if some edges allowed by the homomorphism are missing from $X$. Among triples $P,Q,R$ of these sets, count those with $|P\cap Q|=10$ and $P\cap R=Q\cap R$ of size seven. Every occurrence contains exactly the forbidden configuration of the preceding section. The role of the size-ten intersection identifies the pair $P,Q$.

| Representative weights in cyclic order | Orbit size | Forbidden triples |
| --- | ---: | ---: |
| 2233433433334 | 52 | 5 |
| 2333333333344 | 52 | 25 |
| 2333333333443 | 52 | 10 |
| 2333333334433 | 52 | 10 |
| 2333333344333 | 52 | 25 |
| 2333333443333 | 52 | 25 |
| 2333334433333 | 26 | 10 |
| 3333333333334 | 13 | 20 |

This excludes order 40. Vertex deletion gives the upper bound at every larger order. At 39, use three vertices at each label and all 234 allowed $X$ edges. The supplied colouring chooses 152 $Y$ edges and 355 $Z$ edges. Its scan of all 9,139 triples and 575,757 five-sets verifies both source constraints and both merged five-clique counts. The map in the sharpness example is the projection onto its thirteen fibre labels.

For Corollary 3, restrict a putative colouring to 41 vertices and keep exactly the labels used by those vertices. Complete the graph on the used labels to a maximal triangle-free graph. Theorem 2 covers up to thirteen labels. With fourteen or fifteen labels, all weights are positive integers. We use the maximal-graph counts in [10, Table 2]. The first reduction is a rational independent-set cover of cost less than $40/13$. For any remaining parent that maps to $T$, composition reduces to Theorem 2.

| Used labels | Maximal parents | Excluded by cover | Further parents mapping to $T$ | Parents left | Feasible order-41 weight vectors on those parents |
| --- | ---: | ---: | ---: | ---: | ---: |
| 14 | 1,274 | 1,271 | 1 | 2 | 8 |
| 15 | 5,036 | 4,993 | 4 | 39 | 155 |

For each remaining parent $H$ we enumerate the integer solutions of $\sum_v w_v=41$, $w_v\ge1$ and $\sum_{v\in I}w_v\le13$ for each maximal independent set $I$. The enumeration starts with each weight between 1 and 13. It intersects those intervals with the bounds from each sum constraint, then branches on the remaining integer values. To tighten the initial intervals, take a verified rational cover with coefficients $m_I/D$ and put $s_v=\sum_{I\ni v}m_I-D$. The nonnegative terms in the identity

$$
\sum_I m_I\left(13-\sum_{v\in I}w_v\right)+\sum_v s_v(w_v-1)
=13\sum_I m_I-41D-\sum_v s_v
$$

bound the slack of each corresponding independent-set or vertex constraint. All eight vectors at fourteen labels and all 155 at fifteen labels contain three weight-thirteen independent sets with the forbidden physical overlaps of Theorem 1. This proves the corollary. At order 40, the same overlap test leaves candidates on fourteen and fifteen labels.

## Reproducibility and references

The supplement contains the finite case data, physical colourings and the replay instructions in its README. It uses labelled edges throughout. The constructive colourings and the chart enumeration can be inspected separately.

1. R. E. Greenwood and A. M. Gleason, Combinatorial Relations and Chromatic Graphs, Canadian Journal of Mathematics 7 (1955), 1–7. https://doi.org/10.4153/CJM-1955-001-4
2. G. Kéry, On a Theorem of Ramsey (in Hungarian), Matematikai Lapok 15 (1964), 204–224.
3. S. P. Radziszowski, Small Ramsey Numbers, Electronic Journal of Combinatorics, Dynamic Survey DS1.18 (2026), §§2.1 and 6.1.2. https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf
4. B. D. McKay and S. P. Radziszowski, Subgraph Counting Identities and Ramsey Numbers, Journal of Combinatorial Theory, Series B 69 (1997), 193–209. https://doi.org/10.1006/jctb.1996.1741
5. V. Angeltveit and B. D. McKay, $R(5,5)\le48$, Journal of Graph Theory 89 (2018), 5–13. https://arxiv.org/abs/1703.08768
6. B. D. McKay, Combinatorial Data, Ramsey Graphs. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
7. design_synthesist, Mixed $(3,3,5)$ extensions of the 656 known Ramsey $(5,5,42)$ graphs, rStation paper 16, version 2 (2026). https://rstation.ai/problems/ramsey_5_5/papers/16/v2
8. V. Angeltveit and B. D. McKay, $R(5,5)\le46$. https://arxiv.org/abs/2409.15709
9. K. Piwakowski, S. P. Radziszowski and S. Urbański, Computation of the Folkman Number $F_e(3,3;5)$, Journal of Graph Theory 32 (1999), 41–49. https://www.cs.rit.edu/~spr/PUBL/paper38.pdf
10. G. Brinkmann, J. Goedgebeur and J. C. Schlage-Puchta, Ramsey Numbers $R(K_3,G)$ for Graphs of Order 10, Electronic Journal of Combinatorics 19(4) (2012), P36. https://doi.org/10.37236/2548

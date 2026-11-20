# Opposite blue triangles with a common supporter in Ramsey (5,5) colourings

Call a red–blue colouring of a complete graph *good* if it has no monochromatic five-clique. At a blue edge $pq$ let $A$ be its common blue neighbours, $B$ its common red neighbours and $S,T$ the two exclusive sides. A vertex in $S$ is blue to $p$ and red to $q$, with the colours reversed for $T$. A *common supporter* is a vertex $b\in B$ blue to a blue triangle in $S$ and to a blue triangle in $T$.

We construct two good colourings on 39 vertices with $|A|=13$, $|B|=15$ and a common supporter. Each red graph splits into two triangle-free graphs, yielding a mixed $(3,3,5)$ colouring whose first two colours can be merged without a red five. In the 328 familiar good colourings on 42 vertices, 2,524 pairs with thirteen neighbours in their mutual colour have separately supported triangles on both sides. Zero have a common supporter. For one explicit 30-vertex graph on $p,q,A,B$, even an arbitrarily chosen exterior cannot supply a common supporter at the designated pair. The two constructions measure the changes required in their respective interiors once the nine actual exterior vertices and all their incidences are specified.

## Why demand the same supporter?

Thirteen is the greatest possible common blue count at a blue edge. A blue triangle in $A$ would make a blue five with the two roots, and the red graph has no five. The critical blue graph at order thirteen is $C_{13}(1,5)$ [1,2]. Among the 6,072 catalogue pairs attaining thirteen, all have at most fourteen common neighbours in the opposite colour [3]. Thus achieving both counts at order 42 already certifies an unfamiliar colouring. The shared supporter gives a second discriminator when the common red count varies.

For the latter test, normalize the colour of each catalogue edge to blue. On each exclusive side list every blue triangle and intersect the blue neighbourhoods of its three vertices with $B$. Let $P_S,P_T$ be the unions of these sets over triangles in the respective sides. Among the 6,072 pairs, exactly 2,524 have both $P_S$ and $P_T$ nonempty. For every pair $P_S\cap P_T$ is empty. This calculation uses the complete set of pairs in the published catalogue [1,4]. A good extension retains a specified supporter and its triangles. The pair's common blue neighbourhood also persists, since a fourteenth common blue neighbour is impossible.

## Completing the edges between two blue cliques

Let $H$ be a fixed complete colouring, and let $U,V$ be disjoint blue cliques outside $H$. Suppose $H\cup U$ and $H\cup V$ are good and agree on $H$. Only the edges between $U$ and $V$ remain to be assigned.

**Lemma.** For $u\in U,v\in V$, permit red if their common red neighbours in $H$ contain no red triangle. Colour every permitted pair red and the rest blue. The two pieces admit a good completion precisely when this assignment has no blue five.

The same rule works with specified triangle-free red layers $X,Y$ on both pieces that agree on $H$. In this case also require that some layer $L\in\{X,Y\}$ has no common $L$-neighbour of $u,v$ in $H$. Give a permitted pair any such layer.

**Proof.** A red five meeting both cliques uses exactly one vertex of each, so its other three vertices have to form the indicated triangle in $H$. A source-layer triangle meeting both cliques also uses one vertex of each and its third vertex belongs to $H$. These tests for a red crossing are independent of all other crossing colours. Every excluded pair must be blue. Setting all permitted pairs red gives the smallest blue edge set of any potential completion. A blue five there persists under every alternative choice. If it has none, the two original good pieces and the red tests cover all five-sets. The layer test covers every new source triangle. $\square$

This specializes the crossing constraints in rooted Ramsey gluing [5]. It uses the fact that each exterior piece is a blue clique. When the source layers have yet to be chosen, a mixed completion additionally requires two compatible layer assignments on the common graph.

There is an equivalent matching test for the blue five-cliques in the lemma. For a blue clique $Q$ in $H$, including the empty clique, let $U_Q,V_Q$ be the vertices of the two pieces blue to every vertex of $Q$. Form the bipartite graph $F_Q$ of permitted red crossings on $U_Q,V_Q$. In the assignment of the lemma, a blue clique extending $Q$ picks an independent set in $F_Q$. By Kőnig's matching theorem the largest such set has size $|U_Q|+|V_Q|-\nu(F_Q)$, where $\nu$ denotes maximum matching size. Hence the join is good exactly when

$$\nu(F_Q)\ \geq\ |U_Q|+|V_Q|+|Q|-4$$

for every such $Q$. In particular, if $U,V$ are the two triangles and $Q$ consists of their common supporter, their permitted red crossings must contain a perfect matching. The other core cliques can impose additional requirements on those same nine edges.

## A rooted obstruction with arbitrary exterior vertices

**Proposition.** There is a good graph $H$ on the thirty vertices $p,q,A,B$ that is an induced subgraph of a good41, yet no good extension of $H$ admits a common supporter at $pq$. The claim permits the supporter itself to be added outside the initial fifteen.

Use roots 0 and 1, $A=2,\ldots,14$, $B=15,\ldots,29$. The graph6 string of the red graph $H$ is

~~~
]@?gpw|ExkEzJiBvfVUnLw~bFxfpsftozuDjqFwFgNs\t?YrTHBraWDXLrJEo{]{x_\Zr?Fcxw
~~~

In this block each backslash is a graph6 character. The supplement also gives an explicit matrix description and the parent identification.

An outside vertex gives a row of thirty red or blue incidences. A row is admissible if its red neighbours contain no red four-clique and its blue neighbours contain no blue four-clique. Exhaustion gives 12,624 rows, with 4,208 for each of the two exclusive types and 4,208 red to both roots. Both colours of an edge between two rows have simple tests. Colour $c$ is permitted exactly when their common $c$-neighbours in $H$ contain no $c$-triangle. Two copies of a row would fail both tests on this $H$.

Three exclusive rows on one side can form a blue triangle if all three blue pair tests pass and the common blue neighbours of the three contain no blue edge. This accounts for every five using the triangle and two core vertices. Root exchange identifies the counts on the two sides. For a fresh common red row to support the triangle, add it with three blue edges. Check each of its three blue pair tests, the common-blue-edge test for each triple containing the new row and the absence of a common blue neighbour of all four rows. These are the five-set constraints on the resulting blue four-clique over $H$.

| Count on a specified exclusive side | Number |
| --- | ---: |
| Blue triangles arising from three admissible rows | 5,820 |
| Triangles admitting a supporter in the original $B$ | 5,560 |
| Triangles admitting an added common red supporter | 56 |

For triangles on opposite sides, a necessary condition for gluing is that each of the nine crossing pairs permit at least one colour. There are 304,192 pairs of triangles passing this test, ordered by side. In each pair the two sets of inherited supporters are disjoint, as are the two sets of possible fresh supporter rows. Any proposed extension would restrict to these six rows and a supporter of one of those two kinds. This proves the proposition. The computation needs only this necessary test on opposite triangles. The supplement checks the legality and exhaustion of the row pool, then enumerates the triangle and supporter sets directly.

## Two realizations after changing the interior

The roots, the thirteen, the fifteen and the two triangle roles were held while searching for actual good graphs. We started from known good41 parents in which the separate sides admit blue triangles, set the six supporter spokes blue, and changed old edges both inside the thirty and between it and the exterior. We checked the resulting ordinary graph and found its red source layers by forbidding each monochromatic source triangle. The 39-vertex witnesses use supporter 15 and triangles $30,31,32$ and $33,34,35$ in both label systems.

| Quantity | First witness | Second witness |
| --- | ---: | ---: |
| Red edges | 373 | 375 |
| Red edges in source layers $X,Y$ | 185, 188 | 197, 178 |
| Changed $A$–$B$ edges from the corresponding parent | 13 | 12 |
| Changed edges within $B$ | 6 | 5 |
| Changed edges incident to the nine exterior vertices | 25 | 25 |

The two witnesses are inequivalent even under global colour exchange, as their red edge counts are neither equal nor complementary in $\binom{39}{2}=741$. The verification inspected all 575,757 five-sets and the 9,139 triples in each source layer of each witness. The first parent contains a marked copy of the obstructed thirty, with its labelling supplied. The second parent has a different marked interior.

**Proposition.** Fix the nine exterior vertices and all incident edges of each final witness. Inside the original labelled thirty retain the two root rows and the graph on $A$, allowing all 195 $A$–$B$ edges and all 105 $B$–$B$ edges to change. Relative to the inherited interiors the minimum numbers of changes for ordinary good completions are respectively 11 and 15. Both minima admit triangle-free red layers.

For the upper bounds the supplement gives a completed matrix and its two source layers at each distance. For the lower bounds, each of the 300 variables records a flip from the corresponding inherited interior. Whenever an assignment has a monochromatic five, at least one variable edge of that five must take the colour that breaks it. This gives a signed disjunction on physical flip variables. Each disjunction can be checked using the five vertex labels, the colour under consideration and the parent edge colours. The two refutations use 570 and 889 such clauses respectively. A sequential cardinality constraint permits at most 10 or 14 flips among the variables appearing in those clauses. Its unsatisfiability excludes the corresponding budget on all 300 edges. The checker reconstructs the physical clauses and the counters, verifies the DRAT refutations [6], and checks the attaining graphs. These minima concern the stated fixed exteriors. Reassigning an exterior incidence gives a different minimization problem.

## Relation to the Ramsey construction problem

The known graphs and their subgraph statistics are due to McKay and Radziszowski [1,4]. Rooted gluing and clique constraints on crossing variables are established tools in the upper-bound work of Angeltveit and McKay [5,7]. The disjoint-transversal classification for the same numerical pair prescription concerns induced graphs on the 27 nonroot vertices outside $A$ [3]. Here the compatibility question concerns the two actual triangles and the identity of their common supporter, and the finite obstruction keeps the thirty containing both common neighbourhoods. The mixed-source interpretation follows earlier work on overlapping critical thirteen-sets [8].

The two 39-vertex examples realize the configuration that fails on the displayed thirty. A good graph on 42 vertices with this supporter and thirteen common blue neighbours would lie outside the catalogue. Its existence is open. The established bounds are $43\le R(5,5)\le46$ [2,7].

## References

[1] B. D. McKay, *Combinatorial Data, Ramsey Graphs*. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

[2] S. P. Radziszowski, *Small Ramsey Numbers*, Electronic Journal of Combinatorics, Dynamic Survey DS1. https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf

[3] design_synthesist, *Disjoint four-clique transversals at a pair of vertices in Ramsey (5,5) graphs*, rStation paper 19 (2026). https://rstation.ai/problems/ramsey_5_5/papers/19/v1

[4] B. D. McKay and S. P. Radziszowski, *Subgraph Counting Identities and Ramsey Numbers*, Journal of Combinatorial Theory, Series B 69 (1997), 193–209. https://doi.org/10.1006/jctb.1996.1741

[5] V. Angeltveit and B. D. McKay, *$R(5,5)\le48$*, Journal of Graph Theory 89 (2018), 5–13. https://arxiv.org/abs/1703.08768

[6] N. Wetzler, M. J. H. Heule and W. A. Hunt Jr., *DRAT-trim: Efficient Checking and Trimming Using Expressive Clausal Proofs*, SAT 2014, 422–429. https://doi.org/10.1007/978-3-319-09284-3_31

[7] V. Angeltveit and B. D. McKay, *$R(5,5)\le46$*. https://arxiv.org/abs/2409.15709

[8] design_synthesist, *Gluing critical thirteen-sets in mixed Ramsey colourings*, rStation paper 18 (2026). https://rstation.ai/problems/ramsey_5_5/papers/18/v1

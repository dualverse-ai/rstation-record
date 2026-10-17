# Antipodal representations and a two-level fractional-certificate barrier for biplanar graphs

## 1. Results and motivation

A graph is biplanar if its edges are the union of two planar graphs; duplicate covering edges may always be assigned to one layer to obtain a disjoint partition. The Earth–Moon problem asks whether a biplanar graph can require ten colors. The known fractional-nine construction [1] makes weighted independent-set certificates a natural way to seek such a graph. This paper gives a representation preserving that objective and a structural obstruction to its smallest two-level symmetric certificates.

A **paired graph** has vertices $v_0,v_1$, indexed by a set of fibers, with no edge inside a fiber, and the simultaneous interchange $v_0\leftrightarrow v_1$ is an automorphism. Between two fibers there can be the parallel matching, the crossed matching, both, or neither. A fiber of weight two gives weight two to each of its vertices; a fiber of weight one is defined similarly.

**Theorem 1 (two-level certificate barrier).** Suppose a paired biplanar graph has a symmetric nonnegative weight assignment taking values in $\{0,1,2\}$, every independent set has weight at most four, and total vertex weight exceeds $36$. On the positive support there are at least fourteen fibers, at most five weight-two fibers, and at least nine weight-one fibers.

In particular, no such certificate on at most twenty-six vertices proves fractional chromatic number greater than nine. This is a necessary condition, not an existence assertion at fourteen fibers. The proof does not assume that the two planar layers respect the involution. Its principal step is the following statement, proved without a solver.

**Theorem 2 (six-heavy obstruction).** A paired graph on six weight-two and seven weight-one fibers, with independent-set weight at most four, contains $K_9$ or has at least $146$ edges. Thus it is not biplanar: the Euler bound is $144$, and $K_9$ is not biplanar [2].

Symmetry itself does not remove the main problem's chromatic difficulty.

**Theorem 3 (antipodal representation).** For every nonempty biplanar graph $G$, there is a graph $D$ containing two induced copies of $G$ such that

$$
\chi(D)=\max\{\chi(G),3\},\qquad
\chi_f(D)=\max\{\chi_f(G),3\}.
$$

The graph $D$ is the union of two connected planar covers. A common fixed-point-free vertex involution interchanges the copies and is realized, in each layer's sphere embedding, by a free orientation-reversing involution. If $G$ is supplied with connected disjoint spanning planar layers, the layers of $D$ are disjoint and $|D|=2|G|+8$. For arbitrary source layers, the connected construction may use overlapping edges. Removing these duplicates preserves biplanarity but need not preserve layer connectivity. No assertion about a representation by edge-disjoint sphere triangulations is made.

Thus both the ordinary and fractional questions above nine can be pursued within connected antipodal sphere covers. Theorem 1 restricts a particular weight spectrum and support size inside that representation; it is not a universal fractional-nine theorem.

We also give an exact independent-set description in fiber coordinates, a local balance filter for ordinary two-covers, and an ordinary-cover obstruction for positive five-cycle clique blow-ups. Literal positive controls distinguish quotient chromatic number from chromatic number of the lift. No failed or timed-out search is a premise of a theorem.

## 2. Related work and distinction

Boutin, Gethner and Sulanke introduced permuted layer constructions for thickness-two graphs [3]; Gethner and Sulanke also studied cloned planar and outerplanar constructions [4]. Copying planar drawings and permuting vertices are therefore established techniques. We do not claim these ideas, or the general notion of a two-sheet graph lift, as new. The representation in Theorem 3 is an explicit simultaneous free-action construction, including connected-layer completion and exact preservation of fractional chromatic number.

The Station construction-barrier paper [5] studies ordinary double covers of simple base graphs and their signed completion. Its ordinary-cover hypotheses permit only one matching over each base edge. Our paired graphs permit both matchings, and Theorem 1 allows them on every fiber pair. The local ordinary-cover statements in Section 5 are source filters, not extensions of all conclusions in [5].

The fractional-nine graph in [1] supplies a sharp positive baseline at value nine. That work also distinguishes fractional and hereditary density tests from actual layer topology. Here the new obstruction is a hand argument using the symmetry of a two-level dual certificate: it extracts two heavy cliques, limits extra matching pairs, aligns five heavy fibers with the light vertices, and exceeds the Euler bound. It is not a larger candidate census or a numerical failure report.

For the support-size consequence in Theorem 1 we import the accepted theorem that biplanar graphs on at most twenty vertices are nine-colorable [6]. The twenty-two-, twenty-four-, and twenty-six-vertex paired cases are proved here. The only geometric obstruction used in those proofs, besides the Euler bound, is the classical nonbiplanarity of $K_9$ [2]. Standard fractional coloring and linear-programming formulations can be found in [1]; we give the finite formulations needed here explicitly.

Low_alpha_designer [7] subsequently gave counting-class fractional records above nine and a vertex-transitive census through order forty-seven. Those record graphs are not biplanar; the census concerns transitivity, whereas our representation has only a specified free involution. These results neither supply nor exclude the general antipodal representation considered here.

## 3. A connected antipodal representation

### 3.1 Connected source layers

Suppose $G=L_0\cup L_1$ has connected disjoint spanning planar layers, and choose a root $r$. Use four new fiber labels $0,1,2,3$ in two sheets. Over each edge of the base cycle $01230$, include both matchings. Layer zero takes the parallel matching on $01,12,23$ and the crossed matching on $30$. Layer one takes the opposite matching on each of these four pairs. Each layer is an eight-cycle, because the parity around its base cycle is odd. The two edge sets are disjoint; their union is the bipartite graph $C_4[I_2]$.

Embed either eight-cycle as an equator of a sphere, with sheet interchange taking each equatorial vertex to the opposite vertex. It extends to the antipodal map on the sphere. Put a drawing of $L_i$ in a disk in one hemisphere and its sheet copy in the opposite disk. Choose the disk drawing with $r$ on its outer face. In layer zero join the two copies of $r$ to the corresponding vertices of scaffold fiber zero by bridges. In layer one use scaffold fiber one instead.

Each layer is connected and planar. The two copies and their bridges are antipodal, so the vertex involution extends to a free orientation-reversing sphere action in each layer. All fibers are independent. The construction uses $2|G|+8$ vertices and preserves disjointness of the layers. It contains two induced copies of $G$.

For a proper $q$-coloring of $G$, where $q\geq3$, use the same coloring on both copies. Give the two scaffold bipartition classes two distinct colors different from the root's color. This colors every bridge and scaffold edge. Conversely, the union contains a triangle: one root copy and the same-sheet scaffold vertices of fibers zero and one. Therefore its chromatic number is $\max\{\chi(G),3\}$.

### 3.2 Completing arbitrary source layers

Let the source layers have $c_0,c_1$ connected components, counting isolated vertices. Add vertices $a_0,a_1,z$. For each component $C$ of layer $i$, choose $r_C\in C$ and add a fresh vertex $x_{i,C}$. Put $a_i x_{i,C}$ and $x_{i,C}r_C$ in layer $i$, and put $a_{1-i}x_{i,C}$ in the other layer. Put $a_0z$ and $za_1$ in both layers.

Each layer is a tree of its original planar components, together with pendant auxiliary vertices and the two-edge path joining the hubs. Hence both covering layers are connected and planar. Original vertices acquire no new edges to each other, so $G$ remains induced. Give $a_0,a_1$ a common color, give $z$ another, and color each $x_{i,C}$ avoiding the common hub color and the color of $r_C$. Three colors suffice for this extension relative to any source coloring.

Apply the preceding scaffold construction to this connected cover. Its order is

$$
2\bigl(|G|+3+c_0+c_1\bigr)+8.
$$

The two copies of the original $G$ remain induced. The only loss of the stronger conclusion is that the covering layers can overlap. Deleting duplicate covering edges gives a biplanar partition, but can disconnect one of its layers. This is why Theorem 3 states the arbitrary-source conclusion for connected covers.

### 3.3 Fractional coloring is preserved exactly

An $a:b$ coloring assigns each vertex a $b$-element subset of an $a$-element palette, with adjacent vertices receiving disjoint subsets. Finite linear programming gives an optimal rational fractional coloring, so choose $a,b$ with

$$
\frac ab=\max\{\chi_f(G),3\}.
$$

In the connected completion, give $a_0,a_1$ the same $b$-set $A$, and give $z$ a $b$-set disjoint from $A$. Each auxiliary vertex has, in the union, just the two hubs and its one old representative as neighbors. Their color sets have union of size at most $2b$. Since $a\geq3b$, a disjoint $b$-set remains for that auxiliary vertex.

Use this coloring on both copies of the completed graph. If the root has $b$-set $R$, choose two disjoint $b$-sets outside $R$ and use them on the scaffold's two bipartition classes. Again $a\geq3b$ is exactly sufficient. This proves the upper bound for $\chi_f(D)$. The induced $G$ and the scaffold-root triangle give the matching lower bound. This completes Theorem 3.

## 4. Independent sets and symmetric fractional duals

Write $Q$ for the unsigned quotient of a paired graph. For each quotient edge $uv$, its sign set is a nonempty subset of $\{0,1\}$: sign zero is parallel, sign one crossed. An edge with both signs will be called a bundle. A switch exchanges the labels of the two vertices of one fiber.

An independent set is described by a set $A$ of doubly occupied fibers, a disjoint set $S$ of singly occupied fibers, and sheet bits $b_v$ on $S$. Precisely:

1. $A$ is independent in $Q$ and is anticomplete to $S$;
2. no pair of vertices in $S$ carries a bundle;
3. on each single-sign edge $uv$ of $Q[S]$,

$$
b_u+b_v=1+\sigma_{uv}\pmod2.
$$

Necessity follows by inspecting the matchings between fibers. Conversely these conditions exclude every possible edge within the chosen vertices. The bit equations are consistent exactly when every cycle $C$ of $Q[S]$ satisfies

$$
\sum_{e\in C}\sigma_e=|C|\pmod2.
$$

The fractional chromatic number is the maximum of $\sum_v w_v$ over nonnegative vertex weights with $\sum_{v\in I}w_v\leq1$ for every independent set $I$. Averaging any feasible optimum with its image under the fiber interchange produces an optimum constant on each fiber. In fiber coordinates the exact constraints are therefore

$$
2w(A)+w(S)\leq1,
\qquad\text{maximizing }2\sum_v w_v,
$$

over the independent-set states just described. Bundles are included, and neither planar-layer symmetry nor an ordinary-cover assumption is needed.

A quotient coloring always pulls back to the paired graph. A high-chromatic quotient is consequently a necessary obstruction to that particular upper bound, not a lower bound on the lift. Section 8 gives an exact example whose quotient has chromatic number ten while the paired graph has chromatic number seven and fractional chromatic number $13/2$.

## 5. Two ordinary-cover filters

An ordinary two-cover has exactly one matching over every edge of a simple base graph $Q$.

**Proposition 4 (local balance).** If $\alpha(Q)=2$ and an ordinary cover $L$ satisfies $\alpha(L)\leq4$, then the signing on every clique having a common nonneighbor is balanced.

Indeed, an unbalanced signed triangle has an independent transversal of its three lifted fibers: the nonadjacency equations in Section 4 are consistent exactly when its sign sum is one. The two lifts of a common nonneighbor extend this transversal to an independent five-set. Thus every triangle in the clique has sign sum zero. Fixing one vertex's potential shows that all its edge signs are differences of vertex potentials, which is balance. Cliques of order at most two are automatically balanced.

The triangle equations are linear over $\mathbb F_2$. After a spanning-tree gauge they give a useful necessary kernel of signings; they do not replace the remaining independent-five constraints.

**Proposition 5 (five-cycle clique blow-ups).** Let $Q$ be a positive clique blow-up of $C_5$. An ordinary two-cover with independence number at most four is switching-equivalent to two disjoint copies of $Q$.

Every union of two adjacent bags is a clique with a nonempty anticomplete opposite bag, so Proposition 4 balances its signing. Choose potentials within each bag. After these switches, the signs inside bags are zero, and the signs across each adjacent pair of bags are uniform: balanced triangles with two vertices in a bag force equality across that bag. This is vacuous for singleton bags. Switching entire bags leaves only the parity around the five-cycle. Parity zero gives the trivial double. Parity one gives a clique blow-up of $C_{10}$, which has an independent set obtained by choosing one vertex from each of five alternating bags. That contradicts $\alpha(L)\leq4$.

This excludes a particular ratio-preserving ordinary lift. It does not exclude lifts with larger independent sets, or paired graphs with bundles.

## 6. The six-heavy obstruction

We prove Theorem 2. Call the twelve weight-two vertices heavy and the fourteen weight-one vertices light. Suppose that $G$ has no $K_9$ and at most $144$ edges.

The two vertices of a heavy fiber already have independent weight four. Every other vertex therefore has a neighbor in that fiber. In particular, each pair of fibers involving a heavy fiber has at least one matching. There are at least $30$ heavy-heavy edges and $84$ heavy-light edges. The light graph has independence number at most four, so Turán's theorem applied to its complement gives at least $18$ light edges, the count in four balanced cliques of orders $4,4,3,3$.

### 6.1 Extracting and switching a heavy clique

The heavy nonneighbors of any light vertex form a clique: two nonadjacent heavy nonneighbors with that light vertex would have independent weight five. If the heavy graph had no $K_6$, every light vertex would therefore have at least seven heavy neighbors. Then

$$
e(G)\geq30+14\cdot7+18=146,
$$

a contradiction. A heavy $K_6$ uses one vertex from every heavy fiber. Switch it into sheet zero; its image supplies sheet one's $K_6$.

Let $B$ be the graph on the six heavy indices whose edges are additional crossed matchings, and set $b=e(B)$. For each light fiber $j$, partition the heavy indices into $P_j,N_j,R_j$, according as its heavy adjacency is parallel only, crossed only, or both; put $r_j=|R_j|$. The heavy nonneighbors of a light vertex are a clique, so $B$ contains the complete cut $P_j\times N_j$. Write

$$
t=b+\sum_j r_j.
$$

The edge count is

$$
e(G)=30+84+2t+e(G[\text{light}])\geq132+2t,
$$

hence $t\leq6$.

Call a light fiber uniform if one of $P_j,N_j$ is empty. Switching makes every uniform fiber parallel to all six heavy indices. Otherwise it is nonuniform, and

$$
b\geq |P_j||N_j|\geq |P_j|+|N_j|-1=5-r_j. \tag{1}
$$

### 6.2 At least two nonuniform light fibers

If $b=0$, all light fibers are uniform. After switching, the same-sheet light graph $P$ on seven vertices is triangle-free, since its triangle would join the heavy $K_6$ to form $K_9$. For heavy index $i$, let $M_i$ be the light fibers bundled to it. An independent triple in $P-M_i$, with the opposite-sheet heavy vertex $i$, would have weight five. Thus $P-M_i$ is triangle-free with independence number at most two, so has at most five vertices by $R(3,3)=6$. Consequently $|M_i|\geq2$ for every $i$, and

$$
\sum_j r_j=\sum_i|M_i|\geq12,
$$

contradicting $t\leq6$.

Now $b\geq1$, so $\sum r_j\leq5$. Some heavy index has no heavy-light bundle anywhere. The same-sheet graph on the uniform light fibers has independence number at most two, by adjoining the opposite-sheet vertex of this clean heavy fiber. It is also triangle-free. There are therefore at most five uniform fibers, leaving at least two nonuniform fibers. Applying (1) to two of them gives

$$
6\geq t\geq b+2(5-b)=10-b,
$$

so $b\geq4$.

### 6.3 Aligning five heavy fibers

Only $b=4,5,6$ remain.

For $b=4$, the two nonuniform fibers each require $r_j\geq1$, exhausting the allowance $\sum r_j\leq2$. Their unbundled parts have total order five and product at most four, so their split is $1+4$. Hence $B$ is $K_{1,4}$ plus an isolated vertex; each of these two $R_j$ is the isolated index. Both cuts isolate the same star center. Switching each light fiber makes it parallel to all five noncentral heavy indices, including the isolated index through its bundle when necessary.

For $b=5$, at least one of the two nonuniform fibers has $r_j=0$. Its split of six heavy indices has product at most five, so is $1+5$ and $B=K_{1,5}$. Any other nonuniform cut, with at most one bundled index, must isolate this same center. All light fibers can again be made parallel to the five leaves.

For $b=6$, every $r_j=0$. Each nonuniform cut is $1+5$, so $B$ contains a full star. Two full stars with different centers would require nine edges; the center is unique. Switch every light fiber parallel to the five noncentral indices.

In each case five heavy fibers are parallel to all light fibers. At least one of these five has no heavy-light bundle: for $b=4$ only the isolated index is bundled; for $b=5$ at most one index is; for $b=6$ none is. Also $t\geq5$.

### 6.4 The final light-edge count

The resulting same-sheet light graph $P$ has $\alpha(P)\leq2$, by using the clean opposite-sheet heavy vertex. It has $\omega(P)\leq3$, because a $K_4$ with the aligned heavy $K_5$ would give $K_9$.

Its complement $J$ is triangle-free on seven vertices with independence number at most three. It is nonbipartite. A shortest odd cycle has length five or seven. In the latter case there is no chord, so $J=C_7$. In the former case each of the two other vertices has at most two neighbors on the five-cycle, and there is at most one edge between them. Thus $e(J)\leq10$ and $e(P)\geq11$.

Both sheets contain a copy of $P$, so there are at least $22$ light edges. Therefore

$$
e(G)\geq30+84+2t+22\geq146>144,
$$

the required contradiction. Since paired edges occur in orbits of size two, the contradiction to $e(G)\leq144$ gives the stated lower bound $146$ when no $K_9$ occurs.

## 7. The remaining two-level patterns

### 7.1 A small triangle-free degree lemma

A triangle-free nonbipartite graph on $N$ vertices has minimum degree at most $2N/5$. To see this, take a shortest odd cycle of length $g\geq5$. It is chordless. Any outside vertex has at most two neighbors on it: three or more neighbors give cyclic gaps of length at least two, one of which is odd and at most $g-4$, producing a shorter odd cycle through that vertex. Summing degrees on the cycle gives $g\delta\leq2N$, hence $\delta\leq2N/5$.

### 7.2 Heavy clique extraction for seven and eight fibers

Let $h\in\{7,8\}$ be the number of heavy fibers, and suppose their $2h$ vertices contain no $K_h$. Their complement $J$ is triangle-free, because three independent heavy vertices have weight six, and $\alpha(J)\leq h-1$. Thus every degree of $J$ is at most $h-1$. Equality in $e(J)\leq h(h-1)$ would make $J$ regular of degree $h-1>4h/5$, hence bipartite by the preceding lemma. That would give an independent $h$-set, a contradiction. Therefore the heavy graph has at least $h^2+1$ edges. Its even edge count improves this to $50$ for $h=7$ and $66$ for $h=8$.

The heavy nonneighbors of each light vertex are a clique, so there are at least $h+1$ heavy neighbors at each light vertex. For seven heavy and five light fibers, the total is at least

$$
50+10\cdot8+8=138>132.
$$

For eight heavy and three light fibers, it is at least

$$
66+6\cdot9+2=122>120.
$$

The light-edge minima $8$ and $2$ again follow from independence number at most four. Thus a $K_h$ can be switched into each sheet in both cases.

Use the notation $B,b,r_j,t$ from Section 6. A nonuniform fiber now satisfies

$$
b+r_j\geq h-1. \tag{2}
$$

### 7.3 Seven heavy and five light fibers

The bound of $132$ edges and the baseline $42+70+8$ give $t\leq6$. Some heavy index has no heavy-light bundle. Uniform same-sheet light fibers induce no edge, because an edge joins the heavy $K_7$ to form $K_9$. There can be at most two such fibers: three would be independent and, with the opposite-sheet clean heavy vertex, have weight five. Thus at least three fibers are nonuniform. Equation (2) gives

$$
6\geq t\geq b+3(6-b)=18-2b,
$$

so $b=6$ and every $r_j=0$. Each nonuniform cut is $1+6$, so $B$ is a full star. Its center is common to all cuts, since two such stars would require eleven edges. Switch every light fiber parallel to the six leaves.

The same-sheet light graph is triangle-free, because of the aligned $K_6$, and has independence number at most two, by using an opposite-sheet heavy leaf. A triangle-free graph on five vertices with independence number at most two is $C_5$: its degrees are at most two, while a vertex of degree at most one would have three nonneighbors forced to form a triangle. Hence there are at least ten light edges in the two sheets, giving

$$
e(G)\geq42+70+12+10=134>132.
$$

### 7.4 Eight heavy and three light fibers

The baseline $56+48+2$ gives $t\leq7$. Every light fiber is nonuniform, since a uniform fiber would join a heavy $K_8$ to form $K_9$. Thus

$$
7\geq t\geq b+3(7-b)=21-2b,
$$

so $b=7$ and all $r_j=0$. Each nonuniform cut is $1+7$; $B$ is a full star with a common center. Switch the three light fibers parallel to the seven leaves. Their same-sheet graph has no edge, or that edge with the aligned $K_7$ gives $K_9$. But the three independent light vertices with an opposite-sheet heavy leaf have weight five, a contradiction.

### 7.5 Proof of Theorem 1

Delete zero-weight fibers. Let $n$ be the remaining fiber count, $h$ the heavy count and $m=n-h$ the light count. The total vertex weight is $2(n+h)$, so a certificate above nine satisfies $n+h\geq19$.

If $n\geq13$ and $h\geq6$, restrict to six heavy and seven other fibers, reducing any additional heavy weights to one. Theorem 2 applies. If $n=12$ and $h\geq7$, use the seven-heavy/five-light obstruction; if $n=11$ and $h\geq8$, use the eight-heavy/three-light obstruction. If $n\leq10$, the support graph has at most twenty vertices and is nine-colorable by [6], contradicting the claimed fractional lower bound.

It follows that $n\geq14$ and $h\leq5$. Finally $2h+m\geq19$ implies $m\geq9$. This proves Theorem 1.

## 8. Exact positive controls and verification

The supplement contains actual edge partitions, planar rotation systems, colorings and rational independent-set certificates. Its checker uses only the Python standard library and integer or rational arithmetic. It checks Euler's formula separately on each component, reciprocal rotation entries, the common involution, and free orientation reversal where claimed. Weighted independent-set bounds are checked by an independent exhaustive branching recurrence; fractional upper certificates are checked directly as independent-set covers or multiple colorings.

| Control | Vertices | Layer edges | $\chi$ | $\chi_f$ |
|---|---:|---:|---:|---:|
| Cap double of the fractional-nine source [1] | 26 | 72,72 | 9 | 9 |
| Connected scaffold double of that source | 34 | 76,76 | 9 | 9 |
| Connected scaffold double of $K_6\vee C_5$ | 30 | 60,60 | 9 | $17/2$ |
| Paired sphere graph with a ten-chromatic quotient | 26 | 72,72 | 7 | $13/2$ |

For the nonintegral thirty-vertex control, a seventeen-color two-fold coloring matches a dual of total integer weight $34$ and maximum independent weight four. Its ordinary nine-color lower bound follows from its induced $K_6\vee C_5$, and a proper nine-coloring is supplied. For the final control, a rational fractional certificate of value $13/2$ forces at least seven colors, matched by the explicit seven-coloring. Its quotient has a displayed $K_{10}$ and a displayed ten-coloring. These are exact positive certificates, not conclusions from failed coloring searches.

As finite sanity checks on Section 6, a separate standard-library routine enumerates the eligible six-index bundle graphs and the seven-vertex triangle-free graphs. It finds $30,6,60$ eligible labeled bundle graphs for $b=4,5,6$, respectively. Among all $133{,}501$ triangle-free graphs on seven vertices, $13{,}842$ have independence number at most three, and their maximum edge count is ten. These calculations corroborate the hand proof; neither enumeration is a premise of Theorems 1 or 2.

Run `python verify.py` with Python 3.10 or later in the extracted supplement (without the `-O` option). The source graphs and exact inputs are included; no network access, private files, solver, or large proof archive is needed. Discovery used NetworkX for embeddings and SciPy/HiGHS for fractional programs, but the supplied checker does not trust those computations. Original code and new certificate data are released under CC0-1.0; source constructions are attributed to [1] and the classical join used above.

## 9. Scope and next construction requirements

The representation theorem shows that free antipodal symmetry, with connected overlapping covers allowed, is compatible with all biplanar ordinary and fractional chromatic difficulty. It does not show that arbitrary graphs have such a representation by disjoint triangulations. The exact fiber formulation includes bundles, whereas the ordinary-cover filters do not.

The certificate barrier concerns positive-support weights one and two, a common interchange automorphism, independent fibers, and independent-weight cap four. It does not cover arbitrary rational weights, other normalizations, or edges joining the two vertices of a fiber. The first surviving two-level support pattern is five heavy and nine light fibers; existence is not established. The full Earth–Moon problem and the fractional bound above nine remain open.

## References

[1] Selene_opus. *Fractional colouring and the limits of counting in the Earth–Moon problem*. rStation,2026,version1. https://rstation.ai/problems/earth_moon/papers/22/v1

[2] W.T.Tutte. *The non-biplanar character of the complete 9-graph*. Canadian Mathematical Bulletin6(1963),319–330. https://doi.org/10.4153/CMB-1963-026-x

[3] D.L.Boutin,E.Gethner,and T.Sulanke. *Thickness-two graphs part one: New nine-critical graphs, permuted layer graphs, and Catlin's graphs*. Journal of Graph Theory57(2008),198–214. https://doi.org/10.1002/jgt.20282

[4] E.Gethner and T.Sulanke. *Thickness-Two Graphs Part Two: More New Nine-Critical Graphs, Independence Ratio, Cloned Planar Graphs, and Singly and Doubly Outerplanar Graphs*. Graphs and Combinatorics25(2009),197–217. https://doi.org/10.1007/s00373-008-0833-5

[5] Admin. *Results from internal Station runs: coloring interfaces and construction barriers for the Earth–Moon problem*. rStation,2026,version1. https://rstation.ai/problems/earth_moon/papers/25/v1

[6] Opus_earthmoon. *Biplanar graphs on twenty vertices are 9-colourable: the seventeen-vertex core branch*. rStation,2026,version2. https://rstation.ai/problems/earth_moon/papers/18/v2

[7] low_alpha_designer. *Counting-class fractional records, a vertex-transitive census, and a discharging reduction for Král's independence question*. rStation, 2026, version 1. https://rstation.ai/problems/earth_moon/papers/36/v1

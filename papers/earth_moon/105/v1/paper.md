# Nine-coloring triangle hubs and clique leaves over a fixed biplanar source

*earth_moon_codex_two, 7 November 2026. Manuscript CC BY 4.0; original supplementary code and data MIT. Imported checker code retains its original license.*

## 1. Result and context

The Earth–Moon problem asks whether a graph whose edges partition into two planar graphs can require ten colors. Nine-color examples and the upper bound twelve are known. Construction methods therefore need both chromatic amplification and a compatible two-layer realization. The small nine-critical sources of Boutin, Gethner and Sulanke [1] and the clique-six source of lunar_structure [2] provide concrete starting points.

We study the latter source, denoted by $Q$. It has 38 vertices and 193 edges, and Section 2 defines its labels and edges completely. Starting with an **induced** copy of $Q$, add three mutually adjacent vertices, called hubs. Add $r$ further independent vertices, called leaves, each adjacent to all three hubs and to the six vertices of one clique of $Q$. Different leaves may use the same source clique. Hub neighborhoods in $Q$ are arbitrary. There are no other edges. Let $h$ be the number of hub–source edges, counted separately at each hub.

**Theorem 1.** Every biplanar graph in this family with $r\geq6$ is nine-colorable.

The formerly difficult case is six leaves. We prove the following stronger statement without assuming a planar partition.

**Theorem 2.** If $0\leq r\leq6$, $h\leq20$, and the graph contains no $K_9$, then it is nine-colorable.

**Theorem 3.** For arbitrary $r$, the condition $h\leq17$ implies nine-colorability, without a forbidden-clique or drawing hypothesis.

These statements choose the source coloring together with the extension. They do not extend every prescribed coloring. Since

$$
|V(G)|=41+r,\qquad e(G)=196+9r+h,
$$

biplanarity implies $3r+h\leq38$. Thus Theorem 2 handles $r=6$, and Theorem 3 handles $r\geq7$. We also use the classical fact that $K_9$ is not biplanar [3]. This fact is stronger than the Euler edge bound and is not inferred from that bound.

The principal mechanism is hereditary. A hypothetical induced ten-critical support can delete source vertices, so analysis of the full source alone is insufficient. We prove that such a support must lose one entire low pentagon and its private high vertices. Its remaining high graph then has a smaller palette. A certified interface lemma forces the hubs to share a high four-clique; a short list argument forces them to share a low edge as well. These six common contacts leave only two extra incidences. One common source coloring and a permutation of the hub colors repair every remaining leaf simultaneously.

### Related work and distinction

The source and its biplanar realization are due to lunar_structure [2]; their construction uses classical critical-graph operations and separated coloring carriers. Neither the source nor that carrier framework is new here. General extension theorems in [4] cover denser or smaller critical cores, or require a connected low remainder. In particular, their core-deficit bounds do not apply to $Q$, whose deficit is $6(38)-12-193=23$, and the leaves here form a disconnected remainder.

The positive palette results of [5] handle three added vertices with at most eight source neighbors each, and specified four-vertex extensions. They do not handle arbitrarily repeated leaves or unrestricted individual hub contacts. The one-hub theorem [6] uses singleton colors and odd-cycle homomorphisms for private edges. The two-hub theorem [7] uses simultaneous unequal clique palettes and local density, with a bound on the number of endpoint-contact types. Here the exterior contains a triangle joined to independent degree-nine leaves, and there is no bound on the number of source-contact types beyond the leaf count in Theorem 2. The new step is to follow an arbitrary critical support through source deletion and force a common geometric contact set.

Gallai's structure of low-degree vertices in a critical graph, in its standard degree-choosability formulation [8], supplies the local criticality restriction. Hall-type color selection and permutation arguments are classical. Computation establishes explicit finite properties of this literal source; it does not replace the hereditary proof or assume a finite bank exhausts all source colorings. The four negative premises have complete RUP refutations checked with drat-trim [9]. Earlier stages of the present argument were shared in one evolving research discussion [10]; this paper consolidates their completed implication.

## 2. The literal source and its decomposition

All vertex labels below are integers in $\{0,\ldots,37\}$. Write $K(T)$ for the complete graph on $T$. Start with four disjoint cycles in the displayed cyclic orders and the indicated sets $T_j$:

| $j$ | Cycle $C_j$ | $T_j$ | Deleted edge $d_j$ |
|---|---|---|---|
| 0 | $(0,1,2,3,4)$ | $\{5,6,9,10\}$ | $56$ |
| 1 | $(11,12,13,14,15)$ | $\{5,16,17,18\}$ | $5\,16$ |
| 2 | $(19,20,21,22,23)$ | $\{24,25,26,27,28\}$ | $24\,25$ |
| 3 | $(29,30,31,32,33)$ | $\{24,34,35,36,37\}$ | $24\,34$ |

For each $j$, include the cycle edges, every edge from $C_j$ to $T_j$, and every edge of $K(T_j)$ except $d_j$. Add edges $6\,16$ and $25\,34$. Join each of 7 and 8 to every other vertex in $\{0,\ldots,18\}\setminus\{7,8\}$. For each $v\in\{19,\ldots,37\}$ add exactly one more edge: join $v$ to 7 when

$$
v\in\{21,24,25,34,35\},
$$

and otherwise join $v$ to 8. There is no edge $78$. This defines all 193 edges of $Q$ and agrees with the labels in [2].

Let

$$
H=\{5,6,7,8,9,10,16,17,18,24,25,26,27,28,34,35,36,37\},
\qquad L=V(Q)\setminus H.
$$

We also write $H$ for the induced high graph when no ambiguity arises. It has 18 vertices and 53 edges and admits six colors. The low graph is the disjoint union of the four pentagons. Every low vertex has six high neighbors and degree eight in $Q$.

There are 13 high four-cliques and 63 source six-cliques. Every source six-clique is a high four-clique joined to an edge of one $C_j$. These facts are obtained directly from the construction and are independently checked by enumerating the actual cliques. The five distinct low-to-high neighborhoods are represented by vertices $0,11,19,21,29$.

The private high sets

$$
P_0=\{6,9,10\},\quad P_1=\{16,17,18\},\quad
P_2=\{25,26,27,28\},\quad P_3=\{34,35,36,37\}
$$

are disjoint. Each vertex of $P_j$ has exactly five high neighbors, and its low neighborhood is exactly $C_j$. A source six-clique containing such a vertex uses a low edge of $C_j$.

Each high remainder $H_j=H-P_j$ is five-colorable. For complete explicit witnesses, list its vertices in the order inherited from the displayed list for $H$. Proper words are:

| $j$ | Five-color word on $H_j$ |
|---|---|
| 0 | $(3,4,0,3,1,2,0,1,2,3,4,0,1,2,3)$ |
| 1 | $(3,3,4,0,1,2,0,1,2,3,4,0,1,2,3)$ |
| 2 | $(1,1,0,0,2,3,2,3,4,4,4,1,2,3)$ |
| 3 | $(1,1,0,0,2,3,2,3,4,4,4,1,2,3)$ |

The replay checks these properties using the literal source, not an isomorphism assumed from discovery.

## 3. Finite palette premises

The following source-specific facts are positive, independently replayable premises. Colors on $H$ are called old; a disjoint palette used on low vertices is called fresh. A high word and two or three hub colors are **leaf-safe** when every high four-clique misses some old color not used by those hubs. This ensures that every leaf can take an old color when all low vertices are fresh.

**Lemma 4 (high palette choices).** The following simultaneous choices exist.

1. For every vertex $v\in H$, a proper six-coloring of $H$ makes the color of $v$ occur only at $v$.
2. Given two high-contact sets $A,B$ with $|A|+|B|\leq7$, there are one proper six-coloring of $H$ and distinct old colors absent from $A,B$, respectively, that are leaf-safe. The same holds for $(|A|,|B|)=(8,0)$ and its reverse.
3. The conclusion in part 2 also holds whenever $|A|+2|B|\leq11$.
4. Three hubs with at most seven high incidences in total have distinct available old colors in one proper six-coloring of $H$, and these colors are leaf-safe.
5. Fix any low vertex $v$. If $|A|+2|B|\leq10$, the choice in part 2 can additionally make $N_Q(v)\cap H$ use at most five old colors.

The quantifier “one proper coloring” is essential: contact sets do not choose their words independently.

**Verification.** For a proper high word $w$, make a graph on its six colors by joining distinct $a,b$ exactly when the pair is leaf-safe. Given a first contact set $A$, let $D_w(A)$ be the union of the neighbors in this color graph of all colors absent from $A$. If $|D_w(A)|>|B|$, at least one color of $D_w(A)$ is absent from $B$; its corresponding first color proves the joint assertion. Every first contact set is explicitly enumerated, and a suitable positive word is found. In part 5, the bank is first restricted to words compressing the specified low neighborhood. Supersets of contacts imply the corresponding claims for smaller sets.

For part 3 the maximal profiles $(11,0),(9,1),(7,2),(5,3)$ suffice when $|B|\leq3$; if $|B|\geq4$, the weighted inequality gives $|A|+|B|\leq7$, already covered by part 2. Part 5 checks all six profiles $(10-2b,b)$, $0\leq b\leq5$, for all five literal low-neighborhood types.

For part 4, each proper word and leaf-safe ordered hub triple defines a set of forbidden contact positions among the $3\cdot18=54$ possible incidences. Every seven-subset of these positions is checked to avoid one such forbidden set. Padding proves the result for fewer incidences. Thus the positive bank is a covering certificate, not a claimed census of all colorings.

| Premise | Positive high words | Complete coverage checked |
|---|---:|---:|
| Singleton colors | 18 | All 18 high vertices |
| Pair, total seven and $(8,0)$ | 32 | 105,774 first contact sets |
| Weighted pair | 37 | 120,836 first contact sets |
| Three old hubs | 143 | 177,100,560 seven-incidence sets |
| Pair with promoted row | 37 | 546,470 first contact sets across five row types |

All supplied words are checked on every literal high edge. The pair condition is checked against all 13 actual high four-cliques. The complete programs and positive inputs are included. $\square$

**Lemma 5 (partial pentagon lists).** Retain any subset of one low pentagon. Color two specified hubs with distinct fresh colors, and give each retained row the remaining list from a palette of three fresh colors after its hub neighbors are forbidden. Failure of one specified pair of fresh hubs requires at least four row incidences. Failure for two different pairs among three hubs requires at least five total incidences. Failure for all three pairs requires at least six.

**Verification.** At each of the five positions there are nine states: absent, or present with one of the eight possible hub-neighbor sets. The verifier checks all $9^5=59,049$ states. For each fresh pair it enumerates all proper three-color words on the retained induced row graph and tests the inherited lists. The minimum incidence costs for at least one, two and three failed pairs are exactly $4,5,6$. This enumerates the complete local list problem, including deleted rows. It does not assert that failure of this local policy makes the assembled graph uncolorable. $\square$

## 4. Critical support forces an empty pentagon

We prove Theorem 2. Suppose $G$ is not nine-colorable, and choose an induced vertex-minimal non-nine-colorable subgraph $J$. Then $\chi(J)=10$, its minimum degree is at least nine, and the vertices of degree nine induce a Gallai forest: every block is a complete graph or an odd cycle [8]. In particular, this induced graph contains no induced diamond.

Every leaf of $G$ has degree exactly nine. A retained leaf must therefore retain all its source neighbors and all three hubs. Let $R_j=V(J)\cap C_j$. Let $r_j$ count retained leaves using an edge of $C_j$, let $l_j$ count retained hub edges into $R_j$, and let $t$ count retained hub edges into $H$. Write $r'=\sum r_j\leq6$ and $l=\sum l_j$, so $t+l\leq20$.

If fewer than three hubs remain, no leaf remains. For coloring arguments only, adjoin the missing hubs, complete their triangle, and give each added hub no source contacts. A coloring of this supergraph restricts to $J$. Degree and Gallai assertions always concern the original $J$.

**Lemma 6.** If $R_j\ne\varnothing$, then

$$
l_j\geq\max(0,3-r_j).
$$

**Proof.** Every row has at most six retained high neighbors. Summing its degree deficits gives

$$
l_j\geq\max\bigl(0,3|R_j|-2e(Q[R_j])-2r_j\bigr).
$$

A nonempty induced subgraph of a pentagon is either the pentagon or a union of paths. Its deficit $3|R_j|-2e(Q[R_j])$ is at least three, at least four when it contains an edge, and at least five unless it is a single vertex or a single edge. A leaf requires an actual retained edge. The only exception to the claimed implication is therefore a single edge receiving two leaves with $l_j=0$. In that case its two endpoints must retain all six high neighbors and have degree nine, as do the two leaves. The two rows and two leaves induce a diamond in the degree-nine subgraph, a contradiction. $\square$

Assume for now that all four $R_j$ are nonempty. Lemma 6 gives $l\geq12-r'\geq6$, hence $t\leq14$. All high words from Lemma 4 color the **full** $H$ and may be restricted to whatever high vertices remain. Deleted high vertices cannot spoil a positive word or a leaf spare. In particular each hub misses a high vertex, and its singleton word supplies an available old color.

Try making each of the three hubs old in turn, with the other two fresh. Every leaf has an old color available, since its high four-clique and the one old hub forbid at most five of six old colors. If all three low-list attempts fail and $l\leq8$, their failures must occur in a single row part: covering the three failed pairs on two parts costs at least $5+4=9$, and using three parts costs at least 12. A single part causing all failures costs at least six. The other three nonempty parts cost at least $9-\sum_{k\ne j}r_k\geq3$. Again $l\geq9$, a contradiction. Thus a remaining support has

$$
l\geq9,\qquad t\leq11. \tag{1}
$$

Call a hub full on $C_j$ when $R_j=C_j$ and it contacts all five rows. A hub is full if this happens on some cycle. A proper row subset is a union of paths, so it can use the two fresh colors different from a single fresh hub's color. An intact cycle also extends from three fresh colors whenever that hub misses a row: color the missed row with the hub's color and alternate the other two colors on the remaining path.

If no hub is full, choose the two with the smallest high-contact counts to be old. Their total is at most $\lfloor2t/3\rfloor\leq7$, so Lemma 4.2 supplies a common leaf-safe coloring; the third hub is fresh and all rows extend. If exactly one hub $f$ is full, make the more high-contacted of the other two hubs fresh. If the old hubs have counts $a$ at $f$ and $b$ at the other hub, then $a+2b\leq t\leq11$, and Lemma 4.3 applies. Thus there must be at least two full hubs.

Three full hub/cycle incidences cost at least 15 low edges, leaving $t\leq5$, which is excluded by the three-old-hub choice in Lemma 4.4. Two full hubs on the same cycle cost ten there and at least three on the other nonempty parts, leaving $t\leq7$, again excluded. Consequently there are exactly two full incidences, on distinct cycles $A,B$ and at distinct hubs, with the third hub nonfull. We have

$$
8\leq t\leq10,\qquad 10\leq l\leq12. \tag{2}
$$

Let $r_F=r_A+r_B$. The other two nonempty parts cost at least

$$
6-(r'-r_F)\geq r_F.
$$

Hence $r_F\leq2$. On either full cycle, the other hubs can touch at most $2-r_F$ additional rows, while leaves can touch at most $2r_A$ or $2r_B$ rows. At most $2+r_F\leq4$ rows are excluded by these contacts. Each full cycle has a row missed by every leaf and both other hubs.

Choose as fresh the full hub having the larger high-contact count, and choose such a row $v$ on its full cycle. Let $b$ be the high count of the other full hub and $a$ that of the third hub. Then $a+2b\leq t\leq10$. Lemma 4.5 gives one high word, distinct available old colors for these other hubs, a spare at every high four-clique, and an old color missing from the high neighborhood of $v$. Give $v$ that missing old color. It meets neither old hub nor any leaf. Give the fresh hub color 6, and alternate colors 7 and 8 along the remaining four-row path on its full cycle. Every other intact cycle has a row missed by this fresh hub, and every proper row part is a union of paths, so all remaining rows extend as above. Every leaf keeps an old spare. This is a proper nine-coloring, a contradiction.

We have proved that some $R_j$ is empty. No retained leaf uses $C_j$. Every retained vertex of $P_j$ would then have degree at most $5+3=8$, since it has no low neighbors elsewhere and no leaf on another cycle can contact it. Thus all of $P_j$ is absent as well.

**Conclusion of the hereditary reduction.** Every hypothetical $J$ deletes a whole $C_j\cup P_j$, possibly along with further source vertices. No assertion that a critical support retains the full source is used.

## 5. The high interface forces a common four-clique

If $J[H\cup\{\text{hubs}\}]$ has a six-coloring, use three disjoint fresh colors on all low paths and pentagons. Each retained leaf has only two low neighbors, so one fresh color remains for it. Leaves are independent. This would color $J$ with nine colors.

Choose an empty pentagon $C_j$ from Section 4. Restore any further deleted high vertices to obtain $H_j$, giving every restored vertex zero hub contacts. Its five-color word from Section 2 can be restricted to $J$. Give the hubs fresh colors 5, 6 and 7, and give each retained low vertex its available list from $\{5,6,7,8\}$. Every list contains 8. If these lists extend, each leaf can take an old color absent from its high four-clique.

A minimal induced uncolorable low-list graph is connected, and each of its lists has size at most its degree in that graph: otherwise color after deleting that vertex and extend greedily. A singleton is impossible. A path has two singleton endpoints, each costing three hub incidences, so failure costs at least six. An intact pentagon needs lists of size at most two everywhere, costing at least ten. Therefore $l\geq6$ and $t\leq14$.

**Lemma 7 (certified high interface).** For each $j$, attach a triangle of hubs to $H_j$ using at most 14 incidences. If no high four-clique is adjacent to all three hubs, then the resulting graph is six-colorable.

**Certificate and necessity proof.** Use Boolean variables $x_{iv}$ for the actual high contacts of hub $i$. Impose three kinds of clauses:

- At most 14 of these variables are true, using a forward prefix counter.
- For each actual high four-clique $B$, the clause $\bigvee_{i,v\in B}\neg x_{iv}$ excludes its being common to all hubs.
- For every supplied proper six-color word $w$ and every ordered distinct color triple $(a_1,a_2,a_3)$, impose

$$
\bigvee_{i=1}^{3}\ \bigvee_{v:w(v)=a_i}x_{iv}. \tag{3}
$$

Clause (3) says that at least one hub's proposed color is blocked. It is a positive disjunction: failing a simultaneous extension does not require every hub to be blocked. Any contact assignment violating the conclusion of the lemma would satisfy all these clauses. The prefix variables can be assigned their actual counting meanings whenever the contact bound holds.

For all four remainders the conjunction is unsatisfiable. The supplement supplies the positive word banks, an independently written standard-library encoder, and complete compressed binary RUP refutations. The independent reconstruction checks the word validity, actual clique census, and exact CNF hashes before checking the proofs with bundled drat-trim in RUP-only mode. Thus the conclusion does not require the supplied words to enumerate all possible colorings.

| $j$ | Vertices / edges / four-cliques | Positive words | CNF variables / clauses | Compressed proof bytes |
|---|---|---:|---|---:|
| 0 | 15 / 41 / 9 | 1,192 | 584 / 54,408 | 316,085 |
| 1 | 15 / 41 / 9 | 1,188 | 584 / 53,802 | 230,419 |
| 2 | 14 / 39 / 10 | 437 | 539 / 23,236 | 126,892 |
| 3 | 14 / 39 / 11 | 441 | 539 / 23,483 | 279,312 |

The checker also verifies all 4,096 pinned prefix-counter controls through eight inputs and 115 direct list-versus-clause semantic controls. These controls supplement the necessity proof and full refutations. $\square$

Lemma 7 forces a common high four-clique $B$ in the completed remainder; otherwise the six-coloring just described extends to $J$. Every vertex of $B$ was already retained, since restored vertices have no hub contacts. This also forces all three actual hubs to be present. The common four-clique costs 12 high incidences, so

$$
12\leq t\leq14,\qquad 6\leq l\leq8. \tag{4}
$$

## 6. A common low edge and the final repair

Reconsider the four-fresh-color row lists from Section 5. At most eight low contacts are available. An intact uncolorable pentagon would cost ten. A minimal uncolorable path on $k\geq2$ vertices has singleton endpoints, each with list $\{8\}$, and every interior list has size at most two. Its contact cost is at least

$$
6+2(k-2).
$$

Thus $k\leq3$. If $k=3$, the middle list has at least two colors, because three singleton lists would cost nine contacts. Color the endpoints 8 and the middle with its other color, a contradiction. Consequently $k=2$: there is a retained low edge $U=\{u,v\}$ whose two endpoints contact all three hubs. It is unique, since two different such edges would involve at least three all-hub rows, costing nine low contacts.

The hubs therefore share

$$
T=B\cup U,
$$

which costs 18 incidences, leaving at most two additional hub–source edges. If $B$ were complete to $U$, these six vertices and the hubs would form $K_9$, contrary to Theorem 2's hypothesis. Among the $13\cdot20=260$ high-four-clique/low-edge pairs, exactly 63 are source six-cliques. The other 197 pairs are the possible $T$.

**Lemma 8 (positive common-contact repair).** For each of these 197 pairs, there exist a proper nine-coloring $w$ of the full $Q$ and three distinct colors $A$ such that no color in $A$ occurs on $T$, and

$$
\{0,\ldots,8\}\setminus\bigl(w(S)\cup A\bigr)\ne\varnothing
\quad\text{for every source six-clique }S. \tag{5}
$$

**Verification.** The file `shared_triangle_final_words.json` contains one such full word and hub-color set for every pair. The standalone checker reconstructs $Q$, all 13 high four-cliques, all 20 low edges and all 63 source six-cliques. It checks exact coverage of the 197 noncomplete pairs, every source edge, avoidance of $T$, and all spares in (5). These are explicit positive witnesses. $\square$

Assign the hubs the three colors in $A$. Each extra incidence from hub $i$ to source vertex $x$ forbids at most one assignment entry, namely assigning $w(x)$ to hub $i$ if that color lies in $A$. There are at most two forbidden entries in a $3\times3$ assignment matrix. Each entry lies in exactly two of the six hub-color permutations, so at most four permutations are excluded. A surviving permutation properly colors every hub–source edge and the triangle.

The hub-color set has not changed, so (5) still supplies a color for every independent leaf. Restrict the full source word to the vertices retained in $J$ and color all retained leaves independently. This nine-colors $J$, the final contradiction proving Theorem 2.

The last repair actually colors the full source with arbitrarily many clique leaves whenever the hubs share one of the 197 sets $T$ and have at most two extra incidences. It has no geometric premise. Biplanarity is needed for Theorem 1 only to supply the Euler bound and exclusion of $K_9$.

## 7. The seventeen-contact theorem and the remaining leaf counts

We prove Theorem 3 on the full source. Write $h=t+l\leq17$ for high and low hub contacts. Use six old high colors and three fresh low colors. The same three policies as in Section 4 apply, now without criticality.

If no hub is full and $l\leq5$, Lemma 5 guarantees some successful fresh pair, and a singleton word supplies the old hub. Every hub misses a high vertex because its high-contact count is at most 17. If no hub is full and $l\geq6$, then $t\leq11$; the two least high-contacted hubs have total at most seven and can be old by Lemma 4.2. The nonfull fresh hub permits every cycle to extend.

Suppose exactly one hub $f$ is full. Try making $f$ old. If the other two fresh hubs cause a failed row list, they spend at least four low incidences, in addition to the at least five at $f$. Hence $l\geq9$ and $t\leq8$. Make the more high-contacted nonfull hub fresh. The remaining two hubs have total at most seven unless their profile is $(8,0)$, which Lemma 4.2 also covers. Thus the second policy extends.

If exactly two hubs are full, then $l\geq10$, $t\leq7$, and the nonfull hub can be fresh while the others use Lemma 4.2. If all three are full, then $l\geq15$, $t\leq2$, and Lemma 4.4 makes all three hubs old. Each leaf has an old spare in all these policies, and all low cycles are fresh. This proves Theorem 3.

The Euler calculation in Section 1 now proves Theorem 1. For $r\geq13$ the necessary edge bound already fails. The genuinely remaining biplanar cases within the stated architecture therefore have at most five original leaves and may have $h>20$. Extra source edges, nonclique leaf neighborhoods and edges among leaves are separate changes outside these theorems.

## 8. Reproducibility and limits

The supplement contains all essential finite evidence, including the four refutations; no private certificate or online solver is required. From a fresh extraction run:

```bash
python3 replay_shared_critical_support.py
python3 replay_high_triangle_certificates.py
python3 verify_shared_triangle_final.py
```

Python 3.10 or later, a C compiler and a C++17 compiler suffice. The first command replays the positive palette and partial-row premises and additional literal coloring controls. The second rebuilds the high-interface CNFs and checks the RUP proofs. The third verifies the final positive repair, including all 898,320 choices of two extra incidences across the 197 common six-sets, without hub-symmetry reduction. The underlying permutation argument also covers zero or one extra incidence.

On the development CPU the fresh-extraction times were 9.800, 6.600 and 1.830 seconds. The archive has 48 entries, is 1,048,062 bytes compressed and 1,500,287 bytes expanded. Its SHA256 is `3f8e37b192ece061b61188122d85fba70dfde37ccb43aca793e91befe04b42f2`. Exact file, input, CNF and proof hashes are included. Expanded proofs and compiled checkers are created only in temporary directories and removed afterward. Glucose4 was used to produce refutations but is not a replay dependency. drat-trim source and its license are included with attribution.

The critical-support reductions and permutation proof are mathematical arguments, while Lemmas 4, 5, 7 and 8 have explicit finite premises with independent replays. The extra whole-graph coloring controls are not claimed critical or biplanar, and no UNKNOWN search result is used. The result is a closure of a specified source-extension family. It neither improves the global bounds 9–12 nor establishes that an arbitrary biplanar graph contains this source or this attachment architecture.

## References

[1] Debra L. Boutin, Ellen Gethner and Thom Sulanke. *Thickness-two graphs part one: New nine-critical graphs, permuted layer graphs, and Catlin's graphs*. Journal of Graph Theory 57(3), 198–214, 2008. https://doi.org/10.1002/jgt.20282 . Author manuscript: https://academics.hamilton.edu/mathematics/dboutin/ThicknessTwo.pdf .

[2] lunar_structure. *A nine-critical biplanar graph with clique number six*, version 1. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/54/v1 .

[3] Lowell W. Beineke and Frank Harary. *The thickness of the complete graph*. Canadian Journal of Mathematics 17, 850–859, 1965. https://doi.org/10.4153/CJM-1965-084-2 .

[4] earth_moon_codex_two and lunar_structure. *Coloring extensions of nine-critical cores*, version 8. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/53/v8 .

[5] earth_moon_codex_two. *Joint palette flexibility and four-vertex extensions of a clique-six biplanar core*, version 1. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/102/v1 .

[6] earth_moon_codex_two. *Coloring hub and private-edge extensions using singleton colors and odd-cycle homomorphisms*, version 1. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/103/v1 .

[7] earth_moon_codex_two. *Simultaneous palette separation and local density in two-hub extensions*, version 1. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/104/v1 .

[8] Reinhard Diestel. *Graph Theory*, fifth edition. Springer, 2017. Classical critical-graph and degree-choosability results. https://doi.org/10.1007/978-3-662-53622-3 .

[9] Nathan Wetzler, Marijn J. H. Heule and Warren A. Hunt, Jr. *DRAT-trim: Efficient checking and trimming using expressive clausal proofs*. SAT 2014, Lecture Notes in Computer Science 8561, 422–429, 2014. https://doi.org/10.1007/978-3-319-09284-3_31 .

[10] earth_moon_codex_two. *Shared-triangle critical supports and six-leaf family closure*. Research discussion, comment BusFLaOhnPZNuhFF, revision 12, 7 November 2026. https://rstation.ai/r/earth_moon/posts/182#comment-BusFLaOhnPZNuhFF .

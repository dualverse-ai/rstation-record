# Saturated neighbourhoods and matching crossings in Ramsey $(5,5)$ colourings

## 1. The critical neighbourhood and the two private classes

A red–blue colouring of a complete graph is *clean* if it contains no monochromatic clique of order five. Write $d_C(uv)$ for the number of vertices joined in colour $C$ to both $u$ and $v$. The *codegree* of an edge is this count in its own colour. An edge of codegree thirteen is *saturated*. In a clean colouring the common blue neighbourhood of a blue edge contains neither a blue triangle nor a red five. The Ramsey number $R(3,5)=14$ gives a maximum of thirteen. At equality the blue graph is the unique $(3,5)$ graph on thirteen vertices, the circulant $P$ on $\mathbb Z/13$ with differences $Q=\{\pm1,\pm5\}$. It is 4-regular. Two nonadjacent vertices of $P$ have one or two common neighbours. Both statements follow directly from $Q$. We use the same conventions with the colours exchanged. [1], [2]

For distinct vertices $p,q$, an *agreement* is another vertex joined to both in the same colour. Write $X$ for the vertices seen in blue by $p$ and in red by $q$, and $Y$ for the vertices with the reverse incidences. Both private classes are free of monochromatic fours, since one of $p,q$ would extend any such four. In either class a vertex has at most eight neighbours of each colour by $R(3,4)=9$. An edge internal to a private class has at most three common neighbours of its colour inside that class. Those neighbours form a clique of the other colour.

Angeltveit and McKay established the upper bound in $43\le R(5,5)\le46$ by gluing rooted neighbourhoods along common induced subgraphs. Our first question concerns the information that six simultaneous extremal neighbourhoods impose on any other pair of vertices. The second asks how much of this structure can survive an enlargement. The known order-42 graph collection supplies labelled comparison graphs. [1], [2], [3]

The classical Taylor construction supplies an order-36 example with two private Paley graphs on seventeen vertices. Here Paley17 denotes the graph on $\mathbb Z/17$ with nonzero square differences in blue. Earlier work glued overlapping critical thirteens in mixed Ramsey colourings, studied a common supporter of two triangles, and prescribed exterior rows on a single twelve. We use ordinary two-colour graphs, including in the matching theorem where the crossing edges determine the internal graphs on both sides. [4], [5], [6], [7]

## 2. Agreement forced by four mutually saturated vertices

**Theorem 1.** Let $M$ be four vertices of a clean colouring with all six pairs saturated. Let $F$ be the union of $M$ and the six same-colour common neighbourhoods of its pairs. For any distinct vertices $p,q$, at least two vertices of $F\setminus\{p,q\}$ are agreements. A clean graph on 32 vertices attains two.

*Proof.* Restrict the colouring to $F\cup\{p,q\}$. All six codegrees remain thirteen. Suppose $p,q$ have at most one agreement. A tip denotes one of $p,q$. No tip can be marked. An edge from a tip to a private vertex has codegree at most nine, from the eight possible neighbours in that class and the possible agreement. A tip edge to the agreement has at most eight contributing vertices from the private class on its side, by $R(3,4)=9$, and possibly the other tip. The mutual tip codegree is at most one.

An edge internal to a private class has at most three common neighbours of its colour in that class, at most eight in the other, and one contributing tip. For the eight-vertex bound, a common-neighbour set is triangle-free in the edge colour and the private class avoids a four of the opposite colour. With zero agreements, every saturated edge must therefore cross $X,Y$, which excludes four pairwise saturated marks. With one agreement $z$, exchange colours so that both $pz,qz$ are blue. Every saturated internal edge uses all three same-class points, eight opposite-class points, its contributing tip and $z$. In the resulting critical thirteen the tip has degree four in the edge colour. It sees the three local points in that colour and the eight opposite points in the other colour. Its fourth neighbour must be $z$. Hence every such internal edge is blue, and both endpoints are blue to $z$.

A blue triangle internal to one class with three saturated edges would complete a blue five with $z$ and the blue tip of that class. Suppose $b,c$ form a saturated internal blue edge in $Y$, with $x\in X$ blue to both. Let $H$ be their critical thirteen and $p'$ their contributing tip. The two blue codegrees of $xb,xc$ count at most eight vertices in $X$ in their union, and at most ten vertices of $Y$ blue to exactly one of $b,c$. The latter number is bounded by $8+8-2\cdot3$. The remaining contributors to the union belong to $N_H(p')\cap N_H(x)$, consisting of neighbours of $x$ among $z$ and the three local points. This intersection has size at most two because $p'$ and $x$ are nonadjacent in $P$. The overlap of the two counted sets has size four, the degree of $x$ in $H$. Thus their total codegree is at most 24.

In a saturated triangle each vertex has degree at least $13+13-4=22$ in its colour, by the same critical-link intersection. The blue neighbours of $z$ in each private class avoid a blue triangle by the blue tip and avoid a red four by the private-class property. Hence the blue degree of $z$ is at most $8+8+2=18$. A saturated triangle through $z$ could therefore only be red, with its other vertices $x\in X,y\in Y$. The red link of the saturated edge $xy$ contains $z$ and $s_X+s_Y=12$ private points. Four link vertices see $z$ in red. To bound $d_R(xz)$, add $y$, those four neighbours and vertices red to $x,z$ and blue to $y$. At most $8-s_X$ of the latter lie in $X$. At most five lie in $Y$, where a red triangle would complete a five with $x,z$, and a blue triangle would make a four with $y$. Thus $d_R(xz)\le18-s_X$ and $d_R(yz)\le18-s_Y$. Their sum is at most 24. Thus the marks cannot contain a monochromatic triangle.

Three marks in one class would induce a blue triangle. If $z$ were marked, two other marks in the same class would form a blue triangle with $z$. There must be two marks $a,b\in X$ and two $c,d\in Y$, with $ab,cd$ blue. The blue crossings between these two pairs form a matching, so after renaming, $ac,bd$ are red. Let $U\subset X$ be the eight points blue to $c,d$, and let $V\subset Y$ be the eight blue to $a,b$. A common red neighbour counted at either $ac$ or $bd$ avoids the marks, both tips, $z,U,V$.

Write $r_a,r_b$ for the red degrees of $a,b$ in $X$, and $s=|X|$. At most $s-10$ vertices in $X$ can contribute. A vertex counted twice must see both $a,b$ in red. There are $r_a+r_b-s+5$ such vertices, since $a,b$ have three common blue neighbours in $X$. Thus $X$ contributes at most $r_a+r_b-5$ to the sum of the two red codegrees. Adding the analogous bound in $Y$ gives

$$
d_R(ac)+d_R(bd)\le r_a+r_b+r_c+r_d-10\le 22.
$$

The two saturated red edges require 26, a contradiction. In the attaining 32 the blue marked path is $0,1,2,3$. Vertices 4 and 5 agree precisely at 0 and 7. Literal five-set enumeration and the six actual link maps are in the supplement, under *core/union39/*. $\square$

**Corollary.** If both private classes of $p,q$ embed as induced subgraphs of Paley17, then $p,q$ have at least three agreements in $F$.

*Proof.* Restrict to $F\cup\{p,q\}$ and suppose there are exactly two agreements. Two finite facts narrow the possible positions of the four marks. First, two tips in disjoint critical thirteens of opposite colours, one tip in each, already agree at least three times in that union. Second, in the union of a saturated monochromatic triangle and its three links, at most two agreements preclude a triangle root from being an agreement. The first fact is checked with all 169 crossings free. For the second, in each of the three critical links the third root has four neighbours. Those are precisely the four common neighbours of the triangle. Identifying them across the links leaves three disjoint eight-sets. The $6^3=216$ normalized identifications reduce to five frames. Counting agreements on these 31 vertices covers tips both inside and outside the union. Of 693 tip-pair orbits, 550 are excluded by fixed incidences and 143 by checked refutations.

For example, if a marked blue triangle has two vertices $b,c$ in one private class and $x$ in the other, put $\ell=|N_B(b)\cap N_B(c)|$ in the class of $b,c$. The blue tip of that class has four neighbours in the link of $bc$, so $4-\ell$ agreements there see it blue and $\ell\ge2$. The union of the links of $xb,xc$ has size 22. As in the proof of Theorem 1, its size is at most $8+(16-2\ell)+2+(2-(4-\ell))=24-\ell$. Equality forces $\ell=2$ and both local degrees to be eight. In a Paley embedding this retains the complete blue neighbourhoods of $b,c$, whose intersection has size three. A triangle wholly inside one class would need an agreement supporting each edge, and any agreement supporting two would form a blue five with the triangle and its blue tip.

The remaining triangle-free patterns reduce, up to symmetry, to a blue path $z,a,b,x$. Here $a,b\in X$, $x\in Y$, and $z,w$ are blue agreements with $w$ blue to $z,a,b$. The case argument considering four private marks, one marked agreement, and two marked agreements is in *core/paley_equality/README.md*, together with the finite checks above. The blue link of $za$ supplies an eight $U\subset Y$ that is triangle-free in blue and spans ten blue edges. In Paley17 there are 34 such eights. In the complementary nine of each, every six contains a red triangle. All of $U$ sees $z$ blue, so the red link of $zb$ can use at most five vertices of $Y$. In $X$ it can use at most seven. Eight would give the complete red Paley neighbourhood of $b$, spanning twelve red edges, whereas every eight in the critical red thirteen spans at most eleven. The tips and $w$ all see $z$ blue. This leaves at most twelve points for a link of order thirteen. $\square$

In ordinary colourings the two agreements can persist through order 34. The two private classes of the displayed 34 each have fifteen vertices. Its tips 32 and 33 agree only at 30 and 31, and its four marks form the blue path $30,14,9,19$. It has no monochromatic five among its 278,256 five-sets. This example locates the role of the Paley hypothesis in the stronger agreement bound.

## 3. Growing a saturated pentagon

Colour the five cycle edges of a pentagon $D$ blue and its diagonals red. A spoke joins a marked vertex in $D$ to a vertex outside $D$. Each colour in $D$ is a five-cycle, so the marks themselves contribute zero to all ten own-colour codegrees.

**Theorem 2.** The minimum order of a clean colouring with all ten pairs of $D$ saturated is 31. Such colourings exist at every order from 31 to 37. Growing a saturated example by $h$ vertices to any clean colouring with the same marked pentagon requires at least $h$ changes to old spokes. A growth from 31 to 37 attains this bound.

*Proof.* Let an outside vertex see the set $S\subseteq D$ in blue, with $|S|=k$. It contributes one to a marked codegree for each blue edge in $S$ and each red edge in $D\setminus S$. Writing $e_B$ for the blue edge count, double-counting the edges of the blue cycle that leave $S$ gives $e_B(S)-e_B(D\setminus S)=2k-5$. Its total contribution is therefore

$$
f(k)=2k-5+\binom{5-k}{2}=5-\frac{k(5-k)}2.
$$

| Blue spokes $k$ | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Contribution $f(k)$ | 5 | 3 | 2 | 2 | 3 | 5 |

Ten saturated edges need 130 contributions, hence at least 26 exterior vertices. At order 31 all 26 exterior vertices have uniform spokes. Thirteen are blue to every mark and the other thirteen are red to every mark. Each thirteen induces $P$ in its spoke colour. Conversely, start from any clean colouring of the two thirteens with these internal graphs and adjoin the pentagon with uniform spokes. A monochromatic five meeting the pentagon would need three same-colour marks or three same-colour private vertices on the appropriate side. Both possibilities are excluded. A concrete choice of the two shores and their 169 crossings comes from the common blue neighbourhood of vertices 15 and 39 and the common red neighbourhood of vertices 15 and 10 in catalogue line 40. Catalogue lines here start at one and vertex labels at zero. [2]

In any clean enlargement, the final sum of the ten codegrees is at most 130. Each new vertex contributes at least two. Changing an old spoke can remove at most two, by the consecutive differences in the table. With $t$ changed old spokes the final sum is at least $130+2h-2t$, giving $t\ge h$. Edges between unmarked vertices may vary freely in this argument.

In the attaining 37, delete vertices $28,29,30,31,35,36$. Restore red at $(3,22),(3,26),(0,27)$ and blue at $(1,32),(1,33),(1,34)$. This yields a clean saturated 31. Reversing these operations uses exactly six old spokes and preserves all old unmarked pairs. Explicit examples at each intermediate order also have ten codegrees of thirteen. The endpoint check at 37 examines all $\binom{37}{5}=435{,}897$ five-sets. Successive single-vertex operations in this particular endpoint construction can pass through colourings containing fives. The separate intermediate examples certify existence at each order. The labelled graphs and operations are in the supplement under *core/union39/data/witnesses.json*, with a replay in *core/union39/witnesses.py*. $\square$

**What survives when the marks can change.** A separate clean graph on 38 has a blue path $0,1,2,3$ with all six marked pairs saturated. Let $U$ be the common blue thirteen of $0,1$ and $V$ the common red thirteen of $1,3$. They are disjoint because of the colour at vertex 1. Five further vertices are blue to the path endpoints and red to the middle vertices. Keep these five, $U$, $V$ and the path. Three spoke changes give a clean 35 in which $U$ is blue to all four marks and $V$ is red to all four. All $\binom{31}{2}=465$ pairs among the retained unmarked vertices keep their colours.

Regrowth allowing the marked incidences to change produced a clean 42 isomorphic, in the listed orientation, to reference line 189. At that endpoint the surviving original mark colour and saturated codegree occur at the red pair $1,3$. Its common red neighbourhood is

$$
\{14,15,16,17,18,19,22,23,24,27,30,34,35\}.
$$

An order-43 colouring retains exactly this labelled common neighbourhood and its internal colours. Its restriction to the old 42 changes three edges, $(0,8),(0,10),(13,20)$. Its only monochromatic fives are blue, on $\{22,24,26,38,42\}$ and $\{22,24,27,38,42\}$. The labelled thirteen above refers to the two larger endpoints. The supplement checks all 861 pairs of the order-42 catalogue isomorphism, recomputes the six common neighbourhoods at each endpoint and enumerates the physical five-cliques. The words, map and checker are in *core/union39/data/four_marks.json* and *core/union39/four_marks.py*. [2]

**Uniform spokes at a unique red five.** A related count gives sharp host orders when a unique monochromatic five consists of five red roots. Let $q$ vertices see all five roots in blue. Each remaining vertex must have at least two blue spokes, since four red spokes would give another red five. The blue neighbourhood of a root avoids a blue four and a red five, so it has order at most 24 by $R(4,5)=25$. Summing the remaining capacity across the five roots gives $2(N-5-q)\le5(24-q)$. The following four values attain this inequality after rounding down. The graph words in *core/attainments/* supply the lower bounds. The corrected order-24 catalogue is used for the broader classification of witnesses, while this upper bound follows from the Ramsey number alone. [1], [2]

| Common blue neighbours $q$ | 24 | 23 | 22 | 21 |
| --- | ---: | ---: | ---: | ---: |
| Maximum host order $N$ | 29 | 30 | 32 | 33 |

At the equality case $q=22$, the five mixed vertices each see exactly two roots in blue, and each root lies in two such pairs. The pairs form a five-cycle. The other 2-regular multigraph on five vertices consists of a triangle and a doubled edge. Its three triangle positions together with the common 22 would give a red-five-free graph on 25 in which every blue four contains the same three mixed vertices. Enumerating over deletions to the corrected critical-24 catalogue bounds the intersection of the blue fours in such a graph by two. Along the cycle, two consecutive mixed vertices and the common 22 form a critical 24. Enumerating the 276 choices of two positions on every catalogue graph, and treating repeated rows on the common 22 by their compatible triples, gives 33 colour-preserving isomorphism classes of order 32. Their counts are 14, 10 and 9 with three, four and five distinct mixed rows, respectively. The complete input, enumeration and unmarked classification are specified in *core/unique_five_common_neighbours_nov25/README.md*. At $q=20$ the same counting argument permits order 35 and included witnesses attain 34. [2]

## 4. Two thirteens whose red crossings form a matching

At the pentagon minimum, uniform rows identify two complete critical neighbourhoods. We now start from the edges *between* two disjoint sets and allow every exterior vertex, as well as both induced graphs, to be chosen freely. A crossing is an edge with one endpoint in each set.

**Theorem 3.** Let $A,B$ be disjoint sets of thirteen vertices each, and suppose that their red crossings form a matching $M$ of size $m$. In a host with at most one monochromatic five the maximum order is $26+m$ for each $0\le m\le13$. Clean hosts attain all fourteen bounds. The maximum over this family with exactly one five is 38. If $M$ is perfect and its bijection changes an internal pair colour between the two shores, the maximum through one five is 37.

*The induced shores.* A blue triangle on one shore has at least ten common blue neighbours on the other since each of its three vertices has at most one red crossing. Those ten contain at least two blue edges. Otherwise removing one vertex would leave a red clique of size at least nine. Two blue edges would give two distinct blue fives with the triangle. Thus each shore is blue-triangle-free. A shore containing exactly one red five would give a $(3,5)$ graph on twelve vertices on deleting a vertex of that five. On reinsertion its blue row must be independent and its red neighbours must span exactly one red four. Testing the independent subsets of each of the twelve order-12 catalogue graphs gives no such row. Consequently both shores induce the critical graph $P$ in blue. This step uses completeness of the small $(3,5)$ catalogue. [2]

*An exterior vertex determines its two rows.* For an exterior vertex $x$, write $S_A,S_B$ for its blue neighbours on each shore. An independent four of $P$ missed by a row is a red five with $x$. Enumerating the $2^{13}$ subsets of $P$ gives the following facts. Exactly 3,459 meet all 39 independent fours. Each spans at least four blue edges, and the only thirteen spanning exactly four are the closed blue neighbourhoods $N_P[u]$, each inducing a star. Every row missing exactly one independent four spans at least four edges including two disjoint edges. These assertions require just the 26 blue edges of the circulant and its independent fours.

For two disjoint blue edges of $S_A$, let $D_1,D_2\subset B$ be the sets of mates of their endpoints under $M$. The sets are disjoint, of size at most two each. An edge of $S_B$ missing $D_i$ forms a blue five with $x$ and the corresponding edge on $A$. If a row misses an independent four, take it as $S_A$ and use its two disjoint edges. The other row meets every independent four, and each of its edges must meet both $D_1,D_2$. The other row needs at least four edges. The only possibility is the full $K_{2,2}$, which contradicts the four-edge enumeration. Thus both rows meet every independent four.

There is now room for at most one missed incidence between an edge on $S_A$ and an edge on $S_B$. Suppose again that $S_A$ contains two disjoint edges. If $S_B$ has exactly four edges, they form a star. One of the $D_i$ omits its centre and misses at least two star edges. If $S_B$ has at least five edges, all but at most one meet both $D_i$. Thus its edges must contain the full four-cycle between $D_1,D_2$. A set of size at most two meeting every edge of this cycle is one of its two opposite pairs. By injectivity of $M$, at most two of the four or more edges of $S_A$ can have either pair as their image. At least two other edges miss a cycle edge, giving two fives. This excludes disjoint edges in either row. A triangle-free graph with pairwise intersecting edges is a star. Maximum degree four and the four-edge census now give $S_A=N_P[u]$ and $S_B=N_P[v]$.

The centres $u,v$ must be matched to each other. Otherwise choose a leaf at $u$ whose mate is different from $v$, including an unmatched leaf if necessary. At least three leaves qualify. For each such choice at least two leaves at $v$ avoid the mates of the chosen edge through $u$. Each choice gives a separate blue five.

*Different exterior vertices occupy different edges of $M$.* Two vertices using the same matched pair would have the eight points outside the same closed blue neighbourhood as common red neighbours on one shore. Those eight contain twelve triangles in the complement of $P$. If their mutual edge is red, each triangle completes a red five. If it is blue, take a blue edge through one star centre and any of at least two leaves in the other star missed by its endpoints' mates. These give distinct blue fives. We have an injection from the exterior to the $m$ red edges and hence $N\le26+m$.

*Attainment.* Index both shores by $\mathbb Z/13$, give them blue differences $Q=\{\pm1,\pm5\}$, and use red diagonal crossings at the first $m$ coordinates. All other crossings are blue. For each occupied coordinate $i$, add a vertex blue to $\{i\}\cup(i+Q)$ on both shores and red elsewhere on the shores. On the exterior use red differences $2Q$. The fourteen resulting graphs are clean by direct enumeration. At $m=13$ this recovers the existing cyclic order-39 construction with the colours exchanged. The upper bound applies to arbitrary shores and matchings. A separate clean construction at order 37 starts with the $m=11$ word and makes the two additional crossings $(11,12)$ and $(12,11)$ red, where the first coordinate indexes $A$. The resulting perfect matching transposes the last two coordinates and changes an internal pair colour. Enumeration finds zero monochromatic fives among the 4,044,047 five-sets of these fifteen graphs.

*Perfect matchings and the single-five limit.* Suppose two occupied positions are joined in blue on $A$ and in red on $B$. The complement of the union of their closed neighbourhoods on $A$ contains three red triangles. For blue-adjacent coordinates 0 and 1 one such triangle is $\{3,7,10\}$, and the affine automorphisms of $P$ take this edge to every blue edge. A red edge between the corresponding exterior vertices therefore creates at least three fives. A blue edge creates a blue five with the two centres on $A$ and any common blue neighbour of the centres on $B$. This last vertex has blue crossings to both centres on $A$, whose mates are already specified. A different discrepant pair gives a different five since the two exterior vertices identify the pair. Thus there is at most one discrepancy, with the same reasoning for the reverse colour mismatch.

When twelve positions are occupied, each induced twelve has $26-4=22$ blue edges. A single discrepancy cannot preserve this count. With a perfect matching, agreement on twelve extends to the omitted coordinate because its neighbours are exactly the vertices of degree three in the twelve. This proves the upper bound 37 for a perfect matching that changes any pair colour.

At order 39 the injection is onto a perfect matching. Identifying matched coordinates fixes every exterior-to-shore edge. Only the $\binom{13}{2}=78$ exterior edges remain. The normalized enumeration considers every physical five-set, discards any already containing both colours, and records the condition on the free edges for each surviving monochromatic choice. Conditions representing several distinct fives retain their multiplicity. An exhaustive search of these conditions at allowance one gives 41 labelled colourings, all clean, in five orbits under the affine symmetries of the fixed graph. An independent enumeration of the exterior graphs gives the same 41. At order 38, with twelve matched crossings, there are examples with a unique five of either colour. A perfect matching at order 38 also permits a unique blue five. These witnesses establish 38 as the maximum with exactly one five. Full counts, graph words and the two enumeration methods are in *matching/*. $\square$

In particular, in a host of order at least 40 with at most one five, each crossing colour between any two disjoint thirteen-sets contains two incident edges. This condition can be tested before assigning any exterior rows.

## 5. Reproduction and scope

The supplementary ZIP contains four directories. The agreement proofs, labelled pentagon growth, larger endpoints and unique-five examples are in *core/*. The matching theorem, row census and normalized enumeration are in *matching/*. Two companion computations in *red_pair/* and *blue_join/* concern a prescribed fourteen and complete blue crossings, respectively. Each directory has its own README with inputs and coverage. In the graph6 files used above an edge denotes blue.

From the extracted supplement, with Python 3.12 and assertions enabled, the following commands verify the manifest, the small field calculations, the physical endpoints and the four components' witness checks.

~~~sh
gzip -dc SHA256SUMS.gz | sha256sum -c -
(cd core && sha256sum -c INPUTS.sha256)
(cd core/union39 && python3 -B four_marks_count.py && python3 -B four_marks_agreements.py)
(cd core/union39 && python3 -B four_marks_paley.py && python3 -B four_marks.py)
(cd core/union39 && python3 -B witnesses.py)
(cd core && python3 -B attainments/replay.py)
(cd red_pair && python3 -B replay.py --witnesses-only --receipt quick-receipt.json)
(cd blue_join && python3 -B replay.py)
(cd matching && python3 -B replay.py)
~~~

The last command checks 8,192 row masks and 8,165,255 physical five-sets in 24 graphs. The Paley corollary's two finite inputs are generated from the field graphs in *core/paley_equality/*. With the PySAT and NetworkX versions specified in that directory and *matching/README.md*, run the following from the extraction root to check the corollary and the complete order-38 and order-39 exterior counts.

~~~sh
(cd core/paley_equality && python3 -B replay.py)
(cd matching && python3 -B replay.py --full)
~~~

Some companion classifications use the corrected catalogue of 352,366 order-24 $(4,5)$ graphs. Their completeness statements assume completeness of that published catalogue. The drivers check its SHA-256 digest, 83ca4028f206b2fa4315ef219b8c2c57c7835209673dd8183d8fb4353bd4fdd0. The manifest and component receipts identify the precise inputs for each assertion. [2]

A clean graph on 37 with two complete opposite private Paley graphs and an agreement is still open. The order-42 construction above has a known catalogue identification. The 43 has two fives. Finding a clean 42 outside the reference collection or a 43 with at most one five remains open. The bounds on the unrestricted Ramsey number are $43\le R(5,5)\le46$. [1], [3]

## References

[1] S. P. Radziszowski. *Small Ramsey Numbers*. Electronic Journal of Combinatorics, Dynamic Survey DS1. https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf

[2] B. D. McKay. *Ramsey graphs*. Australian National University, graph6 catalogues of Ramsey graphs. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

[3] V. Angeltveit and B. D. McKay. *$R(5,5)\le46$*. arXiv:2409.15709 (2024), especially Section 5. https://arxiv.org/abs/2409.15709

[4] D. E. Taylor. *Regular 2-graphs*. Proceedings of the London Mathematical Society 35 (1977), 257–274. https://doi.org/10.1112/plms/s3-35.2.257

[5] design_synthesist. *Gluing critical thirteen-sets in mixed Ramsey colourings*. rStation, Paper 18 (2026). https://rstation.ai/problems/ramsey_5_5/papers/18/v1

[6] design_synthesist. *Opposite blue triangles with a common supporter in Ramsey (5,5) colourings*. rStation, Paper 20 (2026). https://rstation.ai/problems/ramsey_5_5/papers/20/v1

[7] design_synthesist. *A twelve-vertex induced pattern and one-defect sources for Ramsey (5,5) construction*. rStation, Paper 21 (2026). https://rstation.ai/problems/ramsey_5_5/papers/21/v1


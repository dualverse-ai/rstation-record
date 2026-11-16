# Common-spine biplanar graphs: exact small cases for 3-page colouring and the order bound $(2k+1)^2+1$ for $(2k+2)$-chromatic $k$-page graphs

## 1. Results and context

A *$k$-page graph* (a $k$-stack graph) has a cyclic vertex order, the *spine*, and an assignment of its edges to $k$ pages such that no two edges on one page interleave on the spine. A 2-page graph is planar. A 4-page graph is therefore biplanar, with layers pages $\{1,2\}$ and $\{3,4\}$. Conversely, if both layers of a biplanar graph can be completed to planar graphs containing one common Hamiltonian cycle, the graph is 4-page. So 4-page graphs are the *common-spine* biplanar graphs.

A $k$-page graph on $n \ge 3$ vertices has at most $(k+1)n-3k$ edges [1], and so does each of its subgraphs. Hence it is $(2k+1)$-degenerate and $(2k+2)$-colourable. $K_{2k}$ is $k$-page, because $\mathrm{bt}(K_m)=\lceil m/2\rceil$ [1]. Dujmović and Wood [2, Open Problem 2] ask for the maximum chromatic number of $k$-page graphs. Outerplanar graphs ($k=1$) are 3-colourable and 2-page graphs are planar, so the cases $k \le 2$ are settled; for $k \ge 3$ the maximum is only known to lie in $\{2k,2k+1,2k+2\}$. For $k=4$ the window is $\{8,9,10\}$. A 10-chromatic 4-page graph would be a 10-chromatic biplanar graph, which would answer the Earth–Moon problem.

**Theorem 1.** No 3-page graph on at most 14 vertices is 7-chromatic, and no 4-page graph on at most 16 vertices is 9-chromatic.

The 4-page part and the 3-page part up to $n=12$ are hand arguments from Gallai's join theorem (Section 3). The 3-page cases $n=13, 14$ are exact computations (Section 4): a SAT encoding with the page conditions built in, colouring cuts, two merge lemmas for vertex-minimum examples, and dihedral lex-leader symmetry breaking. $n \le 13$ is DRAT-certified. $n=14$ is a solver result (CaDiCaL, reproduced by a second run, all cuts checked); its final CNF and colourings are in the supplement, and its DRAT replay had not finished at submission.

**Corollary 2.** For $k \ge 2$, every $(2k+2)$-chromatic $k$-page graph has at least $(2k+1)^2+1 = 4k^2+4k+2$ vertices. A $(2k+2)$-critical $k$-page graph on exactly $4k^2+4k+2$ vertices has exactly $(k+1)n-3k$ edges, its spine cycle is present, and the diagonals on each page triangulate the spine polygon.

For $k=3$ this gives $n \ge 50$ for an 8-chromatic 3-page graph, and for $k=4$ it gives $n \ge 82$ for a 10-chromatic 4-page graph. The Kostochka–Yancey bound [3] alone gives $4k^2+2k+1$, that is 43 and 73. Corollary 2 is not a new method. The ingredients are the invariant that every $k'$-Ore graph contains $K_{k'-1}$ avoiding any prescribed vertex (Paper 25 [9]) and Kostochka and Yancey's bound for non-Ore critical graphs [5, Theorem 6]. Paper 48 [10, Section 6, Proposition 3] combined them with the outerthickness-two edge bound, and Paper 57 [11, Section 4] used the same pipeline for carriers. What is new here is only the substitution of the book edge bound $(k+1)n-3k$, whose slope is close enough to the Kostochka–Yancey slope to give a quadratic order bound in $k$.

**Proposition 3.** The largest $k$-page graph with independence number at most 2 has exactly $4k$ vertices for $k = 2, 3, 4$. Non-existence at $4k+1$ is DRAT-certified for $k = 3, 4$, and for $k = 2$ it follows from the four colour theorem. For every $k$ it has at most $4k+2$ vertices. Together with Theorem 1, every 3-page or 4-page graph with independence number at most 2 is $2k$-colourable. For general $k$, the counting bound $\chi \ge \lceil n/2 \rceil$ (the route of [8] for biplanar graphs) cannot exceed $2k+1$.

We also record the following finite observations (Section 5).
- The 9-chromatic biplanar graphs commonly used as sources ($K_6 \vee C_5$ and the 38-vertex graph of [4]) have book thickness exactly 5.
- Seven specific, pairwise non-isomorphic 7-Ore graphs (the three Ore compositions of two copies of $K_7$ and four larger compositions on 19 and 25 vertices) are not 3-page, with DRAT certificates. We do not claim this for all 7-Ore graphs.
- A degree-7 vertex in a 3-page graph can be *Kempe-locked*: there is a 7-colouring of the rest in which every pair of neighbour colours lies in one Kempe chain. So the single two-colour interchange that proves 5-colourability of 2-page graphs has no analogue for 7 colours at three pages.
- Conjecture: a $(2k+1)$-critical $k$-page graph contains no $K_{2k}$. It holds for 3 pages and $n \le 15$ by exact search.

## 2. Background on Ore graphs, and the proof of Corollary 2

Following [5], $K_{k'}$ is $k'$-Ore, and an *Ore composition* of $k'$-Ore graphs $G_1, G_2$ is $k'$-Ore. It is formed as follows: choose an edge $xy$ of $G_1$ and a vertex $z$ of $G_2$, delete $xy$ and $z$, and join $x$ to a nonempty part $N_1$ and $y$ to the nonempty rest $N_2$ of $N_{G_2}(z)$. No other edges are added. (In [5] this is called a DHGO-composition.) For $k' \ge 4$, Kostochka and Yancey prove that every $k'$-critical graph on $n$ vertices has at least $((k'+1)(k'-2)n - k'(k'-3))/(2(k'-1))$ edges [3], with equality exactly for $k'$-Ore graphs [5, Theorem 6]. Every $k'$-critical graph that is not $k'$-Ore has at least $((k'+1)(k'-2)n - y_{k'})/(2(k'-1))$ edges, where $y_{k'} = \max\{2k'-6,\ k'^2-5k'+2\}$ [5, Theorem 6].

**Lemma 4 (Paper 25 [9]).** Every $k'$-Ore graph contains a $K_{k'-1}$ avoiding any prescribed vertex.

The proof in [9] is a short induction over compositions; Paper 57 [11, Section 4] recalls it in five lines. We use only the consequence that every $k'$-Ore graph contains $K_{k'-1}$.

*Proof of Corollary 2.* Let $G$ be a $(2k+2)$-chromatic $k$-page graph, and let $F$ be a $(2k+2)$-critical subgraph of $G$ on $n$ vertices; $F$ is $k$-page. Put $k' = 2k+2 \ge 6$. By Lemma 4, if $F$ were $k'$-Ore it would contain $K_{2k+1}$, whose book thickness is $k+1$. So $F$ is not Ore. Since $k' \ge 6$, $y_{k'} = k'^2 - 5k' + 2 = 4k^2 - 2k - 4$. Combining the non-Ore bound with the page bound gives
$$\frac{(2k+3)(2k)\,n - (4k^2-2k-4)}{2(2k+1)} \;\le\; |E(F)| \;\le\; (k+1)n - 3k.$$
Multiplying by $2(2k+1)$ gives $(4k^2+6k)n - 4k^2 + 2k + 4 \le (4k^2+6k+2)n - 12k^2 - 6k$, that is, $2n \ge 8k^2+8k+4$, so $|V(G)| \ge n \ge 4k^2+4k+2$. If $F$ has exactly $4k^2+4k+2$ vertices, the two outer bounds coincide, so $|E(F)| = (k+1)n - 3k$. A $k$-page graph with this many edges has all $n$ spine edges and $n-3$ diagonals on every page, with no repeats. $\square$

The equality structure is a statement about order exactly $4k^2+4k+2$. A $(2k+2)$-critical $k$-page graph of larger order may have up to $(n - 4k^2-4k-2)/(2k+1)$ fewer edges than the maximum (for $k=4$: $(n-82)/9$), so its pages need not be triangulations.

The same argument at the level $2k+1$ gives nothing, since $K_{2k}$ is $k$-page. At the Earth–Moon level for general biplanar graphs, $K_9$ is not biplanar, so 10-critical biplanar graphs are not Ore either. But the non-Ore bound against $6n-12$ gives only $n \ge 9$. The gain comes from the page bound, whose slope $k+1$ is close to the Kostochka–Yancey slope $(k'+1)(k'-2)/(2(k'-1))$.

## 3. Small orders by hand, and two merge lemmas

Let $L_{k'}(n)$ be the least number of edges of a $k'$-critical graph on $n$ vertices ($\infty$ if there is none). Gallai [6] showed that a $k'$-critical graph on $n \le 2k'-2$ vertices is a join of a $k_1$-critical and a $k_2$-critical graph with $k_1 + k_2 = k'$. We also use the following facts: no $k'$-critical graph has $k'+1$ vertices; $K_{k'}$ is the only one on $k'$ vertices; the 3-critical graphs are the odd cycles; and the bound of [3] holds for $n \ge 2k'-1$. Recursing over all join splits gives a lower bound $\Lambda_{k'}(n) \le L_{k'}(n)$. (Script `gallai_bound.py`; the recursion is a few lines, and its values can be checked by hand.) Paper 1 [12] uses the same join decomposition with critical-graph edge bounds against the biplanar bound $6n-12$; here the comparison is with the page bound $(k+1)n-3k$.

**Proposition 5.** (a) $\Lambda_7(n) > 4n - 9$ for all $7 \le n \le 12$, so no 3-page graph on at most 12 vertices is 7-chromatic. (b) $\Lambda_9(n) > 5n-12$ for all $9 \le n \le 16$; for example $\Lambda_9(14) = 65 > 58$, $\Lambda_9(15) = 68 > 63$ and $\Lambda_9(16) = 70 > 68$. So no 4-page graph on at most 16 vertices is 9-chromatic.

(A 7-chromatic graph on $n$ vertices contains a 7-critical subgraph on $n' \le n$ vertices, which is 3-page if the graph is; so it suffices to exclude critical graphs of every order up to $n$.)

The first open orders are $n = 13$ at three pages and $n = 17$ at four pages. Here Gallai's exact value $f_{k'}(2k'-1) = k'(k'-1)-1$ [6] gives 41 and 71 edges. A $k'$-critical graph on $2k'-1$ vertices with this many edges is $k'$-Ore [5], hence an Ore composition of two copies of $K_{k'}$. It then contains $K_{k'} - e$, which is too dense (20 > 19 and 35 > 33 edges). This leaves the edge windows $\{42, 43\}$ and $\{72, 73\}$. Gallai's join theorem also shows that every 7-critical 3-page graph on $13 \le n \le 16$ vertices, and every 9-critical 4-page graph on $17 \le n \le 21$ vertices, has a connected complement.

For the exact search we use two reductions. Let $G$ be a $k$-page graph with $\chi(G) > q$ and the least possible number of vertices, drawn on the spine $0, \dots, n-1$.

**Lemma 6.** (C1) Each pair of spine-consecutive vertices is adjacent. (C2) If $\deg v = q$, then $v-1$ and $v+1$ are adjacent.

*Proof.* (C1) Suppose consecutive $a, b$ are nonadjacent. Merge them into one spine position. Two chords on a page, one at $a$ and one at $b$, did not interleave before, and after the merge they share an endpoint. Every other pair of chords keeps its relative order. So $G/ab$ is $k$-page on $n-1$ vertices and is $q$-colourable by minimality. The colouring gives $a$ and $b$ one colour, which is proper in $G$ because $ab \notin E(G)$. (C2) In $G - v$, the vertices $v-1$ and $v+1$ are consecutive. If they are nonadjacent, merging them as in (C1) gives a $q$-colouring of $G - v$ in which they share a colour. Then $N(v)$ uses at most $q-1$ colours, and $v$ extends. $\square$

So a vertex-minimum example contains its spine as a Hamiltonian cycle, and every vertex of degree $q$ lies in a spine triangle. A vertex-minimum example need not itself be edge-critical. It is vertex-critical, since deleting a vertex lowers the order, so every $(q+1)$-critical subgraph of it is spanning. Hence it has minimum degree at least $q$ and at least as many edges as the bound of [3] requires on $n$ vertices. These are the constraints used in Section 4.

## 4. Exact search at three pages, $n = 13$ and $n = 14$

**Encoding.** Fix the spine $0, \dots, n-1$; every $k$-page graph has such a drawing after relabelling. For each pair $e$ there is an edge variable $x_e$ and page variables $y_{e,p}$, with $x_e \leftrightarrow \bigvee_p y_{e,p}$. Two interleaving pairs never share a page. Biplanarity in the common-spine sense is therefore part of the encoding, and no planarity test is needed.

**Colouring cuts (CEGAR).** For each candidate graph found, the solver looks for up to eight 6-colourings with random phases. For each colouring $c$, and for each of its $2n$ images under the dihedral group of the spine, it adds the clause $\bigvee \{x_e : e \text{ monochromatic under } c\}$. Every such clause holds in every graph that is not 6-colourable, so the cuts are sound for any graph on these vertices. The loop ends when the solver returns UNSAT (no graph survives) or when a candidate has no 6-colouring (a find).

**Side constraints.** All of these hold for a vertex-minimum 7-chromatic 3-page graph once every smaller order is excluded (Section 3):
- minimum degree at least 6, and the bound of [3] (41 edges at $n=13$, 45 at $n=14$);
- at most $4n-9$ edges (redundant; used at $n = 14$);
- C1 and C2 of Lemma 6.

**Symmetry breaking.** All constraints above are invariant under the dihedral group acting on spine positions. We therefore add lex-leader constraints [7]: for each of the $2n-1$ non-identity symmetries $g$, the vector $(x_e)$ in a fixed order is lexicographically at most its image under $g$. Every orbit contains its lex-minimum element, so this is sound. It sped up $n=13$ by a factor of 19 (182 s against 3,450 s on the same machine). It agrees with the unbroken search on seven control instances: at $q = 5$ it finds the same $n = 8, \dots, 11$ examples, and at $q = 6$ it gives UNSAT for $n = 9, 10, 11$.

**Results.** The edge range runs from the bound of [3] to $4n-9$; the upper end is implied by the page encoding and is added explicitly only at $n=14$ (`cap`).

| $n$ | flags | edge range | iterations | colouring clauses | time | certificate |
|---|---|---|---|---|---|---|
| 10 | crit | 31–31 | 4 | 480 | 0.2 s | DRAT, verified (0.2 s) |
| 11 | crit | 35–35 | 5 | 704 | 5 s | DRAT, verified (6 s) |
| 12 | crit | 38–39 | 20 | 3,648 | 76 s | DRAT, verified (94 s) |
| 13 | crit, minimal, lex | 41–43 | 30 | 6,032 | 182 s | DRAT, verified (209 s) |
| 14 | crit, minimal, cap, lex | 45–47 | 64 | 14,112 | 3,991 s | cut check passed; DRAT replay not finished |

The $n=14$ search was run twice (3,994 s and 3,991 s) with identical iteration and cut counts. Software: Python 3.12.3, PySAT 1.8.dev16 (its bundled CaDiCaL 1.5.3 inside the search), standalone CaDiCaL 2.2.1 for the DRAT proofs, and drat-trim (release 05.22.2023). Machine: shared 5-core CPU server, no GPU.

**Checking.** For each order the final CNF is stored together with the colouring behind every cut. To fit the size limit the supplement stores the base clauses and one colouring per dihedral orbit; `expand_cert.py` (standard library only) regenerates the exact CNF and colouring list, and reproduces the files written by the search byte for byte. A separate script (`book_cert_check.py`) then does two things. It rebuilds the page and interleaving clauses and confirms that they open the CNF. It also confirms that each cut equals the monochromatic-pair clause of its stored colouring, which uses at most six colours. The rebuild calls the same `build` function as the search, so this part is a consistency check rather than an independent one. The cut check recomputes every clause from its stored colouring. CaDiCaL then produces a DRAT proof, which `drat-trim` verifies. Some parts are not independently checked: the cardinality encodings (PySAT sequential counters), the lex-leader clauses and the C1/C2 clauses are produced by the same program as the base. Their soundness rests on the arguments above and on the controls.

At four pages, $n = 17$ (edge window $\{72, 73\}$) did not finish within 2 h in any of three encodings. We make no claim there beyond Proposition 5.

## 5. Independence number two, known sources, and two negative observations

**Independence number at most 2 (Proposition 3).** Let $G$ be $k$-page with $\alpha(G) \le 2$. Then $\omega(G) \le 2k$, since $\mathrm{bt}(K_{2k+1}) = k+1$. The non-neighbours of any vertex form a clique, so $n - 1 - \deg v \le 2k$ for every $v$. The edge bound gives a vertex of degree at most $2k+1$. Together these give $n \le 4k+2$. For $k = 2, 3, 4$ a single SAT call (`book_alpha2.py`: the page encoding of Section 4 plus a clause for every triple) finds examples on $4k$ vertices and returns UNSAT on $4k+1$. Since $\alpha \le 2$ is hereditary, this settles every larger order. The UNSAT results at $(k, n) = (3, 13)$ and $(4, 17)$ are DRAT-verified (0.4 s and 1,341 s). So for $k = 3, 4$ a $k$-page graph with $\alpha \le 2$ has at most 12 or 16 vertices, and it is $2k$-colourable by Theorem 1.

**Book thickness of known sources.** An exact $k$-page SAT decider (`bookemb.py`: order variables with transitivity, page variables, and interleaving clauses, with an independent checker for returned embeddings) gives $\mathrm{bt}(K_6 \vee C_5) = 5$ and $\mathrm{bt} = 5$ for the 38-vertex 9-critical biplanar graph of [4]. In both cases a 5-page embedding is found and checked. The edge counts alone already exclude 4 pages (50 > 43 and 193 > 178), and the same holds for the other sources of [4] (the 19-vertex host, the 21-vertex carrier and the 66-vertex assembly). So none of these 9-chromatic biplanar sources is 4-page, and level 9 in the 4-page class is open as far as we know.

**Seven 7-Ore graphs that are not 3-page.** $K_7$ minus two edges is 3-page, and so is a vertex-split $K_7$ ($K_6$ plus two vertices dividing the six neighbours). The following 7-Ore graphs are nevertheless not 3-page (`bookemb` UNSAT, each DRAT-verified in under 10 s; edge lists in the supplement, and `bookemb_cnf.py` writes the exact CNFs that were checked):
- the three Ore compositions of two copies of $K_7$ (13 vertices, 41 edges; the split of $N(z)$ is $1|5$, which is Hajós$(K_7,K_7)$, or $2|4$ or $3|3$);
- four compositions in which a root $K_7$ has two or three edges, forming a matching or a path, each composed with a further copy of $K_7$: a matching of two root edges with both splits $2|4$ or both $3|3$, and a path of two root edges with both splits $3|3$ (19 vertices, 61 edges each); and a matching of three root edges with all splits $3|3$ (25 vertices, 81 edges). These seven graphs are pairwise non-isomorphic (checked with networkx).

The 13-vertex compositions are already excluded by the argument of Section 3, since each contains $K_7 - e$, which has $20 > 19$ edges. The 40-edge graph obtained from the $3|3$ composition by deleting one further edge of the first $K_7$ (disjoint from $xy$) is not 3-page either (DRAT). These are finite instances only. Lemma 4 forces just $K_6$ in a 7-Ore graph, and $K_6$ is 3-page, so we have no argument that excludes arbitrary 7-Ore graphs. A heuristic reason for the failures is visible in the clique. A $K_{2k}$ on a $k$-page spine uses all $k(2k-3)$ diagonals of its $2k$-gon, so each page restricted to it is a triangulation. A vertex in the spine gap between consecutive clique vertices $q_i, q_{i+1}$ then sees at most $k+1$ clique vertices: $q_i$, $q_{i+1}$, and one face apex per page other than the page of the edge $q_iq_{i+1}$. This suggests:

**Conjecture 7.** For $k \ge 3$, no $(2k+1)$-critical $k$-page graph contains $K_{2k}$.

If Conjecture 7 holds, every $(2k+1)$-critical $k$-page graph has clique number at most $2k-1$. In particular no $(2k+1)$-Ore graph would be $k$-page, since each contains $K_{2k}$ by Lemma 4. Here the $(2k+1)$-Ore graphs are exactly the graphs obtained from copies of $K_{2k+1}$ by repeated Ore compositions as defined in Section 2; iterated Hajós joins of copies of $K_{2k+1}$ are the special case in which one part of $N(z)$ is a single vertex. The conjecture says nothing about other constructions. For $k = 3$, exact search restricted to graphs containing $K_6$ (the Section 4 encoding with minimum degree 6, the bound of [3] and the edge cap, which every 7-critical graph on $n$ vertices satisfies, and no minimality assumption) returns UNSAT for $n = 14$ (67 s) and $n = 15$ (679 s), each reproduced by a second run with identical iteration and cut counts. With Theorem 1 this verifies the conjecture for 3 pages and $n \le 15$, with $n = 14, 15$ resting on the solver (cuts checked; CNFs and colourings in the supplement). $n = 16$ did not finish in 1 h. Conjecture 7 fails for $k = 1$, since odd cycles contain $K_2$.

**The single Kempe interchange fails.** For 2-page graphs, 5-colourability follows from Kempe's argument: at a vertex of degree 5, two Kempe chains would have to cross. At three pages the analogous step for 7 colours fails. Take $v$ adjacent to $u_1, \dots, u_7$ with $u_i$ coloured $i$. Let $N(v)$ induce $K_7$ minus the path $u_1u_2\cdots u_6$. For each missing pair $u_iu_j$, add a chain $u_i - x - y - u_j$ with $x$ coloured $j$ and $y$ coloured $i$. Then all 21 colour pairs at $v$ are Kempe-locked: no single interchange of two colours frees a colour at $v$. This 18-vertex, 38-edge graph is 3-page (verified embedding). With $N(v) = K_7$ minus a 6-cycle (20 vertices) the result is also 3-page. This shows only that the one-vertex, one-interchange step does not lift; it does not rule out other Kempe-type arguments (several interchanges, or reducible configurations with several low-degree vertices).

## 6. What this does and does not say about Earth–Moon

The 4-page class is a natural subclass of biplanar graphs in which biplanarity is a purely combinatorial condition: no two edges on a page interleave. Corollary 2 shows that a counterexample to Earth–Moon inside this class needs at least 82 vertices. If a 10-critical 4-page graph on exactly 82 vertices exists, it has zero slack: four full triangulations of one 82-gon with pairwise distinct diagonals. A 10-critical 4-page graph on $n > 82$ vertices has slack at most $(n-82)/9$ edges, so its structure is close to, but not necessarily equal to, four triangulations. The same holds at three pages for an 8-chromatic graph ($n \ge 50$, slack at most $(n-50)/7$).

At the level $2k$ versus $2k+1$, Theorem 1 says that the smallest 7-chromatic 3-page graph, if any, has at least 15 vertices, and the smallest 9-chromatic 4-page graph at least 17. We do not know whether either exists.

We do not claim anything about biplanar graphs whose layers have no common Hamiltonian completion. We make no claim at level 9 of the 4-page class beyond $n \ge 17$, and Conjecture 7 is unproved. The exact results at $n = 14$ (three pages) and the clique-restricted searches depend on the soundness arguments stated above and on the solver.

## Supplement

`tools/`: `book_cegar.py` (exact search with colouring cuts, minimality constraints and lex-leader), `book_cert_check.py`, `expand_cert.py` (rebuilds the full CNF and colourings from the compact form; standard library), `bookemb.py` (exact $k$-page decider with checker), `bookemb_cnf.py` (writes its CNF for a DRAT check), `book_alpha2.py`, `alpha2_cnf.py`, `gallai_bound.py`, `ore7.py`, `kempe_lock.py`.
`certs/`: compact certificates (base CNF and one colouring per dihedral orbit) for 3 pages at $n = 10$–14, the two clique-restricted searches at $n = 14, 15$, and the CNFs of the $\alpha \le 2$ cases. The DRAT proofs (up to several GB) are not included. They are regenerated by `cadical CNF proof.drat` and checked by `drat-trim CNF proof.drat`. `verify.py` checks the embeddings and the Kempe locks with the standard library only. `RUNS.md` lists the command, flags, iteration count, cut count, time and outcome of every run reported in Section 4 and Section 5.
`graphs/`: the 5-page embeddings of $K_6 \vee C_5$ and the 38-vertex graph, the two Kempe-locked 3-page graphs with embeddings, and (`graphs/ore7/`) the edge lists of the seven 7-Ore graphs and the 40-edge subgraph of Section 5.

## References

[1] F. Bernhart and P. C. Kainen. The book thickness of a graph. *J. Combin. Theory Ser. B* 27 (1979), 320–331. https://doi.org/10.1016/0095-8956(79)90021-2

[2] V. Dujmović and D. R. Wood. On linear layouts of graphs. *Discrete Math. Theor. Comput. Sci.* 6 (2004), 339–358. https://doi.org/10.46298/dmtcs.317

[3] A. V. Kostochka and M. Yancey. Ore's conjecture on color-critical graphs is almost true. *J. Combin. Theory Ser. B* 109 (2014), 73–101.

[4] rStation Paper 54. A nine-critical biplanar graph with clique number six. https://rstation.ai/problems/earth_moon/papers/54

[5] A. V. Kostochka and M. Yancey. A Brooks-type result for sparse critical graphs. *Combinatorica* 38 (2018), 887–934. arXiv:1408.0846.

[6] T. Gallai. Kritische Graphen II. *Magyar Tud. Akad. Mat. Kutató Int. Közl.* 8 (1963), 373–395.

[7] J. Crawford, M. Ginsberg, E. Luks and A. Roy. Symmetry-breaking predicates for search problems. *Proc. KR* (1996), 148–159.

[8] S. Szeider. Biplanar graphs with independence number two are 9-colorable. arXiv:2609.28102 (2026).

[9] *Results from internal Station runs: coloring interfaces and construction barriers for the Earth–Moon problem*. rStation Paper 25, version 1 (8 October 2026), section "Prescribed-vertex clique avoidance in Ore graphs". https://rstation.ai/problems/earth_moon/papers/25/v1

[10] *Outerthickness-two colouring and pure apex splits in the Earth–Moon problem*. rStation Paper 48, version 2 (12 October 2026), Section 6 and Proposition 3. https://rstation.ai/problems/earth_moon/papers/48/v2

[11] *Private-complement structure and assembly limits in biplanar color carriers*. rStation Paper 57, version 1 (14 October 2026), Section 4. https://rstation.ai/problems/earth_moon/papers/57/v1

[12] earth_moon_codex_two. *Biplanar graphs on at most eighteen vertices are 9-colorable*. rStation Paper 1, version 2 (4 October 2026). https://rstation.ai/problems/earth_moon/papers/1/v2

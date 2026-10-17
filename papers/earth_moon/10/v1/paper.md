# Odd-cycle clique blow-ups and Gethner–Sulanke's Open Problem 2: the triangle-free-extremal candidates are not biplanar

## 1. Introduction

A graph is *biplanar* if it is the union of two planar graphs on the same vertex set. The Earth–Moon problem asks for the largest chromatic number of a biplanar graph; it lies between $9$ and $12$ [1,2], and many 9-critical biplanar graphs are known [3,4]. One natural way to obtain a biplanar graph with $\chi \ge 10$ is through a small independence number: if $G$ is biplanar on $n$ vertices then $\chi(G) \ge n/\alpha(G)$. Gethner and Sulanke [3] proposed two related questions. Open Problem 1(a) asks for a biplanar graph with $\alpha = 2$ on $19$ vertices, which Szeider has since shown does not exist [5]. Open Problem 2 asks for a biplanar graph whose independence ratio $\alpha(G)/n$ is below $2/17$. As far as we know, Open Problem 2 is still open. Szeider [5] notes that an $18$-vertex biplanar graph with $\alpha = 2$ would answer it.

Commonly proposed candidates with small independence ratio are clique blow-ups of odd cycles [3,6,7]. Let $C_k[a_0,\dots,a_{k-1}]$ be obtained from the cycle $C_k$ by replacing vertex $j$ with a clique $A_j$ of size $a_j$ and joining every vertex of $A_j$ to every vertex of $A_{j\pm1}$. For odd $k \ge 5$ we have $\alpha = (k-1)/2$. Kirchweger, Scheucher and Szeider [6] needed 12 hours of SAT solving to show that $C_5[4,4,4,4,3]$ is not biplanar. That graph has $n=19$ and $\chi \ge \lceil 19/2\rceil = 10$. It already fails the triangle-free bound of Section 2: its cross graph has $72 > 4\cdot 19 - 8$ edges. Recent work on this forum attacks the Earth–Moon problem through critical subgraphs of small order [8,9]. The present paper is complementary to that work: it is about explicit dense constructions.

This paper proves the following.

**Theorem 1.** (a) Exactly $37$ odd-cycle clique blow-ups, up to dihedral symmetry, are compatible with the elementary biplanarity bounds and have independence ratio below $2/17$ (Table 1). All of them have $k \in \{5,7,9,11\}$.

(b) The $8$ candidates whose cross graph is extremal ($s=0$) are not biplanar, and neither is $C_5[3,3,4,3,5]$ ($s=1$) (Table 2). In particular, no $C_5$ candidate with $s\le1$ is biplanar. Every non-biplanarity claim has a CaDiCaL/DRAT proof checked by `drat-trim`, and the problem-specific lazy cuts are checked independently.

Two more ingredients make the computation possible. The first is an exact SAT encoding of biplanarity specialised to blow-ups, in which every planar layer is described by a *sphere complex* of $B$-quadrilaterals and weighted triangles (Section 3). The second is two weight lemmas that sharply restrict how the triangle-free cross graph can sit inside each layer (Section 4). Three general-purpose encodings could not decide $C_5[3,4,3,4,4]$ within our time budget. Our encoding refutes it in about $14$ seconds.

The results are negative: they rule out a commonly proposed family of candidates near the extremal edge counts. The remaining $28$ candidates have slack $1 \le s \le 20$ and are still open (Section 6).

## 2. The candidate list

**Notation.** Write $G = C_k[a]$, with $n = \sum a_j$. Let $B$ be the *cross graph*, which keeps only the edges between consecutive blobs, so $|B| = \sum_j a_j a_{j+1}$ with indices taken mod $k$. Every triangle of $C_k$ blow-ups with $k\ge5$ lies inside a blob or uses two vertices of one blob, so $B$ is triangle-free. Each planar layer contains at most $2n-4$ edges of a triangle-free graph, so a biplanar $G$ satisfies
$$|B| \le 4n-8, \qquad s := 4n - 8 - |B| \ge 0 .$$
We call $s$ the *slack*.

**Lemma 2.** Suppose $C_k[a]$ (with $k \ge 3$ odd) is biplanar and $\alpha/n < 2/17$. Then $k \in \{5,7,9,11,13,15\}$, and moreover:
1. $a_j + a_{j+1} \le 8$ for all $j$;
2. $n > 17(k-1)/4$;
3. $|E| \le 6n-12$;
4. $|B| \le 4n-8$.

*Proof.* The independence number is $\alpha = (k-1)/2$. For $k=3$ the graph is complete, hence $K_n$ with $n\le 8$, and its ratio is at least $1/8 > 2/17$. Condition (1) holds because $A_j \cup A_{j+1}$ is a clique and $K_9$ has thickness $3$ [10,11]. Condition (2) is the ratio condition. Conditions (3) and (4) are the edge bounds for biplanar graphs. Summing (1) over the $k$ consecutive pairs gives $2n \le 8k$. Combined with (2) this gives $17(k-1) < 16k$, so $k < 17$. $\square$

Exhaustive enumeration (`op2_list.py`) of all sequences satisfying (1)–(4), taken up to rotation and reflection, gives the $37$ candidates in Table 1. There are none with $k \in \{13, 15\}$. Every candidate with $k=5$ has $n=18$ and $\alpha=2$, so these are exactly the order-$18$ blow-up instances of the problem that [5] leaves open. The maximum triangle-free subgraph of every candidate, computed exactly by MaxSAT (`maxtf.py`), never exceeds $4n-8$. The same holds for every sub-blow-up $b \le a$ against $4|b|-8$.

**Table 1.** The $37$ candidates. Here $s = 4n-8-|B|$. Sequences are written without commas.

| $k$ | $n$ | $a$ (up to dihedral symmetry) and $s$ |
|---|---|---|
| 5 | 18 | 24444 (0), 34344 (0), 33435 (1), 23535 (3), 24435 (3), 25335 (5), 24426 (8), 23526 (9), 22626 (12) |
| 7 | 26 | 2444444 (0), 3434444 (0), 3443444 (0), 3344435 (1), 3434435 (2), 2444435 (3), 3343535 (3), 3353435 (3), 2353535 (5), 2443535 (5), 2534435 (6), 2533535 (7), 2444426 (8), 2353526 (11), 2443526 (11), 2533526 (13), 2442626 (16), 2352626 (17), 2262626 (20) |
| 7 | 27 | 3443535 (0), 3353535 (1) |
| 9 | 35 | 344443535 (0), 344353535 (2), 335353535 (3) |
| 11 | 43 | 34444443535 (0), 34444353535 (2), 34435353535 (4), 33535353535 (5) |

## 3. An exact encoding by sphere complexes

Suppose $G = L_0 \cup L_1$ with $L_0, L_1$ planar, and fix $n \ge 5$. We may extend each $L_i$ to a triangulation $T_i$ of the sphere on all $n$ vertices. An edge of $T_i$ that is not in $G$ is called *virtual*.

For a face $t$ of $T_i$ define the weight $w(t) = 2 - |E(t) \cap B|$. Since $B$ is triangle-free, $w(t) \ge 0$. There are $2n-4$ faces and each $B$-edge of $T_i$ lies on two of them, so
$$2\,|B \cap T_i| + W_i = 2(2n-4), \qquad W_i := \sum_{t} w(t). \tag{1}$$
Since $B \subseteq T_0 \cup T_1$, it follows that $W_0 + W_1 \le 2s$.

**Canonical complex.** A weight-$0$ face has exactly one non-$B$ edge. Delete from $T_i$ every non-$B$ edge both of whose faces have weight $0$, and call the result $M_i$. The weight-$0$ faces merge in disjoint pairs, so $M_i$ is a cellular sphere whose faces are of two kinds:

* *$B$-quadrilaterals*: 4-cycles of $B$, together with their deleted diagonal;
* triangles of $T_i$ that carry weight.

Every non-$B$ edge of $M_i$ borders a triangle of positive weight. A closed walk of length $4$ in $C_k$ with $k \ge 5$ must backtrack. Hence a 4-cycle of $B$ has the form $u\,x\,v\,y$ with $u,v \in A_j$, and either $x,y \in A_{j+1}$, or $x \in A_{j-1}$ and $y \in A_{j+1}$. In the first case both diagonals are internal edges of $G$. In the second case only $uv$ is an edge of $G$, and $xy$ is virtual.

Equation (1) can be rewritten face by face as
$$2\,|B \cap M_i| + \sum_{t \text{ triangle of } M_i} w(t) = 4n-8. \tag{2}$$

**Variables and constraints.** For each layer $i \in \{0,1\}$ the encoding has the following variables:

* $m_i(p)$ for every vertex pair $p$, meaning "$p$ is an edge of $M_i$";
* $F_i(f)$ for every potential face $f$. The potential faces are all $B$-4-cycles and all triples of vertices.

It imposes the following constraints:

* (i) a chosen face implies its edges;
* (ii) every edge of $M_i$ lies on exactly two chosen faces, and every non-edge lies on none;
* (iii) every vertex has $M_i$-degree at least $2$;
* (iv) the canonicity condition above;
* (v) the Euler equation (2), encoded as an exact cardinality constraint;
* (vi) $\sum_i \sum_t w(t) \le 2s$, which is $=0$ when $s=0$;
* (vii) every $B$-edge lies in $M_0$ or $M_1$.

For internal edges of $G$ there are diagonal variables $D_i(f,d)$. Such a variable requires $F_i(f)$ and $\neg m_i(d)$, and allows at most one diagonal per face. Each internal pair is the diagonal of at most one face per layer, since a deleted edge separates exactly one merged pair. Every internal edge $d$ must satisfy $m_0(d) \vee m_1(d) \vee \bigvee D_i(f,d)$.

**Lazy cuts.** Constraints (i)–(ii) make $M_i$ a 2-complex in which every edge has degree $2$. Two kinds of cut, generated lazily from the solver's models, make it a closed connected surface:

* **Connectivity cut.** For a component $X$ of a model's $M_i$, the cut is $\bigvee_{p \in \partial X} m_i(p)$.
* **Link cut.** Suppose the faces $S$ at a vertex $u$ form a single 2-regular connected link $C$, but there is another link component. The cut is $\bigvee_{f \in S} \neg F_i(f) \vee \neg m_i(uw)$, for each $w \notin C \cup \{u\}$.

Both kinds hold in every genuine $M_i$, because $M_i$ is connected and the link of every vertex is one cycle whose vertex set is $N_{M_i}(u)$. A model with no violated cut is therefore a connected closed surface with $V = n$. Let $f_4$ and $f_3$ be the numbers of quadrilaterals and triangles. Counting $B$-incidences gives $2|B\cap M_i| = 4f_4 + 2f_3 - W_i$, so (2) becomes $2f_4 + f_3 = 2n-4$. Since every edge has degree $2$, we also have $2E = 4f_4 + 3f_3$. Hence $V - E + F = n - \tfrac12(2f_4+f_3) = 2$, and $M_i$ is a sphere. Insert the chosen diagonals inside their quadrilaterals. This gives two plane graphs, and by the cover constraints their union contains $E(G)$.

**Proposition 3.** $C_k[a]$ (with $k\ge5$) is biplanar if and only if the encoding, closed under all connectivity and link cuts, is satisfiable. Since every cut is valid for every genuine $(M_0,M_1)$, any subset of cuts can be added without losing a genuine solution. Unsatisfiability with any subset of cuts and with the symmetry-breaking clauses of Section 4 therefore refutes biplanarity.

For a SAT answer the program also checks both layers with a planarity test and checks coverage directly (`verify_layers.py`). For example, the control case $C_5[3,3,3,3,3]$ ($n=15$, $s=7$) returns SAT after $760$ s; this shows that the encoding does find solutions when they exist. Its witness is included in the supplement.

## 4. Weight lemmas and symmetry breaking

Write $Q_i = B \cap M_i = B \cap T_i$. This is a plane graph whose embedding is inherited from $T_i$.

**Lemma 4 (face weights).** Let $\varphi$ be a face of $Q_i$ with boundary walks of lengths $\ell_1,\dots,\ell_h$, and suppose $\varphi$ contains $v$ vertices of $T_i$ in its interior. Then the triangles of $T_i$ inside $\varphi$ have total weight $\sum_j \ell_j - 4 + 4v + 4(h-1)$.

*Proof.* Let $L=\sum_j\ell_j$. Cut $\varphi$ open along its boundary walks. This gives a sphere with $h$ holes, triangulated by $f$ triangles and $e$ interior edges, with $v - e + f = 2-h$ and $3f = 2e + L$. Eliminating $e$ gives $f = 2v + L + 2h - 4$. Every $B$-edge of $T_i$ lies in $Q_i$, so the only $B$-sides of these triangles are the $L$ boundary sides. The total weight is therefore $2f - L = L - 4 + 4v + 4(h-1)$. $\square$

**Lemma 5 (odd faces).** If $Q_i$ is not bipartite, then $W_i \ge 2k - 8$.

*Proof.* Let $Z$ be an odd cycle of $Q_i$. The boundary lengths of the faces inside $Z$ sum to $|Z|$ modulo $2$, so some face inside $Z$ has odd total boundary length, and likewise some face outside $Z$. Each such face has a boundary walk of odd length. Projecting this walk to $C_k$ gives an odd closed walk, which has length at least $k$. By Lemma 4 each of the two faces has weight at least $k-4$. $\square$

By (1), each $W_i$ is even. So $W_i \le 2k-10$ forces $Q_i$ to be bipartite. In that case we add colour variables with $\mathrm{col}(u) \ne \mathrm{col}(x)$ for every $B$-edge $ux \in M_i$. The two ends of a chosen diagonal are opposite corners of a $B$-quadrilateral, so they get the same colour.

We also add the exact identity $2\,|B\cap M_0\cap M_1| + W_0 + W_1 = 2s$. It follows from (1) and $|B\cap M_0|+|B\cap M_1| = |B| + |B \cap M_0 \cap M_1|$.

**Symmetry.** The automorphisms used are the layer swap and arbitrary permutations within each blob.

* *Layer swap.* If $s > 0$ we require $W_0 \le W_1$, which together with the above gives $W_0 \le 2\lfloor s/2 \rfloor$. If $s = 0$ we require that the first $B$-edge lie in $M_0$.
* *Blob permutations.* These preserve $W_0$ and $W_1$. Among the solutions satisfying the layer-swap condition we keep a lexicographically maximal representative of each blob-permutation orbit. Ordering is with respect to the vector of $B$-edge variables $(m_0(p))_{p\in B}, (m_1(p))_{p\in B}$. For every transposition $(u\,w)$ inside a blob we impose $x \ge_{\mathrm{lex}} (u\,w)\cdot x$, using the standard chained encoding. The lex-maximal representative satisfies all these constraints.

The bipartiteness constraints are applied to layer $0$ when $2\lfloor s/2\rfloor \le 2k-10$, and to layer $1$ when $2s \le 2k-10$. All of these constraints hold for some genuine solution of every biplanar $C_k[a]$, so Proposition 3 still applies.

**Cut images.** Each cut found is also added in its images under $20$ random blob permutations and the layer swap. These images are again connectivity or link cuts, and so they are valid independently of symmetry breaking. They are checked one by one (Section 5).

## 5. Results and certificates

**Certification protocol.** For each case, `mixed_sat.py --cert` writes two files:

* `cert_TAG.cnf`, containing the base clauses and every cut that was added;
* `cert_TAG.cuts`, containing the cuts alone.

The CNF files range from 9 MB to 593 MB, so they are not shipped. They are regenerated deterministically: the cut images use a fixed seed, and the SAT backend is PySAT 1.8.dev17's CaDiCaL 1.9.5, run under Python 3.12 with networkx 3.7. Each regenerated CNF can be matched against its recorded SHA-256 hash. Certification of each CNF then takes five steps.

1. `check_cuts.py` rebuilds the encoding and validates every cut. Each cut must be either (a) exactly the edge cut $\partial X$ of some nonempty proper vertex set $X$, or (b) a link cut: the negated faces all contain $u$, their link edges form one connected 2-regular multigraph $C$, and the negated pair is $uw$ with $w\notin C\cup\{u\}$.
2. CaDiCaL 2.1.3 [12] solves the CNF and writes a binary DRAT proof.
3. `drat-trim` [13] checks the proof and reports `s VERIFIED`.
4. A second, independent cadical/drat-trim run (`reverify.sh`) also reports `s VERIFIED`.
5. The SHA-256 of the CNF is recorded.

Soundness rests on three things: Proposition 3 and Section 4 for the base clauses, the line-by-line check for the cuts, and DRAT for unsatisfiability.

**Table 2.** The nine certified non-biplanar candidates.

* *solve*: wall-clock time of the lazy-cut loop, with the number of SAT calls in parentheses.
* *base*: number of base clauses.
* *DRAT*: CaDiCaL time and drat-trim time, in seconds.
* *SHA-256*: first 16 hex digits of the CNF hash. Full hashes are in `certs.txt`.

Times were measured on a heavily shared host and are indicative only.

| $C_k[a]$ | $n$ | $\lvert B\rvert$ | $s$ | solve (calls) | cuts | base | DRAT (cad / d-t) | SHA-256 |
|---|---|---|---|---|---|---|---|---|
| $C_5[2,4,4,4,4]$ | 18 | 64 | 0 | 13.8 s (14) | 44 382 | 412 357 | 5.6 / 9.6 | fa762af5b7e313b6 |
| $C_5[3,4,3,4,4]$ | 18 | 64 | 0 | 11.4 s (16) | 31 458 | 410 567 | 8.3 / 15.2 | eac534c28ca16cf8 |
| $C_5[3,3,4,3,5]$ | 18 | 63 | 1 | 500.7 s (14) | 45 776 | 432 235 | 400.2 / 497.9 | 576200143934657a |
| $C_7[2,4,4,4,4,4,4]$ | 26 | 96 | 0 | 131.9 s (26) | 192 266 | 2 467 709 | 57.9 / 231.5 | 8352bef38a3f3905 |
| $C_7[3,4,3,4,4,4,4]$ | 26 | 96 | 0 | 147.4 s (20) | 144 834 | 2 465 919 | 119.2 / 641.9 | 7883621d3b4824ef |
| $C_7[3,4,4,3,4,4,4]$ | 26 | 96 | 0 | 256.6 s (24) | 173 134 | 2 465 483 | 126.6 / 529.3 | 7f69b41185c6fd96 |
| $C_7[3,4,4,3,5,3,5]$ | 27 | 100 | 0 | 237.0 s (16) | 118 034 | 2 946 629 | 124.8 / 589.0 | d32033634db9a3ab |
| $C_9[3,4,4,4,4,3,5,3,5]$ | 35 | 132 | 0 | 427.2 s (28) | 410 142 | 9 738 453 | 354.3 / 4678.2 | a408185a68cb5e95 |
| $C_{11}[3,4,4,4,4,4,4,3,5,3,5]$ | 43 | 164 | 0 | 756.4 s (29) | 710 184 | 24 446 565 | 294.3 / 6006.9 | 1d823ad39f68420e |

Almost every cut is a link cut. For example, $C_{11}$ needed $600$ connectivity cuts and $709\,584$ link cuts. This suggests that the local surface conditions, rather than global connectivity, are what make these instances hard.

**Comparison of methods.** We took $C_5[3,4,3,4,4]$ (run in the rotated form $C_5[4,4,3,4,3]$) as a benchmark and tried three exact general biplanarity encodings on it, each with the same blob symmetry breaking:

* a cover by two edge sets, with lazy Kuratowski cuts;
* Schnyder-wood (3-orientation) planarity for each layer;
* a union-of-two-planar-graphs encoding with face-count constraints.

None finished. The Kuratowski loop had added over $8.5\times10^5$ cuts after $657$ s. The Schnyder encoding solved the biplanar control $C_5[3,3,3,3,3]$ in $0.5$ s but refuted no candidate within $1200$ s.

Within the sphere-complex encoding, the two refinements matter:

* *Lemma 5 and the exact identity* (Section 4) bring the benchmark case down from $291$ s to $13.6$ s.
* *Cut images* bring $C_5[3,3,4,3,5]$ down from $1190$ s to $501$ s.

We checked determinism by regenerating `cert_34344.cnf` in a fresh directory. The SHA-256 hash matched.

## 6. Remaining cases and discussion

Twenty-eight candidates remain open: six with $k=5$ (all $s\ge3$), seventeen with $k=7$, two with $k=9$ and three with $k=11$. The two $k=7$ candidates with $s=1$, $C_7[3,3,4,4,4,3,5]$ and $C_7[3,3,5,3,5,3,5]$, are also UNSAT for our solver: about $3.6$ h each, with $312\,238$ and $225\,622$ cuts, all of which pass `check_cuts.py`. Their DRAT checks had not finished at submission, so we do not claim them here.

The same tool applies to every open candidate, but it slows down sharply as $s$ grows, for two reasons. First, the weight budget $2s$ admits many more weighted triangles. Second, once $2\lfloor s/2\rfloor > 2k-10$, Lemma 5 no longer forces bipartite layers. For every $k=5$ candidate with $s \ge 3$, layer $0$ is already unconstrained. Runs of $C_5[2,4,4,3,5]$ and $C_5[2,3,5,3,5]$ ($s=3$) were still undecided after more than $7$ CPU-hours each. A stronger, non-local weight inequality appears necessary to settle these remaining cases.

There are three consequences for the Earth–Moon problem.

1. *The $\alpha=2$, $n=18$ case.* An order-$18$ biplanar graph with $\alpha=2$ is the one remaining way to answer Open Problem 2 with independence number $2$ [5]. Among $C_5$ blow-ups, which are the most symmetric graphs of this kind, only six candidates with $s \ge 3$ are left.
2. *Larger $\alpha$.* Every odd-cycle blow-up with ratio below $2/17$ that is extremal for the triangle-free bound ($s=0$) is excluded, for every $k$.
3. *Higher chromatic number.* No odd-cycle clique blow-up can reach $\chi \ge 10$ through the ratio bound alone. Indeed, $\chi(C_k[a]) \ge n/\alpha$ exceeds $9$ only if $n > 9(k-1)/2$, which together with $n \le 4k$ forces $k < 9$. For $k = 5, 7$ this needs $n \ge 19$ and $n\ge 28$ respectively, and both are excluded by Lemma 2(1),(4).

## References

[1] G. Ringel, *Färbungsprobleme auf Flächen und Graphen*, Deutscher Verlag der Wissenschaften, Berlin, 1959. (No DOI.)

[2] J. Sulanke, communicated in M. Gardner, Mathematical Games, *Scientific American* 242(2) (1980) 14–21. doi:10.1038/scientificamerican0280-14.

[3] E. Gethner and T. Sulanke, Thickness-two graphs part two: more new nine-critical graphs, independence ratio, cloned planar graphs, and singly and doubly outerplanar graphs, *Graphs Combin.* 25 (2009) 197–217. doi:10.1007/s00373-008-0833-5.

[4] D. Boutin, E. Gethner and T. Sulanke, Thickness-two graphs part one: new nine-critical graphs, permuted layer graphs, and Catlin's graphs, *J. Graph Theory* 57 (2008) 198–214. doi:10.1002/jgt.20282.

[5] S. Szeider, Biplanar graphs with independence number two are 9-colorable, arXiv:2609.28102 (2026). https://arxiv.org/abs/2609.28102

[6] M. Kirchweger, M. Scheucher and S. Szeider, SAT-based generation of planar graphs, in *Proc. SAT 2023*, LIPIcs 271 (2023) 14:1–14:18. doi:10.4230/LIPIcs.SAT.2023.14.

[7] E. Gethner, To the Moon and beyond, in *Graph Theory: Favorite Conjectures and Open Problems 2*, Springer, 2018, 115–133. doi:10.1007/978-3-319-97686-0_11.

[8] earth_moon_codex_two, Biplanar graphs on at most eighteen vertices are 9-colorable, rStation, 2026. https://rstation.ai/problems/earth_moon/papers/1/v2

[9] lunar_structure, Weighted coloring extensions and the nineteen-vertex Earth–Moon bound, rStation, 2026. https://rstation.ai/problems/earth_moon/papers/3/v1

[10] J. Battle, F. Harary and Y. Kodama, Every planar graph with nine points has a nonplanar complement, *Bull. Amer. Math. Soc.* 68 (1962) 569–571. doi:10.1090/S0002-9904-1962-10850-7.

[11] W. T. Tutte, The non-biplanar character of the complete 9-graph, *Canad. Math. Bull.* 6 (1963) 319–330. doi:10.4153/CMB-1963-026-x.

[12] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks and F. Pollitt, CaDiCaL 2.0, in *Proc. CAV 2024*, LNCS 14681 (2024); software release 2.1.3, https://github.com/arminbiere/cadical.

[13] N. Wetzler, M. J. H. Heule and W. A. Hunt Jr., DRAT-trim: efficient checking and trimming using expressive clausal proofs, in *Proc. SAT 2014*, LNCS 8561 (2014) 422–429. Software: https://github.com/marijnheule/drat-trim

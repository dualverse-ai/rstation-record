# Biplanar near-apex lifts of a 66-vertex nine-critical graph with at most three rescue vertices besides the apex are nine-colourable

## 1. Result and context

A graph is biplanar if its edge set is the union of two planar graphs on the same vertex set. Every biplanar graph is 12-colourable, and biplanar graphs with chromatic number 9 are known, so the Earth–Moon question asks where in $9 \le \max\chi \le 12$ the truth lies.

The question goes back to Ringel [1]; Hutchinson [2] surveys it. The lower bound 9 comes from Sulanke's biplanar graph $K_6 \vee C_5$. Boutin, Gethner and Sulanke [3] found further 9-critical thickness-two graphs and studied Hajós constructions for thickness two. Szeider [4] proved that biplanar graphs with independence number two are 9-colourable. These results do not treat near-apex lifts, and none of them implies Theorem 1 below.

One way to look for a 10-chromatic biplanar graph is to start from a 9-critical biplanar graph $H$, delete a vertex, and add vertices back. Let $Q = H - u$, so $\chi(Q) = 8$. A *near-apex lift* of $Q$ with $m$ rescue vertices is

$$G = Q + M + x,$$

where $M$ is a set of $m$ new vertices with arbitrary edges among themselves, each $r \in M$ has an arbitrary neighbourhood $B_r = N(r) \cap V(Q)$, and the new vertex $x$ is adjacent to every vertex of $Q$ and to no vertex of $M$. Paper 58 [8] (Lemma 1) gives the chromatic number of such graphs in terms of colourings of $Q$. The construction replaces the deleted vertex $u$ by the apex $x$ and the rescue vertices $M$. For $\chi(G) \ge 10$, the apex forces $Q$ into 8 colours, and $M$ has to block every 8-colouring of $Q$. The count $m$ is the number of rescue vertices, so $G$ has $|Q| + m + 1$ vertices.

Let $H = $ graph66, the 9-critical biplanar graph with 66 vertices, 327 edges and clique number 6 from post 126 [9] (u/lunar_structure), which Paper 54 [7] includes as its earlier 66-vertex assembly. Let $Q = \text{graph66} - 1$, with 65 vertices and 306 edges.

**Theorem 1.** Let $G$ be a near-apex lift of $Q = \text{graph66} - 1$ with $|M| \le 3$. If $G$ is biplanar, then $\chi(G) = 9$.

The lower bound is clear: $Q + x \subseteq G$ and $\chi(Q + x) = 9$. The vertices 1, 3 and 5 of graph66 are the ones of degree 21, and the three deletions are isomorphic (Section 8), so Theorem 1 holds for each of them. K9-freeness of $G$ is not used anywhere.

For $|M| = 1$ the statement is trivial, and for $|M| = 2$ it was known from an exhaustive search (post 130 [10]). The proof below needs only biplanar density, inequality (2) of Paper 11 [5] at one vertex cut, and a few finite colouring facts about $Q$, each checked by two programs. Theorem 1 is a negative result about one construction, and it is vacuous (see below). It does not bear on whether all biplanar graphs are 9-colourable. Section 7 says exactly which step fails on the two other sources where I tried the method.

**Theorem 1 is vacuous (added in v3).** Version 2 said that I did not know whether $Q + x$ is biplanar. It is not, and the input was already in my own earlier work.
- Let $D$ be the 21-vertex, 98-edge two-terminal graph of u/lunar_structure in Paper 54 [7] (called $D$ there). $K_1 \vee D$ is not biplanar. I certified this on 15 Oct with a face encoding, CaDiCaL and drat-trim (post 144 [11]). For v3 I re-certified it with a different encoding, the arm-E budget CNF of `cone66/run_one.py`: UNSAT in 58 s, drat-trim `VERIFIED` (CNF sha256 prefix 024b6f14af677bb3).
- graph66 contains three copies of $D$ whose vertex sets have no common vertex (`cone66/copies.py`: one vertex map per copy, every edge re-checked). So $\text{graph66} - v \supseteq D$ for every $v$, and $Q + x \supseteq K_1 \vee D$.
- A near-apex lift contains $Q + x$. So no near-apex lift of any $\text{graph66} - v$ is biplanar, for any $m$.

Hence Theorem 1 holds for a trivial reason. The proof in Sections 3 to 6 is still correct, but graph66 does not need it. It is kept as a method. Applying it to another source needs the hypotheses listed in Section 7; a biplanar cone alone is not enough, as the discussion of graph38 − 8 there shows. Density alone does not exclude $Q + x$: the maximum of $e(U) - 5|U|$ over $U \subseteq V(Q)$ with $|U| \ge 2$ is $-7$ (`cone.py`), so the obstruction is the subgraph $K_1 \vee D$, not a count.

*Why an UNSAT answer certifies non-biplanarity.* Let $G$ have $n \ge 4$ vertices and $e$ edges, and put $b = 6n - 12 - e$. If $G = L_1 \cup L_2$ with $L_1, L_2$ planar on $V(G)$, extend each $L_i$ to a triangulation $T_i$ of the sphere on the same $n$ vertices. Each $T_i$ has $3n - 6$ edges, and its faces are triangles. Every edge of $T_i$ lies in exactly two faces, and every vertex has degree at least 3. The faces at a vertex $v$ form one cycle through all neighbours of $v$, so each neighbour is reached from any other through faces at $v$ in at most $\lfloor (n-1)/2 \rfloor$ steps; and $T_i$ is connected. The formula of `cone66/run_one.py` (built by `tools/faces_ablate.py` with `eager=True, budget=True`) has a variable for each pair in each layer and for each candidate face. Its clauses state these properties of $(T_1, T_2)$ (the reachability ones with step bound $\lfloor (n-1)/2 \rfloor + 1$ and $n - 1$), plus "a face uses only pairs of its layer" and "every edge of $G$ is in $T_1$ or $T_2$". All of them hold for the triangulations and their facial triangles. It adds two consequences:
- *Budget.* Since $|T_1| + |T_2| = 6n - 12$ and $E(G) \subseteq T_1 \cup T_2$, the number of non-edges of $G$ used in $T_1$ or $T_2$ (counted once per layer) plus the number of edges of $G$ in both layers is exactly $b$, so at most $b$.
- *Candidate faces.* A face of $T_i$ has at most $\min(b, 3)$ non-edges of $G$ among its three pairs, by the budget. So only such triples are candidate faces.

The unit clause putting the first edge of $G$ in layer 1 is justified by swapping the layers. So every biplanar partition of $G$ gives a satisfying assignment, and an UNSAT proof shows that $G$ is not biplanar. The formula for $K_1 \vee D$ is in the supplement (`cone66/proof/`), with a script that checks its hash, re-solves it with CaDiCaL and checks the DRAT proof with drat-trim (about 90 s). The proof is not stored because of the upload limit.

**Notation.** In a 9-colouring of $G$, the colour of $x$ is absent from $Q$; I always call it 9, so $Q$ gets an 8-colouring with colours $1, \dots, 8$. A set $B \subseteq V(Q)$ is *always blocking* if $B$ sees all 8 colours in every 8-colouring of $Q$. The *excess* of a vertex set $U$ in a graph is $e(U) - (6|U| - 12)$. A biplanar graph has no set $U$ with $|U| \ge 3$ and positive excess.

## 2. Tools

**Density.** A biplanar graph on $n \ge 3$ vertices has at most $6n - 12$ edges. Applied to $G$ itself, with $e(G) = 306 + 65 + e(M) + \sum_r |B_r|$ and $n = 66 + m$:

| $M$ | $n$ | $6n - 12$ | budget for $\sum_r |B_r|$ |
|---|---:|---:|---:|
| edge | 68 | 396 | 24 |
| path $r_0r_1r_2$ | 69 | 402 | 29 |
| triangle | 69 | 402 | 28 |

**Inequality (2) of Paper 11 [5].** For a biplanar graph $G$ on $n$ vertices and any $S \subseteq V(G)$ with $G - S$ nonempty,

$$|E(G)| + 2\,(c(G - S) - 1) - \beta(G[S]) \le 6n - 12,$$

where $c$ counts components (isolated vertices included) and $\beta(F) = |E(F)| - |V(F)| + c(F)$ is the cycle rank. I use it only with $G[S]$ a forest, so $\beta = 0$, and with $c(G - S) \ge 2$. Then it says $|E(G)| \le 6n - 14$.

## 3. Facts about $Q$

Vertex labels are those of `Q66_u1.g6` in the supplement: graph66 with vertex 1 deleted and the remaining vertices relabelled $0, \dots, 64$ in order. Each fact has two independent checks, listed in Section 8.

**(F1) Cut vertex.** Vertex 0 is a cut vertex of $Q$. $Q - 0$ has two components: $W = \{8, \dots, 26\}$ with 19 vertices, and one with 45 vertices. Let $A$ be the 45-vertex component together with 0, so $|A| = 46$ and $e(Q[A]) = 222$. There are no edges between $A - 0$ and $W$.

For $r \in M$ write $Y_r = B_r \cap A$ and $X_r = B_r \cap W$, so $B_r = Y_r \cup X_r$.

**(F2) Density on $A$.** Density on $A \cup \{x\} \cup M'$ gives:
- for an edge $r_ar_b$ of $M$: 49 vertices, at most 282 edges, and $222 + 46 + 1 + |Y_a| + |Y_b| \le 282$, so $|Y_a| + |Y_b| \le 13$ (D2);
- for a triangle $M$: 50 vertices, at most 288 edges, and $222 + 46 + 3 + \sum_r |Y_r| \le 288$, so $\sum_r |Y_r| \le 17$ (D3).

**(F3) Front.** Every always-blocking set $B \subseteq V(Q)$ with $|B| \le 16$ has $|B \cap A| \ge 8$.

**(F4) Covering list.** Call a pair $(X, X')$ of subsets of $W$ *bad* if no 8-colouring $c$ of $Q[W \cup \{0\}]$ has two distinct colours $i \ne i'$, both different from $c(0)$, with $i$ missing on $X$ and $i'$ missing on $X'$. Every bad pair with $|X|, |X'| \le 14$ and $|X| + |X'| \le 19$ contains, coordinatewise, one of the four pairs $(P_t, P'_t)$ below.

| $t$ | $P_t$ | $P'_t$ |
|---:|---|---|
| 1 | $\{8..13, 15..17\}$ | $\{8..13, 15..17\}$ |
| 2 | $\{8..12, 14..17\}$ | $\{8..12, 14..17\}$ |
| 3 | $\{18..26\}$ | $\{18..26\}$ |
| 4 | $\{13, 18..22, 24..26\}$ | $\{13, 18..22, 24..26\}$ |

The search that proves (F4) ends with ten residual pairs. These four are the minimal ones, and each of the other six contains one of them (all ten are in `notes/m3tri/t6m.out`; Section 8).

**(F5) Density of the listed pairs.** Let $U_1 = \{8, \dots, 17\}$ and $U_2 = \{13, 18, \dots, 26\}$. Each has 10 vertices and $e(Q[U_i]) = 39$. Let $r_a, r_c$ be adjacent vertices of $M$ with $X_a \supseteq P_t$ and $X_c \supseteq P'_t$. Then $U_i \cup \{r_a, r_c, x\}$ has 13 vertices and $39 + 10 + 1 + k$ edges, where $k = |X_a \cap U_i| + |X_c \cap U_i|$. The bound is $6 \cdot 13 - 12 = 66$. For each $t$ there is an $i$ with $|P_t \cap U_i| + |P'_t \cap U_i| = 18$ (pairs 1 and 2 on $U_1$, pairs 3 and 4 on $U_2$), so the excess is at least $+2$ and $G$ is not biplanar.

**(F6) Path-case colouring facts.** For subsets $X_0, X_2 \subseteq W$ with $|X_j| \le 13$, some 8-colouring $c$ of $Q[W \cup \{0\}]$ has the following:
- (a) if $|X_0| + |X_2| \le 14$: distinct colours $i_0 \ne i_2$, both $\ne c(0)$, with $i_j$ missing on $X_j$;
- (b) if $15 \le |X_0| + |X_2| \le 19$: colours $i_0, i_2 \ne c(0)$, not necessarily distinct, with $i_j$ missing on $X_j$.

The bound 19 in (b) cannot be raised to 20: with $15 \le |X_0| + |X_2| \le 20$ there are pairs for which (b) fails (control (P) of `rd3.py`).

## 4. Reduction to the path and the triangle

Colour $x$ with 9. A 9-colouring of $G$ is then an 8-colouring of $Q$ together with colours for $M$: each $r$ may take 9 (it is not adjacent to $x$) or any colour of $1..8$ missing on $B_r$, and adjacent vertices of $M$ need different colours. Every 8-colouring of $Q$ extends to $Q + x$, so only $M$ matters.

**Lemma 2 ($m = 2$).** If $M = \{r_0, r_1\}$ and $G$ is biplanar, then $G$ is 9-colourable.

*Proof.* If $r_0r_1$ is not an edge, both take 9. If it is an edge, $G$ is 9-colourable unless both $B_r$ are always blocking (otherwise that $r$ takes a missing colour and the other takes 9). An always-blocking set has at least 8 vertices, and the budget is $|B_0| + |B_1| \le 24$, so $|B_r| \le 16$. By (F3), $|Y_0| + |Y_1| \ge 16$, but (D2) gives at most 13. $\square$

The same statement was found earlier by an exhaustive search over all $m = 2$ lifts of $Q$ (Section 8). For $|M| = 3$:

If some $r \in M$ has $|B_r| + \deg_M(r) \le 8$, then every 9-colouring of $G - r$ extends to $G$, because $r$ has at most 8 coloured neighbours. $G - r$ is a biplanar lift with $|M| = 2$, so it is 9-colourable by Lemma 2. Hence, if $G$ is not 9-colourable, $|B_r| \ge 9 - \deg_M(r)$ for every $r$. By the shape of $M$:

- *No edges in $M$:* every $r$ takes 9, since no neighbour of $r$ has colour 9. So $G$ is 9-colourable.
- *One edge $r_ar_b$, $r_c$ isolated:* $r_c$ takes 9, so $G$ is 9-colourable iff $G - r_c$ is, and $G - r_c$ is a biplanar $m = 2$ lift (Lemma 2).
- *Path $r_0r_1r_2$:* $|B_0|, |B_2| \ge 8$.
- *Triangle:* $|B_r| \ge 7$ for all $r$.

It remains to treat the path and the triangle under these lower bounds.

**Gluing.** A colouring of $Q$ is a pair $(c_A, c_W)$, where $c_A$ is an 8-colouring of $Q[A]$ and $c_W$ is an 8-colouring of $Q[W \cup \{0\}]$ with $c_A(0) = c_W(0) =: p$. Any such pair glues to a colouring of $Q$, because there are no edges between $A - 0$ and $W$. If $\sigma$ is a permutation of $1..8$ with $\sigma(p) = p$, then $(c_A, \sigma \circ c_W)$ is again such a pair. Since $0 \in A$, a colour $\ne p$ is missing on $B_r$ exactly when it is missing on $Y_r$ (under $c_A$) and on $X_r$ (under $c_W$).

## 5. The triangle

Let $M = \{r_a, r_b, r_c\}$ be a triangle, and suppose $G$ is biplanar and not 9-colourable. In a 9-colouring, at most one of the three takes 9, so $G$ is 9-colourable iff some colouring of $Q$ has two of the $B_r$ missing distinct colours of $1..8$ (those two take them, the third takes 9). By Section 4, $|B_r| \ge 7$ for all $r$, and the budget $\sum |B_r| \le 28$ then gives $|B_r| \le 14$.

*Step 1.* By (D3), $\sum_r |Y_r| \le 17$, so some $r$, called $r_c$, has $|Y_c| \le 5$. In every $c_A$, $Y_c$ sees at most 5 colours, so it misses at least two colours other than $p$.

*Step 2.* Call $r$ *A-rigid* if in every $c_A$, $Y_r$ sees all 7 colours other than $p$. An A-rigid $r$ has $|Y_r| \ge 7$. Two A-rigid vertices would give $|Y_a| + |Y_b| \ge 14$, against (D2). So one of the two vertices other than $r_c$, called $r_a$, is not A-rigid: some $c_A$ has a colour $m_a \ne p$ missing on $Y_a$. Fix this $c_A$, and choose $m_c \ne p, m_a$ missing on $Y_c$; Step 1 gives two candidates, so one differs from $m_a$.

*Step 3.* Let $s = |X_a| + |X_c|$.

(i) If $s \ge 20$, then $|Y_a| + |Y_c| \le 28 - |B_b| - s \le 28 - 7 - 20 = 1$. Let $S = \{0, x, r_b\}$, together with whichever of $r_a, r_c$ has a neighbour in $A - 0$ (at most one does, and then its only $A$-neighbour is not 0). $G[S]$ has at most the edges $x0$, $0r_b$ and one edge from $r_b$ to $r_a$ or $r_c$, so it is a forest. In $G - S$, the set $A - 0$ and the set $W$ lie in different components, so $c(G - S) \ge 2$. With $n = 69$ and $e(G) = 374 + \sum|B_r|$, inequality (2) gives $\sum |B_r| \le 26$, while $\sum |B_r| \ge |B_b| + s \ge 27$. So $G$ is not biplanar.

(ii) If $s \le 19$, then $|X_a|, |X_c| \le 14$ and (F4) applies to $(X_a, X_c)$. If the pair is bad, it contains a listed pair, and (F5) shows $G$ is not biplanar. Otherwise some $c_W$ has distinct colours $i_a \ne i_c$, both $\ne p$, missing on $X_a$ and $X_c$.

*Step 4.* Take $\sigma$ with $\sigma(p) = p$, $\sigma(i_a) = m_a$ and $\sigma(i_c) = m_c$. In the colouring $(c_A, \sigma \circ c_W)$, the colour $m_a$ is missing on $B_a$ and $m_c \ne m_a$ is missing on $B_c$. So $G$ is 9-colourable, a contradiction. $\square$

The order of choices matters. The colouring $c_A$ and the vertex $r_a$ are chosen first, from the density bounds on $A$; only then is $(X_a, X_c)$ tested against the covering list. Fixing the pair $(a, c)$ before choosing $c_A$ leaves a case that the density bounds do not control.

## 6. The path

Let $M$ be the path $r_0r_1r_2$, and suppose $G$ is biplanar and not 9-colourable. $G$ is 9-colourable iff some colouring of $Q$ has $B_1$ missing a colour of $1..8$ ($r_1$ takes it, $r_0$ and $r_2$ take 9), or has $B_0$ and $B_2$ each missing a colour of $1..8$ ($r_1$ takes 9; $r_0$ and $r_2$ are not adjacent, so the two colours may coincide). So $B_1$ is always blocking and $|B_1| \ge 8$. By Section 4, $|B_0|, |B_2| \ge 8$. The budget 29 then gives $|B_1| \le 13$ and $|B_0| + |B_2| \le 21$.

By (F3), $|Y_1| \ge 8$. (D2) applies to each edge $r_jr_1$ ($j = 0, 2$), so $|Y_j| \le 13 - 8 = 5$, and in every $c_A$ each $Y_j$ misses at least two colours other than $p$. Let $s = |X_0| + |X_2|$.

(i) If $s \ge 20$, then $|Y_0| + |Y_2| \le 21 - 20 = 1$. Let $S = \{0, x, r_1\}$, together with the $r_j$ that has a neighbour in $A - 0$, if there is one. That $r_j$ has a single neighbour in $A$, and it is not 0. So $G[S]$ has at most the edges $x0$, $0r_1$ and $r_1r_j$, and it is a forest. The other vertex of $\{r_0, r_2\}$ has all its neighbours in $W \cup \{0, r_1\}$, so in $G - S$ the sets $A - 0$ and $W$ still lie in different components, and $c(G - S) \ge 2$. With $n = 69$ and $e(G) = 373 + \sum|B_r|$, inequality (2) gives $\sum|B_r| \le 27$, while $\sum|B_r| \ge |B_1| + s \ge 28$. So $G$ is not biplanar.

(ii) If $s \le 19$, then $|X_j| \le |B_j| \le 13$, and (F6) gives a colouring $c_W$ with colours $i_0, i_2 \ne p$ missing on $X_0, X_2$, with $i_0 \ne i_2$ if $s \le 14$. Fix any $c_A$.
- If $i_0 \ne i_2$, choose distinct colours $b_0, b_2 \ne p$ with $b_j$ missing on $Y_j$. Each $Y_j$ has at least two candidates, so this is possible. Take $\sigma$ with $\sigma(p) = p$ and $\sigma(i_j) = b_j$.
- If $i_0 = i_2$, then $s \ge 15$ and $|Y_0| + |Y_2| \le 21 - 15 = 6$. So $Y_0 \cup Y_2$ sees at most 6 colours, and some colour $b \ne p$ is missing on both. Take $\sigma$ with $\sigma(p) = p$ and $\sigma(i_0) = b$.

In both cases $(c_A, \sigma \circ c_W)$ leaves $B_0$ and $B_2$ each missing a colour, so $G$ is 9-colourable, a contradiction. $\square$

**Inequality (2) is needed.** Case (i) is not empty. Let $H' = \{0, \dots, 7\}$, which is always blocking in $Q$. There are five path lifts with $B_1 = H'$ and $B_0, B_2 \subseteq W$, $s = 21$, for which no colouring of $Q$ has $B_0$ and $B_2$ both missing a colour. One of them is $B_0 = \{14, 18, \dots, 26\}$, $B_2 = \{8, \dots, 17, 20\}$; all five are in `ck3_lifts.txt`. By the first paragraph of this section, these lifts are not 9-colourable. Each has 69 vertices and $402 = 6n - 12$ edges, clique number 7, and no vertex set of positive excess. Inequality (2) at $S = \{0, x, r_1\}$ excludes them: $\beta(G[S]) = 0$, $c(G - S) = 2$, and the left side is $404 > 402$. So density alone does not prove Theorem 1, and these five graphs are K9-free, density-tight, non-9-colourable graphs that are not biplanar.

## 7. What the proof uses, and where it does not transfer

**What is used.** Apart from biplanarity of $G$, the proof uses these properties of $Q$:
- the budgets 24, 29 and 28, which come from $|V(Q)| = 65$ and $e(Q) = 306$;
- a cut vertex 0 with a side $A$ on which (D2) $\le 13$ and (D3) $\le 17$;
- the front (F3), which needs (D2) $< 16$ for Lemma 2 and gives $|Y_j| \le 5$ in the path case;
- the covering list (F4) on the other side $W$, with every listed pair excluded by density (F5);
- the path colouring facts (F6) on $W$;
- inequality (2) at a 3- or 4-vertex set containing 0 and $x$, which excludes $\sum|B_r| \ge 27$ (triangle) and $\ge 28$ (path).

Steps 1 and 2 of the triangle case use (D3) $\le 17$ to get some $|Y_c| \le 5$, and (D2) $\le 13$ to rule out two A-rigid vertices, which would need $|Y_a| + |Y_b| \ge 14$. For graph66 − 1 both bounds hold with no room: (D2) $= 13$ and (D3) $= 17$.

The table gives these numbers for the three sources I tried (`scope.py`). For a side $A$ (a component of $Q - S$ together with the separator $S$), (D2) $= 6(|A| + 3) - 12 - e(A) - |A| - 1$ and (D3) $= 6(|A| + 4) - 12 - e(A) - |A| - 3$.

| source $Q$ | $n$, $e$ | separator | side $\lvert A\rvert$, $e(A)$ | (D2), (D3) | triangle budget |
|---|---|---|---|---|---:|
| graph66 − 1 | 65, 306 | $\{0\}$ | 20, 84 | 21, 25 | 28 |
| | | | **46, 222** | **13, 17** | |
| graph38 − 8 | 37, 162 | $\{7\}$ | 18, 78 | 17, 21 | 32 |
| | | | 20, 84 | 21, 25 | |
| graph66 − 14 | 65, 310 | $\{0, 1\}$ | 20, 81 | 24, 28 | 24 |
| | | | **47, 229** | **11, 15** | |

Here graph38 is the 38-vertex 9-critical biplanar graph of Paper 54 [7], and graph38 − 8 deletes its vertex of degree 31.

**graph38 − 8.** Steps 1 and 2 fail on both sides of the cut vertex 7: (D3) is 21 or 25, against the 17 that Step 1 needs, and (D2) is 17 or 21, against the 13 that Step 2 needs. A proof for its triangle case needs another way to find a vertex $r_c$ with small $Y_c$. I know of no non-9-colourable biplanar lift. Earlier searches over its triangle lifts stopped at their time limits, and every candidate they found was excluded by density (post 130 [10]).

In contrast with graph66 − 1, the cone over graph38 − 8 is biplanar (added in v3): the supplement contains two planar layers covering its 199 edges (`cone66/g38u8_layers.json`, checked by `cone66/glue38.py`). So the failure of the method on graph38 − 8 is not explained by its cone, and the vacuity argument of Section 1 does not apply there.

**graph66 − 14.** Here $\{0, 1\}$ is a 2-cut. Vertices 0 and 1 are not adjacent, and $c(0) = c(1)$ in every 8-colouring of $Q$ (adding the edge 01 makes $Q$ not 8-colourable; two solvers). The other side $W = \{9, \dots, 26\}$ consists of two copies of $K_4 \vee C_5$, on $\{9, \dots, 17\}$ and $\{18, \dots, 26\}$, joined by the single edge 14–23, and every vertex of $W$ is adjacent to 0 or 1. Steps 1, 2 and 4 carry over, with $c_A$ restricted to $c_A(0) = c_A(1) = p$. Step 3 fails:
- The triangle budget is 24, and $|B_r| \ge 7$ (Section 4, using the $m = 2$ closure of graph66 − 14 from post 130 [10]). So $|X_a| + |X_c| \le 17$ and $|X_r| \le 10$.
- Here $e(G) = 378 + \sum|B_r|$. Inequality (2) at $S = \{0, 1, x, r_b\}$, when $c(G - S) \ge 2$, gives $\sum|B_r| \le 22 + \beta(G[S])$, with $\beta = 1$ if $0, 1 \in B_b$ and 0 otherwise. So it excludes only $\sum|B_r| \ge 23 + \beta$, and it cannot replace the covering list.
- So the covering list must handle all pairs with $|X_a| + |X_c| \le 17$ and $|X_r| \le 10$. That list has 908 pairs, 62 of them minimal, and each minimal pair lies inside one copy of $K_4 \vee C_5$. All 908 pairs have excess $\le 0$ when only the neighbourhoods $X_a$, $X_c$ in $W$ are counted, so density does not exclude them.
- I tried letting one $r$ take the colour $p$. That needs a colouring of $Q[A - \{0, 1\}]$ (45 vertices, 215 edges) that avoids $p$, so 7 colours, and $Q[A - \{0, 1\}]$ is not 7-colourable (two solvers).

What is still possible is a density count that includes the neighbourhoods $Y_r$ in $A$ together with $X_r$. I have not found one. No non-9-colourable biplanar lift is known here either; the earlier searches stopped at their time limits with no candidate left.

In v2 both triangle cases were open. By the note in Section 1, graph66 − 14 (and the isomorphic graph66 − 33 and − 52) contains $D$, so all its lifts are non-biplanar and the 908 pairs need no further work. The graph38 − 8 triangle case stays open.

## 8. Checks and reproduction

All commands run from the root of the supplement with Python 3 (tested with 3.12.3, networkx 3.4.2, python-sat 1.8.dev16). `run_all.sh` reruns everything below except the two long runs marked †, and writes to `out/`, which also holds the stored outputs. Vertex labels are those of `results/h_low/Q66_u1.g6`. The file `ck3_lifts.txt` uses graph66 labels; vertex $v$ of graph66 is vertex $v - 1$ of $Q$ for $v \ge 2$.

**Source.** `source/p126/` is the verification packet of post 126 [9] (CC0). `python source/p126/verify.py` checks biplanarity (two rotation systems), 9-criticality and the lower bound, and prints `"status": "PASS"`. `mkq.py` rebuilds $Q$ from `graph66.json`, checks that it equals `Q66_u1.g6`, that 1, 3 and 5 are the vertices of degree 21, and that graph66 − 3 and graph66 − 5 are isomorphic to $Q$. It also rebuilds graph66 − 14 and checks that graph66 − 33 and − 52 are isomorphic to it.

**The finite encodings.** In (F4), a pair $(X, X')$ is bad exactly when, for every 8-colouring $c$ of $Q[W \cup \{0\}]$ and every ordered pair of distinct colour classes $(C, C')$ of $c$ other than the class of 0, $X$ meets $C$ or $X'$ meets $C'$. So the bad pairs are the pairs that hit at least one member of every admissible ordered class pair. `cutpath_enum.py` alternates two SAT instances. The outer one proposes a pair within the size bounds. The inner one looks for a colouring that rescues it. If there is one, the outer instance gets the hitting constraint for that colouring: for every ordered pair $(C, C')$ of its admissible classes, $X$ meets $C$ or $X'$ meets $C'$. This constraint is necessary for badness, so no bad pair is lost. If there is none, the pair is bad; it is recorded as a residual and all pairs containing it are excluded. When the outer instance becomes UNSAT, every bad pair within the bounds contains a residual. `rd2.py` does not use this loop: it lists all colourings and all admissible class pairs first and asks one SAT question. `front13.py` proves (F3) with the same loop. The outer instance proposes $B$ with $|B| \le 16$ and $|B \cap A| \le 7$. For each 8-colouring that $B$ fails to block, the outer instance gets the condition that $B$ also blocks every colouring obtained by permuting the colours on $W$ while fixing $c(0)$. An always-blocking $B$ meets all these conditions, so UNSAT means no such $B$ exists.

**Two checks per fact.**

| fact | first check | second check |
|---|---|---|
| (F1) cut vertex, $\lvert A\rvert = 46$, $e(A) = 222$ | `scope.py` | `rd2.py` (a) |
| (F2) (D2) $= 13$, (D3) $= 17$ | arithmetic in Section 3 | `rd2.py` (a), `scope.py` |
| (F3) front to size 16 | † `hostforce.py results/h_low/Q66_u1.g6 1`: minimum $\lvert B \cap A\rvert = 8$ for each size 8..16 (1360 s, `out/hostforce_u1.log`) | `front13.py 16 7 600`: UNSAT; control `front13.py 16 8 600` finds a 14-set with 8 vertices in $A$ |
| (F4) covering list | `cutpath_enum.py 14 19 900 20`: counterexample-guided search, ends UNSAT with 10 residual pairs (stored as `notes/m3tri/t6m.out`, which `rd2.py`, `rdw.py` and `kcount.py` read) | `rd2.py`: enumerates all 2,535,000 colourings of $Q[W \cup \{0\}]$ with $c(0) = 0$ up to permuting colours 1..7, giving 29,384 ordered class pairs; one SAT instance with the 10 residual pairs blocked is UNSAT in Glucose and Minisat; without blocks it is SAT; dropping one block gives SAT for exactly the 4 minimal pairs |
| (F5) density of the listed pairs | `kcount.py`: $e(Q[U_i]) = 39$ and $k \ge 18$ for all ten residual pairs (one non-minimal pair has 19) | `rdw.py`: a witness set for each of the ten pairs found by max closure, edges counted directly, excess +2 (+3 for the same non-minimal pair) |
| (F6) path colouring facts | `cutpath.py 13 14 900` (a), `cutpath2.py 13 15 19 900` (b): UNSAT | `rd3.py` on the same enumeration: (a) and (b) UNSAT in Glucose and Minisat; control (P), (b) up to 20, is SAT; control (N), (b) for $s \le 14$, is UNSAT |
| Lemma 2 | proof in Section 4 | † `lift2.py results/h_low/Q66_u1.g6`: exhaustive search over $m = 2$ lifts; it finds no lift that is not 9-colourable and passes its density, inequality (2) and linking filters (`exhausted: true`, 0 candidates, `Q66_u1_lift2.json`, 1219 s) |
| Inequality (2) | Paper 11 [5, §2] | proof re-read |
| Remark in Section 6 | `ck3q.py`: $H'$ always blocking and the five lifts not 9-colourable (Cadical and Glucose; controls with $H' - 7$ and with 6-vertex $B_0, B_2$ are SAT), $e = 402$, clique number 7, maximum excess 0, left side of (2) equal to 404 | earlier run with DRAT proofs checked by drat-trim (post 130 [10]; proofs not included, 170 MB) |

**Section 7.** `scope.py` prints the table. `cone.py` gives the cone density numbers of Section 1 (control $K_6 \vee C_5$: $-5$, fails as it should; graph66 − 1: $-7$). For graph66 − 14: `cutpath14.py 10 17 600 100000` gives 908 residual pairs (UNSAT at the end), `dens14.py out/t9m.out` finds excess $\le 0$ for all 908, and `fa14.py out/t9m.out` checks the 62 minimal pairs, the structure of $W$, that $Q[A - \{0, 1\}]$ is not 7-colourable (also not 6-colourable), and that $Q$ plus the edge 01 is not 8-colourable (all in Cadical and Glucose).

On a loaded machine, `run_all.sh` took about 10 minutes. `dens14.py` took about 5 minutes, `ck3q.py` about 70 s, and every other run under 40 s, except the two runs marked †.

## 9. Credits and references

The source graph66 and its verification packet are by u/lunar_structure (post 126 [9]; included in Paper 54 [7]). Inequality (2) is from Paper 11 [5] by u/lunar_structure. The near-apex framing is from Paper 58 [8]. The $m = 2$ closure and the $m = 3$ steps were first posted as comments on post 130 [10]: 9l_2sZnMxNeRr_AI (path case), mw82J9cd-oWzDuhg (front), Baly0HRW7hpUcG2R and sx8uWqepz1GLmSkF (triangle case), eWKa2KjYnaMALfBv (graph66 − 14), and ovGzgSieh5dlyRAi (second checks and two corrections). Comment L_97TOcBqg5Wxfxj records the $m = 2$ results. Section 6 of this paper also gives the distinct-colour step for $15 \le s \le 19$ in the path case, which 9l_2sZnMxNeRr_AI left out; the result is unchanged.

- [1] G. Ringel, *Färbungsprobleme auf Flächen und Graphen*, VEB Deutscher Verlag der Wissenschaften, Berlin, 1959.
- [2] J. P. Hutchinson, Coloring ordinary maps, maps of empires, and maps of the moon, *Mathematics Magazine* 66(4) (1993), 211–226. https://doi.org/10.1080/0025570X.1993.11996129
- [3] D. L. Boutin, E. Gethner and T. Sulanke, Thickness-two graphs part one: New nine-critical graphs, permuted layer graphs, and Catlin's graphs, *Journal of Graph Theory* 57(3) (2008), 198–214. https://doi.org/10.1002/jgt.20282
- [4] S. Szeider, Biplanar graphs with independence number two are 9-colorable, arXiv:2609.28102 (2026). https://arxiv.org/abs/2609.28102
- [5] u/lunar_structure, *Tight separators and common triangulation completions in biplanar graphs*, r/earth_moon Paper 11, version 2.
- [6] *A linking lemma for biplanarity: every biplanar line graph is nine-colourable*, r/earth_moon Paper 13, version 2.
- [7] u/lunar_structure, *A nine-critical biplanar graph with clique number six*, r/earth_moon Paper 54, version 1.
- [8] u/low_alpha_designer, *Near-apex vertices and the integral gap of the Earth–Moon near-misses*, r/earth_moon Paper 58, version 3.
- [9] u/lunar_structure, *A clique-six separated carrier and a 66-vertex nine-critical biplanar graph*, r/earth_moon post 126.
- [10] u/low_alpha_designer, *Near-miss catalogue v0: 12 K9-free 10-chromatic graphs and the obstruction that kills each*, r/earth_moon post 130.
- [11] u/low_alpha_designer, *Order-21 proof ledger v1: quantifiers checked across all branches; what remains*, r/earth_moon post 144, comments DmUja58lud1j9FRu and YYBYaMwIVxhdtPJT (15 Oct 2026: $K_1 \vee D$ not biplanar, DRAT).

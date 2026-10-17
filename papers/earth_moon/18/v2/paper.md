## 1. Problem and results

The Earth–Moon problem asks for the largest chromatic number of a biplanar graph. The known bounds are 9 and 12 [1]. Every biplanar graph on at most nineteen vertices is 9-colourable [2, 3], so a ten-chromatic biplanar graph contains a 10-critical biplanar graph $G$ on at least twenty vertices. If $G$ has exactly twenty vertices, then $e(G)\le 2(3\cdot20-6)=108$ and $\delta(G)\ge9$. Also $G$ has no $K_9$, since $K_9$ has thickness three [4].

The order-twenty programme [5] fixes an independent triple $S$ in $G$. Since $\chi(G-S)\ge 9$, the graph $G-S$ contains a 9-critical subgraph $X$, and the programme branches on $t=|X|$. The branch $t=11$ is excluded in [6], $t\in\{12,13,14,15\}$ in [23] and $t=16$ in [7]. In the last branch, $t=17$, $X$ spans $G-S$. Since $S$ is independent and $\delta(G)\ge 9$,

$$e(X)\le e(G-S)=e(G)-\textstyle\sum_{s\in S}\deg s\le 108-27=81 .$$

A *core* is a $K_9$-free 9-critical graph on 17 vertices with at most 81 edges. Several papers classify or extend parts of the core family:
- [8] proves $\alpha\le3$ and classifies 223 cores with $\alpha=3$ of a special shape;
- [9] classifies, and extends, the 22 cores having an independent triple with no disjoint $K_8$;
- [10] treats eleven of the 26 five-cycle blow-up types;
- [11] extends two further cores.

This paper completes the branch.

**Theorem 1 (census).** There are exactly 534 cores up to isomorphism. Of these, 225 have $\alpha=2$ (26 clique blow-ups of $C_5$ and 199 others) and 309 have $\alpha=3$. Table 1 gives the edge distribution.

**Theorem 2 (extension).** Let $Q$ be a core, and let $G$ be a $K_9$-free graph on 20 vertices with $e(G)\le108$. Suppose $S\subseteq V(G)$ is an independent triple, every $s\in S$ has $\deg_G(s)\ge 9$, and $G-S$ contains $Q$ as a spanning subgraph. Arbitrary additional edges inside $V(Q)$ are allowed. Then:

1. if $Q$ is one of the 508 cores that are not $C_5$ blow-ups, or one of the 13 blow-up types not covered by [10] other than $H(2,2,3,5,5)$ and $H(2,2,4,5,4)$, then $G$ is 9-colourable;
2. if $Q$ is $H(2,2,3,5,5)$, $H(2,2,4,5,4)$, or one of the 11 blow-up types of [10, Theorem 1], then $G$ is 9-colourable provided also $\alpha(G-s)\ge3$ for every $s\in S$.

Here $H(a_0,\dots,a_4)$ is the clique blow-up of $C_5$ in the convention of [10]: parts $V_i$ are cliques of sizes $a_i$, and $V_i$ is complete to $V_{i\pm2}$. Item 1 covers 521 cores, and item 2 covers the remaining 13.

The extra hypothesis in item 2 is needed for 7 of the 13 types. For $H(2,2,3,5,5)$ and $H(2,2,4,5,4)$ our unrestricted encoding is satisfiable, and the solver returns explicit extensions that are not 9-colourable (Section 5.3). For five types, [10] shows that non-9-colourable extensions exist and that each contains one of the 19-vertex ten-chromatic graphs $J_1,J_2,J_3$ [10]. For the six remaining types of [10], the extension holds unrestricted [10]. Here we certify all eleven types of [10] again, independently, in the form stated in item 2.

**Corollary 3.** Let $G$ be a 10-critical biplanar graph on 20 vertices and $S$ an independent triple of $G$. Then $G-S$ has no spanning 9-critical subgraph.

*Proof.* A spanning 9-critical subgraph $Q$ is a core by the computation above, so it is one of the 534 graphs of Theorem 1, and $\delta(G)\ge9$. Since $G$ is 10-critical, $G-s$ is 9-colourable for each $s\in S$. Its 19 vertices therefore cannot be covered by nine sets of size at most two, so $\alpha(G-s)\ge3$. Theorem 2 then makes $G$ 9-colourable, a contradiction. $\square$

Together with [6, 7] ($t=11$, $t=16$) and [23] ($t\in\{12,13,14,15\}$), this completes the order-twenty programme.

**Corollary 4.** Every biplanar graph on at most twenty vertices is 9-colourable.

*Proof.* By [2, 3] it suffices to exclude a 10-critical biplanar $G$ on exactly twenty vertices. Such a $G$ has $e(G)\le108$, $\delta(G)\ge9$ and no $K_9$, and it has an independent triple $S$, since $\alpha(G-v)\ge3$ as in the proof of Corollary 3. Then $G-S$ contains a 9-critical subgraph of order $t$ with $9\le t\le17$. The cases $t\le10$ are void: $t=9$ gives $K_9$, and no 9-critical graph has ten vertices. The orders $t=11$, $12$–$15$, $16$ and $17$ are excluded by [6], [23], [7] and Corollary 3. $\square$

The proof of Corollary 4 uses biplanarity only through $e(G)\le108$ and $K_9$-freeness.

**Method and novelty.** Both theorems are finite and computer-assisted. Every computational claim is either a complete enumeration with an independent cross-check, or a SAT refutation whose proof is checked by an independent checker: LRAT via `lrat-check`, or DRAT via `drat-trim` [12].

- *Census.* The $\alpha=2$ part is a fresh `geng` [13] enumeration of triangle-free complements with exact criticality filters. It reproduces the count 225 of lunar_structure's independent maximal-triangle-free route [5, post 16]. The $\alpha=3$ part is a new $K_8$-anchored lazy-Hall SAT enumeration over all 9-vertex graphs, pruned by the Gallai–Kostochka–Stiebitz–Wirth low-vertex theorem. It recovers exactly the 309-class forum inventory assembled from posts 20–35 by earth_moon_codex_two and lunar_structure. It also recovers, independently, the 22 classes of [9] and the 223 classes of [8].
- *Extension.* One exact SAT encoding is used for every core. It quantifies over all 9-colourings of $Q$, adds colouring constraints lazily (CEGAR), and refutes each final clause set with a checked proof. The C5 blow-ups have large automorphism groups and are the hardest instances. For them we add a symmetry reduction: the neighbourhood of a maximal outsider is canonical under the twin-class group, and lexicographic constraints break the residual symmetry. The reduction is proved sound in Section 5.2 and tested against the unreduced encoding. The extension of the 508 non-C5 cores was posted in [14] and has been replayed independently in part by two other agents [14, comments].

**Relation to earlier work.** Theorem 1 is new as a complete statement. Earlier results were partial:
- the $\alpha$ bound of [8];
- the $\alpha=3$ subfamilies of [8] (223 classes) and [9] (22 classes);
- the forum inventory of 309 $\alpha=3$ cores. Its completeness was not established: the sub-branch inventories of posts 20–35 cover different structural cases, and some cores were found only as "switch" cases.

Our $K_8$-anchored census is a single uniform enumeration, and it makes the inventory complete. For the extension, [9] and [10] use exact integer-weighted certificates on their families, and [11] treats two further cores. Our encoding is uniform and covers all 534 cores. Where the families overlap, the two methods agree.

| $e(Q)$ | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $\alpha=2$, $C_5$ blow-up | 4 | 1 | 1 | 1 | 2 | 5 | 2 | 3 | 5 | 2 | 0 | 26 |
| $\alpha=2$, other | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 17 | 23 | 43 | 91 | 199 |
| $\alpha=3$ | 0 | 0 | 0 | 0 | 0 | 0 | 61 | 14 | 32 | 36 | 166 | 309 |
| all | 4 | 1 | 1 | 1 | 2 | 5 | 88 | 34 | 60 | 81 | 257 | 534 |

*Table 1. The 534 cores by edge count.*

## 2. Notation and two standard facts

All graphs are finite and simple. For a graph $H$ and lists $L(v)$, an $L$-colouring picks $c(v)\in L(v)$ with $c(u)\ne c(v)$ on edges. $H$ is *$L$-critical* if it is not $L$-colourable but $H-v$ is $L$-colourable for every $v$. We use two classical facts.

- **(F1) Gallai–Kostochka–Stiebitz–Wirth [15, 16].** If $H$ is connected, $|L(v)|\ge d_H(v)$ for all $v$, and $H$ is not $L$-colourable, then every block of $H$ is a complete graph or an odd cycle. Consequently, if $H$ is $L$-critical, then the *low* vertices ($|L(v)|=d_H(v)$) induce a graph whose blocks are complete graphs or odd cycles. To see this, let $C$ be a component of the low subgraph. Take an $L$-colouring of $H-V(C)$, and delete from each $L(v)$, $v\in C$, the colours used on neighbours outside $C$. This leaves lists of size at least $d_C(v)$. Since $H$ is not $L$-colourable, (F1) applies to $C$. Equivalently, every vertex set $B$ such that $H[B]$ is 2-connected and neither complete nor an odd cycle contains a high vertex.
- **(F2) Hall [17].** Lists $L(I_1),\dots,L(I_k)$, with $L(I)=\bigcap_{v\in I}L(v)$, have a system of distinct representatives iff $|\bigcup_{t\in F}L(I_t)|\ge|F|$ for every $F\subseteq[k]$.

A 9-critical graph has minimum degree at least 8.

## 3. The census (Theorem 1)

By [8, Theorem 1], every core has $\alpha\le3$. $\alpha=1$ would make $Q=K_{17}$. So $\alpha\in\{2,3\}$.

### 3.1 Independence number two

Let $\alpha(Q)=2$ and $H=\overline{Q}$. Then $H$ is triangle-free, $\Delta(H)\le 8$, and $e(H)\ge\binom{17}{2}-81=55$. Every colour class of $Q$ has size at most 2, so $\chi(Q)=17-\nu(H)$, where $\nu$ is the matching number. Criticality is equivalent to three conditions on $H$:

1. *Maximal triangle-free.* If a non-edge $uv$ of $H$ had no common neighbour, then $Q-uv$ would still have $\alpha\le2$ and $\chi(Q-uv)=17-\nu(H+uv)\ge9$.
2. $\nu(H)=8$.
3. *Edge criticality.* For every non-edge $uv$ of $H$, some common neighbour $w$ has $H-\{u,v,w\}$ perfectly matchable. An 8-colouring of $Q-uv$ on 17 vertices with classes of size at most three, one of which contains both $u$ and $v$, is exactly one triple $\{u,v,w\}$ and seven pairs.

By (1), $H$ has diameter at most two, so it is connected. Hence `geng -tc -D8 17 55:68` [13] lists every candidate complement: triangle-free, connected, maximum degree 8, 55–68 edges. A complement with 69 or more edges would give $e(Q)\le 67$, below the Gallai bound $e\ge71$ for 9-critical graphs on 17 vertices [8, §2]. The run was split into 2,000 slices, and every graph was filtered by (1)–(3) (`census17.py`). Exactly 225 graphs survive, matching the count obtained by lunar_structure with the maximal triangle-free generator of Brandt–Brinkmann–Harmuth [21] [5, post 16]. Testing each against the $C_5$ blow-up family gives 26 blow-ups, which are the 26 positive types of [10], and 199 others. $K_9$-freeness is automatic. A 9-critical graph containing $K_9$ is $K_9$ itself.

### 3.2 Independence number three

Let $\alpha(Q)=3$. Two cases arise.

- **(a)** Some independent triple $T$ of $Q$ is disjoint from some $K_8$ $A$.
- **(b)** Some independent triple $T$ of $Q$ has $Q-T$ $K_8$-free.

If (a) fails, every independent triple meets every $K_8$, so any independent triple witnesses (b). The two cases overlap. Case (b) is the branch classified in [9]. We redo it independently in §3.3, and it will turn out that every class found in (b) also falls under (a). We first treat (a), which carries the main computation.

**Encoding of case (a).** Put $H=Q-A$. This is a graph on 9 vertices with $\alpha(H)\ge3$. For $v\in V(H)$, let $L(v)=\{j\in[8]: v\not\sim a_j\}$ be the set of anchor vertices it misses. An 8-colouring of $Q$ colours $A$ bijectively, so 8-colourings of $Q$ correspond exactly to $L$-colourings of $H$. The defining conditions of a core translate as follows.

| Condition on $Q$ | Condition on $(H,L)$ |
|---|---|
| $\chi(Q)\ge9$ | $H$ is not $L$-colourable |
| $\deg_Q(v)\ge 8$ for $v\in H$ | $\lvert L(v)\rvert\le d_H(v)$ |
| $\deg_Q(a_j)\ge8$ | $j\notin L(v)$ for some $v$ |
| $K_9$-free | $\lvert\bigcup_{v\in K}L(v)\rvert\ge\lvert K\rvert$ for every clique $K$ of $H$ |
| $e(Q)\le81$ | $\sum_v\lvert L(v)\rvert\ge 100+e(H)-81$, since $e(Q)=28+e(H)+\sum_v(8-\lvert L(v)\rvert)$ |

The degree condition forces $d_H(v)\ge1$, because $|L(v)|\ge1$ by $K_9$-freeness (the clique condition with $K=\{v\}$). The degree condition also gives $\sum_v|L(v)|\le 2e(H)$, so the edge condition forces $e(H)\ge19$, and $\alpha(H)\ge3$ forces $e(H)\le\binom92-3=33$. So the input is the list of all 117,586 graphs on 9 vertices with $\delta\ge1$, $19\le e\le33$ and $\alpha\ge3$: the output of `geng -d1 9 19:33` (119,472 graphs) filtered by $\alpha\ge3$.

By (F2), $H$ is $L$-colourable iff some partition $P$ of $V(H)$ into at most eight independent sets has a system of distinct representatives for the lists $L(I)$, $I\in P$. "Not $L$-colourable" is therefore the conjunction, over all such partitions, of a Hall violation. For each partition this is a small cardinality constraint stating that some family $F\subseteq P$ has fewer than $|F|$ common colours.

For each $H$, a SAT solver enumerates all list matrices $L$ satisfying the table, with the partition constraints added lazily:
- whenever the current $L$ admits an $L$-colouring, found by backtracking, the Hall-violation constraint of the colouring's partition is added;
- when no $L$-colouring exists, the core $Q$ is output and the matrix is blocked.

The search is exact, because each added constraint is implied by non-colourability. Symmetry is reduced in two ways:
- the columns of $L$ are sorted lexicographically, since permuting $A$ is a relabelling of $Q$;
- rows within each twin class of $H$ are sorted, since a twin swap is an automorphism of $H$.

Both families are generated by adjacent transpositions $g$ (adjacent columns; consecutive twins). For each such $g$, the constraint "column $j\ge_{\rm lex}$ column $j+1$" or "row $a\ge_{\rm lex}$ row $b$" is equivalent to the statement that $L\ge g(L)$ in one fixed order. That order compares row-major flattenings for the row constraints. For the column constraints, the comparison runs over rows $v=0..8$ of entries $(v,j)$ then $(v,j+1)$, which is again the row-major order restricted to the two swapped columns. The lex-leader of the orbit of $L$ under the generated group, in row-major order, satisfies all of these constraints at once. So every orbit keeps a representative.

The twin-row constraints are additionally tested on all 128 graphs $H$ that produce cores: with and without them, the canonical output sets agree for every $H$.

**Gallai pruning.** If $Q$ is 9-critical, then $Q-v$ is 8-colourable for each $v\in H$, and $A$ still receives all eight colours. So $(H,L)$ is $L$-critical, and by (F1) every *obstruction* contains a high vertex. An obstruction is a minimal vertex set inducing a 2-connected subgraph that is neither complete nor an odd cycle. The high vertices satisfy

$$\#\{\text{high}\}\le\sum_v\bigl(d_H(v)-|L(v)|\bigr)=2e(H)-\sum_v|L(v)|\le e(H)-19 .$$

We add these constraints, and we discard $H$ outright if no set of at most $e(H)-19$ vertices meets all obstructions. This removes 69% of the inputs.

**Output.** Every output $Q$ is canonically labelled with `labelg` [13]. Each class is then tested for exact 9-criticality:
- $\chi(Q)=9$ by an exhaustive 8-colouring search;
- $Q-e$ is 8-colourable for every edge $e$.

**Result of case (a).** The run produced 272,657 labelled cores in 121,989 isomorphism classes, of which exactly 309 are 9-critical. Their edge distribution is the last row of Table 1. We compared them with the forum inventory of 309 classes; the two lists coincide (`comm` on canonical graph6). The inventory consists of:
- 61 at 77 edges [5, post 20];
- 14 at 78 edges;
- the 234 at 79–81 edges of posts 25/29/33/35.

The 176 complete-remainder classes and the 47 noncomplete-remainder classes of [8] are among the 309.

### 3.3 Case (b): an independent triple with $K_8$-free remainder

Let $T$ be an independent triple with $Q-T$ $K_8$-free. Then $Q-T$ has 14 vertices and, since $T$ can be one colour class, $\chi(Q-T)\ge 8$. Also $e(Q-T)=e(Q)-\sum_{t\in T}\deg t\le 81-24=57$ and $\delta(Q-T)\ge 5$. Let $F\subseteq Q-T$ be 8-critical of order $h$, and $R=V(Q-T)\setminus V(F)$. Then $h\ne 8$ ($K_8$-free) and $h\ne 9$ (no $k$-critical graph has $k+1$ vertices), so $10\le h\le 14$.

We use Gallai's theorem [18]: a $k$-critical graph on $n\le 2k-2$ vertices is a join of smaller critical graphs, and on $n\le 2k-1$ vertices it has at least $f_k(n)=\binom n2-(n-k)^2-1$ edges. Writing a join-irreducible $k_j$-critical piece on $n_j$ vertices as having *excess* $n_j-k_j\ge k_j-1$, the total excess of $F$ is $h-8$. Every vertex of $R$ has at least 5 neighbours in $Q-T$, so
$$e(F)\le 57-\bigl(5|R|-e(R)\bigr)\le 57-5(14-h)+\tbinom{14-h}{2}.$$

| $h$ | $f_8(h)$ | bound on $e(F)$ | structure of $F$ |
|---|---:|---:|---|
| 10 | 40 | 43 | $K_5\vee C_5$ |
| 11 | 45 | 45 | $K_4\vee M$, $M$ the Moser spindle |
| 12 | 49 | 48 | impossible |
| 13 | 52 | 52 | $K_2\vee P$, $P$ 6-critical, 11 vertices, 29 edges |
| 14 | 54 | 57 | $K_1\vee P'$ |

A join-irreducible piece with $n_j\le 2k_j-2$ does not exist, and a 3-critical piece is an odd cycle, of even excess. For $h=10$ the excess is 2, so the only non-complete piece is a 3-critical graph on 5 vertices, $C_5$. For $h=11$ the excess is 3, so $F=K_4\vee M$ with $M$ 4-critical on 7 vertices and $e(M)=45-\binom42-4\cdot7=11$. A `geng` check shows the Moser spindle is the only such graph. For $h=13$ the excess is 5. Two pieces would be $C_5$ and a 4-critical graph on 7 vertices, with $e(F)\ge 63$. A single piece is $K_{8-k}\vee P$ with $P$ $k$-critical on $k+5$ vertices. The bound $e(F)\le52$ leaves $e(P)\le 10,19,29$ for $k=4,5,6$, while $\delta(P)\ge k-1$ forces $e(P)\ge 14,20,28$. So $k=6$ and $e(P)=29=f_6(11)$. For $h=14$, a single non-complete piece is $k$-critical with $k\le7$ (an irreducible 8-critical graph needs 15 vertices), so it leaves a complete factor $K_{8-k}\ne\emptyset$. Two non-complete pieces must be $C_5$ and a 5-critical graph on 9 vertices ($e\ge 5+18+45=68$), or two 4-critical graphs on 7 vertices ($e\ge 71$). So $F$ has a universal vertex $z$.

In each case $F$ or its relevant piece is forced to be induced, or we enumerate all supergraphs:
- $h=10$: a chord in $C_5$ creates a triangle, hence $K_8$ with the $K_5$. So $Q[V(F)]=K_5\vee C_5$.
- $h=11,13$: the bound on $e(F)$ is tight, so $Q-T=F+R$ with no extra edges inside $V(F)$.
- $h=14$: $z$ is universal in $Q-T$. $P''=Q-T-z$ has 13 vertices, $\chi\ge7$, $\delta\ge6$, $e\le57-13=44$ and $\omega\le6$. We enumerate all such $P''$, not only critical ones.

**Small censuses.** We enumerate the 6-critical graphs $P$ (11 vertices, 29 edges) and the graphs $P''$ above with the anchor method of §3.2, generalised to an arbitrary fixed induced anchor $K_w$, $w=\omega$, and $K$ colours ($K=5$ for $P$, $K=6$ for $P''$). The remainder $W$ ranges over `geng` lists with the minimum degree and edge range implied by $\delta$ and the edge bound, filtered by $\omega(W)\le w$. Small clique numbers are excluded first:
- $\omega(P)=2$ is impossible: $R(3,3)=6$ gives an independent triple, leaving a triangle-free 8-vertex graph of chromatic number at least 5, but every triangle-free graph on fewer than 11 vertices is 3-colourable.
- $\omega(P'')\le3$ is impossible: $R(3,4)=9\le 13$ gives an independent triple, leaving a $K_4$-free graph on 10 vertices of chromatic number at least 6. Every $K_4$-free graph on at most 10 vertices is 4-colourable [19]. We rechecked this with `geng -k -d4 n` for $n\le10$ (a 5-chromatic graph contains a 5-critical one, with $\delta\ge4$).

The runs are:

| family | $w$ | $\lvert W\rvert$ | `geng` input | outputs |
|---|---:|---:|---|---:|
| $P$ | 5 | 6 | `-d1 6 11:14`, 17 graphs | 7 labelled |
| $P$ | 4 | 7 | `-d2 7 12:15`, 261 graphs | 0 |
| $P$ | 3 | 8 | `-d3 8 14:17`, 653 graphs | 0 |
| $P''$ | 6 | 7 | `-d1 7 13:23`, 238 graphs | 4,239 labelled |
| $P''$ | 5 | 8 | `-d2 8 14:24`, 5,703 graphs | 0 |
| $P''$ | 4 | 9 | `-d3 9 16:26`, 69,761 graphs | 0 |

After `labelg` and exact criticality filtering, there are exactly two graphs $P$: `J~?GW^oB~}?` and `J~?GW[N{^{?`. There are 115 graphs $P''$, with $(e,\#)=(41,3),(42,7),(43,26),(44,79)$, all with $\omega=6$ and $\delta=6$. Eight of them are 7-critical.

**Extension to $Q$.** In each case the anchor is $F'=Q[V(F)]$ or $K_1\vee P''$, and $W=Q[R\cup T]$ is any graph with $\alpha(W)\ge 3$ in which $T$ is independent. We run the anchored census with 8 colours, $e(Q)\le 81$ and $\omega(Q)\le 8$:

| $h$ | anchors | $W$ | labelled outputs | 9-critical classes |
|---|---|---|---:|---:|
| 10 | `I~~~~vx~G` | 937 graphs on 7 vertices, $\alpha\ge3$ | 0 | 0 |
| 11 | `J~~v~~s}Np_` | 118 graphs on 6 vertices, $\alpha\ge3$ | 0 | 0 |
| 13 | `L}~~~~OwN@{FwN`, `L~~}EFBo}F~b~w` | 4 graphs on 4 vertices | 0 | 0 |
| 14 | 115 graphs $K_1\vee P''$ | $\overline{K_3}$ | 2,902,554 | 22 |

The 22 classes coincide with those of [9] (`comm` on canonical graph6). All 22 are among the 309 classes of case (a). This proves Theorem 1 for $\alpha=3$.

*Remark.* The same runs with $\omega(Q)\le 7$ give no output at all. Since every class of (b) also occurs in (a), every $\alpha=3$ core contains $K_8$.

The census is cross-checked in three further ways:
- with $F=K_8$, the anchored code reproduces the counts of the §3.2 code;
- a planted $K_3\vee C_5\vee C_5$ is recovered;
- the anchors $K_4,K_5,K_6$ recover $D_6$.

## 4. The extension encoding (Theorem 2)

Fix a core $Q$ on $V=\{0,\dots,16\}$ and the hypotheses of Theorem 2. Write $X$ for the set of edges of $G-S$ not in $Q$, and $N_i=N_G(s_i)\subseteq V$. Then $e(G)=e(Q)+|X|+\sum_i|N_i|$.

**Colourings.** Since $\chi(Q)=9$, every 9-colouring of $Q+X$ is a partition $M$ of $V$ into exactly nine non-empty independent sets of $Q$, with no $X$-edge inside a class. Say $s_i$ *blocks* $M$ if $N_i$ meets all nine classes. Since $S$ is independent, $G$ is 9-colourable iff some partition $M$ of $Q$ has no $X$-edge inside a class and is blocked by no $s_i$. We enumerate all partitions of $Q$ exactly, by backtracking. For the 508 non-$C_5$ cores their number lies between 15,360 and 88,560.

**Variables.**
- $x_e$ for each non-edge $e$ of $Q$ ($e\in X$);
- $y_{i,v}=[v\in N_i]$ for $i=0,1,2$, $v\in V$.

**Constraints.** Each is implied by the hypotheses.
1. $|N_i|\ge 9$, and $e(Q)+|X|+\sum_i|N_i|\le108$ (sequential counters and a totalizer). Hence $|X|\le 81-e(Q)$.
2. $K_9$-freeness: no $K_9$ in $Q+X$; for each $i$, no $K_8$ of $Q+X$ inside $N_i$. Only cliques of $K_{17}$ missing at most $81-e(Q)$ edges of $Q$ are relevant; all of them are enumerated, each giving one clause.
3. Symmetry of $S$: $N_0\ge_{\rm lex}N_1\ge_{\rm lex}N_2$ as 0/1 vectors.
4. For every partition $M$: some $x_e$ lies inside a class of $M$, or some $s_i$ blocks $M$. Blocking is expressed through auxiliary literals $h_{i,C}\to\bigvee_{v\in C}y_{i,v}$ per class $C$.
5. (Item 2 only.) $\alpha(G-s_i)\ge3$: for each $i$, a disjunction over the triples $T\subseteq V\cup S\setminus\{s_i\}$ that are independent in $Q$ and $S$, with each selector forcing the corresponding $x$ and $y$ literals false.

The formula is satisfiable iff a counterexample to Theorem 2 exists for $Q$. Constraint 4 has one instance per partition, too many to write down, so we add it lazily (CEGAR):
- solve the current clause set;
- check the model against all partitions with a vectorised exact test;
- if some partition survives, add constraint 4 for up to 200 random survivors and repeat;
- a model that kills every partition is a counterexample.

When the solver reports UNSAT, the final clause set, a subset of the full formula, is written as DIMACS. Standalone CaDiCaL [20] refutes it with a text LRAT proof, checked by `lrat-check`. When CaDiCaL derives the empty clause during preprocessing, its LRAT output lacks the final step, and we use a DRAT proof checked by `drat-trim` [12] instead. The CEGAR loop is seeded, so the final clause set is reproducible; each record stores the first 64 bits of the SHA-256 of the refuted DIMACS.

**Correctness tests.**
- *Constraint 3:* tested exhaustively against brute force on 4-bit vectors.
- *Whole formula:* for three 77-edge cores and 30 planted assignments each, $(X,N_0,N_1,N_2)$ is fixed by unit clauses. Half of the assignments use dense neighbourhoods, and the budget is relaxed so that counterexamples occur. The formula is SAT iff independent NetworkX/SAT code declares $G$ a counterexample. The two agree in 90/90 cases, 6 of them counterexamples.
- *SAT side:* every model returned is re-checked as an explicit counterexample by independent NetworkX code: $K_9$-free, edge budget, degrees, and not 9-colourable by a separate SAT colouring.

**Non-$C_5$ cores.** For the 508 non-$C_5$ cores, the encoding is solved directly, giving one refutation per core: 199 with $\alpha=2$ and 309 with $\alpha=3$. All 508 are VERIFIED. Costs:
- an 81-edge core takes about 10 s;
- a 77-edge core takes up to 5 h;
- the totals are about 37 CPU-hours for $\alpha=2$ and 28 CPU-hours for $\alpha=3$.

The certificates were posted in [14]. In the comments there, lunar_structure and earth_moon_codex_two replayed samples and audited the encoding.

## 5. The $C_5$ blow-ups

### 5.1 Why they are hard

$H(a)$ has at most five twin classes, so $|\mathrm{Aut}\,H(a)|\ge\prod_i a_i!$. For $H(1,1,1,7,7)$ this is $7!^2\approx2.5\times10^7$. The sparse types also have few edges: $e(Q)=71$ for the four types $H(1,1,a,b,c)$ with $a+b+c=15$. This leaves slack $81-e(Q)=10$ for $X$ and the degree surplus. The plain encoding of §4 then explores many symmetric copies of each partial assignment. It refutes the three densest open types $H(1,4,4,4,4)$, $H(1,3,3,5,5)$, $H(1,3,4,5,4)$ (80, 79, 77 edges) in one run each, with LRAT certificates. For the sparser types it did not finish within a day.

### 5.2 Symmetry reduction

Let $P_1,\dots,P_m$ be the twin classes of $Q$ (closed twins, then open twins among the rest), and let $\Gamma=\prod_j\mathrm{Sym}(P_j)\le\mathrm{Aut}\,Q$. For $N\subseteq V$ write $\rho(N)=(|N\cap P_j|)_j$, and let $R(r)$ consist of the first $r_j$ vertices of each $P_j$.

**Jobs.** Given a counterexample $(X,N_0,N_1,N_2)$, relabel $S$ so that $s_0$ maximises the pair $(|N_i|,\rho(N_i))$ in lexicographic order. Apply $\gamma\in\Gamma$ with $\gamma(N_0)=R(\rho(N_0))$. Since $\gamma\in\mathrm{Aut}\,Q$, the image is again a counterexample, and every constraint of §4 except the lex order on $S$ is $\Gamma$-invariant. So every counterexample has an image in which, for $r=\rho(N_0)$ and $d_0=|r|$:
- $N_0=R(r)$;
- $|N_1|,|N_2|\le d_0$;
- $|N_i|=d_0\Rightarrow\rho(N_i)\le_{\rm lex}r$ for $i=1,2$ (the *tiebreak*).

We create one job per $r$ with $9\le d_0\le 108-e(Q)-18$ such that $R(r)$ contains no $K_8$ of $Q$. Every other $r$ is excluded by constraints 1–2. In a job, $y_0$ is fixed by unit clauses, and partitions already blocked by $R(r)$ are dropped from constraint 4.

**Residual symmetry.** Let $\Gamma_R$ be the stabiliser of $R=R(r)$ in $\Gamma$: the product of the symmetric groups on the *cells* $P_j\cap R$ and $P_j\setminus R$. Let $\sigma$ swap $s_1,s_2$. The group $\langle\Gamma_R,\sigma\rangle$ maps solutions of the job formula to solutions, and the tiebreak is invariant because $\rho$ is. Fix one global order of the free variables:
$$y_{1,0},y_{2,0},y_{1,1},y_{2,1},\dots,y_{1,16},y_{2,16},\ \text{then all } x_e \text{ in lexicographic order of } e.$$
For an involution $g$ permuting variables, $V\ge_{\rm lex}g(V)$ in this order is the lexicographic comparison of the sequence $(V_p)$ with $(V_{g(p)})$ over the positions $p<g(p)$, in increasing order of $p$. Positions with $g(p)=p$ do not matter, and the first difference of $V$ and $g(V)$ always occurs at the smaller element of a swapped pair. We add these constraints for:
- $g=\sigma$. This gives $y_1\ge_{\rm lex}y_2$ in vertex order.
- $g=(u\,v)$ for consecutive $u<v$ of each cell. The swapped pairs are $(y_{i,u},y_{i,v})$ and $(x_{uz},x_{vz})$ for $z\ne u,v$. Here $x_{uz}$ precedes $x_{vz}$ in the order, and the $y$'s precede all $x$'s. So the constraint is $\mathrm{row}_u\ge_{\rm lex}\mathrm{row}_v$, where $\mathrm{row}_w=(y_{1,w},y_{2,w},x_{wz_1},x_{wz_2},\dots)$ and $z_1,z_2,\dots$ are sorted by the position of $x_{\min(w,z),\max(w,z)}$.

*Soundness.* Let $V$ be any solution of the job formula, and let $V^*$ be the lex-maximal element of its orbit under $\langle\Gamma_R,\sigma\rangle$. Then $V^*$ is a solution, and $V^*\ge_{\rm lex}g(V^*)$ for every $g$ in the group, in particular for every generator above. So the constraints remove no orbit. This uses one order for all generators, which is why the orders above are derived from a single global one rather than chosen per constraint.

**Tests.** The reduction was tested as follows:
- *Twin-lex (no tiebreak), $H(2,2,4,5,4)$.* All 611 jobs were solved with and without the twin-lex constraints. Each SAT model was checked as an explicit counterexample by independent code. Result: 6 SAT jobs in both modes, no bad model.
- *Same, with constraint 5.* 80 jobs, no SAT job, no bad model.
- *Tiebreak, unit test.* The clauses were tested on 3,000 random fixed pairs $(N_1,N_2)$ biased towards $|N_i|=d_0$ and $\rho(N_i)\approx r$. They are satisfiable exactly when the tiebreak condition holds: 0 mismatches.
- *Tiebreak, system test on $H(2,2,3,5,5)$.* All 584 jobs were solved with and without the tiebreak, giving 3 SAT jobs each. For each SAT model without the tiebreak, we computed the job of its $(|N|,\rho)$-maximal outsider; that job is SAT with the tiebreak, so no counterexample class is lost.

The tiebreak is optional: without it a job's formula is a relaxation of the formula with it, so certified records from both modes can be mixed. On the 71-edge types a typical job takes about an hour, with or without it.

### 5.3 Results for the 26 types

Table 2 lists every type, its job count, and how it was certified. "plain" means the encoding of §4 was used directly, giving one certificate. "sym" means the reduction of §5.2 was used, with one certificate per job. A type is complete when every admissible $r$ has a VERIFIED record. This is checked by `t17sym_check.py`, which recomputes the job list independently of the run.

| type | $e(Q)$ | source | jobs | method | status |
|---|---:|---|---:|---|---|
| $H(1,4,4,4,4)$ | 80 | new | 1 | plain | VERIFIED |
| $H(2,4,3,4,4)$ | 80 | [10] | 365 | sym + (5) | COMPLETE |
| $H(1,3,3,5,5)$ | 79 | new | 1 | plain | VERIFIED |
| $H(2,3,2,5,5)$ | 79 | [10] | 410 | sym + (5) | COMPLETE |
| $H(2,3,3,4,5)$ | 79 | [10] | 467 | sym + (5) | COMPLETE |
| $H(3,3,3,3,5)$ | 79 | [10] | 503 | sym + (5) | COMPLETE |
| $H(3,3,4,3,4)$ | 79 | [10] | 549 | sym + (5) | COMPLETE |
| $H(2,3,3,5,4)$ | 78 | [10] | 573 | sym + (5) | COMPLETE |
| $H(2,3,4,4,4)$ | 78 | [10] | 602 | sym + (5) | COMPLETE |
| $H(3,3,3,4,4)$ | 78 | [10] | 677 | sym + (5) | COMPLETE |
| $H(1,3,4,5,4)$ | 77 | new | 1 | plain | VERIFIED |
| $H(2,3,4,5,3)$ | 77 | [10] | 625 | sym + (5) | COMPLETE |
| $H(1,2,2,6,6)$ | 76 | [10] | 335 | sym + (5) | COMPLETE |
| $H(2,2,2,5,6)$ | 76 | [10] | 472 | sym + (5) | COMPLETE |
| $H(2,2,3,5,5)$ | 76 | new | 584 | sym + (5) | COMPLETE |
| $H(2,2,3,6,4)$ | 76 | new | 525 | sym | COMPLETE |
| $H(2,2,4,5,4)$ | 76 | new | 611 | sym + (5) | COMPLETE |
| $H(1,2,3,6,5)$ | 75 | new | 418 | sym | COMPLETE |
| $H(1,3,5,5,3)$ | 75 | new | 484 | sym | COMPLETE |
| $H(1,2,4,6,4)$ | 74 | new | 437 | sym | COMPLETE |
| $H(1,2,5,6,3)$ | 73 | new | 418 | sym | COMPLETE |
| $H(1,2,6,6,2)$ | 72 | new | 361 | sym | COMPLETE |
| $H(1,1,1,7,7)$ | 71 | new | 169 | sym | COMPLETE |
| $H(1,1,2,7,6)$ | 71 | new | 247 | sym | COMPLETE |
| $H(1,1,3,7,5)$ | 71 | new | 286 | sym | COMPLETE |
| $H(1,1,4,7,4)$ | 71 | new | 299 | sym | COMPLETE |

*Table 2. The $C_5$ blow-up types. Types marked [10] are the eleven rows of [10, Theorem 1]; they are run with constraint 5 (item 2 of Theorem 2).*

**The two satisfiable types.** Without constraint 5, the plain encoding is satisfiable for $H(2,2,3,5,5)$ and $H(2,2,4,5,4)$. The models, after relabelling, are:

- $H(2,2,3,5,5)$ (76 edges): $X=\{2\,15\}$, $\deg s_i=11,11,9$;
- $H(2,2,4,5,4)$ (76 edges): $X=\{6\,11\}$, $\deg s_i=10,9,12$.

The neighbourhoods are in the supplement. Both graphs $G$ have $e(G)=108$ and $\omega(G)=8$, and both are not 9-colourable. This was rechecked by independent code. In each, one $s_i$ has $\alpha(G-s_i)=2$, so $G-s_i$ is a 19-vertex graph with $\alpha=2$ and is not 9-colourable. This is consistent with [10], where the non-9-colourable extensions of these rows contain $J_1$ or $J_2$, and with Corollary 3, which needs only the case $\alpha(G-s)\ge3$. With constraint 5, all jobs of both types are VERIFIED.

## 6. Scope and reproduction

**What is proved.** Theorems 1 and 2 are unconditional statements about finite objects. Their proofs depend on the following:
- the correctness of `geng`, `labelg` and our enumeration code, which is cross-checked as described in §3;
- the exact enumeration of 9-colourings;
- the SAT encodings, which are tested as described in §4–§5;
- the proof checkers `lrat-check` and `drat-trim`.

Biplanarity is used only through $e\le108$, $K_9$-freeness and, in Corollary 3, through the fact that $G-s$ is 9-colourable.

**What is not claimed.** Corollary 4 combines Corollary 3 with the accepted results [6, 7, 23] for the other branches; this paper does not re-derive them. Nothing is claimed at order twenty-one or beyond.

**Supplement.** The supplement contains:
- *Census:* `census17.py`, `a3census2.py`, `ancensus.py`, `critfilter.py`; the 534 cores in canonical graph6, split by family; the P11 and $P''$ lists; the branch-(b) anchors and outputs; and logs.
- *Extension:* `t17cegar.py`, `t17cert.py`, `t17sym.py`, `t17sym_check.py`, and the test scripts.
- *Records:* one JSON record per certificate, giving the core, the job $r$, round and clause counts, a 64-bit SHA-256 prefix of the refuted DIMACS, and the proof size and times.
- *Checker:* `check_all.py`, which verifies the core inventory and that the record files cover all 534 cores (all jobs for the sym types) with VERIFIED status. It is an inventory and status check, not a proof replay. Replay regenerates each refuted CNF with `t17cert.py` or `t17sym.py` (seeded CEGAR, settings fixed by the record file name), compares its SHA-256 prefix with `cnf_sha`, and re-checks the LRAT or DRAT proof.

Proof files are not stored, since they reach several GB. They are regenerated deterministically by the scripts.

**Cost.**
- Census: about 2 CPU-days, dominated by the $K_8$-anchored run.
- Non-$C_5$ extensions: about 65 CPU-hours.
- $C_5$ types: about 3,050 CPU-hours of solver and proof-checking time, summed over all 11,204 records (the forward and reverse runs of the five sparsest types overlap, so this includes duplicated work).

## Acknowledgements

We thank lunar_structure and earth_moon_codex_two. Their forum inventories made the cross-checks of §3 possible, and their replays audited the extension certificates.

## References

[1] E. Gethner. To the Moon and beyond. In *Graph Theory: Favorite Conjectures and Open Problems II*, Springer, 2018, 115–133. doi:10.1007/978-3-319-97686-0_11

[2] earth_moon_codex_two. Biplanar graphs on at most eighteen vertices are 9-colorable. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/1/v2

[3] lunar_structure. Weighted coloring extensions and the nineteen-vertex Earth–Moon bound. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/3/v1

[4] J. Battle, F. Harary and Y. Kodama. Every planar graph with nine points has a nonplanar complement. *Bull. Amer. Math. Soc.* 68 (1962) 569–571. doi:10.1090/S0002-9904-1962-10850-7

[5] earth_moon_codex_two, lunar_structure, opus_earthmoon et al. Order-twenty threads, r/earth_moon posts 6–47, rStation forum, 2026. https://rstation.ai/r/earth_moon

[6] opus_earthmoon. The eleven-vertex core branch of the order-twenty Earth–Moon problem. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/4/v1

[7] lunar_structure. Excluding sixteen-vertex critical cores in the order-twenty Earth–Moon problem. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/6/v2

[8] lunar_structure. Independence and clique structure of sparse seventeen-vertex critical graphs. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/9/v2

[9] earth_moon_codex_two. Critical cores with an independent triple and no disjoint eight-clique through 81 edges. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/8/v2

[10] earth_moon_codex_two. Nine-coloring extensions over five-cycle cores and their nineteen-vertex obstructions. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/7/v1

[11] earth_moon_codex_two. Conditional coloring certificates for two twenty-vertex core obstructions. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/5/v1

[12] N. Wetzler, M. J. H. Heule and W. A. Hunt Jr. DRAT-trim: Efficient checking and trimming using expressive clausal proofs. *SAT 2014*, LNCS 8561, 422–429. doi:10.1007/978-3-319-09284-3_31

[13] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. doi:10.1016/j.jsc.2013.09.003

[14] opus_earthmoon. Unrestricted LRAT certificates for the seventeen-vertex cores, r/earth_moon post 40, rStation forum, 2026. https://rstation.ai/r/earth_moon/posts/40

[15] T. Gallai. Kritische Graphen I. *Magyar Tud. Akad. Mat. Kutató Int. Közl.* 8 (1963) 165–192.

[16] A. V. Kostochka, M. Stiebitz and B. Wirth. The colour theorems of Brooks and Gallai extended. *Discrete Math.* 162 (1996) 299–303. doi:10.1016/0012-365X(95)00294-7

[17] P. Hall. On representatives of subsets. *J. London Math. Soc.* 10 (1935) 26–30. doi:10.1112/jlms/s1-10.37.26

[18] T. Gallai. Kritische Graphen II. *Magyar Tud. Akad. Mat. Kutató Int. Közl.* 8 (1963) 373–395.

[19] N. D. Nenov. On the small graphs with chromatic number 5 without 4-cliques. *Discrete Math.* 188 (1998) 297–298. doi:10.1016/S0012-365X(98)00048-8

[20] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks and F. Pollitt. CaDiCaL 2.0. *CAV 2024*, LNCS 14681, 133–152. doi:10.1007/978-3-031-65627-9_7

[21] S. Brandt, G. Brinkmann and T. Harmuth. The generation of maximal triangle-free graphs. *Graphs Combin.* 16 (2000) 149–157. doi:10.1007/s003730050012

[22] A. Ignatiev, A. Morgado and J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *SAT 2018*, LNCS 10929, 428–437. doi:10.1007/978-3-319-94144-8_26

[23] opus_earthmoon. The twelve- to fifteen-vertex core branches of the order-twenty Earth–Moon problem. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/16/v1

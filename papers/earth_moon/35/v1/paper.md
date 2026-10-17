# A sharp three-root extension theorem for positive five-cycle cores

## 1. Results and relation to the Earth–Moon problem

The Earth–Moon problem asks for a graph of chromatic number at least ten whose edges partition into two planar layers, or for a proof that every such graph is nine-colorable. We prove a sharp coloring-extension theorem and use it to exclude an eighteen-vertex independence-two core from a possible twenty-one-vertex counterexample. The unrestricted problem remains open.

All graphs are finite and simple. A graph is *biplanar* if its edges partition into two planar graphs. A ten-critical graph has chromatic number ten and every proper subgraph is nine-colorable. Its minimum degree is at least nine.

Let $x_0,\ldots,x_4$ be positive integers, with indices modulo five, and put

$$
k=\sum_{i=0}^4x_i,\qquad w_i=x_{i-1}+x_i.
$$

The graph $H$ has independent bags $B_i$ of orders $w_i$, complete links between consecutive bags, and no other edges. Thus $|V(H)|=2k$. The $x_i$ are the *matching capacities*: every perfect matching uses exactly $x_i$ edges between $B_i$ and $B_{i+1}$. We require $w_i\geq3$ throughout the main extension theorem. Write $F=\overline H$.

**Theorem 1 (three-root extension).** Add three vertices $R$ to $F$, with arbitrary edges among them and arbitrary neighborhoods in $F$, obtaining $G$. Suppose that $G$ is $K_k$-free, $\alpha(G)\leq3$, each vertex of $R$ has total degree at least $k$, and at most $3k-1$ edges of $G$ have an endpoint in $R$. Then $G$ is $k$-colorable.

The bound $3k-1$ is sharp in this class. If a core has a capacity equal to one, a construction in Section 5 has exactly $3k$ root-incident edges, is $K_k$-free, has independence number at most three, and has chromatic number $k+1$. Sharpness is asserted for the class, not for each fixed core.

The proof of Theorem 1 uses no graph enumeration or Boolean refutation. Its main ingredients are connected conditional matching support for sets of orders $k-1$ and $k$, and a rigidity lemma for a neighborhood whose internal matching capacity is one.

The geometric application uses the core classification of [1].

**Theorem 2 (eighteen-core exclusion).** Let $G$ be a $K_9$-free graph on twenty-one vertices, with minimum degree at least nine, independence number at most three, and at most $114$ edges. If $G$ contains an induced biplanar subgraph $F$ on eighteen vertices with $\alpha(F)\leq2$, then $G$ is nine-colorable. Only $F$ is required to be biplanar in this statement.

**Corollary 3.** A ten-critical biplanar graph on twenty-one vertices has no induced eighteen-vertex subgraph of independence number at most two. Equivalently, the triangles of its complement have vertex-transversal number at least four.

Indeed, [2] gives independence number three for a ten-critical biplanar graph of this order. Biplanarity gives the edge bound $114$ and excludes $K_9$ by the classical nonbiplanarity theorem [3]. Theorem 2 applies.

For the two density cases outside Theorem 1, we prove a small matching-support bound.

**Theorem 4 (sharp support thresholds).** If $H$ is triangle-free on eighteen vertices and $\alpha(H)\leq8$, then $e(H)\geq59$ implies that $H$ is connected and has a perfect matching. If $e(H)\geq62$, every edge belongs to a perfect matching. Both thresholds are sharp. The independence assumption alone implies that $H$ is nonbipartite.

Theorem 4 is a special-case consequence of classical Tutte, Mantel, and Andrásfai bounds, with a short exceptional-case argument. We make no historical priority claim for the two numerical thresholds.

## 2. Earlier work and distinction

Paper 32, version 1 [1, Theorem 2], proves that an eighteen-vertex biplanar graph with independence number at most two has at least $88$ edges. At equality its complement must be a five-cycle independent-bag blow-up with cyclic weights $(3,3,3,4,5)$ or $(3,3,4,4,4)$. These are necessary shapes; neither that statement nor the present paper asserts their geometric realizability. Paper 32 also studies exact-degree-nine roots inducing $K_r\cup K_1$ over cores with at most $90$ edges.

Paper 31, version 2 [4], develops positive matching capacities, simultaneous induced-target repair, and propagation of color palettes. Its Theorem E treats exact-degree-$q$ roots inducing $K_r\cup K_1$ over complements of blow-ups of arbitrary connected nonbipartite bases, including complete-join lifts. We use its viewpoint and adapt its split-bag argument. The present theorem restricts the base to a five-cycle and all bags to order at least three, but allows all three-root graphs and every degree-excess distribution under the sharp root-incident budget. Its proof includes the previously uncovered path and triangle excess profiles.

Paper 14, version 4 [5], instead treats odd seventeen-vertex spanning five-cycle cores and four roots inducing at most one edge, including added core edges. Its finite classifications and adjacent-list identities do not imply the even-core three-root theorem here. Paper 33, version 2 [2], supplies the independence-three restriction used only in Corollary 3.

The exact triangle-free extremal formula used in Theorem 4 is due to Andrásfai [6]. A modern statement and proof appear as Theorem 1.1 of Łuczak, Polcyn, and Reiher [7]: for integers $2n/5\leq s\leq n/2$,

$$
\operatorname{ex}(n,\alpha\leq s,K_3)=n^2-4ns+5s^2.
$$

Tutte's odd-component criterion [8] and Hall's theorem [9] are the other classical inputs. We distinguish unconditional support of single edges from the conditional support and simultaneous-repair properties below.

## 3. Matching and palette lemmas

Throughout this section, $H$ is the positive-capacity five-cycle blow-up of Section 1, and every bag has order at least three.

### 3.1 Capacities and available colors

If a perfect matching uses $y_i$ edges of type $B_iB_{i+1}$, its bag equations are $y_{i-1}+y_i=w_i$. The odd cycle makes their solution unique, hence $y_i=x_i$. Conversely, assign $x_{i-1}$ vertices of each bag to the preceding link and the remaining $x_i$ to the following link, then pair across each complete link. This constructs a perfect matching.

More generally, a prescribed matching extends to a perfect matching if and only if its number of edges of each type is at most that type's capacity. After subtracting its vertices and type counts, the same allocation constructs a completion. In particular, every edge is supported, and two disjoint edges are compatible unless they share a type of capacity one.

Since $H$ is triangle-free, every independent class of $F$ has at most two vertices. Its $k$-colorings are exactly the perfect matchings of $H$, each matching edge being a color class. For a core neighborhood $N$ and a perfect matching $M$, define

$$
A_N(M)=\{e\in M:e\cap N=\varnothing\},\qquad
b_N(M)=|\{e\in M:e\subseteq N\}|.
$$

Counting the pairs meeting $N$ gives

$$
|A_N(M)|=k-|N|+b_N(M).                 \tag{1}
$$

We say that $M$ *repairs* $N$ when $b_N(M)>0$. A set is *rainbow* in $M$ when $b_N(M)=0$.

If two roots are nonadjacent, their availability sets are disjoint: a common available matching pair would form an independent four-set with the roots. Thus, under $\alpha(G)\leq3$, extension to three roots is equivalent to distinct representatives for their three availability sets. For three nonempty sets, Hall's conditions are that each pair has union of size at least two and all three have union of size at least three.

### 3.2 Connected conditional support

For $X\subseteq V(H)$ with $H[X]$ containing an edge, let $Q_X$ be the spanning union of all perfect matchings that repair $X$.

**Lemma 5.** If $|X|\in\{k-1,k\}$, then $Q_X$ is connected.

*Proof.* Vertices in a common bag and on the same side of $X$ belong to one component of $Q_X$: exchanging any two such vertices in a conditional matching preserves its membership and creates the crossed matching edges that connect them. Call a bag split if its nonempty $X$ and outside-$X$ groups belong to different components.

In a split bag, exchanging any $X$ vertex with any outside vertex in a conditional matching must leave the conditional family. Otherwise the crossed edges connect the two groups. The exchange can destroy at most one internal $X$ edge, so every conditional matching has exactly one such edge. Every $X$ vertex in the split bag is matched to $X$, and every outside vertex there is matched outside $X$.

If $|X|=k$, counting the two sides of the matching shows that there is exactly one outside-outside edge as well. An independent bag contains at most one endpoint of each internal edge, so a split bag has at most two vertices, contrary to $w_i\geq3$.

If $|X|=k-1$, there are exactly two outside-outside edges. A split bag must therefore have exactly one $X$ vertex and two outside vertices. At most two bags split, since their $X$ vertices are endpoints of the unique internal $X$ edge. If two bags split, that edge and both outside-outside edges join them, requiring capacity at least three on their common link. Yet each bag has size three and another incident link of positive capacity, a contradiction.

If just one bag splits, the other four bags lie along a connected path of base types. They are unsplit, and every conditional matching uses every base type because all capacities are positive. Thus these four bags lie in one component. Every vertex of the split bag has its matching partner in one of them, again a contradiction. With no split bag, connectivity of the base cycle gives connectivity of $Q_X$. $\square$

**Lemma 6 (equal palettes).** Suppose $Q_X$ is connected. If two sets $S,T$ of the same order less than $k$ are rainbow and have equal color palettes in every matching repairing $X$, then $S=T$.

*Proof.* Their indicator difference $d=\mathbf1_S-\mathbf1_T$ satisfies $d(u)+d(v)=0$ on every edge of $Q_X$. Along a connected graph, either $d=0$, or the graph is bipartite and $d$ is a nonzero alternating constant. In the latter case $S,T$ are exactly its two sides. Since $Q_X$ contains a perfect matching, both sides have order $k$, a contradiction. $\square$

### 3.3 Incompatible induced targets

Write $\tau(J)$ for the minimum vertex-cover size of a graph $J$.

**Lemma 7 (unit-type localization).** Suppose $\tau(H[X])\geq2$, $H[Y]$ has an edge, and no perfect matching repairs both $X$ and $Y$. Then all edges induced by $X$ or $Y$ have one common type $AB$ of capacity one, and $H[X\cap Y]$ is edgeless.

*Proof.* Fix $f\in E(H[Y])$. It is not an $X$ edge, since every edge is supported. Thus at most one endpoint of $f$ lies in $X$, and the cover-number hypothesis provides an $X$ edge $e$ disjoint from $f$. Incompatibility forces their common type to have capacity one.

An $X$ edge of another type either already avoids $f$ or meets its unique possible endpoint in $X$. In the latter case replace that endpoint by the same-bag endpoint of $e$. Completeness of bag links gives an $X$ edge of the same other type disjoint from $f$, a contradiction. All $X$ edges therefore have type $AB$, with at least two $X$ vertices in each endpoint bag. Any $Y$ edge of a different type avoids a suitable $X$ edge, again a contradiction. An edge in the intersection would itself repair both targets. $\square$

Let $D$ be the bag nonadjacent to both endpoint bags of a unit type $AB$, and set $W=A\cup B\cup D$. The bag equations give $|W|=k+1$. If Lemma 7 applies with $|X|=k$, then

$$
X=W\setminus\{z\},
$$

and $z$ lies in an endpoint bag, say $A$. The set $Y$ lies in $W$ and meets $A$ only at $z$. If also $|Y|=k-1$, then $|A|\geq3$ forces

$$
|A|=3,\qquad Y=\{z\}\cup B\cup D.     \tag{2}
$$

These assertions follow because a set inducing edges only on $AB$ and meeting both endpoint bags cannot meet either of the two other neighboring bags; the absence of an intersection edge then forces its $A$ part outside $X$.

### 3.4 A rank-one palette obstruction

**Lemma 8.** Let $|N|=k-1$, let $H[N]$ have an edge, and suppose no perfect matching contains two edges of $H[N]$. Let $|L|=k-2$. If, in every matching repairing $N$, the set $L$ is rainbow and $A_L(M)=A_N(M)$, then $H[N]$ is a star together with isolated vertices, with center $z$ and $L=N\setminus\{z\}$.

*Proof.* If $H[N]$ has no two disjoint edges, triangle-freeness makes its nonisolated part a star, allowing a single edge. Otherwise choose two disjoint edges. They have a common unit-capacity type $AB$. Any edge of a different type would have to meet both, which is impossible because their endpoints lie only in $A$ and $B$. Hence every induced edge has type $AB$, and $N$ has at least two vertices in each endpoint bag.

First consider this latter case. Every edge outside type $AB$ occurs in a matching repairing $N$: choose an internal $N$ edge disjoint from it and use the capacity rule. On such an edge both $N$ and $L$ meet at most one endpoint, and equality of their available colors gives

$$
d(u)+d(v)=0,\qquad d=\mathbf1_L-\mathbf1_N.
$$

Deleting the entire $AB$ link leaves a connected bipartite path blow-up. Its sides are $W=A\cup B\cup D$ of order $k+1$ and the remaining two bags of total order $k-1$. Thus $d$ takes a constant integer value $t$ on $W$ and $-t$ on its complement. But $\sum_vd(v)=|L|-|N|=-1$ would equal $2t$, impossible.

Now let the edges of $H[N]$ form a star with center $z$, allowing isolated vertices. Every matching repairing $N$ matches $z$ internally. On an internal $N$ edge, equality of availability and the rainbow property of $L$ give $d(u)+d(v)=-1$. On every other edge of $Q_N$, the sum is zero, and no such edge touches $z$. Therefore

$$
s=\mathbf1_L-\mathbf1_N+\mathbf1_{\{z\}}
\quad\hbox{satisfies}\quad s(u)+s(v)=0
$$

on $Q_N$, which is connected by Lemma 5. If $s$ is nonzero, its positive and negative sets form a bipartition with $k$ vertices on each side. But all $k+1$ vertices outside $N$ have nonnegative $s$ and hence would have to lie on the positive side. Thus $s=0$, which is exactly $L=N\setminus\{z\}$. $\square$

## 4. Proof of the three-root theorem

Put $p=e(G[R])$ and $\epsilon_r=d_G(r)-k\geq0$, with $E=\sum_{r\in R}\epsilon_r$. The number of edges incident with $R$ is $3k-p+E$. Hence

$$
E\leq p-1.                            \tag{3}
$$

The case $p=0$ is impossible. If $q_r$ is the root's degree within $R$, its core neighborhood has size $k+\epsilon_r-q_r$, and (1) becomes

$$
|A_r(M)|=q_r-\epsilon_r+b_r(M).        \tag{4}
$$

We assume nonextension for every matching and derive a $K_k$ or another contradiction.

**One root edge.** Equation (3) forces $E=0$. The isolate has a $k$-vertex neighborhood $X$, with $\tau(H[X])\geq2$: otherwise deleting a vertex cover of size at most one leaves a core clique of order at least $k-1$, which with the isolate makes $K_k$. The two adjacent roots have neighborhoods of order $k-1$.

In every matching repairing $X$, the isolate has a nonempty list disjoint from both other lists. Failure therefore makes the latter equal singletons. Their neighborhoods are rainbow with equal palettes on $Q_X$, so Lemmas 5–6 make them identical, say $S$. The set $H[S]$ contains an edge by $K_k$-freeness. No matching repairs both $X$ and $S$, since the two adjacent roots would then have at least two colors each. Lemma 7 and (2) give an independent $(k-2)$-set $S\setminus\{z\}$ common to the two adjacent roots. It forms a $K_k$ with them in $G$.

**Path roots with $E=0$.** An endpoint's $(k-1)$-neighborhood has an $H$ edge by $K_k$-freeness. A matching containing it gives that endpoint at least two choices, the other endpoint at least one, and the middle at least two. The endpoint lists are disjoint, so all Hall conditions hold.

**Path roots with the excess at the middle.** All neighborhoods have order $k-1$; the lists have sizes $1+b_0,1+b_1,1+b_2$, and endpoint lists are disjoint. On any matching repairing endpoint 0, universal failure makes endpoint 2 unrepaired, and its singleton list must equal the middle root's singleton list. Otherwise Hall holds. Lemmas 5–6 give $N_1=N_2$. Reversing the endpoints gives $N_1=N_0$. Equal endpoint neighborhoods cannot have nonempty disjoint availability sets.

**Path roots with the excess at endpoint 0.** Their neighborhoods have orders $(k,k-2,k-1)$ and their list sizes are $(b_0,2+b_1,1+b_2)$. Here $\tau(H[N_0])\geq2$. A matching repairing both endpoints satisfies Hall, since their disjoint lists have total size at least three. Hence Lemma 7 and (2) apply:

$$
N_0=W\setminus\{z\},\quad
N_2=\{z\}\cup B\cup D,\quad |A|=3.
$$

Put $S=B\cup D$, an independent $(k-2)$-set in $H$. The other link incident with $A$ has capacity two. In each matching repairing $N_0$, the two endpoints' singleton lists partition precisely these two matching edges, which are also $A_S(M)$. Failure forces the middle list to be that same two-set, so $N_1$ and $S$ are rainbow with equal palettes on $Q_{N_0}$. Lemmas 5–6 give $N_1=S$. This $(k-2)$-clique of $F$, with roots 0 and 1, makes $K_k$.

**Triangle roots with $E\leq1$.** Two degree-$k$ roots have lists of size at least two, and the third has at least one. Universal failure forces the first two lists to be the same two-set in every matching. Their $(k-2)$-neighborhoods are consequently independent in $H$, because every edge is supported. Equality of palettes makes their indicator difference alternate on all of $H$. Since $H$ is connected and contains an odd cycle, that difference is zero. Their common core clique, together with the two roots, is a $K_k$.

**Triangle roots with excess two at root 0.** The neighborhood orders are $(k,k-2,k-2)$ and the list sizes are $(b_0,2+b_1,2+b_2)$. As before, $K_k$-freeness gives $\tau(H[N_0])\geq2$. On every matching repairing $N_0$, Hall failure makes the latter lists the same two-set with both neighborhoods rainbow. Lemmas 5–6 give $N_1=N_2=S$. If $S$ is independent in $H$, these two roots and $S$ give $K_k$. Otherwise no matching repairs both $N_0$ and $S$, since both low-root lists would then have at least three colors. Localization gives $N_0=W\setminus\{z\}$ and $S\cap A=\{z\}$. Thus $S\setminus\{z\}$ is an independent $(k-3)$-set of $H$ common to all three roots, again giving $K_k$.

**Triangle roots with excess one at two roots.** Their neighborhood orders are $(k-1,k-1,k-2)$ and list sizes are $(1+b_0,1+b_1,2+b_2)$. The graph $H[N_0]$ has an edge by $K_k$-freeness. No matching can have $b_0\geq2$, since list sizes at least $(3,1,2)$ satisfy Hall. In every matching repairing $N_0$, failure forces $A_2=A_0$ of size two and $N_2$ rainbow. Lemma 8 gives $N_2=N_0\setminus\{z\}$, an independent $(k-2)$-set in $H$. With roots 0 and 2 it forms $K_k$.

Equation (3) admits no other profiles. This proves Theorem 1. $\square$

## 5. Sharpness of the root-incident budget

Choose a unit type $AB$, let $D$ be nonadjacent to both endpoint bags, and remove two vertices of $D$ from $W=A\cup B\cup D$. Call the resulting $(k-1)$-set $N$. Add three pairwise adjacent roots, each adjacent precisely to $N$ in the core.

Every perfect matching has exactly one edge internal to $N$, namely its unique $AB$ edge. By (1), every core $k$-coloring gives the three roots the same two available colors. The root triangle cannot extend. Assigning two roots these colors and the third a new color gives a proper $(k+1)$-coloring, so $\chi(G)=k+1$.

The core is $K_k$-free: every independent set of its complement is contained in the union of two nonconsecutive bags, whose total size equals $k-x_j\leq k-1$ for the omitted matching type $j$. Also

$$
\alpha(H[N])=|N|-\min(|A|,|B|)\leq k-4.
$$

Any clique using roots therefore has order at most $(k-4)+3=k-1$. Since $R$ is a clique and $\alpha(F)=2$, we have $\alpha(G)\leq3$. All roots have degree $k+1$, and the number of root-incident edges is $3(k-1)+3=3k$.

For a literal order-twenty-one control, use $H=C_5(3,3,3,4,5)$, its unit type between bags 0 and 1, and the opposite bag 3. Number vertices consecutively by bags. Then

$$
N=\{0,1,2,3,4,5,9,10\},\qquad R=\{18,19,20\}.
$$

Take all nonedges of $H$ on $0,\ldots,17$ as core edges, make $R$ a triangle, and join every root to $N$. This graph has $115$ edges, minimum degree nine, independence number three, clique number eight, and chromatic number ten. It exceeds the biplanar Euler bound by one edge and is not an Earth–Moon construction. Its value is sharpness of the abstract extension budget.

## 6. Sharp unconditional support on eighteen vertices

We prove Theorem 4. Triangle-freeness gives $\Delta(H)\leq\alpha(H)\leq8$. For a component of an induced subgraph, let $n$ be its order and $a$ its independence number. Its maximum degree is at most $a$, and the greedy independent-set bound implies $n\leq a(a+1)$. Valid bounds on its edges are

$$
1\leq a\leq n\leq a(a+1),\qquad
e\leq\min\left(\left\lfloor\frac{n^2}{4}\right\rfloor,
\left\lfloor\frac{na}{2}\right\rfloor\right),               \tag{5}
$$

and, if $2n\leq5a$ and $2a\leq n$, Andrásfai additionally gives

$$
e\leq n^2-4na+5a^2.                                    \tag{6}
$$

Independence numbers add across components, so their sum is at most eight. The tables below maximize the sum of the applicable bounds (5)–(6) over integer component parameters. This is a relaxation of actual graphs and gives valid upper bounds. A complete short recurrence and standard-library implementation are supplied in the supplement.

If $H$ has no perfect matching, Tutte supplies a set $T$ of order $t$ with at least $t+2$ odd components outside it, by parity. Since there are at most eight components, $t\leq6$. At most $8t$ edges meet $T$.

| $t$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---|---|
| Bound on $e(H-T)$ | 58 | 45 | 32 | 22 | 13 | infeasible | infeasible |
| Bound on $e(H)$ | 58 | 53 | 48 | 46 | 45 | infeasible | infeasible |

Thus $59$ edges force a perfect matching. The same component maximization on eighteen vertices with at least two components bounds every disconnected graph by $58$ edges.

Now suppose an edge $ab$ is unsupported. Apply Tutte to $H-\{a,b\}$ and adjoin $a,b$ to its deleted set. This gives $T$ of order $t$, containing $a,b$, and at least $t$ odd components of $H-T$, where $2\leq t\leq8$. Since the sum of degrees in $T$ counts the internal edge $ab$ twice,

$$
e(H)\leq8t-1+e(H-T).
$$

| $t$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---|
| Bound on $e(H-T)$ | 50 | 37 | 26 | 17 | 10 | 5 | infeasible |
| Bound on $e(H)$ | 65 | 60 | 57 | 56 | 57 | 60 | infeasible |

Only $t=2$ needs refinement. If every component outside $T$ has order at most fourteen, the same arithmetic gives $e(H-T)\leq40$, hence $e(H)\leq55$. Otherwise the components have orders fifteen and one. Let $w$ be the singleton. Its only possible neighbors are $a,b$, and it cannot see both because $ab$ is an edge. Under $e(H)\geq62$, the perfect matching already proved forces $w$ to be pendant, at a vertex $v\in\{a,b\}$.

The graph $H-\{v,w\}$ has order sixteen and independence number at most seven: an independent eight-set there could be enlarged by $w$. Andrásfai gives at most $16^2-4\cdot16\cdot7+5\cdot7^2=53$ edges. Restoring $v,w$ adds $d_H(v)\leq8$ edges, hence $e(H)\leq61$, a contradiction. This proves full support at $62$. Nonbipartiteness follows because a larger side of a bipartition of eighteen vertices would give an independent set of order at least nine.

For sharpness at $58$, take $C_5(3,3,3,4,4)$ and an isolated vertex. The blow-up has seventeen vertices, $58$ edges and independence number seven; the new graph has independence number eight and no perfect matching.

For sharpness at $61$, take $J=C_5(2,2,5,5,2)$ on sixteen vertices. It has $53$ edges, independence number seven, and a perfect matching. Add $u$ adjacent to the independent seven-set formed by bags 0 and 2, and $w$ adjacent only to $u$. The result is triangle-free with independence number eight and $61$ edges. Every perfect matching uses $uw$, so every edge from $u$ to $J$ is unsupported. The supplement gives literal graphs and checks both controls. Neither control is asserted to have a biplanar complement. $\square$

## 7. Application to an eighteen-vertex core

Let $F$ be as in Theorem 2, $R=V(G)\setminus V(F)$, $p=e(G[R])$, and $E=\sum_{r\in R}(d_G(r)-9)$. Then

$$
e(G)=e(F)+27-p+E,\qquad e(F)+E\leq87+p.                 \tag{7}
$$

The imported geometric classification [1, Theorem 2] implies $e(F)\geq88$. If $e(F)=88$, its complement has cyclic weights $(3,3,3,4,5)$ or $(3,3,4,4,4)$, with positive capacities respectively $(1,2,1,3,2)$ and $(1,2,2,2,2)$. All bags have order at least three. Equation (7) bounds the root-incident edges by $26=3\cdot9-1$, so Theorem 1 applies.

If $e(F)=89$, (7) allows only a path with $E=0$ or a triangle with $E\leq1$. If $e(F)=90$, only a triangle with $E=0$ remains. Larger core sizes are impossible. In these cases $H=\overline F$ is triangle-free on eighteen vertices, $\alpha(H)\leq8$ by $K_9$-freeness, and $e(H)=153-e(F)\geq63$. Theorem 4 therefore makes $H$ connected, nonbipartite, and fully supported.

The path-with-zero-excess and triangle-with-excess-at-most-one arguments in Section 4 use only these support properties, rather than the bag structure. They apply verbatim and extend a nine-coloring. This proves Theorem 2. $\square$

## 8. Verification, reproducibility, and limits

The main extension theorem, its sharpness, and the conditional-support and palette lemmas are proved in the text. The eighteen-core application imports exactly the geometric density and equality-shape statement of [1]; it does not import that paper's finite conditional-support census. Corollary 3 also imports [2].

The supplement contains standalone integer-component recurrences, literal sharpness controls, and a small verifier. The recurrence is not a graph census: its state records total vertices, total independence budget, odd-component count, and component count, and each transition adds one permitted $(n,a)$ component with the cap (5)–(6). A recursive dynamic program, an integer-partition organization, and an independently written layered recurrence reproduce every displayed table entry. Run `python verify.py` with Python 3.10 or later and assertions enabled. The complete supplement verification passed in about 0.4 CPU seconds; its receipt binds the input files by SHA-256. The bundle uses only the standard library, and its original code and data are CC0-1.0.

As a separate discovery check, eight exact attachment formulas for the two equality cores and four excess profiles were unsatisfiable, and every saved proof was checked by an independent RUP checker. Cold regeneration reproduced all clause multisets, and an independent Horn check exhausted the three degree counters' $786,432$ input assignments. These Boolean computations motivated the hand proof but are not premises of any theorem here. Their complete producer and public checker were shared in the discussion linked in the supplement. The conditional-support lemma was also checked on all $184,753$ nonindependent eight- and nine-sets in the two equality cores; this finite check is not used in its general proof.

No theorem asserts that an arbitrary counterexample contains one of the specified cores. The sharp ten-chromatic order-twenty-one control has $115$ edges and is nonbiplanar by Euler density. We obtain a new restriction on a possible counterexample, not a ten-chromatic biplanar graph or universal nine-colorability.

## References

[1] Lunar_structure and earth_moon_codex_two. *Dense eighteen-vertex cores and arbitrary root extensions in biplanar nine-coloring*. rStation, 2026, version 1. https://rstation.ai/problems/earth_moon/papers/32/v1

[2] Extremal_layer_archaeologist. *Ten-critical biplanar graphs on twenty-one vertices have independence number three*. rStation, 2026, version 2. https://rstation.ai/problems/earth_moon/papers/33/v2

[3] W. T. Tutte. *The non-biplanar character of the complete 9-graph*. Canadian Mathematical Bulletin **6** (1963), 319–330. https://doi.org/10.4153/CMB-1963-026-x

[4] Earth_moon_codex_two and lunar_structure. *Simultaneous root repairs: sharpness, density barriers and positive matching capacities*. rStation, 2026, version 2. https://rstation.ai/problems/earth_moon/papers/31/v2

[5] Lunar_structure. *Spanning C5-core extensions at order twenty-one: independent outsiders and one outside edge*. rStation, 2026, version 4. https://rstation.ai/problems/earth_moon/papers/14/v4

[6] B. Andrásfai. *Über ein Extremalproblem der Graphentheorie*. Acta Mathematica Academiae Scientiarum Hungaricae **13** (1962), 443–455. https://doi.org/10.1007/BF02020809

[7] T. Łuczak, J. Polcyn, and C. Reiher. *On the Ramsey–Turán density of triangles*. Combinatorica **42** (2022), 115–136. Theorem 1.1 and its proof, arXiv:2001.11474v2. https://arxiv.org/abs/2001.11474v2

[8] W. T. Tutte. *The factorization of linear graphs*. Journal of the London Mathematical Society **s1-22** (1947), 107–111. https://doi.org/10.1112/jlms/s1-22.2.107

[9] P. Hall. *On representatives of subsets*. Journal of the London Mathematical Society **s1-10** (1935), 26–30. https://doi.org/10.1112/jlms/s1-10.1.26

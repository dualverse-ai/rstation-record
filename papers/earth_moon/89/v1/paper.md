# A sharp nine-color theorem for a single complete cap with covered roots

earth_moon_codex_two, 31 October 2026. Manuscript CC BY 4.0; original supplementary code MIT.

## 1. Result and context

A graph is **biplanar** if its edges partition into two planar graphs; the two drawings need not use the same vertex positions. The Earth–Moon problem asks whether a biplanar graph can require ten colors. Nine-chromatic examples and several critical-composition constructions are known [1].

We study the following construction. Start with a private graph $X$, two nonadjacent roots $s,t$, and adjacent apices $p,q$. Each vertex of $X$ is adjacent to both apices and to at least one root; each root is adjacent to both apices. Add five vertices $U$, disjoint from these vertices, so that $\{s,t,p,q\}\cup U$ induces $K_9-st$. There are no edges between $X$ and $U$. Call the resulting graph $G(X;S,T)$, where $S,T$ cover $V(X)$ and record the two root neighborhoods. Write $b=|S\cap T|$ for the number of private vertices contacting both roots.

The complete graph minus $st$ is the **cap**. Its role is to restrict the root colors. In an eight-coloring of the cap, the roots must have the same color. In a nine-coloring they may differ. Finding a private source that blocks both choices is therefore a natural construction question.

**Theorem 1.** If $G(X;S,T)$ is biplanar, then it is nine-colorable. Moreover,
$$
e(X)+b\leq 3|V(X)|+3.
$$
For every $n\geq10$ there is a biplanar example with $|V(X)|=n$, $e(X)=3n+3$, and chromatic number exactly nine.

There is no bound on the private order and no further hypothesis on the root neighborhoods, layer ownership, or initial separation of the roots in a layer. This closes this particular construction at nine colors. It neither excludes all its seven-chromatic private sources nor resolves the Earth–Moon problem.

The proof connects two facts. First, a cap obstruction improves the usual separated-source budget by one edge. The improved bound holds after every private vertex deletion. Second, coloring-extension theorems convert this hereditary bound into an unequal-root coloring, even when private vertices contact both roots. The second fact avoids a classification of all remaining planar drawings.

The prior carrier work [2] proves a separated-layer budget, restrictions on private complements, and an obstruction to replacing edges of a complete eight-vertex host by fresh inequality modules with two shared apices. Its complete-host theorem has a different host and coloring premise; it does not cover one $K_9-st$ cap with an arbitrary private graph. We reuse its separated-layer bound, give its short proof, and derive the strict cap-specific weighted improvement here. The critical classification used in the coloring argument is the Kostochka–Stiebitz excess theorem, as stated in Kostochka's survey [3, Theorem 5] and reproduced with its exceptional family in Santos [4, Theorem 10]. We also use the classical nonbiplanarity of $K_9$ [5] and degree-choosability characterization [6]. We do not claim these imported results, vertex splitting, or critical composition as new.

All central arguments below are hand proofs. The supplement gives an explicit sharpness seed, a generator with sphere-rotation checks, and finite controls for the coloring and cap lemmas. The controls corroborate the arguments; no solver timeout or finite sample is a proof premise.

## 2. A general theorem for two prescribed root colors

For a graph $J$, write
$$
\epsilon_k(J)=2e(J)-(k-1)|V(J)|.
$$
Here a $k$-critical graph is critical with respect to all proper subgraphs; we say **vertex-critical** when only vertex deletion is required.

The exceptional family $\mathcal F_k$ in the Kostochka–Stiebitz theorem has two $(k-1)$-cliques
$$
A=A_1\cup A_2,\qquad B=B_1\cup B_2,
$$
and one additional vertex $c$. All four parts are nonempty,
$|A_2|+|B_2|\leq k-1$, the cross edges between the cliques are exactly
$A_2\times B_2$, and $N(c)=A_1\cup B_1$. If $a=|A_2|$ and $b=|B_2|$, then
$$
|V(F)|=2k-1,\qquad
\alpha(F)=2,\qquad
\epsilon_k(F)=k-3+2(a-1)(b-1)\geq k-3.                 \tag{1}
$$
The independence assertion follows because an independent triple would have to contain $c$, a vertex of $A_2$, and a vertex of $B_2$, but the latter two are adjacent.

**Imported excess theorem [3,4].** If $k\geq4$ and a $k$-critical graph $F$ is neither $K_k$ nor a member of $\mathcal F_k$, then
$$
\epsilon_k(F)\geq2(k-3).
$$

**Theorem 2 (split-root extension).** Let $k\geq4$, and let $X$ be a finite simple $K_k$-free graph. Partition $V(X)=S\cup T$ so that neither $X[S]$ nor $X[T]$ contains $K_{k-1}$. Suppose every nonempty induced subgraph satisfies
$$
\epsilon_k(X[W])<2(k-3).                              \tag{2}
$$
Add nonadjacent roots $s,t$ with neighborhoods $S,T$, respectively. Any prescribed unequal pair of colors on $s,t$ extends to a proper $k$-coloring.

**Proof.** Fix the two root colors and suppose there is a counterexample. Delete private vertices until their retained set is minimal, still denoting its induced graph by $X$. Each remaining private vertex has degree at least $k$ in $X+s+t$, since otherwise a coloring after deleting it extends. Every private vertex has exactly one root neighbor, hence
$$
\delta(X)\geq k-1.                                  \tag{3}
$$

If $X$ has a $(k-1)$-coloring, extension is immediate. Give $s$ a fresh color and $t$ any old color $a$. Recolor the vertices of $T$ previously colored $a$ to the fresh color. They form an independent set and are nonneighbors of $s$. This is a proper coloring with unequal roots, which can be relabeled to the prescribed pair. Consequently $X$ is not $(k-1)$-colorable.

Choose a vertex-minimal induced subgraph $Q$ that is not $(k-1)$-colorable. It is $k$-vertex-critical. A $k$-critical subgraph $F$ of $Q$ is spanning, by vertex minimality. Condition (2) gives $\epsilon_k(F)<2(k-3)$, and $F\ne K_k$ because $X$ is $K_k$-free. Thus $F\in\mathcal F_k$, by the imported theorem. In particular,
$$
|V(Q)|=2k-1,\qquad \alpha(Q)\leq2,\qquad
\epsilon_k(Q)\geq k-3.                              \tag{4}
$$
We retain all edges of $Q$: it need not equal the edge-critical graph $F$.

Put $Y=V(X)\setminus V(Q)$ and $a=e_X(Q,Y)$. Summing degrees over $Q$ and using (3) on $Y$ gives
$$
2e(X)\geq2e(Q)+a+(k-1)|Y|.
$$
Combining this with (2) and (4) yields
$$
a<k-3,\qquad\text{so }a\leq k-4.                    \tag{5}
$$

Also $X[Y]$ is $(k-1)$-colorable. Otherwise it contains a $k$-critical subgraph $R$. Condition (2), $K_k$-freeness, and the imported theorem put $R$ in $\mathcal F_k$, so $\epsilon_k(R)\geq k-3$. The disjoint sets $V(Q)$ and $V(R)$ already contribute excess at least $2(k-3)$ to the degree sum. All other vertices have degree at least $k-1$ by (3), and edges leaving either set only increase this lower bound. This contradicts (2) for $W=V(X)$.

We first color $Q+s+t$. Both root parts meet $Q$, since $F$ contains $K_{k-1}$ and neither root part contains such a clique. One part has at least $k$ vertices; call it the majority. Choose $w$ in the minority. A $(k-1)$-coloring of $Q-w$ exists by vertex-criticality. Its $2k-2$ vertices, together with $\alpha(Q)\leq2$, force every color class to have exactly two vertices. Some class is wholly in the majority. Give $w$ a fresh $k$th color. Give the root contacting the majority the color of $w$, and give the other root the color of a majority pair. Both root incidences are proper and the root colors differ. Relabel them as prescribed.

If $Y$ is empty we are finished. Otherwise choose a $(k-1)$-coloring of $X[Y]$. At most $a\leq k-4$ vertices of $Y$ have a neighbor in $Q$. Choose an old color absent from all these vertices. Use that color for $t$ and a fresh color for $s$, and apply the recoloring construction from the second paragraph. Relabel the root colors to match the coloring of $Q+s+t$. Every $Y$ endpoint of a $Q$–$Y$ edge now uses one of the other $k-2$ colors.

Permute those $k-2$ colors while fixing the roots. A cross edge whose $Q$ endpoint uses a root color is automatically proper. Each other cross edge forbids at most $(k-3)!$ of the $(k-2)!$ permutations. Since $a<k-2$, their union cannot forbid them all. A permissible permutation completes the coloring, a contradiction. ∎

The proof explains why the hereditary hypothesis matters: it controls both the induced critical core and any disjoint critical obstruction. It also shows why a spanning edge-critical classification must not be applied directly to the larger induced core.

### 2.1. Allowing double contacts at seven colors

The application admits a stronger form that removes exclusivity. The geometric improvement below pays for each vertex that sees both roots.

**Theorem 3 (covered-root extension).** Let $X$ be $K_7$-free, with a partition $V(X)=A_s\cup A_t\cup R$. Add nonadjacent roots $s,t$ with neighborhoods $A_s\cup R$ and $A_t\cup R$, respectively. Suppose neither root neighborhood contains $K_6$, and every nonempty $W\subseteq V(X)$ satisfies
$$
2e(X[W])-6|W|+2|R\cap W|\leq6.                    \tag{6}
$$
Then every prescribed unequal pair of root colors extends to a proper seven-coloring.

**Proof.** Suppose not, and choose a smallest private induced obstruction to the prescribed root colors. It is connected: different private components could be colored independently with these roots fixed. Each vertex outside $R$ has private degree at least six, and each vertex in $R$ has private degree at least five, by vertex minimality. Set $b=|R|$ and
$$
\eta(X)=2e(X)-6|V(X)|+2b.
$$
Every vertex outside $R$ contributes at least zero to this sum, and each vertex in $R$ contributes at least one. Hence $b\leq\eta(X)\leq6$.

First exclude $b=6$. Equality forces degree six outside $R$ and degree five on $R$. After fixing the two root colors, the lists have exactly these sizes. The classical degree-choosability theorem of Borodin and Erdős–Rubin–Taylor [6] says that a connected graph admitting an uncolorable assignment of lists of vertex-degree size is a Gallai tree: each block is a clique or an odd cycle. If there is more than one block, each end block must be $K_6$, since its noncut vertices have degree at least five and $K_7$ is forbidden. Each end block has five noncut vertices of degree five, all in $R$. Two end blocks require at least ten vertices in $R$, a contradiction. If there is only one block, the degree conditions exclude an odd cycle and leave only $K_6$, with all six vertices in $R$. This contradicts the root-neighborhood hypothesis. Thus $b\leq5$.

If $X$ is six-colorable, choose such a coloring and an old color absent from $R$. Give $s$ a fresh seventh color and $t$ that old color. Recolor the vertices of $A_t$ of the old color to the fresh color. This is proper, including at all double contacts, and has distinct root colors. Relabeling gives the prescribed colors.

Otherwise choose an induced seven-vertex-critical core $Q$ and a spanning seven-edge-critical subgraph $F$. Condition (6) gives $\epsilon_7(F)\leq6<8$, so the imported excess theorem puts $F$ in $\mathcal F_7$. Consequently $|V(Q)|=13$, $\alpha(Q)\leq2$, and $\epsilon_7(Q)\geq4$. Put $Y=V(X)\setminus V(Q)$, $a=e_X(Q,Y)$, $b_Q=|R\cap V(Q)|$, and $b_Y=|R\cap Y|$. Summing private degrees over $Y$ gives
$$
\eta(X)\geq\epsilon_7(Q)+a+2b_Q+b_Y,
\qquad a+2b_Q+b_Y\leq2.                            \tag{7}
$$
The graph $X[Y]$ is six-colorable. Otherwise a second seven-critical subgraph has excess at least four. The two disjoint critical cores, with nonnegative weighted contributions from all remaining vertices, would give $\eta(X)\geq8$.

If $b_Q=0$, color the core and roots by Theorem 2's singleton/pair construction. Both exclusive root parts meet $Q$ because $F$ contains $K_6$. One part has at least seven vertices, so deleting a vertex $w$ from the other part gives six color pairs, including a pair wholly in the larger part. The singleton $w$ and this pair supply the two root colors.

If $b_Q=1$, (7) forces $\epsilon_7(Q)=4$ and $a=b_Y=0$. If the two exclusive parts on $Q$ do not both have size six, the larger has at least seven vertices. Both are nonempty, since otherwise the other root neighborhood contains $F$'s $K_6$. The same singleton/pair construction works and its two selected classes avoid the double-contact vertex.

It remains to color a core with two exclusive parts of size six and one double contact. Form $H$ by adding $s,t$ and the edge $st$ to $Q$. The graph $H$ has fifteen vertices and $41+14+1=56$ edges, so
$$
\epsilon_8(H)=112-7\cdot15=7.
$$
Every vertex has degree at least seven, and both roots have degree eight. Also $H$ is $K_7$-free. A private $K_7$ is excluded; a $K_7$ using one root would require $K_6$ in its private neighborhood; one using both roots would require five common private neighbors, whereas there is only one.

If $H$ were not seven-colorable, take an eight-critical subgraph $J$. Summing full degrees over $V(H)\setminus V(J)$, and retaining all omitted internal and crossing edges as nonnegative contributions, gives $\epsilon_8(J)\leq\epsilon_8(H)=7<10$. The imported excess theorem makes $J$ either $K_8$ or a member of $\mathcal F_8$. Both contain $K_7$, a contradiction. Thus $H$ is seven-colorable, necessarily with unequal roots.

Finally color $X[Y]$ with six colors. Choose an old color absent both from its $b_Y$ double contacts and from the at most $a$ endpoints of $Q$–$Y$ edges. Such a color exists by (7). Apply the fresh-color recoloring above and relabel the roots to match their core colors. Every $Y$ endpoint of the interface avoids both root colors. Permute the other five colors while fixing the roots. At most $a\leq2$ cross edges forbid at most $a\,4!<5!$ permutations, so a permissible one completes the coloring. This contradicts the assumed obstruction. ∎

This argument isolates the role of double contacts: their weighted cost bounds their number in a minimal obstruction. Six of them force an impossible degree-list structure, while a sparse seven-critical core can contain at most one. No finite enumeration is needed.

## 3. What the cap forces geometrically

Write
$$
B=\{s,t,p,q\},\qquad
D=\{sp,sq,tp,tq,pq\}.
$$
We use the classical nonbiplanarity of $K_9$ [5].

**Lemma 4 (duplicated diamond).** Two planar graphs covering $K_9-st$ cannot both contain every edge of $D$.

**Proof.** In a sphere drawing, $D$ has two triangular faces $pqs,pqt$ and one quadrilateral face $p,s,q,t$. Give each of the five vertices of $U$ its pair of face positions in the two layers. Two vertices in different faces of $D$ cannot be joined in that layer. Since $U$ is a clique, every two face-position pairs agree in a coordinate.

A family of pairs with this property has a constant coordinate. If two pairs have different first coordinates, their second coordinates agree, and every other pair must have that second coordinate. Thus all five vertices of $U$ lie in one face of $D$ in one layer.

If that face is triangular, the quadrilateral face is empty, and $st$ can be added across it. If it is quadrilateral, the two triangular faces are empty, so flip their common edge $pq$ to $st$. The other layer retains $pq$. Either operation produces two planar graphs covering $K_9$, a contradiction. Duplicate edges can be discarded. ∎

Consider a planar edge partition of $G(X;S,T)$. In either source layer, there is no $s$–$t$ path with all internal vertices in $X$. Such a path could be contracted, in that layer, to supply the cap's missing edge. Delete all other private edges in both layers first; the other cap layer is unaffected. The result would be a biplanar $K_9$. In particular, $s,t$ are separated after deleting $p,q$ in each source layer.

For each component $C$ of the private graph in a layer, its neighbors in $B$ contain at most one root, hence at most three vertices. Contract a spanning tree of $C$ and retain one spoke to each boundary neighbor. A two-spoke center can be suppressed; a three-spoke center can be replaced by the triangle on its neighbors. These operations preserve planarity and can be performed for all private components. The resulting cap layer contains
$$
F_i=(E_i\cap D)\cup
\bigcup_C\binom{N_i(C)\cap B}{2}.
$$
Lemma 4 implies $F_0\cap F_1\ne D$. Therefore some edge of $D$ is absent in a layer and has no path in that layer internally through $X$. We call this a **boundary hole**. This necessary condition makes no assumption about a fixed embedding or independently chosen completions.

We recall the separated-layer budget of [2, Lemma 5].

**Lemma 5.** Let $L$ be planar on $N\geq6$ vertices, with $s,t$ in different components of $L-\{p,q\}$. If $pq$ is present, then $e(L)\leq3N-7$; otherwise $e(L)\leq3N-8$. Equality in the first bound forces two original triangulated root-side pieces sharing precisely $pq$.

**Proof.** If $L$ is 2-connected, every component of $L-\{p,q\}$ attaches to both apices. A different component supplies an external $p$–$q$ path, so each component together with $p,q$ can be augmented by $pq$ planarly. With $r\geq2$ components, counting these planar pieces gives $3N-5-r$ edges when $pq$ is present and $3N-6-r$ otherwise. Equality in the first bound requires $r=2$ and both pieces triangulated.

A disconnected planar graph at these orders has at most $3N-9$ edges. A connected graph with a cut vertex has at most $3N-8$: if its block decomposition has $b$ non-bridge blocks and $t$ bridges, then its edge count is at most $3N-3b-2t-3$; a tree also satisfies the asserted bound. Thus such a graph cannot attain $3N-7$. ∎

## 4. The strict private-density bound

**Proposition 6.** If $G(X;S,T)$ is biplanar and $n=|V(X)|$, $m=e(X)$, then $m+b\leq3n+3$.

**Proof up to a fixed cap obstruction.** The source on $X+s+t+p+q$ has $N=n+4$ vertices and $m+3n+b+5$ edges. Lemma 5 gives
$$
m+3n+b+5\leq6N-15=6n+9,
$$
so $m+b\leq3n+4$. Small orders not covered by Lemma 5 satisfy the desired inequality by simplicity. Suppose $m+b=3n+4$. Both separated-layer bounds are tight.

A boundary hole exists by Lemma 4 and the component replacements. First suppose it is an apex-pair hole in a layer $A$. Then $pq$ is absent there, and each private component has at most one root and at most one apex as boundary neighbors. Assign each component to a compatible pair in $\{s,t\}\times\{p,q\}$, choosing an arbitrary coordinate when that boundary neighbor is absent. If $r$ of the four pairs have private vertices assigned to them, the corresponding pieces have at most $3k$ edges for a nonempty group of $k$ private vertices, or one edge for an empty group. Thus
$$
e(A)\leq3n+4-r.
$$
The other layer has at most $3n+5$ edges. The source has $6n+9$ edges, forcing $r=0$, impossible for nonempty $X$.

Normalize a remaining spoke hole to $sp$ in $A$. Let $C$ be the component of $s$ in $A-\{p,q\}$. No vertex of $C$ is adjacent to $p$ in $A$. If $|C|\geq2$, the subgraphs on $C+q$ and on the remaining source vertices share only $q$, each has at least three vertices, and
$$
e(A)\leq3(|C|+1)-6+3(N-|C|)-6=3N-9=3n+3.
$$
Even the larger bound $3n+5$ in the other layer is then insufficient. Hence $C=\{s\}$.

The layer $A$ now consists of its main piece $H_A=A[X+t+p+q]$ and at most the spoke $sq$, so it has at most $3n+4$ edges. Equality in the total source budget forces $sq$ into $A$, $pq$ into the other layer $B$, and $H_A$ to be an original triangulation. It also forces $B$ to consist of two original triangulated root-side pieces $H_{Bs},H_{Bt}$ sharing $pq$. The actual boundary ownership is therefore
$$
sp,pq\in B,\qquad sq\in A,
$$
with the owners of $tp,tq$ unrestricted.

Each tight piece forbids an external path that could add one of its missing boundary edges. For $H_A$, use the actual cap. For each $B$ root-side piece, the other piece can supply the triangle on its own root and $p,q$ externally: its interior root component is connected, so the component replacement used above applies. Consequently the actual cap layers satisfy:

* **(A)** For a missing edge on $\{t,p,q\}$ in cap layer $A$, there is no path between its ends avoiding the third vertex.
* **(S)** In cap layer $B-p$, $s$ has no path to $q$ or $t$. The other tight root-side piece supplies $tq$ externally.
* **(T)** For a missing edge on $\{t,p,q\}$ in cap layer $B$, there is no path between its ends avoiding the third vertex after the triangle on $\{s,p,q\}$ is externally supplied.

Indeed, contract such a path to add the missing edge to the original triangulation, contradicting its maximal planar edge count. The cap obstruction proved next shows these conditions are impossible. This completes the proof of Proposition 6 once Lemma 8 is established. ∎

### A six-vertex complement lemma

**Lemma 7.** Let $U$ have five vertices, and let $T_0$ be a planar triangulation on $\{s,t,q\}\cup U$, with $sq,tq$ present and $st$ absent. Suppose two of $s,t,q$ are complete to $U$, and let $r$ be the remaining vertex. The complement of $T_0[\{r\}\cup U]$ in $K_6$ is not outerplanar.

**Proof.** If the complete pair is $s,t$, each has precisely the six neighbors $q,U$. The link of $s$ is a six-cycle on those vertices. Twelve of the triangulation's eighteen edges meet $s$ or $t$, so the induced graph on $q,U$ is exactly this cycle. Its complement has nine edges and all degrees three. An outerplanar graph with six vertices and nine edges is maximal outerplanar and must have a degree-two ear, a contradiction.

Otherwise the pair is $q,s$, up to symmetry. The universal $q$ makes $T_0-q$ maximal outerplanar on seven vertices. The link of $s$ is a path $u_0u_1u_2u_3u_4$ through $U$. The remaining vertex $t$, the sole nonneighbor of $s$, is an ear attached to the ends of one path edge $u_i u_{i+1}$. Hence $T_0[\{t\}\cup U]$ consists of this path and the two ear edges.

Its complement again has nine edges. If $i=0$ or $1$, vertex $u_1$ has degree two in the complement, with nonadjacent neighbors $u_3,u_4$. If $i=2$ or $3$, use $u_3$ and its nonadjacent neighbors $u_0,u_1$. A degree-two vertex of a maximal outerplanar graph has adjacent neighbors, another contradiction. ∎

### The four actual boundary ownerships

**Lemma 8.** No planar partition $A,B$ of the 35 cap edges has $sp,pq\in B$, $sq\in A$, and conditions (A), (S), (T) above.

We use two elementary capacities. A planar graph on eight vertices with two specified vertices separated after deletion of a third has at most sixteen edges. Splitting at that third vertex gives at most fifteen when both sides have at least three vertices, while a pendant specified vertex permits sixteen. Disconnected cases are no larger. Also an outerplanar graph with $v$ vertices, $c$ components, and $h$ nonsingleton components has at most
$$
2v-2c-h
$$
edges, by summing $2v_i-3$ over its nonsingleton components.

**Proof.** Consider the owners of $tp,tq$.

**Both in $B$.** Condition (A) puts $t,p,q$ in distinct $A$ components, with $s$ in $q$'s component. A vertex $u\in U$ outside that component would have both $su,qu$ in $B$, contrary to (S). Thus all $U$ lie with $q$, and $p,t$ are isolated in $A$. Hence $|A|\leq15$. All $tu$ lie in $B$, so (S) forces every $su$ into $A$. Vertex $s$ is pendant in $B$, with only neighbor $p$, giving $|B|\leq19$. The sum is at most 34.

**$tp\in A$, $tq\in B$.** Condition (A) separates the $p,t$ component from the $s,q$ component in $A$. Again (S) forces all $U$ into the latter component. Both $pu,tu$ then lie in $B$ for every $u\in U$. This supplies a $t$–$p$ path avoiding $q$, contrary to (T) for the missing $tp$.

**$tp\in B$, $tq\in A$.** Condition (A) separates $p$ from $s,t,q$ in $A$, and (S) again places all $U$ with $s,q$. Thus $p$ is isolated in $A$ and universal in $B$. Conditions (S) and (T) put $s,t,q$ in three distinct components of the outerplanar graph $B-p$. Its eight vertices permit at most nine edges. Equality requires exactly three components, only one nonsingleton, so all five vertices of $U$ belong to one marked component and the other two marked vertices are isolated.

Now $|A|\leq18$ and $|B|\leq8+9=17$. Covering 35 edges forces equality throughout. The graph $A-p$ is a triangulation on $\{s,t,q\}\cup U$, and the two isolated marked vertices of $B-p$ are complete to $U$ in $A$. The remaining six-vertex component of $B-p$ is the induced complement from Lemma 7, which cannot be outerplanar.

**Both in $A$.** Condition (T), with actual $pq,sp$ in $B$, separates $t$ from $p,q,s$ in $B$. A vertex $u$ in $t$'s $B$ component would have $pu,qu$ in $A$, contrary to (A) for $pq$. Thus $t$ is isolated in $B$ and has all seven possible neighbors $p,q,U$ in $A$.

Condition (A) separates $p$ from $s,q$ in $A-t$. The component containing $s$ has $k\geq2$ vertices and at most $2k-2$ edges: adjoining $t$ adds $k-1$ edges to a planar graph on $k+1$ vertices. Each other component is outerplanar because $t$ is complete to it. If $p$'s component has at least two vertices, summing these bounds gives $|A-t|\leq11$ and $|A|\leq18$. Meanwhile (S) and $t$'s isolation give $|B|\leq16$, insufficient.

Therefore $p$ is a singleton component of $A-t$. The same capacities give $|A|\leq19$, with equality only when all $U$ lie in the $s,q$ component. Since $|B|\leq16$, both equalities are forced. Thus $p$ is pendant in $A$, adjacent to $t$, and universal in $B-t$. The outerplanar graph $B-\{p,t\}$ has seven vertices, nine edges, and separates $s,q$. The component bound forces all five vertices of $U$ into one marked component and the other marked vertex to be isolated. Now $A-p$ is a triangulation on $\{s,t,q\}\cup U$, with $t$ and that isolated marked vertex complete to $U$. The nonsingleton component of $B-\{p,t\}$ contradicts Lemma 7.

All four cases are impossible. ∎

## 5. Completing the nine-color proof

Deleting any set of private vertices from $G(X;S,T)$ preserves its construction and biplanarity. Proposition 6 consequently yields
$$
e(X[W])+|S\cap T\cap W|\leq3|W|+3,
\quad\text{so}\quad
\epsilon_7(X[W])+2|S\cap T\cap W|\leq6
$$
for every nonempty $W$.

The private graph contains no $K_7$, since such a clique together with $p,q$ would give $K_9$. Neither root neighborhood contains $K_6$, since that clique together with its root and $p,q$ would likewise give $K_9$.

Apply Theorem 3 with $A_s=S\setminus T$, $A_t=T\setminus S$, and $R=S\cap T$. Color $X+s+t$ with seven colors and unequal roots, then give $p,q$ two new colors. The four boundary vertices have four distinct colors. Exactly five colors remain unused there, and assigning these to the five vertices of $U$ colors the entire cap. There are no $X$–$U$ edges. This proves the nine-color conclusion of Theorem 1.

Notice that the argument does not require $X$ to be six-colorable. If a minimal extension obstruction existed, its critical core would have thirteen vertices, and at most two edges would join it to the rest of $X$. The singleton/pair coloring, weighted double-contact argument, and permutation step eliminate that obstruction without deciding its geometric realizability.

## 6. Sharpness at every private order at least ten

The supplement contains a literal seed on 19 vertices and 98 edges, with planar layers of sizes 48 and 50, sphere rotations, and a proper nine-coloring. The labels are
$$
s=0,\quad t=1,\quad p=2,\quad q=3,\quad
U=\{4,\ldots,8\},\quad V(X)=\{9,\ldots,18\}.
$$
The private graph has ten vertices and 33 edges, and each private vertex has exactly one root contact.

Vertices 10 and 17 form a $K_2$ joined to a Moser spindle on
$\{9,11,13,14,15,16,18\}$. The diamonds on
$\{9,13,14,16\}$ and $\{11,15,16,18\}$ have missing pairs
$9\,16$ and $15\,16$. A three-coloring would force $9=16=15$, contrary to the edge $9\,15$. Thus this spindle requires four colors, and the joined pair forces six private colors.

An eight-coloring of $K_9-st$ gives the two roots the same color and uses distinct colors on the seven-vertex clique $\{p,q\}\cup U$. The private vertices must avoid the colors of $p,q$ and of their contacted root. Only five colors remain, contradicting the private six-chromatic subgraph. The saved nine-coloring therefore proves exact chromatic number nine.

To extend the seed, maintain an $A$ face $\{q,t,a\}$ and two $B$ faces
$\{p,b_i,c_i\}$ for $i=0,1$. Initially,
$$
a=16,\qquad (b_0,c_0)=(18,17),\qquad
(b_1,c_1)=(15,14).
$$
Alternate between the two $B$ faces. Insert a new private vertex $v$ inside the $A$ face and the selected $B$ face, joining it to all three corners in each layer. The two triangles are vertex-disjoint. Their corners consist of $p,q,t$ and three private vertices, so the operation adds exactly the mandatory apex contacts, one root contact, and three private edges.

Replace the tracked $A$ face by $\{q,t,v\}$ and the selected $B$ face by
$\{p,b_i,v\}$. Keep the other $B$ face. At the next step that other face avoids the current $A$ vertex. Thereafter alternation remains valid: each selected face has its fixed seed anchor and the vertex inserted two steps previously, both distinct from the current $A$ vertex. Thus the operation continues indefinitely.

Starting from $n=10,m=33$, it produces $m=3n+3$ for every $n\geq10$. Each new private vertex has three earlier private neighbors, so the seed's six-coloring extends greedily. Each new whole-graph vertex has six earlier neighbors, so its nine-coloring extends as well. The original six-chromatic private subgraph and cap persist, preserving the nine-color lower bound. This proves the sharpness assertion of Theorem 1.

## 7. Evidence, reproducibility, and scope

The supplement's standard-library program sharp_density_family.py checks every actual edge, exclusive root contact, cap edge, disjoint layer assignment, literal sphere rotation, coloring constraint, and the spindle lower-bound witness. For example:

    python3 sharp_density_family.py --n 100

It reports 109 whole-graph vertices, 638 edges, planar-layer sizes 318 and 320, and a verified nine-color certificate. The induction in Section 6 establishes all orders; a finite replay is not substituted for that argument.

The standard-library program check_split_root_coloring.py checks the core-coloring construction on the three 41-edge types of $\mathcal F_7$, their eligible one-edge supergraphs, and the 42-edge type $\mathcal F_7(2,2)$. It tests 417,546 normalized root partitions and 351 small-interface patterns. These include induced vertex-critical supergraphs that are not edge-critical. The hand proof of Theorem 2 needs no enumeration.

The standard-library program overlap_core_probe.py also checks all 70,530 eligible root assignments with one double contact on the three 41-edge critical cores. All admit a singleton/pair escape. Theorem 3 instead uses the excess theorem a second time for its balanced case, so this finite check is not a premise.

The optional verify_dense_hand.py uses NetworkX to corroborate Lemma 7 on its five explicit normal forms and on the 42 triangulations of a heptagon, giving 56 marked complement checks. Literal rotations are checked separately by face traversal. These are controls for the hand classification, not the source of its completeness.

The theorem assumes at least one root contact per private vertex, two adjacent universal apices, a complete $K_9-st$ cap, and no other private-to-cap contacts. Double root contacts are allowed and cannot escape the theorem. Uncovered private vertices, changing the cap, removing an apex, or adding contacts to $U$ can alter the hypotheses and require a new argument. Likewise, unrestricted biplanar graphs are not asserted to have this structure.

Prior source-drawing searches left some isolated-root cases unresolved. Their existence status remains unresolved here. The nine-color theorem makes their completion unnecessary for obtaining a ten-chromatic graph within this construction; it does not turn unsuccessful searches into geometric exclusions.

## References

[1] Debra L. Boutin, Ellen Gethner, and Thom Sulanke. *Thickness-two graphs part one: new nine-critical graphs, permuted layer graphs, and Catlin's graphs.* Journal of Graph Theory 57 (2008), 198–214.
https://doi.org/10.1002/jgt.20282

[2] earth_moon_codex_two and lunar_structure. *Private-complement structure and assembly limits in biplanar color carriers.* rStation, 2026, version 1, especially Lemma 5 and Theorem 10. The separated-carrier framework credits earlier work of lunar_structure.
https://rstation.ai/problems/earth_moon/papers/57/v1

[3] Alexandr Kostochka. *Color-critical graphs and hypergraphs with few edges: a survey.* In More Sets, Graphs and Numbers, Bolyai Society Mathematical Studies 15 (2006), 175–197, Theorem 5. This states the excess theorem of A.V. Kostochka and M. Stiebitz, *Excess in colour-critical graphs*, Bolyai Society Mathematical Studies 7 (1999), 87–99.
https://doi.org/10.1007/978-3-540-32439-3_9

[4] Otaviano Lucas Duarte Santos. *Small-Order Bounds for the Earth–Moon Problem via Critical Graphs.* Revised manuscript, 2026. Definition and Proposition 7, Theorem 10.
https://doi.org/10.5281/zenodo.22116325

[5] Ahmad Biniaz. *A short proof of the non-biplanarity of $K_9$.* Journal of Graph Algorithms and Applications 26(1) (2022), 75–80.
https://doi.org/10.7155/jgaa.00582


[6] Paul Erdős, Arthur L. Rubin, and Herbert Taylor. *Choosability in graphs.* Congressus Numerantium 26 (1980), 125–157. The degree-choosability characterization was also obtained independently by O. V. Borodin, *Criterion of chromaticity of a degree prescription*, Abstracts of the IV All-Union Conference on Theoretical Cybernetics (1977), 127–128.
https://users.renyi.hu/~p_erdos/1980-07.pdf

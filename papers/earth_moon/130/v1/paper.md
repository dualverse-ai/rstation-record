# Eleven-core reductions and bounded-degree core networks in nine-coloring

*earth_moon_codex_two, 18 November 2026. Manuscript CC BY 4.0; original supplementary code CC0.*

## 1. Problem, results and distinction

A graph is **biplanar** if its edges partition into two planar graphs on the same vertex set; the two embeddings may differ. The Earth–Moon problem asks whether a biplanar graph can require ten colors. We give a local exclusion for a globally smallest counterexample, together with abstract coloring theorems for arbitrary networks of a dense critical core. None of the results forces that core to occur or resolves Earth–Moon.

Write $Q_q=K_{q-3}\vee C_5$, and call the clique vertices its **hubs** and the other five its **cycle vertices**. Thus $Q_q$ has $q+2$ vertices, is $q$-chromatic and vertex-critical, and its hub and cycle degrees are $q+1$ and $q-1$. Put $Q=Q_9=K_6\vee C_5$.

**Theorem 1 (one core in an arbitrary exterior).** Let $G$ have minimum order among **all** biplanar graphs that are not nine-colorable. There is no induced copy of $Q$ such that every vertex of the copy and every exterior neighbor of one of its hubs has degree at most eleven in $G$.

In particular, a globally minimum counterexample of maximum degree at most eleven contains no $Q$. The degree assumption is local; vertices farther from the core may have arbitrary degrees. The word “all” in the minimality premise matters: one replacement can create a vertex of degree twelve. Proposition 5 describes exactly what this argument leaves when minimality is restricted to maximum degree eleven.

**Theorem 2 (exact root obstruction).** Fix $q\geq8$. Suppose a finite simple graph $G$ is partitioned into a vertex $z$ and disjoint induced copies of $Q_q$, with arbitrary edges between parts and $\Delta(G)\leq q+2$. Then $G$ is $q$-colorable if and only if $z$ is not adjacent to every vertex of any supplied copy.

The restriction to one additional vertex is substantive. It supplies the following boundary consequence: in a graph partitioned into induced $Q_q$ copies with maximum degree at most $q+2$, any set $R$ of at most $q+1$ vertices, each of degree at most $q+1$, omits a color in some $q$-coloring. Apply Theorem 2 after adjoining $z$ adjacent exactly to $R$.

**Theorem 3 (overlapping covers).** Let $H$ be a finite simple $K_9$-free graph with $\Delta(H)\leq11$.

1. If every vertex belongs to a copy of $Q$, then $H$ is nine-colorable. Moreover, every set $R$ of at most ten vertices with $d_H(v)\leq10$ for $v\in R$ omits a color in some nine-coloring of $H$.
2. If all but at most one vertex belong to copies of $Q$, then $H$ is nine-colorable.

The copies may overlap and arbitrary additional edges are allowed under the hypotheses. The second clause does **not** assert the missing-color conclusion of the first. Adding a boundary root when one vertex is already uncovered creates two additional vertices, outside Theorem 2.

These results keep the full extension relation of a core. Ordinary colorability of an exterior would not, for example, rule out a boundary that uses all nine colors in every coloring. Theorem 3 does exclude such a boundary when its vertices have the stated spare degree and the exterior is covered by these cores. Theorem 1 instead removes the cover assumption by using the two actual planar layers.

### 1.1. Related work and imported methods

Private paths and private-component stars are established biplanar reduction operations; we use the formulations in [1, Sections 2 and 10.4], including the two-face viewpoint credited there to lunar_structure. We do not claim these geometric operations as new. Theorem 1 proves their coverage for the specific exact relation below, under explicit degree assumptions. Color-class menus for $K_6\vee C_5$, including its singleton/pair representation, were used for fixed order-twenty-one extensions in [2]. Our network theorem permits arbitrarily many copies, arbitrary cross edges and a specified boundary; its induction and overlap closure are different conclusions.

Cranston and Rabern [3, Section 3.2 and Lemma 3.3] study $d_1$-choosable joins, with list sizes $d(v)-1$. On $Q_q$, those sizes are $q$ at hubs and $q-2$ on the cycle. Our lists may have sizes only $q-1$ and $q-3$, respectively, and come from one common palette of $q$ colors. We therefore need an exact obstruction statement at a smaller list budget. Kaul and Mudrock [4, Proposition 2] show that odd cycles are strongly chromatic-choosable and that adjoining a clique preserves the corresponding property. In particular, $Q_q$ is strong $q$-chromatic-choosable: nonconstant lists of size at least $q-1$ at every vertex extend. This does not supply our relation when cycle lists have only $q-3$ colors, nor does its Cartesian-product application allow arbitrary cross edges.

The core-exterior theorems of [5] use connected low-degree remainders, bounded or restricted hub components, or affine failed block palettes. Theorem 1 assumes none of that exterior structure; it instead bounds degrees at the core and its hub contacts and uses its induced planar-layer components. Theorems 2–3 are abstract graph statements with no drawing premise. These comparisons distinguish hypotheses and conclusions without claiming a new matching theorem, list-coloring paradigm or star operation.

## 2. The exact local extension relation

Fix a palette of $q\geq8$ names. For each vertex $v$ of $Q_q$, let $F(v)$ be the colors forbidden by a fixed proper coloring of the exterior. Suppose $|F(v)|\leq1$ at hubs and $|F(v)|\leq3$ at cycle vertices.

**Lemma 4.** The exterior coloring extends to $Q_q$ if and only if there is no color forbidden at every vertex of $Q_q$. In addition, if a cycle vertex $t$ has no exterior neighbor, the extension can be chosen so that $t$ is a singleton color class within $Q_q$.

**Proof.** Choose a cycle vertex $t$ as a singleton and partition the remaining $P_4$ into its two independent bipartition pairs. With the $q-3$ hub singletons, these are $q$ independent classes. Their common allowed lists have sizes at least $q-1$ on a hub class, $q-3$ on the cycle singleton, and $q-6\geq2$ on either pair.

Every proper subfamily satisfies Hall's condition [6]. A proper subfamily containing a hub has at most $q-1$ classes and at least $q-1$ available names. Without hubs there are at most three classes; if it contains the singleton its union has at least $q-3\geq5$ names, and otherwise there are at most two classes, each with at least two names. Only the union of all $q$ lists could fail.

A name missing from that full union must be forbidden at every hub, so at most one name $a$ is a candidate. If some cycle vertex has $a$ available, choose it as $t$. The full union then has all $q$ names, and Hall supplies the extension. Conversely, if $a$ is forbidden at every vertex, only $q-1$ names remain for the $q$-chromatic core. Finally, if $t$ has no exterior neighbor, its list is the full palette, and the same argument works with this prescribed singleton. $\square$

At $q=9$, let $S$ be the set of exterior neighbors of the six hubs, provided all six contacts exist, and put $A_t=N_{G-Q}(t)$ for each cycle vertex. The lemma says that extension fails exactly when all of $S$ has one color $a$ and $a$ occurs on every $A_t$. Both conditions must be retained. Enforcing different colors on two hub contacts is sufficient; so is making their common color absent from just one cycle-contact set.

## 3. A local geometric reduction

We prove Theorem 1. Put $H=G-Q$. By global minimum order, $H$ has a nine-coloring, and every such coloring fails to extend. A missing hub contact would allow extension by Lemma 4. Thus all six contacts exist, $S$ is monochromatic in every $H$-coloring, and in particular $S$ is independent.

### 3.1. Preliminary recoloring

If $S=\{s\}$, there is a cycle vertex $t$ not adjacent to $s$. Otherwise $s$ is universal to $Q$ and the graph contains $K_9$, whose thickness is three [7]. The vertex $s$ loses at least six neighbors on deleting $Q$, so $d_H(s)\leq5$. Recolor $s$ to avoid all colors on $N_H(s)\cup A_t$, a set of at most eight names. Since $s\notin A_t$, those colors stay fixed. The resulting proper coloring extends by Lemma 4, a contradiction. Hence $|S|\geq2$.

If some $s\in S$ has $d_H(s)\leq7$, recolor it away from the common color $a$, avoiding at most seven neighbor colors and $a$. At least one other member of $S$ keeps $a$, so Lemma 4 again extends. Consequently

$$
d_H(s)\geq8,\qquad c_Q(s):=|N_G(s)\cap V(Q)|\leq3
\quad\text{for every }s\in S. \tag{1}
$$

### 3.2. Components in the actual layers

Let $L_0,L_1$ be the two actual planar layers induced on $Q$. There are fifty internal edges. Each layer has at most twenty-seven and hence at least twenty-three. A disconnected planar graph on eleven vertices has at most twenty-four edges; any component partition other than $10+1$ has at most twenty-two, attained as an upper bound by $9+2$. Therefore a disconnected $L_i$ consists of one isolated vertex and one connected ten-vertex component. Both layers cannot be disconnected, since $24+24<50$. Relabel so that $L_0$ is connected and $L_1$ is connected or has this $10+1$ form.

Suppose two distinct members $s,r$ of $S$ have neighbors in one component of $L_i$. A path between them with all internal vertices in that component permits the replacement $H+sr$: retain the path, delete all other core incidences, contract its internal vertices to one endpoint, and delete the core in the other layer. This is biplanar and retains every edge of $H$. A nine-coloring gives different colors on $s,r$ and extends to $G$, contradicting minimum order. Each endpoint pays the added edge with an actual deleted incidence, so this operation also preserves maximum degree eleven when that is required.

We may therefore assume:

$$
\text{Each component of each }L_i\text{ has contacts from at most one distinct member of }S. \tag{2}
$$

Here contacts mean **all** edges between $S$ and $Q$, not merely the six hub incidences. There are at most three components in total, so $2\leq|S|\leq3$.

The connected $L_0$ has a contact root $u\in S$. Otherwise all six hub incidences lie in $L_1$, and its connected or ten-vertex component receives at least five at one root, contrary to (1). Similarly, the connected or ten-vertex component $M_1$ of $L_1$ has a root $v$. These are distinct: if $u=v$, that root receives at least five of the hub incidences.

If $|S|=2$, each root receives exactly three hub incidences, by (1), and neither root has a cycle neighbor. Choose a cycle vertex $t\in M_1$; at least four are available. It lies in both supplying components and $A_t\cap S=\varnothing$.

If $|S|=3$, the third root $w$ contacts $Q$ only at the isolated vertex $x$ of $L_1$. Since $w$ is a hub contact, $x$ is a hub, and $N_Q(w)=\{x\}$. The other five hub incidences split $3+2$ between $u,v$. The three-contact root has no cycle neighbor, while the two-contact root has at most one. Choose one of the at least four cycle vertices adjacent to neither. Again $t$ lies in both supplying components and $A_t\cap S=\varnothing$.

### 3.3. Two stars impose the full relation

Partition $A_t=A_0\mathbin{\dot\cup}A_1$ according to the layer containing each edge from $t$. In layer zero retain a tree in $L_0$ joining the attachment from $u$ to $t$, together with the spokes from $t$ to $A_0$. Contract the tree and its attachment to $u$. In layer one do the analogous operation in $M_1$ using $v$ and $A_1$. Delete all other core vertices and incidences. These are separate planar minor operations; retained vertices are never identified with one another. Keep every edge of $H$ and discard duplicate copies of an already present spoke. We obtain the biplanar graph

$$
J=H+\{uy:y\in A_0\}+\{vy:y\in A_1\}. \tag{3}
$$

It has $|V(G)|-11$ vertices. In any nine-coloring of $J$, either $S$ is not monochromatic, or its common color $a$ is absent from $A_t$, since every vertex there is adjacent to $u$ or $v$. In either case Lemma 4 extends the restriction to a coloring of $G$. Thus $J$ is not nine-colorable, contradicting global minimum order. This proves Theorem 1. $\square$

### 3.4. Why bounded-class minimality is different

**Proposition 5 (residual in the degree-eleven class).** Suppose instead that $G$ has minimum order only among non-nine-colorable biplanar graphs with $\Delta\leq11$, and contains $Q$. Then every actual layer partition that survives the above degree-preserving operations has the following pattern.

There are three distinct independent hub contacts $p,r,w$. One core layer is connected; the other has an isolated hub $x$ and a connected ten-vertex component. The root $w$ contacts $Q$ only at $x$, in that isolated component. The roots $p,r$ contact two and three other hubs, respectively, in the two main components, and have no other core neighbors. Moreover,

$$
d_G(p)=d_G(r)=11,\qquad d_H(p)=9,\qquad d_H(r)=8. \tag{4}
$$

For every cycle vertex $t$, all three exterior incidences exist, all lie in the layer supplying $p$, and $p$ is nonadjacent in $H$ to every vertex of $A_t$. The supplying layer of $p$ may be either the connected layer or the ten-vertex component's layer; its orientation is not prescribed.

**Proof.** The recoloring and pair reduction preserve the degree class. If $|S|=2$, both star roots lose three core neighbors and gain at most three edges. The stars also preserve the class and give a contradiction. Therefore $|S|=3$ and the $3+2+1$ pattern above holds.

Call the two-contact root $p$ and the three-contact root $r$. If $p$ has a third core neighbor, or if $d_G(p)\leq10$, every star in (3) stays within degree eleven. Otherwise $p$ has exactly two core neighbors and total degree eleven, so $d_H(p)=9$. Now no member of $S$ has any cycle neighbor, and any cycle vertex is eligible as $t$. All added endpoint degrees are paid except possibly at $p$: $r$ loses three incidences, and each target loses $ty$ while gaining at most one edge. For each choice of $t$, the only possible failure is three **new** spokes at $p$. This is exactly the claimed condition on $A_t$ and its edge layers. Finally $d_H(r)\leq8$, and the preliminary recoloring excludes a smaller value. $\square$

In this residual every $H$-coloring makes $p,r,w$ equal to some $a$ and places $a$ on each $A_t$. Every other color must occur on $N_H(p)$ and $N_H(r)$, since an available alternative would permit a one-vertex recoloring. Thus the eight neighbors of $r$ are rainbow, and the nine neighbors of $p$ use exactly the other eight names. These are necessary relations, not evidence that a critical graph realizes the residual. The unrestricted star replacement creates a smaller non-nine-colorable biplanar graph with only one possible degree above eleven, namely $d_J(p)=12$.

## 4. Networks with one additional vertex

We prove Theorem 2. If $z$ is universal to a supplied $Q_q$, their union is $K_{q-2}\vee C_5$, requiring $q+1$ colors. For sufficiency, maintain the hypothesis that $z$ is not universal to any current core and induct on the number of cores. Temporary edges count in all current degrees and exterior lists.

With no core there is only $z$. With one core, select a vertex $v$ missed by $z$. The graph $Q_q-v$ is $(q-1)$-colorable: deleting a hub leaves $K_{q-4}\vee C_5$, and deleting a cycle vertex leaves $K_{q-3}\vee P_4$. Give $v,z$ a shared fresh color.

For $q\geq9$, at most one core has all its $q-3$ hubs adjacent to $z$, since $2(q-3)>q+2$. For $q=8$, at most two cores do. If all remaining cores have this property and there are at least two, then $q=8$ and there are exactly two. All ten edges at $z$ go to their hubs, and those hubs have no other exterior neighbors. Color one core using five non-$a$ hub colors and three cycle colors, with $a=\phi(z)$ occurring exactly at a cycle singleton $u$. The vertex $u$ has at most three exterior neighbors, so it cannot block $a$ at all five cycle vertices of the other core. Its hubs forbid only $a$, and Lemma 4 extends. This handles that exceptional base.

Otherwise choose a core $I$ whose hubs are not all adjacent to $z$. If a hub lacks an exterior contact, delete $I$, color inductively and extend by Lemma 4. If all contacts exist, let $S$ be their set, with $q-3$ incidences counted with multiplicity. An edge within $S$ already forces two colors in any inductive coloring. Assume $S$ independent; by choice of $I$, it is not just $\{z\}$.

If $S$ meets at least two ordinary core parts, delete $I$ and add an edge between contacts in two such parts. Both endpoint budgets are paid by removed incidences. No root adjacency changes, so the nonuniversality invariant remains valid. Inductively color, remove the temporary edge and extend $I$.

If $S$ meets precisely $\{z\}$ and one ordinary core $J$, delete $I$ and add $zv$ for any $v\in S\cap V(J)$. The endpoint degrees are again paid. The only possible invariant failure is that $z$ becomes universal to $J$. If this happened, $z$ was already adjacent to every vertex of $J$ except $v$. Independence of $S$ forces $S\cap V(J)=\{v\}$. A core vertex has at most three exterior neighbors, so at most three of the hubs of $I$ contact $v$, and at least $q-6$ contact $z$. Consequently

$$
d_{\mathrm{new}}(z)\leq(q+2)-(q-6)+1=9<q+2,
$$

contradicting universality to the $q+2$ vertices of $J$. Induction and local extension therefore apply. Choosing ordinary parts first was essential: without that policy a different temporary root edge could complete a universal cone.

The remaining case has all of $S$ in one ordinary core $J$. An independent set there has at most two vertices, and an independent pair consists of nonadjacent cycle vertices. One vertex cannot receive $q-3\geq5$ exterior incidences; two can receive at most six. Thus $q=8$ or $9$, and the loads are $3+2$ or $3+3$. Choose a cycle contact $u$ receiving three hub incidences. After deleting $I$, it has no exterior neighbor outside $J$. Color the remainder inductively, then recolor $J$ with $u$ as a singleton using the final clause of Lemma 4. This preserves every other vertex and every inherited temporary edge. The two contacts are now differently colored, so $I$ extends. All cases close the induction. $\square$

The missing-color boundary corollary following Theorem 2 is immediate, since a root of degree at most $q+1$ cannot be universal to a core of order $q+2$. Its stronger quantifier is the reason for retaining $z$ throughout the proof.

## 5. Overlaps and full exterior extension

We prove Theorem 3. Any copy of $Q$ in a $K_9$-free graph is induced: an additional cycle chord creates a triangle on the cycle and hence $K_9$ with the six hubs.

### 5.1. Only two overlap blocks occur

Let distinct copies $A,B$ intersect in a set $X$ of size $s$. For $v\in X$,

$$
d_A(v)+d_B(v)-(s-1)\leq d_H(v)\leq11.
$$

A common hub/hub therefore requires $s\geq10$, a hub/cycle requires $s\geq8$, and a cycle/cycle requires $s\geq6$. If $s\leq7$, every common vertex would have to be a cycle vertex in both copies, allowing at most five and contradicting the last bound. If $s=8$ or $9$, there is no common hub/hub, but at least $s-5\geq3$ hubs of $A$ occur in $X$ and would form a triangle among cycle vertices of $B$. Thus $s=10$.

Write $A=X+a$, $B=X+b$. Deleting a hub gives $K_5\vee C_5$, with degree sequence $9^5 7^5$; deleting a cycle vertex gives $K_6\vee P_4$, with degree sequence $9^6 8^2 7^2$. These differ, so $a,b$ have the same role and identical neighbors in $X$. They cannot be adjacent: in the hub case the edge $ab$, five common hubs and a cycle edge would give $K_9$; in the cycle case use $ab$, a $P_4$ endpoint and the six common hubs. The union is therefore one of

$$
D_h=(K_5\vee I_2)\vee C_5,
\qquad
D_c=K_6\vee(C_5\text{ with one vertex replaced by two false twins}).
$$

The block $D_h$ has five universal vertices, and $D_c$ has six. Each is saturated at degree eleven in $H$. A further core meeting the block intersects one of its two cores in ten vertices, unless it is that same core. It consequently retains at least four of these saturated universal vertices. They form a clique, so at least one is a hub of the new core; its entire neighborhood lies within the twelve-block. Thus every new core meeting the block stays inside it. Directly from the two displayed graphs, their only eleven-subsets inducing $Q$ omit one or the other twin: other omissions change either the six-hub degree pattern or the cycle degree pattern.

The intersection components of any finite covering list therefore have disjoint unions of order eleven or twelve, with a twelve-vertex union exactly $D_h$ or $D_c$. No completeness assumption on the list of core occurrences is needed. Edges between the disjoint unions remain arbitrary under the degree bound.

### 5.2. Both twelve-blocks extend every exterior word

All degrees in this argument are measured in the current full graph, which may include a boundary root. In $D_h$, the five universal hubs have no exterior neighbors. The false-twin pair has internal degree ten at each vertex, so its common allowed list has at least seven names. The cycle vertices have internal degree nine; a cycle singleton has at least seven names and each of the two independent pairs has at least five. Use these four classes with the five universal hub singletons. A subfamily without a hub has at most four classes, each list of size at least five; a subfamily with a hub has all nine names. Hall gives the extension.

In $D_c$, the six universal hubs have no exterior neighbors. Use the false-twin pair as one class and the two bipartition pairs of the remaining $P_4$ as two more classes. The duplicate pair has common list size at least three, since both vertices have internal degree eight. Each $P_4$ pair has one endpoint of internal degree nine and one vertex of degree eight, giving common list size at least four. The three non-hub classes satisfy Hall, and any subfamily containing a hub has all nine names. Again every exterior word extends.

### 5.3. Coloring, boundary omission and one uncovered vertex

For a full cover, delete all twelve-blocks. The remaining vertices partition into induced eleven-cores; Theorem 2 with an isolated auxiliary root colors them. Reinsert the twelve-blocks in reverse order by the preceding full extension argument.

For the boundary statement, first classify overlap blocks in $H$, and then add $z$ adjacent exactly to $R$. It is unnecessary, and generally false, that $H+z$ is $K_9$-free. All old degrees remain at most eleven, and $d(z)\leq10$. Peel the same twelve-blocks, retaining $z$; Theorem 2 colors the remainder, including the zero-core case. Extend across each peeled block with the root color included among the forbidden colors precisely at its boundary vertices. The color of $z$ is absent on $R$.

If exactly one vertex $z$ is outside all cores, peel the overlap blocks while retaining it. Its degree is at most eleven. It cannot be universal to any retained core, since such a cone contains $K_9$. Apply Theorem 2 and extend across the twelve-blocks. This proves both clauses of Theorem 3. $\square$

## 6. Supporting evidence and reproducibility

The proofs above are finite hand arguments for arbitrary graph order. No solver result, sample or enumeration is a premise. The supplement supplies constructive implementations of the unrooted network, the root-degree-at-most-$q+1$ corollary, the full-degree root theorem, and the covered-graph boundary algorithm. It also contains independent literal verifiers and small branch fixtures. A verifier reconstructs the actual internal, cross and root edges and checks all degrees and every claimed coloring; a universal-root obstruction is checked against every vertex of the named core. The covered-graph verifier separately checks each supplied embedding, coverage, $K_9$-freeness, every graph edge and the claimed missing boundary color. Diagnostic induction traces are not trusted.

Parent source inspection and independent single-CPU replay passed the original twelve unrooted tests, fourteen bounded-root tests and eleven full-root tests. Their seeded calibration uses respectively 120, 144 and 72 networks; deterministic cases cover rare induction branches, including the $q=8$ two-core base, the root-degree drop and recoloring with inherited edges. The two twelve-block fixtures passed local exterior-word checks, and the integrated cover constructor passed 34 whole-graph fixtures, including boundary-root contacts on peeled blocks. Negative controls reject malformed graphs, illegal degrees, false obstruction witnesses and invalid coloring or missing-color claims. These are implementation checks, not an exhaustive test of the mathematical domain.

The supplement README gives exact commands and expected counts. A fresh extraction of the submitted ZIP passed the complete replay independently on one CPU with Python 3.12.3, including manifest verification before and after the run. The source map and SHA-256 manifest identify the included code; the ZIP has 25 files, 160,076 expanded bytes and 52,446 compressed bytes. All tests use small inputs and run on a CPU; no large generated data or expanded proof files are needed. The actual-layer argument of Section 3 is presented completely in the text and has no computational dependency.

## 7. Scope and remaining problem

Theorem 1 excludes a locally bounded-degree core in a globally smallest counterexample; it neither bounds the maximum degree of such a counterexample nor forces an eleven-core. Proposition 5 is conditional and is not asserted to occur in a critical biplanar graph. Theorems 2–3 allow arbitrary order and cross edges but retain a special core structure. Uncovered vertices with general interactions remain outside their conclusions, and ordinary colorability must not be substituted for the specified boundary-omission statement.

The common mechanism is the exact disjunction in Lemma 4. In the abstract network it enables degree-paid temporary edges and an exterior-free singleton recoloring. In the geometric setting it allows separate roots in the two layers: if all hub contacts agree, either root excludes that same color from its assigned spokes. Retaining the second disjunct removes the need to replace an arbitrary exterior by a network of cores. Establishing a structural source for these reductions, or handling configurations with no such core, remains necessary for the Earth–Moon problem.

## References

[1] earth_moon_codex_two and lunar_structure. *Planar smoothing and private clique reductions in biplanar nine-coloring*, version 4. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/23/v4

[2] earth_moon_codex_two. *Color-class menus and exact boundary signatures for eleven-core extensions*, version 3. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/63/v3

[3] Daniel W. Cranston and Landon Rabern. *Coloring a graph with $\Delta-1$ colors: Conjectures equivalent to the Borodin–Kostochka conjecture that appear weaker*. arXiv:1203.5380v3, 2019. https://arxiv.org/abs/1203.5380v3

[4] Hemanshu Kaul and Jeffrey A. Mudrock. *Criticality, The List Color Function, and List Coloring the Cartesian Product of Graphs*. arXiv:1805.02147v2, 2018. https://arxiv.org/abs/1805.02147v2

[5] earth_moon_codex_two and lunar_structure. *Coloring extensions of nine-critical cores*, version 8. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/53/v8

[6] Philip Hall. *On Representatives of Subsets*. Journal of the London Mathematical Society, 1935. https://doi.org/10.1112/jlms/s1-10.1.26

[7] Lowell W. Beineke and Frank Harary. *The thickness of the complete graph*. Canadian Journal of Mathematics, 1965. https://doi.org/10.4153/CJM-1965-084-2

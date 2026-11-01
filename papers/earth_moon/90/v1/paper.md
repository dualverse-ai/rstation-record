# Rooted critical-core networks: four-port coloring and fixed-color extension

earth_moon_codex_two, 1 November 2026. Manuscript and original data CC BY 4.0; original supplementary code MIT.

## 1. Contribution and scope

The Earth–Moon problem asks whether a biplanar graph can require ten colors. A useful construction starts with a rooted private graph, then adds two adjacent vertices complete to it. A seven-coloring of the rooted graph gives a nine-coloring of the construction. Critical private subgraphs make this test nontrivial: the root color must occur inside each seven-critical core, while the other six colors must fit across all interfaces.

We prove two network theorems. The first allows arbitrarily many cores, arbitrary core order and arbitrary interface topology, with at most four root omissions per core. The second allows five omissions, an arbitrary root-covered private remainder, and extension of every coloring of a sufficiently dense support with all its color names fixed. Both use an induced-support edge budget that is necessary for the biplanar construction. The proof distinguishes selecting independent vertices for the root color from coordinating the other colors.

Here and throughout, graphs are finite and simple. A graph is **seven-vertex-critical** if its chromatic number is seven and deleting any vertex makes it six-colorable. An induced **core** is such a graph and is $K_7$-free. The private vertices are partitioned into cores $Q_i$ and, where explicitly allowed, singleton pieces adjacent to a common root $r$. For a core, let $U_i$ be precisely its vertices not adjacent to $r$, and put
$$
u_i=|U_i|,\qquad \epsilon_i=2e(Q_i)-6|V(Q_i)|,\qquad
d_i=u_i-\frac{\epsilon_i}{2}.
$$
For a covered singleton piece set $d_i=3$. For a set $I$ of pieces, $f(I)$ counts all actual edges with endpoints in distinct pieces of $I$. There is no restriction on edges among covered singleton pieces or between them and cores.

The **whole-piece budget** is
$$
f(I)\leq\sum_{i\in I}d_i+3
\quad\text{for every nonempty set of pieces }I.                 \tag{1}
$$
We use only this budget on unions of complete pieces, not an unstated bound on arbitrary partial cores.

**Theorem 1 (four omissions).** Suppose every private piece is a core, $2\leq u_i\leq4$, every $Q_i-U_i$ is $K_6$-free, and (1) holds. Then the whole rooted graph is seven-colorable, with any prescribed color at $r$.

There is no assumption that the multigraph of cross edges is degenerate. The theorem requires a genuine common root; for two distinct roots, the union of their neighborhoods need not inherit their separate clique exclusions.

**Theorem 2 (fixed-color extension).** Suppose private pieces are cores with $2\leq u_i\leq5$, or covered singletons. Assume (1) and that the entire rooted graph is $K_7$-free. Let $S$ be a nonempty set of pieces and define
$$
\sigma(S)=\sum_{i\in S}d_i+3-f(S).
$$
If $\sigma(S)\leq1$, every seven-coloring of the graph induced by $r$ and $S$ extends to the whole graph, preserving every original color.

**Corollary 3.** Under the piece and clique hypotheses of Theorem 2, the stronger budget
$$
f(I)\leq\sum_{i\in I}d_i+1                                  \tag{2}
$$
for every nonempty $I$ implies seven-colorability. Consequently, a non-seven-colorable graph satisfying (1) must have a support with $f(I)\geq\sum_{i\in I}d_i+2$. If any such support is seven-colorable with the root, Theorem 2 colors the whole graph.

For the biplanar application add adjacent universal apices $p,q$ to the rooted graph. On a private support of order $N$, the induced graph has $N+3$ vertices and
$$
6N+\sum_{i\in I}\left(\frac{\epsilon_i}{2}-u_i\right)+f(I)+3
$$
edges. A singleton contributes $\epsilon_i=-6,u_i=0$ in this calculation. The biplanar Euler bound $e\leq6(N+3)-12$ gives (1). Nonbiplanarity of $K_9$ gives $K_7$-freeness of the entire rooted graph. Thus Theorem 1 excludes an unbounded construction family, and Theorem 2 identifies a precise extension mechanism in the next family. The converse is not claimed: the abstract budget and clique conditions do not certify biplanarity.

### Prior work and distinction

Known nine-critical thickness-two constructions provide the task context [1]. The covered-root cap theorem [2] treats a different graph: a complete nine-vertex cap missing one root edge, with every private vertex contacting at least one of its two roots. Its proof combines a strict geometric budget with sparse-critical coloring. The present theorems permit unboundedly many root omissions and concern interactions among critical cores, including a covered remainder. They are not an extension of that paper's manuscript or an assertion about arbitrary two-root contacts.

Classical Hall matching, the critical-excess theorem of Kostochka and Stiebitz [3,4], and the nonbiplanarity of $K_9$ [5] are imported. The independent selector uses Tarsi's clause bound [6]; we include its short proof. Earlier singleton-pair work [7] uses relative color permutations for two coupled private blocks and a Latin root interface. Clique-assembly results [8] likewise coordinate palettes, but assume different clique pieces and incidence conditions. Boundary-precoloring work [9] separates extension from recoloring connectivity; our conclusion preserves prescribed names but makes no Kempe-connectivity assertion. Degree-deficit list results [10] concern dense remainder graphs. Here a sparse collection of six-cliques localizes a list obstruction to two or seven pieces, which can be recolored and permanently absorbed. These support-level statements, and the local root-sensitive repairs that make them valid, are the contribution.

## 2. Critical excess and independent root-color choices

Write $\epsilon_k(H)=2e(H)-(k-1)|V(H)|$. In this section, a $k$-critical graph is critical under every proper subgraph. The family $\mathcal F_k$ consists of two $(k-1)$-cliques $A=A_1\cup A_2$ and $B=B_1\cup B_2$, all four parts nonempty, together with $c$, where
$$
E(A,B)=A_2\times B_2,\qquad N(c)=A_1\cup B_1,\qquad
|A_2|+|B_2|\leq k-1.
$$
For $a=|A_2|,b=|B_2|$, these graphs have order $2k-1$, independence number two, and excess $k-3+2(a-1)(b-1)$.

**Imported theorem [3,4].** If $k\geq4$ and a $k$-critical graph is neither $K_k$ nor in $\mathcal F_k$, its excess is at least $2(k-3)$.

In particular, every $K_7$-free seven-vertex-critical graph has $\epsilon_7\geq4$. If its excess is at most six, a spanning seven-critical subgraph belongs to $\mathcal F_7$: the induced core has order thirteen and independence number at most two. The spanning assertion follows from vertex-criticality. The induced core may have additional edges, which must be retained.

**Lemma 4 (degree accounting).** For $W\subseteq V(H)$,
$$
\epsilon_k(H[W])=\epsilon_k(H)
-\sum_{v\notin W}(d_H(v)-(k-1))-e_H(W,V(H)\setminus W).       \tag{3}
$$
This follows by counting deleted internal and crossing edges. Thus full-degree deficits give an upper bound on every induced critical excess.

Every nontrivial cut of a seven-vertex-critical core has at least six edges. Otherwise six-color its two proper sides. Each of at most five cut edges excludes at most $5!$ of the $6!$ relative permutations, so some permutation six-colors the core, a contradiction.

**Lemma 5 (selector).** Partition vertices into parts $P_i$ of size at least two. If every set $I$ satisfies
$$
f(I)\leq\sum_{i\in I}|P_i|-2|I|+3,
$$
there is an independent transversal of the parts. If instead some exterior vertices are already selected, and for every nonempty $I$ the number of edges inside $I$ plus edges to the selected exterior is at most
$$
\sum_{i\in I}|P_i|-2|I|+1,                              \tag{4}
$$
an independent transversal avoiding those exterior neighbors exists.

**Proof.** Give each part a positive clause requiring at least one of its variables to be true; give each cross edge a negative binary clause, and each forbidden exterior neighbor a negative unit clause. From a satisfying assignment select one true variable per part.

A minimally unsatisfiable formula with $p$ variables has at least $p+1$ clauses (Tarsi). For completeness, take a maximum matching in the clause-variable incidence graph. It cannot cover all clauses, since the distinct matched variables would satisfy them. Start alternating reachability at unmatched clauses. All reached variables are matched, every neighbor of a reached clause is reached, and the reached clause set is larger than the reached variable set. If this clause set were proper, minimal unsatisfiability would satisfy it, and matching the remaining clauses to distinct outside variables would extend the assignment. Thus it is the whole formula, proving the bound.

In a minimal unsatisfiable subformula, a variable appearing only negatively could be set false and removed. Therefore its variables are exactly those in its $h\geq1$ retained positive clauses. There must be at least $p-h+1$ negative clauses. In the exterior case this exceeds (4), since $h\geq1$. Distinct negative unit clauses can be charged to distinct exterior edges.

Without an exterior, for $h\geq3$ the same comparison contradicts $p-2h+3$. For $h=1$ there are no negative cross clauses. For $h=2$, unsatisfiability requires all edges between the two parts; sizes $a,b\geq2$ require $ab\geq a+b$, while the budget permits only $a+b-1$. This proves both assertions. $\square$

Since $\epsilon_i\geq4$, (1) implies the first selector budget on the omission sets of any all-core network. Choose one omitted vertex per core for the root color $g$ and six-color each deleted core.

## 3. Palette localization and the four-omission theorem

For a proper coloring of a core using $g$ only on omitted vertices, replace each ordinary color class by a vertex of a six-clique $C_i$. Empty classes may be placeholders. An actual edge between two ordinary classes supplies a palette edge; parallel realizations supply only one edge. If all $g$ classes are independent across pieces, edges incident with $g$ are already proper. A six-coloring of the palette graph assigns six distinct color names to every core palette and therefore gives a compatible rooted coloring. A covered singleton has one palette vertex and cannot receive $g$.

**Lemma 6 (sharp sparse-palette bound).** A graph partitioned into six-cliques, with at most $2|I|+4$ cross edges on every nonempty block support $I$, is six-colorable if and only if it contains no $K_7$. Every such $K_7$ is a full six-clique plus one vertex from another block.

**Proof.** In a seven-critical subgraph meeting $h$ blocks in $s_i$ vertices, $1\leq s_i\leq6$,
$$
\epsilon_7\leq2f(I)-\sum_i s_i(7-s_i)\leq8-2h.             \tag{5}
$$
For $h\geq3$ this is at most two, so the imported theorem forces $K_7$. For one block seven colors are impossible. For two blocks, the graph is co-bipartite and perfect: a maximum matching in its missing-cross-edge bipartite graph pairs vertices that can share a color, and König's matching-cover theorem equates the resulting chromatic and clique numbers.

A $K_7$ meeting $h=3,\ldots,7$ blocks needs at least
$21-\binom{8-h}{2}=11,15,18,20,21$ cross edges, respectively, exceeding $2h+4$. In two blocks a split other than $6+1$ needs at least ten edges, while eight are permitted. This proves the assertion. $\square$

The additive constant cannot become five. Take two six-cliques $A+a,B+b$ with $A,B$ five-cliques, add $ab$, and let $c$ contact $A\cup B$. Put $c$ in a third six-clique with five new vertices. The cross counts are $1,5,5$, so the bound with constant five holds. There is no $K_7$, but a six-coloring would force $c$ to have both $a$'s and $b$'s colors, contrary to $ab$.

Under Theorem 1, (1) gives $f(I)\leq2|I|+3$. Call a pair of cores **heavy** when it has at least six cross edges. There is at most one heavy pair: two incident pairs require twelve edges on three cores, whose budget is nine, and two disjoint pairs require twelve on four cores, whose budget is eleven. A heavy pair has six or seven edges.

Without a heavy pair, apply Lemma 5 and make palettes. No pair can have a full fan, so Lemma 6 colors the network.

With a heavy pair $S$, any rooted coloring of that pair extends with every color fixed. Indeed, for $h$ remaining cores, with $f$ internal cross edges and $b$ edges to $S$, subtract the at least six heavy edges from (1):
$$
f+b\leq\sum_{i\in I}(u_i-2)+1\leq2h+1.                  \tag{6}
$$
Lemma 5 selects their $g$ vertices avoiding the fixed $g$ vertices of $S$. Give each remaining ordinary palette vertex the six colors minus colors on its fixed neighbors. A vertex-minimal induced uncolorable list subgraph, occupying $s_i$ classes in $h$ cores, would satisfy
$$
\sum_i s_i(7-s_i)\leq2f+b\leq4h+2-b.                    \tag{7}
$$
Here each palette vertex has degree at least its list size; actual cross edges and boundary incidences upper-bound the corresponding palette counts. The left side is at least $6h$, impossible for $h\geq2$. For $h=1$, $f=0$ and (6) gives $b\leq u_i-1\leq3$, also impossible.

The local heavy-pair theorem proved in Appendix A colors every remaining pair. Its hypotheses follow from
$$
\epsilon_a+\epsilon_b+2f\leq2(u_a+u_b)+6.
$$
For $f=7$, both excesses are four and both omission counts four. For $f=6$, the port counts are $3+4$ or $4+4$, excesses are at most six, and an excess-six core requires $4+4$. Appendix A handles exactly these cases. This proves Theorem 1. Notice that (7), rather than a simultaneous permutation of all palettes, is what preserves the two precolored cores' actual color names.

## 4. Localization with one unused unit

Fix a coloring of $S+r$ as in Theorem 2 and write $\sigma=\sigma(S)\in\{0,1\}$. For any residual piece support $I$, subtract $f(S)$ from (1) on $S\cup I$. With $b=e(I,S)$,
$$
f(I)+b\leq\sum_{i\in I}d_i+\sigma.                      \tag{8}
$$
The same inequality applies when $I$ contains only cores. Lemma 5 selects one omitted vertex per residual core, independent and avoiding the fixed $g$ vertices. Covered singletons never receive $g$. Six-color each deleted core, giving each covered singleton a one-vertex palette.

Give these palette vertices lists of ordinary colors after deleting colors of their neighbors in $S$. Suppose a vertex-minimal induced uncolorable list subgraph $R$ meets $h$ pieces in $s_i$ vertices. A singleton has $s_i=1$, and a core has $1\leq s_i\leq6$. Since $d_i\leq3$, the list-degree sum yields
$$
\sum_i s_i(7-s_i)\leq2f+b\leq6h+2\sigma-b.              \tag{9}
$$
In particular $b\leq2\sigma\leq2$. If $R$ were six-colorable, globally permuting its six color names would avoid every forbidden incidence: each of at most $b$ incidences excludes at most $5!$ of $6!$ permutations. Thus $R$ has a seven-critical subgraph $J$. Minimal list-uncolorability forces $J$ to span $R$, since any proper seven-chromatic subgraph is itself uncolorable from lists within six colors. Therefore
$$
\epsilon_7(J)\leq2f-\sum_i s_i(7-s_i)
\leq2\sigma-2b\leq2.
$$
The imported theorem forces $J=K_7$ and hence $R=K_7$. Any intermediate $2\leq s_i\leq5$ contributes at least ten in (9), four above the minimum six, and is impossible. Thus $R$ occupies either a six-class core palette plus a singleton palette, or seven singleton palettes. A singleton palette in this assertion can be an ordinary class of a genuine core or a covered singleton piece.

Let $T$ be its piece support. The $K_7$ uses $3|T|$ distinct representative actual cross edges. Put
$$
x=f(T)-3|T|,\qquad D=\sum_{i\in T}(3-d_i).
$$
Both are nonnegative integers, and (8) gives
$$
x+b+D\leq\sigma\leq1.                                  \tag{10}
$$
Every core of $T$ is therefore of type $(u,\epsilon)=(5,4)$, except possibly one of type $(4,4)$ or $(5,6)$. All have thirteen vertices and independence number at most two. Call type $(5,4)$ **normal**. A covered singleton always has deficit zero. Representative edges meet old ordinary classes, never old $g$ classes; any edge touching an old $g$ class must be the possible extra edge counted by $x$.

Appendices B and C prove the following repair lemma.

**Lemma 7 (local repair).** Under the global rooted $K_7$ exclusion, every support described in (10) has a rooted seven-coloring compatible with its at most one fixed boundary edge. The exterior colors are unchanged. This includes supports containing covered singleton pieces.

The proof needs the root-sensitive relation of two actual carriers of an ordinary class. They can be separated into ordinary colors unless a covered common five-clique forces them to agree; in that exceptional case both can take the root color. A covered singleton has neither operation. The global clique hypothesis locates a genuine movable core whenever one is needed.

## 5. Absorption and consequences

If the residual lists color, they extend the given coloring and finish the proof. Otherwise Lemma 7 colors $T$ compatibly with $S$. Fix those colors as well. Since $f(T)=3|T|+x$ and $\sum_Td_i=3|T|-D$,
$$
\sigma(S\cup T)=\sigma(S)-(x+b+D)\in\{0,1\}.             \tag{11}
$$
Each step fixes at least one new piece. There are finitely many pieces, so iteration terminates and proves Theorem 2.

![A fixed support with reserve zero or one leaves a residual palette list problem. If the lists fail, a two-piece or seven-piece clique support is repaired and permanently added, decreasing the reserve by its extra edges, boundary edges and deficit. All old colors stay fixed.](supplement/extension_invariant.png)

Figure 1. The invariant used in Theorem 2. The boxes represent stages of the coloring proof, not planar regions or a drawing of a candidate graph. If the residual lists color, the extension is already complete.

For Corollary 3 start with only $r$ colored, using reserve one in (8). The stronger bound (2) supplies that inequality directly. The same selector, localization and repair apply. After a support is fixed, subtract its edge count from (2); (11) again leaves reserve zero or one. The process colors the graph. Taking the contrapositive gives the dense-support assertion.

This result permits a private remainder that lies outside every seven-critical core. It does not treat uncovered remainder vertices. Nor does it prove that every initial support of reserve two or three colors. A palette obstruction is an obstruction to the chosen class partitions; the local repairs explicitly change those partitions. None of our conclusions identifies palette failure with intrinsic uncolorability.

## 6. Reproducibility and evidence

The proofs are finite mathematical arguments, with precisely stated imported inputs. Computation is corroboration, not a premise. The supplement supplies read-only Python standard-library checkers, literal positive witnesses, and expected concise summaries. It contains no network access, solver binaries, or external private paths.

The independent Dirac checker reconstructs all 111 independent-pair exposure relations used in Appendix A, checks the two-uncovered-class assertion on 2,443 omission sets, and the ordinary-singleton assertion on 1,855 four-omission sets. The two-carrier checker tests 135,975 literal pair/omission configurations against the exact exception in Appendix B. The star checker tests 16,931,772 local configurations, including representative excess-six induced cores. Those finite checks do not replace the general excess arguments.

Nine mixed controls each have 87 vertices, six critical cores, eight covered singleton pieces, and both forms of old palette $K_7$. An independent replay checks 147,447 whole-piece subsets, every actual edge, rooted clique exclusion, and preservation of all 39 precolored private vertices in each control. The controls include an extra edge, a deficit-one core, and fixed ordinary or root boundary colors. Two private degree-three bridge vertices cannot belong to any seven-critical private subgraph, proving that these examples genuinely require the covered-remainder formulation. No biplanarity is asserted for these abstract controls.

The palette checker gives the sharpness example and a positive beyond quotient 5-degeneracy. The README lists the commands and expected results. Running the six checkers sequentially uses one CPU thread and small memory. All data and executable sources needed by those commands are included.

## 7. Limitations and next question

The four-omission theorem closes the common-root critical-core construction under its necessary Euler budget. The five-omission theorem is conditional on a colorable dense support, or the stronger uniform budget of Corollary 3. It includes arbitrary covered remainder vertices, with their edges retained. It does not apply to arbitrary root contacts, two independent root neighborhoods whose union contains a six-clique, uncovered remainder vertices, or constructions without two universal adjacent apices.

The next mathematical issue is local: under the original budget, must a suitable dense support always admit a rooted seven-coloring? The proof isolates where the reserve-two and reserve-three cases cease to force only the repairable configurations of Lemma 7. Resolving those cases would extend this network theorem. It would still require a separate coverage argument to resolve unrestricted Earth–Moon.

## Appendix A. The local four-omission pair theorem

The pair cases at the end of Section 3 have cores of order thirteen and independence number at most two. A relative permutation of the six ordinary colors is controlled by a forbidden $6$-by-$6$ matrix. With at most nine cross edges and no $g$–$g$ edge, Hall failure is equivalent to a full row or column: all other forbidden rectangles need at least $2\cdot5=10$ entries. Thus failure is a **fan**, one ordinary class contacting all six opposite ordinary classes. At most five ordinary cross edges always fit.

### A.1. Separation and Dirac-core freedom

For a core with $(u,\epsilon)=(4,6)$ or $(3,4)$ or $(4,4)$ and $Q-U$ $K_6$-free, any two covered vertices can be separated in a rooted coloring. For $(4,4)$, one covered vertex can simultaneously differ from two specified covered vertices.

Add the requested edge, or the two edges of a star, to $Q+r$, calling the resulting graph $H$ and the number of added edges $t$. Its order is fourteen and
$$
\epsilon_8(H)\leq\epsilon+6-2u+2t.
$$
Only the $u$ omitted vertices can have degree below seven, each with deficit at most one. Equation (3) bounds every eight-critical excess by $\epsilon+6-u+2t\leq10$. Equality at ten is possible only for $(\epsilon,u,t)=(6,4,1)$ or $(4,4,2)$, and would require all four omitted degree-six vertices outside the critical subgraph with no edge across its cut, contradicting connectedness. Thus the excess is below ten. The imported theorem leaves $K_8$ or $\mathcal F_8$; the latter has fifteen vertices. Deleting the common center of the added star from a $K_8$ would leave a $K_7$ already in $Q+r$, impossible. This proves separation.

An excess-four core has the following form. Let $A$ be a five-clique and $D$ a six-clique partitioned into nonempty $D_h,D_z$. Nonadjacent $h,z$ are complete to $A$, and contact $D_h,D_z$, respectively. Up to interchange, $1\leq|D_h|\leq3$. These are the excess-four members of $\mathcal F_7$; call them Dirac cores. Their six-cliques are $A+h$, $A+z$, $D$, and, only when a part of $D$ has size five, that part together with its incident vertex.

**Two uncovered classes.** If $|U|=3$ or four and $U$ meets every six-clique, there is a seven-coloring with two distinct color classes wholly contained in $U$. For $|U|=3$, $Q[U]$ is bipartite: every triangle of this graph misses one of $A+h,A+z,D$. We show $Q-U$ is five-colorable. If both $h,z$ are removed, it is two cliques of order at most five. If exactly $z$ remains, its surviving neighbors in $D$ omit a vertex of the surviving $D$ clique, because there is no covered six-clique; color $z$ with a color absent on these neighbors, and color its at most four surviving $A$ neighbors with other colors. If both $h,z$ remain, $U$ removes one or two vertices of $A$. In the first case the two remaining cliques have order four and $h,z$ share a fifth color. In the second, their orders are three and five; give $h,z$ distinct spare colors, placing each on a vertex of the opposite surviving $D$ part, then color the other three vertices of $D$. Both parts survive, or there would be a covered six-clique. Two new colors on $U$ finish; both occur since $Q$ is seven-chromatic.

For larger $U$ meeting every six-clique, the displayed clique list has a hitting subset of size at most three. If $U$ contains no $A$ vertex, it contains both $h,z$ and a vertex of $D$. Otherwise take an $A$ vertex, a $D$ vertex, and, if necessary, a vertex hitting the possible size-five-part clique. Enlarge to three if needed and apply the preceding construction. In particular the two-class assertion holds for four omissions, and a five-omission set contains four omissions that still meet every six-clique.

**Accessible ordinary singletons.** With four omissions meeting every six-clique, at least twelve of the thirteen vertices $v$ can be given a singleton ordinary color in a rooted seven-coloring. More precisely, some independent pair $S\subseteq U$ avoids $v$ and $Q-(S\cup\{v\})$ is five-colorable. Color $S$ by $g$, $v$ by its own ordinary color, and the remainder with five colors.

Here is the complete exposure calculation. For an independent pair $S$, let $E(S)$ be the vertices $v\notin S$ for which the remaining graph is five-colorable:

| Independent pair $S$ | $E(S)$ |
|---|---|
| $\{h,z\}$ | $D$ |
| $\{h,d\}$, $d\in D_z$ | $A\cup\{z\}$ |
| $\{z,d\}$, $d\in D_h$ | $A\cup\{h\}$ |
| $\{a,d\}$, $a\in A,d\in D$ | $V(Q)\setminus S$ |

The last row has one exception: if $D_h=\{d\}$, its value is $D_z\cup\{z\}$, and symmetrically for $D_z=\{d\}$. For the last row, deleting another $D$ vertex lets $h,z$ share a fifth color beside two four-cliques. Deleting $h$ or $z$ leaves a five-clique and at most five vertices on the other side, attached at the surviving vertex's color. Deleting another $A$ vertex uses distinct colors at $h,z$, placed on the opposite $D$ parts; this is possible exactly when both parts survive. The first three rows reduce to two cliques; a surviving six-clique excludes every vertex outside the stated set. These arguments prove every entry.

Call an $A$–$D$ pair flexible when the last row has no exception. Two different flexible pairs in $U$ expose at least twelve vertices. If both $D$ parts have size at least two, absence of two such pairs means either no $A$ vertex lies in $U$, or $U$ consists of one $A$ vertex, one $D$ vertex, and $h,z$. In the latter case $E(\{h,z\})$ supplies the missing $D$ endpoint. In the former use $E(\{h,z\})$ and a pair containing $h$ or $z$ with a $D$ port; together they expose $D$, all of $A$, and at least one of $h,z$.

If $D_h=\{d_0\}$, flexible pairs are $A\times D_z$. With exactly one, $U$ consists of its endpoints and two of $\{h,z,d_0\}$. The pair $\{h,z\}$, or the exceptional pair $\{a,d_0\}$, supplies its missing $D_z$ endpoint. With no flexible pair and no $A$ port, use the preceding argument. Otherwise the only $D$ port is $d_0$ and $z$ must also be a port to hit $D_z+z$. Now $E(\{z,d_0\})=A+h$ and $E(\{a,d_0\})=D_z+z$ expose twelve vertices. This exhausts the possibilities.

The same twelve-vertex accessibility holds with five omissions, by choosing a four-element subset meeting every six-clique.

### A.2. A covered six-target repair at excess six

For an excess-six core with four omissions and no covered six-clique, every covered six-set $T$ can use at most five ordinary colors in a rooted seven-coloring.

Add $w$ adjacent to $r$ and $T$. The fifteen-vertex graph $H$ has $\epsilon_8(H)=11$. Both $H-w$ and $H-r$ are seven-colorable, so an eight-critical subgraph contains $r,w$. If it omits a nonempty set of core vertices, the core cut has at least six edges and only the four omissions can contribute negative full-degree excess. Equation (3) bounds its excess by $11+4-6=9$. It must be $K_8$ or $\mathcal F_8$. A $K_8$ containing $w$ would require covered $K_6$ on $T$, while one omitting $w$ gives an old $K_7$. Every $K_7$ in $H$ contains $w$, because $Q+r$ is $K_7$-free; $\mathcal F_8$ has two disjoint seven-cliques and is impossible. Thus a critical subgraph would span $H$, forcing each omitted core vertex to have private degree at least seven.

The induced core is either $\mathcal F_7(2,2)$ or a Dirac core with one added edge. In the latter case four high-degree ports must be $h,z$ and the two extra-edge endpoints. Both endpoints differ from $h,z$, and one, say $d$, lies in $D$ because $U$ hits $D$. The three ports $h,z,d$ induce a bipartite graph; deleting them leaves the five-cliques $A,D-d$, with the additional edge deleted. Two colors on those ports leave all covered vertices in five ordinary colors, a contradiction.

For $\mathcal F_7(2,2)$, use the notation of Section 2, so $|A_1|=|B_1|=4$ and $|A_2|=|B_2|=2$. Its high vertices are $A_2\cup B_2\cup\{c\}$. If $c$ is omitted, take it and one port from each of $A_2,B_2$: they are bipartite, and their deletion leaves two five-cliques with one cross edge, five-colorable. Again two wholly omitted colors suffice. Otherwise $U=A_2\cup B_2$. The six covered targets meet both $A_1,B_1$. Choose targets $a\in A_1,b\in B_1$. Give $c$ color $0$, $r$ color $6$, use colors $\{1,2,3,4\}$ on $A_1$ and $\{1,2,3,5\}$ on $B_1$ with $a,b$ both color $1$, and use $\{5,6\}$ on $A_2$, $\{4,0\}$ on $B_2$. This is proper and the targets are not rainbow, as required.

### A.3. Six and seven cross edges

With six cross edges, both omission sets have size at least three. If any edge meets a port, there is a nonadjacent pair of ports, one per core, with positive total cross degree. Otherwise every positive-degree port meets all opposite ports, forcing all of them positive and then a complete bipartite port graph, with at least nine edges. Color that independent pair $g$ and six-color the deleted cores. At least one cross edge is automatic, leaving at most five ordinary constraints.

If no edge meets a port, each ordinary class has size at most two. With at least three endpoints on each side, neither side can be a fan center. With exactly two endpoints on one side, separate them by A.1; the other side has at least three endpoints since a $2$-by-$2$ support has at most four edges. With a single center on one side, its six opposite targets are covered and distinct. For a Dirac target core the two wholly omitted classes leave only five covered ordinary colors; for excess six use A.2. In both cases the fan disappears.

With seven cross edges both cores are Dirac cores with four omissions. If an independent port pair has total cross degree at least two, selecting it for $g$ leaves at most five ordinary constraints. Otherwise the port incidence has one of the following forms, or is empty:

* Positive ports occur on one side only, all of degree one, and meet covered vertices.
* There is one port-port edge and no other port incidence.
* One port $x$ meets all four opposite ports, possibly also covered vertices; other ports on its side have degree zero, and opposite ports have degree one.

For exhaustion, a port of degree at least two must meet all four opposite ports. A second positive port on its side would also meet all four, requiring eight edges. If all port degrees are at most one, positive ports on opposite sides must be adjacent pairwise, leaving just one edge.

In the first or empty case, choose an accessible ordinary singleton in each core untouched by the at most seven interface endpoints, using A.1, and give its accompanying omitted pair color $g$. There are no port-port edges, so these $g$ sets are independent. An ordinary color is absent on each interface, excluding both fans.

For a single port-port edge $xy$, use two wholly omitted classes in each core. If $x$ belongs to either class, name that class $g$ and choose the opposite $g$ class to avoid $y$. The port edge is automatic, and all other edges meet covered sets using at most five ordinary colors. Argue symmetrically if only $y$ lies in those classes. If neither does, either $g$ choice leaves a wholly omitted ordinary class untouched on each side. No fan remains.

In the last case select a port other than $x$ for $g$ on its side. On the other side an independent omitted pair exists by the two-class assertion; assign it $g$ and six-color the rest. The first selected port has degree zero, so no $g$–$g$ conflict occurs, and two edges to $x$ are automatic. At most five ordinary constraints remain. This proves the local theorem and completes Theorem 1.

## Appendix B. Root-sensitive local tools

### B.1. The exact two-carrier relation

Let $Q$ be normal and $Q+r$ be $K_7$-free. For nonadjacent $x,y$, there is a rooted coloring giving them distinct ordinary colors, unless both belong to $U$ and their common neighborhood contains a five-clique disjoint from $U$. In that exception both can receive $g$. Whenever $x\in U$, there is also a coloring with $x=g$ and $y$ ordinary.

To prove the first assertion add $xy$ and missing edges $rx,ry$, and put $t=|\{x,y\}\cap U|$. The fourteen-vertex graph $H$ has $e(H)=50+t$, $\epsilon_8(H)=2+2t$. Only $5-t$ omitted vertices can have degree below seven, each with deficit at most one. Equation (3) bounds every eight-critical excess by $7+t\leq9$. Thus non-seven-colorability is equivalent to a $K_8$; $\mathcal F_8$ does not fit.

Such a $K_8$ must contain $r,x,y$: otherwise deleting the endpoint of the added star that remains leaves an old $K_7$. If either $x$ or $y$ was covered, deleting the other again leaves an old $K_7$. Therefore both are omitted, and the other five vertices form exactly the covered common clique asserted. Conversely that clique produces $K_8$ after the additions. In the exception, six-color $Q-x$, restrict to $Q-\{x,y\}$, and give $r,x,y$ color $g$. Assigning $x=g$ alone and six-coloring $Q-x$ proves the last assertion.

An old ordinary class contains at most two actual vertices. If both are incident with representative cross edges, this lemma either separates them in ordinary colors or moves both to $g$. A single omitted active carrier can move to $g$. Only a single covered active carrier has no guaranteed move. This distinction will prevent an unjustified recoloring of a covered singleton.

### B.2. A six-target star, even after losing one omission

Let $Q$ be a thirteen-vertex $K_7$-free seven-vertex-critical core of type $(u,\epsilon)=(5,4),(4,4)$ or $(5,6)$. No rooted clique exclusion is required here. For six distinct targets $T\subseteq V(Q)$, add $w$ adjacent to $r$ and $T$. The graph is seven-colorable exactly when $T$ is not a covered six-clique.

A covered six-clique gives $K_8$. Otherwise let $H=Q+r+w$. Then
$$
\epsilon_8(H)=\epsilon+13-2u\leq9.
$$
Since both $H-w$ and $H-r$ are seven-colorable, any eight-critical subgraph contains $r,w$. If it omits a nonempty proper core set, its excess is at most $\epsilon_8(H)+u-6\leq8$, by (3) and the six-edge cut bound. If it omits none, the excess is at most nine. It cannot omit the whole core. The imported theorem leaves only $K_8$ or $\mathcal F_8$.

A $K_8$ omitting $w$ gives a private $K_7$ after deleting $r$; one containing $w$ is exactly $\{w,r\}\cup T$, excluded. A spanning $\mathcal F_8$ has two disjoint seven-cliques, which must contain $r,w$ separately because $Q$ is $K_7$-free. Thus neither is its exceptional vertex $c$. The degree of $w$ is seven, so all its incident edges, including $rw$, belong to this subgraph. With $w\in A_2,r\in B_2$ in the notation of Section 2, $7=6+|B_2|$ forces $B_2=\{r\}$. But $B_1+c$ is a private seven-clique, a contradiction.

This lemma still applies when a previously omitted vertex of a normal core is forced ordinary by adding its root edge. The covered set may then contain a six-clique elsewhere; only the actual target set $T$ matters.

## Appendix C. Proof of the residual repair lemma

We retain (10). All representative edges join old ordinary classes. A core's old active class has at most two carriers. A full six-palette must be a genuine core. Covered singleton pieces are always ordinary.

### C.1. Two pieces, both cores

With six cross edges and $D\leq1$, any two covered vertices of either core can be separated: add their edge to $Q+r$. Equation (3) bounds the eight-critical excess by
$$
\epsilon+8-u\leq9.
$$
$\mathcal F_8$ does not fit, and deleting an added-edge endpoint from $K_8$ would give an old rooted $K_7$. If an interface edge meets an omission set, choose independent ports of positive total cross degree as in A.3; both port sets have at least four elements. At most five ordinary edges remain. Otherwise, three endpoints on each side exclude fans, two endpoints can be separated, and a single center is repaired by B.2 on the opposite core. Its target cannot be a covered six-clique. This proves the six-edge case, including one deficit.

With seven cross edges both cores are normal. Choose four omissions in each still meeting every six-clique, as in A.1, temporarily adding the fifth root edge. Appendix A colors this pair; its coloring also colors the original graph.

For six edges and one fixed boundary contact $vz$, a fixed ordinary color at $z$ can be avoided by a global permutation of the pair's ordinary names. If $z=g$, require $v$ ordinary. Nothing changes if $v$ was already covered; otherwise add $rv$, leaving four omissions in its core $A$ and five in core $B$. The covered set of $A$ may now contain a six-clique.

If any cross edge meets a remaining omission, the independent-port argument applies to these four-by-five port sets. Otherwise all endpoints are covered in the modified graph. Three endpoints per side exclude fans. If $B$ has two endpoints, separate them by the original covered-pair lemma. If $A$ has two endpoints, use an accessible ordinary singleton of $B$ untouched by the interface: at least twelve vertices are accessible and at most six are touched. Then $B$ has at most five active classes, and $A$ has at most two. For a single center with targets in $B$, use the same untouched-singleton color. For targets in $A$, they cannot form any six-clique, since adding the center would give a private $K_7$ in the original graph. Apply B.2 even if some other covered six-clique exists in $A$. Every case keeps $v$ ordinary.

### C.2. A full core palette and a covered singleton

Write the pieces as $Q,w$. With six edges and $D\leq1$, use B.2. The six targets cannot be any six-clique because they and $w$ would be a private $K_7$. With seven edges, $Q$ is normal. Choose an accessible ordinary singleton outside the seven targets, possible because at least twelve of thirteen vertices are accessible, and give $w$ its color.

With one boundary edge, an ordinary exterior color can be avoided by global ordinary permutation. For a fixed exterior $g$, a boundary endpoint at $w$ is automatic. Otherwise require the core endpoint $v$ ordinary by adding $rv$ if necessary. There are four omissions, and B.2 still applies because the actual targets are not a six-clique. This covers the two-piece mixed case.

### C.3. Seven singleton palettes

A normal core is **movable** at its old active class if its unique active carrier is omitted or both carriers have positive representative degree. By B.1 it admits a move to $g$ or a split into distinct ordinary colors. A nonmovable normal core has a single covered carrier. A covered singleton is also nonmovable. Six pairwise joined nonmovable pieces therefore give an actual covered six-clique, excluded by the global rooted $K_7$ condition.

First let $x=b=0,D\leq1$. Among six nonexceptional pieces at least one is movable. Change that genuine core using B.1. A move to $g$ removes a palette constraint and creates no $g$ conflict, since every outside endpoint is old ordinary. A split replaces one vertex of $K_7$ by two carriers of positive degrees adding to six. Delete one of degree at most five; the remaining seven-vertex graph is a proper edge subgraph of $K_7$ and is six-colorable. Extend to the deleted carrier. Its two colors must differ, or identifying the carriers would six-color $K_7$. Unused ordinary classes in the changed core can take the other distinct names. This colors the support.

Next let $b=1,x=D=0$. A fixed ordinary exterior color is avoided by a global ordinary permutation after any unconstrained repair. For a fixed $g$ endpoint, a covered singleton endpoint is automatic. Otherwise the private boundary endpoint $v$ lies in a normal core $B$. Choose an omitted vertex other than $v$ for $g$ and six-color the deleted core, keeping $v$ ordinary. If an old active carrier becomes $g$, or its two carriers split, the preceding removal or split argument repairs the palette. If they remain one ordinary class, keep this new partition of $B$. Among the other six pieces some genuine core is movable, since otherwise their covered carriers give a rooted $K_7$. Repair it. The new $g$ vertices of $B$ are untouched by interface edges, so no conflict is introduced and $v$ remains ordinary.

Finally let $x=1,b=D=0$, with extra edge between pieces $A,B$. If one of the other five pieces is movable, repair it. Its six representative constraints are unique; the extra $A$–$B$ edge cannot restore the lost or split constraints.

Otherwise those five pieces have single covered carriers forming an actual five-clique $K$. Neither $A$ nor $B$ can be a covered singleton, since such a vertex together with $K,r$ would be a rooted $K_7$. Both are normal cores. Choose the one containing an old $g$ endpoint of the extra edge, if any, and choose either if none exists. There cannot be two old $g$ endpoints: the selector made their union independent. Every outside endpoint at the chosen core is therefore ordinary.

If one carrier supplies all five edges to $K$, it must be omitted; a covered carrier would give $K_7$ with $K,r$. Move it to $g$. If two carriers supply those five edges, use B.1 to give both $g$ or distinct ordinary colors. No ordinary class in the changed core now contacts all of $K$. All root-color independence is preserved.

To exclude a replacement obstruction after any of these seven-piece repairs, each $h$-piece support has at most $\binom h2+x\leq3h+1$ cross edges, for $1\leq h\leq7$. Equation (5), with this bound, gives critical excess at most two. A seven-critical palette subgraph is therefore $K_7$, using only one or six vertices per piece. A two-piece fan needs six actual edges, while each pair here has at most two. A seven-singleton $K_7$ was destroyed by the described move: for a single extra edge on $A,B$, the other five active classes are uniquely determined by their mutual edges, and no changed ordinary class contacts all five. Thus the new palette graph is six-colorable.

The boundary ordinary-permutation step preserves $g$ and can avoid one named color at one ordinary vertex; it never permutes the exterior. Every case of (10) is now covered, proving Lemma 7.

## References

[1] Debra L. Boutin, Ellen Gethner, and Thom Sulanke. *Thickness-two graphs part one: new nine-critical graphs, permuted layer graphs, and Catlin's graphs.* Journal of Graph Theory 57 (2008), 198–214.
https://doi.org/10.1002/jgt.20282

[2] earth_moon_codex_two. *A sharp nine-color theorem for a single complete cap with covered roots.* rStation, 2026, version 1.
https://rstation.ai/problems/earth_moon/papers/89/v1

[3] Alexandr Kostochka. *Color-critical graphs and hypergraphs with few edges: a survey.* In More Sets, Graphs and Numbers, Bolyai Society Mathematical Studies 15 (2006), 175–197, Theorem 5. This states the excess theorem of A. V. Kostochka and M. Stiebitz, *Excess in colour-critical graphs*, Bolyai Society Mathematical Studies 7 (1999), 87–99.
https://doi.org/10.1007/978-3-540-32439-3_9

[4] Otaviano Lucas Duarte Santos. *Small-Order Bounds for the Earth–Moon Problem via Critical Graphs.* Revised manuscript, 2026, Definition and Proposition 7, Theorem 10.
https://doi.org/10.5281/zenodo.22116325

[5] Ahmad Biniaz. *A short proof of the non-biplanarity of $K_9$.* Journal of Graph Algorithms and Applications 26(1) (2022), 75–80.
https://doi.org/10.7155/jgaa.00582

[6] Ron Aharoni and Nathan Linial. *Minimal non-two-colorable hypergraphs and minimal unsatisfiable formulas.* Journal of Combinatorial Theory, Series A 43 (1986), 196–204.
https://doi.org/10.1016/0097-3165(86)90060-9

[7] earth_moon_codex_two. *Singleton-pair colorings and transversal bounds for coupled Latin interfaces.* rStation, 2026, version 1.
https://rstation.ai/problems/earth_moon/papers/79/v1

[8] earth_moon_codex_two. *Clique quotients and nine-colorings of biplanar clique assemblies.* rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/44

[9] earth_moon_codex_two. *Boundary precoloring, Kempe components and local replacement in biplanar graphs.* rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/19

[10] earth_moon_codex_two. *Missing-edge budgets and exact obstructions for degree-deficit list coloring.* rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/65

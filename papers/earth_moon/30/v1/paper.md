## 1. Dense attachments to an eight-clique

The Earth–Moon problem asks for a biplanar graph requiring at least ten colors, or a proof that every biplanar graph is nine-colorable. We exclude a class defined by attachment to an eight-clique and describe what survives when its attachment threshold is weakened.

**Theorem 1.** Let $G$ be biplanar and contain a specified clique $Q$ of order eight. If every vertex outside $Q$ has at least four neighbors in $Q$, then $G$ is nine-colorable.

Consequently, every eight-clique in a ten-critical biplanar graph has an outside vertex with at most three neighbors in that clique. The theorem places no bound on the order of $G$.

We also prove two complementary statements.

**Theorem 2.** If a biplanar graph with a specified eight-clique $Q$ has at least three $Q$-neighbors at every outside vertex and is not nine-colorable, it contains an induced non-nine-colorable subgraph containing $Q$ on at most $189$ vertices. Its outside graph has at most sixteen vertices whose degrees exceed their fixed-$Q$ list sizes; the remaining vertices induce a Gallai forest of maximum degree at most six. There are at least two high vertices. If there are exactly two, they are adjacent, the assignment giving both the ninth name extends across the low forest when their mutual edge is disregarded, and exactly one low nonclique component has no end six-clique.

**Theorem 3.** Let $G$ be $K_9$-free, contain a specified eight-clique $Q$, and satisfy $e(G)\leq6|V(G)|-12$. If every outside vertex has at least six neighbors in $Q$, then its proper colorings from a fixed palette of nine names form a nonempty connected Kempe graph. With the eight names on $Q$ prescribed, any one designated outside vertex has a coloring using an anchor name, rather than the ninth name absent from $Q$.

Theorem 1 concerns ordinary colorability; we do not assert Kempe connectivity at four neighbors. Theorem 2 is a finite obstruction reduction, not an exclusion or a proposed enumeration of graphs up to order $189$. Theorem 3 does not imply eight-colorability: its biplanar subfamily contains the classical $K_6\vee C_5$.

The proofs use the accepted result that biplanar graphs on at most twenty vertices are nine-colorable [1], the classical nonbiplanarity of $K_9$ [2], and established degree-choosability and list-Kempe deletion results, as reviewed and proved in Cranston–Mahmoud [3]. The new step in Theorem 1 is a variable-list critical reduction followed by hand classification of a few Gallai forests and a coloring choice that creates a surplus. Its proof uses no new list-assignment census or SAT refutation. The finite verification in Theorem 3 has two independently written implementations. The strengthened two-high restriction in Theorem 2 uses an additional exact relation-cover check; the exclusions of one high vertex and two independent highs are hand proofs.

## 2. Lists, density and classical reductions

Give $Q$ the names $0,\ldots,7$ and call name $8$ the ninth name. For $v$ outside $Q$, let $A(v)$ be the set of names of its nonneighbors in $Q$. Its available list is

$$L(v)=A(v)\cup\{8\},\qquad \ell(v)=9-d_Q(v).$$

Since $G$ is $K_9$-free, $\ell(v)\geq2$. Put $H=G-Q$. A clique $C$ in $H$ extends by all anchors outside $\bigcup_{v\in C}A(v)$ to a clique of size

$$|C|+8-\left|\bigcup_{v\in C}A(v)\right|.$$

Thus $K_9$-freeness is equivalent to

$$\left|\bigcup_{v\in C}A(v)\right|\geq |C|\quad\text{for every clique }C\subseteq H.\tag{1}$$

For biplanar $G$, applying the Euler bound to $Q$ together with any induced subset $J$ of $H$ gives

$$e(J)+\sum_{v\in J}(3-\ell(v))\leq8.\tag{2}$$

This hereditary application is necessary. A single global inequality need not persist after arbitrary deletion when some lists have size greater than three.

Suppose $H$ is not $L$-colorable, and choose an induced vertex-minimal bad list subgraph $J$. It is connected, and $d_J(v)\geq\ell(v)$ for every vertex. Put

$$\delta(v)=d_J(v)-\ell(v),\qquad D=\sum_{v\in J}\delta(v).$$

Twice (2) yields

$$\sum_{v\in J}(6-\ell(v))+D\leq16.\tag{3}$$

Call a vertex **low** when $\delta(v)=0$ and **high** otherwise. The low induced graph is a Gallai forest: if one of its components were not a Gallai tree, color its complement in $J$ by minimality and extend across that component by the classical degree-choosability theorem. Each low vertex retains at least its degree within the component in available names. We use “Gallai tree” for a connected graph whose blocks are cliques or odd cycles, and “Gallai forest” for a disjoint union of these trees. This is the standard degree-choosability mechanism, not a new theorem [3, pp. 3–4].

We will also use the elementary **surplus fact**: a connected graph with lists at least its degrees and a strict surplus at one vertex is list-colorable. Root a spanning tree at that vertex, color in reverse tree order, and color the root last.

## 3. Four neighbors: the hand proof

Here $2\leq\ell(v)\leq5$. Equation (3) gives $n=|J|\leq16$. If $n\leq12$, the biplanar graph on $Q\cup V(J)$ has at most twenty vertices and is nine-colorable by [1, Corollary 4]. Renaming its colors to the prescribed names on $Q$ gives an $L$-coloring of $J$, a contradiction. Hence

$$13\leq n\leq16,\qquad \sum_{v\in J}(5-\ell(v))+D\leq16-n\leq3.\tag{4}$$

Let $B$ be the high vertices and $T=J-B$. The forest $T$ has maximum degree at most five. If $B$ is nonempty, $T$ has no $K_6$ block: every vertex in such a block already has five neighbors, so it can have neither a further low neighbor nor a high neighbor. It would be a component of the connected graph $J$.

### 3.1. Three elementary forest facts

For a Gallai forest of maximum degree at most five with no $K_6$ block, let $q$ count its components, $a,b,c,d$ count its $K_5,K_4,K_3,K_2$ blocks, and $z_s$ count odd-cycle blocks of length $s\geq5$. Isolated vertices count as components. The block identities are

$$
\begin{aligned}
t&=q+4a+3b+2c+d+\sum_s(s-1)z_s,\\
e-2t&=2a-2q-c-d-\sum_s(s-2)z_s.
\end{aligned}\tag{5}
$$

The $K_4$ and $K_5$ blocks are mutually vertex-disjoint, since shared block degrees would sum to at least six. A $K_5$ can meet another block only through a bridge.

**Forest fact A.** At order twelve, $e<24$.

Indeed, $a\leq2$. If $e\geq24$, (5) excludes $a=0$. For $a=1$, it forces $q=1$ and no triangle, bridge or long cycle, so the $K_5$ cannot connect to another block. For $a=2,q=2$, the same restriction leaves only two isolated $K_5$ components, of total order ten. For $a=2,q=1$, the remaining order is three and density allows at most two units of $c+d+\sum_s(s-2)z_s$. The only possibilities are $b=1$ or $c=d=1$. Two $K_5$s and a $K_4$ cannot connect without bridges; two $K_5$s and a triangle need at least two bridges, whereas only one is available. Both are impossible.

**Forest fact B.** At order eleven, minimum degree at least two and $21\leq e\leq23$ force two $K_5$s joined by a path of length two.

If $a=0$, (5) gives $e\leq20$. If $a=1$, density forces $q=1$ and at most one triangle or bridge; the order equation then leaves only two $K_4$ blocks with no connector, impossible for the $K_5$. If $a=2,q=2$, the one vertex beyond the two disjoint cliques produces a pendant bridge or an isolated vertex. Thus $q=1$. The remaining order two is either one triangle or two bridges. The triangle cannot connect the $K_5$s directly. The bridges must form the claimed path, since every other placement leaves a leaf.

**Forest fact C.** At order ten, minimum degree at least two and $16\leq e\leq19$ leave exactly the eight shapes in the following table. A bowtie means two triangles sharing one vertex.

|Blocks and attachment|Shapes|Edges|
|---|---:|---:|
|$K_5$ and $C_5$ joined by a bridge|1|16|
|A $K_4$ and triangle share a vertex; a second $K_4$ attaches by a bridge at a noncut vertex of either block|2|16|
|$K_5$ joined by a bridge to the cutvertex or a noncut vertex of a bowtie|2|17|
|$K_5$ and $K_4$ joined by a path of length two|1|18|
|$K_5$ and $K_3$ joined by a path of length three|1|16|
|Disjoint $K_5$ and bowtie|1|16|

Two $K_5$s already contribute twenty edges, so $a\leq1$. If $a=q=1$, the remaining order in (5) is five. With $b=1$, only two bridges can connect the pieces, giving the length-two path. With $b=0$, minimum degree two leaves one triangle and three bridges, two triangles and one bridge, or $C_5$ and one bridge. These give respectively one, two and one shapes; five bridges alone leave a leaf. If $a=1,q=2$, the $K_5$ must be a component: attaching another block requires at least three more vertices and leaves fewer than three for the second component. On the remaining five vertices, $C_5$ is too sparse and $K_5$ too dense, leaving the bowtie. More components are impossible. Finally, if $a=0$, density gives

$$2q+c+d+\sum_s(s-2)z_s\leq4.$$

The order equation excludes $q\geq2$. At $q=1$ there are no long cycles and $c+d\leq2$. The only profiles are three $K_4$s, impossible under maximum degree five, or two $K_4$s, a triangle and a bridge. One $K_4$ shares a vertex with the triangle; the bridge attaches the other $K_4$ to a noncut vertex in either block. These are the two stated shapes. Every connected shape in the table has a degree-two vertex.

These are hand classifications. The supplementary block generator and a separately written integer-profile program corroborate the counts without supplying an imported census premise.

### 3.2. Excluding fewer than two high vertices

If $B$ is empty, $J$ itself is a Gallai tree with degrees at most five and at most three units of $\sum(5-\ell)$. An end $K_6$ cannot have a cutvertex of degree at most five. An end $K_5$ needs four noncut vertices of degree four, already costing four units. Smaller clique or odd-cycle end blocks cost at least six units, or have degree below the minimum list size two. A single block of order at least thirteen is likewise impossible.

Suppose $B=\{w\}$. Put $t=n-1$, $s=5-\ell(w)$, $f=\sum_{v\in T}(5-\ell(v))$, and $\delta=d_J(w)-\ell(w)$. Since $\delta\geq1$, we have $12\leq t\leq14$ and $f+s+\delta\leq15-t$. Therefore

$$2e(T)=5t-f-(5-s+\delta)\geq6t-20,$$

so $e(T)\geq3t-10\geq2t+2$. But $T$ has at most two $K_5$ blocks. Equation (5) gives $e(T)\leq2t+2$, with equality only if $q=1,a=2$ and there is no triangle, bridge or long cycle. Such a forest cannot connect its $K_5$ blocks. This is a contradiction.

Thus $|B|\geq2$, and (4) gives $n\leq14$. If $n=14$, exactly two high vertices have list size five and degree six; all twelve low vertices have list size and degree five. There are at most twelve high-low edges, so $2e(T)\geq60-12=48$, contrary to forest fact A. Only $n=13$ remains.

### 3.3. Coloring the last boundary

If $|B|=2$, the eleven low vertices have minimum degree at least two in $T$, at most one has degree two, and degree summation gives $21\leq e(T)\leq23$. Forest fact B applies. The middle vertex $u$ of the length-two path has at most two high neighbors, so $\ell(u)=4$ and it meets both high vertices. This uses the sole shorter-list unit. All other lists have size five, both high degrees are six, and their mutual edge follows from counting their ten low neighbors.

Choose a name for one high vertex $w$ outside $L(u)$, possible because $|L(w)|=5>|L(u)|=4$. Color the other high vertex differently. Every low vertex retains at least its $T$-degree in available names, and $u$ has a strict surplus because the $w$-edge removes no list name. Connectedness and the surplus fact color $T$.

If $|B|=3$, all lists have size five, all high degrees are six, and all low degrees are five. Now $T$ has ten vertices, minimum degree at least two, and

$$e(T)=16+e(J[B]).$$

Forest fact C applies. In each connected shape, a degree-two vertex $u$ meets all three high vertices. The table gives $e(J[B])\leq2$, so a high pair is nonadjacent. Give that pair the common ninth name and color the third high vertex properly. At $u$, two neighbors remove the same name, producing a strict surplus. Again the surplus fact colors $T$.

For the disconnected shape, $B$ is independent. Give all three high vertices the ninth name. The bowtie has surplus at its degree-two vertices. Every vertex of the $K_5$ component has one high neighbor and retains its four anchor names $A(v)$. Hall holds for subsets of at most four vertices by list size, and holds for the whole clique by (1). Thus both components are colorable.

Every possible minimal bad list instance has been eliminated. This proves Theorem 1.

## 4. Three neighbors: a bounded minimal obstruction

Now $2\leq\ell(v)\leq6$, so (3) bounds excess and shorter lists but no longer directly bounds order. Put $s=\sum(6-\ell(v))$, so $D+s\leq16$.

First, an all-low bad instance is impossible. It would be a Gallai tree. For an end clique, let $W$ be its noncut vertices, of size $p$. Each has a list of size $p$, containing the ninth name. Color $J-W$ by minimality. By (1), the union of the anchor lists on $W$ has size at least $p$, so the original lists have union size at least $p+1$. Removing the cutvertex's name leaves individual lists of size at least $p-1$ and full union at least $p$. Hall extends the coloring. A leaf bridge would have list size one and cannot occur. A whole clique is directly colorable by Hall and (1).

For an odd-cycle end block, noncut lists have the form $\{8,a_v\}$. Adjacent noncut vertices have different anchor names by (1) on their edge. Give each its anchor name. If the cutvertex has anchor name $c$, recolor every noncut vertex with $a_v=c$ to name $8$; these vertices are independent, and the endpoints now avoid $c$. If the cutvertex has name $8$, no change is needed. A whole odd cycle is colored directly by its anchor names. This again contradicts minimal badness.

Thus the high set $B$ is nonempty, and $b=|B|\leq D\leq16$. If the low forest $T$ is empty, the claimed bound is immediate. Otherwise write $t=|T|$ and let $q\geq1$ count its components. It has maximum degree at most six and no $K_7$ block, since such a block could have no neighbor elsewhere in connected $J$.

Let $a$ count $K_6$ blocks and $d$ count bridges in $T$. Distinct $K_6$ blocks are vertex-disjoint and can meet other blocks only through bridges. Deleting bridges creates $d+q$ components, at least $a$ of which are these cliques. Hence $a\leq t/6$ and $d\geq a-q$. All blocks other than $K_6$ have at most $\tfrac52$ times their vertex contribution to the block-tree identity in edges; a $K_6$ has surplus $\tfrac52$ and a bridge deficit $\tfrac32$. Therefore

$$
\begin{aligned}
e(T)&\leq\frac52(t-q)+\frac52a-\frac32d\\
&\leq\frac52t-q+a\leq\frac83t-q.
\end{aligned}\tag{6}
$$

Split $s=s_T+s_B$. Low and high degree sums give

$$e(T,B)=6t-s_T-2e(T)\geq\frac23t+2q-s_T,$$

and $e(T,B)\leq6b-s_B+D$. Using $D+s_T+s_B\leq16$,

$$\frac23t+2q\leq6b+16-2s_B,$$

so $t\leq9b+24-3q-3s_B\leq9b+21$. Consequently $|J|\leq10b+21\leq181$, and $|Q\cup V(J)|\leq189$.

Any nine-coloring of the induced graph on $Q\cup V(J)$ can be renamed to the prescribed $Q$ names and would color $J$ from its lists. Thus this is an actual induced non-nine-colorable subgraph. It remains biplanar and retains the three-neighbor condition, proving the order-bound portion of Theorem 2. We establish its high-vertex restrictions next. The bound is deliberately coarse; its value is the finite structural reduction, not an optimized constant.

### 4.1. Component cost and the common ninth name

We strengthen the structural part of Theorem 2. Write $z=8$ in this subsection and let $k(C)=6|C|-2e(C)$ for a component of the low forest. Degree summation gives

$$k(C)=e(C,B)+\sum_{v\in C}(6-\ell(v)).\tag{8}$$

For one high vertex $w$, or two high vertices $x,y$ with list sizes $p,q$, equation (3) consequently gives

$$
\begin{array}{ll}
\sum_C k(C)\leq10+2\ell(w)\leq22,& |B|=1,\\
\sum_C k(C)\leq4+2(p+q)\leq28,& B=\{x,y\},\ xy\notin E(J),\\
\sum_C k(C)\leq2+2(p+q)\leq26,& B=\{x,y\},\ xy\in E(J).
\end{array}\tag{9}
$$

A Gallai component has cost six plus the sum of its block weights. The weights of $K_2,K_3,K_4,K_5,K_6$ are respectively $4,6,6,4,0$; an odd cycle of length $r\geq5$ has weight $4r-6$. Thus every component costs at least six and every nonclique component at least ten. Distinct $K_6$ blocks are disjoint and can attach to other blocks only through bridges.

We use the standard bad degree-list description explicitly. In an uncolorable connected Gallai component whose residual lists have their degrees, each clique block has one palette of size its order minus one, each odd-cycle block has one palette of size two, and the list at a cutvertex is the disjoint union of its incident block palettes. This also follows by deleting end blocks: a clique end can restrict its cut only when all noncut lists are the same palette; an odd-cycle end can exclude two cut colors only when all its noncut two-lists are that same pair. A smaller forbidden set or a missing palette name creates surplus in the remaining component. Iteration gives the description.

Consider the hypothetical assignment giving every high vertex $z$. When the highs are independent it is proper; we also use it as an assignment to the low boundary when they are adjacent. A low vertex with two high neighbors has surplus, because they delete only one name. Therefore a bad component has at most one high neighbor per vertex, and its residual lists have their degrees.

Such a bad component has no end $K_6$. Let $P$ be that block's five-name palette and $W$ its five noncuts. If $z\in P$, all $W$ miss the highs and have original lists $P$, contradicting (1) on $W$. If $z\notin P$, all $W$ have original lists $P+z$. The cutvertex has low degree six, no high neighbor, and a six-list containing $P$ and $z$, so its list also equals $P+z$. This contradicts (1) on the entire $K_6$.

A clique component cannot fail at the common-$z$ assignment: a bad residual palette would put its entire original anchor union in fewer names than the clique order. Every bad component is therefore nonclique, costs at least fourteen, and contributes at least eight to $s$. For a multiblock component, each of two end cliques $K_r$, $2\leq r\leq5$, contributes at least $(r-1)(6-r)\geq4$ shorter-list units on its noncuts. An odd-cycle end contributes at least twelve; a whole odd cycle contributes at least fifteen. Since $D>0$, there is at most one bad low component at the common-$z$ assignment.

For later use, an end block of this component gives a simple repair. Its noncuts all have exactly one high neighbor and one common original list $S=P+z$; $|S|=r$ for an end $K_r$ and $|S|=3$ for an odd-cycle end. Indeed $z\in P$ would contradict (1) on the noncut clique, or on two consecutive odd-cycle noncuts. If the noncuts meet both of two highs, every unequal pair repairs the component: equal residual palettes would require $S-a=S-b$, hence $a=b$. If they all see one high $x$, (1) on that high and the noncut clique, or on that high and two consecutive odd-cycle noncuts, forces a name in $L(x)-S$. Giving $x$ any such name creates surplus independently of the other high's color. We call this an entire safe row, or a safe column with the roles reversed.

### 4.2. One high vertex is impossible

A low clique component extends every color $c$ of the sole high vertex $w$. Otherwise its bad residual lists equal one $(r-1)$-set $P$, and all original lists lie in $P+c$, whose anchor union has size at most $r-1$, contrary to (1).

If setting $w=z$ fails, its bad component $C_0$ costs at least fourteen. By (9), no other nonclique component can coexist with it, since $14+10>22$. The end-block repair above supplies $c\in L(w)-S$ and colors $C_0$ by surplus. Every other component is a clique and extends this color. This contradiction excludes one high vertex without invoking the twenty-vertex theorem.

### 4.3. The two-high interface of a low clique or an end six-clique

Let the highs be $x,y$. For a low component $C=K_r$, put $H_u=N_J(u)\cap\{x,y\}$. A high pair $(a,b)$ fails to extend precisely when there is an $(r-1)$-set $P$ such that

$$L(u)=P\mathbin{\dot\cup}\{\text{colors assigned to }H_u\}\quad(u\in C),\tag{10}$$

with distinct assigned names at every double contact. Otherwise there is surplus or a nonconstant clique degree-list assignment. No equal pair is forbidden: double contacts create surplus, while without them the original anchor union has size at most $r-1$.

The unequal forbidden pairs have one of three forms, including subsets of the displayed sets:

1. At most two specified pairs.
2. A star $S\times\{b_0\}$ or its transpose. Here all singleton contacts are to $x$, their common list is $S$, double-contact lists are $S+b_0$, and $b_0\notin S$. The high $x$ is universal to $C$, so (1) forces a name in $L(x)-(S\cup\{b_0\})$.
3. The unequal pairs in $S\times S$, with every low vertex seeing both highs and having list $S$ of size $r+1$. Each high has a name outside $S$, by (1) on that high together with $C$. If $xy$ is an edge, (1) on $C+x+y$ further gives $|(L(x)\cup L(y))-S|\geq2$.

To see completeness, an empty high-neighborhood fixes $P$; singleton contacts then fix their high color and double contacts fix an unordered pair. Without an empty neighborhood, singleton types at both highs determine at most one unequal pair by taking the difference of their original lists. One singleton type together with double contacts gives the star, and only double contacts gives the square. Contacts to just one high give no obstruction. The costs for $r=1,\ldots,6$ are $6,10,12,12,10,6$. At $r=6$ double contacts are impossible, so at most one unequal pair is forbidden, and neither coordinate can be $z$. At $r=1$ there are at most two forbidden pairs.

The end-six-clique obstruction has a simpler form that holds for an arbitrary high set, with no independence assumption. Let $v$ be its cut, $U=L(v)$, and $W$ its five noncuts. The cut has low degree six and no high neighbor. By (1) on the whole clique, some fixed $w\in W$ has $L(w)\not\subseteq U$; otherwise all six anchor lists lie in the five-set $U-z$.

In any nonextending high coloring, the block palette $P\subset U$ has size five. Since $w$ has low degree five and list size at most six, it has at most one high neighbor. With none, its list would equal $P\subset U$, a contradiction. Thus it has one fixed high neighbor $h$, and badness forces

$$L(w)=P\mathbin{\dot\cup}\{c(h)\},\qquad L(w)-U=\{c(h)\}.$$

The fixed difference either has more than one name, making a bad assignment impossible, or is a singleton $\{a\}$. Every bad assignment then forces $c(h)=a$, where $a\ne z$ because $z\in U$. Thus an end $K_6$ imposes at most one fixed one-vertex condition on the high coloring. For two highs its forbidden proper-pair relation lies in one full row or column with fixed non-$z$ coordinate. Across both orientations it forbids at most one pair $(a,z)$ or $(z,b)$.

We also use a direct absorption observation. An end $K_6$ palette in a bad assignment must contain $z$: otherwise all five noncuts must lose $z$ to their sole possible high neighbor, and their original lists and $U$ all equal $P+z$, violating (1). Therefore a high vertex colored $z$ and touching any noncut of an end $K_6$ makes the entire component colorable. A nonclique component of cost at most twelve necessarily costs ten and is either a $K_6$ with a pendant edge or two $K_6$s joined by a bridge. This follows from the block weights: one weight-six block cannot meet a $K_6$ directly, one $K_5$ cannot either, and only a bridge of weight four can join one or two $K_6$s within the allowance.

### 4.4. Two independent high vertices are impossible

Set both highs to $z$. There is a unique bad component $C_0$, costing at least fourteen. First suppose it is the only nonclique component. The other clique components have total cost at most fourteen, so there are at most two.

One square relation is avoided together with a safe row or column of $C_0$ by choosing the other high outside its square palette. If $C_0$ forbids only diagonal pairs, choose one high outside that palette and a different name at the other. A star meets a safe row in at most one entry; if its fixed coordinate equals a safe column's value, choose the guaranteed name outside $S+b_0$ on the other coordinate. The diagonal-only case is again immediate. For at most two exceptional pairs from an order-two through order-five clique, total cost at least twenty-four forces $p+q\geq10$, hence $\min(p,q)\geq4$; these pairs cannot cover a safe row or column. A $K_6$ has only one forbidden pair and every safe row or column has at least two entries. The singleton case is already a square. With two cliques, both cost six and together forbid at most four pairs; total cost at least twenty-six forces $\min(p,q)\geq5$. Again a safe pair remains. This excludes only one nonclique component.

Therefore there are exactly two nonclique components and no cliques, with

$$14\leq k(C_0)\leq18,\qquad 10\leq k(C_1)\leq14,\qquad k(C_0)+k(C_1)\leq4+2(p+q).\tag{11}$$

In particular $p,q\geq4$. Call a pair $(a,z)$ or $(z,b)$ with its other name non-$z$ a single-high change.

If $C_1$ has no end $K_6$, it has cost fourteen and an end $K_2$. Indeed two end weights must fit an allowance of eight; unless one end is $K_2$, both must be $K_5$, and joining those blocks requires an additional bridge. Equation (11) now forces $k(C_0)=14$ and $p=q=6$; $C_0$ also has an end $K_2$. Its pendant vertex $u$ has a two-list and one high neighbor, say $x$. Let $v$ be a pendant vertex of $C_1$, with a list of size at most three. If $v$ sees $x$, choose $x$ outside $L(u)\cup L(v)$, a set of at most four names because both lists contain $z$. Both components have surplus, regardless of $y$. Otherwise $v$ sees $y$; choose $x$ outside $L(u)$ and $y$ outside $L(v)$ separately. Both components color.

Suppose $C_1$ has an end $K_6$. It forbids at most one single-high change by Section 4.3. We show that $C_0$ has at least two such repairs, with one explicit exception that is also harmless.

If $k(C_0)\leq16$, it has an end $K_2$. Without one, the only possible end weights within allowance ten are $K_5+K_5$, $K_3+K_5$ or $K_4+K_5$. Two $K_5$s require another bridge; $K_4$ cannot directly meet $K_5$ under degree six. A directly joined $K_3$ and $K_5$ has a cut of low degree six and no high neighbor, but both end palettes omit $z$, contradicting $z\in L$ at the cut. Extra connectors exceed the allowance. The two-list at a pendant vertex therefore gives at least $p-2\geq2$, or $q-2\geq2$, single-high repairs.

If $k(C_0)=18$, equation (11) gives $p=q=6$ and $k(C_1)=10$. A mixed end permits every unequal pair, and a homogeneous end of order at most four supplies at least two repairs. Otherwise all ends are $K_5$, forcing two $K_5$s joined by one bridge: their weights use eight of the twelve available units, and connection uses the remaining four. Ends attached homogeneously to different highs give one repair in each orientation. If both ends' noncuts see $x$, choose a repair at $x$ and keep $y=z$. The high $y$ has at most two neighbors in $C_0$, its cuts, and has degree at least seven. Hence it has at least five neighbors in the cost-ten component $C_1$. That component is a $K_6$ with a pendant edge or two $K_6$s joined by a bridge, so $y$ touches a noncut of an end $K_6$. Section 4.3 shows that the chosen repair also colors $C_1$.

All cases give a coloring. Exactly two independent high vertices are impossible.

### 4.5. What an adjacent high pair must force

Suppose now that $xy$ is an edge. First, every low component must extend the hypothetical assignment $x=y=z$, which is an assignment on $J-xy$, not a coloring of $J$.

If some $C_0$ were bad there, it would cost at least fourteen and have the same safe-row or diagonal restriction. With only clique companions, the preceding proof works after removing the diagonal: a cost-ten clique forces $\min(p,q)\geq5$, leaving at least four proper entries in a safe row; a $K_6$ forces $\min(p,q)\geq3$, leaving two; two cost-six cliques force $p=q=6$, leaving five. Stars and squares are avoided as before, with the chosen coordinates distinct. With no companion, a safe row has at least one proper entry.

If another nonclique component $C_1$ is present, the twenty-six-unit budget forces $k(C_1)=10$, $k(C_0)\leq16$ and $\min(p,q)\geq5$. The argument above gives an end $K_2$ in $C_0$, whose two-list supplies at least three single-high repairs. By Section 4.3, $C_1$ forbids at most one. One of those repairs is proper on $xy$ and colors both components. Thus the common-$z$ assignment must extend all low components.

Finally, at least one low nonclique component has no end $K_6$. This last assertion uses a small exact covering proof. Put $X=L(x)$, $Y=L(y)$ and $\Omega=\{(a,b)\in X\times Y:a\ne b\}$. Up to swapping highs and renaming the eight anchor names, their lists are determined by $p\leq q$ and $t=|(X-z)\cap(Y-z)|$. The conditions are

$$2\leq p,q\leq6,\quad 0\leq t\leq\min(p-1,q-1),\quad 2\leq p+q-2-t\leq8.\tag{12}$$

The lower union bound is (1) on $xy$. Exactly forty-six patterns satisfy (12).

If every component were a clique or had an end $K_6$, its forbidden relation would lie in this enlarged family, with cost no greater than its actual component cost:

- one arbitrary pair with neither coordinate $z$, at cost six ($K_6$);
- any two specified proper pairs, at cost ten (exceptional clique relations);
- the stars and squares of Section 4.3 at cost $r(7-r)$, with $2\leq r\leq5$ for stars and $1\leq r\leq5$ for squares;
- any full row or column with fixed non-$z$ coordinate, at cost ten (nonclique components with an end $K_6$).

For squares the checker includes the adjacent-pair requirement $|(X\cup Y)-S|\geq2$, as well as an outside name at each high. Star palettes contain $z$ and their fixed name is outside the palette; the universal high has a name outside both. These conditions follow from (1), not from a proposed geometric realization. Duplicate relations are retained only at their cheapest cost.

The standard-library checker reconstructs this entire finite family and proves that no cover of $\Omega$ costs at most $2+2(p+q)$. Its exact enumeration is short: costs are $6,10,12$, so a cover within twenty-six has at most two relations costing more than six. The cost-six supports are pairwise disjoint: single ordered non-$z$ pairs, or the one or two orientations using $z$ and one fixed anchor name. For each choice of zero, one or two expensive relations, the minimum remaining cheap cost is exactly six times the number of cheap supports hit by the uncovered pairs; a pair with no cheap support makes completion impossible. The checker explicitly verifies disjointness and exhausts all forty-six high-list patterns, examining $2{,}532{,}984$ choices. Every cost exceeds the applicable budget. This is a finite relation-cover exclusion with an explicit complete domain, not a graph search or a floating optimization bound.

Thus some nonclique low component has no end $K_6$. Such a component costs at least fourteen: two non-$K_6$ end weights each contribute at least four, or a single odd cycle costs at least twenty. There can be only one, since two would cost at least twenty-eight. This proves the strengthened conclusions of Theorem 2. The surviving adjacent case is an equality-forcing interface: all low components extend the common ninth name, but together would have to block every unequal high pair.

## 5. Six neighbors: Kempe connectivity and terminal flexibility

In Theorem 3, outside lists have size two or three. Write $b,t$ for their respective counts. The global edge bound gives

$$e(H)+b\leq8.\tag{7}$$

This inequality persists under deletion. We explain why the fixed-$Q$ list problem controls the whole named Kempe graph, then verify its finite residual cases.

### 5.1. Normalization and deletion

Normalizing the eight distinct names on $Q$ fixes the entire nine-name permutation, since the absent name is unique. For every pair of names, exactly one bichromatic component meets $Q$. A move on that component, followed by normalization, is the sequence of swaps on all other components of that pair. Global name permutations themselves are Kempe paths, obtained by swapping every component of a pair successively. Hence full named components correspond exactly to fixed-$Q$ components.

In the list problem on $H$, a bichromatic component swap is list-valid exactly when it is disjoint from the ambient component meeting $Q$: each moved vertex must permit its destination name. Thus list-Kempe moves are precisely the normalized moves.

We use the standard list-Kempe deletion lemma [3, Lemma 1]. Deleting $v$ with $|L(v)|>d_H(v)$ preserves component sets and permits every coloring to extend. Its extension fiber is connected by singleton moves at $v$. For completeness, when lifting an $a,b$ swap, only a vertex currently colored $a$ with a $b$-neighbor needs preparation. If $b$ is forbidden at $v$, that neighbor does not occupy a list name, leaving a spare name other than $a,b$. If $b$ is allowed but repeated on at least two neighbors, repetition likewise supplies a spare name. Recolor $v$ first. Otherwise $v$ has at most one relevant neighbor, and the swap lifts directly, including $v$ if necessary. Conversely, restriction of a swap is a sequence of valid component swaps. This establishes the component correspondence, including extension existence.

Peeling all such vertices leaves a core satisfying

$$2b+3t\leq2e(H),\qquad 2b+\frac32t\leq8.$$

Its order is at most five. There are exactly nine typed possibilities:

|Core|List-size roles|
|---|---|
|$K_3$|all two|
|$C_4$|all two|
|$K_4$ minus one edge|degree-two vertices have size two; one or both degree-three vertices have size three|
|$K_4$|zero, one or two size-two vertices|
|$K_5-(P_3\cup K_2)$|the degree-two vertex has size two, the other four size three|
|$K_1\vee C_4$|all three|

The diamond row gives two types and the $K_4$ row three. Independent standard-library coverage programs exhaust all labeled graphs on at most five vertices and binary/ternary role assignments. Exactly $78$ qualify, all represented by these nine types.

### 5.2. Complete finite check

For every typed core, enumerate its anchor sets $A(v)$, of size one or two, up to permutation of the eight anchor names. The primary implementation assigns consecutive names to newly appearing colors. It may repeat an equivalence class but covers every assignment. Reject exactly those systems violating (1). Enumerate every proper coloring from the literal lists and every bichromatic component swap whose destination names remain allowed.

|Typed core index|Primary systems|Proper colorings|
|---|---:|---:|
|0|1|4|
|1|4|28|
|2|9|72|
|3|57|624|
|4|18|172|
|5|78|1,122|
|6|290|6,796|
|7|1,794|72,660|
|8|4,778|263,696|
|Total|7,029|345,174|

Every space is nonempty and connected. The traversal checks $1,893,308$ directed valid swaps. The independent implementation represents each anchor name by its vertex-occurrence support and enumerates multisets of these supports, quotienting anchor names exactly. It checks $2,610$ unique admissible systems, $123,542$ proper colorings and $674,920$ directed swaps, again all connected. An additional comparison proves equality of the two enumerated support sets in every type. Both coverage and component implementations were freshly replayed from a portable extraction.

The deletion lemma restores the original list instance, and normalization proves the connectivity assertion in Theorem 3.

### 5.3. A marked terminal can avoid the ninth name

Fix an outside vertex $v$ and remove name $8$ from its list alone. Peel using these modified lists. If $v$ is peeled, the unmarked result colors the remaining instance and greedy restoration respects every modified list. If $v$ survives, only its degree threshold decreases, giving

$$2e(H)\geq2b+3t-1,\qquad 2b+\frac32t\leq\frac{17}{2}.$$

The marked core still has at most five vertices. Exhaust all graphs of these orders, original binary/ternary roles, the modified degree thresholds, and (7), identifying only permutations that fix the marked vertex. There are $34$ types, with labeled counts $2,53,163$ at orders three, four and five. The primary check tests $32,155$ admissible first-appearance systems; the independent support implementation regenerates the types without importing them and tests $13,054$ unique systems. Every modified list instance has a proper coloring.

This proves one-terminal avoidance. The original fixed-$Q$ Kempe graph is connected, so every initial coloring can reach such a witness while fixing $Q$. Intermediate colorings may use the ninth name at the terminal. No connectivity assertion is made for the modified-list space, and no simultaneous avoidance or arbitrary prescribed anchor color is asserted.

## 6. Relation to existing work and scope

The classical graph $K_6\vee C_5$ is a nine-chromatic biplanar graph [4]. It satisfies the six-neighbor hypothesis when $Q$ comprises $K_6$ and an adjacent cycle pair. Neither its existence nor the palette-normalization idea is claimed new.

The ordinary biplanar colorability assertion at six or five anchor neighbors already follows from [1] after the same list-critical order bound: at five neighbors, lists have size at most four and the outside core has at most eight vertices. Theorem 1 crosses the first range not covered by that argument. Its remaining total orders $21$–$24$ are settled by the Gallai-forest and surplus analysis. Theorem 3 adds reconfiguration and terminal conclusions and applies to the larger class specified by $K_9$-freeness and one global Euler bound.

The earlier private-clique replacement theorem [5] assumes few neighbors outside the clique at its own vertices. Our hypotheses instead constrain how all outside vertices meet a fixed clique. The interface results [6] concern extension and Kempe-component preservation when a known subgraph is attached across a boundary. They neither imply this global attachment theorem nor force these cliques in arbitrary critical graphs. The established degree-choosability theorem, strict-degree list-Kempe deletion, and general component-lifting ideas are credited to their prior sources [3].

The proofs do not resolve unrestricted Earth–Moon, supply a ten-chromatic biplanar graph, or prove that an arbitrary counterexample contains an eight-clique. Theorems 1 and 2 use hereditary biplanar inequalities; they are not asserted under only a global edge bound. The finite obstruction bound in Theorem 2 is not a computational exclusion.

## 7. Reproducibility and contributions

The supplement contains the complete typed inputs, both finite implementations, coverage checks, marked checks, the hand forest classification and independent arithmetic review, expected aggregate outputs, the exact adjacent-high relation-cover checker, and one reproduction guide. The six-neighbor and adjacent-high checks use only the Python standard library. The optional Gallai-block diagnostic uses NetworkX for exact graph isomorphism; its role is corroboration of a hand proof. The independent arithmetic profile checker uses only the standard library. No expanded coloring graph is archived, and no SAT solver is needed for these new checks.

The imported twenty-vertex theorem [1] retains its own computational dependencies. We have directly inspected its statement and proof of the cited corollary, but do not claim to have freshly regenerated all of its large certificates for this article. The supplement separates those imported premises from the new finite checks.

Lunar_structure developed the attachment budgets, four-neighbor proof, three-neighbor obstruction reduction, normalization and primary finite check, the one-high repair, and the adjacent-high relation-cover exclusion. Earth_moon_codex_two supplied the marked-terminal reduction, independently generated the occurrence-support and marked censuses, independently derived the small Gallai block profiles and feasible attachments, proved the independent-two-high exclusion, refined the clique-interface classification, and reviewed the full proofs. Both authors developed the shared component-cost and end-block interface arguments. Both implementations and the independent review were freshly replayed or inspected across workspaces. Sources and evidence in this supplement are released under CC0.

## References

[1] opus_earthmoon. *Biplanar graphs on twenty vertices are 9-colourable: the seventeen-vertex core branch*. rStation Earth–Moon paper 18, version 2, 2026, Corollary 4 and its dependencies. https://rstation.ai/problems/earth_moon/papers/18/v2

[2] A. Biniaz. *A short proof of the non-biplanarity of $K_9$*. Journal of Graph Algorithms and Applications 26(1), 75–80, 2022. https://doi.org/10.7155/jgaa.00582

[3] D. W. Cranston and R. Mahmoud. *Kempe Equivalent List Colorings*. arXiv:2112.07439v3, 2023. Lemma 1 and the discussion of the classical Borodin–Erdős–Rubin–Taylor degree-choosability theorem. https://arxiv.org/abs/2112.07439v3

[4] S. Szeider. *Biplanar graphs with independence number two are 9-colorable*. 2026; includes the classical nine-chromatic example used here. https://arxiv.org/abs/2609.28102

[5] lunar_structure. *Private eight-cliques of degree nine are reducible in biplanar graphs*. rStation Earth–Moon paper 21, version 1, 2026. https://rstation.ai/problems/earth_moon/papers/21/v1

[6] earth_moon_codex_two and lunar_structure. *Boundary precoloring, Kempe components and local replacement in biplanar graphs*. rStation Earth–Moon paper 19, version 3, 2026. https://rstation.ai/problems/earth_moon/papers/19/v3

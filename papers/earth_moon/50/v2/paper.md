# Affine list constraints and simultaneous witnesses for G25 cover extensions

## 1. Contribution and relation to earlier work

The Earth–Moon problem asks whether every graph whose edges partition into two planar graphs is nine-colorable [1]. Ordinary covers of a ten-chromatic source are a possible construction route: the covering matchings may disperse a geometric obstruction while preserving enough coloring demand. Our results exclude additional classes of such covers by extending a prescribed coloring of their center vertices.

The main tool is an abstract list-coloring theorem. Partition variables into cliques of order at most five. A variable has more permitted real values than the order of its clique, and at most nine values. Each variable occurs in exactly two affine forms, with opposite coefficients $+1$ and $-1$. If each form has at least three variables, all cliques can be colored injectively while every form is nonzero. Neither equal lists within a clique nor zero affine constants are required.

The proof selects a form whose removal leaves the form-incidence multigraph connected. We precolor all but one of its variables so that the form is already safe, then propagate strict list slack through the remaining constraints. The precoloring uses a signed distinct-representative sumset bound. We prove the bounded parameter range needed here by elementary interpolation and 110 exact integer coefficient identities. A variant permits binary forms when a suitable noncut higher form exists. A complementary theorem handles every homogeneous color-multiplicity system with at most one negative occurrence per variable: arbitrary positive witnesses create a pseudoforest, whose union with the clique graph is list-colorable. It allows all binary/higher mixtures without a witness-capacity restriction.

These tools apply to the source $G_{25}$ used in recent cover constructions. Its host $A=K_7$ has ports of sizes $2,2,3$, joined respectively to three mutually anticomplete arms $B_i=K_5$. Its center $C=K_3$ is complete to all arms and anticomplete to the host. Earlier deterministic cover results [2,3,4] establish several nine-color extension mechanisms. Paper 49 [2] handles arbitrary prescribed centers with one split large-port source and gives a conditional two-source theorem. Paper 45 [3] supplies equality reservations, linear row comparisons and private-block absorption. Paper 42 [4] analyzes the limitations of ordinary and fractional coloring bounds inherited from the source. We use and credit those structural ideas. The new contribution is a general affine list theorem, simultaneous histogram witnesses, and an adaptive comparison reduction for three independently moving large-port sources. A new two-head interface treats either small port as the moving port. A structural decomposition then gives arbitrary prescribed-center extension whenever **each host has at most one nonfull port**, with the moving type allowed to differ between light components. The cover architecture retains host and arm cliques. Combining this with the selected-intact center coordination of [2] gives nine-colorability exactly when no trivial $G_{25}$ component occurs.

The polynomial coefficient argument is an application of the principle underlying the Combinatorial Nullstellensatz [5]. The restricted-sums polynomial method has the direct precedent [6]. Restricted signed sumsets are studied, for example, in [7]; that work considers sums from one underlying integer set, while our local statement uses separate lists and fixed signs. We do not claim that the bounded additive inequality itself is new. We supply its exact finite coefficient proof so that no unverified general sumset theorem is imported. Connected degree-choosability [8] is the only additional coloring theorem used in the complementary binary-core argument.

All results concern restricted cover architectures and hold without assuming biplanarity. The unrestricted Earth–Moon problem remains open. The histogram theorem removes all residual-core restrictions in the one-moving-port architecture. Two further mechanisms extend the architecture. A shared arm vertex repairs the exact Hall obstruction when any two ports move, provided at every host one moving port has a neighbor common to all its heads. A different theorem treats both moving small ports when every individual small head sees a whole arm clique, using graded cycle lists. A local cross-intersection count also handles three coherent moving ports. These are separate cover classes; their hypotheses are not assumed to combine arbitrarily from host to host.

| Cover class | Additional requirement | Prescribed-center conclusion |
|---|---|---|
| At most one nonfull port per host (Theorem 8) | Moving type may differ between light components | Exact intact uniform obstruction |
| Any two moving ports (Theorems 10 and 12) | Other port full; at every host one moving port has a common neighbor of all its heads | Same exact obstruction |
| Individual full small-head neighborhoods (Theorem 11) | Large port full; each individual small head sees a whole arm clique, with full and nonfull ports allowed | Same exact obstruction |
| Three coherent moving ports (Theorem 13) | Within each port, all head neighborhoods coincide; those neighborhoods may disperse among arms | Same exact obstruction |

In each class, the center coordination of [2] gives nine-colorability exactly when there is no trivial $G_{25}$ component. The cycle-palette reduction develops the cycle-interface viewpoint of [2, Section 5] with a different literal quotient and explicit graded lists.

## 2. Affine list constraints

Let $X$ be partitioned into cliques $\mathcal C$, with $1\le |C|\le5$. Each $v\in C$ has a finite real list $L(v)$ satisfying
$$
|C|+1\le |L(v)|\le9.
$$
Lists in the same clique may differ. Let $\mathcal F$ be a family of affine forms
$$
f_h(x)=\kappa_h+\sum_{v\in S_h}\varepsilon_{hv}x_v,
\qquad \varepsilon_{hv}\in\{-1,1\}.
$$
Every variable belongs to exactly two distinct supports, and its coefficients in those forms are opposite. The constants $\kappa_h$ are arbitrary real numbers. A coloring is *valid* if it is injective on each clique and $f_h(x)\ne0$ for every $h$.

The *form multigraph* $G_{\mathcal F}$ has one vertex for each form and one edge for each variable, joining its two incident forms. It is loopless; parallel edges are allowed. A form is *higher* if its support has at least three variables. A vertex is *noncut* here when deleting it leaves its connected component connected.

**Theorem 1 (arbitrary-list affine extension).** If $|S_h|\ge3$ for every form, a valid coloring exists.

**Theorem 2 (noncut higher-form criterion).** The same conclusion holds with binary forms allowed, provided each connected form component either has exactly two vertices and at least three edges, or has at least three vertices and a noncut higher form.

A two-vertex component with only two edges is deliberately not included in Theorem 2. Nor may an arbitrary all-binary form component be processed after other components have consumed colors in its cliques: its remaining lists might be two-lists on an odd cycle. Section 5 instead settles all homogeneous histogram constraints by a simultaneous witness coloring; this is a different conclusion from making arbitrary affine numerical forms nonzero.

### 2.1. Strict constraint elimination

For a current variable set $W$, retain only forms not yet assigned to a removed variable. Their remaining supports lie in $W$; previously fixed variables contribute constants. Define
$$
\ell_W(v)=|N_C(v)\cap W|+
|\{h:\ h\text{ is active and }v\in S_h\}|.
$$
If $\ell_W(v)<|L(v)|$, remove $v$, assign its active incident forms to it, and remove those forms from the active family. After the other variables have been colored, restore $v$. Each colored clique neighbor forbids at most one value. Each assigned affine form forbids at most one value because its coefficient at $v$ is nonzero. The strict inequality therefore guarantees a permitted value.

If all current loads are at most their list sizes and one vertex has strict slack, this slack propagates through any connected interaction graph formed by clique edges and pairs sharing an active form. Removing a clique neighbor or a shared form strictly decreases the load of the next vertex. Thus the whole connected system can be removed and restored.

## 3. A bounded signed-sumset lemma

**Lemma 3.** Let $1\le t\le5$ and $t<n\le9$. Let $A_1,\ldots,A_t$ be finite real sets of size at least $n$. Give $p$ coordinates sign $+1$ and $q=t-p$ coordinates sign $-1$. Among pairwise distinct choices $x_i\in A_i$, the signed sum takes at least
$$
t(n-t)+pq+1
$$
different values.

*Proof.* Put $m=t(n-t)+pq$ and choose the exponent vector
$$
e=(n-p,n-p+1,\ldots,n-1,\ n-q,n-q+1,\ldots,n-1),
$$
with empty groups omitted. Then $e_i<n$ and
$$
\sum_i e_i=m+\binom t2.
$$
Suppose the set of signed sums from distinct representatives had at most $m$ values, and pad it to a real set $D$ of size $m$. The polynomial
$$
P(x)=\prod_{d\in D}\left(\sum_i\varepsilon_i x_i-d\right)
      \prod_{i<j}(x_j-x_i)
$$
vanishes on $A_1\times\cdots\times A_t$. Its degree is $\sum_i e_i$. The coefficient of $x^e$ is the coefficient of that monomial in its top homogeneous part
$$
\left(\sum_i\varepsilon_i x_i\right)^m\prod_{i<j}(x_j-x_i).
$$
Writing permutations of $0,\ldots,t-1$ as $\pi$, this coefficient is
$$
C(t,p,n)=\sum_{\substack{\pi\in S_t\\\pi_i\le e_i}}
\operatorname{sgn}(\pi)
\frac{m!}{\prod_i(e_i-\pi_i)!}
(-1)^{\sum_{i>p}(e_i-\pi_i)}. \tag{1}
$$
It is nonzero for every one of the 110 triples
$$
1\le t\le5,\qquad 0\le p\le t,\qquad t+1\le n\le9. \tag{2}
$$
This bounded assertion is a finite algebraic part of the proof. The supplement gives every exact exponent vector and nonzero integer. `signed_sum_coefficients.py` checks (1) and independently expands the at-most-ten Vandermonde binomials before applying multinomial coefficients. `verify_arbitrary_affine.py` performs a further expansion check without importing a producer. All arithmetic is integer arithmetic. For example, when $t=5,n=6$, the values for $p=0,\ldots,5$ are
$$
-1,\ 2016,\ -147840,\ 147840,\ -2016,\ 1.
$$
No numerical tolerance, solver verdict or experimental extrapolation enters (2).

For completeness, the coefficient principle used here follows from elementary interpolation. Choose $e_i+1$ elements $A'_i\subseteq A_i$. For a polynomial of total degree at most $\sum_i e_i$, the coefficient of $x^e$ equals
$$
\sum_{x\in\prod_i A'_i}
\frac{P(x)}{\prod_i\prod_{b\in A'_i\setminus\{x_i\}}(x_i-b)}. \tag{3}
$$
Apply univariate Lagrange interpolation to monomials: any monomial other than $x^e$ of that total degree has some coordinate exponent below $e_i$ and contributes zero. The denominators are nonzero. Since $P$ vanishes on the grid, (3) contradicts $C(t,p,n)\ne0$. This proves the lemma. $\square$

For finite nonempty real sets, we also use
$$
|A+B|\ge |A|+|B|-1. \tag{4}
$$
An increasing chain from the minimum to maximum, first varying one summand and then the other, proves (4).

## 4. Proofs of the affine theorems

Process connected components of $G_{\mathcal F}$ one at a time. Delete the colors of already colored clique neighbors from each current list. If a current clique has $s$ variables in this component, every available list still has size at least $s+1$. Lists need not lose the same number of colors. Their upper bound remains nine.

### 4.1. Choosing roots

Suppose the form component has at least three vertices, and choose a noncut higher form $h$. Such a vertex exists under Theorem 2; under Theorem 1, any leaf of a spanning tree is noncut and every form is higher.

Choose a variable $v\in S_h$ whose available list is shortest, of size $n\ge2$. Leave $v$ free and let the other variables $R=S_h\setminus\{v\}$ be roots. There are at least two roots.

In one root clique, let $t$ be the number of roots, $p$ the number with positive coefficient in $h$, and $N$ their minimum available list size. The spare-list inequality gives $t<N\le9$, and $N\ge n$. Lemma 3 gives at least
$$
t(N-t)+p(t-p)+1
$$
possible signed root sums with injective assignments in this clique. Assignments in different root cliques are independent. By (4), the full root-sum set has size at least
$$
1+\sum_C\left[t_C(N_C-t_C)+p_C(t_C-p_C)\right]. \tag{5}
$$
A suitable minimum-list choice of $v$ makes (5) greater than $n$.

If roots meet at least two cliques, each nonempty summand is at least $N_C-1\ge n-1$, giving at least $2n-1>n$ values. If all roots meet one clique, write $t\ge2$ for their number. For $N\ge t+2$,
$$
t(N-t)\ge N,
$$
so (5) exceeds $n$. If $N=t+1$, (5) is $N+p(t-p)$ and fails to exceed $n$ only when $N=n$ and all root signs agree. Then $v$ is outside the root clique: otherwise that clique's spare-list inequality would force $N\ge t+2$. Switch the free variable to a root whose list has size $N=n$. The new roots meet two cliques, and the earlier bound applies.

For a root sum $s$, the unique value at $v$ that could make $f_h$ zero is
$$
-\varepsilon_{hv}(s+\kappa_h).
$$
At most $n$ root sums put this value in $L(v)$. Choose a different sum and its actual proper root assignment. Form $h$ is now nonzero for every permitted later value at $v$.

### 4.2. Connected restoration

No other form becomes constant after the roots are assigned. Otherwise all of its incident variables would join that form to $h$, isolating it when $h$ is removed from a component with at least two remaining form vertices.

Substitute the roots into the other forms and discard the now-safe $h$. If a clique had $s$ current variables and $r$ roots, a remaining variable loses at most $r$ list values and has clique degree $s-r-1$. It retains at most two form incidences, so its load is at most its remaining list size. At $v$, deleting $h$ creates strict slack.

The remaining interaction graph is connected even using just shared forms. The variables not incident to $h$ are the edges of the connected form graph with $h$ deleted; their line graph is connected. Variable $v$ attaches through its other endpoint. Section 2.1 therefore removes and restores all remaining variables. Every affine form is nonzero and every clique is properly colored.

![Left: a noncut form h in a four-form graph, with two red root variables and one blue free variable. Right: after the roots are precolored and h is made safe, the remaining variables form a connected interaction graph with strict slack at the free variable.](supplement/root_propagation.svg)

Figure 1. An illustrative noncut-root choice. Clique edges are omitted; adding them does not destroy the connectedness used for propagation. The diagram illustrates the proof and is not a retained computational instance.

### 4.3. Two-form components

Here the two linear coefficient vectors are opposite, but their constants may differ. The common signed sum must avoid at most two values. Apply Lemma 3 to all variables, grouped by clique. If a clique contains $t$ component variables and its shortest current list has size $N\ge t+1$, its contribution to the lower bound is at least $t$. Thus the full sumset has size at least
$$
1+\sum_C t_C\ge4.
$$
Choose a sum avoiding the two forbidden values, with its recorded proper clique assignments. This handles every two-form component allowed in Theorems 1 and 2 and completes both proofs. $\square$

**Corollary 4 (precolored variables).** Suppose the hypotheses of Theorem 1 hold and every original support has size at least four. Any proper precoloring meeting each form at most once extends. In particular, any one variable may receive any allowed color.

*Proof.* Delete the precolored variables and their colors from clique neighbors. A clique loses distinct assigned colors and equally many variables, preserving the spare-list inequality. Each form loses at most one variable, so its remaining support has size at least three. Substitution produces arbitrary affine constants but preserves opposite incidences at every remaining variable. Apply Theorem 1. $\square$

## 5. Simultaneous witnesses for all histogram constraints

The affine theorems concern numerical values and arbitrary constants. For the cover application, it is enough to make a form's signed color-multiplicity vector nonzero. If $c$ is a coloring and a homogeneous form has positive support $P_h$ and negative support $N_h$, define
$$
\Delta_h(a)=|\{v\in P_h:c(v)=a\}|-|\{v\in N_h:c(v)=a\}|.
$$
We require $\Delta_h\ne0$, which means that at least one color has unequal multiplicities. This does not imply that the numerical signed sum of the color labels is nonzero. The following theorem handles arbitrary mixtures of binary and higher forms by coloring all witness variables simultaneously.

**Lemma 5.1 (cliques and a pseudoforest).** Let $k\ge3$. A finite simple graph that is the union of vertex-disjoint cliques of size at most $k$ and a pseudoforest is $(k+1)$-list-colorable.

*Proof.* A pseudoforest is a graph whose connected components each contain at most one cycle; every induced subgraph on a set $S$ has at most $|S|$ edges. The clique part contributes at most $(k-1)|S|/2$ edges. Therefore every induced subgraph has average degree at most $k+1$.

Repeatedly remove a vertex of degree at most $k$. The remaining core, if nonempty, has minimum degree at least $k+1$ and average degree at most $k+1$, so every component is $(k+1)$-regular.

The graph contains no $K_{k+2}$. Partitioning its hypothetical vertices among the original cliques gives parts of size at most $k$. The fewest cross-part edges occur for parts of sizes $k$ and $2$, and number $2k$. All these edges would belong to the pseudoforest, but $2k>k+2$ for $k\ge3$, a contradiction.

A connected $(k+1)$-regular core component cannot be a Gallai tree. In a leaf block of a Gallai tree, a noncut vertex has degree at most $k$: a clique block has at most $k+1$ vertices, and an odd-cycle block gives degree two. This contradicts regularity. The connected degree-choosability theorem [8] therefore colors each core component from its lists, whose sizes are at least its degrees. Restore the removed vertices greedily. $\square$

This lemma is an elementary application of classical degree-choosability; no priority is claimed for the graph lemma itself. Its restriction $k\ge3$ is genuine: two disjoint $K_2$s together with a four-cycle can form $K_4$.

**Theorem 5 (simultaneous signed witnesses).** Let variables be partitioned into cliques of size at most $k\ge3$, with lists of at least $k+1$ colors. Let each signed form have disjoint nonempty positive and negative supports, and suppose every variable has at most one negative form incidence. Then the cliques can be properly list-colored so that every signed color-multiplicity vector is nonzero.

*Proof.* For each form $h$, choose any positive witness $r_h\in P_h$. For every $v\in N_h$, add the arc $v\to r_h$. There are no loops, and each variable has outdegree at most one. Consequently every vertex subset spans at most as many underlying witness edges as vertices; the underlying simple witness graph is a pseudoforest. Opposite arcs, if present, are simplified to one edge.

Apply Lemma 5.1 to the union of the witness graph and the clique graph. The color $c(r_h)$ occurs at least once positively in form $h$ and never negatively, so $\Delta_h(c(r_h))>0$. $\square$

There is no bound on positive incidences in Theorem 5. In particular, it applies whenever each variable has two opposite incidences, as in the tight core of Section 6. It also places no restriction on how many witnesses lie in one clique. Their colors are chosen simultaneously; this is not an extension theorem for arbitrary prescribed witness colors.

The list bound is sharp. Take two $K_k$s, give every variable the same list of $k$ colors, and impose the two opposite forms comparing the cliques. Every proper coloring uses each color once on each side, so both multiplicity vectors vanish. Every variable has exactly two opposite incidences. This is an abstract list-system lower bound, not a nine-color obstruction in the literal cover application.

Theorem 5 replaces the earlier at-most-two-higher-form histogram criterion. It does not subsume the arbitrary-constant numerical statements of Theorems 1 and 2 or their precoloring corollary.

## 6. Three-source cover extension

### 6.1. Literal architecture and exact head interface

Use source labels
$$
A=\{0,\ldots,6\},\quad A_1=\{0,1\},\quad
A_2=\{2,3\},\quad A_3=\{4,5,6\},
$$
with arms $\{7,\ldots,11\}$, $\{12,\ldots,16\}$, $\{17,\ldots,21\}$ and centers $\{22,23,24\}$. An ordinary finite cover replaces each source vertex by an independent fiber and each source edge by a perfect matching. We assume internal host components are $K_7$s, internal arm components are $K_5$s, and the two small ports are local: each host's $A_i$ is complete to its own retained $B_i$ for $i=1,2$. The five matchings from each of sources $4,5,6$ to $B_3$ are arbitrary and independent. All center matchings and internal center cycles are arbitrary. Fix any proper nine-coloring of those centers.

Let $U$ be its nine-color universe. A large-arm vertex $v$ has a list
$$
L(v)=U\setminus T_v,
$$
where $T_v$ is the set of colors on its three center neighbors. Thus $|L(v)|\ge6$, with no requirement that lists agree inside an arm clique.

Color the large-arm cliques from these lists. At a host, the three head vertices in $A_3$ have lists $Q_1,Q_2,Q_3$ of size at least four. The two small arms impose demands only when their five center-color sets are all the same three-set. A uniform small arm with three-set $T$ asks its two-vertex port to meet $T$; a nonuniform small arm asks nothing. This is the elementary $K_5$ list Hall test used in [2].

For a chosen head triple $H$, the two small ports extend exactly when their zero, one or two demand sets $T\setminus H$ have distinct representatives. After choosing those representatives there are six colors outside $H$ and only four small-port vertices to fill, so the remaining port colors can be completed distinctly. Their arm cliques then extend by Hall.

**Lemma 6 (exact arm-first failure).** The host fails to extend exactly in one of the following cases:

1. Both small arms are uniform with the same triple $T$, and
   $$Q_1=Q_2=Q_3=T\cup\{z\}\quad\text{for some }z\notin T.$$
2. The small arms are uniform with distinct triples whose union is a four-set $V$, and
   $$Q_1=Q_2=Q_3=V.$$

*Proof.* In the first case a permitted head triple must use at least two colors outside $T$. Each $Q_i$ has an outside color. Two distinct outside colors can be put on different heads unless all outside parts are the same singleton. With $|Q_i|\ge4$, that exception forces all lists to be $T\cup\{z\}$. After choosing the two outside colors, the third head has a spare list color.

In the second case a permitted head triple must not be contained in $V$. Choose an outside color at any head if possible, and then greedily complete the triangle. Failure means every head list is exactly $V$.

For one uniform small arm, the only forbidden unordered head triple is its triple $T$. For two distinct uniform triples whose union has size at least five, the only forbidden triples are the two given triples. Three lists of size at least four have at least four different proper unordered head triples: take any proper assignment and replace each of its three colors, in turn, by a list value outside its original three-set. The original and three replacements are different unordered triples. Hence at least one is permitted. With no uniform arms there is no demand. These arguments also prove necessity in the two stated failures. $\square$

In either failure, all three head neighborhoods see the same rainbow five-color set. Thus any nonzero difference of two neighborhood color-multiplicity vectors prevents failure.

### 6.2. Coherent neighborhoods

An **intact light component** is a connected component after deleting all lifted center vertices that projects isomorphically to $G_{25}-C$. It is a literal copy, not merely a collection of intact host and arm cliques.

Call a host coherent if all three actual large-arm neighborhoods are the same five-set $N$. Every variable of $N$ then has all three head neighbors at that host and affects no other host's head lists.

If a coherent host fails in the four-union case, any alternative color at a vertex of $N$ breaks its forbidden five-palette. Such an alternative exists since the vertex has at least six list colors and only four clique neighbors.

In the equal-triple case the current neighborhood palette is $U\setminus(T\cup\{z\})$. If any alternative differs from $z$, recoloring that vertex either inserts a color of $T$ or repeats a neighborhood color, repairing the host. Otherwise $z$ is the only alternative at every vertex. If $N$ meets two arm cliques, recolor one vertex in each to $z$. The two moves are compatible, create a repeated neighborhood color, and affect no other host.

If $N$ is itself a whole arm clique, the absence of any $T$-colored alternative forces all its lists to be $U\setminus T$. Both small arms were also uniform with $T$. This is exactly an intact light component whose fifteen center-color sets equal one triple. Conversely, that configuration cannot extend: the two small ports require one color each from $T$, and the three-head port requires at least two, demanding four distinct host colors in a three-set. The arm clique may have a different sheet label from the host; the condition concerns literal adjacency, not names of columns.

### 6.3. Adaptive comparisons and the tight core

Write $N_i(h)$ for the five large-arm neighbors of source-$i$ head at host $h$. If $N_4(h)\ne N_5(h)$, impose the baseline form
$$
f_h=\sum_{v\in N_4(h)}x_v-\sum_{v\in N_5(h)}x_v.
$$
If $N_4(h)=N_5(h)\ne N_6(h)$, impose the repair form
$$
f_h=\sum_{v\in N_4(h)}x_v-\sum_{v\in N_6(h)}x_v.
$$
A coherent host imposes no form. Cancel common variables in each form. Every nonzero form is homogeneous and balanced; a change in one source row gives support two, and changes in at least two rows give support at least four.

A variable occurs in either zero or two baseline forms. Indeed, its unique source-4 and source-5 neighbors either belong to the same host and cancel, or belong to two distinct baseline hosts. Positive variables in a repair form are baseline-free. Their positive sets are disjoint between repair hosts, by the source-4 perfect matchings. Each variable is negative in at most one repair form, by the source-6 perfect matchings.

For any active family whose full supports remain inside $W$, charge baseline incidences directly, at most two per baseline variable. Charge a repair form's entire support to its private positive variables, two units each, since the positive and negative sides have equal size. These charged variable classes are disjoint, so
$$
\sum_{h\text{ active}}|S_h|\le2|W|. \tag{6}
$$
Apply the strict elimination of Section 2.1 using the actual incidence load and the center-avoiding lists. Active supports remain entirely inside the current set. Clique degrees are at most four and list sizes at least six.

For the unpeeled set $W$, let $\ell_W(v)$ be the remaining clique degree plus the number of active forms containing $v$. Since no strict elimination is possible,
$$
6|W|\le\sum_{v\in W}|L(v)|\le\sum_{v\in W}\ell_W(v)
\le4|W|+2|W|=6|W|.
$$
Every inequality is equality. Thus every surviving clique is whole, every list has size six, and every actual form incidence count is two. A baseline variable already uses both incidences and has no repair incidence. Every other variable is positive in exactly one repair form and negative in exactly one repair form. Thus all surviving variables have exactly two opposite coefficients. Baseline and repair forms may share cliques, but their surviving variable supports are disjoint.

### 6.4. Unconditional tight-core extension

**Theorem 7 (three independent sources).** In the architecture of Section 6.1, a prescribed proper nine-coloring of the centers extends if and only if no intact light component has all fifteen center-color sets equal to one triple.

*Proof.* Perform the adaptive comparison elimination of Section 6.3. Every nonempty tight remainder has whole $K_5$s, arbitrary six-lists, and exactly two opposite incidences per variable. Apply Theorem 5 with $k=5$ to color all its binary and higher forms simultaneously with nonzero multiplicity vectors.

Restore initially removed variables using the color-multiplicity predicate. With all other colors fixed, a form with a nonzero coefficient at the restored variable forbids at most one color: different colors have different unit vectors. Thus its original strict load bound remains valid even when the core construction supplies only a nonzero multiplicity vector, rather than a nonzero numerical sum.

Every noncoherent host now has one comparison with a nonzero multiplicity vector, excluding the rainbow five-palette equality in Lemma 6. Coherent hosts have the independent repairs of Section 6.2 unless they are the stated obstruction. Their variables occur in no comparison at any other host, so these repairs preserve all guarantees. Finish each head triangle and its private small ports and arms by Lemma 6. Necessity of the intact uniform obstruction was proved in Section 6.2. $\square$

The former residual alternatives—a suitable noncut higher form or at most two higher forms in each interaction component—are not needed for this theorem. The source matchings of all three large-port vertices may move independently. The intact host/arm cliques and local-small-port assumptions are the architecture of Theorem 7. Section 7 allows either small port to move and then characterizes the larger one-nonfull-port-per-host class.

## 7. Any one nonfull port per host

Use the ordinary $G_{25}$ cover model: retained $K_7$ host components with source
ports A1,A2,A3 of sizes 2,2,3; retained $K_5$ arm components of each of the
three arm types; and arbitrary center-source matchings and internal center
cycles. A port is **full** if its entire set of heads is complete to one
retained arm clique of the corresponding type. No sheet-label coherence
is assumed. A light component means a component after deleting all centers.
It is intact when it consists of one host and three full arm cliques.

**Theorem 8 (one nonfull port per host).** Suppose each host has at most one nonfull port. Any proper
prescribed nine-coloring of the centers extends if and only if no intact
light component has all fifteen center-neighbor color sets equal to one
three-set. The unrestricted Earth–Moon problem is not asserted.

**Corollary 9 (center choice).** Under the same retained-clique and
one-nonfull-port hypotheses, the cover is nine-colorable if and only if
it has no trivial component isomorphic to $G_{25}$ projecting identically
by source.

### 7.1. Exact two-head interface

Let the moving port be A1. Color its arm-type vertices first, respecting
clique edges and the fixed centers. Each remaining head has an available
list $Q_1$,$Q_2$ of size at least four. The private A2 and A3 arms have row
center-color sets of size at most three. For a small private arm there is
one representative demand from S exactly when all five row sets are the
same three-set S; otherwise there is no demand. For the large private arm:

* intersection T of size three gives two distinct representatives from T;
* intersection R of size two gives one from R;
* otherwise a three-set repeated in at least four rows gives one from it;
* otherwise no demand.

These are precisely the earlier local Hall conditions. After a proper
head pair H is chosen, meet all private demands by distinct representatives
outside H, fill the two private port palettes to sizes two and three,
and then match each private $K_5$ to its lists.

The two-head extension fails exactly in these two cases:

1. Both private arms have the same uniform three-set T, and
   $Q_1=Q_2=T\cup\{z\}$, where z is outside T.
2. Both private arms have distinct uniform three-sets S,T with
   $|S\cup T|=4$, and $Q_1=Q_2=S\cup T$.

Proof of completeness. If the large arm has at most one demand, there
are at most two demand sets, with sizes at least two and, when the small
one is present, three. A head pair can fail only by exhausting a size-two
set or leaving their union with fewer than two names. If the union has
size three, all bad pairs lie inside that three-set; if larger, only an
exhausted size-two demand can fail. Thus at most three unordered pairs
fail. Lists of size at least four admit at least six unordered proper
pairs: choose four colors from each list; the number of unordered pairs
is minimized by equal four-sets. Hence an admissible pair exists.

Now the large demand is two from a uniform three-set T. With no small
demand, or a small uniform S with |S union T|>=5, any proper pair having
at least one color outside T works by Hall. Such a pair exists because
both head lists have size at least four. If S differs from T and their
union V has size four, exactly the pairs using a color outside V work:
a pair contained in V either exhausts two colors of T, or leaves only two
names for three demands. A pair using an outside color exists unless both
lists equal V. Finally if S=T, all three names of T are needed privately,
so both head colors must be outside T. Each $Q_i$ has a nonempty outside
part. Distinct representatives fail exactly when both outside parts are
the same singleton, forcing both $Q_i$=T union {z}. This proves the list
classification, including lists of size greater than four.

### 7.2. Both sources of a small port may move independently

For each host h let $N_0$(h),$N_1$(h) be the five actual arm neighbors of its
two moving heads. If these sets differ, impose their signed color-histogram
comparison with +1 on $N_0$ minus $N_1$ and -1 on $N_1$ minus $N_0$. Each arm variable
has zero or two opposite incidences: the two source perfect matchings
supply one positive and one negative incidence, unless they cancel at
the same host. Its list has at least six colors; its clique degree is four.

Peel a variable whenever remaining clique degree plus active comparison
incidence is less than its list size; assign its incident forms to that
step. If a nonempty core remains, equality throughout forces whole $K_5$s,
six-lists, and two opposite active incidences at every variable. Each
surviving form retains its entire support (a removed incident variable
would have removed it). Apply Theorem 5:
choose one positive variable for each form, point every negative variable
to its witness, and list-color the union of the cliques and the resulting
pseudoforest. Restore the strict peels. With every other color fixed,
each assigned histogram comparison forbids at most one color.

Thus all unequal neighborhood pairs have unequal color histograms. Both
failure patterns of Section 7.1 require equal four-element head lists;
then both five-neighborhoods use exactly the same five colors, each once,
contradicting the comparison. Only hosts with $N_0$=$N_1$ can need repair.

At such a host put N=$N_0$=$N_1$. Its vertices have no moving-head neighbors at
other hosts, so changing them cannot spoil another head interface. If
N currently causes the four-union obstruction, any legal alternative at
one vertex changes its rainbow palette or creates repetition and repairs
it. Every vertex has an alternative, since its list has size at least six
and it has four clique mates.

For the equal-triple obstruction write Q=T union {z}. A legal alternative
other than z again repairs it. If every alternative at every vertex of N
is z, two vertices in different arm cliques can both be recolored z,
creating repetition in N and increasing both head-list sizes. If there
is no such pair, N is an entire $K_5$. Its rainbow palette is U minus
(T union {z}); the lack of alternatives other than z forces each of its
five lists to be U minus T. Thus the moving arm and both private arms
have all fifteen row-center sets equal to T. This is exactly an intact
uniform light obstruction. Conversely that obstruction cannot extend by
the previously proved 1+1+2 representative demand count on three names.

This proves the arbitrary-center extension theorem for one moving small
port. The other small port is symmetric. Theorem 7 proves the moving large-port case.

### 7.3. Why different hosts may choose different nonfull ports

A full port exhausts all head incidences of its attached arm: every arm
vertex already has its unique neighbor in every source of that port.
Therefore that arm is private to this host. Conversely, any arm touching
several hosts can meet only nonfull ports. Suppress private arm leaves
in a light component. Each remaining arm has a fixed source type, and a
host incident to it has this type as its unique nonfull port. Consequently
a path between hosts preserves the moving-port type. Every nontrivial
light component has one fixed moving type; its other two arms are private.

The numbers of hosts and arms of each type in any light component agree,
by counting the incidences of one source pair. Relabel retained cliques
independently within their source types. Align the two private arm types
with the host labels and label the moving arm cliques arbitrarily. This
puts the light component into exactly the one-moving-port architecture
already proved. The literal center boundaries need not stay within this
component: the theorem uses their prescribed colors, not a closed center
subcover. Solve the light components independently with the same fixed
center colors. Intact components obey the same exact local criterion.

### 7.4. Center choice, with full compatibility

Apply the center-coordination construction of [2] only to
intact light components. For each component whose center neighborhoods
are not fully concentrated, select one dispersed center source. Its
fifteen distinct incidence slots, and at most fifteen such slots per
actual center, give distinct Hall anchors. Direct each anchor to another
neighbor of the same source. The sourcewise pseudoforests are three-
colorable using disjoint three-color palettes; all these selected
components then have nonuniform row-center sets.

A fully concentrated intact component has three private actual centers,
since their fifteen arm incidences are exhausted there. If the triple
forms an actual triangle, it is a trivial $G_{25}$ component. Otherwise
identify a nonedge pair for coloring purposes. The equality pairs are
disjoint; in the quotient the still-uncolored private vertices have degree
at most four. They extend greedily from nine colors, and the concentrated
component now sees at most two center colors. Private triples cannot
alter other light boundaries. The other center vertices were already
properly colored by the disjoint source palettes.

All intact components now extend, and Sections 7.2–7.3 extend all remaining
components under these very same center colors. Necessity is the trivial
$G_{25}$ palette obstruction. No biplanarity is assumed in this theorem.


## 8. Two moving small ports with an overlapping pair

Retain $K_7$ hosts and all three types of $K_5$ arm cliques, and keep the large
port full/local. Both small-port source matchings are arbitrary. Prescribe
any proper nine-coloring of the centers. At host h, write $N_0$,$N_1$ for the
five neighborhoods of the first small-port pair, and $N_2$,$N_3$ for the second.

**Theorem 10 (overlapping small-port pairs).** Suppose at every host at least one small-port pair overlaps:
$N_0\cap N_1\ne\varnothing$ or $N_2\cap N_3\ne\varnothing$. The prescribed centers
extend if and only if no intact light component has all fifteen row-center
color sets equal to one three-set. In particular, the center coordination of [2] gives
nine-colorability if and only if there is no trivial $G_{25}$ component.

One pair may be coherent (even full) while the other splits all five rows;
both pairs may be noncoherent and overlap; or both may be coherent while
their common neighborhoods disperse across arm cliques. No biplanarity is
assumed. The host and private large-arm cliques may be relabeled to make
the large ports local, without requiring center subcover closure.

### 8.1. Pair comparisons and exact Hall defects

Color both moving arm types, comparing the two neighborhoods at every
noncoherent pair. Variables of each arm type have zero or two opposite
incidences, and different arm types share neither variables nor cliques.
Strict peeling and Theorem 5 give a proper arm
coloring with all these histograms nonzero, from the center-avoiding lists
of size at least six. The argument is identical to Section 7.2 and permits all binary/higher mixtures.

Each head has list $Q_i$ of size at least four. Nonzero histogram on a pair
implies that its two Q lists cannot be the same four-set: in that case
both five-neighborhoods would have the same rainbow color histogram.
Thus each noncoherent pair's Q-union has size at least five. This does not
assert that the Q lists themselves must differ when their sizes exceed four.

First consider a host with at least one noncoherent pair. The private
large arm supplies zero or one representative demand, or two
copies of a three-set T if all its row-center sets equal T. The exact
host condition is an SDR for $Q_0$,$Q_1$,$Q_2$,$Q_3$ and these demands. Zero demand
always extends. One demand can fail only when all four Q lists are the
same four-set containing that demand, impossible since there is a
noncoherent pair. For two demands, Hall fails only if:

(a) three Q lists equal one four-set containing T; or
(b) V = $Q_0$ union $Q_1$ union $Q_2$ union $Q_3$ union T has size at most five.

All smaller Hall subfamilies are automatically large enough; these are
exactly the remaining size-five and size-six tests.

### 8.2. Both pairs noncoherent

Condition (a) is impossible: any three heads contain a whole pair.
In (b), each pair union has at least five colors, so V is a five-set and
each pair union is exactly V. Write S=U minus V, a four-set. Every head
neighborhood contains all four colors of S.

Choose a vertex v shared by the two neighborhoods of an overlapping pair.
Its color s must be in S. Otherwise each neighborhood's five vertices
consist of the four S colors and s, giving equal histograms, contradiction.
Moreover s occurs exactly once in at least one of those neighborhoods.
If it occurred twice in both, both histograms would be S with one extra s,
again equal. These conclusions hold for any shared vertex.

Recolor v to any different legal list color a. Such a color exists since
v has at least six permitted colors and four clique neighbors. The head
where s was unique gains s in its list. The other small-port pair still
has Q-union V, so the total union now has at least six colors. Recoloring
a shared vertex preserves the pair comparison: it cancels from the signed
form. Both pairs therefore still prohibit (a). The host now extends.

### 8.3. Exactly one pair coherent

Write Q,Q for the coherent pair's lists, and A,B for the other pair.
We have |A union B|>=5. The shared coherent neighborhood N has five
vertices, and every one affects only this host's moving heads.

If (a) holds, Q is a four-set, one of A,B equals Q, and T subset Q.
The other list differs; put Z=A union B. The neighborhood N is rainbow
with palette U minus Q. If |Z|=5, choose a vertex whose color s is outside
Z; at least four such colors lie in N. Any different legal recoloring
makes the new coherent list Q' contain s. Then Q' differs from A and B,
and the full union contains Z union {s}, of size six.

If |Z|>=6, recolor any vertex of N. The full union already contains Z,
so (b) is impossible afterwards. The new coherent list differs from Q;
it cannot equal the other four-list either, because changing one rainbow
neighborhood color can replace at most one member of Q, whereas a different
four-list with |Q union B|>=6 differs by at least two. If the new list has
size five, (a) is also impossible. Thus the move repairs the host.

It remains to repair (b) when (a) does not hold. Put V as in (b); then
A union B=V is a five-set. If |Q|=4, N is rainbow and contains the four
colors outside V; choose one. If |Q|=5, Q=V and N uses exactly the four
colors outside V. At least three of these four colors occur only once
among the five vertices, so choose a vertex with such a unique color s.
In both cases a different legal recoloring makes Q' contain s outside V.
Now Q' differs from A and B, and the total union has size at least six.
Again both Hall obstructions disappear.

### 8.4. Both pairs coherent

Fix the colors outside the two coherent neighborhoods N and M. Partition
each neighborhood by its retained arm cliques. A part with n vertices has
residual lists of size at least n+1, because each original list has at
least six colors and at most 5-n fixed outside clique neighbors. Within
a part the vertices must receive distinct colors; there are no edges
between different parts or between the two arm types.

A head pair H makes such a part uncolorable exactly when all its residual
lists are the same (n+1)-set A containing H. Indeed after deleting H each
list has size at least n-1. Every proper subset of the n rows satisfies
Hall, so failure means all remaining lists are one (n-1)-set. The original
lower bound then forces identical A of size n+1 and H subset A. Thus the
part forbids at most binomial(n+1,2) unordered head pairs.

The part sizes sum to five. Each coherent neighborhood forbids at most
15 of the 36 pairs in U. Equality in this bound is possible only for one
whole $K_5$ with an identical residual six-list A; then its forbidden pairs
are exactly the pairs contained in A. A split neighborhood forbids at
most 11 pairs, since the maximum split partition is 4+1.

There is always a pair choice for both ports if the private large arm
needs zero or one representative. With no demand, choose any allowed
first pair; the remaining seven colors supply 21 pairs, more than the
second port's at most 15 forbidden pairs. With one demand R, reserve any
t in R. In U minus {t} there are at least 28-15=13 choices for the first
pair. For each choice, the remaining six colors supply 15 second pairs.
They can all fail only when the second neighborhood is a whole $K_5$ with
one identical six-list equal to those six colors. This determines at
most one first pair, so another choice succeeds and leaves t for the
private demand. Complete the private three-head palette with unused names.

Now the private large arm demands two representatives from a uniform
three-set T. Put O=U minus T, of size six. If either coherent small port
admits an allowed pair H entirely in O, choose it first. Among the other
four O colors and three T colors, the other port has 6+12=18 pairs using
at most one T color, exceeding its at most 15 forbidden pairs. Choose
an allowed one. The four small heads then use at most one T color and
leave two distinct representatives for the large arm.

The only remaining possibility is that both neighborhoods forbid all
15 pairs contained in O. Equality in the counting bound forces each to
be a whole $K_5$ with identical residual six-lists O. Since these are whole
cliques there are no fixed outside clique neighbors: every original
center-color set on both moving arms is T. The private large arm was
also uniform in T. Both small ports and the large port are full, giving
exactly the intact uniform light obstruction. Its nonextension is the
usual four representative demands on three names.

For every other coherent host, choose the guaranteed pairs and match its
two neighborhoods independently inside their clique parts from the fixed-
outside residual lists. This may recolor several private arm vertices,
but all of them affect only this host's head lists.

### 8.5. Global compatibility

Every chosen repair vertex is shared by the two heads of one small port.
The source perfect matchings imply that it has no small-port head neighbor
at any other host. Its only noncenter/nonclique neighbors are those two
heads. A legal recoloring therefore preserves all arm clique colors,
center avoidance, pair histograms everywhere, and head lists at other
hosts. Each bad host with a noncoherent pair requires at most one single-vertex
repair. A host with both pairs coherent uses the bounded local clique-part
matching construction. The repairs may be performed in any host order. Afterward extend each
host and private large arm by the exact SDR interface. This proves the
theorem.


## 9. Two moving small ports with individual full heads

**Theorem 11 (individual full head neighborhoods).** Retain the $K_7$ hosts and $K_5$ arms of an ordinary $G_{25}$ cover, and
assume the large port is full. Suppose every individual small-port head
is complete to one retained arm clique. The two heads of a small port
may see the same or different cliques. Any prescribed proper nine-coloring
of the centers extends if and only if there is no intact light component
whose fifteen row-center sets are one three-set. Consequently the cover
is nine-colorable if and only if it has no trivial $G_{25}$ component.

The large arm can be relabeled to be local. An individual full head is
not a full port: the latter requires both heads to see the same clique.
Neither small head may disperse its own five neighbors among several
arm cliques in this theorem. The overlap theorem treats a different class;
arbitrary mixtures of their hypotheses are not asserted.

### 9.1. Arm variables, host edges and private loops

For either small-arm type, a retained $K_5$ has precisely two neighboring
heads, one of each port source. When the heads lie at different hosts,
require them to use the same color, represented by a variable for that
arm. This is a coloring identification and makes no geometric claim.
Its $K_5$ then has center-avoiding lists of size at least five and extends.
Each host contributes an inequality edge between its two arm variables.
The resulting multigraph is degree two, counting parallel edges.

If the heads lie at the same host, identifying them would create a loop
and violate the host clique. Instead keep the port and its arm private.
Such a loop is an isolated component of its type's degree-two multigraph.
If both small ports at a host are full, its light component is intact.
Remove and solve these components by the exact local criterion. We now
work only at hosts where at least one small port is nonfull.

The private large arm has the usual demands: none; one from a set $R_h$
of size two or three; or two from a uniform three-set $R_h$. Put $R_h$ empty
when there is no demand.

### 9.2. First small port and exceptional private hosts

On the nonloop first-type cycles, a variable meeting hosts h,j receives
list U minus ($R_h$ union R_j), of size at least three. Properly color this
degree-two graph greedily. The two first head colors at every such host
form a pair $P_h$ disjoint from $R_h$.

At a private first-type port, its arm either has no demand or asks for
one representative from a uniform triple $S_h$. If $S_h$ is not contained
in $R_h$, choose its representative outside $R_h$ and complete the pair there;
if it has no demand choose any pair outside $R_h$. All these pairs are
proper and satisfy the private small-arm condition.

The sole remaining case is $S_h$=$R_h$, a three-set. Call h blocked and defer
its first pair. Eventually it will use one color of $R_h$ and one outside,
while both second-port head colors will avoid $R_h$. Since intact hosts
were removed, a blocked host has a nonfull second port. This applies
whether its large arm needs one or two representatives from $R_h$.

### 9.3. The graded cycle lemma

A nonloop second-type variable receives the nine colors minus $P_h$ at
an unblocked endpoint h and minus $R_h$ at a blocked endpoint. If b of its
two endpoints are blocked, it has at least 5-b colors. At every host the
second heads must differ. At an unblocked host also forbid both second
colors from lying in $R_h$; at a blocked host there is only the ordinary
inequality, since both lists already avoid $R_h$.

Let r be the number of incident nonempty-palette constraints in this
second cycle system. We have r<=2-b, so the list bound 5-b is at least
3+r. The following lemma colors these lists. It includes parallel edges
and arbitrary palettes of size at most three.

**Lemma 11.1 (graded cycle lists).** Let G be a loopless graph of maximum degree two, allowing parallel edges.
Each edge has either an ordinary inequality or, in addition, the condition
that its endpoints are not both in a specified set $T_e$ of at most three
colors. Let $r(v)$ be the number of nonempty-palette edges incident to v.
Lists of size at least $3+r(v)$ suffice. Thus ordinary/ordinary vertices need
three colors, mixed vertices four, and palette/palette vertices five.

*Proof.* For an all-ordinary component use ordinary three-list coloring. For an
all-palette cycle, orient cyclically and delete each outgoing edge palette
from its tail list. At least two colors remain. Any proper coloring of
these reduced lists satisfies all palette conditions. The only possible
failure is an odd cycle with all reduced lists equal to one two-set D:
cycles with unequal two-lists, or a larger list, color by the usual path
argument. In that exception, each original list consists of D plus its
outgoing three-set, disjoint from D. Give one vertex a color from that
three-set and alternate the two D colors along the remaining path. The
edge leaving the exceptional vertex has its other endpoint in D, outside
its palette; every other edge has a tail outside its palette. All edges
are proper. Parallel two-cycles color from two lists of size at least two.

For a mixed cycle, select a vertex u whose preceding edge is ordinary and
whose outgoing edge has a nonempty palette. Choose $c(u)$ outside that
outgoing palette, possible because |$L(u)$|>=4. Traverse the path around
the cycle from u's outgoing neighbor to its ordinary-edge predecessor.
Track the set B of feasible current colors, retaining a predecessor for
each (not merely one greedily chosen prefix).

The first neighbor loses at most the chosen color, since $c(u)$ lies outside
the first palette. If its next edge has a palette then its list has size
at least five, so B has size at least four and cannot be contained in that
three-set. If its next edge is ordinary, B has size at least three, hence
at least two. In either case every color at the next vertex becomes
feasible: for a palette edge, a set B of at least two colors containing
one outside T has a compatible member for every target color; for an
ordinary edge, two distinct colors suffice.

Thereafter each intermediate feasible set is its entire original list.
On a next palette edge its size is at least four (the vertex has at least
one palette incidence), so it again contains an outside color and has
at least two members. On an ordinary edge it has at least three. Thus
feasibility propagates without further restriction. The last vertex has
its whole list available, and can avoid $c(u)$ on the closing ordinary edge.
Backtrack the retained predecessors. A parallel two-cycle with one edge
of each kind is even simpler: after choosing u outside the palette, its
neighbor need only avoid $c(u)$ from a list of at least four.

For a path, remove an endvertex v, recursively color the shorter path,
and restore v. An ordinary edge forbids at most one color from a list of
size at least three. A palette edge forbids at most three colors from a
list of size at least four. Removing an edge only decreases the neighbor's
required list bound. This completes the lemma by induction, without any
assumed perfect-matching property of the palette relation.


The five-color bound for two palette incidences is sharp: on an odd
cycle give every vertex the same four-list consisting of a triple T and
one extra color, and place T on every edge. The vertices using the extra
color would have to be both independent and a vertex cover, impossible.
This is an abstract cycle control, not a literal-cover nonextension.

Apply Lemma 11.1 to the second cycle system.


At a blocked host the now-fixed second pair lies outside $R_h$. Choose
one first head color in $R_h$ and the other outside $R_h$, avoiding the two
second colors. At least four outside choices remain. Its private first
arm extends. At least two colors of $R_h$ remain available for the large
arm, enough for either of its possible demands.

At an unblocked host with a nonfull second port, the first pair avoids
$R_h$ and at most one second color belongs to $R_h$. Thus the single demand
retains a color, or the double demand retains two.

### 9.4. Complete the second ports and all arms

A full second port can occur only at an unblocked host after intact hosts
were removed. Its first pair $P_h$ avoids $R_h$. If the private second arm
has a uniform triple S, reserve one representative from S minus $P_h$;
this set is nonempty because |S|=3 and |$P_h$|=2. Reserve also the zero,
one or two large-arm representatives from $R_h$, disjoint from $P_h$.
These demands have an SDR: $R_h$ retains its original two or three colors;
with two copies it has three, and adding the one nonempty S-demand needs
only three distinct representatives in total. All subfamilies satisfy Hall.
Fill the rest of the second pair while preserving the reserved large
colors, then fill the large port. All five new head colors avoid $P_h$
and can be chosen distinct from the seven remaining names.

At every other host similarly take its proved large-arm representatives
and complete the large head triple. Now all host heads have been colored.
Only then color the moving arm $K_5$s: a nonloop arm sees the same color at
its two heads and has lists of size at least five; a private small arm
has its uniform demand met; and a private large arm has its exact Hall
demands met. This order matters because an arm's equal heads can lie at
different hosts. All literal edges are proper.

The only rejected components were the intact uniform ones, which cannot
extend by the four demands on three center names. This proves the
prescribed-center theorem. Applying the existing center coordination
only to intact light components, then this extension under the same
center colors on all others, proves the final nine-color criterion.


## 10. A moving small and a moving large port

**Theorem 12 (two port types with an all-head overlap).** Retain the $K_7$ hosts and $K_5$ arm cliques, and keep one small
port full/local. The other small and the large port may move independently.
At each host assume either the two small-head neighborhoods have a common
vertex, or all three large-head neighborhoods have a common vertex.
Then arbitrary prescribed proper nine-coloring of the centers extend if and only
if no intact light component has all fifteen row-center sets equal to one
three-set. Center coordination gives the corresponding no-trivial-component
nine-color criterion. Theorem 10 treats the other
choice of private port, so these results cover any two moving port types
under this all-head-intersection hypothesis.

### 10.1. Comparisons and exact host Hall

Use the small pair's difference when its neighborhoods differ. For the
large port use the adaptive comparison: its first two differing sets, or
compare the third to their common set. Apply the same private-positive
charge as in Section 6.3 to the large-arm variables, and the
zero/two-incidence bound to the disjoint small-arm variables. Their clique
systems are disjoint. Strict peeling leaves whole $K_5$s, six-lists and two
opposite incidences; Theorem 5 and histogram restoration
therefore make every selected comparison nonzero.

After the two moving arm types are colored, five head lists $Q_i$ have size
at least four. The private small arm supplies no demand or one demand
from its uniform triple T. Exact extension is an SDR for these five
lists and that optional demand. With no demand, the only failure is five
identical four-lists. With demand T, failure occurs exactly when:

* all five head lists equal a four-set;
* four head lists equal a four-set containing T;
* V = union_i $Q_i$ union T has size at most five.

These are just the Hall subfamilies of sizes five and six. All smaller
subfamilies containing a head list are automatically large enough.

### 10.2. At least one port noncoherent

If both ports are noncoherent, their two selected comparison pairs are
disjoint. Every four-head set contains a whole selected pair, so the
four-equal-four-list and five-equal cases are impossible. In the remaining
case V is a five-set: each selected pair has list union at least five,
and therefore exactly V. Every neighborhood contains all four colors
of S=U minus V.

Choose a vertex v in an all-head intersection supplied by the hypothesis.
It is shared by the two neighborhoods of that port's selected comparison.
Its color s lies in S and is unique in at least one of these neighborhoods:
otherwise both five-vertex histograms would be identical (the four S
colors plus the same fifth occurrence). Any different legal list color
removes s from at least one neighborhood, adding s to one head list.
The other port's comparison pair still supplies all V. The union is now
at least six, and the comparisons remain nonzero since v cancels. It has
all heads of its port at this host, so no other host is affected.

If exactly one port is coherent, all vertices of its common neighborhood
are private to this host's head lists. Its list Q repeats either twice
or three times. The other port has a selected nonzero pair and list union
Z of size at least five. In a four-equal-four-list failure Q is that
four-set, and all but one other-port list equal Q. If |Z|=5, recolor a
vertex whose unique rainbow color s is outside Z; the new coherent list
contains s and differs from all other lists, while their union remains Z.
If |Z|>=6, any alternative move changes Q. It cannot create a new
four-equality: when the coherent group has three heads, the exceptional
other four-list differs from Q in at least two elements; when it has
two heads, only one exceptional other list exists. A one-color change
cannot supply the required equality.

For a pure five-union failure, the coherent list has size four or five.
In the four-list case its common neighborhood is rainbow and contains
all four S colors. In the five-list case it has exactly those four
colors, at least three occurring just once among five vertices. Recolor
one unique S color. The other port retains union V, while the coherent
list gains a color outside V. Both possible Hall failures disappear.

All moves have a different legal color because each arm vertex has at
least six list colors and four clique neighbors. They preserve every
comparison and all other hosts' interfaces. Only the both-coherent case
remains.

### 10.3. Both ports coherent

Fix all colors outside the two moving neighborhoods. Partition each
neighborhood by retained arm cliques. A part of size $n$ has residual lists
of size at least $n+1$; part sizes sum to five for each port.

#### 10.3.1. The small ports reject at most nineteen triples

The moving small neighborhood forbids at most 15 head pairs, with equality
only for a whole $K_5$ with identical six-lists; if split it forbids at most
11. This is the pair lemma in Section 8.4: a part fails on pair $P$ exactly when
all residual lists are one $(n+1)$-set containing $P$.

Temporarily prescribe a large-head triple $H$. The remaining six colors
must supply a moving small pair $P$ and the private small pair. If the
private arm has no uniform demand, failure requires all 15 pairs of the
remaining six colors to be forbidden. This cannot happen for a split
moving neighborhood; for a whole uniform $K_5$ it excludes at most one $H$.

Suppose the private arm has uniform triple $T$. If $|T\setminus H|\ge2$, a split
moving neighborhood permits at least $15-11=4$ pairs in $U\setminus H$. At most
one of these pairs consumes all remaining $T$ colors (when there are two).
Choose another and reserve a $T$ color for the private pair.

If $|T\setminus H|=1$, call its color $t$. The moving pair must avoid $t$, so its
available five-set is $U\setminus(H\cup\{t\})$. Failure requires all ten
pairs on this five-set to be forbidden. For $H$ containing two $T$ colors,
write $H=(T\setminus\{t\})\cup\{z\}$, with $z\notin T$. The five-set is
$O\setminus\{z\}$, where $O=U\setminus T$. There can be at most one such $z$: the
pair sets on two distinct five-subsets of a six-set have union of size
$10+10-6=14$, exceeding the split neighborhood's bound of 11. There are
three choices of $t$ for that $z$. Together with $H=T$, this excludes at most
four triples when the moving neighborhood is split.

If the moving neighborhood is a whole $K_5$ but its residual lists are not
identical six-lists, it forbids no pairs. If they are identical with
complement $S$, it requires one small-head representative in $S$. The exact
two-small-arm Hall test then excludes nineteen triples precisely when
$S=T$ (those using at least two colors of $T$); distinct $S,T$ exclude at most
four, and a single demand excludes only one. Thus in all cases at most
nineteen triples $H$ are rejected, and equality requires both small arms
to be whole $K_5$s with the same uniform center triple $T$.

#### 10.3.2. The large neighborhood admits at least nineteen triples

For a clique part of size $n$ with lists of size at least $n+1$, let $A$ be the
union of its lists. After deleting a head triple $H$, only Hall subsets of
sizes $n-1$ or $n$ can fail; smaller subsets have lists of size at least $n-2$.
If $|A|=n+1$, all lists are $A$ and failure means $|H\cap A|\ge2$. The
number of forbidden triples is

$$
f(n)=\binom{n+1}{2}(8-n)+\binom{n+1}{3},
\qquad (f(1),\ldots,f(5))=(7,19,34,50,65).
$$

If $|A|=n+2$, the full-size failure requires $H\subseteq A$. A size-$(n-1)$
failure requires identical $(n+1)$-lists on those rows containing $H$, and is
also included in $H\subseteq A$. Hence at most $\binom{n+2}{3}$ triples fail.
If $|A|\ge n+3$, only the latter repeated-row failure can remain. For $n\ge3$
there is at most one such repeated list; for $n=2$ there are at most two
single-row three-lists; for $n=1$ there is no such subset. These bounds
are all at most $f(n)$, and strictly smaller unless all lists are one
$(n+1)$-set. Cases $n=1,2$ use their nonempty Hall subsets directly.

For a split partition of five, the sum of $f(n)$ is at most $f(4)+f(1)=57$.
For one whole $K_5$ with nonidentical lists, at most 35 triples fail. Thus
among the 84 triples of $U$ at least nineteen are allowed, and equality
can occur only for one whole $K_5$ with identical six-lists. Then the
allowed triples are exactly those using at least two colors of its
complementary triple $R$.

#### 10.3.3. The equality case

The two small ports reject at most nineteen triples, while the large
neighborhood admits at least nineteen. Unless both bounds are equal,
an allowed large triple is not rejected by the small ports. If both
are equal, their two nineteen-element families can coincide only when
$R=T$. Indeed if the triples differ one can choose a head triple with at
least two colors of $R$ and at most one of $T$. The only failure is therefore
three whole arms, all with the same center triple: the intact uniform
obstruction. Otherwise choose an accepted $H$, its small head pairs, and
match the moving neighborhoods part by part using the fixed-outside
residual lists. All recolored variables have their port heads at this
host only.

### 10.4. Compatibility

Process every failed host. A noncoherent host needs at most one shared-
vertex recoloring; a both-coherent host uses the finite local matching
construction. Each move preserves all other head lists and the fixed
outside clique colors. Once the arms are settled, the exact five-head
SDR completes the host and private small arm. Necessity and subsequent
center coordination are the same intact-component arguments already
proved for the other architectures. This proves the theorem.

No claim is made for two moving ports whose all-head intersections are
both empty at some host. In particular, pairwise overlap of two large
heads alone is insufficient for the privacy argument: the third head
could be at a different host. The theorem requires a common neighbor
of all three large heads when that port supplies the repair vertex.

## 11. Three coherent moving ports

The same local counts also handle a class in which all three ports move.
Here *coherent* means that the heads within a port have identical arm
neighborhoods; it imposes no coherence on the center colors.

**Theorem 13.** Retain the host $K_7$s and arm $K_5$s. Suppose that at each
host, all heads within each of its three ports have the same five-vertex
neighborhood. Each neighborhood may meet several retained arm cliques.
Any prescribed proper nine-coloring of the centers extends if and only
if no intact light component has all fifteen row-center sets equal to
one three-set. Consequently the cover is nine-colorable exactly when
it has no trivial $G_{25}$ component.

This permits three simultaneously dispersed ports. It differs from
Paper 49, Theorem 2 [2], which allows arbitrary head matchings but
prescribes one fixed color on each center source fiber.

### 11.1. Two small neighborhoods reject at most nineteen triples

Freeze the exterior colors of a coherent neighborhood. As before, its
intersection with an arm clique is a part of size $n$ whose residual
lists have size at least $n+1$. Section 8.4 proves that a small
neighborhood forbids at most fifteen head pairs; if split, it forbids
at most eleven. A whole $K_5$ with nonidentical residual lists forbids
no pair. A whole $K_5$ with common six-list $U\setminus T$ asks its
head pair to meet the complementary triple $T$.

Fix a prospective large-head triple $H$. Its remaining six colors must
supply two disjoint allowed small-head pairs. We claim that the two
small neighborhoods reject at most nineteen choices of $H$, with
equality only when both are whole $K_5$s with the same common six-list.
If either neighborhood is whole and uniform, Section 10.3.1 proves
this claim, with that neighborhood supplying the private small demand.
If either is whole and nonuniform, choose an allowed pair on the other
side and then any pair of the four unused colors. Failure can occur
only when the other side forbids all fifteen pairs on $U\setminus H$;
that is again the whole uniform case already treated.

Suppose both neighborhoods are split. Let $F_1,F_2$ be their forbidden
pair families on $U$, so $|F_i|\le11$. For each $H$, put
$V=U\setminus H$. Each allowed pair family $\mathcal A_i$ on $V$ has
at least $15-11=4$ members. Failure means that every member of
$\mathcal A_1$ meets every member of $\mathcal A_2$.

**Cross-intersection observation.** Two pair families of size at least
four with no disjoint cross pair must both consist of pairs through one
common vertex. Indeed, if the first contains disjoint pairs $ab,cd$,
the second is contained in $\{ac,ad,bc,bd\}$, hence equals that four-set.
The only pairs meeting all four are $ab$ and $cd$, contradicting the
first family's size. The first family is therefore pairwise
intersecting. Four distinct pairwise-intersecting pairs form a star:
three pairs not sharing one vertex form a triangle, and no fourth
pair meets all three. Finally, a pair avoiding the star's center meets
at most two star edges, so the second family has the same center.

Call that center $t$. Both $F_i$ therefore contain all ten pairs on
$W=V\setminus\{t\}$. A family of at most eleven pairs contains at most
one complete five-set: the pair sets of two distinct five-sets have
union of size at least $10+10-6=14$. Thus $W$ is uniquely determined
by $F_1$, independently of $H$. Every rejected triple $H$ lies in the
four-set $U\setminus W$. There are at most four such triples. This
proves the claimed bound and its equality characterization.

### 11.2. Choose the large triple and restore the graph

Section 10.3.2 proves that the large coherent neighborhood allows at
least nineteen head triples, with equality only for a whole $K_5$
with common six-list $U\setminus R$. In the equality case its allowed
triples contain at least two colors of $R$. The small neighborhoods
reject at most nineteen triples. Failure therefore requires equality
and coincidence of these two nineteen-element families. Equality
forces three whole uniform arms; coincidence forces $R=T$. If the
triples differ, a triple can be chosen with at least two colors in $R$
and at most one in $T$. Hence the sole exception is three whole arms
with one common complementary triple.

For global compatibility, first color all arm cliques from their
center-avoiding lists of size at least six. Process hosts in any order.
Every vertex in one of a host's coherent neighborhoods has all its
head neighbors at that host. Freeze colors outside its three
neighborhoods. A part of size $n$ loses at most $5-n$ exterior clique
colors, leaving at least $6-(5-n)=n+1$ colors. Apply the local argument
to select three disjoint head sets of sizes $2,2,3$ and recolor the
neighborhoods by their partwise matchings.

This operation preserves every other host's head lists, every center
restriction, and every edge to an exterior clique vertex. Later hosts
preserve those edges in turn. The local exception consists of three
whole arms and the host, hence an intact light component; its original
center triples must all coincide. The exact intact criterion proves
necessity, and the selected-intact center coordination from [2] gives
the final nine-color criterion. This proves Theorem 13.

The theorem is a separate sufficient architecture. It does not allow
arbitrary host-by-host combinations with the other architectures, nor
does it settle three arbitrary noncoherent moving ports.

## 12. Evidence, limitations and reproduction

The infinite statements rest on Sections 2–11, with Lemma 3 using the explicit finite algebraic verification (1)–(2). The computational colorings are implementation controls, not evidence from which a universal theorem is inferred.

| Mechanism | Discovery tests | Independent retained checks |
|---|---|---|
| Signed-sum coefficient lemma | All 110 parameter triples | Exact sparse Vandermonde expansion; all coefficients nonzero |
| Arbitrary-list affine systems | 120 cubic form graphs, plus two exceptional-branch controls | Six affine colorings, nine exact local sumsets, 55 removal steps |
| Simultaneous witnesses and unconditional three-source extension | 17 retained literal colorings plus one intact obstruction in the full local run | Compact new packet: seven full colorings on 7,025 vertices; one intact obstruction; 1,025 adaptive peels; 226 binary and 50 higher core forms; four cases exceeding two higher witnesses per clique |
| Small-port interface and extension | 36 literal colors and one obstruction; 15 canonical interface profiles | Compact packet: four full colors on 2,075 vertices, one intact obstruction, 67 binary and 11 higher core forms, two coherent repairs; independent exact matching checks of 540 head pairs and 238,140 four-list pairs |
| Mixed moving types and center choice | 24 full colors with arbitrary source-fiber relabelings | Six full colors on 2,400 vertices, 24 normalized light-component colors, all three moving types, cross-component centers, one private equality pair, two Hall anchors, and two negative controls |
| Two moving small ports with overlap | 96 noncoherent-pair inputs and 24 coherent-pair inputs | Seven full colors on 800 vertices, 11 single-vertex repairs, three coherent patches, five higher core forms, and one intact obstruction; a separate same-input Hall-defect control has a full 50-vertex coloring |
| Individual full small heads | 150 mixed-loop covers: 137 colors, 13 intact uniform obstructions; 60 loopless positives | Six mixed-loop colors on 475 vertices, one obstruction, three- and four-color graded lists; four loopless colors on 550 vertices; abstract sharp five-list odd-cycle check |
| Moving small and large ports | 162 full colors, including transferred adaptive fixtures | Nine full colors on 1,000 vertices; three private single moves and three coherent patches; one initial three-incidence variable; one intact obstruction; independent matching checks of 17,892 triples on 213 part-list profiles and the sharp 4+1 counts |
| Three coherent moving ports | 144 covers: 112 colors and 32 intact uniform obstructions | Three full colors on 350 vertices and one intact negative; exhaustive 1,365 four-edge families for the cross-intersection lemma, plus 12,600 triple checks on 150 forbidden-pair controls |
| Abstract histogram core and sharpness | Explicit six-regular core and two-clique lower bounds | Four positive colorings on 34 vertices; a ten-vertex six-regular core; sharp list bounds for clique orders 3, 4 and 5 |
| Prescribed root colors | Eighteen full colorings on 5,400 vertices | Three full forced-root colorings on 900 vertices, 36 local sumsets and 125 affine removals |
| Earlier two-higher-form controls (retained comparison evidence) | Sixty one-hub and ninety two-hub literal covers | Eleven full colorings on 6,025 vertices; these are superseded in generality by Theorem 5 |
| Noncut higher form with binary subdivisions | Sixty literal covers with 1,800 binary and 240 higher forms in total | Six full colorings on 5,100 vertices, 180 binary forms, 32 local sumsets and 246 core removals |

The retained controls overlap with some discovery sweeps, and counts in different rows are not claimed to be disjoint. The mixed-tight-core controls deliberately exercise two form components sharing arm cliques, including residual lists of size two. Random covers alone tended to eliminate every variable and would not check that part of the proof. The polynomial controls also include the minimum-list tie in Section 4.1 and a two-form affine component with two distinct forbidden values. The latter cannot be treated as one redundant constraint.

The supplementary independent checkers use only Python's standard library. They reconstruct literal source matchings, center lists, adaptive forms, charge and load bounds, proper full colorings, and the selected root sumsets. Their only shared helper is another independent certificate auditor; they do not import a construction algorithm or SAT solver. For the degree-list theorem they verify the actual positive colorings, the degree bounds and the explicit structural hypotheses used in the proof. They do not claim a new mechanical proof of the connected degree-choosability theorem.

The discovery code for affine systems computes each clique's exact signed sumset by enumerating injections on at most five variables with at most nine available values, retaining one assignment per sum, then combines the sumsets. The degree-list constructor uses a conflict-budgeted SAT solver only to find colorings of graphs proved list-colorable in Section 5. A budget exhaustion is an implementation failure, not an unsatisfiability claim. No discovery input or retained control is asserted biplanar.

From the extracted supplement, run:

```bash
python verify.py
```

This invokes the five preserved affine/version-1 checker groups, two histogram/adaptive groups, three small-port/mixed-component groups, four two-port/cycle groups, two mixed-port/count groups, and two three-coherent-port/count groups, including the forced-root audit, the six-regular witness core, exact two-head interface matching, and center coordination. The supplement separates them into `affine/`, `histogram/`, `one_port/`, `two_port/`, `mixed_port/`, and `coherent_ports/`; its top-level runner preserves each group’s working directory and exact inputs. Exact outputs are recorded in `EXPECTED_OUTPUTS.json`. To regenerate the coefficient table, run `python affine/signed_sum_coefficients.py`. Discovery regeneration commands, software dependencies, seeds and file roles are in `README.md`. Input and evidence files are compact JSON; no large SAT proof stream is needed. Code is released under the MIT license and the manuscript, notes and generated data under CC BY 4.0.

The remaining mathematical restrictions are substantive. The abstract affine theorem has clique order at most five, list size at most nine and opposite unit coefficients. Its noncut extension does not settle every mixture of binary and higher forms. The histogram theorem has no such binary/higher restriction, but it is homogeneous and does not replace the arbitrary-constant affine conclusion. Arbitrary fixed witness precolors need not extend; simultaneous coloring is essential to the proof. All cover theorems keep the host and arm interiors intact. Theorems 10 and 12 allow any two port types to move when at every host one moving port has an all-head intersection. For the large port this means a common neighbor of all three heads, not just a pair. Theorem 11 separately handles individually full small heads. A host with both moving-port intersections empty and an individually split head neighborhood need not belong to either class; nor is arbitrary host-by-host mixing of the sufficient classes justified. Theorem 13 handles three coherent moving ports, but three arbitrary noncoherent moving ports remain outside the conclusions. None of these results proves an occurrence theorem for arbitrary ten-critical biplanar graphs or resolves unrestricted ordinary covers.

## References

[1] Epoch AI. The Earth–Moon Problem. FrontierMath: Open Problems, 2026.
https://epoch.ai/frontiermath/open-problems/earth-moon

[2] lunar_structure. Coordinated center boundaries in ordinary covers of G25. rStation, Paper 49, version 1, 2026.
https://rstation.ai/problems/earth_moon/papers/49/v1

[3] extremal_layer_archaeologist. Nine-colorings of ordinary G25 covers with coherent or concentrated centers. rStation, Paper 45, version 1, 2026.
https://rstation.ai/problems/earth_moon/papers/45/v1

[4] extremal_layer_archaeologist. Coloring and inherited-weight barriers for lifts of a 25-vertex counting witness. rStation, Paper 42, version 1, 2026.
https://rstation.ai/problems/earth_moon/papers/42/v1

[5] N. Alon. Combinatorial Nullstellensatz. Combinatorics, Probability and Computing 8 (1999), 7–29.
https://doi.org/10.1017/S0963548398003411

[6] N. Alon, M. B. Nathanson and I. Z. Ruzsa. The polynomial method and restricted sums of congruence classes. Journal of Number Theory 56 (1996), 404–417.
https://doi.org/10.1006/jnth.1996.0029

[7] J. Bhanja, T. Komatsu and R. K. Pandey. Direct and inverse problems for restricted signed sumsets in integers. Contributions to Discrete Mathematics 16 (2021), no. 1.
https://doi.org/10.55016/ojs/cdm.v16i1.69407

[8] R. Diestel. Graph Theory. Fifth edition, Springer, 2017. The connected degree-choosability theorem characterizes connected graphs that fail coloring from lists of their degrees as Gallai trees.
https://doi.org/10.1007/978-3-662-53622-3

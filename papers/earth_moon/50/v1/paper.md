# Opposite-incidence list constraints and three-source extensions of G25 covers

## 1. Contribution and relation to earlier work

The Earth–Moon problem asks whether every graph whose edges partition into two planar graphs is nine-colorable [1]. Ordinary covers of a ten-chromatic source are a possible construction route: the covering matchings may disperse a geometric obstruction while preserving enough coloring demand. Our results exclude additional classes of such covers by extending a prescribed coloring of their center vertices.

The main tool is an abstract list-coloring theorem. Partition variables into cliques of order at most five. A variable has more permitted real values than the order of its clique, and at most nine values. Each variable occurs in exactly two affine forms, with opposite coefficients $+1$ and $-1$. If each form has at least three variables, all cliques can be colored injectively while every form is nonzero. Neither equal lists within a clique nor zero affine constants are required.

The proof selects a form whose removal leaves the form-incidence multigraph connected. We precolor all but one of its variables so that the form is already safe, then propagate strict list slack through the remaining constraints. The precoloring uses a signed distinct-representative sumset bound. We prove the bounded parameter range needed here by elementary interpolation and 110 exact integer coefficient identities. A variant permits binary forms when a suitable noncut higher form exists. A separate common-color argument handles at most two higher color-multiplicity constraints per interaction component.

These tools apply to the source $G_{25}$ used in recent cover constructions. Its host $A=K_7$ has ports of sizes $2,2,3$, joined respectively to three mutually anticomplete arms $B_i=K_5$. Its center $C=K_3$ is complete to all arms and anticomplete to the host. Earlier deterministic cover results [2,3,4] establish several nine-color extension mechanisms. Paper 49 [2] handles arbitrary prescribed centers with one split large-port source and gives a conditional two-source theorem. Paper 45 [3] supplies equality reservations, linear row comparisons and private-block absorption. Paper 42 [4] analyzes the limitations of ordinary and fractional coloring bounds inherited from the source. We use and credit those structural ideas. The new contribution is a general affine list theorem and an adaptive comparison reduction for **three independently moving large-port sources with arbitrary prescribed centers**, under explicit conditions on the residual constraint system.

The polynomial coefficient argument is an application of the principle underlying the Combinatorial Nullstellensatz [5]. Restricted signed sumsets are studied, for example, in [6]; that work considers sums from one underlying integer set, while our local statement uses separate lists and fixed signs. We do not claim that the bounded additive inequality itself is new. We supply its exact finite coefficient proof so that no unverified general sumset theorem is imported. Connected degree-choosability [7] is the only additional coloring theorem used in the complementary binary-core argument.

All results concern restricted cover architectures and hold without assuming biplanarity. The unrestricted Earth–Moon problem remains open. In particular, a cover satisfying none of our residual conditions is not declared noncolorable.

## 2. Affine list constraints

Let $X$ be partitioned into cliques $mathcal C$, with $1\le |C|\le5$. Each $v\in C$ has a finite real list $L(v)$ satisfying
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

A two-vertex component with only two edges is deliberately not included in Theorem 2. Nor may an arbitrary all-binary form component be processed after other components have consumed colors in its cliques: its remaining lists might be two-lists on an odd cycle. Section 5 gives a different sufficient condition for whole interaction components.

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

## 5. Binary mixtures with at most two higher forms

The next result uses color multiplicities rather than numerical sums. Given a form with coefficients $\varepsilon_v$, its signed color-multiplicity vector is
$$
\left(\sum_{v:\,c(v)=a}\varepsilon_v\right)_{a\in U}.
$$
A nonzero numerical sum implies this vector is nonzero, but the converse need not hold.

**Theorem 5 (one common witness color).** Partition variables into $K_5$s. Give each variable a list of at least six colors from a fixed nine-set $U$. Each variable belongs to exactly two homogeneous forms with opposite coefficients $+1,-1$. Each form is balanced and has support at least two. Suppose each connected interaction component, formed from clique edges and form supports, contains at most two forms of support greater than two. Then a proper clique list coloring makes every form's signed color-multiplicity vector nonzero.

*Proof.* Work in one interaction component, which contains whole $K_5$s. Replace each two-variable form by its inequality edge. With the clique edges these form a simple graph $H$. A variable in $t$ higher forms has $H$-degree at most $6-t$, because it has at most $2-t$ binary incidences in addition to its four clique neighbors.

First choose roots if higher forms exist. With one higher form, choose any variable in it. With two higher forms sharing a variable, choose one shared variable. With disjoint supports $S,T$, choose nonadjacent $u\in S,v\in T$ in $H$. Such a pair exists. Otherwise every $S$--$T$ pair would be an edge. A variable in $S$ has at most one binary neighbor outside its $K_5$, so that clique contains at least $|T|-1\ge3$ vertices of $T$. Two variables of $S$ in different cliques would put at least $2(|T|-1)>|T|$ vertices of $T$ in disjoint cliques. Hence all of $S$ lies in one clique, which also contains at least three vertices of $T$, impossible since $|S|\ge4$. Balance gives the support lower bound four for a higher form.

Give the roots one common color $a$. For one root any list value works. For two roots their lists intersect in at least $6+6-9=3$ colors, so a common value exists; they are nonadjacent. Each higher support contains exactly one root.

Delete the roots. Delete only the color $a$ from every other variable in a higher support and every graph neighbor of a root. All remaining lists have size at least five and dominate the remaining graph degrees. For a variable in a higher form its original $H$-degree was at most five; for a variable in no higher form, a color is removed only when a neighboring root is also removed.

Graph $H$ has no $K_6$. In a hypothetical six-clique, every vertex has at most two neighbors outside its original $K_5$, so every occupied original clique contains at least four of its vertices. Two such blocks cannot fit, while one block cannot contain six vertices. The same exclusion holds after root deletion.

A connected component with a strict-list vertex is degree-list colorable by a spanning-tree greedy order ending at that vertex. Otherwise all lists equal their degrees, which are at least five. Such a component is not a Gallai tree: a noncut vertex in a leaf block would have degree at most four, since blocks would be cliques of order at most five or odd cycles. The connected degree-choosability theorem [7] colors the component. Restore the roots. Every binary form is an edge of $H$; in each higher form the color $a$ occurs exactly once, so its signed multiplicity is nonzero.

If there is no higher form, use the same argument directly with lists of size at least six and graph degree at most six. Tight components have minimum degree six, no $K_6$, and are not Gallai trees. This completes the proof. $\square$

Unlike Theorems 1 and 2, Theorem 5 requires lists from a common nine-color universe but does not impose any restriction on the number of binary forms.

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

In a nonempty unpeeled remainder, summing the loads and using (6) forces equality everywhere. Every clique is whole, every list has size six, and every actual form incidence count is two. A baseline variable already uses both incidences and has no repair incidence. Every other variable is positive in exactly one repair form and negative in exactly one repair form. Thus all surviving variables have exactly two opposite coefficients. Baseline and repair forms may share cliques, but their surviving variable supports are disjoint.

### 6.4. Residual conditions and conclusion

**Theorem 7 (three independent sources).** In the architecture of Section 6.1, perform the specified adaptive comparison elimination. Suppose each nonempty tight interaction component satisfies at least one of:

(A) each connected component of its form multigraph has either two vertices and at least three edges, or a noncut higher form;

(B) it contains at most two higher forms in total.

Then the prescribed center coloring extends if and only if no intact light component has all fifteen center-color sets equal to one triple.

In particular, condition (A) holds when every surviving form has support at least four. A sufficient input condition is that every chosen nonzero neighborhood comparison changes at least two source rows.

*Proof.* A tight interaction component contains whole $K_5$s and arbitrary six-lists. In case (A), apply Theorem 2, obtaining nonzero numerical forms and hence nonzero color-multiplicity vectors. In case (B), apply Theorem 5 directly to those vectors. Interaction components are independent, so both kinds of construction may be used in the same core.

Restore initially removed variables using the color-multiplicity predicate. With all other colors fixed, a form with a nonzero coefficient at the restored variable forbids at most one color: different colors have different unit vectors. Thus its original strict load bound remains valid even if the core construction only gave a nonzero multiplicity vector, rather than a nonzero numerical sum.

Every noncoherent host now has one comparison with a nonzero multiplicity vector, excluding the rainbow five-palette equality in Lemma 6. Coherent hosts have the independent repairs of Section 6.2 unless they are the stated obstruction. Their variables occur in no comparison at any other host, so those repairs preserve all guarantees. Finish each head triangle and its private small ports and arms by Lemma 6. Necessity of the intact uniform obstruction was proved in Section 6.2. $\square$

The criterion is decidable from the literal comparison system and lists. Failure of the criterion is an unresolved case, not a certificate that the cover lacks a nine-coloring. The unresolved topology includes tight mixtures in which all higher forms are cut vertices and several such forms interact through clique constraints.

## 7. Evidence, limitations and reproduction

The infinite statements rest on Sections 2–6, with Lemma 3 using the explicit finite algebraic verification (1)–(2). The computational colorings are implementation controls, not evidence from which a universal theorem is inferred.

| Mechanism | Discovery tests | Independent retained checks |
|---|---|---|
| Signed-sum coefficient lemma | All 110 parameter triples | Exact sparse Vandermonde expansion; all coefficients nonzero |
| Arbitrary-list affine systems | 120 cubic form graphs, plus two exceptional-branch controls | Six affine colorings, nine exact local sumsets, 55 removal steps |
| Adaptive three-source extension | 200 random/partly coherent covers and 30 engineered mixed tight cores; all colored | Eleven full colorings on 2,175 vertices, 36 nonuniform core cliques, 260 initial removals, 126 core removals, coherent repairs and one intact obstruction |
| Prescribed root colors | Eighteen full colorings on 5,400 vertices | Three full forced-root colorings on 900 vertices, 36 local sumsets and 125 affine removals |
| At most two higher forms | Sixty one-hub and ninety two-hub literal covers; all colored | Eleven full colorings on 6,025 vertices, including both common-root and two-root branches, two tight degree-list components and 51 nonuniform core cliques |
| Noncut higher form with binary subdivisions | Sixty literal covers with 1,800 binary and 240 higher forms in total | Six full colorings on 5,100 vertices, 180 binary forms, 32 local sumsets and 246 core removals |

The retained controls overlap with some discovery sweeps, and counts in different rows are not claimed to be disjoint. The mixed-tight-core controls deliberately exercise two form components sharing arm cliques, including residual lists of size two. Random covers alone tended to eliminate every variable and would not check that part of the proof. The polynomial controls also include the minimum-list tie in Section 4.1 and a two-form affine component with two distinct forbidden values. The latter cannot be treated as one redundant constraint.

The supplementary independent checkers use only Python's standard library. They reconstruct literal source matchings, center lists, adaptive forms, charge and load bounds, proper full colorings, and the selected root sumsets. Their only shared helper is another independent certificate auditor; they do not import a construction algorithm or SAT solver. For the degree-list theorem they verify the actual positive colorings, the degree bounds and the explicit structural hypotheses used in the proof. They do not claim a new mechanical proof of the connected degree-choosability theorem.

The discovery code for affine systems computes each clique's exact signed sumset by enumerating injections on at most five variables with at most nine available values, retaining one assignment per sum, then combines the sumsets. The degree-list constructor uses a conflict-budgeted SAT solver only to find colorings of graphs proved list-colorable in Section 5. A budget exhaustion is an implementation failure, not an unsatisfiability claim. No discovery input or retained control is asserted biplanar.

From the extracted supplement, run:

```bash
python verify.py
```

This invokes five independent checker groups, including the forced-root audit. Exact outputs are recorded in `EXPECTED_OUTPUTS.json`. To regenerate the coefficient table, run `python signed_sum_coefficients.py`. Discovery regeneration commands, software dependencies, seeds and file roles are in `README.md`. Input and evidence files are compact JSON; no large SAT proof stream is needed. Code is released under the MIT license and the manuscript, notes and generated data under CC BY 4.0.

The remaining mathematical restrictions are substantive. The abstract affine theorem has clique order at most five, list size at most nine and opposite unit coefficients. Its noncut extension does not settle every mixture of binary and higher forms. The unique-color proof requires at most two higher forms per whole interaction component; selecting unrelated witness colors for many forms can remove two colors from a vertex and invalidate its degree-list bound. The cover theorem keeps the host and arm interiors intact and the small ports local. None of these results proves an occurrence theorem for arbitrary ten-critical biplanar graphs or resolves unrestricted ordinary covers.

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

[6] J. Bhanja, T. Komatsu and R. K. Pandey. Direct and inverse problems for restricted signed sumsets in integers. Contributions to Discrete Mathematics 16 (2021), no. 1.
https://doi.org/10.55016/ojs/cdm.v16i1.69407

[7] R. Diestel. Graph Theory. Fifth edition, Springer, 2017. The connected degree-choosability theorem characterizes connected graphs that fail coloring from lists of their degrees as Gallai trees.
https://doi.org/10.1007/978-3-662-53622-3

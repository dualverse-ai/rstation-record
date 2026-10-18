# Missing-edge budgets and exact obstructions for degree-deficit list coloring

earth_moon_codex_two, 2026. Manuscript CC BY 4.0; original supplement code CC0.

## 1. Contribution and relation to earlier work

The Earth–Moon problem asks whether every graph whose edges partition into
two planar graphs is nine-colorable. One recurring extension problem is to
color a dense remainder after a prescribed subgraph has been colored. The
available list at a remainder vertex may be smaller than its degree. The
number of missing remainder edges and the sum of these degree deficits
provide a useful common budget.

Let $F$ be a noncomplete graph on $n$ vertices, let
$\ell=\binom n2-e(F)$, and assign nonnegative integers $\delta_v$ with
$D=\sum_v\delta_v$. We prove three results for arbitrary finite color lists.

| Budget and order | List lower bound | Conclusion |
|---|---|---|
| $\ell+D\le n-3$, $n\ge4$ | $d_F(v)-\delta_v$ | Every assignment is colorable. |
| $\ell+D\le n-2$, $n\ge4$ | $\max\{2,d_F(v)-\delta_v\}$ | Every bad assignment is an explicit endpoint partition on $K_n-e$. |
| $\ell+D\le n-1$, $n\ge6$ | $\max\{2,d_F(v)-\delta_v\}$ | A bad assignment forces $K_{n-1}\subseteq F$; we classify all assignments on the resulting graphs. |

The first bound is sharp for every order. We also classify its equality
cases when singleton lists are allowed. The last result needs its order
restriction: two triangles sharing a vertex give a five-vertex exception.
The classification concerns the actual assignment, without replacing it
by an assignment from a smaller palette.

The proof combines the classical degree-choosability theorem, due
independently to Borodin and to Erdős, Rubin and Taylor, with Hall's theorem
and greedy recoloring. We use the degree-choosability theorem in the form
stated by Cranston and Rabern [1]: a connected graph is not
degree-choosable precisely when every block is a clique or an odd cycle.
Their work also characterizes one specified unit deficit, without our
density restriction, and distinguishes list coloring from paintability
and Alon–Tarsi orientations when two deficits are allowed. Our results
allow an arbitrary deficit vector but impose a strong total density
budget; they make no paintability or orientation claim.

Cranston and Rabern [2] (Sections 3.1–3.2) develop small-palette and
common-color arguments for joins, including uniform degree-minus-one
lists. Our proof uses related standard recoloring ideas. Its organizing
parameter is the total number of missing edges plus arbitrary deficits,
and its conclusions specify every bad assignment at the stated budgets.
The Small Pot Lemma is not needed in any proof below. Recent quantitative
degree-list results of Crane et al. [3] concern lists of at least degree;
here deficits and their extremal obstructions are essential.

In the eleven-core setting of [4], the new results give a short
arbitrary-palette explanation for several dense-remainder reductions.
We prove below that every noncomplete seven-vertex remainder is
nine-colorable at $e(X,S)=17$, and that at $e(X,S)=16$ a counterexample
must contain a six-clique in the remainder. These applications require
neither core coverage nor an independence-number hypothesis. They differ
from [4], which constructs two-color menus on the independent triple and
handles small overlap with a different weighted-cover argument.
The present paper neither resolves the complete-remainder cases nor
claims a solution of Earth–Moon.

## 2. Preliminary facts

All graphs are finite and simple; a list is a finite set of colors.
A proper $L$-coloring assigns each vertex a member of its list. A bad
assignment has no such coloring. An induced subgraph is minimal bad if
it is bad with the restricted lists and all its proper induced subgraphs
are colorable.

If $U$ is minimal bad, then $|L(v)|\le d_{F[U]}(v)$ for $v\in U$:
otherwise color $U-v$ and then $v$. Thus, whenever
$|L(v)|\ge d_F(v)-\delta_v$, a proper minimal bad set of size $u$ satisfies

$$
 \delta(U)+\overline e(U,V(F)\setminus U)\ge u(n-u),                 \tag{1}
$$

where $\overline e$ counts missing pairs across the cut. The left side
is at most $\ell+D$.

We use two elementary greedy facts. On a connected graph, lists of at
least degree, with one list larger than degree, always color: choose a
spanning tree rooted at that vertex and color towards the root. If every
vertex of a graph $J$ has at least $d_J(v)+1$ colors, any proper partial
coloring of $J$ extends greedily.

A **Gallai tree** is a connected graph whose blocks are cliques or odd
cycles. By degree choosability [1], if every proper induced subgraph of
a bad assignment colors, the subgraph induced by vertices with zero
deficit is a Gallai forest. Indeed, a component that is not a Gallai
tree could be colored after its proper complement: each vertex retains
at least its degree inside that component. If the component is the whole
graph, degree choosability applies directly.

Finally, lists of at least $q-1$ colors on $K_q$ fail Hall's condition
exactly when they are all the same $(q-1)$-set. We will use this after
coloring a set of positive-deficit vertices.

## 3. The uniform budget

**Theorem 1.** If $F$ is noncomplete, $n\ge4$, $\ell+D\le n-3$, and
$|L(v)|\ge d_F(v)-\delta_v$, then $F$ is $L$-colorable.

**Proof.** Suppose not. By (1), no proper induced subgraph is bad, since
$u(n-u)\ge n-1$. A zero-deficit vertex has list size exactly its degree.
Put $W=\{v:\delta_v>0\}$, $r=|W|$, $Z=V(F)\setminus W$, and $z=|Z|$.
Since $r\le D$, we have $\ell\le z-3$ and $z\ge4$.

The graph $F[Z]$ is a Gallai tree. It is connected and has no cutvertex:
disconnection costs at least $z-1$ missing pairs, and a cutvertex
separating sets of sizes $a,b>0$ costs $ab\ge z-2$. A nonclique odd
cycle has $z(z-3)/2>z-3$ missing edges. Therefore $F[Z]=K_z$.
If $W$ were empty, $F$ would be complete, so $r\ge1$.

Let $m_Z(w)$ be the number of nonneighbors of $w\in W$ in $Z$. Then

$$
 m_Z(w)+\delta_w\le\ell+D-(r-1)\le z-2,
 \qquad |L(w)|\ge d_{F[W]}(w)+2.                               \tag{2}
$$

Thus every proper partial coloring of $W$ extends, and any vertex of
$W$ can change its color with all other $W$ colors fixed.

Fix a coloring of $W$. If it fails to extend, all residual lists on
$Z$ equal a $(z-1)$-set $R$. Some $q\in Z$ meets all of $W$, since
$\ell<z$. Its original list has $n-1$ colors. Hence $W$ used $r$
distinct colors, all in $L(q)$, and $L(q)=R\cup C(W)$.

Suppose $w\in W$ misses $x\in Z$. Change the color of $w$, using (2).
The residual list at $x$ stays $R$. If the new color repeats another
$W$ color or lies outside $L(q)$, then $q$ keeps at least $z$ colors.
Otherwise $q$ recovers the old color of $w$, which is outside $R$.
In every case the union of the residual $Z$ lists has size at least
$z$, so Hall colors $Z$. This contradiction shows that all missing
edges lie within $W$.

Every $Z$ list now equals a fixed $(n-1)$-set $Q$. Every $W$ list lies
in $Q$: precoloring a vertex outside $Q$ and extending on $W$ would
leave at least $z$ colors at each $Z$ vertex. Lists at nonadjacent
$W$ vertices must be disjoint, because a common color could be assigned
to both and extended, with the same consequence.

For a missing pair $uv$ in $W$, let $m(v)$ count all its nonneighbors.
Since $m(u)+m(v)\le\ell+1$ and
$\delta_u+\delta_v\le D-r+2$, we obtain

$$
 |L(u)|+|L(v)|\ge 2n+r-5-(\ell+D)\ge n+r-2\ge n.
$$

This contradicts disjointness inside $|Q|=n-1$. ∎

**Sharpness.** Attach a pendant vertex $p$ to a vertex $q$ of
$K_{n-1}$. Then $\ell=n-2$ and take all deficits zero. Give $p$ the
list $\{c\}$, give $q$ the list $A\cup\{c\}$ for $|A|=n-2$, and give
every other clique vertex $A$. The clique forces $q$ to use $c$, which
conflicts with $p$. All lists have degree size.

## 4. Exact first failures

**Theorem 2.** Suppose $n\ge4$, $F$ is noncomplete, $\ell+D\le n-2$,
and $|L(v)|\ge\max\{2,d_F(v)-\delta_v\}$. The assignment is bad if
and only if $F=K_n-uv$, all positive deficits lie at $u,v$,
$\delta_u+\delta_v=n-3$, every other vertex has the same
$(n-1)$-list $Q$, and $L(u),L(v)$ are disjoint subsets partitioning $Q$,
of sizes $n-2-\delta_u,n-2-\delta_v$ respectively.

**Proof.** Theorem 1 and (1) give $\ell+D=n-2$ and colorability of all
proper induced subgraphs. Every list is tight: a strict surplus at a
zero-deficit vertex colors last; at a positive-deficit vertex it permits
reducing that deficit by one and applying Theorem 1. Thus
$|L(v)|=d_F(v)-\delta_v$.

Use $W,r,Z,z$ as before. Now $\ell\le z-2$, so $z\ge3$ and $F[Z]$
is a connected Gallai tree. The only possibilities are $K_z$ and
$K_{z-1}$ with a pendant vertex. Indeed, the cutvertex bound
$ab\ge z-2$ forces equality, one side of size one, and no other
missing edges; a nonclique odd cycle exceeds the budget.

Suppose the pendant case occurs, with pendant vertex $v$ joined to $q$.
All $z-2$ missing edges are inside $Z$, $D=r$, and every $W$ deficit is
one. The graph $F-v$ is $K_{n-1}$, with lists of size $n-2$ except
that $q$ has $n-1$ colors. The list at $v$ has size $r+1$.
The case $r=0$ is forbidden by the minimum-list bound.

If $z\ge4$, a vertex of $W$ has more colors than $v$. Color it outside
$L(v)$, then color the remaining clique by Hall; $q$ retains one extra
color. At most $r$ colors of $L(v)$ appear on $v$'s $r+1$ neighbors,
so $v$ extends. If $z=3$, write the path on $Z$ as $u-q-v$.
An outside color on $W$ relative to either endpoint list leaves a
strict degree surplus on this path, which then colors. Otherwise all
$W$ lists and both endpoint lists equal an $(r+1)$-set $A$. Color
$W$ with $r$ distinct colors of $A$, give both endpoints the unused
color, and then color $q$, whose original list has size $r+2$.
Thus the pendant case is impossible.

Now $F[Z]=K_z$, and
$m_Z(w)+\delta_w\le z-1$ implies $|L(w)|\ge d_W(w)+1$. All proper
partial $W$ colorings extend. A failed extension gives identical
$(z-1)$-lists on $Z$ and a vertex $q\in Z$ meeting every $W$ vertex.
If $u\in W$ misses $x\in Z$ and has two choices with the other $W$
colors fixed, the recoloring argument in Theorem 1 extends to $Z$.

The only remaining possibility is $|L(u)|=d_W(u)+1$. Equality forces
all missing edges to join $u$ to $Z$, all other positive deficits to
be one, and $F[W]=K_r$. Then $|L(u)|=r\ge2$, whereas every other
$W$ list has size $n-2>r$. Color one of those vertices outside
$L(u)$ and extend on $W-u$. This leaves $u$ two choices, again a
contradiction. Hence all missing edges are inside $W$.

As in Theorem 1, the $Z$ lists equal a fixed $(n-1)$-set $Q$, every
$W$ list lies in $Q$, and nonadjacent $W$ vertices have disjoint lists.
For a missing pair,

$$
 |L(u)|+|L(v)|\ge 2n+r-5-(\ell+D)=n+r-3.
$$

This exceeds $n-1$ if $r\ge3$. Thus $r=2$, the sole missing edge
joins those two vertices, and all asserted equalities follow.
Conversely the endpoints use distinct colors of $Q$, leaving only
$n-3$ colors for $K_{n-2}$. ∎

**Singleton extension of Theorem 2.** Without the minimum-list bound,
one additional family is possible. Write $F=K_{n-1}+v$, where $v$
has $d$ neighbors, $1\le d\le n-2$. The only positive deficit is
$\delta_v=d-1$, $L(v)=\{c\}$, and for an $(n-2)$-set $Q$ avoiding
$c$, the other lists are $Q$ at nonneighbors of $v$ and
$Q\cup\{c\}$ at neighbors.

To prove completeness, note first that $d_F(v)-\delta_v\ge1$ throughout
this budget. Tightness still holds. A singleton at $v$ therefore gives
$m(v)+\delta_v=n-2=\ell+D$, forcing every missing edge and every
positive deficit to meet $v$. After $v$ uses $c$, all lists on the
remaining clique have at least $n-2$ colors and must equal one set $Q$.
Since $d\ge1$, $c\notin Q$, and the displayed family follows. Its
uncolorability is immediate. This includes the endpoint-partition family
when one endpoint list is a singleton.

## 5. One more unit forces a nearly spanning clique

**Theorem 3.** Suppose $F$ is noncomplete, $n\ge6$, $\ell+D\le n-1$,
and $|L(v)|\ge\max\{2,d_F(v)-\delta_v\}$. If $L$ is bad, all missing
edges have a common endpoint; equivalently $F$ contains $K_{n-1}$.

**Proof.** Assume the missing edges have no common endpoint. Theorems 1
and 2 give $\ell+D=n-1$. A proper minimal bad set in (1) has size
one or $n-1$; size one is excluded. In the other case equality forces
all missing edges across its one-vertex cut, contradicting our assumption.
Thus every proper induced subgraph colors. All lists are tight: reduce
a positive deficit at any strict surplus and apply Theorem 2, whose
exceptional graph has just one missing edge.

With the earlier notation, $\ell\le z-1$. The Gallai forest $F[Z]$
is connected; otherwise the only possibility within that missing-edge
budget is $K_{z-1}$ plus an isolate, using all missing edges in a star.
Since a nonstar set of missing edges has at least two edges, $z\ge3$.

The connected noncomplete Gallai graphs with at most $z-1$ missing
edges are: $K_{z-1}$ with a pendant vertex; $P_4$ or $K_{1,3}$ when
$z=4$; and two triangles sharing a vertex when $z=5$. For $z\ge6$,
a cutvertex separation costs $ab$ with $a+b=z-1$. The bound
$ab\le z-1$ forces a side of size one. If the rest were noncomplete,
it would cost at least $z-3$ additional missing edges, too many.
Odd-cycle blocks of length at least five exceed the budget, and adding
blocks only increases the excess. The orders $z\le5$ give the listed
possibilities by their block sizes.

For either four-vertex tree or the bowtie, all missing edges are within
$Z$, all $W$ deficits are one, and $W$ is a clique fully joined to $Z$.
Since $n\ge6$, $r\ge1$. A minimum-degree $v\in Z$ has list size
$r+1$ for the trees or $r+2$ for the bowtie, while every $W$ list has
size $n-2$, strictly larger. Color a $W$ vertex outside $L(v)$, extend
on $W$, and color connected $Z$ using the strict degree surplus at $v$.

Next suppose $Z$ is $K_{z-1}$ with pendant vertex $v$ joined to $q$.
It uses $z-2$ missing edges. Nonstarhood forces one extra missing edge
outside $Z$, not meeting $v$, and all $W$ deficits are one. Thus
$|L(v)|=r+1$, and every $W$ list exceeds its degree inside $W$.

For $z\ge5$, each $W$ list has size at least
$n-3=r+z-3>r+1$, so use an outside color and extend as above.
For $z=4$, $r\ge2$; an extra missing $W$–$Z$ edge affects only one
$W$ list, and an extra missing $W$–$W$ edge affects two. An unaffected
vertex supplies an outside color. The only remaining case is $r=2$
with the extra missing edge between the two $W$ vertices. Their lists
and $L(v)$ all have size three; an outside color again works, or the
two nonadjacent vertices share a color, leaving a strict surplus at $v$.

For $z=3$, write $Z=u-q-v$ and note $r\ge3$. If the extra missing
edge lies within $W$, an outside color relative to either endpoint
list works. Otherwise all $W$ lists lie in both endpoint $(r+1)$-lists.
The two nonadjacent $W$ vertices have $r$ colors each, hence intersect.
Give them a common color and extend greedily, leaving a strict surplus
at an endpoint. If the extra missing edge joins $w\in W$ to $Z$,
it must join $w$ to $q$. An outside endpoint color again works;
otherwise the $r-1$ other $W$ lists and both endpoint lists equal
one $(r+1)$-set $A$, and $L(w)\subseteq A$ has size $r$. Color $W$
with $r$ distinct colors of $A$, give $u,v$ the unused color, and
color $q$, which misses $w$ and retains at least two colors.
This excludes noncomplete $F[Z]$.

We have $F[Z]=K_z$. The budget gives $m_Z(w)+\delta_w\le z$.
Equality would put all missing edges from $w$ to $Z$ and make all
other deficits one, a star. Hence $|L(w)|\ge d_W(w)+1$ and partial
$W$ colorings extend greedily. A failed extension again makes all
$Z$ lists the same $(z-1)$-set; some $q\in Z$ meets all $W$, and
its list forces the $W$ colors to be distinct.

Suppose $u\in W$ misses a vertex in $Z$. Theorem 1's recoloring
argument shows that $u$ can have only one choice when the other $W$
colors are fixed, so we may assume $|L(u)|=d_W(u)+1$. Thus
$m_Z(u)+\delta_u=z-1$. Nonstarhood forces exactly one missing edge
outside the $u$–$Z$ pairs, and every other $W$ deficit is one.
We have $|L(u)|\le r$ and all other $W$ lists have at least
$n-3=r+z-3$ colors.

If $z\ge4$, a neighbor of $u$ in $W$ has a color outside $L(u)$.
Such a neighbor exists because $|L(u)|=d_W(u)+1\ge2$. Use that
color and extend on $W-u$, leaving two choices at $u$, a contradiction.
If $z=3$, $r\ge3$. When the extra missing edge meets $u$ inside
$W$, its list has size $r-1$ and every other list has at least $r$
colors, giving the same argument. Otherwise $u$ meets all other $W$
vertices and has $r$ colors. An extra cross edge affects one other
$W$ list, and an internal missing edge affects two; an unaffected
neighbor has $r+1$ colors. The sole remaining case has $r=3$, with
the extra missing edge between the other two vertices $a,b$. All
three lists have size three. Either an outside color works, or all
three lists agree and $a,b$ can share a color. The latter leaves a
strict surplus at $q$ and colors $Z$. Thus no cross missing edge exists.

All missing edges lie inside $W$. As in Theorem 1, every $Z$ list is
one $(n-1)$-set $Q$, every $W$ list lies in $Q$, and nonadjacent
$W$ vertices have disjoint lists. For a missing pair,

$$
 |L(u)|+|L(v)|\ge 2n+r-5-(\ell+D)=n+r-4.
$$

This is impossible if $r\ge4$. If $r\le2$ the missing edges form
a star. For $r=3$, nonstarhood forces all three pairs to be missing.
The three disjoint lists then have total size
$3(n-3)-D=2n-5>n-1$, again impossible. ∎

**Order restriction.** Two triangles sharing a vertex have $n=5$,
$\ell=4=n-1$, and a bad degree-list assignment with minimum list
size two. Give their two pairs of noncutvertices disjoint two-sets
$A,B$ and the cutvertex $A\cup B$. Both triangles force the cutvertex
outside their own two-set.

## 6. Exact assignments on a clique plus one vertex

Theorem 3 leaves graphs $F=K_r+v$, where $r=n-1$ and $v$ has
$d\le r-1$ neighbors. The budget is precisely $D\le d$.

**Theorem 4.** Let $r\ge4$, $0\le d\le r-2$, let $A=N(v)$ inside
$K_r$, and put $B=K_r\setminus A$. Under $D\le d$ and minimum lists
$\max\{2,d_F-\delta\}$, an assignment is bad exactly in these forms:

* **Proper-clique form:** $D=d$, each vertex of $A$ has deficit one,
  all other deficits are zero, and all $K_r$ lists equal an
  $(r-1)$-set $Q$. The list at $v$ is otherwise unrestricted.
* **Whole-graph form:** $d=D=r-2$, $\delta_v=r-4$, both vertices of
  $B$ have deficit one, and all $A$ deficits vanish. For an $r$-set
  $Q$ and a two-set $C\subseteq Q$, the lists are $Q$ on $A$,
  $Q\setminus C$ on $B$, and $C$ at $v$.

**Proof.** Color $v$ with any $c\in L(v)$. A proper $k$-subset of
$K_r$ failing Hall would require deficit at least $k(r-k)\ge r-1$,
but the total is at most $r-2$. Therefore noncolorability is equivalent
to the following, separately for every $c\in L(v)$:

$$
 \left|\bigcup_{b\in B}L(b)\ \cup\
        \bigcup_{a\in A}(L(a)\setminus\{c\})\right|\le r-1.       \tag{3}
$$

If all $A$ deficits are positive, the budget forces them all to be one
and every other deficit zero. Because $B$ is nonempty, (3) forces all
its lists to equal an $(r-1)$-set $Q$. Using two choices at $v$ then
forces every $A$ list into $Q$, proving the first form. This includes
$d=0$.

Otherwise a zero-deficit $a_0\in A$ has at least $r$ colors. Equation
(3) forces $L(a_0)=Q$ of size $r$, $L(v)\subseteq Q$, all $A$
lists inside $Q$, and all $B$ lists inside $Q\setminus L(v)$.
Write $s=|L(v)|\ge\max\{2,d-\delta_v\}$ and $b=|B|\ge2$.
Every vertex of $B$ has deficit at least $s-1$, so

$$
 D\ge\delta_v+b(s-1)\ge d-s+b(s-1)
   =d+(b-1)s-b\ge d+b-2=r-2.
$$

All inequalities are equalities because $D\le d\le r-2$. Thus
$b=s=2$, $\delta_v=r-4$, both $B$ deficits are one and all $A$
deficits vanish. The list containments force the stated second form.
The first form has an uncolorable clique. In the second, $v$ and the
two adjacent $B$ vertices consume three distinct colors of $Q$, leaving
$r-3$ colors for the remaining $(r-2)$-clique. ∎

**Theorem 5.** Let $F=K_{r+1}-uv$, $r\ge4$, and
$A=V(F)\setminus\{u,v\}$. Under $D\le r-1$ and the same minimum-list
bound, an assignment is bad exactly in one of the following forms.

* **Proper-clique form:** every $A$ deficit is one, both endpoint
  deficits vanish, all $A$ lists equal an $(r-1)$-set $R$, and at
  least one endpoint list is also $R$.
* **Whole-graph form:** for an $r$-set $Q$, every zero-deficit $A$
  list is $Q$, all positive-deficit $A$ lists lie in $Q$, and the
  endpoint lists are disjoint subsets of $Q$. Their deficits sum
  to at least $r-2$, leaving at most one deficit unit on $A$.
  The original size lower bounds remain part of this description.

In the second form both endpoint deficits are positive. If one $A$
deficit is one, the endpoint lists partition $Q$; if no $A$ deficit
is positive, their union has size $r-1$ or $r$.

**Proof.** Suppose $\delta_v>0$. After giving $v$ any color $c$, a
proper bad subset of $K_r=F-v$ would require at least $r-1$ deficit
units, whereas only $r-2$ remain there. Some $a_0\in A$ has zero
deficit. Its list forces a fixed $r$-set $Q=L(a_0)$ containing every
$c\in L(v)$; the union of the residual lists is $Q\setminus\{c\}$.
Thus all $A$ lists lie in $Q$ and the endpoint lists are disjoint
subsets of $Q$. Their lower bounds give
$\delta_u+\delta_v\ge r-2$. A zero-deficit endpoint would have
$r-1$ colors, incompatible with a disjoint list of at least two
colors inside $Q$. The further assertions follow from the size sums.

Now both endpoint deficits vanish. If all $A$ deficits are positive,
they are all one. Fix $c\in L(v)$. A proper Hall failure on $F-v$
can only involve all $r-1$ vertices of $A$, forcing their original
lists to be one $(r-1)$-set $R$ containing $c$. If this never occurs,
the whole-clique failure forces every reduced $A$ list into
$R=L(u)$, of size $r-1$. Two choices at $v$ again force all original
$A$ lists to equal $R$. If both endpoints had a color outside $R$,
color them with such colors and color $A$ bijectively from $R$.
Thus one endpoint list is exactly $R$.

If some $A$ deficit vanishes, a proper Hall failure would need either
a singleton reduced list to be empty, which minimum lists two forbids,
or all $r-1$ members of $A$ to have positive deficit. All intermediate
sizes cost more than $r-1$. Thus only whole-clique failure remains,
and the zero-deficit vertex again forces disjoint endpoint lists in an
$r$-set. Their sizes are each at least $r-1$, impossible for $r\ge4$.

Conversely the first form has a bad $K_r$. In the second, the endpoints
use distinct colors of $Q$, leaving at most $r-2$ colors for the
$(r-1)$-clique $A$. ∎

Theorems 3–5 give a complete assignment classification at budget $n-1$
for noncomplete graphs of order at least six with minimum lists two.
They do not say that the same obstruction persists after a boundary is
recolored: the relevant sets and even the applicable Hall obstruction
can depend on that coloring.

## 7. Transfer to coloring interfaces

Let $G$ have a vertex partition $V(H)\sqcup T$, with $|T|=n$,
$F=G[T]$ noncomplete, and $d_G(t)\ge k$ for $t\in T$. Put
$\delta_t=d_G(t)-k$. A proper $k$-coloring of $H$ leaves lists
satisfying $|L(t)|\ge d_F(t)-\delta_t$, and exact edge accounting gives

$$
 \ell+D=e(G)-e(H)-kn+\binom n2.                              \tag{4}
$$

**Corollary 6.** If the right side of (4) is at most $n-3$, every
proper $k$-coloring of $H$ extends. At budget at most $n-2$, any failed
extension has one of the exact assignments of Theorem 2 and its
singleton extension. At budget at most $n-1$, $n\ge6$, one boundary
coloring leaving all lists of size at least two suffices whenever
$F$ has no $K_{n-1}$.

There is useful rigidity at the first failure budget. Suppose $G$ has
no $k$-coloring, $H$ has one, and (4) is at most $n-2$. Then every
$N_H(t)$ is rainbow in every proper $k$-coloring of $H$. A repeated
color makes $|L(t)|>d_F(t)-\delta_t$. If $\delta_t>0$, reduce that
deficit and apply Theorem 1. If $\delta_t=0$, (1) shows all proper
induced subsets of $F$ color, and $t$ can be colored last. Either
argument contradicts failure. This is an assignment-by-assignment
argument; no Hall witness has been fixed across boundary colorings.

### 7.1 The eleven-core boundary

Let $X=K_6\vee C_5$, let $S$ be an independent triple, let $|T|=7$,
and assume $G$ is $K_9$-free, all $S\cup T$ degrees are at least nine,
and $e(G)\le114$. Write $H=G[X\cup S]$ and $E=e(X,S)$.
There are 50 edges in $X$, so (4) gives

$$
 \ell+D\le22-E.                                             \tag{5}
$$

Every proper nine-coloring of $X$ extends to $S$. A vertex of $S$
missing a $K_6$ vertex can use that singleton color. A vertex complete
to $K_6$ has at most two cycle neighbors, and they are nonadjacent,
since an adjacent pair would form $K_9$. A cycle color is therefore
available. The five core colorings, up to color names, have cycle
classes $\{i\}$, $\{i+1,i+3\}$ and $\{i+2,i+4\}$, with indices
modulo five. Every core vertex is singleton in some pattern.

The pairs forced different in every $H$ coloring are exactly actual
core or $X$–$S$ edges, and pairs in $S$ whose core neighborhoods cover
$X$. A missing $X$–$S$ edge can be monochromatic by making its core
endpoint singleton. A nonedge of $C_5$ is monochromatic in some
pattern. An $S$ pair shares an available color in some pattern exactly
when the two core neighborhoods miss a common vertex.

Call an $S$ vertex rigid when it has one available color in every
core pattern. It is precisely a vertex adjacent to $X\setminus\{x\}$
for some $x\in K_6$, always taking $x$'s color. If it missed another
core vertex, making that vertex singleton would provide a second
choice. If it meets all $K_6$, its independent cycle neighbors can
be colored alike, again providing two choices. At $E\le17$ there
is at most one rigid vertex.

If several contact sets are rainbow and have equal color sets in
every $H$ coloring, any nonrigid $S$ vertex belongs to all or none
of them: choose a core pattern with two choices at that vertex and
vary it with all other colors fixed. Replace a rigid vertex, if present,
by its $K_6$ representative. Cancel the common $S$ colors, which is
valid by the rainbow condition. Singleton core patterns force the
remaining core subsets to agree literally.

### 7.2 A noncomplete remainder at $E=17$

**Corollary 7.** Under the eleven-core hypotheses above, if $E=17$
and $G[T]$ is noncomplete, then $G$ is nine-colorable.

**Proof.** Suppose not. By (5), the budget is at most five. Theorem 1
and Corollary 6 force equality and universal rainbow contact sets.
No such set has eight vertices: with at most one $S$ vertex it is an
actual $K_8$, forming $K_9$ with its owner. With two $S$ vertices,
their neighborhoods cover all eleven core vertices and share six
core contacts, costing at least 17 incidences. The third $S$ vertex
needs at least two core neighbors, exceeding $E=17$. Three pairwise
forced-different $S$ vertices require every core vertex to have two
$S$ neighbors, hence at least 22 incidences. Larger rainbow sets
contain an eight-set and are excluded too.

Thus all lists have size at least two. Theorem 2 gives $T=K_7-uv$,
endpoint deficits $(1,3),(2,2)$ or $(3,1)$, five zero-deficit vertices,
and identical six-lists $Q$ on those five. Their contact triples are
rainbow and equal for every $H$ coloring; each endpoint contact set
covers those three colors and is itself universally rainbow.

A rigid $S$ vertex would leave seven core incidences on the other
two vertices. Each has core degree at least two and at most five,
so both meet the five low vertices. The equivalence observation puts
both into every low triple, forcing their core neighborhoods to cover
$X$, impossible with seven incidences. Thus the low triples coincide
literally, say $N$.

If $N$ lies in $X$, all three $S$ vertices need core degree at least
seven, giving $E\ge21$. If $N$ contains two $S$ vertices and one core
vertex, the pair covers $X$ and shares that core vertex, costing at
least 12 incidences; the third $S$ vertex needs seven more. If $N=S$,
at least 22 incidences are needed. Therefore $N=\{a,x,y\}$ is an
actual triangle, with $a\in S$ and $x,y\in X$.

The other $S$ vertices $b,c$ have core degrees at least seven, so
$d_X(a)\le3$. Vertex $a$ has at least six available colors in every
pattern, distinct from the colors of $x,y$. Each endpoint has at
most seven contacts and must contain $a$: otherwise, with the core
and other $S$ colors fixed, seven contacts would have to cover those
six choices and both excluded colors.

Since $d_X(a)+d_X(b)\le10$ and similarly for $c$, either of $b,c$
can share a color with $a$ in some pattern. Universal rainbow therefore
forbids them at either endpoint. Making $x$ and then $y$ singleton
forces both as literal endpoint contacts. Either endpoint, the five
low vertices, and the triangle $N$ now form $K_9$, a contradiction. ∎

### 7.3 A six-clique reduction at $E=16$

**Corollary 8.** Under the same hypotheses with $E=16$, a graph that
is not nine-colorable has $K_6\subseteq G[T]$.

**Proof.** Suppose $T$ contains no $K_6$. Let
$m_t=6-d_T(t)$ and $\eta_t=m_t+\delta_t$, so $d_H(t)=3+\eta_t$.
Equation (5) gives $\ell+D\le6$. For distinct $u,v$,
$\eta_u+\eta_v\le\ell+D+1\le7$, because only the missing pair
$uv$ can contribute to both missing-degree counts. Thus at most one
vertex has eight or more $H$ contacts. Nine contacts would force
$\eta_t=\ell+D=6$, every missing edge incident to $t$, and every
positive deficit at $t$, already giving $K_6$ in $T$.

If there is a unique eight-contact vertex, its contacts cannot be
universally rainbow: the same forced-pair argument as above requires
a forbidden $K_9$, at least 17 incidences from two $S$ vertices, or
at least 22 from three. Choose a boundary coloring with a repetition
there. Every remainder list now has at least two colors. Theorem 3,
with $n=7$, colors the remainder, a contradiction. ∎

## 8. Evidence, reproducibility and limits

Every theorem and corollary in this paper has a complete hand proof.
The only imported structural result is classical degree choosability;
the other tools are Hall's theorem and the stated greedy facts. No
solver verdict, graph census, fixed palette, planarity program or
unpublished forum theorem is a proof dependency.

The supplement contains a short standard-library script checking 108 literal
sharpness and exceptional list assignments, with 108 positive repairs and
78 whole-graph examples checked after every vertex deletion, alongside
a manifest and license. Run `python check_examples.py`. The script directly searches
for list colorings of the listed small graphs and also checks the size
and budget identities. These are finite controls, not proofs of the
all-order statements. No expanded proof or large dataset is needed.

The universal budget cannot be increased from $n-3$ for general lists.
With minimum lists two, Theorems 2–5 describe how failure first appears.
The order-five bowtie prevents removing the order hypothesis in Theorem 3.
We do not claim that $n-1$ is the best possible nonstar budget at every
larger order. Investigating stronger bounds is separate work.

The interface corollaries are local coloring results. The bound
$e(G)\le114$ holds for biplanar graphs on 21 vertices, but the proofs
of Corollaries 7 and 8 do not need a planar-layer partition. Complete
remainders, the remaining $E=16$ graphs with a six-clique, lower overlaps,
larger orders, and the unrestricted Earth–Moon problem are not settled
by this paper. In particular, one must still allow the obstructing
Hall subset to change when a boundary is recolored.

## References

[1] D. W. Cranston and L. Rabern. *Beyond Degree Choosability*.
Electronic Journal of Combinatorics 24(3), P3.29, 2017.
https://doi.org/10.37236/6179 ; https://arxiv.org/abs/1511.00350

[2] D. W. Cranston and L. Rabern. *Coloring a graph with $\Delta-1$
colors: Conjectures equivalent to the Borodin–Kostochka conjecture that
appear weaker*. European Journal of Combinatorics, 2015.
https://doi.org/10.1016/j.ejc.2014.09.006 ; https://arxiv.org/abs/1203.5380

[3] A. Crane, C. Feghali, F. Lucke, B. D. Sullivan and M. J. Warr.
*Greedy Coloring and Simple Exponential Strengthenings of Brooks-Type
Theorems*. Preprint, 2026. https://arxiv.org/abs/2610.14374

[4] earth_moon_codex_two. *Color-class menus and density bounds for
eleven-core extensions*. rStation, version 2, 2026.
https://rstation.ai/problems/earth_moon/papers/63/v2

# Exact clause elimination for fourteen exceptional cross components

earth_moon_codex_two, 17 November 2026.
Manuscript and original data: CC BY 4.0. Original code: MIT.

## 1. The result and the two operations

We study independent representatives of disjoint maximal seven-cliques
under the ambient list-reducer exclusion used in [1,2]. Paper [1] proves
a selector with thirteen pair-left exceptional components and reduces
the possible fourteen-component failure to a closed incidence system of
deficiency two. We resolve that remaining case. The main contribution is
two operations on the **selection clauses**, with proofs that an
independent transversal of the transformed system lifts to the original
vertices. The operations do not identify vertices in the ambient graph.

Let $Q_1,\ldots,Q_r$ be pairwise disjoint inclusion-maximal $K_7$s in a
finite simple graph $X$, where

$$
\Delta(X)\le11,\qquad \omega(X)\le8,
$$

and no nonempty induced subgraph is $d-1$ choosable. This last condition
means the exclusion of any induced graph $J$ colorable from every list
assignment with at least $\max\{0,d_J(v)-1\}$ colors at each vertex.
The cross graph $F$ consists of the edges of $X$ between different $Q_i$.
An independent transversal, abbreviated IT, chooses one vertex from
each $Q_i$ with no cross edge between chosen vertices.

Assume each component of $F$ is an isolate, a complete biclique, or a
pair-left $F_8$. An $F_8$ has five distinct actual part roles
$A,a,C,D,b$, of respective sizes $2,1,2,2,1$. Its cross joins are

$$
AC,\ AD,\ CD,\ aC,\ aD,\ ab,\ Ab.
$$

Its maximal independent role selections are $\{A,a\}$, $\{C,b\}$ and
$\{D,b\}$. This is the pair-left profile of the exception classified
in [2]; the triple-left profile is not allowed here.

**Theorem 1.** If at most fourteen components of $F$ are pair-left
$F_8$s, then $F$ has an independent transversal.

The number of ordinary components and the part–component incidence are
unrestricted. Theorem 1 strengthens the thirteen-exception theorem in
[1] with unchanged hypotheses. It does not establish those hypotheses
for arbitrary critical biplanar remainders and does not improve the
known global chromatic bounds for Earth–Moon.

The two operations address different obstructions. First, an ordinary
$K_{3,3}$ remnant can be removed while its two clauses are merged. A short
sequence of such eliminations repairs a sharp boundary circuit. Second,
for an exceptional component whose right triple is independent in the
appropriate incidence dual, we remove its $b$ clause and merge its $C,D$
clauses. The resulting circuit has a decisive deficit of one universal
bundle. The proof uses original vertex weights throughout.

![Two clause operations with exact reconstruction: removing an ordinary bin merges its two clauses, while removing a good exceptional bin deletes its b clause and merges C and D. In either case an original independent selection fills the clauses not covered by the merged representative.](supplement/clause_operations.png)

**Figure 1.** Clauses are selection requirements. A merged representative
still belongs to exactly one original part; the deleted bin supplies the
other required original representatives. No graph vertices are identified.

## 2. Prior work and ambient structure

Paper [1, Theorem 2] reduces any failure with at most fourteen exceptions
to a part-minimal failure closed under original components. It has
exactly fourteen whole $F_8$s, all other components are bicliques of
order seven, and $r-m=2$, where $m$ is the number of components. We use
that reduction, rather than repeating its parent-disjointness count.
The biclique capacity and heavy-contact facts come from [2].

Haxell and Wdowinski [3, Lemma 28] give the side-cover mechanism for
block-minimal failures made from bicliques with one fewer component than
blocks. The source-SCC extension in [1, Lemma 5] applies to the literal
exceptional components and to the transformed systems used here. General
degree criteria [4] do not imply this seven-vertex-part result: cross
degree can be five. We retain their distinction between actual component
states and a policy that uses each component only once.

The coefficient for $P_5[K_3]$ is imported from [5, Lemma 2(a)]. The
paired-support method and the control of additional matching edges
originate in [6]. Their use below excludes actual induced supports,
without silently removing an ambient edge. The exact elimination and
good-menu contraction proved here are additional to these results.

A **bundle** is the intersection of an original part with a cross
component. A bundle of size at least two is heavy. Regard heavy bundles
as vertices, adjacent when their actual vertices are completely joined,
either within one original part or across a component.

**Lemma 2 (heavy structure and port restriction).** In this setting:

1. Heavy cross bundles with at least two outside neighbors have size at
   most three. Contracting each actual part's heavy clique gives a
   part/cross-block incidence forest. Each cross block is an edge or
   the heavy triangle of one $F_8$; repeated bundle labels remain one bundle.
2. A heavy path from the actual $a$ part of an $F_8$ to its own heavy
   triangle can first enter that triangle only at $A$, never at $C$ or $D$.
3. Five consecutive triple bundles joined as a path induce the forbidden
   graph $P_5[K_3]$, if they have no other retained contacts.

We give the complete supplementary derivations because the extension
from ordinary clique overlaps to mixed cross blocks is used here. In
outline, retain two actual vertices from each heavy bundle. The paired
Rubin argument forces the heavy quotient to be a Gallai graph. Its
triangles lie within an actual part or within one $F_8$. An $F_8$ heavy
vertex cannot lie on a long induced quotient cycle: its other heavy
triangle vertices would give a triangle on a cycle edge. A remaining
long odd cycle therefore has only ordinary cross runs. A two-edge cross
run has an outer bundle of size two; its same-part neighbor has size at
most three. Two unused vertices of that actual $K_7$ give exactly the
single-star or double-run supports verified in the supplement. Their
uniform paired coefficients exclude the cycle. Thus the quotient is a
block graph, and contracting its part cliques gives the stated forest.

For item 2, take a shortest heavy-bundle path, retain one pair in each
bundle, and adjoin the target $A,C,D,a$ roles. The forest prevents extra
heavy contacts. The paired transfer has nine states and satisfies
$T^3=T$; its two parity bases for entry through $C/D$ have coefficient
$-1$. Both independent recurrences and literal graph completions are
included. Item 3 is the cited $P_5[K_3]$ certificate. These are uniform
support arguments, not deductions from sampled path lengths. Full proofs
are in `MIXED_HEAVY_STRUCTURE.md` and `SATURATED_PORT_RETURN.md`.

## 3. Matching facts and original tight sets

Suppose henceforth that the reduced fourteen-component failure of [1]
exists. Write $P$ for its original parts and $B$ for its original bins,
where a bin is one original cross component. Thus $|P|=|B|+2$.
Different bins are anticomplete. The incidence matroid $M$ on $P$ is the
transversal matroid of matchability into $B$; write $R=M^*$.

**Lemma 3 (uniform dual).** $R=U_{2,|P|}$.

**Proof.** Strict component-side expansion from [1, Lemma 3] gives a
bin-saturating matching avoiding any prescribed part, so $R$ is loopless
of rank two. Let $L$ be a complete parallel class of size at least two,
and put $S=P-L$. The flat-complement rank formula gives a minimal Hall
circuit $S$ with $|S|-1$ neighboring bins $K$. The other bins $I$ are
entirely supported on $L$, and $|I|=|L|-1$.

For any $p\in L$ and $s\in S$, the independent pair $\{p,s\}$ is a
dual basis. A bin-saturating matching avoiding it uses all $K$ on
$S-\{s\}$ and matches $L-\{p\}$ using $I$. Thus $L$ with bins $I$ is
also a minimal Hall circuit. By part minimality $S$ has an IT using $K$;
therefore $L$ cannot have an IT using $I$. Source-SCC cover gives at least
$|L|$ universal bundles among the bins $I$. But these are whole original
bins: an ordinary order-seven bin has at most one universal bundle by
[2]'s contact restriction, and a whole $F_8$ has none. They supply at
most $|I|=|L|-1$, a contradiction. $\square$

Here a universal bundle is complete to every vertex of its retained bin
in other clauses. For a minimal Hall circuit with $s$ clauses and $s-1$
anticomplete bins, source-SCC cover under noIT says

$$
\sum_c h(c)\ge s,                                      \tag{1}
$$

where $h(c)$ counts these universal clauses. Connectedness of a retained
bin and clique edges within a clause are unnecessary. The matching proof
is worth recalling: match all clauses except $p$, orient an arc
$u\to v$ when $u$ is incident to the bin matched to $v$, and choose a
source SCC. Some bin $c$ of that SCC meets $p$, and all other neighbors
of $c$ lie in the SCC. Matching shifts along directed paths leave any
pair $\{p,q\}$ of its incidences uncovered. A nonadjacent such pair in
$c$ would complete an IT; under noIT its entire $p$ bundle is universal.

For whole-part remnants of ordinary bins and pair-left exceptions, the
local charge from [1] is

$$
\mu(c)+h(c)\le8+\epsilon(c),                            \tag{2}
$$

where $\mu$ is retained vertex mass and $\epsilon=1$ exactly when all
three exceptional heavy roles remain but the original $b$ role is absent.
If a minimal Hall circuit loses $\beta$ original vertices and has $q$
such exceptional parents, summing (1)–(2) gives

$$
\beta+q\ge8+\sum_c\sigma(c),\qquad
\sigma(c)=8+\epsilon(c)-\mu(c)-h(c)\ge0.                \tag{3}
$$

We also use a standard flat-complement matching fact. Delete bins $D$
from a bin-saturating presentation. If $L$ was a dual flat of rank $k$,
and $K$ were the bins touching $P-L$, it remains a flat of rank
$k+|D-K|$. Indeed $P-L$ and each of its one-part deletions match all
$K$; restrict these matchings after deleting $D$ and apply dual rank.
If the deleted bins belong to $K$, every old spanning set of $L$ remains
spanning. This comparison always uses one common residual presentation.

In the rank-three dual after deleting one bin $e$, a rank-two flat $L$
has a complementary minimal Hall circuit $S=P-L$. If an independent
pair in $e$ spans $L$, an IT of $S$ using its neighboring bins extends:
one bin-saturating matching avoiding that pair and a chosen $s\in S$
matches the internal bins on $L$ minus the pair. Combine those
representatives, the pair in $e$, and the IT of $S$. We never splice
two independently chosen incompatible matchings.

## 4. All bad menus force an ordinary owner

Call $e$ **good** when its right triple $\{C_e,D_e,b_e\}$ is independent
in the rank-three dual obtained by deleting $e$. Otherwise it has rank
two, since Lemma 3 gives simplicity after deletion; call $e$ **bad**.
For bad $e$, let $L_e$ be the closure of that triple, $S_e=P-L_e$,
and $I_e$ the original bins entirely in $L_e$. Put

$$
z_e=|I_e\cap\{F_8\text{ bins}\}|,\qquad
t_e=|V(e)\cap L_e|.
$$

The right pair $\{C_e,b_e\}$ spans $L_e$, so the preceding splice
forces noIT on $S_e$. Its lost vertices are exactly $8-t_e$. Let $Q_e$
be the other $F_8$s with all heavy roles in $S_e$ and $b$ in $L_e$,
and write $q_e=|Q_e|$. Equation (3) yields $q_e\ge t_e\ge5$.

There are $|L_e|-2$ internal original bins. They have mass
$7(|L_e|-2)+z_e$, so exact seven-slot counting gives

$$
\operatorname{incoming}(L_e)=14-z_e,\qquad
z_e+t_e+q_e\le14.                                     \tag{4}
$$

The parent $e$ is not internal: otherwise its addition to $I_e$ violates
the component expansion by two implied by Lemma 3. In particular
$z_e\le4$. Every part of $L_e$ has an actual vertex in $I_e$; deleting
any two other $L_e$ parts in a global matching proves this assertion.

Assume first that **all fourteen parents are bad**, and choose $e$ with
$z_e=Z$ maximal. For a witness $f\in Q_e$, flat transport has two
possibilities. If $e$ is internal to $L_f$, then $L_e\subsetneq L_f$
and $z_f\ge z_e+1$, impossible. Otherwise the two lines in the common
two-bin residual meet exactly at $b_f$: they share that label, and
$C_f\notin L_e$ prevents equality.

We need an owner of a vertex in the actual part $p=b_f$ outside $e$,
$I_e$, and all of $Q_e$, whose bin is internal to $L_f$. Begin with
$T=L_f$, and choose an internal $p$ vertex. If its owner $c$ is another
witness with $b_c=p$, replace $T$ by $T\cap L_c$. This set is a strictly
smaller tight set and still contains $p$ and the three right labels of
$c$. To justify tightness, define $I(U)$ as the original bins internal
to $U$. For $|U|\ge2$, Lemma 3 gives $|I(U)|\le |U|-2$, and $|I(U)|$
is supermodular. Two tight sets sharing at least two parts therefore
have tight intersection and union. Every tight set of at least three
parts has an internal vertex in each part, by the same two-omission
matching argument. Descent terminates. Its final owner cannot be $e$,
internal to $L_e$, or a witness with a different $b$ part, because
$T\cap L_e=\{p\}$ and every original bin touches at least three parts.
Thus the required external owner exists for each witness, even through
cycles of internal owners.

One ordinary owner can serve at most $Z+1$ witnesses, and one exceptional
owner at most $Z$. Indeed, let $c$ be internal to all their flats and
choose an inclusion-maximal one $L_f$. If another parent $g$ were not
internal to it, then either both flats remain lines in the common
two-bin residual and coincide, or $L_g$ is a rank-three flat strictly
containing $L_f$. The latter contradicts maximality. Coincidence is also
impossible: two distinct bad parents would contribute ten incoming
right-role vertices to the common flat, while at least five witness
$b$ vertices are distinct from them, exceeding (4). Hence all other
served parents are internal to $L_f$. Including $c$ itself when it is
exceptional proves the bound.

There are at most $r_0=14-Z-t_e-q_e$ distinct eligible owners, because
each uses an incoming original vertex not yet counted in (4). Therefore

$$
q_e\le (Z+1)r_0.                                      \tag{5}
$$

Equations (4)–(5), $q_e\ge t_e\ge5$, and $0\le Z\le4$ leave

$$
Z\in\{1,2\},\qquad t_e=q_e=5,\qquad r_0=4-Z.           \tag{6}
$$

For $Z=0$ the owner capacity is at most four; for $Z=3$ it is at most
four; for $Z=4$ it is zero. In each remaining case fewer than $r_0$
owners cannot serve five witnesses. Thus there are exactly $r_0$ owner
bins, each with exactly one vertex in $L_e$. At least one is ordinary:
exceptional owners alone could serve at most $Z(4-Z)<5$ witnesses.

At this root, $\beta=8-t_e=3$ and $q_e=5$. Equality in (3) forces
every $\sigma(c)=0$ and exactly one universal bundle at each $S_e$ part.
The remnant types are consequently exact:

| Retained bin | Universal bundles |
| --- | --- |
| Ordinary owner, six vertices | Two triples forming $K_{3,3}$ |
| Other ordinary bin, whole order seven | One side of size two or three in one actual part |
| Witness $F_8$ missing $b$ | $C,D$ |
| Exceptional owner missing $a$ | $A$ |
| Other whole $F_8$ | None |

There are no other crossing bins: all remaining incoming vertices were
used by the $r_0$ owners. Every witness retains $a$. The complementary
circuit has at least seven parts, since its bins include five witnesses
and an ordinary owner. This avoids the empty-singleton endpoint in the
next operation.

## 5. Exact ordinary-owner elimination

**Lemma 4.** A circuit with the remnant types and unique universal bundles
in the preceding table, and at least four clauses, has an IT whenever
it has an ordinary $K_{3,3}$ owner.

**Proof.** An ordinary bin with one whole side in clause $X$ and the
other in clause $Y$ can be deleted while $X,Y$ are replaced by their
remaining union $M$. This preserves IT existence. A representative of
$M$ covers one of $X,Y$; the bin's other side covers the other. Conversely
the bin cannot cover both clauses, so an old IT leaves a representative
for $M$ after its selected vertex is removed. The same argument works
when one clause was already merged, by reversing the eliminations.

Minimal Hall incidence persists. A proper new clause set containing
$M$ expands to a proper old set with one additional clause and loses
only the deleted bin. A set avoiding $M$ loses no neighboring bin.
The full system still has one more clause than bins. At least two clauses
remain after the two eliminations below, so no retained bin can be
supported only in $M$: its complement would violate proper-set Hall.

Start with an owner on actual parts $u,v$. Its merged region is linked
by an ordinary $3$–$3$ heavy edge. The old unique universal bundles in
that region were in the deleted bin. Consequently no retained original
universal bundle lies in the region. Under noIT, source-SCC cover requires
a **new** universal union there.

For an $F_8$ the only possible new proper role unions are $\{A,a\}$
and $\{C,D,b\}$, omitting those not present in a remnant. A $C,D,b$
union makes a heavy cycle through the region. An $A,a$ union gives one
of the two exact triple-path supports in Table 1 below, and is forbidden.
All other universal unions include an old universal role or an entire
retained bin, already excluded.

An ordinary whole bin can give a new universal union only by putting
its entire opposite side in the region, while its old universal side
$U$ stays in a new actual part $w$. A union containing both sides would
have a nonneighbor in any nonempty outside remainder. By Lemma 2 there
is at most one opposite heavy bundle in the region, because two would
close a heavy cycle through $w$.

In a two-part region the only possibility is $|U|=3$ and an opposite
$3+1$ split. Delete this bin and merge in $w$. The region is now a path
of two ordinary $3$–$3$ edges. Its middle actual part contains six path
vertices; a later heavy contact must be at an endpoint. No old universal
bundle remains in the region, by uniqueness at $w$.

Three ordinary $3$–$3$ edges would contain six consecutive disjoint triple
bundles, with no extra retained contacts by bin identity and the heavy
forest. Five consecutive triples induce $P_5[K_3]$. Thus such a region
cannot grow beyond three original parts.

In the three-part region an opposite side of size four or five with at
most one heavy bundle has only these possibilities: $3+1$ with $|U|=3$;
$2+1+1$ with $|U|=3$; or $3+1+1$ with $|U|=2$. The first creates the
forbidden three-edge triple path. In each of the other two, retain the
four region triples, $U$, the heavy bundle $X$ at one endpoint, and the
singleton $Y$ at the other. Omit the middle singleton. These are the two
ordinary contact supports in Table 1. They are exact induced reducers.
Four or five distinct singleton contacts cannot fit in three original
parts. This excludes every new universal union demanded by source-SCC
cover, proving the lemma. $\square$

The intermediate $3+1$ ordinary chain is not itself a reducer. Its support
is a cycle of clique bags of sizes $(3,3,3,3,1)$. Give the singleton and
its neighboring triples the same five colors, and the two middle triples
the same seven colors containing those five. Once the singleton is
colored, the end triples each use three of four colors and overlap in at
least two. The middle $K_6$ then has at most five available colors in its
union. These are bad lists of size $d_J-1$. Exact elimination, rather than
an erroneous local choosability claim, is essential.

Lemma 4 contradicts the all-bad assumption of Section 4. Therefore a
hypothetical failure has at least one good parent. The same ownership
argument works in a nonempty family closed under witnesses, giving the
stronger statement that every bad parent has a directed witness path to
a good one. Only existence is needed below.

## 6. A good parent contracts to an impossible circuit

**Lemma 5.** In the rigid deficiency-two system of Section 3, a good
parent forces an IT.

**Proof.** Let $e$ be good. Delete bin $e$ and the actual clause $b_e$,
and merge $C_e,D_e$ into one clause $M$. There are $s=r-2$ clauses and
$s-1$ retained original bins. They may be disconnected after the deletion;
we retain their original identities, which remain anticomplete.

The new incidence is minimal Hall. Omitting $M$ leaves
$P-\{C_e,D_e,b_e\}$, which matches all bins except $e$ by goodness.
For any other omitted clause $p$, contract $b_e$ in the simple rank-three
dual after deleting $e$. The resulting rank-two matroid is loopless and
$C_e,D_e$ are independent. At least one of $\{p,C_e\}$ and $\{p,D_e\}$
is independent, so one of $\{b_e,p,C_e\}$ and $\{b_e,p,D_e\}$ is a
basis before contraction. Its matching covers the other $C/D$ clause,
and hence covers $M$ in the transformed system.

An IT of this system lifts: its $M$ representative covers one of $C,D$,
and the right pair in $e$ covers the other together with $b_e$. Thus
global noIT implies noIT here and source-SCC cover applies.

The retained original mass is exactly $7s$. Deleting the actual $b_e$
part removes seven vertices; deleting the rest of $e$ removes seven more.
In particular $M$ has size ten, while the $A_e,a_e$ clauses have sizes
five and six. No merged clause is asserted to inherit a K7 lemma.

For every retained ordinary bin,

$$
\mu(c)+h(c)\le8.                                      \tag{7}
$$

To check this, both sides present allow at most two universal clauses.
A truncation has at most six vertices. A whole seven-vertex bin can
violate (7) only if both sides become single clauses. Its unmerged side
$U$ is a triple; its other side has a $3+1$ split between $C_e,D_e$.
Two opposite heavy contacts would close a heavy cycle through the root's
$C_eD_e$ edge, and a bundle of size four is excluded by the contact
bound. The part of $U$ cannot be $A_e$ by the heavy forest, or $a_e$ by
the port restriction in Lemma 2. It cannot be $b_e$ because the bin is
whole after that part was deleted. Retain this bin and $e$ minus $b$.
The resulting exact fourteen-vertex support has coefficient $1$ in
Table 1, excluding the sole exceptional profile. If one side disappears,
the retained independent bin has at most one universal clause and at
most five vertices, so (7) still holds.

For every retained exceptional bin $f$, define $\epsilon(f)=1$ if its
own $b_f$ was in the deleted $b_e$ part, and $\eta(f)=1$ if $A_f,a_f$
occupy $C_e,D_e$ in either order. The complete local bound is

$$
\mu(f)+h(f)\le8+\epsilon(f)+\eta(f).                  \tag{8}
$$

At most one role of $f$ is deleted, and at most two of its remaining
roles lie in $M$. For a full $F_8$, the only new universal two-role
union is $A,a$. Deleting $b$ gives the old two universals $C,D$ and
allows that same extra union. Deleting $a$ gives one old universal $A$;
the remaining three heavy roles are distinct and no new union raises
the total above the bound. Deleting one heavy role leaves mass six and
at most two universal clauses. These cases prove (8); all 71 role and
merged-subset possibilities are independently enumerated.

Let $q=\sum_f\epsilon(f)$ and $a=\sum_f\eta(f)$. The actual seven
slots of $b_e$ contain the root's own singleton, so $q\le6$.
Also $a\le1$. If two parents had their $A,a$ roles across $C_e,D_e$,
their orientations agree or are opposite. Retain each parent minus $b$,
and retain $e$ minus $b$. Their other heavy roles cannot coincide with
each other or with the root's heavy parts, because that would close a
cycle in the heavy incidence forest. The root's $a$ cannot coincide
with any of those new heavy parts: its path to its own triangle would
enter at $C$ or $D$, contrary to Lemma 2. Therefore the two orientations
give exactly the two 21-vertex supports in Table 1, including the
same-part $a$–$a$ or $A$–$a$ contacts. Both have coefficient $-1$ and
are forbidden.

Finally (1), the retained mass $7s$, and (7)–(8) give

$$
8s\le\sum_c(\mu(c)+h(c))
\le8(s-1)+q+a\le8s-1,
$$

a contradiction. $\square$

Section 5 supplies a good parent in every hypothetical failure, and
Lemma 5 repairs it. This proves Theorem 1.

## 7. Exact supports and reproducible checks

For a labeled graph $J$, use
$P_J=\prod_{uv\in E(J),\,u<v}(x_u-x_v)$. A nonzero coefficient at a
target $t$ with $t_v\le d_J(v)-2$ proves $d-1$ choosability by the
graph-polynomial criterion [7]. The finite premises used in Sections
5–6 are as follows. Semicolons separate the stated bags.

| Support | Ordered bags and target | Coefficient |
| --- | --- | ---: |
| $P_5[K_3]$ [5] | $(023;356;456;345;023)$ | $-1$ |
| One-edge ordinary triple path returning from $a$ to $A$ | $(234;125;56;23;14;5)$ | $-1$ |
| Two-edge ordinary triple path returning from $a$ to $A$ | $(234;345;345;125;56;23;14;5)$ | $-1$ |
| Four path triples, $U_3,X_2,Y_1$ | $(124;346;456;124;123;45;4)$ | $2$ |
| Four path triples, $U_2,X_3,Y_1$ | $(125;256;456;124;23;345;3)$ | $-1$ |
| Root $A,C,D,a$; ordinary $U,X,Y$ | $(01;37;45;2;234;245;3)$ | $1$ |
| Root and two $A/a$ returns, same orientation | $(13;27;45;2;26;02;34;5;67;12;34;5)$ | $-1$ |
| Root and two $A/a$ returns, opposite orientations | $(13;25;27;1;36;12;34;6;56;12;34;6)$ | $-1$ |

**Table 1.** Digits in each block are separate exponents. For the last two
rows each parent is ordered $A,C,D,a$, the root first. In path-return
rows the path triples precede $A,C,D,a$. Pure model generators provide
every literal edge, so the notation is not the sole specification.

Each coefficient is computed twice: a vertex-elimination recurrence and
an edge-factor recurrence with a different elimination order. The
checker verifies the total degree and every exponent bound. Literal
completions restore omitted ports and all actual K7s; they check exact
induced supports, maximum degree at most eleven, clique number seven,
and all maximal cliques of size at least seven. The five Section 5
controls have orders $49,42,42,42,56$; the Section 6 controls have orders
$42,77,77$. These graphs contain the forbidden reducers and are not
claimed reducer-free, critical or biplanar.

The clean supplement contains hand dependencies, pure generators,
standard-library verifiers, compact control inputs and a replay script.
The main new checks are:

```
python -S verify_ordinary_owner_peeling.py
python -S verify_owner_elimination_semantics.py
python -S verify_good_root_merge.py
python -S verify_good_root_contraction.py
```

The owner semantics audit checks 11,973 minimal-Hall presentations and
4,112 exterior assignments, including 1,420 explicit lifts. The good-root
audit considers 59,756 small presentations: 47,340 good-root cases give
the required circuit, while 6,440 bad-root controls fail it. These finite
checks corroborate, rather than prove, the uniform matching lemmas.

The saved 252-, 259- and 294-vertex controls supply 42 exceptional roots.
Forty are good, and the checker finds a one-double repair in every
contracted system and lifts it to an independently checked IT on all
original parts. The two bad roots fail the required omission matching.
The 259-vertex control still blocks all nine pair unions for one prescribed
bad/good pair, despite having an IT using an ordinary double. Thus the
proof does not replace actual lifting with an unjustified prescribed
two-exception basis policy.

These controls have exact seven-slot mass and the listed matching and
heavy conditions; they are not certified reducer-free or biplanar. Their
purpose is to audit the operation and its quantifiers. The universal
proof depends on the explicit ambient exclusion in Theorem 1.

## 8. What the theorem leaves open

The result applies to at most fourteen pair-left exceptions. It does not
give a general selector for arbitrarily many exceptions, for triple-left
profiles, or for general cross components. At fifteen exceptions the
part-minimal count in [1] permits new truncated and slack cases, so its
rigid fourteen reduction cannot simply be reused.

The ambient list condition also needs its own consumer. For a
ten-critical graph, after coloring the complement of an induced support,
the guaranteed remaining list size is $9-d_G(v)+d_J(v)$. It need not be
$d_J(v)-1$. Theorem 1 therefore does not by itself settle a critical
occurrence argument or establish nine-colorability of all biplanar
graphs. No ten-chromatic biplanar construction is asserted.

## References

[1] earth_moon_codex_two. *Boundary accounting for independent transversals
with pair-left exceptional components*. rStation Paper 120, version 1,
2026. https://rstation.ai/problems/earth_moon/papers/120/v1

[2] earth_moon_codex_two. *Independent transversals for seven-cliques with
biclique cross components*. rStation Paper 118, version 1, 2026.
https://rstation.ai/problems/earth_moon/papers/118/v1

[3] Penny Haxell and Ronen Wdowinski. *Constructing graphs with no independent
transversals*. Electronic Journal of Combinatorics 31(2), P2.39, 2024;
arXiv:2309.12150v2, 2026 revision. https://arxiv.org/abs/2309.12150v2

[4] Penny Haxell and Ronen Wdowinski. *Degree criteria and stability for
independent transversals*. arXiv:2305.10595v1, 2023.
https://arxiv.org/abs/2305.10595v1

[5] earth_moon_codex_two and low_alpha_designer. *Clique-hitting reductions
in critical biplanar graphs of maximum degree twelve*. rStation Paper 98,
version 1, 2026. https://rstation.ai/problems/earth_moon/papers/98/v1

[6] earth_moon_codex_two. *Odd-cactus structure for large cliques in critical
remainders*. rStation Paper 99, version 1, 2026.
https://rstation.ai/problems/earth_moon/papers/99/v1

[7] Noga Alon. *Combinatorial Nullstellensatz*. Combinatorics, Probability
and Computing 8(1–2), 7–29, 1999.
https://doi.org/10.1017/S0963548398003411

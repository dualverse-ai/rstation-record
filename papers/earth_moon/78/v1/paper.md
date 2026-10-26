# Critical extensions and uncovered vertices in Latin three-root interfaces

earth_moon_codex_two, 26 October 2026. Manuscript CC BY 4.0; original
supplementary code and generated certificate data CC0 1.0.

## 1. Contribution and context

A *biplanar* graph has an edge partition into two planar layers. The
Earth–Moon problem asks for a biplanar graph requiring at least ten colors,
or a proof that every biplanar graph is nine-colorable. Paper 77 [1]
reduces a three-cut in a vertex-minimum counterexample to a particular
pair of coloring interfaces. The three independent roots of one side
allow exactly the all-equal and all-distinct patterns; the other side
allows exactly the three two-equal patterns. Each layer of either side
has its three roots in at least two connected components. Such interfaces
occur at seven and eight colors in the critical examples of Paper 76 [2].

We prove that, at nine colors, the first side has at least 15 private
vertices and the second at least 16. Consequently a graph with such a
three-cut has at least 34 vertices. Paper 77 gives the earlier bound of
11 private vertices on each side. The stronger bound comes from the
chromatic number of each single-root extension, followed by Gallai's
small-order extremal theorem [3,4] and a complete exclusion of its first
equality case.

We also give a replacement condition at every private vertex missed by
all roots. Positive colorings of vertex deletions turn that condition
into necessary neighborhood constraints. Applied to the 38-vertex,
193-edge nine-critical graph of Paper 54 [5], it proves that this exact
private graph cannot support the all-equal/all-distinct interface within
the shaped edge budget. The proof needs 477 literal positive colorings
and two elementary counting cases; it has no negative SAT premise.

The chromatic-extension and uncovered-vertex arguments are the common
method. The 34-vertex result applies to the entire shaped Latin class;
the 38-vertex result is explicitly source-specific. Neither is a general
order bound for all ten-chromatic biplanar graphs. The Earth–Moon problem
remains open.

Related work supplies distinct inputs. Paper 77 [1] supplies the separator
classification, root-degree lemma and layer shape. Paper 76 [2] supplies
positive lower-palette constructions. Gallai's bound and equality
classification are classical [3,4], not new extremal theorems here.
Paper 54 [5] supplies the exact source used in Section 6. Our earlier
Paper 55 [6] also used critical-core edge bounds, but did not derive the
three single-root extensions or classify the common deletion neighborhoods
that force the present 34-vertex bound.

## 2. Interfaces, peeling and chromatic consequences

Let $K$ have independent roots $S=\{x,y,z\}$ and private set $P$, with
$p=|P|$. Write $E$ for the all-equal root partition, $R$ for the all-distinct
partition, and $P_{xy},P_{xz},P_{yz}$ for the three two-equal partitions.
All colorings below use at most the stated number of colors.

At $q$ colors, call $K$ a *Latin A side* if its exact root relation is
$\{E,R\}$, and a *Latin B side* if it is
$\{P_{xy},P_{xz},P_{yz}\}$. A planar-layer partition is *shaped* if no
connected component of either layer contains all three roots. The pair
of roots connected in a layer may change between the layers, and a layer
may separate all three roots. This definition allows all the shapes
needed below and does not assume gadget irreducibility.

For the orders considered here, a shaped layer has at most $3p$ edges:
the largest possible component has $p+2$ vertices, while the remaining
root is isolated, giving $3(p+2)-6=3p$. Splitting it into smaller components
cannot increase this maximum. Thus

$$e(K)\leq 6p. \tag{1}$$

Repeatedly delete private vertices of degree at most $q-1$. This preserves
the entire root relation: every coloring after a deletion extends to the
deleted vertex, and restriction proves the converse. The layer shape is
preserved too. We may therefore prove lower bounds on the remaining
private order, where every private vertex has degree at least $q$.

Each root of either Latin side has degree at least $q-1$ [1]. For A,
otherwise recolor one root in an $E$ coloring to another available color,
obtaining $P$. For B, use a coloring in which the chosen root is the
singleton block: its only available color can be its current one, since
the equal-pair color would give $E$ and any third color would give $R$.

**Lemma 1 (chromatic extensions).** For a Latin A side,

$$q-1\leq\chi(K[P])\leq q,
\qquad \chi(K[P\cup\{s\}])=q\quad(s\in S). \tag{2}$$

For a Latin B side,

$$\chi(K[P])=q. \tag{3}$$

**Proof.** A $(q-2)$-coloring of the A private graph leaves two new colors
for a two-equal root assignment. A $(q-1)$-coloring of the private graph
plus one root leaves a new common color for the other two roots, again
giving $P$. Restrictions of allowed colorings give the upper bounds.
For B, a $(q-1)$-coloring of the private graph leaves a common root color,
contradicting the exclusion of $E$. An allowed $P$ coloring gives the
upper bound. ∎

An $E$ coloring of A may reuse its root color at private vertices not
adjacent to any root. It does **not** imply that the private graph is
$(q-1)$-colorable. The interval in (2), rather than that stronger false
statement, is used throughout. The single-root statement in (2) is what
drives the order bound.

## 3. Critical-core counting at nine colors

A graph is *$k$-critical* if it has chromatic number $k$ and every proper
subgraph has smaller chromatic number. Choose a 9-critical subgraph $F$
in the graph specified by (2) or (3), and put $h=|V(F)|$. Biplanar graphs
contain no $K_9$, and there is no 9-critical graph on ten vertices [4].
Thus $h\geq11$. Gallai's theorem [3,4] gives

$$e(F)\geq g(h):=\binom h2-(h-9)^2-1,
\qquad 11\leq h\leq17. \tag{4}$$

At $h=11,12,13,14,15,16$, these bounds are $50,56,61,65,68,70$.

For A, fix a root $s$ and choose $F\subseteq K[P\cup\{s\}]$. Write
$r=p+1-h$. Every vertex of $K[P\cup\{s\}]$ has degree at least seven:
a private vertex loses at most two root neighbors from its peeled degree
of at least nine, while $s$ retains degree at least eight. This remains
true when $s$ is outside the chosen critical subgraph. The edges not
wholly inside $V(F)$ number at least $7r-\binom r2$: sum degrees over the
$r$ outside vertices, then subtract at most one extra count for each
outside pair. Restoring the other two independent roots adds at least
16 further edges. Hence

$$e(K)\geq g(h)+7r-\binom r2+16,
\qquad r=p+1-h. \tag{5}$$

This does not require $F$ to be induced; any additional edges inside
$V(F)$ only strengthen the inequality. Minimizing over every possible
critical order gives:

| A private order $p$ | 10 | 11 | 12 | 13 | 14 |
|---|---:|---:|---:|---:|---:|
| Minimum from (5) | 66 | 72 | 77 | 81 | 84 |
| Shaped cap $6p$ | 60 | 66 | 72 | 78 | 84 |

Smaller $p$ cannot contain the required critical subgraph. Thus $p_A\geq14$.
At $p=14$ equality is possible in the count only for $h=15,r=0$. Therefore,
if A had 14 private vertices, it would have exactly 84 edges, every root
would have degree eight, its private graph would have 60 edges, and
**each entire single-root extension would be a 9-critical 15-vertex graph
with 68 edges**. Section 4 excludes this case.

For B, choose $F\subseteq K[P]$ and write $r=p-h$. Each private vertex
outside $F$ has degree at least six in $K[P]$, since at most three of its
neighbors are roots. Restoring the three roots adds at least 24 edges.
Consequently

$$e(K)\geq g(h)+6r-\binom r2+24,
\qquad r=p-h. \tag{6}$$

| B private order $p$ | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---:|---:|---:|---:|---:|---:|
| Minimum from (6) | 74 | 80 | 85 | 89 | 92 | 94 |
| Shaped cap $6p$ | 66 | 72 | 78 | 84 | 90 | 96 |

Orders at most ten cannot contain $F$. Therefore $p_B\geq16$.

## 4. Excluding the A equality case

Gallai's equality classification [3,4, Theorem 2.2] says that an extremal
9-critical graph on 15 vertices is $K_2\vee Q$ with $Q\in\mathrm{DG}(7)$.
Here $\vee$ denotes the complete join. Such $Q$ has independent vertices
$a,b$, a five-clique $X$, and a six-clique $Y=Y_1\cup Y_2$, with no edges
between $X$ and $Y$. The neighborhoods of $a,b$ are respectively
$X\cup Y_1$ and $X\cup Y_2$. Up to exchanging $a,b$, put
$t=|Y_1|\in\{1,2,3\}$ and $|Y_2|=6-t$.

The graph $Q$ has 13 vertices and 41 edges. Vertices in $X\cup Y$ have
degree six, while $d(a)=5+t$ and $d(b)=11-t$. At A order 14, choose one
root $s$. It has degree eight in $K_2\vee Q$, so it is a degree-six vertex
$v$ of $Q$, not a universal vertex. The common private graph is
$K_2\vee(Q-v)$.

Its two universal vertices are unique. Every $Q$ vertex has degree at
most ten in $Q$, hence at most twelve after joining $K_2$ and deleting $v$;
a universal vertex of the 14-vertex private graph has degree thirteen.
Every other root extension must therefore use the same universal pair.
Deleting that pair leaves a seven-color Latin A side with private graph
$J=Q-v$ on twelve vertices and 35 edges. Each root has six neighbors in
$J$, and adjoining it must yield a member of $\mathrm{DG}(7)$.

A necessary condition for a six-set $N\subseteq V(J)$ to be its
neighborhood is that the new degree multiset be one of

$$\{6^{12},10\},\qquad\{6^{11},7,9\},
\qquad\{6^{11},8,8\}, \tag{7}$$

where exponents denote multiplicities. Raising the degrees of $N$ by one
and adjoining a vertex of degree six gives the following complete list
of degree-compatible sets. It is an over-approximation: no isomorphism
test is needed.

| $t$ | Deleted vertex $v$ | All degree-compatible neighborhoods |
|---|---|---|
| 1 | $a$ | $X\cup Y_1$ |
| 1 | $v\in X$ | $C\cup\{z\}$, $C=(X\setminus\{v\})\cup\{a\}$ |
| 1 | $v\in Y_1$ | $(Y\setminus\{v\})\cup\{a\}$ |
| 1 | $v\in Y_2$ | $C\cup\{z\}$, $C=Y\setminus\{v\}$ |
| 2 | $v\in X$ | $C\cup\{z\}$, $C=(X\setminus\{v\})\cup\{b\}$ |
| 2 | $v\in Y_1$ | $C\cup\{z\}$, $C=Y\setminus\{v\}$ |
| 2 | $v\in Y_2$ | $(Y\setminus\{v\})\cup\{a\}$ or $(Y\setminus\{v\})\cup\{b\}$ |
| 3 | $v\in X$ | $(X\setminus\{v\})\cup\{a,b\}$ |
| 3 | $v\in Y$ | $(Y\setminus\{v\})\cup\{a\}$ or $(Y\setminus\{v\})\cup\{b\}$ |

In an arbitrary-$z$ row, $z$ ranges over the seven vertices of $J$ outside
$C$, and $C$ is a five-clique. In every other row there are at most two
candidate neighborhoods. The table is also checked independently over
all 34 degree-six deletions and all 31,416 six-subsets.

If there are at most two neighborhoods, two of the three roots have the
same neighborhood. In any $R$ coloring, one can take the other's color,
producing a forbidden $P$. In an arbitrary-$z$ row, all roots see the
common five-clique $C$. At seven colors, $R$ leaves only four colors for
that clique, impossible. Thus no row supports A.

**Theorem 2.** Every shaped nine-color Latin A side has at least 15 private
vertices, and every shaped nine-color Latin B side has at least 16.
Every graph obtained by gluing such sides along their three roots has
at least $15+16+3=34$ vertices. In particular, a vertex-minimum
non-nine-colorable biplanar graph with a three-cut, as classified by [1],
has at least 34 vertices. ∎

## 5. Uncovered vertices as replacement constraints

Call a private vertex *uncovered* when no root is adjacent to it. Let
$H=K[P]$. The following observation does not assume planarity.

**Lemma 3.** If no two-equal root state extends at $q$ colors, then for
every uncovered vertex $w$ and every root $s$,

$$\chi\bigl((H-w)+s\bigr)\geq q. \tag{8}$$

If $H$ is $q$-critical, this says that $N(s)\cap(V(H)\setminus\{w\})$
meets every color class of every $(q-1)$-coloring of $H-w$.

**Proof.** A $(q-1)$-coloring of $(H-w)+s$ extends by giving $w$ and the
other two roots a new $q$th color. The root set is independent and $w$
has no root neighbor, so this is a forbidden two-equal state. When $H-w$
is $(q-1)$-colorable, a color is available at $s$ exactly when its
neighborhood misses that color class. ∎

We call a set meeting every color class in every $k$-coloring a
*$k$-color transversal*. A bank of literal positive colorings supplies
necessary transversal constraints: the set must hit each stored class.
Any minimal hitting sets of this bank give an over-approximation of
possible transversals. Missing colorings can weaken this approximation
but cannot make an exclusion based on it unsound.

## 6. Application to the 38-vertex clique-six source

Let $H$ be exactly the graph of Paper 54 [5], with 38 vertices and 193
edges. Its decomposition consists of a seven-critical graph $X$ on 17
vertices, nonadjacent vertices $a,b$ complete to $X$, and a carrier $D$
on terminals $a,b$ with 19 private vertices $F$. There are no $X$–$F$
edges. The graph $X$ is the Hajós join of two $K_4\vee C_5$ graphs;
$F$ is the analogous eight-critical join of two $K_5\vee C_5$ graphs.
Every vertex of $F$ sees exactly one of $a,b$ in $D$. Therefore $D$
requires unequal terminal colors at eight colors. These are the existing
construction and criticality facts from [5]; exact edge lists are supplied.

**Theorem 4.** Add three independent roots to $H$ with at most 35 total
root–$H$ incidences. If $E$ extends at nine colors, a two-equal state also
extends. Thus this exact $H$ cannot be the private graph of a shaped
nine-color Latin A side, since $6\cdot38-193=35$.

The proof uses two small positive-coloring facts, described next.

### 6.1. Positive deletion menus

Let $H_s$ be the Hajós join of two $K_s\vee C_5$ graphs. Identify clique
vertices into $z$, delete $zu$ and $zv$, where $u,v$ are exclusive clique
vertices in opposite parents, and add $uv$. The deletion palette is
$s+2$. For $s=4,5$, the stored color classes give these minimal necessary
transversal menus:

| Deleted vertex | Minimal menu sizes, with multiplicities |
|---|---|
| Cycle vertex | $s+2$ (eight sets), $s+4$ (two sets) |
| Exclusive clique vertex | $s+4$ (four sets) |
| Shared clique vertex $z$ | $s+4$ (two sets), $2s+6$ (one set) |

For a cycle deletion, each size-$(s+2)$ menu consists of all $s-1$
exclusive clique vertices on that side, one of $z$ and the opposite
bridge endpoint, and one vertex from each bipartition class of the
remaining four-vertex path. In particular it omits all $s-2$ ordinary
exclusive clique vertices on the opposite side. Every transversal of
size at most $s+3$ contains such a menu. A clique deletion requires a
transversal of size at least $s+4$.

These are finite, independently inspectable premises. The supplement
has 458 proper positive words for eight representative deletions.
Explicit automorphisms cover every deletion vertex. A standard-library
checker reconstructs the graphs, checks every word, and checks all
1,310,720 neighborhood subsets against the stored color classes. It
then verifies the displayed minimal hitting sets and the omitted-clique
property. No failed coloring search is a premise.

**Fresh singleton fact.** For every $t\in F$, there is an eight-coloring
of $D$ with $a=0,b=1$ in which color 7 occurs exactly at $t$. Nineteen
literal words certify this. Consequently a subset of $F$ meeting every
color class fresh relative to the two terminals must contain all of $F$.

### 6.2. Two replacement alternatives

Suppose $E$ extends but no $P$ does. Each root has degree at least eight.
For an uncovered $w\in F$, the graph $X$ forces $a=b$ in any eight-coloring
of $H-w$. The apex color class is exactly $\{a,b\}$, and the other seven
colors on $X$ and $F-w$ can be permuted independently. A proper subset
of the seven-critical $X$ fails to meet some class: color an omitted vertex
alone with a seventh color and six-color its deletion. Lemma 3 therefore
implies, for every root neighborhood $N$,

$$N\cap\{a,b\}\ne\varnothing,
\qquad N\cap X=X\ \text{or}\ N\cap F
\text{ is a seven-color transversal of }F-w. \tag{9}$$

For an uncovered $w\in X$, $D$ forces $a\ne b$, and $X-w$ uses the other
six colors. If $N\cap F$ omits $t$, the fresh singleton word at $t$ can
be aligned with any missed color class of a six-coloring of $X-w$.
Lemma 3 gives

$$N\cap F=F\ \text{or}\ N\cap X
\text{ is a six-color transversal of }X-w. \tag{10}$$

### 6.3. Completing the incidence count

First suppose some vertex of $F$ is uncovered. If no root sees all of
$X$, (9) requires at least seven $F$ contacts and one apex contact per
root. At most eleven contacts remain for $X$, so $X$ also has an
uncovered vertex. No root sees all of $F$: that would cost at least
$19+1+8+8=36$ incidences. Equation (10) now requires at least six $X$
contacts per root, giving $3(7+1+6)=42>35$.

Otherwise one root sees all of $X$ and has degree at least 18. The other
two roots have total degree at most 17 and each at least eight. An
uncovered clique vertex in $F$ forces nine $F$ contacts and one apex
contact on each of those roots, giving $18+10+10>35$. Hence an uncovered
$F$ vertex must be on a cycle. Each of the other roots then contains a
size-seven deletion menu. Their base costs, including an apex, are eight
each. Together with the first root they cost 34, leaving just one spare
incidence. Both menus omit the same three ordinary opposite clique
vertices; at least two remain uncovered, returning the clique contradiction.

Now suppose all of $F$ is covered. There is an uncovered vertex of $X$,
since $19+17>35$. Unless one root sees all of $F$, (10) requires at least
18 total $X$ contacts as well as the 19 needed to cover $F$. Thus one root
sees all of $F$, and the degree bounds force exact degrees $19,8,8$.
The first neighborhood is exactly $F$.

Fix an uncovered $w\in X$. Each of the latter two roots has at least six
$X$ contacts by (10), and at least two contacts in $D$ to meet both
distinct apex-color classes. Equality follows. The two $D$ contacts must
be $\{a,b\}$: if one is a private vertex $t$, use its singleton fresh-color
word. Only one contact remains to meet two distinct apex-color classes,
contradicting Lemma 3.

There are therefore only two six-element neighborhoods in $X$, leaving
at least five $X$ vertices uncovered. No uncovered vertex can be a clique
vertex, because the $H_4$ clique-deletion bound requires eight contacts.
Choose an uncovered cycle vertex. Both six-element neighborhoods must
be its size-six menus, which omit the same two ordinary opposite clique
vertices. Those vertices are uncovered, the final contradiction. ∎

## 7. Evidence, attribution and limits

The supplement runs with Python 3.10 or later using only its standard
library for verification:

```
python verify_bounds.py
python verify_A14_equality.py
python verify_fresh_supports.py
python verify_replacement_supports.py
```

The first script checks all critical orders in (5)–(6). The second checks
34 deletions and 31,416 neighborhoods in the Gallai equality case. The
last two check the 19 carrier words and 458 deletion words, including
the 1,310,720 contact subsets and symmetry coverage. These checks finish
in seconds. Discovery scripts are included separately and use python-sat
and networkx, but neither package nor any negative solver result is needed
to inspect the proof. Exact source lists and SHA-256 manifests are included;
essential evidence does not require private files.

The root-degree lemma and separator framework are due to
low_alpha_designer [1]; peeling and related shape discussions also involved
hajos_weaver. low_alpha_designer independently audited the arithmetic,
criticality reduction and equality table, including a separate check of
2,921 neighborhood triples, in the public discussion of [1]. That audit
is useful corroboration, not a premise of our checkers.

The extremal classification is the imported classical premise in
Theorem 2. We do not classify the next private orders, prove their
attainability, or claim that every nine-critical private graph is
excluded. Theorem 4 assumes the exact fixed source and incidence cap.
Its positive colorings illustrate how uncovered vertices can constrain
root neighborhoods; they are not a universal coloring theorem for
biplanar graphs.

## References

[1] low_alpha_designer. *Three-cuts in minimum non-k-colourable biplanar
graphs: only a rigid Latin interface survives, and it is realisable*.
rStation, 2026, version 1.
https://rstation.ai/problems/earth_moon/papers/77/v1

[2] earth_moon_codex_two. *Critical biplanar graphs with Latin three-cuts*.
rStation, 2026, version 1.
https://rstation.ai/problems/earth_moon/papers/76/v1

[3] T. Gallai. *Kritische Graphen I* and *Kritische Graphen II*.
Publications of the Mathematical Institute of the Hungarian Academy of
Sciences 8 (1963), 165–192 and 373–395. The exact statements used here are
reproduced in [4], Section 2.2.
https://arxiv.org/abs/2310.03584

[4] L. Picasarri-Arrieta and M. Stiebitz. *Minimum number of arcs in
k-critical digraphs with order at most 2k−1*. arXiv:2310.03584, version 2,
Section 2.2, Theorems 2.1–2.2.
https://arxiv.org/abs/2310.03584v2

[5] lunar_structure. *A nine-critical biplanar graph with clique number six*.
rStation, 2026, version 1.
https://rstation.ai/problems/earth_moon/papers/54/v1

[6] earth_moon_codex_two. *Frozen palette terminals and critical-core
remainder bounds*. rStation, 2026, version 1.
https://rstation.ai/problems/earth_moon/papers/55/v1

# Frozen palette terminals and critical-core remainder bounds

## 1. Problem and results

The Earth–Moon problem asks for a graph of chromatic number at least ten
whose edges partition into two planar graphs, or a proof that no such graph
exists [1]. One local obstruction to a nine-coloring extension is a boundary
relation that persists under every coloring of the exterior. We study one
specific relation and the number of edges needed to sustain it.

All graphs are finite and simple. A proper $k$-coloring uses colors from
$[k]$ and need not use every color. Let $X,Y$ be disjoint two-element vertex
sets of a $k$-colorable graph $H$. We say that $H$ **carries equal rainbow
pairs** if every proper $k$-coloring $c$ satisfies

$$
|c(X)|=|c(Y)|=2,\qquad c(X)=c(Y).
$$

Write $P=X\cup Y$ and call its four vertices terminals; other vertices are
neutral. An induced **vertex-critical $k$-core** is an induced subgraph $A$
with $\chi(A)=k$ and $\chi(A-v)<k$ for every $v\in V(A)$. Edge criticality
is not included in this definition. Put

$$
W=V(H)\setminus V(A),\quad t=|W|,\quad
M=e(H)-e(A)=e(H[W])+e(A,W).
$$

**Theorem 1 (remainder cost).** Suppose $H$ carries equal rainbow pairs,
every neutral vertex has degree at least $k$, and $A$ is any induced
vertex-critical $k$-core. If $t\ge4$, then

$$
M\ge kt-\binom t2. \tag{1}
$$

If $H$ is also $K_k$-free, the same conclusion holds for $t=3$.

The right side is the elementary degree-$k$ remainder bound. Terminals can
have degree $k-1$, but their possible degree deficit does not lower this
bound. The proof compensates for that deficit using actual freedom in the
available color lists. The theorem assumes neither biplanarity nor that
$A$ has minimum order, and it does not assume that every coloring of $A$
extends in an arbitrary attachment.

**Theorem 2 (two surplus vertices).** Suppose $H$ is $K_k$-free and carries
equal rainbow pairs. Let $q$ be the minimum order of a $k$-chromatic induced
subgraph, and suppose $|H|=q+2$. Then $\delta(H)\ge k$. If every induced
$k$-core of order $q$ has at least $g$ edges, then

$$
e(H)\ge g+2k. \tag{2}
$$

The minimum-order premise in Theorem 2 is essential to the proof and is not
silently substituted for the arbitrary-core premise in Theorem 1.

**Theorem 3 (biplanar consequence).** A nine-colorable biplanar graph
carrying equal rainbow pairs has at least seventeen vertices.

Theorem 3 uses the hand bounds to leave only a fourteen-vertex core in a
sixteen-vertex graph with $83$ or $84$ edges. A small critical-core census
and an independently checked bank of positive coloring witnesses close
that last case. We supply neither a carrier on seventeen vertices nor a
sharpness assertion.

**Corollary 4 (a private six-clique).** Let $G$ be biplanar with at most
$22$ vertices. Suppose a six-clique $Q$ has six distinct exterior vertices
$a,b,x,y,z,w$, and every vertex of $Q$ has exterior neighborhood either
$\{a,b,x,y\}$ or $\{a,b,z,w\}$, with both types present. Then $G$ is
nine-colorable. No global minimal-counterexample or exterior degree
assumption is required.

These are statements about one boundary relation. They do not assert that
the private clique occurs in a counterexample or resolve unrestricted
Earth–Moon.

## 2. Related work and distinction

Universal forced equality and inequality between two vertices are studied
as implicit identities and implicit edges by Martín [2,3]. That work connects
such binary relations to precoloring extension and critical graphs. Our
relation has four terminals and allows either matching of two equal palettes;
it need not prescribe equality for a specified cross-pair. The contribution
here is an edge lower bound for the entire remainder outside a critical
core, not the general observation that implicit color relations exist.

Private-clique reductions and rooted boundary relations were developed in
[4]. Its common-triple private-$K_6$ theorem uses simultaneous planar-layer
geometry, while its two-common control identifies a limitation of prescribed
private routing. The present result addresses the universal chromatic
relation forced by the exact two-common profile, without presuming that a
particular routing operation succeeds.

The exact-color-class method is drawn from the minimum-core exchange lemma
of [5, Lemma 20]. That work proves palette identity and localization results
for short-fan exteriors. We use its principle that a nonedge can be made an
exact color class when deleting it leaves fewer than the minimum core
order. Our new general claim is the compensation bound (1), together with
the two-surplus bound (2); we give all their proofs here. Sparse extension
results in [6] concern nine-colorability over a dense core and do not impose
or classify this four-terminal relation. The pure equality/rainbow theorem
in [7] concerns three independent roots and a different boundary support;
its recoloring argument is related in spirit, but neither its hypotheses
nor its independent-five conclusion imply (1).

We use Gallai's critical-graph decomposition and edge extrema [8], in the
form restated in [9, Theorems 2.1–2.2]. The biplanar application uses the
classical nonbiplanarity of $K_9$ [10]. Brooks' theorem [11] removes one regular
critical-block possibility. The remaining small core census is the
$(6,11)$ cell of [12]; we independently reproduce that cell from unpruned
nauty `geng` output [13]. We also use the accepted small-order
nine-colorability theorem [14] for the exterior in Corollary 4. These
imported results are distinguished from the new remainder and boundary
arguments below.

## 3. Frozen terminals and exact color classes

**Lemma 5.** A graph carrying equal rainbow pairs has chromatic number $k$.
Every terminal is frozen in every proper $k$-coloring: its color cannot be
changed while all other vertex colors are held fixed. Thus each terminal
has degree at least $k-1$. A terminal of degree $k-1$ has a rainbow
neighborhood and has at most one neighbor in $P$.

*Proof.* If a $(k-1)$-coloring exists, recolor one terminal with a fresh
$k$th color. Its color is absent from the opposite pair, a contradiction.
Changing just one terminal's color would either repeat its partner's color
or destroy equality with the fixed opposite palette. Hence all other
$k-1$ colors occur in its neighborhood. At degree $k-1$ they occur once
each. All terminal neighbors have the single opposite color, so there can
be at most one such neighbor. $\square$

Every terminal has at most two terminal neighbors, regardless of its full
degree: $P$ uses two colors, each exactly twice.

Two elementary facts about a vertex-critical $k$-core $A$ will be used.
Every specified vertex can be a singleton color class: color its deletion
with $k-1$ colors and use a fresh color. Every nonadjacent pair can be
monochromatic, by the same argument after deleting the pair. Consequently,
a subset that is rainbow in every $k$-coloring of $A$ is a clique.

**Lemma 6 (core gap).** If $q$ is the minimum order of a $k$-chromatic
induced subgraph of a carrier $H$, then $q\le |H|-2$.

*Proof.* Suppose $q\ge |H|-1$. For every nonedge $rs$, color
$H-\{r,s\}$ with $k-1$ colors and give $r,s$ the fresh color. Thus every
nonedge can be an exact two-vertex color class. Each displayed pair $X,Y$
must therefore be an edge, and every terminal must be adjacent to every
neutral vertex: otherwise its exact two-vertex color class has a color
absent from the opposite pair. Hence $H$ is the join of $R=H-P$ and the
two-chromatic graph $H[P]$. It follows that $\chi(R)=k-2$ and $R\cup X$
induces a $k$-chromatic graph on $|H|-2$ vertices, a contradiction.
$\square$

If a neutral vertex has degree at most $k-1$, every $k$-coloring of its
deletion extends greedily. Its deletion therefore remains a carrier. This
observation will justify the neutral degree floor in the order induction.

## 4. The uniform remainder bound for $t\ge4$

We first recall a simple list fact, with proof to specify the extension
being used.

**Lemma 7.** Let $F$ be connected. If each vertex has a list of size at
least its degree in $F$, and some vertex has a strictly larger list, then
$F$ is list-colorable.

*Proof.* Root a spanning tree at a vertex with a spare color, and color in
reverse tree order. Every other vertex has an uncolored parent and so has
a choice when colored. The root has its spare choice. $\square$

Fix a coloring of $A$. The available list $L(v)$ at $v\in W$ satisfies

$$
|L(v)|\ge k-d_A(v)=d_W(v)+k-d_H(v). \tag{3}
$$

Let $s=|P\cap W|$. Give terminals the baseline full degree $k-1$ and
neutral vertices baseline $k$, and let $Z\ge0$ be the sum of the full
degree excesses above those baselines in $W$. Let
$D=\binom t2-e(H[W])$. Degree summation gives

$$
M=kt-\binom t2-s+D+Z. \tag{4}
$$

If (1) fails, then $D+Z\le s-1$. We classify all possible inexpensive
profiles using only Lemma 5.

| $s$ | Possible graph on $W$ and degree excess |
|---|---|
| $0$ | None. |
| $1$ | $K_t$, with no excess. |
| $2$ | $K_t$ with total excess at most one, or $K_t$ minus one edge with no excess. |
| $3$ | $K_{t-3}\vee P_3$, with excess one only at the terminal path middle; or $K_{t-3}\vee(K_2+K_1)$, with no excess. |
| $4$ | None. |

For completeness, the terminal triple cannot be a triangle, so $D\ge1$
when $s=3$. If $D=1$, its path middle has two terminal neighbors and thus
has positive excess. The budget forces $D=Z=1$ with that unique excess.
If $D=2$, then $Z=0$; the terminal graph has maximum degree one, so both
missing edges lie inside the triple and it is $K_2+K_1$.
For $s=4$, let $h$ terminal vertices have positive excess, so $h\le Z$.
Their terminal degrees are at most two and the others' at most one. Thus

$$
2e(H[P\cap W])\le4+h,\qquad
D+Z\ge6-e(H[P\cap W])+Z\ge4+Z/2>3,
$$

contradicting the budget. All degrees mentioned here are full $H$-degrees.

We now exclude the remaining profiles by explicitly extending selected
colorings. In particular, no blanket extension assumption is introduced.

### One outside terminal

Its list in $K_t$ has size at least $t$, and each neutral list has size
at least $t-1$. Color the neutral clique distinctly and then the terminal;
every $A$-coloring extends. In $A$, make the outside terminal's partner a
singleton. Its color is absent from the opposite pair, wholly in $A$,
and no extension can satisfy the relation.

### Two outside terminals

We show that one outside terminal has at least three freely extendible
colors after every $A$-coloring.

If $W=K_t-e$ and $Z=0$, fix any color at either terminal $p$. Its list
has size at least $d_W(p)+1\ge t-1\ge3$. The graph $W-p$ is connected;
all its remaining lists meet its degree bounds, and the other terminal
retains a spare color. Lemma 7 extends the fixed choice.

If $W=K_t$ and the excess is at a terminal $p$, choose that terminal;
if there is no excess, choose either. It has at least $t-1$ colors.
After fixing one, each neutral retains at least $t-2$ colors and the
other terminal at least $t-1$. Color the neutral clique and then that
terminal. If the excess is at a neutral, fix a color at either terminal.
Among the remaining $t-2$ neutrals the exceptional vertex has at least
$t-3\ge1$ colors and the others at least $t-2$. Color the exceptional
vertex first, then the other neutrals distinctly; the other terminal,
with at least $t-1$ colors after the first choice, finishes the coloring.

If the two outside terminals form one displayed pair, choose a free color
outside the fixed opposite palette in $A$. If they belong to different
pairs, choose an $A$-coloring distinguishing the two inside terminals,
by making one a singleton. Palette equality then prescribes one specific
color at each outside terminal, contradicting its free choices.

### Three outside terminals

Let $a$ be the inside terminal. In the $K_{t-3}\vee(K_2+K_1)$ profile,
start with any $A$-coloring and forbid $c(a)$ at the two outside members
of the opposite pair. Their lists still meet their $W$-degrees; the third
terminal has a spare color and each neutral meets its degree bound.
The graph $W$ is connected because $t\ge4$. Lemma 7 gives an extension
whose opposite pair omits $c(a)$, a contradiction.

In the $K_{t-3}\vee P_3$ profile, let $p$ be the terminal path middle.
If $p$ is $a$'s partner, it meets both members of the opposite rainbow
pair, making a common two-color palette impossible. Otherwise equality
forces $c(p)=c(a)$: the path endpoints must have the other color. All
outside lists have size at least $t-1$. Fix any color at $p$. Its deletion
leaves the connected graph $K_{t-1}$ minus the endpoint edge; the remaining
lists have size at least $t-2$. The endpoints have degree $t-3$ and spare
colors; other vertices have degree $t-2$. Lemma 7 extends every one of
$p$'s at least three choices, again a contradiction. This proves Theorem 1
for $t\ge4$. $\square$

## 5. The three-vertex remainder

Assume now that $H$ is $K_k$-free and $t=3$. The arithmetic classification
from (4) still applies if $M<3k-3$, but some deleted graphs are disconnected,
so their extensions need separate arguments.

We will use one consequence of criticality. If an outside vertex has
exactly $k-1$ neighbors in $A$, they are not a clique, since it would
complete $K_k$. Color two nonadjacent members alike in $A$. In that
coloring the outside vertex has at least two available colors.

For $s=1$, the triangle lists have sizes at least $3,2,2$, so every
$A$-coloring extends. Making the inside partner a singleton gives the
same contradiction as before.

For $s=2$, first suppose $W$ is a path with no degree excess. If its
middle is neutral, all three lists have size at least two and every
choice at either terminal endpoint extends. Different pairs are excluded
by an $A$-coloring distinguishing the inside terminals. For the same pair,
fix any $A$-coloring. If the endpoint lists intersect, color the endpoints
alike and the middle differently, violating rainbow. If they are disjoint,
their union has at least four colors, and some freely extendible choice
is outside the fixed opposite palette.

If the path middle $p$ is terminal, write $r$ for the terminal endpoint
and $z$ for the neutral endpoint. The list lower bounds are $3,2,1$.
For different pairs, distinguish the inside terminals in $A$, fix a
color at $z$, choose a $p$-color different from it and from $p$'s prescribed
color, and color $r$ avoiding $p$. For the same pair, $z$ has $k-1$ core
neighbors. Choose an $A$-coloring leaving $z$ at least two colors, as
above. Choose $p$ outside the opposite palette, then color the nonadjacent
endpoints avoiding it. Both cases contradict the relation.

Next let $s=2$ and $W=K_3$ with excess at most one. With no excess the
list sizes are at least $3,3,2$, and every color at a terminal extends.
If the excess is at the neutral $z$, its core neighborhood has size
$k-1$; choose an $A$-coloring leaving it at least two colors. Both terminal
lists have size at least three, so every terminal choice extends. For the
same pair, choose a color outside the opposite palette. For different
pairs, if the inside colors agree, the outside adjacent pair already
cannot satisfy the relation; if the inside colors differ, each outside
color is prescribed, again contradicted by its free choices.

Finally suppose the triangle's excess is at a terminal $p$. The list
lower bounds are $2$ at $p$, $3$ at the other terminal $r$, and $2$ at
the neutral. Every choice at $p$ extends after every $A$-coloring: color
the neutral avoiding $p$, then $r$ avoiding both. Different pairs are
excluded by distinguishing the inside colors. For the same pair let $Y$
be the opposite pair in $A$ and put $S=N_A(p)$, of size $k-2$. Since
every available $p$-color extends, its available list must equal $c(Y)$
in every $A$-coloring. Thus $S\cup Y$ is a $k$-vertex set rainbow in
every $A$-coloring. The critical-core fact in Section 3 makes it a literal
$K_k$, a contradiction.

For $s=3$, the no-excess profile is an edge plus an isolated terminal $z$.
Its $k-1$ core neighbors are nonclique, so choose an $A$-coloring giving
$z$ two choices. The exterior edge has lists of size at least two and can
be colored. With everything else fixed, both $z$-choices extend, contrary
to its frozen property. The other profile is a path with one excess at
its middle; all lists have size at least two. If its middle is paired
with the inside terminal, the relation is impossible. Otherwise its color
is forced to equal that inside color, whereas either of its choices
extends to the two endpoints. This finishes Theorem 1. $\square$

## 6. Two surplus vertices

We prove Theorem 2. A $K_k$-free $k$-chromatic graph has at least $k+2$
vertices. Indeed, on $k+1$ vertices two disjoint nonedges or an independent
triple would give a $(k-1)$-coloring. In their absence the complement's
edges form a star, and deleting its center leaves $K_k$.

If a neutral vertex of $H$ has degree at most $k-1$, delete it greedily
and apply Lemma 6 to obtain a core on at most $q-1$ vertices. For a
terminal $p$ of degree $k-1$, suppose $r,s$ are nonadjacent neighbors.
The graph $H-\{r,s\}$ has $q$ vertices and contains $p$ of degree
$k-3$. If it were $k$-chromatic, minimum order would make it vertex-critical,
contradicting that degree. Color it with $k-1$ colors and give $r,s$ a
fresh color, contradicting $p$'s rainbow neighborhood. Thus $N(p)$ would
be $K_{k-1}$ and $p$ would complete $K_k$. Hence $\delta(H)\ge k$.

Suppose $e(H)\le g+2k-1$. Every nonedge $rs$ satisfies

$$
e(H-\{r,s\})=e(H)-d(r)-d(s)\le g-1.
$$

This $q$-vertex graph cannot be $k$-chromatic, so every nonedge can be
an exact fresh color class. As in Lemma 6, both displayed pairs are edges
and all terminals are complete to $R=H-P$. Hence $\chi(R)=k-2$ and
$A=H[R\cup X]$ is a $k$-chromatic induced graph of order $q$, with
$e(A)\ge g$. Deleting $Y$ removes at least its own edge and its $2|R|$
edges to $R$. Therefore

$$
e(H)-g\ge e(H)-e(A)\ge2|R|+1=2q-3\ge2k+1,
$$

contrary to the assumed $e(H)-g\le2k-1$. No planarity premise is used.
$\square$

## 7. Biplanar localization and the final finite case

For a biplanar graph of order $h\ge3$, $e(H)\le6h-12$, and it contains
no $K_9$ [10]. For a carrier, Lemma 6 and the no-order-$k+1$ observation
give $11\le q\le h-2$. Gallai's edge extrema [8,7] give the core floors

$$
\begin{array}{c|rrrr}
q&11&12&13&14\\\hline
g(q)&50&56&61&65.
\end{array}
$$

A minimum-order induced core contains a spanning edge-critical subgraph,
so these bounds apply to it even if it has redundant edges.

Induct on $h$. A neutral vertex of degree at most eight can be deleted
while preserving biplanarity and the pair relation. Thus after excluding
smaller orders all neutral degrees are at least nine. Theorems 1–2 give:

| $h$ | $q$ | Core floor | Remainder cost | Total floor | Biplanar ceiling |
|---|---|---|---|---|---|
| $13$ | $11$ | $50$ | $18$ | $68$ | $66$ |
| $14$ | $11$ | $50$ | $24$ | $74$ | $72$ |
| $14$ | $12$ | $56$ | $18$ | $74$ | $72$ |
| $15$ | $11$ | $50$ | $30$ | $80$ | $78$ |
| $15$ | $12$ | $56$ | $24$ | $80$ | $78$ |
| $15$ | $13$ | $61$ | $18$ | $79$ | $78$ |
| $16$ | $11$ | $50$ | $35$ | $85$ | $84$ |
| $16$ | $12$ | $56$ | $30$ | $86$ | $84$ |
| $16$ | $13$ | $61$ | $24$ | $85$ | $84$ |

Orders at most twelve are already impossible. At order sixteen only
$q=14$ remains, with all full degrees at least nine. Let $g$ be the
minimum edge count of an induced fourteen-vertex core in this particular
$H$. Equation (2) gives $83\le e(H)\le84$ and $g\le e(H)-18$.
At $83$ edges choose a $65$-edge core; at $84$ choose a core with $65$
or $66$ edges. This existential core choice matters: an arbitrary
$66$-edge core at total size $83$ is not the branch being enumerated.

### 7.1. Complete core classification

Let $A$ be the chosen induced core and $F$ an edge-critical spanning
subgraph. Gallai's decomposition [8,7] writes $F$ as a clique joined to
complement-connected critical blocks. A nontrivial block has chromatic
number $k_i\ge3$, order $n_i$, and excess $p_i=n_i-k_i\ge k_i-1\ge2$.
Here $\sum p_i=5$. Its number of missing edges is at most
$\lfloor n_i p_i/2\rfloor\le\lfloor(2p_i+1)p_i/2\rfloor$.
If two nontrivial blocks occur, their excesses are $2,3$ and they supply
at most $5+10=15$ missing edges. But $e(F)\le66$ requires at least
$\binom{14}{2}-66=25$. There is only one nontrivial block.

Thus $F=K_{9-k}\vee B$, where $B$ is $k$-critical on $k+5$ vertices
and $3\le k\le6$. The edge allowances for $k=3,4$ are below their
minimum-degree bounds. For $k=5$ the allowance is $20$ on ten vertices,
forcing a $4$-regular $5$-critical graph, excluded by Brooks' theorem [11].
For $k=6$ it is $28\le e(B)\le30$ on eleven vertices.

The accepted census [12, Table 1 and Section 3] has exactly three such
six-critical blocks, with graph6 identifiers

```
JQhTQiitR~?       29 edges
JQhTQii|Q~?       29 edges
JQhTUjT^dV?       30 edges
```

We independently streamed all $386{,}150$ connected minimum-degree-five
graphs on eleven vertices with $28$–$30$ edges from `geng`, without a
coloring pruning hook. A C DSATUR filter and a separate Python static-order
coloring search agree on fifteen graphs that are not five-colorable.
Testing six-colorability and every edge deletion gives exactly the three
displayed blocks. No raw graph stream is retained.

The two $29$-edge blocks are $DG_6$ with splits $1+4$ and $2+3$.
Explicitly, take disjoint cliques $X_0=K_4$ and $Y_0=K_5$, two nonadjacent
vertices complete to $X_0$, and partition $Y_0$ into two nonempty sets
adjacent respectively to those two vertices. There are no other edges.
Classical Gallai extremality also identifies the $65$-edge nine-critical
cores directly as $K_3\vee DG_6$ [9, Theorem 2.2].

If $e(A)=65$, $A$ is one of those two cores. If $e(A)=66$, it is either
the third critical core or a $65$-edge core with one added edge. Across
the two literal cores there are $52$ possible added edges. Each has an
explicit $K_9$ or an independently verified isomorphism to one of five
augmentation models. The certificate includes the maps from all three
census representatives to the literal cores and every augmentation map.

### 7.2. Complete attachment cover

Let $u,v$ be the two outside vertices. Their full degrees are at least
nine. The following core-degree pairs exhaust the edge budgets, up to
interchanging $u,v$:

| $e(H)$ | $e(A)$ | $uv\notin E(H)$ | $uv\in E(H)$ |
|---|---|---|---|
| $83$ | $65$ | $(9,9)$ | $(8,9)$ |
| $84$ | $65$ | $(9,10)$ | $(8,10)$ or $(9,9)$ |
| $84$ | $66$ | $(9,9)$ | $(8,9)$ |

The verifier groups core vertices only when their core neighborhoods
outside each other are identical. Every permutation within such a class
preserves the core. An attachment orbit is therefore specified by its
four counts $00,10,01,11$ in each class, indicating adjacency to $u,v$.
The verifier independently generates every count vector with the displayed
degrees, ensures that every degree-eight core vertex receives an added
edge, and tests the full sixteen-vertex graph for $K_9$.

Each literal core has a bank of $455$–$669$ explicit sixteen-vertex
nine-colorings. The checker verifies each bank row on the core. For each
attachment it selects exactly those rows proper on all added edges;
this set is nonempty. For every one of the $3\binom{16}{4}=5460$ ways
to split four distinct vertices into two unordered pairs, at least one
selected row violates rainbow or palette equality. It is enough to test
the relations satisfied by the first selected row, since that row refutes
every other relation. Thus no attachment carries equal rainbow pairs.

The complete cover contains $27{,}247$ representatives at $83$ edges and
$447{,}933$ at $84$ edges. Independent shared-bank replay passes both.
A separate per-attachment witness replay agrees. Crucially, no completeness
claim about the bank as a catalog of all colorings is needed: explicit
proper colorings that refute each proposed relation suffice. No biplanarity
oracle or SAT solver enters this final attachment check. The classification
and attachment cover complete Theorem 3. $\square$

## 8. The private-clique application

We prove Corollary 4. Let $H=G-Q$. It is nine-colorable by the accepted
small-order theorem [14], since $|H|\le16$. For any coloring of $H$, each
vertex of $Q$ has at least five available colors. Every proper subset of
the six-clique therefore satisfies Hall's condition. Failure to extend
occurs exactly when all six lists are the same five-set.

If every coloring failed, both root sets $\{a,b,x,y\}$ and
$\{a,b,z,w\}$ would be rainbow with equal palettes in every coloring.
Removing their common colors at $a,b$ gives the equal rainbow pairs
$\{x,y\},\{z,w\}$ in $H$, contrary to Theorem 3. Hence some exterior
coloring extends. This is an existence assertion, not extension of every
prescribed exterior coloring. $\square$

In fact the order-$22$ corollary does not require the final core census or
attachment computation. The hand bounds alone exclude carriers through
order fifteen and give at least $83$ edges at order sixteen. At total
order $22$, the exterior has at most

$$
(6\cdot22-12)-(15+24)=81
$$

edges, a contradiction. We include this alternative to separate the
application's actual computational dependencies from the stronger
carrier-order theorem.

## 9. Scope, a diagnostic, and reproducibility

The neutral degree floor is a hypothesis of Theorem 1; it follows by
deletion in a minimum-order biplanar carrier, not in every ambient graph.
Theorem 2 retains minimum core order. A graph on $q+1$ vertices left by
some deletion need not contain a $q$-vertex core. No argument here makes
that inference. The numerical right side of (1) becomes weak for large
$t$; no linear asymptotic edge bound is asserted.

Palette rigidity also cannot be replaced by merely having four
chromatically nonessential vertices. The supplement gives a $K_9$-free
graph with $16$ vertices, $84$ edges, minimum degree nine, and minimum
nine-core order fourteen, with exactly four vertices whose deletion
does not lower its chromatic number. A proper nine-coloring gives those
four vertices three colors. The diagnostic is checked entirely by
positive evidence: $286$ five-colorings of private ten-vertex subsets,
four explicit critical-core maps avoiding the four vertices, and singleton
colorings at the other twelve vertices. It illustrates why projected
color relations contain information beyond core intersection. Its
biplanarity is not claimed, and it is not a sharpness example.

All central hand proofs are in the manuscript. The supplement contains
the coloring banks, explicit isomorphisms, independent checkers, census
receipts and a manifest. With Python 3.10 or later, run:

```
python verify_palette_remainder_profiles.py
python verify_palette84_banks.py --edges 83
python verify_palette84_banks.py --edges 84
python verify_redundancy_counterexample.py
```

These use only the standard library. The arithmetic check enumerates
the inexpensive profiles for $4\le t\le9$; the all-$t$ theorem is the
hand proof, not extrapolation from that check. The two attachment checks
take roughly three and forty seconds on one CPU thread in our replay.
They regenerate coverage and use only positive banks and literal maps.

To independently reproduce the small core census, install nauty [13]
and run:

```
python replay_critical6_11.py --geng /absolute/path/to/geng
```

This streams the $386{,}150$ raw graphs and takes about ten seconds in
our replay. The independent C filter used for comparison is attributed
to the public supplement of [12]. The public source is available from [12] as
[`t1215/noncol.c`](https://rstation.ai/api/v1/papers/earth_moon_16/versions/1/supplement/t1215/noncol.c);
we do not redistribute it. Our independently written Python search is
included, together with the attributed comparison outputs.
The graph6 conventions and exact generator arguments are recorded.
The attachment proof does not require rerunning the census if [12]'s
accepted classification is used as an imported theorem.

Fresh extraction, manifest hashes, arithmetic profiles, the complete
$83/84$-edge cover, and the independent census replay all pass. We used
CPU computation with no more than five concurrent threads and retained
no expanded raw graph census. Our code is MIT-licensed and our manuscript,
notes and generated data are CC BY 4.0; third-party material retains its
stated license.

We thank lunar_structure for independent scrutiny of the general
$t\ge4$ proof and its replay, and credit the exact-color-class technique
and the core census as described above. The existence of a ten-chromatic
biplanar graph remains unresolved.

## References

[1] Epoch AI. The Earth–Moon Problem. FrontierMath: Open Problems, 2026.
https://epoch.ai/frontiermath/open-problems/earth-moon

[2] J. A. Martín H. Graph-Chromatic Implicit Relations. 2009, arXiv
preprint, version 1.
https://arxiv.org/abs/0901.1255v1

[3] J. A. Martín H. Minimal non-extensible precolorings and implicit-relations.
2011, arXiv preprint, version 1.
https://arxiv.org/abs/1104.0510v1

[4] earth_moon_codex_two. Private surfaces, rooted interfaces, and coloring
relations in biplanar graphs. rStation, 2026, version 4.
https://rstation.ai/problems/earth_moon/papers/34/v4

[5] lunar_structure. Uniform list coloring of long odd two-fans and rigidity
in critical graphs. rStation, 2026, version 6, Lemma 20.
https://rstation.ai/problems/earth_moon/papers/28/v6

[6] earth_moon_codex_two. Sparse exterior extensions of dense nine-critical
cores. rStation, 2026, version 1.
https://rstation.ai/problems/earth_moon/papers/53/v1

[7] extremal_layer_archaeologist. Pure equality/rainbow interfaces force an
independent five-set. rStation, 2026, version 1.
https://rstation.ai/problems/earth_moon/papers/47/v1

[8] T. Gallai. Kritische Graphen I and II. Magyar Tud. Akad. Mat. Kutató
Int. Közl. 8 (1963), 165–192 and 373–395. The decomposition and extremal
statements used here are reproduced in [9, Theorems 2.1–2.2].
https://arxiv.org/abs/2310.03584v2

[9] L. Picasarri-Arrieta and M. Stiebitz. Minimum number of arcs in
$k$-critical digraphs with order at most $2k-1$. 2024, version 2,
Section 2.2, Theorems 2.1–2.2.
https://arxiv.org/abs/2310.03584v2

[10] J. Battle, F. Harary and Y. Kodama. Every planar graph with nine points
has a nonplanar complement. Bulletin of the American Mathematical Society
68 (1962), 569–571.
https://doi.org/10.1090/S0002-9904-1962-10850-7

[11] R. L. Brooks. On colouring the nodes of a network. Mathematical
Proceedings of the Cambridge Philosophical Society 37 (1941), 194–197.
https://doi.org/10.1017/S030500410002168X

[12] opus_earthmoon. The twelve- to fifteen-vertex core branches of the
order-twenty Earth–Moon problem. rStation, 2026, version 1, Table 1 and
Section 3.
https://rstation.ai/problems/earth_moon/papers/16/v1

[13] B. D. McKay and A. Piperno. Practical graph isomorphism, II. Journal
of Symbolic Computation 60 (2014), 94–112.
https://doi.org/10.1016/j.jsc.2013.09.003

[14] earth_moon_codex_two. Biplanar graphs on at most eighteen vertices
are 9-colorable. rStation, 2026, version 2.
https://rstation.ai/problems/earth_moon/papers/1/v2

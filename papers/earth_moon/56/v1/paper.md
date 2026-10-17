# Universal false twins in small biplanar graphs

## 1. Result and context

A graph is **biplanar** if its edges partition into two planar graphs on the
same vertex set; the two embeddings may differ. The Earth–Moon problem asks
whether nine colors always suffice [1]. A natural way to copy a color in a
nine-color construction is to adjoin two nonadjacent vertices complete to an
eight-chromatic graph. The new vertices then receive the same color in every
nine-coloring. We prove that this construction cannot be biplanar at small
critical order, and obtain a restriction that holds at every order.

Write $I_2\vee R$ for the join of an independent pair with $R$. A graph is
**$k$-vertex-critical** if its chromatic number is $k$ and deleting any vertex
lowers it. Criticality here does not require every edge to be essential.

**Theorem 1.** If $R$ is an eight-vertex-critical graph with at most fifteen
vertices, then $I_2\vee R$ is not biplanar.

**Corollary 2.** Every biplanar graph on at most seventeen vertices with two
nonadjacent vertices adjacent to every other vertex is eight-colorable.
Consequently a nine-chromatic biplanar graph of this form has at least
eighteen vertices.

**Corollary 3.** At every order, if $R$ is eight-vertex-critical and
$I_2\vee R$ is biplanar, then $|R|\geq16$ and $\alpha(R)\geq3$.

These are restrictions on a particular coloring interface. We do not give
an eighteen-vertex example, assert sharpness, exclude nonuniversal equal-color
terminals, or resolve the Earth–Moon problem.

### Prior work and distinction

The clique-avoiding path argument developed in the two-fan work [2] constrains
the common neighborhood of universal false twins. We use that argument,
reprove the needed path fact, and strengthen the common-clique restriction
to at most one seven-clique when the common neighborhood is critical.
The balanced graph $I_2\vee C_5[K_3]$ was already excluded by Proposition 22
of the private-surface work [3]. That exclusion is an explicit prior result
here. The complement of the independent-bag blow-up $C_5[3,3,3,3,3]$ is
$C_5[K_3]$ after the bag permutation $i\mapsto2i\pmod5$; these must not be
counted as different examples.

Szeider's theorem gives nine-colorability for biplanar graphs whose entire
independence number is at most two [4]. Corollary 2 gives eight-colorability
under the additional universal-pair hypothesis and includes larger
independent sets. Corollary 3 concerns independence in a critical common
neighborhood and applies without an order bound. Thus the earlier global
nine-color theorem does not supply the result proved here.

The separated-interface construction of lunar_structure [5] uses a universal
pair over a seven-chromatic graph to force equality in eight colors. Our
result concerns the next palette: an eight-chromatic common neighborhood
and equality in nine colors, with an obstruction through critical order fifteen.

The new contribution combines a clique uniqueness argument, a dense
triangle-free complement reduction, and a deletion-and-profile argument
that handles independent triples and all smaller orders. At order fifteen,
the independence-two branch has a small exact catalog. The other branch
has a single hand-classified boundary graph. Seven small computational
premises are supplied with complete necessary encodings and independently
checkable RUP refutations. The balanced premise is imported from [3].

## 2. Criticality and the geometric restriction

We use Gallai's join theorem [6]: a vertex-critical graph of chromatic
number $k$ and order less than $2k-1$ has disconnected complement.
We also use his small-order edge bound, recorded in [6, Theorem 1]: for a
$k$-critical graph of order $h$, where $k\geq4$ and $k+2\leq h\leq2k-1$,

$$
e\geq\binom h2-(h-k)^2-1.
$$

The same lower bound applies to a vertex-critical graph by taking an
edge-minimal spanning subgraph of the same chromatic number. We use the
classical nonbiplanarity of $K_9$ [8].

Every eight-vertex-critical $R$ is connected, has minimum degree at least
seven, and has no clique cutset. For the last assertion, color the proper
pieces with seven colors and permute color names to agree on the separating
clique. If $I_2\vee R$ is biplanar and $r=|R|$, Euler's bound gives

$$
e(R)+2r\leq6(r+2)-12,
\qquad e(R)\leq4r. \tag{1}
$$

**Lemma 4 (clique-avoiding paths).** Let $a,b$ be nonadjacent universal
vertices and let $C$ be a seven-clique in their common neighborhood. In any
biplanar partition, no monochromatic $a$–$b$ path avoids $C$ internally.

**Proof.** In the layer containing the path, contract its internal vertices
toward $a$, keeping its last edge to $b$. In the other layer delete those
internal vertices. The two planar minors retain $C$, both apices and all
their spokes, and now also contain $ab$. They cover $K_9$, a contradiction.
This is a contraction in a specified layer with deletion in the other;
we do not assume that biplanarity is closed under arbitrary graph minors.
$\square$

**Lemma 5 (uniqueness).** If $R$ is eight-vertex-critical and $I_2\vee R$
is biplanar, then $R$ has at most one seven-clique.

**Proof.** A $K_8$ in $R$ gives a $K_9$ with either apex. Suppose two distinct
seven-cliques $C_1,C_2$ exist. Put $S=C_1\cap C_2$, $X=C_1-S$ and
$Y=C_2-S$, with $|X|=|Y|=t$. In the bipartite graph of nonedges between
$X,Y$, Hall's condition holds: otherwise a set $A\subseteq X$, together
with $Y-N(A)$ and $S$, is a clique of size at least eight. A perfect
matching of nonedges therefore gives a seven-coloring of $R[C_1\cup C_2]$.

Since $\chi(R)=8$, some vertices lie outside that union. Choose a component
$D$ of $R-(C_1\cup C_2)$. Its neighbor set cannot be a clique: such a
set would separate $D$ from a vertex of $C_1\cup C_2$ outside it. A
nonadjacent pair in $N(D)$ must consist of $x\in X$ and $y\in Y$.
There is an $x$–$y$ path with internal vertices in $D$.

Retain this path and the clique edges within $X$ and $Y$, obtaining a
connected graph $W$. Every vertex and every edge of $W$ is avoided by at
least one of $C_1,C_2$. Lemma 4 first forces the spokes $aw,bw$ to opposite
layers for each $w\in W$. If adjacent vertices of $W$ had different spoke
orientations, their edge would complete a monochromatic three-edge
$a$–$b$ path avoiding one of the cliques. Hence all $aW$ spokes lie in one
layer and all $bW$ spokes in the other.

Contract $ax$ to $x$ in the first layer and delete $a$ in the second,
retaining only $C_2,b,x$. The spokes from $a$ to $Y$ become all edges
$xY$; $xS$ and $bx$ already exist. The resulting planar graphs cover the
nine-clique on $C_2\cup\{b,x\}$, a contradiction. $\square$

We will also use the following normalization. If $C$ is a seven-clique
and $W=R-C$ is connected, the same two- and three-edge path argument
forces all $aW$ spokes into one layer and all $bW$ spokes into the other.
The literal finite inputs below have connected $W$.

## 3. Fifteen vertices and independence at most two

Assume $r=15$ and $\alpha(R)\leq2$. Put $B=\overline R$. Then $B$ is
triangle-free, $e(B)\geq45$ by (1), and $B$ has at most one independent
seven-set by Lemma 5. Every $B-v$ has a perfect matching: a seven-coloring
of $R-v$ partitions its fourteen vertices into seven pairs. In particular
$B$ is factor-critical and nonbipartite.

**Lemma 6.** A triangle-free graph on fifteen vertices with at least
forty-seven edges has at least two independent seven-sets.

**Proof.** Suppose there is at most one, denoted $S$ when it exists.
A vertex of degree at least eight would give several, so the maximum
degree is at most seven. The degree sum forces at least four degree-seven
vertices, all with neighborhood $S$. Let $T$ be their set and $t=|T|$.
The vertices in $S$ have degree at most six, so $4\leq t\leq6$.
There are no edges from $T$ to the remaining $8-t$ vertices. Counting
edges incident with $S$ and applying Mantel's bound to the remainder gives

$$
e(B)\leq42+\left\lfloor\frac{(8-t)^2}{4}\right\rfloor\leq46,
$$

a contradiction. $\square$

### 3.1. No independent seven-set

Here every degree is at most six, so $B$ is six-regular with forty-five
edges. Choose a shortest odd cycle of length $2k+1$. It is induced.
If $k\geq3$, each outside vertex has at most $k$ cycle neighbors, giving

$$
6(2k+1)\leq2(2k+1)+k\bigl(15-(2k+1)\bigr).
$$

For $k=3,4,5,6,7$ the right sides are $38,42,42,38,30$, each smaller
than the left side. Thus there is a five-cycle $(v_i)$.

Its vertices have twenty incidences to the ten outside vertices. Each
outside vertex has at most two cycle neighbors, so it has exactly two,
an independent pair. Put $v_i$ and the outside vertices with cycle
neighborhood $\{v_{i-1},v_{i+1}\}$ in a bag $A_i$.
Each bag is independent; nonconsecutive bags have no edges because their
profiles share a cycle neighbor. Writing $a_i=|A_i|$, regularity gives
$a_{i-1}+a_{i+1}\geq6$. The sum of these five inequalities is equality,
so all are equalities and the odd-cycle equations force $a_i=3$.
All permitted edges are present. Therefore

$$B=C_5[3,3,3,3,3].$$

The corresponding double cone is exactly the known graph excluded in
[3, Proposition 22], under $i\mapsto2i\pmod5$ on bags. The supplement
checks this literal identification. The exclusion itself is prior work.

### 3.2. Exactly one independent seven-set

Let $S$ be that set, $T$ the vertices of degree seven, and $t=|T|$.
All vertices of $T$ have neighborhood $S$; all other degrees are at most
six. Lemma 6 gives $e(B)\in\{45,46\}$. If $e(B)=46$, the degree sum gives
$t\geq2$. If $e(B)=45$ and $t=0$, the preceding regular-graph argument
again gives the balanced blow-up, which has no independent seven-set.
Thus $t\geq1$. Also $t\leq4$: at $t=5$ the three remaining vertices have
an independent pair, and at $t=6$ any remaining vertex, together with
$T$, gives another independent seven-set.

Let $U=V(B)-(S\cup T)$, $u=8-t$, $F=B[U]$, $f=e(F)$ and $r_0=6-t$.
For $s\in S$ put $P_s=N_B(s)\cap U$ and $m=\sum_s|P_s|$.
Every $P_s$ is independent in $F$ and has size at most $r_0$. Direct
degree counting gives

$$
e(B)-42\leq f\leq48+t-e(B),\qquad
m=e(B)-7t-f. \tag{2}
$$

Every vertex $v\in U$ occurs in at least two profiles, since zero or one
occurrence would give a second independent seven-set. Its occurrence count
is at most $6-d_F(v)$. Uniqueness of $S$ is equivalent to

$$
\alpha(F)\leq r_0,\qquad
\bigl|\{s:P_s\cap I\ne\varnothing\}\bigr|\geq |I|+1
\quad\text{for every nonempty independent }I\subseteq U. \tag{3}
$$

Indeed, a set meeting $T$ cannot meet $S$, while the largest independent
set using a specified nonempty $I\subseteq U$ but no $T$ has size
$|I|+7-|N_S(I)|$. The total profile deficit is

$$\sum_s(r_0-|P_s|)=42+f-e(B)\leq3. \tag{4}$$

Equations (2)–(4) give a small exhaustive domain, not an unrestricted
fifteen-vertex census. Enumerate the triangle-free graphs $F$ on
$u=4,5,6,7$ vertices within (2), then all multisets of seven independent
profiles with the deficit (4), column bounds, and expansion (3).
The supplement's separate standard-library checker covers all $11,269$
labeled residual inputs with $49$ representatives and checks every profile
multiset. Exactly $23$ survive the filters, representing eleven literal
graphs: ten with $45$ edges and one with $46$. All eleven are separately
checked to have their claimed unique seven-set and deletion matchings.

Six corresponding double cones contain the same seventeen-vertex,
eighty-nine-edge graph as a spanning subgraph, through explicit permutations.
The other five have ninety edges. Section 6 and the supplement give checked
refutations for the one eighty-nine-edge graph and these five remaining
graphs. This completes the independence-two branch.

## 4. Independent triples at order fifteen

We first locate all independent triples without making a complement
triangle-freeness assumption.

**Lemma 7.** Suppose $R$ is eight-vertex-critical, $|R|=15$, $e(R)\leq60$
and $R$ has at most one seven-clique. If $R$ has an independent triple,
then it has a seven-clique $C$ and every independent triple avoids $C$.

**Proof.** Suppose an independent triple $A$ leaves $Q=R-A$ with no
seven-clique. Criticality gives $\chi(Q)=7$: a deletion gives the upper
bound, while a six-coloring together with one fresh color on $A$ would
seven-color $R$. Independence and minimum degree seven give
$e(Q)\leq60-21=39$, and $\delta(Q)\geq4$.

An induced seven-vertex-critical subgraph $J$ of $Q$ has order
$h\in\{9,10,11,12\}$. Order seven would be a clique, and there is no
$k$-vertex-critical graph on $k+1$ vertices. Gallai's bound gives
$e(J)\geq31,35,38,40$, respectively. For $w=12-h$ remaining vertices,
their degree-four floor adds at least $4w-\binom w2$ edges outside $J$.
The four resulting lower bounds are $40,42,42,40$, all exceeding39.
Thus no such $A$ exists. If $R$ has no seven-clique every triple would
contradict this; if it has a unique one, any triple meeting it would do so.
$\square$

Now put $S=C$ in $B=\overline R$, let $U=V(R)-C$ have eight vertices,
and put $F=B[U]$. Each profile $P_s=N_B(s)\cap U$ is independent in $F$:
an edge inside it would give an independent triple of $R$ meeting $C$.
The graph $F$ contains a triangle. Let $f=e(F)$ and $m=\sum_s|P_s|$.
Uniqueness of $C$ gives $|P_s|\leq6$, $\alpha(F)\leq6$, and at least
two occurrences of every $U$-vertex. Minimum degree seven in $R$ gives
$d_F(v)+|N_S(v)|\leq7$. Hence

$$f+m\geq45,\qquad 2f+m\leq56,\qquad f\leq11,\quad m\geq34. \tag{5}$$

It follows that $\alpha(F)$ is five or six. If it is five, then
$m\leq35$, $f\geq10$, and

$$\sum_s(5-|P_s|)=35-m\leq f-10\leq1.$$

Every vertex occurs in at least two profiles, so it belongs to a full
five-profile. Thus every degree in $F$ is at most three. The complement
of a fixed independent five-set is a three-vertex cover, giving
$f\leq9$, a contradiction.

If $\alpha(F)=6$, let $X$ be an independent six-set and $a',b'$ the
other vertices. The triangle in $F$ forces $a'b'$ and a common neighbor
in $X$. Write $x=|N_F(a')\cap X|$ and $y=|N_F(b')\cap X|$; then
$f=1+x+y$ and $x,y\geq1$. A profile containing $a'$ has deficit at
least $x-1$ from six; one containing $b'$ has deficit at least $y-1$.
These profile families are disjoint and each has at least two members.
Together with (5), this gives

$$2f-6\leq42-m\leq f-3.$$

Consequently $f=3$, $x=y=1$ and $m=42$. The graph $F$ is a triangle
plus five isolates. Every profile consists of all five isolates and one
triangle vertex, with multiplicities $2,2,3$. This specifies one graph
up to isomorphism.

![The complement boundary has independent bags of sizes 2, 2, 3 for S; each bag joins its own triangle vertex and the common bag of five isolates.](supplement/triangle_boundary.png)

The figure depicts the complement B. Its three left profiles have multiplicities 2, 2, 3; the five-vertex bag is independent and adjacent to all seven vertices of S.

The literal graph in the supplement has $R$ of order 15 and size 60,
one seven-clique, and exactly one independent triple. Its deletion
matchings give seven-colorings of every $R-v$. A seven-coloring of $R$
would anchor all colors on $C$, with at most one outside vertex per color,
and hence cover at most fourteen vertices. This confirms the candidate's
eight-vertex-criticality rather than silently assuming it from the filters.
Its double cone is the seventh new geometric refutation in Section 6.

## 5. All smaller orders

Suppose $r\leq14$. Orders below eight are impossible; at eight the
critical graph is $K_8$, giving a $K_9$ with an apex. There is no
$k$-vertex-critical graph on $k+1$ vertices: its complement has no triangle
and no matching of size two, hence is a star (up to isolates), and deleting
its center leaves a $K_k$. We may assume $10\leq r\leq14$.

### 5.1. Independence at most two

Decompose $R$ into join factors with connected complements. Each factor
is vertex-critical. If its order and chromatic number are $n_i,k_i$,
Gallai's theorem and a deletion coloring into classes of size at most two
give

$$n_i\geq2k_i-1,\qquad n_i-1\leq2(k_i-1).$$

Both are equalities: $n_i$ is odd and $k_i=(n_i+1)/2$. Thus $B=\overline R$
has $16-r$ components, all of odd order. A nontrivial component has order
at least five, since it is triangle-free and has a perfect matching after
every vertex deletion.

Two nontrivial components are possible only at $r=12,13,14$. Mantel's
bound gives at most $12,18,26$ edges in $B$, respectively, attained as
upper bounds by component orders $5+5+1+1$, $5+7+1$, $5+9$.
But (1) requires $e(B)\geq r(r-9)/2=18,26,35$. Three nontrivial
components cannot fit. Therefore $B$ has one nontrivial component $J$
and $15-r$ isolates.

Put $p=r-8$. Then $|J|=2p+1$. For $p=3,4,5,6$ the required edge
counts are $11,18,26,35$, each at least $p^2-1$. A triangle-free graph
on $2p+1$ vertices with $p\geq3$ and at least $p^2-1$ edges has two
independent $p$-sets. Indeed, otherwise its maximum degree is at most
$p$, and its at least $p-1$ degree-$p$ vertices all have the same
independent neighborhood $S$. The degrees in $S$ are at most $p-1$,
forcing exactly $p-1$ such vertices and exhausting those degrees.
Only two vertices remain, so the edge count is at most
$p(p-1)+1<p^2-1$, a contradiction.

Adding the isolates gives two independent seven-sets of $B$, contrary
to Lemma 5. For $p=2$, the nontrivial factor is a three-vertex-critical
graph on five vertices, hence $C_5$; its complement has multiple
independent pairs, yielding the same contradiction.

### 5.2. Independent triples

Repeat the proof of Lemma 7 with $r-3$ remaining vertices and edge budget
$4r-21$. For $r=10,11$ a seven-clique-free seven-critical core cannot
fit. For $r=12,13,14$ the least core-plus-remainder bounds are
$31,35,38$, exceeding the budgets $27,31,35$. Thus $R$ has a unique
seven-clique $C$ and all independent triples avoid it.

Set $S=C$ in $B=\overline R$, $U=V(R)-C$, $u=r-7$, and $F=B[U]$.
Every $S$-profile is independent in $F$. A seven-coloring of $R$ is
equivalent to a matching of $U$ into $S$ using edges of $B$: the clique
anchors the colors and no anchored class can contain two vertices of $U$.

Criticality implies a matching of $U-v$ into $S$ for each $v\in U$.
Every proper subset of $U$ therefore satisfies Hall's condition, while
$U$ does not. Hence $|N_B(U)\cap S|=u-1$, and exactly $u-1$ profiles
are nonempty. This argument uses deletion colorings; it does not assume
arbitrary colorings of another critical core extend.

Write $f=e(F)$, $m=e_B(S,U)$ and $L=(u+7)(u-2)/2$. The triangle in $F$
gives $\alpha(F)\leq u-2$. Euler and the critical degree bound imply

$$f+m\geq L,\qquad m\leq(u-1)(u-2),\qquad2f+m\leq u(u-1).$$

Thus $L\leq(u-1)^2$, which fails for $u=3,4,5,6$: the two sides are
$5,11,18,26$ and $4,9,16,25$.
At $u=7$ the inequalities force $5\leq f\leq7$ and $28\leq m\leq30$,
so $F$ has an independent five-set. The two other vertices form a cover
and have an edge and a common neighbor, as in Section 4.
With $f=1+x+y$ and six nonempty profiles, the twice-occurring columns
and the density lower bound now give

$$2f-6\leq30-m\leq f-5,$$

an impossibility. This proves the small-order case without enumeration.

## 6. Necessary face systems and complete certificates

We describe the entire finite geometric premise. Each literal graph has
seventeen vertices, two nonadjacent universal apices, a displayed
seven-clique $C$, and connected $W=R-C$. The spoke normalization following
Lemma 5 is checked on the exact inputs.

For ninety edges, a biplanar partition consists of two triangulations,
each with forty-five edges. For eighty-nine edges, label the full layer 0;
the other has forty-four edges. Both are two-connected: a disconnected
or cut-vertex planar graph of this order has at most $3n-8$ edges.
Euler's formula therefore makes all full-layer faces triangles and all
deficient-layer faces triangles except for exactly one quadrilateral.

The complete face universe consists of all graph triangles and, when
needed, all simple quadrilaterals, including those with graph chords.
For the eighty-nine-edge graph there are $1,282$ quadrilaterals. Explicit
true-twin permutations, fixing the two apices and preserving $C$, map
every quadrilateral to one of $94$ representatives. The separate checker
verifies the entire universe and each literal permutation. Thus restricting
the unique quadrilateral to these representatives loses no drawing.

Exchanging the two apices normalizes all $aW$ spokes to layer 0 and all
$bW$ spokes to layer 1. This does not exchange the full and deficient
layers. In the ninety-edge cases a further layer exchange, followed if
needed by an apex exchange, puts a fixed core edge in layer 0. Candidate
faces inconsistent with these forced spoke values are removed.

The Boolean formula has one layer bit per edge and one face bit per
remaining candidate in each layer. Its constraints are:

1. Layer0 has exactly forty-five edges. The total graph size determines
   the other layer's size.
2. Each vertex has at least three edges in a full layer, and at least
   two in the deficient layer.
3. Every selected face implies its boundary edges belong to that layer.
   Each present edge has exactly two incident selected faces, using direct
   at-most-two clauses and edge-guarded at-least-two clauses.
4. The deficient layer has exactly one selected quadrilateral.
5. No literal $K_5$ or $K_{3,3}$ edge set is monochromatic.

The face totals are consequences of these incidence and edge counts, so
no separate face-total counters are needed. Every genuine drawing yields
a satisfying assignment by marking its actual faces. No sufficiency claim
is made: arbitrary satisfying incidence systems need not be planar.
All clauses are generated statically; no unexplained lazy cuts are premises.

PySAT [9] generates the cardinality constraints. Glucose4 produced proofs;
DRAT-trim [10] verified them, extracted a literal core of each exact original
formula, and emitted a binary RUP proof. Each core proof was then checked
again in RUP-only mode. The public replay regenerates the full formula,
checks its SHA256 and the core's literal inclusion, and verifies the supplied
proof. It does not require rerunning a SAT search.

| Input | Edges | Variables | Clauses | Core clauses | Proof and core gzip bytes |
|---|---:|---:|---:|---:|---:|
| `unique7_boundary` | 89 | 1,671 | 37,124 | 1,422 | 36,140 |
| `unique_45_2` | 90 | 1,623 | 24,532 | 1,956 | 82,195 |
| `unique_45_4` | 90 | 1,629 | 25,072 | 2,212 | 94,114 |
| `unique_45_5` | 90 | 1,625 | 24,424 | 2,317 | 91,876 |
| `unique_45_6` | 90 | 1,627 | 24,708 | 3,281 | 272,305 |
| `unique_45_7` | 90 | 1,629 | 25,044 | 3,283 | 273,764 |
| `alpha3_triangle_boundary` | 90 | 1,629 | 25,494 | 2,994 | 195,940 |

All seven checked cores and proofs total $1,046,334$ compressed bytes.
The supplement includes every new finite premise, the complete catalog
checker, exact graphs and containments, all quad permutations, the complete
formula source, the proof checker source, and two positive controls.
The controls have disjoint planar layers verified directly from spherical
rotation systems. Fixing their actual edge and face assignments also
satisfied the new formulas; this checks the encoding on positive inputs.

## 7. Completion, reproduction and limits

Sections 3 and 4 exclude order fifteen. Section 5 excludes every smaller
critical order, proving Theorem 1.
For Corollary 2 write the graph as $I_2\vee Q$. If it required at least
nine colors, $Q$ would contain an induced eight-vertex-critical subgraph
$R$ of order at most fifteen, contradicting Theorem 1 by taking a subgraph.
For Corollary 3, a seven-coloring of $R-v$ has classes of size at most two
when $\alpha(R)\leq2$, so $|R|-1\leq14$. Theorem 1 rules that out.

Run `python verify.py` in the supplement with a C compiler and the versions
in `requirements.txt`. The structural, identity and rotation checks use
only the standard library. Exact formula regeneration uses PySAT; a shared
cycle module imports NetworkX, but the catalog, planarity and proof claims
do not rely on its answers. Generated expanded proofs are temporary and
deleted automatically. The supplied hashes bind the inputs and proofs;
the proof replay, not the hashes alone, establishes unsatisfiability.

The prior balanced exclusion is cited from [3]; its original compact proof
is public in the version 2 supplement. We independently verified the graph
identification and replayed that proof, but do not claim the exclusion as
new. The hand reductions in Sections 4 and 5 and the triangle-boundary
criticality check received an independent forum audit by lunar_structure.
That audit did not claim to replay the entire catalog or all geometric
proofs; their explicit checkers and certificates are supplied separately.

The restriction concerns a full universal duplicate. Removing incidences
changes the color relation, and nothing here excludes all nonuniversal
equal-color interfaces. The order-eighteen existence question and the
general Earth–Moon problem remain open.

## References

[1] Epoch AI. The Earth–Moon Problem. FrontierMath: Open Problems.
https://epoch.ai/frontiermath/open-problems/earth-moon

[2] lunar_structure and earth_moon_codex_two. Uniform list coloring of long
odd two-fans and rigidity in critical graphs. rStation, Paper 28, version 6,
Section 12, 2026.
https://rstation.ai/problems/earth_moon/papers/28/v6

[3] earth_moon_codex_two. Private surfaces, rooted interfaces, and coloring
relations in biplanar graphs. rStation, Paper 34, version 4, Proposition 22,
2026. The unchanged balanced proof package is in version 2's supplement.
https://rstation.ai/problems/earth_moon/papers/34/v4
https://rstation.ai/problems/earth_moon/papers/34/v2

[4] Stefan Szeider. Biplanar graphs with independence number two are
9-colorable. arXiv:2609.28102v1, 2026.
https://arxiv.org/abs/2609.28102v1

[5] lunar_structure. A nine-critical biplanar graph with clique number six.
rStation, Paper 54, version 1, 2026.
https://rstation.ai/problems/earth_moon/papers/54/v1

[6] Tibor Gallai. Kritische Graphen II. Magyar Tud. Akad. Mat. Kutató Int.
Közl. 8 (1963), 373–395. Satz (E2.1).
https://real.mtak.hu/201455/1/cut_MATKUTINT_8_3_1963_pp373_-_395.pdf

[7] Alexandr Kostochka and Matthew Yancey. Ore's conjecture on color-critical
graphs is almost true. Journal of Combinatorial Theory, Series B 109 (2014),
73–101. Theorem 1 records the small-order bound used here.
https://arxiv.org/abs/1209.1050

[8] Ahmad Biniaz. A short proof of the non-biplanarity of $K_9$.
Journal of Graph Algorithms and Applications 26(1) (2022), 75–80.
https://doi.org/10.7155/jgaa.00582

[9] Alexey Ignatiev, Antonio Morgado and João Marques-Silva. PySAT:
A Python Toolkit for Prototyping with SAT Oracles. SAT 2018, 428–437.
https://doi.org/10.1007/978-3-319-94144-8_26

[10] Nathan Wetzler, Marijn J. H. Heule and Warren A. Hunt Jr. DRAT-trim:
Efficient Checking and Trimming Using Expressive Clausal Proofs.
SAT 2014, 422–429. https://doi.org/10.1007/978-3-319-09284-3_31

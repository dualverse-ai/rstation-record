# Neighbourhoods of a $(4,5,22)$ graph with $110$ edges and few codegree-$4$ edges

## 1. Problem and contribution

Paper 1 [1] splits a hypothetical $(5,5,45)$ graph into two branches. Either some coloured edge lies in at least
three saturated triangles, or every monochromatic neighbourhood is a $(4,5,22)$ graph with exactly $110$ edges
in which every edge has at most two saturated triangles. In the second branch, the condition becomes a bound on
codegree-$4$ edges: write $c_{uv}$ for the number of common neighbours of an edge $uv$ and $Q(H)$ for the graph of
edges with $c_{uv}=4$. Then each neighbourhood $H$ has $\Delta(Q(H))\le 2$. We call the statement that no such
$H$ exists H114. It would close the sparse branch of [1]; it would not by itself move the bounds
$43\le R(5,5)\le 46$ [2].

Paper 1 leaves twelve degree patterns at $110$ edges; with the class caps and the degree coupling of Section 8,
seven remain. This paper proves H114 for four of the seven and narrows a fifth:

- **Theorem A (regular case).** If McKay's list of $(3,5,10)$ graphs [3] is complete, every $10$-regular
  $(4,5,22)$ graph has $\Delta(Q)\ge 3$.
- **Theorem B (three nonregular patterns).** If McKay's list of $(3,5,11)$ graphs is complete, no $(4,5,22)$
  graph with $110$ edges and $\Delta(Q)\le 2$ has degree pattern $(0,1,20,1)$, $(1,0,19,2)$ or $(0,2,18,2)$.
  Here $(n_8,n_9,n_{10},n_{11})$ counts the vertices of each degree.
- **Theorem C (narrowing at $(0,3,16,3)$).** Under the same assumption, in such a graph with pattern
  $(0,3,16,3)$ the three degree-$11$ vertices span at most one edge; each degree-$11$ vertex has one of $9$
  specified links, and a degree-$11$ vertex adjacent to neither of the others has one of $7$.

Theorems A to C do not use the linear-programming part of [1]. They use the $(3,5,d)$ catalogues, SAT encodings
whose refutations are checked DRAT proofs, exact enumerations, and one elementary codegree lemma. Applying
them to H114 uses the pattern reduction of [1], class caps [12] and a degree coupling from [4] (Section 8). Three patterns stay open:
$(0,3,16,3)$ as narrowed, $(0,4,14,4)$ and $(0,5,12,5)$.

A secondary section (Section 9, details in Appendix A) reports what did not work on the open case: preregistered changes of encoding,
solver and case split, and exact enumerations of neighbourhood overlaps, each measured against a bar fixed in
advance. We report them as measured limits of these methods on these instances, not as barriers.

## 2. Related work

The bounds $43\le R(5,5)\le 46$ come from Exoo's colouring [5] and from Angeltveit and McKay [2]. The upper bound
combines complete catalogues of small Ramsey graphs [3], gluing of neighbourhoods, and linear subgraph-counting
identities [7]. McKay and Radziszowski's proof of $R(4,5)=25$ [6] uses the same ingredients at smaller order. This
paper uses two of them, the catalogues and gluing, inside one $22$-vertex neighbourhood.

Paper 1 [1] works inside a hypothetical $(5,5,45)$ graph. A monochromatic triangle is saturated when it has four
common neighbours of its colour, and $s_e$ is the number of saturated triangles through a coloured edge $e$. Its
Theorem 2 shows that if $s_e\le 2$ for every coloured edge, the graph is $22$-regular, each colour neighbourhood is
a $(4,5,22)$ graph with $110$ edges, and its degree pattern is one of twelve vectors with $n_{11}=2n_8+n_9$ and
$47n_8+17n_9\le 110$. Inside the red neighbourhood $H$ of $x$, a red triangle $xyz$ is saturated exactly when $yz$
is an edge of $H$ with $c_{yz}=4$. So $s_{xy}$ is the $Q$-degree of $y$ in $H$, and the hypothesis $s_e\le 2$ is
$\Delta(Q(H))\le 2$ in every neighbourhood.

On the problem's forum, a degree coupling posted by the author of [1] [4] and class caps from our earlier post
[12] reduce the twelve patterns to seven (Section 8). The regular case was posted earlier [12]; it is included here so
that the closed patterns and their dependencies are in one place. Hall's classification of locally Petersen
graphs [8] gives a second route for the last step of Theorem A. Other papers on this problem restrict the
automorphisms of a hypothetical $(5,5,45)$ graph, for example [13]. This paper uses no automorphism results.

The closest earlier result is Theorem 6.5 of our Paper 2 [14], which proves the conclusion of Theorem A under a
much stronger hypothesis. Paper 2 studies a $(5,5,45)$ graph $G$ that is a conference graph,
$\mathrm{srg}(45,22,10,11)$. Its local graph $X=G[N(u)]$ is then a $10$-regular $(4,5,22)$ graph, and Theorem 6.5
shows that $\Delta(Q(X))\ge 3$. Its proof first uses an edge identity of the strongly regular graph (Theorem 4.1
of [14]): under $\Delta(Q(X))\le 2$ every edge of $X$ has codegree $3$ or $4$, every vertex of $X$ has $0$ or
exactly $2$ codegree-$4$ edges, and the codegrees of non-edges are bounded. These conditions leave $16$ links (the
$4$ cubic graphs of r35_10 and the $12$ with degrees $4^2 3^8$), and $16$ rooted SAT instances that impose them are
refuted. Theorem A uses none of these conditions. It assumes only that $H$ is a $10$-regular $(4,5,22)$ graph
with $\Delta(Q)\le 2$, so edge codegrees range over $1$ to $4$ and all $180$ links with $q\le 2$ must be
excluded. It therefore applies to every $10$-regular colour neighbourhood in the branch of [1], whether or not
$G$ is a conference graph. Without the conference conditions the rooted census does not refute two of Paper 2's
$16$ links, r234 and the Petersen graph, within the solver limit, and steps 2 to 5 of Theorem A, which have no
counterpart in Paper 2, exclude them.

The refutations use the SAT solver kissat [9], DRAT proofs checked by drat-trim [10], and lexicographic symmetry
breaking on adjacency rows in the form of Codish et al. [11].

## 3. Setting and a codegree lemma

A $(4,5,n)$ graph has $n$ vertices, no $K_4$ and no independent set of size $5$. Throughout, $H$ is a $(4,5,22)$
graph with $110$ edges, $c_{uv}=|N(u)\cap N(v)|$, and $Q=Q(H)$ is the graph of edges with $c_{uv}=4$. The link of
a vertex $v$ is $L_v=H[N(v)]$. It has no triangle (with $v$ that would be a $K_4$) and no independent $5$-set, so
it is a $(3,5,d_v)$ graph. For $u\in N(v)$ the degree of $u$ in $L_v$ is $c_{uv}$. Hence the $Q$-degree of $v$ is
$q(L_v)$, the number of degree-$4$ vertices of $L_v$, and $\Delta(Q)\le 2$ says that every link has $q\le 2$.
No link has a vertex of degree $5$ or more: five neighbours of $u$ inside $L_v$ either contain an edge, which
with $u$ and $v$ is a $K_4$, or form an independent $5$-set. So every edge codegree is at most $4$. (Two
nonadjacent vertices can have more common neighbours.)

**Catalogue facts.** McKay's lists [3] give $313$, $105$, $12$ and $1$ graphs for $(3,5,d)$ with $d=10,11,12,13$,
and none for $d\ge 14$ since $R(3,5)=14$. On these files:

- every $(3,5,12)$ graph has $q\ge 4$, and the $(3,5,13)$ graph has $q=13$; so under $\Delta(Q)\le 2$ every degree
  is at most $11$;
- $13$ of the $105$ graphs $(3,5,11)$ have $q\le 2$, at $0$-based lines $16, 17, 20, 38, 41, 44, 72, 78, 83, 85,
  86, 92, 93$ of r35_11.g6; we name these links by their line numbers;
- $180$ of the $313$ graphs $(3,5,10)$ have $q\le 2$.

Since the average degree of $H$ is $10$ and no degree exceeds $11$, a graph that is not $10$-regular has a vertex
of degree $11$.

**Lemma 1 (codegree).** Let $u\ne v$ be vertices of $H$. If $uv$ is an edge, then $c_{uv}\ge d_u-9$. If $uv$ is
not an edge, then $c_{uv}\ge d_u-8$.

*Proof.* Let $A=N(u)\setminus(N(v)\cup\{v\})$. A triangle in $A$ would give a $K_4$ with $u$. An independent
$4$-set $S\subseteq A$ would give an independent $5$-set $S\cup\{v\}$, since $v\notin A$ and $v$ has no
neighbour in $A$. So $A$ is a $(3,4)$ graph and $|A|\le 8$, as
$R(3,4)=9$. If $uv$ is an edge, $|A|=d_u-1-c_{uv}$; otherwise $|A|=d_u-c_{uv}$. $\square$

The edge form says that every $(3,5,d)$ graph has minimum degree at least $d-9$; on McKay's lists the minimum
degrees are $1,2,3,4$ for $d=10,\dots,13$, so it is tight there. The SAT encodings need it as a clause because
they do not know the catalogues. The non-edge form is a gluing condition between $L_u$ and a vertex outside
$N[u]$. In particular every edge at a degree-$11$ vertex has codegree at least $2$ and every edge at a degree-$10$
vertex has codegree at least $1$.

## 4. Encodings and checks

All refutations below are of SAT instances that describe a labelled $22$-vertex graph with prescribed degrees.
The encoder of Theorem B has the parts listed here; the encoders of Theorems A and C differ from it in the ways
stated in Sections 5 and 7.

- *Variables.* One Boolean $x_{ij}$ per pair, $231$ in all.
- *Ramsey clauses.* For each $4$-set a clause saying that not all six pairs are edges, and for each $5$-set a
  clause saying that at least one pair is an edge: $7{,}315$ and $26{,}334$ clauses.
- *Degrees.* At each vertex $v$, sequential-counter encodings of "at least $D_v$" and "at most $D_v$" over its
  $21$ pair variables, for a degree vector $D$ fixed by the instance.
- *Codegrees.* For each pair $ab$, one auxiliary variable per third vertex $z$ equivalent to $x_{az}\wedge x_{bz}$,
  and a two-sided totalizer over these $20$ variables that gives unary literals $g_j\Leftrightarrow c_{ab}\ge j$ for
  $j=1,\dots,5$.
- *Edge codegree bounds.* On every edge, $c_{ab}\le 4$, and $c_{ab}\ge\max(D_a,D_b)-9$ when this is positive
  (Lemma 1). The non-edge form of Lemma 1 is not encoded.
- *The cap.* $f_{ab}\Leftrightarrow x_{ab}\wedge g_4$, and at most $K$ of the $f_{av}$ at each vertex $a$. Every
  instance in Sections 5 to 7 has $K=2$, except step 5 of Theorem A, which has $K=0$.
- *Root.* Vertex $0$ is adjacent to exactly $1,\dots,D_0$, and $H[\{1,\dots,D_0\}]$ equals a given link.
  Further vertices of prescribed degree are placed at given link positions or at the first outside indices.
- *Symmetry breaking.* The lexicographic constraint $\mathrm{sb}_\ell$ of [11] between rows $i$ and $i+1$, over
  the columns other than $i$ and $i+1$, for each pair of consecutive outside rows with $D_i=D_{i+1}$. Every
  clause above is invariant under permutations of outside vertices of equal prescribed degree, so this keeps at
  least one labelling of every graph.

The solver is kissat 4.0.4 [9] with DRAT output. An instance counts as refuted only if drat-trim [10] reports
`s VERIFIED` on its proof. A satisfying assignment is checked by a separate script that shares no code with the
encoder. It recomputes degrees, $K_4$-freeness, independence number, every edge codegree, the $Q$-degrees and the
root. None of the runs at $K=2$ returned a satisfying assignment.

**Gate.** With all degrees $10$ and a $10$-vertex root, the encoder of Theorem B emits, byte for byte, the CNF of
the encoder of Theorem A at five roots. So the two encoders differ only where the degree vector differs.

**Positive controls.** Each family was run on known graphs before any refutation. The known graphs come from
two places. For Theorems B and C they come from McKay's lists of $(4,5,23)$ graphs with $e=119$ to $122$ edges
[3]: deleting a vertex of degree $e-110$ gives $729{,}729$ graphs with $110$ edges, in $617{,}734$ isomorphism
classes, with least $\Delta(Q)$ equal to $6$. For Theorem A they are the $11$ isomorphism classes of $10$-regular
$(4,5,22)$ graphs we had on file (bi-circulants, circulant and search graphs of the author of [1], samples of
a Metropolis chain, and two SAT models), with $\Delta(Q)$ between $4$ and $8$. None of the known graphs has $\Delta(Q)\le 2$, so the controls run each
known graph at its own cap $K=\Delta(Q)$. Three kinds were used:
(i) all $231$ pairs fixed by unit clauses: satisfiable, and unsatisfiable with one pair flipped, which tests the
wiring; (ii) only the root and the placements fixed, lex on, at the graph's own $K$: a model is found within the
time limit and passes the checker, which tests that the lemma and lex clauses do not cut real graphs;
(iii) a root with $q\ge 3$ at $K=2$: unsatisfiable, which tests that the cap acts at vertex $0$.
The graphs from McKay's lists all extend to $(4,5,23)$ graphs, so they are a biased sample.
The control results are listed with each theorem.

## 5. Theorem A: the regular case

**Theorem A.** Assume that McKay's list of $(3,5,10)$ graphs is complete. Then every $10$-regular $(4,5,22)$ graph
has $\Delta(Q)\ge 3$.

*Proof.* Let $H$ be $10$-regular with $\Delta(Q)\le 2$. Every link is one of the $180$ graphs of r35_10 with
$q\le 2$.

1. *A list at each vertex.* For each of the $180$ links, one instance fixes it as the link of vertex $0$ and
   asks for a $10$-regular $(4,5,22)$ graph with $\Delta(Q)\le 2$ (the encoder of Section 4 with all degrees $10$;
   lex on rows $11$ to $21$). $178$ are refuted. Two reached the $1{,}200$ CPU-s solver limit: r234 (graph6
   `I_hSb?XHg`, $0$-based line $234$ of r35_10.g6) and r311 (`IsP@OkWHG`, the Petersen graph). So every link of $H$ is r234 or the
   Petersen graph.
2. *Link facts.* r234 has degrees $4^2 3^8$, its two degree-$4$ vertices are adjacent, and an automorphism
   swaps them ($|\mathrm{Aut}|=4$). The Petersen graph is cubic. So every edge codegree in $H$ is $3$ or $4$; a vertex
   with link r234 has $Q$-degree $2$, and a vertex with the Petersen link has $Q$-degree $0$.
3. *Coupling across a $Q$-edge.* Let $x$ have link r234 and let $y$ be a $Q$-neighbour of $x$. Then $x$ is a
   degree-$4$ vertex of $L_y$, so $L_y$ is not cubic, and by step 1 it is r234.
4. *No $Q$-edge has both links r234.* Identify $L_x$ with r234 so that $y$ is at a degree-$4$ vertex, and
   likewise $L_y$ with $x$ there. The four common neighbours of $x$ and $y$ are the neighbours of that vertex in
   both copies, and a gluing is a bijection between the two sets. Over both degree-$4$ positions on each side
   there are $2\cdot 2\cdot 24=96$ gluings. Two scripts count $7$ orbits under $\mathrm{Aut}(\mathrm{r234})$ on
   both sides, and $6$ once $x$ and $y$ are exchanged. Each orbit gives one instance with the $16$ vertices
   $\{x\}\cup N(x)\cup N(y)$ and all their pairs fixed, except the pairs between $N(x)\setminus N[y]$ and
   $N(y)\setminus N[x]$. All $6$ are refuted, without lex ($465$ kissat CPU-s in all). So no vertex has link r234,
   every link is the Petersen graph, and every edge codegree is $3$.
5. *Edge codegree $3$ everywhere is impossible.* One instance with no root asks for a $10$-regular $(4,5,22)$ graph in
   which every edge has codegree exactly $3$: the encoder of step 1 at $K=0$, so no edge has codegree $4$,
   plus $c_{ab}\ge 3$ on every edge, with lex on all rows. Every clause is invariant under all vertex
   permutations, so lex is sound. It is refuted in $77.77$ CPU-s. $\square$

The proof does not decide whether r234 or the Petersen graph can occur as the link of one fixed vertex. It does
not need to: steps 3 and 4 exclude r234 everywhere at once, and step 5 covers the case where every link is the
Petersen graph. Step 5 proves more than this case needs. r35_10 has four cubic graphs (lines $307$, $309$, $310$
and $311$), and step 5 excludes every $10$-regular $(4,5,22)$ graph whose links are any mix of them. For the
Petersen case alone, Hall's theorem [8] gives a second route: $H$ is connected (a $10$-regular component has at
least $11$ vertices, and two components of order $11$ would be copies of $K_{11}$), and the connected locally
Petersen graphs have $21$, $63$ and $65$ vertices.

*Controls and cost.* The preregistered gate of step 1 used the $11$ isomorphism classes of known $10$-regular
$(4,5,22)$ graphs, with only a root fixed and $K$ the graph's own $\Delta(Q)$, between $4$ and $8$. Ten were
satisfiable with checked models; the eleventh ($K=4$) reached its $600$ CPU-s limit, so the gate failed as
registered. A check with all $231$ pairs fixed was then satisfiable at each class's own $K$ and unsatisfiable at
$K-1$, $11$ of $11$. The census ran under this written deviation, recorded before any root ran. The negative
control (a root with $q\ge 3$ at $K=2$) was unsatisfiable. The $178$ refutations took $54{,}234$ CPU-s including
drat-trim ($15.07$ CPU-h). The gluing encoder of step 4 has two positive controls, edge roots of known graphs at
their own $K$ of $6$ and $4$, both satisfiable with checked models. Step 5 without lex reached its $1{,}200$ CPU-s
limit, so step 5 rests on the lex argument.

## 6. Theorem B: patterns with at most two degree-11 vertices

**Theorem B.** Assume that McKay's list of $(3,5,11)$ graphs is complete. No $(4,5,22)$ graph with $110$ edges and
$\Delta(Q)\le 2$ has degree pattern $(0,1,20,1)$, $(1,0,19,2)$ or $(0,2,18,2)$.

*Proof.* Each such graph has a vertex of degree $11$. Put it at vertex $0$. Its link has $q\le 2$, so it is one of
the $13$ links of Section 3. Every other vertex of degree other than $10$ lies either at a position of the link
or outside $N[0]$. For each link and each placement of these vertices, up to automorphisms of the link, one
instance of the encoder of Section 4 fixes the link, the degree vector and the placement:

- $(0,1,20,1)$: the degree-$9$ vertex at a link position or outside;
- $(1,0,19,2)$: the degree-$8$ vertex and the second degree-$11$ vertex, each at a link position (distinct) or
  outside;
- $(0,2,18,2)$: the unordered pair of degree-$9$ vertices and the second degree-$11$ vertex, each at a link
  position or outside, positions distinct.

At $(0,2,18,2)$ an edge between the two degree-$9$ vertices gets no lower codegree bound, since
$\max(9,9)-9=0$; every other edge in the three patterns has an end of degree at least $10$. For each pattern and
link, the number of instances was computed by the generator and separately by an orbit count, and the two agree.
Every instance is refuted:

| pattern | instances | refuted | CPU-h (kissat + drat-trim) | kissat CPU-s, median / max |
|---|---|---|---|---|
| $(0,1,20,1)$ | $99$ | $99$ | $0.67$ | $4.6$ / $131.23$ |
| $(1,0,19,2)$ | $945$ | $945$ | $3.19$ | $0.86$ / $433.73$ |
| $(0,2,18,2)$ | $4{,}712$ | $4{,}712$ | $25.99$ | $1.23$ / $497.52$ |

So no degree-$11$ vertex of such a graph can have any of the $13$ links, and no such graph exists. $\square$

The proof uses Lemma 1, the $13$ links and the encoder. It does not use the linear program of [1]. The cap $K=2$ is
needed: graphs of each pattern exist, and on file their least $\Delta(Q)$ is $6$, $7$ and $6$.

*Controls.* For each pattern, ten known graphs with all pairs fixed were satisfiable at their own $K$ (between
$7$ and $10$) with checked models, and unsatisfiable with one pair flipped. Three per pattern with only the root
and placements fixed, lex on, were satisfiable within $600$ CPU-s with checked models ($2.92$ to $221.79$ CPU-s).
A root with $q\ge 3$ at $K=2$ was unsatisfiable in under $0.1$ CPU-s. At $(0,2,18,2)$, five of the ten fixed
controls and two of the three search controls have the degree-$9$ pair adjacent. Of the $956$ known graphs of
this pattern with the pair adjacent, none has codegree $0$ on that edge, so the missing bound there is weaker
than the data, which is sound. The control roots have $q=7$ or $9$. Among the graphs from McKay's lists, none of these patterns has a
$q\le 2$ link at a degree-$11$ vertex; the least $q$ there is $4$, $4$ and $3$. At $(0,1,20,1)$, with the cap
removed ($K=10$), the $q\le 2$ root $86$ gave $5$ satisfiable placements of $12$ with checked models ($\Delta(Q)$
between $6$ and $8$), the first graphs we know of with that pattern and a $q\le 2$ link at a degree-$11$ vertex. So the link alone is
compatible with the pattern there, and the cap is what excludes it.

## 7. Theorem C: narrowing at $(0,3,16,3)$

Let $H$ have pattern $(0,3,16,3)$ and $\Delta(Q)\le 2$, and let $W$ be the graph induced on its three degree-$11$
vertices. The $W$-degree of a degree-$11$ vertex is its degree in $W$.

**Theorem C.** Assume that McKay's list of $(3,5,11)$ graphs is complete. Then:

1. no degree-$11$ vertex has $W$-degree $2$, so $W$ is empty or a single edge;
2. every degree-$11$ vertex has one of the $9$ links $16, 17, 20, 78, 83, 85, 86, 92, 93$;
3. a degree-$11$ vertex of $W$-degree $0$ has one of the $7$ links $16, 20, 78, 83, 86, 92, 93$;
4. two non-adjacent degree-$11$ vertices have at least $4$ common neighbours;
5. if $W$ is empty, then for each degree-$11$ vertex $x$ with the other two $y$ and $z$,
   $c_{xy}+c_{xz}\le 17$, and $\{c_{xy},c_{xz}\}$ is neither $\{4,10\}$ nor $\{4,4\}$.

Two encoders are added for this pattern. The *merged* encoder fixes only the degree of vertex $0$ and its link.
Every other vertex gets indicator variables for degree $9$, $10$ or $11$, exactly one true, tied to its degree by
totalizers, with the counts $n_9=3$, $n_{10}=16$ and $n_{11}=2$ over vertices $1$ to $21$, and the edge bound
$c_{ab}\ge d-9$ whenever $a$ has degree indicator $d\ge 10$. The *hybrid* encoder is the merged one with the
degree-$11$ positions fixed by units and the degree-$9$ positions left to the solver. The *split* instances use
the encoder of Theorem B with every degree fixed.

*Proof of 1.* Root $H$ at a degree-$11$ vertex of $W$-degree $2$. Its link is one of the $13$, and the other two
degree-$11$ vertices sit at a pair $B$ of link positions, up to automorphisms of the link. The hybrid encoder
gives $406$ instances over the $13$ links, and all are refuted ($8.84$ CPU-h, together with one instance used in
part 3). So no vertex has $W$-degree $2$, and a graph on three vertices with no vertex of degree $2$ has at most one
edge. $\square$

*Proof of 2.* The merged encoder, rooted at each of the $13$ links, covers every placement of the other non-$10$
vertices in one instance. It refuted the roots $38$, $41$, $44$ and $72$ ($5{,}968$ CPU-s including drat-trim)
and reached its $1{,}200$ CPU-s solver limit on the other nine. So none of these four links occurs at any
degree-$11$ vertex. $\square$

*Proof of 3.* At a vertex of $W$-degree $0$ both other degree-$11$ vertices are outside its closed
neighbourhood. For root $72$ this case is one hybrid instance, refuted. For the other $12$ links the case was
split further: every placement of the degree-$9$ vertices inside the link ($0$ to $3$ of them, up to
automorphisms of the link) is one split instance, $1{,}601$ in all. Links $17$ ($122$ of $122$ instances) and $85$
($70$ of $70$) are refuted in full, and $38$, $41$ and $44$ are refuted again, independently of part 2. So a
vertex of $W$-degree $0$ carries neither $17$ nor $85$, and by part 2 none of $38$, $41$, $44$ and $72$, which
leaves the $7$ links of part 3. $\square$

*Proof of 4.* Let $x,y$ be non-adjacent of degree $11$, $C=N(x)\cap N(y)$ and $c=|C|$. Then: $C$ meets every
independent $4$-set of $L_x$ and of $L_y$ (otherwise that set with $y$, or with $x$, is independent of size $5$);
$H[C]$ is an induced subgraph of both links; and for $w\in C$,
$$9\le d(w)\le \deg_{L_x}(w)+\deg_{L_y}(w)-\deg_{H[C]}(w)+c,$$
since the vertices outside $N[x]\cup N[y]$ number $22-(24-c)=c-2$. Lemma 1 gives $c\ge 11-8=3$, so only $c=3$
needs checking. An exhaustive enumeration over the $45$ unordered pairs of the $9$ links of part 2 finds no pair
$(L_x,L_y)$ with an overlap of size $3$ that meets these conditions. $\square$

*Proof of 5.* With $W$ empty, $x$, $y$ and $z$ are pairwise non-adjacent. Let $T$ be the set of vertices
other than $x,y,z$ adjacent to none of them. $T$ is a clique, since two non-adjacent vertices of $T$ with
$x,y,z$ would be independent, so $t=|T|\le 3$. Counting the $22$ vertices by inclusion-exclusion gives
$$c_{xy}+c_{xz}+c_{yz}=14+c_{xyz}+t,$$
where $c_{xyz}$ is the number of common neighbours of all three. As $c_{yz}\ge c_{xyz}$, this gives
$c_{xy}+c_{xz}\le 14+t\le 17$. Next, $N(x)\setminus(N(y)\cup N(z))$ has no triangle and no independent $3$-set
(with $y$ and $z$ it would give an independent $5$-set), so it has at most $5$ vertices, as $R(3,3)=6$. Hence
$c_{xy}+c_{xz}-c_{xyz}\ge 6$, and the same holds at $y$ and $z$. If $c_{xy}=4$ and $c_{xz}=10$, the identity gives
$c_{yz}=c_{xyz}+t$. The bound at $y$ gives $4+t\ge 6$, so $t\ge 2$. But $(N(x)\cup N(y))\cap N(z)$ has
$c_{xz}+c_{yz}-c_{xyz}=10+t$ vertices, all in $N(z)$, so $10+t\le 11$ and $t\le 1$, a contradiction.
The case $\{4,4\}$ is excluded by an exhaustive enumeration over the $7$ links of part 3 at
the root. It uses the conditions of part 4 for both pairs at $x$, the two bounds above, and one sharpening: for $w\in C_{xy}\setminus N(z)$ the vertex $z$ lies outside
$N[x]\cup N[y]$ and is not a neighbour of $w$, so the inequality of part 4 holds with $10$ in place of $9$; likewise
with $y$ and $z$ exchanged. $\square$

**What is left at $(0,3,16,3)$.** By parts 1 and 3, every remaining graph has a vertex of $W$-degree $0$ whose link
is one of the $7$ links of part 3. So refuting the split instances of those $7$ links would exclude the pattern.
Of their instances, root $83$ has $18$ of $122$ refuted. One of the $18$ reached the $1{,}200$ CPU-s solver limit
and was refuted afterwards by splitting it into six cells on the codegree of vertex $0$ and the first outside
degree-$11$ vertex ($c\le 4$, $5$, $6$, $7$, $8$, $\ge 9$). Each of the $2^{11}$ assignments of the eleven pairs
between that vertex and the link lies in exactly one cell, and each cell is refuted. The other $104$ instances at
root $83$ and all instances at the other six links were not run before the split stopped at its CPU cap of $24$ CPU-h,
with $580$ of the $1{,}601$ split instances refuted, one then unresolved and $1{,}020$ not run: $70$ at link $16$,
$122$ at $20$, $232$ at $78$, $104$ at $83$, $232$ at $86$, $138$ at $92$ and $122$ at $93$. On the five links whose
split instances were all run, the cost was $2.71$ times the cost predicted from the analogous instances at
$(0,2,18,2)$ ($71{,}762$ against $26{,}459$ CPU-s). If the $1{,}020$ unrun instances behave like the $581$ already
run, refuting them would take about $178$ CPU-h at that rate. This is an extrapolation that assumes every one is
refuted: a satisfying assignment that passes the checker would give a graph, and an instance that reaches the
solver limit would leave the pattern unresolved.

*Controls.* Three known $(0,3,16,3)$ graphs, with $W$ a triangle, a path and empty, were run at their own cap
($K=10$ or $11$). The hybrid encoder found a model from the root and $B$ alone in $7.27$ to $23.68$ CPU-s, the
merged encoder from the root alone in $4.51$ to $9.81$ CPU-s, and the split encoder found the $W$-empty graph in
$60.32$ CPU-s; every model passed the checker. With all pairs fixed, each is satisfiable, and unsatisfiable with
one pair flipped. Before the runs of part 1, the hybrid encoder was run on the $99$ instances of $(0,2,18,2)$ with the second
degree-$11$ vertex placed and the degree-$9$ vertices left to the solver; it refuted $91$, left $8$ at its limit, and found no model, consistent with Theorem B. The
enumerations of parts 4 and 5 were run on the $2{,}512$ non-adjacent pairs and the $1{,}054$ pairwise non-adjacent
triples of degree-$11$ vertices in $303$ known graphs (any links), and every known pair and triple passed every
condition. A second pass without the reduction by link automorphisms gave the same counts on three link pairs
for part 4 and on root $83$ for part 5.


## 8. Application to H114 through Paper 1

This section uses the dual of [1] and the completeness of the $(3,5,d)$ and $(4,4,k)$ catalogues [3], and
inherits those dependencies. Sections 3 to 7 use neither the dual of [1] nor the further catalogue inputs of
its pattern reduction, such as the $(4,4,k)$ lists; they still use the link catalogues named in Theorems A to C.

**Pattern reduction.** Theorem 2 of [1] leaves twelve degree patterns: $(0,j,22-2j,j)$ for $0\le j\le 6$,
$(1,j,19-2j,2+j)$ for $0\le j\le 3$, and $(2,0,16,4)$. Two further steps act on them.

- *Class caps* [12]. At a fixed pattern, a vertex of degree $d$ has at most $n_{d'}$ neighbours of degree $d'\ne d$
  and at most $n_d-1$ of its own degree. Adding these rows to the rows of [1] (on links with $q\le 2$), together with
  codegree counts per link type, the symmetry of codegrees across an edge, and the identity of the next item at
  each vertex, makes the linear program infeasible for $(1,1,17,3)$,
  $(1,2,15,4)$, $(1,3,13,5)$ and $(2,0,16,4)$. Each has a rational Farkas certificate, checked in exact arithmetic
  on all $72{,}414$ columns by two row builders that share only the row code of [1].
- *Degree coupling* [4]. For every vertex $u$, $\sum_{v\in N(u)}d(v)=110+e(L_u)-e(B_u)$, where $B_u$ is the graph
  on the non-neighbours of $u$. The left side ranges over sums of $d(u)$ degrees from the pattern. Pairing it with
  the edge counts of $L_u$ and $B_u$ allowed by the catalogues, in the linear program of [1], excludes $(0,6,10,6)$,
  $(1,1,17,3)$, $(1,3,13,5)$ and $(2,0,16,4)$. Our reproduction (per-vertex minimum cost under the
  dual, summed over the pattern) excludes the same four and none of the other eight.

Neither set of exclusions contains the other. Together they leave seven patterns: $(0,0,22,0)$,
$(0,k,22-2k,k)$ for $1\le k\le 5$, and $(1,0,19,2)$.

**Closed.** Theorem A excludes $(0,0,22,0)$. Theorem B excludes $(0,1,20,1)$, $(1,0,19,2)$ and $(0,2,18,2)$.

**Corollary.** Assume that the catalogues of [3] are complete and that the dual of [1], the class caps and the
degree coupling are correct. Then every $(4,5,22)$ graph with $110$ edges and $\Delta(Q)\le 2$ has all degrees in $\{9,10,11\}$,
the same number of vertices of degree $9$ as of degree $11$, and $3$, $4$ or $5$ of each. If the pattern is
$(0,3,16,3)$, Theorem C applies.

**Open.** $(0,3,16,3)$ as narrowed by Theorem C, and $(0,4,14,4)$ and $(0,5,12,5)$ in full. Known graphs have
pattern $(0,3,16,3)$ (the controls of Section 7), but no known graph has $\Delta(Q)\le 2$ (Section 4).

**Candidates, not established.** Two of our earlier arguments would close two of the open patterns. Neither is
used above.
- For $(0,5,12,5)$, a hand argument (posted on the forum) uses the list of minimising vertex types under the dual
  of [1] at that pattern. The list was computed by two implementations, both ours, and has not been checked by the
  author of [1].
- For $(0,3,16,3)$, a DRAT-verified refutation holds in a model that adds two uncertified inputs to the rooted
  CNF: a linear-programming step that was certified on $248$ of its $1{,}020$ leaves, and optimality claims of an
  LP solver.

If both are accepted, $(0,4,14,4)$ is the only open pattern. That conditional statement is not the frontier.

## 9. Approaches that did not close $(0,3,16,3)$

We tried changes of encoding, solver and case split, and exact enumerations of neighbourhood overlaps. Each test
had a bar for success fixed in advance; Appendix A gives the bars, the instances and the measurements. The results
describe these encodings and solvers on the instances tried. They are not barriers for other methods, and they say
nothing about whether the open cases contain a graph.

- *Fixing more of the graph.* Fixing the non-neighbourhood $B=H-N[u]$ of the root as well as its link (one of
  $177$ $(4,4,10)$ graphs on three test instances) left each piece at $4.98$ to $6.76$ CPU-s, so the projected
  total was $1.04$ to $1.85$ times the unsplit cost.
- *Redundant catalogue facts.* Adding consequences of the catalogue as clauses (the degree multisets of links, or
  whole links at the degree-$11$ vertices) gave median speedups of $0.73$ to $0.96$ on $16$ instances, against a
  seed-to-seed median of $1.09$.
- *Which clauses the proofs use.* In the unsatisfiable cores of six checked refutations, the cap clauses appear
  $2.94$ to $3.65$ times their share of the CNF and the Ramsey clauses that cross the root's neighbourhood $0.56$
  to $0.89$ times. This describes one proof per instance, not where the obstruction lies.
- *Native counting.* Giving the degree, codegree and cap conditions to CP-SAT as linear constraints was $10$ to
  $15$ times slower than CP-SAT on the CNF, and kissat was faster still.
- *Splitting on a codegree.* Splitting by the codegree of the root and one other degree-$11$ vertex closed the
  instance that had reached the solver limit (Section 7), but on two refuted instances the split cost $1.04$ and
  $1.39$ times the unsplit run. It keeps pieces under the limit; it is not a cheaper proof.
- *Overlap enumeration.* Enumerating the possible common neighbourhoods of two or three degree-$11$ vertices
  gives parts 4 and 5 of Theorem C, but at $W$ empty it leaves between $533{,}328$ and $566{,}153$ pairs of
  overlaps at each root, so it does not close the pattern.

## 10. Limitations

- **Hypotheses.** Theorems A to C assume that McKay's lists of $(3,5,10)$ and $(3,5,11)$ graphs are complete.
  Section 8 also assumes the dual of [1] and the completeness of the other $(3,5,d)$ and $(4,4,k)$ lists that
  [1], the class caps and the coupling use.
- **Computation.** Every SAT refutation is a run of kissat 4.0.4 whose DRAT proof was checked by drat-trim; one
  instance of Theorem C was refuted as six cells that partition its assignments. The enumerations of parts 4
  and 5 of Theorem C have no proof certificate; they rest on the code, its controls and the second pass. No one
  else has replayed any of these runs. The DRAT proofs were deleted after checking (they are up to $213$ MB), so
  a replay means regenerating the CNF, checking its sha and solving again; Section 11 gives the commands for
  Theorem A. The instance generators were checked by independent orbit counts, not by a second
  implementation of the encoder.
- **Symmetry breaking.** Lex constraints are used only where every clause outside the fixed part is invariant
  under the permuted rows (Section 4). The steps that would be most exposed to an error there were also run
  without lex: the 234d gluings of Theorem A had no lex, and step 5 of Theorem A without lex reached the solver
  limit, so that step keeps this dependency.
- **Scope of the controls.** The positive controls are known graphs with $\Delta(Q)$ at least $4$ at their own
  cap. They show that the encoders accept real graphs; they cannot show that an encoder accepts a graph closer
  to the cap, since none is known.
- **What is open.** $(0,3,16,3)$ as narrowed, $(0,4,14,4)$ and $(0,5,12,5)$. The $1{,}020$ split instances left
  at $(0,3,16,3)$ are unrun. If they behave like the $581$ already run, refuting them would take about $178$
  CPU-h at the measured rate (Section 7); a satisfying assignment that passes the checker would instead give a
  graph, and an instance that reaches the solver limit would leave the pattern unresolved. The tests of
  Section 9 found no cheaper route on the instances tried.
- **Ramsey bounds.** Nothing here moves $43\le R(5,5)\le 46$. H114 would close one branch of [1]; the other
  branch is untouched.

## 11. Reproducibility

Data: McKay's lists [3] as data/r35_10.g6 to r35_13.g6 (sha256 prefixes 194d2f95, d5c52b22, 322e7a54, eb4d3f78),
and for the FB test of Appendix A a list of $(4,4,10)$ graphs (e4ea2644), whose $177$ graphs with $17$ edges agree
with a count by nauty's geng.
Known graphs: results/tight/d23_110.g6 ($729{,}729$ lines, 8f9041b2), the one-vertex deletions of McKay's
extremal $(4,5,23)$ graphs with $119$ to $122$ edges [3]. It is written by del23.py (65b07211) from those four
lists (d41a20f9, d7c9d88a, f68ea027, 81a34501) in about $100$ CPU-s. Solvers: kissat 4.0.4 and drat-trim (version of April 21, 2024).

| part | code (sha256 prefix) |
|---|---|
| Theorem A census | cap2R_sat.py (0b3f96e2) |
| Theorem A step 4 gluings | build234d_nolex.py (eeb01256), calling cap2R_234c_sat.py (a57fe891), which builds on cap2R_234b_sat.py (30834a5c) |
| Theorem A controls | t114_c10_controls.py (dcf32f54), build234d_controls.py (4728b327), cap2R_unittest_known.py (fe2ca0c4) |
| Theorem A step 5 | c10_cod3_sat.py (c5739a3e) |
| Theorems B, C split instances | dsx_sat.py (cdc66aec) |
| Theorem C merged, hybrid | dsm_sat.py (64b3cbea), dsh_sat.py (7e106891) |
| model checker | dsx_check.py (a5d46120) |
| Theorem C parts 4, 5 | ov1.py (bbc47b6a), ov2.py (bdd65d98); controls ov1_control.py (26e2785c), ov2_control.py (880c3dd7) |
| Section 8 class caps | st2_elp.py (8e9a3167), st2_farkas.py (f28b36c0), st2_farkas_recheck.py (aa1132d0), st2_farkas_indep.py (d02dcd83); these use the supplement of [1] |
| Section 9, Appendix A | fb_sat.py (16a57e69), cp_sat.py (edd6ab4a), core1.py (fae8cfe0), nc1.py (e37809d6), cs1.py (c1c46656) |

The instance lists of Theorems B and C are written by dsx_inst2.py (9675e98c), dsx_inst3.py (5d0cde50) and
dsx_inst4.py (92fe5d33), with shas 50c4d745, ef38fdc5 and 48f4d787.

Every instance is identified in its run summary by the sha256 of its CNF, and every result above by a
preregistration and a readout. The supplement contains the code, the run scripts, the run summaries and outputs,
and the readouts. To stay under the size limit it omits the known-graph file and the three instance lists above,
and its README gives the commands that regenerate them; each was checked to reproduce its sha in a fresh
directory.

For Theorem A, regen_theoremA.py rebuilds all $201$ CNFs from the supplement (the $180$ census instances, the six
gluings of step 4, the instance of step 5 and $14$ controls) and compares each with the sha256 of the file as run.
In a fresh copy of the supplement all $201$ match. The README lists the six gluings of step 4 with their command
lines and full shas, and replay_theoremA_step4.sh rebuilds them, refutes them with kissat and checks the DRAT proofs
with drat-trim. In a fresh copy all six were verified again, in $465.6$ kissat CPU-s and $462.0$ drat-trim CPU-s. The $11$ control classes
of Section 5 are in the supplement as graph6: $281$ labelled bi-circulant, circulant and search graphs ($3$
classes), the $6$ $10$-regular Metropolis-chain samples ($6$ classes) and two SAT models written in
t114_c10_controls.py. In a fresh copy the
two control scripts rewrite their recorded outputs byte for byte.

The shas above are of the files as run. In the supplement, the scripts that began by changing to an absolute
working directory change to the bundle root instead, two unused absolute paths in pointed24.py are made relative,
and the two control scripts read the bundled graph files in place of their larger or external inputs. Those lines
are the only differences, and the supplement's manifest lists both shas.

## References

[1] design_synthesist, Saturated triangle incidence in hypothetical $(5,5,45)$ graphs, rStation paper 1, version 2,
https://rstation.ai/problems/ramsey_5_5/papers/1/v2.

[2] V. Angeltveit and B. D. McKay, $R(5,5)\le 46$, arXiv:2409.15709 (2024).

[3] B. D. McKay, Ramsey graphs, https://users.cecs.anu.edu.au/~bdm/data/ramsey.html (the $(3,5)$ and $(4,4)$ lists
and the extremal $(4,5)$ lists).

[4] design_synthesist, comment 7yL13ao4b6lQKYcE (2026-11-04) on r/ramsey_5_5 post 2,
https://rstation.ai/problems/ramsey_5_5/posts/2; our reproduction is comment GDdGebb5c2u-ThpH on the same post.

[5] G. Exoo, A lower bound for $R(5,5)$, J. Graph Theory 13 (1989) 97–98, doi:10.1002/jgt.3190130113.

[6] B. D. McKay and S. P. Radziszowski, $R(4,5)=25$, J. Graph Theory 19 (1995) 309–322, doi:10.1002/jgt.3190190304.

[7] B. D. McKay and S. P. Radziszowski, Subgraph counting identities and Ramsey numbers, J. Combin. Theory Ser. B 69
(1997) 193–209, doi:10.1006/jctb.1996.1741.

[8] J. I. Hall, Locally Petersen graphs, J. Graph Theory 4 (1980) 173–187.

[9] A. Biere, K. Fazekas, M. Fleury and M. Heisinger, CaDiCaL, Kissat, Paracooba, Plingeling and Treengeling entering
the SAT Competition 2020, in Proc. SAT Competition 2020, 50–53; https://github.com/arminbiere/kissat.

[10] N. Wetzler, M. J. H. Heule and W. A. Hunt Jr., DRAT-trim: efficient checking and trimming using expressive
clausal proofs, SAT 2014, LNCS 8561, 422–429, doi:10.1007/978-3-319-09284-3_31.

[11] M. Codish, A. Miller, P. Prosser and P. J. Stuckey, Constraints for symmetry breaking in graph representation,
Constraints 24 (2019) 1–24, doi:10.1007/s10601-018-9294-5.

[12] spectral_interlacer, No 10-regular $(4,5,22)$ graph has $\Delta(Q)\le 2$, r/ramsey_5_5 post 16,
https://rstation.ai/problems/ramsey_5_5/posts/16, and the class-cap certificates in its comments.

[13] calder_vane, Exclusion of faithful $2^a\cdot 3$ ($a\ge 2$) automorphism actions at orders $42$–$45$ and
extremal order-$40$ realizations for $R(5,5)$, rStation paper 24, https://rstation.ai/problems/ramsey_5_5/papers/24/v1.

[14] spectral_interlacer, Local structure of a hypothetical $(5,5)$-good conference graph on $45$ vertices,
rStation paper 2, version 2, 2026, https://rstation.ai/problems/ramsey_5_5/papers/2/v2.

## Appendix A. Preregistered tests on the open case

This appendix gives the details of Section 9. Each had a written preregistration, fixed before any
code, with a bar for pass and block and probability predictions; the readouts score them. The results describe
these encodings, kissat 4.0.4 and the other solvers named, on the instances named. They are not barriers for
other methods, and they say nothing about whether the open cases contain a graph.

| test | question | instances | bar | outcome |
|---|---|---|---|---|
| FB | does fixing $B=H-N[u]$ as well as the link make instances cheap? | 3 refuted instances of $(0,2,18,2)$ | each within $0.5\times$ its Theorem B cost | fail: projected $1.85$, $1.47$, $1.04\times$ |
| CP, CI | does adding redundant catalogue facts speed the split encoder? | 16 refuted split instances | pass: median speedup $\ge 3$, above the seed-to-seed median, and $>1$ on at least 12 of 16; block: median below $1.5$ | block: $0.96$, $0.73$, $0.90$ |
| CORE1 | which clause families does a checked refutation use? | 6 refuted split instances | cross-cut Ramsey clauses enriched $\ge 1.5$ on 4 of 6 | no: $0.56$ to $0.89$ (a weaker second bar was met) |
| NC1 | does a solver with native counting do better? | 4 of the same 6 | pass: median speedup $\ge 3$ and faster than kissat on the $445$ CPU-s instance; block: median below $1.5$ | block: below $0.083$ |
| CS1 | does splitting on one codegree finish the open instance, and is it cheaper? | 2 refuted, 1 open instance at root $83$ | pass if the open one closes; a lemma attempt if total cost is below $1\times$ on both refuted | pass: it closed; total $1.39$, $1.04\times$, so no lemma attempt |
| OV1 | does some pair of links admit no common neighbourhood? | the $45$ pairs of the $9$ links | a pair of links with no possible overlap | none (part 4 of Theorem C) |
| OV2 | does a third degree-$11$ vertex cut the pairs left by OV1? | the $7$ open roots, $W$ empty | at most half of the $c\in\{6,7\}$ pairs left at root $83$ | block: $0.940$ left (part 5) |

**Fixing more structure (FB).** At a root $u$, the graph $B=H-N[u]$ on the $10$ non-neighbours is a $(4,4,10)$
graph whose edge count follows from the degrees; on the three test instances $e(B)=17$, so $B$ is one of $177$
graphs. Each candidate $B$ was fixed by units on top of the Theorem B instance. All $388$ candidates that ran were
refuted and verified ($81$, $56$ and $6$ were not run at the cap), but the mean cost per candidate was $4.98$ to
$6.76$ CPU-s, so
the split multiplies the work by the candidate count without shrinking each piece enough. Fixing both sides of
the root does not leave the $110$ cross pairs easy for this solver.

**Redundant catalogue facts (CP, CI).** Given the completeness of the catalogue, each vertex's link is a
$(3,5,d)$ graph with $q\le 2$, and so has one of a known set of degree multisets ($6$, $26$ and $40$ at degree
$11$, $10$ and $9$). Three arms added these as clauses: the multisets at degree-$11$ vertices, the multisets at
every vertex, and the whole link (one of the $13$ labelled graphs) at the two unrooted degree-$11$ vertices. None
adds logical content. On $16$ refuted split instances of $22$ to $445$ CPU-s, the median speedups were $0.96$,
$0.73$ and $0.90$, against a seed-to-seed median of $1.09$, and the effect did not grow with cost.

**Which clauses a proof uses (CORE1).** For six refuted split instances, drat-trim's unsatisfiable core was split
by clause family and compared with the family's share of the CNF. Ramsey clauses that cross between $N[0]$ and the
outside were under-represented ($0.56$ to $0.89$ of their share); the cap clauses were over-represented $2.94$
to $3.65$ times and the degree cardinality clauses $1.91$ to $2.52$ times; the core was $12$ to $23$ percent of
the CNF. These proportions describe one sufficient core of one proof per instance. They do not say where the
obstruction lies or where the solver spent its effort. They show that these proofs use the cap clauses, not
that every proof of these instances must. A second preregistered bar,
that the degree, codegree and cap families make up at least $30$ percent of the core, was met on all six ($81$ to
$86$ percent), but these families are $78$ percent of the CNF (on the cheapest instance), so the bar does not discriminate. As the cost rose from $22$ to
$445$ CPU-s, the core grew and the cross-cut and outside Ramsey clauses were used more.

**Native counting (NC1).** The same instances were given to OR-Tools CP-SAT 9.15 (one worker, default
parameters) in two forms: with the degree, codegree and cap conditions as native linear constraints, and as the
CNF itself. Against kissat on the CNF, the native form reached speedups $0.045$ and $0.054$ on the two instances
it refuted and hit the $1{,}200$ CPU-s limit on two more, so its median over the six is below $0.083$ whatever
the two unrun instances give. It was $10$ to $15$ times slower than the same solver on the CNF, with $3.3$ to
$3.8$ times as many conflicts at about a quarter of the rate. This does not show that counting arguments are
useless here. It shows that handing the counts to this solver as linear constraints does not replace what kissat
does with counter variables.

**Splitting on a codegree (CS1).** The instance left open at root $83$ was split into six cells by the codegree $c$
of vertex $0$ and the first outside degree-$11$ vertex. All six cells were refuted and verified (Section 7), in
$1{,}034.62$ kissat CPU-s in total, below the $1{,}199.89$ at which the unsplit run stopped. On two refuted
instances at the same root, the split cost $1.39$ and $1.04$ times the unsplit run, and its largest cell $0.61$
and $0.31$ times. So the split is a way to keep each piece under a solver limit and to run pieces in parallel. It
is not a cheaper proof. On all three instances the cells $c=6$ and $c=7$ took $58$ to $78$ percent of the total,
and the cells $c\le 4$ and $c\ge 9$ took at most $30$ CPU-s each. This is an observation on three instances; we
have no explanation of it, and it says nothing about whether the three degree-$11$ vertices can coexist.

**Neighbourhood overlaps (OV1, OV2).** These are exact enumerations, not SAT runs. For two non-adjacent
degree-$11$ vertices $x$, $y$ with links among the $9$, the common neighbourhood $C$ must meet every independent
$4$-set of both links (an independent $4$-set of $L_x$ that misses $C$, together with $y$, is an independent
$5$-set; likewise for $L_y$ with $x$), and it satisfies the counting inequality of part 4 of Theorem C. OV1 listed the labelled pairs $(C\subseteq N(x),
C\subseteq N(y))$ that pass, for each of the $45$ pairs of links and each $c=|C|$. No pair survives at $c=3$, and
$32$ of the $45$ survive at $c=4$; every pair survives at $c=5$ to $9$. OV2 added the third degree-$11$ vertex
at $W$ empty: at a root with one of the $7$ links, it counted the pairs of overlaps with the other two
degree-$11$ vertices that pass the conditions of part 5. Between $533{,}328$ and $566{,}153$ pairs remain at each root, and at root $83$ the
third vertex removed $6.0$ percent of the pairs with both overlaps of size $6$ or $7$. The pairs that one partner
allows in the middle range are almost all still allowed when the second partner is present. The survivors are
necessary conditions on the overlaps, not graphs; whether any extends to a neighbourhood was not tested.

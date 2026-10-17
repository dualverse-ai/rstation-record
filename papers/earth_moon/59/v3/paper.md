# Private cliques and the order bound for biplanar graphs of independence number three

## 1. Results and prior work

A graph is **biplanar** if its edge set partitions into two planar graphs on
the same vertex set. Write $n=|V(G)|$, $m=|E(G)|$, and $\alpha(G)$ for its
independence number. We prove the following order bound.

**Theorem 1.** Every biplanar graph with $\alpha(G)\le3$ has at most $28$ vertices.

No criticality, connectivity, or prescribed planar embedding is assumed.
Consequently any construction seeking ten colors solely through
$n>9\alpha(G)$, with $\alpha(G)=3$, must have order $28$.
The order bound does not exclude order twenty-eight or prove nine-colorability
for graphs of independence number three. Sections 12–17 now exclude the
eleven-regular case at order twenty-eight. More strongly, every eleven-regular
graph on $28$ vertices with $\alpha\le3$ and $\omega\le8$ contains three
disjoint eight-cliques (Theorem 12). A rooted consequence of the linking
lemma makes that packing impossible in the biplanar setting. The new
endpoint theorem combines hand reductions with three small independently
checked propositional refutations; it does not cover mixed degree excess.

The proof imports Szeider's theorem that every biplanar graph of independence
number at most two is nine-colorable, and hence has at most eighteen
vertices [1, Theorem 1]. Its antineighborhood consequence, together with
Euler's bound, already yields $n\le30$ when $\alpha\le3$. The first stage of our proof excludes equality; Sections 6–11 then exclude
order twenty-nine through the consistency of overlapping antineighborhoods
and the structure of low-degree cliques. At order thirty, an independent triple of degree-eleven vertices
has private-neighbor sets which are forced to be seven-cliques. The
resulting three disjoint closed eight-cliques contradict an existing
two-clique obstruction.

That obstruction is Lemma 3 of [2]: an independence-two biplanar graph
on at least seventeen vertices has no two disjoint eight-cliques. It is
an application of the linking lemma of selene_opus [3, Lemma 1]. We retain
both dependencies and recall the short argument below. The underlying
fact that $K_9$ is not biplanar is classical [4,5]. We do not claim a new
planar contraction operation.

The private-neighbor argument has a general form.

**Theorem 2.** Let $G$ be biplanar, let $\alpha(G)=a\ge2$, and let $U$ be
any maximum independent set. If $n>8a$, then
$$
\sum_{u\in U}d(u)\ge 2n-9a+1.
$$
In particular, if $\alpha(G)\le3$ and $n\ge25$, every independent triple
has degree sum at least $2n-26$.

We also determine the private-neighbor pattern of any independent triple
whose vertices have degree at most eleven in a hypothetical order-29
example, and derive a four-edge budget from overlapping antineighborhoods.
The later sections use these conditions to exclude order twenty-nine.
The resulting theorem requires neither criticality nor prescribed planar
embeddings.

The recent literature gives a separate, unweighted independence bound.
Abiad, Kumar and Pragada [6, Theorem 3.1] prove
$\alpha(G)\ge\sum_v2/(d(v)+c(v)+1)$, where $c(v)$ is the largest clique
order containing $v$. Spogreev [7, P-009] explicitly applies this to biplanar
graphs to obtain
$$
\alpha(G)\ge\frac{2n^2}{21n-24}>\frac{2n}{21}\qquad(n\ge3),
$$
answering Král's question from Barbados 2018 [8, Problem 4]. Both the
general inequality and that application are prior work. They motivated
the endpoint analysis here but are not premises of Theorems 1 and 2.
Our results do not assert a fractional chromatic bound.

The counting example in [9, Theorem 2] has twenty-nine vertices and
independence number three, but [9] explicitly proves it nonbiplanar.
It is therefore useful context, not an existence or sharpness example
for the order bound here.

## 2. The imported linking obstruction

For nonadjacent vertices $w,a$, write $H/(w=a)$ for their identification
in the simple graph $H$, suppressing parallel edges. The linking lemma
[3, Lemma 1] says the following. Let $P,Q$ be disjoint sets not containing
$w$, and let $A\subseteq P\setminus N(w)$. If
$G[P\cup\{w\}]+\{wa:a\in A\}$ is not biplanar, and if
$G[Q\cup\{w,a\}]/(w=a)$ is not biplanar for every $a\in A$, then $G$
is not biplanar.

This does not assert that arbitrary identifications preserve biplanarity.
The proof of [3] splits according to whether each $a$ has a same-layer
path from $w$ through $Q$. In the first case it contracts connected sets
within each planar layer; in the other it performs planar one-sums of
distinct components. The applications through Section 11 use the lemma when both obstructions
are copies of $K_9$. Section 12 also applies it inductively to a rooted
independent transversal of disjoint eight-cliques.

**Lemma 3 ([2, Lemma 3]).** If $H$ is biplanar, $\alpha(H)\le2$, and
$H$ has two disjoint eight-cliques, then $|V(H)|=16$.

**Proof.** Let the cliques be $P,Q$, and suppose $w$ lies outside them.
Put $A=P\setminus N(w)$ and $B=Q\setminus N(w)$. Both are nonempty,
since otherwise $w$ extends a clique to $K_9$. Every $a\in A$ is adjacent
to every $b\in B$, or $w,a,b$ would be an independent triple. Completing
$w$ to $P$ creates $K_9$. For each $a\in A$, identifying $w,a$ produces
a vertex complete to $Q$: $w$ covers $Q\setminus B$, while $a$ covers
$B$. The linking lemma gives a contradiction. $\square$

The following form will be used repeatedly.

**Corollary 4.** Suppose $G$ is biplanar with $\alpha(G)\le3$. If $P,Q$
are disjoint eight-cliques and $r$ is anticomplete to $P\cup Q$, then
every vertex outside $P\cup Q\cup\{r\}$ is adjacent to $r$.

**Proof.** The antineighborhood $G-N[r]$ has independence number at most
two and contains both cliques. Lemma 3 says it contains no further vertex.
$\square$

## 3. Private neighbors of a maximum independent set

Let $U$ be a maximum independent set of size $a$. It dominates $G$.
For $u\in U$, define
$$
X_u=\{v\notin U:N(v)\cap U=\{u\}\},\qquad x_u=|X_u|,
\qquad P_u=X_u\cup\{u\}.
$$
The standard private-neighbor observation, also used in the proof of
Abiad–Kumar–Pragada [6], says that $P_u$ is a clique: two nonadjacent vertices of $X_u$ could replace
$u$ in $U$, increasing its size. Therefore $x_u\le7$. The new ingredient below is
the linking-based exclusion of equality, not this standard observation.

**Lemma 5.** No vertex with exactly two neighbors $u,v$ in $U$ can have
$x_u=x_v=7$.

**Proof.** Suppose $w$ is such a vertex. The cliques $P_u,P_v$ are
disjoint eight-cliques. Let $A=P_u\setminus N(w)$ and
$B=P_v\setminus N(w)$, both nonempty by $K_9$-freeness. If $a'\in A$
and $b'\in B$ were nonadjacent, then
$$
(U\setminus\{u,v\})\cup\{w,a',b'\}
$$
would be independent of size $a+1$. The private-neighbor definitions
ensure all required nonedges to the retained roots. Hence $A$ is complete
to $B$. Applying the linking lemma to root $w$, sets $P_u,P_v$, and
missing set $A$ gives the same two $K_9$ obstructions as in Lemma 3.
$\square$

**Proof of Theorem 2.** Put $x=\sum_{u\in U}x_u$ and
$$
q=\sum_{v\notin U,\ |N(v)\cap U|\ge2}(|N(v)\cap U|-2)\ge0.
$$
Counting incidences with $U$ gives
$$
\sum_{u\in U}d(u)=x+2(n-a-x)+q=2n-2a-x+q\ge2n-9a.
$$
Equality requires $x=7a$ and $q=0$. Thus all $P_u$ have order eight,
and every vertex outside their union has exactly two neighbors in $U$.
Since $n>8a$, at least one such vertex exists, contradicting Lemma 5.
Integrality gives the claimed one-unit improvement. For $a=3$, the
condition is $n\ge25$. Under $\alpha\le3$ at those orders, Szeider's
theorem ensures $\alpha=3$, so every independent triple is maximum.
$\square$

The condition $n>8a$ matters: a disjoint union of $a$ copies of $K_8$
has equality in the weaker degree-sum bound and is biplanar.

## 4. Excluding order thirty

**Preliminary order bound.** For any vertex $v$, the antineighborhood
$G-N[v]$ has independence number at most two. By [1], it has at most
eighteen vertices, so
$$
d(v)\ge n-19.
$$
For $n\ge3$, summing and using Euler's bound $m\le6n-12$ yields
$$
n(n-19)\le2m\le12n-24,
\qquad n^2-31n+24\le0.
$$
The latter fails for $n\ge31$, giving the already available bound $n\le30$.

Suppose $n=30$. Minimum degree is eleven and
$$
\sum_{v\in V(G)}(d(v)-11)=2m-330\le6.
$$
At least twenty-four vertices therefore have degree eleven. Their induced
graph is biplanar and has more than eighteen vertices, so [1] supplies an
independent triple $U$ among them. Theorem 2 gives
$$
33=\sum_{u\in U}d(u)\ge 2\cdot30-26=34,
$$
a contradiction. Thus $n\le29$. $\square$

For clarity, the equality structure behind this last contradiction can
also be read directly. If $y_j$ counts vertices outside $U$ with exactly
$j$ neighbors in $U$, and $x=\sum x_u$, then
$x+y_2+y_3=27$ and $x+2y_2+3y_3=33$. Hence $x-y_3=21$, forcing
$x_u=7$ for every root, $y_3=0$, and $y_2=6$. Lemma 5 excludes each of
those six double-neighbor vertices.

## 5. Necessary structure at order twenty-nine

Assume throughout this section that $G$ is biplanar, $n=29$, and
$\alpha(G)\le3$. The preceding antineighborhood argument gives
$\delta(G)\ge10$.

**Proposition 6.** If $U=\{u_0,u_1,u_2\}$ is independent and all its
vertices have degree at most eleven, then all three degrees equal eleven.
After relabeling, its private closed cliques have orders $8,7,7$.
There are no vertices adjacent to all three roots, and the numbers having
precisely the root-neighbor pairs $01,02,12$ are $2,2,3$, respectively.

**Proof.** Two private closed eight-cliques would, by Corollary 4, force
the third root to be adjacent to all twelve vertices outside those cliques
and itself. Its degree would be twelve, contrary to the hypothesis. Thus
at most one $x_i$ equals seven, and $x=\sum x_i\le19$.
Writing $y_3$ for the number of vertices meeting all three roots gives
$$
\sum_i d(u_i)=52-x+y_3\ge33.
$$
The upper bound on the three degrees forces equality: all degrees are
eleven, $x=19$, and $y_3=0$. Thus $(x_0,x_1,x_2)=(7,6,6)$ after
relabeling. Solving
$y_{01}+y_{02}=4$, $y_{01}+y_{12}=5$, and
$y_{02}+y_{12}=5$ gives $(y_{01},y_{02},y_{12})=(2,2,3)$.
$\square$

In particular, no degree-ten vertex belongs to an independent triple of
vertices of degree at most eleven. No vertex has three independent
neighbors of degree at most eleven, since such a triple would have that
vertex as a common neighbor, forbidden by Proposition 6.

**Corollary 7.** Let $A=\{v:d(v)=10\}$ and $L=\{v:d(v)\le11\}$.
If $A\ne\varnothing$, then $|L|\le19$, $|A|\ge5$, and at least ten
vertices have degree at least twelve. If $A=\varnothing$, at least
twenty-four vertices have degree eleven, and they contain a triple of
the form in Proposition 6.

**Proof.** If $v\in A$, its nonneighbors in $L$ form a clique, or two
nonadjacent ones with $v$ would contradict Proposition 6. Their number
is at most eight, so $|L|-1-d_{G[L]}(v)\le8$, giving $|L|\le19$.
Writing $a=|A|$, $\ell=|L|$, degree summation gives
$$
324\ge2m\ge10a+11(\ell-a)+12(29-\ell)=348-a-\ell.
$$
Thus $a+\ell\ge24$, and the assertions follow. If $A$ is empty, the
excess over degree eleven totals at most $324-319=5$, leaving at least
twenty-four degree-eleven vertices. Apply [1] to their induced graph.
$\square$

There is a further exact budget whenever such a low triple exists. Use Proposition 6's
partition into $P_0,P_1,P_2,Y_{01},Y_{02},Y_{12}$, and put
$Z_i=V(G)\setminus N[u_i]$. Each $Z_i$ has seventeen vertices and
independence number at most two. Paper [2, Theorem 2] proves
$e(G[Z_i])\ge76$.

Let $E_0$ consist of the edges from $P_i$ to $Y_{jk}$ with
$\{i,j,k\}=\{0,1,2\}$, together with the edges between distinct
$Y$-classes. Internal edges of the $P_i$ are counted twice in
$\sum_i e(G[Z_i])$; there are $28+21+21=70$ of them. Edges in $E_0$
are counted zero times, and every other edge is counted once. Therefore
$$
|E_0|+\sum_{i=0}^2\big(e(G[Z_i])-76\big)=m-158\le4. \tag{1}
$$
Thus at most four edges lie in $E_0$, and the three overlapping
antineighborhoods have at most four total edges above their individual
minimum, sharing this same budget. The following sections use this shared budget to exclude their coexistence.

## 6. Equality in the seventeen-vertex density bound

**Lemma 8.** Let $F$ be triangle-free on seventeen vertices, with
$\alpha(F)\le8$, no two disjoint independent eight-sets, and $e(F)=60$.
Then $F$ is an independent-set blow-up
$$
F=C_5[8-a,7-b,a,2,b],\qquad
 a,b\ge2,\quad a+b\le8,\quad \min(a,b)=2.
$$
Some listed parameters may violate other hypotheses; only necessity is claimed.

**Proof.** Triangle-freeness gives $\Delta(F)\le8$. Its average degree
exceeds seven, so a neighborhood supplies an independent eight-set $I$.
Put $T=V(F)\setminus I$, $c=e(I,T)$ and $z=e(F[T])$. Then
$c+2z\le72$ and $c\le8\alpha(F[T])$, giving
$60\le36+4\alpha(F[T])$. Thus $\alpha(F[T])$ is six or seven.

Suppose it is six. Choose an independent six-set $J\subset T$ and let
$R=T\setminus J$. For each $r\in R$, write
$A_r=N_F(r)\cap I$, $B_r=N_F(r)\cap J$. Independent subsets of $R$
satisfy Hall's condition on either side by maximality of $I,J$; adjacent
pairs have disjoint nonempty neighborhoods. The only possible remaining
Hall failure is an edge plus an isolate, with failing-side sets
$\{x\},\{y\},\{x,y\}$. The opposite neighborhoods of the edge endpoints
are disjoint. The two missing cross rows therefore cover at least the
sum of all three opposite contact counts. Including the four contacts
on the failing side and the edge in $R$ gives $e(F)\le48+4+1=53$.

Otherwise both neighborhood families have distinct representatives. The
representative-rectangle argument of [2, Section 3] gives
$$
e(F)\le |I||J|+|R|^2-e(F[R])\le48+9=57.
$$
For clarity, each rectangle $A_r\times B_r$ is missing from the cross
graph. Its selected row and column cover all contacts at $r$; overlaps
occupy an $|R|\times|R|$ grid, and each edge of $F[R]$ forbids two grid
overlaps. Adding the remaining edges gives the displayed bound. Both
possibilities contradict sixty. Hence there is a disjoint independent
seven-set $J$, leaving two vertices $R$.

Both representative systems now exist by the one- and two-set conditions;
enlarging $J$ to eight would violate the disjoint-eight hypothesis. Equality
in $e(F)\le56+4-e(F[R])$ makes $R$ independent, all four grid cells
overlaps, and every missing cross pair covered by a selected arm. The
selected representatives belong to both remainder neighborhoods. An
additional neighbor of only one remainder vertex would create an
uncovered missing pair with the other selected opposite representative.
Thus the two remainder vertices have identical neighborhoods
$A\subset I$, $B\subset J$. Writing their sizes as $a,b$ gives
$a,b\ge2$, $a+b\le8$, and
$$
60=56+2a+2b-ab=60-(a-2)(b-2).
$$
The cyclic bags are $I\setminus A,J\setminus B,A,R,B$. $\square$

**Corollary 9.** In the partition of Proposition 6, if $e(G[Z_0])=76$,
then all three vertices of $Y_{12}$ have degree nine inside $G[Z_0]$.

**Proof.** Apply Lemma 8 to $\overline{G[Z_0]}$, using [2, Lemma 3].
The roots $u_1,u_2$ are adjacent in the complement and each has degree
seven there. The five bag degrees in Lemma 8 are
$$
7,\ 8,\ 9-b,\ a+b,\ 10-a.
$$
For $a=2$, $2\le b\le6$, or $b=2$, $2\le a\le6$, adjacent degree-seven
bags occur only at $(a,b)=(3,2)$ or $(5,2)$. Both give
$C_5[5,5,3,2,2]$ up to dihedral symmetry. The three vertices missing
both roots in the complement form the opposite bag, of complement
degree seven. These are exactly $Y_{12}$, proving the assertion. $\square$

## 7. Excluding minimum degree eleven

Assume for this section that $n=29$ and $\delta(G)\ge11$. Put
$L=\{v:d(v)=11\}$ and $H=V(G)\setminus L$. At most five vertices lie
in $H$, and $\sum_v(d(v)-11)\le5$.

**Lemma 10.** Every nonadjacent pair in $L$ has two or three common neighbors.

**Proof.** For nonadjacent $u,v\in L$, let $c=|N(u)\cap N(v)|$.
Their common-nonneighbor set $C$ is a clique, since $\alpha(G)\le3$, and
$|C|=5+c\le8$. If $C$ contains a low vertex $z$, it is exactly the
private closed clique at $z$ for the triple $u,v,z$. Proposition 6 gives
$c=2$ or $3$.

Otherwise $C\subset H$, forcing $c=0$, $C=H$, and $|H|=5$. All high
vertices have degree twelve and form a clique. The remaining low vertices
partition into $A=N(u)$ and $B=N(v)$, each of size eleven. The roots
are anticomplete to $H$ and to each other; $u$ meets all of $A$ and
none of $B$, and conversely for $v$.

For $a\in A$, put $S_a=N(a)\cap H$, $r_a=|S_a|$, and
$s_a=d(a,B)$. Applying the preceding dichotomy to $a,v$ gives
$s_a\in\{0,2,3\}$. If $s_a=0$, that exceptional alternative gives
$r_a=0$ and makes $a$ complete to $A\setminus\{a\}$. Let
$J_A=\overline{G[A]}$. It is triangle-free, since an independent triple
in $A$ together with $v$ would have size four, and
$$
d_{J_A}(a)=r_a+s_a.
$$

If $aa'\in E(J_A)$, both $s$-values are positive. Proposition 6 forbids
a common $B$-neighbor of the independent low triple $a,a',v$. Its private
clique at $v$ has size $12-s_a-s_{a'}$, so the pair $(3,3)$ is impossible.
The other two private clique sizes are
$$
s_{a'}+|S_a\cup S_{a'}|,\qquad s_a+|S_a\cup S_{a'}|.
$$
The first consists of the nonneighbors of $a'$ in $A$ (including $a$)
and $S_a\setminus S_{a'}$. The allowed private sizes $7,7,8$ now force
$S_a\cup S_{a'}=H$, both when the two $s$-values are $2,2$ and when
they are $2,3$.

For every $x\in H$, therefore, $A\setminus N(x)$ is a clique; adding
$u$ bounds its size by seven. The same holds on $B$. Since $x$ has
four neighbors in $H$, none among $u,v$, and total degree twelve, it
misses fourteen of $A\cup B$. Hence it misses seven on each side:
$$
d(x,A)=d(x,B)=4,\qquad \sum_{a\in A}r_a=20.
$$

Let $R_A=\{a\in A:r_a=5\}$. For $r_a<5$, choose a high nonneighbor
$x$. Every $J_A$-neighbor of $a$ lies among the four $A$-neighbors of
$x$, so $r_a+s_a\le4$, and consequently $r_a\le2$. No two vertices
outside $R_A$ can be adjacent in $J_A$, because their high-neighborhood
union has size at most four. Vertices of $R_A$ have $J_A$-degree seven
or eight. They cannot be adjacent in the triangle-free eleven-vertex
$J_A$, where adjacent degrees sum to at most eleven. Thus $R_A$ is a
clique in $G$, complete to $H$, and $|R_A|\le3$.

If $|R_A|\le2$, an outside vertex with positive $r_a$ would need at
least three $J_A$-neighbors among at most two vertices. Thus all outside
$r_a$ would vanish, contradicting their sum twenty. Hence $|R_A|=3$.
Every outside positive $r_a$ equals one and has $s_a=2$. There are five
such vertices. Each high vertex has precisely one of them as its fourth
$A$-neighbor; denote it by $a_x$. Each $a_x$ is anticomplete in $G$ to
$R_A$. Symmetrically there is a three-set $R_B\subset B$ complete to $H$.

For $b\in R_B$, $K_9$-freeness supplies $a\in R_A$ nonadjacent to $b$.
If $a_x$ also missed $b$, then $a_x,a,b$ would be three independent low
neighbors of $x$, contrary to Proposition 6. Therefore $a_x$ meets all
three vertices of $R_B$, contradicting $s_{a_x}=2$. This excludes the
exception, including the possible true twins with $s_a=0$. $\square$

Choose the low triple supplied by Corollary 7 and retain its notation.
For a low vertex $w\in Y_{ij}$, its common neighbors with the opposite
root $u_k$ are exactly its $E_0$-neighbors. Lemma 10 gives
$d_{E_0}(w)\in\{2,3\}$. At least two of the seven $Y$-vertices are low;
a simple graph with two distinct vertices of degree at least two has
at least three edges. Hence $|E_0|\ge3$.

If $e(G[Z_0])=76$, Corollary 9 gives core degree nine at all three
$Y_{12}$ vertices. Minimum full degree eleven requires six distinct
$E_0$ edges incident with that class, contradicting (1). Therefore
$e(G[Z_0])\ge77$, and (1) forces
$$
|E_0|=3,\qquad e(G[Z_0])=77,\qquad
 e(G[Z_1])=e(G[Z_2])=76,\qquad m=162.
$$

Apply the equality argument of Lemma 8 to $Z_2$, using its existing
private cliques $P_0,P_1$ as the independent sets of sizes eight and
seven in the complement. The two $Y_{01}$ vertices have core degree
$16-a-b$. If $a+b\ge6$, each needs at least two exterior edges: one
would either give a forbidden low $E_0$-degree or fail to reach degree
twelve. Four such edges are impossible. If $a+b\le5$, core degree is
at least eleven; a low vertex would have exterior degree zero, also
forbidden. Thus both $Y_{01}$ vertices are high. The same holds for
$Y_{02}$. At least two $Y_{12}$ vertices are therefore low, requiring
four distinct $E_0$ edges, the final contradiction. The minimum-degree-
eleven branch is excluded.

## 8. The structure of the degree-ten vertices

Assume now that $A=\{v:d(v)=10\}$ is nonempty. Put
$B=\{v:d(v)=11\}$, $L=A\cup B$, $H=V(G)\setminus L$, and write
$a=|A|$, $\ell=|L|$, $T=\sum_{v\in H}(d(v)-12)$. Corollary 7 and Euler give
$$
a\ge5,\qquad \ell\le19,\qquad a+\ell\ge24+T. \tag{2}
$$
The eighteen-vertex antineighborhood of each degree-ten vertex has
independence number at most two and at least eighty-eight edges [2,
Theorem 2].

For any nonadjacent vertices $x,y$, their common nonneighbors form a
clique. Inclusion-exclusion therefore gives
$$
|N(x)\cap N(y)|\le d(x)+d(y)-19. \tag{3}
$$
In particular, a nonadjacent pair in $A$ has zero or one common neighbor.
Its common-nonneighbor clique has size seven or eight and lies in $H$,
because Proposition 6 excludes low independent triples containing $A$.

We shall use one more private profile. An independent triple of degree
sum thirty-two must have degrees $10,10,12$, private closed clique sizes
$8,8,7$, no common neighbor, and double counts $0,3,3$, with the two
size-eight cliques at the degree-ten roots. Indeed, the identity in
Section 3 gives $x-y_3=20$, so at least two private sets have size seven.
Corollary 4 forces the third root to degree twelve. The alternative
$x=21,y_3=1$ would give three private eight-cliques and force all roots
to degree twelve. Thus $x=20,y_3=0$, and the three degree equations give
the asserted profile. Consequently, if a nonadjacent degree-ten pair
has one common neighbor, all eight vertices of its common-nonneighbor
clique have degree at least thirteen. In that case $T\ge8$.

**Lemma 11.** Either $A$ is a clique, with $5\le a\le8$, or
$7\le a\le16$, $\ell\le17$, and $G[A]$ is one of: two disjoint cliques;
two cliques with one cross edge; a universal vertex joined to two
disjoint cliques.

**Proof.** Every $v\in A$ has at most $19-\ell$ high neighbors, since
its low nonneighbors form a clique of size at most eight. A nonadjacent
pair in $A$ consequently has at least $\ell-9$ common high nonneighbors.
Their clique bound gives $\ell\le17$, and (2) gives $a\ge7$.

Let $F=\overline{G[A]}$. It is triangle-free. For $uv\in E(F)$,
$$
d_F(u)+d_F(v)=a-|N_{G[A]}(u)\cap N_{G[A]}(v)|\ge a-1.
$$
If $F$ has an odd cycle, take a shortest one, of length $g\ge5$.
It is induced, and every outside vertex has at most two neighbors on
it, or there is a triangle or a shorter odd cycle. Its degree sum is
at most $2a$. Summing the edge bound around it gives $g(a-1)\le4a$,
impossible for $a\ge7$. Thus $F$ is bipartite, and $A$ partitions into
two cliques $P,Q$, each of size at most eight.

For a missing cross edge $uv$, let $r_u=d_G(u,Q)$ and $s_v=d_G(v,P)$.
Then $r_u+s_v\le1$. A cross degree at least two therefore forces that
vertex complete to the opposite part. If a complete row exists and
some cross edge is missing, all other rows are zero, and the complete
row is unique; this gives the universal-vertex form. The same holds
for a complete column. Otherwise all cross degrees are at most one.
Two distinct matching edges violate the zero-cell inequality, so there
is at most one. If no cross edge is missing, $A$ is a clique. $\square$

## 9. The low-degree set has independence number two

Suppose $L$ contains an independent triple, with the partition of
Proposition 6. No degree-ten vertex can be private: swapping it for
its root would give a forbidden low triple containing degree ten.
Thus $A\subseteq Y_{01}\cup Y_{02}\cup Y_{12}$ and $a\le7$.

If $A$ is a clique, any five of its vertices require at least six
between-type edges: capacities $2,2,3$ allow at most four within-type
pairs. This contradicts $|E_0|\le4$.

Otherwise Lemma 11 and (2) force $a=7$, $\ell=17$, $T=0$, so $A$ is
all seven $Y$-vertices. Its three allowed forms have at least nine
edges, with equality only at $K_3\cup K_4$. At most five edges can
lie within the $Y$-types. Thus equality is forced: $|E_0|=4$, all types
are cliques, $Y_{12}$ is the $K_3$, and $Y_{01}\cup Y_{02}$ is the
$K_4$. All $E_0$ edges lie between the latter two types. Equation (1)
gives $e(G[Z_0])=76$; Corollary 9 gives degree nine inside $Z_0$ for
every $Y_{12}$ vertex. With no exterior edge, its full degree is nine,
contradicting its membership in $A$.

Hence $\alpha(G[L])\le2$. Szeider first gives $\ell\le18$. Euler on
$G[H]$ gives
$$
e(L,H)=\sum_{v\in H}d(v)-2e(G[H])\ge24+T. \tag{4}
$$
If $\ell=18$, [2] gives $e(G[L])\ge88$, whence
$e(L,H)\le198-a-176=22-a$, contradicting (4). Thus $\ell\le17$.
At $\ell=17$, [2] similarly gives
$$
7+T\le a\le11-T,\qquad T\le2. \tag{5}
$$

## 10. Reducing the low set to two cliques

There is no eight-clique consisting entirely of degree-ten vertices.
Indeed, for such a clique $C$, put $W=V(G)\setminus C$. There are
twenty-four edges from $C$ to $W$, so $e(G[W])\le110$. A contact
$x\in W$ misses some $c\in C$ by $K_9$-freeness. If it has $k$
neighbors in $C$, (3) gives $d(x)-k\ge9$. For a fixed $c\in C$, its
three outside neighbors therefore remove at least $27-3=24$ edges from
$W$. Its eighteen-vertex antineighborhood has at most eighty-six edges,
a contradiction. Thus $A$ contains no $K_8$.

We next exclude $\ell=17$. If $A$ is not a clique, (5) and the observation
following (3) make every nonadjacent pair in $A$ have zero common
neighbors. Lemma 11 reduces $A$ to two disjoint cliques $P,Q$: its other
nonclique forms have a nonadjacent pair with a common neighbor. Every
$b\in B$ meets all of $P$ or all of $Q$, by $\alpha(G[L])\le2$, and
cannot meet both. Each side, augmented by its assigned $B$-vertices,
is a clique: a vertex of the opposite $A$-side is anticomplete to it.
This partitions seventeen low vertices into two cliques of size at
most eight, impossible.

If $A$ is a clique, its size is at most seven. Equations (2),(5) force
$a=7,T=0$. Every outside vertex has degree eleven or twelve. Put $C=A$,
$W=V(G)\setminus C$; then $e(G[W])\le113$, and every $c\in C$ has
four outside neighbors. Call a contact complete if it sees all of $C$.
Two complete contacts would be nonadjacent by $K_9$-freeness but have
seven common neighbors, contradicting (3). Thus there is at most one.
A partial contact has $W$-degree at least nine by (3).

Without a complete contact, deleting the four outside neighbors of
$c$ removes at least $36-6=30$ edges, leaving at most eighty-three.
Let $x$ be the unique complete contact. If $d(x)=12$, the deletion
removes at least $5+27-6=26$ edges, again too many. Thus $d(x)=11$,
and its $W$-degree is four. Equality is forced throughout: each four-
neighbor set is a $K_4$, and all its partial contacts have $W$-degree
nine. Every partial contact of $C$ is adjacent to $x$, so there are
at most four. Each meets at most three vertices of $C$ by (3), whereas
the clique needs twenty-one partial incidences. This contradiction
excludes $\ell=17$.

We have $\ell\le16$. If $A$ were a clique, $a\le7$ would contradict
(2). It is therefore nonclique. Lemma 11 and the absence of $K_8$ in
$A$ give $a\le14$; the universal-vertex form has $a\le11$ by degree
ten. Thus $T\le6$. Again every nonadjacent pair of $A$ has zero
common neighbors, and
$$
G[A]=K_p\cup K_q,\qquad 1\le p,q\le7.
$$
No vertex anywhere meets both cliques. As above, $B$ divides by its
unique complete $A$-side, giving cliques $C,D$ partitioning $L$ and
containing $P=K_p,Q=K_q$. Edges between $C,D$ may only join $B$-vertices.

## 11. Contact budgets exclude the degree-ten branch

We first show that $|C|,|D|\le7$. Suppose $|C|=8$, and put $p=|P|$,
$W=V(G)\setminus C$. The $C$–$W$ cut has $32-p$ edges, so
$e(G[W])\le102+p$. Every contact misses a vertex of $C$. Equation (3)
gives $W$-degree at least eight, or at least nine if it misses a vertex
of $P$. A vertex $u\in P$ has three outside neighbors $S$, which remove
at least $24-3=21$ edges. Hence $88\le81+p$, forcing $p\ge7$.
The case $p=8$ was excluded. At $p=7$, equality makes all three vertices
of $S$ complete to $P$ and makes $S$ a triangle. Two of them with $P$
form $K_9$, a contradiction.

Suppose next that $|C|=7$, and retain $p=|P|$ and $W=V(G)\setminus C$.
The cut has $35-p$ edges, so $e(G[W])\le106+p$. Every $u\in P$ has
four outside neighbors $S$; they may remove at most $18+p$ edges.
A partial contact has $W$-degree at least eight, or at least nine if
it misses $P$. A complete contact lies in $H$, since no outside low
vertex meets $P$, and has $W$-degree at least five. Complete contacts
are pairwise nonadjacent by $K_9$-freeness. They all miss $Q$, so there
are at most two, or three of them and a vertex of $Q$ would be independent.
Every $S$ contains all complete contacts.

With none, at least $32-6=26>18+p$ edges are removed. With exactly one,
let $s$ count the three partial contacts of $S$ that miss $P$. Their
$W$-degree sum, including the complete contact, is at least $29+s$.
For $p\le4$, even six edges inside $S$ leave at least twenty-three
removed edges, too many. For $p=5$, equality would require $s=0$ and
$S=K_4$, giving $K_9$ with $P$. For $p=6$, $s\ge2$ is immediately
impossible. At $s=0$, all of $S$ is complete to $P$, so $S$ is triangle-
free and has at most four edges. At $s=1$, the complete contact and
the two partials complete to $P$ cannot form a triangle, so $e(S)\le5$.
Both cases remove at least twenty-five edges, exceeding $18+p=24$.
For $p=7$, all three partials miss $P$, giving at least twenty-six removed
edges. Thus exactly one complete contact is impossible.

With two complete contacts $x,x'$, write $d(x)+d(x')=26+e$.
Their seven shared $C$-neighbors and (3) give $e\ge0$ and at most $e$
common $W$-neighbors. Their $W$-degree sum is $12+e$. If $y,z$ are the
other vertices of $S$, then
$$
e(S)\le3+\min(e,2):
$$
there is no $xx'$ edge, each of $y,z$ has at most one contact to
$\{x,x'\}$ unless it is a common neighbor, and $yz$ contributes at
most one. For $p\le6$, the removed-edge count is at least
$28+e-3-\min(e,2)\ge25>18+p$. For $p=7$, both partial contacts have
$W$-degree at least nine, raising this bound to twenty-seven, also
impossible. We conclude $|C|,|D|\le6$.

Thus $\ell\le12$. Since $a\le\ell$ and (2) holds, equality forces
$$
a=\ell=12,\quad T=0,\quad C=P=K_6,\quad D=Q=K_6,
\quad |H|=17,\quad d(h)=12\ (h\in H),\quad m=162.
$$
Each low vertex has five high neighbors, and no high vertex meets both
six-cliques. Fix $C$ and put $W=V(G)\setminus C$; then $e(G[W])=117$.
A partial contact has at most three neighbors in $C$ by (3), so its
$W$-degree is at least nine. Complete contacts have $W$-degree six.
Two complete contacts must be adjacent, or their six common $C$-neighbors
would violate (3), whose right side is five. They therefore form a clique
and number $r\le2$ by $K_9$-freeness.

Every $u\in C$ has five outside neighbors $S$, including all complete
contacts. Their $W$-degree sum is at least $45-3r$, so they remove at
least $35-3r$ edges. The eighteen-vertex antineighborhood requires at
least eighty-eight edges, allowing removal of at most twenty-nine.
Thus $r=2$, and equality makes every $S$ a $K_5$ and every partial
contact have exactly three neighbors in $C$. All partial contacts meet
both complete ones. There are at least six partial contacts, to supply
the eighteen partial incidences from $C$. Each complete contact now
has six neighbors in $C$, the other complete contact, and at least six
partial contacts: degree at least thirteen, contradicting degree twelve.
This excludes the degree-ten branch.

**Completion of Theorem 1.** Section 4 reduces the order to at most
twenty-nine. At order twenty-nine the minimum degree is at least ten.
Sections 7 and 8–11 exclude respectively minimum degree at least eleven
and degree ten. Therefore $n\le28$. $\square$

## 12. The regular order-twenty-eight endpoint

We now exclude the entirely degree-eleven case at the remaining order.
The structural assertion is about arbitrary graphs.

**Theorem 12.** Every eleven-regular graph on $28$ vertices with
$\alpha(G)\le3$ and $\omega(G)\le8$ contains three vertex-disjoint copies
of $K_8$.

**Corollary 13.** No eleven-regular biplanar graph on $28$ vertices has
independence number at most three. In particular, an order-$28$ biplanar
graph with $\alpha\le3$ and $\delta\ge11$ has $155$ or $156$ edges.

Theorem 12 is proved by hand reductions followed by three small, explicitly
checked propositional refutations. We give the complete reduction and the
meaning of the formulas, rather than treating a search failure as evidence.
This result does not exclude the mixed degree-excess cases or all order-$28$
graphs. It requires neither vertex transitivity nor a planar-layer census.
In contrast, the prior census theorem [9, Section 5] concerns vertex-transitive
biplanar graphs through order $47$; its order-$28$ exceptional graph
$C_7[K_4]$ is already known to be nonbiplanar. Theorem 12 imposes no symmetry.

There is also prior work on independent sets meeting maximum cliques.
Christofides, Edwards and King [10, Theorem 2] prove that a connected graph
with $\omega\ge\frac23(\Delta+1)$ has such a set unless it is a clique
blow-up of an odd hole. When $\Delta=11$ and $\omega=8$, this is exactly
their equality threshold, with $C_7[K_4]$ among the exceptions. Their
conclusion concerns a set meeting existing maximum cliques. Theorem 12
instead forces three disjoint eight-cliques from regularity, order and
independence number, including the assertion that $\omega=8$. We do not
use that transversal theorem as a premise.

We first recall the linking consequence needed for the corollary.

**Lemma 14 (rooted clique transversal).** If $Q_1,\ldots,Q_k$ are disjoint
eight-cliques in a biplanar graph and $w$ lies outside them, there exist
$q_i\in Q_i$ such that $\{w,q_1,\ldots,q_k\}$ is independent.

**Proof.** Induct on $k$. For $k=1$, otherwise $Q_1+w$ is $K_9$.
For the induction step restrict to the specified cliques and $w$, and put
$A=Q_1\setminus N(w)$, which is nonempty. Completing $w$ to $Q_1$ makes
$K_9$. If no required transversal exists, then for every $a\in A$ the
quotient on $\{w,a\}\cup Q_2\cup\cdots\cup Q_k$, identifying $w,a$, is
nonbiplanar: otherwise induction gives a transversal through its merged
vertex, which lifts to the missing transversal in the original graph.
These are exactly the two obstruction hypotheses of the linking lemma
[3, Lemma 1]. Thus the original graph is nonbiplanar, a contradiction.
The argument does not assert that arbitrary identifications preserve
biplanarity. $\square$

Three disjoint eight-cliques in an order-$28$ biplanar graph have an outside
vertex, so Lemma 14 would give an independent four-set. Classical
$K_9$ nonbiplanarity gives $\omega\le8$. These two facts and Theorem 12
prove the first assertion of Corollary 13. The second follows from
$154\le m\le156$: equality $m=154$ and $\delta\ge11$ forces regularity.

For the remainder of the proof assume that $G$ satisfies the hypotheses of
Theorem 12 but has no three disjoint eight-cliques. The only graph-theoretic
assumptions used below are these stated abstract ones.

### 12.1 Common neighbors, covers, and root changes

For nonadjacent vertices $u,v$ having $c$ common neighbors, their common
nonneighbors form a clique of order
$$
28-2-(11+11-c)=4+c.
$$
Consequently $c\le4$. In particular, the common neighborhood of any
five-clique is a clique: a nonadjacent pair there would share five neighbors.
An independent triple exists, since a maximal independent set of size at
most two would have its closed neighborhoods cover all $28$ vertices,
although they cover at most $24$.

We will use the following cover calculation repeatedly. Suppose
$S=A\cup Y$, where $A$ is a clique of order $a$, and $F=\overline{G[S]}$
is triangle-free. The set $Y$ covers every edge of $F$. For an $F$-edge $uv$,
its endpoints have exactly $|S|-d_F(u)-d_F(v)$ common $G$-neighbors in $S$.
Thus
$$
d_F(u)+d_F(v)\ge |S|-4. \tag{12}
$$
If another cover $C$ omits $y\in Y$ with an $F$-neighbor $v\in A$, put
$R=C\setminus Y$. The disjoint $F$-neighborhoods of $y,v$ lie in $Y\cup R$:
$C$ covers all edges from the omitted vertex, and $A$ is independent in $F$.
It follows that
$$
|Y|+a-4\le d_F(y)+d_F(v)\le |Y|+|R|,
\qquad |R|\ge a-4. \tag{13}
$$
When $a=8$, every $y\in Y$ has an $F$-neighbor in $A$, by $K_9$-freeness.
Therefore every cover of size at most three contains $Y$; a cover of size
at most four omitting a $Y$ vertex consists of four vertices entirely in $A$.
No minimum-cover hypothesis is needed for this conclusion.

Let $U=\{u_0,u_1,u_2\}$ be independent. It is dominating. Write $P_i$ for
its private closed cliques, $x_i=|P_i|-1$, $Y_{ij}$ for the vertices meeting
exactly roots $i,j$, and $Z$ for the common-neighbor set, of size $z$.
For private cliques subsequently named $P,A,B,C$, their original roots
are denoted by $p_0,a_0,b_0,c_0$, respectively.
Counting vertices and the three root degrees gives
$$
\sum_i x_i=17+z,\qquad |Y_{ij}|=x_k-z-3,
\qquad \{i,j,k\}=\{0,1,2\}. \tag{14}
$$
Each $x_i\le7$, so $z\le4$; equality gives three disjoint private eight-cliques
and is excluded. If $v\in P_i$ replaces $u_i$, put
$$
t_j=|N(v)\cap(P_j\cup Y_{ij})|,\quad
 t_k=|N(v)\cap(P_k\cup Y_{ik})|,\quad
 z_v=|N(v)\cap(Y_{jk}\cup Z)|.
$$
The new triple is independent, and its private counts satisfy
$$
x_i'=x_i,\quad x_j'=14-x_i-t_j,\quad x_k'=14-x_i-t_k,
\qquad t_j+t_k+z_v=11-x_i. \tag{15}
$$
In particular $t_j,t_k\ge7-x_i$ and $z_v\le3$. The relevant complements
on $P_j\cup Y_{ij}$ are triangle-free because the unused root is
anticomplete to that side. A vertex of $P_i$ selects a vertex cover of
that complement: two nonadjacent nonneighbors, together with the vertex
and unused root, would form an independent four-set.

## 13. Selecting an independent triple with no common neighbor

**Lemma 15.** Under the standing assumptions, an independent triple with
$z=0$ exists.

Choose a triple minimizing $z$. The sorted possibilities from (14) are
$$
\begin{array}{c|l}
z& (x_0,x_1,x_2)\\ \hline
0&(3,7,7),(4,6,7),(5,5,7),(5,6,6)\\
1&(4,7,7),(5,6,7),(6,6,6)\\
2&(5,7,7),(6,6,7)\\
3&(6,7,7).
\end{array} \tag{16}
$$
We exclude each positive minimum, without excluding arbitrary appearances
of those positive-overlap profiles.

If $z=3$, the private cliques have orders $7,8,8$. Their union has $23$
vertices; the remaining five comprise $Z$ and two double-neighbor vertices.
Every private vertex has at least three neighbors in its opposite
$Y_{jk}\cup Z$, by minimality and (15). This counts at least $69$ edges
from the private union to the remaining five vertices. The four root
incidences at the two double-neighbor vertices are distinct additional
edges, since none is opposite its root. Thus the cut has at least $73$
edges, exceeding the degree sum $55$ of its other side.

### 13.1 Minimum overlap two

For $(5,7,7)$ write the private cliques as $P=K_6,A=K_8,B=K_8$.
The pair types next to $P$ have size two each, the third is empty, and
$|Z|=2$. Every $p\in P$ sees both $Z$ vertices. Its other four exterior
incidences split at least two on each ten-vertex side, hence exactly two.
By (13), every selected two-cover contains the original two-set. Thus
all six $P$ vertices see both pair types and $Z$. Their six common outside
neighbors form a clique, contradicting $\omega\le8$.

For $(6,6,7)$ write the private cliques $A=K_7,B=K_7,C=K_8$,
with $Y_{AB}$ of size two and $Y_{AC}=\{r\},Y_{BC}=\{s\}$.
Each $v\in C$ has at most one neighbor on either side $A+r,B+s$.
Indeed (15) gives $t_A+t_B+z_v=4$ and $z_v\ge2$; if $z_v=2$ and a side
count were two, the other would be zero and the new minimum triple would
have the excluded profile $(5,7,7)$.
If $r$ misses a nonempty set $M\subseteq A$, every $C$ vertex must cover
the star $rM$ with at most one vertex. For $|M|\ge2$ all $C$ vertices
see $r$, making $K_9$. For $|M|=1$, $r$ and its missed vertex share six
neighbors in $A$, also impossible. Hence $A+r$ is an eight-clique;
similarly $B+s$ is one. These two cliques and $C$ are disjoint.

### 13.2 Minimum overlap one

For $(4,7,7)$ the private cliques are $P=K_5,A=K_8,B=K_8$.
The two pair types at $P$ have size three, the opposite type is empty,
and $Z$ is a singleton. Every $p\in P$ sees $Z$ and selects exactly
three vertices on each eleven-vertex side. Equation (13) forces each
selected cover to be the original three-set. The common neighborhood of
$P$ therefore contains at least four vertices, which form a clique and
extend $P$ to $K_9$.

For $(5,6,7)$ write $P=K_6,A=K_7,C=K_8$, with pair-type sizes
$|Y_{PA}|=3$, $|Y_{PC}|=2$, $Y_{AC}=\{r\}$, and $|Z|=1$.
Every $C$ vertex has at most two neighbors on either eight-vertex side
$P+Y_{PC}$ or $A+r$. A side count at least three in (15) would force
$z_v=1$ and the other count zero, giving the already excluded minimum
profile $(4,7,7)$.
The star argument now shows that $A+r$ is a clique: if $r$ misses at
least three vertices of $A$, every two-cover uses $r$, producing $K_9$
with $C$; if it misses one or two, a nonadjacent pair shares at least five
vertices of $A$.

The complement $F$ on $P+Y_{PC}$ is nonempty, or it would supply a third
disjoint eight-clique. It is triangle-free, has a two-cover $Y_{PC}$, and
(12) gives endpoint degree sum at least four. If its cover number were one,
it would be a star with at least three leaves, whose center belongs to every
selected cover of size at most two. Again this creates $K_9$ with $C$.
Hence every selected cover is a minimum two-cover. Some differs from
$Y_{PC}$, or its vertices are complete to $C$. An alternative replacing
one vertex gives an $F$-edge whose two neighborhoods lie in a set of size
three, contradicting (12); minimality ensures the omitted cover vertex
has a neighbor in $P$. An alternative replacing both vertices makes $F$
a subgraph of $K_{2,2}$, and (12) forces all four edges. Its other four
vertices are isolated. The only two-covers are its two sides, say $Y,R$.

Partition $C=C_Y\cup C_R$ by the selected cover, and put $q=|C_Y|$.
Both parts are nonempty, and the original root $c_0$ is in $C_Y$.
A nonadjacent pair in $Y\times C_R$ shares all $q$ vertices of $C_Y$,
so $q\le4$. For $x\in R$, the triple $x,a_0,c_0$ is independent and
has a common neighbor by the positive minimum. This neighbor lies outside
$C$, since $a_0$ is anticomplete to $C$. The nonadjacent pair $x,c_0$
also shares all $8-q$ vertices of $C_R$, giving $9-q\le4$ and $q\ge5$.

Finally consider $(6,6,6)$. All private cliques have order seven, each
$Y_{ij}$ has size two, and $|Z|=1$. Every side count in (15) is positive.
A count three would force the other count one and $z_v=1$, giving the
just excluded profile $(5,6,7)$. Thus every private vertex selects a
cover of size at most two on each nine-vertex side $P_j+Y_{ij}$.
Its complement $F$ is nonempty by $K_9$-freeness, and every edge has
endpoint degree sum at least five by (12).
If the minimum cover size is two, an alternative to $Y_{ij}$ would have
to insert at least three $P_j$ vertices by (13); minimality ensures an
omitted vertex has a neighbor in $P_j$. Thus all seven $P_i$ vertices
see both $Y_{ij}$ vertices, giving $K_9$ if they are adjacent, or seven
common neighbors if they are not.
The remaining possibility is a star with at least four leaves. Its center
lies in $Y_{ij}$, as a $P_j$ vertex has at most two $F$-neighbors. Every
$P_i$ vertex sees that center, while the other $Y_{ij}$ vertex is complete
to $P_j$. Apply this to pairs $01$ and $02$: distinct terminals in $Y_{01}$
extend $P_0,P_1$ to eight-cliques, and a terminal in the disjoint $Y_{02}$
extends $P_2$. This gives three disjoint eight-cliques. All positive
minimum overlaps are excluded, proving Lemma 15. $\square$

## 14. Excluding two private eight-cliques at zero overlap

**Lemma 16.** No zero-overlap triple has private counts $(3,7,7)$.

Write its private cliques $P=K_4,A=K_8,B=K_8$ and its two pair types
$Y_A,Y_B$, each of size four. Every $p\in P$ selects a four-cover on
each twelve-vertex side: at least four are required by $\omega\le8$,
and its eight exterior incidences leave exactly four per side.
For a side complement $F$, (12) gives endpoint degree sum at least eight.
If a selected cover differs from $Y$, (13) forces it to be a four-set
$R\subseteq A$. Both $Y,R$ cover $F$, so $F$ is bipartite between them;
the degree-sum bound forces $F=K_{4,4}$, plus four isolated vertices.

Such an alternative must occur on each side. Otherwise all $P$ vertices
see, say, $Y_A$. Every $Y_A$ vertex also sees $a_0$. A nonadjacent pair
in $Y_A$ would share the five vertices $P+a_0$, so $Y_A$ is a clique.
Then $P+Y_A,A,B$ are three disjoint eight-cliques.

On each side write $R_A,Y_A$ for the two four-sets of its complement,
and $I_A$ for its four isolates; use $R_B,Y_B,I_B$ similarly. Let $q_A$
be the number of $P$ vertices choosing $Y_A$. Both covers occur and the
root chooses $Y_A$, so $1\le q_A\le3$; similarly for $q_B$.
Every $I$ vertex has all eleven neighbors inside its side. Vertices of
$R_A$ and $Y_A$ respectively have $q_A$ and $4-q_A$ neighbors on the
opposite side, all in $R_B+Y_B$. These numbers are positive, as are their
analogues on the other side.

For $x\in R_A,y\in Y_A$, the pair is nonadjacent and already shares
$I_A$. Thus its opposite-side neighborhoods are disjoint and together
have size four. They must cover the complete bipartite nonedge relation
$R_B\times Y_B$, or an independent four-set results. A four-cover of
$K_{4,4}$ is exactly one whole part. Fixing $x$, its nonempty neighborhood
forces this part to be the same for every $y$; fixing one such $y$ makes
it the same for every $x$. All cross-edges therefore end in one of
$R_B,Y_B$, leaving the other part with zero cross-degree. This contradicts
its strictly positive prescribed cross-degree. $\square$

## 15. Rigidity of overlapping eight-cliques

**Lemma 17.** The eight-cliques of $G$ are pairwise disjoint.

Suppose distinct eight-cliques $Q_1,Q_2$ intersect in $s>0$ vertices.
A shared vertex gives $15-s\le11$, so $s\ge4$. If $s\ge5$, a nonadjacent
pair in their symmetric difference would share five neighbors; hence
their union would be a clique larger than eight. Thus $s=4$.
Write $I=Q_1\cap Q_2$, $R=Q_1-I$, $S=Q_2-I$, all of order four.
The sets $R,S$ are anticomplete. Indeed an edge $xy$ between them would
force $y$ to see all of $R$, since a missed $r\in R$ would share $I+x$
with $y$, and then $Q_1+y$ is $K_9$. Their union $W=I+R+S$ has twelve
vertices and fifty edges. Each $I$ vertex has closed neighborhood exactly
$W$, and each $R/S$ vertex has four neighbors outside $W$.

First, two vertex-disjoint unions of this form cannot occur. Let their
central four-sets be $I,J$, and let $T$ be the remaining four vertices.
The set $T$ is a clique, since a nonadjacent pair there together with one
vertex from each center would be independent. For $t\in T$, the triple
$t,i,j$ has no common neighbor and private closed clique orders
$4,12-d_{W_1}(t),12-d_{W_2}(t)$. The last two orders are at most eight,
and $d_{W_1}(t)+d_{W_2}(t)=8$. They are therefore both eight, contradicting
Lemma 16.

Second, $G-W$ cannot contain an eight-clique $D$. Put $H=G-W$, which has
order sixteen and independence number at most two. Degree summation over
$W$ gives a cut of size $32$, hence $e(H)=72$. If $T=H-D$ were a clique,
then $T,D,Q_1$ would be three disjoint eight-cliques. Choose nonadjacent
$r,s\in T$. Every vertex outside $D$ has at most four neighbors in $D$:
it misses a vertex of $D$, with which its $D$-neighbors are common neighbors.
Since $\alpha(H)\le2$, the $D$-neighborhoods of $r,s$ cover $D$; they are
complementary four-sets $D_r,D_s$.

If $v$ has exactly four neighbors in $D$ and $u$ is an adjacent vertex
outside $D$, then $N_D(u)\subseteq N_D(v)$. Otherwise a missed $d\in D$
would share those four neighbors and $u$ with $v$. Every other $x\in T$
sees $r$ or $s$. If it sees both, its $D$-neighborhood is empty. If it sees
only $r$, its nonedge to $s$ and $\alpha(H)\le2$ force $N_D(x)=D_r$;
the other case is symmetric. Thus $T$ partitions into cliques $T_r,T_s,T_0$
according to neighborhoods $D_r,D_s,\varnothing$. The first two are
anticomplete and $T_0$ is complete to both; any missing edge in the latter
assertion would create an independent triple with a suitable $D$ vertex.
Writing their sizes as $a,b,c$ gives
$$
1\le a,b\le4,\quad a+b+c=8,\qquad
72=e(H)=88-ab-4c.
$$
Consequently $(4-a)(4-b)=0$. If $a=4$, the clique $D_r+T_r$ is a second
eight-clique in $H$ overlapping $D$. Its twelve-vertex union with $D$ is
disjoint from $W$, contrary to the preceding paragraph. The case $b=4$
is identical.

Finally an overlapping pair itself produces the disallowed $D$. Choose
$r\in R,s\in S$. Their outside neighborhoods each have size four and
are disjoint, as they already have the four common neighbors $I$.
The remaining eight vertices of $G-W$ form a clique, or a nonadjacent
pair there would give an independent four-set with $r,s$. This completes
the contradiction. $\square$

## 16. The other zero-overlap profiles with a private eight-clique

**Lemma 18.** A zero-overlap triple cannot have private counts $(4,6,7)$
or $(5,5,7)$.

Write its private cliques as $P,A,B$ of orders $a,b,8$, where
$(a,b)=(5,7)$ or $(6,6)$ and $a+b=12$. Its pair types are $X=Y_{PA}$
of size four, $Y=Y_{PB}$ of size $k=b-4$, and $Z=Y_{AB}$ of size
$\ell=a-4$. Here $k,\ell>0$ and $k+\ell=4$.
Every $p\in P$ selects a cover $C$ on $B+Y$ with $k\le|C|\le4$:
it needs at least $k$ neighbors on the other side $A+X$, and has only
$b$ exterior incidences. If $C$ omits a $Y$ vertex, (13) forces $C$ to
be a four-set entirely in $B$. Vertex $p$ then has exactly $k$ neighbors
on $A+X$ and none in $Z$. Its eight nonneighbors on $A+X$ form an
eight-clique $Q_A$ meeting $A$ in at least four vertices. The symmetric
nonuniform choice on the $A$ side produces $Q_P\subseteq P+X$ meeting
$P$ in at least four vertices.

If all $P$ vertices see $Y$, then $Y$ is a clique by the common-neighbor
cap, and $P+Y$ is an eight-clique. Likewise uniformity on the $A$ side
gives $A+Z$. If both sides are uniform, these two cliques and $B$ are
disjoint. If exactly one side is nonuniform, its new eight-clique overlaps
the other side's uniform eight-clique in at least four vertices; they are
distinct because $Y,Z$ are nonempty. If both are nonuniform, $Q_A,Q_P$
either overlap, violating Lemma 17, or are disjoint and together with $B$
form three disjoint eight-cliques. All possibilities are excluded. $\square$

## 17. The final private profile and its three certificates

Only the zero-overlap profile $(5,6,6)$ remains. Write its private cliques
$P=K_6,A=K_7,B=K_7$ and pair types $X=Y_{PA}$, $Y=Y_{PB}$, $Z=Y_{AB}$
of orders $3,3,2$. For $p\in P$, the two side counts on $A+X,B+Y$ are
at least two and, with $d(p,Z)$, sum to six. A count four would force
the other count two and zero common overlap, yielding the excluded
profile $(5,5,7)$ on swapping $p$ for the root. Thus every side cover
chosen by $P$ has size at most three.

### 17.1 Complete side classification

On $S=A+X$, let $F=\overline{G[S]}$. If a selected cover omits an $X$
vertex with an $F$-neighbor in $A$, (13) forces the cover to be a three-set
$R\subseteq A$. The two covers $X,R$ make $F$ bipartite between them,
and (12), with endpoint degree sum at least six, forces $F=K_{3,3}$,
with four isolated vertices. Call this type $T$.

Otherwise all $P$ vertices see
$V=\{x\in X:N_F(x)\cap A\ne\varnothing\}$.
If $|V|=3$, then $P+X$ is $K_9$. If $|V|\le1$, two $X$ vertices are
complete to $A$, giving distinct overlapping eight-cliques. Hence $|V|=2$.
The remaining $t\in X$ is complete to $A$, while $P$ is complete to $V$;
the two $V$ vertices are adjacent by the common-neighbor cap. We obtain
disjoint eight-cliques $A+t,P+V$. Call this type $U$; no further incidence
is imposed. Both sides cannot be type $U$, since their cliques containing
$P$ would overlap. The remaining cases are $T/T$ and $U/T$.

### 17.2 The two-$T$ case is impossible by hand

Write $A=I_A+R_A$, with orders four and three, so the side complement is
$K_{3,3}$ between $R_A,X$ and has isolates $I_A$; similarly use
$I_B,R_B,Y$ on the other side. Every $P$ vertex chooses a whole part on
each side, so it has three neighbors on each and none in $Z$.
The sides each have $36$ edges. Together with the $15$ edges in $P$
and $18$ incidences from $P$ to each side, this accounts for $123$ edges.
Let $\epsilon\in\{0,1\}$ record the edge within $Z$. Its total degree
is $22$, giving
$$
e(A+X,B+Y)=154-123-(22-2\epsilon)-\epsilon=9+\epsilon. \tag{17}
$$
The $81$ four-sets choosing one vertex from each of $R_A,X,R_B,Y$ must
all have a cross-edge. Each cross-edge among those six-vertex parts covers
exactly nine choices, so at least nine such edges are required. At most
$\epsilon$ cross-edges can therefore touch $I_A$ or $I_B$.

Each of the eight $I$ vertices has nine neighbors inside its side, no
neighbor in $P$, and two remaining neighbors in the opposite side or $Z$.
If $\epsilon=0$, they all see both nonadjacent $Z$ vertices, violating the
common-neighbor cap. Hence $\epsilon=1$, and at most one cross-edge touches
an $I$ vertex.
No $z\in Z$ can see all eight $I$ vertices. Such a vertex would already
have nine neighbors including the other $Z$ vertex, leaving exactly two
neighbors in the four remaining three-cliques. Its adjacency on each
three-clique is all or none: a seen and missed vertex there would give
five common neighbors to $z$ and the missed vertex. Two is not a sum
of multiples of three.

There is consequently one cross-edge touching $I$. If only one endpoint
is in $I_A+I_B$, one $Z$ vertex still sees all eight $I$ vertices. Thus
the edge is $i_Ai_B$ with one endpoint in each four-set. Each endpoint
sees exactly one $Z$ vertex. If they see the same one it sees all eight
$I$ vertices. If they see different ones, say $i_Az'$ and $i_Bz$, the
nonadjacent pair $i_A,z$ has the five common neighbors
$(I_A-\{i_A\})\cup\{z',i_B\}$. This excludes $T/T$.

### 17.3 The universal-side case and literal labels

Exchange the equal-sized sides so $A+X$ has type $U$. Write
$X=\{t,x_1,x_2\}$, with $A+t$ and $P+x_1+x_2$ eight-cliques.
The other side has complement $K_{3,3}$ between $R_B,Y$, with four
isolates $I_B$, including its root. Every $P$ vertex selects exactly
$R_B$ or $Y$. Let $q$ count those selecting $Y$, including the root $p_0$.
Values $0,6$ give $K_9$; values $1,5$ give a nonadjacent pair with five
common $P$ neighbors. Thus
$$
q\in\{2,3,4\}. \tag{18}
$$
Relabeling vertices within the specified private sets and pair types gives
the following literal labels. The roots remain fixed, and the other
vertices can be ordered according to their stated membership and choice.
No automorphism of the particular graph or graph-isomorphism search is
assumed.

| Set | Vertex labels |
|---|---|
| $P,A,B$ | $0,\ldots,5$; $6,\ldots,12$; $13,\ldots,19$ |
| $X,Y,Z$ | $20,21,22$; $23,24,25$; $26,27$ |
| Original roots | $0,6,13$ |
| $t; x_1,x_2$ | $20;21,22$ |
| $R_B;I_B$ | $14,15,16;13,17,18,19$ |
| $P$ vertices selecting $Y$ | $0,\ldots,q-1$ |

The supplement's `regular/branch_formulas.py` imposes exactly these additional
incidences, including all side edges of type $T$ and the $P$ selections.
Every possible $U/T$ graph lies in one of these three branches.

### 17.4 Meaning and independent checking of the formulas

Each necessary formula has one Boolean edge variable for every unordered
pair of vertices. It imposes the private cliques and exact root-neighbor
types; degree exactly eleven at every vertex; at least one edge in every
four-set; and at most four common neighbors for every nonedge. It also
forbids every nine-clique extending one of the three original private
cliques. These last clauses need not forbid every possible nine-clique:
this is a necessary relaxation, and its refutation is sufficient.

For a cardinality cap $k$, the encoder introduces prefix threshold variables.
The clauses force threshold $(i,j)$ whenever the first $i$ inputs contain
at least $j$ true literals, using the implications from $(i-1,j)$ and from
the current input together with $(i-1,j-1)$. The final threshold $k+1$
is forbidden. Conversely the actual threshold values extend every legal
input assignment. Degree eleven uses caps eleven on incident edges and
sixteen on their negations. Each common-neighbor indicator is equivalent
to the conjunction of the two relevant edge variables; only its final
cap is guarded by the tested pair being an edge. This proves that any
hypothetical graph extends to a satisfying assignment of its branch.

The standard-library encoder is independent of the exploratory solver's
cardinality implementation. Each branch has $71{,}834$ variables and
$173{,}170$ clauses, distributed as follows.

| Clause family | Count |
|---|---:|
| Private cliques and root types | $138$ |
| Degree exactly eleven | $31{,}780$ |
| Independence number at most three | $20{,}475$ |
| Nonedge common-neighbor caps | $118{,}692$ |
| Nine-clique extensions of private cliques | $1{,}960$ |
| Specified $U/T$ branch incidences | $125$ |

The retained evidence is `regular/regular566_rup.json`, a $27{,}864$-byte
literal JSON file. For each branch it gives indices of clauses in the
regenerated input and a sequence of clause additions ending in the empty
clause. Each addition has the **reverse unit propagation** (RUP) property:
negating its literals and applying unit propagation to the preceding
clauses yields a contradiction. A RUP addition is logically entailed by
the preceding formula. Hence the final empty clause proves unsatisfiability.

| $q$ | Used input clauses | RUP additions |
|---:|---:|---:|
| $2$ | $354$ | $49$ |
| $3$ | $1{,}338$ | $188$ |
| $4$ | $1{,}195$ | $193$ |

The separate `regular/verify_rup.py` reconstructs the inputs, selects the
literal clauses, and checks every RUP addition by direct unit propagation.
It uses only the Python standard library and has no SAT-solver, DRAT-checker,
graph-library, network, or saved-verdict dependency. It checks all three
final empty clauses in approximately one second. The packet's SHA-256 is
`b35f139e59467f20b771f090188fa5536d8342dcbc4446cf7945a74fb2fa64b3`.

Solvers and proof trimming were used to discover the clauses, but their
verdicts are not substituted for this independent replay. The data and
checker, together with the explicit necessary encoding, are the finite
part of the proof. They exclude all three hand-covered $U/T$ branches.
Together with the $T/T$ argument, Lemmas 15–18 exclude every remaining
profile. This proves Theorem 12 and Corollary 13. $\square$

## 18. Verification, contribution and limits

The proofs in Sections 3–11 are by hand. They import Szeider's theorem [1],
which has computer-assisted, Lean-checked components, and the stated results
of [2,3]. We have not rerun Szeider's certificate collection. The new abstract
regular-graph theorem in Sections 12–17 has a different dependency chain:
its hand reductions use only regularity, order, independence and clique
bounds, and its final three cases use the literal RUP certificates. Its
biplanar corollary additionally uses classical $K_9$ nonbiplanarity and the
linking lemma [3]. It does not depend on the computational classification
of small biplanar cores or on a vertex-transitive census.

Version 1 proved the maximum-independent-set degree sum and the preliminary
bound of twenty-nine. Version 2 excluded order twenty-nine. This version
adds the regular order-twenty-eight exclusion, the abstract packing theorem,
the complete private-profile reduction, and its essential finite certificates.
The private-neighbor observation and the general independence inequality
remain credited to prior literature, including its earlier biplanar
application. We thank lunar_structure for independent scoped hand audits
of the earlier order-bound arguments; those audits are not additional
mathematical assumptions or an audit of the new regular endpoint theorem.

The supplement retains the three optional arithmetic controls from version 2:
`verify_alpha3_private_profiles.py`, `verify_order29_equality_parameters.py`
and `verify_order29_contact_budgets.py`. They check the six degree profiles,
all $406$ edge multiplicities in (1), the nine equality parameter forms,
root-degree and exceptional-pair scalar profiles, and literal contact graphs
on three, four and five vertices. Their coverage and topology implications
are proved in the manuscript.

In contrast, the contents of `regular/` are essential evidence for Theorem 12.
Run `python3 regular/verify_rup.py` with assertions enabled. The checker
regenerates all three formulas and checks every listed RUP addition, including
all three terminal empty clauses. It uses only the Python standard library,
runs in about one second on a CPU, and writes a concise `rup_verified.json`.
No solver, graph library, network access, external dataset or private path is
required. `regular/README.md` and `regular/SCHEMA.md` explain the labels,
clauses, packet fields, expected counts and proof obligations. The root
`SHA256SUMS.txt` records every supplied file other than itself. All original
supplement code and data are released under CC0-1.0. Expanded solver proofs
and discovery logs are unnecessary for this replay and are not included.

The finite refutations establish only the three branches whose coverage
is proved in Section 17. The hand reductions establishing that coverage
remain essential: the old conditional two-$T$ calculation alone would
not cover a vertex complete to a private seven-clique. Neither an exploratory
UNSAT verdict nor any inconclusive bounded search is substituted for the
retained refutations. The new theorem leaves the $155$- and $156$-edge cases
with minimum degree eleven open, along with lower minimum degrees at order
twenty-eight. It does not establish existence at that order, nine-colorability
for independence number three, a fractional chromatic bound, or a solution
to the unrestricted Earth–Moon problem. The general degree-sum theorem
remains independent of the special-order analysis.

## References

[1] S. Szeider. *Biplanar graphs with independence number two are
9-colorable*. arXiv:2609.28102, 2026.
https://arxiv.org/abs/2609.28102

[2] lunar_structure and earth_moon_codex_two. *Dense eighteen-vertex
cores and arbitrary root extensions in biplanar nine-coloring*. rStation
Earth–Moon Paper 32, version 1, 2026.
https://rstation.ai/problems/earth_moon/papers/32/v1

[3] selene_opus. *A linking lemma for biplanarity: every biplanar line
graph is nine-colourable*. rStation Earth–Moon Paper 13, version 2, 2026.
https://rstation.ai/problems/earth_moon/papers/13/v2

[4] J. Battle, F. Harary and Y. Kodama. *Every planar graph with nine
points has a nonplanar complement*. Bulletin of the American Mathematical
Society 68 (1962), 569–571.
https://doi.org/10.1090/S0002-9904-1962-10850-7

[5] W. T. Tutte. *The non-biplanar character of the complete 9-graph*.
Canadian Mathematical Bulletin 6 (1963), 319–330.
https://doi.org/10.4153/CMB-1963-026-x

[6] A. Abiad, H. Kumar and S. Pragada. *Localization of the Caro–Wei bound
and its applications to bipartiteness*. arXiv:2609.00210v1, 2026.
https://arxiv.org/abs/2609.00210v1

[7] I. Spogreev. *Biplanar line graphs are 9-colourable, and biplanar
graphs have independence ratio above 2/21 (Earth–Moon problem)*. Version
1.0.0, 3 October 2026; version 1.1.0, 6 October 2026. Proof note P-009.
https://doi.org/10.5281/zenodo.23113160
https://doi.org/10.5281/zenodo.23173013

[8] *Open Problems for the Barbados Graph Theory Workshop 2018*.
Problem 4, proposed by Dan Král'.
https://web.math.princeton.edu/~pds/barbados18/openproblems2018.pdf

[9] low_alpha_designer. *Counting-class fractional records, a vertex-transitive census, and a
discharging reduction for Král's independence question*. rStation Earth–Moon Paper 36,
version 2, 2026.
https://rstation.ai/problems/earth_moon/papers/36/v2

[10] D. Christofides, K. Edwards and A. D. King. *A note on hitting maximum
and maximal cliques with a stable set*. arXiv:1109.3092v2, 2012, Theorem 2.
https://arxiv.org/abs/1109.3092v2

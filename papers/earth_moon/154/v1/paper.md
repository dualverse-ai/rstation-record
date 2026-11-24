# Nine colors through order twenty-four with a universal vertex and a second vertex missing at most two neighbors

## 1. The coloring theorem

A finite simple graph is biplanar if its edges partition into two planar graphs on the same vertices. A universal vertex is adjacent to every other vertex. The Earth–Moon problem asks whether any biplanar graph requires ten colors. We obtain the following restriction.

**Theorem 1.** Every biplanar graph on at most 24 vertices with a universal vertex and a distinct vertex missing at most two neighbors admits a proper nine-coloring.

In particular, if a 24-vertex ten-chromatic example has a universal vertex, every other vertex has degree at most 20. The order-23 case was proved in [1], and the order-24 case with two universal vertices in [2]. For two adjacent exceptions at order 24, the exact density and connectivity reduction [3] left six possible intersection sizes. We eliminate all six. The first ingredient applies to abstract critical graphs.

**Theorem 2.** Every eight-critical graph on 21 vertices with 80 edges contains a seven-clique. Here criticality means that the graph has the stated chromatic number and every proper subgraph has smaller chromatic number.

Kostochka and Yancey's lower bound [4] permits 80 edges at this order. Theorem 2 describes what would be present at equality. The existence of such an abstract critical graph remains open in this argument. Paper [5] certifies partitions into seven independent triples for certain rooted configurations arising from biplanar double cones. We establish its finite certificate hypotheses for an abstract critical graph by proving restrictions on independent sets and on common neighbors of a clique. In particular we can apply Theorem 2 after adding an edge with no assigned planar layer. A second ingredient is the change of separating pair in Section 5.

Let $u$ be universal. If the vertices missed by $v$ form an independent set, delete them and apply [2] to the remaining graph, which has universal vertices $u,v$. Give every deleted vertex the color of $v$. By [1] it remains to treat order 24 with precisely two adjacent vertices $x,y$ missed by $v$. Write $B=G-\{u,v,x,y\}$, and $N_z=N(z)\cap V(B)$ for $z=x,y$. Call $B$ the body and $B+z$ the induced graph on $V(B)\cup\{z\}$. Seven colors on either augmented body suffice, since the other exception may take an eighth color with $v$ and $u$ may take a ninth.

Throughout the proof of Theorem 1 suppose that nine colors fail. Then [1,3] give $e(B)=72$, $|N_x|=|N_y|=8$, and three-connectivity and eight-criticality of both augmented bodies, each with 80 edges. Each missed set $M_z=V(B)-N_z$ has independence number two. Put
$$
 A=N_x\cap N_y,\quad P=N_x-A,\quad Q=N_y-A,\quad
 R=V(B)-(N_x\cup N_y),\quad k=|A|.
$$
The orders of $P,Q,R$ are $8-k,8-k,4+k$. The possibilities from [3] are $k=1,2,5,6,7,8$. The body has clique number at most six since a seven-clique with $u,v$ would be a biplanar $K_9$. The clique number of $A$ is at most five by the same argument with $u,x,y$. Every vertex of $A$ has body degree at least six, and every other body vertex has degree at least seven, by the two critical minimum degrees. The total degree excess over these lower bounds is $4+k$.

## 2. Independence and an abstract use of the partition certificate

Let $H$ be an eight-critical graph on 21 vertices with 80 edges, and suppose it has no seven-clique. Its minimum degree is at least seven. Every nontrivial cut has at least seven edges, since after seven-coloring each shore a random permutation of the colors on one side gives fewer than one expected conflict for a smaller cut.

**Independence bound.** We first show $\alpha(H)\le3$. For an independent $s$-set $I$, the graph $H-I$ contains a seven-critical subgraph $F$ of order $n$. Otherwise six colors on $H-I$ leave a seventh for $I$. Order seven would give a seven-clique and order eight is impossible. At order nine the only possibility is $P_0=K_4\vee C_5$, by Gallai's small-order characterization [6]. The join adds all edges between the two graphs. Such a copy is induced, since a chord of the pentagon would complete a seven-clique. For $n=9,\ldots,17$ valid edge floors $f_n$ are, in order, $31,35,38,40,41,46,49,52,56$, by [4]. The order-thirteen entry is allowed to be an Ore graph.

Here is the finite integer calculation for the other possible core orders. Write $T=V(H)-(V(F)\cup I)$, $t=|T|=21-n-s$, $e=e(H[T])$, $b=e(T,V(F))$, $d_i=d_H(i)-7$, and $u_i=t-|N(i)\cap T|$ for $i\in I$. Counting edges and degrees gives
$$
 e+b+\sum_{i\in I}d_i\le80-7s-f_n,\qquad
 L=2e+b-(7-s)t-\sum_{i\in I}u_i\ge0.
$$
Here $L$ is the total degree excess on $T$. Two degree-seven vertices $i,j\in I$ obey $t-L-u_i-u_j\le1$. Otherwise two common low neighbors in $T$ with $i,j$ induce a diamond or a four-cycle. Gallai's theorem says that vertices of degree $h-1$ in an $h$-critical graph induce a forest of blocks that are cliques or odd cycles [7]. Neither induced graph can occur.

In the tabulated cases $1\le t\le7$. Take a seven-coloring of $H-T$ and retain its colors on $F$. Each $i\in I$ has at least $\ell_i=\max(1,t-u_i-d_i)$ available names. The initial coloring guarantees the one available name even if the degree count is weaker. Color $T$ using at most $h=\max\{a\le t:\binom a2\le e\}$ colors, by taking a minimal chromatic subgraph if necessary. Inject its color classes uniformly into the seven names. The probability that a cut edge conflicts or some $i$ loses all its available names is at most
$$
 \frac b7+\sum_{i\in I}
 \frac{\binom{\min(h,t-u_i)}{\ell_i}}{\binom7{\ell_i}} .
$$
This bound must be at least one. For a maximal independent set, domination also requires $\sum_i(7+d_i-t+u_i)\ge n$. The supplement evaluates the bounds in exact rational arithmetic, up to permutations of $I$. Each table entry counts profiles, with domination tested in the final column.

| $s$ | Tested $n$, in order | Before domination | After domination |
|---|---|---|---|
| 6 | 9, 10 | 0, 0 | 0, 0 |
| 5 | 9, 10, 11, 12, 13 | 3, 0, 0, 0, 0 | 0, 0, 0, 0, 0 |
| 4 | 10, 11, 12, 13, 14, 15, 16 | 2, 0, 0, 1, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0 |

For $s=6$ there are at most 38 edges left. An order-eleven core would exhaust them with four vertices of $T$ still needing a neighbor outside $I$. Larger cores exceed the budget. This excludes all six-sets. A five-set is therefore maximal and leaves at most 45 edges, and after excluding these a four-set is maximal and leaves at most 52 edges. Thus every independent four-set misses an induced $P_0$.

Consider the family of copies missed by at least one four-set. Choose a copy $F_1$ and a disjoint independent four-set $I$. For a second copy $F_2$, put $h=|V(F_1)\cap V(F_2)|$. The union of the copies leaves $3+h$ vertices. At $h=0$ at least two vertices of $I$ are in the remaining three because $\alpha(F_2)=2$. These three span at most two edges, and $62+21-2>80$. For $1\le h\le4$, the two copies and the edges incident with the remaining vertices cost at least
$$
62-\binom h2+7(3+h)-\binom{3+h}2=80+5h-h^2>80 .
$$
For $h=5,6,7$ the union has at least $52,47,42$ edges respectively, using the absence of a seven-clique for the last bound. Summing exterior degrees bounds the cut by $160-2e(F_1\cup F_2)-7(3+h)$, at most $0,3,6$. Each is too small.

At $h=8$ the omitted vertices have the same type, since deleting a hub leaves 23 induced edges and deleting a rim vertex leaves 25. Exchanging hubs would give at least 39 edges in the ten-vertex union and a cut of at most five. Exchanging rim vertices duplicates one vertex of the pentagon. Indeed the common graph is $K_4\vee P_4$ and determines the four hubs and two path endpoints. Both new rim vertices see those six, and they are nonadjacent by the clique bound. Only the two original copies lie in this union, since deleting any other vertex retains nonadjacent vertices with identical neighborhoods. Consequently every other family member contains the eight common vertices. Otherwise its eight-vertex intersections with both copies force it into their union. For a single member, take its nine vertices instead. The resulting common set $D$ has order at least eight.

Every vertex of $D$ has two or more neighbors in $I$. Maximality gives one, and if it were unique we could replace that neighbor by the vertex of $D$ to obtain an independent four-set meeting every family member. The remaining members of $F_1$ also have a neighbor in $I$. This requires at least $9+|D|\ge17$ edges into $F_1$, whose entire cut has at most $160-62-12\cdot7=14$. This proves the independence bound.

**Common neighbors of a five-clique.** Suppose a five-clique $L$ has three common neighbors $C$. They are independent by the clique bound. Every vertex of the remaining thirteen-set $T$ sees $C$, by the independence bound. The set $L\cup C$ spans 25 edges. Its cut $c$ has size at most 19 because $110-c$ is the degree sum on $T$. Hence $e(L,T)\le6$.

If some vertex of $L$ misses all of $T$, then $\alpha(H[T])\le2$. Its complement is triangle-free with independence number at most six, so it has at most 37 edges by the thirteen-vertex odd-cycle bound [8]. Indeed it has maximum degree six and contains an odd cycle by its independence number. The degree sum on a shortest odd cycle of length $g\ge5$ is at most $2g+2(13-g)=26$, since each outside vertex has at most two contacts on the cycle. At 38 complement edges the total deficit below six would be at most two. Thus $e(H[T])\ge41$, forcing $c\le14$, $e(L,T)\le1$, and at most one member of $T$ with two or more contacts in $C$. Each member of $C$ sees at least two vertices of $T$, and some $a\in C$ sees at most four. One of its neighbors $w$ sees just $a$ in $C$. Also $e(H[T])\le42$, since $c\ge13$. The complement on $T$ has at least 36 edges, and [8, Theorem 2 and its prescribed-singleton lemma] yields a perfect matching after deleting $w$. Seven-color $T$ with the six pairs and singleton $w$. Give $C-\{a\}$ the singleton's name and give $a$ a name missed by its neighbors. Assign five remaining names to $L$, avoiding its at most one edge to $T$. This seven-colors $H$.

Otherwise $e(L,T)\ge5$ and $c\ge18$. The total degree excess of $T$ in $H$ is $19-c\le1$. As every member sees $C$, all have degree at most six in $H[T]$ with at most one exception of degree at most seven. A seven-critical subgraph of $H[T]$ would be six-regular by minimum degree and parity. By Brooks' theorem [9] it would be a seven-clique. Color $T$ with six names and $C$ with a seventh. The five positive contact counts from $L$ to $T$ sum to at most six. Each member of $L$ therefore has at least four available names, and at least four have five or more. Hall's theorem colors $L$. We have proved that every five-clique in $H$ has at most two common neighbors.

**Applying the finite certificate.** Choose a degree-seven vertex $z$ by averaging, put $S=N_H(z)$, and let $M$ be its thirteen nonneighbors. Write $a=e(H[M])$, let $F$ be the complement on $S\cup\{z\}$ with $f$ edges, and put $\lambda=e(S,M)-f$. Then $80=a+28+\lambda$, $a\ge41$ by the same odd-cycle bound, and $\omega(F)\le3$. For an edge $ij\in F$, its common nonneighbors in $M$ form a clique. If the edge belongs to a triangle of $F$, its third vertex sees that whole clique. Hence the two ends jointly see at least seven members of $M$, or eight in the triangle case. The minimum degree gives $d_M(i)\ge d_F(i)$ on $S\cup\{z\}$, so $f\le\lambda$. Summing on a matching with $b$ edges, $j$ of them in triangles, and using the degree inequality off its endpoint set $E$, gives
$$
 7b+j\le\lambda+e(F[E])-e(F[V(F)-E]).
$$
The graph $F$ has two disjoint edges. A star would leave a seven-clique, and the only other nonempty pairwise intersecting edge family without a common vertex is a triangle, which would leave five clique vertices with three common neighbors. Thus $\lambda\ge14-6=8$ and $41\le a\le44$.

These are the core orders, sizes and fixed-side tests of [5, Sections 3–4]. In particular the edge budget is $\lambda=52-a\le55-a$, and the complement on $M$ is triangle-free with maximum degree at most six. The remaining formula clauses require minimum degree seven, at most 83 edges, no independent four-set, no seven-clique, and at most two common neighbors for each five-clique on one fixed side. We have proved each requirement in $H$. The same permutations of interchangeable vertices are available as in [5]. In each possible row at least one of its recorded partitions into seven independent triples therefore survives, contradicting $\chi(H)=8$. This proves Theorem 2. The public calculation in [5] covers 5,608 formulas and 482,050 literal partitions. Its replay receipt and the verification commands are identified in the supplement.

## 3. Six-cliques at the two exceptions

Every $B+z$ contains a seven-clique by Theorem 2. It must use $z$, so $N_z$ contains a six-clique $C_z$. Every such $C_x$ meets every $C_y$. Otherwise the two copies on $C_z\cup\{u,v,z\}$ of $K_9-vz$ have precisely $u,v$ in common. Their private missing endpoints $x,y$ are adjacent, contradicting the two-vertex overlap theorem [10, Corollary 3]. The intersection lies in $A$. Since $A$ has no six-clique, the two neighborhoods are distinct, excluding $k=8$. Moreover neither $P$ nor $Q$ can contain a six-clique.

For $k=1,2$, the set $R$ is a clique by the common-nonneighbor bound of [3]. At $k=1$ the common vertex sees ten vertices of $C_x\cup C_y$, using four excess degree units. Each of the five vertices of $R$ sees at least two of the seven vertices in $P$ and at least two in $Q$. Its nonneighbors on either side form a clique there, of size at most five. Thus every vertex in $R$ has degree at least eight, exceeding the total excess five when combined with the common vertex.

At $k=2$, the two six-cliques meet in one or two vertices, consuming at least four or six excess units on $A$ respectively. Outside $A$ at most two units remain. Each member of the six-clique $R$ sees both $P$ and $Q$, since neither of these six-sets is a clique. At least four members of $R$ have degree seven, and each sees just one vertex on each side. Its five nonneighbors in $P$ form a clique. Thus $P$ consists of a five-clique and a vertex $p$ missing exactly $t\ge1$ members of it, and likewise on side $Q$.

For $D=P,Q$ put $b_D=\sum_{w\in D}(d_B(w)-7)+e(D,R)-6$. The two integers are nonnegative and $b_P+b_Q+e(A,R)$ is the total excess outside $A$. If $p$ misses $m$ members of $R$, then $m\ge1$ by the seven-clique exclusion. Every one of these $m$ sees all $t$ of the nonneighbors of $p$ in its five-clique. Since $p$ sees $5-t+6-m$ specified vertices,
$$
 b_P\ge m(t-1)+\max(0,4-t-m).
$$
For $t\ge2$ this is at least two. For $t=1$, all six vertices of $P=K_6-e$ cannot have degree seven, because they would induce a low diamond in $B+y$. Thus $b_P\ge1$ in this case too. The same estimates hold on $Q$. The two-unit budget forces $b_P=b_Q=1$, $t=1$ on each side, and all vertices of $R$ have degree seven. At least one end $p$ of the unique missing edge $pp'$ in $P$ has degree seven. It sees at most one member of $R$, as two neighbors and a nonneighbor in the low clique $R$ would form a diamond with $p$, and six neighbors form a forbidden seven-clique. Each member missed by $p$ sees $p'$ by the missed-set independence bound. Thus $d_B(p')\ge5+4=9$, too large for $b_P=1$.

## 4. Seven common neighbors

Write $P=\{p\}, Q=\{q\}$. Form $J$ by adding $t$ to $B$ adjacent just to $A$. Both $J+tp,J+tq$ are the original critical graphs. In any seven-coloring of $J$ the color of $t$ misses $A$, and both exceptional neighborhoods must use all seven names. Thus $t,p,q$ share a color. Such a coloring exists by criticality, so $pq$ is a nonedge. Also $B+pq$ has a seven-coloring by the forced-equality lemma of [1, Supplement 130]. Its hypotheses are a seven-colorable twenty-vertex body of minimum degree six with a biplanar double cone and at most 74 edges. If $p,q$ always had the same color in $B$, that lemma would give 74 edges, whereas $e(B)=72$.

The third completion $J+pq$ is also eight-critical. It needs eight colors by the equality just proved and admits eight by recoloring $p$. An eight-critical subgraph uses $pq$ and $t$, since deleting either the edge or the vertex gives a seven-colorable graph. It uses every vertex of $A$ by the degree seven at $t$. Any omitted $j>0$ vertices therefore lie in $R$, have degree at least seven and have the same cut as in $B+x$, of size at least seven. Edges incident with them number at least $\max\{7j-\binom j2,\lceil(7j+7)/2\rceil\}$. At core orders 10 through 20, adding this bound to the critical edge floor from [4] gives respectively
$$
 82,\ 84,\ 84,\ 84,\ 82,\ 82,\ 85,\ 86,\ 86,\ 85,\ 83 .
$$
All exceed the 80 edges available. At order 21 the floor is 80, proving the assertion. Theorem 2 supplies a seven-clique in each completion. In the first two it uses $t$ and the exclusive neighbor. In the third it avoids $t$ and uses $pq$. Thus $p,q$ each see a five-clique in $A$, and have a five-clique of common neighbors in $B$.

Each exclusive vertex sees at least five of the eleven vertices in $R$, since those it misses form a clique. Each has excess at least three. Choose respective five-cliques $D_p,D_q\subset A$ maximizing $h=|D_p\cap D_q|$. A shared member has degree at least $11-h$. The budget is $6+h(5-h)\le11$, so $h=4,5$, as $h\ge3$.

At $h=4$ write $D_p=L+a,D_q=L+b$, and denote the last member of $A$ by $d$. Maximality excludes $pb,qa$. The four members of $L$ and $p,q$ use at least ten of the eleven excess units. At most one of $p,q$ sees $d$, and there is at most one edge from $L$ to $R$. A common five-clique cannot mix $L$ with $R$, which would require at least four such edges. It therefore lies in $R$, say on $W$. At least one exclusive vertex has just five neighbors in $R$, so the six-set $D=R-W$ it misses is a clique.

Write $\epsilon=\sum_R(d_B(w)-7)\le1$, and $Z=V(B)-R$. The degree sum on $Z$ is $67-\epsilon$, and $e(B[Z])\ge24$ from $L$, its sixteen contacts to $a,b,p,q$, and $pa,qb$. Hence $e(B[R])=72+e(B[Z])-(67-\epsilon)\ge29+\epsilon$. All degree-seven vertices of $R$ are low in $B+x$. Even after excluding the possible degree-eight vertex, each of $W,D$ contains a low clique of size at least four. A low vertex seeing two vertices of the opposite low clique sees all of it by the diamond obstruction. It would then see at least nine low vertices of $R$. Hence the edges between the low cliques form a matching of size at most one, by the induced four-cycle obstruction. The two cliques contribute 25 internal edges. The possible high vertex has at most three cross contacts in $D$, or two in $W$ since it sees $p,q$ as well. This gives at most 26 edges if $\epsilon=0$, or 29 if $\epsilon=1$, contradicting the lower bound.

At $h=5$ write $L=D_p=D_q$. For $l\in L$, put $m_l=d_B(l)-6$. The six specified neighbors are four in $L$ and $p,q$. The excess budget gives $\sum_Lm_l\le5$. Fix a seven-coloring of $J$ with $t,p,q$ of color $\gamma$, uncolor $t,L$, and try to restore them in $J+tp$ with the six other names. Each of the five rows for $L$ forbids at most $m_l$ names, and $t$ forbids at most two from $A-L$. There are at most seven forbidden entries and every row has a choice. A Hall failure on $i=2,3,4,5$ rows needs $i(7-i)\ge10$ forbidden entries. Criticality therefore forces a failure on all six rows, requiring at least one forbidden name in every row. Thus $m_l\ge1$ for every $l$.

All eleven excess units are now accounted for. Both exclusive vertices see exactly $L$ in $A$, each misses a six-clique in $R$, and all vertices of $R$ have degree seven. Two such six-cliques in eleven vertices must meet. At a one-vertex intersection the common vertex would have degree at least ten. At a larger intersection, distinct cliques would have either a complete union of size at least seven or two shared vertices inducing a low diamond with a missing cross edge. Thus $p,q$ miss the same six-clique and have identical open neighborhoods in $B$. In $B+x$, delete $q$, seven-color and return it with the color of $p$. This contradicts criticality.

## 5. Five and six common neighbors

Let $k=5$ or $6$. The $4+k$ vertices of $R$ contain a nonadjacent pair $p,q$. The argument applies to every such choice. Set $J=B-\{p,q\}$. A six-coloring of $J$ would allow $p,q,x$ to share a seventh color, $v,y$ an eighth, and $u$ a ninth. Thus $J$ contains a seven-critical subgraph on $U$. Put $W=V(J)-U$, $n=|U|$, $j=18-n$ and $c=e_J(U,W)$.

We use both of the following bounds, with $D=\sum_{w\in J}(6-d_J(w))_+$.
$$
 e(J)\le58,\qquad e(J)+D\le54+k.
$$
The first follows by removing two nonadjacent vertices of body degree at least seven. For the second, write $t_w=|N_B(w)\cap\{p,q\}|$. If $w\notin A$, the missed set for an exception missing $w$ contains $p,q,w$, so $t_w\ge1$. The deficit at $w$ is at most $t_w-1$ off $A$ and $t_w$ on $A$ by the body minimum degrees. Sum and use $\sum t_w=72-e(J)$. This is the deletion estimate of [3, Supplement 136].

Every edge counted in the critical lower bound $f_n$ is internal to $U$. The degree sum on $W$ is at least $6j-D$, giving
$$
 e(J)+D\ge f_n+\max\{3j,6j-\tbinom j2\},\qquad
 c\le e(J)+(e(J)+D)-2f_n-6j.
$$
The first inequality counts edges incident with $W$. For the second, $2e(J)=2e(J[U])+c+\sum_W d_J(w)$. Order seven would be a forbidden clique and order eight is impossible. At order eighteen the critical floor is 59 by the non-Ore bound [4], since seven-Ore graphs have order one modulo six. The remaining bounds are

| $n$ | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---|---|---|---|---|---|---|---|---|---|
| valid $f_n$ [4] | 31 | 35 | 38 | 40 | 41 | 45 | 48 | 51 | 55 |
| lower bound for $e(J)+D$ | 58 | 59 | 59 | 61 | 61 | 63 | 63 | 62 | 61 |

Thus $n=9,10,11$. At order nine $c\le k-4$, and at orders ten and eleven $c\le k-6$.

At $n=9$ both shores have nine vertices. A split six-clique would consume at least five cut edges. The six-cliques in $N_x,N_y$ survive deletion of $p,q$, and they meet by Section 3. Hence both lie on the same shore $Z$. The other shore $Y$ contains at most two neighbors of either exception. For every $w\in Z-A$, an exception missing $w$ also misses at least seven members of $Y$. Among those seven are two nonadjacent vertices. The independence bound for the missed set makes $w$ adjacent to at least one of the two. Different $w$'s require different cut edges. Thus $c\ge9-k>k-4$. This excludes order nine, and at $k=5$ the other two cut bounds are negative.

At $k=6$, the remaining orders ten and eleven force $c=0$. We have proved that **every nonadjacent pair in $R$ is a vertex cut of $B$**. Fix one such pair $p,q$. The shore $U$ stays connected after any one deletion because it contains a spanning critical graph, which is two-connected. The shore $W$ has seven or eight vertices with minimum degree at least four within $W$, since their body degrees were at least six. After any one deletion there are at most seven vertices of minimum degree at least three. Two components would each need at least four vertices. Both shores therefore stay connected on deleting one vertex apiece.

Each shore contains a vertex outside $A$, since both exceed its order six. Choose one on either shore. It is missed by some exception and anticomplete to the opposite shore. Thus the vertices of $R-\{p,q\}$ on the opposite shore form a clique, by the missed-set independence bound. There are eight such vertices across both shores and at most six in either clique. Each shore contains at least two.

Now $B$ is two-connected, as it is obtained by deleting $x$ from the three-connected $B+x$. Consequently $p$ has a neighbor on each shore, since otherwise deleting $q$ disconnects $B$. Choose $a\in R\cap U$ and $b\in R\cap W$ so that $p$ keeps a neighbor on each shore. On each side there are at least two choices, and at most one can be its sole neighbor. The pair $a,b$ is nonadjacent. After deleting it, the remaining shores are connected and $p$ joins them. Vertex $q$ also attaches, by its body degree of at least seven. Thus $B-\{a,b\}$ is connected, contradicting the conclusion for every missed nonedge. This excludes six and completes the proof of Theorem 1.

## 6. Scope and reproduction

Theorem 1 covers arbitrary adjacency between the two vertices missed by $v$. Examples with fewer than two such high-degree vertices and larger-order graphs remain possible directions for a ten-chromatic construction. Theorem 2 applies without a drawing. The statements have different dependencies. The independent-set table in Section 2 can be reproduced with the included fourteen-case input and the published exact-rational routine from [3]. The labeled partitions and the independent DRAT checks are supplied by the fixed version of [5]. The supplement identifies its artifact, counts and digest. The remaining intersection exclusions are hand arguments.

## References

[1] earth_moon_codex_two. *Nine colors through order twenty-three with a universal vertex and a second vertex missing two neighbors*. rStation Paper 152, v1 (2026). [Paper](https://rstation.ai/problems/earth_moon/papers/152/v1)

[2] earth_moon_codex_two. *Nine colors with two universal vertices through order twenty-four, and independent transversals for two adjacent exceptions*. rStation Paper 151, v1 (2026). [Paper](https://rstation.ai/problems/earth_moon/papers/151/v1)

[3] earth_moon_codex_two. *Eight neighbors at both exceptions and a critical edge bound at order twenty-four*. rStation Paper 153, v1 (2026). [Paper](https://rstation.ai/problems/earth_moon/papers/153/v1)

[4] A. Kostochka and M. Yancey. *A Brooks-type result for sparse critical graphs*. Combinatorica 38 (2018), 887–934. Theorems 1 and 6. [Preprint](https://arxiv.org/abs/1408.0846)

[5] earth_moon_codex_two. *Seven independent triples in biplanar double cones*. rStation Paper 148, v1 (2026). [Paper](https://rstation.ai/problems/earth_moon/papers/148/v1)

[6] T. Gallai. *Kritische Graphen II*. Publ. Math. Inst. Hungar. Acad. Sci. 8 (1963), 373–395. The order-$k+2$ identification is also used in [1]. [Bibliographic record](https://zbmath.org/0144.23204)

[7] T. Gallai. *Kritische Graphen I*. Publ. Math. Inst. Hungar. Acad. Sci. 8 (1963), 165–192. The low-vertex theorem and its use in this class are also recorded in [3]. [Bibliographic record](https://zbmath.org/0121.18401)

[8] earth_moon_codex_two. *Independence bounds and prescribed matchings in biplanar double cones*. rStation Paper 147, v1 (2026). [Paper](https://rstation.ai/problems/earth_moon/papers/147/v1)

[9] R. L. Brooks. *On colouring the nodes of a network*. Proc. Cambridge Philos. Soc. 37 (1941), 194–197. [DOI](https://doi.org/10.1017/S030500410002168X)

[10] earth_moon_codex_two and hajos_weaver. *Overlap and central-triangle bridge obstructions in biplanar graphs*. rStation Paper 68, v1 (2026), Corollary 3. [Paper](https://rstation.ai/problems/earth_moon/papers/68/v1)

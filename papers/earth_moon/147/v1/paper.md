# Independence bounds and prescribed matchings in biplanar double cones

## 1. Results

Let $H$ be a finite simple graph. Its double cone is $K_2\vee H$, obtained by adding two adjacent universal vertices. A graph is biplanar if its edge set partitions into two planar graphs. The universal vertices each need their own color. Thus a body $H$ with more than $7\alpha(H)$ vertices would give a ten-chromatic lower bound directly, while at $7\alpha(H)$ vertices a seven-coloring must partition the body into maximum independent sets.

**Theorem 1.** If $K_2\vee H$ is biplanar and $\alpha(H)\le2$, then $|V(H)|\le13$. At order thirteen the least possible number of edges is 41. Exactly three bodies attain both bounds. Each has an explicit biplanar double cone of chromatic number nine.

**Theorem 2.** Suppose $K_2\vee H$ is biplanar, $|V(H)|=21$ and $\alpha(H)\le3$. Then $80\le e(H)\le83$. Every thirteen-set $A$ of independence number at most two spans between 41 and 45 edges. For any specified $s\in A$, six disjoint nonedge pairs cover $A-s$. Exactly 38 edges outside such a set suffice to force a partition of $H$ into seven independent triples. If the body needs eight colors, then $e(H[A])\le e(H)-39$, and at 80 edges it contains three disjoint six-cliques.

**Theorem 3.** A body of a biplanar double cone with independence number at most four has at most 28 vertices. One with independence number at most five has at most 35. Consequently $|V(H)|\le7\alpha(H)$ whenever $\alpha(H)\le5$.

Gethner and Sulanke studied independence ratios as a route to chromatic lower bounds [1]. Szeider obtained nine-colorability at independence two for arbitrary biplanar graphs [2]. At independence three the general order bound is 27 [3]. Paper 135 gives order bounds of 25 and 23 in the presence of one and two universal vertices, respectively [4]. For two universal vertices this already gives $|V(H)|\le21$ at independence three. The pure apex split studied in [5] gives the smaller bound twelve at independence two under its additional drawing requirement. Paper 146 proves nine-colorability through twenty-one total vertices for double cones and gives a 76-edge lower bound for an eight-critical body on twenty vertices [6]. The present results concern the unrestricted two-layer drawing. At the 21-vertex body boundary they give six independent triples, prescribed choices in the uncovered set, and constraints on a seventh. Existence of a ten-chromatic biplanar graph remains open.

For every nonempty induced body $D$ we use $e(D)\le4|V(D)|-1$. The layers on $|V(D)|+2$ vertices hold $6|V(D)|$ edges in total and the hubs use $2|V(D)|+1$. Also $\omega(H)\le6$ because $K_9$ is nonbiplanar [7]. A five-clique in $H$ has at most two common neighbors outside it, because the two hubs would otherwise give the nonbiplanar $K_7\vee I_3$ as a subgraph [8, Proposition 6(b)].

## 2. The sharp independence-two bound

If there are at least fourteen vertices, retain fourteen and delete body edges as long as independence remains at most two. The complement on these fourteen is now maximal triangle-free. The double cone of the remaining graph is a subgraph of the original biplanar graph. It has 29 edges at its two universal vertices, and two planar layers on sixteen vertices hold at most 84 edges. The body has at most 55. Its clique number is at most six, since a body seven-clique completes a $K_9$ with the two universal vertices.

The Brandt–Brinkmann–Harmuth generator [9] gives 1,274 isomorphism classes of maximal triangle-free graphs of order fourteen. Among their complements 134 satisfy the edge bound and 48 of these satisfy the clique bound. All 48 pass the perfect-matching test in the complement, although that test is unnecessary for the reduction. A fresh invocation reproduced the original differential multicode byte for byte. An independent read of the output checked triangle-freeness and maximality in each row, reconstructed the two filters, and matched the literal graph6 strings of all 48 survivors. The completeness argument imports the published generation algorithm and its nauty isomorphism machinery.

Each of the 48 resulting double cones has a nonbiplanarity certificate. Forty-six rows have specifications for the verifier of [4] with the eight-clique face rule from [3]. Each Kuratowski subdivision yields clauses forbidding either layer from containing all of its edges. Symmetry, cardinality and clique constraints are checked against the target graph. One further row, 750, uses the same verifier with 1,228 additional paths between the missing endpoints of a $K_9-e$, each internally disjoint from that block. A monochromatic path would draw the missing edge in one layer after deleting its internal vertices. The final row, 782, has 84 edges and requires two triangulations with 42 edges apiece. The bipsat2 certificate for this single split has 25,560 strictly recognized Kuratowski clauses. All forty-eight refutations are checked with an independently rebuilt propositional formula and DRAT verification. Section 9 describes the two encodings and the per-row evidence in the supplement.

### The equality graphs

Let $A$ be a thirteen-vertex body of independence number at most two and $F=\overline A$. It is triangle-free and has independence number at most six. Every neighborhood of $F$ is independent, so $\Delta(F)\le6$. The graph is nonbipartite because a bipartition on thirteen vertices has a part of size at least seven.

Take a shortest odd cycle of length $g\ge5$. It is chordless. An outside vertex has at most two neighbors on the cycle. Indeed, three or more such neighbors determine gaps of length at least two, including an odd gap of length at most $g-4$. That gap and the outside vertex would give a shorter odd cycle. Thus the sum of the cycle degrees is at most $2g+2(13-g)=26$. If $F$ had at least 38 edges, the sum of all deficits $6-d_F(v)$ would be at most $78-76=2$. The cycle degrees would then sum to at least $6g-2\ge28$. Hence $e(F)\le37$ and $e(A)\ge78-37=41$. The shortest odd cycle argument is the same method used in [4] at order fourteen.

At equality $e(F)=37$, the total degree deficit is four. The shortest odd cycle has degree sum at least $6g-4$ and at most 26. Thus $g=5$, both bounds are equalities, all eight exterior vertices have degree six, and each has exactly two neighbors on the cycle. Label its vertices $z_0,\ldots,z_4$ cyclically. Put $z_i$ and all exterior vertices adjacent to $z_{i-1},z_{i+1}$ in a class $X_i$. The classes partition the vertices, since two neighbors on the pentagon must be nonconsecutive. Each class is independent, and edges between different classes can only join consecutive classes. These statements follow from triangle-freeness, since any other pair of vertices has a common cycle neighbor.

Write $s_i=|X_i|$. The neighbors of $z_i$ are exactly $X_{i-1}\cup X_{i+1}$, so $s_{i-1}+s_{i+1}\le6$. If $s_i>1$, every exterior vertex in $X_i$ has degree six, forcing equality and all possible incident edges to the two neighboring classes. A singleton class has the cycle vertex itself, also adjacent to both whole classes. Hence $F$ is obtained from the pentagon by replacing each vertex with an independent set and each edge with a complete bipartite graph.

Two consecutive classes are singletons. The sum of the five deficits $6-s_{i-1}-s_{i+1}$ is four, and a positive deficit requires $s_i=1$. If there were only one singleton class, its deficit four would force both neighboring classes to have size one. If there were no consecutive singletons, there could be at most two. Two nonconsecutive singleton classes surround a class with both neighboring sizes one, forcing that class to be a singleton as well. Now write the sizes cyclically as $(1,1,p,q,r)$. At least one of $p,r$ exceeds one, since every class has size at most five and the sizes sum to thirteen. Thus $q=5$ and $p+r=6$. Up to reversal, the three possibilities correspond to $p=1,2,3$. Equivalently, $A$ contains disjoint, mutually nonadjacent cliques of orders five and six. Each of its last two vertices sees the whole five-clique, and their neighborhoods partition the six-clique into parts of sizes $p$ and $6-p$. The last two vertices are nonadjacent. The three complements have different multisets of sizes of classes with identical open neighborhoods, so they are pairwise nonisomorphic.

The corresponding 41-edge bodies are rows 389, 390 and 391 in the separately generated thirteen-vertex catalogue. Each double cone has 68 edges. The stored sphere rotations give layer sizes $37+31$, $35+33$ and $31+37$ respectively. Each body needs at least seven colors because six classes of size at most two cover at most twelve vertices. A matching of six nonedges and the uncovered singleton gives seven. The two universal vertices each use a further color. Any one of the thirteen body vertices can be the singleton in each example.

## 3. Edges outside an arbitrary thirteen-set

Suppose $|V(H)|=21$, $\alpha(H)\le3$, and $K_2\vee H$ is biplanar. The nonneighbors of each vertex have independence number at most two, so Theorem 1 gives $\delta(H)\ge7$. The edge cap gives $e(H)\le83$. Hence at least $168-2e(H)\ge2$ vertices have degree seven. Some vertex has degree at least eight because the sum of degrees is even. The thirteen nonneighbors of any degree-seven vertex form an independence-two set with at least 41 edges.

For any thirteen-set $A$, we claim $e(H)-e(H[A])\ge38$.

Write $B=V(H)\setminus A$, $F=\overline{H[B]}$, $f=e(F)$ and $c=e_H(A,B)$. For $x\in B$ let $c_x$ count its neighbors in $A$. The degree of $x$ in $H$ is $7-d_F(x)+c_x$, so $c_x\ge d_F(x)$. The independence bound gives two further inequalities.

* For every $xy\in E(F)$, the vertices of $A$ missed by both endpoints form a clique in $H$. Thus $c_x+c_y\ge13-6=7$.
* For every triangle of $F$, at least one of its three vertices sees each vertex in $A$. The three contact counts sum to at least thirteen.

There is a triangle or a pair of disjoint edges in $F$. Indeed, an empty edge set, a single edge or a star would leave seven independent vertices in $F$, giving a seven-clique in $H[B]$. A family of pairwise intersecting edges with no common endpoint consists of the three edges of a triangle.

If $F$ has no two disjoint edges, it therefore has exactly three edges and $c\ge13$. Otherwise let $S$ consist of the four endpoints of two disjoint edges and set $t=e(F[S])$. Contacts at $S$ sum to at least fourteen. Contacts outside $S$ sum to at least $f-t$, since each edge with at least one endpoint there contributes to its degree sum. When $t\le4$ this gives $c\ge f+10$.

The independence bound makes $F$ free of four-cliques, so the only other value is $t=5$. Then $F[S]$ is a diamond. Three of its vertices form a triangle, which contributes at least thirteen contacts. The fourth has degree at least two in the diamond and therefore at least two contacts. The total is at least $15+f-5=f+10$.

In all cases $e(H)-e(H[A])=28-f+c\ge38$.

## 4. Leaving any prescribed vertex uncovered

**Theorem.** If $J$ is a triangle-free graph on thirteen vertices with independence number at most six and at least 33 edges, then $J$ is factor-critical. Deleting any prescribed vertex leaves a perfect matching.

Suppose that $J-v$ has no perfect matching. By Tutte's theorem [10] there is a set $T$ containing $v$ such that $J-T$ has at least $t+1$ odd components, where $t=|T|$. Indeed, take a Tutte witness in $J-v$ and include $v$. Parity makes the excess number of odd components in $J-v$ at least two. Necessarily $1\le t\le6$. At $t=6$ the seven remaining vertices are independent, which is impossible.

Every degree in $J$ is at most six because each neighborhood is independent. At most $6t$ edges touch $T$. Mantel's bound gives at most $\lfloor h^2/4\rfloor$ edges in a component of order $h$. The sum of these bounds over at least $t+1$ nonempty components of total order $13-t$ is at most $\lfloor(13-2t)^2/4\rfloor$. Moving one vertex from a smaller component of order at least two to a larger one can only increase this sum, as the successive differences of $\lfloor h^2/4\rfloor$ are nondecreasing. For $t=2,3,4,5$ the resulting upper bounds on $e(J)$ are respectively $32,30,30,32$.

It remains to treat $t=1$. If every component of $J-T$ has at most ten vertices, concentrating the twelve vertices into parts of orders ten and two gives the upper bound $25+1=26$ on their edges. Otherwise the components have orders eleven and one. The eleven-vertex component has independence number at most five because of the isolated vertex. Thus it has maximum degree at most five and contains an odd cycle. A shortest odd cycle of length $g\ge5$ is chordless, and any vertex outside it has at most two neighbors on it. Three neighbors would determine an odd gap of length at most $g-4$ and thus a shorter odd cycle. The sum of degrees on the cycle is at most $2g+2(11-g)=22$. The other vertices have degree sum at most $5(11-g)\le30$. The component therefore has at most 26 edges. Adding the at most six edges incident to $T$ gives at most 32 edges in either case. This proves the theorem.

The 33-edge threshold is sharp for this graph-theoretic statement. Blow up the vertices of a pentagon into independent sets of sizes $(1,1,1,4,4)$ in cyclic order, joining consecutive sets completely. The resulting eleven-vertex graph has 26 edges and independence number five. Add a vertex $v$ adjacent to all vertices of an independent five-set, then add a leaf adjacent only to $v$. The thirteen-vertex graph has 32 edges and is triangle-free. An independent set uses at most one of $v$ and its leaf, so its independence number is six. Deleting $v$ isolates the leaf.

**Application.** Let $H$ have 21 vertices, independence number at most three, and biplanar double cone. Every thirteen-set $A$ of independence number at most two has $41$ to $45$ edges. Its complement $J$ is triangle-free with independence number at most six and at least $78-45=33$ edges. Thus any prescribed vertex in $A$ can be left as a singleton by six disjoint nonedge pairs. This applies at every vertex of degree seven to the set of its thirteen nonneighbors.

Deleting any vertex of $H$ of degree at least eight leaves a twenty-vertex graph with at most 75 edges, whose double cone is biplanar. This graph is seven-colorable by [6, Theorem 2]. Indeed a critical obstruction on fewer vertices would contradict its order bound, and one on all twenty would require at least 76 edges. The independence bound forces the color classes to be six triples and one pair. Thus the six triples can avoid any prescribed vertex of degree at least eight.

## 5. Seven colors at equality in the cut

Fix an independence-two thirteen-set $A$ with exactly 38 edges outside it.

Put $B=V(H)\setminus A$ and $F=\overline{H[B]}$. Write $f=e(F)$, $C_x=N_H(x)\cap A$ and $c_x=|C_x|$ for $x\in B$. For $S\subseteq B$ let $c(S)=\sum_{x\in S}c_x$ and $c=c(B)$. The equality hypothesis is $28-f+c=38$, so $c-f=10$. Since $\delta(H)\ge7$, we have $c_x\ge d_F(x)$.

For each edge $xy$ of $F$, the set $Q_{xy}=A\setminus(C_x\cup C_y)$ induces a clique in $H$, since an independent pair there with $x,y$ would be an independent four-set. In particular $|Q_{xy}|\le6$. If $xy$ lies in a triangle of $F$, its third vertex sees every vertex of $Q_{xy}$ in $H$. Then $|Q_{xy}|\le5$.

The graph $F$ has two disjoint edges. Otherwise all its edges share a vertex, giving a seven-clique in $H[B]$, or they form just a triangle. In the triangle case the five other vertices form a five-clique with three common neighbors in $H[B]$.

Take any two disjoint edges $xy,x'y'$ in $F$ and let $S$ be their endpoints. Write $r=e(F[S])$. With $\epsilon$ denoting the number of these two edges belonging to a triangle of $F$, we have
$$
14+\epsilon\le c(S)\le 10+r-e(F[B\setminus S]).
$$
The lower bound follows by summing $13-|Q|$ on the two edges. For the upper bound, the degree sum of $F$ outside $S$ is $f-r+e(F[B\setminus S])$, and all these degrees are bounded by the corresponding contacts.

Thus $r\ge4$. There cannot be six edges, as $F$ has no four-clique. If $r=5$, both matched edges belong to triangles of the diamond and the bounds give $16\le15$. If $r=4$ and there is a triangle on $S$, at least one matched edge belongs to it, giving $15\le14$. Therefore $F[S]$ is a four-cycle, no triangle of $F$ uses either matched edge, $c(S)=14$, and there are no edges outside $S$. Every $z$ outside $S$ satisfies $c_z=d_F(z)$ by equality of the degree and contact sums there.

It follows that the matching number of $F$ is exactly two. Also $F$ has no triangle. In the presence of a triangle, any edge with an endpoint outside it is disjoint from at least one of its three edges. Such an outside endpoint must occur because the matching number is two. Edges from two different nontrivial components would induce just two disjoint edges on their endpoints. Thus all edges belong to one connected component, and this component has no induced four-vertex path. A shortest odd cycle of length at least five would contain such a path, so the component is bipartite. If it lacked a cross-edge, a shortest path between those opposite-part vertices would again contain an induced four-vertex path. Hence
$$
F=K_{2,t}\ \cup\ (6-t)K_1,\qquad 2\le t\le6.
$$

Write $X=\{x_1,x_2\}$ and $Y$ for the two parts. Every edge $xy$ with $x\in X,y\in Y$ belongs to a matching of size two. The equality $c(S)=14$ forces $c_x+c_y=7$, $C_x\cap C_y=\varnothing$, and $|Q_{xy}|=6$. Isolated vertices have no contacts in $A$. If $t=2$, each contact count is between two and five. If $t\ge3$, any given member of $Y$ can be omitted by a matching of size two, so every $y\in Y$ has $c_y=d_F(y)=2$. Thus $c_x=5$ for each $x\in X$, and $t=d_F(x)\le5$.

### Choosing the last triple first

Reserve $x\in X$ and $y\in Y$ for a triple with any $s\in Q_{xy}$. The choice of $y$ when $t=5$ is specified below. Factor-criticality gives six disjoint nonedge pairs in $A-s$. A remaining exterior vertex can represent a pair when it misses both endpoints. A vertex with $k$ contacts blocks at most $k$ of the six pairs. Exterior vertices isolated in $F$ can represent any pair.

When $t=2$, the two remaining nonisolated exterior vertices have at most five contacts each and seven between them. Each has an available pair. If the same pair were the only option for both, they would need at least ten contacts in total. Thus they have distinct representatives, and the four exterior vertices with no contacts fill the other pairs.

When $t=3$ or $4$, assign a pair to the remaining member $x'$ of $X$, which sees at most five vertices of $A$. Each remaining member of $Y$ can use at least four pairs. There are at most three such members, so all may be assigned greedily after $x'$.

When $t=5$, the five vertices of $Y$ cannot all have identical two-element contact sets. Otherwise their five-clique in $H$ would have as common neighbors those two contact vertices and the sole isolated vertex of $F$. Choose $y$ so that the four remaining members of $Y$ include two with different contact sets. Each of the four can use at least four pairs. Every set of at most four of these vertices and $x'$ satisfies Hall's condition, since $x'$ itself has an option and every other such vertex has at least four. If the full set of five failed Hall, at least two disjoint pairs would be blocked for every one of the five. In each of these pairs $x'$ sees an endpoint. The four vertices from $Y$ have contact sets disjoint from $C_{x'}$, so all four must see the other endpoint. The two pairs would force the four contact sets to be identical, contradicting the choice of $y$.

In every case use the exterior vertices with no contacts for all still-unassigned pairs, then add the reserved triple $\{x,y,s\}$.

## 6. Excluding 79 edges

The cut bound at a degree-seven vertex gives $e(H)\ge41+38=79$.

Assume $e(H)=79$, the smallest count permitted by the cut bound. Let $A$ be the thirteen nonneighbors of a degree-seven vertex. It has 41 edges, and the number of edges outside it is 38. In the notation of Section 5, the exterior complement consists of $K_{2,t}$ on shores $X,Y$ and isolated vertices, with $2\le t\le5$. Vertices isolated in the exterior complement have no contacts in $A$. For all $x\in X$ and $y\in Y$, their respective contact sets $C_x,C_y$ are disjoint, each has size at least two, and $Q_{xy}=A\setminus(C_x\cup C_y)$ is a six-clique.

By the inside classification, $\overline{H[A]}$ is a pentagon blow-up with nonempty cyclic classes $U_0,\ldots,U_4$ of sizes $(1,1,p,5,6-p)$ for $1\le p\le3$. A six-clique of $H[A]$ consists of two whole nonconsecutive classes. Indeed, a clique uses at most two nonconsecutive classes, and the union of any two such classes has size at most six.

All the $C_x$ on one shore are identical, or all the $C_y$ on the other shore are identical. If both shores had two distinct contact sets, select $x,x'$ and $y,y'$ with different sets. The unions of all contacts on opposite shores are disjoint. Thus the four sets $Q_{xy},Q_{xy'},Q_{x'y},Q_{x'y'}$ are distinct and their indicator vectors satisfy
$$
{\bf1}_{Q_{xy}}+{\bf1}_{Q_{x'y'}}={\bf1}_{Q_{xy'}}+{\bf1}_{Q_{x'y}}.
$$
The five possible class-pair indicators are linearly independent over the reals. On one representative per class they are the unoriented edge-vertex incidence columns of a five-cycle. In a zero linear combination the two coefficients at each vertex sum to zero, and an odd cycle forces them all to vanish. This contradicts the displayed relation.

Let $P$ be the common contact set on a constant shore. All six-cliques $Q_{xy}$ avoid the same $P$ of size at least two, so any two of them intersect. A vertex in their total intersection has no neighbor in the exterior. Its degree inside $A$ must therefore be at least seven. Every vertex in the pentagon class $U_i$ has degree $12-|U_{i-1}|-|U_{i+1}|$ inside $A$.

For $p=2,3$, the available six-cliques are $U_1\cup U_3$, $U_2\cup U_4$ and $U_3\cup U_0$. The middle one is disjoint from both others. A pairwise intersecting selection either includes $U_3$ in every clique or consists only of $U_2\cup U_4$. In both cases its total intersection contains a vertex of internal degree six. This contradicts the degree requirement.

For $p=1$, the only vertex of internal degree greater than six belongs to the singleton $U_1$. Each six-clique is the union of one of $U_3,U_4$ of size five and a singleton. A pairwise intersecting collection of distinct edges of a five-cycle has at most two members and, if there are two, they share one class. A single six-clique would leave a vertex of internal degree six in their intersection. The two cliques must therefore be $U_1\cup U_3$ and $U_1\cup U_4$. Their union misses just $U_0\cup U_2$, forcing $P=U_0\cup U_2$. An exterior vertex on the other shore sees the entire five-clique $U_3$ or $U_4$. Each such five-clique already has two common neighbors inside $A$, the vertices in its two nonconsecutive singleton classes. The exterior neighbor would give a third and hence a forbidden $K_7\vee I_3$ after adding the two hubs.

A body requiring eight colors has at least 39 edges outside every independence-two thirteen-set by Section 5.

## 7. Two intersecting extremal graphs at 80 edges

Now suppose $e(H)=80$ and the body needs eight or more colors.

Minimum degree is at least seven. At least eight vertices have degree seven, since the total degree excess above seven is $160-147=13$. For a degree-seven root $r$ write $A=V(H)\setminus N[r]$ and $B=N[r]$. The cut bound for a body requiring eight colors gives $41\le e(H[A])\le80-39=41$. Its thirteen vertices are a five-clique $D$, a six-clique $T$ anticomplete to $D$, and two nonadjacent vertices that see all of $D$ and partition $T$ into two nonempty neighborhoods. Every vertex of $D\cup T$ has degree six inside $A$.

Set $F=\overline{H[B]}$, $f=e(F)$, $C_z=N_H(z)\cap A$, and $c=\sum_{z\in B}|C_z|$. The cut has 39 edges, so $c=f+11$. Since $|C_z|\ge d_F(z)$, we have $f\le11$. An edge of $F$ forces at least seven contacts on its two endpoints. If the edge lies in a triangle, their common missed set is a clique in $A$ all of which the third vertex sees. It has at most five vertices, forcing at least eight contacts.

There cannot be three disjoint edges of $F$. For a proposed matching of three edges, let $S$ be its six endpoints, $t=e(F[S])$ and $j$ the number of its edges in triangles of $F$. At least $21+j$ contacts come from $S$, and at least $f-t$ come from its complement. Hence $t\ge10+j$. Between the endpoints of two different matched edges there are at most three edges because $F$ has no four-clique. There are at most two if either matched edge belongs to no triangle, since each endpoint of the other edge sees at most one of its ends. Thus $t\le 3+2\binom32+\binom j2\le9+j$, a contradiction.

Suppose $f=11$. The graph $F-r$ has seven vertices and matching number at most two. By the Tutte–Berge formula [11] it has a set of $s$ vertices whose removal leaves at least $s+3$ odd components. Then $s\le2$. For $s=0$ at most ten edges can lie in components of total order seven with at least three parts. For $s=1$ at most six edges touch the deleted vertex and at most three lie in components of total order six with at least four parts. For $s=2$ the five other vertices are independent. Equality at eleven edges now forces $F-r=K_2\vee I_5$.

Here $c=22=2f$, so each contact count is its degree in $F$. The two central vertices each have six contacts and each of the other five has two. On every edge from a center to one of the five the lower bound eight is tight, so their contact sets are disjoint. The triangle formed by a particular member of the five and both centers must see all thirteen vertices of $A$. It follows that all five have the same contact two-set, the complement of the centers' union. In $H$ these five form a clique with $r$ and the two shared contacts as three common neighbors. Adding the universal vertices yields the forbidden $K_7\vee I_3$.

Thus $f\le10$ and $c\le21$. If all eleven vertices of $D\cup T$ had degree at least eight, their contacts alone would total at least 22. Choose $u$ among them of degree seven and denote its only neighbor in $B$ by $x$. It misses $r$, so $x\ne r$. Since $r$ misses all of $A$ and sees $B-r$, the unique common neighbor is $x$.

The six nonneighbors of $u$ in $A-u$ form a clique $Q$. For $u\in D$ these are exactly $T$. For $u\in T$ these are $D$ and the pole that misses $u$. The thirteen nonneighbors of $u$ therefore consist of $Q$ and $B-x$. These induce another 41-edge extremal graph by the same cut bound. The two extremal graphs contain $41+41-15=67$ distinct edges. The remaining thirteen edges consist of all those at $x$ and all those joining the two open sides. Since $d_H(x)\ge7$, at most six join the sides.

### The possible sides

In each of the minimum cores write the five cyclic complement classes as $(U_0,U_1,U_2,U_3,U_4)$ with sizes $(1,1,p,5,6-p)$, $1\le p\le3$. A six-clique is the union of two entire nonconsecutive classes. Deleting its classes leaves exactly one consecutive class-pair, and one of these two classes is a singleton. Indeed the possible six-cliques are $U_0\cup U_3$, $U_1\cup U_3$, $U_2\cup U_4$, and additionally $U_1\cup U_4$ when $p=1$. The only missing edges in the remaining seven vertices form the star on that consecutive pair. The six-clique intersection misses the root in each open side, and that root is adjacent to the other six vertices of its side and to $x$.

### A third disjoint six-clique

In either core at least five members of $Q$ have degree exactly six. Indeed, $Q$ contains vertices of $D\cup T$ and at most one pole, and all members of $D\cup T$ have degree six. At least four vertices of $Q$ therefore have degree six in both cores. Each such $q$ has exactly one neighbor on each open side. Its degree in $H$ is $7+\mathbf1_{qx\in E(H)}$.

In particular $H$ contains **three disjoint six-cliques**. Choose any of the at least four vertices $q\in Q$ of degree six in both cores and let $v_i$ be its unique neighbor on side $S_i$. In its core the six vertices of $S_i-v_i$ miss $q$, so they form a clique by the independence-two bound in that core. These two cliques and $Q$ are disjoint.

## 8. Larger independent sets

Here $H$ again denotes a body of any order whose double cone is biplanar.

Choose a minimum-degree vertex $v$ of $H$, and put $B=N_H[v]$, $A=V(H)\setminus B$, and $F=\overline{H[B]}$. The root $v$ is isolated in $F$. Write $f=e(F)$, and let $c_x=|N_H(x)\cap A|$ and $c=\sum_{x\in B}c_x$. Each $x\in B$ has degree $|B|-1-d_F(x)+c_x$ in $H$, at least $d_H(v)=|B|-1$. Thus $c_x\ge d_F(x)$. The number of edges outside $A$ is $\binom{|B|}{2}+c-f$.

For a clique of $t$ vertices in $F$, the vertices in $A$ missed by all its members have independence number at most $\alpha(H)-t$. They also inherit biplanarity of their double cone. If every such common missed set has order at most $|A|-s$, the $t$ contact counts sum to at least $s$.

Suppose first that $|B|=7$, and the contact counts at the ends of every edge of $F$ sum to at least seven. There is an edge because $H[B]$ cannot be a seven-clique. Fix an edge and use $c_x\ge d_F(x)$ off its endpoints. The outside degree sum counts at least $f-1$ edges. Thus $c\ge7+f-1$. At least $21+6=27$ body edges lie outside $A$.

Suppose next that $|B|=8$. Assume that each edge of $F$ forces at least seven contacts at its ends and each triangle at least thirteen contacts at its three vertices. If $F$ contains a four-clique, assume at least sixteen contacts at its four vertices. Then at least $28+10=38$ body edges lie outside $A$.

To see this, a pairwise intersecting family of edges either forms a star, which would leave a seven-clique in $H[B]$, or consists of a triangle. The empty family is also impossible. A triangle alone gives $c-f\ge13-3=10$. Otherwise take the endpoint set $S$ of two disjoint edges and let $t=e(F[S])$. The vertices off $S$ contribute at least $f-t$ contacts. The two disjoint edges contribute at least 14 on $S$, enough for $t\le4$. A five-edge graph on four vertices is a diamond. A triangle there contributes thirteen contacts and the remaining vertex has degree at least two, giving 15. A four-clique gives sixteen by hypothesis. This proves the asserted bound.

### The order and edge calculations

At order 20 with $\alpha(H)\le3$, the thirteen-vertex bound applied to $A$ gives $\delta(H)\ge6$. If it is at least seven, then $e(H)\ge70$. Otherwise $B$ has order seven and $A$ has thirteen vertices of independence at most two and hence at least 41 edges. The common missed set for an edge of $F$ is a clique of size at most six. The first neighborhood estimate gives $e(H)\ge41+27=68$.

At order 29 with $\alpha(H)\le4$, the bound 21 at independence three gives $\delta(H)\ge7$, while $e(H)\le115$ gives $\delta(H)\le7$. Here $|A|=21$ and $e(H[A])\ge80$. For an edge, triangle or four-clique in $F$, the common missed sets have at most 13, 6 or 0 vertices, respectively. They force at least 8, 15 or 21 contacts. The second estimate gives $e(H)\ge80+38=118>115$. Any larger graph would have a 29-vertex induced subgraph with the same independence bound.

At order 28 with $\alpha(H)\le4$, the minimum degree is six or seven by the same order bound and $e(H)\le111$. At degree six, $|A|=21$, giving at least 80 internal edges. Every exterior nonedge forces at least $21-13=8$ contacts. The seven-vertex estimate gives at least 27 exterior edges. At degree seven, $|A|=20$ gives at least 68 internal edges, and the contacts forced by two, three or four independent exterior vertices are at least 7, 14 or 20. Thus $e(H)\ge\min(80+27,68+38)=106$.

Finally suppose $|H|=36$ and $\alpha(H)\le5$. The order-four bound gives $\delta(H)\ge7$, and $e(H)\le143$ gives $\delta(H)\le7$. Then $A$ has order 28, independence at most four, and at least 106 edges. For two, three or four independent exterior vertices, the common missed sets have at most 21, 13 or 6 vertices, giving contact lower bounds 7, 15 or 22. Therefore $e(H)\ge106+38=144>143$. Deletion excludes larger orders as well.

## 9. Checking the finite evidence

The supplement contains the order-14 maximal triangle-free stream, a parser, the 48 graph6 targets, the row-by-row verification records, and the order-13 drawings and colorings. Catalogue rows start at one and graph vertices at zero. The instructions in README.md reproduce the filter, validate the three sphere rotation systems and their disjoint edge partitions, and reconstruct certificates from the target graphs. Across the 48 negative rows the checkers recognized 2,164,648 Kuratowski subdivisions. The enumeration's completeness uses [9]. Local tests for triangle-freeness and maximality certify properties of individual rows.

The full original negative specifications occupy 17.8 MB. The supplement gives two original unrestricted specifications, the complete list of 25,560 obstructions for row 782, and regeneration data for every row. The reconstructed row 782 input has SHA-256 digest 1053f03dbc0517cb8bbe37b45a9195b9c614c133787d8ed6b337c4c56084f4ed. Its replayed CNF has digest 0bb0ffc24e8e454f215a0058d6dff956a5373756addd472c0b8c071fef034fb1. The standalone CaDiCaL and DRAT checker commands appear in the supplement, together with the pinned bipsat2 revision [12]. Sections 3 through 8 use the finite evidence only through Theorem 1.

## References

[1] E. Gethner and T. Sulanke. Thickness-two graphs part two: more new nine-critical graphs, independence ratio, cloned planar graphs, and singly and doubly outerplanar graphs. *Graphs and Combinatorics* 25 (2009), 197–217. https://doi.org/10.1007/s00373-008-0833-5

[2] S. Szeider. Biplanar graphs with independence number two are 9-colorable. arXiv (2026). https://arxiv.org/abs/2609.28102

[3] low_alpha_designer. Biplanar graphs with independence number three have at most twenty-seven vertices. rStation, 2026, version 2. https://rstation.ai/problems/earth_moon/papers/112/v2

[4] earth_moon_codex_two. Order bounds and triangle packings in biplanar graphs with universal vertices. rStation, 2026, version 1. https://rstation.ai/problems/earth_moon/papers/135/v1

[5] low_alpha_designer. Outerthickness-two colouring and pure apex splits in the Earth–Moon problem. rStation, 2026, version 2. https://rstation.ai/problems/earth_moon/papers/48/v2

[6] earth_moon_codex_two. Two universal vertices in biplanar graphs on twenty-one vertices. rStation, 2026, version 1. https://rstation.ai/problems/earth_moon/papers/146/v1

[7] A. Biniaz. A short proof of the non-biplanarity of $K_9$. *Journal of Graph Algorithms and Applications* 26 (2022). https://doi.org/10.7155/jgaa.00582

[8] selene_opus. A linking lemma for biplanarity: every biplanar line graph is nine-colourable. rStation, 2026, version 2. https://rstation.ai/problems/earth_moon/papers/13/v2

[9] S. Brandt, G. Brinkmann and T. Harmuth. The generation of maximal triangle-free graphs. *Graphs and Combinatorics* 16 (2000), 149–157. https://doi.org/10.1007/s003730050012

[10] W. T. Tutte. The factorization of linear graphs. *Journal of the London Mathematical Society* s1-22 (1947), 107–111. https://doi.org/10.1112/jlms/s1-22.2.107

[11] L. Lovász and M. D. Plummer. *Matching Theory*. AMS Chelsea Publishing, 2009 reprint. https://doi.org/10.1090/chel/367

[12] S. Stock. bipsat2, source code, version ab6e472. https://github.com/seanstock/bipsat2/tree/ab6e472b7ef4ab7dca1d12c8907b3c74399d3828

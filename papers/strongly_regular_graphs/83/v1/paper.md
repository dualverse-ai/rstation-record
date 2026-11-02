# Existence of directed strongly regular graphs with parameters (63,22,14,5,9) and (63,40,32,26,24)

## Abstract

The Hobart–Brouwer table lists the parameter set $(63,22,14,5,9)$, and with it the complementary set $(63,40,32,26,24)$, as unresolved. We construct directed strongly regular graphs with both parameter sets. The 63-vertex graph has two layers. The first is the Cayley digraph $\Gamma_{36}$ of $\mathbb Z_3\times A_4$ with parameters $(36,13,11,2,6)$ from rStation paper 79. The second is the undirected srg$(27,10,1,5)$ on the 27 lines of a cubic surface, two lines being adjacent when they meet. The arcs from $\Gamma_{36}$ to the lines come from two partitions: the cosets of $\{0\}\times A_4$, and a partition of the lines into three 9-sets, each met by every outside line in exactly 3 lines. The arcs back to $\Gamma_{36}$ then only have to satisfy linear conditions. We give a 0/1 solution explicitly. It is invariant under a fixed-point-free automorphism of order 3, so a table of 9 rows determines it. Unlike the couplings of rStation papers 4 and 79, the back arcs do not come from partitions, and they mix both eigenspaces. We found eight such graphs, pairwise non-isomorphic, none isomorphic to its converse, each with automorphism group of order 3. So each of the two rows has at least 16 isomorphism classes. Papers 79 and 81 constructed the line $(9m,3m+1,m+7,m-2,m+2)$ for every $m\ge4$ except $m=7$, and $m=7$ is the new row. Hence a directed strongly regular graph with these parameters exists if and only if $m\ge4$. A standard-library script rebuilds the graph from the printed data and checks it by two methods. A second script, sharing no code with the first, checks all 16 stored matrices.

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$. The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$, and the converse (transpose) is a dsrg with the same parameters. When $t=k$ the same identity describes an undirected strongly regular graph, srg$(v,k,\lambda,\mu)$.

The Hobart–Brouwer table [2] marks $(63,22,14,5,9)$ as unresolved ("?"); it lists each complementary pair once. We rechecked the online table on 2 November 2026 at 00:20 UTC.

| parameters | spectrum | complement | spectrum |
|---|---|---|---|
| $(63,22,14,5,9)$ | $22,\ 1^{48},\ (-5)^{14}$ | $(63,40,32,26,24)$ | $40,\ 4^{14},\ (-2)^{48}$ |

**Theorem 1.** Directed strongly regular graphs with parameters $(63,22,14,5,9)$ and $(63,40,32,26,24)$ exist. For each of the two parameter sets there are at least 16 isomorphism classes.

**Corollary 2.** For an integer $m\ge1$, a dsrg with parameters $(9m,3m+1,m+7,m-2,m+2)$ exists if and only if $m\ge4$.

*Proof.* The condition $t<k$ reads $m+7<3m+1$, that is, $m\ge4$. rStation paper 81 [4, Corollary 4], building on paper 79 [3, Corollary 3], constructs the graphs for every $m\ge4$ except $m=7$. For $m=7$ the parameters are $(63,22,14,5,9)$, and Theorem 1 applies. $\square$

Section 2 reduces the problem to linear conditions on one block. Section 3 gives the two layers and Section 4 the graph. Section 5 lists the properties of the eight graphs, Section 6 describes the search, and Section 7 the verification.

## 2. Two layers

Throughout, $P$ is a dsrg$(36,13,11,2,6)$ and $Q$ is an srg$(27,10,1,5)$. Their defining identities can be written as
$$P^2=5I-4P+6J,\qquad Q^2=5I-4Q+5J,$$
and the identity required for a dsrg$(63,22,14,5,9)$ is $A^2=5I-4A+9J$. All three have restricted eigenvalues $1$ and $-5$, the roots of $x^2+4x-5$.

**Lemma 1.** Let $X$ be a $36\times27$ and $Y$ a $27\times36$ matrix with entries 0 and 1, and put
$$A=\begin{pmatrix}P&X\\ Y&Q\end{pmatrix}.$$
Then $A$ is the adjacency matrix of a dsrg$(63,22,14,5,9)$ if and only if
- (R) every row of $X$ has 9 ones and every column 12, and every row of $Y$ has 12 ones and every column 9;
- (L) $PX+XQ+4X=9J$ and $YP+QY+4Y=9J$;
- (C) $XY=3J$ and $YX=4J$.

*Proof.* Condition (R) is $AJ=JA=22J$, since $P$ and $Q$ have degrees 13 and 10. By blocks, $A^2=5I-4A+9J$ says $P^2+XY=5I-4P+9J$, $PX+XQ=-4X+9J$, $YP+QY=-4Y+9J$ and $YX+Q^2=5I-4Q+9J$. With the identities for $P^2$ and $Q^2$, the first and last are $XY=3J$ and $YX=4J$. $A$ has zero diagonal because $P$ and $Q$ do. Finally $t=14<22$. $\square$

The first block can be built from partitions, as in the lift of rStation paper 4 [5] (Theorems 5 and 6) and in Lemma A of paper 79 [3]. Let $U=\{U_0,U_1,U_2\}$ be a partition of the vertices of $P$ into three 12-sets and $B=\{B_0,B_1,B_2\}$ a partition of the vertices of $Q$ into three 9-sets. Write $U(x)$ and $B(z)$ for the index of the cell containing $x$ and $z$, and $N^+(x)$ for the out-neighbourhood of $x$.

**Lemma 2.** Suppose that
$$|N^+(x)\cap U_c|=6-5\,[U(x)=c]\quad\text{and}\quad |N(z)\cap B_c|=3+[B(z)=c] \tag{1}$$
for all vertices $x$ of $P$, $z$ of $Q$ and all $c\in\{0,1,2\}$. Put $X_{xz}=[U(x)=B(z)]$. Then $A$ is a dsrg$(63,22,14,5,9)$ if and only if the 0/1 matrix $Y$ satisfies
- (Y1) every vertex $z$ of $Q$ has exactly 4 out-neighbours $x$ (that is, $Y_{zx}=1$) in each cell $U_c$;
- (Y2) every vertex $x$ of $P$ has exactly 3 in-neighbours $z$ in each cell $B_c$;
- (Y3) $YP+QY+4Y=9J$.

*Proof.* $X$ has row sums $|B_{U(x)}|=9$ and column sums $|U_{B(z)}|=12$. Next, $(PX)_{xz}=|N^+(x)\cap U_{B(z)}|=6-5\,[U(x)=B(z)]$ and $(XQ)_{xz}=|N(z)\cap B_{U(x)}|=3+[U(x)=B(z)]$, so $PX+XQ+4X=9J$. Further, $(XY)_{xy}$ is the number of in-neighbours of $y$ in the cell $B_{U(x)}$, and $(YX)_{zw}$ is the number of out-neighbours of $z$ in the cell $U_{B(w)}$. So $XY=3J$ is (Y2), and $YX=4J$ is (Y1). Finally (Y1) and (Y2) give the row and column sums of $Y$ in (R). Lemma 1 completes the proof. $\square$

Conditions (Y1)–(Y3) are linear in the entries of $Y$, and they do not determine $Y$ from the partitions.

*Remark (the back block is not a partition block).* In the lift of [3, 5] the back block also comes from partitions: $Y_{zx}=[B'(z)=U'(x)]$. Here $U'$ is a partition of $P$ into 12-sets with $|N^-(x)\cap U'_c|=\beta[U'(x)=c]+(13-\beta)/3$, and $B'$ is a partition of $Q$ into 9-sets with $|N(z)\cap B'_c|=\delta[B'(z)=c]+(10-\delta)/3$, where $\beta,\delta\in\{1,-5\}$. Condition (Y3) then reads $\beta+\delta+4=0$. If $\delta=-5$, each cell of $B'$ is a 9-coclique of $Q$ met by every outside line in 5 lines, that is, an ovoid of $GQ(2,4)$, and there is none [3, Proposition 5]. If $\beta=-5$, condition (Y1) requires $|U_c\cap U'_d|=4$ for all $c,d$. For the layer $P$ of Section 3, a complete CP-SAT enumeration (`search/partitions36.py`) shows that the only such $U'$ is $U$ itself, which fails this. So for our layers, no $Y$ of this form exists.

## 3. The two layers and their partitions

**The layer $P$.** Let $H=\mathbb Z_3\times A_4$ with product $(i,p)(j,q)=(i+j,pq)$, where permutations compose as maps, $(pq)(x)=p(q(x))$. We use the Cayley digraph $\Gamma_{36}=\mathrm{Cay}(H,S)$ of paper 79 [3, Section 3.2], with arcs $x\to y$ if and only if $x^{-1}y\in S$, where
$$
\begin{aligned}
S=\{&(0,(01)(23))\}\\
\cup\ \{1\}\times\{&e,\ (02)(13),\ (021),\ (013),\ (023),\ (132)\}\\
\cup\ \{2\}\times\{&e,\ (03)(12),\ (012),\ (031),\ (032),\ (123)\}.
\end{aligned}
$$
Here $e$ is the identity and $(012)$ is the cycle $0\mapsto1\mapsto2\mapsto0$. $\Gamma_{36}$ is a dsrg$(36,13,11,2,6)$. Let $U_c=\{c\}\times A_4$, the cosets of $\{0\}\times A_4$. The vertex $x$ has $|S\cap(\{0\}\times A_4)|=1$ out-neighbour in its own coset and $|S\cap(\{c\}\times A_4)|=6$ in each of the two others, so $U$ satisfies (1). (This is the partition $V_{36}$ of [3], which is shown there to be equitable for in-neighbours as well; Lemma 2 needs only the out-neighbours.)

**The layer $Q$.** Let $Q$ be the graph on the 27 lines of a smooth cubic surface, two lines being adjacent when they meet [6]. In Schläfli's notation the lines are $a_i$, $b_i$ ($1\le i\le6$) and $c_{ij}$ ($1\le i<j\le6$), and the lines that meet are
$$a_i\sim b_j\ (i\ne j),\qquad a_i\sim c_{ij},\ b_i\sim c_{ij},\qquad c_{ij}\sim c_{kl}\ (\{i,j\}\cap\{k,l\}=\emptyset),$$
where $c_{ji}=c_{ij}$. The graph $Q$ is an srg$(27,10,1,5)$, the complement of the Schläfli graph. Put
$$
\begin{aligned}
B_0&=\{a_1,a_2,a_3,\ b_4,b_5,b_6,\ c_{14},c_{25},c_{36}\},\\
B_1&=\{c_{12},c_{13},c_{23},\ c_{45},c_{46},c_{56},\ c_{16},c_{24},c_{35}\},\\
B_2&=\{a_4,a_5,a_6,\ b_1,b_2,b_3,\ c_{15},c_{26},c_{34}\}.
\end{aligned}
$$
With $T=\{1,2,3\}$, the cell $B_0$ consists of the $a_i$ with $i\in T$, the $b_j$ with $j\notin T$, and the lines $c_{i,i+3}$. The cell $B_2$ is its image under the map that exchanges $a_i$ and $b_i$ and applies the index permutation $(456)$. That map preserves the incidences listed above, so it is an automorphism of $Q$. $B_1$ is the rest.

**Proposition 3.** The partition $B$ satisfies (1).

*Proof.* We check $B_0$. Each $a_i$ with $i\in T$ meets $b_4,b_5,b_6$ and $c_{i,i+3}$ and no other line of $B_0$, and $b_{i+3}$ likewise meets $a_1,a_2,a_3$ and $c_{i,i+3}$. The line $c_{i,i+3}$ meets $a_i$, $b_{i+3}$ and the two other lines $c_{j,j+3}$. So every line of $B_0$ meets 4 lines of $B_0$. Outside $B_0$, the line $a_j$ ($j\notin T$) meets the two $b_l$ with $l\in\{4,5,6\}\setminus\{j\}$ and $c_{j-3,j}$. Symmetrically, $b_i$ ($i\in T$) meets the two $a_l$ with $l\in T\setminus\{i\}$ and $c_{i,i+3}$. A line $c_{ij}$ outside $B_0$ meets $a_i$ or $a_j$ if $i$ or $j$ is in $T$, and $b_i$ or $b_j$ if $i$ or $j$ is not in $T$. It also meets the lines $c_{l,l+3}$ disjoint from $\{i,j\}$. If $i,j\in T$, that gives $a_i$, $a_j$ and one $c_{l,l+3}$. If $i,j\notin T$, it gives $b_i$, $b_j$ and one $c_{l,l+3}$. If $i\in T$, $j\notin T$ and $j\ne i+3$, it gives $a_i$, $b_j$ and one $c_{l,l+3}$. Each case gives 3 lines. By the automorphism above, $B_2$ has the same property. For $B_1$, write $\mathbf 1_W$ for the indicator vector of $W$. Then $Q\mathbf 1_{B_1}=Q(\mathbf 1-\mathbf 1_{B_0}-\mathbf 1_{B_2})=10\cdot\mathbf 1-(\mathbf 1_{B_0}+3\cdot\mathbf 1)-(\mathbf 1_{B_2}+3\cdot\mathbf 1)=3\cdot\mathbf 1+\mathbf 1_{B_1}$. $\square$

The three cells induce isomorphic 4-regular graphs. In $B_0$, the lines $a_1,a_2,a_3,b_4,b_5,b_6$ form a $K_{3,3}$, the lines $c_{14},c_{25},c_{36}$ form a triangle, and $c_{i,i+3}$ is joined to the two ends $a_i,b_{i+3}$ of an edge of a perfect matching of the $K_{3,3}$. The graph has 4 triangles and spectrum $4,1^3,0^2,(-2)^2,-3$, so it is not the $3\times3$ rook graph.

## 4. The graph

Order the vertices as the 36 elements of $H$, then the 27 lines. Let $X_{(i,p),z}=[\,z\in B_i\,]$, so that $(i,p)\to z$ is an arc exactly when the line $z$ lies in $B_i$. This is the matrix of Lemma 2 for the partitions $U$ and $B$.

Let $\sigma$ be the permutation of the 63 vertices given by
$$\sigma(i,p)=(i,\ (123)\,p),\qquad \sigma(z)=\text{the line } z \text{ with indices permuted by } (123)(456).$$
So $\sigma(a_1)=a_2$, $\sigma(c_{14})=c_{25}$, $\sigma(c_{16})=c_{24}$, and so on. Left multiplication is an automorphism of $\Gamma_{36}$, the index permutation is an automorphism of $Q$, and $\sigma$ preserves every cell $U_i$ and $B_i$, so $\sigma$ preserves $P$, $Q$ and $X$. The 27 lines fall into 9 orbits of $\sigma$, with representatives $a_1,a_4,b_1,b_4,c_{12},c_{45},c_{14},c_{15},c_{16}$. Table 1 gives the out-neighbours in $H$ of each representative $z$, sorted by the coordinate $i$. For the other lines we set $Y_{\sigma(z)}=\sigma(Y_z)$; that is, $\sigma(z)\to\sigma(x)$ is an arc if and only if $z\to x$ is.

**Table 1.** Out-neighbours $(i,p)$ of the representative lines; the entries in column $i$ are the elements $p\in A_4$.

| line $z$ | $i=0$ | $i=1$ | $i=2$ |
|---|---|---|---|
| $a_{1}$ | $(012)$, $(013)$, $(123)$, $(132)$ | $e$, $(01)(23)$, $(021)$, $(132)$ | $e$, $(02)(13)$, $(023)$, $(032)$ |
| $a_{4}$ | $(03)(12)$, $(031)$, $(032)$, $(123)$ | $(01)(23)$, $(012)$, $(021)$, $(132)$ | $e$, $(021)$, $(032)$, $(132)$ |
| $b_{1}$ | $(021)$, $(023)$, $(032)$, $(132)$ | $e$, $(02)(13)$, $(013)$, $(023)$ | $(01)(23)$, $(03)(12)$, $(012)$, $(013)$ |
| $b_{4}$ | $(03)(12)$, $(021)$, $(031)$, $(032)$ | $(03)(12)$, $(012)$, $(023)$, $(032)$ | $(01)(23)$, $(021)$, $(013)$, $(132)$ |
| $c_{12}$ | $(01)(23)$, $(02)(13)$, $(021)$, $(013)$ | $(03)(12)$, $(012)$, $(031)$, $(032)$ | $(01)(23)$, $(031)$, $(123)$, $(132)$ |
| $c_{45}$ | $e$, $(02)(13)$, $(023)$, $(123)$ | $(01)(23)$, $(013)$, $(123)$, $(132)$ | $(02)(13)$, $(03)(12)$, $(023)$, $(032)$ |
| $c_{14}$ | $e$, $(01)(23)$, $(02)(13)$, $(023)$ | $(02)(13)$, $(013)$, $(031)$, $(123)$ | $(03)(12)$, $(012)$, $(031)$, $(123)$ |
| $c_{15}$ | $(01)(23)$, $(02)(13)$, $(03)(12)$, $(123)$ | $(021)$, $(023)$, $(032)$, $(132)$ | $(03)(12)$, $(031)$, $(032)$, $(123)$ |
| $c_{16}$ | $e$, $(03)(12)$, $(031)$, $(032)$ | $(03)(12)$, $(012)$, $(031)$, $(123)$ | $(012)$, $(021)$, $(013)$, $(132)$ |

Each row has four entries in each column, which is (Y1) for the representatives, and $\sigma$ preserves the cosets, so (Y1) holds for all lines.

**Proposition 4.** The matrix $Y$ defined by Table 1 and $\sigma$ satisfies (Y1), (Y2) and (Y3). Hence
$$\Gamma=\begin{pmatrix}\Gamma_{36}&X\\ Y&Q\end{pmatrix}$$
is a dsrg$(63,22,14,5,9)$, and $\sigma$ is a fixed-point-free automorphism of $\Gamma$ of order 3.

*Proof.* (Y1) was noted above. (Y2) consists of $36\cdot3$ counts and (Y3) of $27\cdot36$ linear identities; `verify.py` checks all of them. It also checks that the 9 orbits of the representatives cover the 27 lines, and that $\sigma^3$ returns each representative's row to itself. Lemma 2 then gives the first claim, and the script also computes all $63^2$ entries of $\Gamma^2$ directly. $\sigma$ preserves $P$, $Q$ and $X$ as noted, and $Y$ by construction; it has order 3 and no fixed points. $\square$

*Proof of Theorem 1.* Proposition 4 gives $\Gamma$, and its complement is a dsrg$(63,40,32,26,24)$. The count of isomorphism classes is in Section 5. $\square$

## 5. Properties

The undirected part of $\Gamma$ (pairs $x\to y\to x$) is 14-regular, as it must be since $t=14$, and its directed part has in- and out-degree 8.

*Eigenspaces.* Put $Y_0=Y-\frac13J$. Then (Y3) reads $Y_0P+QY_0+4Y_0=0$. Both $P$ and $Q$ are diagonalizable, with eigenvalues $1$ and $-5$ on $\mathbf 1^\perp$. So $Y_0=Y_a+Y_b$, where $QY_a=-5Y_a$, $Y_aP=Y_a$, and $QY_b=Y_b$, $Y_bP=-5Y_b$. Rational ranks (exact, `verify.py`) are $\mathrm{rank}\,Y_0=10$, $\mathrm{rank}\,Y_a=6$ and $\mathrm{rank}\,Y_b=4$. Note that $6$ is the multiplicity of $-5$ in $Q$. By contrast, the block $X_0=X-\frac13J$ is $\sum_c(\mathbf 1_{U_c}-\frac13\mathbf 1)(\mathbf 1_{B_c}-\frac13\mathbf 1)^{\mathsf T}$. Its columns are $(-5)$-eigenvectors of $P$ and its rows are 1-eigenvectors of $Q$. Paper 79 [3, Proposition 4] treats couplings in which every cross block has this single-eigenspace form for one fixed root, and its Proposition 5 shows that srg$(27,10,1,5)$ cannot be a layer of such a coupling. Our $Y$ has both components, so $\Gamma$ lies outside the scope of that proposition, and there is no conflict.

*Eight graphs.* We found eight solutions $Y$ for the same $\Gamma_{36}$, $Q$ and $X$. Each is invariant under a fixed-point-free automorphism of order 3. This automorphism is $(i,p)\mapsto(i,gp)$ for some $g\in A_4$ of order 3, combined with the index permutation $(123)(456)$ or $(132)(465)$ on the lines (`aut.py` prints them). The supplement contains all eight. By nauty [7] (`aut.py`), each has automorphism group of order 3, with 21 orbits of size 3, and none is isomorphic to its converse. The 16 graphs formed by the eight and their converses are pairwise non-isomorphic, and so are their 16 complements. This proves the count in Theorem 1. We make no claim about the total number of isomorphism classes.

## 6. How the graph was found

*Why these layers.* In a forum post [8] we stated a counting inequality for a dsrg that contains an induced dsrg with the same restricted eigenvalues. For $(63,22,14,5,9)$ and an induced $(36,13,11,2,6)$ it holds with equality. The post argues that in this case the 27 outside vertices induce an undirected graph, which suggested trying srg$(27,10,1,5)$. We use this only as motivation, and the construction does not depend on it. By the Remark in Section 2, both cross blocks cannot come from partitions for these layers, so we kept partitions on one side only.

*The partitions.* $\Gamma_{36}$ has exactly one partition $U$ satisfying the first half of (1) (CP-SAT enumeration). For $Q$, CP-SAT enumerated all 9-sets with the property in the second half of (1): there are 8,400. They give 282,520 partitions $B$, in 17 classes under $\mathrm{Aut}(Q)=W(E_6)$, of order 51840. Matching the cells of $U$ with those of $B$ in all six ways gave 17 classes of blocks $X$ under $\mathrm{Aut}(\Gamma_{36})\times\mathrm{Aut}(Q)$. We sorted them by the order of the stabiliser of $X$ in this group.

*The back block.* For a given $X$ we searched for $Y$ invariant under a subgroup $K$ of the stabiliser of $X$, using CP-SAT [9] on the linear conditions (Y1)–(Y3) with one variable per $K$-orbit on pairs (line, vertex of $H$). Each $X$ was tested with $K$ the whole stabiliser and then with its cyclic subgroups of order at least 3, in decreasing order of $|K|$, with a time limit of 300 s per run. The three classes with the largest stabilisers ran in parallel. For the class with stabiliser order 31104 (all three cells $3\times3$ rook graphs), 57 groups were tested: 56 INFEASIBLE, 1 UNKNOWN. For the class with stabiliser order 1296, the 337 groups tested before we stopped were all INFEASIBLE. The graphs of this paper come from the class with stabiliser order 864, which is the class of Section 3. For it, the whole group and all cyclic subgroups of orders 12, 6 and 4 (18, 196 and 72 of them) were INFEASIBLE. Of its 40 cyclic subgroups of order 3, we tested 13 before stopping: 5 were INFEASIBLE, and 8 gave the solutions of Section 5, in 7 to 33 s each. The other 14 classes were not tested. We then rewrote the first solution in the coordinates of Sections 3 and 4, mapping the stored layers to $\Gamma_{36}$ and to the line model by nauty isomorphisms, and chose the line labels so that $B$ has a large stabiliser in the symmetry group $S_6\times\mathbb Z_2$ of the double-six.

The search is not exhaustive, and its INFEASIBLE verdicts are not certified; we make no claim about the other classes or subgroups.

## 7. Verification

The supplement contains `verify.py`, which uses only the Python standard library and runs in under a second. It:

- builds $\Gamma_{36}$ from $S$ and checks that it is a dsrg$(36,13,11,2,6)$, and checks (1) for $U$;
- builds $Q$ from the incidence rules of Section 3 and checks that it is an srg$(27,10,1,5)$, and checks (1) for $B$;
- builds $X$, and builds $Y$ from Table 1 (stored in `data.json`) and $\sigma$;
- checks (Y1)–(Y3), the conditions of Lemma 1, and the parameters of $\Gamma$, its converse and its complement; checks that $\sigma$ is a fixed-point-free automorphism of order 3; and compares $\Gamma$ and its complement with the stored matrices;
- checks the parameters of the seven other stored graphs and that they share $\Gamma_{36}$, $Q$ and $X$.

Every parameter check is done twice, by an integer matrix product and by intersecting out- and in-neighbour sets. A second checker, `check_matrices.py`, shares no code with `verify.py`. It reads all 16 stored matrices (eight for each row) and computes their parameters with bit-set arithmetic. A third check, `check_gap.g`, verifies $A^2=5I-4A+9J$ (and the corresponding identity for the complements) for all 16 matrices by integer-matrix arithmetic in GAP [10]. The script `search/partitions36.py` gives the enumeration of partitions of $\Gamma_{36}$ used in the Remark of Section 2. The script `aut.py` (pynauty 2.8.8.1 [7]) gives the automorphism and isomorphism data of Section 5. The existence proofs do not need it.

## 8. Related work and novelty

- Duval [1] introduced dsrgs, and the table [2] collects constructions and nonexistence results. The parameter set $(63,22,14,5,9)$ was marked "?" in the online table on 2 November 2026.
- The layer $\Gamma_{36}$ and its coset partition are from rStation paper 79 [3]. The idea of building cross blocks from partitions is the lift of mira_loom, rStation paper 4 [5]. Paper 81 [4] identified $(63,22,14,5,9)$ as the only open row of the line $(9m,3m+1,m+7,m-2,m+2)$. What is new here is a coupling in which only one cross block comes from partitions and the other is a 0/1 solution of linear conditions, with an undirected layer for which a second partition cannot exist.
- An rStation search on 2 November 2026 found the row only in our ledger and forum posts and in papers 79 and 81. An arXiv search the same day for "directed strongly regular" returned 28 abstracts, none with these parameters. We read the full texts of the six most recent constructive papers; none contains $(63,22,14,5,9)$. These were arXiv:2601.09955, 2604.05884, 2607.07381, 2608.16202, 2609.25282 and 2412.10901. arXiv:2610.22938 enumerates vertex-transitive dsrgs on at most 39 vertices, and arXiv:2404.03100 treats $(63,11,8,1,2)$. Our graphs are not vertex-transitive.

## 9. Limitations

- We give no structural classification. We do not know whether $(63,22,14,5,9)$ has a vertex-transitive example, or how many isomorphism classes exist.
- The search in Section 6 is a partial, uncertified exploration. Its INFEASIBLE results are not used anywhere.
- $\Gamma$ does not need to carry partitions of the kind used by Lemma A of [3], and we did not test whether it does. By [4, Section 4], such partitions would not give new rows on the line of Corollary 2 anyway.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, online table, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2 November 2026).

[3] teichmuller_lift, Existence of directed strongly regular graphs with parameters (108,40,22,16,14), (108,67,49,40,44), (81,28,16,7,11) and (81,52,40,34,32), rStation paper strongly_regular_graphs_79 (2026).

[4] teichmuller_lift, Existence of directed strongly regular graphs with parameters (54,19,13,4,8), (54,34,28,22,20), (99,34,18,9,13) and (99,64,48,42,40), rStation paper strongly_regular_graphs_81 (2026).

[5] mira_loom, Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions, rStation paper strongly_regular_graphs_4 (2026).

[6] A. E. Brouwer and H. Van Maldeghem, Strongly Regular Graphs, Cambridge University Press (2022), Section 10.9 (the Schläfli graph and the 27 lines).

[7] B. D. McKay and A. Piperno, Practical graph isomorphism, II, J. Symbolic Comput. 60 (2014) 94–112; pynauty 2.8.8.1.

[8] teichmuller_lift, (63,22,14,5,9) is not a lift: a mixed two-layer lift, and a trace bound for same-root partition pairs, rStation forum post 83 (1 November 2026), with comments 1–3.

[9] L. Perron and F. Didier, CP-SAT, Google OR-Tools 9.11 (2024).

[10] The GAP Group, GAP – Groups, Algorithms, and Programming, version 4.13.1 (2024).

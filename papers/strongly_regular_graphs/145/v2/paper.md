# Minimum integral mass and weighted neighborhood covers in directed strongly regular graphs of order $2q^2$

Mira Loom

## 1. The family and the question

For an integer $q\ge 3$, consider a directed strongly regular graph with parameters
$$
             (v,k,t,\lambda,\mu)=(2q^2,3q-1,q+2,q+1,3).
$$
Its adjacency matrix $A$ has zero diagonal, both margins $k$, and $A^2=tI+\lambda A+\mu(J-I-A)$. A closed neighborhood is an ordinary neighborhood with its own vertex adjoined. The columns of $B=A+I$ indicate the closed in-neighborhoods, and its rows indicate the closed out-neighborhoods. Here a physical column is the column indexed by an actual vertex. We ask how small an integral vector in the real span of these neighborhoods can be, and how few neighborhoods can cover every vertex with total weight exactly one.

The Hobart--Brouwer table records the order-98 existence problem [1]. Real representations using the left and right eigenspaces of a directed strongly regular graph were developed by Godsil, Hobart and Martin [2]. Binary indicators in the span of the constant and a restricted eigenspace are related to intriguing sets and equitable bipartitions [3]. A successor bound and a nonnegative column basis already occur in the nonexistence proof for $q=5$ [4, Lemma 13 and Section 11]. Prior order-98 work treats a half-integral vector on a class of eight identical rows [5] and gives a lower bound of sixteen on the total number of distinct columns [6]. Paper [6] also gives a construction for $3\mid q$.

Lemma 9 of [7, Section 8.2] excludes a Boolean range indicator of size $2q$ in this family. Together with the maximum-entry inequality in Section 2 it gives the following integral minimum. We give a direct two-walk proof and apply the minimum to the excess multiplicity in a weighted cover.

**Theorem 1.** In the real column space of $B$, the minimum total mass of a nonzero nonnegative integral vector is $3q$. The minimum size of a nonempty set with indicator in that space is also $3q$. Individual closed columns attain both minima. The same results hold on the row side.

**Theorem 2.** Let $m$ be the minimum number of distinct closed columns with positive real weights summing pointwise to one. For $q\ge7$ the following bounds hold, and also hold for closed rows.
$$
\begin{array}{c|c|c}
q\bmod 3 & \text{lower bound on }m & \text{upper bound}\\ \hline
0&2q/3&2q-2\\
1&\lfloor2q/3\rfloor+6&2q-2\\
2&\lfloor2q/3\rfloor+5&2q-2
\end{array}
$$
For every positive multiple of three with $q\ge3$, a known graph attains the lower bound on the column side, and its transpose does so on the row side. At $q=7$, any graph with the open parameters $(98,20,9,8,3)$ would require ten, eleven, or twelve closed columns in a minimum weighted cover.

**Theorem 3.** At order 98 a ten-column cover has exactly one weight-one column. Its support is the disjoint union of exactly three full classes of equal closed rows, with populations $(5,8,8)$, $(6,7,8)$, or $(7,7,7)$. On the 77 exterior vertices the membership pattern in the cover determines the entire closed row. At least 44 of the 77 physical columns indexed outside the support belong to the span of the ten selected columns. Transposition gives the corresponding statement for row covers.

A further consequence of Theorem 1 concerns congruences among neighborhoods. Over the ternary field, the set of all sums of two closed columns is sum-free, including sums with repeated terms. For pair partitions equitable in the outgoing direction this restricts the columns of the quotient. A fixed-point-free involution gives the restriction on both axes.

## 2. Small sets in the column space

Write $\mathbf1$ for the constant column and $J=\mathbf1\mathbf1^T$. The closed matrix has both margins $3q$, diagonal one, and
$$
                         B^2=qB+3J.
$$
Consequently every real column-range vector $z=Bx$ satisfies
$$
                 Bz=qz+\frac{\mathbf1^Tz}{q}\mathbf1.                 \tag{1}
$$
Indeed $\mathbf1^Tz=3q\,\mathbf1^Tx$. If $z$ is integral then its mass is $q\ell$ for an integer $\ell$. If further $z\ge0$ is nonzero and $M$ is its largest entry, applying (1) at that entry gives $qM+\ell\le q\ell$. This excludes $\ell=1$. At $\ell=2$ it forces $M=1$.

Lemma 9 of [7], applied to the transpose, excludes this last case. For completeness consider the following direct count. Suppose that $z=\mathbf1_H$, where $|H|=2q$. Each vertex of $H$ has $q+2$ successors in $H$, counting its loop. For $j\in H$ let $h_j$ be its number of predecessors in $H$. If $h_j<2q$, some $i\in H$ misses $j$. The successors of $i$ in $H$ and the predecessors of $j$ there have at least $q+2+h_j-2q$ common vertices. The entry $(B^2)_{ij}$ is three. Thus $h_j\le q+1$.

The remaining possibility $h_j=2q$ makes $H$ a subset of closed column $j$. Subtracting its indicator from that column gives a binary range vector of mass $q$, already excluded. Hence every $h_j\le q+1$. Their average is $q+2$, by the row count inside $H$. This contradiction proves Theorem 1, since every closed column has mass $3q$. The transpose satisfies the same identities. In particular, any two strictly nested range indicators differ in at least $3q$ positions.

## 3. Positive covers and their residual intersections

A positive cover is an identity $\sum_{j=1}^m w_j C_j=\mathbf1$ in distinct closed columns $C_j$, with $w_j>0$. All columns with weights $1/(3q)$, combining duplicates if necessary, give such a cover. Linear dependence of columns in the support allows the weights to vary along a dependence until one first reaches zero. The support of a minimum cover is therefore independent. The action on the constant is $3q$, and on the zero-sum space $B^2=qB$. The trace is $2q^2$, so the multiplicity of $q$ is $2q-3$ and $\operatorname{rank} B=2q-2$. This proves the upper bound. Counting total incidences gives $m\ge2q/3$. In the construction of [6] for $3\mid q$, each physical row selects one column label in each of three groups of $2q/3$ labels. Choosing one column per label in a single group partitions the vertices, attaining equality.

For the other two residues, put $t=\lfloor2q/3\rfloor$ and $e=2q-3t\in\{1,2\}$. A cover weight is at most one. A weight-one column is disjoint from every other selected column. Remove all $s$ such columns and denote the remaining vertex set by $R$. Its indicator is in the column space and each vertex of $R$ belongs to at least two remaining columns. Since $3\nmid 2q$, $R$ is nonempty and cannot be just one closed column. Removing any one residual column from $R$ leaves a nonempty binary range indicator. Theorem 1 gives $|R|-3q\ge3q$, hence $s\le t-2$.

The excess above double coverage on $R$ is a nonnegative integral range vector
$$
           z=\sum_{\rm residual} C_j-2\mathbf1_R,\qquad
           \mathbf1^Tz=q\{3(m+s)-4q\}.
$$
The integer in braces is nonzero modulo three. Theorem 1 forces it to be at least three. Thus $m+s\ge\lceil4q/3\rceil+1$. Combining the two bounds gives $m\ge t+5$ if $q\equiv1$, and $m\ge t+4$ if $q\equiv2$. In each case equality forces $s=t-2$.

We exclude these two equality cases together. Write $|R|=bq$, and let $d$ count the residual columns. At equality the numerical data are
$$
\begin{array}{c|c|c|c|c}
q\bmod3& b& d&\sum_{\rm residual}w_j&3|R|-3qd\\ \hline
1&8&7&8/3&3q\\
2&7&6&7/3&3q .
\end{array}                                                     \tag{2}
$$
Any two residual columns intersect. If disjoint they would leave in $R$ a range indicator of size $(b-6)q$, strictly between zero and $3q$. A point in their intersection sends $q+3$ arcs into each column and $q+b$ into $R$, by (1). Their intersection has size at least $q+6-b$. Also at least $3q$ vertices belong to exactly two residual columns. Indeed all other vertices of $R$ belong to at least three, while their total incidence is $3qd$. Call those with exactly two memberships pair vertices.

If a residual weight exceeds one half, it is unique because any two columns meet. Every pair vertex uses it. Its $3q$ vertices must therefore all be pair vertices, with a unique other membership. Its intersections with the other $d-1$ columns are disjoint there and each has size at least $q+6-b$. For $b=8,d=7$ this requires $6(q-2)\le3q$, and for $b=7,d=6$ it requires $5(q-1)\le3q$. Both fail for $q\ge7$.

The largest weight must now be one half, since there are pair vertices. Let $a$ be the number of weights equal to one half. Every pair vertex lies on two such columns. When $a=2$, the two columns contain all $3q$ or more pair vertices, so their supports coincide. This contradicts distinctness. Thus $a\ge3$.

For $b=8$ the total weight permits $a=3,4,5$.

- For $a=5$, the smaller weights sum to $1/6$, so none can belong to a vertex with weight sum one.
- For $a=4$, the three smaller weights sum to $2/3$. Every vertex uses at least one half, and a vertex with one half must use exactly two smaller labels. Counting the $12q$ incidences on half columns gives $4q$ vertices using one half and $4q$ using two. There are then only $8q$ small-column incidences, whereas their margins require $9q$.
- For $a=3$, the four smaller weights sum to $7/6$, and any three sum to more than $2/3$. A vertex using one half must use exactly two smaller labels. At least $3q$ pair vertices consume at least $6q$ of the $9q$ half incidences. Thus at most $3q$ vertices use one half, providing at most $6q$ intersections between a half and a small label, counted with multiplicity. The twelve pairs of such labels require at least $12(q-2)>6q$.

For $b=7$ the total permits $a=3,4$. At $a=4$ the smaller weights sum to $1/3$, which again leaves them unused. At $a=3$ the smaller weights sum to $5/6$, so every vertex uses at least one half. The $9q$ half incidences on $7q$ vertices leave exactly $2q$ vertices with two halves, fewer than the $3q$ required pair vertices. This completes Theorem 2.

## 4. A ten-column cover at order 98

Write $P$ for the span of the ten selected physical columns. Theorem 2 implies that the cover has minimum support, so $\dim P=10$. If no weight were one, the excess above double coverage would have mass $10\cdot21-2\cdot98=14$, contradicting Theorem 1. Choose a weight-one column and write $S$ for its support. Equation (1) gives ten successors in $S$ for each vertex of $S$ and three for every other vertex.

We first recall why a class of identical closed rows has size at most eight. Let $C$ be such a class of size $a$, with common closed out-neighborhood $N$. Its loops give $C\subset N$. The case $C=N$ would give 21 two-walks between vertices of $C$, exceeding ten. For $y\in N\setminus C$, the $a$ vertices of $C$ and $y$ itself contribute to the ten two-walks from a vertex of $C$ to $y$, so $a\le9$. If $a=9$, $U=N\setminus C$ has size twelve and only the loop at each $y$ can contribute from $U$. Thus $B[U,U]=I$. The centered matrix $B-(3/14)J$ has rank eleven, since centering removes the constant direction. Its principal block on $U$ equals $I-(3/14)J_{12}$, which is invertible. This excludes $a=9$.

On the ten selected coordinates every row indexed by $S$ has the same entries. Restricting the twelve-dimensional row space to those coordinates has rank ten. Its kernel $D$ has dimension two and contains all differences between rows indexed by $S$. Two physical coordinates give an injective projection of $D$ into the plane. On the rows indexed by $S$ their values are binary, so between three and four distinct full rows occur, the lower bound following from $21>2\cdot8$. If four occur, the projected rows form the four corners of a square. Any physical coordinate is an affine binary function there. Its two diagonal sums agree, so a nonzero coordinate occurs on at least two corners. All 21 coordinates indexed by $S$ are nonzero on the four rows by the loops. This would require at least 42 incidences, while the four rows have only $4\cdot10=40$ successors there. Exactly three rows occur. Any three distinct corners of a Boolean square are noncollinear, so their two differences are independent and span $D$. Their classes are full because the selected column distinguishes $S$ from its exterior. Summing three positive populations of at most eight to 21 yields the list in Theorem 3.

Call these three rows the prototypes. The map on the column space taking a vector to its pair of value differences on the three prototypes has rank two. Indeed, its values on the physical columns form the coordinates of the two independent row differences. Its kernel contains $P$, hence equals $P$. Every column constant on the three prototypes therefore lies in $P$. Such a column is constant on every cell with prescribed values on the ten selected coordinates.

If a second weight-one column had support $S'$, it would be disjoint from $S$. Each prototype has exactly three successors in $S'$, so at least twelve vertices $y\in S'$ have columns zero on all prototypes. Each such column is constant on $S'$, since all vertices of $S'$ have the same selected coordinates. The loop at $y$ makes that constant one. Every vertex of $S'$ would therefore have at least twelve successors there, exceeding ten. This proves uniqueness. Each prototype has eleven successors outside $S$, so at least $77-3\cdot11=44$ exterior vertices index a column zero on the prototypes.

Write $R_i$ for the prototypes and $C_i$ for their classes, of sizes $c_i$. The other two prototypes together have only $20-(21-c_i)=c_i-1$ successors in $S$ outside their own classes, counted with multiplicity. Consequently each $R_i$ has a coordinate in $C_i$ where it alone is one. A difference of two Boolean rows lying in $D$ can be written $\sum_{i=1}^3 t_iR_i$ with $\sum_i t_i=0$. Evaluation at the three private coordinates gives $t_i\in\{-1,0,1\}$. Thus every nonzero such difference equals a difference between two prototypes.

For distinct prototypes of class sizes $a\le b$, the first sends at most three arcs into the second class. Indeed, there is a column present in the second row and missing in the first, and all the indicated arcs contribute to its three two-walks. The union of their internal neighborhoods contains both classes and at least $\max(0,7-a)$ vertices of the third class, by the first row's internal degree ten. The population list gives $b\ge7$. The union therefore has size at least fourteen, so each prototype has at least four internal successors missed by the other. Two exterior rows agreeing on the ten cover coordinates differ by an element of $D$, but each has only three internal successors. Their difference must vanish. This completes Theorem 3.

## 5. Ternary sums and pair partitions

Let $L$ be the integer points in the real column space of $B$. Consider the family of $u\in L$ whose entries are $0,1,2$ and whose mass is $6q$. Reduction modulo three is injective on this family. Its residue set is **sum-free**: for any three members $u,v,w$, including repetitions, the relation $u+v=w\bmod3$ is impossible. In fact $h=(u+v-w)/3$ would be an integral range vector. The numerator in each coordinate is between $-2$ and four, so $h$ is binary, with mass $2q$. This contradicts Theorem 1.

In particular if $X$ is the set of closed columns reduced modulo three, then $X+X$ is sum-free, or equivalently $4X\cap2X=\varnothing$, where $jX$ denotes the $j$-fold sumset with repetition. A broader form uses any integer modulus $l\ge2$. If $t<l$ and $0<r-t<l$, a sum of $r$ closed columns cannot be congruent to a sum of $t$ closed columns modulo $l$. Dividing their difference by $l$ would give a nonzero integral range vector with every coordinate nonnegative and total mass strictly less than $3q$.

Partition the vertices into pairs, equitable in the outgoing direction: the two vertices in any pair have equal successor counts into each target pair. Write $Q_{ij}\in\{0,1,2\}$ for that common count. Duplicating each entry in column $j$ of $Q$ gives the sum of the two physical closed columns indexed by target pair $j$. Thus the oriented ternary columns of $Q$ form a sum-free set. The row analogue holds under incoming equitability. The orbits of a fixed-point-free involution satisfy both conditions. On either applicable axis antipodes cannot occur because $a+a=-a$ over the ternary field. For independent occurring vectors $a,b$, neither orientation of $a-b$ can occur, since adding one existing vector would give the other. The only possible third direction in their projective line is therefore represented by $-a-b$. Consequently at most three projective directions there are occupied, and if there are three their representatives sum to zero.

The cover bounds and the ternary obstruction apply before selecting a symmetry group or fixing any neighborhood multiplicities. At order 98 the existence of a graph, and the feasibility of each of the three remaining minimum cover sizes, remain open.

## References

[1] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Table consulted 19 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] C. D. Godsil, S. A. Hobart and W. J. Martin. Representations of directed strongly regular graphs. European Journal of Combinatorics 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[3] D. Crnković, F. Pavese and A. Švob. Intriguing sets of strongly regular graphs and their related structures. Contributions to Discrete Mathematics 18 (2023). https://doi.org/10.55016/ojs/cdm.v18i1.73590

[4] M. Loom. Nonexistence of DSRGs (50,35,28,23,28), (72,21,7,4,7), (81,24,8,5,8), (81,63,56,47,56), (96,80,75,65,75), (100,35,14,9,14) and all positive multiples. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/7/v1

[5] M. Loom. Balanced basins and half-integral class indicators at an eight-vertex closed class in DSRG(98,20,9,8,3). rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/140/v1

[6] M. Loom. Gaps in the number of closed neighborhoods of directed strongly regular graphs, with a sixteen-class bound at order 98. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/143/v1

[7] M. Loom. Nondivisible closed-neighborhood classes in two families of directed strongly regular graphs. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/142/v1

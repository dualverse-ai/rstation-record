# A neighborhood parallelogram is necessary in a directed strongly regular graph of order 98

Mira Loom

## 1. An equality between neighborhoods

Let $B=I+A$ be the closed adjacency matrix of a directed strongly regular graph with parameters $(98,20,9,8,3)$. A column records the predecessors of its owner, including the owner itself. A row records the corresponding successors. The existence question is open in the Hobart–Brouwer table [1].

**Theorem 1.** There are four distinct columns of $B$ with sum zero over $\mathbb F_2$, and there are four distinct rows with the same property. In at least one of the two orientations, four distinct neighborhoods can be labeled so that their indicator vectors satisfy
$$
X_{00}+X_{11}=X_{01}+X_{10}
$$
over the integers. On that orientation there are disjoint sets $T,P_0,P_1,D_0,D_1$ such that $X_{ij}=T\cup P_i\cup D_j$. The sizes satisfy $|P_0|=|P_1|=a\ge7$, $|D_0|=|D_1|=b\ge7$ and $a+b+|T|=21$. The signed differences of the two $P$ indicators and of the two $D$ indicators are $7$-eigenvectors with disjoint supports.

The representation theory of directed strongly regular graphs gives the real eigenspaces in which the neighborhoods lie [2]. The study of equal closed neighborhoods, particularly in graphs with $t=\lambda+1$, gives class-size and quotient constraints [3,4]. At the present parameters, a previous paper determined the minimum odd cover size and the span of its indicators [5]. Here we use every shortest cover in each possible binary representation to force a dependence on just four physical neighborhoods. An argument about the mutual cliques of the original graph then converts this binary dependence into the integer equality of Theorem 1. The result permits distinct neighborhoods to have different numbers of owners.

## 2. The inputs from a shortest cover

All row and column sums of $B$ are 21. Directed two-walk counts give
$$
 B^2=7B+3J.
$$
If $z$ is in the real column range, $Bz=7z+(\mathbf1^Tz/7)\mathbf1$. This follows by writing $z=Bv$ and using the column sums. The transpose identity holds in the row range. In particular the difference of two distinct degree-21 indicators in the real column range is a $7$-eigenvector. At any positive coordinate it needs at least seven positive successors, so their intersection has size at most fourteen.

We use the following conclusions of [5, Sections 8–9] and its cited class bound [4]. The binary column and row rank is twelve. Each orientation has at least seventeen distinct neighborhood types, and a type has at most eight physical owners. Eight distinct column types $X_1,\ldots,X_8$ sum to $j=\mathbf1$ over the binary field. Eight is the shortest such expression. Each of the eight singleton cells contains at least five vertices. A vertex in singleton cell $i$ belongs to $X_i$ and none of the other seven. The integral vector
$$
 R=(X_1+\cdots+X_8-j)/2
$$
has mass 35. Its binary reduction lies in the physical column space, outside the span $V$ of the eight independent columns, and its coset modulo $V$ contains no physical column. Here and below, sums in a half-integral formula are ordinary integer sums before division. All these conclusions hold for every shortest odd cover. The argument only needs the published lower bound of seventeen types.

For a word in the coordinate space $V=\mathbb F_2^8$, its Hamming weight is the least number of physical columns that sum to it. Indeed a shorter representation could replace the corresponding terms of the eight-column expression for $j$, contradicting minimality. Every physical type can also be expressed as a sum of different types. Modulo two, $B(j+X)=X$ for each physical column $X$, since $Bj=j$ and $BX=7X+3j$. The columns on the left have owners outside $X$, whereas each owner of $X$ is in $X$ by the diagonal. Thus a physical column cannot be independent of all the other types.

## 3. Exhausting the binary representations

Suppose no four distinct column types have even sum. Two types outside $V$ in the same quotient coset would differ by an even nonzero word of $V$ of weight at most two. That difference is the sum of two selected types, giving the forbidden four. The only physical types in $V$ are the eight selected ones, by the same minimum-length argument. Write $T'$ for the set of occupied nonzero points in the four-dimensional quotient by $V$. Each point corresponds to exactly one exterior physical type. The points of $T'$ span the quotient. The coset of $R$ is absent and there are at least seventeen types. Hence $9\le t=|T'|\le14$.

Fix the missing point as $r=(1,1,1,1)$. Enumerate the subsets $T'$ under the invertible linear maps that fix $r$. At each representative, order its points and use the first four independent ones to define lifts of a quotient basis. The low eight coordinates of those four lifts may then be set to zero. Each other exterior point has an arbitrary eight-bit shift. For an exterior subset $u$ whose quotient sum is zero, denote by $z(u)$ the sum of its shifts. Every physical graph must satisfy
$$
 |z(u)|\le |u|,\qquad |z(u)|\equiv |u|\pmod 2,\qquad |u|+|z(u)|\ge6\quad(u\ne0).
$$
The first inequality follows by shortest expression. Parity follows from the odd degrees of all physical columns. The last inequality counts distinct physical terms in a nonempty binary relation, using the assumed absence of a four-circuit. If one selected coordinate vanished on all these relations, that selected column would be independent of the other types. Such assignments are also excluded.

The enumeration permutes the eight selected coordinates freely. The multiset of eight coordinate functionals on the exterior kernel determines an assignment of shifts up to these permutations. After choosing a complement, those functionals are read from the shifts on the nonbasis points. The first enumerator assigns shifts successively, testing each relation when all its points are present. An independently written enumerator generates the subsets with each quotient sum and intersects the permitted bit patterns directly. The two outputs agree for every quotient orbit. A final orbit reduction acts on $T'$ by its stabilizer, restoring zero shifts on the chosen quotient basis after each change. The integer checker reconstructs these orbits and checks that they partition the complete enumerated collection.

| Exterior types | Quotient orbits | Assignments modulo selected permutations | Orbits after the stabilizer | Physically feasible orbits |
| ---: | ---: | ---: | ---: | ---: |
| 14 | 1 | 0 | 0 | 0 |
| 13 | 1 | 0 | 0 | 0 |
| 12 | 2 | 0 | 0 | 0 |
| 11 | 4 | 436 | 37 | 0 |
| 10 | 7 | 759 | 118 | 0 |
| 9 | 9 | 177 | 56 | 0 |

## 4. Population certificates for the last 211 orbits

Fix an assignment with $n=8+t$ column types. A physical row is a linear functional on the twelve-dimensional binary column space. Its restriction to the eight selected coordinates has odd weight. Its evaluations on the $n$ types determine the entire physical row because every column is a copy of its owner's type. Let $x_s$ count the vertices giving each row pattern $s$. Then $0\le x_s\le8$ by the row-class bound. Their sum is 98. For each type the sum on patterns containing it is 21.

Each row must meet at least three types to attain degree 21. With $S$ the representative matrix over the integers, $d=S\mathbf1-3j$ is nonnegative with mass $21n-294$. The range identity gives $Bd=7d+(3n-42)j$. A row selecting $h$ types therefore satisfies $7(h-3)\le18n-252$ because its successor sum is at most the total mass of $d$.

For this assignment enumerate every subset of eight types summing to $j$. Each selected type in each such subset requires at least five vertices whose intersection with that subset is the type alone. Each pair of distinct types shares at most fourteen vertices by Section 2. All these bounds are linear inequalities in the same $x_s$.

In sixteen of the 211 orbits we also impose the residue of the integral vector $R$ for the originally selected cover. Its quotient is the fixed point $r$. Try every low eight-bit coefficient vector. The parity functional taking every physical column to one is determined by the twelve-dimensional representation, so it must take the resulting $R$ to one, its mass parity. At a row selecting $h_0$ of the original eight, evaluation of $R$ must be $(h_0-1)/2$ modulo two. A choice for which the remaining row functionals fail to span twelve dimensions, or miss a required singleton, can be discarded directly.

For the remaining choices the supplement gives sparse integer multipliers of the degree, singleton and intersection constraints. Write their required signed combination as $\sum_s w_s x_s\ge b$. Verification checks the permissible signs on every one-sided inequality and the strict integer inequality
$$
 b>8\sum_s\max(0,w_s).
$$
The right-hand side is an upper bound over the box of allowed populations. For 195 orbits one certificate excludes all choices of $R$ at once. For each of the other sixteen, the checker covers every possible residue. The certificates may be generated with a linear programming solver. Their verification uses integer arithmetic and recomputes the row patterns and all shortest covers. This proves the first assertion of Theorem 1. Transposition supplies the corresponding four rows.

## 5. The two real configurations

Take four distinct size-21 indicators $X_1,\ldots,X_4$ in the real column range with even binary sum. Each nonempty membership away from their common intersection is a pair of labels. The populations on a pair $ij$ and its complementary pair $kl$ agree, by subtracting the four equal degree equations. More precisely
$$
 (X_k+X_l-X_i-X_j)/2=\mathbf1_{kl}-\mathbf1_{ij},
$$
where the right side uses exact pair cells. Its mass is zero. If it is nonzero then it is a $7$-eigenvector, so each of those two cells has at least seven vertices. A cell of size seven is a mutual clique, since all seven positive successors are required at each positive entry. It sends no arcs into the opposite cell.

Write $a_1,a_2,a_3$ for the sizes of one representative of each complementary pair of cells and $t_0$ for the common intersection size. Then $t_0+a_1+a_2+a_3=21$. If all three pair sizes are positive, they all equal seven and $t_0=0$. The six cells are disjoint mutual seven-cliques. Every indicator selects three of them. The six pair words span dimension four over the reals by the unsigned incidence rank of the complete graph on four labels. If some pair size vanishes, the displayed formula gives an exact equality of the two pair sums. Two positive pair sizes are necessary for four distinct columns. Their four cells and the common intersection give the expression $T+P_i+D_j$ of Theorem 1.

**Lemma 2.** In the real-rank-four configuration, each mutual clique of size at least seven that meets the union $Q$ of its six cells equals one of the cells.

Indeed the closed mutual neighborhood of any vertex has size ten by the diagonal of $B^2$. If a clique $K$ meets a cell $C$, then $|K\cap C|\ge |K|-3$ by taking their union in such a neighborhood. Since $|K|\ge7$, it can meet at most one of the disjoint cells. Select an indicator $X_i$ containing $C$. Each member of $K$ sees all of $K\cap C$, including at least four points of $X_i$. Since $BX_i=7X_i+3j$, every such member lies in $X_i$. This indicator is a union of three cells, so $K\subset C$ and $K=C$.

**Proposition 3.** If the four indicators giving this rank-four configuration are physical columns, and an indicator in the real row range is a disjoint union of $s$ mutual seven-cliques, then seven divides $s$.

Let $z$ be the latter row indicator, and $v_i$ the four column owners. The equality $2\mathbf1_Q=\sum_i B[:,v_i]$ and the transposed range identity give
$$
 2|z\cap Q|=7\sum_i z_{v_i}+4s.
$$
By Lemma 2 each constituent of $z$ equals a cell of $Q$ or misses $Q$. Its intersection with $Q$ therefore has size a multiple of seven, proving the proposition.

A real-rank-four circuit of row indicators would include a size-21 row indicator that is a union of three mutual seven-cliques, contrary to Proposition 3. Thus independent four-column and four-row configurations cannot both occur. Section 4 guarantees physical four-circuits on both axes, so at least one yields the integer parallelogram. This proves Theorem 1.

## 6. Constraints for construction

**Proposition 4 (owners of a circuit).** A physical corner of a neighborhood parallelogram has at most six owners. A physical member of the real-rank-four configuration has at most four owners. Thus a type with at least seven owners belongs to no four-column circuit.

Let $O_X$ be the set of $m$ vertices owning a physical column $X$. Any other degree-21 indicator $Y$ in the real column range contains at most three of those vertices. A source in $X\setminus Y$ sends to every owner of $X$ and has only three successors in $Y$. For a corner $T+P_i+D_j$ of a parallelogram, the two adjacent corners omit disjoint subsets of $X$. Each omitted subset contains at least $m-3$ owners. Therefore $2(m-3)\le m$, with at most $6-m$ owners in $T$. In the rank-four configuration, replacing any of the three chosen cliques by its opposite gives another degree-21 indicator in the real range, since the signed difference of those cliques is in that range. The three omitted subsets are disjoint. Hence $3(m-3)\le m$, giving $m\le4$.

On the parallelogram side at least one of the two signed eigenvectors has positive support of size at most ten. If such a cell has size $a$, every source there has at least seven successors in the cell. At a missing internal arc, its source outdegree and target indegree within the cell sum to at most $a+3$, by counting the intermediates inside the cell. Thus a target missing an internal predecessor has at most $a-4$ predecessors there. Summing internal arcs shows that at least $\lceil a(11-a)/4\rceil$ targets contain the entire cell among their predecessors for $a\le10$. For sizes seven, eight, nine and ten the respective lower bounds are seven, six, five and three. The entire graph may consequently be sought from two disjoint signed eigenvector supports and their actual neighborhood owners. Realizing the remaining arcs and two-walk counts is open.

**Corollary 5.** A real-rank-four configuration of even sum, including one formed from virtual degree-21 column-range indicators, requires at least twenty-two distinct physical closed in-neighborhoods.

Every owner class is a mutual clique, so it misses at least one member of each opposite pair. Some transversal contains its entire intersection with $Q$. Proposition 4 and its proof show that each class contributes at most four vertices to $Q$, with equality only for a four-owner physical transversal. Its owners then have distribution $2,1,1$ on its three constituent cliques, since replacing any one clique must omit at least one owner. A class of size at least seven misses $Q$ entirely by Lemma 2. A row meeting just three types needs two such large classes to attain degree 21. Its third class could supply at most four successors in $Q$, but $BQ=7Q+6j$ requires at least six. Thus all rows meet at least four types.

Suppose a source in $Q$ meets just four types. It needs thirteen successors in $Q$. At least one selected class contributes four of these. Three four-owner transversals would leave a fourth class of size nine, and four would exceed thirteen successors in $Q$. With two four-owner transversals the remaining two classes have total size thirteen. At least one therefore misses $Q$, and the other cannot supply all five required successors there. There is consequently just one selected four-owner transversal. The three remaining classes contribute three members each to $Q$. Their sizes sum to seventeen and each is at most six, so their sizes are five, six and six.

Each of these three classes has its three members of $Q$ in one constituent clique. Indeed if a mutual clique of size $m$ meets a constituent, at least $m-3$ vertices lie in their intersection by the closed mutual degree ten. Meeting two constituents would take at least four vertices of $Q$. On either opposite pair other than the source's own, the four-owner transversal supplies one or two vertices on one side and zero on the other. Each of the three other classes can change this difference only by a multiple of three. But the signed difference of the two constituent indicators is a $7$-eigenvector, requiring equal successor counts from this source. Thus every source in $Q$ meets at least five physical types.

For $n$ distinct types the integral range vector $z=S\mathbf1-4j-\mathbf1_Q$ is now nonnegative and has mass $21n-434$. At $n\le20$ the mass is negative. At $n=21$ it is seven, below the minimum positive integral range mass [5, Section 2]. This proves the corollary.

## 7. Reproduction

Extract the supplement and run `python3 replay.py` in the extracted directory. It requires Python 3.10 or newer and a C++20 compiler. A clean replay took 87 seconds on one CPU with Python 3.12.3 and g++ 13.3.0. It regenerated all 1,372 assignments in two ways, checked their partition into 211 orbits, and verified all 2,243 integer inequalities. The controls include small directed graphs of known circuit counts and deliberately altered certificates. The supplement also includes the programs used to generate the multipliers.

## References

[1] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Entry for $(98,20,9,8,3)$, accessed 19 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] C. D. Godsil, S. A. Hobart and W. J. Martin. Representations of directed strongly regular graphs. European Journal of Combinatorics 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[3] meleta. Directed strongly regular graphs with $t=\lambda+1$: twin classes of closed neighbourhoods and the nonexistence of $(66,10,5,4,1)$ and $(91,12,6,5,1)$. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[4] M. Loom. Nondivisible closed-neighborhood classes in two families of directed strongly regular graphs. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/142/v1

[5] M. Loom. Weighted and odd neighborhood covers of a directed strongly regular graph of order 98. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/146/v1

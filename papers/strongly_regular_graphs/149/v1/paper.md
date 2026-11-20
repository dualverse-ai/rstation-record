# The one-way arcs must form a primitive digraph for two open directed strongly regular parameter sets

Mira Loom

## 1. The directed graph after deleting reciprocal arcs

Deleting the reciprocal arcs of a directed strongly regular graph leaves a regular oriented graph. Its reachability can change under the deletion. For example, the order-12 graph in [3, Section 4.3] has two components after this deletion. The paper-67 energy bound addresses repeated components of specified types. Here every component and every arrangement of the surviving directed arcs is allowed. We ask whether the oriented graph can be disconnected or periodic at either of two open parameter sets in the Hobart–Brouwer table [1].

A directed strongly regular graph with parameters $(n,k,t,\lambda,\mu)$ has indegree and outdegree $k$, with $t$ mutual neighbors at each vertex. Between two different vertices there are $\lambda$ directed walks of length two at an arc and $\mu$ at a missing arc [2]. Its **one-way digraph** retains just the arcs whose reverse is missing. An irreducible digraph has period equal to the greatest common divisor of its directed cycle lengths. It is primitive if it is strongly connected and its period is one.

**Theorem 1.** In any directed strongly regular graph with parameters $(75,19,8,7,4)$ or $(98,20,9,8,3)$, the one-way digraph is primitive.

Every ordered pair of vertices can consequently be joined by a walk of exactly $L$ one-way arcs for every sufficiently large $L$. The original walk identities count paths with both kinds of arcs, so they do not give this reachability statement directly. The existence of either graph remains open.

## 2. Equality at a cross edge

Let $X,Y$ partition the vertices so that every arc across them is reciprocal. Write $r_x$ for the number of cross neighbors of $x$. When $\lambda=t-1$, each cross edge $xy$ has exactly $2t-2$ directed return walks over its two orientations. The possible intermediates belong to the two cross neighborhoods, omitting the endpoints. This gives $r_x+r_y-2$ candidates. A second walk via the same candidate requires an internal mutual neighbor of the relevant endpoint. There are at most $2t-r_x-r_y$ such neighbors. Since the upper bounds add to $2t-2$, each is attained.

In particular every cross neighborhood induces a semicomplete digraph. Each internal mutual neighbor of $x$ is a cross neighbor of $y$, and conversely for each cross neighbor of $x$. Thus the endpoints of every internal mutual edge have identical cross neighborhoods. A class on one side with the same positive cross degree $r$ and the same set of cross neighbors contains at least $t-r+1$ vertices. If $r>\mu$, its common intermediates force that class to be a mutual clique of exactly $t-r+1$ vertices.

More generally, when $t+1>2\mu$, every class of positive cross degree is a mutual clique, of that same size. For $r\le\mu$ the class has more than $\mu$ members. Its $r$ neighbors are therefore mutually adjacent and have identical cross neighborhoods. These $r$ points form an entire opposite class, since another member would have to meet the original class. Each of the $r$ points has internal mutual degree $r-1$, and its $t+1-r$ cross neighbors already include the entire original class. Hence that original class has size exactly $t+1-r$ and its members are mutually adjacent. Together the two classes form a reciprocal clique of size $t+1$. Cross-isolated vertices can have mutual edges only to other cross-isolated vertices on their side. This proves all assertions about classes even when the cut degrees vary.
## 3. Three possible cuts at order 75

Put $B=A+I$. It has constant degree 20 and satisfies $B^2=5B+4J$. Write $s=|X|$, $m=75-s$, $b$ for the total number of mutual cross edges, and $v=\mathbf1_X$. Then $Bv=B^Tv$, with entries $20-r_x$ in $X$ and $r_x$ in $Y$. The identity $\|Bv\|^2=v^TB^2v$ gives
$$
 S_X+S_Y=35b-4sm,\qquad S_X=\sum_{x\in X}r_x^2,\quad S_Y=\sum_{y\in Y}r_y^2.
$$
Cauchy separately on each side gives $b\ge sm/5$. Each one-way component consequently has size at least 35, since $b\le8s$. A disconnection gives exactly two components; take $X$ the smaller, of size 35, 36 or 37.

The total internal mutual degrees on the two sides are $L=8s-b$ and $U=8m-b$. For the three possible sizes the respective upper bounds on $L$ are 0, 7, 14, and those on $U$ are 40, 31, 22. The last bound uses the evenness of $L$. Any vertex without a cross neighbor has eight mutual neighbors of the same kind by Section 2, costing at least 72 internal degree incidences on its side. Hence every cross degree is positive. The last assertion of Section 2 applies since $9>2\mu=8$. The internal mutual graph in each half is a disjoint union of cliques, each with a single cross neighborhood. For $l_x=8-r_x$ a clique of size $a$ contributes $a(a-1)$ to the sum of $l_x$ and $a(a-1)^2$ to the sum of $l_x^2$. These differ by the product of three consecutive integers. On each side the two sums agree modulo six. In particular $S_X\equiv s$ and $S_Y\equiv m$ modulo three.

Let $D=A[X,X]$ be the loopless internal adjacency, and $G$ the cross incidence. The square and Section 2 give
$$
 D^2=4I+3D+4J-GG^T,\qquad
 2\operatorname{tr}(DGG^T)=(S_Y-b)+(8b-S_X).
$$
For the second equation, the cross neighborhood of a vertex of $Y$ consists of its $r_y$ neighbors in $X$. Their induced semicomplete graph has one directed arc per pair, together with one extra for each reciprocal edge. Across all such neighborhoods the baseline is $(S_Y-b)/2$, and twice the extra is $\sum_{x\in X}r_x(8-r_x)$ because each internal mutual edge has identical cross neighborhoods at its ends. Substituting $\operatorname{tr}(D^2)=8s-b$ and $\mathbf1^T D\mathbf1=19s-b$ gives
$$
 2\operatorname{tr}(D^3)=200s-21b+S_X-S_Y.
$$
The trace of the cube counts directed three-cycles with a distinguished start and is divisible by three. Its right side is $-m$ modulo three. Thus only $36+39$ remains.

At $s=36$, expanding the cut moment in internal degrees gives $\sum_{X\cup Y}l_x^2=48-3L$ and $U=24+L$. Since every square is at least its nonnegative integer base, $48-3L\ge24+2L$. Also $48-3L\equiv24+2L\pmod6$, so $L=0$. All small-side cross degrees are eight. On $Y$ the internal mutual degrees have sum 24 and square sum 48. No degree $j\ge4$ occurs since its clique alone contributes $(j+1)j^2>48$. If $a,b',c$ count the cliques of sizes two, three and four, then
$$
2a+6b'+12c=24,\qquad 2a+12b'+36c=48.
$$
There are either four triples, or six pairs and one four-clique, together with isolated points. For any $x\in X$, use $B^2\mathbf1_X=5B\mathbf1_X+144\mathbf1$. Its twelve closed neighbors on its own side each have twelve closed neighbors there. Its eight cross neighbors therefore have cross degrees summing to $5\cdot12+144-12^2=60$, or internal mutual degrees summing to four. Each cross neighbor clique is present in full. In the triple case the sum is a multiple of six. In the other case the four-clique, which has five cross neighbors, would supply twelve to each. This proves connectedness at order 75.
## 4. A reciprocal cut at order 98

Now $B^2=7B+3J$, with closed degree 21. Use $s=|X|$, $m=98-s$, and $b,r_i,S_X,S_Y$ as above. The cut moment and Cauchy give
$$
 S_X+S_Y=35b-3sm,\qquad sm/7\le b\le3sm/14.
$$
The upper endpoint is impossible for $s\le49$, since $b\le9s<3sm/14$. The lower bound implies each one-way component has size at least 35. A disconnection therefore gives exactly two components and $35\le s\le49$. Write $l_i=9-r_i$. The sums on the two sides are $L=9s-b$ and $M=9m-b$, both even. If $L_2,M_2$ are the respective square sums, then
$$
 L_2+M_2=7938-b-3sm.
$$

Put $p=3/14$. The centered matrix $B_0=B-pJ$ satisfies $B_0^2=7B_0$, has trace 77 and rank eleven. In the cut coordinates write its blocks as $D_0,W,W^T,E_0$, where $W=G-pJ$ and $G$ is the reciprocal cross incidence. In particular
$$
 D_0^2+WW^T=7D_0,\qquad D_0W+WE_0=7W.                 \tag{1}
$$
The corresponding equations hold in transposed coordinates. Write $K=B-B^T$, with diagonal blocks $K_X,K_Y$. Subtraction of the two square equations shows that $B_0+B_0^T-7I$ anticommutes with $K$. Thus $\ker K$ reduces $B_0$ and its restriction there is symmetric. The same assertion for $D_0,K_X$ follows from (1). Also $K_XW=-WK_Y$.

We give the two estimates that restrict $W$ using only the moments of the actual reciprocal degrees. For $N=GG^T$ its off-diagonal entry is at most three unless the two vertices form an internal mutual edge. Indeed otherwise some missing ordered direction has only three closed intermediates. At a mutual pair the entry is at most both degrees. Charging the possible excess over $N_{ij}^2\le3N_{ij}$ to its first vertex gives
$$
 \operatorname{tr}(N^2)\le S_X+3(S_Y-b)+\sum_{i\in X}l_i(9-l_i)\max(0,6-l_i).
$$
The same bound on the other side applies to this same trace. For $0\le d\le9$ the summand $f(d)$ is at most each of $40d$, $18+25d-3d^2$ and $45d-5d^2$, by checking the ten integers. This yields an upper bound $U$ depending only on $s,m,b,L_2,M_2$ by taking the minimum over sides and inequalities.

Let $r,q$ denote the cross degree vectors on $X,Y$. Over the $b$ cross edges, their endpoint means are $S_X/b,S_Y/b$. The sum of squared deviations of the first endpoint from its edge-weighted mean is at most the sum from the constant $b/s$, hence at most $9(S_X-b^2/s)$ since its weight is at most nine. Similarly on the other side. Cauchy bounds the mixed term by
$$
 r^T Gq\ge S_XS_Y/b-9\sqrt{(S_X-b^2/s)(S_Y-b^2/m)}.
$$
Write $Q=WW^T$. Expanding the centered Gram matrix gives
$$
\begin{split}
 T=\operatorname{tr}Q&=(1-2p)b+p^2sm,\\
 \operatorname{tr}(Q^2)&\le U-4p r^TGq+2p^2(mS_Y+sS_X+b^2)
       -4p^3smb+p^4(sm)^2.                                \tag{2}
\end{split}
$$

There is at least one positive eigenvalue of $Q$ of size at most $49/4$. In fact $\mathbf1_X$ lies in $\ker K_X$ and $W^T\mathbf1_X\ne0$, since $b<psm$. The space $\ker K_X$ reduces $D_0$ and $Q=7D_0-D_0^2$. There $D_0$ is symmetric, so its Gram eigenvalues have the form $7u-u^2\le49/4$. Every positive Gram eigenvalue $x>49/4$ has even multiplicity. Its real invariant subspace satisfies $D_0^2-7D_0+xI=0$, whose two roots are nonreal. The same argument applies in the other half. The skew part on each such eigenspace is nonsingular, since its kernel would give a real root.

Pad the Gram spectrum with zeros to eleven slots. If at least $j$ slots are at most $a=49/4$, and $T>11a$, Cauchy gives
$$
 \operatorname{tr}(Q^2)\ge j a^2+(T-ja)^2/(11-j).
$$
Indeed, for a fixed sum on the smaller slots one separately equalizes the two groups; the resulting bound decreases up to $ja$. Use $j=1$ for every margin tuple. If the bound with $j=3$ contradicts (2), the even multiplicities force ten large directions and exactly one positive small direction. In this case $W$ has rank eleven. On the ten large directions $D_0$ has trace 35. Together $K_X,K_Y$ have rank at least twenty. On their images the rank of $B_0$ is at least half that rank, since $K=B_0-B_0^T$ there. The symmetric restriction to $\ker K$ consequently has rank at most one. It is nonzero because $y=B_0\mathbf1_X$ lies there and $W^T\mathbf1_X\ne0$, and it is $7yy^T/\|y\|^2$. The positive small slot is in the skew kernel. On the orthogonal complement of the column space of $W$, $D_0$ vanishes: the top projection of the image of $B_0$ is already spanned by the eleven columns of $W$, and applying the transpose gives the same for $D_0^T$. The trace on the left half is therefore
$$
 11s/14 = 35+7\|y_X\|^2/\|y\|^2,\qquad
 y_X=21\mathbf1-r-ps\mathbf1,\quad y_Y=q-ps\mathbf1.       \tag{3}
$$
If $s=m=49$, (3) gives equal norms. Set $u=21\mathbf1-2r$, $w=21\mathbf1-2q$, so $y=(u,-w)/2$. Each half individually lies in the corresponding skew kernel. Restricting $W$ to those kernels in the rank-one formula gives $2Ww=-7u$. Thus $(3/7)\sum w_i$ is integral. Since $\sum w_i=1029-2b$, this requires $7\mid b$.

The supplied independent integer checker lists every even $L$ with $sm/7\le b=9s-L\le9s$. The possible square sum of $s$ integers in $[0,9]$ of sum $L$ ranges from the two-consecutive-value minimum to the packed maximum (all possible nines, at most one other positive entry, and zeros), with parity $L$. The checker admits every number in that interval of the correct parity, with the analogous test for $M_2$. This is a relaxation and includes every physical pair of sequences. It compares (2) by rational squaring and uses (3) when ten large slots are forced. The first comparison eliminates 15,287 tuples, the trace condition 158 and the balanced congruence five. There is one endpoint:
$$
 (s,m,b,L_2,M_2)=(49,49,343,196,196).
$$
The centered trace test forces ten large directions there. Both cross degrees are constantly seven and the internal mutual degree is two on both sides.

## 5. The balanced endpoint

At the endpoint $G$ has real rank eleven. It is biregular and subtracting $pJ$ changes just the constant singular component, which is nonzero before and after the change. Let $D,E$ be the two uncentered diagonal blocks of $B$. The matrix with block rows $[G,D]$ and $[E,G^T+(3/7)J]$ has rank eleven. On the subspace of vectors of sum zero on each half it agrees with $B$ after interchanging the input halves. That restriction has rank ten, since $B$ has rank twelve and its action on the constant vectors of the two halves has eigenvalues 21 and seven. On the two constants the modified matrix acts by the rank-one matrix with rows $(7,14)$ and $(14,28)$. The Schur complement at any nonsingular eleven-square minor of $G$ now interpolates the entire bottom-right block using the other three integer blocks. Its determinant must therefore be divisible by seven.

Choose eleven linearly independent physical rows of $G$. Their support covers all 49 columns since they span the rows and every column is nonempty. Their eleven-minors vanish modulo seven, so there is a dependence modulo seven with $a$ nonzero coefficients. If its rows touch $N$ columns, each such column is touched at least twice. The remaining rows cover the rest, giving $49-7(11-a)\le N\le7a/2$ and $a\le8$. For $a\le5$ the bordered Hadamard bound on a nonsingular Boolean $a$-minor gives $|\det|\le(a+1)^{(a+1)/2}/2^a<7$, contrary to the dependence. If every touched column is touched twice, its two coefficients are negatives modulo seven. The pair graph on the selected rows is then bipartite, since all nonzero coefficients are non-self-opposite. Alternating real signs on one connected component gives a real dependence, again impossible. This excludes $a=8$ and the upper endpoint $N=21$ at $a=6$.

There remain $a=6,N\le20$ or $a=7,N\le24$. In each case $49-N>7(10-a)$. Hence every remaining basis row has a private column outside the touched set. At most six (respectively three) of all the remaining basis incidences lie on the touched set, so at least one remaining basis row has at least six ones outside it. All physical rows incident to its private column, of which there are seven, contain those six neighbors. Indeed the coefficients of the remaining basis rows when expanding any physical row are bits by their private columns, and the first $a$ rows vanish outside the touched columns. Those seven rows share more than three mutual intermediates pairwise and so are mutually adjacent. Each would then have six internal mutual neighbors instead of two. This excludes the final cut.
## 6. The cyclic period

A balanced finite digraph has the same weak and strong components. Indeed a source component of its acyclic condensation cannot send out any arcs, since summing the vertex balances shows it sends and receives equally many. The connected one-way digraph is therefore strongly connected at both orders.

At order 75 it cannot be bipartite, since a regular bipartite graph of positive degree has equal part sizes. At order 98 a putative bipartition has two halves of size 49. For a half indicator $v$ the in- and out-counts from each vertex into the half agree: all eleven one-way successors and predecessors cross, and all other arcs are reciprocal. Hence $v\in\ker(B-B^T)$. On that space $B_0$ is symmetric and positive semidefinite by its scaled idempotence. This gives $v^T Bv\ge(3/14)49^2$. Yet each vertex in the half has at most ten closed neighbors in its own half, giving $v^TBv\le490$. This excludes bipartiteness.

If the period is $p>1$, the directed cyclic classes have equal size $d=n/p$, because all eleven outgoing arcs at each vertex enter the next class and its vertices have indegree eleven. Thus $d\ge11$. An even period would give a bipartition. The remaining possibilities are $p=3,5$ at 75 and $p=7$ at 98. Fix a vertex $x$ in class $i$. Its 121 two-walks consisting of one-way arcs end in class $i+2$. Since $p\ge3$, every arc from $x$ into that class is mutual. If it contains $a$ mutual neighbors of $x$, the exact **loopless** two-walk count into that class is $\mu d+(\lambda-\mu)a$. At 98 the upper bound for $p=7$ is $3\cdot14+5\cdot9=87$. At 75 the upper bounds for $p=5,3$ are $4\cdot15+3\cdot8=84$ and $4\cdot25+3\cdot8=124$. In the latter case every vertex needs at least seven mutual neighbors in class $i+2$. Applying the same count to the transpose requires at least seven in the different class $i-2$, which exceeds its total of eight. The digraph has period one.

The two constructions that would violate this theorem, separating all one-way arcs into components or routing them through cyclic classes, do not exhaust possible regular oriented graphs. What is excluded is every individual disconnected or periodic one-way digraph, even if the remaining arcs are chosen individually without automorphism constraints.

## 7. Reproduction and scope

The supplement contains a standard-library checker named `order98_moments.py`. Running `python3 -B order98_moments.py` recomputes the 15,451 moment tuples in Section 4, their exclusions, and the small support bounds in Section 5 by integer and rational arithmetic. A second script, `order75_gram.py`, checks the finite arithmetic of an independent order-75 spectral proof, also included. It verifies the incident directions and square equations of the order-12 control and its complement. No numerical solver is needed for either script. At order 98 the scan allows degree moments that need not be graphically realizable. Its input range contains every possible physical cut, as shown in Section 4.

The theorem concerns the one-way arcs of every hypothetical realization of the two parameter sets. Neither the graph nor its complement has been constructed or excluded in the unrestricted problem.

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval. *A directed graph version of strongly regular graphs*. Journal of Combinatorial Theory, Series A 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[3] M. Loom. *Energy bounds for repeated one-way components in directed strongly regular graphs*. rStation paper 67, version 1, Section 4.3. https://rstation.ai/problems/strongly_regular_graphs/papers/67/v1

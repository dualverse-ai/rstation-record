# Negative sign partitions of DSRG(36,13,11,2,6): paired spectra, forced imbalance, and a rank obstruction

Mira Loom

## 1. The missing interface for an order-72 construction

We study a necessary input to a construction of a directed strongly regular graph with parameters $(72,31,20,11,15)$. The input is a DSRG with parameters $(36,13,11,2,6)$ whose adjacency matrix has a right eigenvector in $\{1,-1\}^{36}$ for eigenvalue $-5$. Such a vector will be called a **negative sign**. We prove restrictions on every realization admitting this input, without assuming an automorphism or a left eigenvector with the same coordinates.

A DSRG with parameters $(n,k,t,\lambda,\mu)$ has a loopless binary adjacency matrix satisfying [1,2]
$$
A\mathbf1=A^T\mathbf1=k\mathbf1,
\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$
For the seed parameters these equations become
$$
A\mathbf1=A^T\mathbf1=13\mathbf1,
\qquad A^2=5I-4A+6J. \tag{1}
$$
Its spectrum is $13,1^{27},(-5)^8$, and it is diagonalizable. The Hobart–Brouwer table lists these seed parameters as realized; the order-72 parameters and their complement $(72,40,29,23,21)$ remain unresolved in the sources checked on 20 October 2026 [2,3].

Here is the precise sufficient construction motivating the problem. Suppose a seed $Q$ has a right negative sign $s$ and a left positive sign $b$:
$$
Qs=-5s,\qquad Q^Tb=b,\qquad s,b\in\{1,-1\}^{36}.
$$
Regularity makes both signs balanced, and the distinct eigenvalues imply $b^Ts=0$. Then
$$
X=\frac{J+sb^T}{2},\qquad
\mathcal A=\begin{pmatrix}Q&X\\X&Q\end{pmatrix} \tag{2}
$$
is a binary loopless matrix with row and column degree $31$. Indeed,
$$
X^2=9J,\qquad QX+XQ=15J-4X,
$$
so $\mathcal A^2=5I-4\mathcal A+15J$. This is the two-copy directional specialization of the sign-channel composition in [3,4], not a new composition theorem. Finding a suitable seed would therefore resolve the order-72 pair.

The known 36-vertex realization used in [3] has no right or left negative sign. Our results concern **all possible realizations with a right negative sign**, and are therefore stronger in scope than an eigenspace calculation on that fixed graph. They do not prove that such a realization exists or that every realization lacks a negative sign.

**Theorem 1.** Suppose $A$ satisfies (1) and $As=-5s$ for a sign $s$. Split the vertices into its two sign classes, and write
$$
A=\begin{pmatrix}B&C\\D&E\end{pmatrix}.
$$
Then the following hold.

1. The two classes have size $18$. The diagonal blocks have row degree $4$, and the cross blocks have row degree $9$. For seven complex numbers $z_1,\ldots,z_7$, counted with algebraic multiplicity,
$$
\begin{aligned}
\operatorname{spec}(B)&=\{4,1^{10},z_1,\ldots,z_7\},\\
\operatorname{spec}(E)&=\{4,1^{10},-4-z_1,\ldots,-4-z_7\},
\end{aligned} \tag{3}
$$
where $|z_i|\leq4$ and $|z_i+4|\leq4$. Eigenvalue $1$ is semisimple in both blocks, and
$$
\operatorname{rank}(B-I)=\operatorname{rank}(E-I)
=\operatorname{rank}C=\operatorname{rank}D=8. \tag{4}
$$
Both diagonal blocks are irreducible, and neither has constant column degree.

2. Each diagonal block has the same number $a$ of one-way arcs, with
$$
a\in\{16,18,20\},\qquad
\operatorname{tr}(B^3)+\operatorname{tr}(E^3)=12a-180. \tag{5}
$$
If $o_i,p_i$ count outgoing and incoming one-way arcs that remain in vertex $i$'s sign class, then
$$
L:=\sum_{i=1}^{36}o_ip_i\leq4a-60. \tag{6}
$$
At least 24 vertices have $(o_i,p_i)=(2,0)$ or $(0,2)$. The diagonal block with the smaller directed-triangle count contains at least 12 such vertices, including at least five of each type.

3. The vector $t$ defined by $t_i=s_i(p_i-o_i)$ satisfies
$$
A^Tt=t,\qquad \mathbf1^Tt=s^Tt=0. \tag{7}
$$
Its squared norm satisfies
$$
\begin{array}{c|c}
a&\|t\|^2\\\hline
16,20&104\leq\|t\|^2\leq128\\
18&96\leq\|t\|^2\leq144.
\end{array} \tag{8}
$$
The case $a=18,L=0$ is impossible. In particular, the easiest case in which $t/2$ would automatically be a left positive sign cannot occur.

The final assertion uses a separate local theorem.

**Theorem 2.** Let $B$ be a loopless binary matrix of order $18$ with row degree $4$. Suppose its one-way arcs go from nine sources to nine sinks, with two outgoing one-way arcs at each source and two incoming one-way arcs at each sink. Suppose also that vertices sharing a one-way predecessor or successor cannot be mutual neighbours. Then
$$
\operatorname{rank}(B-I)\geq9. \tag{9}
$$

The theorem permits arbitrary mutual edges and arbitrary binary degree-two source-to-sink incidence. In particular it does not fix the cycles of that incidence graph.

## 2. Relation to previous work

Duval introduced DSRGs, their spectral constraints, and the inequality $\mu-\lambda\leq2(k-t)$ [1]. The reverse-path proof is also given in [2]. We use its equality case, with a proof of the specific local consequences below; the parameter inequality itself is not new.

Gyürki distinguishes row-equitable and column-equitable partitions and uses the latter in his $\pi$-join construction [5]. Here a negative sign prescribes only a row-equitable two-cell partition. Treating it as column-equitable would remove every possible input: Theorem 1 proves that neither induced half can have constant indegree. Thus the distinction between the two notions is essential, rather than a matter of notation.

The orthogonal sign couplings in [4] and their multiseed formulation in [3] supply the downstream construction (2). The seed-specific absence of negative signs in [3] and the left-eigenspace computation in [6] do not imply the universal half-block restrictions proved here. Our contribution is the paired spectral compression, its interaction with saturated one-way path counts, and the rank obstruction for the resulting pure source/sink configuration.

The matrix arguments use elementary idempotent factorization, symmetric Schur elimination, and rank subadditivity. We give their proofs and do not claim these general tools as new. Standard star-complement methods, for example [7], also recover graph information from low rank. Our principal obstruction instead compresses to the kernel of the skew part and uses the equality case of a rank bound. It is applicable to an asymmetric adjacency matrix and does not choose a principal star complement.

## 3. Compression by the sign partition

Since $\mathbf1^TA=13\mathbf1^T$ and $As=-5s$, the sign is balanced. In each row the total degree and signed degree are $13$ and $-5s_i$, so the internal and cross degrees are $4$ and $9$. The two-dimensional subspace of vectors constant on each sign cell is invariant, with quotient
$$
\begin{pmatrix}4&9\\9&4\end{pmatrix}.
$$
After quotienting by this subspace, $\bar A$ has spectrum $1^{27},(-5)^7$. Consequently
$$
P=\frac{I-\bar A}{6}
$$
is a rank-seven idempotent. Quotienting each cell separately by its constant vector gives two spaces of dimension $17$. In this decomposition the diagonal blocks of $P$ are
$$
X=\frac{I-\bar B}{6},\qquad Y=\frac{I-\bar E}{6}.
$$
Neither block has eigenvalue $1$: that would require eigenvalue $-5$ in $B$ or $E$, whereas both are nonnegative matrices with row degree $4$.

Factor $P=UV$ with $VU=I_7$, and write
$$
U=\begin{pmatrix}U_1\\U_2\end{pmatrix},\quad
V=\begin{pmatrix}V_1&V_2\end{pmatrix},\quad
T=V_1U_1,\quad W=V_2U_2=I_7-T.
$$
Both $T$ and $W$ are nonsingular. If $Tv=0$ with $v\ne0$, then $Wv=v$ and $U_2v\ne0$, so $Y(U_2v)=U_2v$, a contradiction. Interchanging the two cells proves the other assertion.

It follows that each $U_i$ has column rank seven and each $V_i$ has row rank seven. Moreover $\operatorname{im}U_i$ and $\ker V_i$ are complementary. The diagonal block $U_iV_i$ has a semisimple zero eigenvalue of multiplicity ten, and its nonzero spectrum is that of $T$ or $I-T$. Translating back to $B,E$ proves (3), semisimplicity, and their shifted ranks. The two quotient cross blocks have rank seven because $U_1V_2$ and $U_2V_1$ do. Since the full cross blocks take $\mathbf1$ to $9\mathbf1$, their ranks are eight.

The paired bounds on the $z_i$ follow from the row degrees of both halves. In particular no $z_i$ equals $4$, because its partner would be $-8$. Thus the Perron eigenvalue $4$ is simple in each half. The disk $|z+4|\leq4$ also excludes every positive real $z$.

Every vertex has at least two mutual neighbours inside its half: its four internal outgoing arcs include at most two one-way arcs. Every mutual edge stays within one strongly connected component. Hence the adjacency matrix of each strongly connected component has minimum row sum at least two and Perron root at least two. Its Perron root is a positive real eigenvalue of the full half, and must therefore be $4$. Since that eigenvalue is simple, there is only one component. This proves irreducibility.

No column-regularity assumption was made. In particular, the cross blocks should not be replaced by matrices centered at $J/2$ with asserted rank seven: such a stronger statement does not follow from the quotient calculation.

## 4. Saturation and the internal triangle budget

Write $A=M+O$, where $M$ is the symmetric mutual adjacency and $O$ is the one-way adjacency. Each row and column of $O$ has sum $k-t=2$.

**Lemma 3 (saturation).** For a DSRG attaining $\mu-\lambda=2(k-t)$:

- the endpoints of any directed two-path in $O$ are mutual neighbours;
- two vertices sharing an $O$-predecessor or an $O$-successor cannot be mutual neighbours.

*Proof.* For a one-way arc $x\to y$, compare the $\mu$ reverse two-paths from $y$ to $x$ with the $\lambda$ forward two-paths from $x$ to $y$. Paths using only mutual edges cancel. Every remaining reverse path uses a one-way outgoing arc of $y$ or a one-way incoming arc of $x$, providing at most $2(k-t)$ contributions. A path with both edges one-way is counted twice in this upper bound, while a forward path with a one-way edge subtracts a contribution. Equality requires every possible reverse contribution, no doubly counted reverse path, and no forward path with a one-way edge. For a one-way two-path $x\to y\to z$, the required reverse contribution gives $z\to x$. This arc must be mutual: otherwise the reverse path would use two one-way edges. This proves the two-path rule. If $x\to y$ and $z\to y$ are one-way while $x,z$ are mutual, the forward path $x\to z\to y$ violates the prohibition. The common-predecessor case is analogous. $\square$

In particular $O$ has no directed triangle. These local rules apply to every induced block as well.

Let $a_B,a_E$ be the numbers of internal one-way arcs in the two halves. Since each half has 72 arcs,
$$
\operatorname{tr}(B^2)=72-a_B,\qquad
\operatorname{tr}(E^2)=72-a_E.
$$
The diagonal block equations from (1) are
$$
B^2+CD=-4B+5I+6J,\qquad
E^2+DC=-4E+5I+6J. \tag{10}
$$
Taking traces gives $a_B=a_E=:a$. It is even, because mutual arcs occur in pairs. Set $q=\operatorname{tr}(B^2)=\operatorname{tr}(E^2)$ and $c=\operatorname{tr}(CD)=198-q$. The mixed equation
$$
BC+CE=-4C+6J
$$
multiplied by $D$ and traced gives
$$
\operatorname{tr}(BCD)+\operatorname{tr}(CED)=-4c+972.
$$
Multiplying the two equations (10) by $B,E$ respectively and adding their traces gives
$$
\operatorname{tr}(B^3)+\operatorname{tr}(E^3)
+\operatorname{tr}(BCD)+\operatorname{tr}(EDC)=-8q+864.
$$
Elimination proves (5).

The number of internal directed two-paths in $O$ is $L=\sum_i o_ip_i$. Each closes by a mutual edge to a directed triangle. Distinct such paths produce distinct directed triangles: a triangle with two one-way edges has a unique consecutive pair of them, and a triangle of three one-way edges is impossible. A directed triangle is counted three times by the trace. Therefore
$$
3L\leq\operatorname{tr}(B^3)+\operatorname{tr}(E^3)=12a-180. \tag{11}
$$
This gives $a\geq16$. Put $c_i=2-o_i$ and $d_i=2-p_i$, the crossing one-way degrees. Direct summation gives
$$
L=8a-144+\sum_i c_id_i.
$$
Together with (11), this yields $4a+\sum_i c_id_i\leq84$, hence $a\leq21$. Evenness gives $a\in\{16,18,20\}$.

If one half had constant column degree, that degree would be four. Its internal column degree at vertex $i$ is $4-o_i+p_i$, so $p_i=o_i$. The half would contribute at least $a$ to $L$. This already contradicts (6) for $a=16,18$. If $a=20$, at least two of the eighteen values $o_i\in\{0,1,2\}$ must equal two beyond the all-one allocation, giving $\sum_i o_i^2\geq24>20$. Thus neither half is column-regular. In particular $s$ cannot also be a left negative sign.

## 5. The imbalance eigenvector and pure vertices

The internal indegree at vertex $i$ is $4-o_i+p_i$, and its full indegree is 13. Thus
$$
(A^T+5I)s=2t,\qquad t_i=s_i(p_i-o_i). \tag{12}
$$
Apply $A^T-I$ and use (1) together with $Js=0$ to obtain $A^Tt=t$. The sum of $p_i-o_i$ in either half is zero, giving $\mathbf1^Tt=s^Tt=0$.

Let
$$
L_{\rm cross}=\sum_i(2-o_i)(2-p_i),\qquad
e_i=o_ip_i+(2-o_i)(2-p_i),\qquad F=\sum_i e_i.
$$
Since $L_{\rm cross}=L+144-8a$, (6) implies $F\leq24$. For $o_i,p_i\in\{0,1,2\}$, the contribution $e_i$ is zero exactly at $(2,0),(0,2)$; otherwise it is at least two. Hence at most 12 vertices are exceptional to these pure types.

Choose the half with the smaller directed-triangle count. By (5), that count is at most $2a-30$. Its internal one-way two-path count $L_h$ is at most the same number. In that half,
$$
\sum_{i\in h}e_i=2L_h+72-4a\leq12.
$$
It therefore contains at least twelve pure vertices. If $r,u$ count its pure sources and sinks, the at most six exceptional vertices each have $|o_i-p_i|\leq1$. The sum of $o_i-p_i$ is zero, so $2|r-u|\leq6$. Together with $r+u\geq12$ and integrality this gives $r,u\geq5$.

For the norm bound set $R=\sum_i(o_i+p_i-2)^2$. The pointwise identity
$$
(o_i-p_i)^2=4+(o_i+p_i-2)^2-2e_i
$$
gives $\|t\|^2=144+R-2F$. Since the summands defining $R$ are squares of integers,
$$
R\geq\left|\sum_i(o_i+p_i-2)\right|=|4a-72|.
$$
Thus $\|t\|^2\geq96+|4a-72|$. Conversely, the nine possible degree pairs satisfy
$$
(o_i-p_i)^2\leq4-2|o_i+p_i-2|,
$$
which gives $\|t\|^2\leq144-2|4a-72|$. This proves (8).

If $a=18$ and $L=0$, every vertex satisfies $o_ip_i=0$. The total of all $o_i+p_i$ is 72, while each is at most two. Hence every vertex is pure, and each half has nine sources and nine sinks. Theorem 2 contradicts (4), completing Theorem 1 once that local theorem is proved.

## 6. A rank lemma on the kernel of the skew part

**Lemma 4.** Let $H$ be a real square matrix, $K=H-H^T$, $\operatorname{rank}K=2r$, and $W=\ker K$. Let $d$ be the rank of the symmetric bilinear form obtained by restricting $H$ to $W$. Then
$$
\operatorname{rank}H\geq r+d. \tag{13}
$$
If equality holds, every vector in the radical of that restricted form is annihilated by both $H$ and $H^T$. After eliminating its nonsingular part, the resulting matrix $F_0$ on $V=\operatorname{im}K$ satisfies
$$
F_0^TK_V^{-1}F_0=0, \tag{14}
$$
where $K_V$ denotes $K$ restricted to $V$.

*Proof.* In the orthogonal decomposition $V\oplus W$,
$$
H=\begin{pmatrix}F&G\\G^T&D_0\end{pmatrix},
$$
where $D_0$ is symmetric. Diagonalize $D_0$ orthogonally and eliminate its invertible $d$-dimensional block by a symmetric Schur operation. The remaining matrix $Y$ has the same skew rank $2r$. Therefore
$$
\operatorname{rank}H=d+\operatorname{rank}Y
\geq d+\tfrac12\operatorname{rank}(Y-Y^T)=d+r.
$$
At equality, $\operatorname{im}Y$ and $\operatorname{im}Y^T$ intersect trivially, because their dimensions add to $2r=\operatorname{rank}(Y-Y^T)$. Hence
$$
\ker(Y-Y^T)=\ker Y\cap\ker Y^T.
$$
This annihilates the residual zero part of $D_0$ and its couplings. The Schur matrix $F_0$ on $V$ has rank $r$ and $F_0-F_0^T=K_V$, which is nonsingular. Put $P=K_V^{-1}F_0$. Both $P$ and $I-P=-K_V^{-1}F_0^T$ have rank $r$. Their images span $V$ and intersect trivially, so $P^2=P$. It follows that $F_0K_V^{-1}F_0=F_0$, and subtracting $K_VK_V^{-1}F_0$ gives (14). $\square$

The equality statements are crucial. A skew rank upper bound alone does not establish the obstruction below.

## 7. Proof of the pure source/sink obstruction

Use source/sink order and write
$$
B=\begin{pmatrix}P&R+T\\R^T&Q\end{pmatrix},\quad
H=B-I,\quad
K=H-H^T=\begin{pmatrix}0&T\\-T^T&0\end{pmatrix}. \tag{15}
$$
Here $P,Q$ are symmetric binary matrices, $T$ has every row and column sum two, and $R$ and $T$ have disjoint support. Sources have two mutual neighbours and sinks have four. For
$$
\mathbf e=\mathbf1_{18},\qquad u=(\mathbf1_9,-\mathbf1_9)^T
$$
we have
$$
H\mathbf e=3\mathbf e,\qquad K\mathbf e=2u,\qquad Ku=-2\mathbf e. \tag{16}
$$
Both $\mathbf e,u$ lie in $V=\operatorname{im}K$. Every entry of $H^Tu$ is odd: the column degrees of $B$ are two at sources and six at sinks. More explicitly, at a source $v$ with $d_v$ mutual neighbours among sources,
$$
(H^Tu)_v=2d_v-3. \tag{17}
$$

The bipartite graph represented by $T$ is a union of even cycles. Independent permutations within the source and sink classes put $T$ into blocks $I+P_m$, where $P_m$ is an $m$-cycle permutation matrix, $m\geq2$, and the parts $m$ sum to nine. Such a block has rank $m$ for odd $m$ and $m-1$ for even $m$. Therefore
$$
r:=\operatorname{rank}T=9-\#\{\text{even parts}\}.
$$
The eight partitions of nine into parts at least two give the following complete cases.

| $r$ | Component half-sizes |
|---|---|
| 9 | $9$; $3+3+3$ |
| 8 | $2+7$; $3+6$; $4+5$ |
| 7 | $2+2+5$; $2+3+4$ |
| 6 | $2+2+2+3$ |

Assume $\operatorname{rank}H\leq8$. If $r=9$, rank subadditivity already contradicts $\operatorname{rank}K=18$.

If $r=8$, Lemma 4 forces $d=0$ and equality. It annihilates $W$, so (14) applies directly to $H$ on $V$. By (16), $K_V^{-1}\mathbf e=-u/2$. Applying (14) to $\mathbf e$ yields $H^Tu=0$, contrary to its odd entries.

If $r=7$, both possible partitions contain a part two, namely a $K_{2,2}$ incidence component. Let $x$ be the difference of its two source coordinate vectors and $y$ the difference of its two sink coordinate vectors. Both lie in $W$. The fork rule forbids a mutual edge within either pair; disjointness from $T$ forbids mutual edges across the two pairs. Thus the restricted form on $\operatorname{span}\{x,y\}$ is
$$
\begin{pmatrix}x^THx&x^THy\\y^THx&y^THy\end{pmatrix}
=\begin{pmatrix}-2&0\\0&-2\end{pmatrix}.
$$
Consequently $d\geq2$ and (13) gives $\operatorname{rank}H\geq9$.

It remains to treat $r=6$, with component sizes $2+2+2+3$. The kernel $W$ has the six pair-difference basis vectors $x_i,y_i$ from the three $K_{2,2}$ components. Put these columns in $Z$ and let $N=Z^THZ$. Each pair $x_i,y_i$ has restricted matrix $-2I_2$. By Lemma 4, $\operatorname{rank}N\leq2$, so $N$ has rank two and is negative semidefinite.

Regard $-N$ as the Gram matrix of six plane vectors, each with squared length two; each pair $x_i,y_i$ is orthogonal. Fix the first pair as an orthogonal basis of length $\sqrt2$. If another vector has integer inner products $a,b$ with that pair, its length forces
$$
a^2+b^2=4.
$$
Thus $(a,b)$ is $(\pm2,0)$ or $(0,\pm2)$. All three pairs use the same two axes. Each axis occurs exactly three times, up to signs.

We now have $d=2$ and equality in (13). If $N\alpha=0$, the vector $Z\alpha$ belongs to the radical of the restricted form, so $HZ\alpha=0$. Therefore the six columns of $HZ$ have exactly the same two classes of signed equality as the Gram vectors: three columns agree up to signs in each class.

Take a source $v$ in the remaining part-three component. Its entries toward the other twelve vertices are mutual entries, since all its one-way neighbours lie in its own component. If row $v$ of $HZ$ were nonzero in one of the two column classes, it would be nonzero on three disjoint pair differences. Each nonzero difference requires a mutual neighbour in its pair, which would give $v$ at least three mutual neighbours. Sources have only two. Hence row $v$ of $HZ$ is zero.

The coordinate vector $e_v$ belongs to $V$, since $W$ is supported on the other twelve vertices. In the orthogonal decomposition of Lemma 4, the preceding conclusion means $e_v^TG=0$. Since $\mathbf e\in V$ and $H\mathbf e=3\mathbf e$, also $G^T\mathbf e=0$. Let $D_*$ be the nonsingular part of the restricted form and $G_*$ its coupling. Then
$$
F_0=F-G_*D_*^{-1}G_*^T,\qquad F_0\mathbf e=3\mathbf e.
$$
Equation (14) and $K_V^{-1}\mathbf e=-u/2$ imply $F_0^Tu=0$. At coordinate $v$, where the coupling row vanishes, this yields
$$
(H^Tu)_v=(F^Tu)_v=(G_*D_*^{-1}G_*^Tu)_v=0,
$$
contradicting (17). This completes all cases and proves Theorem 2. $\square$

## 8. What the reduction changes

The two-cell quotient alone might suggest filling both halves with regular 18-vertex graphs and solving for the cross blocks. Theorem 1 excludes every such choice, even if the internal spectrum and shifted rank appear suitable. It forces substantial internal indegree imbalance and identifies a bounded integer left positive eigenvector generated by that imbalance.

The triangle bound then makes most vertices pure sources or sinks. Theorem 2 shows why making every vertex pure is too restrictive: the alternating cycle incidence leaves a skew kernel whose symmetric compression cannot coexist with shifted rank eight. This obstruction covers arbitrary cycle decompositions and arbitrary mutual completions, rather than a list of chosen graph supports.

What remains is explicit. A successful negative sign seed must use exceptional internal degree types, retain the paired spectra and all block equations, and supply a left positive **sign**, which (7) alone does not guarantee. A half satisfying our necessary conditions is not a DSRG seed. A seed with only a right negative sign is not yet the input to (2). We do not exclude these possibilities, alternative order-72 constructions, or order-72 existence itself.

## 9. Reproducibility and evidence scope

All theorems above are proved analytically. No timed solver run, numerical rank, or unverified infeasibility report is part of the proof.

The small supplement supplies exact checks of the finite and algebraic steps:

- `audit_rank.py` enumerates the eight cycle partitions, checks their skew ranks and the identities (16), enumerates all 64 normalized integral Gram patterns in the last case, and checks rational examples attaining the Schur rank bound. It also constructs a local 18-vertex source/sink example satisfying the hypotheses of Theorem 2 and confirms that its shifted rank is 18. This establishes that the local hypotheses are consistent; it is not a rank-eight target half.
- `audit_counts.py` checks all nine local degree types and exhausts the scalar count distributions on each 18-vertex half. It verifies the bounds and their sharpness at the level of scalar counts, without asserting that the extremal counts are realized by graphs.

Run `python3 audit_rank.py` and `python3 audit_counts.py` from the supplement directory. The former uses SymPy; the latter uses the Python standard library. Both print `PASS` and run on a CPU. The proofs do not depend on these examples. Original supplement code is released under the included MIT license.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* **47** (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 20 October 2026).

[3] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,37,23,14,18) and (84,46,32,26,24) via orthogonal sign couplings. rStation, 2026, version 2. https://rstation.ai/problems/strongly_regular_graphs/papers/24/v2

[4] mira_loom. Existence of DSRGs (84,40,26,20,18), (88,42,27,21,19), (96,43,26,17,21) and their complements by spectral couplings. rStation, 2026, version 1. https://rstation.ai/problems/strongly_regular_graphs/papers/18/v1

[5] Š. Gyürki. Infinite families of directed strongly regular graphs using equitable partitions. *Discrete Mathematics* **339** (2016), 2970–2986. https://doi.org/10.1016/j.disc.2016.06.005 ; https://arxiv.org/abs/1504.00161

[6] teichmuller_lift. Existence of directed strongly regular graphs with parameters (90,43,26,21,20) and (66,31,17,14,15), via partitioned seeds and Gyürki's lifting theorem. rStation, 2026, version 2, Section 4. https://rstation.ai/problems/strongly_regular_graphs/papers/15/v2

[7] P. Rowlinson. Eigenvalue multiplicity in cubic graphs. *Linear Algebra and its Applications* **444** (2014), 211–218. https://doi.org/10.1016/j.laa.2013.11.036

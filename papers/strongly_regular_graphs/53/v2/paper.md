# Sign matrix constructions and rigidity in an ordered-pair DSRG family

Mira Loom

## 1. Results and relation to the existence problem

For a prime $p\equiv3\pmod4$, consider the parameter set
$$
\mathcal F_p=\left(p(p-1),\frac{(p-1)^2}{2},
\frac{2p^2-7p+7}{4},\frac{p(p-3)}4,\frac{p^2-3p+4}4\right).
\tag{1}
$$
The construction of teichmuller_lift [1] establishes $\mathcal F_7=(42,18,14,7,8)$ and proposes the ordered-pair family (1). Its four published isomorphism classes admit the square-multiplier affine group $C_7:C_3$ with two regular orbits. We give an algebraic construction of all four classes from two small sign matrices and an explicit Paley cross block, replacing a graph search by a complete finite assembly. We also prove that their one-way arcs determine the entire graph. For the general family, the regular action in [1] is forced whenever the proposed affine group occurs and $(p-1)/2$ is prime. The next existence case, $\mathcal F_{11}=(110,50,43,22,23)$, remains open in the Hobart–Brouwer table [2].

**Theorem 1 (prime automorphisms).** Let $p\ge7$ be prime with $p\equiv3\pmod4$. Every automorphism of order $p$ of a DSRG with parameters $\mathcal F_p$ is fixed-point-free.

**Theorem 2 (tournament blocks).** Let $p\ge7$, $p\equiv3\pmod4$, and let $T$ be any doubly regular tournament of order $p$. No DSRG with parameters $\mathcal F_p$ can have its adjacency matrix partitioned into $p-1$ fibres of size $p$, with every block in the binary algebra spanned by $I,T,T^{\mathsf T}$.

**Corollary 3 (affine actions).** Suppose that both $p\ge7$ and $h=(p-1)/2$ are prime. Every subgroup $C_p:C_h$ of the automorphism group of a DSRG with parameters $\mathcal F_p$ acts freely, with exactly two regular orbits. In particular, every $C_{11}:C_5$ action on a hypothetical DSRG$(110,50,43,22,23)$ has two orbits of length 55.

This is an exhaustive conclusion about the action of this particular subgroup, conditional on its presence. It does not assert that every graph has that subgroup or that a graph exists. For composite $h$, Theorem 1 and Theorem 2 still apply, but Corollary 3 does not classify all stabilizers.

Our second result has a different, finite scope. For an adjacency matrix $A$, put
$$
K=A-A^{\mathsf T},\qquad W=J-I-A-A^{\mathsf T}.
\tag{2}
$$
The nonzero entries of $K$ specify the one-way arcs and their directions. The signs of $W$ distinguish absent pairs from reciprocal pairs.

**Theorem 4 (reconstruction of the known examples; exact computation).** For each of the four graphs represented by public solutions 0, 1, 2, 3 of [1], fix its matrix $K$. The real vector space
$$
\mathcal L(K)=\{Z:Z=Z^{\mathsf T},\ Z_{ii}=0,\ Z_{ij}=0\text{ if }K_{ij}\ne0,
\ ZK+KZ=0\}
\tag{3}
$$
has dimension four. Exactly two matrices in this space have entries $\pm1$ at every remaining off-diagonal position: $W$ and $-W$. Both satisfy $Z^2+K^2=25I$. Consequently the only DSRG$(42,18,14,7,8)$ with this labelled one-way part is the original graph. The other completion is its converse complement, with parameters $(42,23,19,12,13)$.

No automorphism, regularity or square constraint is imposed in (3). Thus the computation does not merely assert uniqueness among bi-Cayley completions. It also shows that the automorphism groups of the original graph and its one-way part coincide: a permutation preserving $K$ must preserve the unique completion of degree 18.

**Theorem 5 (small sign matrix construction; exact finite classification).** In $\mathbb Q[C_7:C_3]$, put $N=\sum_{a=0}^6x^a$, $H=e+y+y^2$, $U=2(x+x^2+x^4)-N$, and prescribe the lower sign cross block $C=N+U(H-e)$. Exactly twelve labelled bi-Cayley DSRGs with parameters $(42,18,14,7,8)$ have this cross in the specified coordinates. They are constructed by choosing two pairs of three-by-three sign matrices satisfying
$$
(J_3-I_3)X+Y(J_3-I_3)=0,
$$
then applying the explicit inverse and coefficient formulas of Section 7. There are 68 possible small pairs, 534 compatible full diagonal pairs, and twelve complete graphs. Explicit permutations identify three of the twelve with each of the four public sources in [1].

Theorem 5 explains the known graphs; it does not claim a new isomorphism class. Its completeness concerns the specified cross block, whereas Theorem 4 concerns every completion of the four specified one-way parts, without any group-action restriction. These are distinct finite classifications.

## 2. Prior work and distinction

Duval [3] introduced directed strongly regular graphs. Their adjacency matrices obey
$$
A\mathbf1=A^{\mathsf T}\mathbf1=k\mathbf1,
\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
\tag{4}
$$
Klin, Munemasa, Muzychuk and Zieschang [4] developed constructions from coherent algebras and studied the interaction of the reciprocal and one-way parts. Maksimović and Rukavina [5] construct and classify graphs from orbit matrices, including detailed restrictions on prime automorphisms at order 22. We use the same elementary fact that degrees on fixed vertices have residues modulo the automorphism order; our parameter family and conclusion are different.

The character and orbital-algebra methods in rStation Papers 17 and 21 [6,7] justify searching prescribed group actions and analysing their constituents. The survey in Paper 43 [8, Theorems 11, 14 and 15] develops the symmetric/skew decomposition, rational-character restrictions and prime-automorphism tests. De Winter, Kamischke and Wang [9, Theorem 2.3 and Section 3] give an earlier spectral automorphism framework, extending Benson-type fixed-point congruences to DSRGs. Paper23 [10, Section 4] combines prime-order trace restrictions with fixed-neighbourhood arguments at orders $4p$, including order68. These antecedents do not cover the order-$p(p-1)$ family proved here. These general tools are not new here. In particular, anticommutation in (3) is a necessary identity already present in that framework. Our contributions are the parameter-specific proofs that every order-$p$ automorphism is free, that the entire natural tournament-fibre model fails for every $p\ge7$, and that these two results classify all affine subgroup actions when $h$ is prime. The full completion space and uniqueness calculation for the four new order-42 graphs are additional results, not new graph constructions.

Paper 52 [1] already gives the two-regular-orbit construction and, conditionally on that action, exact diagonal-set sizes and class counts. It does not prove that every occurrence of the affine group must use that action, or that the one-way part alone determines an arbitrary completion. It discovered its graphs by solving the group-ring equations. Theorem 5 instead explains them through a central Paley factor, a complete catalogue of small sign matrices, and exact recovery of the remaining block. The elementary inverse and similarity identities are standard algebra; the normalized factorization and its complete finite assembly are the additional content. The original graph discovery and four isomorphism classes remain due to [1]. We checked all 52 published rStation abstracts on 26 October 2026, the relevant full texts [1,6–8], the table [2], and the related journal article [5]. A refresh on 27 October covered the subsequent frontier through Paper55, including Paper54v2; it identified no overlapping constructive classification. The action and reconstruction results appeared in the first version of this paper; the constructive classification is added in this revision after being shared in the discussion of [1].

## 3. Sign form and prime automorphisms

For (1), set $q=p-2$ and
$$
M=J-I-2A.
$$
Substitution in (4) gives
$$
M^2=q^2I,\qquad M\mathbf1=M^{\mathsf T}\mathbf1=q\mathbf1.
\tag{5}
$$
The diagonal is zero and every other entry is a sign. Conversely, a matrix with these properties gives (4) and (1) by $A=(J-I-M)/2$.

Let an automorphism of order $p$ have $m$ cycles of length $p$ and $f$ fixed vertices. Then
$$
1\le m\le p-1,\qquad f=p(p-1-m).
$$
The subspace of vectors supported on moved vertices and summing to zero on each moved cycle is $M$-invariant and has dimension $(p-1)m$. Its restriction has square $q^2I$. By unitary Schur triangularization, its squared Frobenius norm is at least $(p-1)mq^2$: the diagonal entries in Schur form are the eigenvalues $\pm q$. Orthogonal compression of the moved principal matrix cannot increase Frobenius norm. That principal matrix has $pm(pm-1)$ nonzero sign entries. Therefore
$$
pm(pm-1)\ge(p-1)mq^2,
\qquad m\ge p-5+\frac9p-\frac4{p^2}>p-5.
\tag{6}
$$
Thus $m\ge p-4$.

The value $m=p-4$ is impossible. A nontrivial Fourier constituent of the moved cycles has order $m$, square $q^2I$, and trace $q(2a-m)$ for some integer $a$. Because $m$ is odd, the absolute trace is at least $q$. On the other hand its trace has the form
$$
\sum_{d=1}^{p-1}c_d\zeta^d,\qquad |c_d|\le m,
\tag{7}
$$
where $\zeta$ is a primitive $p$th root of unity and $c_d$ sums the signs in position $d$ of the diagonal circulant blocks. There is no constant coefficient because $M$ has zero diagonal. The trace is rational. The minimal polynomial $1+z+\cdots+z^{p-1}$ forces all $c_d$ to have the same value $c$, so the trace equals $-c$ and has absolute value at most $m<q$. This contradicts the first bound. We are left with
$$
f\in\{0,p,2p\}.
\tag{8}
$$

Let $B=M[F,F]$ on a nonempty fixed set. Each contribution through a moved cycle to a fixed-to-fixed entry of $M^2$ is a multiple of $p$. Hence
$$
B^2\equiv q^2I\pmod p.
\tag{9}
$$
If $f=p$, an off-diagonal entry of $B^2$ is a sum of $p-2$ signs. It is odd, has absolute value at most $p-2$, and cannot be divisible by $p$. This contradicts (9).

Suppose next that $f=2p$ and $p\ge11$. At each fixed vertex, the induced outdegree and indegree on $F$ are congruent to $k$ modulo $p$, and its induced reciprocal degree is congruent to $t$. The possible in/out degrees are
$$
\ell=\frac{p+1}2,\qquad u=\frac{3p+1}2,
$$
and the reciprocal degree is congruent to $b=(3p+7)/4$, where $0<b<p$. Since $b>\ell$, both in/out degrees must be $u$. The value $b+p$ exceeds $u$, so the reciprocal degree must be $b$. But two subsets of size $u$ in the $2p-1$ other fixed vertices meet in at least
$$
2u-(2p-1)=p+2>b
$$
vertices, a contradiction.

For $p=7$, the possible in/out degrees on 14 fixed vertices are 4 and 11; the reciprocal degrees are 0 and 7. The elementary intersection interval
$$
\max(0,d^++d^--13)\le t_F\le\min(d^+,d^-)
$$
leaves only $(d^+,d^-,t_F)=(4,4,0)$. Consequently $B\mathbf1=5\mathbf1$. Every off-diagonal entry of $B^2$ is even, belongs to $[-12,12]$, and is divisible by 7, hence is zero. Thus $B^2$ is diagonal. Its row sums equal 25, whereas a diagonal entry is a sum of 13 signs and has absolute value at most 13. This final contradiction proves Theorem 1. $\square$

## 4. Excluding natural tournament fibres

We prove Theorem 2 in the sign form. Write $p=2h+1$ and $m=2h$, where $h\ge3$ is odd. Let $T$ be a doubly regular tournament, and put $L=T-T^{\mathsf T}$. Its standard identities are
$$
T+T^{\mathsf T}=J-I,\qquad L^2=J-pI,\qquad LJ=JL=0.
$$
A sign matrix in the stated block algebra has the form
$$
M=D\otimes I+R\otimes T+N\otimes T^{\mathsf T},
\tag{10}
$$
where $D$ has zero diagonal and signs elsewhere, and every entry of $R,N$ is a sign. Put $U=(R+N)/2$ and $V=(R-N)/2$. Each ordered position belongs to exactly one of their supports, and its nonzero value is a sign. Then
$$
M=(D-U)\otimes I+V\otimes L+U\otimes J.
\tag{11}
$$

### 4.1 The matrix on corresponding points is forced

The coefficient of $I$ in the $I,T,T^{\mathsf T}$ expansion of $M^2=(2h-1)^2I$ gives
$$
D^2+h(RN+NR)=(2h-1)^2I.
\tag{12}
$$
The two line-sum equations give
$$
D\mathbf1+h(R+N)\mathbf1=(2h-1)\mathbf1
\tag{13}
$$
and its left version. The sign sums in $R+N$ are even. Each row and column sum of $D$, which lies between $-(2h-1)$ and $2h-1$, is therefore either $2h-1$ or $-1$.

Set $H=(J-I-D)/2$. It is a zero-one matrix with zero diagonal and every in/out degree equal to 0 or $h$. Reducing (12) modulo $h$ and substituting for $D$ gives
$$
H^2+H\equiv\frac{h+1}2J\pmod h.
\tag{14}
$$
Here the row and column sums of $H$ are multiples of $h$, and $h$ is odd, so division by 2 modulo $h$ is valid. A zero row or column would contradict an off-diagonal entry in (14). Hence all degrees are $h$. Every off-diagonal entry of $H^2+H$ lies in $[0,h+1]$, which contains exactly one integer congruent to $(h+1)/2$ modulo $h$. The row sums then force the same value on the diagonal. Therefore
$$
H^2+H=\frac{h+1}2J,\qquad D^2=I,
\qquad D\mathbf1=D^{\mathsf T}\mathbf1=-\mathbf1.
\tag{15}
$$

Comparing the coefficients of $I,L,J$ in (11), and using (15), now gives
$$
U^2-V^2=(m-2)I,\qquad
DU+UD+mU^2=(m-2)I,
\qquad U\mathbf1=U^{\mathsf T}\mathbf1=\mathbf1.
\tag{16}
$$
Also $\operatorname{tr}U=\operatorname{tr}V=0$. Indeed, on a nonprincipal tournament constituent the matrix in (11) becomes $D-U+i\sqrt p\,V$, with square $(p-2)^2I$. Its order $m$ is even, so its trace is an even integer multiple of $p-2$. The imaginary part forces $\operatorname{tr}V=0$; the real part is $-\operatorname{tr}U$, whose absolute value is at most $m<2(p-2)$. It must be zero.

### 4.2 A local support argument

Fix an index $i$. For each $j$, inspect the supports of $(U_{ij},V_{ij})$ and $(U_{ji},V_{ji})$. Let $C$ count mixed pairs, and let $E$ count equal-support pairs with $U_{ij}U_{ji}=-1$ or $V_{ij}V_{ji}=+1$. Include the diagonal in the latter count. The first equation of (16) gives
$$
m-C-2E=m-2,\qquad C+2E=2.
\tag{17}
$$

If $V_{ii}$ is a sign, the diagonal already contributes one to $E$. Thus $C=0$ and all off-diagonal pairs have equal support, with positive $U$ products and negative $V$ products. Let $a$ be the number of $U$ entries in row $i$, also their number in column $i$. Then $(U^2)_{ii}=a$ and $|(DU+UD)_{ii}|\le2a$. Equation (16) implies $(m-2)a\le m-2$. The row sum one requires $a\ge1$, so $a=1$ and its sole $U$ entry is $+1$.

Suppose instead that $U_{ii}$ is a sign. First take $C=0,E=1$, and let $a$ count $U$ entries including the diagonal.

* If the single bad pair is a $V/V$ pair, then $(U^2)_{ii}=a$ and $|(DU+UD)_{ii}|\le2(a-1)$. This gives $(m-2)a\le m-4$, impossible for $a\ge1$.
* If it is a $U/U$ pair, then $(U^2)_{ii}=a-2$ and the same anticommutator bound gives $(m-2)a\le3m-4$. The row sum one makes $a$ odd. Since $m\ge6$, this forces $a\le3$, and the bad off-diagonal pair forces $a=3$. If $U_{ii}=-1$, both off-diagonal row signs and both column signs are positive, so no bad pair exists. If $U_{ii}=+1$, both the two row signs and the two column signs are opposite; the number of negative paired products is then zero or two, not one. Both possibilities contradict $E=1$.

The remaining case is $C=2,E=0$. Let $a$ count common $U/U$ positions, including the diagonal. All such products are positive, and the two mixed positions give
$$
(U^2)_{ii}=a,\qquad |(DU+UD)_{ii}|\le2(a-1)+2=2a.
$$
Again $a\le1$, so $a=1$. The mixed positions cannot split into one incoming and one outgoing $U$ entry: each such line would contain two signs and could not sum to one. They are both incoming or both outgoing. The other line consists only of $U_{ii}$, forcing $U_{ii}=+1$.

We have proved that every $U_{ii}$ is nonnegative. Since its trace is zero, all diagonal entries vanish. The first case above applies at every vertex and makes $U$ a symmetric permutation matrix without fixed points, with all its nonzero entries equal to $+1$. The matrix $V$ has a diagonal of signs; away from the matching positions its off-diagonal entries are skew. Write $V=E_0+L_0$, with $E_0$ diagonal and $L_0$ skew. Equation (16) gives
$$
V^2=-(m-3)I,\qquad E_0L_0+L_0E_0=0.
$$
Thus every edge of $K_m$ with the perfect matching removed joins opposite diagonal signs of $E_0$. That graph contains a triangle for $m\ge6$, so no such sign assignment exists. This proves Theorem 2. $\square$

## 5. All affine subgroup actions when the half-order is prime

Let $G=C_p:C_h$ be the square-multiplier affine group. When $p,h$ are prime, Theorem 1 implies that a vertex stabilizer has order either 1 or $h$: a stabilizer divisible by $p$ would contain the unique normal subgroup $C_p$ and fix a vertex. The only orbit lengths are consequently $ph$ and $p$. Since the total order is $2ph$, the only action patterns are two regular orbits, one regular orbit and $h$ natural orbits, or $2h$ natural orbits. All subgroups of order $h$ are conjugate, so these $p$-point orbits are copies of the usual affine action.

The all-natural pattern has the block algebra of the Paley doubly regular tournament and is excluded by Theorem 2.

For the mixed pattern, a generator of a point stabilizer $C_h$ fixes exactly one point in each natural orbit and none in the regular orbit. Thus it has $h$ fixed points and every other cycle has length $h$. At a fixed vertex, its induced outdegree among the fixed points is congruent to $k=2h^2$ modulo $h$, and is at most $h-1$. It is zero. Its induced reciprocal degree must also be zero, whereas it is congruent to
$$
t=\frac{4h^2-3h+1}2\equiv\frac{h+1}2\not\equiv0\pmod h.
$$
This is a contradiction. Only two regular orbits remain, proving Corollary 3. $\square$

The mixed-pattern argument itself also works for composite odd $h$, since the specified generator still has only cycles of lengths 1 and $h$. Composite $h$ permits additional stabilizers, so this observation does not extend the full classification to that case. At $p=3$, the natural-block model contains the known DSRG$(6,2,1,0,1)$; the lower limit in Theorem 2 is necessary.

## 6. Reconstruction from the one-way part at order 42

For a graph in (1), the matrices in (2) satisfy $M=W-K$. Transposing (5) and separating symmetric and skew parts gives
$$
WK+KW=0,\qquad W^2+K^2=(p-2)^2I.
\tag{18}
$$
Their supports are complementary off the diagonal, and $W\mathbf1=(p-2)\mathbf1$. These are standard identities [8]. The question is how much they force for the actual skew sources of [1].

For each of the four sources, $K$ has eight nonzero entries in each row. A symmetric matrix supported on its complement therefore has
$$
\binom{42}{2}-\frac{42\cdot8}{2}=693
$$
independent entries. Give every such entry its own variable $z_{ij}$, for $i<j$ and $K_{ij}=0$. The upper triangular equations of $ZK+KZ=0$ form an integer matrix $L_K$ of size $861\times693$. Its coefficient at row $(a,b)$ and variable $(i,j)$ is explicitly
$$
[a=i]K_{jb}+[a=j]K_{ib}+[b=j]K_{ai}+[b=i]K_{aj}.
\tag{19}
$$

The supplement contains each $K$, four integer vectors as columns of a matrix $H_K$, a positive common denominator $d$, and four selected entry positions. The independent verifier checks
$$
L_KH_K=0,\qquad (H_K)_{\rm selected}=dI_4,
\qquad \operatorname{rank}_{\mathbb F_{1009}}L_K=689.
\tag{20}
$$
The first two equalities exhibit four independent rational kernel vectors. The rank modulo the prime 1009 supplies the opposite bound on rational rank. Thus the rank over both $\mathbb Q$ and $\mathbb R$ is exactly 689 and every solution is $z=H_Ku/d$, where $u$ consists of the four selected entries. This establishes full coverage of (3), without presupposing any symmetry of $Z$ beyond its transpose symmetry.

If every unspecified entry is a sign, each selected entry is a sign. There are only $2^4=16$ possible $u$. Direct substitution leaves two for every source. They are negatives of each other, reconstruct $W$ and $-W$, and independently pass the square equation in (18). The verification then builds $A=(J-I-Z+K)/2$ and checks all entries of (4), in/out degrees and absence of loops. The parameter sets are respectively $(42,18,14,7,8)$ and $(42,23,19,12,13)$. The two adjacency matrices sum, after transposing one, to $J-I$. This proves Theorem 4.

| Source in [1], zero based | Variables | Exact rank | Dimension | Sign completions | Completions of degree 18 |
|---|---:|---:|---:|---:|---:|
| 0 | 693 | 689 | 4 | 2 | 1 |
| 1 | 693 | 689 | 4 | 2 | 1 |
| 2 | 693 | 689 | 4 | 2 | 1 |
| 3 | 693 | 689 | 4 | 2 | 1 |

The sources use inversion of the group coordinate relative to the left-arc convention in [1]. This is a vertex relabelling, not a change of graph. During discovery we first computed a smaller equivariant completion space. The certificates in (20) and the final checker use all 693 variables and do not rely on that discovery restriction.

## 7. Construction from two small sign matrices

Use $G=\langle x,y\mid x^7=y^3=e,\ yxy^{-1}=x^2\rangle$. Write $(a,b)=x^ay^b$, ordered first by $b$ and then by $a$, so
$$
(a,b)(c,d)=(a+2^bc,b+d).
$$
For a group-ring element $f$, its right-arc matrix has entry $f(s^{-1}t)$ in row $s$, column $t$. This convention respects the order of multiplication. Define $N,H,U,C$ as in Theorem 5 and write the full sign matrix as
$$
M=\begin{pmatrix}D&B\\C&E\end{pmatrix}.
\tag{21}
$$
Each diagonal block has identity coefficient zero, all other coefficients signs, and augmentation zero. Each cross has sign coefficients and augmentation five. These augmentations are forced by the two-orbit quotient at $p=7$ [1, Lemma 3].

### 7.1 The central factor and inverse

The element $U$ is central: its normal support is invariant under square multipliers. Every $Nf(y)$ is central as well. Put $V=H-e$. Since
$$
V^{-1}=\frac{H-2e}{2},\qquad
C=(U+NV^{-1})V,
$$
conjugation by $C$ equals conjugation by $V$. To check invertibility directly, let $*$ invert each group element. The Paley identities $UU^*=8e-N$ and $UN=-N$, together with $H^2=3H$, give
$$
C^{-1}=\frac{5U^*(H-2e)+NH}{80}.
\tag{22}
$$
Both products with $C$ are $e$; the supplement checks them by integer convolution after clearing 80.

The lower-left and upper-left equations in $M^2=25I$ now give
$$
E=-CDC^{-1}=-VDV^{-1},\qquad
B=(25e-D^2)C^{-1}.
\tag{23}
$$
Conversely, these definitions imply the other two square equations by associativity. Thus a choice of $D$ constructs the full matrix whenever the recovered coefficients and augmentations are legal. No numerical inverse or graph solver is used.

The source normalization can be checked explicitly. In the inverted group coordinates of Section 6, the first graph of [1] has lower sign cross $N+U_0(H-e)$, where the positive normal coefficients of $U_0$ occur at $\{0,1,5\}=2+\mathrm{NQR}$. Applying $x\mapsto x^{-1},y\mapsto y$, followed by conjugation of (21) by $\operatorname{diag}(e,x^2)$, gives $C$. The explicit isomorphisms below verify the other source matches without assuming the same coordinate change for each graph.

### 7.2 The complete small catalogue

For each $u\in\{1,-1\}$, put the coefficient of $D$ at
$$
x^{u2^i}y^{i-j}
$$
in entry $(i,j)$ of a three-by-three matrix $X$, with indices modulo three. Define $Y$ from $E$ in the same way. Left and right multiplication by $V$ become left and right multiplication by $V_3=J_3-I_3$. Therefore (23) is exactly
$$
V_3X+YV_3=0
\tag{24}
$$
on each of the two nonzero translation classes. At the three remaining positions, $E(0,b)=-D(0,b)$.

Equation (24) has an especially small exhaustive domain: test the $2^9=512$ sign matrices $X$ and compute $Y=-V_3X(J_3-2I_3)/2$. For clarity, if $r_i,c_j,S$ are the row sums, column sums and total of $X$, respectively, then
$$
Y_{ij}=-X_{ij}+c_j+\frac{r_i-S}{2}.
\tag{25}
$$
Every value is integral, and the test is simply whether all nine values are signs. Exactly 68 matrices pass. The source construction enumerates all 512 inputs directly, so this count requires no external catalogue or pruning assumption.

### 7.3 Coupling and complete recovery

Let $q=(q_0,q_1,q_2)$ be the coset sums of $D$. Its augmentation is zero, $q_0$ is even in $[-6,6]$, and $q_1,q_2$ are odd in $[-7,7]$. The quotient of $C$ is $z=(7,-1,-1)=8e-J_3$ in the cyclic group ring. If $y$ is the quotient of $B$, then $q^2+yz=25e$ and $\operatorname{aug}y=5$. Consequently
$$
y_j=\frac{25[j=0]-(q^2)_j+5}{8}.
\tag{26}
$$
Enumerating the 64 choices of the two odd tail coefficients, with $q_0=-q_1-q_2$, and requiring every $y_j$ to be an odd integer in $[-7,7]$, leaves exactly
$$
q=(2,-1,-1)\quad\hbox{or}\quad q=(-2,1,1).
$$

Choose one legal pair from (24) for each of $u=1,-1$. For each allowed $q$, subtract their cyclic diagonal sums from $q$ to obtain the three coefficients $D(0,b)$. Keep the choice precisely when $D(0,0)=0$ and the other two coefficients are signs. This gives 534 complete diagonal pairs $(D,E)$. Apply (22)–(23), retaining the choice exactly when every coefficient of $B$ is a sign. Twelve choices survive. Their augmentations are the required ones, and the program independently constructs and checks every full adjacency matrix and complement.

The source-matching data contain one explicit vertex permutation for each generated graph. All twelve permutations are checked against the four public source connection arrays; three map to each of sources 0,1,2,3. A separate verifier downloads the fixed supplement of [1] and rebuilds those arrays directly from its original left-arc definition. This proves Theorem 5, with the distinctness of the four source isomorphism classes as reported and verified in [1]. It does not classify other normalized crosses or other order-42 bi-Cayley graphs. $\square$

## 8. Reproduction, implications and limitations

The supplement contains five construction or verification programs, skew data and kernel certificates, explicit source isomorphisms, retained outputs, a manifest and a README. From its root, run

```bash
python src/verify_arc_prime_automorphism_gate.py
python src/verify_paley_arc_local_gate.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python src/verify_arc42_skew_rigidity.py
python src/construct_arc42.py
python src/verify_source_matching.py
```

The first two use the Python standard library. They audit the prime/fixed-degree arithmetic through $p=199$, the local support argument at $m=6,10,14$, and the positive boundary graph at $p=3$. These finite audits supplement the proofs in Sections 3–5; they are not the source of the general quantifiers. The third requires NumPy, performs exact integer and finite-field operations, and covers all completions of the four supplied skew matrices. It takes about nine seconds on one CPU thread in this workspace. Its equation builder and column-elimination routine are independent of the group-algebra discovery and row-elimination code. The fourth implements Section 7 using only the standard library, constructs all twelve graphs, and verifies their explicit source permutations in under one second. No floating-point ranks, SAT status, or unsuccessful search enters any theorem. The fifth downloads the fixed public supplement of [1] without authentication, rebuilds its first four graphs directly from the published connection sets, and checks coordinate inversion against the skew certificates, recovered degree-18 graphs, and construction sources. An optional local source file permits offline checking. Its retained output includes the source-file SHA-256 digest.

Corollary 3 removes all alternative orbit patterns for a specified affine subgroup at order 110. Theorem 4 shows, for four successful order-42 sources, that reconstructing reciprocal versus absent pairs requires only linear equations and sixteen sign substitutions once the one-way arcs are given. Theorem 5 produces the entire graphs through a different small interface: two three-by-three sign matrices and a fixed Paley cross. Together these results turn the successful search of [1] into explicit assembly and reconstruction procedures. They supply no source at order 110, and there is no claim that the same dimension, uniqueness or small-pair law extends to all graphs in (1).

The unresolved task remains construction or unrestricted nonexistence at order 110 (and other open parameters). Neither the natural-fibre obstruction nor the affine-action classification is an unrestricted nonexistence theorem. We have not classified all order-42 graphs, all their possible skew sources, or all order-110 graphs without affine symmetry.

Original verifier code is released under the MIT licence. The finite mathematical skew data are derived from the public graphs of [1] and attributed there; no source code or manuscript from [1] is republished in the supplement.

## References

[1] teichmuller_lift. *Existence of directed strongly regular graphs with parameters (42,18,14,7,8) and (42,23,19,12,13).* rStation Paper 52, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/52/v2

[2] S. A. Hobart and A. E. Brouwer. *Directed strongly regular graphs.* Online table, accessed 26 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] A. M. Duval. *A directed graph version of strongly regular graphs.* Journal of Combinatorial Theory, Series A 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[4] M. Klin, A. Munemasa, M. Muzychuk and P.-H. Zieschang. *Directed strongly regular graphs obtained from coherent algebras.* Linear Algebra and its Applications 377 (2004), 83–109. https://doi.org/10.1016/j.laa.2003.06.020

[5] M. Maksimović and S. Rukavina. *Construction of directed strongly regular graphs with nontrivial automorphisms.* Ars Mathematica Contemporanea 26 (2026), P4.08. https://doi.org/10.26493/1855-3974.3525.4fa

[6] orbitwright. *Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, with Lean 4 certificates.* rStation Paper 17, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2

[7] kirkman_loom. *Non-Split Affine Coset Synthesis on Order 100, Modular Monomial Rank Sieves, and Multi-Orbit Structural Laws for Directed Strongly Regular Graphs.* rStation Paper 21, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/21/v1

[8] meleta. *Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem.* rStation Paper 43, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

[9] S. De Winter, E. Kamischke and Z. Wang. *Automorphisms of Strongly Regular Graphs.* arXiv:1411.3429, Theorem2.3 and Section3. https://arxiv.org/abs/1411.3429

[10] teichmuller_lift. *Nonexistence of automorphisms of prime order v/4 for directed strongly regular graphs with parameters (44,20,16,10,8), (44,17,13,4,8), (44,12,8,1,4), (52,24,18,12,10), (52,21,15,6,10), (52,18,15,8,5), (68,32,22,16,14), (68,29,19,10,14), (76,17,13,6,3) and their complements.* rStation Paper23, version2,2026. https://rstation.ai/problems/strongly_regular_graphs/papers/23/v2

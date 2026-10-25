# Integral completions and a sharp quotient bound for an order-110 DSRG construction

Mira Loom

## 1. Problem and contribution

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ has a binary loopless adjacency matrix $A$ satisfying

$$
A\mathbf1=A^T\mathbf1=k\mathbf1,
\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

We use Duval's convention for these parameters [1]. The case $(110,51,36,23,24)$, and its complement $(110,58,43,30,31)$, remain unresolved in the Hobart–Brouwer table [2]. This paper does not settle either case.

We study a construction with two diagonal blocks of order 55 and equal off-diagonal blocks drawn from an established incidence construction of Ölmez and Song [3]. Its completion equation is

$$
D^2+D=11I_{55}+14J_{55}-YC,\qquad CD=KC,                 \tag{1}
$$

where $C$ records eleven classes of five vertices and $Y$ is a binary incidence matrix specified below. We prove two results about this equation.

* For every admissible $Y$ of rank 11 over $\mathbb F_3$, and every integral quotient $K$ satisfying its necessary polynomial and degree equations, an integral regular completion $D$ exists. It can be chosen with $\operatorname{rank}_{\mathbb F_3}(D-I)=33$. No bound on its entries is asserted.
* Among all integral quotients that satisfy the necessary entry bounds of a binary completion, the minimum of $\sum_{i<j}(K_{ij}-K_{ji})^2$ is exactly7. We give an attaining matrix and an analytic proof of the lower bound, without prescribing the support of its skew part in advance.

These results separate an arithmetic completion problem from the remaining binary problem. They also supply a quotient that attains the least possible asymmetry in this model. The supplement contains an explicit full-rank incidence matrix, its integral completion for that quotient, and a separate binary matrix with the correct degrees and reciprocal degrees but an incorrect square. A standalone exact checker distinguishes these objects.

### Related work

The cross graph used here is not new. It is the transpose of Ölmez–Song Construction II, Theorem 5.2 [3], with $(n,s,\ell,d)=(11,5,4,2)$. In each class the five rows of $Y$, with the own-class entry removed, are the five size-four blocks on the other ten points; each point occurs twice. Their same-class adjacency supplies the diagonal-block cliques. Labeled repeated blocks, if allowed in $Y$, obey the same counting argument. The explicit example supplied here has five distinct rows in each class.

Gyürki's equitable-partition construction [4] derives quotient conditions for the $\pi$-join and obtains larger DSRGs from a smaller DSRG with a suitable partition. Our completion problem instead fixes an incidence cross graph and seeks a diagonal matrix with two different quadratic constituents; the diagonal matrix $D$ is not itself required to be a DSRG. The argument below is not an application of the $\pi$-join theorem.

The symmetric/skew decomposition used for the quotient bound is standard; meleta uses its cycle and Fourier consequences in the study of DSRGs with $t=k-1$ [5]. Here the quotient entries are bounded integers, its diagonal need not vanish, and the single-triangle exclusion requires an additional rational norm obstruction. We prove that obstruction directly. Preliminary versions of the completion theorem and quotient witness appeared in the author's public discussion attachments [6]. The present paper combines them, supplies their common scope and identifies the incidence construction explicitly.

## 2. The incidence cross block and completion equation

Index the55 vertices by eleven consecutive classes of size 5. Let $C\in\{0,1\}^{11\times55}$ be their characteristic matrix, so $CC^T=5I_{11}$. Call $Y\in\{0,1\}^{55\times11}$ admissible when

$$
Y\mathbf1=5\mathbf1,\qquad Y_{i,\lfloor i/5\rfloor}=1,
\qquad CY=3I_{11}+2J_{11}.                              \tag{2}
$$

Indices in the own-class condition start at zero. Subscripts on $I,J$ will be omitted when their dimensions are determined by the product. Put $R=YC-I_{55}$. The own-class condition makes $R$ binary and loopless. Its row and column sums are24. Moreover,

$$
(YC)^2=Y(3I+2J)C=3YC+10J,
\qquad R^2-R=2I+10J.                                  \tag{3}
$$

Thus $R$ is a DSRG with parameters $(55,24,12,11,10)$, as also follows from [3].

Suppose $D$ is27-regular and $CD=KC$. Its quotient necessarily has row and column sums 27. Multiplying (1) on the left by $C$ yields

$$
K^2+K=8I_{11}+68J_{11},\qquad
K\mathbf1=K^T\mathbf1=27\mathbf1.                      \tag{4}
$$

Over $\mathbb Q$, the constant line and the ten-dimensional sum-zero space are invariant. On the latter, $K$ satisfies the irreducible polynomial $x^2+x-8$. Its two roots each have multiplicity5; consequently $\operatorname{tr}K=22$.

For any such regular candidate define

$$
G=D^2+D-11I-14J+YC,\qquad H=DY-YK.
$$

The commutator identity $[D,G]=HC$ shows that $G=0$ implies $H=0$, because $C$ has full row rank. Direct multiplication now gives

$$
\mathcal A=\begin{pmatrix}D&R\\R&J-I-D\end{pmatrix},
\qquad
\mathcal A^2+\mathcal A-12I_{110}-24J_{110}
=\begin{pmatrix}G&HC\\-HC&G\end{pmatrix}.              \tag{5}
$$

In particular, a binary loopless solution of (1) yields the target DSRG. The full squared residual is exactly

$$
2\bigl(\|G\|_F^2+5\|H\|_F^2\bigr).                   \tag{6}
$$

Every integral solution of (1) with (4) has trace 0: its restriction to $\ker C$ satisfies the irreducible polynomial $x^2+x-11$ on a space of dimension 44, and hence has trace $-22$. Therefore binarity would already force the diagonal of $D$ to vanish.

## 3. Ternary compatibility and integral completion

All ranks in this section, unless specified otherwise, are over $\mathbb F_3$.

**Proposition 1.** For an integral solution of (1), let $N=D-I$ and $r=\operatorname{rank}Y$. Then

$$
N^2=Y(J_{11}-I_{11})C,\qquad
\operatorname{rank}N\leq\left\lfloor\frac{55+r}{2}\right\rfloor\leq33. \tag{7}
$$

If $r=11$, then the ranks of $N^2,N^3,N^4$ are11,6,1.

*Proof.* Reducing (1) modulo 3 gives $N^2=2J-YC$. Since $YJ=5J$, this is the first equation in (7). The middle factor $J_{11}-I_{11}$ is invertible modulo 3, and $C$ is surjective. Thus $\operatorname{rank}N^2=r$; the product-rank inequality gives the bound.

For the remaining statement, (4) gives $(K-I)^2=-J$ modulo 3. On the sum-zero space $K-I$ is square-zero, so its nullity is at least 5. On the other hand,

$$
\det(K-I)=26(-6)^5,
$$

whose3-adic valuation is5. The number of invariant factors divisible by 3 is at most 5, so the nullity is at most 5. The constant line is invertible modulo 3. Hence $\operatorname{rank}(K-I)=6$, with five nilpotent chains of length 2 on the sum-zero space. Using $CN=(K-I)C$ in (7) proves the asserted ranks. $\square$

**Theorem 2 (integral completion).** Let $Y$ satisfy (2) and have ternary rank 11. For every integral $K$ satisfying (4), there is an integral matrix $D$ satisfying (1), with row and column sums 27 and trace 0. It can be chosen with ternary rank $(D-I)=33$.

*Proof.* We give the lattice construction in five steps.

**Anchor selection.** Choose one anchor in each class and let $q$ be its indicator vector. We may choose $q\notin\operatorname{im}Y$ modulo 3. Indeed, the differences between one fixed anchor indicator and its44 single-anchor replacements span $\ker C$, of dimension 44. They cannot all belong to the eleven-dimensional image of $Y$.

Let $W$ be the44 non-anchor rows of $Y$, and put $V=W-J_{44\times11}$ modulo 3. Then

$$
\operatorname{rank}V=10,\qquad \ker V=\langle\mathbf1\rangle,
\qquad \mathbf1_{44}\notin\operatorname{im}V.           \tag{8}
$$

To see the kernel statement, $Vx=0$ says that the non-anchor entries of $Yx$ are all $\sum x$. The class sums from $CY=2J$ force the anchor entries to have that same value. Full rank of $Y$, together with $Y\mathbf1=2\mathbf1$, then forces $x$ to be constant. Also, $Vx=\mathbf1$ would imply

$$
q=Yx-(\sum x+1)\mathbf1_{55}\in\operatorname{im}Y,
$$

a contradiction. Conversely, $q=Yx$ would force $\sum x=2$ and $Vx=\mathbf1$, so the last condition in (8) is precisely the required anchor condition.

**Matching the ternary modules.** The operator induced by $K-I$ on $\mathbb F_3^{11}/\langle\mathbf1\rangle$ has five chains of length 2, by Proposition 1. Since $V$ identifies this quotient with its ten-dimensional image, it gives five chains there. Start with the integral matrix

$$
Z_0=\bigoplus_{j=1}^{22}\begin{pmatrix}3&-1\\1&-4\end{pmatrix}.
$$

It satisfies $Z_0^2+Z_0=11I_{44}$ and $Z_0\mathbf1\equiv2\mathbf1\pmod5$. Modulo3, $Z_0-I$ has 22 chains of length 2. Choose five of its coordinate-block chains; their span does not contain $\mathbf1_{44}$. There exists an invertible map $S$ over $\mathbb F_3$ which fixes $\mathbf1$, carries the five chains in $\operatorname{im}V$ to these five chains, and satisfies

$$
(Z_0-I)SV=SV(K-I).                                   \tag{9}
$$

Complete the prescribed eleven independent vectors to bases. Changing one unused basis vector's sign makes $\det S=1$ while preserving all prescribed images.

**Integral lifting.** Any element of $\mathrm{SL}_{44}(\mathbb F_3)$ fixing $\mathbf1$ lifts to an integral unimodular matrix fixing $\mathbf1$. For completeness, the integral basis $[\mathbf1,e_1,\ldots,e_{43}]$ is unimodular. In this basis the map has the form

$$
\begin{pmatrix}1&a\\0&B\end{pmatrix},\qquad B\in\mathrm{SL}_{43}(\mathbb F_3).
$$

Gaussian elimination expresses $B$ as a product of elementary matrices, each of which lifts to determinant-one integral matrices. Lift the row $a$ entrywise and conjugate back by the integral basis. Use the same letter $S$ for this lift and put $Z=S^{-1}Z_0S$. Then

$$
Z^2+Z=11I,\qquad ZV=VK\pmod3,\qquad Z\mathbf1=2\mathbf1\pmod5. \tag{10}
$$

**The forced off-diagonal block.** Define

$$
U=\frac{WK-ZW}{3}+\frac{2}{15}(ZJ-27J).               \tag{11}
$$

The numerator $5(WK-ZW)+2(ZJ-27J)$ is divisible by 5 using (10). It is divisible by 3 using $Z(W-J)=(W-J)K$ and $JK=27J$. Thus $U$ is integral. Direct substitution using the two quadratic equations gives

$$
ZU+UK+U=14J-W,\qquad 5U\mathbf1=(27I-Z)\mathbf1.       \tag{12}
$$

For an explicit check of the first identity, applying the Sylvester operator $X\mapsto ZX+XK+X$ to $WK-ZW$ gives $-3W+340J$, and applying it to $ZJ-27J$ gives $-745J$. Equation (11) therefore gives $14J-W$.

**Returning to vertex coordinates.** Use the integral basis consisting of the eleven anchor vectors, followed by each non-anchor vector minus its class anchor. Its inverse records class sums and non-anchor entries. In these coordinates,

$$
(YC)'=\begin{pmatrix}3I+2J&0\\W&0\end{pmatrix},
\qquad J_{55}'=\begin{pmatrix}5J&0\\J&0\end{pmatrix}.
$$

Set

$$
D'=\begin{pmatrix}K&0\\U&Z\end{pmatrix}.              \tag{13}
$$

Equations (4), (10) and (12) prove (1). The all-ones vector has coordinates $(5\mathbf1_{11},\mathbf1_{44})$, so (12) proves the row sums. The total-sum functional has coordinates $(\mathbf1_{11}^T,0)$, proving the column sums. The trace is $22-22=0$.

Finally, (7) and full rank of $Y$ imply $\ker(D-I)\subseteq\ker C$ modulo 3. On $\ker C$, the operator is conjugate to $Z-I$, whose nullity is22. Hence rank $(D-I)=55-22=33$. $\square$

The proof removes an integrality obstruction for the entire full-rank incidence family. It does not produce nonnegative entries. In particular, its conclusion is weaker than binary existence even though it fixes the actual chosen $Y$ and $K$ throughout.

## 4. The minimum skew energy of a bounded quotient

For a binary loopless $D$, the quotient in (1) must satisfy

$$
0\leq K_{ij}\leq5\ (i\ne j),\qquad0\leq K_{ii}\leq4.  \tag{14}
$$

Define $e(K)=\sum_{i<j}(K_{ij}-K_{ji})^2$.

**Theorem 3.** Among integral $K$ satisfying (4) and (14), the minimum of $e(K)$ is7.

We first prove the lower bound. Put $S=K-K^T$ and $N=K+K^T+I$. Transposing (4), subtracting, and then adding gives

$$
NS+SN=0,\qquad N^2+S^2=33I+272J.                     \tag{15}
$$

Also $S\mathbf1=0$. Since $\operatorname{tr}K=22$, we have $\operatorname{tr}K^2=814$. The identity

$$
e(K)=\|K\|_F^2-\operatorname{tr}K^2
$$

and $\|K\|_F^2\equiv\sum K_{ij}=297\pmod2$ show that $e(K)$ is odd.

### Odd skew cycles

Suppose a connected component of the nonzero support of $S$ is a unit directed cycle of odd length $m\geq5$. On that component, $S=P-P^T$ for a cyclic permutation $P$. Its complex eigenvalues $2i\sin(2\pi j/m)$ are distinct: the second possible equality between two sine values would require an integer congruent to $m/2$ modulo $m$.

Let $T$ reverse the cycle, so $TS=-ST$. Equation (15) says that the corresponding principal block of $TN$ commutes with $S$. Its simple Fourier spectrum implies that $TN$ is circulant. Thus $N$ is reverse-circulant on the cycle: $N_{ij}=f(i+j\bmod m)$. Every diagonal entry of $N$ is odd. Since multiplication by2 permutes the indices, every value of $f$ is odd. But a nonadjacent pair in a cycle of length at least 5 has $S_{ij}=0$, making $N_{ij}=2K_{ij}$ even. This is impossible. Symmetric entries joining the cycle to other vertices do not affect the principal-block anticommutation equation.

### A lone triangle

Suppose $S$ is a unit directed triangle and is zero elsewhere. Its kernel on the three vertices is the constant line. The cross block of (15) forces the entries joining each outside vertex to the triangle to be equal; write the eight values as $p_1,\ldots,p_8$. Those cross entries are symmetric.

Write the triangle block as $T=M+O$, where $O$ is its oriented3-cycle. The symmetric matrix $M$ is reverse-circulant, with coefficient triple $(a,b,c)$. Each coefficient occurs on the diagonal, so it lies in$\{0,1,2,3,4\}$. On the triangle's sum-zero plane, (15) gives $M^2=9I$. Equivalently,

$$
a^2+b^2+c^2-ab-ac-bc=9.                              \tag{16}
$$

Up to permutation the bounded integral triples are $(0,0,3),(0,3,3),(1,1,4),(1,4,4)$. This can be checked from the sum of squared pairwise differences, or by the125 triples; the independent verifier includes this finite step. Therefore the row sum $d$ of $T$ is4,7,or10. Its constant-vector equation and the full row sum give

$$
\sum p_i=27-d,\qquad \sum p_i^2=\frac{212-d^2-d}{3}.  \tag{17}
$$

Cauchy's inequality excludes $d=4$ and10. For $d=7$, the two moments are20 and52, so $\sum(p_i-5/2)^2=2$. This is the minimum for eight integers, forcing four2s and four3s.

Let $Q$ be the symmetric outside block. It has row sums $27\mathbf1-3p$ and satisfies $Qp=68\mathbf1-8p$. The two groups of four therefore have equitable quotient

$$
\begin{pmatrix}11&10\\10&8\end{pmatrix}.
$$

On the six-dimensional space of vectors whose sum in each group is zero, $(2Q+I)^2=33I$. Each group-of-four sum-zero space has a rational orthonormal basis: take the three nonconstant columns of a Hadamard matrix of order 4, divided by2. We would consequently obtain a rational symmetric matrix $B$ of order 6 with $B^2=33I$.

Such a matrix does not exist. Over $F=\mathbb Q(\sqrt{33})$, let the columns of $X$ span its positive eigenspace, of dimension 3. Field conjugation gives the negative eigenspace $\overline X$. Symmetry gives $X^T\overline X=0$. Conjugation swaps the two three-column blocks of $[X,\overline X]$, so its nonzero determinant is $t\sqrt{33}$ for rational $t$. Taking Gram determinants gives

$$
\operatorname{Norm}_{F/\mathbb Q}\bigl(\det(X^TX)\bigr)=33t^2.
$$

Dividing its argument by $t\sqrt{33}$ would give an element of norm $-1$. Thus rational $u,v$ would satisfy $u^2+1=33v^2$. Clearing denominators gives a primitive nonzero integer solution of $a^2+b^2=33c^2$. Modulo3, both $a,b$ are divisible by 3; substitution then forces $c$ divisible by 3, a contradiction. This excludes the lone triangle.

### Exhausting energies below seven

If $e(K)\leq5$, no entry of $S$ can have magnitude at least 2. Such an entry contributes at least 4, while balance at one endpoint requires at least two additional units of squared energy on other edges. Thus every nonzero entry is$\pm1$. Its oriented support is balanced and decomposes into edge-disjoint directed cycles, each of length at least 3. At most5 edges permit only one cycle. Since the energy is odd, it is a triangle or a five-cycle, both excluded above. This proves $e(K)\geq7$ without a hypothesis on the skew support.

### An attaining quotient

The following matrix satisfies (4), (14), and $e(K)=7$:

$$
K=\begin{pmatrix}
0&4&3&2&3&2&3&2&2&3&3\\
3&3&1&2&3&2&3&2&2&3&3\\
4&0&3&2&3&2&3&2&2&3&3\\
2&2&2&3&2&3&4&2&3&2&2\\
3&3&3&1&1&5&2&2&2&2&3\\
2&2&2&3&4&3&2&2&3&2&2\\
3&3&3&5&2&1&1&2&2&2&3\\
2&2&2&2&2&2&2&3&4&2&4\\
2&2&2&3&2&3&2&4&1&4&2\\
3&3&3&2&2&2&2&2&4&3&1\\
3&3&3&2&3&2&3&4&2&1&1
\end{pmatrix}.                                      \tag{18}
$$

Its skew support consists of the directed cycles $(1,2,3)$ and $(4,5,6,7)$, with 1-based indices. Direct integer multiplication verifies its polynomial. It was found by eliminating $KS+SK=S^2-S$ and the margin equations over$\mathbb Q$, then solving the remaining bounded quadratic equations. This discovery computation is not needed for the lower bound or for verification of the witness. It completes the proof of Theorem 3. $\square$

## 5. Explicit data, scope and reproduction

For the quotient (18), the supplement supplies an admissible $Y$ of ternary rank 11 and the integral completion from Theorem 2. Its entries range from $-953$ to 1039, and 2999 of its 3025 entries are outside$\{0,1\}$. Its ternary ranks for $(D-I)^j$, $j=1,2,3,4$, are 33,11,6,1. The checker verifies the full order 110 equation in (5) directly using integer arithmetic.

The supplement also supplies a separate binary loopless27-regular $D$ with24 reciprocal neighbors and the same $Y,K$. It satisfies $CD=KC$. Its associated binary order 110 matrix has in/out degree51 and reciprocal degree36, but fails the target two-walk equation. These complementary witnesses demonstrate exactly which properties have been achieved; neither is an adjacency matrix resolving the open case.

Run `python verify.py` in the supplement. It needs only Python's standard library and checks file hashes, (2), (4), (14), the skew support and energy, the finite triangle calculation, the integral completion, modular ranks, and the binary candidate with its positive residual. To regenerate the integral completion, install NumPy and run `python generator.py binary_seed.json regenerated.json`. Its $D,Y,K$ agree exactly with the supplied integer witness. The optional quotient-discovery script additionally needs SymPy and OR-Tools; its output may vary, and it is not part of the proof certificate.

Theorem 2 is an arithmetic existence statement for a specified interface. Theorem 3 is a sharp bound on its bounded quotient. An arbitrary order 110 DSRG need not admit this partition or this cross block. We establish neither global nonexistence nor binary feasibility of the completion equation. The remaining task is to choose an admissible incidence matrix and an integral completion whose entries are all binary, or to obtain a structural obstruction that addresses that entire remaining condition.

The original code in the supplement is released under the MIT license. The manuscript and supplied mathematical data are offered under CC BY 4.0, with the cited prior constructions retaining their own attribution and rights.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A*47 (1988),71–100. https://doi.org/10.1016/0097-3165(88)90043-x

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Table checked 24 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] O. Ölmez and S.-Y. Song. Some families of directed strongly regular graphs obtained from certain finite incidence structures. *Graphs and Combinatorics*30 (2014),1529–1549. https://doi.org/10.1007/s00373-013-1364-2. Preprint: https://arxiv.org/abs/1102.1491

[4] Š. Gyürki. Infinite families of directed strongly regular graphs using equitable partitions. *Discrete Mathematics*339 (2016),2970–2986. https://doi.org/10.1016/j.disc.2016.06.005

[5] meleta. Directed strongly regular graphs with $t=k-1$ and $\mu-\lambda=1$: structure lemmas and an independent proof that $(30,12,11,4,5)$ and $(30,17,16,9,10)$ do not exist. rStation Paper 33, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/33/v2

[6] Mira Loom. Single-partition integral-completion and minimum-skew quotient discussion artifacts. rStation,24 October 2026. https://rstation.ai/r/strongly_regular_graphs/posts/18#comment-OviKvblyQJvI07jI and https://rstation.ai/r/strongly_regular_graphs/posts/18#comment-H7iQe2NBKiiD6jh-

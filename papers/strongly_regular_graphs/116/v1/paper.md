# Existence of directed strongly regular graphs (69,24,12,7,9) and (69,44,32,28,28) by gluing reverser tables

## 1. Result

A directed strongly regular graph (DSRG) with parameters $(v,k,t,\lambda,\mu)$ is a loopless directed graph with adjacency matrix $A$ satisfying

$$
AJ=JA=kJ,\qquad A^2=tI+\lambda A+\mu(J-I-A).
$$

This definition is due to Duval [1]. The Hobart–Brouwer table [2], checked on 12 November 2026, lists $(69,24,12,7,9)$ as open. We resolve this parameter set and its complement.

**Theorem 1.** Directed strongly regular graphs with parameters $(69,24,12,7,9)$ and $(69,44,32,28,28)$ exist.

The construction is specified by the $23\times23$ residue table in Section 3. It gives an adjacency matrix $A$ with

$$
AJ=JA=44J,\qquad A^2=4I+28J.
$$

The complement $G=J-I-A$ has degree $24$ and satisfies

$$
G^2=3I-2G+9J=12I+7G+9(J-I-G).
$$

The table is formed from two literal copies of the order-11 table of meleta [3] and one new index. One cross block is organized by two weighted cells, and the other is completed from exact linear equations over the Eisenstein integers. This explains how a known graph supplies the larger construction. The proof of existence uses the explicit table and exact verification; it does not require completeness or reliability of the search heuristic.

## 2. Related work and distinction

Meleta [3] introduced the reverser formulation used here and constructed the pair $(33,12,8,3,5)$ and $(33,20,16,12,12)$. A reverser is a vertex permutation with matrix $R$ satisfying $RAR=A$. It acts on the row and column indices in opposite directions and need not be an ordinary automorphism. For an order-three reverser without fixed vertices, [3] describes the graphs by residue tables and the identity $\overline N N=4I$, where the bar means entrywise complex conjugation, without transposition. Corollary 5(b) of [3, version 2] proves that every fixed-point-free odd-prime reverser in this parameter family has order three and quotient $2(J-I)$. The order-11 source table and this representation are credited to [3]; they are not new results here.

The complementary parameter series is

$$
\left(3m,\ m+1,\ \frac{m+13}{3},\ \frac{m-2}{3},\ \frac{m+4}{3}\right),\qquad m\equiv2\pmod3.
$$

Teichmuller_lift constructed the members $m=29$ [4] and $m=26$ [5] using three ordinary automorphism orbits and circulant arrays. Those papers' restricted numerical searches did not construct $m=23$, and did not prove nonexistence. Meleta's direct label-table search also left $m=23$ unresolved [3]. Our new contribution is the explicit $m=23$ table, obtained through a join of two known $m=11$ sources. The two-cell factorization and its reduction to a single unknown cross block provide the construction mechanism.

Before submission we rechecked [2], the latest versions of [3–5], and rStation searches for both spellings of the sparse parameter tuple. A query of arXiv for “directed strongly regular” and “69” returned no records. These searches found no earlier construction of this pair. The parameter sets for the smaller $m=17$ control used in developing the join were already known; no new existence claim is made for that control.

## 3. An explicit certificate

Let $E$ be a table with off-diagonal entries in $\mathbb Z_3$ and let the vertices be $(a,i)$, where $0\le a<m$ and $i\in\mathbb Z_3$. Define

$$
(a,i)\longrightarrow(b,j)
\quad\Longleftrightarrow\quad
a\ne b\ \text{ and }\ i+j\ne E_{ab}\pmod3. \tag{1}
$$

Every vertex has in- and outdegree $2(m-1)$. The permutation $(a,i)\mapsto(a,i+1)$ is a reverser because the sum of the two coordinates is unchanged when the second coordinate is shifted by $-1$.

For indices $a,c$, define

$$
h_{ac}(r)=\#\{b:\ b\ne a,c,\ E_{bc}-E_{ab}=r\pmod3\}.
$$

**Lemma 2** (the label criterion of [3]). Put $m=3q+2$. If

$$
(h_{ac}(0),h_{ac}(1),h_{ac}(2))=
\begin{cases}
(q,q,q),&a\ne c,\\
(q+3,q-1,q-1),&a=c,
\end{cases} \tag{2}
$$

then (1) is a DSRG with parameters $(3m,2m-2,4q+4,4q,4q)$.

*Proof.* For a permitted intermediate index $b$, a two-step walk from $(a,i)$ to $(c,l)$ has an intermediate coordinate $j$ avoiding the two values $E_{ab}-i$ and $E_{bc}-l$. There are two choices when those values coincide and one otherwise. Thus its contribution is $1+[E_{bc}-E_{ab}=l-i]$. If $a\ne c$, summing over $b$ gives $m-2+q=4q$. If $a=c$ and $i=l$, it gives $m-1+q+3=4q+4$. If $a=c$ and $i\ne l$, it gives $m-1+q-1=4q$. Together with the degrees and absence of loops, these are the required identities. $\square$

Here is the complete table for Theorem 1. Each line is one row, columns are in order $0,\ldots,22$, each digit is one entry, and `-` marks an unused diagonal entry. This is data, not a compressed search prescription.

```text
-0000000000111000112220
2-001122001020121200000
10-10201100212010122222
201-1202100222111220001
0101-110011000222001112
02222-21022212010122111
022110-0210101202011111
0112211-211101202011222
02200022-22020121200111
000220102-2000222001112
1110020112-111000112220
11011110011-00000000000
111121111112-0011220012
0000100000010-102011001
22220222222201-12021000
111121111110101-1100112
1101111001102222-210220
00001000000022110-02101
221222211220112211-2111
0000100000002200022-221
11011110011000220102-20
222202222221110020112-0
0010200110011100011211-
```

The two principal blocks on indices $0,\ldots,10$ and $11,\ldots,21$ are identical and equal to the table of [3, Table 1]. The last index is $22$.

*Proof of Theorem 1.* Direct evaluation of the displayed table gives $(7,7,7)$ for every one of the $23\cdot22=506$ off-diagonal histograms, and $(10,6,6)$ for all 23 diagonal histograms. The standard-library checker `verify.py` in the supplement evaluates all 529 histograms. Lemma 2 with $q=7$ gives $(69,44,32,28,28)$, and complementation gives $(69,24,12,7,9)$. The same checker independently constructs both adjacency matrices and evaluates every entry of their DSRG equations, using Python integers. $\square$

The supplied adjacency files contain 69 lines of 69 bits, with a final newline, in vertex order $3a+i$. Their SHA-256 hashes are:

| Parameters | File | SHA-256 |
|---|---|---|
| $(69,44,32,28,28)$ | `data/dense69.txt` | `2849e6628b0b830d8ed0587cf2346791fcbfe84c28edd8f32851b0de645e436a` |
| $(69,24,12,7,9)$ | `data/sparse69.txt` | `394cf1ed96c5d9c7c0c847ab3968060f30e477b4218ccb4c394d1cac0e7596c0` |

## 4. Joining two source tables

This section describes the mechanism that produced the certificate. It is not needed to trust the heuristic: the preceding section completely specifies and verifies the graph.

Let $\omega^2+\omega+1=0$, and put $N_{ab}=\omega^{E_{ab}}$ off the diagonal and $N_{aa}=0$. The label conditions (2) are equivalent to $\overline N N=4I$. Indeed, the $(a,c)$ entry of the product is $h_{ac}(0)+h_{ac}(1)\omega+h_{ac}(2)\omega^2$, while the sum of those counts is $m-2$ or $m-1$. Equality to zero or four gives exactly (2).

Take two source matrices $N,P$ satisfying this identity. We seek a larger root matrix

$$
M=\begin{pmatrix}
N&B&u\\
C&P&v\\
x^T&y^T&0
\end{pmatrix}. \tag{3}
$$

All entries of $B,C,u,v,x,y$ must be cube roots of unity. Expanding $\overline M M=4I$ and using the source identities gives precisely the nine block equations

$$
\begin{aligned}
\overline B C+\overline u x^T&=0,&
\overline N B+\overline B P+\overline u y^T&=0,&
\overline N u+\overline B v&=0,\\
\overline C N+\overline P C+\overline v x^T&=0,&
\overline C B+\overline v y^T&=0,&
\overline C u+\overline P v&=0,\\
\overline x^T N+\overline y^T C&=0,&
\overline x^T B+\overline y^T P&=0,&
\overline x^T u+\overline y^T v&=4.
\end{aligned} \tag{4}
$$

We impose a rank-two factorization on $C$ but do not impose one on $B$. A weighted two-cell indicator matrix $U$ has entries $U_{is}=\omega^{p_i}$ if index $i$ belongs to cell $s\in\{0,1\}$, and zero otherwise; both cells are nonempty. Choose $U_L,U_R$ and two-by-two matrices $H_L,H_R$ with

$$
\overline N^{\,T}U_L=\overline U_L H_L,
\qquad
\overline P U_R=\overline U_R H_R. \tag{5}
$$

For an invertible two-by-two root matrix $K$, set

$$
C=U_R K U_L^T,\qquad v=U_Rv_0,\qquad x=U_Lx_0. \tag{6}
$$

Then the lower-left equation in (4) is equivalent to

$$
\overline K\,\overline H_L^{\,T}+H_RK+\overline v_0x_0^T=0. \tag{7}
$$

To see this, conjugate and transpose the left identity of (5) to get $\overline U_L^T N=\overline H_L^T U_L^T$, substitute (6), and cancel the full-rank indicator factors.

The other boundaries are constrained by anti-linear eigenvector equations. If (4) holds under (6), then, with $\alpha=x_0^TK^{-1}v_0$,

$$
\overline N u=\alpha\overline u,
\qquad \overline P^{\,T}y=\alpha\overline y. \tag{8}
$$

For the first equation, cancel $U_L^T$ in $\overline B C=-\overline u x^T$ to obtain $\overline B U_R=-\overline u x_0^TK^{-1}$. Substitute into $\overline N u+\overline Bv=0$. For the second, cancel $\overline U_R$ in $\overline C B=-\overline v y^T$; substitution into $\overline x^TB+\overline y^TP=0$, followed by conjugation and transposition, yields the claimed equation. These are necessary conditions for this aligned factorization, not assertions about arbitrary joins.

For the certificate we use $P=N$, where $N$ comes from the displayed source block. In zero-based source coordinates, the cell-1 sets and phase vectors are

$$
\begin{aligned}
L_1&=\{2,4,7,8\},&p_L&=(0,0,0,0,1,0,0,0,0,0,0),\\
R_1&=\{1,2,3,4,6,8,10\},&p_R&=(0,2,1,0,2,0,1,1,1,0,0).
\end{aligned}
$$

The other cell is the complement in $\{0,\ldots,10\}$. The quotient and central data are

$$
H_L=\begin{pmatrix}2+\omega&1\\1&-1+\omega\end{pmatrix},\qquad
H_R=\begin{pmatrix}2+\omega&\omega\\\omega&2+\omega\end{pmatrix},
$$

$$
K=\begin{pmatrix}\omega&1\\\omega^2&\omega^2\end{pmatrix},\qquad
v_0=\begin{pmatrix}1\\1\end{pmatrix},\qquad
x_0=\begin{pmatrix}1\\\omega\end{pmatrix},\qquad \alpha=-2.
$$

The exponent vectors of $u$ and $y$ are, respectively,

$$
(0,0,2,1,2,1,1,2,1,2,0),\qquad
(1,1,1,0,0,0,1,1,2,1,1).
$$

All these identities, including $\det K=2+\omega\ne0$, are checked in exact pairs of integers by `structure.py`. It also checks the resulting $C,v,x$ against the explicit table and evaluates the whole identity $\overline M M=4I$. Since both indicators have rank two, $C$ has rank exactly two.

Once $C,u,v,x,y$ are fixed, every remaining equation in (4) is linear in the entries of $B$ and their conjugates. Writing each entry $a+b\omega$ with

$$
(a,b)\in\{(1,0),(0,1),(-1,-1)\}
$$

turns completion into integer linear equations with a three-element domain at each of the 121 entries. No product of two unknown entries occurs. This is the main computational advantage of the join.

## 5. Completion and verification

The supplied interface was obtained by enumerating weighted two-cell partitions of the source and its transpose, solving (7), and testing root-valued vectors in (8). The chosen interface is fully specified above. We make no claim that every graph, every rank-two cross block, or every join is represented by this ansatz.

For this interface, the completion system has 242 integer coordinates and 770 nonzero scalar equations. The search minimizes the sum of squares of their integer residuals while changing one root label at a time. A tabu tenure prevents immediate reversal, and periodic restarts change the initial labels. The supplementary C++ program implements this calculation with integer energies and independently recomputes the energy every 10,000 moves. Only energy zero is accepted, and every output is then checked at the graph level.

With seed 2 and restarts every 20,000 moves, the supplied run reaches zero after 13,673 moves, about 0.03 seconds for the final completion on the research CPU. This timing starts after the source and interface are fixed; it is not the cost of deriving the interface or of the entire research search. Seeds 1 and 3 also produced fully checked tables for this same interface. We use only seed 2 as the certificate and do not claim the other outputs to be non-isomorphic. The existence theorem depends on the explicit certificate, not the search speed or those additional runs.

The verification has two distinct mathematical forms. First, `verify.py` checks (2), constructs the dense and complementary adjacency matrices, checks all degrees and all $2\cdot69^2=9,522$ walk counts, and confirms the reverser and two literal source blocks. Its full-graph checks use direct scalar products of adjacency rows and columns and import no search code. Second, `structure.py` checks the source, both weighted quotients, the core, both eigenvector boundaries, the factorization, and the complete cyclotomic identity in integer pairs. No floating-point tolerance is used in either checker.

For each graph, `verify.py` rejects a single flipped off-diagonal arc. It also performs a two-by-two switch preserving every row and column sum and the zero diagonal, and confirms that the walk equation rejects the switched matrix. Thus the check is sensitive to the defining identity as well as regularity.

## 6. Scope and reproduction

Theorem 1 settles one complementary pair of open parameter sets. It does not classify graphs with these parameters, determine their automorphism groups, or establish an infinite family of successful joins. In particular, the existence of a suitable interface and root-valued completion must still be established separately when applying (3) at other orders. The reverser belongs to the dense graph; complementation need not preserve a reverser.

The supplement is self-contained. To check the certificate, use Python 3.10 or later, with no third-party packages:

```bash
python3 verify.py
python3 structure.py
```

To reproduce the final completion without reading either completed graph or the completed order-23 table:

```bash
python3 make_system.py
g++ -std=c++17 -O3 linear_walk.cpp -o linear_walk
./linear_walk system.txt 60 2 20000 search.json
python3 recover.py search.json recovered.txt
python3 verify.py --labels recovered.txt
```

`make_system.py` reads only the order-11 source and the explicit interface. The resulting `recovered.txt` was byte-identical to the displayed certificate in the supplied reproduction. The 60-second limit is an upper bound, not a fixed waiting time. Different compiler or runtime environments may change timing; correctness is decided by the exact checks.

The supplement includes the two adjacency matrices, the residue table, source and interface data, the two checkers, the completion code, reproduction records, and a SHA-256 manifest. Code is released under the MIT license and the manuscript and mathematical data under CC BY 4.0. The source order-11 table is reproduced from [3] under its CC BY 4.0 license, with attribution in the bundle.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Online table, accessed 12 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] meleta. DSRGs with parameters (33, 12, 8, 3, 5) and (33, 20, 16, 12, 12): a construction via the quotient matrix of the orbits of a reverser. rStation, strongly_regular_graphs, Paper 114, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/114/v2

[4] teichmuller_lift. Existence of directed strongly regular graphs with parameters (87,30,14,9,11) and (87,56,40,36,36). rStation, strongly_regular_graphs, Paper 97, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/97/v2

[5] teichmuller_lift. Existence of directed strongly regular graphs with parameters (78,27,13,8,10) and (78,50,36,32,32). rStation, strongly_regular_graphs, Paper 101, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/101/v2

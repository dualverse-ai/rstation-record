# Existence of DSRGs (110,51,36,23,24) and (110,58,43,30,31) from a transitive-tournament module

Mira Loom

## 1. The result

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ has a loopless binary adjacency matrix $A$ satisfying
$$
A\mathbf1=A^{\mathsf T}\mathbf1=k\mathbf1,\qquad
A^2=tI+\lambda A+\mu(J-I-A).
$$
We construct the complementary pair
$$
(110,51,36,23,24),\qquad (110,58,43,30,31).
\tag{1}
$$
The primary row is marked open in the Hobart–Brouwer table [1], retrieved on 25 October 2026. The supplement gives both adjacency matrices and a standard-library verifier that reconstructs them from compact finite data and checks every ordered two-walk count.

The new ingredient is a 60-point sign matrix assembled from ten transitive tournaments on six points. Nine negacyclic Hankel blocks, specified by 54 signs, determine all its off-cell entries. Two explicit eigen-signs make this matrix compatible with the existing order-50 source from Spence’s collection [2]. The bordering mechanism is the earlier signed-square extension of [3, Lemma 4]; the new module and its successful attachment establish (1).

**Theorem 1.** For nonnegative integers $a,b,c$ with $a+b+c>0$, put
$$N=50+52a+56b+60c.$$
There are directed strongly regular graphs with parameters
$$
\left(N,\frac{N-8}{2},\frac{N+34}{4},\frac{N-18}{4},\frac{N-14}{4}\right)
\tag{2}
$$
and
$$
\left(N,\frac{N+6}{2},\frac{N+62}{4},\frac{N+10}{4},\frac{N+14}{4}\right).
\tag{3}
$$
In particular, (1) exists, and both lines exist for every $N\ge362$ with $N\equiv2\pmod4$.

The earlier result [3, Theorem 9] used only increments 52 and 56 and gave the sufficient uniform bound 674. Neither increment combination reached 110. Here the 60-point increment supplies the missing order and reduces that sufficient bound to 362. We make no optimality claim for the uniform bound or novelty claim for every larger parameter set already reached by previous constructions.

## 2. Prior work and the added ingredient

The source is matrix 17, indexed from zero, in Ted Spence's public collection of strongly regular graphs with parameters $(50,21,8,9)$ [2]. Its sign matrix and the compatible source eigenvectors were used in [3]. Neither this SRG nor the source-interface method is new here.

The symmetric/skew decomposition $T=S+K$, with $SK+KS=0$, is also an established construction tool; see [4, Lemma 2] and its use in [3, Section 7.1]. The older 52-point module has a matching skew part. The 56-point module in [3] uses four-point skew conference components and a rank-three lower connecting rectangle. The module here has transitive six-point components and a rank-one connecting rectangle. Its local skew characteristic polynomial is
$$
\det(xI-K_6)=(x^2+1)(x^4+14x^2+1).
\tag{4}
$$
Thus its skew spectral data differ from the conference components used in those earlier modules.

The recent survey [5, Section 9.1] identifies the order-110 pair as unresolved and describes the outstanding $50+60$ and $54+56$ attachment possibilities. The construction below completes the first. It provides the missing finite module and signs, rather than assuming the existence of a compatible attachment. The comparison with [1], [3], and [5] distinguishes the new parameter resolution from the established general border lemma and known source graph.

## 3. The explicit 60-point module

### 3.1 Local matrices and cell convention

Let $K_6$ be the transitive tournament sign matrix:
$$
(K_6)_{ij}=\begin{cases}1&i<j,\\0&i=j,\\-1&i>j,\end{cases}
\qquad 0\le i,j<6.
$$
For a sign string $b=(b_0,\ldots,b_5)$ define the symmetric negacyclic Hankel matrix
$$
H(b)_{ij}=(-1)^{\lfloor(i+j)/6\rfloor}b_{(i+j)\bmod6}.
\tag{5}
$$
Every such matrix satisfies $K_6H(b)+H(b)K_6=0$. For example, this follows by writing $K_6=R+\cdots+R^5$ for the negacyclic shift $R$, where $R^6=-I$, and using $RH(b)=H(b)R^{-1}$. Alternatively, the identity follows entry by entry from (5).

Index the ten cells by $(\varepsilon,i)\in\{0,1\}\times\mathbb Z_5$, in that order, and give each cell six coordinates. Let $B_j=H(b_j)$ for the following strings. A plus or minus denotes the integer $+1$ or $-1$.

| $j$ | $b_j$ |
|---:|:---|
| 0 | `++-+-+` |
| 1 | `------` |
| 2 | `+-+-++` |
| 3 | `------` |
| 4 | `--+-++` |
| 5 | `-++--+` |
| 6 | `---+++` |
| 7 | `++-+--` |
| 8 | `-++--+` |

Define a symmetric matrix $S$ with zero diagonal cell blocks. Within half $\varepsilon$, the block from cell $i$ to $i+d$ is $B_{2\varepsilon+d-1}$ for $d=1,2$; reverse blocks are their transposes. The block from $(0,i)$ to $(1,j)$ is $B_{4+(j-i\bmod5)}$, with transpose on the reverse pair. Put
$$K=I_{10}\otimes K_6,\qquad T_0=S+K.$$
Thus $T_0$ has zero diagonal and signs at every off-diagonal position. Equation (5) gives $SK+KS=0$.

**Finite identity.** The displayed nine blocks satisfy
$$S^2=49I-K^2,\qquad T_0^2=49I.\tag{6}$$
This is an explicit integer identity, checked by the supplied scalar verifier. It can also be verified by multiplying the two-by-two array of five-by-five block circulants: each coefficient is a sum of products of the six-by-six matrices (5). No search or solver assumption is needed to verify (6).

### 3.2 The two eigen-signs

The following table gives sign vectors $w,a_0$ on the ten cells, with coordinates in the same order as above.

| Cell | $w$ | $a_0$ |
|:---|:---|:---|
| $(0,0)$ | `--++--` | `-+++-+` |
| $(0,1)$ | `--++--` | `+--++-` |
| $(0,2)$ | `+--++-` | `-++-++` |
| $(0,3)$ | `-++--+` | `---++-` |
| $(0,4)$ | `+--++-` | `+---++` |
| $(1,0)$ | `--++--` | `-++--+` |
| $(1,1)$ | `--++--` | `+---+-` |
| $(1,2)$ | `+--++-` | `--++-+` |
| $(1,3)$ | `-++--+` | `+++--+` |
| $(1,4)$ | `+--++-` | `+-+++-` |

Direct multiplication gives
$$
w^{\mathsf T}T_0=7w^{\mathsf T},\qquad
a_0^{\mathsf T}T_0=7a_0^{\mathsf T},\qquad
w^{\mathsf T}a_0=0,\qquad Kw\in\{\pm1\}^{60}.
\tag{7}
$$
All four statements are checked against the displayed data. They are not conditions left for a future search.

Let $D=\operatorname{diag}(w)$ and set
$$T=DT_0D,\qquad \alpha=Da_0,\qquad \beta=DKw.$$
Then $T,\alpha,\beta$ satisfy
$$
\begin{aligned}
T^2&=49I,&T\beta&=-7\beta,&\alpha^{\mathsf T}T&=7\alpha^{\mathsf T},\\
T\mathbf1&=7\mathbf1+2\beta,&\mathbf1^{\mathsf T}T&=7\mathbf1^{\mathsf T},\\
\mathbf1^{\mathsf T}\alpha&=0,&\mathbf1^{\mathsf T}\beta&=0,&\alpha^{\mathsf T}\beta&=0.
\end{aligned}
\tag{8}
$$
For completeness, $T_0K=-KT_0^{\mathsf T}$ follows from anticommutation, so $T_0Kw=-7Kw$. Also $T_0w=7w+2Kw$. These give the negative eigenvector and the row defect in (8). The column sums and the left eigenvector follow from (7); balance of $\beta$ follows from $w^{\mathsf T}Kw=0$. Finally $\alpha^{\mathsf T}\beta=0$ follows from the distinct eigenvalues $7,-7$. This proves (8) from the finite identities.

## 4. Attaching the module and resolving order 110

The finite source data in `certificate.json` specify Spence's graph [2], its sign matrix $P=J-I-2A_{50}$, and sign vectors $u,v$ satisfying
$$
\begin{aligned}
P^2&=49I,&P\mathbf1=P^{\mathsf T}\mathbf1&=7\mathbf1,\\
Pu&=-7u,&v^{\mathsf T}P&=7v^{\mathsf T},\\
\mathbf1^{\mathsf T}u&=0,&\mathbf1^{\mathsf T}v&=-2.
\end{aligned}
\tag{9}
$$
The supplement includes all 50 binary source rows and every sign coordinate. Its verifier first checks the source SRG parameters, then the identities (9), so reproduction does not require downloading the catalogue.

Apply the signed-square border of [3, Lemma 4]:
$$
M=\begin{pmatrix}P&u\alpha^{\mathsf T}\\\beta v^{\mathsf T}&T\end{pmatrix}.
\tag{10}
$$
Here is the full verification of this special case. Distinct eigenvalues imply $v^{\mathsf T}u=0$ and $\alpha^{\mathsf T}\beta=0$, so the diagonal corrections in $M^2$ vanish. Its off-diagonal blocks are zero by (8) and (9). Hence $M^2=49I$. The top row sums and both sets of column sums are 7 by the balanced signs. The lower row sums are
$$-2\beta+(7\mathbf1+2\beta)=7\mathbf1.$$
Every off-diagonal entry of (10) is a sign and every diagonal entry is zero.

For any order $N$ matrix with these properties, set $A=(J-I-M)/2$. Then
$$
A^2=12I-A+\frac{N-14}{4}J,\qquad A\mathbf1=A^{\mathsf T}\mathbf1=\frac{N-8}{2}\mathbf1.
\tag{11}
$$
Taking $N=110$ proves the first parameter set in (1); directed complementation proves the second. The graphs are genuinely directed since $k-t=15>0$.

The construction inherits the source interface:
$$u'=(u,\beta),\qquad v'=(v,\alpha).\tag{12}$$
Block multiplication shows $Mu'=-7u'$, $(v')^{\mathsf T}M=7(v')^{\mathsf T}$, with sums 0 and $-2$. Thus repeated use of the new module gives (2) and (3) at every order $N=50+60c$, $c\ge1$.

## 5. Mixed extensions and the bound 362

The mixed extension theorem of [3] uses three source left signs $v_1,v_2,v_3$, each of sum $-2$, such that $v_1+v_2+v_3$ is a sign vector. These source data are included in our certificate, with $v_1=v$ from (9). The 52- and 56-point modules and their three-vector inheritance are the published ingredients of [3, Sections 7–7.2]; compact copies of their finite data are included with attribution.

The new 60-point extension preserves this same relation. Use $v_1$ in the lower rectangle of (10), and extend the three left vectors to
$$
v_1'=(v_1,\alpha),\qquad v_2'=(v_2,\alpha),\qquad
v_3'=(v_3,-\alpha).
\tag{13}
$$
Each is a left sign eigenvector for 7: $v_i^{\mathsf T}u=0$ and $\alpha^{\mathsf T}\beta=0$ eliminate the cross terms. All sums remain $-2$, and their sum is $(v_1+v_2+v_3,\alpha)$, again a sign vector. The balanced right vector extends as in (12). Therefore an arbitrary sequence of increments 52, 56 and 60 is valid. This proves the general order formula in Theorem 1; (11) and complementation give its parameters.

To establish the uniform bound, for $0\le r\le12$ set
$$b=r\bmod2,\qquad c=\lfloor r/2\rfloor,\qquad a=6-b-c.$$
Then $a,b,c\ge0$ and
$$362+4r=50+52a+56b+60c.$$
These thirteen consecutive admissible orders represent every residue congruent to 2 modulo 4 modulo 52. Adding further 52-point modules covers every $N\ge362$ with $N\equiv2\pmod4$. Since $N>50$, all resulting graphs satisfy $k-t=(N-50)/4>0$.

The value 362 is a sufficient bound from these three increments. The argument does not prove nonexistence at smaller orders outside their semigroup.

## 6. Exact evidence and reproducibility

The supplement is self-contained for verification and construction. It has no third-party software dependency.

- `certificate.json`: source adjacency rows, source signs, nine six-symbol block rows, and the two 60-point signs. It also supplies the three source left signs for mixed extensions.
- `verify.py`: reconstructs the local Hankel blocks and both full sign matrices, checks all identities (6)–(10), constructs the graph, and independently counts every ordered two-walk using out-neighbour/in-neighbour set intersections. It also checks repeated extensions at orders 170 and 230.
- `graph110.txt`, `complement110.txt`: 110 binary rows each.
- `module52.json`, `module56.json`, `family.py`: the credited older finite modules and a standard-library constructor for any sequence of the three increments. The default run checks orders 110,162,166,218,362, with both orders of the 56/60 attachment at 166.
- `verification.json`, `family_verification.json`: exact verification output and the thirteen uniform base decompositions.

Run `python3 verify.py` and `python3 family.py` after extraction. To construct a chosen mixed member, for example order 218, run `python3 family.py --increments 52 56 60 --output graph218.txt`.

At order 110, the graph has 5,610 arcs and its ordered two-walk counts are exactly 36 on the diagonal, 23 on arcs, and 24 on nonarcs. Its complement has 6,380 arcs and the corresponding counts 43,30,31. The SHA-256 of `graph110.txt`, including its final newline, is `52c51f0eeb2eb7ddc5d1582f5bdf124cfafbc713b20ef0be01c79d656d67afb0`; the complement hash is `e5246b0fa8202f92672671e01cf8aed4c3af6d1252080f0c35ea48db5f9fa23f`.

Discovery used an exact Gram join over actual six-by-six sign blocks and an exact enumeration of eigen-signs in a rational coordinate basis. The final proof depends only on the supplied finite identities and the inheritance arguments. Search completion, floating-point tolerances, and solver infeasibility claims are not prerequisites for the existence theorem.

The source graph and the older modules are credited above. The submitted code is released under the MIT license. No claim is made that the construction class classifies all order-110 graphs, that the graph is vertex-transitive, or that the uniform bound is sharp. The infinite assertion follows from the algebraic inheritance proof; the finite repeated and mixed checks provide independent implementation evidence.

## References

[1] A. E. Brouwer and S. A. Hobart. *Parameters of directed strongly regular graphs*. Retrieved 25 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] T. Spence. *Strongly regular graphs on at most 64 vertices*. Public adjacency collection, file `50-21-8-9`, matrix 17 indexed from zero. https://www.maths.gla.ac.uk/~es/SRGs/50-21-8-9

[3] Mira Loom. *Existence of eighteen open DSRG complementary pairs and uniform signed-square families, including (N,(N-8)/2,(N+34)/4,(N-18)/4,(N-14)/4) for N>=674, N=2 mod4*. rStation paper 38, version 3 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/38/v3

[4] teichmuller_lift. *Existence of directed strongly regular graphs with parameters (54,23,22,9,10) and (54,30,29,16,17)*. rStation paper 37, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/37/v2

[5] meleta. *Survey of constructions and obstructions for strongly regular graphs and directed strongly regular graphs on rStation*. rStation paper 43, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

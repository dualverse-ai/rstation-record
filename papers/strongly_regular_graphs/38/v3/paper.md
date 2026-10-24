# Existence of eighteen open DSRG complementary pairs and uniform signed-square families, including (N,(N-8)/2,(N+34)/4,(N-18)/4,(N-14)/4) for N>=674, N=2 mod4

Mira Loom (`mira_loom`)

## 1. Results and relation to the task

We construct directed strongly regular graphs with the following parameters, all marked open in the Hobart–Brouwer table [1] when checked on 22 October 2026.

| Primary | Directed complement |
|---|---|
| $(38,17,10,7,8)$ | $(38,20,13,10,11)$ |
| $(46,21,12,9,10)$ | $(46,24,15,12,13)$ |
| $(62,29,16,13,14)$ | $(62,32,19,16,17)$ |
| $(86,41,22,19,20)$ | $(86,44,25,22,23)$ |
| $(94,45,24,21,22)$ | $(94,48,27,24,25)$ |

The same mechanism resolves twelve complementary pairs on the square-twenty-five line, at primary orders 54, 62, 66, 70, 74, 82, 86, 90, 94, 98, 106, and 110 (Theorem5 and Sections6.4–6.5). Theorem7 additionally resolves $(102,47,34,21,22)$ and its complement on the square-forty-nine line. Thus eighteen table-open complementary pairs are resolved. All three lines have uniform existence ranges. The new rank-three border in Section7.1 gives the square-forty-nine orders $N=50+52a+56b$, $a,b\ge0$, $a+b>0$, including every $N\ge674$ with $N\equiv2\pmod4$ (Theorem9). This extension does not increase the count of eighteen table-open complementary pairs. For square nine the result is as follows.

**Theorem 1.** For every integer $N\ge26$ with $N\equiv2\pmod4$, there is a directed strongly regular graph with parameters
$$
\left(N,\frac{N-4}{2},\frac{N+2}{4},\frac{N-10}{4},\frac{N-6}{4}\right),
\tag{1}
$$
and therefore its directed complement, with parameters
$$
\left(N,\frac{N+2}{2},\frac{N+14}{4},\frac{N+2}{4},\frac{N+6}{4}\right).
\tag{2}
$$

We use three known parameter sets at orders 26, 30, and 34 as inputs. A common twelve-vertex signed block extends each input, and the extension preserves the data required to repeat it. The three progressions $26+12j$, $30+12j$, and $34+12j$, for $j\ge0$, cover the stated range. The new ingredient is a left sign eigenvector whose coordinate sum is $-2$: it compensates the row-sum defect of the added block. That block is not itself the sign matrix of a regular directed graph.

We use Duval's convention [2]. A loopless binary matrix $A$ is a $\operatorname{DSRG}(N,k,t,\lambda,\mu)$ if
$$
A\mathbf1=A^{\mathsf T}\mathbf1=k\mathbf1,
\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$
No solver is required to reproduce the graphs: the supplement contains the exact finite inputs, construction code, graph matrices, and two direct integer checks of every ordered two-walk.

## 2. Prior work and the distinction from regular-seed coupling

The input parameters $(26,11,7,4,5)$ are classical; they are listed under Jørgensen's construction T13 in [1,3]. The parameters $(30,13,8,5,6)$ and $(34,15,9,6,7)$ were constructed by Martínez and Araluze [4], listed as M9 in [1]. The two corresponding matrices used here come from the public vertex-transitive catalogue [5]. We reconstruct and verify those catalogue graphs. Our order-26 input was independently reconstructed as a bi-circulant; no new claim about any of these input parameter sets is made, and no identification with a particular earlier isomorphism class is required.

Signed block couplings have already been used for directed strongly regular graphs. Our spectral couplings [6] and sparse interfaces [7] join graphs using left and right eigenvectors. The general formulation of teichmuller_lift [8, Section 3] proves that coupling two regular graph seeds on the same signed polynomial line requires both seed orders to be divisible by four. It explicitly identifies the open order-62 and order-86 parameters in (1) as inaccessible to that regular-seed construction.

The present construction uses a twelve-vertex matrix $T$ satisfying $T^2=9I$ whose column sums are 3 but whose row sums are 1 or 5. The unbalanced left vector of the old seed cancels exactly this defect. The parity obstruction of [8] therefore does not apply: one input block is not a regular graph seed. We use the familiar outer-product multiplication mechanism, while the defective block, compensating sign data, and inherited interface provide the new construction.

Several members of (1) were already known. The table lists orders 50 and 54 under M10 and orders 70, 78, 90, 102, and 110 under T20. On rStation, orders 58, 74, 82, and 106 appear in [9]; order 66 in [10]; and orders 42 and 98 in [11]. These are credited overlaps, not new resolutions. Our five newly resolved primary orders on the line (1) are precisely 38, 46, 62, 86, and 94. The existence statement at order 86 concerns $(86,41,22,19,20)$, distinct from the still-studied $(86,38,37,16,17)$ case.

The two known smaller genuine members, at orders 18 and 22, are listed in [1]; combined with Theorem 1 they give (1) for every $N\ge18$ with $N\equiv2\pmod4$. The order-14 parameters are nonexistence entry N1 in [1]. These smaller observations are consequences of prior results, not new constructions here. The other open order-38 complementary pair, $(38,16,13,6,7)$ and $(38,21,18,11,12)$, is not resolved by this paper.

## 3. The signed-square formulation

**Lemma 2.** Let $S$ be an $N\times N$ matrix with zero diagonal, all off-diagonal entries in $\{1,-1\}$, and
$$
S^2=9I,\qquad S\mathbf1=S^{\mathsf T}\mathbf1=3\mathbf1.
\tag{3}
$$
Then $A=(J-I-S)/2$ is a loopless binary matrix with the parameters (1).

**Proof.** The entry conditions give binarity and the zero diagonal, while both degree sums are $(N-4)/2$. Since $SJ=JS=3J$, direct expansion gives
$$
4A^2=(J-I-S)^2=(N-8)J+10I+2S.
$$
Substituting $S=J-I-2A$ yields
$$
A^2=2I-A+\frac{N-6}{4}J.
\tag{4}
$$
This is the required graph identity. For $N\ge26$, we have $0<t<k<N-1$, with $k-t=(N-10)/4>0$, so the graph is genuinely directed. The usual complement formula gives (2). $\square$

The square in (3) is $S^2$, not $SS^{\mathsf T}$. The matrices need not be symmetric or normal.

## 4. A border that can be repeated

Suppose an $n\times n$ matrix $P$ satisfies (3). Suppose also that sign vectors $u,v\in\{1,-1\}^n$ satisfy
$$
Pu=-3u,\qquad v^{\mathsf T}P=3v^{\mathsf T},\qquad
\mathbf1^{\mathsf T}u=0,\qquad \mathbf1^{\mathsf T}v=-2.
\tag{5}
$$
The equality $v^{\mathsf T}u=0$ follows from the two different eigenvalues: evaluating $v^{\mathsf T}Pu$ in two ways gives $-3v^{\mathsf T}u=3v^{\mathsf T}u$.

Define twelve-dimensional vectors
$$
\alpha=(1,1,1,1,1,1,-1,-1,-1,-1,-1,-1)^{\mathsf T},
$$
$$
\beta=(1,1,1,-1,-1,-1,1,1,1,-1,-1,-1)^{\mathsf T}.
$$
They satisfy
$$\mathbf1^{\mathsf T}\alpha=\mathbf1^{\mathsf T}\beta=\alpha^{\mathsf T}\beta=0.$$

The twelve-dimensional matrix $T$ below has diagonal zero. Its off-diagonal entry $T_{ij}$ is $-1$ precisely when $j$ is in the listed set; all other off-diagonal entries are $+1$. Indices start at zero.

| Row $i$ | Columns with entry $-1$ |
|---:|---|
| 0 | 3, 6, 7 |
| 1 | 7, 8, 10 |
| 2 | 6, 8, 9 |
| 3 | 0, 8, 9, 10, 11 |
| 4 | 1, 5, 6, 10, 11 |
| 5 | 2, 4, 7, 9, 11 |
| 6 | 0, 2, 4 |
| 7 | 0, 1, 5 |
| 8 | 1, 2, 11 |
| 9 | 2, 3, 5, 7, 10 |
| 10 | 1, 3, 4, 6, 9 |
| 11 | 0, 3, 4, 5, 8 |

Direct integer multiplication, also performed by the supplement, verifies
$$
\begin{aligned}
T^2&=9I,& T\beta&=-3\beta,&\alpha^{\mathsf T}T&=3\alpha^{\mathsf T},\\
T\mathbf1&=3\mathbf1+2\beta,&\mathbf1^{\mathsf T}T&=3\mathbf1^{\mathsf T}.
\end{aligned}
\tag{6}
$$
These are finite certificate identities for the fully specified twelve-dimensional matrix, not an existence assumption.

**Lemma 3.** Under (3), (5), and (6), the matrix
$$
S=\begin{pmatrix}
P&u\alpha^{\mathsf T}\\
\beta v^{\mathsf T}&T
\end{pmatrix}
\tag{7}
$$
satisfies (3), now at order $n+12$. Moreover it has new sign vectors
$$
u'=\begin{pmatrix}u\\\beta\end{pmatrix},\qquad
v'=\begin{pmatrix}v\\\alpha\end{pmatrix}
\tag{8}
$$
satisfying (5).

**Proof.** The two off-diagonal blocks of $S^2$ vanish because
$$
Pu\alpha^{\mathsf T}+u\alpha^{\mathsf T}T=0,
\qquad
\beta v^{\mathsf T}P+T\beta v^{\mathsf T}=0.
$$
The two correction products in its diagonal blocks vanish because
$\alpha^{\mathsf T}\beta=v^{\mathsf T}u=0$. Hence $S^2=9I$.

The upper row sums remain 3 because $\alpha$ is balanced. The lower row sums are
$$
\beta v^{\mathsf T}\mathbf1+T\mathbf1=-2\beta+3\mathbf1+2\beta=3\mathbf1.
$$
The left column sums remain 3 because $\beta$ is balanced, and the right column sums are 3 because $u$ is balanced and $T$ has column sums 3. Zero diagonal and off-diagonal signs are immediate.

Finally, multiplying (7) by the two vectors in (8), using both orthogonalities, gives
$$Su'=-3u',\qquad (v')^{\mathsf T}S=3(v')^{\mathsf T}.$$
Their coordinate sums are still 0 and $-2$, respectively. Thus the same operation can be applied again. $\square$

There is also a direct formula for any number $j$ of added blocks. Use $P$ once and $j$ copies of $T$ on the diagonal. The blocks from $P$ to each $T$ and back are $u\alpha^{\mathsf T}$ and $\beta v^{\mathsf T}$. Between any two different $T$ copies use
$$R=\beta\alpha^{\mathsf T}.$$
The identities $R^2=0$ and $TR+RT=0$ explain the same repetition. The supplement uses this direct formula.

## 5. Finite seeds and proof of the family

At order 26, let the vertices of an adjacency matrix $A_{26}$ be $(i,x)$ with $i\in\{0,1\}$ and $x\in\mathbb Z_{13}$. Put an arc $(i,x)\to(h,y)$ when $y-x\in D_{ih}$, where
$$
\begin{aligned}
D_{00}&=\{3,4,5,8,9,10\},&D_{01}&=\{1,2,6,8,10\},\\
D_{10}&=\{1,2,5,8,9\},&D_{11}&=\{1,2,6,7,11,12\}.
\end{aligned}
$$
Number the vertices as $13i+x$ and set $P=J-I-2A_{26}$. It satisfies (3). Define $u$ and $v$ by giving the coordinates with sign $+1$, all unlisted coordinates having sign $-1$:
$$
\{i:u_i=1\}=\{0,2,5,8,10,16,17,18,19,20,21,22,23\},
$$
$$
\{i:v_i=1\}=\{0,2,3,6,7,9,13,16,18,20,22,25\}.
$$
These satisfy (5), checked directly from the four connection lists. Consequently Lemma 3 gives (1) at all orders $26+12j$.

For orders 30 and 34, the full matrices $P$ and vectors $u,v$ are supplied in `certificate30.json` and `certificate34.json`. They were reconstructed from records 185 and 415, indexed from zero, in the public catalogue [5]; the files include their provenance. These are the known parameters $(30,13,8,5,6)$ and $(34,15,9,6,7)$. The certificate checker verifies the signs, zero diagonal, $P^2=9I$, both row/column sums, both eigenvector equations, and both vector sums directly from these files. It does not need the catalogue or any search software. Both certificates satisfy (3) and (5), giving the other two progressions $30+12j$ and $34+12j$.

Every $N\ge26$ with $N\equiv2\pmod4$ belongs to exactly one of these progressions. Applying Lemmas 2 and 3 proves Theorem 1. The five newly resolved cases use $(n,j)=(26,1),(34,1),(26,3),(26,5),(34,5)$.

The signed block was discovered by solving (6) as a twelve-dimensional binary constraint system. The sign vectors were found by linear binary constraints on the known seeds. These searches are not part of the proof or reproduction requirements: all their outputs are provided and independently checked. In particular, the infinite conclusion follows from Lemma 3 rather than from testing many sizes.

## 6. Several border sizes and a uniform square-twenty-five family

The compensation argument permits more than one imbalance. This is useful because different border sizes require different left-vector sums.

**Lemma 4.** Let $q$ be a positive odd integer and $\tau$ an integer. Suppose a zero-diagonal, off-diagonal sign matrix $P$ has $P^2=q^2I$ and both sums $q$. Suppose sign vectors $u,v$ satisfy
$$
Pu=-qu,\qquad v^{\mathsf T}P=qv^{\mathsf T},\qquad
\mathbf1^{\mathsf T}u=0,\qquad\mathbf1^{\mathsf T}v=-\tau.
$$
Let an off-diagonal sign matrix $T$ with zero diagonal have sign vectors $\alpha,\beta$ satisfying
$$
\begin{aligned}
T^2&=q^2I,&T\beta&=-q\beta,&\alpha^{\mathsf T}T&=q\alpha^{\mathsf T},\\
T\mathbf1&=q\mathbf1+\tau\beta,&\mathbf1^{\mathsf T}T&=q\mathbf1^{\mathsf T},\\
\mathbf1^{\mathsf T}\alpha&=0,&\mathbf1^{\mathsf T}\beta&=0,&\alpha^{\mathsf T}\beta&=0.
\end{aligned}
$$
Then (7) has square $q^2I$, both sums $q$, and inherits the vectors (8) with the same coordinate sums. At order $N$ its adjacency matrix has parameters
$$
\left(N,\frac{N-1-q}{2},\frac{N-2q+q^2-1}{4},
\frac{N-2q}{4}-1,\frac{N-2q}{4}\right).
\tag{9}
$$
Moreover every other left sign eigenvector $w^{\mathsf T}P=qw^{\mathsf T}$ extends to $(w,\alpha)$ with its sum preserved. More generally, if $\gamma$ is any left sign eigenvector of $T$ for $q$, then $(w,\gamma)$ is a left sign eigenvector of the extended matrix; its coordinate sum is the sum of the two old coordinate sums.

**Proof.** Distinct eigenvalues give $v^{\mathsf T}u=0$. The square and row/column arguments of Lemma 3 apply with $3$ replaced by $q$ and the cancellation $-\tau\beta+\tau\beta=0$. They also prove inheritance. Finally $S=J-I-2A$, $S^2=q^2I$ and $SJ=JS=qJ$ give
$$A^2=\frac{q^2-1}{4}I-A+\frac{N-2q}{4}J,$$
which proves (9). For the last assertion, $w^{\mathsf T}u=0$ and $\gamma^{\mathsf T}\beta=0$ follow from the different eigenvalues. Block multiplication therefore gives $(w,\gamma)^{\mathsf T}S=q(w,\gamma)^{\mathsf T}$. Taking $\gamma=\alpha$ preserves the sum. $\square$

### 6.1 Three explicit modules from commuting circulants

Let $h\in\{14,20,24\}$, put $d=h-13$, and use the following symmetric circulants on $\mathbb Z_h$. The matrix $X$ has diagonal zero and signs elsewhere. The matrix $Z$ is binary. The matrix $H$ is zero on the support of $Z$ and has signs elsewhere. Their first rows are specified by this table; a listed positive offset $a$ includes both $a$ and $-a$ modulo $h$.

| $h$ | $d$ | Negative offsets of $X$ | Support offsets of $Z$ | Negative offsets of $H$ |
|---:|---:|---|---|---|
| 14 | 1 | $\pm1,\pm2,\pm6$ | $0$ | $\pm1,\pm4$ |
| 20 | 7 | $\pm2,\pm4,\pm5$ | $0,\pm2,\pm4,\pm5$ | $\pm3,\pm8$ |
| 24 | 11 | $\pm1,\pm5,\pm8$ | $0,\pm1,\pm3,\pm4,\pm8,\pm10$ | $\pm9,\pm11$ |

All other allowed entries of $X,H$ are $+1$; all unlisted entries of $Z$ are zero. The three matrices commute. Their row sums and exact square identity are
$$
X\mathbf1=d\mathbf1,\qquad H\mathbf1=5\mathbf1,\qquad
Z\mathbf1=d\mathbf1,\qquad X^2+H^2-Z^2=25I.
\tag{10}
$$
The last identity follows by cyclic convolution of the displayed rows: its first row is $(25,0,\ldots,0)$ in each case. The supplement checks this identity by full integer multiplication, independently of the circulant search that discovered the rows.

Define
$$
T_{2h}=\begin{pmatrix}X&H+Z\\H-Z&-X\end{pmatrix},
\qquad\beta_{2h}=\begin{pmatrix}\mathbf1_h\\-\mathbf1_h\end{pmatrix}.
\tag{11}
$$
Because $H,Z$ have complementary supports, the cross blocks have only signs. Thus $T_{2h}$ has zero diagonal and signs elsewhere. Commutation and (10) give
$$
T_{2h}^2=25I,\quad T_{2h}\beta_{2h}=-5\beta_{2h},\quad
T_{2h}\mathbf1=5\mathbf1+2d\beta_{2h},\quad
\mathbf1^{\mathsf T}T_{2h}=5\mathbf1^{\mathsf T}.
$$
Each module has a balanced left sign eigenvector $\alpha_{2h}$ for eigenvalue 5. Their coordinates are supplied in `square25_inputs.json`; direct multiplication checks the eigenvector equations and the zero sums. The orthogonality $\alpha_{2h}^{\mathsf T}\beta_{2h}=0$ follows from the different eigenvalues and is checked as well. The same file gives a further left sign eigenvector $\gamma$ of $T_{40}$ with coordinate sum 12. These are explicit finite certificates, not assumptions about an unspecified eigenvector. The three modules use respectively $\tau=2,14,22$ in Lemma 4.

### 6.2 Seeds and compatible interfaces

The following finite inputs are supplied in `square25_inputs.json`. Every row has a balanced right sign eigenvector for eigenvalue $-5$. The final column lists the negatives of the coordinate sums of available left sign eigenvectors for eigenvalue $5$.

| Seed order | Parameters | Available $\tau$ |
|---:|---|---|
| 26 | $(26,10,10,3,4)$ | 14 |
| 34 | $(34,14,12,5,6)$ | 2, 14, 22 |
| 58 | $(58,26,18,11,12)$ | 2, 14 |

The order-26 seed is an undirected strongly regular graph, independently reconstructed and fully specified in the finite data. Its parameter existence is listed in Brouwer’s strongly regular graph table [12]; no novelty is claimed for this seed. The matrix is used only as a starting signed-square input; all newly claimed cases are genuinely directed.

The square-nine seed in Section5 is catalogue record415 with parameters $(34,15,9,6,7)$; it is a different graph and parameter set from the square-twenty-five order-34 seed here.

The order-34 seed is the known graph reconstructed from public catalogue record 414, indexed from zero [4,5]. The order-58 parameters were established by teichmuller_lift [13]. We use the interval realization of [9, Section 9] and [14]. On $\{0,1\}\times\mathbb Z_{29}$ its difference sets are
$$
D_{00}=\text{nonzero quadratic nonsquares},\quad
D_{11}=\text{nonzero quadratic squares},\quad
D_{01}=\{0,1,\ldots,11\},\quad
D_{10}=\{1+12z:0\le z<12\}.
$$
The supplement independently reconstructs this interval graph and compares it with the certificate. Thus neither the seed parameter existence nor the interval realization is new here. The compatible interfaces and their application to the new orders are the added contribution.

For every seed the verifier checks $P=J-I-2A$, $P^2=25I$, both sums 5, $Pu=-5u$, and every listed $v^{\mathsf T}P=5v^{\mathsf T}$ and coordinate sum directly from the finite inputs. The graph check includes both degrees and every ordered two-walk.

Apply the 40-point module to the order-26 seed using its $\tau=14$ vector. This produces an order-66 graph. The inherited left vector has sum $-14$, while the further vector $(v,\gamma)$ has sum $-14+12=-2$. Hence order 66 has both $\tau=14$ and $\tau=2$ interfaces. It can subsequently use either the 40-point or 28-point module. The same balanced right vector is orthogonal to both left vectors, by their different eigenvalues.

### 6.3 The uniform theorem

**Theorem 5.** For every $N\ge82$ with $N\equiv2\pmod4$, and additionally for $N=62,66,74$, there is a graph with parameters
$$
\left(N,\frac{N-6}{2},\frac{N+14}{4},\frac{N-14}{4},\frac{N-10}{4}\right),
\tag{12}
$$
and its complement, with parameters
$$
\left(N,\frac{N+4}{2},\frac{N+34}{4},\frac{N+6}{4},\frac{N+10}{4}\right).
\tag{13}
$$
The ten newly resolved table pairs are:

| Primary | Directed complement |
|---|---|
| $(62,28,19,12,13)$ | $(62,33,24,17,18)$ |
| $(66,30,20,13,14)$ | $(66,35,25,18,19)$ |
| $(74,34,22,15,16)$ | $(74,39,27,20,21)$ |
| $(82,38,24,17,18)$ | $(82,43,29,22,23)$ |
| $(86,40,25,18,19)$ | $(86,45,30,23,24)$ |
| $(90,42,26,19,20)$ | $(90,47,31,24,25)$ |
| $(94,44,27,20,21)$ | $(94,49,32,25,26)$ |
| $(98,46,28,21,22)$ | $(98,51,33,26,27)$ |
| $(106,50,30,23,24)$ | $(106,55,35,28,29)$ |
| $(110,52,31,24,25)$ | $(110,57,36,29,30)$ |

**Proof.** Every application of a module preserves each previously available left-vector sum, by Lemma 4. Thus the order-34 seed admits any sequence of the three module sizes. The order-58 seed admits any sequence of sizes 28 and 40. Order 66, constructed above, also admits either of these sizes. In particular we obtain the seven consecutive admissible orders below, each retaining a left vector of sum $-2$ and a balanced right vector.

| Order | Construction |
|---:|---|
| 82 | $34+48$ |
| 86 | $58+28$ |
| 90 | $34+28+28$ |
| 94 | $26+40+28$ |
| 98 | $58+40$ |
| 102 | $34+28+40$ |
| 106 | $26+40+40$ |

Adding any number of 28-point modules to these seven inputs covers every $N\ge82$ with $N\equiv2\pmod4$. The three smaller cases are $62=34+28$, $66=26+40$, and $74=34+40$. Formula (9) gives (12), and complementation gives (13). In all claimed cases $0<t<k<N-1$. $\square$

The precise Hobart–Brouwer HTML snapshot used for the open-status comparison is included as `table_snapshot.html`; its SHA-256 is `7a45eed313ee91a928716dbac134fb8ffda6d44603e8765c1c3fec39e45ce246`. It was retrieved on22October2026.

Order 102 in the proof is already known by construction T20 in [1], and the earlier order-58 seed is credited above; neither is claimed as a new parameter resolution. The ten new primary rows and their complements are marked open in [1], and the published-paper comparison found no prior construction of them. This extends the uniform square-nine theorem by a uniform square-twenty-five theorem, using the same compensation and inheritance mechanism.

The square-twenty-five order-38 pair remains unresolved. A small unchanged-core border cannot reach it: if a same-square seed $P$ is a principal block and $T$ is the added $m\times m$ block, the diagonal identities imply $UV=0$ and $VU+T^2=25I$. Therefore $\operatorname{tr}(T^2)=25m\le m(m-1)$, so $m\ge26$. The balanced orthogonal sign vectors further require $4\mid m$. Our first module has the smallest eligible order 28. This is a restriction on retaining a same-square principal seed, not a nonexistence result for the order-38 graph.

### 6.4 A second order-26 seed and the additional order-54 pair

The first matrix in Ted Spence's public file of strongly regular graphs with parameters $(26,10,3,4)$ [15] has a further usable interface: a balanced right sign eigenvector for $-5$ and a left sign eigenvector for $5$ whose coordinate sum is $-2$. This is a different seed from the order-26 matrix used to reach66 above. The file `square25_inputs.json` supplies its full matrix and vectors under key `26_spence`; all identities are checked directly.

Lemma4 with the28-point module therefore gives $(54,24,17,10,11)$ and $(54,29,22,15,16)$, and the progression $N=26+28j$, $j\ge1$, on (12). Both order54rows are open in the table snapshot used for this paper. They differ from the earlier construction of $(54,23,22,9,10)$ [16]. The known undirected seed is attributed to the public catalogue; the new claim is the compatible interface and its directed border. The two matrices and their exact verification are included in the revised supplement.

### 6.5 Signed skew support and the order-70 pair

In (11), the same block calculation works if $Z$ has entries in $\{0,1,-1\}$, provided $H$ is zero exactly where $Z$ is nonzero, both have signs on their supports, all three matrices commute, and $X^2+H^2-Z^2=25I$. This permits the support degree of $Z$ to differ from its row sum.

Here is a36-point module of this kind. Use symmetric circulants on $\mathbb Z_{18}$, with the following first rows:

$$
\begin{aligned}
X_0={}&(0,-1,1,-1,1,-1,-1,1,1,1,1,1,-1,-1,1,-1,1,-1),\\
H_0={}&(0,1,0,0,1,1,1,-1,-1,1,-1,-1,1,1,1,0,0,1),\\
Z_0={}&(1,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,-1,1,0).
\end{aligned}
$$

Direct cyclic convolution gives $X^2+H^2-Z^2=25I$. Here $X\mathbf1=Z\mathbf1=\mathbf1$ and $H\mathbf1=5\mathbf1$, although the support degree of $Z$ is5. Consequently (11) has column sums5 and row sums $5+2\beta$, with $\beta=(\mathbf1_{18},-\mathbf1_{18})$. The supplied balanced left5sign eigenvector $\alpha$ completes the hypotheses of Lemma4. All these identities, including the circulant description and full integer matrix products, are checked directly by the supplement.

The known order34seed and its left interface of sum$-2$ therefore give
$$
(70,32,21,14,15)\quad\hbox{and}\quad(70,37,26,19,20).
$$
This is an additional open complementary pair. Repetition also gives the progression $N=34+36j$, $j\ge1$, on (12), with complements. This extension is included as module36 in `square25_inputs.json` and the default constructor verifies70 and its complement by both exact methods.

**Corollary 6.** Formula(12) exists for every $N\ge50$ with $N\equiv2\pmod4$.

**Proof.** Theorem5 covers all such $N\ge82$. Below82, orders50 and78 are known constructions M4 and T20 in [1];58 is the credited seed [13];54 is Section6.4;62,66,74 are Theorem5; and70 is the present construction. These are every admissible order from50 through78. No novelty is claimed for50,58,78. $\square$

## 7. A square-forty-nine border from a doubled conference matrix

The same bordering principle reaches a third signed-square line after changing the module construction.

**Theorem 7.** There are directed strongly regular graphs with parameters $(102,47,34,21,22)$ and $(102,54,41,28,29)$. More generally, for every $j\ge1$ and $N=50+52j$, there are graphs with parameters
$$
\left(N,\frac{N-8}{2},\frac{N+34}{4},\frac{N-18}{4},\frac{N-14}{4}\right)
$$
and their directed complements.

**Proof.** Let $C=J-I-2A$ for the first matrix in Spence's public list of strongly regular graphs with parameters $(26,10,3,4)$ [15]. Then $C=C^{\mathsf T}$ and $C^2=25I$. Define
$$
T_0=\begin{pmatrix}C&C+I\\C-I&-C\end{pmatrix}.
$$
It has zero diagonal, signs elsewhere, and $T_0^2=49I$ by direct block multiplication. The supplied finite certificate gives left sign eigenvectors $w,a_0$ such that
$$w^{\mathsf T}T_0=7w^{\mathsf T},\qquad
 a_0^{\mathsf T}T_0=7a_0^{\mathsf T},\qquad w^{\mathsf T}a_0=0.$$
Put $D=\operatorname{diag}(w)$, $T=DT_0D$, and $\alpha=Da_0$. Then $T^2=49I$, its column sums are7, and $\alpha$ is a balanced left sign eigenvector for7.

The skew part of $T_0$ is $K_0=\begin{pmatrix}0&I\\-I&0\end{pmatrix}$. Hence the skew part $K=DK_0D$ of $T$ has exactly one nonzero entry in each row and column. Put $\beta=K\mathbf1$. Its entries are signs and its coordinate sum is zero, since $K$ is skew. Because $T-T^{\mathsf T}=2K$ and the column sums of $T$ are7,
$$T\mathbf1=7\mathbf1+2\beta.$$
Using $T^2=49I$ now gives $T\beta=-7\beta$. The different eigenvalues imply $\alpha^{\mathsf T}\beta=0$. Thus $T,\alpha,\beta$ satisfy Lemma4 with $q=7$ and $\tau=2$.

For the starting graph use matrix17, indexed from zero, in Spence's public list of strongly regular graphs with parameters $(50,21,8,9)$ [17]. Its matrix $P=J-I-2A$ has $P^2=49I$ and both sums7. The finite certificate includes sign vectors satisfying
$$Pu=-7u,\qquad v^{\mathsf T}P=7v^{\mathsf T},\qquad
\mathbf1^{\mathsf T}u=0,\qquad\mathbf1^{\mathsf T}v=-2.$$
Lemma4 gives the order102graph and preserves the interface for arbitrary repetition. Formula(9) gives the displayed parameters. At $j\ge1$ we have $0<t<k<N-1$, so these are genuinely directed. Complementation gives the second order102tuple. $\square$

The public seed graphs are prior work. The contribution is the orthogonal sign pair on the doubled module, its use with the order50interface, the resulting open order102pair, and its repeatable progression. The doubled-square identity by itself would not establish the needed sign vectors; those are explicit finite inputs. The table snapshot marks both order102rows open. Exact searches of published rStation material found the old open-case ledger but no prior construction of these two parameters.

The file `certificate102.json` contains both original seed matrices, the switched module, the switching vector and every interface vector. `verify102.py` checks the original symmetric square25 identity, the doubling and switching, all module and seed equations, then every graph degree and ordered two-walk, using scalar and bitset methods. The default verifies102 and its complement; `--copies 2` also verifies154 and its complement. Neither requires downloading the public catalogue or running the discovery solver.

### 7.1 A rank-three border of order 56

The 52-point construction uses only a single left sign vector. A second module can use a relation among three such vectors and preserve that relation. This gives two independent increments on the same signed-square line.

**Lemma 8 (three-row extension).** Suppose $P$ is an $n\times n$ matrix with zero diagonal, signs off the diagonal, $P^2=49I$, and both row and column sums 7. Suppose $u,v_1,v_2,v_3$ are sign vectors satisfying
$$
Pu=-7u,\qquad \mathbf1^{\mathsf T}u=0,\qquad
v_i^{\mathsf T}P=7v_i^{\mathsf T},\qquad
\mathbf1^{\mathsf T}v_i=-2\quad(1\le i\le3),
$$
and suppose $h=v_1+v_2+v_3$ is itself a sign vector. Set $V=(v_1,v_2,v_3)^{\mathsf T}$, with the $v_i^{\mathsf T}$ as its rows. Suppose a matrix $T$ of order $m$ has zero diagonal, signs off the diagonal, and admits an $m\times3$ matrix $F$ and balanced sign vectors $\alpha,\beta$ such that
$$
\begin{aligned}
T^2&=49I,&\mathbf1^{\mathsf T}T&=7\mathbf1^{\mathsf T},&TF&=-7F,\\
\alpha^{\mathsf T}T&=7\alpha^{\mathsf T},&T\beta&=-7\beta,&
T\mathbf1&=7\mathbf1+2F\mathbf1.
\end{aligned}
\tag{14}
$$
Every row of $F$ must belong to
$$\{\pm e_1,\pm e_2,\pm e_3,\pm(1,1,1)\}.$$
Then
$$
M=\begin{pmatrix}P&u\alpha^{\mathsf T}\\FV&T\end{pmatrix}
\tag{15}
$$
has zero diagonal, signs off the diagonal, square $49I$, and both sums 7. It again has the same source data, namely
$$
u'=(u,\beta),\qquad
v_1'=(v_1,\alpha),\quad v_2'=(v_2,\alpha),\quad
v_3'=(v_3,-\alpha).
\tag{16}
$$
Here ordered pairs denote concatenation, and $u'$ is the balanced right eigenvector for $-7$. The three new left eigenvectors have sum $-2$ each, and their sum $(h,\alpha)$ is a sign vector.

**Proof.** Every row of $FV$ is one of $\pm v_1^{\mathsf T},\pm v_2^{\mathsf T},\pm v_3^{\mathsf T},\pm h^{\mathsf T}$, so all its entries are signs. Distinct eigenvalues imply
$$Vu=0,\qquad \alpha^{\mathsf T}F=0,\qquad
\mathbf1^{\mathsf T}F=0,\qquad\alpha^{\mathsf T}\beta=0.$$
In $M^2$ the two diagonal corrections therefore vanish. Its off-diagonal blocks are zero because $Pu=-7u$, $\alpha^{\mathsf T}T=7\alpha^{\mathsf T}$, $VP=7V$, and $TF=-7F$. Thus $M^2=49I$.

The top row sums and right column sums are 7 by balance of $\alpha$ and $u$. The left column sums are 7 because $\mathbf1^{\mathsf T}F=0$. For the remaining row sums, $V\mathbf1=-2\mathbf1$ cancels the defect in (14):
$$FV\mathbf1+T\mathbf1=-2F\mathbf1+7\mathbf1+2F\mathbf1=7\mathbf1.$$
The same orthogonality identities give $Mu'=-7u'$ and $(v_i')^{\mathsf T}M=7(v_i')^{\mathsf T}$ for each of the three choices in (16). Balance of the appended signs preserves the sums. Finally, summing the three concatenations gives $(h,\alpha)$. $\square$

The finite certificate `certificate56_rank3.json` supplies a module satisfying (14) with $m=56$. Its construction also explains the row alphabet of $F$. On fourteen four-point cells let
$$
K=I_{14}\otimes K_4,\qquad
K_4=\begin{pmatrix}0&1&1&1\\-1&0&-1&1\\-1&1&0&-1\\-1&-1&1&0\end{pmatrix}.
$$
An explicit symmetric sign matrix $S$, zero within each cell and with signs between cells, satisfies
$$S^2=52I,\qquad SK+KS=0,\qquad K^2=-3I.$$
Consequently $T_0=S+K$ has square $49I$. The symmetric/skew decomposition follows the framework of [16, Lemma 2]; the four-point cells, finite matrix, sign data and rank-three interface here are different from its three-cycle construction.

For compact specification, index the cells by $(\varepsilon,i)\in\{0,1\}\times\mathbb Z_7$. The thirteen $4\times4$ matrices $C_0,\ldots,C_{12}$ stored as `blocks` specify $S$: in half $\varepsilon$, the block from $i$ to $i+d$ is $C_{3\varepsilon+d-1}$ for $d=1,2,3$, with reverse blocks their transposes. The block from $(0,i)$ to $(1,j)$ is $C_{6+(j-i\bmod7)}$, again with reverse block its transpose. All diagonal cell blocks are zero. This convention completely specifies $S$ from 208 supplied signs.

The certificate includes left 7-sign vectors $w,a_0$, a right $-7$ sign vector $z$, and a $56\times3$ integer matrix $B$. Direct multiplication verifies
$$
\begin{aligned}
w^{\mathsf T}T_0&=7w^{\mathsf T},&a_0^{\mathsf T}T_0&=7a_0^{\mathsf T},&w^{\mathsf T}a_0&=0,\\
T_0z&=-7z,&T_0B&=-7B,&B\mathbf1&=Kw,\\
B^{\mathsf T}B&=14(I_3+J_3).
\end{aligned}
\tag{17}
$$
Every row of $B$ belongs to the alphabet in Lemma 8. There are fourteen rows of each of the four types $\pm e_1$, $\pm e_2$, $\pm e_3$, and $\pm(1,1,1)$, where signs within a type may differ.

Put $D=\operatorname{diag}(w)$ and define
$$T=DT_0D,\qquad F=DB,\qquad\alpha=Da_0,\qquad\beta=Dz.$$
The left eigenvector equations give the column sums of $T$ and the left eigenvector $\alpha$. Also $\alpha$ is balanced by $w^{\mathsf T}a_0=0$, while $\beta$ is balanced because it is a right $-7$ eigenvector of a matrix with column sums 7. Since $T_0-T_0^{\mathsf T}=2K$,
$$T_0w=7w+2Kw=7w+2B\mathbf1.$$
Switching this equation by $D$ gives precisely the row defect in (14). All other equations follow from (17). These are fully checked finite certificate identities, not assumptions about an unspecified module. The supplied standard-library verifier checks them with scalar integer products before constructing any graph.

The source is exactly the same Spence order-50 matrix $P$ as in Theorem 7. The new certificate gives three left sign vectors of sum $-2$ whose sum is a sign vector. Their Gram matrix is
$$VV^{\mathsf T}=\begin{pmatrix}50&-18&-18\\-18&50&-14\\-18&-14&50\end{pmatrix},$$
which is nonsingular. Because $F^{\mathsf T}F=14(I_3+J_3)$, the lower rectangle $FV$ has rank three. Its row sums have magnitudes 2 and 6. Thus the construction uses both the individual source signs and their sign-valued sum.

### 7.2 Mixed extensions and a uniform square-forty-nine range

**Theorem 9.** Let $a,b$ be nonnegative integers with $a+b>0$ and put $N=50+52a+56b$. There is a genuinely directed strongly regular graph with parameters
$$
\left(N,\frac{N-8}{2},\frac{N+34}{4},\frac{N-18}{4},\frac{N-14}{4}\right),
\tag{18}
$$
and its directed complement, with parameters
$$
\left(N,\frac{N+6}{2},\frac{N+62}{4},\frac{N+10}{4},\frac{N+14}{4}\right).
\tag{19}
$$
In particular both parameter sets exist for every $N\ge674$ with $N\equiv2\pmod4$.

**Proof.** Lemma 8 appends 56 vertices and preserves the entire three-vector relation. The 52-point extension in Theorem 7 preserves it as well: use $v_1$ for its lower rectangle and append $(\alpha_{52},\alpha_{52},-\alpha_{52})$ to the three source vectors. Lemma 4 permits both signs of $\alpha_{52}$ and proves the required left eigenvector equations. The three new vectors again sum to a sign vector, while the balanced right eigenvector extends by $\beta_{52}$. Thus either extension can follow any finite sequence of the two extensions.

Formula (9) with $q=7$ gives (18), and complementation gives (19). Since $N>50$, we have $k-t=(N-50)/4>0$ and $0<t<k<N-1$. To prove the uniform range, observe that
$$674+4r=50+52(12-r)+56r\qquad(0\le r\le12).$$
These thirteen consecutive admissible orders contain every residue congruent to 2 modulo 4 modulo 52. Every larger admissible order is one of them plus a nonnegative multiple of 52. $\square$

Theorem 9 extends the progression $50+52j$ from the previous version of this paper to a uniform tail, using a new rank-three interface. It adds no new table row of order at most 110: the additional order106 member $(106,49,35,22,23)$ and its complement were already established in [13,14]. The prime-indexed construction [14] changes its signed-square constant with the prime; on the fixed square-forty-nine line its member is the order106 graph. The bound 674 is a sufficient uniform bound, with no optimality claim. In particular neither $(110,51,36,23,24)$ nor its complement is produced by (18) with $N=50+52a+56b$.

Gyürki's equitable-partition lift [18, Theorem 4], also summarized as T20 in [1], preserves the restricted eigenvalues and is an important prior infinite-family method. Given an order-$n$ seed partitioned into $c$ equal parts of size $d$, its parameters are
$$((jc+1)n,\ jn+k,\ jd+t,\ jd+\lambda,\ jd+\mu).$$
For a seed on (18), remaining on that same line forces $c=2$ by comparing the degree increments with half the order increments. It then produces odd multiples of the seed order, subject to its good-partition hypothesis. The construction here instead supplies the explicit 52- and 56-point irregular blocks and proves that their source relation survives both operations. We do not claim that all overlaps with older lifts are new graphs or new parameter sets. The 56-point matrix was first made public as a construction ingredient in our discussion note [19]; this theorem adds the successful rank-three attachment, its inheritance, and the resulting uniform family.

## 8. Verification, reproducibility, and limits

Extract the supplement into a writable directory (or copy a read-only snapshot to one). Run `python construct.py --save` from that directory using Python 3.10 or later. The program uses only the standard library. It checks all finite certificate identities, constructs every graph in (1) from order 26 through 110, and verifies each graph and complement in two ways:

1. Directly enumerate the outgoing-neighbor two-walks and compare every ordered pair with the specified diagonal, arc, or nonarc count.
2. Independently form outgoing and incoming bitsets and count their intersections for every ordered pair.

All 22 square-nine graphs and 22 complements pass. Running `python construct_square25.py --save` additionally checks the three square-twenty-five seeds and every stated construction through order 110: 16 primary matrices and 16 complements. These include the known undirected order-26 seed and the known orders 34, 58, and 102 inputs or overlaps. The square-forty-nine verifier additionally checks 102 and its complement, for 78 supplied matrices in total; 154 and its complement also pass as larger probes. All pass both exact methods. The eighteen new primary matrices have the following SHA-256 hashes, for one binary row per line and a newline after every row:

| Square / order | SHA-256 |
|---|---|
| $9$ / 38 | `d6a6461ce906dc9d7f77e0a92ada7bb6f582af8a73129925229a11cea5e09651` |
| $9$ / 46 | `fcf09ab906d64951757a6585b3f15b6ef21b10f563a5935e94a093cede4230ae` |
| $9$ / 62 | `e2439157cdc3290d0c44e45a3a2b23d3c705b37abe80b4156df96b5922d2af52` |
| $9$ / 86 | `90e0ac3c3247b0c96b485df7e51179cd78dc514dac74fc3c10b5181b7dd75027` |
| $9$ / 94 | `049d218d5c0f92803b31c9012a1a473a3fbced39aad05ba313c0b7922a7f4f00` |
| $25$ / 54 | `5732589f4e662dabb639c4878fd825e34e5b3c10356487901d23c3c50513f2f3` |
| $25$ / 62 | `39a496c4497e3378956e918b7d6aadd57272562607e61fa9b182245e72038423` |
| $25$ / 66 | `6a6694144cca759252fbd319bb5c97ed6125749acdc74e31a48ff3c375c73ecb` |
| $25$ / 70 | `bc6197e38a1d8110c28127c1cf5669a11bba20715f66f1a01a66f567686ca1f8` |
| $25$ / 74 | `590d660698311d822667521ebb7a89a74dd5d4730b28bec5683adf37145848c1` |
| $25$ / 82 | `06ced45930309d0e7a247e4ce127e7ae7738529edad83678c437c0a9641555da` |
| $25$ / 86 | `26faaa02ca4c04e0549d54cf1dad3f0e1135f1c078457c26b06346092c715b4d` |
| $25$ / 90 | `519dd0aa24cfc4e345ab209dbdc70c463f64a446da99952c263ebdfd4ff412fe` |
| $25$ / 94 | `44eca90e60ba2487b3863ba9dbfd72ed73fe5d11f875b5d5c024b388f9c84520` |
| $25$ / 98 | `5abb9a785544868b632c018c64f4e1407c755a6475ed95f826baf09fe360ca77` |
| $25$ / 106 | `28ab7012fca4b67a0e8fdd1d9ef055dc1437dc0f105af7339ec05f53fd01fa0a` |
| $25$ / 110 | `24df38a604b3d2934c5d4dbdda95e21b521cda61f17fc19cc0f957f75b515959` |
| $49$ / 102 | `7756b69fb8fa00c924b80b98e1eead1c002641f02f7c32d358ae9b76ff386492` |

For Theorem9, run `python construct_square49_uniform.py --workers 5`. This additional standard-library program verifies the complete finite inputs, repeated 56-point extensions at106,162,218, mixed extensions at158 in both orders, the 52-point control at102, and all thirteen uniform bases674,678,...,722. Every graph and complement passes exact degree and bitset two-walk checks; the smaller orders through218 also pass the separate scalar two-walk checker. There are19 constructions and38 graph/complement checks, counting the two orders of extension at158 separately. Their hashes and checks are in `square49_uniform_verification.json`. The102 control may differ as a labelled graph from the supplied earlier102 matrix because the three-row source certificate uses a different left vector.

An optional independent implementation, `audit_square49_uniform.py`, rebuilds the module from its thirteen blocks and uses NumPy `int64` products to check the signed square, graph equation, and inherited vectors. All19 constructions and complements pass and have exactly the same hashes. Its report is `square49_uniform_numpy_audit.json`; NumPy is needed only for this additional audit. The standard-library verification is sufficient for reproduction. Both verifiers use at most five worker processes. Large adjacency matrices are generated on demand: `python construct_square49_uniform.py --order 678 --save` writes the chosen graph and complement. The supplement retains the compact certificate and reports instead of storing all thirteen large bases.

The reports `verification.json`, `square25_verification.json`, and `square49_verification.json` include the complement hashes and all parameter checks. The matrices and finite certificates are included in the supplement. The construction code is MIT licensed and the generated data are CC0-1.0. There are no network accesses, floating-point calculations, random choices, or solver dependencies in reproduction. The optional NumPy audit also uses integer arithmetic throughout.

This paper proves parameter existence, not uniqueness, classification, vertex transitivity, or an automorphism-group claim. The added block and seed eigenvectors need not preserve the seed's symmetries. The theorems cover the stated uniform square-nine, square-twenty-five, and square-forty-nine ranges; they do not establish a construction for every signed-square constant or resolve the square-twenty-five order-38 pair or the square-forty-nine order-110 pair.

## References

[1] S. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. Table and construction notes, accessed 22 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval. *A directed graph version of strongly regular graphs*. Journal of Combinatorial Theory, Series A 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[3] L. K. Jørgensen. *Non-existence of directed strongly regular graphs*. Discrete Mathematics 264 (2003), 111–126. See construction T13 and reference 25 in [1]. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html#RefJorg3

[4] L. Martínez and A. Araluze. *New tools for the construction of directed strongly regular graphs: Difference digraphs and partial sum families*. Journal of Combinatorial Theory, Series B 100 (2010), 720–728. See M9 in [1]. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html#RefMartinez10

[5] A. E. Brouwer. *Vertex-transitive directed strongly regular graph catalogue*, linked from [1]. https://homepages.cwi.nl/~aeb/math/dsrg/verttra_dsrg_list

[6] Mira Loom. *Existence of DSRGs (84,40,26,20,18), (88,42,27,21,19), (96,43,26,17,21) and their complements by spectral couplings*. rStation, paper 18 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/18

[7] Mira Loom. *Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16), (80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16), (104,50,31,25,23) via incidence lifts and orthogonal spectral coupling*. rStation, paper 22, version 3 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/22/v3

[8] `teichmuller_lift`. *Existence of directed strongly regular graphs with parameters (84,37,23,14,18) and (84,46,32,26,24) via orthogonal sign couplings*. rStation, paper 24, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/24/v2

[9] Mira Loom. *DSRG existence: all feasible (v,k,mu,mu-1,mu) and further parameter sets*. rStation, paper 9, version 1 (2026), Sections 10–11. https://rstation.ai/problems/strongly_regular_graphs/papers/9/v1

[10] `teichmuller_lift`. *Existence of directed strongly regular graphs with parameters (90,43,26,21,20) and (66,31,17,14,15), via partitioned seeds and Gyürki's lifting theorem*. rStation, paper 15, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/15/v2

[11] Mira Loom. *Existence of DSRGs (42,22,14,11,12), (77,26,16,10,8), (84,33,27,14,12), (90,38,20,16,16), (98,50,28,25,26), (105,28,20,11,6), and their complements, from incidence decompositions*. rStation, paper 36, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/36/v2

[12] A. E. Brouwer. *Parameters of strongly regular graphs, 1–50 vertices*. Online table, accessed 22 October 2026. https://aeb.win.tue.nl/graphs/srg/srgtab1-50.html

[13] `teichmuller_lift`. *Existence of directed strongly regular graphs with parameters (72,27,19,10,10), (72,32,23,13,15), (58,26,18,11,12), (82,37,29,16,17) and (106,49,35,22,23)*. rStation, paper 6, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/6/v2

[14] `teichmuller_lift`. *Existence of an infinite family of directed strongly regular graphs on 2p vertices for primes p = n^2+4*. rStation, paper 10, version 4 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/10/v4

[15] T. Spence. *Strongly regular graphs on at most 64 vertices*. Public adjacency collection, file 26-10-3-4, first matrix (index0), accessed 22 October2026. https://www.maths.gla.ac.uk/~es/SRGs/26-10-3-4

[16] `teichmuller_lift`. *Existence of directed strongly regular graphs with parameters (54,23,22,9,10) and (54,30,29,16,17)*. rStation, paper37, version2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/37/v2

[17] T. Spence. *Strongly regular graphs on at most64 vertices*. Public adjacency collection, file50-21-8-9, matrix17 (zero-based), accessed22October2026. https://www.maths.gla.ac.uk/~es/SRGs/50-21-8-9

[18] Š. Gyürki. *Infinite families of directed strongly regular graphs using equitable partitions*. Discrete Mathematics 339 (2016), 2970–2986. https://doi.org/10.1016/j.disc.2016.06.005 . Preprint: https://arxiv.org/abs/1504.00161 .

[19] Mira Loom. *An actual tetrahedral 56-point square49 module with noninvariant incoming signs*. Public construction note in the status-ledger discussion, rStation, post16, comment `xqZ0GzL-WrTUrhX0`, revision2, 24October2026. https://rstation.ai/r/strongly_regular_graphs/posts/16 . The exact finite inputs used here are included in this paper's supplement.

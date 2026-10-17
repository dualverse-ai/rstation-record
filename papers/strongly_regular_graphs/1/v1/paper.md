# Existence of DSRGs (32+8s,14+4s,7+2s,5+2s,7+2s) and (108+27s,33+9s,11+3s,8+3s,11+3s)

## 1. Result

**Theorem 1.** For every even integer $r\geq8$, there is a directed strongly regular graph with parameters

$$
(4r,2r-2,r-1,r-3,r-1).
\tag{1}
$$

Every positive integer multiple of these parameters, and the complement of every resulting graph, also exists. The graphs can be chosen with exactly $r+1$ distinct outgoing neighborhoods, the minimum possible, whenever $r\geq12$. The double of the $r=10$ parameter set also admits this minimum, with eleven outgoing neighborhoods. A second family,

$$
(108+27s,33+9s,11+3s,8+3s,11+3s),\qquad s\geq0,
$$

also exists, together with all positive multiples and complements. Section 7 proves this by a related extension of the quotient certificate.

Equivalently, the primary family and its complement are, for every $s\geq0$,

$$
\begin{aligned}
&(32+8s,14+4s,7+2s,5+2s,7+2s),\\
&(32+8s,17+4s,10+2s,9+2s,9+2s).
\end{aligned}
\tag{2}
$$

The following fifteen complementary pairs are marked unknown in the Hobart–Brouwer table archived on 16 October 2026 [1]. Ten pairs occur directly in (2), four more follow by multiplication, and the final pair begins the second family.

| Constructed parameters | Complementary parameters | Source |
|---|---|---|
| $(32,14,7,5,7)$ | $(32,17,10,9,9)$ | $s=0$ |
| $(40,18,9,7,9)$ | $(40,21,12,11,11)$ | $s=1$ |
| $(48,22,11,9,11)$ | $(48,25,14,13,13)$ | $s=2$ |
| $(56,26,13,11,13)$ | $(56,29,16,15,15)$ | $s=3$ |
| $(64,30,15,13,15)$ | $(64,33,18,17,17)$ | $s=4$ |
| $(72,34,17,15,17)$ | $(72,37,20,19,19)$ | $s=5$ |
| $(80,38,19,17,19)$ | $(80,41,22,21,21)$ | $s=6$ |
| $(88,42,21,19,21)$ | $(88,45,24,23,23)$ | $s=7$ |
| $(96,46,23,21,23)$ | $(96,49,26,25,25)$ | $s=8$ |
| $(104,50,25,23,25)$ | $(104,53,28,27,27)$ | $s=9$ |
| $(64,28,14,10,14)$ | $(64,35,21,20,18)$ | double of $s=0$ |
| $(80,36,18,14,18)$ | $(80,43,25,24,22)$ | double of $s=1$ |
| $(96,42,21,15,21)$ | $(96,53,32,31,27)$ | triple of $s=0$ |
| $(96,44,22,18,22)$ | $(96,51,29,28,26)$ | double of $s=2$ |
| $(108,33,11,8,11)$ | $(108,74,52,51,50)$ | Section 7 |

The first existence proof uses a ten-class, 32-vertex certificate and an eight-vertex extension that can be repeated indefinitely. Each extension retains the previous graph as an induced subgraph. Two additional seed certificates supply the neighborhood-count refinement. A fourth seed gives the second infinite family. The supplement supplies fifteen representative matrices, two independent deterministic constructors, and an independent exact checker. No search or optimization software is needed for reproduction.

## 2. Context and matrix formulation

For odd $r\geq3$, family (1) follows from the known graphs

$$
\left(2r,r-1,\frac{r-1}{2},\frac{r-3}{2},\frac{r-1}{2}\right)
$$

of Klin, Munemasa, Muzychuk, and Zieschang [2], followed by a coclique extension of multiplicity two; these are recorded as T5 and T10 in [1]. Our construction supplies every even $r\geq8$. We do not claim new existence for the odd-rank members or a classification of all realizations.

Parameters are ordered $(n,k,t,\lambda,\mu)$. A directed strongly regular graph is a loopless binary adjacency matrix $A$ satisfying

$$
A\mathbf1=k\mathbf1,\qquad \mathbf1^TA=k\mathbf1^T,\qquad
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
\tag{3}
$$

For (1), putting $H=J-2A$ makes (3) equivalent to

$$
H_{ij}\in\{-1,1\},\quad H_{ii}=1,\quad
H\mathbf1=4\mathbf1,\quad \mathbf1^TH=4\mathbf1^T,\quad H^2=4H.
\tag{4}
$$

The rank is $r$: $H/4$ is idempotent with trace $n/4$. On $\mathbf1^\perp$, $A=-H/2$, while $A\mathbf1=(2r-2)\mathbf1$, so $A$ and $H$ have the same rank.

Eigenspace representations and signed adjacency matrices are established tools for directed strongly regular graphs [3]. Johnson, Harel, Hillar, Groves, and Rault study absolutely flat idempotents, equivalently sign matrices satisfying $H^2=cH$ [4]. Their general existence theorem does not impose both regularity conditions in (4). Here a left-kernel sign vector permits a fixed local extension whose column imbalance is canceled by the cross block. The construction and every required identity are proved below.

## 3. A repeatable block extension

**Lemma 2.** Let $q$ be a positive even integer. Suppose $H$ is a sign matrix with diagonal one, $H^2=qH$, and both row and column sums equal to $q$. If there is a sign vector $z$ such that $z^TH=0$, then there is a matrix $G$ of order $n+2q$ with all the same properties, containing $H$ as a principal submatrix and having a sign vector in its left kernel. Its rank is two greater than that of $H$.

**Proof.** Write $e=\mathbf1_q$ and set

$$
c=\begin{pmatrix}\mathbf1_{q/2}\\-\mathbf1_{q/2}\end{pmatrix},\qquad
b=\begin{pmatrix}c\\c\end{pmatrix},\qquad
a=\begin{pmatrix}-e\\e\end{pmatrix},\qquad
D=\begin{pmatrix}J_q&-ec^T\\-ec^T&J_q\end{pmatrix}.
\tag{5}
$$

Direct multiplication gives

$$
\begin{gathered}
D^2=qD,\quad D\mathbf1_{2q}=q\mathbf1_{2q},\quad
\mathbf1_{2q}^TD=q(\mathbf1_{2q}-b)^T,\\
Da=qa,\quad b^TD=0,\quad b^Ta=0,\quad
\mathbf1_{2q}^Ta=\mathbf1_{2q}^Tb=0.
\end{gathered}
\tag{6}
$$

The diagonal of $D$ is one. Take any actual column $h$ of $H$. Then

$$
Hh=qh,\qquad \mathbf1^Th=q,\qquad z^Th=0.
$$

Also $z^T\mathbf1=0$, because $z^TH\mathbf1=qz^T\mathbf1=0$. Define

$$
G=\begin{pmatrix}H&hb^T\\az^T&D\end{pmatrix},\qquad
z'=\begin{pmatrix}z\\b\end{pmatrix}.
\tag{7}
$$

Every entry is a sign, and the diagonal is one. Its old row and column sums stay $q$ because $a$ and $b$ are balanced. Its new row sums are $q$ because $z$ is balanced and $D\mathbf1=q\mathbf1$. Its new column sums are

$$
qb^T+\mathbf1^TD=q\mathbf1^T.
$$

The four blocks of $G^2$ are

$$
\begin{aligned}
H^2+h(b^Ta)z^T&=qH,\\
Hhb^T+hb^TD&=qhb^T,\\
az^TH+Daz^T&=qaz^T,\\
a(z^Th)b^T+D^2&=qD.
\end{aligned}
$$

Thus $G^2=qG$. Finally,

$$
(z')^TG=(z^TH+b^Taz^T,\ z^Thb^T+b^TD)=0.
$$

The hypothesis is preserved, so the extension can be repeated. Since $G/q$ is idempotent, its rank is its trace $(n+2q)/q=n/q+2$. $\square$

For $q=4m$ and $n=4mr$, the matrix $A=(J-H)/2$ has parameters

$$
(4mr,2m(r-1),m(r-1),m(r-3),m(r-1)).
$$

The extension increases $r$ by two and keeps $m$ fixed. The local block $D$ has column sums zero or $2q$; the cross block compensates for this imbalance. Requiring every diagonal block to be column-regular would miss the construction.

![Adjacency matrices of the 32-vertex seed and its 40-vertex extension. Dark pixels represent arcs. The orange square in the right panel encloses the unchanged 32-by-32 principal submatrix; the final eight rows and columns belong to the added vertices.](supplement/figures/eight_vertex_extension.png)

## 4. A ten-class certificate at order 32

The following general certificate specifies every adjacency entry. Let $a_j$ be positive integers with $\sum_j a_j=2mr$, and let $U_j,V_j$ be integer vectors of a common length $\ell$, with $\sum_jV_j=0$. For each class $j$, take an ordered multiset $\mathcal C_j$ of $2a_j$ binary vectors of length $d$, the number of classes. Repeated patterns represent distinct vertices. Require, for every occurrence $x\in\mathcal C_j$,

$$
x_j=0,\qquad a^Tx=m(r-1),\qquad \sum_iV_ix_i=0,
\tag{8}
$$

and require the class sums

$$
\sum_{x\in\mathcal C_j}x_i=a_j+U_i\cdot V_j-2m\delta_{ij}=:Q_{ij}.
\tag{9}
$$

**Lemma 3.** Such a certificate constructs a graph with parameters $m(4r,2r-2,r-1,r-3,r-1)$ and a sign vector in the left kernel of $J-2A$.

**Proof.** Vertices are occurrences $(j,x)$ with $x\in\mathcal C_j$. Define

$$
A_{(i,x),(j,y)}=y_i.
\tag{10}
$$

The first condition in (8) excludes loops. The indegree of $(j,y)$ is $2a^Ty=2m(r-1)$. The outdegree of any vertex in class $i$ is

$$
\sum_jQ_{ij}=\sum_ja_j+U_i\cdot\sum_jV_j-2m=2m(r-1).
$$

The number of two-walks from any vertex in class $i$ to $(j,y)$ is

$$
(Qy)_i=a^Ty+U_i\cdot\sum_lV_ly_l-2my_i=m(r-1)-2my_i.
\tag{11}
$$

Thus $t=\mu=m(r-1)$ and $\lambda=m(r-3)$. In each class, give $z$ value $+1$ on its first $a_j$ vertices and $-1$ on the rest. Rows within a class are identical, so $z^TA=0$, and also $z^T\mathbf1=0$. Hence $z^T(J-2A)=0$. $\square$

For the primary seed take $m=1$, $r=8$, $d=10$, $\ell=2$, with the following complete data. Coordinates are numbered from zero. An integer mask $M$ encodes $x_i=(M\mathbin{\mathrm{div}}2^i)\bmod2$. Pattern order determines the vertex order.

| $j$ | $a_j$ | $U_j$ | $V_j$ | Incoming masks in $\mathcal C_j$ |
|---:|---:|---|---|---|
| 0 | 1 | $(1,0)$ | $(1,0)$ | 226, 792 |
| 1 | 1 | $(0,1)$ | $(0,1)$ | 209, 804 |
| 2 | 1 | $(-1,0)$ | $(-1,0)$ | 226, 792 |
| 3 | 1 | $(0,-1)$ | $(0,-1)$ | 209, 804 |
| 4 | 2 | $(0,0)$ | $(-1,0)$ | 397, 590, 226, 804 |
| 5 | 2 | $(0,0)$ | $(0,-1)$ | 654, 333, 209, 792 |
| 6 | 2 | $(0,0)$ | $(0,0)$ | 305, 305, 654, 654 |
| 7 | 2 | $(0,0)$ | $(0,0)$ | 305, 305, 590, 590 |
| 8 | 2 | $(0,0)$ | $(0,1)$ | 654, 103, 209, 562 |
| 9 | 2 | $(0,0)$ | $(1,0)$ | 397, 91, 305, 226 |

All certificate conditions are short finite integer checks. For example, mask $226$ has support $\{1,5,6,7\}$, so $a^Tx=1+2+2+2=7$ and $\sum_iV_ix_i=(0,1)+(0,-1)=(0,0)$. Its zeroth coordinate is zero, as required for class zero. The complete checker verifies every mask and every class sum.

The resulting $32\times32$ adjacency matrix has SHA-256

`2c248dc10217b141ea1e4e478015bd4a21139a8b0bd50253f6bca626f5393bd4`.

Lemma 3 supplies the seed and its kernel sign vector. Lemma 2 with $q=4$ proves existence for every even $r\geq8$.

The quotient form also explains the search. If $d$ denotes the number of distinct outgoing rows, the correction $Q+2mI-\mathbf1a^T$ has rank $d-r$. Taking $d=r+2$ permits a correction of rank two, realized by the two-coordinate vectors in the table. The existence proof uses only the displayed certificate; it makes no completeness claim about a search.

## 5. The minimum number of outgoing neighborhoods

**Lemma 4.** For even $r$ and positive $m$, any graph with parameters $m(4r,2r-2,r-1,r-3,r-1)$ has at least $r+1$ distinct outgoing neighborhoods.

**Proof.** The adjacency rank is $r$, so at least $r$ distinct rows are necessary. If there are exactly $r$, write $A=XY$, where $X$ indicates the row classes and $Y$ consists of the distinct rows. The quotient $Q=YX$ has spectrum $2m(r-1)$ and $-2m$, the latter with multiplicity $r-1$. If $w$ records the class sizes, regularity gives

$$
Q=-2mI+\frac12\mathbf1w^T.
$$

A class has no internal arcs: identical outgoing neighborhoods and a zero diagonal force every such entry to be zero. Thus $Q_{jj}=0$ and $w_j=4m$ for every $j$. Every indegree would be divisible by $4m$. But $2m(r-1)$ is not divisible by $4m$ for even $r$, a contradiction. $\square$

The next two scalar certificates ($\ell=1$) attain this lower bound. They use the notation and conditions (8)–(9), with $U_j=u_j$ and $V_j=v_j$.

### 5.1 A 48-vertex certificate with thirteen neighborhoods

Take $m=1$, $r=12$, $d=13$.

| $j$ | $a_j$ | $u_j$ | $v_j$ | Incoming masks in $\mathcal C_j$ |
|---:|---:|---:|---:|---|
| 0 | 1 | 1 | 1 | 7712, 6592 |
| 1 | 1 | -1 | -1 | 1596, 476 |
| 2 | 1 | -1 | -1 | 1594, 474 |
| 3 | 2 | -1 | 0 | 3185, 3185, 4998, 4998 |
| 4 | 2 | -1 | 0 | 3177, 3177, 4998, 4998 |
| 5 | 2 | 0 | -1 | 3103, 1628, 4998, 474 |
| 6 | 2 | 0 | -1 | 3103, 1596, 4998, 442 |
| 7 | 2 | 0 | 1 | 5699, 7189, 2409, 6944 |
| 8 | 2 | 0 | 1 | 5699, 7189, 2281, 6816 |
| 9 | 2 | 0 | 1 | 5443, 7189, 2281, 6560 |
| 10 | 2 | 0 | 1 | 4931, 6677, 2281, 6560 |
| 11 | 2 | 1 | 0 | 1145, 1145, 4998, 4998 |
| 12 | 3 | 1 | -1 | 3655, 3655, 1628, 444, 442, 442 |

The 48-vertex adjacency matrix has SHA-256

`b2ee75171df5dfb6ce0a77e4b7d1a6198522050b16405da64cb3d92242c89c04`.

### 5.2 An 80-vertex certificate with eleven neighborhoods

Take $m=2$, $r=10$, $d=11$.

| $j$ | $a_j$ | $u_j$ | $v_j$ | Incoming masks in $\mathcal C_j$ |
|---:|---:|---:|---:|---|
| 0 | 2 | 1 | 2 | 1856, 1856, 1920, 1920 |
| 1 | 2 | -1 | -2 | 124, 124, 188, 188 |
| 2 | 3 | -1 | -1 | 1081, 1081, 714, 714, 370, 434 |
| 3 | 3 | -1 | -1 | 1077, 1077, 710, 710, 370, 434 |
| 4 | 4 | -1 | 0 | 1321, 1321, 1321, 1321, 710, 710, 710, 710 |
| 5 | 4 | -1 | 0 | 1305, 1305, 1305, 1305, 710, 710, 710, 710 |
| 6 | 4 | 0 | 2 | 1667, 1667, 1317, 1317, 793, 793, 1920, 1920 |
| 7 | 4 | 0 | 2 | 1603, 1603, 1317, 1317, 793, 793, 1856, 1856 |
| 8 | 4 | 1 | 0 | 1081, 1081, 1081, 1081, 710, 710, 710, 710 |
| 9 | 5 | 1 | -1 | 1321, 1321, 159, 159, 188, 124, 1222, 1222, 370, 370 |
| 10 | 5 | 1 | -1 | 809, 809, 159, 159, 188, 124, 710, 710, 370, 370 |

The 80-vertex adjacency matrix has SHA-256

`19d8ed0ae20ffe473006831efc1caf6f8ff6c405a671c393c0dfa00b76ec34dc`.

Both certificates satisfy $|v_j|\leq a_j$. Besides the kernel vector in Lemma 3, we may therefore use a vector with $+1$ on the first $a_j+v_j$ vertices of class $j$ and $-1$ on the rest. Its class sum is $2v_j$; the equations $\sum_jv_j=0$ and $\sum_jv_jy_j=0$ prove that it too lies in the left kernel of $H$. The scalar-certificate implementation uses this choice.

Each extension (7) adds at most two outgoing row types. Old equal rows remain equal because $h$ is an actual column of $H$, and the new rows occur in two groups of $q$ equal rows. Lemma 4 shows that the initial bounds of thirteen and eleven are attained and remain attained under extension. Multiplication preserves the number of distinct outgoing rows. This proves the refinement in Theorem 1, and transposition gives the analogous incoming-neighborhood examples. We do not claim optimality of the ten-class seed at order 32 or its twelve-class extension at order 40.

## 6. Multiples, complements, and reproduction

For a positive integer $b$, replacing $A$ by $A\otimes J_b$ multiplies all five parameters by $b$, because $t=\mu$. Explicitly, if $A$ has parameters $m(4r,2r-2,r-1,r-3,r-1)$, then

$$
(A\otimes J_b)^2=-2mb(A\otimes J_b)+bm(r-1)J_{4rmb}.
$$

The complement $J-I-A$ of a graph with parameters $(n,k,t,\lambda,\mu)$ has parameters

$$
(n,n-k-1,n-2k+t-1,n-2k+\mu-2,n-2k+\lambda).
$$

The supplement provides all four seed certificates, the general extension, fifteen representative matrices, an independent direct two-walk checker, expected hashes, and a manifest. Two independent generators produce byte-identical matrices: one applies (7), while the other extends the class certificates. Independent integer matrix multiplication also checked the supplied graphs and their complements during development. Larger checks at orders 112, 128, and 160 agree with the general proof.

After extracting the supplement, run

```bash
python -S src/verify_even_rank_family.py
python -S src/even_rank_family.py --seed 32 --steps 1 --output order40.txt
python -S src/even_rank_family.py --seed 32 --multiple 3 --output order96.txt
python -S src/even_rank_family.py --seed 48 --steps 3 --output order72.txt
python -S src/even_rank_family.py --seed 80 --output order80.txt
python -S src/alphabet_family.py --steps 1 --output order135.txt
```

Python 3.10 or later suffices. The first command validates every certificate and manifest hash, compares both constructors, and checks all fifteen representatives and fifteen complements. The remaining commands illustrate arbitrary extension, multiplication, and the two neighborhood-minimal seeds. The search that discovered the certificates is unnecessary for verification. Code and generated data are released under the MIT license. These are exact existence results and a neighborhood-count refinement, without a classification of all graphs with these parameters.

## 7. A related extension by three new classes

The certificate construction has a version for any integer $b\geq2$. Let class $j$ have $ba_j$ vertices, where $\sum_j a_j=br$. Use integer vectors $U_j,V_j$ with $\sum_jV_j=0$, and require

$$
x_j=0,\qquad a^Tx=r-1,\qquad \sum_iV_ix_i=0,
$$

for each $x\in\mathcal C_j$, together with

$$
\sum_{x\in\mathcal C_j}x_i=a_j+U_i\cdot V_j-b\delta_{ij}.
\tag{12}
$$

Defining adjacency by (10) gives degrees $b(r-1)$ and two-walk counts $r-1-by_i$, by exactly the calculation in Lemma 3. Hence the parameters are

$$
(b^2r,b(r-1),r-1,r-b-1,r-1).
\tag{13}
$$

**Lemma 5.** Suppose a certificate for (13) has $b-1$ pairwise disjoint binary patterns $p_1,\ldots,p_{b-1}$ satisfying $a^Tp_l=r-1$ and $\sum_iV_i(p_l)_i=0$. The patterns need not all occur in the same old class. Then there is a certificate with $b$ more classes and rank parameter $r+b$, containing the original graph as an induced subgraph. The same disjoint-pattern hypothesis holds for the new certificate.

**Proof.** Let $p_b=\mathbf1-\sum_{l=1}^{b-1}p_l$. Disjointness makes $p_b$ binary, with weight

$$
a^Tp_b=br-(b-1)(r-1)=r+b-1
$$

and zero $V$ moment. Add $b$ classes, each with $a_j=b$ and $U_j=V_j=0$, hence each containing $b^2$ vertices. Partition the $ba_j$ vertices of each old class into $b$ groups of size $a_j$. Extend each old incoming pattern by a single one in the new coordinate corresponding to its group. Its weight increases by $b$, its moment stays zero, and the old part of the adjacency matrix is retained.

For each new class $j$, biject the first $b-1$ patterns with the new coordinates other than $j$. Place $b$ copies of $p_l$ with a one in its assigned new coordinate, for $1\leq l<b$, and $b$ copies of $p_b$ with no new one. Every resulting pattern has weight $r+b-1$, zero moment, and zero coordinate at its own class.

For an old row coordinate, the patterns in each new class sum to $b$, since $p_1+\cdots+p_b=\mathbf1$; this is (12) with the new $a_j=b$ and $V_j=0$. For a new row coordinate, the patterns in an old class sum to $a_j$ by the equal grouping; this is (12) with the new $U_i=0$. Within the new classes, the sum is zero on the diagonal and $b$ off the diagonal, again as required. Thus every certificate condition holds.

Finally, the first $b-1$ patterns in any one new class remain pairwise disjoint: their old parts are disjoint and their new ones occupy distinct coordinates. They all have the new required weight and zero moment. The operation therefore repeats. $\square$

For $b=2$, a single eligible pattern always suffices, recovering an eight-vertex certificate extension. For $b=3$, two disjoint patterns give an extension by 27 vertices. The known construction T12 in [1], from [3], already supplies (13) when $r\equiv1\pmod b$ and the usual positivity conditions hold. The seed below instead has $b=3$, $r=12$, and generates $r=12+3s$.

Take $b=3$, $r=12$, $d=13$, and scalar $U_j=u_j$, $V_j=v_j$:

| $j$ | $a_j$ | $u_j$ | $v_j$ | Incoming masks in $\mathcal C_j$ |
|---:|---:|---:|---:|---|
| 0 | 2 | 1 | 1 | 3586, 3588, 3336, 368, 2224, 1232 |
| 1 | 2 | -1 | -1 | 4109, 4124, 836, 840, 4256, 4256 |
| 2 | 2 | -1 | -1 | 4107, 4122, 834, 840, 4256, 4256 |
| 3 | 2 | -1 | -1 | 4103, 4118, 834, 836, 4256, 4256 |
| 4 | 2 | 1 | 1 | 3586, 3588, 3336, 353, 2209, 1217 |
| 5 | 3 | 0 | -1 | 1672, 2440, 4288, 4109, 4109, 4118, 4118, 834, 834 |
| 6 | 3 | 0 | -1 | 1672, 2440, 4256, 4109, 4109, 4118, 4118, 802, 802 |
| 7 | 3 | 0 | 0 | 3137, 3137, 3137, 802, 802, 802, 4124, 4124, 4124 |
| 8 | 3 | 0 | 1 | 6208, 3586, 3586, 624, 3152, 3105, 1185, 157, 157 |
| 9 | 3 | 0 | 1 | 6208, 3330, 3330, 368, 3152, 3105, 1185, 157, 157 |
| 10 | 3 | 2 | 0 | 2241, 2241, 2241, 802, 802, 802, 4124, 4124, 4124 |
| 11 | 3 | 2 | 0 | 1217, 1217, 1217, 802, 802, 802, 4124, 4124, 4124 |
| 12 | 5 | -2 | 1 | 3586, 3586, 3586, 3586, 624, 3152, 3120, 1416, 2436, 157, 157, 157, 353, 353, 353 |

The disjoint masks $157$ and $802$ have supports $\{0,2,3,4,7\}$ and $\{1,5,8,9\}$. Each has $a$ weight eleven and zero $v$ moment; their complement has weight fourteen. Thus Lemma 5 applies. The seed matrix has SHA-256

`c316f8a0c93695dfbc66fec56eeedf9772840bfebb6266ffc815141f6238c092`.

This proves the second family in Theorem 1. The supplement includes the certificate, its direct recurrence, and a separate implementation that extends the full adjacency matrix by blocks. The two implementations agree exactly at orders 108, 135, and 162; the double of the base at order 216 also passes both integer checks. The 108-vertex graph and its complement add two unknown entries in [1]. The general construction requires the stated disjoint-pattern hypothesis; we do not assert it for arbitrary DSRGs or for every parameter set in (13).

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. Online table, retrieved 16 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] M. Klin, A. Munemasa, M. Muzychuk, and P.-H. Zieschang. *Directed strongly regular graphs obtained from coherent algebras*. Linear Algebra and its Applications 377 (2004), 83–109. https://doi.org/10.1016/j.laa.2003.06.020

[3] C. D. Godsil, S. A. Hobart, and W. J. Martin. *Representations of directed strongly regular graphs*. European Journal of Combinatorics 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008. Author manuscript: https://users.wpi.edu/~martin/RESEARCH/godsilhobartmartin.pdf

[4] C. R. Johnson, Y. Harel, C. J. Hillar, J. M. Groves, and P. X. Rault. *Absolutely flat idempotents*. Electronic Journal of Linear Algebra 10 (2003), 190–200. https://doi.org/10.13001/1081-3810.1106. Open full text: https://journals.uwyo.edu/index.php/ela/article/download/213/213

# Nondivisible closed-neighborhood classes in two families of directed strongly regular graphs

Mira Loom (`mira_loom`), 18 November 2026.

## 1. Results and motivation

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ has a Boolean adjacency matrix $A$ satisfying

$$
AJ=JA=kJ,\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

When $t=\lambda+1$, its closed adjacency matrix $B=A+I$ has diagonal one and satisfies

$$
B\mathbf1=K\mathbf1,\qquad \mathbf1^{\mathsf T}B=K\mathbf1^{\mathsf T},
\qquad B^2=qB+\mu J,\qquad K=k+1,\quad q=\lambda+2-\mu. \tag{1}
$$

This standard reduction follows from the DSRG equations [1]. A *full row class* is a maximal set of vertices having the same row of $B$. Full column classes are defined by transposition. Their sizes count vertices, not distinct row vectors.

The existence questions for $(75,19,8,7,4)$ and $(98,20,9,8,3)$ remain open in the Hobart–Brouwer table consulted on 18 November 2026 [2]. They satisfy (1) with $(K,q,\mu)=(20,5,4)$ and $(21,7,3)$. We prove restrictions that apply to every hypothetical graph, without selecting a class size, local rank, equitable partition or automorphism.

**Theorem 1.** Let $q\ge7$ be an integer not divisible by $3$. Suppose a Boolean matrix $B$ with diagonal one has constant row and column sum $3q$ and satisfies $B^2=qB+3J$. Then its order is $2q^2$, and at least eight full row classes have size not divisible by $3$.

**Theorem 2.** Let $q\ge3$ be odd. Suppose a Boolean matrix $B$ with diagonal one has constant row and column sum $4q$ and satisfies $B^2=qB+4J$. Then its order is $3q^2$, and at least six full row classes have size not divisible by $4$.

Both theorems hold for full column classes. In DSRG notation they concern the parameter families

$$
(2q^2,3q-1,q+2,q+1,3),\qquad
(3q^2,4q-1,q+3,q+2,4).
$$

**Corollary 3.** A hypothetical DSRG$(98,20,9,8,3)$ has at least eight full row classes of size nondivisible by $3$. If every full row class has size at most three, there are at least 36 classes. A hypothetical DSRG$(75,19,8,7,4)$ has at least six full row classes of size nondivisible by $4$; if all classes have size at most four, there are at least 21 classes. All statements transpose.

The main mechanism is global. Column regularity gives a weighted identity among the distinct actual rows. Reducing it modulo $\mu$ deletes all classes whose sizes are divisible by $\mu$. A short remaining list forces integer affine combinations of actual rows. Boolean combinations are controlled by overlap bounds; signed combinations require separate analysis of their positive and negative supports. In two cases the actual vertices owning the rows exclude a set system that abstract equal-weight Boolean vectors could otherwise realize. Section 8 forces short actual-row relations at both target orders, restricts their coefficients and complements, and connects the longest possibilities to full neighborhood classes.

## 2. Relation to previous work

Duval's work supplies the basic spectral and parameter framework [1]. Meleta develops (1) in terms of full closed-neighborhood classes [3], including the directed-distance bound between distinct rows, bounds on class size, and the restriction that a vertex outside a class meets it in at most $\mu$ points. We use the same matrix and actual-row framework. For clarity, all elementary facts required below are proved here, including the equality structure in the directed-distance bound.

The contribution is a lower bound on the number of full classes whose sizes have nonzero residues. It does not follow by substituting the target parameters into the individual class-size bounds in [3]: those bounds do not prohibit a short global residue relation. Our proof uses that relation, a five-label weighted support argument, and signed residual supports. For $\mu=3$, a seven-row relation forces weighted triples on seven labels. Actual row equations impose a lower bound on every four-label subset. Counting excludes all parameters except $q=7$, where two fully certified finite covering cases finish the proof.

Literal control matrices used by the independent checks include the constructions of order 65 and 77 in [4], the known generalized-quadrangle flag graph of order 45 discussed in [3], and independently reconstructed matrices of orders 45 and 48. They validate the general inequalities and their equality conditions. They are not examples satisfying the hypotheses of the open order-75 or order-98 existence problems.

## 3. Affine rows, sharp distance and actual ownership

We identify a Boolean row with its support where convenient. All row vectors in equations act on the left. Put $\mathbf j=\mathbf1^{\mathsf T}$. If $R$ is an actual row of $B$, then

$$
RB=qR+\mu\mathbf j.
$$

Consequently $f=\sum_i a_iR_i$ satisfies

$$
fB=qf+\mu\Bigl(\sum_i a_i\Bigr)\mathbf j. \tag{2}
$$

**Lemma 4 (signed mass).** Suppose $zB=qz+\gamma\mathbf j$. Let
$M_+(z)=\sum_u\max(z_u,0)$ and $M_-(z)=\sum_u\max(-z_u,0)$. At every coordinate $h$,

$$
-M_-(z)\le qz_h+\gamma\le M_+(z). \tag{3}
$$

If equality holds on the right, every positive coordinate of $z$ enters $h$, and no negative coordinate enters $h$. Equality on the left reverses these two conclusions.

*Proof.* Each entry of $B$ is zero or one. The largest possible value of $\sum_u z_uB_{uh}$ is the sum of the positive terms, and equality requires all of them and none of the negative terms. The minimum is analogous. $\square$

**Lemma 5 (Boolean overlap).** If a Boolean row $x$ satisfies $xB=qx+\beta\mathbf j$ and $R$ is an actual row, put $P=\operatorname{supp}(x)\setminus R$ and $N=R\setminus\operatorname{supp}(x)$. Then

$$
P\ne\varnothing\Longrightarrow |P|\ge q+\beta-\mu,
\qquad
N\ne\varnothing\Longrightarrow |N|\ge q+\mu-\beta. \tag{4}
$$

*Proof.* Apply (3) to $x-R$, whose affine constant is $\beta-\mu$, at a coordinate of $P$ or $N$. $\square$

A Boolean row with exactly $q$ ones and affine constant one is impossible: at one of its positive coordinates its equation requires $q+1$ contributions from only $q$ vertices. When $K=3q$ and $\mu=3$, (4) gives two further useful bounds:

$$
\begin{array}{c|c|c}
|\operatorname{supp}(x)|&\beta&|R\cap\operatorname{supp}(x)|\text{ at most}\\ \hline
2q&2&q+1\\
4q&4&2q+1
\end{array} \tag{5}
$$

For the first, $P$ cannot be empty: otherwise $|N|=q$ contradicts (4), which requires $q+1$. Hence $|P|\ge q-1$. For the second, $N$ cannot be empty, and $|N|\ge q-1$.

**Lemma 6 (sharp distance).** Distinct actual rows $R,S$ have $|R\setminus S|=|S\setminus R|\ge q$. If equality holds, the two difference sets induce complete $q\times q$ blocks of $B$, with no entries between the blocks in either direction.

*Proof.* The row sums agree. Apply (3) to $R-S$, for which $\gamma=0$. If each difference set has size $q$, every positive and negative coordinate attains equality, giving the asserted entries. $\square$

Two consequences require that these are rows of a matrix with diagonal one.

First, there cannot be $\ell\ge3$ actual rows $R_i=X\setminus D_i$, where the $D_i$ partition $X$ into $q$-sets. Their pairwise differences force the $D_i$ to be mutually isolated complete blocks. Any vertex owning $R_i$ belongs to some $D_j$ with $j\ne i$, since its own diagonal entry is one. Its row would select another block $D_k$ with $k\notin\{i,j\}$, contrary to isolation.

Second, if actual rows $S_i=Y\cup E_i$ have disjoint $q$-sets $E_i$ and common part $Y$ disjoint from them, an additional actual row cannot be $\bigcup_iE_i$ when at least two $E_i$ occur. Its owner lies in one of the mutually isolated $E_i$ but would select the others. We call these the two *ownership contradictions*.

## 4. Reduction to short residue profiles

Let $R_i$ be all distinct full row representatives, with class sizes $w_i$. Column regularity states

$$
\sum_iw_iR_i=K\mathbf j. \tag{6}
$$

When $K=\mu q$, reduce (6) modulo $\mu$. Only classes with nonzero residues remain. If $c_r$ counts classes of size $r$ modulo $\mu$, a column pattern $v$ on these representatives satisfies

$$
\sum_{r=1}^{\mu-1}r\sum_{i\text{ of residue }r}v_i\equiv0\pmod\mu,
\qquad
\sum_{r=1}^{\mu-1}rc_r\equiv n\pmod\mu. \tag{7}
$$

Taking row sums in (1) gives $n=(\mu-1)q^2$. Thus $n\equiv2\pmod3$ in Theorem 1, and $n\equiv3\pmod4$ in Theorem 2. A row combination $x=(\sum_i a_iR_i)/\mu$ has coordinate sum $q\sum_i a_i$ and affine constant $\sum_i a_i$.

The complete populations with at most five exceptional classes appear in Tables 1 and 2. Rows are ordered by ascending residue. An entry “zero” names a representative forced to vanish; a coefficient list in the zero-combination column gives a combination identically zero with coefficient sum nonzero, contradicting the common positive row degree. A coefficient list in the indicator column gives a Boolean $x=(\sum a_iR_i)/\mu$ with $\sum a_i=1$, impossible by Lemma 4. These assertions follow by the Boolean patterns in (7); the supplement independently lists every pattern.

**Table 1.** The seven populations for $\mu=3$ with at most five exceptional classes.

| $(c_1,c_2)$ | Exclusion |
|---|---|
| $(0,1)$ | sole row zero |
| $(2,0)$ | both rows zero |
| $(1,2)$ | zero combination $(-1,1,1)$ |
| $(2,3)$ | indicator coefficients $(-1,-1,1,1,1)$ |
| $(0,4)$ | four rows complementary to four $q$-sets |
| $(3,1)$ | three rows $Y\cup E_i$ and the fourth row $\bigcup_iE_i$ |
| $(5,0)$ | five-label argument in Section 5 |

In the fifth row, every nonzero column has three selected representatives. Equal row degrees imply that their union has size $4q$ and each missing block has size $q$. In the sixth row, the first three representatives have a common part of size $2q$ and disjoint private $q$-sets, whose union is the last row. Lemma 6 and its ownership consequences apply.

**Table 2.** The fourteen populations for $\mu=4$ with at most five exceptional classes.

| $(c_1,c_2,c_3)$ | Exclusion |
|---|---|
| $(0,0,1)$ | sole row zero |
| $(1,1,0)$ | both rows zero |
| $(3,0,0)$ | all rows zero |
| $(0,2,1)$ | residue-3 row zero |
| $(0,4,1)$ | residue-3 row zero |
| $(1,3,0)$ | residue-1 row zero |
| $(1,0,2)$ | zero combination $(-1,1,1)$ |
| $(0,1,3)$ | zero combination $(-2,1,1,1)$ |
| $(2,0,3)$ | zero combination $(1,1,-1,-1,-1)$ |
| $(2,1,1)$ | zero combination $(1,1,-2,-1)$ |
| $(1,2,2)$ | indicator coefficients $(-1,-2,2,1,1)$ |
| $(3,2,0)$ | indicator coefficients $(-1,-1,-1,2,2)$ |
| $(0,0,5)$ | five rows complementary to five $q$-sets |
| $(4,0,1)$ | four rows $Y\cup E_i$ and a row $\bigcup_iE_i$ |

Here the last two rows follow exactly as above, with union size $5q$ in the complementary-block case and common part size $3q$ in the private-block case. This proves Theorem 2.

## 5. Five representatives and a weighted graph on five labels

Consider the last row of Table 1. Five actual degree-$3q$ rows select either zero or three entries in each column. Their union $X$ has size $5q$, and its indicator satisfies

$$
\mathbf1_X^{\mathsf T}B=q\mathbf1_X^{\mathsf T}+5\mathbf j.
$$

Label each vertex in $X$ by the pair of representatives that miss it. Let $m_{ab}$ be the size of the corresponding fibre. These weights define a simple graph on five labels, of weighted degree $2q$ at each label and total weight $5q$.

At a column in fibre $\{a,b\}$ there are $q+5$ predecessors from $X$. The number of these missed by row $i$ is $q+2$ if $i\in\{a,b\}$ and two otherwise. If $h_{ab}$ of the predecessors come from the same fibre, comparison of the two endpoint degrees with the other three degrees gives

$$
2h_{ab}\ge2(q+2)-6=2q-2.
$$

Thus every positive fibre has size at least $q-1$. For $q\ge7$, the support has at most five edges and ordinary degree at most two, because $3(q-1)>2q$. A leaf forces its incident edge to have weight $2q$, so its neighbor is also a leaf. Every other component is a cycle. There are exactly two possibilities: a five-cycle of edge weights $q$, or a triangle of weights $q$ and a disjoint edge of weight $2q$.

Choose a fibre on an odd cycle. Its predecessor counts on that cycle are uniquely determined. They equal $q+1$ on its own fibre and one on each other cycle edge; in the triangle case the isolated edge contributes two. These counts satisfy the required endpoint degrees, and uniqueness follows from the invertibility of the incidence matrix of an odd cycle. A fibre of size $q$ cannot supply $q+1$ predecessors. This excludes $(5,0)$ and proves that at least six classes are exceptional.

For exactly six exceptional classes, (7) leaves only $(c_1,c_2)=(4,2)$ and $(1,5)$. Their complete profiles give Boolean combinations

$$
x=\frac{R_1+\cdots+R_4-R_5-R_6}{3},
\qquad
x=\frac{-R_1+R_2+\cdots+R_6}{3},
$$

of size $2q$, constant two, and size $4q$, constant four, respectively. Restricting the identities to their positive supports and using (5) requires

$$
6q\le4(q+1),\qquad 12q\le5(2q+1),
$$

respectively. Both are false for $q\ge7$. Hence at least seven classes are exceptional.

## 6. Both mixed seven-class patterns are impossible

The possibilities for seven exceptional classes are $(6,1),(3,4),(0,7)$.

### 6.1 Six residue-one classes and one residue-two class

Write the rows as $R_1,\ldots,R_6,S$, and put $f=(\sum_iR_i-S)/3$. The profile alphabet gives $f\in\{0,1,2\}^n$, coordinate sum $5q$, and affine constant five. Each $y_i=f-R_i$ has values $-1,0,1$, sum $2q$, and constant two.

If $y_i$ had no negative coordinate, it would be Boolean. But

$$
3y_i=\sum_{j\ne i}R_j-2R_i-S
$$

would require $6q$ positive incidences from five rows, at most $5(q+1)$ by (5). Thus the negative support of every $y_i$ is nonempty. Its size is at least $q-2$ by (3). The profile alphabet says that a negative coordinate has $f=0$, $S=1$, and precisely one selected $R_i$. Hence these six negative supports are pairwise disjoint subsets of $S$, requiring $6(q-2)>3q$ points. This is impossible.

### 6.2 Three residue-one classes and four residue-two classes

Write the first three rows as $N_1,N_2,N_3$ and the other four as $P_1,\ldots,P_4$. Put

$$
f=\frac{\sum_{i=1}^4P_i-\sum_{j=1}^3N_j}{3}.
$$

The complete profiles give values $-1,0,1$, sum $q$, and affine constant one. Let $T=\{f=-1\}$, $X=\{f=1\}$, $Z=\{f=0\}$, and $t=|T|$. Every point of $T$ is selected by all three $N$ rows and no $P$ row. On $X$ the counts $(N,P)$ are $(0,3)$ or $(1,4)$; on $Z$ they agree. Therefore $|X|=t+q$, and distinctness of the $N$ rows gives $t\le2q$.

Let $D_i=X\setminus P_i$. These four sets are disjoint. If $D_i$ were empty, $P_i-f$ would be Boolean of size $2q$ and constant two, while

$$
3(P_i-f)=2P_i+\sum_jN_j-\sum_{\ell\ne i}P_\ell
$$

has positive coefficient sum five. Again $6q\le5(q+1)$ would be necessary. Thus $D_i\ne\varnothing$. The positive entries of $f-P_i$ are precisely its ones on $D_i$, and its affine constant is $-2$. Lemma 4 gives $|D_i|\ge q-2$. Consequently

$$
3q-8\le t\le2q. \tag{8}
$$

This is impossible for $q\ge9$. It remains to treat $(q,t)=(7,13),(7,14),(8,16)$.

Suppose first $t=2q$, with $q=7$ or $8$. Write $N_j=T\cup E_j$. The $E_j$ are disjoint $q$-sets; Lemma 6 makes them mutually isolated complete blocks. At most $8-q\le1$ points of $X$ are selected by any $N$ row, so choose an $E_j$ entirely in $Z$.

For a column $h\in E_j$, its $N_j$ equation says that $T$ contributes three predecessors. Its $f$ equation then says that $X$ contributes four. Every $h\in E_j$ belongs to exactly one $P$ row. Any $D_i$ has size at most six, because the other three have size at least $q-2$; thus every $P_i$ contains at least $3q-6$ points of $X$ and at most six points of $E_j$. Choose $P_i$ containing $h$ and put $r=|P_i\cap E_j|$. Since $1\le r\le6<q$, a point of $E_j$ missed by $P_i$ exists. The $P_i$ equation at that point has value three, and the complete block forces $r\le3$. At $h$, the row $P_i$ can receive at most four contributions from $X$ and $r$ from $E_j$, and none from the other $E$ blocks. Its entire support lies in $X\cup\bigcup_jE_j$. Thus its value is at most seven, contradicting the required $q+3\ge10$.

Finally let $q=7,t=13$. Then $|X|=20$, and the four $D_i$ partition $X$ into five-sets. Each $P_i$ has 15 points in $X$ and a residual six-set $F_i=P_i\cap Z$. Each $N_j$ consists of $T$ and an eight-set $E_j\subseteq Z$. The pair intersections of the three $E_j$ have size at most one. At every point of $Z$, the number of $E$ incidences equals the number of $F$ incidences.

There are at most three points lying in multiple $E_j$. Each six-set $F_i$ therefore contains a point $h$ belonging to just one $E_j$. Let $a$ be the number of predecessors of $h$ in $T$. The two other $N$ equations give $a\le3$, and $f(h)=0$ gives $a+1\le4$ predecessors in $X$. The $P_i$ equation at $h$ requires ten. Its $F_i$ part has only six points, so equality forces $a=3$, all six $F_i$ points entering $h$, and four predecessors from its $X$ part. The two other $N$ equations now say that neither of their residual $E$ sets enters $h$. It follows that all of $F_i$ lies in the private part of the one $E_j$.

This holds for every $F_i$. A point in multiple $E_j$ would require positive $F$ incidence, but no $F_i$ can contain such a point. Thus the three $E_j$ are disjoint. Each eight-set needs at least two of the six-sets assigned to it to cover all its points. That requires at least six $F_i$, whereas only four exist. This completes the exclusion of $(3,4)$.

## 7. The remaining equality case

Only $(c_1,c_2)=(0,7)$ remains. The profile equation says that the seven representative rows select zero, three or six entries at each column. Thus $f=\sum_iR_i/3$ has values $0,1,2$, sum $7q$ and affine constant seven.

For any pair $i,j$, the vector $g=f-R_i-R_j$ has values $-1,0,1$, sum $q$ and constant one. Its negative support is exactly the set of points of $X=\{f=1\}$ selected by both $R_i,R_j$. It cannot be empty, because a nonnegative $g$ would be the impossible Boolean row of size $q$ and constant one. By (3) it has at least $q-1$ points.

Every point of $X$ is selected by three representatives and belongs to precisely three of these 21 pair supports. If $h=|\{f=2\}|$, then $|X|=7q-2h$, so

$$
21(q-1)\le3(7q-2h),\qquad h\le3. \tag{9}
$$

We next exclude this final seven-row pattern for every parameter in Theorem 1.

### 7.1 Every four-label set has positive capacity

Every vertex of $X$ has a triple profile on the seven row labels. Every vertex of $H=\{f=2\}$ misses one label; let $h_i$ count those missing label $i$, and put $h=\sum_i h_i$. For a triple $A$, let $m_A$ be its fibre size. The degree of label $i$ on $X$ is $3q-h+h_i$. Put

$$
x_{ij}=|R_i\cap R_j\cap X|=q-1+d_{ij},\qquad d_{ij}\ge0.
$$

For complementary label sets $T,S$ of sizes three and four, define
$\delta_T=\sum_{\{i,j\}\subset T}d_{ij}$, $h_{\rm out}(T)=\sum_{i\notin T}h_i$, and $M_S=\sum_{A\subset S}m_A$. Inclusion-exclusion by the number of selected labels in $T$ gives

$$
M_S+m_T=q-3+\delta_T+h_{\rm out}(T). \tag{10}
$$

To bound $m_T$, apply Lemma 4 to $z=\sum_i y_iR_i$, with $y_i=2$ on $T$ and $-1$ elsewhere. The affine constant is six. At a column of profile $T$, $z$ equals six. On the other triple profiles its positive value is three exactly when two labels belong to $T$. On $H$ it equals three exactly when the missing label is outside $T$. If $n_2=\sum_{|A\cap T|=2}m_A$, the signed-mass bound yields

$$
6q+6\le6m_T+3n_2+3h_{\rm out}(T).
$$

Since $3m_T+n_2=3(q-1)+\delta_T$, this is

$$
m_T>0\Longrightarrow m_T\le q-5+\delta_T+h_{\rm out}(T). \tag{11}
$$

If $M_S=0$, equation (10) forces positive $m_T$ that exceeds (11) by two. Therefore every four-set $S$ contains an occupied triple. Now take $y_i=1$ on $S$ and $-2$ outside. Its affine constant is $-6$. The only positive values of $z$ are three on the triple profiles contained in $S$; on every $H$ profile its value is nonpositive. At an occupied triple contained in $S$, Lemma 4 therefore gives

$$
M_S\ge q-2\quad\hbox{for every four-set }S. \tag{12}
$$

Each triple lies in four four-sets. Summing (12) gives

$$
4(7q-2h)\ge35(q-2),\qquad 7q+8h\le70. \tag{13}
$$

This excludes every $q\ge11$.

We also need a lower bound on a positive fibre. At a column of profile $A$, let $a_X,b$ count predecessors in $X,H$, and let $a_A$ count those in its own fibre. The affine equation gives $a_X+2b=q+7$. The three actual row equations indexed by $A$ have sum $3q+9$. An $X$ predecessor outside this fibre contributes at most two to that sum, a same-fibre predecessor contributes three, and an $H$ predecessor at most three. Thus

$$
3q+9\le2a_X+a_A+3b,
\qquad m_A\ge a_A\ge q-5+b\ge q-5. \tag{14}
$$

### 7.2 Counting excludes $q=8$ and $q=10$

At $q=8$, every positive $m_A$ is at least three, and every four-set has weight at least six. Replace the weight of a triple by six if it is the sole occupied triple in some four-set, by three if it is occupied but never sole, and by zero otherwise. These replacements do not increase total weight and preserve every four-set lower bound. Divide by three. The resulting integer weights have total $W\le\lfloor56/3\rfloor=18$, and each four-set has weight at least two. Summation forces $4W\ge70$, so $W=18$.

Let $d_i$ be the total normalized weight of triples containing label $i$. The sum of the weights of the 20 four-sets containing $i$ is $W+3d_i\ge40$. Hence $d_i\ge8$ for every label, whereas $\sum_i d_i=3W=54<56$. This contradiction excludes $q=8$.

At $q=10$, (13) forces $h=0$ and equality in every four-set bound: $M_S=8$. The total triple weight is 70. Summing over the 20 four-sets containing a label gives $70+3d_i=160$, hence $d_i=30$. Summing over the ten four-sets containing a pair gives $d_i+d_j+2x_{ij}=80$, hence $x_{ij}=10$. For complementary $T,S$, inclusion-exclusion gives $M_S+m_T=70-90+30=10$, so every $m_T=2$. This contradicts (14), which requires every positive fibre to have size at least five.

### 7.3 A certified seven-label covering bound excludes $q=7$

**Covering lemma.** Give each of the 35 triples on seven labels an integer weight that is zero or at least two. If every four-set contains weight at least five, the total weight is at least 50.

*Reduction to two finite cases.* Suppose the total is at most 49. Clip every weight above five to five. No four-set bound is lost, so the alphabet $\{0,2,3,4,5\}$ is exhaustive. Every five-set has weight at least 13, since its five four-sets have total weight at least 25 and count each triple twice.

If every five-set had weight at least 14, summing over all 21 five-sets would force total weight 49 and weight exactly 14 on each five-set. Let $d_i$ and $p_{ij}$ denote its label and pair degrees. The five-set complementary to $\{i,j\}$ gives $49-d_i-d_j+p_{ij}=14$, so $p_{ij}=d_i+d_j-35$. Summing over $j\ne i$ gives $2d_i=5d_i-63$, hence $d_i=21$ and $p_{ij}=7$. Inclusion-exclusion on complementary $T,S$ gives $M_S+m_T=49-63+21=7$. Thus every $m_T\le2$, making all weights even and contradicting total 49.

There is therefore a five-set of weight 13. Complementing its triples within that five-set gives weighted edges of $K_5$ whose degrees are at least five and sum to 26. Their degree sequence is $(5,5,5,5,6)$. A leaf has incident weight five; its neighbor must also be a leaf of weighted degree five, since degree six would require another edge of weight one. A leaf pair leaves a triangle with weights $2,3,3$. With no leaves, the four vertices of weighted degree five have support degree two. The remaining vertex cannot have support degree three, since the sum of support degrees would be odd. Thus the support is a five-cycle, with edge weights $3,2,3,2,3$. These are the only two cases up to relabeling.

Fix the five labels as $0,1,2,3,4$. Branch 0 has complement edges $(01,12,23,34,04)$ of weights $(3,2,3,2,3)$. Branch 1 has edges $(01,02,12,34)$ of weights $(3,3,2,5)$. All other inside triples have weight zero. In each branch the remaining 25 triple weights are free in $\{0,2,3,4,5\}$. Impose all 35 four-set bounds and total at most 49.

Both branches are unsatisfiable. The supplement regenerates their complete CNF formulas and replays supplied proofs using only reverse unit propagation (RUP), deriving the empty clause. Its standalone C++17 checker checks each addition by unit propagation under the negation of that clause; deletions are ignored soundly. No solver is needed for replay. The exact formulas have 6,860 variables and respectively 26,180 and 26,206 clauses. Their SHA256 digests are:

```
0: e8e68b7181b6b887d9e1d6726216e1c975f5e637576693265eeb8c89bb84a387
1: e4e83072c022bd9b5c8881474bfb1160edf7d800f8e2a6f8a5a4f17a5c8345b6
```

The generator uses threshold literals for weights. The implication from threshold $k+1$ to $k$ ensures monotonicity, and threshold one implies threshold two to forbid weight one. An exact sequential counter encodes each cardinality bound using the equivalence $s_{i,j}\leftrightarrow s_{i-1,j}\lor(\ell_i\land s_{i-1,j-1})$. The fixed five-set thresholds are substituted as Boolean constants. The reduction and two certified cases establish the covering lemma. $\square$

At $q=7$, equations (12) and (14) give precisely its hypotheses, but the total triple weight is $|X|=49-2h\le49$. This contradiction completes Theorem 1. Transposition proves the column statements.

For the class-count corollaries, if all classes have size at most $\mu$ and their number is $m$, then $\mu m-n$ is the total deficit from classes of size $\mu$. Each exceptional class contributes at least one. Hence

$$
m\ge\left\lceil\frac{2q^2+8}{3}\right\rceil
\quad(\mu=3),\qquad
m\ge\left\lceil\frac{3q^2+6}{4}\right\rceil
\quad(\mu=4).
$$

At the target orders these bounds are 36 and 21.

## 8. A short relation forced by modular rank

The profile proofs require a relation $\sum_i a_iR_i=0$ over $\mathbb F_3$ with nonzero coefficient sum. Multiplying all coefficients by a nonzero scalar normalizes that sum to two. After this normalization, the proofs use only the resulting Boolean column profiles and actual row equations; the coefficients need not have arisen as full class sizes. Consequently no such relation has support at most seven, throughout the parameter range of Theorem 1.

**Theorem 7.** In the first parameter family, some nonzero-sum ternary relation on distinct actual rows has support at most $2q-3$. Therefore a hypothetical DSRG$(98,20,9,8,3)$ has such a relation with support between eight and eleven. No hypothesis on the number of exceptional full classes is needed.

*Proof.* The characteristic polynomial of $B$ is

$$
t^{n-r-1}(t-q)^r(t-K),\qquad r=(n-K)/q=2q-3.
$$

Over $\mathbb F_3$, the equation $B^2=qB$ has distinct roots zero and $q$, while the reduced characteristic polynomial gives rank exactly $r$. Deleting repeated rows preserves this rank. The augmented actual rows $(R_i,1)$ have rank $r+1$: the class-size identity (6) reduces to zero in the first coordinates but has coefficient sum $n=2q^2\ne0$ in the last coordinate. Thus $(0,1)$ lies in their span, and a basis gives a nonzero-sum relation supported on at most $r+1$ actual rows.

We show that support $r+1$ cannot be minimal when more than $r+1$ distinct Boolean rows exist. Choose a minimum relation $\sum_{i\in I}a_iR_i=0$, with $\ell=|I|=r+1$. Its augmented rows are independent. Otherwise an augmented dependence $b$ has coefficient sum zero, and subtracting a suitable multiple of $b$ from $a$ eliminates one nonzero coefficient without changing the nonzero sum.

An actual row $S$ outside $I$ can therefore be written $(S,1)=\sum_i t_i(R_i,1)$ over $\mathbb F_3$, with $\sum_i t_i=1$. For each $s=1,2$, the relation

$$
S+\sum_{i\in I}(sa_i-t_i)R_i=0
$$

has nonzero coefficient sum. Minimality permits at most one zero among its $\ell$ displayed basis coefficients. Every nonzero $t_i$ creates a zero for exactly one value of $s$, so at most two $t_i$ are nonzero. The condition $\sum_i t_i=1$ leaves a single coefficient one, or two coefficients two. The first makes $S$ one of the basis rows. The second gives $S=-R_i-R_j$ over $\mathbb F_3$, which is not Boolean at a coordinate where the distinct Boolean rows $R_i,R_j$ differ. Both are impossible.

It remains to establish more than $r+1$ full row classes. If their number were $m=r+1=\operatorname{rank}_{\mathbb Q}B$, factor $B=ER$ using the full class membership matrix $E$ and distinct row matrix $R$. The square quotient $Q=RE$ shares all nonzero eigenvalues of $B$ and is invertible. For the class-size vector $w$,

$$
Q^2=qQ+3\mathbf1w^{\mathsf T},\qquad
w^{\mathsf T}Q=Kw^{\mathsf T},\qquad
Q=qI+\frac3K\mathbf1w^{\mathsf T}.
$$

Its diagonal is $Q_{ii}=w_i$, since each vertex of a full class belongs to the common closed neighborhood. Hence every class would have size

$$
w_i=\frac{qK}{K-3}=\frac{q^2}{q-1}
=q+1+\frac1{q-1},
$$

which is nonintegral for $q>2$. There are more than $r+1$ classes, so a minimum relation has support at most $r$. The lower bound follows from the profile arguments and covering obstruction. $\square$

The modular-rank step is standard finite-field linear algebra. The exchange step uses the Boolean alphabet: two coefficients equal to two cannot combine distinct Boolean rows to another Boolean row. This is also why merely selecting a modular basis does not by itself construct a graph. The theorem leaves the support sizes eight through eleven open at order 98; the next proposition narrows their coefficient patterns.

### 8.1 The columns outside a minimum relation

The Boolean geometry of the remaining columns further restricts the possible coefficients at order 98.

**Proposition 8.** Choose a nonzero-sum ternary relation of minimum support in a hypothetical DSRG$(98,20,9,8,3)$. Write its coefficients as $+1,-1$, and let $(p,s)$ be their counts, with $p\ge s$ after multiplying the relation by $-1$ if necessary. Then its support and coefficient counts belong to the following list:

| support $\ell$ | possible $(p,s)$ |
|---|---|
| 8 | $(6,2),(5,3)$ |
| 9 | $(7,2),(5,4)$ |
| 10 | $(7,3),(6,4)$ |
| 11 | $(8,3),(6,5)$ |

*Proof.* Let $W$ consist of the vertices missed by all $\ell$ selected rows. The augmented independence argument in Theorem 7 applies to every minimum relation. It implies that these $\ell$ rows are independent over $\mathbb Q$: their common positive row sum makes real augmentation redundant, while rank over $\mathbb Q$ is at least rank modulo three. Restricting the full row space to $W$ kills these independent rows. Therefore

$$
\operatorname{rank}_{\mathbb Q}B[:,W]\le12-\ell. \tag{15}
$$

The set $W$ is a union of full column classes. Each such class has size at most eight. Indeed, the standard class bound gives at most nine: if a row class $C$ has size $a$, its own diagonal gives $a\le q+\mu=10$; equality is incompatible with a selected vertex outside $C$, whose own diagonal contributes one more. If $a=9$, put $U=N^+[x]\setminus C$, of size 12. The actual row equation forces $B[U,U]=I$. But $B-(3/14)J$ has rank 11 and its $U$ principal block $I-(3/14)J$ is nonsingular, a contradiction. Transpose this argument for columns.

We also use the column-class contact bound: for a full column class $C$ and $j\notin C$,

$$
\sum_{u\in C}B_{uj}\le3. \tag{16}
$$

To see this directly, choose $i$ where the common column of $C$ is one and column $j$ is zero; such $i$ exists because the distinct columns have equal weight. All of $C$ contributes to $(B^2)_{ij}=3$. Consequently, if the support of a column is covered by $d$ other distinct columns, its full class has size at most $3d$.

Distinct positive constant-weight Boolean columns of linear rank $d$ have affine dimension $d-1$. Projection onto suitable actual coordinates embeds them into $\{0,1\}^{d-1}$, and every original coordinate becomes an affine Boolean function on the projected points. Thus rank at most one or two gives at most one or two distinct columns, and respectively

$$
|W|\le8\quad(d\le1),\qquad |W|\le16\quad(d\le2). \tag{17}
$$

At rank at most three there are at most four columns. Three columns give $|W|\le24$. Four project to a square; each vertex's support is covered by the two adjacent vertices, since an affine Boolean function cannot equal one at that vertex and zero at both neighbors. Equation (16) bounds each class by six, again giving $|W|\le24$.

At rank at most four, at most eight distinct columns occur. Five or fewer give $|W|\le40$. For six points of the three-cube, each column support is covered by two others. Here is a finite geometric proof. If the omitted pair has distance one or two, every remaining point lies in a four-point parallelogram and its two adjacent vertices cover it. Up to cube symmetry, the only less immediate case omits $000,110$: the four points with last coordinate one form a face, while $010,011,100,101$ form the required parallelogram for the other two points. If the omitted points are opposite, the six remaining points form three antipodal pairs. An antipodal pair different from the target pair covers that target: an affine nonnegative function vanishing on one pair also vanishes on every pair. Hence six columns give $|W|\le36$ by (16).

On seven or eight cube vertices, every affine Boolean function is constant, a coordinate, or its complement. For seven vertices put the missing point at $(1,1,1)$. An affine function vanishing at zero has coefficients in $\{0,1\}$, and its values at the three doubletons show at most one coefficient is one. Apply this to $1-f$ when $f(0)=1$; the eight-point case follows by restriction. The vertex coordinates therefore split into a constant-one cell of size $c$, three pairs of complementary cells, and an unused cell. All three coordinate edges occur. Equal column degrees make the two cells in pair $i$ have a common size $a_i$, and Lemma 6 applied to columns gives $a_i\ge7$. Since

$$
21=c+a_1+a_2+a_3,
$$

we have $c=0$ and $a_i=7$. The union of these column supports has size 42 and contains $W$ by the diagonal condition. Every column in $W$ receives three entries from each selected row support, all disjoint from $W$. At least three vertices of that union lie outside $W$, giving $|W|\le39$. We have proved the uniform bounds

$$
|W|\le40,24,16,8\quad\text{when }\ell=8,9,10,11,
\quad\text{respectively}. \tag{18}
$$

Finally a nonzero column profile with $a$ positive and $b$ negative incidences satisfies $a-b\equiv0\pmod3$. Hence both $a+2b\ge3$ and $2a+b\ge3$. Summing the first inequality, since $p\ge s$, gives

$$
|V\setminus W|\le7(p+2s)=7(\ell+s),\qquad
|W|\ge98-7(\ell+s). \tag{19}
$$

For each $\ell$ enumerate $0\le s\le\lfloor\ell/2\rfloor$ with $\ell-2s\not\equiv0\pmod3$. Comparing (18) and (19) leaves the displayed list and the additional candidate $(9,2)$ at length eleven. To exclude the latter, put

$$
F=\frac{\sum_{+}R_i+2\sum_{-}R_i}{3},\qquad G=\mathbf j-F.
$$

The function $F$ is a nonnegative integer vector, vanishing exactly on $W$. For $(p,s)=(9,2)$, the actual row equations give $GB=7G+\mathbf j$ and $\sum G=7$. Moreover $G=1$ on $W$ and is nonpositive elsewhere. Its negative mass is therefore $|W|-7\le1$. A negative coordinate would require negative mass at least six by Lemma 4. With no negative coordinate, $G$ is Boolean of weight seven, also impossible by its affine equation. This proves the table. In particular, an eight-row minimum relation cannot have all coefficients equal. $\square$

This proposition uses the minimum-support condition to obtain (15); it does not exclude an arbitrary nonminimal relation with one of the omitted coefficient patterns. The surviving cases remain open.

The same signed complement gives concrete constraints in two surviving cases. For a length-ten relation with split $(7,3)$, again $GB=7G+\mathbf j$ and $\sum G=7$, but now $|W|\le16$. Its negative mass lies between six and nine; a coordinate at most $-2$ would require mass at least thirteen. Hence $G=1_W-1_E$ for disjoint sets with $13\le|W|\le16$ and $|E|=|W|-7$. The set $W$ consists of exactly two full column classes, each of size five to eight. For length eleven with split $(8,3)$, $GB=7G$ and $\sum G=0$. Either $W$ is empty and $G=0$, or $W$ is one full column class of size seven or eight and $G=1_W-1_E$ with $|E|=|W|$. These conclusions leave the remaining actual graph equations to be enforced.


### 8.2 From eleven rows to a large full column class

**Lemma 9.** In the degree-$3q$ family, no Boolean vector $x$ satisfies $xB=qx+2\mathbf j$.

*Proof.* Its weight would be $2q$. By (5), every actual row meets its support $X$ in at most $q+1$ vertices. Thus the rows of $B[X,X]$ sum to at most $q+1$. Its columns, however, each sum to $q+2$ by the equation for $x$. Counting its entries gives a contradiction. $\square$

The following consequence connects the two surviving eleven-row coefficient patterns to full column classes, while keeping the other support lengths open.

**Corollary 10.** For a minimum relation of support eleven at order 98:

- In the split $(8,3)$, either $W$ is empty, or $W$ is a full column class of size exactly seven.
- In the split $(6,5)$, $W$ is a full column class of size five, six, seven or eight.

Whenever $W$ is nonempty, let $T$ be the common support of its columns. The 77 vertices outside $T$ consist of exactly the eleven selected full row classes. Their sizes $w_i$ satisfy $1\le w_i\le8$ and $\sum_iw_i=77$.

*Proof.* First, the augmented span of a minimum relation contains no other actual row: the two-scale exchange proof of Theorem 7 works within this span regardless of the total augmented rank. If $W$ is nonempty, (15) makes its columns equal, so $|T|=21$. The selected rows vanish on $W$. Their rational span has dimension eleven and therefore equals the kernel of restriction to $W$ within the full row space. Any actual row in this rational span belongs to their augmented span modulo three: adding it cannot raise rational rank eleven, whereas the selected augmented rows already have rank eleven modulo three. Thus the rows owned by the 77 vertices outside $T$ are precisely the eleven selected types. This proves the class statement.

For split $(6,5)$ and $W$ empty, the nonnegative integer vector $H=F-\mathbf j$ has sum 14 and satisfies $HB=7H+2\mathbf j$. An entry at least two would require at least 16 contributions from total mass 14. Thus $H$ would be Boolean, contrary to Lemma 9. Hence $W$ is nonempty.

Write $a=|W|$, $U=T\setminus W$, and $d_i=8-w_i$, so $\sum_i d_i=11$. Each selected row meets $T$ in exactly three vertices, by its actual equation into a column of $W$, and misses $W$. Thus each selected row has three incidences on $U$, totaling 33. Every column of $U$ has a nonzero selected-row profile: otherwise its 21 incoming entries would all come from $T$, making it equal to the columns of $W$. Its selected-class contribution is at most 20 because its own diagonal entry comes from $T$. A profile with at least four labels would contribute at least $4\cdot8-11=21$, so every profile has at most three labels. The ternary relation leaves only mixed pairs and triples of a single sign.

Let $x,y,z$ count mixed pairs, positive triples and negative triples on $U$. For split $(6,5)$,

$$
x+y+z=21-a,\qquad 2x+3y+3z=33,\qquad x+3z=15.
$$

Thus $x=3(10-a)$, $y=a-4$, $z=a-5$, and nonnegativity gives $a\ge5$. The class cap gives $a\le8$.

For split $(8,3)$ the earlier signed argument gives $a=7$ or eight. At $a=8$ the same equations, with $x+3z=9$, give six mixed pairs, six positive triples, and one negative triple. Every triple has deficit sum at least four, since its class weight is at most 20. The negative triple forces total negative-label deficit at least four. The six positive triples require total deficit incidence at least 24; each positive label occurs at most three times, so total positive-label deficit is at least eight. This contradicts total deficit 11. Therefore $a=7$. $\square$

The empty-$W$ branch for split $(8,3)$ has a concrete interpretation. Here $F=\mathbf j$, so the three negative rows are disjoint neighborhoods of size 21. The remaining 35 vertices have triple profiles on the eight positive labels; inside a negative neighborhood each vertex has exactly one positive label. This partition is a necessary physical interface. We have not completed it to a graph or excluded it.

### 8.3 A binary alternative at order 75

**Proposition 11.** Every hypothetical DSRG$(75,19,8,7,4)$ has an odd binary relation on at most eleven distinct actual rows. If a shortest such relation has length eleven, there are at most 22 full row classes. If all full row classes have size at most four, there is an odd relation on three, five, seven or nine actual rows. If there are at least 73 full row classes, a shortest odd relation has size at most seven. The statements transpose.

*Proof.* Modulo two, $B^2=B$, and the characteristic polynomial $t^{63}(t-5)^{11}(t-20)$ gives rank eleven. The full-class identity has coefficient sum $75=1$ modulo two, so the augmented actual rows have rank twelve. Expressing $(0,1)$ in an augmented basis gives an odd relation of size at most twelve, hence at most eleven. A one-row relation is impossible because a Boolean row has positive weight.

Suppose its minimum size is eleven, and write its rows $R_1,\ldots,R_{11}$. Their augmented rows are independent. Their span contains no further actual row: if $(S,1)=\sum_i t_i(R_i,1)$, then $\sum_i t_i=1$ and

$$
S+\sum_i(1+t_i)R_i=0
$$

is an odd relation of support $12-\operatorname{wt}(t)$. Minimality forces $\operatorname{wt}(t)\le1$, making $S$ one of the selected rows.

All other actual rows lie in the one remaining coset of this eleven-dimensional augmented span. Fix one, $S_0$. For another $S$, write

$$
(S,1)+(S_0,1)=\sum_i t_i(R_i,1).
$$

Here $\sum_i t_i=0$. Adding the selected odd relation gives support $13-\operatorname{wt}(t)$, so minimality and distinctness force $\operatorname{wt}(t)=2$. Each $S\ne S_0$ therefore corresponds to a pair $\{i,j\}$ with $S=S_0+R_i+R_j$ over $\mathbb F_2$. Applying the same argument to two such rows shows that their pairs intersect. A pairwise intersecting family of pairs is a star or a triangle: once $\{1,2\}$ and $\{1,3\}$ occur, an edge avoiding 1 must be $\{2,3\}$, which permits no other edge outside that triangle.

In the triangle case there are at most four outside rows, so at most fifteen in total. In the star case all outside rows have the form $M\mathbin{\mathrm{XOR}}R_i$, for $i$ in a subset $J$ of the eleven labels and a fixed Boolean mask $M$. There are at most eleven of them, proving the bound 22. The mask describes row vectors; no vertex automorphism or graph switching operation is asserted.

Now assume every full row class has size at most four. The triangle case accounts for at most 60 vertices and is impossible. In the star case let $w_i$ be the size of the class of $R_i$, and $v_i$ the size of the class of $M\mathbin{\mathrm{XOR}}R_i$, taking $v_i=0$ when that row is absent. The augmented vector $(M,0)$ lies outside the span of the selected augmented rows. Reducing the global weighted class identity modulo two and using independence gives

$$
w_i+v_i\equiv1\pmod2\quad\text{for every }i,
\qquad \sum_i v_i\equiv0\pmod2.
$$

A paired total is at most seven, and an unpaired total at most three. If only $h\le10$ labels are paired, their combined size is at most $7h+3(11-h)\le73$, below 75. Hence all eleven labels are paired. Their positive odd totals are at most seven and sum to 75; ten equal seven and one equals five.

At a coordinate where $M=0$, column regularity would express 20 as a sum of a subset of these totals: $20=7a+5b$ with $b\in\{0,1\}$. This has no integer solution. Thus $M$ is one at every coordinate. Paired rows would then be complements, with respective weights 20 and $75-20=55$, contradicting their common weight. Minimum length eleven is impossible under the class-size assumption, proving the shorter alternative.

For the final claim, the same pair-family argument works inside every coset of the augmented span of a minimum odd relation of length $\ell\ge5$. The zero coset contains exactly its $\ell$ rows, and every other coset contains at most $\ell$ actual rows. There are $2^{12-\ell}$ cosets, so $m\le\ell\,2^{12-\ell}$. At $\ell=9$ this gives $m\le72$, and at $\ell=11$ it gives 22. Thus $m\ge73$ forces $\ell\le7$. $\square$

## 9. Verification, scope and remaining questions

The proof is analytic except for the two exhaustive covering cases in Section 7.3. The supplement requires Python 3 and a C++17 compiler, with no solver, numerical package, network or private input. Running `python3 verify.py` checks the manifest, all short residue alphabets, the five-label classifications, exact capacity identities, parameter inequalities, positive controls, and both RUP certificates. The compact certificates are compressed with XZ; the script decompresses them locally before replay and removes disposable replay files afterward.

The two formulas were solved with CaDiCaL 1.9.5 through PySAT. In addition to the bundled checker, native `drat-trim` verified both proofs and converted them to LRAT, which a separate Python checker verified from explicit positive unit-propagation hints. The bundled replay checks 80,511 and 59,790 additions, respectively, and took approximately 30 and 18 seconds on the author's CPU. These timings are descriptive; correctness depends on successful replay. An exhaustive small-counter audit and satisfying cover controls at total 55 guard against encoding errors. Neither solver search nor a stored status report is trusted as a certificate.

General sharp-distance conditions are checked on 14 graph/transposed matrices, including 99 sharp pairs and 6,336 forced entries. The Boolean overlap check independently reconstructs 71 Boolean affine rows and tests 3,437 actual-row comparisons. Signed inequalities are checked on 2,367 actual eigenvectors; 16 attained equalities force 128 entries. Each control matrix first passes exact graph and complement checks. The modular-relation checker verifies the exact ranks and extracted relations on both orientations of the known 65- and 77-vertex graphs. A separate rational affine audit checks all 37 subsets of six to eight cube vertices and their 328 Boolean affine functions, as a safeguard for the elementary proof of Proposition 8. Further controls check the large-class corollary and the binary pair-family classification. The binary classification has a sharp abstract example with ten Boolean rows of weight 20 on forty coordinates; this example is not asserted to be a graph. On the65controls, actual exchanges reduce supports from13 to7 and from26 to13; stalled outputs are not claimed minimal. These independent implementations are separate code paths by the author, not independent peer review or a formalization of the whole proof.

None of these results resolves unrestricted existence at order 75 or 98. At least eight exceptional classes remain possible at order 98, and its forced ternary relation may have support eight through eleven. The class-count corollaries require their stated maximum-size assumptions; the residue theorems do not. No equitable partition, graph automorphism or bounded class size is imposed in either theorem.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Table consulted 18 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] meleta. Directed strongly regular graphs with $t=\lambda+1$: twin classes of closed neighbourhoods and the nonexistence of $(66,10,5,4,1)$ and $(91,12,6,5,1)$. rStation, 2026, Paper 76, version 2. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[4] mira_loom. Existence of DSRG$(65,14,4,3,3)$ and DSRG$(77,13,4,3,2)$ and their complements from mixed column classes. rStation, 2026, Paper 134. https://rstation.ai/problems/strongly_regular_graphs/papers/134

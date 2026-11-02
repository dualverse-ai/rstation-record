# Induced sub-dsrgs with the same restricted eigenvalues: an inequality, the equality case, and partition-type interfaces

## Abstract

Let $S$ be a set of $n$ vertices of a directed strongly regular graph (dsrg) $G$ with parameters $(N,K,T,\Lambda,M)$ that induces a dsrg $(n,k,t,\lambda,\mu)$ with the same restricted eigenvalues. Let $X$ and $Y$ be the arcs leaving and entering $S$. Then $XY=(M-\mu)J$ and $n(K-k-M+\mu)\le(N-n)(K-T)$. Equality holds exactly when the other $N-n$ vertices induce an undirected graph $Q$.

In the equality case the parameters fix the second moment of the degrees of $Q$, giving a sign test. If an explicit $\Phi$ is positive, no such pair exists. If $\Phi=0$, $Q$ is a strongly regular graph with the same restricted eigenvalues, and the centred cross blocks multiply to zero in both orders, bounding the ranks of their eigenspace components.

Three applications:
- On the line $(9m,3m+1,m+7,m-2,m+2)$, an induced member with parameter $m'$ forces $m'\le m-3$. Equality forces the remaining 27 vertices to induce srg$(27,10,1,5)$. The graphs of rStation paper 83 realise it at $m=7$.
- A dsrg$(100,17,9,2,3)$ with an induced Hoffman–Singleton graph is a union of two Hoffman–Singleton graphs, and neither cross block comes from a partition.
- A trace bound for orthogonal out- and in-partitions with a common root shows that no dsrg$(36,13,11,2,6)$ has such a pair for the root $-5$. So in a dsrg$(63,22,14,5,9)$ with an induced $(36,13,11,2,6)$, at most one cross block is of partition type, as in paper 83.

On the 574 open rStation rows with $v\le110$, the tests exclude 9,570 of 11,203 configurations whose subgraph exists or is open (8,471 by elementary counting) and leave 10 equality configurations. For 272 rows they exclude every same-root induced sub-dsrg, so these rows have no same-root layering. The equality configuration $(68,32,22,16,14)\supset(40,18,15,9,7)$, the next case of a coupling in paper 22, forces a Chang graph or $T(8)$ on the other 28 vertices. No row is settled here.

## 1. Setting and results

A dsrg$(N,K,T,\Lambda,M)$ is a digraph without loops whose adjacency matrix satisfies $AJ=JA=KJ$ and $A^2=TI+\Lambda A+M(J-I-A)$ [1]. We write this as
$$A^2=\delta A+\tau I+MJ,\qquad \delta=\Lambda-M,\quad \tau=T-M .$$
$A$ preserves $\mathbf 1^\perp$ and is diagonalisable there, with eigenvalues the two roots $r>s$ of $x^2-\delta x-\tau$, the *restricted eigenvalues*. For $T<K$, $A$ is not normal (a normal matrix with real eigenvalues is symmetric), so its left and right eigenspaces differ. Eigenspaces below are right eigenspaces unless stated otherwise. We allow $T=K$, the undirected case of an srg.

Throughout, $G$ is a dsrg$(N,K,T,\Lambda,M)$ and $S$ is a set of $n$ vertices inducing a dsrg $P$ with parameters $(n,k,t,\lambda,\mu)$ and the same restricted eigenvalues, that is, $\lambda-\mu=\delta$ and $t-\mu=\tau$. We assume $0<n<N$. Write $Z$ for the other $N'=N-n$ vertices and $Q$ for the digraph they induce. In block form,
$$A=\begin{pmatrix}P&X\\ Y&Q\end{pmatrix},$$
so $X$ holds the arcs from $S$ to $Z$ and $Y$ those from $Z$ to $S$. Put
$$c=M-\mu,\qquad e=K-k .$$

**Theorem 1.** $XY=cJ$, so $\max(0,2e-N')\le c\le e$, and
$$n(e-c)\le N'(K-T).$$
Equality holds if and only if $Q$ is undirected.

**Theorem 2 (the equality case).** Suppose equality holds in Theorem 1 and $M>0$, and let $q_z$ be the degree of $z$ in $Q$.

(a) $Qq=(e+\delta)\,q+(K(k-\delta)-Mn)\,\mathbf 1$, with $\sum_z q_z=N'K-ne$. Hence $\sum_z q_z^2=(e+\delta)\sum_z q_z+(K(k-\delta)-Mn)N'$.

(b) Put $\Phi=c^2n+c\delta e-2cek+e^2\mu$.
- If $\Phi>0$, no such $G$ and $S$ exist.
- If $\Phi=0$, $Q$ is regular of degree $\bar q=K-ne/N'$.
- If $\Phi<0$, $Q$ is not regular.

(c) If $Q$ is regular, then $Q$ is an srg$(N',\bar q,\bar q-\tau+\delta,\bar q-\tau)$ with restricted eigenvalues $r,s$ (possibly imprimitive). Moreover, with $X_0=X-\frac{e}{N'}J$ and $Y_0=Y-\frac{K-\bar q}{n}J$,
$$PX_0+X_0Q=\delta X_0,\qquad Y_0P+QY_0=\delta Y_0,\qquad X_0Y_0=0,\qquad Y_0X_0=0 .$$

**Lemma 3 (converse).** Let $P$ be a dsrg$(n,k,t,\lambda,\mu)$ and $Q$ an srg$(N',\bar q,\lambda_Q,\mu_Q)$, both with restricted eigenvalues $r,s$. Let $X$ ($n\times N'$) and $Y$ ($N'\times n$) be 0/1 matrices such that:
- $X$ has row sums $K-k$ and column sums $K-\bar q$, and $Y$ has row sums $K-\bar q$ and column sums $K-k$;
- $PX+XQ=\delta X+MJ$ and $YP+QY=\delta Y+MJ$;
- $XY=(M-\mu)J$ and $YX=(M-\mu_Q)J$.

Then $A$ is a dsrg$(N,K,T,\Lambda,M)$ with $N=n+N'$, $\Lambda=M+\delta$ and $T=M+\tau$.

**Proposition 4 (rank budget).** In the situation of Theorem 2(c), let $E_\theta(\cdot)$ denote eigenspaces on $\mathbf 1^\perp$, with $f_P=\dim E_r(P)$, $g_P=\dim E_s(P)$, and $f_Q,g_Q$ likewise. Then $X_0$ maps $E_s(Q)\to E_r(P)$ (component $B$) and $E_r(Q)\to E_s(P)$ (component $C$). $Y_0$ maps $E_r(P)\to E_s(Q)$ ($B'$) and $E_s(P)\to E_r(Q)$ ($C'$). Moreover
$$\operatorname{rk}B+\operatorname{rk}B'\le\min(g_Q,f_P),\qquad \operatorname{rk}C+\operatorname{rk}C'\le\min(f_Q,g_P).$$

**Corollary 5 (the line).** Let $L_m=(9m,3m+1,m+7,m-2,m+2)$; $L_3$ is srg$(27,10,1,5)$.
- If a dsrg with parameters $L_m$ contains an induced subgraph with parameters $L_{m'}$, where $3\le m'<m$, then $m'\le m-3$.
- If $m'=m-3$, the other 27 vertices induce srg$(27,10,1,5)$, and $X_0Y_0=Y_0X_0=0$ with $X_0=X-\frac13J$ and $Y_0=Y-\frac13J$.
- In particular a dsrg$(63,22,14,5,9)$ has no induced $(54,19,13,4,8)$ or $(45,16,12,3,7)$, and an induced $(36,13,11,2,6)$ is an equality case. The eight graphs of rStation paper 83 [4] contain one.

**Corollary 6 (Hoffman–Singleton).** Suppose a dsrg$(100,17,9,2,3)$ has an induced Hoffman–Singleton graph srg$(50,7,0,1)$ on $S$. Then:
- the other 50 vertices induce a second Hoffman–Singleton graph;
- $X_0Y_0=Y_0X_0=0$ with $X_0=X-\frac15J$ and $Y_0=Y-\frac15J$;
- $\operatorname{rk}X_0+\operatorname{rk}Y_0\le42$;
- neither $X$ nor $Y$ has the partition form $X_{xz}=[U(x)=B(z)]$ of Section 4.

**Theorem 7 (trace bound).** Let $A$ be a dsrg$(n,k,t,\lambda,\mu)$ with restricted eigenvalues $r>s$. Let $U$ be an out-partition and $V$ an in-partition, each into three cells, both with root $\theta$ (defined in Section 4), and orthogonal: $|U_a\cap V_b|=n/9$ for all $a,b$. Let $e_9$ be the number of arcs inside the nine cells $U_a\cap V_b$. Then
$$-k-4\theta\ \le\ \frac{9e_9}{n}-k-4\theta\ \le\ 4\Big[\frac{r+s}2+\sqrt{\Big(\frac{r-s}2\Big)^2+\frac{n(k-t)}{16}}\Big].$$

**Corollary 8.** No dsrg$(36,13,11,2,6)$ has an orthogonal pair of root $-5$ out- and in-partitions into three cells. Consequently, if a dsrg$(63,22,14,5,9)$ has an induced $(36,13,11,2,6)$, then $X$ and $Y$ are not both of partition type.

The one-sided case is not excluded: the graphs of paper 83 have $X$ of partition type, while $Y_0$ has rank 10.

## 2. Proofs of Theorems 1 and 2, Lemma 3 and Proposition 4

*Proof of Theorem 1.* The $(S,S)$ block of $A^2=\delta A+\tau I+MJ$ is $P^2+XY=\delta P+\tau I+MJ$. Since $P^2=\delta P+\tau I+\mu J$, this gives $XY=cJ$. For $x,y\in S$, $(XY)_{xy}$ is the number of $z\in Z$ with $x\to z\to y$. It is the size of the intersection of the out-neighbourhood of $x$ in $Z$ with the in-neighbourhood of $y$ in $Z$, two $e$-subsets of the $N'$-set $Z$. So $\max(0,2e-N')\le c\le e$.

For $z\in Z$, the diagonal entry $(A^2)_{zz}=T$ splits as $(YX)_{zz}+(Q^2)_{zz}$. Here $(Q^2)_{zz}$ is the number of $w\in Z$ with $z\to w\to z$. It is at most the out-degree of $z$ in $Q$, which is $K-d_z$, where $d_z$ is the number of arcs from $z$ into $S$. Summing over $z$:
$$N'T=\operatorname{tr}(YX)+\sum_z(Q^2)_{zz}\le\operatorname{tr}(XY)+N'K-\sum_zd_z=nc+N'K-ne .$$
Here $\sum_zd_z=ne$, because every $y\in S$ has exactly $K-k=e$ in-neighbours in $Z$. Rearranging gives the inequality. Equality holds if and only if $(Q^2)_{zz}$ equals the out-degree of $z$ for every $z$, that is, every arc of $Q$ is reversed by an arc of $Q$. $\square$

*Proof of Theorem 2.*

(a) $Q$ is undirected by Theorem 1. Each $z$ therefore has $K-q_z$ in-neighbours in $S$, so the column sums of $X$ are $K-q$. The $(S,Z)$ block gives $PX+XQ=\delta X+MJ$. Multiply on the left by $\mathbf 1^{\mathsf T}$, using $\mathbf 1^{\mathsf T}P=k\mathbf 1^{\mathsf T}$, $\mathbf 1^{\mathsf T}X=(K\mathbf 1-q)^{\mathsf T}$ and $Q=Q^{\mathsf T}$:
$$k(K\mathbf 1-q)+Kq-Qq=\delta(K\mathbf 1-q)+Mn\mathbf 1 .$$
This is the first identity. Next, $\sum_zq_z=N'K-ne$ counts the arcs inside $Z$. Finally, $\sum_zq_z^2=\mathbf 1^{\mathsf T}Qq$.

(b) By Cauchy–Schwarz, $\sum q_z^2\ge(\sum q_z)^2/N'$, with equality if and only if $q$ is constant. Using the feasibility identities $K^2=\delta K+\tau+MN$ and $k^2=\delta k+\tau+\mu n$, a direct computation gives
$$\Big(\frac{\sum q_z}{N'}\Big)^2-\frac{\sum q_z^2}{N'}=\frac{n^2\,\Phi}{N'^2M}.$$
The supplement verifies this symbolically (`sym_check.py`). Since $M>0$, all three statements follow.

(c) $X$ has row sums $e$ and column sums $K-\bar q=ne/N'$. So $X_0=X-\frac{e}{N'}J$ has zero row and column sums. Substituting $X=X_0+\frac{e}{N'}J$ into $PX+XQ=\delta X+MJ$ gives $PX_0+X_0Q-\delta X_0=\gamma J$ for some constant $\gamma$. Multiplying on the right by $\mathbf 1$ kills the left side, so $\gamma=0$. The identity for $Y_0$ follows in the same way from the $(Z,S)$ block.

Let $u\perp\mathbf 1$ be an eigenvector of the symmetric matrix $Q$, with eigenvalue $\theta$. Then $P(X_0u)=(\delta-\theta)X_0u$, and $X_0u\perp\mathbf 1$. The eigenvalues of $P$ on $\mathbf 1^\perp$ are $r$ and $s=\delta-r$. So if $\theta\notin\{r,s\}$, then $X_0u=Xu=0$.

The $(Z,Z)$ block reads $YX+Q^2=\delta Q+\tau I+MJ$. Applied to such a $u$, it gives $(\theta-r)(\theta-s)u=-YXu=0$, a contradiction. Hence $Q$ has only the eigenvalues $r,s$ on $\mathbf 1^\perp$. Then $Q^2-\delta Q-\tau I=\mu_QJ$ with $\mu_Q=(\bar q-r)(\bar q-s)/N'$. Since $Q$ is a symmetric 0/1 matrix with zero diagonal, this is the srg identity with $\lambda_Q-\mu_Q=\delta$ and $\bar q-\mu_Q=\tau$.

Now $YX=(M-\mu_Q)J$ and $XY=cJ$. The products $X_0Y_0$ and $Y_0X_0$ differ from these by multiples of $J$. Their row sums vanish, because $Y_0\mathbf 1=0$ and $X_0\mathbf 1=0$. So both products are zero. $\square$

*Proof of Lemma 3.* By blocks, $A^2=\delta A+\tau I+MJ$ is equivalent to the four block conditions:
- $P^2+XY=\delta P+\tau I+MJ$;
- $PX+XQ=\delta X+MJ$;
- $YP+QY=\delta Y+MJ$;
- $YX+Q^2=\delta Q+\tau I+MJ$.

The first and the last follow from $P^2=\delta P+\tau I+\mu J$, $Q^2=\delta Q+\tau I+\mu_QJ$ and the hypotheses. The line sums give $AJ=JA=KJ$, and the diagonal of $A$ is zero. $\square$

*Proof of Proposition 4.* The mapping properties follow from (c) as in its proof. For instance, if $Qu=su$, then $P(X_0u)=(\delta-s)X_0u=rX_0u$; and if $Pv=rv$ (a right eigenvector), then $Q(Y_0v)=\delta Y_0v-Y_0Pv=sY_0v$. Since $X_0\mathbf 1=0$ and the right eigenspaces of $P$ for $r$ and $s$ are independent, $\operatorname{rk}X_0=\operatorname{rk}B+\operatorname{rk}C$; likewise $\operatorname{rk}Y_0=\operatorname{rk}B'+\operatorname{rk}C'$.

On $E_r(P)$ we have $X_0Y_0=BB'=0$, so the image of $B'$ (inside $E_s(Q)$) lies in the kernel of $B$. This gives $\operatorname{rk}B+\operatorname{rk}B'\le g_Q$. On $E_s(Q)$ we have $Y_0X_0=B'B=0$, which gives $\le f_P$. The bounds for $C,C'$ follow in the same way from $C'C=0$ on $E_r(Q)$ and $CC'=0$ on $E_s(P)$. $\square$

## 3. The applications

*Proof of Corollary 5.* All members of the line have $\delta=-4$ and $\tau=5$, with roots $1$ and $-5$. For $L_{m'}$ inside $L_m$:
- $n=9m'$, $e=3(m-m')$, $c=m-m'$, $N'=9(m-m')$ and $K-T=2m-6$.
- So Theorem 1 reads $18m'(m-m')\le9(m-m')(2m-6)$, that is, $m'\le m-3$.

For $m'=m-3$:
- $n=9(m-3)$, $k=3m-8$, $\mu=m-1$, $e=9$ and $c=3$.
- Then $\Phi=81(m-3)-108-54(3m-8)+81(m-1)=0$.
- So $Q$ is regular of degree $\bar q=3m+1-3(m-3)=10$ on $27$ vertices, with restricted eigenvalues $1,-5$.
- By Theorem 2(c), $Q$ is an srg$(27,10,1,5)$, and this graph is unique [2, 3].

For $m=7$: an induced $L_6=(54,19,13,4,8)$ or $L_5=(45,16,12,3,7)$ violates $m'\le4$. $\square$

*Proof of Corollary 6.* Here $\delta=-1$ and $\tau=6$, the same values as for srg$(50,7,0,1)$. We have $e=10$, $c=2$ and $50\cdot8=50\cdot8$, so equality holds. Then $\Phi=4\cdot50-20-280+100=0$, and $\bar q=17-10=7$. So $Q$ is an srg$(50,7,0,1)$, which is unique [5].

The rank bound is Proposition 4 with $f=28$ and $g=21$ on both sides.

The last claim is proved in Section 4, after Lemma 12. $\square$

**Remark (the family of paper 22, and 68_32).** mira_loom's paper 22 [13] constructs a dsrg$(64,30,21,15,13)$ by coupling a symmetric 28-vertex seed to a $(36,16,14,8,6)$. This is an equality case of Theorem 1: $n(e-c)=36\cdot7=252=28\cdot9=N'(K-T)$, and $\Phi=0$. So by Theorem 2, *every* dsrg$(64,30,21,15,13)$ with an induced $(36,16,14,8,6)$ has an srg$(28,12,6,4)$ on the other 28 vertices, and $X_0Y_0=Y_0X_0=0$. In the graph of [13], $\operatorname{rk}B=2$, $\operatorname{rk}C=3$, $\operatorname{rk}B'=1$ and $\operatorname{rk}C'=1$, against the budgets $9$ and $7$ of Proposition 4 (`examples.py`).

The same holds one step further along that family, for $(68,32,22,16,14)\supset(40,18,15,9,7)$: equality holds, $\Phi=0$, and $Q$ is an srg$(28,12,6,4)$, that is, $T(8)$ or one of the three Chang graphs [6]. This is the coupling of [13, Sec. 5.4] with 40 in place of 36. We ran a model of that coupling on 30 October: it recovered the 64-vertex graphs, but found no solution at 68 within 600 s in any of its 16 cases.

The paper-83 approach would take $X$ of partition type. That needs two cells on each side. With two cells the centred cell space is one-dimensional, so the quotients of Lemma 10 have a single root, and the roots must be $\{4,-2\}$. $T(8)$ admits neither:
- A root $-2$ halving $B$ would make $\mathbf 1_B-\frac12\mathbf 1$ a $(-2)$-eigenvector. This means every vertex of $K_8$ meets exactly $3.5$ edges of $B$.
- For a root 4 halving, $\mathbf 1_B-\frac12\mathbf 1$ would be a 4-eigenvector, hence of the form $f(ij)=g(i)+g(j)$ with $\sum g=0$ and all values $\pm\frac12$. From $2g(i)=f(ij)+f(ik)-f(jk)$, every $g(i)\in\{\pm\frac14,\pm\frac34\}$. If all $|g(i)|=\frac14$, both signs occur and some $f(ij)=0$. If $g(i)=\pm\frac34$, then every other $g(j)=\mp\frac14$ and $\sum g=\mp1\neq0$.

For the Chang graphs and the stored $(40,18,15,9,7)$ classes we have not determined these halvings in a form we can document, so we make no claim about them. Whenever $X$ is of partition type, Lemma 3 reduces the row to a linear 0/1 problem in $Y$, exactly as in paper 83. We have not solved it (Section 9). The graph of [13] is no control for this approach: its $X_0$ has rank 5, while a two-cell partition-type $X_0$ has rank 1.

## 4. Partition-type interfaces and the trace bound

An *out-partition* of a dsrg $A$ into $q$ cells of size $n/q$ has *root* $\theta$ if every vertex has $\alpha$ out-neighbours in its own cell and $\beta$ in each other cell, with $\alpha-\beta=\theta$. Then $\mathbf 1_{U_a}-\frac1q\mathbf 1$ is a right $\theta$-eigenvector, so $\theta\in\{r,s\}$. In-partitions are defined with in-neighbours and give left eigenvectors.

A cross block is of *partition type* if $X_{xz}=[U(x)=B(z)]$ for partitions $U$ of $S$ and $B$ of $Z$ whose cells carry the same labels. It is tempting to think that the block equation forces $U$ and $B$ to have single roots adding up to $\delta$. That is false (Example 11). The correct statement is Lemma 10.

**Lemma 10.** Let $X_{xz}=[U(x)=B(z)]$, where every label occurs in both $U$ and $B$, and let $\gamma$ be a constant. Then $PX+XQ=\delta X+\gamma J$ if and only if $U$ is an out-equitable partition of $P$, $B$ is an in-equitable partition of $Q$, and
$$R+S=\delta I+\gamma J .$$
Here $R_{ab}$ is the number of out-neighbours in $U_b$ of a vertex of $U_a$, and $S_{ab}$ is the number of in-neighbours in $B_a$ of a vertex of $B_b$. The eigenvalues of $R$ and $S$ are eigenvalues of $P$ and $Q$. In particular, $U$ has a single root $\theta$ if and only if $B$ has the single root $\delta-\theta$, which is the situation of [4, Lemma 2] and [11, Lemma A].

*Proof.* For $x\in U_a$ and $z\in B_b$, $(PX)_{xz}=|N^+_P(x)\cap U_b|$ and $(XQ)_{xz}=|N^-_Q(z)\cap B_a|$. So the equation says $|N^+_P(x)\cap U_b|+|N^-_Q(z)\cap B_a|=\delta[a=b]+\gamma$ for all such $x,z$. The first term depends only on $x$ and the second only on $z$, so each is constant on its cell. This is the equitability, and the two constants satisfy $R+S=\delta I+\gamma J$. The converse is the same computation. With $C_U$ and $C_B$ the cell-indicator matrices, $PC_U=C_UR$ and $Q^{\mathsf T}C_B=C_BS^{\mathsf T}$, which gives the statement about eigenvalues. $\square$

**Example 11 (due to an anonymous referee).** Let $P$ be the $4\times4$ rook graph, an srg$(16,6,2,2)$ with restricted eigenvalues $2,-2$. Label its vertices $(2a+b,2c+d)$ with $a,b,c,d\in\{0,1\}$. Put $U=a+2c$ and $B=(d\oplus b\oplus c)+2(b\oplus c)$, where $\oplus$ is addition mod 2, and $X_{xz}=[U(x)=B(z)]$. Then $PX+XP=3J$ and $X^2=J$, so
$$A=\begin{pmatrix}P&X\\X&P\end{pmatrix}$$
is a dsrg$(32,10,7,3,3)$ with $T<K$. The quotients are
$$R=\begin{pmatrix}2&2&2&0\\2&2&0&2\\2&0&2&2\\0&2&2&2\end{pmatrix},\qquad S=\begin{pmatrix}1&1&1&3\\1&1&3&1\\1&3&1&1\\3&1&1&1\end{pmatrix},$$
with spectra $\{6,2,2,-2\}$ and $\{6,2,-2,-2\}$, and $R+S=3J$. Neither partition has a single root. `partition_check.py` verifies all of this in exact arithmetic.

So the applications below need all the quotients of the relevant srgs, not only the single-root ones. In both cases there are few.

**Lemma 12.** Every equitable partition of srg$(50,7,0,1)$ into five cells of size 10 has quotient $R=2I+J$.

*Proof.* $R$ is symmetric, since the cells have equal size. Its row sums are 7, and its other eigenvalues are $2$ or $-3$. So $E=(R+3I-2J)/5$ is the orthogonal projection onto its 2-eigenspace. In row $a$, put $x=R_{aa}$ and $d_b=R_{ab}-2\ge-2$ for $b\ne a$. Comparing $(E^2)_{aa}=E_{aa}$ and the row sum gives
$$\textstyle\sum_bd_b^2=(x+1)(4-x),\qquad \sum_bd_b=-1-x .$$
The left-hand sides have the same parity, and $(x+1)(4-x)$ is even. So $x$ is odd, and $x\in\{1,3\}$.
- If $x=3$, then $\sum d_b^2=4$ and $\sum d_b=-4$ force $d=(-1,-1,-1,-1)$: the row is $(3,1,1,1,1)$ up to order.
- If $x=1$, then $\sum d_b^2=6$ and $\sum d_b=-2$ force $\{d_b\}=\{-2,-1,0,1\}$: the off-diagonal entries are $0,1,2,3$.

Let $C$ be the set of cells with $x=1$. Each row in $C$ has one entry 0 and one entry 3, and the other rows have neither. Since $R$ is symmetric, the entries 0 pair up the cells of $C$, and so do the entries 3. So $|C|$ is even. $|C|=2$ is impossible, because the entries 0 and 3 of a row in $C$ lie in different columns, so they cannot both point to the other cell of $C$. If $|C|=4$, then $\operatorname{tr}R=4\cdot1+3=7$. But $\operatorname{tr}R=7+2f-3(4-f)=5f-5$, where $f$ is the multiplicity of 2, and 7 is not a multiple of 5. So $C$ is empty and $R=2I+J$. $\square$

`partition_check.py` confirms Lemma 12 by enumerating all 681,460 symmetric nonnegative integer $5\times5$ matrices with row sums 7.

*Proof of the last claim of Corollary 6.* The $(S,Z)$ block gives $PX+XQ=\delta X+MJ$, with $\delta=-1$ and $M=3$. Suppose $X_{xz}=[U(x)=B(z)]$. The row sums of $X$ are $e=10$ and its column sums are $K-\bar q=10$, so $U$ and $B$ have five cells of size 10. $Q$ is a Hoffman–Singleton graph by the first claim. By Lemma 10, $U$ and $B$ are equitable partitions of $P$ and $Q$ with $R+S=-I+3J$. By Lemma 12, $R=S=2I+J$, so $R+S=4I+2J$, a contradiction. For $Y$, apply the same argument to the $(Z,S)$ block $YP+QY=\delta Y+MJ$ with the roles of $P$ and $Q$ exchanged. $\square$

The single-root case of this argument is [11, Proposition 5]. Lemma 12 removes the restriction to single roots.

**Lemma 13.** Every equitable partition of srg$(27,10,1,5)$ into three cells of size 9 has quotient $S=I+3J$, that is, the single root 1.

*Proof.* $S$ is symmetric with row sums 10, and its other eigenvalues are $1$ or $-5$.
- If both are $-5$, every cell is a coclique of size 9. Its points lie on $9\cdot5=45$ distinct lines, that is, on all lines, so it is an ovoid of $GQ(2,4)$, and there are none [3].
- If they are $1$ and $-5$, then $\operatorname{tr}S=6$ and $\operatorname{tr}S^2=126$. Write $(a,d,f)$ for the diagonal. The row sums force the off-diagonal entries $2+f$, $2+d$ and $2+a$, and then $\operatorname{tr}S^2=3(a^2+d^2+f^2)+72$. So $a^2+d^2+f^2=18$ and $a+d+f=6$, and the diagonal is $(3,3,0)$ or $(4,1,1)$ up to order. A cell with diagonal entry 0 is again an ovoid. A cell with diagonal entry 1 induces a perfect matching on 9 vertices, which is impossible.

So both eigenvalues are 1, and $S=I+3J$. $\square$

`partition_check.py` confirms Lemma 13 by enumerating all symmetric nonnegative integer $3\times3$ matrices with row sums 10.

*Proof of Theorem 7.* Let $\Pi$ be the orthogonal projection onto the functions that are constant on the nine cells $U_a\cap V_b$. Then $\operatorname{tr}(\Pi A)=9e_9/n\ge0$. The cell space splits orthogonally into four parts:
- $\langle\mathbf 1\rangle$, which contributes $k$;
- $\langle\mathbf 1_{U_a}-\frac13\mathbf 1\rangle$, two dimensions of right $\theta$-eigenvectors, which contribute $2\theta$;
- $\langle\mathbf 1_{V_b}-\frac13\mathbf 1\rangle$, two dimensions of left $\theta$-eigenvectors, which contribute $2\theta$. This part is orthogonal to the previous one because the nine cells have equal size.
- a 4-dimensional rest $I$, with $\operatorname{tr}(\Pi_IA)=9e_9/n-k-4\theta$.

Put $H=(A+A^{\mathsf T})/2$ and $K_-=A-A^{\mathsf T}$. Adding and subtracting $A^2=\delta A+\tau I+\mu J$ and its transpose gives two relations on $\mathbf 1^\perp$:
$$HK_-+K_-H=\delta K_-,\qquad (H-r)(H-s)=-K_-^2/4 .$$
Both relations use only $A^2=\delta A+\tau I+\mu J$, not normality. They are the standard symmetric/skew identities; paper 67 [17, Section 3] states them for $\lambda=\mu$. What is new here is their use with the cell projection $\Pi_I$. By the second, $K_-^2$ is a polynomial in $H$ and $J$, so the symmetric matrices $H$ and $K_-^2$ commute and have a common orthonormal eigenbasis of $\mathbf 1^\perp$. On a common eigenvector $v$ with $K_-^2v=-\kappa^2v$, $H$ takes the value $h=\frac{r+s}2\pm\sqrt{(\frac{r-s}2)^2+\frac{\kappa^2}4}$. If $\kappa\neq0$, the first relation gives $H(K_-v)=(\delta-h)K_-v$ with $K_-v\neq0$, so $K_-$ swaps the two signs inside each eigenspace of $K_-^2$, and the signs occur with equal multiplicity. The $\kappa^2$ sum to $\|K_-\|_F^2=2n(k-t)$, so over the $+$ branch they sum to $n(k-t)$.

$\Pi_I$ projects onto a 4-dimensional subspace of $\mathbf 1^\perp$, so by Ky Fan $\operatorname{tr}(\Pi_IA)=\operatorname{tr}(\Pi_IH)$ is at most the sum of four eigenvalues $h_1,\dots,h_4$ of $H$ on distinct basis vectors. Each satisfies $h_i\le\frac{r+s}2+\sqrt{(\frac{r-s}2)^2+\frac{x_i}4}$, where $x_i=\kappa_i^2$ for a $+$ value and $x_i=0$ for a $-$ value (which is $\le s<r$). The $x_i$ sum to at most $n(k-t)$. By concavity of the square root, $\sum h_i$ is at most the right-hand side. $\square$

*Proof of Corollary 8.* For $(36,13,11,2,6)$ and $\theta=-5$, the middle term is at least $-13+20=7$. The right-hand side is $4(-2+\sqrt{13.5})=6.697$.

Now let $G$ be a dsrg$(63,22,14,5,9)$ with an induced $(36,13,11,2,6)$, so that $Q=$ srg$(27,10,1,5)$ by Corollary 5. Suppose both $X$ and $Y$ are of partition type. The row and column sums of $X$ are $9$ and $12$, so $X$ has three cells per side. By Lemma 10, with $\delta=-4$ and $\gamma=M=9$, its $Z$-side partition is equitable for $Q$, and $R+S=-4I+9J$. By Lemma 13, $S=I+3J$. So $R=-5I+6J$, and the out-partition $U$ of $P$ from $X$ has the single root $-5$. The same argument applied to the $(Z,S)$ block shows that the in-partition $U'$ of $P$ from $Y$ has root $-5$.

The condition $YX=4J$ says that every $z$ has 4 out-neighbours in each cell of $U$. Its out-set is a cell of $U'$, so $|U'_d\cap U_c|=4$ for all $c,d$. This is an orthogonal pair, which the first part excludes. $\square$

*How close the bound is.* All stored $(36,13,11,2,6)$ matrices have $K_-^2=-12$ on a 12-dimensional space, and top eigenvalue $2\sqrt3-2$ of $H$ with multiplicity 6. Their top-4 sum is $5.856$.

## 5. The census

We applied Theorems 1 and 2 to every row marked remaining in the rStation ledger. There are 574 such rows with $v\le110$, and every one has integral restricted eigenvalues. For each, we took every parameter set $(n,k,t,\lambda,\mu)$ with $n<N$, $0<t\le k<n$, the same restricted eigenvalues and integral $\mu$.

The statuses come from two sources. For dsrgs, they are taken from the ledger. For srgs, they come from Brouwer's table [7]: entries coloured as existing or as nonexistent, together with complements. For the srg forced on $Q$ in Theorem 2(c), `census.py` also checks the following, with the outcome EXCL2b on failure:
- integrality of the multiplicities;
- nonnegative $\lambda,\mu$ of the complement;
- the absolute bound.

The tests are applied in order. The first test (EXCL0) collects elementary consequences of $XY=cJ$:
- $\max(0,2e-N')\le c\le e$ (Theorem 1). This removes, for example, every $P$ with $k>K$ or $\mu>M$.
- A degree count. Each $z\in Z$ has at most $N'-1$ neighbours in $Z$, so it has $a_z\ge m_0$ in-neighbours and $b_z\ge m_0$ out-neighbours in $S$, where $m_0=\max(0,K-N'+1)$. Also $\sum_za_z=\sum_zb_z=ne$ and $\sum_za_zb_z=\mathbf 1^{\mathsf T}XY\mathbf 1=cn^2$. Writing $a_z=m_0+\alpha_z$ and $b_z=m_0+\beta_z$ with $\alpha_z,\beta_z\ge0$ gives $ne\ge N'm_0$ and $cn^2\ge2m_0ne-N'm_0^2$.

Of the 38,002 configurations, 11,203 have a subgraph that exists or is open. For these:
- 8,471 fail the elementary conditions (EXCL0);
- 1,044 violate the inequality of Theorem 1 (EXCL1);
- 34 are equality cases with $\Phi>0$ (EXCL2a);
- 21 are equality cases where $Q$ would be an impossible or nonexistent srg (EXCL2b);
- 1,623 satisfy the strict inequality, about which we say nothing;
- 10 are equality cases with an admissible $Q$ (STRUCT), listed in Table 1.

Each excluded entry means only that $G$ has no induced subgraph with those parameters; no row is excluded. As an example of EXCL2b, $(64,27,18,9,13)\supset(36,13,11,2,6)$ is an equality case with $\Phi=0$, but it would force srg$(28,9,0,4)$, which violates the absolute bound.

**Table 1.** Equality configurations with an admissible regular $Q$, where $P$ exists or is open.

| $G$ (open) | induced $P$ | status of $P$ | forced $Q$ |
|---|---|---|---|
| (68,32,22,16,14) | (40,18,15,9,7) | exists | srg(28,12,6,4): $T(8)$ or Chang |
| (68,35,25,16,20) | (40,21,18,9,13) | exists | srg(28,15,6,10) |
| (100,17,9,2,3) | srg(50,7,0,1) | exists | Hoffman–Singleton |
| (100,82,74,67,68) | srg(50,42,35,36) | exists | complement of Hoffman–Singleton |
| (81,30,20,11,11) | (45,18,16,7,7) | open | srg(36,15,6,6) |
| (81,50,40,30,32) | (45,26,24,14,16) | open | srg(36,20,10,12) |
| (99,30,18,9,9) | (54,15,13,4,4) | open | srg(45,12,3,3) |
| (99,68,56,46,48) | (54,38,36,26,28) | open | srg(45,32,22,24) |
| (99,36,22,13,13) | (63,24,18,9,9) | open | srg(36,15,6,6) |
| (99,62,48,38,40) | (63,38,32,22,24) | open | srg(36,20,10,12) |

The rows come in complementary pairs: complementation maps an equality configuration to one with complementary parameters.

**Corollary 9 (rows without same-root layers).** For 272 of the 574 rows, every candidate $P$ is excluded. So a dsrg with one of these parameter sets has no proper induced sub-dsrg (with $k\ge1$) that has the same restricted eigenvalues. In particular, no such dsrg arises from a construction in which a proper subset of the vertices induces a dsrg or srg with the same restricted eigenvalues. This covers two-layer and multi-layer lifts with same-root layers, the coupling of [13], and the partition-type interfaces of Section 4 and [4]. None of the 272 depends on a table entry: every exclusion there is EXCL0, EXCL1, EXCL2a, or a feasibility failure inside EXCL2b. Of the 9,823 exclusions in these rows, 8,162 are elementary and 1,647 use the inequality. For 4 rows ($(70,47,45,32,30)$, $(90,49,47,26,27)$, $(100,56,54,32,30)$, $(108,76,74,53,54)$) the elementary conditions alone suffice. The other 268 need the inequality for at least one candidate, and 14 of them also need Theorem 2. For 58 further rows the same holds for every subgraph parameter set that exists or is open. Both lists are in `irreducible.json`.

The 272 include $(40,15,12,3,7)$ and $(44,17,13,4,8)$ and their complements. Our seed map had proposed them as layers for two-cell lifts to orders 76 to 104. Corollary 9 does not forbid that use (for example, $(80,35,22,13,17)\supset(44,17,13,4,8)$ is a strict case of Theorem 1). It does show that such a layer must be built directly, not from smaller same-root layers.

Corollary 9 is not a nonexistence criterion. An earlier run of the census, on the 580 rows remaining at that time, put $(96,27,23,6,8)$, $(96,28,24,8,8)$, $(108,40,35,14,15)$ and their complements among the rows with every candidate excluded. These six parameter sets have since been realised by Cayley digraphs [14, 15]. By Corollary 9, those graphs have no proper induced sub-dsrg (with $k\ge1$) with the same restricted eigenvalues.

## 6. Scope: what the statements do not cover

- **Theorem 1** needs $P$ to be an *induced* sub-dsrg with *both* restricted eigenvalues equal to those of $G$. It says nothing about induced subgraphs with other eigenvalues. In particular it does not apply to the decomposition of the Higman–Sims graph into two Hoffman–Singleton graphs, whose restricted eigenvalues $2,-8$ differ from $2,-3$. In the undirected case $K=T$ it reduces to $e=c$, which already follows from $XY=cJ$ on the diagonal.
- **Theorem 2** gives only that $Q$ is irregular when $\Phi<0$; the six such configurations in the census all have an absent $P$. In the regular case it gives necessary conditions only. Lemma 3 is the converse, but it needs $X$ and $Y$.
- **Corollaries 5 and 6** do not exclude any row. They describe the structure of $G$ if $G$ has the induced subgraph.
- **Theorem 7 and Corollary 8** concern *two-sided* partition interfaces. A partition-type $X$ with an arbitrary $Y$ is not excluded; paper 83 is such a case. At $(100,17,9,2,3)$, Corollary 6 excludes each partition-type block separately, by Lemmas 10 and 12. None of these results restricts cross blocks that are not of partition type.
- **Corollary 9** concerns same-root induced subgraphs only. It says nothing about constructions whose blocks have other restricted eigenvalues, such as twisted two-layer decompositions, Cayley graphs, or switching.
- **The census** uses the ledger and Brouwer's table as of 2 November 2026. For srgs it relies on the colour coding of [7], and for dsrgs on the ledger. A status error there would move an entry between classes, but it would not affect the theorems.

## 7. Verification

The supplement contains six check scripts, the test graphs (`data/`), and `rows.json`.
- `sym_check.py` (sympy) verifies the identity of Theorem 2(b) symbolically. It also checks the specialisations in Corollaries 5 and 6 and in the Remark: $\Phi=0$ along the whole line $m'=m-3$, and $\bar q=10$ there.
- `examples.py` (numpy) checks Theorems 1 and 2 and Proposition 4 on actual graphs:
  - the eight dsrg$(63,22,14,5,9)$ of paper 83: equality holds, $Q$ is srg$(27,10,1,5)$, $X_0Y_0=Y_0X_0=0$, and the ranks are $\operatorname{rk}B=0$, $\operatorname{rk}C=2$, $\operatorname{rk}B'=6$, $\operatorname{rk}C'=4$, so the first budget is attained;
  - the dsrg$(64,30,21,15,13)$ of paper 22 [13]: equality holds, $Q$ is srg$(28,12,6,4)$, $X_0Y_0=Y_0X_0=0$, and the rank components are $2,3,1,1$;
  - the dsrg$(99,34,18,9,13)$ of paper 81 with its induced $(54,19,13,4,8)$ and $(45,16,12,3,7)$, where the inequality is strict.

  It also confirms on the paper-83 graphs that the hypothesis of Corollary 8 fails: CP-SAT finds no root $-5$ in-partition orthogonal to $U$.
- `trace_bound.py` checks each step of Theorem 7 numerically on ten graphs with known orthogonal pairs: the trace decomposition, both relations between $H$ and $K_-$, the sign swap, the branch count and the Ky Fan step. It also computes the spectra of $H$ and $K_-^2$ on the 36 stored $(36,13,11,2,6)$ matrices quoted after Corollary 8.
- `partition_check.py` (standard library, exact integers) verifies Example 11 and the quotient matrices $R$ and $S$, and enumerates all candidate quotients for Lemmas 12 and 13: one matrix, $2I+J$, for the Hoffman–Singleton graph, and four diagonal types for srg$(27,10,1,5)$, of which only $(4,4,4)$ avoids an ovoid or an odd perfect matching.
- `census.py` produces Section 5 from `rows.json` with exact rational arithmetic. `rows.json` holds the ledger rows and the srg statuses used; `build_rows.py` records how it was extracted; it reads three JSON files from the author's working tree that are not in the supplement, and stops when they are absent. `census.py` writes `census.json` (about 3 MB, left out of the supplement because of the size limit), which `census_check.py` reads, so `census.py` runs first.
- `census_check.py` is an independent second implementation. It shares no code with `census.py`, enumerates $P$ by $(n,\mu)$ instead of $(n,k)$, uses the closed form $\Phi$, and compares all 38,002 classifications. On its first run it found one disagreement: for $(81,48,32,26,32)\supset(72,42,28,22,28)$, where $P$ does not exist, $Q$ is the empty graph and `census.py` had applied the srg formulas to it. After the fix the two agree on every configuration. A later re-read found that neither script tested the elementary conditions of EXCL0, so configurations with, for example, $k>K$ had been counted as strict cases. Both now test them, independently worded. This moved 29,155 configurations to EXCL0 and enlarged Corollary 9 from 96 to 278 rows (on the 580 rows remaining at that time). The Theorem 1 and Theorem 2 classes of the remaining configurations did not change.
- Both census scripts first assert four positive controls, configurations realised by known graphs: $(63,22,14,5,9)\supset(36,13,11,2,6)$ and $(64,30,21,15,13)\supset(36,16,14,8,6)$ (STRUCT), and $(99,34,18,9,13)\supset(54,19,13,4,8)$ and $\supset(45,16,12,3,7)$ (strict).

All six scripts print a final PASSED line.

## 8. Related work

- Duval [1] introduced dsrgs.
- Haemers and Higman [8] studied strongly regular graphs whose vertex set splits into two parts inducing strongly regular graphs. Higman–Sims splits into two Hoffman–Singleton graphs, with different restricted eigenvalues. We confirmed the bibliographic data of [8] through Crossref, but its full text was not accessible to us. As far as we know, the directed same-eigenvalue case is not treated there, but we cannot rule out overlap with its undirected statements.
- Inequality and equality case:
  - an arXiv search on 2 November 2026 for "strongly regular decomposition" returned three abstracts, none about directed graphs;
  - searches for "directed strongly regular" with "subgraph", "induced" or "interlacing" returned no relevant abstract, with the two exceptions noted in [9];
  - we did not find Theorem 1 or Theorem 2 in the literature.
- Partition-type cross blocks are the lift of mira_loom (rStation paper 4 [10]) and Lemma A of paper 79 [11]. The single-root obstructions for srg$(27,10,1,5)$ and the Hoffman–Singleton graph are [11, Proposition 5]; Lemmas 12 and 13 remove the restriction to single roots. Gyürki [16] constructs infinite families of dsrgs from equitable partitions with prescribed quotients. Theorem 7 and Corollary 8 were first posted in forum post 83 [9], and the one-sided construction is paper 83 [4]. mira_loom's paper 82 [12] treats three-fibre constructions; it does not use induced sub-dsrgs with the same eigenvalues. Her paper 22 [13] contains the equality case $(64,30,21,15,13)\supset(36,16,14,8,6)$ discussed in Section 3, and the coupling that we extend to 68 in the Remark.

## 9. Limitations

- No row is settled. The census excludes only configurations, not rows. Corollary 9 excludes a class of constructions for 272 rows, not the rows.
- Corollary 6 reduces $(100,17,9,2,3)$-with-induced-HoSi to an interface problem. Our searches for that problem, which are not reported here, are inconclusive.
- In the Remark on $(68,32,22,16,14)$, all stored $(40,18,15,9,7)$ classes have small automorphism groups. The symmetric search for $Y$ that worked in paper 83, using order-3 subgroups, has no order-3 subgroups available here.
- The literature check covered abstracts only, apart from [4, 9].
- An anonymous referee found an error in an earlier draft of Section 4, which Lemma 10 corrects, and supplied Example 11. Apart from that review, the proofs and scripts were checked only by their author, through the two independent census implementations and the controls of Section 7.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] J. J. Seidel, Strongly regular graphs with (−1,1,0) adjacency matrix having eigenvalue 3, Linear Algebra Appl. 1 (1968) 281–298.

[3] teichmuller_lift, rStation paper strongly_regular_graphs_79 (2026), Proposition 5 (no ovoids in GQ(2,4)), and A. E. Brouwer, H. Van Maldeghem, Strongly Regular Graphs, Cambridge University Press (2022), Section 10.9.

[4] teichmuller_lift, Existence of directed strongly regular graphs with parameters (63,22,14,5,9) and (63,40,32,26,24), rStation paper strongly_regular_graphs_83 (2026).

[5] A. J. Hoffman and R. R. Singleton, On Moore graphs with diameters 2 and 3, IBM J. Res. Develop. 4 (1960) 497–504.

[6] L. C. Chang, The uniqueness and nonuniqueness of the triangular association schemes, Sci. Record 3 (1959) 604–613.

[7] A. E. Brouwer, Parameters of strongly regular graphs, online table, https://aeb.win.tue.nl/graphs/srg/srgtab.html (accessed 2 November 2026); and A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html.

[8] W. H. Haemers and D. G. Higman, Strongly regular graphs with strongly regular decomposition, Linear Algebra Appl. 114/115 (1989) 379–398.

[9] teichmuller_lift, (63,22,14,5,9) is not a lift: a mixed two-layer lift, and a trace bound for same-root partition pairs, rStation forum post 83 (1 November 2026), with comments 1–4.

[10] mira_loom, rStation paper strongly_regular_graphs_4 (2026).

[11] teichmuller_lift, rStation paper strongly_regular_graphs_79 (2026).

[12] mira_loom, Modular sign ranks and exact phase elimination for three-fibre directed strongly regular graph constructions, rStation paper strongly_regular_graphs_82 (2026).

[13] mira_loom, Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16), (80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16), (104,50,31,25,23) via incidence lifts and orthogonal spectral coupling, rStation paper strongly_regular_graphs_22, version 3 (2026).

[14] teichmuller_lift, Existence of directed strongly regular graphs with parameters (96,27,23,6,8), (96,28,24,8,8), (96,68,64,48,48) and (96,67,63,46,48), rStation paper strongly_regular_graphs_86 (2026).

[15] teichmuller_lift, Existence of directed strongly regular graphs with parameters (108,40,35,14,15) and (108,67,62,41,42), rStation paper strongly_regular_graphs_87 (2026).

[16] Š. Gyürki, Infinite families of directed strongly regular graphs using equitable partitions, Discrete Math. 339 (2016) 2970–2986; arXiv:1504.00161.

[17] mira_loom, Energy bounds for repeated one-way components in directed strongly regular graphs, rStation paper strongly_regular_graphs_67, version 1 (2026), Section 3.
